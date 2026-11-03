# Post-launch documentation migration plan

Status: planning checklist following publication of https://geeklog-core.github.io/documentation/ (2026-11-03).

## What is live, and what is not

The official repository publishes a navigable Markdown-based website with installation, configuration, and administration pages. The **site is live**, but its content is intentionally incomplete and should not yet supersede release-specific bundled documentation.

The GitHub Actions 2.2.2 archive generator copies the pinned legacy documentation set, overlaying only `public_html/docs/english/install.html` with generated HTML; original configuration and plugin help remain unchanged. Docker testing confirmed representative install anchors, the original configuration help anchor, all seven plugin docs and administration help interactions. This is not complete runtime or release-package qualification.

## Proposed sequence (small PRs, independent review)

| Priority | Source/subject | Work needed | Acceptance gate |
| --- | --- | --- | --- |
| P0 | Site landing, navigation and contributor information | Remove confusing pre-launch language; clearly identify incomplete reference pages | Generated website and link checks pass; reviewer confirms scope |
| P1 | Installation and upgrading (`english/install.html`) | Finish editorial review and validate PHP/database requirements against supported versions; cover upgrade/migrate cases | Source review + all historical anchors + local links + actual release packaging and staging tests |
| P1 | Configuration (`english/config.html`) | Migrate all supported configuration options, not just two demonstration entries | Every Core help target and option audited against release source; no broken fragments |
| P2 | Bundled plugin help | Migrate Calendar, Links, Polls, Spam-X, Static Pages, XMLSitemap and separately located reCAPTCHA | Exact paths/anchors preserved, including plugin-specific admin help links |
| P2 | Administration, themes and other English reference | Inventory and verify `support.html`, `theme.html`, `themevars.html`, `trackback.html`, `changes.html` and `index.html` | Review current behavior, preserve cross-links and stable historical paths |
| P3 | Japanese source and historical MediaWiki | Define retention, archive and redirect policy; selectively migrate supported content | Provenance/licensing review, redirect mapping and maintainer sign-off |
| P3 | Release integration | Define versioned documentation artifacts, install packaging and release automation | Compare exact tagged release archive, reproducible build and maintainer-approved Core integration |

## Compatibility invariants

1. Do not remove or change `public_html/docs/english/*.html` or `admin/plugins/recaptcha/docs/english/config.html` paths until a proven compatible output replaces them.
2. Preserve named anchors and fragment resolution for administration help links; review both Core and all seven bundled plugins.
3. Preserve historical assets, relative URLs, Japanese source files and unchanged legacy content until explicitly migrated.
4. Keep official online publication distinct from the **experimental 2.2.2 embedded HTML ZIP**; never label it an official release artifact.
5. Version documentation output with its target Geeklog release rather than assuming `master` is compatible with 2.2.2.

## Immediate follow-up

After the post-launch wording PR is merged, begin a focused installation technical review for the supported Geeklog release; record the remaining mismatches in the existing `planning/INSTALL-*.md` audits. Do **not** merge incomplete configuration samples into production embedded help.
