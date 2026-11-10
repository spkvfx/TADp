# Python consumers to record SDK contract

**Architecture ID:** `ARC-CTR-005`  
**Status:** Accepted  
**Architecture revision:** `2.0.0`  
**Contract owner:** SDK component owner and project architecture authority  
**Producer:** `example-records-sdk` distribution  
**Consumers:** `record-cli` image and supported containerized Python integrators  
**Last reviewed:** 2026-11-10  

## Purpose and scope

This contract defines the public synchronous Python SDK: imports, immutable
models, client construction/lifecycle, methods, exceptions, retries,
observability, and compatibility. It wraps the accepted HTTP API; it does not
add domain operations, local persistence, client-side search, or an async API.
The wheel is built, tested, and consumed inside declared OCI build/runtime
images. This contract does not establish a host Python installation path.

## Public namespace

The package `example_records_sdk` exports exactly these v1 public symbols
(module locations may be documented, but root re-exports own compatibility):

```text
RecordClient
Record
VersionedRecord
RecordPatch
RecordField
MatchMode
SearchSpec
RecordPage
Direction
Boundary
NeighborResult
ProblemIssue
RecordSdkError
ClientValidationError
ApiProblemError
InvalidSearchError
RecordNotFoundError
RevisionConflictError
CapacityExceededError
ServiceUnavailableError
IndeterminateWriteError
ProtocolError
```

HTTPX/Pydantic classes, generated schema internals, transport helpers, and
symbols beginning with `_` are not public. The package version is available
through standard distribution metadata, not a mutable module global contract.

## Public models

All public data models are Pydantic v2 models configured `frozen=True`, strict
input types, and `extra='forbid'`. Enum values are lowercase wire tokens.

| Model | Fields and rules |
|---|---|
| `Record` | `id: UUID` serialized canonically, `name: str`, `value: str`; represents canonical API data |
| `VersionedRecord` | `record: Record`, `etag: str`, `request_id: str`; ETag is opaque and nonempty |
| `RecordPatch` | `name` and `value` presence-aware; at least one; no `id`/null; applies domain client validation |
| `RecordField` | Enum `id`, `name`, `value` |
| `MatchMode` | Enum `exact`, `starts_with`, `ends_with`, `contains`, `regex` |
| `SearchSpec` | `field: RecordField`, `mode: MatchMode`, `query: str`; validates accepted query limits without claiming server acceptance |
| `RecordPage` | immutable tuple of `Record`, `next_cursor: str | None`, `snapshot_ceiling: int`, `request_id: str` |
| `Direction` | Enum `next`, `previous` |
| `Boundary` | Enum `start`, `end` |
| `NeighborResult` | exactly one of `record: VersionedRecord` or `boundary: Boundary`, plus `snapshot_ceiling` |
| `ProblemIssue` | `path`, `code`, `message` strings from a validated problem document |

SDK input validation mirrors `ARC-CTR-001`/`003` for early feedback. Server
responses are decoded strictly and must already be canonical. A response that
would need SDK normalization/coercion is a `ProtocolError`.

## Client construction and lifecycle

Normative constructor shape:

```python
RecordClient(
    base_url: str,
    *,
    timeout: float = 5.0,
    transport: httpx.BaseTransport | None = None,
    user_agent_suffix: str | None = None,
) -> RecordClient
```

- `base_url` must be absolute `http`, contain no credentials/query/fragment,
  and normalize without a trailing slash. In the supported topology it is
  exactly `http://record-api:8000` for Compose-network consumers. Loopback,
  `localhost`, host-gateway names, arbitrary hostnames, container IPs,
  nonloopback host addresses, and HTTPS are rejected in v2. Injected mock
  transports retain this canonical base without creating another live origin.
- `timeout` is finite and within `0.1..60.0` seconds; one value applies as the
  total SDK request policy while HTTPX phase values are derived internally.
- Injected transport exists for tests/approved embedding and does not change
  URL or contract validation.
- The client owns one HTTPX synchronous client/connection pool, is a context
  manager, and has idempotent `close()`. Calls after close fail locally.
- Thread sharing is not promised. One client may be used sequentially; callers
  use separate instances for concurrent threads unless a later release
  documents evidence-backed safety.
- Construction/import makes no network call. The first explicit method call is
  the first possible network interaction.

## Public method surface

```python
create_record(*, name: str, value: str) -> VersionedRecord
get_record(record_id: UUID | str) -> VersionedRecord
update_record(
    record_id: UUID | str,
    patch: RecordPatch,
    *,
    expected_etag: str,
) -> VersionedRecord
search_page(
    spec: SearchSpec | None = None,
    *,
    limit: int = 25,
    cursor: str | None = None,
) -> RecordPage
iter_records(
    spec: SearchSpec | None = None,
    *,
    page_size: int = 25,
    max_pages: int | None = None,
) -> Iterator[Record]
neighbor(
    record_id: UUID | str,
    direction: Direction,
    *,
    spec: SearchSpec | None = None,
    snapshot_ceiling: int | None = None,
) -> NeighborResult
```

- IDs supplied as strings must already be canonical; the SDK rejects alternate
  text rather than silently change the request.
- `iter_records` starts one context and follows server cursors unchanged. It
  yields lazily, stops at null cursor/max pages, detects repeated cursors, and
  never preloads the full collection. `max_pages` must be positive if present.
- A new `iter_records` invocation observes a new snapshot ceiling.
- `update_record` accepts only a previously returned strong ETag. It sends one
  PATCH and never refetches/retries/resolves a conflict automatically.
