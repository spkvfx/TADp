# Add a project-local prompts boundary to the TADp scaffold

Work in `C:\Users\User\PycharmProjects\TADp`.

Implement one bounded protocol change: add a project-local `prompts/`
directory to the generic TADp scaffold and place an `AGENTS.md` and `README.md`
in that directory. The instruction file must confine prompt-driven work to the
current scaffold, and the README must explain that this directory is for work
about the project itself rather than maintenance of TADp. Both files must
preserve every applicable TADp gate, protected-source rule, and integrity lock.

## Explicit human authority and limits

I explicitly authorize the exact protected reusable-source changes required
to:

- create `protocol/template/project/prompts/AGENTS.md` and
  `protocol/template/project/prompts/README.md`;
- create the corresponding working-scaffold files at
  `protocol/prompts/AGENTS.md` and `protocol/prompts/README.md`;
- update the smallest necessary reusable project documentation under
  `protocol/template/**` so the project-local `prompts/` directory is part of
  the copied scaffold;
- update directly affected protocol documentation, adoption guidance,
  validation, and regression tests; and
- refresh `protocol/template/.tadp-lock.json` only after the authorized
  reusable-source changes are coherent and verified.

This authority is limited to the project-local prompt boundary described in
this prompt. It does not authorize:

- a change to `protocol/evidence/authoritative/LLM/**` or its lock;
- a change to an authoritative invariant, initiative lifecycle state, workflow
  stage, correlation identity, acceptance decision, or completion claim;
- a change to the repository-maintenance prompt boundary at
  `prompts/AGENTS.md`;
- moving or duplicating the numbered initiative workflow from
  `protocol/template/prompts/`;
- using the new project-local prompt directory to maintain the generic TADp
  protocol, invariant suite, reusable templates, workflow, validator,
  protection controls, or adoption guidance; or
- unrelated template, prompt, product, initiative, or project changes.

If the requested result cannot be made coherent without one of those excluded
changes, stop that affected work and report the exact conflict and required
human decision. Do not broaden this authority by inference.

## Canonical scaffold definition

Use the following definition in this change and state it clearly in the new
project-local `prompts/AGENTS.md`.

A **TADp scaffold** is one self-contained, project-shaped directory tree that
owns a single TADp working boundary. Its root is a directory `S` containing,
at minimum:

```text
S/AGENTS.md
S/evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md
S/initiatives/
S/products/
S/template/
S/tools/
S/prompts/AGENTS.md
S/prompts/README.md
```

The scaffold includes the project-owned governance records, evidence,
initiatives, products, source, configuration, documentation, tests, tools, and
other files whose resolved paths remain inside `S`. Protected trees inside
`S` are within the scaffold boundary, but being within that boundary does not
grant permission to edit them.

The scaffold does not include:

- the parent or a sibling of `S`;
- another TADp scaffold, repository, worktree, or submodule nested within or
  adjacent to `S`;
- a path that lexically appears under `S` but resolves outside it through a
  symlink, junction, mount, or equivalent indirection;
- an external source distribution from which the scaffold was copied;
- an external service or remote system; or
- a referenced or attached project merely because a prompt mentions it.

The **current TADp scaffold** is the unique scaffold whose direct child
`prompts/` directory contains the `AGENTS.md` governing the invoked prompt.
Determine `S` from that file's resolved location before doing any work. Do not
derive `S` from the shell's current directory, an attachment, a target named in
prompt prose, or the enclosing Git top level.

A complete governed TADp project must still satisfy the authoritative Git-root
requirement. A scaffold embedded in a larger repository for distribution,
testing, or another non-governed purpose does not gain project compliance,
lifecycle standing, or authority merely because its directory shape matches
this definition. When Git metadata is rooted above `S`, that fact never
expands prompt scope to a parent or sibling path.

If the markers are missing, more than one candidate `S` exists, a path escapes
the boundary after resolution, or the relationship between `S` and the active
Git worktree is ambiguous, stop before any write or external side effect and
report the ambiguity.

## Distinguish the two prompt locations

Keep these roles separate:

- `template/prompts/` is the protected reusable library for the numbered TADp
  initiative workflow and its shared workflow contract.
- root `prompts/` in an instantiated scaffold is the project-local workspace
  for prompts whose subject and work are confined to that project and
  scaffold.

Do not copy the numbered workflow into the project-local directory and do not
treat project-local prompts as authoritative evidence, accepted initiatives,
or proof that a gate passed.

