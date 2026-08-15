# Software-visible sensors and actuators

This inventory is a view over hardware fact records. Unless a row says **verified**, its endpoint is a disputed candidate rather than an established machine interface. The inventory records hardware exposure only; it defines no brewing behavior or control policy.

## Display, touch, buttons, and indicators

| Device or endpoint | Identity and endpoint | Hardware interface or drive fact | Electrical/current-state limits | Status |
| --- | --- | --- | --- | --- |
| Display | Attached panel identity unknown; a 480 by 272 RGB565 scanout was reported. | Physical display bus and timing are not established. [HW-006](facts/HW-006.md) | Panel model, voltage, timing, and carrier routing unknown. | disputed |
| Display backlight | A13 PB3 is the legacy control candidate; `pwm-0` is separately identified as a backlight PWM with reported 50 µs period and inverse polarity. | GPIO/PWM relationship is not reconciled. [HW-009](facts/HW-009.md) [HW-082](facts/HW-082.md) [HW-092](facts/HW-092.md) [HW-093](facts/HW-093.md) | Electrical pin, voltage, polarity meaning, duty cycle, drive stage, and exact revision unknown. | disputed |
| Display power | A13 PB10 is the legacy LCD power-enable candidate. | GPIO candidate. [HW-010](facts/HW-010.md) | Voltage, polarity, routing, destination, and current-image control unknown. | disputed |
| Touchscreen | During the fresh 2026-08-12 Olimex/Debian boot, Linux identified Goodix ID 911/version 1060 and enumerated it on I2C bus 2 at address `0x14`. | Verified dated runtime identity and Linux endpoint only. [HW-007](facts/HW-007.md) [HW-008](facts/HW-008.md) | Exact fitted part, pull-ups, voltage, carrier routing, interrupt, reset, and electrical limits remain unknown. | verified runtime observations; physical identity/interface unresolved |
| Drain button | MCU PD2/pin 45 candidate. A separate legacy SOM PB15 candidate ambiguously names drain/second button. | GPIO candidates; direction is unresolved for the MCU mapping. [HW-027](facts/HW-027.md) [HW-075](facts/HW-075.md) | Physical identity/reconciliation, voltage, pull-up, active level, and debounce unknown. | disputed |
| Power button | MCU PD7/pin 50 candidate. | GPIO candidate; direction is unresolved. [HW-028](facts/HW-028.md) | Connector, voltage, pull-up, active level, debounce, and safety significance unknown. | disputed |
| Drain-button LED | MCU PC7/pin 60 candidate. | GPIO candidate; direction is unresolved. [HW-034](facts/HW-034.md) | Circuit, connector, voltage, polarity, current limiting, and active level unknown. | disputed |
| Power LED | MCU PL5/pin 40 is the current candidate; PF3/pin 94 is separately N/C-classified and described as no longer active. | GPIO candidate plus separate mapping-status records. [HW-056](facts/HW-056.md) [HW-074](facts/HW-074.md) [HW-091](facts/HW-091.md) | Physical trace, circuit, voltage, polarity, and current limiting unknown. | disputed |
| MCU LEDs 1 and 2 | MCU PF2/pin 95 and PF1/pin 96 candidates. | ADC-capable GPIO candidates. [HW-057](facts/HW-057.md) [HW-058](facts/HW-058.md) | Circuit, direction, voltage, polarity, current limiting, active level, and ADC availability unknown. | disputed |
| Legacy second LED | A13 PB16 candidate. | GPIO output candidate. [HW-077](facts/HW-077.md) | LED identity, drive circuit, connector, voltage, polarity, and current limit unknown. | disputed |

## Thermal and quantity sensing

