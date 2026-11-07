#!/usr/bin/env python3
"""Check the seven practical 2.2.2 tutorials in source and built documentation.

Static checks only: they do not prove that any user-interface workflow has been
performed on a live Geeklog instance. Run after build_dual_preview.py.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "dist/online"
TUTORIALS = {
    "user-guide/overview": (
        "user-guide/README.md",
        ("Hands-on learning course: build a small information site", "Lesson 1", "Lesson 2", "Lesson 3", "Lesson 4"),
        ("submit.php", "story.edit", "Static Pages"),
    ),
    "user-guide/articles-and-topics": (
        "user-guide/articles-and-topics/README.md",
        ("Detailed tutorial: write, review and publish an article", "Detailed tutorial: create a topic and a child topic", "Detailed tutorial: investigate an unpublished article"),
        ("story.moderate", "topic.edit", "STORY_SAVED_SUBMISSION"),
    ),
    "user-guide/blocks-and-navigation": (
        "user-guide/blocks-and-navigation/README.md",
        ("Detailed tutorial: create an About block", "Detailed tutorial: add a useful navigation link", "Detailed tutorial: diagnose a missing block"),
        ("block.edit", "phpblock", "normal"),
    ),
    "user-guide/comments-and-moderation": (
        "user-guide/comments-and-moderation/README.md",
        ("Detailed tutorial: comment on an article", "Detailed tutorial: moderate a submitted comment", "Detailed tutorial: process a contributed story"),
        ("comment.moderate", "commentsubmission", "story.moderate"),
    ),
    "user-guide/syndication-rss-autotags": (
        "user-guide/syndication-rss-autotags/README.md",
        ("Detailed tutorial: create an RSS feed", "Detailed tutorial: insert an autotag safely", "Follow an existing feed as a reader"),
        ("syndication.edit", "PLG_replaceTags", "RSS-2.0"),
    ),
    "plugins/plugin-installation-management": (
        "plugins/plugin-installation-management/README.md",
        ("Detailed tutorial: install and maintain a trusted plugin", "Part 1", "Part 2", "Part 3"),
        ("plugin.edit", "plugin.install", "plugin.upload"),
    ),
    "plugins/static-pages": (
        "plugins/static-pages/README.md",
        ("Detailed tutorial: create an About page with Static Pages", "Safe clone exercise"),
        ("staticpages.edit", "staticpages.PHP", "staticpages.delete"),
    ),
}

def main():
    for slug, (relative, headings, terms) in TUTORIALS.items():
        source = ROOT / "docs" / relative
        rendered = HTML / ("user-guide" if slug == "user-guide/overview" else slug) / "index.html"
        assert source.is_file() and rendered.is_file(), slug
        md = source.read_text(encoding="utf-8")
        html = rendered.read_text(encoding="utf-8")
        for phrase in headings:
            assert phrase in md and phrase in html, (slug, "missing tutorial", phrase)
        for term in terms:
            assert term in md and term in html, (slug, "missing source-linked fact", term)
        assert re.search(r"https://github[.]com/Geeklog-Core/geeklog/blob/v2[.]2[.]2/", md), (
            slug, "no pinned tagged Core citation"
        )
        assert len(re.findall(r"(?m)^\d+\. ", md)) >= 12, (slug, "insufficient action steps")
        assert "staging" in md.lower() or "disposable" in md.lower(), (slug, "missing test boundary")
    print(f"PASS: {len(TUTORIALS)} detailed tutorials have source and generated HTML coverage")
    print("NOTE: no application UI or runtime workflows were executed")

if __name__ == "__main__":
    main()
