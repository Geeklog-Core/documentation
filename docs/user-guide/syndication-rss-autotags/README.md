# Syndication, RSS and autotags

> **Geeklog 2.2.2 orientation — feature-level verification pending.** Feeds and autotags depend on configuration, content visibility and plugin support; the exact URLs and available tag names must be checked on the installed release.

## Publishing and following feeds

Syndication lets readers follow updates through a supported feed reader. An administrator should identify the feeds actually exposed by the installed site, verify the intended content scope, and ensure feed links do not disclose restricted content.

1. Find a feed link that your site actually publishes.
2. Open it with a suitable reader or inspect its MIME/content type safely.
3. Compare visible feed entries with public article visibility.
4. Recheck the feed after publishing, changing topics or upgrading feed-related plugins.

Do not assume an older Wiki feed URL or a trackback integration still works in Geeklog 2.2.2.

## Autotags in content

An **autotag** is a configured shortcut that Geeklog or a plugin can interpret while rendering content. Available tags and their expansion rules differ by plugin, version and enabled features. Confirm the supported syntax in the actual editor and plugin documentation before publishing.

When reviewing autotag behavior:

- Test a documented tag on a disposable page or article.
- Verify how it renders for anonymous and registered readers.
- Confirm the target content's permissions; an autotag must not bypass access restrictions.
- Check link targets and escaping before copying user-supplied input into a tag.
- Prefer a documented plugin feature over injecting arbitrary PHP into Static Pages.

## Problems and security

Missing feed entries can reflect publication status, visibility or caching. Unexpanded tags may indicate a disabled plugin, unsupported syntax or an unavailable target. Do not enable high-risk page execution or relax security controls simply to make historical samples render.

Related references: [Configuration](../../index.html) via the documentation homepage, [Static Pages](../../plugins/static-pages/index.html), and [Security and permissions](../../development/security-and-permissions/index.html).

## Remaining research

Inventory supported feeds and built-in/plugin autotags in tagged 2.2.2 source; test real output formats, caching and access filtering. Historical Wiki pages are candidate references only, not validation of current endpoints.
