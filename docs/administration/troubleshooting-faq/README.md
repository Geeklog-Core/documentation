# Troubleshooting and FAQ

> **Geeklog 2.2.2 administrator FAQ.** This page helps choose a safe first diagnostic step. It does not replace hosting-specific log investigation or reproduce every historical FAQ answer.

## Why does the site show HTTP 500 or a blank page?

Record the first relevant PHP or web-server error and the exact action that triggered it. Verify the installed PHP version and extensions. Do not publish a stack trace or change multiple permissions at once. Follow [Troubleshooting](../troubleshooting/index.html).

## Why do I get HTTP 403 in administration?

Review the effective user/group feature rights, any CSRF token checks and hosting security logs. A web-server security rule and an application permission denial are different causes. Reproduce with a disposable test account, not by disabling security globally.

## Why is the administrator URL incorrect?

Confirm that `site_admin_url` is a **web URL**, not a filesystem path, and review the configured canonical site URL. Investigate safely before touching serialized configuration or rerunning the installer.

## Why is my article or comment not visible?

Check publication state, topic/content visibility, moderation queue and spam filtering before submitting again or changing permissions. See [Articles and topics](../../user-guide/articles-and-topics/index.html) and [Comments and moderation](../../user-guide/comments-and-moderation/index.html).

## Is an SQL backup enough for recovery?

No. A complete recovery normally requires database and relevant files, private configuration, uploaded media and plugin/theme customizations. Restore into an isolated environment and verify the application. See [Backup and recovery](../backup-and-recovery/index.html).

## Why do plugin pages break after an update?

Check the precise plugin and Core versions, the first error, and whether the change affected database schema or themes. Preserve the state before rerunning an upgrade. Use [Plugin installation and management](../../plugins/plugin-installation-management/index.html).

## How can I request support?

Provide release versions, sanitized route and first error, time of the incident, reproduction steps and attempted checks. Exclude passwords, tokens, private records and public debug endpoints.

## Editorial backlog

The historic Geeklog FAQ and Wiki may contain additional useful questions. Their answers must be rechecked against a tagged release and current hosting practices before adoption. This page intentionally contains new, scope-limited guidance rather than copied historical troubleshooting prescriptions.
