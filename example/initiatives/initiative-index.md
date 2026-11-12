# Example Record Application initiative index

**Index owner:** User

**Last reviewed:** 2026-11-12

This index owns current membership, one row per initiative. Each initiative README owns its lifecycle. Scope identity, Git refs and preparation do not establish acceptance or delivery.

## Initiative and correlation register

| Scope | Initiative ID | Type | Record location | Source notes | Execution branch | Execution mode | Captured base ref | Captured base commit | Integration target | Revision cycle | Lifecycle evidence | Integration evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| v1.0 | INIT-IMP-001 | implementation | [INIT-IMP-001-contract-documentation](v1.0/implementation/INIT-IMP-001-contract-documentation/README.md) | [RZN-001-P1-DOCS-N01](../evidence/non-authoritative/realizations/v1.0/01-RZN-001-P1-DOCS-contract-documentation.md) | initiative/v1.0-INIT-IMP-001-contract-documentation | dedicated | v1.0 | 7b9d302b3dc7a94627518e42819a3130b5ba17d3 | v1.0 | 2 | [Proposed lifecycle and migration history](v1.0/implementation/INIT-IMP-001-contract-documentation/README.md) | Pending; [preparation recovery; no closure or merge](decision-receipts/EX-VSG-VER-001-migration-verification.md) |
| v2.0 | INIT-IMP-002 | implementation | [INIT-IMP-002-container-platform](v2.0/implementation/INIT-IMP-002-container-platform/README.md) | [RZN-001-P2-PLATFORM-N01](../evidence/non-authoritative/realizations/v2.0/01-RZN-001-P2-PLATFORM-v2.0-container-platform.md) | initiative/v2.0-INIT-IMP-002-container-platform | dedicated | v2.0 | 36bb20c88802191e13b873a36a07531fcfab5f42 | v2.0 | 2 | [Proposed lifecycle and migration history](v2.0/implementation/INIT-IMP-002-container-platform/README.md) | Pending; [preparation recovery; no closure or merge](decision-receipts/EX-VSG-VER-001-migration-verification.md) |
| v2.1 | INIT-IMP-003 | implementation | [INIT-IMP-003-api-sqlite-runtime](v2.1/implementation/INIT-IMP-003-api-sqlite-runtime/README.md) | [RZN-001-P2-API-SQLITE-N01](../evidence/non-authoritative/realizations/v2.1/01-RZN-001-P2-API-SQLITE-v2.1-api-runtime.md) | initiative/v2.1-INIT-IMP-003-api-sqlite-runtime | dedicated | v2.1 | 36bb20c88802191e13b873a36a07531fcfab5f42 | v2.1 | 2 | [Proposed lifecycle and migration history](v2.1/implementation/INIT-IMP-003-api-sqlite-runtime/README.md) | Pending; [preparation recovery; no closure or merge](decision-receipts/EX-VSG-VER-001-migration-verification.md) |
| v2.2 | INIT-IMP-004 | implementation | [INIT-IMP-004-python-sdk](v2.2/implementation/INIT-IMP-004-python-sdk/README.md) | [RZN-001-P2-SDK-N01](../evidence/non-authoritative/realizations/v2.2/01-RZN-001-P2-SDK-v2.2-python-sdk.md) | initiative/v2.2-INIT-IMP-004-python-sdk | dedicated | v2.2 | 36bb20c88802191e13b873a36a07531fcfab5f42 | v2.2 | 2 | [Proposed lifecycle and migration history](v2.2/implementation/INIT-IMP-004-python-sdk/README.md) | Pending; [preparation recovery; no closure or merge](decision-receipts/EX-VSG-VER-001-migration-verification.md) |
| v3.0 | INIT-IMP-005 | implementation | [INIT-IMP-005-standalone-cli-image](v3.0/implementation/INIT-IMP-005-standalone-cli-image/README.md) | [RZN-001-P3-CLI-N01](../evidence/non-authoritative/realizations/v3.0/01-RZN-001-P3-CLI-command-image.md) | initiative/v3.0-INIT-IMP-005-standalone-cli-image | dedicated | v3.0 | 36bb20c88802191e13b873a36a07531fcfab5f42 | v3.0 | 2 | [Proposed lifecycle and migration history](v3.0/implementation/INIT-IMP-005-standalone-cli-image/README.md) | Pending; [preparation recovery; no closure or merge](decision-receipts/EX-VSG-VER-001-migration-verification.md) |
| v4.0 | INIT-IMP-006 | implementation | [INIT-IMP-006-web-application-bundle](v4.0/implementation/INIT-IMP-006-web-application-bundle/README.md) | [RZN-001-P4-WEB-N01](../evidence/non-authoritative/realizations/v4.0/01-RZN-001-P4-WEB-browser-bundle.md) | initiative/v4.0-INIT-IMP-006-web-application-bundle | dedicated | v4.0 | 36bb20c88802191e13b873a36a07531fcfab5f42 | v4.0 | 2 | [Proposed lifecycle and migration history](v4.0/implementation/INIT-IMP-006-web-application-bundle/README.md) | Pending; [preparation recovery; no closure or merge](decision-receipts/EX-VSG-VER-001-migration-verification.md) |

## Historical assignments

[Cycle 1 allocations and immutable historical bases](legacy-correlation-index.md) preserve the old tuple register. [Migration authority](decision-receipts/EX-VSG-DR-001-initiative-migration.md), [scope registry](version-scopes.md) and [migration ledger](version-scope-migration-ledger.md) own the adoption mapping. Each current assignment is cycle 2; claims remain Proposed.

## Update rules

Reuse a suitable scope and catalog under specification 09; allocate initiative IDs independently. Preserve assignment history and exact source routing; use a new recorded cycle for reassignment. Shared branches need explicit placement and initiative-specific traceability. Scope READMEs and status views link here without creating competing membership authority.
