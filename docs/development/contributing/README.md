# Contributing to Geeklog

## Choose the repository

Geeklog Core, plugin projects and the documentation repository have distinct code owners and release cycles. Before filing a change, check the target repository's README, open issues and contribution instructions. Link a reproducible bug report to the affected release or plugin version.

## Prepare a focused contribution

1. Identify the user problem and minimum change that solves it.
2. Create or reference a clear issue where the maintainers ask for one.
3. Work in a fork/branch with a focused diff.
4. Add regression tests and documentation appropriate to the change.
5. Check permissions, secure input/output handling and backwards compatibility for code changes.
6. Explain the change, reproduction and verification steps in the PR.
7. Respond to review, keep scope manageable and do not merge without the repository's approval.

## Documentation contributions

The [official documentation repository](https://github.com/Geeklog-Core/documentation) maintains Markdown source and builds an online site. A documentation PR should specify its Geeklog release scope, affected guide, historical source basis and verification details. Verify local links, anchors and generated output before opening the PR.

Do not import text, code examples or images from the old Geeklog Wiki without checking author attribution, applicable license and technical accuracy. Prefer new explanations grounded in tagged release source.

## Review checklist

| Area | Question |
| --- | --- |
| Compatibility | Is the target version explicit? |
| Reproduction | Can a reviewer reproduce the issue without private data? |
| Tests | What was actually executed versus merely planned? |
| Security | Are permission checks and untrusted data handled correctly? |
| Documentation | Do links, terms and examples match the target release? |
| Provenance | Are third-party contributions and reuse rights clear? |
