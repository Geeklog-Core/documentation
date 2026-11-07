# Security and permissions for developers

> **Geeklog 2.2.2 online developer reference — runtime verification pending.** Use it as a code-reading map, not a substitute for the permission, session and CSRF behavior tests required by your application.

## Core security checks

The [Geeklog 2.2.2 security library](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/system/lib-security.php) defines:

```php
SEC_hasRights($features, $operator = 'AND', $uid = 0);
SEC_inGroup($grp_to_verify, $uid = 0);
SEC_createToken($ttl = 1200);
SEC_checkToken();
```

These are signatures present in the tagged source. Their default arguments, return behavior and handling of the current user should be reviewed before changing authorization logic.

## Authorizing administrative actions

Perform authorization checks **on the server**, not only by hiding menu entries. A practical reference is the tagged [user administration handler](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/public_html/admin/user.php), which checks `user.edit` and then applies additional group-assignment and deletion rules.

Use feature rights that reflect the action being performed, and verify that a lower-privileged account cannot modify objects it does not own.

## Protecting write actions against CSRF

Geeklog's administration handlers generate tokens with `SEC_createToken()` and validate submissions with `SEC_checkToken()`. Follow the corresponding pattern for your selected release; do not replace a server-side check with a hidden form field that is never validated.

CSRF defenses are separate from authentication, authorization and output escaping. A valid token alone does not grant the right to perform an operation.

## Inputs, outputs and secrets

- Treat values received from users, external services and stored content as untrusted.
- Validate inputs and use database access APIs appropriate for the installed release.
- Escape output for the destination context (HTML, attribute, URL, JavaScript).
- Avoid revealing stack traces, credentials, password-reset values, access tokens and server paths in public error pages.
- Verify that personally identifiable data is not accidentally exposed by cache entries or debug logging.

## Review checklist

- [x] `SEC_*` API names and displayed signatures checked in Geeklog 2.2.2.
- [x] Token use and permission checks confirmed in 2.2.2 user/group administration handlers.
- [ ] Plugin-specific authorization cases tested with nonadministrator accounts.
- [ ] Interaction with the current release's session and cookie settings audited.
- [ ] Historical Wiki provenance and attribution reviewed.

**Source scope:** Geeklog v2.2.2; verify behavioral assumptions before deploying code to later releases.
