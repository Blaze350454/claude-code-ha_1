# Irrigation System - Home Assistant

## System Overview

ESP32-based irrigation control system integrated with Home Assistant via ESPHome.

## Hardware Inventory

### Valves
| Type | Brand | Control Method |
|------|-------|----------------|
| Solenoid valves | US Solid | ESP32 GPIO via ESPHome |
| Motorized ball valves | US Solid | ESP32 GPIO via ESPHome |
| Irrigation valves | Rainbird | ESP32 GPIO via ESPHome |

### Pumps
| Pump | Control Method |
|------|----------------|
| Pressure pump | Matter/WiFi smart plug |
| Air pump | Matter/WiFi smart plug |
| Aquarium pump 1 | Matter/WiFi smart plug |
| Aquarium pump 2 | Matter/WiFi smart plug |

### Sensors
| Sensor | Model | Purpose | Interface |
|--------|-------|---------|-----------|
| Liquid level | XKC-Y25 | Reservoir fluid levels | ESP32 via ESPHome |
| Temperature | DS18B20 | Temperature monitoring | ESP32 via ESPHome |

### Controllers
- **ESP32** - All valve and sensor control via ESPHome
- **Smart plugs** - Pump control via Matter/WiFi

## Project Structure

```
Irrigation/
├── esphome/              # ESPHome device configurations
│   ├── irrigation-controller.yaml
│   └── secrets.yaml
├── home-assistant/
│   ├── automations/      # HA automation YAML files
│   └── dashboards/       # Lovelace dashboard configs
├── docs/                 # Additional documentation
└── README.md
```

## ESPHome Pin Reference

### XKC-Y25 Liquid Level Sensor
- Non-contact capacitive sensor
- Output: Digital (HIGH when liquid detected)
- Voltage: 5-24V DC
- Interface: Single GPIO pin (digital input)

### DS18B20 Temperature Sensor
- 1-Wire digital temperature sensor
- Requires 4.7kΩ pull-up resistor on data line
- Multiple sensors can share one GPIO pin

### Valve Control
- **Solenoid valves**: Single GPIO (on/off)
- **Motorized ball valves**: May require 2 GPIOs (open/close) or single GPIO depending on model

## Next Steps

- [ ] Define ESP32 GPIO pin assignments
- [ ] Create ESPHome configuration files
- [ ] Set up Home Assistant automations
- [ ] Create irrigation dashboard
- [ ] Configure weather-based scheduling (optional)
