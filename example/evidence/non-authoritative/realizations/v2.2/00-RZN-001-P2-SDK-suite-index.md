# Product 2 Python SDK realization suite

**Suite ID:** `RZN-001-P2-SDK-SUITE`  
**Suite version:** `v2.2`  
**Status:** Recorded; non-authoritative proposal input  
**Recorded by:** Codex on behalf of the User  
**Recorded date:** 2026-11-10  
**Source realization:** [`RZN-001`](../v0/RZN-001-example-record-application.md)  
**Historical product relationship:** SDK portion of `RZN-001-P2-SDK-API`  
**Accepted delivery-unit alignment:** `D4 Python SDK artifact`  
**Intended future initiative boundary:** One D4 Python SDK initiative  
**Related initiative or proposal:** None created, as explicitly instructed  

> **Evidence standing:** This dot-version directory is a separate realization
> suite and one intended future initiative boundary. It is not an initiative,
> wheel, compatibility promise, conformance result, or completion claim.

## Purpose

This suite narrows the historical Product 2 SDK intent to the accepted D4
wheel boundary: public synchronous Python models and methods, client lifecycle,
wire encoding/decoding, retries, exceptions, packaging, compatibility, and
containerized evidence. It does not aggregate the v2.0 platform or v2.1 API.

## Version, suite, and future-initiative rule

`v2.2` is one directory, one realization suite, and one intended future D4
initiative boundary. Multiple notes may belong here only when they retain the
same SDK wheel outcome, authority, owner, destination family, verification
claim, and lifecycle. A separately acceptable product requires a new
dot-version directory.

## Authoritative baseline

| Evidence | Standing and use |
|---|---|
| [Codex invariant suite](../../../authoritative/LLM/00_Codex_Invariant_Suite_Index.md) | Governs evidence standing, scope, decisions, and lifecycle claims. |
| [`ARC-BND-004`](../../../authoritative/architecture/17-python-sdk-boundary.md) | Owns the SDK package/dependency/state boundary and exclusions. |
| [`ARC-CTR-005`](../../../authoritative/architecture/18-python-sdk-contract.md) | Owns public symbols, models, methods, retries, exceptions, compatibility, and verification. |
| [`ADR-005`](../../../authoritative/architecture/08-ADR-005-containerized-technology-stack.md) | Owns wheel build/consumption and no-host-toolchain rules. |
| [`ADR-007`](../../../authoritative/architecture/10-ADR-007-product-and-delivery-decomposition.md) | Defines D4 dependencies and independent completion. |
| [`ARC-CTR-009`](../../../authoritative/architecture/24-conformance-contract.md) | Defines the D4 gate and records no current D4 implementation or conformance. |
| [`SEC-NIST-SUITE-001@1.0.1`](../../../authoritative/security/NIST/00-nist-security-policy-suite-index.md) | Primary NIST-aligned SDK security/assurance invariant. |
| [`SEC-HIPAA-SUITE-001@1.0.1`](../../../authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md) | Primary data-use, safe-output, evidence, and successor-gate invariant. |

## Document catalog

| Order | Realization ID | Suite version | Same future-initiative scope |
|---:|---|---|---|
| `00` | `RZN-001-P2-SDK-SUITE` | `v2.2` | This standing, authority, lineage, and dependency index |
| `01` | `RZN-001-P2-SDK-N01` | `v2.2` | Public SDK surface, packaging, client behavior, data handling, security, compatibility, and D4 evidence boundary |

## Exact suite boundary

Included concerns are the exact SDK wheel and its supported containerized
consumer path. Excluded are the v2.0 platform completion claim, v2.1 server and
SQLite behavior, v3.0 CLI process, v4.0 browser product, host Python installation,
async/raw/offline clients, and all remote/regulated-use claims.

## Dependencies and consumers

- D1/v1.0 supplies the exact SDK contract identity.
- D2/v2.0 supplies the `sdk-wheel` and test/developer build path.
- D3/v2.1 supplies the compatible mock fixtures and live `/api/v1` baseline.
- D5/v3.0 consumes the exact tested wheel without importing internal modules.

## Handoff rule

If later directed, one D4 proposal may consume all notes in this directory. It
must keep v2.0, v2.1, and v3.0 separately governed, identify exact predecessor
artifacts, and limit its claim to the D4 wheel. No initiative is created by
this suite.

