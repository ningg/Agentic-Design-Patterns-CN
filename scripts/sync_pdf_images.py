from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


IMAGE_PATTERN = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<ref>[^)]+)\)")


@dataclass(frozen=True)
class MarkdownImageSlot:
    md_path: Path
    chapter_key: str
    index_in_doc: int
    alt_text: str
    original_markdown: str
    original_reference: str
    filename: str
    before_text: str
    after_text: str
    target_reference: str
    heading_text: str = ""


@dataclass(frozen=True)
class PdfImageCandidate:
    candidate_id: str
    page_number: int
    chapter_key: str
    order_in_chapter: int
    before_text: str
    after_text: str
    caption_text: str
    image_bytes: bytes
    image_ext: str


@dataclass(frozen=True)
class ImageMatch:
    slot: MarkdownImageSlot
    candidate_id: str
    method: str
    score: float
    page_number: int
    image_bytes: bytes
    image_ext: str
    reason: str


@dataclass(frozen=True)
class MarkdownDocument:
    md_path: Path
    chapter_key: str
    heading_text: str
    slot_count: int


def _natural_sort_key(text: str) -> list[object]:
    parts = re.split(r"(\d+)", text)
    key: list[object] = []
    for part in parts:
        if not part:
            continue
        key.append(int(part) if part.isdigit() else part.lower())
    return key


def _path_sort_key(path: Path, base_dir: Path) -> tuple[int, list[object]]:
    relative = path.relative_to(base_dir)
    flattened: list[object] = []
    for part in relative.parts:
        flattened.extend(_natural_sort_key(part))
    return len(relative.parts), flattened


