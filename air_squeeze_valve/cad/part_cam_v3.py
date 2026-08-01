"""CAM v3 - single-lobe pin-follower cam with a hard DETENT POCKET.
Replaces the v2 "W crown": that tried to make an over-center detent out of
cam-vs-silicone, but the tube just conforms and the hold was mush. In v3 the
cam pushes a rigid guided PINCH PIN (part_pin.py); the tube's restoring force
presses the pin's R4 nose back onto the cam, and at full pinch the nose drops
into an R4.2 pocket cut into the crest -> crisp hard-on-hard bistable hold at
0/180 deg, servo can de-energize. Escaping the pocket re-squeezes the tube by
DOC=0.6 over the rim (same over-travel physics as the W, right materials).
v3.1 (user Fusion review): cam grown A LOT - base R7 -> R16 so the base circle
clears the d21 horn (old R7 base < horn R10.5: at rest the nose sat on the
EXPOSED HORN, not the cam) and the ramp stretched 50 -> 75 deg of rotation
(worst pressure angle ~45 -> ~32 deg, under the ~40 jam zone for sliders).
Profile: base R16 | concentric crest R27.2 +-10 deg | raised-cosine ramp to
85 deg | pocket floor R26.6. Hub unchanged: thk 15, d8 bore, d21x3 horn
recess (underside). STEP export for Fusion."""
import _vtk_shim  # noqa: F401  (stubs WDAC-blocked VTK before cadquery import)
import os, numpy as np, cadquery as cq

OUT = r"D:\Claude\Projects\Grow Home\air_squeeze_valve\step"
os.makedirs(OUT, exist_ok=True)

# --- params (mm / deg) ---
R_LOW      = 16.0    # base circle (pin retracted; clears d21 horn by 5.5)
R_CREST    = 27.2    # concentric crest = pocket rim (transient over-travel)
CREST_HALF = 10.0    # crest concentric half-width
RAMP       = 75.0    # raised-cosine crest->base (10..85 deg)
POCKET_R   = 4.2     # pocket = vertical cylinder cut (pin nose R4.0 + 0.2)
POCKET_C   = 30.8    # cut center on tip axis -> floor at 30.8-4.2 = R26.6
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

path = os.path.join(OUT, "1_cam_v3.step")
cq.exporters.export(cam, path)
print("WROTE", path)
bb = cam.val().BoundingBox()
print("bbox:", round(bb.xlen,2), round(bb.ylen,2), round(bb.zlen,2))
floor = POCKET_C - POCKET_R
half_ang = np.degrees(np.arcsin(POCKET_R*np.sin(np.arccos(
    (POCKET_C**2 + POCKET_R**2 - R_CREST**2)/(2*POCKET_C*POCKET_R)))/R_CREST))
print(f"pocket: floor R{floor:.1f} | rim R{R_CREST} (DOC {R_CREST-floor:.1f}) | span +-{half_ang:.1f} deg (inside +-{CREST_HALF} crest)")
print(f"pin gaps at WALL=53.2, pin L=24: hold {53.2-floor-24:.1f} | crest transient {53.2-R_CREST-24:.1f} | open {53.2-R_LOW-24:.1f}")
