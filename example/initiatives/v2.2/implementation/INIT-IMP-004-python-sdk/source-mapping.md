# Python SDK artifact evidence mapping

**Initiative:** `INIT-IMP-004`
**Status:** Proposed
**Last updated:** 2026-11-11

## Evidence inventory

| Evidence | Standing | Initiative use |
|---|---|---|
| [Architecture suite](../../../../evidence/authoritative/architecture/00-architecture-suite-index.md) | Authoritative | Decomposition and conformance |
| [SDK boundary](../../../../evidence/authoritative/architecture/17-python-sdk-boundary.md) | Authoritative | D4 ownership and exclusions |
| [SDK contract](../../../../evidence/authoritative/architecture/18-python-sdk-contract.md) | Authoritative | Models, methods, exceptions, transport |
| [HTTP contract](../../../../evidence/authoritative/architecture/13-record-http-contract.md) | Authoritative | Compatible D3 behavior |
| [Operations/security](../../../../evidence/authoritative/architecture/23-operations-security-contract.md) | Authoritative | Failure, security, evidence |
| [Conformance](../../../../evidence/authoritative/architecture/24-conformance-contract.md) | Authoritative | D4 gates and vectors |
| [NIST suite](../../../../evidence/authoritative/security/NIST/00-nist-security-policy-suite-index.md) | Authoritative | Security and assurance |
| [HIPAA-aligned suite](../../../../evidence/authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md) | Authoritative | Data-use and evidence gates |
| [v2.2 suite](../../../../evidence/non-authoritative/realizations/v2.2/00-RZN-001-P2-SDK-suite-index.md) | Non-authoritative | Planning details only |

## Concept and contract mapping

| Concern | Authoritative evidence | Verification evidence | Open dependency |
|---|---|---|---|
| Public models/methods | SDK contract | SDK-001..SDK-004, typing/docs | `SDK-03` |
| Transport/errors/retry | SDK and HTTP contracts | SDK-005..SDK-008, fault tests | `SDK-04` |
| Packaging/matrix | D4 boundary and conformance | wheel inspection, mock/live matrix | `SDK-01`, `SDK-02` |
| Security/data use | Operations and security suites | scans, URL/leak review | `SDK-05` |
| D4 completion boundary | ADR-007 and conformance | artifact-bound D4 manifest | `SDK-06` |

## Mapping rules

Only authoritative evidence creates requirements. Tests, generated schemas,
realization notes, and compatibility reports verify cited sources only.

## Coverage audit

Public behavior, transport, packaging, compatibility, security, data use, and
D4 conformance are covered; exact evidence destinations remain open.

## Unresolved mappings

`SDK-01` through `SDK-06` remain open. Missing evidence never becomes proof.


## Migration navigation and source standing

[EX-VSG-DR-001](../../../decision-receipts/EX-VSG-DR-001-initiative-migration.md) preserves the originating suite/note, claim and evidence standing. See the initiative README for the reciprocal per-source routing record and the migration verification record for branch preparation recovery. No new specification or delivery evidence is claimed.
