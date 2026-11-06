#!/usr/bin/env python3
"""Validate the 12 content-role defaults in the Markdown permissions matrix.

Only checks source-backed default values and rendered matrix semantics; it
does not certify account permissions, existing records, or live behavior.
"""
from pathlib import Path
import os
import re
from html import unescape
from html.parser import HTMLParser
import markdown

ROOT = Path(__file__).resolve().parents[1]
LEGACY = Path(os.environ["GEEKLOG_CORE_DOCS"]) / "english/config.html"
MARKDOWN = ROOT / "docs/configuration/README.md"

class CellParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.cells = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        if tag in ("td", "th"):
            self.current = []

    def handle_data(self, data):
        if self.current is not None:
            self.current.append(data)

    def handle_endtag(self, tag):
        if tag in ("td", "th") and self.current is not None:
            self.cells.append(" ".join("".join(self.current).split()))
            self.current = None

def main():
    original = LEGACY.read_text(encoding="utf-8")
    text = MARKDOWN.read_text(encoding="utf-8")
    heading = "### Default permissions at a glance"
    assert text.count(heading) == 1
    section = text.split(heading, 1)[1].split("### Autotag usage permissions at a glance", 1)[0]
    rendered = markdown.markdown(section, extensions=["tables"])
    tables = re.findall(r"<table[^>]*>([\s\S]*?)</table>", rendered, re.I)
    assert len(tables) == 1, "Exactly one permission matrix expected"
    rows = re.findall(r"<tr[^>]*>([\s\S]*?)</tr>", tables[0], re.I)
    assert len(rows) == 4, "Header plus story/topic/block rows expected"
    for resource, row in zip(("story", "topic", "block"), rows[1:]):
        parsed = CellParser()
        parsed.feed(row)
        assert len(parsed.cells) == 5
        assert resource in parsed.cells[0].lower(), resource
        for role in range(4):
            key = f"default_permissions_{resource}_{role}"
            matched = [r for r in re.findall(
                r"<tr\b[^>]*>[\s\S]*?</tr>", original, re.I)
                if f'name="desc_{key}"' in r]
            assert len(matched) == 1, f"Missing 2.2.2 source row: {key}"
            src = CellParser()
            src.feed(matched[0])
            assert len(src.cells) == 3
            expected = src.cells[1]
            actual = parsed.cells[role + 1]
            assert actual == expected, (
                f"Permission matrix differs from original {key}: {actual!r} != {expected!r}"
            )
    print("PASS: all 12 permission matrix cells match the tagged Geeklog 2.2.2 reference")

if __name__ == "__main__":
    main()
