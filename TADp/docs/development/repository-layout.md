# Repository layout

The copied baseline follows the installed project shape. All folders have
README.md navigation, and applicable record shapes use .template.md.

~~~text
project-root/
  AGENTS.md
  README.md
  project-profile.template.md
  .githooks/
  decisions/                  project-wide decisions when actually made
  docs/                       project-use guides
  evidence/                   binding and contextual sources and record shapes
  initiatives/                coordination and common initiative record shapes
    initiative-README.template.md
    architecture.template.md
    proposal/
    decision-receipts/
    implementation/
    design/
    planning/
  products/                   product record shape; no delivered products
  prompts/                    project-local prompt boundary
  tools/                      runtime verification and synchronization
  tests/                      project test navigation; no imported test results
  template/                   complete protected distribution library
~~~

The distribution source project/template/ contains only a README placeholder
to prevent recursive embedding. Installation supplies the full outer library
at that path once. The library keeps workflow prompts, coverage and this project
baseline; initiative record shapes have one owner under its project/initiatives/.

Instantiating an initiative creates its actual records at the declared
initiatives/<scope>/<type>/<id-and-slug>/ destination. Template filenames never
create those records automatically. Preserve legacy project paths and claims
until explicitly authorized migration. Keep TADp maintenance work outside
this project's baseline.
