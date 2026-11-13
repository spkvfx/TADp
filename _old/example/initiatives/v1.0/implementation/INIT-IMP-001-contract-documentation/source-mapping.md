# Contract documentation evidence mapping

**Initiative:** Contract documentation  
**Status:** Proposed  
**Last updated:** 2026-11-11  
**Decision prefix:** `DOC`

This map connects evidence to the Proposed specification, product destination,
and verification. It does not resolve assumptions or decisions.

## Evidence inventory

| Evidence ID | Source | Evidence label | Governs | Conflict rule |
|---|---|---|---|---|
| `EVD-01` | [`ARC-SUITE-001@2.0.1`](../../../../evidence/authoritative/architecture/00-architecture-suite-index.md) | `../../evidence/authoritative` | Technical meaning, source catalog, D1–D6 decomposition | Block derivative; authority is never edited here |
| `EVD-02` | [`ADR-006`](../../../../evidence/authoritative/architecture/09-ADR-006-contract-versioning-and-feedback.md) | `../../evidence/authoritative` | Revision, compatibility, and feedback handling | Preserve conflict and route governed successor |
| `EVD-03` | [`ADR-007`](../../../../evidence/authoritative/architecture/10-ADR-007-product-and-delivery-decomposition.md) | `../../evidence/authoritative` | D1 boundary and independent claims | Split work that crosses a delivery-unit claim |
| `EVD-04` | [`ARC-CTR-009`](../../../../evidence/authoritative/architecture/24-conformance-contract.md) | `../../evidence/authoritative` | D1 gate and truthful evidence vocabulary | Planned vectors never become results |
| `EVD-05` | [NIST suite `1.0.1`](../../../../evidence/authoritative/security/NIST/00-nist-security-policy-suite-index.md) | `../../evidence/authoritative` | Security/use/assurance requirements and claim limits | Block conflicting or incomplete security text |
| `EVD-06` | [HIPAA suite `1.0.1`](../../../../evidence/authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md) | `../../evidence/authoritative` | Data profile, safeguards, evidence, successor gate | Prohibit possible ePHI and route successor trigger |
| `EVD-07` | [`RZN-001-P1-DOCS-N01`](../../../../evidence/non-authoritative/realizations/v1.0/01-RZN-001-P1-DOCS-contract-documentation.md) | `../../evidence/non-authoritative` | Candidate areas, risks, and open publication choices | May inform but cannot override EVD-01–06 |

## Concept and contract mapping

