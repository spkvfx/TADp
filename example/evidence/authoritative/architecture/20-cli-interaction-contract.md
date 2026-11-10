# User to record CLI interaction contract

**Architecture ID:** `ARC-CTR-006`  
**Status:** Accepted  
**Architecture revision:** `2.0.0`  
**Contract owner:** CLI component owner and project architecture authority  
**Producer:** `record-cli` one-shot Compose service / `recordctl` image entrypoint  
**Consumer:** Local shell user or invoking process  
**Last reviewed:** 2026-11-10  

## Purpose and scope

This contract defines v1 CLI invocation, commands, configuration precedence,
input sources, human/JSON outputs, diagnostics, and exit codes. The CLI is a
thin application over `ARC-CTR-005` and must expose all accepted user record
capabilities without direct HTTP/database shortcuts.
The host-facing executable is Docker Compose; `recordctl` runs only inside the
CLI image. Direct native installation/execution is not a supported interface.

## Invocation grammar

```text
docker compose run --rm record-cli [GLOBAL-OPTIONS] COMMAND [COMMAND-OPTIONS]
```

For redirected/noninteractive stdin the caller adds Compose option `-T` before
the service name: `docker compose run --rm -T record-cli ...`. Compose options
are not CLI options. The caller first brings up the accepted release with
`docker compose up -d --wait record-api`; a CLI invocation does not own API
lifecycle. Inside the image, the equivalent entrypoint grammar is `recordctl
[GLOBAL-OPTIONS] COMMAND [COMMAND-OPTIONS]`, used only by image/conformance
tests.

Global options:

| Option | Meaning and rule |
|---|---|
| `--timeout SECONDS` | Finite decimal `0.1..60.0`; default `5.0` |
| `--json` | Emit stable machine-readable success/problem JSON to stdout/stderr as defined below |
| `--no-color` | Disable ANSI styling; styling is also disabled when stream is not a TTY or `NO_COLOR` is present |
| `--version` | Print CLI and compatible SDK/API-major information, then exit 0; mutually exclusive with command |
| `--help` | Print contextual help to stdout, then exit 0 |

The release Compose service supplies the fixed internal base URL
`http://record-api:8000`; there is no public `--api-url`, user-overridable URL
environment variable, implicit config file, credential, working-directory
database, host gateway discovery, or Docker-socket discovery. Command timeout
option overrides the image default. Unknown options, missing values, repeated
single-value options, or conflicting sources are usage errors. A test image
may inject an HTTPX transport without adding a release CLI route.

Every SDK call appends the same `/api/v1` path used by the browser adapter.
There is no CLI prefix, gateway, command endpoint, or alternate representation;
the internal Compose origin changes transport addressing only.

## Commands

### `create`

```text
docker compose run --rm record-cli create --name TEXT VALUE-SOURCE
```

Exactly one value source is required:

- `--value TEXT`; or
- `--value-stdin`.

Stdin is read as strict UTF-8 with a 16,384-byte accepted-value bound plus
bounded decoder overhead, only when explicitly selected. A host file is sent
through shell redirection to `--value-stdin`; no path is passed and no host
directory/file is mounted in the container. The CLI validates, calls
`create_record` once, and prints the canonical created record. It never
retries or searches for a similar record.

### `get`

```text
docker compose run --rm record-cli get ID
```

Requires one canonical UUID. Prints the canonical record. Missing record uses
exit 3; malformed ID is usage/validation exit 2.

### `update`

```text
docker compose run --rm record-cli update ID [--name TEXT] [VALUE-SOURCE]
```

At least one mutable field is supplied. The CLI retrieves the record, keeps its
ETag, submits one conditional patch, and prints the resulting record. It must
not prompt for or perform force overwrite. A no-op is success with the same
record. Conflict is exit 5; indeterminate write is exit 9 with reconcile
guidance. An optional future explicit ETag flag is not part of v1.

### `search`

```text
docker compose run --rm record-cli search
    [--field FIELD --mode MODE --query TEXT|--query-stdin]
    [--limit N] [--all] [--max-pages N]
```

