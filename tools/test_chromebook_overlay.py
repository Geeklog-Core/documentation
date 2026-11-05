#!/usr/bin/env python3
"""Safely stage and roll back the documentation ZIP on the Chromebook lab.

Only accepts ~/geeklog-docs-validation/staging-222/site, never live 211/222 sites.
No Docker commands, database changes, credentials or permission broadening.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import sys
import time
import zipfile

DOCS = Path("public_html/docs")
RECAPTCHA = Path("public_html/admin/plugins/recaptcha/docs")
SENTINELS = (DOCS / "english/config.html", DOCS / "english/install.html",
             RECAPTCHA / "english/config.html")
PREFIXES = ("public_html/docs/", "public_html/admin/plugins/recaptcha/docs/")
MARKER = "geeklog-docs-222-qa-v1"

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def require_stage(site):
    site = site.expanduser().resolve(strict=True)
    expected = (Path.home() / "geeklog-docs-validation/staging-222/site").resolve()
    if site != expected:
        raise RuntimeError("Refusing non-disposable site: expected " + str(expected))
    if not (site.parent / "compose.yaml").is_file():
        raise RuntimeError("The isolated staging-222/compose.yaml is missing")
    if not all((site / item).is_file() for item in SENTINELS):
        raise RuntimeError("Original Core and reCAPTCHA help files are missing")
    for item in (site / DOCS, site / RECAPTCHA):
        if item.is_symlink():
            raise RuntimeError("Symlink documentation folder is unsafe: " + str(item))
    return site

def validate_archive(archive):
    if not archive.is_file():
        raise RuntimeError("ZIP not found: " + str(archive))
    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None:
            raise RuntimeError("ZIP CRC check failed")
        infos = z.infolist()
        names = [i.filename for i in infos]
        if len(set(names)) != len(names) or not names:
            raise RuntimeError("Duplicate or empty ZIP")
        for info in infos:
            p = PurePosixPath(info.filename)
            if info.is_dir() or p.is_absolute() or "." in p.parts or ".." in p.parts:
                raise RuntimeError("Unsafe ZIP entry: " + info.filename)
            if not info.filename.startswith(PREFIXES):
                raise RuntimeError("Unexpected ZIP path: " + info.filename)
            if (info.external_attr >> 16) & 0o170000 == 0o120000:
                raise RuntimeError("Symlink entry: " + info.filename)
        for required in (
            "public_html/docs/english/install.html",
            "public_html/docs/english/config.html",
            "public_html/docs/english/modern/index.html",
            "public_html/admin/plugins/recaptcha/docs/english/config.html",
        ):
            if required not in names:
                raise RuntimeError("Missing required entry: " + required)
        return names

def copy_originals(site, backup):
    for rel in (DOCS, RECAPTCHA):
        shutil.copytree(site / rel, backup / rel, symlinks=True)
    return {str(rel): digest(site / rel) for rel in SENTINELS}

def apply(site, archive):
    names = validate_archive(archive)
    original = {str(rel): digest(site / rel) for rel in SENTINELS}
    # The official 2.2.2 release can differ from the pinned source only by
    # line ending normalization. Preserve *all* existing historical files
    # byte-for-byte instead of rewriting them with the ZIP's line endings.
    with zipfile.ZipFile(archive) as z:
        for name in names:
            target = site / name
            if target.is_file() and name != str(DOCS / "english/install.html"):
                packed = z.read(name)
                original_bytes = target.read_bytes()
                if packed.replace(b"\\r\\n", b"\\n") != original_bytes.replace(b"\\r\\n", b"\\n"):
                    raise RuntimeError("Refusing ZIP: legacy document content differs: " + name)
    backup = site.parent / ("docs-qa-backup-" + time.strftime("%Y%m%d-%H%M%S"))
    backup.mkdir(mode=0o700)
    try:
        copy_originals(site, backup)
        manifest = {"marker": MARKER, "site": str(site),
                    "archive_sha256": digest(archive), "original": original}
        (backup / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        with zipfile.ZipFile(archive) as z:
            for name in names:
                dest = site / name
                # Do not write through symlinks, even when located below docs.
                if any(parent.is_symlink() for parent in (dest, *dest.parents) if parent != site and site in parent.parents):
                    raise RuntimeError("Refusing symlink target: " + name)
                # Preserve existing historical files exactly, including CRLF.
                if dest.is_file() and name != str(DOCS / "english/install.html"):
                    continue
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(z.read(name))
        for rel in (DOCS / "english/config.html", RECAPTCHA / "english/config.html"):
            if digest(site / rel) != original[str(rel)]:
                raise RuntimeError("Unexpected change to " + str(rel))
    except Exception:
        print("ERROR: deployment stopped. Backup retained at:", backup, file=sys.stderr)
        print("Use --rollback with this backup once the staging path is confirmed.", file=sys.stderr)
        raise
    print("PASS: overlay applied in isolated staging only; original legacy files preserved")
    print("Files in ZIP:", len(names))
    print("Backup:", backup)
    print("HTTP test: http://localhost:8083/docs/english/modern/index.html")
    print("Core help: http://localhost:8083/docs/english/config.html#desc_site_url")
    print("Use --rollback and --backup PATH to restore original docs after browser checks.")

def rollback(site, backup):
    backup = backup.expanduser().resolve(strict=True)
    if backup.parent != site.parent or not backup.name.startswith("docs-qa-backup-"):
        raise RuntimeError("Backup must belong to isolated staging-222")
    meta = json.loads((backup / "manifest.json").read_text(encoding="utf-8"))
    if meta.get("marker") != MARKER or meta.get("site") != str(site):
        raise RuntimeError("Backup identity mismatch")
    for rel in (DOCS, RECAPTCHA):
        if not (backup / rel).is_dir():
            raise RuntimeError("Incomplete backup: " + str(rel))
    for rel in (DOCS, RECAPTCHA):
        shutil.rmtree(site / rel)
        shutil.copytree(backup / rel, site / rel, symlinks=True)
    for name, sha in meta["original"].items():
        if digest(site / name) != sha:
            raise RuntimeError("Rollback verification failed for " + name)
    print("PASS: original 2.2.2 Core and reCAPTCHA docs restored")
    print("Backup kept for inspection:", backup)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--site", default="~/geeklog-docs-validation/staging-222/site")
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--apply", metavar="ZIP", type=Path)
    group.add_argument("--rollback", action="store_true")
    p.add_argument("--backup", type=Path, help="Backup path printed after --apply")
    args = p.parse_args()
    site = require_stage(Path(args.site))
    if args.apply:
        apply(site, args.apply.expanduser().resolve())
    else:
        if not args.backup:
            p.error("--rollback requires --backup")
        rollback(site, args.backup)

if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError, zipfile.BadZipFile) as exc:
        sys.exit("STOP: " + str(exc))
