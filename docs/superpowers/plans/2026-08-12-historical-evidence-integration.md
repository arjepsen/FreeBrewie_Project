# Historical Evidence Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Integrate the approved `OldStuff` archive and fresh runtime captures into milestone 001's unified, traceable hardware-evidence registry without importing legacy implementation design.

**Architecture:** Existing `HW-xxx` records remain the canonical atomic evidence store. New evidence updates matching records and creates only narrowly scoped new records; indexes and summaries are derived afterward. Runtime, historical configuration, reverse-engineering, manufacturer, and owner-observation evidence remain explicitly distinct.

**Tech Stack:** Markdown, Python 3 standard library validator, POSIX shell utilities, Git.

**Execution status (2026-08-15):** Tasks 1-3 and the corrective implementation
portion of Task 4 are complete. The final scoped branch re-review, PR approval,
merge, and post-merge validation in Task 4 Step 5 remain pending.

**Provenance terminology erratum:** The planned-file-map and Task 2 shorthand
originally used “captured” for both fresh runtime reports and retained archive
artifacts. Canonical evidence records control: `NewOlimexDebianInfo.txt` and
`ReBrewieLegacyRuntimeInfo.txt` are owner-attested fresh runtime captures;
`uImage` and the older-image `dmesg.txt` are artifacts retained in the supplied
archive. “Retained” describes archive placement only and makes no forensic,
factory-acquisition, or untouched-image claim.

## Global Constraints

- Do not design or implement the Linux image, SOM application, MCU firmware, communication protocol, brewing logic, or UI.
- Do not use historical implementation architecture, control logic, state machines, protocol design, module structure, or source code as requirements or design inputs.
- Keep `/home/anders/Documents/OldStuff` external, read-only, unimported, and outside all builds.
- Treat `ReBrewieLegacyRuntimeInfo.txt` as a community-edited ReBrewie userspace on the legacy Brewie Linux platform, not as an untouched factory image.
- Treat `brewie.dts` as an owner-created experimental overlay for the later Olimex/Debian image, not as an original Brewie artifact or authoritative physical wiring record.
- A runtime capture may verify a narrowly scoped runtime observation; it cannot by itself verify a physical wire or electrical characteristic.
- Repetition within one configuration lineage is corroboration, not independent physical verification.
- Preserve exact local paths and SHA-256 hashes for every selected local artifact.
- Do not perform or request powered measurements, continuity checks, actuator commands, or hardware reconnection.
- Keep milestone 001 active unless its measurable completion criteria genuinely pass after integration.

---

## Planned file map

- `docs/evidence/hardware/facts/HW-007.md`: current runtime touch identity.
- `docs/evidence/hardware/facts/HW-008.md`: current runtime touch bus/address.
- `docs/evidence/hardware/facts/HW-101.md`: fresh ReBrewie kernel/platform runtime, with retained archive corroboration.
- `docs/evidence/hardware/facts/HW-102.md`: fresh ReBrewie Buildroot userspace identity.
- `docs/evidence/hardware/facts/HW-103.md`: fresh ReBrewie active SD/MMC partition and mount layout.
- `docs/evidence/hardware/facts/HW-104.md`: fresh ReBrewie PCF8563 RTC runtime observation.
- `docs/evidence/hardware/facts/HW-105.md`: fresh Olimex/Debian kernel and SOM-model runtime observation.
- `docs/evidence/hardware/facts/HW-106.md`: fresh Olimex/Debian watchdog runtime observation.
- `docs/evidence/hardware/facts/HW-107.md`: fresh USB Wi-Fi runtime enumeration/use.
- `docs/evidence/hardware/facts/HW-108.md`: ttyS0/ttyS1 enumeration shared by legacy and modern captures.
- `docs/evidence/hardware/fact-index.md`: canonical index of all 108 records.
- `docs/evidence/hardware/sources.md`: exact provenance and selection ledger.
- `docs/evidence/hardware/local-historical-evidence-review.md`: bounded archive review.
- `docs/evidence/hardware/baseline.md`: overall baseline and status counts.
- `docs/evidence/hardware/som-carrier.md`: compute-platform summary.
- `docs/evidence/hardware/som-mcu-interconnect.md`: UART/runtime distinction.
- `docs/evidence/hardware/capabilities.md`: runtime resource and platform observations.
- `docs/evidence/hardware/verification-register.md`: remaining conflicts, debt, and blocked decisions.
- `docs/milestones/001-hardware-baseline.md`: evidence-based completion review.
- `tools/validate_hardware_evidence.py`: existing deterministic consistency validator; modify only if it cannot validate the approved record structure.

