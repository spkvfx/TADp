from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))

from tadp_validate import (  # noqa: E402
    PROTECTED_ROOTS,
    build_protected_lock,
    parse_work_version,
    protected_lock_path,
    validate,
    validate_version_correlation,
)


class ValidatorTests(unittest.TestCase):
    def make_repository(self, root: Path) -> None:
        git_directory = root / ".git"
        git_directory.mkdir()
        (git_directory / "HEAD").write_text("ref: refs/heads/main\n", encoding="utf-8")
        (git_directory / "config").write_text("[core]\n\trepositoryformatversion = 0\n", encoding="utf-8")
        files = {
            ".gitattributes": "/template/** text eol=lf\n",
            "README.md": "# Project\n",
            "AGENTS.md": "# Instructions\n",
            "docs/README.md": "# Documentation\n",
            "docs/development/getting-started.md": "# Getting started\n",
            "docs/development/architecture-and-authority.md": "# Architecture\n",
            "docs/development/repository-layout.md": "# Layout\n",
            "docs/development/initiative-workflow.md": "# Workflow\n",
            "docs/development/git-and-codex-requirements.md": "# Requirements\n",
            "docs/development/validation-and-quality.md": "# Validation\n",
            "docs/development/developing-tadp.md": "# Development\n",
            "docs/development/adapting-other-tools.md": "# Adapting tools\n",
            "docs/guides/project-local-prompts-migration.md": "# Prompt migration\n",
            "docs/guides/protected-source-integrity-migration.md": "# Protection migration\n",
            "docs/guides/version-realization-correlation-migration.md": "# Correlation migration\n",
            "docs/guides/workflow-stage-0-13-migration.md": "# Workflow migration\n",
            "evidence/README.md": "# Evidence\n",
            "evidence/authoritative/README.md": "# Authoritative\n",
            "evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md": "# Suite\n",
            "evidence/authoritative/LLM/AGENTS.md": "# Protected invariants\n",
            "evidence/non-authoritative/README.md": "# Context\n",
            "initiatives/README.md": "# Initiatives\n",
            "products/README.md": "# Products\n",
            "prompts/AGENTS.md": "# Project-local prompt boundary\n",
            "prompts/README.md": "# Project-local prompts\n",
            "template/AGENTS.md": "# Protected templates\n",
            "template/initiatives/README.md": "# Initiative template\n",
            "template/initiatives/preparation-README.template.md": "# Preparation template\n",
            "template/initiatives/proposal/preparation-README.template.md": "# Proposal preparation template\n",
            "template/project/AGENTS.md": "# Instructions\n",
            "template/project/.gitattributes": "/template/** text eol=lf\n",
            "template/project/.githooks/pre-commit": "#!/bin/sh\n",
            "template/project/prompts/AGENTS.md": "# Project-local prompt boundary\n",
            "template/project/prompts/README.md": "# Project-local prompts\n",
            "template/project/evidence/non-authoritative/realizations/realization-suite-index.template.md": "# Suite template\n",
            "template/project/initiatives/version-correlation-migration-ledger.template.md": "# Ledger template\n",
            "template/prompts/README.md": "# Prompts\n",
            "template/prompts/WORKFLOW-CONTRACT.md": "# Contract\n",
            ".githooks/pre-commit": "#!/bin/sh\n",
            "tools/tadp_protect.py": "# Protection tool\n",
        }
        for number, name in enumerate(
            (
                "initiative_preparation",
                "proposal_creation",
                "proposal_alignment",
                "initiative_creation",
                "initiative_alignment",
                "initiative_assumption_review",
                "initiative_open_question_review",
                "initiative_acceptance",
                "initiative_sdk_api_alignment",
                "initiative_implementation_readiness_review",
                "initiative_execution",
                "design_delivery",
                "planning_delivery",
                "initiative_finalization",
            )
        ):
            files[f"template/prompts/{number:02d}_{name}.md"] = (
                "# Prompt\n\n## Example usage\n\nattached initiative\n\n"
                "WORKFLOW-CONTRACT.md\n\n```text\nUse {initiative}.\n```\n"
            )
        for number, name in enumerate(
            (
                "Evidence_Authority_Specification",
                "Initiative_Governance_Specification",
                "Invariant_Conflict_Register",
                "Initiative_Lifecycle_Specification",
                "Git_Workflow_Specification",
                "Initiative_Scope_Specification",
                "Human_Decision_Receipt_Specification",
                "Initiative_Workflow_Specification",
            ),
            start=1,
        ):
            files[f"evidence/authoritative/LLM/{number:02d}_Codex_{name}.md"] = "# Specification\n"
        files[
            "evidence/authoritative/LLM/09_Codex_Version_Realization_Initiative_Correlation_Specification.md"
        ] = "# Correlation specification\n"
        for name, content in files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        for protected_root in PROTECTED_ROOTS:
            lock = protected_lock_path(root, protected_root)
            lock.write_text(
                json.dumps(
                    build_protected_lock(root, protected_root, "test fixture"),
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )

    def make_initiative(
        self,
        root: Path,
        *,
        status: str = "Proposed",
        initiative_type: str = "planning",
        history: str = "| 2026-11-10 | Initial | Proposed | proposal | initial | start | pending |",
    ) -> Path:
        initiative = root / "initiatives" / "example"
        files = {
            "README.md": (
                "# Example\n\n"
                f"**Status:** {status}\n"
                f"**Initiative type:** `{initiative_type}`\n\n"
                "### Lifecycle history\n\n"
                "| Effective date or event | From | To | Authority or evidence | Claim revision | Reason and affected scope | Git commit |\n"
                "|---|---|---|---|---|---|---|\n"
                f"{history}\n"
            ),
            "proposal/README.md": "# Sources\n",
            "proposal/proposal.md": "# Proposal\n",
            "assumption.md": "# Assumptions\n",
            "scope-assessment.md": "# Scope\n",
            "architecture.md": "# Architecture\n",
            "source-mapping.md": "# Mapping\n\nAuthoritative evidence\n\nVerification evidence\n",
            "open-questions.md": "# Questions\n",
            "implementation-roadmap.md": "# Roadmap\n",
            "implementation-steps.md": "# Steps\n",
        }
        for name, content in files.items():
            path = initiative / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        return initiative

    def activate_correlation(
        self,
        root: Path,
        *,
        version: str = "v13.10",
        branch: str = "initiative/v13.10-example",
    ) -> tuple[Path, Path, Path]:
        profile = root / "project-profile.md"
        profile.write_text(
            "# Profile\n\n"
            "**Correlation revision effective point:** " + "f" * 40 + "\n\n"
            "**Correlation migration ledger:** "
            "[ledger](initiatives/version-correlation-migration-ledger.md)\n",
            encoding="utf-8",
        )

        initiatives = root / "initiatives"
        ledger = initiatives / "version-correlation-migration-ledger.md"
        ledger.write_text(
            "# Migration ledger\n\n"
            "| Legacy identity | Canonical identity | Suite | Initiative | Branch | Action | Authority/evidence | Ambiguity or blocker |\n"
            "|---|---|---|---|---|---|---|---|\n",
            encoding="utf-8",
        )

        initiative = self.make_initiative(root)
        base_commit = "a" * 40
        initiative_readme = initiative / "README.md"
        initiative_readme.write_text(
            "# Example\n\n"
            "**Initiative:** Example\n"
            "**Initiative ID:** INIT-PLN-001\n"
            "**Status:** Proposed\n"
            "**Initiative type:** `planning`\n"
            f"**Work version:** {version}\n"
            "**Realization suite ID:** RZN-001-EXAMPLE-SUITE\n"
            f"**Realization suite:** [RZN-001-EXAMPLE-SUITE](../../evidence/non-authoritative/realizations/{version}/00-RZN-001-EXAMPLE-suite-index.md)\n"
            "**Canonical project correlation:** [index](../initiative-index.md#initiative-and-correlation-register)\n"
            f"**Dedicated branch:** {branch}\n"
            "**Captured base branch:** main\n"
            f"**Captured base commit:** {base_commit}\n\n"
            "### Lifecycle history\n\n"
            "| Effective date or event | From | To | Authority or evidence | Claim revision | Reason and affected scope | Git commit |\n"
            "|---|---|---|---|---|---|---|\n"
            "| 2026-11-11 | Initial | Proposed | suite | initial | start | pending |\n",
            encoding="utf-8",
        )

        suite = (
            root
            / "evidence"
            / "non-authoritative"
            / "realizations"
            / version
            / "00-RZN-001-EXAMPLE-suite-index.md"
        )
        suite.parent.mkdir(parents=True, exist_ok=True)
        suite.write_text(
            "# Example realization suite\n\n"
            f"**Work version:** {version}\n"
            "**Suite ID:** RZN-001-EXAMPLE-SUITE\n"
            "**Status:** Recorded; non-authoritative proposal input\n"
            "**Initiative ID:** INIT-PLN-001\n"
            "**Initiative type:** `planning`\n"
            "**Initiative path:** [initiative](../../../../initiatives/example/)\n"
            f"**Dedicated branch:** {branch}\n"
            "**Captured base branch:** main\n"
            f"**Captured base commit:** {base_commit}\n"
            "**Canonical project correlation:** [index](../../../../initiatives/initiative-index.md#initiative-and-correlation-register)\n",
            encoding="utf-8",
        )

        index = initiatives / "initiative-index.md"
        index.write_text(
            "# Index\n\n## Initiative and correlation register\n\n"
            "| Work version | Realization suite | Initiative ID | Name | Type | Status | Dedicated branch | Captured base branch | Captured base commit | Predecessor or successor | Record location | Lifecycle evidence | Branch removal evidence | Owner | Next gate |\n"
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n"
            f"| {version} | [RZN-001-EXAMPLE-SUITE](../evidence/non-authoritative/realizations/{version}/00-RZN-001-EXAMPLE-suite-index.md) | INIT-PLN-001 | Example | planning | Proposed | {branch} | main | {base_commit} | None | [Initiative](example/README.md) | [Lifecycle](example/README.md#lifecycle-history) | Not applicable — active ref required | User | Acceptance |\n",
            encoding="utf-8",
        )

        status = initiatives / "status.md"
        status.write_text(
            "# Status\n\n"
            "| Work version | Initiative ID | Realization suite | Type | Status | Current milestone | Next gate | Blockers or holds | Status evidence | Owner | Last updated |\n"
            "|---|---|---|---|---|---|---|---|---|---|---|\n"
            f"| {version} | INIT-PLN-001 | RZN-001-EXAMPLE-SUITE | planning | Proposed | Prepared | Acceptance | None | [Index](initiative-index.md#initiative-and-correlation-register) | User | 2026-11-11 |\n",
            encoding="utf-8",
        )

        branch_ref = root / ".git" / "refs" / "heads" / Path(*branch.split("/"))
        branch_ref.parent.mkdir(parents=True, exist_ok=True)
        branch_ref.write_text("b" * 40 + "\n", encoding="utf-8")
        return initiative, suite, index

    def test_minimal_repository_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            self.assertEqual([], validate(root))

    def test_missing_project_prompt_directory_is_reported_precisely(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            (root / "prompts" / "AGENTS.md").unlink()
            (root / "prompts" / "README.md").unlink()
            (root / "prompts").rmdir()

            findings = validate(root)

            self.assertTrue(
                any(item.code == "TADP038" and item.path == "prompts" for item in findings)
            )

    def test_missing_project_prompt_file_is_reported_precisely(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            (root / "prompts" / "README.md").unlink()

            findings = validate(root)

            self.assertTrue(
                any(
                    item.code == "TADP038" and item.path == "prompts/README.md"
                    for item in findings
                )
            )

    def test_working_project_prompt_must_preserve_reusable_source(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            (root / "prompts" / "AGENTS.md").write_text(
                "# Different instructions\n", encoding="utf-8"
            )

            findings = validate(root)

            self.assertTrue(
                any(
                    item.code == "TADP040" and item.path == "prompts/AGENTS.md"
                    for item in findings
                )
            )

    def test_template_lock_records_project_prompt_sources(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            payload = json.loads(
                protected_lock_path(root, "template").read_text(encoding="utf-8")
            )

            self.assertIn("project/prompts/AGENTS.md", payload["files"])
            self.assertIn("project/prompts/README.md", payload["files"])

    def test_additional_project_local_prompt_is_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            (root / "prompts" / "review-one-initiative.md").write_text(
                "# Review one initiative\n\nNon-authoritative local work description.\n",
                encoding="utf-8",
            )

            self.assertEqual([], validate(root))
            payload = json.loads(
                protected_lock_path(root, "template").read_text(encoding="utf-8")
            )
            self.assertNotIn("prompts/review-one-initiative.md", payload["files"])

    def test_broken_link_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            (root / "README.md").write_text("[missing](missing.md)\n", encoding="utf-8")
            self.assertIn("TADP002", {item.code for item in validate(root)})

    def test_markdown_link_literal_in_fenced_code_is_ignored(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            (root / "README.md").write_text(
                "# Transcript\n\n```text\n[local](file:///C:/missing.md)\n```\n",
                encoding="utf-8",
            )
            self.assertNotIn("TADP002", {item.code for item in validate(root)})

    def test_unresolved_token_is_reported_outside_templates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            (root / "README.md").write_text("{{project_name}}\n", encoding="utf-8")
            self.assertIn("TADP003", {item.code for item in validate(root)})

    def test_inline_code_braces_are_not_unresolved_tokens(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            (root / "README.md").write_text(
                "# Contract\n\nUse `GET /records/{id}` with `\"rev-{decimal}\"`.\n",
                encoding="utf-8",
            )
            self.assertNotIn("TADP003", {item.code for item in validate(root)})

    def test_modified_template_source_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            (root / "template" / "AGENTS.md").write_text(
                "# Unexpected template edit\n", encoding="utf-8"
            )
            self.assertIn("TADP024", {item.code for item in validate(root)})

    def test_protected_text_hash_ignores_line_ending_conversion(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            (root / "template" / "AGENTS.md").write_bytes(
                b"# Protected templates\r\n"
            )
            self.assertNotIn("TADP024", {item.code for item in validate(root)})

    def test_modified_llm_invariant_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            invariant = (
                root
                / "evidence"
                / "authoritative"
                / "LLM"
                / "01_Codex_Evidence_Authority_Specification.md"
            )
            invariant.write_text("# Unauthorized invariant edit\n", encoding="utf-8")
            self.assertIn("TADP024", {item.code for item in validate(root)})

    def test_new_protected_source_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            (root / "template" / "unexpected.md").write_text(
                "# Unexpected\n", encoding="utf-8"
            )
            self.assertIn("TADP025", {item.code for item in validate(root)})

    def test_missing_locked_source_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            (root / "template" / "AGENTS.md").unlink()
            self.assertIn("TADP026", {item.code for item in validate(root)})

    def test_missing_protected_source_lock_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            protected_lock_path(root, "template").unlink()
            self.assertIn("TADP023", {item.code for item in validate(root)})

    def test_incomplete_initiative_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            initiative = root / "initiatives" / "example"
            initiative.mkdir()
            (initiative / "architecture.md").write_text("# Architecture\n", encoding="utf-8")
            self.assertIn("TADP004", {item.code for item in validate(root)})

    def test_git_repository_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            (root / ".git" / "HEAD").unlink()
            (root / ".git" / "config").unlink()
            (root / ".git").rmdir()
            self.assertIn("TADP012", {item.code for item in validate(root)})

    def test_protocol_root_may_be_contained_in_parent_git_repository(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository = Path(directory)
            protocol = repository / "protocol"
            protocol.mkdir()
            self.make_repository(protocol)
            for path in (protocol / ".git").iterdir():
                path.unlink()
            (protocol / ".git").rmdir()
            git_directory = repository / ".git"
            git_directory.mkdir()
            (git_directory / "HEAD").write_text(
                "ref: refs/heads/main\n", encoding="utf-8"
            )
            (git_directory / "config").write_text(
                "[core]\n\trepositoryformatversion = 0\n", encoding="utf-8"
            )
            (repository / "AGENTS.md").write_text(
                "# Repository instructions\n", encoding="utf-8"
            )
            self.assertEqual([], validate(protocol))

    def test_enclosing_git_root_does_not_supply_prompt_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository = Path(directory)
            protocol = repository / "protocol"
            protocol.mkdir()
            self.make_repository(protocol)
            for path in (protocol / ".git").iterdir():
                path.unlink()
            (protocol / ".git").rmdir()
            git_directory = repository / ".git"
            git_directory.mkdir()
            (git_directory / "HEAD").write_text(
                "ref: refs/heads/main\n", encoding="utf-8"
            )
            (git_directory / "config").write_text(
                "[core]\n\trepositoryformatversion = 0\n", encoding="utf-8"
            )
            (repository / "AGENTS.md").write_text(
                "# Repository instructions\n", encoding="utf-8"
            )
            parent_prompts = repository / "prompts"
            parent_prompts.mkdir()
            (parent_prompts / "AGENTS.md").write_text(
                "# Parent prompt instructions\n", encoding="utf-8"
            )
            (parent_prompts / "README.md").write_text(
                "# Parent prompts\n", encoding="utf-8"
            )
            (protocol / "prompts" / "AGENTS.md").unlink()
            (protocol / "prompts" / "README.md").unlink()
            (protocol / "prompts").rmdir()

            findings = validate(protocol)

            self.assertTrue(
                any(item.code == "TADP038" and item.path == "prompts" for item in findings)
            )

    def test_parent_git_repository_requires_root_agents_entry_point(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository = Path(directory)
            protocol = repository / "protocol"
            protocol.mkdir()
            self.make_repository(protocol)
            for path in (protocol / ".git").iterdir():
                path.unlink()
            (protocol / ".git").rmdir()
            git_directory = repository / ".git"
            git_directory.mkdir()
            (git_directory / "HEAD").write_text(
                "ref: refs/heads/main\n", encoding="utf-8"
            )
            (git_directory / "config").write_text(
                "[core]\n\trepositoryformatversion = 0\n", encoding="utf-8"
            )
            self.assertIn("TADP022", {item.code for item in validate(protocol)})

    def test_illegal_lifecycle_transition_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            self.make_initiative(
                root,
                status="Completed",
                history="| 2026-11-10 | Proposed | Completed | none | initial | skipped | pending |",
            )
            self.assertIn("TADP009", {item.code for item in validate(root)})

    def test_completed_initiative_requires_completion_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            self.make_initiative(root, status="Completed")
            self.assertIn("TADP010", {item.code for item in validate(root)})

    def test_resolved_decision_requires_linked_receipt(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            initiative = self.make_initiative(root)
            (initiative / "assumption.md").write_text(
                "# Assumptions\n\n| ID | Disposition |\n|---|---|\n| A-01 | Confirmed |\n",
                encoding="utf-8",
            )
            codes = {item.code for item in validate(root)}
            self.assertIn("TADP013", codes)
            self.assertIn("TADP014", codes)

    def test_numbered_prompt_requires_shared_contract(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            prompt = root / "template" / "prompts" / "00_initiative_preparation.md"
            prompt.write_text(
                "# Prompt\n\n## Example usage\n\nattached initiative\n\nUse {initiative}.\n",
                encoding="utf-8",
            )
            self.assertIn("TADP016", {item.code for item in validate(root)})

    def test_accepted_initiative_requires_acceptance_receipt(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            self.make_initiative(
                root,
                status="Accepted",
                history=(
                    "| 2026-11-10 | Initial | Proposed | proposal | initial | start | c1 |\n"
                    "| 2026-11-11 | Proposed | Accepted | decision | v1 | accepted | c2 |"
                ),
            )
            self.assertIn("TADP020", {item.code for item in validate(root)})

    def test_accepted_initiative_with_linked_acceptance_receipt_passes_gate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            initiative = self.make_initiative(
                root,
                status="Accepted",
                history=(
                    "| 2026-11-10 | Initial | Proposed | proposal | initial | start | c1 |\n"
                    "| 2026-11-11 | Proposed | Accepted | "
                    "[receipt](decision-receipts/acceptance.md) | v1 | accepted | c2 |"
                ),
            )
            receipts = initiative / "decision-receipts"
            receipts.mkdir()
            (receipts / "acceptance.md").write_text(
                "# Acceptance\n\n**Disposition:** Accepted\n", encoding="utf-8"
            )
            codes = {item.code for item in validate(root)}
            self.assertNotIn("TADP020", codes)
            self.assertNotIn("TADP021", codes)

    def test_in_progress_design_requires_delivery_record(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            initiative = self.make_initiative(
                root,
                status="In progress",
                initiative_type="design",
                history=(
                    "| 2026-11-10 | Initial | Proposed | proposal | initial | start | c1 |\n"
                    "| 2026-11-11 | Proposed | Accepted | decision | v1 | accepted | c2 |\n"
                    "| 2026-11-12 | Accepted | In progress | delivery | v1 | began | c3 |"
                ),
            )
            receipts = initiative / "decision-receipts"
            receipts.mkdir()
            (receipts / "acceptance.md").write_text(
                "# Acceptance\n\n**Disposition:** Accepted\n", encoding="utf-8"
            )
            readme = initiative / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8")
                + "\n[Acceptance receipt](decision-receipts/acceptance.md)\n",
                encoding="utf-8",
            )
            findings = validate(root)
            self.assertIn("TADP019", {item.code for item in findings})
            self.assertNotIn("TADP020", {item.code for item in findings})
            self.assertNotIn("TADP021", {item.code for item in findings})

    def test_work_version_syntax_and_numeric_ordering(self) -> None:
        canonical = ("v0.0", "v0.1", "v1.0", "v1.1", "v13.8", "v13.9", "v13.10")
        parsed = [parse_work_version(value) for value in canonical]
        self.assertEqual(
            [(0, 0), (0, 1), (1, 0), (1, 1), (13, 8), (13, 9), (13, 10)],
            parsed,
        )
        self.assertGreater(parse_work_version("v13.10"), parse_work_version("v13.9"))
        for value in ("v0", "0.1", "v01.0", "v1.01", "v1.0.0"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                parse_work_version(value)

    def test_complete_governed_correlation_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            self.activate_correlation(root)
            self.assertEqual([], validate_version_correlation(root))

    def test_noncanonical_governed_version_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            self.activate_correlation(
                root,
                version="v13.01",
                branch="initiative/v13.01-example",
            )
            self.assertIn(
                "TADP028", {item.code for item in validate_version_correlation(root)}
            )

    def test_duplicate_version_and_branch_mapping_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            _, _, index = self.activate_correlation(root)
            row = index.read_text(encoding="utf-8").splitlines()[-1]
            index.write_text(
                index.read_text(encoding="utf-8") + row + "\n", encoding="utf-8"
            )
            self.assertIn(
                "TADP030", {item.code for item in validate_version_correlation(root)}
            )

    def test_missing_reciprocal_metadata_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            initiative, _, _ = self.activate_correlation(root)
            readme = initiative / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8").replace(
                    "**Work version:** v13.10", "**Work version:** v13.9"
                ),
                encoding="utf-8",
            )
            self.assertIn(
                "TADP032", {item.code for item in validate_version_correlation(root)}
            )

    def test_orphan_realization_suite_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            self.activate_correlation(root)
            orphan = (
                root
                / "evidence"
                / "non-authoritative"
                / "realizations"
                / "v0.1"
                / "00-RZN-ORPHAN-suite-index.md"
            )
            orphan.parent.mkdir(parents=True)
            orphan.write_text(
                "# Orphan\n\nNon-authoritative proposal input.\n", encoding="utf-8"
            )
            self.assertIn(
                "TADP031", {item.code for item in validate_version_correlation(root)}
            )

    def test_orphan_prepared_initiative_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            self.activate_correlation(root)
            orphan = root / "initiatives" / "orphan" / "README.md"
            orphan.parent.mkdir()
            orphan.write_text(
                "# Orphan\n\n**Work version:** v0.1\n\n"
                "**Initiative ID:** INIT-PLN-999\n",
                encoding="utf-8",
            )
            self.assertIn(
                "TADP031", {item.code for item in validate_version_correlation(root)}
            )

    def test_active_initiative_requires_live_branch(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            self.activate_correlation(root)
            (root / ".git" / "refs" / "heads" / "initiative" / "v13.10-example").unlink()
            self.assertIn(
                "TADP035", {item.code for item in validate_version_correlation(root)}
            )

    def test_absent_historical_branch_requires_removal_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            initiative, _, index = self.activate_correlation(root)
            index.write_text(
                index.read_text(encoding="utf-8").replace(
                    "| planning | Proposed |", "| planning | Superseded |"
                ),
                encoding="utf-8",
            )
            readme = initiative / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8").replace(
                    "**Status:** Proposed", "**Status:** Superseded"
                ),
                encoding="utf-8",
            )
            (root / ".git" / "refs" / "heads" / "initiative" / "v13.10-example").unlink()
            self.assertIn(
                "TADP035", {item.code for item in validate_version_correlation(root)}
            )

    def test_absent_historical_branch_with_removal_evidence_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            initiative, _, index = self.activate_correlation(root)
            evidence = initiative / "decision-receipts" / "branch-removal.md"
            evidence.parent.mkdir()
            evidence.write_text("# Authorized branch removal\n", encoding="utf-8")
            index.write_text(
                index.read_text(encoding="utf-8")
                .replace("| planning | Proposed |", "| planning | Superseded |")
                .replace(
                    "Not applicable — active ref required",
                    "[Removal authority](example/decision-receipts/branch-removal.md)",
                ),
                encoding="utf-8",
            )
            readme = initiative / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8").replace(
                    "**Status:** Proposed", "**Status:** Superseded"
                ),
                encoding="utf-8",
            )
            (root / ".git" / "refs" / "heads" / "initiative" / "v13.10-example").unlink()
            self.assertNotIn(
                "TADP035", {item.code for item in validate_version_correlation(root)}
            )

    def test_deferred_legacy_row_is_an_actionable_warning(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            _, _, index = self.activate_correlation(root)
            ledger = root / "initiatives" / "version-correlation-migration-ledger.md"
            ledger.write_text(
                ledger.read_text(encoding="utf-8")
                + "| Legacy v13.10 | Not allocated — must not be inferred | "
                "[suite](../evidence/non-authoritative/realizations/v13.10/00-RZN-001-EXAMPLE-suite-index.md) | "
                "[initiative](example/README.md) | `initiative/v13.10-example` | Deferred | "
                "source; governing workflow revision: pre-correlation | "
                "unresolved; re-entry or migration condition: explicit decision |\n",
                encoding="utf-8",
            )
            index.write_text(
                index.read_text(encoding="utf-8").replace(
                    "[Lifecycle](example/README.md#lifecycle-history)",
                    "[Legacy disposition](version-correlation-migration-ledger.md)",
                ),
                encoding="utf-8",
            )
            findings = validate_version_correlation(root)
            self.assertIn("TADP033", {item.code for item in findings})
            self.assertNotIn("TADP034", {item.code for item in findings})

    def test_mixed_legacy_and_canonical_identity_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            self.activate_correlation(root)
            ledger = root / "initiatives" / "version-correlation-migration-ledger.md"
            ledger.write_text(
                ledger.read_text(encoding="utf-8")
                + "| Legacy v13.10 | v13.10 | "
                "[suite](../evidence/non-authoritative/realizations/v13.10/00-RZN-001-EXAMPLE-suite-index.md) | "
                "[initiative](example/README.md) | `initiative/v13.10-example` | Deferred | "
                "source; governing workflow revision: pre-correlation | "
                "partial mapping; re-entry or migration condition: explicit decision |\n",
                encoding="utf-8",
            )
            self.assertIn(
                "TADP034", {item.code for item in validate_version_correlation(root)}
            )

    def test_canonical_row_cannot_mix_legacy_tuple_components(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            self.activate_correlation(root)
            ledger = root / "initiatives" / "version-correlation-migration-ledger.md"
            ledger.write_text(
                ledger.read_text(encoding="utf-8")
                + "| Legacy example | Not allocated — must not be inferred | "
                "[suite](../evidence/non-authoritative/realizations/v13.10/00-RZN-001-EXAMPLE-suite-index.md) | "
                "[initiative](example/README.md) | `legacy/v13.10-example` | Deferred | "
                "source; governing workflow revision: pre-correlation | "
                "unresolved; re-entry or migration condition: explicit decision |\n",
                encoding="utf-8",
            )
            self.assertIn(
                "TADP034", {item.code for item in validate_version_correlation(root)}
            )

    def test_realization_suite_must_preserve_non_authoritative_standing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            _, suite, _ = self.activate_correlation(root)
            suite.write_text(
                suite.read_text(encoding="utf-8").replace(
                    "non-authoritative proposal input", "proposal input"
                ),
                encoding="utf-8",
            )
            self.assertIn(
                "TADP037", {item.code for item in validate_version_correlation(root)}
            )

    def test_branch_must_retain_exact_version_token(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            self.activate_correlation(root, branch="initiative/example")
            self.assertIn(
                "TADP035", {item.code for item in validate_version_correlation(root)}
            )

    def test_branch_version_substring_is_not_an_exact_token(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            self.activate_correlation(root, branch="initiative/v13.100-example")
            self.assertIn(
                "TADP035", {item.code for item in validate_version_correlation(root)}
            )

    def test_preparation_skeleton_does_not_require_status_row(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            initiative, _, _ = self.activate_correlation(root)
            readme = initiative / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8")
                + "\n## Preparation state\n\nStage 0 identity only.\n",
                encoding="utf-8",
            )
            (root / "initiatives" / "status.md").unlink()
            codes = {item.code for item in validate_version_correlation(root)}
            self.assertNotIn("TADP029", codes)
            self.assertNotIn("TADP032", codes)

    def test_complete_correlation_requires_status_view(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            self.activate_correlation(root)
            (root / "initiatives" / "status.md").unlink()
            self.assertIn(
                "TADP029", {item.code for item in validate_version_correlation(root)}
            )

    def test_status_view_must_match_canonical_correlation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            self.activate_correlation(root)
            status = root / "initiatives" / "status.md"
            status.write_text(
                status.read_text(encoding="utf-8").replace(
                    "| planning | Proposed |", "| planning | Accepted |"
                ),
                encoding="utf-8",
            )
            self.assertIn(
                "TADP032", {item.code for item in validate_version_correlation(root)}
            )


if __name__ == "__main__":
    unittest.main()

