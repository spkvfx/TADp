# Record search and navigation contract

**Architecture ID:** `ARC-CTR-003`  
**Status:** Accepted  
**Architecture revision:** `2.0.0`  
**Contract owner:** API component owner and project architecture authority  
**Producer:** Record API query layer  
**Consumers:** Python SDK, CLI through SDK, and browser adapter  
**Last reviewed:** 2026-11-10  

## Purpose and scope

This contract defines browsing, one-predicate search, exact/prefix/suffix/
contains/regex matching, deterministic ordinal ordering, forward pagination,
and next/previous navigation. The API alone computes membership and order.
Clients may render, page, and retain history but must not refilter, resort, or
infer adjacent records independently.

## Vocabulary

| Term | Binding meaning |
|---|---|
| Collection | All records whose ordinal is at or below the query snapshot ceiling |
| Search context | Exactly one `field` + `mode` + `query` predicate applied to the collection |
| Browse context | Collection with no predicate |
| Membership | Whether a canonical stored field value satisfies the context under the rules below |
| Order | Strict ascending internal ordinal for pages/next; strict descending scan for previous, returning the nearest member |
| Boundary | No qualifying ordinal exists before/after the current member; navigation does not wrap |
| Snapshot ceiling | Maximum committed ordinal observed when the initial page/context is created; later records are excluded |

## Interface surface

| Operation | Method and path | Required input | Success result | Principal failures |
|---|---|---|---|---|
| Browse/search page | `GET /api/v1/records` | Either no predicate parameters or all of `field`, `mode`, `q`; optional `limit`, `cursor` | `200 RecordPage` | `400 invalid_search/invalid_regex/cursor_invalid`, `503 search_budget_exceeded/store_*` |
| Adjacent record | `GET /api/v1/records/{id}/neighbor` | Canonical ID, `direction`; optional complete predicate and `ceiling` | `200 NeighborResult` with record or explicit boundary | `400`, `404`, `409 context_mismatch`, `503` |

### `RecordPage`

```json
{
  "items": [
    {"id":"9f3f6db2-39c7-4ce6-a570-7eaf32a2a95d","name":"Alpha","value":"one"}
  ],
  "next_cursor": null,
  "snapshot_ceiling": 42
}
```

- `items` is ordered by ascending ordinal and contains canonical public
  records only.
- `next_cursor` is a nonempty opaque string when more members may follow,
  otherwise null.
- `snapshot_ceiling` is a nonnegative decimal integer. It is navigation
  context metadata, not a record field or promise that every earlier ordinal
  exists/matches.
- Empty membership returns `200` with an empty array, null cursor, and current
  ceiling (zero for an empty database).

### `NeighborResult`

Record found:

```json
{
  "record": {"id":"...","name":"...","value":"..."},
  "boundary": null,
  "snapshot_ceiling": 42
}
```

Boundary reached:

```json
{"record":null,"boundary":"end","snapshot_ceiling":42}
```

- `boundary` is null when a record is returned, `start` for no previous member,
  or `end` for no next member.
- When `record` is present, the response includes that record's strong `ETag`.
  Boundary results contain no ETag.
- A boundary is a successful domain result, not `404` or an error.

## Query parameters

| Parameter | Accepted value | Rule |
|---|---|---|
| `field` | `id`, `name`, `value` | Present with both `mode` and `q`, or all three absent |
| `mode` | `exact`, `starts_with`, `ends_with`, `contains`, `regex` | Names are exact lowercase ASCII enum tokens |
| `q` | UTF-8 query string | Present even when exact-empty value search; no implicit trim |
| `limit` | Decimal integer 1-100 | Default 25; leading `+`, sign, fraction, exponent, or repeated value invalid |
| `cursor` | API-produced opaque base64url token | Page operation only; requires identical predicate parameters |
| `direction` | `next` or `previous` | Neighbor operation only; exactly one value |
| `ceiling` | Nonnegative decimal integer | Neighbor operation; omitted creates current ceiling; supplied value cannot exceed current max ordinal |

Repeated parameters, unknown query parameters, malformed percent encoding,
invalid UTF-8, or partial predicate triples return `400 invalid_search`.
Parameter names and enum values are case-sensitive.

## Query normalization and limits

1. Decode percent encoding and UTF-8 strictly.
2. Require Unicode scalar values and normalize `q` to NFC. Do not trim or
   perform line-ending normalization beyond what UTF-8 decoding yields.
