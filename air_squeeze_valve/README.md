# Air Squeeze Valve v4 — twin-servo pinch valves (one unit per hose)

Air routing for the VIVOHOME VH181 → feed / flush reservoirs. **v4 architecture: each
hose gets its own compact pinch-valve UNIT** — a DS3225 servo turning a single-lobe cam
that drives a guided pinch pin (printed roller nose) squeezing the hose against a printed
backstop wall. **Build two identical units** (the 2× DS3225s were already in the
2026-06-20 parts order; firmware outputs GPIO33/GPIO5 are already staged in
`tent-irrigation-controller.yaml`).

**Why twin-servo (v4, 2026-07-04):** the single-servo 3-way diverter had to fit two
pinches + a both-open state into 180°, capping every ramp at ~80° of rotation. One servo
per hose has one pin and two states — **PINCH at 0° (detent pocket), OPEN at 180°** — so
the ramp spreads over 160°: worst pressure angle drops ~32° → **~16°**. At open, nothing
touches the cam (roller parks on base circle) → both states hold de-energized.

**Roller nose (user spec):** printed roller OD12 × 4 (bore 5.4) spinning on an **M5×12
screw** axle in a printed fork — no bought bearing. Rolling moves the friction to the M5
shank (r 2.5 vs R6 roller → effective drag ~0.09), killing the sliding side-load of the
plain nose. A 685ZZ bearing (5×11×5) drops onto the same screw if a roller ever wears.
The roller clicks into the cam's R6.2 pocket for the detent; breakout is a rolling action.

**Dead-head guard moves to firmware:** both-closed is now physically possible (it
dead-heads the pump). The interlock lives in **ESPHome on the tent-irrigation ESP32**
(both servos on one board): refuse to close a valve while the other is closed. Detents
mean power loss freezes the last (legal) state. TODO when flashing the staged servo
firmware.

Gaps (hose OD 12.7, 2×wall ≈ 3.2 solid): **hold/seal 2.6** | rim transient 2.0 |
open 13.2. Wall face Y = 53.2 printed into the housing — no bench calibration.
Hose transition: guided only far from the pinch (Ø15 bore in the raised housing roof
12 mm above the channel; plate Ø15 hole ~8 mm below), free to go round→slot between.

## Folder layout
- `step/` — importable solids for Fusion 360 (mm). **`0_assembly.step` = ONE complete
  unit** incl. DS3225 / horn / M5-axle reference solids — build two.
  v4 parts: `1_cam_v4.step`, `4_pin_v4.step`, `6_roller.step`, `5_housing.step`,
  `3_base_plate_v5.step`. Older superseded files (`1_cam.step`, `1_cam_v3.step`,
  `2_anvil.step`, `4_pin.step`, `3_base_plate*.step` v1–v4) kept for reference — safe
  to delete.
