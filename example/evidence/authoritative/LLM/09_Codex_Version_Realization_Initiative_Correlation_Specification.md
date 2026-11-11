# Codex version-realization-initiative correlation specification

## Purpose and authority

This specification defines the project-local identity and traceability model
for TADp work allocated under this revision:

```text
work version <-> realization suite <-> initiative <-> dedicated Git branch
```

The relationships are reciprocal and one-to-one. They establish identity and
traceability only. They do not establish evidence authority, initiative
acceptance, dependency satisfaction, implementation, completion,
compatibility, release, or deployment.

### Revision record

- **Authority:** The User's explicit instruction in
  `prompts/version-realization-initiative-correlation-protocol-change.md`,
  executed on 2026-11-11, authorizes this exact invariant revision and the
  affected protected-source changes.
- **Reason:** A governed work unit needs one immutable project-local version,
  one non-authoritative realization suite, one self-contained initiative, and
  one dedicated branch so identity cannot drift or be reused across
  independently acceptable outcomes.
- **Affected scope:** Work-version syntax and allocation, realization-suite
  structure, initiative metadata and scope, branch traceability, Stage 0 and
  later workflow contracts, legacy compatibility, templates, prompts,
  validator behavior, tests, adoption guidance, and migration guidance.
- **Effective point:** The first Git commit that contains this coherent
  specification, every necessarily affected authoritative and reusable
  consumer, the required validation behavior and regression tests, and the
  authorized protected-source locks. A governed project must record that
  commit as its correlation-revision effective point before allocating work
  under this model.
- **Compatibility and migration:** The revision governs tuples allocated after
  the project-recorded effective point, pre-effective tuples explicitly
  migrated to it, and every substantive successor or mandatory split begun
  after it. Pre-effective records require the legacy disposition defined
  below; this revision never infers or retroactively invents a tuple.
- **Successor relationship:** This specification succeeds specifications 02,
  05, 06, and 08 only for work identity, reciprocal correlation, branch
  correlation, split allocation, and Stage 0 preparation. Their evidence,
  governance, lifecycle, scope, Git, decision, and workflow rules continue to
  govern every other subject.

## Canonical work version

A TADp work version has the exact syntax `v<major>.<minor>`.

- Both components are non-negative base-10 integers.
- `0` is canonical. A multi-digit component must not have a leading zero.
- A sign, whitespace, patch component, prerelease label, build metadata, or
  bare major identifier is prohibited.
- Canonical examples include `v0.0`, `v0.1`, `v1.0`, `v1.1`, `v13.8`,
  `v13.9`, and `v13.10`.
- Components are compared numerically. `v13.10` follows `v13.9`; lexical
  ordering is not authoritative.
- A work version is unique within one governed TADp project, immutable after
  allocation, and never reused or silently renumbered.

The work version is distinct from architecture, contract, workflow, product,
package, protocol-distribution, and release versions. Its order does not
establish authority, acceptance, dependency satisfaction, compatibility,
completion, or release status.

## Governed tuple and cardinality

A governed tuple contains exactly one of each of the following:

1. canonical work version;
2. realization suite with one stable suite ID and path;
3. new, self-contained initiative with one stable ID, type, and path; and
4. dedicated Git branch created from a captured base branch and base commit.

Within one governed project, each value maps to exactly one value in every
other position. The reverse relationships are also unique. Two initiatives
must not share a work version, suite, or branch; a suite or branch must not be
orphaned; and a correlation row must not point to missing or inconsistent
reciprocal records.

The project initiative index owns the canonical project-level correlation
row. The realization-suite index, initiative README, status view, delivery or
execution record, completion evidence, and Git traceability records copy only
the fields needed for their subject and must link to that canonical row. A
copy never becomes a competing source of lifecycle standing or authority.

At minimum, the canonical row and reciprocal records preserve:

- canonical work version;
- realization-suite ID and path;
- initiative ID, declared type, and path;
- dedicated branch;
- captured base branch and immutable base commit;
- predecessor or successor relationship, when one exists;
- lifecycle status and its supporting evidence; and
- branch-removal authority and evidence when an historical branch ref is
  absent.

The project uses its recorded branch-naming convention. When none exists, the
default is `initiative/v<major>.<minor>-<initiative-slug>`. The branch name
must retain the exact work-version token.

## Realization-suite and initiative boundaries

A realization suite is permanently non-authoritative proposal input. Creating
it or pairing it with an initiative does not accept the initiative or promote
any realization claim.

A suite may contain an index and several supporting realization notes only
when every note describes the same narrowly bounded outcome, owner, authority
boundary, output family, verification claim, and lifecycle. The suite index
owns suite identity, boundary, catalog, evidence standing, and reciprocal
correlation metadata.

The paired initiative must be self-contained. It owns one narrow outcome, one
acceptance claim, its complete required initiative suite, its decisions,
lifecycle history, type-specific delivery records, and completion evidence.
External invariants and dependencies are cited rather than duplicated, but no
parent, sibling, subinitiative, release, or earlier version may substitute for
a missing initiative-local record or prove another version's completion.

Every parent, sibling, or subinitiative created, substantively revised, or
migrated under this revision receives its own work version, realization suite,
initiative, and branch. A mandatory scope split therefore creates separately
allocated tuples; a version must not act as an umbrella for independently
acceptable outcomes.

## Successors, reopening, and immutable identity

A substantive change to an outcome, scope, authority boundary, output family,
compatibility obligation, or verification claim requires a successor work
version, realization suite, initiative, branch, and correlation row. The old
tuple remains immutable and links to the successor.

