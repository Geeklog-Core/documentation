#!/usr/bin/env python3
"""Build Geeklog documentation website and a 2.2.2-layout offline ZIP.

Requires tools/check_install_anchors.py to have built build/ using a pinned
Geeklog Core documentation tree (GEEKLOG_CORE_DOCS).
"""
from html import escape
from pathlib import Path
from urllib.parse import urlsplit, unquote
from html.parser import HTMLParser
import os
import shutil
import zipfile
import markdown

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
DIST = ROOT / "dist/geeklog-2.2.2/public_html/docs"
WEB = ROOT / "dist/online"
PAGES = {
    "index.html": ("Geeklog documentation", None),
    "installation.html": ("Installation", ROOT / "docs/installation/README.md"),
    "configuration.html": ("Configuration", ROOT / "docs/configuration/README.md"),
    "administration.html": ("Administration", ROOT / "docs/administration/README.md"),
}
NAV = ' · '.join(f'<a href="{name}">{escape(title)}</a>' for name, (title, _) in PAGES.items())
CSS = """*{box-sizing:border-box}body{font:17px/1.6 system-ui,sans-serif;max-width:960px;margin:auto;padding:20px;color:#24292f}nav{padding:1rem 0;border-bottom:1px solid #ddd}main{padding-top:1rem}a{color:#1766a2}pre{overflow:auto;background:#f4f4f4;padding:1rem}blockquote{border-left:4px solid #bd8700;padding:.1rem 1rem;background:#fff8e8}img{max-width:100%}label[for=docs-search]{display:block;margin-bottom:.6rem}#docs-search{display:block;width:100%;max-width:32rem;min-height:2.75rem;padding:.6rem .75rem;border:1px solid #8c959f;border-radius:6px;font:inherit}#docs-search:focus-visible{outline:2px solid #1766a2;outline-offset:2px}.docs-topic-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,19rem),1fr));gap:1rem;margin:1.25rem 0}.docs-topic-group{border:1px solid #d0d7de;border-radius:8px;padding:1rem 1.25rem;min-width:0}.docs-topic-group h3{margin:0 0 .25rem;font-size:1.1rem}.docs-topic-group p{margin:.25rem 0 .75rem;color:#57606a;font-size:.94rem}.docs-topic-group ul{margin:.5rem 0 0;padding-left:1.25rem}.docs-topic-group li{margin:.35rem 0}@media(max-width:600px){body{padding:12px}nav a{display:inline-block;margin:.3rem}}"""
class Inspect(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=set()
        self.refs=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        self.ids.update(x for x in (a.get("id"),a.get("name")) if x)
        if tag=="a" and a.get("href"): self.refs.append(a["href"])
        if tag=="link" and a.get("href"): self.refs.append(a["href"])

def main():
    core = os.environ.get("GEEKLOG_CORE_DOCS")
    if not core:
        raise SystemExit("GEEKLOG_CORE_DOCS required: do not package placeholder legacy docs")
    source=Path(core)
    if not (source/"english/config.html").is_file():
        raise SystemExit("Pinned source missing english/config.html")
    if not (BUILD/"english/install.html").is_file():
        raise SystemExit("Run tools/check_install_anchors.py first")
    if DIST.parent.exists(): shutil.rmtree(DIST.parent)
    if WEB.exists(): shutil.rmtree(WEB)
    shutil.copytree(BUILD, DIST, ignore=shutil.ignore_patterns("legacy-link-audit.json"))
    assert (DIST/"english/index.html").is_file()
    assert (DIST/"english/config.html").read_bytes()==(source/"english/config.html").read_bytes()
    assert (DIST/"english/install.html").read_bytes()!=(source/"english/install.html").read_bytes()
    plugin_source=Path(os.environ["GEEKLOG_RELEASE_RECAPTCHA_DOCS"])
    assert (plugin_source/"english/config.html").is_file(), "Missing tagged reCAPTCHA docs"
    plugin_dest=ROOT/"dist/geeklog-2.2.2/public_html/admin/plugins/recaptcha/docs"
    shutil.copytree(plugin_source,plugin_dest)
    WEB.mkdir(parents=True)
    (WEB/"style.css").write_text(CSS,encoding="utf-8")
    for file,(title,md) in PAGES.items():
        if md:
            body=markdown.markdown(md.read_text(encoding="utf-8"),extensions=["tables","fenced_code","toc"])
        else:
            body='<h1>Geeklog documentation</h1><p>Guides for Geeklog 2.2.2. Search the documentation or browse the topics below.</p>'
        page=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)}</title><link rel="stylesheet" href="style.css"></head><body><nav>{NAV if file != "index.html" else '<a href="index.html">Geeklog documentation</a>'}</nav><main>{body}</main><footer><hr>Geeklog documentation · Geeklog 2.2.2 reference edition</footer></body></html>'
        (WEB/file).write_text(page,encoding="utf-8")
    # Render the unified modern Markdown pilot into both outputs. Core 2.2.2
    # historical help paths remain unchanged; modern help is additive.
    from build_modern_pilot import write_site, check_links
    modern_web = WEB / "modern"
    modern_embed = DIST / "english" / "modern"
    for target in (modern_web, modern_embed):
        assert write_site(target) == 22
        assert check_links(target) == 23
    for p in modern_web.rglob("*"):
        if p.is_file():
            assert p.read_bytes() == (modern_embed / p.relative_to(modern_web)).read_bytes()
    # Add the newly generated section to the existing site homepage.
    index_file = WEB / "index.html"
    index_html = index_file.read_text(encoding="utf-8")
    index_file.write_text(index_html, encoding="utf-8")
    for file in PAGES:
        p=WEB/file
        d=Inspect();d.feed(p.read_text(encoding="utf-8"))
        for ref in d.refs:
            u=urlsplit(ref)
            if u.scheme or u.netloc: continue
            dest=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
            assert dest.is_relative_to(WEB.resolve()) and dest.is_file(),f"Broken web reference: {file}: {ref}"
            if u.fragment:
                t=Inspect();t.feed(dest.read_text(encoding="utf-8"))
                assert u.fragment in t.ids,f"Broken web fragment: {file}: {ref}"
    assert '<a id="desc_site_url" name="desc_site_url"></a>' in (WEB/"configuration.html").read_text(encoding="utf-8")
    required=["index.html","install.html","config.html"]
    for name in required: assert (DIST/"english"/name).is_file()
    archive=ROOT/"dist/geeklog-2.2.2-docs-preview.zip"
    with zipfile.ZipFile(archive,"w",compression=zipfile.ZIP_DEFLATED) as z:
        for p in sorted((ROOT/"dist/geeklog-2.2.2/public_html").rglob("*")):
            if p.is_file(): z.write(p, p.relative_to(ROOT/"dist/geeklog-2.2.2"))
    with zipfile.ZipFile(archive) as z:
        names=set(z.namelist())
        for name in required: assert "public_html/docs/english/"+name in names
        assert "public_html/admin/plugins/recaptcha/docs/english/config.html" in names
        assert len(names)==sum(p.is_file() for p in (ROOT/"dist/geeklog-2.2.2/public_html").rglob("*"))
    online_html = list(WEB.rglob("*.html"))
    modern_html = list(modern_web.rglob("*.html"))
    assert len(online_html) == len(PAGES) + len(modern_html)
    assert len(modern_html) == 23, "Expected modern index and twenty-two guides"
    assert (WEB / "modern/search-index.json").is_file()
    assert (WEB / "modern/search.js").is_file()
    for page in modern_html:
        relative = page.relative_to(modern_web)
        embedded_path = DIST / "english/modern" / relative
        assert embedded_path.is_file(), f"Missing embedded modern page: {relative}"
    print(f"PASS: {len(online_html)} total online HTML pages, including "
          f"{len(modern_html)} modern pages, and {len(names)} embedded files; "
          f"ZIP {archive.name}")
if __name__=="__main__": main()
