# Platform-Enablement Evidence Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Classify every material disputed hardware fact by its actual effect on clean-slate Linux platform enablement and replace the raw disputed-fact count with a reviewed, enforceable evidence gate.

**Architecture:** Keep canonical evidence in the existing atomic fact records and add one derived Markdown triage registry for dependency and scheduling decisions. A dedicated Python validator derives the expected material-disputed set from the fact records, excludes only the five already owner-removed audio facts, and enforces complete, unique, structurally valid triage rows. Derived summaries and milestone language consume the reviewed registry without changing hardware-fact status.

**Tech Stack:** Markdown, Python 3 standard library, `unittest`, POSIX shell utilities, Git.

## Global Constraints

- Do not design or implement a Linux image, SOM application, MCU firmware, communication protocol, UI, brewing logic, or hardware-control behavior.
- Do not select a distribution, build system, kernel, bootloader, filesystem, update mechanism, UI toolkit, or application architecture.
- Do not convert a historical implementation choice into a requirement or design input.
- Do not inspect sources beyond the already approved read-only evidence boundary.
- Do not authorize or perform powered tests, continuity measurements, probing, output activation, or physical handling.
- Keep every hardware fact's evidence and verification status canonical in `docs/evidence/hardware/facts/`; triage records dependency and schedule only.
- A fact is a blocker only when the row names the exact decision, credible consequence, why isolation cannot permit progress, verification deadline, and cheapest reliable check.
- An unresolved capability remains disabled, isolated, preserved, untouched, or blocked according to its recorded safe default.
- A candidate scope removal remains pending until the project owner explicitly approves its reason and date.
- Preserve the current hardware-fact totals and statuses unless a separately evidenced correction is required: 108 total, 23 verified, 85 disputed; the five owner-removed audio facts are disputed but non-material to this gate.

---

## Planned file map

- `docs/evidence/hardware/platform-enablement-triage.md`: single registry containing scope rules, all 80 material disputed-fact dispositions, blocker register, first-bring-up constraints, deferrals, removals, and the gate decision.
- `tools/validate_platform_enablement_triage.py`: deterministic registry parser and cross-check against canonical fact status.
- `tests/test_validate_platform_enablement_triage.py`: isolated fixtures proving missing, duplicate, invalid, and incomplete rows fail.
- `docs/evidence/hardware/baseline.md`: concise link to the triage result and corrected blocked-decision summary.
- `docs/evidence/hardware/verification-register.md`: disposition totals, owner-removal reconciliation, and downstream dependency summary.
- `docs/milestones/001-hardware-baseline.md`: consequential completion criteria and evidence-based gate decision.
- `docs/roadmap.md`: activation wording for Linux-image requirements after the gate decision, without activating or designing that milestone.

### Task 1: Create the triage registry contract and validator

**Files:**
- Create: `docs/evidence/hardware/platform-enablement-triage.md`
- Create: `tools/validate_platform_enablement_triage.py`
- Create: `tests/test_validate_platform_enablement_triage.py`

**Interfaces:**
- Consumes: canonical `- Status:` fields in `docs/evidence/hardware/facts/HW-*.md` and the existing owner-removal set `HW-068`, `HW-069`, `HW-070`, `HW-079`, `HW-081`.
- Produces: table columns `ID`, `Claim`, `Disposition`, `Decision or later milestone`, `Wrong-claim consequence`, `Safe default`, `Deadline`, `Why isolation cannot permit progress`, `Cheapest reliable check`, `Evidence/confidence/status`, and `Owner approval`.
- Produces: allowed dispositions `platform blocker`, `platform constraint`, `integration dependency`, `brewing-device dependency`, `non-blocking reference`, and `candidate removal`.
- Produces: allowed deadlines `before requirements`, `before first powered bring-up`, `before named integration`, and `deferred`.

- [ ] **Step 1: Write validator fixture tests that fail without the validator**

