# Pinch Station v7 — cam → pivot arm → squeeze arm (1.5:1)

**2026-08-06.** Supersedes `lever_station_v6_spec.md` (v6 = direct lever onto the hose,
hoses at |Y| 44.65). v7 keeps the single-servo complementary architecture but inserts a
**pivot arm** between the cam and a **linear squeeze arm**, and moves the hoses out to
|Y| 63.

Geometry lives in the Fusion doc **"Servo Air Valve"**, component **`My Air Pinch Valve`**.
All coordinates below are in that component's frame. **Root Z = local Z + 30.4.**

---

## Force chain

```
DS3225 ──► Cam ──► roller R6 ──► Pivot Arm (1.5:1) ──► Squeeze Arm ──► hose ──► W anvil
```

Station B is the same parts rotated 180° about the cam axis (9.5, 0). Both-closed is
still geometrically impossible.

**1.5:1 does not reduce servo torque** — work in = nose force × nose stroke, and both are
fixed, so torque is ~10.4 kg·cm at either ratio against ~25 kg·cm available at 6 V. What
it buys is a **33 % lower cam/roller contact force** (66.7 N instead of 100 N), which
matters on printed parts. It costs a bigger cam and a higher pressure angle.

---

## Cam (component `Cam`)

| | |
|---|---|
| Axis | (9.500, 0.000) = servo spline |
| Low dwell (both open) | **r 25.000**, 196° of arc (262°→0°→98°) |
| Ramp | 98° → 170°, trapezoidal (10° ease each end) |
| Pinch dwell | **r 41.500**, 170°–190° (±10°) |
| **Lift** (roller-centre) | **16.500** |
| Follower | R6 roller → pitch 31.000 → 47.500 |
| Band | Z 12.35 – 26.35 |
| Peak pressure angle | **26.19°** at the bottom of the ramp, 17.80° at the top |

Verified off the solid: both dwells ripple **0.0000**, mirror symmetry **0.0000**.

**States:** 0° = both open (**±8° dead band**) · −90° = +Y station pinched · +90° = −Y
station pinched. Both dwells are concentric, so servo positioning error inside them
changes the gap by **nothing**, and holding torque at the pinch is ≈0 *before* any detent.

### ⚠ How to change the cam

The outer profile is driven by the sketch dimension **`d339 = cam_r_low + cam_lift`**
(cam axis → far profile point). **Change the parameters, not the geometry.** Trying to
`move()` the split-line endpoints fails silently — a driving dimension rejects the move
and the point snaps back.

The profile itself is two exact arcs (dwells) plus two computed ramp splines. Regenerating
it means re-running the profile script; the dwells must stay true arcs or the ripple
returns.

---

## Linkage — station A

| Item | Open | Mid | Pinched |
|---|---|---|---|
| Arm angle | −9.594° | 0° | +9.594° |
| **Roller centre** | (8.808, 31.000) | (9.500, 39.250) | (8.808, 47.500) |
| Cam pitch seen | 31.008 | 39.250 | 47.505 |
| **Push face Y** | 39.250 | 44.750 | 50.250 |
| Shaft pinch face | **56.180** | 61.680 | **67.180** |
| Gap vs anvil 69.350 | **13.170** | 7.670 | **2.170** |

- **Pivot (−40.000, 39.250)** · **rF 49.500** · **rN 33.000** → ratio **1.5000**
- Push-face travel **11.000** exactly · lift at the roller **16.497**
- Ratio depends only on the contact point's **X**, not its Y — the push face just has to
  land on **x = −7.000**
- Pad scrub 0.46, roller x-wander 0.69 — both negligible

---

## Parts

### Pivot stack — three parts on one M5

| Part | Component | Geometry |
|---|---|---|
| **Pivot Pad** | `Component28` → *Pivot Pad* | Ø25.30 OD / Ø11.30 bore, Z −2.40 → 12.35 (7.00 wall) |
| **Pivot Sleeve** | *Pivot Sleeve* (new) | Ø11.30 journal Z −2.40 → **26.85**, Ø17.30 collar → 28.85, Ø5.30 bore |
| **Pivot Arm** | `Pivot Cam` | bore Ø11.30 @ (−40, 39.25), axle Ø5.00 @ (9.5, 39.25), Z 12.35 – 26.35 |

Clamp order: bolt head → collar → sleeve → pad → base plate → nut. One solid column, so
torque never reaches the arm. Journal is **14.50** against a **14.00** arm = **0.50 float**.
Pivot carries only **33 N** net → 0.21 MPa on the journal.

Arm is an 11.0-wide bar, hub Ø18.0, fork cheeks **r5.5 about the axle** so they trail the
Ø12 roller by 0.5 mm at every angle and never touch the cam.

