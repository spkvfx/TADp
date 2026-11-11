# Standalone CLI image initiative

**Initiative:** Standalone CLI image

**Initiative ID:** `INIT-IMP-005`

**Status:** Proposed

**Last updated:** 2026-11-11

**Initiative type:** `implementation`

**Work version:** `v3.0`

**Realization suite ID:** `RZN-001-P3-CLI-SUITE`

**Dedicated branch:** `initiative/v3.0-standalone-cli-image`

**Captured base:** `v1` at `5a0ea0bd9f51edf97f9eddd39c6a3509c271503b`

## Correlation and identity

- [Canonical row](../../initiative-index.md#initiative-and-correlation-register)
- [Realization suite](../../../evidence/non-authoritative/realizations/v3.0/00-RZN-001-P3-CLI-suite-index.md)
- [Migration ledger](../../version-correlation-migration-ledger.md#migration-ledger)
- Preparation commit: `af45ea7b2d98decd875eb793fadc16558ffae764`
- Predecessor or successor: none

The tuple is immutable; realization evidence remains non-authoritative.

## Protocol vocabulary

The state is `Proposed`. Ready, usable, compatible, qualified, released, and
complete require later authority/evidence.

## Initiative type and output boundary

This implementation initiative may eventually deliver CLI source, help and
completion, one immutable one-shot image, metadata, and D5 evidence. It cannot
deliver D2-D4 or D6 outcomes.

## Narrow scope and nesting

Parsing, commands, public-SDK dispatch, output, exit codes, signals/pipes,
image packaging, help/completion, and D5 qualification form one product
boundary. No child exists; `CLI-06` retains split review.

## Products and placement

No destination is selected. `CLI-01` owns exact source, help/completion, image,
metadata, and evidence paths; a product record is required before delivery.

## Proposal source

[proposal/proposal.md](proposal/proposal.md) is frozen Stage 1 input. Its
[source inventory](proposal/README.md) preserves standing and precedence.

## Reading order

1. README and [scope assessment](scope-assessment.md).
2. [Assumptions](assumption.md) and [questions](open-questions.md).
3. [Architecture](architecture.md) and [mapping](source-mapping.md).
4. [Roadmap](implementation-roadmap.md) and [steps](implementation-steps.md).

## Optional supporting documents

None; create later records only when a governed workflow requires them.

## Implementation-readiness review

Not performed. Stage 5 reviews assumptions and Stage 6 resolves blockers.

## Delivery, execution, and completion records

None exist. No CLI image, compatibility, usability, conformance, release, or
deployment claim is made.

## Human decision receipts

No initiative-local human decision has been resolved.

## Reusable prompts

Stages 0–3 are complete. Stage 4 may align this Proposed record without
resolving assumptions or `CLI-*` questions.

## Repository baseline

The captured base contains contracts and notes, not a governed D5 product.

## Intended outcome

A one-shot Compose CLI image using only the exact D4 public wheel against
`record-api:8000/api/v1`, with deterministic commands, output, exit codes,
signals, broken-pipe behavior, and safe diagnostics.

## Scope

### Included

Commands/parser/validation, help/completion, human/JSON rendering, error and
exit mapping, signals/pipes, image/package metadata, compatibility, security,
and CLI-001 through CLI-011 plus applicable vectors.

### Excluded

Direct HTTP/SQLite/internal SDK use, mounts, ports, Docker socket, long-running
service behavior, D2-D4/D6 delivery, remote production/regulated use, ePHI,
and unresolved paths/tools/versions/owners.

## Dependencies

D5 consumes exact D2, D3, and D4 artifacts. D6 is independent. Dependency does
not aggregate lifecycle or completion.

## Readiness

Not implementation-ready; assumptions await review and `CLI-01`-`CLI-06` are
open.

## Initiative lifecycle

### Lifecycle history

| Effective date or event | From | To | Authority or evidence | Claim revision | Reason and affected scope | Git commit |
|---|---|---|---|---|---|---|
| 2026-11-11 | Initial | Proposed | [realization suite](../../../evidence/non-authoritative/realizations/v3.0/00-RZN-001-P3-CLI-suite-index.md) and [canonical row](../../initiative-index.md#initiative-and-correlation-register) | Preparation skeleton | Allocate the migrated D5 tuple; no delivery authority | `af45ea7b2d98decd875eb793fadc16558ffae764` |

## Initiative record maintenance

Reconcile decisions across every affected record. Lifecycle changes require
human authority, required receipts, and coherent index/status updates.

## Authority and conflict discipline

Read-only authoritative evidence controls. Conflicts with notes, generated
artifacts, or convenience block affected work.
