# Webservices and the service API

> **Geeklog 2.2.2 source-checked developer guide.** The recovered Wiki article `Webservices_API` documents Geeklog 1.5 and the Atom Publishing Protocol. This replacement is based on code paths present in the Geeklog 2.2.2 release, not on an assumption that all historical endpoints or older clients still work.

## Core service dispatch

Geeklog 2.2.2 includes `PLG_invokeService()` in [`system/lib-plugins.php`](https://github.com/Geeklog-Core/geeklog/blob/v2.2.2/system/lib-plugins.php):

```php
PLG_invokeService($type, $action, $args, &$output, &$svc_msg);
```

The source accepts a content type, an action, an arguments array, and two result parameters by reference. It initializes the output and message arrays and dispatches through a service handler when one exists.

**Do not expose a custom handler without verifying the current permission checks and supported arguments.** Presence of a service dispatcher does not by itself prove that a public endpoint permits any particular operation.

## HTTP entry points

The Geeklog 2.2.2 distribution includes these files:

- `public_html/webservices/atom/index.php`
- `system/lib-webservices.php`

They are relevant starting points when inspecting Atom-related functionality. The historical Wiki's client examples and URLs must be checked against your actual installation, web server configuration and enabled plugins.

## Implementing or troubleshooting an integration

1. Inspect the webservices entry point and how it authenticates a request.
2. Trace the action from the HTTP layer to `PLG_invokeService()` and its service handler.
3. Check the supported input fields, response codes and output serialization.
4. Validate permissions for every read and write operation using a test account.
5. Test allowed and forbidden requests in a disposable installation.
6. Avoid exposing user passwords or access tokens in logs, documentation or support tickets.

## Historical compatibility

The [Atom Publishing Protocol, RFC 5023](https://www.rfc-editor.org/rfc/rfc5023) is the standard discussed by the original Wiki page. This does **not** guarantee that every RFC feature is implemented or enabled by Geeklog 2.2.2. Check each desired operation in the source and in a staging site.

The Wiki also describes older example clients and interfaces. Their support in 2.2.2 has **not** been validated and is intentionally not presented as a modern setup instruction.

## Verification status

- [x] Core function signature checked in the Geeklog 2.2.2 distribution.
- [x] Core service and Atom entry-point files confirmed in the distribution.
- [ ] Supported methods, authentication and permission outcomes tested in a live 2.2.2 installation.
- [ ] Exact public routes and response formats documented from integration tests.
- [ ] Reuse licensing and contributor attribution reviewed.

**Provenance:** recovered Wiki `Webservices_API` (2024 backup); replaced with a version-scoped, code-referenced guide.
