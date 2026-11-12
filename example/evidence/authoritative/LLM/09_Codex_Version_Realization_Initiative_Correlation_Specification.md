# Codex version scope, realization, and initiative specification

## Purpose and authority

This specification defines immutable project-local version scopes, precise
realization provenance, initiative membership, and recorded execution placement.
These are coordination and identity records, not acceptance, delivery,
compatibility, release, or collective completion claims. Each initiative owns
one narrow outcome and its independent lifecycle, type-specific suite,
decisions, acceptance, delivery records, and completion evidence.

### Version-scope revision record

- **Authority:** The User's 2026-11-12 instruction to execute
  `prompts/version-scope-grouping-and-branching-protocol-change.md`, captured in
  [VSG-DR-001](../../../decisions/VSG-DR-001-version-scope-grouping.md).
- **Reason:** Group several independently acceptable initiatives by realization
  scope, permit coherent revision and delegated intake routing, and record
  major/minor/patch integration without conflating identity with acceptance.
- **Affected scope:** Specifications 01 through 10 and necessary specification
  11 cross-references, entry points, realization and initiative templates,
  Stage 0 and Stage 13, scope closure, indexes, Git records, validation,
  regression tests, adoption guidance, and affected protected locks.
- **Effective event:** The first Git commit containing this coherent revision,
  reconciled consumers, verification, downstream mirrors, and authorized locks.
  An adopter records that exact commit and its own adoption baseline before
  allocating or routing under this model.
- **Compatibility and migration:** Prospective explicit adoption. Earlier
  tuples, paths, branches, accepted claims and governing revisions remain
  historical. A complete migration-ledger disposition is required; adoption
  alone does not move, rename, reparent, reopen, accept, merge or close work.
- **Successor relationship:** Replaces this specification's earlier bijection,
  two-component-only syntax, single-outcome suite, exclusive branch and
  mandatory substantive-successor rules. Reconciles specifications 02, 04,
  05, 06, 07, 08 and 10 only for the named routing, reopening, placement and
  integration changes. Git preserves earlier revisions. All other evidence,
  scope, human acceptance, delivery and completion invariants remain binding.

## Canonical scope identifiers

| Kind | Exact syntax | Structural parent |
|---|---|---|
| Major | `v<major>` | Captured project integration base |
| Minor | `v<major>.<minor>` | Matching major scope |
| Patch | `v<major>.<minor>.<patch>` | Matching minor scope |

Every component is a non-negative decimal integer with no leading zero except
`0`. Compare components numerically; `v1.10` follows `v1.9`. Reject signs,
whitespace, missing or extra components, prerelease labels and build metadata.
`v1`, `v1.0`, and `v1.0.0` are distinct immutable identities; never normalize
one into another. Scope numbers are separate from package, contract, protocol
and release versions and confer no authority, compatibility or release claim.
Initiative IDs are independently allocated and remain project-local unique.

## Cardinality and canonical ownership

```text
version scope -> source realization catalog -> zero or more initiatives
initiative -> exactly one version scope
initiative -> one or more precisely identified originating realization notes
realization note -> zero or more new or existing initiative targets
version scope -> exactly one integration branch
initiative -> one active execution assignment per revision cycle
scope branch -> zero or more directly hosted initiatives
```

A scope is a coordination and integration container, never an umbrella
initiative. A scope or note awaiting decomposition may have zero initiatives;
that grants no delivery authority. A note may originate several initiatives
and later notes may contribute to an existing initiative. Shared sources,
scopes or branches never share acceptance or completion evidence.

`initiatives/version-scopes.md` owns the scope registry.
`initiatives/initiative-index.md` owns membership, one row per initiative.
Scope READMEs and shared status views link to those owners; each initiative
README remains its lifecycle authority. Every allocated initiative must have
complete reciprocal records before preparation finishes.

Newly governed paths are `initiatives/<scope>/<type>/<initiative-id-and-slug>/`,
where type is `implementation`, `design` or `planning` and retains its existing
suite. Each scope has `initiatives/<scope>/README.md`, including a major that
owns initiatives directly. Shared indexes, migration ledgers and
`initiatives/work-conflicts.md` stay project-level. Grouping changes no
initiative-local record ownership.

