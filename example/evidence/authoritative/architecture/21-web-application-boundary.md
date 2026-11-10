# Record web application system boundary

**Architecture ID:** `ARC-BND-006`  
**Status:** Accepted  
**Architecture revision:** `2.0.0`  
**Owner:** Web component owner under a future accepted initiative  
**Last reviewed:** 2026-11-10  
**Related records:** [`ADR-001`](04-ADR-001-api-exclusive-persistence.md), [`ADR-004`](07-ADR-004-container-only-deployment-trust-model.md), [`ARC-CTR-003`](14-search-navigation-contract.md), [`ARC-CTR-007`](22-web-interaction-contract.md), [`ARC-CTR-008`](23-operations-security-contract.md)  

## Boundary statement

The web application boundary begins at the same-origin entry document embedded
in and served by the `record-api` image and includes content-addressed
HTML/CSS/JavaScript assets,
accessible record/search forms, a small typed browser API adapter, in-memory
view/edit/search state, and deterministic rendering of API outcomes. It ends
at browser same-origin requests to
`http://127.0.0.1:${RECORDS_HOST_PORT}` published by Docker. Its TypeScript is
compiled in the pinned `web-build` stage and copied into the API runtime image;
Node/npm/compiler and a separate web server exist on neither host nor runtime.
It does not own persistence,
record/search rules, authentication, service-worker/offline state, Python SDK
use, direct SQLite access, server-side sessions, third-party scripts, or remote
deployment.

## Responsibilities

| Responsibility | Boundary owner | Explicitly outside this boundary |
|---|---|---|
| Present ID as read-only and name/value as explicitly editable | Web view/form layer | Changing domain validation or making ID writable through hidden controls |
| Provide Create, Save, Cancel, Search, Next, and Previous interactions | Web state controller | Implicit autosave or wraparound navigation |
| Mirror safe validation for immediate feedback | Browser validation adapter | Final acceptance; API remains authoritative |
| Call only same-origin `/api/v1` operations | Browser API adapter | Python SDK, cross-origin endpoints, SQLite, or local file APIs |
| Preserve the latest ETag with the displayed record | Browser state controller | Force overwrite or automatic conflict resolution |
| Present loading, empty, boundary, validation, conflict, unavailable, and unexpected states | Accessible status/error components | Suppressing errors or treating an empty result as a transport failure |
| Meet keyboard, focus, semantic, contrast, zoom, and announcement requirements | Web product | Browser/assistive-technology defects outside supported matrix |
| Avoid durable client storage of records | Browser state controller | Offline cache, localStorage, IndexedDB, or service-worker record copies |

## Inputs and outputs

| Direction | Counterparty | Interface or artifact | Validated by | Compatibility rule |
|---|---|---|---|---|
| Inbound | Browser user | Keyboard/pointer input and text | HTML constraints and TypeScript form validator | Browser validation mirrors but never widens API rules |
| Inbound | API service | JSON, ETag, cursor, request ID, and problem responses | Typed browser decoder | Malformed success becomes a visible protocol error, not partial UI |
| Inbound | Static asset route | Entry HTML and content-addressed assets | Subresource/content-type/CSP checks | Entry document references one coherent asset build |
| Outbound | API service | Same-origin JSON requests | Browser adapter and API validation | Only accepted `/api/v1` operations and fields |
| Outbound | Browser user | Semantic document, focus movement, status announcements, rendered record/result data | View-state renderer and accessibility checks | Values render as text, never untrusted HTML |
| Outbound | Browser history | Optional non-sensitive app route/state identifier | Router allowlist | Record values and raw search queries must not be placed in URL/history |

## Client state model

Exactly one primary view state is active:

| State | Required content/actions | Permitted transition |
|---|---|---|
| `empty` | No current record; Create and Search available | `creating`, `searching`, `loading` |
| `loading` | Progress indication; mutating controls disabled | Prior stable state on failure, or `viewing`/`search-results` on success |
| `viewing` | Read-only ID, name, value; Edit/Create/Search/Next/Previous | `editing`, `creating`, `searching`, `loading` |
| `editing` | Draft name/value; original ID; Save and Cancel | `loading` on Save, `viewing` on Cancel |
| `creating` | Blank accepted defaults; Create and Cancel | `loading` on Create, prior stable state on Cancel |
| `searching` | Field/mode/query form and validation | `loading` on submit, prior stable state on Cancel |
| `search-results` | Ordered page, active context, empty/page status, selection | `loading` for paging/selection/neighbor, `searching` to revise |
| `conflict` | Unsaved draft, server-change notice, Reload and Copy Draft actions | `loading` on Reload, `editing` after explicit user reconciliation |
| `unavailable` | Service-unavailable status and explicit Retry | `loading` on Retry |
| `fatal` | Protocol/unexpected error, request ID when available, Reload action | Full reload only |

