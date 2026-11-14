# TADp instructions for Codex

## This development project's boundary

This is the installed development project named **TADp**. Resolve the enclosing
repository as `R` and this installation as `P=R/TADp/`, from either operating
context. Read [the profile](project-profile.md),
[setup authority](decisions/SETUP-001.md), and
[development workflow](docs/development/tadp-development-workflow.md).
The [current repository owner](decisions/OWNERSHIP-001.md) holds the human
ownership and approval roles, including the respective owner of a fork, unless
explicitly delegated. No personal identity is inferred from Git. The human
prospectively adopted source `6120bd10bb2e368274fd5bd4ff5481d33f61c4c6` in
[ADOPTION-001](decisions/ADOPTION-001.md); installation and checks alone would
not establish that decision. Preserve its captured coherence baseline on rerun.

Candidate protocol sources belong in `C=P/protocol/`, an initially empty product
workspace with a boundary README, not another installed project. Project
governance, decisions, initiative records, verification and completion history
belong in their canonical locations at `P`. Installed tools and the governing
suite remain distinguishable from candidate replacements. Generic changes need
an explicitly invoked repository-level maintenance instruction naming the work
and `C`, with the applicable initiative gates and exact source-change authority.
The unchanged [project-local prompt boundary](prompts/AGENTS.md) still forbids
generic framework maintenance; cwd cannot elevate a stored project-local prompt.

Never develop directly in `U=R/protocol/`. The protected installed library is
`D=P/template/`; the upstream protected library is `S=U/template/`. Enforce the
serial delivery contract in the guide: develop in `C`; qualify exact content
with tests, an isolated clean installation trial and independent review;
introduce only specifically authorized proven reusable work into `D`; record
actual development completion; promote the reviewed sanitized manifest into
`S` under exact authority; then roll out from its pinned revision to expressly
mapped consumers in `U`. Completion proves neither promotion nor rollout.
Recheck source/destination drift, consumers, compatibility, migration, links,
protection and recovery at each boundary. Refresh only specifically authorized
affected locks after coherent content verification. Future operations were not
performed or authorized by setup.

Keep the inclusion manifest, authority, exact content identities, commands,
results, exclusions, dependencies, review and recovery evidence with the owning
work outside the clean payload. Sanitize exports, preserve original history and
required provenance, and never export populated project records or experiments
as reusable sources. Reruns verify and reuse this installation and stable
records without replacing customization, altering adoption history or making
empty commits. The canonical requirements below remain binding.

When interpreting any TADp task, read and apply the project root's
[prompt keyword specification](evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md).
This includes ordinary requests, analysis, project-local prompts, numbered
workflow prompts, and repository maintenance. Apply operative directives and
list scheduling only as defined there; reading the registry or its examples
does not activate them. Record bounded exceptions before relying on them;
all unexcepted rules and TADp locks remain binding.

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
  gates. Never refine a closed claim before recorded reopening under adopted bounded
  intake delegation or separate human authority, receipt and legal transition.
  Preserve prior claims; coherent same-outcome revisions may retain identity,
  while independent outcomes and incompatible boundaries split.
- Require one narrow outcome and acceptance claim. Split independent outcomes;
  use a subinitiative only inside a real parent specification.
- Require human decisions for assumptions, questions, acceptance and exceptions
  unless exact governing authority provides another bounded method. The adopted
  specification 09 human intake request delegates placement, coherent revision
  and necessary initiative/scope reopening; record actual LLM authorship and
  each event before applying it. Changed claims still require human acceptance.
- Treat initiative acceptance as a separate explicit human-authority stage.
  Alignment and resolved assumptions or questions do not imply acceptance.
- Record only legal lifecycle transitions. Preserve prior claims and document
  every reopening or revision.
- Require Git, captured immutable creation bases and recorded dedicated/shared
  execution assignment for each revision cycle.
  Preserve unrelated work and keep commits traceable. Never rewrite shared
  history or merge without explicit authority.
- Require standard execution and completion evidence before making the
  corresponding lifecycle claim. Use the delivery record for design or
  planning and follow exactly one delivery path for the declared type.

For documentary prerequisites, apply specification 02's canonical template-use
rules and specification 08's preceding owning-stage preparation procedure.
Use the project root's `template/TEMPLATE-COVERAGE.md` to locate sources,
destinations, and owners. Recover only necessary evidence-backed paperwork
before the invoked entry check; missing authority, identity, actual work, and
verification remain blockers. Preserve accepted/closed claims and reuse records
idempotently. Stage 9 must disclose preceding preparation changes and keep its
assessment itself read-only.

The TADp project root is the scaffold installation directory under
[specification 05](evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md#requirement).
It may equal or lie beneath the Git worktree root; enclosing Git identity does
not enlarge file authority. Resolve the invoked target without ancestor or
sibling redirection, retain parent instructions and coordinate shared Git state.

Preserve source identity, distinguish observed evidence from accepted
authority, and report only outcomes supported by verification.
