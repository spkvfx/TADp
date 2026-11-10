# Accessible same-origin browser bundle

**Realization ID:** `RZN-001-P4-WEB-N01`  
**Suite:** [`RZN-001-P4-WEB-SUITE@v4.0`](00-RZN-001-P4-WEB-suite-index.md)  
**Suite version:** `v4.0`  
**Status:** Recorded; invariant-bounded proposal input  
**Recorded by:** Codex on behalf of the User  
**Recorded date:** 2026-11-10  
**Source:** User request in the current Codex conversation and [`RZN-001`](../v0/RZN-001-example-record-application.md)  
**Historical product lineage:** `RZN-001-P4-WEB`  
**Accepted delivery-unit alignment:** `D6 Web application bundle`  
**Related initiative or proposal:** None created  

> **Evidence standing:** This note records detailed realization input for one
> possible D6 outcome. It is not an initiative, UI specification, implemented
> bundle, accessibility result, browser test, security assessment, release,
> conformance result, or completion claim. The cited authoritative records own
> every accepted browser and delivery meaning.

## Realization

There is a bounded opportunity to deliver one independently versioned,
content-hashed browser bundle that makes the accepted record capabilities
usable through an accessible graphical interface at the exact Docker-published
loopback origin. The bundle would be compiled in the pinned `web-build` stage,
embedded in a compatible D3 API image, served with a coherent manifest and
restrictive headers, and call only the same-origin `/api/v1` contract.

The candidate web product would own browser interaction, in-memory view and
draft state, safe rendering, accessibility, race handling, and bundle identity.
It would not own persistence, domain/search semantics, API behavior, Python SDK
behavior, authentication, remote deployment, a separate server, or durable
client storage.

## Narrow outcome and beneficiary

| Dimension | Candidate record |
|---|---|
| Outcome | One D6 browser bundle that realizes the accepted routes, state transitions, flows, accessibility, client security, embedded delivery, compatibility, and evidence boundary |
| Primary beneficiaries | Local browser users, keyboard and assistive-technology users, D3 static-hosting owners, operators, release/security reviewers, and cross-surface conformance owners |
| Authority boundary | Browser presentation and interaction, typed same-origin API adaptation, in-memory state, safe client rendering, accessibility behavior, and bundle build/release identity only |
| Output class | Container-built HTML/CSS/JavaScript assets, static manifest and hash/provenance records, browser-state implementation, accessibility/security evidence, and D6 release metadata |
| Independent review claim | The exact bundle embedded in the exact compatible API image passes the D6 web, browser/accessibility, security/storage, container, operations, and applicable end-to-end gates |
| Explicit non-claim | No API or database completion, alternate server/origin, host web toolchain, Python SDK use, durable browser record state, remote/multi-user use, regulated use, or general compliance certification |

## Version identity is not product acceptance

`v4.0` identifies this realization suite and one intended future-initiative
boundary. It does not silently select a web semantic version, replace the
accepted `v1` browser interaction contract, or prove compatibility with an API
image. Future governed records must identify the actual bundle semantic
version and hash, source commit, asset manifest, compatible API/image digest,
Compose/render identity, architecture revision, browser matrix, and security
suite revisions.

The fact that D6 assets are copied into a D3 image does not merge the two
completion claims. D3 may prove static hosting without proving D6 behavior;
D6 may prove a bundle only against an exact compatible D3 artifact.

## Context and invariant evidence

| Question | Record |
|---|---|
| What was requested historically? | Product 4 in `RZN-001` requested a web interface over the same record capabilities as the CLI. |
| What is now accepted? | Architecture `2.0.1` fixes the loopback origin, embedded delivery, routes, document structure, state model, create/edit/search/navigation flows, race/error behavior, accessibility, storage exclusions, browser matrix, headers, and D6 gate. |
| What is current product status? | `ARC-CTR-009` defines required vectors and records no supplied D6 implementation, accessibility audit, or passing conformance evidence. |
| What remains proposal-level? | Exact source and product paths, UI styling within the interaction/accessibility invariants, framework or no-framework choice within the build boundary, dependency locks, semantic version, owners, evidence environments, and release disposition. |
| Who is affected? | Local users, users of supported assistive technology, D2/D3 owners, D5 parity reviewers, security/accessibility reviewers, and release operators. |
| Which data may be used? | Only non-production purpose-created synthetic data or externally documented de-identified data that also satisfies the NIST restrictions; actual or possible ePHI and higher-control data remain prohibited. |

