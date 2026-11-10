# API and SQLite runtime image

**Realization ID:** `RZN-001-P2-API-SQLITE-N01`  
**Suite:** [`RZN-001-P2-API-SQLITE-SUITE@v2.1`](00-RZN-001-P2-API-SQLITE-suite-index.md)  
**Suite version:** `v2.1`  
**Status:** Recorded; invariant-bounded proposal input  
**Recorded by:** Codex on behalf of the User  
**Recorded date:** 2026-11-10  
**Source:** User request in the current Codex conversation and [`RZN-001`](../v0/RZN-001-example-record-application.md)  
**Historical product lineage:** API portion of `RZN-001-P2-SDK-API`  
**Accepted delivery-unit alignment:** `D3 API and SQLite runtime image`  
**Related initiative or proposal:** None created  

> **Evidence standing:** This note is detailed realization input for one D3
> outcome. It does not accept an API specification, implement a server or
> database, create an image, run a test, assess a security control, or claim
> product completion. The cited architecture owns every accepted behavior.

## Realization

There is a bounded opportunity to deliver one API and SQLite runtime image
that realizes the accepted three-field record domain, `/api/v1` HTTP contract,
bounded search and navigation semantics, exclusive SQLite persistence,
health/static-asset hosting, and stopped-API maintenance behavior on a
compatible D2 platform.

The opportunity is narrower than the historical Product 2 label: it excludes
the independently versioned Python SDK, CLI, and web interaction products.
The image may embed D6 assets when they later exist, but static hosting does
not make the browser bundle part of D3's acceptance claim.

## Narrow outcome and beneficiary

| Dimension | Candidate record |
|---|---|
| Outcome | A compatible D3 OCI image whose live API and SQLite behavior conform to the accepted domain, HTTP, query, persistence, operations, and security contracts |
| Primary beneficiaries | SDK/client implementers, CLI and web product owners, local operators, persistence owners, and conformance reviewers |
| Authority boundary | API/domain/query/persistence/health/static-hosting and compatible maintenance code; no client interaction ownership or platform completion claim |
| Output class | API application packages, repository adapter, ordered migrations, maintenance commands, health/static routes, OpenAPI derivative, API runtime image, and D3 evidence |
| Independent review claim | The exact image and store behavior pass the D3 architecture and security gates on supported matrices |
| Explicit non-claim | No SDK wheel behavior, CLI image, web UI/accessibility, D2 platform completion, remote deployment, regulated use, or compliance certification |

## Context and evidence

| Question | Record |
|---|---|
| What was requested? | `RZN-001` asked for a Pydantic-modeled API over SQLite supporting create, retrieve, update, search, and next/previous behavior. |
| What is now authoritative? | Architecture `2.0.1` fixes the domain, routes, models, failures, search dialect, ordering, cursor, concurrency, schema, transaction, migration, maintenance, health, deployment, and verification meanings. |
| What is current product status? | `ARC-CTR-009` records no supplied D3 implementation or conformance evidence. |
| What is uncertain? | Exact source paths and module names within the accepted layer boundaries, dependency patch/digest locks, implementation sequencing, evidence storage, and whether any further sub-scope needs separate governed work without merging D3 with D2/D4. |
| Which data is allowed? | Non-production purpose-created synthetic data or externally documented de-identified data that also meets NIST restrictions; actual or possible ePHI and higher-control data are prohibited. |

## Binding source inventory

