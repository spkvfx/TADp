# Codex invariant suite index

## Purpose

This suite defines how Codex must interpret and use evidence when working in a
TADp repository. It is intentionally broad. Project-, product-, and
initiative-specific invariants may impose stricter requirements, but they may
not weaken this suite.

Everything under `..` is part of the authoritative baseline. It
serves as the durable architectural source of truth for specifications,
products, implementation, verification, and status claims. Invariant material
is preserved unless an explicit human instruction authorizes a particular
change.

Authoritative evidence belongs under the single `..`
hierarchy.

## Protected baseline

This suite is a protected source tree. During ordinary work, Codex may read and
cite it but must not edit, replace, rename, move, or delete it. A change is
permitted only when an explicit human instruction identifies the particular
invariant revision or addition being authorized; general implementation,
alignment, repair, completion, or validation instructions are insufficient.

The directory-scoped `AGENTS.md` repeats that edit boundary at the point of
use. `.tadp-lock.json` records canonical-content SHA-256 digests for every other
file in this directory, and repository validation rejects missing, added,
removed, or changed files that do not match that lock. The lock is integrity
evidence, not authority to revise an invariant. It may be refreshed only after
the authorized revision has satisfied the preservation, impact, compatibility,
migration, and consumer-reconciliation requirements of this suite.

### Protection revision record

- **Authority:** Explicit human instruction on 2026-11-10 to protect reusable
  templates and the authoritative LLM invariant suite from inadvertent LLM
  edits.
- **Reason:** A copied TADp project needs a durable distinction between
  read-only reusable sources and editable instantiated records.
- **Affected scope:** Codex edit instructions, template and invariant integrity
  locks, validation, the local commit gate, adoption guidance, and migration
  guidance. The substantive meaning of specifications 01 through 08 is
  unchanged.
- **Effective point:** The Git commit that introduces the complete
  protected-source control set.
- **Compatibility and migration:** Existing initiatives and accepted claims do
  not change. Existing adopters must use the protected-source integrity
  migration guide before claiming the new controls are active; initializing a
  lock does not accept unexplained drift.
- **Successor relationship:** This protection revision succeeds the prior
  suite-index revision only for source-integrity handling. Git history
  preserves the predecessor and every earlier substantive invariant.

### Version-realization-initiative correlation revision record

- **Authority:** The User's explicit
  `prompts/version-realization-initiative-correlation-protocol-change.md`
  instruction, executed on 2026-11-11, authorizes the exact correlation
  invariant and affected protected-source revisions.
- **Reason:** Give every governed work unit one immutable project-local version,
  one realization suite, one self-contained initiative, and one dedicated Git
  branch with reciprocal traceability.
- **Affected scope:** Work identity, realization-suite structure, initiative
  metadata and scope, branch traceability, workflow Stage 0 and later handoffs,
  legacy compatibility, reusable sources, validation, and adoption guidance.
- **Effective point:** The first Git commit containing the coherent
  specification 09 revision, every necessarily affected consumer, validation
  behavior, regression tests, and authorized protected-source locks. Each
  project records that commit before allocating governed tuples.
- **Compatibility and migration:** The revision governs post-effective
  allocations, explicitly migrated pre-effective tuples, and post-effective
  successors or mandatory splits. Pre-effective records require a complete
  non-inferred migration-ledger disposition and may otherwise remain under
  their recorded earlier compatible workflow revision.
- **Successor relationship:** Specification 09 succeeds the earlier suite only
  for work identity and correlation. Specifications 01 through 08 continue to
  govern evidence, governance, conflicts, lifecycle, Git, scope, human
  decisions, and workflow except where they expressly reference this revision.

### Initiative coherence and completion-feedback revision record

- **Authority:** The User's exact 2026-11-12 instructions preserved in
  [COH-DR-001](../../../decisions/COH-DR-001-initiative-coherence.md).
- **Reason:** Count open effort as work, document incompatible efforts,
  route completion learning to open initiatives, and require explicit
  reopening before refining closed claims.
