# Record identity, order, and concurrency metadata

**Decision ID:** `ADR-002`  
**Status:** Accepted  
**Architecture revision:** `2.0.0`  
**Decision owner:** User, project authority  
**Decision date:** 2026-11-10  
**Supersedes / superseded by:** Not applicable  
**Related initiative:** Not applicable - direct project-architecture instruction  

## Decision question

How does v1 assign immutable public identity, define deterministic adjacency,
and prevent concurrent edits from silently overwriting one another?

## Context and binding evidence

| Source | Precise claim or constraint | Effect on this decision |
|---|---|---|
| [`AUTH-EX-001.2`](01-accepted-architecture-baseline.md) | Public `id` is immutable and service-generated | Requires a canonical server identity policy |
| [`AUTH-EX-001.5`](01-accepted-architecture-baseline.md) | Updates require the current strong revision ETag | Requires internal revision metadata |
| [`RZN-001`](../../non-authoritative/realizations/v0/RZN-001-example-record-application.md), Q03-Q05 | UUID form, navigation order, boundaries, and concurrency were unresolved | Context only; requires coherent choices |
| [`ARC-AUT-001`](02-authority-and-source-disposition.md) | Best judgment authorized for all listed questions | Authorizes selected metadata model |

## Decision

V1 uses four separate concepts rather than overloading public ID:

1. **Public identity:** the API creates a UUIDv4 using the operating-system
   CSPRNG after input validation. It is serialized/stored as canonical
   lowercase hyphenated text and never changes. Callers cannot supply it.
2. **Navigation order:** SQLite allocates an internal positive integer
   `ordinal` using `INTEGER PRIMARY KEY AUTOINCREMENT`. It is never reused,
   changed, or exposed as a public record field/address. Ascending ordinal is
   creation order; adjacent navigation selects the nearest qualifying ordinal.
   Search/navigation may expose only the aggregate `snapshot_ceiling` context
   value defined by `ARC-CTR-003`, never a record's ordinal.
3. **Concurrency revision:** each record begins at internal `revision = 1`.
   A material update increments it exactly once. HTTP exposes it only as the
   strong opaque ETag `"rev-{decimal}"`; PATCH requires the current tag.
4. **Operational timestamps:** `created_at` and `updated_at` are API-generated
   UTC RFC 3339 strings with exactly millisecond precision. They support
   diagnostics/migration but do not establish identity or navigation order.

No-op normalized updates retain revision and `updated_at`. There is no delete,
so ordinals never disappear through supported behavior; migration may preserve
gaps but must never renumber existing records.

## Consequences

### Benefits

- Random public IDs do not disclose collection size or order.
- Navigation remains total and deterministic even when timestamps collide.
- ID format remains simple and widely supported.
- ETags make stale writes explicit without expanding the three-field public
  record model.
- Internal metadata may evolve under migration while the public record shape
  stays compact.

### Costs, risks, and required follow-up

- SQLite schema contains internal fields beyond the three public fields.
- UUIDv4 is not naturally sortable; every ordered query uses `ordinal`.
- ETags expose a revision counter if inspected, though clients must treat it
  as opaque; this is acceptable in local single-user v1.
- `snapshot_ceiling` reveals the maximum committed ordinal and therefore an
  upper bound on historical creates; it is accepted local navigation metadata,
  not a record identifier or proof that every lower ordinal currently matches.
- A create response lost in transit is indeterminate because callers cannot
  preselect or deduplicate identity.
- Database migration/restore must preserve IDs, ordinals, revisions, and
  timestamps exactly.
- Conformance must test UUID collision handling, no-op updates, stale ETags,
  ordering, and non-wrap boundaries.

## Alternatives considered

| Alternative | Why it was not selected | Reconsideration trigger |
|---|---|---|
| UUIDv7 as both identity and order | Couples public identity to order/time, relies on newer runtime/library behavior, and complicates same-timestamp total order | A cross-database distributed creation requirement |
| Caller-supplied UUID | Allows inconsistent generation and makes create/ownership rules harder to protect | An import/synchronization product with accepted external identity |
| Timestamp plus UUID ordering | Harder to explain/test and sensitive to clock behavior | Multi-node writers where a database sequence is unavailable |
| Lexical name or ID ordering | User edits would move neighbors or random IDs would create unintuitive order | A user-selectable sort/search product revision |
| Last-write-wins | Can silently lose edits | Never within the accepted record-editing safety claim |
| Expose `revision` as a fourth record field | Violates compact three-field public model and leaks transport concern | A new public domain contract requiring revisions as user data |

## Acceptance and verification

| Required result | How it is verified | Evidence location |
|---|---|---|
| IDs are valid canonical UUIDv4 and immutable | Generator, API, schema-trigger, migration tests | Future API/persistence evidence |
| Ordinal order is deterministic and no record ordinal is exposed | Repository/query tests, public record-schema scan, and ceiling-only response review | [`ARC-CTR-003`](14-search-navigation-contract.md) conformance |
| Stale update never overwrites | Concurrent conditional-update test | [`ARC-CTR-009`](24-conformance-contract.md) |
| No-op update preserves revision/time | Domain plus HTTP ETag test | Future API evidence |
| Restore preserves all metadata | Backup/restore semantic comparison | Future operations evidence |

## Revision record

| Date | Change | Authority |
|---|---|---|
| 2026-11-10 | Accepted UUIDv4, internal ordinal/revision, ETag, and timestamp model | User-authorized best-judgment architecture method recorded in `ARC-AUT-001` |

