"""Dimensioned 2D sheets for the v3.1 PIN-FOLLOWER air squeeze valve.
Sheet 1  1_assembly_top.png    - plan, BOTH OPEN vs PINCH-A detent hold
Sheet 2  2_assembly_front.png  - Y-Z section, stack heights + hose bays
Sheet 3  3_cam.png             - cam v3.1 profile + detent pocket detail
Sheet 4  4_pin_housing.png     - pin + housing dims
Plain matplotlib env is fine (no cadquery)."""
import os
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon

DRW = r"D:\Claude\Projects\Grow Home\air_squeeze_valve\drawings"
os.makedirs(DRW, exist_ok=True)

# ---- shared geometry (mm) - keep in sync with the part scripts ----
R_LOW, R_CREST, CREST_HALF, RAMP = 16.0, 27.2, 10.0, 75.0
PK_R, PK_C = 4.2, 30.8
PK_FLOOR = PK_C - PK_R                      # 26.6
PIN_L, PIN_W, NOSE_R, PIN_TH = 24.0, 22.0, 4.0, 15.0
WALL, TUBE_Y, TUBE_OD, TUBE_HOLE = 53.2, 46.6, 12.7, 15.0
CH_W, HX, HF, HB = 22.6, 17.3, 28.0, 59.2
BAY_Y0, BAY_Z1 = 39.0, 40.3                 # hose bay start Y / bay top Z (asm)
PL_X, PL_Y, PL_TH = 70.0, 130.0, 5.0
CAM_Z0, CAM_TH = 13.0, 15.0
CH_Z0, CH_Z1, HTOP = 12.7, 28.3, 46.0       # assembly Z
BODY_CX, BODY_X, BODY_Y = -5.7, 40.5, 20.5

def cam_r(d):
    d = abs(((d + 180) % 360) - 180)
    if d <= CREST_HALF: return R_CREST
    if d <= CREST_HALF + RAMP:
        t = (d - CREST_HALF) / RAMP
        return R_LOW + (R_CREST - R_LOW) * 0.5 * (1 + np.cos(np.pi * t))
    return R_LOW

def cam_r_p(d):
    r = cam_r(d)
    dd = abs(((d + 180) % 360) - 180)
    s = PK_C * np.sin(np.radians(dd))
    if s < PK_R and dd < 90:   # pocket exists only around the tip
        near = PK_C * np.cos(np.radians(dd)) - np.sqrt(PK_R**2 - s**2)
        if near < r: r = near
    return r

def cam_xy(tip_deg):
    th = np.linspace(0, 360, 1441)
    r = np.array([cam_r_p(t - tip_deg) for t in th])
    a = np.radians(th)
    return r * np.cos(a), r * np.sin(a)

def pin_poly(nose_r, sgn):
    pts = [(-PIN_W/2, 24.0), (-PIN_W/2, 10.0), (-5.0, 4.0)]
    for a in np.linspace(np.pi, 2*np.pi, 33):
        pts.append((NOSE_R*np.cos(a), 4.0 + NOSE_R*np.sin(a)))
    pts += [(5.0, 4.0), (PIN_W/2, 10.0), (PIN_W/2, 24.0)]
    return [(x, sgn*(nose_r + y)) for (x, y) in pts]

def draw_housing_plan(ax, sgn):
    y0 = HF if sgn > 0 else -HB
    ax.add_patch(Rectangle((-11.3, min(sgn*HF, sgn*WALL)), 22.6, WALL-HF,
                           fc="#faf7f0", ec="none", zorder=1))          # channel floor
    for xs in (-1, +1):                                                  # side walls
        ax.add_patch(Rectangle((xs*HX - (0 if xs<0 else 6), y0), 6, HB-HF,
                               fc="#e8e2d4", ec="black", lw=1.3, zorder=2))
    wy0 = WALL if sgn > 0 else -HB                                       # end wall
    ax.add_patch(Rectangle((-HX, wy0), 2*HX, HB-WALL,
                           fc="#e8e2d4", ec="black", lw=1.3, zorder=2))
    ax.plot([-11.3, 11.3], [sgn*WALL]*2, color="#8a4b16", lw=2.0, zorder=3)
    ax.add_patch(Circle((0, sgn*TUBE_Y), TUBE_HOLE/2, fill=False,
                        ec="0.45", ls=(0, (3, 2)), lw=1.1, zorder=4))    # roof bore

