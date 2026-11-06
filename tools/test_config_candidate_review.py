#!/usr/bin/env python3
"""Negative regressions for the isolated Markdown-generated configuration candidate.

Run only after build_config_candidate.py, with GEEKLOG_CORE_DOCS pointing to
the pinned Geeklog 2.2.2 documentation checkout. No Docker or site writes.
"""
import importlib.util
import io
import unittest
import zipfile
from pathlib import Path

SCRIPT = Path(__file__).with_name("check_config_candidate_review.py")
spec = importlib.util.spec_from_file_location("config_candidate_review", SCRIPT)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class CandidateReviewNegativeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = gate.LEGACY.read_bytes()
        cls.candidate = gate.CANDIDATE.read_bytes()
        gate.validate_anchors(cls.original, cls.candidate)

    def test_unmodified_candidate_is_valid(self):
        self.assertEqual(
            len(gate.validate_anchors(self.original, self.candidate).anchors), 449
        )

    def test_missing_anchor_is_rejected(self):
        broken = self.candidate.replace(
            b'id="desc_site_url"', b'id="desc_site_url_missing"', 1
        ).replace(
            b'name="desc_site_url"', b'name="desc_site_url_missing"', 1
        )
        self.assertNotEqual(broken, self.candidate)
        with self.assertRaisesRegex(AssertionError, "Legacy help anchor set differs"):
            gate.validate_anchors(self.original, broken)

    def test_duplicate_anchor_is_rejected(self):
        broken = self.candidate.replace(
            b'<body>', b'<body><a id="desc_site_url"></a>', 1
        )
        # Actual generated candidate starts with <body><main>; test inserts
        # duplicate before the first existing target, not after parsing.
        self.assertNotEqual(broken, self.candidate)
        with self.assertRaisesRegex(AssertionError, "Duplicate anchor"):
            gate.validate_anchors(self.original, broken)

    def test_broken_same_page_fragment_is_rejected(self):
        broken = self.candidate.replace(
            b'<main>', b'<main><a href="#missing_context_help_target">broken</a>', 1
        )
        self.assertNotEqual(broken, self.candidate)
        with self.assertRaisesRegex(AssertionError, "Broken internal help link"):
            gate.validate_anchors(self.original, broken)

    @staticmethod
    def archive(entries):
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
            for name, data in entries:
                z.writestr(name, data)
        buf.seek(0)
        return zipfile.ZipFile(buf)

    def test_single_member_zip_is_valid(self):
        with self.archive([(gate.MEMBER, self.candidate)]) as z:
            gate.validate_archive(z, self.candidate)

    def test_extra_zip_member_is_rejected(self):
        with self.archive([
            (gate.MEMBER, self.candidate),
            ("public_html/docs/english/other.html", b"unexpected"),
        ]) as z:
            with self.assertRaisesRegex(AssertionError, "single config.html"):
                gate.validate_archive(z, self.candidate)

    def test_changed_zip_contents_are_rejected(self):
        with self.archive([(gate.MEMBER, self.candidate + b"tamper")]) as z:
            with self.assertRaisesRegex(AssertionError, "Archive differs"):
                gate.validate_archive(z, self.candidate)


if __name__ == "__main__":
    unittest.main()
