# Pinch Station v7 — cam → pivot arm → squeeze arm (1.5:1)

**2026-08-06, substantially corrected 2026-08-07.** Supersedes `lever_station_v6_spec.md`
(v6 = direct lever onto the hose, hoses at |Y| 44.65). v7 keeps the single-servo
complementary architecture but inserts a **pivot arm** between the cam and a **linear
squeeze arm**.

Geometry lives in the Fusion doc **"Servo Air Valve"**, component **`My Air Pinch Valve`**.
All coordinates below are in that component's frame. **Root Z = local Z + 30.4.**

> ### ⚠ Read this first — what changed on 2026-08-07
>
> The 2026-08-06 modelling session was **never saved** and its work was lost. Everything
> was rebuilt on 2026-08-07 and re-verified off the solid. In the course of that, several
> numbers in the original spec turned out to be **wrong, not merely incomplete**:
>
> | Was | Now | Why |
> |---|---|---|
> | `hose_far` 63 | **72** | Folded in old open item #1 up front. Every Y downstream of the hose moved +9. |
> | Arm "11.0-wide bar" | **7.0 (±3.5)** | At 11.0 the bar's own edge beats the nose pad to contact and the 1.5:1 ratio is lost. Derivation below. |
> | Bolt **M5 × 35** | **M5 × 40** | Local base-plate thickening added 3.0 mm; span is now 37.25. |
> | Hose at local Z 19.35 | **19.600** | The user's actual hose bodies are centred root 50.0. The spec's 19.35 was 0.25 out. |
> | Open item #1 "shaft guide only 4.15" | **obsolete** | Described the lost chamber. The real one had 23.0; the rebuilt one has 13.150. |
> | Open item #5 "cam lost its Ø5.3 step" | **obsolete** | Applied to a component that no longer exists. |
> | Cam in `cam_v7` | **component `Cam`** | `cam_v7` was an unauthorised parallel component and has been **deleted**. |
>
> **The document does not autosave. Save before ending any session that built geometry.**

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

### ⚠ Every interface in this chain is a CONTACT FACE, not a joint

**The pivot arm must NOT be pin-mated to the squeeze arm.** The nose is a plain
cylindrical pad bearing on a flat face — no pin, no captured slot, no Fusion joint. Same
at cam→roller. Confirmed as the user's explicit instruction 2026-08-07; do not "improve"
it into a pin/slider mate.

### ⚠ NO RETURN SPRING — the hose is the return (user, 2026-08-07)

Every contact is push-only, so something must drive the chain back. **That something is
the hose's own elasticity, and no separate spring is to be added.**

```
gap open    13.170      hose OD 12.700       stroke 11.000
gap pinched  2.170

hose in contact from gap 12.700 down to 2.170 = 10.530 mm = 95.7 % of the stroke
free float at full open = 13.170 − 12.700     =  0.470 mm
```

The flattened hose pushes the squeeze arm back through **95.7 %** of the travel, and that
runs the chain in reverse: squeeze arm → nose pad → pivot arm → roller back onto the cam.
The **0.470 mm** of free float sits entirely at full open, where the cam is on its
**concentric low dwell** — so the roller's position there changes the gap by nothing and
the cam picks it straight back up on the next ramp. There is no lost motion to design for.

(An earlier revision of this file called a light spring "mandatory". That was wrong.)

**What actually decides whether it returns is friction, not force:** the squeeze arm must
slide freely in its 13.15 mm guide and the pivot journal must not stick. Print the shaft
slot with real clearance. Motion is horizontal, so gravity neither helps nor hinders.
**If it ever fails to return, the fix is a positive-return grooved/conjugate cam, not a
spring** — but that needs an outer wall at pitch+6 (r 53.5), which overruns the base
plate's X 40 edge, so treat it as a last resort.

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
| Band | Z 12.35 – 26.35 (`cam_z_bot` … `cam_z_top`) |
| Peak pressure angle | **26.19°** at the bottom of the ramp, 17.80° at the top |

Verified off the rebuilt solid (2026-08-07): low dwell ripple **0.00001**, pinch dwell
**0.00001**, mirror symmetry **0.00000**, lift **16.50000**, pitch **31.0000 / 47.5000**.
The residual 0.00001 is binary-search resolution — the dwells are true cylindrical faces
(r=25.000 and r=41.500 appear in the face list), so they are exact by construction.

