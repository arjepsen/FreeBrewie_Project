# Hardware evidence sources

## Inspection authority

Inspection is authorised by active milestone 001, `docs/milestones/001-hardware-baseline.md`, as approved by the project owner on 2026-08-08. The allowed read-only boundary is:

- `https://github.com/arjepsen/FreeBrewie-MCU`, limited to `FreeBrewie-MCU/Documentation`, directly referenced supporting schematics, images, diagrams, and datasheets, and `FreeBrewie-MCU/Documentation/BrewieMCU.kicad_sch`; and
- `https://github.com/arjepsen/FreeBrewie-SOM`, limited to `FreeBrewie-SOM/Docs` and directly referenced supporting schematics, images, diagrams, and datasheets.

`FreeBrewie-MCU/Documentation/BrewieMCU.kicad_sch` is selected as non-authoritative, inferred reverse-engineering evidence. Repositories were accessed read-only and were not cloned. An inventory entry records an evidence-selection decision; it does not validate the item's contents or establish a hardware fact.

### Approved filename-only expansion

On 2026-08-12, the project owner approved listing repository-relative path names
and Git object types across the two already pinned repositories solely to locate
candidate evidence for the pending Task 3 and Task 4 requests. File contents,
symlink/submodule targets, moving branches, and hardware conclusions remain
outside this approval. Candidate content paths must be presented to and approved
by the project owner before inspection.

#### Filename-only inventory result

The approved metadata inventory completed on 2026-08-12 against the two pinned
commits. GitHub reported complete, non-truncated trees containing 65 paths/object
types for FreeBrewie-MCU and 5,405 for FreeBrewie-SOM. Only repository-relative
paths and Git object types were retained; no newly exposed blob content was read.

The path names expose no candidate BOM, assembly record, native netlist,
revision-matched carrier schematic, device-tree source or blob, boot-media or
persistent-storage record, networking-hardware record, connector/harness
drawing, or complete characterization report. The SOM tree is dominated by the
previous application and its vendored UI dependency, neither of which is an
authoritative hardware source.

The following previously excluded paths are the only newly inventoried names
that plausibly contain narrowly scoped hardware-configuration observations:

- FreeBrewie-MCU `boards/brewie_atmega2560.json`;
- FreeBrewie-MCU `platformio.ini`;
- FreeBrewie-MCU `src/Board.h`;
- FreeBrewie-SOM `Deploy/Admin/flash_mcu_from_som.sh`;
- FreeBrewie-SOM `Deploy/Admin/probe_buzzer_gpio.sh`;
- FreeBrewie-SOM `Apps/BrewieApp/src/Platform/Display.c`; and
- FreeBrewie-SOM `Apps/CalibrationApp/src/main.c`.

These names do not establish relevance, correctness, or hardware facts. Their
contents remain unapproved and unread. Audio/buzzer evidence is non-blocking,
and application/calibration source risks exposing historical implementation
logic, so those candidates should be opened only for a specific unresolved fact
that cannot be addressed by a more authoritative source.

### Approved local historical evidence

On 2026-08-12, the project owner approved thorough read-only inspection of the
external folder `/home/anders/Documents/OldStuff` for hardware facts,
historical Linux-image facts, boot/kernel/device-tree observations, and prior
physical-investigation records. The initial path inventory identified:

- `brewie.dts` and `first dmesg.txt`;
- `old dts - collected them into one/`;
- `oldImage/`, including device-tree, interrupt, GPIO, MCU-pinout,
  pressure-sensor, cable-PCB, and valve-PCB material; and
- the historical repository directories `ReBrewie-main/` and
  `reb20-develop/`.

Inspection must select and cite evidence by exact local path. Encountered
legacy application architecture, module structure, brewing/control logic,
state machines, communication-protocol design, and implementation source are
not reusable and must not become requirements or design inputs. The folder
remains external, read-only, unimported, and outside all builds.

#### Local evidence inventory and provenance

The 2026-08-12 inventory contains 1,231 entries. Its top-level groups are
`reb20-develop` (693 entries), `oldImage` (512), `ReBrewie-main` (19),
`old dts - collected them into one` (4), plus `brewie.dts` and
`first dmesg.txt`. Entry counts describe the captured folder only; they do not
make any file authoritative.

