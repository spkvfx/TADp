<!-- Replace every braced placeholder before execution. -->

# 13. Finalize completed initiative and record local integration

Use this prompt after the initiative's type-specific delivery has verified
`Completed`. It verifies existing completion, finalizes traceable commits and
integrates a dedicated initiative branch into its assigned scope when specifically
authorized, or records verified direct placement. It never closes that scope.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) and the
[Git workflow specification](../../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md).

Use the [integration receipt source](../project/initiatives/integration-receipt.template.md)
for each actual integration or explicit exclusion/transfer/no-deliverable event.
Preserve exact current-cycle identity, source/target tips, closure authority,
method and post-integration verification; record failures as failures.
## Example usage

> **Reference only — do not execute this example.**
>
> Using [initiative finalization](13_initiative_finalization.md), finalize the
> attached initiative after verified completion and its recorded immediate-parent
> integration.

Only the **Finalize initiative prompt** block below is executable when invoked.

## Finalize initiative prompt

```text
Apply {initiative_template_root}/prompts/WORKFLOW-CONTRACT.md and the canonical
prompt keyword specification at evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md.
Preserve effective settings, protected locks, all unexcepted gates and truthful
evidence. Finalize {initiative} at {initiative_path} under its adopted revision.

Before changing anything, verify the canonical membership row, exact scope,
source provenance, current revision cycle, dedicated/shared execution mode,
active branch, captured base and immediate integration target. Inspect both
branch tips and the staged, unstaged and untracked worktree. Stop on a mismatch,
missing ref/authority, changed target requiring review, or unrelated work that
cannot be preserved safely. Do not infer repairs, targets or remote authority.

Before integration, instantiate the reusable integration receipt outside
template/ at the initiative/scope evidence location and capture authority.
Complete its objective fields from actual Git results, never planned values.
Integration state uses exact Pending, Blocked, Merged, Fast-forward,
Already integrated, Direct placement, Excluded, Transferred or No deliverable.

Perform these actions serially:
1. Verify README.md is Completed under its recorded accepted claim and current
   revision. Confirm completion-evidence.md supplies every applicable passing
   gate; implementation uses execution-record.md and design/planning uses
   delivery-record.md. Verify complete source diff, output/type boundaries,
   acceptance receipts, proposal, specifications, decisions, mapping, roadmap,
   steps, verification, compatibility and deferred ownership agree. Do not
   manufacture completion or weaken specifications to fit delivered work.
2. Recheck the cross-initiative coherence review against current open effort
   and affected closed claims. Reconcile source-claim blockers through owning
   workflows. Verify initiative-status and parent/dependent records reflect
   the same claim. Preserve conflicts and historical closures. A new cycle's
   delta requires fresh verification; earlier completion/integration receipts
   do not certify it. Return stale or unsupported completion to delivery.
3. Review the full branch diff and current target. On a shared scope branch,
   attribute this initiative's exact paths, commits, revision base, verification
   and unavoidable mixed boundaries; preserve every other member's work and
   latest index additions. Stage only traceable accepted work and aligned
   evidence/tracking. Commit remaining changes coherently or retain existing
   commits when nothing remains; do not make an empty commit.
4. Capture the actual human instruction to close/finalize this identified
   initiative, its bounded local merge authority and exact source/target in
   the closure record before acting. A prior protocol adoption, implementation
   request or terminal status alone does not authorize integration. Do not ask
   again when the exact instruction already supplies sufficient authority.
5. For shared execution directly on its assigned scope branch, record already
   present placement and exact verified initiative commits. Perform no self-
   merge and no upward scope merge. Mere presence is not acceptance of other
   hosted work. For a dedicated initiative branch, verify its accepted source delta,
   current target, open parent state and all applicable checks, then integrate
   initiative branch -> assigned version-scope branch locally. If the parent
   is closed, require its recorded authorized reopening before integration.
   Detect already integrated source commits before retrying. Record a real
   fast-forward, merge or already integrated result without inventing a merge
   commit. Conflicts or failed checks leave integration pending/blocked while
   preserving truthful lifecycle completion and actual failures. Resolve only
   accepted scope; substantive claim changes return through revision gates.
6. Record actual source and target tips, target ref, authority, method, result
   commit, source delta, command results and post-integration verification in
   initiative integration evidence and reciprocal index/scope records. Preserve
   previous cycles and immutable creation bases. Retain source branches.

Cancelled or Superseded work uses a separate explicit closure disposition;
this Completed entry must not integrate abandoned or unaccepted deliverables.
A scope closes only through scope_closure.md after every required member/child
integration and aggregate gate passes. This initiative finalization neither
closes siblings/ancestors nor authorizes further upward merges.

Pushes, publication, deployment, history rewriting and branch removal need
separate specific authority. Human-managed review requests are outside this
operation; no hosting connection or URL is a prerequisite or output. If remote
policy constrains integration, report the constraint without bypassing it.

Report exact tracking paths, acceptance/completion verification, commit IDs,
execution mode, source/target refs and tips, authority, method/result commit,
post-integration checks, closure versus integration status, pending failures
and remaining independently owned follow-up. Report no merge when none occurred.
```