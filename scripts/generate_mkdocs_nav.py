#!/usr/bin/env python3
"""Generate MkDocs nav entries from cn/**/*.md."""

from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CN_DIR = ROOT / "cn"
MKDOCS_YML = ROOT / "mkdocs.yml"
START_MARKER = "  # AUTO_NAV_START"
END_MARKER = "  # AUTO_NAV_END"
OTHERS_FILES = [
    "publics_as_website_mkdocs.md",
    "Agentic_Design_Patterns.md",
    "Conclusion.md",
    "Glossary.md",
    "Index_of_Terms.md",
    "LICENSE.md",
    "Online_Contribution-Frequently_Asked_Questions_Agentic_Design_Patterns.md",
]


def natural_sort_key(value: str) -> list[object]:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", value)]


def strip_numeric_prefix(name: str) -> str:
    return re.sub(r"^\d+[-_ ]*", "", name)


def to_readable_title(path: Path) -> str:
    stem = path.stem
    if stem.lower() == "readme":
        return "首页"
    return strip_numeric_prefix(stem).replace("_", " ").strip()


def markdown_files() -> list[Path]:
    files = sorted(CN_DIR.rglob("*.md"), key=lambda p: natural_sort_key(p.relative_to(CN_DIR).as_posix()))
    return [f for f in files if f.is_file()]


def nav_item_for_file(path: Path) -> str:
    rel = path.relative_to(CN_DIR).as_posix()
    title = to_readable_title(path)
    return f"{title}: {rel}"


def folder_label(folder_name: str) -> str:
    return strip_numeric_prefix(folder_name).replace("_", " ").strip()


def yaml_line(indent: int, text: str) -> str:
    return f'{" " * indent}- {text}'


def build_folder_entries(folder: Path, indent: int = 2) -> list[str]:
    lines: list[str] = []
    others_paths = {CN_DIR / name for name in OTHERS_FILES}

    files = sorted(
        [p for p in folder.glob("*.md") if p.is_file() and p.name.lower() != "readme.md"],
        key=lambda p: natural_sort_key(p.name),
    )
    for file in files:
        if file in others_paths:
            continue
        lines.append(yaml_line(indent, nav_item_for_file(file)))

    subdirs = sorted([p for p in folder.iterdir() if p.is_dir()], key=lambda p: natural_sort_key(p.name))
    for subdir in subdirs:
        sub_entries = build_folder_entries(subdir, indent + 2)
        if not sub_entries:
            continue
        lines.append(yaml_line(indent, f"{folder_label(subdir.name)}:"))
        lines.extend(sub_entries)

    return lines


def build_nav_lines(files: list[Path]) -> list[str]:
    lines: list[str] = []
    top_readme = CN_DIR / "README.md"
    others_paths = {CN_DIR / name for name in OTHERS_FILES}

    if top_readme in files:
        lines.append(yaml_line(2, nav_item_for_file(top_readme)))

    lines.extend(build_folder_entries(CN_DIR, indent=2))

    existing_others = [CN_DIR / name for name in OTHERS_FILES if (CN_DIR / name) in files]
    if existing_others:
        lines.append(yaml_line(2, "Others:"))
        for file in existing_others:
            lines.append(yaml_line(4, nav_item_for_file(file)))

    return lines


def inject_nav_block(mkdocs_text: str, nav_lines: list[str]) -> str:
    lines = mkdocs_text.splitlines()
    try:
        start_idx = lines.index(START_MARKER)
        end_idx = lines.index(END_MARKER)
    except ValueError as exc:
        raise SystemExit("mkdocs.yml is missing AUTO_NAV markers.") from exc

    if end_idx <= start_idx:
        raise SystemExit("AUTO_NAV markers are in invalid order.")

    new_lines = lines[: start_idx + 1] + nav_lines + lines[end_idx:]
    return "\n".join(new_lines) + "\n"


def main() -> None:
    if not MKDOCS_YML.exists():
        raise SystemExit("mkdocs.yml not found.")

    files = markdown_files()
    if not files:
        raise SystemExit("No markdown files found under cn/.")

    nav_lines = build_nav_lines(files)
    current = MKDOCS_YML.read_text(encoding="utf-8")
    updated = inject_nav_block(current, nav_lines)
    MKDOCS_YML.write_text(updated, encoding="utf-8")
    print(f"Updated nav with {len(files)} markdown files.")


if __name__ == "__main__":
    main()