Create `tests/test_validate_platform_enablement_triage.py` with a temporary repository fixture containing three disputed facts, one owner-removed ID, and a registry table. Include these tests:

```python
def test_accepts_one_complete_row_per_material_disputed_fact(self):
    result = self.run_fixture(rows=[self.complete_row("HW-001"), self.complete_row("HW-002")])
    self.assertEqual(result.returncode, 0, result.stderr)

def test_rejects_missing_material_fact(self):
    result = self.run_fixture(rows=[self.complete_row("HW-001")])
    self.assertNotEqual(result.returncode, 0)
    self.assertIn("missing triage rows: HW-002", result.stderr)

def test_rejects_duplicate_fact(self):
    row = self.complete_row("HW-001")
    result = self.run_fixture(rows=[row, row, self.complete_row("HW-002")])
    self.assertNotEqual(result.returncode, 0)
    self.assertIn("duplicate triage row: HW-001", result.stderr)

def test_rejects_unknown_disposition(self):
    rows = [self.complete_row("HW-001", disposition="maybe"), self.complete_row("HW-002")]
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
```

The fixture must invoke a copied validator through `subprocess.run`, matching the isolation pattern in `tests/test_validate_hardware_evidence.py`. Its owner-removed fixture ID must be excluded by an environment-independent fixture constant or fixture metadata, never by weakening the production expected-set check.

- [ ] **Step 2: Run the tests and verify the expected failure**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_validate_platform_enablement_triage.py' -v
```

Expected: FAIL because `tools/validate_platform_enablement_triage.py` does not exist.

- [ ] **Step 3: Create the registry skeleton**

Create `docs/evidence/hardware/platform-enablement-triage.md` with:

- the purpose and clean-slate boundary from the approved design;
- definitions of all six dispositions and four deadlines;
- the exact eleven-column table header listed in this task's Interfaces block;
- no factual rows yet;
- empty derived headings: `Platform blockers`, `First-bring-up constraints`, `Deferred work`, `Candidate removals`, `Owner-removed non-material disputed facts`, and `Gate decision`; and
- an explicit statement that fact files remain canonical and table rows do not promote status.

- [ ] **Step 4: Implement the minimal validator**

Create `tools/validate_platform_enablement_triage.py` using only the standard library. It must:

```python
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
```

Parse canonical fact files with the same `- Field: value` convention used by `validate_hardware_evidence.py`. Derive `expected` as every `disputed` record minus `OWNER_REMOVED`. Parse only rows beginning with `| HW-NNN |` and require exactly eleven columns. Reject missing, extra, or duplicate IDs; invalid dispositions or deadlines; broken `[HW-NNN](facts/HW-NNN.md)` links; empty values, a lone hyphen, common unfinished-work markers, and any owner-removed ID in the material table.

For `platform blocker`, require deadline `before requirements` or `before first powered bring-up`, require the isolation-rationale column to explain why isolation cannot permit progress, and require safe default exactly `Not applicable — isolation cannot permit progress.` For every other disposition, reject that blocker-only safe-default phrase and require a concrete safe default. For `candidate removal`, require owner approval exactly `Pending owner decision`; for all other categories accept `Not applicable` or an exact recorded approval reference.

Print:

```text
validated 80 material disputed-fact triage rows
```

using the computed count rather than a hard-coded `80`.

- [ ] **Step 5: Run the focused tests**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_validate_platform_enablement_triage.py' -v
```

Expected: all five tests PASS.

