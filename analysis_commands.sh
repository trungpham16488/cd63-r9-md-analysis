#!/bin/bash
################################################################################
# GROMACS ANALYSIS COMMANDS
# MD simulation analysis for CD63-R9 vs CD9-R9 comparison
# Nature Communications submission
################################################################################

echo "MD Simulation Analysis Workflow"
echo "================================"

# Set system name
SYSTEM="cd63_r9"  # Change to cd9_r9 for CD9 system
TPR="production_5ns.tpr"
TRJ="cd63_1380to4500ps_clean.xtc"  # Matched trajectory (1.38-4.5 ns)
INDEX="index_r9_v2.ndx"

################################################################################
# 1. BACKBONE RMSD ANALYSIS
################################################################################
echo "1. Calculating backbone RMSD..."

gmx rms -s ${TPR} \
        -f ${TRJ} \
        -n ${INDEX} \
        -o rmsd_backbone_MATCHED.xvg \
        -tu ns << EOF
4
4
EOF

# Group 4 = Backbone (for both fit and RMSD calculation)

################################################################################
# 2. PER-RESIDUE RMSF ANALYSIS
################################################################################
echo "2. Calculating per-residue RMSF..."

gmx rmsf -s ${TPR} \
         -f ${TRJ} \
         -n ${INDEX} \
         -o rmsf_residue_MATCHED.xvg \
         -res << EOF
18
EOF

# Group 18 = Protein_noR9 (protein without R9 peptide)

################################################################################
# 3. R9 PEPTIDE RADIUS OF GYRATION
################################################################################
echo "3. Calculating R9 gyration..."

gmx gyrate -s ${TPR} \
           -f ${TRJ} \
           -n ${INDEX} \
           -o gyrate_r9_MATCHED.xvg << EOF
17
EOF

# Group 17 = R9_peptide

################################################################################
# 4. HYDROGEN BOND ANALYSIS (Protein-R9)
################################################################################
echo "4. Calculating hydrogen bonds..."

gmx hbond -s ${TPR} \
          -f ${TRJ} \
          -n ${INDEX} \
          -num hbond_MATCHED.xvg << EOF
18
17
EOF

# Group 18 = Protein_noR9
# Group 17 = R9_peptide
# Default: distance cutoff 0.35 nm, angle cutoff 30°

################################################################################
# 5. CREATE INDEX GROUPS (if needed)
################################################################################
echo "5. Creating custom index groups..."

# This creates the R9_peptide and Protein_noR9 groups
# Modify residue ranges based on your system

gmx make_ndx -f system.gro -o index_custom.ndx << EOF
!1
name 13 Protein_noR9
r 248-256
name 14 R9_peptide
q
EOF

# Adjust residue numbers based on your system:
# - Protein_noR9: protein residues (e.g., 1-247)
# - R9_peptide: R9 residues (e.g., 248-256)

################################################################################
# NOTES
################################################################################

# Simulation parameters:
# - Equilibration: 1.38 ns (NVT + NPT)
# - Production: 3.12 ns (1.38-4.5 ns)
# - Temperature: 300 K
# - Pressure: 1 bar
# - Force field: CHARMM36m
# - Water: TIP3P
# - Salt: 0.15 M NaCl

# Output files:
# - rmsd_backbone_MATCHED.xvg: Backbone RMSD vs time
# - rmsf_residue_MATCHED.xvg: Per-residue RMSF
# - gyrate_r9_MATCHED.xvg: R9 radius of gyration vs time
# - hbond_MATCHED.xvg: Number of H-bonds vs time

################################################################################
