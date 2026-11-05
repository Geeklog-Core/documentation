#!/usr/bin/env python3
"""Inventory documented defaults from Geeklog 2.2.2's pinned HTML reference.

Creates a machine-readable audit report, NOT a replacement configuration
reference. This deliberately does not copy full legacy descriptions or modify
the original embedded help. Requires GEEKLOG_CORE_DOCS from the CI workflow.
"""
from html.parser import HTMLParser
from pathlib import Path
import json
import os
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(os.environ["GEEKLOG_CORE_DOCS"]) / "english/config.html"
OUTPUT = ROOT / "dist/config-defaults-audit.json"
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

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({
        "source": "Geeklog-Core/geeklog v2.2.2: public_html/docs/english/config.html",
        "notice": "Historical documentation defaults only; not live configuration or certified migration",
        "total_rows": len(records),
        "manually_reviewed_settings": list(historical),
        "items": records,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: inventoried {len(records)} historical configuration defaults; "
          f"{len(historical)} manually checked")
    print("NOTE: 380 other defaults require editorial review before full parity")


if __name__ == "__main__":
    main()
