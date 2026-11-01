#!/usr/bin/env python3
"""Audit pinned documentation tree against the Geeklog v2.2.2 Git tag.

Mismatch is reported and treated as a release-compatibility gate: no claim that
the pinned checkout represents the release unless all files match exactly.
"""
import hashlib
import os
from pathlib import Path
PINNED=Path(os.environ["GEEKLOG_CORE_DOCS"])
RELEASE=Path(os.environ["GEEKLOG_RELEASE_DOCS"])
def snapshot(base):
    return {p.relative_to(base).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
            for p in base.rglob("*") if p.is_file()}
def main():
    a,b=snapshot(PINNED),snapshot(RELEASE)
    added=sorted(b.keys()-a.keys())
    removed=sorted(a.keys()-b.keys())
    modified=sorted(k for k in (a.keys()&b.keys()) if a[k]!=b[k])
    print(f"RELEASE SOURCE AUDIT: pinned={len(a)} files; v2.2.2 tag={len(b)} files")
    for name,items in (("tag-only",added),("pinned-only",removed),("modified",modified)):
        print(f"{name}: {len(items)}")
        for item in items[:50]: print("  "+item)
    assert not (added or removed or modified), "Pinned docs differ from v2.2.2 tag. Rebase package on verified release source before claiming compatibility."
    print("PASS: pinned Core documentation is byte-for-byte identical to v2.2.2 tag")
if __name__=="__main__":main()
