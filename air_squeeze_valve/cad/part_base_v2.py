"""Base plate v3 - origin = servo OUTPUT SHAFT. Servo long axis = X.
Shaft offset from servo pic: shaft->right tabs 19.05, ->left tabs 30.45 (49.50 span).
Anvils on Y (perpendicular to long body) at +-19.6 face.
v3 (2026-07-03), reconciled with the outboard-foot anvil v2:
  - anvil screws moved 26.6 -> 37.6 (now under the slotted foot overhang, driver
    access clear; 26.6 sat under the solid anvil body and matched no slot)
  - plate widened Y 80 -> 88 so the foot + screw fit
  - 2x d15 tube pass-through holes at (0, +-19.6): the silicone tube drops
    straight through the pinch line (no room to bend above the plate)
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
SCREW_D   = 3.5

# --- anvils on Y (foot outboard, anvil v2) ---
D_ANVIL   = 19.6
ANVIL_HOLE_Y = 37.6     # fixed base screw under the foot-overhang slot (19.6+18)
TUBE_HOLE_D  = 15.0     # tube OD 12.7 drop-through (barbs connect below plate)
# --- plate ---
PL_X, PL_Y, PL_TH = 70.0, 88.0, 5.0   # X = servo length dir, Y = anvil dir

# ---------- STEP ----------
plate = cq.Workplane("XY").box(PL_X, PL_Y, PL_TH).translate((0,0,PL_TH/2))
cut = cq.Workplane("XY").box(BODY_X, BODY_Y, PL_TH+4).translate((BODY_CX,0,PL_TH/2))
plate = plate.cut(cut)
holes = [(TAB_R_X, TAB_DY),(TAB_R_X,-TAB_DY),(TAB_L_X,TAB_DY),(TAB_L_X,-TAB_DY),  # servo tabs
         (0, ANVIL_HOLE_Y),(0,-ANVIL_HOLE_Y)]                                      # anvil screws
plate = plate.faces(">Z").workplane(centerOption="CenterOfBoundBox").pushPoints(holes).hole(SCREW_D)
plate = (plate.faces(">Z").workplane(centerOption="CenterOfBoundBox")
         .pushPoints([(0, D_ANVIL),(0,-D_ANVIL)]).hole(TUBE_HOLE_D))               # tube drops
spath = os.path.join(OUT,"3_base_plate_v3.step")
cq.exporters.export(plate, spath)
bb = plate.val().BoundingBox()
print("WROTE", spath, "bbox", round(bb.xlen,1), round(bb.ylen,1), round(bb.zlen,1))

# ---------- top-view diagram ----------
# W-crown cam (matches part_cam.py)
R_LOW,R_HOLD,DOC = 7.0,17.0,0.6
R_PEAK = R_HOLD+DOC
V_HALF,RISE,CROWN,RAMP = 5.0,8.0,3.0,50.0
def camr(t,tip):
    d=abs(((t-tip+180)%360)-180)
    if d<=V_HALF: return R_HOLD
    if d<=V_HALF+RISE:
        x=(d-V_HALF)/RISE; return R_HOLD+DOC*0.5*(1-np.cos(np.pi*x))
    if d<=V_HALF+RISE+CROWN: return R_PEAK
    if d<=V_HALF+RISE+CROWN+RAMP:
        x=(d-V_HALF-RISE-CROWN)/RAMP; return R_LOW+(R_PEAK-R_LOW)*0.5*(1+np.cos(np.pi*x))
    return R_LOW
th=np.linspace(0,360,1441)
cx=np.array([camr(t,90)*np.cos(np.radians(t)) for t in th])  # lobe up (+Y) = pinch top
cy=np.array([camr(t,90)*np.sin(np.radians(t)) for t in th])

fig,ax=plt.subplots(figsize=(9,10.4))
ax.add_patch(Rectangle((-PL_X/2,-PL_Y/2),PL_X,PL_Y,fc="#f2efe6",ec="black",lw=1.8))
# servo body + cutout
ax.add_patch(Rectangle((BODY_CX-BODY_X/2,-BODY_Y/2),BODY_X,BODY_Y,fc="#f4b7b0",ec="#b03a2e",lw=1.4,alpha=.8))
ax.text(BODY_CX,0,"servo body\n(hangs below)",ha="center",va="center",fontsize=8,color="#7b241c")
# tabs
for x in (TAB_R_X,TAB_L_X):
    for y in (TAB_DY,-TAB_DY):
        ax.add_patch(Circle((x,y),SCREW_D/2,fc="white",ec="black",lw=1.1))
# shaft + horn
ax.plot(0,0,marker="+",color="#1f6feb",ms=16,mew=2,zorder=6)
ax.add_patch(Circle((0,0),10.5,fill=False,ec="#1f6feb",ls=(0,(5,4)),lw=1.1))  # ~horn dia
# cam (lobe up, pinch top anvil)
ax.fill(cx,cy,color="#9fd0ff",ec="black",lw=1.6,zorder=4,alpha=.9)
# anvils on Y: body at face..face+12, foot overhang OUTBOARD to face+24
for sgn in (+1,-1):
    yf=sgn*D_ANVIL                      # groove face
    body_y0 = yf if sgn>0 else yf-12
    ax.add_patch(Rectangle((-9, body_y0),18,12,fc="#dfe6e9",ec="black",lw=1.5,zorder=2))
    foot_y0 = yf if sgn>0 else yf-24
    ax.add_patch(Rectangle((-9, foot_y0),18,24,fill=False,ec="black",lw=1.0,ls=(0,(4,3)),zorder=1))
    # fixed screw under the slot in the overhang
    ax.add_patch(Circle((0,sgn*ANVIL_HOLE_Y),SCREW_D/2,fc="white",ec="black",lw=1.1,zorder=3))
    # tube drop-through hole in plate, centered on the groove face
    ax.add_patch(Circle((0,yf),TUBE_HOLE_D/2,fc="white",ec="#8a4b16",lw=1.3,zorder=1))
    # groove (tube nest)
    ax.add_patch(Circle((0,yf),6.6,fill=False,ec="#8a4b16",ls=(0,(3,2)),lw=1.0,zorder=3))
# dims / labels
ax.annotate("",(0,0),(0,D_ANVIL),arrowprops=dict(arrowstyle="<->",color="#c0392b",lw=1.2))
ax.text(1.2,D_ANVIL/2,"D=19.6",color="#c0392b",fontsize=9,va="center")
ax.annotate("",(0,0),(TAB_R_X,0),arrowprops=dict(arrowstyle="<->",color="#117a3d",lw=1.1))
ax.text(TAB_R_X/2,-2.4,"19.05",color="#117a3d",fontsize=8,ha="center")
ax.annotate("",(0,7),(TAB_L_X,7),arrowprops=dict(arrowstyle="<->",color="#117a3d",lw=1.1))
ax.text(TAB_L_X/2,7.6,"30.45",color="#117a3d",fontsize=8,ha="center")
ax.annotate("anvil screw Y=37.6\n(under foot slot)",(0,ANVIL_HOLE_Y),(16,ANVIL_HOLE_Y+3),
            color="black",fontsize=7.5,arrowprops=dict(arrowstyle="->",color="0.4"))
ax.annotate("d15 tube hole\n(tube drops through)",(TUBE_HOLE_D/2,-D_ANVIL),(16,-D_ANVIL-9),
            color="#8a4b16",fontsize=7.5,arrowprops=dict(arrowstyle="->",color="#8a4b16"))
ax.text(0,D_ANVIL+27,"ANVIL (groove faces cam; foot+slot outboard)",ha="center",fontsize=8)
ax.text(0,-D_ANVIL-27,"ANVIL #2 (mirror)",ha="center",fontsize=8)
ax.text(34,0,"<- servo long axis (X) ->\ntabs 49.50 apart",ha="center",fontsize=7,color="#7b241c",rotation=90,va="center")
ax.set_aspect("equal");ax.set_xlim(-42,42);ax.set_ylim(-50,50)
ax.set_title("BASE PLATE v3 - TOP  (origin=shaft; anvils on Y, feet outboard; W cam)",fontsize=11,fontweight="bold")
ax.grid(True,color="0.9");ax.set_axisbelow(True);ax.tick_params(labelsize=7)
fig.tight_layout()
ppath=os.path.join(DRW,"6_baseplate_v3_top.png")
fig.savefig(ppath,dpi=130);print("WROTE",ppath)
