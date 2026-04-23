# Home Assistant Tagging Standard

**Version:** v1 (2026-04-23)
**Scope:** Phase 1a + 1b — Tent garden (irrigation + climate + lighting). Extensible to all gardens and whole-home subsystems.
**Status:** Active. Phase 1a applied 2026-04-23. Phase 1b applied 2026-04-23.

## Purpose

A consistent, machine-targetable taxonomy for organizing every HA entity, device, automation, script, and helper across a multi-garden smart home. Enables:

- **Automation targeting** by `label_id` without brittle entity-ID patterns
- **Alert routing** by severity tier
- **Dashboard filtering** by subsystem / function / loop
- **Scalability** to additional gardens (Tower, Vegetable, etc.) and whole-home systems without re-architecting

## Decisions (locked)

| Decision | Choice |
|---|---|
| Per-garden model | One HA area per physical garden. Subsystems are **labels**, not areas. |
| Label style | Underscore-prefixed slugs (`sys_irrigation`). HA slugify collapses dashes/colons to `_`; underscores survive unchanged, so display name = `label_id`. |
| `sub_` scoping | **System-scoped** (`sub_irrigation_feed_loop`) to eliminate collisions across systems. |
| Severity tiers | 3: `sev_critical`, `sev_warning`, `sev_info`. |
| Categories | NOT used for entities. Reserved only for per-table UI grouping on Automations/Scripts/Scenes/Helpers list pages. |

## Label Taxonomy

### `sys_` — Top-level subsystem

One per entity (mandatory). Defines what the entity belongs to at the highest functional level.

| Label | Meaning |
|---|---|
| `sys_irrigation` | Water delivery + nutrients + flushing + drainage |
| `sys_climate` | Temp / humidity / airflow / CO2 / dehumidification |
| `sys_lighting` | Grow lights + schedules |
| `sys_power` *(reserved)* | Dedicated power delivery infrastructure (only when not subsumed by another sys). No tent entities use this — all tent Sonoffs are subsumed by their downstream system (HLG Sonoff → sys_lighting, etc.). |

*Phase 2+:* `sys_security`, `sys_camera`, `sys_hvac`, `sys_water`, `sys_network`, `sys_energy`, `sys_appliance`, `sys_printer`, `sys_access`, `sys_entertainment`

### `sub_` — Subsystem / loop / zone

Zero or one per entity. System-scoped: `sub_<sys>_<loop>` to avoid collisions when other systems are added.

| Label | Meaning |
|---|---|
| `sub_irrigation_feed_loop` | Feed reservoir + feed pump + feed-side plumbing |
| `sub_irrigation_flush_loop` | Flush reservoir + flush pump + flush-side plumbing |
| `sub_irrigation_drain_loop` | Table drain + drain pump + drain plumbing |
| `sub_irrigation_reservoir` | Reservoir-level utilities (prime pump, reservoir sensors) |
| `sub_climate_ac` | Air conditioner appliance (unit + its sensors + mode switches) |
| `sub_climate_humidifier` | Humidifier appliance (+ humidifier PWM fan on grow-tent-one ESP32) |
| `sub_climate_dehumidifier` | Dehumidifier appliance (+ tank / fan / child-lock controls) |
| `sub_climate_circulation` | Interior air-movement fans (circulation fans, AC circulation fan) |
| `sub_climate_exhaust` | Tent exhaust (duct fan) |
| `sub_climate_canopy` | Canopy-position BME280 sensor cluster (temp/humidity/pressure) |
| `sub_climate_flower` | Flower-position BME280 sensor cluster (temp/humidity/pressure) |
| `sub_climate_co2` | CO2 concentration monitor (+ raw ADC / corrected voltage) |

*Lighting has no `sub_` labels yet — only 2 fixtures (HLG, Chilled). Target by device or `fn_light` instead.*

### `fn_` — Function / type

One or more per entity. Describes **what the entity is** at the device/sensor level. Applied to entities, not automations/scripts/helpers.

| Label | Meaning |
|---|---|
| `fn_pump` | Any pump (feed, flush, stir, air, drain, prime) |
| `fn_valve` | Any valve (`valve` domain entities — solenoids etc.) |
| `fn_controller` | Device-level control entity (ESP32 controllers, smart-plug switches, power strips) |
| `fn_power_meter` | Energy/voltage/current/consumption telemetry |
| `fn_sensor_level` | Liquid-level sensors (continuous or discrete/float) |
| `fn_sensor_pressure` | Pressure sensors |
| `fn_sensor_flow` | Flow rate / total flow |
| `fn_sensor_temp` | Temperature sensors |
| `fn_sensor_humidity` | Humidity sensors |
| `fn_sensor_co2` | CO2 sensors |
| `fn_fan` | Any fan (circulation, exhaust, fresh-air, PWM, dehumidifier fan-swing) |
| `fn_light` | Grow-light fixtures (HA `light` domain entities) |
| `fn_climate` | Climate-control appliances (AC, humidifier, dehumidifier as a unit) |
| `fn_sensor_ec` *(reserved)* | EC / TDS |
| `fn_sensor_ph` *(reserved)* | pH |

