#!/usr/bin/env python3
"""Render a non-deployable embedded configuration candidate from maintained Markdown.

This creates a separate review artifact. It must NEVER overwrite the embedded
Geeklog 2.2.2 config.html, which stays byte-identical to the tagged release.
Run after the dual documentation build, with GEEKLOG_CORE_DOCS set.
"""
from html.parser import HTMLParser
from html import unescape
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import os
import re
import zipfile

import markdown

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/configuration/README.md"
LEGACY = Path(os.environ["GEEKLOG_CORE_DOCS"]) / "english/config.html"
ORIGINAL_TREE = ROOT / "dist/geeklog-2.2.2/public_html"
OUTPUT = ROOT / "dist/config-candidate/public_html/docs/english/config.html"
REPORT = ROOT / "dist/config-candidate-report.json"
ARCHIVE = ROOT / "dist/config-candidate-review.zip"


class Inspect(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.anchors = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.anchors.extend(dict.fromkeys([a["id"]] if a.get("id") else []))
        if tag == "a" and a.get("name") and a["name"] != a.get("id"):
            self.anchors.append(a["name"])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "link" and a.get("href"):
            self.links.append(a["href"])


def parsed(html):
    obj = Inspect()
    obj.feed(html)
    return obj


def main():
    assert LEGACY.is_file() and SOURCE.is_file()
    original = parsed(LEGACY.read_text(encoding="utf-8"))
    md = SOURCE.read_text(encoding="utf-8")
    body = markdown.markdown(md, extensions=["tables", "fenced_code"])
    # Old relative stylesheet layout must remain resolvable at docs/english.
    candidate = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Geeklog 2.2.2 configuration reference</title>'
        '<link rel="stylesheet" href="../docstyle.css"></head>'
        '<body><main>' + body + '</main></body></html>'
    )
    # The two historical routing tables are now maintained in Markdown.
    # Compare all individual legacy rows with the candidate, not just counts.
    routing_tables = {}
    for anchor, columns in (("url-rewrite", 2), ("url-routing", 3)):
        old_location = LEGACY.read_text(encoding="utf-8").index(
            'name="' + anchor + '"')
        candidate_location = candidate.index('id="' + anchor + '"')
        legacy_table = re.search(
            r"<table\b[^>]*>[\s\S]*?</table>",
            LEGACY.read_text(encoding="utf-8")[old_location:], re.I)
        new_table = re.search(
            r"<table\b[^>]*>[\s\S]*?</table>",
            candidate[candidate_location:], re.I)
        assert legacy_table and new_table, (
            f"Missing legacy or migrated routing table: {anchor}")
        def read_rows(markup):
            result = []
            for row in re.findall(
                r"<tr\b[^>]*>([\s\S]*?)</tr>", markup, re.I
            ):
                cells = [
                    re.sub(r"\s+", " ", unescape(
                        re.sub(r"<[^>]+>", "", text))).strip()
                    for text in re.findall(
                        r"<td\b[^>]*>([\s\S]*?)</td>", row, re.I)
                ]
                if cells:
                    result.append(cells)
            return result
        expected = read_rows(legacy_table.group(0))
        actual = read_rows(new_table.group(0))
        assert len(expected) == 10 and all(len(row) == columns for row in expected)
        assert actual == expected, (
            f"Routing URL / priority mismatch in {anchor}")
        routing_tables[anchor] = len(actual)

    # Keep the complete historical date directive inventory in Markdown.
    locale_start = LEGACY.read_text(encoding="utf-8").index(
        "<h3>Date Format Syntax</h3>")
    legacy_list = re.search(
        r"<ul[^>]*>([\s\S]*?)</ul>",
        LEGACY.read_text(encoding="utf-8")[locale_start:], re.I)
    assert legacy_list, "Missing original date format list"
    original_directives = [
        re.search(r"%[a-zA-Z%]", item).group(0)
        for item in re.findall(
            r"<li[^>]*>([\s\S]*?)</li>", legacy_list.group(1), re.I)
    ]
    candidate_date = candidate.index('id="date_formats"')
    candidate_next = candidate.index('id="url-cron"', candidate_date)
    date_section = candidate[candidate_date:candidate_next]
    migrated_directives = re.findall(
        r"<td><code>(%[a-zA-Z%])</code></td>", date_section)
    assert len(original_directives) == 33, "Unexpected legacy directive count"
    assert migrated_directives == original_directives, (
        "Date format token lost or reordered in Markdown candidate")

    # Regression gates for the restored historical cron appendix.
    cron_start = candidate.index('id="url-cron"')
    cron_markup = candidate[cron_start:]
    for expected in (
        "cron-emailgeeklogdailydigest",
        "cron-emailgeeklogdatabasebackup",
        "db_backup_sendto",
        "lastemailedstories",
        "lib-common.php",
        "COM_emailUserTopics",
    ):
        assert expected in cron_markup, f"Cron appendix detail missing: {expected}"
    assert "30 2 * * * /path/to/geeklog/cron-emailgeeklogdailydigest" in cron_markup, (
        "Original daily digest cron schedule absent")
    assert "<pre>" in cron_markup and "</pre>" in cron_markup, (
        "Cron schedule example is not rendered as preformatted code")

    current = parsed(candidate)
    historical = set(original.anchors)
    generated = set(current.anchors)
    missing = sorted(historical - generated)
    extra = sorted(generated - historical)
    assert not missing, f"Missing historical anchors: {missing[:10]}"
    assert not extra, f"Unexpected historical anchors: {extra[:10]}"
    assert len(historical) == 449
    assert len(current.anchors) == len(generated), "Duplicated generated anchors"
    assert body.count("Documented default (Geeklog 2.2.2)") == 387, (
        "Not all 387 historical defaults are present in the candidate"
    )

    # Work out link destinations as if config.html were installed in the
    # existing validated 2.2.2 archive. Do not mutate that archive.
    linked = 0
    for link in current.links:
        target = urlsplit(link)
        if target.scheme or target.netloc or link.startswith("//"):
            continue
        source_relative = Path("docs/english/config.html")
        next_path = (source_relative.parent / unquote(target.path)) if target.path else source_relative
        import posixpath
        normalized = posixpath.normpath(next_path.as_posix())
        assert not normalized.startswith("../"), f"Path escapes site: {link}"
        if normalized == "docs/english/config.html":
            match = current
        else:
            located = ORIGINAL_TREE / normalized
            assert located.is_file(), f"Missing local document or asset: {link}"
            match = parsed(located.read_text(encoding="utf-8")) if located.suffix == ".html" else None
        if target.fragment and match is not None:
            assert unquote(target.fragment) in match.anchors, f"Missing fragment: {link}"
        linked += 1

    assert (ORIGINAL_TREE / "docs/docstyle.css").is_file()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(candidate + "\n", encoding="utf-8")
    # One file only: recipient may preview/inspect it, never auto-deploy it.
    with zipfile.ZipFile(ARCHIVE, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(OUTPUT, "public_html/docs/english/config.html")
    legacy_html = LEGACY.read_text(encoding="utf-8")
    historical_links = {
        url for url in original.links
        if not urlsplit(url).scheme and not urlsplit(url).netloc
        and not url.startswith("//")
    }
    candidate_links = {
        url for url in current.links
        if not urlsplit(url).scheme and not urlsplit(url).netloc
        and not url.startswith("//")
    }
    # This is an outstanding migration inventory, not a signoff: the old
    # reference may intentionally have obsolete links that need rewriting.
    link_gaps = sorted(historical_links - candidate_links)
    structure = {
        "legacy_html_tables": len(re.findall(r"<table", legacy_html, re.I)),
        "candidate_html_tables": len(re.findall(r"<table", candidate, re.I)),
        "legacy_preformatted_blocks": len(re.findall(r"<pre", legacy_html, re.I)),
        "candidate_preformatted_blocks": len(re.findall(r"<pre", candidate, re.I)),
        "original_local_link_count": len(historical_links),
        "candidate_local_link_count": len(candidate_links),
        "historical_link_targets_not_yet_represented": link_gaps,
    }
    report = {
        "scope": "Geeklog 2.2.2 candidate for review ONLY; not deployed",
        "candidate_html": str(OUTPUT.relative_to(ROOT)),
        "historical_unique_anchors": len(historical),
        "generated_unique_anchors": len(generated),
        "historical_defaults_transcribed": 387,
        "candidate_local_links_checked": linked,
        "legacy_embedded_configuration_replaced": False,
        "content_parity": "INCOMPLETE — original tables, examples and links remain under review",
        "validated_routing_tables": routing_tables,
        "validated_date_format_directives": len(migrated_directives),
        "validated_cron_appendix": True,
        "comparison": structure,
        "outstanding": [
            "Full semantic/text/table/example parity with tagged original",
            "Editorial provenance and contributor license review",
            "Real context-sensitive admin help tests against this candidate",
            "Maintainer approval before any official replacement",
        ],
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("PASS: candidate generated from Markdown, 449 historical anchors, 387 defaults")
    print("PASS: all 20 legacy URL rewriting/routing data rows match the candidate")
    print("PASS: all 33 date format directives preserved in source order")
    print(f"PASS: {linked} candidate local links, referenced assets and fragments checked")
    print("NOTE: candidate is an isolated review artifact, NOT a production replacement")


if __name__ == "__main__":
    main()