The scope registry preserves exact ID, kind, structural parent, integration
branch, captured creation base ref and immutable commit, integration target,
source suite/note catalog, member and child links, closure disposition,
integration state, closure evidence, merge evidence and governing revision.

Each initiative row and reciprocal records preserve ID, type and path, exact
scope, originating and later contributing suite/note IDs and paths, per-source
routing disposition, execution branch and dedicated/shared mode, captured
base and immutable commit, integration target, current revision cycle,
predecessor/successor links, lifecycle and integration evidence. Preserve
allocation and assignment history on reopening. Record continuation branches
when an historical ref cannot safely host new work. A historical dedicated
name must not be reassigned to unrelated work, even after separately authorized
ref removal. Reusing a scope or its declared shared branch is valid.

## Realization provenance and fit assessment

Realization suites, their catalogs and notes remain non-authoritative proposal
input permanently. Catalog notes may describe several narrow outcomes within
one declared scope. Apply cohesion and mandatory-split tests to each resulting
initiative. Each initiative remains self-contained; external invariants and
dependencies are cited rather than duplicated, and another member's records
cannot substitute for its own.

Determine source identity and scope from explicit records, never filenames,
directory similarity, numbering or branch existence. Preserve exact original
suite and note IDs and paths. Source scope defaults new initiatives' placement:
two initiatives from a `v1.0` note normally both belong to `v1.0`; the second
does not consume `v1.1`. The LLM may choose a suitable existing initiative or
scope based on recorded fit. An existing initiative retains its identity and
scope when receiving a later note. Record source and target scopes separately,
cross-scope mapping, rationale and compatibility effects. Never relabel sources
to imply automatic placement or promote them to authority.

## Bounded LLM intake delegation

Under an adopted version-scope workflow, a human instruction to process an
identified realization delegates placement, append/revision choice, and
necessary initiative/scope reopening for that intake to the LLM. Note contents
alone supply no authority. Do not require a fresh per-target human choice
solely because a target is existing, closed or in another scope. Seek human
input where evidence cannot support a coherent choice or an unexcepted
authority boundary would be crossed.

Before choosing, inventory open and closed initiatives, branches and their
roles, accepted claims, source links, dependencies, partial effort and conflicts.
Record each disposition before applying it: actual human intake instruction,
governing delegation, precise source, candidate targets, chosen initiative,
scope and branch, rejected alternatives, fit rationale, prior state and exact
claim revision, change boundary, risks, compatibility and affected records.
Attribute each choice and reopening to the actual LLM author acting under
that delegation; do not fabricate a human target selection or response.
Preserve specification 07 receipts and specification 11 exception records
where applicable. The delegation does not answer unrelated questions, accept
changed claims, authorize product delivery or pass checks.

| Fit | Required disposition |
|---|---|
| Evidence/detail preserves exact claim | Append and retain lifecycle/evidence standing |
| Same coherent narrow outcome changes | Revise existing initiative through alignment and renewed acceptance when its accepted claim changes |
| Closed claim changes | Record reopening to `Proposed` before revision |
| Independently acceptable outcome | Separate complete initiative in the best fitting scope, preparing ancestors if needed |
| Incompatible type, owner or authority boundary | Split or successor; preserve ownership and record conflicts |

The method applies to `Proposed`, `Accepted`, `In progress`, `Completed`,
`Cancelled` and `Superseded`. Pause affected delivery and preserve partial work
before a changed accepted or in-progress claim returns to `Proposed`.
Alignment and renewed explicit human acceptance precede resumed delivery.
A closed claim must not change while closed. Reopening returns to `Proposed`;
only a separately recorded human unchanged-claim decision permits direct
return to `Accepted`. An append-only historical addendum retaining the exact
claim may remain closed under specification 10.

