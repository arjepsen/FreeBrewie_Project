# Milestone: Hardware baseline

- Milestone ID: 001
- Status: active
- Owner: Project owner
- Purpose: Establish verified hardware facts for the existing device before later requirements work.
- Last completion review: 2026-08-10

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
inferred reverse-engineering evidence. No other repository path or historical
repository is authorised.

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
assumptions. Historical repositories remain external, read-only, and unimported.

## Reference-inspection authority

Inspection is limited to the approved source boundary above and only for hardware
facts needed for this milestone. Historical repositories remain unauthorised
except for the two permitted repository paths above.

## Deliverables

- Verified hardware-fact records for each material SOM, MCU, carrier-board, and
  relevant peripheral identity and each material connection.
- A baseline summary that links each material fact to its evidence record.
- A record of conflicts, assumptions, confidence, verification status, and
  dependent decisions for every material fact.
- A record of every baseline item removed as unnecessary, including the owner's
  explicit approval and the reason for removal.

## Measurable completion criteria

- The material SOM, MCU, and carrier-board identities and revisions are
  verified.
- The identities and applicable revisions of all relevant peripherals,
  including storage, memory, display, input hardware, and attached devices, are
  verified.
- All material connections among the SOM, MCU, carrier board, and relevant
  peripherals are verified in supporting hardware-fact records.
- A baseline item is removed only when the owner explicitly approves its
  removal and the milestone records why the item is unnecessary.
- Every material fact completes the mandatory provenance fields and identifies
  its confidence, status, conflicts, and assumptions.
- Material facts affecting consequential decisions are verified or keep those
  decisions blocked.
- Required reviews pass or are explicitly marked inapplicable with a reason.

Any unresolved material baseline fact that has not been removed under the
owner-approved exception keeps the milestone active or blocked; the milestone
cannot be marked complete.

## Current completion-review status

Milestone 001 remains active. The current baseline contains 100 indexed records:
13 verified and 87 disputed, with no proposed or provisionally accepted facts.
The [baseline's disputed-fact table](../evidence/hardware/baseline.md#all-disputed-facts-and-blocked-decisions)
records every disputed fact and its blocked or bounded decision.

Five disputed audio records, HW-068 through HW-070, HW-079, and HW-081, do not
block completion because the owner removed buzzer/audio availability from this
milestone on 2026-08-10. The remaining 82 disputed facts are material and keep
the milestone active:

- Compute/platform identity, revision, boot, storage, networking, display,
  input, SOM-MCU link, reset, and power-control evidence remains incomplete.
  The exact indexed blockers are HW-004 through HW-014 and HW-017 through
  HW-018, together with the unindexed boot-hardware, persistent-storage,
  networking-hardware, interrupt, watchdog, and revision-matched carrier/MCU
  board evidence gaps recorded in the
  [verification register](../evidence/hardware/verification-register.md#verification-debt).
- Brewing-device identities, connections, electrical constraints, limits, and
  present-machine state remain incomplete. The exact indexed blockers are
  HW-019 through HW-067, HW-073 through HW-078, HW-080, and HW-084 through
  HW-091.
- Current SOM pin-mux, GPIO-numbering, PWM-consumer, period, and polarity
  evidence remains incomplete in HW-072, HW-082, HW-083, HW-092, and HW-093.

Progress remains possible and the milestone therefore does not meet the policy
threshold for blocked status. The project owner can enable the next verification
pass by approving exact read-only evidence paths for the two requests in the
[source ledger](../evidence/hardware/sources.md#boundary-expansion-requests):

1. Revision-matched carrier and MCU board schematics, native netlists, BOMs,
   assembly records, and part-specific boot, storage, networking, interrupt,
   and watchdog documentation for the compute-platform gaps.
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

Later Linux-image requirements and design, system requirements, and subsystem
planning may depend only on verified material hardware facts.

## Required reviews

- Scope review: pass on 2026-08-10; every deliverable is authorised by this
  milestone, all explicit exclusions remained excluded, and no source-boundary
  expansion occurred without owner approval.
- Provenance review: pass on 2026-08-10 for all 100 fact records; each record
  identifies its source and location, extraction date, extractor, dependent
  decisions, direct or inferred basis, independent confirmation, conflicts,
  and limitations.
- Assumption review: pass on 2026-08-10 for all 100 fact records; every record
  states confidence, cheapest useful check, verification action, and blocked
  decisions. No fact is provisionally accepted, and consequential use of every
  unverified in-scope fact remains blocked.
- Independent-decision review: inapplicable unless a decision is introduced;
  hardware discovery introduced no technical decision.
- Asset review: inapplicable unless an asset is considered; any such review
  requires separate authorised scope, and no asset was considered.
- Completion review: fail on 2026-08-10. The measurable identity, connection,
  capability/limit, and complete verified-baseline criteria do not pass while
  82 in-scope material facts and the unindexed category gaps above remain
  unresolved. Conflicts, debt, owner-approved removals, and blocked decisions
  remain visible in the verification register and baseline.

## Approval

- Approved by and date: Project owner, 2026-08-08.
- Scope expansion approval by owner and date: No scope expansion is authorised.

## Next milestone

[Linux-image requirements and design](../roadmap.md) remains proposed and
inactive. It may not be activated until this milestone is completed and its
verified facts are available.
