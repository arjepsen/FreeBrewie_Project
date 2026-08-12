# SOM-MCU interconnect map

This map reports only indexed physical candidates and observations. It does not define or imply a communication protocol.

| Function | SOM endpoint | MCU endpoint | Interface and direction | Electrical level | Reset/enable/interrupt detail | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Candidate data link | Linux `/dev/ttyS1`; physical SOM UART instance/pins and carrier connector unknown. | ATmega2560 UART pins and carrier connector unknown. | Physical UART candidate; bidirectional traffic is a separate software-visible observation. [HW-004](facts/HW-004.md) [HW-017](facts/HW-017.md) | Unknown. | No enable or interrupt line is established by these records. | disputed |
| Candidate MCU reset | A13 PE9 candidate; current Linux observation names `gpio137`. | ATmega2560 reset input candidate; package/connector path and intervening components unknown. | SOM toward MCU reset; a high-then-low drive was separately reported to reset the MCU. [HW-005](facts/HW-005.md) [HW-018](facts/HW-018.md) | Thresholds and carrier levels unknown. | Pulse duration, asserted polarity beyond the reported sequence, and complete trace are unknown. | disputed |
| Power/enable relationship | No SOM endpoint or SOM-MCU route is established. | PB5 `PRE_CHARGE`, PB6 `PWR_EN_5V`, PB7 `PWR_EN_6V5_SERVO`, and PH7 `PWR_EN_12V` are MCU endpoint candidates only. [HW-011](facts/HW-011.md) [HW-012](facts/HW-012.md) [HW-013](facts/HW-013.md) [HW-014](facts/HW-014.md) | Destination circuitry and direction are not established. | Unknown. | These records do not establish SOM-controlled enable lines or interrupt lines. | disputed candidates; SOM-MCU relationship unresolved |

No indexed record verifies an interrupt line between the SOM and MCU, an interconnect watchdog, physical connector positions, complete endpoint pins for the UART, or signal voltage levels. The candidate records above therefore block consequential electrical-interface, automated-reset, or hard-coded endpoint decisions. [HW-004](facts/HW-004.md) [HW-005](facts/HW-005.md) [HW-017](facts/HW-017.md) [HW-018](facts/HW-018.md)

No baud rate, framing, message format, command set, retry behavior, recovery policy, or ownership model is specified here.
