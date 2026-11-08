# Geeklog release documentation workflow — proposed maintainer process

**Priority P0. Status: proposal for Core maintainer review, not an approved release procedure.**

## Goal

Maintain **one Markdown source** for version-scoped official online documentation and the HTML/contextual help bundled with a Geeklog release. Publishing a website must not automatically imply that its files are safe to ship inside the CMS.

## Proposed release sequence

1. **Open a release documentation issue:** name the target Geeklog version, commit/tag baseline, documentation owner/reviewer, and required deliverables. Link the Core release notes, configuration and plugin changes.
2. **Inventory release differences:** compare the prior and target release for configuration keys/defaults/help anchors, installer and upgrade steps, theme/template APIs, plugin changes, user-facing behavior, security guidance and supported dependencies.
3. **Update Markdown:** prepare version-scoped guides and examples. Preserve old version references where needed rather than silently rewriting historical behavior.
4. **Review and validate:** run the documentation build and editorial/link/anchor checks; peer-review technical claims against the target Core tag. Execute high-risk install, upgrade, restore, permissions and plugin scenarios in staging. Record evidence and incomplete work honestly.
5. **Publish the website:** merge reviewed changes into the official repository; a maintainer triggers the GitHub Pages publishing workflow and checks public navigation, search, deep links and mobile presentation.
6. **Prepare embedded help separately:** generate the target-version HTML and assets from the same maintained content; compare every expected bundled path and configuration-help anchor, test help links in a real target-version admin interface and plugins, and verify rollback.
7. **Integrate into the Geeklog release:** require Core maintainer sign-off before replacing shipped legacy docs. Include the vetted generated artifacts in the matching Core release process, with ownership, acceptance evidence and rollback instructions documented.
8. **After release:** verify public docs and embedded help against the released tag, record defects and backport version-specific corrections.

## Acceptance checklist

- [ ] Target source tag and documentation version recorded.
- [ ] Documentation changes reviewed for technical accuracy and security.
- [ ] Markdown-to-site build, site search, links and editorial lint pass.
- [ ] Configuration anchors and default values reconciled with the exact target release.
- [ ] Staging installation, upgrade, rollback and representative plugin workflows evidenced.
- [ ] Embedded HTML paths, assets and contextual links verified in the target CMS.
- [ ] Maintainer approval for both online publishing and embedded release packaging.
- [ ] Published site smoke-tested and embedded artifact included only after sign-off.

## Roles to agree with Tom and Core maintainers

Define a documentation change owner, Core technical reviewer, staging/test owner and the maintainer responsible for the website deployment and release packaging. One person may fill multiple roles, but approval responsibility should be explicit.

## Current backlog

- **P0:** Agree on this release documentation procedure and the necessary ownership/review gates.
- **P1:** Verify historical CTL and other technical examples in Geeklog 2.2.2; repeat against a pinned 2.2.3 baseline when available.
- **P1:** Preserve a read-only archive of the historical Wiki with provenance, and verify the planned `wiki.geeklog.net` redirect (including HTTPS, root and representative deep links). Do not delete the archive or claim redirects work without HTTP tests.
- **P1:** Continue isolated validation of embedded documentation, configuration anchors, plugin help links, archive paths, and rollback, separately for 2.2.2 and 2.2.3.

## Boundaries

Existing 2.2.2 documentation overlay tests do not certify an official 2.2.3 embedded package. Historical Wiki references are leads, not automatically accurate or licensed for wholesale republication.