- [ ] **Step 6: Confirm the empty production registry fails closed**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 tools/validate_platform_enablement_triage.py
```

Expected: FAIL listing all 80 missing material disputed IDs. This failure is intentional until Tasks 2 and 3 populate the registry.

- [ ] **Step 7: Commit the contract and failing production skeleton**

```bash
git add docs/evidence/hardware/platform-enablement-triage.md tools/validate_platform_enablement_triage.py tests/test_validate_platform_enablement_triage.py
git commit -m "docs: define platform evidence triage contract"
```

### Task 2: Classify compute-platform and SOM-facing facts

**Files:**
- Modify: `docs/evidence/hardware/platform-enablement-triage.md`
- Review: `docs/evidence/hardware/facts/HW-004.md` through `HW-018.md`
- Review: `docs/evidence/hardware/facts/HW-072.md`, `HW-075.md` through `HW-078.md`, `HW-080.md`, `HW-082.md`, `HW-083.md`, `HW-092.md`, and `HW-093.md`
- Review: `docs/evidence/hardware/sources.md`
- Review: `docs/evidence/hardware/som-carrier.md`
- Review: `docs/evidence/hardware/som-mcu-interconnect.md`

**Interfaces:**
- Consumes: the eleven-column registry contract and approved platform-enablement areas.
- Produces: proposition-specific rows for each reviewed disputed fact, with no status changes.
- Produces: the initial blocker and first-bring-up constraint registers for boot/storage, display/touch, console/recovery, SOM-carrier control, and MCU isolation.

- [ ] **Step 1: Build a dependency worksheet from canonical records**

For every reviewed ID, extract its exact claim, dependent decisions, known limitations, verification method, confidence, and next verification action. Do not use topical-summary wording when it differs from the atomic record.

- [ ] **Step 2: Test each candidate blocker against the four-part blocker rule**

For each fact that appears relevant to boot, recovery, storage preservation, display/touch bring-up, or safe MCU isolation, write a private review note answering:

1. What exact requirements or first-boot decision depends on it?
2. What credible failure or safety consequence follows if it is wrong?
3. Why can the interface not simply remain disabled, untouched, or isolated?
4. What is the cheapest reliable check and when must it occur?

If answer 3 has a safe isolation path, classify the fact as `platform constraint` or a later dependency, not a blocker.

- [ ] **Step 3: Add the compute/SOM-facing table rows**

Use exact `[HW-NNN](facts/HW-NNN.md)` links. Keep every disputed proposition conditional. Use these later-milestone names consistently where applicable:

- `Linux-image requirements`
- `first powered Linux bring-up`
- `SOM-MCU integration`
- `display/touch integration`
- `hardware-control integration`

Do not assume that current Linux enumeration proves physical routing, that old GPIO aliases remain valid, or that an observed runtime mode selects the future configuration.

- [ ] **Step 4: Populate only supported blocker and constraint summaries**

Under `Platform blockers`, list only rows satisfying all blocker criteria and link back to their table IDs. Under `First-bring-up constraints`, state explicit prohibitions such as leaving an unresolved GPIO unconfigured, preserving identified media, or not relying on an unverified interface. Do not prescribe the mechanism the future image will use.

- [ ] **Step 5: Run partial deterministic checks**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 tools/validate_platform_enablement_triage.py
```

Expected: FAIL only with the still-missing brewing-device/interconnect IDs. It must report no duplicate, malformed, invalid-category, or incomplete compute/SOM rows.

- [ ] **Step 6: Run a clean-slate wording audit**

Run targeted searches in the registry for `should use`, `reuse`, `adopt`, `architecture`, `state machine`, `protocol`, `Qt`, `LVGL`, `Buildroot`, `Debian`, `EXT3`, and kernel-version strings. Every hit must be an exclusion, historical observation, or explicit non-selection; revise any prescriptive hit.

- [ ] **Step 7: Commit the compute-platform classification**

```bash
git add docs/evidence/hardware/platform-enablement-triage.md
git commit -m "docs: classify platform-facing hardware disputes"
```

### Task 3: Classify brewing-device and remaining interconnect facts

**Files:**
- Modify: `docs/evidence/hardware/platform-enablement-triage.md`
- Review: `docs/evidence/hardware/facts/HW-019.md` through `HW-067.md`
- Review: `docs/evidence/hardware/facts/HW-073.md`, `HW-074.md`, and `HW-084.md` through `HW-091.md`
- Review: `docs/evidence/hardware/brewing-devices.md`
- Review: `docs/evidence/hardware/mcu.md`

