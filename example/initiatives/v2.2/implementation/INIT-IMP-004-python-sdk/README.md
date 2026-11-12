# Python SDK artifact initiative

**Initiative:** Python SDK artifact

**Initiative ID:** `INIT-IMP-004`

**Status:** Proposed

**Last updated:** 2026-11-11

**Initiative type:** `implementation`

**Work version:** `v2.2`

**Realization suite ID:** `RZN-001-P2-SDK-SUITE`

**Historical dedicated branch:** `initiative/v2.2-python-sdk`

**Captured base:** `v1` at `5a0ea0bd9f51edf97f9eddd39c6a3509c271503b`

**Version scope:** `v2.2`
**Source notes:** [RZN-001-P2-SDK-N01](../../../../evidence/non-authoritative/realizations/v2.2/01-RZN-001-P2-SDK-v2.2-python-sdk.md)
**Execution branch:** `initiative/v2.2-INIT-IMP-004-python-sdk`
**Execution mode:** dedicated
**Captured base ref:** `v2.2`
**Captured base commit:** `36bb20c88802191e13b873a36a07531fcfab5f42`
**Integration target:** `v2.2`
**Revision cycle:** 2
**Claim revision:** Existing Proposed claim, unchanged by migration
**Prior revision record:** [Cycle 1 allocation and assignment](../../../legacy-correlation-index.md)
**Governing revision:** `873021eef226576aebfc60b94f69886eb4da4a1c`
**Preparation recovery:** [Branch checkout and baseline availability](../../../decision-receipts/EX-VSG-VER-001-migration-verification.md)

## Historical correlation and identity

- [Canonical correlation row](../../../initiative-index.md#initiative-and-correlation-register)
- [Realization suite](../../../../evidence/non-authoritative/realizations/v2.2/00-RZN-001-P2-SDK-suite-index.md)
- [Migration ledger](../../../version-correlation-migration-ledger.md#migration-ledger)
- Preparation commit: `9ea472f8287a38f324edce41662a07058e1bd5e1`
- Predecessor or successor: none

The tuple is immutable and the realization suite remains non-authoritative.

## Protocol vocabulary

The lifecycle state is `Proposed`. Readiness, compatibility, qualification,
release, and completion are later evidence-backed claims, not synonyms for
having this documentation.

## Initiative type and output boundary

This implementation initiative may eventually deliver one immutable Python
wheel, its source, metadata, docs/examples, and D4 verification evidence. It
cannot deliver the D3 server, D5 CLI, D2 platform, or D6 web application.

## Narrow scope and nesting

Strict models, public methods, exceptions, validated private transport, retry
rules, packaging, typing, and documentation form one D4 artifact/completion
boundary. No child initiative exists; `SDK-06` retains split review.

## Products and placement

No destination is selected. `SDK-01` governs exact source, wheel, metadata,
docs, examples, and evidence paths. A product record is required before any
delivery claim.

## Proposal source

The frozen input is [proposal/proposal.md](proposal/proposal.md); the
[source inventory](proposal/README.md) preserves standing and precedence.

## Reading order

1. This README and [scope assessment](scope-assessment.md).
2. [Assumptions](assumption.md) and [open decisions](open-questions.md).
3. [Architecture/specification](architecture.md) and [mapping](source-mapping.md).
4. [Roadmap](implementation-roadmap.md) and [delivery steps](implementation-steps.md).

## Optional supporting documents

None. Add only records demanded by a later governed workflow.

## Implementation-readiness review

Not performed. Stage 5 reviews assumptions and Stage 6 resolves blocking
`SDK-*` choices through explicit human authority.

## Delivery, execution, and completion records

None exist. No wheel, compatibility, conformance, release, or downstream CLI
claim is created by this suite.

## Human decision receipts

No initiative-local human decision has been resolved.

## Reusable prompts

Stages 0–4 are complete. The Proposed record remains one D4 initiative: no
split was introduced and no assumption or `SDK-*` question was resolved. The
next workflow stage is Stage 5 assumption-confirmation review.

## Repository baseline

At the captured base the example contains contracts and realization notes, not
a governed D4 SDK product or built wheel.

## Intended outcome

A strict, typed, immutable Python wheel that faithfully exposes the D3 API
contract, validates URLs and inputs, maps errors predictably, retries only safe
reads, and supports exact compatible mock/live evidence.

## Scope

### Included

Public models/methods/exceptions, private transport, URL and response
validation, read-only retry policy, packaging, typing/docs/examples,
compatibility, security, and SDK-001 through SDK-008 plus applicable vectors.

### Excluded

Server/SQLite implementation, write retries, public transport internals, host
runtime prerequisites, CLI/web behavior, production/regulated deployment,
actual or possible ePHI, and unresolved artifact/tool choices.

## Dependencies

D4 uses D2 build/test targets and a compatible D3 API. D5 may consume only the
declared public wheel. Dependencies do not transfer lifecycle or completion.

## Readiness

Not implementation-ready: assumptions await review and `SDK-01` through
`SDK-06` remain open.

## Initiative lifecycle

### Lifecycle history

| Effective date or event | From | To | Authority or evidence | Claim revision | Reason and affected scope | Git commit |
|---|---|---|---|---|---|---|
| 2026-11-11 | Initial | Proposed | [realization suite](../../../../evidence/non-authoritative/realizations/v2.2/00-RZN-001-P2-SDK-suite-index.md) and [canonical row](../../../initiative-index.md#initiative-and-correlation-register) | Preparation skeleton | Allocate the migrated D4 tuple; no delivery authority | `9ea472f8287a38f324edce41662a07058e1bd5e1` |

## Initiative record maintenance

Reconcile future decisions across all affected records. Lifecycle changes
require human authority, required receipts, and coherent index/status updates.

## Authority and conflict discipline

Authoritative evidence is read-only and controls over realization detail,
generated artifacts, or convenience. Conflicts block the affected claim.


## Version-scope migration and provenance

[EX-VSG-DR-001](../../../decision-receipts/EX-VSG-DR-001-initiative-migration.md) migrates the complete suite and records the continuation assignment. The exact outcome, type, ownership, unresolved assumptions/questions and Proposed lifecycle standing remain unchanged. The historical tuple above remains cycle 1 evidence; the canonical index now owns scope membership. Independent outcomes may share this scope or source with separate complete initiative records.

| Suite ID | Suite path | Source ID | Source scope | Source path | Disposition | Routing evidence |
| --- | --- | --- | --- | --- | --- | --- |
| RZN-001-P2-SDK-SUITE | [Original suite](../../../../evidence/non-authoritative/realizations/v2.2/00-RZN-001-P2-SDK-suite-index.md) | RZN-001-P2-SDK-N01 | v2.2 | [RZN-001-P2-SDK-N01](../../../../evidence/non-authoritative/realizations/v2.2/01-RZN-001-P2-SDK-v2.2-python-sdk.md) | Originate | [Migration placement and rationale](../../../decision-receipts/EX-VSG-DR-001-initiative-migration.md) |

No source or accepted claim changes, no cross-scope routing and no reopening occur. Before Stage 5, preparation recovery must verify the current migrated suite and adopted scaffold on the assigned checkout. The new ref alone is not a ready handoff. Human review and acceptance gates remain open.
