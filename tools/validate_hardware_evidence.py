from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FACTS = ROOT / "docs/evidence/hardware/facts"
INDEX = ROOT / "docs/evidence/hardware/fact-index.md"
ALLOWED = {"proposed", "provisionally accepted", "verified", "disputed", "superseded"}
REQUIRED = {
    "Record ID", "Status", "Claim", "Scope or hardware revision",
    "Source", "Source location", "Extraction date", "Extractor",
    "Evidence type", "Verification method", "Independent confirmation",
    "Confidence", "Known conflicts or limitations", "Dependent decisions",
    "Verification cost", "Basis for high confidence",
    "Why verification is time-consuming", "How delay would impede progress",
    "Provisional-use qualification", "Decisions blocked until verified",
    "Next verification action", "Recorded by and date", "Verified by and date",
}

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

files = sorted(FACTS.glob("HW-[0-9][0-9][0-9].md"))
if not files:
    fail("no hardware fact records")
expected = [f"HW-{number:03d}" for number in range(1, len(files) + 1)]
actual = [path.stem for path in files]
if actual != expected:
    fail(f"fact IDs are not contiguous: {actual}")
index_text = INDEX.read_text()
index_rows = {}
for line in index_text.splitlines():
    if not re.match(r"^\|\s*HW-[0-9]{3}\s*\|", line):
        continue
    columns = [column.strip() for column in line.strip().strip("|").split("|")]
    if len(columns) != 6:
        fail(f"malformed fact-index row: {line}")
    row_id, _, _, row_status, _, record_link = columns
    if row_id in index_rows:
        fail(f"{row_id}: duplicate fact-index row")
    if record_link != f"[record](facts/{row_id}.md)":
        fail(f"{row_id}: index record link does not match row ID")
    index_rows[row_id] = row_status

if sorted(index_rows) != expected:
    fail(f"fact-index IDs do not match record IDs: {sorted(index_rows)}")

for path, record_id in zip(files, expected):
    text = path.read_text()
    if re.search(r"<[^>]+>", text):
        fail(f"{path}: untouched template prompt")
    data = fields(text)
    missing = sorted(name for name in REQUIRED if not data.get(name))
    if missing:
        fail(f"{path}: empty or missing fields: {', '.join(missing)}")
    if data["Record ID"] != record_id:
        fail(f"{path}: Record ID does not match filename")
    if data["Status"] not in ALLOWED:
        fail(f"{path}: invalid status {data['Status']}")
    if index_rows[record_id] != data["Status"]:
        fail(
            f"{record_id}: index status {index_rows[record_id]} "
            f"does not match record status {data['Status']}"
        )
    link = f"facts/{record_id}.md"
    if index_text.count(link) != 1:
        fail(f"{record_id}: expected exactly one index link")
print(f"validated {len(files)} hardware fact records")
