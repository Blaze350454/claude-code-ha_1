"""Part 2 of 3: ANVIL (print x2). STEP export for Fusion.
Local frame: cam-facing face at X=0 (cam sits at -X). Groove axis vertical (Z).
v2 (2026-07-03): foot now extends OUTBOARD (+X, behind the body, away from the
cam) - the old toward-cam foot blocked the vertical tube drop and clashed with
the servo body through the plate cutout. Slot sits in the exposed overhang
(center 18 behind the face -> plate screw at 19.6+18 = 37.6 from shaft) and the
groove is cut down through the foot so the tube passes the face uninterrupted."""
import _vtk_shim  # noqa: F401  (stubs WDAC-blocked VTK before cadquery import)
import os, cadquery as cq

OUT = r"D:\Claude\Projects\Grow Home\air_squeeze_valve\step"
os.makedirs(OUT, exist_ok=True)

AW, AH, AD = 18.0, 25.0, 12.0   # width(Y), height(Z), depth(X)
GROOVE_R   = 6.6                # half-round tube cradle (tube OD 12.7)
FOOT_TH    = 4.0
FOOT_OUT   = 12.0               # foot overhang past body back (+X, outboard)
SLOT_L, SLOT_W = 8.0, 4.0       # slot in the overhang: +-2.5 D calibration on M3
SLOT_CX    = AD + FOOT_OUT/2    # 18 behind the face

# body: X 0..12, Y -9..9, Z 0..25
body = cq.Workplane("XY").box(AD, AW, AH).translate((AD/2, 0, AH/2))

# foot: X 0..24, Y -9..9, Z -4..0 (under body + outboard overhang)
foot_len = AD + FOOT_OUT
foot = cq.Workplane("XY").box(foot_len, AW, FOOT_TH).translate((foot_len/2, 0, -FOOT_TH/2))

part = body.union(foot)

# vertical half-round groove on the cam face (axis Z at X0,Y0), cut through
# body AND foot so the tube can continue straight down past the plate hole
groove = cq.Workplane("XY", origin=(0, 0, -FOOT_TH)).circle(GROOVE_R).extrude(AH + FOOT_TH)
part = part.cut(groove)

# obround slot through the foot overhang (center X=18)
slot = (cq.Workplane("XY", origin=(SLOT_CX, 0, 1))
        .slot2D(SLOT_L, SLOT_W, 0)
        .extrude(-(FOOT_TH + 2)))
part = part.cut(slot)

path = os.path.join(OUT, "2_anvil.step")
cq.exporters.export(part, path)
bb = part.val().BoundingBox()
print("WROTE", path)
print("bbox X/Y/Z:", round(bb.xlen,2), round(bb.ylen,2), round(bb.zlen,2))
print(f"slot center {SLOT_CX} behind face -> plate screw at 19.6+{SLOT_CX} = {19.6+SLOT_CX}")
