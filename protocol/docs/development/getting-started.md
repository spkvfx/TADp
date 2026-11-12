# Getting started with TADp

## Audience

This guide is for developers, architects, maintainers, and project owners who
are adopting TADp in a repository or changing the TADp reference implementation.

## Required software and access

TADp has two explicit platform requirements:

1. **Git** must be available, and the TADp project must be the root of its own
   Git repository or Git worktree. Git provides the branch and history evidence
   used by the initiative workflow.
2. **Codex** must be able to open and modify the repository, read `../../AGENTS.md`,
   inspect Git state, pause for human decisions, edit files, and run validation.

Python 3 is required to run the bundled validator and regression tests. The
validator itself uses only the Python standard library. A remote Git host and
pull-request service are needed only when the chosen finalization workflow will
push a branch and open a pull request.

Other agents and tools are outside the guaranteed execution environment. Read
[Adapting TADp to other tools](adapting-other-tools.md) before substituting one.

## Choose an adoption path

Every TADp task applies the canonical
[prompt keyword contract](../../evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md),
even when no stored prompt is invoked. Existing installations use the
[keyword migration guide](../guides/prompt-keywords-migration.md) before
claiming adoption; installing the capability grants no live exception.

### Use this repository as the TADp reference implementation

Use this path when maintaining the protocol itself:

1. Open the repository root in Codex.
2. Read `../../AGENTS.md`.
3. Read the applicable specifications under
   `../../evidence/authoritative/LLM`, starting with the suite index.
4. Inspect the Git branch, staged changes, unstaged changes, and untracked
   paths before editing.
5. Classify the intended change as an authoritative protocol change, a
   reusable template or prompt change, validator work, or explanatory
   documentation.
6. Update every consumer of the changed contract and run validation.

### Adopt TADp in an existing product repository

Use this path when TADp will govern work in another repository:

1. Confirm that the target directory is its own Git repository root.
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
5. Merge the provided `../../AGENTS.md` requirements with existing repository
   instructions. More local instructions may be stricter, but they must not
   weaken the authoritative TADp rules.
6. Copy `../../docs`, `../../tools`, and `../../tests`. This preserves the
   protection utility, validator, migration guidance, and regression coverage.
7. Run `python tools/tadp_protect.py check .`, then activate the tracked hook
   with `git config core.hooksPath .githooks`. The hook is local Git
   configuration and therefore must be enabled in every clone or worktree.
8. Create `project-profile.md` from its template and record owners, boundaries,
   Git conventions, evidence locations, approval authority, and the exact
   adopted correlation-revision commit.
9. Establish the evidence register, canonical initiative and correlation
   index, status view, and version-correlation migration ledger before
   allocating the first governed tuple.
10. Give every pre-effective record a complete `Unmigrated`, `Deferred`, or
    separately authorized migration disposition. Do not infer a partial tuple.
11. Run a narrow pilot initiative before migrating a large body of work.

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

From the protocol root (`protocol/` in the reference repository and normally
the project root in an adopted repository), run:

```powershell
python tools/tadp_protect.py check .
python tools/tadp_validate.py .
python -m unittest discover -s tests -v
```

On systems where the Python launcher is named differently, use the equivalent
interpreter command without changing validator semantics.

The validator should report zero errors before an initiative is prepared. If it
reports missing protocol files, complete the adoption structure rather than
disabling the check. A passing result establishes structural conformance only;
it does not accept evidence or an initiative.

Protected-source findings are not fixed by automatically refreshing a lock.
Unexpected changes under `template/` or `evidence/authoritative/LLM/` must be
reverted or investigated. Refresh is reserved for an explicitly authorized
change to the named reusable source or invariant.

## First initiative

Choose a small outcome with one owner, one authority boundary, and an
independent acceptance claim. Use numbered stages 0 through 7 in
`../../template/prompts` in order, beginning with preparation. After explicit
acceptance, use exactly one delivery path for the declared initiative type:
stages 8 through 10 for implementation, stage 11 for design, or stage 12 for
planning. Use stage 13 only after evidence-backed completion. Do not begin with
a portfolio-wide or multi-outcome effort.

Stage 0 allocates a canonical work version, realization suite,
self-contained initiative, and version-bearing branch from a captured base as
one reciprocal tuple. Later stages verify rather than recreate that identity.

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
- Confirm that every clone or worktree has configured
  `core.hooksPath=.githooks`.
- Ensure contributors can run the validator and product-specific checks.
- Explain that `..` is explanatory while `../../evidence/authoritative` is
  binding.