- `drawings/` — dimensioned 2D PNGs: sheets 1–4 + `6_baseplate_v5_top.png`.
- `cad/` — CadQuery + matplotlib generator scripts (the editable source of truth).
  v4 scripts: `part_cam_v4.py`, `part_pin_v4.py` (also exports the roller),
  `part_housing.py` (unchanged since v3.1), `part_base_v5.py`, `assembly.py`,
  `drawings_v4.py`. Older versioned scripts kept for reference.
  `_vtk_shim.py` stubs VTK (this machine's VTK DLLs are WDAC-blocked; only OCP is used).

## Regenerate
Python 3.13 has no `cadquery-ocp` wheel and numpy 2 breaks cq 2.4, so pin both.
The interpreter segfaults at *exit* (OCP teardown quirk) — outputs are already
written; ignore exit 139 / chain with `;` not `&&`.
```bash
CQ='uv run --no-project --python 3.12 --with cadquery==2.4.0 --with numpy==1.26.4 --with matplotlib python'
$CQ air_squeeze_valve/cad/part_cam_v4.py
$CQ air_squeeze_valve/cad/part_pin_v4.py     # exports pin + roller
$CQ air_squeeze_valve/cad/part_housing.py
$CQ air_squeeze_valve/cad/part_base_v5.py
$CQ air_squeeze_valve/cad/assembly.py        # AFTER the parts (imports their STEPs)
uv run --no-project --with matplotlib --with numpy python air_squeeze_valve/cad/drawings_v4.py
```

## Parts (per UNIT — build 2 of everything)
| Part | STEP | Print | Key dims (mm / deg) |
|---|---|---|---|
| **Unit assembly** | `0_assembly.step` | — | pose = pinch detent hold; red servo / blue horn / grey axle are reference-only |
| Cam v4 | `1_cam_v4.step` | ×1 | base R16; crest R27.2 ±10°; raised-cosine ramp 10→170°; pocket R6.2 cut @ R32.8 → floor R26.6, span ±5.1°; thk 15; Ø8 bore; Ø21×3 horn recess (underside) |
| Pin v4 | `4_pin_v4.step` | ×1 | 22 W × 15 thk × 24 (roller front→blade); fork cheeks Z 0–4.9/10.1–15; axle M5 @ Y6 (Ø10×2.8 head recess / Ø4.4 self-tap); plan chamfer ±7→±11 |
| Roller | `6_roller.step` | ×1 | OD12 × 4, bore 5.4 (M5 shank); 685ZZ 5×11×5 = drop-in upgrade |
| Housing | `5_housing.step` | ×1 | 34.6 × 31.2 × 41; channel 22.6 × 15.6; front Y28; wall face **Y53.2**; open hose bay; Ø15 hose bore @ Y46.6 in raised roof; 4× Ø2.8 pilots |
| Base plate v5 | `3_base_plate_v5.step` | ×1 | 70 × 90 × 5 (Y −24..66); housing screws Ø3.4 (±14, 31/56.2); Ø15 hose hole @ Y46.6 (funnel); 4× Ø4.2 unit mounts; origin = shaft |

Hardware per unit: DS3225 + **round** 25T horn, 1× M5×12 (roller axle), 4× M3×10
(housing, self-tap or heat-set), 4× servo tab M3, 3/8"ID×1/2"OD platinum silicone hose
+ 1/2" barbs. **No silicone grease near the hose** (swells it) — dry or PTFE film.

## Confirmed servo geometry (DS3225)
- Tab screw holes 49.5 apart (long axis), ±5 across (width).
- Output shaft OFFSET: 19.05 from one tab line, 30.45 from the other. Origin = shaft.
- Base body cutout 40.5 × 20.5 centered at X = −5.70. **Verify body L×W against real servo.**

## Assembly (per unit; origin = shaft axis; Z = 0 at plate bottom = servo flange plane)
- Plate Z 0–5; servo flange under the plate, body up through the cutout.
- Housing on +Y (Z 5–46), 4× M3 from below into the printed pilots. Channel Z 12.7–28.3;
  cam + pin Z 13–28; roller Z 18.3–22.3; hose bay to 40.3; roof bore 40.3–46.
  **CAM_Z0 = 13 is an estimate — verify the real horn height, adjust `assembly.py`.**
- Roller onto M5×12, screw down through the fork (head recessed in top cheek, self-tap
  into bottom cheek — don't overtighten, roller must spin). Insert pin roller-first,
  then drop the hose through roof bore → bay → plate hole; barbs below the plate.
  **The hose holds the pin captive.**
- Cam clocking: pocket (lobe tip) at 0° = pinched; 180° = open. Command the preset, let
  the roller click into the pocket, then detach.
- Mount each unit near its hose run via the 4× Ø4.2 corner holes.

## Design log
- **2026-07-04 — v4 twin-servo**: one unit per hose (2× DS3225 already owned + GPIOs
  staged). Ramp 75°→160° of rotation (pressure angle ~32→~16°). Printed roller on M5
  axle replaces both the sliding nose and the briefly-considered 623ZZ (user spec).
  Housing carried over unchanged from v3.1; plate v5 = compact single-unit. Dead-head
  guard becomes an ESPHome interlock. (User's tangent-hose scroll-valve photo reviewed:
  inline hose is elegant, but no detent + flexy seal gap — kept our pin/housing.)
- 2026-07-04 — v3.1: cam base R7→R16 (base was smaller than the Ø21 horn — nose sat on
  the horn), crest R27.2, ramp 50→75°; hose funnel cups → open transition bays.
- 2026-07-04 — v3 pin-follower: cam-on-pin replaces cam-on-tube; detent pocket replaces
  the W crown ("the ball would work, the W is useless").
- 2026-07-03 — W over-center crown; anvil foot outboard; base plate v3; one-file assembly.
- 2026-06-28 — base plate v2; parts v1.

## OPEN / VERIFY before printing
1. **Horn type** — cam recess is Ø21 for a ROUND 25T horn; user's model shows a
   single-ARM horn. Pick a round horn or re-cut the recess. UNRESOLVED.
2. CAM_Z0 stack height (13) vs the real servo + horn (drives housing channel Z too).
3. DS3225 body L×W vs the 40.5 × 20.5 cutout.
4. Real hose OD (assumed 12.7 — scales the 2.6 gap, Ø15 holes, wall at 53.2).
5. Pocket breakout torque on the bench (dials = POCKET_C or roller R — cam/roller reprint).
6. Pin return at open relies on hose elasticity; retrofit a light return spring if a
   hose takes compression set. Pin is captive only once the hose is in.
7. Roller spin on M5 threads — if it binds/squeaks, drop a 685ZZ onto the same screw.
8. **ESPHome both-closed interlock** before the valves touch the real air line.
