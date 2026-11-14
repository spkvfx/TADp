# INTEGRATION-001 decision receipt

**Receipt ID:** INTEGRATION-001

**Initiative:** Project-wide Git configuration; no initiative accepted

**Source ID or lifecycle event:** Appointment of the TADp project integration base

**Human authority:** Requesting human acting as current repository owner under OWNERSHIP-001

**Response date or event:** 2026-11-14, reply to the pending preflight question

**Capture date or event:** 2026-11-14, resumed execution before scope allocation

**Recorded by:** Codex, primary agent

**Capture context:** Continuation of the invoked assumption/question review protocol-change prompt

**Disposition:** Project integration branch appointed: `v1`

**Git commit:** Recorded by the scoped intake commit containing this receipt

**Scope:** Project-wide; no version scope allocated by this human answer

**Revision cycle:** Not applicable to project configuration

**Claim revision:** Git preflight `9c9fd1daad655fd58349c005f8d31a4f52790cc9`

## Exact prompt or question

```text
The TADp project has no appointed integration branch, which specification 05 requires before allocating its first scope. Which branch should be the project integration base? The current branch is `docs/assumption-question-review-prompt`; `v1` also exists. Naming the base does not authorize a merge.
```

## Evidence and limitations presented

- **Authoritative evidence:** Installed specification 05 requires an actual project integration base; specification 09 separately governs placement.
- **Other evidence:** The profile and adoption records left that branch unappointed; observed `v1` existed.
- **Material limitations:** The answer appoints a branch, not a scope, acceptance, merge, push or protected-source introduction.
- **Affected scope described to the human:** The TADp development project's Git integration base.

## Exact human response

```text
TADp v1
```

## Resulting scope and rationale

The response identifies project TADp and branch `v1` in answer to the exact
integration-base question. At resumed inspection the worktree was clean on
`v1` at `9c9fd1daad655fd58349c005f8d31a4f52790cc9`, tracking `origin/v1`.
The earlier preflight is retained on `work/assumption-question-review-preflight`
at `f6df64cbfb718bf4a4406e1e2e5b027878adc0a4`. This receipt does not infer who
switched the worktree or derive human authority from Git identity.

`v1` is an appointed integration-base role, not an allocated project scope.
Do not give it a self-parenting major-scope role. New allocation uses a distinct
free scope selected and recorded under adopted specification 09.

## Reconciled records

| Record | Change required by this decision | Verification |
|---|---|---|
| [Profile](../project-profile.md) | Appoint v1; preserve historical unassigned state in the change record | Exact response, actual ref and scoped diff |
| [Development workflow](../docs/development/tadp-development-workflow.md#current-installation-and-authority) | Reflect current appointment and distinct scope role | Role inspection and links |
| [Resumed intake](../evidence/non-authoritative/assumption-question-review/intake.md) | Record captured tip, fit and proposed separate scope/execution assignment | Specification 05/09 preflight |

## Unresolved consequences and re-entry conditions

The appointed base removes the allocation blocker; it does not accept a new
initiative. Preserve existing branch/ref history, prior documentation effort
and the governing revision. New initiative acceptance, candidate implementation
entry, qualified introduction into the installed library, completion, promotion,
rollout and any integration remain their separate gates. No remote action is
authorized.
