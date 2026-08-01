# Flood-Table Drain-Corner Filter — slotted corner dam (v2, bolt-mounted)

Replacement for the small window-screen corner filter that keeps **blinding (clogging)** in
the flood-table drain corner. A **slotted "dam"** walls off the drain corner; it is
**bolted to the two walls with M3 hardware and siliconed to the floor**, so the only path to
the drain hole is **through coarse ~2 mm vertical slots**.

## Why this design

- The reservoir pump is a small **VIVOSUN 400GPH submersible** (same as the feed/flush stir
  pumps). It only needs protection from **strings/roots and chunks** that jam the impeller —
  **slime and silt pass through harmlessly**. The old fiberglass window screen (~1 mm) was
  *over-filtering*; that fine film is what blinded it. The fix is **coarser, not finer**.
- Flow here is mostly a **splash from one small spot**, so flow-driven self-cleaning doesn't
  apply. The win is **coarse slots + large area + in-place brushing**.
- The face is a **convex arc bowing into the reservoir** (`BOW=30`): 158 × 70 mm, **~29 %
  open ≈ 2,760 mm² ≈ 5.1× the drain bore**. The curve buys ~12 % more slot area than a flat
  plate in the same corner, adds **arch stiffness** (no oil-canning), and sheds debris off the
  round face instead of collecting it in a flat trough. Set `BOW=0` for a flat plate.
- **No top cap** — the dehumidifier sits directly above the drain corner, so nothing drips in
  from above or behind the wall; only the reservoir-side face needs to filter.

## Table (measured)

- Perimeter walls **70 mm tall, 3.5 mm thick**.
- Drain hole **Ø26.35 mm**, centre **16.5 mm off each inner wall** (jammed into the corner).
- Grid-mount post Ø29.6 at ~110.8/110.8 from the corner — the dam (`LEG=100`) stays inside it.

## Mounting (the v2 change)

Each end of the dam carries an **over-the-wall clamp** that hooks over the 3.5 mm lip:

```
   inside            outside
  (reservoir)  wall  (of table)
   ┌──────┐   ▓▓▓   ┌──────┐
   │inner │   ▓▓▓   │skirt │   ── bridge over the top ──┐
   │ leg  │═══▓▓▓═══│      │←── M3 screw from outside ──┘
   │[nut] │   ▓▓▓   │ o    │    through skirt + drilled wall
   └──────┘   ▓▓▓   └──────┘    into the captive nut
```

- Drill a **Ø3.4 hole** through the thin wall at each clamp.
- Drop an **M3 hex nut** into the trap in the inner leg, hold the part over the corner, and
  drive an **M3 screw from outside** → it pinches the wall and holds the dam flat and located
  while the floor silicone cures (and as a permanent hard mount after). All from outside.
- The **inner silicone flanges** up each wall seal the ends; the **floor lip** is the
  silicone bead to the floor. Any gap = unfiltered bypass.

## Geometry / frame (exported as `step/1_corner_dam_filter.step`)

Corner frame, Z up: drain corner at origin. Wall A = inner face `Y=0` (body `Y∈[-3.5,0]`),
Wall B = inner face `X=0`; reservoir interior `X>0, Y>0`. Dam spans `P1=(LEG,0)` → `P2=(0,LEG)`;
floor `Z=0`, walls to `Z=70`. `+n_out=(1,1)/√2` points into the reservoir (dirty side); the
small triangular pocket with the drain hole is on the corner side.

Preview: `step/1_corner_dam_filter.svg` (regenerated with the STEP).

## Parameters (edit at the top of `cad/flood_table_filter.py`)

| Param | Default | Notes |
|---|---|---|
| `LEG` | 100 | reach off the corner along each wall. Chord = `LEG·√2` = 141 mm. |
| `BOW` | 30 | face bulge into the reservoir (0 = flat). Arc face = 158 mm; adds area + stiffness. |
| `WALL_H` / `WALL_T` | 70 / 3.5 | table wall height / thickness (clamp spans `WALL_T`). |
| `SLOT_W` | 2.0 | slot width — coarse, for the small VIVOSUN impeller. |
| `OPEN_FRAC` | 0.35 | target open fraction → sets slot pitch. |
| `PANEL_T` | 4.0 | face thickness. |
| `FLANGE_LEN/_TH`, `FLOOR_W` | 30 / 5 / 15 | inner silicone tabs + floor lip. |
| `CLAMP_W`, `SKIRT_T`, `SKIRT_DROP`, `BRIDGE_TH`, `INNER_LEG_T` | 18 / 5 / 35 / 5 / 9 | over-the-wall clamp. |
| `SCREW_Z`, `M3_CLEAR`, `M3_NUT_AF`, `M3_NUT_TH` | 48 / 3.5 / 5.7 / 2.8 | M3 screw + captive nut. |

## Regenerate

VTK is stubbed in-file (this machine's VTK DLLs are blocked); only OCP is used. Python 3.13
has no `cadquery-ocp` wheel, so pin 3.12 + numpy<2:

```bash
uv run --no-project --python 3.12 --with "cadquery==2.4.0" --with "numpy==1.26.4" \
    python flood_table_filter/cad/flood_table_filter.py
```

## Print

- **PETG** (constant moisture — PLA hydrolyzes/warps and will fail). ASA also fine.
- Best orientation: stand the **dam face vertical** (slots run up the Z build direction) so
  the 2 mm slots resolve with no bridging. The end clamps then need a little support under
  the top bridge / skirt — that's fine, they're non-cosmetic. 3–4 perimeters, 0.4 mm nozzle OK.
- Whole part is **134 × 134 × 75 mm** — fits a 256 mm bed one-piece.

## Install & verify

1. **Slot test coupon first** — print a small section at `SLOT_W` to confirm 2 mm slots
   resolve in PETG and pass water / hold strings before the full print.
2. **Dry fit** into the corner; check both clamps hook over the walls and the inner flanges +
   floor lip sit flat. Mark and **drill the two Ø3.4 wall holes** through the clamp bores.
3. **Bolt it down** — M3 nut in each trap, screw from outside, snug (don't crush the 3.5 mm wall).
4. **Silicone** the floor lip + up both inner flanges (any gap = unfiltered bypass). Cure fully.
5. **Run a drain/pump cycle**: confirm no bypass past the flanges and the pump draws clean.
6. **Blinding watch** over a few feed/flush cycles. If it films too fast, step `SLOT_W` up and
   reprint — the open-area margin is large, so coarser is safe.

## Off-the-shelf

100 % silicone aquarium-safe sealant · 2× M3 screws + nuts · PETG/ASA filament.
