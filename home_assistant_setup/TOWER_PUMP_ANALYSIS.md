# Tower Pump Automation - Analysis & Improvements

## Current Logic Understanding

**Trigger:** Water sensor state changes (after 10 sec) or HA starts

**Behavior:**
1. **Sensor OFF (no water?)** → Wait 25 min → Turn pump OFF
2. **Sensor ON (water detected?)** → Complex cycle with retries
3. **Sensor unavailable** → Turn pump OFF (safety)

## Issues & Questions

### 🤔 Logic Clarification Needed

**What does your sensor detect?**
- **Option A:** Sensor ON = Water level TOO HIGH → Need to pump OUT
- **Option B:** Sensor ON = Water level TOO LOW → Need to pump IN

This is important because the logic seems backwards if it's Option B!

### 🔴 Current Issues

1. **Redundant pump shutoffs** - Pump gets turned off multiple times
2. **Complex retry logic** - The repeat block is hard to follow
3. **Mode not set** - Could cause overlapping automations
4. **Magic numbers** - Delays (25 min, 8 min, 10 min) aren't explained
5. **Race conditions** - Sensor changing during delays

## ✅ Cleaned Up Version 1: Simplified Logic

```yaml
alias: Tower Pump Control - Simplified
description: Controls water pump based on water sensor with retry logic
mode: restart  # Restart if triggered again

triggers:
  - entity_id: binary_sensor.tower_water_sensor
    for:
      seconds: 10
    trigger: state
    id: sensor_changed
  - event: start
    trigger: homeassistant
    id: ha_start

actions:
  - choose:
      # Safety: Turn off if sensor unavailable
      - conditions:
          - condition: or
            conditions:
              - condition: state
                entity_id: binary_sensor.tower_water_sensor
                state: unavailable
              - condition: state
                entity_id: binary_sensor.tower_water_sensor
                state: unknown
        sequence:
          - action: switch.turn_off
            target:
              entity_id: switch.tower_water_pump

      # Sensor OFF: No water needed, ensure pump is off
      - conditions:
          - condition: state
            entity_id: binary_sensor.tower_water_sensor
            state: "off"
        sequence:
          - delay:
              minutes: 25  # Grace period before stopping
          - action: switch.turn_off
            target:
              entity_id: switch.tower_water_pump

      # Sensor ON: Water needed, run pump cycle
      - conditions:
          - condition: state
            entity_id: binary_sensor.tower_water_sensor
            state: "on"
        sequence:
          # Initial pump cycle
          - action: switch.turn_on
            target:
              entity_id: switch.tower_water_pump

          - wait_for_trigger:
              - entity_id: binary_sensor.tower_water_sensor
                to: "off"
                trigger: state
            timeout: "00:03:00"

          - action: switch.turn_off
            target:
              entity_id: switch.tower_water_pump

          # Wait before checking if more pumping needed
          - delay:
              minutes: 8

          # Retry loop if still needed
          - repeat:
              while:
                - condition: state
                  entity_id: binary_sensor.tower_water_sensor
                  state: "on"
              sequence:
                - action: switch.turn_on
                  target:
                    entity_id: switch.tower_water_pump

                - wait_for_trigger:
                    - entity_id: binary_sensor.tower_water_sensor
                      to: "off"
                      trigger: state
                  timeout: "00:02:00"

                - action: switch.turn_off
                  target:
                    entity_id: switch.tower_water_pump

                - delay:
                    minutes: 10
```

**Improvements:**
- ✅ Added `mode: restart` to prevent overlapping runs
- ✅ Changed `if/then/repeat/until` to simpler `repeat/while`
- ✅ Moved safety check to top
- ✅ Clearer structure

## ✅ Cleaned Up Version 2: With Variables