def draw_state(ax, tip_deg, noseA, noseB, title, pinched_side=None):
    ax.add_patch(Rectangle((-PL_X/2, -PL_Y/2), PL_X, PL_Y, fc="#f2efe6", ec="black", lw=1.6))
    ax.add_patch(Rectangle((BODY_CX-BODY_X/2, -BODY_Y/2), BODY_X, BODY_Y,
                           fc="#f4b7b0", ec="#b03a2e", lw=1.2, alpha=.75, zorder=1))
    for sgn in (+1, -1):
        draw_housing_plan(ax, sgn)
    # tubes
    for sgn, nose in ((+1, noseA), (-1, noseB)):
        if pinched_side == sgn:
            ax.add_patch(Rectangle((-10, sgn*min(nose+PIN_L, WALL) if sgn>0 else sgn*WALL),
                                   20, WALL-(nose+PIN_L), fc="#f0b27a", ec="#8a4b16", lw=1.3, zorder=5))
        else:
            ax.add_patch(Circle((0, sgn*TUBE_Y), TUBE_OD/2, fc="#f8dcbf", ec="#8a4b16", lw=1.3, zorder=5))
    # pins
    for sgn, nose in ((+1, noseA), (-1, noseB)):
        ax.add_patch(Polygon(pin_poly(nose, sgn), closed=True,
                             fc="#a9dfbf", ec="#145a32", lw=1.4, zorder=6))
    # cam
    cx, cy = cam_xy(tip_deg)
    ax.fill(cx, cy, color="#9fd0ff", ec="black", lw=1.5, zorder=7, alpha=.92)
    ax.plot(0, 0, marker="+", color="#1f6feb", ms=14, mew=2, zorder=8)
    ax.set_aspect("equal"); ax.set_xlim(-42, 42); ax.set_ylim(-73, 73)
    ax.grid(True, color="0.92"); ax.set_axisbelow(True); ax.tick_params(labelsize=7)
    ax.set_title(title, fontsize=10, fontweight="bold")

# ================= SHEET 1 - assembly top, two states =================
fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.5, 9.6))
draw_state(a1, 0, R_LOW, R_LOW, "BOTH OPEN  (cam @ 90 deg, tip -> +X)")
a1.annotate("", (0, R_LOW+PIN_L), (0, WALL), arrowprops=dict(arrowstyle="<->", color="#c0392b", lw=1.2))
a1.text(12.8, 44.0, "open gap 13.2\n(hose OD 12.7)", color="#c0392b", fontsize=8)
a1.text(0, -68, "pins retracted on base circle R16; both hoses open\n(base R16 > horn R10.5: nose never touches the servo)", ha="center", fontsize=8)

draw_state(a2, 90, PK_FLOOR, R_LOW, "PINCH A - DETENT HOLD  (cam @ 0 deg, tip -> +Y)", pinched_side=+1)
a2.annotate("", (0, PK_FLOOR+PIN_L), (0, WALL), arrowprops=dict(arrowstyle="<->", color="#c0392b", lw=1.2))
a2.text(-41, 40, "seal 2.6\n(2.0 crossing\nthe rim)", color="#c0392b", fontsize=8)
a2.annotate("nose R4 parked in R4.2 pocket\n(floor R26.6, rim R27.2)\nhose spring = the latch",
            (0, PK_FLOOR), (-41, 58), color="#145a32", fontsize=8,
            arrowprops=dict(arrowstyle="->", color="#145a32"))
a2.annotate("backstop wall Y=53.2\n(printed into housing)", (11.3, WALL), (14, 66),
            color="#8a4b16", fontsize=7.5, arrowprops=dict(arrowstyle="->", color="#8a4b16"))