A governed initiative reopened with its exact accepted claim unchanged may
retain its tuple. The reopening event, authority, compatibility effect, and
new verification boundary remain subject to the lifecycle and human-decision
specifications. A pre-effective initiative follows its recorded legacy
disposition. Neither reopening nor a successor changes historical identity.

## Workflow integration

The canonical Stage 0 sequence is:

1. Preflight the proposed work version, suite ID and path, initiative ID and
   path, dedicated branch, base branch, and base commit without writing.
2. Verify canonical syntax, project-local uniqueness, intended scope and type,
   readable templates, and a clean worktree.
3. Create the version-bearing initiative branch from the captured base.
4. On that branch, create the realization-suite index and initial
   non-authoritative realization note, canonical correlation row, reciprocal
   metadata, and minimal initiative skeleton as one preparation unit.
5. Record the preparation commit when one is created, without treating it as
   acceptance or delivery evidence.

Stage 0 does not create a proposal, resolve a question, accept the initiative,
or begin delivery. Stages 1 through 13 must verify that the same tuple remains
canonical, complete, reciprocal, and on the recorded branch before consuming
or changing initiative state. A mismatch is a failed entry or verification
gate; a later stage must not repair earlier identity by inference.

The stage numbers and type-specific paths do not change under this revision.

## Branch retention and removal

An active initiative in `Proposed`, `Accepted`, or `In progress` state requires
the recorded local branch ref to exist. Branch identity remains unique even
after the workflow becomes terminal.

A branch ref may be absent only after a separately authorized removal whose
decision receipt or equivalent governing evidence is linked from the
canonical correlation row and initiative Git history. The recorded branch,
base branch, and base commit remain immutable. Absence without linked removal
authority is an error; branch deletion must never free the name for another
tuple.

## Effective point and legacy compatibility

A governed project records the exact correlation-revision effective commit in
its project profile and links its migration ledger. The new model governs:

- every work version, realization suite, and initiative allocated after that
  effective point;
- every pre-effective tuple whose ledger action explicitly migrates it; and
- every substantive successor or mandatory split begun after that point.

An unchanged pre-effective claim may continue only under its recorded,
invariant-compatible earlier workflow revision and a complete `Unmigrated` or
`Deferred` migration-ledger disposition. Such a row must preserve the legacy
identity and source evidence, name the earlier workflow revision, state the
re-entry or migration condition, and contain no partial or inferred new
correlation. It remains an actionable warning until migrated or given another
authorized terminal disposition.

An undeclared legacy record, a missing or incomplete ledger disposition, or a
record that mixes legacy and new correlation fields is an error. Any
substantive change after the effective point requires a new governed tuple.

## Migration ledger

Every adopting project uses this reusable minimum ledger shape:

| Legacy identity | Canonical identity | Suite | Initiative | Branch | Action | Authority/evidence | Ambiguity or blocker |
|---|---|---|---|---|---|---|---|
| `<legacy identity>` | `<canonical identity or not allocated>` | `<suite path or not inferred>` | `<initiative path or not inferred>` | `<branch or not inferred>` | `<Unmigrated, Deferred, Migrate, Normalize, Split, or Blocked>` | `<source links and governing workflow revision>` | `<ambiguity and re-entry or migration condition>` |

Ledger actions obey these rules:

- Normalize a bare `vN` to `vN.0` only when evidence proves a notation-only,
  identity-preserving change.
- Do not silently convert a broad realization or umbrella initiative into a
  narrow governed tuple. Allocate one new tuple for each required split.
- When a bare suite embeds or references a distinct dot-scoped outcome,
  preserve both identities as a possible split until an explicit human
  decision resolves the mapping.
- Preserve immutable realization evidence and historical links. Use a linked
  successor, compatibility mapping, or migration record rather than rewriting
  history to imply that this model always applied.
- Do not invent missing realizations, decisions, initiatives, branches,
  acceptance, implementation, completion, or release evidence.
- A migrated initiative begins `Proposed` unless retained evidence supports a
  different legal state.
- A meaning-changing mapping requires an explicit human decision and receipt
  before it is applied.

Project-specific legacy tuples are migrated later, one narrowly scoped tuple
at a time on its own version-correlated branch. A protocol distribution
revision does not perform those project migrations.

## Validation requirements

Validation for a project that records this revision must report errors for:

- non-canonical work versions;
- duplicate versions, suites, initiatives, or branch mappings;
- missing required metadata or captured base identity;
- inconsistent or missing reciprocal links;
- orphan suites, initiatives, or canonical rows;
- a version token missing from its branch name;
- a missing live branch for an active initiative;
- an absent historical branch ref without linked removal authority;
- a mandatory split represented by shared tuple identity;
- lifecycle or evidence-standing claims that treat identity as acceptance,
  completion, or authority; and
- undeclared, partial, mixed, or incompletely dispositioned legacy records.

A complete pre-effective `Unmigrated` or `Deferred` row is an actionable
legacy warning, not an error. The validator must never infer or write a mapping
to clear a finding.

## Review checklist

- [ ] The work version is canonical and unique under numeric comparison.
- [ ] Suite, initiative, branch, and canonical row are reciprocal and unique.
- [ ] The initiative owns one narrow, self-contained acceptance claim.
- [ ] Captured base branch and commit remain immutable and traceable.
- [ ] Lifecycle and evidence standing remain separate from tuple identity.
- [ ] A successor or mandatory split has a separately allocated tuple.
- [ ] Legacy records have complete non-inferred ledger dispositions.
- [ ] Active and removed-branch states carry the required Git evidence.
