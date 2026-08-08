# FreeBrewie Hardware Baseline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (- [ ]) syntax for tracking.

**Goal:** Activate milestone 001, inspect only its approved evidence boundary, and produce a verified software-relevant hardware baseline for the project owner's specific Brewie machine.

**Architecture:** Evidence moves through four explicit stages: pinned source inventory, candidate fact extraction, independent verification, and linked baseline summaries. Every material claim is stored as an individual record and indexed; summaries never become uncited alternative sources of truth. Discovery determines the number of fact records, but deterministic IDs and filenames keep the output auditable.

**Tech Stack:** Markdown, Git, GitHub read-only access, KiCad schematic text inspection, manufacturer documentation, targeted owner-provided observations, POSIX shell commands, Python 3 standard library.

## Global Constraints

- The milestone discovers and records facts only.
- Do not design or implement the Linux image, SOM application, MCU firmware, communication protocol, brewing behaviour, UI, or control algorithms.
- Historical architecture, module structure, control logic, state machines, protocol design, and implementation recommendations are not evidence for the new implementation.
- Initial repository inspection is limited to hardware-relevant material in FreeBrewie-MCU/Documentation, FreeBrewie-SOM/Docs, directly referenced supporting artifacts, and FreeBrewie-MCU/Documentation/BrewieMCU.kicad_sch.
- Pin each reference repository to an exact commit before reading evidence.
- Do not clone or import either historical repository into FreeBrewie_Project.
- Do not inspect excluded repository paths. Stop and request owner approval before expanding the source boundary.
- Treat BrewieMCU.kicad_sch as inferred reverse-engineering evidence, not an authoritative original schematic.
- Repetition within one evidence lineage is not independent verification.
- Verify cheap material facts promptly.
- Provisional use requires recorded high confidence, time-consuming verification, and a delay that impedes progress.
- An unverified fact cannot support a safety-critical, consequential, or hard-to-reverse decision.
- Do not energize disconnected heaters or pumps, add water, perform continuity checks on powered circuits, or request powered measurements without a separately approved safety-reviewed procedure.
- The machine need not be reassembled or operated to complete this milestone.
- No general photographic inventory is required; request only photographs tied to a specific verification question.
- Material unresolved facts keep the milestone active or blocked unless the owner explicitly removes them as unnecessary with a recorded reason.

---

## Planned file map and record contract

- PROJECT.md: canonical current-authority status.
- docs/milestones/001-hardware-baseline.md: active milestone scope, approvals, and final status.
- docs/evidence/hardware/sources.md: pinned source inventory and selection decisions.
- docs/evidence/hardware/schematic-readability.md: native KiCad structural-readability result.
- docs/evidence/hardware/fact-index.md: canonical index of every hardware-fact record.
- docs/evidence/hardware/facts/HW-NNN.md: one fact per file, using docs/templates/hardware-fact.md.
- docs/evidence/hardware/verification-register.md: conflicts, assumptions, verification debt, and blocked decisions.
- docs/evidence/hardware/baseline.md: overall software-relevant baseline linking fact IDs.
- docs/evidence/hardware/som-carrier.md: SOM and carrier capability summary.
- docs/evidence/hardware/mcu.md: MCU capability and pin-resource summary.
- docs/evidence/hardware/som-mcu-interconnect.md: SOM–MCU electrical map.
- docs/evidence/hardware/brewing-devices.md: software-visible brewing-device map.
- docs/evidence/hardware/capabilities.md: optimization- and control-relevant limits.
- tools/validate_hardware_evidence.py: deterministic fact-record and index validator.

Assign fact IDs sequentially in discovery order as HW-001, HW-002, and so on. The filename must exactly match the ID. Never reuse an ID. If a fact is superseded, keep its file and link the replacement. Every summary claim must cite one or more fact IDs as relative Markdown links.

### Task 1: Activate milestone 001

**Files:**
- Modify: PROJECT.md
- Modify: docs/milestones/001-hardware-baseline.md