**States:** 0° = both open (**±8° dead band**) · −90° = +Y station pinched · +90° = −Y
station pinched. Measured dead band: **0.0000 rise out to 6.72°**, +0.0226 at 8°.

### The ramp law (reconstructed and validated)

Trapezoidal, ramp β = 72°, ease e = 10°:

```
ACC   = LIFT / (e·(β−e)) = 16.5 / (10·62) = 0.0266129 mm/deg²
v     = ACC·e            = 0.266129 mm/deg      (constant-velocity mid-section)
ds/dφ = v·180/π          = 15.2467 mm/rad
PA    = atan(15.2467 / r_pitch)  →  26.19° at 31.0,  17.80° at 47.5
```

Both pressure angles reproduce this spec's own figures, which is what confirms the law.

### ⚠ How to rebuild the cam profile

**The old `d339 = cam_r_low + cam_lift` instruction is obsolete** — that dimension lived
in the pre-v7 sketch and drove only the far profile point of a 9-fit-point spline. The
cam is now built in component `Cam` as:

| Z band (local) | sketch | feature |
|---|---|---|
| `cam_z_bot` → `cam_z_top` | `cam_profile` — **2 true 3-point arcs (dwells) + 2 fitted splines (ramps, 2° fit points)** | `cam_outline` new body |
| `cam_z_bot` → +6 | `cam_arm_pocket` — circle (9.5,0) r7.375; circles (−15,±0.375) r3.0; rect (9.5,−3.375)→(−15,3.375) | `cam_arm_pocket_cut`, 9 profiles |
| `cam_z_bot + 6` → +3 | `cam_screw_shafts` — (9.5,0) r2.65; (−14.7,0) r1.5 | `cam_screw_shafts_cut` |
| `cam_z_bot + 9` → +5 | `cam_screw_heads` — (9.5,0) r3.35; (−14.7,0) r3.35 | `cam_screw_heads_cut` |

**Use true arcs for the dwells.** A single closed spline spanning dwells and ramps smooths
the curvature discontinuity at the junctions and measures 0.00379 ripple on the low dwell.

---

## Linkage — station A (at `hose_far` = 72)

| Item | Open | Mid | Pinched |
|---|---|---|---|
| Arm angle | −9.594° | 0° | +9.594° |
| **Roller centre** | (8.808, 31.000) | (9.500, 39.250) | (8.808, 47.500) |
| Cam pitch seen | 31.008 | 39.250 | 47.505 |
| **Push face Y** | 39.250 | 44.750 | 50.250 |
| Shaft pinch face | **65.180** | 70.680 | **76.180** |
| Gap vs anvil 78.350 | **13.170** | 7.670 | **2.170** |

- **Pivot (−40.000, 39.250)** · **rF 49.500** · **rN 33.000** → ratio **1.5000**
- Push-face travel **11.000** exactly · lift at the roller **16.497**
- **`rF` and `rN` are horizontal X offsets from the pivot, not radial distances:**
  (9.5 − −40)/(−7 − −40) = 49.5/33 = 1.5. This is what "ratio depends only on the contact
  point's X" means — the push face just has to land on **x = −7.000**.
- Pad scrub 0.46, roller x-wander 0.69 — both negligible

Verified off the solid: contact Y **39.2499 / 44.7500 / 50.2498**, travel **10.9999**,
and the maximum occurs **at the nose pad (x ≈ −7)**, not at the arm's own edge.

---

## Parts

### Pivot stack — three parts on one M5

| Part | Component | Geometry |
|---|---|---|
| **Pivot Pad** | `Component28` (body named *Pivot Pad*) | Ø25.30 OD / Ø11.30 bore, Z −2.40 → `cam_z_bot` (7.00 wall) |
| **Pivot Sleeve** | *Pivot Sleeve* | Ø11.30 journal Z −2.40 → **`cam_z_top` + 0.5** = 26.85, Ø17.30 collar → 28.85, Ø5.30 bore |
| **Pivot Arm** | `Pivot Cam` | bore Ø11.30 @ (−40, 39.25), axle Ø5.00 @ (9.5, 39.25), Z `cam_z_bot` – `cam_z_top` |

