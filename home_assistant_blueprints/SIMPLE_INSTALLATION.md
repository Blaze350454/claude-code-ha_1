# Simple Installation Guide - No Counter Needed!

## What You Need

**5 Helpers** (you already have these):
1. Growth Stage (dropdown) - `input_select.growth_stage`
2. Veg Lights On Time - `input_datetime.veg_lights_on_time`
3. Veg Lights Off Time - `input_datetime.veg_lights_off_time`
4. Flower Lights On Time - `input_datetime.flower_lights_on_time`
5. Flower Lights Off Time - `input_datetime.flower_lights_off_time`

## Step 1: Update Growth Stage Helper

Add "Transition" option:

1. Go to **Settings** → **Devices & Services** → **Helpers**
2. Find **Growth Stage** (`input_select.growth_stage`)
3. Click on it → Click the gear icon or **Edit**
4. Add third option: `Transition`
5. Your options should be:
   - Vegetative
   - Transition
   - Flower
6. Click **Update**

## Step 2: Install the Automation

1. Open file: `grow_lights_SIMPLE.yaml`
2. Copy **ALL** contents
3. In Home Assistant: **Settings** → **Automations & Scenes** → **Automations**
4. Click **+ Create Automation**
5. Click **⋮** (three dots, top right) → **Edit in YAML**
6. **Delete everything** in the editor
7. **Paste** the automation YAML
8. Click **Save**
9. Name it: `Grow Lights Controller`

**Done!**

## How It Works

### Veg Mode
- Set Growth Stage to `Vegetative`
- Lights: 6pm-12pm (18 hours)

### Transition Mode
- When ready: Change Growth Stage to `Transition`
- Each day when lights turn off, the off time moves 1 hour earlier
- Automatically switches to Flower when it reaches 12/12

### Flower Mode
- Automatically enabled after transition completes
- Lights: 6pm-6am (12 hours)

## Transition Example

Starting schedule: 6pm-12pm (18 hours)
- Day 1: 6pm-12pm → Lights turn off at 12pm, schedule adjusts
- Day 2: 6pm-11am → Lights turn off at 11am, schedule adjusts
- Day 3: 6pm-10am → Lights turn off at 10am, schedule adjusts
- Day 4: 6pm-9am → Lights turn off at 9am, schedule adjusts
- Day 5: 6pm-8am → Lights turn off at 8am, schedule adjusts
- Day 6: 6pm-7am → Lights turn off at 7am, schedule adjusts
- Day 7: 6pm-6am → Target reached! Auto-switches to Flower mode

## Notifications

You'll receive notifications:
- Each day showing the new schedule and days remaining
- When transition completes

## Troubleshooting

**Lights not responding:**
- Check automation is enabled
- Verify all 5 helpers exist with values
- View automation trace: Click automation → ⋮ → **Traces**

**Transition not working:**
- Ensure Growth Stage = "Transition"
- Verify both lights actually turn off
- Check that veg off time is later than flower off time

**Restart transition:**
- Set Growth Stage to Vegetative
- Set Veg Lights Off Time back to 12:00
- Change Growth Stage to Transition

---

**This version is simpler - no extra helpers needed!**
