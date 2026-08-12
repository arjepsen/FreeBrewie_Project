# MCU hardware summary

This is a status-preserving view of indexed hardware fact records, not independent evidence. A disputed mapping remains a candidate and must not be used as a baseline conclusion.

## Verified identity and memory

| Area | Record-backed statement | Status |
| --- | --- | --- |
| Fitted MCU | U1 is marked `Atmel`, `ATMEGA2560`, `16U-TW`, `355E3F`, `1813U7G`; only the explicit model-name line is interpreted, and no MCU-board revision is established. [HW-002](facts/HW-002.md) | verified |
| Flash | The marked ATmega2560 model has 256 KiB nominal flash; usable layout remains unresolved. [HW-003](facts/HW-003.md) | verified |
| SRAM | The marked ATmega2560 model has 8 KiB nominal SRAM; runtime availability remains unresolved. [HW-015](facts/HW-015.md) | verified |
| EEPROM | The marked ATmega2560 model has 4 KiB nominal EEPROM; contents, wear, protection, ownership, and layout remain unresolved. [HW-016](facts/HW-016.md) | verified |
| Clock | The fitted marking record deliberately leaves `16U-TW` uninterpreted and establishes no clock source, frequency, tolerance, fuse, or prescaler state. [HW-002](facts/HW-002.md) | unresolved |

## Peripheral-resource view

| Resource | Indexed evidence and limit | Status |
| --- | --- | --- |
| GPIO | Many endpoint-to-port mappings are indexed, but all machine-specific mappings, directions where unstated, levels, polarities, and safe limits remain disputed. [HW-019](facts/HW-019.md) [HW-020](facts/HW-020.md) [HW-027](facts/HW-027.md) [HW-028](facts/HW-028.md) | disputed |
| ADC | PK6 through PK0 are candidate ADC endpoints for five current/measurement channels, board temperature, and AC measure; PF2/PF1 are ADC-capable GPIO candidates used as LEDs. ADC resolution, reference, scaling, accuracy, bandwidth, and safe limits are not established. [HW-049](facts/HW-049.md) [HW-050](facts/HW-050.md) [HW-051](facts/HW-051.md) [HW-052](facts/HW-052.md) [HW-053](facts/HW-053.md) [HW-054](facts/HW-054.md) [HW-055](facts/HW-055.md) [HW-057](facts/HW-057.md) [HW-058](facts/HW-058.md) | disputed; numeric ADC limits unresolved |
| Timers | Timer4 is reported allocated to valve-servo pulses and Timer3 to a pump-diagnostics tick. Channels, pins, frequencies, pulse limits, interrupt load, and exact consumers are unknown. [HW-059](facts/HW-059.md) [HW-060](facts/HW-060.md) | disputed |
| PWM/timer output | PG5 is a GPIO/timer-output heater candidate, but its timer channel and electrical constraints are not established. [HW-019](facts/HW-019.md) | disputed |
| Interrupt-capable pins | PE4 and PE5 are interrupt-capable GPIO candidates for the two pump tachometers; direction, voltage, pull-up, polarity, and pulse relationship are unknown. [HW-021](facts/HW-021.md) [HW-022](facts/HW-022.md) | disputed |
| SPI-like pump-DAC lines | PB1/SCK clock, PB2/MOSI data, PB4 chip select, and PH6 LDAC are candidate lines; PB3/MISO is classified N/C but physical disconnection is not established. Direction where unstated, DAC identity, logic level, mode/rate, polarity, and limits are unknown. [HW-086](facts/HW-086.md) [HW-087](facts/HW-087.md) [HW-088](facts/HW-088.md) [HW-023](facts/HW-023.md) [HW-073](facts/HW-073.md) | disputed |
| I2C-like mass endpoint | PD0/SCL and PD1/SDA are candidates for the boil-mass endpoint. Device identity, address, pull-ups, voltage, direction, calibration, quantity, and limits are unknown. [HW-024](facts/HW-024.md) [HW-089](facts/HW-089.md) | disputed |
| Prepared mass endpoint | PD4/SCL and PD5/SDA are prepared mash-mass candidates, but actual interface semantics are not established and the device was reported absent. [HW-025](facts/HW-025.md) [HW-090](facts/HW-090.md) [HW-026](facts/HW-026.md) | disputed |
| 1-Wire candidates | PG0 and PG1 are mash- and boil-temperature 1-Wire candidates. Sensor identity, pull-up, voltage, addressing, accuracy, range, and update rate are unknown. [HW-029](facts/HW-029.md) [HW-030](facts/HW-030.md) | disputed |
| SOM serial/reset | A SOM-MCU UART is a physical candidate with separate `/dev/ttyS1` traffic observation; SOM PE9/`gpio137` is a reset candidate with a separate reset observation. Endpoint pins, routing, levels, and complete reset behavior are unresolved. [HW-004](facts/HW-004.md) [HW-017](facts/HW-017.md) [HW-005](facts/HW-005.md) [HW-018](facts/HW-018.md) | disputed |
| Watchdog | The reset records do not establish MCU or external watchdog hardware, configuration, timeout, or reset path. [HW-005](facts/HW-005.md) [HW-018](facts/HW-018.md) | unresolved |

