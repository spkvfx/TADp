# Container platform and runtime packaging initiative

**Initiative:** Container platform and runtime packaging

**Initiative ID:** `INIT-IMP-002`

**Status:** Proposed

**Last updated:** 2026-11-11

**Initiative type:** `implementation`

**Decision prefix:** `PLT`

**Work version:** `v2.0`

**Realization suite ID:** `RZN-001-P2-PLATFORM-SUITE`

**Realization suite:** [Container platform realization suite](../../../../evidence/non-authoritative/realizations/v2.0/00-RZN-001-P2-PLATFORM-suite-index.md)

**Canonical project correlation:** [initiative and correlation register](../../../initiative-index.md#initiative-and-correlation-register)

**Historical dedicated branch:** `initiative/v2.0-container-platform`

**Historical captured base branch:** `v1`

**Historical captured base commit:** `5a0ea0bd9f51edf97f9eddd39c6a3509c271503b`

**Predecessor or successor:** None

**Historical correlation governance:** `007e791750a7dd5bca1befabd88cf83defde14b4` and the [migration ledger](../../../version-correlation-migration-ledger.md)

**Human ownership:** Apply the [project ownership convention](../../../../project-profile.md).
The User is the Sole Project Owner; platform, security, artifact, and evidence
responsibilities remain explicit.

This initiative proposes the D2 build, Compose, image, hardening, artifact
identity, and safe lifecycle product family required by architecture `2.0.1`.
It supplies independently reviewable platform behavior without implementing or
completing D3–D6.

**Version scope:** `v2.0`
**Source notes:** [RZN-001-P2-PLATFORM-N01](../../../../evidence/non-authoritative/realizations/v2.0/01-RZN-001-P2-PLATFORM-v2.0-container-platform.md)
**Execution branch:** `initiative/v2.0-INIT-IMP-002-container-platform`
**Execution mode:** dedicated
**Captured base ref:** `v2.0`
**Captured base commit:** `36bb20c88802191e13b873a36a07531fcfab5f42`
**Integration target:** `v2.0`
**Revision cycle:** 2
**Claim revision:** Existing Proposed claim, unchanged by migration
**Prior revision record:** [Cycle 1 allocation and assignment](../../../legacy-correlation-index.md)
**Governing revision:** `873021eef226576aebfc60b94f69886eb4da4a1c`
**Preparation recovery:** [Branch checkout and baseline availability](../../../decision-receipts/EX-VSG-VER-001-migration-verification.md)

## Historical correlation and identity

The index owns the immutable `v2.0` / suite / `INIT-IMP-002` / branch
tuple. The dated migration addendum preserves the pre-effective suite's
historical standing. This copy creates no acceptance or delivery authority.

## Protocol vocabulary

Specification means this initiative-scoped direction; product means the future
platform artifacts. Repository authoritative evidence governs both.
Non-authoritative realization evidence supplies proposal context only.

## Initiative type and output boundary

This `implementation` initiative may create platform products and their
product documentation. It must not change an accepted specification or absorb
API/domain, SDK, CLI, or web product behavior.

## Narrow scope and nesting

One D2 platform outcome and one platform qualification claim are owned here.
[Scope assessment](scope-assessment.md) rechecks every split trigger; a
separable platform product must receive its own tuple.

## Products and placement

| Product | Form | Destination | Governing specification | Verification |
|---|---|---|---|---|
| Container platform and runtime packaging | BuildKit graph, Compose model, image targets, locks, release metadata, and runbooks | Open — `PLT-01` | `ADR-004`, `ADR-005`, `ARC-CTR-008`, and security suites | All `CNT-*`, applicable `OPS-*`, `E2E-009`, and exact policy evidence |

## Proposal source

[Proposal sources](proposal/README.md) inventories the canonical
[proposal](proposal/proposal.md), realization, and authoritative inputs.
Corrections belong in assumptions or stable decisions.

## Reading order

1. Proposal and source inventory.
2. [Assumptions](assumption.md).
3. [Scope assessment](scope-assessment.md).
4. [Architecture](architecture.md).
5. [Evidence mapping](source-mapping.md).
6. [Open questions](open-questions.md).
7. [Roadmap](implementation-roadmap.md).
8. [Delivery steps](implementation-steps.md).

## Optional supporting documents

None initially. Later risk, build/release, host/media, recovery, activity, and
incident records are created only in their named execution/evidence stages.

## Implementation-readiness review

Not created. A later accepted initiative must complete it immediately before
product execution.

## Delivery, execution, and completion records

No execution or completion record exists; no platform product or passing result
is claimed.

## Human decision receipts

No initiative-local receipt exists because no assumption, question, or
lifecycle decision has been resolved.

## Reusable prompts

Stages 0–4 are complete. The Proposed record remains one D2 initiative: no
split was introduced and no assumption or `PLT-*` question was resolved. The
next workflow stage is Stage 5 assumption-confirmation review.

## Repository baseline

- `ADR-004` fixes the Compose-only local trust and hardened runtime boundary.
- `ADR-005` fixes the multi-stage technology/build/release graph.
- `ARC-CTR-008/009` fix topology, operations, D2 vectors, and evidence fields.
- NIST/HIPAA `1.0.1` independently govern security, data/use, and claim gates.

## Intended outcome

One exact, digest-identified platform builds and runs only accepted roles,
confines state and network access, enforces hardening and safe lifecycle
boundaries, and supplies reviewable artifacts without claiming D3–D6 behavior.

## Scope

### Included

- Build, Compose, targets, images, private network, named volumes, hardening,
  configuration, health envelope, lifecycle, and artifact traceability.
- D2 host/platform/supply-chain/security qualification planning.

### Excluded

- Domain/API/SQLite semantics, SDK behavior, CLI grammar, and web behavior.
- Host-native fallback, remote/public operation, production/ePHI use, and
  routine destructive volume commands.

## Dependencies

| Initiative or contract | Relationship | Required state |
|---|---|---|
| Architecture/security suites | Binding platform and policy contracts | Accepted exact revisions |
| D3–D6 | Future consumers of D2 targets and topology | Independent; no completion is inferred |
| D1 | Possible derivative guidance | Not a prerequisite to authoritative platform contracts |

## Readiness

| Area | Current evidence | Required before the next initiative output |
|---|---|---|
| Product direction | D2 boundary and topology fixed | Resolve `PLT-01`–`PLT-06` |
| Repository fit | No product paths selected | Accept exact destinations and generated/owned paths |
| Data and migration | Volume/recovery envelope fixed | Preserve D3 ownership; approve synthetic fixtures |
| Operations and recovery | Lifecycle and destructive boundaries fixed | Define exact commands, matrix, rollback, and evidence |
| Verification | D2 vectors and policies fixed | Select exact tools, environments, and evidence destinations |

## Initiative lifecycle

### Lifecycle history

| Effective date or event | From | To | Authority or evidence | Claim revision | Reason and affected scope | Git commit |
|---|---|---|---|---|---|---|
| 2026-11-11 | Initial | Proposed | [realization suite](../../../../evidence/non-authoritative/realizations/v2.0/00-RZN-001-P2-PLATFORM-suite-index.md) and [canonical row](../../../initiative-index.md#initiative-and-correlation-register) | Preparation skeleton | Allocate the migrated D2 tuple; no acceptance or delivery authority | `d888ea74d36477ba2a192c1eb5531aca6003fe25` |

## Initiative record maintenance

Reconcile every explicit decision across all affected records. Lifecycle
changes require human authority, a receipt, and status/index updates.

## Authority and conflict discipline

Authoritative evidence remains read-only. Any conflicting product convenience
blocks affected work and routes to the owning specification workflow.


## Version-scope migration and provenance

[EX-VSG-DR-001](../../../decision-receipts/EX-VSG-DR-001-initiative-migration.md) migrates the complete suite and records the continuation assignment. The exact outcome, type, ownership, unresolved assumptions/questions and Proposed lifecycle standing remain unchanged. The historical tuple above remains cycle 1 evidence; the canonical index now owns scope membership. Independent outcomes may share this scope or source with separate complete initiative records.

| Suite ID | Suite path | Source ID | Source scope | Source path | Disposition | Routing evidence |
| --- | --- | --- | --- | --- | --- | --- |
| RZN-001-P2-PLATFORM-SUITE | [Original suite](../../../../evidence/non-authoritative/realizations/v2.0/00-RZN-001-P2-PLATFORM-suite-index.md) | RZN-001-P2-PLATFORM-N01 | v2.0 | [RZN-001-P2-PLATFORM-N01](../../../../evidence/non-authoritative/realizations/v2.0/01-RZN-001-P2-PLATFORM-v2.0-container-platform.md) | Originate | [Migration placement and rationale](../../../decision-receipts/EX-VSG-DR-001-initiative-migration.md) |

No source or accepted claim changes, no cross-scope routing and no reopening occur. Before Stage 5, preparation recovery must verify the current migrated suite and adopted scaffold on the assigned checkout. The new ref alone is not a ready handoff. Human review and acceptance gates remain open.

## Administrative addendum: verified preparation recovery

On 2026-11-12, [EX-PREP-DR-001](../../../decision-receipts/EX-PREP-DR-001-branch-recovery.md)
recorded the User-authorized history repair and exact baseline installation.
The actual assigned checkout, initiative/v2.0-INIT-IMP-002-container-platform,
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
