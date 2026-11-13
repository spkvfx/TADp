# API and SQLite runtime image initiative

**Initiative:** API and SQLite runtime image

**Initiative ID:** `INIT-IMP-003`

**Status:** Proposed

**Last updated:** 2026-11-11

**Initiative type:** `implementation`

**Work version:** `v2.1`

**Realization suite ID:** `RZN-001-P2-API-SQLITE-SUITE`

**Historical dedicated branch:** `initiative/v2.1-api-sqlite-runtime`

**Captured base:** `v1` at `5a0ea0bd9f51edf97f9eddd39c6a3509c271503b`

**Version scope:** `v2.1`
**Source notes:** [RZN-001-P2-API-SQLITE-N01](../../../../evidence/non-authoritative/realizations/v2.1/01-RZN-001-P2-API-SQLITE-v2.1-api-runtime.md)
**Execution branch:** `initiative/v2.1-INIT-IMP-003-api-sqlite-runtime`
**Execution mode:** dedicated
**Captured base ref:** `v2.1`
**Captured base commit:** `36bb20c88802191e13b873a36a07531fcfab5f42`
**Integration target:** `v2.1`
**Revision cycle:** 2
**Claim revision:** Existing Proposed claim, unchanged by migration
**Prior revision record:** [Cycle 1 allocation and assignment](../../../legacy-correlation-index.md)
**Governing revision:** `873021eef226576aebfc60b94f69886eb4da4a1c`
**Preparation recovery:** [Branch checkout and baseline availability](../../../decision-receipts/EX-VSG-VER-001-migration-verification.md)

## Historical correlation and identity

