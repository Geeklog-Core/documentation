#!/usr/bin/env python3
"""Inventory links in the tagged Geeklog 2.2.2 config reference.

The archive preserves legacy help. This report classifies outgoing references
for editorial decisions, without asserting that the external sites are live.
"""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import os
import posixpath

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(os.environ["GEEKLOG_CORE_DOCS"]) / "english/config.html"
MARKDOWN = ROOT / "docs/configuration/README.md"
REPORT = ROOT / "dist/config-link-audit.json"
SITE = ROOT / "dist/geeklog-2.2.2/public_html"


class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.anchors = set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "a" and values.get("name"):
            self.anchors.add(values["name"])
        if values.get("id"):
            self.anchors.add(values["id"])
        if tag in ("a", "link") and values.get("href"):
            self.links.append(values["href"])


def main():
    old = Links()
    old.feed(SOURCE.read_text(encoding="utf-8"))
    markdown = MARKDOWN.read_text(encoding="utf-8")
    results = []
    for href, uses in sorted(Counter(old.links).items()):
        parsed = urlsplit(href)
        if parsed.scheme in ("http", "https") or parsed.netloc:
            kind = "external"
            state = "editorial-review-needed"
            if "wiki.geeklog.net" in parsed.netloc.lower():
                state = "legacy-wiki-attribution-and-replacement-needed"
        elif not parsed.path and parsed.fragment:
            kind = "fragment"
            state = ("anchor-preserved" if unquote(parsed.fragment) in old.anchors
                     else "missing-source-anchor")
        else:
            kind = "local-file"
            location = posixpath.normpath(
                posixpath.join("docs/english", unquote(parsed.path)))
            assert not location.startswith("../"), f"Escaping legacy link: {href}"
            state = "file-present" if (SITE / location).is_file() else "file-missing"
        results.append({
            "href": href, "kind": kind, "source_occurrences": uses,
            "status": state,
            "linked_from_modern_markdown": href in markdown,
        })

    assert len([r for r in results if r["kind"] == "fragment"]) == 34, (
        "Unexpected number of distinct local fragment links")
    assert all(r["status"] == "anchor-preserved"
               for r in results if r["kind"] == "fragment"), (
                   "Historic config.html contains a dangling fragment")
    assert all(r["status"] == "file-present"
               for r in results if r["kind"] == "local-file"), (
                   "Missing historical local file in the 2.2.2 archive")
    # Escaped <a href="%s"> inside a <pre> is text, NOT a real href.
    assert not any(r["href"] == "%s" for r in results), (
        "Incorrectly parsed a literal printf template as a navigation link")

    counter = Counter(r["kind"] for r in results)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps({
        "source": "Geeklog-Core/geeklog v2.2.2 public_html/docs/english/config.html",
        "note": "Link inventory only; external HTTP status, safety and redirect targets NOT tested",
        "counts": dict(sorted(counter.items())),
        "all_original_fragments_resolve": True,
        "items": results,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("PASS: legacy link audit: " + ", ".join(
        f"{k}={v}" for k, v in sorted(counter.items())))
    print("NOTE: external links still require human replacement/retention review")


if __name__ == "__main__":
    main()
