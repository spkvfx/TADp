# Version-realization-suite-initiative correlation delivery steps

**Initiative:** INIT-DSN-001-version-realization-correlation

**Status:** Proposed

**Last updated:** 2026-11-10

**Initiative type:** design

Related documents:

- [Initiative README](README.md)
- [Architecture](architecture.md)
- [Evidence mapping](source-mapping.md)
- [Delivery roadmap](implementation-roadmap.md)
- [Open questions and decisions](open-questions.md)

## Current-state analysis

| Path or system | Current behavior | Planned use or change | Evidence |
|---|---|---|---|
| protocol/evidence/authoritative/LLM and example counterpart | Protected specifications 00-08; no work-version correlation specification | Add specification 09 and coherent references after acceptance | EVD-01 and protected locks |
| protocol/template and example counterpart | Protected initiative/project/workflow sources; no suite-index template or canonical tuple | Add reciprocal identity fields and stage continuity | EVD-07 and template inventory |
| protocol/realizations, example/realizations, and realization path consumers | Obsolete top-level README aliases remain while actual records and reusable scaffolds use `evidence/non-authoritative/realizations/**`; some wording still permits reclassification | Remove aliases, make the evidence path canonical everywhere, and require separate accepted records for derivative claims | EVD-03, MAP-014, and repository consumer audit |
| protocol/tools, protocol/tests, and example counterparts | Structural/lifecycle/protection checks; no correlation graph validation | No change here; create exact handoff to implementation sibling | EVD-06/EVD-07 and current validator source |
| example/evidence/non-authoritative/realizations | Observed v0.0-v4.0 sources; no tracked v3.1/v4.1 | Inventory and preserve; do not migrate on this branch | EVD-04/EVD-05 |
| Four protected .tadp-lock.json files | Hash current protected baselines | Refresh last after authorized source review and verification | EVD-01/EVD-03 and protection workflow |

## Delivery strategy

- Follow the design boundary: specifications and supporting design evidence
  only.
- Update protocol and example protected counterparts as matched pairs.
- Preserve predecessor authority and migration limits in every successor
  specification.
- Make locks the final source-recording step, never a drift suppressor.
- Hand executable work to a separate implementation tuple.

## Step 1 - Establish the authoritative correlation model

### Objective

Create one complete specification 09 and reconcile only necessary invariant
references in both protected authoritative suites.

### Expected output locations

- protocol/evidence/authoritative/LLM/09_Codex_Version_Realization_Initiative_Correlation_Specification.md
- example/evidence/authoritative/LLM/09_Codex_Version_Realization_Initiative_Correlation_Specification.md
- Necessary protected specification 00-08 counterparts in both trees

### Planned output

- Exact canonical grammar, positive/negative examples, arbitrary-size numeric
  parsing, comparison, immutability, uniqueness, and version-class separation.
- One-to-one forward and reverse mapping plus canonical-row ownership.
- Self-contained suite/initiative, split/successor, evidence/lifecycle,
  workflow, recovery, compatibility, migration, and effective-point clauses.
- Permanent non-authoritative realization standing, sole canonical placement,
  and the separate-record rule for accepted derivative claims.

### Dependencies

- Receipt-backed assumptions and VRC-01 disposition.
- Exact Stage 7 acceptance of the aligned baseline.

### Authoritative evidence

- Current specifications 01, 02, 04, 05, 06, 07, and 08.
- User's exact 2026-11-10 invariant authority.

### Migration and rollback

- **Migration or backfill:** No legacy backfill; publish compatibility and
  migration requirements only.
- **Mixed-version behavior:** Active initiatives retain their recorded
  compatible workflow or adopt through an explicit change record.
- **Rollback:** Preserve predecessor Git history and locks; any correction is
  an authorized successor, not a silent historical rewrite.

### Verification

- Review every normative clause against MAP-001 through MAP-013.
- Compare protocol/example counterpart semantics and links.

### Acceptance

- Specification 09 is complete and coherent with 00-08.
- No unrelated invariant changed and no conflict-register edit lacks evidence.

## Step 2 - Integrate reciprocal records and workflow stages

### Objective

Make protected reusable sources create and preserve one tuple without changing
stage numbering, permanent realization standing, canonical placement, or
lifecycle gates.

### Expected output locations

- protocol/template/project/evidence/non-authoritative/realizations and example counterpart
- protocol/template/initiatives, protocol/template/project, and example counterparts
- protocol/template/prompts and example counterpart

### Planned output

- A realization-suite-index template and updated realization guidance.
- Canonical `evidence/non-authoritative/realizations/**` references throughout
  protected consumers, with no top-level alias or in-place promotion wording.
- Correlation metadata in README, project profile, initiative index, status,
  execution, delivery, completion, and traceability templates.
- Stage 0 preflight and atomic preparation; Stage 1-13 tuple continuity checks,
  handoffs, and recovery.

### Dependencies

- Step 1 authoritative terms and ownership.

### Authoritative evidence

- Accepted specification 09.
- Current workflow, lifecycle, Git, scope, and receipt specifications.

### Migration and rollback

- **Migration or backfill:** Templates affect new/adopted work; existing
  initiatives migrate explicitly.
- **Mixed-version behavior:** Historical prompts keep their recorded identity.
- **Rollback:** Preserve predecessor protected baseline and require authorized
  correction if the accepted design fails verification.

