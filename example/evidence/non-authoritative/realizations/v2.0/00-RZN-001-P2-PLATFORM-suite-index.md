# Product 2 container-platform realization suite

**Suite ID:** `RZN-001-P2-PLATFORM-SUITE`  
**Suite version:** `v2.0`  
**Status:** Recorded; non-authoritative proposal input  
**Recorded by:** Codex on behalf of the User  
**Recorded date:** 2026-11-10  
**Source realization:** [`RZN-001`](../v0.0/RZN-001-example-record-application.md)  
**Historical product relationship:** Architecture-required predecessor for `RZN-001-P2-SDK-API`  
**Accepted delivery-unit alignment:** `D2 Container platform and runtime packaging`  
**Intended future initiative boundary:** One D2 container-platform initiative  
**Related initiative or proposal:** None created, as explicitly instructed  

> **Evidence standing:** This suite records one future-initiative input. It is
> not an initiative record, accepted specification, platform implementation,
> release, security assessment, or completion claim.

## Purpose

The parent realization grouped an implemented SDK and API as Product 2. The
accepted architecture later added a separately reviewable container-platform
predecessor because every supported build, test, runtime, maintenance, and
release path must be Docker Compose-only. This v2.0 suite captures only that D2
outcome. It does not coordinate or aggregate the independent v2.1 API/SQLite
or v2.2 SDK suites.

The placement preserves historical identity: `RZN-001` did not originally
name a container-platform product. The explicit Dockerization authority and
`ADR-007` created this required delivery unit.

## Version, suite, and future-initiative rule

This `v2.0` directory is one realization suite and corresponds to one intended
future D2 initiative boundary. Multiple notes may appear here only when they
share the same container-platform outcome, authority, owner, product
destination family, verification claim, and lifecycle.

Every dot version is a separate directory, separate realization suite, and
separate future initiative boundary. Accordingly:

- [`v2.1`](../v2.1/00-RZN-001-P2-API-SQLITE-suite-index.md) owns the D3 API and
  SQLite runtime-image realization suite; and
- [`v2.2`](../v2.2/00-RZN-001-P2-SDK-suite-index.md) owns the D4 Python SDK
  realization suite.

Those suites are dependencies or consumers, not children whose status this
suite may accept, aggregate, or complete.

## Authoritative baseline

| Evidence | Standing and use |
|---|---|
| [Codex invariant suite](../../../authoritative/LLM/00_Codex_Invariant_Suite_Index.md) | Governs evidence standing, narrow scope, source preservation, lifecycle, and truthful claims. |
| [`ARC-SUITE-001@2.0.1`](../../../authoritative/architecture/00-architecture-suite-index.md) | Owns the complete technical architecture. |
| [`ADR-004`](../../../authoritative/architecture/07-ADR-004-container-only-deployment-trust-model.md) | Owns the Compose-only trust boundary, host exclusions, and container controls. |
| [`ADR-005`](../../../authoritative/architecture/08-ADR-005-containerized-technology-stack.md) | Owns the BuildKit targets, selected image/runtime stack, and release rules. |
| [`ADR-007`](../../../authoritative/architecture/10-ADR-007-product-and-delivery-decomposition.md) | Defines D2 as independent from D3-D6 and supplies dependency order. |
| [`ARC-CTR-008`](../../../authoritative/architecture/23-operations-security-contract.md) | Owns effective Compose topology, hardening, lifecycle, maintenance, health, and release behavior. |
| [`ARC-CTR-009`](../../../authoritative/architecture/24-conformance-contract.md) | Defines the D2 gate and states that no current D2 implementation or conformance evidence exists. |
| [`SEC-NIST-SUITE-001@1.0.1`](../../../authoritative/security/NIST/00-nist-security-policy-suite-index.md) | Primary NIST-aligned platform/release security and assurance invariant. |
| [`SEC-HIPAA-SUITE-001@1.0.1`](../../../authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md) | Primary data-use, safeguard, inherited-control, evidence, and successor-gate invariant. |
| [`REC-RZN-001-001`](../../reconciliations/RZN-001-architecture-security-reconciliation.md) | Non-authoritative applied comparison recording why D2-D6 supersede the historical combined delivery assumption. |

## Document catalog

| Order | Realization ID | Suite version | Same future-initiative scope |
|---:|---|---|---|
| `00` | `RZN-001-P2-PLATFORM-SUITE` | `v2.0` | This standing, lineage, authority, dependency, and navigation index |
| `01` | `RZN-001-P2-PLATFORM-N01` | `v2.0` | BuildKit/Compose runtime packaging, topology, hardening, artifact identity, lifecycle, and D2 evidence boundary |

## Exact suite boundary

Included realization concerns are limited to:

- the multi-stage BuildKit graph and deny-by-default build context;
- Compose services, profiles, private network, loopback publication, named
  volumes, health, security settings, and resource ceilings;
- container-only build, test, runtime, SDK-consumption, CLI, web-asset,
  maintenance, and recovery envelopes;
- immutable image/manifests and wheel/bundle continuity mechanisms;
- platform configuration, supported hosts/OCI targets, lifecycle commands,
  supply-chain evidence, and platform failure behavior; and
- exact architecture/NIST/HIPAA evidence needed for the D2 claim.

Excluded from this suite are record/domain/API/persistence behavior, SDK public
behavior, CLI interaction, browser behavior/accessibility, and every D3-D6
completion claim.

## Dependency and handoff

```text
v1 / D1 contract identity
        |
        v
v2.0 / D2 container platform
        |
        v
v2.1 / D3 API and SQLite image
        |
        v
v2.2 / D4 Python SDK
        |
        v
v3.0 / D5 CLI -> v4.0 / D6 web delivery sequence
```

The graph records dependency intent only. It is not evidence that any future
initiative, product, artifact, test, or gate exists or passes.

## Security and data boundary

The suite is limited to local, single-user, non-production operation using
purpose-created synthetic data or externally documented de-identified data
that also satisfies the NIST restrictions. Actual or possible ePHI,
credentials, confidential business data, production records, remote or
multi-user access, shared workstations, third-party record processing, and
formal compliance claims are excluded and trigger the applicable successor
gate.

Passing D2 architecture vectors cannot substitute for NIST or HIPAA evidence,
and D2 cannot claim the status of any dependent suite.

## Handoff rule

If the User later requests initiative work, one D2 proposal may consume all
notes in this directory because they share one future-initiative boundary. It
must cite exact authoritative sources, choose product destinations, perform the
mandatory scope assessment, and keep v2.1 and v2.2 as separately governed
initiatives. No initiative is created by this suite.

