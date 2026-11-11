# Standalone CLI image architecture and specification

**Initiative:** `INIT-IMP-005`
**Status:** Proposed
**Last updated:** 2026-11-11

## Proposal standing

This specification elaborates frozen input without resolving choices or
changing source authority.

## Specification boundary

Specify one D5 image, interaction/process behavior, public-SDK dispatch,
packaging, compatibility, and evidence—not D2-D4 or D6 products.

## Current repository baseline

No governed CLI source or image exists at the captured base.

## Goals and non-goals

### Goals

- Deterministic parsing, commands, human/JSON output, exits, signals, and pipes.
- Use only exact D4 public models/methods/exceptions.
- Preserve fixed private D3 targeting and hardened one-shot D2 execution.
- Produce CLI-001..CLI-011 and applicable security/contract evidence.

### Non-goals

- Select paths, libraries, versions, seams, owner, or split.
- Implement direct HTTP/SQLite, host CLI, daemon, mounts, ports, or socket.
- Claim remote production, regulated, or downstream readiness.

## Terms and identity

Command, option, output schema, diagnostic, exit code, signal outcome, image
digest, SDK/API compatibility entry, and evidence record require stable identity.

## Architectural decisions

No local decision is final. Authoritative contracts bind behavior; `CLI-01`
through `CLI-06` own open implementation choices.

## Boundaries and ownership

D5 owns command interaction, SDK dispatch, rendering, exits, process behavior,
image/help/completion, and evidence. D4 owns client logic, D3 API, D2 platform.

## Domain model and evidence/authoritative

### Model

Represent parsed intent, validated arguments, SDK results/exceptions, output
documents, diagnostics, and process outcomes without duplicating domain logic.

### Binding requirements

Help, validation, prompts, JSON/human separation, terminal safety, exit mapping,
signal/pipe behavior, fixed targeting, and SDK-only access cannot be weakened.

## State and persistence

The CLI is one-shot and non-durable. In-memory state ends at exit. It writes no
database, credential store, or host-mounted state.

## Primary workflows

### Build and qualify

Resolve locked parser/formatter and exact wheel; build/scan image; run command,
golden output, JSON schema, process-fault, and compatible live matrices.

### Operate and upgrade

Invoke through Compose; parse/validate; dispatch public SDK; render success or
diagnostic; handle signal/pipe; exit; compare semantic/compatibility policy
before replacing image.

## Interfaces and integration

Input is argv/stdin/terminal state. Output is defined stdout/stderr and exit
code. Network access uses the public wheel to fixed `record-api:8000/api/v1`.
No mounts, ports, socket, direct HTTP, SQLite, or internal SDK imports.

## Failure and recovery

Cover parse/validation failure, API/SDK faults, timeout/cancellation,
pre-dispatch interruption, post-dispatch ambiguity, broken pipe, render/encode
failure, non-TTY prompt conditions, and Compose pre-entrypoint failure.

## Security and authorization

Use non-root/least privilege, immutable locked inputs, fixed private endpoint,
safe terminal/JSON encoding, redacted diagnostics, no unsafe mounts/socket, and
synthetic/de-identified evidence only.

## Observability and operations

Diagnostics are bounded, stream-correct, actionable, and free of secrets,
payloads except explicit success output, host paths, and control injection.

## Compatibility migration and rollout

Declare CLI semantic version separately from v3.0 and exact D2-D4 matrices.
Compare command/help/output/JSON/exit surfaces and provide fallback by immutable
image identity.

## Testing strategy

Run CLI-001..CLI-011 plus applicable DOM/HTTP/SRCH/NAV/CNT/OPS/E2E vectors;
parser properties, golden human output, JSON schemas, terminal escaping, exits,
signals, pipes, pre/post-dispatch faults, and clean Compose invocation.

## Risks and edge cases

Ambiguous parsing, output drift, terminal injection, secret/content leakage,
broken-pipe stack traces, wrong exit, duplicate writes after interruption,
internal SDK coupling, and matrix overclaims block gates.

## Deferred work

Paths, libraries/locks, semantic policy, fault seams, owner, and split remain
open under `CLI-01`-`CLI-06`. Open work is not a lifecycle disposition.

## Architecture and specification acceptance

Not sought; later explicit human authority is required and remains separate
from artifact acceptance, conformance, release, or completion.
