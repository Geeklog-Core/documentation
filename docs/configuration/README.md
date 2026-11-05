# Geeklog 2.2.2 configuration reference

> **Coverage notice:** This Markdown reference preserves historical help anchors but does not yet reproduce all details of the bundled 2.2.2 configuration guide. Use the original `docs/english/config.html` for exhaustive defaults, examples and tables. The embedded distribution keeps that file unchanged until full content parity has been reviewed.

## Selected documented defaults — Geeklog 2.2.2

The following **historical defaults** were checked against the [tagged 2.2.2 Core configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). They describe the example/default values in that documentation, **not the current values on your site**.

| Setting | Documented 2.2.2 default | Purpose and precautions |
| --- | --- | --- |
| `site_url` | `http://www.example.com` | Public base URL, without a trailing slash. Replace with the actual site's URL. |
| `site_admin_url` | `http://www.example.com/admin` | Browser URL of the administration directory, **not** a filesystem path. |
| `site_name` | `Geeklog Site` | Site name displayed in the interface. |
| `site_slogan` | `Another Nifty Geeklog Site` | Slogan added to the HTML title. |
| `mail_settings_port` | `25` | Historic mail-server port setting; configure the actual SMTP provider's required port and encryption, not an assumed default. |
| `mail_settings_auth` | `0` | Historic setting for SMTP authentication disabled; enable authentication when required by the server. |
| `ip_anonymization` | `-1` | Historic setting for no database-IP anonymization; cron scheduling can affect nonnegative policies. |

For a migrated or upgraded installation, record the actual configuration before making changes. Avoid reusing example domains, historic SMTP ports or historic security defaults as production recommendations.

## Configuration panel

Geeklog provides a Configuration administration panel for most settings. Installation and database bootstrap values can also reside in `siteconfig.php` and `db-config.php`.

## Context-sensitive help

Core configuration help links use `config.html#desc_<option>`. These examples illustrate the intended Markdown source format.

<a id="site" name="site"></a>
<a id="site_site" name="site_site"></a>

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

<a id="site_mail" name="site_mail"></a>

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

<a id="site_syndication" name="site_syndication"></a>

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


## Articles and presentation — Geeklog 2.2.2

