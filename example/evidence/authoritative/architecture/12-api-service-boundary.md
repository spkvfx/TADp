# Record API service system boundary

**Architecture ID:** `ARC-BND-002`  
**Status:** Accepted  
**Architecture revision:** `2.0.0`  
**Owner:** API component owner under a future accepted initiative  
**Last reviewed:** 2026-11-10  
**Related records:** [`ARC-CTR-001`](11-record-domain-contract.md), [`ARC-CTR-002`](13-record-http-contract.md), [`ARC-CTR-003`](14-search-navigation-contract.md), [`ARC-CTR-004`](16-sqlite-persistence-contract.md), [`ARC-CTR-008`](23-operations-security-contract.md)  

## Boundary statement

The API service boundary begins at container port 8000 on the private Compose
network and ends at the repository port to the exclusively owned SQLite
adapter on the `record-data` named volume. Inside are request
correlation, content negotiation, Pydantic validation, domain normalization,
UUID generation, conditional-update enforcement, search compilation and
evaluation, navigation, transaction orchestration, error translation, health
reporting, static web-asset serving, and OpenAPI generation. Docker host-port
publication, Compose DNS/network/volume lifecycle, image construction, browser
rendering, SDK conveniences, CLI parsing, offline maintenance, remote
authentication, and backup storage remain outside.

## Internal layers

Dependencies must point inward in the following order:

```text
HTTP routes / middleware
        -> application commands and queries
        -> domain values and policies
        -> repository port
        -> SQLite adapter
```

- Domain code must not import FastAPI, HTTPX, browser, CLI, or SQLite modules.
- The SQLite adapter may implement the repository port but may not own HTTP or
  user-interface behavior.
- Routes must not issue SQL directly.
- Generated OpenAPI describes the implemented route schema but does not
  override the accepted Markdown contracts when a defect creates a mismatch.

## Responsibilities

| Responsibility | Boundary owner | Explicitly outside this boundary |
|---|---|---|
| Listen on `0.0.0.0:8000` inside `record-net` and expose `/api/v1` | API transport layer | Host publication, Compose DNS/network, public ingress, TLS/proxy identity |
| Decode JSON, enforce media types and size limits, validate models | Pydantic route layer | Client-side-only validation or permissive unknown fields |
| Normalize and enforce record invariants | Domain layer | SDK/CLI/web redefinition of field meaning |
| Generate UUIDv4, internal timestamps, and correlation IDs | Application/domain services using OS CSPRNG and UTC clock | Caller-provided record IDs or client-authoritative clocks |
| Execute create/get/update/search/neighbor behavior | Application services | Presentation, interactive prompting, or client paging history |
| Enforce ETag preconditions and map revisions | Application plus repository adapter | Last-write-wins or force-update endpoints |
| Own all normal-runtime access to live database | Repository port/SQLite adapter on `record-data` | Direct SDK/CLI/browser/test/host access; stopped-API maintenance is separately bounded |
| Emit bounded health and privacy-aware observability | Operations layer | Record export through logs or remote telemetry |
| Serve immutable web assets and browser entry document | Static asset route | Building assets or owning browser UI state |

## Inputs and outputs

| Direction | Counterparty | Interface or artifact | Validated by | Compatibility rule |
|---|---|---|---|---|
| Inbound | CLI/SDK containers | HTTP requests to `http://record-api:8000/api/v1` on private network | Internal Host allowlist, body limit, route schema, domain | `/api/v1` follows `ADR-006`; no Origin required for non-browser clients |
| Inbound | Host browser adapter | HTTP requests through `http://127.0.0.1:${RECORDS_HOST_PORT}/api/v1` | Public Host/exact Origin middleware, body limit, route/domain | Browser writes require exact configured public Origin; CORS absent |
| Inbound | Compose | Validated container environment, named-volume mount, resource/security settings | Typed startup settings plus conformance of rendered Compose | Unsafe/missing container settings stop readiness; API cannot authorize host publication itself |
| Inbound | SQLite adapter | Records or persistence failures | Repository-result decoder and invariant checks | Corrupt rows are never returned as valid resources |
| Outbound | API clients | JSON resources, ETags, cursors, and problem documents | Pydantic response models and centralized exception mapping | Stable field meaning and error codes for API v1 under architecture v2 |
| Outbound | SQLite adapter | Parameterized repository commands/queries | Repository adapter | No SQL text or identifiers derived from untrusted values |
| Outbound | Docker/Local operator | Health, structured stdout/stderr, process exit status | Operations policy | No in-container log file; output excludes `value` and raw query content |
| Outbound | Browser | Entry HTML and content-addressed static assets | Static manifest | HTML may reference only current built assets and same-origin API URLs |