### Task 1: Reconcile sources and existing touch facts

**Files:**
- Modify: `docs/evidence/hardware/sources.md`
- Modify: `docs/evidence/hardware/local-historical-evidence-review.md`
- Modify: `docs/evidence/hardware/facts/HW-007.md`
- Modify: `docs/evidence/hardware/facts/HW-008.md`

**Interfaces:**
- Consumes: the approved design, hashes already recorded in `sources.md`, and exact lines in `NewOlimexDebianInfo.txt` and `ReBrewieLegacyRuntimeInfo.txt`.
- Produces: final source classifications and narrowly verified current runtime touch records used by the index and summaries.

- [x] **Step 1: Confirm source hashes have not changed**

Run:

    sha256sum /home/anders/Documents/OldStuff/NewOlimexDebianInfo.txt
    sha256sum /home/anders/Documents/OldStuff/ReBrewieLegacyRuntimeInfo.txt
    sha256sum /home/anders/Documents/OldStuff/brewie.dts

Expected hashes:

    1abc86106395e27b3cd6e1a80f13692a03cc77625f609cd53fd6730baeb86933
    e734165cae681b785ecfb373a73c38178fc44a3f216510115961c402bb242d78
    06d56de96b826e13d2c95070aea218021bf755ff00f3023ff81a6a5a2a345f7f

- [x] **Step 2: Audit the source classifications**

Confirm `sources.md` states all of the following:

- both fresh captures are owner-requested read-only runtime captures;
- ReBrewie is community-edited and not an untouched factory image;
- `brewie.dts` is the owner's later experimental overlay;
- exact local paths and hashes are present;
- excluded legacy implementation material remains excluded.

Do not add application, firmware, recipe, protocol, or control-flow sources.

- [x] **Step 3: Narrow and verify HW-007**

Change HW-007's claim to the dated runtime proposition:

    During the fresh 2026-08-12 Olimex/Debian boot, Linux identified the
    attached touchscreen controller as Goodix ID 911, version 1060.

Set status to `verified`, evidence type to `direct`, and cite
`NewOlimexDebianInfo.txt` lines 334-348 plus its hash. Retain the limitation that
runtime identification does not verify package marking, supply wiring,
interrupt/reset pins, or electrical limits.

- [x] **Step 4: Narrow and verify HW-008**

Change HW-008's claim to:

    During the fresh 2026-08-12 Olimex/Debian boot, the Goodix touchscreen
    enumerated on Linux I2C bus 2 at address 0x14.

Set status to `verified`, evidence type to `direct`, cite lines 334-348 and the
capture hash, and state that Linux bus numbering does not independently verify
carrier traces, pull-ups, voltage, IRQ, or reset wiring.

- [x] **Step 5: Validate and commit**

Run:

    grep -Fq 'community-edited ReBrewie image' docs/evidence/hardware/sources.md
    grep -Fq 'owner-created experimental configuration' docs/evidence/hardware/sources.md
    grep -Fq 'Status: verified' docs/evidence/hardware/facts/HW-007.md
    grep -Fq 'Status: verified' docs/evidence/hardware/facts/HW-008.md
    git diff --check
    python3 tools/validate_hardware_evidence.py

Expected: every command exits 0. The validator may still report the existing
100-record count; no new records exist yet.

Commit:

    git add docs/evidence/hardware/sources.md docs/evidence/hardware/local-historical-evidence-review.md docs/evidence/hardware/facts/HW-007.md docs/evidence/hardware/facts/HW-008.md
    git commit -m "docs: verify current touchscreen runtime facts"

### Task 2: Add atomic legacy and modern runtime records

**Files:**
- Create: `docs/evidence/hardware/facts/HW-101.md`
- Create: `docs/evidence/hardware/facts/HW-102.md`
- Create: `docs/evidence/hardware/facts/HW-103.md`
- Create: `docs/evidence/hardware/facts/HW-104.md`
- Create: `docs/evidence/hardware/facts/HW-105.md`
- Create: `docs/evidence/hardware/facts/HW-106.md`
- Create: `docs/evidence/hardware/facts/HW-107.md`
- Create: `docs/evidence/hardware/facts/HW-108.md`
- Modify: `docs/evidence/hardware/fact-index.md`

**Interfaces:**
- Consumes: `docs/templates/hardware-fact.md`, the two fresh captures, the retained legacy-image `uImage`/`dmesg`, and the evidence-strata rules from Task 1.
- Produces: eight independently reviewable atomic records and a complete 108-record index.

- [x] **Step 1: Confirm the new ID range is unused**

