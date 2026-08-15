# SOM and carrier hardware summary

This is a view over the indexed hardware fact records. It is not independent evidence, and disputed candidates below are not baseline conclusions.

## Verified identity and capacity

| Area | Record-backed statement | Status |
| --- | --- | --- |
| SOM identity | The fitted module marking is `Olimex A13-SOM (512)`, PCB revision `G`; the record verifies the visible marking only. [HW-001](facts/HW-001.md) | verified |
| Carrier identity | The fitted carrier marking is `Brewie ARM board`, revision `V1p2`; schematic correspondence, population, connectivity, and electrical behavior are outside the verified claim. [HW-094](facts/HW-094.md) | verified |
| Installed memory | The marked SOM variant has a manufacturer-defined nominal capacity of 512 MB DDR3. Exact DDR3 part, timings, runtime availability, and health are not established. [HW-095](facts/HW-095.md) | verified |

## Compute, storage, and boot hardware

| Area | Record-backed boundary | Status |
| --- | --- | --- |
| CPU architecture | The modern experimental boot reported `armv7l`, kernel `5.10.180-olimex #140856`, model `Olimex A13-SOM-512`, and 521,216 KiB to Linux. These are dated runtime values, not fitted-part identity or a future platform selection. [HW-105](facts/HW-105.md) | verified runtime observation; physical details unresolved |
| Persistent storage | The legacy boot used `mmcblk0` partitions p1/p2/p3 with the recorded sizes, EXT3 root on p2, and EXT3 `/home/brewie` on p3. Physical medium identity, total capacity, health, endurance, and any future layout remain unresolved. [HW-103](facts/HW-103.md) | verified runtime observation; physical storage unresolved |
| Boot path hardware | The legacy capture records `Linux 3.4.90-Brewie #5` and Buildroot `2014.02-git-g3b4bd90-dirty`, but neither those observations nor the fitted-SOM marking establish boot media or carrier wiring. [HW-101](facts/HW-101.md) [HW-102](facts/HW-102.md) | runtime lineage verified; hardware path unresolved |

## Legacy platform observations

| Area | Dated observation | Boundary |
| --- | --- | --- |
| Kernel lineage | The fresh 2026-08-12 ReBrewie boot reported `Linux 3.4.90-Brewie #5`. [HW-101](facts/HW-101.md) | Historical compatibility evidence only; it does not select a future kernel. |
| Userspace | The same community-edited ReBrewie boot identified Buildroot `2014.02-git-g3b4bd90-dirty`. [HW-102](facts/HW-102.md) | Not factory-image proof and not a clean-slate userspace requirement. |
| Active storage layout | The same boot used the recorded `mmcblk0` partition sizes and EXT3 mounts. [HW-103](facts/HW-103.md) | Does not identify the physical medium or select partition sizes, EXT3, mount points, or boot layout. |
| RTC | Linux detected PCF8563 on I2C adapter 0 at `0x51` and registered `rtc0`. [HW-104](facts/HW-104.md) | Physical part marking, wiring, battery, electrical limits, accuracy, and future RTC policy remain unresolved. |

## Modern experimental platform observations

| Area | Dated observation | Boundary |
| --- | --- | --- |
| Runtime platform | The fresh 2026-08-12 Olimex/Debian experiment reported kernel `5.10.180-olimex #140856`, `armv7l`, model `Olimex A13-SOM-512`, and 521,216 KiB to Linux. [HW-105](facts/HW-105.md) | Does not identify a RAM package or select a future kernel, memory reservation, or platform configuration. |
| Watchdog | Linux enabled the A13 watchdog at `0x1c20c90` with a 16-second timeout and `nowayout=0`. [HW-106](facts/HW-106.md) | This old captured behavior does not establish application use, reset routing, or a future timeout/`nowayout` policy. |
| USB WLAN | A Realtek `0bda:8176` USB device enumerated, loaded `rtl8192cu`, and associated during the dated runtime capture. [HW-107](facts/HW-107.md) | It does not independently establish physical fitment, permanent networking hardware, placement, performance, or a future adapter/driver requirement. |

## Display and input

