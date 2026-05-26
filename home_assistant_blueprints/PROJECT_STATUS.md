# Grow Room Automation Project

## Current Status
**Status:** Architecture Defined - Building Components
**Last Updated:** 2025-12-29
**Home Assistant Instance:** http://192.168.2.151:8123

## Project Overview
Building a modular grow room automation system with shared schedules and separate blueprints for each equipment type.

## Architecture Decision ✅
**Approach:** Separate blueprints + shared schedule helpers

**Benefits:**
- Change schedule times once, affects all equipment
- Easy to adjust during veg/flower transitions
- Each system (lights, fans, AC, etc.) can be maintained independently
- Can test and troubleshoot individual systems
- Professional, scalable approach

## Equipment List

### Lights
- `light.chilled`
- `light.hlg`

### Other Equipment (Future)
- Fans (to be documented)
- AC (to be documented)
- Dehumidifier (to be documented)
- Temperature control (to be documented)

## Growth Schedules

### Veg Cycle
- **Lights ON:** 6:00 PM
- **Lights OFF:** 12:00 PM (next day)
- **Duration:** 18 hours on / 6 hours off

### Flower Cycle
- **Lights ON:** 6:00 PM
- **Lights OFF:** 6:00 AM (next day)
- **Duration:** 12 hours on / 12 hours off

## Progress Tracker

### Phase 1: Core Infrastructure ✅
- [x] Define architecture approach
- [x] Document equipment and schedules
- [x] Create input_datetime helpers in Home Assistant
- [x] Create input_select helper for growth stage (veg/flower/transition)
- [x] Create transition day counter helper

### Phase 2: Lights Automation ✅
- [x] Create lights automation YAML with transition support
- [x] Create transition manager automation
- [ ] Install both automations in Home Assistant
- [ ] Test veg mode
- [ ] Test transition mode
- [ ] Test flower mode

### Phase 3: Additional Equipment Automations
- [ ] Fans automation
- [ ] AC automation
- [ ] Dehumidifier automation
- [ ] Temperature control automation

### Phase 4: Advanced Features
- [x] Transition mode automation (automatic 1hr/day reduction)
- [x] Alerts/notifications (built into transition manager)
- [ ] Dashboard cards
- [ ] Manual override switches

## Files in This Project
- `PROJECT_STATUS.md` - This file (tracks progress and decisions)
- `SETUP_HELPERS.md` - Instructions for creating helpers in HA
- `grow_lights_blueprint.yaml` - Lights control blueprint
- `README.md` - Overall project documentation

## Next Steps
1. Create the required helpers in Home Assistant (see SETUP_HELPERS.md)
2. Build the lights blueprint
3. Test and refine
4. Build additional equipment blueprints as needed

---
*Use this file to track progress between sessions with Claude*
