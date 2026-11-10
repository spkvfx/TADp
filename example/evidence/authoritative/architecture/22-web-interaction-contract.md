# Browser user to web application interaction contract

**Architecture ID:** `ARC-CTR-007`  
**Status:** Accepted  
**Architecture revision:** `2.0.0`  
**Contract owner:** Web component owner and project architecture authority  
**Producer:** Same-origin record web application  
**Consumer:** Local browser user  
**Last reviewed:** 2026-11-10  

## Purpose and scope

This contract defines the v1 browser information architecture, controls,
state transitions, create/edit/search/navigation flows, validation/error
presentation, concurrency behavior, accessibility, client security, and
browser compatibility. The API remains authoritative for data; this contract
owns how browser users invoke and understand it.

The supported entry origin is exactly
`http://127.0.0.1:${RECORDS_HOST_PORT}`, where Docker publishes the embedded
assets and API from `record-api`. The browser is a host user agent, not an
application service. No host Node/web server, file URL, separate web container,
proxy, CDN, or alternate origin is part of this contract.

## Entry routes and document structure

| Route | Meaning | Data behavior |
|---|---|---|
| `/app/` | Stable application entry and current in-memory context | After assets load, requests a browse page of one; when nonempty, retrieves/displays its first record and ETag, otherwise enters `empty`; no hidden writes |
| `/app/records/{id}` | Optional deep link to one canonical record ID | Performs GET after app load; invalid/absent ID is presented distinctly |

Routes are relative to the exact supported origin. Asset URLs are generated
from the API image's immutable manifest and remain same-origin; an entry
document and asset manifest from different builds is a fatal deployment error,
not a recoverable client update.

Search query text, name, value, ETag, cursor, and full search context must not
appear in URL, fragment, document title, referrer, or browser history. A
canonical record ID may appear in a deep link because it is an opaque public
identifier. Navigating browser Back/Forward may restore an ID route but reruns
an authoritative GET; it does not restore cached record content as current.

The entry document contains, in logical order:

1. one skip link to the main region;
2. application heading and compact service-status region;
3. primary actions: Create and Search;
4. record workspace with ID, Name, Value, Save/Cancel while editing, and
   Previous/Next navigation;
5. search panel/results when active;
6. one polite status live region and one assertive error live region; and
7. nonessential version/help text.

There is one visible primary `h1`. Dialogs are used only when focus trapping,
labelling, Escape behavior, and return focus are implemented correctly;
ordinary create/edit/search can be inline panels and must not require modal UI.

## Record presentation

| Element | View mode | Edit/create mode |
|---|---|---|
| ID | Read-only text with full canonical UUID and Copy ID action | Existing ID remains read-only; create says "Assigned when saved" and has no input |
| Name | Text preserving canonical content | Required single-line labelled input, max-length guidance/counter |
| Value | Pre-wrapped text preserving LF/spacing | Labelled multiline textarea, length guidance/counter |
| ETag/revision | Not displayed as a user-editable field | Retained only in memory for Save; optional conflict language may say "record changed" but not expose counter as domain data |

Record text is inserted as text, never HTML. Long unbroken content wraps
without horizontal page overflow. The value view preserves LF and whitespace
visually using safe CSS but remains selectable/copyable.

## Primary flows

### Create

1. Create moves to `creating`, retaining the prior stable context in memory.
2. Name starts empty. Value starts empty (valid only after Name is valid).
3. ID is non-input text. The user can Create record or Cancel.
4. Client validation follows `ARC-CTR-001`; server validation is still handled.
5. Submit disables all mutating actions, marks busy, sends one POST, and moves
   to `loading`.
6. On `201`, render the returned canonical record/ETag, announce success, set
   the deep-link ID using History API without record values, and enter `viewing`.
7. On determinate validation/failure, retain draft and focus the error summary
   or first invalid field. On indeterminate transport loss, retain draft,
   explain uncertainty, and offer Refetch/Search - not automatic resubmit.
8. Cancel discards the draft after confirmation only when nonempty/changed,
   then restores the prior stable state.

### Edit and save

1. Edit copies canonical name/value into a draft and retains ID/ETag.
2. ID has no input, hidden mutable field, or contenteditable representation.
3. Save validates and sends exactly one PATCH with retained `If-Match`.
4. On success, replace record/ETag with server response and announce Saved.
5. A normalized no-op succeeds without a false "changed revision" claim.
6. Cancel discards draft and restores the unchanged canonical view; navigating
   away from a dirty draft requires explicit discard confirmation.