## Binding source inventory

| Source | Exact relevance |
|---|---|
| [Codex invariant suite](../../../authoritative/LLM/00_Codex_Invariant_Suite_Index.md) | Governs authority, source identity, narrow scope, explicit decisions, truthful status, and evidence claims. |
| [`ARC-SUITE-001@2.0.1`](../../../authoritative/architecture/00-architecture-suite-index.md) | Owns the active technical architecture and reading order. |
| [`AUTH-EX-001`](../../../authoritative/architecture/01-accepted-architecture-baseline.md) | Owns shared capabilities, one API path, local trust, Compose-only execution, additive security, and permitted-use claims. |
| [`ADR-001`](../../../authoritative/architecture/04-ADR-001-api-exclusive-persistence.md) | Requires all browser record behavior to traverse the API and forbids direct/offline persistence. |
| [`ADR-004`](../../../authoritative/architecture/07-ADR-004-container-only-deployment-trust-model.md) | Owns exact loopback ingress, private service topology, and unsupported remote/proxy paths. |
| [`ADR-005`](../../../authoritative/architecture/08-ADR-005-containerized-technology-stack.md) | Owns containerized TypeScript build, embedded assets, immutable artifact flow, and no-host-toolchain rule. |
| [`ADR-006`](../../../authoritative/architecture/09-ADR-006-contract-versioning-and-feedback.md) | Governs compatibility feedback and successor revisions rather than UI-led contract drift. |
| [`ADR-007`](../../../authoritative/architecture/10-ADR-007-product-and-delivery-decomposition.md) | Owns the D6 boundary, D1-D3 dependencies, and delivery after D5. |
| [`ARC-CTR-001`](../../../authoritative/architecture/11-record-domain-contract.md) | Owns record validation and public shape that browser feedback may mirror but not widen. |
| [`ARC-CTR-003`](../../../authoritative/architecture/14-search-navigation-contract.md) | Owns search predicates, ordering, cursors, ceilings, neighbors, and boundaries displayed by the web product. |
| [`ARC-BND-006`](../../../authoritative/architecture/21-web-application-boundary.md) | Owns bundle, adapter, in-memory state, supported-browser, storage, accessibility, and origin boundaries. |
| [`ARC-CTR-007`](../../../authoritative/architecture/22-web-interaction-contract.md) | Owns routes, controls, flows, races, errors, accessibility, browser security, and compatibility. |
| [`ARC-CTR-008`](../../../authoritative/architecture/23-operations-security-contract.md) | Owns API/static headers, Host/Origin behavior, health, logging, runtime content, and release controls. |
| [`ARC-CTR-009`](../../../authoritative/architecture/24-conformance-contract.md) | Owns `WEB-001` through `WEB-013`, applicable cross-vector groups, the D6 gate, and evidence fields. |
| [`SEC-NIST-SUITE-001@1.0.1`](../../../authoritative/security/NIST/00-nist-security-policy-suite-index.md) | Primary future-development security and assurance invariant for the browser product. |
| [`SEC-HIPAA-SUITE-001@1.0.1`](../../../authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md) | Primary data/use, safeguard, inherited-control, evidence, and successor-gate invariant. |

The parent realization preserves product lineage only. It cannot override the
accepted browser contract or either primary security suite.

## Exact product boundary

The D6 candidate includes:

- a same-origin entry document, content-addressed first-party CSS/JavaScript
  assets, static manifest, and product version/hash identity;
- accessible record, create/edit, search/result, navigation, status, conflict,
  unavailable, and fatal presentation components;
- a small typed browser adapter limited to accepted same-origin `/api/v1`
  requests and strict response/problem decoding;
