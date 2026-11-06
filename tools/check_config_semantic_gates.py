#!/usr/bin/env python3
"""Sixty-six source-backed Geeklog 2.2.2 semantic regression checks; not full parity."""
from pathlib import Path
import os
import re
from html import unescape

root = Path(__file__).resolve().parents[1]
source = (Path(os.environ["GEEKLOG_CORE_DOCS"]) / "english/config.html").read_text(encoding="utf-8")
markdown = (root / "docs/configuration/README.md").read_text(encoding="utf-8")
checks = {
    "mail_settings_backend": ["smtp", "smtps", "sendmail", "mail", "OpenSSL"],
    "pass_alg": ["md5", "sha1", "sha256", "sha512", "blowfish"],
    "ip_anonymization": ["-1", "cron_schedule_interval", "log files"],
    "url_routing": ["URL rewriting", "index.php", "web server"],
    "filemanager_disabled": ["Root", "true"],
    "noreply_mail": ["site_mail"],
    "mail_settings_port": ["25", "587"],
    "mail_settings_auth": ["smtp", "smtps", "1", "0"],
    "invalidloginattempts": ["0"],
    "invalidloginmaxtime": ["0"],
    "enable_twofactorauth": ["Google Authenticator", "1"],
    "pass_stretch": ["iterations", "0"],
    "allow_account_delete": ["1", "Anonymous"],
    "allow_username_change": ["1", "username"],
    "custom_registration": ["true", "lib-custom.php"],
    "usersubmission": ["1", "0", "queue"],
    "disable_new_user_registration": ["true", "new"],
    "allow_domains": ["queue", "regular expressions"],
    "disallow_domains": ["queue", "regular expression"],
    "storysubmission": ["1", "0"],
    "commentsubmission": ["1", "0"],
    "trackback_enabled": ["true", "sending", "receiving"],
    "show_topic_icon": ["new articles", "article submissions", "topic icon"],
    "draft_flag": ["Story Admins", "draft", "1", "0"],
    "frontpage": ["frontpage", "topic", "archive"],
    "hide_no_news_msg": ["No News To Display", "index"],
    "hide_main_page_navigation": ["frontpage", "frontpage_topics", "older articles"],
    "onlyrootfeatures": ["root", "article admins", "feature"],
    "listdraftstories": ["moderation.php", "draft", "block"],
    "skip_preview": ["Preview", "Submit", "articles", "comments"],
    "aftersave_story": ["item", "list", "home", "admin", "submission"],
    "comment_mode": ["threaded", "nested", "flat", "nocomments"],
    "comment_order": ["ASC", "DESC", "Oldest First", "Newest First"],
    "comment_code": ["new articles", "0", "-1"],
    "comment_edit": ["Anonymous", "comment.edit", "Comment Submissions", "Queued"],
    "comment_edittime": ["seconds", "user"],
    "article_comment_close_enabled": ["new articles", "separately", "article"],
    "article_comment_close_days": ["days", "Disable Comments", "enabled"],
    "comment_close_rec_stories": ["most recent articles", "new article", "oldest", "0"],
    "allow_reply_notifications": ["subscribing", "Registered users", "email"],
    "show_comments_at_replying": ["comment list", "comment page", "comment_on_same_page"],
    "sort_admin": ["true","Admin","Command and Control","alphabetically"],
    "link_documentation": ["documentation","Admin","0"],
    "link_versionchecker": ["GL Version Test","Admin","0","Root"],
    "sortmethod": ["alpha","alphabetically","sortnum","sort number"],
    "showstorycount": ["articles","topic","Sections","0","1"],
    "showsubmissioncount": ["article submissions","topic","Sections","0","1"],
    "hide_home_link": ["Home","Sections","0","1"],
    "whosonline_threshold": ["seconds","idle"],
    "whosonline_anonymous": ["anonymous users","number","registered users","names","logged-in users"],
    "whosonline_photo": ["thumbnail","photo","else","photo icon"],
    "newstoriesinterval": ["new","seconds"],
    "newcommentsinterval": ["new","seconds"],
    "hidenewstories": ["1","new articles","What's New"],
    "hidenewcomments": ["1","new comments","What's New"],
    "whatsnew_cache_time": ["What's New","cached","no longer","seconds","0"],
    "newtrackbackinterval": ["Trackback comments","new","seconds"],
    "hidenewtrackbacks": ["1","new trackback comments","What's New"],
    "hidenewplugins": ["1","new entries by plugins","What's New"],
    "title_trim_length": ["length","title","items","What's New"],
    "language": ["default language","language files","language directory","Localization"],
    "allow_user_language": ["1","site labels","My Account"],
    "switchlang_homepage": ["switch language block","homepage","articles","topics","staticpages","404"],
    "new_item_set_current_lang": ["multiple languages","COM_makeSid","current language","Articles","Staticpages","Blocks","Topics"],
    "language_files": ["language shortcuts","same number of characters","language files","hreflang","both","enabled","disabled"],
    "languages": ["language shortcuts","native name","match","Language Files","enabled","disabled"],
}
rows = re.findall(r"<tr\b[^>]*>[\s\S]*?</tr>", source, re.I)
for setting, tokens in checks.items():
    hits = [row for row in rows if 'name="desc_' + setting + '"' in row]
    assert len(hits) == 1, "Original option missing: " + setting
    cells = re.findall(r"<td\b[^>]*>([\s\S]*?)</td>", hits[0], re.I)
    assert len(cells) == 3, "Original row malformed: " + setting
    original = re.sub(r"\s+", " ", re.sub(r"<[^>]*>", " ", unescape(cells[2]))).strip().lower()
    heading = "### `" + setting + "`\n"
    assert markdown.count(heading) == 1, "Markdown heading missing: " + setting
    current = markdown.split(heading, 1)[1].split("\n<a id=", 1)[0].lower()
    for token in tokens:
        assert token.lower().replace(" ", "-") in current.replace(" ", "-"), (
            "Lost option detail " + setting + ": " + token)
        assert token.lower().replace(" ", "-") in original.replace(" ", "-"), (
            "Source meaning changed " + setting + ": " + token)
assert "not current password-security guidance" in markdown.lower()
print(f"PASS: {len(checks)} release-scoped semantic checks; no complete editorial-parity claim")
