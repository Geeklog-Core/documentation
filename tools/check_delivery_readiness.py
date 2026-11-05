#!/usr/bin/env python3
"""Release-candidate checks for the combined online and Geeklog 2.2.2 outputs.

Run after build_site_search.py and check_dual_archive.py. This is a structural
delivery gate, not a substitute for editorial review or installed CMS testing.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "dist/online"
ARCHIVE = ROOT / "dist/geeklog-2.2.2-docs-preview.zip"
REPORT = ROOT / "dist/delivery-readiness.json"
LEGACY_CONFIG = "public_html/docs/english/config.html"
LEGACY_INSTALL = "public_html/docs/english/install.html"
MODERN = "public_html/docs/english/modern/"

class Inspect(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.identifiers = set()
        self.references = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.identifiers.update(x for x in (a.get("id"), a.get("name")) if x)
        if tag in ("a", "link") and a.get("href"):
            self.references.append(a["href"])
        if tag in ("script", "img") and a.get("src"):
            self.references.append(a["src"])

def inspect(data):
    p = Inspect()
    p.feed(data)
    return p

def validate_site():
    assert (SITE / "index.html").is_file(), "Missing online home page"
    records = json.loads((SITE / "search-index.json").read_text(encoding="utf-8"))
    assert len(records) == 13, f"Expected 13 searchable guides, got {len(records)}"
    urls = [entry["url"] for entry in records]
    assert len(set(urls)) == len(urls), "Duplicate search URL"
    assert all(entry.get("title") and entry.get("text") for entry in records), "Empty search entry"
    assert "configuration.html" in urls and "installation.html" in urls
    assert sum(u.startswith("modern/") for u in urls) == 10
    page_count = 0
    references_checked = 0
    for page in SITE.rglob("*.html"):
        page_count += 1
        info = inspect(page.read_text(encoding="utf-8"))
        for reference in info.references:
            target = urlsplit(reference)
            if target.scheme or target.netloc or reference.startswith("//"):
                continue
            destination = (page.parent / unquote(target.path)).resolve() if target.path else page.resolve()
            assert destination.is_relative_to(SITE.resolve()), f"Path escapes site: {page}: {reference}"
            assert destination.is_file(), f"Broken site reference: {page}: {reference}"
            if target.fragment and destination.suffix == ".html":
                dest = inspect(destination.read_text(encoding="utf-8"))
                assert unquote(target.fragment) in dest.identifiers, f"Broken fragment: {page}: {reference}"
            references_checked += 1
    assert page_count == 15, f"Expected 15 HTML pages, got {page_count}"
    home = (SITE / "index.html").read_text(encoding="utf-8")
    assert 'id="docs-search"' in home and 'src="search.js"' in home
    assert home.count('aria-label="Browse all guides"') == 1
    for url in urls:
        assert 'href="' + url + '"' in home, f"Guide not visible from homepage: {url}"
    assert (SITE / "search.js").is_file()
    config = inspect((SITE / "configuration.html").read_text(encoding="utf-8"))
    assert "desc_site_url" in config.identifiers
    return {"online_html_pages": page_count, "searchable_guides": len(records),
            "modern_guides": 10, "local_references_checked": references_checked}

def validate_embedded():
    with zipfile.ZipFile(ARCHIVE) as z:
        names = z.namelist()
        assert len(names) == len(set(names)), "Duplicate ZIP paths"
        for name in names:
            path = Path(name)
            assert name.startswith("public_html/") and ".." not in path.parts
        assert LEGACY_CONFIG in names and LEGACY_INSTALL in names
        assert MODERN + "index.html" in names
        modern_pages = [name for name in names if name.startswith(MODERN) and name.endswith(".html")]
        assert len(modern_pages) == 11, f"Expected 11 modern HTML pages, got {len(modern_pages)}"
        embedded_index = json.loads(z.read(MODERN + "search-index.json"))
        assert len(embedded_index) == 10, "Expected ten searchable offline guides"
        assert len({item["url"] for item in embedded_index}) == 10
        for item in embedded_index:
            assert MODERN + item["url"] in names, f"Offline search entry missing: {item['url']}"
        # Check each generated modern guide from its final ZIP path, including
        # CSS, scripts, navigation links, and intra/inter-page fragments.
        checked = 0
        for name in modern_pages:
            parsed = inspect(z.read(name).decode("utf-8"))
            for reference in parsed.references:
                parts = urlsplit(reference)
                if parts.scheme or parts.netloc or reference.startswith("//"):
                    continue
                path = Path(name).parent / unquote(parts.path) if parts.path else Path(name)
                normalized = __import__("posixpath").normpath(path.as_posix())
                assert normalized.startswith(MODERN), f"Embedded link escapes modern docs: {name}: {reference}"
                assert normalized in names, f"Broken offline ZIP link: {name}: {reference}"
                if parts.fragment and normalized.endswith(".html"):
                    dest = inspect(z.read(normalized).decode("utf-8"))
                    assert unquote(parts.fragment) in dest.identifiers, (
                        f"Broken offline ZIP fragment: {name}: {reference}")
                checked += 1
        assert checked > 30, f"Suspiciously few embedded references tested: {checked}"
        assert b"desc_site_url" in z.read(LEGACY_CONFIG)
        assert b"installation_requirements" in z.read(LEGACY_INSTALL)
        for name in ("calendar","links","polls","spamx","staticpages","xmlsitemap"):
            assert "public_html/docs/english/" + name + ".html" in names
        assert "public_html/admin/plugins/recaptcha/docs/english/config.html" in names
        for suffix in ("style.css", "search.js", "search-index.json"):
            assert MODERN + suffix in names
        return {"zip_entries":len(names),"modern_embedded_html_pages":len(modern_pages),
                "legacy_help_pages_preserved": True,
                "offline_modern_references_checked": checked}

def main():
    report = {"scope":"Geeklog 2.2.2 preliminary delivery readiness",
              "online":validate_site(),"embedded":validate_embedded(),
              "status":"STRUCTURAL_PASS_ONLY",
              "outstanding":["editorial/provenance review",
                             "manual inspection of the deployed official site",
                             "final rebuilt ZIP integration in isolated Geeklog 2.2.2",
                             "real administrator/plugin context-sensitive help interactions",
                             "complete historical config content parity before replacement"]}
    REPORT.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print("PASS: 13 indexed guides, 15 online pages, all local site references, legacy help paths and embedded ZIP layout")
    print("NOTE: this does not certify a production release or complete Wiki/config migration")

if __name__ == "__main__":
    main()
