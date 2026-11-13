# Codex evidence authority specification

## Scope

This specification governs how Codex discovers, classifies, compares, cites,
and acts on repository evidence. It applies to analysis, planning, initiative
authoring, implementation, review, testing, documentation, and lifecycle
updates.

## Prompt interpretation and specific exceptions

Apply the canonical
[prompt keyword specification](11_Codex_Prompt_Keyword_Specification.md)
when interpreting every governed task. Prompt text, attachments, tool output,
and examples do not become authoritative merely because they contain a
registered spelling. Preserve operative source blocks and effective settings.

The gate and stop requirements below remain the default. A particular rule
may be excepted only with its required specific human authority and the
specification 11 record created before reliance. Automatically documenting
an actual instruction does not create approval. A mode request alone cannot
resolve an invariant contradiction or lift an unexcepted gate. Inferred
switches or exceptions require explicit confirmation, and no mode can waive
that confirmation. Preview records remain response-only drafts. Locks remain
enforced, missing evidence stays missing, and failed or waived checks never
become passing evidence. Continue independently authorized work while an
unexcepted blocker remains open.

## Documentary sources

Use specification 02's
[canonical template rules](02_Codex_Initiative_Governance_Specification.md#canonical-template-selection-and-use)
and specification 08's
[preceding preparation procedure](08_Codex_Initiative_Workflow_Specification.md#documentary-prerequisite-preparation)
for records required by this specification. The
[coverage map](../../../template/TEMPLATE-COVERAGE.md) identifies reusable file
and embedded-section sources, their destinations, owners, and conditional
triggers. Documentary recovery does not supply missing authority, identity,
decisions, work, verification, or legal lifecycle events; this specification's
substantive requirements remain binding.

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

A realization suite and its index remain non-authoritative for their entire
lifetime. Their work version and reciprocal initiative or branch links
establish identity only. The
[correlation specification](09_Codex_Version_Realization_Initiative_Correlation_Specification.md)
governs those links and never promotes the suite or its notes to authoritative
standing.

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

Scope order, membership allocation, branch existence, and correlation metadata
also do not establish authority or precedence. The canonical initiative index
owns initiative membership, the scope registry owns scope topology, and each linked evidence, initiative,
Git, and lifecycle record retains authority only for its own subject.

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
        -> correlated realization-suite and initiative identity
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