| Source | Exact relevance |
|---|---|
| [`ARC-CTR-001`](../../../authoritative/architecture/11-record-domain-contract.md) | Exact public record, normalization, validation, mutability, equality, internal-metadata boundary, and domain failures. |
| [`ARC-BND-002`](../../../authoritative/architecture/12-api-service-boundary.md) | API layers, responsibilities, request pipeline, state authority, startup/readiness, and failure boundaries. |
| [`ARC-CTR-002`](../../../authoritative/architecture/13-record-http-contract.md) | `/api/v1` create/get/update, media, headers, ETags, problems, status codes, and route exclusions. |
| [`ARC-CTR-003`](../../../authoritative/architecture/14-search-navigation-contract.md) | Browse/search/regex, cursors, ceilings, membership, ordering, pagination, neighbors, boundaries, and budgets. |
| [`ARC-BND-003`](../../../authoritative/architecture/15-sqlite-store-boundary.md) | Live-store placement, ownership, lock, capacity, failure, and recovery boundary. |
| [`ARC-CTR-004`](../../../authoritative/architecture/16-sqlite-persistence-contract.md) | Database identity/schema, pragmas, repository surface, transactions, migrations, backups, restore, and integrity. |
| [`ADR-001`](../../../authoritative/architecture/04-ADR-001-api-exclusive-persistence.md) | Sole normal runtime database authority and identical shared API path for all consumers. |
| [`ADR-002`](../../../authoritative/architecture/05-ADR-002-identity-order-and-concurrency.md) | UUIDv4, internal ordinal/revision/timestamps, ETag, and no-op behavior. |
| [`ADR-003`](../../../authoritative/architecture/06-ADR-003-search-execution-semantics.md) | Centralized NFC/case-sensitive literal and RE2-compatible bounded regex behavior. |
| [`ARC-CTR-008`](../../../authoritative/architecture/23-operations-security-contract.md) | Runtime limits, exact Host/Origin, health, logs, lifecycle, maintenance, recovery, and security-policy integration. |
| [`ARC-CTR-009`](../../../authoritative/architecture/24-conformance-contract.md) | D3 gate and required `DOM`, `HTTP`, `SRCH`, `NAV`, `DB`, platform/operations, and API end-to-end vectors. |
| [`SEC-NIST-POL-001`](../../../authoritative/security/NIST/01-demonstrator-security-policy.md) and [`SEC-NIST-VER-001`](../../../authoritative/security/NIST/03-future-development-assurance.md) | Primary NIST-aligned requirements and exact prospective evidence anchors. |
| [`SEC-HIPAA-POL-001`](../../../authoritative/security/HIPPA/02-prospective-security-policy.md) and [`SEC-HIPAA-DEV-001`](../../../authoritative/security/HIPPA/04-future-development-and-evidence-standard.md) | Primary data-use/safeguard requirements and exact prospective records/evidence. |

## Candidate internal layering

The architecture already requires dependencies to point inward:

```text
HTTP routes and middleware
        -> application commands and queries
        -> domain values and policies
        -> repository port
        -> SQLite adapter
```

The candidate D3 outcome would make that boundary observable. Domain code
would not import FastAPI, HTTPX, browser, CLI, or SQLite modules; routes would
not issue SQL; the adapter would not own HTTP behavior; generated OpenAPI would
describe observed routes without superseding the accepted Markdown contracts.

## Candidate domain behavior

| Concern | Accepted behavior a future D3 product would need to realize |
|---|---|
| Public shape | Exactly `id`, `name`, and `value`; closed strict representations; no public ordinal/revision/timestamps |
| Identity | API-generated OS-CSPRNG UUIDv4, lowercase canonical form, caller ID forbidden, immutable after commit |
| Name | Strict string; CR/CRLF handling, Unicode-edge trim, NFC, single-line/control restrictions, 1-120 scalar values and at most 480 UTF-8 bytes |
| Value | Strict string; LF-normalized, NFC, whitespace preserved, TAB/LF permitted, other controls rejected, 0-4,096 scalar values and at most 16,384 bytes |
| Patch | Presence-aware `name` and/or `value`; null/unknown/empty patch rejected; normalized no-op preserves revision and update time |
| Equality and duplicates | All canonical public fields define representation equality; duplicate name/value pairs remain distinct records |
| Exclusions | Delete, archive, undelete, merge, caller-selected ID, bulk operations, history, record import/export, and offline writes absent |

## Candidate HTTP surface

| Operation | Exact route | Candidate success | Candidate principal boundaries |
|---|---|---|---|
| Create | `POST /api/v1/records` | `201`, exact record, `Location`, strong `ETag`, request ID, no-store after commit | No caller ID, no `Idempotency-Key`, no write replay; loss after dispatch may be indeterminate |
| Retrieve | `GET /api/v1/records/ID` | `200`, exact record, current strong `ETag` | `ID` denotes the canonical path value; invalid and absent remain distinct; read is side-effect-free |
| Update | `PATCH /api/v1/records/ID` | `200`, exact record, same or incremented ETag | `ID` denotes the canonical path value; exactly one current strong `If-Match`; no force/merge/last-write-wins; stale write changes nothing |
| Browse/search | `GET /api/v1/records` | Ordered `RecordPage` with cursor/ceiling | Zero or one complete predicate; strict query parsing; complete result or explicit failure |
| Neighbor | `GET /api/v1/records/ID/neighbor` | Record with ETag or explicit start/end boundary | `ID` denotes the canonical path value; exact context/ceiling; no wrap; mismatch differs from boundary/not-found |
| Health | `GET /health/live`, `GET /health/ready` | Coarse safe status | No data/path/version disclosure or state mutation; exact allowed Host |
| Static app | `/app/` and content-addressed assets | Coherent same-origin D6 bundle when present | Hosting is D3 behavior; UI correctness and bundle completion remain D6 |

