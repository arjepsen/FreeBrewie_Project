from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
FACTS = ROOT / "docs/evidence/hardware/facts"
REGISTRY = ROOT / "docs/evidence/hardware/platform-enablement-triage.md"
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
UNFINISHED = re.compile(
    r"(?:\b(?:todo|tbd|fixme|placeholder|unknown)\b|<[^>]+>)", re.IGNORECASE
)


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
    return not value or value == "-" or bool(UNFINISHED.search(value))


fact_statuses = {}
for path in sorted(FACTS.glob("HW-[0-9][0-9][0-9].md")):
    data = fields(path.read_text())
    record_id = data.get("Record ID", path.stem)
    fact_statuses[record_id] = data.get("Status", "")

if not fact_statuses:
    fail("no hardware fact records")

expected = {
    record_id
    for record_id, status in fact_statuses.items()
    if status == "disputed" and record_id not in OWNER_REMOVED
}

rows = {}
for line in REGISTRY.read_text().splitlines():
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
owner_removed_rows = sorted(row_ids & OWNER_REMOVED)
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
    if claim != f"[{record_id}](facts/{record_id}.md)":
        fail(f"{record_id}: broken fact link")
    if disposition not in ALLOWED_DISPOSITIONS:
        fail(f"{record_id}: invalid disposition {disposition}")
    if deadline not in ALLOWED_DEADLINES:
        fail(f"{record_id}: invalid deadline {deadline}")
    if disposition == "platform blocker":
        if deadline not in {"before requirements", "before first powered bring-up"}:
            fail(f"{record_id}: blocker has invalid deadline {deadline}")
        if incomplete(isolation_reason):
            fail(f"{record_id}: blocker requires isolation rationale")
        if safe_default != BLOCKER_SAFE_DEFAULT:
            fail(f"{record_id}: blocker requires non-applicable safe default")
    elif safe_default == BLOCKER_SAFE_DEFAULT:
        fail(f"{record_id}: non-blocker uses blocker-only safe default")
    if disposition == "candidate removal":
        if approval != "Pending owner decision":
            fail(f"{record_id}: candidate removal requires pending owner decision")
    elif approval != "Not applicable" and not re.fullmatch(r"\[[^]]+\]\([^)]+\)", approval):
        fail(f"{record_id}: invalid owner approval reference")

print(f"validated {len(rows)} material disputed-fact triage rows")