**Interfaces:**
- Consumes: the same registry contract and Task 2's fixed later-milestone names.
- Produces: all remaining material rows so the table covers exactly 80 disputed facts.
- Produces: deferred-work and candidate-removal registers without changing canonical status.

- [ ] **Step 1: Reconcile the exact remaining ID set**

Compute disputed IDs from fact records, subtract the five owner-removed audio IDs and all Task 2 rows, and record the resulting Task 3 worklist in the task report. Do not rely only on numeric ranges.

- [ ] **Step 2: Separate platform safety constraints from brewing behavior**

For each remaining fact, ask whether an unconfigured SOM during minimal Linux bring-up could drive the relevant MCU or load. If the fact affects only future MCU firmware, actuator behavior, sensing, calibration, or brewing operation, use `integration dependency` or `brewing-device dependency`. Use `platform constraint` only when Linux-side bring-up must explicitly avoid or preserve something despite not controlling brewing hardware.

- [ ] **Step 3: Add every remaining material row**

Name one concrete safe default per unresolved fact. Appropriate defaults include keeping the physical load disconnected, leaving the interface unconfigured, prohibiting output activation, treating a connector as unknown, or deferring calibration. Do not state that a line is electrically safe unless verified evidence says so.

- [ ] **Step 4: Complete deferred-work and removal registers**

Group deferrals under `SOM-MCU integration`, `hardware-control integration`, and `brewing-device characterization`. In `Owner-removed non-material disputed facts`, list HW-068, HW-069, HW-070, HW-079, and HW-081 with the existing dated audio-removal authority. Put only genuinely new proposals under `Candidate removals`, each marked `Pending owner decision`.

- [ ] **Step 5: Run the production validator**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 tools/validate_platform_enablement_triage.py
```

Expected:

```text
validated 80 material disputed-fact triage rows
```

- [ ] **Step 6: Independently count dispositions**

Use a separate short Python or `awk` command—not the production validator—to print the row total and category counts. Confirm the total is 80 and record the exact category distribution in the registry summary.

- [ ] **Step 7: Commit the complete classification**

```bash
git add docs/evidence/hardware/platform-enablement-triage.md
git commit -m "docs: complete hardware dispute triage"
```

### Task 4: Derive the gate decision and revise milestone controls

**Files:**
- Modify: `docs/evidence/hardware/platform-enablement-triage.md`
- Modify: `docs/evidence/hardware/baseline.md`
- Modify: `docs/evidence/hardware/verification-register.md`
- Modify: `docs/milestones/001-hardware-baseline.md`
- Modify: `docs/roadmap.md`

**Interfaces:**
- Consumes: the validated 80-row registry and exact disposition counts.
- Produces: one consistent gate decision, revised completion criteria, and traceable downstream constraints.
- Produces no Linux-image technical selection and does not activate implementation.

- [ ] **Step 1: Derive the gate outcome from classified rows**

The gate decision must use this rule:

- Linux-image requirements may begin only when no unresolved row with deadline `before requirements` remains a `platform blocker`.
- First powered bring-up remains prohibited for every unresolved `before first powered bring-up` blocker.
- Constraints and later dependencies do not block requirements work, but their safe defaults remain mandatory.

Record the actual result; do not force a pass. If requirements remain blocked, list only the exact blocking IDs and checks. If requirements may begin, list all capabilities that remain prohibited.

- [ ] **Step 2: Update baseline and verification summaries**

Add the registry link, disposition counts, blocker IDs, and the gate outcome. Keep canonical hardware counts at 108 total, 23 verified, and 85 disputed. Explain that disposition changes schedule and dependency, not evidence status.

- [ ] **Step 3: Revise milestone 001 completion criteria**

Replace the rule that every material fact must be verified with consequential criteria:

- every material disputed fact has one reviewed disposition;
- no unresolved `before requirements` platform blocker remains when Linux-image requirements are activated;
- every first-bring-up blocker and constraint remains explicit and enforceable;
- all deferrals and removals are traceable; and
- consistency, provenance, clean-slate, and safety reviews pass.

Retain milestone 001 as `active` if first-bring-up blockers or required classification/approval work remains. Do not mark it complete merely because Linux-image requirements may start.

- [ ] **Step 4: Update roadmap activation wording**

State that Linux-image requirements and design may become active when the evidence gate permits it, even if milestone 001 remains active for first-bring-up or later integration evidence. Keep Linux implementation inactive until a separately approved Linux-image design exists.

- [ ] **Step 5: Run all deterministic tests**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py' -v
PYTHONDONTWRITEBYTECODE=1 python3 tools/validate_hardware_evidence.py
PYTHONDONTWRITEBYTECODE=1 python3 tools/validate_platform_enablement_triage.py
git diff --check
```

