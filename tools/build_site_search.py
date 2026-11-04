#!/usr/bin/env python3
"""Add unified client-side search to the existing online Geeklog preview.

Only the online HTML folder is modified. The embedded legacy documentation and
its compatibility anchors are deliberately untouched.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "dist/online"
SOURCES = {
    "installation.html": "Installation and upgrades",
    "configuration.html": "Configuration",
    "administration.html": "Administration",
    "modern/development/plugin-api/index.html": "Plugin API",
    "modern/development/templates/index.html": "Themes and templates",
    "modern/plugins/static-pages/index.html": "Static Pages",
    "modern/development/webservices/index.html": "Webservices API",
    "modern/development/configuration-api/index.html": "Configuration API",
    "modern/administration/users-and-groups/index.html": "Users and groups",
    "modern/development/security-and-permissions/index.html": "Security and permissions",
    "modern/administration/backup-and-recovery/index.html": "Backup and recovery",
    "modern/administration/maintenance/index.html": "Maintenance and upgrades",
    "modern/administration/troubleshooting/index.html": "Troubleshooting",
}

SEARCH_JS = r"""(() => {
  'use strict';
  const field = document.getElementById('docs-search');
  const output = document.getElementById('docs-results');
  if (!field || !output) return;
  let records = [];
  const status = document.createElement('p');
  status.setAttribute('role', 'status');
  const list = document.createElement('ul');
  output.append(status, list);

  fetch('search-index.json')
    .then(response => {
      if (!response.ok) throw new Error('Search index unavailable');
      return response.json();
    })
    .then(data => {
      records = data;
      update();
    })
    .catch(() => {
      status.textContent = 'Search is unavailable; browse the links below.';
    });

  function update() {
    list.replaceChildren();
    const terms = field.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    if (!terms.length) {
      status.textContent = '';
      return;
    }
    const matches = records.filter(item => {
      const haystack = (item.title + ' ' + item.text).toLocaleLowerCase();
      return terms.every(term => haystack.includes(term));
    });
    status.textContent = matches.length + ' matching pages';
    for (const item of matches) {
      const li = document.createElement('li');
      const a = document.createElement('a');
      a.href = item.url;
      a.textContent = item.title;
      li.append(a);
      list.append(li);
    }
  }
  field.addEventListener('input', update);
})();"""


class ExtractText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.content = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if self.skip:
            self.skip += 1
        elif tag in ("script", "style", "nav", "footer"):
            self.skip = 1

    def handle_endtag(self, tag):
        if self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.content.append(data)


def main():
    if not (SITE / "index.html").is_file():
        raise SystemExit("Run build_dual_preview.py before creating search index")
    entries = []
    for relative, title in SOURCES.items():
        page = SITE / relative
        if not page.is_file():
            raise FileNotFoundError(page)
        parser = ExtractText()
        parser.feed(page.read_text(encoding="utf-8"))
        entries.append({
            "url": quote(relative, safe="/"),
            "title": title,
            "text": re.sub(r"\s+", " ", " ".join(parser.content)).strip()[:50000],
        })
    assert len(entries) == len(SOURCES) == 13
    (SITE / "search-index.json").write_text(
        json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (SITE / "search.js").write_text(SEARCH_JS + "\n", encoding="utf-8")
    index = SITE / "index.html"
    html = index.read_text(encoding="utf-8")
    tag = "</main>"
    if html.count(tag) != 1:
        raise AssertionError("Cannot safely add search to site homepage")
    search_markup = (
        '<section aria-label="Search all documentation">'
        '<h2>Search documentation</h2>'
        '<label for="docs-search">Find a topic across all available guides</label>'
        '<input type="search" id="docs-search" autocomplete="off" '
        'placeholder="Search all documentation">'
        '<div id="docs-results" aria-live="polite"></div>'
        '<noscript>Search requires JavaScript. Use the topic links instead.</noscript>'
        '</section>'
        '<script defer src="search.js"></script>'
    )
    html = html.replace(tag, search_markup + tag)
    index.write_text(html, encoding="utf-8")
    assert all((SITE / item["url"]).is_file() for item in entries)
    assert html.count('id="docs-search"') == 1
    assert (SITE / "search.js").is_file()
    print(f"PASS: unified homepage search indexes {len(entries)} current Markdown guides")


if __name__ == "__main__":
    main()
