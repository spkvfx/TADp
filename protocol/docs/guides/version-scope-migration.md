# Version scopes, intake routing, and local integration

This guide explains the prospectively adopted
[scope specification](../../evidence/authoritative/LLM/09_Codex_Version_Realization_Initiative_Correlation_Specification.md)
and [Git contract](../../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md).
The maintenance authority is [VSG-DR-001](../../decisions/VSG-DR-001-version-scope-grouping.md).
Installation alone migrates no initiative and authorizes no live merge.

## Identity and placement

A coordination scope is exactly `vN`, `vN.M`, or `vN.M.P`, using non-negative
decimal integers without leading zeroes. Compare components numerically;
`v1.10` follows `v1.9`. `v1`, `v1.0`, and `v1.0.0` are distinct identities.
Never rename a legacy minor scope to a major or normalize a bare major.
Work scopes are separate from package versions and release claims.

Each initiative belongs to one scope, owns one independently acceptable
outcome and its complete type-specific records, and has one active execution
assignment per revision cycle. A scope may have no members or many members
of different types. Several initiatives may cite the same source note; a
note may route to several existing or new targets. Record exact originating
and contributing suite/note IDs and paths, their source scope, target scope,
per-target disposition, and fit rationale. Preserve source standing.

New initiative paths are `initiatives/<scope>/<type>/<id-and-slug>/`.
`initiatives/version-scopes.md` owns scope registration;
`initiatives/initiative-index.md` owns membership and correlation.
Each scope README links to those owners, while each initiative README retains
lifecycle authority. Project status, migration and work-conflict registers
remain at project level. Never move historical initiatives as distribution
synchronization or rewrite old links to imply that grouping always applied.

## Adopt and preserve legacy records

1. Capture Git baseline, worktree inventory, governing revision, old version,
   suite/note, initiative, branch/base, path and lifecycle evidence.
2. Install a coherent revision with verified templates, tools, tests, guidance
   and protected locks. Record its actual delivery commit as the project
   `Version scope revision effective point` only after that commit exists.
   Link `Version scope migration ledger` and exact adoption authority.
3. Inventory every legacy initiative in the ledger. Record proposed scope,
   old/new path mapping, source evidence, action, authority, blockers and
   re-entry condition. A complete `Deferred` or `Unmigrated` disposition keeps
   the project/record on its earlier compatible revision. Do not mix inferred
   partial scope fields into it.
4. Perform only explicitly authorized evidence-backed migrations. Path moves,
   provenance changes and branch reparenting are substantive operations;
   preserve history and old links. One-to-one legacy tuples can map into a
   shared scope only with recorded authority and reciprocal records.
5. Verify both the new records and retained legacy records. Historical PR
   evidence, immutable claims, source identity and removal evidence remain.

The earlier [correlation migration guide](version-realization-correlation-migration.md)
describes the predecessor revision. Its old tuple and notation rules apply
only to records still governed by that revision.

In this reference repository, maintenance targets `protocol/` and its scoped
support files. The example application lives in a separate repository; it is
not a synchronized mirror or an adoption prerequisite. Existing target projects
choose and record their own coherent governing revision. For evidence-backed
document recovery within that revision, use the
[template and prerequisite guide](template-prerequisites-migration.md).

## Route realizations before allocation

A human request to process an identified realization under the adopted
workflow delegates intake placement and necessary initiative/scope reopening.
The note itself grants no authority. Inventory existing claims, branches,
open and partial effort, dependencies and conflicts before allocating an ID.
For each target, record candidate choices, rejected alternatives, fit, exact
claim baseline, prior state, actual intake instruction, agent author and
delegation, affected records, compatibility effects and verification boundary.

Append detail that preserves the claim. Revise the same coherent narrow
outcome when supported by fit. Split independent outcomes or incompatible
types, ownership or authority; use a separate successor when appropriate.
The originating source scope is the default for new initiatives. An existing
target retains its scope even when a later source note belongs elsewhere.

Before changing a closed claim, record each reopening and return to
`Proposed`, preserving prior acceptance, completion and integration evidence.
This applies to `Completed`, `Cancelled` and `Superseded`; reconcile the latter
with its replacement. A direct return to `Accepted` requires a separate human
unchanged-claim decision. Before changing an accepted/in-progress normative
claim, pause affected delivery and record its return to `Proposed` and partial
work disposition. Alignment and renewed human acceptance precede delivery.
Record necessary closed scope and ancestor reopenings individually, including
pending integration. Delegated intake does not decide unrelated questions,
accept claims, authorize delivery, waive checks or close ancestors.

## Branches and closure

Discover the actual integration base from Git/configuration. Create major
branches from its captured tip, minors directly from the matching major, and
patches directly from the matching minor. Capture base ref and immutable
commit before creation, after clean-worktree/role/identity/parent preflight.
Prepare missing ancestors explicitly in order. For example, `v2.0` and `v2.1`
are siblings from `v2`; `v2.1.1` comes from `v2.1`.

Choose a dedicated `initiative/<scope>-<id-and-slug>` child or directly host
the initiative on its matching scope branch. Never silently repurpose an
exclusive initiative branch. Shared writes are serialized, preserve concurrent
index additions, and attribute paths, commits, revision bases and verification
to each member. Preserve assignment history and use continuation branches
when a historical ref cannot safely host a new revision.

Merge down means child into immediate recorded parent: dedicated initiative
to scope, patch to minor, minor to major, major to captured project base.
A directly hosted initiative records its verified commits without a self-merge.
Closing it does not close its scope or merge that scope upward.

A human instruction to close/finalize an identified governed initiative or
scope authorizes its bounded local child-to-recorded-parent integration once
all gates pass. Record the instruction, source/target and tips before acting.
Ordinary implementation, installation, or a terminal status grants no merge
authority. Pushes, branch deletion and further upward merges remain separate.

Scope closure is a separate operation: capture every member and descendant,
their truthful closed dispositions, child integration or authorized exclusions,
aggregate verification, coherence/conflict reconciliation and closure snapshot.
Pending child integration blocks closure. Empty scopes need explicit no-work
dispositions. Never merge a shared tip carrying unfinished, unaccepted,
cancelled or unrelated work. Isolation/transfer needs its own recorded authority;
closing one member does not authorize discarding another's changes.

Inspect source/target tips, diff and worktree, verify the current target and
run checks before and after integration. Record method and actual resulting
commit; fast-forward and already-integrated results do not invent merge commits.
Conflicts or changed targets leave integration pending/blocked without erasing
truthful lifecycle closure. A reopened cycle requires fresh delta verification
and integration evidence. Retain branches unless deletion is separately authorized.

Pull requests are human managed. Workflow stages neither ask about nor create
them, and local finalization requires no PR URL or hosting connection. Preserve
historical PR evidence. Report external remote-policy constraints without
bypassing them. Stage numbers 0 through 13 and all three delivery paths remain.
