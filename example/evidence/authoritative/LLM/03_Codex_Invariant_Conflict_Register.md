# Codex invariant conflict register

## Purpose and authority

This register is the durable authoritative record of contradictions Codex
discovers between an invariant and a proposal, realization, initiative,
product, implementation, test, status claim, or other source.

An entry establishes that a conflict is known and blocks the affected claim.
It does not make the conflicting claim authoritative, revise the invariant,
approve an exception, or select a resolution.

Codex is explicitly authorized by the
[evidence authority specification](01_Codex_Evidence_Authority_Specification.md)
to append a factual entry when direct evidence demonstrates a contradiction.
Codex must not rewrite or remove existing entries. Resolution requires the
authority stated by the governing invariant or an explicit human instruction.

## Active conflicts

No invariant conflicts are recorded.

<!--
When a conflict is discovered, replace the statement above with the first
entry and append later entries without renumbering or reusing IDs. Preserve
resolved entries under the resolution history.

### INV-CONFLICT-001 — {{short title}}

- **Detected:** {{yyyy-mm-dd}}
- **Status:** Open
- **Governing invariant:** {{precise file, section, and claim}}
- **Conflicting source or behavior:** {{precise file, symbol, test, or claim}}
- **Exact contradiction:** {{state both incompatible claims}}
- **Affected scope:** {{initiatives, products, releases, or decisions}}
- **Immediate disposition:** {{blocked work and independent work that may continue}}
- **Required authority:** {{human or invariant owner}}
- **Required resolution:** {{lower-standing correction or explicitly authorized invariant revision/exception}}
- **Linked initiative records:** {{source mapping, decision, and status links}}
- **Evidence:** {{verification or observation proving the conflict}}
-->

## Resolution history

### INV-CONFLICT-001 — Embedded example project root and Git-root invariant

- **Detected:** 2026-11-11
- **Status:** Resolved by an example-project invariant exception
- **Governing invariant:**
  [`05_Codex_Git_Workflow_Specification.md`, Requirement](05_Codex_Git_Workflow_Specification.md#requirement)
  requires every TADp project to be the root of a Git repository.
- **Conflicting source or behavior:** The installed `example/` tree is intended
  to operate as a complete, self-contained TADp example project, while its Git
  metadata and history are owned by the enclosing TADp repository or worktree.
- **Exact contradiction:** The project-local boundary resolves `example/` as
  the example application's root, but `git rev-parse --show-toplevel` resolves
  to its parent. The generic Git-root invariant would therefore prevent the
  embedded example from having governed project standing even when every
  project file mutation remains inside `example/`.
- **Affected scope:** The entire installed Example Record Application under
  `example/`, including present and future project files, evidence, prompts,
  initiatives, products, lifecycle records, and validation. The conflict does
  not affect the enclosing repository's protocol-maintenance scope, a sibling
  tree, another scaffold, or another TADp project.
- **Immediate disposition:** Governed example-project work remained blocked by
  the Git-root precondition while adoption records were instantiated and an
  explicit project-specific exception was obtained.
- **Required authority:** User, the recorded sole project and
  invariant-exception authority.
- **Required resolution:** An explicit exception treating `example/` as the
  TADp project root while limiting the enclosing repository or worktree to Git
  mechanics, with a durable receipt and reconciliation of all project-root
  consumers.
- **Linked project records:**
  [`EX-GIT-DR-001`](../../../initiatives/decision-receipts/EX-GIT-DR-001-enclosing-worktree-exception.md),
  [project instructions](../../../AGENTS.md),
  [synchronized prompt instructions](../../../prompts/AGENTS.md),
  [project profile](../../../project-profile.md),
  [initiative index](../../../initiatives/initiative-index.md),
  [status view](../../../initiatives/status.md), and
  [migration ledger](../../../initiatives/version-correlation-migration-ledger.md).
- **Evidence:** The active enclosing worktree directly contains `example/`;
  the example has its own project instructions, authoritative and contextual
  evidence, prompts, initiatives, products, templates, tools, tests, profile,
  and tracking records; and its path guards keep non-Git side effects inside
  that directory.

#### Resolution

- **Resolution authority and date:** The User's explicit 2026-11-11 decisions,
  including the supplemental instruction not to limit the resolution to the
  current files or initiatives, are preserved in
  [`EX-GIT-DR-001`](../../../initiatives/decision-receipts/EX-GIT-DR-001-enclosing-worktree-exception.md).
- **Selected resolution and rationale:** For this installed example only,
  `example/` is the TADp project root for files, evidence, prompts, initiatives,
  products, lifecycle behavior, validation, and scope. The directly enclosing
  repository or worktree supplies only Git metadata, captured bases, local
  branch refs, staging, commits, history, and Git verification. This keeps the
  example self-contained as a project without making the enclosing TADp
  repository part of its project scope. The project-root instructions and this
  authoritative resolution supply the installed exception; the synchronized
  generic prompt instructions remain unchanged and continue to define the
  normal rule.
- **Invariant exception:** This is a project-wide, project-specific exception
  to specification 05's Git-root requirement. It applies to all governed work
  whose project root is this installed `example/` tree; it is not limited to a
  prompt, initiative set, version, branch, or file list. The generic invariant
  remains binding for the enclosing TADp repository, every sibling or parent
  scope, and every other TADp project. Only Git metadata may be mutated outside
  `example/` when performing example-project work.
- **Effective point:** The first Git commit containing this resolution, the
  decision receipt, all reconciled project consumers, and the refreshed
  example invariant lock.
- **Compatibility and migration:** Existing evidence standing, realization
  identity, and lifecycle history remain unchanged. The Git-root conflict is
  resolved project-wide, but it allocates no tuple and changes no lifecycle
  state. The six current legacy rows remain `Deferred` until their own Stage 0
  migration commits allocate complete tuples, and `RZN-001` at `v0.0` remains
  `Unmigrated` for its separately recorded reasons.
- **Successor relationship:** No generic invariant successor is created. New
  example initiatives and files inherit this project-root resolution without a
  new exception. A move of the example to its own Git root, a change to its
  containment relationship, or an attempt to extend its scope outside
  `example/` requires explicit reconciliation.
- **Verification:** Protected-source integrity, full validation, regression
  tests, local-link checks, exact path review, and read-only worktree audits
  must pass before governed example-project work consumes the exception.

For each resolved entry, retain the original conflict text and add:

- resolution authority and date;
- selected resolution and rationale;
- invariant revision, exception, or lower-standing correction;
- affected initiative and product changes;
- compatibility, migration, and recovery disposition; and
- verification proving the conflict is no longer active for the stated scope.

## Register rules

- Use one stable ID per distinct contradiction.
- Cite exact claims; a directory-level reference is insufficient.
- Preserve both sources and their original standing.
- Do not mark an entry resolved because work stopped, a test passed, or a lower
  record was edited unless the actual contradiction was removed or an explicit
  invariant exception was accepted.
- Keep the affected initiative and portfolio status synchronized with this
  register.

