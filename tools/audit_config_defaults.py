#!/usr/bin/env python3
"""Inventory documented defaults from Geeklog 2.2.2's pinned HTML reference.

Creates a machine-readable audit report, NOT a replacement configuration
reference. This deliberately does not copy full legacy descriptions or modify
the original embedded help. Requires GEEKLOG_CORE_DOCS from the CI workflow.
"""
from html.parser import HTMLParser
from html import unescape
from pathlib import Path
import json
import os
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(os.environ["GEEKLOG_CORE_DOCS"]) / "english/config.html"
OUTPUT = ROOT / "dist/config-defaults-audit.json"
MARKDOWN = ROOT / "docs/configuration/README.md"
ROW = re.compile(
    r'<tr\b[^>]*>\s*<td\b[^>]*>\s*<a\s+name="(desc_[^"]+)"[^>]*>.*?</tr>',
    re.I | re.S,
)


class TableCells(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.cells = []
        self.in_cell = False

    def handle_starttag(self, tag, attrs):
        if tag == "td":
            self.cells.append([])
            self.in_cell = True

    def handle_endtag(self, tag):
        if tag == "td":
            self.in_cell = False

    def handle_data(self, value):
        if self.in_cell and self.cells:
            self.cells[-1].append(value)


def main():
    source = SOURCE.read_text(encoding="utf-8")
    records = []
    seen = set()
    for match in ROW.finditer(source):
        identifier = match.group(1)
        assert identifier not in seen, f"Duplicate option: {identifier}"
        seen.add(identifier)
        parser = TableCells()
        parser.feed(match.group(0))
        assert len(parser.cells) >= 3, f"Not a three-column config row: {identifier}"
        text = lambda index: re.sub(
            r"\s+", " ", " ".join(parser.cells[index])
        ).strip()
        records.append({
            "anchor": identifier,
            "setting": identifier.removeprefix("desc_"),
            "documented_default": text(1),
            "default_reviewed": False,
        })

    # A stable structural baseline; not an assertion that every default is
    # usable as-is or even nonempty.
    assert len(records) == 387, (
        f"Expected 387 2.2.2 configuration option rows, got {len(records)}"
    )
    historical = {
        "desc_site_url": "http://www.example.com",
        "desc_site_admin_url": "http://www.example.com/admin",
        "desc_site_name": "Geeklog Site",
        "desc_site_slogan": "Another Nifty Geeklog Site",
        "desc_mail_settings_port": "25",
        "desc_mail_settings_auth": "0",
        "desc_ip_anonymization": "-1",
    }
    by_id = {item["anchor"]: item for item in records}
    for identifier, expected in historical.items():
        assert by_id[identifier]["documented_default"] == expected, (
            f"Unexpected historical default for {identifier}"
        )
        by_id[identifier]["default_reviewed"] = True

    # Each historical default must now be present in the maintained
    # Markdown source next to its original setting description.
    markdown = MARKDOWN.read_text(encoding="utf-8")
    for item in records:
        key = item["setting"]
        title = {
            "site_url": "### Site URL",
            "site_name": "### Site name",
        }.get(key, f"### `{key}`")
        assert markdown.count(title + "\n") == 1, (
            f"Missing or repeated Markdown setting heading: {key}")
        after = markdown.split(title + "\n", 1)[1]
        next_heading = after.find("\n### ")
        section = after if next_heading < 0 else after[:next_heading]
        pattern = r"\*\*Documented default \(Geeklog 2\.2\.2\):\*\* `([^`]+)`"
        found = re.search(pattern, section)
        assert found, f"Missing migrated default in Markdown: {key}"
        actual = unescape(found.group(1))
        expected = item["documented_default"] or "(empty)"
        assert actual == expected, (
            f"Default mismatch for {key}: {actual!r} != {expected!r}")
        item["default_transcribed"] = True

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({
        "source": "Geeklog-Core/geeklog v2.2.2: public_html/docs/english/config.html",
        "notice": "Historical documentation defaults only; not live configuration or certified migration",
        "total_rows": len(records),
        "manually_reviewed_settings": list(historical),
        "defaults_transcribed_into_markdown": len(records),
        "items": records,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: {len(records)} historical defaults reproduced in the Markdown source; "
          f"{len(historical)} independently reviewed")
    print("NOTE: values transcribed structurally; prose, tables and examples still require editorial review")


if __name__ == "__main__":
    main()
