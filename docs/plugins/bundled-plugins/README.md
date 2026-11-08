# Bundled plugins reference

Geeklog 2.2.2 includes extensions for events, links, polls, spam filtering, static pages, sitemap generation and reCAPTCHA. The features available on a particular site depend on which plugins its administrator has enabled.

## Find the right plugin

| Plugin | Purpose | What to do |
| --- | --- | --- |
| Calendar | Publish events and display event information | Open Calendar administration if available; review event visibility and date before saving |
| Links | Maintain a directory of external resources | Add links in the appropriate category and verify that the target URL works |
| Polls | Ask questions and collect votes | Review the question, possible answers and voting restrictions before making a poll public |
| Spam-X | Apply configured anti-spam checks to supported content | Review filtering configuration and investigate false positives before changing rules |
| Static Pages | Publish independent informational pages | Follow the [Static Pages guide](../static-pages/index.html) for editing and access permissions |
| XMLSitemap | Produce a sitemap for search engines | Check the sitemap destination, file permissions and whether generated entries match public content |
| reCAPTCHA | Add supported anti-abuse verification to configured forms | Review the plugin's own configuration and ensure it works with the site's forms and policies |

Only install or enable a plugin when you understand its permissions, version compatibility and data changes. See [Plugin installation and management](../plugin-installation-management/index.html).

## Common administration tasks

### Publish an event with Calendar

1. Sign in with an account authorized to manage Calendar.
2. Open the plugin's event management screen.
3. Enter the event title, date and other details available in your installed version.
4. Review audience visibility, then save.
5. Check that the event is visible to the intended audience.

### Add a link or poll

For **Links**, choose the directory category, enter the link title and destination, and check the public listing. For **Polls**, review the question and available answers, confirm the allowed audience, then check the voting and results experience with a nonadministrator account. Do not use a privileged administrator session as proof of public visibility.

### Review spam protection and forms

For **Spam-X** and **reCAPTCHA**, test legitimate submissions as well as unwanted submissions using authorized test accounts. Check site logs before changing filtering rules. Never disable anti-abuse protections globally merely to investigate one rejected form.

### Check XMLSitemap output

After enabling sitemap generation, check whether the expected sitemap file can be created and served. Verify that its URLs point to publicly accessible pages. If a write error occurs, inspect only the relevant target file or directory permissions; avoid granting blanket write access to the site's document root.

## Plugin help and technical sources

The release also includes plugin-specific help. The Core documents for Calendar, Links, Polls, Spam-X, Static Pages and XMLSitemap are in `public_html/docs/english/`; the reCAPTCHA reference is under `public_html/admin/plugins/recaptcha/docs/english/config.html`.

For the exact options, inspect the plugin version installed on your site and the matching source. The Geeklog 2.2.2 release contains [Calendar](https://github.com/Geeklog-Core/geeklog/tree/v2.2.2/plugins/calendar), [Links](https://github.com/Geeklog-Core/geeklog/tree/v2.2.2/plugins/links), [Polls](https://github.com/Geeklog-Core/geeklog/tree/v2.2.2/plugins/polls), [Spam-X](https://github.com/Geeklog-Core/geeklog/tree/v2.2.2/plugins/spamx), [Static Pages](https://github.com/Geeklog-Core/geeklog/tree/v2.2.2/plugins/staticpages) and [XMLSitemap](https://github.com/Geeklog-Core/geeklog/tree/v2.2.2/plugins/xmlsitemap).
