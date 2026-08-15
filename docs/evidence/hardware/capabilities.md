# Software-relevant hardware capability limits

This summary contains only record-backed limits or explicit unresolved questions. It is a view over the fact records, not independent evidence; disputed observations are not capability guarantees.

## Verified numeric capacities

| Resource | Verified limit | Qualification | Status |
| --- | --- | --- | --- |
| SOM memory | 512 MB installed DDR3 by fitted Olimex product variant. [HW-095](facts/HW-095.md) | Exact DDR3 part/timings, runtime-usable capacity, reservations, and health are not established. | verified nominal capacity |
| MCU flash | 256 KiB nominal in-system self-programmable flash for the fitted marked ATmega2560. [HW-003](facts/HW-003.md) | Bootloader, fuses, protection, programming state, usable layout, and errata remain unresolved. | verified nominal capacity |
| MCU SRAM | 8 KiB nominal internal SRAM for the fitted marked ATmega2560. [HW-015](facts/HW-015.md) | Runtime availability after firmware, stack, buffers, and libraries is unresolved. | verified nominal capacity |
| MCU EEPROM | 4 KiB nominal EEPROM for the fitted marked ATmega2560. [HW-016](facts/HW-016.md) | Contents, wear state, endurance, protection, reserved addresses, ownership, and layout are unresolved. | verified nominal capacity; endurance unresolved |

## Verified runtime observations, not capability selections

| Runtime area | Dated observation | Qualification |
| --- | --- | --- |
| Legacy kernel and userspace | The fresh ReBrewie boot reported `Linux 3.4.90-Brewie #5` and Buildroot `2014.02-git-g3b4bd90-dirty`. [HW-101](facts/HW-101.md) [HW-102](facts/HW-102.md) | Historical lineage only; neither version is selected for a clean-slate system. |
| Legacy storage layout | The same boot used the recorded `mmcblk0` p1/p2/p3 sizes, with EXT3 root on p2 and EXT3 `/home/brewie` on p3. [HW-103](facts/HW-103.md) | Physical medium, total capacity, health, and endurance are unresolved; the partition sizes and EXT3 are not requirements. |
| Legacy RTC detection | The same boot detected PCF8563 on I2C0 at `0x51` as `rtc0`. [HW-104](facts/HW-104.md) | Physical identity, wiring, electrical limits, battery state, accuracy, and future RTC policy remain unresolved. |
| Modern experimental platform | The fresh Olimex/Debian boot reported kernel `5.10.180-olimex #140856`, `armv7l`, model `Olimex A13-SOM-512`, and 521,216 KiB to Linux. [HW-105](facts/HW-105.md) | Runtime accounting is not fitted-memory identity and does not select a future kernel or memory configuration. |
| Modern experimental watchdog | The same boot enabled the A13 watchdog at `0x1c20c90`, timeout 16 seconds, `nowayout=0`. [HW-106](facts/HW-106.md) | This old captured behavior does not establish application use, reset effects, or a future watchdog policy. |
| Modern experimental WLAN | A fitted-on-date Realtek `0bda:8176` USB adapter loaded `rtl8192cu` and associated. [HW-107](facts/HW-107.md) | Not a permanent hardware, throughput, placement, adapter, or driver requirement. |
| Shared serial enumeration | Both fresh captures enumerate `ttyS0` and `ttyS1` at matching MMIO addresses. [HW-108](facts/HW-108.md) | Corroborates runtime enumeration only, not physical MCU connectivity, telemetry, levels, or protocol. |

## Compute, boot, display, and storage limits