- Predicate options are all present or all absent. Absence browses records.
- `--field` and `--mode` use exact accepted enum tokens.
- `--query-stdin` may replace `--query` as a mutually exclusive source; host
  files use redirection, not a mount, and query input is bounded by search
  limits.
- `--limit` is page size 1-100, default 25.
- Without `--all`, print one page. With `--all`, follow cursors using SDK
  `iter_records`; `--max-pages` may bound it and is valid only with `--all`.
- Empty results are success and produce an explicit empty rendering/array.

### `next` and `previous`

```text
docker compose run --rm record-cli next ID [SEARCH-CONTEXT] [--ceiling N]
docker compose run --rm record-cli previous ID [SEARCH-CONTEXT] [--ceiling N]
```

Search context uses the same all-or-none `--field/--mode/query-source` options.
The command calls SDK `neighbor`. A returned record is printed. A start/end
boundary prints a safe boundary message/object and exits 4; it is not an error
diagnostic or wraparound. A context mismatch exits 8.

No `delete`, bulk, record import/export, SQL, force-update, server-start, login,
host-path input, Docker-control, or interactive full-screen command exists.

## Success output

### Human mode

- Single record output uses labeled `ID`, `Name`, and `Value` fields in that
  order. ID is never described as editable.
- Multiline values begin on a new line and are emitted literally only to
  stdout. Potential terminal control characters are already excluded by the
  domain contract; ANSI styling never derives from record content.
- Search prints a header and ordered rows/blocks without truncating data
  silently. If a TTY-width view abbreviates display, it must clearly mark the
  abbreviation and offer/use a full block form; JSON is always complete.
- Empty search prints `No records found.` to stdout and exits 0.
- Create/update success says which action committed and includes canonical
  data; it is emitted only after SDK success.

### JSON mode

stdout contains exactly one UTF-8 JSON document plus a trailing LF and no ANSI
codes/progress/diagnostics:

| Outcome | JSON document |
|---|---|
| Single record | `{ "record": { "id": "...", "name": "...", "value": "..." } }` |
| One search page | `{"items": [...], "next_cursor": string|null, "snapshot_ceiling": int}` |
| `--all` search | `{"items": [...], "complete": bool, "pages": int, "snapshot_ceiling": int}`; `complete=false` only when user `--max-pages` stops normally |
| Boundary | `{"record": null, "boundary": "start"|"end", "snapshot_ceiling": int}` |
| Version | A documented version object when `--json --version` is used |

JSON property names/meanings and record ordering are stable within CLI major
version. `request_id` may appear as optional top-level metadata only after a
compatible minor revision; record objects remain closed.

## Diagnostic output

- Usage help requested explicitly goes to stdout/0. Parser errors go to stderr
  with a short usage line/2.
- Runtime failures write one safe diagnostic to stderr. stdout remains empty.
- In JSON mode, stderr contains one problem-like object with `code`, `message`,
  optional `request_id`, and safe issue metadata; no traceback/HTTPX repr/value
  or raw regex/query.
- `--debug` is deliberately absent from v1. Developers use separately
  configured safe logs; ordinary users never receive stack traces.
- Indeterminate writes explicitly say the outcome is unknown and instruct the
  user to `get`/search before manually deciding whether to retry.

## Stable exit codes

| Code | Class | Examples |
|---:|---|---|
| 0 | Success | Create/get/update, including no-op; empty or completed search; help/version |
| 1 | Unexpected CLI/protocol failure | Internal CLI bug or malformed incompatible success |
| 2 | Usage or local validation | Parser error, invalid ID/model/query/options/file encoding |
| 3 | Record not found | Canonical requested ID absent |
| 4 | Collection boundary | `next` at end or `previous` at start |
| 5 | Revision conflict | Conditional update failed with `revision_conflict` |
| 6 | Service unavailable | Exhausted safe-read retry, store unavailable/busy, connection failure before a write dispatch |
| 7 | Server/API failure | Valid API problem not assigned another exit class, including capacity exceeded for create |
| 8 | Search/navigation failure | Invalid server search/regex/cursor, context mismatch, or search budget exceeded |
| 9 | Indeterminate write | Create/update request dispatched but outcome unprovable |
| 130 | Interrupted | SIGINT/console interrupt; no success claim |

