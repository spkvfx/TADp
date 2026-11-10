# Record clients to API HTTP contract

**Architecture ID:** `ARC-CTR-002`  
**Status:** Accepted  
**Architecture revision:** `2.0.0`  
**Contract owner:** API component owner and project architecture authority  
**Producer:** Record API service  
**Consumers:** Python SDK, CLI through SDK, and browser adapter  
**Last reviewed:** 2026-11-10  

## Purpose and scope

This contract defines the v1 HTTP protocol for creating, retrieving, and
conditionally updating records, together with shared request/response headers
and problem semantics. Search/list/neighbor behavior is owned by
[`ARC-CTR-003`](14-search-navigation-contract.md); health and operator endpoints
are owned by [`ARC-CTR-008`](23-operations-security-contract.md).

## Protocol baseline

| Concern | Binding rule |
|---|---|
| Browser/public origin | Exactly `http://127.0.0.1:${RECORDS_HOST_PORT}` as published by Compose; no IPv6/wildcard/hostname alternate in v2 |
| Container-client base | `http://record-api:8000` on private `record-net`; never exposed as a browser origin |
| API base | `/api/v1` |
| Transport | HTTP/1.1 is required; HTTP/2 may be supported only without semantic change |
| Success media type | `application/json` encoded as UTF-8; response declares `application/json` |
| Problem media type | `application/problem+json` encoded as UTF-8 |
| Request body | JSON object only; unique member names; maximum 32 KiB encoded body |
| Schema behavior | Strict Pydantic v2 models; no scalar coercion; unknown input fields forbidden |
| Cache | Record/data responses include `Cache-Control: no-store`; clients do not persist them |
| Request correlation | Every response includes `X-Request-ID`; accepted client IDs follow `ARC-BND-002` |
| Server disclosure | No framework/server version header, stack trace, SQL, or filesystem path |

Both network bases append the identical `/api/v1` paths defined below. They
are two entrances to one router and contract, not separate APIs. A route,
method, representation, problem, or behavior available only to CLI/SDK or only
to web is nonconforming.

`Accept` absent or including `application/json`, `application/problem+json`, or
`*/*` is accepted as appropriate to the outcome. A request that explicitly
excludes the possible response representation receives `406`. A request body
must declare `Content-Type: application/json`; parameters other than
`charset=utf-8` are rejected. JSON numbers must not substitute for strings.

## Interface surface

| Operation | Method and path | Required input | Success result | Principal failure results |
|---|---|---|---|---|
| Create record | `POST /api/v1/records` | `RecordCreate` JSON; no `Idempotency-Key` | `201`, canonical `Record`, `Location`, strong `ETag` | `400/413/415/422`, `409 capacity_exceeded`, `503 store_busy/unavailable`, `500` |
| Retrieve record | `GET /api/v1/records/{id}` | Canonical UUID path | `200`, canonical `Record`, strong `ETag` | `400 invalid_id`, `404 record_not_found`, `503`, `500` |
| Update record | `PATCH /api/v1/records/{id}` | `RecordPatch` JSON and exactly one current strong `If-Match` | `200`, canonical `Record`, current/new strong `ETag` | `400/413/415/422`, `404`, `412 revision_conflict`, `428 precondition_required`, `503`, `500` |

No v1 `PUT`, `DELETE`, bulk-create, bulk-update, ID-allocation, or force-update
route exists. Unsupported methods return `405` with an accurate `Allow`
header and a problem body.

## Create contract

### Request

```http
POST /api/v1/records HTTP/1.1
Content-Type: application/json
Accept: application/json

{"name":"Example name","value":"Example value"}
```

- The body must contain exactly `name` and `value` before normalization.
- A caller-supplied `id`, null, missing field, or extra field is invalid.
- `Idempotency-Key` is not supported in v1. If present, the service returns
  `400` with `code: "idempotency_not_supported"` rather than imply a guarantee.
