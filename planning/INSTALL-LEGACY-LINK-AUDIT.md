# Legacy link audit — installation integration

Date: 2026-11-01. Source: pinned `Geeklog-Core/geeklog` commit `dd44c01368afad32e16467fd5357af3299c11d3a`.

CI scans 14 English HTML pages of the assembled legacy documentation tree, with only `english/install.html` generated from Markdown.

## Findings

Seven references from unchanged `english/changes.html` fail the local-fragment check, comprising five unique targets:

| Source | Fragment target | Occurrences | Classification |
| --- | --- | ---: | --- |
| changes.html | `#changes1.7.2` | 1 | Missing historical section anchor |
| changes.html | `config.html#submission` | 3 | Obsolete section anchor, absent from current `config.html` |
| changes.html | `config.html#image` | 1 | Obsolete section anchor, absent |
| changes.html | `config.html#links` | 1 | Obsolete section anchor, absent |
| changes.html | `config.html#login` | 1 | Obsolete section anchor, absent |

The source `config.html` now uses granular configuration anchors; do not guess replacements for the former section links without editorial review.

These defects are **inherited from untouched Core documentation**, not introduced by the installation Markdown overlay. Neither the old documents nor the official Core repository were modified.

## Regression policy

The exact seven occurrences are frozen in `planning/install-legacy-link-baseline.json`. `tools/check_install_bundle.py` now fails on any difference (new broken links, removed ones or changed targets) rather than silently accepting any inherited failures. The CI also writes `build/legacy-link-audit.json` for investigation.

## Remaining work

- Decide whether the old changelog references should be redirected to meaningful current configuration sections or preserved with explanatory notes.
- Validate external links separately.
- Test a real packaged Geeklog installation and editor-approved migration output.

CI reference: https://github.com/hostellerie/documentation/actions/runs/41268192768
