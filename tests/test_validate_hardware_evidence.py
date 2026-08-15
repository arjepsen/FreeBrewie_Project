import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools/validate_hardware_evidence.py"
FACT = ROOT / "docs/evidence/hardware/facts/HW-001.md"


class HardwareEvidenceValidatorTests(unittest.TestCase):
    def run_fixture(self, index_status):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory)
            tools = fixture / "tools"
            facts = fixture / "docs/evidence/hardware/facts"
            tools.mkdir(parents=True)
            facts.mkdir(parents=True)
            shutil.copy2(VALIDATOR, tools / VALIDATOR.name)
            shutil.copy2(FACT, facts / FACT.name)
            (facts.parent / "fact-index.md").write_text(
                "# Hardware fact index\n\n"
                "| ID | Claim summary | Category | Status | Primary source | Record |\n"
                "| --- | --- | --- | --- | --- | --- |\n"
                f"| HW-001 | Fixture claim. | Fixture | {index_status} | Fixture | "
                "[record](facts/HW-001.md) |\n"
            )
            return subprocess.run(
                [sys.executable, str(tools / VALIDATOR.name)],
                cwd=fixture,
                capture_output=True,
                text=True,
                check=False,
            )

    def test_rejects_index_status_that_differs_from_record(self):
        result = self.run_fixture("disputed")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn(
            "HW-001: index status disputed does not match record status verified",
            result.stderr,
        )


if __name__ == "__main__":
    unittest.main()
