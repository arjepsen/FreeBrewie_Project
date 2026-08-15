# Minimum Platform-Enablement Evidence Gate Design

Date: 2026-08-16
Status: approved in conversation; awaiting written-spec review

## Purpose

Define the smallest verified hardware baseline needed to begin clean-slate
Linux-image requirements and bring-up safely. The current count of disputed
hardware facts is not itself a useful gate: a fact blocks progress only when an
upcoming platform decision depends on it or an incorrect assumption could make
initial bring-up unsafe or materially misdirected.

This work classifies the existing disputed facts. It does not design or build a
Linux image, SOM application, MCU firmware, communication protocol, UI, brewing
logic, or hardware-control behavior.

## Clean-slate and evidence boundary

All existing clean-slate and reference-material restrictions remain in force.
Historical sources may establish verified or candidate hardware facts,
historical Linux-image facts, boot/kernel/device-tree observations, external
behavior, and prior physical-investigation records within their approved
read-only boundaries. Legacy implementation architecture, module structure,
control logic, state machines, communication-protocol design, brewing logic,
and source code cannot become requirements or design inputs.

This classification must not convert a historical implementation choice into a
new requirement. Historical filesystems, kernel versions, boot arguments,
drivers, partition layouts, frameworks, and runtime policies remain
observations unless independently selected during later requirements work.

## Scope

The milestone will:

- classify every material disputed fact by its effect on platform enablement;
- identify the facts that must be resolved before Linux-image requirements,
  before first powered bring-up, or before a later integration stage;
- record safe constraints for unresolved facts;
- defer brewing-device and other later-stage facts explicitly;
- identify facts that are useful context but do not block an upcoming decision;
- identify candidate scope removals for separate owner approval; and
- revise milestone 001 so completion depends on consequential platform
  blockers rather than every potentially useful hardware detail.

The milestone will not:

- choose a Linux distribution, build system, kernel version, bootloader,
  filesystem, update mechanism, UI toolkit, or application architecture;
- create or boot a new image;
- define SOM-MCU messages or protocol behavior;
- design MCU firmware or brewing control;
- energize, probe, command, or characterize heaters, pumps, valves, sensors, or
  other brewing hardware; or
- authorize continuity tests, powered measurements, or physical operations.

## Platform-enablement target

The evidence gate exists to support a later minimal bring-up capable of:

- booting reliably on the fitted A13-SOM;
- accessing an identified boot medium and persistent storage without
  unintentionally destroying material retained data;
- presenting a basic display test output;
- receiving touchscreen input;
- exposing the Linux serial controller intended for later SOM-MCU integration;
- keeping MCU reset or isolation behavior bounded during early testing;
- avoiding accidental activation of heaters, pumps, valves, and other outputs;
  and
- retaining a diagnostic or recovery path if display or networking is
  unavailable.

These are evidence dependencies, not an image design. The later requirements
and design milestone remains responsible for deciding how to satisfy them.

## Classification model

Every material disputed fact receives exactly one primary disposition.

### 1. Platform blocker

Verification is required before Linux-image requirements or first powered
bring-up because a wrong assumption could prevent boot, damage hardware,
activate an unsafe output, destroy material data, or force a major redesign.
The disposition must name the exact decision and the required verification
deadline.

### 2. Platform constraint

The fact does not prevent requirements work, but it restricts what an initial
image may configure, drive, probe, or enable. The affected interface remains
disabled or untouched until the fact is resolved.

### 3. Integration dependency

The fact is needed for later SOM-MCU integration or controlled hardware access,
but not for an initial minimal Linux platform. Its target integration milestone
must be named.

### 4. Brewing-device dependency

The fact is needed for pumps, heaters, valves, sensors, calibration, brewing
behavior, or associated safety validation. It is deferred to a later
hardware-control or brewing-device milestone.

### 5. Non-blocking reference

The fact is useful context but does not control a currently planned decision.
It remains visible with its evidence status and limitations.

### 6. Candidate removal from required scope

The fact has no necessary role in the intended new system. Classification alone
does not remove it: removal requires explicit owner approval, reason, and date
in the verification register and milestone record.

## Classification rule

A fact may be a platform blocker only when its disposition names:

1. the exact upcoming decision or operation;
2. the credible consequence if the fact is wrong;
3. why a safe constraint cannot permit progress; and
4. the cheapest reliable verification method.

“Might be useful,” general completeness, or similarity to the old system is not
sufficient. When an unresolved fact can be isolated safely, it is a platform
constraint or later dependency rather than a blocker.