- **Affected scope:** Specifications 02, 04, 07, and 08, new specification 10,
  reusable sources for every initiative type, validation, tests, documentation,
  and the protocol and installed example adoption records and locks.
- **Effective event:** Coherent adoption with a captured pre-revision Git
  baseline. Earlier closed claims remain historical; no retrospective
  acceptance, completion review, or reopening is invented.
- **Successor relationship:** Specification 10 strengthens coherence and
  feedback handling without changing evidence precedence, type boundaries,
  human decision gates, stage numbering, or specification 09 successor rules.

### Positional prompt keyword revision record

- **Authority:** The User's 2026-11-12 instruction to execute
  `prompts/positional-gate-switches-protocol-change.md`, captured in
  [KWD-DR-001](../../../decisions/KWD-DR-001-positional-keywords.md).
- **Reason and scope:** Establish canonical extensible directive vocabulary,
  positional composition, list execution, preview, local access, independent
  review, and precise recorded exceptions across instructions and consumers.
- **Effective event:** The first coherent specification 11 revision commit,
  including reconciled consumers, verification, and authorized locks.
- **Compatibility and migration:** Prospective adoption only; no historical
  prompt, decision, gate, question, initiative, or lifecycle claim changes.
  Existing adopters retain their recorded revision until adoption and any
  applicable exception authority are recorded.
- **Successor relationship:** Specification 11 qualifies earlier gate clauses
  only through its specific authority and documentation process. Unexcepted
  rules, protected sources, locks, evidence truth, ordinary lifecycle meanings,
  type boundaries, and substantive-successor requirements remain binding.

### Version-scope grouping, delegated intake and closure integration revision

- **Authority:** The User's 2026-11-12 instruction to execute
  `prompts/version-scope-grouping-and-branching-protocol-change.md`, captured in
  [VSG-DR-001](../../../decisions/VSG-DR-001-version-scope-grouping.md).
- **Reason:** Several narrow initiatives may share an immutable realization
  scope while retaining precise provenance and independent acceptance.
- **Affected clauses:** Specification 09's bijection, two-component-only
  version syntax, single-outcome suite, exclusive branch and mandatory
  substantive-successor requirements; specifications 02, 04, 07, 08 and 10's
  necessary per-target human reopening clauses; specification 05's hierarchy,
  finalization and local integration contract; necessary specification 01/06
  references, reusable sources, entry points, consumers, validation, tests,
  guidance, adoption records and locks. Specification 11 changes only its
  affected reopening/successor cross-reference, preserving registry semantics.
- **Effective event:** The first coherent Git commit containing reconciled
  sources and consumers, verification, mirrors and authorized lock updates.
  Projects adopt explicitly with their governing commit, baseline and ledger.
- **Compatibility:** Preserve legacy versions, suites/notes, initiatives,
  paths, branches and claims under their recorded compatible revision until
  evidence-backed migration. Distribution synchronization does not migrate
  live work. Historical PR evidence remains preserved.
- **Successor relationship:** This revision supersedes only the named clauses.
  The earlier revision records above preserve their historical contracts; their
  old tuple and mandatory-successor descriptions do not govern new allocations
  after explicit version-scope adoption. Git preserves prior invariant text.

The current specification 09 permits major, minor and patch scopes, many-note
and many-initiative provenance, coherent same-initiative revision, bounded LLM
intake placement/reopening and dedicated/shared placement. Human acceptance
and ordinary completion evidence remain required. Specification 05 defines
child-to-immediate-parent local integration after recorded closure authority,
separate scope closure and human-managed PRs. No protocol adoption itself
reopens, accepts, closes, merges or migrates live work.
## Documents

1. [Codex evidence authority specification](01_Codex_Evidence_Authority_Specification.md)
   defines evidence classes, precedence, invariant use, and contradiction
   handling.
2. [Codex initiative governance specification](02_Codex_Initiative_Governance_Specification.md)
   defines realization standing, initiative quality, human decision gates, and
   revision discipline.
3. [Codex invariant conflict register](03_Codex_Invariant_Conflict_Register.md)
   is the required durable record for contradictions discovered by Codex.