## Candidate pin-resource allocations

Every allocation in this table is disputed.

| Pins | Candidate allocation | Status and record |
| --- | --- | --- |
| PB5 / pin 24 | `PRE_CHARGE`; destination and polarity unknown. | disputed — [HW-011](facts/HW-011.md) |
| PB6 / pin 25 | `PWR_EN_5V`; destination and polarity unknown. | disputed — [HW-012](facts/HW-012.md) |
| PB7 / pin 26 | `PWR_EN_6V5_SERVO`; destination and polarity unknown. | disputed — [HW-013](facts/HW-013.md) |
| PH7 / pin 27 | `PWR_EN_12V`; destination and polarity unknown. | disputed — [HW-014](facts/HW-014.md) |
| PG5 / pin 1; PE2 / pin 4 | Mash-heater-2 and boil-heater-1 control candidates; current-code active-output observations are separate and also disputed. | disputed — [HW-019](facts/HW-019.md) [HW-020](facts/HW-020.md) [HW-084](facts/HW-084.md) [HW-085](facts/HW-085.md) |
| PE4 / pin 6; PE5 / pin 7 | Boil- and mash-pump tachometer candidates. | disputed — [HW-021](facts/HW-021.md) [HW-022](facts/HW-022.md) |
| PB1 / pin 20; PB2 / pin 21; PB4 / pin 23; PH6 / pin 18 | Pump-DAC clock, data, chip-select, and LDAC candidates. | disputed — [HW-086](facts/HW-086.md) [HW-087](facts/HW-087.md) [HW-088](facts/HW-088.md) [HW-023](facts/HW-023.md) |
| PB3 / pin 22 | Pump-DAC MISO row classified N/C, with physical connection unresolved. | disputed — [HW-073](facts/HW-073.md) |
| PD0 / pin 43; PD1 / pin 44 | Boil-mass SCL/SDA candidates. | disputed — [HW-024](facts/HW-024.md) [HW-089](facts/HW-089.md) |
| PD2 / pin 45; PD7 / pin 50 | Drain- and power-button candidates. | disputed — [HW-027](facts/HW-027.md) [HW-028](facts/HW-028.md) |
| PD4 / pin 47; PD5 / pin 48 | Prepared mash-mass SCL/SDA candidates; device reported absent. | disputed — [HW-025](facts/HW-025.md) [HW-090](facts/HW-090.md) [HW-026](facts/HW-026.md) |
| PG0 / pin 51; PG1 / pin 52 | Mash- and boil-temperature 1-Wire candidates. | disputed — [HW-029](facts/HW-029.md) [HW-030](facts/HW-030.md) |
| PC1 / pin 54 | Boil-inlet-valve candidate. | disputed — [HW-031](facts/HW-031.md) |
| PC3 / pin 56; PC5 / pin 58 | Mash- and boil-pump enable candidates. | disputed — [HW-032](facts/HW-032.md) [HW-033](facts/HW-033.md) |
| PC7 / pin 60; PL5 / pin 40; PF2 / pin 95; PF1 / pin 96 | Drain-button LED, current power LED, MCU LED1, and MCU LED2 candidates. | disputed — [HW-034](facts/HW-034.md) [HW-056](facts/HW-056.md) [HW-057](facts/HW-057.md) [HW-058](facts/HW-058.md) |
| PJ2 / pin 65; PJ3 / pin 66; PJ4 / pin 67; PJ5 / pin 68; PJ6 / pin 69 | Mash-inlet, boil-return, prepared valve 5, outlet, and cooling-valve candidates; valve 5 is separately reported absent. | disputed — [HW-035](facts/HW-035.md) [HW-036](facts/HW-036.md) [HW-037](facts/HW-037.md) [HW-038](facts/HW-038.md) [HW-039](facts/HW-039.md) [HW-040](facts/HW-040.md) |
| PA7 / pin 71; PA6 / pin 72; PA5 / pin 73; PA4 / pin 74; PA3 / pin 75 | Hop 2, mash-return, hop 4, hop 1, and hop 3 valve candidates. | disputed — [HW-041](facts/HW-041.md) [HW-042](facts/HW-042.md) [HW-043](facts/HW-043.md) [HW-044](facts/HW-044.md) [HW-045](facts/HW-045.md) |
| PA2 / pin 76; PA1 / pin 77; PA0 / pin 78 | Cooling-inlet solenoid, brew-inlet solenoid, and fan-enable candidates. | disputed — [HW-046](facts/HW-046.md) [HW-047](facts/HW-047.md) [HW-048](facts/HW-048.md) |
| PK6 / pin 83 through PK0 / pin 89 | Mash-side, boil-side, hop-valves, cooling-inlet, and brew-inlet current sense; MCU-board temperature; AC measure. | disputed — [HW-049](facts/HW-049.md) [HW-050](facts/HW-050.md) [HW-051](facts/HW-051.md) [HW-052](facts/HW-052.md) [HW-053](facts/HW-053.md) [HW-054](facts/HW-054.md) [HW-055](facts/HW-055.md) |
| PF3 / pin 94 | Classified N/C and separately described as no longer the active power-LED pin; neither statement proves absence of a physical trace. | disputed — [HW-074](facts/HW-074.md) [HW-091](facts/HW-091.md) |