- in-memory current-record/ETag, draft, search context, cursor history, request
  token, and prior-stable-state handling;
- a pinned container-only build whose exact output is copied into the API
  runtime image without runtime Node/npm/compiler or remote dependency; and
- component, supported-browser, accessibility, storage/network, security,
  bundle-provenance, and cross-surface evidence for the exact released assets.

The D6 candidate excludes:

- domain, query, API, SQLite, migration, health, and operator semantics from
  its ownership or completion claim;
- Python SDK use, direct SQLite/file APIs, separate web server/container, host
  Node service, development server, file-URL app, proxy, CDN, alternate origin,
  cross-origin API, or remote-use path;
- authentication, server sessions, cookies, service worker, offline mode,
  local/session storage, IndexedDB, Cache API record copies, telemetry, or
  third-party scripts/fonts/images; and
- delete, bulk operations, record import/export, history, force overwrite,
  automatic merge, hidden write retry, autosave, or client-side resorting that
  changes API membership/order.

## Container-built and embedded delivery

The TypeScript/web source is compiled only in the pinned `web-build` stage.
The output is hashed, tested, recorded in one coherent manifest, and copied
into the compatible API runtime image. The runtime contains compiled/minified
assets and allowed manifest/source-map-policy outputs only; it contains no Node
runtime, package manager, source dependency tree, build cache, or mutable
install step.

Entry HTML and static manifest from different builds are a fatal deployment
error. Static hashed assets may be long-cached; entry HTML is revalidated or
not cached and references exactly one coherent asset build. A future explicit
release decision is required for production source maps, and any permitted map
must disclose neither secrets nor host paths.

The supported origin is exactly:

```text
http://127.0.0.1:${RECORDS_HOST_PORT}
```

Docker publishes that IPv4-loopback origin from `record-api`. No wildcard,
IPv6, hostname, LAN, public interface, host gateway, file URL, proxy, tunnel,
CDN, or random alternate port becomes supported through this note.

## Entry routes and document structure

| Route | Candidate behavior inherited from `ARC-CTR-007` |
|---|---|
| `/app/` | Loads one coherent asset build, browses one record, then retrieves/displays the first record and ETag; enters `empty` if none; performs no hidden write |
| `/app/records/ID` | `ID` denotes the canonical public path value; the route performs an authoritative GET and keeps invalid and absent IDs distinct |

Only a canonical record ID may appear in a deep link. Name, value, ETag,
cursor, search query, and complete search context must not appear in the URL,
fragment, document title, referrer, or history. Back/Forward may restore an ID
route but reruns GET; cached record content is not restored as current truth.

The logical document order contains a skip link; one application `h1` and
compact service status; Create and Search actions; the record workspace with
ID/Name/Value and edit/navigation controls; conditional search panel/results;
one polite status region and one assertive error region; then nonessential
version/help content. Ordinary forms need no modal. Any dialog must implement
correct labelling, focus trap, Escape behavior, and return focus.

## Candidate state model

Exactly one primary state is active:

| State | Required content and actions | Controlled transition |
|---|---|---|
| `empty` | No current record; Create and Search available | `creating`, `searching`, or `loading` |
| `loading` | Progress is exposed; mutating controls disabled | Prior stable state on failure; `viewing` or `search-results` on success |
| `viewing` | Read-only ID, name, value; Edit/Create/Search/Previous/Next | `editing`, `creating`, `searching`, or `loading` |
| `editing` | Draft name/value, original read-only ID, Save and Cancel | `loading` on Save; `viewing` on Cancel |
| `creating` | Blank draft, non-input future ID text, Create and Cancel | `loading` on Create; prior stable state on Cancel |
| `searching` | Field/mode/query controls and validation | `loading` on submit; prior stable state on Cancel |
| `search-results` | Ordered page, active context/ceiling, empty/page status, selection | `loading` for page/selection/neighbor; `searching` to revise |
| `conflict` | Unsaved draft, server-change notice, Reload latest and Copy draft | `loading` on Reload; `editing` after explicit reconciliation |
| `unavailable` | Service-unavailable status, request ID when safe, explicit Retry | `loading` on Retry |
| `fatal` | Protocol/unexpected failure and Reload action | Full reload only |

