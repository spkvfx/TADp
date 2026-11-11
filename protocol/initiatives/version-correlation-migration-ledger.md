# TADp protocol version-correlation migration ledger

**Project:** Traceable Architecture Design Protocol (TADp)

**Correlation revision effective point:** `007e791750a7dd5bca1befabd88cf83defde14b4`,
the coherent protected-update commit containing specification 09, affected
consumers, validator behavior, tests, and refreshed protocol and example locks

**Ledger owner:** User

**Last reviewed:** 2026-11-11

## Authority boundary

This ledger records compatibility disposition only. It does not infer a new
tuple, accept an initiative, create lifecycle standing, or claim migration.
Meaning-changing mappings require a separate explicit human decision receipt.

## Migration ledger

| Legacy identity | Canonical identity | Suite | Initiative | Branch | Action | Authority/evidence | Ambiguity or blocker |
|---|---|---|---|---|---|---|---|
| Pre-effective v1.0 bootstrap identity recorded 2026-11-10 | Not migrated — must not be inferred as governed by specification 09 | [RZN-TADP-001-VERSION-CORRELATION-SUITE](../evidence/non-authoritative/realizations/v1.0/00-RZN-TADP-001-VERSION-CORRELATION-suite-index.md) | [INIT-DSN-001](design/INIT-DSN-001-version-realization-correlation/README.md) | `initiative/v1.0-version-realization-correlation` from `v1` at `d05f334e854431716275a59c980f0c909d88d002` | Deferred | [VRC-DR-001](design/INIT-DSN-001-version-realization-correlation/decision-receipts/VRC-DR-001-supersede-prior-initiative.md), Stage 0 commit `e2677f2`, and retained source records; governing workflow revision: authoritative specifications 00–08 before the specification 09 effective point | The paired initiative is `Superseded`, and VRC-01/VRC-02 remain historical unresolved project-specific questions that do not govern the protocol revision; re-entry or migration condition: an explicit reopening or migration decision, with a new governed successor tuple for any substantive claim change |

## Disposition rules

- The row preserves the original suite, initiative, branch, base, lifecycle,
  and source identities. It does not assert that specification 09 governed
  their allocation.
- `Deferred` is an actionable legacy warning, not a validator error or a
  completion claim.
- No project-specific meaning-changing mapping is performed by this protocol
  revision.
- Reopening INIT-DSN-001 requires explicit human authority reconciled with its
  named replacement. A substantive change requires a new Stage 0 tuple.
