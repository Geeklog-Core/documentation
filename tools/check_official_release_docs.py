#!/usr/bin/env python3
"""Compare a downloaded Geeklog 2.2.2 release archive against pinned source docs.

Read-only: never extracts the archive. The official tar.gz must be obtained
separately by the reviewer; comparing the Git tag alone is not sufficient.
"""
import argparse
import hashlib
from pathlib import Path, PurePosixPath
import sys
import tarfile

OFFICIAL_SIZE = 16978448
OFFICIAL_MD5 = "962cc6e6ed1ce13f65066e47859511d8"
MAX_DOC_MEMBER = 20 * 1024 * 1024
DOC_PREFIXES = (
    ("public_html/docs/", "core"),
    ("public_html/admin/plugins/recaptcha/docs/", "recaptcha"),
)


def canonical_name(name):
    parts = PurePosixPath(name).parts
    if name.startswith("/") or ".." in parts or "\\" in name:
        raise ValueError(f"Unsafe archive path: {name!r}")
    clean = "/".join(p for p in parts if p != ".")
    for prefix, group in DOC_PREFIXES:
        needle = "/" + prefix
        if clean.startswith(prefix):
            return group, clean[len(prefix):]
        if needle in clean:
            before, after = clean.split(needle, 1)
            if before and after:
                return group, after
    return None


def local_files(root):
    if not root.is_dir():
        raise ValueError(f"Missing pinned source directory: {root}")
    return {p.relative_to(root).as_posix(): p for p in root.rglob("*") if p.is_file()}


def inspect_archive(archive):
    result = {"core": {}, "recaptcha": {}}
    with tarfile.open(archive, mode="r:gz") as tf:
        for member in tf:
            mapped = canonical_name(member.name)
            if mapped is None or member.isdir():
                continue
            group, relative = mapped
            if not relative or member.type not in (tarfile.REGTYPE, tarfile.AREGTYPE):
                raise ValueError(f"Non-regular documentation file: {member.name}")
            if member.size > MAX_DOC_MEMBER:
                raise ValueError(f"Unexpectedly large documentation file: {member.name}")
            if relative in result[group]:
                raise ValueError(f"Duplicate documentation file: {member.name}")
            stream = tf.extractfile(member)
            if stream is None:
                raise ValueError(f"Unreadable documentation file: {member.name}")
            result[group][relative] = stream.read()
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("--core-docs", required=True, type=Path)
    parser.add_argument("--recaptcha-docs", required=True, type=Path)
    parser.add_argument("--allow-crlf-normalization", action="store_true",
                        help="Accept only CRLF vs LF differences, with per-file reporting")
    parser.add_argument("--ignore-published-size-md5", action="store_true",
                        help="Only for custom/repacked archive investigation")
    a = parser.parse_args(argv)
    if not a.archive.is_file():
        parser.error(f"Archive not found: {a.archive}")
    actual_size = a.archive.stat().st_size
    sha256 = hashlib.sha256()
    md5 = hashlib.md5(usedforsecurity=False)
    with a.archive.open("rb") as stream:
        while chunk := stream.read(1024 * 1024):
            sha256.update(chunk)
            md5.update(chunk)
    print(f"Archive: {a.archive.name} | bytes={actual_size} | SHA-256={sha256.hexdigest()}")
    if not a.ignore_published_size_md5 and (actual_size != OFFICIAL_SIZE or md5.hexdigest() != OFFICIAL_MD5):
        print("FAIL: size/MD5 differs from geeklog.net's published 2.2.2 archive metadata", file=sys.stderr)
        return 1
    print(f"Published size/MD5: {'SKIPPED' if a.ignore_published_size_md5 else 'MATCH'} (MD5 is legacy integrity metadata, not a modern signature)")
    archive_files = inspect_archive(a.archive)
    failed = False
    for group, root in (("core", a.core_docs), ("recaptcha", a.recaptcha_docs)):
        expected = {key: path.read_bytes() for key, path in local_files(root).items()}
        actual = archive_files[group]
        missing = sorted(expected.keys() - actual.keys())
        extra = sorted(actual.keys() - expected.keys())
        different = []
        line_endings_only = []
        identical = []
        for key in sorted(expected.keys() & actual.keys()):
            packaged = actual[key]
            source = expected[key]
            if packaged == source:
                identical.append(key)
            elif packaged.replace(b"\r\n", b"\n") == source.replace(b"\r\n", b"\n"):
                line_endings_only.append(key)
            else:
                different.append(key)
        print(f"{group}: pinned={len(expected)} packaged={len(actual)} identical={len(identical)} "
              f"line-endings-only={len(line_endings_only)} missing={len(missing)} "
              f"extra={len(extra)} content-differences={len(different)}")
        for label, entries in (("MISSING", missing), ("EXTRA", extra),
                               ("DIFFERENT", different), ("LINE_ENDINGS_ONLY", line_endings_only)):
            for path in entries:
                print(f"  {label}: {path}")
        failed |= bool(missing or extra or different or
                       (line_endings_only and not a.allow_crlf_normalization))
    print("FAIL: packaged documentation differs from pinned source" if failed
          else "PASS: packaged docs and reCAPTCHA docs exactly match pinned source")
    return int(failed)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, tarfile.TarError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(2)
