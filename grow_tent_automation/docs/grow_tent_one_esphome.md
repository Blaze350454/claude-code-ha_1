# grow-tent-one — ESPHome Device

**Board:** ESP32-C3-DevKitM-1
**ESPHome dashboard:** `http://192.168.2.14:6052/`
**Device name:** `grow-tent-one`

---

## XKC-Y25-NPN Liquid Level Sensors

Two non-contact capacitive sensors running on 15-foot Cat5 cable runs (3.3V power).

### GPIO Pins

| Sensor | GPIO | HA Entity |
|--------|------|-----------|
| Table Drain Empty | GPIO6 | `binary_sensor.table_drain_empty_irrigation_tent` |
| Table Drain Full | GPIO7 | `binary_sensor.table_drain_full_irrigation_tent` |

> **GPIO12-17 are reserved for SPI flash on ESP32-C3 — do not use.**

### Wiring

No external resistors. Uses internal `INPUT_PULLUP`. Sensor powered externally — only signal wire and shared GND run to ESP32.

### Cat5 Pair Assignment

| Pair | Wire A | Wire B |
|------|--------|--------|
| 1 | Sensor 1 SIG | Sensor 1 GND |
| 2 | Sensor 2 SIG | Sensor 2 GND |
| 3-4 | spare | spare |

### ESPHome Config

```yaml
binary_sensor:
  - platform: gpio
    pin:
      number: GPIO6
      mode: INPUT_PULLUP
      inverted: true
    name: "Table Drain Empty"
    id: table_drain_empty_irrigation_tent
    device_class: moisture

  - platform: gpio
    pin:
      number: GPIO7
      mode: INPUT_PULLUP
      inverted: true
    name: "Table Drain Full"
    id: table_drain_full_irrigation_tent
    device_class: moisture
```

### Behavior

- `inverted: true` — NPN open-collector pulls SIG low when liquid detected; ESPHome inverts so `on` = liquid present
- At startup with no liquid: GPIO reads HIGH → entity reports `off`
- With liquid detected: GPIO pulls LOW → entity reports `on`

### Level Logic

| State | Meaning |
|-------|---------|
| Neither sensor `on` | Table empty (0%) |
| `table_drain_empty_irrigation_tent` on | Water at lower sensor — half full (50%) |
| `table_drain_full_irrigation_tent` on | Water at upper sensor — full (100%) |

### Verification Steps

1. Flash via ESPHome dashboard
2. Check logs: GPIO6/7 should read HIGH (no liquid) at startup
3. Hold sensor against water container — HA entity flips to `on`
4. Remove — returns to `off` after 50ms debounce
