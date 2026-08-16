import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools/validate_platform_enablement_triage.py"


class PlatformEnablementTriageValidatorTests(unittest.TestCase):
    def complete_row(self, record_id, disposition="platform constraint", **changes):
        values = {
            "record_id": record_id,
            "claim": f"[{record_id}](facts/{record_id}.md) — Fixture claim.",
            "disposition": disposition,
            "decision": "first powered Linux bring-up",
            "consequence": "The interface could be configured incorrectly.",
            "safe_default": "Leave the interface unconfigured.",
            "deadline": "before first powered bring-up",
            "isolation_reason": "Isolation permits requirements work.",
            "check": "Review the approved schematic evidence.",
            "evidence": "documentary / medium / disputed",
            "approval": "Not applicable",
        }
        values.update(changes)
        return (
            "| {record_id} | {claim} | {disposition} | {decision} | "
            "{consequence} | {safe_default} | {deadline} | {isolation_reason} | "
            "{check} | {evidence} | {approval} |"
        ).format(**values)

    def run_fixture(self, rows):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory)
            tools = fixture / "tools"
            facts = fixture / "docs/evidence/hardware/facts"
            tools.mkdir(parents=True)
            facts.mkdir(parents=True)
            shutil.copy2(VALIDATOR, tools / VALIDATOR.name)
            for record_id in ("HW-001", "HW-002", "HW-068"):
                (facts / f"{record_id}.md").write_text(
                    f"# {record_id}\n\n- Record ID: {record_id}\n- Status: disputed\n"
                )
            registry = facts.parent / "platform-enablement-triage.md"
            registry.write_text(
                "# Platform-enablement triage\n\n"
                "| ID | Claim | Disposition | Decision or later milestone | "
                "Wrong-claim consequence | Safe default | Deadline | "
                "Why isolation cannot permit progress | Cheapest reliable check | "
                "Evidence/confidence/status | Owner approval |\n"
                "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
                + "\n".join(rows)
                + "\n"
            )
            return subprocess.run(
                [sys.executable, str(tools / VALIDATOR.name)],
                cwd=fixture,
                capture_output=True,
                text=True,
                check=False,
            )

    def test_accepts_one_complete_row_per_material_disputed_fact(self):
        result = self.run_fixture(
            rows=[self.complete_row("HW-001"), self.complete_row("HW-002")]
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_missing_material_fact(self):
        result = self.run_fixture(rows=[self.complete_row("HW-001")])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing triage rows: HW-002", result.stderr)

    def test_rejects_duplicate_fact(self):
        row = self.complete_row("HW-001")
        result = self.run_fixture(
            rows=[row, row, self.complete_row("HW-002")]
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate triage row: HW-001", result.stderr)

    def test_rejects_unknown_disposition(self):
        rows = [
            self.complete_row("HW-001", disposition="maybe"),
            self.complete_row("HW-002"),
        ]
        result = self.run_fixture(rows=rows)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("HW-001: invalid disposition maybe", result.stderr)

    def test_blocker_requires_non_applicable_safe_default_and_complete_rationale(self):
        row = self.complete_row(
            "HW-001",
            disposition="platform blocker",
            safe_default="Not applicable — isolation cannot permit progress.",
            isolation_reason="-",
        )
        result = self.run_fixture(rows=[row, self.complete_row("HW-002")])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("HW-001: blocker requires isolation rationale", result.stderr)


if __name__ == "__main__":
    unittest.main()
