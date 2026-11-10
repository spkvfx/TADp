# Product and delivery decomposition

**Decision ID:** `ADR-007`  
**Status:** Accepted  
**Architecture revision:** `2.0.1`  
**Decision owner:** User, project authority  
**Decision date:** 2026-11-10  
**Supersedes / superseded by:** Not applicable  
**Related initiative:** Not applicable - future initiatives must apply this decision  

## Decision question

How must the requested documentation, container platform, API, SDK, CLI, and
web outputs be decomposed and dependency-ordered for delivery/verification?

## Context and binding evidence

| Source | Precise claim or constraint | Effect on this decision |
|---|---|---|
| [`AUTH-EX-001.7`](01-accepted-architecture-baseline.md) | Outputs are distinct independently verifiable delivery units | Prohibits one undifferentiated completion claim |
| [`AUTH-EX-001.11`](01-accepted-architecture-baseline.md) | Compose-only runtime and no host application toolchain | Adds an independently verifiable container-platform output |
| [`RZN-001`](../../non-authoritative/realizations/v0.0/RZN-001-example-record-application.md), candidate product sequence and Q17 | Requests docs, SDK/API, CLI, web in order; SDK/API cohesion unresolved | Supplies dependency intent, not initiative authority |
| [Initiative scope specification](../LLM/06_Codex_Initiative_Scope_Specification.md) | Different outputs/verification/lifecycles trigger separate scopes | Requires narrow future initiatives |

## Decision

The architecture recognizes six independently reviewable delivery units:

| Unit | Accepted output boundary | Required predecessor evidence | Independent completion claim |
|---|---|---|---|
| `D1 Architecture and contract documentation` | This suite plus approved derivative developer/user contract docs | User architecture authority and source traceability | Specification completeness/coherence only; no product behavior claim |
| `D2 Container platform and runtime packaging` | Multi-stage Dockerfile, `.dockerignore`, Compose services/profiles/network/volumes/security/health, build/test targets, release digest/provenance/SBOM flow | Accepted D1 revision | Clean-host Compose-only build/run/test/maintenance and topology conformance; no API/domain completion claim |
| `D3 API and SQLite runtime image` | Executable `/api/v1`, migrations, SQLite adapter, health/static hosting, API OCI image and operations behavior | Accepted D1, compatible D2 platform | API/persistence/image conformance; no SDK/CLI/web completion claim |
| `D4 Python SDK artifact` | Independently versioned wheel plus containerized build/test/developer consumption path | Accepted D1/D2 plus contract-testable D3 API | SDK public API/wheel/live conformance; no host-install or CLI completion claim |
| `D5 Standalone CLI image` | Independently versioned OCI image/entrypoint using the exact D4 wheel | Accepted D1-D4 compatible revisions | Compose command/output/exit/live parity; no web completion claim |
| `D6 Web application bundle` | Accessible browser assets built in containers and embedded/versioned in D3 API image | Accepted D1-D3; delivery follows D5 per requested sequence | UI/accessibility/browser/bundle/end-to-end conformance |

`D3` and `D4` replace the realization's combined SDK/API candidate as two
architectural components and separately verifiable outcomes. `D2` is added by
the User's Docker-only invariant and owns cross-product container infrastructure
without absorbing API/SDK/CLI/web completion claims. Future initiative
preparation must normally create separately scoped initiatives for each of
`D1`-`D6`. A human authority may accept another boundary only after an explicit
scope assessment demonstrates that no mandatory split trigger applies; shared
timing or a "Product 2" label is not sufficient.

The dependency/delivery order is:

```text
D1 contracts
    -> D2 container platform
        -> D3 API + SQLite image
            -> D4 Python SDK artifact
                -> D5 CLI image
        -> (after D5 sequencing gate) D6 web bundle in API image
```

The web does not technically depend on CLI code, but its delivery follows the
requested sequence so CLI proves the API/SDK capabilities before the final UI.
A future explicit human instruction may revise that sequencing gate without
changing the web's technical dependency on D2/D3.

Each unit owns its own proposal, scope assessment, acceptance, branch,
delivery path, verification, completion evidence, release disposition, and
compatibility claim. A coordinating view may aggregate status but cannot
accept or complete all units through one umbrella claim.

## Consequences

### Benefits

- SDK and API can fail, change, or release independently without obscuring
  status.
- Compose/image infrastructure can be verified and changed without claiming
  API/domain delivery, while all products reuse one governed platform.
- Contract-first intent remains visible and testable at every handoff.
- CLI validates the public SDK rather than an internal API package.
- Web delivery consumes a proven API while retaining its own accessibility and
  browser acceptance.
- Implementation feedback can return to the owning specification without
  rewriting completed claims.

### Costs, risks, and required follow-up

- More than one initiative/branch/acceptance/completion record is required.
- Cross-unit contract fixtures and compatibility matrices need explicit owners.
- D4 may start against a contract test double but cannot claim live
  conformance until a compatible D3 baseline exists.
- D6 sequencing after D5 can delay web work despite no code dependency; this
  preserves the User-requested product order until revised.
- D2 is cross-cutting infrastructure but must remain narrow: it owns the
  reusable Compose/build/security contract, not product behavior.
- A defect spanning units must be routed to its owning contract/product rather
  than patched in every consumer.

## Alternatives considered

| Alternative | Why it was not selected | Reconsideration trigger |
|---|---|---|
| One initiative for all products | Independent outputs, owners, verification, and completion violate narrow-scope rules | Never without explicit invariant-compatible scope authority |
| Combined API+SDK initiative | They are independently packaged, consumed, blocked, and verifiable | Human-approved scope assessment proving one inseparable claim for a specific revision |
| Hide Compose/Docker work inside API initiative | Platform graph/build/test/maintenance is reused by multiple products and has its own clean-host/security claim | A scope assessment proves the infrastructure is truly inseparable for one revision |
| CLI embeds internal API/domain code | Breaks SDK/API boundary and hides public conformance | A replacement embedded/offline architecture |
| Build web before CLI | Conflicts with requested delivery sequence | Explicit User revision of sequencing priority |
| Treat this suite as D1 completion | Architecture creation does not supply an initiative delivery/completion record | A governed D1 initiative may cite/adopt this existing authority and verify its accepted claim |

## Acceptance and verification

| Required result | How it is verified | Evidence location |
|---|---|---|
| Future work uses narrow unit ownership | Initiative scope assessments and index review | Future initiative records |
| Each handoff names exact architecture, Compose, image, API, SDK, schema, and bundle revisions/digests | Source mappings and product metadata | Future D2-D6 records |
| No unit claims another unit's completion | Lifecycle/completion evidence audit | Future portfolio records |
| Cross-unit behavior remains identical | Conformance matrix | [`ARC-CTR-009`](24-conformance-contract.md) |

## Revision record

| Date | Change | Authority |
|---|---|---|
| 2026-11-10 | Accepted five delivery units, split API/SDK, and dependency/sequence order | User-authorized best-judgment architecture method recorded in `ARC-AUT-001` |
| 2026-11-10 | Added independent container-platform unit, made API/CLI/web outputs container artifacts, and revised dependencies to six units | User's explicit Dockerization/no-host-services instruction; predecessor in `ARC-REV-001` |

