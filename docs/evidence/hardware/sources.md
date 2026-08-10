# Hardware evidence sources

## Inspection authority

Inspection is authorised by active milestone 001, `docs/milestones/001-hardware-baseline.md`, as approved by the project owner on 2026-08-08. The allowed read-only boundary is:

- `https://github.com/arjepsen/FreeBrewie-MCU`, limited to `FreeBrewie-MCU/Documentation`, directly referenced supporting schematics, images, diagrams, and datasheets, and `FreeBrewie-MCU/Documentation/BrewieMCU.kicad_sch`; and
- `https://github.com/arjepsen/FreeBrewie-SOM`, limited to `FreeBrewie-SOM/Docs` and directly referenced supporting schematics, images, diagrams, and datasheets.

`FreeBrewie-MCU/Documentation/BrewieMCU.kicad_sch` is selected as non-authoritative, inferred reverse-engineering evidence. Repositories were accessed read-only and were not cloned. An inventory entry records an evidence-selection decision; it does not validate the item's contents or establish a hardware fact.

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

### Pending Task 3 compute-platform evidence request

The selected approved documents do not establish the exact SOM revision, carrier-board identity or revision, MCU board identity or revision, SOM RAM configuration, boot hardware or boot-media identity, persistent-storage identity or capacity, or networking hardware. To close those required evidence categories, the project owner must provide or approve exact read-only paths for authoritative SOM, carrier, and MCU board markings, schematics, BOM or assembly records, and part-specific boot, storage, and networking documentation. No additional repository path, root content, source code, or supporting artifact may be inspected until that approval is recorded against milestone 001.

Any later need to inspect another path outside the approved boundary, resolve footprint-library content, or use a historical repository likewise requires project-owner approval recorded against milestone 001 before inspection.

### Pending Task 4 device and interconnect evidence request

The selected approved documents provide candidate MCU mappings and limited connector structures, but they do not establish the exact identities or revisions of the pumps, pump DAC, mass/pressure/water-level devices, temperature sensors, heater drive stages, valves, inlet solenoids, fan, current-sense circuits, AC-measure circuit, buttons, indicators, or their connectors. They also do not establish most signal voltages, active polarities, pull-ups, scaling, calibrated limits, complete pin-to-net connectivity, or the present connection state of each device. The pin-map ADC-count observations for the inlet solenoids omit measurement apparatus, test conditions, calibration, and uncertainty and therefore cannot be accepted as characterized limits.

To close these gaps, the project owner must provide or approve exact read-only paths for authoritative board schematics and native netlists tied to the inspected revision; BOM and assembly records; connector drawings and harness pinouts; readable device markings and part-specific datasheets; dated photographs or inspection records for the current machine; and existing characterization reports that include apparatus, conditions, calibration, and uncertainty. The request also includes the exact immutable kernel/device-tree artifact needed to resolve the current A13 PB2 PWM assignment and the exact carrier/audio assembly evidence needed to verify the removed amplifier state. No additional repository path, root content, source code, footprint library, moving-branch artifact, or unapproved device document may be inspected until approval is recorded against milestone 001.
