# TADp version scopes

This is the canonical scope identity, topology and closure registry. Scope
READMEs and status views link here; each initiative README owns its lifecycle.
Scopes are coordination containers, not collective specifications or releases.

**Governing revision:** 6120bd10bb2e368274fd5bd4ff5481d33f61c4c6

**Reopening evidence:** None; first allocation is new and reopens no scope

| Scope | Kind | Structural parent | Integration branch | Captured base ref | Captured base commit | Integration target | Source catalog | Members | Child scopes | Closure disposition | Integration state | Closure evidence | Merge evidence | Governing revision |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v2 | Major | v1 | v2 | v1 | 9c9fd1daad655fd58349c005f8d31a4f52790cc9 | v1 | [RZN-SUITE-001](../evidence/non-authoritative/realizations/v2/00-review-decisions-suite-index.md), [RZN-001](../evidence/non-authoritative/realizations/v2/RZN-001-owned-review-decisions.md) | [TADP-001](v2/implementation/tadp-001-owned-review-decisions/README.md) | None | Open | Not integrated; no merge authority | Not applicable; open | None | 6120bd10bb2e368274fd5bd4ff5481d33f61c4c6 |

Canonical scopes are exact vN, vN.M or vN.M.P with non-negative decimal
components and no leading zeros except 0. Compare numerically without
normalizing identities. Major/minor/patch parents are structural and creation
bases never change after allocation. Zero members is valid without delivery
authority. Preserve additions, reopenings, branch removals and historical bases.

## Scope event history

| Event | Scope | Prior disposition | New disposition | Instruction and actual decision author | Snapshot or revision | Consequences and record links | Git commit |
|---|---|---|---|---|---|---|---|
| 2026-11-14 allocation | v2 | Not allocated | Open | [Exact invocation and Codex delegated placement](../evidence/non-authoritative/assumption-question-review/intake.md); [base appointment](../decisions/INTEGRATION-001.md) | v1 at 9c9fd1daad655fd58349c005f8d31a4f52790cc9 | One new Proposed member; no reopening, acceptance or integration | See scoped Stage 0 allocation commit |

Closing one member never closes a scope. Scope closure needs all member and
child dispositions, successful required integration, aggregate checks and
coherence/conflict reconciliation. Accepted deliverables must be integrated or
have explicitly authorized exclusion/transfer. Reopening and reintegration
remain per-event records; no silent ancestor reopening or closure.

Each scope or ancestor reopening has its own receipt declaring Disposition:
Reopened, exact Scope and actual Human authority/intake delegation. Link every
applicable event from Reopening evidence; the event table alone is insufficient.

## Installation inventory

This section preserves the setup event. The first later allocation is v2 above;
installation itself allocated none of these records.

No scopes, realization notes, initiatives, prior decisions, products, or lifecycle
claims were imported or allocated. The setup authority and verification records
are linked from [SETUP-001](../decisions/SETUP-001.md). Existing upstream work and
Git branch names do not become this project's membership. Ownership follows the current repository owner under OWNERSHIP-001; prospective adoption is recorded in [the profile](../project-profile.md) under ADOPTION-001.
