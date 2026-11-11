# TADp protocol initiative status

**Status owner:** User

**Last reviewed:** 2026-11-11

**Review cadence:** At every initiative lifecycle or gate change

## Authority boundary

This record summarizes current lifecycle standing and gates. Each initiative
README remains authoritative for its detailed scope, decisions, and lifecycle.
The [initiative index](initiative-index.md) owns canonical project-level tuple
correlation. A row here does not create acceptance, delivery, completion, or
release standing.

## Current status

| Work version | Initiative ID | Suite | Type | Status | Current milestone | Next gate | Blockers or holds | Status evidence | Owner | Last updated |
|---|---|---|---|---|---|---|---|---|---|---|
| v1.0 | INIT-DSN-001 | [RZN-TADP-001-VERSION-CORRELATION-SUITE](../evidence/non-authoritative/realizations/v1.0/00-RZN-TADP-001-VERSION-CORRELATION-suite-index.md) | design | Superseded | Prior proposal baseline 0.2 retained as historical material; direct work transferred to the named repository prompt | None for this initiative; explicit reopening authority would be required | VRC-01 and VRC-02 remain historical unresolved questions but do not govern the replacement revision | [Lifecycle history](design/INIT-DSN-001-version-realization-correlation/README.md#initiative-lifecycle); [VRC-DR-001](design/INIT-DSN-001-version-realization-correlation/decision-receipts/VRC-DR-001-supersede-prior-initiative.md); [canonical correlation row](initiative-index.md#initiative-and-correlation-register) | User | 2026-11-11 |

## Portfolio gates

| Gate ID | Outcome required | Depends on | Evidence required | Owner | State |
|---|---|---|---|---|---|
| TADP-CORR-GATE-01 | Historical acceptance gate for the superseded v1.0 design plan | INIT-DSN-001 remained Proposed and was superseded | [VRC-DR-001](design/INIT-DSN-001-version-realization-correlation/decision-receipts/VRC-DR-001-supersede-prior-initiative.md) | User | Superseded; never accepted |
| TADP-CORR-GATE-02 | Historical separate-validator gate from the superseded type split | No successor initiative was allocated; direct validator work is now bounded by the named repository prompt | [VRC-DR-001](design/INIT-DSN-001-version-realization-correlation/decision-receipts/VRC-DR-001-supersede-prior-initiative.md) and [replacement prompt](../../prompts/version-realization-initiative-correlation-protocol-change.md) | User | Superseded; no implementation claim |

## Maintenance rules

- Update status only from current initiative and verification evidence.
- Record only legal lifecycle states and transitions; Reopened is an event.
- Link blockers to the record that owns their resolution.
- Retain terminal rows until a separately recorded retention rule permits
  archival.
- Reconcile this view with the initiative index and affected README in the same
  reviewed change.
