#!/usr/bin/env python3
"""HTTP smoke test for generated documentation, without deploying publicly.

Serve the built online site and the unpacked embedded docs from a disposable
local HTTP server; inspect reachable endpoints, content types and assets.
This does not execute Geeklog PHP or validate administration permissions.
"""
from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from urllib.request import urlopen
import json
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "dist/online"
ZIP = ROOT / "dist/geeklog-2.2.2-docs-preview.zip"

class SilentHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass

@contextmanager
def serve(directory):
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(SilentHandler, directory=str(directory)))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield "http://127.0.0.1:" + str(server.server_port)
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)

def fetch(base, path, content_type):
    with urlopen(base + "/" + path, timeout=5) as response:
        assert response.status == 200, (path, response.status)
        mime = response.headers.get_content_type()
        assert mime == content_type, f"Unexpected MIME for {path}: {mime}"
        data = response.read()
        assert data, f"Empty HTTP resource: {path}"
        return data

def online():
    with serve(SITE) as base:
        index = fetch(base, "index.html", "text/html")
        assert b"docs-search" in index and b"Browse all guides" in index
        docs = json.loads(fetch(base, "search-index.json", "application/json"))
        assert len(docs) == 25
        # Browse remains available without JS, organized by task rather than a flat list.
        assert index.count(b'class="docs-topic-group"') == 6
        assert index.count(b'<h3>') == 6
        assert b'Getting Started' in index and b'User Guide' in index and b'Administration' in index
        assert b'Plugins' in index and b'Development &amp; Theming' in index and b'Reference &amp; Archive' in index
        for item in docs:
            assert index.count(('href="' + item["url"] + '"').encode("utf-8")) == 1

        assert b"fetch('search-index.json')" in fetch(base, "search.js", "text/javascript")
        css = fetch(base, "style.css", "text/css").decode("utf-8")
        # The label and input must not run together on desktop or mobile.
        assert "label[for=docs-search]{display:block;margin-bottom:.6rem}" in css
        assert "#docs-search{display:block;width:100%;max-width:32rem;" in css
        assert "#docs-search:focus-visible" in css
        assert ".docs-topic-grid{display:grid;" in css
        assert "grid-template-columns:repeat(auto-fit" in css
        assert b'<label for="docs-search">Find a topic across all available guides</label>' in index
        assert b'<input type="search" id="docs-search"' in index
        for item in docs:
            html = fetch(base, item["url"], "text/html")
            assert b"<html" in html
        fetch(base, "modern/index.html", "text/html")
        fetch(base, "configuration.html", "text/html")
        return len(docs)

def embedded():
    with tempfile.TemporaryDirectory(prefix="geeklog-docs-http-") as temp:
        stage = Path(temp)
        with zipfile.ZipFile(ZIP) as z:
            names = z.namelist()
            for name in names:
                target = stage / name
                assert target.resolve().is_relative_to(stage.resolve())
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(z.read(name))
        with serve(stage / "public_html") as base:
            install = fetch(base, "docs/english/install.html", "text/html")
            assert b"installation_requirements" in install
            config = fetch(base, "docs/english/config.html", "text/html")
            assert b"desc_site_url" in config
            fetch(base, "docs/docstyle.css", "text/css")
            fetch(base, "docs/images/logo.gif", "image/gif")
            modern = fetch(base, "docs/english/modern/index.html", "text/html")
            assert b"Geeklog" in modern
            search = json.loads(fetch(base, "docs/english/modern/search-index.json", "application/json"))
            assert len(search) == 22
            fetch(base, "docs/english/modern/style.css", "text/css")
            fetch(base, "docs/english/modern/search.js", "text/javascript")
            for item in search:
                fetch(base, "docs/english/modern/" + item["url"], "text/html")
            for slug in ("calendar", "links", "polls", "spamx", "staticpages", "xmlsitemap"):
                fetch(base, "docs/english/" + slug + ".html", "text/html")
            fetch(base, "admin/plugins/recaptcha/docs/english/config.html", "text/html")
            return len(search)

def main():
    assert SITE.is_dir() and ZIP.is_file(), "Run documentation builders first"
    indexed = online()
    offline = embedded()
    print(f"PASS: HTTP 200 and MIME for online index, CSS, JS, {indexed} guides")
    print(f"PASS: HTTP 200 and MIME for embedded help, six Core plugin pages, reCAPTCHA and {offline} modern guides")
    print("NOTE: local static HTTP test only; no Geeklog application or browser UI was exercised")

if __name__ == "__main__":
    main()