Run:

    test ! -e docs/evidence/hardware/facts/HW-101.md
    test ! -e docs/evidence/hardware/facts/HW-108.md
    ! grep -Eq 'HW-10[1-8]' docs/evidence/hardware/fact-index.md

Expected: all commands exit 0.

- [x] **Step 2: Create verified legacy runtime records**

Use every mandatory field from `docs/templates/hardware-fact.md` and create:

- HW-101: the fresh ReBrewie boot runs exact kernel
  `Linux 3.4.90-Brewie #5`, corroborated by the retained `uImage` header and
  retained older-image `dmesg`; limit the claim to platform lineage.
- HW-102: `/etc/os-release` on that boot identifies Buildroot
  `2014.02-git-g3b4bd90-dirty`; explicitly classify userspace as
  community-edited ReBrewie rather than factory-original.
- HW-103: that boot actively uses SD/MMC with three observed partitions,
  EXT3 root on partition 2, and EXT3 `/home/brewie` on partition 3; record exact
  observed sizes but prohibit treating them as clean-slate requirements.
- HW-104: that boot detects PCF8563 on I2C0 address `0x51` and registers it as
  `rtc0`; retain the repeated-read behavior as a limitation/observation rather
  than a proposed design.

Each is `verified` only for its dated runtime proposition.

- [x] **Step 3: Create verified modern runtime records**

Create:

- HW-105: the fresh boot reports Linux `5.10.180-olimex #140856`, `armv7l`,
  model `Olimex A13-SOM-512`, and 521,216 KiB physical memory to Linux; do not
  reinterpret reserved/available memory as fitted RAM part identity.
- HW-106: the fresh boot enables the A13 watchdog at `0x1c20c90` with a
  16-second timeout and `nowayout=0`; do not infer application use or required
  future policy.
- HW-107: the fresh boot sees a Realtek USB WLAN adapter `0bda:8176`, loads
  `rtl8192cu`, and associates; scope it to the fitted device on that date.
- HW-108: both fresh legacy and modern captures enumerate `ttyS0` at
  `0x01c28400` and `ttyS1` at `0x01c28c00`; state that enumeration does not
  prove the physical MCU endpoint or protocol.

Each is `verified` only for its dated runtime proposition.

- [x] **Step 4: Add the eight records to the canonical index**

Append HW-101 through HW-108 in numeric order. Use concise claim summaries,
accurate categories, `verified` status, exact primary-source descriptions, and
relative record links.

- [x] **Step 5: Validate and commit**

Run:

    python3 tools/validate_hardware_evidence.py
    test "$(find docs/evidence/hardware/facts -maxdepth 1 -name 'HW-*.md' | wc -l)" -eq 108
    test "$(grep -Ec '^\| HW-[0-9]{3} \|' docs/evidence/hardware/fact-index.md)" -eq 108
    grep -Ril 'untouched factory image' docs/evidence/hardware/facts/HW-10[1-8].md
    git diff --check

Expected: the validator exits 0, both counts equal 108, the wording search
returns only explicit negations/limitations (inspect every result), and the
formatting check emits nothing.

Commit:

    git add docs/evidence/hardware/facts/HW-10[1-8].md docs/evidence/hardware/fact-index.md
    git commit -m "docs: record legacy and modern runtime facts"

### Task 3: Rebuild summaries and milestone status

**Files:**
- Modify: `docs/evidence/hardware/baseline.md`
- Modify: `docs/evidence/hardware/som-carrier.md`
- Modify: `docs/evidence/hardware/som-mcu-interconnect.md`
- Modify: `docs/evidence/hardware/capabilities.md`
- Modify: `docs/evidence/hardware/verification-register.md`
- Modify: `docs/milestones/001-hardware-baseline.md`

**Interfaces:**
- Consumes: all 108 final fact records and the canonical fact index.
- Produces: consistent derived summaries, current verification debt, exact counts, and an evidence-based active milestone status.

- [x] **Step 1: Compute status counts from records**

Run:

    grep -h '^- Status:' docs/evidence/hardware/facts/HW-*.md | sort | uniq -c

This parses the status field from every record without copying the old
`13 verified / 87 disputed` values.

Expected after Tasks 1 and 2: 23 verified and 85 disputed, totaling 108. If the
actual record contents produce different counts, stop and resolve the record or
plan discrepancy before editing summaries.

- [x] **Step 2: Update topical summaries**

In the relevant summaries:

- link HW-007/HW-008 as verified dated touch-runtime observations while keeping
  physical IRQ/reset/supply wiring unresolved;
