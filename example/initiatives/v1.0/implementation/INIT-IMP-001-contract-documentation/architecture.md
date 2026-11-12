# Contract documentation architecture and specification

**Initiative:** Contract documentation  
**Status:** Proposed  
**Last updated:** 2026-11-11

Related documents: [initiative](README.md), [proposal sources](proposal/README.md),
[assumptions](assumption.md), [evidence mapping](source-mapping.md), [open
questions](open-questions.md), [roadmap](implementation-roadmap.md), and
[delivery steps](implementation-steps.md).

## Proposal standing

The proposal and realization note are non-authoritative inputs. This Proposed
specification applies binding architecture and security evidence without
accepting any `DOC-*` decision or assumption. Product execution cannot begin
until the initiative is separately accepted and the blocking choices are
resolved.

## Specification boundary

This implementation specification defines derivative documentation product
behavior. It does not revise the architecture/security specifications it
explains. A mismatch blocks the derivative and routes to the owning authority.

## Current repository baseline

| Area | Current contract or evidence | Consequence for this initiative |
|---|---|---|
| Technical authority | `ARC-SUITE-001@2.0.1`, including records `00`–`24` | Every technical statement needs a precise source identity |
| Security/use | NIST and HIPAA suites `1.0.1` | Security claims, allowed data, inherited controls, and successor triggers must stay distinct and complete |
| D1 gate | `ARC-CTR-009`, D1 | Structural documentation checks are required but do not prove D2–D6 products |
| Product placement | No destination is selected | `DOC-01` blocks product creation |

## Goals and non-goals

### Goals

1. Provide one reviewable source-to-document navigation and explanation set.
2. Preserve exact contract identity, limitations, and prospective evidence
   language at every relevant entry point.
3. Qualify documentation structure, semantics, accessibility/usability, safe
   examples, and revision traceability.

### Non-goals

- Implement or verify any D2–D6 executable behavior.
- Change authoritative evidence, choose a regulated-use design, or claim NIST
  certification, HIPAA compliance, release readiness, or ePHI suitability.

## Terms and identity

| Term or identity | Definition | Authority or lifecycle |
|---|---|---|
| Documentation revision | Immutable identity of one reviewed derivative set | Selected by `DOC-04`; never substitutes for source revisions |
| Normative source locator | Exact suite/revision/record/section or policy/vector ID | Owned by authoritative evidence |
| Derivative claim | Product prose or diagram paraphrasing a source | Owned by D1 product and blocked on source mismatch |
| Observed claim | Statement about an exact product/artifact/environment result | Permitted only with exact later evidence |
| Example fixture | Purpose-created synthetic content with recorded provenance | Governed by NIST/HIPAA data rules |

Stable identity is created by the chosen documentation release process. Source
locators and artifact hashes reject stale or substituted input; no duplicate
documentation revision may describe different source identities.

## Architectural decisions

| Decision ID | Direction used by this design | Status |
|---|---|---|
| `DOC-01` | Select the product destination before writing output | Open, blocking |
| `DOC-02` | Keep only audience areas that share one acceptance claim | Open, blocking |
| `DOC-03` | Separate authored and generated derivatives and drift-check both | Open, blocking |
| `DOC-04` | Bind a documentation revision to exact source/product identities | Open |
| `DOC-05` | Select a documentation-specific accessibility/usability review | Open |
| `DOC-06` | Assign source-currency, disclaimer, and review responsibilities | Open |

Recommendations and alternatives remain in `open-questions.md`; no direction
in this table is accepted.

## Boundaries and ownership

| Component or package | Responsibility | Authoritative state | Must not own |
|---|---|---|---|
| Derivative set | Navigation, explanation, examples, and source links | Versioned documentation product | Architecture, security policy, or runtime truth |
| Source map | Connect each normative claim to exact authority | Reviewed mapping in the product/evidence record | Independent normative meaning |
| Generated appendix | Present observed schemas/help/metadata when exact artifacts exist | Content-addressed derivative | Contract changes or unqualified results |
| Review pipeline | Structure, links, drift, examples, claim language, and selected accessibility/usability checks | Evidence for exact documentation revision | Runtime conformance |