No `PUT`, `DELETE`, force update, alternate client route, direct SQL endpoint,
login, bulk, or administrative record API is a candidate capability.

## Request and problem boundary

A candidate D3 implementation would need to preserve all of these accepted
request properties:

- one public origin at `http://127.0.0.1:${RECORDS_HOST_PORT}` and one private
  base at `http://record-api:8000`, both appending identical `/api/v1` paths;
- exact public/internal Host allowlists and exact browser Origin enforcement
  before body processing; no CORS or proxy-derived identity;
- JSON object bodies only, unique keys, strict UTF-8, 32 KiB maximum, accepted
  media types, strict Pydantic v2 models, no scalar coercion, and unknown fields
  forbidden;
- safe request IDs and bounded structured outcome logs;
- centralized `application/problem+json` with stable `status`, `code`, safe
  issue ordering, and no stack, SQL, filesystem path, record value, or raw
  query disclosure; and
- distinct validation, not-found, conflict, capacity, busy, unavailable,
  search-budget, overload, and internal outcomes that never fabricate an empty
  or successful result.

## Candidate search and navigation behavior

| Concern | Accepted candidate behavior |
|---|---|
| Predicate | Browse has none; search has exactly one `field`, `mode`, and `q` triple |
| Fields/modes | `id|name|value` and `exact|starts_with|ends_with|contains|regex` |
| Literal matching | NFC, case-sensitive Unicode scalar comparison; no trim, locale, case/accent fold, token, glob, wildcard, SQL `LIKE`, or client refilter |
| Regex | Pinned RE2-compatible engine, unanchored search, explicit anchors, accepted flags, no backreferences/lookaround, 1-256 UTF-8 bytes |
| Bounds | At most 10,000 records; page 1-100; complete evaluation budget 2 seconds; no partial page presented as complete |
| Ordering | Internal ascending non-reused ordinal; ordinal never appears as a public record field |
| Snapshot | Initial maximum-ordinal ceiling excludes later creates; current values determine later-page membership |
| Cursor | Opaque validated base64url identity bound to normalized predicate and ceiling; no query text or record content |
| Neighbor | Nearest qualifying ordinal in exact browse/search context; explicit `start`/`end`, no wrap, context mismatch when current member leaves context |

SDK, CLI, browser, and SQLite are prohibited from independently deciding
membership or neighbor order.

## Candidate persistence boundary

| Property | Accepted candidate behavior |
|---|---|
| Identity and placement | SQLite application ID `1163416113`, schema/user version 1, fixed path in `record-data`, numeric ownership `10001:10001` |
| Live ownership | One API replica/process/worker holds the shared instance lock; networkless maintenance only after API stop and lock acquisition |
| Schema | Strict migration-owned tables, internal ordinal/revision/timestamps, unique canonical ID, immutability/no-delete triggers, migration hash records |
| Connections | Foreign keys on, 5 s busy timeout, WAL, `synchronous=FULL`, in-memory temporary storage, trusted schema off, extension loading disabled |
| SQL | Fixed parameterized statements; raw input never selects identifiers, clauses, paths, functions, or code |
| Writes | One in-process mutex, `BEGIN IMMEDIATE`, bounded atomic transaction, success only after commit, no automatic replay |
| Capacity | At most 10,000 committed rows; excess create fails without a committed allocation |
| Reads | Side-effect-free; typed absent/boundary differs from busy/corruption/integrity failure |
| Startup | Verify path/ownership, lock, application/schema/migration identity, required pragmas, quick check, and asset compatibility; never initialize/migrate while serving |

### Candidate transaction truths

- Create validates first, generates the UUID immediately before the write,
  checks capacity inside the transaction, commits one row, and may internally
  retry only a proved UUID collision up to three attempts before any commit.
- Conditional update validates and normalizes before the transaction, checks
  ID and expected revision inside it, returns absence/conflict distinctly,
  preserves metadata on a normalized no-op, and increments revision exactly
  once on a material update.
- Connection loss, cancellation, deadline, container kill, or daemon failure
  cannot be translated into a rollback or success claim without authoritative
  evidence of the final transaction.

## Candidate migration, backup, and restore behavior

The D3 image owns compatible code and resources for these behaviors; the D2
platform owns their container topology and mounts.

