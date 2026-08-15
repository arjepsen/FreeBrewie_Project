# Historical Evidence Integration Design

Date: 2026-08-12
Status: approved; implementation and correction wave complete; final branch review and PR approval pending

## Purpose

Integrate the approved local historical evidence and fresh runtime captures into
the existing hardware-evidence model so milestone 001 accurately represents
what is known, what is merely corroborated, and what remains unresolved.

This work does not design or implement the Linux image, SOM application, MCU
firmware, SOM–MCU protocol, brewing logic, or UI. Historical implementation
architecture, control logic, state machines, protocol design, module structure,
and source code remain prohibited as design inputs.

## Selected approach

Extend the existing `HW-xxx` evidence model rather than leaving the archive as
an isolated report or creating a second historical registry.

- Update an existing fact when the new evidence addresses the same narrowly
  worded proposition.
- Create a new atomic fact only when the observation is absent from the current
  registry and is software-relevant.
- Keep source provenance and evidence limitations inside every affected record.
- Recalculate indexes, summaries, verification debt, and milestone status from
  the resulting records.

This avoids duplicated evidence systems and makes downstream requirements work
consume one coherent baseline.

## Evidence strata

Evidence must retain its origin and strength:

1. Owner physical observations describe the fitted machine at the stated date
   and machine state.
2. Manufacturer documentation establishes published properties of the
   identified component or product variant.
3. Retained legacy-image artifacts establish historical configuration or
   operation described by those artifacts; archive placement does not establish
   a forensic capture or untouched factory provenance.
4. The fresh ReBrewie capture establishes runtime behavior of the
   community-edited userspace on the legacy Brewie Linux platform. It is not an
   untouched factory-image claim.
5. Fresh and archived Olimex/Debian captures establish later experimental
   runtime behavior. They do not establish original factory configuration.
6. Owner-created overlays, reconstructed FEX text, traced schematics, and
   handwritten investigation notes remain inferred or experimental evidence
   unless independently verified.

## Status rules

- A runtime observation may be `verified` when the dated capture directly and
  unambiguously demonstrates the narrowly stated runtime fact.
- A physical wiring, electrical, or fitted-component claim does not become
  verified merely because software configuration names that connection.
- Multiple copies derived from one configuration lineage are corroboration, not
  independent physical verification.
- Conflicting observations remain visible and keep the fact disputed until the
  conflict is resolved or the claims are split by image, date, or scope.
- Assumptions remain labelled as assumptions. No confidence wording may silently
  replace a missing verification method.

## Integration scope

Review all existing records that concern:

- SOM identity and runtime memory;
- boot media, storage layout, and filesystems;
- display, backlight, and touch;
- SOM UARTs and observed MCU telemetry;
- networking hardware and runtime association;
- watchdog and RTC;
- legacy GPIO candidates;
- pressure-sensor, cable, valve, pump, and servo investigation notes.

Add new atomic records only for software-relevant facts not already expressible
by an existing record. Expected candidates include the historical kernel and
Buildroot identity, active SD boot/storage layout, PCF8563 RTC runtime presence,
modern watchdog observation, and dated USB Wi-Fi identity. The implementation
review may combine or omit candidates if an existing record already provides
the correct atomic scope.

## Derived-document updates

After the fact records are correct, update:

- `docs/evidence/hardware/fact-index.md`;
- the relevant topical summaries;
- `docs/evidence/hardware/verification-register.md`;
- `docs/evidence/hardware/baseline.md`;
- `docs/milestones/001-hardware-baseline.md`; and
- source/provenance documentation where necessary.

All counts and milestone statements must be derived from the final record set,
not copied from earlier summaries.

## Validation

Validation must check:

- every indexed fact has exactly one record and every record is indexed;
- status counts agree across generated or hand-maintained summaries;
- every new source citation names the exact local path, capture date, and hash;
- runtime, configuration, physical, and manufacturer evidence are not conflated;
- the ReBrewie image is never described as an untouched factory image;
- `brewie.dts` is identified as the owner's later experimental overlay;
- no excluded legacy implementation material becomes a requirement or design
  input;
- Markdown and repository consistency checks pass.

## Completion criterion

The pass is complete when the unified evidence registry accurately incorporates
the approved archive and runtime captures, verification debt is explicit, the
milestone status is evidence-based, and a reviewer can trace every changed
claim back to its exact evidence without consulting prohibited legacy logic.