**Interfaces:**
- Consumes: docs/superpowers/specs/2026-08-08-hardware-baseline-design.md and the owner's written-specification approval on 2026-08-08.
- Produces: the sole authority for Tasks 2–8 to inspect the approved sources and gather hardware facts.

- [ ] **Step 1: Confirm the milestone is not active**

Run:

    grep -Fq "Status: proposed" docs/milestones/001-hardware-baseline.md
    grep -Fq "No work is currently active" PROJECT.md

Expected: both commands exit 0.

- [ ] **Step 2: Update the milestone approval and scope**

In docs/milestones/001-hardware-baseline.md:

- Change Status to active.
- Set Approved by and date to Project owner, 2026-08-08.
- Link the approved hardware-baseline design.
- State the exact two-repository source boundary from Global Constraints.
- Explicitly permit the KiCad artifact as inferred evidence.
- State that no other repository path or historical repository is authorized.
- Retain every existing technical and safety exclusion.
- Record that selective reference inspection may begin only after this activation commit.

- [ ] **Step 3: Update canonical current authority**

In PROJECT.md, replace the inactive-status paragraph with:

    Milestone 001, hardware baseline, is active. Only the factual discovery,
    verification, and documentation authorized by its approved design and
    milestone record may proceed. Product implementation and technical subsystem
    design remain unauthorized.

Link “Milestone 001” to docs/milestones/001-hardware-baseline.md.

- [ ] **Step 4: Validate activation**

Run:

    grep -Fq "Status: active" docs/milestones/001-hardware-baseline.md
    grep -Fq "Project owner, 2026-08-08" docs/milestones/001-hardware-baseline.md
    grep -Fq "BrewieMCU.kicad_sch" docs/milestones/001-hardware-baseline.md
    grep -Fq "Milestone 001, hardware baseline, is active" PROJECT.md
    git diff --check

Expected: all commands exit 0 and the formatting check emits nothing.

- [ ] **Step 5: Commit activation**

Run:

    git add PROJECT.md docs/milestones/001-hardware-baseline.md
    git commit -m "docs: activate hardware baseline milestone"

Expected: commit succeeds. Do not inspect reference material before this commit exists.

### Task 2: Pin sources and validate the MCU schematic

**Files:**
- Create: docs/evidence/hardware/sources.md
- Create: docs/evidence/hardware/schematic-readability.md

**Interfaces:**
- Consumes: the active source boundary from milestone 001.
- Produces: immutable commit references, an approved artifact inventory, evidence-selection decisions, and the schematic parser/dependency result used by all extraction tasks.

- [ ] **Step 1: Prove source records are absent**

Run:

    test ! -e docs/evidence/hardware/sources.md
    test ! -e docs/evidence/hardware/schematic-readability.md

Expected: both commands exit 0.

- [ ] **Step 2: Resolve immutable repository commits without cloning**

Use GitHub read-only access to resolve the current default-branch commit for:

    https://github.com/arjepsen/FreeBrewie-MCU
    https://github.com/arjepsen/FreeBrewie-SOM

Record the full 40-character commit SHA, default branch, repository URL, and retrieval date 2026-08-08. All later reads must use URLs pinned to those SHAs, not moving branch names.

- [ ] **Step 3: Inventory only approved paths**

List filenames, paths, types, and titles where available under:

    FreeBrewie-MCU/Documentation
    FreeBrewie-SOM/Docs

Do not open other directories. For each item, record one selection status:

- selected: likely contains software-relevant hardware evidence;
- supporting-only: read only if directly referenced by a selected item;
- excluded: no apparent software-relevant hardware content.

Add a one-sentence reason. Record BrewieMCU.kicad_sch as selected and inferred.

- [ ] **Step 4: Write sources.md**

Use these sections:

    # Hardware evidence sources
    ## Inspection authority
    ## Pinned repositories
    ## MCU Documentation inventory
    ## SOM Docs inventory
    ## Directly referenced supporting artifacts
    ## Excluded sources and paths
    ## Boundary-expansion requests

State explicitly that an inventory entry does not validate its contents and that excluded paths were not inspected.

- [ ] **Step 5: Check native schematic readability**

