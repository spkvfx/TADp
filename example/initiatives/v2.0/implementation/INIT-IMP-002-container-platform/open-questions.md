# Container platform and runtime packaging open questions and decisions

**Initiative:** Container platform and runtime packaging
**Status:** Open
**Last updated:** 2026-11-11

No recommendation below is an answer.

**Human ownership:** The [project ownership convention](../../../../project-profile.md)
assigns human decisions to the User while preserving technical responsibilities.

## Status vocabulary

Open entries require explicit human review. `Open, blocking` prevents the
affected work. A later disposition requires a decision receipt and coupled
record reconciliation.

## Decision register

| ID | Decision | Recommendation | Status | Blocks |
|---|---|---|---|---|
| `PLT-01` | Artifact placement | Prefer one root product family whose ownership and generated outputs are explicit. | Open, blocking | Acceptance and product execution |
| `PLT-02` | Supported toolchain matrix | Select the narrowest reproducible matrix that covers the architecture-required hosts and native OCI targets. | Open, blocking | Acceptance and product execution |
| `PLT-03` | Provenance trust | Choose one authenticated, documented mechanism and keep signatures as evidence rather than proof by assertion. | Open, blocking | Acceptance and product execution |
| `PLT-04` | Evidence environments | Use declared external runners/hosts without making them application runtime dependencies. | Open | Qualification or release |
| `PLT-05` | Evidence retention | Use a content-addressed project evidence destination that excludes prohibited data. | Open | Qualification or release |
| `PLT-06` | D2 split boundary | Keep one D2 initiative only if the complete scope remains one platform artifact family and gate. | Open | Qualification or release |

## Earliest blocking decisions

1. `PLT-01` fixes owned product paths.
2. `PLT-02` and `PLT-03` fix the reproducible matrix and release trust before execution.

## PLT-01 - Artifact placement

**Question:** Which exact repository paths own the D2 build graph, Compose material, locks, and release metadata?

**Context and evidence:** The platform realization records this choice as
unresolved; architecture fixes the boundary and expected outcomes but not this
implementation selection.

**Options:**

1. Adopt the recommended narrow direction and record exact identities.
2. Select a compatible alternative with equivalent boundary and evidence.
3. Defer or split the affected outcome before product work.

**Recommendation:** Prefer one root product family whose ownership and generated outputs are explicit.

**Decision:** Open.

**Rationale:** To be recorded when accepted.

**Owner:** User

**Decision date:** -

**Acceptance:** Record exact products, owners, compatibility, failure behavior,
verification, and any split consequence.

**Affected documents:** `assumption.md`, `architecture.md`,
`source-mapping.md`, `implementation-roadmap.md`, and
`implementation-steps.md`.

## PLT-02 - Supported toolchain matrix

**Question:** Which Docker, Compose, BuildKit, registry, host, and OCI-platform versions form the first supported matrix?

**Context and evidence:** The platform realization records this choice as
unresolved; architecture fixes the boundary and expected outcomes but not this
implementation selection.

**Options:**

1. Adopt the recommended narrow direction and record exact identities.
2. Select a compatible alternative with equivalent boundary and evidence.
3. Defer or split the affected outcome before product work.

**Recommendation:** Select the narrowest reproducible matrix that covers the architecture-required hosts and native OCI targets.

**Decision:** Open.

**Rationale:** To be recorded when accepted.

**Owner:** User

**Decision date:** -

**Acceptance:** Record exact products, owners, compatibility, failure behavior,
verification, and any split consequence.

**Affected documents:** `assumption.md`, `architecture.md`,
`source-mapping.md`, `implementation-roadmap.md`, and
`implementation-steps.md`.

## PLT-03 - Provenance trust

**Question:** Which provenance/signature mechanism and trust root govern release verification?

**Context and evidence:** The platform realization records this choice as
unresolved; architecture fixes the boundary and expected outcomes but not this
implementation selection.

**Options:**

1. Adopt the recommended narrow direction and record exact identities.
2. Select a compatible alternative with equivalent boundary and evidence.
3. Defer or split the affected outcome before product work.

