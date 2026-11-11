# Version-realization-initiative correlation migration

## Purpose and standing

This guide explains how an existing TADp project adopts the one-to-one
correlation among work version, realization suite, self-contained initiative,
and dedicated Git branch. It implements the authoritative
[correlation specification](../../evidence/authoritative/LLM/09_Codex_Version_Realization_Initiative_Correlation_Specification.md)
without rewriting legacy identity or inventing missing evidence.

The guide is procedural. It does not accept an initiative, resolve a mapping,
or make a legacy record governed by the new revision merely because a row is
added.

## Establish the project effective point

1. Adopt one complete TADp distribution commit containing specification 09,
   its affected templates and prompts, validator behavior, tests,
   documentation, and protected-source locks.
2. Record that exact commit in `project-profile.md` as the correlation-revision
   effective point.
3. Record the project's initiative branch convention. If none exists, use
   `initiative/v<major>.<minor>-<initiative-slug>`.
4. Instantiate
   `template/project/initiatives/version-correlation-migration-ledger.template.md`
   as `initiatives/version-correlation-migration-ledger.md` and link it from
   the profile.
5. Do not allocate post-effective work until the profile, canonical initiative
   index, status view, and ledger are present and validation can identify their
   roles.

The effective point governs new allocation. It does not retroactively change
the meaning, authority, lifecycle, or completion standing of an earlier
record.

## Inventory without inference

Inventory every pre-effective version-like identity, realization suite or
note, initiative, recorded branch, workflow revision, lifecycle state, and
supporting evidence. Preserve exact paths and source text.

For each item, determine only what the evidence proves:

- whether a version spelling was canonical or merely version-like;
- whether a suite actually existed and which notes it contained;
- whether an initiative existed and which workflow revision governed it;
- whether a branch and captured base were recorded; and
- whether a human decision, acceptance, delivery, completion, or branch-removal
  record exists.

Do not infer a missing relationship from a shared number, similar title,
directory adjacency, current code, or likely intent.

## Required ledger format

Use this minimum table:

| Legacy identity | Canonical identity | Suite | Initiative | Branch | Action | Authority/evidence | Ambiguity or blocker |
|---|---|---|---|---|---|---|---|
| `<legacy identity>` | `<canonical identity or not allocated>` | `<suite path or not inferred>` | `<initiative path or not inferred>` | `<branch or not inferred>` | `<action>` | `<source links>; governing workflow revision: <revision>` | `<ambiguity>; re-entry or migration condition: <condition>` |

Every row must preserve the original identity, link its evidence, identify the
earlier workflow revision, and state a re-entry or migration condition. Use
`Not allocated — must not be inferred` rather than leaving a partial new tuple.

## Actions

- **Unmigrated:** Preserve the earlier identity and compatible workflow. The
  row is an actionable validator warning. A substantive change requires a new
  tuple unless a later migration decision says otherwise.
- **Deferred:** Preserve the earlier identity and name the event or evidence
  that will reopen migration. The row remains an actionable warning.
- **Normalize:** Change only notation when evidence proves identity is
  unchanged. A bare `vN` may become `vN.0`; no other meaning may change.
- **Migrate:** Map a complete evidenced legacy tuple to the new model through a
  separately governed migration on its own correlated branch.
- **Split:** Preserve the broad legacy source and allocate one new tuple per
  narrow outcome. Never imply the source was always split.
- **Blocked:** Preserve every candidate identity and name the exact ambiguity,
  evidence owner, and human decision needed.

An `Unmigrated` or `Deferred` row must not contain some new correlation fields
while leaving others inferred or absent. It either preserves evidenced legacy
fields as legacy evidence or states that the canonical fields are not
allocated.

## Meaning-preserving and meaning-changing cases

Normalize `vN` to `vN.0` only when the source proves that the difference is
notation alone. Numeric resemblance is insufficient.

When a broad suite embeds or references a separate dot-scoped outcome,
preserve both identities as a possible split. A mapping that changes scope,
ownership, authority boundary, output family, compatibility obligation, or
verification claim is meaning-changing and requires an explicit human
decision receipt before it is applied.

Do not create missing realization notes, initiatives, branches, captured base
commits, decisions, acceptance, implementation, completion, or release
evidence. A migrated initiative starts `Proposed` unless retained evidence
supports another legal state.

## New and successor work after adoption

Every post-effective work unit uses Stage 0 to preflight and create one unused
canonical work version, realization suite, initiative, and version-bearing
branch from a captured base. Every mandatory split and substantive successor
does the same. An unchanged-claim reopening may retain its tuple only under its
lifecycle evidence.

Migrate project-specific legacy tuples later, one narrow tuple at a time on
its own correlated branch. Updating the protocol distribution itself does not
perform those migrations.

## Validation and recovery

The validator reports a warning for a complete `Unmigrated` or `Deferred` row.
It reports an error for a non-canonical governed version, duplicate identity,
partial or inconsistent tuple, orphan record, missing reciprocal metadata,
undeclared legacy record, missing ledger disposition, mixed old and new
fields, absent active branch, or absent historical branch without linked
removal authority.

Never write or infer a mapping to clear a finding. Correct the owning record,
add a truthful legacy disposition, obtain the required human decision, or
allocate a new tuple through Stage 0.

Run the protected-source check, full validator, and unit tests after adoption.
A warning preserves actionable legacy work; it does not make the project
invalid or claim the legacy tuple was migrated.
