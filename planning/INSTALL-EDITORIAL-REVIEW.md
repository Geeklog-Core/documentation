# Installation documentation editorial review

Review date: 2026-10-29. Status: **draft suitable for maintainer feedback, not publication approval**.

## Reviewed against source

- The source `Geeklog-Core/geeklog/public_html/docs/english/install.html` contains sections for glossary, prerequisites, installation, upgrade, migration and troubleshooting. The draft follows those sections and preserves their nine legacy anchor identifiers.
- Historical minimums are confirmed in installer `Common.php` for the 2.2.2 source, and marked as historical rather than modern deployment advice.
- The source mentions removing `admin/install` after completion; the draft retains that instruction.
- Outdated recommendations about open filesystem permissions, dangerous database resets and legacy commands have been replaced by cautious diagnostic guidance.
- The preview has a local stylesheet, navigable index and support placeholders, plus a distinct text-only preview mark.

## Blocking checks before publication

1. Test new installs, upgrades and migration workflows in a clean staging installation, including database/driver variations.
2. Confirm supported PHP/database versions in an actual release package; especially avoid attributing 2.2.3 support to the still-2.2.2 source constants.
3. Independently review all database charset/collation examples and language variants from the original source.
4. Audit plugin-specific upgrade behavior and custom themes before stating a comprehensive upgrade procedure.
5. Replace the two placeholder pages and preview mark with approved distributed assets and content.
6. Verify external URLs and a complete offline Geeklog distribution.
7. Compare migration text against the project's licensing policy and obtain Tom's editorial approval.

The tests passing in this branch show **preview mechanics**, not the above release compatibility gates.

## PR scope proposed

Open a **draft** PR based on `docs/installation-migration` to discuss wording, anchors and preview tests independently from foundation PR #1. Do not merge until the underlying foundation integration and release-specific validation are complete.
