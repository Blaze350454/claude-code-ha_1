# Servo Air Control Valve — v2 design (2026-08-08)

**This is a NEW design and it supersedes `pinch_station_v7_spec.md` for build purposes.**
The user rebuilt the valve from scratch on 2026-08-08 and explicitly retired the v7 geometry
("i've eliminated your design forget about your design for now").

| | |
|---|---|
| Fusion doc | **`Servo Air Control Vlave`** — note the typo in the filename, it is the real name |
| Root component | `Servo Air Control Valve` |
| Version at end of 2026-08-09 | **v49** (was v27 at the end of 08-08) — Fusion was closed with `modified=True` showing; confirm it saved on exit |
| Old doc (v7, retired) | `Servo Air Valve` — still exists, do not edit |

---

## CURRENT STATE — end of 2026-08-09

**Both stations are complete, symmetric and clash-free. The two datum bugs that broke the arm
twice are fixed at source, not compensated.**

| | Feed (−Y, the source) | Flush (+Y, live mirror) |
|---|---|---|
| arm | `Pivot Arm Feed ` 15.96322 cm³ / 17 f | `Pivot Arm Flush` **identical** |
| pusher | `Push Arm` 4.89189 / 50 f | `Push Arm Flush` **identical** |
| sleeve | `Pivot Arm Feed` 5.37697 / 8 f | `Pivot Arm Sleeve Flush` **identical** |
| housing bottom | `Hose Housing Bottom Feed` 59.60002 / 115 f | `... Flush` **identical** |
| housing top | `Hose Housing Top Feed` 26.58870 / 71 f | `... Flush` **identical** |
| revolute | `Revolute 1` −30..+5°, rest 0 | `Revolute 2` as-built, **same limits** |
| slider | `Slider 7` as-built, −1..10.75, rest 1.0 | `Slider 6` as-built, **same limits** |

- **Interference 0.000000 mm³** in all three real states: both open · Feed pinched · Flush pinched.
- Motion verified mirror-exact: arms at −15.32° → pads (2.1335, ∓47.2357); pushers at 10.75 →
  Y ∓78.2500..∓53.2500.
- **⚠ `Pivot Arm Feed ` keeps its trailing space.** Components get renamed often — **find them
  by geometry (r6.72 + r12.65), not by name.**
- Timeline 129, marker at the end. Remaining unhealthy items are all deliberate:
  `Push Arm/Extrude2`, two rolled-back `Mirror1`, and the suppressed `pos_arm_mirrored` /
  `pos_arm_place`. **The empty `Pivot Arm  (1):1` occurrence must stay** — it carries
  `RemoveBody-Pivot Arm`, the only thing suppressing a stray 13.45816 cm³ body.

### The two datum bugs — both fixed at source

1. **Pivot was dimensioned from the servo shaft.** `Base Plate/Sketch1` `d104` measured
   `pivot_off_front` from the *projected servo shaft* at X 9.65, so swapping the DS3225 model
   (v17→v22, axis 9.50→9.65) dragged the pivot −33.00 → −32.85 and left the freehand arm
   sketches behind — split bore, deformed blade. **Fixed: `d104` deleted, `d335` added from the
   sketch ORIGIN, `pivot_off_front` 42.5 → 32.85.** Pivot X = −`pivot_off_front`.
   `pivot_off_side` (`d22`) was always origin-referenced, which is why Y never drifted.
2. **Pusher Z tracked the clearance parameter.** `Slider 5` was a *regular* joint that
   re-derived the pusher's Z from a housing face, giving an offset of exactly `0.1 − |d95|`.
   **Fixed: replaced with as-built `Slider 7`**, and the `d165`/`d166` ±0.03 compensation in
   `Pivot Arm/Sketch2` reset to a clean **4 mm**. Band holds at Z 48–58 for *any* `d95`.

---

## Architecture

```
DS3225 servo (axis 9.5, 0)
  -> Cam                    rigid to the servo Arm (root joint "Rigid 2")
  -> Pivot Arm              revolute about a VERTICAL axis at (-33, +/-33)
  -> Push Arm               slider along -Y, guided in the Hose Housing
  -> Hose                   Y = +/-75, OD 12.70, ID 7.62
  -> Hose Housing anvil     solid from Y -81.45
```

Two mirrored stations at ±Y, one cam serving both. Cam is symmetric about the X axis, so
+φ pinches the −Y station and −φ pinches the +Y station. Both open at φ = 0.

---

## Parameters (user parameters, as of v49 — 2026-08-09)

```
base_wide            190   <-- was 250, user shrank it       base_thick        10
base_long            100   <-- was 200, user shrank it
hose_od              ( 25.4 * 0.5 ) * 1 mm  = 12.70
hose_id              ( 25.4 * 0.3 ) * 1 mm  =  7.62      -> wall 2.54 each side
squeeze_depth        10.75      <-- this is the SLIDER MAX, not the stroke
push_arm_tall         18        push_arm_long        25        push_arm_wide     12
cam_tall             push_arm_tall   <-- DRIVES NOTHING (verified; safe to delete)
hose_side_offset      75        hose_off_top_base    25
pivot_off_front    32.85   <-- was 42.5; DATUM CHANGED to the sketch origin, see below
pivot_off_side       33
push_arme_off_centre  -5        <-- typo in the name
cam_base_r       22.0030        cam_peak_r       33.6510
cam_lift         cam_peak_r - cam_base_r = 11.6480
```