Read only the pinned BrewieMCU.kicad_sch artifact. Determine and record:

- file format and KiCad version marker;
- whether the complete file is retrievable and structurally balanced;
- external symbol, library, sheet, image, or table dependencies;
- resolvable symbol instances and library identifiers;
- component reference/value fields;
- labels, hierarchical labels, junctions, wires, buses, and connector symbols;
- whether pin-to-net extraction is complete, partial, or blocked;
- all parse warnings or unresolved identifiers.

Do not turn schematic content into hardware-fact claims in this task.

- [ ] **Step 6: Write schematic-readability.md**

Use these sections:

    # MCU schematic structural-readability report
    ## Pinned artifact
    ## Format and completeness
    ## Dependencies
    ## Extractable structures
    ## Unresolved structures
    ## Suitability for fact extraction
    ## Required owner input

The final suitability must be one of usable, usable-with-limitations, or blocked, with evidence for the result.

- [ ] **Step 7: Validate and commit**

Run:

    grep -Eq "[0-9a-f]{40}" docs/evidence/hardware/sources.md
    grep -Fq "FreeBrewie-MCU/Documentation" docs/evidence/hardware/sources.md
    grep -Fq "FreeBrewie-SOM/Docs" docs/evidence/hardware/sources.md
    grep -Fq "## Suitability for fact extraction" docs/evidence/hardware/schematic-readability.md
    grep -Eq "usable|usable-with-limitations|blocked" docs/evidence/hardware/schematic-readability.md
    git diff --check
    git add docs/evidence/hardware/sources.md docs/evidence/hardware/schematic-readability.md
    git commit -m "docs: pin hardware evidence sources"

Expected: every command exits 0.

### Task 3: Extract compute-platform facts

**Files:**
- Create: docs/evidence/hardware/fact-index.md
- Create: docs/evidence/hardware/facts/HW-NNN.md records allocated sequentially
- Create: docs/evidence/hardware/verification-register.md
- Create: tools/validate_hardware_evidence.py

**Interfaces:**
- Consumes: selected pinned MCU/SOM documents and the schematic-readability result.
- Produces: indexed candidate facts for the SOM, carrier, MCU, memory, storage, boot, display/input, networking, and compute-related connections.

- [ ] **Step 1: Create empty validated indexes before extraction**

Create fact-index.md with columns:

    ID | Claim summary | Category | Status | Primary source | Record

Create verification-register.md with sections:

    # Hardware verification register
    ## Disputed facts
    ## Provisional assumptions
    ## Verification debt
    ## Blocked downstream decisions
    ## Owner-approved removals

No section may contain an unlinked factual claim.

- [ ] **Step 2: Read selected compute-relevant documents only**

From the Task 2 inventory, read selected documents concerning:

- SOM identity and revision;
- carrier-board identity and revision;
- MCU identity and revision;
- memory and storage;
- boot hardware;
- display and input;
- networking; and
- compute-side buses, reset, enable, interrupt, watchdog, and power-control lines.

Stop and write a boundary-expansion request in sources.md instead of reading an excluded path.

- [ ] **Step 3: Write one record per material claim**

For every extracted material claim:

1. Allocate the next HW-NNN ID.
2. Copy docs/templates/hardware-fact.md to facts/HW-NNN.md.
3. Replace every template prompt with evidence or an explicit not-applicable reason.
4. Cite repository URL, full commit SHA, file path, and precise line, page, figure, table, or schematic object.
5. Mark evidence direct or inferred.
6. Mark status proposed until verification is assessed.
7. Add the record to fact-index.md.

Do not copy source prose beyond short identifiers or labels necessary to state the fact.

- [ ] **Step 4: Record conflicts and dependencies**

Link every disputed or provisional fact from verification-register.md. Identify which later Linux-image or control-system questions remain blocked, without answering those questions.

- [ ] **Step 5: Create the deterministic record validator**

Create tools/validate_hardware_evidence.py with this implementation:

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
        link = f"facts/{record_id}.md"
        if index_text.count(link) != 1:
            fail(f"{record_id}: expected exactly one index link")
    print(f"validated {len(files)} hardware fact records")

