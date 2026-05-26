# Setting Up Home Assistant Helpers

Before using the blueprints, you need to create helper entities in Home Assistant. These helpers store your schedule times and growth stage, allowing all blueprints to reference the same values.

## Step-by-Step Setup

### 1. Access Helpers in Home Assistant

1. Open your Home Assistant: http://192.168.2.151:8123
2. Go to **Settings** → **Devices & Services** → **Helpers** tab
3. Click **+ CREATE HELPER** button

### 2. Create Growth Stage Selector

**Helper Type:** Dropdown

- Click **+ CREATE HELPER**
- Select **Dropdown**
- Configure:
  - **Name:** `Growth Stage`
  - **Icon:** `mdi:sprout` (or `mdi:cannabis`)
  - **Options:** (Add these two options)
    - `Vegetative`
    - `Flower`
- Click **CREATE**

**Result:** Entity ID will be `input_select.growth_stage`

### 3. Create Time Helpers (4 total)

You need to create 4 time helpers for your schedules.

#### Helper 1: Veg Lights On Time
- Click **+ CREATE HELPER**
- Select **Date and/or time**
- Configure:
  - **Name:** `Veg Lights On Time`
  - **Icon:** `mdi:weather-sunset-up`
  - **Has date:** ❌ (unchecked)
  - **Has time:** ✅ (checked)
- Click **CREATE**
- After creation, set the time to **18:00** (6:00 PM)

**Result:** Entity ID will be `input_datetime.veg_lights_on_time`

#### Helper 2: Veg Lights Off Time
- Click **+ CREATE HELPER**
- Select **Date and/or time**
- Configure:
  - **Name:** `Veg Lights Off Time`
  - **Icon:** `mdi:weather-sunset-down`
  - **Has date:** ❌ (unchecked)
  - **Has time:** ✅ (checked)
- Click **CREATE**
- After creation, set the time to **12:00** (12:00 PM)

**Result:** Entity ID will be `input_datetime.veg_lights_off_time`

#### Helper 3: Flower Lights On Time
- Click **+ CREATE HELPER**
- Select **Date and/or time**
- Configure:
  - **Name:** `Flower Lights On Time`
  - **Icon:** `mdi:weather-sunset-up`
  - **Has date:** ❌ (unchecked)
  - **Has time:** ✅ (checked)
- Click **CREATE**
- After creation, set the time to **18:00** (6:00 PM)

**Result:** Entity ID will be `input_datetime.flower_lights_on_time`

#### Helper 4: Flower Lights Off Time
- Click **+ CREATE HELPER**
- Select **Date and/or time**
- Configure:
  - **Name:** `Flower Lights Off Time`
  - **Icon:** `mdi:weather-sunset-down`
  - **Has date:** ❌ (unchecked)
  - **Has time:** ✅ (checked)
- Click **CREATE**
- After creation, set the time to **06:00** (6:00 AM)

**Result:** Entity ID will be `input_datetime.flower_lights_off_time`

## Summary of Created Helpers

After completing these steps, you should have these 5 helpers:

| Helper Name | Entity ID | Type | Initial Value |
|-------------|-----------|------|---------------|
| Growth Stage | `input_select.growth_stage` | Dropdown | Vegetative or Flower |
| Veg Lights On Time | `input_datetime.veg_lights_on_time` | Time | 18:00 (6 PM) |
| Veg Lights Off Time | `input_datetime.veg_lights_off_time` | Time | 12:00 (12 PM) |
| Flower Lights On Time | `input_datetime.flower_lights_on_time` | Time | 18:00 (6 PM) |
| Flower Lights Off Time | `input_datetime.flower_lights_off_time` | Time | 06:00 (6 AM) |

## How This Works

1. The **Growth Stage** dropdown lets you switch between Veg and Flower cycles
2. The **time helpers** store your on/off times for each cycle
3. All blueprints (lights, fans, AC, etc.) will reference these helpers
4. When you change a time or growth stage, ALL automations update automatically
5. During transitions, just adjust the times gradually - no need to edit multiple automations

## Next Steps

Once these helpers are created, you can:
1. Install the grow lights blueprint
2. Create an automation from the blueprint
3. The automation will automatically use these helpers

---

**Note:** You can adjust these times anytime from the Helpers page or add them to your dashboard for quick access!