### `sev_` — Severity / alert tier

Exactly one per entity (mandatory). Used for alert routing and dashboard prioritization.

| Tier | When to use |
|---|---|
| `sev_critical` | Failure = plant death, flood, fire risk, missed feed, or system unrecoverable without intervention. Pages / pushes alerts. |
| `sev_warning` | Failure = degraded performance, off-schedule behavior, or recoverable condition. Notifies but doesn't page. |
| `sev_info` | Telemetry / scheduling / helpers / informational. Dashboard-only; no alerts. |

### Cross-cutting (optional)

| Label | Meaning |
|---|---|
| `grow` | Marks entities belonging to the grow operation across every garden. Applied to every `sys_irrigation` / `sys_climate` / `sys_lighting` entity in phase 1a+1b. Enables a master grow dashboard spanning Tent + future Tower + Vegetable. |

## Required labels per entity

- **Exactly one** `sys_`
- **At most one** `sub_` (only when the entity is scoped to a specific loop/zone)
- **One or more** `fn_` (for entities; skip for automations/scripts/helpers)
- **Exactly one** `sev_`

### Exception — aggregated / template sensors

Template sensors that compute a derived value from multiple inputs (e.g. VPD from temp+humidity, DLI from light-accumulation, an overall "status" string) don't map cleanly to a single `fn_sensor_*` physical-quantity bucket. For these, `fn_` is **not required** — the `sys_` + `sev_` pair is sufficient. Documented examples:

- `sensor.grow_tent_vpd` (sys_climate + sev_info)
- `sensor.grow_tent_dli` (sys_lighting + sev_info)
- `sensor.grow_tent_status` (sys_climate + sev_info)

If a new aggregate fits an existing physical bucket (e.g. `fn_sensor_humidity` for an averaged humidity), prefer that bucket over skipping `fn_`.

## Automations / scripts / scenes / helpers

Same taxonomy minus `fn_`. Apply `sys_`, `sub_` (if loop-scoped), and `sev_` based on safety impact:

- Watchdog / safety-lock / emergency-kill → `sev_critical`
- Alert / notification → match the underlying condition's severity (usually `sev_critical` or `sev_warning`)
- Scheduler / setup / transition → `sev_info`

## Severity triage — worked examples

| Entity | Severity | Why |
|---|---|---|
| Feed pump switch | `sev_critical` | Pump failure = plants dry out |
| Feed-stir pump switch | `sev_warning` | Mixing important but not immediately fatal |
| Post-regulator pressure sensor | `sev_critical` | Sudden pressure drop = burst or leak |
| Feed-tank empty binary sensor | `sev_critical` | Must block the feed cycle |
| Feed-tank half-full binary sensor | `sev_info` | Status indicator, not actionable |
| Flow-rate sensor | `sev_warning` | Deviation is important but not catastrophic |
| Flow-total sensor | `sev_info` | Telemetry |
| Irrigation watchdog automation | `sev_critical` | Catches cascading failures |
| HLG / Chilled grow light | `sev_critical` | Photoperiod failure stresses plants |
| AC unit + power switch | `sev_critical` | Cooling failure = heat damage |
| Dehumidifier power | `sev_critical` | Humidity runaway = mold risk |
| Humidifier power | `sev_critical` | Failure = plants dessicate in flower |
| Circulation / exhaust / fresh-air fan | `sev_warning` | Stagnant air degrades conditions but isn't instant death |
| Canopy / flower temp+humidity | `sev_warning` | Feeds climate control — deviation matters |
| CO2 concentration | `sev_warning` | Supplementation/monitoring — off-target is recoverable |
| Power-meter telemetry (current/voltage/power, RSSI, energy totals) | `sev_info` | Monitoring-only |
| Safety flower-night humidifier shutoff automation | `sev_critical` | Prevents bud mold |
| Light schedule / transition automations | `sev_info` | Scheduling logic |

## Area vs label decision tree

1. **Is it a physical location?** → **Area.** One per garden (`Tent`, future: `Tower`, `Vegetable`, etc.) + whole-home areas.
2. **Is it about what the entity IS (pump, valve, sensor)?** → `fn_` label.
3. **Is it about what subsystem the entity belongs to?** → `sys_` label.
4. **Is it about what loop/zone within a subsystem?** → `sub_` label.
5. **Is it about alert severity?** → `sev_` label.

Areas **never** duplicate system/function semantics. A label never encodes physical location.

## Per-garden scaling

Adding a new garden (e.g. Tower):

