# grow-tent-climate — ESPHome Device

**Board:** ESP32-WROOM-32, 30-pin devkit (flashed 2026-07-16, COM6/CP210x)
**Device name:** `grow-tent-climate`
**Static IP:** `192.168.2.236` (set in firmware — the router refuses DHCP reservations)
**WiFi:** Brentons grow-area AP preferred (priority 10), main router as fallback
**Config:** `esphome-config/grow-tent-climate.yaml`

> 30-pin note: this board has **no GPIO16/17**. Fine here — the mux design only
> needs GPIO21/22.

---

## Site facts

| Fact | Value | Why it's recorded |
|------|-------|-------------------|
| **Elevation** | **30 m ASL** | SCD41 `altitude_compensation` — see [CO2 calibration](#co2-calibration-policy) |
| Tent intake air | Living room | Never sees outdoor 420 ppm — drives the ASC/FRC policy below |
| Tent exhaust | Outside | |
| Barometric pressure sensor | **None, by design** | Cancelled; `sensor.tent_average_pressure` was deleted 2026-07-24 |

---

## I2C topology

One physical bus → **TCA9548A** mux → one sensor per channel. All four SHT41
share address `0x44`, so each gets its own channel; a shorted or dead sensor
only takes out its own channel instead of the whole bus. The SCD41 (`0x62`)
does not clash, but shares the mux anyway for the same isolation reason.

- Bus `bus_main`: SDA **GPIO21**, SCL **GPIO22**, 50 kHz, `scan: true`
- TCA9548A strap: A0/A1/A2 all to GND → address **0x70**

| Channel | `bus_id` | Sensor | Position |
|---------|----------|--------|----------|
| 0 | `mux_canopy` | SHT41 `0x44` | Canopy |
| 1 | `mux_flower` | SHT41 `0x44` | Flower |
| 2 | `mux_stem` | SHT41 `0x44` | Stem |
| 3 | `mux_controller` | SHT41 `0x44` | Controller enclosure |
| 4 | `mux_co2` | SCD41 `0x62` | CO2 / temp / RH |

> Channel 0 was named **Lights** until 2026-07-29; renamed to **Canopy** before mounting.

---

## Temperature / humidity — 4× SHT41

| Position | Temperature entity | Humidity entity | In tent averages? |
|----------|--------------------|-----------------|-------------------|
| Canopy | `sensor.grow_tent_climate_canopy_temperature` | `..._canopy_humidity` | **Yes** |
| Flower | `sensor.grow_tent_climate_flower_temperature` | `..._flower_humidity` | **Yes** |
| Stem | `sensor.grow_tent_climate_stem_temperature` | `..._stem_humidity` | **Yes** |
| Controller | `sensor.grow_tent_climate_controller_temperature` | `..._controller_humidity` | **No — excluded** |

**Canopy + Flower + Stem = tent air.** These three feed
`sensor.tent_average_temperature` / `_humidity` in HA by area auto-discovery
(area `tent` + `device_class`), which in turn feed `sensor.grow_tent_vpd` and
`sensor.tent_dewpoint`.

**Controller is deliberately excluded.** It measures the control-box enclosure,
which two buck regulators self-heat, so it legitimately runs ~2 °C hotter than
tent air. Including it would bias the average and would trip the divergence
check permanently. It drives the controller over-temp / condensation alerts
instead.

### Filtering (added 2026-08-05)

Each of the eight values carries:

```yaml
      accuracy_decimals: 2
      filters:
        - sliding_window_moving_average:
            window_size: 4
            send_every: 2
            send_first_at: 1
        - round: 2
```

- Samples every 30 s, **publishes every 60 s** as the mean of the last 4 samples.
- `send_first_at: 1` publishes the first sample after boot, so HA is not blank
  for two minutes after every flash.
- Order matters: **average first, then round**, so rounding applies to the
  smoothed value rather than to each raw sample.

> ⚠ **`accuracy_decimals` alone does not round the stored value.** It only sets
> display precision (HA maps it to `suggested_display_precision`); the raw
> float still crosses the API and lands in the recorder at full width. Verified
> 2026-08-05 — a flash carrying `accuracy_decimals` but no `round` filter left
> states reading `22.1890316009521`. The `round: 2` filter is what produced
> `22.35`. Do not remove it as redundant.

Before this change the board published raw unrounded float32 every 30 s — 13
decimal places, ~29k recorder rows/day from this board alone, with every publish
counting as a state *change* because no two raw samples are ever bit-identical.

---

## CO2 — SCD41

**Status: not fitted.** `sensor.grow_tent_climate_tent_co2*` read `unknown`.
The replacement sensor still needs mounting; the original arrived DOA
(internally shorted VDD↔GND).

### CO2 calibration policy

**ASC (Automatic Self-Calibration) is flashed `false`, permanently.**

ASC tracks the lowest CO2 seen over a rolling ~7-day window and re-zeros so
that minimum reads ~400 ppm. That is only valid if the sensor periodically
breathes genuine ~420 ppm **outdoor** air. **This tent never does** — intake is
living-room air and exhaust goes outside. An occupied indoor space bottoms out
around 450–700 ppm, so ASC would drag that floor down to 400 and bake in a
permanent **50–300 ppm under-read** — the dangerous direction, since a dosing
automation would then overshoot chasing a target the sensor claims it hasn't hit.

ASC lives in the sensor's own EEPROM and fresh SCD41s ship with it **on**, which
is why it is flashed `false` *before* the replacement is fitted — it never runs
a bad cycle. Not runtime-toggleable; changing it is a one-line reflash.

**Baseline is maintained by manual FRC instead:** carry the sensor to genuinely
fresh outdoor air at the start of every grow (before seedlings go in), away from
the house and your own breath, leave it powered and measuring for **at least
3 minutes** (Sensirion's equilibration requirement), then press the guarded
**CO2 Force Recalibration** button. Drift without ASC is only tens of ppm/yr, so
per-grow FRC is comfortably more often than needed.

The button refuses to fire when the live reading is >300 ppm from
`number.co2_calibration_reference` (default 425 ppm) — wide enough for any
plausible drift, narrow enough to catch the real mistake of pressing while still
in tent air.

### Altitude compensation

**Site elevation is 30 m ASL.** With no pressure sensor on the board, NDIR ppm
is compensated statically by altitude instead.

**It barely matters at this elevation.** 30 m is ~1009.7 hPa against 1013.25 at
sea level — a **0.36 %** pressure delta, so the correction is roughly **1.5 ppm
at 420 ppm** and **5 ppm at 1500 ppm**. That is far inside the SCD41's own
±(40 ppm + 5 %) spec. Set it for correctness, but do not treat it as an accuracy
lever — **FRC in real outdoor air is what actually determines accuracy here.**

`altitude_compensation: 30m` is currently **commented out** in the config,
deliberately: the SCD41 is not fitted, and leaving it commented keeps the config
from leading the flashed firmware. **Uncomment and reflash in the same pass that
mounts the replacement sensor.**

---

## Open items

- [ ] Fit, mount and FRC the replacement SCD41
- [ ] Uncomment `altitude_compensation: 30m` in that same flash
- [ ] Decide whether the SCD41's own temp/RH join the tent averages (currently
      excluded via the `co2` entity-id rule — it carries a ~+4 °C offset and is
      a CO2 die temperature, not an air probe)
- [ ] "Insurance wiring" for the replacement (per-drop polyfuses / Schottky /
      clamp / local caps) — specced, nothing bought

## Related

- Flashing: `.claude/skills/flash-esp32/SKILL.md` — OTA from Windows,
  `uvx esphome@2026.6.5 run grow-tent-climate.yaml --device 192.168.2.236`
- Tent averages / VPD / divergence templates: **`homeassistant-config`** repo,
  `packages/grow_tent_package.yaml` and `templates/tent_average_spread.yaml`
- Sibling board docs: `grow_tent_one_esphome.md`, `tent_irrigation_esphome.md`
