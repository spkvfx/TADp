<!-- Replace every braced placeholder before execution. -->

# Close a version scope and integrate its recorded branch

This separate operation closes a major, minor or patch coordination scope; it
is not an initiative type or a fifteenth initiative stage. Apply
[WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md).

Use the [integration receipt source](../project/initiatives/integration-receipt.template.md)
for each actual integration or explicit exclusion/transfer/no-deliverable event.
Preserve exact current-cycle identity, source/target tips, closure authority,
method and post-integration verification; record failures as failures.
## Documentary prerequisites

Use the [canonical coverage and use map](../TEMPLATE-COVERAGE.md) and the
[shared preparation procedure](WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation).
The following metadata is a reference inventory of applicable canonical
record roles, not an action list or authority to create every listed record.
<!-- tadp-prerequisites: {"stage":"scope-closure","records":["profile","adoption","scope-registry","membership","scope-closure","integration","coherence","decision-receipt"],"procedure":"WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation"} -->

The executable block below applies these prerequisites to this stage before
its substantive entry check. Existing records and actual events retain their
owners and authority; conditional roles require a cited applicability result.

## Example usage

> **Reference only — do not execute this example.**
>
> Use [scope closure](scope_closure.md) to close the identified scope after
> verifying its inventory and required child integrations.

Only the **Scope closure prompt** block below is executable when invoked.

## Scope closure prompt

```text
Apply the shared workflow contract and authoritative specifications 05, 08,
09, 10 and 11. Close identified scope {version_scope} only under the actual
human close/finalize instruction captured in its closure record. The instruction
supplies only bounded local integration into its recorded immediate parent
after all required gates pass; protocol adoption or terminal status alone does
not. Do not infer remote authority, scope reopening or further ancestor closure.

Before the substantive step, apply documentary prerequisite preparation in
WORKFLOW-CONTRACT.md using
template/TEMPLATE-COVERAGE.md and this stage's inventory.
Classify and prepare only necessary constructible inputs from sufficient
scoped evidence through their owning stages; then validate and recheck this
step's real entry gates. Disclose preparation changes separately. The edit
limits below govern the substantive activity after this preparation.
Reusable source paths below are relative to template/; instantiate only at
the map's declared project-relative destination.
Required inputs: exact adopted scope/parent identity, complete current member
and descendant inventory, truthful closed dispositions, actual required child
integration/aggregate verification/coherence and human closure authority. Use
project/initiatives/version-scopes.template.md, scope-README.template.md,
initiative-index.template.md and integration-receipt.template.md plus mapped
decision/coherence sources. Recover missing documentary prerequisites only
from sufficient actual events through their owning activities. Missing
identity, open members, failed checks or missing authority still blocks
closure; preparation cannot close a member or invent integration. Validate
current inventory, links, topology and actual gates before scope closure.

Before integration, instantiate the reusable integration receipt outside
template/ at the initiative/scope evidence location and capture authority.
Complete its objective fields from actual Git results, never planned values.
Integration state uses exact Pending, Blocked, Merged, Fast-forward,
Already integrated, Direct placement, Excluded, Transferred or No deliverable.

Perform these actions serially:
1. Inspect Git, both branch tips, clean worktree, governing adoption revision,
   scope registry and reciprocal member/child records. Validate exact scope
   syntax, branch role, immutable creation base and immediate parent mapping.
   Inventory every member and descendant at a captured revision, including
   direct hosted and dedicated work, cancelled/superseded outcomes and partial
   effort. Record snapshot and closure authority. No omission by path or status.
2. Require every member and descendant to be closed with truthful disposition.
   Every completed member/child with accepted deliverables must already be
   integrated into this scope or have separately authorized exclusion/transfer
   preserving ownership and the exact closure claim. Pending or blocked required
   integration blocks closure. An empty scope needs explicit no-work disposition.
   Cancelled/Superseded work does not automatically qualify abandoned output.
3. Verify aggregate outputs, applicable checks, coherence inventory, conflict
   reconciliation and exact source diff/current target. Shared whole-tip merges
   are blocked by any unfinished, unaccepted, cancelled or unrelated inclusion.
   Do not cherry-pick, revert, discard or qualify another member without separate
   safe isolation/transfer authority. Preserve unrelated work and latest indexes.
4. Record scope closure independently of initiative lifecycle. Verify the parent
   scope is open; integrating into a closed parent requires its recorded
   authorized reopening first. Merge patch -> matching minor, minor -> matching
   major, major -> captured project integration base. No sibling reparenting,
   self-merge or automatic ancestor closure. Detect already integrated source
   commits on retry. Record fast-forward/already integrated results accurately.
5. Record actual source and target tips, target ref, human authority, method,
   resulting commit, closure snapshot and post-integration verification. Preserve
   failures and pending/blocked integration separately from truthful closure.
   Resolve conflicts only inside accepted scope; route substantive claim changes
   to revision/reopening and renewed acceptance. Retain source branches and
   historical records. A reopened cycle needs fresh delta checks and integration.

Stop affected closure/integration on an unmet gate and retain actual evidence.
Report exact inventory, closure disposition, integration status, refs/tips,
commands/results, authority and outstanding blockers. No hosting service is
required. Publication, pushes and branch removal need separate authority.
```
