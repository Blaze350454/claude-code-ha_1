"""CAM v4 - ONE-HOSE cam for the twin-servo architecture (print x2, one per
valve unit). v4 (2026-07-04): the single-servo 3-way diverter capped every
ramp at ~80 deg of rotation (the both-open state at 90 deg is shared by any
number of cam tracks). With one servo per hose there is one pin and two
states - PINCH at 0 deg (detent pocket), OPEN at 180 deg (base circle, no
contact) - so the ramp sprawls over 160 deg: worst pressure angle ~32 -> ~16
deg. Pocket cut R6.2 for pin v4's PRINTED ROLLER (R6 on an M5 screw axle,
user's spec) - rolling contact kills the sliding-friction side load.
Profile: base R16 (clears d21 horn) | concentric crest R27.2 +-10 deg |
raised-cosine ramp 10..170 deg | pocket floor R26.6 (DOC 0.6 over the rim).
Hub: thk 15, d8 bore, d21x3 horn recess (underside). STEP for Fusion."""
import _vtk_shim  # noqa: F401  (stubs WDAC-blocked VTK before cadquery import)
import os, numpy as np, cadquery as cq

OUT = r"D:\Claude\Projects\Grow Home\air_squeeze_valve\step"
os.makedirs(OUT, exist_ok=True)

# --- params (mm / deg) ---
R_LOW      = 16.0    # base circle (pin retracted; clears d21 horn by 5.5)
R_CREST    = 27.2    # concentric crest = pocket rim (transient over-travel)
CREST_HALF = 10.0    # crest concentric half-width
RAMP       = 160.0   # raised-cosine crest->base (10..170 deg)
POCKET_R   = 6.2     # pocket = vertical cylinder cut (printed roller R6 + 0.2)
POCKET_C   = 32.8    # cut center on tip axis -> floor at 32.8-6.2 = R26.6
CAM_TH     = 15.0
BORE       = 8.0
HORN_D     = 21.0
HORN_TH    = 3.0

def cam_radius(theta_deg, tip=0.0):
    d = abs(((theta_deg - tip + 180) % 360) - 180)
    if d <= CREST_HALF:
        return R_CREST
    if d <= CREST_HALF + RAMP:
        t = (d - CREST_HALF) / RAMP
        return R_LOW + (R_CREST - R_LOW) * 0.5 * (1 + np.cos(np.pi * t))
    return R_LOW

# profile points (lobe tip @ +X), 0.25 deg steps
n = 1440
pts = []
for i in range(n):
    th = 360.0 * i / n
    r = cam_radius(th)
    a = np.radians(th)
    pts.append((r*np.cos(a), r*np.sin(a)))

cam = (cq.Workplane("XY")
       .polyline(pts).close()
       .extrude(CAM_TH))

# detent pocket: vertical cylinder cut into the crest at the lobe tip
pocket = (cq.Workplane("XY", origin=(POCKET_C, 0, -1))
          .circle(POCKET_R).extrude(CAM_TH + 2))
cam = cam.cut(pocket)

# bore d8 through all
cam = cam.faces(">Z").workplane().hole(BORE)

# horn recess on UNDERSIDE (z=0): cut d21 x 3 deep
cam = (cam.faces("<Z").workplane()
       .circle(HORN_D/2).cutBlind(-HORN_TH))

path = os.path.join(OUT, "1_cam_v4.step")
cq.exporters.export(cam, path)
print("WROTE", path)
bb = cam.val().BoundingBox()
print("bbox:", round(bb.xlen,2), round(bb.ylen,2), round(bb.zlen,2))
floor = POCKET_C - POCKET_R
half_ang = np.degrees(np.arcsin(POCKET_R*np.sin(np.arccos(
    (POCKET_C**2 + POCKET_R**2 - R_CREST**2)/(2*POCKET_C*POCKET_R)))/R_CREST))
slope = np.pi/2 * (R_CREST - R_LOW) / np.radians(RAMP)   # max mm/rad, raised cosine
pa = np.degrees(np.arctan(slope / ((R_LOW + R_CREST)/2)))
print(f"pocket: floor R{floor:.1f} | rim R{R_CREST} (DOC {R_CREST-floor:.1f}) | span +-{half_ang:.1f} deg (inside +-{CREST_HALF} crest)")
print(f"ramp 10..{CREST_HALF+RAMP:.0f} deg | max slope {slope:.2f} mm/rad | worst pressure angle ~{pa:.1f} deg")
print(f"pin gaps at WALL=53.2, pin L=24: hold {53.2-floor-24:.1f} | crest transient {53.2-R_CREST-24:.1f} | open {53.2-R_LOW-24:.1f}")
