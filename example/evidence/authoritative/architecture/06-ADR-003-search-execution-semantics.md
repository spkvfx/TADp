# Centralized bounded search execution semantics

**Decision ID:** `ADR-003`  
**Status:** Accepted  
**Architecture revision:** `2.0.1`  
**Decision owner:** User, project authority  
**Decision date:** 2026-11-10  
**Supersedes / superseded by:** Not applicable  
**Related initiative:** Not applicable - direct project-architecture instruction  

## Decision question

Where and how are literal and regular-expression searches evaluated so every
surface returns the same safe, deterministic membership and order?

## Context and binding evidence

| Source | Precise claim or constraint | Effect on this decision |
|---|---|---|
| [`AUTH-EX-001.4`](01-accepted-architecture-baseline.md) | Search meaning and order are API-owned and consistent | Prohibits independent client/SQLite semantics |
| [`RZN-001`](../../non-authoritative/realizations/v0/RZN-001-example-record-application.md), search behavior and Q06-Q07 | All fields/modes including regex requested; dialect/case/safety unresolved | Requires explicit semantics and resource bounds |
| [`ARC-CTR-001`](11-record-domain-contract.md) | Stored text is bounded NFC Unicode | Supplies canonical comparison input |

## Decision

The API query layer is the sole evaluator of search membership. V1 accepts
zero predicates for browse or exactly one predicate composed of field
(`id|name|value`), mode (`exact|starts_with|ends_with|contains|regex`), and
query.

- Literal matching compares NFC scalar sequences case-sensitively with no
  locale, collation, trimming, wildcard, or token rules.
- Regex uses a pinned RE2-compatible Python binding and unanchored search
  semantics. Users anchor explicitly. Backreferences/lookaround and other
  non-RE2 constructs are rejected.
- Regex patterns are at most 256 UTF-8 bytes. Record fields, record count, and
  request evaluation time are bounded by the accepted contracts.
- Search results and adjacent navigation use ascending internal ordinal and an
  initial maximum-ordinal ceiling.
- SQLite supplies ordered rows but does not define `LIKE`, collation, or
  `REGEXP` membership. Clients never re-evaluate a query.
- An over-budget search fails as a whole; partial results are not returned as
  complete.

All precise syntax, cursor, snapshot, invalid-query, and boundary rules are
owned by [`ARC-CTR-003`](14-search-navigation-contract.md).

## Consequences

### Benefits

- API, SDK, CLI, and web return identical membership/order.
- RE2 avoids catastrophic backtracking classes by construction.
- Case-sensitive NFC rules are testable without locale or SQLite collation
  drift.
- The bounded dataset makes application-layer semantics acceptable for the
  educational example and supports detailed conformance vectors.
- Centralization prevents a browser or CLI from exposing behavior the API
  cannot reproduce.

### Costs, risks, and required follow-up

- V1 search is intentionally not an optimized large-dataset design.
- Users must request case-insensitive regex via supported inline flag; literal
  modes remain case-sensitive.
- RE2 does not support familiar backtracking-only regex features.
- Scanning bounded rows may reach the request budget; failures must be explicit.
- Changes to the RE2 binding/version require dialect conformance review.
- Future indexing must preserve exact accepted semantics and cannot silently
  delegate to SQLite `LIKE`/collation.

## Alternatives considered

| Alternative | Why it was not selected | Reconsideration trigger |
|---|---|---|
| SQLite `LIKE` and custom `REGEXP` | Built-in case/collation differs from desired Unicode rules; regex remains extension-defined | A proven extension/index implementing every accepted vector identically |
| Python standard `re` | Backtracking can create disproportionate runtime and lacks a dependable built-in per-match timeout | A bounded safe engine with equivalent accepted dialect and evidence |
| Client-side search | Downloads state and creates divergent behavior/security/resource use | Never for authoritative membership in this architecture |
| Case-insensitive literal search by default | Unicode case folding expands/changes code points and is less transparent for an example | A user requirement plus an accepted normalization/index strategy |
| Multi-predicate boolean queries | Expands UI/API/cursor semantics beyond the requested compact example | A separately scoped query-language product |

## Acceptance and verification

| Required result | How it is verified | Evidence location |
|---|---|---|
| All literal modes follow exact NFC/case rules | Required Unicode/literal vector matrix | [`ARC-CTR-009`](24-conformance-contract.md) |
| Regex dialect rejects unsafe unsupported features | Compile/negative vectors and dependency-version pin | Future API evidence |
| Every surface yields same IDs/order | End-to-end cross-surface comparison | Future product evidence |
| Budget failure returns no partial page | Injected deadline test | Future API evidence |
| No SQLite/client semantic search path exists | Architecture/dependency tests | Future API/clients evidence |

## Revision record

| Date | Change | Authority |
|---|---|---|
| 2026-11-10 | Accepted centralized case-sensitive NFC/RE2 search with bounded execution | User-authorized best-judgment architecture method recorded in `ARC-AUT-001` |

