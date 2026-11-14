# Validation and quality

Use the configured Python interpreter and run checks from the project Git root.
These inert examples do not execute when this guide is read:

~~~text
python tools/tadp_protect.py check .
python tools/tadp_validate.py .
python tools/tadp_validate.py . --json
~~~

The protection check is read-only and reports source-lock drift. The validator
checks installed structure, links, records and objective workflow evidence.
Exit 0 means no structural errors, 1 means findings, and 2 means rejected
arguments or an invalid root. Warnings remain visible. Passing checks does not
authenticate decisions, establish adoption or prove product correctness.

## Protected-source workflow

Preserve the installed template and authoritative-suite locks. Never refresh a
lock merely to silence drift. A deliberate source update needs exact human
authority, coherent consumer changes and applicable verification before the
governed lock procedure. Ordinary project work populates declared instances
rather than protected reusable sources.

## Project verification

Add project-specific tests only for actual accepted work. The baseline supplies
a tests README, not TADp's development regression suite or fictional results.
Record actual passed, failed, skipped and unperformed checks with their scope
and limitations. Consult [runtime tools](../../tools/README.md) for supported
commands and synchronization safeguards.
