<!--
Create one suite index during Stage 0 for one canonical work version and one
self-contained initiative. Place it in the suite directory as a stable
00-...-suite-index.md filename. Replace every token and remove this comment.
-->

# {{realization_suite_title}}

**Work version:** {{v_major_minor}}

**Suite ID:** {{realization_suite_id}}

**Suite path:** {{project_relative_suite_path}}

**Status:** Recorded; non-authoritative proposal input

**Recorded by:** {{human_team_or_source}}

**Recorded date:** {{yyyy-mm-dd}}

**Initiative ID:** {{initiative_id}}

**Initiative type:** `{{implementation_design_or_planning}}`

**Initiative path:** [{{initiative_path}}]({{relative_initiative_path}})

**Dedicated branch:** {{initiative_branch}}

**Captured base branch:** {{base_branch}}

**Captured base commit:** {{base_commit}}

**Predecessor or successor:** {{relationship_or_none}}

**Canonical project correlation:** [initiative and correlation register]({{relative_initiative_index_path}}#initiative-and-correlation-register)

**Lifecycle status and evidence:** Proposed; [initiative lifecycle]({{relative_initiative_readme_path}}#initiative-lifecycle)

> **Evidence standing:** This suite is permanently non-authoritative proposal
> input. Its version, initiative, and branch links establish identity and
> navigation only. They do not accept the initiative, establish authority,
> prove delivery, or create release status.

## Suite boundary

**Single outcome:** {{one_narrow_outcome}}

**Owner and authority boundary:** {{owner_and_authority_boundary}}

**Output family:** {{product_specification_or_evidence_family}}

**Verification claim:** {{one_verification_claim}}

Every note cataloged below must share this boundary. A note with an
independently acceptable outcome, different owner or authority, different
output family, separable verification, or independent lifecycle requires a new
work version, suite, initiative, and branch.

## Document catalog

| Order | Realization ID | Work version | Role |
|---:|---|---|---|
| 00 | {{realization_suite_id}} | {{v_major_minor}} | Suite identity, boundary, standing, reciprocal correlation, and navigation |
| 01 | [{{realization_id}}]({{realization_note_filename}}) | {{v_major_minor}} | {{note_role}} |

## Handoff

The paired initiative remains `Proposed` until its separate human acceptance
gate passes. Later stages must verify this suite against the canonical
correlation row and must not rewrite the suite to imply acceptance or
completion.