4. [Codex initiative lifecycle specification](04_Codex_Initiative_Lifecycle_Specification.md)
   defines lifecycle states, legal transitions, transition evidence, and
   reopening history.
5. [Codex Git workflow specification](05_Codex_Git_Workflow_Specification.md)
   makes Git history and initiative branches part of protocol traceability.
6. [Codex initiative scope specification](06_Codex_Initiative_Scope_Specification.md)
   defines narrow scope, mandatory split triggers, and legacy decomposition.
7. [Codex human decision receipt specification](07_Codex_Human_Decision_Receipt_Specification.md)
   makes explicit human authority durable and traceable to reconciled records.
8. [Codex initiative workflow specification](08_Codex_Initiative_Workflow_Specification.md)
   defines authoritative stage order, acceptance, type-specific delivery,
   record ownership, handoffs, and recovery behavior.
9. [Codex version-realization-initiative correlation specification](09_Codex_Version_Realization_Initiative_Correlation_Specification.md)
   defines immutable version scopes, exact provenance, delegated intake,
   revision-cycle execution placement, adoption, migration-ledger requirements,
   and correlation validation.
10. [Codex initiative coherence specification](10_Codex_Initiative_Coherence_Specification.md)
    defines open effort as work, cross-initiative conflict records, completion
    feedback, closed-claim preservation, and prospective adoption controls.
11. [Codex prompt keyword specification](11_Codex_Prompt_Keyword_Specification.md)
    is the canonical extensible directive registry and governs universal
    interpretation, positional settings, action-list scheduling, explicit
    exceptions, confirmation, locks, and keyword registration.

The repository-root `../../../AGENTS.md` is the Codex entry point because Codex loads
repository guidance from that standard location. It summarizes this suite but
does not replace it. When the summary and this suite differ, this suite governs
the evidence protocol and the more restrictive instruction applies.

Read and apply specification 11 when interpreting every governed TADp task,
including ordinary requests and analysis without a stored prompt. Registry
examples and supporting records remain inert. A requested setting is not
authority to waive a rule. A specifically authorized, documented exception
governs only its named rule, block, revision, and duration; compare all other
instructions under ordinary precedence rather than treating a keyword as a
blanket override. No switch weakens locks or truthful evidence.

## Normative language

`Must`, `must not`, `required`, and `may only` are binding. `Should` expresses
the expected practice unless a documented, invariant-compatible reason makes
it inapplicable. `May` grants permission within the stated boundary; it does
not grant permission to revise an invariant.

## Default precedence

Apply evidence in this order:

1. Applicable governing invariants and their explicit revisions or exceptions.
2. Released contracts and accepted architectural decisions that comply with
   those invariants.
3. Accepted initiative specifications within their declared scope.
4. Verified product and implementation evidence, interpreted through the
   governing specifications and invariants.
5. Proposed initiatives, realizations, observations, examples, prompts,
   historical records, and other non-authoritative material.

An explicit human instruction may authorize a particular invariant revision,
exception, assumption disposition, or decision. Codex must not infer that
authority from urgency, convenience, a broad implementation request, or the
existence of contradictory lower-standing material.

## Core rules

- No lower-standing record may override or silently reinterpret an invariant.
- Newer material is not automatically stronger material.
- Implemented behavior is evidence of current behavior, not authority to
  contradict the architecture.
- A prompt describes requested work; it is not evidence that a premise is true
  or that a gate has passed.
- A work version, realization suite, correlation row, or branch proves identity
  only; none establishes evidence authority, acceptance, implementation,
  completion, compatibility, or release.
- Missing evidence remains missing. Codex must not fabricate verification,
  acceptance, ownership, qualification, or release evidence.
- Every material conclusion must retain a traceable path to the evidence and
  authority that support it.
- Open initiative effort must be considered as work without promoting its
  authority. Document incompatible efforts, review completion feedback against
  open initiatives, and require recorded reopening under specification 09 intake
  delegation or separate human authority before refining a closed claim.

