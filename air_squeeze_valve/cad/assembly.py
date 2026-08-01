"""ASSEMBLY v4 - ONE VALVE UNIT in one importable STEP (0_assembly.step).
Twin-servo architecture (2026-07-04): one DS3225 per hose, so the physical
valve is this compact unit BUILT TWICE (feed + flush), mounted wherever each
hose runs. Unit = cam v4 (160 deg ramp + roller pocket) + fork pin v4 with
PRINTED ROLLER on an M5 axle + housing (unchanged v3.1) + base plate v5,
plus DS3225 / round-25T-horn / M5-axle REFERENCE solids.
Datum: origin = servo output shaft axis; Z=0 = plate bottom = servo tab
flange plane. Pose = PINCH detent hold: cam tip -> +Y, roller parked in the
pocket (front surface at R26.6), blade at 50.6 vs wall 53.2 = 2.6 seal.
OPEN = cam at 180 (lobe -> -Y, roller on base R16, hose open 13.2, zero
contact -> parks unpowered). Both-closed is now an ESPHome interlock job,
not a mechanical impossibility - see README.

CAM_Z0 (cam underside = horn underside) is an ESTIMATE from typical DS3225
dims. VERIFY against the real servo before printing spacers.
Run part_cam_v4 / part_pin_v4 / part_housing / part_base_v5 first."""
import _vtk_shim  # noqa: F401  (stubs WDAC-blocked VTK before cadquery import)
import os
import cadquery as cq

HERE = os.path.dirname(os.path.abspath(__file__))
STEP = os.path.normpath(os.path.join(HERE, "..", "step"))

PL_TH   = 5.0
CAM_Z0  = 13.0          # cam underside / horn underside - VERIFY on real servo
CAM_TH  = 15.0
PIN_Z0  = CAM_Z0        # pin body Z 13..28 (channel 12.7..28.3)
NOSE    = 26.6          # pose: roller front surface radius (parked in pocket)

cam     = cq.importers.importStep(os.path.join(STEP, "1_cam_v4.step"))
pin     = cq.importers.importStep(os.path.join(STEP, "4_pin_v4.step"))
roller  = cq.importers.importStep(os.path.join(STEP, "6_roller.step"))
housing = cq.importers.importStep(os.path.join(STEP, "5_housing.step"))
plate   = cq.importers.importStep(os.path.join(STEP, "3_base_plate_v5.step"))

# --- DS3225 reference solids (typical dims - VERIFY) ---
BODY_CX = -5.70
servo = (cq.Workplane("XY").box(40.0, 20.0, 40.5).translate((BODY_CX, 0, 11.0 - 40.5/2))
         .union(cq.Workplane("XY").box(57.0, 20.0, 2.5).translate((BODY_CX, 0, -1.25)))
         .union(cq.Workplane("XY").circle(6.5).extrude(1.5).translate((0, 0, 11.0)))
         .union(cq.Workplane("XY").circle(3.0).extrude(3.5).translate((0, 0, 12.5))))
# round 25T metal horn: d21 x 3 disc w/ spline bore, captured by the cam recess
horn = cq.Workplane("XY").circle(21.0/2).circle(3.1).extrude(3.0).translate((0, 0, CAM_Z0))
# M5x12 axle reference (head sits in the top-cheek recess)
axle = (cq.Workplane("XY").circle(2.5).extrude(11.0)
        .union(cq.Workplane("XY").circle(4.8).extrude(2.6).translate((0, 0, 11.0)))
        .translate((0, NOSE + 6.0, PIN_Z0 + 1.2)))

asm = (cq.Assembly(name="air_squeeze_valve_v4_unit")
       .add(plate, name="base_plate_v5", color=cq.Color(0.62, 0.62, 0.62))
       .add(housing, name="housing", color=cq.Color(0.93, 0.89, 0.78),
            loc=cq.Location((0, 0, PL_TH)))
       .add(pin, name="pin_v4", color=cq.Color(0.15, 0.55, 0.35),
            loc=cq.Location((0, NOSE, PIN_Z0)))
       .add(roller, name="roller_printed", color=cq.Color(0.55, 0.75, 0.55),
            loc=cq.Location((0, NOSE + 6.0, PIN_Z0 + 5.3)))
       .add(axle, name="axle_M5x12_ref", color=cq.Color(0.35, 0.35, 0.38))
       .add(cam, name="cam_v4", color=cq.Color(0.95, 0.55, 0.10),
            loc=cq.Location((0, 0, CAM_Z0), (0, 0, 1), 90))
       .add(servo, name="servo_DS3225_ref", color=cq.Color(0.80, 0.15, 0.15))
       .add(horn, name="horn_25T_ref", color=cq.Color(0.15, 0.35, 0.85)))

path = os.path.join(STEP, "0_assembly.step")
asm.save(path)
print("WROTE", path)
print("pose: PINCH detent hold (cam tip +Y, roller in pocket). BUILD TWO of this unit.")
print(f"blade at {NOSE+24} vs wall 53.2 -> seal 2.6 | open (cam 180): roller at 16, gap 13.2")
print(f"stack Z: plate 0-{PL_TH} | housing {PL_TH}-46 (channel 12.7-28.3, hose bay to 40.3, roof bore 40.3-46)"
      f" | horn {CAM_Z0}-{CAM_Z0+3} | cam+pin {CAM_Z0}-{CAM_Z0+CAM_TH} | roller 18.3-22.3  (VERIFY CAM_Z0)")
