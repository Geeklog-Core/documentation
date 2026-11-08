# Syndication, RSS and autotags

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

## Detailed tutorial: create an RSS feed

**Source-backed in Geeklog 2.2.2:** the [Syndication administration handler](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/syndication.php) is located at `admin/syndication.php` and checks `syndication.edit`. Its editor contains a title, description, filename, format, content limit, language and enabled state. It initializes new Geeklog feeds with `RSS-2.0` as a format value; supported choices can vary.

**Scenario:** expose public news updates through a test feed.

1. Use an authorized test administrator with `syndication.edit` on a disposable Geeklog 2.2.2 installation.
2. Open Content Syndication administration (`admin/syndication.php`). Record existing feed names and filenames to avoid collisions.
3. Select the action to create a feed. If the interface asks for its type, choose the Core/Geeklog article feed rather than an unrelated plugin feed.
4. Enter **Community updates** as title and **Latest public articles from our site** as description.
5. Select RSS 2.0 **if it appears in the format list**. Choose a unique filename such as `training-updates.rss`; the handler validates or normalizes supported file extensions.
6. Choose a topic/feed scope appropriate for **public** content, and select a small entry limit. Enable the feed.
7. Save with the administration form. The handler requires a valid CSRF token for saving.
8. Find the actual feed URL on that installation and open it in a feed reader or safe browser inspector. Confirm the content is correctly formatted and that no private articles appear.
9. Publish a disposable public story, let the feed's normal update process run, then recheck the feed. **Do not assume immediate regeneration**; configuration and update scheduling can affect timing.
10. Remove the test feed or restore the previous configuration after the exercise.

**Common problems:** duplicate feed filename, blank title or description, disabled backend functionality, feed update delay, and items excluded by visibility or topic scope.

## Detailed tutorial: insert an autotag safely

The [Geeklog plugin dispatcher](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/system/lib-plugins.php) contains `PLG_replaceTags()` and documents an example of historical autotag syntax: `[story:20040101093000103 here]`. That identifier is an example, **not a guaranteed story on your site**. Available tag names and parameters depend on the installed Core and plugins.

1. Select an actual article or Static Page created on a disposable test site and record its identifier.
2. Find the installed Core/plugin's documented autotag name and format. Do not assume all historical Wiki tag names are supported.
3. In a test article or Static Page, insert a properly formed autotag using that **existing** target identifier.
4. Preview the page, then save. Check whether the tag becomes a link or embedded content as described by the selected plugin.
5. View the resulting page as an anonymous visitor and a registered member. A tag must not disclose content they cannot otherwise access.
6. If the literal tag remains visible, verify tag spelling, plugin activation, applicable configuration and target permissions before trying alternative syntax.
7. Remove the test content when finished.

**Do not enable PHP execution in Static Pages** to make an autotag expand. These are separate mechanisms.

## Follow an existing feed as a reader

1. Find a feed link published by the site. Do not guess filenames or copy old Wiki feed URLs.
2. Open it using a feed reader and subscribe to the URL actually provided.
3. Compare the latest visible entries with articles that can be read without an administrator account.
4. If an expected item is missing, check its publication state, topic and feed update interval before assuming the feed is broken.