- The service validates both fields, checks capacity, generates identity, and
  commits one transaction.

### Success

```http
HTTP/1.1 201 Created
Location: /api/v1/records/9f3f6db2-39c7-4ce6-a570-7eaf32a2a95d
ETag: "rev-1"
Cache-Control: no-store
Content-Type: application/json
X-Request-ID: ...

{"id":"9f3f6db2-39c7-4ce6-a570-7eaf32a2a95d","name":"Example name","value":"Example value"}
```

The response is emitted only after commit. A connection loss before the caller
receives it creates an indeterminate outcome; clients must retrieve/reconcile
before choosing whether to create again. V1 does not deduplicate create calls.

## Retrieve contract

- `{id}` must already be the exact lowercase canonical UUID form. The API does
  not redirect or silently canonicalize uppercase, braces, URNs, or compact
  UUIDs.
- A syntactically invalid/noncanonical ID is `400 invalid_id`; a valid absent
  ID is `404 record_not_found`.
- Success returns the canonical record plus current strong ETag.
- Conditional GET is not part of v1. A supplied `If-None-Match` is ignored as
  an extension header and does not change the required `200` semantics.

## Update contract

### Preconditions

- `If-Match` is required and contains exactly one strong ETag returned for the
  same record. `*`, weak tags, lists, malformed tags, or tags for another
  representation are `400 invalid_precondition`; absence is `428`.
- The body contains `name`, `value`, or both. Null, no fields, `id`, or an
  unknown field is invalid.

### Execution

1. Validate/canonicalize path, ETag, and entire patch before starting a write.
2. In one transaction, find the record and compare expected revision.
3. If absent, return `404`. If revision differs, return `412` with no write.
4. Normalize fields and compare to stored canonical values.
5. If nothing changes, commit no mutation and return `200` with the same record
   and ETag.
6. Otherwise update only mutable fields, increment revision exactly once, set
   `updated_at`, commit, and return the new record/ETag.

There is no blind, last-write-wins, force, merge-patch, or server-side conflict
resolution endpoint.

## ETag contract

- The wire form is the quoted ASCII strong entity tag `"rev-{n}"`, where `n`
  is the positive decimal internal revision without leading zeroes.
- ETags are scoped to the identified record resource. Consumers must treat the
  entire string as opaque and must not infer update count or compare tags from
  different records.
- Creation begins at revision 1. A material update increments by one. A no-op
  update does not increment.
- Search page ETags are not defined. Individual records selected through a
  neighbor operation return their own ETag as specified by `ARC-CTR-003`.

## Problem document

Every non-`204` API error that reaches the HTTP boundary uses:

```json
{
  "type": "urn:example-records:problem:validation-failed",
  "title": "Request validation failed",
  "status": 422,
  "detail": "One or more request fields are invalid.",
  "instance": "/api/v1/records",
  "code": "validation_failed",
  "request_id": "...",
  "errors": [
    {"path":"/name","code":"too_short","message":"Name must not be empty."}
  ]
}
```

| Member | Rule |
|---|---|
| `type` | Stable URN `urn:example-records:problem:{kebab-code}`; never `about:blank` for defined errors |
| `title` | Stable human summary for the code, not data-dependent |
| `status` | Integer equal to HTTP status |
| `detail` | Safe human explanation; no raw record value/query, stack, SQL, or path |
| `instance` | Request path without query string |
| `code` | Stable snake-case machine code |
| `request_id` | Same value as response header |
| `errors` | Present only when field/query issues exist; ordered by input path then validation order |

Each `errors` item contains exactly `path` (JSON Pointer or parameter name),
`code`, and safe `message`. Clients may branch on `status` and `code`, not on
English text. Internal failures use a generic detail and log safe diagnostics
under the request ID.

## Stable problem codes

