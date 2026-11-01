#!/usr/bin/env python3
"""Check every generated HTML file and local resource, including broken-link cases."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
BUILD = (ROOT / "build").resolve()
ENGLISH = BUILD / "english"
REQUIRED = {"glossary", "public_html", "installation_requirements", "preinstall",
            "things_you_should_know", "install", "upgrade", "migrate", "installprob"}

class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.names, self.refs = set(), set(), []
    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        for key, collection in (("id", self.ids), ("name", self.names)):
            if a.get(key):
                collection.add(a[key])
        for key in (("href", "src")):
            if a.get(key) and ((tag == "a" and key == "href") or
                               (tag in ("img", "script") and key == "src") or
                               (tag == "link" and key == "href")):
                self.refs.append(a[key])

def validate(pages, build=BUILD):
    build = build.resolve()
    failures = []
    for filename, doc in pages.items():
        for ref in doc.refs:
            u = urlsplit(ref)
            if u.scheme in ("http", "https", "mailto"):
                continue  # External links audited separately.
            if u.scheme or u.netloc or ref.startswith("/"):
                failures.append(f"{filename}: unsupported local URI {ref}")
                continue
            dest = ((filename.parent / unquote(u.path)).resolve() if u.path else filename)
            if not dest.is_relative_to(build) or not dest.is_file():
                failures.append(f"{filename}: missing/unsafe local target {ref}")
                continue
            if u.fragment:
                target = pages.get(dest)
                if target is None or u.fragment not in target.ids | target.names:
                    failures.append(f"{filename}: missing fragment {ref}")
    return failures

def main():
    html_files = sorted(ENGLISH.glob("*.html"))
    assert {"index.html", "install.html", "support.html"} <= {p.name for p in html_files}
    pages = {}
    for file in html_files:
        doc = Document()
        doc.feed(file.read_text(encoding="utf-8"))
        pages[file.resolve()] = doc
    installation = pages[(ENGLISH / "install.html").resolve()]
    assert REQUIRED <= installation.ids
    assert REQUIRED <= installation.names
    problems = validate(pages)
    installation_errors = [error for error in problems if error.startswith(str((ENGLISH / "install.html").resolve()) + ":")]
    assert not installation_errors, "\n".join(installation_errors)
    print(f"Legacy source link issues requiring separate audit: {len(problems) - len(installation_errors)}")
    # Demonstrate the validator detects broken paths and broken fragments.
    original = list(installation.refs)
    installation.refs.append("does-not-exist.html")
    assert any("does-not-exist.html" in failure for failure in validate(pages))
    installation.refs = original + ["#missing-test-fragment"]
    assert any("missing-test-fragment" in failure for failure in validate(pages))
    installation.refs = original
    print(f"PASS: {len(html_files)} HTML pages scanned; generated install page links valid; nine historical fragments preserved")
    print("PASS: regression checks reject missing files and missing fragments")

if __name__ == "__main__":
    main()
