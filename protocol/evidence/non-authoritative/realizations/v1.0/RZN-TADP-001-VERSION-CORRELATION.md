# Govern work-version, realization-suite, initiative, and branch correlation

**Realization ID:** RZN-TADP-001-VERSION-CORRELATION

**Status:** Recorded

**Recorded by:** Codex on behalf of the User

**Recorded date:** 2026-11-10

**Source:** User instruction in the current repository task

**Related initiative or proposal:** [INIT-DSN-001 version-realization correlation](../../../../initiatives/design/INIT-DSN-001-version-realization-correlation/)

> **Evidence standing:** This realization is non-authoritative proposal input.
> It preserves the requested outcome and explicit invariant-change authority,
> but it does not accept the initiative, make the proposed invariant effective,
> prove delivery, or change any legacy lifecycle claim.

## Realization

The protocol does not yet give a canonical TADp work version a one-to-one,
reciprocal identity relationship with one realization suite, one
self-contained initiative, and one dedicated Git branch. Establish that
correlation consistently in the protocol and example project without
collapsing evidence classes, lifecycle gates, or initiative scope.

## Context and evidence

| Question | Record |
|---|---|
| What was observed? | Version-like realization directories, initiative records, and Git branches lack one authoritative project-level correlation model and machine validation. |
| Where and when? | TADp repository at branch v1, captured 2026-11-10 before initiative preparation. |
| Who is affected? | Protocol maintainers, project adopters, initiative owners, reviewers, validators, and the example project. |
| What source supports it? | The User's explicit invariant-revision instruction and required v4 migration case; current authoritative specifications 00 through 08; current templates, prompts, validators, tests, and realization records. |
| What is uncertain? | Legacy v4 versus v4.1 meaning-changing mappings and any other broad legacy mapping require separate human decisions; no legacy initiative state may be invented. |

## Candidate outcome

An authoritative correlation specification, synchronized protected protocol
and example sources, updated workflow consumers, migration ledger, and
validation rules make canonical work-version identity and the required
bijection explicit while preserving existing authority and lifecycle
distinctions.

## Suggested next step

Create and align the proposed design initiative
INIT-DSN-001-version-realization-correlation on its dedicated branch. Present
the exact aligned baseline for separate human acceptance before protected
design delivery begins.

## Bootstrap note

The current Stage 0 contract permits only a branch and two-README skeleton.
Accordingly, this source note was recorded immediately after Stage 0 so the
current Stage 1 proposal can cite a durable realization. The proposed revision
will require future Stage 0 preparation units to create the correlated suite
record and skeleton together; it must not rewrite this bootstrap history.
