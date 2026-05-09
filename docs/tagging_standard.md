# Home Assistant Tagging Standard

**Version:** v1 (2026-04-23)
**Scope:** Phases 1a + 1b + 1c + 1d (Tent garden — irrigation + climate + lighting + helper cleanup), Phase 3d (3D printer), Phase 2 (Blink cameras — whole home). Extensible to remaining whole-home subsystems.
**Status:** Active. Phases 1a/1b/1c/1d/3d/2 all applied 2026-04-23.

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
| `sys_printer` | 3D printers + their Kasa power outlets + integration/spool/camera entities. Applied phase 3d. |
| `sys_camera` | Whole-home surveillance cameras (Blink + future doorbells) + their motion/battery/temp/signal sensors + motion-detection switches + Blink sync-module alarm panels. Applied phase 2. |

*Future:* `sys_security`, `sys_hvac`, `sys_water`, `sys_network`, `sys_energy`, `sys_appliance`, `sys_access`, `sys_entertainment`

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
| `sub_camera_indoor` | Cameras + sync module installed inside the house (bath room, bedroom, hall, kitchen, tent-cam — tent treated as indoor since enclosed) |
| `sub_camera_outdoor` | Cameras installed outside (back door, front, front door, front driveway, garage, garden, water side) |

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
| `fn_camera` | Camera entities + their enable/image-sensor switches. Applied phase 3d to the Bambu P1S chamber cam; will extend to tent-cam in phase 2. |
| `fn_sensor_status` | Diagnostic / status / error sensors that report a printer/device state string or error flag rather than a physical quantity (e.g. `binary_sensor.hms_errors_p1s`, `sensor.print_status_p1s`, `update.firmware_*`, `binary_sensor.*_camera_armed`). Applied phase 3d + phase 2. |
| `fn_sensor_motion` | PIR / motion binary sensors (applied phase 2 to all 12 Blink cameras). |
| `fn_sensor_battery` | Battery level / low-battery binary sensors. Applied phase 2. |
| `fn_sensor_signal` | Wi-Fi / RF signal strength sensors (Blink cams + bambu wifi). Applied phase 2. |
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
| `bambu` | Brand/vendor tag for Bambu Lab 3D printer entities (P1S + Bambu Lab integration + Kasa `switch.bambu`). Lets automations target one printer when multiple brands are present. |
| `prusa` | Brand/vendor tag for Prusa 3D printer entities. Currently only the Kasa outlet (`switch.prusa`) + its power-meter siblings — printer not yet wired. Reserved so entities land correctly when hardware comes online. |
| `blink` | Brand/vendor tag for Blink camera entities (all 12 cams + 2 sync modules). Lets automations scope to Blink when future doorbells or other brands land. |

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

- ~~**Camera Tent** device — deferred after 1b.~~ Resolved in phase 2 (2026-04-23) with `sys_camera` + `sub_camera_indoor` + `blink` + `grow`.
- **Grow Tent Two ESP32 plant/flood moisture sensors** (22 entities: `sensor.grow_tent_two_plant_{1..9}_{volts,moisture}`, `sensor.grow_tent_two_flood_{1..4}_{volts,moisture}`) → reserved for future irrigation hardware; tag when wired to `sys_irrigation` with `fn_sensor_level`.
- **Not currently in use** (user confirmed 2026-04-23 — leave untagged until they come into use): `switch.blank_2` (Kasa reservoir prime pump 2-outlet, second outlet), `switch.grow_tent_one_extra_relay` (spare relay on grow-tent-one ESP32). (Note: `switch.humidifier_2` was on this list but brought into the climate/humidifier scope on 2026-05-09 — now `switch.tent_humidifier_2`, tagged `sys_climate/sub_climate_humidifier/fn_controller/sev_warning/grow`.)
- **Kasa outdoor plug outlets** (`switch.kasa_smart_outdoor_plug_switch_1/2`) — not in use. Phase 1b tagged them `sys_irrigation` + `fn_controller` + `sev_warning` based on the device name ("Irrigation Multi - Plug"); re-evaluate labels/severity when they come into use.
- **Whole-home legacy labels** — many superseded during phases 2 / 3d:
  - `3d_printer` → deleted in phase 3d (replaced by `sys_printer`).
  - `camera` → deleted in phase 2 (replaced by `sys_camera` + `fn_camera`).
  - `wi_fi` → deleted in phase 2 (replaced by `fn_sensor_signal`).
  - `battery` → still alive, used by 2 phone entities; will be replaced by `fn_sensor_battery` when phone scope is tagged in a future phase.
  - Remaining legacy (`pc`, `electricity`, `outside`, `power_switch`, `phone`, `firmware`) — re-evaluated per future sub-phase.

