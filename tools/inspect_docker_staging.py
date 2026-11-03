#!/usr/bin/env python3
"""Read-only report of existing Geeklog Docker test containers.

Runs locally on a machine with Docker. Never prints container environment,
database credentials, file contents, or network addresses other than port bindings.
Does not create, stop, clone, or modify containers.
"""
import json
import subprocess
import sys

DEFAULTS = ["geeklog211-web", "geeklog211-db", "geeklog222-web", "geeklog222-db"]


def docker(*args):
    result = subprocess.run(["docker", *args], text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError("Docker command failed (details intentionally omitted)")
    return result.stdout


def main():
    names = sys.argv[1:] or DEFAULTS
    for name in names:
        if not name or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-" for c in name):
            raise ValueError("Invalid container name")
    found = json.loads(docker("inspect", "--type", "container", *names))
    by_mount = {}
    for c in found:
        for m in c.get('Mounts') or []:
            token = (m.get('Type'), m.get('Source') or m.get('Name'))
            if token[1]:
                by_mount.setdefault(token, []).append(c['Name'].lstrip('/'))
    print('cross-container shared mounts:')
    shared = [(kind, sorted(set(names))) for (kind, _), names in by_mount.items()
              if len(set(names)) > 1]
    if shared:
        for kind, names in shared:
            print('  SHARED {}: {}'.format(kind, ', '.join(names)))
    else:
        print('  none among inspected containers')
    print('')
    for c in found:
        name = c["Name"].lstrip("/")
        config = c.get("Config") or {}
        state = c.get("State") or {}
        network = c.get("NetworkSettings") or {}
        print(f"== {name} ==")
        print(f"status: {state.get('Status', 'unknown')}")
        print(f"image: {config.get('Image', 'unknown')}")
        labels = config.get('Labels') or {}
        print('compose project: {}'.format(labels.get('com.docker.compose.project', '(not labelled)')))
        print('compose service: {}'.format(labels.get('com.docker.compose.service', '(not labelled)')))
        print(f"ports: {json.dumps(network.get('Ports') or {}, sort_keys=True)}")
        mounts = c.get("Mounts") or []
        print("mounts (type and target only; no source host paths):")
        for m in mounts:
            print(f"  {m.get('Type', 'unknown')} -> {m.get('Destination', '?')} (rw={m.get('RW', '?')})")
        print("")

    print("READ-ONLY INSPECTION COMPLETE.")
    print("Shared-mount check covers inspected containers only.")
    print("Do not reuse live databases for installation/upgrade/migration tests.")
    print("Do not share docker inspect JSON: it can contain credentials and secrets.")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, ValueError, json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Cannot complete inspection: {e}", file=sys.stderr)
        sys.exit(2)