The first substantive pass selected the following narrowly scoped artifacts:

| Exact local path | SHA-256 | Evidence role |
| --- | --- | --- |
| `brewie.dts` | `06d56de96b826e13d2c95070aea218021bf755ff00f3023ff81a6a5a2a345f7f` | Later experimental overlay; its own comments label key pin assignments as assumptions. |
| `first dmesg.txt` | `69c037bbcced1863148f702fff04366e368223fc3ea7ac47c228eeb8252bfef8` | Later runtime capture from Linux 5.10.180; not an original-image log. |
| `NewOlimexDebianInfo.txt` | `1abc86106395e27b3cd6e1a80f13692a03cc77625f609cd53fd6730baeb86933` | Owner-requested fresh capture of `uname -a`, `/proc/cmdline`, `/proc/device-tree/model`, and complete `dmesg` from the later Olimex/Debian experiment. |
| `oldImage/Gamle Brewie software/uboot partition/boot.scr` | `375397d0cce1618a43479d3cb9508653289868377e79a6ae00bf5c31a1b72a78` | Captured legacy U-Boot script; historical boot configuration. |
| `oldImage/Gamle Brewie software/uboot partition/script.bin` | `f134c3f515df2343112d7fe4b493350f2b90794214f5fa4a78eb8480b4ebfeec` | Captured legacy Allwinner configuration binary; not decoded during this pass. |
| `oldImage/Gamle Brewie software/uboot partition/uEnv.txt` | `5c64ab9828e26e0525983192af9361c85aac3f79039280095ac2f1ff7744d3c7` | Captured legacy U-Boot environment fragment; it contains only a comment. |
| `oldImage/Gamle Brewie software/uboot partition/uImage` | `225637cdcd41e6d2df7a8a11f1294fb4f63e722abbdd2e377b9bf7248801af5a` | Captured legacy kernel image identified by its U-Boot header as `Linux-3.4.90-Brewie`. |
| `oldImage/Gamle Brewie software/usr/share/brewie/dmesg.txt` | `8c0712889e9adde309107317217702e76b588cdb7acaeb997b405da2892f92d8` | Runtime log from the captured original image; historical operational evidence. |

Also selected were `oldImage/gamle filer/script.fex.txt`, the DTS/DTSI files
under `oldImage/dts filer fra kernel image filer`, the small physical tracing
notes directly under `oldImage`, and the hardware/runtime sections of
`reb20-develop/Documentation/archived/HardwareMap_A13SOM_V0.md` and
`Brewie_A13_linux_setup_guide_working_updated20V0.5.md`. These are prior
investigations or configuration reconstructions, not factory records. Exact
line citations and source hashes must accompany any facts extracted from them.

The project owner clarified on 2026-08-12 that top-level `brewie.dts` was
probably created specifically for the later Olimex/Debian-image experiment.
It is therefore classified as an owner-created experimental configuration, not
an original Brewie artifact, factory device tree, or authoritative wiring
record. Its comments explicitly call its key pin assignments assumptions.

The legacy GUI executables and source, recipes, brewing state, MCU firmware
images/source, protocol-oriented material, and old application startup and
control-flow analyses were inventoried but excluded from substantive review.
They remain available only under a future, explicitly approved reference task
whose purpose is compatible with the clean-slate policy.

### Boundary incident and owner disposition

During the original Task 2 execution, a web opener automatically rendered part of the out-of-bound `FreeBrewie-SOM` repository-root README while the default branch was being resolved. No information from that render was selected, extracted, or used. On 2026-08-08, the project owner approved retaining this transparent disclosure on condition that a fresh agent independently audit Task 2 using only approved paths pinned to the already-recorded full commit SHAs.

