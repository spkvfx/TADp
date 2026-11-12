# Project-local prompt boundary

These instructions apply recursively to every prompt and descendant directory
under this file's active project-local `prompts/` directory. They govern a
reusable copy only after it is installed as the direct
`<scaffold-root>/prompts/AGENTS.md` child of one valid TADp scaffold. The copy
under `template/project/prompts/` is protected reusable source, is not an
active prompt workspace, and does not authorize prompt execution there.

## Resolve the current scaffold first

A **TADp scaffold** is one self-contained, project-shaped directory tree that
owns one TADp working boundary. Its root `S` contains, at minimum:

- `S/AGENTS.md`;
- `S/evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md`;
- `S/initiatives/`;
- `S/products/`;
- `S/template/`;
- `S/tools/`; and
- `S/prompts/AGENTS.md` and `S/prompts/README.md`.

The scaffold includes project-owned governance records, evidence, initiatives,
products, source, configuration, documentation, tests, tools, and other files
whose resolved paths remain inside `S`. Protected trees inside `S` remain
protected; containment never grants edit authority.

The scaffold excludes:

- the parent or a sibling of `S`;
- another scaffold, repository, worktree, or submodule nested within or
  adjacent to `S`;
- a path that appears beneath `S` but resolves outside it through a symlink,
  junction, mount, or equivalent indirection;
- the external distribution from which the scaffold was copied;
- an external service or remote system; and
- a referenced or attached project merely because a prompt mentions it.

The **current TADp scaffold** is the unique scaffold whose direct child
`prompts/` directory contains the resolved `AGENTS.md` governing the invoked
prompt. Resolve this file first, then derive `S` from its parent
`prompts/` directory. Never derive `S` from the shell's current directory,
an attachment, a target named in prompt prose, or the enclosing Git top level.

Before any read that could drive a decision, write, Git mutation, generated
output, or external side effect, verify the resolved markers above, the unique
candidate `S`, every affected resolved path, and the relationship between
`S` and the active Git worktree. Stop before the affected action when a marker
is missing, candidates are ambiguous, a path escapes, or the Git relationship
is ambiguous.

A complete governed TADp project must still satisfy the authoritative Git-root
requirement. A scaffold embedded in a larger repository for distribution,
testing, or another non-governed purpose gains no project compliance,
lifecycle standing, or authority from its shape. Git metadata above `S` never
expands prompt scope.

## Scope and project subject

- Limit file creation, editing, renaming, moving, deletion, generated output,
  Git pathspecs, staging, commits, and all other side effects to `S` and to
  the exact narrower boundary declared by the invoked prompt.
- Treat `S` as a maximum boundary, not blanket authority. The prompt,
  initiative, workflow stage, protected-source rule, or human decision may
  impose a smaller boundary.
- Read outside material only when the invoked prompt explicitly identifies it
  as evidence and repository policy permits the read. Preserve source identity
  and standing. A read never authorizes a write or promotes the material.
- Stop and request separately scoped human authority when completion requires a
  change to another scaffold or any side effect outside `S`.
- Permit work about the current project's realizations, evidence, initiatives,
  products, and other project-owned material only through its applicable
  authority and workflow gates.
- Do not treat TADp framework files inside `S` as permission to maintain TADp
  itself. A project-local prompt must not change generic TADp invariants,
  reusable sources, workflow contracts, numbered prompts, validation or
  protection behavior, or generic adoption and migration guidance.
- Report or record a possible protocol defect without implementing it. Require
  a separately invoked, protocol-scoped maintenance instruction in the
  appropriate external maintenance prompt location.
- Existing TADp validators, protection checks, and workflow tools may be run
  for verification. Running them does not authorize changing their generic
  behavior.

## Gates, evidence, and prompt authority

- Read and apply the current scaffold's canonical
  [prompt keyword specification](../evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md)
  when interpreting any task, including ordinary requests and local prompts.
  Its registry, positional blocks, list scheduling, and bounded exception
  process govern operative instructions. Reading examples does not activate
  them. A requested setting alone cannot except a rule; record sufficient
  exact authority before reliance, retain every unexcepted gate, and distinguish
  excepted work from ordinary acceptance or completion. This contract does not
  expand the scaffold boundary or permit protected-source maintenance here.
- Read `S/AGENTS.md` and all applicable authoritative material, beginning
  with the local invariant-suite index, before making a normative decision.
- Apply the more restrictive instruction when the root instructions, a local
  directory instruction, an authoritative invariant, an accepted initiative,
  or the invoked prompt narrows the work.
- Treat every stored prompt as a non-authoritative work description. Its
  existence, wording, or invocation does not prove an assumption, answer a
  question, accept an initiative, authorize an exception, satisfy a gate,
  change lifecycle state, or establish completion or release.
- An actual human request to process an identified realization under adopted
  specification 09 delegates bounded fit-based placement, coherent revision and
  necessary target/scope reopening. Capture each choice, prior claim, exact
  source/target and actual LLM author before action. Invocation alone proves
  no acceptance or changed completion and supplies no unrelated waiver.
- Require explicit human authority and a decision receipt wherever the
  protocol requires them. Never infer a decision from invocation, urgency,
  silence, a recommendation, or later work.
- Preserve the declared initiative type, narrow scope, scope membership and revision assignment,
  captured base, active branch, stage ownership, lifecycle evidence, and
  type-specific delivery path whenever a prompt participates in an initiative
  workflow.
- When an unexcepted gate fails, retain the failure and stop only the affected work.
  Continue independent in-scope work only when the protocol permits it.
- Record invariant conflicts through the required conflict process. Do not
  alter higher- or lower-standing material to conceal a contradiction.

## Protected sources and locks

- Treat `S/template/**` and `S/evidence/authoritative/LLM/**` as protected
  sources.
- From a project-local prompt, never edit, fill, add, rename, move, or delete a
  protected-source file. An exact reusable-source or invariant change requires
  a separately scoped protocol-maintenance instruction and its own explicit
  human authority.
- Treat every `.tadp-lock.json` as integrity evidence, not edit authority.
  Check applicable locks before relying on protected sources, preserve and
  report pre-existing drift, and never absorb it into project work.
- Never refresh a lock, weaken validation, or use a protected-update commit
  override from a project-local prompt.
- Route protected-source revisions to protocol maintenance so named authority,
  affected consumers, compatibility or migration handling, verification, and
  governed lock refresh remain one coherent change.

## Git, unrelated work, and reporting

- Inspect the applicable worktree, branch, staged paths, unstaged paths, and
  untracked paths before mutation. Preserve unrelated work and never absorb it
  into the invoked prompt's change.
- Scope every diff, pathspec, staging operation, commit, and report to `S`
  and the prompt's narrower boundary. An enclosing repository grants no access
  to another scaffold.
- Follow the authoritative branch and history rules. Do not rewrite shared
  history, force-push, merge, delete a branch, deploy, or publish unless exact
  human authority and the applicable workflow stage both permit it.
- Report only claims supported by the files, Git evidence, decisions, and
  verification that actually exist.
