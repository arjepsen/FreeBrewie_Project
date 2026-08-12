# Local historical evidence review

Date: 2026-08-12

## Purpose and boundary

This review records what the approved local `OldStuff` evidence can establish
about software-relevant hardware and historical Linux operation. It does not
select a new Linux image, UI toolkit, software architecture, brewing model,
state machine, protocol, or firmware design. Old implementations are not a
design input.

## Evidence strata

The folder contains three materially different kinds of evidence:

1. **Captured original-image artifacts** — the legacy kernel image, boot files,
   root-filesystem fragments, and original-image `dmesg`. These are strong
   evidence of what one historical installation was configured to do, but do
   not independently prove every physical net.
2. **Later direct runtime observations** — two Linux 5.10 boot logs, including
   the fresh four-command capture `NewOlimexDebianInfo.txt`, and 2026 bring-up
   notes. These show what worked on the inspected machine during that later
   experiment, subject to the accuracy and completeness of each capture.
3. **Reconstructions and tracing notes** — overlays, FEX text, cable maps, and
   handwritten investigation records. These are useful candidate evidence and
   corroboration, but retain their recorded uncertainty and are not promoted to
   authoritative schematics or factory assembly records.

## High-value findings

### Original Linux installation

- The captured `uImage` header identifies an uncompressed ARM kernel image as
  `Linux-3.4.90-Brewie`, built 2018-01-12.
- The original-image runtime log identifies Linux `3.4.90-Brewie`, an Allwinner
  A13 revision B (`AW1625/sun5i`), 512 MB total RAM, and a root filesystem on
  `/dev/mmcblk0p2`.
- That runtime saw a 14.8 GiB SDHC card with three partitions; partitions 2 and
  3 were mounted as EXT3. This establishes one historical boot/storage setup,
  not the required capacity or partitioning of the clean-slate image.
- The captured boot script sets `console=ttyS0,115200`,
  `root=/dev/mmcblk0p2`, `rootwait`, quiet boot, and panic recovery. These are
  historical settings only.
- The legacy runtime exposed `ttyS0` at `0x01c28400` and `ttyS1` at
  `0x01c28c00`; its configuration enabled UARTs on PG3/PG4 and PG9/PG10.
  Physical endpoint identity still needs carrier/net corroboration.
- The original-image log records a Goodix touchscreen at I2C bus 2, address
  `0x14`, and a 480×272 LCD configuration appears in the captured FEX text.
- The captured FEX text declares USB Wi-Fi enabled and SDIO Wi-Fi disabled. The
  runtime log alone does not identify the fitted USB Wi-Fi model.

### Fresh ReBrewie legacy-platform boot

The owner booted the community-edited ReBrewie image with heaters and pumps
still disconnected and captured the requested read-only commands in
`ReBrewieLegacyRuntimeInfo.txt`. The login banner identifies ReBrewie
`v4.1.0-rc0`; the owner states that its application/userspace was edited by
other users while retaining the older Linux image. It must not be described as
an untouched factory image.

- `uname` and `dmesg` identify the same `Linux 3.4.90-Brewie #5` kernel build
  and timestamp as the archived original-image kernel and log. This strongly
  corroborates that the archive represents the same legacy platform lineage,
  while not proving that every userspace file is original.
- `/etc/os-release` identifies Buildroot
  `2014.02-git-g3b4bd90-dirty`, with the display name `Brewie 2014.02-git`.
- The running system reports an ARMv7 Cortex-A8-class CPU, Allwinner A13
  revision B, 512 MB physical RAM at boot, and 397,524 KiB currently exposed as
  `MemTotal` after legacy reservations.
- The installed SD card exposes 15,558,144 one-kilobyte blocks and three
  partitions: a 16 MiB first partition, approximately 383 MiB root partition,
  and approximately 7.0 GiB third partition. Root and `/home/brewie` are
  writable EXT3 filesystems. These are observations of this installed card,
  not a clean-slate partitioning requirement.
- The legacy command line boots from `/dev/mmcblk0p2`, uses `ttyS0` at 115200,
  waits for root, requests quiet boot, and contains an empty `loglevel=` value
  that the kernel reports as malformed.
- No model string was returned by `/proc/device-tree/model`. Combined with the
  legacy sunxi configuration behavior, this means the absence must not be
  mistaken for an unidentified physical SOM or treated like the modern DT
  model property.
- The boot enumerates `ttyS0` at `0x01c28400` and `ttyS1` at `0x01c28c00`, a
  PCF8563 RTC on I2C0 at `0x51`, and a Goodix touchscreen on I2C2 at `0x14`.
  The Goodix backport creates the capacitive touchscreen input successfully.
- The RTC supplies the initial system clock, but the log contains an unusually
  large burst of repeated RTC reads around 61 seconds. This is a historical
  behavior worth avoiding or diagnosing later, not a design to inherit.
