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
import markdown

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ONLINE = ROOT / "dist/modern-online"
EMBED = ROOT / "dist/modern-embedded/public_html/docs/english/modern"
SOURCES = [
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
# Each guide offers two actionable follow-up paths without leaving the current
# generated documentation tree. These references work in both website and ZIP.
RELATED = {
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

def related_guides(slug):
    titles = dict(SOURCES)
    assert set(RELATED) == set(titles), "Related navigation must cover every modern guide"
    targets = RELATED[slug]
    assert len(targets) == len(set(targets)) == 2 and slug not in targets
    assert all(target in titles for target in targets), f"Unknown related guide: {slug}"
    links = ''.join(
        '<li><a href="../../' + target + '/index.html">' +
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


def write_site(directory):
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "style.css").write_text(CSS, encoding="utf-8")
    records = []
    for slug, title in SOURCES:
        source = DOCS / slug / "README.md"
        if not source.is_file():
            raise FileNotFoundError(source)
        md = source.read_text(encoding="utf-8")
        body = markdown.markdown(md, extensions=["tables", "fenced_code", "toc"])
        target = directory / slug / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(wrap(title, body + related_guides(slug), 2), encoding="utf-8")
        plain = re.sub(r"(?s)<[^>]+>", " ", body)
        records.append({"title":title,"url":slug+"/index.html",
                        "text":re.sub(r"\s+"," ",plain)[:30000]})
    (directory/"search-index.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
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
