from pathlib import Path
import re
import sys
from collections import Counter


ROOT = Path(__file__).resolve().parents[1]
FACTS = ROOT / "docs/evidence/hardware/facts"
REGISTRY = ROOT / "docs/evidence/hardware/platform-enablement-triage.md"
OWNER_REMOVED_FIXTURE = ROOT / "docs/evidence/hardware/owner-removed-fixture.txt"
OWNER_REMOVED = {"HW-068", "HW-069", "HW-070", "HW-079", "HW-081"}
ALLOWED_DISPOSITIONS = {
    "platform blocker",
    "platform constraint",
    "integration dependency",
    "brewing-device dependency",
    "non-blocking reference",
    "candidate removal",
}
ALLOWED_DEADLINES = {
    "before requirements",
    "before first powered bring-up",
    "before named integration",
    "deferred",
}
BLOCKER_SAFE_DEFAULT = "Not applicable — isolation cannot permit progress."
INTEGRATION_MILESTONES = {
    "SOM-MCU integration",
    "display/touch integration",
    "hardware-control integration",
}
UNFINISHED_VALUES = {"-", "todo", "tbd", "fixme", "placeholder", "unknown"}
PLACEHOLDER = re.compile(r"<[^>]+>")


def fields(text):
    result = {}
    current = None
    for line in text.splitlines():
        match = re.match(r"^- ([^:]+):(?:\s*(.*))?$", line)
        if match:
            current = match.group(1)
            result[current] = (match.group(2) or "").strip()
        elif current and line.startswith("  "):
            result[current] = (result[current] + " " + line.strip()).strip()
        else:
            current = None
    return result


def fail(message):
    print(message, file=sys.stderr)
    raise SystemExit(1)


def incomplete(value):
    return (
        not value
        or value.strip().lower() in UNFINISHED_VALUES
        or bool(PLACEHOLDER.search(value))
    )


fact_statuses = {}
fact_records = {}
for path in sorted(FACTS.glob("HW-[0-9][0-9][0-9].md")):
    data = fields(path.read_text())
    record_id = data.get("Record ID", path.stem)
    fact_statuses[record_id] = data.get("Status", "")
    fact_records[record_id] = data

if not fact_statuses:
    fail("no hardware fact records")

owner_removed = OWNER_REMOVED
if OWNER_REMOVED_FIXTURE.exists():
    owner_removed = {
        line.strip()
        for line in OWNER_REMOVED_FIXTURE.read_text().splitlines()
        if line.strip()
    }
elif not OWNER_REMOVED <= set(fact_statuses):
    fail("production owner-removal set is incomplete")
for record_id in owner_removed:
    if fact_statuses.get(record_id) != "disputed":
        fail(f"{record_id}: owner-removed record must exist and remain disputed")

expected = {
    record_id
    for record_id, status in fact_statuses.items()
    if status == "disputed" and record_id not in owner_removed
}

registry_text = REGISTRY.read_text()
rows = {}
for line in registry_text.splitlines():
    if not re.match(r"^\|\s*HW-[0-9]{3}\s*\|", line):
        continue
    columns = [column.strip() for column in line.strip().strip("|").split("|")]
    if len(columns) != 11:
        fail(f"malformed triage row: {line}")
    record_id = columns[0]
    if record_id in rows:
        fail(f"duplicate triage row: {record_id}")
    rows[record_id] = columns

row_ids = set(rows)
owner_removed_rows = sorted(row_ids & owner_removed)
if owner_removed_rows:
    fail("owner-removed IDs in material table: " + ", ".join(owner_removed_rows))
extra = sorted(row_ids - expected)
if extra:
    fail("extra triage rows: " + ", ".join(extra))
missing = sorted(expected - row_ids)
if missing:
    fail("missing triage rows: " + ", ".join(missing))