| Operation | Candidate invariant-bounded behavior |
|---|---|
| Initialize | Stopped-API networkless maintenance only; provably empty accepted volume; ordered immutable migration; validate before success; refuse overwrite |
| Check | Read-only application-level validation of identity, ownership, schema, migration hashes, capacity, rows, and `quick_check`; no mutation |
| Migrate | API stopped and lock free; mandatory new validated backup; compatible image; one accepted ordered migration at a time; no automatic downgrade |
| Backup | New generated artifact in separate backup volume; SQLite-consistent copy; metadata/hash; row/schema/integrity validation; atomic finalize; never overwrite |
| Export/import | Opaque framed validated backup artifact through bounded streams; no live mount, arbitrary path, merge, or record-level interchange |
| Restore | Validate source and candidate, preserve former live set, switch under stopped-API ownership, start exact image, run readiness/domain smoke, and roll back on failure |

No same-host backup claim implies host-loss recovery. Backups inherit their
data sensitivity and use restrictions.

## Operational and safe-failure boundary

- The API runs one Uvicorn process/worker in the D2-hardened image and uses a
  bounded synchronous worker pool.
- At most 64 requests are admitted; header/body, worker, busy, query, request,
  CPU, memory, PID, tmpfs, and log limits remain bounded.
- Readiness becomes false for persistent unsafe store, lock, schema, ownership,
  or required-asset conditions; ordinary validation/not-found/conflict does
  not make the process unready.
- Logs contain safe metadata only and remain diagnostic, not an audit trail or
  record store.
- OOM, forced kill, daemon restart, or lost response requires lock/store/
  schema/integrity re-verification before readiness.
- Runtime makes no outbound request and receives no application secret.

## Security-policy applicability

| D3 concern | NIST policy anchors | HIPAA policy anchors | Candidate evidence direction |
|---|---|---|---|
| Data/use and truthful claims | `SEC-POL-01`, `SEC-POL-14` | `HSP-001`, `HSP-002`, `HSP-015` | Fixture manifest, data-path inventory, release limitations, negative trigger review |
| API/network boundary | `SEC-POL-02`, `SEC-POL-06` | `HSP-004`, `HSP-005`, `HSP-006` | Host/Origin/proxy negatives, strict parser, safe rendering/outputs, no alternate route |
| Least privilege and resources | `SEC-POL-03`, `SEC-POL-07` | `HSP-009` | Image/runtime probes, resource/fault tests, safe restart/readiness |
| State integrity | `SEC-POL-05` | `HSP-007` | Mount/lock/schema/transaction/concurrency/corruption/migration evidence |
| Logging and activity limits | `SEC-POL-08` | `HSP-008` | Log schema, redaction, rotation, activity-review procedure, non-audit disclaimer |
| Recovery and host/media dependencies | `SEC-POL-09`, `SEC-POL-13` | `HSP-010`, `HSP-011`, `HSP-012` | Backup/restore/rollback drill, custody/encryption decision, incident exercise |
| Build/release and vulnerabilities | `SEC-POL-04`, `SEC-POL-10`, `SEC-POL-12` | `HSP-009`, `HSP-013` | Exact image identity, SBOM/provenance/scans, external-service and egress inventory |
| Secure development and evidence | `SEC-POL-11` | `HSP-003`, `HSP-014` | Named owner, risk analysis, policy/vector traceability, exact evidence record and source review |

Every policy still requires an individual future applicability decision. This
table is an evidence-routing aid, not a pass or accepted exception.

## Candidate conformance boundary

The D3 gate requires all applicable `DOM-*`, `HTTP-*`, `SRCH-*`, `NAV-*`,
`DB-*`, `OPS-*`, `CNT-*`, and API portions of `E2E-*`, plus the exact NIST and
HIPAA evidence for the same image and claim.

| Evidence group | Candidate claim it could support | Important limitation |
|---|---|---|
| `DOM-001`-`012` | Canonical record normalization, strict validation, duplicate behavior, no-op, and ID immutability | Pure domain tests do not prove HTTP or persistence. |
| `HTTP-001`-`012` | Routes, headers, media, problems, ETags, failures, request IDs, and indeterminate writes | HTTP mocks alone do not prove real SQLite behavior. |
| `SRCH-001`-`018` | Exact literal/regex membership, limits, cursors, ceilings, and cross-surface equality | D3 can prove direct API results but not complete SDK/CLI/web packaging. |
| `NAV-001`-`008` | Browse/search adjacency, boundaries, context mismatch, and determinism | Client presentation remains owned by later products. |
| `DB-001`-`010` | Schema, lock, capacity, concurrency, fault rollback, migration, backup/restore, and corruption behavior | Platform topology must use the compatible D2 artifact; one local engine run is not full matrix evidence. |
| Applicable `CNT`/`OPS` | Exact image, runtime, Host/Origin, health, resources, logs, recovery, and supply chain | Passing D2 controls is additive, not a substitute for API behavior. |
| API portions of `E2E` | Shared path, parity oracle, outage/recovery, excluded capabilities, and exact state path | Later client evidence is still required for their own claims. |

