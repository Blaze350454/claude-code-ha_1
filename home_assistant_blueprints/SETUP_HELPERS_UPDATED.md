# Setting Up Home Assistant Helpers (WITH TRANSITION)

## Updates Needed

### 1. Update Growth Stage Helper

You already created this, but we need to add the "Transition" option:

1. Go to **Settings** → **Devices & Services** → **Helpers**
2. Find **Growth Stage** (`input_select.growth_stage`)
3. Click on it
4. Click **⚙️ Settings** or **Edit**
5. In the **Options** section, add a third option:
   - `Transition`
6. So your options should now be:
   - Vegetative
   - Transition
   - Flower
7. Click **Update**

### 2. Create Transition Day Counter (NEW)

This tracks which day of the transition you're on (0-6).

1. Click **+ CREATE HELPER**
2. Select **Number**
3. Configure:
   - **Name:** `Transition Day Counter`
   - **Icon:** `mdi:counter`
   - **Minimum:** `0`
   - **Maximum:** `6`
   - **Step:** `1`
   - **Mode:** `Box`
   - **Unit of measurement:** (leave empty)
4. Click **CREATE**
5. After creation, set initial value to `0`

**Result:** Entity ID will be `input_number.transition_day_counter`

## Summary of All Helpers

After these updates, you should have:

| Helper Name | Entity ID | Type | Value/Options |
|-------------|-----------|------|---------------|
| Growth Stage | `input_select.growth_stage` | Dropdown | Vegetative / Transition / Flower |
| Transition Day Counter | `input_number.transition_day_counter` | Number | 0-6 |
| Veg Lights On Time | `input_datetime.veg_lights_on_time` | Time | 18:00 (6 PM) |
| Veg Lights Off Time | `input_datetime.veg_lights_off_time` | Time | 12:00 (12 PM) |
| Flower Lights On Time | `input_datetime.flower_lights_on_time` | Time | 18:00 (6 PM) |
| Flower Lights Off Time | `input_datetime.flower_lights_off_time` | Time | 06:00 (6 AM) |

## How Transition Works

1. **When you're ready to transition:** Change Growth Stage to "Transition"
2. **Each day when lights turn off:** The off time automatically moves 1 hour earlier
3. **After 6 days:** Growth Stage automatically switches to "Flower" at 12/12 schedule
4. **The counter tracks progress:** You can see which day of transition you're on

---

**Next:** Complete these helper updates, then we'll install the updated automations!