| HTTP | Code | Meaning and required state effect |
|---:|---|---|
| 400 | `invalid_request` | Malformed protocol input not covered below; no application execution |
| 400 | `invalid_json` | Invalid UTF-8/JSON, duplicate keys, or non-object body; no execution |
| 400 | `invalid_id` | Noncanonical record ID; no repository query required |
| 400 | `invalid_precondition` | Unsupported/malformed `If-Match`; no write |
| 400 | `idempotency_not_supported` | `Idempotency-Key` supplied; no write |
| 400 | `invalid_search` / `invalid_regex` / `cursor_invalid` | Query contract failure; no partial result |
| 403 | `origin_forbidden` | Browser Origin is present but not the configured same origin; body/command not processed |
| 404 | `record_not_found` | Canonical ID has no record |
| 405 | `method_not_allowed` | Path exists but method is outside contract |
| 406 | `not_acceptable` | Accepted response media type excluded |
| 409 | `capacity_exceeded` | Record cap prevents create; existing data unchanged |
| 409 | `context_mismatch` | Current record does not belong to requested navigation context |
| 412 | `revision_conflict` | ETag no longer current; record unchanged by request |
| 413 | `payload_too_large` | Encoded body exceeds 32 KiB; body not processed |
| 415 | `unsupported_media_type` | Required JSON media type absent/invalid |
| 422 | `validation_failed` | Well-formed model/domain value invalid; no write |
| 428 | `precondition_required` | PATCH lacks `If-Match`; no write |
| 503 | `store_busy` | Busy timeout reached; operation rolled back/no result claim |
| 503 | `store_unavailable` | Store/readiness unsafe; no success claim |
| 503 | `search_budget_exceeded` | Complete search could not finish within budget; no partial page |
| 503 | `overloaded` | Admission limit exceeded; application command/query not executed |
| 500 | `internal_error` | Unclassified server failure; no details leaked |

Rate limiting is not an API v1 feature; `429` is not emitted by the application.
A future proxy may add it only under revised deployment architecture; v2 has
no proxy container.

## Contract rules

| Concern | Rule | Owner |
|---|---|---|
| Authentication/authorization | None at app layer; exact public/internal Host allowlist, exact browser Origin, private Compose network, and loopback-only Docker publication are mandatory | API/operations |
| Validation/idempotency | Strict validation; create non-idempotent; GET safe; PATCH conditional and no-op-aware | API service |
| Timeouts/retries | Server bounds processing; clients may retry qualifying GETs only; writes never auto-retried | API and client contracts |
| Ordering | Not applicable to single-resource operations | Search contract |
| Versioning | `/api/v1` and `ADR-006`; breaking shape/meaning requires new major path | Architecture authority |
| Observability/audit | Request ID and safe structured outcome; no audit history claim | API operations |

## Compatibility and verification

Within `/api/v1`, adding an optional response member is permitted only after
SDK/browser decoders are explicitly defined to ignore it for that object.
Record objects remain closed and cannot gain a field in v1. New optional
request fields are breaking because requests reject unknown fields. Problem
codes may be added for a genuinely new failure only with synchronized clients.

| Verification | Scenario | Evidence location |
|---|---|---|
| HTTP contract tests | Every operation, media/header rule, status, ETag, and problem code | `ARC-CTR-009`; future API evidence |
| Consumer-driven tests | SDK and browser fixtures decode all accepted results/problems | Future SDK/web evidence |
| Fault tests | Rollback, disconnect, busy, capacity, and internal error | Future API/persistence evidence |
| Negative inventory | Unsupported mutation routes/methods absent | Future API evidence |

## Related records

- System boundary: [`ARC-BND-002`](12-api-service-boundary.md)
- Decisions: [`ADR-001`](04-ADR-001-api-exclusive-persistence.md), [`ADR-002`](05-ADR-002-identity-order-and-concurrency.md)
- Governing evidence: [`AUTH-EX-001`](01-accepted-architecture-baseline.md)