Clamp order: bolt head → collar → sleeve → pad → base plate → nut. One solid column, so
torque never reaches the arm. Journal is **14.500** against a **14.000** arm =
**0.500 float** (verified). Pivot carries only **33 N** → 0.21 MPa on the journal.

**Bolt M5 × 40** (was M5×35 — see below), thin nut (2.7) in an 8.10-across-flats pocket.

### Pivot Arm shape

- Bar **7.0 wide (±3.5)** on the centreline y = 39.25, from the pivot to the axle
- Pivot hub Ø18.0 @ (−40, 39.25)
- **Nose pad: cylinder r5.5 centred at (−7.000, 39.250)** — this is the contact feature
- Fork cheeks **r5.5 about the axle**, so they trail the Ø12 roller by 0.5 mm at every
  angle and never touch the cam (verified clash-free across the sweep)
- Fork slot 8.4 wide at `cam_z_bot + 2.8` → 2.8 cheeks, roller Ø12×8 sits Z 15.35–23.35
- **Cam relief on the underside: everything below y = 36.750 removed over x ∈ [−12.0, +2.5]**
  (feature `pivot_arm_cam_relief_cut`) — see below, this is not optional

#### ⚠ Why the bar is 7.0 wide and NOT 11.0

The squeeze arm's rear face spans x ∈ [−14, 0]. A straight arm edge at half-width `w`
reaches, at θ = +9.594° and x = 0:

```
y − 39.25 = 6.7606 + 1.014183·w        boss contact = 10.9989
w = 5.5  →  12.339   ... 1.34 mm ABOVE the pad → the bar contacts, ratio is LOST
w = 3.5  →  10.310   ... 0.689 mm below the pad → the pad contacts ✓
```

The nose must be the highest thing in the contact zone or the linkage silently stops being
1.5:1. Bending at the nose station is 66.7 N × 16.5 mm ÷ (14×7²/6) = **9.6 MPa**, ~5×
margin in PLA/PETG, so the narrower bar is structurally fine.

#### Why the nose is a cylinder, not a flat edge

A straight edge at 5.5 offset gives contact Y **50.405** at θ = +9.594°; the table says
50.250. A cylinder r5.5 at 33.0 from the pivot gives exactly **50.250** *and* predicts the
contact-X drift to −7.462 = the **0.46 pad scrub**. Two independent matches.

#### ⚠ The cam relief — the nose boss fouled the cam, FIXED 2026-08-08

Drawing the nose as a **full** r5.5 circle hung 5.5 mm of dead material below the
centreline, and the cam's lobe swept straight through it. Only the boss's **upper** arc
ever does any work (contact is at boss centre + 5.5 in Y), so everything below was pure
interference.

The foul was real across essentially the whole ramp — φ −17.5° to −67.5°, peaking at
**0.1978 cm³** at φ = −50° (θ = +2.39°), with a deepest penetration of **2.445 mm** at
x = −6.625.

**The fix is one prismatic rectangular cut**, `pivot_arm_cam_relief_cut`:

| | |
|---|---|
| Sketch | `pivot_arm_cam_relief` on `pivot_arm_cam_relief_plane` (offset `cam_z_bot` from XY) |
| Profile | rectangle (−12.0, 28.0) → (**+2.5**, **36.750**) |
| Extent | `cam_z_top - cam_z_bot` (full 14 mm band), cut, `participantBodies = [Body1]` |
| Removes | **0.368223 cm³** — arm goes 6.291379 → **5.923156 cm³**, 17 → 21 faces |

**Why y = 36.750.** The cam's swept envelope, measured in the arm's own frame over the
full 0→−90° servo sweep, **never exceeds y = 36.339** (max at x = −3.875). 36.750 leaves
**0.411 mm** clearance. The relief line is flat, not curved — the envelope is a shallow
smooth arc and following it would buy ~0.4 mm of material for a lot of complexity.

**Why the ends are −12.0 and +2.5.** The cam only breaks the bar's original 35.75
underside over x ∈ [−9.33, +1.44]; the boss bulge itself needs clearing over
x ∈ [−11.9, −2.1]. One rectangle spanning both is simpler than a stepped profile, and
**+2.5 lands exactly on the fork slot's start** so no thin rib is left between the two
cuts.

