# Geeklog Documentation

Official documentation for [Geeklog CMS](https://github.com/Geeklog-Core/geeklog).

This repository will serve as the single source of truth for Geeklog documentation, maintained collaboratively in English using Markdown.

## Project Goals

- Consolidate and update the existing documentation from `public_html/docs/english`.
- Selectively recover useful information from the historical Geeklog MediaWiki.
- Maintain documentation through GitHub forks and pull requests.
- Support documentation versioning for Geeklog releases.
- Eventually generate both an online documentation website and HTML documentation distributed with Geeklog.

## Backward Compatibility

Geeklog Core and plugins use documentation links and anchors for configuration help.

Existing URLs and anchors must remain functional when migrating the documentation.

## Contributing

Contributions will be welcome through GitHub pull requests once the initial documentation structure and guidelines are established.

## Project Status

Initial setup. Documentation migration and publishing workflows are under development.


## Initial migration pilot

The [initial documentation branch](https://github.com/hostellerie/documentation/tree/feature/initial-documentation) contains three limited Markdown examples in `docs/`, a minimal HTML builder, a link/anchor test, and a GitHub Actions workflow.

To preview the generated pages:

```sh
python -m pip install -r requirements-docs.txt
python tools/check_docs.py
```

The prototype writes `build/english/index.html`, `install.html`, and `config.html`. It checks that `config.html#desc_site_url` and `config.html#desc_site_name` survive conversion. **This is not a full installation manual or configuration reference. Do not ship the generated files with Geeklog yet.** Full link/anchor inventory and plugin coverage are pending. Only reviewed, trusted Markdown must be compiled because raw HTML is permitted.

See `planning/` for inventory, architecture and compatibility requirements. The publishing technology and distribution workflow are not yet approved.
