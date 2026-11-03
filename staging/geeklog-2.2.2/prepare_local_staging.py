#!/usr/bin/env python3
"""Prepare isolated local Geeklog 2.2.2 testing files, without running Docker.

Run inside staging/geeklog-2.2.2 after copying this directory to a new local
workspace. Exits without touching a pre-existing site or .env file.
"""
from pathlib import Path, PurePosixPath
from hashlib import sha256, md5
import os
import secrets
import sys
import tarfile

EXPECTED_SIZE = 16978448
EXPECTED_MD5 = "962cc6e6ed1ce13f65066e47859511d8"
EXPECTED_SHA256 = "d12991f78225289d2bac297bff1a7e9be55f04a9e0aa097bb379e41d7fb138a8"


def main():
    root = Path(__file__).resolve().parent
    archive = root.parent.parent / "geeklog-2.2.2.tar.gz"
    site = root / "site"
    env = root / ".env"

    if site.exists() or env.exists():
        raise RuntimeError("Staging directory already initialized. Refusing to overwrite site/.env")
    if not archive.is_file():
        raise RuntimeError("Missing ../.. /geeklog-2.2.2.tar.gz (place it in geeklog-docs-validation)")
    if archive.stat().st_size != EXPECTED_SIZE:
        raise RuntimeError("Archive size mismatch: not the verified Geeklog 2.2.2 tarball")
    raw = archive.read_bytes()
    if md5(raw).hexdigest() != EXPECTED_MD5 or sha256(raw).hexdigest() != EXPECTED_SHA256:
        raise RuntimeError("Official archive hash mismatch; no files extracted")

    # Safe extraction: the published archive contains regular files/directories
    # only. Reject any links, devices, traversal, or duplicate normalized names.
    with tarfile.open(archive, "r:gz") as tf:
        entries = tf.getmembers()
        seen = set()
        for m in entries:
            p = PurePosixPath(m.name)
            if p.is_absolute() or not p.parts or ".." in p.parts or "\\" in m.name:
                raise RuntimeError("Unsafe archive member name")
            if not (m.isfile() or m.isdir()):
                raise RuntimeError("Archive contains non-file member")
            normalized = p.as_posix()
            if normalized in seen:
                raise RuntimeError("Duplicate archive member")
            seen.add(normalized)

        site.mkdir(mode=0o755)
        try:
            for m in entries:
                target = site.joinpath(*PurePosixPath(m.name).parts)
                if m.isdir():
                    target.mkdir(parents=True, exist_ok=True)
                    target.chmod(0o755)
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    stream = tf.extractfile(m)
                    if stream is None:
                        raise RuntimeError("Unreadable archive member")
                    with target.open("xb") as output:
                        while data := stream.read(1024 * 1024):
                            output.write(data)
                    target.chmod(0o644)
            # archive directory order may cause changed modes; normalize at end
            for directory in site.rglob("*"):
                if directory.is_dir():
                    directory.chmod(0o755)
            os.chmod(site, 0o755)
        except Exception:
            raise RuntimeError("Partial staging copy created. Inspect then remove ONLY staging/site before retry")

    # Local-only throwaway database credentials; don't share the .env contents.
    fd = os.open(env, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as out:
        out.write("STAGE_DB_ROOT_PASSWORD=" + secrets.token_hex(24) + "\n")
        out.write("STAGE_DB_PASSWORD=" + secrets.token_hex(24) + "\n")
    print("PASS: verified real official Geeklog 2.2.2 tarball and prepared isolated staging/site")
    print("PASS: generated local .env with new disposable DB secrets (not printed)")
    print("NOT STARTED: Docker containers or installer. Review docker compose config before starting.")
    print("Installation DB server=db, database=geeklog_stage, user=geeklog_stage.")
    print("Your generated password is in local staging/.env; never paste it into chat.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, tarfile.TarError) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        sys.exit(2)
