#!/usr/bin/env python3
"""Validate an install.html overlay without running Geeklog or changing Core."""
from pathlib import Path
import hashlib
import os

ROOT = Path(__file__).resolve().parents[1]
CORE = Path(os.environ["GEEKLOG_CORE_DOCS"]).resolve()
BUILD = (ROOT / "build").resolve()
REL = Path("english/install.html")

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    assert (CORE / REL).is_file(), "Missing pinned Core installation document"
    assert (BUILD / REL).is_file(), "Missing generated installation document"
    assert digest(CORE / REL) != digest(BUILD / REL), "Installation overlay did not occur"
    core_files = {p.relative_to(CORE) for p in CORE.rglob("*") if p.is_file()}
    build_files = {p.relative_to(BUILD) for p in BUILD.rglob("*") if p.is_file()}
    missing = sorted(core_files - build_files)
    assert not missing, f"Original Core files missing: {missing}"
    for rel in sorted(core_files - {REL}):
        assert digest(CORE / rel) == digest(BUILD / rel), f"Unexpected Core file change: {rel}"
    added = sorted(build_files-core_files)
    allowed = {Path("legacy-link-audit.json")}
    assert set(added) <= allowed, f"Unexpected generated files: {added}"
    print(f"PASS: {len(core_files)} Core documentation files preserved except install.html")
    print(f"PASS: only install.html overlaid; generated audit files: {added}")
    print("NOTE: archive/website compatibility only; installer execution not tested")

if __name__ == "__main__":
    main()
