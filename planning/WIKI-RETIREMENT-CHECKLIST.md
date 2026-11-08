# Historical Wiki preservation and redirect acceptance

**Priority P1. Status: archive and redirect acceptance not completed.**

Tom reported that most of the 400+ discovered Wiki backlinks point to the Wiki root and that a Pair Hosting redirect was being configured. He also reported a missing HTTPS certificate. This note defines checks before retiring the Wiki; it does **not** assert that any redirect is working.

## Preserve before redirecting

- Produce and retain an immutable snapshot of the Wiki files, page text, assets, export metadata, and database or complete public export where licensing and access permit.
- Record archive date, source origin, filenames, checksums, format, location, and who is responsible for maintaining the copy.
- Keep page title, original Wiki URL, last revision timestamp, author/license metadata where possible, and cross-reference any rewritten Markdown equivalent.
- Maintain a review inventory with dispositions: migrated and reviewed, retained in archive only, obsolete, or requires provenance/technical review.
- For key developer references, include the **Caching Template Library** and **Theme Developers Guide** in the mapping.
- Confirm with Dan and Tom that archive access is available to future Core maintainers *before* switching off the old Wiki.

A single MHTML saved page is useful as a review input, but is **not** a complete Wiki archive.

## HTTPS and redirects

Check both `http://wiki.geeklog.net/` and `https://wiki.geeklog.net/`; issue a normal browser request and inspect the redirect status and final target. Do not bypass invalid certificates.

Test at least:

1. Bare hostname and root with both schemes.
2. A representative existing developer page (for example, Caching Template Library).
3. A different historical guide and a nonexistent Wiki path.
4. An old externally linked deep path with query parameters, if one is known.
5. A browser with redirects and cookies disabled for diagnosis, plus a normal browser.

Record the observed HTTP status, `Location` header, TLS certificate validity/expiry, final page content, and any redirect loop. If the redirect deliberately sends every old page to the documentation homepage, document the loss of deep-link context and provide a searchable archive/index where possible. Prefer page-specific redirects only for reviewed, confirmed equivalents.

## Validation record (2026-11-08)

- Tom reported Pair Hosting SSL was not yet installed and a support request was open.
- A follow-up external fetch of both HTTP and HTTPS Wiki root returned **502** from the fetching service. This result is inconclusive and does not establish the origin server's response, TLS certificate state, or intended redirects.
- **Remaining:** a real client/HTTP header check from a network able to reach Pair Hosting, after Tom confirms SSL work is complete.
- **Remaining:** confirmation of durable archive custody and provenance inventory.

## Approval gate

Only retire the original public Wiki after the archive owner, HTTPS availability, redirects, and recovery plan are agreed by Geeklog maintainers. Keep documentation source migration and the hostname redirect as separately reversible changes.
