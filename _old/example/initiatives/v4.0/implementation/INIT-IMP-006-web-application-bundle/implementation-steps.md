# Web application bundle delivery steps

**Initiative:** `INIT-IMP-006`
**Status:** Proposed planning only
**Last updated:** 2026-11-11

## Current-state analysis

Contracts and notes exist; governed web source/bundle and D6 evidence do not.

## Delivery strategy

Build state/accessibility core, immutable same-origin integration, browser and
security evidence, then qualify one exact bundle after later authority.

## Step 1 - Establish source and asset graph

### Objective

Create authorized D6 structure and reproducible locked build.

### Expected output locations

Open under `WEB-01`.

### Planned output

Source skeleton, locked toolchain, manifest, asset pipeline, evidence identity.

### Dependencies

`WEB-01`, `WEB-02`, `WEB-07` and exact D2/D3 interfaces.

### Evidence / authoritative

Web boundary/contract, ADR-007, conformance, security suites.

### Migration and rollback

No data migration; immutable manifest enables bundle fallback/cache control.

### Verification

Reproducible build, asset/manifest inspection, provenance, scans, no remote asset.

### Acceptance

Later review only.

## Step 2 - Implement workflows state and accessibility

### Objective

Implement record/search/navigation/edit/delete/help and accessible state model.

### Expected output locations

Authorized D6 paths.

### Planned output

Views/components, API adapter, validation, pending/race/cancel/retry/stale/
conflict/indeterminate states, focus/status/help behavior.

### Dependencies

Step 1, `WEB-03`, `WEB-04`.

### Evidence / authoritative

Web/API contracts and WEB-001..WEB-010.

### Migration and rollback

Public state/route changes obey semantic policy; no durable record migration.

### Verification

Unit/property/component, keyboard/focus/semantics/status/contrast/zoom,
race/conflict/cancel/indeterminate tests.

### Acceptance

Exact interaction/accessibility outcomes pass for candidate bundle.

## Step 3 - Integrate and prove browser/security envelope

### Objective

Embed same-origin assets and verify supported browser/API/security behavior.

### Expected output locations

Authorized compiled/report/trace/evidence paths.

### Planned output

D3 static integration, browser/AT matrix, CSP/DOM/storage/map/dependency checks,
network fault/E2E results, safe telemetry.

### Dependencies

Step 2 and `WEB-04`-`WEB-06`.

### Evidence / authoritative

Web/operations/conformance contracts and security/data policies.

### Migration and rollback

Define compatible D3 pairing, cache invalidation, previous bundle fallback.

### Verification

WEB-011..WEB-013, browser/Safari, AT, high contrast, CSP, same-origin, storage,
source-map, leak, dependency, and fault tests.

### Acceptance

No critical accessibility/security issue or unsupported compatibility claim.

## Step 4 - Qualify D6 outcome

### Objective

Produce artifact-bound D6 conformance record.

### Expected output locations

Authorized product/evidence records.

### Planned output

Manifest, matrix, accessibility/security/risk/license review, release
disposition, source-map record, human review packet.

### Dependencies

Steps 1-3 and all blocking decisions.

### Evidence / authoritative

Conformance contract and source mapping.

### Migration and rollback

Record fallback/cache/API compatibility and evidence invalidation.

### Verification

Clean install, workflow/state, accessibility, browser, security, fault, E2E matrix.

### Acceptance

Only later explicit human authority advances lifecycle or accepts product.

## Validation matrix

| Area | Required evidence | Blocking gap |
|---|---|---|
| Workflows/state | WEB-001..WEB-006 | Race/conflict/indeterminate gap |
| Accessibility/help | WEB-007..WEB-010 and manual/automated AT | Keyboard/focus/status/contrast gap |
| Artifact/integration | WEB-011..WEB-013, manifest/same-origin | Remote/cross-origin/mutable asset |
| Browser compatibility | browser/OS/AT/Safari matrix | Unsupported combination |
| Security/data | CSP/DOM/storage/map/dependency/leak review | Secret/content/ePHI/source risk |
| Boundary | D6 manifest | Reliance on predecessor or D5 completion |

## Final acceptance criteria

Binding outcomes map to passing bundle-specific evidence; decisions/products
have authority; no D2/D3/D5 completion is inferred. Planning only.