- [Canonical correlation row](../../../initiative-index.md#initiative-and-correlation-register)
- [Realization suite](../../../../evidence/non-authoritative/realizations/v2.1/00-RZN-001-P2-API-SQLITE-suite-index.md)
- [Migration ledger](../../../version-correlation-migration-ledger.md#migration-ledger)
- Preparation commit: `eaebb511c49c4f451af8516504763d9529b00967`
- Predecessor or successor: none

The tuple is immutable. The suite remains non-authoritative and supplies
planning input only.

## Protocol vocabulary

`Proposed` is the current lifecycle state. “Ready,” “qualified,” “compatible,”
“released,” and “complete” are claims that require later evidence and authority;
they are not implied here.

## Initiative type and output boundary

This implementation initiative may eventually deliver one immutable D3
API/SQLite runtime image, source, migrations, maintenance tooling, and D3
verification evidence. It cannot deliver D2, D4, D5, or D6 outcomes.

## Narrow scope and nesting

The domain, HTTP API, search/navigation, SQLite, health, maintenance, and
same-origin static-hosting slot are one cohesive D3 artifact and completion
boundary. No subinitiative is created. `API-06` keeps mandatory split triggers
open.

## Products and placement

No product destination has been chosen. `API-01` governs exact source, image,
migration, maintenance, static, and evidence paths. A future product record
must be linked before any delivery claim.

## Proposal source

The frozen working proposal is [proposal/proposal.md](proposal/proposal.md).
Its [source inventory](proposal/README.md) preserves authority and standing.

## Reading order

1. This README and [scope assessment](scope-assessment.md).
2. [Assumptions](assumption.md) and [open decisions](open-questions.md).
3. [Architecture/specification](architecture.md) and [source mapping](source-mapping.md).
4. [Delivery roadmap](implementation-roadmap.md) and [steps](implementation-steps.md).

## Optional supporting documents

None. Add only governed records required by an actual later workflow.

## Implementation-readiness review

Not performed. Stage 5 must review assumptions; Stage 6 must resolve blocking
questions through explicit human authority and receipts where required.

## Delivery, execution, and completion records

None exist. This record creates no implementation, conformance, release,
deployment, or downstream compatibility claim.

## Human decision receipts

No initiative-local human decision has been resolved. The project-root
exception receipt governs repository mechanics only.

## Reusable prompts

Stages 0–4 are complete. The Proposed record remains one D3 initiative: no
split was introduced and no assumption or `API-*` question was resolved. The
next workflow stage is Stage 5 assumption-confirmation review.

## Repository baseline

The example is documentation/protocol material. No D3 product source or image
is present at the captured base.

## Intended outcome

A contract-faithful, locally operated D3 image with deterministic domain,
API, search, navigation, persistence, migration, health, maintenance, recovery,
and static-hosting-boundary behavior.

## Scope

### Included

- Domain and `/api/v1` behavior.
- SQLite schema, migrations, constraints, backup/restore, and maintenance.
- Search, navigation, errors, concurrency, health, and bounded observability.
- D3 security and applicable DOM/HTTP/SRCH/NAV/DB/CNT/OPS/E2E evidence.

### Excluded

- D2 platform qualification and D4-D6 product behavior.
- Remote, multi-user, production, or regulated deployment.
- Actual or possible ePHI and any unsupported compliance claim.
- Selected destinations, dependency locks, tools, owners, or split decisions.

## Dependencies

D3 consumes a separately governed compatible D2 platform. D4-D6 may consume
D3 only through declared interfaces. Dependency never transfers lifecycle,
authority, acceptance, or completion.

## Readiness

The specification is traceable but not implementation-ready: all assumptions
await review and `API-01` through `API-06` remain open.

## Initiative lifecycle

### Lifecycle history

| Effective date or event | From | To | Authority or evidence | Claim revision | Reason and affected scope | Git commit |
|---|---|---|---|---|---|---|
| 2026-11-11 | Initial | Proposed | [realization suite](../../../../evidence/non-authoritative/realizations/v2.1/00-RZN-001-P2-API-SQLITE-suite-index.md) and [canonical row](../../../initiative-index.md#initiative-and-correlation-register) | Preparation skeleton | Allocate the migrated D3 tuple; no delivery authority | `eaebb511c49c4f451af8516504763d9529b00967` |

## Initiative record maintenance

Reconcile future explicit decisions across every affected record. Lifecycle
changes require human authority, status/index updates, and required receipts.

## Authority and conflict discipline

Authoritative evidence remains read-only and prevails over realization notes
or product convenience. A conflict blocks the affected claim and routes to the
owning specification workflow.


## Version-scope migration and provenance

[EX-VSG-DR-001](../../../decision-receipts/EX-VSG-DR-001-initiative-migration.md) migrates the complete suite and records the continuation assignment. The exact outcome, type, ownership, unresolved assumptions/questions and Proposed lifecycle standing remain unchanged. The historical tuple above remains cycle 1 evidence; the canonical index now owns scope membership. Independent outcomes may share this scope or source with separate complete initiative records.

| Suite ID | Suite path | Source ID | Source scope | Source path | Disposition | Routing evidence |
| --- | --- | --- | --- | --- | --- | --- |
| RZN-001-P2-API-SQLITE-SUITE | [Original suite](../../../../evidence/non-authoritative/realizations/v2.1/00-RZN-001-P2-API-SQLITE-suite-index.md) | RZN-001-P2-API-SQLITE-N01 | v2.1 | [RZN-001-P2-API-SQLITE-N01](../../../../evidence/non-authoritative/realizations/v2.1/01-RZN-001-P2-API-SQLITE-v2.1-api-runtime.md) | Originate | [Migration placement and rationale](../../../decision-receipts/EX-VSG-DR-001-initiative-migration.md) |

No source or accepted claim changes, no cross-scope routing and no reopening occur. Before Stage 5, preparation recovery must verify the current migrated suite and adopted scaffold on the assigned checkout. The new ref alone is not a ready handoff. Human review and acceptance gates remain open.

## Administrative addendum: verified preparation recovery

On 2026-11-12, [EX-PREP-DR-001](../../../decision-receipts/EX-PREP-DR-001-branch-recovery.md)
recorded the User-authorized history repair and exact baseline installation.
The actual assigned checkout, initiative/v2.1-INIT-IMP-003-api-sqlite-runtime,
was verified at 12bddc8d978b44e0761a0d9bf448f379c163ccf1: the current
canonical suite, adopted ancestry, protection and full validation/local links
passed. [Actual results](../../../decision-receipts/EX-VSG-VER-001-migration-verification.md#ex-prep-001-verified-recovery-results)
supersede the earlier missing-preparation blocker. Final administrative
tracking updates preserve that baseline's source and protected content.

This initiative remains Proposed with its original source dispositions,
creation base, cycle 2 assignment, provenance and narrow claim unchanged.
The next stage is template 05, followed by 06 under the separate authorized
review method and D1-D6 order. No source review, initiative acceptance,
delivery, scope closure or upward integration is claimed here.
