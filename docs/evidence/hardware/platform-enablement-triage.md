# Platform-enablement evidence triage

## Purpose and boundary

This registry classifies disputed hardware evidence by its effect on clean-slate
Linux platform enablement. It schedules verification and records safe defaults;
it does not select or implement a Linux image, firmware, protocol, UI, brewing
logic, or hardware-control design. Historical implementation choices remain
observations and do not become requirements or design inputs.

The atomic records in `facts/` remain canonical for claims, evidence,
confidence, and verification status. A row in this registry does not promote or
otherwise change a fact's status.

## Dispositions

- `platform blocker`: verification is required before requirements work or
  first powered bring-up because isolation cannot permit safe progress.
- `platform constraint`: requirements work may proceed, but the unresolved
  interface or capability must remain disabled, isolated, preserved, or
  untouched.
- `integration dependency`: verification is required for a named later
  integration, not for minimal platform enablement.
- `brewing-device dependency`: verification is deferred to hardware-control or
  brewing-device work.
- `non-blocking reference`: useful evidence that controls no currently planned
  decision.
- `candidate removal`: proposed removal from required scope, pending explicit
  owner approval with a reason and date.

## Deadlines

- `before requirements`: resolve before Linux-image requirements are activated.
- `before first powered bring-up`: resolve before the first powered Linux test.
- `before named integration`: resolve before the named later integration.
- `deferred`: no current activation deadline; retain the recorded safe default.

## Material disputed-fact dispositions

