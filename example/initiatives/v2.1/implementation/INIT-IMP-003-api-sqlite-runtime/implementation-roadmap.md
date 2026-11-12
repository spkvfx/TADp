# API and SQLite runtime image delivery roadmap

**Initiative:** `INIT-IMP-003`
**Status:** Proposed planning only
**Last updated:** 2026-11-11

## Objective

Sequence a future D3 delivery without implying authorization, completion, or
release.

## Delivery scope

### Included

One D3 source/build graph, runtime image, database lifecycle, maintenance
surface, and exact D3 verification evidence.

### Excluded from this roadmap

D2 qualification, D4-D6 delivery, remote/production operation, regulated data,
and any unresolved placement or ownership choice.

## Type-specific delivery boundary

Implementation work begins only after lifecycle authority and blocking decisions.
A later product record must own artifact destinations and release evidence.

## Prerequisites

- Assumptions reviewed.
- `API-01` through `API-06` resolved as required.
- Compatible D2 interface identified.
- Authoritative source currency and security/data gates reviewed.

## Phase summary

| Phase | Outcome | Entry gate | Exit evidence |
|---|---|---|---|
| 0 | Specification and placement authorized | Human review | Traceable decisions and product map |
| 1 | Domain/API/persistence core | Phase 0 | Contract and DB evidence |
| 2 | Operations and recovery | Phase 1 | Health, migration, backup/restore evidence |
| 3 | D3 qualification | Phase 2 | Complete artifact-bound D3 evidence |

## Phase 0 - Authorize specification and output boundary

### Objective

Resolve blocking assumptions, decisions, ownership, destinations, and matrix.

### Work

Review scope, source mapping, security/data use, compatibility, and evidence
retention; create required product and decision records.

### Exit gate

Explicit authority exists and no required D3 decision is silently open.

## Phase 1 - Implement domain API and persistence

### Objective

Build the record-domain, HTTP, search/navigation, and SQLite behavior.

### Work

Implement validated models, services, problems, query/navigation, schema,
transactions, and clean initialization using locked inputs.

### Exit gate

Applicable DOM/HTTP/SRCH/NAV/DB evidence passes for the exact artifact.

## Phase 2 - Implement operations and recovery

### Objective

Add health, maintenance, migration, backup/restore, fault behavior, and bounded
observability.

### Work

Exercise restart, lock, corruption, disk, interruption, rollback, and recovery
paths with synthetic/de-identified data.

### Exit gate

Applicable CNT/OPS/recovery evidence passes and security findings are dispositioned.

## Phase 3 - Qualify D3 outcome

### Objective

Assemble the complete traceable D3 conformance record.

### Work

Run clean-host/upgrade matrices, drift checks, scans, source-currency review,
and evidence completeness review.

### Exit gate

A human reviewer can evaluate D3 alone without relying on downstream claims.

## Rollout controls

Use immutable identities, narrow compatible matrices, backup-before-migration,
verified rollback/recovery, and explicit stop conditions for safety or evidence
gaps.

## Release definition

A release is an immutable D3 artifact plus locked inputs, compatibility
declaration, migration/maintenance material, security records, and complete
verification evidence. This roadmap creates none of those claims.