7. On `412`, enter `conflict`, preserve draft in memory, and offer:
   - **Reload latest**, which discards the draft only after confirmation and
     GETs the current record; and
   - **Copy draft**, which copies or exposes the user's text for manual
     reconciliation without making a write.
8. There is no Force save, automatic merge, hidden retry, or last-write-wins.

### Search and browse

1. Search opens labelled Field, Match mode, and Query controls. Field options
   are ID, Name, Value; mode options are Exact, Starts with, Ends with,
   Contains, Regular expression.
2. Query is single-line. Mode help changes to explain case-sensitive literal
   matching or RE2/unanchored regex and links to concise supported-syntax help.
3. The empty query is accepted only for exact Value; all other invalid
   combinations are blocked locally and remain server-validated.
4. Submitting creates one search context, clears prior cursor history/results,
   and calls one page request with default 25.
5. Results appear in API order. Each item exposes Select/View; the UI does not
   sort or filter membership. Names may be primary labels, but full ID remains
   available and duplicate names remain distinguishable.
6. No matches show an explicit successful empty state, not an error.
7. Next page follows only the returned cursor. Back page uses only in-memory
   prior cursor/context history and reruns that page; reload restarts search.
8. Selecting a result retrieves the current record/ETag before editing and
   retains the search context/ceiling for Previous/Next.
9. Invalid regex, cursor, budget, or context mismatch remains distinguishable.
   Cursor/context mismatch offers Restart search; it never guesses.

### Previous and next

- From a record outside search, Previous/Next uses browse context and the
  retained or newly established ceiling.
- From a selected search result, it sends the exact normalized user context
  parameters and retained ceiling through the adapter.
- During navigation, controls are disabled and current content remains visibly
  stale/loading rather than blanking without explanation.
- A returned record replaces record/ETag and updates deep-link ID. `start` or
  `end` disables the corresponding direction and announces the boundary.
- Navigation never wraps, skips based on client state, or discards dirty edits
  without explicit confirmation.
- Context mismatch restarts/refetches explicitly; it is not shown as a normal
  collection boundary.

## Validation presentation

- Client validation runs on submit and may run on blur; it must not announce
  errors on every keystroke.
- An error summary at the start of the active form contains links to each
  invalid control. Each control also has a programmatically associated message.
- Limits describe normalized accepted input in user language. Counters are
  advisory; the API's normalized code-point/byte checks are authoritative.
- Server `errors.path` maps only to known controls. Unknown paths appear in the
  summary as a safe form-level error rather than being inserted into selectors
  or HTML.
- Error text never echoes full record values or regex/query text. When a safe
  offset exists, the UI may show the offset and focus the query control.
- After successful submission, obsolete validation messages are removed from
  the accessibility tree.

## Asynchrony and race rules

- Each UI intent has a monotonically increasing in-memory request token.
  Responses update state only when their token remains current for that view.
- AbortController may cancel obsolete GETs. Cancellation of POST/PATCH after
  dispatch is not treated as proof of rollback; the UI uses indeterminate
  handling.
- Mutating controls remain disabled for the complete in-flight write. Keyboard
  repeat/double-click cannot issue a second write.
- Search changes cancel/obsolete prior search GETs; late responses cannot
  replace current results.
- Page unload while a write is pending must not use `sendBeacon`, background
  replay, or automatic retry. A standard unsaved/pending warning may be used
  where the browser permits.

## Error/state mapping

| API/transport outcome | Required UI result | Draft/current-record treatment |
|---|---|---|
| Validation/invalid search/regex | Form/search error summary | Preserve draft/context input |
| Record not found | Explicit Not found state with Search/Create actions | Clear stale current record after acknowledgement; preserve unrelated search context |
| Revision conflict | Conflict state and reconciliation actions | Preserve edit draft and prior ID |
| Capacity exceeded | Create failure explaining no new record was saved | Preserve create draft |
| Boundary | Start/end status, direction disabled | Preserve current record/context |
| Context/cursor mismatch | Context changed; Restart search action | Preserve current record where still valid; discard cursor only after user action |
| Store/search unavailable | Unavailable state with request ID and explicit Retry | Preserve safe draft and last stable data labelled stale |
| Indeterminate write | Unknown outcome warning; Refetch/Search actions | Preserve draft; never auto-submit |
| Protocol/internal error | Fatal or recoverable generic error with request ID | Never render partial decoded data |

