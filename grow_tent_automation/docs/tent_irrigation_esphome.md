# Tent Irrigation — Home Assistant / ESPHome

*HA-relevant content migrated from the Grow Tent project. Physical hardware docs remain in `D:\Claude\Projects\Grow Tent\Tent_Irrigation_Project.md`.*

---

## Operation Modes (Home Assistant Controlled)

### Feed Cycle
| Component | State | Control |
|-----------|-------|---------|
| Feed Pump (Flora Flex) | ON | Home Assistant |
| Flush Pump (DEKOPRO) | OFF | Home Assistant |
| Flush Valve | CLOSED | Home Assistant (12V DC) |
| Feed Valve | OPEN | Home Assistant (12V DC) |
| Drain Valve | CLOSED | Home Assistant (12V DC) |
| **Result** | Nutrients flow to emitters | |

### Flush Cycle (Push nutrients, fill with clean water)
| Component | State | Control |
|-----------|-------|---------|
| Feed Pump (Flora Flex) | OFF | Home Assistant |
| Flush Pump (DEKOPRO) | ON | Home Assistant |
| Flush Valve | OPEN | Home Assistant (12V DC) |
| Feed Valve | CLOSED | Home Assistant (12V DC) |
| Drain Valve | OPEN or CLOSED | Home Assistant (12V DC) |
| **Result** | Clean water pushes remaining nutrients to plants, then fills lines | |

**Note:** All U.S. Solid 3/4" 12V DC solenoid valves are controlled by Home Assistant via the ESP32 relay outputs.

### Night Pulses (Reservoir Mixing & Aeration During Dark Period)

Replaces the older indefinite "night cycle" loop. Discrete pulse sequences run at user-set times after lights-off, gated by growth stage.

**Pulse shape** (per session, durations are UI-editable `input_number`s):
1. Stir pumps ON for `night_pulse_stir_pre_minutes` (default 7 min) — homogenize
2. 500 ms gap
3. Air pump ON for `night_pulse_air_minutes` (default 45 min) — aerate
4. 500 ms gap
5. Stir pumps ON for `night_pulse_stir_post_minutes` (default 5 min) — re-mix
6. `input_boolean.alternating_active` flips on for the full sequence, off at end

Total ≈ 57 min per pulse. Air max capped at 55 min so total stays under the 60-min air-pump watchdog threshold.

**Schedule helpers** (UI-editable absolute clock times — drag in HA Helpers UI):

| Stage group (covers) | Helper(s) | Defaults |
|---|---|---|
| Veg-side: Seedling, Early Veg, Veg, Transition | `input_datetime.night_pulse_veg_1`, `_2` | 14:00, 16:00 (lights_off 12:00 + 2h, +4h) |
| Flower-side: Early Flower, Flower, Late Flower | `input_datetime.night_pulse_flower_1` … `_5` | 08:00, 10:00, 12:00, 14:00, 16:00 (lights_off 06:00 + 2/4/6/8/10h) |

If you shift your lights schedule, drag the pulse times to match — they don't auto-adjust.

**Automations:** `automation.irrigation_night_pulses_veg`, `automation.irrigation_night_pulses_flower` (one per stage group). Both gated on `input_boolean.irrigation_enabled` and the appropriate stage list.

**Script:** `script.run_night_pulse` is the single entry point — both automations call it. Reuses the same pump entities as `script.run_alternating`.

---

## ESP32 Entities Visible in Home Assistant

Device: `tent-irrigation-controller`

### Binary Sensors (float switches)
| Entity | GPIO | Description |
|--------|------|-------------|
| Feed Empty Irrigation Tent | GPIO21 | Feed reservoir — empty level |
| Feed Half Irrigation Tent | GPIO19 | Feed reservoir — half level |
| Feed Three Quarter Irrigation Tent | GPIO18 | Feed reservoir — three quarter level |
| Feed Full Irrigation Tent | GPIO16 | Feed reservoir — full level |
| Flush Empty Irrigation Tent | GPIO17 | Flush reservoir — empty level |
| Flush Half Irrigation Tent | GPIO13 | Flush reservoir — half level |
| Flush Full Irrigation Tent | GPIO14 | Flush reservoir — full level |