3. Reject NUL and all C0/C1 controls, including TAB/LF, in every query.
4. For literal modes, require at most 4,096 scalar values and 16,384 UTF-8
   bytes. Empty `q` is permitted only for `field=value, mode=exact`.
5. For regex, require 1-256 UTF-8 bytes and at most 256 scalar values before
   compilation.
6. For `field=id`, literal queries may contain only lowercase ASCII hex digits
   and hyphens. `exact` additionally requires a canonical valid UUID. Regex
   uses the ordinary regex character rules against the canonical ID string.

An input normalized by the API is the context identity. Cursors bind to the
normalized form. Clients should send the original parameters consistently and
must not attempt to normalize a cursor themselves.

## Literal match semantics

Let `S` be the canonical stored field string and `Q` the normalized query.
Comparisons are case-sensitive Unicode scalar-value comparisons:

| Mode | Membership rule |
|---|---|
| `exact` | `S` and `Q` contain exactly the same scalar-value sequence |
| `starts_with` | `Q` is a prefix of `S` |
| `ends_with` | `Q` is a suffix of `S` |
| `contains` | `Q` occurs as one contiguous subsequence of `S` |

There is no locale collation, case folding, accent folding, tokenization,
stemming, glob syntax, wildcard escaping, SQL `LIKE` behavior, or implicit
whitespace normalization. Because stored text and query text are NFC, canonically
equivalent composed/decomposed inputs compare consistently after normalization.

`exact` is the accepted correction of the realization's `exacth match` text.

## Regex semantics

- The API uses an RE2-compatible UTF-8 engine selected in `ADR-003`.
- Membership uses unanchored search: a record matches when the engine finds any
  match within the complete canonical field string. Users use `^` and `$` when
  anchoring is desired.
- Default matching is case-sensitive. Supported inline flags are `i` (case
  insensitive), `m` (multiline anchors), and `s` (dot matches LF) in forms the
  selected RE2 binding accepts.
- Accepted constructs are literals, escapes, `.`, character classes,
  Unicode character classes supported by the bound engine, anchors,
  alternation, capturing/noncapturing groups, and bounded/unbounded repetition
  supported by RE2.
- Backreferences, lookahead/lookbehind, atomic/conditional groups, recursion,
  backtracking control verbs, embedded code, locale mode, and unsupported
  engine extensions are invalid.
- Invalid syntax or unsupported constructs return `400 invalid_regex` with a
  stable safe issue code and character/byte offset when the engine supplies
  one. The API does not return the full pattern in the problem detail/log.
- Regex is compiled once per request and applied only inside the API. SDK,
  CLI, web, and SQLite must not run an independent regex for membership.

The complete page/neighbor evaluation has a 2,000 ms server budget measured
after validation and before response serialization. The database holds at
most 10,000 bounded records. If the API cannot prove a complete result within
the budget, it returns `503 search_budget_exceeded` and no partial page.

## Ordering and pagination

### Snapshot and membership behavior

- An initial page computes `snapshot_ceiling = MAX(committed ordinal)` in the
  read transaction, or zero if empty.
- Only records with `ordinal <= snapshot_ceiling` are eligible. Records
  created later never enter that paging/navigation session.
- The operation evaluates membership from canonical current record values at
  each request. Concurrent updates may cause a record to enter or leave a
  search between pages. V1 is therefore a bounded-ceiling, read-committed view,
  not a historical snapshot.
- Within unchanged data and one context, results and neighbors are
  deterministic.

### Cursor format and treatment

The cursor is URL-safe base64 without padding over UTF-8 JSON with exactly
these members in exactly this order, no insignificant whitespace/BOM, decimal
integers without leading zeroes, and lowercase hexadecimal:

```json
{"v":1,"after":17,"ceiling":42,"filter_sha256":"<64 lowercase hex>"}
```

- `after` is the last returned ordinal; `ceiling` is the snapshot ceiling.
- Define `LP(s)` as ASCII decimal length of `UTF-8(s)`, one ASCII colon, then
  the UTF-8 bytes. `filter_sha256` is lowercase hex SHA-256 over exactly one of:
  - browse: `b"example-records-filter-v1\x00B"`; or
  - predicate: `b"example-records-filter-v1\x00P" + LP(field) + LP(mode) +
    LP(normalized_query)`.
  The field/mode bytes are their lowercase wire tokens. Length counts bytes,
  not code points; no separator, newline, or terminal NUL is appended.