| Area | Record-backed limit or question | Status |
| --- | --- | --- |
| SOM boot media and persistent storage | The dated legacy boot supplies an active `mmcblk0`/EXT3 layout observation, but boot-media identity, physical storage device/capacity, health, interface, and endurance remain unresolved. [HW-103](facts/HW-103.md) | runtime layout verified; physical capability unresolved |
| MCU clock | The verified fitted-U1 record leaves the non-model marking codes uninterpreted and establishes no clock source, frequency, tolerance, fuse, or prescaler state. [HW-002](facts/HW-002.md) | unresolved |
| Display dimensions/format | A 480 by 272 RGB565 scanout was reported on the current SOM, but panel identity, physical bus, timings, and electrical limits are not established. [HW-006](facts/HW-006.md) | disputed observation, not a verified limit |
| Backlight PWM | `pwm-0` is a disputed backlight candidate with separately reported 50 µs period and inverse polarity. Electrical pin, voltage, duty cycle, measurement basis, and exact revision are unresolved. [HW-082](facts/HW-082.md) [HW-092](facts/HW-092.md) [HW-093](facts/HW-093.md) | disputed observations, not verified limits |
| Touch interface | During the dated modern boot, Linux identified Goodix ID 911/version 1060 and enumerated it on I2C bus 2 at `0x14`. Exact fitted part, supply, voltage, pull-ups, interrupt/reset, carrier route, and electrical limits are unresolved. [HW-007](facts/HW-007.md) [HW-008](facts/HW-008.md) | verified runtime observations; physical capability unresolved |
| Networking | A dated modern boot used a fitted Realtek `0bda:8176` USB WLAN adapter with `rtl8192cu`, but permanent networking identity, placement, interface limits, throughput, and future suitability are unresolved. [HW-107](facts/HW-107.md) | verified runtime observation; permanent capability unresolved |

## MCU peripheral and bus limits

| Area | Record-backed limit or question | Status |
| --- | --- | --- |
| ADC | The indexed records expose ADC candidate endpoints, but do not establish resolution, reference, input range, scaling, accuracy, bandwidth, calibration, or safe limit. [HW-049](facts/HW-049.md) [HW-050](facts/HW-050.md) [HW-051](facts/HW-051.md) [HW-052](facts/HW-052.md) [HW-053](facts/HW-053.md) [HW-054](facts/HW-054.md) [HW-055](facts/HW-055.md) | disputed endpoints; numeric limits unresolved |
| Timer/PWM availability | Timer4 and Timer3 are reported allocated to valve pulses and a pump-diagnostics tick, but channels, rates, pulse ranges, interrupt load, and remaining availability are unknown. [HW-059](facts/HW-059.md) [HW-060](facts/HW-060.md) | disputed allocations |
| Pump-DAC bus | Clock, data, chip-select, and LDAC candidates exist, while MISO is only N/C-classified. DAC identity, logic voltage, mode/rate, polarity, timing, and safe limits are unknown. [HW-086](facts/HW-086.md) [HW-087](facts/HW-087.md) [HW-088](facts/HW-088.md) [HW-023](facts/HW-023.md) [HW-073](facts/HW-073.md) | disputed |
| Mass-device buses | Boil SCL/SDA candidates and prepared mash SCL/SDA-like candidates are indexed. Device identity, actual mash interface semantics, address, pull-ups, voltage, calibration, quantity, and limits are unknown. [HW-024](facts/HW-024.md) [HW-089](facts/HW-089.md) [HW-025](facts/HW-025.md) [HW-090](facts/HW-090.md) | disputed |
| Temperature buses | Mash and boil 1-Wire candidates exist, but device identities, pull-ups, voltage, addressing, range, accuracy, and update rate are unknown. [HW-029](facts/HW-029.md) [HW-030](facts/HW-030.md) | disputed |
| SOM-MCU link | Shared `ttyS0`/`ttyS1` enumeration is verified, while the UART/reset physical candidates and traffic/reset observations remain separate. Endpoint pins, MCU binding, telemetry, connector route, voltage, thresholds, and timing are unknown. [HW-108](facts/HW-108.md) [HW-004](facts/HW-004.md) [HW-017](facts/HW-017.md) [HW-005](facts/HW-005.md) [HW-018](facts/HW-018.md) | runtime enumeration verified; physical/electrical link disputed |

## Sensor characteristics

| Sensor class | Record-backed limit or question | Status |
| --- | --- | --- |
| Mash/boil temperature | No indexed record establishes sensor part, range, accuracy, resolution, response time, update rate, or calibration. [HW-029](facts/HW-029.md) [HW-030](facts/HW-030.md) | unresolved behind disputed endpoints |
| Mass/pressure/water level | The measured quantity itself, device identity, range, accuracy, resolution, calibration, update rate, and present boil-device connection are not established; the mash device was only reported absent. [HW-024](facts/HW-024.md) [HW-089](facts/HW-089.md) [HW-026](facts/HW-026.md) | unresolved; absence report disputed |
| Board temperature | Sensor identity, placement, supply, transfer function, range, accuracy, and response time are unknown. [HW-054](facts/HW-054.md) | disputed endpoint; limits unresolved |
| Current sensing | Five ADC endpoint candidates exist; topology, range, scaling, accuracy, bandwidth, calibration, and safe limits are unknown, and uncharacterized ADC counts are not limits. [HW-049](facts/HW-049.md) [HW-050](facts/HW-050.md) [HW-051](facts/HW-051.md) [HW-052](facts/HW-052.md) [HW-053](facts/HW-053.md) | disputed endpoints; limits unresolved |
| AC measure | Quantity, topology, isolation, range, scaling, accuracy, bandwidth, and safety limits are unknown. [HW-055](facts/HW-055.md) | disputed endpoint; limits unresolved |
| Pump tachometers | Pull-ups, levels, polarity, pulse-to-motion relationship, frequency range, and present connection are unknown. [HW-021](facts/HW-021.md) [HW-022](facts/HW-022.md) | disputed endpoints; limits unresolved |

