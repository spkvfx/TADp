# Example Record Application project decision receipts

These receipts preserve explicit human decisions that govern project-level
exceptions or complete initiative sets before an individual initiative record
exists. Each receipt is linked from its source conflict or tracking record and
committed with the records reconciled from the decision.

| Receipt ID | Source ID or event | Disposition | Human authority | Date or event | Source record | Commit |
|---|---|---|---|---|---|---|
| [EX-GIT-DR-001](EX-GIT-DR-001-enclosing-worktree-exception.md) | `INV-CONFLICT-001` | Project-wide embedded-example-root exception accepted | User, sole project and invariant-exception authority | 2026-11-11 | [Resolved conflict](../../evidence/authoritative/LLM/03_Codex_Invariant_Conflict_Register.md#inv-conflict-001--embedded-example-project-root-and-git-root-invariant) | `553b1d386623908bdf244cc35c9bc2cea06985fd` |
| [EX-VSG-DR-001](EX-VSG-DR-001-initiative-migration.md) | Six-initiative scope adoption and migration | Explicit migration; all six remain Proposed | User migration instruction; Codex placement author | 2026-11-12 | [Migration ledger](../version-scope-migration-ledger.md), [verification](EX-VSG-VER-001-migration-verification.md) | Receipt/plan: `9edc7f3`; reconciliation commit discoverable through Git |
| [EX-PREP-DR-001](EX-PREP-DR-001-branch-recovery.md) | EX-PREP-001 / EX-AQ-PREFLIGHT-001 | Executed local history merge and exact baseline installation; six assigned checkouts verified | User's follow-up merge/preparation instruction; Codex execution author | 2026-11-12 | [Preparation verification](EX-VSG-VER-001-migration-verification.md) | Discoverable through the receipt's Git history |
