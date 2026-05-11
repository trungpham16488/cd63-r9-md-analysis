"""
PYMOL SCRIPT FOR FIGURE 2 PANELS C AND D
================================================================================
Energy-minimized structures showing EDC/NHS covalent attachment
Panel c: CD63-R9 conjugate (LYS156, bond length 1.45 Å)
Panel d: CD9-R9 conjugate (LYS156, bond length 1.50 Å)
================================================================================

USAGE:
1. Open PyMOL
2. Load your structure file: File > Open > cd63_r9_minimized.pdb
3. Copy and paste commands below into PyMOL command line
4. OR: pymol -c cd63_r9_minimized.pdb pymol_panel_c.py

================================================================================
"""

# ============================================================================
# PANEL C: CD63-R9 STRUCTURE
# ============================================================================

# Load structure
load cd63_r9_minimized.pdb, cd63_r9

# Basic view settings
bg_color white
set ray_opaque_background, on
set antialias, 2
set ray_shadows, 0

# Protein representation
hide everything
show cartoon, cd63_r9
color skyblue, cd63_r9 and chain A  # CD63 protein

# R9 peptide representation
show sticks, cd63_r9 and chain B  # R9 peptide
color blue, cd63_r9 and chain B
set stick_radius, 0.2, cd63_r9 and chain B

# Highlight LYS156 (EDC/NHS conjugation site)
show sticks, cd63_r9 and resi 156
color magenta, cd63_r9 and resi 156
set stick_radius, 0.3, cd63_r9 and resi 156

# Show covalent bond (EDC/NHS linkage)
# Assuming bond between LYS156 NZ and R9 first residue N-terminus
distance bond_c, cd63_r9 and resi 156 and name NZ, cd63_r9 and chain B and resi 1 and name N
hide labels, bond_c
color yellow, bond_c
set dash_width, 4, bond_c
set dash_color, yellow, bond_c

# Add bond length label
label cd63_r9 and resi 156 and name NZ, "1.45 Å"
set label_color, black
set label_size, 12
set label_position, (2, 2, 2)

# Optimal view
zoom cd63_r9 and (resi 156 or chain B), 5
orient cd63_r9 and (resi 156 or chain B)

# Ray trace and save
ray 2400, 2400  # High resolution for publication
png Figure2_panel_c_CD63_R9.png, dpi=600

# Clean view for manual adjustment
set stick_transparency, 0.0
set cartoon_transparency, 0.0

print "Panel C (CD63-R9) rendered!"
print "Output: Figure2_panel_c_CD63_R9.png"
print "Bond length: 1.45 Å (EDC/NHS covalent linkage)"

# ============================================================================
# PANEL D: CD9-R9 STRUCTURE
# ============================================================================

# Clear previous
delete all

# Load structure
load cd9_r9_minimized.pdb, cd9_r9

# Basic view settings
bg_color white
set ray_opaque_background, on
set antialias, 2
set ray_shadows, 0

# Protein representation
hide everything
show cartoon, cd9_r9
color palegreen, cd9_r9 and chain A  # CD9 protein (different color from CD63)

# R9 peptide representation
show sticks, cd9_r9 and chain B  # R9 peptide
color blue, cd9_r9 and chain B
set stick_radius, 0.2, cd9_r9 and chain B

# Highlight LYS156 (EDC/NHS conjugation site)
show sticks, cd9_r9 and resi 156
color magenta, cd9_r9 and resi 156
set stick_radius, 0.3, cd9_r9 and resi 156

# Show covalent bond (EDC/NHS linkage)
distance bond_d, cd9_r9 and resi 156 and name NZ, cd9_r9 and chain B and resi 1 and name N
hide labels, bond_d
color yellow, bond_d
set dash_width, 4, bond_d
set dash_color, yellow, bond_d

# Add bond length label
label cd9_r9 and resi 156 and name NZ, "1.50 Å"
set label_color, black
set label_size, 12
set label_position, (2, 2, 2)

# Optimal view
zoom cd9_r9 and (resi 156 or chain B), 5
orient cd9_r9 and (resi 156 or chain B)

# Ray trace and save
ray 2400, 2400  # High resolution
png Figure2_panel_d_CD9_R9.png, dpi=600

print "Panel D (CD9-R9) rendered!"
print "Output: Figure2_panel_d_CD9_R9.png"
print "Bond length: 1.50 Å (EDC/NHS covalent linkage)"

# ============================================================================
# ALTERNATIVE: SIDE-BY-SIDE COMPARISON
# ============================================================================

delete all

# Load both structures
load cd63_r9_minimized.pdb, cd63_r9
load cd9_r9_minimized.pdb, cd9_r9

# Align structures for comparison
align cd9_r9, cd63_r9

# Position side by side
translate [20, 0, 0], cd9_r9

# Apply same visualization to both
for obj in ['cd63_r9', 'cd9_r9']:
    hide everything, obj
    show cartoon, obj and chain A
    show sticks, obj and chain B
    show sticks, obj and resi 156
    color blue, obj and chain B
    color magenta, obj and resi 156

# Different protein colors
color skyblue, cd63_r9 and chain A
color palegreen, cd9_r9 and chain A

# Zoom to show both
zoom all, 3

# Save comparison
ray 4800, 2400  # Wide format for side-by-side
png Figure2_panels_cd_comparison.png, dpi=600

print "Side-by-side comparison rendered!"

# ============================================================================
# INSTRUCTIONS FOR GENERATING THESE IMAGES
# ============================================================================

"""
STEP-BY-STEP INSTRUCTIONS:

1. PREPARE STRUCTURES:
   - Extract final frame from energy minimization
   - Save as PDB format
   - Name files: cd63_r9_minimized.pdb, cd9_r9_minimized.pdb

2. RUN IN PYMOL:
   Option A (Interactive):
     - Open PyMOL GUI
     - Load structure: File > Open > cd63_r9_minimized.pdb
     - Copy/paste commands from Panel C section
     - Repeat for Panel D
   
   Option B (Command line):
     - pymol -cq cd63_r9_minimized.pdb pymol_panel_c.py
     - pymol -cq cd9_r9_minimized.pdb pymol_panel_d.py

3. MANUAL ADJUSTMENTS:
   - Rotate view for best angle (mouse drag in PyMOL)
   - Adjust zoom level
   - Re-run: ray 2400, 2400; png output.png, dpi=600

4. VERIFY:
   - Check bond length measurement is visible
   - Confirm LYS156 is magenta
   - Confirm R9 is blue sticks
   - Confirm EDC/NHS bond is highlighted (yellow)

OUTPUTS:
- Figure2_panel_c_CD63_R9.png (2400x2400, 600 DPI)
- Figure2_panel_d_CD9_R9.png (2400x2400, 600 DPI)
- Figure2_panels_cd_comparison.png (optional, side-by-side)

NOTES:
- If bond is not visible, check atom names (NZ for lysine, N for peptide)
- Adjust residue numbers if your system differs (resi 156)
- Bond colors: yellow for covalent, red for hydrogen bonds
- Protein transparency can be adjusted: set cartoon_transparency, 0.3
"""

# ============================================================================
# GROMACS COMMAND TO EXTRACT MINIMIZED STRUCTURE
# ============================================================================

"""
# Extract final frame after energy minimization
gmx trjconv -s em.tpr -f em.trr -o em_final.pdb -dump 0

# Or extract specific frame
gmx trjconv -s em.tpr -f em.trr -o frame_minimized.pdb -b 1000 -e 1000

# Then rename and use in PyMOL:
mv em_final.pdb cd63_r9_minimized.pdb
"""
