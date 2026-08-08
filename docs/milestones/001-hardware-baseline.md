# Milestone: Hardware baseline

- Milestone ID: 001
- Status: active
- Owner: Project owner
- Purpose: Establish verified hardware facts for the existing device before later requirements work.

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

- Scope review: required after separate approval.
- Provenance review: required for every material hardware fact.
- Assumption review: required for every material assumption.
- Independent-decision review: inapplicable unless a decision is introduced;
  hardware discovery alone is not a technical decision.
- Asset review: inapplicable unless an asset is considered; any such review
  requires separate authorised scope.
- Completion review: required before this milestone can be complete.

## Approval

- Approved by and date: Project owner, 2026-08-08.
- Scope expansion approval by owner and date: No scope expansion is authorised.

## Next milestone

[Linux-image requirements and design](../roadmap.md) may be proposed only after
this milestone is completed and its verified facts are available.
