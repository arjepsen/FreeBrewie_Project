# Hardware verification register

## Disputed facts

No [indexed facts](fact-index.md) currently carry disputed status.

## Provisional assumptions

No proposed candidate in the [fact index](fact-index.md) has been accepted for provisional use.

## Verification debt

- Obtain authoritative SOM and carrier product identifiers and revision markings; the current candidate is [HW-001](facts/HW-001.md).
- Obtain authoritative SOM RAM, boot-media, persistent-storage, and networking-hardware evidence within the [approved source boundary](sources.md#inspection-authority), or record an owner-approved boundary expansion before inspection.
- Resolve the exact MCU and its memory table from manufacturer evidence after checking [HW-002](facts/HW-002.md) and [HW-003](facts/HW-003.md).
- Resolve carrier-level UART and reset connectivity for [HW-004](facts/HW-004.md) and [HW-005](facts/HW-005.md).
- Preserve and identify the boot image and configuration represented by [HW-006](facts/HW-006.md).
- Identify display and touch parts and carrier wiring for [HW-007](facts/HW-007.md), [HW-008](facts/HW-008.md), and [HW-009](facts/HW-009.md).
- Produce a native KiCad 9 netlist and physical trace for the power-control candidates in [HW-010](facts/HW-010.md).

## Blocked downstream decisions

- Linux image, kernel, boot-media, and device-tree selection remain blocked on [HW-001](facts/HW-001.md), [HW-007](facts/HW-007.md), [HW-008](facts/HW-008.md), [HW-009](facts/HW-009.md), and the unfilled SOM storage/networking evidence request linked under verification debt.
- MCU build targeting, memory budgets, recovery, and irreversible configuration changes remain blocked on [HW-002](facts/HW-002.md), [HW-003](facts/HW-003.md), and [HW-006](facts/HW-006.md).
- Control-system integration decisions involving serial binding, reset, or power control remain blocked on [HW-004](facts/HW-004.md), [HW-005](facts/HW-005.md), and [HW-010](facts/HW-010.md).

## Owner-approved removals

No owner-approved removals are recorded in the [fact index](fact-index.md).
