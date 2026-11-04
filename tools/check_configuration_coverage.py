#!/usr/bin/env python3
"""Measure configuration-help Markdown coverage against pinned Geeklog Core HTML.

Never changes embedded config.html. Fail only for source mismatches or loss of
an already-covered configuration anchor; report remaining work, do not fake
completion. Intended to run after check_install_anchors.py and build_dual_preview.py.
"""
import json
import os
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = Path(os.environ["GEEKLOG_CORE_DOCS"]) / "english/config.html"
PACKAGED = ROOT / "dist/geeklog-2.2.2/public_html/docs/english/config.html"
WEB = ROOT / "dist/online/configuration.html"
REPORT = ROOT / "dist/configuration-coverage.json"


class Anchors(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.identifiers = []
    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        for name in ("id", "name"):
            value = attributes.get(name)
            if value:
                self.identifiers.append(value)


def names(path):
    parsed = Anchors()
    parsed.feed(path.read_text(encoding="utf-8"))
    return set(parsed.identifiers)


def main():
    for path in (CORE, PACKAGED, WEB):
        if not path.is_file():
            raise SystemExit(f"Required input absent: {path}")
    assert PACKAGED.read_bytes() == CORE.read_bytes(), (
        "Embedded config.html differs from pinned source")
    source = {name for name in names(CORE) if name.startswith("desc_")}
    rendered = {name for name in names(WEB) if name.startswith("desc_")}
    assert len(source) >= 300, "Unexpectedly small source anchor inventory"
    unknown = rendered - source
    assert not unknown, f"Online configuration anchors not in pinned source: {sorted(unknown)}"
    # The two existing intentionally migrated examples must remain available.
    # Verified site, mail and syndication migration baseline is a regression baseline.
    required = {
        "desc_site_url", "desc_site_name",
        "desc_site_admin_url", "desc_site_slogan", "desc_path_site_logo",
        "desc_site_disabled_msg", "desc_owner_name", "desc_copyrightyear",
        "desc_url_rewrite", "desc_url_routing", "desc_cdn_hosted",
        "desc_meta_tags", "desc_meta_description", "desc_meta_keywords",
        "desc_cookie_consent", "desc_about_cookies_link",
        "desc_terms_of_use_link", "desc_privacy_policy_link",
        "desc_ip_anonymization", "desc_site_mail", "desc_noreply_mail",
        "desc_mail_settings_backend", "desc_mail_settings_sendmail_path",
        "desc_mail_settings_sendmail_args", "desc_mail_settings_host",
        "desc_mail_settings_port", "desc_mail_settings_auth",
        "desc_mail_settings_username", "desc_mail_settings_password",
        "desc_mail_cc_enabled", "desc_mail_cc_default", "desc_mail_charset",
        "desc_backend", "desc_rdf_file", "desc_rdf_limit",
        "desc_rdf_storytext", "desc_rdf_language",
        "desc_syndication_max_headlines", "desc_comment_feeds_article_tag",
        "desc_comment_feeds_article_tag_position",
        "desc_comment_feeds_article_author_tag",
        "desc_comment_feeds_comment_author_tag",
        "desc_maximagesperarticle",
        "desc_limitnews",
        "desc_minnews",
        "desc_contributedbyline",
        "desc_hideviewscount",
        "desc_hideemailicon",
        "desc_hideprintericon",
        "desc_allow_page_breaks",
        "desc_page_break_comments",
        "desc_article_image_align",
        "desc_show_topic_icon",
        "desc_draft_flag",
        "desc_frontpage",
        "desc_hide_no_news_msg",
        "desc_hide_main_page_navigation",
        "desc_onlyrootfeatures",
        "desc_lastlogin",
        "desc_loginrequired",
        "desc_submitloginrequired",
        "desc_commentsloginrequired",
        "desc_statsloginrequired",
        "desc_searchloginrequired",
        "desc_profileloginrequired",
        "desc_emailuserloginrequired",
        "desc_emailstoryloginrequired",
        "desc_directoryloginrequired",
        "desc_passwordspeedlimit",
        "desc_login_attempts",
        "desc_login_speedlimit",
        "desc_invalidloginattempts",
        "desc_invalidloginmaxtime",
        "desc_enable_twofactorauth",
        "desc_pass_alg",
        "desc_pass_stretch",
        "desc_theme",
        "desc_doctype",
        "desc_menu_elements",
        "desc_path_themes",
        "desc_cache_templates",
        "desc_cache_mobile",
        "desc_cache_resource",
        "desc_usersubmission",
        "desc_allow_domains",
        "desc_disallow_domains",
        "desc_storysubmission",
        "desc_listdraftstories",
        "desc_postmode",
        "desc_speedlimit",
        "desc_skip_preview",
        "desc_advanced_editor",
        "desc_advanced_editor_name",
        "desc_wikitext_editor",
        "desc_remove_4byte_chars",
        "desc_commentspeedlimit",
        "desc_comment_limit",
        "desc_comment_mode",
        "desc_comment_order",
        "desc_comment_code",
        "desc_commentsubmission",
        "desc_comment_edit",
        "desc_comment_edittime",
        "desc_article_comment_close_enabled",
        "desc_article_comment_close_days",
        "desc_comment_close_rec_stories",
        "desc_allow_reply_notifications",
        "desc_comment_on_same_page",
        "desc_show_comments_at_replying",
    }
    assert required <= rendered, f"Lost existing configuration help: {required-rendered}"
    remaining = sorted(source - rendered)
    report = {
        "source": "Pinned Geeklog 2.2.2 Core docs/english/config.html",
        "source_help_anchor_count": len(source),
        "online_help_anchor_count": len(rendered),
        "remaining_help_anchor_count": len(remaining),
        "percent_migrated": round(100 * len(source & rendered) / len(source), 2),
        "remaining_anchors": remaining,
        "note": "Coverage is structural only. Text, behavior and technical accuracy require review. Original embedded config.html stays byte-identical.",
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: pinned embedded configuration reference unchanged")
    print(f"COVERAGE: {len(rendered)}/{len(source)} help anchors on the online Markdown page; {len(remaining)} remaining")
    print(f"REPORT: {REPORT}")


if __name__ == "__main__":
    main()
