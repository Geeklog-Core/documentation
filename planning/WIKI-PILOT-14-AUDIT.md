# Editorial audit — first 14 recovered Wiki pages

Source: contributor-supplied `wiki-review-pilot-14.zip`, exported from the Geeklog Wiki SQL snapshot dated 2024-11-02. The original Wiki text is not committed: do not publish or quote it in bulk without attribution, license, privacy and technical review.

## Topic-by-topic decisions (initial review)

| Wiki title | Disposition | Reason |
| --- | --- | --- |
| `Plugin_API` | **Merge** into `docs/development/plugin-api/README.md` | Useful callback overview; signatures and deprecated hooks require source checks |
| `Plugin_APIG2` | **Do not import as current API** | Explicitly describes a proposed next-generation Geeklog 2 action-manager architecture with references to the 1.3.x branch |
| `Plugin_Autoinstall` | **Merge** into plugin API then a dedicated installation guide | Written for Geeklog 1.6; installation metadata examples must be verified |
| `Functions.inc_-_Listing_of_the_Plugin_Functions` | **Merge** into plugin API | Overlaps Plugin_API; assertion that only uninstallation is mandatory must be checked for current release |
| `AddToConfiguration` | **Technical review** before guide | Discusses 1.7.x database-managed configuration |
| `DatabaseSchema` | **Exclude old SQL as current schema** | Contains explicit `geeklog 1.4.1` schema; generate schema reference from pinned current release |
| `Caching_Template_Library` | **Merge** into themes/templates | Covers compiled templates, search paths and rendering; old performance claims and caches not authoritative |
| `Webservices_API` | **Technical review** | Explicitly framed as Geeklog 1.5 webservices with Atom Publishing Protocol and old clients |
| `Multi-Site_Setup` | **Do not promote as supported** | Article itself says multi-site customization is not officially supported; security and maintenance risks |
| `Integrating_the_Comment_Engine` | **Technical review** | Documents version bands 1.3.7 to 1.4; signatures need current confirmation |
| `Static_Pages_Plugin` | **Merge** into `docs/plugins/static-pages/README.md` | General page-management guidance useful; PHP execution needs strong security warning |
| `Theme_Developers_Guide` | **Merge** into themes/templates | Contains Geeklog 2.0 rendering changes, old themes/scripts, encoding artifacts |
| `Coding_Guidelines` | **Do not make authoritative without project approval** | Historical March 2007 PEAR convention; check today's contribution requirements |
| `Adding_Moderation_Capability` | **Merge** into plugin API and future moderation guide | Historic callback examples must be checked in pinned source |

## Markdown guides now available on the consolidated branch

The original 14-page Wiki pilot informed the Markdown guides for plugin APIs, themes/templates, Static Pages, configuration APIs, webservices, security, and associated administration topics. The consolidated branch also contains installation, configuration and administration guides and 10 supplementary guides, delivered through the same online and embedded build.

**Status is mixed:** selected Geeklog 2.2.2 function signatures and callbacks were checked against tagged source; full API examples, runtime behavior, copyright reuse and attribution have not all passed review. These guides are **not** blanket-approved historical Wiki imports. No bulk Wiki body was committed. The historic 14 article bodies remain in the contributor's review ZIP.

This pilot is **14 of 351** recovered Wiki pages, not an audit of all archived pages. The remaining pages require inventory and selective classification before any claim of full Wiki migration.

## Release gates

1. Validate code references against the pinned Geeklog 2.2.2 source and current active plugins.
2. Confirm compatibility with the `prototype/dual-output-222` build and embedded help anchor contract.
3. Check licenses/attribution and review any code samples before publication.
4. Introduce these pages into a single online navigation and search, and the appropriate embedded HTML output.
5. Consolidate the validated guides and installation/staging checks into **one reviewed upstream PR**. The original upstream installation draft PR #4 was closed without merge on 2026-11-05 after its changes were carried into `prototype/wiki-unified-222`.
6. Do not block an initial complete-to-use Geeklog 2.2.2 documentation delivery on all 351 historic Wiki pages; retain explicit release scope and list unresolved historical topics.
