# TADp instructions for Codex

When interpreting any TADp task, read and apply the
[prompt keyword specification](evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md).
This includes ordinary requests, analysis, project-local prompts, numbered
workflow prompts, and repository maintenance. Apply operative directives and
list scheduling only as defined there; reading the registry or its examples
does not activate them. Record bounded exceptions before relying on them;
all unexcepted rules and TADp locks remain binding.

Before changing architecture, specifications, initiatives, products, or
evidence, read the applicable documents in
`evidence/authoritative/LLM`, beginning with the suite index.

`template/**` and `evidence/authoritative/LLM/**` are protected source trees.
Ordinary project and initiative work may read or copy them but must not edit,
fill, rename, move, or delete them. Instantiate a template by copying it to its
declared destination outside `template/`, then edit the copy. A protected
source may change only when the user explicitly requests that exact reusable
template or invariant change. Never refresh its `.tadp-lock.json` or use the
protected-update commit override without the same explicit authority.

## Embedded example project root

For this installed example only, treat the directory containing this file as
the TADp project root for every project file, evidence source, prompt,
initiative, product, lifecycle record, validation run, and scope decision.
The resolved
[`INV-CONFLICT-001`](evidence/authoritative/LLM/03_Codex_Invariant_Conflict_Register.md#inv-conflict-001--embedded-example-project-root-and-git-root-invariant)
and
[`EX-GIT-DR-001`](initiatives/decision-receipts/EX-GIT-DR-001-enclosing-worktree-exception.md)
permit the enclosing repository or worktree to supply Git metadata, branch
refs, staging, commits, history, and Git verification only. Verify that it
directly contains this root, and limit every non-Git side effect to this root
and any narrower applicable workflow boundary.

This project-specific exception applies throughout `example/`; it is not
limited to one prompt, initiative set, version, or file list. It does not make
the enclosing TADp repository part of the example project, grant authority to
change a sibling or parent path, relax protected-source rules, or revise the
generic requirement for any other TADp project.

- Treat every artifact under `evidence/authoritative` and every source
  explicitly classified as authoritative evidence as binding baseline
  authority.
- Do not modify, weaken, reinterpret, replace, or delete an invariant unless
  the user explicitly instructs that invariant change. A general request to
  implement, align, repair, or complete work is not such permission.
- Never make an initiative, product, implementation, test, or status claim
  conflict with an invariant. Correct the lower-standing work or record an
  unresolved invariant conflict.
- Use non-authoritative evidence only as a clue: to resolve ambiguity among
  invariant-compatible interpretations, locate stronger evidence, compare
  options, or frame the smallest necessary work. It cannot resolve a
  contradiction with an invariant.
- Treat realization notes as broad initiative inputs, not specifications or
  implementation authority.
- Treat initiatives as the structured specifications for bounded work. Keep
  every initiative internally coherent, mutually coherent with other active
  initiatives, and aligned with all applicable invariants.
- Never create umbrella or multi-purpose initiative containers. Each
  initiative must own one narrowly bounded outcome and acceptance claim. Use
  separately scoped sibling initiatives or subinitiatives when work must be
  decomposed.
- Questions and assumptions require explicit human resolution unless the user
  expressly authorizes another decision method for the stated scope.
- Preserve each human disposition in a linked decision receipt before changing
  its source assumption, question, lifecycle event, or exception record.
- Treat initiative acceptance as a separate explicit human-authority stage.
  Alignment and resolved assumptions or questions do not imply acceptance.
- Reopen or revise an initiative only with a documented reason, authority,
  change record, impact analysis, and cross-record reconciliation.
- Count open effort as work without promoting its authority, document
  incompatible efforts in `initiatives/work-conflicts.md`, and review
  completion feedback against all open initiatives. Require explicit human
  reopening before refining closed claims under specification 10.
- Record only legal lifecycle transitions. Require the standard execution
  record for implementation, the standard delivery record for design or
  planning, and standard completion evidence before any initiative is marked
  `Completed`. Follow exactly one delivery path for the declared type.
- Require Git for every TADp project. Use a dedicated initiative branch from a
  captured base, preserve unrelated work, and keep commits and branch history
  traceable to the initiative. Never rewrite shared history or merge without
  explicit authority.
- Record every discovered contradiction in the invariant conflict register and
  in the affected initiative records. Do not hide it by changing history,
  narrowing a claim, or marking incomplete work complete.

Preserve source identity, distinguish observed evidence from accepted
authority, and report only outcomes supported by verification.

