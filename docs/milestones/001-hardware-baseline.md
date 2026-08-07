# Milestone: Hardware baseline

- Milestone ID: 001
- Status: proposed
- Owner: Project owner
- Purpose: Establish verified hardware facts for the existing device before later requirements work.

## Entry criteria

A separate brainstorming and approval cycle must define and approve this
milestone before any work or reference inspection begins.

## Authorised work

Once separately approved, identify and verify:

- the exact SOM and revision;
- the exact MCU and revision;
- the carrier board and revision;
- storage, memory, display, and input hardware;
- buses and connections among the SOM, MCU, and attached devices; and
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

No inspection is authorised by this proposed record. After a separate approval,
historical repositories may be inspected only for hardware facts needed for this
milestone. The approved record must name the purpose, source boundary, permitted
evidence classes, approver, and approval date before inspection.

## Deliverables

- Verified hardware-fact records for each material hardware item and connection.
- A baseline summary that links each material fact to its evidence record.
- A record of conflicts, assumptions, confidence, verification status, and
  dependent decisions for every material fact.

## Measurable completion criteria

- The SOM, MCU, carrier board, storage, memory, display, and input hardware have
  exact identified revisions or explicitly recorded unresolved status.
- Connections among the SOM, MCU, and attached devices are recorded with their
  supporting hardware facts.
- Every material fact identifies its source, confidence, status, conflicts, and
  assumptions.
- Material facts affecting consequential decisions are verified or keep those
  decisions blocked.
- Required reviews pass or are explicitly marked inapplicable with a reason.

## Assumptions

Before approval, no hardware assumption is accepted. Any later assumption must
state confidence, the cheapest available check, a verification action, and the
consequential decisions blocked until verification.

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

- Approved by and date: Not approved; separate brainstorming and approval required.
- Scope expansion approval by owner and date: No scope expansion is authorised.

## Next milestone

[Linux-image requirements and design](../roadmap.md) may be proposed only after
this milestone is completed and its verified facts are available.