| Device or endpoint | Identity and MCU endpoint | Hardware interface fact | Electrical/current-state limits | Status |
| --- | --- | --- | --- | --- |
| Mash temperature | Sensor identity unknown; PG0/pin 51 candidate. | `MASH_TEMP_1WIRE` candidate. [HW-029](facts/HW-029.md) | Connector, pull-up, voltage, addressing, accuracy, range, update rate, and connection state unknown. | disputed |
| Boil temperature | Sensor identity unknown; PG1/pin 52 candidate. | `BOIL_TEMP_1WIRE` candidate. [HW-030](facts/HW-030.md) | Connector, pull-up, voltage, addressing, accuracy, range, update rate, and connection state unknown. | disputed |
| MCU-board temperature | Sensor identity unknown; PK1/pin 88 candidate. | ADC input candidate. [HW-054](facts/HW-054.md) | Location, supply, voltage range, reference, scaling, accuracy, and response time unknown. | disputed |
| Boil mass/pressure/water-level endpoint | Device identity and measured quantity unknown; PD0/pin 43 SCL and PD1/pin 44 SDA candidates. | I2C candidate. [HW-024](facts/HW-024.md) [HW-089](facts/HW-089.md) | Connector, address, pull-ups, voltage, calibration, range, accuracy, and present connection unknown. | disputed |
| Prepared mash mass endpoint | Device identity unknown; PD4/pin 47 SCL-like and PD5/pin 48 SDA-like candidates. | GPIO/timer mappings; actual interface semantics are not established. [HW-025](facts/HW-025.md) [HW-090](facts/HW-090.md) | A device was reported absent; connector identity, voltage, pull-up, and limits remain unknown. [HW-026](facts/HW-026.md) | disputed; reported unpopulated state is also disputed |
| MASS connector structure | J11, value `MASS (unused)`, four positions. | Structural connector observation only. [HW-061](facts/HW-061.md) | No device identity, physical location, or pin-to-net mapping is established. | disputed |
| TEMP connector structure | J7, value `TEMP`, three positions. | Structural connector observation only. [HW-062](facts/HW-062.md) | No sensor identity, zone, voltage, location, or pin-to-net mapping is established. | disputed |

## Heaters and power-support outputs

The project owner reports that both physical heater loads are currently disconnected. This dated state does not identify either heater, connect either load to a candidate row below, or establish original factory wiring, connector mapping, electrical limits, or later state. [HW-099](facts/HW-099.md)

| Device or endpoint | MCU endpoint | Hardware drive fact | Electrical/current-state limits | Status |
| --- | --- | --- | --- | --- |
| Mash heater 2 | PG5/pin 1 candidate. | GPIO/timer-output mapping; separately described as active in current code. [HW-019](facts/HW-019.md) [HW-084](facts/HW-084.md) | Drive stage, voltage, polarity, timer channel, load rating, safe limit, exact firmware, and initialization state unknown. | disputed |
| Boil heater 1 | PE2/pin 4 candidate. | GPIO mapping; separately described as active in current code. [HW-020](facts/HW-020.md) [HW-085](facts/HW-085.md) | Drive stage, voltage, polarity, load rating, safe limit, exact firmware, and initialization state unknown. | disputed |
| Heater connector structures | J1 and J18, each value `Heat2`, two positions. | Structural connector observations only. [HW-064](facts/HW-064.md) [HW-065](facts/HW-065.md) | Zone correspondence, voltage, load rating, physical location, and pin-to-net mapping unknown. | disputed |
| Pre-charge | PB5/pin 24 candidate. | GPIO candidate. [HW-011](facts/HW-011.md) | Destination circuitry, direction, voltage, polarity, and safety behavior unknown. | disputed |
| 5 V enable | PB6/pin 25 candidate. | GPIO candidate. [HW-012](facts/HW-012.md) | Destination circuitry, direction, voltage, polarity, and safety behavior unknown. | disputed |
| 6.5 V servo enable | PB7/pin 26 candidate. | GPIO candidate. [HW-013](facts/HW-013.md) | Destination circuitry, direction, voltage, polarity, and safety behavior unknown. | disputed |
| 12 V enable | PH7/pin 27 candidate. | GPIO candidate. [HW-014](facts/HW-014.md) | Destination circuitry, direction, voltage, polarity, and safety behavior unknown. | disputed |
| Legacy hold-power | A13 PB4 candidate. | SOM GPIO output candidate. [HW-076](facts/HW-076.md) | Destination, voltage, polarity, power-domain effect, and current capability unknown. | disputed |
| Legacy power-related endpoint | A13 PC7 candidate. | Direction and function are not established. [HW-078](facts/HW-078.md) | Destination, voltage, polarity, and current capability unknown. | disputed |

## Pumps and pump DAC

The project owner reports that both physical pump loads are currently disconnected. This dated state does not identify either pump, connect either load to a candidate row below, or establish original factory wiring, connector, enable, tachometer, DAC mapping, electrical limits, or later state. [HW-100](facts/HW-100.md)