Expected: all tests PASS; validators report 108 fact records and 80 triage rows; `git diff --check` exits 0.

- [ ] **Step 6: Cross-check all derived counts and IDs**

Independently compare the triage category counts, blocker list, first-bring-up constraint IDs, owner-removal list, baseline, verification register, milestone, and roadmap. Resolve every mismatch before committing.

- [ ] **Step 7: Commit the gate integration**

```bash
git add docs/evidence/hardware/platform-enablement-triage.md docs/evidence/hardware/baseline.md docs/evidence/hardware/verification-register.md docs/milestones/001-hardware-baseline.md docs/roadmap.md
git commit -m "docs: integrate platform enablement evidence gate"
```

### Task 5: Final independent consistency, boundary, and safety review

**Files:**
- Review: all files changed since commit `18512a2`
- Modify only: files listed in Tasks 1-4 when a verified inconsistency is found

**Interfaces:**
- Consumes: complete branch diff, both validators, all tests, and the approved design.
- Produces: review-ready branch with exact evidence-disposition coverage and no prohibited design leakage.

- [ ] **Step 1: Inspect the complete diff**

Run:

```bash
git diff --stat 18512a2..HEAD
git diff --check 18512a2..HEAD
git diff 18512a2..HEAD -- docs/evidence/hardware docs/milestones/001-hardware-baseline.md docs/roadmap.md tools tests
```

Read the complete diff. Confirm classification does not alter fact status or present disputed claims as verified.

- [ ] **Step 2: Run fresh full validation**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py' -v
PYTHONDONTWRITEBYTECODE=1 python3 tools/validate_hardware_evidence.py
PYTHONDONTWRITEBYTECODE=1 python3 tools/validate_platform_enablement_triage.py
git status --short
```

Expected: all tests PASS, validators report 108 and 80, and the worktree is clean after any corrective commit.

- [ ] **Step 3: Audit blocker quality**

For every `platform blocker`, verify the row names a real decision, credible consequence, isolation rationale, deadline, and reliable check. Challenge any blocker that can be converted into a safe constraint. Confirm the gate decision follows only from the remaining `before requirements` blockers.

- [ ] **Step 4: Audit clean-slate and safety boundaries**

Search changed files for legacy technical selections and for verbs that could authorize physical action. Confirm every legacy configuration mention is historical/non-selected and every measurement or activation remains prohibited unless separately approved. Confirm no Linux, firmware, protocol, UI, or brewing design was introduced.

- [ ] **Step 5: Request independent review and correct findings**

Request a reviewer against base `18512a2` and the final head. Require findings-first reporting for completeness, disposition consistency, blocker rigor, gate logic, clean-slate compliance, and safety scope. Correct every Critical or Important finding, rerun Steps 1-4, and commit corrections with a narrowly descriptive message.

- [ ] **Step 6: Push for owner review**

After a clean independent review and fresh verification, push `platform-enablement-gate`. Do not merge without the project owner's explicit approval.
