# Hardware evidence baseline

## Scope and navigation

The target is the currently inspected machine with fitted SOM marked `Olimex A13-SOM (512)`, revision `G`, fitted carrier marked `Brewie ARM board`, revision `V1p2`, and fitted U1 marked `ATMEGA2560`. The marking observations were made with the machine unplugged, and the U1 observation was also explicitly dry. [HW-001](facts/HW-001.md) [HW-094](facts/HW-094.md) [HW-002](facts/HW-002.md)

The carrier's audio-amplifier IC position is presently absent/unpopulated; the cause and wider circuit condition are not established. [HW-071](facts/HW-071.md)

Evidence and status records:

- [Source boundary and inventory](sources.md)
- [Schematic readability](schematic-readability.md)
- [Hardware fact index](fact-index.md)
- [Verification register](verification-register.md)

Detailed status-preserving views:

- [SOM and carrier](som-carrier.md)
- [MCU](mcu.md)
- [SOM-MCU interconnect](som-mcu-interconnect.md)
- [Software-visible sensors and actuators](brewing-devices.md)
- [Software-relevant capability limits](capabilities.md)

These summaries are views over the linked fact records, not independent evidence. A disputed candidate remains disputed wherever it is repeated. This baseline contains no product design, control design, brewing behavior, protocol, firmware/software architecture, Linux choice, or implementation decision.

## Verified configuration overview

| Configuration item | Verified record-backed conclusion | Status |
| --- | --- | --- |
| SOM marking | Fitted module reads `Olimex A13-SOM (512)`, PCB revision `G`; this verifies the marking only. [HW-001](facts/HW-001.md) | verified |
| Carrier marking | Fitted carrier reads `Brewie ARM board`, revision `V1p2`; electrical and schematic correspondence are not inferred. [HW-094](facts/HW-094.md) | verified |
| SOM memory | The fitted marked product variant has 512 MB nominal installed DDR3; exact part/timings and runtime availability are not established. [HW-095](facts/HW-095.md) | verified |
| MCU marking | Fitted U1 explicitly reads `ATMEGA2560`; the other transcribed codes are retained without decoding. [HW-002](facts/HW-002.md) | verified |
| MCU flash | 256 KiB nominal flash for the fitted marked model; usable layout is unresolved. [HW-003](facts/HW-003.md) | verified |
| MCU SRAM | 8 KiB nominal SRAM for the fitted marked model; runtime availability is unresolved. [HW-015](facts/HW-015.md) | verified |
| MCU EEPROM | 4 KiB nominal EEPROM for the fitted marked model; wear, contents, protection, and layout are unresolved. [HW-016](facts/HW-016.md) | verified |
| Audio population | Audio-amplifier IC position is absent/unpopulated on the fitted carrier; cause, circuit condition, and behavior are outside the verified claim. [HW-071](facts/HW-071.md) | verified |

The [fact index](fact-index.md) contains 8 verified and 87 disputed records. There are no proposed or provisionally accepted records. No disputed record below is accepted as a baseline conclusion.

## All disputed facts and blocked decisions

Every disputed record is retained here individually. “Blocked” means the candidate may guide verification, but cannot support a consequential hardware, electrical, configuration, or integration decision. The audio rows explicitly retain their disputed status even though audio availability is an owner-approved milestone removal.

