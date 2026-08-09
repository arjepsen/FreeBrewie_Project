# Hardware verification register

## Disputed facts

No [indexed facts](fact-index.md) currently carry disputed status.

## Provisional assumptions

No proposed candidate in the [fact index](fact-index.md) has been accepted for provisional use.

## Verification debt

- Resolve the exact SOM identifier and revision and the carrier identity and revision; the current SOM candidate is [HW-001](facts/HW-001.md), and missing evidence is covered by the [pending boundary-expansion request](sources.md#pending-task-3-compute-platform-evidence-request).
- Obtain authoritative SOM RAM, boot-hardware, boot-media, persistent-storage, and networking-hardware evidence only after approval of the [pending boundary-expansion request](sources.md#pending-task-3-compute-platform-evidence-request).
- Resolve the exact MCU and its memory table from manufacturer evidence after checking [HW-002](facts/HW-002.md) and [HW-003](facts/HW-003.md).
- Resolve carrier-level UART and reset connectivity for [HW-004](facts/HW-004.md) and [HW-005](facts/HW-005.md).
- Identify the display part and wiring for [HW-006](facts/HW-006.md).
- Resolve touch identity and wiring for [HW-007](facts/HW-007.md) and [HW-008](facts/HW-008.md).
- Resolve the separate LCD control candidates in [HW-009](facts/HW-009.md) and [HW-010](facts/HW-010.md).
- Produce a native KiCad 9 netlist and separate physical traces for [HW-011](facts/HW-011.md), [HW-012](facts/HW-012.md), [HW-013](facts/HW-013.md), and [HW-014](facts/HW-014.md).

### Required-category coverage

| Required category | Indexed candidate or bounded outcome |
| --- | --- |
| SOM identity and revision | Candidate identity [HW-001](facts/HW-001.md); exact identity and revision pending the [boundary-expansion request](sources.md#pending-task-3-compute-platform-evidence-request) |
| Carrier-board identity and revision | No approved-source candidate; pending the [boundary-expansion request](sources.md#pending-task-3-compute-platform-evidence-request) |
| MCU identity and revision | Candidate identity [HW-002](facts/HW-002.md); board revision pending the [boundary-expansion request](sources.md#pending-task-3-compute-platform-evidence-request) |
| Memory and storage | MCU embedded-memory candidate [HW-003](facts/HW-003.md); SOM RAM and storage pending the [boundary-expansion request](sources.md#pending-task-3-compute-platform-evidence-request) |
| Boot hardware | No approved-source hardware candidate; pending the [boundary-expansion request](sources.md#pending-task-3-compute-platform-evidence-request) |
| Display and input | [HW-006](facts/HW-006.md), [HW-007](facts/HW-007.md), [HW-008](facts/HW-008.md), [HW-009](facts/HW-009.md), and [HW-010](facts/HW-010.md) |
| Networking | No approved-source hardware candidate; pending the [boundary-expansion request](sources.md#pending-task-3-compute-platform-evidence-request) |
| Compute-side buses, reset, enable, interrupt, watchdog, and power control | UART and reset candidates [HW-004](facts/HW-004.md) and [HW-005](facts/HW-005.md); separate enable/control candidates [HW-009](facts/HW-009.md) through [HW-014](facts/HW-014.md); no approved-source interrupt or watchdog candidate, pending the [boundary-expansion request](sources.md#pending-task-3-compute-platform-evidence-request) |

## Blocked downstream decisions

- Linux image, kernel, boot-media, storage, networking, and device-tree selection remain blocked on [HW-001](facts/HW-001.md), [HW-006](facts/HW-006.md), [HW-007](facts/HW-007.md), [HW-008](facts/HW-008.md), [HW-009](facts/HW-009.md), [HW-010](facts/HW-010.md), and the [pending boundary-expansion request](sources.md#pending-task-3-compute-platform-evidence-request).
- MCU build targeting and memory budgets remain blocked on [HW-002](facts/HW-002.md) and [HW-003](facts/HW-003.md); boot-hardware questions remain blocked on the [pending boundary-expansion request](sources.md#pending-task-3-compute-platform-evidence-request).
- Control-system integration decisions involving UART, reset, display enables, or power-control candidates remain blocked on [HW-004](facts/HW-004.md), [HW-005](facts/HW-005.md), and [HW-009](facts/HW-009.md) through [HW-014](facts/HW-014.md).

## Owner-approved removals

No owner-approved removals are recorded in the [fact index](fact-index.md).
