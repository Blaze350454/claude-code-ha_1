"""PINCH PIN v4 - fork nose with a PRINTED ROLLER on an M5 screw axle
(user's spec: no bought bearing - print the roller, M5 screw as the center).
Exports TWO parts: 4_pin_v4.step (print x2) and 6_roller.step (print x2).

Why a roller: the printed half-cylinder nose of v3 slid across the cam - with
dry PLA/PETG friction (mu 0.3-0.5) roughly HALF the mid-ramp contact force
went sideways into the guide. Rolling moves the friction to the M5 shank at
r=2.5 vs the R6 roller surface -> effective drag at the cam contact ~ mu*0.42
= ~0.09, near ball-bearing territory at our speeds. If a printed roller ever
wears/squeaks, a 685ZZ bearing (5x11x5) drops onto the same screw (bore 5.4,
gap 5.2 - it fits). The roller drops into the cam's R6.2 pocket for the
detent, and breakout is a rolling action.

Local frame: travel axis = Y, ROLLER front surface at Y=0 (faces -Y toward
the cam), blade face at Y=24 (same travel chain as v3 -> housing unchanged).
- roller: OD12 x 4, bore 5.4 (rides the M5 shank/threads)
- fork: cheeks Z 0..4.9 and 10.1..15 (gap 5.2); d7 x 0.4 printed bosses on
  the gap faces keep the roller off the cheeks; axle at (0, 6)
- axle: M5 x 12 from the top - d10 x 2.8 head recess + d5.3 clearance in the
  top cheek, d4.4 self-tap in the bottom cheek
- plan chamfer +-7 -> +-11 over Y 2.5..11 (cam sweep clearance ~2.9 min)
Hardware per pin: 1x M5x12 pan head. STEP export for Fusion."""
import _vtk_shim  # noqa: F401  (stubs WDAC-blocked VTK before cadquery import)
import os, cadquery as cq

OUT = r"D:\Claude\Projects\Grow Home\air_squeeze_valve\step"
os.makedirs(OUT, exist_ok=True)

PIN_W   = 22.0   # X width (blade + guided body)
PIN_TH  = 15.0   # Z height (channel is 15.6)
PIN_L   = 24.0   # roller front surface .. blade face
ROLL_R  = 6.0    # printed roller OD 12
ROLL_H  = 4.0    # roller width
ROLL_BORE = 5.4  # on M5 shank/threads
AXLE_Y  = 6.0    # axle center -> roller front at Y=0
NECK_HW = 7.0    # cheek half-width at the front
NECK_Y0 = 2.5    # cheek front edge (roller protrudes 2.5 ahead)
BODY_Y0 = 11.0   # full 22 width from here back
GAP_Z0, GAP_Z1 = 4.9, 10.1   # fork gap (roller 4 + bosses 2x0.4 + slack)

# ---- pin ----
sil = [(-PIN_W/2, PIN_L), (-PIN_W/2, BODY_Y0), (-NECK_HW, NECK_Y0),
       (NECK_HW, NECK_Y0), (PIN_W/2, BODY_Y0), (PIN_W/2, PIN_L)]
pin = cq.Workplane("XY").polyline(sil).close().extrude(PIN_TH)

# fork gap: clears the roller (R6 + 0.6) back past the axle
gap = (cq.Workplane("XY")
       .box(2*(ROLL_R + 0.6), 14.8, GAP_Z1 - GAP_Z0)
       .translate((0, 14.8/2 - 2.0, (GAP_Z0 + GAP_Z1)/2)))
pin = pin.cut(gap)

# roller standoff bosses (d7 x 0.4) on the gap faces
pin = pin.union(cq.Workplane("XY", origin=(0, AXLE_Y, GAP_Z0)).circle(3.5).extrude(0.4))
pin = pin.union(cq.Workplane("XY", origin=(0, AXLE_Y, GAP_Z1 - 0.4)).circle(3.5).extrude(0.4))

# axle: d5.3 clearance + d10 head recess thru the top cheek, d4.4 self-tap below
pin = pin.cut(cq.Workplane("XY", origin=(0, AXLE_Y, GAP_Z1 - 0.5)).circle(2.65).extrude(PIN_TH))
pin = pin.cut(cq.Workplane("XY", origin=(0, AXLE_Y, PIN_TH - 2.8)).circle(5.0).extrude(3.8))
pin = pin.cut(cq.Workplane("XY", origin=(0, AXLE_Y, -1)).circle(2.2).extrude(GAP_Z0 + 0.5 + 1))

ppath = os.path.join(OUT, "4_pin_v4.step")
cq.exporters.export(pin, ppath)
bb = pin.val().BoundingBox()
print("WROTE", ppath, "bbox", round(bb.xlen,2), round(bb.ylen,2), round(bb.zlen,2))

# ---- printed roller ----
roller = (cq.Workplane("XY").circle(ROLL_R).circle(ROLL_BORE/2).extrude(ROLL_H)
          .edges("%CIRCLE").chamfer(0.4))
rpath = os.path.join(OUT, "6_roller.step")
cq.exporters.export(roller, rpath)
print("WROTE", rpath, f"(OD{2*ROLL_R} x {ROLL_H}, bore {ROLL_BORE}; 685ZZ 5x11x5 is a drop-in upgrade)")
print(f"roller front -> blade face {PIN_L} (R{ROLL_R} at Y={AXLE_Y}) | blade {PIN_W} wide | thk {PIN_TH}")
print("hardware per pin: 1x M5x12 pan head (axle)")