The reusable sources at `protocol/template/project/prompts/AGENTS.md` and
`protocol/template/project/prompts/README.md` must be suitable for copying to
the corresponding files under `<scaffold-root>/prompts/`. When those files are
read from `template/project/prompts/`, they remain protected reusable sources
and must not redefine that template location as the active project scaffold or
authorize prompt execution there.

## Project-local purpose and README

The new `prompts/README.md` must define the directory as a home for explicit
instructions about the current project. It must include clearly labelled,
reference-only categories such as:

- creating a project realization note through the applicable preparation and
  correlation workflow;
- giving a direct instruction for one named project initiative at a permitted
  workflow stage; and
- requesting a direct change to a project product when an accepted
  implementation initiative and its entry gates authorize that product work.

These are examples of subject matter, not authority to skip the workflow. The
README must say that a project-local prompt remains non-authoritative, inherits
`prompts/AGENTS.md`, and may act only when the applicable evidence, human
decisions, initiative state, branch, stage, and verification gates permit the
requested work.

The README must also identify what does not belong in the directory. In
particular, project-local prompts must not be used to change the generic TADp
protocol, the Codex invariant suite, reusable templates, numbered workflow
prompts or contracts, validator or protection semantics, or generic adoption
and migration guidance. Route a discovered need for that work to a separately
scoped protocol-maintenance instruction outside the project-local directory.

Do not include executable prompt blocks in the README. Keep its examples
clearly illustrative so reading the README cannot recursively trigger work.

## Required `prompts/AGENTS.md` behavior

Make the new instruction file concise enough to load for every project-local
prompt, but require all of the following behavior.

### Recursive scope boundary

- Apply the instruction to every prompt and descendant directory under the
  scaffold's root `prompts/` directory.
- Resolve and verify the current scaffold root before reads that could drive a
  decision, before writes, before Git mutation, and before any external side
  effect.
- Limit file creation, editing, renaming, moving, deletion, generated output,
  Git pathspecs, commits, and other side effects to the current scaffold and
  the exact narrower boundary declared by the invoked prompt.
- Treat the scaffold boundary as a maximum, not as blanket authority. A prompt,
  initiative, stage, protected-source instruction, or user decision may impose
  a smaller boundary.
- Permit outside material to be read only when the invoked prompt explicitly
  identifies it as evidence and repository policy permits the read. Preserve
  its source identity and standing. Reading it never authorizes a write to its
  location or makes it authoritative.
- Stop and request separately scoped human authority when completion would
  require changing another scaffold or producing a side effect outside the
  current scaffold.

### Project subject boundary

- Permit prompts about the current project's realizations, evidence,
  initiatives, products, and other project-owned work, subject to the exact
  authority and workflow gates for that work.
- Do not treat the presence of TADp framework files inside the scaffold as
  permission to maintain TADp itself from this directory.
- Do not change generic TADp invariants, reusable sources, workflow contracts,
  numbered prompts, validation or protection behavior, or adoption and
  migration guidance in response to a project-local prompt.
- When project work exposes a possible protocol defect or improvement, record
  or report it without implementing the protocol change. Require a separately
  invoked, protocol-scoped instruction in the appropriate maintenance prompt
  location.
- Allow a project prompt to run the existing TADp validator, protection checks,
  and workflow tooling as verification. Running those tools does not authorize
  changing their generic behavior.

### Gates, evidence, and prompt authority

- Read the current scaffold's root `AGENTS.md` and all applicable authoritative
  material beginning with the local invariant-suite index before making a
  normative decision.
- Apply the more restrictive instruction when the root, a directory-scoped
  instruction, an authoritative invariant, an accepted initiative, or the
  invoked prompt narrows the work.
- Treat a stored prompt as non-authoritative work description. Its existence,
  wording, or execution does not prove an assumption, answer a question,
  accept an initiative, authorize an invariant exception, satisfy an entry or
  exit gate, change lifecycle state, or establish completion or release.
- Require explicit human authority and a decision receipt wherever the
  protocol requires them. Do not infer a decision from prompt invocation,
  urgency, silence, a recommendation, or later work.
- Preserve the declared initiative type, narrow scope, correlation tuple,
  active branch, captured base, stage ownership, lifecycle evidence, and
  type-specific delivery path whenever the invoked prompt participates in an
  initiative workflow.
- Stop only the affected work when a gate fails, retain the evidence of that
  failure, and continue independent in-scope work only when the protocol
  permits it.
- Record invariant conflicts through the required conflict process rather than
  changing lower- or higher-standing material to hide the contradiction.

### Protected sources and locks

- Treat `template/**` and `evidence/authoritative/LLM/**` within the current
  scaffold as protected sources.
