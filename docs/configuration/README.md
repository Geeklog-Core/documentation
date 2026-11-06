# Geeklog 2.2.2 configuration reference

> **Coverage notice:** This Markdown reference preserves historical help anchors but does not yet reproduce all details of the bundled 2.2.2 configuration guide. Use the original `docs/english/config.html` for exhaustive defaults, examples and tables. The embedded distribution keeps that file unchanged until full content parity has been reviewed.

## Configuration panel

Geeklog provides a Configuration administration panel for most settings. Installation and database bootstrap values can also reside in `siteconfig.php` and `db-config.php`.

## Context-sensitive help

Core configuration help links use `config.html#desc_<option>`. These examples illustrate the intended Markdown source format.

<a id="site" name="site"></a>
<a id="site_site" name="site_site"></a>

<a id="desc_site_url" name="desc_site_url"></a>

### Site URL

**Documented default (Geeklog 2.2.2):** `http://www.example.com`

The `site_url` option represents the base website URL. Check the bundled 2.2.2 reference before changing it.

<a id="desc_site_name" name="desc_site_name"></a>

### Site name

**Documented default (Geeklog 2.2.2):** `Geeklog Site`

The `site_name` option represents the displayed website name.

## Complete reference

Use the original `docs/english/config.html` distributed with Geeklog 2.2.2. The online samples are **not** a substitute for the full configuration documentation.


## Site settings — Geeklog 2.2.2

