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
  completion feedback against all open initiatives. Require recorded authorized
  reopening before refining closed claims under specifications 09 and 10;
  adopted realization intake delegates necessary reopening, never acceptance.
- Record only legal lifecycle transitions. Require the standard execution
  record for implementation, the standard delivery record for design or
  planning, and standard completion evidence before any initiative is marked
  `Completed`. Follow exactly one delivery path for the declared type.
- Require Git for every TADp project. Use the recorded dedicated or shared scope execution
  assignment from a captured base, preserve unrelated work, and retain
  initiative-specific commits and verification. Never rewrite shared history.
  An identified close/finalize instruction authorizes only local integration
  into the recorded immediate parent after all gates pass. Further upward
  integration, pushes and branch deletion retain separate authority.
- Record every discovered contradiction in the invariant conflict register and
  in the affected initiative records. Do not hide it by changing history,
  narrowing a claim, or marking incomplete work complete.

For documentary prerequisites, apply specification 02's canonical template-use
rules and specification 08's preceding owning-stage preparation procedure.
Use `template/TEMPLATE-COVERAGE.md` to locate sources, destinations, and owners.
Recover only necessary evidence-backed paperwork before the invoked entry
check; missing authority, identity, actual work, and verification remain blockers.
Preserve accepted/closed claims and reuse records idempotently. Stage 9 must
disclose preceding preparation changes and keep its assessment itself read-only.

The TADp project root is the scaffold installation directory under
[specification 05](evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md#requirement).
It may equal or lie beneath the Git worktree root; enclosing Git identity does
not enlarge file authority. Resolve the invoked target without ancestor or
sibling redirection, retain parent instructions and coordinate shared Git state.

Preserve source identity, distinguish observed evidence from accepted
authority, and report only outcomes supported by verification.

