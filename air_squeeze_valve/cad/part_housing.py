"""PIN HOUSING v3.1 (print x2 of the SAME part - X-symmetric, the -Y unit is
this rotated 180 about Z). One printed part per side = pin guide channel +
open hose-transition bay + backstop wall, so the critical blade-to-wall seal
distance is PRINTED, not assembled.

v3.1 (user Fusion review): the small funnel "cups" that seated the hose right
at the pinch are GONE - a 12.7 OD hose flattening to a ~20 slot needs about
one hose-diameter of free length each side to change shape, and the old d15
roof/floor holes sat 0 mm from the pinch. Now the hose is guided only FAR
from the pinch: a d15 bore in a raised roof 12 mm above the channel, and the
base-plate d15 hole ~8 mm below it; in between is an open bay. Also moved
outboard for the bigger cam (crest R27.2).

Modeled in assembly plan coords for the +Y side (origin under the servo
shaft) but with LOCAL Z0 = housing bottom = plate top (assembly Z=5).
- channel: 22.6 wide x 15.6 tall (local Z 7.7..23.3), pin slides on Y
- front face Y=28 (cam crest sweep R27.2 + 0.8 clearance)
- backstop wall inner face Y=53.2 -> gaps: hold 2.6 / crest 2.0 / open 13.2
- hose bay: Y 39..53.2 open from plate top up to local Z 35.3
- roof bore d15 at Y=46.6, local Z 35.3..41, entry funnel on the underside
- 4x d2.8 pilot holes from the bottom: M3 self-tap (or heat-set) from below
  the plate. STEP export for Fusion."""
import _vtk_shim  # noqa: F401  (stubs WDAC-blocked VTK before cadquery import)
import os, cadquery as cq

OUT = r"D:\Claude\Projects\Grow Home\air_squeeze_valve\step"
os.makedirs(OUT, exist_ok=True)

CH_W    = 22.6            # channel width (pin 22 + 0.3/side)
CH_Z0   = 7.7             # channel floor, local (assembly 12.7; pin bottom 13)
CH_Z1   = 23.3            # channel roof,  local (assembly 28.3; pin top 28)
WALL_T  = 6.0
X_HALF  = CH_W/2 + WALL_T   # 17.3
Y_FRONT = 28.0            # front face (crest sweep R27.2 + 0.8)
WALL_Y  = 53.2            # backstop inner face
Y_BACK  = WALL_Y + WALL_T   # 59.2
BAY_Y0  = 39.0            # hose bay start (floor + channel-roof end)
BAY_Z1  = 35.3            # bay top, local (12 mm free hose above the channel)
H       = 41.0            # local top (assembly 46)
TUBE_Y  = 46.6            # hose axis (blade open at 40, wall 53.2 -> centered)
TUBE_D  = 15.0
SCREWS  = [(14, 31.0), (-14, 31.0), (14, 56.2), (-14, 56.2)]
PILOT_D, PILOT_DEPTH = 2.8, 7.0

# solid block
blk = (cq.Workplane("XY")
       .box(2*X_HALF, Y_BACK - Y_FRONT, H)
       .translate((0, (Y_FRONT + Y_BACK)/2, H/2)))

# pin channel (open at the front, ends at the backstop wall)
ch = (cq.Workplane("XY")
      .box(CH_W, WALL_Y - (Y_FRONT - 2), CH_Z1 - CH_Z0)
      .translate((0, (Y_FRONT - 2 + WALL_Y)/2, (CH_Z0 + CH_Z1)/2)))
blk = blk.cut(ch)

# hose transition bay: open from plate top to BAY_Z1 between channel-roof end
# and the wall (the hose goes round -> pinched slot in here, unconstrained)
bay = (cq.Workplane("XY")
       .box(CH_W, WALL_Y - BAY_Y0, BAY_Z1 + 1)
       .translate((0, (BAY_Y0 + WALL_Y)/2, (BAY_Z1 - 1)/2)))
blk = blk.cut(bay)

# hose guide bore d15 through the raised roof, entry funnel on the underside
bore = (cq.Workplane("XY", origin=(0, TUBE_Y, BAY_Z1 - 1))
        .circle(TUBE_D/2).extrude(H - BAY_Z1 + 2))
blk = blk.cut(bore)
funnel = (cq.Workplane("XY", origin=(0, TUBE_Y, BAY_Z1))
          .circle(TUBE_D/2 + 2.0).workplane(offset=2.0).circle(TUBE_D/2)
          .loft(combine=True))
blk = blk.cut(funnel)

# M3 pilot holes from the bottom
for (sx, sy) in SCREWS:
    p = (cq.Workplane("XY", origin=(sx, sy, -1))
         .circle(PILOT_D/2).extrude(PILOT_DEPTH + 1))
    blk = blk.cut(p)

path = os.path.join(OUT, "5_housing.step")
cq.exporters.export(blk, path)
bb = blk.val().BoundingBox()
print("WROTE", path)
print("bbox X/Y/Z:", round(bb.xlen,2), round(bb.ylen,2), round(bb.zlen,2))
print(f"channel {CH_W} x {CH_Z1-CH_Z0:.1f} (local Z {CH_Z0}..{CH_Z1}) | wall face Y={WALL_Y} | bore d{TUBE_D} at Y={TUBE_Y}")
print(f"hose free length: {BAY_Z1-CH_Z1:.0f} above pinch (bay) + {CH_Z0:.1f} below (to plate top)")
print(f"pin guided span: retracted Y{Y_FRONT}..40 = {40-Y_FRONT:.0f} mm | sealed Y{Y_FRONT}..50.6 = {50.6-Y_FRONT:.1f} mm")
