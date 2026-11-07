# Phase 2 PR handoff — practical user tutorials

**Base:** `Geeklog-Core/documentation:main`  
**Head:** `hostellerie/documentation:docs/phase2-user-guides-222`  
**Scope:** Geeklog **2.2.2** documentation and static content validation only.

## Proposed PR title

`docs: expand user documentation with practical 2.2.2 tutorials`

## Proposed PR description

### Summary

Expand the existing Geeklog documentation into task-oriented, illustrated-by-examples **written tutorials** without changing the public site's six-section/25-guide information architecture. Seven existing guides now cover beginner learning, articles and topics, blocks and menus, comments/moderation, RSS and autotags, plugin installation/maintenance, and Static Pages.

### Highlights

- Beginner four-lesson mini-course: account roles, publishing, blocks/pages and moderation.
- Concrete walkthroughs for story contribution, moderation, topic hierarchy, publication dates, block types and missing content.
- RSS-feed configuration, subscriber checking and plugin-provided autotag examples.
- Plugin lifecycle, rights, data/backup expectations and cautious upgrade planning.
- Static Pages About-page creation and cloning, with clear PHP execution privilege warnings.
- Source-backed technical details verified against immutable Geeklog Core **v2.2.2** files.
- Two documentation-regression scripts validate generated HTML coverage, source anchors and a **30-case** staging test matrix across all seven guides.

### Testing

Branch CI must pass on the final head. HTML generation and static local linking are checked. All staging/manual cases remain `NOT_RUN`. A passing CI **does not** claim that screenshots, browser behavior or production plugin upgrades were exercised.

### Explicitly out of scope

- Live audit/visual QA of the official documentation site (postponed).
- Real runtime certification of the tutorials; staging acceptance and screenshot evidence remain follow-up tasks.
- Geeklog 2.2.3 embedded-help integration.
- Full migration of the historic Wiki.

### Next step

Review the new tutorials for clarity and accurate boundaries, then merge if acceptable. Publish the official Pages workflow from upstream `main` after merge.

## Supporting files

- `planning/PHASE2-USER-GUIDES-ACCEPTANCE.md`
- `planning/PHASE2-STAGING-SCENARIOS.csv`
- `tools/check_p0_user_guides.py`
- `tools/check_practical_tutorials.py`