- [ ] **Step 6: Run the record validator**

Run:

    python3 tools/validate_hardware_evidence.py

Expected: exit 0 and output validated N hardware fact records, where N equals the number of indexed files.

- [ ] **Step 7: Commit**

Run:

    git diff --check
    git add docs/evidence/hardware/fact-index.md docs/evidence/hardware/facts docs/evidence/hardware/verification-register.md docs/evidence/hardware/sources.md tools/validate_hardware_evidence.py
    git commit -m "docs: extract compute hardware facts"

Expected: commit succeeds.

### Task 4: Extract interconnect and brewing-device facts

**Files:**
- Modify: docs/evidence/hardware/fact-index.md
- Create: additional docs/evidence/hardware/facts/HW-NNN.md records
- Modify: docs/evidence/hardware/verification-register.md
- Modify: docs/evidence/hardware/sources.md only if a boundary request is needed

**Interfaces:**
- Consumes: pinned selected evidence, readable schematic structures, and the next ID from fact-index.md.
- Produces: candidate facts for SOM–MCU wiring and every software-visible sensor, actuator, safety signal, and relevant limit.

- [ ] **Step 1: Read selected device and connection documents**

Read only selected approved documents concerning:

- SOM–MCU electrical interconnection;
- pressure or water-level sensing;
- pumps;
- heaters;
- valves;
- other software-visible sensors and actuators;
- connector and pin mappings;
- voltage levels, signal direction, reset/enable/interrupt lines; and
- timer, PWM, ADC, bus, and other MCU resources used by attached devices.

Prior pump-characterization measurements may be extracted only with their apparatus, conditions, source, and uncertainty.

- [ ] **Step 2: Extract schematic-derived claims conservatively**

Use BrewieMCU.kicad_sch only to extract structures judged usable in schematic-readability.md. Mark each such fact inferred. Use exact symbol references, pins, labels, and net identifiers as source locations. Do not infer behavior from circuit grouping or component placement alone.

- [ ] **Step 3: Add one record per material claim**

Continue the sequential HW-NNN allocation and the complete record procedure from Task 3. Every connection record must name both endpoints, relevant pins or connector positions when software depends on them, direction where established, interface type, and voltage level where relevant.

- [ ] **Step 4: Update conflicts and blocked decisions**

Add links for every dispute, provisional assumption, missing device identity, ambiguous connection, and material capability gap. Do not hide currently disconnected hardware; distinguish documented wiring from the machine's present disconnected state.

- [ ] **Step 5: Validate and commit**

Run the record validator over the full facts directory. Then inspect each selected device-oriented source row in sources.md and confirm that every software-visible device it identifies is linked from fact-index.md or verification-register.md.

Run:

    python3 tools/validate_hardware_evidence.py
    git diff --check
    git add docs/evidence/hardware
    git commit -m "docs: extract machine interconnect facts"

Expected: all checks pass and the commit succeeds.

### Task 5: Verify material facts proportionately

**Files:**
- Modify: docs/evidence/hardware/facts/HW-NNN.md
- Modify: docs/evidence/hardware/verification-register.md
- Modify: docs/evidence/hardware/fact-index.md

**Interfaces:**
- Consumes: all proposed candidate facts and permitted independent evidence.
- Produces: verified, provisionally accepted, or disputed records with explicit verification evidence and owner questions.

- [ ] **Step 1: Classify verification cost and consequence**

For each proposed fact, record:

- whether a cheap independent check exists;
- verification cost as quick or time-consuming;
- whether Linux, firmware, safety, or hard-to-reverse work could depend on it; and
- the next verification action.

Never use multiple files from the same prior investigation as independent confirmation.

- [ ] **Step 2: Perform cheap documentary verification**

Use manufacturer datasheets or other authoritative sources for component identity, memory/storage capacity, electrical interfaces, pin functions, voltage limits, timer/ADC/PWM resources, display characteristics, and other published capabilities. Record exact document revision and section/page.

- [ ] **Step 3: Request targeted owner evidence only where needed**

