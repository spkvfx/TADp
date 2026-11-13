# Architecture and authority

## Purpose

TADp is an evidence-governance and work-traceability architecture. Its central
rule is that information must retain both its content and its standing. Two
documents may say similar things while having different authority, scope, or
verification value.

## Authority layers

| Layer | What it establishes | What it cannot do |
|---|---|---|
| Authoritative evidence | Binding invariant conditions for specifications, products, and status claims | Be changed by convenience, implementation drift, or a lower-standing record |
| Accepted decision or initiative specification | A bounded interpretation and authorization compatible with invariants | Govern work outside its recorded scope or revise an invariant implicitly |
| Verified product evidence | What was implemented and what tests or observations show | Convert existing behavior into architectural authority by itself |
| Non-authoritative evidence | Context, observations, research, examples, recommendations, and ambiguity-resolution clues | Override, narrow, or resolve a contradiction with authoritative evidence |
| Realization or proposal | A possible outcome and the reasoning for considering it | Authorize work, confirm assumptions, or prove completion |

The normative precedence is defined in the
[Codex invariant suite](../../evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md)
and
[evidence authority specification](../../evidence/authoritative/LLM/01_Codex_Evidence_Authority_Specification.md).

## Traceability chain

Every material requirement should remain traceable through this chain:

```text
authoritative claim or accepted authority
        -> initiative interpretation or human decision
        -> bounded specification and planned output
        -> product or initiative-evidence destination
        -> verification
        -> lifecycle claim
```

Each arrow requires an explicit link or stable identifier. Repeating text does
not transfer ownership of the claim. The source remains authoritative, and the
consumer records how it interprets that source for its own scope.

## Invariants

Everything under `../../evidence/authoritative` is invariant evidence. Preserve its
identity and history. A human may explicitly authorize a particular revision,
but a broad request to implement, repair, align, or complete work does not
authorize changing the invariant to fit the work.

When an invariant changes legitimately, retain:

- the previous claim and revision identity;
- the human authority for the change;
- the reason and affected scope;
- the effective event;
- compatibility and migration consequences; and
- the successor or exception relationship.

## Human authority

Assumption dispositions, open-question answers, acceptance, reopening,
cancellation, supersession, and invariant exceptions require explicit human
authority unless a human has defined another decision method for the exact
scope.

The decision receipt preserves what the human was asked, what evidence and
limitations were shown, the exact response, the authority under which it
governs, the resulting disposition, and the records reconciled from it. The
receipt proves the decision, not implementation or release.

## Conflict handling

When records conflict:

1. Preserve both claims and their source identities.
2. Determine their evidence class, scope, revision, and applicable authority.
3. Stop only the affected decision or work.
4. Record the contradiction in the authoritative conflict register and the
   affected initiative record.
5. Identify the owner and exact evidence or human decision needed.
6. Resolve the conflict by correcting lower-standing work or through an
   explicitly authorized invariant revision.

Do not make documents appear coherent by deleting uncertainty, changing
history, weakening acceptance criteria, or marking incomplete work complete.

## Explanatory documentation

Developer documents under `..` explain the protocol but are not binding
invariants. They should link to the authoritative source for normative rules.
If a guide conflicts with authority, correct the guide and record any material
effect on work that relied on it.

