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
| CPU architecture | The indexed verified evidence establishes the fitted A13-SOM product marking, but does not establish a CPU core or instruction-set claim. [HW-001](facts/HW-001.md) | unresolved; only the linked identity claim is verified |
| Persistent storage | The fitted-SOM marking record explicitly does not identify boot media; no storage device identity, capacity, interface, or endurance conclusion is supported by that record. [HW-001](facts/HW-001.md) | unresolved |
| Boot path hardware | The fitted-SOM marking record explicitly excludes boot-media and carrier-wiring conclusions, so the hardware boot path is not established. [HW-001](facts/HW-001.md) | unresolved |

## Display and input

| Endpoint | Candidate mapping or observation | Relevant limits | Status |
| --- | --- | --- | --- |
| Attached display | A 480 by 272 RGB565 Linux scanout was reported, but panel identity, physical bus, electrical interface, and timing are not established. [HW-006](facts/HW-006.md) | The reported mode is not verified hardware capability. | disputed |
| LCD backlight | A13 PB3 is the legacy backlight-control candidate. [HW-009](facts/HW-009.md) | Carrier routing, voltage, polarity, and current-image control are unknown. | disputed |
| LCD power enable | A13 PB10 is the legacy power-enable candidate. [HW-010](facts/HW-010.md) | Carrier routing, voltage, polarity, and current-image control are unknown. | disputed |
| Current backlight PWM | `pwm-0` is identified as a backlight PWM, with a reported 50 µs period and inverse polarity. [HW-082](facts/HW-082.md) [HW-092](facts/HW-092.md) [HW-093](facts/HW-093.md) | Consumer assignment, electrical pin, voltage, measurement basis, duty cycle, and exact revision are unresolved. | disputed |
| Touch identity | The attached touch-controller candidate is in the Goodix family. [HW-007](facts/HW-007.md) | Exact part, panel revision, interrupt line, and reset line are unknown. | disputed |
| Touch bus | The controller is a candidate on SOM I2C bus 2 at address `0x14`. [HW-008](facts/HW-008.md) | Pull-ups, voltage, carrier routing, interrupt, and reset are unknown. | disputed |

## Networking and exposed interfaces

| Area | Record-backed boundary | Status |
| --- | --- | --- |
| Networking | The verified carrier-marking claim does not establish any networking device, connector, interface, or limit. [HW-094](facts/HW-094.md) | unresolved |
| SOM-MCU serial | A physical UART connection is a candidate, and bidirectional traffic was separately reported at `/dev/ttyS1`. Physical SOM/MCU pins, carrier connector, and levels are unknown. [HW-004](facts/HW-004.md) [HW-017](facts/HW-017.md) | disputed |
| Touch I2C | I2C bus 2, address `0x14`, is a candidate software-visible endpoint; its physical and electrical realization is not established. [HW-008](facts/HW-008.md) | disputed |
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
| Watchdog | The indexed reset records establish only disputed reset candidates/observations and do not establish watchdog hardware. [HW-005](facts/HW-005.md) [HW-018](facts/HW-018.md) | unresolved |

No row above selects a Linux configuration, firmware architecture, protocol, product behavior, or control policy.
