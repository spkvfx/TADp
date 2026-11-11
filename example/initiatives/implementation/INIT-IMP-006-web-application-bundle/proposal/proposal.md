# Web application bundle proposal

**Initiative:** Web application bundle

**Proposal status:** Draft

**Revision:** 0.1

**Last updated:** 2026-11-11

**Owner:** User

**Initiative type:** `implementation`

**Work version:** `v4.0`

**Realization suite:** [`RZN-001-P4-WEB-SUITE`](../../../../evidence/non-authoritative/realizations/v4.0/00-RZN-001-P4-WEB-suite-index.md)

**Type requirements:** See [the initiative skeleton](../README.md).

## Executive proposal

Create one container-built web bundle embedded and served same-origin by the D3
API image. The D6 application provides accessible record workflows, explicit
loading/empty/error/conflict/indeterminate states, safe browser behavior, and
no separate web server, host Node prerequisite, durable browser record
storage, third-party/remote assets, or cross-origin API. Paths, framework,
versions, matrices, source maps, owners, and split choices remain open.

## Initiative type and permitted output

This implementation initiative may eventually deliver web source, manifest,
compiled immutable assets, accessibility/security evidence, traces, and D6
verification. It cannot deliver D2/D3 or D5 outcomes.

## Problem and evidence

Authoritative web contracts exist but the example has no governed D6 bundle.
The v4.0 realization suite is planning evidence only and cannot prove
implementation, accessibility, security, acceptance, or conformance.

## Intended outcomes

- One same-origin bundle served through D3’s static-hosting boundary.
- Accessible keyboard, focus, semantics, status, contrast, and assistive-tech behavior.
- Complete record/search/navigation/edit/delete/conflict workflows.
- Explicit loading, empty, error, retry, cancellation, stale, and indeterminate states.
- WEB-001 through WEB-013 plus applicable contract/security/accessibility evidence.

## Scope

### Included

Browser state and interaction, accessible UI, same-origin API use, immutable
asset build, help, compatibility, source-map disposition, security,
accessibility, and D6 verification.

### Excluded

Separate web server/container, host Node runtime, durable browser record store,
third-party/remote assets, cross-origin API, D2/D3/D5 delivery, production or
regulated use, actual or possible ePHI, and unresolved implementation choices.

## Users and stakeholders

Local keyboard, pointer, screen-reader, zoom, contrast, and automation users
interact with D6. Owners/reviewers govern lifecycle, design, accessibility,
security, API compatibility, dependencies, and evidence.

## Terms

- **D6:** the web bundle artifact family from ADR-007.
- **Same-origin:** assets and API share D3’s origin and trust boundary.
- **Indeterminate:** completion cannot safely be inferred after interruption.
- **Durable browser storage:** record-bearing persistence such as IndexedDB or
  localStorage, prohibited for application data.

## Proposed direction

### Product behavior or placement

Build one immutable bundle into D3’s declared static slot. Exact source,
manifest, assets, reports, traces, and evidence paths stay open under `WEB-01`.

### Domain and authority model

Render authoritative domain/API semantics without inventing server truth.
Client state tracks editing, pending, stale, conflict, error, and indeterminate
conditions explicitly.

### System boundaries

Build inside D2; run in supported browsers; call same-origin D3 only; use no
separate server, cross-origin endpoint, remote asset, or durable record storage.

### Primary workflows

Load/list/search/navigate records; create/edit/delete with validation and
conflict handling; cancel/retry; recover focus/state; use help; communicate all
states accessibly.

### Data and lifecycle

Keep record data in memory for the active session only. Browser preferences may
be stored only if non-record, non-secret, and authorized. Evidence uses
synthetic or documented de-identified data.

## Operational behavior

### Failure and recovery

Network loss, timeout, cancellation, stale response, conflict, validation
failure, unavailable API, asset failure, navigation race, interrupted write,
and indeterminate outcome require safe accessible recovery.

### Security and authorization

Use same-origin policy, CSP and safe DOM practices, dependency locks/scans,
no remote assets or unsafe persistence, redacted telemetry, and local
single-user non-production constraints.

### Observability

Capture safe client errors, accessibility results, performance/interaction
traces, and E2E artifacts without record content, secrets, host paths, or unsafe
source-map disclosure.

## Compatibility and transition

D6 depends on exact D2/D3 artifacts. D5 provides sequencing context only and is
independent. Web semantic versioning and browser/assistive-tech matrices must be
explicit and artifact-bound.

## Alternatives considered

Separate server, cross-origin SPA, remote CDN assets, host-built bundle, and
durable offline record store conflict with boundaries. Multiple D6 initiatives
are not justified; `WEB-07` keeps split triggers open.

## Risks and tradeoffs

Risks include inaccessible focus/status, race and stale-state bugs, unsafe DOM,
source-map leakage, remote dependencies, client persistence, browser drift,
poor conflict/indeterminate handling, and API compatibility overclaims.

## Assumptions requiring assumption

Initial assumptions cover one embedded D6 bundle, same-origin D3 use, no
separate server/storage/remote assets, inclusive accessibility, safe data use,
and blocking evidence gaps. Stage 3 records them as unconfirmed.

## Questions requiring decisions

- `WEB-01`: exact source, manifest, compiled asset, report, trace, evidence paths.
- `WEB-02`: framework/no-framework and dependency patch locks.
- `WEB-03`: web semantic version and compatibility policy.
- `WEB-04`: browser/OS/screen-reader/high-contrast/Safari matrix.
- `WEB-05`: source-map disposition and disclosure verification.
- `WEB-06`: accessibility/security/risk/API/vulnerability/license/evidence owner.
- `WEB-07`: design-system/help/accessibility split trigger.

All remain open.

## Acceptance outcomes

A later human review may assess whether D6 is narrow, accessible, secure,
traceable, and testable. Accessibility pass, artifact acceptance, conformance,
and release require later authority and evidence.

## References

- [Architecture suite](../../../../evidence/authoritative/architecture/00-architecture-suite-index.md)
- [ADR-007](../../../../evidence/authoritative/architecture/10-ADR-007-product-and-delivery-decomposition.md)
- [Web boundary](../../../../evidence/authoritative/architecture/21-web-application-boundary.md)
- [Web contract](../../../../evidence/authoritative/architecture/22-web-interaction-contract.md)
- [Operations/security](../../../../evidence/authoritative/architecture/23-operations-security-contract.md)
- [Conformance](../../../../evidence/authoritative/architecture/24-conformance-contract.md)
- [NIST suite](../../../../evidence/authoritative/security/NIST/00-nist-security-policy-suite-index.md)
- [HIPAA-aligned suite](../../../../evidence/authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md)
- [v4.0 suite](../../../../evidence/non-authoritative/realizations/v4.0/00-RZN-001-P4-WEB-suite-index.md)

## Revision history

| Revision | Date | Change | Authority |
|---|---|---|---|
| 0.1 | 2026-11-11 | Initial D6 proposal; all implementation choices remain open | User prompt and cited evidence |
