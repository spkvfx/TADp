# Shared record domain contract

**Architecture ID:** `ARC-CTR-001`  
**Status:** Accepted  
**Architecture revision:** `2.0.0`  
**Contract owner:** Project architecture authority  
**Producer:** Record API domain layer  
**Consumers:** API transport, SQLite adapter, Python SDK, CLI, and web application  
**Last reviewed:** 2026-11-10  

## Purpose and scope

This contract owns the public v1 record shape, field meaning, input
normalization, validation, identity, mutability, and representation equality.
It is the single semantic source for every product. Storage-only metadata and
transport envelopes may accompany a record but may not become public record
fields or change these meanings.

## Public model

```json
{
  "id": "9f3f6db2-39c7-4ce6-a570-7eaf32a2a95d",
  "name": "Example name",
  "value": "Example value"
}
```

| Field | Public type | Required | Creation authority | Mutability | Accepted representation |
|---|---|---:|---|---|---|
| `id` | JSON string / UUID | Yes | API service only | Immutable forever | RFC 9562 UUIDv4 in lowercase canonical 8-4-4-4-12 hyphenated text |
| `name` | JSON string | Yes | Caller supplies; API normalizes/validates | Replaceable by conditional update | NFC, single-line, trimmed human label; 1-120 code points and at most 480 UTF-8 bytes |
| `value` | JSON string | Yes | Caller supplies; API normalizes/validates | Replaceable by conditional update | NFC text with LF newlines; 0-4,096 code points and at most 16,384 UTF-8 bytes |

The public record object contains exactly these three fields. API list or
neighbor envelopes, HTTP headers, SDK wrappers, CLI metadata, and internal
columns are not fields of the record itself.

## Normative input algorithm

All length checks count Unicode scalar values after normalization, not UTF-16
code units, grapheme clusters, terminal columns, or bytes. Byte limits are
measured by encoding the normalized string as UTF-8. Inputs containing an
unpaired surrogate or otherwise not representable as Unicode scalar values
are invalid.

### `name`

Apply these steps in order:

1. Require a JSON/Python string; do not coerce numbers, booleans, null, bytes,
   lists, or objects.
2. Replace CRLF (`U+000D U+000A`) and lone CR (`U+000D`) with LF (`U+000A`),
   so all newline forms are detectable consistently.
3. Remove Unicode `White_Space` property characters only from the beginning
   and end. Preserve all internal spacing exactly.
4. Normalize the result to Unicode Normalization Form C (NFC).
5. Reject LF, Unicode line/paragraph separators (`U+2028`, `U+2029`), all C0
   controls (`U+0000`-`U+001F`), DEL (`U+007F`), and C1 controls
   (`U+0080`-`U+009F`). The field is single-line.
6. Require 1-120 scalar values and no more than 480 UTF-8 bytes.

Names are not unique and have no case-insensitive identity meaning. Two
different normalized strings, including strings differing only by case, are
different names.

### `value`

Apply these steps in order:

1. Require a JSON/Python string with no coercion.
2. Replace CRLF and lone CR with LF.
3. Normalize to NFC. Do not trim leading/trailing whitespace.
4. Permit TAB (`U+0009`) and LF. Reject all other C0 controls, DEL, and C1
   controls. In particular, NUL is always invalid.
5. Require 0-4,096 scalar values and no more than 16,384 UTF-8 bytes.

The empty string is a valid `value`. Whitespace-only values are valid if they
meet the control and length rules. API responses and persistence must preserve
the normalized value exactly; clients must not perform additional trimming or
line-ending conversion.

### `id`

The API generates `id` after create input validation and immediately before
the create transaction. Generation uses UUID version 4 and operating-system
cryptographically secure randomness. The variant and version bits must be
valid. Serialization is the lowercase canonical hyphenated form. The API must
reject any create or update payload containing `id`, even if it equals the
existing value.

## Input and result models

| Model | Fields | Rules |
|---|---|---|
| `RecordCreate` | required `name`, required `value` | Unknown fields forbidden; both normalized as above; no `id` |
| `RecordPatch` | optional-by-presence `name`, optional-by-presence `value` | At least one field present; null forbidden; unknown fields forbidden; omitted field remains unchanged |
| `Record` | required `id`, `name`, `value` | All values already canonical; extra fields forbidden at typed client boundaries |
| `VersionedRecord` | `record` plus transport/store revision token | Wrapper only; revision is not a public record field |