## Actuator-drive constraints

| Actuator class | Record-backed constraint | Status |
| --- | --- | --- |
| Heaters | Candidate MCU outputs and separate current-code-active observations exist, but drive stages, voltages, polarities, load ratings, timing, isolation, and safe limits are unknown. [HW-019](facts/HW-019.md) [HW-020](facts/HW-020.md) [HW-084](facts/HW-084.md) [HW-085](facts/HW-085.md) | disputed |
| Pumps | Enable, tachometer, and DAC candidates exist, but pump/DAC identities, drive stages, levels, mode/rate, polarity, feedback limits, and safe ranges are unknown. [HW-032](facts/HW-032.md) [HW-033](facts/HW-033.md) [HW-021](facts/HW-021.md) [HW-022](facts/HW-022.md) [HW-023](facts/HW-023.md) | disputed |
| Valves | Candidate GPIO endpoints and a Timer4 allocation observation exist, but valve identities, drive stages, supply, polarity, current limit, pulse/travel limits, and connection state are unresolved. [HW-031](facts/HW-031.md) [HW-035](facts/HW-035.md) [HW-039](facts/HW-039.md) [HW-059](facts/HW-059.md) | disputed |
| Inlet solenoids | Two dedicated-output candidates exist, but identity, drive stage, voltage, polarity, current limit, and safe limits are unknown. [HW-046](facts/HW-046.md) [HW-047](facts/HW-047.md) | disputed |
| Fan | An enable candidate exists, but fan identity, drive stage, supply, polarity, current limit, speed-control/feedback capability, and safe limits are unknown. [HW-048](facts/HW-048.md) | disputed |
| Indicators | GPIO candidates exist, but voltage, polarity, current limiting, and active levels are unknown. [HW-034](facts/HW-034.md) [HW-056](facts/HW-056.md) [HW-057](facts/HW-057.md) [HW-058](facts/HW-058.md) | disputed |
| Power enables | Pre-charge, 5 V, 6.5 V servo, and 12 V candidates exist, but destinations, polarity, rail tolerances, sequencing, current capability, and safety effect are unknown. [HW-011](facts/HW-011.md) [HW-012](facts/HW-012.md) [HW-013](facts/HW-013.md) [HW-014](facts/HW-014.md) | disputed |
| Audio/sounder | The fitted amplifier position is verified unpopulated; historical path, +5 V supply, and standby candidates do not establish current audio capability or electrical limits. [HW-071](facts/HW-071.md) [HW-068](facts/HW-068.md) [HW-070](facts/HW-070.md) [HW-081](facts/HW-081.md) | present unpopulated state verified; path/limits disputed |

## Other discovered constraints

- The prepared mash-mass and valve-5 endpoints were reported unpopulated, but both current-state reports remain disputed and must not be treated as current-machine conclusions. [HW-026](facts/HW-026.md) [HW-038](facts/HW-038.md)
- Structurally observed connectors do not establish pin-to-net connectivity, load ratings, electrical levels, or physical locations. [HW-061](facts/HW-061.md) [HW-062](facts/HW-062.md) [HW-063](facts/HW-063.md) [HW-064](facts/HW-064.md) [HW-065](facts/HW-065.md) [HW-066](facts/HW-066.md) [HW-067](facts/HW-067.md)
- Original Brewie GPIO aliases were reported absent on the current image, but that does not establish physical disconnection or current pin ownership. [HW-080](facts/HW-080.md)

Historical partition sizes, EXT3, kernel versions, Buildroot, the old captured watchdog behavior, and the fitted-on-date Realtek adapter remain observations rather than selected clean-slate requirements. These limits constrain future evidence gathering only. They do not select an operating system, software architecture, firmware implementation, protocol, brewing behavior, or control policy.
