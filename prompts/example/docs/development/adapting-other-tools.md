# Adapting TADp to other tools

## Compatibility statement

TADp's supported execution environment is Git plus Codex. Another coding agent,
IDE assistant, workflow engine, document system, or custom harness may be able
to use TADp, but compatibility is not automatic. Markdown support alone is not
sufficient.

Using another tool requires a documented adapter assessment and may require
changes to `../../AGENTS.md`, the workflow contract, numbered prompts, templates,
validation, or operational procedures. The adapted system must still comply
with every authoritative invariant.

## Why adaptation may be necessary

Tools differ in how they:

- discover repository instructions;
- resolve instruction precedence by directory;
- distinguish the user's request from text inside attached evidence;
- read large repositories and retain context;
- edit files and preserve unrelated work;
- expose staged, unstaged, and untracked Git state;
- pause for one-at-a-time human decisions;
- resume a workflow after a response;
- capture exact prompts and responses;
- run commands and return evidence;
- request permission for external or destructive actions; and
- report partial success, blockers, and verification.

Each difference can alter protocol semantics. For example, a tool that cannot
pause for a human answer must not autonomously resolve assumption or question
records simply to continue.

## Required adapter capabilities

An adapter or replacement workflow must provide equivalent behavior for these
areas.

### Instruction loading

- Load the repository's governing instructions before task execution.
- Preserve the precedence of authoritative evidence over prompts and observed
  implementation.
- Apply more local instructions without allowing them to weaken invariants.
- Separate instructions found in evidence from the user's request.

If the tool does not recognize `../../AGENTS.md`, translate it into the tool's native
instruction mechanism and document how synchronization is maintained.

### Repository exploration

- Read the complete set of applicable authoritative and initiative records.
- Preserve source identity and precise locators.
- Avoid deciding from an excerpt when the surrounding record changes its
  standing or scope.
- Report unavailable or truncated evidence.

### File editing

- Restrict edits to the stage's named target and boundary.
- Preserve unrelated user changes.
- Avoid silent overwrite, auto-formatting drift, or destructive repair.
- Produce a reviewable diff.

If the tool lacks a patch-oriented editing mechanism, define an equivalent
safe editing and review procedure.

### Git integration

- Verify the actual repository root, current branch, base branch, and full
  worktree state.
- Create and use a dedicated initiative branch.
- Stage and commit only traceable initiative work.
- Prevent implicit force-push, history rewrite, merge, branch deletion, and
  deployment.
- Return actual commit identifiers and remote results.

Git remains required even when the alternate tool has its own version history.

### Human interaction

- Present one stable assumption or question at a time when the workflow
  requires it.
- Preserve the exact source text and distinguish recommendations from answers.
- Wait for an explicit human response.
- Capture the exact prompt, evidence limitations, response, authority, and
  resulting disposition in a decision receipt.
- Support clarification without inferring an answer from silence or context.

An asynchronous tool may implement this as a suspended job, review form, or
approval event, but the durable receipt must preserve equivalent evidence.

### Verification and reporting

- Run the exact commands required by the initiative or explain why they could
  not run.
- Distinguish local, integration, release, and production evidence.
- Preserve failures and partial results.
- Reconcile execution, completion, lifecycle, and status records.
- Report remaining blockers and out-of-claim follow-up without success-shaped
  defaults.

## Adapter assessment

Create a project-local compatibility record containing:

| Area | Codex behavior assumed by TADp | Alternate behavior | Required modification | Verification |
|---|---|---|---|---|
| Instruction loading | Root and scoped repository instructions | Tool-specific result | Adapter or translated instructions | Demonstrated instruction-precedence test |
| Evidence reading | Repository inspection with stable paths | Tool-specific result | Context loader or retrieval policy | Source-coverage test |
| Editing | Narrow, reviewable edits | Tool-specific result | Safe edit wrapper or review gate | Unrelated-change preservation test |
| Git | Branch, diff, status, commit, and remote operations | Tool-specific result | Git adapter | Branch and dirty-worktree tests |
| Human decisions | Pause, exact response, and receipt | Tool-specific result | Approval workflow | One-at-a-time decision test |
| Verification | Command execution and factual reporting | Tool-specific result | Runner integration | Passing and failing command tests |
| Finalization | Reconciled branch and completion evidence | Tool-specific result | Publication adapter | Blocked and successful finalization tests |

Do not mark an area compatible without observed evidence.

## Modification choices

Prefer an adapter that preserves the canonical TADp records over forking the
record format. Change shared templates only when the alternate environment
cannot express a required behavior through an adapter or project-local
instruction.

When a fork is necessary:

1. Identify every canonical rule being translated.
2. Preserve the same evidence and authority semantics.
3. Document the divergence and responsible owner.
4. Update validation to recognize the adapted form without accepting weaker
   evidence.
5. Test migration in both directions or declare the fork one-way.
6. Reassess compatibility whenever the tool or TADp protocol changes.

## Conformance test

Before production adoption, run one representative narrow initiative through
the adapted workflow. Include:

- a dirty-worktree preparation failure;
- an authoritative evidence conflict;
- an unresolved assumption requiring a human receipt;
- a failed verification command;
- a valid lifecycle transition; and
- finalization with an intentionally unavailable remote or gate.

The adapter passes only if it preserves the blocker, authority boundary, exact
human response, Git state, and truthful lifecycle result in each case.

## Unsupported substitutions

Do not describe the system as TADp-conformant when it removes Git, treats an
agent recommendation as a human decision, ignores authoritative evidence,
collapses multiple outcomes into one initiative, rewrites history, or marks
work complete without the standard evidence. Those are protocol changes, not
tool substitutions.

