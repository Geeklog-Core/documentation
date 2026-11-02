#!/usr/bin/env python3
"""Regression checks for the limited Markdown -> HTML documentation pilot."""
from html.parser import HTMLParser
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urldefrag
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "build" / "english"
EXPECTED = {"config.html": {"desc_site_url", "desc_site_name"}}
PAGES = ("index.html", "install.html", "config.html")

class Inspect(HTMLParser):
    def __init__(self):
        super().__init__()
        self.anchors = []
        self.links = []
    def handle_starttag(self, tag, attrs):
        fields = dict(attrs)
        for attr in ("id", "name"):
            if fields.get(attr):
                self.anchors.append(fields[attr])
        if tag == "a" and fields.get("href"):
            self.links.append(fields["href"])

def main():
    subprocess.run([sys.executable, str(ROOT / "tools" / "build_docs.py")], check=True)
    parsed = {}
    for filename in PAGES:
        page = DEST / filename
        assert page.is_file(), f"Missing output: {page}"
        parsed[filename] = Inspect()
        parsed[filename].feed(page.read_text(encoding="utf-8"))
    manifest = json.loads((ROOT / "planning" / "legacy-config-anchors.json").read_text(encoding="utf-8"))
    counts = Counter(manifest["anchors"])
    assert manifest["anchor_count"] == sum(counts.values()) == 450
    assert sorted(manifest["duplicate_anchor_names"]) == sorted(k for k, v in counts.items() if v > 1)
    assert set(EXPECTED["config.html"]).issubset(counts)
    plugins = json.loads((ROOT / "planning" / "bundled-plugin-doc-links.json").read_text(encoding="utf-8"))
    expected_plugins = {"calendar", "links", "polls", "recaptcha", "spamx", "staticpages", "xmlsitemap"}
    plugin_rows = plugins["entries"]
    assert len(plugin_rows) == len(expected_plugins)
    assert {entry["plugin"] for entry in plugin_rows} == expected_plugins
    for entry in plugin_rows:
        assert entry["relative_path"].endswith(".html")
        if entry["plugin"] == "recaptcha":
            assert entry["relative_path"] == "admin/plugins/recaptcha/docs/english/config.html"
        else:
            assert entry["relative_path"] == f'docs/english/{entry["plugin"]}.html'
    print("Bundled plugin help-path inventory: 7 entries structurally validated (not runtime-tested)")
    plugin_anchors = json.loads((ROOT / "planning" / "plugin-anchors.json").read_text(encoding="utf-8"))
    assert {p["plugin"] for p in plugin_anchors["pages"]} == expected_plugins
    for p in plugin_anchors["pages"]:
        assert p["source_path"].endswith("/config.html") if p["plugin"] == "recaptcha" else p["source_path"].endswith("/" + p["plugin"] + ".html")
        assert set(p["config_anchors"]).issubset(set(p["named_anchors"]))
        assert all(a.startswith("desc_") for a in p["config_anchors"])
        assert len(p["named_anchors"]) > 0
    print("Plugin HTML anchor snapshot: 7 sources checked; migration coverage not yet tested")
    for filename, required in EXPECTED.items():
        missing = required - set(parsed[filename].anchors)
        assert not missing, f"Missing legacy anchors {filename}: {sorted(missing)}"
    for filename, p in parsed.items():
        for href in p.links:
            if href.startswith(("http:", "https:", "mailto:")):
                continue
            target, fragment = urldefrag(href)
            target = target or filename
            if "/" in target or target.startswith("."):
                continue  # other source references/paths require later audit
            assert target in parsed, f"Broken local page {filename}: {href}"
            if fragment:
                assert fragment in parsed[target].anchors, f"Broken fragment {filename}: {href}"
    missing_legacy = set(counts) - set(parsed["config.html"].anchors)
    print("Pilot page links and two sample legacy configuration anchors: OK")
    print(f"Full source snapshot: {manifest['anchor_count']} occurrences, {len(counts)} unique; "
          f"{len(missing_legacy)} unique legacy anchors not yet migrated (expected for pilot)")

if __name__ == "__main__":
    main()