def normalize_text(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    normalized = normalized.encode("ascii", "ignore").decode("ascii")
    normalized = normalized.lower().replace("_", " ")
    normalized = re.sub(r"[^a-z0-9]+", " ", normalized)
    return " ".join(normalized.split())


def build_target_reference(md_path: Path, en_dir: Path, filename: str) -> str:
    relative_file = md_path.relative_to(en_dir)
    depth = len(relative_file.parents) - 1
    prefix = "../" * depth
    return f"{prefix}assets-new/{filename}"


def _first_heading(lines: list[str]) -> str:
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
    return ""


def _anchor_text(lines: list[str], start_index: int, step: int, limit: int = 2) -> str:
    collected: list[str] = []
    index = start_index
    while 0 <= index < len(lines) and len(collected) < limit:
        stripped = lines[index].strip()
        if stripped and not IMAGE_PATTERN.search(stripped):
            collected.append(stripped)
        index += step
    if step < 0:
        collected.reverse()
    return " ".join(collected)


def collect_markdown_slots(en_dir: Path) -> list[MarkdownImageSlot]:
    slots: list[MarkdownImageSlot] = []
    md_paths = sorted(en_dir.rglob("*.md"), key=lambda path: _path_sort_key(path, en_dir))
    for md_path in md_paths:
        lines = md_path.read_text(encoding="utf-8").splitlines()
        heading = _first_heading(lines)
        chapter_key = str(md_path.relative_to(en_dir).with_suffix(""))
        slot_index = 0
        for line_number, line in enumerate(lines):
            for match in IMAGE_PATTERN.finditer(line):
                reference = match.group("ref").strip()
                filename = Path(reference).name.strip()
                slots.append(
                    MarkdownImageSlot(
                        md_path=md_path,
                        chapter_key=chapter_key,
                        index_in_doc=slot_index,
                        alt_text=match.group("alt").strip(),
                        original_markdown=match.group(0),
                        original_reference=reference,
                        filename=filename,
                        before_text=_anchor_text(lines, line_number - 1, -1),
                        after_text=_anchor_text(lines, line_number + 1, 1),
                        target_reference=build_target_reference(md_path, en_dir, filename),
                        heading_text=heading,
                    )
                )
                slot_index += 1
    return slots


def collect_markdown_documents(slots: Iterable[MarkdownImageSlot]) -> list[MarkdownDocument]:
    grouped: dict[Path, list[MarkdownImageSlot]] = {}
    for slot in slots:
        grouped.setdefault(slot.md_path, []).append(slot)
    documents: list[MarkdownDocument] = []
    for md_path, md_slots in grouped.items():
        documents.append(
            MarkdownDocument(
                md_path=md_path,
                chapter_key=md_slots[0].chapter_key,
                heading_text=md_slots[0].heading_text,
                slot_count=len(md_slots),
            )
        )
    return documents


def _token_overlap(left: str, right: str) -> float:
    left_tokens = set(normalize_text(left).split())
    right_tokens = set(normalize_text(right).split())
    if not left_tokens or not right_tokens:
        return 0.0
    return len(left_tokens & right_tokens) / len(left_tokens)


def _score_slot_candidate(slot: MarkdownImageSlot, candidate: PdfImageCandidate) -> tuple[float, str]:
    before_score = max(
        _token_overlap(slot.before_text, candidate.before_text),
        _token_overlap(slot.before_text, candidate.after_text),
    )
    after_score = max(
        _token_overlap(slot.after_text, candidate.after_text),
        _token_overlap(slot.after_text, candidate.caption_text),
        _token_overlap(slot.after_text, candidate.before_text),
    )
    alt_score = max(
        _token_overlap(slot.alt_text, candidate.caption_text),
        _token_overlap(slot.alt_text, candidate.after_text),
    )
    total = before_score * 0.35 + after_score * 0.45 + alt_score * 0.20
    reason = (
        f"before={before_score:.3f}, after={after_score:.3f}, alt={alt_score:.3f}"
    )
    return total, reason


def match_slots_to_candidates(
    slots: list[MarkdownImageSlot],
    candidates: list[PdfImageCandidate],
    minimum_context_score: float = 0.35,
) -> list[ImageMatch]:
    candidates_by_chapter: dict[str, list[PdfImageCandidate]] = defaultdict(list)
    for candidate in candidates:
        candidates_by_chapter[candidate.chapter_key].append(candidate)
    for chapter_candidates in candidates_by_chapter.values():
        chapter_candidates.sort(key=lambda item: (item.order_in_chapter, item.page_number))

    matches: list[ImageMatch] = []
    for chapter_key, chapter_slots in defaultdict(list, ((slot.chapter_key, []) for slot in slots)).items():
        pass
    slots_by_chapter: dict[str, list[MarkdownImageSlot]] = defaultdict(list)
    for slot in slots:
        slots_by_chapter[slot.chapter_key].append(slot)

    for chapter_key, chapter_slots in slots_by_chapter.items():
        ordered_slots = sorted(chapter_slots, key=lambda item: item.index_in_doc)
        available = list(candidates_by_chapter.get(chapter_key, []))
        used_ids: set[str] = set()
        pending_slots: list[MarkdownImageSlot] = []

        for slot in ordered_slots:
            scored: list[tuple[float, str, PdfImageCandidate]] = []
            for candidate in available:
                if candidate.candidate_id in used_ids:
                    continue
                score, reason = _score_slot_candidate(slot, candidate)
                scored.append((score, reason, candidate))
            scored.sort(key=lambda item: item[0], reverse=True)
            if scored and scored[0][0] >= minimum_context_score:
                score, reason, candidate = scored[0]
                used_ids.add(candidate.candidate_id)
                matches.append(
                    ImageMatch(
                        slot=slot,
                        candidate_id=candidate.candidate_id,
                        method="context",
                        score=score,
                        page_number=candidate.page_number,
                        image_bytes=candidate.image_bytes,
                        image_ext=candidate.image_ext,
                        reason=reason,
                    )
                )
            else:
                pending_slots.append(slot)

        remaining_candidates = [
            candidate for candidate in available if candidate.candidate_id not in used_ids
        ]
        for slot, candidate in zip(
            pending_slots,
            sorted(remaining_candidates, key=lambda item: (item.order_in_chapter, item.page_number)),
        ):
            score, reason = _score_slot_candidate(slot, candidate)
            matches.append(
                ImageMatch(
                    slot=slot,
                    candidate_id=candidate.candidate_id,
                    method="fallback_order",
                    score=score,
                    page_number=candidate.page_number,
                    image_bytes=candidate.image_bytes,
                    image_ext=candidate.image_ext,
                    reason=reason,
                )
            )

    matches.sort(key=lambda item: (str(item.slot.md_path), item.slot.index_in_doc))
    return matches


def rewrite_markdown(
    content: str,
    slots: list[MarkdownImageSlot],
    matches: list[ImageMatch],
) -> str:
    matched_slots = {match.slot: match for match in matches}
    rewritten = content
    for slot in slots:
        if slot not in matched_slots:
            continue
        updated = f"![{slot.alt_text}]({slot.target_reference})"
        rewritten = rewritten.replace(slot.original_markdown, updated, 1)
    return rewritten


def rewrite_markdown_files(en_dir: Path, slots: list[MarkdownImageSlot], matches: list[ImageMatch]) -> None:
    slots_by_path: dict[Path, list[MarkdownImageSlot]] = defaultdict(list)
    for slot in slots:
        slots_by_path[slot.md_path].append(slot)

    matches_by_path: dict[Path, list[ImageMatch]] = defaultdict(list)
    for match in matches:
        matches_by_path[match.slot.md_path].append(match)

    for md_path, md_slots in slots_by_path.items():
        rewritten = rewrite_markdown(
            md_path.read_text(encoding="utf-8"),
            md_slots,
            matches_by_path.get(md_path, []),
        )
        md_path.write_text(rewritten, encoding="utf-8")


def write_extracted_assets(output_dir: Path, matches: list[ImageMatch]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for match in matches:
        output_path = output_dir / match.slot.filename
        output_path.write_bytes(match.image_bytes)


def _import_fitz():
    try:
        import fitz  # type: ignore
    except ImportError as exc:  # pragma: no cover - exercised in runtime only
        raise RuntimeError(
            "PyMuPDF is required. Install it with `python3 -m pip install --user pymupdf`."
        ) from exc
    return fitz


def _find_document_start_pages(
    documents: list[MarkdownDocument],
    page_texts: list[str],
) -> dict[str, int]:
    starts: dict[str, int] = {}
    search_start = 0
    for document in documents:
        title = normalize_text(document.heading_text)
        if not title:
            starts[document.chapter_key] = search_start
            continue

        exact_hits: list[int] = []
        best_page = search_start
        best_score = 0.0
        title_tokens = set(title.split())
        for page_number in range(search_start, len(page_texts)):
            page_text = page_texts[page_number]
            if title in page_text:
                exact_hits.append(page_number)
            page_tokens = set(page_text.split())
            if not page_tokens:
                continue
            score = len(title_tokens & page_tokens) / max(1, len(title_tokens))
            if score > best_score:
                best_score = score
                best_page = page_number
        chosen_page = None
        for hit in exact_hits:
            if hit > search_start + 1:
                chosen_page = hit
                break
        if chosen_page is None and exact_hits:
            chosen_page = exact_hits[0]
        starts[document.chapter_key] = chosen_page if chosen_page is not None else best_page
        search_start = starts[document.chapter_key]
    return starts


def _extract_png_bytes(doc, xref: int) -> bytes:
    fitz = _import_fitz()
    pixmap = fitz.Pixmap(doc, xref)
    if pixmap.n - pixmap.alpha > 3:
        pixmap = fitz.Pixmap(fitz.csRGB, pixmap)
    return pixmap.tobytes("png")


def _nearby_text(blocks: list[tuple[float, float, str]], y0: float, y1: float) -> tuple[str, str, str]:
    above = [block for block in blocks if block[1] <= y0 + 2]
    below = [block for block in blocks if block[0] >= y1 - 2]
    above_text = " ".join(block[2] for block in above[-2:])
    below_text_blocks = below[:2]
    below_text = " ".join(block[2] for block in below_text_blocks)
    caption = below_text_blocks[0][2] if below_text_blocks else ""
    return above_text, caption, below_text


def extract_pdf_candidates(pdf_path: Path, documents: list[MarkdownDocument]) -> list[PdfImageCandidate]:
    fitz = _import_fitz()
    doc = fitz.open(pdf_path)
    page_texts = [normalize_text(page.get_text("text")) for page in doc]
    start_pages = _find_document_start_pages(documents, page_texts)

    ordered_documents = sorted(documents, key=lambda item: start_pages.get(item.chapter_key, 0))
    candidates: list[PdfImageCandidate] = []

    for doc_index, document in enumerate(ordered_documents):
        start_page = start_pages.get(document.chapter_key, 0)
        next_start = (
            start_pages.get(ordered_documents[doc_index + 1].chapter_key, doc.page_count)
            if doc_index + 1 < len(ordered_documents)
            else doc.page_count
        )
        order_in_chapter = 0
        for page_number in range(start_page, next_start):
            page = doc[page_number]
            text_blocks = [
                (block[1], block[3], block[4].strip())
                for block in page.get_text("blocks")
                if len(block) >= 7 and int(block[6]) == 0 and block[4].strip()
            ]
            text_blocks.sort(key=lambda item: item[0])

            for image_info in page.get_images(full=True):
                xref = image_info[0]
                rects = page.get_image_rects(xref)
                if not rects:
                    continue
                image_bytes = _extract_png_bytes(doc, xref)
                for rect_index, rect in enumerate(rects):
                    if rect.width < 80 or rect.height < 80:
                        continue
                    before_text, caption_text, after_text = _nearby_text(
                        text_blocks,
                        rect.y0,
                        rect.y1,
                    )
                    candidates.append(
                        PdfImageCandidate(
                            candidate_id=f"page{page_number + 1}-xref{xref}-rect{rect_index}",
                            page_number=page_number + 1,
                            chapter_key=document.chapter_key,
                            order_in_chapter=order_in_chapter,
                            before_text=before_text,
                            after_text=after_text,
                            caption_text=caption_text,
                            image_bytes=image_bytes,
                            image_ext="png",
                        )
                    )
                    order_in_chapter += 1

    return candidates


def write_report(
    report_path: Path,
    slots: list[MarkdownImageSlot],
    candidates: list[PdfImageCandidate],
    matches: list[ImageMatch],
) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    matched_by_slot = {match.slot: match for match in matches}
    payload = {
        "slot_count": len(slots),
        "candidate_count": len(candidates),
        "matched_count": len(matches),
        "unmatched_count": len(slots) - len(matches),
        "matches": [
            {
                "md_path": str(match.slot.md_path),
                "filename": match.slot.filename,
                "page_number": match.page_number,
                "method": match.method,
                "score": round(match.score, 4),
                "reason": match.reason,
                "target_reference": match.slot.target_reference,
            }
            for match in matches
        ],
        "unmatched": [
            {
                "md_path": str(slot.md_path),
                "filename": slot.filename,
                "before_text": slot.before_text,
                "after_text": slot.after_text,
            }
            for slot in slots
            if slot not in matched_by_slot
        ],
    }
    report_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def run(repo_root: Path) -> dict[str, int]:
    en_dir = repo_root / "en"
    pdf_path = repo_root / "pdf" / "Agentic-Design-Patterns.pdf"
    output_dir = en_dir / "assets-new"
    report_path = repo_root / "reports" / "pdf-image-sync-report.json"

    slots = collect_markdown_slots(en_dir)
    documents = collect_markdown_documents(slots)
    candidates = extract_pdf_candidates(pdf_path, documents)
    matches = match_slots_to_candidates(slots, candidates)

    write_extracted_assets(output_dir, matches)
    rewrite_markdown_files(en_dir, slots, matches)
    write_report(report_path, slots, candidates, matches)

    return {
        "slot_count": len(slots),
        "candidate_count": len(candidates),
        "matched_count": len(matches),
        "unmatched_count": len(slots) - len(matches),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract PDF images and sync markdown references.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root containing en/ and pdf/ directories.",
    )
    args = parser.parse_args()
    summary = run(args.repo_root.resolve())
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