For facts cheaply checked on the physical machine, ask one targeted question or photograph request at a time. State the exact component, label, connector, wire, or view required and what claim it would verify.

Do not request a general photo inventory.

- [ ] **Step 4: Gate measurements**

If a material connection remains unresolved after documentation and targeted visual inspection, write a proposed measurement request containing:

- fact ID and question;
- exact unpowered continuity points or powered measurement points;
- required equipment and settings;
- machine power/fluid/disconnection state;
- expected result or range;
- risks and stop conditions; and
- safer alternatives attempted.

Do not perform or ask the owner to perform the measurement until separately approved.

- [ ] **Step 5: Update statuses**

Set records to:

- verified only with adequate direct or genuinely independent evidence;
- provisionally accepted only when all three binding assumption conditions are demonstrated;
- disputed when evidence conflicts or remains insufficient.

Keep blocked decisions visible for every unverified consequential fact.

- [ ] **Step 6: Validate and commit**

Run:

    python3 tools/validate_hardware_evidence.py

Then inspect the indexed records and reject the task if:

- a verified record lacks Verification method or Independent confirmation;
- a provisionally accepted record lacks high-confidence rationale, time-consuming-verification rationale, delay-impact rationale, next action, or blocked decisions;
- a disputed record is absent from verification-register.md; or
- a consequential unverified fact has no blocked decision.

Run:

    git diff --check
    git add docs/evidence/hardware
    git commit -m "docs: verify material hardware facts"

Expected: verification checks pass and the commit succeeds. If owner input is pending, commit the visible disputed state without claiming milestone completion.

### Task 6: Build linked hardware maps and capability summaries

**Files:**
- Create: docs/evidence/hardware/baseline.md
- Create: docs/evidence/hardware/som-carrier.md
- Create: docs/evidence/hardware/mcu.md
- Create: docs/evidence/hardware/som-mcu-interconnect.md
- Create: docs/evidence/hardware/brewing-devices.md
- Create: docs/evidence/hardware/capabilities.md

**Interfaces:**
- Consumes: fact-index.md and verified/provisional/disputed fact records.
- Produces: human-readable maps that later milestones can use without reading historical repositories.

- [ ] **Step 1: Write SOM and carrier summary**

som-carrier.md must cover verified identity/revision, CPU architecture, memory, storage, boot path hardware, display/input, networking, exposed buses, reset/power/watchdog hardware, and relevant limits. Every bullet or table row must link fact IDs.

- [ ] **Step 2: Write MCU summary**

mcu.md must cover verified identity/revision, clock and memory capabilities, GPIO, ADC, timers, PWM, buses, interrupts, reset/watchdog, pin-resource allocations, and unresolved resource questions. Cite every row.

- [ ] **Step 3: Write SOM–MCU map**

som-mcu-interconnect.md must identify physical endpoints, pins/connectors, interface type, direction, electrical level, reset/enable/interrupt lines, and current verification status. Do not define a communication protocol.

- [ ] **Step 4: Write brewing-device map**

brewing-devices.md must list every discovered software-visible sensor and actuator, identity where established, MCU/SOM endpoint, interface or drive method as a hardware fact, relevant electrical constraints, disconnected current state where applicable, and verification status. Do not define brewing behavior or control policy.

- [ ] **Step 5: Write capability summary**

capabilities.md must capture only limits potentially relevant to later software decisions: memory/storage, boot media, display, bus limits, ADC resolution, timer/PWM resources, sensor characteristics, actuator drive constraints, storage endurance, and other discovered constraints. Cite fact records and distinguish verified limits from unresolved questions.

- [ ] **Step 6: Write baseline.md**

baseline.md must:

- state the target machine and current physical context;
- link sources.md, schematic-readability.md, fact-index.md, verification-register.md, and every detailed summary;
- contain a concise verified configuration overview;
- list all material disputed/provisional facts and blocked decisions by link;
- state that summaries are views over fact records, not independent evidence; and
- repeat that the baseline contains no product or control design.

- [ ] **Step 7: Validate and commit**