That independent audit completed on 2026-08-08. It accessed no repository landing or root page and used only commit-pinned GitHub contents API or raw URLs for `FreeBrewie-MCU/Documentation`, `FreeBrewie-SOM/Docs`, the sole inventoried `Docs/UI_Design` subdirectory, the selected documents, and `Documentation/BrewieMCU.kicad_sch`. It reproduced both repository pins, the complete 9-entry MCU and 15-entry SOM inventories, every selection label and title, and all schematic structural/readability results. The audit corrected one presentation error in the readability report: the schematic is UTF-8 text, not strictly ASCII. No hardware fact was extracted and no design was produced during the audit.

## Pinned repositories

| Repository | Default branch | Immutable commit | Retrieved |
| --- | --- | --- | --- |
| `https://github.com/arjepsen/FreeBrewie-MCU` | `main` | `31efc798a4eff7208e3ed538215ef2ddfcc02884` | 2026-08-08 |
| `https://github.com/arjepsen/FreeBrewie-SOM` | `master` | `1f83897f73530abc02f598f07b8e61454768a26d` | 2026-08-08 |

The default branches and full 40-character commits were resolved with read-only `git ls-remote --symref`. All subsequent content reads used one of these full commit SHAs, never a moving branch name.

## MCU Documentation inventory

All entries below came from the pinned `FreeBrewie-MCU/Documentation` directory inventory. “Inferred title” means the excluded or supporting-only file was not opened merely to discover a display title.

| Path | Type | Title | Selection | Reason |
| --- | --- | --- | --- | --- |
| `Documentation/BrewieMCU.kicad_sch` | KiCad schematic | Not applicable | selected (inferred) | Explicitly authorised reverse-engineering artifact likely to expose software-relevant connectivity structures. |
| `Documentation/Brewie_MCU_Application_Flow_2026-08-01.md` | Markdown | Brewie MCU Application Flow (inferred title) | excluded | The filename indicates firmware flow and state-model design rather than hardware evidence. |
| `Documentation/Brewie_MCU_Pin_Map_Updated_2026-08-01.md` | Markdown | Brewie MCU Pin Map | selected | The title indicates direct software-relevant pin and connection evidence. |
| `Documentation/Brewie_MCU_Roadmap_Updated_2026-08-01.md` | Markdown | Brewie MCU Roadmap (inferred title) | excluded | The filename indicates planning and work ordering rather than hardware evidence. |
| `Documentation/Brewie_MCU_Runtime_Services_2026-08-01.md` | Markdown | Brewie MCU Runtime Services (inferred title) | excluded | The filename indicates runtime software responsibilities rather than hardware evidence. |
| `Documentation/Brewie_MCU_Structure_Notes_Updated_2026-08-01.md` | Markdown | Brewie MCU Structure Notes (inferred title) | supporting-only | A selected document identifies it as a companion for naming and ownership context; it is not primary hardware evidence and was not opened. |
| `Documentation/Brewie_SOM_MCU_Protocol_2026-08-01.md` | Markdown | Brewie SOM-MCU Protocol | selected | The title indicates software-relevant interface evidence for the SOM-to-MCU boundary. |
| `Documentation/README_2026-08-01.md` | Markdown | README (inferred title) | supporting-only | It is apparently an index useful only for locating or interpreting selected documentation and was not opened. |
| `Documentation/older_pinmapping.md` | Markdown | Older pin mapping (inferred title) | supporting-only | The filename indicates legacy mapping that may help explain conflicts but should not be treated as current evidence without a selected-item reference. |

## SOM Docs inventory

All entries below came from the pinned `FreeBrewie-SOM/Docs` inventory and its sole directory, `FreeBrewie-SOM/Docs/UI_Design`. Excluded files were classified from names and types and were not opened.

