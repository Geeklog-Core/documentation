# Plugin configuration versus documentation anchors

Initial static comparison on 2026-10-29. Source: bundled plugin `install_defaults.php` `$c->add()` option declarations, compared with `desc_*` anchors in English HTML docs.

**Do not interpret each difference as a missing help link.** Permission arrays are represented by subfield anchors `_0` through `_3`, while configuration declarations use the unsuffixed array key. XMLSitemap includes additional documented subkeys. Neither the configuration upgrade paths nor runtime UI have been tested.

| Plugin | Declared option keys | Documented `desc_` anchors | Initial interpretation |
| --- | ---: | ---: | --- |
| Calendar | 22 | 31 | Permission-array split anchors |
| Links | 19 | 28 | Permission-array split anchors |
| Polls | 25 | 40 | Permission-array split anchors |
| Spam-X | 12 | 12 | Exact name match |
| Static Pages | 33 | 41 | Permission-array splits; `langurl_staticpages` is a hidden Core option |
| XMLSitemap | 14 | 18 | Additional `frequencies_*` subkey anchors |
| reCAPTCHA | 23 | 23 | Exact name match |

## Next checks

- [x] Confirmed `langurl_staticpages` is declared with type `@hidden` and group `Core` in Static Pages initial install and upgrade code. It is not an ordinary visible Static Pages setting; absence of a `desc_` anchor does not prove a documentation defect.
- [ ] Explicitly normalize array permission anchors, then compare actual interactive options rather than raw keys.
- [ ] Review defaults installed by upgrades and programmatic configuration changes.
- [ ] Test UI-rendered help links for each active plugin and record actual URL/anchor results.
- [ ] Preserve historical anchors even when currently unused; only retire them with a reviewed redirect or compatibility plan.

Full raw comparison and file SHAs: [plugin-config-crosscheck.json](plugin-config-crosscheck.json). No source files in Geeklog Core changed.

## Normalized regression check

The new [check_plugin_config.py](../tools/check_plugin_config.py) expands a known permission array only when all four indexed anchors (`_0` to `_3`) exist in the legacy snapshot. This avoids flagging those legitimate UI subfields as missing. The remaining expected static differences are:

- `staticpages.langurl_staticpages`: hidden Core option, not a visible plugin setting.
- Four `xmlsitemap.frequencies_*` entries: documented subkeys that need separate behavioral review.

This check compares **stored source snapshots**, not the current state of a running Geeklog installation. The expected exception list is explicit so future snapshot changes do not pass silently.