## Accessibility requirements

The product must meet applicable WCAG 2.2 Level A and AA success criteria and
these concrete obligations:

- native semantic controls/labels are used before ARIA; every input/action has
  a persistent accessible name;
- all actions, results, paging, dialogs, and conflict recovery are keyboard
  operable with visible focus and no keyboard trap;
- focus moves to the main heading on route load, error summary after failed
  submit, record heading after successful navigation/create, and triggering
  control after panel/dialog cancellation;
- status updates use a polite live region; blocking errors use a concise
  assertive region without repeating entire content;
- reading/DOM/focus order remains logical at 320 CSS px width and 200% zoom;
- text/background and focus indicators meet AA contrast, with status never
  communicated by color alone;
- animations honor `prefers-reduced-motion`; no essential timed interaction,
  flashing, drag-only, hover-only, or pointer-precision action exists;
- control targets meet WCAG 2.2 Target Size (Minimum) where applicable;
- error prevention/confirmation protects discard of unsaved changes;
- automated accessibility output is supplemented by keyboard, zoom,
  high-contrast where available, and screen-reader review.

## Browser security and storage

The server supplies at least:

```text
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; font-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'
Referrer-Policy: no-referrer
X-Content-Type-Options: nosniff
Cross-Origin-Opener-Policy: same-origin
Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=(), usb=()
```

Scripts/styles are external content-addressed assets; no `unsafe-inline` or
`unsafe-eval`. There are no third-party scripts/fonts/images, cookies, service
workers, Cache API, localStorage, sessionStorage, IndexedDB, telemetry, or
cross-origin fetch. Record/data API responses are `no-store`. Static hashed
assets may be long-cached; the entry HTML is revalidated/no-cache and references
one coherent manifest.

## Contract rules

| Concern | Rule | Owner |
|---|---|---|
| Authentication/authorization | None; same-origin loopback trust only | Architecture/API |
| Container delivery | Compiled bundle embedded in the API image; exact IPv4 loopback Docker publication; no host web toolchain/service | Platform/web |
| Validation/idempotency | Mirror for feedback; API authoritative; one write per intent | Web state controller |
| Ordering/timeouts/retries | Preserve API order; user-explicit retry; no write retry | Web adapter |
| Versioning | UI behavior follows web semantic release and declares API major | Web release owner |
| Observability | No remote telemetry; console production output contains no record/query data | Web |

## Compatibility and verification

| Verification | Scenario | Evidence location |
|---|---|---|
| Component/state tests | Every tabled state/transition, late response, double action, conflict, indeterminate outcome | [`ARC-CTR-009`](24-conformance-contract.md) |
| Browser end-to-end | Create/edit/cancel/search/page/neighbor/error on supported matrix | Future web evidence |
| Accessibility | Automated plus manual keyboard/zoom/high-contrast/screen-reader audit | Future accessibility evidence |
| Security/storage | CSP/header checks, XSS vectors, Origin/Host tests, browser storage/network inspection | Future web/API evidence |
| Cross-surface parity | IDs/order/values/outcomes equal direct API/CLI vector results | Future end-to-end evidence |
| Containerized bundle | Pinned build-stage compilation, bundle hash/provenance, runtime absence of Node, and clean-host Compose serving | Future build evidence |
| Origin confinement | Alternate Host/Origin/interface/file URL/proxy requests fail; only exact loopback entry works | Future operations/security evidence |

## Related records

- System boundary: [`ARC-BND-006`](21-web-application-boundary.md)
- Search contract: [`ARC-CTR-003`](14-search-navigation-contract.md)
- Decisions: [`ADR-001`](04-ADR-001-api-exclusive-persistence.md), [`ADR-004`](07-ADR-004-container-only-deployment-trust-model.md), [`ADR-007`](10-ADR-007-product-and-delivery-decomposition.md)
- Governing evidence: [`AUTH-EX-001`](01-accepted-architecture-baseline.md)
- Superseded native deployment baseline: [`ARC-REV-001`](revisions/1.0.0/00-superseded-native-runtime-deployment-baseline.md)

## Revision record

| Date | Change | Authority |
|---|---|---|
| 2026-11-10 | Defined browser routes, flows, accessibility, and client-security behavior | User-authorized best-judgment architecture completion |
| 2026-11-10 | Fixed the browser entry to the Docker-published loopback origin and the bundle to the API image build | User's explicit full-Dockerization/no-host-services instruction |

