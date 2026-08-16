# Platform-enablement evidence triage

## Purpose and boundary

This registry classifies disputed hardware evidence by its effect on clean-slate
Linux platform enablement. It schedules verification and records safe defaults;
it does not select or implement a Linux image, firmware, protocol, UI, brewing
logic, or hardware-control design. Historical implementation choices remain
observations and do not become requirements or design inputs.

The atomic records in `facts/` remain canonical for claims, evidence,
confidence, and verification status. A row in this registry does not promote or
otherwise change a fact's status.

## Dispositions

- `platform blocker`: verification is required before requirements work or
  first powered bring-up because isolation cannot permit safe progress.
- `platform constraint`: requirements work may proceed, but the unresolved
  interface or capability must remain disabled, isolated, preserved, or
  untouched.
- `integration dependency`: verification is required for a named later
  integration, not for minimal platform enablement.
- `brewing-device dependency`: verification is deferred to hardware-control or
  brewing-device work.
- `non-blocking reference`: useful evidence that controls no currently planned
  decision.
- `candidate removal`: proposed removal from required scope, pending explicit
  owner approval with a reason and date.

## Deadlines

- `before requirements`: resolve before Linux-image requirements are activated.
- `before first powered bring-up`: resolve before the first powered Linux test.
- `before named integration`: resolve before the named later integration.
- `deferred`: no current activation deadline; retain the recorded safe default.

## Material disputed-fact dispositions

| ID | Claim | Disposition | Decision or later milestone | Wrong-claim consequence | Safe default | Deadline | Why isolation cannot permit progress | Cheapest reliable check | Evidence/confidence/status | Owner approval |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Platform blockers

None recorded yet.

## First-bring-up constraints

None recorded yet.

## Deferred work

None recorded yet.

## Candidate removals

None recorded yet.

## Owner-removed non-material disputed facts

None recorded yet.

## Gate decision

Pending complete classification and validation.
