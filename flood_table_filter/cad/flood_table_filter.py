"""Flood-table drain-corner filter: a slotted "dam" that walls off the drain
corner of the flood table (70 mm perimeter walls, 3.5 mm thick; drain hole
Ø26.35 mm tucked 16.5 mm off each inner wall). The dam is siliconed to the floor
and BOLTED to the two walls, so the only path to the drain is THROUGH the coarse
vertical slots.

MOUNTING (v2, per the table photos):
  Each end of the dam carries an over-the-wall CLAMP that hooks over the 3.5 mm
  lip: an inner leg on the inside, a bridge across the top, and an outer skirt
  down the outside. An M3 screw runs horizontally from OUTSIDE, through the skirt
  and a drilled Ø3.4 hole in the wall, into a CAPTIVE M3 NUT trapped in the inner
  leg -> pinches the wall and holds the part flat while the floor silicone cures
  (and permanently after). All tightening is done from outside the table.

Sized COARSE (~2 mm) on purpose: the reservoir pump is a small VIVOSUN 400GPH
submersible that only needs string/chunk protection; slime and silt pass through.
Big area + coarse slots + in-place brushability beat blinding.

CORNER FRAME (this is what gets exported, Z up):
  - drain corner at origin (0,0,0); floor at Z=0, walls up to Z=WALL_H.
  - Wall A: inner face at Y=0, body Y in [-WALL_T, 0], reservoir interior Y>0.
  - Wall B: inner face at X=0, body X in [-WALL_T, 0], reservoir interior X>0.
  - dam spans from P1=(LEG,0) on wall A to P2=(0,LEG) on wall B.
  - +n_out = (1,1)/sqrt2 points into the reservoir (dirty side); the small
    triangular pocket (with the drain hole) is on the corner side.

Regenerate (this machine: WDAC blocks VTK DLLs, py3.13 has no ocp wheel -> pin 3.12,
cadquery 2.4.0, numpy<2; the in-file shim stubs VTK so only OCP is used):
  uv run --no-project --python 3.12 --with "cadquery==2.4.0" --with "numpy==1.26.4" \
      python flood_table_filter/cad/flood_table_filter.py
"""
import os, math, sys, types, importlib.abc, importlib.machinery

# CadQuery hard-imports VTK at load, but this build/STEP export path only uses
# OCP. This machine's VTK native DLLs are blocked by Application Control policy,
# so we satisfy `import vtkmodules.*` with harmless stubs (never actually called).
class _VtkStub(types.ModuleType):
    def __getattr__(self, name):
        return type(name, (), {})