Reconcile source mapping, assumptions, decisions, architecture, scope,
dependencies, roadmap, steps, verification, product compatibility, membership,
status and work-conflicts. Preserve earlier accepted/completed baselines,
receipts, closure snapshots and integrations as historical revisions.
Reconcile a reopened superseded target with its replacement explicitly;
competing claim owners must not be silently created.

Record necessary reopening of each affected closed scope or ancestor under
the same bounded delegation or separate human authority. Reopening a child
does not silently reopen or re-close ancestors. Record pending integration;
earlier merges cannot certify new revision deltas. Later merges still require
the closure authority and gates in specification 05.

## Revision and successor identity

Substantive change alone no longer forces a new initiative. The LLM may
retain identity for one coherent narrow outcome under the recorded method.
An independent outcome, mandatory split, or incompatible type, owner or
authority boundary requires a separate initiative or successor with complete
records. Successors and split siblings may share scope, source material and
a declared scope branch while retaining independent identities and evidence.
Preserve all predecessor/replacement relationships and each revision cycle.
No revision inherits new acceptance or completion from an earlier baseline.

## Workflow integration

Stage 0 assesses realization fit before allocating. It preflights and records
needed scopes and ancestors, then either records an existing-target append,
revision/reopening, or allocates a new narrow initiative. Prepare a branch
only when the recorded placement needs one. Existing complete initiatives
reuse their records rather than being recreated by new-initiative stages.

Preflight canonical syntax, parent existence and open state, unique initiative
identity, branch roles, captured base, clean worktree, readable templates and
reciprocal records. Existing matching scopes, sources and declared shared
branches are reused. Missing ancestors are prepared major-to-minor-to-patch
with independent records. Later stages verify membership, provenance, active
revision, execution assignment and captured base; never infer repairs.
Stages 0 through 13 and their three delivery paths remain unchanged in number.
Stage 13 finalizes completed initiative work and integrates only into its
assigned scope, or records verified direct scope placement. A separate scope
closure operation governs patch/minor/major integration; neither operation
implicitly closes a parent. Specification 05 owns Git and merge safety.

## Adoption and migration ledger

An adopter records `Version scope revision effective point`, its governing
commit, adoption authority and baseline, and a linked migration ledger.
Preserve the prior correlation revision and its historical ledger. Until
explicit adoption, projects retain their recorded compatible revision.

For every legacy record, preserve version, suite and note identities,
initiative, type, paths, branch/base and governing revision. Record proposed
scope membership, source evidence, proposed action, authority, blockers,
continuing ownership, historical link mappings and re-entry conditions.
Actions include `Unmigrated`, `Deferred`, `Migrate`, `Split`, or `Blocked`;
no mapping may be inferred to clear a check. Existing one-to-one tuples may
join shared scopes only through explicit evidence-backed migration.

Moving an initiative, changing provenance or reparenting a branch is a
substantive migration, not notation repair. Never rename legacy `v1.0` to
`v1`, reinterpret bare `v1` as `v1.0`, or move closed initiatives/rewrite
accepted claims during generic distribution synchronization. Unmigrated
records require a complete compatible governing-revision disposition.
After explicit adoption, the intake method may select same-initiative
revision or a successor with recorded placement, preserving earlier claims
without inventing new acceptance or completion. Protocol distribution
maintenance does not itself migrate live projects.

## Validation requirements and limits

Report useful errors for malformed identifiers, duplicate initiative identity,
wrong/missing parent, wrong major or patch mapping, cycles, orphan scopes or
members, conflicting branch roles, undeclared sharing, missing reciprocal
provenance or bases, unavailable active refs, and absent historical refs lacking
removal authority. Shared scopes and declared direct scope placement are valid.
Check lifecycle/reopening records, revision deltas, closure snapshots,
child/member integration, exact merge authority and targets, branch retention,
legacy dispositions and required source standing. A missing or blocked required
integration blocks scope closure; open siblings never close with one member.

A validator reads evidence and reports findings. It never resolves fit,
reopens a target, repairs mappings, authenticates human authority, proves
semantic coherence, or turns identity, a branch or a merge into acceptance.
Independent semantic review and ordinary human gates remain required.