| ID | Claim | Disposition | Decision or later milestone | Wrong-claim consequence | Safe default | Deadline | Why isolation cannot permit progress | Cheapest reliable check | Evidence/confidence/status | Owner approval |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HW-004 | [HW-004](facts/HW-004.md) — The SOM and ATmega2560 have a candidate physical UART connection. | platform constraint | first powered Linux bring-up | Enabling a candidate serial route could drive the MCU through unverified pins or electrical levels. | Do not configure or drive the candidate serial link. | before first powered bring-up | Isolation permits progress if candidate UART pins remain unconfigured. | Trace the carrier UART nets to both endpoints and identify their electrical levels. | inferred / medium / disputed | Not applicable |
| HW-005 | [HW-005](facts/HW-005.md) — A13 PE9 is the SOM-controlled MCU reset candidate. | platform constraint | first powered Linux bring-up | Configuring PE9 could reset or otherwise disturb the MCU through an unverified route. | Leave PE9 unconfigured and do not rely on SOM-controlled MCU reset. | before first powered bring-up | Isolation permits progress if PE9 remains unconfigured. | Trace PE9 through the carrier to the fitted MCU reset input. | direct / medium / disputed | Not applicable |
| HW-006 | [HW-006](facts/HW-006.md) — Linux DRM has been observed using a 480 by 272 RGB565 scanout mode. | integration dependency | display/touch integration | Treating the runtime observation as panel evidence could select incompatible timing or bus configuration. | Do not rely on this mode as physical-panel or bus proof. | before named integration | Display output can remain unconfigured during minimal platform work. | Capture current DRM state and separately identify the panel and physical bus. | direct / medium / disputed | Not applicable |
| HW-009 | [HW-009](facts/HW-009.md) — The legacy LCD backlight-control candidate maps to A13 PB3. | platform constraint | first powered Linux bring-up | Driving PB3 could affect an unverified backlight circuit with unverified polarity. | Leave PB3 unconfigured and do not automate backlight control. | before first powered bring-up | Isolation permits progress with backlight control disabled. | Trace PB3 to the backlight circuit and establish pinmux ownership and levels. | inferred / low / disputed | Not applicable |
| HW-010 | [HW-010](facts/HW-010.md) — The legacy LCD power-enable candidate maps to A13 PB10. | platform constraint | first powered Linux bring-up | Driving PB10 could switch an unverified display power domain with unverified polarity. | Leave PB10 unconfigured and do not switch display power. | before first powered bring-up | Isolation permits progress with display power control disabled. | Trace PB10 to the display power circuit and establish pinmux ownership and levels. | inferred / low / disputed | Not applicable |
| HW-011 | [HW-011](facts/HW-011.md) — MCU PRE_CHARGE is a candidate mapping to ATmega2560 PB5, package pin 24. | brewing-device dependency | hardware-control integration | Incorrect mapping or polarity could invalidate later power-domain control. | Do not alter MCU firmware or activate PRE_CHARGE from this mapping. | deferred | MCU-controlled power behavior is outside minimal Linux enablement. | Generate the exact-schematic netlist, trace PB5, then separately approve any level observation. | inferred / medium / disputed | Not applicable |
| HW-012 | [HW-012](facts/HW-012.md) — MCU PWR_EN_5V is a candidate mapping to ATmega2560 PB6, package pin 25. | brewing-device dependency | hardware-control integration | Incorrect mapping or polarity could invalidate later 5 V power-domain control. | Do not alter MCU firmware or activate PWR_EN_5V from this mapping. | deferred | MCU-controlled power behavior is outside minimal Linux enablement. | Generate the exact-schematic netlist, trace PB6, then separately approve any level observation. | inferred / medium / disputed | Not applicable |
| HW-013 | [HW-013](facts/HW-013.md) — MCU PWR_EN_6V5_SERVO is a candidate mapping to ATmega2560 PB7, package pin 26. | brewing-device dependency | hardware-control integration | Incorrect mapping or polarity could invalidate later servo-domain control. | Do not alter MCU firmware or activate PWR_EN_6V5_SERVO from this mapping. | deferred | MCU-controlled power behavior is outside minimal Linux enablement. | Generate the exact-schematic netlist, trace PB7, then separately approve any level observation. | inferred / medium / disputed | Not applicable |
| HW-014 | [HW-014](facts/HW-014.md) — MCU PWR_EN_12V is a candidate mapping to ATmega2560 PH7, package pin 27. | brewing-device dependency | hardware-control integration | Incorrect mapping or polarity could invalidate later 12 V power-domain control. | Do not alter MCU firmware or activate PWR_EN_12V from this mapping. | deferred | MCU-controlled power behavior is outside minimal Linux enablement. | Generate the exact-schematic netlist, trace PH7, then separately approve any level observation. | inferred / medium / disputed | Not applicable |
| HW-017 | [HW-017](facts/HW-017.md) — Bidirectional SOM-to-MCU traffic has been observed through `/dev/ttyS1`. | platform constraint | first powered Linux bring-up | Binding or transmitting on this endpoint could interact with the MCU through an unverified physical route. | Do not bind or transmit on `/dev/ttyS1` as the SOM-MCU link. | before first powered bring-up | Isolation permits progress without SOM-MCU traffic. | Observe both directions independently while correlating `/dev/ttyS1` traffic. | direct / medium / disputed | Not applicable |
| HW-018 | [HW-018](facts/HW-018.md) — A brief gpio137 high-then-low operation was observed to reset the ATmega2560. | platform constraint | first powered Linux bring-up | Exporting or driving gpio137 could interrupt the MCU with an unsuitable pulse or route. | Do not export, drive, or automate gpio137 for MCU reset. | before first powered bring-up | Isolation permits progress while the candidate reset control remains untouched. | Separately approve and repeat the operation while observing waveform and MCU reset indication. | direct / medium / disputed | Not applicable |
| HW-072 | [HW-072](facts/HW-072.md) — Current kernel pin control shows A13 PB2 assigned to `1c20e00.pwm`. | platform constraint | first powered Linux bring-up | Reassigning PB2 could conflict with an existing consumer or affect unverified carrier circuitry. | Preserve the current PB2 assignment and do not drive or remux it. | before first powered bring-up | Isolation permits progress while PB2 remains untouched. | Capture immutable kernel and device-tree identity and repeat read-only pinctrl inspection. | direct / medium / disputed | Not applicable |
| HW-075 | [HW-075](facts/HW-075.md) — Legacy notes map a drain-or-second-button endpoint to A13 PB15. | integration dependency | hardware-control integration | Treating the ambiguous mapping as settled could bind the wrong input or electrical assumptions. | Leave PB15 unconfigured and do not assign a button function. | before named integration | Minimal platform work does not require this button input. | Trace PB15 to the physical control and capture levels only after separate approval. | inferred / medium / disputed | Not applicable |
| HW-076 | [HW-076](facts/HW-076.md) — Legacy notes map a hold-power output endpoint to A13 PB4. | platform constraint | first powered Linux bring-up | Driving PB4 could affect unverified power-hold circuitry or shut down a power domain. | Leave PB4 unconfigured and do not depend on software power hold. | before first powered bring-up | Isolation permits progress if PB4 remains untouched and power hold is not assumed. | Identify the carrier revision and trace PB4 to its destination with power removed. | inferred / medium / disputed | Not applicable |
| HW-077 | [HW-077](facts/HW-077.md) — Legacy notes map a second-LED output endpoint to A13 PB16. | integration dependency | hardware-control integration | Driving the candidate mapping could affect a different circuit or exceed its electrical limits. | Leave PB16 unconfigured and do not drive a second indicator. | before named integration | Minimal platform work does not require this indicator. | Identify the carrier revision and trace PB16 through the indicator circuit with power removed. | inferred / medium / disputed | Not applicable |
| HW-078 | [HW-078](facts/HW-078.md) — Legacy notes map an unspecified power-related endpoint to A13 PC7. | platform constraint | first powered Linux bring-up | Configuring PC7 could affect an unidentified power-related circuit. | Leave PC7 unconfigured and make no power-control assumption from the legacy endpoint. | before first powered bring-up | Isolation permits progress if PC7 remains untouched. | Identify the carrier revision and trace PC7 to its endpoint with power removed. | inferred / medium / disputed | Not applicable |
| HW-080 | [HW-080](facts/HW-080.md) — Current-image notes state that original `/dev/brewie-*` GPIO aliases are not created automatically. | non-blocking reference | Linux-image requirements | Assuming legacy aliases exist would make diagnostics or later integration fail. | Make no requirement depend on legacy `/dev/brewie-*` aliases. | deferred | The absence or presence of aliases does not prevent clean-slate requirements work. | Record immutable image and kernel identity and enumerate only the expected alias paths. | direct / medium / disputed | Not applicable |
| HW-082 | [HW-082](facts/HW-082.md) — Current-image notes identify `pwm-0` as a backlight PWM. | platform constraint | first powered Linux bring-up | Enabling the PWM could drive the wrong consumer, polarity, pin, or voltage. | Preserve `pwm-0` state and do not enable or reconfigure it. | before first powered bring-up | Isolation permits progress with PWM-driven backlight control disabled. | Resolve the consumer against immutable kernel identity and a physically traced endpoint. | direct / medium / disputed | Not applicable |
| HW-083 | [HW-083](facts/HW-083.md) — A legacy numbering rule maps A13 PB2 to Linux gpio34. | non-blocking reference | Linux-image requirements | Treating an inferred legacy number as current could address the wrong GPIO. | Do not use gpio34 as proof of PB2 identity or routing. | deferred | Clean-slate requirements can use controller-and-pin identity without this legacy translation. | Confirm the mapping from authoritative kernel data without changing pin state. | inferred / medium / disputed | Not applicable |
| HW-092 | [HW-092](facts/HW-092.md) — Current-image notes report a 50 microsecond period for `pwm-0`. | integration dependency | display/touch integration | Reusing the observation could select an unsuitable backlight frequency. | Do not configure `pwm-0` from the reported period. | before named integration | Minimal platform work can keep the PWM disabled. | Capture immutable kernel identity and later measure the period under separately approved conditions. | direct / medium / disputed | Not applicable |
| HW-093 | [HW-093](facts/HW-093.md) — Current-image notes report inverse polarity for `pwm-0`. | integration dependency | display/touch integration | Reusing the observation could invert backlight behavior or activate it unexpectedly. | Do not configure `pwm-0` from the reported polarity. | before named integration | Minimal platform work can keep the PWM disabled. | Capture immutable kernel identity and later confirm configured and measured polarity under separate approval. | direct / medium / disputed | Not applicable |

## Platform blockers

None among the compute-platform and SOM-facing facts. Each unresolved interface
has a credible isolation path, so none meets the blocker rule.

## First-bring-up constraints

- Leave PE9, PB3, PB10, PB4, and PC7 unconfigured; do not rely on MCU reset,
  display power, backlight control, or software power hold through those pins.
- Preserve the current PB2 and `pwm-0` assignments and states; do not remux,
  drive, enable, or reconfigure them.
- Do not configure candidate SOM-MCU UART pins, bind or transmit on
  `/dev/ttyS1` as the MCU link, or export or drive gpio137 for MCU reset.
- Do not rely on the graphical display, legacy GPIO aliases, or SOM-MCU
  communication as the diagnostic or recovery path.

## Deferred work

None recorded yet.

## Candidate removals

None recorded yet.

## Owner-removed non-material disputed facts

None recorded yet.

## Gate decision

Pending complete classification and validation.
