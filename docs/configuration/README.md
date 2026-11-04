# Geeklog configuration — migration preview

> **Prototype only.** This is a partial, non-authoritative guide. The embedded distribution deliberately retains the complete historical `english/config.html` until its anchors and options have been migrated and verified.

## Configuration panel

Geeklog provides a Configuration administration panel for most settings. Installation and database bootstrap values can also reside in `siteconfig.php` and `db-config.php`.

## Context-sensitive help

Core configuration help links use `config.html#desc_<option>`. These examples illustrate the intended Markdown source format.

<a id="desc_site_url" name="desc_site_url"></a>

### Site URL

The `site_url` option represents the base website URL. Check the bundled 2.2.2 reference before changing it.

<a id="desc_site_name" name="desc_site_name"></a>

### Site name

The `site_name` option represents the displayed website name.

## Complete reference

Use the original `docs/english/config.html` distributed with Geeklog 2.2.2. The online samples are **not** a substitute for the full configuration documentation.


## Site settings — Geeklog 2.2.2

The following descriptions are adapted and condensed from the [Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Defaults shown in that reference may not equal the actual values on an upgraded site.

<a id="desc_site_admin_url" name="desc_site_admin_url"></a>

### `site_admin_url`

Base URL of the administration area, without a trailing slash. If the admin directory has a different public name or path, configure the corresponding URL. This must be a **web URL**, not a filesystem directory.

<a id="desc_site_slogan" name="desc_site_slogan"></a>

### `site_slogan`

The site's slogan; Geeklog adds it to the HTML page title in the configuration described for 2.2.2.

<a id="desc_path_site_logo" name="desc_path_site_logo"></a>

### `path_site_logo`

Absolute path to the image file used for publisher structured data, regardless of the selected theme unless a theme overrides it. The bundled reference gives a theme image path as an example.

<a id="desc_site_disabled_msg" name="desc_site_disabled_msg"></a>

### `site_disabled_msg`

Message displayed when a site is disabled. The bundled guide also documents redirect behavior when the setting begins with `http:`. The actual **site-disable switch belongs in `siteconfig.php`**, rather than this message setting. Verify redirect behavior before using it.

<a id="desc_owner_name" name="desc_owner_name"></a>

### `owner_name`

Owner name displayed in the copyright notice, if specified; otherwise Geeklog uses the site name.

<a id="desc_copyrightyear" name="desc_copyrightyear"></a>

### `copyrightyear`

Optional copyright year for the site footer. When unset, the bundled documentation says the current year is used.

<a id="desc_url_rewrite" name="desc_url_rewrite"></a>

### `url_rewrite`

Enable or disable URL rewriting. Check your web server's support and the site routing options before changing this on an established site.

<a id="desc_url_routing" name="desc_url_routing"></a>

### `url_routing`

URL routing requires URL rewriting to be enabled. The option that removes `index.php` from routes can require additional web server configuration. Test old and new links before enabling it.

<a id="desc_cdn_hosted" name="desc_cdn_hosted"></a>

### `cdn_hosted`

Controls whether selected frontend libraries, including jQuery, jQuery UI and UIkit in the 2.2.2 reference, use CDN-hosted resources.

<a id="desc_meta_tags" name="desc_meta_tags"></a>

### `meta_tags`

Controls whether Geeklog outputs article and topic metadata. The reference describes disabled, enabled, and enabled with defaults limited to the homepage. When enabled, article keywords can also affect the display of related articles.

<a id="desc_meta_description" name="desc_meta_description"></a>

### `meta_description`

Default site meta description when the metadata functionality is enabled and a page-specific value is unavailable.

<a id="desc_meta_keywords" name="desc_meta_keywords"></a>

### `meta_keywords`

Default meta keywords for the site when metadata is enabled. The original reference describes their use in page metadata and related-article behavior; do not treat the presence of this setting as evidence that search engines use meta keywords for ranking.

<a id="desc_cookie_consent" name="desc_cookie_consent"></a>

### `cookie_consent`

Enables or disables the built-in cookie-consent behavior for themes supporting it. A supporting theme may use `about_cookies_link` for a learn-more destination. This setting alone does not establish legal compliance.

<a id="desc_about_cookies_link" name="desc_about_cookies_link"></a>

### `about_cookies_link`

Link to the cookie information page. The reference allows external destinations or site-relative paths, such as a path beginning with `/article.php`.

<a id="desc_terms_of_use_link" name="desc_terms_of_use_link"></a>

### `terms_of_use_link`

Link to a site's terms of use. For internal pages, the reference recommends site-relative URLs rather than including the domain.

<a id="desc_privacy_policy_link" name="desc_privacy_policy_link"></a>

### `privacy_policy_link`

Link to the site's privacy policy. For internal links, use a site-relative path as described in the bundled 2.2.2 reference.

<a id="desc_ip_anonymization" name="desc_ip_anonymization"></a>

### `ip_anonymization`

The 2.2.2 reference documents `-1` as disabled, `0` as immediate, and positive numbers as delays in seconds. Its scheduled processing depends on Geeklog's cron configuration, so anonymity changes may not occur immediately. It affects supported IP data in the Geeklog database, **not web server or application log files**. Low delays can interfere with functions that rely on IP addresses.

## Mail settings — Geeklog 2.2.2

<a id="desc_site_mail" name="desc_site_mail"></a>

### `site_mail`

Administrative email address used by Geeklog.

<a id="desc_noreply_mail" name="desc_noreply_mail"></a>

### `noreply_mail`

Sender address used by system-generated messages such as registration emails. Configure it as a valid address allowed by your mail transport.

<a id="desc_mail_settings_backend" name="desc_mail_settings_backend"></a>

### `mail_settings_backend`

Select the email sending method: `smtp`, `smtps`, `sendmail` or PHP `mail` in the 2.2.2 reference. Secure SMTP support depends on compatible PHP/OpenSSL and mail server configuration.

<a id="desc_mail_settings_sendmail_path" name="desc_mail_settings_sendmail_path"></a>

### `mail_settings_sendmail_path`

Absolute filesystem path to the `sendmail` executable when the `sendmail` backend is selected.

<a id="desc_mail_settings_sendmail_args" name="desc_mail_settings_sendmail_args"></a>

### `mail_settings_sendmail_args`

Optional arguments passed to `sendmail` when that backend is selected. Only use values approved for your server.

<a id="desc_mail_settings_host" name="desc_mail_settings_host"></a>

### `mail_settings_host`

SMTP server hostname for the `smtp` and `smtps` backends.

<a id="desc_mail_settings_port" name="desc_mail_settings_port"></a>

### `mail_settings_port`

Port used to connect to the mail server. Match this setting to the server and its encryption requirements rather than relying on a default port.

<a id="desc_mail_settings_auth" name="desc_mail_settings_auth"></a>

### `mail_settings_auth`

Controls SMTP authentication: the 2.2.2 reference documents `1` when authentication is required and `0` otherwise.

<a id="desc_mail_settings_username" name="desc_mail_settings_username"></a>

### `mail_settings_username`

SMTP account name used when the selected mail backend requires authentication.

<a id="desc_mail_settings_password" name="desc_mail_settings_password"></a>

### `mail_settings_password`

SMTP account secret. Never include a real password in documentation examples, public issue reports or diagnostic logs.

<a id="desc_mail_cc_enabled" name="desc_mail_cc_enabled"></a>

### `mail_cc_enabled`

Controls whether users can send themselves a copy of an email.

<a id="desc_mail_cc_default" name="desc_mail_cc_default"></a>

### `mail_cc_default`

Controls whether the copy-to-self checkbox is selected by default.

<a id="desc_mail_charset" name="desc_mail_charset"></a>

### `mail_charset`

Character encoding of outgoing email. If empty, the configuration reference says the site's `default_charset` is used.

---

**Migration note:** These are version-scoped descriptions based on the bundled 2.2.2 reference; a working installation and original defaults should still be reviewed before calling them authoritative. The embedded `config.html` is intentionally preserved unchanged until complete migration.


## Syndication and feeds — Geeklog 2.2.2

The settings below are **defaults for newly created feeds**, not necessarily overrides of existing feed configurations. They follow the [bundled Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html#site_syndication). Geeklog also provides a *Content Syndication* administration interface.

<a id="desc_backend" name="desc_backend"></a>

### `backend`

Controls whether a feed file is generated for articles. The 2.2.2 reference documents `0` for disabled and `1` for enabled. The default in that reference is `1`.

<a id="desc_rdf_file" name="desc_rdf_file"></a>

### `rdf_file`

Filesystem path to the feed file. The bundled reference places it under the site's HTML directory, with a `/backend/geeklog.rss` suffix. The destination directory **must be inside `path_html`**. This is a server path, not a public URL.

<a id="desc_rdf_limit" name="desc_rdf_limit"></a>

### `rdf_limit`

Controls how many articles are exported. A number such as `10` limits the count; a value such as `24h` selects articles within the previous number of hours. The documented default is `10`.

<a id="desc_rdf_storytext" name="desc_rdf_storytext"></a>

### `rdf_storytext`

Determines how much article introduction text is included in a feed: `0` excludes it, `1` includes the complete introduction, and a value greater than `1` limits it to that many characters. The documented default is `0`.

<a id="desc_rdf_language" name="desc_rdf_language"></a>

### `rdf_language`

Language tag advertised by the feed. The bundled reference gives `en-gb` as the default and notes that feed language tags can differ from PHP locale strings; for example, `de-DE` versus `de_DE`.

<a id="desc_syndication_max_headlines" name="desc_syndication_max_headlines"></a>

### `syndication_max_headlines`

Maximum number of headlines **imported** into a portal block. The per-block setting can also provide a limit. The documented default `0` means import all available headlines.

<a id="desc_comment_feeds_article_tag" name="desc_comment_feeds_article_tag"></a>

### `comment_feeds_article_tag`

Format string inserted for an article referenced in a comment feed. The bundled documentation describes **four ordered string placeholders**, supplied through a formatting call: article URL, article title, article-author tag and comment-author tag. Preserve the correct placeholder count and formatting when customizing it; avoid inserting untrusted raw markup.

<a id="desc_comment_feeds_article_tag_position" name="desc_comment_feeds_article_tag_position"></a>

### `comment_feeds_article_tag_position`

Controls placement of the formatted article tag within the comment body. The 2.2.2 reference documents `start`, `end` and `none`; the default is `end`.

<a id="desc_comment_feeds_article_author_tag" name="desc_comment_feeds_article_author_tag"></a>

### `comment_feeds_article_author_tag`

Optional format string for a link to the article author's profile and name. It contributes to `comment_feeds_article_tag` when populated. The documented default is an empty string.

<a id="desc_comment_feeds_comment_author_tag" name="desc_comment_feeds_comment_author_tag"></a>

### `comment_feeds_comment_author_tag`

Optional format string for a link to the comment author's profile and name. It contributes to `comment_feeds_article_tag`; setting it to an empty string omits that tag.

**Compatibility note:** These are version-specific descriptions, not tested configuration changes. Confirm effects on a staging installation. The embedded `config.html` remains unchanged during migration.
