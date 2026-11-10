from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))

from tadp_protect import mutate_locks, paths_for_roots  # noqa: E402
from tadp_validate import (  # noqa: E402
    PROTECTED_ROOTS,
    protected_lock_path,
    validate_protected_sources,
)


class ProtectionToolTests(unittest.TestCase):
    def make_sources(self, root: Path) -> None:
        (root / "template").mkdir(parents=True)
        (root / "template" / "record.template.md").write_text(
            "# Template\n", encoding="utf-8"
        )
        invariant_root = root / "evidence" / "authoritative" / "LLM"
        invariant_root.mkdir(parents=True)
        (invariant_root / "00_index.md").write_text("# Invariants\n", encoding="utf-8")

    def test_initialize_creates_valid_locks_with_authority(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_sources(root)

            result = mutate_locks(
                root,
                action="initialize",
                protected_roots=PROTECTED_ROOTS,
                authority="decision DR-001",
            )

            self.assertEqual(0, result)
            self.assertEqual([], validate_protected_sources(root))
            for protected_root in PROTECTED_ROOTS:
                payload = json.loads(
                    protected_lock_path(root, protected_root).read_text(encoding="utf-8")
                )
                self.assertEqual("decision DR-001", payload["authority"])

    def test_initialize_refuses_to_replace_an_existing_lock(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_sources(root)
            lock = protected_lock_path(root, "template")
            lock.write_text("{}\n", encoding="utf-8")

            result = mutate_locks(
                root,
                action="initialize",
                protected_roots=("template",),
                authority="decision DR-001",
            )

            self.assertEqual(2, result)
            self.assertEqual("{}\n", lock.read_text(encoding="utf-8"))

    def test_refresh_requires_an_existing_lock(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_sources(root)

            result = mutate_locks(
                root,
                action="refresh",
                protected_roots=("template",),
                authority="decision DR-002",
            )

            self.assertEqual(2, result)
            self.assertFalse(protected_lock_path(root, "template").exists())

    def test_staged_paths_are_scoped_to_the_tadp_root(self) -> None:
        git_root = Path("/repository")
        tadp_root = git_root / "protocol"
        paths = {
            "protocol/template/record.template.md",
            "protocol/evidence/authoritative/LLM/00_index.md",
            "template/outside.md",
        }

        grouped = paths_for_roots(paths, git_root, tadp_root)

        self.assertEqual(
            ["protocol/template/record.template.md"], grouped["template"]
        )
        self.assertEqual(
            ["protocol/evidence/authoritative/LLM/00_index.md"],
            grouped["evidence/authoritative/LLM"],
        )


if __name__ == "__main__":
    unittest.main()
