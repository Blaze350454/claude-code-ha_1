# Grow Room Automation System

A modular Home Assistant automation system for controlling grow room equipment with shared schedules.

## Quick Start

### 1. Set Up Helpers (First Time Only)
Follow the instructions in **SETUP_HELPERS.md** to create the required helper entities in Home Assistant.

### 2. Import Blueprint
1. Copy `grow_lights_blueprint.yaml` content
2. In Home Assistant, go to **Settings** → **Automations & Scenes** → **Blueprints**
3. Click **Import Blueprint**
4. Paste the YAML content
5. Click **Preview** then **Import**

### 3. Create Automation
1. Go to **Settings** → **Automations & Scenes** → **Automations**
2. Click **+ Create Automation** → **Use Blueprint**
3. Select "Grow Room Lights Controller"
4. Configure:
   - **Chilled Light:** `light.chilled`
   - **HLG Light:** `light.hlg`
   - Leave other fields at defaults (they'll use the helpers you created)
5. Name it "Grow Lights" and save

## How It Works

### Shared Schedule System
All equipment references the same schedule helpers:
- Change the growth stage → all equipment switches modes
- Adjust veg/flower times → all equipment uses new times
- Easy transitions between growth cycles

### Current Schedules

**Vegetative Cycle:**
- Lights ON: 6:00 PM
- Lights OFF: 12:00 PM (next day)
- Duration: 18 hours

**Flower Cycle:**
- Lights ON: 6:00 PM
- Lights OFF: 6:00 AM (next day)
- Duration: 12 hours

### Adjusting Schedules
1. Go to **Settings** → **Devices & Services** → **Helpers**
2. Find the time helper you want to adjust
3. Click on it and change the time
4. All automations update automatically

### Switching Growth Stages
1. Find the "Growth Stage" helper in your dashboard or Helpers page
2. Change from "Vegetative" to "Flower" (or vice versa)
3. All equipment automatically switches to the new schedule

## Project Structure

```
home_assistant_blueprints/
├── PROJECT_STATUS.md          # Track progress and decisions
├── SETUP_HELPERS.md           # Helper setup instructions
├── grow_lights_blueprint.yaml # Lights control blueprint
└── README.md                  # This file
```

## Equipment

### Current
- **Lights:** light.chilled, light.hlg

### Planned
- Fans
- AC
- Dehumidifier
- Temperature control

## Adding More Equipment Blueprints

Each new blueprint will:
1. Reference the same growth stage selector
2. Reference the same time helpers
3. Work independently but in sync with other equipment

## Home Assistant Instance
- **URL:** http://192.168.2.151:8123
- **Backup Key:** See parent directory

## Support Files
- See **PROJECT_STATUS.md** for current development progress
- See **SETUP_HELPERS.md** for helper configuration details

---

*For questions or issues, check PROJECT_STATUS.md for current status and next steps.*
