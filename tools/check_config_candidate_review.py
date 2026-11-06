#!/usr/bin/env python3
"""Review-only integrity gate for the isolated Markdown config.html candidate.

The candidate ZIP is intentionally *not* an installable documentation overlay.
This checks its contents and sampled help targets; it does not execute Geeklog,
change the embedded legacy HTML, or prove live administrator behavior.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import os
import zipfile

ROOT = Path(__file__).resolve().parents[1]
LEGACY = Path(os.environ["GEEKLOG_CORE_DOCS"]) / "english/config.html"
RELEASE = ROOT / "dist/geeklog-2.2.2/public_html/docs/english/config.html"
CANDIDATE = ROOT / "dist/config-candidate/public_html/docs/english/config.html"
ZIP = ROOT / "dist/config-candidate-review.zip"
REPORT = ROOT / "dist/config-candidate-report.json"
MEMBER = "public_html/docs/english/config.html"
SAMPLES = (
    "desc_site_url",
    "desc_mail_settings_port",
    "desc_ip_anonymization",
    "desc_filemanager_disabled",
    "desc_default_permissions_story_3",
    "desc_autotag_permissions_structureddata_1",
    "desc_frontpage",
    "desc_commentsubmission",
    "desc_language_files",
    "desc_languages",
)

class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.anchors = set()
        self.duplicates = set()
        self.links = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        targets = [a["id"]] if a.get("id") else []
        if tag == "a" and a.get("name") and a["name"] != a.get("id"):
            targets.append(a["name"])
        for target in targets:
            if target in self.anchors:
                self.duplicates.add(target)
            self.anchors.add(target)
        if tag in ("a", "link") and a.get("href"):
            self.links.append(a["href"])

def parse(data):
    parser = Links()
    parser.feed(data.decode("utf-8"))
    return parser

def validate_archive(archive, candidate_bytes):
    """Reject extra members and any mismatch against the generated candidate."""
    assert archive.testzip() is None, "Corrupt candidate review ZIP"
    assert archive.namelist() == [MEMBER], "Candidate review must be a single config.html file"
    info = archive.infolist()[0]
    assert not info.is_dir(), "Unexpected directory"
    assert (info.external_attr >> 16) & 0o170000 != 0o120000, "Symlink member"
    assert archive.read(MEMBER) == candidate_bytes, "Archive differs from generated candidate"


def validate_anchors(original_bytes, candidate_bytes):
    baseline = parse(original_bytes)
    candidate = parse(candidate_bytes)
    assert not candidate.duplicates, f"Duplicate anchor IDs: {sorted(candidate.duplicates)[:5]}"
    assert candidate.anchors == baseline.anchors, "Legacy help anchor set differs"
    assert len(candidate.anchors) == 449, "Unexpected source anchor count"
    assert set(SAMPLES) <= candidate.anchors, "Missing sampled configuration help target"
    for link in candidate.links:
        target = urlsplit(link)
        if target.path == "" and target.fragment:
            assert unquote(target.fragment) in candidate.anchors, "Broken internal help link: " + link
    assert "../docstyle.css" in candidate.links, "Legacy stylesheet link absent"
    assert b"Documented default (Geeklog 2.2.2)" in candidate_bytes
    return candidate


def main():
    original_bytes = LEGACY.read_bytes()
    candidate_bytes = CANDIDATE.read_bytes()
    assert RELEASE.is_file() and REPORT.is_file()
    # The standard distribution still must contain historical config.html.
    # Compare normalized line endings because the source and source archive
    # may have different historical checkout normalization.
    normalize = lambda b: b.replace(b"\r\n", b"\n")
    assert normalize(RELEASE.read_bytes()) == normalize(original_bytes), (
        "The standard embedded config.html has changed"
    )
    with zipfile.ZipFile(ZIP) as archive:
        validate_archive(archive, candidate_bytes)
    candidate = validate_anchors(original_bytes, candidate_bytes)
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    assert report["legacy_embedded_configuration_replaced"] is False
    assert report["historical_unique_anchors"] == 449
    assert report["generated_unique_anchors"] == 449
    assert report["content_parity"].startswith("INCOMPLETE")
    print("PASS: review ZIP contains exactly the generated config.html; no other files")
    print("PASS: standard embedded config is still the historical source")
    print(f"PASS: {len(candidate.anchors)} anchors and {len(SAMPLES)} sampled help targets checked")
    print("PENDING: candidate installation, real admin help clicks, security and editorial approval")

if __name__ == "__main__":
    main()