All external or generated content is validated against exact source identity
before publication. The derivative depends on authority; authority never
depends on the derivative.

## Domain model and evidence/authoritative

### Model

A documentation set contains entry points, audience guides, normative source
locators, derivative explanations, examples, compatibility statements, and
review evidence. Each normative statement maps to one or more exact source
owners. Examples are explicitly non-normative. Planned vectors are labelled
prospective; observed results identify exact artifacts and limitations.

### Binding requirements

- Preserve architecture `2.0.1` contracts, D1–D6 separation, and `ADR-006`
  successor/change discipline.
- Preserve every applicable `SEC-POL-*` and `HSP-*` limitation, including
  synthetic/documented-de-identified-only use and `HSP-015` triggers.
- Meet the D1 gate without converting structural review into implementation or
  security conformance evidence.

## State and persistence

| State | Durable source | Live or derived state | Write owner | Recovery rule |
|---|---|---|---|---|
| Normative meaning | Accepted authoritative records | Linked/paraphrased views | Source owner only | Revert derivative and route source issue; never edit authority here |
| Documentation content | Selected product destination | Rendered navigation/site/output | D1 product work after acceptance | Restore last reviewed revision or issue corrected successor |
| Generated derivative | Exact named product artifact | Rendered appendix | Generation/review pipeline | Regenerate only from same identity or invalidate review |
| Review evidence | Initiative/product evidence destination selected later | Reports and summaries | Evidence owner under `DOC-06` | Preserve prior result; rerun for changed revision |

No database or product runtime state is created. Concurrency is ordinary Git
change control; duplicate or stale revisions are rejected by source/revision
identity. Retention follows project and any future accepted product rule.

## Primary workflows

### Author and qualify a documentation revision

**Preconditions:** Blocking `DOC-*` decisions and assumptions are reviewed;
the initiative is accepted; exact source revisions are captured.

1. Inventory sources, claims, examples, audience entry points, and exclusions.
2. Author or generate content only at the accepted destination, preserving
   source locators and non-normative labels.
3. Run structure/link, semantic drift, safe-data, accessibility/usability, and
   claim-language review for the exact revision.

**Success result:** One traceable derivative revision meets the bounded D1
claim with review evidence.

**Failure result:** Publication is withheld; the product owner corrects the
derivative or routes a source conflict without weakening the expected result.

### Consume a source revision change

**Preconditions:** An authoritative successor or patch has a durable identity.

1. Classify the change under `ADR-006` and identify every affected derivative.
2. Update links/explanations/examples and preserve the predecessor revision.
3. Re-run all affected checks and publish only a newly identified derivative.

**Success result:** Compatibility and consumed-source identity are explicit.

**Failure result:** The prior derivative remains identifiable and the new
publication is blocked.

## Interfaces and integration

| Interface | Producer or caller | Consumer or handler | Compatibility rule |
|---|---|---|---|
| Repository links and source IDs | Authoritative suites | Documentation source map | Exact active revision/record/section; unresolved links block |
| Optional generated schemas/help/metadata | Future D2–D6 artifacts | Generated appendix | Exact artifact hash and observed label; accepted contracts win on conflict |
| Documentation entry points | D1 product | Readers and later initiatives | Repeat supported profile and version identity where context may be isolated |
| Review reports | Documentation checks/reviewers | Product and initiative evidence | Bound to exact revision, method, result, limitation, and reviewer |

Payload and tool choices remain open. Retrying a read-only check may not hide a
failure. Publication acknowledgement means only the documentation artifact was
created; acceptance requires the complete review gate.

## Failure and recovery