| Path | Type | Title | Selection | Reason |
| --- | --- | --- | --- | --- |
| `Docs/Brewie_SOM_MCU_Integration_Notes_2026-08-01.md` | Markdown | Brewie SOM-MCU Integration Notes | selected | The title indicates software-relevant physical/OS interface and integration evidence. |
| `Docs/Brewie_SOM_Platform_Notes_2026-08-04.md` | Markdown | Brewie SOM Platform Notes | selected | The title indicates platform, peripheral, and interface evidence. |
| `Docs/Brewie_SOM_Service_Autostart_2026-06-25.md` | Markdown | Brewie SOM Service Autostart (inferred title) | excluded | The filename indicates service deployment behavior rather than hardware evidence. |
| `Docs/FreeBrewie_Process_Plan_Design_2026-08-04.md` | Markdown | FreeBrewie Process Plan Design (inferred title) | excluded | The filename indicates brewing/application process design, which milestone 001 excludes. |
| `Docs/FreeBrewie_Recipe_Model_Decisions_2026-07-30.md` | Markdown | FreeBrewie Recipe Model Decisions (inferred title) | excluded | The filename indicates application-domain decisions rather than hardware evidence. |
| `Docs/FreeBrewie_SOM_Architecture_Notes_2026-08-04.md` | Markdown | FreeBrewie SOM Architecture Notes (inferred title) | excluded | The filename indicates software architecture rather than source evidence for hardware identity or connectivity. |
| `Docs/FreeBrewie_SOM_Development_Environment_Consolidated_2026-07-22.md` | Markdown | FreeBrewie SOM Development Environment (inferred title) | excluded | The filename indicates host, toolchain, and workflow material rather than hardware evidence. |
| `Docs/FreeBrewie_UI_Current_Status_2026-07-22.md` | Markdown | FreeBrewie UI Current Status | selected | The title and headings indicate likely software-relevant display and input observations. |
| `Docs/README_2026-08-04.md` | Markdown | README (inferred title) | supporting-only | It is apparently a documentation index and was not opened. |
| `Docs/UI_Design` | Directory | UI Design (inferred title) | excluded | The directory name indicates UI design, which milestone 001 excludes. |
| `Docs/UI_Design/FreeBrewie_Old_UI_Map_2026-07-05.html` | HTML | FreeBrewie Old UI Map (inferred title) | excluded | The filename indicates historical UI mapping rather than hardware evidence. |
| `Docs/UI_Design/FreeBrewie_UI_Design_Spec_2026-07-03.html` | HTML | FreeBrewie UI Design Spec (inferred title) | excluded | The filename indicates UI design, which milestone 001 excludes. |
| `Docs/UI_Design/FreeBrewie_UI_Navigation_Mockups_2026-07-03.md` | Markdown | FreeBrewie UI Navigation Mockups (inferred title) | excluded | The filename indicates UI navigation design rather than hardware evidence. |
| `Docs/UI_Design/FreeBrewie_UI_UX_Philosophy_2026-07-04.md` | Markdown | FreeBrewie UI/UX Philosophy (inferred title) | excluded | The filename indicates UX design rather than hardware evidence. |
| `Docs/optimizing_cpp.pdf` | PDF | Optimizing C++ (inferred title) | excluded | The filename indicates software optimisation guidance rather than hardware evidence. |

## Directly referenced supporting artifacts

The selected MCU pin-map and protocol documents name the MCU structure notes as a companion. That entry remains supporting-only and was not opened. Their other named companions are already excluded above because their apparent subjects are software flow, runtime services, or planning.

The selected schematic structurally contains nine non-placeholder datasheet URLs. They are supporting-only references, were not opened, and do not affect S-expression parsing:

- `http://ww1.microchip.com/downloads/en/DeviceDoc/20002249B.pdf`
- `http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-2549-8-bit-AVR-Microcontroller-ATmega640-1280-1281-2560-2561_datasheet.pdf`
- `http://www.ti.com/lit/ds/symlink/lm35.pdf`
- `http://www.ti.com/lit/ds/symlink/lmv324.pdf`
- `http://www.ti.com/lit/ds/symlink/tps54202.pdf`
- `http://www.ti.com/lit/gpn/SN65HVD51`
- `https://www.diodes.com/assets/Datasheets/ds30396.pdf`
- `https://www.ti.com/lit/ds/symlink/sn74lvc1g08.pdf`
- `https://www.vishay.com/doc?85881`

The schematic also contains the legacy datasheet placeholder `~`; this is not a retrievable artifact.

## Excluded sources and paths

