# Milestone: Hardware baseline

- Milestone ID: 001
- Status: active
- Owner: Project owner
- Purpose: Establish verified hardware facts for the existing device before later requirements work.
- Last completion review: 2026-08-12

## Approval and authorised source boundary

This milestone is authorised by the approved
[hardware-baseline design](../superpowers/specs/2026-08-08-hardware-baseline-design.md).
Selective reference inspection may begin only after this activation commit.

The exact read-only repository boundary is:

- `https://github.com/arjepsen/FreeBrewie-MCU`, limited to hardware-relevant
  documents in `Documentation/`, directly referenced schematics, images,
  diagrams, and datasheets, and `Documentation/BrewieMCU.kicad_sch`; and
- `https://github.com/arjepsen/FreeBrewie-SOM`, limited to hardware-relevant
  documents in `Docs/` and directly referenced schematics, images, diagrams,
  and datasheets.

`Documentation/BrewieMCU.kicad_sch` is explicitly permitted as non-authoritative
inferred reverse-engineering evidence. No other online repository path or
historical repository is authorised by this original boundary; the later,
bounded filename-only and local `OldStuff` exceptions are recorded below.

### Filename-only inventory expansion

On 2026-08-12, the project owner approved a metadata-only expansion for the two
pinned previous-work repositories. The project may list repository-relative
path names and Git object types at commits
`31efc798a4eff7208e3ed538215ef2ddfcc02884` (FreeBrewie-MCU) and
`1f83897f73530abc02f598f07b8e61454768a26d` (FreeBrewie-SOM) solely to identify
candidate evidence paths for a later approval request.

This expansion does not authorise reading file contents, following symlinks or
submodules, resolving moving branches, or using path names as hardware evidence.
Every candidate file still requires explicit project-owner approval before its
contents may be inspected.

### Local historical evidence expansion

On 2026-08-12, the project owner approved thorough read-only inspection of
`/home/anders/Documents/OldStuff`. Permitted evidence classes are verified or
candidate hardware facts, historical Linux-image facts, boot/kernel/device-tree
observations, and prior physical-investigation records.

Legacy application architecture, module structure, brewing/control logic,
state machines, communication-protocol design, and implementation source remain
non-reusable. When they are encountered incidentally, they must not become
requirements or design inputs. The local folder remains external to this
repository and none of its contents may be imported wholesale or used as a
build dependency.

## Authorised work

Once separately approved, identify and verify:

- the exact SOM and revision;
- the exact MCU and revision;
- the carrier board and revision;
- the identities and revisions, where applicable, of relevant peripherals,
  including storage, memory, display, input hardware, and attached devices;
- all material buses and connections among the SOM, MCU, carrier board, and
  relevant peripherals; and
- the source, confidence, status, conflicts, and assumptions for each material fact.

## Explicit exclusions

Linux design, application design, firmware design, protocol design, brewing-logic
design, and UI design are excluded. This milestone does not authorise any
implementation or technical subsystem design.

## Evidence permitted

After approval, permitted evidence is hardware facts recorded with the
[hardware-fact template](../templates/hardware-fact.md), supported by
authoritative documents and direct hardware observations where available. Each
material fact must retain its source, confidence, status, conflicts, and
assumptions. Historical repositories remain external, read-only, and unimported;
only the listed evidence classes in the 2026-08-12 local `OldStuff` exception
may be inspected, and legacy application implementation remains excluded.

## Reference-inspection authority

Inspection is limited to the approved source boundary above and only for hardware
facts needed for this milestone. Historical repositories remain unauthorised
except for the two pinned online documentation paths and the bounded,
read-only 2026-08-12 `OldStuff` exception above.

## Deliverables

- Verified hardware-fact records for each material SOM, MCU, carrier-board, and
  relevant peripheral identity and each material connection.
- A baseline summary that links each material fact to its evidence record.
- A record of conflicts, assumptions, confidence, verification status, and
  dependent decisions for every material fact.
- A record of every baseline item removed as unnecessary, including the owner's
  explicit approval and the reason for removal.

## Measurable completion criteria

- Every material disputed fact has exactly one reviewed disposition in the
  platform-enablement triage registry.
- No unresolved `before requirements` platform blocker remains when
  Linux-image requirements are activated.
- Every first-bring-up blocker and constraint remains explicit and enforceable
  until its fact is resolved.
- Every deferral and candidate or approved removal is traceable to its affected
  records, safe default, milestone, and owner decision where required.
- A baseline item is removed only when the owner explicitly approves its
  removal and the milestone records why the item is unnecessary.
- Every material fact completes the mandatory provenance fields and identifies
  its confidence, status, conflicts, and assumptions.
- Consistency, provenance, clean-slate, and safety reviews pass or are
  explicitly marked inapplicable with a reason.

Linux-image requirements may be activated when their evidence gate passes even
while milestone 001 remains active for first-bring-up constraints, later
dependencies, or pending owner decisions.

## Current completion-review status

