# Geeklog documentation — online-first delivery plan

**Decision (2026-11-06): The official public documentation website is P0.**
The versioned embedded documentation is P1 for the upcoming Geeklog **2.2.3** integration. This decision supersedes earlier proposals to block online publication until all 387 configuration descriptions achieve complete editorial parity.

## P0 — publish useful reviewed documentation online

Target: https://geeklog-core.github.io/documentation/ from `Geeklog-Core/documentation:main`.

- Prepare **one** contributor PR from `hostellerie/documentation:docs/published-site-labels` into upstream `main`, after checking the exact diff and branch CI. No need to create another feature branch.
- Prioritize site navigation, the 13-guide search index, installation, administration, plugins, development, and the fuller Geeklog 2.2.2 configuration reference.
- The online configuration page may publish as a **version-scoped historical reference** even while targeted editorial review remains incomplete (currently 66/387 descriptions). Clearly display its status and link to the official original for unreviewed behavior. Preserve 449 anchors, 387 documented defaults and existing explicit caveats.
- Do not imply that online publication replaces the help bundled with Geeklog, proves operational security, or certifies compatibility with 2.2.3.
- CI gates for online publication: output generation, internal link/anchor coverage, search index/navigation, HTML/CSS assets, and accurate source/version labels. Keep all existing compatibility tests; editorial blockers specific to replacing bundled `config.html` are **not** blockers for an appropriately labeled online publication.
- After Tom/maintainer review and merge, the upstream maintainer must manually trigger **Publish Geeklog documentation (maintainer opt-in)** on `main`, then verify the official homepage, search and `configuration.html#desc_site_url` live.
- Triage unreviewed content by risk: mark a section historical or requiring verification rather than stating that every option is fully certified.

## P1 — prepare offline and contextual help for Geeklog 2.2.3

- Derive the eventual offline HTML from the same maintained Markdown, but **pin a separate 2.2.3 source/release baseline** when officially available. Never silently reuse a 2.2.2-compatible ZIP as a certified 2.2.3 distribution.
- Inventory 2.2.3 configuration keys, help URLs/anchors, plugin paths, templates, assets and installer/release requirements and compare against 2.2.2.
- Test context-sensitive links from a real Geeklog 2.2.3 administrator interface, not just static HTML. Exercise least-privilege roles and representative plugin-specific help.
- Require exact legacy-path compatibility (or an agreed upgrade/redirect policy), provenance/licensing review, generated package verification, backups/rollback and documented staging results.
- Keep the original 2.2.2 embedded `config.html` untouched until these gates pass and a Core maintainer accepts the replacement in the relevant Geeklog release workflow.

## Publication and ownership

This repository's fork CI does **not** deploy to the official site. Only an upstream merge and maintainer-controlled Pages workflow update `geeklog-core.github.io/documentation`.

**Next action:** review the accumulated PR diff and propose a concise online-first publication PR to Tom. Continue the remaining semantic configuration work incrementally after the public site is updated, while tracking 2.2.3 embedding as its own release gate.
