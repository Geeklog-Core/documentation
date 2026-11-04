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


## Articles and presentation — Geeklog 2.2.2

Source: [bundled Geeklog 2.2.2 configuration reference](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/docs/english/config.html). Descriptions reflect this specific release; do not apply old security defaults to newer deployments.

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

<a id="desc_sort_admin" name="desc_sort_admin"></a>

### `sort_admin`

Sort entries in the Administrator block and Command and Control icons alphabetically when enabled.

<a id="desc_link_documentation" name="desc_link_documentation"></a>

### `link_documentation`

Show the Geeklog documentation link in the administrator block when set to `1`.

<a id="desc_link_versionchecker" name="desc_link_versionchecker"></a>

### `link_versionchecker`

Display the version-check link in the administrator block when enabled; the reference notes this is visible only to `Root` members.

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

<a id="desc_whosonline_threshold" name="desc_whosonline_threshold"></a>

### `whosonline_threshold`

Idle-time threshold, in seconds, after which a user is no longer listed in the Who's Online block; the 2.2.2 reference default is `300`.

<a id="desc_whosonline_anonymous" name="desc_whosonline_anonymous"></a>

### `whosonline_anonymous`

When enabled, anonymous visitors see only the count of registered users online rather than their names.

<a id="desc_whosonline_photo" name="desc_whosonline_photo"></a>

### `whosonline_photo`

When enabled, display a thumbnail of a user's uploaded photo where available, otherwise a photo icon.

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

