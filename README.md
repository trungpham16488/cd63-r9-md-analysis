# MD Simulation Analysis: CD63 vs CD9 for R9-Exosome Engineering

[![DOI](https://img.shields.io/badge/DOI-10.XXXX%2Fxxxxxx-blue)](https://doi.org/10.XXXX/xxxxxx)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

Molecular dynamics simulation analysis demonstrating that CD63 tetraspanin provides superior binding interface for R9 cell-penetrating peptide compared to CD9, despite identical EDC/NHS covalent conjugation.

**Publication:** [Your paper title]  
**Authors:** Duc-Trung Pham, et al.  
**Journal:** Nature Communications (submitted/in press/published)

## Key Findings

- **4-fold difference** in R9 conformation: CD63-R9 compact (1.26 nm) vs CD9-R9 extended (4.98 nm)
- **183-fold difference** in H-bonds: CD63-R9 maintains stable binding interface (1.83 bonds) vs CD9-R9 negligible (0.01 bonds)
- **Clinical implication:** CD63 is superior scaffold for R9-engineered therapeutic exosomes

## Repository Contents

```
.
├── scripts/                    # Analysis and visualization scripts
│   ├── generate_all_figures.py
│   ├── pymol_structure_visualization.py
│   └── analysis_commands.sh
├── docs/                       # Documentation
├── results/                    # Example outputs
├── requirements.txt            # Python dependencies
├── LICENSE                     # MIT License
└── README.md                   # This file
```

## Requirements

### Software
- GROMACS 2023.4+ ([Download](https://www.gromacs.org/))
- Python 3.x
- PyMOL (for structure visualization)

### Python Packages
```bash
pip install -r requirements.txt
```

Required packages:
- numpy >= 1.20.0
- pandas >= 1.3.0
- matplotlib >= 3.4.0
- openpyxl >= 3.0.0

## Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/cd63-r9-md-analysis.git
cd cd63-r9-md-analysis
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate Figures
```bash
cd scripts
python3 generate_all_figures.py
```

This creates:
- `Figure2_efg.pdf` - Main figure panels (e, f, g)
- `Supplementary_Figure_S1g_RMSD.pdf` - RMSD validation
- `Supplementary_Figure_S2h_RMSF.pdf` - RMSF analysis

### 4. Generate Structure Visualizations (Optional)
```bash
# Requires PyMOL and minimized structure files
pymol cd63_r9_minimized.pdb pymol_structure_visualization.py
```

## Simulation Details

- **Force field:** CHARMM36m
- **Water model:** TIP3P
- **Salt:** 0.15 M NaCl
- **Temperature:** 300 K (V-rescale thermostat)
- **Pressure:** 1 bar (Parrinello-Rahman barostat)
- **Equilibration:** 1.38 ns (NVT + NPT)
- **Production:** 3.12 ns (1.38-4.5 ns total)

## Analysis Methods

### Trajectory Analysis (GROMACS)
- **RMSD:** Backbone stability
- **RMSF:** Per-residue flexibility
- **Gyration:** R9 peptide compactness
- **H-bonds:** Protein-R9 interactions

See `scripts/analysis_commands.sh` for complete workflow.

### Visualization (Python/Matplotlib)
- Time series plots with running averages (50-frame window)
- Statistical comparisons with error bars (mean ± SD)
- Publication-quality output (600 DPI, Nature format)

## Data Availability

Due to large file sizes (>10 GB), trajectory files are available from the corresponding author upon reasonable request. 

Source data for all figures is provided in the publication's Supplementary Information.

## Citation

If you use this code, please cite:

```bibtex
@article{pham2026cd63,
  title={CD63 provides superior binding interface for R9-engineered exosomes},
  author={Pham, Duc-Trung and others},
  journal={Nature Communications},
  year={2026},
  doi={10.XXXX/xxxxxx}
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

**Duc-Trung Pham**  
BioMEMS & Bio-impedance Lab  
Department of Biomedical Engineering  
Gachon University, South Korea  
Email: [your.email@example.com]

## Acknowledgments

- MD simulations performed using GROMACS 2023.4
- System preparation with CHARMM-GUI
- Analysis and visualization using Python scientific stack (NumPy, Pandas, Matplotlib)

## Contributing

This repository contains code for a published study. For questions or issues, please open a GitHub issue or contact the corresponding author.

---

**Keywords:** Molecular dynamics, exosomes, CD63, CD9, R9 peptide, cell-penetrating peptide, drug delivery, nanomedicine
