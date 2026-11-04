#!/usr/bin/env python3
"""Measure configuration-help Markdown coverage against pinned Geeklog Core HTML.

Never changes embedded config.html. Fail only for source mismatches or loss of
an already-covered configuration anchor; report remaining work, do not fake
completion. Intended to run after check_install_anchors.py and build_dual_preview.py.
"""
import json
import os
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = Path(os.environ["GEEKLOG_CORE_DOCS"]) / "english/config.html"
PACKAGED = ROOT / "dist/geeklog-2.2.2/public_html/docs/english/config.html"
WEB = ROOT / "dist/online/configuration.html"
REPORT = ROOT / "dist/configuration-coverage.json"


class Anchors(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.identifiers = []
    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        for name in ("id", "name"):
            value = attributes.get(name)
            if value:
                self.identifiers.append(value)


def names(path):
    parsed = Anchors()
    parsed.feed(path.read_text(encoding="utf-8"))
    return set(parsed.identifiers)


def main():
    for path in (CORE, PACKAGED, WEB):
        if not path.is_file():
            raise SystemExit(f"Required input absent: {path}")
    assert PACKAGED.read_bytes() == CORE.read_bytes(), (
        "Embedded config.html differs from pinned source")
    source = {name for name in names(CORE) if name.startswith("desc_")}
    rendered = {name for name in names(WEB) if name.startswith("desc_")}
    assert len(source) >= 300, "Unexpectedly small source anchor inventory"
    unknown = rendered - source
    assert not unknown, f"Online configuration anchors not in pinned source: {sorted(unknown)}"
    # The two existing intentionally migrated examples must remain available.
    required = {"desc_site_url", "desc_site_name"}
    assert required <= rendered, f"Lost existing configuration help: {required-rendered}"
    remaining = sorted(source - rendered)
    report = {
        "source": "Pinned Geeklog 2.2.2 Core docs/english/config.html",
        "source_help_anchor_count": len(source),
        "online_help_anchor_count": len(rendered),
        "remaining_help_anchor_count": len(remaining),
        "percent_migrated": round(100 * len(source & rendered) / len(source), 2),
        "remaining_anchors": remaining,
        "note": "Coverage is structural only. Text, behavior and technical accuracy require review. Original embedded config.html stays byte-identical.",
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: pinned embedded configuration reference unchanged")
    print(f"COVERAGE: {len(rendered)}/{len(source)} help anchors on the online Markdown page; {len(remaining)} remaining")
    print(f"REPORT: {REPORT}")


if __name__ == "__main__":
    main()
