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

## Adoption and compatibility

A governing revision takes effect at the coherent Git commit containing its
authorized sources, reconciled consumers, verification and protected locks.
Record the actual immutable commit; never invent a future identifier.

Adoption is prospective and explicit. Record the governing revision, human
authority, actual project baseline, affected active work and required migration
dispositions in the adopting project's profile and applicable ledgers.
Installation, synchronization or a lock initialization does not establish
adoption, accept unexplained drift, or change a live initiative's decisions,
acceptance, lifecycle, execution assignment, integration or release status.

Preserve existing sources, compatible governing revisions, versions, notes,
initiatives, paths, branches and accepted claims until an authorized,
evidence-backed migration. Adoption never retroactively interprets prompts,
waives gates, resolves questions, accepts work, reopens claims or manufactures
completion evidence.
Use the protected-source integrity migration procedure before claiming source
protection is active.

Specification 09 governs major, minor and patch scopes, precise many-note and
many-initiative provenance, coherent same-initiative revision, bounded intake
placement and necessary reopening, and dedicated or shared execution. Each
initiative retains independent human acceptance and ordinary completion
evidence. Specification 05 permits child-to-immediate-parent local integration
only after recorded closure authority and required checks; scope closure,
remote actions and branch deletion retain their own authority.

For coherence adoption, capture the immutable Git snapshot immediately before
adoption as the project's Coherence revision baseline. Unchanged terminal
initiatives at that baseline need no retrospective completion review. New
work, completion and later refinement follow specification 10, including
open-effort inventory, conflict recording and authorized reopening.

Specification 11 governs directive interpretation, list scheduling and
specifically documented exceptions. Unexcepted gates, truthful evidence,
protected sources, stage numbering, initiative types and ordinary lifecycle
meanings remain binding.

Use the [canonical coverage and use map](../../../template/TEMPLATE-COVERAGE.md)
to locate reusable sources. Binding use rules are in
[specification 02](02_Codex_Initiative_Governance_Specification.md#canonical-template-selection-and-use),
and the shared preceding-stage preparation procedure is in
[specification 08](08_Codex_Initiative_Workflow_Specification.md#documentary-prerequisite-preparation).
Preparation does not supply missing identity, authority, actual work or
verification and does not change stage ownership or acceptance requirements.

The [owning root requirement](05_Codex_Git_Workflow_Specification.md#requirement)
distinguishes installed projects, Git worktrees, the source distribution and
protected scaffold libraries. See the
[prospective adoption guide](../../../docs/guides/project-root-installation-migration.md).

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

The project-root `../../../AGENTS.md` is the Codex entry point because Codex loads
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

