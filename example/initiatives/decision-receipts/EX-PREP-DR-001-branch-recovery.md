# EX-PREP-DR-001: authorized branch preparation recovery

**Receipt ID:** `EX-PREP-DR-001`

**Source event:** `EX-PREP-001`, recovery of `EX-AQ-PREFLIGHT-001`

**Human authority:** User, repository and Example Record Application owner

**Actual planning and execution author:** Codex (`/root`)

**Capture date:** 2026-11-12

**Disposition:** Authorized local merge and preparation recovery; execution pending

**Git commit:** Discoverable through this receipt's Git history; actual results
are appended after execution.

## Exact human instruction and context

After the blocked automatic review, Codex explained:

> The needed next step is to prepare the assigned branches with the current scaffold and initiative records, and reconcile the adoption-history mismatch. Once that passes verification, the automatic reviews can proceed without asking you to approve each answer.

The User responded, attaching the same example review prompt:

> ok. apply all relevant merges and clean up the repository I guess.

This specifically authorizes the preparation and history reconciliation just
described, including installation of the existing locked scaffold onto the
otherwise empty assigned branches. It does not authorize semantic changes to
protected sources, lock refresh, changed initiative claims, acceptance,
delivery, scope closure, upward integration of Proposed work into `main`,
remote publication, history rewriting, or deletion of historical refs.

## Evidence and bounded recovery plan

The [prior preflight](EX-VSG-VER-001-migration-verification.md#assumption-and-question-review-preflight-2026-11-12)
preserves 36 unresolved assumptions, 37 unresolved questions, missing current
suites on all six assigned continuations, and the failed `TADP048` ancestry
check. Those source decisions and all six `Proposed` lifecycle states remain
unchanged by this administrative recovery.

Initial checkout: `v1` at `c592920f0b0e2114c4305464fb29605400486b2e`.
Only the two previously authored preflight tracking files were modified;
the index was empty and there were no untracked files. Preserve and commit
that evidence with this authority record before merging. No unrelated work
is included. Git metadata is outside `example/` only under
[EX-GIT-DR-001](EX-GIT-DR-001-enclosing-worktree-exception.md).

Serial execution plan, independently checked by `/root/merge_audit`:

1. Commit this authority and the preserved preflight notes on `v1`. Retain
   the existing validator failure as evidence; this diagnosis commit is not
   a review disposition, passing preparation claim or initiative acceptance.
2. Merge the already available `origin/docs/example-app-decision-prompt`
   at `703177aec5dfc57d838827c437d37a51a12c0a20` into `v1`. Its committed
   tree equals the initial `v1` tree; legacy three-way preview reports no
   changes or conflicts. This joins original protocol/migration history and
   restores the recorded `873021eef226576aebfc60b94f69886eb4da4a1c`
   adoption ancestry without replacing that identity or fetching remotely.
3. Merge local `main` at `36bb20c88802191e13b873a36a07531fcfab5f42`
   into `v1`, leaving the `main` ref and its other worktree untouched.
   Its independent README commit is not currently an ancestor of `v1`.
   Reconcile the anticipated `protocol/README.md` conflicts using current
   adopted workflow, prompt-boundary and migration guidance; preserve any
   independent editorial contribution. This authorizes necessary README
   merge resolution outside the example scaffold, not protocol redesign.
4. Verify the resulting current baseline and commit recovery tracking. Then
   install this exact prepared baseline on `v2`, `v3`, `v4` by fast-forward
   merge. These existing refs retain their recorded creation parents/bases;
   copying the administrative baseline is not sibling creation/reparenting
   or completion integration. Propagate from each major to its recorded
   minor, then from that minor to its assigned continuation, using only
   fast-forward merges and clean checkouts. Stop on unexpected divergence.
5. Verify actual assigned checkouts, adoption ancestry, protection, full
   validation/local links, unchanged correlation fields and source decisions,
   regression tests and exact diffs. Record actual tips and results, reconcile
   current preparation tracking, and leave a clean prepared checkout.

## Exact targets and immutable prior tips

| Preparation target | Recorded parent used for minor/continuation propagation | Prior tip |
|---|---|---|
| `v1` | History repair from cached original source and `main` | `c592920f0b0e2114c4305464fb29605400486b2e` |
| `v2`, `v3`, `v4` | Explicit installation of the verified administrative baseline | `36bb20c88802191e13b873a36a07531fcfab5f42` |
| `v1.0` | `v1` | `7b9d302b3dc7a94627518e42819a3130b5ba17d3` |
| `v2.0`, `v2.1`, `v2.2` | `v2` | `36bb20c88802191e13b873a36a07531fcfab5f42` |
| `v3.0` | `v3` | `36bb20c88802191e13b873a36a07531fcfab5f42` |
| `v4.0` | `v4` | `36bb20c88802191e13b873a36a07531fcfab5f42` |
| `initiative/v1.0-INIT-IMP-001-contract-documentation` | `v1.0` | `7b9d302b3dc7a94627518e42819a3130b5ba17d3` |
| `initiative/v2.0-INIT-IMP-002-container-platform` | `v2.0` | `36bb20c88802191e13b873a36a07531fcfab5f42` |
| `initiative/v2.1-INIT-IMP-003-api-sqlite-runtime` | `v2.1` | `36bb20c88802191e13b873a36a07531fcfab5f42` |
| `initiative/v2.2-INIT-IMP-004-python-sdk` | `v2.2` | `36bb20c88802191e13b873a36a07531fcfab5f42` |
| `initiative/v3.0-INIT-IMP-005-standalone-cli-image` | `v3.0` | `36bb20c88802191e13b873a36a07531fcfab5f42` |
| `initiative/v4.0-INIT-IMP-006-web-application-bundle` | `v4.0` | `36bb20c88802191e13b873a36a07531fcfab5f42` |

Preserve canonical membership, scope creation evidence, provenance, revision
cycles, original locked `template/**` and `evidence/authoritative/LLM/**`
content, all historical initiative refs, protocol/migration source refs and
remote-tracking refs. Existing scope closure and initiative integration
states remain pending; installation is distinct from delivery integration.

## Effective settings, obligations and restoration

This new ordinary instruction contains no operative directive. All recovery
blocks retain `human_gates=true`, `other_gates=true`, `preview=false`,
`local=false`, `review=false`. Work is serial because it shares one checkout
and depends on the prior merge. This receipt is explicit preparation authority,
not a gate waiver. No new generic invariant exception or inferred directive
is activated. The recovery ends at verified clean branch preparation; any
resumed automatic source review retains its separate prompt, exact authority,
per-item receipts, D1-D6 sequence and independent-review requirements.

Risks are conflicting historical documentation and propagating an incomplete
baseline. Resolve only inspected documentation conflicts, verify before
propagation, preserve all original tips and failed checks, and stop on new
unrelated changes. Historical records remain append-only. No branch deletion
is necessary to obtain a clean worktree.
