#!/usr/bin/env python3
"""Build a small offline HTML preview from curated Markdown sources.

Not a replacement for the complete bundled Geeklog documentation.
Run: python -m pip install -r requirements-docs.txt
     python tools/build_docs.py
"""
from pathlib import Path
from html import escape
import re
import markdown

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "docs"
OUTPUT = ROOT / "build" / "english"
PAGES = {"index.md": "index.html", "install.md": "install.html", "config.md": "config.html"}

def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for source, output in PAGES.items():
        text = (SOURCES / source).read_text(encoding="utf-8")
        for old, new in PAGES.items():
            text = text.replace(f"]({old})", f"]({new})")
        body = markdown.markdown(text, extensions=["tables", "fenced_code", "toc"])
        # Markdown permits embedded HTML: only trusted, reviewed repository content
        # should be passed to this build. No live user-supplied Markdown is accepted.
        title = re.search(r"^# (.+)$", text, flags=re.M)
        name = title.group(1) if title else "Geeklog Documentation"
        html = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
                f'<title>{escape(name)}</title></head><body>\n'
                '<nav><a href="index.html">Geeklog Documentation</a></nav>\n'
                f'{body}\n</body></html>\n')
        (OUTPUT / output).write_text(html, encoding="utf-8")
    print(f"Generated {len(PAGES)} pilot pages in {OUTPUT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
