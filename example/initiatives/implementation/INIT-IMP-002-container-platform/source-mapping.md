# Container platform and runtime packaging evidence mapping

**Initiative:** Container platform and runtime packaging
**Status:** Proposed
**Last updated:** 2026-11-11
**Decision prefix:** `PLT`

## Evidence inventory

| Evidence ID | Source | Evidence label | Governs | Conflict rule |
|---|---|---|---|---|
| `EVD-01` | [`ADR-004`](../../../evidence/authoritative/architecture/07-ADR-004-container-only-deployment-trust-model.md) | `../../evidence/authoritative` | Trust topology and hardening | Block conflicting product |
| `EVD-02` | [`ADR-005`](../../../evidence/authoritative/architecture/08-ADR-005-containerized-technology-stack.md) | `../../evidence/authoritative` | Build targets and release integrity | Block drift; route design change |
| `EVD-03` | [`ARC-CTR-008`](../../../evidence/authoritative/architecture/23-operations-security-contract.md) | `../../evidence/authoritative` | Compose, lifecycle, limits, operations | Exact contract wins |
| `EVD-04` | [`ARC-CTR-009`](../../../evidence/authoritative/architecture/24-conformance-contract.md) | `../../evidence/authoritative` | D2 vectors/evidence | Planned checks are not results |
| `EVD-05` | [NIST](../../../evidence/authoritative/security/NIST/00-nist-security-policy-suite-index.md) and [HIPAA](../../../evidence/authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md) suites | `../../evidence/authoritative` | Security/use/evidence gates | Both apply additively |
| `EVD-06` | [Platform realization](../../../evidence/non-authoritative/realizations/v2.0/01-RZN-001-P2-PLATFORM-v2.0-container-platform.md) | `../../evidence/non-authoritative` | Candidate detail/open choices | Cannot override EVD-01–05 |

## Concept and contract mapping

| Map ID | Concept or contract | Authoritative evidence | Assumption | Decision | Specification location | Product destination | Verification evidence | Status |
|---|---|---|---|---|---|---|---|---|
| `MAP-001` | One D2 platform family | `EVD-01`–`EVD-04` | `PLT-A01` | `PLT-01`, `PLT-06` | [Goals](architecture.md#goals-and-non-goals) | Open by `PLT-01` | Scope and D2 gate review | Proposed |
| `MAP-002` | Build/target/artifact identity | `EVD-02`, `EVD-04` | `PLT-A02` | `PLT-02`, `PLT-03` | [Terms](architecture.md#terms-and-identity) | Build/release paths | `CNT-007`–`009`, `OPS-010` | Proposed |
| `MAP-003` | Effective Compose topology | `EVD-01`, `EVD-03` | `PLT-A03` | `PLT-01` | [Boundaries](architecture.md#boundaries-and-ownership) | Compose product | `CNT-002`–`005`, `011`, `015` | Proposed |
| `MAP-004` | Volumes/test isolation/lifecycle | `EVD-03`, `EVD-04` | `PLT-A04` | `PLT-04` | [State](architecture.md#state-and-persistence) | Compose/runbooks | `CNT-010`–`013`, `OPS-011`–`013` | Proposed |
| `MAP-005` | Hardening/resources/failure | `EVD-01`, `EVD-03` | `PLT-A05` | `PLT-02` | [Failure](architecture.md#failure-and-recovery) | Images/Compose | `CNT-005/006`, `OPS-006/007` | Proposed |
| `MAP-006` | Consumer handoffs remain independent | `EVD-02`, `EVD-04` | `PLT-A06` | `PLT-06` | [Interfaces](architecture.md#interfaces-and-integration) | Target/hash metadata | `CNT-008/014`, `E2E-009` | Proposed |
| `MAP-007` | Security/use/supply-chain evidence | `EVD-05` | `PLT-A02`, `PLT-A05` | `PLT-03`, `PLT-05` | [Security](architecture.md#security-and-authorization) | Release/evidence records | Exact policy and artifact evidence | Proposed |

## Mapping rules

Use exact authoritative locators; keep realization evidence contextual; map
each product output to a decision and verification; block missing/conflicting
authority; retain Proposed standing until the authorized lifecycle changes it.

## Coverage audit

| Area | Expected concepts or contracts | Mapped | Gaps | Gate |
|---|---|---|---|---|
| Product and scope | D2 family/paths/split | `MAP-001` | `PLT-01`, `PLT-06` | Blocked |
| Domain and identity | Digests, targets, render | `MAP-002`, `MAP-003` | `PLT-02`, `PLT-03` | Blocked |
| Interfaces and integration | Consumer handoffs | `MAP-003`, `MAP-006` | Exact products unavailable | Blocked |
| Data and lifecycle | Volumes, tests, upgrade/recovery | `MAP-004` | Matrix/evidence selection | Blocked |
| Security and authority | Hardening, supply chain, use | `MAP-005`, `MAP-007` | `PLT-03`, `PLT-05` | Blocked |
| Operations and recovery | Lifecycle/fault/host matrix | `MAP-004`, `MAP-005` | `PLT-02`, `PLT-04` | Blocked |

## Unresolved mappings

| ID | Missing or conflicting evidence | Affected rows | Decision or owner | Required resolution |
|---|---|---|---|---|
| `MAP-Q01` | Product paths and artifact family not selected | `MAP-001`–`MAP-007` | `PLT-01` / User | Select paths and rerun scope/ownership review |
| `MAP-Q02` | Tool/platform/provenance matrix open | `MAP-002`–`MAP-005` | `PLT-02`–`PLT-04` / User | Fix exact identities, trust, and environments |
| `MAP-Q03` | Evidence destination and split review open | `MAP-001`, `MAP-006`, `MAP-007` | `PLT-05`, `PLT-06` / User | Select retention and confirm one claim |
