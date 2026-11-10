# Contract versioning and implementation-feedback governance

**Decision ID:** `ADR-006`  
**Status:** Accepted  
**Architecture revision:** `2.0.1`  
**Decision owner:** User, project authority  
**Decision date:** 2026-11-10  
**Supersedes / superseded by:** Not applicable  
**Related initiative:** Not applicable - direct project-architecture instruction  

## Decision question

How are architecture/documentation, Compose, OCI images, API, SDK, CLI, web,
and database contracts versioned when implementation evidence reveals an
omission or impractical choice?

## Context and binding evidence

| Source | Precise claim or constraint | Effect on this decision |
|---|---|---|
| [`AUTH-EX-001.8`](01-accepted-architecture-baseline.md) | Released contract meaning is versioned and never rewritten to match drift | Requires immutable historical meaning and governed successors |
| [`RZN-001`](../../non-authoritative/realizations/v0.0/RZN-001-example-record-application.md), feedback loop and Q16 | Documentation guides implementation; evidence should refine it without losing identity | Requires explicit classification/reconciliation workflow |
| [Evidence authority specification](../LLM/01_Codex_Evidence_Authority_Specification.md) | Implementation evidence cannot override architecture | Prohibits product-led silent contract changes |

## Decision

### Version identities

| Artifact | Active identity | Version rule |
|---|---|---|
| Architecture suite | `ARC-SUITE-001` revision `2.0.1`; predecessor `2.0.0` at Git commit `5f0c325`, with `1.0.0` in `ARC-REV-001` | Semantic revision recorded in index, affected records, and preserved predecessor/successor link |
| Compose application | Project/release semantic version plus normalized effective-config hash | Any service/network/volume/port/security/default change is reviewed for architecture/compatibility effect |
| API OCI image | API product semantic version plus immutable multi-platform manifest digest | Labels declare architecture, API, schema, source commit, and dependency/SBOM identity |
| HTTP API | `/api/v1` | Major path identifies compatibility family; accepted schema/semantics form one baseline |
| Python SDK | Wheel semantic version and SHA-256 | Major tracks incompatible public Python API; image/build metadata declares wheel and server compatibility |
| CLI | CLI semantic version plus CLI image manifest digest | Major tracks incompatible command/JSON/exit/Compose invocation behavior; image labels identify installed SDK |
| Web assets | Product semantic version plus bundle hashes embedded in API image | Must declare compatible API major; entry/assets and API image deploy coherently |
| SQLite schema | Positive integer `PRAGMA user_version` plus checksummed migration IDs | Every schema change uses the next migration; downgrade is not implicit |
| Conformance vectors | Architecture revision plus stable vector IDs | Existing vector meaning is preserved; new revision may add IDs or explicitly supersede them |

### Change classification

- **Patch (`x.y.Z`)**: fixes spelling, broken links, or explanatory ambiguity
  only when no conforming implementation/test/user could behave differently.
- **Minor (`x.Y.0`)**: adds backward-compatible optional behavior that old
  clients can safely ignore and does not widen closed record/request objects
  or alter existing results/errors. Every consumer compatibility claim must be
  evidenced.
- **Major (`X.0.0`)**: changes any accepted value, normalization, field,
  required input, route, status/problem meaning, ordering, regex semantics,
  cursor, update/concurrency rule, public command/model, host prerequisite,
  service/network/volume graph, data-mount authority, trust boundary, or
  behavior on an existing input.

A purported clarification that changes a conformance vector is not a patch.
When classification is uncertain, treat the proposal as breaking until the
architecture authority explicitly decides otherwise with evidence.

### Feedback workflow

1. Preserve the exact architecture revision, implementation version/commit,
   observed behavior, environment, and reproducer.
2. Classify the observation as implementation defect, documentation defect,
   missing architecture decision, dependency limitation, or proposed feature.
3. Compare it with every affected accepted claim; record an invariant conflict
   immediately when behavior contradicts the current suite.
4. Correct the implementation when the accepted contract remains viable.
5. If a contract change is proposed, create a narrowly scoped design initiative
   or direct explicit architecture-authority instruction, impact analysis,
   compatibility/migration plan, revised vectors, and successor/revision links.
6. Obtain explicit human acceptance before the new meaning becomes effective.
7. Reconcile Compose, image digests/labels, API, SDK, CLI, web bundle, database
   migration/volume procedures, docs, and conformance claims; do not mark any
   product compatible until its containerized tests pass the new baseline.

When a change affects security standing, permitted data/use, inherited
controls, or a security claim, the same workflow must reconcile the applicable
NIST and HIPAA suite revisions. A policy cannot be treated as implementation
evidence, and an architecture patch cannot silently lower a policy gate.

Git history and revision tables preserve earlier meaning. Editing an accepted
record in place is permitted only as the explicit recorded revision operation;
the prior accepted content must remain recoverable and linked.

## Consequences

### Benefits

- Future readers can identify which contract an implementation actually used.
- Implementation learning improves the design without converting behavior
  into authority automatically.
- Consumers can reason about compatibility independently across product
  versions.
- Database migrations and API/client changes remain coordinated.

### Costs, risks, and required follow-up

- Even small semantic changes require impact analysis and explicit authority.
- Architecture, conformance fixtures, and product version metadata must be
  maintained together.
- Parallel old/new major versions require an explicit support and migration
  plan; revision `2.0.1` does not support the superseded native runtime.
- Image tags, base tags, local build caches, Compose overrides, and generated
  effective configuration can drift unless immutable digests/hashes are
  recorded and tested.
- Generated OpenAPI, schemas, examples, and docs are derivative artifacts and
  need drift checks against the accepted source.

## Alternatives considered

| Alternative | Why it was not selected | Reconsideration trigger |
|---|---|---|
| Edit docs to match each implementation | Erases contract identity and lets lower-standing behavior govern | Never under evidence protocol |
| Treat every addition as non-breaking | Closed requests/enums/clients can break on additions | Only with proven consumer behavior for the specific change |
| Date-only versions | Do not communicate compatibility class | May supplement, not replace, semantic identities |
| Generate architecture solely from code/OpenAPI | Observed implementation cannot own architectural meaning | Generated artifacts remain useful verification outputs only |
| Freeze one baseline permanently | Prevents evidence-led improvement and migration | Not selected; governed successors are permitted |

## Acceptance and verification

| Required result | How it is verified | Evidence location |
|---|---|---|
| Product declares exact architecture/Compose/image/API/SDK/schema compatibility | Image labels, manifest/config hashes, wheel/bundle hashes, and product metadata review | Future product records |
| Breaking change cannot enter same major silently | Diff classifier plus architecture/human review | Future design initiative evidence |
| Generated contracts do not drift | Snapshot/schema comparison against accepted vectors | Future API/SDK evidence |
| Migration supports every declared prior schema | Fixture migration and restore tests | Future persistence evidence |

## Revision record

| Date | Change | Authority |
|---|---|---|
| 2026-11-10 | Accepted semantic change classes and governed implementation-feedback workflow | User-authorized best-judgment architecture method recorded in `ARC-AUT-001` |
| 2026-11-10 | Applied the workflow to preserve `1.0.0` and establish container-only `2.0.0`; added Compose/image/artifact identities | User's explicit Dockerization/no-host-services authority preserved in `ARC-REV-001` |
| 2026-11-10 | Established patch `2.0.1` and coordinated security-policy patches `1.0.1` to make cross-suite standing and `RZN-001` consumption explicit without product-semantic change | User's explicit in-place reconciliation instruction recorded in `ARC-AUT-001`; predecessor preserved at Git commit `5f0c325` |