| Record | Disputed candidate or observation | Decision that remains blocked or bounded |
| --- | --- | --- |
| [HW-004](facts/HW-004.md) | Candidate physical UART connection between SOM and MCU. | Consequential electrical-interface changes are blocked; only non-destructive observation is bounded as permissible. |
| [HW-005](facts/HW-005.md) | A13 PE9 as SOM-controlled MCU-reset candidate. | Automated use of this reset mapping is blocked. |
| [HW-006](facts/HW-006.md) | Reported 480 by 272 RGB565 Linux scanout. | Hard-to-reverse display-mode, panel, or physical-bus decisions are blocked. |
| [HW-007](facts/HW-007.md) | Goodix-family touch-controller candidate. | Consequential controller replacement or exact-part assumptions are blocked. |
| [HW-008](facts/HW-008.md) | Touch candidate on I2C bus 2 at address `0x14`. | Touch wiring and electrical-interface changes are blocked. |
| [HW-009](facts/HW-009.md) | A13 PB3 legacy LCD-backlight candidate. | Automated backlight control is blocked. |
| [HW-010](facts/HW-010.md) | A13 PB10 legacy LCD-power-enable candidate. | Automated display-power switching is blocked. |
| [HW-011](facts/HW-011.md) | PB5/pin 24 `PRE_CHARGE` candidate. | Behavior or safety conclusions based on this signal are blocked. |
| [HW-012](facts/HW-012.md) | PB6/pin 25 `PWR_EN_5V` candidate. | Behavior or safety conclusions based on this signal are blocked. |
| [HW-013](facts/HW-013.md) | PB7/pin 26 `PWR_EN_6V5_SERVO` candidate. | Behavior or safety conclusions based on this signal are blocked. |
| [HW-014](facts/HW-014.md) | PH7/pin 27 `PWR_EN_12V` candidate. | Behavior or safety conclusions based on this signal are blocked. |
| [HW-017](facts/HW-017.md) | Reported bidirectional SOM-MCU traffic through `/dev/ttyS1`. | Consequential hard-coded endpoint binding is blocked. |
| [HW-018](facts/HW-018.md) | Reported MCU reset after `gpio137` high-then-low drive. | Automated reset/recovery behavior is blocked. |
| [HW-019](facts/HW-019.md) | PG5/pin 1 mash-heater-2 GPIO/timer-output candidate. | Consequential use is blocked pending physical and electrical verification. |
| [HW-020](facts/HW-020.md) | PE2/pin 4 boil-heater-1 GPIO candidate. | Consequential use is blocked pending physical and electrical verification. |
| [HW-021](facts/HW-021.md) | PE4/pin 6 boil-pump tachometer candidate. | Consequential use is blocked pending pump, level, polarity, and pulse verification. |
| [HW-022](facts/HW-022.md) | PE5/pin 7 mash-pump tachometer candidate. | Consequential use is blocked pending pump, level, polarity, and pulse verification. |
| [HW-023](facts/HW-023.md) | PH6/pin 18 pump-DAC LDAC candidate. | Consequential use is blocked pending DAC, level, polarity, and routing verification. |
| [HW-024](facts/HW-024.md) | PD0/pin 43 boil-mass SCL candidate. | Consequential use is blocked pending device, bus, calibration, and limit verification. |
| [HW-025](facts/HW-025.md) | PD4/pin 47 prepared mash-mass SCL-like candidate. | Interface assignment and consequential use are blocked. |
| [HW-026](facts/HW-026.md) | Report that no mash-mass device was present. | Current availability conclusions are blocked pending dated physical confirmation. |
| [HW-027](facts/HW-027.md) | PD2/pin 45 drain-button candidate. | Consequential use is blocked pending direction, level, pull-up, polarity, and debounce verification. |
| [HW-028](facts/HW-028.md) | PD7/pin 50 power-button candidate. | Consequential use is blocked pending direction, level, pull-up, polarity, and debounce verification. |
| [HW-029](facts/HW-029.md) | PG0/pin 51 mash-temperature 1-Wire candidate. | Consequential use is blocked pending sensor identity and characterized limits. |
| [HW-030](facts/HW-030.md) | PG1/pin 52 boil-temperature 1-Wire candidate. | Consequential use is blocked pending sensor identity and characterized limits. |
| [HW-031](facts/HW-031.md) | PC1/pin 54 boil-inlet-valve candidate. | Consequential use is blocked pending valve, drive-stage, level, polarity, and limit verification. |
| [HW-032](facts/HW-032.md) | PC3/pin 56 mash-pump-enable candidate. | Consequential use is blocked pending pump and drive-stage verification. |
| [HW-033](facts/HW-033.md) | PC5/pin 58 boil-pump-enable candidate. | Consequential use is blocked pending pump and drive-stage verification. |
| [HW-034](facts/HW-034.md) | PC7/pin 60 drain-button-LED candidate. | Consequential use is blocked pending circuit, level, polarity, and current-limit verification. |
| [HW-035](facts/HW-035.md) | PJ2/pin 65 mash-inlet-valve candidate. | Consequential use is blocked pending valve and drive-stage verification. |
| [HW-036](facts/HW-036.md) | PJ3/pin 66 boil-return-valve candidate. | Consequential use is blocked pending valve and drive-stage verification. |
| [HW-037](facts/HW-037.md) | PJ4/pin 67 prepared valve-5 candidate. | Consequential use is blocked pending intended-device and drive-stage verification. |
| [HW-038](facts/HW-038.md) | Report that no valve-5 device was present. | Current availability conclusions are blocked pending dated physical confirmation. |
| [HW-039](facts/HW-039.md) | PJ5/pin 68 outlet-valve candidate. | Consequential use is blocked pending valve and drive-stage verification. |
| [HW-040](facts/HW-040.md) | PJ6/pin 69 cooling-valve candidate. | Consequential use is blocked pending valve and drive-stage verification. |
| [HW-041](facts/HW-041.md) | PA7/pin 71 hop-2-valve candidate. | Consequential use or resource allocation is blocked pending verification. |
| [HW-042](facts/HW-042.md) | PA6/pin 72 mash-return-valve candidate. | Consequential use or resource allocation is blocked pending verification. |
| [HW-043](facts/HW-043.md) | PA5/pin 73 hop-4-valve candidate. | Consequential use or resource allocation is blocked pending verification. |
| [HW-044](facts/HW-044.md) | PA4/pin 74 hop-1-valve candidate. | Consequential use or resource allocation is blocked pending verification. |
| [HW-045](facts/HW-045.md) | PA3/pin 75 hop-3-valve candidate. | Consequential use or resource allocation is blocked pending verification. |
| [HW-046](facts/HW-046.md) | PA2/pin 76 cooling-inlet-solenoid output candidate. | Consequential use or resource allocation is blocked pending solenoid and drive-stage verification. |
| [HW-047](facts/HW-047.md) | PA1/pin 77 brew-inlet-solenoid output candidate. | Consequential use or resource allocation is blocked pending solenoid and drive-stage verification. |
| [HW-048](facts/HW-048.md) | PA0/pin 78 fan-enable candidate. | Consequential use or resource allocation is blocked pending fan and drive-stage verification. |
| [HW-049](facts/HW-049.md) | PK6/pin 83 mash-side current-sense candidate. | Consequential use is blocked pending topology, reference, scaling, accuracy, and limit verification. |
| [HW-050](facts/HW-050.md) | PK5/pin 84 boil-side current-sense candidate. | Consequential use is blocked pending topology, reference, scaling, accuracy, and limit verification. |
| [HW-051](facts/HW-051.md) | PK4/pin 85 hop-valves current-sense candidate. | Consequential use is blocked pending topology, reference, scaling, accuracy, and limit verification. |
| [HW-052](facts/HW-052.md) | PK3/pin 86 cooling-inlet current-sense candidate. | Consequential use is blocked; uncharacterized ADC counts are not accepted limits. |
| [HW-053](facts/HW-053.md) | PK2/pin 87 brew-inlet current-sense candidate. | Consequential use is blocked; uncharacterized ADC counts are not accepted limits. |
| [HW-054](facts/HW-054.md) | PK1/pin 88 MCU-board-temperature candidate. | Consequential use is blocked pending sensor identity, scaling, accuracy, and response verification. |
| [HW-055](facts/HW-055.md) | PK0/pin 89 AC-measure candidate. | Consequential use is blocked pending quantity, isolation, scaling, accuracy, and safety verification. |
| [HW-056](facts/HW-056.md) | PL5/pin 40 current power-LED candidate. | Consequential use is blocked pending circuit, level, polarity, and current-limit verification. |
| [HW-057](facts/HW-057.md) | PF2/pin 95 MCU-LED1 candidate. | Consequential use/resource assumptions are blocked pending circuit and ADC-availability verification. |
| [HW-058](facts/HW-058.md) | PF1/pin 96 MCU-LED2 candidate. | Consequential use/resource assumptions are blocked pending circuit and ADC-availability verification. |
| [HW-059](facts/HW-059.md) | Reported Timer4 allocation to valve-servo pulse generation. | Consequential timer/resource assumptions are blocked pending channel, rate, load, and endpoint verification. |
| [HW-060](facts/HW-060.md) | Reported Timer3 allocation to a pump-diagnostics tick. | Consequential timer/resource assumptions are blocked pending channel, rate, load, and purpose verification. |
| [HW-061](facts/HW-061.md) | Structural J11 `MASS (unused)` four-position connector observation. | Pin-to-net, device, and physical-location conclusions are blocked. |
| [HW-062](facts/HW-062.md) | Structural J7 `TEMP` three-position connector observation. | Pin-to-net, sensor, zone, voltage, and physical-location conclusions are blocked. |
| [HW-063](facts/HW-063.md) | Structural J8 `PUMP` four-position connector observation. | Pin-to-net, pump, voltage, and physical-location conclusions are blocked. |
| [HW-064](facts/HW-064.md) | Structural J1 `Heat2` two-position connector observation. | Pin-to-net, zone, voltage, load, and physical-location conclusions are blocked. |
| [HW-065](facts/HW-065.md) | Structural J18 `Heat2` two-position connector observation. | Pin-to-net, zone, voltage, load, and physical-location conclusions are blocked. |
| [HW-066](facts/HW-066.md) | Structural J9 `VALVE 10 - Mash Return` three-position connector observation. | Pin functions, valve identity, voltage, and physical-location conclusions are blocked. |
| [HW-067](facts/HW-067.md) | Structural J10 `VALVE 11 - Boil Inlet` three-position connector observation. | Pin functions, valve identity, voltage, and physical-location conclusions are blocked. |
| [HW-068](facts/HW-068.md) | Historical candidate that the carrier sounder is amplifier-driven. | No milestone decision is blocked because audio availability was removed from scope; repair/use conclusions remain unsupported. |
| [HW-069](facts/HW-069.md) | Historical candidate from SOM `HPOUTL`/`HPCOM` to carrier-amplifier input. | No milestone decision is blocked under the audio removal; electrical/path conclusions remain unsupported. |
| [HW-070](facts/HW-070.md) | Historical candidate that carrier amplifier supply is on +5 V. | No milestone decision is blocked under the audio removal; rail and amplifier-limit conclusions remain unsupported. |
| [HW-072](facts/HW-072.md) | Reported current A13 PB2 assignment to `1c20e00.pwm`. | Consequential pin-mux or consumer use is blocked pending immutable configuration and routing evidence. |
| [HW-073](facts/HW-073.md) | PB3/pin 22 pump-DAC MISO row classified N/C. | Physical-disconnection and bus-design assumptions are blocked. |
| [HW-074](facts/HW-074.md) | PF3/pin 94 row classified N/C. | Physical-disconnection and resource assumptions are blocked. |
| [HW-075](facts/HW-075.md) | A13 PB15 legacy drain/second-button candidate. | Consequential input use is blocked pending identity, route, level, pull-up, and polarity verification. |
| [HW-076](facts/HW-076.md) | A13 PB4 legacy hold-power candidate. | Consequential power control is blocked pending destination, route, level, polarity, and effect verification. |
| [HW-077](facts/HW-077.md) | A13 PB16 legacy second-LED candidate. | Consequential indicator use is blocked pending LED, route, level, polarity, and current-limit verification. |
| [HW-078](facts/HW-078.md) | A13 PC7 legacy power-related GPIO candidate. | Consequential use is blocked pending direction, function, route, level, and polarity verification. |
| [HW-079](facts/HW-079.md) | Historical A13 PB2 legacy buzzer alias. | No milestone decision is blocked under the audio removal; direct-wiring/current-consumer conclusions remain unsupported. |
| [HW-080](facts/HW-080.md) | Report that the current image does not create original Brewie GPIO aliases. | Physical-disconnection and stable endpoint-binding conclusions are blocked. |
| [HW-081](facts/HW-081.md) | Historical candidate for a 10 kΩ pull-down on amplifier standby. | No milestone decision is blocked under the audio removal; standby-circuit conclusions remain unsupported. |
| [HW-082](facts/HW-082.md) | Reported identification of current `pwm-0` as backlight PWM. | Consequential PWM-consumer or display-control use is blocked. |
| [HW-083](facts/HW-083.md) | Inferred mapping from A13 PB2 to Linux `gpio34`. | Consequential GPIO numbering/use is blocked pending direct confirmation. |
| [HW-084](facts/HW-084.md) | Report that PG5/mash-heater-2 is active in current code. | Consequential output behavior assumptions are blocked pending exact firmware and electrical verification. |
| [HW-085](facts/HW-085.md) | Report that PE2/boil-heater-1 is active in current code. | Consequential output behavior assumptions are blocked pending exact firmware and electrical verification. |
| [HW-086](facts/HW-086.md) | PB1/pin 20 pump-DAC clock candidate. | Consequential bus use is blocked pending DAC, direction, level, mode/rate, and limit verification. |
| [HW-087](facts/HW-087.md) | PB2/pin 21 pump-DAC serial-data candidate. | Consequential bus use is blocked pending DAC, level, mode/rate, and limit verification. |
| [HW-088](facts/HW-088.md) | PB4/pin 23 pump-DAC chip-select candidate. | Consequential bus use is blocked pending DAC, direction, level, polarity, timing, and limit verification. |
| [HW-089](facts/HW-089.md) | PD1/pin 44 boil-mass SDA candidate. | Consequential use is blocked pending device, bus, calibration, and limit verification. |
| [HW-090](facts/HW-090.md) | PD5/pin 48 prepared mash-mass SDA-like candidate. | Interface assignment and consequential use are blocked. |
| [HW-091](facts/HW-091.md) | PF3 described as no longer the active power-LED pin. | Physical-trace and active-power-LED conclusions are blocked. |
| [HW-092](facts/HW-092.md) | Reported 50 µs period for current `pwm-0`. | Consequential timing use is blocked pending measurement, pin, duty-cycle, voltage, and revision verification. |
| [HW-093](facts/HW-093.md) | Reported inverse polarity for current `pwm-0`. | Consequential polarity use is blocked pending electrical meaning, pin, voltage, duty-cycle, and revision verification. |