1. Create HA area `Tower`.
2. All Tower entities/devices get area `Tower` + the same `sys_/sub_/fn_/sev_` taxonomy.
3. `sub_` labels stay system-scoped and are reused (e.g. Tower's feed loop is also `sub_irrigation_feed_loop` — that label now spans multiple gardens).
4. An automation targeting `[sys_irrigation, fn_pump]` auto-scales: it fires every irrigation pump in every garden. To scope to one garden, combine label target with `area_id` target.

## Whole-home expansion (phase 3+)

Same rules. Create new `sys_*` labels per subsystem (security, camera, HVAC, etc.); add new `sub_<sys>_*` as needed; reuse the `fn_*` and `sev_*` tiers.

## Historical note

### Phase 1a — 2026-04-23 (irrigation)

Prior to 2026-04-23, Tent entities were split across two areas: `tent` and `tent_irrigation`. The split abused areas for logical grouping and didn't generalize to additional gardens. The 2026-04-23 phase 1a migration:

- Moved all `tent_irrigation` entities + devices into `tent`
- Deleted the `tent_irrigation` area
- Replaced the flat `irrigation_tent` label with the full `sys_/sub_/fn_/sev_` taxonomy on 129 entities
- Deleted the `irrigation_tent` label

Pre-1a snapshot: `Container Home/migration_snapshots/20260423-011358Z_pre-tagging-migration/`
Post-1a snapshot: `Container Home/migration_snapshots/20260423-015033Z_post-phase1a/`

### Phase 1b — 2026-04-23 (climate / lighting + grow master label)

The same day, phase 1b expanded the taxonomy to climate and lighting:

- Created 16 new labels: `sys_climate`, `sys_lighting`, 8 × `sub_climate_*`, `fn_fan`, `fn_light`, `fn_climate`, `fn_sensor_humidity`, `fn_sensor_co2`, `grow`
- Tagged 149 climate/lighting/residual-irrigation entities (AC, humidifier, dehumidifier, circulation/exhaust/fresh-air fans, HLG + Chilled lights, canopy + flower BME280, CO2 sensor, Tent Controller Sonoff, KP303 ancillaries, Kasa outdoor-plug outlets, light/climate input helpers, climate/lighting automations)
- Added retroactive `grow` label to every phase-1a `sys_irrigation` entity (277 entities total carry `grow` post-1b)
- Stripped and deleted 7 superseded labels: `tent`, `fans_tent`, `lights_tent`, `ac_tent`, `humidifier_tent`, `air_quality_tent`, `controller`

Pre-1b snapshot: `Container Home/migration_snapshots/20260423-015715Z_pre-phase1b/`
Post-1b snapshot: `Container Home/migration_snapshots/20260423-050316Z_post-phase1b/`

### Deferred after phase 1b

- **Camera Tent** device (7 entities: `camera.tent`, `binary_sensor.motion_camera_tent`, `binary_sensor.battery_camera_tent`, `binary_sensor.tent_camera_armed`, `switch.motion_detection_camera_tent`, `sensor.temperature_camera_tent`, `sensor.wi_fi_signal_strength_camera_tent`) → phase 2 (`sys_camera` / `sys_security`).
- **Grow Tent Two ESP32 plant/flood moisture sensors** (22 entities: `sensor.grow_tent_two_plant_{1..9}_{volts,moisture}`, `sensor.grow_tent_two_flood_{1..4}_{volts,moisture}`) → reserved for future irrigation hardware; tag when wired to `sys_irrigation` with `fn_sensor_level`.
- **Not currently in use** (user confirmed 2026-04-23 — leave untagged until they come into use): `switch.blank_2` (Kasa reservoir prime pump 2-outlet, second outlet), `switch.humidifier_2` (second entity on Humidifier device), `switch.grow_tent_one_extra_relay` (spare relay on grow-tent-one ESP32).
- **Kasa outdoor plug outlets** (`switch.kasa_smart_outdoor_plug_switch_1/2`) — not in use. Phase 1b tagged them `sys_irrigation` + `fn_controller` + `sev_warning` based on the device name ("Irrigation Multi - Plug"); re-evaluate labels/severity when they come into use.
- **Whole-home labels** (`3d_printer`, `pc`, `camera`, `electricity`, `outside`, `battery`, `wi_fi`, `power_switch`, `bambu`, `phone`, `firmware`) remain unchanged — phase 2+ scope.

## Tooling

- `Container Home/tag_migration_phase1a.py` — phase 1a migrator (irrigation): creates labels, moves `tent_irrigation` → `tent` area, tags entities, deletes old labels/areas. Idempotent. Dry-run default; `--apply` commits.
- `Container Home/tag_migration_phase1b.py` — phase 1b migrator (climate/lighting + residual-irrigation ancillaries + `grow`): creates the climate/lighting labels, tags entities, retroactively adds `grow` to phase-1a entities, strips and deletes 7 superseded labels. Idempotent. Dry-run default; `--apply` commits.
- `Container Home/registry_export.py` — snapshots all 4 registries as JSON under `migration_snapshots/<timestamp>[_label]/`. Run before every migration.
- `Container Home/area_labeler.py` — legacy one-shot for the pre-2026-04-23 tent/tent_irrigation split. Superseded by `tag_migration_phase1a.py`.