### Sensors
| Entity | GPIO | Description |
|--------|------|-------------|
| Reservoir Temperature Tent | GPIO4 (1-wire) | Nutrient reservoir temp (Dallas) |
| Air Pump Temperature Tent | GPIO4 (1-wire) | Air pump area temp (Dallas) |
| Pressure Pre-Regulator Tent | GPIO34 (ADC) | System pressure before regulator (PSI) |
| Pressure Post-Regulator Tent | GPIO35 (ADC) | System pressure after regulator (PSI) |
| Flow Rate Irrigation Tent | GPIO32 (pulse) | Flow rate (L/min) — sensor range: 0.5–20 L/min — entity: `sensor.flow_rate_irrigation_tent` |
| Flow Total Irrigation Tent | GPIO32 (pulse) | Cumulative volume (L) — entity: `sensor.flow_total_irrigation_tent` |

### Valves (solenoid control)
| Entity | GPIO | Description |
|--------|------|-------------|
| Flush Drain | GPIO22 | End-of-line drain valve |
| Flush Irrigation | GPIO23 | Flush reservoir input valve |
| Feed Fill Valve | GPIO25 | Feed reservoir fill valve — HA entity: `valve.feed_fill_valve_irrigation_tent` |
| Flush Fill Valve | GPIO26 | Flush reservoir fill valve — HA entity: `valve.flush_fill_valve_irrigation_tent` |
| Feed Irrigation | GPIO27 | Feed distribution valve |

---

## ESPHome Code — Complete File

**Device name:** `tent-irrigation-controller`
**Framework:** `esp-idf`
**Attenuation note:** Valid options are `0db`(1.1V), `2.5db`(1.5V), `6db`(2.2V), `12db`(3.9V), `auto`. Use `12db` for voltage divider output range (0.33–3.0V).

**Live source of truth:** `D:\Claude\Projects\esphome-config\tent-irrigation-controller.yaml` (deploys to ESPHome VM at `192.168.2.14:/root/config`). The YAML below is a reference snapshot and may drift — for any actual change, edit the live file and trigger a build/flash via the ESPHome dashboard at http://192.168.2.14:6052.