**Verified after the cut:** 73 poses across the full servo sweep, **arm ∩ cam = 0.000000
cm³ at every one**; arm ∩ chamber / base plate / pivot sleeve all still 0; and the contact
faces still measure **39.2500 / 44.7500 / 50.2500** — the 1.5:1 ratio and the 11.000
stroke are untouched.

**Structurally it is better than the old margin claimed, not worse.** Section depth and
bending stress measured off the solid (cam pushes 66.7 N at x = +9.5, hose reacts 100 N at
x = −7, pivot takes 33.3 N, peak moment 1100 N·mm at the nose):

| station | depth | σ |
|---|---|---|
| x = −7 (peak moment, **nose**) | **8.000** | **7.37 MPa** |
| x = −11.25 (**new critical section**) | 6.015 | **11.35 MPa** |
| x = −2 … +2 (notch floor) | 6.000 | 5.9 – 9.1 MPa |
| x < −12 (untouched bar) | 7.000 | ≤ 8.16 MPa |

The relief *deepens* the section at the highest-moment station (8.0 vs the 7.0 the old
9.62 MPa figure assumed) and only trims lightly-loaded ones. Peak stress moves to
x = −11.25 and rises 9.62 → **11.35 MPa**, ≈ **3.1× margin** on derated printed PLA.

#### The notch-end blend — `pivot_arm_cam_relief_blend`, r0.75, LEFT END ONLY

The notch ends are re-entrant corners at a 7.0 → 6.0 section step, so they carry a Kt of
roughly 2–2.5 on top of the nominal stress. The **left** end is blended:

| | |
|---|---|
| Feature | `pivot_arm_cam_relief_blend`, constant-radius fillet, rolling-ball |
| Edge | the single 14.000 mm edge at **(x −12.000, y 36.750)** — step face (14.00 mm², n = −X) ∧ notch floor (203 mm², n = +Y) |
| Radius | **0.75** |
| Adds | **0.001690 cm³** = r²(1 − π/4)·L exactly. Arm 5.923156 → **5.924846 cm³**, 21 → 22 faces |

**⚠ The radius is capped at 1.0 by geometry, not by choice.** The step is only
36.750 − 35.750 = **1.0 mm** tall, and a fillet consumes its full radius down the step
face. r0.75 leaves 0.25 mm of flat; anything ≥1.0 runs off the end of the face. (An
earlier note in this file suggested "r1.0–1.5" — 1.5 is impossible here.)

**Only the left end is blended, and that is deliberate.** At x = +2.5 the corner is
**split into three edges** by the fork slot — 2.8 mm cheek bands at Z 12.35–15.15 and
23.55–26.35 where the neighbour is the step face, and an 8.4 mm band at Z 15.15–23.55
where the neighbour is the **fork slot's own left wall** (n = −X, 50.4 mm²), which is not
this relief's corner at all. Blending it would mean filleting three dissimilar edges to
fix a station carrying only 5.95 MPa, versus 8.16 MPa nominal (and the 11.35 MPa peak
just inside) at the left. Left end only is the right trade.

**Re-verified after the blend** — a fillet puts material *back* into the relieved zone, so
this is not optional: 73 poses over the full sweep, **arm ∩ cam = 0.000000**; chamber,
base plate and pivot sleeve all still 0.

**Minimum clearance anywhere in the mechanism is +0.2861 mm at x = +2.50**, where the bar's
*original* 35.750 underside passes the cam. That is pre-existing geometry, not something
the relief introduced, and it is the tightest point by design — compare the +0.485 to
+0.498 the fork cheeks hold across x 6–13. Inside the relieved band the clearance bottoms
out at **+0.4108 at x = −3.75**.

### Squeeze Arm (component *Squeeze Arm*) — BUILT 2026-08-07

| | |
|---|---|
| Slides | +Y on **x = −7.000** |
| Section | 14.0 (X) × **18.70 (Z, 10.25 – 28.95)** |
| Length rear → face | **25.930** (was 16.930 at `hose_far` 63) |
| Push edges | **r3.0 sloping fillet** (the two edges the hose wraps over) |
| Rear face | plain flat face — the pivot arm's pad bears on it. **No pin, no slot.** |

#### ⚠ Why Z must be 18.70

