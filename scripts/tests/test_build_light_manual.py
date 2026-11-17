"""Deterministic tests for the Stage 7 Markdown wiki / generated manual.

These tests exercise the committed sources and temporary isolated Markdown
fixtures. They never connect to GitHub, download packages, deploy, or change
the real MANUAL.md.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import build_light_manual as manual


class ManualBuildTests(unittest.TestCase):
    def test_manifest_contains_complete_wiki(self):
        pages = manual.source_pages()
        self.assertEqual(len(pages), 41)
        self.assertEqual(pages[0], "index.md")
        self.assertIn("foundations/comparison.md", pages)
        self.assertIn("quality/validation.md", pages)
        self.assertIn("reference/faq.md", pages)

    def test_source_relative_links_all_resolve(self):
        self.assertEqual(manual.verify_source_links(manual.source_pages()), [])

    def test_committed_manual_has_zero_drift(self):
        expected = manual.build_manual(manual.source_pages())
        self.assertEqual(manual.OUTPUT.read_text(encoding="utf-8"), expected)

    def test_each_chapter_has_unique_anchor_and_toc(self):
        actual = manual.OUTPUT.read_text(encoding="utf-8")
        pages = manual.source_pages()
        for rel in pages:
            anchor = manual.page_id(rel)
            self.assertEqual(actual.count(f'<a id="{anchor}"></a>'), 1)
            self.assertIn(f"](#{anchor})", actual)

    def test_comparison_table_is_present_in_manual(self):
        text = manual.OUTPUT.read_text(encoding="utf-8")
        self.assertIn("ADDF Light Games vs. Original ADDF", text)
        for expected in ("Eight steps", "Five stages", "Original ADDF", "Gate I"):
            # Terminology varies slightly; require corresponding comparative prose/table.
            self.assertTrue(expected in text or expected.lower() in text.lower())

    def test_external_links_are_preserved(self):
        self.assertEqual(
            manual.resolve_link("foundations/comparison.md", "https://example.org/a#b", {"foundations/comparison.md"}),
            "https://example.org/a#b",
        )

    def test_wiki_page_links_become_chapter_anchors(self):
        text = manual.transform_page(
            "guides/intro.md", "# Intro\n\nSee [related](../foundations/comparison.md).\n",
            {"guides/intro.md", "foundations/comparison.md"},
        )
        self.assertIn("[related](#wiki-foundations--comparison)", text)

    def test_headings_have_stable_explicit_anchors(self):
        text = manual.transform_page(
            "guides/intro.md", "# Intro\n\n## Design Choices\n\n### Scope\n",
            {"guides/intro.md"},
        )
        self.assertIn('<a id="wiki-guides--intro--design-choices"></a>', text)
        self.assertIn("### Design Choices", text)
        self.assertIn('<a id="wiki-guides--intro--scope"></a>', text)

    def test_code_fences_do_not_get_link_rewrites(self):
        text = manual.transform_page(
            "guides/intro.md",
            "# Intro\n\n```md\n[not-real](missing.md)\n```\n\nSee [Intro](intro.md).\n",
            {"guides/intro.md"},
        )
        self.assertIn("[not-real](missing.md)", text)
        self.assertIn("[Intro](#wiki-guides--intro)", text)

    def test_deterministic_repeat_generation(self):
        chapters = manual.source_pages()
        self.assertEqual(manual.build_manual(chapters), manual.build_manual(chapters))

    def test_unicode_slug_is_stable(self):
        self.assertEqual(manual.slug("Research → Design / Ideation"), "research-design-ideation")
        self.assertEqual(manual.page_id("sprints/review.md"), "wiki-sprints--review")

    def fixture(self, root: Path, source: str):
        wiki = root / "docs" / "light-games"
        wiki.mkdir(parents=True)
        (wiki / "index.md").write_text(source, encoding="utf-8")
        (wiki / "manifest.txt").write_text("index.md\n", encoding="utf-8")
        return wiki

    def test_broken_internal_link_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            wiki = self.fixture(root, "# Home\n\nSee [missing](nope.md).\n")
            with patch.object(manual, "ROOT", root), patch.object(manual, "WIKI", wiki), patch.object(manual, "MANIFEST", wiki / "manifest.txt"):
                errors = manual.verify_source_links(manual.source_pages())
                self.assertTrue(any("broken relative link" in x for x in errors))

    def test_unlisted_wiki_file_is_an_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            wiki = self.fixture(root, "# Home\n")
            (wiki / "forgotten.md").write_text("# Forgotten\n", encoding="utf-8")
            with patch.object(manual, "ROOT", root), patch.object(manual, "WIKI", wiki), patch.object(manual, "MANIFEST", wiki / "manifest.txt"):
                with self.assertRaisesRegex(ValueError, "not in manifest"):
                    manual.source_pages()

    def test_duplicate_manifest_chapter_is_an_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            wiki = self.fixture(root, "# Home\n")
            (wiki / "manifest.txt").write_text("index.md\nindex.md\n", encoding="utf-8")
            with patch.object(manual, "ROOT", root), patch.object(manual, "WIKI", wiki), patch.object(manual, "MANIFEST", wiki / "manifest.txt"):
                with self.assertRaisesRegex(ValueError, "Duplicate manifest"):
                    manual.source_pages()

    def test_drift_detectable_without_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            wiki = self.fixture(root, "# Home\n\nOriginal text.\n")
            with patch.object(manual, "ROOT", root), patch.object(manual, "WIKI", wiki), patch.object(manual, "MANIFEST", wiki / "manifest.txt"):
                original = manual.build_manual(manual.source_pages())
                (wiki / "index.md").write_text("# Home\n\nChanged text.\n", encoding="utf-8")
                changed = manual.build_manual(manual.source_pages())
                self.assertNotEqual(original, changed)

    def test_cli_check_does_not_modify_manual(self):
        before = manual.OUTPUT.read_bytes()
        self.assertEqual(manual.main(["--check", "--verify-links"]), 0)
        self.assertEqual(before, manual.OUTPUT.read_bytes())


if __name__ == "__main__":
    unittest.main()
