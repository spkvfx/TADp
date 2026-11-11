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
   defines canonical work versions, reciprocal suite-initiative-branch
   identity, effective-point compatibility, migration-ledger requirements,
   and correlation validation.

The repository-root `../../../AGENTS.md` is the Codex entry point because Codex loads
repository guidance from that standard location. It summarizes this suite but
does not replace it. When the summary and this suite differ, this suite governs
the evidence protocol and the more restrictive instruction applies.

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