Inspect every hardware assertion in a summary bullet or table row and require a relative link to facts/HW-NNN.md. Run the record validator and local-link checker to catch missing IDs. Compare all disputed and provisional IDs in fact-index.md with baseline.md and reject the task if any are omitted.

Run:

    python3 tools/validate_hardware_evidence.py
    python3 -c 'from pathlib import Path; import re,sys; files=list(Path("docs/evidence/hardware").rglob("*.md")); missing=[]; pat=re.compile(r"\[[^]]+\]\((?!https?://|#)([^)#]+)(?:#[^)]+)?\)"); [(missing.append((str(p),t)) if not (p.parent/t).resolve().exists() else None) for p in files for t in pat.findall(p.read_text())]; print("\n".join(f"{p}: {t}" for p,t in missing)); sys.exit(bool(missing))'
    git diff --check
    git add docs/evidence/hardware
    git commit -m "docs: assemble software-relevant hardware baseline"

Expected: all checks pass and commit succeeds.

### Task 7: Complete or block milestone 001

**Files:**
- Modify: docs/milestones/001-hardware-baseline.md
- Modify: PROJECT.md
- Modify: README.md
- Modify: docs/evidence/hardware/verification-register.md if final review finds a gap

**Interfaces:**
- Consumes: all milestone deliverables and governance review checklists.
- Produces: an honest terminal status: complete only when every material completion criterion passes, otherwise active or blocked with exact unresolved facts.

- [ ] **Step 1: Run scope review**

Compare every changed file against the milestone design and Global Constraints. Confirm no excluded repository path was inspected and no Linux, application, firmware, protocol, brewing-logic, UI, or control design entered the work.

- [ ] **Step 2: Run provenance and assumption reviews**

For every fact record, answer each applicable question in docs/governance/review-checklists.md. Record failures in verification-register.md and do not mark completion while a required answer fails.

- [ ] **Step 3: Run completion review**

Verify:

- material SOM, MCU, carrier, memory, storage, display/input, networking, and brewing-peripheral identities and applicable revisions;
- material connections among compute and brewing hardware;
- software-relevant capabilities and limits;
- complete provenance;
- visible conflicts, assumptions, debt, and blocked decisions; and
- no consequential decision depending on an unverified fact.

An unresolved material item can be removed only through a record in verification-register.md containing the item, reason it is unnecessary, Project owner approval, and approval date.

- [ ] **Step 4: Set honest milestone status**

If every completion criterion passes:

- set milestone 001 Status to complete;
- record completion date;
- update PROJECT.md to state no work is active and that Linux-image requirements/design remains proposed;
- update README.md milestone status.

If material facts remain but can progress with owner input, keep Status active and list exact blockers.

If progress cannot continue without unavailable information after repeated attempts, set Status blocked and list exact facts, attempted verification, and required owner/external action.

Do not create or activate a Linux-image milestone in this task.

- [ ] **Step 5: Validate all documentation**

Run:

    python3 -c 'from pathlib import Path; import re,sys; files=[Path("README.md"),Path("PROJECT.md"),Path("CONTRIBUTING.md"),*Path("docs").rglob("*.md")]; missing=[]; pat=re.compile(r"\[[^]]+\]\((?!https?://|#)([^)#]+)(?:#[^)]+)?\)"); [(missing.append((str(p),t)) if not (p.parent/t).resolve().exists() else None) for p in files for t in pat.findall(p.read_text())]; print("\n".join(f"{p}: {t}" for p,t in missing)); sys.exit(bool(missing))'
    if grep -RInE "TBD|TODO|FIXME" README.md PROJECT.md CONTRIBUTING.md docs --include="*.md" --exclude="*-plan.md"; then exit 1; fi
    git diff --check
    git status --short

Expected: links resolve, no placeholders are found outside plans, formatting is clean, and only planned final-review changes are present.

- [ ] **Step 6: Commit terminal status**

Run:

    git add README.md PROJECT.md docs/milestones/001-hardware-baseline.md docs/evidence/hardware/verification-register.md
    git commit -m "docs: record hardware baseline milestone status"
    git status --short --branch

Expected: commit succeeds and the working tree is clean.
