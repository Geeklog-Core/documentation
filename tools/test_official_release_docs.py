#!/usr/bin/env python3
"""Self-contained regression tests; no download of the official archive needed."""
import io
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("check_official_release_docs.py")


class ReleaseArchiveComparisonTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.core = self.root / "core"
        self.recaptcha = self.root / "recaptcha"
        self.core.mkdir()
        self.recaptcha.mkdir()
        (self.core / "install.html").write_bytes(b"legacy install")
        (self.recaptcha / "config.html").write_bytes(b"legacy plugin")
        self.archive = self.root / "geeklog-2.2.2.tar.gz"

    def build_archive(self, plugin=b"legacy plugin", include_core=True):
        with tarfile.open(self.archive, "w:gz") as tf:
            files = [
                ("geeklog/public_html/admin/plugins/recaptcha/docs/config.html", plugin),
            ]
            if include_core:
                files.append(("geeklog/public_html/docs/install.html", b"legacy install"))
            for name, data in files:
                entry = tarfile.TarInfo(name)
                entry.size = len(data)
                tf.addfile(entry, io.BytesIO(data))

    def check(self, *args):
        return subprocess.run([
            sys.executable, str(SCRIPT), str(self.archive),
            "--core-docs", str(self.core), "--recaptcha-docs", str(self.recaptcha),
            *args
        ], capture_output=True, text=True)

    def test_identical_docs_pass_when_metadata_explicitly_ignored(self):
        self.build_archive()
        p = self.check("--ignore-published-size-md5")
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)

    def test_crlf_only_requires_explicit_opt_in(self):
        (self.core / "install.html").write_bytes(b"first\nsecond\n")
        self.build_archive()
        # Repack synthetic sample with CRLF only in its Core doc.
        with tarfile.open(self.archive, "w:gz") as tf:
            for name, data in [
                ("geeklog/public_html/docs/install.html", b"first\r\nsecond\r\n"),
                ("geeklog/public_html/admin/plugins/recaptcha/docs/config.html", b"legacy plugin"),
            ]:
                entry = tarfile.TarInfo(name)
                entry.size = len(data)
                tf.addfile(entry, io.BytesIO(data))
        strict = self.check("--ignore-published-size-md5")
        self.assertEqual(strict.returncode, 1, strict.stdout + strict.stderr)
        self.assertIn("LINE_ENDINGS_ONLY: install.html", strict.stdout)
        normalized = self.check("--ignore-published-size-md5", "--allow-crlf-normalization")
        self.assertEqual(normalized.returncode, 0, normalized.stdout + normalized.stderr)

    def test_modified_plugin_doc_fails(self):
        self.build_archive(plugin=b"modified")
        p = self.check("--ignore-published-size-md5")
        self.assertEqual(p.returncode, 1)
        self.assertIn("DIFFERENT: config.html", p.stdout)

    def test_missing_documentation_fails(self):
        self.build_archive(include_core=False)
        p = self.check("--ignore-published-size-md5")
        self.assertEqual(p.returncode, 1)
        self.assertIn("MISSING: install.html", p.stdout)

    def test_nonofficial_archive_fails_published_metadata_check(self):
        self.build_archive()
        p = self.check()
        self.assertEqual(p.returncode, 1)
        self.assertIn("size/MD5 differs", p.stderr)


if __name__ == "__main__":
    unittest.main()