a2.text(0, -68, "0 deg = pinch A | 90 = both open | 180 = pinch B (stock 180 servo)", ha="center", fontsize=8)
fig.suptitle("SHEET 1  -  ASSEMBLY TOP VIEW  (v3.1 pin-follower air squeeze valve)", fontsize=13, fontweight="bold")
fig.tight_layout(rect=(0, 0, 1, 0.96))
fig.savefig(os.path.join(DRW, "1_assembly_top.png"), dpi=130); print("WROTE 1_assembly_top.png")

# ================= SHEET 2 - front (Y-Z section), pinch-A pose =================
fig, ax = plt.subplots(figsize=(12, 9))
# plate (with servo cutout gap)
for y0, y1 in ((-PL_Y/2, -BODY_Y/2), (BODY_Y/2, PL_Y/2)):
    ax.add_patch(Rectangle((y0, 0), y1-y0, PL_TH, fc="#dcd6c6", ec="black", lw=1.3))
# servo
ax.add_patch(Rectangle((-10, 11-40.5), 20, 40.5, fc="#f4b7b0", ec="#b03a2e", lw=1.3))
ax.add_patch(Rectangle((-10, -2.5), 20, 2.5, fc="#f4b7b0", ec="#b03a2e", lw=1.0))
ax.add_patch(Rectangle((-6.5, 11), 13, 1.5, fc="#c0392b", ec="#b03a2e"))
ax.add_patch(Rectangle((-3, 12.5), 6, 3.5, fc="#c0392b", ec="#b03a2e"))
ax.text(0, -12, "DS3225 servo\n(shaft offset ~10 from body ctr - VERIFY)", ha="center", fontsize=8, color="#7b241c")
# horn + cam
ax.add_patch(Rectangle((-10.5, CAM_Z0), 21, 3, fc="#aec6f5", ec="#1a3f8f", lw=1.2))
ax.add_patch(Rectangle((-R_LOW, CAM_Z0), R_LOW+PK_FLOOR, CAM_TH, fc="#9fd0ff", ec="black", lw=1.4))
ax.text(5, CAM_Z0+CAM_TH/2, "CAM v3.1\n(section thru tip)", ha="center", va="center", fontsize=8)
# housings, both sides: front block (lower slab + upper block), ghost roof w/ bore, end wall
for sgn in (+1, -1):
    for (z0, z1) in ((PL_TH, CH_Z0), (CH_Z1, HTOP)):
        y0, y1 = sgn*HF, sgn*BAY_Y0
        ax.add_patch(Rectangle((min(y0, y1), z0), abs(y1-y0), z1-z0, fc="#e8e2d4", ec="black", lw=1.0))
    y0, y1 = sgn*BAY_Y0, sgn*WALL   # raised roof over the bay (all bore at X=0 section)
    ax.add_patch(Rectangle((min(y0, y1), BAY_Z1), abs(y1-y0), HTOP-BAY_Z1,
                           fill=False, ec="0.4", lw=1.1, ls=(0, (3, 2))))
    y0, y1 = sgn*WALL, sgn*HB       # end wall
    ax.add_patch(Rectangle((min(y0, y1), PL_TH), HB-WALL, HTOP-PL_TH, fc="#d5cdba", ec="black", lw=1.3))
# tubes (vertical); A pinched at the channel window
ax.add_patch(Rectangle((-TUBE_Y-TUBE_OD/2, -12), TUBE_OD, 68, fc="#f8dcbf", ec="#8a4b16", lw=1.2, alpha=.85))
for (z0, z1) in ((-12, CH_Z0), (CH_Z1, 56)):
    ax.add_patch(Rectangle((TUBE_Y-TUBE_OD/2, z0), TUBE_OD, z1-z0, fc="#f8dcbf", ec="#8a4b16", lw=1.2, alpha=.85))