⚠ **`cam_base_r` / `cam_peak_r` LOCK the cam arcs, they do NOT drive the cam** — the 36-point
rise/fall splines are not tied to the arc ends (2 constraints for 14 curves), so changing
either value opens a gap and the profile stops closing. Retune by regenerating the profile.

### ⚠ Parameter gotchas, all verified empirically

- ⚠ **`pivot_off_front`'s datum CHANGED on 2026-08-09 — it is now the BASE PLATE SKETCH
  ORIGIN, and its value is 32.85 (was 42.5).** Pivot X = **−`pivot_off_front`**.
  It used to be measured from the *projected servo shaft* in `Base Plate/Sketch1` (`d104`,
  X = 9.5 − value), which meant **swapping the servo model dragged the pivot** — that is what
  broke the arm twice (split bore, blade-band offset). `d104` was deleted and replaced by
  `d335`, an origin-referenced horizontal dimension. `pivot_off_side` (33, `d22`) was always
  origin-referenced, which is why Y never drifted. **Do not re-couple the pivot to the servo.**
- **`squeeze_depth` is the slider's maximum**, an absolute coordinate, not the travel.
  Travel = max − rest = 10.75 − 1.00 = **9.75 mm**. This caused real confusion; rename it.
- **`hose_side_offset` translates the hose, housing AND push arm together as one rigid group.**
  The push arm's recess into the housing is invariant at 5.850 mm at every value of it —
  moving everything outward can never make the pusher protrude.
- **`push_arm_long` lengthens the housing sleeve with the push arm**, because
  `Hose Housing/Extrude1` and `Extrude7` are *to-entity* extrudes aimed at a face of the
  Push Arm. So it cannot produce protrusion either.
- **`cam_tall` drives nothing** (verified 2026-08-09 against every expression in the doc).
  The cam profile sketch was fully undimensioned; as of 2026-08-09 the **two dwell radii are
  dimensioned** via `cam_base_r` / `cam_peak_r` — but see open item 3, **they lock, they do
  not drive**. The rise/fall splines remain non-parametric by design.

---

## The pinch (step 1 — settled)

Re-measured off the solids 2026-08-09 — **the anvil is at −81.500, not −81.450**, so the slop
and squash below correct the earlier figures:

```
push face at rest    Y -68.500      hose near face  -68.650   -> standoff 0.150
hose far face        Y -81.350      anvil            -81.500  -> slop     0.150   (was 0.100)
combined wall        5.080          gap at full pinch  3.250  -> squash   1.830 = 36.0 %
working stroke       9.750 mm
```

The anvil is a **flat full-width face at Y −81.5000**, spanning Z 40.500..65.500 and
X −13.000..22.000 (areas 542.50 lower + 332.50 upper). Not a cylindrical cradle — the r6.35
cylinders in the housing are the hose entry/exit, not the pinch.

36 % wall squash is the right ballpark for low-pressure air. **The 0.150 standoff is tight** —
it is inside the tolerance band of the parts (tubing runs ±0.2–0.3 on OD), so the valve may
sit pre-loaded on the hose at rest. 0.6 mm would be safer; that is the user's call, they set
0.150 deliberately.

⚠ **`pi*ID/2 + 2*wall` = 17.05 mm is the flattened OUTER envelope. It is NOT a sealing
requirement** — see the closed open item 2 for why. The sealing number is `pi*ID/2` = **11.97**.
The housing has 25.00 mm of free height (Z 40.500..65.500), and the 17.05 envelope needs
Z 44.475..61.525, so the ears never touch the pocket.

---

## Force and torque (step 3)

Soft silicone, Shore A ≈ 45, E ≈ 2.0 MPa.

```
ovalizing  OD 12.70 -> walls touching 5.08     5 - 30 N     (thin-ring bending)
wall compression  5.08 -> 3.20 (37 % strain)   -> 130 N nominal
                  neo-Hookean sigma = (E/3)(lambda - 1/lambda^2), A ~ 8 x 12 mm
DESIGN FORCE                                    200 N
```

DS3225 = 25 kg·cm = 2.45 N·m. Torque = F × ds/dφ, and the lever ratio does **not** enter it.

**The whole torque budget depends on the cam decelerating into the pinch.** Constant velocity
gives 13.4 kg·cm (too tight); the long ease-out gives **10.55 kg·cm, a 2.37× margin**.

---

## Cam (component `Cam`) — BUILT AND VERIFIED

Servo axis (9.5, 0). ψ measured from +X about that axis.

| segment | ψ range | width | R |
|---|---|---|---|
| **Low dwell** (both open) | −97.36 … +97.36 | 194.72° | **22.003** |
| **Rise** | 97.36 … 167.36 | 70° | 22.003 → 33.651 |
| **Pinch dwell** | 167.36 … 192.64 | 25.28° | **33.651** |
| **Fall** | 192.64 … 262.64 | 70° | mirror of rise |

