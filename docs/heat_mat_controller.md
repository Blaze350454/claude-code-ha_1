# Heat Mat Controller — temperature-controlled heating mats on Home Assistant

**Status: FUTURE PROJECT. Parked 2026-08-23.** Nothing bought, nothing wired, nothing
in `hardware-inventory.md`. This document exists so the next session picks the design up
cold without re-deriving it. Same posture as the plant-scales build: designed, not ordered.

Everything in the parts section is a **PROPOSAL**. Per the standing rule, a part enters
the inventory only when it is installed, working, and the user says so.

---

## The problem

Two heaters on hand, opposite characters, neither with usable temperature control:

- **110 V AC body/recovery mat** — large area, low watt density. Its factory controller
  (a 1/2/3 dial) has **already been cut off the power wires**; it is now a bare element
  with a simple on/off switch. Physically cannot get very hot, and is *good* at gentle heat.
- **Silicone 3D-printer bed mats, 12/24 V DC** — small area, high watt density, will go
  past 120 °C. Bad at gentle, excellent at hot.

Wanted: one HA-controlled system spanning **sourdough starter and seedlings (~25–28 °C)
up to whatever the silicone mat can do**, with two physical setups expected eventually.

## The shaping idea

**Do not force one heater or one sensor to span 25–130 °C.** The two heaters already
tile the range. Build **one controller with two independent channels**, each matched to
what its heater can physically do.

| Channel | Heater | Its job | Switch | Control sensor |
|---|---|---|---|---|
| **A** | 110 V AC body mat | **25–45 °C** — sourdough starter, seedlings, proofing | Zero-cross SSR | DS18B20 ×3 |
| **B** | 12/24 V silicone bed | **40–130 °C** — drying, curing, hot work | MOSFET | 100 k NTC (already owned) |

Same firmware twice. The only per-channel differences are the `output:` block and the
sensor block.

## The control loop lives on the ESP32, not in HA

Non-negotiable. `climate:` → `platform: pid` runs entirely on-device, so a WiFi drop, an
HA restart, or the nightly config pull cannot leave a mat calling for heat with nothing
watching it. HA supplies the setpoint and the UI and nothing else, and gets two
`climate.*` entities for free via the ESPHome native API.

---

## ⚠ Consequence of the factory controller being cut off

**Simpler wiring, and one fewer safety layer.**

- **Simpler:** the SSR gates mains straight to the element. There is no "does the
  controller boot to OFF after every PWM cycle?" problem and nothing to tap in
  downstream of. Channel A is fully unblocked.
- **The cost:** whatever thermal protection lived inside that controller is **gone**.
  The **KSD9700 bimetallic cutoff is now the only hardware overtemp device on channel
  A**, not a backup to a factory one. It moves from "recommended" to **"this channel
  does not get energised without it."**

**Free measurement that closes an open question:** ohm the element's two leads.
`P = 120² / R` gives the mat's real wattage, which sizes the SSR, the fuse and the
KSD9700 trip point. Costs nothing and needs no power applied.

---

## Sensor reasoning

The "little glass ball" is a **glass-bead 100 k NTC thermistor** (3D-printer standard —
Semitec 104GT-2 or a generic 100 k B3950). The instinct to reuse it is **right for
channel B and wrong for channel A**, and the reason is worth keeping.

A thermistor's resolution is set by where its divider sits. With the printer's stock
**4.7 kΩ** pullup, a 100 k B3950 at 25 °C is ~93 kΩ, so the ADC sees
`3.3 × 4.7 / 97.7 = 0.16 V` — buried in the ESP32 ADC's worst nonlinearity region. That
is why it feels imprecise down low: **the part is optimised for 200–300 °C, not 27 °C.**

Changing the pullup moves the useful window, but you cannot have both ends from one divider:

| Pullup | Useful from | Useful to |
|---|---|---|
| 4.7 kΩ (printer stock) | ~80 °C | 300 °C |
| **10 kΩ** | **~35 °C** | **~140 °C** ← use this for channel B |
| 100 kΩ | ~10 °C | ~60 °C |

**Channel B therefore gets a 10 kΩ pullup, not the printer's 4.7 kΩ.** That single
resistor swap makes hardware already on hand cover channel B's whole job, for free.

**Channel A gets DS18B20s** — digital, ±0.5 °C, no divider or ADC calibration anywhere
in the path, three share one GPIO by address, and the pattern already exists in this
build at `tent-irrigation-controller.yaml:261` and `grow-tent-one.yaml:97`. Its 125 °C
ceiling is irrelevant on a mat that tops out near 50 °C.

