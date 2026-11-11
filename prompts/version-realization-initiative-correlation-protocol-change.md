# Implement version-realization-suite-initiative correlation

Work in `C:\Users\User\PycharmProjects\TADp`.

Implement a governed TADp protocol revision establishing a one-to-one
correlation among:

```text
work version <-> realization suite <-> initiative <-> dedicated Git branch
```

## Explicit human authority

I explicitly authorize this exact invariant revision:

1. Every new work version identifies exactly one realization suite.
2. Every realization suite identifies exactly one new, self-contained
   initiative.
3. Every initiative identifies exactly one work version and realization suite.
4. Every such initiative uses exactly one dedicated Git branch correlated to
   that version.
5. A substantive successor claim requires a new version, realization suite,
   initiative, and branch.

I authorize the protected-source changes necessary to establish this rule,
including:

- `protocol/evidence/authoritative/LLM/**`;
- `protocol/template/**`;
- directly affected prompts, validators, tests, documentation, and migration
  guidance.

## Canonical work-version rule

Define a distinct TADp work-version identifier:

- Syntax: `v<major>.<minor>`.
- Both components are non-negative base-10 integers.
- Canonical examples include `v0.0`, `v0.1`, `v1.0`, `v1.1`, `v13.8`, and
  `v13.9`.
- Use no sign, whitespace, leading zero on a multi-digit component, patch
  component, prerelease label, or build metadata.
- Treat components numerically, not lexicographically.
- Minor values are unbounded; for example, `v13.10` follows `v13.9`.
- A bare identifier such as `v4` is not canonical.
- A version is unique within one governed TADp project, immutable after
  allocation, and never reused or silently renumbered.
- Version ordering does not establish evidence authority, acceptance,
  dependency satisfaction, compatibility, completion, or release status.
- Keep this work version distinct from architecture, contract, workflow,
  product, package, and release versions.

## Required cardinality and records

Enforce a bijection within each project:

- one work version -> one realization suite;
- one realization suite -> one initiative;
- one initiative -> one dedicated branch;
- and the reverse relationships must also be unique.

A realization suite may contain an index and multiple supporting realization
notes only when all notes describe the same narrowly bounded outcome, owner,
authority boundary, output family, verification claim, and lifecycle. A
mandatory split allocates a new version, suite, initiative, and branch.

Add reciprocal correlation metadata to:

- the realization-suite index;
- the initiative README;
- the project initiative index;
- the project status view where useful for navigation; and
- preparation, delivery, completion, and Git traceability records that consume
  the identity.

At minimum, record:

- canonical work version;
- realization-suite ID and path;
- initiative ID, type, and path;
- dedicated branch;
- captured base branch and base commit when available;
- predecessor or successor relationship, if any;
- lifecycle status and its supporting evidence.

The project initiative index should own the canonical project-level
correlation row. Copies elsewhere must link to it and must not become competing
sources of status or authority.

Use the project's recorded branch-naming convention. If none exists, use:

```text
initiative/v<major>.<minor>-<initiative-slug>
```

The branch identity must retain the exact version token. Preserve the recorded
branch and base identity even if later branch removal is separately authorized.

## Meaning of "self-contained"

Each initiative must contain its own complete required initiative suite, one
narrow outcome, one acceptance claim, its own decisions, lifecycle history,
delivery records, and completion evidence.

Self-contained does not mean duplicating authoritative sources or pretending
dependencies do not exist. Cite external invariants and dependencies precisely.
No sibling, parent, release, or earlier version may substitute for a missing
initiative-local record or permit the initiative to claim another version's
completion.

Every parent, sibling, or subinitiative that is itself an initiative must
receive its own version, realization suite, and branch. Do not create a version
as an umbrella for multiple independently acceptable outcomes.

A reopening that leaves the exact accepted claim unchanged may retain its
version. A substantive change to scope, outcome, authority boundary, output,
compatibility obligation, or verification claim requires a successor version,
suite, initiative, and branch.

## Preserve evidence and lifecycle distinctions

The one-to-one correlation must not collapse evidence classes:

