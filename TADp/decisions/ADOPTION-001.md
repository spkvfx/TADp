# ADOPTION-001 decision receipt

**Receipt ID:** ADOPTION-001  
**Initiative:** Not applicable; prospective project adoption  
**Source ID or lifecycle event:** Adoption of the pinned installed governing baseline  
**Human authority:** Requesting human instructing this setup; repository-owner policy in [OWNERSHIP-001](OWNERSHIP-001.md)  
**Response date or event:** Current session, 2026-11-14  
**Capture date or event:** 2026-11-14, after explicit response and before adoption fields are activated  
**Recorded by:** Codex, primary agent  
**Capture context:** Separate explicit adoption question during setup  
**Disposition:** Prospectively adopted identified baseline for this new project  
**Git commit:** See the scoped setup commits containing this receipt and its reconciliation in Git history  
**Scope:** Not applicable; no version scope allocated  
**Revision cycle:** Not applicable; project adoption event  
**Claim revision:** `6120bd10bb2e368274fd5bd4ff5481d33f61c4c6`

## Exact prompt or question

Do you authorize prospective adoption of the verified installed TADp baseline at commit 6120bd10bb2e368274fd5bd4ff5481d33f61c4c6 for this new development project? This is separate from ownership and does not accept any initiative.

## Evidence and limitations presented

- **Authoritative evidence:** Installed suite index adoption contract; specifications 05, 08, 09, 10 and 11 retain their gates and source identities.
- **Other evidence:** Immutable source `6120bd10bb2e368274fd5bd4ff5481d33f61c4c6`; upstream worktree clean at preflight; copied protected content matches source; protection check passes. Baseline regressions: 292 tests, 4 skipped, no failures.
- **Material limitations:** Upstream structural validation reports TADP041 for a previously adopted coherence baseline whose profile declaration is absent. It was disclosed before this decision and is not repaired or waived. New-project first validation found links to the not-yet-written setup report; retain those failed runs and revalidate after the report exists. Structural checks do not establish semantic conformance or personal repository control.
- **Affected scope described to the human:** Prospective adoption for this new project only, with no initiative acceptance or upstream modification.

## Exact human response

```text
Adopt that verified baseline
```

## Resulting scope and rationale

Adopt the installed governing suite and compatible canonical workflow at
`6120bd10bb2e368274fd5bd4ff5481d33f61c4c6` prospectively for P. This actual
immutable commit identifies the governing source, not an invented future setup
commit. No governing source or lock changes during installation or adoption.

The captured pre-adoption Git baseline is
`6120bd10bb2e368274fd5bd4ff5481d33f61c4c6`, confirmed by `git rev-parse HEAD`
immediately before capturing this receipt. The setup is uncommitted on
`setup/tadp-development-project`; its installation-only state and earlier
pending decisions are preserved in the setup receipt and records. P had no
tracked earlier installation at that Git snapshot and no predecessor governing
revision. No initiatives, scopes, realizations, assignments, accepted claims,
partial execution, terminal claims or migrations exist within P. Upstream work,
branch names and historical adoption do not become this project's work.

The profile records the actual adopted source in the project-root, version-scope,
correlation and keyword revision fields and this pre-adoption snapshot in the
coherence field. The canonical migration ledger has no legacy rows to migrate.
Record a new decision before any later adoption or migration; do not reset this
captured baseline on a rerun. The current repository owner is the continuing
human steward under OWNERSHIP-001. Shared Git integration and scope assignments
must be established at the actual first allocation; no scope is allocated now.

## Reconciled records

| Record | Change required by this decision | Verification |
|---|---|---|
| [Profile](../project-profile.md) | Exact adopted source, coherence baseline, adoption authority and impact | Git identity, source manifest and structural validation |
| [Scope registry](../initiatives/version-scopes.md) and [ledger](../initiatives/version-scope-migration-ledger.md) | Governing revision and actual adoption event; retain empty legacy inventory | No inferred scope/member rows |
| [Entry point](../AGENTS.md), [README](../README.md), [workflow](../docs/development/tadp-development-workflow.md) | Reflect adoption separately from source installation and future delivery | Semantic and context review |
| [Evidence register](../evidence/evidence-register.md) and [setup verification](../evidence/non-authoritative/setup/verification.md) | Record actual authority and observed limitations separately | Link and provenance checks |

## Unresolved consequences and re-entry conditions

Adoption waives no failed check or human gate, performs no live migration,
accepts no initiative, reopens no claim, and authorizes no generic protected
source change, integration, remote write, release, promotion or rollout. The
upstream TADP041 finding remains disclosed and outside this setup's edit scope.
Future scope allocation must resolve shared branch roles and actual integration
configuration first. Each subsequent claim requires its actual evidence.
