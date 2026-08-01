"""Base plate v4 - origin = servo OUTPUT SHAFT. Servo long axis = X.
v4 (2026-07-04) for the pin-follower redesign: the slotted-anvil hardware is
gone; each side now takes one printed HOUSING (part_housing.py) bolted with
4x M3 from below. v4.1 (same day, user Fusion review): bigger cam (base R16
clears the horn, crest R27.2) pushes everything outboard - walls +-53.2,
hose holes Y +-46.6, plate Y 112 -> 130; hose holes get a top-edge funnel
(the plate hole is now the hose's ONLY guide below the pinch, ~8 mm under it,
so the lead-in matters). Servo cutout/tabs unchanged. STEP + top-view PNG."""
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

# --- housings on Y (part_housing.py; same part both sides, B rotated 180) ---
HSG_SCREW_D  = 3.4      # M3 clearance; self-tap into d2.8 pilots above
HSG_SCREWS   = [(14, 31.0), (-14, 31.0), (14, 56.2), (-14, 56.2)]
TUBE_Y       = 46.6
TUBE_HOLE_D  = 15.0     # tube OD 12.7 drop-through (barbs connect below plate)
# --- plate ---
PL_X, PL_Y, PL_TH = 70.0, 130.0, 5.0   # X = servo length dir, Y = housing dir

# ---------- STEP ----------
plate = cq.Workplane("XY").box(PL_X, PL_Y, PL_TH).translate((0,0,PL_TH/2))
cut = cq.Workplane("XY").box(BODY_X, BODY_Y, PL_TH+4).translate((BODY_CX,0,PL_TH/2))
plate = plate.cut(cut)
tabs = [(TAB_R_X, TAB_DY),(TAB_R_X,-TAB_DY),(TAB_L_X,TAB_DY),(TAB_L_X,-TAB_DY)]
plate = plate.faces(">Z").workplane(centerOption="CenterOfBoundBox").pushPoints(tabs).hole(TAB_SCREW_D)
hsg = [(sx, sgn*sy) for (sx, sy) in HSG_SCREWS for sgn in (+1,-1)]
plate = plate.faces(">Z").workplane(centerOption="CenterOfBoundBox").pushPoints(hsg).hole(HSG_SCREW_D)
plate = (plate.faces(">Z").workplane(centerOption="CenterOfBoundBox")
         .pushPoints([(0, TUBE_Y),(0,-TUBE_Y)]).hole(TUBE_HOLE_D))
for sgn in (+1, -1):   # top-edge lead-in funnel on each hose hole
    fun = (cq.Workplane("XY", origin=(0, sgn*TUBE_Y, PL_TH))
           .circle(TUBE_HOLE_D/2 + 1.5).workplane(offset=-1.5).circle(TUBE_HOLE_D/2)
           .loft(combine=True))
    plate = plate.cut(fun)
spath = os.path.join(OUT,"3_base_plate_v4.step")
cq.exporters.export(plate, spath)
bb = plate.val().BoundingBox()
print("WROTE", spath, "bbox", round(bb.xlen,1), round(bb.ylen,1), round(bb.zlen,1))

# ---------- top-view diagram ----------
fig,ax=plt.subplots(figsize=(8.5,11))
ax.add_patch(Rectangle((-PL_X/2,-PL_Y/2),PL_X,PL_Y,fc="#f2efe6",ec="black",lw=1.8))
# servo body + cutout
ax.add_patch(Rectangle((BODY_CX-BODY_X/2,-BODY_Y/2),BODY_X,BODY_Y,fc="#f4b7b0",ec="#b03a2e",lw=1.4,alpha=.8))
ax.text(BODY_CX,0,"servo body\n(hangs below)",ha="center",va="center",fontsize=8,color="#7b241c")
for x in (TAB_R_X,TAB_L_X):
    for y in (TAB_DY,-TAB_DY):
        ax.add_patch(Circle((x,y),TAB_SCREW_D/2,fc="white",ec="black",lw=1.1))
ax.plot(0,0,marker="+",color="#1f6feb",ms=16,mew=2,zorder=6)
ax.add_patch(Circle((0,0),27.2,fill=False,ec="#1f6feb",ls=(0,(5,4)),lw=1.1))  # crest sweep
ax.text(19,-21,"crest sweep\nR27.2",fontsize=7,color="#1f6feb")
# housing footprints (dashed) + their holes
for sgn in (+1,-1):
    ax.add_patch(Rectangle((-17.3, sgn*28 if sgn>0 else sgn*59.2),34.6,31.2,
                           fill=False,ec="0.35",lw=1.2,ls=(0,(4,3))))
    ax.plot([-17.3,17.3],[sgn*53.2]*2,color="#8a4b16",lw=1.6)
    for (sx,sy) in HSG_SCREWS:
        ax.add_patch(Circle((sx,sgn*sy),HSG_SCREW_D/2,fc="white",ec="black",lw=1.1,zorder=3))
    ax.add_patch(Circle((0,sgn*TUBE_Y),TUBE_HOLE_D/2,fc="white",ec="#8a4b16",lw=1.4,zorder=2))
# dims / labels
ax.annotate("",(0,2),(0,TUBE_Y-1),arrowprops=dict(arrowstyle="<->",color="#c0392b",lw=1.2))
ax.text(1.4,24,"hose Y=46.6",color="#c0392b",fontsize=8,va="center",rotation=90)
ax.annotate("",(0,0),(TAB_R_X,0),arrowprops=dict(arrowstyle="<->",color="#117a3d",lw=1.1))
ax.text(TAB_R_X/2,-2.6,"19.05",color="#117a3d",fontsize=8,ha="center")
ax.annotate("",(0,7),(TAB_L_X,7),arrowprops=dict(arrowstyle="<->",color="#117a3d",lw=1.1))
ax.text(TAB_L_X/2,7.6,"30.45",color="#117a3d",fontsize=8,ha="center")
ax.annotate("housing screws d3.4\n(+-14, +-31 / +-56.2)\nM3 self-tap from below",(14,31),(24,36),
            color="black",fontsize=7.5,arrowprops=dict(arrowstyle="->",color="0.4"))
ax.annotate("backstop wall face\nY=53.2 (printed-in)",(15,53.2),(22,61),
            color="#8a4b16",fontsize=7.5,arrowprops=dict(arrowstyle="->",color="#8a4b16"))
ax.annotate("d15 hose hole\n(1.5 top funnel;\nonly guide below pinch)",(TUBE_HOLE_D/2,-TUBE_Y),(20,-TUBE_Y-10),
            color="#8a4b16",fontsize=7.5,arrowprops=dict(arrowstyle="->",color="#8a4b16"))
ax.text(0,67,"HOUSING A footprint (dashed; wall outboard)",ha="center",fontsize=8)
ax.text(0,-69,"HOUSING B (same part, rotated 180)",ha="center",fontsize=8)
ax.set_aspect("equal");ax.set_xlim(-44,44);ax.set_ylim(-75,75)
ax.set_title("BASE PLATE v4.1 - TOP  (origin=shaft; pin housings on Y; 70 x 130 x 5)",fontsize=11,fontweight="bold")
ax.grid(True,color="0.9");ax.set_axisbelow(True);ax.tick_params(labelsize=7)
fig.tight_layout()
ppath=os.path.join(DRW,"6_baseplate_v4_top.png")
fig.savefig(ppath,dpi=130);print("WROTE",ppath)