An empty search is not exit 3/4/8. A capacity error is not usage. Exit 130 does
not imply rollback; if interruption followed write dispatch, stderr must retain
indeterminate guidance even though the process exit remains 130.

## Contract rules

| Concern | Rule | Owner |
|---|---|---|
| Authentication | None; no token flags/env/config | CLI/architecture |
| Validation/idempotency | Validate locally; one SDK write invocation; no auto retry | CLI |
| Ordering/timeouts/retries | Preserve SDK/API order; safe-read retry remains SDK-owned | SDK/API |
| Versioning | Command grammar, JSON schema, streams, and exit meanings use CLI semantic versioning | CLI release owner |
| Observability | No telemetry; safe diagnostics; full data only in explicit success output | CLI |
| Container execution | One ephemeral container per invocation; private API DNS; no mounts/ports/restart; image digest belongs to release | Platform/CLI |

## Failure and recovery

| Failure condition | Detection | Required behavior | Recovery owner |
|---|---|---|---|
| Invalid/missing conflicting options | Parser/validator | stderr/2; no SDK call | User |
| Stdin oversized/non-UTF-8 or absent when selected | Bounded reader | stderr/2; no SDK call | User |
| Missing record or boundary | SDK typed result | Stable output/exit 3 or 4 | User chooses next action |
| Conflict | SDK exception | No overwrite; stderr/5; advise refetch/reapply | User |
| Write outcome unknown | SDK exception/interruption phase tracking | stderr/9 or 130 with reconcile guidance; no auto retry | User |
| API unavailable/failure | SDK exception | stderr/6/7/8; no fabricated data | Operator/user |
| Broken stdout pipe | OS write failure | Stop rendering, close normally using platform convention; never repeat a write | Invoking pipeline |
| Compose cannot create/start container | Compose/daemon pre-entrypoint failure | No CLI process/exit mapping exists; show Compose diagnostic and repair platform/release | Operator |

## Compatibility and verification

| Verification | Scenario | Evidence location |
|---|---|---|
| Process golden tests | Every command, mode, stream, JSON shape, and exit code | [`ARC-CTR-009`](24-conformance-contract.md) |
| Live parity | CLI results/actions equal direct API/SDK vectors | Future CLI evidence |
| Packaging | Pinned CLI image execution through released Compose outside source checkout, with exact SDK wheel hash | Future CLI release evidence |
| Negative architecture | No HTTPX/SQLite/API-server imports or hidden commands | Future CLI evidence |
| Container isolation | No mounts/published ports/Docker socket, fixed private DNS, nonroot/read-only/capability controls | Future operations evidence |
| Clean-host use | Every command works with Docker/Compose and browser as the only host runtime prerequisites | Required by `ARC-CTR-009` |

## Related records

- System boundary: [`ARC-BND-005`](19-cli-boundary.md)
- SDK contract: [`ARC-CTR-005`](18-python-sdk-contract.md)
- Decisions: [`ADR-001`](04-ADR-001-api-exclusive-persistence.md), [`ADR-007`](10-ADR-007-product-and-delivery-decomposition.md)
- Governing evidence: [`AUTH-EX-001`](01-accepted-architecture-baseline.md)
- Superseded native deployment baseline: [`ARC-REV-001`](revisions/1.0.0/00-superseded-native-runtime-deployment-baseline.md)

## Revision record

| Date | Change | Authority |
|---|---|---|
| 2026-11-10 | Defined native `recordctl` command, output, and exit semantics | User-authorized best-judgment architecture completion |
| 2026-11-10 | Made the host interface a one-shot Compose CLI container with fixed private API discovery and stdin-only host data ingress | User's explicit full-Dockerization/no-host-services instruction |

