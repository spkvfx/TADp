# Standalone CLI image delivery roadmap

**Initiative:** `INIT-IMP-005`
**Status:** Proposed planning only
**Last updated:** 2026-11-11

## Objective

Sequence a future D5 image delivery without implying authorization/release.

## Delivery scope

### Included

One CLI source/interaction surface, immutable image, help/completion, exact
D2-D4 compatibility, and D5 evidence.

### Excluded from this roadmap

D2-D4/D6 delivery, direct HTTP/SQLite, host CLI/daemon, mounts/ports/socket,
production/regulated use, ePHI, unresolved destinations/tools.

## Type-specific delivery boundary

Delivery starts only after authority, blocking decisions, and product mapping.

## Prerequisites

Assumptions reviewed; `CLI-01`-`CLI-06` addressed; exact D2-D4 artifacts and
security/data gates reviewed.

## Phase summary

| Phase | Outcome | Entry gate | Exit evidence |
|---|---|---|---|
| 0 | Specification/placement authorized | Human review | Decisions/product map |
| 1 | Command/output core | Phase 0 | CLI contract evidence |
| 2 | Image/process behavior | Phase 1 | Compose/fault/security matrix |
| 3 | D5 qualification | Phase 2 | Artifact-bound D5 record |

## Phase 0 - Authorize specification and output boundary

### Objective

Resolve scope, paths, stack, policy, seams, owner, and evidence plan.

### Work

Review contracts, D2-D4 matrix, security/data use, compatibility, retention,
and create required product/decision records.

### Exit gate

Explicit authority exists and required D5 choices are addressed.

## Phase 1 - Implement command and output core

### Objective

Build parser, validation, SDK dispatch, help, human/JSON, and exits.

### Work

Implement commands without direct HTTP/SQLite or internal SDK dependencies.

### Exit gate

CLI interaction vectors and output/exit schemas pass.

## Phase 2 - Package and prove process behavior

### Objective

Build immutable one-shot image and verify signals, pipes, faults, and matrix.

### Work

Lock/build/scan; test non-root Compose invocation, fixed targeting,
pre/post-dispatch faults, terminal safety, and compatible live behavior.

### Exit gate

Artifact, process, security, and compatibility evidence passes.

## Phase 3 - Qualify D5 outcome

### Objective

Assemble a D5-only review packet.

### Work

Complete source-currency, risk/license/vulnerability, compatibility, incident,
evidence, and clean invocation reviews.

### Exit gate

A human can evaluate D5 without inferring D2-D4/D6 completion.

## Rollout controls

Immutable image identity, strict output/exit diff, narrow matrix, fallback,
indeterminate-write stop rules, and safety/evidence stop conditions.

## Release definition

One immutable image plus locked inputs, help/completion, semantic compatibility,
security records, and complete D5 evidence. No release is created here.