No source-code directory, repository clone, historical repository, other repository path, or moving-branch content URL is approved. Excluded inventory files were not opened, and no contents/raw API endpoint outside `FreeBrewie-MCU/Documentation`, `FreeBrewie-SOM/Docs`, or a directly referenced supporting artifact was intentionally used. A GitHub repository landing page used during the original default-branch resolution automatically rendered part of the SOM root README; that out-of-bound content was not selected, extracted, or used. The deviation, owner disposition, and clean independent audit are retained here and in the Task 2 execution and boundary-audit reports.

## Boundary-expansion requests

### Task 5 authoritative external document pin

The manufacturer document used to verify the fitted SOM product variant's nominal capacity is Olimex, *A13-SOM-256 and A13-SOM-512 User's Manual*, revision B, March 2015, URL `https://www.olimex.com/Products/SOM/A13/A13-SOM-512/resources/A13-SOM-um.pdf`, downloaded artifact SHA-256 `f0544df121fad9b8e0a5ae1b039e123569e1d51c7f9a6411e4c967eb8795fc2d`. Sections 1.3-1.5, page 7, define the `-256` and `-512` suffixes as RAM-indicating product variants and specify the latter as 512 MB DDR3. The owner's direct fitted-module marking reads `Olimex A13-SOM (512)`, PCB revision `G`; Olimex's official A13-SOM documentation at `https://www.olimex.com/wiki/A13-SOM` explicitly uses `A13-SOM-512 revision G` nomenclature. Together these sources establish nominal installed capacity only, not exact DDR3 vendor, part, timings, runtime availability, or current health.

On 2026-08-10 the owner removed exact DDR3 package identity from milestone scope because the package faces the carrier and viewing it would require separating fragile small connectors, creating more damage risk than evidentiary value. Connector separation must not be requested for this purpose.

### Pending Task 3 compute-platform evidence request

The originally selected project documents did not establish the exact SOM revision, carrier-board identity or revision, MCU board identity or revision, SOM RAM configuration, boot hardware or boot-media identity, persistent-storage identity or capacity, or networking hardware. Subsequent owner observations and Task 5 authoritative documentation now establish the fitted SOM and carrier markings, fitted MCU model marking, and nominal 512 MB SOM capacity in HW-001, HW-002, HW-094, and HW-095. Exact DDR3 package identity is an owner-approved removal. To close the remaining required evidence categories, the project owner must provide or approve exact read-only paths for authoritative carrier and MCU board schematics, BOM or assembly records, part-specific boot, storage, and networking documentation, and authoritative evidence for compute-side interrupt and watchdog candidates. No additional repository path, root content, source code, or supporting artifact may be inspected until that approval is recorded against milestone 001.

Any later need to inspect another path outside the approved boundary, resolve footprint-library content, or use a historical repository likewise requires project-owner approval recorded against milestone 001 before inspection.

### Pending Task 4 device and interconnect evidence request

The selected approved documents provide candidate MCU mappings and limited connector structures, but they do not establish the exact identities or revisions of the pumps, pump DAC, mass/pressure/water-level devices, temperature sensors, heater drive stages, valves, inlet solenoids, fan, current-sense circuits, AC-measure circuit, buttons, indicators, or their connectors. They also do not establish most signal voltages, active polarities, pull-ups, scaling, calibrated limits, complete pin-to-net connectivity, or the present connection state of each device. The pin-map ADC-count observations for the inlet solenoids omit measurement apparatus, test conditions, calibration, and uncertainty and therefore cannot be accepted as characterized limits.

To close these gaps, the project owner must provide or approve exact read-only paths for authoritative board schematics and native netlists tied to the inspected revision; BOM and assembly records; connector drawings and harness pinouts; readable device markings and part-specific datasheets; dated photographs or inspection records for the current machine; and existing characterization reports that include apparatus, conditions, calibration, and uncertainty. The request also includes the exact immutable kernel/device-tree artifact needed to resolve the current A13 PB2 PWM assignment. The present unpopulated audio-amplifier state is now verified in HW-071, and buzzer/audio availability was removed from the milestone's required baseline by the owner on 2026-08-10; exact audio-path evidence is therefore no longer a milestone blocker. No additional repository path, root content, source code, footprint library, moving-branch artifact, or unapproved device document may be inspected until approval is recorded against milestone 001.
