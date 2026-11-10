# Version-realization-suite-initiative correlation proposal

**Initiative:** INIT-DSN-001-version-realization-correlation

**Proposal status:** Draft

**Revision:** 0.1

**Last updated:** 2026-11-10

**Owner:** User

**Initiative type:** design

**Type requirements:** See [the initiative template](../README.md#initiative-type-and-output-boundary).

## Executive proposal

Define and govern one canonical project-local identity correlation:

work version <-> realization suite <-> initiative <-> dedicated Git branch.

The requested decision is to accept a narrowly bounded design that adds the
authoritative correlation model, synchronizes its protected reusable protocol
and example specifications, and specifies the migration and validation
contracts without weakening evidence authority, lifecycle, human-decision, or
scope rules.

## Initiative type and permitted output

This is a design initiative. Its permitted delivery is the authoritative
correlation specification plus directly affected reusable specification
sources: invariant references, templates, workflow contract, numbered prompts,
and protected protocol/example counterparts. It may create initiative-local
design and migration analysis.

Executable validator and regression-test changes are product changes under the
current type boundary. They require a separate implementation initiative,
work version, realization suite, and dedicated branch after this design is
accepted. Developer and adoption documentation that operates the executable
change belongs with that implementation consumer. This split prevents the
protocol revision from becoming an umbrella initiative.

## Problem and evidence

The current authoritative suite requires a dedicated branch for every
initiative and narrow, self-contained initiatives, but it does not define a
canonical TADp work-version syntax or reciprocal project-level mapping among a
version, realization suite, initiative, and branch. The User's migration
instruction identifies legacy bare and dotted identities, including a v4
suite and v4.1 dot-scope relationship. The captured repository at
v1@d05f334 instead contains v0.0, v1.0, v2.0, v2.1, v2.2, v3.0, and v4.0;
reachable Git history introduces the web suite directly at v4.0 in 80c0ee0
and contains no tracked v4 path or v4.1 reference. That source mismatch is an
open migration-evidence question, not permission to invent the missing
identity or silently equate it with v4.0. Without an explicit model, version
identities can drift, collide, become orphans, or imply authority and lifecycle
standing they do not possess.

The User explicitly authorized this invariant revision and the required
protected-source changes. The same instruction explicitly withheld initiative
acceptance and completion, preserved all evidence and lifecycle distinctions,
required the v4 source identity to remain non-authoritative, and required a
human decision before any legacy mapping changes meaning.

## Intended outcomes

1. One authoritative specification defines canonical v<major>.<minor> work
   versions, numeric ordering, immutability, project-local uniqueness, the
   reciprocal one-to-one mapping, mandatory splits, successor behavior, and
   the distinction from every other version class.
2. Protected protocol and example invariant/template sources express the same
   correlation and workflow semantics, including reciprocal metadata and
   Stage 0 preflight/preparation.
3. A durable migration ledger inventories legacy v0, v1, v2, v2.1, v2.2,
   v3/v3.1, and v4/v4.1 identities without fabricating initiatives, decisions,
   acceptance, implementation, completion, or release evidence.
4. A separate implementation consumer receives an exact validator, regression
   test, documentation, and adoption contract for both protocol and example
   trees.

## Scope

### Included

- The new authoritative correlation specification and the smallest coherent
  updates to authoritative evidence authority, governance, lifecycle, Git,
  scope, decision-receipt, and workflow references.
- Matching protected protocol and example invariant suites.
- A reusable realization-suite-index template and correlation fields in
  realization, initiative, project profile, initiative index, status,
  preparation, delivery, completion, and Git traceability sources.
- Workflow contract and Stage 0 through Stage 13 prompt changes needed to
  create and preserve the same tuple.
- A legacy migration ledger and the v4/v4.1 analysis as design evidence.
- Authorized protected lock refresh after source review and verification.
- A precise handoff specification for executable validation, regression
  tests, operational documentation, and adoption guidance.

### Excluded

- Executable validator or test changes; a separately versioned implementation
  initiative owns them.
- Bulk migration of legacy initiatives or creation of missing legacy records.
- Meaning-changing legacy mappings without an explicit human decision.
- Acceptance, implementation, completion, release, deployment, merge,
  rebase, force-push, branch deletion, or automatic merge claims not supported
  by their own required evidence.
- Any unrelated invariant change or relaxation of evidence precedence,
  lifecycle, human-decision, Git, or narrow-scope requirements.

## Users and stakeholders

| Stakeholder or affected party | Need or responsibility | Expected change |
|---|---|---|
| Project owner | Allocate immutable work identities and accept exact initiative baselines | Reviews one canonical correlation row and initiative-local evidence |
| Initiative owner | Maintain one narrow, self-contained claim | Records reciprocal version, suite, branch, base, lineage, and lifecycle links |
| Protocol maintainer | Preserve invariant coherence and protected sources | Uses specification 09 and synchronized protocol/example reusable sources |
| Validator maintainer | Enforce syntax, cardinality, reciprocity, and orphans | Implements the accepted validation contract in a separate initiative |
| Legacy migration owner | Preserve history and surface ambiguity | Uses the ledger and obtains decisions for meaning-changing mappings |

## Terms

| Term | Meaning in this proposal |
|---|---|
| Work version | A project-local immutable identifier using canonical v<major>.<minor> syntax |
| Realization suite | One non-authoritative suite index and any notes that share one narrow outcome and lifecycle boundary |
| Correlation row | The project initiative index row that canonically owns the tuple and links to initiative-local status evidence |
| Dedicated branch | One recorded Git branch whose exact name retains the work-version token |
| Substantive successor | A changed scope, outcome, authority boundary, output, compatibility obligation, or verification claim requiring a new tuple |

## Proposed direction

### Product behavior or placement

Add 09_Codex_Version_Realization_Initiative_Correlation_Specification.md to
each protected authoritative LLM suite. Add a reusable realization-suite-index
template and revise only the protected templates and prompts that consume tuple
identity. Record the design initiative's own v1.0 bootstrap tuple without
pretending the new Stage 0 rule existed before acceptance.

The project initiative index owns canonical project-level correlation.
Initiative README, suite index, status, delivery, completion, and Git records
link to that row and remain authoritative only for their existing declared
subjects.

### Domain and authority model

The correlation specification is authoritative after its accepted design
delivery and effective commit. Realization suites remain non-authoritative.
The initiative README remains lifecycle authority for its initiative.
Acceptance and completion require their existing decision and verification
evidence. A work version or branch proves identity only.

### System boundaries

The design applies identically to the reusable protocol and example protected
sources. It does not reinterpret the example application's architecture,
security policy, product versions, package versions, contract versions, or
release versions. The example v4 case remains non-authoritative migration
evidence.

### Primary workflows

1. Stage 0 preflights the complete proposed tuple and uniqueness without
   writing, then creates the version-bearing branch from a captured clean base.
2. On that branch, Stage 0 records the realization-suite index, canonical
   correlation row, and minimal initiative skeleton as one preparation unit;
   later stages verify the same tuple and keep status Proposed until acceptance.
3. A substantive successor or mandatory split allocates a new work version,
   suite, self-contained initiative, branch, and canonical row.

### Data and lifecycle

Version tokens and tuple identities are immutable and never silently reused or
renumbered. The canonical project row is retained as history. Initiative-local
lifecycle history links its supporting receipt or verification. Preserved
branch and base identity remains recorded even if branch removal is separately
authorized later.

## Operational behavior

### Failure and recovery

Preparation stops before writes on dirty worktrees, noncanonical or duplicate
versions, reused suite/initiative/branch identities, ambiguous placement, or
missing templates. Later stages stop on tuple drift or missing reciprocal
links. Recovery preserves the original source identity and returns to the
owning stage; it does not silently renumber, overwrite, or manufacture records.

### Security and authorization

The model introduces no runtime trust boundary. Protected-source edits and
lock refresh use the User's exact authority for this invariant only. Human
decision receipts remain required for acceptance and meaning-changing legacy
mappings.

### Observability

The initiative index provides the canonical navigation row. Status views
summarize current evidence and link back. Validator diagnostics will identify
invalid syntax, duplicates, missing reciprocal links, orphans, branch/version
drift, and lifecycle/evidence-class violations without treating a passing
check as acceptance or completion.

## Compatibility and transition

Bare vN may normalize to vN.0 only when identity and meaning are unchanged.
Broad or umbrella legacy evidence is never silently narrowed. A bare suite
with a distinct dot-scoped outcome preserves both identities until a human
decision resolves the mapping. Historical realization evidence and links are
preserved through migration or compatibility records rather than rewritten to
imply the new invariant always applied.

The design initiative is a bootstrap case: current Stage 0 created only the
branch and two-README skeleton, and its durable source realization was recorded
immediately afterward. The accepted design will record this chronology and
will not retroactively claim conformance to the successor Stage 0 contract.

## Alternatives considered

| Alternative | Benefit | Cost or reason not selected |
|---|---|---|
| Treat existing version-like labels as sufficient | No migration work | Leaves syntax, ownership, reciprocity, and authority ambiguous |
| Use one umbrella version for several initiatives | Fewer identifiers | Violates narrow scope, independent lifecycle, and the authorized bijection |
| Put validators and specifications in one design initiative | One branch | Violates current type-specific output boundaries and the proposed mandatory split rule |
| Rewrite legacy paths into canonical form | Superficially uniform tree | Erases provenance and can silently change meaning |

## Risks and tradeoffs

| Risk or tradeoff | Impact | Mitigation or evidence needed |
|---|---|---|
| Bootstrap chronology differs from successor Stage 0 | False retroactive-conformance claim | Preserve preparation commit, realization timing, and compatibility note |
| Protocol/example protected copies drift | Inconsistent adopter behavior | Byte/content parity review and separate lock verification for both trees |
| Legacy bare and dotted identities encode separate outcomes | Incorrect migration | Ledger records both; exact human question before meaning-changing action |
| Requested v4/v4.1 source is absent from the captured tree and reachable history | Fabricated provenance or incorrect normalization | Record the requested identity separately from observed v4.0 and require a human mapping decision |
| Correlation fields become competing status sources | Conflicting lifecycle claims | Initiative index owns tuple; README owns lifecycle; copies link rather than redefine |
| Design/implementation split delays executable enforcement | Temporary gap after design | Name a v1.1 implementation consumer and keep delivery/effectiveness claims precise |

## Assumptions requiring assumption

- INIT-DSN-001 may allocate protocol work version v1.0 because no existing
  protocol work-version registry or conflicting protocol allocation exists.
- In the protected reusable sources, corresponding protocol and example files
  should carry identical normative semantics; project-relative paths may
  differ only when their actual placement requires it.

## Questions requiring decisions

- Does the User accept the exact aligned INIT-DSN-001 baseline at Stage 7
  after the complete initiative suite and migration analysis are presented?
- For each legacy bare/dotted pair whose mapping would change meaning,
  should it remain unresolved, normalize notation-only, or split into distinct
  successor tuples? Each exact mapping question must be presented separately.

## Acceptance outcomes

- The complete proposed initiative suite defines one narrow design claim,
  records the bootstrap tuple, identifies every protected specification source
  in scope, and has no undisposed mandatory split trigger.
- The migration ledger preserves every required legacy identity and gives the
  v4/v4.1 case a precise, evidence-backed disposition or explicit blocker.
- The exact protected protocol/example design baseline and its validator
  implementation handoff are coherent enough for an explicit Stage 7 human
  acceptance decision.

## References

- [Source realization](../../../../evidence/non-authoritative/realizations/v1.0/RZN-TADP-001-VERSION-CORRELATION.md) — non-authoritative record of the requested outcome and authority limits.
- [Codex invariant suite](../../../../evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md) — current authoritative evidence and workflow baseline.
- [Evidence authority specification](../../../../evidence/authoritative/LLM/01_Codex_Evidence_Authority_Specification.md) — invariant revision and evidence-standing requirements.
- [Initiative governance specification](../../../../evidence/authoritative/LLM/02_Codex_Initiative_Governance_Specification.md) — realization, initiative, acceptance, and revision rules.
- [Git workflow specification](../../../../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md) — captured base and dedicated-branch requirements.
- [Scope specification](../../../../evidence/authoritative/LLM/06_Codex_Initiative_Scope_Specification.md) — mandatory split and self-contained initiative rules.
- [Workflow specification](../../../../evidence/authoritative/LLM/08_Codex_Initiative_Workflow_Specification.md) — current Stage 0 through Stage 13 contracts.
- User instruction dated 2026-11-10 — explicit authority for the exact invariant and protected-source revision, with acceptance and lifecycle limits.

## Revision history

| Revision | Date | Owner | Change |
|---|---|---|---|
| 0.1 | 2026-11-10 | User | Initial working proposal |
