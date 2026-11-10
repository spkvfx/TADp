# Version-realization-suite-initiative correlation architecture and specification

**Initiative:** INIT-DSN-001-version-realization-correlation

**Status:** Proposed

**Last updated:** 2026-11-10

Related documents:

- [Initiative README](README.md)
- [Proposal sources](proposal/README.md)
- [Assumption review](assumption.md)
- [Scope assessment](scope-assessment.md)
- [Evidence mapping](source-mapping.md)
- [Open questions and decisions](open-questions.md)
- [Delivery roadmap](implementation-roadmap.md)
- [Detailed delivery steps](implementation-steps.md)

## Proposal standing

This document is a proposed design specification. The User has authorized the
exact invariant revision and protected-source scope, but explicitly withheld
initiative acceptance and completion. No section becomes an accepted
initiative baseline until Stage 7 captures the exact human response in a
decision receipt and reconciles the lifecycle records.

## Specification boundary

This design specifies protocol identity, records, workflow, migration, and an
implementation handoff. It may revise protected reusable specification
sources only after acceptance. It does not implement validator/test products
or migrate legacy initiatives.

## Current repository baseline

| Area | Current contract or evidence | Consequence for this initiative |
|---|---|---|
| Evidence authority | [Specification 01](../../../evidence/authoritative/LLM/01_Codex_Evidence_Authority_Specification.md) preserves source standing and requires explicit revision authority | Correlation cannot promote realization suites or version order into authority |
| Initiative governance | [Specification 02](../../../evidence/authoritative/LLM/02_Codex_Initiative_Governance_Specification.md) requires narrow initiatives and separate acceptance | Tuple creation must not imply acceptance or combine outcomes |
| Lifecycle | [Specification 04](../../../evidence/authoritative/LLM/04_Codex_Initiative_Lifecycle_Specification.md) makes the README lifecycle authority | Project correlation copies status and links evidence only |
| Git | [Specification 05](../../../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md) requires one dedicated branch and captured base per initiative | The new model correlates that identity with the version and suite |
| Scope | [Specification 06](../../../evidence/authoritative/LLM/06_Codex_Initiative_Scope_Specification.md) defines cohesion and mandatory split triggers | Every split and independently governed initiative receives a new tuple |
| Human decisions | [Specification 07](../../../evidence/authoritative/LLM/07_Codex_Human_Decision_Receipt_Specification.md) requires durable receipts | Acceptance and meaning-changing migration decisions remain separate receipts |
| Workflow | [Specification 08](../../../evidence/authoritative/LLM/08_Codex_Initiative_Workflow_Specification.md) limits current Stage 0 to branch and skeleton | The successor Stage 0 must add tuple preflight and atomic correlation preparation without renumbering stages |
| Legacy example evidence | [Observed v4.0 suite](../../../../example/evidence/non-authoritative/realizations/v4.0/00-RZN-001-P4-WEB-suite-index.md), introduced at 80c0ee0 | The requested v4/v4.1 case cannot be silently equated to the observed v4.0 source |

## Goals and non-goals

### Goals

1. Define one canonical work-version grammar, numeric model, uniqueness scope,
   immutability rule, and ordering limitation.
2. Define a project-local bijection among one work version, realization suite,
   self-contained initiative, and dedicated branch, with reciprocal records.
3. Integrate correlation into current stages, templates, traceability,
   migration, recovery, and a separately governed validator implementation
   handoff while preserving authority and lifecycle distinctions.
4. Make `evidence/non-authoritative/realizations/**` the only project-local
   realization placement and keep each source artifact permanently
   non-authoritative, even when a separate governed record accepts a derived
   claim.

### Non-goals

- Reclassify or promote a realization note or suite in place, or treat a
  version, branch, or correlation row as acceptance, delivery, completion,
  compatibility, or release evidence.
- Implement executable validation or migrate legacy initiative tuples.
- Change architecture, contract, workflow, product, package, or release
  version semantics.
- Add or renumber workflow stages.

## Terms and identity

