# Webservices and the service API

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

## Request-to-handler investigation checklist

Before implementing a client against the 2.2.2 Webservices interface, trace the entire request rather than assuming that the presence of `PLG_invokeService()` makes an operation publicly callable.

| Layer | What to inspect | What to record |
| --- | --- | --- |
| HTTP entry point | Route, method, content type and requested action | Exact local route and observed status in staging |
| Authentication | Whether/how the entry point authenticates callers | Supported method verified in tagged code, without credentials |
| Authorization | Permission check for each requested resource and action | Allowed and denied operations using disposable accounts |
| Dispatch | How an action reaches `PLG_invokeService()` and the selected handler | Actual dispatcher and callback used |
| Input | Required fields, field validation and decoding | Safe representative requests and expected validation failures |
| Output | Success and error status, serialization and response format | Captured redacted response examples |
| Logging | Whether errors expose private request data | Redaction and retention expectations |

For write operations, verify that a valid authentication credential is not treated as unrestricted permission to publish or change content. For read operations, verify that private or unpublished records cannot be retrieved by unauthorized callers.

## Staging-only interoperability tests

A sensible minimum test set is: (a) a supported read request as an authorized test account, (b) the same request without sufficient privileges, (c) malformed or missing required inputs, (d) an unsupported action, and (e) a permitted write followed by a read-back **only when the target handler is verified to support it**.

Use a disposable site and accounts. Capture HTTP status and response content type, not live session cookies or credentials. Avoid publishing a copy-and-paste request containing guessed endpoint paths or authentication headers; verify the actual routing and accepted operations in the installed release first.

**Compatibility boundary:** Geeklog 2.2.2's inclusion of Atom-related files is historical evidence of code presence, not an assurance of API stability, universal standards compliance, or modern authentication support. A later Geeklog release requires new source and runtime tests.
