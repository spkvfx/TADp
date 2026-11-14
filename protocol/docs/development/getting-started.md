# Getting started with TADp

## Audience

This guide is for developers, architects, maintainers, and project owners who
are adopting TADp in a repository or changing the TADp reference implementation.

## Required software and access

TADp has two explicit platform requirements:

1. **Git** must be available, and the TADp installation directory must be
   contained in a valid Git worktree. Project root `P` may equal Git root
   `G` or be beneath it. Git supplies branch and history evidence without
   widening the project's file boundary; see
   [specification 05](../../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md#requirement).
2. **Codex** must be able to open and modify the repository, read `../../AGENTS.md`,
   inspect Git state, pause for human decisions, edit files, and run validation.

Python 3 is required to run the bundled validator and regression tests. The
validator itself uses only the Python standard library. Local finalization requires no hosting connection. Humans independently manage
pull requests; pushes require separate authority.

Other agents and tools are outside the guaranteed execution environment. Read
[Adapting TADp to other tools](adapting-other-tools.md) before substituting one.

## Choose an adoption path

This reference repository stores the distributable protocol under `protocol/`
inside the enclosing Git repository. An adopted project installs its scaffold
at a selected directory inside a valid Git worktree, including the Git root.
Paths in links below are relative to this
guide; command paths are relative to the explicitly named working directory.
Inspect the recorded governing revision before applying installed capabilities
to existing work. Installation alone is not adoption or acceptance.

Every TADp task applies the canonical
[prompt keyword contract](../../evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md),
even when no stored prompt is invoked. Existing installations use the
[keyword migration guide](../guides/prompt-keywords-migration.md) before
claiming adoption; installing the capability grants no live exception.

### Use this repository as the TADp reference implementation

Use this path when maintaining the protocol itself:

1. Open the repository root in Codex.
2. Read the enclosing repository's `AGENTS.md`, `protocol/AGENTS.md`, and
   applicable directory instructions.
3. Read the applicable specifications under
   `../../evidence/authoritative/LLM`, starting with the suite index.
4. Inspect the Git branch, staged changes, unstaged changes, and untracked
   paths before editing.
5. Classify the intended change as an authoritative protocol change, a
   reusable template or prompt change, validator work, or explanatory
   documentation.
6. Update every consumer of the changed contract and run validation.

Run checks from `protocol/`. To configure the protocol-owned hook from the
enclosing Git root, inspect existing configuration first, then use
`git config core.hooksPath protocol/.githooks`. The old root hook still targets
both `protocol/` and absent `example/`; it is not the current maintenance check
boundary. Setup changes local Git configuration; reading this guide does not
perform them. Set `TADP_PYTHON` to the configured interpreter for hook execution.

### Adopt TADp in an existing product repository

Use this path when TADp will govern work in another repository:

1. Select the resolved project installation directory inside a valid Git worktree; discover the actual Git root and verified relative prefix. Preserve parent and sibling boundaries.
2. Copy the complete `../../template` tree to `template/` in the target. Keep
   its scoped `AGENTS.md` and `.tadp-lock.json` intact. If the project instead
   uses an external template distribution, pin an immutable revision and
   record it in the project profile.
3. Copy the contents of `../../template/project`, including `.gitattributes`,
   `.githooks/`, `prompts/AGENTS.md`, and `prompts/README.md`, into the
   target root without overwriting established project files blindly. The root
   copies are working scaffold files; the copies under `template/` remain
   protected reusable sources. Reconcile pre-existing prompt-directory
   instructions without weakening either set.
4. Copy the authoritative `../../evidence/authoritative/LLM` suite, including
   its scoped `AGENTS.md` and `.tadp-lock.json`, to the same path in the target.
5. Merge the copied `template/project/AGENTS.md` requirements with existing repository
   instructions. More local instructions may be stricter, but they must not
   weaken the authoritative TADp rules.
6. Copy `../../docs`, `../../tools`, and `../../tests`. This preserves the
   protection utility, validator, migration guidance, and regression coverage.
   Preserve historical distribution receipts linked by the suite under
   `decisions/`; these are source-provenance records, not decisions for your
   project's work.
7. From the project root run `python tools/tadp_protect.py check .`.
   Inspect existing hooks at `G` and coordinate them manually before explicit
   activation. `core.hooksPath` is shared and relative to `G`; for example,
   use `.githooks` at a Git-root installation or `projects/widget/.githooks`
   at that nested project. Do not overwrite or enable parent hooks implicitly.
8. Create `project-profile.md` from its template and record owners, boundaries,
   Git conventions, evidence locations, approval authority, and the exact
   adopted scope-revision commit, with predecessor revision retained for legacy work.
9. Establish the evidence register, canonical initiative and correlation
   index, status view, scope registry and version-scope migration ledger before
   allocating the first governed scope member.
10. Give every pre-effective record a complete `Unmigrated`, `Deferred`, or
    separately authorized migration disposition. Do not infer a partial tuple.
11. Run a narrow pilot initiative before migrating a large body of work.

Adopt the installation-root revision through the
[prospective adoption guide](../guides/project-root-installation-migration.md).
Existing root installations retain their paths and earlier governing revisions
until recorded adoption. Synchronization supports an existing `--target`
directory or defaults to exact cwd; see the [tool commands](../../tools/README.md).

An existing adoption without locks must use the
[protected-source integrity migration](../guides/protected-source-integrity-migration.md).
Do not initialize a lock until a human has identified the exact template and
invariant baseline being accepted.
An existing scaffold without the root project-local prompt boundary must use
the [project-local prompts migration guide](../guides/project-local-prompts-migration.md).
The migration copies only the canonical project-local files from
`template/project/prompts/`; it does not copy the numbered workflow from
`template/prompts/`.
Use the
[version-realization-initiative correlation migration guide](../guides/version-realization-correlation-migration.md)
for effective-point and legacy-ledger adoption.

### Start a new repository

Create the project directory, initialize Git, and make an initial baseline
commit before beginning initiative work. Then follow the existing-repository
adoption path. Do not begin from an untracked directory and later attempt to
reconstruct the base branch or original evidence state.

## First validation

The following commands are reference procedures, not instructions activated by
reading this guide. Select the project's configured Python interpreter (the
`python` spelling below is illustrative) before running them.

