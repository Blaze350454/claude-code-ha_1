"""
Fan Diffuser Bottom — Asymmetric Flared Outlet with Deflector Cones

For Noctua NF-F12 iPPC 3000 PWM on grow tent humidifier reservoir.
Generates a STEP file importable into Fusion 360.

Layout (looking down at reservoir from above):
  [OUTLET]  <<<  [FOGGER]  <<<  [FAN/DIFFUSER]
  Left end       Center         Right end
  (+X)                          (origin)

Airflow: fan blows straight down -> hits two stacked inverted cones ->
air is deflected outward -> solid baffles on +/-X sides block outlet/wall
directions -> air exits only through +/-Y gaps (the two long sides of
the reservoir), sweeping across the water surface.
"""

import cadquery as cq
import os

# ============================================================
# PARAMETERS — edit these to adjust the design
# ============================================================

# Fan opening
TOP_ID = 124.0          # mm — inner diameter at top (fan mount opening)

# Flared bottom
BOTTOM_ID = 176.0       # mm — inner diameter at bottom (flared exit)
OFFSET_X = 25.0         # mm — bottom center offset toward outlet (+X)

# Dimensions
CONE_HEIGHT = 45.0      # mm — diffuser depth below flange
WALL = 3.0              # mm — wall thickness (PETG)

# Mounting flange (sits against underside of lid)
FLANGE_EXTRA = 15.0     # mm — flange extends beyond cone outer wall
FLANGE_THICK = 4.0      # mm — flange thickness

# Noctua NF-F12 mounting holes (standard 120mm fan pattern)
MOUNT_SPACING = 105.0   # mm — hole-to-hole on each axis
MOUNT_HOLE_DIA = 4.5    # mm — for M4 screws (4.0mm + clearance)

# Deflector cones (inverted — peak up, base down)
DEF1_PEAK_Z = -8.0      # mm — Z of upper cone peak (below lid plane)
DEF1_HEIGHT = 15.0       # mm — cone height
DEF1_BASE_R = 42.0       # mm — base radius of upper deflector
PEAK_R = 1.0             # mm — small radius at peak (approximates point)

DEF2_PEAK_Z = -26.0      # mm — Z of lower cone peak
DEF2_HEIGHT = 15.0        # mm — cone height
DEF2_BASE_R = 55.0        # mm — base radius (larger, catches spillover)

# ============================================================
# DERIVED VALUES
# ============================================================

top_ir = TOP_ID / 2             # 62.0 mm
top_or = top_ir + WALL          # 65.0 mm
bottom_ir = BOTTOM_ID / 2      # 88.0 mm
bottom_or = bottom_ir + WALL   # 91.0 mm
flange_or = top_or + FLANGE_EXTRA  # 80.0 mm
mh = MOUNT_SPACING / 2         # 52.5 mm from center

# ============================================================
# BUILD THE DIFFUSER SHELL
# ============================================================

print("Building diffuser shell...")

# Outer loft (solid)
outer_loft = (
    cq.Workplane("XY")
    .circle(top_or)
    .workplane(offset=-CONE_HEIGHT)
    .center(OFFSET_X, 0)
    .circle(bottom_or)
    .loft()
)

# Inner loft (to hollow out)
inner_loft = (
    cq.Workplane("XY")
    .circle(top_ir)
    .workplane(offset=-CONE_HEIGHT)
    .center(OFFSET_X, 0)
    .circle(bottom_ir)
    .loft()
)

# Hollow shell
shell = outer_loft.cut(inner_loft)

# Mounting flange at top (ring, extends upward)
flange = (
    cq.Workplane("XY")
    .circle(flange_or)
    .circle(top_ir)
    .extrude(FLANGE_THICK)
)

# Drill mounting holes
hole_positions = [(mh, mh), (mh, -mh), (-mh, mh), (-mh, -mh)]
flange = (
    flange.faces(">Z").workplane()
    .pushPoints(hole_positions)
    .hole(MOUNT_HOLE_DIA, FLANGE_THICK)
)

result = flange.union(shell)

# ============================================================
# DEFLECTOR CONES (inverted — peak up, base down)
# ============================================================

print("Building deflector cones...")

# Upper deflector
def1 = (
    cq.Workplane("XY")
    .workplane(offset=DEF1_PEAK_Z)
    .circle(PEAK_R)
    .workplane(offset=-DEF1_HEIGHT)
    .circle(DEF1_BASE_R)
    .loft()
)