**Optional upgrade, not required for v1:** if channel B ever needs to be accurate at
*low* temps too (silicone mat proofing dough at 28 °C), a **PT100 + MAX31865** is the one
sensor that is linear and ±0.5 °C across −50 → 300 °C with no divider trade-off. ESPHome
supports it natively. The SPI pins are reserved in the pin map so it drops in later.

---

## Safety

Standing fact from `hardware-inventory.md`, user-confirmed 2026-08-16: **there is no
fuse anywhere in this system.** A heating mat is the one load where that is genuinely
dangerous. This is the build where it changes.

### Layer 0 — hardware. Must work with the ESP32 dead.

**Both switching elements fail SHORTED.** SSRs fail shorted; MOSFETs fail
drain-to-source shorted. No software catches that. Layer 0 is the only answer, which is
why it is not optional and not a phase-2 item.

| Item | Channel | Why |
|---|---|---|
| **KSD9700** NC bimetallic, bonded to the mat, **in series with the mat's power** | Both | The only thing that catches a shorted switch. Self-resetting. ~60 °C on A, ~150 °C on B |
| **One-shot thermal fuse**, higher trip, in series | A | Absolute backstop on the mains channel |
| **Fuse on the DC supply** | B | First fuse in the system |
| **GFCI** on the AC feed | A | Mains, possible damp, possible skin contact |
| **Smart plug upstream of the SSR** | A | Independent HA-controllable mechanical break in a path whose primary element fails shorted. Its power reporting also cross-checks that the SSR is really modulating |

### Layer 1 — firmware. Works with HA and WiFi down.

- **`on_boot: priority: -100`** → both outputs forced to 0, master enable relay OFF,
  both climates to OFF mode. Direct precedent: the 2026-07-06 power blip, where
  optimistic valves published "open" on boot — `tent-irrigation-controller.yaml:58-69`.
- **10 kΩ gate-to-source pulldown on the MOSFET.** The GPIO floats during ESP boot and
  reset, and a floating gate on a part switching 200 W *is* the "heater on at boot"
  failure. The pulldown is what makes `on_boot` true in hardware rather than only in
  firmware.
- **Sensor-failure interlock** on an `interval:`: control sensor NaN, or last publish
  older than 3× `update_interval` → output 0, drop the enable relay, latch fault.
  ⚠ **ESPHome's PID docs do not define NaN behaviour** (verified against esphome.io
  2026-08-23). The output holds its last value — a heater stuck at whatever duty it was
  at when the probe died. **This interlock is ours to write, not inherited.**
- **Absolute over-temp:** `max()` of every probe on the channel above its hard limit →
  latch. Runs independently of the PID.
- **Divergence check:** control sensor vs safety sensor differ by more than ~8 °C →
  latch. Catches the probe that fell off the mat and is reading room air while the PID
  drives to 100 %.
