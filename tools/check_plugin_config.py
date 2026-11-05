#!/usr/bin/env python3
"""Compare installed-default plugin option names with legacy HTML help anchors.

Static source snapshot only. Array subkeys are normalized exclusively for known
permission-array options whose _0.._3 anchors are all present.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "planning" / "plugin-config-crosscheck.json"

def inspect():
    source = json.loads(DATA.read_text(encoding="utf-8"))
    outcomes = []
    for plugin in source["plugins"]:
        declared, anchors = set(plugin["declared"]), set(plugin["documented"])
        permission_groups = set()
        for option in declared:
            if not option.endswith("permissions") and "_permissions_" not in option:
                continue
            expected = {f"{option}_{index}" for index in range(4)}
            if expected <= anchors:
                permission_groups.add(option)
        expanded = (declared - permission_groups) | {
            f"{option}_{index}" for option in permission_groups for index in range(4)
        }
        missing = sorted(expanded - anchors)
        additional = sorted(anchors - expanded)
        outcomes.append({
            "plugin": plugin["plugin"],
            "permission_arrays_expanded": sorted(permission_groups),
            "missing": missing,
            "additional": additional,
        })
    return outcomes

def main():
    results = inspect()
    for result in results:
        print(f"{result['plugin']}: missing={result['missing']} additional={result['additional']}")
    expected_missing = {"staticpages": ["langurl_staticpages"]}
    expected_extra = {"xmlsitemap": ["frequencies_article", "frequencies_calendar", "frequencies_polls", "frequencies_staticpages"]}
    for result in results:
        name = result["plugin"]
        assert result["missing"] == expected_missing.get(name, []), f"Unexpected missing options for {name}"
        assert result["additional"] == expected_extra.get(name, []), f"Unexpected additional anchors for {name}"
    print("Normalized plugin configuration snapshot: expected differences only (no runtime validation)")

if __name__ == "__main__":
    main()