```yaml
alias: Tower Pump Control - With Variables
description: Controls water pump with configurable timings
mode: restart

variables:
  grace_period: 25  # Minutes to wait before stopping pump
  initial_wait: 8   # Minutes to wait after first cycle
  retry_wait: 10    # Minutes to wait between retry cycles
  pump_timeout: 3   # Minutes max for initial pump cycle
  retry_timeout: 2  # Minutes max for retry cycles

triggers:
  - entity_id: binary_sensor.tower_water_sensor
    for:
      seconds: 10
    trigger: state
  - event: start
    trigger: homeassistant

actions:
  - choose:
      # Safety: Sensor unavailable
      - conditions:
          - condition: state
            entity_id: binary_sensor.tower_water_sensor
            state:
              - unavailable
              - unknown
        sequence:
          - action: switch.turn_off
            target:
              entity_id: switch.tower_water_pump

      # No water needed
      - conditions:
          - condition: state
            entity_id: binary_sensor.tower_water_sensor
            state: "off"
        sequence:
          - delay:
              minutes: "{{ grace_period }}"
          - action: switch.turn_off
            target:
              entity_id: switch.tower_water_pump

      # Water needed - pump cycle
      - conditions:
          - condition: state
            entity_id: binary_sensor.tower_water_sensor
            state: "on"
        sequence:
          # Initial cycle
          - action: switch.turn_on
            target:
              entity_id: switch.tower_water_pump
          - wait_for_trigger:
              - entity_id: binary_sensor.tower_water_sensor
                to: "off"
                trigger: state
            timeout: "00:0{{ pump_timeout }}:00"
          - action: switch.turn_off
            target:
              entity_id: switch.tower_water_pump

          # Wait before retry check
          - delay:
              minutes: "{{ initial_wait }}"

          # Retry if still needed
          - repeat:
              while:
                - condition: state
                  entity_id: binary_sensor.tower_water_sensor
                  state: "on"
              sequence:
                - action: switch.turn_on
                  target:
                    entity_id: switch.tower_water_pump
                - wait_for_trigger:
                    - entity_id: binary_sensor.tower_water_sensor
                      to: "off"
                      trigger: state
                  timeout: "00:0{{ retry_timeout }}:00"
                - action: switch.turn_off
                  target:
                    entity_id: switch.tower_water_pump
                - delay:
                    minutes: "{{ retry_wait }}"
```

**Improvements:**
- ✅ All timing values in variables at top
- ✅ Easy to adjust without editing logic
- ✅ Self-documenting

## ✅ Version 3: Blueprint-Ready

If you want to reuse this for multiple pumps:

```yaml
blueprint:
  name: Water Pump Controller
  description: Control pump based on water sensor with retry logic
  domain: automation

  input:
    water_sensor:
      name: Water Sensor
      selector:
        entity:
          domain: binary_sensor

    pump_switch:
      name: Pump Switch
      selector:
        entity:
          domain: switch

    grace_period:
      name: Grace Period (minutes)
      description: Wait time before stopping pump when sensor is off
      default: 25
      selector:
        number:
          min: 0
          max: 60

    initial_wait:
      name: Initial Wait (minutes)
      description: Wait after first pump cycle
      default: 8
      selector:
        number:
          min: 0
          max: 30

mode: restart

triggers:
  - entity_id: !input water_sensor
    for:
      seconds: 10
    trigger: state
  - event: start
    trigger: homeassistant

actions:
  - choose:
      - conditions:
          - condition: state
            entity_id: !input water_sensor
            state:
              - unavailable
              - unknown
        sequence:
          - action: switch.turn_off
            target:
              entity_id: !input pump_switch

      - conditions:
          - condition: state
            entity_id: !input water_sensor
            state: "off"
        sequence:
          - delay:
              minutes: !input grace_period
          - action: switch.turn_off
            target:
              entity_id: !input pump_switch

      - conditions:
          - condition: state
            entity_id: !input water_sensor
            state: "on"
        sequence:
          - action: switch.turn_on
            target:
              entity_id: !input pump_switch
          - wait_for_trigger:
              - entity_id: !input water_sensor
                to: "off"
                trigger: state
            timeout: "00:03:00"
          - action: switch.turn_off
            target:
              entity_id: !input pump_switch
          - delay:
              minutes: !input initial_wait
          - repeat:
              while:
                - condition: state
                  entity_id: !input water_sensor
                  state: "on"
              sequence:
                - action: switch.turn_on
                  target:
                    entity_id: !input pump_switch
                - wait_for_trigger:
                    - entity_id: !input water_sensor
                      to: "off"
                      trigger: state
                  timeout: "00:02:00"
                - action: switch.turn_off
                  target:
                    entity_id: !input pump_switch
                - delay:
                    minutes: 10
```

## 💡 Additional Suggestions

### Add Notifications
```yaml
- action: notify.mobile_app_your_phone
  data:
    title: "Tower Pump Alert"
    message: "Pump has been running for {{ retry_count }} cycles"
```

### Add Max Retry Limit
```yaml
- repeat:
    count: 5  # Max 5 retries
    while:
      - condition: state
        entity_id: binary_sensor.tower_water_sensor
        state: "on"
    sequence:
      # ... pump cycle
```

### Add Pump Runtime Tracking
```yaml
variables:
  pump_start: "{{ now() }}"

# Later...
- action: notify.persistent_notification
  data:
    message: "Pump ran for {{ (now() - pump_start).total_seconds() / 60 }} minutes"
```

## 🎯 Recommended Version

I recommend **Version 2 (With Variables)** because:
- ✅ Easy to tune timing values
- ✅ Clean and readable
- ✅ Not over-engineered
- ✅ Works with your existing setup

---

## Questions to Clarify

Before finalizing:

1. **What does your sensor detect?**
   - Water level too HIGH?
   - Water level too LOW?

2. **What should happen if pump runs too long?**
   - Add max runtime safety?
   - Send alert?

3. **Why the 25-minute delay when sensor goes off?**
   - Is this intentional or leftover from testing?

Let me know and I can adjust the automation!
