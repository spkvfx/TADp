# Web application bundle evidence mapping

**Initiative:** `INIT-IMP-006`
**Status:** Proposed
**Last updated:** 2026-11-11

## Evidence inventory

| Evidence | Standing | Initiative use |
|---|---|---|
| [Architecture suite](../../../../evidence/authoritative/architecture/00-architecture-suite-index.md) | Authoritative | Decomposition/conformance |
| [Web boundary](../../../../evidence/authoritative/architecture/21-web-application-boundary.md) | Authoritative | D6 ownership/exclusions |
| [Web contract](../../../../evidence/authoritative/architecture/22-web-interaction-contract.md) | Authoritative | State/interaction/accessibility |
| [HTTP contract](../../../../evidence/authoritative/architecture/13-record-http-contract.md) | Authoritative | Same-origin API semantics |
| [Operations/security](../../../../evidence/authoritative/architecture/23-operations-security-contract.md) | Authoritative | Runtime/security/failure |
| [Conformance](../../../../evidence/authoritative/architecture/24-conformance-contract.md) | Authoritative | D6 vectors/gates |
| [NIST suite](../../../../evidence/authoritative/security/NIST/00-nist-security-policy-suite-index.md) | Authoritative | Security/assurance |
| [HIPAA-aligned suite](../../../../evidence/authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md) | Authoritative | Data-use/evidence gates |
| [v4.0 suite](../../../../evidence/non-authoritative/realizations/v4.0/00-RZN-001-P4-WEB-suite-index.md) | Non-authoritative | Planning only |

## Concept and contract mapping

| Concern | Authoritative evidence | Verification evidence | Open dependency |
|---|---|---|---|
| Workflows/state | Web/API contracts | WEB-001..WEB-006, state/race tests | `WEB-02` |
| Accessibility/help | Web contract | WEB-007..WEB-010, manual/automated AT | `WEB-04`, `WEB-07` |
| Assets/same-origin | Web boundary/operations | WEB-011..WEB-013, manifest/CSP/storage | `WEB-01`, `WEB-05` |
| Browser/API matrix | Conformance | browser/OS/AT/D3 matrix | `WEB-03`, `WEB-04` |
| Security/data | Security suites | DOM/dependency/map/leak review | `WEB-05`, `WEB-06` |
| D6 boundary | ADR-007/conformance | D6 manifest | `WEB-07` |

## Mapping rules

Authoritative sources create requirements. Generated assets, audit reports,
snapshots, traces, and realization notes only verify cited contracts.

## Coverage audit

Workflows, state, accessibility, artifact, integration, compatibility,
security, data use, and D6 conformance are covered; locations/matrix remain open.

## Unresolved mappings

`WEB-01`-`WEB-07` remain open. Missing evidence never proves an outcome.


## Migration navigation and source standing

[EX-VSG-DR-001](../../../decision-receipts/EX-VSG-DR-001-initiative-migration.md) preserves the originating suite/note, claim and evidence standing. See the initiative README for the reciprocal per-source routing record and the migration verification record for branch preparation recovery. No new specification or delivery evidence is claimed.
