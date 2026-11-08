#!/usr/bin/env python3
"""Prevent internal documentation-project status from leaking into public guides.

Only explicit editorial/project-status phrases are forbidden. User-relevant
safety, version limits, prerequisites, and operational warnings remain allowed.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ONLINE = ROOT / "dist/online"
SOURCES = (
    "installation/README.md",
    "configuration/README.md",
    "administration/README.md",
    "user-guide/README.md",
    "user-guide/articles-and-topics/README.md",
    "user-guide/blocks-and-navigation/README.md",
    "user-guide/comments-and-moderation/README.md",
    "user-guide/syndication-rss-autotags/README.md",
    "administration/users-and-groups/README.md",
    "administration/backup-and-recovery/README.md",
    "administration/maintenance/README.md",
    "administration/troubleshooting/README.md",
    "plugins/plugin-installation-management/README.md",
    "plugins/bundled-plugins/README.md",
    "plugins/static-pages/README.md",
    "development/plugin-development/README.md",
    "development/security-and-permissions/README.md",
    "development/templates/README.md",
    "development/caching-template-library/README.md",
    "development/theme-development/README.md",
    "development/contributing/README.md",
    "reference/database-schema/README.md",
    "development/plugin-api/README.md",
    "development/configuration-api/README.md",
    "development/webservices/README.md",
)
# Do not add generic 'unverified' or 'not yet' here: those words can convey
# genuine limitations of insecure legacy features or unpublished content.
RULES = (
    r"editorial review ongoing",
    r"UI verification pending",
    r"runtime verification pending",
    r"## (?:Documentation status|Verification status|Remaining research|Still missing|What this guide still needs|Still to verify|Further verification|What remains to verify|Editorial backlog)",
    r"\*\*Remaining gates:\*\*",
    r"\*\*Remaining manual validation:\*\*",
    r"\*\*(?:Historical Wiki leads|Historical Wiki sources to evaluate|Source provenance):\*\*",
    r"tests remain pending",
    r"test cases to execute, not a record",
    r"not yet marked as executed",
    r"this walkthrough has not yet been exercised",
    r"complete live plugin installation or upgrade is \*\*not\*\* claimed",
    r"migration has been reviewed",
    r"not yet fully transcribed",
    r"legacy relative links.*audited separately",
)
PATTERNS = [re.compile(pattern, re.IGNORECASE) for pattern in RULES]

def check_file(path):
    contents = path.read_text(encoding="utf-8")
    failures = []
    for number, line in enumerate(contents.splitlines(), 1):
        if any(rule.search(line) for rule in PATTERNS):
            failures.append(f"{path.relative_to(ROOT)}:{number}: {line[:160]}")
    return failures

def main():
    failures = []
    for source in SOURCES:
        p = DOCS / source
        assert p.is_file(), f"Missing public source: {p}"
        failures.extend(check_file(p))
    assert ONLINE.is_dir(), "Build public HTML first"
    # Check the rendered public HTML too: injected site copy must not regress.
    for p in sorted(ONLINE.rglob("*.html")):
        failures.extend(check_file(p))
    if failures:
        raise AssertionError("Internal project status found in public documentation:\n" +
                             "\n".join(failures[:45]))
    assert len(SOURCES) == 25
    print("PASS: 25 public sources and rendered HTML contain no internal editorial gates")
    print("NOTE: structural wording check only; it does not certify technical accuracy")

if __name__ == "__main__":
    main()