# Lower deflector (larger to catch air that slips past the first)
def2 = (
    cq.Workplane("XY")
    .workplane(offset=DEF2_PEAK_Z)
    .circle(PEAK_R)
    .workplane(offset=-DEF2_HEIGHT)
    .circle(DEF2_BASE_R)
    .loft()
)

result = result.union(def1).union(def2)

# ============================================================
# X-DIRECTION BAFFLES (solid fills on +/-X sides)
#
# These block air from exiting toward the outlet (+X) or the
# near reservoir wall (-X). Air can only exit through the
# +/-Y gaps (the two long sides of the reservoir).
#
# Method: create oversized boxes for each half, intersect with
# the diffuser interior volume, then cut out the cone shapes.
# ============================================================

print("Building baffles...")

# Z range for baffles: from upper cone peak to diffuser bottom
baf_z_top = DEF1_PEAK_Z          # -8
baf_z_bot = -CONE_HEIGHT         # -45
baf_h = abs(baf_z_top - baf_z_bot)  # 37
baf_z_mid = (baf_z_top + baf_z_bot) / 2  # -26.5

# +X fill: oversized box covering the +X half of the interior
px_box = (
    cq.Workplane("XY")
    .box(200, 200, baf_h)
    .translate((100, 0, baf_z_mid))
)
# Trim to diffuser interior
px_fill = px_box.intersect(inner_loft)
# Cut out deflector cones (they're solid — air hits them, not the fill)
px_fill = px_fill.cut(def1).cut(def2)

# -X fill: same for the -X half
nx_box = (
    cq.Workplane("XY")
    .box(200, 200, baf_h)
    .translate((-100, 0, baf_z_mid))
)
nx_fill = nx_box.intersect(inner_loft)
nx_fill = nx_fill.cut(def1).cut(def2)

result = result.union(px_fill).union(nx_fill)

# ============================================================
# EXPORT
# ============================================================

output_dir = os.path.join(os.path.expanduser("~"), "Desktop")
output_path = os.path.join(output_dir, "fan_diffuser_bottom.step")

print("Exporting STEP file...")
cq.exporters.export(result, output_path)

# Print summary
outlet_ext = OFFSET_X + bottom_ir - top_ir
wall_ext = bottom_ir - OFFSET_X - top_ir
side_ext = bottom_ir - top_ir

print(f"\nSTEP exported: {output_path}")
print()
print("=== Diffuser Shell ===")
print(f"  Top opening ID:       {TOP_ID:.0f} mm")
print(f"  Bottom opening ID:    {BOTTOM_ID:.0f} mm (offset {OFFSET_X:.0f} mm toward outlet)")
print(f"  Cone height:          {CONE_HEIGHT:.0f} mm")
print(f"  Wall thickness:       {WALL:.0f} mm")
print(f"  Flange OD:            {flange_or * 2:.0f} mm, thickness {FLANGE_THICK:.0f} mm")
print()
print("=== Flare Beyond Top Edge ===")
print(f"  Outlet side (+X):     {outlet_ext:.0f} mm")
print(f"  Wall side (-X):       {wall_ext:.0f} mm")
print(f"  Lateral (+/-Y):       {side_ext:.0f} mm")
print()
print("=== Deflector Cones ===")
print(f"  Upper: peak Z={DEF1_PEAK_Z:.0f}, base Z={DEF1_PEAK_Z - DEF1_HEIGHT:.0f}, base R={DEF1_BASE_R:.0f} mm")
print(f"  Lower: peak Z={DEF2_PEAK_Z:.0f}, base Z={DEF2_PEAK_Z - DEF2_HEIGHT:.0f}, base R={DEF2_BASE_R:.0f} mm")
print()
print("=== Baffles ===")
print(f"  Solid fills on +/-X sides from Z={baf_z_top:.0f} to Z={baf_z_bot:.0f}")
print(f"  Air exits only through +/-Y gaps (long sides of reservoir)")
print()
print("=== Mounting Holes ===")
print(f"  Pattern: 4x M4 at {MOUNT_SPACING:.0f} mm square spacing")
print(f"  Hole dia: {MOUNT_HOLE_DIA:.1f} mm at +/-{mh:.1f} mm on X and Y")