| Device or endpoint | MCU endpoint | Hardware interface or drive fact | Electrical/current-state limits | Status |
| --- | --- | --- | --- | --- |
| Mash pump enable | PC3/pin 56 candidate. | GPIO candidate; direction is unresolved. [HW-032](facts/HW-032.md) | Pump identity, drive stage, connector, voltage, polarity, semantics, and safe limits unknown. | disputed |
| Boil pump enable | PC5/pin 58 candidate. | GPIO candidate; direction is unresolved. [HW-033](facts/HW-033.md) | Pump identity, drive stage, connector, voltage, polarity, semantics, and safe limits unknown. | disputed |
| Mash pump tachometer | PE5/pin 7 candidate. | Interrupt-capable GPIO candidate. [HW-022](facts/HW-022.md) | Pump identity, direction, pull-up, polarity, voltage, pulse relationship, limits, and connection state unknown. | disputed |
| Boil pump tachometer | PE4/pin 6 candidate. | Interrupt-capable GPIO candidate. [HW-021](facts/HW-021.md) | Pump identity, direction, pull-up, polarity, voltage, pulse relationship, limits, and connection state unknown. | disputed |
| Pump DAC | DAC identity unknown; PB1/pin 20 clock, PB2/pin 21 data input, PB4/pin 23 chip select, PH6/pin 18 LDAC candidates. | SPI-like candidate lines plus GPIO LDAC. [HW-086](facts/HW-086.md) [HW-087](facts/HW-087.md) [HW-088](facts/HW-088.md) [HW-023](facts/HW-023.md) | Destination pins, logic voltage, rate/mode, polarity, and safe limits unknown. | disputed |
| Pump DAC MISO | PB3/pin 22 row classified N/C. | Mapping classification only. [HW-073](facts/HW-073.md) | The source itself questions connection, so physical disconnection is not established. | disputed |
| Pump timer allocation | Timer3 is reported used for a pump diagnostics tick. | Timer allocation observation only. [HW-060](facts/HW-060.md) | Channel, frequency, meaning, interrupt load, and pump relationship unknown. | disputed |
| PUMP connector structure | J8, value `PUMP`, four positions. | Structural connector observation only. [HW-063](facts/HW-063.md) | Pump identity, voltage, location, and pin-to-net mapping unknown. | disputed |

## Valves, solenoids, and fan

| Device or endpoint | MCU endpoint and drive fact | Electrical/current-state limits | Status |
| --- | --- | --- | --- |
| Boil inlet valve | PC1/pin 54 GPIO candidate. [HW-031](facts/HW-031.md) | Identity, drive stage, connector, voltage, polarity, current limit, travel positions, and connection state unknown. | disputed |
| Mash inlet valve | PJ2/pin 65 GPIO candidate. [HW-035](facts/HW-035.md) | Identity, drive stage, connector, voltage, polarity, current limit, travel positions, and connection state unknown. | disputed |
| Boil return valve | PJ3/pin 66 GPIO candidate. [HW-036](facts/HW-036.md) | Identity, drive stage, connector, voltage, polarity, current limit, travel positions, and connection state unknown. | disputed |
| Prepared valve 5 | PJ4/pin 67 GPIO candidate. [HW-037](facts/HW-037.md) | A valve was reported absent; intended identity, connector, voltage, polarity, and drive limit remain unknown. [HW-038](facts/HW-038.md) | disputed; reported unpopulated state is also disputed |
| Outlet valve | PJ5/pin 68 GPIO candidate. [HW-039](facts/HW-039.md) | Identity, drive stage, connector, voltage, polarity, current limit, travel positions, and connection state unknown. | disputed |
| Cooling valve | PJ6/pin 69 GPIO candidate. [HW-040](facts/HW-040.md) | Identity, drive stage, connector, voltage, polarity, current limit, travel positions, and connection state unknown. | disputed |
| Hop 2 valve | PA7/pin 71 GPIO candidate. [HW-041](facts/HW-041.md) | Identity, drive stage, connector, voltage, polarity, current limit, travel positions, and connection state unknown. | disputed |
| Mash return valve | PA6/pin 72 GPIO candidate. [HW-042](facts/HW-042.md) | Identity, drive stage, connector, voltage, polarity, current limit, travel positions, and connection state unknown. | disputed |
| Hop 4 valve | PA5/pin 73 GPIO candidate. [HW-043](facts/HW-043.md) | Identity, drive stage, connector, voltage, polarity, current limit, travel positions, and connection state unknown. | disputed |
| Hop 1 valve | PA4/pin 74 GPIO candidate. [HW-044](facts/HW-044.md) | Identity, drive stage, connector, voltage, polarity, current limit, travel positions, and connection state unknown. | disputed |
| Hop 3 valve | PA3/pin 75 GPIO candidate. [HW-045](facts/HW-045.md) | Identity, drive stage, connector, voltage, polarity, current limit, travel positions, and connection state unknown. | disputed |
| Valve timer allocation | Timer4 is reported used for ISR-generated valve-servo pulses. [HW-059](facts/HW-059.md) | Channels, pins, frequency, pulse limits, interrupt load, and exact endpoints unknown. | disputed |
| Valve connector structures | J9 `VALVE 10 - Mash Return` and J10 `VALVE 11 - Boil Inlet`, each three positions. [HW-066](facts/HW-066.md) [HW-067](facts/HW-067.md) | Voltage, pin functions, valve identity, physical location, and pin-to-net mapping unknown. | disputed |
| Cooling-inlet solenoid | PA2/pin 76 dedicated-output candidate. [HW-046](facts/HW-046.md) | Solenoid identity, drive stage, connector, voltage, polarity, current limit, and safe limits unknown. | disputed |
| Brew-inlet solenoid | PA1/pin 77 dedicated-output candidate. [HW-047](facts/HW-047.md) | Solenoid identity, drive stage, connector, voltage, polarity, current limit, and safe limits unknown. | disputed |
| Fan | PA0/pin 78 enable candidate. [HW-048](facts/HW-048.md) | Fan identity, drive stage, connector, voltage, polarity, current limit, speed control/feedback, and safe limits unknown. | disputed |

