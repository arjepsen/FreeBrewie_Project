# FreeBrewie Hardware Baseline Design

Date: 2026-08-08  
Status: Written specification approved by Project owner on 2026-08-08

## Purpose

Milestone 001 establishes a verified, software-relevant hardware baseline for the project owner's specific Brewie machine. The baseline will support later independent design of an optimized, maintainable, and updateable Linux image and new control software capable of offering greater control than the original system.

This milestone discovers and records facts. It does not design or implement the Linux image, SOM application, MCU firmware, communication protocol, brewing behaviour, UI, or control algorithms.

## Scope

The baseline covers every hardware element that software must support, configure, communicate with, monitor, diagnose, or control:

- SOM, MCU, carrier board, identities, revisions, memory, and storage;
- boot- and update-relevant hardware;
- display, input, networking, and other SOM peripherals;
- SOM–MCU connections and electrical constraints;
- software-visible sensors, pumps, heaters, valves, and other brewing devices;
- reset, enable, interrupt, watchdog, power-control, and safety-relevant signals;
- connector and pin mappings where software or diagnostics depend on them; and
- capabilities and limits affecting drivers, timing, precision, performance, reliability, optimization, or future control.

Passive circuitry and board-level reconstruction are excluded unless needed to understand a software-visible signal, electrical constraint, or safety condition.

The baseline describes the owner's specific machine first. Other revisions are noted when encountered but do not expand this milestone into a complete variant catalogue.

## Approved source boundary

Initial read-only inspection is limited to the following sources after milestone activation.

### Previous MCU work

Repository: `https://github.com/arjepsen/FreeBrewie-MCU`

Permitted material:

- hardware-relevant documents within `Documentation/`;
- schematics, images, diagrams, and datasheets directly referenced by a selected document; and
- `Documentation/BrewieMCU.kicad_sch` as explicitly permitted reverse-engineering evidence.

### Previous SOM work

Repository: `https://github.com/arjepsen/FreeBrewie-SOM`

Permitted material:

- hardware-relevant documents within `Docs/`; and
- schematics, images, diagrams, and datasheets directly referenced by a selected document.

### Other permitted evidence

- the owner's specific physical machine, through visual inspection, labels, wiring inspection, and targeted photographs supplied in response to a specific verification request; and
- manufacturer datasheets and other authoritative hardware documentation needed to verify an extracted claim.

Each GitHub repository and artifact must be pinned to an exact commit before its contents are used as evidence.

The original and newer historical Brewie repositories remain outside the approved boundary. Source-code directories and other areas of the previous-work repositories are also excluded. Access to any excluded source requires a specific request that identifies the missing material fact, explains why approved sources are insufficient, and names the proposed additional file or evidence class. The project owner must approve the expansion before inspection.

## Evidence selection

Inspection is selective rather than exhaustive:

1. Inventory filenames and document titles within the approved folders.
2. Select items likely to contain component identities, revisions, pinouts, buses, connections, peripherals, physical constraints, or software-relevant capabilities.
3. Record why each selected item is relevant.
4. Read selected items and directly linked supporting artifacts only.
5. Ignore software architecture, implementation recommendations, control logic, state machines, protocol design, and module structure even if they appear in a selected document.

## Reconstructed MCU schematic

`Documentation/BrewieMCU.kicad_sch` is a recent reverse-engineered tracing of most of the MCU board. The owner estimates that it is approximately 97% complete or correct. This estimate is context, not a verification claim.

The schematic is high-value but non-authoritative inferred evidence. An early structural-readability check will:

- confirm that the native KiCad schematic can be parsed completely;
- identify missing or unresolved symbols, sheets, libraries, or other dependencies;
- confirm whether components, pins, nets, labels, connectors, and annotations can be extracted; and
- report missing information before using the schematic for hardware claims.

The schematic and prose derived from the same tracing work share one evidence lineage and cannot independently verify each other. Individual claims derived from the schematic remain inferred until independently confirmed.

## Extraction and verification workflow

The milestone proceeds in controlled passes:

1. **Pin and inventory:** Record repository commits and inventory only the approved source locations.
2. **Select evidence:** Choose hardware-relevant documents and record the reason for selection.
3. **Validate the schematic:** Perform the structural-readability check before detailed MCU fact extraction.
4. **Extract candidate facts:** Convert each material claim into a hardware-fact record with exact provenance.
5. **Build provisional maps:** Organize facts into compute hardware, SOM peripherals, MCU resources, SOM–MCU interconnection, brewing devices, power/reset/safety signals, and software-relevant capabilities.
6. **Verify proportionately:** Verify cheap facts promptly with independent documentation, labels, wiring inspection, targeted photographs, or safe continuity evidence.
7. **Resolve conflicts:** Preserve competing claims, assess source independence, and ask the owner about unresolved consequential ambiguity.
8. **Produce the baseline:** Summarize the verified machine configuration with links to every material fact record and visible gaps.
9. **Review completion:** Run all required governance reviews before changing milestone status.