Validation messages are transient, not a separate primary state. Recoverable
errors may retain the last stable context behind the error, but must label it
as stale rather than freshly confirmed.

## Record presentation and mutation flows

ID is full, canonical, read-only text with a Copy ID action; it is never an
input, hidden mutable field, or contenteditable value. Name is canonical text
in view mode and a labelled required single-line input in create/edit mode.
Value is safely rendered as selectable pre-wrapped text and edited through a
labelled multiline textarea. ETag/revision stays in memory and is never exposed
as editable domain data.

### Create

1. Create retains the prior stable context in memory and enters `creating`.
2. Name and value start empty; ID reads “Assigned when saved” and is not an
   input.
3. Client validation mirrors `ARC-CTR-001` only for feedback; the API remains
   authoritative.
4. Submit disables all mutating actions, marks busy, sends exactly one POST,
   and enters `loading`.
5. A `201` replaces the view with the canonical returned record/ETag, announces
   success, records only the ID deep link, and enters `viewing`.
6. A determinate error retains the draft and focuses the summary or first
   invalid field. An indeterminate result retains the draft and offers
   Refetch/Search, never an automatic resubmit.
7. Cancel requires confirmation only for a nonempty/changed draft, then
   restores the prior stable state.

### Edit and save

1. Edit copies canonical name/value to a draft and retains ID/ETag.
2. Save validates and sends exactly one PATCH with the retained `If-Match`.
3. Success replaces record/ETag with the response and announces Saved. A
   normalized no-op remains success without falsely claiming a revision change.
4. Cancel restores the unchanged canonical view; leaving a dirty draft requires
   explicit discard confirmation.
5. A `412` enters `conflict`, preserves the draft, and offers only Reload
   latest—with explicit discard confirmation—and Copy draft for manual
   reconciliation.
6. No Force save, automatic merge, hidden retry, or last-write-wins path exists.

## Search, browse, and navigation flows

Search exposes labelled Field, Match mode, and Query controls. Field options
are ID, Name, and Value. Modes are Exact, Starts with, Ends with, Contains, and
Regular expression. Help explains case-sensitive literal behavior or
RE2-compatible unanchored regex. Empty query is accepted only for exact Value;
the API still validates every combination.

Submitting creates one context, clears old cursor history/results, and requests
one page with default limit `25`. Results remain in API order with full IDs
available so duplicate names remain distinguishable. An empty page is a
successful explicit empty state. Forward paging follows only the returned
cursor; back paging uses in-memory prior cursor/context and reruns the page.
Reload discards that history. Selection retrieves the current record and ETag
before edit and retains context/ceiling for neighbor navigation.

Previous/Next uses the retained search context when present and browse context
otherwise. Returned boundaries announce start/end, disable the unavailable
direction, and never wrap. An ID no longer in context or cursor/context
mismatch offers explicit Restart search/refetch; the client never guesses,
resorts, or filters membership locally.

## Asynchrony, errors, and truthfulness

- Every UI intent receives a monotonically increasing in-memory request token;
  only the current token may update that view.
- Obsolete GETs may be aborted. Cancellation after POST/PATCH dispatch never
  proves rollback and uses indeterminate handling.
- Mutating actions remain disabled for the complete in-flight write;
  double-click, key repeat, or late responses cannot issue or confirm a second
  accepted write.
- Search changes obsolete prior results. Page unload uses no `sendBeacon`,
  background replay, or automatic retry.
- Validation, not-found, conflict, capacity, boundary, context/cursor mismatch,
  unavailable, indeterminate, and protocol/internal outcomes remain visibly
  distinct and preserve/discard draft/current state exactly as the contract
  specifies.
- A malformed success or problem never renders partial decoded data. A network
  failure never produces a success message.