ax.add_patch(Rectangle((PK_FLOOR+PIN_L, CH_Z0), WALL-(PK_FLOOR+PIN_L), CH_Z1-CH_Z0, fc="#f0b27a", ec="#8a4b16", lw=1.3))
# pins
ax.add_patch(Rectangle((PK_FLOOR, CAM_Z0), PIN_L, PIN_TH, fc="#a9dfbf", ec="#145a32", lw=1.4))
ax.add_patch(Rectangle((-R_LOW-PIN_L, CAM_Z0), PIN_L, PIN_TH, fc="#a9dfbf", ec="#145a32", lw=1.4))
ax.text(PK_FLOOR+PIN_L/2, CAM_Z0+PIN_TH+2.2, "pin A (sealed)", ha="center", fontsize=8, color="#145a32")
ax.text(-R_LOW-PIN_L/2, CAM_Z0+PIN_TH+2.2, "pin B (open)", ha="center", fontsize=8, color="#145a32")
# dims
ax.annotate("", (68, 0), (68, PL_TH), arrowprops=dict(arrowstyle="<->", color="#c0392b", lw=1.1))
ax.text(69.5, 2.5, "plate 5", fontsize=7.5, color="#c0392b", va="center")
ax.annotate("", (68, CH_Z0), (68, CH_Z1), arrowprops=dict(arrowstyle="<->", color="#c0392b", lw=1.1))
ax.text(69.5, (CH_Z0+CH_Z1)/2, "channel\n12.7-28.3", fontsize=7.5, color="#c0392b", va="center")
ax.annotate("", (68, CH_Z1), (68, BAY_Z1), arrowprops=dict(arrowstyle="<->", color="#8a4b16", lw=1.1))
ax.text(69.5, (CH_Z1+BAY_Z1)/2, "hose bay\n12 free", fontsize=7.5, color="#8a4b16", va="center")
ax.annotate("", (-68, CAM_Z0), (-68, CAM_Z0+CAM_TH), arrowprops=dict(arrowstyle="<->", color="#1a3f8f", lw=1.1))
ax.text(-83, CAM_Z0+CAM_TH/2, "cam+pins\n13-28\n(CAM_Z0=13\nVERIFY)", fontsize=7.5, color="#1a3f8f", va="center")
ax.annotate("", (0, 33), (WALL, 33), arrowprops=dict(arrowstyle="<->", color="#8a4b16", lw=1.1))
ax.text(WALL/2 - 8, 34.5, "wall face 53.2", ha="center", fontsize=7.5, color="#8a4b16")
ax.annotate("raised roof w/ d15 guide bore (dashed; the section\nplane removes it) - hose guided 12 ABOVE the pinch\nand ~8 below (plate hole), free to go round->slot between",
            (TUBE_Y, BAY_Z1+3), (2, 52), fontsize=8, color="0.25",
            arrowprops=dict(arrowstyle="->", color="0.4"))
ax.annotate("hose drops thru plate d15 (1.5 funnel);\n1/2\" barbs below the plate",
            (TUBE_Y, -10), (8, -24), fontsize=8, color="#8a4b16",
            arrowprops=dict(arrowstyle="->", color="#8a4b16"))
ax.set_aspect("equal"); ax.set_xlim(-88, 88); ax.set_ylim(-46, 62)
ax.grid(True, color="0.92"); ax.set_axisbelow(True); ax.tick_params(labelsize=7)
ax.set_title("SHEET 2  -  ASSEMBLY FRONT (Y-Z section, pinch-A hold; Z=0 = plate bottom)", fontsize=12, fontweight="bold")
fig.tight_layout()
fig.savefig(os.path.join(DRW, "2_assembly_front.png"), dpi=130); print("WROTE 2_assembly_front.png")

# ================= SHEET 3 - cam v3.1 =================
fig, (ax, axz) = plt.subplots(1, 2, figsize=(13, 7.2), gridspec_kw={"width_ratios": [1.35, 1]})
cx, cy = cam_xy(0)
for A in (ax, axz):
    A.fill(cx, cy, color="#9fd0ff", ec="black", lw=1.6, alpha=.92)
    A.set_aspect("equal"); A.grid(True, color="0.92"); A.set_axisbelow(True); A.tick_params(labelsize=7)