Ramp law trapezoidal, **β = 70°, ease e = 25°**, ACC = 0.010354 mm/deg², v_max = 0.25884 mm/deg.

**Servo states: 0° = both open · +80° = −Y pinched · −80° = +Y pinched. Dead band ±10°.**

Measured off the solid:
```
low dwell ripple    0.00000        pinch dwell ripple   0.00000
LIFT                11.6480        target               11.648
mirror symmetry     0.00000
true cylindrical faces present: r=22.0030 and r=33.6510, both at (9.500, 0.000)
cam body 37.2231 cm3, 47 faces
thinnest wall (servo horn pocket to outer profile) 6.20 mm at psi 180
```

Both dwells are **true arcs**, so ripple is zero by construction, not by measurement. That is
what makes servo positioning error inside the dead band or the pinch dwell change the hose gap
by nothing, and makes holding a hose shut cost ≈ zero torque.

### ⚠ How the cam was rebuilt (repeat this method)

`Cam/Sketch1` is a **keyhole**: the outer boundary connects to the servo-horn pocket through
a slit line at ψ = 0, so `prof[1]` is one multi-curve loop, not an annulus. The rebuild
replaced the two old NURBS splines and the slit with:

```
2 x true arc  r22.003 @ (9.5,0)   split at psi 0 where the slit attaches
1 x spline    rise 97.36 -> 167.36, 2-deg fit points
1 x true arc  r33.651 @ (9.5,0)   167.36 -> 192.64
1 x spline    fall 192.64 -> 262.64
1 x line      slit (31.503, 0) -> (16.875, 0)
```

**`Cam/Sketch1` has Yax = (0, −1, 0)** — sketch Y is negated vs model Y, so arc sweep signs
must be flipped. Points placed with `modelToSketchSpace` are safe, but **the point's model Z
must be the sketch plane's Z (42.75), not 0** — getting that wrong put the whole profile
42.75 mm off-plane.

---

## Pivot Arm — BUILT AND VERIFIED
**⚠ Component RENAMED 2026-08-09: `Pivot Arm ` → `Pivot Arm Feed ` (trailing space survives).**
The mirror is `Pivot Arm Flush`. He renames components often — **find them by geometry
(r6.72 bore + r12.65 hub), never by name.** Coordinates below are pre-rename; the pivot is
now at (−32.85, ±33), not (−33, ±33).

Pivot (−33, −33), vertical axis. 16.1314 cm³, 17 faces.

| feature | value |
|---|---|
| Hub | r12.65 over the blade band, r11.856 above/below, Z 37.75–65 |
| Bore | r6.72, Z 37.75–60.91, cone above |
| **Blade** | **Z 48–58 (10 mm)** — see below, this is not negotiable |
| **Cam pad** | convex **r9.0 at (10.930, −30.970)**, 43.977 from the pivot |
| **Push pad** | convex **r6.0 at (4.500, −37.500)**, 37.769 from the pivot |
| Web relief | `arm_web_relief`, −1.0267 cm³ |

Timeline features added: `arm_strip_old_blade`, `arm_blade`, `arm_rebore`, `arm_web_relief`.

### ⚠ The blade must stay 10 mm — it is set by push-arm retention, not by the cam

A 16 mm blade (Z 45–61) looks better for contact stress, but the housing cutout then eats the
material that guides the push arm above and below, and **full four-sided surround collapses
from 11.0 mm to 0**. The push arm must not twist. 10 mm is correct.

### ⚠ Both pads must stand proud of the web

The first blade used tangent-trapezoid webs from the hub to each pad. The web then sat above
the pad and **took the cam contact itself** at r 26–34 from the pivot instead of the pad at
43.977 — the arm over-rotated to 12.044 mm and the dead band vanished. The web relief fixes it.
Same rule as v7's "the bar must not beat the nose pad to contact."

---

## Verified motion (−Y station, matched poses)

```
 phi    theta      push travel   contact r_from_pivot
   0   -0.000      0.000 mm         44.908     dead band
  10   -0.000      0.000 mm         44.642     dead band
  20   -1.124      0.735 mm         42.268
  45   -8.993      5.806 mm         40.490
  70  -14.957      9.526 mm         42.077
  78  -15.320      9.748 mm         42.785     PINCH
  90  -15.320      9.748 mm         42.857     PINCH (dwell holds flat)
```

Target 9.750 mm; achieved **9.748**. Contact is on the r9 pad throughout.

**Interference: 0.00000 at every pose** — cam↔arm, cam↔sleeve, cam↔housing, cam↔push arm,
cam↔plate, arm↔housing, arm↔upper housing, arm↔sleeve. Both stations.

---

## Housing

- Hub relief pockets: **r12.40 at (−33, ∓33), Z 28 → 43**, 0.09887 cm³ each. Opens downward
  through the underside so it prints without an overhang. 0.544 mm clearance on the r11.856 hub.
- Both housings 63.6716 cm³ / 134 faces; upper housings 28.2581 / 71.
- **Push-arm retention: 11.0 mm of full four-sided surround, Y −57.0 to −68.0.** Engaged at
  every stroke position (the pusher always occupies Y −68.5 … −53.25). Engagement is longest
  at full pinch and shortest at rest, which is the right way round.