Client error text does not echo full record values or raw regex/query text.
Known server issue paths map only to known controls; unknown paths become safe
form-level errors and are never inserted into selectors or HTML.

## Accessibility boundary

The product must meet all applicable WCAG 2.2 Level A and AA criteria plus the
contract's concrete obligations:

- prefer native semantic elements and labels; every control has a persistent
  accessible name;
- make every action, result, page control, dialog, and conflict recovery path
  keyboard operable with visible focus and no trap;
- move focus to the main heading on route load, the error summary after failed
  submit, the record heading after successful create/navigation, and the
  triggering control after panel/dialog cancellation;
- announce ordinary asynchronous status politely and blocking errors concisely
  through an assertive region without repeating full content;
- preserve logical reading, DOM, and focus order at 320 CSS pixels and 200%
  zoom without essential horizontal-page overflow;
- meet AA text/background and focus-indicator contrast and never communicate
  state by color alone;
- honor reduced motion and avoid essential timing, flashing, drag-only,
  hover-only, or precision-pointer actions;
- meet WCAG 2.2 Target Size (Minimum) where applicable and protect discard of
  unsaved changes; and
- supplement automated checks with keyboard, zoom, available high-contrast,
  and screen-reader review.

At each release, conformance covers the latest two stable desktop major
versions of Chrome, Edge, and Firefox and the latest stable desktop Safari
available to the test owner. JavaScript is required. Mobile and no-JavaScript
operation are outside the accepted product claim, although the 320 CSS-pixel
layout obligation remains.

## Browser security and storage boundary

Record, query, error, and problem text is inserted only as text or equivalently
escaped content, never as HTML. The server supplies at least the accepted
restrictive policy:

```text
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; font-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'
Referrer-Policy: no-referrer
X-Content-Type-Options: nosniff
Cross-Origin-Opener-Policy: same-origin
Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=(), usb=()
```

Scripts and styles are external content-addressed same-origin assets with no
`unsafe-inline` or `unsafe-eval`. The candidate uses no third-party content,
cookie, service worker, Cache API, localStorage, sessionStorage, IndexedDB,
telemetry, or cross-origin fetch. Record/API responses are `no-store`. Console
production output contains no record/query data.

## Security and permitted-use boundary

- Same-origin loopback is a limited local trust model, not an authentication or
  remote-access control system. There is no account, role, session, token, TLS,
  or per-user audit claim.
- Browser memory holds current data and drafts only for the active document;
  reload discards them. Browser history and URLs retain no record/query content.
- Fixtures, screenshots, accessibility artifacts, browser traces, console
  output, network captures, source maps, and evidence must use classified
  synthetic/de-identified inputs and be reviewed for unintended disclosure.
- Actual or possible ePHI, production/confidential records, remote or
  multi-user use, shared workstations, third-party processing, external
  telemetry, or formal compliance claims trigger successor review and remain
  unauthorized.
- Passing `WEB` vectors, accessibility automation, or CSP scans cannot
  substitute for exact NIST and HIPAA policy/evidence gates.

## Security-policy applicability

| D6 concern | NIST policy anchors | HIPAA policy anchors | Candidate evidence direction |
|---|---|---|---|
| Permitted use and truthful claims | `SEC-POL-01`, `SEC-POL-14` | `HSP-001`, `HSP-002`, `HSP-015` | Fixture/data-flow inventory, product limitations, negative successor-trigger review, no broad compliance claim |
| Loopback/same-origin access | `SEC-POL-02`, `SEC-POL-03`, `SEC-POL-06` | `HSP-004`, `HSP-005`, `HSP-006` | Host/Origin/CORS/proxy/alternate-interface negatives, route inventory, no credentials or alternate origin |
| Safe presentation and transient state | `SEC-POL-05`, `SEC-POL-06`, `SEC-POL-08` | `HSP-006`, `HSP-007`, `HSP-008`, `HSP-010` | XSS/text-rendering vectors, storage/history/cache/console inspection, redacted browser/evidence artifacts |
| Availability, races, and reconciliation | `SEC-POL-07`, `SEC-POL-09`, `SEC-POL-13` | `HSP-007`, `HSP-010`, `HSP-012` | Double-action/late-response/fault tests, accurate unavailable/indeterminate states, incident/recovery exercise |
| Bundle and release integrity | `SEC-POL-04`, `SEC-POL-10`, `SEC-POL-12` | `HSP-009`, `HSP-013` | Exact source/bundle/manifest/image hashes, SBOM/provenance/signature disposition, scan/license/external-service evidence |
| Secure development and assurance | `SEC-POL-11` | `HSP-003`, `HSP-014` | Named owner/risk mapping, accessibility/manual review, architecture/policy/vector traceability, exact evidence and reviewer |

