# Local historical evidence review

Date: 2026-08-12

## Purpose and boundary

This review records what the approved local `OldStuff` evidence can establish
about software-relevant hardware and historical Linux operation. It does not
select a new Linux image, UI toolkit, software architecture, brewing model,
state machine, protocol, or firmware design. Old implementations are not a
design input.

## Citation key

Every factual local-source statement below cites one or more key entries and a
specific line range (or, for `uImage`, the inspected binary-header method).
The key supplies the exact local path and SHA-256, so it is an unambiguous
source-ledger reference for each citation.

| Key | Exact local path | SHA-256 |
| --- | --- | --- |
| S1 | `/home/anders/Documents/OldStuff/oldImage/Gamle Brewie software/uboot partition/uImage` | `225637cdcd41e6d2df7a8a11f1294fb4f63e722abbdd2e377b9bf7248801af5a` |
| S2 | `/home/anders/Documents/OldStuff/oldImage/Gamle Brewie software/usr/share/brewie/dmesg.txt` | `8c0712889e9adde309107317217702e76b588cdb7acaeb997b405da2892f92d8` |
| S3 | `/home/anders/Documents/OldStuff/oldImage/gamle filer/script.fex.txt` | `6d076a06f6284f7211c8cc92593aefe957fdc577fec93380304f94cecf1c6667` |
| S4 | `/home/anders/Documents/OldStuff/oldImage/Gamle Brewie software/uboot partition/boot.scr` | `375397d0cce1618a43479d3cb9508653289868377e79a6ae00bf5c31a1b72a78` |
| S15 | `/home/anders/Documents/OldStuff/oldImage/Gamle Brewie software/uboot partition/script.bin` | `f134c3f515df2343112d7fe4b493350f2b90794214f5fa4a78eb8480b4ebfeec` |
| S16 | `/home/anders/Documents/OldStuff/oldImage/Gamle Brewie software/uboot partition/uEnv.txt` | `5c64ab9828e26e0525983192af9361c85aac3f79039280095ac2f1ff7744d3c7` |
| S5 | `/home/anders/Documents/OldStuff/ReBrewieLegacyRuntimeInfo.txt` | `e734165cae681b785ecfb373a73c38178fc44a3f216510115961c402bb242d78` |
| S6 | `/home/anders/Documents/OldStuff/NewOlimexDebianInfo.txt` | `1abc86106395e27b3cd6e1a80f13692a03cc77625f609cd53fd6730baeb86933` |
| S7 | `/home/anders/Documents/OldStuff/first dmesg.txt` | `69c037bbcced1863148f702fff04366e368223fc3ea7ac47c228eeb8252bfef8` |
| S8 | `/home/anders/Documents/OldStuff/brewie.dts` | `06d56de96b826e13d2c95070aea218021bf755ff00f3023ff81a6a5a2a345f7f` |
| S9 | `/home/anders/Documents/OldStuff/oldImage/hardware info.txt` | `a98389a6f67ee42e64575e909479f3275a6990b2231a93b2c3a2f0d4158d9f6c` |
| S10 | `/home/anders/Documents/OldStuff/oldImage/pressure sensor pullups.txt` | `fc10c54eb14e44856cd22d1a6f6ca8cd9cadcca33524ff05b6c10ee8e2b19c9f` |
| S11 | `/home/anders/Documents/OldStuff/oldImage/Servoer.txt` | `9bbae080e7fb805000668eade3c68a208de7fdf73139fb427443fa5ea6950878` |
| S12 | `/home/anders/Documents/OldStuff/oldImage/gpio-s.txt` | `a58862cb3b82c74940e8d0a57494f1ed821de007913b2a11d4f4e6fa2e470b84` |
| S13 | `/home/anders/Documents/OldStuff/reb20-develop/Documentation/archived/HardwareMap_A13SOM_V0.md` | `164eaa9f423440cf353bad794e50d90296acbd7e2307715782db85a4b7fd340b` |
| S14 | `/home/anders/Documents/OldStuff/reb20-develop/Documentation/archived/Brewie_A13_linux_setup_guide_working_updated20V0.5.md` | `17be955f7071d8c4432c3a9c0095d2e6b06ac33f3c59efccafdcd516354316b1` |

## Evidence strata

This is a source-classification policy, not an additional hardware claim.

