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
2. **Later direct runtime observations** — the Linux 5.10 `dmesg` and 2026
   bring-up notes. These show what worked on the inspected machine during that
   later experiment, subject to the accuracy and completeness of the capture.
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

### Later clean-image experiment

- The later runtime capture identifies an Olimex A13-SOM-512 running Linux
  5.10.180 with approximately 512 MB physical RAM and an SD card as storage.
- It records a Realtek USB adapter with USB ID `0bda:8176`, advertised as an
  802.11n WLAN adapter. This is a dated fitted-device observation, not proof of
  the original factory adapter or a requirement for the new design.
- The 2026 notes record working `/dev/ttyS1` passive MCU telemetry at 115200
  8N1, a working Goodix GT911 path at I2C2 address `0x14`, and a working
  480×272, 32-bpp framebuffer. Together they materially corroborate the
  corresponding historical configuration candidates.
- The later overlay assigns PB3 to backlight enable, PG11 to touchscreen IRQ,
  PC3 to touchscreen reset, and UART3/PG pins to the MCU link, but explicitly
  labels these assignments as assumptions. Successful system-level operation
  supports the configuration as a set; it does not isolate every individual
  pin claim.

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