Prior pump-characterization results may be recorded as historical measured evidence when found in approved documentation. Their original apparatus, conditions, uncertainty, and source must remain visible. Experiments will not be repeated unless a later approved decision requires better data.

## Evidence and uncertainty model

Each material fact uses `docs/templates/hardware-fact.md` and records:

- the precise claim and affected hardware revision;
- repository commit, source, file, and exact location;
- whether evidence is direct or inferred;
- verification method and genuinely independent confirmation;
- confidence, conflicts, limitations, and status;
- downstream decisions that may depend on it;
- the cheapest useful verification action; and
- decisions blocked until verification.

Statuses have these meanings:

- **Proposed:** extracted but not assessed.
- **Provisionally accepted:** high-confidence, time-consuming to verify, and temporarily useful without enabling consequential decisions.
- **Verified:** supported by adequate independent evidence or direct verification.
- **Disputed:** sources conflict or evidence is insufficient.
- **Superseded:** replaced by a newer traceable record.

Repetition across sources derived from one original investigation is not independent confirmation.

Missing schematic dependencies, unreadable artifacts, ambiguous pin mappings, and revision uncertainty are explicit gaps. Connections must not be inferred from legacy software implementation. A material gap that blocks later Linux-image or control-system work keeps the milestone active or blocked unless the owner explicitly removes it from scope as unnecessary.

## Physical machine context

The machine is currently upside down on a table, providing access to the MCU board, SOM and carrier board, pumps, pressure sensor, and wiring. Both heaters and both pumps are disconnected to prevent accidental damage. The current physical state is context and must not be treated as evidence of the original factory assembly.

A general photographic inventory is not required. Targeted photographs may be requested only when they are a quick way to verify a specific material fact.

The machine does not need to be reassembled, filled, heated, or operated for this milestone. Documentation, component identification, wiring inspection, photographs, and safe continuity evidence may adequately verify a fact without operational testing.

## Safety boundary

This milestone does not authorize:

- energizing disconnected heaters or pumps;
- introducing water into the upside-down machine;
- moving wiring merely to match reference imagery;
- continuity measurements on powered circuitry; or
- powered measurements without a separate safety-reviewed request.

A request for continuity or powered measurement must state the exact points, purpose, equipment, method, expected result or range, and risks before the owner performs it. Powered or wet experiments outside these facts require a later explicitly approved scope.

## Deliverables

The milestone produces:

- a source inventory containing pinned commits and approved artifacts;
- a structural-readability report for the reconstructed MCU schematic;
- individual hardware-fact records;
- a software-relevant hardware baseline summary;
- a SOM and carrier-board capability summary;
- an MCU capability and pin-resource summary;
- a SOM–MCU electrical interconnection map;
- a brewing-device connection map covering software-visible sensors, pumps, heaters, valves, and safety-related signals;
- a list of capabilities and limits relevant to later optimization and expanded control;
- a conflict, assumption, and verification-debt register; and
- a list of downstream decisions blocked by unresolved facts.

Each summary and map links back to the supporting fact records rather than becoming an uncited alternative source of truth.

## Completion criteria

Completion requires:

- verified identities and applicable revisions for the material SOM, MCU, carrier board, memory, storage, display/input hardware, networking hardware, and software-visible brewing peripherals;
- verified material connections among the SOM, MCU, carrier board, and relevant peripherals;
- recorded software-relevant capabilities and limits where later choices could depend on them;
- complete mandatory provenance for every material fact;
- explicit visibility of conflicts, assumptions, verification debt, and blocked decisions;
- no consequential downstream decision depending on an unverified material fact; and
- passing scope, provenance, assumption, and completion reviews.

Powered operational testing is not intrinsically required. A baseline item may be removed only with the owner's explicit approval and a recorded reason that it is unnecessary. Any other unresolved material baseline fact keeps the milestone active or blocked.

## Activation and review gates

The milestone became active after the following required sequence was completed:

1. this written specification is committed;
2. the owner reviews and approves the written specification;
3. the milestone record is updated to reference this design, identify the approved source boundary, record the approver and approval date, and change its status to active; and
4. that activation change is committed.

Only then may selective reference inspection begin.

Before completion, reviews must confirm:

- every material claim has adequate provenance;
- direct evidence and inference are distinguished;
- cheap verification opportunities were not skipped;
- remaining assumptions meet the provisional-use rule;
- no consequential decision depends on an unverified material fact;
- inspection stayed within the approved source boundary;
- no excluded technical design entered the milestone; and
- records and local links are internally consistent.
