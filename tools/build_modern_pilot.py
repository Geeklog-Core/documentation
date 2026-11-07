#!/usr/bin/env python3
"""Build one modern Markdown documentation subset to online + embedded HTML.

This supplements, but does not replace, the pinned 2.2.2 docs until the
existing dual-output builder is integrated. No legacy page or anchor is changed.
"""
from pathlib import Path
from html import escape
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import re
import shutil
import posixpath
import markdown

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ONLINE = ROOT / "dist/modern-online"
EMBED = ROOT / "dist/modern-embedded/public_html/docs/english/modern"
SOURCES = [
    ("user-guide/overview", "Using Geeklog: User Guide"),
    ("user-guide/articles-and-topics", "Articles, Topics and Publishing"),
    ("user-guide/blocks-and-navigation", "Blocks, Menus and Navigation"),
    ("user-guide/comments-and-moderation", "Comments and Moderation"),
    ("plugins/plugin-installation-management", "Plugin Installation and Management"),
    ("development/plugin-development", "Plugin Development: Step by Step"),
    ("development/theme-development", "Theme Development: Step by Step"),
    ("user-guide/syndication-rss-autotags", "Syndication, RSS and Autotags"),
    ("plugins/bundled-plugins", "Bundled Plugins Reference"),
    ("reference/database-schema", "Database Schema and Data Model"),
    ("administration/troubleshooting-faq", "Troubleshooting and FAQ"),
    ("development/contributing", "Contributing to Geeklog"),
    ("development/plugin-api", "Plugin API"),
    ("development/templates", "Themes and templates"),
    ("plugins/static-pages", "Static Pages"),
    ("development/webservices", "Webservices API"),
    ("development/configuration-api", "Configuration API"),
    ("administration/users-and-groups", "Users and groups"),
    ("development/security-and-permissions", "Security and permissions"),
    ("administration/backup-and-recovery", "Backup and recovery"),
    ("administration/maintenance", "Maintenance and upgrades"),
    ("administration/troubleshooting", "Troubleshooting"),
]
# Web-only route mapping. Existing embedded HTML keeps its historical subtree.
ONLINE_EXCLUDED = {"administration/troubleshooting-faq"}
def route(slug):
    if slug == "user-guide/overview":
        return "user-guide/"
    if slug == "administration/troubleshooting-faq":
        return "administration/troubleshooting/"
    return slug + "/"

def online_link(current_slug, href):
    parts = urlsplit(href)
    if parts.scheme or parts.netloc or href.startswith("//") or not parts.path:
        return href
    # Markdown links were authored relative to the original embedded /modern/ pages.
    old = posixpath.normpath(posixpath.join("modern", current_slug, parts.path))
    if old == "modern/index.html":
        dest = ""
    elif old in ("installation.html", "configuration.html", "administration.html"):
        dest = old.removesuffix(".html") + "/"
    elif old.startswith("modern/") and old.endswith("/index.html"):
        dest = route(old[len("modern/"):-len("/index.html")])
    elif old.startswith("modern/") and old.endswith(".html"):
        dest = None
    else:
        dest = None
    if dest is None:
        # Files, images and unknown links preserve their relative form for link audits.
        return href
    here = route(current_slug).rstrip("/")
    relative = posixpath.relpath(dest.rstrip("/") or ".", here or ".")
    if dest:
        relative = ("./" if relative == "." else relative + "/")
    else:
        relative = posixpath.relpath(".", here or ".") + "/"
    return relative + (("?" + parts.query) if parts.query else "") + (("#" + parts.fragment) if parts.fragment else "")

def rewrite_online_links(html, slug):
    return re.sub(r'href="([^"]+)"', lambda match:
                  'href="' + online_link(slug, match.group(1)) + '"', html)