```yaml
esphome:
  name: tent-irrigation-controller
  friendly_name: Tent Irrigation Controller

esp32:
  board: esp32dev
  framework:
    type: esp-idf

logger:

api:
  encryption:
    key: "6QW8BdnIVJgYu+IoT/SGzCpkUOMSvI2ksIbLwLHsLUA="

ota:
  - platform: esphome
    password: "e9d18a3d5531692f06956f87737ce080"

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  ap:
    ssid: "Tent-Irrigation-Controller"
    password: "qLhuT30xVe6X"

captive_portal:

binary_sensor:
   - platform: gpio
     pin:
       number: GPIO21
       mode: INPUT_PULLUP
       inverted: true
     name: "Feed Empty"
     id: feed_empty_irrigation_tent
     device_class: moisture
     filters:
       - delayed_on: 2s
       - delayed_off: 2s

   - platform: gpio
     pin:
       number: GPIO19
       mode: INPUT_PULLUP
       inverted: true
     name: "Feed Half"
     id: feed_half_irrigation_tent
     device_class: moisture
     filters:
       - delayed_on: 2s
       - delayed_off: 2s

   - platform: gpio
     pin:
       number: GPIO18
       mode: INPUT_PULLUP
       inverted: true
     name: "Feed Three Quarter"
     id: feed_three_quarter_irrigation_tent
     device_class: moisture
     filters:
       - delayed_on: 2s
       - delayed_off: 2s

   - platform: gpio
     pin:
       number: GPIO17
       mode: INPUT_PULLUP
       inverted: true
     name: "Feed Full"
     id: feed_full_irrigation_tent
     device_class: moisture
     filters:
       - delayed_on: 2s
       - delayed_off: 2s

   - platform: gpio
     pin:
       number: GPIO16
       mode: INPUT_PULLUP
       inverted: true
     name: "Flush Empty"
     id: flush_empty_irrigation_tent
     device_class: moisture
     filters:
       - delayed_on: 2s
       - delayed_off: 2s

   - platform: gpio
     pin:
       number: GPIO13
       mode: INPUT_PULLUP
       inverted: true
     name: "Flush Half"
     id: flush_half_irrigation_tent
     device_class: moisture
     filters:
       - delayed_on: 2s
       - delayed_off: 2s

   - platform: gpio
     pin:
       number: GPIO14
       mode: INPUT_PULLUP
       inverted: true
     name: "Flush Full"
     id: flush_full_irrigation_tent
     device_class: moisture
     filters:
       - delayed_on: 2s
       - delayed_off: 2s

one_wire:
   - platform: gpio
     pin: GPIO4

sensor:
   - platform: dallas_temp
     address: 0x5000000047758c28
     name: "Feed Temperature"
     id: feed_temperauture_irrigation_tent

   - platform: dallas_temp
     address: 0x6f000000455cab28
     name: "Flush Temperature"
     id: flush_temperature_irrigation_tent

   - platform: adc
     pin: GPIO34
     name: "Pressure Pre-Regulator Tent"
     id: pressure_pre_regulator
     attenuation: 12db
     update_interval: 2s
     filters:
       - lambda: |-
           float psi = (x - 0.333f) / (3.0f - 0.333f) * 100.0f;
           return psi < 0.0f ? 0.0f : psi;
       - sliding_window_moving_average:
           window_size: 5
           send_every: 5
     unit_of_measurement: "PSI"
     device_class: pressure
     state_class: measurement
     accuracy_decimals: 1

   - platform: adc
     pin: GPIO35
     name: "Pressure Post-Regulator Tent"
     id: pressure_post_regulator
     attenuation: 12db
     update_interval: 2s
     filters:
       - lambda: |-
           float psi = (x - 0.333f) / (3.0f - 0.333f) * 100.0f;
           return psi < 0.0f ? 0.0f : psi;
       - sliding_window_moving_average:
           window_size: 5
           send_every: 5
     unit_of_measurement: "PSI"
     device_class: pressure
     state_class: measurement
     accuracy_decimals: 1

   - platform: pulse_counter
     pin:
       number: GPIO32
       mode: INPUT
     name: "Flow Rate Tent"
     id: flow_rate
     update_interval: 60s
     filters:
       - lambda: |-
           return x / 7.5f;  # K-factor = 7.5 — confirm from sensor datasheet and update if needed
     unit_of_measurement: "L/min"
     state_class: measurement
     accuracy_decimals: 2
     total:
       name: "Flow Total Tent"
       id: flow_total
       unit_of_measurement: "L"
       state_class: total_increasing
       filters:
         - lambda: return x / 7.5f;  # K-factor = 7.5 — confirm from sensor datasheet and update if needed

output:
   - platform: gpio
     pin:
       number: GPIO22
       mode: OUTPUT
     id: flush_drain_valve_tent_output

   - platform: gpio
     pin:
       number: GPIO23
       mode: OUTPUT
     id: flush_irrigation_valve_tent_output

   - platform: gpio
     pin:
       number: GPIO25
       mode: OUTPUT
     id: empty_two_tent_output

   - platform: gpio
     pin:
       number: GPIO26
       mode: OUTPUT
     id: empty_one_tent_output

   - platform: gpio
     pin:
       number: GPIO27
       mode: OUTPUT
     id: main_irrigation_valve_tent_output

valve:
   - platform: template
     name: "Flush Drain"
     id: reservoir_prime_valve_tent
     disabled_by_default: true
     open_action:
       - output.turn_on: flush_drain_valve_tent_output
     close_action:
       - output.turn_off: flush_drain_valve_tent_output
     optimistic: true

   - platform: template
     name: "Flush Irrigation"
     id: flush_irrigation_valve_tent
     open_action:
       - output.turn_on: flush_irrigation_valve_tent_output
     close_action:
       - output.turn_off: flush_irrigation_valve_tent_output
     optimistic: true

   - platform: template
     name: "Empty Two"
     id: reservoir_prime_block_valve_tent
     disabled_by_default: true
     open_action:
       - output.turn_on: empty_two_tent_output
     close_action:
       - output.turn_off: empty_two_tent_output
     optimistic: true

   - platform: template
     name: "Empty One"
     id: empty_one_tent
     open_action:
       - output.turn_on: empty_one_tent_output
     close_action:
       - output.turn_off: empty_one_tent_output
     optimistic: true

   - platform: template
     name: "Feed Irrigation"
     id: main_irrigation_valve_tent
     open_action:
       - output.turn_on: main_irrigation_valve_tent_output
     close_action:
       - output.turn_off: main_irrigation_valve_tent_output
     optimistic: true
```

---

## ESPHome Component Reference

### ADC Sensor (`sensor/adc`)

| Config Key | Required | Default | Notes |
|------------|----------|---------|-------|
| `pin` | Yes | — | Must be ADC1 pin when WiFi active on ESP32 |
| `attenuation` | No | `0db` | ESP32 only: `0db`(1.1V) `2.5db`(1.5V) `6db`(2.2V) `12db`(3.9V) `auto` |
| `raw` | No | false | Returns raw counts instead of calibrated voltage |
| `samples` | No | 1 | Number of ADC readings averaged per update |
| `sampling_mode` | No | `avg` | `avg`, `min`, or `max` |
| `update_interval` | No | `60s` | — |