**Recommendation:** Choose one authenticated, documented mechanism and keep signatures as evidence rather than proof by assertion.

**Decision:** Open.

**Rationale:** To be recorded when accepted.

**Owner:** User

**Decision date:** -

**Acceptance:** Record exact products, owners, compatibility, failure behavior,
verification, and any split consequence.

**Affected documents:** `assumption.md`, `architecture.md`,
`source-mapping.md`, `implementation-roadmap.md`, and
`implementation-steps.md`.

## PLT-04 - Evidence environments

**Question:** How are native amd64/arm64 and Windows, Linux, macOS, and browser evidence environments provisioned?

**Context and evidence:** The platform realization records this choice as
unresolved; architecture fixes the boundary and expected outcomes but not this
implementation selection.

**Options:**

1. Adopt the recommended narrow direction and record exact identities.
2. Select a compatible alternative with equivalent boundary and evidence.
3. Defer or split the affected outcome before product work.

**Recommendation:** Use declared external runners/hosts without making them application runtime dependencies.

**Decision:** Open.

**Rationale:** To be recorded when accepted.

**Owner:** User

**Decision date:** -

**Acceptance:** Record exact products, owners, compatibility, failure behavior,
verification, and any split consequence.

**Affected documents:** `assumption.md`, `architecture.md`,
`source-mapping.md`, `implementation-roadmap.md`, and
`implementation-steps.md`.

## PLT-05 - Evidence retention

**Question:** Where are SBOMs, provenance, findings, machine-readable results, and review dispositions retained?

**Context and evidence:** The platform realization records this choice as
unresolved; architecture fixes the boundary and expected outcomes but not this
implementation selection.

**Options:**

1. Adopt the recommended narrow direction and record exact identities.
2. Select a compatible alternative with equivalent boundary and evidence.
3. Defer or split the affected outcome before product work.

**Recommendation:** Use a content-addressed project evidence destination that excludes prohibited data.

**Decision:** Open.

**Rationale:** To be recorded when accepted.

**Owner:** User

**Decision date:** -

**Acceptance:** Record exact products, owners, compatibility, failure behavior,
verification, and any split consequence.

**Affected documents:** `assumption.md`, `architecture.md`,
`source-mapping.md`, `implementation-roadmap.md`, and
`implementation-steps.md`.

## PLT-06 - D2 split boundary

**Question:** Does any platform sub-scope have an independent owner, lifecycle, destination, or acceptance claim requiring another tuple?

**Context and evidence:** The platform realization records this choice as
unresolved; architecture fixes the boundary and expected outcomes but not this
implementation selection.

**Options:**

1. Adopt the recommended narrow direction and record exact identities.
2. Select a compatible alternative with equivalent boundary and evidence.
3. Defer or split the affected outcome before product work.

**Recommendation:** Keep one D2 initiative only if the complete scope remains one platform artifact family and gate.

**Decision:** Open.

**Rationale:** To be recorded when accepted.

**Owner:** User

**Decision date:** -

**Acceptance:** Record exact products, owners, compatibility, failure behavior,
verification, and any split consequence.

**Affected documents:** `assumption.md`, `architecture.md`,
`source-mapping.md`, `implementation-roadmap.md`, and
`implementation-steps.md`.

## Decision dependencies

| Decision | Depends on | Unblocks |
|---|---|---|
| `PLT-01` | None | Product placement and structure |
| `PLT-02` | `PLT-01` product graph | Build/test matrix |
| `PLT-03` | `PLT-02` tools/registry | Release provenance gate |
| `PLT-04` | `PLT-02` matrix | Qualification environments |
| `PLT-05` | `PLT-03`, `PLT-04` evidence forms | Retention and review |
| `PLT-06` | `PLT-01`–`PLT-05` | Final scope acceptance or split |

## Decision process

Confirm evidence and owner boundaries; compare options against scope,
compatibility, failure, and policy; record exact human answer/receipt; reconcile
all affected records; link verification when first exercised.