From the protocol root (`protocol/` in the reference repository and normally
the project root in an adopted repository), run:

```powershell
python tools/tadp_protect.py check .
python tools/tadp_validate.py .
python -m unittest discover -s tests -v
```

Use the configured interpreter's actual executable when the shell default
differs. Protection should report zero errors; the validator exits 0 with no
errors, 1 with errors, and 2 for an invalid root. Warnings remain visible and
do not alone cause exit 1. Tests report their actual passing/failing results.

The validator should report zero errors before an initiative is prepared. If it
reports missing protocol files, complete the adoption structure rather than
disabling the check. A passing result establishes structural conformance only;
it does not accept evidence or an initiative.

Protected-source findings are not fixed by automatically refreshing a lock.
Unexpected changes under `template/` or `evidence/authoritative/LLM/` must be
reverted or investigated. Refresh is reserved for an explicitly authorized
change to the named reusable source or invariant.

## First initiative

Use the [canonical coverage map](../../template/TEMPLATE-COVERAGE.md) for source
selection and [prerequisite recovery guide](../guides/template-prerequisites-migration.md)
for evidence-backed preparation before a stage's entry check. Existing adopters
record the revision explicitly; installing sources does not migrate live work.

Choose a small outcome with one owner, one authority boundary, and an
independent acceptance claim. Use numbered stages 0 through 7 in
`../../template/prompts` in order, beginning with preparation. After explicit
acceptance, use exactly one delivery path for the declared initiative type:
stages 8 through 10 for implementation, stage 11 for design, or stage 12 for
planning. Use stage 13 only after evidence-backed completion. Do not begin with
a portfolio-wide or multi-outcome effort.

Stage 0 assesses realization fit before allocation, recording append, revision,
reopening or new initiative placement with a shared/dedicated branch assignment.
Adopt the [scope revision](../guides/version-scope-migration.md) explicitly and
preserve every legacy disposition. Later stages verify recorded identity.

During the pilot, record friction rather than bypassing it. A repeated friction
point may justify a later TADp change, but a local convenience must not silently
weaken the invariant baseline.

## Before inviting contributors

- Ensure Git identity, branch protections, review ownership, and the intended
  integration branch are documented.
- Confirm who may accept initiatives and resolve human decision gates.
- Confirm which paths are authoritative and who may revise them.
- Require review ownership or branch rules for `template/**`,
  `evidence/authoritative/LLM/**`, and their `.tadp-lock.json` files on the
  chosen Git host.
- Confirm every clone or worktree has coordinated its shared hook dispatcher
  using the selected project's correct Git-relative hook path.
- Ensure contributors can run the validator and product-specific checks.
- Explain that `..` is explanatory while `../../evidence/authoritative` is
  binding.


For scope-revision adoption, establish the scope registry, membership index and
complete version-scope migration ledger before allocation. Record the coherent
revision's real immutable delivery commit in the profile. Legacy work remains
under its recorded compatible revision until explicitly migrated; predecessor
adoption steps above do not allocate a new scope or rename historical versions.
See [scope migration](../guides/version-scope-migration.md).

## Separate example

The example is maintained in the separate
[TADp-example repository](https://github.com/spkvfx/TADp-example), with clone URL
`https://github.com/spkvfx/TADp-example.git`. Its current rebuild, adoption and
application behavior are unverified here. Cloning it is optional and does not
replace the adoption steps or make it a protocol synchronization target.