Transient validation messages do not create a separate primary state. The UI
must retain the last stable record/result context behind recoverable errors
without presenting it as freshly confirmed.

## State and authority

| State or decision | System of record | Write authority | Recovery or reconciliation rule |
|---|---|---|---|
| Live records | API/SQLite | Web only through API commands | Refetch after errors or conflicts |
| Current displayed record and ETag | Browser memory | Successful API decoder | Replace only with a newer successful response |
| Edit/create draft | Browser memory | User | Cancel discards; success replaces; conflict preserves until explicit action |
| Search context, results, cursor history | Browser memory | Successful API decoder plus user navigation | Discard on reload; rerun on invalid cursor |
| Static asset build identity | API static manifest | Web build/release process | Atomic coherent deployment; reload after mismatch |
| Delivered bundle identity | Content hashes linked to API image digest, source commit, and web semantic version | Container build/release process | Hash/provenance mismatch blocks release; assets and API deploy atomically |

## Invariants and failure boundaries

- The app uses no service worker, localStorage, sessionStorage, IndexedDB,
  cookies, analytics, third-party fonts/scripts, or cross-origin network calls.
- DOM insertion of record values, errors, and search text uses text nodes or
  equivalent escaping; no value is interpreted as HTML.
- Save/Create controls are disabled during their in-flight request. A double
  activation cannot issue two accepted writes from one UI action.
- Navigation never discards an unsaved edit without an explicit confirmation.
- A `412` conflict preserves the user's draft and offers no force-overwrite
  action. Reload/reconcile is explicit.
- Boundary responses disable the unavailable direction and announce first/last
  state; navigation never wraps.
- Search results and navigation display only API membership/order. Client-side
  filtering or resorting that changes contract meaning is prohibited.
- Network failure cannot produce a success notification. An indeterminate
  create/update tells the user to refetch before retrying.
- All essential behavior is keyboard operable at 200% zoom with visible focus,
  programmatic labels, logical headings, non-color status cues, and an ARIA
  live region for asynchronous results.
- The only supported asset origin is the API's Docker-published IPv4 loopback
  origin. There is no host `npm` development server, file-URL application,
  separate web container, CDN, proxy, or cross-origin API configuration.
- The runtime image contains compiled/minified assets and manifest/source-map
  policy outputs only; it contains no Node runtime, package manager, source
  dependency tree, or build cache. Production source maps, if emitted, must not
  reveal secrets or host paths and require an explicit release decision.

## Supported browser boundary

At each web release, conformance is required on the latest two stable desktop
major versions of Chrome, Edge, and Firefox and the latest stable desktop
Safari version available to the test owner. JavaScript is required. Mobile
browsers and no-JavaScript operation are outside v1 acceptance, although the
layout should remain usable at a 320 CSS-pixel viewport.

## Verification and change control

| Claim | Verification | Evidence location |
|---|---|---|
| State transitions preserve drafts and never claim false success | Component and browser end-to-end fault tests | Future web completion evidence |
| Browser never bypasses API or persists record data | Network/storage inspection and architecture test | Required by `ARC-CTR-009` |
| UI conforms to WCAG 2.2 AA applicable success criteria | Automated checks plus keyboard/screen-reader/manual review | Future accessibility evidence |
| Supported browsers render and execute the same contract behavior | Browser matrix | Future web release evidence |
| Bundle is built/tested without a host web toolchain and is coherent with API image | Build provenance, asset hash/manifest, image scan, and clean-host Compose test | Future web release evidence |
| Only the exact Docker loopback origin serves assets/API | Host/network tests, CSP/Origin/Host negatives, and no-separate-server inspection | Future operations evidence |

Changes require web owner review and project architecture authority. UI state,
storage, API, accessibility, browser-support, or security changes require
synchronized contract, operations, compatibility, and conformance updates.

## Revision record

| Date | Change | Authority |
|---|---|---|
| 2026-11-10 | Defined same-origin browser application, state, and accessibility boundary | User-authorized best-judgment architecture completion |
| 2026-11-10 | Bound web build to a container stage and embedded delivery to the loopback-published API image | User's explicit full-Dockerization/no-host-services instruction |

