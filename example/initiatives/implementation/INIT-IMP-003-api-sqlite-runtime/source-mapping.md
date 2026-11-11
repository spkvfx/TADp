# API and SQLite runtime image evidence mapping

**Initiative:** `INIT-IMP-003`
**Status:** Proposed
**Last updated:** 2026-11-11

## Evidence inventory

| Evidence | Standing | Initiative use |
|---|---|---|
| [Architecture suite](../../../evidence/authoritative/architecture/00-architecture-suite-index.md) | Authoritative | D3 contracts, decomposition, operations, conformance |
| [Record domain](../../../evidence/authoritative/architecture/11-record-domain-contract.md) | Authoritative | Identity, validation, timestamps, revisions |
| [API service boundary](../../../evidence/authoritative/architecture/12-api-service-boundary.md) | Authoritative | D3 service ownership and interfaces |
| [HTTP API](../../../evidence/authoritative/architecture/13-record-http-contract.md) | Authoritative | `/api/v1` methods, problems, concurrency |
| [Search and navigation](../../../evidence/authoritative/architecture/14-search-navigation-contract.md) | Authoritative | Query, result, and hierarchy behavior |
| [SQLite](../../../evidence/authoritative/architecture/16-sqlite-persistence-contract.md) | Authoritative | Schema, transactions, migration, recovery |
| [Operations/security](../../../evidence/authoritative/architecture/23-operations-security-contract.md) | Authoritative | Runtime, health, logging, maintenance |
| [Conformance](../../../evidence/authoritative/architecture/24-conformance-contract.md) | Authoritative | D3 evidence gates |
| [NIST suite](../../../evidence/authoritative/security/NIST/00-nist-security-policy-suite-index.md) | Authoritative | Security and assurance |
| [HIPAA-aligned suite](../../../evidence/authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md) | Authoritative | Data-use and safeguard gates |
| [v2.1 suite](../../../evidence/non-authoritative/realizations/v2.1/00-RZN-001-P2-API-SQLITE-suite-index.md) | Non-authoritative | Planning details only |

## Concept and contract mapping

| Concern | Authoritative evidence | Verification evidence | Open dependency |
|---|---|---|---|
| Domain and HTTP semantics | ARC-CTR-001 and API contract | DOM/HTTP vectors and fixtures | `API-03`, `API-04` |
| Search and navigation | Search/navigation contracts | SRCH/NAV vectors | `API-03` |
| SQLite and migrations | ARC-CTR-004 | DB vectors, clean/upgrade/recovery runs | `API-01`, `API-02` |
| Runtime and health | ARC-CTR-008 | CNT/OPS vectors and fault runs | `API-02`, `API-03` |
| Security and data use | NIST and HIPAA-aligned suites | scans, review, synthetic-data record | `API-05` |
| D3 completion boundary | ADR-007 and ARC-CTR-009 | traceable D3 evidence set | `API-06` |

## Mapping rules

Authority flows only from authoritative evidence. Realization notes may suggest
work but cannot add requirements. Generated artifacts and tests verify cited
contracts; they never replace those contracts.

## Coverage audit

The mapping covers domain, API, search, navigation, persistence, operations,
security, data use, compatibility, and D3 conformance. Exact evidence locations
remain open.

## Unresolved mappings

`API-01` through `API-06` remain open. No missing mapping is silently treated
as not applicable or as proof of completion.
