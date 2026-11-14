# Workflow stage 0–13 migration

## Purpose

This guide explains how to migrate an active initiative from the earlier
0–10 prompt sequence to the authoritative 0–13 workflow. It preserves the
initiative's evidence, decisions, lifecycle history, and recorded workflow
identity. It does not grant acceptance or permission to deliver work.

The governing contract is the
[Codex initiative workflow specification](../../evidence/authoritative/LLM/08_Codex_Initiative_Workflow_Specification.md).
Use that specification when this guide and an initiative record appear to
differ.

## Stage mapping

| Earlier stage | Current stage | Migration consequence |
|---|---|---|
| 0 — Initiative preparation | 0 — Initiative preparation | No renumbering |
| 1 — Proposal creation | 1 — Proposal creation | No renumbering |
| 2 — Proposal alignment | 2 — Proposal alignment | No renumbering |
| 3 — Initiative creation | 3 — Initiative creation | No renumbering |
| 4 — Initiative alignment | 4 — Initiative alignment | No renumbering |
| 5 — Assumption confirmation | 5 — Assumption confirmation | No renumbering |
| 6 — Open-question resolution | 6 — Open-question resolution | No renumbering |
| Not separate | 7 — Initiative acceptance | New explicit human gate |
| 7 — SDK/API alignment | 8 — SDK/API alignment | Renumbered; implementation only |
| 8 — Implementation-readiness review | 9 — Implementation-readiness review | Renumbered; implementation only |
| 9 — Initiative execution | 10 — Implementation execution | Renumbered and explicitly type-specific |
| Not separate | 11 — Design delivery | New design path |
| Not separate | 12 — Planning delivery | New planning path |
| 10 — Finalization | 13 — Finalization | Renumbered after all type-specific paths |

## Migration procedure

1. Record the earlier workflow revision and the initiative's current stage and
   lifecycle state. Do not rewrite historical stage numbers in existing
   records.
2. Compare the current initiative suite with the entry contract for its next
   current stage. Preserve all earlier receipts, evidence classifications,
   limitations, and lifecycle history.
3. Add a migration entry to the initiative record that names the old and new
   workflow revisions, the effective commit, the stage mapping, the human
   authority for the migration, and every affected record.
4. Reconcile links to renamed prompts without changing the meaning of the
   decisions or work they document.
5. Continue only after the applicable state-specific rules below are met.

## State-specific handling

### Proposed

Complete stage 7 before beginning any type-specific delivery path. Earlier
assumption or question decisions may satisfy their own gates, but none of them
implicitly accepts the initiative.

### Accepted

Confirm that an explicit human acceptance decision exists for the exact
accepted baseline. Create or link an acceptance receipt only from the preserved
human prompt and response. Never reconstruct or fabricate acceptance from a
status label, prior implementation, or a general instruction to continue.

If exact acceptance evidence is unavailable, return the initiative to stage 7
and obtain a current human decision before delivery resumes.

### In progress

Verify the accepted baseline first. An implementation initiative continues
through stages 8–10 and maintains `execution-record.md`. A design initiative
continues through stage 11 and maintains `delivery-record.md`. A planning
initiative continues through stage 12 and maintains `delivery-record.md`.
Create a missing work record from truthful existing evidence; do not invent
past commands, results, decisions, or dates.

### Completed

A historical completed initiative may retain its recorded earlier workflow
when its completion remains compatible with the authoritative invariants. Do
not relabel or renumber its history solely for consistency. If it is reopened,
record the reopening and migration explicitly, then use the current workflow
for the new or revised claim.

## Finalization and mixed revisions

Do not combine old and current stage contracts silently. Before stage 13,
confirm that the initiative record states which workflow revision governed
delivery, that the required execution or delivery record exists, and that
completion evidence supports the same accepted claim. A prompt filename change
is not evidence of a lifecycle transition or completed work.
