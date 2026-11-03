# Installation migration checklist

Source: `Geeklog-Core/geeklog` master `public_html/docs/english/install.html`, blob `eae47434247b4fc0e54706ee9b116618cc40f83e` (checked 2026-10-29).

Historical checklist migrated to the official documentation repository. PR #1 has been superseded and closed; the documentation architecture has been merged via PR #2 and GitHub Pages is live. This checklist retains earlier milestones for traceability.

- [x] Identify nine legacy named HTML anchors and record them in `docs/installation/README.md`.
- [x] Write a limited installation/upgrade/migration introduction with explicit release-specific caveats.
- [x] Inspect the 2.2.2 installer class entrypoint and requirement constants; see `INSTALL-REQUIREMENTS-SOURCE-AUDIT.md`.
- [ ] Exercise installer installation/upgrade/migrate flows in staging and test the actual packaged release.
- [x] Record the historical 2.2.2 minimum constants (PHP 5.6.4, MySQL 4.1.3, PostgreSQL 9.1.7) **as source facts only**, not safe deployment baselines.
- [ ] Verify currently supported runtime/database requirements and the future 2.2.3 release separately.
- [x] Extend the source-derived installation, upgrade, migration and troubleshooting draft with safer diagnostic recommendations.
- [ ] Verify all legacy troubleshooting examples and version-specific procedures before treating the draft as comprehensive.
- [x] Add standalone Markdown-to-HTML preview and test of all nine legacy `id` / `name` anchors on this branch; [CI succeeded](https://github.com/hostellerie/documentation/actions/runs/40865064684).
- [x] Inventory original HTML local assets/navigation and historical external references in `INSTALL-RESOURCE-AUDIT.md`.
- [x] Add standalone checks for local relative paths and fragment links, with a real table of contents linking to preserved historical anchors; [CI successful](https://github.com/hostellerie/documentation/actions/runs/40866083596).
- [x] Generate an independent **preview-only** offline bundle: `build/english/install.html`, `index.html`, `support.html`, `build/docstyle.css`, `build/images/logo.svg`; verify relative references in install page and upload complete bundle in CI ([successful run](https://github.com/hostellerie/documentation/actions/runs/40866357612)).
- [x] Validate **all three generated HTML pages** and their local resources across the whole preview bundle; deliberate missing-file and missing-fragment negative tests pass ([CI](https://github.com/hostellerie/documentation/actions/runs/41184209438)).
- [x] Capture frozen legacy installation source anchor/resource contract in `install-legacy-contract.json` and add generated-vs-original anchor comparison in `check_install_legacy.py`.
- [x] Preserve original `../images/logo.gif` file path using a transparent 1×1 **placeholder** (not official Geeklog imagery). All four local references in the source manifest now resolve; replace the placeholder with licensed original assets before shipping.
- [ ] Integrate with eventual shared build and validate original assets, all bundled docs, external references, release packaging and a real Geeklog installation. The SVG is a text-only preview mark, **not** the official logo.
- [ ] Verify documentation against a packaged installation and obtain maintainer review.

**Non-goal:** replacing or deleting existing shipped installation HTML in this branch.

## Pinned Core assets integration (2026-11-01)

- [x] CI checks out Geeklog Core at pinned commit `dd44c01368afad32e16467fd5357af3299c11d3a` and copies the **actual** `public_html/docs/docstyle.css` and `public_html/docs/images/logo.gif` into their original relative locations.
- [x] Byte-for-byte equality of both copied assets is checked against the pinned checkout; [GitHub Actions successful](https://github.com/hostellerie/documentation/actions/runs/41260273461).
- [ ] Original `index.html` and `support.html` remain preview placeholders; validate full published documentation and packaging before release.

## End-to-end legacy tree overlay — 2026-11-01

- [x] GitHub Actions copies the complete documentation tree from pinned Geeklog Core commit `dd44c01368afad32e16467fd5357af3299c11d3a` and overlays ONLY the generated `english/install.html`.
- [x] Confirm original `english/index.html`, `english/support.html`, `docstyle.css`, and `images/logo.gif` remain byte-for-byte identical to the pinned Core checkout.
- [x] Scan 14 English HTML pages; generated installation document and its local references pass strict validation; [CI passed](https://github.com/hostellerie/documentation/actions/runs/41260633640).
- [ ] Investigate **7 pre-existing local reference/fragment issues** reported in the inherited legacy docs. They are not automatically repaired or hidden as a compatibility success.
- [ ] Test assembled output in a real Geeklog release installation and review version-specific instructions.

- [x] Triage inherited seven link defects (five unique targets) in unchanged `changes.html` and freeze an exact CI baseline; [passing run](https://github.com/hostellerie/documentation/actions/runs/41268192768). See `INSTALL-LEGACY-LINK-AUDIT.md`.
- [ ] Editorially determine replacement destinations; no historic Core HTML modified.

## External links and approvals — 2026-11-01

- [x] Audit the four actual external links in Markdown draft; separate example URLs from actionable links. See `INSTALL-EXTERNAL-LINK-AUDIT.md`.
- [ ] Replace contributor-branch audit link with stable documentation URL once Tom approves architecture.
- [ ] Obtain technical validation of actual staging install/upgrade/migrate flows before any production guidance.
- [ ] Wait for Tom's review of PR #1 before proposing a second PR, release packaging or official documentation replacement.

## Complete documentation overlay integrity — 2026-11-01

- [x] Add `tools/check_install_overlay.py` to compare SHA-256 of **every** pinned Core documentation file against output; only `english/install.html` may differ, and optional `legacy-link-audit.json` may be added. [CI passed](https://github.com/hostellerie/documentation/actions/runs/41294526352).
- [ ] Run complete Geeklog install/upgrade/migrate in an approved isolated environment. This script does not execute the installer or validate runtime compatibility.

## Staging readiness — 2026-11-01

- [x] Prepare isolated new-install, upgrade, migration, offline-doc, rollback and security test matrix in `INSTALL-STAGING-VALIDATION.md`.
- [ ] Obtain approval for disposable staging environment before performing runtime tests; never test on production.

## Post-publication installation review — 2026-11-03

- [x] User validated the generated installation page and representative historical links in Geeklog 2.2.2 Docker, along with all seven plugin documentation pages and representative administration help links. See `INSTALL-STAGING-VALIDATION.md` for the **limited scope**.
- [x] Confirm tagged installer constants and official v2.2.2 release notes. **Discrepancy:** release notes say MySQL 4.1.2, tagged installer's `Common.php` says MySQL 4.1.3. Both are historical minimums; see `INSTALL-REQUIREMENTS-SOURCE-AUDIT.md`.
- [x] Publish initial official Markdown website at https://geeklog-core.github.io/documentation/; note that online installation text and embedded ZIP still have different release-readiness states.
- [ ] Execute clean install, upgrade, migrate, rollback, and security checks in approved disposable environments; merely opening HTML in Docker does not exercise the installer.
- [ ] Compare generated output with the exact downloadable Geeklog 2.2.2 release archive; tag-source identity is already checked but cannot establish package identity.
- [ ] Technical/editorial release review of the installation draft before treating it as authoritative.

## Exact 2.2.2 release tarball verification — 2026-11-03

- [x] Add `tools/check_official_release_docs.py` to compare posted official archive size/MD5 and SHA-256 of all packaged Core and reCAPTCHA documentation against pinned `v2.2.2` source.
- [x] Add four synthetic tarball regression cases (`tools/test_official_release_docs.py`) and run them in dual-output CI; documented in `OFFICIAL-ARCHIVE-VALIDATION.md`.
- [x] Received `geeklog-2.2.2.tar.gz` from the user; actual file size 16,978,448 bytes and MD5 `962cc6e6ed1ce13f65066e47859511d8` exactly match official metadata; SHA-256 `d12991f78225289d2bac297bff1a7e9be55f04a9e0aa097bb379e41d7fb138a8`.
- [x] Compared all 46 packaged documentation files to GitHub's official `v2.2.2` tree blob IDs: 8 identical, 38 differ only by CRLF vs LF, 0 missing, 0 extra, 0 substantive differences. Updated checker to report CRLF-only differences separately and require explicit opt-in to accept them. See `OFFICIAL-ARCHIVE-VALIDATION.md`.
- [x] Updated checker unit tests passed in [CI run 41564854616](https://github.com/hostellerie/documentation/actions/runs/41564854616) (5 synthetic cases), and the **actual generated artifact ZIP** was compared to the **actual user-supplied 2.2.2 tar.gz**: 46/46 files, 0 missing or extra, 8 byte-identical, 37 line-ending-only changes, and exactly **one intended content replacement**: `docs/english/install.html`. Full evidence in `OFFICIAL-ARCHIVE-VALIDATION.md`.
- [ ] Still required: execute installer, upgrade, migration, rollback and post-install security scenarios in disposable staging and obtain editorial/release maintainer approval before distributing the generated HTML as an official release.

## Safe Docker installer preflight — 2026-11-03

- [x] Inspected real official 2.2.2 tarball installer entrypoint `public_html/admin/install/index.php`: sets `GL_INSTALL_ACTIVE`, loads `Common.php`, `Install.php`, `Upgrade.php`, `Migrate.php` and `installer.class.php`, then runs `Installer::run()`.
- [x] Reconfirmed in packaged `Common.php` historic requirements PHP 5.6.4, MySQL 4.1.3 and PostgreSQL 9.1.7 (source values only, not secure recommendations).
- [x] Added `tools/inspect_docker_staging.py` with **read-only Docker inspect only**; emits state, image name, published ports and mount types/destination paths but not environment/credentials/source paths.
- [x] Added detailed `planning/INSTALL-STAGING-VALIDATION.md` preflight instructions, independent volumes/networks/databases, five disposable workflows and safety stop conditions.
- [ ] Execute read-only preflight on user's local Docker host and inspect sanitised output.
- [ ] Create and verify *independent disposable* Docker staging environment before exercising installer/upgrade/migrate; existing Geeklog 2.1.1 and 2.2.2 containers must stay untouched.
