"""
Air squeeze valve (single-lobe cam diverter) - 2D orthographic drawing set.
Generates dimensioned top/front/side PNGs to model in Fusion 360.
Units: millimetres. Lobe tip drawn pointing +X (pinch RIGHT).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrow, Arc, Polygon

OUT = r"D:\Claude\Projects\Grow Home\air_squeeze_valve\drawings"
os.makedirs(OUT, exist_ok=True)

# ---- master parameters -------------------------------------------------
R_LOW   = 7.0     # base-circle radius
R_HOLD  = 17.0    # valley = working pinch radius (hold)
DOC     = 0.6     # over-travel: crest height above valley (latch barrier)
R_PEAK  = R_HOLD + DOC   # 17.6 crests (over-center W crown)
V_HALF  = 5.0     # valley concentric half-width (deg) = servo park tolerance
RISE    = 8.0     # raised-cosine valley->crest (deg)
CROWN   = 3.0     # crest crown width (deg), concentric at R_PEAK
RAMP    = 50.0    # ramp angle each side (deg)
CAM_TH  = 15.0    # cam thickness (>= tube OD 12.7)
TUBE_OD = 12.7
TUBE_ID = 9.525
D_ANVIL = 19.6    # axis -> anvil face
BORE    = 8.0     # central clearance hole for servo spline screw
HORN_D  = 21.0    # metal round horn recess dia
HORN_TH = 3.0     # horn recess depth

LINE = dict(color="black", lw=1.6)
CENT = dict(color="#1f6feb", lw=0.9, ls=(0,(8,4,2,4)))
DIMC = "#c0392b"
HID  = dict(color="0.55", lw=1.0, ls=(0,(5,4)))

def cam_radius(theta_deg, tip=0.0):
    """Over-center W crown (matches part_cam.py)."""
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

def cam_profile(tip=0.0, n=720):
    th = np.linspace(0, 360, n)
    r = np.array([cam_radius(t, tip) for t in th])
    a = np.radians(th)
    return r*np.cos(a), r*np.sin(a)

# ---- dimension helpers -------------------------------------------------
def dimh(ax, x1, x2, y, txt, tick=1.2, dy=0.0):
    ax.annotate("", (x1,y), (x2,y),
                arrowprops=dict(arrowstyle="<->", color=DIMC, lw=1.1))
    for x in (x1,x2):
        ax.plot([x,x],[y-tick,y+tick], color=DIMC, lw=0.8)
    ax.text((x1+x2)/2, y+0.6+dy, txt, color=DIMC, ha="center", va="bottom", fontsize=8.5)

def dimv(ax, y1, y2, x, txt, tick=1.2, side=1):
    ax.annotate("", (x,y1), (x,y2),
                arrowprops=dict(arrowstyle="<->", color=DIMC, lw=1.1))
    for y in (y1,y2):
        ax.plot([x-tick,x+tick],[y,y], color=DIMC, lw=0.8)
    ax.text(x+0.8*side, (y1+y2)/2, txt, color=DIMC, ha="left" if side>0 else "right",
            va="center", fontsize=8.5, rotation=90)

def radial(ax, r, ang, txt, x0=0, y0=0):
    a = np.radians(ang)
    x,y = x0+r*np.cos(a), y0+r*np.sin(a)
    ax.annotate("", (x,y), (x0,y0),
                arrowprops=dict(arrowstyle="->", color=DIMC, lw=1.1))
    ax.text(x0+r*0.55*np.cos(a), y0+r*0.55*np.sin(a)+0.8, txt,
            color=DIMC, fontsize=8.5, ha="center")

def finish(ax, title, xlim, ylim):
    ax.set_aspect("equal"); ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.set_title(title, fontsize=11, fontweight="bold")
    ax.grid(True, color="0.9", lw=0.6); ax.set_axisbelow(True)
    ax.tick_params(labelsize=7)

# =======================================================================
# SHEET 1 - ASSEMBLY TOP (open + pinch states)
# =======================================================================
fig, axs = plt.subplots(1, 2, figsize=(13, 6.5))
for ax, tip, state in ((axs[0], 90.0, "BOTH OPEN  (cam @ 90 deg)"),
                        (axs[1],  0.0, "PINCH RIGHT  (cam @ 0 deg)")):
    cx, cy = cam_profile(tip)
    ax.fill(cx, cy, color="#dbe9ff", ec="black", lw=1.6, zorder=3)
    ax.plot(0,0, marker="+", color="#1f6feb", ms=12, mew=1.5, zorder=4)
    # anvils L/R
    for sgn in (+1,-1):
        ax.add_patch(Rectangle((sgn*D_ANVIL if sgn>0 else -D_ANVIL-12, -10),
                               12, 20, fc="0.8", ec="black", lw=1.4, zorder=1))
    # tubes - compute squeeze on right tube when pinched
    for sgn,label in ((+1,"R"),(-1,"L")):
        cl = sgn*(R_LOW + (D_ANVIL-R_LOW))/2 if True else 0
        cl = sgn*((R_LOW + D_ANVIL)/2)
        pinched = (state.startswith("PINCH") and sgn>0)
        if pinched:
            # flattened tube: gap 2.6 between cam valley(17) and anvil(19.6)
            gap = D_ANVIL - R_HOLD
            ax.add_patch(Rectangle((R_HOLD, -7), gap, 14, fc="#ffd9b3",
                                   ec="#b5651d", lw=1.3, zorder=2))
        else:
            ax.add_patch(Circle((cl,0), TUBE_OD/2, fc="#ffe9d1", ec="#b5651d", lw=1.3, zorder=2))
            ax.add_patch(Circle((cl,0), TUBE_ID/2, fc="white", ec="#b5651d", lw=0.8, zorder=2))
    # servo footprint (dashed)
    ax.add_patch(Rectangle((-20,-10), 40, 20, fill=False, ec="0.5", ls=(0,(5,4)), lw=1.0, zorder=0))
    ax.text(0,-13.5,"DS3225 body 40x20 (under plate)", color="0.5", ha="center", fontsize=7)
    if state.startswith("PINCH"):
        dimh(ax, 0, D_ANVIL, 23, "D = 19.6", dy=0)
        radial(ax, R_HOLD, 35, "R17.0 valley (hold)")
        ax.annotate("2.6 gap (2.0 at crests)", (R_HOLD+ (D_ANVIL-R_HOLD)/2, 9), (24,16),
                    color=DIMC, fontsize=8, arrowprops=dict(arrowstyle="->", color=DIMC))
    else:
        radial(ax, R_LOW, 135, "R7 base")
        dimh(ax, 0, -D_ANVIL, 23, "D = 19.6")
    finish(ax, state, (-40,40), (-18,28))
fig.suptitle("SHEET 1  -  ASSEMBLY TOP VIEW  (air squeeze valve / single-lobe cam diverter)",
             fontsize=12, fontweight="bold")
fig.tight_layout(rect=(0,0,1,0.96))
fig.savefig(os.path.join(OUT,"1_assembly_top.png"), dpi=130); plt.close(fig)

# =======================================================================
# SHEET 2 - ASSEMBLY FRONT (stack heights)
# =======================================================================
fig, ax = plt.subplots(figsize=(9,7))
BASE_TH=5; SERVO_H=40.5; CAM_Z0=13.0  # cam underside = horn underside (VERIFY vs real DS3225 stack)
# base plate
ax.add_patch(Rectangle((-40,0),80,BASE_TH, fc="0.85", ec="black", lw=1.5))
# servo below
ax.add_patch(Rectangle((-20,-SERVO_H),40,SERVO_H, fc="0.7", ec="black", lw=1.4))
ax.text(0,-SERVO_H/2,"DS3225\nservo", ha="center", va="center", fontsize=8)
# shaft
ax.add_patch(Rectangle((-3,0),6,CAM_Z0, fc="0.6", ec="black", lw=1))
# cam
cy0=CAM_Z0
ax.add_patch(Rectangle((-R_PEAK,cy0),2*R_PEAK,CAM_TH, fc="#dbe9ff", ec="black", lw=1.5))
ax.text(0,cy0+CAM_TH/2,"CAM  (dia 35.2 lobe / 14 base)\nthk 15, Z=13 VERIFY", ha="center", va="center", fontsize=8)
# anvils + tube (right); body 25 on 4 foot -> top at 34
for sgn in (+1,-1):
    x = sgn*D_ANVIL if sgn>0 else -D_ANVIL-12
    ax.add_patch(Rectangle((x,BASE_TH),12,29, fc="0.8", ec="black", lw=1.4))
ax.text(D_ANVIL+6, BASE_TH+31,"ANVIL", ha="center", fontsize=8)
# tube vertical in the groove face plane; drops through d15 plate hole
tube_cl = D_ANVIL
ax.add_patch(Rectangle((tube_cl-TUBE_OD/2, -6), TUBE_OD, 46, fc="#ffe9d1",
                       ec="#b5651d", lw=1.2, alpha=0.8))
ax.text(tube_cl, 44,"silicone\ntube (vert)", ha="center", fontsize=7, color="#8a4b16")
dimv(ax, 0, BASE_TH, -44, "5", side=-1)
dimv(ax, cy0, cy0+CAM_TH, 24, "15", side=1)
dimv(ax, -SERVO_H, 0, 30, "40.5", side=1)
ax.text(0, -SERVO_H-5,"(servo shaft is offset ~10mm from body centre on real DS3225 - VERIFY)",
        ha="center", fontsize=7, color="0.4")
finish(ax,"SHEET 2  -  ASSEMBLY FRONT VIEW  (stack heights, mm)", (-50,50), (-SERVO_H-9,52))
fig.tight_layout(); fig.savefig(os.path.join(OUT,"2_assembly_front.png"), dpi=130); plt.close(fig)

# =======================================================================
# SHEET 3 - CAM (top profile + side)
# =======================================================================
fig, axs = plt.subplots(1,2, figsize=(13,6.5))
# top
ax=axs[0]
cx,cy=cam_profile(0.0)
ax.fill(cx,cy, color="#dbe9ff", ec="black", lw=1.8, zorder=2)
ax.plot(0,0, marker="+", color="#1f6feb", ms=14, mew=1.6, zorder=4)
ax.add_patch(Circle((0,0),BORE/2, fc="white", ec="black", lw=1.4, zorder=3))
ax.add_patch(Circle((0,0),HORN_D/2, fill=False, ec="0.55", ls=(0,(5,4)), lw=1.1, zorder=3))
# centerlines
ax.plot([-20,20],[0,0],**CENT); ax.plot([0,0],[-20,20],**CENT)
radial(ax,R_HOLD,4,"R17.0 valley"); radial(ax,R_PEAK,-14.5,"R17.6 crest"); radial(ax,R_LOW,150,"R7")
# W crown + ramp arcs annotation
ax.add_patch(Arc((0,0),2*R_HOLD+3,2*R_HOLD+3, theta1=-V_HALF, theta2=V_HALF, color=DIMC, lw=1.4))
ax.text(R_PEAK+3,0,"valley +-5deg R17.0\n(park/hold; over-center\nwell between crests)", color=DIMC, fontsize=7.5, va="center")
ax.add_patch(Arc((0,0),2*R_PEAK+3,2*R_PEAK+3, theta1=V_HALF, theta2=V_HALF+RISE+CROWN, color="#8e44ad", lw=1.4))
ax.text(11,15,"rise 8deg +\ncrown 3deg\n(crest R17.6)", color="#8e44ad", fontsize=7.5)
ax.add_patch(Arc((0,0),2*R_PEAK+9,2*R_PEAK+9, theta1=V_HALF+RISE+CROWN, theta2=V_HALF+RISE+CROWN+RAMP, color="#117a3d", lw=1.4))
ax.text(6,21,"ramp 50deg", color="#117a3d", fontsize=8)
ax.annotate("Ø8 bore\n(spline screw clr)",(0,0),(-13,-22),color=DIMC,fontsize=8,
            ha="center", arrowprops=dict(arrowstyle="->",color=DIMC))
ax.annotate("Ø21 horn recess\n(3 deep, underside)",( HORN_D/2*np.cos(np.radians(-60)),HORN_D/2*np.sin(np.radians(-60))),
            (16,-20),color="0.4",fontsize=7.5, arrowprops=dict(arrowstyle="->",color="0.5"))
finish(ax,"CAM - TOP (profile, lobe @ +X)", (-26,30), (-26,26))
# side
ax=axs[1]
ax.add_patch(Rectangle((-R_PEAK,0),2*R_PEAK,CAM_TH, fc="#dbe9ff", ec="black", lw=1.8))
# horn recess underside
ax.add_patch(Rectangle((-HORN_D/2,0),HORN_D,HORN_TH, fc="white", ec="0.55", ls=(0,(4,3)), lw=1.1))
# bore
ax.add_patch(Rectangle((-BORE/2,0),BORE,CAM_TH, fill=False, ec="0.55", ls=(0,(4,3)), lw=1.0))
ax.plot([0,0],[-3,CAM_TH+3],**CENT)
dimv(ax,0,CAM_TH,R_PEAK+4,"15", side=1)
dimv(ax,0,HORN_TH,-R_PEAK-4,"3", side=-1)
dimh(ax,-R_PEAK,R_PEAK,-4,"Ø35.2 max (lobe)")
dimh(ax,-HORN_D/2,HORN_D/2,CAM_TH+4,"Ø21 horn recess")
ax.text(0,CAM_TH+8,"underside faces servo", ha="center", fontsize=7, color="0.4")
finish(ax,"CAM - SIDE (section)", (-26,26), (-10,22))
fig.suptitle("SHEET 3  -  CAM  W over-center crown  (print flat; PETG/ABS; capture metal 25T round horn in recess)",
             fontsize=12, fontweight="bold")
fig.tight_layout(rect=(0,0,1,0.95))
fig.savefig(os.path.join(OUT,"3_cam.png"), dpi=130); plt.close(fig)

# =======================================================================
# SHEET 4 - ANVIL (top + front + side)
# =======================================================================
AW=18.0; AH=25.0; AD=12.0; GROOVE_R=6.6; FOOT_OUT=12.0; FOOT_TH=4.0
fig, axs = plt.subplots(1,3, figsize=(15,5.6))
# TOP (looking down: face groove visible)
ax=axs[0]
ax.add_patch(Rectangle((-AW/2,0),AW,AD, fc="0.85", ec="black", lw=1.7))
# groove (half-round) on the cam-facing edge (y=0 side faces cam at -y)
ax.add_patch(Arc((0,0),2*GROOVE_R,2*GROOVE_R, theta1=180, theta2=360, color="black", lw=1.7))
ax.add_patch(Circle((0,0),GROOVE_R, fc="white", ec="none", zorder=0))
ax.plot([0,0],[-GROOVE_R-3,AD+3],**CENT)
dimh(ax,-AW/2,AW/2,AD+3,"18 W")
dimh(ax,-GROOVE_R,GROOVE_R,-GROOVE_R-4,"R6.6 groove (Ø13.2)")
dimv(ax,0,AD,AW/2+3,"12 D", side=1)
ax.text(0, AD+7,"tube nests in groove; cam pushes from -Y", ha="center", fontsize=7, color="0.4")
finish(ax,"ANVIL - TOP", (-18,18), (-12,18))
# FRONT (cam-facing): groove runs vertically full height
ax=axs[1]
ax.add_patch(Rectangle((-AW/2,0),AW,AH, fc="0.85", ec="black", lw=1.7))
ax.add_patch(Rectangle((-GROOVE_R,0),2*GROOVE_R,AH, fc="#eef5ff", ec="0.55", ls=(0,(4,3)), lw=1.1))
# foot (groove is cut through it too, so the tube passes the face)
ax.add_patch(Rectangle((-AW/2,-FOOT_TH),AW,FOOT_TH, fc="0.78", ec="black", lw=1.4))
ax.add_patch(Rectangle((-GROOVE_R,-FOOT_TH),2*GROOVE_R,FOOT_TH, fc="#eef5ff", ec="0.55", ls=(0,(4,3)), lw=1.1))
ax.plot([0,0],[-FOOT_TH-2,AH+2],**CENT)
dimv(ax,0,AH,AW/2+3,"25 H", side=1)
dimh(ax,-GROOVE_R,GROOVE_R,AH+3,"Ø13.2 groove")
ax.text(0,-FOOT_TH-3,"foot", ha="center", fontsize=8)
finish(ax,"ANVIL - FRONT (faces cam)", (-16,16), (-9,33))
# SIDE: foot extends OUTBOARD (+X, away from cam) with the calibration slot
ax=axs[2]
ax.add_patch(Rectangle((0,0),AD,AH, fc="0.85", ec="black", lw=1.7))
ax.add_patch(Rectangle((0,-FOOT_TH),AD+FOOT_OUT,FOOT_TH, fc="0.78", ec="black", lw=1.4))
# slot in the overhang (center 18 behind the face, 4x8)
sx0=AD+FOOT_OUT/2-4
ax.add_patch(Rectangle((sx0,-FOOT_TH+1),8,FOOT_TH-2, fc="white", ec="black", lw=1.1))
ax.add_patch(Arc((sx0,-FOOT_TH/2),FOOT_TH-2,FOOT_TH-2,theta1=90,theta2=270,color="black",lw=1.1))
ax.add_patch(Arc((sx0+8,-FOOT_TH/2),FOOT_TH-2,FOOT_TH-2,theta1=-90,theta2=90,color="black",lw=1.1))
# groove depth on face (left edge faces cam)
ax.add_patch(Arc((0,AH/2),2*(GROOVE_R-3),AH, theta1=90, theta2=270, color="0.55", ls=(0,(4,3)), lw=1.0))
dimv(ax,0,AH,AD+3,"25 H", side=1)
dimh(ax,0,AD,AH+3,"12 D")
dimh(ax,0,AD+FOOT_OUT,-FOOT_TH-3,"foot 24")
ax.annotate("slot 4x8 ctr@18\n(slide to set D; plate screw Y=37.6)",(sx0+4,-FOOT_TH/2),(3,8),
            color=DIMC, fontsize=7.5, arrowprops=dict(arrowstyle="->",color=DIMC))
ax.text(0.5,AH/2,"<-cam side", fontsize=7, color="0.4", rotation=90, va="center")
finish(ax,"ANVIL - SIDE (foot OUTBOARD + slot)", (-6,AD+FOOT_OUT+8), (-9,33))
fig.suptitle("SHEET 4  -  ANVIL v2  (print 2x; groove cradles tube, cut through foot; outboard foot slot = D calibration)",
             fontsize=12, fontweight="bold")
fig.tight_layout(rect=(0,0,1,0.94))
fig.savefig(os.path.join(OUT,"4_anvil.png"), dpi=130); plt.close(fig)

# =======================================================================
# (SHEET 5 removed 2026-07-03: it drew the superseded v1 plate. The base
#  plate v3 top view is generated by part_base_v2.py -> 6_baseplate_v3_top.png)
# =======================================================================

print("WROTE:")
for f in sorted(os.listdir(OUT)):
    print(" ", os.path.join(OUT,f))