- **`d77` in `Hose Housing/Sketch1` sets how far the sleeve runs past the pusher.** It is safe
  up to ~15 mm; at 24.85 it breaks `Fillet1/2`, `Extrude14/15` **and silently moves `Split1`
  from Z 56 to Z 62.50**. Leave it at 7.

---

## Base plate — COMPLETE

10 mm slab at Z 18–28 (= `base_thick`); everything mounts on the Z=28 face. The only things
above it are the two pivot bosses.

| mount | holes |
|---|---|
| Servo | 4 × Ø3.5 at (±24, ±4.9), Z 25–28 |
| Servo body clearance | through-void X −16…+12 |
| Pivot, both sides | Ø25.3 boss × 9.75 tall (Z 28→37.75) + Ø5.3 bore |
| Hose housing | **8 × Ø3.5, Z 24–28** at (−30.5, ±87.35), (39.5, ±87.35), (−17.5, ±43.65), (26.5, ±43.65) |
| Upper housing | bolts into the lower housing, not the plate |

All 8 housing spigots verified against plate holes: **0 missing.**

**⚠ Do not blanket-mirror the base plate.** The pivot bosses and servo holes are already
symmetric and would double up. Mirror only what is one-sided.

---

## OPEN ITEMS

### 1. Print clearances — DONE 2026-08-09. **0.07 mm per side everywhere.**

⚠ **The table that used to live here was wrong on two of its three rows.** It claimed the
model was "at exact nominal" with no fit pass done. It was not — the user had already set
0.07/side, and 0.07 is *his* number for his printer. Do not "fix" these back to the generic
0.20–0.40 FDM figures.

| fit | before | after | how |
|---|---|---|---|
| Arm bore on sleeve journal | 0.0700/side | **unchanged** | already right — `Pivot Arm/OffsetFaces1` = **−0.07 mm** |
| Push arm in housing slot | 0.1000/side | **0.0700/side** | `Hose Housing/Sketch3` **`d95`: −0.1 → −0.07** |
| Cone seat (arm↔sleeve, axial) | 0.07 normal | **unchanged** | already right — same OffsetFaces1 |

Measured off the solids after the change: slot **12.1400 × 18.1400**, pusher **12.0000 ×
18.0000**, gap **0.0700 on all four faces**. Interference **0.000000 mm³** across 10 body
pairs. Timeline health unchanged (the same 2 pre-existing).

**BOTH STATIONS verified 2026-08-09** (the +Y side was initially missed — its pusher is a
separate component, **`Push Arm 2`**, a child occurrence of `Push Arm`, so a naive
`pusher.bRepBodies` scan finds only the −Y body):

```
-Y  slot X 12.1400  gaps 0.0700 / 0.0700   bore 6.72 vs journal 6.65 = 0.070
+Y  slot X 12.1400  gaps 0.0700 / 0.0700   bore 6.72 vs journal 6.65 = 0.070
+Y housing bodies are named 'Hose Housing Bottom (1)' and 'Hose Housing (1)'
```

Arm parity is exact: −Y live and +Y frozen are both **17 faces, 34 edges, 16.13136 cm³**,
Z height 27.2500, radii `[6.0, 6.72, 9.0, 11.8556, 12.65]`. Interference 0.000000 mm³ on
both stations.

**The "0.02 mm axial" row was a misreading and there is no such fit.** What sits above the
journal is a **matched 35° cone pair** (sleeve `Z 60.9298→65.0000`, arm `Z 60.9077→65.0000`),
already carrying 0.07 mm *normal* clearance from OffsetFaces1. The 0.0221 was just the Z
offset between where the two cones start, which is a *consequence* of that 0.07, not a gap.
The arm's real axial thrust face is its underside on the base-plate boss at **Z 37.75, in
hard contact by design** — that one is supposed to be 0.000.

**`d95` is the ONLY control for the slot clearance.** `Hose Housing/Sketch3` projects the
push-arm outline (18 of its 36 curves are reference curves) and offsets it by `d95`. Growing
the pusher does **not** open the fit — the slot tracks it. Do not go looking for another knob.

#### ⚠ Two side-effects of touching `d95` — both understood, one still open

> **✅ BOTH CURED 2026-08-09 — this section is HISTORY.** `Slider 5` (a *regular* joint) was
> re-deriving the pusher's Z from a housing face; it is now as-built **`Slider 7`**, so the
> pusher no longer tracks `d95` at all and `d165`/`d166` are back to a clean **4 mm**.
> Verified across d95 −0.10 / −0.04 / −0.07: pusher Z 44.0..62.0 and band 48.0..58.0 every
> time. **Do not reintroduce the ±0.03 bias.** Kept below only to explain the mechanism.

Changing `d95` away from −0.1 *used to* drag two things, because `Push Arm/Sketch1` and
`Pivot Arm /Sketch1` are undimensioned and built on projected geometry (see open item 3):

