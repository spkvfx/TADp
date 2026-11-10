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
- Missing evidence remains missing. Codex must not fabricate verification,
  acceptance, ownership, qualification, or release evidence.
- Every material conclusion must retain a traceable path to the evidence and
  authority that support it.