### Verification

- Check every token has one stage owner and no unresolved token escapes
  protected templates.
- Audit all fourteen prompts for the shared contract, target tuple, edit
  boundary, evidence/lifecycle limits, and stage-specific continuity.
- Search all protocol, template, prompt-template, and example consumers for
  stale top-level placement or conditional realization classification.
- Compare protected protocol/example counterpart content.

### Acceptance

- Future Stage 0 can create a complete tuple as one preparation unit.
- Later stages cannot silently operate on another version, suite, initiative,
  or branch.

## Step 3 - Preserve legacy mappings and specify executable enforcement

### Objective

Create initiative-local migration and implementation handoff evidence without
performing migrations or product work.

### Expected output locations

- protocol/initiatives/design/INIT-DSN-001-version-realization-correlation/legacy-migration-ledger.md
- protocol/initiatives/design/INIT-DSN-001-version-realization-correlation/validator-implementation-handoff.md

### Planned output

- Required ledger columns and rows for requested and observed legacy
  identities, suites, initiatives, branches, action, evidence, and blockers.
- Exact v4/VRC-01 disposition and preserved non-authoritative standing.
- Validator discovery, parser, graph, lifecycle/evidence, legacy compatibility,
  finding, fixture, test, documentation, and parity requirements.

### Dependencies

- Steps 1-2 and VRC-01; VRC-02 may remain a receipt-backed deferral.

### Authoritative evidence

- Accepted specification 09 and evidence-authority requirements.
- Receipt-backed VRC-01/VRC-02 dispositions.

### Migration and rollback

- **Migration or backfill:** No migration performed; ledger prescribes one
  tuple-specific branch at a time after adoption.
- **Mixed-version behavior:** Observed, requested, and canonical identities are
  separate columns; no alias is implied.
- **Rollback:** Correct ledger analysis with an append-only evidence note or
  receipt-backed revision; never rewrite source history.

### Verification

- Audit that every required identity appears and each absence remains explicit.
- Prove the handoff includes all required positive/negative cases and cannot
  infer human decisions or lifecycle.

### Acceptance

- The v4 case is exact, non-authoritative, and traceable.
- A future implementation initiative can implement objective checks without
  expanding this design's scope.

## Step 4 - Verify protected parity and refresh locks last

### Objective

Prove the accepted design output, record lock authority, and reconcile
delivery/completion evidence.

### Expected output locations

- protocol/evidence/authoritative/LLM/.tadp-lock.json
- protocol/template/.tadp-lock.json
- example/evidence/authoritative/LLM/.tadp-lock.json
- example/template/.tadp-lock.json
- Initiative delivery record and completion evidence

### Planned output

- Explained pre-refresh protection findings for only authorized source drift.
- Four refreshed locks carrying the exact user instruction as authority.
- Exact verification results and reconciled lifecycle/tracking evidence.

### Dependencies

- Steps 1-3 complete and reviewed.

### Authoritative evidence

- Suite protection revision, protected-source instructions, and User's exact
  lock authority.

### Migration and rollback

- **Migration or backfill:** Lock refresh records reviewed current content; it
  does not migrate adopters automatically.
- **Mixed-version behavior:** Existing adopters use explicit adoption guidance.
- **Rollback:** Stop on any unexplained digest/file-set drift; restore or
  investigate rather than refresh.

### Verification

- Run protected checks, validators, regression tests, local-link checks,
  placeholder checks, path matrix, and parity audit before refresh.
- Refresh locks only after the authorized source set is complete and reviewed.
- Rerun all checks and record exact commands, exits, findings, and limitations.

### Acceptance

- All protected content and locks agree with the accepted design.
- Completion evidence excludes validator implementation and legacy migration.

## Validation matrix

| Requirement or authoritative evidence | Step | Verification | Evidence location |
|---|---|---|---|
| Canonical syntax and numeric ordering | 1 | Specification examples and future parser handoff | Specification 09 and validator handoff |
| Bijection, reciprocal links, orphans, and branch/version identity | 1-2 | Record ownership and stage matrix review | Architecture, protected templates/prompts |
| Self-contained initiatives, splits, successors, and reopening | 1-2 | Scope/lifecycle cross-review | Specification 09 and reusable sources |
| Evidence and lifecycle standing plus canonical realization placement | 1-3 | Authority wording and consumer-path audit | Source map, spec, templates, prompts, guides, examples, ledger |
| Required legacy identities and v4 case | 3 | Source/Git inventory and receipt audit | Legacy migration ledger |
| Positive and negative validator cases | 3 | Handoff completeness review | Validator implementation handoff |
| Protocol/example synchronization | 1-4 | Protected counterpart parity review | Delivery record |
| Authorized lock refresh | 4 | Pre/post protection checks and lock authority audit | Four locks and completion evidence |

## Final acceptance criteria

- [ ] Every delivery step is complete and its verification passes.
- [ ] Every authoritative requirement maps through source-mapping.md.
- [ ] Every protected protocol/example counterpart is synchronized.
- [ ] The migration ledger preserves source identity and contains no invented
      lifecycle evidence.
- [ ] Validator product work is fully handed off and absent from this branch's
      design completion claim.
- [ ] Locks were refreshed last with the exact authority and pass rechecks.
- [ ] Delivery record, completion evidence, README, suite, initiative index,
      status, and Git commits describe the same bounded claim.
