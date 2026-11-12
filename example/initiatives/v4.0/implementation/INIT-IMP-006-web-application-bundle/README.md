# Web application bundle initiative

**Initiative:** Web application bundle

**Initiative ID:** `INIT-IMP-006`

**Status:** Proposed

**Last updated:** 2026-11-11

**Initiative type:** `implementation`

**Work version:** `v4.0`

**Realization suite ID:** `RZN-001-P4-WEB-SUITE`

**Historical dedicated branch:** `initiative/v4.0-web-application-bundle`

**Captured base:** `v1` at `5a0ea0bd9f51edf97f9eddd39c6a3509c271503b`

**Version scope:** `v4.0`
**Source notes:** [RZN-001-P4-WEB-N01](../../../../evidence/non-authoritative/realizations/v4.0/01-RZN-001-P4-WEB-browser-bundle.md)
**Execution branch:** `initiative/v4.0-INIT-IMP-006-web-application-bundle`
**Execution mode:** dedicated
**Captured base ref:** `v4.0`
**Captured base commit:** `36bb20c88802191e13b873a36a07531fcfab5f42`
**Integration target:** `v4.0`
**Revision cycle:** 2
**Claim revision:** Existing Proposed claim, unchanged by migration
**Prior revision record:** [Cycle 1 allocation and assignment](../../../legacy-correlation-index.md)
**Governing revision:** `873021eef226576aebfc60b94f69886eb4da4a1c`
**Preparation recovery:** [Branch checkout and baseline availability](../../../decision-receipts/EX-VSG-VER-001-migration-verification.md)

## Historical correlation and identity

- [Canonical row](../../../initiative-index.md#initiative-and-correlation-register)
- [Realization suite](../../../../evidence/non-authoritative/realizations/v4.0/00-RZN-001-P4-WEB-suite-index.md)
- [Migration ledger](../../../version-correlation-migration-ledger.md#migration-ledger)
- Preparation commit: `370ffcfa1bee8763a23ef5481716e6b093a11e42`
- Predecessor or successor: none

The tuple is immutable and the realization suite remains non-authoritative.

## Protocol vocabulary

The lifecycle state is `Proposed`. Accessible, secure, compatible, qualified,
released, and complete are later evidence-backed claims.

## Initiative type and output boundary

This implementation initiative may eventually deliver web source, manifest,
one immutable bundle, reports/traces, and D6 evidence. It cannot deliver the D2
platform, D3 API, or D5 CLI.

## Narrow scope and nesting

Record/search/navigation/edit/delete workflows, accessibility, same-origin API
state, asset build, help, security, and D6 qualification share one embedded
bundle/completion boundary. No child exists; `WEB-07` retains split review.

## Products and placement

No destination is selected. `WEB-01` governs source, manifest, compiled assets,
accessibility reports, traces, and evidence paths. A product record is required
before delivery.

## Proposal source

[proposal/proposal.md](proposal/proposal.md) is frozen Stage 1 input; its
[source inventory](proposal/README.md) preserves standing and precedence.

## Reading order

1. README and [scope assessment](scope-assessment.md).
2. [Assumptions](assumption.md) and [questions](open-questions.md).
3. [Architecture](architecture.md) and [mapping](source-mapping.md).
4. [Roadmap](implementation-roadmap.md) and [steps](implementation-steps.md).

## Optional supporting documents

None; add later records only when the governed workflow requires them.

## Implementation-readiness review

Not performed. Stage 5 reviews assumptions and Stage 6 resolves blockers.

## Delivery, execution, and completion records

None exist. No bundle, accessibility/security result, compatibility,
conformance, release, or deployment claim is made.

## Human decision receipts

No initiative-local human decision has been resolved.

## Reusable prompts

Stages 0–4 are complete. The Proposed record remains one D6 initiative: no
split was introduced and no assumption or `WEB-*` question was resolved. The
next workflow stage is Stage 5 assumption-confirmation review.

## Repository baseline

The base contains contracts/notes, not a governed D6 source or bundle.

## Intended outcome

An accessible, secure, container-built same-origin web bundle served by D3,
with complete record workflows and explicit loading, empty, error, stale,
conflict, cancellation, retry, and indeterminate states.

## Scope

### Included

Browser state/interaction, accessibility, same-origin API, immutable assets,
help, compatibility, source-map handling, security, and WEB-001..WEB-013 plus
applicable contract/security/accessibility evidence.

### Excluded

Separate server/container, host Node runtime, durable browser record storage,
third-party/remote assets, cross-origin API, D2/D3/D5 delivery, production or
regulated use, ePHI, and unresolved paths/framework/matrix/ownership.

## Dependencies

D6 consumes exact D2 and D3 artifacts. D5 sequencing is context only and D5 is
independent. Dependencies do not transfer lifecycle or completion.

## Readiness

Not implementation-ready; assumptions await review and `WEB-01`-`WEB-07` are
open.

## Initiative lifecycle

### Lifecycle history

| Effective date or event | From | To | Authority or evidence | Claim revision | Reason and affected scope | Git commit |
|---|---|---|---|---|---|---|
| 2026-11-11 | Initial | Proposed | [realization suite](../../../../evidence/non-authoritative/realizations/v4.0/00-RZN-001-P4-WEB-suite-index.md) and [canonical row](../../../initiative-index.md#initiative-and-correlation-register) | Preparation skeleton | Allocate the migrated D6 tuple; no delivery authority | `370ffcfa1bee8763a23ef5481716e6b093a11e42` |

## Initiative record maintenance

Reconcile explicit decisions across every affected record. Lifecycle changes
require human authority, required receipts, and coherent index/status updates.

## Authority and conflict discipline

Read-only authoritative evidence controls over realization detail, generated
assets, or convenience. Conflicts block affected work.


## Version-scope migration and provenance

[EX-VSG-DR-001](../../../decision-receipts/EX-VSG-DR-001-initiative-migration.md) migrates the complete suite and records the continuation assignment. The exact outcome, type, ownership, unresolved assumptions/questions and Proposed lifecycle standing remain unchanged. The historical tuple above remains cycle 1 evidence; the canonical index now owns scope membership. Independent outcomes may share this scope or source with separate complete initiative records.

| Suite ID | Suite path | Source ID | Source scope | Source path | Disposition | Routing evidence |
| --- | --- | --- | --- | --- | --- | --- |
| RZN-001-P4-WEB-SUITE | [Original suite](../../../../evidence/non-authoritative/realizations/v4.0/00-RZN-001-P4-WEB-suite-index.md) | RZN-001-P4-WEB-N01 | v4.0 | [RZN-001-P4-WEB-N01](../../../../evidence/non-authoritative/realizations/v4.0/01-RZN-001-P4-WEB-browser-bundle.md) | Originate | [Migration placement and rationale](../../../decision-receipts/EX-VSG-DR-001-initiative-migration.md) |

No source or accepted claim changes, no cross-scope routing and no reopening occur. Before Stage 5, preparation recovery must verify the current migrated suite and adopted scaffold on the assigned checkout. The new ref alone is not a ready handoff. Human review and acceptance gates remain open.