Bolt **M5 × 35**, thin nut (2.7) in an 8.10-across-flats pocket at (−40.000, 39.250).
Base plate has the Ø5.30 through hole; **the nut pocket is NOT cut** — a 2.7 nut in a
3.0 plate leaves a 0.3 ceiling, so it waits on local plate thickening.

### Squeeze Arm (component *Squeeze Arm*)

| | |
|---|---|
| Slides | +Y on **x = −7.000** |
| Section | 14.0 (X) × **18.70 (Z, 10.00 – 28.70)** |
| Length rear → face | **16.930** |
| Push edges | **r3.0 sloping fillet** (the two edges the hose wraps over) |

### ⚠ Why Z must be 18.70

Pinching Ø12.70 to a 2.17 gap conserves perimeter: π×12.70 = 39.9, so the flattened hose
is **~18.7 mm across**. Faces narrower than that let the hose squeeze out past the ends
and it never seals. v6 already had this — *"nose + anvil faces span z10–30, flattened hose
spreads ±8.7 from ℄"*. An earlier v7 pass used 14 mm and was wrong.

### Chamber (component `Hose Tube`)

X[−33.00, 19.00] Y[52.50, 76.00] Z[4.00, 34.70], one body.

- Hose bore **Ø12.70** along X at **Y 63.000, Z 19.35**
- **W anvil ribs**: r1.000 crowns at x **−11.620** / **−2.380**, **9.24 apart**
  (73 % of hose OD — same ratio as the Printables remix's 8.0/11.0), crest plane **69.350**,
  standing 3.0 proud of a relief at 72.350
- Free-hose window x −20 → +6 = **13.0 mm either side** of the pinch
- Shaft U slot 14 wide, open at the top
- Roller relief x 1.0 → 19.0 back to Y 54.50

**Ridges go on the anvil, not the shaft, and not both.** On both, aligned crests make the
two printed parts alignment-critical in X and concentrate stress on the hose; staggered
crests make an S-bend that needs *more* travel and force. On the anvil, the pusher stays a
flat face with nothing to misalign, and the anvil is the part you want replaceable for gap
tuning.

Keeping the crowns **at** 69.350 (relief cut behind them) rather than standing them proud
of it is what preserves every downstream number — shaft length, travel, both gaps.

---

## Parameters

Claude-added: `cam_r_low` 25 · `cam_lift` 16.5 · `cam_r_high` = `cam_r_low + cam_lift` ·
`cam_roller_r` 6 · `cam_dead_band` 8° · `cam_pinch_dwell` 10° · `cam_z_bot` 12.35 ·
`cam_z_top` 26.35 (both **LOCKED** — mate and bolts) · `hose_od` 12.7 · `hose_id` 9.525 ·
`hose_wall` = (od−id)/2 · `pinch_gap` 2.17 · `nose_stroke` 11 ·
`linkage_ratio` = `cam_lift / nose_stroke` → 1.5

User's own: `hose_far` 63 · `hose_high` 49.75 (root) · `baseplate_wide` = hose_far×2+35 →
161 · `baseplate_infront` 100 · `baseplate_behind` 40

---

## Open items

1. **Shaft guide is only 4.15 mm long** (Y 52.50 → 56.65), squeezed between the arm's
   swept flank (~51.4 at pinch) and the hose. Poor aspect ratio for a 14 mm shaft.
   **Fix: `hose_far` 63 → 72** buys 9 mm and costs nothing else in the chain.
2. **Chamber lost its parametric link** to `hose_far`/`hose_od` — rebuilt with hard
   numbers. Re-dimension when doing (1).
3. `Base Plate/Body1` and `Hose Tube/chamber` report `visible=False` and it can't be
   cleared by script — click the lightbulb in the browser.
4. Nut pocket — waiting on local plate thickening.
5. Cam **centre bolt lost its Ø5.3 step and head seat** during a manual rebuild; the
   bore is now straight Ø6.7 from z 18.35 → 26.35, so the screw head has nothing to bear on.
6. `cam_v6_comp` (hidden, old v6) still has 2 unhealthy features.
7. **Not built yet:** station B mirror, the Ø12 × 8 roller, the over-center detent
   (deliberately deferred), a light return spring (at full open the shaft is 0.47 clear of
   the hose so nothing holds the roller against the cam).
8. **Firmware still un-reworked** — `tent-irrigation-controller.yaml` still has the staged
   2-servo block (feed GPIO33 / flush GPIO5) with placeholder −100 %/100 % levels. Needs
   one servo on GPIO33, GPIO5 freed, three presets, boot/idle = both-open.