- link HW-101 through HW-104 under legacy platform observations;
- link HW-105 through HW-107 under modern experimental platform observations;
- link HW-108 while preserving the distinction between UART enumeration and
  physical MCU connectivity/telemetry;
- remove claims that boot, storage, networking, RTC, or watchdog have no
  approved-source candidate;
- retain exact fitted-display identity, physical wiring, electrical limits, and
  actuator verification as debt.

- [x] **Step 3: Update verification debt and blocked decisions**

Remove only gaps answered by the new narrowly scoped records. Keep downstream
Linux-image choices blocked where they require requirements analysis rather than
mere historical observation, and keep physical/electrical claims blocked on
their own evidence.

Explicitly record that historical partition sizes, EXT3, kernel versions,
Buildroot, the old watchdog behavior, and the Realtek adapter are observations,
not selected clean-slate requirements.

- [x] **Step 4: Update milestone completion review**

Set the review date to 2026-08-12, record the computed counts, and keep milestone
001 `active`. Explain which former category gaps are now bounded by runtime
evidence and which material identity/connectivity/electrical gaps still prevent
completion. Do not mark the milestone blocked because productive verification
work remains possible.

- [x] **Step 5: Validate and commit**

Run:

    python3 tools/validate_hardware_evidence.py
    grep -Fq 'Status: active' docs/milestones/001-hardware-baseline.md
    grep -Fq '108 indexed records' docs/milestones/001-hardware-baseline.md
    grep -Fq '23 verified and 85 disputed' docs/milestones/001-hardware-baseline.md
    grep -RniE '13 verified|87 disputed|100 indexed records|No approved-source hardware candidate' docs/evidence/hardware docs/milestones/001-hardware-baseline.md
    git diff --check

Expected: validator and positive checks exit 0. Inspect every stale-wording
search result; no result may present an obsolete current count or unresolved
category statement. Historical quotations or clearly labelled prior-review
statements may remain only if necessary for audit history.

Commit:

    git add docs/evidence/hardware/baseline.md docs/evidence/hardware/som-carrier.md docs/evidence/hardware/som-mcu-interconnect.md docs/evidence/hardware/capabilities.md docs/evidence/hardware/verification-register.md docs/milestones/001-hardware-baseline.md
    git commit -m "docs: integrate runtime evidence into hardware baseline"

### Task 4: Final consistency and clean-slate review

**Files:**
- Review: all files changed since integration base `f73751d565009a26f360a5968a5755386bc18147`
- Modify only: files from Tasks 1-3 when a verified inconsistency is found

**Interfaces:**
- Consumes: the complete integration diff.
- Produces: review-ready branch with reproducible validation evidence and no prohibited design leakage.

- [x] **Step 1: Inspect the complete diff**

Run:

    git diff --stat f73751d565009a26f360a5968a5755386bc18147..HEAD
    git diff --check f73751d565009a26f360a5968a5755386bc18147..HEAD
    git diff f73751d565009a26f360a5968a5755386bc18147..HEAD -- docs/evidence/hardware docs/milestones/001-hardware-baseline.md

Read the complete diff. Confirm every status promotion is limited to a directly
observed proposition and every local-source claim includes exact provenance.

- [x] **Step 2: Run deterministic validation**

Run:

    python3 tools/validate_hardware_evidence.py
    git status --short

Expected: validator exits 0. Working tree is clean after any corrective commit.

- [x] **Step 3: Audit the clean-slate boundary**

Run targeted searches across changed files for `architecture`, `state machine`,
`protocol`, `control logic`, `Arduino`, `Qt`, `LVGL`, and `should use`.

Inspect each hit. Accept only boundary statements, historical labels, or factual
observations. Reject any new implementation recommendation derived from the old
systems.

- [ ] **Step 4: Commit corrections if required**

Implementation is complete, but the 2026-08-15 agent could not create the
worktree index lock because the shared Git metadata is read-only. The controller
must commit the already-authored changes; this checkbox remains open until then.

If review found issues, edit only the affected evidence files, rerun Steps 1-3,
then commit:

    git add docs/evidence/hardware docs/milestones/001-hardware-baseline.md
    git commit -m "docs: correct evidence integration review findings"

If no issue exists, do not create an empty commit.

- [ ] **Step 5: Request review and integrate only after approval**

Push the completed branch under the approved automatic-push policy, open or
update its pull request, and present the validation results and remaining
milestone blockers to the project owner. Merge only after review approval. After
merge, rerun `python3 tools/validate_hardware_evidence.py` on fresh `main` before
automatically pushing `main`.
