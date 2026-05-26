# Complete Installation Guide - Grow Lights with Transition

## Overview

This system controls your grow lights (light.chilled and light.hlg) with:
- **Vegetative mode:** 18 hours on (6pm-12pm)
- **Flower mode:** 12 hours on (6pm-6am)
- **Transition mode:** Automatic 6-day gradual reduction from 18hrs → 12hrs

## Step-by-Step Setup

### Step 1: Create/Update Helpers

Follow the instructions in **SETUP_HELPERS_UPDATED.md** to:

1. **Update** your existing Growth Stage helper to add "Transition" option
2. **Create** a new Transition Day Counter helper

**Result:** 6 helpers total (5 existing + 1 new)

### Step 2: Import Automations

You need to create **TWO** automations:

#### Automation 1: Grow Lights Controller

1. Go to **Settings** → **Automations & Scenes** → **Automations**
2. Click **+ Create Automation**
3. Click **⋮** (three dots) → **Edit in YAML**
4. Copy and paste contents of: `grow_lights_automation_v2.yaml`
5. Click **Save**
6. Name it: `Grow Lights Controller`

#### Automation 2: Transition Manager

1. Click **+ Create Automation** again
2. Click **⋮** (three dots) → **Edit in YAML**
3. Copy and paste contents of: `transition_manager_automation.yaml`
4. Click **Save**
5. Name it: `Transition Manager - Daily Light Adjustment`

### Step 3: Verify Setup

1. Go to **Settings** → **Automations & Scenes** → **Automations**
2. You should see both automations enabled:
   - ✅ Grow Lights Controller
   - ✅ Transition Manager - Daily Light Adjustment

## How to Use

### Normal Veg Mode

1. Set **Growth Stage** to `Vegetative`
2. Lights will run 18 hours (6pm to 12pm next day)
3. Adjust times as needed using the time helpers

### Starting Transition to Flower

When you see your plants are ready for flower:

1. Make sure **Veg Lights Off Time** is set to `12:00` (12pm)
2. Change **Growth Stage** to `Transition`
3. **That's it!** The system will automatically:
   - Day 1: 18 hours (6pm-12pm)
   - Day 2: 17 hours (6pm-11am) - adjusts at 12pm
   - Day 3: 16 hours (6pm-10am) - adjusts at 11am
   - Day 4: 15 hours (6pm-9am) - adjusts at 10am
   - Day 5: 14 hours (6pm-8am) - adjusts at 9am
   - Day 6: 13 hours (6pm-7am) - adjusts at 8am
   - Day 7: 12 hours (6pm-6am) - auto-switches to Flower!

### Full Flower Mode

- After transition completes, Growth Stage automatically changes to `Flower`
- Lights run 12 hours (6pm to 6am next day)
- Adjust flower times as needed using the time helpers

### Monitoring Transition Progress

- Check **Transition Day Counter** to see which day you're on (0-6)
- You'll receive notifications each day showing progress
- Final notification when transition completes

### Manual Control

If you need to manually override:
- Turn lights on/off manually - automation will resume at next check
- To cancel transition: Change Growth Stage back to Vegetative or Flower
- The transition counter will reset next time you start a transition

## Troubleshooting

**Lights not turning on/off:**
- Check that both automations are enabled
- Verify all helpers exist and have values
- Check automation traces in Settings → Automations

**Transition not working:**
- Make sure Growth Stage is set to "Transition"
- Verify Transition Manager automation is enabled
- Check that lights are actually turning off to trigger the adjustment

**Want to restart transition:**
- Set Growth Stage back to Vegetative
- Reset Veg Lights Off Time to 12:00
- Set Transition Day Counter to 0
- Change Growth Stage to Transition

## Files Reference

- `SETUP_HELPERS_UPDATED.md` - Helper creation instructions
- `grow_lights_automation_v2.yaml` - Main lights controller
- `transition_manager_automation.yaml` - Handles daily adjustments
- `PROJECT_STATUS.md` - Overall project tracking

---

**Questions?** Check PROJECT_STATUS.md for current status and next steps!
