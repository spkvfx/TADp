# Web application bundle architecture and specification

**Initiative:** `INIT-IMP-006`
**Status:** Proposed
**Last updated:** 2026-11-11

## Proposal standing

This specification elaborates frozen input without resolving choices or
changing source authority.

## Specification boundary

Specify one D6 bundle, browser state/interaction, accessibility, same-origin
integration, asset build, security, compatibility, and evidence—not D2/D3/D5.

## Current repository baseline

No governed web source or bundle exists at the captured base.

## Goals and non-goals

### Goals

- Complete accessible record/search/navigation/edit/delete workflows.
- Model loading, empty, error, stale, conflict, retry, and indeterminate states.
- Build immutable same-origin assets inside the container toolchain.
- Produce WEB-001..WEB-013 and browser/accessibility/security evidence.

### Non-goals

- Select paths, framework, versions, matrix, maps, owner, or split.
- Add separate server, host runtime, durable record store, remote asset, or CORS.
- Claim production, regulated, or predecessor/CLI readiness.

## Terms and identity

Bundle/manifest/asset hash, route/view, focus target, live region, request
generation, pending edit, conflict, indeterminate state, browser/matrix entry,
and evidence record require stable identity.

## Architectural decisions

No local decision is final. Authoritative contracts bind behavior; `WEB-01`
through `WEB-07` retain open implementation choices.

## Boundaries and ownership

D6 owns browser UI/state, accessibility, same-origin API adapter, asset build,
help, safe client diagnostics, and D6 evidence. D3 owns API/static serving; D2
owns build/runtime; D5 is independent.

## Domain model and evidence/authoritative

### Model

Represent records, queries/navigation, edit drafts, validation, pending
operations, stale responses, conflicts, errors, retry/cancel, and indeterminate
writes without treating client state as server truth.

### Binding requirements

Keyboard/focus/semantics/status/contrast/zoom, safe DOM, same-origin API,
race ordering, conflict and indeterminate handling, no durable record storage,
and no remote assets cannot be weakened.

## State and persistence

Record-bearing state is session memory only. Request generations prevent stale
responses from overwriting current state. Optional non-record preferences need
later authority and may not contain secrets or record data.

## Primary workflows

### Build and qualify

Resolve locked web inputs; build/inspect/scan immutable assets in D2; embed in
D3 static slot; run unit/component/browser/E2E/accessibility/security matrices.

### Operate and upgrade

Load same-origin app; search/navigate; create/edit/delete with validation,
pending/conflict/indeterminate behavior; restore focus; retry/cancel safely;
compare bundle/API/browser compatibility before replacement.

## Interfaces and integration

Inputs are browser interaction and same-origin D3 responses. Outputs are
accessible DOM/status/focus and same-origin requests. No separate server,
remote asset, cross-origin call, service-worker offline record store, or
durable application data.

## Failure and recovery

Cover initial/partial load failure, timeout, cancellation, network loss, stale
response, validation, conflict, interrupted write, indeterminate result,
asset/chunk failure, browser navigation race, focus loss, and retry exhaustion.

## Security and authorization

Use CSP-compatible safe DOM/rendering, same-origin protections, locked/scanned
dependencies, no remote executable content, safe URLs, redacted telemetry,
source-map controls, and synthetic/de-identified evidence only.

## Observability and operations

Capture bounded client errors, state transitions, accessibility results,
performance and interaction traces without secrets, record content, host paths,
raw unsafe URLs, or source disclosure.

## Compatibility migration and rollout

Declare web semantic version separately from v4.0 and exact D2/D3 plus
browser/OS/assistive-tech matrices. Diff manifest/routes/accessibility/API
usage and allow immutable bundle fallback.

## Testing strategy

Run WEB-001..WEB-013 plus applicable DOM/HTTP/SRCH/NAV/CNT/OPS/E2E vectors;
state reducer properties, race/cancel/conflict/indeterminate tests, keyboard,
focus, semantics, screen-reader, contrast, zoom, browser/Safari, CSP, DOM,
storage, dependency, map, and same-origin checks.

## Risks and edge cases

Focus traps, missing announcements, stale overwrite, duplicate writes,
inaccessible conflicts, unsafe HTML/URL, source-map leaks, remote assets,
durable sensitive state, browser drift, and broad compatibility claims block
affected gates.

## Deferred work

Paths, framework/locks, version policy, browser/AT matrix, source maps, owner,
and split remain open under `WEB-01`-`WEB-07`. Open work is not lifecycle.

## Architecture and specification acceptance

Not sought. Later human authority remains separate from accessibility pass,
artifact acceptance, conformance, security result, release, and completion.