Source: [bundled Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Descriptions reflect this specific release; do not apply old security defaults to newer deployments.

<a id="stories" name="stories"></a>
<a id="stories_story" name="stories_story"></a>

<a id="desc_maximagesperarticle" name="desc_maximagesperarticle"></a>

### `maximagesperarticle`

Maximum number of images allowed in an article; bundled default: `5`.

<a id="desc_limitnews" name="desc_limitnews"></a>

### `limitnews`

Number of articles displayed on the index page and in the older-articles block; bundled default: `10`.

<a id="desc_minnews" name="desc_minnews"></a>

### `minnews`

Minimum number of articles that may appear on a topic page; bundled default: `1`.

<a id="desc_contributedbyline" name="desc_contributedbyline"></a>

### `contributedbyline`

When set to `1`, displays an article author's username publicly and permits username-based search; `0` disables it.

<a id="desc_hideviewscount" name="desc_hideviewscount"></a>

### `hideviewscount`

`0` shows an article's view count, while `1` hides it.

<a id="desc_hideemailicon" name="desc_hideemailicon"></a>

### `hideemailicon`

`1` disables the email-article feature and hides its article options; default `0`.

<a id="desc_hideprintericon" name="desc_hideprintericon"></a>

### `hideprintericon`

`1` disables the printer-friendly article view and hides its links; default `0`.

<a id="desc_allow_page_breaks" name="desc_allow_page_breaks"></a>

### `allow_page_breaks`

Controls use of the `[page_break]` tag to split an article into multiple pages; default `1`.

<a id="desc_page_break_comments" name="desc_page_break_comments"></a>

### `page_break_comments`

For multipage articles, places comments on `first`, `last` or `all` pages; documented default `last`. Comments on all pages may return a user to the first page after posting under some settings.

<a id="desc_article_image_align" name="desc_article_image_align"></a>

### `article_image_align`

Displays the article's topic image on the `right` or `left`; bundled default `right`.

<a id="desc_show_topic_icon" name="desc_show_topic_icon"></a>

### `show_topic_icon`

Default for new articles and submissions: `1` shows the topic icon, `0` hides it.

<a id="desc_draft_flag" name="desc_draft_flag"></a>

### `draft_flag`

Default draft status of newly created articles by story administrators; `1` drafts, `0` otherwise.

<a id="desc_frontpage" name="desc_frontpage"></a>

### `frontpage`

Default article and submission placement: `1` front page, `0` topic-only. The archived topic is an exception.

<a id="desc_hide_no_news_msg" name="desc_hide_no_news_msg"></a>

### `hide_no_news_msg`

Set to `1` to suppress the no-news notice on pages with no articles.

<a id="desc_hide_main_page_navigation" name="desc_hide_main_page_navigation"></a>

### `hide_main_page_navigation`

Controls hiding index pagination on the front page or on front page plus topic pages; doing so can make older articles harder to reach.

<a id="desc_onlyrootfeatures" name="desc_onlyrootfeatures"></a>

### `onlyrootfeatures`

If enabled, restricts selection of featured articles to `Root` users to avoid conflicts between administrators with different article visibility.

## Login, access and account protection — Geeklog 2.2.2

Source: [bundled Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Descriptions reflect this specific release; do not apply old security defaults to newer deployments.

<a id="users_login" name="users_login"></a>

<a id="desc_lastlogin" name="desc_lastlogin"></a>

### `lastlogin`

Controls whether Geeklog records users' most recent login time.

<a id="desc_loginrequired" name="desc_loginrequired"></a>

### `loginrequired`

Require an account to access the site (`1`). This setting overrides the more specific login requirements below when enabled.

<a id="desc_submitloginrequired" name="desc_submitloginrequired"></a>

### `submitloginrequired`

Require a logged-in user for article and plugin-item submissions when `1`.

<a id="desc_commentsloginrequired" name="desc_commentsloginrequired"></a>

### `commentsloginrequired`

Require login to submit comments when `1`.

<a id="desc_statsloginrequired" name="desc_statsloginrequired"></a>

### `statsloginrequired`

Require login to view site statistics when `1`.

<a id="desc_searchloginrequired" name="desc_searchloginrequired"></a>

### `searchloginrequired`

`1` restricts advanced search to logged-in users; `2` also restricts simple search.

<a id="desc_profileloginrequired" name="desc_profileloginrequired"></a>

### `profileloginrequired`

Require login to view another user's profile when `1`.

<a id="desc_emailuserloginrequired" name="desc_emailuserloginrequired"></a>

### `emailuserloginrequired`

Require login to send email to another user using the site form when `1`.

<a id="desc_emailstoryloginrequired" name="desc_emailstoryloginrequired"></a>

### `emailstoryloginrequired`

Require login to email articles when `1`.

<a id="desc_directoryloginrequired" name="desc_directoryloginrequired"></a>

### `directoryloginrequired`

Require login to access the list of older articles when `1`.

<a id="desc_passwordspeedlimit" name="desc_passwordspeedlimit"></a>

### `passwordspeedlimit`

Minimum time between password-reset requests in seconds; bundled default `300`.

<a id="desc_login_attempts" name="desc_login_attempts"></a>

### `login_attempts`

Number of failed sign-in attempts before the login speed limit applies; bundled default `3`.

<a id="desc_login_speedlimit" name="desc_login_speedlimit"></a>

### `login_speedlimit`

Delay, in seconds, before another login may be attempted after the failed-attempt threshold; bundled default `300`.

<a id="desc_invalidloginattempts" name="desc_invalidloginattempts"></a>

### `invalidloginattempts`

Number of invalid login attempts for one user account before an administrator warning is eligible; bundled default `7`. Interacts with the observation window below.

<a id="desc_invalidloginmaxtime" name="desc_invalidloginmaxtime"></a>

### `invalidloginmaxtime`

Observation period in seconds used for warnings about repeated invalid account logins; bundled default `1200`. Set to `0` to disable this warning feature in the 2.2.2 reference.

<a id="desc_enable_twofactorauth" name="desc_enable_twofactorauth"></a>

### `enable_twofactorauth`

Enables two-factor authentication as an available account feature. Users must also configure it in their own account settings. The bundled default is disabled.

<a id="desc_pass_alg" name="desc_pass_alg"></a>

### `pass_alg`

Legacy password-hashing algorithm selector documented for Geeklog 2.2.2. The bundled reference lists old algorithms including SHA-1 and Blowfish. **Do not treat a historical default or its recommendation as modern password-security advice**; verify the actual installed implementation and current supported upgrade path before changing existing hashes.

<a id="desc_pass_stretch" name="desc_pass_stretch"></a>

### `pass_stretch`

Number of password-hash iterations configured for the 2.2.2 legacy scheme; documented default `4096`. Compatibility and safe migration need review before making changes.



## Theme and template settings — Geeklog 2.2.2

Settings derived from the [tagged Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Verify behavior against the installed release before changing live site settings.

<a id="theme" name="theme"></a>
<a id="theme_theme" name="theme_theme"></a>

<a id="desc_theme" name="desc_theme"></a>

### `theme`

Default theme for anonymous visitors and new accounts. Existing users may retain their chosen theme if user theme selection is allowed; 2.2.2 reference default: Denim Three.

<a id="desc_doctype" name="desc_doctype"></a>

### `doctype`

Document type declaration emitted by themes that use the `{doctype}` template variable. Hard-coded DOCTYPE declarations in a theme are not controlled by this setting.

<a id="desc_menu_elements" name="desc_menu_elements"></a>

### `menu_elements`

Controls entries in themes using `{menu_elements}`. The 2.2.2 reference lists `home`, `contribute`, `search`, `stats`, `directory`, `login`, `prefs`, `plugins` and `custom`; actual display depends on the theme.

<a id="desc_path_themes" name="desc_path_themes"></a>

### `path_themes`

Filesystem directory containing themes. The 2.2.2 reference identifies it as the site's `public_html/layout/` directory and states this path cannot be changed from its default.

<a id="desc_cache_templates" name="desc_cache_templates"></a>

### `cache_templates`

Controls caching of theme template files. Caching usually helps performance, but may be unsuitable for disk bottlenecks or dynamic autotags in templates. It is separate from content caching.

<a id="desc_cache_mobile" name="desc_cache_mobile"></a>

### `cache_mobile`

When enabled, mobile-device responses may be cached separately from desktop responses. Disabling it can reduce cache variants when mobile and desktop output are equivalent.

<a id="desc_cache_resource" name="desc_cache_resource"></a>

### `cache_resource`

Controls combining, minifying and caching JavaScript and CSS resources. The 2.2.2 reference notes that themes using `style.css.php` can apply separate mandatory caching behavior.


## User registration and approval — Geeklog 2.2.2

Settings derived from the [tagged Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Verify behavior against the installed release before changing live site settings.

<a id="users_usersub" name="users_usersub"></a>

<a id="desc_usersubmission" name="desc_usersubmission"></a>

### `usersubmission`

Enables the approval queue for newly submitted accounts when `1`; when turning it off, first process existing queued accounts.

<a id="desc_allow_domains" name="desc_allow_domains"></a>

### `allow_domains`

Comma-separated approved email domains that can bypass the user approval queue when that queue is enabled. The 2.2.2 reference allows regular expressions; review patterns carefully to avoid unintended approvals.

<a id="desc_disallow_domains" name="desc_disallow_domains"></a>

### `disallow_domains`

List or regular expressions for email domains forbidden for new registrations. This blacklist applies even when the account approval queue is disabled.


## Article and content submissions — Geeklog 2.2.2

Settings derived from the [tagged Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Verify behavior against the installed release before changing live site settings.

<a id="users_submission" name="users_submission"></a>

<a id="desc_storysubmission" name="desc_storysubmission"></a>

### `storysubmission`

Enable or disable moderation queue for submitted articles (`1` on, `0` off).

<a id="desc_listdraftstories" name="desc_listdraftstories"></a>

### `listdraftstories`

When enabled, adds a block of draft articles to the moderation page.

<a id="desc_postmode" name="desc_postmode"></a>

### `postmode`

Default article submission format: `plaintext` or `html` in the 2.2.2 reference.

<a id="desc_speedlimit" name="desc_speedlimit"></a>

### `speedlimit`

Minimum delay between content submissions, in seconds; bundled default `45`. This is a rate-limiting mechanism, not a complete spam defense.

<a id="desc_skip_preview" name="desc_skip_preview"></a>

### `skip_preview`

When enabled, permits immediate article and comment submission without first requiring a preview.

<a id="desc_advanced_editor" name="desc_advanced_editor"></a>

### `advanced_editor`

Enables a rich-text/WYSIWYG editor for supported article, comment and Static Pages forms. Geeklog 2.2.2 shipped with CKEditor.

<a id="desc_advanced_editor_name" name="desc_advanced_editor_name"></a>

### `advanced_editor_name`

Name of the selected rich-text editor; the 2.2.2 reference lists CKEditor as the default.

<a id="desc_wikitext_editor" name="desc_wikitext_editor"></a>

### `wikitext_editor`

Adds Wiki-style formatting to the article editor using the older PEAR Text_Wiki implementation when enabled. Confirm dependencies before relying on this legacy option.

<a id="desc_remove_4byte_chars" name="desc_remove_4byte_chars"></a>

### `remove_4byte_chars`

Controls removal of four-byte UTF-8 characters, including emoji, when `COM_applyBasicFilter()` runs. Turning removal off requires compatible `utf8mb4` database/table/column collations and compatible plugins; otherwise saving content can fail.


## Comments and moderation — Geeklog 2.2.2

Settings derived from the [tagged Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Verify behavior against the installed release before changing live site settings.

<a id="users_comments" name="users_comments"></a>

<a id="desc_commentspeedlimit" name="desc_commentspeedlimit"></a>

### `commentspeedlimit`

Minimum delay in seconds between comments by the same user; bundled default `45`.

<a id="desc_comment_limit" name="desc_comment_limit"></a>

### `comment_limit`

Maximum number of comments displayed per page; bundled default `100`.

<a id="desc_comment_mode" name="desc_comment_mode"></a>

### `comment_mode`

Default display mode for comments; 2.2.2 lists `threaded`, `nested`, `flat` and `nocomments`.

<a id="desc_comment_order" name="desc_comment_order"></a>

### `comment_order`

Top-level comment order by date: `ASC` oldest first or `DESC` newest first.

<a id="desc_comment_code" name="desc_comment_code"></a>

### `comment_code`

Default comment availability on new articles: `0` enables comments, while `-1` disables them.

<a id="desc_commentsubmission" name="desc_commentsubmission"></a>

### `commentsubmission`

Controls whether submitted comments must be approved in a moderation queue.

<a id="desc_comment_edit" name="desc_comment_edit"></a>

### `comment_edit`

Enables a limited editing window for registered users' own comments. Anonymous users cannot edit their comments, while administrators with `comment.edit` may. Review interactions with queued comments.

<a id="desc_comment_edittime" name="desc_comment_edittime"></a>

### `comment_edittime`

Time in seconds during which an author may edit a comment when editing is enabled; bundled default `1800`.

<a id="desc_article_comment_close_enabled" name="desc_article_comment_close_enabled"></a>

### `article_comment_close_enabled`

Default setting for whether newly created articles should stop accepting comments after a specified number of days. It can be changed per article.

<a id="desc_article_comment_close_days" name="desc_article_comment_close_days"></a>

### `article_comment_close_days`

Number of days after which new articles configured for automatic closure stop accepting comments; bundled default `30`. It has no effect unless closure is enabled for that article.

<a id="desc_comment_close_rec_stories" name="desc_comment_close_rec_stories"></a>

### `comment_close_rec_stories`

Number of most recent articles that permit new comments; older articles can be closed as new ones arrive. `0` disables this limit.

<a id="desc_allow_reply_notifications" name="desc_allow_reply_notifications"></a>

### `allow_reply_notifications`

Controls whether registered users can subscribe to email notifications when someone replies directly to their comments.

<a id="desc_comment_on_same_page" name="desc_comment_on_same_page"></a>

### `comment_on_same_page`

Controls whether the comment editor is shown on the same page as the content instead of a separate page.

<a id="desc_show_comments_at_replying" name="desc_show_comments_at_replying"></a>

### `show_comments_at_replying`

Controls whether existing comments are visible on the dedicated reply page. This option is irrelevant when the same-page editor is enabled.



## Blocks — administration and topic navigation — Geeklog 2.2.2

Descriptions condensed from the [bundled 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Check installed-release behavior before modifying a production site.

<a id="blocks" name="blocks"></a>
<a id="blocks_admin" name="blocks_admin"></a>

<a id="desc_sort_admin" name="desc_sort_admin"></a>

### `sort_admin`

Sort entries in the Administrator block and Command and Control icons alphabetically when enabled.

<a id="desc_link_documentation" name="desc_link_documentation"></a>

### `link_documentation`

Show the Geeklog documentation link in the administrator block when set to `1`.

<a id="desc_link_versionchecker" name="desc_link_versionchecker"></a>

### `link_versionchecker`

Display the version-check link in the administrator block when enabled; the reference notes this is visible only to `Root` members.

<a id="blocks_topics" name="blocks_topics"></a>

<a id="desc_sortmethod" name="desc_sortmethod"></a>

### `sortmethod`

Topic sorting in the Sections block: `alpha` sorts alphabetically; `sortnum` uses the configured sort number.

<a id="desc_showstorycount" name="desc_showstorycount"></a>

### `showstorycount`

Show the number of articles in each topic in the Sections block when `1`.

<a id="desc_showsubmissioncount" name="desc_showsubmissioncount"></a>

### `showsubmissioncount`

Show the number of article submissions by topic in the Sections block when `1`.

<a id="desc_hide_home_link" name="desc_hide_home_link"></a>

### `hide_home_link`

Hide the Home link in the Sections block when `1`.


## Blocks — online users and recent content — Geeklog 2.2.2

Descriptions condensed from the [bundled 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Check installed-release behavior before modifying a production site.

<a id="blocks_who" name="blocks_who"></a>

<a id="desc_whosonline_threshold" name="desc_whosonline_threshold"></a>

### `whosonline_threshold`

Idle-time threshold, in seconds, after which a user is no longer listed in the Who's Online block; the 2.2.2 reference default is `300`.

<a id="desc_whosonline_anonymous" name="desc_whosonline_anonymous"></a>

### `whosonline_anonymous`

When enabled, anonymous visitors see only the count of registered users online rather than their names.

<a id="desc_whosonline_photo" name="desc_whosonline_photo"></a>

### `whosonline_photo`

When enabled, display a thumbnail of a user's uploaded photo where available, otherwise a photo icon.

<a id="blocks_what" name="blocks_what"></a>

<a id="desc_newstoriesinterval" name="desc_newstoriesinterval"></a>

### `newstoriesinterval`

Maximum age, in seconds, for articles classified as new; default `86400`.

<a id="desc_newcommentsinterval" name="desc_newcommentsinterval"></a>

### `newcommentsinterval`

Maximum age, in seconds, for comments classified as new; default `172800`.

<a id="desc_newtrackbackinterval" name="desc_newtrackbackinterval"></a>

### `newtrackbackinterval`

Maximum age of new trackbacks, in seconds; default `172800`.

<a id="desc_hidenewstories" name="desc_hidenewstories"></a>

### `hidenewstories`

Hide new articles in the What's New block when `1`.

<a id="desc_hidenewcomments" name="desc_hidenewcomments"></a>

### `hidenewcomments`

Hide new comments in the What's New block when `1`.

<a id="desc_hidenewtrackbacks" name="desc_hidenewtrackbacks"></a>

### `hidenewtrackbacks`

Hide new trackbacks in the What's New block when `1`.

<a id="desc_hidenewplugins" name="desc_hidenewplugins"></a>

### `hidenewplugins`

Hide recent items provided by plugins in the What's New block when `1`.

<a id="desc_title_trim_length" name="desc_title_trim_length"></a>

### `title_trim_length`

Maximum displayed title length for items in the What's New block; default `20`.

<a id="desc_whatsnew_cache_time" name="desc_whatsnew_cache_time"></a>

### `whatsnew_cache_time`

Maximum cache duration for the What's New block, in seconds; default `3600`. Set to `0` to disable this cache.


## Language selection and multilingual content — Geeklog 2.2.2

Descriptions condensed from the [bundled 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Check installed-release behavior before modifying a production site.

<a id="languages" name="languages"></a>
<a id="languages_language" name="languages_language"></a>

<a id="desc_language" name="desc_language"></a>

### `language`

Default interface language for the site; the 2.2.2 bundled reference uses `english`.

<a id="desc_allow_user_language" name="desc_allow_user_language"></a>

### `allow_user_language`

Allow registered users to choose an interface language in My Account when `1`.

<a id="desc_switchlang_homepage" name="desc_switchlang_homepage"></a>

### `switchlang_homepage`

When enabled, changing language returns the visitor to the homepage, useful when an equivalent translated topic or page is absent.

<a id="desc_new_item_set_current_lang" name="desc_new_item_set_current_lang"></a>

### `new_item_set_current_lang`

When enabled and multilingual support is configured, eligible new article or Static Pages identifiers include a current-language suffix.

<a id="desc_language_files" name="desc_language_files"></a>

### `language_files`

Mapping of language suffixes such as `en` or `de` to installed Geeklog language files for multilingual content. It must be configured together with `languages`.

<a id="desc_languages" name="desc_languages"></a>

### `languages`

Mapping of the same language suffixes to display names for multilingual content. This must match `language_files`; both must be enabled or disabled together.


## Locale, dates and number formats — Geeklog 2.2.2

Descriptions condensed from the [bundled 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Check installed-release behavior before modifying a production site.

<a id="languages_locale" name="languages_locale"></a>

<a id="desc_locale" name="desc_locale"></a>

### `locale`

PHP locale used for localized information such as dates; bundled reference default `en_GB`.

<a id="desc_date" name="desc_date"></a>

### `date`

Format string used for general dates and article timestamps. Check the bundled reference for its version-specific formatting directives.

<a id="desc_daytime" name="desc_daytime"></a>

### `daytime`

Shorter date-time format used where compact timestamps are needed.

<a id="desc_shortdate" name="desc_shortdate"></a>

### `shortdate`

Shortest date format, with the historical default `%x`.

<a id="desc_dateonly" name="desc_dateonly"></a>

### `dateonly`

Short day-and-month date format, used by features including event and older-article blocks.

<a id="desc_timeonly" name="desc_timeonly"></a>

### `timeonly`

Time-only format used for time-specific displays such as event details.

<a id="desc_week_start" name="desc_week_start"></a>

### `week_start`

First day of a calendar week: `Sun` or `Mon`.

<a id="desc_hour_mode" name="desc_hour_mode"></a>

### `hour_mode`

Time-editing mode: `12` for AM/PM or `24` for a 24-hour clock.

<a id="desc_thousand_separator" name="desc_thousand_separator"></a>

### `thousand_separator`

Character used to group thousands in formatted numbers.

<a id="desc_decimal_separator" name="desc_decimal_separator"></a>

### `decimal_separator`

Character separating the integer and fractional parts of a number.

<a id="desc_decimal_count" name="desc_decimal_count"></a>

### `decimal_count`

Number of decimal places displayed; historical default `2`.

<a id="desc_timezone" name="desc_timezone"></a>

### `timezone`

Site's intended time zone when it differs from that of the hosting server. Confirm behavior on the installed release.



## Image processing libraries — Geeklog 2.2.2

Descriptions adapted from the [official Geeklog 2.2.2 configuration HTML](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). These are release-specific settings; test image operations in staging before applying them to a public site.

<a id="images" name="images"></a>
<a id="images_imagelib" name="images_imagelib"></a>

<a id="desc_image_lib" name="desc_image_lib"></a>

### `image_lib`

Selects the image resize engine used for uploads: ImageMagick (`imagemagick`), Netpbm (`netpbm`) or PHP GD (`gdlib`) in Geeklog 2.2.2. Leave as `None` if no supported resizing backend is available. Verify installed extensions/binaries before enabling.

<a id="desc_path_to_mogrify" name="desc_path_to_mogrify"></a>

### `path_to_mogrify`

Absolute filesystem path to the ImageMagick `mogrify` executable when `image_lib` is `imagemagick`. The historical reference uses `/usr/bin/mogrify` as an example; check your server.

<a id="desc_path_to_netpbm" name="desc_path_to_netpbm"></a>

### `path_to_netpbm`

Absolute directory containing Netpbm executables when `image_lib` is `netpbm`. The 2.2.2 reference specifies a trailing slash.


## Image uploads and scaling — Geeklog 2.2.2

Descriptions adapted from the [official Geeklog 2.2.2 configuration HTML](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). These are release-specific settings; test image operations in staging before applying them to a public site.

<a id="images_upload" name="images_upload"></a>

<a id="desc_keep_unscaled_image" name="desc_keep_unscaled_image"></a>

### `keep_unscaled_image`

When enabled, retains the original uploaded image as well as a resized version, allowing thumbnails to link to the original. Consider additional disk usage.

<a id="desc_allow_user_scaling" name="desc_allow_user_scaling"></a>

### `allow_user_scaling`

When original images are retained, lets article authors select scaled or original images using the supported image tags (`[image X]` and `[unscaled X]`).

<a id="desc_jpeg_quality" name="desc_jpeg_quality"></a>

### `jpeg_quality`

Controls JPEG encoding quality when images are resized. The referenced range is 0–100, but it is not a percentage; its documented fallback is 75 when unset. High values increase file size.

<a id="desc_debug_image_upload" name="desc_debug_image_upload"></a>

### `debug_image_upload`

Adds diagnostic output for image upload and resize operations to Geeklog's error log when enabled. Avoid leaving verbose logging enabled in production.


## Images attached to articles — Geeklog 2.2.2

Descriptions adapted from the [official Geeklog 2.2.2 configuration HTML](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). These are release-specific settings; test image operations in staging before applying them to a public site.

<a id="images_articles" name="images_articles"></a>

<a id="desc_max_image_width" name="desc_max_image_width"></a>

### `max_image_width`

Maximum article image width in pixels. The historical 2.2.2 reference documents `160`; larger images may be resized or rejected depending on the selected image library.

<a id="desc_max_image_height" name="desc_max_image_height"></a>

### `max_image_height`

Maximum article image height in pixels; the reference documents `160`. Oversized images may be resized or rejected according to the image backend.

<a id="desc_max_image_size" name="desc_max_image_size"></a>

### `max_image_size`

Maximum uploaded article image size in bytes; documented as `1048576` (1 MiB). Files larger than the limit are rejected even when an image-resizing library is configured.


## Topic icon image limits — Geeklog 2.2.2

Descriptions adapted from the [official Geeklog 2.2.2 configuration HTML](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). These are release-specific settings; test image operations in staging before applying them to a public site.

<a id="images_topic" name="images_topic"></a>

<a id="desc_max_topicicon_width" name="desc_max_topicicon_width"></a>

### `max_topicicon_width`

Maximum topic icon width in pixels; the bundled reference documents `48`. Oversized icons may be resized or rejected.

<a id="desc_max_topicicon_height" name="desc_max_topicicon_height"></a>

### `max_topicicon_height`

Maximum topic icon height in pixels; documented as `48`.

<a id="desc_max_topicicon_size" name="desc_max_topicicon_size"></a>

### `max_topicicon_size`

Maximum uploaded topic icon size in bytes; documented as `65536` (64 KiB). Oversized files are rejected regardless of whether a resizing library exists.


## User photos and generated avatars — Geeklog 2.2.2

Descriptions adapted from the [official Geeklog 2.2.2 configuration HTML](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). These are release-specific settings; test image operations in staging before applying them to a public site.

<a id="images_photos" name="images_photos"></a>

<a id="desc_max_photo_width" name="desc_max_photo_width"></a>

### `max_photo_width`

Maximum stored user-photo width in pixels; historical default `128`. Images exceeding this may be resized or rejected.

<a id="desc_max_photo_height" name="desc_max_photo_height"></a>

### `max_photo_height`

Maximum stored user-photo height in pixels; historical default `128`.

<a id="desc_max_photo_size" name="desc_max_photo_size"></a>

### `max_photo_size`

Maximum uploaded user-photo size in bytes; historical default `65536` (64 KiB). Files above the limit are rejected.

<a id="desc_force_photo_width" name="desc_force_photo_width"></a>

### `force_photo_width`

Optional maximum display width for user photos in emitted HTML. This changes their displayed dimensions, not the dimensions of the stored image.

<a id="desc_default_photo" name="desc_default_photo"></a>

### `default_photo`

Full URL of a fallback photo for accounts without their own photo, when configured. The original 2.2.2 reference describes this as disabled by default.

<a id="desc_generate_user_icon" name="desc_generate_user_icon"></a>

### `generate_user_icon`

When enabled and `default_photo` is unavailable, generates a basic avatar from the username. Appearance depends on the theme's CSS and browser support for CSS variables.


## Gravatar integration — Geeklog 2.2.2

Descriptions adapted from the [official Geeklog 2.2.2 configuration HTML](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). These are release-specific settings; test image operations in staging before applying them to a public site.

<a id="images_gravatar" name="images_gravatar"></a>

<a id="desc_use_gravatar" name="desc_use_gravatar"></a>

### `use_gravatar`

When enabled, requests an avatar from Gravatar for users who did not upload a photo. Uploaded photos take precedence. Consider external-service privacy and page-load performance.

<a id="desc_gravatar_rating" name="desc_gravatar_rating"></a>

### `gravatar_rating`

Maximum Gravatar rating permitted for displayed remote avatars; the 2.2.2 reference mentions `G`, `PG`, `R` and `X`.

<a id="desc_gravatar_identicon" name="desc_gravatar_identicon"></a>

### `gravatar_identicon`

Fallback Gravatar style when a remote avatar is absent. The historical reference lists Mystery Man, Identicon, MonsterId, WAvatar and Retro; availability may change with the external provider.



## Filesystem paths and storage — Geeklog 2.2.2

Descriptions based on the [versioned Geeklog configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Values and operating behavior must be checked on the target installation before modifying production settings.

<a id="site_paths" name="site_paths"></a>

<a id="desc_path_html" name="desc_path_html"></a>

### `path_html`

Filesystem path of the web-accessible Geeklog tree. A trailing slash is required. The 2.2.2 reference warns against modifying this setting on a live site except as part of a controlled migration; dependent image, editor, theme and feed paths must remain consistent.

<a id="desc_path_log" name="desc_path_log"></a>

### `path_log`

Filesystem path of the Geeklog logging directory. Keep log files protected against public downloads.

<a id="desc_path_language" name="desc_path_language"></a>

### `path_language`

Filesystem path to the installed Geeklog language files.

<a id="desc_backup_path" name="desc_backup_path"></a>

### `backup_path`

Filesystem path to stored database backup files. Protect this directory from web access and verify write permissions and actual recovery procedures.

<a id="desc_path_data" name="desc_path_data"></a>

### `path_data`

Filesystem path for Geeklog application data, including data used by bulk user import.

<a id="desc_path_images" name="desc_path_images"></a>

### `path_images`

Filesystem path for Geeklog images, user photos and article images. The 2.2.2 reference requires it to reside within `path_html`.

<a id="desc_path_editors" name="desc_path_editors"></a>

### `path_editors`

Filesystem path to the rich-text editor assets. The 2.2.2 reference requires it to reside within `path_html`.


## Database backup options — Geeklog 2.2.2

Descriptions based on the [versioned Geeklog configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Values and operating behavior must be checked on the target installation before modifying production settings.

<a id="site_database" name="site_database"></a>

<a id="desc_dbdump_filename_prefix" name="desc_dbdump_filename_prefix"></a>

### `dbdump_filename_prefix`

Filename prefix used for database dump files; the 2.2.2 reference uses `geeklog_db_backup`.

<a id="desc_dbdump_tables_only" name="desc_dbdump_tables_only"></a>

### `dbdump_tables_only`

When `1`, export database table structures without their row data; when `0`, export both table definitions and data. **Structure-only dumps cannot restore site content.**

<a id="desc_dbdump_gzip" name="desc_dbdump_gzip"></a>

### `dbdump_gzip`

Controls whether database backup dumps are compressed when gzip support is available.

<a id="desc_dbdump_max_files" name="desc_dbdump_max_files"></a>

### `dbdump_max_files`

Maximum number of retained database backup files; the reference default is `10`, with `0` disabling automatic deletion. Set retention based on your recovery requirements.


## Search results configuration — Geeklog 2.2.2

Descriptions based on the [versioned Geeklog configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Values and operating behavior must be checked on the target installation before modifying production settings.

<a id="site_search" name="site_search"></a>

<a id="desc_search_style" name="desc_search_style"></a>

### `search_style`

Display style for search results: `google` or `table` in Geeklog 2.2.2.

<a id="desc_search_limits" name="desc_search_limits"></a>

### `search_limits`

Comma-separated result counts offered to users; the reference lists `10,15,25,30`.

<a id="desc_num_search_results" name="desc_num_search_results"></a>

### `num_search_results`

Default number of search results per page, chosen from `search_limits`; the bundled default is `30`.

<a id="desc_search_show_limit" name="desc_search_show_limit"></a>

### `search_show_limit`

Controls whether visitors can select the number of results shown on a search page.

<a id="desc_search_show_sort" name="desc_search_show_sort"></a>

### `search_show_sort`

Controls display of sorting controls; in table mode it affects column sorting.

<a id="desc_search_show_num" name="desc_search_show_num"></a>

### `search_show_num`

Controls whether the search result number is shown.

<a id="desc_search_show_type" name="desc_search_show_type"></a>

### `search_show_type`

Controls whether the source plugin or result type is shown in search results.

<a id="desc_search_separator" name="desc_search_separator"></a>

### `search_separator`

Separator used between search-result type subgroups.

<a id="desc_search_def_keytype" name="desc_search_def_keytype"></a>

### `search_def_keytype`

Default matching method: `all` requires every term, `any` permits one or more terms, and `phrase` matches the supplied phrase.

<a id="desc_search_def_sort" name="desc_search_def_sort"></a>

### `search_def_sort`

Default ordering of search results; the 2.2.2 reference uses descending hits.

<a id="desc_search_use_topic" name="desc_search_use_topic"></a>

### `search_use_topic`

If enabled, search can default to the most recently visited topic; otherwise it defaults to all topics.


## Advanced theme settings — Geeklog 2.2.2

These settings describe the historical [bundled 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html); they should be reviewed on a staging installation and must not be interpreted as current security defaults.

<a id="theme_advanced" name="theme_advanced"></a>

<a id="desc_show_right_blocks" name="desc_show_right_blocks"></a>

### `show_right_blocks`

When enabled, shows the right-side block column on all site pages instead of limiting it to the homepage.

<a id="desc_showfirstasfeatured" name="desc_showfirstasfeatured"></a>

### `showfirstasfeatured`

When enabled, renders the first article on any article listing page using featured-article templates, even when the article itself is not marked as featured.

<a id="desc_template_comments" name="desc_template_comments"></a>

### `template_comments`

Controls whether internal template comments are preserved as HTML comments rather than removed. The 2.2.2 reference also describes extra template-path diagnostic output for `Root` users under specific template debugging settings. Avoid enabling diagnostic output on production sites.


## Cookies and sessions — Geeklog 2.2.2

These settings describe the historical [bundled 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html); they should be reviewed on a staging installation and must not be interpreted as current security defaults.

<a id="misc" name="misc"></a>
<a id="misc_cookies" name="misc_cookies"></a>

<a id="desc_cookie_session" name="desc_cookie_session"></a>

### `cookie_session`

Name of the cookie storing the session identifier; historical reference default `gl_session`.

<a id="desc_cookie_name" name="desc_cookie_name"></a>

### `cookie_name`

Name of the persistent site cookie; the 2.2.2 reference uses `geeklog`.

<a id="desc_cookie_password" name="desc_cookie_password"></a>

### `cookie_password`

Name used for the historical password-related cookie. This describes a legacy configuration identifier, not a recommended modern credential-storage pattern.

<a id="desc_cookie_theme" name="desc_cookie_theme"></a>

### `cookie_theme`

Cookie name for the selected theme.

<a id="desc_cookie_language" name="desc_cookie_language"></a>

### `cookie_language`

Cookie name for the selected language.

<a id="desc_cookie_tzid" name="desc_cookie_tzid"></a>

### `cookie_tzid`

Cookie name used for the selected time zone.

<a id="desc_cookie_anon_name" name="desc_cookie_anon_name"></a>

### `cookie_anon_name`

Cookie name for the name supplied by an anonymous commenter.

<a id="desc_cookie_ip" name="desc_cookie_ip"></a>

### `cookie_ip`

Legacy option for associating the session ID with the visitor's IP address. The 2.2.2 reference notes that enabling it can cause users whose IP changes to log in again; do not assume it replaces current session-security controls.

<a id="desc_default_perm_cookie_timeout" name="desc_default_perm_cookie_timeout"></a>

### `default_perm_cookie_timeout`

Default automatic-login cookie duration, in seconds; historical default `28800` (8 hours). The reference describes its interaction with `session_cookie_timeout`.

<a id="desc_session_cookie_timeout" name="desc_session_cookie_timeout"></a>

### `session_cookie_timeout`

Inactivity timeout for the session cookie, in seconds; historical default `7200` (2 hours), with reference bounds of 300 to 86400 seconds.

<a id="desc_cookie_path" name="desc_cookie_path"></a>

### `cookie_path`

URL path scope for cookies, typically `/`.

<a id="desc_cookiedomain" name="desc_cookiedomain"></a>

### `cookiedomain`

Cookie domain scope. Geeklog's 2.2.2 reference says it attempts to derive the domain from `site_url`.

<a id="desc_cookiesecure" name="desc_cookiesecure"></a>

### `cookiesecure`

Controls whether the Secure cookie flag is used. For HTTPS deployments, protect authentication cookies with an appropriate Secure setting; do not treat the old `0` default as security guidance.


## General functionality and diagnostics — Geeklog 2.2.2

These settings describe the historical [bundled 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html); they should be reviewed on a staging installation and must not be interpreted as current security defaults.

<a id="misc_misc" name="misc_misc"></a>

<a id="desc_notification" name="desc_notification"></a>

### `notification`

Selects administrative email notifications for submissions and account events. The 2.2.2 reference lists event keys `article`, `comment`, `trackback`, `pingback`, `user` and `user_update`.

<a id="desc_cron_schedule_interval" name="desc_cron_schedule_interval"></a>

### `cron_schedule_interval`

Interval, in seconds, for Geeklog's visitor-triggered scheduled tasks; `0` disables. This internal mechanism depends on a homepage visit near the scheduled time, so lightly visited sites may run tasks late.

<a id="desc_disable_autolinks" name="desc_disable_autolinks"></a>

### `disable_autolinks`

When enabled, stops interpreting Geeklog content autotags such as `[article:]`.

<a id="desc_clickable_links" name="desc_clickable_links"></a>

### `clickable_links`

Controls automatic conversion of URLs in plaintext posts to clickable links.

<a id="desc_linktext_maxlen" name="desc_linktext_maxlen"></a>

### `linktext_maxlen`

Maximum displayed URL text length for auto-linked URLs; `0` means unlimited in the 2.2.2 reference.

<a id="desc_compressed_output" name="desc_compressed_output"></a>

### `compressed_output`

Experimental option to compress some HTML output when supported by browser and server. The bundled 2.2.2 reference states it is not implemented for all output.

<a id="desc_frame_options" name="desc_frame_options"></a>

### `frame_options`

Controls the `X-Frame-Options` anti-clickjacking header. The 2.2.2 reference offers deny, same-origin and disabled modes. Disabling frame restrictions can expose pages to framing risks.

<a id="desc_page_navigation_max_pages" name="desc_page_navigation_max_pages"></a>

### `page_navigation_max_pages`

Number of pagination links displayed on desktop; bundled default `7`, with permitted range from 3 to 20.

<a id="desc_page_navigation_mobile_max_pages" name="desc_page_navigation_mobile_max_pages"></a>

### `page_navigation_mobile_max_pages`

Number of pagination links shown on mobile; bundled default `7`. Different desktop/mobile page counts may require separated mobile caching when template caching is enabled.

<a id="desc_default_cache_time_block" name="desc_default_cache_time_block"></a>

### `default_cache_time_block`

Default block-cache policy: positive seconds specify a lifetime, `0` disables cache, and `-1` keeps cached content until the block is edited.

<a id="desc_titletoid" name="desc_titletoid"></a>

### `titletoid`

Enables automatically deriving content identifiers from titles in supporting article, topic and Static Pages editors.

<a id="desc_404_log" name="desc_404_log"></a>

### `404_log`

Controls logging of HTTP 404 errors into the `404.log` file in Geeklog's log directory.

<a id="misc_debug" name="misc_debug"></a>

<a id="desc_rootdebug" name="desc_rootdebug"></a>

### `rootdebug`

If enabled, PHP error details may be shown to all visitors instead of only `Root` users. **Keep disabled on production** to avoid leaking private information.


## Daily digest options — Geeklog 2.2.2

These settings describe the historical [bundled 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html); they should be reviewed on a staging installation and must not be interpreted as current security defaults.

<a id="misc_digest" name="misc_digest"></a>

<a id="desc_emailstories" name="desc_emailstories"></a>

### `emailstories`

Enables sending articles through Geeklog's legacy email digest feature; the 2.2.2 reference says it requires cron and PHP command-line execution.

<a id="desc_emailstorieslength" name="desc_emailstorieslength"></a>

### `emailstorieslength`

When the digest is enabled, `0` sends titles and links, `1` sends full article introductions, and other numeric values limit the number of introduction characters.

<a id="desc_emailstoriesperdefault" name="desc_emailstoriesperdefault"></a>

### `emailstoriesperdefault`

When enabled, newly registered accounts are automatically subscribed to the daily digest. Verify consent requirements before enabling.



## HTML filtering and safe content — Geeklog 2.2.2

Based on the [tagged configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Test behavior in a staging site before changing production settings, especially HTML filtering, permissions, uploads and external services.

<a id="misc_html" name="misc_html"></a>

<a id="desc_user_html" name="desc_user_html"></a>

### `user_html`

Allowed HTML tags and attributes for ordinary users in articles and comments. The 2.2.2 reference lists basic formatting tags; only add tags or attributes after considering script injection and unsafe URLs.

<a id="desc_admin_html" name="desc_admin_html"></a>

### `admin_html`

Extra tags and attributes allowed for administrators, in addition to `user_html`. Defining a tag again here can replace the ordinary-user attribute definition.

<a id="desc_advanced_html" name="desc_advanced_html"></a>

### `advanced_html`

Additional HTML tags and attributes permitted when the advanced rich-text editor is used. Review these allowances for unsafe markup.

<a id="desc_skip_html_filter_for_root" name="desc_skip_html_filter_for_root"></a>

### `skip_html_filter_for_root`

When enabled, `Root` members may bypass HTML filtering for their content. This is a security-sensitive option; keep filtering unless the risks have been evaluated.

<a id="desc_allowed_protocols" name="desc_allowed_protocols"></a>

### `allowed_protocols`

List of URL schemes allowed in HTML links. The 2.2.2 reference includes `http`, `https` and `ftp`; avoid untrusted executable schemes.


## Content censoring and IP lookup — Geeklog 2.2.2

Based on the [tagged configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Test behavior in a staging site before changing production settings, especially HTML filtering, permissions, uploads and external services.

<a id="misc_censoring" name="misc_censoring"></a>

<a id="desc_censormode" name="desc_censormode"></a>

### `censormode`

Controls word filtering: `0` disabled, `1` exact match, `2` word-start match and `3` substring match in the 2.2.2 reference.

<a id="desc_censorreplace" name="desc_censorreplace"></a>

### `censorreplace`

Text substituted for censored words; historically `*censored*`. The legacy filter may fail to detect words interrupted by HTML or BBCode markup.

<a id="desc_censorlist" name="desc_censorlist"></a>

### `censorlist`

List of terms checked by the censoring facility. Test false positives and the actual filter implementation before deployment.

<a id="misc_ip_lookup" name="misc_ip_lookup"></a>

<a id="desc_ip_lookup" name="desc_ip_lookup"></a>

### `ip_lookup`

Optional external IP lookup URL for administrative review of comment poster IPs. The historical setting uses `*` as the substitution marker; consider visitor privacy before sending an address to a third-party service.


## Webservices API controls — Geeklog 2.2.2

Based on the [tagged configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Test behavior in a staging site before changing production settings, especially HTML filtering, permissions, uploads and external services.

<a id="misc_ip_webservices" name="misc_ip_webservices"></a>

<a id="desc_disable_webservices" name="desc_disable_webservices"></a>

### `disable_webservices`

Setting `true` disables the Geeklog webservices facility in the 2.2.2 reference.

<a id="desc_restrict_webservices" name="desc_restrict_webservices"></a>

### `restrict_webservices`

When enabled, limits webservices access to users with the `webservices.atompub` permission, such as a properly configured Webservices Users group.

<a id="desc_atom_max_stories" name="desc_atom_max_stories"></a>

### `atom_max_stories`

Maximum number of articles returned by an Atom webservices feed request; documented default `10`.


## Topic breadcrumb controls — Geeklog 2.2.2

Based on the [tagged configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Test behavior in a staging site before changing production settings, especially HTML filtering, permissions, uploads and external services.

<a id="misc_topics" name="misc_topics"></a>

<a id="desc_multiple_breadcrumbs" name="desc_multiple_breadcrumbs"></a>

### `multiple_breadcrumbs`

Show more than one breadcrumb trail when available.

<a id="desc_disable_breadcrumbs_topics" name="desc_disable_breadcrumbs_topics"></a>

### `disable_breadcrumbs_topics`

Suppress breadcrumbs associated with topic pages when enabled.

<a id="desc_disable_breadcrumbs_articles" name="desc_disable_breadcrumbs_articles"></a>

### `disable_breadcrumbs_articles`

Suppress breadcrumbs associated with article pages when enabled.

<a id="desc_disable_breadcrumbs_plugins" name="desc_disable_breadcrumbs_plugins"></a>

### `disable_breadcrumbs_plugins`

Suppress breadcrumbs generated by plugins when enabled.

<a id="desc_breadcrumb_root_site_name" name="desc_breadcrumb_root_site_name"></a>

### `breadcrumb_root_site_name`

Display the site name as the root entry of breadcrumb navigation when enabled.


## File manager — display and server behavior — Geeklog 2.2.2

Based on the [tagged configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Test behavior in a staging site before changing production settings, especially HTML filtering, permissions, uploads and external services.

<a id="filemanager" name="filemanager"></a>
<a id="filemanager_general" name="filemanager_general"></a>

<a id="desc_filemanager_disabled" name="desc_filemanager_disabled"></a>

### `filemanager_disabled`

Disable the file manager for ordinary users when enabled; the 2.2.2 reference specifies that `Root` members retain access.

<a id="desc_filemanager_browse_only" name="desc_filemanager_browse_only"></a>

### `filemanager_browse_only`

Enable read-only browsing in the file manager.

<a id="desc_filemanager_default_view_mode" name="desc_filemanager_default_view_mode"></a>

### `filemanager_default_view_mode`

Default file manager layout: `grid` or `list`.

<a id="desc_filemanager_show_confirmation" name="desc_filemanager_show_confirmation"></a>

### `filemanager_show_confirmation`

Show a confirmation message for file manager operations when enabled.

<a id="desc_filemanager_search_box" name="desc_filemanager_search_box"></a>

### `filemanager_search_box`

Show the file manager search field when enabled.

<a id="desc_filemanager_file_sorting" name="desc_filemanager_file_sorting"></a>

### `filemanager_file_sorting`

File/folder sorting by name, type or modification date, each ascending or descending.

<a id="desc_filemanager_chars_only_latin" name="desc_filemanager_chars_only_latin"></a>

### `filemanager_chars_only_latin`

Control whether non-Latin characters are allowed in folder names. Verify the exact boolean interpretation before changing this historic option.

<a id="desc_filemanager_date_format" name="desc_filemanager_date_format"></a>

### `filemanager_date_format`

Format of dates shown in the file manager; the bundled default uses `yMMMdHm`.

<a id="desc_filemanager_logger" name="desc_filemanager_logger"></a>

### `filemanager_logger`

Log file manager server-side actions in Geeklog's error log when enabled. Avoid exposing sensitive file paths in public logs.

<a id="desc_filemanager_show_thumbs" name="desc_filemanager_show_thumbs"></a>

### `filemanager_show_thumbs`

Show thumbnails of supported files when enabled.

<a id="desc_filemanager_generate_thumbnails" name="desc_filemanager_generate_thumbnails"></a>

### `filemanager_generate_thumbnails`

Generate thumbnail images using PHP for faster directory browsing. The reference places them in an internal `_thumbs` directory.


## File manager — uploads and media — Geeklog 2.2.2

Based on the [tagged configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Test behavior in a staging site before changing production settings, especially HTML filtering, permissions, uploads and external services.

<a id="filemanager_upload" name="filemanager_upload"></a>

<a id="desc_filemanager_upload_overwrite" name="desc_filemanager_upload_overwrite"></a>

### `filemanager_upload_overwrite`

Overwrite an existing file with the same name when enabled; otherwise append an index to the uploaded filename. Review permissions before enabling overwrites.

<a id="desc_filemanager_upload_file_size_limit" name="desc_filemanager_upload_file_size_limit"></a>

### `filemanager_upload_file_size_limit`

Maximum upload size checked by the HTML5 client and PHP connector, in MiB; bundled default `16`. Server-side PHP limits may further restrict uploads.

<a id="filemanager_images" name="filemanager_images"></a>

<a id="desc_filemanager_images_ext" name="desc_filemanager_images_ext"></a>

### `filemanager_images_ext`

Allowed image filename extensions in the file manager; the 2.2.2 reference lists `jpg`, `jpeg`, `gif`, `png` and `svg`. Extension checks alone are not sufficient file-content validation.

<a id="filemanager_videos" name="filemanager_videos"></a>

<a id="desc_filemanager_show_video_player" name="desc_filemanager_show_video_player"></a>

### `filemanager_show_video_player`

Show the browser-based video player for supported video files.

<a id="desc_filemanager_videos_ext" name="desc_filemanager_videos_ext"></a>

### `filemanager_videos_ext`

Video filename extensions supported by the built-in player; the 2.2.2 reference lists `ogv`, `mp4`, `webm`.

<a id="desc_filemanager_videos_player_width" name="desc_filemanager_videos_player_width"></a>

### `filemanager_videos_player_width`

Width in pixels for the embedded video player; historical default `400`.

<a id="desc_filemanager_videos_player_height" name="desc_filemanager_videos_player_height"></a>

### `filemanager_videos_player_height`

Height in pixels for the embedded video player; historical default `222`.

<a id="filemanager_audios" name="filemanager_audios"></a>

<a id="desc_filemanager_show_audio_player" name="desc_filemanager_show_audio_player"></a>

### `filemanager_show_audio_player`

Show the browser-based audio player for supported audio files.

<a id="desc_filemanager_audios_ext" name="desc_filemanager_audios_ext"></a>

### `filemanager_audios_ext`

Audio filename extensions recognized by the player; the 2.2.2 reference lists `ogg`, `mp3` and `wav`.


## Default content permissions and autotag access — Geeklog 2.2.2

The following 44 help identifiers describe the **defaults** for content permissions and autotag usage in the [bundled Geeklog 2.2.2 reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html#misc_permissions). They are not recommendations to grant public users broader rights. Review effective group permissions and test with least-privileged accounts before changing production.

The suffixes `_0`, `_1`, `_2` and `_3` refer to distinct audience/role positions recorded by the original configuration page. Do not infer access solely from a setting name; the actual group and operation are important.

<a id="misc_permissions" name="misc_permissions"></a>

<a id="desc_default_permissions_story_0" name="desc_default_permissions_story_0"></a>

### `default_permissions_story_0`

**Bundled default:** Read-Write. Default permission for Owner of new articles. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_story_1" name="desc_default_permissions_story_1"></a>

### `default_permissions_story_1`

**Bundled default:** Read-Only. Default permission for Group of new articles. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_story_2" name="desc_default_permissions_story_2"></a>

### `default_permissions_story_2`

**Bundled default:** Read-Only. Default permission for all logged in users of new articles. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_story_3" name="desc_default_permissions_story_3"></a>

### `default_permissions_story_3`

**Bundled default:** Read-Only. Default permission for all anonymous visitors of new articles. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_topic_0" name="desc_default_permissions_topic_0"></a>

### `default_permissions_topic_0`

**Bundled default:** Read-Write. Default permission for Owner of new topics. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_topic_1" name="desc_default_permissions_topic_1"></a>

### `default_permissions_topic_1`

**Bundled default:** Read-Only. Default permission for Group of new topics. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_topic_2" name="desc_default_permissions_topic_2"></a>

### `default_permissions_topic_2`

**Bundled default:** Read-Only. Default permission for all logged in users of new topics. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_topic_3" name="desc_default_permissions_topic_3"></a>

### `default_permissions_topic_3`

**Bundled default:** Read-Only. Default permission for all anonymous visitors of new topics. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_block_0" name="desc_default_permissions_block_0"></a>

### `default_permissions_block_0`

**Bundled default:** Read-Write. Default permission for Owner of new blocks. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_block_1" name="desc_default_permissions_block_1"></a>

### `default_permissions_block_1`

**Bundled default:** Read-Only. Default permission for Group of new blocks. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_block_2" name="desc_default_permissions_block_2"></a>

### `default_permissions_block_2`

**Bundled default:** Read-Only. Default permission for all logged in users of new blocks. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_default_permissions_block_3" name="desc_default_permissions_block_3"></a>

### `default_permissions_block_3`

**Bundled default:** Read-Only. Default permission for all anonymous users of new blocks. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_story_0" name="desc_autotag_permissions_story_0"></a>

### `autotag_permissions_story_0`

**Bundled default:** Use. Usage permission for autotag by autotag Owner (Default Root User). This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_story_1" name="desc_autotag_permissions_story_1"></a>

### `autotag_permissions_story_1`

**Bundled default:** Use. Usage permission for autotag by Article Admin Group. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_story_2" name="desc_autotag_permissions_story_2"></a>

### `autotag_permissions_story_2`

**Bundled default:** Use. Usage permission for autotag by all logged in users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_story_3" name="desc_autotag_permissions_story_3"></a>

### `autotag_permissions_story_3`

**Bundled default:** Use. Usage permission for autotag by anonymous users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_user_0" name="desc_autotag_permissions_user_0"></a>

### `autotag_permissions_user_0`

**Bundled default:** Use. Usage permission for autotag by autotag Owner (Default Root User). This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_user_1" name="desc_autotag_permissions_user_1"></a>

### `autotag_permissions_user_1`

**Bundled default:** Use. Usage permission for autotag by User Admin Group. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_user_2" name="desc_autotag_permissions_user_2"></a>

### `autotag_permissions_user_2`

**Bundled default:** Use. Usage permission for autotag by all logged in users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_user_3" name="desc_autotag_permissions_user_3"></a>

### `autotag_permissions_user_3`

**Bundled default:** Use. Usage permission for autotag by anonymous users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_topic_0" name="desc_autotag_permissions_topic_0"></a>

### `autotag_permissions_topic_0`

**Bundled default:** Use. Usage permission for autotag by autotag Owner (Default Root User). This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_topic_1" name="desc_autotag_permissions_topic_1"></a>

### `autotag_permissions_topic_1`

**Bundled default:** Use. Usage permission for autotag by Topic Admin Group. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_topic_2" name="desc_autotag_permissions_topic_2"></a>

### `autotag_permissions_topic_2`

**Bundled default:** Use. Usage permission for autotag by all logged in users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_topic_3" name="desc_autotag_permissions_topic_3"></a>

### `autotag_permissions_topic_3`

**Bundled default:** Use. Usage permission for autotag by anonymous users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_related_topics_0" name="desc_autotag_permissions_related_topics_0"></a>

### `autotag_permissions_related_topics_0`

**Bundled default:** Use. Usage permission for autotag by autotag Owner (Default Root User). This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_related_topics_1" name="desc_autotag_permissions_related_topics_1"></a>

### `autotag_permissions_related_topics_1`

**Bundled default:** Use. Usage permission for autotag by Topic Admin Group. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_related_topics_2" name="desc_autotag_permissions_related_topics_2"></a>

### `autotag_permissions_related_topics_2`

**Bundled default:** No Access. Usage permission for autotag by all logged in users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_related_topics_3" name="desc_autotag_permissions_related_topics_3"></a>

### `autotag_permissions_related_topics_3`

**Bundled default:** No Access. Usage permission for autotag by anonymous users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_related_items_0" name="desc_autotag_permissions_related_items_0"></a>

### `autotag_permissions_related_items_0`

**Bundled default:** Use. Usage permission for autotag by autotag Owner (Default Root User). This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_related_items_1" name="desc_autotag_permissions_related_items_1"></a>

### `autotag_permissions_related_items_1`

**Bundled default:** Use. Usage permission for autotag by Topic Admin Group. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_related_items_2" name="desc_autotag_permissions_related_items_2"></a>

### `autotag_permissions_related_items_2`

**Bundled default:** No Access. Usage permission for autotag by all logged in users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_related_items_3" name="desc_autotag_permissions_related_items_3"></a>

### `autotag_permissions_related_items_3`

**Bundled default:** No Access. Usage permission for autotag by anonymous users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_block_0" name="desc_autotag_permissions_block_0"></a>

### `autotag_permissions_block_0`

**Bundled default:** Use. Usage permission for autotag by autotag Owner (Default Root User). This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_block_1" name="desc_autotag_permissions_block_1"></a>

### `autotag_permissions_block_1`

**Bundled default:** Use. Usage permission for autotag by Block Admin Group. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_block_2" name="desc_autotag_permissions_block_2"></a>

### `autotag_permissions_block_2`

**Bundled default:** No Access. Usage permission for autotag by all logged in users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_block_3" name="desc_autotag_permissions_block_3"></a>

### `autotag_permissions_block_3`

**Bundled default:** No access. Usage permission for autotag by anonymous users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_structureddata_0" name="desc_autotag_permissions_structureddata_0"></a>

### `autotag_permissions_structureddata_0`

**Bundled default:** Use. Usage permission for autotag by autotag Owner (Default Root User). This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_structureddata_1" name="desc_autotag_permissions_structureddata_1"></a>

### `autotag_permissions_structureddata_1`

**Bundled default:** Use. Usage permission for autotag by Root Group. Please note, changing this will not affect permissions since the Root Group automatically has access to everything. To give usage permissions for this autotag to other Security Groups, assign them the feature structureddata.autotag . This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_structureddata_2" name="desc_autotag_permissions_structureddata_2"></a>

### `autotag_permissions_structureddata_2`

**Bundled default:** No Access. Usage permission for autotag by all logged in users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_structureddata_3" name="desc_autotag_permissions_structureddata_3"></a>

### `autotag_permissions_structureddata_3`

**Bundled default:** No access. Usage permission for autotag by anonymous users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_likes_block_0" name="desc_autotag_permissions_likes_block_0"></a>

### `autotag_permissions_likes_block_0`

**Bundled default:** Use. Usage permission for autotag by autotag Owner (Default Root User). This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_likes_block_1" name="desc_autotag_permissions_likes_block_1"></a>

### `autotag_permissions_likes_block_1`

**Bundled default:** Use. Usage permission for autotag by Blocks Admin Group. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_likes_block_2" name="desc_autotag_permissions_likes_block_2"></a>

### `autotag_permissions_likes_block_2`

**Bundled default:** No Access. Usage permission for autotag by all logged in users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.

<a id="desc_autotag_permissions_likes_block_3" name="desc_autotag_permissions_likes_block_3"></a>

### `autotag_permissions_likes_block_3`

**Bundled default:** No Access. Usage permission for autotag by anonymous users. This is a version-specific initial permission; the effective permission may differ on an upgraded or customized site.



## Articles — structured data and related content — Geeklog 2.2.2

Version-scoped documentation adapted from the [tagged Geeklog configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Do not assume historical external identity or ping services remain supported.

<a id="desc_structured_data_type_default" name="desc_structured_data_type_default"></a>

### `structured_data_type_default`

Selects the default structured-data type for new articles. The 2.2.2 reference offers `none`, `core-webpage`, `core-article`, `core-newsarticle`, and `core-blogposting`. Full-article pages may expose JSON-LD; validate actual markup before release.

<a id="desc_structured_data_article_topic" name="desc_structured_data_article_topic"></a>

### `structured_data_article_topic`

Controls whether article structured data is included on home/topic listings as well as full article pages; the historical reference describes `1` enabled and `0` disabled.

<a id="desc_aftersave_story" name="desc_aftersave_story"></a>

### `aftersave_story`

Where the administrator is sent after saving an article: `item`, `list`, `home` or `admin`. Editing a queued submission continues to return to moderation, regardless of this setting.

<a id="desc_related_topics" name="desc_related_topics"></a>

### `related_topics`

Controls whether related topics are shown on articles, article and topic pages, or neither; verify exact choices in the installed configuration UI.

<a id="desc_related_topics_max" name="desc_related_topics_max"></a>

### `related_topics_max`

Maximum number of related topics to display; `0` means no limit.

<a id="desc_whats_related" name="desc_whats_related"></a>

### `whats_related`

Controls the What's Related block on article pages, including filtering of internal/external article links.

<a id="desc_whats_related_max" name="desc_whats_related_max"></a>

### `whats_related_max`

Maximum number of related links displayed on an article; `0` requests all available items, with a minimum of two items for display in the historical reference.

<a id="desc_whats_related_trim" name="desc_whats_related_trim"></a>

### `whats_related_trim`

Maximum displayed length of related-item titles. A value of `0` disables truncation; changing the option can rebuild stored related links.

<a id="desc_default_cache_time_article" name="desc_default_cache_time_article"></a>

### `default_cache_time_article`

Default article cache policy: positive seconds for an expiry, `0` to regenerate for each request, or `-1` to keep the cached article until it is edited.

<a id="desc_blocks_article_topic_list_repeat_after" name="desc_blocks_article_topic_list_repeat_after"></a>

### `blocks_article_topic_list_repeat_after`

Number of article introductions after which the Article Topic List block location repeats; `0` disables that block placement.


## Trackbacks and pingbacks — legacy integration — Geeklog 2.2.2

Version-scoped documentation adapted from the [tagged Geeklog configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Do not assume historical external identity or ping services remain supported.

<a id="stories_trackback" name="stories_trackback"></a>

<a id="desc_trackback_enabled" name="desc_trackback_enabled"></a>

### `trackback_enabled`

Enables or disables sending and receiving trackback comments. The original source contains a boolean wording typo; treat `true` as enabled and check runtime behavior before changing it.

<a id="desc_trackback_code" name="desc_trackback_code"></a>

### `trackback_code`

Default setting for new articles: `0` accepts trackbacks, `-1` disables them.

<a id="desc_trackbackspeedlimit" name="desc_trackbackspeedlimit"></a>

### `trackbackspeedlimit`

Minimum number of seconds between trackbacks or pingbacks originating from the same IP address; historical default `300`.

<a id="desc_check_trackback_link" name="desc_check_trackback_link"></a>

### `check_trackback_link`

Selects anti-spam validation of incoming trackbacks, including backlink presence and possibly sender IP checks. Check the exact option modes in the tagged source before relying on the protection.

<a id="desc_multiple_trackbacks" name="desc_multiple_trackbacks"></a>

### `multiple_trackbacks`

Handling repeated trackbacks/pingbacks from a source: `0` keep the first, `1` replace with the latest, `2` allow multiple.

<a id="stories_pingback" name="stories_pingback"></a>

<a id="desc_pingback_enabled" name="desc_pingback_enabled"></a>

### `pingback_enabled`

Enables or disables sending and receiving pingbacks; the original description contains an apparent boolean typo.

<a id="desc_pingback_excerpt" name="desc_pingback_excerpt"></a>

### `pingback_excerpt`

When enabled, Geeklog attempts to retrieve the linking page and extract an excerpt for a pingback, since pingbacks do not transmit one themselves.

<a id="desc_pingback_self" name="desc_pingback_self"></a>

### `pingback_self`

Controls processing of pingbacks that point to other pages on the same site; the historical source documents `0` as skipping these.

<a id="desc_ping_enabled" name="desc_ping_enabled"></a>

### `ping_enabled`

Enables sending notifications to historical weblog-directory ping services; availability of old external services is not guaranteed.


## User registration, identity and profile options — Geeklog 2.2.2

Version-scoped documentation adapted from the [tagged Geeklog configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Do not assume historical external identity or ping services remain supported.

<a id="users" name="users"></a>
<a id="users_users" name="users_users"></a>

<a id="desc_disable_new_user_registration" name="desc_disable_new_user_registration"></a>

### `disable_new_user_registration`

When enabled, disables public registration of new Geeklog accounts.

<a id="desc_allow_user_themes" name="desc_allow_user_themes"></a>

### `allow_user_themes`

Allows registered users to select a site theme in their account preferences when enabled.

<a id="desc_allow_user_photo" name="desc_allow_user_photo"></a>

### `allow_user_photo`

Allows users to upload a profile photograph when enabled.

<a id="desc_allow_username_change" name="desc_allow_username_change"></a>

### `allow_username_change`

Allows account holders to change their login username. The 2.2.2 reference says article/comment bylines are updated to use the new username.

<a id="desc_allow_account_delete" name="desc_allow_account_delete"></a>

### `allow_account_delete`

Allows users to delete their own accounts. The historical reference says existing articles and comments are retained but attributed to Anonymous.

<a id="desc_hide_author_exclusion" name="desc_hide_author_exclusion"></a>

### `hide_author_exclusion`

Hides the preference for excluding selected authors' content from a user's view.

<a id="desc_show_fullname" name="desc_show_fullname"></a>

### `show_fullname`

Controls whether an account's full name is shown instead of its username; the username is used when no full name is supplied.

<a id="desc_require_user_email" name="desc_require_user_email"></a>

### `require_user_email`

Requires accounts lacking an email address to provide and verify one before continued authenticated use; remote login providers may not supply email.

<a id="desc_show_servicename" name="desc_show_servicename"></a>

### `show_servicename`

Appends a remote authentication service identifier to a username, helping distinguish local and remotely authenticated accounts.

<a id="desc_custom_registration" name="desc_custom_registration"></a>

### `custom_registration`

Enables a custom account registration form provided by site code, such as custom hooks in `lib-custom.php`.

<a id="desc_user_login_method_standard" name="desc_user_login_method_standard"></a>

### `user_login_method_standard`

Controls login by a local Geeklog account stored in the site's database.

<a id="desc_user_login_method_openid" name="desc_user_login_method_openid"></a>

### `user_login_method_openid`

Enables the historical OpenID login integration. The 2.2.2 reference notes that account approval queues can disable this login path. Compatibility with today's identity providers is unverified.

<a id="desc_user_login_method_3rdparty" name="desc_user_login_method_3rdparty"></a>

### `user_login_method_3rdparty`

Enables external account authentication, including the historical LDAP integration, where the provider and necessary authorization settings are configured.

<a id="desc_user_login_method_oauth" name="desc_user_login_method_oauth"></a>

### `user_login_method_oauth`

Enables the built-in legacy OAuth login methods. This 2.2.2 feature is **not proof of compatibility with current provider APIs**; test each connection with up-to-date credentials and endpoints.

<a id="desc_aftersave_user" name="desc_aftersave_user"></a>

### `aftersave_user`

Administrator destination after saving a user record: `item`, `list`, `home`, or `admin`, as listed by the original reference.

<a id="users_spamx" name="users_spamx"></a>

<a id="desc_spamx" name="desc_spamx"></a>

### `spamx`

Bitmask selecting actions that the Spam-X plugin runs when spam is detected. The 2.2.2 reference documents `128` for its delete action; inspect installed plugin modules before combining bit flags.



## Historic OAuth provider settings — Geeklog 2.2.2

These descriptions are scoped to the [versioned source reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Provider integrations and bootstrap settings need separate operational checks before a live change.

<a id="desc_google_login" name="desc_google_login"></a>

### `google_login`

Enables the historical Google OAuth login integration when supported by the specific Geeklog 2.2.2 configuration and an authorized provider application. **Do not assume compatibility with the provider's present-day OAuth APIs**; verify endpoints, callback URL, scopes and the installed login implementation.

<a id="desc_google_consumer_key" name="desc_google_consumer_key"></a>

### `google_consumer_key`

Application/client identifier for the historical Google login integration. Configure it through the administrator's secure settings, not in published documentation or debug logs.

<a id="desc_google_consumer_secret" name="desc_google_consumer_secret"></a>

### `google_consumer_secret`

Application/client secret for the historical Google login integration. Keep it private and rotate if exposed; do not include actual secrets in examples or commits.

<a id="desc_facebook_login" name="desc_facebook_login"></a>

### `facebook_login`

Enables the historical Facebook OAuth login integration when supported by the specific Geeklog 2.2.2 configuration and an authorized provider application. **Do not assume compatibility with the provider's present-day OAuth APIs**; verify endpoints, callback URL, scopes and the installed login implementation.

<a id="desc_facebook_consumer_key" name="desc_facebook_consumer_key"></a>

### `facebook_consumer_key`

Application/client identifier for the historical Facebook login integration. Configure it through the administrator's secure settings, not in published documentation or debug logs.

<a id="desc_facebook_consumer_secret" name="desc_facebook_consumer_secret"></a>

### `facebook_consumer_secret`

Application/client secret for the historical Facebook login integration. Keep it private and rotate if exposed; do not include actual secrets in examples or commits.

<a id="desc_linkedin_login" name="desc_linkedin_login"></a>

### `linkedin_login`

Enables the historical Linkedin OAuth login integration when supported by the specific Geeklog 2.2.2 configuration and an authorized provider application. **Do not assume compatibility with the provider's present-day OAuth APIs**; verify endpoints, callback URL, scopes and the installed login implementation.

<a id="desc_linkedin_consumer_key" name="desc_linkedin_consumer_key"></a>

### `linkedin_consumer_key`

Application/client identifier for the historical Linkedin login integration. Configure it through the administrator's secure settings, not in published documentation or debug logs.

<a id="desc_linkedin_consumer_secret" name="desc_linkedin_consumer_secret"></a>

### `linkedin_consumer_secret`

Application/client secret for the historical Linkedin login integration. Keep it private and rotate if exposed; do not include actual secrets in examples or commits.

<a id="desc_twitter_login" name="desc_twitter_login"></a>

### `twitter_login`

Enables the historical Twitter OAuth login integration when supported by the specific Geeklog 2.2.2 configuration and an authorized provider application. **Do not assume compatibility with the provider's present-day OAuth APIs**; verify endpoints, callback URL, scopes and the installed login implementation.

<a id="desc_twitter_consumer_key" name="desc_twitter_consumer_key"></a>

### `twitter_consumer_key`

Application/client identifier for the historical Twitter login integration. Configure it through the administrator's secure settings, not in published documentation or debug logs.

<a id="desc_twitter_consumer_secret" name="desc_twitter_consumer_secret"></a>

### `twitter_consumer_secret`

Application/client secret for the historical Twitter login integration. Keep it private and rotate if exposed; do not include actual secrets in examples or commits.

<a id="desc_microsoft_login" name="desc_microsoft_login"></a>

### `microsoft_login`

Enables the historical Microsoft OAuth login integration when supported by the specific Geeklog 2.2.2 configuration and an authorized provider application. **Do not assume compatibility with the provider's present-day OAuth APIs**; verify endpoints, callback URL, scopes and the installed login implementation.

<a id="desc_microsoft_consumer_key" name="desc_microsoft_consumer_key"></a>

### `microsoft_consumer_key`

Application/client identifier for the historical Microsoft login integration. Configure it through the administrator's secure settings, not in published documentation or debug logs.

<a id="desc_microsoft_consumer_secret" name="desc_microsoft_consumer_secret"></a>

### `microsoft_consumer_secret`

Application/client secret for the historical Microsoft login integration. Keep it private and rotate if exposed; do not include actual secrets in examples or commits.

<a id="desc_yahoo_login" name="desc_yahoo_login"></a>

### `yahoo_login`

Enables the historical Yahoo OAuth login integration when supported by the specific Geeklog 2.2.2 configuration and an authorized provider application. **Do not assume compatibility with the provider's present-day OAuth APIs**; verify endpoints, callback URL, scopes and the installed login implementation.

<a id="desc_yahoo_consumer_key" name="desc_yahoo_consumer_key"></a>

### `yahoo_consumer_key`

Application/client identifier for the historical Yahoo login integration. Configure it through the administrator's secure settings, not in published documentation or debug logs.

<a id="desc_yahoo_consumer_secret" name="desc_yahoo_consumer_secret"></a>

### `yahoo_consumer_secret`

Application/client secret for the historical Yahoo login integration. Keep it private and rotate if exposed; do not include actual secrets in examples or commits.

<a id="desc_github_login" name="desc_github_login"></a>

### `github_login`

Enables the historical Github OAuth login integration when supported by the specific Geeklog 2.2.2 configuration and an authorized provider application. **Do not assume compatibility with the provider's present-day OAuth APIs**; verify endpoints, callback URL, scopes and the installed login implementation.

<a id="desc_github_consumer_key" name="desc_github_consumer_key"></a>

### `github_consumer_key`

Application/client identifier for the historical Github login integration. Configure it through the administrator's secure settings, not in published documentation or debug logs.

<a id="desc_github_consumer_secret" name="desc_github_consumer_secret"></a>

### `github_consumer_secret`

Application/client secret for the historical Github login integration. Keep it private and rotate if exposed; do not include actual secrets in examples or commits.


## Likes and dynamic likes block — Geeklog 2.2.2

These descriptions are scoped to the [versioned source reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Provider integrations and bootstrap settings need separate operational checks before a live change.

<a id="desc_likes_enabled" name="desc_likes_enabled"></a>

### `likes_enabled`

Likes facility scope: `0` disabled, `1` registered and anonymous visitors, `2` registered users only. The historical reference identifies anonymous users using IP address, which warrants privacy consideration.

<a id="desc_likes_articles" name="desc_likes_articles"></a>

### `likes_articles`

Controls ratings on articles: `0` disabled, `1` likes and dislikes, or `2` likes only. The master `likes_enabled` option must also permit the feature.

<a id="desc_likes_comments" name="desc_likes_comments"></a>

### `likes_comments`

Controls ratings on comments: `0` disabled, `1` likes and dislikes, or `2` likes only; requires the master likes setting.

<a id="desc_likes_speedlimit" name="desc_likes_speedlimit"></a>

### `likes_speedlimit`

Minimum time between rating actions by a visitor, in seconds; historical default `45`.

<a id="desc_likes_users_listed" name="desc_likes_users_listed"></a>

### `likes_users_listed`

Maximum number of recent users shown in a tooltip for an item's likes/dislikes. `0` disables user listing.

<a id="desc_likes_block_enable" name="desc_likes_block_enable"></a>

### `likes_block_enable`

Enables the dynamic block highlighting recently liked or disliked content based on the options below.

<a id="desc_likes_block_isleft" name="desc_likes_block_isleft"></a>

### `likes_block_isleft`

Displays the dynamic likes block on the left when `1`, or on the right when `0`.

<a id="desc_likes_block_order" name="desc_likes_block_order"></a>

### `likes_block_order`

Position of the dynamic likes block within its column; historical default `10`.

<a id="desc_likes_block_topic_option" name="desc_likes_block_topic_option"></a>

### `likes_block_topic_option`

Where the likes block appears: all pages, homepage only or selected topics. This controls placement, not which rated items qualify.

<a id="desc_likes_block_topic" name="desc_likes_block_topic"></a>

### `likes_block_topic`

Topic selection used when the likes block's placement mode is set to selected topics.

<a id="desc_likes_block_cache_time" name="desc_likes_block_cache_time"></a>

### `likes_block_cache_time`

Maximum lifetime of the dynamic likes block's cache, in seconds; `0` disables caching.

<a id="desc_likes_block_displayed_actions" name="desc_likes_block_displayed_actions"></a>

### `likes_block_displayed_actions`

Include likes and dislikes (`3`), likes only (`1`) or dislikes only (`2`) in the dynamic block's ranking.

<a id="desc_likes_block_include_time" name="desc_likes_block_include_time"></a>

### `likes_block_include_time`

Age window for rating activity considered by the block, in seconds; historical default `604800` (one week), `0` includes all time.

<a id="desc_likes_block_max_items" name="desc_likes_block_max_items"></a>

### `likes_block_max_items`

Maximum number of content items displayed in the dynamic likes block; historical default `10`.

<a id="desc_likes_block_title_trim_length" name="desc_likes_block_title_trim_length"></a>

### `likes_block_title_trim_length`

Maximum displayed item title length in the dynamic likes block; historical default `20`.

<a id="desc_likes_block_likes_new_line" name="desc_likes_block_likes_new_line"></a>

### `likes_block_likes_new_line`

Displays the likes/dislikes count on a separate line below the item title when enabled.

<a id="desc_likes_block_type" name="desc_likes_block_type"></a>

### `likes_block_type`

Optional filter by a single liked-item type such as article, comment, poll or plugin-defined type. Empty includes all supported types.

<a id="desc_likes_block_subtype" name="desc_likes_block_subtype"></a>

### `likes_block_subtype`

Optional subtype filter when the selected item type supports multiple subtypes, for example forum posts.

<a id="desc_likes_block_group_id" name="desc_likes_block_group_id"></a>

### `likes_block_group_id`

Security group associated with the dynamic likes block's permissions; the 2.2.2 reference uses Block Admin.

<a id="desc_likes_block_permissions_0" name="desc_likes_block_permissions_0"></a>

### `likes_block_permissions_0`

View permission for the owner of the dynamic likes block. Original reference default: Read-Only.

<a id="desc_likes_block_permissions_1" name="desc_likes_block_permissions_1"></a>

### `likes_block_permissions_1`

View permission for the configured administrator group of the dynamic likes block. Original reference default: Read-Only.

<a id="desc_likes_block_permissions_2" name="desc_likes_block_permissions_2"></a>

### `likes_block_permissions_2`

View permission for authenticated users of the dynamic likes block. Original reference default: Read-Only.

<a id="desc_likes_block_permissions_3" name="desc_likes_block_permissions_3"></a>

### `likes_block_permissions_3`

View permission for anonymous visitors of the dynamic likes block. Original reference default: Read-Only.


## Bootstrap settings in siteconfig.php — Geeklog 2.2.2

These descriptions are scoped to the [versioned source reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Provider integrations and bootstrap settings need separate operational checks before a live change.

<a id="siteconfig.php" name="siteconfig.php"></a>

<a id="desc_path" name="desc_path"></a>

### `path`

Installation root filesystem path in `siteconfig.php` (trailing slash required), outside the assumption that the web document root is the full Geeklog installation.

<a id="desc_path_system" name="desc_path_system"></a>

### `path_system`

Absolute filesystem path to Geeklog's `system/` code libraries in `siteconfig.php` (trailing slash required).

<a id="desc_site_enabled" name="desc_site_enabled"></a>

### `site_enabled`

Fast maintenance switch in `siteconfig.php`: set to `false` to disable access; the user-facing message is configured by `site_disabled_msg`.

<a id="desc_default_charset" name="desc_default_charset"></a>

### `default_charset`

Fallback character encoding when the selected language file does not specify one. The 2.2.2 reference mentions a historical ISO-8859-1 default but recommends UTF-8 for multilingual installations; verify actual database and language encodings.

<a id="desc_rootdebug_siteconfig" name="desc_rootdebug_siteconfig"></a>

### `rootdebug_siteconfig`

Emergency diagnostic override in `siteconfig.php`. The special `force` mode may expose extremely sensitive information, including credentials or cookies. **Never leave this enabled on a public site.**



## Historical configuration reference appendices — migration preview

These reference sections retain their original fragment identifiers, but some legacy tables and operational examples are **not yet fully transcribed**. The embedded v2.2.2 `config.html` remains the authoritative complete version until final content review.

<a id="db-config.php" name="db-config.php"></a>

### Database bootstrap configuration

The installation's `db-config.php` stores connection parameters such as the database host, name, user, password, table prefix and database type. These are installation-sensitive values, not safe defaults to copy into an existing site. Do not expose this file or credentials.

<a id="url-rewrite" name="url-rewrite"></a>

### URL rewriting

Geeklog 2.2.2 supports rewritten links for articles, topic pages, Static Pages and selected plugin resources. The exact legacy URL mapping table is retained in the original embedded reference while conversion and regression tests remain incomplete. Check old links and server handling before switching.

<a id="url-routing" name="url-routing"></a>

### URL routing

URL routing builds on URL rewriting and can use `index.php` as a front controller. It requires URL rewriting first, and server rules may be needed to omit `index.php`. The complete route and priority table must still be migrated and tested.

<a id="Localization" name="Localization"></a>

### Language-file localization

Geeklog ships interface strings in language files, such as `english.php`. Interface translation is distinct from translating site content. Check that locale settings, language file names, encodings and user-selectable languages align.

<a id="date_formats" name="date_formats"></a>

### Locale and date format reference

Date formats are version- and locale-dependent. The original 2.2.2 reference includes a detailed table of formatting tokens, including `%a`, `%A`, `%b`, `%B`, `%d`, `%H`, `%I`, `%m`, `%M`, `%p` and `%Y`. That full table still requires editorial migration; retain the legacy reference until it is complete.

<a id="url-cron" name="url-cron"></a>

### Command-line scheduled jobs

Geeklog 2.2.2 documents command-line PHP scripts for tasks such as daily digests and emailed database backups. Scripts should remain outside the public web tree. Review script paths, CLI availability and scheduler configuration on the installed environment.

<a id="cron_daily_digest" name="cron_daily_digest"></a>

### Daily-digest cron script

The historical `cron-emailgeeklogdailydigest` sends newly published articles to subscribers. On first activation, older articles may all be considered new; review the latest digest marker and test delivery carefully in staging.

<a id="cron_emailed_database_backup" name="cron_emailed_database_backup"></a>

### Email-based database backup cron script

The historical `cron-emailgeeklogdatabasebackup` sends a database dump to an address configured by the cron script or a `db_backup_sendto` value. Email attachments are not a substitute for a complete, encrypted, regularly tested backup strategy.