# Each guide offers two actionable follow-up paths without leaving the current
# generated documentation tree. These references work in both website and ZIP.
RELATED = {
    "user-guide/overview": ("user-guide/articles-and-topics", "user-guide/blocks-and-navigation"),
    "user-guide/articles-and-topics": ("user-guide/comments-and-moderation", "plugins/static-pages"),
    "user-guide/blocks-and-navigation": ("development/theme-development", "plugins/static-pages"),
    "user-guide/comments-and-moderation": ("user-guide/articles-and-topics", "administration/troubleshooting-faq"),
    "plugins/plugin-installation-management": ("plugins/bundled-plugins", "administration/backup-and-recovery"),
    "development/plugin-development": ("development/plugin-api", "development/configuration-api"),
    "development/theme-development": ("development/templates", "user-guide/blocks-and-navigation"),
    "user-guide/syndication-rss-autotags": ("user-guide/articles-and-topics", "plugins/static-pages"),
    "plugins/bundled-plugins": ("plugins/plugin-installation-management", "plugins/static-pages"),
    "reference/database-schema": ("development/configuration-api", "administration/backup-and-recovery"),
    "administration/troubleshooting-faq": ("administration/troubleshooting", "administration/maintenance"),
    "development/contributing": ("development/plugin-development", "development/security-and-permissions"),
    "development/plugin-api": ("development/configuration-api", "development/security-and-permissions"),
    "development/templates": ("plugins/static-pages", "development/plugin-api"),
    "plugins/static-pages": ("development/templates", "administration/users-and-groups"),
    "development/webservices": ("development/plugin-api", "development/security-and-permissions"),
    "development/configuration-api": ("development/plugin-api", "administration/maintenance"),
    "administration/users-and-groups": ("development/security-and-permissions", "administration/troubleshooting"),
    "development/security-and-permissions": ("administration/users-and-groups", "development/plugin-api"),
    "administration/backup-and-recovery": ("administration/maintenance", "administration/troubleshooting"),
    "administration/maintenance": ("administration/backup-and-recovery", "administration/troubleshooting"),
    "administration/troubleshooting": ("administration/maintenance", "administration/backup-and-recovery"),
}

def related_guides(slug, online=False):
    titles = dict(SOURCES)
    assert set(RELATED) == set(titles), "Related navigation must cover every modern guide"
    targets = tuple("administration/troubleshooting" if x in ONLINE_EXCLUDED and online else x for x in RELATED[slug])
    assert len(targets) == len(set(targets)) == 2 and slug not in targets
    assert all(target in titles for target in targets), f"Unknown related guide: {slug}"
    links = ''.join(
        '<li><a href="' + (online_link(slug, "../../" + target + "/index.html") if online else "../../" + target + "/index.html") + '">' +
        escape(titles[target]) + '</a></li>'
        for target in targets
    )
    return ('<aside class="related-guides" aria-label="Related documentation">'
            '<h2>Continue reading</h2><ul>' + links + '</ul></aside>')

CSS = """*{box-sizing:border-box}body{font:16px/1.65 system-ui,sans-serif;color:#202b36;max-width:1040px;margin:0 auto;padding:20px}header,footer{padding:16px 0;border-bottom:1px solid #ddd}footer{border-top:1px solid #ddd;border-bottom:0}nav{display:flex;flex-wrap:wrap;gap:14px}a{color:#1763a5}main{padding:18px 0}pre{padding:16px;background:#f4f6f8;overflow:auto}code{overflow-wrap:anywhere}blockquote{padding:8px 16px;background:#fff6de;border-left:4px solid #ba8b21}table{border-collapse:collapse;max-width:100%;display:block;overflow-x:auto}td,th{padding:6px 10px;border:1px solid #cdd}input[type=search]{font:inherit;width:100%;padding:12px;margin:12px 0;border:1px solid #aaa;border-radius:6px}.related-guides{margin-top:2rem;padding:1rem 1.25rem;border-top:1px solid #cdd;background:#f6f8fa}.related-guides h2{font-size:1.15rem;margin:.1rem 0 .6rem}.related-guides ul{margin:.4rem 0;padding-left:1.5rem}.related-guides li{margin:.35rem 0}"""
class Inspect(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"): self.ids.add(a["id"])
        if tag == "a" and a.get("href"): self.links.append(a["href"])
        if tag == "link" and a.get("href"): self.links.append(a["href"])
        if tag == "script" and a.get("src"): self.links.append(a["src"])


def relative_nav(depth):
    pre = "../" * depth
    return '<nav><a href="' + pre + 'index.html">Documentation home</a>' + ''.join(
        '<a href="' + pre + slug + '/index.html">' + escape(title) + '</a>'
        for slug, title in SOURCES
    ) + '</nav>'


def wrap(title, body, depth):
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>' + escape(title) + ' — Geeklog documentation</title>'
            '<link rel="stylesheet" href="' + '../'*depth + 'style.css"></head>'
            '<body><header>' + relative_nav(depth) + '</header><main>' + body
            + '</main><footer>Geeklog documentation · Geeklog 2.2.2 reference · '
              'verify version-specific APIs before production use</footer></body></html>')


