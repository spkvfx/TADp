# Version-realization-suite-initiative correlation open questions and decisions

**Initiative:** INIT-DSN-001-version-realization-correlation

**Status:** Open

**Last updated:** 2026-11-10

This register separates unresolved legacy identity mappings from the
source-authorized invariant direction. Recommendations remain proposed until
the User's exact response is preserved in a decision receipt.

**Human ownership:** The [project ownership convention](../../../project-profile.md)
identifies the User as Sole Project Owner for these decisions.

## Status vocabulary

- Open, blocking: the exact accepted design cannot apply the affected mapping.
- Open: the ledger may preserve an explicit unresolved blocker without
  applying a mapping.
- Accepted YYYY-MM-DD: a receipt-backed decision governs this initiative.
- Deferred: no mapping is applied and the named re-entry condition is retained.
- Superseded by VRC-xx: a later receipt-backed decision replaces the entry.

## Decision register

| ID | Decision | Recommendation | Status | Blocks |
|---|---|---|---|---|
| VRC-01 | Disposition of requested legacy v4 and v4.1 identities relative to observed v4.0 | Preserve all source identities; apply no equivalence until the User identifies the intended mapping or missing source | Open, blocking | Final v4 migration-ledger disposition and exact accepted migration baseline |
| VRC-02 | Disposition of requested legacy v3 and v3.1 identities relative to observed v3.0 | Preserve requested and observed identities separately; defer mapping to a migration-specific decision if no source exists | Open | Any future v3 tuple migration; not the core invariant wording |

## Earliest blocking decisions

1. VRC-01 — the User requires the v4 case to be resolved, while the captured
   repository lacks the named v4 path and v4.1 source.
2. VRC-02 — early disposition avoids implying that v3.1 existed or that v3 and
   v3.0 are automatically identical.

## VRC-01 - v4/v4.1 source identity and mapping

**Question:** The captured repository contains
example/evidence/non-authoritative/realizations/v4.0/00-RZN-001-P4-WEB-suite-index.md,
introduced directly as v4.0 in commit 80c0ee0, and reachable history contains
no tracked v4 path or v4.1 reference. Your instruction instead names the
legacy v4 path and requires resolution of a v4 versus v4.1 dot-scope
relationship. Which exact disposition should govern this migration ledger?

**Context and evidence:** The observed v4.0 suite is non-authoritative and
describes one D6 browser-bundle boundary. The user instruction is authority to
revise this protocol, not evidence of the missing file contents. A
meaning-changing mapping may not be invented.

**Options:**

1. Decide that requested v4 is a notation-only identity for the observed v4.0
   suite, while requested v4.1 is a distinct unresolved identity that must be
   preserved until its source and narrow outcome are supplied.
2. Decide that requested v4 and v4.1 are distinct historical identities and
   neither maps to observed v4.0; keep all three as separate ledger rows until
   project-specific migration evidence resolves them.
3. Provide or identify the missing v4/v4.1 source or state a different exact
   mapping, including which identity owns the D6 browser-bundle outcome.

**Recommendation:** Option 2 unless the User can identify the missing source.
It preserves every stated identity and avoids converting an absent source into
a notation-only claim.

**Decision:** Open.

**Rationale:** To be recorded from the exact human response.

**Owner:** User

**Decision date:** -

**Acceptance:** The receipt must identify each of v4, v4.0, and v4.1; state
whether any relationship is notation-only or meaning-changing; preserve the
non-authoritative standing; and define the ledger action without creating an
initiative or lifecycle claim.

**Affected documents:** assumption.md, architecture.md, source-mapping.md,
scope-assessment.md, implementation-roadmap.md, implementation-steps.md,
the planned legacy migration ledger, suite/index/status tracking, and the
accepted-baseline presentation.

## VRC-02 - v3/v3.1 source identity and mapping

**Question:** The captured repository contains only the v3.0 CLI realization
suite, introduced directly at commit 80c0ee0, while the required inventory
names v3 and v3.1. Which disposition should the ledger retain?

**Context and evidence:** The observed v3.0 suite is non-authoritative and owns
one intended D5 CLI boundary. No tracked v3 path or v3.1 reference was found.
The protocol can preserve unresolved identities without applying a migration.

**Options:**

1. Decide that requested v3 is a notation-only identity for observed v3.0 and
   keep v3.1 as a separate unresolved identity.
2. Keep requested v3, observed v3.0, and requested v3.1 as separate ledger
   identities with a blocker and no mapping.
3. Provide or identify the missing source or state a different exact mapping.

**Recommendation:** Option 2. It completes the inventory without asserting a
meaning not supported by repository evidence.

**Decision:** Open.

**Rationale:** To be recorded from the exact human response if the mapping is
to be applied; otherwise record a receipt-backed deferral or retain the
explicit blocker.

**Owner:** User

**Decision date:** -

**Acceptance:** The ledger states the observed and requested identities,
source availability, chosen action, evidence standing, and future re-entry
condition without inventing an initiative or lifecycle claim.

**Affected documents:** architecture.md, source-mapping.md, the planned legacy
migration ledger, and any future v3 migration initiative.

## Decision dependencies

| Decision | Depends on | Unblocks |
|---|---|---|
| VRC-01 | Captured v4.0 source, Git history, and User clarification | Final v4 ledger action and exact migration baseline |
| VRC-02 | Captured v3.0 source, Git history, and User clarification if mapping is desired | Future v3 mapping; ledger may otherwise retain an explicit blocker |

## Decision process

1. Preserve the exact question, evidence, options, recommendation, and response.
2. Create one decision receipt before changing this register.
3. Reconcile only the records affected by that response.
4. Do not treat a mapping decision as initiative acceptance, delivery,
   implementation, completion, or release evidence.
