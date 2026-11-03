# Geeklog 2.2.2 official release archive comparison

Status: **comparison procedure implemented; original downloadable release archive not yet obtained and compared** (2026-11-03).

## Evidence and boundaries

The official [Geeklog 2.2.2 download listing](https://www.geeklog.net/downloads/index.php/file_geeklog-2.2.2) publishes:

- Filename: `geeklog-2.2.2.tar.gz`
- Size: **16,978,448 bytes**
- MD5: `962cc6e6ed1ce13f65066e47859511d8`

This older MD5 value is provided by the project as an **archive identity check**, not a cryptographic signature or guarantee of authenticity. Source/tag identity checks in GitHub Actions are separate from archive identity. A complete original packaged release comparison must be performed before declaring that the original release files match pinned source.

A direct archive download from this execution environment was unsuccessful. No claim of real-archive byte comparison is made.

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
  --recaptcha-docs ../geeklog-2.2.2-source/public_html/admin/plugins/recaptcha/docs
```

The script does **not extract** the tarball. It checks the posted size and MD5, prints the calculated SHA-256, then compares SHA-256 of every packaged Core documentation and plugin-local reCAPTCHA documentation file against `v2.2.2` source. It reports **missing, extra, and changed files separately** and exits non-zero on any difference.

If the official archive genuinely differs from source, preserve and investigate those differences before updating the generator's provenance policy. Do **not** update pinned hashes or add exceptions merely to make the test green.

## Regression testing

```bash
python -m unittest discover -s tools -p 'test_official_release_docs.py'
```

These unit tests create **synthetic tarballs**, confirming that matching files pass, modified/missing files fail, and an arbitrary archive fails the official size/MD5 gate. **They are not evidence that the real 2.2.2 release archive passes.**

## Follow-up and release gates

- [x] Prepare a read-only archive comparison tool and isolated regression tests.
- [ ] Obtain original 2.2.2 distribution tarball from the official download source.
- [ ] Record posted size/MD5 verification and local computed SHA-256.
- [ ] Report every difference in Core and reCAPTCHA documents against the pinned source.
- [ ] Cross-check the generated ZIP overlay against the **actual packaged** documentation tree.
- [ ] Keep installer/upgrade/migration runtime validation and editorial approval as separate work.
