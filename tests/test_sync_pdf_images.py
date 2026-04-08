import importlib.util
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


def load_module():
    module_path = (
        Path(__file__).resolve().parents[1] / "scripts" / "sync_pdf_images.py"
    )
    spec = importlib.util.spec_from_file_location("sync_pdf_images", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class MarkdownSlotTests(unittest.TestCase):
    def test_collect_markdown_slots_parses_supported_path_shapes(self):
        sync = load_module()

        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            (repo / "en" / "01-Part_One").mkdir(parents=True)
            (repo / "en" / "Agentic.md").write_text(
                textwrap.dedent(
                    """\
                    # Root

                    Intro line.
                    ![Cover](assets/Cover.png)
                    After line.
                    """
                ),
                encoding="utf-8",
            )
            (repo / "en" / "01-Part_One" / "Chapter.md").write_text(
                textwrap.dedent(
                    """\
                    # Chapter 1

                    Before the first figure.
                    ![Figure A](../assets/Figure_A.png)
                    Fig.1: Figure A

                    Before the second figure.
                    ![Figure B](Bare_Figure.png)
                    Fig.2: Figure B

                    Before the third figure.
                    ![Figure C](../assests/Figure_C.png)
                    Fig.3: Figure C
                    """
                ),
                encoding="utf-8",
            )

            slots = sync.collect_markdown_slots(repo / "en")

        self.assertEqual(len(slots), 4)
        self.assertEqual(slots[0].filename, "Cover.png")
        self.assertEqual(slots[0].target_reference, "assets-new/Cover.png")
        self.assertEqual(slots[1].filename, "Figure_A.png")
        self.assertEqual(slots[1].target_reference, "../assets-new/Figure_A.png")
        self.assertEqual(slots[2].filename, "Bare_Figure.png")
        self.assertEqual(slots[2].target_reference, "../assets-new/Bare_Figure.png")
        self.assertEqual(slots[3].filename, "Figure_C.png")
        self.assertIn("Before the third figure.", slots[3].before_text)

    def test_normalize_text_removes_noise(self):
        sync = load_module()

        text = " Fig. 1:  Prioritization Design Pattern  \n\n(see Fig. 1) "
        self.assertEqual(
            sync.normalize_text(text),
            "fig 1 prioritization design pattern see fig 1",
        )


class MatchingTests(unittest.TestCase):
    def test_match_slots_prefers_context_over_order(self):
        sync = load_module()

        slot = sync.MarkdownImageSlot(
            md_path=Path("en/chapter.md"),
            chapter_key="chapter-1",
            index_in_doc=0,
            alt_text="Some Examples of an Agent Using Tool",
            original_markdown="![Some Examples](Some_Examples.png)",
            original_reference="Some_Examples.png",
            filename="Some_Examples.png",
            before_text="Tool Use transforms a language model from a text generator.",
            after_text="Fig.1: Some examples of an Agent using Tools",
            target_reference="../assets-new/Some_Examples.png",
        )

        strong = sync.PdfImageCandidate(
            candidate_id="page10-img1",
            page_number=10,
            chapter_key="chapter-1",
            order_in_chapter=1,
            before_text="Tool Use transforms a language model from a text generator into an agent.",
            after_text="Fig.1: Some examples of an Agent using Tools",
            caption_text="Some examples of an Agent using Tools",
            image_bytes=b"good",
            image_ext="png",
        )
        weak = sync.PdfImageCandidate(
            candidate_id="page10-img2",
            page_number=10,
            chapter_key="chapter-1",
            order_in_chapter=0,
            before_text="Unrelated content",
            after_text="Different caption",
            caption_text="Other image",
            image_bytes=b"bad",
            image_ext="png",
        )

        matches = sync.match_slots_to_candidates([slot], [weak, strong])

        self.assertEqual(matches[0].candidate_id, "page10-img1")
        self.assertEqual(matches[0].method, "context")

    def test_match_slots_falls_back_to_order_within_chapter(self):
        sync = load_module()

        slots = [
            sync.MarkdownImageSlot(
                md_path=Path("en/ch1.md"),
                chapter_key="chapter-1",
                index_in_doc=0,
                alt_text="Alpha",
                original_markdown="![Alpha](Alpha.png)",
                original_reference="Alpha.png",
                filename="Alpha.png",
                before_text="Noisy OCR text one",
                after_text="Noisy OCR text two",
                target_reference="assets-new/Alpha.png",
            ),
            sync.MarkdownImageSlot(
                md_path=Path("en/ch1.md"),
                chapter_key="chapter-1",
                index_in_doc=1,
                alt_text="Beta",
                original_markdown="![Beta](Beta.png)",
                original_reference="Beta.png",
                filename="Beta.png",
                before_text="Different noisy OCR text",
                after_text="Still noisy",
                target_reference="assets-new/Beta.png",
            ),
        ]
        candidates = [
            sync.PdfImageCandidate(
                candidate_id="c1",
                page_number=5,
                chapter_key="chapter-1",
                order_in_chapter=0,
                before_text="noise",
                after_text="noise",
                caption_text="noise",
                image_bytes=b"1",
                image_ext="png",
            ),
            sync.PdfImageCandidate(
                candidate_id="c2",
                page_number=6,
                chapter_key="chapter-1",
                order_in_chapter=1,
                before_text="noise",
                after_text="noise",
                caption_text="noise",
                image_bytes=b"2",
                image_ext="png",
            ),
        ]

        matches = sync.match_slots_to_candidates(slots, candidates, minimum_context_score=0.95)

        self.assertEqual([match.candidate_id for match in matches], ["c1", "c2"])
        self.assertTrue(all(match.method == "fallback_order" for match in matches))


class RewriteTests(unittest.TestCase):
    def test_rewrite_markdown_references_only_for_matched_slots(self):
        sync = load_module()

        slot_a = sync.MarkdownImageSlot(
            md_path=Path("en/chapter.md"),
            chapter_key="chapter",
            index_in_doc=0,
            alt_text="Alpha",
            original_markdown="![Alpha](../assets/Alpha.png)",
            original_reference="../assets/Alpha.png",
            filename="Alpha.png",
            before_text="before",
            after_text="after",
            target_reference="../assets-new/Alpha.png",
        )
        slot_b = sync.MarkdownImageSlot(
            md_path=Path("en/chapter.md"),
            chapter_key="chapter",
            index_in_doc=1,
            alt_text="Beta",
            original_markdown="![Beta](../assets/Beta.png)",
            original_reference="../assets/Beta.png",
            filename="Beta.png",
            before_text="before",
            after_text="after",
            target_reference="../assets-new/Beta.png",
        )
        match = sync.ImageMatch(
            slot=slot_a,
            candidate_id="c1",
            method="context",
            score=1.0,
            page_number=4,
            image_bytes=b"x",
            image_ext="png",
            reason="matched by context",
        )

        rewritten = sync.rewrite_markdown(
            "![Alpha](../assets/Alpha.png)\n![Beta](../assets/Beta.png)\n",
            [slot_a, slot_b],
            [match],
        )

        self.assertIn("![Alpha](../assets-new/Alpha.png)", rewritten)
        self.assertIn("![Beta](../assets/Beta.png)", rewritten)


if __name__ == "__main__":
    unittest.main()