1. **Legacy-image artifacts retained in the local archive** — S1's legacy U-Boot header (bytes
   0-63), S2's retained legacy-image log (lines 3-29 and 251-278), S4's U-Boot
   script header/payload (bytes 0-63 and offset 72), and S16's comment-only
   environment fragment (line 1) are archive artifacts.
   They establish historical configuration/runtime
   observations only and do not independently prove every physical net.
2. **Later direct runtime observations** — S5 (lines 1-11 and 108-138), S6
   (lines 1-11 and 31-36), and S7 (lines 1-31) are dated boot captures; they
   show what ran in their respective experiments, subject to capture accuracy
   and completeness.
3. **Reconstructions and tracing notes** — S3 is extracted FEX text (lines
   1-674), not a legacy-image artifact: its correspondence to S15 `script.bin`
   remains unverified. S15 is cited only by `file` reporting `data` and
   SHA-256 inspection; it has not been decoded, so this review makes no content
   claim about it. S8 is an experimental overlay
   (logical lines 1-96; the last line lacks a newline); S9--S11 are short handwritten investigation notes (lines
   1-35, 1-12, and 1-39 respectively), while S12 contains only `GPIO1:` on
   line 1; S13 and S14 are archived investigation
   notes (lines 1-109 and 1-1183 respectively). These sources retain their
   recorded uncertainty and are not authoritative schematics or factory
   assembly records.