**ESP32-WROOM-32E ADC pin map:**
- ADC1 (WiFi-safe): GPIO32, 33, 34, 35, 36, 39
- ADC2 (disabled when WiFi active): GPIO0, 2, 4, 12–15, 25–27 — **do not use for analog sensors**

**Usable voltage range:** ~0.075V to ~3.12V with `auto` attenuation.

**WiFi + ADC noise:** WiFi transmissions cause brief ADC noise spikes even on ADC1. Mitigated by `sliding_window_moving_average`. Add `samples: 5` if jitter persists in HA.

---

### Pulse Counter Sensor (`sensor/pulse_counter`)

| Config Key | Required | Default | Notes |
|------------|----------|---------|-------|
| `pin` | Yes | — | Any interrupt-capable GPIO |
| `count_mode.rising_edge` | No | `INCREMENT` | `DISABLE`, `INCREMENT`, or `DECREMENT` |
| `count_mode.falling_edge` | No | `DISABLE` | `DISABLE`, `INCREMENT`, or `DECREMENT` |
| `use_pcnt` | No | `true` | Use ESP32 hardware pulse counter (max 8 channels) |
| `internal_filter` | No | `13us` | Discard pulses shorter than this |
| `update_interval` | No | `60s` | — |
| `total` | No | — | Sub-sensor tracking cumulative pulse count |

**Converting to flow:**
```yaml
filters:
  - lambda: return x / K_FACTOR;  # K_FACTOR = pulses per liter (from sensor datasheet)
```

---

### Dallas Temperature Sensor (`sensor/dallas_temp`)

| Config Key | Required | Default | Notes |
|------------|----------|---------|-------|
| `address` | No* | — | Hardware address (preferred with multiple sensors) |
| `index` | No* | — | Zero-based order on bus |
| `resolution` | No | 12 | 9–12 bits |
| `update_interval` | No | `60s` | — |
| `one_wire_id` | No | — | Required only with multiple 1-Wire buses |

**Scanning for addresses:** Flash with `one_wire:` configured and check ESPHome logs — addresses printed on boot.

---

### GPIO Binary Sensor (`binary_sensor/gpio`)

| Config Key | Default | Notes |
|------------|---------|-------|
| `use_interrupt` | `true` | Hardware interrupt — 98% lower CPU vs polling |
| `interrupt_type` | `ANY` | `ANY`, `RISING`, or `FALLING` |

**Debounce filter** (float switches/reed contacts):
```yaml
filters:
  - delayed_on: 10ms
  - delayed_off: 10ms
```

---

### Sensor Base — Common Filters

| Filter | Purpose |
|--------|---------|
| `lambda` | Custom math transform — `x` is the input value |
| `calibrate_linear` | Map measured values to known-good values |
| `sliding_window_moving_average` | Smooth noisy signals (e.g., ESP32 ADC) |
| `median` | Remove outliers over a sliding window |
| `delta` | Only publish if change exceeds threshold |
| `throttle` | Limit publish frequency |
| `round` | Round to N decimal places |

**Accessing sensor values in automations:**
- `id(sensor_id).state` — current filtered value
- `id(sensor_id).raw_state` — pre-filter value
- `on_value_range` trigger — fire automations when value crosses a threshold

---

## Phase 2 — Needle Valve Stepper Config

*Future addition — no timeline set. See `reservoir_temp_mixing.md` for full context.*

Append the following blocks to the `tent-irrigation-controller` ESPHome config. Assign step/dir GPIOs to free pins at install time (current free options: GPIO5, GPIO15, GPIO33 — verify before committing).

```yaml
# --- Phase 2: Needle valve stepper (hot/cold mixing) ---

stepper:
  - platform: a4988
    id: needle_valve_stepper
    step_pin: GPIOXX    # TBD — free GPIO, assign at install
    dir_pin: GPIOXX     # TBD — free GPIO, assign at install
    max_speed: 250 steps/s
    acceleration: 100 steps/s²

number:
  - platform: template
    id: needle_valve_position
    name: "Needle Valve Position"
    min_value: 0
    max_value: 1000     # calibrate full open→close range in steps at install
    step: 1
    optimistic: true
    set_action:
      - stepper.set_target:
          id: needle_valve_stepper
          target: !lambda return (int) x;
```

**Calibration (at install):**
1. Power on with stepper at known position (fully closed = 0)
2. Jog open slowly via `number.needle_valve_position` until fully open, note step count
3. Set `max_value` to that count
4. Mark physical "closed" position on coupler/bracket for re-homing after power loss
