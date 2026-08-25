#!/usr/bin/env python3
"""
COMPLETE FIGURE GENERATION FOR Advanced Functional Materials SUBMISSION
================================================================================
Figure 1: Main figure with MD simulation results
- Panel c: CD63-R9 structure (PyMOL - see separate script)
- Panel d: CD9-R9 structure (PyMOL - see separate script)
- Panel e: R9 gyration time series
- Panel f: H-bonds time series
- Panel g: Summary bar chart

Supplementary Figure S1/S2:
- Panel g: RMSD time series
- Panel h: RMSF per-residue plot
================================================================================
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

# Nature Communications specifications
plt.rcParams.update({
    'font.size': 7,
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica'],
    'axes.linewidth': 0.5,
    'lines.linewidth': 1.0,
    'figure.dpi': 600
})

# Colors
COLOR_CD63 = '#0173B2'  # Blue
COLOR_CD9 = '#E69F00'   # Orange

def load_xvg(filename):
    """Load GROMACS .xvg file"""
    data = []
    with open(filename, 'r') as f:
        for line in f:
            if not line.startswith(('@', '#')):
                try:
                    data.append([float(x) for x in line.split()])
                except:
                    continue
    return np.array(data)

def running_average(data, window=50):
    """Calculate running average"""
    return pd.Series(data).rolling(window=window, center=True).mean()

print("="*80)
print("GENERATING ALL FIGURES FOR NATURE COMMUNICATIONS")
print("="*80)
print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# ============================================================================
# LOAD DATA
# ============================================================================
print("Loading data...")

# CD63-R9 data
cd63_rmsd = load_xvg('/home/trungpd89/md_simulations/cd63_r9/rmsd_cd63_backbone_MATCHED.xvg')
cd63_rmsf = load_xvg('/home/trungpd89/md_simulations/cd63_r9/rmsf_cd63_residue_MATCHED.xvg')
cd63_gyr = load_xvg('/home/trungpd89/md_simulations/cd63_r9/gyrate_r9_only_cd63_MATCHED.xvg')
cd63_hb = load_xvg('/home/trungpd89/md_simulations/cd63_r9/hbond_cd63_MATCHED.xvg')

# CD9-R9 data
cd9_rmsd = load_xvg('/home/trungpd89/md_simulations/cd9_r9/rmsd_cd9_backbone_FULL.xvg')
cd9_rmsf = load_xvg('/home/trungpd89/md_simulations/cd9_r9/rmsf_cd9_residue_FULL.xvg')
cd9_gyr = load_xvg('/home/trungpd89/md_simulations/cd9_r9/gyrate_r9_only_cd9_FULL.xvg')
cd9_hb = load_xvg('/home/trungpd89/md_simulations/cd9_r9/hbond_cd9_FULL.xvg')

print("✓ Data loaded\n")

# Calculate statistics
stats = {
    'CD63_RMSD_mean': cd63_rmsd[:, 1].mean(),
    'CD63_RMSD_std': cd63_rmsd[:, 1].std(),
    'CD9_RMSD_mean': cd9_rmsd[:, 1].mean(),
    'CD9_RMSD_std': cd9_rmsd[:, 1].std(),
    'CD63_RMSF_mean': cd63_rmsf[:, 1].mean(),
    'CD63_RMSF_std': cd63_rmsf[:, 1].std(),
    'CD9_RMSF_mean': cd9_rmsf[:, 1].mean(),
    'CD9_RMSF_std': cd9_rmsf[:, 1].std(),
    'CD63_Gyr_mean': cd63_gyr[:, 1].mean(),
    'CD63_Gyr_std': cd63_gyr[:, 1].std(),
    'CD9_Gyr_mean': cd9_gyr[:, 1].mean(),
    'CD9_Gyr_std': cd9_gyr[:, 1].std(),
    'CD63_Hbond_mean': cd63_hb[:, 1].mean(),
    'CD63_Hbond_std': cd63_hb[:, 1].std(),
    'CD9_Hbond_mean': cd9_hb[:, 1].mean(),
    'CD9_Hbond_std': cd9_hb[:, 1].std(),
}

# Running averages
cd63_gyr_avg = running_average(cd63_gyr[:, 1], window=50)
cd9_gyr_avg = running_average(cd9_gyr[:, 1], window=50)
cd63_hb_avg = running_average(cd63_hb[:, 1], window=50)
cd9_hb_avg = running_average(cd9_hb[:, 1], window=50)

# ============================================================================
# FIGURE 2: MAIN FIGURE (panels e, f, g)
# Panels c, d are PyMOL structures - see separate script
# ============================================================================
print("Creating Figure 2 (panels e, f, g)...")

fig = plt.figure(figsize=(183/25.4, 80/25.4))

# Panel e: R9 Gyration
ax1 = plt.subplot(1, 3, 1)
ax1.plot(cd63_gyr[:, 0]/1000, cd63_gyr_avg, color=COLOR_CD63, linewidth=1.5, 
         label=f'CD63–R9\n({stats["CD63_Gyr_mean"]:.2f} ± {stats["CD63_Gyr_std"]:.2f} nm)', 
         alpha=1.0, zorder=3)
ax1.plot(cd9_gyr[:, 0]/1000, cd9_gyr_avg, color=COLOR_CD9, linewidth=1.5, 
         label=f'CD9–R9\n({stats["CD9_Gyr_mean"]:.2f} ± {stats["CD9_Gyr_std"]:.2f} nm)', 
         alpha=1.0, zorder=2)
ax1.fill_between(cd63_gyr[:, 0]/1000, cd63_gyr[:, 1]-0.08, cd63_gyr[:, 1]+0.08,
                 color=COLOR_CD63, alpha=0.12)
ax1.fill_between(cd9_gyr[:, 0]/1000, cd9_gyr[:, 1]-0.08, cd9_gyr[:, 1]+0.08,
                 color=COLOR_CD9, alpha=0.12)
ax1.set_xlabel('Time (ns)', fontsize=7, fontweight='bold')
ax1.set_ylabel('R9 radius of gyration (nm)', fontsize=7, fontweight='bold')
ax1.set_title('e', fontsize=9, fontweight='bold', loc='left')
ax1.set_xlim(1.38, 4.5)
ax1.set_ylim(0.8, 6.0)
ax1.legend(fontsize=5.5, frameon=False, loc='upper right')
ax1.tick_params(labelsize=6)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Panel f: H-bonds
ax2 = plt.subplot(1, 3, 2)
ax2.plot(cd63_hb[:, 0]/1000, cd63_hb_avg, color=COLOR_CD63, linewidth=1.5, 
         label=f'CD63–R9\n({stats["CD63_Hbond_mean"]:.2f} ± {stats["CD63_Hbond_std"]:.2f})', 
         alpha=1.0, zorder=3)
ax2.plot(cd9_hb[:, 0]/1000, cd9_hb_avg, color=COLOR_CD9, linewidth=1.5, 
         label=f'CD9–R9\n({stats["CD9_Hbond_mean"]:.2f} ± {stats["CD9_Hbond_std"]:.2f})', 
         alpha=1.0, zorder=2)
ax2.fill_between(cd63_hb[:, 0]/1000, cd63_hb[:, 1]-0.3, cd63_hb[:, 1]+0.3,
                 color=COLOR_CD63, alpha=0.12)
ax2.set_xlabel('Time (ns)', fontsize=7, fontweight='bold')
ax2.set_ylabel('Protein–R9 hydrogen bonds', fontsize=7, fontweight='bold')
ax2.set_title('f', fontsize=9, fontweight='bold', loc='left')
ax2.set_xlim(1.38, 4.5)
ax2.set_ylim(-0.3, 5.5)
ax2.legend(fontsize=5.5, frameon=False, loc='upper left')
ax2.tick_params(labelsize=6)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# Panel g: Summary bar chart
ax3 = plt.subplot(1, 3, 3)

parameters = ['RMSD\n(nm)', 'RMSF\n(nm)', 'R9 Gyr\n(nm)', 'H-bonds']
cd63_values = [stats['CD63_RMSD_mean'], stats['CD63_RMSF_mean'], 
               stats['CD63_Gyr_mean'], stats['CD63_Hbond_mean']]
cd9_values = [stats['CD9_RMSD_mean'], stats['CD9_RMSF_mean'], 
              stats['CD9_Gyr_mean'], stats['CD9_Hbond_mean']]
cd63_errors = [stats['CD63_RMSD_std'], stats['CD63_RMSF_std'], 
               stats['CD63_Gyr_std'], stats['CD63_Hbond_std']]
cd9_errors = [stats['CD9_RMSD_std'], stats['CD9_RMSF_std'], 
              stats['CD9_Gyr_std'], stats['CD9_Hbond_std']]

x = np.arange(len(parameters))
width = 0.35

bars1 = ax3.bar(x - width/2, cd63_values, width, label='CD63–R9', 
                color=COLOR_CD63, alpha=0.8, edgecolor='black', linewidth=0.5,
                yerr=cd63_errors, capsize=2, error_kw={'linewidth': 0.5})
bars2 = ax3.bar(x + width/2, cd9_values, width, label='CD9–R9', 
                color=COLOR_CD9, alpha=0.8, edgecolor='black', linewidth=0.5,
                yerr=cd9_errors, capsize=2, error_kw={'linewidth': 0.5})

ax3.set_ylabel('Value', fontsize=7, fontweight='bold')
ax3.set_title('g', fontsize=9, fontweight='bold', loc='left')
ax3.set_xticks(x)
ax3.set_xticklabels(parameters, fontsize=6)
ax3.legend(fontsize=6, frameon=False, loc='upper left')
ax3.tick_params(labelsize=6)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

# Add value labels for key panels
for i, (bar1, bar2) in enumerate(zip(bars1, bars2)):
    if i >= 2:  # Only for R9 Gyr and H-bonds
        height1 = bar1.get_height()
        height2 = bar2.get_height()
        ax3.text(bar1.get_x() + bar1.get_width()/2., height1 + cd63_errors[i],
                f'{height1:.2f}', ha='center', va='bottom', fontsize=5)
        ax3.text(bar2.get_x() + bar2.get_width()/2., height2 + cd9_errors[i],
                f'{height2:.2f}', ha='center', va='bottom', fontsize=5)

plt.tight_layout(pad=0.5)
plt.savefig('/home/trungpd89/Figure2_efg.pdf', dpi=600)
plt.savefig('/home/trungpd89/Figure2_efg.png', dpi=600)
print("✓ Figure 2 (panels e, f, g) created\n")

# ============================================================================
# SUPPLEMENTARY FIGURE S1: RMSD (panel g)
# ============================================================================
print("Creating Supplementary Figure S1 (RMSD)...")

fig_s1 = plt.figure(figsize=(90/25.4, 70/25.4))
ax_rmsd = plt.subplot(1, 1, 1)

ax_rmsd.plot(cd9_rmsd[:, 0], cd9_rmsd[:, 1], color=COLOR_CD9, linewidth=1.0, 
             label=f'CD9–R9\n({stats["CD9_RMSD_mean"]:.2f} ± {stats["CD9_RMSD_std"]:.2f} nm)', 
             alpha=0.95, zorder=2)
ax_rmsd.plot(cd63_rmsd[:, 0], cd63_rmsd[:, 1], color=COLOR_CD63, linewidth=1.0, 
             label=f'CD63–R9\n({stats["CD63_RMSD_mean"]:.3f} ± {stats["CD63_RMSD_std"]:.3f} nm)', 
             alpha=0.95, zorder=3)

ax_rmsd.set_xlabel('Time (ns)', fontsize=7, fontweight='bold')
ax_rmsd.set_ylabel('Backbone RMSD (nm)', fontsize=7, fontweight='bold')
ax_rmsd.set_title('g', fontsize=9, fontweight='bold', loc='left')
ax_rmsd.set_xlim(1.38, 4.5)
ax_rmsd.legend(fontsize=6, frameon=False, loc='best')
ax_rmsd.tick_params(labelsize=6)
ax_rmsd.spines['top'].set_visible(False)
ax_rmsd.spines['right'].set_visible(False)

# Add fold difference annotation
fold_diff = stats['CD9_RMSD_mean'] / stats['CD63_RMSD_mean']
ax_rmsd.text(0.98, 0.98, f'{fold_diff:.1f}-fold difference', 
             transform=ax_rmsd.transAxes, fontsize=6,
             verticalalignment='top', horizontalalignment='right',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.tight_layout()
plt.savefig('/home/trungpd89/Supplementary_Figure_S1g_RMSD.pdf', dpi=600)
plt.savefig('/home/trungpd89/Supplementary_Figure_S1g_RMSD.png', dpi=600)
print("✓ Supplementary Figure S1 (RMSD) created\n")

# ============================================================================
# SUPPLEMENTARY FIGURE S2: RMSF (panel h)
# ============================================================================
print("Creating Supplementary Figure S2 (RMSF)...")

fig_s2 = plt.figure(figsize=(90/25.4, 70/25.4))
ax_rmsf = plt.subplot(1, 1, 1)

# Only plot protein residues (0-250)
cd63_rmsf_protein = cd63_rmsf[cd63_rmsf[:, 0] <= 250]
cd9_rmsf_protein = cd9_rmsf[cd9_rmsf[:, 0] <= 250]

ax_rmsf.plot(cd9_rmsf_protein[:, 0], cd9_rmsf_protein[:, 1], color=COLOR_CD9, 
             linewidth=1.0, label='CD9–R9', alpha=0.95, zorder=2)
ax_rmsf.plot(cd63_rmsf_protein[:, 0], cd63_rmsf_protein[:, 1], color=COLOR_CD63, 
             linewidth=1.0, label='CD63–R9', alpha=0.95, zorder=3)

ax_rmsf.set_xlabel('Residue number', fontsize=7, fontweight='bold')
ax_rmsf.set_ylabel('RMSF (nm)', fontsize=7, fontweight='bold')
ax_rmsf.set_title('h', fontsize=9, fontweight='bold', loc='left')
ax_rmsf.set_xlim(0, 250)
ax_rmsf.legend(fontsize=6, frameon=False, loc='best')
ax_rmsf.tick_params(labelsize=6)
ax_rmsf.spines['top'].set_visible(False)
ax_rmsf.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('/home/trungpd89/Supplementary_Figure_S2h_RMSF.pdf', dpi=600)
plt.savefig('/home/trungpd89/Supplementary_Figure_S2h_RMSF.png', dpi=600)
print("✓ Supplementary Figure S2 (RMSF) created\n")

# ============================================================================
# PRINT STATISTICS
# ============================================================================
print("="*80)
print("STATISTICS FOR MANUSCRIPT:")
print("="*80)
print(f"\nFigure 2 descriptions:")
print(f"(e) R9 radius of gyration:")
print(f"    CD63–R9: {stats['CD63_Gyr_mean']:.2f} ± {stats['CD63_Gyr_std']:.2f} nm (compact)")
print(f"    CD9–R9: {stats['CD9_Gyr_mean']:.2f} ± {stats['CD9_Gyr_std']:.2f} nm (extended)")
print(f"    Fold difference: {stats['CD9_Gyr_mean']/stats['CD63_Gyr_mean']:.1f}x")

print(f"\n(f) Protein–R9 hydrogen bonds:")
print(f"    CD63–R9: {stats['CD63_Hbond_mean']:.2f} ± {stats['CD63_Hbond_std']:.2f} bonds per frame")
print(f"    CD9–R9: {stats['CD9_Hbond_mean']:.2f} ± {stats['CD9_Hbond_std']:.2f} bonds per frame")
print(f"    Fold difference: {stats['CD63_Hbond_mean']/max(stats['CD9_Hbond_mean'],0.01):.0f}x")

print(f"\nSupplementary Figure S1(g) - RMSD:")
print(f"    CD63–R9: {stats['CD63_RMSD_mean']:.3f} ± {stats['CD63_RMSD_std']:.3f} nm")
print(f"    CD9–R9: {stats['CD9_RMSD_mean']:.2f} ± {stats['CD9_RMSD_std']:.2f} nm")
print(f"    Fold difference: {stats['CD9_RMSD_mean']/stats['CD63_RMSD_mean']:.1f}x")

print(f"\nSupplementary Figure S2(h) - RMSF:")
print(f"    CD63–R9: {stats['CD63_RMSF_mean']:.3f} ± {stats['CD63_RMSF_std']:.3f} nm")
print(f"    CD9–R9: {stats['CD9_RMSF_mean']:.3f} ± {stats['CD9_RMSF_std']:.3f} nm")

print("="*80)
print("\n✅ ALL FIGURES CREATED!")
print("="*80)
print("\nFiles generated:")
print("  1. Figure2_efg.pdf - Main figure panels e, f, g")
print("  2. Supplementary_Figure_S1g_RMSD.pdf - RMSD time series")
print("  3. Supplementary_Figure_S2h_RMSF.pdf - RMSF per-residue")
print("  4. PNG versions of all figures")
print("="*80)
print("\nNote: Panels c, d (PyMOL structures) require separate PyMOL script")
print("See: pymol_structure_visualization.py")
print("="*80)
