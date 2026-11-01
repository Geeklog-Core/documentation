#!/usr/bin/env python3
"""Validate legacy installation fragment IDs in Markdown and rendered HTML.

This independent branch uses Python-Markdown and does not rely on the
unmerged foundation PR.
"""
from html.parser import HTMLParser
from pathlib import Path
import shutil
from urllib.parse import urlsplit, unquote
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
        self.links = []
        self.assets = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.names.add(attrs["name"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag in ("img", "script") and attrs.get("src"):
            self.assets.append(attrs["src"])
        if tag == "link" and attrs.get("href"):
            self.assets.append(attrs["href"])

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
    root_build = ROOT / "build"
    (root_build / "images").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / "assets/install.css", root_build / "docstyle.css")
    # Stand-in GIF at the historical path only; NOT Geeklog branding artwork.
    (root_build / "images/logo.gif").write_bytes(bytes.fromhex(
        "47494638396101000100800000ffffff00000021f9040100000000"
        "2c00000000010001000002024401003b"
    ))
    html_body = (
        '<nav><a href="index.html">Documentation preview</a> '
        '<a href="support.html">Support</a></nav>'
        '<p><img src="../images/logo.gif" alt="" width="1" height="1"></p>'
        + html
    )
    full_html = (
        '<!doctype html>\\n<html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>Installing Geeklog — preview</title>'
        '<link rel="stylesheet" href="../docstyle.css"></head><body>\\n'
        + html_body + '\\n</body></html>\\n'
    )
    OUTPUT.write_text(full_html, encoding="utf-8")
    (OUTPUT.parent / "index.html").write_text(
        '<!doctype html><html lang="en"><meta charset="utf-8">'
        '<title>Documentation preview</title><link rel="stylesheet" href="../docstyle.css">'
        '<h1>Documentation preview</h1><a href="install.html">Installation draft</a>',
        encoding="utf-8",
    )
    (OUTPUT.parent / "support.html").write_text(
        '<!doctype html><html lang="en"><meta charset="utf-8">'
        '<title>Support preview</title><link rel="stylesheet" href="../docstyle.css">'
        '<h1>Support placeholder</h1><a href="install.html">Installation draft</a>',
        encoding="utf-8",
    )
    found = Anchors()
    found.feed(full_html)
    # Link/asset checks are intentionally strict for locally generated files.
    # Remote links are listed for later human review, not tested for uptime.
    remote = []
    for url in found.links + found.assets:
        parts = urlsplit(url)
        if parts.scheme in ("http", "https", "mailto"):
            remote.append(url)
            continue
        assert not parts.scheme and not parts.netloc, f"Unsupported local URI: {url}"
        target = unquote(parts.path)
        if not target:
            assert parts.fragment in found.ids | found.names, f"Broken fragment: {url}"
            continue
        assert not target.startswith("/"), f"Absolute local path: {url}"
        # Relative resources must remain within the generated documentation directory.
        destination = (OUTPUT.parent / target).resolve()
        assert destination.is_relative_to((ROOT / "build").resolve()), f"Unsafe relative path: {url}"
        assert destination.exists(), f"Missing generated relative link/asset: {url}"
    print(f"PASS: local links/assets resolved; {len(remote)} remote references require separate review")
    print(f"PASS: all {len(REQUIRED)} legacy installation anchors present in generated HTML")

if __name__ == "__main__":
    main()
