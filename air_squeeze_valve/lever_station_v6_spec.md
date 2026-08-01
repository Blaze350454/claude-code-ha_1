# Pinch Station v6 — horizontal hose + pivoting lever (layout spec)

**2026-07-15.** Replaces the v4/v5 housing+sliding-pin station (hose ran vertically through
roof bore → bay → plate hole). Geometry lives in Fusion doc **"Servo Air Valve"**, component
**`lever_layout_v6`**, sketches **`PLAN_lever_layout`** (XY) + **`ELEV_pinch_section`**
(YZ at pinch). All coords = assembly frame: origin = cam/servo axis, z0 = plate bottom,
plate z0–5, station A on **+Y**.

## ⚡ ARCHITECTURE PIVOT (same day, after watching the Magnetic IDEX air valve):
## SINGLE-SERVO COMPLEMENTARY — one DS3225, one cam, TWO mirrored stations

Solids built + verified in Fusion (components `cam_v6_comp`, `station_body_v6` ×2 occ,
`lever_v6` ×2 occ, `anvil_insert_v6` ×2 occ — station B = the SAME parts as A, placed
rotated 180° about the cam axis → **print two of everything, no mirrored parts**).

**New cam `cam_v6_comp`** (blank Ø61.8, z12.3–28, Ø8 bore, arm pocket along −Y = frozen
servo-arm direction, attach screw at (0,−24.2), same as v5): **symmetric single lobe**,
tip at +X in the as-built (both-open) pose. Profile by off-tip angle d:
seat **r30.5** (d≤4°) → shoulder → crest **r30.9** (8–20°) → **linear ramp → r20.5 over
20–82°** → low dwell r20.5 (82–180°). One tip detent serves BOTH stations. Ramp pressure
angle ≈21°, cam torque ≈3–5 kg·cm vs 21+ available at 6 V. (Profile is a 1°-faceted
polyline — the R6 roller bridges facets; re-fit a smooth spline if you care.)

**States (joint `cam_v6_revolute_servo`, limits ±90°, zero = as-built):**
| joint | lobe | state |
|---|---|---|
| **+90°** | +Y | station **A pinched** (in detent), B open |
| **0°** | +X | **BOTH OPEN** — boot/idle default, 16°-wide dead band (c ∈ ±8°) |
| **−90°** | −Y | station **B pinched** (in detent), A open |

**Both-closed is geometrically impossible** → the ESPHome interlock and dead-head
automation are **DELETED** as work items. Fail state anywhere in the sweep leaves ≥1 hose
open. Which hose is feed vs flush = plumbing choice at install; map in firmware names.

**Verified:** 7-pose interference sweep (A-seat / A-crest / A-mid / both-open / B-mid /
B-crest / B-seat, levers driven to matched angles) × all 28 body pairs = **CLEAN**.
Assembly left in the both-open pose. Old cam_v4 hidden (not deleted); old joint remains
on it, inert.

**Plate:** extended to **73 × 128** (y −62..66) + 4× Ø3.4 station-B screws at
(±14,−31)/(±14,−56.2) — rotated copies of station A's.

**Firmware impact:** ONE servo (GPIO33), **GPIO5 freed**; the staged 2-servo blocks in
`tent-irrigation-controller.yaml` need rework to 1 servo + 3 presets (−100% / 0 / +100%
after endpoint calibration to the printed detents). Boot/idle default = 0 (both open).

## Solved layout (mm / deg)

| Item | Value |
|---|---|
| Cam radii (unchanged) | low **r20.5** / seat **r30.5** / crest **r30.9**, band z12.3–28 |
| Follower roller | reused printed roller **R6** (OD12×4, M5 axle, 685ZZ fallback), z18.3–22.3 |
| Roller-center states | open (0, 26.5) · seat (0, 36.5) · crest (−0.07, 36.90) |
| **Pivot P** | **(−32.00, 31.50)**, vertical axis, boss Ø12 |
| Lever radii | follower arm **rF = 32.39** · nose arm **rN = 36.19** |
| Lever angles (from P) | open −8.88° → seat +8.88° (sweep 17.76°); crest +9.60° → **over-center 0.72°** |
| Nose crown contact | seat (0, 48.40) · crest (−0.21, 48.80) · open (+3.63, 37.83) |
| **Anvil face** | y = **51.0** (fixed; replaceable insert) |
| **Gaps** | hold **2.60** / crest transient **2.20** / open **13.17** (v4-proven targets) |
| Hose | ℄ y = **44.65**, z = **20.0**, runs along X; OD 12.7 (**VERIFY real OD**) |
| Hose guides | inner faces at **\|x\| = 17** (≥13 = one OD of free hose each side — v3.1 round→flat lesson); Ø15 tunnels, funneled mouths |
| Contact face heights | nose + anvil faces span **z10–30** (flattened hose spreads ±8.7 from ℄) |

Checks: follower-velocity misalignment ≤8.9°; combined pressure angle ≈22° worst at
mid-ramp (fine — est. cam torque <5 kg·cm vs 25 kg·cm servo); nose scrubs ~3.6 mm along
the hose over the full stroke but only ~0.2 mm during the final squeeze (crest→seat).

## Fillet schedule — no sharp edge anywhere on the hose path (the core requirement)

- Nose crown: **2.5–3 mm wide** along hose axis, pinch-edge fillets **r ≥ 1.6** (never
  below wall thickness 1.6); face top/bottom edges r2.
- Anvil insert face: all four edges **r2–3**.
- Hose-guide mouths: r4–5 or funneled (like the old roof-bore funnel).

## Part notes

- **Lever**: section ≥ ~10 mm deep (gap accuracy = lever stiffness). Route the arm
  **above the cam top (z > 28)** and drop the roller fork down into the cam band — this
  clears the Ø61.8+2 keep-out (dashed circle in the sketch) in every pose; a plan-view
  dog-leg works too but the overhead route is immune to lobe-sweep direction. Fork =
  copy pin_v4's proven design (cheeks, M5×12 through, head recess). Leave a boss for an
  optional light return spring (return force = hose elasticity, as v4; spring only if a
  hose takes compression set).
- **Anvil insert**: small exact-dim print (zero-offset rule) in a pocket (dovetail /
  T-slot from top) in the station body; gap tuning = reprint the insert only. Insert
  must seat on solid plastic, not cantilevered.
- **Pivot post**: boss Ø12 at (−32, 31.5) reaches x = −38 = the plate edge, exactly
  flush — extend the plate 2–4 mm on −X if you want margin.
- **Detent unchanged**: hose back-pressure through the lever seats the roller past
  crest r30.9 into the r30.5 seat — same de-energized over-center hold. The 0.72°
  over-center margin is visible in the sketch (crest arc past the seat line).
- **Lube**: NO silicone grease anywhere near the hose (swells it) — dry or PTFE only.
  Roller needs none.
- Barbs hang past the plate edges on the horizontal run; hose is captive between
  guides + anvil once fitted.

## Open items (updated for the complementary architecture)

1. Verify real hose OD (12.7 assumed — scales gaps, guide bores, anvil y).
2. Detent breakout torque on the bench (one shared tip detent now).
3. Firmware rework: ONE servo on GPIO33, three presets (A-pinched / both-open /
   B-pinched), endpoints calibrated to the printed detents; **boot + idle default =
   both-open** (compression-set protection, from the IDEX valve's return-to-open habit).
   GPIO5 freed.
4. ~~ESPHome both-closed interlock~~ — **DELETED**: both-closed geometrically impossible.
5. User refinement + test print (2× station body, 2× lever, 2× insert, 2× roller, 1× cam).
