# Contract documentation delivery steps

**Initiative:** Contract documentation  
**Status:** Proposed  
**Last updated:** 2026-11-11  
**Initiative type:** `implementation`

Related documents: [initiative](README.md), [architecture](architecture.md),
[mapping](source-mapping.md), [roadmap](implementation-roadmap.md), and
[decisions](open-questions.md).

## Current-state analysis

| Path or system | Current behavior | Planned use or change | Evidence |
|---|---|---|---|
| `evidence/authoritative/architecture` | Owns accepted technical meaning | Read and link only | `ARC-SUITE-001@2.0.1` |
| `evidence/authoritative/security` | Owns NIST/HIPAA policies and evidence gates | Read and link only | Suite revisions `1.0.1` |
| `evidence/non-authoritative/realizations/v1.0` | Preserves candidate D1 intent | Frozen proposal input | `RZN-001-P1-DOCS-N01` |
| Product destination | Not selected | Create only after `DOC-01` acceptance | Open decision and scope assessment |

## Delivery strategy

- Change only the accepted derivative documentation product.
- Land source identity and product structure before content, and content before
  qualification/publication.
- Keep each change reviewable against source mapping and safe-fixture rules.
- Pair any irreversible publication step with an explicit rollback limit.

## Step 1 - Establish product identity and structure

### Objective

Create the accepted destination, consumed-source manifest, navigation,
audience structure, content classes, and review configuration.

### Expected output locations

- Destination selected by `DOC-01`
- Evidence/review location selected with `DOC-05` and `DOC-06`

### Planned output

- Exact architecture/security source identities and documentation revision.
- Audience entry points, source-link rules, authored/generated classification,
  fixture manifest, and concise limitation text.
- Fail-closed rules for missing sources, drift, unsafe data, and overclaim.

### Dependencies

- Accepted initiative, `DOC-01`–`DOC-06`, and reviewed `DOC-A01`–`DOC-A06`.

### Evidence / authoritative

- `ADR-006`, `ADR-007`, and `ARC-CTR-009` D1 gate.
- `SEC-POL-01`–`14` and `HSP-001`–`015` as applicable.

### Migration and rollback

- **Migration or backfill:** No existing D1 product; create a new identified revision.
- **Mixed-version behavior:** Entry points declare exact consumed source revisions.
- **Rollback:** Remove/withdraw the candidate and restore the last reviewed revision; no authority changes.

### Verification

- Validate source manifest, links, destination ownership, and no template residue.
- Test missing/stale sources and prohibited data/claim fixtures fail closed.

### Acceptance

- Product frame matches every accepted decision and scope boundary.
- Review configuration records exact methods, environments, owners, and evidence destinations.

## Step 2 - Author authoritative-source-linked content

### Objective

Create the accepted orientation, contract, operations, security, compatibility,
and evidence guidance with safe examples.

### Expected output locations

- Accepted product destination from Step 1
- Consumed-source and example manifests within the accepted product/evidence boundary

### Planned output

- Source-linked explanations for the accepted audience/content areas.
- Repeated local/non-production limitations and prospective/result distinctions.
- Purpose-created synthetic examples consistent across described surfaces.

### Dependencies

- Step 1 source map, information architecture, and fixture rules.

### Evidence / authoritative

- Exact architecture records `00`–`24` applicable to each page.
- NIST/HIPAA suite indexes, policy IDs, and evidence standards.

### Migration and rollback

- **Migration or backfill:** Not applicable; no prior product is rewritten.
- **Mixed-version behavior:** Content for different source revisions is never presented as one coherent set.
- **Rollback:** Revert the affected derivative to the last source-accurate revision.

### Verification

- Claim/source coverage, terminology, limit, example, and exclusion review.
- Synthetic provenance and leakage scan across product and evidence.

### Acceptance

- Every normative statement maps to authority and every example is safe and non-normative.
- No runtime, conformance, certification, compliance, or regulated-use overclaim remains.

