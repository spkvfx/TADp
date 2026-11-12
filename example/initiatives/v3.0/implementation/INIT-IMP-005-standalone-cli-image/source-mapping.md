# Standalone CLI image evidence mapping

**Initiative:** `INIT-IMP-005`
**Status:** Proposed
**Last updated:** 2026-11-11

## Evidence inventory

| Evidence | Standing | Initiative use |
|---|---|---|
| [Architecture suite](../../../../evidence/authoritative/architecture/00-architecture-suite-index.md) | Authoritative | Decomposition and conformance |
| [CLI boundary](../../../../evidence/authoritative/architecture/19-cli-boundary.md) | Authoritative | D5 ownership/exclusions |
| [CLI contract](../../../../evidence/authoritative/architecture/20-cli-interaction-contract.md) | Authoritative | Commands/output/exits/process |
| [SDK contract](../../../../evidence/authoritative/architecture/18-python-sdk-contract.md) | Authoritative | Permitted D4 public dependency |
| [Operations/security](../../../../evidence/authoritative/architecture/23-operations-security-contract.md) | Authoritative | Runtime/security/failure |
| [Conformance](../../../../evidence/authoritative/architecture/24-conformance-contract.md) | Authoritative | D5 vectors/gates |
| [NIST suite](../../../../evidence/authoritative/security/NIST/00-nist-security-policy-suite-index.md) | Authoritative | Security/assurance |
| [HIPAA-aligned suite](../../../../evidence/authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md) | Authoritative | Data-use/evidence gates |
| [v3.0 suite](../../../../evidence/non-authoritative/realizations/v3.0/00-RZN-001-P3-CLI-suite-index.md) | Non-authoritative | Planning only |

## Concept and contract mapping

| Concern | Authoritative evidence | Verification evidence | Open dependency |
|---|---|---|---|
| Commands/help/validation | CLI contract | CLI-001..CLI-004 | `CLI-01`, `CLI-02` |
| Output/JSON/exits | CLI contract | CLI-005..CLI-008, golden/schema tests | `CLI-03` |
| Signals/pipes/faults | CLI and operations contracts | CLI-009..CLI-011, process harness | `CLI-04` |
| Image/dependencies | Boundary/conformance | build/scan/Compose matrix | `CLI-01`, `CLI-02` |
| Security/data | Security suites | terminal/leak/risk review | `CLI-05` |
| D5 boundary | ADR-007/conformance | D5 manifest | `CLI-06` |

## Mapping rules

Authoritative sources create requirements. Notes, golden output, generated
completion, and tests only verify cited contracts.

## Coverage audit

Interaction, process behavior, artifact, dependencies, compatibility, security,
data use, and D5 conformance are covered; destinations remain open.

## Unresolved mappings

`CLI-01`-`CLI-06` remain open. Missing evidence never becomes proof.


## Migration navigation and source standing

[EX-VSG-DR-001](../../../decision-receipts/EX-VSG-DR-001-initiative-migration.md) preserves the originating suite/note, claim and evidence standing. See the initiative README for the reciprocal per-source routing record and the migration verification record for branch preparation recovery. No new specification or delivery evidence is claimed.