| Term or identity | Definition | Authority or lifecycle |
|---|---|---|
| Work version | Canonical v<major>.<minor> token whose components are non-negative base-10 integers without multi-digit leading zeros | Project-local immutable identity; ordering has no authority or lifecycle effect |
| Realization suite | One permanently non-authoritative suite index plus zero or more notes under `evidence/non-authoritative/realizations/<work-version>/` sharing one narrow outcome, owner, authority boundary, output family, verification claim, and lifecycle | Proposal input only; an accepted derivative claim is recorded separately |
| Initiative | One self-contained required initiative suite with one outcome and acceptance claim | README owns lifecycle; Accepted state requires receipt |
| Dedicated branch | One exact Git branch correlated to the work version and initiative | Git traceability only |
| Correlation row | Canonical project initiative-index row joining the four identities and their links | Owns project-level identity/navigation, not lifecycle authority |
| Substantive successor | Change to scope, outcome, authority boundary, output, compatibility obligation, or verification claim | Requires a new work version, suite, initiative, branch, and row |

The canonical syntax is:

    ^v(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$

Both components are parsed as arbitrary-size non-negative integers. Therefore
v13.10 follows v13.9. A token is compared numerically as (major, minor), never
lexicographically. Valid examples are v0.0, v0.1, v1.0, v1.1, v13.8, v13.9,
and v13.10. Invalid examples include v0, 0.1, v01.0, v1.01, and v1.0.0.

## Architectural decisions

| Decision ID | Direction used by this design | Status |
|---|---|---|
| VRC-01 | Preserve requested v4 and v4.1 identities separately from observed v4.0 until the exact mapping is decided | Open, blocking |
| VRC-02 | Preserve requested v3 and v3.1 identities separately from observed v3.0 until evidence or a decision establishes any mapping | Open |
| VRC-03 | Use canonical v<major>.<minor> syntax and numeric component ordering exactly as authorized | Proposed; source-authorized, pending initiative acceptance |
| VRC-04 | Enforce a project-local bijection and canonical initiative-index row with reciprocal links | Proposed; source-authorized, pending initiative acceptance |
| VRC-05 | Allocate a new tuple for every initiative, mandatory split, and substantive successor | Proposed; source-authorized, pending initiative acceptance |
| VRC-06 | Extend current Stage 0 atomically and make later stages verify tuple continuity without changing stage numbering | Proposed; source-authorized, pending initiative acceptance |
| VRC-07 | Keep executable validation and each legacy migration in separate correlated initiatives | Proposed; required by current type and scope specifications |
| VRC-08 | Use only `evidence/non-authoritative/realizations/**`, remove top-level aliases, and prohibit in-place realization promotion | Proposed; source-authorized, pending initiative acceptance |

Detailed open options and human gates are in
[open-questions.md](open-questions.md). Source-authorized directions still
require acceptance of this initiative's exact coherent baseline.

## Boundaries and ownership

| Component or record | Responsibility | Authoritative state | Must not own |
|---|---|---|---|
| Authoritative specification 09 | Canonical grammar, cardinality, self-contained/successor semantics, record ownership, workflow integration, migration limits | Binding after accepted effective delivery | Project-specific status or legacy mapping decisions |
| Project initiative index | Canonical correlation row and navigation | Project-local identity registry | Initiative lifecycle transitions or evidence authority |
| Initiative README | Detailed scope, current lifecycle, append-only history, links to receipts/verification | Initiative-local lifecycle authority | Project-wide identity uniqueness by itself |
| Realization-suite index | Permanently non-authoritative suite identity, boundary, document catalog, and reciprocal links at the canonical evidence path | Historical proposal input | Acceptance, specification, implementation, completion, or in-place promotion |
| Git branch/base record | Exact branch, base branch, and base commit identity | Git traceability | Acceptance, compatibility, release, or completion |
| Validator implementation consumer | Objective syntax, reciprocity, uniqueness, orphan, and lifecycle/evidence checks | Product behavior under separate accepted implementation initiative | Semantic human decisions or automatic repair |

## Domain model and authoritative evidence

### Model

For project P, let V, S, I, and B be allocated work versions, realization-suite
IDs, initiative IDs, and dedicated branch identities. The canonical register
defines one tuple T = (P, V, S, I, B). Within P:

- projection from T to each of V, S, I, and B is unique;
- reverse lookup from each allocated identity returns exactly the same T;
- the initiative type and paths are attributes of I, not new tuple keys;
- captured base branch and base commit are immutable preparation evidence;
- predecessor/successor links form lineage without reusing identity; and
- lifecycle status is linked evidence owned by I, not a property inferred from
  V, S, or B.

A realization suite may contain several notes only if every note passes the
same cohesion test. A note with an independent outcome, owner, authority
boundary, output family, verification claim, compatibility obligation, or
lifecycle triggers a new tuple.

Every suite and note is stored beneath the project-local
`evidence/non-authoritative/realizations/**` hierarchy. No top-level
`realizations/` alias is valid. When an authority accepts a claim derived from
a realization, it creates or revises a separate authoritative evidence,
decision, or accepted initiative record that cites the source; the source
artifact retains its path, identity, and non-authoritative standing.

### Binding requirements

- [Evidence authority specification](../../../evidence/authoritative/LLM/01_Codex_Evidence_Authority_Specification.md)
  governs source standing and revision preservation.
- [Initiative governance specification](../../../evidence/authoritative/LLM/02_Codex_Initiative_Governance_Specification.md)
  governs self-contained records and separate acceptance.
- [Lifecycle specification](../../../evidence/authoritative/LLM/04_Codex_Initiative_Lifecycle_Specification.md)
  governs states, transitions, and lifecycle evidence.
- [Git specification](../../../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md)
  governs branch/base capture and worktree safety.
- [Scope specification](../../../evidence/authoritative/LLM/06_Codex_Initiative_Scope_Specification.md)
  governs mandatory splits.
- [Decision receipt specification](../../../evidence/authoritative/LLM/07_Codex_Human_Decision_Receipt_Specification.md)
  governs migration and acceptance decisions.
- [Workflow specification](../../../evidence/authoritative/LLM/08_Codex_Initiative_Workflow_Specification.md)
  governs stage order and record ownership.

## State and persistence

| State | Durable source | Live or derived state | Write owner | Recovery rule |
|---|---|---|---|---|
| Work-version allocation and tuple | Project initiative index in Git | Status/navigation projections | Stage 0, then owning workflow stages for linked evidence only | Stop on duplicate/drift; preserve original allocation and reconcile from evidence |
| Realization-suite identity and boundary | Suite index under `evidence/non-authoritative/realizations/**` in Git | Note catalog views | Stage 0 for new work; migration initiative for legacy work | Preserve source identity and permanent non-authoritative standing; never rewrite history to imply prior conformance |
| Initiative lifecycle | Initiative README and linked receipts/verification | Project status row | Owning lifecycle stage | Add correction/history entry; never infer transition from tuple |
| Branch and base identity | Suite/index/README Git metadata plus repository history | Current branch availability | Stage 0 records; later stages verify | Preserve recorded identity even if later deletion is separately authorized |
| Protected-source canonical content | Protected files plus .tadp-lock.json | Validation findings | Accepted delivery and authorized lock refresh | Restore unexplained drift or stop; refresh only after reviewed authorized change |

## Primary workflows

### New tuple preparation

**Preconditions:** Git repository, checked-out base, clean worktree, canonical
unused version, unique suite/initiative/branch/path proposal, readable
templates, and unambiguous type.

1. Preflight syntax, uniqueness, target paths, branch, base branch, and base
   commit without writing.
2. Create initiative/v<major>.<minor>-<slug> from the captured base.
3. On that branch, create the suite index, canonical correlation row, and
   minimal initiative skeleton as one preparation unit.

**Success result:** One Proposed tuple with reciprocal links and captured base.

**Failure result:** No partial allocation; stop and report the exact conflict.
If a Git branch was created before a later atomic write failed, preserve it,
record the partial state, and use recovery rather than silently reusing or
deleting identity.

### Later-stage continuity

**Preconditions:** Prepared tuple and active recorded branch.

1. Re-read the canonical row and reciprocal records.
2. Verify exact version token, suite, initiative, branch, base, paths, and
   lifecycle evidence ownership.
3. Stop on drift; return to the owning stage without renumbering.

**Success result:** The stage consumes the same tuple and updates only its
owned records.

**Failure result:** A precise blocker, preserved evidence, and recovery owner.

### Mandatory split or substantive successor

**Preconditions:** A split trigger or material change has been evidenced.

1. Preserve the earlier tuple and exact accepted/completed claim.
2. Allocate a new canonical version and a new suite, initiative, branch, and
   row.
3. Link predecessor/successor and compatibility/migration consequences.

**Success result:** Separate self-contained claims and lifecycle evidence.

**Failure result:** The broad or changed claim remains unaccepted or returns
to Proposed; no sibling substitutes for missing local records.

### Legacy migration

**Preconditions:** Inventory row, preserved source identity, and sufficient
evidence for the proposed mapping.

1. Normalize bare vN to vN.0 only when evidence proves notation-only identity.
2. Preserve broad and dot-scoped identities separately when meaning may differ.
3. Ask the exact human question before any meaning-changing mapping.
4. Migrate each resolved tuple on its own correlated branch after adoption.

**Success result:** Traceable mapping without fabricated lifecycle evidence.

**Failure result:** Ledger blocker and preserved identities; no silent rewrite.

## Interfaces and integration

| Interface | Producer or caller | Consumer or handler | Compatibility rule |
|---|---|---|---|
| Correlation row schema | Stage 0 | Later prompts, status view, validator | Additive fields must preserve canonical owner and reciprocal identity |
| Realization-suite index metadata | Stage 0 or legacy migration | Proposal and initiative workflows | Canonical path is `evidence/non-authoritative/realizations/**`; evidence standing remains non-authoritative permanently |
| Initiative README metadata | Stage 0 then owning stages | Status, acceptance, delivery, finalization | Lifecycle remains README-owned and receipt-backed |
| Validator finding contract | Accepted design handoff | Future implementation initiative | Diagnostics only; no repair or human-decision inference |
| Protected lock authority | Accepted design delivery | Protection tool and commit guard | Authority string must exactly record the authorized instruction |

## Failure and recovery

| Failure | Detection | Durable effect | Recovery | Required evidence |
|---|---|---|---|---|
| Noncanonical version | Grammar/numeric parser | No allocation | Correct proposed token before Stage 0 writes | Preflight result |
| Duplicate version, suite, initiative, or branch | Project scan and Git ref scan | No new tuple | Select a genuinely new tuple through preparation | Conflict diagnostic and project index |
| Missing reciprocal link or orphan | Graph validation | Affected stage blocked | Reconcile from canonical row and source history; never invent | Validator finding and Git/source evidence |
| Dirty worktree | Git preflight | No branch creation | User resolves unrelated work; no stash/move/absorb | Git status |
| Partial preparation | Post-write tuple audit | Preserved partial records/ref | Record partial state and retry owning Stage 0 idempotently | Branch/ref state and diff |
| Top-level realization alias or noncanonical realization path | Path/consumer audit | Affected preparation or delivery blocked | Move only through an authorized preservation-aware migration, reconcile links, and keep standing non-authoritative | Exact source identity, Git history, and path diff |
| Meaning-changing migration ambiguity | Ledger comparison | Mapping remains open | Human decision receipt or preserved unresolved row | Exact sources and question |
| Protected-source drift | Lock check | Delivery/commit blocked | Explain and restore or authorize exact source revision; refresh last | Lock diff, authority, verification |
| Tuple drift after acceptance | Later-stage continuity check | Delivery stops | Return to alignment and acceptance if claim changes | Canonical row, README, branch, receipts |

## Security and authorization

- **Trust boundary:** Repository-local governance records and Git; no runtime
  trust boundary is introduced.
- **Authentication:** Human identity is the task's User and recorded project
  owner; external identity verification is outside this design.
- **Authorization:** Exact user instructions govern invariant edits, decisions,
  acceptance, protected locks, and publication within their recorded scope.
- **Secrets:** No secrets belong in tuple metadata, diagnostics, prompts,
  ledgers, or verification output.
- **Audit:** Git commits, lifecycle history, decision receipts, protected locks,
  and validator results form the traceability record.
- **Data handling:** No product or personal data is required; migration
  evidence records only repository identities and source locators.

## Observability and operations

| Signal or operation | Purpose | Required dimensions or safeguards |
|---|---|---|
| Correlation validation findings | Identify syntax, duplicate, orphan, reciprocity, branch, and evidence/lifecycle issues | Stable code, exact path/identity, no automatic repair |
| Project index/status view | Navigate tuple and current gate | Links canonical row and README evidence; no inferred state |
| Git status/branch/base capture | Prove preparation and active branch identity | Include staged, unstaged, untracked, base branch, and commit |
| Protected-source check | Detect unauthorized or incomplete reusable-source drift | Run before refresh, expect only explained stale-lock findings, refresh last |
| Regression tests | Prove objective parser/graph behavior | Positive and negative cases from the accepted handoff |

## Compatibility migration and rollout

The revision is additive for new work but not retroactive authority. Existing
initiatives may finish under their recorded compatible workflow revision or
migrate through an explicit change record. Existing canonical realization
paths and links remain historical evidence. Obsolete top-level README aliases
are removed because they contain no realization records; links are reconciled
to the canonical evidence hierarchy without rewriting source content. Bare
identities receive compatibility mapping rather than silent renames unless
notation-only identity is proven.

The effective point is the commit containing the complete accepted
authoritative revision, synchronized protected consumers, refreshed locks, and
design delivery evidence. The separately accepted validator implementation
may follow; until it does, projects enforce the invariant through governed
records and review rather than claiming executable enforcement.

## Testing strategy

| Level | Behavior proved | Required environment or fixture |
|---|---|---|
| Specification review | Grammar, numeric ordering, bijection, self-contained/successor, realization placement/standing, authority, and workflow clauses are coherent | Authoritative suite and initiative source map |
| Template/prompt contract | Every consumer creates or verifies reciprocal metadata without changing stage numbering | Protected protocol/example source matrix |
| Migration review | Required identities and v4 case preserve source standing and ambiguity | Git history, current example suites, and migration ledger |
| Protection | Authorized protected content and locks agree | tadp_protect check before/after refresh |
| Future unit tests | Canonical positives/negatives and numeric ordering | Separate validator implementation initiative |
| Future integration | Duplicate, reciprocal, orphan, branch, split, lifecycle, and legacy cases | Temporary project fixtures under separate implementation initiative |

## Risks and edge cases

| Risk or edge case | Impact | Mitigation or decision |
|---|---|---|
| Unbounded integer components exceed machine types | Incorrect rejection or ordering | Specify arbitrary-size integer parsing; VRC-03 |
| Lexicographic comparison places v13.10 before v13.9 | Incorrect successor order | Numeric tuple comparison; VRC-03 |
| Same branch reused by two initiatives | Bijection violation and mixed traceability | Unique reverse mapping and Stage 0 Git preflight; VRC-04 |
| Version/status conflation | False acceptance or completion | Explicit authority/lifecycle prohibition in spec and templates |
| Parent or subinitiative shares a version | Hidden independent lifecycle | New tuple for every initiative; VRC-05 |
| Reopening changes accepted claim materially | Silent scope expansion | New substantive successor tuple; unchanged-claim exception only |
| Missing requested v4/v4.1 source | Fabricated migration | Preserve requested and observed identities; VRC-01 |
| Top-level realization alias or in-place promotion | Competing source homes or false authority | Canonical path audit, separate accepted derivative record, and VRC-08 |
| Protocol/example drift | Divergent adopter behavior | Protected parity matrix, checks, and matched locks; VRC-A03 |

## Deferred work

- Executable validator, test, hook, and documentation implementation after
  accepted design, via a new correlated implementation initiative.
- Each example legacy tuple migration after protocol adoption, via its own
  correlated initiative and branch.
- Any v3/v3.1 or v4/v4.1 meaning-changing mapping until its explicit human
  decision receipt exists.

## Architecture and specification acceptance

This proposed specification is ready for Stage 7 only after assumptions are
receipt-backed, VRC-01 is resolved or the exact accepted baseline explicitly
retains its blocker without applying a mapping, source mapping and scope agree,
the legacy ledger is reviewable, every protected destination is enumerated,
and the implementation handoff defines objective verification without
including product work in this initiative.