## Blocked decision summary

- Consequential image, kernel, boot-media, persistent-storage, networking, display, touch, and device-tree decisions remain blocked by the disputed compute/platform records and by evidence gaps explicitly retained in the verified identity records. [HW-001](facts/HW-001.md) [HW-006](facts/HW-006.md) [HW-007](facts/HW-007.md) [HW-008](facts/HW-008.md) [HW-009](facts/HW-009.md) [HW-010](facts/HW-010.md) [HW-094](facts/HW-094.md)
- Consequential MCU programming, exact image layout, runtime allocation, and persistence layout remain blocked despite verified nominal capacities. [HW-002](facts/HW-002.md) [HW-003](facts/HW-003.md) [HW-015](facts/HW-015.md) [HW-016](facts/HW-016.md)
- Consequential integration of serial, reset, power, heaters, pumps, sensing, buttons, valves, solenoids, fan, indicators, or electrical monitoring remains blocked on the corresponding disputed mappings and limits. [HW-004](facts/HW-004.md) [HW-005](facts/HW-005.md) [HW-011](facts/HW-011.md) [HW-019](facts/HW-019.md) [HW-021](facts/HW-021.md) [HW-024](facts/HW-024.md) [HW-027](facts/HW-027.md) [HW-031](facts/HW-031.md) [HW-046](facts/HW-046.md) [HW-049](facts/HW-049.md)
- Audio/sounder availability is not a milestone blocker, but all historical audio-path candidates remain disputed and the verified unpopulated amplifier state supports no repair or behavior conclusion. [HW-068](facts/HW-068.md) [HW-069](facts/HW-069.md) [HW-070](facts/HW-070.md) [HW-071](facts/HW-071.md) [HW-079](facts/HW-079.md) [HW-081](facts/HW-081.md)

## Explicit non-design statement

This evidence baseline records identity, capacity, candidates, observations, limits, and unresolved questions only. It does not define a SOM-MCU protocol, control policy, brewing process, safety behavior, product behavior, firmware or software architecture, Linux selection/configuration, ownership model, recovery behavior, timing policy, or implementation.
