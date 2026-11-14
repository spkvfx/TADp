# TADp evidence register

**Register owner:** Current repository owner (respective owner in a fork); see OWNERSHIP-001  
**Last reviewed:** 2026-11-14  
**Review cadence:** At source intake, authority change, or adoption review  

## Classification rules

- Label an artifact `../../../evidence/authoritative` only when a named authority has
  made it binding for a stated subject.
- Label contextual, exploratory, or observational material
  `../../../evidence/non-authoritative`.
- Preserve the original artifact and record a revision relationship instead of
  overwriting history.

## Evidence inventory

| Evidence ID | Classification | Artifact and precise locator | Governs or informs | Owner | Revision/date | Status |
|---|---|---|---|---|---|---|
| EVD-001 | `../../../evidence/authoritative` | [Suite index](authoritative/LLM/00_Codex_Invariant_Suite_Index.md#purpose) and its named specifications | Binding governing requirements retained unchanged; installation alone is not prospective adoption | Upstream source authority; project steward is the current repository owner | Source commit 6120bd10bb2e368274fd5bd4ff5481d33f61c4c6 | Prospectively adopted by ADOPTION-001 |
| EVD-002 | Human setup decision, exact bounded authority | [SETUP-001](../decisions/SETUP-001.md#exact-human-response) | Installation and local workflow only | Requesting human; captured by Codex | Current session, 2026-11-14 | Recorded; no owner appointment or adoption inferred |
| EVD-003 | `../../../evidence/non-authoritative` | [Setup verification](non-authoritative/setup/verification.md) | Observed preflight, assembly, context, checks and review; does not prove semantic conformance | Codex; current repository owner is continuing human steward | 2026-11-14 | Setup evidence |
| EVD-004 | Non-authoritative preparation and observed verification | [Documentation split preparation](non-authoritative/documentation-split/preparation.md) and [verification](non-authoritative/documentation-split/verification.md) | Exact source/destination mapping, prepared candidate/support docs, isolated trials and pending boundary decisions; no initiative acceptance or delivery | Codex; current repository owner retains human authority | Source 014d455e3d99213e0dc4a156cb198ac1a4a85747; captured 2026-11-14 | Prepared and qualified; protected delivery pending |
| EVD-005 | Non-authoritative preparation and observed verification | [Documentation refresh preparation](non-authoritative/documentation-refresh/preparation.md), [coverage](non-authoritative/documentation-refresh/coverage.md), and [verification](non-authoritative/documentation-refresh/verification.md) | Current usage/feature review, reused and revised candidate documentation, exact delivery mapping and actual checks; no acceptance, introduction, promotion or rollout | Codex; current repository owner retains human authority | Prompt/baseline 345a05559afc177f50609ccc2bb819a050f284b3; captured 2026-11-14 | Bounded candidate preparation; see verification for actual qualification and remaining gates |

## Classification and conflict log

Later authority events: [OWNERSHIP-001](../decisions/OWNERSHIP-001.md#exact-human-response)
appoints the repository-owner role, including respective fork owners;
[ADOPTION-001](../decisions/ADOPTION-001.md#exact-human-response) explicitly adopts
the pinned installed baseline. Neither is inferred from the setup invocation or
verification. They accept no initiative and authorize no protected-source change.

| Date | Evidence ID | Classification decision or conflict | Decision owner | Resolution or next review |
|---|---|---|---|---|
| 2026-11-14 | EVD-001 through EVD-003 | Preserve suite standing, actual setup authority, and observed evidence separately | Current repository owner; see ADOPTION-001 for the later explicit adoption decision | Before governed scope allocation or initiative acceptance; see SETUP-001 |

## Intake checklist

- [ ] Preserve the source, author or owner, date, and available revision.
- [ ] Assign an evidence ID and a classification.
- [ ] Record a precise locator rather than a directory-only reference.
- [ ] Link the initiatives or products materially affected by the artifact.
- [ ] Record any conflict with binding evidence before relying on the artifact.