- a realization suite remains non-authoritative proposal input;
- creating its paired initiative does not accept that initiative;
- the initiative begins through the existing preparation, proposal, creation,
  alignment, decision, and acceptance workflow;
- a version or branch never proves acceptance, implementation, completion, or
  release;
- existing human-decision, lifecycle, narrow-scope, conflict, verification, and
  completion rules remain binding.

## Workflow integration

Do not add or renumber workflow stages unless a separately identified need
requires it. Integrate the correlation into Stage 0 preparation:

1. Preflight the proposed version, suite ID/path, initiative ID/path, branch,
   base branch, and base commit without writing.
2. Verify uniqueness and a clean worktree.
3. Create the version-bearing initiative branch from the captured base.
4. On that branch, create the realization-suite record, reciprocal correlation
   entry, and minimal initiative skeleton as one preparation unit.
5. Require later stages to verify that the same correlation remains intact.
6. Keep the initiative `Proposed` until the existing acceptance requirements
   are satisfied.

Update the stage contracts, reusable prompts, templates, handoffs, and recovery
rules accordingly.

## Authoritative and protected changes

Add an authoritative specification dedicated to this model, preferably:

`09_Codex_Version_Realization_Initiative_Correlation_Specification.md`

Update the authoritative suite index and the smallest necessary portions of
the evidence-authority, governance, lifecycle, Git, scope, and workflow
specifications to reference it coherently.

Update the protected reusable sources, including as applicable:

- realization guidance and realization-note templates;
- a new realization-suite-index template;
- initiative README, project profile, initiative index, and status templates;
- workflow contract and numbered prompts, especially preparation, proposal
  creation, initiative creation, alignment, acceptance, delivery, and
  finalization;
- adoption and migration documentation.

## Legacy migration

Define a reusable migration-ledger format containing:

| Legacy identity | Canonical identity | Suite | Initiative | Branch | Action | Authority/evidence | Ambiguity or blocker |
|---|---|---|---|---|---|---|---|

Apply these rules:

- Normalize a bare `vN` to `vN.0` only when that is a notation-only,
  identity-preserving change.
- Do not silently convert a broad or umbrella realization into a narrow
  initiative.
- Where a bare suite embeds or references a distinct dot-scoped outcome, treat
  that as a possible split and preserve both identities until the mapping is
  explicitly resolved.
- Preserve immutable realization evidence and historical links. Use a linked
  successor, compatibility mapping, or migration record instead of rewriting
  history to imply that the new rule always existed.
- Do not invent missing realization documents, decisions, initiatives,
  acceptance, implementation, or completion evidence.
- A migrated paired initiative starts as `Proposed` unless existing evidence
  supports another legal state.
- Do not migrate project-specific legacy tuples as part of this protocol
  revision. Apply the migration rules later to each governed project, with each
  separately scoped tuple handled on its own version-correlated branch.

If a legacy mapping changes meaning rather than notation, record the exact
question and obtain an explicit human decision before applying that mapping.

## Validation

Extend repository validation and regression tests to check:

- canonical version syntax;
- numeric parsing and ordering;
- uniqueness of every version, suite, initiative, and branch mapping;
- reciprocal links and required metadata;
- orphan suites, initiatives, or correlation rows;
- one initiative branch per version;
- separate versions when a mandatory split occurs;
- preservation of lifecycle and evidence standing;
- legacy compatibility and migration records.

Include positive cases for:

`v0.0`, `v0.1`, `v1.0`, `v1.1`, `v13.8`, `v13.9`, and `v13.10`.

Include negative cases for:

`v0`, `0.1`, `v01.0`, `v1.01`, `v1.0.0`, duplicate mappings, missing reciprocal
links, orphan suites, and two initiatives sharing a version or branch.

Use self-contained protocol-owned fixtures for validation. Run the
repository-defined protected-source checks, validator, and unit tests using the
configured project Python environment.

## Completion report

Report:

- the final invariant and cardinality model;
- the authoritative revision and successor relationship;
- the migration-ledger format, migration rules, and unresolved protocol-level
  ambiguities;
- templates, prompts, validator rules, tests, and documentation updated;
- remaining migrations, blockers, or human decisions.