def write_site(directory, online=False):
    directory.mkdir(parents=True, exist_ok=True)
    styles = directory / "style.css"
    previous_styles = styles.read_text(encoding="utf-8") if online and styles.is_file() else ""
    styles.write_text(previous_styles + "\n" + CSS, encoding="utf-8")
    records = []
    visible = [(slug, title) for slug, title in SOURCES if not online or slug not in ONLINE_EXCLUDED]
    groups = (
        ("Getting Started", ("installation/", "configuration/")),
        ("User Guide", ("user-guide/",)),
        ("Administration", ("administration/",)),
        ("Plugins", ("plugins/plugin-installation-management/",)),
        ("Development & Theming", ("development/plugin-development/",)),
        ("Technical Reference", ("reference/database-schema/",)),
    )
    for index, (slug, title) in enumerate(visible):
        source = DOCS / ("user-guide" if slug == "user-guide/overview" else slug) / "README.md"
        if not source.is_file():
            raise FileNotFoundError(source)
        md = source.read_text(encoding="utf-8")
        body = markdown.markdown(md, extensions=["tables", "fenced_code", "toc"])
        if online:
            body = rewrite_online_links(body, slug)
            dest_slug = route(slug)
            root_relative = "../" * len(dest_slug.rstrip("/").split("/"))
            breadcrumb = '<nav aria-label="Breadcrumb"><a href="' + root_relative + '">Documentation</a> / ' + escape(title) + '</nav>'
            sections = ''.join('<a href="' + root_relative + path + '">' + escape(label) + '</a>' for label, paths in groups for path in paths[:1])
            site_nav = '<nav aria-label="Documentation sections" class="sections">' + sections + '</nav>'
            headings = re.findall(r'<h[23] id="([^"]+)">([^<]+)</h[23]>', body)
            toc = ('<nav aria-label="On this page"><h2>On this page</h2><ul>' +
                   ''.join('<li><a href="#' + escape(anchor) + '">' + label + '</a></li>' for anchor, label in headings) +
                   '</ul></nav>') if headings else ''
            previous = visible[index - 1] if index else None
            following = visible[index + 1] if index + 1 < len(visible) else None
            def adjacent(item, label):
                if not item: return ''
                target = posixpath.relpath(route(item[0]).rstrip("/"), dest_slug.rstrip("/"))
                return '<a href="' + (("./" if target == "." else target + "/")) + '">' + label + ': ' + escape(item[1]) + '</a>'
            pager = '<nav aria-label="Previous and next guides">' + adjacent(previous, "Previous") + adjacent(following, "Next") + '</nav>'
            page = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + escape(title) + ' — Geeklog documentation</title><link rel="stylesheet" href="' + root_relative + 'style.css"></head><body><header>' + breadcrumb + site_nav + '</header><main>' + toc + body + related_guides(slug, online=True) + pager + '</main><footer>Geeklog documentation · Geeklog 2.2.2 reference</footer></body></html>'
            dest = directory / dest_slug / "index.html"
        else:
            dest_slug = slug + "/"
            page = wrap(title, body + related_guides(slug), 2)
            dest = directory / slug / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page, encoding="utf-8")
        plain = re.sub(r"(?s)<[^>]+>", " ", body)
        records.append({"title": title, "url": dest_slug if online else slug + "/index.html",
                        "text": re.sub(r"\\s+", " ", plain)[:30000]})
    (directory / "search-index.json").write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    if online:
        # The published site has one main homepage and search index, not an extra
        # /modern/ catalogue or duplicate guide index.
        return len(records)
    body = ('<h1>Geeklog documentation — additional guides</h1>'
            '<p>One maintained Markdown source, two outputs. These guides complement '
            'the original Geeklog 2.2.2 documentation, which retains detailed historical settings.</p>'
            '<label for="search">Search published pilot pages</label>'
            '<input id="search" type="search" placeholder="Search documentation">'
            '<div id="results" aria-live="polite"></div>'
            '<noscript><p>Search requires JavaScript; browse the links below.</p></noscript>'
            '<ul>' + ''.join('<li><a href="'+r["url"]+'">'+escape(r["title"])+'</a></li>'
                            for r in records) + '</ul>'
            '<script src="search.js" defer></script>')
    (directory/"index.html").write_text(wrap("Documentation",body,0),encoding="utf-8")
    (directory/"search.js").write_text(
        """(async()=>{const input=document.getElementById('search'),out=document.getElementById('results');
const data=await(await fetch('search-index.json')).json();
function update(){const q=input.value.trim().toLowerCase();out.replaceChildren();if(!q)return;
const matches=data.filter(d=>(d.title+' '+d.text).toLowerCase().includes(q));const h=document.createElement('p');
h.textContent=matches.length+' matching pages';out.append(h);
const ul=document.createElement('ul');for(const d of matches){const li=document.createElement('li'),a=document.createElement('a');
a.href=d.url;a.textContent=d.title;li.append(a);ul.append(li)}out.append(ul)}input.addEventListener('input',update)})();""",
        encoding="utf-8")
    return len(records)