- **Thermal-runaway check** (Marlin's logic): output ≥ 90 % for N minutes with < 2 °C
  rise → latch. Catches a disconnected heater and a probe in the wrong place.
- **Per-channel max-on-time ceiling**, same idea and same `substitutions:` style as
  `valve_max_on_time` at `tent-irrigation-controller.yaml:3`.
- **The fault latch is sticky.** Cleared only by an explicit HA button press — never on
  a timer, never on reboot. An auto-clearing fault re-energises a mat that just overheated.

### Layer 2 — Home Assistant

Two thermostat cards. Diagnostic sensors per probe, duty-cycle %, fault reason, uptime.
An alert on the fault latch reusing the tent alert-banner pattern. Optional schedules —
warm the starter at 06:00. **No control logic here.**

---

## Pin map — node `heat-mat-controller`, `esp32dev` / `esp-idf`

Avoids strapping pins (0, 2, 5, 12, 15) and flash pins (6–11), and **deliberately skips
GPIO16/17** so the design works on a 30-pin devkit as well as a 38-pin — see the ESP32
GPIO gotchas memory note.

| GPIO | Use |
|---|---|
| **4** | 1-Wire bus — DS18B20 ×3 (ch A). 4.7 kΩ pullup to 3V3 on the data line. Matches the irrigation board's convention |
| **25** | `slow_pwm` → ch A SSR, `period: 5s`. A zero-cross SSR can only switch at zero crossings (120/s at 60 Hz), so 5 s still gives ~600 steps |
| **26** | `slow_pwm` → ch B MOSFET gate stage, `period: 2s` |
| **27** | Heater master enable relay, in series with **both** supplies. LOW = off. Second independent break path |
| **34** | ADC — ch B 100 k NTC, **external 10 kΩ pullup to 3V3**. Input-only with no internal pull is *correct* here; the pullup is external by design. Same pattern as the irrigation pressure ADCs |
| **35** | Spare ADC — second thermistor, or ch A cross-check |
| **18 / 19 / 23 / 21** | SPI SCK / MISO / MOSI / CS — reserved for a MAX31865 if PT100 is ever added. Leave unpopulated |

**Static IP `192.168.2.243`** — the next free slot above the DHCP pool
(`.236`, `.240`, `.241`, `.242`, `.248`, `.250` are taken). Pin it in firmware on **both**
network entries; the router refuses DHCP reservations. See `docs/network_addressing.md`,
and note that changing an ESP's IP also requires re-pointing HA by hand.

**Where the config lives:** author at `/root/config/heat-mat-controller.yaml` on LXC 100
(`192.168.2.14`) — that is the copy that gets flashed. The `esphome-config` repo is a
mirror only; committing there reaches no device.

---

## Parts and options — PROPOSED, NOTHING VERIFIED OR BOUGHT

### Temperature sensing

| Option | Part | Range | Notes |
|---|---|---|---|
| **Ch A pick** | **DS18B20**, waterproof stainless probe | −55…125 °C, ±0.5 °C | The probe's **PVC cable is the real limit (~105 °C)**, not the chip. Silicone-cable versions exist. Needs a 4.7 kΩ pullup. Addressable — 3 on one GPIO |
| | DS18B20 bare TO-92 | same | Cheaper; needs its own potting and bonding |
| **Ch B pick** | **100 k NTC**, glass bead or **M3/M4 screw-in cartridge** — Semitec 104GT-2, 104NT-4-R025H42G, or generic 100 k **B3950** | ~35…140 °C **with a 10 kΩ pullup** | Already owned. The screw-in style bolts to a bed cleanly |
| Upgrade | **PT100 + MAX31865** — Adafruit #3328 (430 Ω ref resistor) or a clone | −50…300 °C, ±0.5 °C **across the whole span** | The only sensor linear and accurate at *both* 28 °C and 130 °C. ~C$10–15. Add only if ch B ever needs precise low-temp control |
| Upgrade | PT1000 + MAX31865 — Adafruit #3648 (**4300 Ω** ref) | same | **Match the board to the probe.** A PT100 board needs its reference resistor changed for PT1000 |
| ✗ Rejected | K-type thermocouple + MAX6675 / MAX31855 | | ±2 °C and cold-junction dependent — worse than everything above below 100 °C |

ESPHome platforms, all verified present 2026-08-23: `dallas_temp` (on `one_wire:`),
`adc` → `resistance` → `ntc`, and `max31865` (needs `spi:` with both `miso_pin` and
`mosi_pin`; keys are `cs_pin`, `reference_resistance`, `rtd_nominal_resistance`,
`rtd_wires`, `mains_filter`).

### Switching

| Ch | | Part | Notes |
|---|---|---|---|
| **A** | **Pick** | **Omron G3MB-202P** | 2 A, PCB-mount, zero-cross, **built-in snubber**, ~C$3, **through-hole**. Ample for a body mat at ~0.4–1.25 A |
| A | Bigger | Omron G3NA-210B-DC5, Crydom D2425 | If the element measures higher than expected |
| A | ⚠ **Avoid** | "Fotek" SSR-25DA bricks from AliExpress | Overwhelmingly counterfeit — rated 25 A, good for ~5 A, and **fails shorted**, which is the dangerous direction |
| **B** | **Pick** | **IRFZ44N** + a 12 V gate-drive stage | 17 mΩ fully enhanced. Cheap and everywhere. `slow_pwm` runs at ~1 Hz so switching losses are irrelevant, and a **2N3904 + 2 resistors** (inverting) or an **MCP1407 / TC4420** driver makes MOSFET selection stop being something that can be got wrong |
| B | Simpler | **IRLB8743PbF** | True logic level — Rds(on) specified at Vgs = 4.5 V. Drives straight off the GPIO, one less stage to build |
| B | ⚠ **Trap** | **IRLZ44N** | "Logic level" here means *5 V* gates. **Marginal at 3.3 V**; it runs hot, which is the tell |
| B | Alt | SSR-40DD (DC–DC) | Isolated and hard to get wrong, but fails shorted and needs a heatsink |
| B | Alt | MKS MOSFET / "Heat Bed Power Expansion Module" | Drop-in 25 A, but **check the trigger voltage — many expect 12 V logic, not 3.3 V** |

Gate network either way: **100 Ω** gate resistor, **10 kΩ** gate-to-source pulldown,
TO-220 heatsink and thermal pad. **No flyback diode** — the load is purely resistive.
Low-side switching, so the mat's + stays at supply potential.

### Protection — the mandatory column

| Part | Spec | For |
|---|---|---|
| **KSD9700** NC bimetallic, self-resetting | Sold in 5 °C steps, 40–150 °C, typically 5 A/250 V. **~60 °C for ch A, ~150 °C for ch B** | The only thing that catches a shorted switch. **Ch A does not get energised without it** |
| One-shot thermal fuse | RY series, e.g. 72 °C 10 A/250 V | Absolute backstop on the mains channel |
| Inline fuse holder + fuses | Sized from measured wattage | First fuse in this system |
| Polyfuse, RXEF | Already on hand from the 2026-08-16 climate order | Logic and sensor branches |
| GFCI outlet or plug adapter | | Mains |

### Support

ESP32 WROOM-32 devkit (spares on hand — the `test-esp32` bench board is one) ·
**a separate 24 V PSU** — Mean Well **LRS-350-24** class for a large silicone mat.
⚠ **Do not share the tent's RSP-100-24**; it is committed to the ESP trio and
`switch.controller_tent` is already a common-mode point. · Resistors 4.7 k / 10 k / 100 Ω ·
Capacitors from the BOJACK kits already owned — ⚠ **check the sleeve voltage rating on
anything ≥100 µF before putting it on a 24 V rail**; the kits derate as capacitance rises.

**Sourcing constraint stands:** Amazon.ca or AliExpress only. Recom / Traco / Pololu are
not practically buyable here.

### Sizing reference

- Silicone bed, 200×200 mm at 24 V ≈ **200 W ≈ 8.3 A**; 300×300 mm ≈ 300–400 W.
- Body mat at 120 V, likely **50–150 W ≈ 0.4–1.25 A** — comfortably inside the G3MB-202P.

---

## ❓ Open — needs eyes. None of it blocking today.

1. **Body mat element resistance** → its real wattage. The free ohm measurement above.
2. **Silicone mat(s): 12 V or 24 V?** Size and wattage?
3. **Which spare 3D-printer control boards are actually on hand** (models)? The plan is
   a discrete MOSFET stage rather than reusing one, but the models are worth recording.
4. Whether channel B ever needs precise low-temp control — that is the only thing that
   buys the PT100.

## Build order, when it starts

1. Firmware on the bench with **no heater connected**, outputs to LEDs. Every safety
   latch proven before a mat is in circuit.
2. Channel B wired — MOSFET stage, thermistor at 10 kΩ, KSD9700, DC fuse, real mat.
3. PID autotune (`climate.pid.autotune`) per channel, **in the real use configuration** —
   a mat under a blanket tunes differently from a bare one. Transfer the resulting
   kp/ki/kd into `substitutions:`.
4. Channel A.

## Verification, when it starts — by side effect, never by "done"

Each of these must *actually trip*, observed in HA. A latch that has never fired is a
latch nobody knows exists.

1. **Boot state:** power-cycle with a meter on both gate/SSR inputs. Both read 0 V
   through boot and stay there — this proves the gate pulldown, not just `on_boot`.
2. **Sensor failure:** unplug a DS18B20 mid-run. The channel latches FAULT and drops to
   0 within 3× the update interval. *The most important test in the list* — it covers
   behaviour the PID component does not document.
3. **Divergence:** hold one probe in your hand while the other is on the mat.
4. **Thermal runaway:** disconnect the heater while the channel calls for heat.
5. **Over-temp:** drop the hard limit to just above ambient and let it heat.
6. **Fault stickiness:** reboot the ESP with a fault latched. It must come back faulted.
7. **MOSFET gate check:** run ch B at 100 % into the real mat for 5 min, then read the
   TO-220 case with an IR thermometer. Warm is fine; hot means the gate is not fully
   enhanced — switch to the 12 V gate-drive path.
8. **KSD9700 — test it with the ESP32 completely unplugged.** Wire the mat straight to
   its supply and confirm the bimetallic opens. The entire point of layer 0 is that it
   works when the controller is dead, so that is the only configuration in which the
   test is valid.
9. Only after 1–8: leave it running unattended.

---

Related: `docs/network_addressing.md` (static IPs and the HA re-point trap),
`D:\Claude\Knowledge\grow\hardware-inventory.md` (the no-fuse standing fact, sourcing
constraints, capacitor-kit trap), and the memory notes `project-heat-mat-controller`,
`reference-esp32-gpio-gotchas`, `reference-capacitor-kits-on-hand`.