- The token is opaque to consumers and untrusted by the API. The API strictly
  decodes shape/types/ranges/version, checks `after <= ceiling`, checks ceiling
  against the current database maximum, and requires the filter hash to match
  the supplied predicate.
- Cursor tampering or a mismatched/unsupported cursor returns
  `400 cursor_invalid`; it never changes SQL identifiers or bypasses limits.
- Cursors contain no record value or query text. They are not authenticated
  and grant no authority; all values are validated.
- Only forward page cursors are returned. A browser may keep earlier cursors in
  memory to implement Back; the API does not define a reverse-page cursor.

The API scans eligible ordinals after `after`, evaluates the predicate, and
returns at most `limit` matches. It may scan beyond `limit` to determine that a
subsequent match exists before deciding `next_cursor`. It must not return a
cursor based only on unfiltered rows that cannot yield another match.

## Next and previous semantics

For `GET /records/{id}/neighbor`:

1. Validate the current ID and retrieve its ordinal. Absent valid ID is `404`.
2. Establish the supplied ceiling or current maximum. If the current ordinal
   exceeds the ceiling, return `409 context_mismatch`.
3. If a predicate is supplied, evaluate the current record. If it does not
   match, return `409 context_mismatch`; clients must select a valid member or
   restart the context.
4. For `next`, choose the matching eligible record with the least ordinal
   greater than current. For `previous`, choose the greatest ordinal less than
   current.
5. If none exists, return the explicit `end` or `start` boundary. Never wrap.

The context predicate and ceiling must remain identical across a user's
search-result navigation. An update that causes the current record to leave
the context makes the next call a context mismatch; the client refetches or
reruns the search rather than guessing.

## Contract rules

| Concern | Rule | Owner |
|---|---|---|
| Authentication/authorization | Same local trust boundary as all API routes | API/operations |
| Validation/idempotency | GET only, strict query validation, side-effect-free | API query layer |
| Ordering/timeouts/retries | Ordinal order, 2 s complete-evaluation budget; qualifying GET may use bounded client retry | API and SDK |
| Versioning | Enum/token/meaning changes are breaking; adding a new mode/field requires synchronized consumers | Architecture authority |
| Observability | Log field/mode and query byte length/hash prefix only; never raw query or matched value | API operations |

## Failure and recovery

| Failure condition | Detection | Required behavior | Recovery owner |
|---|---|---|---|
| Partial/unknown/repeated query parameters | Query parser | `400 invalid_search`; no repository result | Caller corrects query |
| Invalid/unsupported regex | RE2 compile | `400 invalid_regex`; no partial result | Caller corrects pattern |
| Cursor mismatch/tampering | Strict cursor validator | `400 cursor_invalid` | Caller restarts initial search |
| Current ID absent | Repository lookup | `404 record_not_found` | Caller selects/refetches |
| Current record outside context | Membership check | `409 context_mismatch` | Caller reruns context |
| Search exceeds budget | Deadline check before response | `503 search_budget_exceeded`; discard partial results | Caller narrows/retries explicitly; operator investigates recurring issue |
| Store failure | Repository adapter | Stable store problem; never empty/boundary result | Operator/API |

## Compatibility and verification

Changing case, normalization, engine/dialect, unanchored behavior, limits,
ordering, snapshot treatment, cursor identity, or boundary behavior is breaking
even when route/schema fields remain unchanged.

| Verification | Scenario | Evidence location |
|---|---|---|
| Search vector matrix | `SRCH-*` literal, Unicode, regex, empty, limit, and invalid cases | [`ARC-CTR-009`](24-conformance-contract.md) |
| Navigation matrix | Full/search contexts, both directions, boundaries, updates, new creates | Future API/client evidence |
| Cursor property/fuzz tests | Round trip, tamper, mismatch, malformed, oversized tokens | Future API evidence |
| Cross-surface comparison | Same context returns identical IDs/order through API, SDK, CLI, and web | Future end-to-end evidence |

## Related records

- System boundary: [`ARC-BND-002`](12-api-service-boundary.md)
- Decision: [`ADR-003`](06-ADR-003-search-execution-semantics.md)
- Governing evidence: [`AUTH-EX-001`](01-accepted-architecture-baseline.md)

