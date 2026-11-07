#!/usr/bin/env python3
"""Add unified client-side search to the published Geeklog site.

Only the online HTML folder is modified. The embedded legacy documentation and
its compatibility anchors are deliberately untouched.
"""
from html.parser import HTMLParser
from html import escape
from pathlib import Path
from urllib.parse import quote
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "dist/online"
SOURCES = {
    "installation/": "Installation and upgrades",
    "configuration/": "Configuration",
    "administration/": "Administration",
    "user-guide/": "Using Geeklog: User Guide",
    "user-guide/articles-and-topics/": "Articles, Topics and Publishing",
    "user-guide/blocks-and-navigation/": "Blocks, Menus and Navigation",
    "user-guide/comments-and-moderation/": "Comments and Moderation",
    "plugins/plugin-installation-management/": "Plugin Installation and Management",
    "development/plugin-development/": "Plugin Development: Step by Step",
    "development/theme-development/": "Theme Development: Step by Step",
    "user-guide/syndication-rss-autotags/": "Syndication, RSS and Autotags",
    "plugins/bundled-plugins/": "Bundled Plugins Reference",
    "reference/database-schema/": "Database Schema and Data Model",
    "development/contributing/": "Contributing to Geeklog",
    "reference/plugin-api/": "Plugin API",
    "development/templates/": "Themes and templates",
    "plugins/static-pages/": "Static Pages",
    "reference/webservices/": "Webservices API",
    "reference/configuration-api/": "Configuration API",
    "administration/users-and-groups/": "Users and groups",
    "development/security-and-permissions/": "Security and permissions",
    "administration/backup-and-recovery/": "Backup and recovery",
    "administration/maintenance/": "Maintenance and upgrades",
    "administration/troubleshooting/": "Troubleshooting",
}

# Every searchable guide appears exactly once in one task-oriented homepage group.
# These labels organize the catalogue only; they do not alter search targets.
TOPIC_GROUPS = (
    ("Getting Started", "Install Geeklog, upgrade safely and understand configuration.", (
        "installation/",
        "configuration/",
    )),
    ("User Guide", "Learn how to publish, organize content and use site features.", (
        "user-guide/",
        "user-guide/articles-and-topics/",
        "user-guide/blocks-and-navigation/",
        "user-guide/comments-and-moderation/",
        "user-guide/syndication-rss-autotags/",
    )),
    ("Administration", "Manage accounts, site operations, recovery and support.", (
        "administration/",
        "administration/users-and-groups/",
        "administration/backup-and-recovery/",
        "administration/maintenance/",
        "administration/troubleshooting/",
    )),
    ("Plugins", "Install, manage and document bundled extensions.", (
        "plugins/plugin-installation-management/",
        "plugins/bundled-plugins/",
        "plugins/static-pages/",
    )),
    ("Development & Theming", "Build plugins, create themes and contribute safely.", (
        "development/plugin-development/",
        "development/security-and-permissions/",
        "development/templates/",
        "development/theme-development/",
        "development/contributing/",
    )),
    ("Technical Reference", "Consult version-scoped technical APIs and data model.", (
        "reference/database-schema/",
        "reference/plugin-api/",
        "reference/configuration-api/",
        "reference/webservices/",
    )),
)

def grouped_catalogue(entries):
    by_url = {entry["url"]: entry for entry in entries}
    assert len(by_url) == len(entries), "Duplicate guide URLs"
    used = []
    sections = []
    for title, description, paths in TOPIC_GROUPS:
        assert paths, f"Empty topic category: {title}"
        items = []
        for url in paths:
            assert url in by_url, f"Unknown grouped guide: {url}"
            used.append(url)
            item = by_url[url]
            items.append('<li><a href="' + item["url"] + '">' +
                         escape(item["title"]) + '</a></li>')
        sections.append(
            '<section class="docs-topic-group"><h3>' + escape(title) + '</h3>'
            '<p>' + escape(description) + '</p><ul>' +
            ''.join(items) + '</ul></section>'
        )
    assert len(used) == len(set(used)) == len(entries), (
        "A guide is missing or repeated across homepage categories"
    )
    assert set(used) == set(by_url), "Homepage categories do not cover search index"
    return '<div class="docs-topic-grid">' + ''.join(sections) + '</div>'


SEARCH_JS = r"""(() => {
  'use strict';
  const field = document.getElementById('docs-search');
  const output = document.getElementById('docs-results');
  const catalogue = document.getElementById('docs-catalogue');
  if (!field || !output || !catalogue) return;
  let records = [];
  let indexReady = false;
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
      if (!Array.isArray(data)) throw new Error('Invalid search index');
      records = data;
      indexReady = true;
      update();
    })
    .catch(() => {
      indexReady = false;
      catalogue.hidden = false;
      output.hidden = false;
      list.replaceChildren();
      status.textContent = 'Search is unavailable; browse the links below.';
    });

  function update() {
    list.replaceChildren();
    if (!indexReady) {
      catalogue.hidden = false;
      output.hidden = true;
      return;
    }
    catalogue.hidden = field.value.trim().length > 0;
    output.hidden = !catalogue.hidden;
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
        page = SITE / relative / "index.html"
        if not page.is_file():
            raise FileNotFoundError(page)
        parser = ExtractText()
        parser.feed(page.read_text(encoding="utf-8"))
        entries.append({
            "url": quote(relative, safe="/"),
            "title": title,
            "text": re.sub(r"\s+", " ", " ".join(parser.content)).strip()[:50000],
        })
    assert len(entries) == len(SOURCES) == 24
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
        '<div id="docs-results" aria-live="polite" hidden></div>'
        '<noscript>Search requires JavaScript. Use the topic links instead.</noscript>'
        '</section>'
        '<script defer src="search.js"></script>'
    )
    browse_markup = (
        '<section id="docs-catalogue" aria-label="Browse all guides">'
        '<h2>Browse the documentation</h2>'
        '<p>Guides for Geeklog 2.2.2, with additional administration and development references. '
        'The original embedded configuration help remains authoritative for '
        'historical defaults and detailed examples.</p>'
        + grouped_catalogue(entries) + '</section>'
    )
    # A simple, task-oriented journey for visitors new to Geeklog.
    journey = ('<section aria-label="Start here: beginner learning path">'
        '<h2>Start here — five practical steps</h2><ol>'
        '<li><a href="installation/">Install Geeklog</a></li>'
        '<li><a href="configuration/">Configure the site</a></li>'
        '<li><a href="user-guide/articles-and-topics/">Create your first article</a></li>'
        '<li><a href="administration/users-and-groups/">Manage users and groups</a></li>'
        '<li><a href="administration/backup-and-recovery/">Back up the site</a></li>'
        '</ol><p>Use a disposable staging site for changes and follow each guide\'s rights requirements.</p></section>')
    html = html.replace(tag, journey + search_markup + browse_markup + tag)
    index.write_text(html, encoding="utf-8")
    assert all((SITE / item["url"] / "index.html").is_file() for item in entries)
    assert html.count('aria-label="Browse all guides"') == 1
    assert all('href="' + item["url"] + '"' in html for item in entries)
    assert html.count('id="docs-search"') == 1
    assert (SITE / "search.js").is_file()
    print(f"PASS: unified homepage search indexes {len(entries)} current Markdown guides")


if __name__ == "__main__":
    main()
