# Product 3 command-line interface realization suite

**Suite ID:** `RZN-001-P3-CLI-SUITE`  
**Suite version:** `v3.0`  
**Status:** Recorded; non-authoritative proposal input  
**Recorded by:** Codex on behalf of the User  
**Recorded date:** 2026-11-10  
**Source realization:** [`RZN-001`](../v0/RZN-001-example-record-application.md)  
**Historical product label:** `RZN-001-P3-CLI`  
**Accepted delivery-unit alignment:** `D5 Standalone CLI image`  
**Intended future initiative boundary:** One D5 standalone CLI-image initiative  
**Related initiative or proposal:** None created, as explicitly instructed  

> **Evidence standing:** This suite records a bounded CLI opportunity. It does
> not specify, implement, accept, release, or complete the CLI product.

## Purpose

This suite narrows Product 3 to the independently versioned, one-shot Compose
CLI image accepted by architecture `2.0.1`. The candidate outcome is a human
and machine-readable command surface that uses the exact released Python SDK
and the shared `/api/v1` API while owning no server, database, web, or platform
lifecycle behavior.

## Version, suite, and future-initiative rule

`v3.0` is one directory, one realization suite, and one intended future D5
initiative boundary. Multiple notes may belong here only when they retain the
same CLI-image outcome, authority, owner, product destination family,
verification claim, and lifecycle. The command interaction and image
isolation concerns remain together because both are necessary to the same
independently reviewable one-shot CLI outcome. Any independently acceptable
new outcome requires a new dot-version directory and a separate future
initiative boundary.

## Authoritative baseline

| Evidence | Standing and use |
|---|---|
| [Codex invariant suite](../../../authoritative/LLM/00_Codex_Invariant_Suite_Index.md) | Governs realization standing, narrow scope, decisions, and lifecycle claims. |
| [`ARC-SUITE-001@2.0.1`](../../../authoritative/architecture/00-architecture-suite-index.md) | Owns the shared system and capability meanings. |
| [`ADR-001`](../../../authoritative/architecture/04-ADR-001-api-exclusive-persistence.md) | Requires the CLI to use the SDK/API and forbids direct SQLite or offline fallback. |
| [`ARC-BND-005`](../../../authoritative/architecture/19-cli-boundary.md) | Owns the one-shot CLI-image boundary and exclusions. |
| [`ARC-CTR-006`](../../../authoritative/architecture/20-cli-interaction-contract.md) | Owns invocation, commands, streams, JSON, diagnostics, and exit codes. |
| [`ADR-007`](../../../authoritative/architecture/10-ADR-007-product-and-delivery-decomposition.md) | Owns D5 dependencies and the CLI-before-web sequencing gate. |
| [`ARC-CTR-009`](../../../authoritative/architecture/24-conformance-contract.md) | Owns CLI, container, operations, and end-to-end vectors and records no current D5 evidence. |
| [`SEC-NIST-SUITE-001@1.0.1`](../../../authoritative/security/NIST/00-nist-security-policy-suite-index.md) | Governs CLI security, safe output, packaging, assurance, and release claims. |
| [`SEC-HIPAA-SUITE-001@1.0.1`](../../../authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md) | Governs allowed data, diagnostics, inherited controls, evidence, and successor triggers. |

## Document catalog

| Order | Realization ID | Suite version | Same future-initiative scope |
|---:|---|---|---|
| `00` | `RZN-001-P3-CLI-SUITE` | `v3.0` | This standing, lineage, authority, dependency, and navigation index |
| `01` | `RZN-001-P3-CLI-N01` | `v3.0` | The D5 one-shot CLI image, command contract, streams, failures, isolation, release identity, security, and exact evidence boundary |

## Dependency and sequencing

The candidate CLI depends on compatible D1-D4 identities from `v1.0`, `v2.0`,
`v2.1`, and `v2.2`: documented contracts, the container platform, a live
API/SQLite baseline, and the exact released SDK wheel. It cannot claim those
units as part of its own completion.
Delivery of D5 precedes D6 by the accepted sequence even though web code does
not depend on CLI code.

## Suite-wide boundary

- No host-installed CLI, Python, SDK, SQLite, or source checkout is a supported
  product path.
- No direct HTTP implementation outside the SDK, direct SQLite path, API
  lifecycle control, background daemon, hidden prompt, force update, delete,
  bulk operation, record import/export, or offline fallback is in scope.
- Record content is permitted only as explicit success output for in-profile
  synthetic or documented de-identified data; diagnostics and evidence remain
  minimized and redacted.
- No initiative, implementation, conformance, or release claim is created.

## Handoff rule

A future proposal must cite `RZN-001-P3-CLI-N01`, identify the exact compatible
D2-D4 artifacts, map all applicable architecture vectors and security gates,
and keep the acceptance claim limited to D5. This suite creates no initiative.