Milestone 001 remains active. The current baseline contains 108 indexed records:
23 verified and 85 disputed, with no proposed or provisionally accepted facts.
The [baseline's disputed-fact table](../evidence/hardware/baseline.md#all-disputed-facts-and-bounded-decisions)
records every disputed fact and its bounded decision. The
[platform-enablement triage](../evidence/hardware/platform-enablement-triage.md)
classifies all 80 material disputed facts as 0 platform blockers, 10 platform
constraints, 10 integration dependencies, 46 brewing-device dependencies, 9
non-blocking references, and 5 candidate removals.

Five disputed audio records, HW-068 through HW-070, HW-079, and HW-081, are
non-material to this gate because the owner removed buzzer/audio availability
from the milestone on 2026-08-10. No unresolved `before requirements` platform
blocker remains, so Linux-image requirements and independent design may begin.
Milestone 001 stays active because ten first-bring-up constraints and five
pending candidate-removal decisions remain, alongside later integration and
brewing-device evidence:

- Former category gaps are now bounded by dated runtime evidence: HW-007 and
  HW-008 identify/enumerate the Goodix touchscreen in the modern boot;
  HW-101 through HW-104 record the legacy kernel, community-edited Buildroot
  userspace, active SD/MMC/EXT3 layout, and RTC detection; HW-105 through
  HW-107 record the modern experimental platform values, watchdog settings,
  and runtime-enumerated Realtek USB WLAN use; and HW-108 records shared Linux UART
  enumeration. These are historical observations, not physical verification or
  selected clean-slate requirements.
- Material compute/platform gaps remain: exact fitted display and touch-part
  identity; display timing; boot-media and persistent-storage hardware;
  permanent networking and RTC hardware; revision-matched carrier evidence;
  physical UART/MCU connectivity and telemetry; interrupt/reset/supply routing;
  and electrical characteristics. Historical partition sizes, EXT3, kernel
  versions, Buildroot, the old captured watchdog behavior, and the Realtek
  adapter do not select a future Linux image, storage layout, watchdog policy,
  networking design, or other platform requirement. Those choices require
  later requirements analysis.
- Brewing-device identities, connections, electrical constraints, limits, and
  present-machine state remain incomplete. The exact indexed blockers are
  HW-019 through HW-067, HW-073 through HW-078, HW-080, and HW-084 through
  HW-091.
- Current SOM pin-mux, GPIO-numbering, PWM-consumer, period, and polarity
  evidence remains incomplete in HW-072, HW-082, HW-083, HW-092, and HW-093.

Productive verification work remains possible, so the milestone stays active
and does not meet the policy threshold for blocked status. The project owner
can enable the next verification pass by approving exact read-only evidence
paths for the two requests in the
[source ledger](../evidence/hardware/sources.md#boundary-expansion-requests):

1. Revision-matched carrier and MCU board schematics, native netlists, BOMs,
   assembly records, and part-specific boot/storage/networking/RTC/interrupt/
   reset/watchdog documentation for the remaining physical compute-platform
   gaps.
2. Revision-matched schematics/netlists, BOMs and assembly records, connector
   drawings and harness pinouts, readable device markings and part-specific
   datasheets, dated machine inspection evidence, complete characterization
   reports, and the immutable kernel/device-tree artifact for device and
   interconnect gaps.

No continuity or powered measurement is approved. If documentary and safe
visual evidence prove insufficient, each proposed measurement requires its own
safety-reviewed procedure and separate owner approval. Alternatively, a material
item may leave scope only through a register entry naming the item, why it is
unnecessary, the owner's approval, and the approval date.

## Assumptions

Before approval, no hardware assumption is accepted. After approval, provisional
use requires recorded high confidence, time-consuming verification, and a delay
that would impede progress. The record must state why those conditions are met,
the cheapest available check, the verification action, and every
safety-critical, consequential, or hard-to-reverse decision blocked until
verification.

## Dependent decisions

Later Linux-image requirements and design may use verified facts as conclusions
and disputed facts only through the triage registry's explicit constraints,
safe defaults, deadlines, and named dependencies. No disputed proposition may
be treated as verified.

## Required reviews

- Scope review: pass on 2026-08-12; every deliverable is authorised by this
  milestone, all explicit exclusions remained excluded, and no source-boundary
  expansion occurred without owner approval.
- Provenance review: pass on 2026-08-12 for all 108 fact records; each record
  identifies its source and location, extraction date, extractor, dependent
  decisions, direct or inferred basis, independent confirmation, conflicts,
  and limitations.
- Assumption review: pass on 2026-08-12 for all 108 fact records; every record
  states confidence, cheapest useful check, verification action, and blocked
  decisions. No fact is provisionally accepted, and consequential use of every
  unverified in-scope fact remains blocked.
- Independent-decision review: inapplicable unless a decision is introduced;
  hardware discovery introduced no technical decision.
- Asset review: inapplicable unless an asset is considered; any such review
  requires separate authorised scope, and no asset was considered.
- Completion review: milestone remains active on 2026-08-16. All 80 material
  disputed facts now have reviewed dispositions and no requirements blocker
  remains, but first-bring-up constraints, pending candidate removals, and later
  integration evidence remain open. Conflicts, debt, removals, safe defaults,
  and bounded decisions remain visible in the triage, verification register,
  and baseline.

## Approval

- Approved by and date: Project owner, 2026-08-08.
- Scope expansion approval by owner and date: Filename-only inventory and local
  historical-evidence expansions approved by the project owner on 2026-08-12,
  subject to the boundaries recorded above; no broader expansion is authorised.

## Next milestone

[Linux-image requirements and design](../roadmap.md) may now be activated under
its own approval because the evidence gate has no `before requirements`
blockers. Linux-image implementation and first powered bring-up remain inactive;
the latter remains subject to every recorded first-bring-up constraint.