for record_id in sorted(rows):
    (
        _, claim, disposition, decision, consequence, safe_default, deadline,
        isolation_reason, reliable_check, evidence, approval,
    ) = rows[record_id]
    values = columns = rows[record_id][1:]
    if any(incomplete(value) for value in values):
        if disposition == "platform blocker" and incomplete(isolation_reason):
            fail(f"{record_id}: blocker requires isolation rationale")
        fail(f"{record_id}: empty or unfinished triage value")
    claim_prefix = f"[{record_id}](facts/{record_id}.md) — "
    if not claim.startswith(claim_prefix) or incomplete(claim.removeprefix(claim_prefix)):
        fail(f"{record_id}: broken fact link")
    if claim.removeprefix(claim_prefix) != fact_records[record_id].get("Claim", ""):
        fail(f"{record_id}: claim does not match record")
    if disposition not in ALLOWED_DISPOSITIONS:
        fail(f"{record_id}: invalid disposition {disposition}")
    if deadline not in ALLOWED_DEADLINES:
        fail(f"{record_id}: invalid deadline {deadline}")
    expected_evidence = " / ".join(
        (
            fact_records[record_id].get("Evidence type", ""),
            fact_records[record_id].get("Confidence", ""),
            fact_records[record_id].get("Status", ""),
        )
    )
    if evidence != expected_evidence:
        fail(f"{record_id}: evidence/confidence/status does not match record")
    if disposition == "platform blocker":
        if deadline not in {"before requirements", "before first powered bring-up"}:
            fail(f"{record_id}: blocker has invalid deadline {deadline}")
        if incomplete(isolation_reason):
            fail(f"{record_id}: blocker requires isolation rationale")
        if safe_default != BLOCKER_SAFE_DEFAULT:
            fail(f"{record_id}: blocker requires non-applicable safe default")
    elif safe_default == BLOCKER_SAFE_DEFAULT:
        fail(f"{record_id}: non-blocker uses blocker-only safe default")
    if disposition == "platform constraint" and deadline != "before first powered bring-up":
        fail(f"{record_id}: platform constraint requires first-bring-up deadline")
    if disposition == "integration dependency" and deadline != "before named integration":
        fail(f"{record_id}: integration dependency requires named-integration deadline")
    if disposition == "integration dependency" and decision not in INTEGRATION_MILESTONES:
        fail(f"{record_id}: invalid integration milestone {decision}")
    if disposition in {"brewing-device dependency", "non-blocking reference", "candidate removal"} and deadline != "deferred":
        fail(f"{record_id}: {disposition} requires deferred deadline")
    if disposition == "candidate removal":
        if approval != "Pending owner decision":
            fail(f"{record_id}: candidate removal requires pending owner decision")
    elif approval != "Not applicable" and not re.fullmatch(r"\[[^]]+\]\([^)]+\)", approval):
        fail(f"{record_id}: invalid owner approval reference")

counts = Counter(row[2] for row in rows.values())
expected_summary = (
    f"Disposition totals: {len(rows)} rows — "
    f"{counts['platform blocker']} `platform blocker`, "
    f"{counts['platform constraint']} `platform constraint`, "
    f"{counts['integration dependency']} `integration dependency`, "
    f"{counts['brewing-device dependency']} `brewing-device dependency`, "
    f"{counts['non-blocking reference']} `non-blocking reference`, and "
    f"{counts['candidate removal']} `candidate removal`."
)
summary_count = registry_text.count("Disposition totals:")
if summary_count != 1:
    fail("expected exactly one disposition summary")
if expected_summary not in " ".join(registry_text.split()):
    fail("disposition summary does not match rows")

owner_section_match = re.search(
    r"^## Owner-removed non-material disputed facts\n(.*?)(?=^## |\Z)",
    registry_text,
    re.MULTILINE | re.DOTALL,
)
if not owner_section_match:
    fail("owner-removal reconciliation section missing")
owner_section = owner_section_match.group(1)
for record_id in owner_removed:
    if owner_section.count(f"[{record_id}](facts/{record_id}.md)") != 1:
        fail(f"{record_id}: owner-removal reconciliation missing or duplicated")
if "Authority:" not in owner_section and not OWNER_REMOVED_FIXTURE.exists():
    fail("owner-removal authority missing")

coverage_match = re.search(
    r"^## Initial-gate coverage gaps\n(.*?)(?=^## Gate decision)",
    registry_text,
    re.MULTILINE | re.DOTALL,
)
if coverage_match and re.search(r"^- ", coverage_match.group(1), re.MULTILINE):
    if "**Linux-image requirements and independent design remain blocked.**" not in registry_text:
        fail("coverage gaps require a blocked gate outcome")

if not OWNER_REMOVED_FIXTURE.exists():
    derived = {
        ROOT / "docs/evidence/hardware/baseline.md": "remain blocked",
        ROOT / "docs/evidence/hardware/verification-register.md": "Requirements remain blocked",
        ROOT / "docs/milestones/001-hardware-baseline.md": "requirements remain blocked",
    }
    count_fragment = (
        f"{counts['platform blocker']} platform blockers, "
        f"{counts['platform constraint']} platform constraints, "
        f"{counts['integration dependency']} integration dependencies, "
        f"{counts['brewing-device dependency']} brewing-device dependencies, "
        f"{counts['non-blocking reference']} non-blocking references, and "
        f"{counts['candidate removal']} candidate removals"
    )
    for path, outcome in derived.items():
        normalized = " ".join(path.read_text().split())
        if normalized.count(count_fragment) != 1:
            fail(f"{path}: derived disposition counts do not match")
        if outcome not in path.read_text():
            fail(f"{path}: derived gate outcome does not match")
    roadmap = (ROOT / "docs/roadmap.md").read_text()
    if "complete initial-gate coverage and explicitly permits requirements work" not in roadmap:
        fail("roadmap activation does not match gate rule")

print(f"validated {len(rows)} material disputed-fact triage rows")
