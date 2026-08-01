"""Base plate v5 - SINGLE VALVE UNIT plate (print x2, one per hose).
Twin-servo architecture (2026-07-04): each hose gets its own DS3225 + cam +
pin + housing on its own compact plate, mounted wherever that hose runs.
Origin = servo OUTPUT SHAFT; servo long axis = X; the one housing sits on +Y
(front 28, wall 53.2, hose 46.6 - identical to the v3.1 shared-plate side).
Corner d4.2 holes mount the unit to the bench/frame.
Outputs STEP + top-view PNG."""
import _vtk_shim  # noqa: F401  (stubs WDAC-blocked VTK before cadquery import)
import os, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import cadquery as cq

OUT = r"D:\Claude\Projects\Grow Home\air_squeeze_valve\step"
DRW = r"D:\Claude\Projects\Grow Home\air_squeeze_valve\drawings"
os.makedirs(OUT, exist_ok=True); os.makedirs(DRW, exist_ok=True)

# --- servo / tab geometry (origin = shaft) ---
TAB_R_X   =  19.05      # shaft -> right tab line
TAB_L_X   = -30.45      # shaft -> left  tab line
TAB_DY    =  5.0        # tabs at Y = +-5
BODY_CX   = (TAB_R_X + TAB_L_X)/2   # body center X = -5.70
BODY_X, BODY_Y = 40.5, 20.5         # body cutout (clearance)
TAB_SCREW_D  = 3.5

# --- the one housing on +Y (part_housing.py, unchanged from v3.1) ---
HSG_SCREW_D  = 3.4      # M3 clearance; self-tap into d2.8 pilots above
HSG_SCREWS   = [(14, 31.0), (-14, 31.0), (14, 56.2), (-14, 56.2)]
TUBE_Y       = 46.6
TUBE_HOLE_D  = 15.0     # hose OD 12.7 drop-through (barbs connect below plate)
MOUNT_D      = 4.2      # corner mounting holes
MOUNTS       = [(30, -18), (-30, -18), (30, 60), (-30, 60)]
# --- plate: X 70, Y -24..66 ---
PL_X, PL_TH  = 70.0, 5.0
PL_Y0, PL_Y1 = -24.0, 66.0
PL_Y  = PL_Y1 - PL_Y0
PL_CY = (PL_Y0 + PL_Y1)/2

# ---------- STEP ----------
plate = cq.Workplane("XY").box(PL_X, PL_Y, PL_TH).translate((0, PL_CY, PL_TH/2))
cut = cq.Workplane("XY").box(BODY_X, BODY_Y, PL_TH+4).translate((BODY_CX, 0, PL_TH/2))
plate = plate.cut(cut)
holes = ([(TAB_R_X, TAB_DY), (TAB_R_X, -TAB_DY), (TAB_L_X, TAB_DY), (TAB_L_X, -TAB_DY)]
         + HSG_SCREWS)
for (hx, hy) in holes:
    d = TAB_SCREW_D if abs(hx) > 15 else HSG_SCREW_D
    plate = plate.cut(cq.Workplane("XY", origin=(hx, hy, -1)).circle(d/2).extrude(PL_TH+2))
for (hx, hy) in MOUNTS:
    plate = plate.cut(cq.Workplane("XY", origin=(hx, hy, -1)).circle(MOUNT_D/2).extrude(PL_TH+2))
plate = plate.cut(cq.Workplane("XY", origin=(0, TUBE_Y, -1)).circle(TUBE_HOLE_D/2).extrude(PL_TH+2))
fun = (cq.Workplane("XY", origin=(0, TUBE_Y, PL_TH))
       .circle(TUBE_HOLE_D/2 + 1.5).workplane(offset=-1.5).circle(TUBE_HOLE_D/2)
       .loft(combine=True))
plate = plate.cut(fun)
spath = os.path.join(OUT, "3_base_plate_v5.step")
cq.exporters.export(plate, spath)
bb = plate.val().BoundingBox()
print("WROTE", spath, "bbox", round(bb.xlen,1), round(bb.ylen,1), round(bb.zlen,1))

# ---------- top-view diagram ----------
fig, ax = plt.subplots(figsize=(8.5, 10))
ax.add_patch(Rectangle((-PL_X/2, PL_Y0), PL_X, PL_Y, fc="#f2efe6", ec="black", lw=1.8))
ax.add_patch(Rectangle((BODY_CX-BODY_X/2, -BODY_Y/2), BODY_X, BODY_Y, fc="#f4b7b0", ec="#b03a2e", lw=1.4, alpha=.8))
ax.text(BODY_CX, 0, "servo body\n(hangs below)", ha="center", va="center", fontsize=8, color="#7b241c")
for x in (TAB_R_X, TAB_L_X):
    for y in (TAB_DY, -TAB_DY):
        ax.add_patch(Circle((x, y), TAB_SCREW_D/2, fc="white", ec="black", lw=1.1))
ax.plot(0, 0, marker="+", color="#1f6feb", ms=16, mew=2, zorder=6)
ax.add_patch(Circle((0, 0), 27.2, fill=False, ec="#1f6feb", ls=(0, (5, 4)), lw=1.1))
ax.text(17, -23, "crest sweep\nR27.2", fontsize=7, color="#1f6feb")
ax.add_patch(Rectangle((-17.3, 28), 34.6, 31.2, fill=False, ec="0.35", lw=1.2, ls=(0, (4, 3))))
ax.plot([-17.3, 17.3], [53.2]*2, color="#8a4b16", lw=1.6)
for (sx, sy) in HSG_SCREWS:
    ax.add_patch(Circle((sx, sy), HSG_SCREW_D/2, fc="white", ec="black", lw=1.1, zorder=3))
for (sx, sy) in MOUNTS:
    ax.add_patch(Circle((sx, sy), MOUNT_D/2, fc="white", ec="#1f6feb", lw=1.3, zorder=3))
ax.add_patch(Circle((0, TUBE_Y), TUBE_HOLE_D/2, fc="white", ec="#8a4b16", lw=1.4, zorder=2))
ax.annotate("", (0, 2), (0, TUBE_Y-1), arrowprops=dict(arrowstyle="<->", color="#c0392b", lw=1.2))
ax.text(1.4, 24, "hose Y=46.6", color="#c0392b", fontsize=8, va="center", rotation=90)
ax.annotate("housing screws d3.4\nM3 self-tap from below", (14, 31), (23, 38),
            color="black", fontsize=7.5, arrowprops=dict(arrowstyle="->", color="0.4"))
ax.annotate("backstop wall Y=53.2", (15, 53.2), (21, 61),
            color="#8a4b16", fontsize=7.5, arrowprops=dict(arrowstyle="->", color="#8a4b16"))
ax.annotate("d4.2 unit mounting x4", (30, -18), (5, -22),
            color="#1f6feb", fontsize=7.5, arrowprops=dict(arrowstyle="->", color="#1f6feb"))
ax.text(0, 70, "ONE VALVE UNIT - print x2 (feed + flush)", ha="center", fontsize=9, fontweight="bold")
ax.set_aspect("equal"); ax.set_xlim(-44, 44); ax.set_ylim(-32, 76)
ax.set_title("BASE PLATE v5 - TOP  (single unit; origin=shaft; 70 x 90 x 5)", fontsize=11, fontweight="bold")
ax.grid(True, color="0.9"); ax.set_axisbelow(True); ax.tick_params(labelsize=7)
fig.tight_layout()
ppath = os.path.join(DRW, "6_baseplate_v5_top.png")
fig.savefig(ppath, dpi=130); print("WROTE", ppath)
