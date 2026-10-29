#!/usr/bin/env python3
"""Validate legacy installation fragment IDs in Markdown and rendered HTML.

This independent branch uses Python-Markdown and does not rely on the
unmerged foundation PR.
"""
import re
from html.parser import HTMLParser
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/installation/README.md"
OUTPUT = ROOT / "build/english/install.html"
REQUIRED = {
    "glossary", "public_html", "installation_requirements", "preinstall",
    "things_you_should_know", "install", "upgrade", "migrate", "installprob",
}

class Anchors(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.names = set()
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.names.add(attrs["name"])

def main():
    raw = SOURCE.read_text(encoding="utf-8")
    html = markdown.markdown(raw, extensions=["tables", "fenced_code", "toc"])
    found = Anchors()
    found.feed(html)
    assert REQUIRED <= found.ids, f"Missing legacy id anchors: {sorted(REQUIRED - found.ids)}"
    assert REQUIRED <= found.names, f"Missing legacy name anchors: {sorted(REQUIRED - found.names)}"
    # Keep the legacy identifiers represented by explicit named anchors.
    for anchor in REQUIRED:
        literal = f'<a id="{anchor}" name="{anchor}"></a>'
        assert literal in raw, f"Source missing explicit anchor: {anchor}"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><title>Installing Geeklog</title></head><body>\n' + html + '\n</body></html>\n', encoding="utf-8")
    print(f"PASS: all {len(REQUIRED)} legacy installation anchors present in generated HTML")

if __name__ == "__main__":
    main()