Pinching Ø12.70 to a 2.17 gap conserves perimeter: π×12.70 = 39.9, so the flattened hose
is **~18.7 mm across**. Faces narrower than that let the hose squeeze out past the ends
and it never seals. An earlier v7 pass used 14 mm and was wrong. Centred on the hose at
Z 19.600 → **10.25 … 28.95**.

### Chamber (component `Hose Tube`) — rebuilt 2026-08-07

| feature | extent |
|---|---|
| block | X[−33, 19] · Y[52.50, 85.00] · Z[−2.40, 33.60] |
| hose bore | Ø12.70 along X at Y 72.000, **Z 19.600** |
| free-hose window | X[−20, 6] · Y[65.65, 81.35] · Z[10.25, 28.95] |
| **W anvil ribs** | r1.000 crowns at x **−11.620 / −2.380** (9.24 apart = 73 % of hose OD), crest plane **78.350**, standing 3.0 proud of a relief at **81.350** |
| shaft U slot | X[−14, 0] · Y[52.50, 65.65], open at the top → **guide 13.150** |
| **roller relief** | X[1, 19] back to **Y 54.500** |

**Ridges go on the anvil, not the shaft, and not both.** On both, aligned crests make the
two printed parts alignment-critical in X and concentrate stress on the hose; staggered
crests make an S-bend that needs *more* travel and force. On the anvil, the pusher stays a
flat face with nothing to misalign, and the anvil is the part you want replaceable for gap
tuning.

#### ⚠ The roller relief is not optional

Trimming the front face to 52.50 alone does **not** clear the arm: at pinch the fork boss
reaches Y **52.998** and the Ø12 roller **53.498**. The relief to 54.500 gives 1.000 mm.

#### ⚠ The old chamber was laterally wrong

Before the rebuild, every pinch feature centred on **X = 5.9** instead of −7.0. That is
fatal, not cosmetic: with the push face at 5.9, `rN` = 45.9 and the ratio collapses to
**1.078**. If the chamber is ever rebuilt again, check the station X first.

---

## Base plate

- Ø5.30 pivot hole at **(−40, 39.25)**. It is driven parametrically in `Base Plate/Sketch1`
  by **`d354` (X offset) and `d355` (Y offset) measured from the cam-axis point (9.5, 0)** —
  set `d354 = 49.5`, `d355 = 39.25`. Change those, never the geometry.
  **Note that sketch's frame: Xax=(1,0,0), Yax=(0,−1,0) — sketch Y is negated.**
- **Local thickening (done):** Ø25.30 boss extruded −3.0 mm from the underside
  (−5.4 → −8.4), with an **8.10 across-flats hex nut pocket 3.0 deep** cut up from −8.4.
  Nut ceiling is now **3.00 mm** (was 0.30). Verified: bolt path clear end to end, hex
  inradius measured between r=4.04 and r=4.06 → AF 8.10 exact.

### ⚠ The bolt is M5 × 40, not M5 × 35

Boss underside −8.40 to collar top 28.85 = **37.25 mm** of span. M5×35 reaches only −6.15
and engages under a millimetre of the nut. This is forced, not a preference: keeping M5×35
would cap the thickening at 0.75 mm, barely better than the 0.30 defect it fixes.

---

## Parameters

Claude-added: `cam_r_low` 25 · `cam_lift` 16.5 · `cam_r_high` = `cam_r_low + cam_lift` ·
`cam_roller_r` 6 · `cam_dead_band` 8° · `cam_pinch_dwell` 10° · `cam_z_bot` 12.35 ·
`cam_z_top` 26.35 (both **LOCKED** — mate and bolts) · `hose_od` 12.7 · `hose_id` 9.525 ·
`hose_wall` = (od−id)/2 · `pinch_gap` 2.17 · `nose_stroke` 11 ·
`linkage_ratio` = `cam_lift / nose_stroke` → 1.5

User's own: **`hose_far` 72** · `hose_high` 50 (root) · `baseplate_wide` = hose_far×2+35 →
**179** · `baseplate_infront` 100 · `baseplate_behind` 40

---

## Verification method

Interference is checked with **TemporaryBRepManager**: copy each body, transform the arm
about the pivot, boolean-intersect, read the volume. Sweeping θ = −9.594 … +9.594 on
2026-08-07: arm×chamber, arm×cam, arm×plate, chamber×cam, chamber×plate all
**0.000000 cm³**.

