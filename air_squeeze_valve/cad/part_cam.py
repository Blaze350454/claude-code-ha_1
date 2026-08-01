"""Part 1 of 3: CAM - single-lobe air-squeeze diverter cam, over-center W crown.
The old 24 deg concentric dwell (neutral hold) is replaced by a W: a concentric
VALLEY at the working pinch radius R17.0 (+-5 deg = servo park tolerance) flanked
by two CRESTS at R17.6 (0.6 mm over-travel). Leaving the hold in either direction
must re-squeeze the tube over a crest, so each pinch is a bistable well and the
servo can de-energize (auto_detach). Holds stay at 0/180 deg -> stock 180 deg
DS3225 travel; anvils/base plate unchanged by this change. STEP export for Fusion."""
import _vtk_shim  # noqa: F401  (stubs WDAC-blocked VTK before cadquery import)
import os, numpy as np, cadquery as cq

OUT = r"D:\Claude\Projects\Grow Home\air_squeeze_valve\step"
os.makedirs(OUT, exist_ok=True)

# --- params (mm / deg) ---
R_LOW   = 7.0     # base circle (open ~ tube OD gap at D=19.6)
R_HOLD  = 17.0    # valley = working pinch radius (seal gap 2.6 at D=19.6)
DOC     = 0.6     # over-travel: crest above valley = latch barrier depth
R_PEAK  = R_HOLD + DOC          # 17.6 (transient gap 2.0 while crossing)
V_HALF  = 5.0     # valley concentric half-width (park tolerance)
RISE    = 8.0     # raised-cosine valley->crest (steeper = stronger latch)
CROWN   = 3.0     # crest crown width, concentric at R_PEAK
RAMP    = 50.0    # raised-cosine crest->base circle
CAM_TH  = 15.0
BORE    = 8.0
HORN_D  = 21.0
HORN_TH = 3.0

def cam_radius(theta_deg, tip=0.0):
    d = abs(((theta_deg - tip + 180) % 360) - 180)
    if d <= V_HALF:
        return R_HOLD
    if d <= V_HALF + RISE:
        t = (d - V_HALF) / RISE
        return R_HOLD + DOC * 0.5 * (1 - np.cos(np.pi * t))
    if d <= V_HALF + RISE + CROWN:
        return R_PEAK
    if d <= V_HALF + RISE + CROWN + RAMP:
        t = (d - V_HALF - RISE - CROWN) / RAMP
        return R_LOW + (R_PEAK - R_LOW) * 0.5 * (1 + np.cos(np.pi * t))
    return R_LOW

# profile points (lobe @ +X); 0.25 deg steps so the small W features are smooth
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

# bore d8 through all
cam = cam.faces(">Z").workplane().hole(BORE)

# horn recess on UNDERSIDE (z=0): cut d21 x 3 deep
cam = (cam.faces("<Z").workplane()
       .circle(HORN_D/2).cutBlind(-HORN_TH))

path = os.path.join(OUT, "1_cam.step")
cq.exporters.export(cam, path)
print("WROTE", path)
print("bbox:", cam.val().BoundingBox().xlen, cam.val().BoundingBox().ylen, cam.val().BoundingBox().zlen)
HALF_LOBE = V_HALF + RISE + CROWN + RAMP
print(f"W crown: valley R{R_HOLD} +-{V_HALF}deg | crests R{R_PEAK} at +-{V_HALF+RISE+CROWN/2}deg | half-lobe {HALF_LOBE}deg")
print(f"gaps at D=19.6: hold {19.6-R_HOLD:.1f} | crest transient {19.6-R_PEAK:.1f} | open {19.6-R_LOW:.1f}")
