# TADp protocol initiative status

**Status owner:** User

**Last reviewed:** 2026-11-10

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
| v1.0 | INIT-DSN-001 | [RZN-TADP-001-VERSION-CORRELATION-SUITE](../evidence/non-authoritative/realizations/v1.0/00-RZN-TADP-001-VERSION-CORRELATION-suite-index.md) | design | Proposed | Proposal aligned; initial initiative suite pending | Complete Stages 3-6, then request exact Stage 7 acceptance | Meaning-changing legacy mappings require explicit decisions; executable validator work requires a separate initiative | [Proposal revision 0.1](design/INIT-DSN-001-version-realization-correlation/proposal/proposal.md); [canonical correlation row](initiative-index.md#initiative-and-correlation-register) | User | 2026-11-10 |

## Portfolio gates

| Gate ID | Outcome required | Depends on | Evidence required | Owner | State |
|---|---|---|---|---|---|
| TADP-CORR-GATE-01 | Exact aligned v1.0 design baseline is ready for human acceptance | Complete initial suite, evidence alignment, assumption review, and legacy mapping decisions | Initiative suite, decision receipts, migration ledger, and explicit acceptance question | User | Open |
| TADP-CORR-GATE-02 | Executable validator and regression implementation is separately governed | Accepted design and a new correlated implementation tuple | New implementation initiative, branch, acceptance receipt, execution record, and verification | User | Open |

## Maintenance rules

- Update status only from current initiative and verification evidence.
- Record only legal lifecycle states and transitions; Reopened is an event.
- Link blockers to the record that owns their resolution.
- Retain terminal rows until a separately recorded retention rule permits
  archival.
- Reconcile this view with the initiative index and affected README in the same
  reviewed change.
