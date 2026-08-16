# Air Diverter Valve — Servo Pinch Valve on the Irrigation ESP32

Live since **2026-08-16**. One DS3225 servo turns a single symmetric cam that serves both
pinch stations, routing the VIVOHOME VH181 air pump (950 GPH ≈ 60 L/min, ~2 PSI) to the feed
reservoir, the flush reservoir, or both.

Mechanism and CAD are documented separately — this file covers **wiring, firmware, Home
Assistant integration, and the bench procedure**.

---

## Wiring — three wires, and the ground is not optional

| DS3225 lead | Connects to |
|---|---|
| Signal | **GPIO33** on the ESP32 |
| V+ | XL4016 buck **+6.0 V** — never the ESP 5V/3V3 rail |
| GND | Buck GND **and** ESP32 GND |

> **⚠ The common ground is mandatory.** PWM is a voltage referenced to ground. With the servo
> on its own supply, the buck's return must still be bonded to the ESP32's or the servo sees a
> floating signal — it sits dead or jitters at random, and it presents *identically* to a wrong
> pin or bad firmware. Check this first if the servo misbehaves on initial power-up.
>
> The firmware comment used to read *"only this signal wire lands on the ESP32"*, which
> describes a servo that does not work. Corrected 2026-08-16.

Put the **2200 µF** across the buck output, physically close to the servo, to absorb the
inrush when the cam starts moving. The DS3225's stall current is amps — far beyond what the
ESP board's regulator can source, which is why it never shares the ESP rail.

**GPIO5 is free.** It carried the second servo in the retired two-servo design. It is a
strapping pin, so choose it last if something else ever needs a pin here.

---

## The three states

The cam has exactly three positions, and they are **mutually exclusive by construction** —
"both pinched" is not a reachable geometry, so the pump can never be dead-headed. That is a
property of the mechanism, not of the config, so nothing in software guards against it.

| Option | Cam φ | Servo level | Effect |
|---|---|---|---|
| `Both Open` | 0° | 0% | Both hoses open — **boot and idle default** |
| `Feed Air Blocked` | +80° | +88.9% | Feed hose pinched → all air reaches **flush** |
| `Flush Air Blocked` | −80° | −88.9% | Flush hose pinched → all air reaches **feed** |

**Options are named for which hose is PINCHED, not for where the air goes.** This is
deliberate. The earlier destination-style naming (`Air to Feed`) inverted the name against the
cam sign, and the two got swapped in the config at least once. With pinch-centric names, the
name and the cam spec read in the same direction and there is nothing left to invert.

**Levels are percent, not degrees.** `min_level`/`max_level` of 2.5%/12.5% map to 500–2500 µs
= 0–180°, so level 0% is the servo's 90° mid-travel and `level% = (cam φ / 90) × 100`. Both
±80° positions sit inside the cam's verified pinch dwell (flat from φ 78 to φ 90), so
positioning error anywhere in that band changes the hose gap by nothing.

---

## Entities

Device: `tent-irrigation-controller`

| Entity | Purpose |
|---|---|
| `select.air_route_irrigation_tent` | The route. Three options above. |
| `number.air_servo_level_irrigation_tent` | Direct level −100…100%, 0.1% step. Bench only. |
| `button.air_servo_detach_irrigation_tent` | Go limp so the cam can be turned by hand. |
| `switch.air_servo_calibrate_irrigation_tent` | Suspends the re-assert interval. `ALWAYS_OFF`. |

The last three are `entity_category: config`, so they stay off the tent dashboard.

> **Entity-ID note:** these were created with a *doubled* area prefix
> (`select.tent_tent_irrigation_controller_air_route`) and renamed by hand to match this
> device's `<name>_irrigation_tent` convention. Expect to redo that after any reflash that
> adds entities.

---

## Firmware behaviour worth knowing

**Boot drives the cam, and that line is load-bearing.** `on_boot` at priority −100 issues
`select.set: "Both Open"`. This is *not* redundant with `initial_option`: ESPHome's template
select publishes the initial option without ever calling `control()`, so `set_action` never
runs and the servo never moves. Without the explicit boot action the ESP would come up
*reporting* Both Open with the cam wherever it was left — the same optimistic-state lie that
caused the 2026-07-06 valve incident. Priority −100 is also the only choice: it is the sole
`on_boot` priority that runs after every component's `setup()`.