## Initial enablement gate

The triage must determine whether sufficient evidence exists for these areas:

### Boot path and recovery

- supported boot medium and relevant boot-order facts;
- a recovery or diagnostic path that does not depend on the graphical UI; and
- boundaries preventing accidental modification of retained media or data.

### Storage

- identity and role of available boot and persistent-storage devices; and
- which media may be overwritten, must be preserved, or remain untouched.

### SOM and carrier essentials

- revision-relevant power, clock, reset, and essential carrier connections
  needed for boot and safe operation; and
- any unresolved carrier signal that must remain disabled during bring-up.

### Display

- physical interface and defensible initial display mode;
- required power, enable, and backlight controls; and
- safe defaults for control lines whose polarity or routing remains disputed.

### Touchscreen

- runtime bus, address, and driver-family observations;
- supply constraints; and
- required reset or interrupt controls, or a safe method to defer them.

### MCU isolation and external-output safety

- which SOM-controlled lines can reset, power, or communicate with the MCU;
- how early Linux testing can avoid unpredictable MCU interaction; and
- which lines could indirectly activate brewing hardware and must remain
  unconfigured or safely constrained.

### Console and diagnostics

- at least one known diagnostic path suitable for initial bring-up; and
- recovery expectations if display, touch, or networking is unavailable.

Networking hardware identity, RTC identity, watchdog policy, the application
framework, complete SOM-MCU communication, and brewing devices do not block the
initial Linux requirements milestone unless triage demonstrates a direct boot,
recovery, data-preservation, or safety dependency.

## Triage record

Each material disputed fact must have one row containing:

- record ID and concise claim;
- primary disposition;
- exact upcoming decision or later milestone affected;
- consequence if the claim is wrong;
- safe default while unresolved;
- verification deadline: before requirements, before first powered bring-up,
  before named integration, or deferred;
- cheapest reliable verification method;
- current evidence type, confidence, and status; and
- owner approval reference when removal is proposed or accepted.

The canonical hardware-fact record remains the authority for the fact and its
evidence. The triage table records dependency and scheduling disposition; it
must not restate disputed claims as verified facts.

## Deliverables

1. A complete disposition table covering every material disputed fact exactly
   once.
2. A short platform-blocker register naming the decision, consequence,
   verification deadline, and cheapest reliable check for each blocker.
3. A first-bring-up safety-constraint list stating what must remain disabled,
   isolated, preserved, or untouched.
4. A deferred-work register grouped by integration, brewing-device, and other
   later milestones.
5. A candidate-removal register requiring explicit owner decisions.
6. Revised milestone-001 completion criteria and completion review.
7. An explicit evidence-based decision on whether Linux-image requirements work
   may begin and which capabilities remain prohibited.

## Consistency and review rules

Deterministic checks must confirm:

- every material disputed fact appears exactly once in the disposition table;
- every referenced fact ID exists;
- every disposition uses one allowed category;
- every platform blocker names a concrete decision, credible consequence,
  verification deadline, and reliable check;
- every unresolved platform constraint states a safe default;
- every deferral names its later milestone class;
- every removal remains pending until owner approval is recorded; and
- counts agree across the disposition table, verification register, baseline,
  and milestone review.

A clean-slate review must confirm that no classification adopts a legacy
architecture, implementation, configuration, or behavior as a new design
choice. A safety review must confirm that classification does not itself
authorize powered testing, probing, continuity measurements, output activation,
or handling beyond the already approved machine state.

## Failure and uncertainty handling

If evidence is insufficient, the fact remains disputed. The affected capability
stays disabled, isolated, preserved, or blocked according to its disposition.
The project must not invent a conclusion merely to advance the milestone.

If a fact cannot be classified without knowing a later design choice, it is
recorded as a constraint on that future choice rather than treated as a current
blocker. If classification reveals that a supposedly deferred fact directly
affects boot, recovery, data preservation, or safe isolation, it is promoted to
the blocker register with the reason recorded.

## Completion criteria

This design-and-triage milestone is complete when:

- all material disputed facts have exactly one reviewed disposition;
- all current platform blockers and first-bring-up constraints are explicit;
- deferrals and candidate removals are complete and traceable;
- milestone 001 completion criteria reflect consequential dependencies rather
  than raw verification count;
- required consistency, provenance, clean-slate, and safety reviews pass; and
- the project records whether Linux-image requirements may start.

The gate may permit Linux-image requirements to begin while facts remain
disputed. It may not permit an affected interface or powered operation beyond
the constraints supported by verified evidence.
