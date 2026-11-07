#!/usr/bin/env python3
"""Verify canonical public navigation while retaining versioned embedded help.

No redirect or public compatibility pages are allowed. This validates generated
files and links, not the live GitHub Pages deployment or Geeklog runtime.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "dist/online"
EMBED = ROOT / "dist/geeklog-2.2.2/public_html/docs/english"
LEGACY_WEB = ("installation.html", "configuration.html", "administration.html")
REQUIRED = ("installation/", "configuration/", "administration/", "user-guide/",
            "administration/troubleshooting/", "reference/database-schema/")
FORBIDDEN_PUBLIC = ("modern/", "administration/troubleshooting-faq/")
BAD_URL = re.compile(
    r"https://geeklog-core[.]github[.]io/documentation/(?:modern/|(?:installation|configuration|administration)[.]html)"
)

class HTMLLinks(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "a" and a.get("name"):
            self.ids.add(a["name"])
        if tag in ("a", "link") and a.get("href"):
            self.links.append(a["href"])
        if tag in ("script", "img") and a.get("src"):
            self.links.append(a["src"])

def main():
    assert SITE.is_dir() and (SITE / "index.html").is_file()
    indexed = json.loads((SITE / "search-index.json").read_text(encoding="utf-8"))
    urls = [item["url"] for item in indexed]
    assert len(urls) == len(set(urls)) == 24, "Expected 24 unique canonical guide URLs"
    assert all(url.endswith("/") and not url.startswith("modern/") for url in urls)
    assert all((SITE / url / "index.html").is_file() for url in urls)
    assert all((SITE / slug / "index.html").is_file() for slug in REQUIRED)
    assert not any((SITE / slug).exists() for slug in FORBIDDEN_PUBLIC)
    assert not any((SITE / file).exists() for file in LEGACY_WEB), "No public compatibility pages"
    assert len(list(SITE.rglob("*.html"))) == 25, "Unexpected public HTML output"
    home = (SITE / "index.html").read_text(encoding="utf-8")
    assert home.count('class="docs-topic-group"') == 6
    assert "Technical Reference" in home and "Reference &amp; Archive" not in home
    assert 'aria-label="Start here: beginner learning path"' in home
    assert 'href="installation/"' in home and 'href="administration/backup-and-recovery/"' in home
    troubleshooting = (SITE / "administration/troubleshooting/index.html").read_text(encoding="utf-8")
    assert "Frequently asked questions" in troubleshooting and "HTTP 500" in troubleshooting
    for url in urls:
        if url in ("installation/", "configuration/", "administration/"):
            continue
        page = (SITE / url / "index.html").read_text(encoding="utf-8")
        assert 'aria-label="Breadcrumb"' in page, url
        assert 'aria-label="Documentation sections"' in page, url
        assert 'aria-label="Previous and next guides"' in page, url
        assert 'aria-label="On this page"' in page, url
    checked = 0
    for page in SITE.rglob("*.html"):
        data = page.read_text(encoding="utf-8")
        assert not BAD_URL.search(data), f"Old public URL in {page}"
        parsed = HTMLLinks()
        parsed.feed(data)
        for ref in parsed.links:
            part = urlsplit(ref)
            if part.scheme or part.netloc or ref.startswith("//"):
                continue
            destination = (page.parent / unquote(part.path)).resolve() if part.path else page.resolve()
            if destination.is_dir():
                destination = destination / "index.html"
            assert destination.is_relative_to(SITE.resolve()) and destination.is_file(), (
                f"Broken public link: {page}: {ref}"
            )
            if part.fragment and destination.suffix == ".html":
                target = HTMLLinks()
                target.feed(destination.read_text(encoding="utf-8"))
                assert unquote(part.fragment) in target.ids, (
                    f"Broken public fragment: {page}: {ref}"
                )
            checked += 1
    assert (EMBED / "config.html").is_file()
    assert (EMBED / "install.html").is_file()
    assert (EMBED / "modern/index.html").is_file()
    assert (EMBED / "modern/administration/troubleshooting-faq/index.html").is_file()
    print(f"PASS: 24 canonical public routes, 6 categories, beginner journey, compact guide navigation")
    print(f"PASS: no public /modern/, root legacy .html pages, separate FAQ, or redirects; {checked} links")
    print("PASS: original embedded Geeklog 2.2.2 help layout retained")

if __name__ == "__main__":
    main()
