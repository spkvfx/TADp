# Product 4 web application realization suite

**Suite ID:** `RZN-001-P4-WEB-SUITE`  
**Suite version:** `v4.0`  
**Status:** Recorded; non-authoritative proposal input  
**Recorded by:** Codex on behalf of the User  
**Recorded date:** 2026-11-10  
**Source realization:** [`RZN-001`](../v0.0/RZN-001-example-record-application.md)  
**Historical product label:** `RZN-001-P4-WEB`  
**Accepted delivery-unit alignment:** `D6 Web application bundle`  
**Intended future initiative boundary:** One D6 web-application-bundle initiative  
**Related initiative or proposal:** None created, as explicitly instructed  

> **Evidence standing:** This suite records a bounded browser-product
> opportunity. It is not a UI specification, accepted initiative, implemented
> bundle, accessibility result, security assessment, release, or completion
> claim.

## Purpose

This suite narrows Product 4 to the accessible, container-built browser bundle
accepted by architecture `2.0.1`. The bundle would be embedded in a compatible
API image, served only from the Docker-published IPv4 loopback origin, and use
the same `/api/v1` contract as the CLI/SDK path without owning persistence or
server semantics.

## Version, suite, and future-initiative rule

`v4.0` is one directory, one realization suite, and one intended future D6
initiative boundary. Multiple notes may belong here only when they retain the
same browser-bundle outcome, authority, owner, product destination family,
verification claim, and lifecycle. Browser interaction, accessibility,
client security, and embedded bundle identity remain together because they
support one reviewable web-bundle outcome. Any independently acceptable new
outcome requires a new dot-version directory and separate future initiative
boundary.

## Authoritative baseline

| Evidence | Standing and use |
|---|---|
| [Codex invariant suite](../../../authoritative/LLM/00_Codex_Invariant_Suite_Index.md) | Governs realization standing, source authority, narrow scope, decisions, and status. |
| [`ARC-SUITE-001@2.0.1`](../../../authoritative/architecture/00-architecture-suite-index.md) | Owns the shared record, API, search, deployment, and evidence meanings. |
| [`ARC-BND-006`](../../../authoritative/architecture/21-web-application-boundary.md) | Owns browser state, same-origin delivery, storage exclusions, and supported-browser boundary. |
| [`ARC-CTR-007`](../../../authoritative/architecture/22-web-interaction-contract.md) | Owns routes, UI flows, validation, conflicts, races, accessibility, and browser security. |
| [`ADR-007`](../../../authoritative/architecture/10-ADR-007-product-and-delivery-decomposition.md) | Owns D6 dependencies and the delivery-after-D5 sequence. |
| [`ARC-CTR-009`](../../../authoritative/architecture/24-conformance-contract.md) | Owns web, accessibility, security, container, and end-to-end vectors and records no current D6 evidence. |
| [`SEC-NIST-SUITE-001@1.0.1`](../../../authoritative/security/NIST/00-nist-security-policy-suite-index.md) | Governs browser boundary, safe handling, assurance, supply chain, and claim limits. |
| [`SEC-HIPAA-SUITE-001@1.0.1`](../../../authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md) | Governs allowed data, minimum presentation, browser storage, inherited controls, evidence, and successor triggers. |

## Document catalog

| Order | Realization ID | Suite version | Same future-initiative scope |
|---:|---|---|---|
| `00` | `RZN-001-P4-WEB-SUITE` | `v4.0` | This standing, lineage, authority, dependency, and navigation index |
| `01` | `RZN-001-P4-WEB-N01` | `v4.0` | The D6 accessible browser interaction, in-memory state, same-origin security, embedded bundle, compatibility, and exact evidence boundary |

## Dependency and sequence

D6 technically depends on compatible D1-D3 artifacts from `v1.0`, `v2.0`, and
`v2.1`. Its delivery follows the `v3.0` D5 CLI suite under the accepted
User-requested sequence.
The web bundle is copied into the D3 API image, but D6 has its own version,
hash, browser/accessibility evidence, and completion boundary. Neither product
may use embedding to claim the other's completion.

## Suite-wide boundary

- The browser uses only the exact loopback same origin and shared `/api/v1`.
- Record state remains in memory; no cookie, service worker, localStorage,
  sessionStorage, IndexedDB, telemetry, third-party content, cross-origin API,
  or client-side persistence is a candidate capability.
- No direct database, Python SDK, separate web server/container, host Node
  service, CDN, proxy, or remote-use path is included.
- The data profile is non-production synthetic or externally documented
  de-identified data that also satisfies the NIST restrictions; possible ePHI
  or an expanded boundary triggers successor work.
- No initiative, implementation, accessibility pass, security result, or
  release claim is created.

## Handoff rule

A future proposal must cite `RZN-001-P4-WEB-N01`, name the compatible D2/D3
artifact identities and D5 sequencing evidence, map all applicable web and
security gates, and keep the acceptance claim limited to D6. This suite creates
no initiative.

## Correlation migration addendum

**Effective date:** 2026-11-11

**Migration action:** `Migrate`

**Authority:** [six-initiative migration prompt](../../../../prompts/create-v1.0-through-v4.0-initiatives.md), [EX-GIT-DR-001](../../../../initiatives/decision-receipts/EX-GIT-DR-001-enclosing-worktree-exception.md), and [resolved `INV-CONFLICT-001`](../../../authoritative/LLM/03_Codex_Invariant_Conflict_Register.md#inv-conflict-001--embedded-example-project-root-and-git-root-invariant)

This addendum applies current correlation governance without rewriting the
pre-effective suite's header, source identity, standing, or recorded claims.

| Correlation field | Migrated identity |
|---|---|
| Work version | `v4.0` |
| Realization suite | `RZN-001-P4-WEB-SUITE` at this path |
| Initiative | [`INIT-IMP-006` — Web application bundle](../../../../initiatives/v4.0/implementation/INIT-IMP-006-web-application-bundle/README.md) |
| Dedicated branch | `initiative/v4.0-web-application-bundle` |
| Captured base | `v1` at `5a0ea0bd9f51edf97f9eddd39c6a3509c271503b` |
| Canonical row | [Example initiative index](../../../../initiatives/initiative-index.md#initiative-and-correlation-register) |
| Migration disposition | [Version-correlation migration ledger](../../../../initiatives/version-correlation-migration-ledger.md#migration-ledger) |
| Predecessor or successor | None |

The initiative begins `Proposed`. Migration creates identity and navigation
only; it does not promote this suite, select artifact paths, accept web work,
or make a delivery, conformance, accessibility, security, release, or
deployment claim.


## Version-scope migration addendum (2026-11-12)

**Version scope:** `v4.0`

**Migration authority:** [EX-VSG-DR-001](../../../../initiatives/decision-receipts/EX-VSG-DR-001-initiative-migration.md)

**Current initiative target:** [INIT-IMP-006](../../../../initiatives/v4.0/implementation/INIT-IMP-006-web-application-bundle/README.md)

**Exact source catalog:** [RZN-001-P4-WEB-N01](01-RZN-001-P4-WEB-browser-bundle.md)

The original headers and one-to-one allocation language remain historical evidence under the prior revision. This addendum adopts scope membership and many-target catalog capability without changing source identity, relabeling this note or promoting its non-authoritative standing. The existing target retains the same narrow Proposed claim. Future independent outcomes require their own initiative records, not necessarily another version. The initiative index owns current assignments; the historical branch and base above remain history.
