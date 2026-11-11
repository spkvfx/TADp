# Web application bundle open questions and decisions

**Initiative:** `INIT-IMP-006`
**Status:** Proposed
**Last updated:** 2026-11-11

## Status vocabulary

`Open` means no human choice exists. Only explicit authority and required
receipts may change state.

## Decision register

| ID | Decision | State | Earliest blocker | Owner |
|---|---|---|---|---|
| `WEB-01` | Exact web/artifact/evidence paths | Open | Product placement | User |
| `WEB-02` | Framework and dependency locks | Open | Build/architecture | User |
| `WEB-03` | Web semantic/compatibility policy | Open | Public compatibility | User |
| `WEB-04` | Browser/OS/assistive-tech matrix | Open | Accessibility qualification | User |
| `WEB-05` | Source-map disposition | Open | Security/release | User |
| `WEB-06` | Accessibility/security/release owner | Open | Readiness/release | User |
| `WEB-07` | Design/help/accessibility split trigger | Open | Scope confirmation | User |

## Earliest blocking decisions

`WEB-07` blocks scope; `WEB-01` placement; `WEB-02`-`WEB-06` readiness.

## WEB-01 - Artifact placement

### Question

Which exact paths hold source, manifest, compiled assets, accessibility reports,
traces, and evidence?

### Why it matters

Traceability, embedding, ownership, and release identity require an exact map.

### Options and tradeoffs

A consolidated web subtree aids cohesion; separated build/evidence outputs need
strong manifest links.

### Default if unanswered

No destination is inferred.

### Decision needed from

User.

## WEB-02 - Framework and dependencies

### Question

Use a framework or no-framework approach, with which exact dependency locks?

### Why it matters

State, accessibility, CSP, asset size, support, and supply-chain obligations vary.

### Options and tradeoffs

A framework can speed accessible components/state handling but expands
dependencies; minimal code narrows supply chain but increases custom behavior.

### Default if unanswered

No build architecture is selected.

### Decision needed from

User.

## WEB-03 - Semantic compatibility

### Question

What web semantic version and compatibility policy applies apart from v4.0?

### Why it matters

Routes, assets, browser behavior, and D3 API use need controlled evolution.

### Options and tradeoffs

Strict compatibility protects deployment; faster change requires explicit
major transitions and cache/asset handling.

### Default if unanswered

No compatibility/release claim.

### Decision needed from

User.

## WEB-04 - Browser and assistive-tech matrix

### Question

Which browser, OS, screen-reader, high-contrast, zoom, and Safari combinations
are supported?

### Why it matters

Accessibility and interaction claims are matrix-specific.

### Options and tradeoffs

A narrow representative matrix lowers cost; broader coverage improves reach
but multiplies manual and automated evidence.

### Default if unanswered

No accessibility qualification claim.

### Decision needed from

User.

## WEB-05 - Source maps

### Question

Are source maps omitted, external/restricted, or shipped, and how is absence of
secrets, host paths, record data, and unsafe dependencies verified?

### Why it matters

Debug value trades against source/information disclosure.

### Options and tradeoffs

Omission minimizes disclosure; restricted maps aid diagnosis with retention and
access-control obligations.

### Default if unanswered

No releasable bundle claim.

### Decision needed from

User.

## WEB-06 - Review ownership

### Question

Who owns accessibility, security, risk, API compatibility, vulnerability,
license, and evidence review?

### Why it matters

Cross-disciplinary continuing duties require accountable humans.

### Options and tradeoffs

One owner simplifies disposition; specialists improve depth with handoffs.

### Default if unanswered

Readiness and release remain blocked.

### Decision needed from

User.

## WEB-07 - Split boundary

### Question

Do design-system, help, or accessibility assets require an independent initiative?

### Why it matters

Independent lifecycle/artifact evidence requires a split; convenience does not.

### Options and tradeoffs

Keep one bundle-centered D6 initiative unless evidence proves an independent
owner, artifact, lifecycle, or safety boundary.

### Default if unanswered

Retain one Proposed D6 initiative and do not deliver.

### Decision needed from

User.

## Decision dependencies

Scope precedes placement; placement/framework/policy precede build;
matrix/maps/ownership precede qualification.

## Decision process

Record explicit choices, rationale, alternatives, affected records, and
receipts; reconcile every coupled file together.
