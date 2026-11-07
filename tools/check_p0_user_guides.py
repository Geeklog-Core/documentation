#!/usr/bin/env python3
"""Regression checks for phase-two P0 Geeklog documentation.

Only source and rendered HTML structure is checked. The test does not certify
administration workflows, PHP permissions or UI behavior in a running Geeklog.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ONLINE = ROOT / "dist/online/modern"
CASES = {
    "user-guide/overview": ("user-guide/README.md", ("## Everyday tasks and source-backed administration paths", "## Practical learning path"), ("submit.php", "admin/article.php", "admin/topic.php", "admin/block.php", "admin/moderation.php", "admin/plugins.php")),
    "user-guide/articles-and-topics": ("user-guide/articles-and-topics/README.md", ("## Choose the correct workflow in Geeklog 2.2.2", "## Article scheduling and topic hierarchy: fields to verify", "## Staging acceptance checklist"), ("story.edit", "topic.edit", "story.moderate", "listdraftstories")),
    "user-guide/blocks-and-navigation": ("user-guide/blocks-and-navigation/README.md", ("## Configure a block using the Core administrator", "## Block types in Geeklog 2.2.2"), ("block.edit", "block.delete", "normal", "portal", "phpblock", "gldefault")),
    "user-guide/comments-and-moderation": ("user-guide/comments-and-moderation/README.md", ("## Understand the moderation queues in Geeklog 2.2.2", "## Moderation acceptance tests"), ("comment.moderate", "story.moderate", "commentsubmission", "SEC_checkToken")),
    "plugins/plugin-installation-management": ("plugins/plugin-installation-management/README.md", ("## Locate the Geeklog 2.2.2 plugin manager", "## Upgrade states and dependencies", "## Permission and lifecycle acceptance"), ("plugin.edit", "plugin.install", "plugin.upload", "PLG_upgrade", "PLG_resolveDependencies")),
}

def main():
    for slug, (source, headings, terms) in CASES.items():
        markdown_path = ROOT / "docs" / source
        html_path = ONLINE / slug / "index.html"
        assert markdown_path.is_file(), markdown_path
        assert html_path.is_file(), html_path
        markdown = markdown_path.read_text(encoding="utf-8")
        page = html_path.read_text(encoding="utf-8")
        for heading in headings:
            assert heading in markdown, (source, heading)
        for term in terms:
            assert term in markdown, (source, term)
            assert term in page, (slug, term)
        assert "[x]" not in markdown.lower(), f"Manual checklist already marked completed: {source}"
        assert re.search(r"https://github[.]com/Geeklog-Core/geeklog/blob/v2[.]2[.]2/", markdown), (
            "Missing immutable Core source reference", source
        )
        assert "staging" in markdown.lower(), f"Missing real-world verification boundary: {source}"
    print(f"PASS: {len(CASES)} P0 guides and generated pages include source-backed procedures, exact rights, and unchecked staging gates")
    print("NOTE: this is documentation coverage, not execution of a Geeklog installation")


if __name__ == "__main__":
    main()