The following descriptions are adapted and condensed from the [Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Defaults shown in that reference may not equal the actual values on an upgraded site.

<a id="desc_site_admin_url" name="desc_site_admin_url"></a>

### `site_admin_url`


**Documented default (Geeklog 2.2.2):** `http://www.example.com/admin`
Base URL of the administration area, without a trailing slash. If the admin directory has a different public name or path, configure the corresponding URL. This must be a **web URL**, not a filesystem directory.

<a id="desc_site_slogan" name="desc_site_slogan"></a>

### `site_slogan`


**Documented default (Geeklog 2.2.2):** `Another Nifty Geeklog Site`
The site's slogan; Geeklog adds it to the HTML page title in the configuration described for 2.2.2.

<a id="desc_path_site_logo" name="desc_path_site_logo"></a>

### `path_site_logo`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Absolute path to the image file used for publisher structured data, regardless of the selected theme unless a theme overrides it. The bundled reference gives a theme image path as an example.

<a id="desc_site_disabled_msg" name="desc_site_disabled_msg"></a>

### `site_disabled_msg`


**Documented default (Geeklog 2.2.2):** `'Geeklog Site is down. Please come back soon.'`
Message displayed when a site is disabled. The bundled guide also documents redirect behavior when the setting begins with `http:`. The actual **site-disable switch belongs in `siteconfig.php`**, rather than this message setting. Verify redirect behavior before using it.

<a id="desc_owner_name" name="desc_owner_name"></a>

### `owner_name`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Owner name displayed in the copyright notice, if specified; otherwise Geeklog uses the site name.

<a id="desc_copyrightyear" name="desc_copyrightyear"></a>

### `copyrightyear`


**Documented default (Geeklog 2.2.2):** `(disabled)`
Optional copyright year for the site footer. When unset, the bundled documentation says the current year is used.

<a id="desc_url_rewrite" name="desc_url_rewrite"></a>

### `url_rewrite`


**Documented default (Geeklog 2.2.2):** `false`
Enable or disable URL rewriting. Check your web server's support and the site routing options before changing this on an established site.

<a id="desc_url_routing" name="desc_url_routing"></a>

### `url_routing`


**Documented default (Geeklog 2.2.2):** `Disabled`
URL routing requires URL rewriting to be enabled. The `Enabled (without "index.php")` setting requires compatible web-server rewriting. Review the [historical routing appendix](#url-routing), verify `PATH_INFO` support and test existing links before enabling it.

<a id="desc_cdn_hosted" name="desc_cdn_hosted"></a>

### `cdn_hosted`


**Documented default (Geeklog 2.2.2):** `false`
Controls whether selected frontend libraries, including jQuery, jQuery UI and UIkit in the 2.2.2 reference, use CDN-hosted resources.

<a id="desc_meta_tags" name="desc_meta_tags"></a>

### `meta_tags`


**Documented default (Geeklog 2.2.2):** `Disabled`
Controls whether Geeklog outputs article and topic metadata. The reference describes disabled, enabled, and enabled with defaults limited to the homepage. When enabled, article keywords can also affect the display of related articles.

<a id="desc_meta_description" name="desc_meta_description"></a>

### `meta_description`


**Documented default (Geeklog 2.2.2):** `'Geeklog, the open source content management system designed with security in mind.'`
Default site meta description when the metadata functionality is enabled and a page-specific value is unavailable.

<a id="desc_meta_keywords" name="desc_meta_keywords"></a>

### `meta_keywords`


**Documented default (Geeklog 2.2.2):** `'Geeklog, Blog, Content Management System, CMS, Open Source, Security'`
Default meta keywords for the site when metadata is enabled. The original reference describes their use in page metadata and related-article behavior; do not treat the presence of this setting as evidence that search engines use meta keywords for ranking.

<a id="desc_cookie_consent" name="desc_cookie_consent"></a>

### `cookie_consent`


**Documented default (Geeklog 2.2.2):** `Enable`
Enables or disables the built-in cookie-consent behavior for themes supporting it. A supporting theme may use `about_cookies_link` for a learn-more destination. This setting alone does not establish legal compliance.

<a id="desc_about_cookies_link" name="desc_about_cookies_link"></a>

### `about_cookies_link`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Link to the cookie information page. The reference allows external destinations or site-relative paths, such as a path beginning with `/article.php`.

<a id="desc_terms_of_use_link" name="desc_terms_of_use_link"></a>

### `terms_of_use_link`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Link to a site's terms of use. For internal pages, the reference recommends site-relative URLs rather than including the domain.

<a id="desc_privacy_policy_link" name="desc_privacy_policy_link"></a>

### `privacy_policy_link`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Link to the site's privacy policy. For internal links, use a site-relative path as described in the bundled 2.2.2 reference.

<a id="desc_ip_anonymization" name="desc_ip_anonymization"></a>

### `ip_anonymization`


**Documented default (Geeklog 2.2.2):** `-1`
The 2.2.2 reference documents `-1` as disabled, `0` as immediate, and positive numbers as delays in seconds. Its scheduled processing depends on Geeklog's [`cron_schedule_interval`](#desc_cron_schedule_interval), so anonymization may occur later than the configured delay. It affects supported IP data in the Geeklog database, **not web server or application log files**. The tagged reference warns that separately retained application and server logs must be handled under the site's own retention procedures. Low delays can interfere with functions that rely on IP addresses.

## Mail settings — Geeklog 2.2.2

<a id="site_mail" name="site_mail"></a>

<a id="desc_site_mail" name="desc_site_mail"></a>

### `site_mail`


**Documented default (Geeklog 2.2.2):** `admin@example.com`
Administrative email address used by Geeklog.

<a id="desc_noreply_mail" name="desc_noreply_mail"></a>

### `noreply_mail`


**Documented default (Geeklog 2.2.2):** `noreply@example.com`
Sender address of system-generated messages, including registration emails. The tagged 2.2.2 reference permits the same address as `site_mail` or a separate non-reply address to reduce address harvesting through registrations. When it differs from `site_mail`, the historical mail output includes a message discouraging replies to that address. Use a valid authenticated sender accepted by your actual transport; do not rely on an undeliverable address.

<a id="desc_mail_settings_backend" name="desc_mail_settings_backend"></a>

### `mail_settings_backend`


**Documented default (Geeklog 2.2.2):** `mail`
Select the email sending method: `smtp`, `smtps`, `sendmail` or PHP `mail` in the 2.2.2 reference. In the tagged 2.2.2 reference, the `smtps` transport requires the PHP OpenSSL extension. Available transports are `smtp`, `smtps`, `sendmail` and PHP `mail`. Verify the server's current encryption and authentication requirements before selecting a transport; this historical setting does not guarantee transport security by itself.

<a id="desc_mail_settings_sendmail_path" name="desc_mail_settings_sendmail_path"></a>

### `mail_settings_sendmail_path`


**Documented default (Geeklog 2.2.2):** `/usr/bin/sendmail`
Absolute filesystem path to the `sendmail` executable when the `sendmail` backend is selected.

<a id="desc_mail_settings_sendmail_args" name="desc_mail_settings_sendmail_args"></a>

### `mail_settings_sendmail_args`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Optional arguments passed to `sendmail` when that backend is selected. Only use values approved for your server.

<a id="desc_mail_settings_host" name="desc_mail_settings_host"></a>

### `mail_settings_host`


**Documented default (Geeklog 2.2.2):** `smtp.example.com`
SMTP server hostname for the `smtp` and `smtps` backends.

<a id="desc_mail_settings_port" name="desc_mail_settings_port"></a>

### `mail_settings_port`


**Documented default (Geeklog 2.2.2):** `25`
SMTP destination port used by `smtp` or `smtps`. The 2.2.2 reference gives `25` for SMTP and `587` for its secure SMTP example, but the correct port and encryption mode are determined by the real mail server. The historical default `25` is not a deployment recommendation.

<a id="desc_mail_settings_auth" name="desc_mail_settings_auth"></a>

### `mail_settings_auth`


**Documented default (Geeklog 2.2.2):** `0`
Controls authentication with an `smtp` or `smtps` backend: `1` if the server requires credentials, `0` (or an empty field) otherwise. Review the configured SMTP username and password separately; do not publish credentials in documentation or logs.

<a id="desc_mail_settings_username" name="desc_mail_settings_username"></a>

### `mail_settings_username`


**Documented default (Geeklog 2.2.2):** `smtp-username`
SMTP account name used when the selected mail backend requires authentication.

<a id="desc_mail_settings_password" name="desc_mail_settings_password"></a>

### `mail_settings_password`


**Documented default (Geeklog 2.2.2):** `smtp-password`
SMTP account secret. Never include a real password in documentation examples, public issue reports or diagnostic logs.

<a id="desc_mail_cc_enabled" name="desc_mail_cc_enabled"></a>

### `mail_cc_enabled`


**Documented default (Geeklog 2.2.2):** `True`
Controls whether users can send themselves a copy of an email.

<a id="desc_mail_cc_default" name="desc_mail_cc_default"></a>

### `mail_cc_default`


**Documented default (Geeklog 2.2.2):** `False`
Controls whether the copy-to-self checkbox is selected by default.

<a id="desc_mail_charset" name="desc_mail_charset"></a>

### `mail_charset`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Character encoding of outgoing email. If empty, the configuration reference says the site's `default_charset` is used.

---

**Migration note:** These are version-scoped descriptions based on the bundled 2.2.2 reference; a working installation and original defaults should still be reviewed before calling them authoritative. The embedded `config.html` is intentionally preserved unchanged until complete migration.


## Syndication and feeds — Geeklog 2.2.2

The settings below are **defaults for newly created feeds**, not necessarily overrides of existing feed configurations. They follow the [bundled Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html#site_syndication). Geeklog also provides a *Content Syndication* administration interface.

<a id="site_syndication" name="site_syndication"></a>

<a id="desc_backend" name="desc_backend"></a>

### `backend`


**Documented default (Geeklog 2.2.2):** `1`
Controls whether a feed file is generated for articles. The 2.2.2 reference documents `0` for disabled and `1` for enabled. The default in that reference is `1`.

<a id="desc_rdf_file" name="desc_rdf_file"></a>

### `rdf_file`


**Documented default (Geeklog 2.2.2):** `HTML path with "/backend/geeklog.rss" suffix`
Filesystem path to the feed file. The bundled reference places it under the site's HTML directory, with a `/backend/geeklog.rss` suffix. The destination directory **must be inside `path_html`**. This is a server path, not a public URL.

<a id="desc_rdf_limit" name="desc_rdf_limit"></a>

### `rdf_limit`


**Documented default (Geeklog 2.2.2):** `10`
Controls how many articles are exported. A number such as `10` limits the count; a value such as `24h` selects articles within the previous number of hours. The documented default is `10`.

<a id="desc_rdf_storytext" name="desc_rdf_storytext"></a>

### `rdf_storytext`


**Documented default (Geeklog 2.2.2):** `0`
Determines how much article introduction text is included in a feed: `0` excludes it, `1` includes the complete introduction, and a value greater than `1` limits it to that many characters. The documented default is `0`.

<a id="desc_rdf_language" name="desc_rdf_language"></a>

### `rdf_language`


**Documented default (Geeklog 2.2.2):** `en-gb`
Language tag advertised by the feed. The bundled reference gives `en-gb` as the default and notes that feed language tags can differ from PHP locale strings; for example, `de-DE` versus `de_DE`.

<a id="desc_syndication_max_headlines" name="desc_syndication_max_headlines"></a>

### `syndication_max_headlines`


**Documented default (Geeklog 2.2.2):** `0`
Maximum number of headlines **imported** into a portal block. The per-block setting can also provide a limit. The documented default `0` means import all available headlines.

<a id="desc_comment_feeds_article_tag" name="desc_comment_feeds_article_tag"></a>

### `comment_feeds_article_tag`


**Documented default (Geeklog 2.2.2):** `&lt;p&gt;[Original Article: &lt;a href="%s"&gt;%s&lt;/a&gt;%s%s]\n`
Format string inserted for an article referenced in a comment feed. The bundled documentation describes **four ordered string placeholders**, supplied through a formatting call: article URL, article title, article-author tag and comment-author tag. Preserve the correct placeholder count and formatting when customizing it; avoid inserting untrusted raw markup.

<a id="desc_comment_feeds_article_tag_position" name="desc_comment_feeds_article_tag_position"></a>

### `comment_feeds_article_tag_position`


**Documented default (Geeklog 2.2.2):** `end`
Controls placement of the formatted article tag within the comment body. The 2.2.2 reference documents `start`, `end` and `none`; the default is `end`.

<a id="desc_comment_feeds_article_author_tag" name="desc_comment_feeds_article_author_tag"></a>

### `comment_feeds_article_author_tag`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Optional format string for a link to the article author's profile and name. It contributes to `comment_feeds_article_tag` when populated. The documented default is an empty string.

<a id="desc_comment_feeds_comment_author_tag" name="desc_comment_feeds_comment_author_tag"></a>

### `comment_feeds_comment_author_tag`


**Documented default (Geeklog 2.2.2):** `, Comment By: &lt;a href="%s"&gt;%s&lt;/a&gt;`
Optional format string for a link to the comment author's profile and name. It contributes to `comment_feeds_article_tag`; setting it to an empty string omits that tag.

### Comment-feed formatting examples

The bundled 2.2.2 reference includes three preformatted templates. The examples below present their *literal template characters* for review, not HTML to insert directly into this Markdown page. A site-specific formatter must supply the expected arguments in the documented order and escape output appropriately.

**Article reference** — four `%s` substitutions (article URL, title, article-author fragment, comment-author fragment):

```text
<p>[Original Article: <a href="%s">%s</a>%s%s]\\n
```

**Article-author fragment** — two `%s` substitutions:

```text
 Written By: <a href="%s">%s</a>
```

**Comment-author fragment** — two `%s` substitutions:

```text
, Comment By: <a href="%s">%s</a>
```

These legacy strings should not be treated as safe, modern HTML templates without checking escaping, author visibility and the current rendering context.



**Compatibility note:** These are version-specific descriptions, not tested configuration changes. Confirm effects on a staging installation. The embedded `config.html` remains unchanged during migration.


## Articles and presentation — Geeklog 2.2.2

Source: [bundled Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Descriptions reflect this specific release; do not apply old security defaults to newer deployments.

<a id="stories" name="stories"></a>
<a id="stories_story" name="stories_story"></a>

<a id="desc_maximagesperarticle" name="desc_maximagesperarticle"></a>

### `maximagesperarticle`


**Documented default (Geeklog 2.2.2):** `5`
Maximum number of images allowed in an article; bundled default: `5`.

<a id="desc_limitnews" name="desc_limitnews"></a>

### `limitnews`


**Documented default (Geeklog 2.2.2):** `10`
Number of articles displayed on the index page and in the older-articles block; bundled default: `10`.

<a id="desc_minnews" name="desc_minnews"></a>

### `minnews`


**Documented default (Geeklog 2.2.2):** `1`
Minimum number of articles that may appear on a topic page; bundled default: `1`.

<a id="desc_contributedbyline" name="desc_contributedbyline"></a>

### `contributedbyline`


**Documented default (Geeklog 2.2.2):** `1`
When set to `1`, displays an article author's username publicly and permits username-based search; `0` disables it.

<a id="desc_hideviewscount" name="desc_hideviewscount"></a>

### `hideviewscount`


**Documented default (Geeklog 2.2.2):** `0`
`0` shows an article's view count, while `1` hides it.

<a id="desc_hideemailicon" name="desc_hideemailicon"></a>

### `hideemailicon`


**Documented default (Geeklog 2.2.2):** `0`
`1` disables the email-article feature and hides its article options; default `0`.

<a id="desc_hideprintericon" name="desc_hideprintericon"></a>

### `hideprintericon`


**Documented default (Geeklog 2.2.2):** `0`
`1` disables the printer-friendly article view and hides its links; default `0`.

<a id="desc_allow_page_breaks" name="desc_allow_page_breaks"></a>

### `allow_page_breaks`


**Documented default (Geeklog 2.2.2):** `1`
Controls use of the `[page_break]` tag to split an article into multiple pages; default `1`.

<a id="desc_page_break_comments" name="desc_page_break_comments"></a>

### `page_break_comments`


**Documented default (Geeklog 2.2.2):** `last`
For multipage articles, places comments on `first`, `last` or `all` pages; documented default `last`. Comments on all pages may return a user to the first page after posting under some settings.

<a id="desc_article_image_align" name="desc_article_image_align"></a>

### `article_image_align`


**Documented default (Geeklog 2.2.2):** `right`
Displays the article's topic image on the `right` or `left`; bundled default `right`.

<a id="desc_show_topic_icon" name="desc_show_topic_icon"></a>

### `show_topic_icon`


**Documented default (Geeklog 2.2.2):** `1`
Default for **new articles and article submissions**: `1` shows the topic icon, `0` hides it. This controls the initial setting for those items; it does not change already saved articles.

<a id="desc_draft_flag" name="desc_draft_flag"></a>

### `draft_flag`


**Documented default (Geeklog 2.2.2):** `0`
The default draft flag for **new articles created by Story Admins**: `1` marks the article as a draft; `0` leaves the draft flag unset. This is a creation default, not a rule that publishes all drafts automatically.

<a id="desc_frontpage" name="desc_frontpage"></a>

### `frontpage`


**Documented default (Geeklog 2.2.2):** `0`
For **new articles and article submissions**, `1` selects the site's frontpage and `0` selects only the article's topic page. The original 2.2.2 reference explicitly exempts articles submitted to the **archive topic**: they do not appear on the frontpage even if this setting would otherwise select it. This is an initial placement setting, not a change to existing articles.

<a id="desc_hide_no_news_msg" name="desc_hide_no_news_msg"></a>

### `hide_no_news_msg`


**Documented default (Geeklog 2.2.2):** `0`
Set to `1` to suppress the **No News To Display** message on `index.php`, including topic views with no articles. The documented default is `0`, so the message is normally shown.

<a id="desc_hide_main_page_navigation" name="desc_hide_main_page_navigation"></a>

### `hide_main_page_navigation`


**Documented default (Geeklog 2.2.2):** `false`
The historical values are `frontpage` (hide Google-style paging on the site's `index.php` frontpage) and `frontpage_topics` (hide it on both the frontpage and topic pages); the bundled default is `false`. Hiding pagination can make older articles difficult to reach. These strings are historical 2.2.2 options, not a recommendation for newer versions.

<a id="desc_onlyrootfeatures" name="desc_onlyrootfeatures"></a>

### `onlyrootfeatures`


**Documented default (Geeklog 2.2.2):** `0`
Set to `1` to allow only **Root** users to mark an article as featured. The source explains the reason: multiple article admins (Story Admins) may have different visibility over articles and otherwise unintentionally replace one another's featured article. The default `0` does not impose this Root-only restriction; actual editorial privileges still depend on the site's permissions.

<a id="users_login" name="users_login"></a>

<a id="desc_lastlogin" name="desc_lastlogin"></a>

### `lastlogin`


**Documented default (Geeklog 2.2.2):** `true`
Controls whether Geeklog records users' most recent login time.

<a id="desc_loginrequired" name="desc_loginrequired"></a>

### `loginrequired`


**Documented default (Geeklog 2.2.2):** `0`
Require an account to access the site (`1`). This setting overrides the more specific login requirements below when enabled.

<a id="desc_submitloginrequired" name="desc_submitloginrequired"></a>

### `submitloginrequired`


**Documented default (Geeklog 2.2.2):** `0`
Require a logged-in user for article and plugin-item submissions when `1`.

<a id="desc_commentsloginrequired" name="desc_commentsloginrequired"></a>

### `commentsloginrequired`


**Documented default (Geeklog 2.2.2):** `0`
Require login to submit comments when `1`.

<a id="desc_statsloginrequired" name="desc_statsloginrequired"></a>

### `statsloginrequired`


**Documented default (Geeklog 2.2.2):** `0`
Require login to view site statistics when `1`.

<a id="desc_searchloginrequired" name="desc_searchloginrequired"></a>

### `searchloginrequired`


**Documented default (Geeklog 2.2.2):** `0`
`1` restricts advanced search to logged-in users; `2` also restricts simple search.

<a id="desc_profileloginrequired" name="desc_profileloginrequired"></a>

### `profileloginrequired`


**Documented default (Geeklog 2.2.2):** `0`
Require login to view another user's profile when `1`.

<a id="desc_emailuserloginrequired" name="desc_emailuserloginrequired"></a>

### `emailuserloginrequired`


**Documented default (Geeklog 2.2.2):** `0`
Require login to send email to another user using the site form when `1`.

<a id="desc_emailstoryloginrequired" name="desc_emailstoryloginrequired"></a>

### `emailstoryloginrequired`


**Documented default (Geeklog 2.2.2):** `0`
Require login to email articles when `1`.

<a id="desc_directoryloginrequired" name="desc_directoryloginrequired"></a>

### `directoryloginrequired`


**Documented default (Geeklog 2.2.2):** `0`
Require login to access the list of older articles when `1`.

<a id="desc_passwordspeedlimit" name="desc_passwordspeedlimit"></a>

### `passwordspeedlimit`


**Documented default (Geeklog 2.2.2):** `300`
Minimum time between password-reset requests in seconds; bundled default `300`.

<a id="desc_login_attempts" name="desc_login_attempts"></a>

### `login_attempts`


**Documented default (Geeklog 2.2.2):** `3`
Number of failed sign-in attempts before the login speed limit applies; bundled default `3`.

<a id="desc_login_speedlimit" name="desc_login_speedlimit"></a>

### `login_speedlimit`


**Documented default (Geeklog 2.2.2):** `300`
Delay, in seconds, before another login may be attempted after the failed-attempt threshold; bundled default `300`.

<a id="desc_invalidloginattempts" name="desc_invalidloginattempts"></a>

### `invalidloginattempts`


**Documented default (Geeklog 2.2.2):** `7`
Maximum invalid login attempts for one user account before Geeklog sends an administrator alert within the configured time window; bundled default `7`. Setting this option to `0` disables this alert in the tagged 2.2.2 reference. This notification is distinct from the login retry speed limit.

<a id="desc_invalidloginmaxtime" name="desc_invalidloginmaxtime"></a>

### `invalidloginmaxtime`


**Documented default (Geeklog 2.2.2):** `1200`
Time window, in seconds, during which invalid attempts on a user account are counted before Geeklog emails an administrator; bundled default `1200`. Setting `0` disables this notification in the tagged 2.2.2 reference. The `login_speedlimit` and `login_attempts` settings can suppress or delay retries enough that the warning threshold is never reached; test the interaction before relying on these alerts.

<a id="desc_enable_twofactorauth" name="desc_enable_twofactorauth"></a>

### `enable_twofactorauth`


**Documented default (Geeklog 2.2.2):** `False`
Set to `1` to make two-factor authentication available. Each user must also enable it in their own account settings and configure a compatible authenticator application; the tagged 2.2.2 guide specifically references Google Authenticator. The bundled default is `False`, so enabling the site option alone does not automatically enroll users.

<a id="desc_pass_alg" name="desc_pass_alg"></a>

### `pass_alg`


**Documented default (Geeklog 2.2.2):** `sha1`
Legacy password-hashing algorithm selector documented for Geeklog 2.2.2. The bundled 2.2.2 reference lists `md5`, `sha1`, `sha256`, `sha512` and `blowfish`. It describes `sha1` as portable and Blowfish as stronger in that historical context. **These old recommendations are not current password-security guidance.** Do not change this setting or existing stored password hashes without a tested migration and the actual installed implementation.

<a id="desc_pass_stretch" name="desc_pass_stretch"></a>

### `pass_stretch`


**Documented default (Geeklog 2.2.2):** `4096`
Number of password-hash iterations in the historical 2.2.2 scheme; it must be greater than `0` and its documented default is `4096`. Do not infer that this legacy iteration count provides adequate password protection today; changing hashing parameters requires a tested account migration and review of the installed implementation.



## Theme and template settings — Geeklog 2.2.2

Settings derived from the [tagged Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Verify behavior against the installed release before changing live site settings.

<a id="theme" name="theme"></a>
<a id="theme_theme" name="theme_theme"></a>

<a id="desc_theme" name="desc_theme"></a>

### `theme`


**Documented default (Geeklog 2.2.2):** `Denim Three`
Default theme for anonymous visitors and new accounts. Existing users may retain their chosen theme if user theme selection is allowed; 2.2.2 reference default: Denim Three.

<a id="desc_doctype" name="desc_doctype"></a>

### `doctype`


**Documented default (Geeklog 2.2.2):** `HTML 4.01 Strict`
Document type declaration emitted by themes that use the `{doctype}` template variable. Hard-coded DOCTYPE declarations in a theme are not controlled by this setting.

<a id="desc_menu_elements" name="desc_menu_elements"></a>

### `menu_elements`


**Documented default (Geeklog 2.2.2):** `array('contribute', 'search', 'stats', 'directory', 'plugins')`
Controls entries in themes using `{menu_elements}`. The 2.2.2 reference lists `home`, `contribute`, `search`, `stats`, `directory`, `login`, `prefs`, `plugins` and `custom`; actual display depends on the theme.

<a id="desc_path_themes" name="desc_path_themes"></a>

### `path_themes`


**Documented default (Geeklog 2.2.2):** `/path/to/geeklog/public_html/layout/`
Filesystem directory containing themes. The 2.2.2 reference identifies it as the site's `public_html/layout/` directory and states this path cannot be changed from its default.

<a id="desc_cache_templates" name="desc_cache_templates"></a>

### `cache_templates`


**Documented default (Geeklog 2.2.2):** `true`
Controls caching of theme template files. Caching usually helps performance, but may be unsuitable for disk bottlenecks or dynamic autotags in templates. It is separate from content caching.

<a id="desc_cache_mobile" name="desc_cache_mobile"></a>

### `cache_mobile`


**Documented default (Geeklog 2.2.2):** `true`
When enabled, mobile-device responses may be cached separately from desktop responses. Disabling it can reduce cache variants when mobile and desktop output are equivalent.

<a id="desc_cache_resource" name="desc_cache_resource"></a>

### `cache_resource`


**Documented default (Geeklog 2.2.2):** `true`
Controls combining, minifying and caching JavaScript and CSS resources. The 2.2.2 reference notes that themes using `style.css.php` can apply separate mandatory caching behavior.


## User registration and approval — Geeklog 2.2.2

Settings derived from the [tagged Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Verify behavior against the installed release before changing live site settings.

<a id="users_usersub" name="users_usersub"></a>

<a id="desc_usersubmission" name="desc_usersubmission"></a>

### `usersubmission`


**Documented default (Geeklog 2.2.2):** `0`
Set to `1` to require administrative approval of new accounts before their password is issued; `0` disables the submission queue. The tagged reference explicitly warns that **queued accounts should be processed before switching off the queue**, or pending registrations may be left unresolved.

<a id="desc_allow_domains" name="desc_allow_domains"></a>

### `allow_domains`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
When the user approval queue is enabled, a comma-separated list of email domains can bypass manual approval and be accepted automatically. The 2.2.2 reference also accepts regular expressions. An overbroad regex may bypass review for unintended addresses, so test matching rules with permitted and forbidden examples before deployment.

<a id="desc_disallow_domains" name="desc_disallow_domains"></a>

### `disallow_domains`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Reject registration email domains matching this list or its regular expressions. Unlike `allow_domains`, the 2.2.2 reference explicitly states that **this restriction applies even when the `usersubmission` approval queue is disabled**. Validate expression boundaries and representative addresses before relying on the restriction.


## Article and content submissions — Geeklog 2.2.2

Settings derived from the [tagged Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Verify behavior against the installed release before changing live site settings.

<a id="users_submission" name="users_submission"></a>

<a id="desc_storysubmission" name="desc_storysubmission"></a>

### `storysubmission`


**Documented default (Geeklog 2.2.2):** `1`
Set to `1` to enable the article submission moderation queue, or `0` to disable it. The documented default is `1`. This controls review of submitted articles; do not confuse it with account registration approval.

<a id="desc_listdraftstories" name="desc_listdraftstories"></a>

### `listdraftstories`


**Documented default (Geeklog 2.2.2):** `0`
When set to `1`, displays an additional block on the submissions/moderation page (`moderation.php`) listing articles with the **draft** flag. It does not itself publish, approve or change those drafts.

<a id="desc_postmode" name="desc_postmode"></a>

### `postmode`


**Documented default (Geeklog 2.2.2):** `plaintext`
Default article submission format: `plaintext` or `html` in the 2.2.2 reference.

<a id="desc_speedlimit" name="desc_speedlimit"></a>

### `speedlimit`


**Documented default (Geeklog 2.2.2):** `45`
Minimum delay between content submissions, in seconds; bundled default `45`. This is a rate-limiting mechanism, not a complete spam defense.

<a id="desc_skip_preview" name="desc_skip_preview"></a>

### `skip_preview`


**Documented default (Geeklog 2.2.2):** `0`
When set to `1`, displays both **Preview** and **Submit** buttons on the submission forms for articles and comments, so the user need not preview before submitting. With the default `0`, preview is required by the historical workflow. This does not bypass the separate moderation queue or permission checks.

<a id="desc_advanced_editor" name="desc_advanced_editor"></a>

### `advanced_editor`


**Documented default (Geeklog 2.2.2):** `false`
Enables a rich-text/WYSIWYG editor for supported article, comment and Static Pages forms. Geeklog 2.2.2 shipped with CKEditor.

<a id="desc_advanced_editor_name" name="desc_advanced_editor_name"></a>

### `advanced_editor_name`


**Documented default (Geeklog 2.2.2):** `CKEditor`
Name of the selected rich-text editor; the 2.2.2 reference lists CKEditor as the default.

<a id="desc_wikitext_editor" name="desc_wikitext_editor"></a>

### `wikitext_editor`


**Documented default (Geeklog 2.2.2):** `false`
Adds Wiki-style formatting to the article editor using the older PEAR Text_Wiki implementation when enabled. Confirm dependencies before relying on this legacy option.

<a id="desc_remove_4byte_chars" name="desc_remove_4byte_chars"></a>

### `remove_4byte_chars`


**Documented default (Geeklog 2.2.2):** `true`
Controls removal of four-byte UTF-8 characters, including emoji, when `COM_applyBasicFilter()` runs. Turning removal off requires compatible `utf8mb4` database/table/column collations and compatible plugins; otherwise saving content can fail.


## Comments and moderation — Geeklog 2.2.2

Settings derived from the [tagged Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Verify behavior against the installed release before changing live site settings.

<a id="users_comments" name="users_comments"></a>

<a id="desc_commentspeedlimit" name="desc_commentspeedlimit"></a>

### `commentspeedlimit`


**Documented default (Geeklog 2.2.2):** `45`
Minimum delay in seconds between comments by the same user; bundled default `45`.

<a id="desc_comment_limit" name="desc_comment_limit"></a>

### `comment_limit`


**Documented default (Geeklog 2.2.2):** `100`
Maximum number of comments displayed per page; bundled default `100`.

<a id="desc_comment_mode" name="desc_comment_mode"></a>

### `comment_mode`


**Documented default (Geeklog 2.2.2):** `nested`
Default display mode for comments; 2.2.2 lists `threaded`, `nested`, `flat` and `nocomments`.

<a id="desc_comment_order" name="desc_comment_order"></a>

### `comment_order`


**Documented default (Geeklog 2.2.2):** `ASC`
Top-level comment order by date: `ASC` oldest first or `DESC` newest first.

<a id="desc_comment_code" name="desc_comment_code"></a>

### `comment_code`


**Documented default (Geeklog 2.2.2):** `0`
Default comment availability on new articles: `0` enables comments, while `-1` disables them.

<a id="desc_commentsubmission" name="desc_commentsubmission"></a>

### `commentsubmission`


**Documented default (Geeklog 2.2.2):** `0`
Set to `1` to enable the comment submission moderation queue, or `0` to disable it. The documented default is `0`. This controls approval of submitted comments, not the separate article or user queues.

<a id="desc_comment_edit" name="desc_comment_edit"></a>

### `comment_edit`


**Documented default (Geeklog 2.2.2):** `0`
Enables a limited editing window for registered users' own comments. Anonymous users cannot edit their comments, while administrators with `comment.edit` may. Review interactions with queued comments.

<a id="desc_comment_edittime" name="desc_comment_edittime"></a>

### `comment_edittime`


**Documented default (Geeklog 2.2.2):** `1800`
Time in seconds during which an author may edit a comment when editing is enabled; bundled default `1800`.

<a id="desc_article_comment_close_enabled" name="desc_article_comment_close_enabled"></a>

### `article_comment_close_enabled`


**Documented default (Geeklog 2.2.2):** `0`
Default setting for whether newly created articles should stop accepting comments after a specified number of days. It can be changed per article.

<a id="desc_article_comment_close_days" name="desc_article_comment_close_days"></a>

### `article_comment_close_days`


**Documented default (Geeklog 2.2.2):** `30`
Number of days after which new articles configured for automatic closure stop accepting comments; bundled default `30`. It has no effect unless closure is enabled for that article.

<a id="desc_comment_close_rec_stories" name="desc_comment_close_rec_stories"></a>

### `comment_close_rec_stories`


**Documented default (Geeklog 2.2.2):** `0`
Number of most recent articles that permit new comments; older articles can be closed as new ones arrive. `0` disables this limit.

<a id="desc_allow_reply_notifications" name="desc_allow_reply_notifications"></a>

### `allow_reply_notifications`


**Documented default (Geeklog 2.2.2):** `0`
Controls whether registered users can subscribe to email notifications when someone replies directly to their comments.

<a id="desc_comment_on_same_page" name="desc_comment_on_same_page"></a>

### `comment_on_same_page`


**Documented default (Geeklog 2.2.2):** `0`
Controls whether the comment editor is shown on the same page as the content instead of a separate page.

<a id="desc_show_comments_at_replying" name="desc_show_comments_at_replying"></a>

### `show_comments_at_replying`


**Documented default (Geeklog 2.2.2):** `0`
Controls whether existing comments are visible on the dedicated reply page. This option is irrelevant when the same-page editor is enabled.



## Blocks — administration and topic navigation — Geeklog 2.2.2

Descriptions condensed from the [bundled 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Check installed-release behavior before modifying a production site.

<a id="blocks" name="blocks"></a>
<a id="blocks_admin" name="blocks_admin"></a>

<a id="desc_sort_admin" name="desc_sort_admin"></a>

### `sort_admin`


**Documented default (Geeklog 2.2.2):** `false`
Sort entries in the Administrator block and Command and Control icons alphabetically when enabled.

<a id="desc_link_documentation" name="desc_link_documentation"></a>

### `link_documentation`


**Documented default (Geeklog 2.2.2):** `1`
Show the Geeklog documentation link in the administrator block when set to `1`.

<a id="desc_link_versionchecker" name="desc_link_versionchecker"></a>

### `link_versionchecker`


**Documented default (Geeklog 2.2.2):** `1`
Display the version-check link in the administrator block when enabled; the reference notes this is visible only to `Root` members.

<a id="blocks_topics" name="blocks_topics"></a>

<a id="desc_sortmethod" name="desc_sortmethod"></a>

### `sortmethod`


**Documented default (Geeklog 2.2.2):** `alpha`
Topic sorting in the Sections block: `alpha` sorts alphabetically; `sortnum` uses the configured sort number.

<a id="desc_showstorycount" name="desc_showstorycount"></a>

### `showstorycount`


**Documented default (Geeklog 2.2.2):** `1`
Show the number of articles in each topic in the Sections block when `1`.

<a id="desc_showsubmissioncount" name="desc_showsubmissioncount"></a>

### `showsubmissioncount`


**Documented default (Geeklog 2.2.2):** `1`
Show the number of article submissions by topic in the Sections block when `1`.

<a id="desc_hide_home_link" name="desc_hide_home_link"></a>

### `hide_home_link`


**Documented default (Geeklog 2.2.2):** `0`
Hide the Home link in the Sections block when `1`.


## Blocks — online users and recent content — Geeklog 2.2.2

Descriptions condensed from the [bundled 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Check installed-release behavior before modifying a production site.

<a id="blocks_who" name="blocks_who"></a>

<a id="desc_whosonline_threshold" name="desc_whosonline_threshold"></a>

### `whosonline_threshold`


**Documented default (Geeklog 2.2.2):** `300`
Idle-time threshold, in seconds, after which a user is no longer listed in the Who's Online block; the 2.2.2 reference default is `300`.

<a id="desc_whosonline_anonymous" name="desc_whosonline_anonymous"></a>

### `whosonline_anonymous`


**Documented default (Geeklog 2.2.2):** `0`
When enabled, anonymous visitors see only the count of registered users online rather than their names.

<a id="desc_whosonline_photo" name="desc_whosonline_photo"></a>

### `whosonline_photo`


**Documented default (Geeklog 2.2.2):** `0`
When enabled, display a thumbnail of a user's uploaded photo where available, otherwise a photo icon.

<a id="blocks_what" name="blocks_what"></a>

<a id="desc_newstoriesinterval" name="desc_newstoriesinterval"></a>

### `newstoriesinterval`


**Documented default (Geeklog 2.2.2):** `86400`
Maximum age, in seconds, for articles classified as new; default `86400`.

<a id="desc_newcommentsinterval" name="desc_newcommentsinterval"></a>

### `newcommentsinterval`


**Documented default (Geeklog 2.2.2):** `172800`
Maximum age, in seconds, for comments classified as new; default `172800`.

<a id="desc_newtrackbackinterval" name="desc_newtrackbackinterval"></a>

### `newtrackbackinterval`


**Documented default (Geeklog 2.2.2):** `172800`
Maximum age of new trackbacks, in seconds; default `172800`.

<a id="desc_hidenewstories" name="desc_hidenewstories"></a>

### `hidenewstories`


**Documented default (Geeklog 2.2.2):** `0`
Hide new articles in the What's New block when `1`.

<a id="desc_hidenewcomments" name="desc_hidenewcomments"></a>

### `hidenewcomments`


**Documented default (Geeklog 2.2.2):** `0`
Hide new comments in the What's New block when `1`.

<a id="desc_hidenewtrackbacks" name="desc_hidenewtrackbacks"></a>

### `hidenewtrackbacks`


**Documented default (Geeklog 2.2.2):** `0`
Hide new trackbacks in the What's New block when `1`.

<a id="desc_hidenewplugins" name="desc_hidenewplugins"></a>

### `hidenewplugins`


**Documented default (Geeklog 2.2.2):** `0`
Hide recent items provided by plugins in the What's New block when `1`.

<a id="desc_title_trim_length" name="desc_title_trim_length"></a>

### `title_trim_length`


**Documented default (Geeklog 2.2.2):** `20`
Maximum displayed title length for items in the What's New block; default `20`.

<a id="desc_whatsnew_cache_time" name="desc_whatsnew_cache_time"></a>

### `whatsnew_cache_time`


**Documented default (Geeklog 2.2.2):** `3600`
Maximum cache duration for the What's New block, in seconds; default `3600`. Set to `0` to disable this cache.


## Language selection and multilingual content — Geeklog 2.2.2

Descriptions condensed from the [bundled 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Check installed-release behavior before modifying a production site.

<a id="languages" name="languages"></a>
<a id="languages_language" name="languages_language"></a>

<a id="desc_language" name="desc_language"></a>

### `language`


**Documented default (Geeklog 2.2.2):** `english`
Default interface language for the site; the 2.2.2 bundled reference uses `english`.

<a id="desc_allow_user_language" name="desc_allow_user_language"></a>

### `allow_user_language`


**Documented default (Geeklog 2.2.2):** `1`
Allow registered users to choose an interface language in My Account when `1`.

<a id="desc_switchlang_homepage" name="desc_switchlang_homepage"></a>

### `switchlang_homepage`


**Documented default (Geeklog 2.2.2):** `0`
When enabled, changing language returns the visitor to the homepage, useful when an equivalent translated topic or page is absent.

<a id="desc_new_item_set_current_lang" name="desc_new_item_set_current_lang"></a>

### `new_item_set_current_lang`


**Documented default (Geeklog 2.2.2):** `0`
When enabled and multilingual support is configured, eligible new article or Static Pages identifiers include a current-language suffix.

<a id="desc_language_files" name="desc_language_files"></a>

### `language_files`


**Documented default (Geeklog 2.2.2):** `(disabled)`
Mapping of language suffixes such as `en` or `de` to installed Geeklog language files for multilingual content. It must be configured together with `languages`.

<a id="desc_languages" name="desc_languages"></a>

### `languages`


**Documented default (Geeklog 2.2.2):** `(disabled)`
Mapping of the same language suffixes to display names for multilingual content. This must match `language_files`; both must be enabled or disabled together.


## Locale, dates and number formats — Geeklog 2.2.2

Descriptions condensed from the [bundled 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Check installed-release behavior before modifying a production site.

<a id="languages_locale" name="languages_locale"></a>

<a id="desc_locale" name="desc_locale"></a>

### `locale`


**Documented default (Geeklog 2.2.2):** `en_GB`
PHP locale used for localized information such as dates; bundled reference default `en_GB`.

<a id="desc_date" name="desc_date"></a>

### `date`


**Documented default (Geeklog 2.2.2):** `%A, %B %d %Y @ %I:%M %p %Z`
Format string used for general dates and article timestamps. Check the bundled reference for its version-specific formatting directives.

<a id="desc_daytime" name="desc_daytime"></a>

### `daytime`


**Documented default (Geeklog 2.2.2):** `%m/%d %I:%M%p`
Shorter date-time format used where compact timestamps are needed.

<a id="desc_shortdate" name="desc_shortdate"></a>

### `shortdate`


**Documented default (Geeklog 2.2.2):** `%x`
Shortest date format, with the historical default `%x`.

<a id="desc_dateonly" name="desc_dateonly"></a>

### `dateonly`


**Documented default (Geeklog 2.2.2):** `%d-%b`
Short day-and-month date format, used by features including event and older-article blocks.

<a id="desc_timeonly" name="desc_timeonly"></a>

### `timeonly`


**Documented default (Geeklog 2.2.2):** `%I:%M %p %Z`
Time-only format used for time-specific displays such as event details.

<a id="desc_week_start" name="desc_week_start"></a>

### `week_start`


**Documented default (Geeklog 2.2.2):** `Sun`
First day of a calendar week: `Sun` or `Mon`.

<a id="desc_hour_mode" name="desc_hour_mode"></a>

### `hour_mode`


**Documented default (Geeklog 2.2.2):** `12`
Time-editing mode: `12` for AM/PM or `24` for a 24-hour clock.

<a id="desc_thousand_separator" name="desc_thousand_separator"></a>

### `thousand_separator`


**Documented default (Geeklog 2.2.2):** `,`
Character used to group thousands in formatted numbers.

<a id="desc_decimal_separator" name="desc_decimal_separator"></a>

### `decimal_separator`


**Documented default (Geeklog 2.2.2):** `.`
Character separating the integer and fractional parts of a number.

<a id="desc_decimal_count" name="desc_decimal_count"></a>

### `decimal_count`


**Documented default (Geeklog 2.2.2):** `2`
Number of decimal places displayed; historical default `2`.

<a id="desc_timezone" name="desc_timezone"></a>

### `timezone`


**Documented default (Geeklog 2.2.2):** `(disabled)`
Site's intended time zone when it differs from that of the hosting server. Confirm behavior on the installed release.



## Image processing libraries — Geeklog 2.2.2

Descriptions adapted from the [official Geeklog 2.2.2 configuration HTML](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). These are release-specific settings; test image operations in staging before applying them to a public site.

<a id="images" name="images"></a>
<a id="images_imagelib" name="images_imagelib"></a>

<a id="desc_image_lib" name="desc_image_lib"></a>

### `image_lib`


**Documented default (Geeklog 2.2.2):** `None`
Selects the image resize engine used for uploads: ImageMagick (`imagemagick`), Netpbm (`netpbm`) or PHP GD (`gdlib`) in Geeklog 2.2.2. Leave as `None` if no supported resizing backend is available. Verify installed extensions/binaries before enabling.

<a id="desc_path_to_mogrify" name="desc_path_to_mogrify"></a>

### `path_to_mogrify`


**Documented default (Geeklog 2.2.2):** `(disabled)`
Absolute filesystem path to the ImageMagick `mogrify` executable when `image_lib` is `imagemagick`. The historical reference uses `/usr/bin/mogrify` as an example; check your server.

<a id="desc_path_to_netpbm" name="desc_path_to_netpbm"></a>

### `path_to_netpbm`


**Documented default (Geeklog 2.2.2):** `(disabled)`
Absolute directory containing Netpbm executables when `image_lib` is `netpbm`. The 2.2.2 reference specifies a trailing slash.


## Image uploads and scaling — Geeklog 2.2.2

Descriptions adapted from the [official Geeklog 2.2.2 configuration HTML](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). These are release-specific settings; test image operations in staging before applying them to a public site.

<a id="images_upload" name="images_upload"></a>

<a id="desc_keep_unscaled_image" name="desc_keep_unscaled_image"></a>

### `keep_unscaled_image`


**Documented default (Geeklog 2.2.2):** `0`
When enabled, retains the original uploaded image as well as a resized version, allowing thumbnails to link to the original. Consider additional disk usage.

<a id="desc_allow_user_scaling" name="desc_allow_user_scaling"></a>

### `allow_user_scaling`


**Documented default (Geeklog 2.2.2):** `1`
When original images are retained, lets article authors select scaled or original images using the supported image tags (`[image X]` and `[unscaled X]`).

<a id="desc_jpeg_quality" name="desc_jpeg_quality"></a>

### `jpeg_quality`


**Documented default (Geeklog 2.2.2):** `(disabled)`
Controls JPEG encoding quality when images are resized. The referenced range is 0–100, but it is not a percentage; its documented fallback is 75 when unset. High values increase file size.

<a id="desc_debug_image_upload" name="desc_debug_image_upload"></a>

### `debug_image_upload`


**Documented default (Geeklog 2.2.2):** `false`
Adds diagnostic output for image upload and resize operations to Geeklog's error log when enabled. Avoid leaving verbose logging enabled in production.


## Images attached to articles — Geeklog 2.2.2

Descriptions adapted from the [official Geeklog 2.2.2 configuration HTML](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). These are release-specific settings; test image operations in staging before applying them to a public site.

<a id="images_articles" name="images_articles"></a>

<a id="desc_max_image_width" name="desc_max_image_width"></a>

### `max_image_width`


**Documented default (Geeklog 2.2.2):** `160`
Maximum article image width in pixels. The historical 2.2.2 reference documents `160`; larger images may be resized or rejected depending on the selected image library.

<a id="desc_max_image_height" name="desc_max_image_height"></a>

### `max_image_height`


**Documented default (Geeklog 2.2.2):** `160`
Maximum article image height in pixels; the reference documents `160`. Oversized images may be resized or rejected according to the image backend.

<a id="desc_max_image_size" name="desc_max_image_size"></a>

### `max_image_size`


**Documented default (Geeklog 2.2.2):** `1048576 (equals 1 MB)`
Maximum uploaded article image size in bytes; documented as `1048576` (1 MiB). Files larger than the limit are rejected even when an image-resizing library is configured.


## Topic icon image limits — Geeklog 2.2.2

Descriptions adapted from the [official Geeklog 2.2.2 configuration HTML](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). These are release-specific settings; test image operations in staging before applying them to a public site.

<a id="images_topic" name="images_topic"></a>

<a id="desc_max_topicicon_width" name="desc_max_topicicon_width"></a>

### `max_topicicon_width`


**Documented default (Geeklog 2.2.2):** `48`
Maximum topic icon width in pixels; the bundled reference documents `48`. Oversized icons may be resized or rejected.

<a id="desc_max_topicicon_height" name="desc_max_topicicon_height"></a>

### `max_topicicon_height`


**Documented default (Geeklog 2.2.2):** `48`
Maximum topic icon height in pixels; documented as `48`.

<a id="desc_max_topicicon_size" name="desc_max_topicicon_size"></a>

### `max_topicicon_size`


**Documented default (Geeklog 2.2.2):** `65536 (equals 64 KB)`
Maximum uploaded topic icon size in bytes; documented as `65536` (64 KiB). Oversized files are rejected regardless of whether a resizing library exists.


## User photos and generated avatars — Geeklog 2.2.2

Descriptions adapted from the [official Geeklog 2.2.2 configuration HTML](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). These are release-specific settings; test image operations in staging before applying them to a public site.

<a id="images_photos" name="images_photos"></a>

<a id="desc_max_photo_width" name="desc_max_photo_width"></a>

### `max_photo_width`


**Documented default (Geeklog 2.2.2):** `128`
Maximum stored user-photo width in pixels; historical default `128`. Images exceeding this may be resized or rejected.

<a id="desc_max_photo_height" name="desc_max_photo_height"></a>

### `max_photo_height`


**Documented default (Geeklog 2.2.2):** `128`
Maximum stored user-photo height in pixels; historical default `128`.

<a id="desc_max_photo_size" name="desc_max_photo_size"></a>

### `max_photo_size`


**Documented default (Geeklog 2.2.2):** `65536 (equals 64 KB)`
Maximum uploaded user-photo size in bytes; historical default `65536` (64 KiB). Files above the limit are rejected.

<a id="desc_force_photo_width" name="desc_force_photo_width"></a>

### `force_photo_width`


**Documented default (Geeklog 2.2.2):** `(disabled)`
Optional maximum display width for user photos in emitted HTML. This changes their displayed dimensions, not the dimensions of the stored image.

<a id="desc_default_photo" name="desc_default_photo"></a>

### `default_photo`


**Documented default (Geeklog 2.2.2):** `(disabled)`
Full URL of a fallback photo for accounts without their own photo, when configured. The original 2.2.2 reference describes this as disabled by default.

<a id="desc_generate_user_icon" name="desc_generate_user_icon"></a>

### `generate_user_icon`


**Documented default (Geeklog 2.2.2):** `true`
When enabled and `default_photo` is unavailable, generates a basic avatar from the username. Appearance depends on the theme's CSS and browser support for CSS variables.


## Gravatar integration — Geeklog 2.2.2

Descriptions adapted from the [official Geeklog 2.2.2 configuration HTML](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). These are release-specific settings; test image operations in staging before applying them to a public site.

<a id="images_gravatar" name="images_gravatar"></a>

<a id="desc_use_gravatar" name="desc_use_gravatar"></a>

### `use_gravatar`


**Documented default (Geeklog 2.2.2):** `false`
When enabled, requests an avatar from Gravatar for users who did not upload a photo. Uploaded photos take precedence. Consider external-service privacy and page-load performance.

<a id="desc_gravatar_rating" name="desc_gravatar_rating"></a>

### `gravatar_rating`


**Documented default (Geeklog 2.2.2):** `(disabled)`
Maximum Gravatar rating permitted for displayed remote avatars; the 2.2.2 reference mentions `G`, `PG`, `R` and `X`.

<a id="desc_gravatar_identicon" name="desc_gravatar_identicon"></a>

### `gravatar_identicon`


**Documented default (Geeklog 2.2.2):** `(disabled)`
Fallback Gravatar style when a remote avatar is absent. The historical reference lists Mystery Man, Identicon, MonsterId, WAvatar and Retro; availability may change with the external provider.



## Filesystem paths and storage — Geeklog 2.2.2

Descriptions based on the [versioned Geeklog configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Values and operating behavior must be checked on the target installation before modifying production settings.

<a id="site_paths" name="site_paths"></a>

<a id="desc_path_html" name="desc_path_html"></a>

### `path_html`


**Documented default (Geeklog 2.2.2):** `/path/to/geeklog/public_html/`
Filesystem path of the web-accessible Geeklog tree. A trailing slash is required. The 2.2.2 reference warns against modifying this setting on a live site except as part of a controlled migration; dependent image, editor, theme and feed paths must remain consistent.

<a id="desc_path_log" name="desc_path_log"></a>

### `path_log`


**Documented default (Geeklog 2.2.2):** `/path/to/geeklog/logs/`
Filesystem path of the Geeklog logging directory. Keep log files protected against public downloads.

<a id="desc_path_language" name="desc_path_language"></a>

### `path_language`


**Documented default (Geeklog 2.2.2):** `/path/to/geeklog/language/`
Filesystem path to the installed Geeklog language files.

<a id="desc_backup_path" name="desc_backup_path"></a>

### `backup_path`


**Documented default (Geeklog 2.2.2):** `/path/to/geeklog/backups/`
Filesystem path to stored database backup files. Protect this directory from web access and verify write permissions and actual recovery procedures.

<a id="desc_path_data" name="desc_path_data"></a>

### `path_data`


**Documented default (Geeklog 2.2.2):** `/path/to/geeklog/data/`
Filesystem path for Geeklog application data, including data used by bulk user import.

<a id="desc_path_images" name="desc_path_images"></a>

### `path_images`


**Documented default (Geeklog 2.2.2):** `/path/to/geeklog/public_html/images/`
Filesystem path for Geeklog images, user photos and article images. The 2.2.2 reference requires it to reside within `path_html`.

<a id="desc_path_editors" name="desc_path_editors"></a>

### `path_editors`


**Documented default (Geeklog 2.2.2):** `/path/to/geeklog/public_html/editors/`
Filesystem path to the rich-text editor assets. The 2.2.2 reference requires it to reside within `path_html`.


## Database backup options — Geeklog 2.2.2

Descriptions based on the [versioned Geeklog configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Values and operating behavior must be checked on the target installation before modifying production settings.

<a id="site_database" name="site_database"></a>

<a id="desc_dbdump_filename_prefix" name="desc_dbdump_filename_prefix"></a>

### `dbdump_filename_prefix`


**Documented default (Geeklog 2.2.2):** `geeklog_db_backup`
Filename prefix used for database dump files; the 2.2.2 reference uses `geeklog_db_backup`.

<a id="desc_dbdump_tables_only" name="desc_dbdump_tables_only"></a>

### `dbdump_tables_only`


**Documented default (Geeklog 2.2.2):** `0`
When `1`, export database table structures without their row data; when `0`, export both table definitions and data. **Structure-only dumps cannot restore site content.**

<a id="desc_dbdump_gzip" name="desc_dbdump_gzip"></a>

### `dbdump_gzip`


**Documented default (Geeklog 2.2.2):** `1`
Controls whether database backup dumps are compressed when gzip support is available.

<a id="desc_dbdump_max_files" name="desc_dbdump_max_files"></a>

### `dbdump_max_files`


**Documented default (Geeklog 2.2.2):** `10`
Maximum number of retained database backup files; the reference default is `10`, with `0` disabling automatic deletion. Set retention based on your recovery requirements.


## Search results configuration — Geeklog 2.2.2

Descriptions based on the [versioned Geeklog configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Values and operating behavior must be checked on the target installation before modifying production settings.

<a id="site_search" name="site_search"></a>

<a id="desc_search_style" name="desc_search_style"></a>

### `search_style`


**Documented default (Geeklog 2.2.2):** `'google'`
Display style for search results: `google` or `table` in Geeklog 2.2.2.

<a id="desc_search_limits" name="desc_search_limits"></a>

### `search_limits`


**Documented default (Geeklog 2.2.2):** `10,15,25,30`
Comma-separated result counts offered to users; the reference lists `10,15,25,30`.

<a id="desc_num_search_results" name="desc_num_search_results"></a>

### `num_search_results`


**Documented default (Geeklog 2.2.2):** `30`
Default number of search results per page, chosen from `search_limits`; the bundled default is `30`.

<a id="desc_search_show_limit" name="desc_search_show_limit"></a>

### `search_show_limit`


**Documented default (Geeklog 2.2.2):** `true`
Controls whether visitors can select the number of results shown on a search page.

<a id="desc_search_show_sort" name="desc_search_show_sort"></a>

### `search_show_sort`


**Documented default (Geeklog 2.2.2):** `true`
Controls display of sorting controls; in table mode it affects column sorting.

<a id="desc_search_show_num" name="desc_search_show_num"></a>

### `search_show_num`


**Documented default (Geeklog 2.2.2):** `true`
Controls whether the search result number is shown.

<a id="desc_search_show_type" name="desc_search_show_type"></a>

### `search_show_type`


**Documented default (Geeklog 2.2.2):** `true`
Controls whether the source plugin or result type is shown in search results.

<a id="desc_search_separator" name="desc_search_separator"></a>

### `search_separator`


**Documented default (Geeklog 2.2.2):** `&amp;gt; (Space before and after character)`
Separator used between search-result type subgroups.

<a id="desc_search_def_keytype" name="desc_search_def_keytype"></a>

### `search_def_keytype`


**Documented default (Geeklog 2.2.2):** `'phrase'`
Default matching method: `all` requires every term, `any` permits one or more terms, and `phrase` matches the supplied phrase.

<a id="desc_search_def_sort" name="desc_search_def_sort"></a>

### `search_def_sort`


**Documented default (Geeklog 2.2.2):** `'Hits (desc)'`
Default ordering of search results; the 2.2.2 reference uses descending hits.

<a id="desc_search_use_topic" name="desc_search_use_topic"></a>

### `search_use_topic`


**Documented default (Geeklog 2.2.2):** `false`
If enabled, search can default to the most recently visited topic; otherwise it defaults to all topics.


## Advanced theme settings — Geeklog 2.2.2

These settings describe the historical [bundled 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html); they should be reviewed on a staging installation and must not be interpreted as current security defaults.

<a id="theme_advanced" name="theme_advanced"></a>

<a id="desc_show_right_blocks" name="desc_show_right_blocks"></a>

### `show_right_blocks`


**Documented default (Geeklog 2.2.2):** `false`
When enabled, shows the right-side block column on all site pages instead of limiting it to the homepage.

<a id="desc_showfirstasfeatured" name="desc_showfirstasfeatured"></a>

### `showfirstasfeatured`


**Documented default (Geeklog 2.2.2):** `0`
When enabled, renders the first article on any article listing page using featured-article templates, even when the article itself is not marked as featured.

<a id="desc_template_comments" name="desc_template_comments"></a>

### `template_comments`


**Documented default (Geeklog 2.2.2):** `false`
Controls whether internal template comments are preserved as HTML comments rather than removed. The 2.2.2 reference also describes extra template-path diagnostic output for `Root` users under specific template debugging settings. Avoid enabling diagnostic output on production sites.


## Cookies and sessions — Geeklog 2.2.2

These settings describe the historical [bundled 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html); they should be reviewed on a staging installation and must not be interpreted as current security defaults.

<a id="misc" name="misc"></a>
<a id="misc_cookies" name="misc_cookies"></a>

<a id="desc_cookie_session" name="desc_cookie_session"></a>

### `cookie_session`


**Documented default (Geeklog 2.2.2):** `gl_session`
Name of the cookie storing the session identifier; historical reference default `gl_session`.

<a id="desc_cookie_name" name="desc_cookie_name"></a>

### `cookie_name`


**Documented default (Geeklog 2.2.2):** `geeklog`
Name of the persistent site cookie; the 2.2.2 reference uses `geeklog`.

<a id="desc_cookie_password" name="desc_cookie_password"></a>

### `cookie_password`


**Documented default (Geeklog 2.2.2):** `password`
Name used for the historical password-related cookie. This describes a legacy configuration identifier, not a recommended modern credential-storage pattern.

<a id="desc_cookie_theme" name="desc_cookie_theme"></a>

### `cookie_theme`


**Documented default (Geeklog 2.2.2):** `theme`
Cookie name for the selected theme.

<a id="desc_cookie_language" name="desc_cookie_language"></a>

### `cookie_language`


**Documented default (Geeklog 2.2.2):** `language`
Cookie name for the selected language.

<a id="desc_cookie_tzid" name="desc_cookie_tzid"></a>

### `cookie_tzid`


**Documented default (Geeklog 2.2.2):** `timezone`
Cookie name used for the selected time zone.

<a id="desc_cookie_anon_name" name="desc_cookie_anon_name"></a>

### `cookie_anon_name`


**Documented default (Geeklog 2.2.2):** `anon_name`
Cookie name for the name supplied by an anonymous commenter.

<a id="desc_cookie_ip" name="desc_cookie_ip"></a>

### `cookie_ip`


**Documented default (Geeklog 2.2.2):** `0`
Legacy option for associating the session ID with the visitor's IP address. The 2.2.2 reference notes that enabling it can cause users whose IP changes to log in again; do not assume it replaces current session-security controls.

<a id="desc_default_perm_cookie_timeout" name="desc_default_perm_cookie_timeout"></a>

### `default_perm_cookie_timeout`


**Documented default (Geeklog 2.2.2):** `28800`
Default automatic-login cookie duration, in seconds; historical default `28800` (8 hours). The reference describes its interaction with `session_cookie_timeout`.

<a id="desc_session_cookie_timeout" name="desc_session_cookie_timeout"></a>

### `session_cookie_timeout`


**Documented default (Geeklog 2.2.2):** `7200`
Inactivity timeout for the session cookie, in seconds; historical default `7200` (2 hours), with reference bounds of 300 to 86400 seconds.

<a id="desc_cookie_path" name="desc_cookie_path"></a>

### `cookie_path`


**Documented default (Geeklog 2.2.2):** `/`
URL path scope for cookies, typically `/`.

<a id="desc_cookiedomain" name="desc_cookiedomain"></a>

### `cookiedomain`


**Documented default (Geeklog 2.2.2):** `(empty)`
Cookie domain scope. Geeklog's 2.2.2 reference says it attempts to derive the domain from `site_url`.

<a id="desc_cookiesecure" name="desc_cookiesecure"></a>

### `cookiesecure`


**Documented default (Geeklog 2.2.2):** `0`
Controls whether the Secure cookie flag is used. For HTTPS deployments, protect authentication cookies with an appropriate Secure setting; do not treat the old `0` default as security guidance.


## General functionality and diagnostics — Geeklog 2.2.2

These settings describe the historical [bundled 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html); they should be reviewed on a staging installation and must not be interpreted as current security defaults.

<a id="misc_misc" name="misc_misc"></a>

<a id="desc_notification" name="desc_notification"></a>

### `notification`


**Documented default (Geeklog 2.2.2):** `array()`
Selects administrative email notifications for submissions and account events. The 2.2.2 reference lists event keys `article`, `comment`, `trackback`, `pingback`, `user` and `user_update`.

<a id="desc_cron_schedule_interval" name="desc_cron_schedule_interval"></a>

### `cron_schedule_interval`


**Documented default (Geeklog 2.2.2):** `0`
Interval, in seconds, for Geeklog's visitor-triggered scheduled tasks; `0` disables. This internal mechanism depends on a homepage visit near the scheduled time, so lightly visited sites may run tasks late.

<a id="desc_disable_autolinks" name="desc_disable_autolinks"></a>

### `disable_autolinks`


**Documented default (Geeklog 2.2.2):** `0`
When enabled, stops interpreting Geeklog content autotags such as `[article:]`.

<a id="desc_clickable_links" name="desc_clickable_links"></a>

### `clickable_links`


**Documented default (Geeklog 2.2.2):** `true`
Controls automatic conversion of URLs in plaintext posts to clickable links.

<a id="desc_linktext_maxlen" name="desc_linktext_maxlen"></a>

### `linktext_maxlen`


**Documented default (Geeklog 2.2.2):** `50`
Maximum displayed URL text length for auto-linked URLs; `0` means unlimited in the 2.2.2 reference.

<a id="desc_compressed_output" name="desc_compressed_output"></a>

### `compressed_output`


**Documented default (Geeklog 2.2.2):** `false`
Experimental option to compress some HTML output when supported by browser and server. The bundled 2.2.2 reference states it is not implemented for all output.

<a id="desc_frame_options" name="desc_frame_options"></a>

### `frame_options`


**Documented default (Geeklog 2.2.2):** `DENY`
Controls the `X-Frame-Options` anti-clickjacking header. The 2.2.2 reference offers deny, same-origin and disabled modes. Disabling frame restrictions can expose pages to framing risks.

<a id="desc_page_navigation_max_pages" name="desc_page_navigation_max_pages"></a>

### `page_navigation_max_pages`


**Documented default (Geeklog 2.2.2):** `7`
Number of pagination links displayed on desktop; bundled default `7`, with permitted range from 3 to 20.

<a id="desc_page_navigation_mobile_max_pages" name="desc_page_navigation_mobile_max_pages"></a>

### `page_navigation_mobile_max_pages`


**Documented default (Geeklog 2.2.2):** `7`
Number of pagination links shown on mobile; bundled default `7`. Different desktop/mobile page counts may require separated mobile caching when template caching is enabled.

<a id="desc_default_cache_time_block" name="desc_default_cache_time_block"></a>

### `default_cache_time_block`


**Documented default (Geeklog 2.2.2):** `0`
Default block-cache policy: positive seconds specify a lifetime, `0` disables cache, and `-1` keeps cached content until the block is edited.

<a id="desc_titletoid" name="desc_titletoid"></a>

### `titletoid`


**Documented default (Geeklog 2.2.2):** `false`
Enables automatically deriving content identifiers from titles in supporting article, topic and Static Pages editors.

<a id="desc_404_log" name="desc_404_log"></a>

### `404_log`


**Documented default (Geeklog 2.2.2):** `true`
Controls logging of HTTP 404 errors into the `404.log` file in Geeklog's log directory.

<a id="misc_debug" name="misc_debug"></a>

<a id="desc_rootdebug" name="desc_rootdebug"></a>

### `rootdebug`


**Documented default (Geeklog 2.2.2):** `false`
If enabled, PHP error details may be shown to all visitors instead of only `Root` users. **Keep disabled on production** to avoid leaking private information.


## Daily digest options — Geeklog 2.2.2

These settings describe the historical [bundled 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html); they should be reviewed on a staging installation and must not be interpreted as current security defaults.

<a id="misc_digest" name="misc_digest"></a>

<a id="desc_emailstories" name="desc_emailstories"></a>

### `emailstories`


**Documented default (Geeklog 2.2.2):** `0`
Enables sending articles through Geeklog's legacy email digest feature; the 2.2.2 reference says it requires cron and PHP command-line execution.

<a id="desc_emailstorieslength" name="desc_emailstorieslength"></a>

### `emailstorieslength`


**Documented default (Geeklog 2.2.2):** `1`
When the digest is enabled, `0` sends titles and links, `1` sends full article introductions, and other numeric values limit the number of introduction characters.

<a id="desc_emailstoriesperdefault" name="desc_emailstoriesperdefault"></a>

### `emailstoriesperdefault`


**Documented default (Geeklog 2.2.2):** `0`
When enabled, newly registered accounts are automatically subscribed to the daily digest. Verify consent requirements before enabling.



## HTML filtering and safe content — Geeklog 2.2.2

Based on the [tagged configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Test behavior in a staging site before changing production settings, especially HTML filtering, permissions, uploads and external services.

<a id="misc_html" name="misc_html"></a>

<a id="desc_user_html" name="desc_user_html"></a>

### `user_html`


**Documented default (Geeklog 2.2.2):** `&lt;p&gt;, &lt;b&gt;, &lt;i&gt;, &lt;a&gt;, &lt;em&gt;, &lt;br&gt;, &lt;tt&gt;, &lt;hr&gt;, &lt;ol&gt;, &lt;ul&gt;, &lt;li&gt;, &lt;code&gt;, &lt;pre&gt;`
Allowed HTML tags and attributes for ordinary users in articles and comments. The 2.2.2 reference lists basic formatting tags; only add tags or attributes after considering script injection and unsafe URLs.

<a id="desc_admin_html" name="desc_admin_html"></a>

### `admin_html`


**Documented default (Geeklog 2.2.2):** `additional HTML tags, e.g. for tables`
Extra tags and attributes allowed for administrators, in addition to `user_html`. Defining a tag again here can replace the ordinary-user attribute definition.

<a id="desc_advanced_html" name="desc_advanced_html"></a>

### `advanced_html`


**Documented default (Geeklog 2.2.2):** `additional HTML tags for use with the Advanced Editor, e.g. for images`
Additional HTML tags and attributes permitted when the advanced rich-text editor is used. Review these allowances for unsafe markup.

<a id="desc_skip_html_filter_for_root" name="desc_skip_html_filter_for_root"></a>

### `skip_html_filter_for_root`


**Documented default (Geeklog 2.2.2):** `0`
When enabled, `Root` members may bypass HTML filtering for their content. This is a security-sensitive option; keep filtering unless the risks have been evaluated.

<a id="desc_allowed_protocols" name="desc_allowed_protocols"></a>

### `allowed_protocols`


**Documented default (Geeklog 2.2.2):** `array ('http', 'https', 'ftp');`
List of URL schemes allowed in HTML links. The 2.2.2 reference includes `http`, `https` and `ftp`; avoid untrusted executable schemes.


## Content censoring and IP lookup — Geeklog 2.2.2

Based on the [tagged configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Test behavior in a staging site before changing production settings, especially HTML filtering, permissions, uploads and external services.

<a id="misc_censoring" name="misc_censoring"></a>

<a id="desc_censormode" name="desc_censormode"></a>

### `censormode`


**Documented default (Geeklog 2.2.2):** `1`
Controls word filtering: `0` disabled, `1` exact match, `2` word-start match and `3` substring match in the 2.2.2 reference.

<a id="desc_censorreplace" name="desc_censorreplace"></a>

### `censorreplace`


**Documented default (Geeklog 2.2.2):** `*censored*`
Text substituted for censored words; historically `*censored*`. The legacy filter may fail to detect words interrupted by HTML or BBCode markup.

<a id="desc_censorlist" name="desc_censorlist"></a>

### `censorlist`


**Documented default (Geeklog 2.2.2):** `array( a list of "bad" words goes here ... )`
List of terms checked by the censoring facility. Test false positives and the actual filter implementation before deployment.

<a id="misc_ip_lookup" name="misc_ip_lookup"></a>

<a id="desc_ip_lookup" name="desc_ip_lookup"></a>

### `ip_lookup`


**Documented default (Geeklog 2.2.2):** `(disabled)`
Optional external IP lookup URL for administrative review of comment poster IPs. The historical setting uses `*` as the substitution marker; consider visitor privacy before sending an address to a third-party service.


## Webservices API controls — Geeklog 2.2.2

Based on the [tagged configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Test behavior in a staging site before changing production settings, especially HTML filtering, permissions, uploads and external services.

<a id="misc_ip_webservices" name="misc_ip_webservices"></a>

<a id="desc_disable_webservices" name="desc_disable_webservices"></a>

### `disable_webservices`


**Documented default (Geeklog 2.2.2):** `false`
Setting `true` disables the Geeklog webservices facility in the 2.2.2 reference.

<a id="desc_restrict_webservices" name="desc_restrict_webservices"></a>

### `restrict_webservices`


**Documented default (Geeklog 2.2.2):** `false`
When enabled, limits webservices access to users with the `webservices.atompub` permission, such as a properly configured Webservices Users group.

<a id="desc_atom_max_stories" name="desc_atom_max_stories"></a>

### `atom_max_stories`


**Documented default (Geeklog 2.2.2):** `10`
Maximum number of articles returned by an Atom webservices feed request; documented default `10`.


## Topic breadcrumb controls — Geeklog 2.2.2

Based on the [tagged configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Test behavior in a staging site before changing production settings, especially HTML filtering, permissions, uploads and external services.

<a id="misc_topics" name="misc_topics"></a>

<a id="desc_multiple_breadcrumbs" name="desc_multiple_breadcrumbs"></a>

### `multiple_breadcrumbs`


**Documented default (Geeklog 2.2.2):** `false`
Show more than one breadcrumb trail when available.

<a id="desc_disable_breadcrumbs_topics" name="desc_disable_breadcrumbs_topics"></a>

### `disable_breadcrumbs_topics`


**Documented default (Geeklog 2.2.2):** `false`
Suppress breadcrumbs associated with topic pages when enabled.

<a id="desc_disable_breadcrumbs_articles" name="desc_disable_breadcrumbs_articles"></a>

### `disable_breadcrumbs_articles`


**Documented default (Geeklog 2.2.2):** `false`
Suppress breadcrumbs associated with article pages when enabled.

<a id="desc_disable_breadcrumbs_plugins" name="desc_disable_breadcrumbs_plugins"></a>

### `disable_breadcrumbs_plugins`


**Documented default (Geeklog 2.2.2):** `false`
Suppress breadcrumbs generated by plugins when enabled.

<a id="desc_breadcrumb_root_site_name" name="desc_breadcrumb_root_site_name"></a>

### `breadcrumb_root_site_name`


**Documented default (Geeklog 2.2.2):** `false`
Display the site name as the root entry of breadcrumb navigation when enabled.


## File manager — display and server behavior — Geeklog 2.2.2

Based on the [tagged configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Test behavior in a staging site before changing production settings, especially HTML filtering, permissions, uploads and external services.

<a id="filemanager" name="filemanager"></a>
<a id="filemanager_general" name="filemanager_general"></a>

<a id="desc_filemanager_disabled" name="desc_filemanager_disabled"></a>

### `filemanager_disabled`


**Documented default (Geeklog 2.2.2):** `false`
When set to `true`, disables the Filemanager feature for ordinary users. The tagged 2.2.2 reference explicitly states that members of the `Root` group can still use it. Verify effective permissions on the installed site; this setting alone is not a complete access-control policy.

<a id="desc_filemanager_browse_only" name="desc_filemanager_browse_only"></a>

### `filemanager_browse_only`


**Documented default (Geeklog 2.2.2):** `false`
Enable read-only browsing in the file manager.

<a id="desc_filemanager_default_view_mode" name="desc_filemanager_default_view_mode"></a>

### `filemanager_default_view_mode`


**Documented default (Geeklog 2.2.2):** `grid`
Default file manager layout: `grid` or `list`.

<a id="desc_filemanager_show_confirmation" name="desc_filemanager_show_confirmation"></a>

### `filemanager_show_confirmation`


**Documented default (Geeklog 2.2.2):** `true`
Show a confirmation message for file manager operations when enabled.

<a id="desc_filemanager_search_box" name="desc_filemanager_search_box"></a>

### `filemanager_search_box`


**Documented default (Geeklog 2.2.2):** `true`
Show the file manager search field when enabled.

<a id="desc_filemanager_file_sorting" name="desc_filemanager_file_sorting"></a>

### `filemanager_file_sorting`


**Documented default (Geeklog 2.2.2):** `default`
File/folder sorting by name, type or modification date, each ascending or descending.

<a id="desc_filemanager_chars_only_latin" name="desc_filemanager_chars_only_latin"></a>

### `filemanager_chars_only_latin`


**Documented default (Geeklog 2.2.2):** `true`
Control whether non-Latin characters are allowed in folder names. Verify the exact boolean interpretation before changing this historic option.

<a id="desc_filemanager_date_format" name="desc_filemanager_date_format"></a>

### `filemanager_date_format`


**Documented default (Geeklog 2.2.2):** `yMMMdHm`
Format of dates shown in the file manager; the bundled default uses `yMMMdHm`.

<a id="desc_filemanager_logger" name="desc_filemanager_logger"></a>

### `filemanager_logger`


**Documented default (Geeklog 2.2.2):** `false`
Log file manager server-side actions in Geeklog's error log when enabled. Avoid exposing sensitive file paths in public logs.

<a id="desc_filemanager_show_thumbs" name="desc_filemanager_show_thumbs"></a>

### `filemanager_show_thumbs`


**Documented default (Geeklog 2.2.2):** `true`
Show thumbnails of supported files when enabled.

<a id="desc_filemanager_generate_thumbnails" name="desc_filemanager_generate_thumbnails"></a>

### `filemanager_generate_thumbnails`


**Documented default (Geeklog 2.2.2):** `true`
Generate thumbnail images using PHP for faster directory browsing. The reference places them in an internal `_thumbs` directory.


## File manager — uploads and media — Geeklog 2.2.2

Based on the [tagged configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Test behavior in a staging site before changing production settings, especially HTML filtering, permissions, uploads and external services.

<a id="filemanager_upload" name="filemanager_upload"></a>

<a id="desc_filemanager_upload_overwrite" name="desc_filemanager_upload_overwrite"></a>

### `filemanager_upload_overwrite`


**Documented default (Geeklog 2.2.2):** `false`
Overwrite an existing file with the same name when enabled; otherwise append an index to the uploaded filename. Review permissions before enabling overwrites.

<a id="desc_filemanager_upload_file_size_limit" name="desc_filemanager_upload_file_size_limit"></a>

### `filemanager_upload_file_size_limit`


**Documented default (Geeklog 2.2.2):** `16`
Maximum upload size checked by the HTML5 client and PHP connector, in MiB; bundled default `16`. Server-side PHP limits may further restrict uploads.

<a id="filemanager_images" name="filemanager_images"></a>

<a id="desc_filemanager_images_ext" name="desc_filemanager_images_ext"></a>

### `filemanager_images_ext`


**Documented default (Geeklog 2.2.2):** `'jpg', 'jpeg', 'gif', 'png', 'svg'`
Allowed image filename extensions in the file manager; the 2.2.2 reference lists `jpg`, `jpeg`, `gif`, `png` and `svg`. Extension checks alone are not sufficient file-content validation.

<a id="filemanager_videos" name="filemanager_videos"></a>

<a id="desc_filemanager_show_video_player" name="desc_filemanager_show_video_player"></a>

### `filemanager_show_video_player`


**Documented default (Geeklog 2.2.2):** `true`
Show the browser-based video player for supported video files.

<a id="desc_filemanager_videos_ext" name="desc_filemanager_videos_ext"></a>

### `filemanager_videos_ext`


**Documented default (Geeklog 2.2.2):** `'ogv', 'mp4', 'webm'`
Video filename extensions supported by the built-in player; the 2.2.2 reference lists `ogv`, `mp4`, `webm`.

<a id="desc_filemanager_videos_player_width" name="desc_filemanager_videos_player_width"></a>

### `filemanager_videos_player_width`


**Documented default (Geeklog 2.2.2):** `400`
Width in pixels for the embedded video player; historical default `400`.

<a id="desc_filemanager_videos_player_height" name="desc_filemanager_videos_player_height"></a>

### `filemanager_videos_player_height`


**Documented default (Geeklog 2.2.2):** `222`
Height in pixels for the embedded video player; historical default `222`.

<a id="filemanager_audios" name="filemanager_audios"></a>

<a id="desc_filemanager_show_audio_player" name="desc_filemanager_show_audio_player"></a>

### `filemanager_show_audio_player`


**Documented default (Geeklog 2.2.2):** `true`
Show the browser-based audio player for supported audio files.

<a id="desc_filemanager_audios_ext" name="desc_filemanager_audios_ext"></a>

### `filemanager_audios_ext`


**Documented default (Geeklog 2.2.2):** `'ogg', 'mp3', 'wav'`
Audio filename extensions recognized by the player; the 2.2.2 reference lists `ogg`, `mp3` and `wav`.


## Default content permissions and autotag access — Geeklog 2.2.2

The following 44 help identifiers describe the **defaults** for content permissions and autotag usage in the [bundled Geeklog 2.2.2 reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html#misc_permissions). They are not recommendations to grant public users broader rights. Review effective group permissions and test with least-privileged accounts before changing production.

The suffixes `_0`, `_1`, `_2` and `_3` refer to distinct audience/role positions recorded by the original configuration page. Do not infer access solely from a setting name; the actual group and operation are important.

### Default permissions at a glance

The following values are taken from the Geeklog **2.2.2 bundled configuration reference**, for **new content**. They are not the effective permissions of existing articles, topics or blocks.

| New content | Owner (`_0`) | Group (`_1`) | Logged-in users (`_2`) | Anonymous visitors (`_3`) |
| --- | --- | --- | --- | --- |
| Articles (`story`) | Read-Write | Read-Only | Read-Only | Read-Only |
| Topics (`topic`) | Read-Write | Read-Only | Read-Only | Read-Only |
| Blocks (`block`) | Read-Write | Read-Only | Read-Only | Read-Only |

For these defaults, **Read-Only permits viewing but not editing**. A new item's effective access also depends on its assigned owner/group and the permissions saved for that item. If public access is not intended, review the `_3` settings **before** creating new content and test anonymous requests on a staging site. Changes to a default must not be assumed to retroactively modify existing records.

Autotag `Use` permissions are distinct from content `Read-Write` permissions: being allowed to use an autotag does **not** in itself authorize modifying the referenced content. Each autotag family and audience has its own defaults documented below.

### Autotag usage permissions at a glance

These are the **32 historical documented defaults** in Geeklog 2.2.2. The group column refers to the autotag's assigned administration group, which differs across families (Article Admin, User Admin, Topic Admin, Block Admin or Root). It is **not** a generic group permission. The `structureddata` Root Group exception is explained in its individual setting below.

| Autotag family | Owner (`_0`) | Assigned group (`_1`) | Logged-in users (`_2`) | Anonymous visitors (`_3`) |
| --- | --- | --- | --- | --- |
| `story` | Use | Use | Use | Use |
| `user` | Use | Use | Use | Use |
| `topic` | Use | Use | Use | Use |
| `related_topics` | Use | Use | No Access | No Access |
| `related_items` | Use | Use | No Access | No Access |
| `block` | Use | Use | No Access | No access |
| `structureddata` | Use | Use | No Access | No access |
| `likes_block` | Use | Use | No Access | No Access |

`Use` and `No Access` are the exact *documented* 2.2.2 labels (including the original capitalization of `No access` for two cells). They do not independently prove that an autotag is registered, that the referenced content is visible, or that a current installation enforces the same access. For structured-data autotags, the historic reference says the Root Group retains access regardless of changing its default and mentions the `structureddata.autotag` feature for other security groups. Test actual rendering and authorization with accounts of different roles before deployment.

<a id="misc_permissions" name="misc_permissions"></a>

<a id="desc_default_permissions_story_0" name="desc_default_permissions_story_0"></a>

### `default_permissions_story_0`


**Documented default (Geeklog 2.2.2):** `Read-Write`
**Bundled default:** Read-Write. Default permission for Owner of new articles. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_story_1" name="desc_default_permissions_story_1"></a>

### `default_permissions_story_1`


**Documented default (Geeklog 2.2.2):** `Read-Only`
**Bundled default:** Read-Only. Default permission for Group of new articles. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_story_2" name="desc_default_permissions_story_2"></a>

### `default_permissions_story_2`


**Documented default (Geeklog 2.2.2):** `Read-Only`
**Bundled default:** Read-Only. Default permission for all logged in users of new articles. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_story_3" name="desc_default_permissions_story_3"></a>

### `default_permissions_story_3`


**Documented default (Geeklog 2.2.2):** `Read-Only`
**Bundled default:** Read-Only. Default permission for all anonymous visitors of new articles. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_topic_0" name="desc_default_permissions_topic_0"></a>

### `default_permissions_topic_0`


**Documented default (Geeklog 2.2.2):** `Read-Write`
**Bundled default:** Read-Write. Default permission for Owner of new topics. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_topic_1" name="desc_default_permissions_topic_1"></a>

### `default_permissions_topic_1`


**Documented default (Geeklog 2.2.2):** `Read-Only`
**Bundled default:** Read-Only. Default permission for Group of new topics. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_topic_2" name="desc_default_permissions_topic_2"></a>

### `default_permissions_topic_2`


**Documented default (Geeklog 2.2.2):** `Read-Only`
**Bundled default:** Read-Only. Default permission for all logged in users of new topics. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_topic_3" name="desc_default_permissions_topic_3"></a>

### `default_permissions_topic_3`


**Documented default (Geeklog 2.2.2):** `Read-Only`
**Bundled default:** Read-Only. Default permission for all anonymous visitors of new topics. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_block_0" name="desc_default_permissions_block_0"></a>

### `default_permissions_block_0`


**Documented default (Geeklog 2.2.2):** `Read-Write`
**Bundled default:** Read-Write. Default permission for Owner of new blocks. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_block_1" name="desc_default_permissions_block_1"></a>

### `default_permissions_block_1`


**Documented default (Geeklog 2.2.2):** `Read-Only`
**Bundled default:** Read-Only. Default permission for Group of new blocks. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_block_2" name="desc_default_permissions_block_2"></a>

### `default_permissions_block_2`


**Documented default (Geeklog 2.2.2):** `Read-Only`
**Bundled default:** Read-Only. Default permission for all logged in users of new blocks. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_block_3" name="desc_default_permissions_block_3"></a>

### `default_permissions_block_3`


**Documented default (Geeklog 2.2.2):** `Read-Only`
**Bundled default:** Read-Only. Default permission for all anonymous users of new blocks. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_story_0" name="desc_autotag_permissions_story_0"></a>

### `autotag_permissions_story_0`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by autotag Owner (Default Root User). This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_story_1" name="desc_autotag_permissions_story_1"></a>

### `autotag_permissions_story_1`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by Article Admin Group. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_story_2" name="desc_autotag_permissions_story_2"></a>

### `autotag_permissions_story_2`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by all logged in users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_story_3" name="desc_autotag_permissions_story_3"></a>

### `autotag_permissions_story_3`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by anonymous users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_user_0" name="desc_autotag_permissions_user_0"></a>

### `autotag_permissions_user_0`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by autotag Owner (Default Root User). This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_user_1" name="desc_autotag_permissions_user_1"></a>

### `autotag_permissions_user_1`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by User Admin Group. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_user_2" name="desc_autotag_permissions_user_2"></a>

### `autotag_permissions_user_2`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by all logged in users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_user_3" name="desc_autotag_permissions_user_3"></a>

### `autotag_permissions_user_3`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by anonymous users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_topic_0" name="desc_autotag_permissions_topic_0"></a>

### `autotag_permissions_topic_0`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by autotag Owner (Default Root User). This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_topic_1" name="desc_autotag_permissions_topic_1"></a>

### `autotag_permissions_topic_1`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by Topic Admin Group. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_topic_2" name="desc_autotag_permissions_topic_2"></a>

### `autotag_permissions_topic_2`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by all logged in users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_topic_3" name="desc_autotag_permissions_topic_3"></a>

### `autotag_permissions_topic_3`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by anonymous users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_related_topics_0" name="desc_autotag_permissions_related_topics_0"></a>

### `autotag_permissions_related_topics_0`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by autotag Owner (Default Root User). This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_related_topics_1" name="desc_autotag_permissions_related_topics_1"></a>

### `autotag_permissions_related_topics_1`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by Topic Admin Group. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_related_topics_2" name="desc_autotag_permissions_related_topics_2"></a>

### `autotag_permissions_related_topics_2`


**Documented default (Geeklog 2.2.2):** `No Access`
**Bundled default:** No Access. Usage permission for autotag by all logged in users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_related_topics_3" name="desc_autotag_permissions_related_topics_3"></a>

### `autotag_permissions_related_topics_3`


**Documented default (Geeklog 2.2.2):** `No Access`
**Bundled default:** No Access. Usage permission for autotag by anonymous users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_related_items_0" name="desc_autotag_permissions_related_items_0"></a>

### `autotag_permissions_related_items_0`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by autotag Owner (Default Root User). This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_related_items_1" name="desc_autotag_permissions_related_items_1"></a>

### `autotag_permissions_related_items_1`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by Topic Admin Group. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_related_items_2" name="desc_autotag_permissions_related_items_2"></a>

### `autotag_permissions_related_items_2`


**Documented default (Geeklog 2.2.2):** `No Access`
**Bundled default:** No Access. Usage permission for autotag by all logged in users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_related_items_3" name="desc_autotag_permissions_related_items_3"></a>

### `autotag_permissions_related_items_3`


**Documented default (Geeklog 2.2.2):** `No Access`
**Bundled default:** No Access. Usage permission for autotag by anonymous users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_block_0" name="desc_autotag_permissions_block_0"></a>

### `autotag_permissions_block_0`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by autotag Owner (Default Root User). This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_block_1" name="desc_autotag_permissions_block_1"></a>

### `autotag_permissions_block_1`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by Block Admin Group. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_block_2" name="desc_autotag_permissions_block_2"></a>

### `autotag_permissions_block_2`


**Documented default (Geeklog 2.2.2):** `No Access`
**Bundled default:** No Access. Usage permission for autotag by all logged in users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_block_3" name="desc_autotag_permissions_block_3"></a>

### `autotag_permissions_block_3`


**Documented default (Geeklog 2.2.2):** `No access`
**Bundled default:** No access. Usage permission for autotag by anonymous users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_structureddata_0" name="desc_autotag_permissions_structureddata_0"></a>

### `autotag_permissions_structureddata_0`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by autotag Owner (Default Root User). This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_structureddata_1" name="desc_autotag_permissions_structureddata_1"></a>

### `autotag_permissions_structureddata_1`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by Root Group. Please note, changing this will not affect permissions since the Root Group automatically has access to everything. To give usage permissions for this autotag to other Security Groups, assign them the feature structureddata.autotag . This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_structureddata_2" name="desc_autotag_permissions_structureddata_2"></a>

### `autotag_permissions_structureddata_2`


**Documented default (Geeklog 2.2.2):** `No Access`
**Bundled default:** No Access. Usage permission for autotag by all logged in users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_structureddata_3" name="desc_autotag_permissions_structureddata_3"></a>

### `autotag_permissions_structureddata_3`


**Documented default (Geeklog 2.2.2):** `No access`
**Bundled default:** No access. Usage permission for autotag by anonymous users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_likes_block_0" name="desc_autotag_permissions_likes_block_0"></a>

### `autotag_permissions_likes_block_0`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by autotag Owner (Default Root User). This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_likes_block_1" name="desc_autotag_permissions_likes_block_1"></a>

### `autotag_permissions_likes_block_1`


**Documented default (Geeklog 2.2.2):** `Use`
**Bundled default:** Use. Usage permission for autotag by Blocks Admin Group. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_likes_block_2" name="desc_autotag_permissions_likes_block_2"></a>

### `autotag_permissions_likes_block_2`


**Documented default (Geeklog 2.2.2):** `No Access`
**Bundled default:** No Access. Usage permission for autotag by all logged in users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_likes_block_3" name="desc_autotag_permissions_likes_block_3"></a>

### `autotag_permissions_likes_block_3`


**Documented default (Geeklog 2.2.2):** `No Access`
**Bundled default:** No Access. Usage permission for autotag by anonymous users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.



## Articles — structured data and related content — Geeklog 2.2.2

Version-scoped documentation adapted from the [tagged Geeklog configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Do not assume historical external identity or ping services remain supported.

<a id="desc_structured_data_type_default" name="desc_structured_data_type_default"></a>

### `structured_data_type_default`


**Documented default (Geeklog 2.2.2):** `'core-article'`
Selects the default structured-data type for new articles. The 2.2.2 reference offers `none`, `core-webpage`, `core-article`, `core-newsarticle`, and `core-blogposting`. Full-article pages may expose JSON-LD; validate actual markup before release.

<a id="desc_structured_data_article_topic" name="desc_structured_data_article_topic"></a>

### `structured_data_article_topic`


**Documented default (Geeklog 2.2.2):** `0`
Controls whether article structured data is included on home/topic listings as well as full article pages; the historical reference describes `1` enabled and `0` disabled.

<a id="desc_aftersave_story" name="desc_aftersave_story"></a>

### `aftersave_story`


**Documented default (Geeklog 2.2.2):** `'list'`
Where a Story Admin is redirected after saving an article: `item` displays the article, `list` shows the admin article list (the default), `home` goes to the site's homepage, and `admin` opens **Admin Home (Command & Control)**. The 2.2.2 reference explicitly excludes **article submissions**: editing a queued submission returns to the submission queue regardless of this setting. Verify actual navigation in staging before replacing the bundled help.

<a id="desc_related_topics" name="desc_related_topics"></a>

### `related_topics`


**Documented default (Geeklog 2.2.2):** `1`
Controls whether related topics are shown on articles, article and topic pages, or neither; verify exact choices in the installed configuration UI.

<a id="desc_related_topics_max" name="desc_related_topics_max"></a>

### `related_topics_max`


**Documented default (Geeklog 2.2.2):** `6`
Maximum number of related topics to display; `0` means no limit.

<a id="desc_whats_related" name="desc_whats_related"></a>

### `whats_related`


**Documented default (Geeklog 2.2.2):** `1`
Controls the What's Related block on article pages, including filtering of internal/external article links.

<a id="desc_whats_related_max" name="desc_whats_related_max"></a>

### `whats_related_max`


**Documented default (Geeklog 2.2.2):** `0`
Maximum number of related links displayed on an article; `0` requests all available items, with a minimum of two items for display in the historical reference.

<a id="desc_whats_related_trim" name="desc_whats_related_trim"></a>

### `whats_related_trim`


**Documented default (Geeklog 2.2.2):** `26`
Maximum displayed length of related-item titles. A value of `0` disables truncation; changing the option can rebuild stored related links.

<a id="desc_default_cache_time_article" name="desc_default_cache_time_article"></a>

### `default_cache_time_article`


**Documented default (Geeklog 2.2.2):** `0`
Default article cache policy: positive seconds for an expiry, `0` to regenerate for each request, or `-1` to keep the cached article until it is edited.

<a id="desc_blocks_article_topic_list_repeat_after" name="desc_blocks_article_topic_list_repeat_after"></a>

### `blocks_article_topic_list_repeat_after`


**Documented default (Geeklog 2.2.2):** `1`
Number of article introductions after which the Article Topic List block location repeats; `0` disables that block placement.


## Trackbacks and pingbacks — legacy integration — Geeklog 2.2.2

Version-scoped documentation adapted from the [tagged Geeklog configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Do not assume historical external identity or ping services remain supported.

<a id="stories_trackback" name="stories_trackback"></a>

<a id="desc_trackback_enabled" name="desc_trackback_enabled"></a>

### `trackback_enabled`


**Documented default (Geeklog 2.2.2):** `true`
Controls **both sending and receiving trackback comments**. The tagged 2.2.2 reference contains a typo, saying both "enable" and "disable" use `true`; the documented default is `true`. Verify the actual runtime behavior and external exposure before changing this historic feature. The contradictory wording must not be copied as configuration advice.

<a id="desc_trackback_code" name="desc_trackback_code"></a>

### `trackback_code`


**Documented default (Geeklog 2.2.2):** `0`
Default setting for new articles: `0` accepts trackbacks, `-1` disables them.

<a id="desc_trackbackspeedlimit" name="desc_trackbackspeedlimit"></a>

### `trackbackspeedlimit`


**Documented default (Geeklog 2.2.2):** `300`
Minimum number of seconds between trackbacks or pingbacks originating from the same IP address; historical default `300`.

<a id="desc_check_trackback_link" name="desc_check_trackback_link"></a>

### `check_trackback_link`


**Documented default (Geeklog 2.2.2):** `2`
Selects anti-spam validation of incoming trackbacks, including backlink presence and possibly sender IP checks. Check the exact option modes in the tagged source before relying on the protection.

<a id="desc_multiple_trackbacks" name="desc_multiple_trackbacks"></a>

### `multiple_trackbacks`


**Documented default (Geeklog 2.2.2):** `0`
Handling repeated trackbacks/pingbacks from a source: `0` keep the first, `1` replace with the latest, `2` allow multiple.

<a id="stories_pingback" name="stories_pingback"></a>

<a id="desc_pingback_enabled" name="desc_pingback_enabled"></a>

### `pingback_enabled`


**Documented default (Geeklog 2.2.2):** `true`
Enables or disables sending and receiving pingbacks; the original description contains an apparent boolean typo.

<a id="desc_pingback_excerpt" name="desc_pingback_excerpt"></a>

### `pingback_excerpt`


**Documented default (Geeklog 2.2.2):** `true`
When enabled, Geeklog attempts to retrieve the linking page and extract an excerpt for a pingback, since pingbacks do not transmit one themselves.

<a id="desc_pingback_self" name="desc_pingback_self"></a>

### `pingback_self`


**Documented default (Geeklog 2.2.2):** `0`
Controls processing of pingbacks that point to other pages on the same site; the historical source documents `0` as skipping these.

<a id="desc_ping_enabled" name="desc_ping_enabled"></a>

### `ping_enabled`


**Documented default (Geeklog 2.2.2):** `true`
Enables sending notifications to historical weblog-directory ping services; availability of old external services is not guaranteed.


## User registration, identity and profile options — Geeklog 2.2.2

Version-scoped documentation adapted from the [tagged Geeklog configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Do not assume historical external identity or ping services remain supported.

<a id="users" name="users"></a>
<a id="users_users" name="users_users"></a>

<a id="desc_disable_new_user_registration" name="desc_disable_new_user_registration"></a>

### `disable_new_user_registration`


**Documented default (Geeklog 2.2.2):** `false`
Set to `true` to disable all new-user signup paths in Geeklog 2.2.2 (default `false`). This is broader than requiring registration approval through `usersubmission`; it prevents new registrations entirely.

<a id="desc_allow_user_themes" name="desc_allow_user_themes"></a>

### `allow_user_themes`


**Documented default (Geeklog 2.2.2):** `1`
Allows registered users to select a site theme in their account preferences when enabled.

<a id="desc_allow_user_photo" name="desc_allow_user_photo"></a>

### `allow_user_photo`


**Documented default (Geeklog 2.2.2):** `1`
Allows users to upload a profile photograph when enabled.

<a id="desc_allow_username_change" name="desc_allow_username_change"></a>

### `allow_username_change`


**Documented default (Geeklog 2.2.2):** `0`
Set to `1` to allow account holders to change their login username; the documented default is `0`. The 2.2.2 reference states that existing article and comment bylines automatically show the new username after a change.

<a id="desc_allow_account_delete" name="desc_allow_account_delete"></a>

### `allow_account_delete`


**Documented default (Geeklog 2.2.2):** `0`
Set to `1` to allow users to delete their own accounts; the documented default is `0` (not allowed). The 2.2.2 reference states that the user's previously posted articles and comments remain on the site and are attributed to `Anonymous`. Account deletion therefore does not erase previously submitted content; review retention and privacy obligations separately.

<a id="desc_hide_author_exclusion" name="desc_hide_author_exclusion"></a>

### `hide_author_exclusion`


**Documented default (Geeklog 2.2.2):** `0`
Hides the preference for excluding selected authors' content from a user's view.

<a id="desc_show_fullname" name="desc_show_fullname"></a>

### `show_fullname`


**Documented default (Geeklog 2.2.2):** `0`
Controls whether an account's full name is shown instead of its username; the username is used when no full name is supplied.

<a id="desc_require_user_email" name="desc_require_user_email"></a>

### `require_user_email`


**Documented default (Geeklog 2.2.2):** `true`
Requires accounts lacking an email address to provide and verify one before continued authenticated use; remote login providers may not supply email.

<a id="desc_show_servicename" name="desc_show_servicename"></a>

### `show_servicename`


**Documented default (Geeklog 2.2.2):** `true`
Appends a remote authentication service identifier to a username, helping distinguish local and remotely authenticated accounts.

<a id="desc_custom_registration" name="desc_custom_registration"></a>

### `custom_registration`


**Documented default (Geeklog 2.2.2):** `false`
Set to `true` to use a site-specific new-user registration form. The tagged Geeklog 2.2.2 source refers to the bundled `lib-custom.php` as an implementation example. A custom registration form is site code and should be reviewed for validation, authorization and updates before enabling.

<a id="desc_user_login_method_standard" name="desc_user_login_method_standard"></a>

### `user_login_method_standard`


**Documented default (Geeklog 2.2.2):** `true`
Controls login by a local Geeklog account stored in the site's database.

<a id="desc_user_login_method_openid" name="desc_user_login_method_openid"></a>

### `user_login_method_openid`


**Documented default (Geeklog 2.2.2):** `false`
Enables the historical OpenID login integration. The 2.2.2 reference notes that account approval queues can disable this login path. Compatibility with today's identity providers is unverified.

<a id="desc_user_login_method_3rdparty" name="desc_user_login_method_3rdparty"></a>

### `user_login_method_3rdparty`


**Documented default (Geeklog 2.2.2):** `false`
Enables external account authentication, including the historical LDAP integration, where the provider and necessary authorization settings are configured.

<a id="desc_user_login_method_oauth" name="desc_user_login_method_oauth"></a>

### `user_login_method_oauth`


**Documented default (Geeklog 2.2.2):** `false`
Enables the built-in legacy OAuth login methods. This 2.2.2 feature is **not proof of compatibility with current provider APIs**; test each connection with up-to-date credentials and endpoints.

<a id="desc_aftersave_user" name="desc_aftersave_user"></a>

### `aftersave_user`


**Documented default (Geeklog 2.2.2):** `'item'`
Administrator destination after saving a user record: `item`, `list`, `home`, or `admin`, as listed by the original reference.

<a id="users_spamx" name="users_spamx"></a>

<a id="desc_spamx" name="desc_spamx"></a>

### `spamx`


**Documented default (Geeklog 2.2.2):** `128`
Bitmask selecting actions that the Spam-X plugin runs when spam is detected. The 2.2.2 reference documents `128` for its delete action; inspect installed plugin modules before combining bit flags.



## Historic OAuth provider settings — Geeklog 2.2.2

These descriptions are scoped to the [versioned source reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Provider integrations and bootstrap settings need separate operational checks before a live change.

<a id="desc_google_login" name="desc_google_login"></a>

### `google_login`


**Documented default (Geeklog 2.2.2):** `false`
Enables the historical Google OAuth login integration when supported by the specific Geeklog 2.2.2 configuration and an authorized provider application. **Do not assume compatibility with the provider's present-day OAuth APIs**; verify endpoints, callback URL, scopes and the installed login implementation.

<a id="desc_google_consumer_key" name="desc_google_consumer_key"></a>

### `google_consumer_key`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Application/client identifier for the historical Google login integration. Configure it through the administrator's secure settings, not in published documentation or debug logs.

<a id="desc_google_consumer_secret" name="desc_google_consumer_secret"></a>

### `google_consumer_secret`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Application/client secret for the historical Google login integration. Keep it private and rotate if exposed; do not include actual secrets in examples or commits.

<a id="desc_facebook_login" name="desc_facebook_login"></a>

### `facebook_login`


**Documented default (Geeklog 2.2.2):** `false`
Enables the historical Facebook OAuth login integration when supported by the specific Geeklog 2.2.2 configuration and an authorized provider application. **Do not assume compatibility with the provider's present-day OAuth APIs**; verify endpoints, callback URL, scopes and the installed login implementation.

<a id="desc_facebook_consumer_key" name="desc_facebook_consumer_key"></a>

### `facebook_consumer_key`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Application/client identifier for the historical Facebook login integration. Configure it through the administrator's secure settings, not in published documentation or debug logs.

<a id="desc_facebook_consumer_secret" name="desc_facebook_consumer_secret"></a>

### `facebook_consumer_secret`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Application/client secret for the historical Facebook login integration. Keep it private and rotate if exposed; do not include actual secrets in examples or commits.

<a id="desc_linkedin_login" name="desc_linkedin_login"></a>

### `linkedin_login`


**Documented default (Geeklog 2.2.2):** `false`
Enables the historical Linkedin OAuth login integration when supported by the specific Geeklog 2.2.2 configuration and an authorized provider application. **Do not assume compatibility with the provider's present-day OAuth APIs**; verify endpoints, callback URL, scopes and the installed login implementation.

<a id="desc_linkedin_consumer_key" name="desc_linkedin_consumer_key"></a>

### `linkedin_consumer_key`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Application/client identifier for the historical Linkedin login integration. Configure it through the administrator's secure settings, not in published documentation or debug logs.

<a id="desc_linkedin_consumer_secret" name="desc_linkedin_consumer_secret"></a>

### `linkedin_consumer_secret`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Application/client secret for the historical Linkedin login integration. Keep it private and rotate if exposed; do not include actual secrets in examples or commits.

<a id="desc_twitter_login" name="desc_twitter_login"></a>

### `twitter_login`


**Documented default (Geeklog 2.2.2):** `false`
Enables the historical Twitter OAuth login integration when supported by the specific Geeklog 2.2.2 configuration and an authorized provider application. **Do not assume compatibility with the provider's present-day OAuth APIs**; verify endpoints, callback URL, scopes and the installed login implementation.

<a id="desc_twitter_consumer_key" name="desc_twitter_consumer_key"></a>

### `twitter_consumer_key`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Application/client identifier for the historical Twitter login integration. Configure it through the administrator's secure settings, not in published documentation or debug logs.

<a id="desc_twitter_consumer_secret" name="desc_twitter_consumer_secret"></a>

### `twitter_consumer_secret`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Application/client secret for the historical Twitter login integration. Keep it private and rotate if exposed; do not include actual secrets in examples or commits.

<a id="desc_microsoft_login" name="desc_microsoft_login"></a>

### `microsoft_login`


**Documented default (Geeklog 2.2.2):** `false`
Enables the historical Microsoft OAuth login integration when supported by the specific Geeklog 2.2.2 configuration and an authorized provider application. **Do not assume compatibility with the provider's present-day OAuth APIs**; verify endpoints, callback URL, scopes and the installed login implementation.

<a id="desc_microsoft_consumer_key" name="desc_microsoft_consumer_key"></a>

### `microsoft_consumer_key`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Application/client identifier for the historical Microsoft login integration. Configure it through the administrator's secure settings, not in published documentation or debug logs.

<a id="desc_microsoft_consumer_secret" name="desc_microsoft_consumer_secret"></a>

### `microsoft_consumer_secret`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Application/client secret for the historical Microsoft login integration. Keep it private and rotate if exposed; do not include actual secrets in examples or commits.

<a id="desc_yahoo_login" name="desc_yahoo_login"></a>

### `yahoo_login`


**Documented default (Geeklog 2.2.2):** `false`
Enables the historical Yahoo OAuth login integration when supported by the specific Geeklog 2.2.2 configuration and an authorized provider application. **Do not assume compatibility with the provider's present-day OAuth APIs**; verify endpoints, callback URL, scopes and the installed login implementation.

<a id="desc_yahoo_consumer_key" name="desc_yahoo_consumer_key"></a>

### `yahoo_consumer_key`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Application/client identifier for the historical Yahoo login integration. Configure it through the administrator's secure settings, not in published documentation or debug logs.

<a id="desc_yahoo_consumer_secret" name="desc_yahoo_consumer_secret"></a>

### `yahoo_consumer_secret`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Application/client secret for the historical Yahoo login integration. Keep it private and rotate if exposed; do not include actual secrets in examples or commits.

<a id="desc_github_login" name="desc_github_login"></a>

### `github_login`


**Documented default (Geeklog 2.2.2):** `false`
Enables the historical Github OAuth login integration when supported by the specific Geeklog 2.2.2 configuration and an authorized provider application. **Do not assume compatibility with the provider's present-day OAuth APIs**; verify endpoints, callback URL, scopes and the installed login implementation.

<a id="desc_github_consumer_key" name="desc_github_consumer_key"></a>

### `github_consumer_key`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Application/client identifier for the historical Github login integration. Configure it through the administrator's secure settings, not in published documentation or debug logs.

<a id="desc_github_consumer_secret" name="desc_github_consumer_secret"></a>

### `github_consumer_secret`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Application/client secret for the historical Github login integration. Keep it private and rotate if exposed; do not include actual secrets in examples or commits.


## Likes and dynamic likes block — Geeklog 2.2.2

These descriptions are scoped to the [versioned source reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Provider integrations and bootstrap settings need separate operational checks before a live change.

<a id="desc_likes_enabled" name="desc_likes_enabled"></a>

### `likes_enabled`


**Documented default (Geeklog 2.2.2):** `1`
Likes facility scope: `0` disabled, `1` registered and anonymous visitors, `2` registered users only. The historical reference identifies anonymous users using IP address, which warrants privacy consideration.

<a id="desc_likes_articles" name="desc_likes_articles"></a>

### `likes_articles`


**Documented default (Geeklog 2.2.2):** `1`
Controls ratings on articles: `0` disabled, `1` likes and dislikes, or `2` likes only. The master `likes_enabled` option must also permit the feature.

<a id="desc_likes_comments" name="desc_likes_comments"></a>

### `likes_comments`


**Documented default (Geeklog 2.2.2):** `1`
Controls ratings on comments: `0` disabled, `1` likes and dislikes, or `2` likes only; requires the master likes setting.

<a id="desc_likes_speedlimit" name="desc_likes_speedlimit"></a>

### `likes_speedlimit`


**Documented default (Geeklog 2.2.2):** `45`
Minimum time between rating actions by a visitor, in seconds; historical default `45`.

<a id="desc_likes_users_listed" name="desc_likes_users_listed"></a>

### `likes_users_listed`


**Documented default (Geeklog 2.2.2):** `5`
Maximum number of recent users shown in a tooltip for an item's likes/dislikes. `0` disables user listing.

<a id="desc_likes_block_enable" name="desc_likes_block_enable"></a>

### `likes_block_enable`


**Documented default (Geeklog 2.2.2):** `true`
Enables the dynamic block highlighting recently liked or disliked content based on the options below.

<a id="desc_likes_block_isleft" name="desc_likes_block_isleft"></a>

### `likes_block_isleft`


**Documented default (Geeklog 2.2.2):** `1`
Displays the dynamic likes block on the left when `1`, or on the right when `0`.

<a id="desc_likes_block_order" name="desc_likes_block_order"></a>

### `likes_block_order`


**Documented default (Geeklog 2.2.2):** `10`
Position of the dynamic likes block within its column; historical default `10`.

<a id="desc_likes_block_topic_option" name="desc_likes_block_topic_option"></a>

### `likes_block_topic_option`


**Documented default (Geeklog 2.2.2):** `'all'`
Where the likes block appears: all pages, homepage only or selected topics. This controls placement, not which rated items qualify.

<a id="desc_likes_block_topic" name="desc_likes_block_topic"></a>

### `likes_block_topic`


**Documented default (Geeklog 2.2.2):** `(empty)`
Topic selection used when the likes block's placement mode is set to selected topics.

<a id="desc_likes_block_cache_time" name="desc_likes_block_cache_time"></a>

### `likes_block_cache_time`


**Documented default (Geeklog 2.2.2):** `3600`
Maximum lifetime of the dynamic likes block's cache, in seconds; `0` disables caching.

<a id="desc_likes_block_displayed_actions" name="desc_likes_block_displayed_actions"></a>

### `likes_block_displayed_actions`


**Documented default (Geeklog 2.2.2):** `3`
Include likes and dislikes (`3`), likes only (`1`) or dislikes only (`2`) in the dynamic block's ranking.

<a id="desc_likes_block_include_time" name="desc_likes_block_include_time"></a>

### `likes_block_include_time`


**Documented default (Geeklog 2.2.2):** `604800`
Age window for rating activity considered by the block, in seconds; historical default `604800` (one week), `0` includes all time.

<a id="desc_likes_block_max_items" name="desc_likes_block_max_items"></a>

### `likes_block_max_items`


**Documented default (Geeklog 2.2.2):** `10`
Maximum number of content items displayed in the dynamic likes block; historical default `10`.

<a id="desc_likes_block_title_trim_length" name="desc_likes_block_title_trim_length"></a>

### `likes_block_title_trim_length`


**Documented default (Geeklog 2.2.2):** `20`
Maximum displayed item title length in the dynamic likes block; historical default `20`.

<a id="desc_likes_block_likes_new_line" name="desc_likes_block_likes_new_line"></a>

### `likes_block_likes_new_line`


**Documented default (Geeklog 2.2.2):** `true`
Displays the likes/dislikes count on a separate line below the item title when enabled.

<a id="desc_likes_block_type" name="desc_likes_block_type"></a>

### `likes_block_type`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Optional filter by a single liked-item type such as article, comment, poll or plugin-defined type. Empty includes all supported types.

<a id="desc_likes_block_subtype" name="desc_likes_block_subtype"></a>

### `likes_block_subtype`


**Documented default (Geeklog 2.2.2):** `'' (empty)`
Optional subtype filter when the selected item type supports multiple subtypes, for example forum posts.

<a id="desc_likes_block_group_id" name="desc_likes_block_group_id"></a>

### `likes_block_group_id`


**Documented default (Geeklog 2.2.2):** `Block Admin`
Security group associated with the dynamic likes block's permissions; the 2.2.2 reference uses Block Admin.

<a id="desc_likes_block_permissions_0" name="desc_likes_block_permissions_0"></a>

### `likes_block_permissions_0`


**Documented default (Geeklog 2.2.2):** `Read-Only`
View permission for the owner of the dynamic likes block. Original reference default: Read-Only.

<a id="desc_likes_block_permissions_1" name="desc_likes_block_permissions_1"></a>

### `likes_block_permissions_1`


**Documented default (Geeklog 2.2.2):** `Read-Only`
View permission for the configured administrator group of the dynamic likes block. Original reference default: Read-Only.

<a id="desc_likes_block_permissions_2" name="desc_likes_block_permissions_2"></a>

### `likes_block_permissions_2`


**Documented default (Geeklog 2.2.2):** `Read-Only`
View permission for authenticated users of the dynamic likes block. Original reference default: Read-Only.

<a id="desc_likes_block_permissions_3" name="desc_likes_block_permissions_3"></a>

### `likes_block_permissions_3`


**Documented default (Geeklog 2.2.2):** `Read-Only`
View permission for anonymous visitors of the dynamic likes block. Original reference default: Read-Only.


## Bootstrap settings in siteconfig.php — Geeklog 2.2.2

These descriptions are scoped to the [versioned source reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Provider integrations and bootstrap settings need separate operational checks before a live change.

<a id="siteconfig.php" name="siteconfig.php"></a>

<a id="desc_path" name="desc_path"></a>

### `path`


**Documented default (Geeklog 2.2.2):** `/path/to/geeklog/`
Installation root filesystem path in `siteconfig.php` (trailing slash required), outside the assumption that the web document root is the full Geeklog installation.

<a id="desc_path_system" name="desc_path_system"></a>

### `path_system`


**Documented default (Geeklog 2.2.2):** `/path/to/geeklog/system/`
Absolute filesystem path to Geeklog's `system/` code libraries in `siteconfig.php` (trailing slash required).

<a id="desc_site_enabled" name="desc_site_enabled"></a>

### `site_enabled`


**Documented default (Geeklog 2.2.2):** `true`
Fast maintenance switch in `siteconfig.php`: set to `false` to disable access; the user-facing message is configured by `site_disabled_msg`.

<a id="desc_default_charset" name="desc_default_charset"></a>

### `default_charset`


**Documented default (Geeklog 2.2.2):** `iso-8859-1`
Fallback character encoding when the selected language file does not specify one. The 2.2.2 reference mentions a historical ISO-8859-1 default but recommends UTF-8 for multilingual installations; verify actual database and language encodings.

<a id="desc_rootdebug_siteconfig" name="desc_rootdebug_siteconfig"></a>

### `rootdebug_siteconfig`


**Documented default (Geeklog 2.2.2):** `(disabled)`
Emergency diagnostic override in `siteconfig.php`. The special `force` mode may expose extremely sensitive information, including credentials or cookies. **Never leave this enabled on a public site.**



## Historical configuration reference appendices — migration preview

These reference sections retain their original fragment identifiers, but some legacy tables and operational examples are **not yet fully transcribed**. The embedded v2.2.2 `config.html` remains the authoritative complete version until final content review.

<a id="db-config.php" name="db-config.php"></a>

### Database bootstrap configuration

The installation's `db-config.php` stores connection parameters such as the database host, name, user, password, table prefix and database type. These are installation-sensitive values, not safe defaults to copy into an existing site. Do not expose this file or credentials.

<a id="url-rewrite" name="url-rewrite"></a>

### URL rewriting

Geeklog 2.2.2 documents the following mappings. The placeholders such as `@sid`, `@page` and `@topic` are identifiers; the domains shown are examples, not deployment URLs. URL rewriting availability depends on the installed web server and configuration.

| Original URL | Rewritten URL |
| --- | --- |
| `https://www.example.com/article.php?story=@sid` | `https://www.example.com/article.php/@sid` |
| `https://www.example.com/article.php?story=@sid&mode=print` | `https://www.example.com/article.php/@sid/print` |
| `https://www.example.com/article.php?story=@sid&page=@page` | `https://www.example.com/article.php/@sid/@page` |
| `https://www.example.com/index.php?topic=@topic` | `https://www.example.com/index.php/topic/@topic/` |
| `https://www.example.com/index.php?topic=@topic&page=@page` | `https://www.example.com/index.php/topic/@topic/@page` |
| `https://www.example.com/directory.php?topic=@topic&year=@year&month=@month` | `https://www.example.com/directory.php/@topic/@year/@month` |
| `https://www.example.com/staticpages/index.php?page=@page` | `https://www.example.com/staticpages/index.php/@page` |
| `https://www.example.com/staticpages/index.php?page=@page&disp_mode=print` | `https://www.example.com/staticpages/index.php/@page/print` |
| `https://www.example.com/links/portal.php?what=link&item=@item` | `https://www.example.com/links/portal.php/link/@item` |
| `https://www.example.com/links/index.php?category=@cat` | `https://www.example.com/links/index.php/@cat` |

**Source:** [Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html#url-rewrite).


<a id="url-routing" name="url-routing"></a>

### URL routing

URL routing requires URL rewriting to be enabled first. The tagged 2.2.2 documentation defines these route patterns and priorities. Check the web server's routing configuration and existing links before enabling this feature.

| Public route | Internal destination | Priority |
| --- | --- | --- |
| `https://www.example.com/article/@sid` | `https://www.example.com/article.php?story=@sid` | 100 |
| `https://www.example.com/article/@sid/print` | `https://www.example.com/article.php?story=@sid&mode=print` | 110 |
| `https://www.example.com/article/@sid/@page` | `https://www.example.com/article.php?story=@sid&page=@page` | 120 |
| `https://www.example.com/topic/@topic` | `https://www.example.com/index.php?topic=@topic` | 130 |
| `https://www.example.com/topic/@topic/@page` | `https://www.example.com/index.php?topic=@topic&page=@page` | 140 |
| `https://www.example.com/archives/@topic/@year/@month` | `https://www.example.com/directory.php?topic=@topic&year=@year&month=@month` | 150 |
| `https://www.example.com/page/@page` | `https://www.example.com/staticpages/index.php?page=@page` | 160 |
| `https://www.example.com/page/@page/print` | `https://www.example.com/staticpages/index.php?page=@page&disp_mode=print` | 170 |
| `https://www.example.com/links/portal/@item` | `https://www.example.com/links/portal.php?what=link&item=@item` | 180 |
| `https://www.example.com/links/category/@cat` | `https://www.example.com/links/index.php?category=@cat` | 190 |

**Order matters:** the print route must be matched before the article pagination route. Rewriting and routing require end-to-end tests on the actual server.

**Source:** [Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html#url-routing).

### Web server rewrite examples (Geeklog 2.2.2)

These are **historical examples** for installations that enable URL routing without `index.php`. They are not complete hardened server configurations. The original release includes `.htaccess.txt` and `web.config.txt`; review those files, your actual document root and your server's rewrite module before using any rule.

**Apache `mod_rewrite` example:**

```apache
<IfModule mod_rewrite.c>
    RewriteEngine On
    # RewriteBase /
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule ^(.*)$ /index.php/$1 [L]
</IfModule>
```

For a site in a subdirectory, adjust the path prefix on the `RewriteRule` and review the public route rules separately. Do not copy a subdirectory placeholder verbatim.

**IIS URL Rewrite example:**

```xml
<configuration>
  <system.webServer>
    <rewrite>
      <rules>
        <rule name="Geeklog front controller" stopProcessing="true">
          <match url="^(.*)$" ignoreCase="false" />
          <conditions>
            <add input="{REQUEST_FILENAME}" matchType="IsFile" negate="true" />
            <add input="{REQUEST_FILENAME}" matchType="IsDirectory" negate="true" />
          </conditions>
          <action type="Rewrite" url="/index.php/{R:1}" />
        </rule>
      </rules>
    </rewrite>
  </system.webServer>
</configuration>
```

**Apache `RewriteRule` path variants from the legacy reference:**

For a site deployed at the document root:

```apache
RewriteRule ^(.*)$ /index.php/$1 [L]
```

For a subdirectory deployment, the original examples use a placeholder. Replace `[sub_directory]` with the correct path, including the slash where required:

```apache
RewriteRule ^(.*)$ [sub_directory]/index.php/$1 [L]
```

```apache
RewriteRule ^(.*)$ /[sub_directory]/index.php/$1 [L]
```

Never keep `[sub_directory]` literally in a production rule. The required prefix depends on the document root and application location.

The examples reflect the routing mechanism in the tagged 2.2.2 reference; they do **not** reproduce all settings or security rules in the distribution's sample files. Routing relies on supported `PATH_INFO` handling, rule ordering and a compatible web server configuration. First validate existing and rewritten URLs in staging, including articles, archives, print views and a site installed in a subdirectory.




<a id="Localization" name="Localization"></a>

### Language-file localization

Geeklog ships interface strings in language files, such as `english.php`. Interface translation is distinct from translating site content. Check that locale settings, language file names, encodings and user-selectable languages align.

<a id="date_formats" name="date_formats"></a>

### Locale and date format reference

The tagged Geeklog 2.2.2 documentation lists **33 date-format directives**. Their output is locale- and platform-dependent. This reference preserves the full directive inventory while using concise, newly written descriptions; test formatting against the PHP runtime used by your installation.

| Directive | Meaning |
| --- | --- |
| `%a` | Short weekday name, using the active locale |
| `%A` | Full weekday name, using the active locale |
| `%b` | Short month name, using the active locale |
| `%B` | Full month name, using the active locale |
| `%c` | Locale's date and time representation |
| `%C` | Century number |
| `%d` | Day of month, zero-padded |
| `%D` | Numeric date in month/day/two-digit-year order |
| `%e` | Day of month, space-padded |
| `%h` | Same abbreviated month as `%b` |
| `%H` | Hour on a 24-hour clock |
| `%I` | Hour on a 12-hour clock |
| `%j` | Day number within the year |
| `%m` | Numeric month |
| `%M` | Minute |
| `%n` | Newline |
| `%p` | Locale-specific AM/PM indicator |
| `%r` | Locale-specific 12-hour time representation |
| `%R` | Hours and minutes in 24-hour format |
| `%S` | Seconds |
| `%t` | Tab |
| `%T` | 24-hour time with seconds |
| `%u` | Weekday number, Monday first (1–7) |
| `%U` | Week number, Sunday-first convention |
| `%V` | ISO week number |
| `%W` | Week number, Monday-first convention |
| `%w` | Weekday number, Sunday = 0 |
| `%x` | Locale-specific date representation |
| `%X` | Locale-specific time representation |
| `%y` | Two-digit year |
| `%Y` | Four-digit year |
| `%Z` | Time zone name or abbreviation |
| `%%` | Literal percent sign |

The operating system must have the requested locale installed. Check available locales and actual date output before changing formatting settings. These are **historical directives**; compatibility with newer PHP/runtime combinations must be confirmed separately.

**Source:** [Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html#date_formats).

<a id="url-cron" name="url-cron"></a>

### Command-line scheduled jobs

Geeklog 2.2.2 ships two optional command-line PHP scripts at the **private Geeklog installation root**, outside `public_html`. Both must load the correct `lib-common.php` for the site; the tagged scripts contain a placeholder `/path/to/geeklog/lib-common.php` which must be adjusted before use. Confirm the PHP CLI executable, filesystem permissions and scheduler environment on your own server.

The tagged reference gives this historical **daily-digest scheduling example** (02:30 every day):

```cron
30 2 * * * /path/to/geeklog/cron-emailgeeklogdailydigest
```

The schedule describes when cron runs, not whether the script has been installed or configured. Replace the example path with the actual private installation path. Do not expose these scripts through a public web directory. Check whether the installed PHP CLI matches your Geeklog release's runtime requirements, and avoid broad filesystem permissions.

**Source:** [Geeklog 2.2.2 cron appendix](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html#url-cron).

<a id="cron_daily_digest" name="cron_daily_digest"></a>

### Daily-digest cron script

The [bundled daily-digest script](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/cron-emailgeeklogdailydigest) invokes `COM_emailUserTopics()` after loading `lib-common.php`. The site's Daily Digest configuration and the subscriber's topic preferences determine the content.

**First-run warning:** the historical reference warns that previously published articles may all be treated as new when the feature is first activated. Test delivery with a controlled recipient and review the `lastemailedstories` marker in the Geeklog `vars` table if you need to prevent an unexpectedly large first mailing. Do not edit a live database marker without a backup, a verified database prefix and a staging rehearsal.

<a id="cron_emailed_database_backup" name="cron_emailed_database_backup"></a>

### Email-based database backup cron script

The [tagged backup script](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/cron-emailgeeklogdatabasebackup) uses `dbBackup` to create and email a database export. In Geeklog 2.2.2, this script explicitly supports **MySQL only**; it does not create a complete backup of themes, uploads, private files or plugin directories.

The recipient can be configured in the script or via the `db_backup_sendto` value in the site's `vars` table. Configure a controlled mailbox and confirm that the attachment size fits the mail provider's limits. Schedule this task during a quieter period, restrict its access, and protect backup emails because SQL exports may contain personal or sensitive data.

For reliable recovery, retain separate protected copies of both the database **and** site files, and test restoration in an isolated environment. Email delivery is not itself evidence of a usable backup.

**Source:** [Geeklog 2.2.2 configuration appendix](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html#cron_emailed_database_backup).

## Historical configuration cross-references

The Geeklog 2.2.2 HTML reference links to the following 34 same-page destinations. All these historical anchors are preserved in this Markdown source. This index keeps those **navigation targets clickable** in the generated documentation; it does not yet reproduce every link in its original explanatory context.

**Main sections:** [Site](#site) · [Stories](#stories) · [Themes](#theme) · [Blocks](#blocks) · [Users](#users) · [Images](#images) · [Languages](#languages) · [Miscellaneous](#misc) · [File manager](#filemanager).

**Installation and appendices:** [Database configuration](#db-config.php) · [Site bootstrap](#siteconfig.php) · [URL rewriting](#url-rewrite) · [URL routing](#url-routing) · [Localization](#Localization) · [Date formats](#date_formats) · [Cron jobs](#url-cron).

**Settings and linked help:** [Structured data](#desc_structured_data_type_default) · [Cookie information URL](#desc_about_cookies_link) · [Cookie consent](#desc_cookie_consent) · [Cron interval](#desc_cron_schedule_interval) · [Site HTML path](#desc_path_html) · [Image path](#desc_path_images) · [Editor path](#desc_path_editors) · [Theme path](#desc_path_themes) · [Feed file path](#desc_rdf_file) · [Comment edit period](#desc_comment_edittime) · [Comment editing](#desc_comment_edit) · [Likes block subtype](#desc_likes_block_subtype) · [Likes block type](#desc_likes_block_type) · [Gravatar](#images_gravatar) · [Debug configuration](#desc_rootdebug_siteconfig) · [Advanced editor](#desc_advanced_editor) · [Site-disabled message](#desc_site_disabled_msg) · [Root debug](#desc_rootdebug).

**Scope:** Legacy relative links to other HTML help files and historical external websites are audited separately in `config-link-audit.json`. Only valid in-page navigation is asserted here.