def check_links(directory):
    root = directory.resolve()
    pages = list(directory.rglob("*.html"))
    for page in pages:
        parsed = Inspect()
        parsed.feed(page.read_text(encoding="utf-8"))
        for ref in parsed.links:
            parts = urlsplit(ref)
            if parts.scheme or parts.netloc:
                continue
            dest = (page.parent / unquote(parts.path)).resolve() if parts.path else page.resolve()
            if not dest.is_relative_to(root) or not dest.is_file():
                raise AssertionError(f"Broken link in {page}: {ref}")
            if parts.fragment and dest.suffix == ".html":
                target = Inspect()
                target.feed(dest.read_text(encoding="utf-8"))
                if unquote(parts.fragment) not in target.ids:
                    raise AssertionError(f"Missing anchor in {page}: {ref}")
    if len(pages) != len(SOURCES)+1:
        raise AssertionError("Wrong number of generated HTML pages")
    return len(pages)


def main():
    # Non-destructive to pre-existing release artifacts and original Core docs:
    # only this script's dedicated output roots are replaced.
    for directory in (ONLINE, EMBED):
        if directory.exists():
            shutil.rmtree(directory)
        count = write_site(directory)
        checked = check_links(directory)
        print(f"PASS {directory}: {count} guides, {checked} valid HTML pages")
    # Online and embedded page trees must be byte-for-byte equivalent.
    rels = [p.relative_to(ONLINE) for p in ONLINE.rglob("*") if p.is_file()]
    assert all((ONLINE/r).read_bytes() == (EMBED/r).read_bytes() for r in rels)
    print("PASS: single Markdown source; identical web and embedded pilot pages")


if __name__ == "__main__":
    main()