### Phase 1c / 1d — 2026-04-23 (helper / AC-subcontrol cleanup)

Same day, two residual passes brought the tent-scope invariants to 100 % green:

- **Phase 1c (21 stragglers):** 11 irrigation helpers (`input_boolean.feed_cycle_*`, flush-related, watering helpers), 8 climate automations/helpers, 2 lighting helpers that were missed in 1a/1b. Additive label merge; full `sys_/sev_/grow` triple applied per helper rules.
- **Phase 1d (23 AC/dehumidifier sub-controls):** per-appliance helpers under `sub_climate_ac` / `sub_climate_dehumidifier` that expose mode/fan/swing/child-lock/buzzer/light toggles. One entity (`binary_sensor.full_dust_air_conditioner_tent`) was special-cased because it already had `sev_warning` — avoided a double-`sev_` merge conflict.

After 1d, the 5 tent invariants hold across all 297 tent-scope entities: exactly one `sys_`, exactly one `sev_`, `grow` on every entity, `fn_` on every non-helper (except the 3 documented aggregated template sensors), no `fn_` on helpers.

Post-1c snapshot: `Container Home/migration_snapshots/20260423-0*Z_post-phase1c/`
Post-1d snapshot: `Container Home/migration_snapshots/20260423-0*Z_post-phase1d/`

### Phase 3d — 2026-04-23 (3D printer)

First whole-home sub-phase applied. Brought the Bambu P1S and its Kasa + integration + spool + camera + automation entities under `sys_printer` with brand tags:

- Created 4 new labels: `sys_printer`, `fn_camera`, `fn_sensor_status`, `prusa`.
- Tagged 69 entities: 60 Bambu P1S entities, 2 Bambu Lab integration entities, 2 External Spool entities, `switch.bambu` + `update.firmware_2_p1s` (Kasa main power + firmware), and 4 Prusa Kasa entities (`switch.prusa`, current/power/voltage). Also re-tagged 2 automations (`automation.bambu_light_on_power`, `automation.bambu_turn_off_after_print`).
- Moved the Bambu Lab integration device into area `3d_printer` so its entities inherit area via device (the 60 P1S entities already had area from their device).
- Deleted the legacy `3d_printer` label (redundant with `sys_printer`). Stripped `camera` from the 3 printer cam entities only (`camera.camera_p1s`, `switch.enable_camera_p1s`, `switch.use_image_sensor_camera_p1s`) — the `camera` label is kept alive for the phase-2 tent-cam entities.

Printer-scope severity rules:
- Print controls (pause/resume/stop buttons, main Kasa outlet `switch.bambu`) → `sev_critical` (failure = print damage / fire risk).
- Error sensors (`binary_sensor.hms_errors_p1s`, `binary_sensor.print_error_p1s`) → `sev_critical` + `fn_sensor_status`.
- Bed / nozzle actual temps → `sev_warning` + `fn_sensor_temp` (runaway = fire).
- Bed / nozzle target/setpoint (`number.*_target_temperature_p1s`) → `sev_warning` + `fn_controller` (wrong setpoint = damage).
- Heatbreak fan → `sev_warning` + `fn_fan`; cooling fan → `sev_info` + `fn_fan`.
- Chamber light → `sev_info` + `fn_light`. Camera + enable/image-sensor switches → `sev_info` + `fn_camera`.
- Online sensor + firmware update → `sev_warning` + `fn_sensor_status`. Other telemetry (fall back) → `sev_info` + `fn_sensor_status`.
- Prusa Kasa switch → `sev_critical` + `fn_controller`; Prusa current/power/voltage → `sev_info` + `fn_power_meter`.