### ⚠ Drive θ FROM φ, not the other way round

Earlier sweeps picked a θ and bisected for the matching cam angle φ. That works on the
ramps but **degenerates on the dwells** — the cam is concentric there, so many φ tie for
one θ, and there is a mirror branch (θ = 0 also solves to φ = −136, station B's side).

**Solve in the physical direction instead: pick φ, then bisect θ.** Engagement is strictly
monotonic in θ (the roller centre rides an arc of radius 49.5 about the pivot, so larger θ
= further from the cam axis = less engagement), so a plain bisection on
`roller ∩ cam > 0` over θ ∈ [−9.594, +9.594] always converges to the one right answer,
dwells included. Clamp to the end stops when the whole range is engaged (pinch dwell) or
none of it is (dead band).

### ⚠ `Matrix3D.transformBy` composition order

Building a compound pose as `m = rot(−θ, PIV); m.transformBy(rot(φ, CAM))` composed the
two rotations the **wrong way round** and produced volumes that were silently plausible —
correct at θ = 0 (where one rotation is identity, so the bug cannot show) and wrong
everywhere else, by up to 10×. **Apply the rotations as successive `tbm.transform(body, …)`
calls instead**, where the order is unambiguous. Cross-check any pose measurement by
computing it a second way (rotate body A vs rotate body B) — the volumes must agree to
<1e-6 cm³.

Two more traps when verifying:
- `Profile.boundingBox` is a **loose control-polygon box**, not the tight geometric box.
  Sample `worldGeometry` evaluators for real extents.
- Never write `try: worldGeometry except: geometry` — the fallback silently measures
  sketch space and makes a frame-mapping bug unfalsifiable.

---

## Open items

1. ~~Squeeze Arm not built~~ — **BUILT and verified 2026-08-07.** 6.734 cm³, 8 faces,
   X[−14, 0] Y[44.750, 70.680] Z[10.250, 28.950] as drawn at the **mid** pose.
   Travel reproduces 39.250→50.250 rear / 65.180→76.180 front / gap 13.170→2.170.
   Built as a YZ section extruded ±7 along X: two overlapping rectangles + two r3.0
   circles unioned (12 profiles → 1 body) rather than 3D fillet picking.
   **The assembly is drawn at the MID (half-stroke) pose**, because the pivot arm was
   sketched with its centreline horizontal. Consequence: the arm overlaps the *rigid*
   `Hoses` body — that is the hose being compressed, and is expected, not a fault. All
   other pairs sweep clash-free at 0.000000 cm³.
2. ~~Ø12 × 8 roller not built~~ — **BUILT.** Component `Roller`, Ø12 × 8, bore Ø5.30, at
   the axle (9.5, 39.25), Z 15.35–23.35. **0.7283 cm³ = analytic exactly.**
3. **Station B mirror not built.**
4. ~~Cam ↔ servo-arm mate is broken~~ — **NOT broken; this entry misread the joint.**
   `Rigid 4` inside `My Air Pinch Valve` joins `Cam:1` ↔ `Arm:1` and is healthy. The
   `occurrenceTwo = None` joint `Rigid 23` is a **root-level legacy** joint that belongs to
   the old hidden parts, not to this assembly. (Verified 2026-08-08.)
5. ~~Light return spring~~ — **NOT being fitted.** The hose returns 95.7 % of the stroke;
   see the no-return-spring note above. Watch shaft/journal friction instead.
6. Over-center detent — deliberately deferred.
7. The chamber was rebuilt with hard numbers and has **no parametric link** to
   `hose_far`/`hose_od`. Re-dimension if `hose_far` changes again.
8. `Component28` still carries that name rather than *Pivot Pad*.
9. Legacy components still in the document: `cam_v4`, `cam_v6_comp` (2 unhealthy
   features), `lever_v6`, `station_body_v6`, `pin_v4`, `housing`, `base_plate_v5`.
10. **Firmware still un-reworked** — `tent-irrigation-controller.yaml` still has the staged
    2-servo block (feed GPIO33 / flush GPIO5) with placeholder −100 %/100 % levels. Needs
    one servo on GPIO33, GPIO5 freed, three presets, boot/idle = both-open.
