#!/usr/bin/env python3
"""Render a non-deployable embedded configuration candidate from maintained Markdown.

This creates a separate review artifact. It must NEVER overwrite the embedded
Geeklog 2.2.2 config.html, which stays byte-identical to the tagged release.
Run after the dual documentation build, with GEEKLOG_CORE_DOCS set.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import os
import re
import zipfile

import markdown

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/configuration/README.md"
LEGACY = Path(os.environ["GEEKLOG_CORE_DOCS"]) / "english/config.html"
ORIGINAL_TREE = ROOT / "dist/geeklog-2.2.2/public_html"
OUTPUT = ROOT / "dist/config-candidate/public_html/docs/english/config.html"
REPORT = ROOT / "dist/config-candidate-report.json"
ARCHIVE = ROOT / "dist/config-candidate-review.zip"


class Inspect(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.anchors = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.anchors.extend(a[n] for n in ("id", "name") if a.get(n))
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "link" and a.get("href"):
            self.links.append(a["href"])


def parsed(html):
    obj = Inspect()
    obj.feed(html)
    return obj


def main():
    assert LEGACY.is_file() and SOURCE.is_file()
    original = parsed(LEGACY.read_text(encoding="utf-8"))
    md = SOURCE.read_text(encoding="utf-8")
    body = markdown.markdown(md, extensions=["tables", "fenced_code", "toc"])
    # Old relative stylesheet layout must remain resolvable at docs/english.
    candidate = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Geeklog 2.2.2 configuration reference</title>'
        '<link rel="stylesheet" href="../docstyle.css"></head>'
        '<body><main>' + body + '</main></body></html>'
    )
    current = parsed(candidate)
    historical = set(original.anchors)
    generated = set(current.anchors)
    missing = sorted(historical - generated)
    extra = sorted(generated - historical)
    assert not missing, f"Missing historical anchors: {missing[:10]}"
    assert not extra, f"Unexpected historical anchors: {extra[:10]}"
    assert len(historical) == 449
    assert len(current.anchors) == len(generated), "Duplicated generated anchors"
    assert body.count("Documented default (Geeklog 2.2.2)") == 387, (
        "Not all 387 historical defaults are present in the candidate"
    )

    # Work out link destinations as if config.html were installed in the
    # existing validated 2.2.2 archive. Do not mutate that archive.
    linked = 0
    for link in current.links:
        target = urlsplit(link)
        if target.scheme or target.netloc or link.startswith("//"):
            continue
        source_relative = Path("docs/english/config.html")
        next_path = (source_relative.parent / unquote(target.path)) if target.path else source_relative
        import posixpath
        normalized = posixpath.normpath(next_path.as_posix())
        assert not normalized.startswith("../"), f"Path escapes site: {link}"
        if normalized == "docs/english/config.html":
            match = current
        else:
            located = ORIGINAL_TREE / normalized
            assert located.is_file(), f"Missing local document or asset: {link}"
            match = parsed(located.read_text(encoding="utf-8")) if located.suffix == ".html" else None
        if target.fragment and match is not None:
            assert unquote(target.fragment) in match.anchors, f"Missing fragment: {link}"
        linked += 1

    assert (ORIGINAL_TREE / "docs/docstyle.css").is_file()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(candidate + "\n", encoding="utf-8")
    # One file only: recipient may preview/inspect it, never auto-deploy it.
    with zipfile.ZipFile(ARCHIVE, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(OUTPUT, "public_html/docs/english/config.html")
    report = {
        "scope": "Geeklog 2.2.2 candidate for review ONLY; not deployed",
        "candidate_html": str(OUTPUT.relative_to(ROOT)),
        "historical_unique_anchors": len(historical),
        "generated_unique_anchors": len(generated),
        "historical_defaults_transcribed": 387,
        "candidate_local_links_checked": linked,
        "legacy_embedded_configuration_replaced": False,
        "outstanding": [
            "Full semantic/text/table/example parity with tagged original",
            "Editorial provenance and contributor license review",
            "Real context-sensitive admin help tests against this candidate",
            "Maintainer approval before any official replacement",
        ],
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("PASS: candidate generated from Markdown, 449 historical anchors, 387 defaults")
    print(f"PASS: {linked} candidate local links, referenced assets and fragments checked")
    print("NOTE: candidate is an isolated review artifact, NOT a production replacement")


if __name__ == "__main__":
    main()
