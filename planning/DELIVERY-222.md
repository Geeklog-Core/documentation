# Geeklog documentation — rapid release checklist for Geeklog 2.2.2

Status: **release candidate / preview only**, not an official Geeklog 2.2.2 distribution. The objective is to provide **both** the public documentation on `Geeklog-Core/documentation` GitHub Pages and a verifiable offline-compatible documentation ZIP from the **same Markdown source**.

## Online publication

1. Review and merge one consolidated fork PR into `Geeklog-Core/documentation:main`; do not change upstream `main` directly without maintainer review.
2. From the official repository Actions, run **Publish Geeklog documentation (maintainer opt-in)** on `main` after merge. The workflow checks out the selected repository/ref (not a pinned fork branch).
3. Build and check the original Core 2.2.2 documents, the Markdown-generated installation page, modern supplementary guides, and all historical configuration anchors.
4. Build the **unified homepage search** (13 indexed guides), then upload `dist/online/` to GitHub Pages.
5. Visit `https://geeklog-core.github.io/documentation/`, open the homepage, its search, `configuration.html#desc_site_url`, `installation.html`, and `modern/index.html`. Verify navigation and CSS in a browser; a green CI is not a substitute for a visual check.

## Embedded Geeklog 2.2.2 documentation ZIP

1. Use the **Dual documentation prototype** workflow or the same manual publishing workflow and download the `geeklog-2.2.2-embedded-docs-preview` artifact.
2. The contained `geeklog-2.2.2-docs-preview.zip` has relative paths beginning with `public_html/`. **Inspect the ZIP**: it is an overlay into the Geeklog installation **root**, not into `public_html/docs` directly.
3. On a disposable Geeklog 2.2.2 test installation, **back up** `public_html/docs/` and `public_html/admin/plugins/recaptcha/docs/` before applying the overlay. Never assume this ZIP is a full CMS installation.
4. Unpack it **at the installation root** (in test staging only), preserving the `public_html/` prefix. Verify that the same `public_html/docs/english/install.html` path still exists and that `config.html` retains its 2.2.2 content.
5. Check `/docs/english/install.html`, `/docs/english/config.html#desc_site_url`, `/docs/english/modern/index.html`, one modern guide's CSS, and context-sensitive help launched from the actual administration UI; test all seven bundled plugin help destinations.
6. Preserve an original-docs rollback copy. Do not announce fully verified packaging until tests are recorded. The built ZIP contains unchanged legacy config/plugin help and a generated install.html; additional Markdown guides are additive under `docs/english/modern/`.

## Automated extracted-overlay test

Both CI workflows now run `tools/check_extracted_overlay.py` after building and checking the ZIP. The test copies the pinned Geeklog 2.2.2 Core documentation and tagged reCAPTCHA documentation into a **temporary disposable filesystem tree**, extracts the actual generated ZIP there, compares all original files, and confirms that only `public_html/docs/english/install.html` changes. It also verifies the modern HTML/CSS/search files exist, that unrelated installation files remain untouched, and that restoring the historical documentation returns the entire test tree to its original checksums.

This test **does not start Geeklog or a Docker container** and is **not equivalent** to clicking Core and plugin help links in the installed administrator UI. It is a repeatable filesystem packaging and restoration gate, intended to catch deployment-path errors before a manual integration test.

## Served HTTP smoke test — validated in CI

The release-candidate workflow additionally runs `tools/check_http_preview.py`. It starts a local loopback HTTP server for the generated website and one for the unpacked 2.2.2 overlay. It checks successful HTTP responses and expected content types for the homepage, all 13 online indexed guides, styling and JavaScript; then checks the embedded installation/configuration help, six bundled Core plugin HTML guides, plugin-local reCAPTCHA configuration help, modern guide index, ten modern guides and their assets.