ax.add_patch(Circle((0, 0), 4, fc="white", ec="black", lw=1.2))
ax.add_patch(Circle((0, 0), 10.5, fill=False, ec="#1a3f8f", ls=(0, (5, 4)), lw=1.1))
ax.text(-8, -14.5, "horn recess d21 x 3 (underside)\nbase R16 > horn R10.5 ->\nnose can NEVER touch the horn", fontsize=7.5, color="#1a3f8f")
ax.text(0.2, 5.6, "bore d8", fontsize=7.5, ha="center")
ax.add_patch(Circle((0, 0), R_LOW, fill=False, ec="0.5", ls=(0, (2, 2)), lw=0.9))
ax.annotate("", (0, 0), (R_LOW*np.cos(2.62), R_LOW*np.sin(2.62)), arrowprops=dict(arrowstyle="<-", color="0.3", lw=1.0))
ax.text(-15.5, 9.6, "R16 base", fontsize=8)
ax.annotate("", (0, 0), (R_CREST*np.cos(0.35), R_CREST*np.sin(0.35)), arrowprops=dict(arrowstyle="<-", color="0.3", lw=1.0))
ax.text(14.5, 11.6, "R27.2 crest", fontsize=8)
for a_deg, lbl, (tx, ty) in ((10, "crest +-10 deg", (29.5, 6.2)), (85, "ramp end 85 deg", (-13.5, 30.0))):
    for s in (+1, -1):
        a = np.radians(s*a_deg)
        ax.plot([0, 29*np.cos(a)], [0, 29*np.sin(a)], color="0.6", lw=0.8, ls=(0, (4, 3)))
    ax.text(tx, ty, lbl, fontsize=7.5, color="0.35")
ax.set_xlim(-34, 42); ax.set_ylim(-32, 32)
ax.set_title("CAM v3.1  (thk 15; raised-cosine ramp 10->85 deg; pressure angle <= ~32 deg)", fontsize=10, fontweight="bold")
# pocket zoom
axz.add_patch(Circle((PK_C, 0), PK_R, fill=False, ec="#c0392b", ls=(0, (4, 3)), lw=1.2))
axz.plot(PK_C, 0, "+", color="#c0392b", ms=10, mew=1.6)
nose = Circle((PK_FLOOR + NOSE_R, 0), NOSE_R, fill=False, ec="#145a32", lw=1.4)
axz.add_patch(nose)
axz.text(PK_FLOOR + NOSE_R, 5.1, "pin nose R4.0\n(parked)", fontsize=8, color="#145a32", ha="center")
axz.annotate("pocket cut R4.2\ncenter at R30.8", (PK_C, -PK_R), (28.5, -8.5), fontsize=8, color="#c0392b",
             arrowprops=dict(arrowstyle="->", color="#c0392b"))
axz.annotate("", (PK_FLOOR, 2.8), (R_CREST, 2.8), arrowprops=dict(arrowstyle="<->", color="black", lw=1.0))
axz.text((PK_FLOOR+R_CREST)/2, 3.3, "DOC 0.6", fontsize=7.5, ha="center")
axz.text(23.2, -6.6, "floor R26.6 | rim R27.2 | span +-4.3 deg\nescape re-squeezes hose 0.6 over the rim\n= bistable hold, servo de-energizes", fontsize=7.5)
axz.set_xlim(22.5, 33.5); axz.set_ylim(-9, 7)
axz.set_title("DETENT POCKET detail (lobe tip)", fontsize=10, fontweight="bold")
fig.suptitle("SHEET 3  -  CAM v3.1 with hard detent pocket (pin-follower)", fontsize=13, fontweight="bold")
fig.tight_layout(rect=(0, 0, 1, 0.95))
fig.savefig(os.path.join(DRW, "3_cam.png"), dpi=130); print("WROTE 3_cam.png")

# ================= SHEET 4 - pin + housing =================
fig, (ap, ah) = plt.subplots(1, 2, figsize=(13, 8.6))
# pin plan (local frame, nose down)
ap.add_patch(Polygon([(x, y) for (x, y) in pin_poly(0, +1)], closed=True,
                     fc="#a9dfbf", ec="#145a32", lw=1.6))