1. **The Push Arm occurrence shifts in Z by `0.1 − |d95|`** (at −0.07, +0.03 mm). This is
   **pose only** — the Push Arm's *component-space* body is byte-identical (X −1.5..10.5,
   Z 44.0..62.0, vol 4.89189) and only `transform2.translation.z` changes 0 → 0.03. As
   manufactured parts the fit is a true 0.07/side. But it means an **assembly-space** gap
   measurement reads a misleading **0.10 bottom / 0.04 top**. Measure the parts, not the pose.
2. **The Pivot Arm grows a 0.03 mm ledge on its hub — STILL OPEN.** The hub step at Z 58.00
   moves to Z 58.0300 while `arm_blade` (a fixed 10 mm extrude from Z 48) stays at 58.00,
   leaving a sliver: **17 faces → 23**, vol 16.13136 → 16.14819 (+16.8 mm³ = a 0.03 skin over
   561 mm²). **Harmless to print** (0.03 is below any layer height) and **no contact geometry
   is touched** — cam pad r9 (375.8934), push pad r6 (85.6981), bore r6.72 (977.7880) and the
   blade band Z 48–58 are all identical to before. It is a model-hygiene defect only. It
   disappears once `Pivot Arm /Sketch1` is dimensioned.

The transfer function, if you ever retune (`c = |d95|`, assembly-space): **X gaps = c ·
bottom gap = 0.10 always · top gap = 2c − 0.10.** Component-space (what prints) is c on all
four faces.

### 2. ~~Push arm pinch face is 14.00 mm tall~~ — CLOSED 2026-08-09, **no change needed**

**The premise was wrong: it compared the face to the flattened OUTER envelope (17.05) when the
sealing requirement is the flattened BORE width, `pi*ID/2` = 11.969 mm.**

```
flattened bore width  pi*ID/2   = 11.969   <- must be covered to shut off
flat pinch face (Z)             = 14.000   <- current, centred on the hose axis Z 53
margin                          =  2.031   (1.015 mm each side)
```

The face already covers the bore with a millimetre to spare each side, so **the valve shuts.**
The 1.5 mm of hose hanging past each edge is the two folded side walls ("ears") — solid rubber
that carries no flow. They do not need to be compressed, and the r2.0 rounds landing at the
fold is the *right* place for a radius; a sharper edge would cut the tube there.

**Widening the face would actively hurt.** Scaling the spec's own force model (A ≈ 8 × 12 mm):

