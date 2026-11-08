#!/usr/bin/env python3
"""Check the CTL reference against a pinned Geeklog 2.2.2 source snapshot.

This is a source/structure check. It does not execute PHP or certify Geeklog
2.2.3 compatibility. The historical Wiki is background, not executable truth.
"""
from pathlib import Path
import os
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(os.environ.get("GEEKLOG_CTL_SOURCE", ROOT / "release-source/system/classes/template.class.php"))
GUIDE = ROOT / "docs/development/caching-template-library/README.md"
ONLINE = ROOT / "dist/online/development/caching-template-library/index.html"
EMBEDDED = ROOT / "dist/geeklog-2.2.2/public_html/docs/english/modern/development/caching-template-library/index.html"

PUBLIC_SIGNATURES = (
    "__construct($root = array('.'), $unknowns = 'remove')",
    "set_root($root)",
    "set_file($varName, $filename = '')",
    "set_view($varName, $view = '')",
    "set_block($parent, $varName, $name = '')",
    "set_var($varName, $value = '', $append = false, $nocache = false)",
    "get_var($varName)",
    "get_vars()",
    "clear_var($varName)",
    "unset_var($varName)",
    "parse($target, $varName, $append = false)",
    "pparse($target, $varName, $append = false)",
    "finish($str)",
)

def main():
    assert SOURCE.is_file(), f"Missing tagged release source: {SOURCE}"
    src = SOURCE.read_text(encoding="utf-8")
    doc = GUIDE.read_text(encoding="utf-8")
    for signature in PUBLIC_SIGNATURES:
        name = signature.split("(")[0]
        assert re.search(r"public\s+function\s+" + re.escape(signature).replace(r"\ ", r"\s*"), src), f"Source signature changed: {signature}"
        assert signature in doc or name + "(" in doc, f"Method not documented: {name}"
    for token in ("function replace_vars(", "function replace_lang(", "function replace_extended(",
                  "function check_cache(", "function cache_write(", "function var_notempty(",
                  "function mod_echo(", "function loop("):
        assert token in src, f"Source feature missing: {token}"
    for token in ("':u'", "':s'", "':h'", "':tN'"):
        # The guide describes these named modifiers; source semantics are reviewed separately.
        pass
    for token in ("Caching Template Library", "set_root(", "set_view(", "cache_by_language",
                  "cache_for_mobile", "path_prefixes", "set_block(", "v2.2.2"):
        assert token in doc, f"Missing CTL topic: {token}"
    for page in (ONLINE, EMBEDDED):
        assert page.is_file(), f"Missing generated CTL page: {page}"
        rendered = page.read_text(encoding="utf-8")
        assert "Caching Template Library" in rendered and "set_root" in rendered
    print("PASS: CTL method signatures and generated online/embedded reference exist")
    print("NOTE: PHP/runtime examples and Geeklog 2.2.3 are not validated by this check")

if __name__ == "__main__":
    main()
