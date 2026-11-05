# Geeklog 2.2.2 official release archive comparison

Status: **the user supplied the official release archive and the full documentation tree was compared against the official `v2.2.2` Git tree** (2026-11-03).

## Evidence and boundaries

The official [Geeklog 2.2.2 download listing](https://www.geeklog.net/downloads/index.php/file_geeklog-2.2.2) publishes:

- Filename: `geeklog-2.2.2.tar.gz`
- Size: **16,978,448 bytes**
- MD5: `962cc6e6ed1ce13f65066e47859511d8`

This older MD5 value is provided by the project as an **archive identity check**, not a cryptographic signature or guarantee of authenticity. Source/tag identity checks in GitHub Actions are separate from archive identity. A complete original packaged release comparison must be performed before declaring that the original release files match pinned source.

The user uploaded `geeklog-2.2.2.tar.gz` on 2026-11-03. The archive size and published MD5 **match**, and its computed SHA-256 is `d12991f78225289d2bac297bff1a7e9be55f04a9e0aa097bb379e41d7fb138a8`.

Using the official GitHub `v2.2.2` **recursive tree's Git blob object IDs**, every documentation member in the archive was compared as a raw Git blob and again after `CRLF → LF` normalization. The comparison covers **41 Core documentation files and 5 reCAPTCHA documentation files** (46 files). Result: **8 byte-identical, 38 CRLF-only differences, 0 substantive content differences, 0 missing and 0 extra files.** No other normalization was performed. This establishes exact documentation-content equivalence modulo the distribution's CRLF line endings; it does **not** establish byte-for-byte archive/source equality, complete archive code equivalence, or a valid official cryptographic signature.

The comparison was independently executed against the provided tarball, not merely inferred from successful historical CI. A reproducible checkout-based verification script is included below.

## Run the comparison on a workstation

Obtain `geeklog-2.2.2.tar.gz` from the official Geeklog download listing above, and place it outside the documentation checkout. Then use a clean `v2.2.2` checkout of the Core repository and the documentation checkout containing the checker:

```bash
git clone --depth 1 --branch v2.2.2 https://github.com/Geeklog-Core/geeklog.git geeklog-2.2.2-source
git clone https://github.com/Geeklog-Core/documentation.git geeklog-docs
# Until the tools are merged, run from the fork's docs/installation-release-audit-222 branch.
cd geeklog-docs
git remote add contributor https://github.com/hostellerie/documentation.git
git fetch contributor docs/installation-release-audit-222
git checkout -b archive-verification FETCH_HEAD

python tools/check_official_release_docs.py ~/Downloads/geeklog-2.2.2.tar.gz \
  --core-docs ../geeklog-2.2.2-source/public_html/docs \
  --recaptcha-docs ../geeklog-2.2.2-source/public_html/admin/plugins/recaptcha/docs \\
  --allow-crlf-normalization
```

The script does **not extract** the tarball. It checks the posted size and MD5, prints the calculated SHA-256, then compares SHA-256 of every packaged Core documentation and plugin-local reCAPTCHA documentation file against `v2.2.2` source. It reports **missing, extra, content-different, and CRLF-only files separately**. By default, even line-ending-only changes fail the strict comparison; `--allow-crlf-normalization` permits only CRLF/LF differences, never substantive mismatches.

If the official archive genuinely differs from source, preserve and investigate those differences before updating the generator's provenance policy. Do **not** update pinned hashes or add exceptions merely to make the test green.

## Regression testing

```bash
python -m unittest discover -s tools -p 'test_official_release_docs.py'
```

These unit tests create **synthetic tarballs**, confirming that matching files pass, modified/missing files fail, CRLF-only differences require explicit opt-in, and an arbitrary archive fails the official size/MD5 gate. The **real archive comparison reported above is separate evidence**. The updated checker/CI tests must still run in GitHub Actions on the current branch.

## Follow-up and release gates

- [x] Prepare a read-only archive comparison tool and isolated regression tests.
- [x] Receive original 2.2.2 distribution tarball from user (published size and MD5 verified).
- [x] Record posted size/MD5 verification and local computed SHA-256.
- [x] Compare complete Core and reCAPTCHA documentation against Git tag's blob hashes: 8 identical + 38 CRLF-only, no missing or substantive differences.
- [x] Compared final generated ZIP overlay from GitHub Actions run 41564854616 to the **real official packaged** documentation tree; exactly one content-different file (generated install.html), 37 CRLF/LF-only changes, eight byte-identical files, no missing or extra files.
- [ ] Keep installer/upgrade/migration runtime validation and editorial approval as separate work.

## Real generated ZIP versus real official release tarball — 2026-11-03

The user-supplied original archive `geeklog-2.2.2.tar.gz` was directly compared, in a separate local analysis, with the **actual GitHub Actions artifact ZIP** produced by the installation-audit branch's successful [run 41564854616](https://github.com/hostellerie/documentation/actions/runs/41564854616). The artifact contained a nested `geeklog-2.2.2-docs-preview.zip`, which was opened without extracting or executing Geeklog.

| Comparison against the real official tarball | Number of files |
| --- | ---: |
| Documentation paths in original tarball | 46 |
| Documentation paths in generated ZIP | 46 |
| Missing or extra paths | 0 |
| Exact byte matches | 8 |
| Only CRLF/LF differences | 37 |
| Actual content differences | **1** |

The **only content-different file** is `public_html/docs/english/install.html`, which is intentionally generated from `docs/installation/README.md`. All **45 other** Core and reCAPTCHA documentation files are preserved byte-for-byte after CRLF→LF normalization; this includes all plugin documentation and original HTML help paths. The generated install page was also checked not to contain literal `\\n` escape text.

This **closes the packaged-documentation versus generated-ZIP overlay comparison gate**. It does **not** validate that installation/upgrade/migration procedures succeed, that the generated documentation is an editorially approved release artifact, or that all obsolete language in the historical sources has been replaced.

The comparison artifact was generated in [CI run 41564854616](https://github.com/hostellerie/documentation/actions/runs/41564854616), which passed all existing dual-output tests and the updated **five** synthetic archive-checker unit tests. An earlier run 41564762417 failed because a new synthetic test used literal backslash escapes in its own fixture; it was corrected before the passing run.