| Failure | Detection | Durable effect | Recovery | Required evidence |
|---|---|---|---|---|
| Broken/stale locator | Link and revision check | Candidate blocked | Correct link or wait for source disposition | Link/source report |
| Semantic drift | Human/automated comparison | Candidate blocked | Restore source-accurate text or route conflict | Claim-to-source review |
| Unsafe example or claim | Data/claim review | Candidate blocked; preserve finding | Replace with synthetic safe content and rerun | Fixture manifest and scan/review |
| Generated mismatch | Hash/drift check | Generated appendix invalid | Regenerate from exact input; do not rewrite source | Input/output hashes and diff |
| Accessibility/usability failure | Selected `DOC-05` method | Affected entry point blocked | Correct product and repeat review | Exact method and result |
| Publication interruption | Build/publish result | No success claim | Restore last reviewed revision or retry from immutable inputs | Product/release evidence |

## Security and authorization

- **Trust boundary:** Local project authors/reviewers; derivative publication
  introduces no application runtime trust.
- **Authentication:** Project/Git/publishing access is an inherited dependency,
  not an application control.
- **Authorization:** The User accepts decisions and lifecycle; source owners
  alone may change authoritative records.
- **Secrets:** None may enter content, examples, generated output, or evidence.
- **Audit:** Traceable Git/review evidence supports change history but is not a
  per-user HIPAA audit system.
- **Data handling:** Use purpose-created synthetic or externally documented
  de-identified data that also satisfies NIST restrictions; minimize and scan
  derivatives and evidence.

## Observability and operations

| Signal or operation | Purpose | Required dimensions or safeguards |
|---|---|---|
| Source/link check | Find missing or stale authority | Exact source revision; no content leakage |
| Coverage/claim review | Detect omission and overclaim | Claim ID, source locator, result, limitation |
| Accessibility/usability review | Prove documentation-specific access | Selected method, entry point, environment, reviewer |
| Revision diff | Classify source/product changes | Predecessor, successor, semantic classification |
| Publication rollback | Restore reviewed product | Exact prior revision; never alter authority |

Health, alerting, backup, and runtime repair are not applicable to this
documentation-only product unless `DOC-01` selects a publishing system that
requires separately governed operational controls.

## Compatibility migration and rollout

The initial product consumes the three accepted suite revisions named above.
Mixed documentation/source versions are not silently supported: entry points
declare the consumed revisions. A source successor is evaluated under
`ADR-006`, prior derivative revisions remain traceable, and rollback restores
only an earlier reviewed derivative. No product data migration applies.

## Testing strategy

| Level | Behavior proved | Required environment or fixture |
|---|---|---|
| Unit or domain | Terms, IDs, limits, and examples match precise sources | Purpose-created synthetic examples and source fixtures |
| Contract | Every normative claim and limitation maps to exact authority | Source/coverage map for captured revisions |
| Integration | Links, navigation, generated inputs, and selected publication output cohere | Destination/tooling chosen by `DOC-01`/`DOC-03` |
| Failure and recovery | Drift, unsafe data, missing links, and interrupted publication block safely | Mutated synthetic fixtures and prior reviewed revision |
| Acceptance | Readers can navigate one accurate, accessible, honest D1 product | Accepted audience set and `DOC-05` method |

## Risks and edge cases

| Risk or edge case | Impact | Mitigation or decision |
|---|---|---|
| One guide hides independent audiences | Umbrella scope | `DOC-02` and split review |
| Generated product differs from accepted contract | False authority | `DOC-03`, exact hashes, and source precedence |
| Source limitations appear only in one page | Unsafe isolated reading | Repeat concise profile at every relevant entry point |
| Planned vectors look like passes | False conformance | Explicit prospective/result vocabulary and claim review |
| Documentation version confused with suite/product version | Compatibility error | `DOC-04` identity model |

## Deferred work

- D2–D6 implementation and observed product documentation re-enter only under
  their own accepted initiatives and exact evidence.
- Any separate audience product, publishing service, or generated artifact
  with an independent claim re-enters through a new Stage 0 tuple.

## Architecture and specification acceptance

This Proposed specification is not accepted. It is ready for acceptance review
only after assumptions are explicitly reviewed, blocking `DOC-*` decisions are
accepted, the source map and destination agree, and every requirement maps to
a product step and documentation verification gate.