ap.annotate("", (-PIN_W/2, 26), (PIN_W/2, 26), arrowprops=dict(arrowstyle="<->", color="black", lw=1.0))
ap.text(0, 27, "22.0  (channel 22.6)", ha="center", fontsize=8)
ap.annotate("", (14, 0), (14, 24), arrowprops=dict(arrowstyle="<->", color="black", lw=1.0))
ap.text(15, 12, "24.0 nose tip -> blade face", fontsize=8, rotation=90, va="center")
ap.annotate("nose: vertical half-cylinder R4.0\n(line contact; drops into cam pocket)", (0, 0), (-24, -7),
            fontsize=8, color="#145a32", arrowprops=dict(arrowstyle="->", color="#145a32"))
ap.annotate("plan chamfer (+-5 -> +-11 over 6)\nso the crest sweep can't graze", (8, 7), (13, -4),
            fontsize=8, arrowprops=dict(arrowstyle="->", color="0.3"))
ap.text(0, 21.4, "BLADE face (flat)", ha="center", fontsize=8, color="#145a32")
ap.text(0, -13, "thickness 15.0 (channel 15.6) | print x2 | dry / PTFE film only (NO silicone grease)", ha="center", fontsize=8)
ap.set_aspect("equal"); ap.set_xlim(-30, 30); ap.set_ylim(-16, 30)
ap.grid(True, color="0.92"); ap.set_axisbelow(True); ap.tick_params(labelsize=7)
ap.set_title("PINCH PIN (plan; travel = Y) - unchanged in v3.1", fontsize=10, fontweight="bold")
# housing plan
draw_housing_plan(ah, +1)
ah.add_patch(Polygon(pin_poly(R_LOW, +1), closed=True, fc="#a9dfbf", ec="#145a32", lw=1.2, alpha=.55))
for (sx, sy) in ((14, 31), (-14, 31), (14, 56.2), (-14, 56.2)):
    ah.add_patch(Circle((sx, sy), 1.4, fc="white", ec="black", lw=1.0, zorder=6))
ah.annotate("", (-11.3, 33), (11.3, 33), arrowprops=dict(arrowstyle="<->", color="black", lw=1.0))
ah.text(0, 34.2, "channel 22.6 (Z 12.7-28.3)", ha="center", fontsize=7.5)
ah.annotate("", (20, HF), (20, WALL), arrowprops=dict(arrowstyle="<->", color="black", lw=1.0))
ah.text(21, 40, "front 28 -> wall 53.2", fontsize=7.5, rotation=90, va="center")
ah.annotate("backstop wall face Y=53.2\n(sets the 2.6 seal - PRINTED, no bench cal)", (0, WALL), (-38, 66),
            fontsize=8, color="#8a4b16", arrowprops=dict(arrowstyle="->", color="#8a4b16"))
ah.annotate("d15 hose bore in RAISED roof (Z 40.3-46) at Y=46.6;\nbelow it an open bay to the plate - hose free to\nflatten for 12 above / ~8 below the pinch", (TUBE_HOLE/2, TUBE_Y), (22, 73),
            fontsize=8, color="0.3", arrowprops=dict(arrowstyle="->", color="0.3"))
ah.annotate("4x d2.8 pilots, 7 deep\n(M3 self-tap from below plate)", (14, 31), (24, 16),
            fontsize=8, arrowprops=dict(arrowstyle="->", color="0.3"))
ah.text(0, 10, "pin shown retracted (ghost);\nguided 12 retracted / 22.6 sealed", ha="center", fontsize=7.5, color="#145a32")
ah.set_aspect("equal"); ah.set_xlim(-42, 42); ah.set_ylim(4, 80)
ah.grid(True, color="0.92"); ah.set_axisbelow(True); ah.tick_params(labelsize=7)
ah.set_title("PIN HOUSING v3.1 (plan; print x2 of same part, B rotated 180)", fontsize=10, fontweight="bold")
fig.suptitle("SHEET 4  -  PIN + HOUSING", fontsize=13, fontweight="bold")
fig.tight_layout(rect=(0, 0, 1, 0.95))
fig.savefig(os.path.join(DRW, "4_pin_housing.png"), dpi=130); print("WROTE 4_pin_housing.png")
print("done")