The owner-requested/read-only status of S5 and S6 is owner-supplied provenance
recorded on 2026-08-12 in the [local evidence inventory and provenance
ledger](sources.md#local-evidence-inventory-and-provenance), table rows
`NewOlimexDebianInfo.txt` and `ReBrewieLegacyRuntimeInfo.txt`; it is not a fact
proved by either artifact. The same owner-attested row identifies S5 as a
community-edited ReBrewie image, while its displayed banner and OS-release
content are artifact facts at S5 lines 1-11 and 98-103. S8's comments call its
pin assignments assumptions (S8 lines 7-24).

## High-value findings

### Retained legacy-image platform

- The legacy U-Boot header identifies an uncompressed ARM `Linux-3.4.90-Brewie`
  kernel built 2018-01-12. Provenance: S1, bytes 0-63 inspected as a legacy
  U-Boot image header (`file` reports name, architecture, compression, and
  timestamp).
- The archived legacy log reports Linux `3.4.90-Brewie`, A13 revision
  B (`AW1625/sun5i`), 512 MB total RAM, and an SD/MMC root path. Provenance:
  S2 lines 3-29 and 251-262.
- That log reports a 14.8 GiB SDHC card, three partitions, and EXT3 mounts for
  the root and `/home/brewie` partitions. This is one historical storage setup,
  not a clean-slate requirement. Provenance: S2 lines 251-278.
- The archived boot script sets `console=ttyS0,115200`,
  `root=/dev/mmcblk0p2`, `rootwait`, quiet boot, `loglevel=0`, and `panic=10`.
  These are historical settings only. Provenance: S4, legacy U-Boot script
  header bytes 0-63 and plaintext `setenv bootargs` payload beginning at byte
  offset 72 (inspected with `grep -oba`); the payload is binary-container
  content rather than line-addressable text.
- The FEX configuration enables UARTs on PG3/PG4 and PG9/PG10; the log
  enumerates `ttyS0` and `ttyS1`. This remains configuration/runtime evidence,
  not physical endpoint proof. Provenance: S3 lines 123-135; S2 lines 114-120.
- The retained legacy-image log reports Goodix at I2C2 address `0x14`; the FEX text
  declares 480 by 272 LCD geometry and the same Goodix bus/address. Provenance:
  S2 lines 300-317; S3 lines 173-183 and 219-228.
- The FEX text enables USB Wi-Fi and disables SDIO Wi-Fi. The runtime log alone
  does not identify a fitted USB Wi-Fi model. Provenance: S3 lines 505-512;
  S2 line 127.

### Fresh ReBrewie legacy-platform boot

- The capture reports `Linux 3.4.90-Brewie #5` and Buildroot
  `2014.02-git-g3b4bd90-dirty`; its kernel line corroborates, but does not make
  the userspace identical to, the archived legacy lineage. Provenance: S5
  lines 98-102 and 108-118; S1 binary-header inspection above.
- It reports 512 MB at boot, 397,524 KiB `MemTotal`, a 15,558,144-block card,
  three partitions, and writable EXT3 root and `/home/brewie`. These are
  installed-card observations, not partitioning requirements. Provenance: S5
  lines 31, 72-78, 95, and 133-134.
- Its command line selects `/dev/mmcblk0p2` and `ttyS0` at 115200; the kernel
  reports the empty `loglevel=` field as malformed. Provenance: S5 lines 14 and
  108-129.
- It enumerates `ttyS0`/`ttyS1`, PCF8563 on I2C0 at `0x51`, and Goodix on I2C2
  at `0x14`; the Goodix backport creates an input device. Provenance: S5 lines
  222-225, 282-297, and 382-404.
- The RTC sets the initial clock and the capture contains a burst of repeated
  RTC reads near 61 seconds. This is historical behavior, not a design to
  inherit. Provenance: S5 lines 358-360 and 424-582.
- The NAND driver fails while the system boots from SD/MMC; this bounds the
  active storage path for that boot without proving board-level NAND absence.
  Provenance: S5 lines 228-230 and 356-365.
- `rtl8192cu` is present and `wlan0` becomes ready, but this capture has no USB
  vendor/product ID. Provenance: S5 lines 232 and 421-423.

### Later Olimex/Debian experiment

- The fresh capture reports Linux `5.10.180-olimex #140856`, `armv7l`, model
  `Olimex A13-SOM-512`, 521,216 KiB to Linux, 96 MiB CMA reserve, and a 59.5
  GiB card with one visible partition. Provenance: S6 lines 1-13, 36, and
  165-166.
- Its command line uses a PARTUUID root, `ttyS0` at 115200, `panic=10`, and
  log level 4. These are experimental-image observations, not clean-slate
  choices. Provenance: S6 lines 4 and 31.
- It records Realtek USB ID `0bda:8176`, `rtl8192cu`, and association. This is
  a dated runtime enumeration/use observation, not independent physical-fitment
  evidence, original-adapter proof, or a future requirement. Provenance: S6
  lines 215-218, 342-349, and 358-365.
- It enumerates `ttyS0` and `ttyS1` and enables the A13 watchdog with a
  16-second timeout. Enumeration does not establish an external `ttyS1`
  endpoint. Provenance: S6 lines 123-138.
- It identifies Goodix ID 911/version 1060 at I2C2 `0x14`, creates an input
  device, and falls back after the optional configuration load fails.
  Provenance: S6 lines 334-338 and 348.
- The archived 2026 notes record passive `/dev/ttyS1` observation, the Goodix
  path, and 480 by 272 framebuffer observations, but are reconstruction notes
  rather than independent physical verification. Provenance: S13 lines 11-15,
  48-55, 63-64, and 108-109; S14 lines 138-148 and 298-320.
- S8 assigns PB3, PG11, PC3, and UART3/PG pins in its experimental overlay,
  while explicitly labelling them assumptions; successful operation cannot
  isolate each pin claim. Provenance: S8 lines 7-24, 26-31, 48-87.
- The fresh log records missing regulator descriptions, missing
  `connector_type`, malformed/unsigned regulatory database, and late random
  initialisation. These are maintainability observations, not architecture
  decisions. Provenance: S6 lines 122, 137, 169-170, 221-228, 244-327, and
  339-341.
- `first dmesg.txt` is a distinct `#123712` build dated 2024-09-19, whereas S6
  is `#140856` dated 2026-01-28, despite a shared release string. They are not
  duplicate copies of one boot. Provenance: S7 lines 1-6; S6 lines 8-11.

### Physical investigation notes

- S10 records only these green-cable candidates for the boil-side small
  valve/pump/sensor PCB: pin 16 ground, pin 15 SDA, pin 9 5 V, and pin 6 SCL.
  It is an incomplete tracing note, not a connector pinout or physical-to-MCU
  mapping. Provenance: S10 lines 4-12.
- The pressure note reports a working green-cable observation and proposed
  pull-ups, but itself questions 3.3 V versus 5 V. It cannot choose voltage or
  resistor values. Provenance: S10 lines 1-12.
- The servo note records TowerPro MG996R markings and 50 Hz / 740 µs / 1780 µs
  pulse observations. Its undocumented setup and uncertainty leave these as
  characterization candidates only. Provenance: S11 lines 1-17.
- S9 records legacy aliases for PB15 button2, PB2 buzzer, PB4 hold-power, PB3
  backlight, PB10 LCD power, PB16 LED2, PE9 MCU reset, and PC7 power; it also
  records point-in-time PB3/PB10 sysfs values. It describes an old-kernel
  interface, not a required new-image API or independent physical trace.
  Provenance: S9 lines 1-8 and 15-25. S12 contributes no hardware proposition:
  its only content is `GPIO1:` at line 1.

## Observation-to-fact disposition ledger

This ledger prevents selected observations from silently becoming requirements
or untracked evidence. A direct, dated runtime capture can verify only its
narrowly stated runtime proposition. Physical wiring, electrical limits, and
fitted-part identity still require independent physical or authoritative
evidence. Same-lineage notes may corroborate a disputed record but do not
promote it.

| Selected observation | Fact or no-op disposition | Status effect and limitation |
| --- | --- | --- |
| S1 legacy U-Boot kernel header, bytes 0-63 | Partial same-lineage support already recorded with exact path/hash/header method in [HW-101](facts/HW-101.md), not corroboration of its complete atomic claim. | Matches only the kernel-name/lineage component; archive placement and a header string do not prove build `#5`, the fresh-boot event, or fitted hardware. |
| S2 retained log line 3: kernel string | Partial same-lineage support already recorded with exact path/hash/range in [HW-101](facts/HW-101.md), not corroboration of its complete atomic claim. | Matches the kernel string, not the separately dated fresh-boot event or physical hardware. |
| S2 retained log lines 250-278: SDHC, partition names, EXT3 root/p3 activity | Partial historical context for [HW-103](facts/HW-103.md), not corroboration of its complete atomic claim. | S2 omits HW-103's exact partition sizes and `/home/brewie` mount point; no status or canonical-source change. |
| S2 lines 114-120 and 286-317; S3 lines 123-135, 173-186, and 199-235: legacy UART/touch/display runtime or configuration | Context/no-op for [HW-004](facts/HW-004.md), [HW-006](facts/HW-006.md), [HW-007](facts/HW-007.md), [HW-008](facts/HW-008.md), and [HW-108](facts/HW-108.md). | Does not prove a physical SOM-MCU link, current DRM RGB565 observation, fresh-boot ID 911/version 1060, or the two-fresh-capture proposition; S3-to-S15 correspondence is unverified. |
| S3 lines 505-512: USB/SDIO Wi-Fi configuration | No new fact; contextual contrast only with [HW-107](facts/HW-107.md). | Configuration does not identify the device runtime-enumerated in the later dated capture. |
| S4 U-Boot header bytes 0-63 and boot-argument payload at offset 72 | No new fact; retained as review-level historical configuration. | Does not select a clean-slate boot path, filesystem, console, or recovery policy. |
| S15 undecoded `script.bin`, SHA-256 plus `file` inspection | No-op. | `file` reports only `data`; no decode or content proposition exists. |
| S16 `uEnv.txt` line 1 | No-op. | The single comment establishes no hardware or runtime proposition. |
| S5 fresh ReBrewie runtime | Direct dated evidence already recorded with exact path/hash/ranges: lines 10-11/108 in [HW-101](facts/HW-101.md), 96-102 in [HW-102](facts/HW-102.md), 70-95/355-381 in [HW-103](facts/HW-103.md), and 282-297/424-582 in [HW-104](facts/HW-104.md). Lines 221-225 are one required direct-evidence component of [HW-108](facts/HW-108.md), jointly sufficient with S6 lines 123-126; neither capture alone establishes HW-108's two-capture proposition. | Verifies only those scoped runtime observations; not factory-userspace, fitted-part, wiring, or electrical evidence. |
| S5 lines 382-404: legacy Goodix family/bus output | Different-boot context/no-op for [HW-007](facts/HW-007.md) and [HW-008](facts/HW-008.md), not corroboration of their fresh Olimex/Debian dated claims. | Reports a different IC-version string and cannot verify the 2026-08-12 Olimex/Debian event. |
| S6 fresh Olimex/Debian runtime | Direct dated evidence already recorded with exact path/hash/ranges: lines 334-348 in [HW-007](facts/HW-007.md)/[HW-008](facts/HW-008.md), 1-11/36 in [HW-105](facts/HW-105.md), 138 in [HW-106](facts/HW-106.md), and 214-219/342-349/358-365 in [HW-107](facts/HW-107.md). Lines 123-126 are one required direct-evidence component of [HW-108](facts/HW-108.md), jointly sufficient with S5 lines 221-225; neither capture alone establishes HW-108's two-capture proposition. | Verifies only the scoped runtime observations; physical identities and future choices remain separate. |
| S7 lines 1-31: older Olimex/Debian log | No new fact; retained to distinguish a different build from S6. | Same release string does not make the boots identical or independently verify hardware. |
| S8 logical lines 7-24, 26-31, and 41-87: experimental overlay | Assumption/configuration context only for [HW-004](facts/HW-004.md), [HW-008](facts/HW-008.md), and [HW-009](facts/HW-009.md). | Does not prove a physical UART link, the later fresh-boot enumeration, or a legacy PB3 mapping; no canonical-source or status change. |
| S9 lines 1-8 and 15-25: legacy GPIO aliases and PB3/PB10 values | Same-lineage corroboration recorded with exact path/hash/ranges in [HW-005](facts/HW-005.md), [HW-009](facts/HW-009.md), [HW-010](facts/HW-010.md), and [HW-075](facts/HW-075.md) through [HW-079](facts/HW-079.md). | All remain disputed; the note does not identify board revision, current routing, voltage, or electrical behavior. |
| S10 lines 1-12: green-cable and pressure note | Partial context recorded in [HW-024](facts/HW-024.md) and [HW-089](facts/HW-089.md), not corroboration of either complete MCU-pin claim. | It does not name PD0/PD1, its test setup is absent, and it conflicts internally on 3.3 V versus 5 V and pull-up values; no status promotion. |
| S11 lines 1-17: servo marking and pulse note | No new fact. | Machine endpoint, test setup, load, uncertainty, and revision are absent; the historical values must not become actuator requirements. |
| S12 line 1: `GPIO1:` fragment | No-op. | No mapping, endpoint, state, or other factual proposition is present. |
| S13 lines 10-15, 28-34, 48-55, 63-64, and 108-109: archived UART/touch map | Investigation context only for [HW-004](facts/HW-004.md), [HW-007](facts/HW-007.md), [HW-008](facts/HW-008.md), and [HW-017](facts/HW-017.md); no [HW-006](facts/HW-006.md) proposition is present. | It does not physically trace the UART, report 480x272/RGB565, show bidirectional traffic, or report Goodix ID 911/version 1060; its touch family/bus text is not the later dated capture. |
| S14 lines 134-150, 298-304, and 308-322: copied overlay assumptions and observed touch/framebuffer values | Configuration/observation context only for [HW-004](facts/HW-004.md), [HW-006](facts/HW-006.md), [HW-007](facts/HW-007.md), and [HW-008](facts/HW-008.md); no support for [HW-017](facts/HW-017.md). | It does not trace a physical UART, establish DRM RGB565, report Goodix ID 911/version 1060, independently establish the fresh I2C event, or demonstrate bidirectional traffic. |

## What this evidence changes

The cited legacy/runtime artifacts bound historical boot and kernel (S1
bytes 0-63; S2 lines 3-29; S5 lines 108-134; S6 lines 1-36), display/touch
(S2 lines 300-317; S3 lines 173-228; S5 lines 382-404; S6 lines 334-348),
storage (S2 lines 251-278; S5 lines 72-95 and 356-381; S6 lines 163-166), and
networking observations (S3 lines 505-512; S5 lines 232 and 421-423; S6 lines
215-218, 342-349, and 358-365). They do not distinguish physical wiring from
configuration, nor justify inheriting the legacy image architecture. Direct
dated runtime evidence may verify its own narrowly worded runtime proposition;
independent physical or authoritative evidence is still required before a
physical wiring, electrical, or fitted-component proposition becomes verified.

## Remaining high-value checks

- Correlate S3 with S15 `script.bin` before treating the FEX text as an exact
  decode of that binary. S15's current evidence is only `file` output (`data`)
  and SHA-256 inspection; no decoded content has been used.
- Compare historical FEX, the experimental overlay, and traced carrier evidence
  as separate sources.
- Identify fitted display and Wi-Fi hardware if their identities would
  constrain later work.
- Resolve the pressure-sensor voltage and pull-ups from physical or
  revision-matched electrical evidence before any powered test.
- Keep actuator tests gated; the current-machine safety restrictions remain in
  the milestone and verification register, not in these historical artifacts.
