# Initiative coherence migration

This guide applies the [initiative coherence specification](../../evidence/authoritative/LLM/10_Codex_Initiative_Coherence_Specification.md)
to an existing TADp project. It does not accept an initiative, reopen a closed
claim, resolve a work conflict, or revise project architecture.

## Adoption

1. Preserve the current Git baseline and inventory existing initiative states,
   specifications, decisions, planned effort, partial outputs, and completion
   evidence. Keep unrelated changes separate.
2. Adopt one coherent protocol revision containing the authoritative rule,
   reusable templates and prompts, verified runtime tools, and reviewed
   protected-source locks. Record the adopting authority and the resolved
   pre-adoption Git commit in the project profile's
   `Coherence revision baseline` field. This fixed predecessor separates
   historical completions from newly governed completion claims.
3. Instantiate `initiatives/work-conflicts.md` from its reusable source. Link
   any known incompatible work claims to the exact affected initiative
   records. Preserve the source standing of each claim; also use the invariant
   conflict register when an invariant is contradicted.
4. Review active initiatives at their next material alignment, acceptance,
   delivery, or completion handoff. Record new evidence and effort at risk,
   then route revisions through the target's existing type and human gates.
5. Add the cross-initiative coherence review to new completion evidence under
   the adopted revision. Inventory every other open initiative, including
   `Proposed` effort, and relevant closed claims. Record the reviewed baseline,
   targets, findings, and dispositions, including an evidenced no-target result
   where appropriate.
6. Run protected-source checks, full validation, and applicable project-owned verification. Use an
   explicit Git comparison baseline in CI when reviewing a whole branch.

## Historical claims and reopening

Adoption is prospective. Do not invent a review for a historical completion,
retroactively accept proposed effort, or rewrite a truthful closed record to
make it appear governed by the new revision. Preserve its earlier workflow
identity and evidence. Any later refinement is subject to the new closed-claim
protection.

When a finding affects a closed initiative, record the finding and impact in
the new work and project conflict register first. Obtain explicit human
reopening authority before changing the closed specification. Append the
reopening event, preserve the prior claim, and return to the legal active
state. Under adopted [scope intake](version-scope-migration.md), a human instruction
to process an identified realization delegates necessary reopening and coherent
same-outcome revision. Record the actual agent decision before changing records;
return changed claims to `Proposed`, preserve prior evidence and obtain renewed
human acceptance. Independent outcomes and incompatible boundaries still split.
A direct closed-to-`Accepted` return requires a separate human unchanged-claim
decision. Unadopted records retain the predecessor workflow.

Append-only factual corrections and successor references may preserve history
without refining the closed claim. They must not conceal a changed scope,
decision, acceptance criterion, or verification obligation.

## Resolution and limits

Every work conflict retains both exact claims, their lifecycle and authority,
the effort affected, an accountable owner, blocked gates, and a linked
resolution or explicit re-entry condition. Do not resolve competing effort by
recency or by declaring the newest completed initiative authoritative.

Structural validation checks records and Git evidence. Human review still
determines whether the inventory is complete, the claims are compatible, the
effort was represented honestly, and the selected resolution is authorized.

The validator compares current initiative files with `HEAD` by default. In a
branch review or CI job, use `--base-ref <captured-base-commit>` to cover changes
across the whole branch. The adoption baseline remains fixed; the comparison
base is selected for the review being performed. Neither field authorizes a
revision or reopening.
Keep the adoption declaration and its captured baseline immutable. Removing
or deactivating the declaration cannot disable controls already adopted.
Branch review checks intermediate terminal states as well as the initial
snapshot, so closing and then silently refining work in separate commits does
not evade the rule.
