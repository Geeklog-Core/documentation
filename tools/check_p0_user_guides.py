#!/usr/bin/env python3
"""Regression checks for phase-two P0 Geeklog documentation.

Only source and rendered HTML structure is checked. The test does not certify
administration workflows, PHP permissions or UI behavior in a running Geeklog.
"""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
ONLINE = ROOT / "dist/online"
CASES = {
    "user-guide/overview": ("user-guide/README.md", ("## Everyday tasks and source-backed administration paths", "## Practical learning path"), ("submit.php", "admin/article.php", "admin/topic.php", "admin/block.php", "admin/moderation.php", "admin/plugins.php")),
    "user-guide/articles-and-topics": ("user-guide/articles-and-topics/README.md", ("## Choose the correct workflow in Geeklog 2.2.2", "## Article scheduling and topic hierarchy: fields to verify", "## Check publishing and permissions"), ("story.edit", "topic.edit", "story.moderate", "listdraftstories")),
    "user-guide/blocks-and-navigation": ("user-guide/blocks-and-navigation/README.md", ("## Configure a block using the Core administrator", "## Block types in Geeklog 2.2.2"), ("block.edit", "block.delete", "normal", "portal", "phpblock", "gldefault")),
    "user-guide/comments-and-moderation": ("user-guide/comments-and-moderation/README.md", ("## Understand the moderation queues in Geeklog 2.2.2", "## Check moderation permissions"), ("comment.moderate", "story.moderate", "commentsubmission", "SEC_checkToken")),
    "plugins/plugin-installation-management": ("plugins/plugin-installation-management/README.md", ("## Locate the Geeklog 2.2.2 plugin manager", "## Upgrade states and dependencies", "## Verify permissions and plugin lifecycle"), ("plugin.edit", "plugin.install", "plugin.upload", "PLG_upgrade", "PLG_resolveDependencies")),
}

# Important role/route distinctions must remain documented across revisions.
WORKFLOW_GATES = {
    "user-guide/overview": ("Why two users may see different publishing screens", "story.edit", "submitloginrequired"),
    "user-guide/articles-and-topics": ("Submission outcomes and role-aware navigation", "STORY_SAVED", "STORY_SAVED_SUBMISSION", "TOPIC_ROOT"),
    "user-guide/blocks-and-navigation": ("Check block visibility and display options", "phpblock", "PLG_getBlockLocations"),
    "user-guide/comments-and-moderation": ("When the moderation dashboard shows nothing", "SEC_hasModerationAccess", "comment.moderate"),
    "plugins/plugin-installation-management": ("Plugin manager actions: reading is not upgrading", "info_installed", "autoinstall", "updatethisplugin"),
}

def main():
    for slug, (source, headings, terms) in CASES.items():
        markdown_path = ROOT / "docs" / source
        html_path = ONLINE / ("user-guide" if slug == "user-guide/overview" else slug) / "index.html"
        assert markdown_path.is_file(), markdown_path
        assert html_path.is_file(), html_path
        markdown = markdown_path.read_text(encoding="utf-8")
        page = html_path.read_text(encoding="utf-8")
        for heading in headings:
            assert heading in markdown, (source, heading)
        for term in terms:
            assert term in markdown, (source, term)
            assert term in page, (slug, term)
        for required in WORKFLOW_GATES[slug]:
            assert required in markdown and required in page, (slug, "missing workflow gate", required)
        assert "[x]" not in markdown.lower(), f"Manual checklist already marked completed: {source}"
        assert re.search(r"https://github[.]com/Geeklog-Core/geeklog/blob/v2[.]2[.]2/", markdown), (
            "Missing immutable Core source reference", source
        )
        assert "staging" in markdown.lower(), f"Missing real-world verification boundary: {source}"
    scenario_file = ROOT / "planning/PHASE2-STAGING-SCENARIOS.csv"
    with scenario_file.open(encoding="utf-8", newline="") as stream:
        scenarios = list(csv.DictReader(stream))
    expected_columns = {"case_id", "guide", "actor", "precondition", "action", "expected_result", "source", "status", "evidence"}
    assert scenarios and set(scenarios[0]) == expected_columns, "Incorrect scenario schema"
    expected_guides = set(CASES)
    expected_roles = {"anonymous", "contributor", "editor", "topic_editor", "story_editor", "block_editor", "moderator", "plugin_editor", "plugin_admin", "staticpages_editor", "feed_admin", "unauthorized"}
    assert len(scenarios) >= 30, "Too few source-mapped acceptance scenarios"
    assert len({item["case_id"] for item in scenarios}) == len(scenarios), "Duplicate case IDs"
    assert {item["guide"] for item in scenarios} == expected_guides | {"user-guide/syndication-rss-autotags", "plugins/static-pages"}, "Missing practical guide acceptance coverage"
    for item in scenarios:
        assert item["actor"] in expected_roles, (item["case_id"], "Unexpected test role")
        assert item["status"] in {"NOT_RUN", "PASS", "FAIL", "BLOCKED"}, (item["case_id"], "Unknown test status")
        assert all(item[field].strip() for field in ("case_id", "guide", "actor", "precondition", "action", "expected_result", "source")), item
        assert item["source"].startswith(("public_html/", "system/")), (item["case_id"], "Missing tagged Core source")
        if item["status"] != "NOT_RUN":
            assert item["evidence"].strip(), (item["case_id"], "Manual evidence required for a claimed outcome")
    print(f"PASS: {len(scenarios)} version-scoped staging cases covering every P0 guide; no results asserted without evidence")
    print(f"PASS: {len(CASES)} P0 guides and generated pages include source-backed procedures, exact rights, and operational checks")
    print("NOTE: this is documentation coverage, not execution of a Geeklog installation")


if __name__ == "__main__":
    main()
