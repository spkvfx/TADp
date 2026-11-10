# Record command-line interface system boundary

**Architecture ID:** `ARC-BND-005`  
**Status:** Accepted  
**Architecture revision:** `2.0.0`  
**Owner:** CLI component owner under a future accepted initiative  
**Last reviewed:** 2026-11-10  
**Related records:** [`ADR-001`](04-ADR-001-api-exclusive-persistence.md), [`ARC-CTR-005`](18-python-sdk-contract.md), [`ARC-CTR-006`](20-cli-interaction-contract.md), [`ARC-CTR-008`](23-operations-security-contract.md)  

## Boundary statement

The CLI boundary is the independently versioned `example-records-cli` OCI
image, its exec-form `recordctl` entrypoint, argument/input parser, SDK
invocation adapter, human/JSON formatters, stderr diagnostics, and documented
exit-code mapping. A local shell user invokes it as the one-shot Compose
service `record-cli`; no host Python, pipx, wheel, executable, or repository
checkout is required. The image requires a healthy API on private
`record-net`, embeds neither API nor SQLite, mounts no volume, and does not own
domain rules, a full-screen terminal UI, Compose lifecycle, or service state.

## Responsibilities

| Responsibility | Boundary owner | Explicitly outside this boundary |
|---|---|---|
| Parse one explicit command and options | CLI parser | Ambiguous positional guessing or hidden prompts in non-interactive use |
| Read `name`/`value` from arguments or explicitly selected bounded stdin | CLI input layer | Host filesystem access, arbitrary bind mounts, editing files, or persisting drafts |
| Invoke only the public Python SDK | CLI application adapter | HTTP calls outside the SDK or direct SQLite access |
| Render stable JSON or readable terminal output | CLI formatters | Reinterpreting API membership/order or changing data values |
| Map SDK outcomes to stable exit classes | CLI error mapper | Stack traces as normal user errors or success on partial failure |
| Preserve stdout/stderr separation | CLI process | Shell redirection, terminal configuration, or pager ownership |
| Package an exec-form image entrypoint and optional generated completion artifact | CLI release owner | Installing host executables or starting/managing the API implicitly |

## Inputs and outputs

| Direction | Counterparty | Interface or artifact | Validated by | Compatibility rule |
|---|---|---|---|---|
| Inbound | Shell user through `docker compose run --rm record-cli` | Arguments, flags, bounded stdin, terminal capability | Compose service plus CLI parser and SDK models | Commands/options and exit meaning follow CLI semantic versioning |
| Inbound | Python SDK | Models and SDK exceptions | CLI adapter | Only documented SDK public API may be consumed |
| Outbound | Python SDK | One method call per command action, plus paging calls for `--all` | CLI adapter | Uses ETags and search context without alteration |
| Outbound | stdout | Successful human or JSON data | Selected formatter | `--json` schema is stable within CLI major version; no diagnostics |
| Outbound | stderr | Warnings and problem diagnostics | Error formatter and redaction | No successful data; no record value unless user explicitly supplied it and validation echoes a safe locator rather than content |
| Outbound | Process caller | Stable integer exit status | Top-level dispatcher | Exit codes in `ARC-CTR-006` are invariant within v1 |

## Standalone meaning

For v2, standalone means all of the following:

- the CLI has its own minimal OCI image, semantic version, digest, SBOM, and
  exec-form entrypoint;
- the image contains the exact released SDK wheel but no API implementation,
  FastAPI/Uvicorn, SQLite state/tool, browser asset, compiler, or package
  manager cache;
- it is invoked from the Compose project as a disposable container, may run
  from any host working directory containing the release Compose material, and
  is removed after each invocation;
- it requires only Docker/Compose on the host and a healthy compatible
  `record-api` service reachable as `http://record-api:8000`; and
- direct `docker run`, host wheel/pipx installation, and native `recordctl`
  execution are unsupported deployment paths.

