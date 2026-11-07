#!/usr/bin/env python3
"""Cross-guide website audit for online and embedded Geeklog documentation.

Static integrity check: it verifies generated files, internal fragments, guide
inventory and local navigation. It does not validate external HTTP services,
the editorial truth of prose, or administration runtime behavior.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re

ROOT = Path(__file__).resolve().parents[1]
ONLINE = ROOT / "dist/online"
OFFLINE = ROOT / "dist/geeklog-2.2.2/public_html/docs/english/modern"
REPORT = ROOT / "dist/online-guide-audit.json"

GUIDES = {
    "installation.html": "docs/installation/README.md",
    "configuration.html": "docs/configuration/README.md",
    "administration.html": "docs/administration/README.md",
    "modern/user-guide/overview/index.html": "docs/user-guide/README.md",
    "modern/user-guide/articles-and-topics/index.html": "docs/user-guide/articles-and-topics/README.md",
    "modern/user-guide/blocks-and-navigation/index.html": "docs/user-guide/blocks-and-navigation/README.md",
    "modern/user-guide/comments-and-moderation/index.html": "docs/user-guide/comments-and-moderation/README.md",
    "modern/plugins/plugin-installation-management/index.html": "docs/plugins/plugin-installation-management/README.md",
    "modern/development/plugin-development/index.html": "docs/development/plugin-development/README.md",
    "modern/development/theme-development/index.html": "docs/development/theme-development/README.md",
    "modern/user-guide/syndication-rss-autotags/index.html": "docs/user-guide/syndication-rss-autotags/README.md",
    "modern/plugins/bundled-plugins/index.html": "docs/plugins/bundled-plugins/README.md",
    "modern/reference/database-schema/index.html": "docs/reference/database-schema/README.md",
    "modern/administration/troubleshooting-faq/index.html": "docs/administration/troubleshooting-faq/README.md",
    "modern/development/contributing/index.html": "docs/development/contributing/README.md",
    "modern/development/plugin-api/index.html": "docs/development/plugin-api/README.md",
    "modern/development/templates/index.html": "docs/development/templates/README.md",
    "modern/plugins/static-pages/index.html": "docs/plugins/static-pages/README.md",
    "modern/development/webservices/index.html": "docs/development/webservices/README.md",
    "modern/development/configuration-api/index.html": "docs/development/configuration-api/README.md",
    "modern/administration/users-and-groups/index.html": "docs/administration/users-and-groups/README.md",
    "modern/development/security-and-permissions/index.html": "docs/development/security-and-permissions/README.md",
    "modern/administration/backup-and-recovery/index.html": "docs/administration/backup-and-recovery/README.md",
    "modern/administration/maintenance/index.html": "docs/administration/maintenance/README.md",
    "modern/administration/troubleshooting/index.html": "docs/administration/troubleshooting/README.md",
}

class Inspect(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.refs = []
        self.title_count = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for target in (a.get("id"), a.get("name") if tag == "a" else None):
            if target:
                self.ids.add(target)
        if tag == "h1":
            self.title_count += 1
        for field in (("href",) if tag in ("a", "link") else ("src",) if tag in ("script", "img") else ()):
            if a.get(field):
                self.refs.append(a[field])

def inspect(page):
    p = Inspect()
    p.feed(page.read_text(encoding="utf-8"))
    return p

def local_links(site, pages):
    checked = 0
    fragments = 0
    for page in pages:
        info = inspect(page)
        assert info.title_count == 1, f"Expected one H1: {page}"
        for link in info.refs:
            url = urlsplit(link)
            if url.scheme or url.netloc or link.startswith("//"):
                continue
            dest = (page.parent / unquote(url.path)).resolve() if url.path else page.resolve()
            assert dest.is_relative_to(site.resolve()), f"Link escapes site: {page}: {link}"
            assert dest.is_file(), f"Broken local link: {page}: {link}"
            checked += 1
            if url.fragment and dest.suffix == ".html":
                assert unquote(url.fragment) in inspect(dest).ids, f"Missing fragment: {page}: {link}"
                fragments += 1
    return checked, fragments

def main():
    assert ONLINE.is_dir() and OFFLINE.is_dir(), "Build online and embedded docs first"
    indexed = json.loads((ONLINE / "search-index.json").read_text(encoding="utf-8"))
    expected = set(GUIDES)
    observed = [entry["url"] for entry in indexed]
    assert len(observed) == len(set(observed)) == 25, "Duplicate/incorrect search entries"
    assert set(observed) == expected, "Search index misses or invents guides"
    for path, source in GUIDES.items():
        assert (ROOT / source).is_file(), f"Source guide missing: {source}"
        assert (ONLINE / path).is_file(), f"Published guide missing: {path}"
        body = (ROOT / source).read_text(encoding="utf-8")
        assert re.search(r"(?m)^# ", body), f"Missing title: {source}"
        if path.startswith("modern/"):
            assert not re.search(
                r"https://geeklog-core[.]github[.]io/documentation/modern/",
                body
            ), f"Use a relative cross-guide URL for online/offline navigation: {source}"
            embedded = OFFLINE / path.removeprefix("modern/")
            assert embedded.is_file(), f"Embedded modern guide missing: {path}"
            assert embedded.read_bytes() == (ONLINE / path).read_bytes(), (
                f"Online/embedded guide mismatch: {path}"
            )
    # Each modern guide needs two contextual onward routes; these links must
    # resolve in both outputs and remain independent from the public host.
    related_count = 0
    for path in GUIDES:
        if not path.startswith("modern/"):
            continue
        info = inspect(ONLINE / path)
        markup = (ONLINE / path).read_text(encoding="utf-8")
        assert markup.count('class="related-guides"') == 1, (
            f"Missing or duplicate related reading: {path}"
        )
        assert markup.count('aria-label="Related documentation"') == 1
        assert markup.count('<h2>Continue reading</h2>') == 1
        related_links = re.findall(
            r'<a href="([.][.]/[.][.]/[^"]+/index[.]html)">',
            markup.split('class="related-guides"', 1)[1]
        )
        assert len(related_links) == len(set(related_links)) == 2, (
            f"Expected two distinct related links: {path}"
        )
        related_count += len(related_links)
    # External link inventory only: remote sites are not fetched in CI.
    # Pin Core source links to the release discussed by these guides rather
    # than silently using a changing master/main revision.
    external = {}
    unpinned = []
    for path, source in GUIDES.items():
        markdown_text = (ROOT / source).read_text(encoding="utf-8")
        for url in re.findall(r"(?<!!)\[[^\]]+\]\((https?://[^)\s]+)\)", markdown_text):
            parsed = urlsplit(url)
            external[parsed.netloc] = external.get(parsed.netloc, 0) + 1
            if re.match(
                r"^https://github[.]com/Geeklog-Core/geeklog/(?:blob|tree)/(?:main|master)/",
                url,
            ):
                unpinned.append({"source": source, "url": url})
    assert sum(external.values()) >= 20, "External-link inventory unexpectedly empty or incomplete"
    assert not unpinned, f"Unpinned Core source links in versioned guides: {unpinned}"
    online_pages = sorted(ONLINE.rglob("*.html"))
    embedded_pages = sorted(OFFLINE.rglob("*.html"))
    online_links, online_fragments = local_links(ONLINE, online_pages)
    embedded_links, embedded_fragments = local_links(OFFLINE, embedded_pages)
    report = {
        "scope": "Static generated-site navigation and source inventory only",
        "indexed_guides": len(indexed),
        "online_html_pages": len(online_pages),
        "embedded_modern_html_pages": len(embedded_pages),
        "contextual_related_links": related_count,
        "online_local_refs_checked": online_links,
        "online_fragments_checked": online_fragments,
        "embedded_local_refs_checked": embedded_links,
        "embedded_fragments_checked": embedded_fragments,
        "external_link_occurrences": sum(external.values()),
        "external_hosts": dict(sorted(external.items())),
        "unpinned_core_source_links": unpinned,
        "external_web_links_checked_live": False,
        "editorial_semantics_certified": False,
        "geeklog_runtime_tested": False,
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("PASS: 25 unique indexed guides with source Markdown and generated pages")
    print(f"PASS: {related_count} distinct contextual guide links across 22 modern pages")
    print(f"PASS: online HTML {len(online_pages)} pages, {online_links} local links, {online_fragments} fragments")
    print(f"PASS: embedded modern {len(embedded_pages)} pages, {embedded_links} local links, {embedded_fragments} fragments")
    print(f"PASS: {sum(external.values())} external reference occurrences inventoried; no unpinned Geeklog Core source URLs")
    print("NOTE: external targets NOT fetched; live Geeklog behavior and editorial provenance remain separate checks")

if __name__ == "__main__":
    main()