| Map ID | Concept or contract | Authoritative evidence | Assumption | Decision | Specification location | Product destination | Verification evidence | Status |
|---|---|---|---|---|---|---|---|---|
| `MAP-001` | One documentation-only D1 outcome | `EVD-03`, D1 | `DOC-A01` | `DOC-02` | [Goals and non-goals](architecture.md#goals-and-non-goals) | Destination selected by `DOC-01` | Scope and D1 claim review | Proposed |
| `MAP-002` | Normative-source ownership | `EVD-01`, suite standing; `EVD-02` | `DOC-A02` | `DOC-03` | [Domain model](architecture.md#domain-model-and-evidenceauthoritative) | Source map and derivative prose | Claim-to-source and drift review | Proposed |
| `MAP-003` | D1–D6 non-claim boundary | `EVD-03`; `EVD-04`, Current evidence status | `DOC-A03` | `DOC-02` | [Specification boundary](architecture.md#specification-boundary) | Limitations at each entry point | Claim-language review | Proposed |
| `MAP-004` | Local/Compose-only trust profile | `EVD-01`, `AUTH-EX-001.6/.11`; `EVD-05`, `SEC-POL-01/02` | `DOC-A02` | `DOC-06` | [Security](architecture.md#security-and-authorization) | Security/use guide | Source coverage review | Proposed |
| `MAP-005` | Synthetic/de-identified-only data | `EVD-06`, `HSP-002`; `EVD-05`, `SEC-POL-01` | `DOC-A04` | `DOC-06` | [Security](architecture.md#security-and-authorization) | Examples and evidence | Fixture manifest and leak review | Proposed |
| `MAP-006` | No certification/compliance/ePHI claim | `EVD-05`, claim gate; `EVD-06`, `HSP-001/015` | `DOC-A05` | `DOC-06` | [Failure and recovery](architecture.md#failure-and-recovery) | Entry-point limitations | Claim-language review | Proposed |
| `MAP-007` | Revision and compatibility identity | `EVD-02`; `EVD-04`, evidence fields | `DOC-A04` | `DOC-04` | [Compatibility](architecture.md#compatibility-migration-and-rollout) | Product metadata | Revision/source diff review | Proposed |
| `MAP-008` | Documentation accessibility/usability | `EVD-04`, D1 review boundary | `DOC-A01` | `DOC-05` | [Testing strategy](architecture.md#testing-strategy) | Selected documentation product | Accepted `DOC-05` method/result | Proposed |
| `MAP-009` | Generated artifacts remain derivative | `EVD-01`, authority; `EVD-02` | `DOC-A02` | `DOC-03` | [Interfaces](architecture.md#interfaces-and-integration) | Optional generated appendices | Exact input/output hashes and drift check | Proposed |
| `MAP-010` | Independent later-product evidence | `EVD-04`, D2–D6 gates | `DOC-A06` | Not applicable — authority already fixes the boundary | [Deferred work](architecture.md#deferred-work) | Later products only | Exact later initiative evidence | Proposed |

## Mapping rules

- Cite exact records, revisions, policies, claims, or sections.
- Keep proposal and realization inputs non-authoritative.
- Every product statement must map through this table before publication.
- A source conflict or missing authority is blocking and belongs in the
  decision register or invariant-conflict process.
- `Proposed` changes only after source, specification, destination, and
  verification agree through the authorized lifecycle.

## Coverage audit

| Area | Expected concepts or contracts | Mapped | Gaps | Gate |
|---|---|---|---|---|
| Product and scope | D1 claim, destination, audiences | `MAP-001`, `MAP-003` | `DOC-01`, `DOC-02` | Blocked |
| Domain and identity | Source ownership, derivative/revision identity | `MAP-002`, `MAP-007`, `MAP-009` | `DOC-03`, `DOC-04` | Blocked |
| Interfaces and integration | Links, generated inputs, entry points | `MAP-002`, `MAP-009` | Exact tooling/destination | Blocked |
| Data and lifecycle | Fixtures, revisions, later evidence | `MAP-005`, `MAP-007`, `MAP-010` | Owner/review details | Blocked |
| Security and authority | Trust profile, data limits, claim limits | `MAP-004`–`MAP-006` | `DOC-06` | Blocked |
| Operations and recovery | Review, publication rollback, accessibility | `MAP-006`, `MAP-008` | `DOC-01`, `DOC-05` | Blocked |

## Unresolved mappings

| ID | Missing or conflicting evidence | Affected rows | Decision or owner | Required resolution |
|---|---|---|---|---|
| `MAP-Q01` | Product destination and publication system are not selected | `MAP-001`–`MAP-009` | `DOC-01` / User | Select an owned destination and re-evaluate operational implications |
| `MAP-Q02` | Audience and generated-output cohesion are not accepted | `MAP-001`, `MAP-002`, `MAP-009` | `DOC-02`, `DOC-03` / User | Accept one coherent set or split before acceptance |
| `MAP-Q03` | Accessibility/usability method and review ownership are open | `MAP-004`–`MAP-008` | `DOC-05`, `DOC-06` / User | Select methods, owners, environments, and evidence destinations |


## Migration navigation and source standing

[EX-VSG-DR-001](../../../decision-receipts/EX-VSG-DR-001-initiative-migration.md) preserves the originating suite/note, claim and evidence standing. See the initiative README for the reciprocal per-source routing record and the migration verification record for branch preparation recovery. No new specification or delivery evidence is claimed.