Every policy needs an exact future applicability decision. This table is an
evidence-routing aid; it records no pass, waiver, inherited-control acceptance,
or exception.

## Required invariant verification

The minimum D6 claim would require all exact `WEB` vectors:

| Vector | Candidate evidence obligation |
|---|---|
| `WEB-001` | Prove initial/empty, create, view, edit, cancel, and save states, focus/actions, immutable ID, and no autosave. |
| `WEB-002` | Prove one write per intent and that late/obsolete GETs cannot replace current state. |
| `WEB-003` | Prove `412` preserves the draft and offers Reload/Copy Draft only, with no force/merge/retry. |
| `WEB-004` | Prove indeterminate create/update makes no success or rollback claim and preserves draft/reconciliation actions. |
| `WEB-005` | Prove all search modes, empty results, paging/back, and selection preserve API membership/order and in-memory context/ceiling. |
| `WEB-006` | Prove accessible start/end boundary and context-mismatch Restart behavior without wrap or guessing. |
| `WEB-007` | Prove every validation/API/transport/protocol failure has the correct summary, focus, live-region, draft treatment, and safe request ID. |
| `WEB-008` | Prove malicious HTML/script/style/URL-like record/problem content renders only as text and cannot execute or navigate. |
| `WEB-009` | Inspect browser storage/cache/network and prove no prohibited storage, telemetry, cross-origin data, or cache of API responses. |
| `WEB-010` | Complete keyboard, focus, 200% zoom, 320-pixel, contrast, reduced-motion, and screen-reader evidence for applicable WCAG 2.2 A/AA obligations. |
| `WEB-011` | Run the required Chrome/Edge/Firefox/Safari release matrix with no skips in the claimed matrix. |
| `WEB-012` | Prove a coherent content-hashed first-party bundle in the API image, exact headers/controls, and no runtime Node/compiler/remote dependency/host service. |
| `WEB-013` | Compare browser and CLI/SDK route inventories and prove the same `/api/v1` resources, methods, problems, and results; only origin differs. |

Applicable `DOM`, `HTTP`, `SRCH`, `NAV`, `CNT`, `OPS`, and `E2E` vectors remain
additive. Required evidence includes exact bundle copy/hash provenance, CSP and
headers across entry/assets/API/health/errors, same-origin Host/Origin
negatives, container content, API unavailability/recovery, stale-draft
conflicts, search parity, lifecycle from a clean supported host, and equivalent
CLI/web outcomes. Screenshots alone do not prove accessibility or behavior.

## Evidence-record boundary

Any future execution record must identify the evidence ID;
`ARC-SUITE-001@2.0.1` and vector IDs; NIST/HIPAA suite, policy, and gate IDs;
D6 semantic version, bundle/manifest/API-image hashes, Compose/render hash and
source commit; host/OCI/browser/assistive-technology/dependency identities;
exact containerized build plus browser/static/live/end-to-end method and
fixture seed; UTC time; results and skips; limitations; nonpass dispositions;
and reviewer identity.

An automated accessibility score, screenshot, asset load, API health response,
unit coverage report, CSP header check, or one-browser success cannot prove the
full D6 claim.

## Dependencies, sequence, and handoffs

