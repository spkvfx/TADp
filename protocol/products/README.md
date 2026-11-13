# Products

Products are output material placed in a declared destination. They include
executable code, scripts, SDKs, APIs, product documentation, configuration,
schemas, and other delivered artifacts.

This directory is an optional index or placement. A product does not need to
live beneath a directory named `products`; record its actual repository path,
package, API route, documentation site, or other destination in its governing
initiative.

Products are authoritative for the actual output at their declared placement.
They must align with accepted initiatives and `../evidence/authoritative`. Record
an observed mismatch as a conflict; do not silently rewrite an invariant or
initiative to make the product appear aligned.

Use the [product-record source](../template/project/products/product-record.template.md)
when an output has a declared destination. Copy it outside protected
`template/`, either into this directory or beside the product, and record the
actual path/package/API placement, revision, owner, governing initiative and
specification, binding evidence, and verification. A record may describe a
planned output if its status and missing verification remain explicit; it must
not describe planned behavior as delivered.

The initiative's declared type controls which work can create the output.
Implementation creates or changes accepted products; design delivers
specifications and planning delivers initiative-local evidence. Documentation
is classified by its role, so an explanatory product guide and a specification
of required behavior need different ownership. See the
[workflow guide](../docs/development/initiative-workflow.md).

Record only observed verification for the exact claim and environment. A
passing structural validator cannot establish product behavior, deployment,
release, or production readiness. Completion and the product record should
link the same delivered revision and verification without replacing each
other's ownership.