`RecordPatch` may set `value` to the empty string. It may set a field to its
current normalized value; that is a valid no-op update and must return the
current record/ETag without incrementing the revision. A patch that normalizes
to no actual field change is also a no-op.

## Identity, equality, and lifecycle

- Record identity is `id` only. Names and values do not identify or deduplicate
  records.
- Two public record representations are equal only when all three canonical
  field values are equal.
- Creation is the only operation that introduces a record and allocates its
  UUID/ordinal/revision.
- Retrieval, search, and navigation never mutate a record.
- Update can replace `name`, `value`, or both under the current ETag. It cannot
  change `id` or storage metadata directly.
- Deletion, archival, undelete, merge, copy, and caller-selected identity are
  not v1 lifecycle operations.
- Duplicate `name`/`value` combinations are valid and create distinct records.

## Internal metadata boundary

The store maintains `ordinal`, `revision`, `created_at`, and `updated_at` under
`ARC-CTR-004`:

- `ordinal` defines total order and is never a public record field, record
  address, or caller-controlled value; search/navigation may return only the
  aggregate `snapshot_ceiling` context metadata defined by `ARC-CTR-003`;
- `revision` supports ETags and is never a public record field;
- timestamps support diagnostics/migration and do not define navigation;
- clients must not infer or depend on any internal value except the opaque
  behavior of an ETag or cursor explicitly returned by the API.

## Contract rules

| Concern | Rule | Owner |
|---|---|---|
| Validation | Strict types, ordered normalization, both code-point and byte limits, and forbidden unknown fields | API domain layer; clients may mirror |
| Authorization | Not applicable in local single-user v1; Docker publishes only IPv4 loopback and container clients remain on the declared private Compose network | Operations/API boundary |
| Idempotency | Reads are side-effect-free; normalized no-op patch preserves revision; create is not idempotent | API application layer |
| Ordering | Public record fields do not establish order; internal ordinal does | Persistence/query layer |
| Versioning | Field removal, meaning change, new required field, or relaxed/tightened accepted values is breaking | Architecture authority under `ADR-006` |
| Observability | Record `value` and full `name` are sensitive-by-default and absent from routine logs | Every component |

## Failure and recovery

| Failure condition | Detection | Required behavior | Recovery owner |
|---|---|---|---|
| Wrong JSON/Python type | Strict model validation | Reject with field-specific validation issue; no normalization/write | Caller corrects input |
| Empty/invalid/oversized normalized name | Domain validation | Reject entire command; no record/revision change | Caller corrects input |
| Invalid/oversized normalized value | Domain validation | Reject entire command; no record/revision change | Caller corrects input |
| Caller supplies `id` or unknown field | Extra-field validation | Reject entire command | Caller removes field |
| UUID collision | Unique constraint after generated ID | Roll back and regenerate/retry internally up to three total attempts; then internal failure | API service; caller must not choose ID |
| Stored row violates contract | Row decoder/integrity verification | Do not return partial record; mark store unhealthy and report integrity failure | Operator restores/repairs through governed process |

The bounded internal retry for a UUID collision is permitted because the first
transaction did not commit and no caller-visible identity existed. It is not a
general write retry policy.

## Compatibility and verification

Changing normalization, limits, field meaning, mutability, identity, or public
shape is a breaking architecture and API change unless evidence proves the
accepted value set and every existing representation remain identical.

| Verification | Scenario | Evidence location |
|---|---|---|
| Domain unit matrix | Required conformance vectors `DOM-*` | [`ARC-CTR-009`](24-conformance-contract.md); future API evidence |
| Cross-model round trip | API -> SDK -> CLI/JS decoder preserves all canonical values | Future cross-product evidence |
| Database defense | Direct attempted ID change and invalid persisted rows fail | Future persistence evidence |
| Negative route inventory | No delete/ID-update/caller-ID operation exists | Future API conformance evidence |

## Related records

- System boundaries: [`ARC-BND-001`](03-record-platform-boundary.md), [`ARC-BND-002`](12-api-service-boundary.md), [`ARC-BND-003`](15-sqlite-store-boundary.md)
- Decisions: [`ADR-002`](05-ADR-002-identity-order-and-concurrency.md), [`ADR-006`](09-ADR-006-contract-versioning-and-feedback.md)
- Governing evidence: [`AUTH-EX-001`](01-accepted-architecture-baseline.md)