**The route is re-asserted every 5 minutes** (`air_reassert_interval`). The servo runs off its
own buck and auto-detaches 1.5 s after arriving, so a brown-out on the 6 V rail can shift the
cam with the ESP none the wiser — and nothing on this valve gives position feedback. Re-issuing
the same option genuinely re-fires `set_action`, so this is a real write, not a no-op.

Trade-off: each re-assert re-attaches the servo for 1.5 s, so it chirps and pulls buck current
on that cadence, indefinitely, including at idle. Raise the interval if that annoys — but do
not remove it, since it is the only thing making the published state self-healing.

**Both dwells are true arcs**, so the hose reaction passes through the cam axis and exerts no
back-driving moment. Holding either state therefore costs zero current and zero torque, which
is why auto-detach is safe. There is no max-on watchdog like the fluid valves — air has no
flood risk.

---

## Home Assistant integration

`script.tent_air_burst` commands the select directly. There is **no HA-side mirror** of the
route: a second copy would diverge from the device the first time the ESP rebooted to Both
Open, with nothing to reconcile them. The device is the single source of truth.

**The mapping is crossed** — routing air *to* a tank means blocking the *other* hose:

| `tank` | Commanded option |
|---|---|
| `feed` | `Flush Air Blocked` |
| `flush` | `Feed Air Blocked` |

It is written as `if`/`elif` rather than a two-way ternary on purpose. A ternary sends any
unexpected `tank` down the else branch and silently aerates the wrong reservoir; the spelled-out
form emits an invalid option, so `select.select_option` raises and the script aborts **before
the pump is energised**.

**If the ESP is offline** the select call fails and the script aborts at that point, before the
pump. This is intended: with the cam position unknown, do not run the pump. Being offline is
separately alerted by `watchdog_irrigation_critical_offline`. The pump-off step runs *before*
the reset-to-Both-Open step, so an ESP that drops mid-burst still leaves the pump off, and the
`on_boot` action recovers the cam when it returns.

### Level-freeze interaction

The reservoir level sensors freeze a *falling* reading while the tank is being agitated, since
splash bounces the floats. The agitation test is **inverted** — a tank is churned unless its
own hose is pinched:

```jinja
{% set air_here = air and not is_state('select.air_route_irrigation_tent', 'Feed Air Blocked') %}
```

Testing "routed here" instead would be wrong in the idle `Both Open` state, where the pump
feeds **both** tanks: the freeze would release while the tank was still being churned and the
float ladder would false-trip — precisely the failure the hysteresis exists to prevent.

Verified truth table:

| Select state | Feed churned | Flush churned |
|---|---|---|
| `Both Open` | yes | yes |
| `Feed Air Blocked` | no | yes |
| `Flush Air Blocked` | yes | no |
| unavailable | yes | yes (fail-safe: freeze rather than believe) |

---

## Bench procedure — indexing the horn

The cam must sit at φ 0 (both hoses open) when the servo is at level 0%.

1. Turn **`switch.air_servo_calibrate_irrigation_tent` ON** and turn
   **`automation.tent_irrigation_air_alternation` OFF** — see the warning below.
2. Drive `number.air_servo_level_irrigation_tent` to **0**.
3. Press `button.air_servo_detach_irrigation_tent`. The servo goes limp.
4. Reseat the horn on the spline tooth that lands the cam on its low dwell. The DS3225 has a
   25T spline, so one tooth is 14.4° — that is the real indexing quantum. The number's 0.1%
   step is 0.09° of cam, far finer, so use it to confirm rather than to compensate.
5. Sweep to **±88.9%** and confirm each pinch is full and the other hose is clear.
6. Restore: **Calibrate → off first, then the automation → on.**

±100% on the number is safe — it maps to exactly the 500/2500 µs limits and stays on the flat
pinch dwell, so there is no over-travel risk anywhere in the slider's range.

> **⚠ Calibrate does NOT block Home Assistant.** The switch only suspends the ESP's own
> re-assert interval. Home Assistant can still command a route, so the alternation automation
> must be turned off separately or the cam will swing mid-calibration. This is a known gap.

Because auto-detach stays active during calibration, writing a pinch level and watching it
**hold de-energized** is a direct bench test of the over-center claim the whole zero-torque
design rests on. Falsify it here, before it matters.