class _VtkFinder(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    def find_spec(self, fullname, path, target=None):
        if fullname == "vtkmodules" or fullname.startswith("vtkmodules."):
            return importlib.machinery.ModuleSpec(fullname, self)
        return None

    def create_module(self, spec):
        return _VtkStub(spec.name)

    def exec_module(self, module):
        pass


sys.meta_path.insert(0, _VtkFinder())

import cadquery as cq

OUT = r"D:\Claude\Projects\Grow Home\flood_table_filter\step"
os.makedirs(OUT, exist_ok=True)

# ---------------- table (measured) ----------------
WALL_H     = 70.0      # perimeter wall height
WALL_T     = 3.5       # perimeter wall thickness (the clamp hooks over this)
DRAIN_DIA  = 26.35     # drain hole diameter
DRAIN_OFF  = 16.5      # drain hole centre off each inner wall

# ---------------- dam face ----------------
LEG        = 100.0     # how far the dam sits off the corner along each wall
PANEL_T    = 4.0       # dam face thickness
BOW        = 30.0      # face bulge into reservoir (0 = flat plate); adds area + arch stiffness

SLOT_W     = 2.0       # slot width  -> coarse, passes slime, stops strings/chunks
OPEN_FRAC  = 0.35      # target open-area fraction of the face -> sets slot pitch
BOT_RAIL   = 4.0       # solid rail at floor (seals to floor, rigidity)
TOP_RAIL   = 6.0       # solid rail at top (rigidity)
END_BORDER = 12.0      # solid border at each wall end (clamp joint)

# ---------------- silicone flanges ----------------
FLANGE_LEN = 30.0      # inner side-wall silicone tab length along the wall
FLANGE_TH  = 5.0       # side / floor flange thickness
OVERLAP    = PANEL_T   # how far flanges overlap the panel so booleans fuse
FLOOR_W    = 15.0      # floor silicone lip width (into reservoir)

# ---------------- over-the-wall M3 clamp (one per wall end) ----------------
CLAMP_W      = 18.0    # clamp width along the wall
SKIRT_T      = 5.0     # outer skirt thickness (down the outside of the wall)
SKIRT_DROP   = 35.0    # how far the skirt hangs below the wall top
BRIDGE_TH    = 5.0     # top bridge thickness (over the wall top)
INNER_LEG_T  = 9.0     # inner-leg thickness into reservoir (holds the captive nut)
SCREW_Z      = 48.0    # height of the horizontal screw axis
M3_CLEAR     = 3.5     # screw clearance-hole diameter
M3_NUT_AF    = 5.7     # M3 hex-nut across-flats (5.5 + fit clearance)
M3_NUT_TH    = 2.8     # nut-trap depth

BED_MAX      = 256.0   # printer bed limit (mm)

# ---------------- derived ----------------
S      = 1.0 / math.sqrt(2.0)
P1     = (LEG, 0.0)
P2     = (0.0, LEG)
MID    = (LEG / 2.0, LEG / 2.0)
DVEC   = (-S, S)                 # unit P1 -> P2 (along the dam)
NOUT   = (S, S)                  # unit into reservoir (dirty side)
DIAG   = LEG * math.sqrt(2.0)
PITCH  = SLOT_W / OPEN_FRAC
HEX_D  = M3_NUT_AF / math.cos(math.radians(30))   # nut circumscribed dia

# curved-face geometry (arc through P1, P2 bulging +NOUT by sagitta BOW)
CURVED = BOW > 1e-6
if CURVED:
    _c  = DIAG / 2.0                              # half chord
    R   = (_c * _c + BOW * BOW) / (2.0 * BOW)     # arc radius
    CEN = (MID[0] - (R - BOW) * NOUT[0], MID[1] - (R - BOW) * NOUT[1])
    U1  = ((P1[0] - CEN[0]) / R, (P1[1] - CEN[1]) / R)   # unit CEN->P1
    U2  = ((P2[0] - CEN[0]) / R, (P2[1] - CEN[1]) / R)   # unit CEN->P2
    UM  = NOUT                                            # unit CEN->arc mid
    TH1 = math.atan2(U1[1], U1[0])
    TH2 = math.atan2(U2[1], U2[0])
    DTH = math.atan2(math.sin(TH2 - TH1), math.cos(TH2 - TH1))  # signed, short way
    ARC_LEN = abs(DTH) * R


def oriented_box(l, w, h, angle_deg, center):
    """Box (l along local X, w along Y, h along Z), rotated about Z, centred."""
    return (cq.Workplane("XY").box(l, w, h)
            .rotate((0, 0, 0), (0, 0, 1), angle_deg)
            .translate(center))


def axbox(cx, cy, cz, lx, ly, lz):
    """Axis-aligned box centred at (cx,cy,cz)."""
    return cq.Workplane("XY").box(lx, ly, lz).translate((cx, cy, cz))


def slot_centers(length):
    """distances along the face (from one end) for evenly spaced slot centres."""
    usable = length - 2 * END_BORDER
    n = int(usable // PITCH)
    if n < 1:
        return []
    span = (n - 1) * PITCH
    u0 = (length - span) / 2.0
    return [u0 + k * PITCH for k in range(n)]


def arc_ribbon(r_in, r_out, height):
    """Curved wall between radii r_in..r_out from CEN, spanning the P1->P2 arc,
    extruded from Z=0 up by `height`."""
    def pt(r, u):
        return (CEN[0] + r * u[0], CEN[1] + r * u[1])
    return (cq.Workplane("XY")
            .moveTo(*pt(r_out, U1))
            .threePointArc(pt(r_out, UM), pt(r_out, U2))
            .lineTo(*pt(r_in, U2))
            .threePointArc(pt(r_in, UM), pt(r_in, U1))
            .close().extrude(height))


slot_h = WALL_H - TOP_RAIL - BOT_RAIL
slot_zc = BOT_RAIL + slot_h / 2.0

# ---------------- dam face panel + vertical slots ----------------
if CURVED:
    face_len = ARC_LEN
    panel = arc_ribbon(R - PANEL_T / 2.0, R + PANEL_T / 2.0, WALL_H)
    us = slot_centers(ARC_LEN)
    cutters = None
    for s in us:                                  # s = arc length from the P1 end
        phi = TH1 + (s / ARC_LEN) * DTH           # angle about CEN
        cx = CEN[0] + R * math.cos(phi)
        cy = CEN[1] + R * math.sin(phi)
        box = oriented_box(PANEL_T + 4.0, SLOT_W, slot_h,
                           math.degrees(phi), (cx, cy, slot_zc))  # length along radius
        cutters = box if cutters is None else cutters.union(box)
    if cutters is not None:
        panel = panel.cut(cutters)
else:
    face_len = DIAG
    panel = oriented_box(DIAG, PANEL_T, WALL_H, 135.0, (MID[0], MID[1], WALL_H / 2.0))
    us = slot_centers(DIAG)
    cutters = None
    for u in us:
        cx = P1[0] + u * DVEC[0]
        cy = P1[1] + u * DVEC[1]
        box = oriented_box(SLOT_W, PANEL_T + 4.0, slot_h, 135.0, (cx, cy, slot_zc))
        cutters = box if cutters is None else cutters.union(box)
    if cutters is not None:
        panel = panel.cut(cutters)

part = panel

# ---------------- inner side silicone flanges (bond to inside of each wall) ----
flangeA = oriented_box(FLANGE_LEN, FLANGE_TH, WALL_H, 0.0,
                       (LEG - OVERLAP + FLANGE_LEN / 2.0, FLANGE_TH / 2.0, WALL_H / 2.0))
flangeB = oriented_box(FLANGE_LEN, FLANGE_TH, WALL_H, 90.0,
                       (FLANGE_TH / 2.0, LEG - OVERLAP + FLANGE_LEN / 2.0, WALL_H / 2.0))
part = part.union(flangeA).union(flangeB)

# ---------------- floor silicone lip (along the dam, dirty side) ----------------
if CURVED:
    r0 = R + PANEL_T / 2.0 - 1.0
    floor_lip = arc_ribbon(r0, r0 + FLOOR_W, FLANGE_TH)
else:
    foff = PANEL_T / 2.0 + FLOOR_W / 2.0 - 1.0
    floor_lip = oriented_box(DIAG, FLOOR_W, FLANGE_TH, 135.0,
                             (MID[0] + foff * NOUT[0], MID[1] + foff * NOUT[1], FLANGE_TH / 2.0))
part = part.union(floor_lip)


# ---------------- over-the-wall M3 clamp bracket ----------------
# Depth axis = perpendicular to the wall (into reservoir = positive).
D_INNER = INNER_LEG_T / 2.0                       # inner-leg centre
D_SKIRT = -(WALL_T + SKIRT_T / 2.0)               # skirt centre (outside wall)
D_BRIDGE_C = (INNER_LEG_T - (WALL_T + SKIRT_T)) / 2.0
D_BRIDGE_L = INNER_LEG_T + WALL_T + SKIRT_T


def build_clamp(wall):
    """Clamp hooking over `wall` ("A": along X at y~0; "B": along Y at x~0),
    centred where the dam meets that wall. Returns a fused solid with the M3
    clearance hole and captive-nut trap already cut."""
    along_c = LEG                                 # centre along the wall

    def place(along, depth, z, la, ld, lz):
        # map (along-wall, depth-into-reservoir, z) -> world box
        if wall == "A":
            return axbox(along, depth, z, la, ld, lz)
        return axbox(depth, along, z, ld, la, lz)

    inner  = place(along_c, D_INNER,   WALL_H / 2.0,
                   CLAMP_W, INNER_LEG_T, WALL_H)
    skirt  = place(along_c, D_SKIRT,   WALL_H - SKIRT_DROP / 2.0,
                   CLAMP_W, SKIRT_T, SKIRT_DROP)
    bridge = place(along_c, D_BRIDGE_C, WALL_H + BRIDGE_TH / 2.0,
                   CLAMP_W, D_BRIDGE_L, BRIDGE_TH)
    clamp = inner.union(skirt).union(bridge)

    # horizontal M3 clearance hole through skirt + wall-gap + inner leg
    y0, y1 = D_SKIRT - SKIRT_T, INNER_LEG_T + 1.0
    if wall == "A":
        base, dirv = cq.Vector(along_c, y0, SCREW_Z), cq.Vector(0, 1, 0)
    else:
        base, dirv = cq.Vector(y0, along_c, SCREW_Z), cq.Vector(1, 0, 0)
    bore = cq.Workplane().add(cq.Solid.makeCylinder(M3_CLEAR / 2.0, y1 - y0, base, dirv))
    clamp = clamp.cut(bore)

    # captive hex-nut trap in the inner leg, opening toward the wall (depth=0)
    nut = (cq.Workplane("XY").polygon(6, HEX_D).extrude(M3_NUT_TH)
           .rotate((0, 0, 0), (1, 0, 0), -90))     # +Z extrusion -> +Y (depth) axis
    if wall == "A":
        nut = nut.translate((along_c, 0.0, SCREW_Z))
    else:
        nut = nut.rotate((0, 0, 0), (0, 0, 1), 90).translate((0.0, along_c, SCREW_Z))
    clamp = clamp.cut(nut)
    return clamp


part = part.union(build_clamp("A")).union(build_clamp("B"))


# ---------------- export ----------------
def export(solid, name):
    path = os.path.join(OUT, name)
    cq.exporters.export(solid, path)
    bb = solid.val().BoundingBox()
    print("WROTE", path, "| bbox X/Y/Z:",
          round(bb.xlen, 1), round(bb.ylen, 1), round(bb.zlen, 1))


face_area = face_len * slot_h
open_area = len(us) * SLOT_W * slot_h
drain_area = math.pi * (DRAIN_DIA / 2.0) ** 2
print(f"{'curved' if CURVED else 'flat'} face {face_len:.0f} x {WALL_H:.0f} mm "
      f"(chord {DIAG:.0f}, bow {BOW:.0f}) | {len(us)} slots @ {SLOT_W} mm, pitch {PITCH:.2f} mm")
print(f"open area ~{open_area:.0f} mm^2 ({open_area/face_area*100:.0f}% of face) "
      f"= {open_area/drain_area:.1f}x the {DRAIN_DIA:.0f} mm drain bore")
if DIAG > BED_MAX:
    print(f"WARNING: {DIAG:.0f} mm diagonal exceeds {BED_MAX:.0f} mm bed")

export(part, "1_corner_dam_filter.step")

# quick preview (SVG uses OCP, not the blocked VTK) — isometric-ish look
cq.exporters.export(
    part, os.path.join(OUT, "1_corner_dam_filter.svg"),
    opt={"projectionDir": (0.6, -0.7, 0.5), "showAxes": False,
         "strokeWidth": 0.4, "width": 900, "height": 700})
print("WROTE preview SVG")
