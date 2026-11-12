# Python SDK artifact proposal

**Initiative:** Python SDK artifact

**Proposal status:** Draft

**Revision:** 0.1

**Last updated:** 2026-11-11

**Owner:** User

**Initiative type:** `implementation`

**Work version:** `v2.2`

**Realization suite:** [`RZN-001-P2-SDK-SUITE`](../../../../../evidence/non-authoritative/realizations/v2.2/00-RZN-001-P2-SDK-suite-index.md)

**Type requirements:** See [the initiative skeleton](../README.md).

## Executive proposal

Create one immutable Python wheel implementing the authoritative D4 client
contract against a compatible D3 `/api/v1`. The SDK exposes strict immutable
models, documented methods, stable exceptions, private transport details, and
bounded retry behavior. Exact paths, dependency patches, tools, and owners
remain open.

## Initiative type and permitted output

This implementation initiative may eventually deliver Python source, one wheel,
metadata, docs/examples, and D4 verification evidence. It cannot deliver the
API server, SQLite access, CLI image, platform, or web application.

## Problem and evidence

The authoritative SDK contracts define behavior but the example has no
governed D4 artifact. The v2.2 realization suite provides planning detail only
and cannot create requirements, acceptance, or conformance.

## Intended outcomes

- One immutable, typed Python wheel with a traceable identity.
- Strict models, documented public methods, and stable exception mapping.
- Private validated transport with no direct SQLite or server implementation.
- Retry only where authoritative idempotency permits; never retry writes.
- SDK-001 through SDK-008 and applicable domain/HTTP/search/navigation/E2E evidence.

## Scope

### Included

Public SDK models, client methods, exceptions, validation, transport behavior,
typing/docs/examples, packaging, compatibility, and D4 evidence.

### Excluded

D2 platform qualification, D3 implementation, D5 CLI behavior, D6 web behavior,
host installation as a runtime prerequisite, direct SQLite access, remote
production deployment, and actual or possible ePHI.

## Users and stakeholders

Application developers consume the public wheel. D5 later consumes only that
public surface. The owner and reviewers govern lifecycle, contract, security,
compatibility, and evidence.

## Terms

- **D4:** the Python SDK artifact family defined by ADR-007.
- **Public surface:** documented models, methods, exceptions, and typing.
- **Private transport:** implementation details that consumers may not import.
- **Compatible D3:** an exact API artifact/matrix entry, not a broad version claim.

## Proposed direction

### Product behavior or placement

Publish one wheel and associated metadata. Exact repository, artifact, docs,
examples, and evidence destinations remain open under `SDK-01`.

### Domain and authority model

Mirror authoritative domain and HTTP meaning without inventing server state.
Models are strict and immutable; generated schema is supporting evidence only.

### System boundaries

Build and test through D2, execute against mock fixtures and a compatible live
D3 API, validate base URLs, and expose no direct database or container internals.

### Primary workflows

Construct a client, validate inputs and URL, invoke public read/write methods,
map problems to stable exceptions, paginate/search/navigate, close resources,
and verify compatible mock/live behavior.

### Data and lifecycle

Hold only request/response data needed in memory; create no durable client data
store. Fixtures must be synthetic or documented de-identified.

## Operational behavior

### Failure and recovery

Bound timeouts, cancellation, connection loss, malformed responses, problem
mapping, retry exhaustion, and cleanup. Read retries require safe policy;
writes are never automatically retried.

### Security and authorization

Validate schemes/hosts/paths, prevent unsafe redirects and secret leakage,
lock dependencies, scan artifacts, keep logs bounded, and preserve local
single-user non-production constraints.

### Observability

Expose diagnostics suitable for tests and support without record payloads,
credentials, unsafe URLs, host paths, or unbounded values.

## Compatibility and transition

D4 depends on exact D2 build/test interfaces and compatible D3 behavior. D5 is
a separate consumer. Public compatibility and retirement policy must be
explicit and artifact-bound.

## Alternatives considered

Multiple packages, generated clients, direct HTTP use, direct SQLite use, and
combining D5 were considered. One hand-governed wheel best preserves the D4
contract; `SDK-06` keeps evidence-based split triggers open.

## Risks and tradeoffs

Risks include public-surface drift, permissive models, unsafe URL handling,
write retries, stale generated code, dependency vulnerabilities, leaky errors,
and compatibility overclaims.

## Assumptions requiring assumption

Initial assumptions cover one D4 wheel boundary, authoritative ownership,
D2/D3 dependencies, D5 separation, strict public behavior, safe data use, and
blocking evidence gaps. Stage 3 records them as unconfirmed.

## Questions requiring decisions

- `SDK-01`: exact source, wheel, metadata, docs, examples, and evidence paths.
- `SDK-02`: dependency patches and supported Python/platform image matrix.
- `SDK-03`: typing, documentation, and compatibility-diff tools.
- `SDK-04`: private fault, clock, randomness, and transport injection.
- `SDK-05`: security/risk/vulnerability/release and compatibility owner.
- `SDK-06`: whether docs or adapters require an independent split.

All remain open.

## Acceptance outcomes

A later human review may assess whether the D4 specification is complete,
narrow, traceable, safe, and testable. Delivery and conformance require
separate later authority and artifact-specific evidence.

## References

- [Architecture suite](../../../../../evidence/authoritative/architecture/00-architecture-suite-index.md)
- [ADR-007 decomposition](../../../../../evidence/authoritative/architecture/10-ADR-007-product-and-delivery-decomposition.md)
- [SDK boundary](../../../../../evidence/authoritative/architecture/17-python-sdk-boundary.md)
- [SDK contract](../../../../../evidence/authoritative/architecture/18-python-sdk-contract.md)
- [Operations/security](../../../../../evidence/authoritative/architecture/23-operations-security-contract.md)
- [Conformance](../../../../../evidence/authoritative/architecture/24-conformance-contract.md)
- [NIST suite](../../../../../evidence/authoritative/security/NIST/00-nist-security-policy-suite-index.md)
- [HIPAA-aligned suite](../../../../../evidence/authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md)
- [v2.2 suite](../../../../../evidence/non-authoritative/realizations/v2.2/00-RZN-001-P2-SDK-suite-index.md)

## Revision history

| Revision | Date | Change | Authority |
|---|---|---|---|
| 0.1 | 2026-11-11 | Initial D4 proposal; all implementation choices remain open | User prompt and cited evidence |