## Request execution rules

1. Assign or validate `X-Request-ID` before logging. A supplied value must be
   1-64 ASCII letters, digits, `_`, `-`, or `.`; otherwise generate a random
   UUIDv4 request ID.
2. Validate `Host` against the exact public host/port and internal service
   host/port allowlist. If `Origin` is present, require the exact public origin;
   reject mismatches before reading a body.
3. Reject bodies over 32 KiB, unsupported media types, invalid UTF-8/JSON,
   duplicate JSON object keys, non-object payloads, unknown fields, and invalid
   model values before application execution.
4. Normalize domain strings exactly once under `ARC-CTR-001`.
5. Execute one application command/query. Writes use one bounded transaction;
   reads do not silently write schema or application state.
6. Convert the repository outcome into one response model or one centralized
   problem document. Never return a successful body after rollback or an
   unhandled internal exception body containing stack or SQL details.
7. Emit a completion log containing request ID, route template, method, status,
   duration, and safe error code only.

## State and authority

| State or decision | System of record | Write authority | Recovery or reconciliation rule |
|---|---|---|---|
| Records, ordinals, revisions, timestamps, schema version | SQLite store | Repository adapter inside a transaction | `ARC-CTR-004` restore/migration procedures |
| Route and model behavior | Accepted contracts in this suite | Architecture authority; implementation must conform | Correct product or explicitly revise architecture |
| In-memory compiled regex, connection handles, static manifest | API process memory | API process | Rebuild on restart; never treated as durable |
| OpenAPI document | Generated from current route implementation | Build pipeline | Compare with accepted contract; generation cannot resolve mismatch |
| Runtime image and embedded web manifest | Immutable image digest/labels | Containerized build/release | Replace container with a verified image; never patch files in place |

## Invariants and failure boundaries

- The API runs as exactly one container replica, one Uvicorn process, and one
  application worker per `record-data` volume. Compose scaling is prohibited.
- The image runs as `10001:10001` with read-only root filesystem; only declared
  tmpfs and `record-data` are writable. It has no Docker socket or backup mount.
- Startup must acquire the instance lock, validate configuration, verify schema
  compatibility and `PRAGMA quick_check` before readiness becomes true. It does
  not initialize/migrate an unprepared database; the maintenance container owns
  those offline changes.
- Missing/uninitialized/unknown schema, failed prior migration, corruption,
  wrong fixed container path/permissions, or inability to obtain the instance
  lock must fail readiness/startup.
- The API intentionally binds all container interfaces at port 8000. Host
  loopback-only publication and private-network attachment are verified from
  rendered Compose and runtime network inspection, not inferred from this bind.
- The public and internal origins terminate on one identical `/api/v1` router.
  CLI-only and web-only record routes, representations, or semantics are
  prohibited; origin selection changes transport reachability only.
- The API must not reveal SQL, filesystem paths, stack traces, record values,
  or raw regex/search strings in client errors or routine logs.
- A cancelled/disconnected write request may finish only if its transaction is
  already committing; the outcome is then discoverable through a later GET.
  The API must not claim rollback without evidence.
- GET/search/neighbor operations must not mutate record or schema state.
- Writes must not be automatically retried at the HTTP layer.
- Validation, not-found, conflict, capacity, busy, and internal failures remain
  distinguishable through stable problem codes in `ARC-CTR-002`.

## Verification and change control

| Claim | Verification | Evidence location |
|---|---|---|
| Layering prevents route SQL and domain framework coupling | Dependency/static analysis and architecture test | Future API initiative evidence |
| Request pipeline rejects malformed and unsafe input before mutation | Contract and negative integration tests | Required by `ARC-CTR-009` |
| Startup and readiness reflect actual store safety | Startup fault-injection tests | Future API/operations evidence |
| Error translation leaks no implementation details | Response/log snapshot tests | Future API evidence |
| Only one API replica owns a database and maintenance cannot overlap | Compose scale prohibition, competing-container/instance-lock tests | Future persistence/operations evidence |
| Image/runtime settings match container invariant | Image user/layer/SBOM and rendered/runtime config inspection | Future release evidence |

Changes require API owner review plus project architecture authority and must
reconcile every affected HTTP, persistence, client, operations, and conformance
record.

