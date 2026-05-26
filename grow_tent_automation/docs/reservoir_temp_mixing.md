# Reservoir Water Temperature — Hot/Cold Mixing for Fill Lines

## Context

Both reservoirs (feed + flush, 25 gal each) fill with cold tap water. Drip irrigation runs frequent feedings during lights-on with a fill-to-feed window as short as 1 hour — no time to heat from cold passively. Reservoirs sit in a living room (~70°F ambient) so once filled at the right temp, they hold it naturally. No heaters needed. Solution: inject hot water into the existing cold fill line via a manually-adjusted needle valve, creating pre-mixed fill water at ~65–70°F.

---

## Phase 1 — Manual Plumbing Setup

### How It Works

Hot and cold supply lines (1/2" PEX, kitchen area) are tapped. Hot is injected into the cold line upstream of the existing solenoid valves via a needle valve. Cold runs full-open. Needle valve is set once with a thermometer, re-calibrated twice yearly for seasonal cold water temp shifts.

### Plumbing Diagram

```
Cold PEX → crimp MPT → spring check valve → nipple ──────────────► TEE → existing solenoid setup → reservoirs
                                                                      ▲
Hot PEX  → crimp MPT → spring check valve → nipple → needle valve ───┘
```

### Hardware Shopping List

| Item | Spec | Est. CAD |
|------|------|----------|
| Needle valve | 1/2" NPT F×F, 304 SS, ASIN B07V96MS7V — 915 PSI, 120°C max | ~$60 | **Ordered** |
| Spring check valve | 1/2" NPT inline, brass, spring-loaded (not swing), 1–5 PSI cracking pressure | ~$10 × 2 | **Ordered** |
| All-female tee | 1/2" NPT F×F×F brass | ~$5 | **Ordered** |
| Close nipples | 1/2" NPT M×M, ~4–5 pieces | ~$3 each | **Ordered** |
| PEX crimp barb × MPT | 1/2" barb × 1/2" MPT — user has crimp tool | ~$5 × 2 | **Ordered** |
| **Total** | | **~$100–110 CAD** | |

### Check Valve Spec Notes

- **Must be spring-loaded** (not swing) — works in any orientation
- Brass body, stainless spring/disc preferred
- 1–5 PSI cracking pressure (low restriction)
- 125 PSI+ WOG rating

### Calibration Procedure

1. Run water 45–60 seconds until hot arrives and temp stabilizes (flush into bucket/drain first)
2. Measure mixed output temp with thermometer
3. Adjust needle valve, wait 15 sec, re-measure
4. Repeat until ~68°F (~20°C) target hit (~3–5 adjustments, 10 min total)
5. Mark handle position with paint pen on handle + valve body
6. Re-calibrate twice yearly (when cold tap temp shifts seasonally ~10–20°F)

### Install Notes

- Needle valve on hot side only — cold runs fully open through check valve directly to tee
- Install needle valve with stem accessible/upward — needed for Phase 2 NEMA 17 upgrade
- Both check valves prevent hot/cold backflow into supply mains

### Phase 1 Verification

1. Install plumbing, confirm no leaks at low pressure before full pressure
2. Flush 60 sec into bucket before first use
3. Measure output temp with thermometer — target 65–70°F (18–21°C)
4. Fill reservoir, confirm temp holds at ambient after 1 hour
5. Confirm solenoid valves and existing fill automation still function normally

---

## Phase 2 — NEMA 17 Stepper Upgrade (no timeline set)

Replace manual needle valve adjustment with closed-loop ESP32 control using the existing reservoir temp sensor.

### Additional Hardware

| Item | Spec | Est. CAD |
|------|------|----------|
| NEMA 17 stepper motor | Standard bipolar, ~40mm body | ~$15 |
| A4988 or DRV8825 driver | Pololu-style breakout | ~$5 |
| Flexible shaft coupler | 5mm bore (stepper) × needle valve stem OD | ~$5 |
| Mount bracket | 3D printed or fabricated | ~$0–10 |
| **Total** | | **~$25–35 CAD** |

### ESPHome Config (Phase 2 additions)

See the Phase 2 section at the bottom of `tent_irrigation_esphome.md` for the full YAML block to append to the `tent-irrigation-controller` config.

GPIOs for step/dir pins are TBD — assign free GPIOs at install time and update the config.
**Free GPIOs on current config** (verify before assigning): GPIO5, GPIO15, GPIO33

### HA Automation (Phase 2)

See `needle_valve_temp_control` automation in `grow_tent_package.yaml`.

- Feedback: `sensor.reservoir_temperature_tent`
- Setpoint: `input_number.grow_tent_target_temp` (°C)
- Hysteresis: ±0.5°C dead band, adjusts ±10 steps per cycle
- Or: replace with ESPHome PID climate component for tighter on-device control

---

## Sensor Entity Reference

| Sensor | Entity ID | Notes |
|--------|-----------|-------|
| Reservoir temp | `sensor.reservoir_temperature_tent` | Dallas DS18B20 on GPIO4 |
| Target temp setpoint | `input_number.grow_tent_target_temp` | °C, min 15 / max 35 / step 0.5 |
| Needle valve position | `number.needle_valve_position_tent_irrigation_controller` | Phase 2 only |