- The NAND driver fails to find a NAND physical architecture, while the system
  boots successfully from SD/MMC. This supports SD/MMC as the active storage
  path for this boot but does not prove that no NAND footprint exists anywhere
  in the hardware.
- The `rtl8192cu` driver is present and `wlan0` becomes ready, but this capture
  does not expose the adapter's USB vendor/product ID. The later Debian capture
  identifies its then-fitted adapter separately.

### Later clean-image experiment

- The fresh capture identifies the running system as Linux
  `5.10.180-olimex #140856`, built 2026-01-28, on `armv7l`; both
  `/proc/device-tree/model` and `dmesg` report `Olimex A13-SOM-512`.
- It reports 521,216 KiB total physical memory to Linux, with 96 MiB reserved
  for CMA, and a 59.5 GiB SDXC card containing a single visible partition.
- The kernel command line selects the root filesystem by PARTUUID, waits for
  it, uses `ttyS0` at 115200 as console, sets `panic=10`, and uses log level 4.
  These are observations of this experimental image, not clean-slate choices.
- It records a Realtek USB adapter with USB ID `0bda:8176`, advertised as an
  802.11n WLAN adapter; the `rtl8192cu` driver associates successfully. This is
  a dated fitted-device observation, not proof of the original factory adapter
  or a requirement for the new design.
- It enumerates `ttyS0` at `0x1c28400` and `ttyS1` at `0x1c28c00`, and enables
  the A13 watchdog with a 16-second timeout. Enumeration does not itself prove
  which external endpoint is wired to `ttyS1`.
- It identifies the touch controller as Goodix ID 911, version 1060, on I2C2
  at `0x14`, and creates a capacitive-touch input device. Its optional
  `goodix_911_cfg.bin` load fails and the driver falls back.
- The 2026 notes record working `/dev/ttyS1` passive MCU telemetry at 115200
  8N1, a working Goodix GT911 path at I2C2 address `0x14`, and a working
  480×272, 32-bpp framebuffer. Together they materially corroborate the
  corresponding historical configuration candidates.
- The owner clarified that `brewie.dts` was probably made specifically for this
  experimental image. That later overlay assigns PB3 to backlight enable, PG11
  to touchscreen IRQ,
  PC3 to touchscreen reset, and UART3/PG pins to the MCU link, but explicitly
  labels these assignments as assumptions. Successful system-level operation
  supports the configuration as a set; it does not isolate every individual
  pin claim.
- The fresh log records missing regulator descriptions for several pin banks,
  backlight, panel, and Goodix supplies; a missing panel `connector_type`; a
  malformed or unsigned wireless regulatory database; and a late initialisation
  of the kernel random-number generator. These are concrete maintainability and
  integration observations to investigate later, not architecture decisions.
- `first dmesg.txt` is a different boot/build (`#123712`, built 2024-09-19)
  from the fresh capture (`#140856`, built 2026-01-28), despite both identifying
  their kernel release as 5.10.180-olimex. They must not be treated as duplicate
  copies of one boot.

### Physical investigation notes

- The cable/PCB notes contain connector-position candidates for pumps, valves,
  buttons, temperature, mass/pressure I2C, power rails, grounds, and an LMV324
  stage. They are incomplete handwritten tracing records and should corroborate
  the newer KiCad tracing rather than override it.
- The pressure-sensor note records a working observation through the long green
  cable and a need for SDA/SCL pull-ups, but is uncertain whether the bus was
  intended for 3.3 V or 5 V. It must not be used to choose voltage or resistor
  values without verification.
- The servo note identifies TowerPro MG996R markings and records measured
  50 Hz command pulses for open and closed positions. Test setup, load,
  uncertainty, endpoint convention, and machine revision are not adequately
  documented, so these values are characterization candidates only.
- The legacy GPIO-node note corroborates PB3 backlight, PB10 LCD power enable,
  PE9 MCU reset, and several button/power/LED candidates. It describes the old
  kernel interface, not a required API for the new image.

## What this evidence changes

The local archive fills the previous absence of boot-media, historical kernel,
display/touch, and networking observations. It does not eliminate the need to
distinguish physical wiring from configuration, nor does it justify inheriting
the legacy image architecture. Existing disputed fact records should gain these
sources as corroboration; a claim should become verified only where independent
evidence verifies the same narrowly worded proposition.

## Remaining high-value checks

- Correlate the original `script.bin` with `script.fex.txt` before treating the
  text as an exact decode of that binary.
- Compare the original FEX UART/GPIO assignments, later mainline overlay, and
  traced MCU/carrier evidence as separate sources.
- Identify the exact fitted display and Wi-Fi hardware if those identities
  would constrain the image.
- Resolve pressure-sensor bus voltage and pull-ups from physical or
  revision-matched electrical evidence before any powered test.
- Keep all actuator tests gated; the current machine remains upside down,
  unplugged, and has heaters and pumps disconnected.
