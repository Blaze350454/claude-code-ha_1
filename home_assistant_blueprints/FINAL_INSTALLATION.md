# Final Installation Guide - Unified Automation

## What You're Installing

**ONE automation** that handles everything:
- Light control for both lights (light.chilled & light.hlg)
- Veg mode (18 hours)
- Flower mode (12 hours)
- Automatic transition (reduces 1 hour/day for 6 days)
- Notifications during transition

## Step 1: Update/Create Helpers

### Update Existing Helper
1. Go to **Settings** → **Devices & Services** → **Helpers**
2. Find **Growth Stage** (`input_select.growth_stage`)
3. Click on it → **⚙️ Edit**
4. Add third option: `Transition`
5. Options should be:
   - Vegetative
   - Transition
   - Flower
6. Click **Update**

### Create New Helper
1. Click **+ CREATE HELPER**
2. Select **Number**
3. Configure:
   - Name: `Transition Day Counter`
   - Icon: `mdi:counter`
   - Minimum: `0`
   - Maximum: `6`
   - Step: `1`
4. Click **CREATE**

## Step 2: Install the Automation

**Use the direct automation file** (easiest method):

1. Open file: `grow_lights_DIRECT_AUTOMATION.yaml`
2. Copy **ALL** contents (lines 1-189)
3. In Home Assistant: **Settings** → **Automations & Scenes** → **Automations**
4. Click **+ Create Automation**
5. Click **⋮** (three dots, top right) → **Edit in YAML**
6. **Delete everything** in the editor
7. **Paste** the automation YAML you copied
8. Click **Save**
9. Name it: `Grow Lights Controller`

**Done!** You now have ONE automation that does everything.

## Step 3: Verify Setup

1. Go to **Settings** → **Automations & Scenes** → **Automations**
2. You should see: ✅ **Grow Lights Controller**
3. Make sure it's **enabled** (toggle on)

## How to Use

### Vegetative Mode
1. Set **Growth Stage** to `Vegetative`
2. Lights run 18 hours (6pm-12pm next day)
3. Adjust times anytime via the time helpers

### Starting Transition
When your plants are ready for flower:
1. Make sure **Veg Lights Off Time** is `12:00` (noon)
2. Change **Growth Stage** to `Transition`
3. **That's it!** The system automatically:
   - Day 1: 18hrs (6pm-12pm)
   - Day 2: 17hrs (6pm-11am) - adjusts when lights turn off
   - Day 3: 16hrs (6pm-10am)
   - Day 4: 15hrs (6pm-9am)
   - Day 5: 14hrs (6pm-8am)
   - Day 6: 13hrs (6pm-7am)
   - Day 7: 12hrs (6pm-6am) - **auto-switches to Flower!**

### Flower Mode
- After transition, Growth Stage automatically becomes `Flower`
- Lights run 12 hours (6pm-6am)

### Monitoring
- Check **Transition Day Counter** to see progress (0-6)
- You'll get notifications each day
- Final notification when complete

## Troubleshooting

**Lights not responding:**
- Check automation is enabled
- Verify all 6 helpers exist and have values
- Check automation trace: Click automation → ⋮ → **Traces**

**Transition not working:**
- Ensure Growth Stage is set to "Transition"
- Verify both lights are actually turning off
- Check Transition Day Counter isn't already at 6

**Need to restart transition:**
- Set Growth Stage to Vegetative
- Set Veg Lights Off Time to 12:00
- Set Transition Day Counter to 0
- Change Growth Stage to Transition

## Files Reference

- `grow_lights_DIRECT_AUTOMATION.yaml` ← **Use this file to import**
- `grow_lights_unified_blueprint.yaml` ← Blueprint version (for future use)
- `SETUP_HELPERS_UPDATED.md` ← Helper setup details
- `PROJECT_STATUS.md` ← Overall project tracking

---

**Questions?** Check PROJECT_STATUS.md or come back to Claude!