| Relationship | Required identity | Boundary preserved |
|---|---|---|
| `v1.0` / D1 -> D6 | Exact architecture/contract revision and derivative documentation used | Documentation guides the UI but does not prove it. |
| `v2.0` / D2 -> D6 | Exact `web-build` target, effective Compose topology, base/platform identities, bundle-copy/hash chain | D6 does not claim platform completion. |
| `v2.1` / D3 -> D6 | Compatible API image/digest, static manifest slot, same-origin `/api/v1`, Host/Origin/header behavior | D6 neither changes the server contract nor claims persistence/API completion. |
| `v3.0` / D5 -> D6 | Accepted delivery-sequence evidence and shared capability/result/route parity | D5 precedes D6, but CLI code or completion is not part of D6. |

The exact bundle and API image deploy atomically for D6 evidence. Their hashes
and completion records remain separate. A later API image may embed no bundle,
an earlier bundle, or a new bundle only according to explicit compatibility and
release records; the presence of bytes alone proves neither product.

## Risks to preserve for proposal analysis

| Risk | Consequence |
|---|---|
| Client validation becomes authoritative | Valid server behavior can be rejected or invalid behavior widened silently. |
| Late GET or double activation changes state | A stale view or duplicate write can be presented as current success. |
| Conflict handling adds force or merge | Revision safety and explicit user reconciliation are lost. |
| Query/value enters URL, history, console, source map, or telemetry | Record content escapes the transient same-origin boundary. |
| UI filters or sorts results locally | Search membership/order diverges from every other surface. |
| HTML insertion or permissive CSP is used | Untrusted content can execute or alter navigation/presentation. |
| Browser persistence or service worker is introduced | Stale or sensitive record copies survive beyond the active document. |
| Host dev server or alternate origin becomes a supported path | Compose-only delivery and exact local trust controls are bypassed. |
| Embedded assets are treated as D3/D6 joint completion | Independent evidence, blockers, owners, and release truth are obscured. |
| Automated accessibility output is treated as the audit | Keyboard, zoom, focus, contrast, announcement, and AT failures remain hidden. |
| Test screenshots/traces contain real data | Evidence artifacts violate the permitted profile even if runtime controls pass. |

## Questions that remain for a future proposal

1. Which exact repository and product paths own web source, static manifest,
   compiled assets, accessibility reports, browser traces, and release evidence?
2. Which framework or no-framework approach and dependency patch locks fit the
   accepted typed-adapter, state, accessibility, CSP, and runtime-content limits?
3. Which web semantic version and compatibility policy are proposed without
   confusing them with this `v4.0` realization-suite label?
4. Which exact browser, operating-system, screen-reader, high-contrast, and
   qualified Safari environments make up the first release matrix?
5. What source-map disposition is selected, and how is absence of secrets,
   host paths, record data, and unsafe runtime dependencies verified?
6. Who owns accessibility review, security/risk analysis, bundle/API
   compatibility, vulnerability/license review, and evidence retention?
7. Does any independently releasable design-system, help, or accessibility
   sub-scope have a different owner, destination, lifecycle, or acceptance
   claim that requires a separate dot-version suite?

No answer is selected by this note.

## Candidate outcome

A local user can open one exact same-origin, container-built browser bundle and
create, retrieve, edit, search, and navigate records through the shared API
with keyboard- and assistive-technology-usable controls, preserved drafts,
accurate conflicts and indeterminate outcomes, safe transient state, and
reviewable bundle/browser evidence—without an alternate server, durable client
copy, direct database path, remote-use claim, or completion claim broader than
the independently evidenced D6 artifact.

## Suggested next step

Take no initiative action now. If later explicitly directed, prepare one
D6-only proposal from this realization, cite the exact invariant sources and
policy IDs, identify compatible D2/D3 artifact hashes and D5 sequence evidence,
choose product destinations and owners, perform the mandatory scope assessment,
and preserve all unresolved choices for explicit human disposition.

## Handoff notes

A receiving proposal must cite this realization and its `v4.0` suite, preserve
the historical Product 4 lineage, distinguish suite identity from bundle
semantic version, map every state and release claim to authoritative contracts
and additive security evidence, and avoid treating this detailed realization
as an accepted UI specification or implementation authorization.

