# Traceable Architecture Design Protocol (TADp)

TADp manages LLM-assisted software development through evidence, focused
initiatives and explicit human decisions. It records why work exists, who
approved it, what changed and what verification supports the result.
It requires **Git and Codex**; Python 3 runs the bundled checks.

## Adopt TADp in a project

Start with [implementing TADp in projects](docs/implementing-tadp-in-projects.md),
then use the portable [installation guide](protocol/docs/development/getting-started.md).
The [protocol overview](protocol/README.md) explains authority and traceability;
the [protocol documentation index](protocol/docs/README.md) covers project
operation, validation and migration. Begin with one narrow pilot initiative.
Structural validation does not establish human acceptance or product correctness.

## Contribute to this repository

Use the [repository documentation index](docs/README.md),
[checkout layout](docs/repository-layout.md) and
[contributor guide](docs/developing-tadp.md).
The installed [TADp development project](TADp/README.md) owns development
governance and history. Candidate protocol work belongs in `TADp/protocol/`;
`protocol/` is the distribution. The project-owned
[development workflow](TADp/docs/development/tadp-development-workflow.md)
governs qualification and controlled delivery.

The documentation split's portable revisions are prepared in the candidate
workspace, pending acceptance and authorized delivery. The links above still
lead to the current distributed guides. See the
[preparation and delivery map](TADp/evidence/non-authoritative/documentation-split/preparation.md)
for exact status and boundaries.

## Example repository

The example has a separate [repository](https://github.com/spkvfx/TADp-example).
Its clone URL is `https://github.com/spkvfx/TADp-example.git`. These supplied
links identify its location; rebuild status, protocol adoption, feature parity
and application behavior have not been verified by this documentation review.
For TADp adoption, follow [getting started](protocol/docs/development/getting-started.md).
