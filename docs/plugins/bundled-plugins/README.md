# Bundled plugins reference

> **Geeklog 2.2.2 bundled-plugin inventory.** The named plugins and historical help files are grounded in the pinned release documentation; this is not a complete modernization of every plugin interface or feature.

## Reference inventory

| Bundled plugin | Primary purpose or next documentation step |
| --- | --- |
| Calendar | Review event publishing, calendars, access and actual admin screens |
| Links | Review directories, categories, submissions and link moderation |
| Polls | Review creating polls, voting permissions and results |
| Spam-X | Review filtering, moderation and configuration of spam protection |
| Static Pages | Use the [modern Static Pages guide](../static-pages/index.html), including rights and PHP execution precautions |
| XMLSitemap | Review site-map generation, file permissions and update behavior |
| reCAPTCHA | Review installation, configuration and help links in its separate admin plugin documentation path |

These names refer to plugins included with the 2.2.2 release. The exact plugin versions and supported options should be confirmed from each plugin's tagged metadata rather than guessed from a historical article.

## Where historical help lives

Most original Core plugin help documents are under `public_html/docs/english/` in Geeklog 2.2.2. The reCAPTCHA help document is located separately under `public_html/admin/plugins/recaptcha/docs/english/config.html`. Their paths are important for context-sensitive administration links.

## Plugin-specific documentation checklist

A modern guide for each bundled plugin should include: purpose, required permissions, setup, typical task workflow, configuration options, public output, upgrade notes, troubleshooting and source/version references. Test at least one allowed and one denied operation in a disposable installation before claiming complete behavior coverage.

## Next steps

Write separate detailed guides for Calendar, Links, Polls, Spam-X, XMLSitemap and reCAPTCHA after comparing their tagged source with their bundled help. Do not assume the archived Wiki material is accurate for the current version. See [Plugin installation and management](../plugin-installation-management/index.html) for general lifecycle guidance.