Post-3d-printer snapshot: `Container Home/migration_snapshots/20260423-182956Z_post-phase3-printer/` (785 entities, 47 labels).

### Phase 2 — 2026-04-23 (Blink cameras, whole-home)

First phase-2 / cross-location rollout. Tagged every Blink-platform entity in HA (12 cameras + 2 sync-module alarm panels + 72 per-camera sensors/switches):

- Created 7 new labels: `sys_camera`, `blink`, `sub_camera_indoor`, `sub_camera_outdoor`, `fn_sensor_motion`, `fn_sensor_battery`, `fn_sensor_signal`.
- Tagged 86 entities: 5 indoor cam devices (bath room, bedroom, hall, kitchen, camera tent) and 7 outdoor cam devices (back door, front, front door, front driveway, garage, garden, water side), plus the `alarm_control_panel.blink_indoor` / `alarm_control_panel.blink_outdoor` sync modules.
- Tent camera stays indoor-classified and carries `grow` (it's part of the grow op — the one cam whose motion events are dashboard telemetry, not security alerts).
- Retrofit: added `fn_sensor_signal` to `sensor.wi_fi_signal_bambu` (replacing `fn_sensor_status`) so every wifi-signal sensor home-wide carries the same `fn_`. Stripped a stray `wi_fi` label from `sensor.flow_rate_irrigation_tent` (phase-1a era misfit).
- Deleted 2 legacy loose labels: `camera`, `wi_fi` (no remaining holders after migration). `battery` left alive — still used by 2 phone entities that are future phase-3 scope.

Camera-scope severity rules:
- Security camera entity → `sev_warning` + `fn_camera` (outdoor + non-tent indoor). Tent cam → `sev_info` + `fn_camera` + `grow`.
- Motion binary sensor → `sev_warning` + `fn_sensor_motion` (security) / `sev_info` (tent).
- Motion-detection switch → `sev_warning` + `fn_controller` (security — disabling = security gap) / `sev_info` (tent).
- Battery binary sensor → `sev_warning` + `fn_sensor_battery` (blind-spot risk on low battery).
- Camera-armed binary sensor → `sev_info` + `fn_sensor_status`.
- Temperature + wi-fi signal sensors → `sev_info` + `fn_sensor_temp` / `fn_sensor_signal`.
- Blink sync modules (`alarm_control_panel.blink_{indoor,outdoor}`) → `sev_warning` + `fn_controller`.

Pre-phase-2 snapshot: `Container Home/migration_snapshots/20260423-193321Z_pre-phase2-camera/`
Post-phase-2 snapshot: `Container Home/migration_snapshots/20260423-193422Z_post-phase2-camera/` (52 labels).

### Mom Grow onboarding — 2026-04-24

Second grow garden added. Kasa EP40M 2-outlet plug strip installed with lights on plug 2; plug 1 is reserve (nothing plugged in yet).

- Created `Main` floor (added to registry — first non-loft non-outside floor).
- Created area `Mom Grow` on `Main` floor.
- Renamed Kasa sub-device "Mom Grow 2" → "Mom Grow Lights".
- Renamed every entity_id from `unnamed_ep40m_*` → `mom_grow_*` convention (16 entities).
- Moved all 3 devices (parent strip + 2 outlet sub-devices) into `Mom Grow`.
- Applied `sys_lighting` + `grow` + appropriate `fn_`/`sev_` to all 16 entities. Strip-level diagnostics (cloud connection, signal, SSID, device time, LED, auto-update) tagged under `sys_lighting` because the only active load on the strip is lights; plug 1 will be re-tagged when its future load arrives.
- Plug-1 empty outlet (`switch.mom_grow_1`) tagged `sev_info` as reserve. Plug-2 lights outlet (`switch.mom_grow_lights`) tagged `sev_critical` (photoperiod failure stresses plants, same as tent HLG). Both overheated binary sensors → `sev_critical` + `fn_sensor_status`.

Pre-mom-grow snapshot: `Container Home/migration_snapshots/20260424-015538Z_pre-mom-grow/`
Post-mom-grow snapshot: `Container Home/migration_snapshots/20260424-015643Z_post-mom-grow/` (51 labels, 468 in-scope entities).

## Tooling

- `Container Home/tag_migration_phase1a.py` — phase 1a migrator (irrigation): creates labels, moves `tent_irrigation` → `tent` area, tags entities, deletes old labels/areas. Idempotent. Dry-run default; `--apply` commits.
- `Container Home/tag_migration_phase1b.py` — phase 1b migrator (climate/lighting + residual-irrigation ancillaries + `grow`): creates the climate/lighting labels, tags entities, retroactively adds `grow` to phase-1a entities, strips and deletes 7 superseded labels. Idempotent. Dry-run default; `--apply` commits.
- `Container Home/tag_migration_phase1c.py` — phase 1c straggler patch (21 irrigation/climate/lighting helpers missed in 1a/1b). Additive merge. Dry-run default; `--apply` commits.
- `Container Home/tag_migration_phase1d.py` — phase 1d AC/dehumidifier sub-controls (23 entities). Additive merge with one hard-coded special case for `binary_sensor.full_dust_air_conditioner_tent` to avoid double-`sev_`. Dry-run default; `--apply` commits.
- `Container Home/tag_migration_phase3_printer.py` — phase 3d printer migrator (sys_printer / fn_camera / fn_sensor_status / prusa + Bambu + Prusa entity tagging; moves Bambu integration device to area `3d_printer`; deletes legacy `3d_printer` label; scoped `camera`-label strip). Dry-run default; `--apply` commits.
- `Container Home/tag_migration_phase2_camera.py` — phase 2 Blink camera migrator (sys_camera / blink / sub_camera_indoor / sub_camera_outdoor / fn_sensor_motion / fn_sensor_battery / fn_sensor_signal + 86 Blink entities + bambu-wifi retrofit + stray-label strip + deletes `camera` and `wi_fi` loose labels). Dry-run default; `--apply` commits.
- `Container Home/tag_migration_firmware_cleanup.py` — follow-up patch that added `fn_sensor_status` to 6 `update.*_firmware` entities in the tent scope (missed in 1a/1b/1c/1d because the `update` domain wasn't in the scope filter). Also stripped + deleted the loose `firmware` label (zero holders post-patch). Dry-run default; `--apply` commits.
- `Container Home/verify_tent_invariants.py` — tent-scope verifier (5 invariants).
- `Container Home/verify_whole_home_invariants.py` — whole-home verifier across every tagged `sys_`: 5 core invariants + 3 cross-cutting checks (`grow` on tent entities, `blink` on cameras, brand on printers). Excludes deferred and future-hardware entities. Authoritative verification after any migration.
- `Container Home/tag_migration_mom_grow.py` — Mom Grow onboarding migrator: creates `Main` floor + `Mom Grow` area, renames the Kasa EP40M strip's plug-2 sub-device to "Mom Grow Lights", renames all 16 `unnamed_ep40m_*` entity IDs to the `mom_grow_*` convention, moves the 3 devices into the area, applies `sys_lighting` + `grow` + per-entity `fn_`/`sev_` tags. Idempotent. Dry-run default; `--apply` commits.
- `Container Home/verify_tent_invariants.py` — re-runs the 5 tent invariants against the live registry. Handles the aggregated-sensor exception + deferred scope filter.
- `Container Home/verify_flood_stop_targets.py` — confirms the flood-stop safety automation's 4 label-intersection targets resolve to the expected feed/flush pumps + valves.
- `Container Home/registry_export.py` — snapshots all 4 registries as JSON under `migration_snapshots/<timestamp>[_label]/`. Run before every migration.
- `Container Home/area_labeler.py` — legacy one-shot for the pre-2026-04-23 tent/tent_irrigation split. Superseded by `tag_migration_phase1a.py`.