| flat face | contact area | force | servo torque | margin |
|---|---|---|---|---|
| 12.00 (spec's model) | 96.0 mm² | 200 N | 1.035 N·m | 2.37× |
| **14.00 (as built)** | 112.0 mm² | **233 N** | **1.208 N·m** | **2.03×** |
| 17.05 (the old proposal) | 136.4 mm² | 284 N | 1.471 N·m | 1.67× |

So the "fix" would have cost ~0.36× of torque margin to compress rubber that does not seal,
and it would have loaded the most fatigue-prone part of the tube. **`push_arm_tall` stays 18.**
That also sidesteps the feature breakage it caused at 24 and 26 — no need to investigate it.

Measured: flat face is Y −67.500, X 0.500..8.500 (8.000 along the hose axis) × Z 14.000,
area 105.31 mm². Pusher rounds are r2.0; pocket free height 25.000.

### 3. Non-parametric sketches — cam locked, 2 of 4 arm sketches anchored (2026-08-09)

**Summary of where this landed** (detail below):

| sketch | state |
|---|---|
| `arm_rebore_profile` | ✅ **fullyConstrained** — projected sleeve journal (as CONSTRUCTION) + Concentric + r6.72 dim |
| `arm_strip_old_blade_prof` | ✅ hub circle Concentric to the same projection + r12.65 dim. Its clearing box is still typed but clears the arm by **14.35 mm**, so its position is immaterial |
| `arm_blade_profile` | ❌ **cannot be constrained in place** |
| `arm_web_relief_profile` | ❌ **cannot be constrained in place** |

- **Anchor to the SLEEVE JOURNAL, not the arm's own bore** — projecting the arm's own bore
  raises `CIRCULAR_DEPENDENCY (arm_rebore_profile -> arm_rebore)`. The sleeve is upstream and
  *is* the pivot datum.
- **Set the projected curve `isConstruction = True`**, or it forms an extra profile
  (rebore went 1→2, strip 2→3) and can break the downstream extrude's profile reference.
- **Why the last two can't be done:** they are *deliberately overlapping freehand primitives*
  (that is where the 27 profiles come from). Measured: blade lines miss tangency by
  **0.0224 / 0.1223 / 0.3506 mm** with three not near-tangent at all, only 8 of 16 endpoints
  exactly coincident; `arm_web_relief_profile` carries a **31-point fitted spline** and no
  tangency. Constraining them would SNAP the outline by up to 0.35 mm and deform the verified
  cam pad. **Do not attempt it.**
- **This no longer matters in practice**, because the pivot is now dimensioned from the sketch
  origin (open item 1 / CURRENT STATE) — a servo swap cannot move it, so these two sketches
  have nothing to drift away from. Only a *deliberate* edit of `pivot_off_front` /
  `pivot_off_side` would leave them behind, and that is a conscious redesign.


**`Push Arm/Sketch1` is FINE — `isFullyConstrained = True`**, 4 dimensions
(`push_arm_tall`, `push_arm_long`, hose Ø12.70, and `(d40/2)+1` setting the near face off the
hose axis), plus a MidPoint constraint that centres the pusher on the hose axis by
construction. ⚠ An earlier note here blamed this sketch for the pusher chasing the slot floor.
**That was wrong** — the sketch is correct; the chase is via the **Slider joint**, whose
reference face moves with the slot. Do not "fix" this sketch.

#### Cam — the two dwell radii are now parametric (solid bit-identical)

| new user parameter | value | meaning |
|---|---|---|
| `cam_base_r` | **22.0030 mm** | low dwell, both open |
| `cam_peak_r` | **33.6510 mm** | pinch dwell |
| `cam_lift` | `cam_peak_r - cam_base_r` = **11.6480** | must stay 11.648 to keep the 9.748 push at φ 78 |

Three radial dimensions were added to `Cam/Sketch1` — two on the r22.003 arcs, one on the
r33.651 arc. Verified after: cam vol **37.22308**, faces **47**, sketch profiles **2**, solid
radii `[1.75, 3.35, 7.375, 22.003, 33.651]` — **bit-identical**.

> ⚠⚠ **These parameters LOCK the arcs. They are NOT safe to drive.**
> `Cam/Sketch1` has **2 geometric constraints for 14 curves** — the rise/fall **36-point
> fitted splines are not tied to the arc endpoints**. Changing `cam_base_r` or `cam_peak_r`
> moves the arc but leaves the splines behind, opening a gap so the profile stops closing and
> the cam extrude dies. The warning is in each parameter's comment in Fusion too.
> **To retune the cam, regenerate the profile by the method in the Cam section — do not edit
> these values.** They exist to name the numbers and stop them being dragged silently.

The rise/fall splines are deliberately left undimensioned: a cam profile generated from a
motion law should stay generated geometry, not hand-dimensioned 36 fit points at a time.

**`cam_tall` is confirmed dead** — checked every parameter expression in the document, nothing
references it. It still reads `push_arm_tall` = 18, while the cam is actually **19.2500 tall**
(Z 42.750..62.000) via to-entity extrudes. Safe to delete; left in place pending the user's call.

#### The Z 58.03 hub ledge — MECHANISM FULLY TRACED 2026-08-09

⚠ **`Pivot Arm /Sketch1` is NOT the cause.** An earlier note here blamed it. A marker walk
proves otherwise: Sketch1 → `Revolve1`/`Extrude1` produce a clean full-height hub,
r12.65 spanning Z **37.7500..65.0000**, with no 0.03 anywhere. Leave Sketch1 alone.

Marker walk over the Pivot Arm timeline (indices 79–114):

```
after [ 86] Sketch2     r12.6500 Z 37.7500..65.0000    full hub
after [ 87] Revolve2    r12.6500 Z 48.0300..58.0300    <-- .03 ENTERS HERE
after [100] arm_strip   r12.6500 Z 48.0300..58.0300    strip PRESERVES the r12.65 stub
after [103] arm_blade   r12.6500 Z 48.0000..58.0300    blade fills the bottom to 48.000
```

**The chain, end to end:**

```
d95 -0.1 -> -0.07
  -> a Hose Housing (1) face moves +0.03
  -> Slider 5 locates Push Arm off THAT face -> occurrence translation Z 0 -> +0.0300
  -> Pivot Arm/Sketch2 PROJECTS the pusher's faces: ref lines at world Z 44.030 / 62.030
  -> d165 = 4 mm, d166 = 4 mm inset  ->  band = 48.030 .. 58.030  (exactly 10.000 tall)
  -> arm_blade is HARDCODED  Z 48.000 + 10 mm  ->  tops out at 58.000
  -> Revolve2's band protrudes 0.03 above it  = the ledge
```

**`Sketch2` is well designed and should not be touched** — it ties the blade band to the
pusher with `d165`/`d166` = 4 mm insets, which is exactly why the band is a perfect 10.000 mm.
The real inconsistency is that the four `arm_*` features (added later) are pinned to a fixed
Z 48 construction plane while `Revolve2` correctly follows the pusher. They agree **iff** the
Push Arm occurrence sits at Z translation 0.

`arm_strip_old_blade` cannot help: its profile is a rectangle **minus the r12.65 circle**
(area 5997.2745 = 6500 − 502.73), so it deliberately preserves the hub stub. Making it taller
strips more of the old blade but never the r12.65 band.

**Root cause = `Slider 5`.** It is a Slider between `Push Arm:1` and `Hose Housing (1):1`,
and its `geometryOrOriginTwo` is a **BRepFace of Hose Housing (1)** — a face whose Z depends
on `d95`. Locating the pusher off a face that moves with a *clearance parameter* is the flaw.

#### ⚠ HISTORY — the ±0.03 bias fix, since SUPERSEDED
> The bias described below was a **compensation** and has been **removed**. `d165`/`d166` are
> now a clean **4 mm** each, because `Slider 7` (as-built) stopped the pusher tracking `d95`.
> Kept for the topology lesson only. **Do not re-apply the bias.**

⚠ **An earlier revision of this file said "leave it, 0.03 is below layer height." That was a
bad call and the user rejected it on sight.** The step is only 0.03 mm tall but it **shatters
the whole blade top into a spurious edge loop**, which renders as a visible seam:

```
frozen/good : blade top = ONE face at Z 58.0000, area 824.7340
broken      : FIVE fragments at Z 58.0000 (area 360.3537)
              + NurbsSurface riser Z 58.0000..58.0300 (3.0842)
              + a 561.0299 face at Z 58.0300
              edges: 19 at Z 58.00, 3 at Z 58.03, 11 more in the band
```

**Judge topology, not just dimensions** — face/edge counts caught this; a millimetre tolerance
never would.

**The fix** (`Pivot Arm /Sketch2`, two dimensions):

```
d165:  4 mm  ->  4 mm + 0.03 mm      band bottom inset from the projected pusher bottom
d166:  d165  ->  4 mm - 0.03 mm      band top    inset from the projected pusher top
```

`d166` was `= d165`; **that link is deliberately broken** — the two biases have opposite signs.
The ±0.03 cancels the Push Arm occurrence's Z bias, so the band lands back on its design
Z **48.000..58.000**. Verified: Pivot Arm **17 faces, vol 16.13136 — exactly equal to the
frozen good copy `Pivot Arm  (1)`** — blade top a single face at [58.0], contact geometry
untouched (r9 pad 375.8934, r6 pad 85.6981, bore r6.72 977.7880), and `d95` stays **−0.07**
so the 0.07/side clearance is kept. Both parameter comments in Fusion record why.

> ⚠ **This is a compensation, not a cure.** The bias is `0.1 mm − |d95|`. **If `d95` ever
> changes again, `d165`/`d166` must change with it** or the ledge returns at the new size.
> The cure is to re-point `Slider 5` so the pusher stops riding a `d95`-driven face — that
> joint carries the motion limits (−1.00 .. 10.75, rest 1.00) the whole verified φ→push table
> depends on, so it means re-verifying the motion. Not attempted.

### 4. ~~The +Y arm is a BaseFeature (dead geometry)~~ — REPLACED 2026-08-09 with a LIVE MIRROR

`Pivot Arm Ass/MirrorComponent1` mirrors the source arm occurrence about the **Pivot Arm Ass XZ
plane**, producing component `Pivot Arm Flush`. The push arm got the same treatment
(`Push Arm Flush`), replacing the old `Push Arm 2`. **Pure reflections, zero offset** — bores
land exactly on their own sleeve journals at (−32.85, ±33).

⚠ **Do not `deleteMe()` the old `Pivot Arm  (1)` occurrence — it CASCADES** (timeline 125→120,
resurrects a stray 13.45816 cm³ body). Suppress `pos_arm_mirrored` + `pos_arm_place` and leave
`RemoveBody-Pivot Arm` ACTIVE. Deleting a *joint* is safe; deleting the *occurrence* is not.

**Fusion mirror/joint lessons from this pass:**
- A mirrored component **can** be jointed and **does** articulate; the mirror does not lock it.
- The mirror turns the **opposite sense**, so the +Y revolute needs the **same** limits as −Y
  (−30..+5), not negated. Verify by pad displacement, never by assumption.
- Slider from `createByPlanarFace`: **the face normal is the joint's Z axis** — use
  `ZAxisJointDirection`. `YAxisJointDirection` produced a slider that moved nothing.
- **Never select joints by "last of type"** — the servo's own `Revolute 8` and stale joints
  masquerade. Match on `occurrenceOne/Two` names.
- After adding a mirror feature, **re-query `childOccurrences`** — the old handle misses it.
- `Push Arm 2` used to be a **child occurrence of `Push Arm`**, so it inherited the slider and
  moved the wrong way. Any +Y interference number involving it was meaningless.

### 4b. Old note, superseded

`pos_arm_mirrored` + `pos_arm_place`. It will not follow changes to the −Y arm. Replace it with
a linked mirrored instance in the final mirror pass. The old `Pivot Arm  (1)/Mirror1` mirrored
a body that `RemoveBody-Pivot Arm` then deleted, so it was never live either.

### 5. Latent fragility, unchanged all session

```
NONHEALTHY  Arm Screws/Extrude3 (legacy, inside the linked servo)
            Push Arm/Extrude2 (rolled back)   Hose Housing/Mirror1 (rolled back)
XREF  Base Plate/Extrude3, Extrude4  <-  Hose Housing/Sketch1
XREF  Push Arm/Extrude2             <-  Hose Housing/Sketch4
```

Two base-plate features are driven by the hose housing's sketch.

### 6. Parameter hygiene

`cam_tall` dead · `push_arme_off_centre` typo · `hose_od`/`hose_id` unit-laundered ·
`squeeze_depth` means slider max not stroke.

### 7. Firmware — WRITTEN + VALIDATED 2026-08-09, **uncommitted and NOT flashed**

`D:\Claude\Projects\esphome-config\tent-irrigation-controller.yaml` (the git mirror — the LIVE
device config never had a servo block at all, so this is staging, not live behaviour).

- 2-servo staging → **one `ledc air_diverter_pwm` on GPIO33; GPIO5 FREED**
- one `servo: air_diverter_servo` (min/max 2.5 %/12.5 %, auto_detach 1.5 s, transition 0 s)
- the two `switch:` entities replaced by a 3-option **`select: air_route_select`** —
  Both Open / Air to Feed / Air to Flush. A select because the single cam has exactly three
  states and "both pinched" is mechanically impossible, so the pump can never be dead-headed.
- `on_boot` → `select.set` **Both Open**
- **⚠ LEVELS ARE PERCENT, NOT DEGREES.** `level% = (cam φ / 90) × 100`, because min/max_level
  2.5/12.5 % = 500–2500 µs = 0–180°, so level 0 % is the servo's 90° mid-travel.
  Used **φ 80 → ±88.9 %**, comfortably inside the verified pinch dwell (flat φ 78–90).
- **Feed/Flush mapping is settled by the CAD names: −Y = Feed, +Y = Flush.** With
  "+80° = −Y pinched", **+80° pinches FEED so air reaches FLUSH**:
  `air_level_air_to_feed: -88.9%` · `air_level_air_to_flush: 88.9%` · `both_open: 0%`.
  (An earlier revision had these two backwards.)
- Validated with the real validator: **`INFO Configuration is valid!`** (levels resolve to
  −0.889 / +0.889 / 0.0). Nothing in HA referenced the two removed switch entities.
- HA side is still DUMMY-SERVO: `input_select.air_route` (none/feed/flush) already maps 1:1;
  flip `input_boolean.air_real_servos` and fill the marked TODO in `script.tent_air_burst`.

⚠ **The `mcp__esphome__*` tools are fully broken** (2026.7 dashboard swap — `read_config`
returns the Device Builder HTML shell). There is no docker and no ssh key-auth from Windows to
LXC 100 or the Proxmox host. Validate locally instead:
```powershell
copy <device>.yaml $tmp\ ; copy ci\fake_secrets.yaml $tmp\secrets.yaml
Set-Location $tmp ; uv run --with esphome esphome config <device>.yaml
```

---

## ▶ TOMORROW — 2026-08-10, in priority order

1. **Confirm Fusion saved.** It was closed with `modified=True` at v49; the exit prompt should
   have caught it. Re-run the state check before doing anything else.
2. **Size reduction — the worthwhile one is the anvil.** Currently **X 103.22 × Y 190.00 ×
   Z 74.00**; plate 100 × 190 × 19.75; parts span X −45.65..53.22, Y ±91.35.
   - **Thin the material behind the anvil: 9.85 mm → ~5–6 mm.** It carries ~200 N over an
     8 × 14 mm patch, so 5–6 mm is plenty in PETG. Pulls the housings to ±86.5 → `base_wide`
     190 → ~175. **≈15 mm off Y, zero kinematic impact.** Do this one.
   - Servo flip: only **6.72 mm** off X (98.87 → 92.15) and costs moved mounting holes, a
     re-indexed horn and new wire routing. The servo is 80.42 mm either way — flipping just
     moves the lopsided half (36.85 one side of the shaft, 43.57 the other). Probably not worth it.
   - `hose_side_offset` 75 → ~71 buys another 8 mm off Y (only 4.00 mm of gap exists to the arm
     hub, and the hub is circular so that gap is rotation-invariant) — **but it moves
     hose+housing+pusher as one group and changes where the pad meets the pusher, so the
     verified 9.748 mm stroke must be re-checked.** Lower priority.
3. **Test prints, staged — do NOT print everything.** Nothing has been exported yet.
   - **⚠ Base plate is 200 × 250 → now 100 × 190 × 19.75.** Re-measure after any size change
     and check it against the bed before committing ~190 cm³ of filament.
   - Print order: **one `Push Arm` (4.89 cm³) + one `Hose Housing Bottom` (59.60 cm³)** first
     and check the pusher slides freely through its full 9.75 mm stroke under finger pressure
     alone — **nothing pulls the valve open; the hose's own elasticity does**, so a binding
     pusher means the valve stays shut. Then sleeve + arm (bore turns freely), then cam, then
     the plate last.
   - If it binds, the fix is one parameter: `d95` in `Hose Housing/Sketch3`.
   - **Orientation matters** on three parts: the arm's blade takes bending, the cam's dwells
     take ~200 N sliding, and the pusher slides on all four faces.
4. **Firmware**: commit + push the esphome mirror, watch CI, pull on the VM. **Do not flash** —
   the valve is not built, the servo is not wired, and this ESP **cannot be power-cycled from
   HA** (recovery is a physical unplug or a reflash).
5. Optional hygiene: delete the dead `cam_tall` parameter; rename `push_arme_off_centre` (typo);
   `squeeze_depth` is the slider MAX, not the stroke — rename it.

## Standing note — grease the cam/pad contact

189 N through a sliding printed contact. The user accepted sliding over a roller because the
duty cycle is a few operations a day — that assumption is doing real work.
