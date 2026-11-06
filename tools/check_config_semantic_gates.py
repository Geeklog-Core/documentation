#!/usr/bin/env python3
"""Twelve source-backed Geeklog 2.2.2 semantic regression checks; not full parity."""
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
}
rows = re.findall(r"<tr\b[^>]*>[\s\S]*?</tr>", source, re.I)
for setting, tokens in checks.items():
    hits = [row for row in rows if 'name="desc_' + setting + '"' in row]
    assert len(hits) == 1, "Original option missing: " + setting
    cells = re.findall(r"<td\b[^>]*>([\s\S]*?)</td>", hits[0], re.I)
    assert len(cells) == 3, "Original row malformed: " + setting
    original = re.sub(r"<[^>]*>", " ", unescape(cells[2])).lower()
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
