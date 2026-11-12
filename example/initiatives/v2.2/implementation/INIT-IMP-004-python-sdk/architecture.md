# Python SDK artifact architecture and specification

**Initiative:** `INIT-IMP-004`
**Status:** Proposed
**Last updated:** 2026-11-11

## Proposal standing

This specification elaborates the frozen proposal without resolving open
choices or changing source authority.

## Specification boundary

Specify one D4 wheel, public API, private transport, packaging, compatibility,
and evidence. Do not specify the server, CLI, platform, or web application.

## Current repository baseline

No governed D4 source or wheel exists at the captured base.

## Goals and non-goals

### Goals

- Preserve authoritative SDK and API semantics in strict public types.
- Keep transport private, URL handling safe, and exceptions predictable.
- Retry only eligible reads and never automatically retry writes.
- Produce mock/live, typing, docs, security, and compatibility evidence.

### Non-goals

- Select paths, dependency patches, tools, seams, owners, or split outcomes.
- Implement server state, SQLite access, CLI behavior, or production operation.
- Treat generated clients, schemas, or realization notes as authority.

## Terms and identity

Wheel/version, public symbol, model, method, exception, request, response,
problem, compatibility entry, and evidence artifact require stable identities.

## Architectural decisions

No initiative-local decision is final. Authoritative evidence binds behavior;
`SDK-01` through `SDK-06` retain all implementation choices.

## Boundaries and ownership

D4 owns the public wheel, models, methods, exceptions, validation, transport
policy, packaging, docs/examples, and evidence. D3 owns HTTP behavior; D5 owns
CLI interaction; D2 owns build/runtime targets.

## Domain model and evidence/authoritative

### Model

Expose immutable record/query/navigation models and stable problem/exception
mapping without leaking transport implementation.

### Binding requirements

Strict validation, typing, URL safety, timeout/cancellation behavior, resource
cleanup, pagination/search meaning, and retry restrictions cannot be weakened.

## State and persistence

Client state is bounded configuration and in-flight data. No durable SDK
database exists. Credentials and record content are not retained in logs or
evidence.

## Primary workflows

### Build and qualify

Resolve locked inputs, build wheel reproducibly, inspect metadata/content,
type-check/docs-check, scan, test mock contracts, then test a compatible live D3.

### Operate and upgrade

Construct/close client, validate base URL and inputs, invoke reads/writes,
map problems, paginate/search/navigate, handle timeout/cancellation, and
evaluate compatibility before wheel replacement.

## Interfaces and integration

Only documented public symbols are supported. Transport adapters and fault
seams remain private. No consumer imports internal modules or accesses SQLite.

## Failure and recovery

Invalid configuration/input, unsafe URLs, timeout, cancellation, connection
loss, malformed response, unknown problem, retry exhaustion, and cleanup
failure are bounded and mapped predictably. Writes are never auto-retried.

## Security and authorization

Validate URLs/redirects, protect credentials, lock and scan dependencies, avoid
secret or payload leakage, bound diagnostics, and preserve local single-user
non-production use with synthetic/de-identified evidence.

## Observability and operations

Provide safe diagnostic hooks and test evidence without exposing credentials,
record payloads, private transport internals, or high-cardinality data.

## Compatibility migration and rollout

Declare exact Python/platform/D3 matrices, public-surface compatibility, and
retirement rules. Compare public typing and docs; qualify old/new compatible
D3 behavior before release disposition.

## Testing strategy

Run SDK-001 through SDK-008 plus applicable DOM/HTTP/SRCH/NAV/E2E vectors;
strict-model, URL, timeout, cancellation, retry, exception, cleanup, typing,
docs, wheel-reproducibility, mock/live, and compatibility-diff checks.

## Risks and edge cases

Permissive coercion, public drift, unsafe redirects, write duplication, stale
fixtures, resource leaks, dependency compromise, error leakage, and overly
broad compatibility claims block affected gates.

## Deferred work

Destinations, patches/matrix, tools, private seams, owner, and split remain
open under `SDK-01` through `SDK-06`. “Open work” is not a lifecycle state.

## Architecture and specification acceptance

Not sought. Later explicit human authority is required, separate from product
acceptance, conformance, release, or completion.
