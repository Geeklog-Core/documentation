#!/usr/bin/env python3
"""Compare generated installation HTML with frozen legacy source contract."""
import json
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
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get("id"): self.ids.add(a["id"])
        if tag=="a" and a.get("name"): self.names.add(a["name"])

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
    # Check against frozen source list, not a separately hard-coded generated list.
    print(f"PASS: all {len(expected)} original named anchors preserved as id and name")
    print("WARNING: original ../images/logo.gif path is not preserved in preview; original distribution packaging remains unverified")

if __name__=="__main__":
    main()
