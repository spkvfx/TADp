# API and SQLite runtime image proposal

**Initiative:** API and SQLite runtime image

**Proposal status:** Draft

**Revision:** 0.1

**Last updated:** 2026-11-11

**Owner:** User

**Initiative type:** `implementation`

**Work version:** `v2.1`

**Realization suite:** [`RZN-001-P2-API-SQLITE-SUITE`](../../../../evidence/non-authoritative/realizations/v2.1/00-RZN-001-P2-API-SQLITE-suite-index.md)

**Type requirements:** See [the initiative skeleton](../README.md).

## Executive proposal

Create one D3 runtime image implementing the record-domain, `/api/v1`,
search/navigation, SQLite persistence, migration, maintenance, health, and
static-hosting slot defined by the authoritative architecture. This proposal
selects no repository destination, dependency patch, image digest, or test
tool; those choices remain open.

## Initiative type and permitted output

This is an implementation initiative. Its eventual output may be source,
container artifacts, migration and maintenance tooling, and verification
records for D3 only. A proposal is not authorization to implement, qualify,
release, or deploy any product.

## Problem and evidence

The authoritative contracts specify observable D3 behavior but the example has
no governed D3 initiative or implementation. The non-authoritative v2.1 suite
organizes useful planning detail while remaining unable to create requirements
or prove conformance.

## Intended outcomes

- One immutable API/SQLite runtime image with a traceable build identity.
- Contract-faithful domain, HTTP, search, navigation, and persistence behavior.
- Deterministic migration, backup, restore, maintenance, and health behavior.
- Evidence for applicable DOM, HTTP, SRCH, NAV, DB, CNT, OPS, and E2E vectors.
- A stable D3 interface for separately governed D4, D5, and D6 consumers.

## Scope

### Included

- Record-domain and API behavior under `/api/v1`.
- SQLite schema, migrations, constraints, backup, restore, and maintenance.
- Search, pagination, hierarchy navigation, error envelopes, and concurrency.
- Health/readiness behavior and the same-origin static-hosting slot.
- D3 security, failure, observability, compatibility, and verification work.

### Excluded

- D2 Compose-platform qualification.
- D4 SDK, D5 CLI, and D6 browser implementation or completion.
- Remote, multi-user, production, or regulated deployment.
- Actual or possible ePHI; only synthetic or documented de-identified data.
- Any claim that this proposal is accepted, delivered, conformant, or released.

## Users and stakeholders

The owner governs decisions and lifecycle. Implementers build the D3 image;
reviewers assess contract, security, data, and operational evidence; later
initiatives consume only declared compatible API behavior.

## Terms

- **D3:** the API and SQLite artifact family defined by ADR-007.
- **Runtime image:** the immutable container artifact serving API and health.
- **Maintenance operation:** an explicit migration, backup, restore, or check.
- **Static-hosting slot:** the D3-owned same-origin serving boundary later used
  by D6; it does not include the web bundle itself.

## Proposed direction

### Product behavior or placement

Keep one D3 artifact/completion boundary. Exact source, product, evidence, and
release paths remain subject to `API-01`.

### Domain and authority model

Implement authoritative record identity, timestamps, validation, hierarchy,
query, conflict, problem, and persistence semantics without treating generated
OpenAPI or realization notes as authority.

### System boundaries

Run inside the D2 topology, bind only through its declared interfaces, store
durable state only in the D3 SQLite volume, and expose no host-only runtime
prerequisite beyond the project profile.

### Primary workflows

Build and attest the image; initialize or migrate a database; serve API,
search, navigation, health, and eligible static content; perform maintenance;
exercise backup/restore; and qualify clean-install and upgrade paths.

### Data and lifecycle

Use synthetic or documented de-identified fixtures. Preserve schema identity,
migration ordering, transaction semantics, timestamp rules, retention
boundaries, and recoverability defined by authoritative contracts.

## Operational behavior

### Failure and recovery

Failures must be bounded and observable: invalid requests, conflicts,
deadlines, locked/corrupt databases, interrupted migrations, unavailable
volumes, and failed restore checks cannot silently become success.

### Security and authorization

Preserve local single-user, private/loopback, non-production use. Apply input,
path, query, output, dependency, secret, logging, and image safeguards. Any
ePHI indication blocks affected work and routes to the governing policy.

### Observability

Emit bounded health, maintenance, migration, and request evidence without
record payloads, secrets, host paths, or unbounded sensitive values.

## Compatibility and transition

D3 depends on a compatible D2 platform claim, while D4-D6 are separate
consumers. Compatibility matrices and retirement rules must be explicit; no
dependency aggregates initiative lifecycle or completion.

## Alternatives considered

- Multiple D3 initiatives: rejected for now because the suite presents one
  cohesive artifact and completion boundary; `API-06` keeps split triggers open.
- Direct host execution: outside the container-only project boundary.
- Treating realization notes as requirements: prohibited by evidence standing.
- Combining SDK, CLI, or web work: conflicts with ADR-007 decomposition.

## Risks and tradeoffs

Key risks are semantic drift, unsafe query construction, migration damage,
mutable dependencies, weak fault injection, leaking data in logs or fixtures,
and overclaiming downstream compatibility. Gates must block unsupported claims.

## Assumptions requiring assumption

Initial assumptions concern the single D3 boundary, authoritative ownership,
D2 dependency, D4-D6 consumer separation, synthetic/de-identified data, and
blocking behavior for missing security or recovery evidence. Stage 3 records
these as unconfirmed assumptions.

## Questions requiring decisions

- `API-01`: exact source, product, migration, maintenance, static, and evidence paths.
- `API-02`: dependency patches, image identities, SQLite build, and RE2 wheel.
- `API-03`: test seams for clocks, UUIDs, faults, deadlines, and network loss.
- `API-04`: contract fixtures and OpenAPI drift evidence handling.
- `API-05`: D3 security, risk, activity-review, incident, and recovery owner.
- `API-06`: whether a mandatory split trigger exists within the D3 boundary.

All remain open.

## Acceptance outcomes

A later human review may evaluate whether the specification is complete,
traceable, narrow, testable, and safe to advance. Product acceptance,
conformance, and completion require their own later workflow and evidence.

## References

- [Authoritative architecture suite](../../../../evidence/authoritative/architecture/00-architecture-suite-index.md)
- [ADR-007 decomposition](../../../../evidence/authoritative/architecture/10-ADR-007-product-and-delivery-decomposition.md)
- [Record-domain contract](../../../../evidence/authoritative/architecture/11-record-domain-contract.md)
- [SQLite persistence contract](../../../../evidence/authoritative/architecture/16-sqlite-persistence-contract.md)
- [Operations/security contract](../../../../evidence/authoritative/architecture/23-operations-security-contract.md)
- [Conformance contract](../../../../evidence/authoritative/architecture/24-conformance-contract.md)
- [NIST security suite](../../../../evidence/authoritative/security/NIST/00-nist-security-policy-suite-index.md)
- [HIPAA-aligned suite](../../../../evidence/authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md)
- [v2.1 realization suite](../../../../evidence/non-authoritative/realizations/v2.1/00-RZN-001-P2-API-SQLITE-suite-index.md)

## Revision history

| Revision | Date | Change | Authority |
|---|---|---|---|
| 0.1 | 2026-11-11 | Initial D3 proposal; all implementation choices remain open | User prompt and cited evidence |