It does **not** mean a host binary, embedded database, offline mode,
self-starting service, or permission to manage other containers. Those are
different products and require accepted architecture changes.

## State and authority

| State or decision | System of record | Write authority | Recovery or reconciliation rule |
|---|---|---|---|
| Records | API/SQLite | CLI only through SDK/API | Refetch; never cache to disk |
| Service URL/image/network configuration | Rendered release Compose model | Release owner; not an ordinary CLI option | Correct/pin Compose release and rerun; CLI never discovers the host or Docker daemon |
| Command options and timeout | Current invocation plus fixed image defaults | Shell user within accepted range | Correct option and rerun |
| Search paging history | Current process memory | CLI | Discard on exit; restart query after cursor failure |
| Unsaved update input | Current process memory/stdin | Shell user | On conflict or transport failure, preserve source outside CLI if needed and rerun explicitly |
| Output files created by shell redirection | Shell/user | Outside CLI | CLI does not treat redirected output as authoritative storage |

## Invariants and failure boundaries

- Every invocation executes one named command, prints only contract-appropriate
  output, returns one stable exit code, and terminates. There is no background
  daemon or hidden persistent process.
- Machine-readable mode emits exactly one JSON document to stdout, including
  for an empty result. Diagnostics remain on stderr.
- The CLI must not automatically retry a create or update, prompt to force an
  overwrite, or turn an indeterminate write into a success/failure claim.
- Through the SDK, the CLI consumes the exact same `/api/v1` paths, methods,
  representations, problems, and search/navigation behavior as the web
  adapter. Private Compose DNS changes only the origin, never the API path.
- Update first retrieves the current record/ETag unless an explicit accepted
  future option supplies an ETag. It sends that ETag once. A conflict reports
  the condition and leaves the server state unchanged.
- `--value` and `--value-stdin` are mutually exclusive. Standard input is read
  only when explicitly selected. Host files are supplied by shell redirection
  to stdin; the CLI service receives no host bind mount and accepts no file
  path option in the supported v2 interface.
- The Compose service has `restart: "no"`, no published port, no data/backup/
  Docker-socket mount, private `record-net` only, read-only root filesystem,
  bounded tmpfs, all capabilities dropped, and numeric user `10001:10001`.
- Container exit status is the CLI exit status. Compose/daemon/image/network
  failures that prevent the process from starting are platform failures and
  must not be misreported as a CLI domain exit code.
- No command may reveal full record values in error messages, verbose logs,
  shell-completion output, or process titles beyond values the user explicitly
  placed on their command line.
- Empty search results are successful. Missing IDs, boundary results, invalid
  searches, conflicts, service failures, and unexpected failures remain
  distinguishable by exit status.

## Verification and change control

| Claim | Verification | Evidence location |
|---|---|---|
| CLI runs without host application install, web assets, or source checkout | Released Compose/image smoke test from a Docker-only host | Future CLI completion evidence |
| Commands expose all and only accepted capabilities | Command inventory and live end-to-end vectors | Required by `ARC-CTR-009` |
| JSON/stdout/stderr/exit behavior is stable | Golden process-level tests | Future CLI evidence |
| CLI contains no direct transport/database path | Dependency and source architecture test | Future CLI evidence |
| CLI cannot reach live state or Docker control plane | Rendered mount/network/capability inspection and negative runtime tests | Future container-security evidence |

Changes require CLI owner review and project architecture authority. Public
command, JSON, exit, configuration, or SDK-use changes require compatibility
analysis and synchronized contract/conformance updates.

## Revision record

| Date | Change | Authority |
|---|---|---|
| 2026-11-10 | Defined a standalone native-installable CLI boundary | User-authorized best-judgment architecture completion |
| 2026-11-10 | Replaced host installation with a minimal one-shot Compose CLI image and private service discovery | User's explicit full-Dockerization/no-host-services instruction |