## Electrical monitoring

| Endpoint | MCU endpoint and interface fact | Relevant limits | Status |
| --- | --- | --- | --- |
| Mash-side current sense | PK6/pin 83 ADC candidate. [HW-049](facts/HW-049.md) | Topology, voltage range, ADC reference, scaling, accuracy, bandwidth, and safe limits unknown. | disputed |
| Boil-side current sense | PK5/pin 84 ADC candidate. [HW-050](facts/HW-050.md) | Topology, voltage range, ADC reference, scaling, accuracy, bandwidth, and safe limits unknown. | disputed |
| Hop-valves current sense | PK4/pin 85 ADC candidate. [HW-051](facts/HW-051.md) | Topology, voltage range, ADC reference, scaling, accuracy, bandwidth, and safe limits unknown. | disputed |
| Cooling-inlet current sense | PK3/pin 86 ADC candidate. [HW-052](facts/HW-052.md) | Topology, voltage range, ADC reference, scaling, accuracy, bandwidth, and safe limits unknown; uncharacterized counts are not limits. | disputed |
| Brew-inlet current sense | PK2/pin 87 ADC candidate. [HW-053](facts/HW-053.md) | Topology, voltage range, ADC reference, scaling, accuracy, bandwidth, and safe limits unknown; uncharacterized counts are not limits. | disputed |
| AC measure | PK0/pin 89 ADC candidate. [HW-055](facts/HW-055.md) | Physical quantity, topology, isolation, voltage range, reference, scaling, accuracy, bandwidth, and safety limits unknown. | disputed |

## Audio/sounder current state

| Endpoint | Hardware fact | Relevant limits | Status |
| --- | --- | --- | --- |
| Carrier sounder path | Historical PCB tracing indicates an amplifier-driven sounder, SOM `HPOUTL`/`HPCOM` inputs, +5 V amplifier supply, and 10 kΩ standby pull-down. [HW-068](facts/HW-068.md) [HW-069](facts/HW-069.md) [HW-070](facts/HW-070.md) [HW-081](facts/HW-081.md) | Exact part, pins, load, levels, impedance, power, pull-down endpoint, and circuit condition unknown. | disputed historical candidates |
| Fitted amplifier position | Audio-amplifier IC position is absent/unpopulated on the fitted carrier. [HW-071](facts/HW-071.md) | The exact removed part, pad/trace condition, surrounding population, current sounder connection, and behavior are not established. | verified present physical state |
| Legacy buzzer alias | A13 PB2 was a legacy buzzer-output alias, conflicting with the reported current PB2 PWM assignment. [HW-079](facts/HW-079.md) [HW-072](facts/HW-072.md) | Current physical routing and consumer are unknown. | disputed |

The owner removed buzzer/audio availability from this milestone's required baseline; the verified unpopulated state and all disputed historical candidates remain visible without becoming product requirements. [HW-071](facts/HW-071.md) [HW-068](facts/HW-068.md)