| Endpoint | Candidate mapping or observation | Relevant limits | Status |
| --- | --- | --- | --- |
| Attached display | A 480 by 272 RGB565 Linux scanout was reported, but panel identity, physical bus, electrical interface, and timing are not established. [HW-006](facts/HW-006.md) | The reported mode is not verified hardware capability. | disputed |
| LCD backlight | A13 PB3 is the legacy backlight-control candidate. [HW-009](facts/HW-009.md) | Carrier routing, voltage, polarity, and current-image control are unknown. | disputed |
| LCD power enable | A13 PB10 is the legacy power-enable candidate. [HW-010](facts/HW-010.md) | Carrier routing, voltage, polarity, and current-image control are unknown. | disputed |
| Current backlight PWM | `pwm-0` is identified as a backlight PWM, with a reported 50 µs period and inverse polarity. [HW-082](facts/HW-082.md) [HW-092](facts/HW-092.md) [HW-093](facts/HW-093.md) | Consumer assignment, electrical pin, voltage, measurement basis, duty cycle, and exact revision are unresolved. | disputed |
| Touch identity | During the fresh 2026-08-12 Olimex/Debian boot, Linux identified Goodix ID 911, version 1060. [HW-007](facts/HW-007.md) | Exact fitted part, panel revision, supply, interrupt line, and reset line are unknown. | verified dated runtime observation; physical identity unresolved |
| Touch bus | During that boot, Linux enumerated the device on I2C bus 2 at address `0x14`. [HW-008](facts/HW-008.md) | Linux numbering does not verify pull-ups, voltage, carrier routing, interrupt, or reset wiring. | verified dated runtime observation; physical interface unresolved |

## Networking and exposed interfaces

| Area | Record-backed boundary | Status |
| --- | --- | --- |
| Networking | A fresh modern experiment enumerated and used a Realtek `0bda:8176` USB WLAN device. Physical fitment, carrier networking hardware, permanent installation, connector/placement, performance, and future selection remain unresolved. [HW-107](facts/HW-107.md) | verified dated runtime observation; physical/permanent hardware unresolved |
| SOM-MCU serial | Both fresh captures enumerate `ttyS0` and `ttyS1` at matching MMIO addresses. That corroborates Linux serial-controller enumeration, not physical MCU connectivity or telemetry; the physical link and `/dev/ttyS1` traffic claims remain separate. [HW-108](facts/HW-108.md) [HW-004](facts/HW-004.md) [HW-017](facts/HW-017.md) | enumeration verified; physical binding disputed |
| Touch I2C | Linux enumerated the Goodix device on I2C bus 2 at address `0x14` during the dated modern boot; its physical and electrical realization is not established. [HW-008](facts/HW-008.md) | verified runtime endpoint; physical interface unresolved |
| RTC | The dated legacy boot detected PCF8563 on I2C0 at `0x51` and registered `rtc0`; exact fitted identity, wiring, supply, battery, and limits are not established. [HW-104](facts/HW-104.md) | verified runtime detection; physical interface unresolved |
| Audio pins | SOM `HPOUTL` and `HPCOM` are candidate connections to a carrier amplifier input path; exact amplifier pins, coupling, amplitude, bias, impedance, bandwidth, and connector positions are unknown. [HW-069](facts/HW-069.md) | disputed |

## Reset, power, GPIO, PWM, and watchdog

| Function | Candidate or bounded state | Status |
| --- | --- | --- |
| MCU reset | A13 PE9 is the candidate SOM-controlled MCU reset, while a high-then-low drive of Linux `gpio137` was separately reported to reset the MCU. The physical trace, pulse parameters, thresholds, and polarity remain unresolved. [HW-005](facts/HW-005.md) [HW-018](facts/HW-018.md) | disputed |
| Legacy button input | A13 PB15 is the legacy drain/second-button candidate. Physical identity, connector, voltage, pull-up, and polarity are unknown. [HW-075](facts/HW-075.md) | disputed |
| Legacy power outputs | A13 PB4 is the legacy hold-power candidate and A13 PC7 is an ambiguously power-related candidate. Destinations, directions where unstated, voltage, polarity, and power effects are unknown. [HW-076](facts/HW-076.md) [HW-078](facts/HW-078.md) | disputed |
| Legacy indicator output | A13 PB16 is the legacy second-LED candidate; LED identity and drive constraints are unknown. [HW-077](facts/HW-077.md) | disputed |
| PB2 mux conflict | PB2 is reported assigned to `1c20e00.pwm`, is inferred as Linux `gpio34`, and also appears as a legacy buzzer alias. These records do not establish current carrier routing or a safe consumer. [HW-072](facts/HW-072.md) [HW-083](facts/HW-083.md) [HW-079](facts/HW-079.md) | disputed |
| Legacy alias state | The current image was reported not to create the original `/dev/brewie-*` GPIO aliases; absence of aliases does not prove physical disconnection. [HW-080](facts/HW-080.md) | disputed |
| Carrier audio population | The audio-amplifier IC position is physically absent/unpopulated on the fitted carrier. This does not establish the rest of the sounder circuit or its behavior. [HW-071](facts/HW-071.md) | verified |
| Watchdog | The dated modern experiment enabled the A13 watchdog at `0x1c20c90` with a 16-second timeout and `nowayout=0`. Application use, physical reset effects, and future policy remain unresolved. [HW-106](facts/HW-106.md) | verified runtime observation; behavior and policy unresolved |

Historical partition sizes, EXT3 use, kernel versions, Buildroot, the old captured watchdog behavior, and the runtime-enumerated Realtek device are observations, not selected clean-slate requirements. No row above selects a Linux configuration, firmware architecture, protocol, product behavior, or control policy.