## Step 3 - Generate and reconcile optional derivatives

### Objective

When accepted and available, add only hash-bound observed appendices without
changing the authored contract explanation.

### Expected output locations

- Generated area selected by `DOC-03`
- Drift evidence location selected by `DOC-06`

### Planned output

- Exact input/output identities and observed labels.
- Semantic drift comparison against accepted contracts.
- Blocked output on absent, substituted, or conflicting inputs.

### Dependencies

- `DOC-03`, compatible exact later artifacts, and Step 2 source mapping.

### Evidence / authoritative

- Architecture source precedence and `ADR-006` conflict workflow.
- Exact later product evidence; absence means this step remains deferred.

### Migration and rollback

- **Migration or backfill:** Additive derivative only.
- **Mixed-version behavior:** One appendix references one exact artifact/source set.
- **Rollback:** Remove the appendix and preserve the mismatch finding.

### Verification

- Reproducible generation, content hashes, semantic comparison, and negative substitution tests.
- Review that generated output does not acquire normative wording.

### Acceptance

- Generated bytes and input identities are traceable and source-compatible.
- Deferred absence of later artifacts does not block authored prospective D1 content unless the accepted scope requires them.

## Step 4 - Qualify and publish the D1 product

### Objective

Run the complete documentation gate and preserve evidence for the exact
revision before any completion or publication claim.

### Expected output locations

- Exact product destination selected by `DOC-01`
- Initiative/product evidence destination selected by `DOC-06`

### Planned output

- Structure/link, coverage, drift, fixture/data, claim, compatibility, and
  accessibility/usability results.
- Revision manifest, limitations, reviewer disposition, and rollback record.
- Later completion evidence only if every required gate passes.

### Dependencies

- Steps 1–3 as applicable and no open blocking decision or split.

### Evidence / authoritative

- `ARC-CTR-009` D1 gate and evidence-record fields.
- `SEC-NIST-VER-001` and `SEC-HIPAA-DEV-001` applicable claim gates.

### Migration and rollback

- **Migration or backfill:** Publish one new immutable documentation revision.
- **Mixed-version behavior:** Unsupported combinations remain explicitly unclaimed.
- **Rollback:** Restore prior reviewed product; never erase failed evidence.

### Verification

- Execute every selected automated and manual review against the same revision.
- Exercise broken links, source mismatch, unsafe fixture, generated drift, and interrupted publication.

### Acceptance

- Every exact D1 acceptance outcome passes with limitations recorded.
- Status remains unchanged until separately reconciled through finalization authority.

## Validation matrix

| Requirement or authoritative evidence | Step | Verification | Evidence location |
|---|---|---|---|
| `ADR-007` D1 boundary | 1, 4 | Scope and claim review | Future D1 review record |
| Architecture records `00`–`24` | 1, 2 | Exact source/coverage and semantic review | Future source manifest/report |
| `ADR-006` revision discipline | 1, 3, 4 | Compatibility classification and drift/rollback tests | Future revision record |
| `ARC-CTR-009` D1 gate | 2, 4 | Structure, links, IDs, claims, and limitations | Future qualification record |
| NIST suite `1.0.1` | 1, 2, 4 | Policy applicability and claim review | Future security evidence record |
| HIPAA suite `1.0.1` | 1, 2, 4 | Fixture provenance, limitation, source-currency review | Future security evidence record |

## Final acceptance criteria

- [ ] Every delivery step and verification passes for the same revision.
- [ ] Every authoritative requirement appears in this matrix and source map.
- [ ] Applicable rollback and source-successor handling are exercised.
- [ ] Security, data, accessibility/usability, and review findings are resolved
      or explicitly dispositioned within authority.
- [ ] User- and operator-facing content states exact supported behavior and limitations.
- [ ] Canonical tuple identity remains unchanged and reciprocal.
- [ ] Status, index, product, and completion evidence truthfully reconcile.