- No `delete`, raw request, SQL, force update, ID allocation, arbitrary route,
  async, or automatic service-start method is public.

## Request and retry policy

| Operation | Automatic retry | Rule |
|---|---:|---|
| `get_record`, `search_page`, `neighbor` | At most 2 retries (3 attempts total) | Only connect failure before response, connect timeout, or HTTP `502/503/504` with no application problem proving a domain outcome |
| Cursor calls through `iter_records` | Same per-GET policy | Reuse identical request/cursor; detect repetition |
| `create_record` | Never | Any connection loss after dispatch can be indeterminate |
| `update_record` | Never | Conditional semantics do not make transport replay an SDK guarantee |

Read retry delays are 100 ms then 250 ms plus deterministic bounded jitter
from an injectable test clock/random source. Respect `Retry-After` only when it
is a valid delta of 0-5 seconds, bounded by remaining timeout; otherwise use
SDK delay. Total attempts remain within the caller's timeout budget.

The SDK sends `Accept: application/json, application/problem+json`, its stable
User-Agent, and a valid generated `X-Request-ID` per attempt chain. Retried
attempts retain the logical request ID and add no nonstandard server contract.

## Exception contract

All public exceptions derive from `RecordSdkError`. Exception attributes are
immutable, safe to display, and never include full `value` or raw search query.

| Exception | Trigger | Stable attributes |
|---|---|---|
| `ClientValidationError` | Constructor/method/model input invalid before HTTP | safe issues; no HTTP status/request ID required |
| `InvalidSearchError` | API `invalid_search`, `invalid_regex`, or `cursor_invalid` | status, code, safe issues, request ID |
| `RecordNotFoundError` | `record_not_found` | record ID, status, request ID |
| `RevisionConflictError` | `revision_conflict` | record ID, expected ETag, status, request ID; no server record body unless contract later adds it |
| `CapacityExceededError` | `capacity_exceeded` | status, request ID |
| `ServiceUnavailableError` | Exhausted safe-read transport retries or typed store/search unavailable result | safe reason category, last request ID/status when known |
| `IndeterminateWriteError` | POST/PATCH dispatched but outcome cannot be proven because response was lost/malformed | operation, record ID for update, request ID; explicit reconcile guidance |
| `ApiProblemError` | Valid problem not mapped to a narrower public type | status, code, title, safe detail/issues, request ID |
| `ProtocolError` | Malformed/nonconforming HTTP success/problem/header/media response | safe category, status/request ID when known |

Unexpected 4xx/5xx valid problems map to `ApiProblemError`. Non-problem error
bodies or success with missing/invalid ETag become `ProtocolError`. Raw HTTPX
exceptions may be chained as causes but are not the required public branch.

## Contract rules

| Concern | Rule | Owner |
|---|---|---|
| Authentication | None in local v1; SDK accepts no token/credential parameters | SDK/architecture |
| Deployment | Supported consumers run in declared containers; service discovery uses `record-api:8000`; no host SDK/CLI installation | Platform/SDK |
| Validation/idempotency | Strict local mirror; server authoritative; no write retry | SDK |
| Ordering/timeouts/retries | Preserve API order/cursor; bounded safe-read retries only | SDK |
| Versioning | Semantic package versions; public exports/signatures/models/exceptions are compatibility surface | SDK release owner |
| Observability | Optional standard-library logger/hooks emit safe method/route/status/timing/request ID only | SDK |

## Compatibility and verification

Patch versions may fix implementation/docs without public semantic change.
Minor versions may add optional methods/symbols while existing behavior remains
identical. Removing/renaming symbols, changing signatures/defaults/model
acceptance/exception mapping/retry behavior, or supporting a new incompatible
API requires a major SDK version.

| Verification | Scenario | Evidence location |
|---|---|---|
| Public API/type snapshot | Imports, signatures, models, enums, exception inheritance | Future SDK evidence |
| Mock transport matrix | Every accepted HTTP result/problem/malformed response/retry branch | [`ARC-CTR-009`](24-conformance-contract.md) |
| Live conformance | SDK results equal direct API results for all vectors | Future API+SDK evidence |
| Packaging | Same hashed wheel built once, installed/imported/used across supported pinned Linux container matrix with no server/SQLite deps | Future SDK release evidence |
| Topology | CLI/test consumers reach `record-api:8000` only on private `record-net`; rejected URL forms fail before transport | Future container conformance evidence |
| Clean host | Build, test, CLI use, and SDK example execute through Docker/Compose without host Python/pip/pipx | Required by `ARC-CTR-009` |

## Related records

- System boundary: [`ARC-BND-004`](17-python-sdk-boundary.md)
- Decisions: [`ADR-001`](04-ADR-001-api-exclusive-persistence.md), [`ADR-005`](08-ADR-005-containerized-technology-stack.md), [`ADR-006`](09-ADR-006-contract-versioning-and-feedback.md)
- Governing evidence: [`AUTH-EX-001`](01-accepted-architecture-baseline.md)
- Superseded native deployment baseline: [`ARC-REV-001`](revisions/1.0.0/00-superseded-native-runtime-deployment-baseline.md)

## Revision record

| Date | Change | Authority |
|---|---|---|
| 2026-11-10 | Defined SDK v1 public surface, lifecycle, retry, and exception semantics | User-authorized best-judgment architecture completion |
| 2026-11-10 | Bound supported SDK consumption and package verification to declared containers and private Compose discovery | User's explicit full-Dockerization/no-host-services instruction |