The future evidence record must preserve image/manifest digest, source commit,
architecture and policy revisions, D2 Compose hash, Python/SQLite/RE2 and
dependency identities, schema/migrations, host/OCI platform, named test
volumes, exact containerized method, results, limitations, dispositions,
reviewer, and fixture classification. This note records none of those results.

## Dependencies and consumer handoffs

| Relationship | Required identity | Boundary preserved |
|---|---|---|
| D1 -> D3 | Exact contract/architecture revision and any derivative docs used | Behavior follows accepted authority, not implementation convenience. |
| D2 -> D3 | Exact BuildKit target, Compose render, platform/image identity, volumes, network, security controls | D3 does not absorb platform completion. |
| D3 -> D4 | Exact `/api/v1` compatibility, live test endpoint, OpenAPI derivative, problem/search fixtures, image digest | SDK remains independent and server behavior remains D3-owned. |
| D3 -> D5 | Compatible API image/route semantics through D4 wheel | CLI does not add routes or open SQLite. |
| D3 -> D6 | Same-origin API/static hosting, exact API image and bundle slot/manifest interface | Web bundle state/accessibility remains D6; embedding does not merge completion. |

## Risks to preserve for proposal analysis

| Risk | Consequence |
|---|---|
| Routes or generated models become the authority | Implementation drift silently replaces accepted contracts. |
| API startup initializes or migrates | Serving can mutate unreviewed state and hide compatibility failures. |
| Search delegates semantics to SQLite/client | Results diverge across surfaces or unsafe regex/resource behavior appears. |
| Busy/corrupt store maps to empty/not-found | Data loss or unavailability is falsely reported as a domain result. |
| HTTP write retry after uncertain dispatch | Duplicate create or unintended repeated update can occur. |
| Multiple API workers/replicas share SQLite | Locking and transaction assumptions are violated. |
| Static web hosting is treated as D6 completion | Browser behavior/accessibility/security evidence is hidden. |
| Test or recovery data is real or insufficiently classified | Source, volumes, backups, logs, screenshots, and evidence breach the permitted profile. |
| Passing architecture vectors is treated as security conformance | Required policy/risk/host/media/incident records remain missing. |

## Questions that remain for a future proposal

1. Which exact source and product paths will own API, domain, query,
   persistence, migration, maintenance, and static-hosting code?
2. Which dependency patch versions, base digest, SQLite build, RE2 wheel, and
   Python image identities will be proposed for the first compatible D2/D3
   matrix?
3. Which test seams provide controlled clocks, UUIDs, faults, deadlines, and
   network loss without weakening production defaults?
4. How will exact contract fixtures and OpenAPI drift evidence be stored and
   reviewed without making generated output authoritative?
5. Which D3 owner is accountable for the risk analysis, security evidence,
   activity review, incident drill, recovery drill, and source-currency check?
6. Does any implementation sub-scope meet a mandatory split trigger while
   still preserving one coherent D3 artifact and completion boundary?

No answer is selected by this realization.

## Candidate outcome

On a compatible D2 platform, one digest-identified API image provides the
accepted record, search, navigation, persistence, health, and maintenance
behavior through one `/api/v1` authority; it fails safely, preserves exact
transaction and recovery truth, hosts only compatible embedded assets, and
produces exact evidence without claiming the SDK, CLI, web, regulated use, or
general security compliance.

## Suggested next step

Take no initiative action now. If later directed, prepare a D3-only proposal
from this note, cite the exact contract and policy IDs, choose the product
destinations and compatible D2 baseline, perform the mandatory scope
assessment, and preserve every unresolved proposal question for explicit human
disposition.

## Handoff notes

A receiving proposal must cite this realization and its v2.1 suite, preserve
the historical Product 2 API lineage without recombining it with the v2.2 SDK
suite, and map each accepted D3 behavior to its authoritative owner, product
destination, exact verification, and security evidence record.

