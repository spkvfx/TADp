# TADp instructions for Codex

Before changing architecture, specifications, initiatives, products, or
evidence, read the applicable documents in the TADp project root's
`evidence/authoritative/LLM`, beginning with the suite index.

The project root's `template/**` and
`evidence/authoritative/LLM/**` trees are protected sources. Ordinary project
and initiative work may read or copy them but must not edit, fill, rename,
move, or delete them. Copy a reusable source to its declared destination
outside `template/` before specializing it. A protected source may change only
when the user explicitly requests that exact reusable template or invariant
change. Never refresh its `.tadp-lock.json` or use the protected-update commit
override without the same explicit authority.

- Treat every artifact under `evidence/authoritative` as binding invariant
  authority. Do not modify it unless the user explicitly instructs the specific
  invariant change.
- Never make an initiative, product, test, implementation, or status claim
  conflict with an invariant. Correct lower-standing work or record an
  invariant conflict.
- Use `evidence/non-authoritative` only as clues for invariant-compatible
  interpretation. It cannot resolve a contradiction with authoritative
  evidence.
- Treat realizations as broad inputs and initiatives as the coherent, bounded
  specifications for work.
- Count open initiative effort as work in coherence review without promoting
  its evidence standing. Before completion, compare current open work and
  affected closed claims; preserve incompatible claims and effort in
  `initiatives/work-conflicts.md` and affected records. Invariant conflicts
  also require the authoritative conflict register. Stop affected incompatible
  acceptance, execution, or completion.
- Refine open initiatives only through their authorized workflow and human
  gates. Never refine a closed initiative before explicit human reopening,
  a linked receipt, and a legal transition. Preserve prior claims and use a
  successor tuple for substantive changes.
- Require one narrow outcome and acceptance claim. Split independent outcomes;
  use a subinitiative only inside a real parent specification.
- Require explicit human decisions for assumptions, questions, lifecycle
  authority, and exceptions, and preserve each result in a decision receipt.
- Treat initiative acceptance as a separate explicit human-authority stage.
  Alignment and resolved assumptions or questions do not imply acceptance.
- Record only legal lifecycle transitions. Preserve prior claims and document
  every reopening or revision.
- Require Git, a captured base branch, and a dedicated initiative branch.
  Preserve unrelated work and keep commits traceable. Never rewrite shared
  history or merge without explicit authority.
- Require standard execution and completion evidence before making the
  corresponding lifecycle claim. Use the delivery record for design or
  planning and follow exactly one delivery path for the declared type.

Preserve source identity, distinguish observed evidence from accepted
authority, and report only outcomes supported by verification.