## Unresolved resource questions

- Board revision, clock source/frequency/fuses, bootloader, programming state, protected flash layout, runtime SRAM budget, EEPROM contents/wear/layout, and applicable errata are not established by the fitted-marking and capacity records. [HW-002](facts/HW-002.md) [HW-003](facts/HW-003.md) [HW-015](facts/HW-015.md) [HW-016](facts/HW-016.md)
- The indexed allocation observations do not establish complete timer/PWM channel availability, ADC resolution/reference, interrupt load, bus electrical limits, or watchdog resources. [HW-019](facts/HW-019.md) [HW-021](facts/HW-021.md) [HW-049](facts/HW-049.md) [HW-059](facts/HW-059.md) [HW-060](facts/HW-060.md)
- The structurally observed connectors J11 `MASS`, J7 `TEMP`, J8 `PUMP`, J1/J18 `Heat2`, J9 `VALVE 10 - Mash Return`, and J10 `VALVE 11 - Boil Inlet` do not establish pin-to-net connectivity or physical connector locations. [HW-061](facts/HW-061.md) [HW-062](facts/HW-062.md) [HW-063](facts/HW-063.md) [HW-064](facts/HW-064.md) [HW-065](facts/HW-065.md) [HW-066](facts/HW-066.md) [HW-067](facts/HW-067.md)

This summary defines no firmware, protocol, control policy, or brewing behavior.
