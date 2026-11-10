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
2. Copy the contents of `../../template/project` into the target root without
   overwriting established project files blindly.
3. Copy `../../template/initiatives` and `../../template/prompts` into a stable target
   template root, or configure the project profile to use a pinned external
   TADp distribution. Do not depend on an unversioned moving template.
4. Copy the authoritative `../../evidence/authoritative/LLM` suite to the same path
   in the target.
5. Merge the provided `../../AGENTS.md` requirements with existing repository
   instructions. More local instructions may be stricter, but they must not
   weaken the authoritative TADp rules.
6. Create `project-profile.md` from its template and record owners, boundaries,
   Git conventions, evidence locations, and approval authority.
7. Establish the evidence register, initiative index, and status view before
   accepting the first initiative.
8. Copy `..`, `../../tools`, and `../../tests` when the complete reference validator
   and developer guidance will be maintained in the target.
9. Run a narrow pilot initiative before migrating a large body of work.

### Start a new repository

Create the project directory, initialize Git, and make an initial baseline
commit before beginning initiative work. Then follow the existing-repository
adoption path. Do not begin from an untracked directory and later attempt to
reconstruct the base branch or original evidence state.

## First validation

From the repository root, run:

```powershell
python tools/tadp_validate.py .
python -m unittest discover -s tests -v
```

On systems where the Python launcher is named differently, use the equivalent
interpreter command without changing validator semantics.

The validator should report zero errors before an initiative is prepared. If it
reports missing protocol files, complete the adoption structure rather than
disabling the check. A passing result establishes structural conformance only;
it does not accept evidence or an initiative.

## First initiative

Choose a small outcome with one owner, one authority boundary, and an
independent acceptance claim. Use the numbered prompts in `../../template/prompts`
in order, beginning with preparation. Do not begin with a portfolio-wide or
multi-outcome effort.

During the pilot, record friction rather than bypassing it. A repeated friction
point may justify a later TADp change, but a local convenience must not silently
weaken the invariant baseline.

## Before inviting contributors

- Ensure Git identity, branch protections, review ownership, and the intended
  integration branch are documented.
- Confirm who may accept initiatives and resolve human decision gates.
- Confirm which paths are authoritative and who may revise them.
- Ensure contributors can run the validator and product-specific checks.
- Explain that `..` is explanatory while `../../evidence/authoritative` is
  binding.

