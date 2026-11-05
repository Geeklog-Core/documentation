#!/usr/bin/env python3
"""Exercise the documentation ZIP as a filesystem overlay in disposable staging.

This does not start Geeklog, touch a live installation or certify runtime help.
Source: pinned Core 2.2.2 documents and the tagged reCAPTCHA documentation.
"""
from pathlib import Path, PurePosixPath
import hashlib
import os
import shutil
import stat
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "dist/geeklog-2.2.2-docs-preview.zip"
CORE = Path(os.environ["GEEKLOG_CORE_DOCS"]).resolve()
RECAPTCHA = Path(os.environ["GEEKLOG_RELEASE_RECAPTCHA_DOCS"]).resolve()
DOCS_REL = Path("public_html/docs")
RECAPTCHA_REL = Path("public_html/admin/plugins/recaptcha/docs")
INSTALL = Path("english/install.html")
CONFIG = Path("english/config.html")

def digest(data):
    return hashlib.sha256(data).hexdigest()

def snapshot(root):
    return {p.relative_to(root).as_posix(): digest(p.read_bytes())
            for p in root.rglob("*") if p.is_file()}

def overlay_safely(archive, stage):
    with zipfile.ZipFile(archive) as z:
        infos = z.infolist()
        names = [entry.filename for entry in infos]
        assert len(names) == len(set(names)), "Duplicate ZIP entries"
        for info in infos:
            name = info.filename
            path = PurePosixPath(name)
            assert not path.is_absolute(), f"Absolute archive path: {name}"
            assert path.parts and path.parts[0] == "public_html", f"Wrong root: {name}"
            assert all(part not in (".", "..") for part in path.parts), f"Unsafe path: {name}"
            assert not (info.external_attr >> 16 & 0o170000) == stat.S_IFLNK, (
                f"Symlink entry forbidden: {name}")
            assert not info.is_dir(), f"Unexpected directory entry: {name}"
            dest = (stage / Path(*path.parts)).resolve()
            assert dest.is_relative_to(stage.resolve()), f"Path escape: {name}"
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(z.read(info))
        return len(infos)

def main():
    assert (CORE / CONFIG).is_file() and (RECAPTCHA / CONFIG).is_file()
    assert ARCHIVE.is_file(), "Build ZIP first"
    with tempfile.TemporaryDirectory(prefix="geeklog-docs-overlay-") as temp:
        sandbox = Path(temp)
        site = sandbox / "site"
        docs = site / DOCS_REL
        plugin = site / RECAPTCHA_REL
        shutil.copytree(CORE, docs)
        shutil.copytree(RECAPTCHA, plugin)
        # Sentinel proves that unrelated installation files are left intact.
        sentinel = site / "system/private-file.php"
        sentinel.parent.mkdir(parents=True)
        sentinel.write_bytes(b"<?php /* test-only sentinel */")
        before = snapshot(site)
        count = overlay_safely(ARCHIVE, site)
        after = snapshot(site)
        assert before["system/private-file.php"] == after["system/private-file.php"]
        assert set(before) <= set(after), "Overlay deleted original files"
        changed = {name for name in before if before[name] != after[name]}
        assert changed == {(DOCS_REL / INSTALL).as_posix()}, (
            f"Unexpected original-file changes: {sorted(changed)}")
        assert (docs / CONFIG).read_bytes() == (CORE / CONFIG).read_bytes()
        assert (plugin / CONFIG).read_bytes() == (RECAPTCHA / CONFIG).read_bytes()
        assert (docs / "english/modern/index.html").is_file()
        assert (docs / "english/modern/style.css").is_file()
        assert (docs / "english/modern/search-index.json").is_file()
        # Restore from an independent snapshot, without touching any real CMS.
        shutil.rmtree(docs)
        shutil.rmtree(plugin)
        shutil.copytree(CORE, docs)
        shutil.copytree(RECAPTCHA, plugin)
        assert snapshot(site) == before, "Rollback to original docs failed"
    print(f"PASS: extracted {count} entries into disposable 2.2.2 docs layout")
    print("PASS: only existing english/install.html changed; Core/plugin config unchanged")
    print("PASS: original filesystem snapshot restored; no real CMS was started")
    print("NOTE: real Geeklog administrator/help interaction remains to be tested")

if __name__ == "__main__":
    main()
