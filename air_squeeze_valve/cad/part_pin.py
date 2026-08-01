"""PINCH PIN (print x2, identical). Rigid follower between cam and tube.
Local frame: travel axis = Y, nose tip at Y=0 (faces -Y toward the cam),
blade face at Y=24. Nose = vertical half-cylinder R4 (line contact on the cam,
self-aligning in Z; drops into the cam's R4.2 detent pocket). Blade = full
22-wide flat face (tube OD 12.7 flattens to ~20). Front corners chamfered in
plan so the sweeping crest can never graze the flat. Body 22 x 15 runs in the
housing channel (22.6 x 15.6 -> 0.3 clearance/side). STEP export for Fusion."""
import _vtk_shim  # noqa: F401  (stubs WDAC-blocked VTK before cadquery import)
import os, cadquery as cq

OUT = r"D:\Claude\Projects\Grow Home\air_squeeze_valve\step"
os.makedirs(OUT, exist_ok=True)

PIN_W   = 22.0   # X width (blade + guided body)
PIN_TH  = 15.0   # Z height (matches cam thickness; channel is 15.6)
NOSE_R  = 4.0    # vertical half-cylinder nose (cam pocket is R4.2)
BODY_L  = 20.0   # Y: nose center plane (4) .. blade face (24)
PIN_L   = BODY_L + NOSE_R          # nose tip .. blade face = 24
CHAM    = 6.0    # plan chamfer: front corners cut from x +-5 back to +-11

# body: X -11..11, Y 4..24, Z 0..15
body = (cq.Workplane("XY")
        .box(PIN_W, BODY_L, PIN_TH)
        .translate((0, NOSE_R + BODY_L/2, PIN_TH/2)))

# nose: vertical cylinder R4 at Y=4 -> front half protrudes to Y=0
nose = (cq.Workplane("XY", origin=(0, NOSE_R, 0))
        .circle(NOSE_R).extrude(PIN_TH))
pin = body.union(nose)

# plan chamfers on the front corners (diagonal (+-5,4) -> (+-11,10))
for sx in (+1, -1):
    tri = (cq.Workplane("XY", origin=(0, 0, -1))
           .polyline([(sx*5.0, NOSE_R), (sx*12.0, NOSE_R), (sx*12.0, NOSE_R + CHAM + 1.0)])
           .close().extrude(PIN_TH + 2))
    pin = pin.cut(tri)

path = os.path.join(OUT, "4_pin.step")
cq.exporters.export(pin, path)
bb = pin.val().BoundingBox()
print("WROTE", path)
print("bbox X/Y/Z:", round(bb.xlen,2), round(bb.ylen,2), round(bb.zlen,2))
print(f"nose tip -> blade face {PIN_L} | blade {PIN_W} wide (tube flattens ~20) | thk {PIN_TH}")
