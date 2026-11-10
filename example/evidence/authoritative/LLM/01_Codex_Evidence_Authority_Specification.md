# Codex evidence authority specification

## Scope

This specification governs how Codex discovers, classifies, compares, cites,
and acts on repository evidence. It applies to analysis, planning, initiative
authoring, implementation, review, testing, documentation, and lifecycle
updates.

## Evidence classes

### Invariants and authoritative evidence

All artifacts under `..` are authoritative baseline evidence.
Sources elsewhere that the repository explicitly classifies as authoritative
have the same binding standing for their stated scope.

`../../non-authoritative` is the canonical location for repository clues
that lack binding standing. Do not create a second authority tree.

Codex must:

- read all applicable invariant material before making a normative decision;
- preserve the original claim, scope, identity, revision, and acceptance
  context;
- align initiatives, products, implementation, verification, and status claims
  with every applicable invariant; and
- cite the most precise applicable claim, section, decision, or stable ID.

Codex must not modify an invariant merely to make a proposal, initiative,
product, test, or existing implementation appear coherent. An invariant may be
changed only when an explicit human instruction authorizes that specific
change. The revision must preserve the earlier record and document the
authority, reason, affected scope, effective point, compatibility or migration
effect, and successor relationship.

### Non-authoritative evidence

Non-authoritative material includes observations, examples, recommendations,
exploratory analysis, prompts, historical notes, proposals, and realization
notes unless a named authority separately accepts a claim as binding.

Codex may use non-authoritative material to:

- discover relevant questions or missing evidence;
- resolve ambiguity among interpretations that all comply with invariants;
- compare invariant-compatible options;
- locate higher-standing evidence; or
- frame the smallest bounded initiative or investigation needed.

Codex must state the material's limits when relying on it. Non-authoritative
evidence must not override, narrow, weaken, reinterpret, or resolve a
contradiction with an invariant. Convenience, recency, implementation fit, and
detail do not increase its authority.

## Evidence-use protocol

For every material claim or change, Codex must:

1. Identify the exact subject, scope, and requested outcome.
2. Inventory applicable invariants before consulting lower-standing sources
   for a decision.
3. Separate binding claims, accepted specifications, observed behavior, and
   contextual clues.
4. Compare the proposed conclusion against every applicable invariant.
5. Cite the precise evidence supporting the conclusion and state any material
   limitation or missing evidence.
6. Map the conclusion to the initiative decision, specification, product
   destination, verification, or status claim that consumes it.
7. Record contradictions, unresolved ambiguity, and unavailable external
   evidence instead of silently choosing an outcome.

Directory names, file extensions, author identity, implementation status, or a
prompt's wording do not establish authority by themselves. Authority comes
from repository classification and explicit acceptance.

## Invariant contradictions

Nothing may be accepted, implemented, released, or reported as complete while
its bounded claim conflicts with an applicable invariant.

When Codex finds a conflict, it must:

1. Preserve both claims and their source identities.
2. Stop the affected decision or work while continuing independent work that
   remains authorized and invariant-compatible.
3. Add an explicit entry to
   [the invariant conflict register](03_Codex_Invariant_Conflict_Register.md).
4. Record the same conflict in the affected initiative's source mapping,
   decision register, status, or other canonical conflict location.
5. Identify the exact invariant claim, conflicting claim or behavior, affected
   scope, consequence, owner, and human decision required.
6. Resolve the contradiction only through an invariant-compatible correction
   of lower-standing work or an explicitly authorized invariant revision or
   exception.

A conflict-register entry is authoritative evidence that the contradiction
exists. It does not make the conflicting claim authoritative and does not
resolve the contradiction.

This specification explicitly authorizes Codex to append factual conflict
entries to the register when a contradiction is directly evidenced. It does
not authorize Codex to alter the governing invariant, approve an exception,
select a disputed interpretation, or delete a resolved entry.

## Missing and conflicting lower-standing evidence

When lower-standing sources disagree without contradicting an invariant,
Codex may compare their methods, dates, scope, and limitations. It may recommend
an invariant-compatible interpretation, but it must preserve uncertainty when
the evidence does not support a conclusion.

When required evidence is unavailable, Codex must complete independent
authorized work, document the exact missing evidence and its owner, and keep
the affected gate open. It must not convert a local test into a production
claim, a proposal into acceptance, a recommendation into a human decision, or
an absence of failure into proof.

## Traceability requirements

Every normative initiative or product claim must be traceable through:

```text
invariant or accepted authority
        -> initiative interpretation or decision
        -> specification and bounded work
        -> product or evidence destination
        -> verification and truthful lifecycle status
```

Copied text is not a substitute for a source link. When a claim is repeated,
the authoritative source retains ownership and the copy must not drift.

## Evidence review checklist

- [ ] Applicable invariants were read before a normative conclusion was made.
- [ ] Binding claims and contextual clues are visibly distinguished.
- [ ] Every cited source has a precise locator and stated scope.
- [ ] No non-authoritative source is used to resolve an invariant conflict.
- [ ] Observed implementation is not mistaken for architectural authority.
- [ ] Missing, stale, or contradictory evidence remains visible.
- [ ] Verification supports the exact claim being made.

