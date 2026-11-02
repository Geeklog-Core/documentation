#!/usr/bin/env python3
"""Compare generated installation HTML with frozen legacy source contract."""
import json
import os
import os
from pathlib import Path
from html.parser import HTMLParser

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"planning/install-legacy-contract.json"
OUTPUT=ROOT/"build/english/install.html"

class Scan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=set()
        self.names=set()
        self.references=set()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get("id"): self.ids.add(a["id"])
        if tag=="a" and a.get("name"): self.names.add(a["name"])
        for field in ("href", "src"):
            if a.get(field): self.references.add(a[field])

def main():
    contract=json.loads(MANIFEST.read_text(encoding="utf-8"))
    expected=set(contract["legacy_named_anchors"])
    assert len(expected)==len(contract["legacy_named_anchors"])==9
    assert contract["source_blob_sha"]=="eae47434247b4fc0e54706ee9b116618cc40f83e"
    assert OUTPUT.is_file(), "Generate preview first"
    scan=Scan()
    scan.feed(OUTPUT.read_text(encoding="utf-8"))
    assert expected<=scan.ids, f"Missing id anchors: {sorted(expected-scan.ids)}"
    assert expected<=scan.names, f"Missing name anchors: {sorted(expected-scan.names)}"
    paths=set(contract["legacy_local_references"])
    assert paths<=scan.references, f"Missing historical references: {sorted(paths-scan.references)}"
    build=ROOT/"build/english"
    for relative in paths:
        assert (build/relative).resolve().is_file(), f"Missing original-path asset: {relative}"
    assert (ROOT/"build/images/logo.gif").read_bytes()[:6].startswith(b"GIF8")
    pinned = os.environ.get("GEEKLOG_CORE_DOCS")
    if pinned:
        core = Path(pinned)
        for source_rel, output_rel in (
            ("docstyle.css", "docstyle.css"),
            ("images/logo.gif", "images/logo.gif"),
            ("english/index.html", "english/index.html"),
            ("english/support.html", "english/support.html"),
        ):
            assert (core / source_rel).read_bytes() == (ROOT / "build" / output_rel).read_bytes(), source_rel
        print("PASS: original Core CSS, logo, index and support are byte-identical")
    # Check against frozen source list, not a separately hard-coded generated list.
    print(f"PASS: all {len(expected)} original named anchors preserved as id and name")
    print("PASS: four legacy local paths resolve in offline preview")
    print("PASS: historical CSS and logo paths retained; full Core release integration remains unverified")

if __name__=="__main__":
    main()