**Verified CI for commit `53359dd`:** [dual output build #41963935889](https://github.com/hostellerie/documentation/actions/runs/41963935889) and [installation docs #41963938676](https://github.com/hostellerie/documentation/actions/runs/41963938676), both successful.

**Boundary:** these are static HTTP requests, not browser rendering checks, administration UI clicks, PHP execution or an upgrade/restore rehearsal. Do not infer actual application integration from this result.

## Final review handoff — one upstream PR

The **single consolidated contributor branch** is `hostellerie/documentation:prototype/wiki-unified-222`. Upstream draft PR #4 was closed without merging after its changes were integrated. The remaining fork draft PR #1 is internal to the contributor fork, not a second upstream publication.

| Gate | Current status | Required evidence before declaring complete |
| --- | --- | --- |
| Site and offline ZIP generation | **PASS (CI)** | Dual-output workflow artifacts |
| Historical Core/plugin help preserved | **PASS (CI)** | Archive diff, anchor and content hashes |
| ZIP extraction and rollback | **PASS (disposable filesystem)** | Extracted-overlay workflow check |
| Search, navigation and static HTTP reachability | **PASS (CI)** | Delivery-readiness and HTTP smoke checks |
| Editorial and technical review of all 13 guides | **PARTIAL** | `EDITORIAL-PROVENANCE-REVIEW-222.md` plus maintainer sign-off |
| Wiki reuse license/author credits | **UNRESOLVED** | Verified Wiki notice, histories, or replacement with noncopied original text |
| Latest ZIP integration in running Geeklog 2.2.2 | **NOT VERIFIED** | Admin help clicks, config/plugins and rollback recorded in staging |
| Official Pages publication and browser check | **NOT DONE for this branch** | Maintainer merge then manual publish and visual review |

**Release decision: NO-GO for calling the complete documentation officially released.** This does not block presenting a consolidated **draft PR** for maintainer review, provided its body openly records those outstanding gates. If the user's priority is a single final, ready-to-merge PR, satisfy the unresolved gates first rather than claiming completeness.

## Scope boundaries

- 387 individual configuration help anchors and 449 historical unique configuration IDs are structurally present on the **online** Markdown configuration page. This does **not** mean full content parity.
- The **embedded** `public_html/docs/english/config.html` is deliberately preserved byte-identical to the tagged Core 2.2.2 source. Its tables, defaults, and context-sensitive help must not be silently replaced with the condensed online reference.
- The retained legacy HTML is a **temporary compatibility asset**, not a second actively edited source of documentation.
- Historical Wiki content is selectively modernized. The prototype does not purport to have migrated the whole Wiki or all release versions.
- The Git tag docs have been checked against the pinned Core tree. The official historical `geeklog-2.2.2.tar.gz` distribution was independently audited in `planning/OFFICIAL-ARCHIVE-VALIDATION.md`; this audit is not certification of the generated preview ZIP as an official release.
- No branch proliferation: continue improvements on `prototype/wiki-unified-222` until its single consolidated upstream PR is ready.

## Editorial, technical sources and attribution gate

Review the [guide-by-guide editorial/provenance register](EDITORIAL-PROVENANCE-REVIEW-222.md) before requesting final upstream approval. The 13 guides have different validation maturity: several API function signatures and Core admin checks are verified against the tagged `v2.2.2` source, but some recovered Wiki topics are historical drafts and do not yet establish runtime behavior.

**The archived Geeklog Wiki's site-specific content license, original contributor credits and edit histories have not been verified.** Do not assume the Geeklog source-code GPL licenses all Wiki articles or pictures. Reuse no unverified historical wording, code examples or images; write new release-scoped prose grounded in tagged Core code, and credit confirmed contributors only when provenance is established. Ask maintainers to confirm rights/attribution requirements before publishing Wiki-derived material officially.

The plugin API guide contains a corrected version-specific distinction: deprecated `PLG_install()` calls `plugin_install_*`, while `PLG_getParams()` discovers `plugin_autoinstall_*` through plugin `autoinstall.php`. Avoid merging older Wiki examples that conflate these pathways.

## Go/no-go

- **Online:** build/test succeeds, 13 searchable guides available, documentation links and layout verified, maintainer-approved merge and manual Pages publication.
- **Embedded:** built ZIP passes integrity checker, offline staging installation and admin help tests are recorded, release scope and rollback documented.
- **Do not claim final release** on only structural anchor counts or a green build.