- Do not edit, fill, rename, move, delete, or add a file in a protected tree
  from a project-local prompt. An exact reusable-source or invariant change
  belongs in a separately scoped protocol-maintenance instruction and remains
  subject to its own explicit human authority.
- Treat `.tadp-lock.json` as integrity evidence, not edit authority. Check the
  applicable locks before work that relies on protected sources. Preserve and
  report pre-existing drift; do not absorb it into project work.
- Never refresh a lock, weaken validation, or use a protected-update commit
  override from a project-local prompt. Do not accept unexplained drift or
  weaken a check to make project work pass.
- Route an exact reusable-source or invariant revision to separately scoped
  protocol maintenance, where its named authority, affected consumers,
  compatibility or migration handling, verification, and governed lock
  refresh can be handled together.

### Git and unrelated work

- Inspect the applicable worktree, branch, staged paths, unstaged paths, and
  untracked paths before mutation. Preserve unrelated work and never absorb it
  into the invoked prompt's change.
- Do not interpret an enclosing repository as permission to touch another
  scaffold. Scope every diff, pathspec, staging operation, and report to `S`
  and to the prompt's narrower declared boundary.
- Follow the authoritative branch and history rules. Do not rewrite shared
  history, force-push, merge, delete a branch, deploy, or publish unless exact
  human authority and the applicable workflow stage both permit that action.
- Report only claims supported by the files, Git evidence, decisions, and
  verification that actually exist.

## Scaffold integration

Update the smallest coherent set of consumers so the new directory is a real
part of the generic scaffold rather than an unreferenced file.

At minimum:

1. Add `protocol/prompts/AGENTS.md` and `protocol/prompts/README.md` as the
   working project-local prompt directory.
2. Add `protocol/template/project/prompts/AGENTS.md` and
   `protocol/template/project/prompts/README.md` as their protected reusable
   sources. Keep each working file aligned with its corresponding generic
   source.
3. Update the project scaffold map and adoption instructions to copy and retain
   root `prompts/AGENTS.md` and `prompts/README.md` from
   `template/project/prompts/`.
4. State that project-local prompt files may be added beneath `prompts/` but
   remain non-authoritative and inherit the scoped instructions.
5. Preserve `protocol/template/prompts/` as the separate protected numbered
   workflow library.
6. Add migration guidance for an existing scaffold: copy the canonical files
   into root `prompts/AGENTS.md` and `prompts/README.md`, reconcile any
   pre-existing prompt-directory instructions without weakening either set,
   and validate before claiming adoption.

Do not make the contents of a project's root `prompts/` directory a protected
file set merely because the reusable sources are locked. The reusable files
under `template/project/` are protected by the template lock; instantiated
project-local prompts remain working project material governed by their local
instructions and normal Git history.

## Validation and regression coverage

Extend validation and tests only as needed to enforce the new structural and
scope contract. Cover at least:

- a complete scaffold containing root `prompts/AGENTS.md` and
  `prompts/README.md` passes;
- a scaffold missing the directory or either required file receives a precise
  finding;
- both reusable files under `template/project/prompts/` are recorded by the
  template integrity lock;
- each working file and its reusable generic source do not drift in the
  maintained protocol scaffold;
- additional project-local prompt files are allowed and are not mistaken for
  authoritative evidence or protected reusable workflow files; and
- the validator does not interpret the enclosing Git root as permission to
  cross a scaffold boundary.

Use self-contained protocol-owned fixtures. Do not create or rewrite project
evidence merely to make a validation case pass.

Before editing, run the read-only protected-source check and inventory existing
Git changes. If a protected lock already reports drift outside this prompt's
authorized paths, preserve it and stop the affected lock refresh rather than
normalizing it into this change.

After the content is coherent:

1. run the repository-defined template lock refresh only for the exact
   authorized template changes, using this prompt as the authority reference;
2. run the protected-source checks;
3. run the TADp validator;
4. run the relevant regression suite with the configured project Python
   environment; and
5. run a whitespace and path review of the final diff.

A passing structural validator does not prove prompt authority, initiative
acceptance, lifecycle completion, or cross-scaffold permission.

## Completion report

Report:

- the exact operational definition of a scaffold and how the current scaffold
  is resolved;
- the project-local prompt scope and every explicit exclusion;
- the working and reusable `prompts/AGENTS.md` and `prompts/README.md` paths
  created;
- documentation, validator, tests, migration guidance, and protected lock
  updated;
- the initial and final protected-source check results;
- every changed path and the verification run; and
- any unresolved ambiguity, pre-existing drift, failed gate, or human decision
  still required.
