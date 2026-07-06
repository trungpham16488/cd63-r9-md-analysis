# MD Simulation Analysis: CD63 vs CD9 for R9-Exosome Engineering

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.XXXXXXX-blue)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

Molecular dynamics simulation analysis comparing the **CD63** and **CD9** tetraspanins as display scaffolds for the **R9 cell-penetrating peptide** in engineered exosome nanocarriers.

This repository supports the manuscript:

> **Computationally Engineered Peptide-Exosome Nanocarriers for Continuous Bioelectronic Monitoring of 3D Epidermal Regeneration**
> Duc-Trung Pham, *et al.*
> *Advanced Functional Materials* (2026), under review. DOI: *[to be added on acceptance]*

---

## Overview

Molecular dynamics simulation analysis demonstrating that the CD63 tetraspanin provides a superior binding interface for the R9 cell-penetrating peptide compared to CD9, despite identical EDC/NHS covalent conjugation. The scripts here reproduce every quantitative analysis and figure derived from the trajectories.

**Software**

| Component | Details |
|---|---|
| MD engine | GROMACS 2023.4 — https://www.gromacs.org/ |
| System preparation | CHARMM-GUI — https://www.charmm-gui.org/ |
| Force field | CHARMM36m |
| Analysis / plotting | Python (`numpy`, `pandas`, `matplotlib`); PyMOL |

**Systems compared:** CD63–R9 vs. CD9–R9
*[Fill in: production length, system size (atoms), replicate scheme, and headline binding-energy values for each system.]*

---

## Repository contents

| File | Description |
|---|---|
| `analysis_commands.sh` | GROMACS command pipeline for all trajectory analyses |
| `generate_all_figures.py` | Generates all publication figures from analysis outputs |
| `pymol_structure_visualization.py` | PyMOL script for structural snapshots and rendering |
| `COMPLETE_FIGURE_GUIDE.txt` | Panel-by-panel mapping of figures to scripts and data |
| `requirements.txt` | Python dependencies |
| `LICENSE` | MIT license |

---

## Requirements

- **GROMACS** 2023.4
- **CHARMM-GUI** (system preparation)
- **Python** >= 3.9 — see `requirements.txt`
- **PyMOL** (structure visualization)

```bash
pip install -r requirements.txt
```

---

## Reproducing the analysis

1. Obtain the trajectory and topology inputs (see **Data availability** below).
2. Run the GROMACS analysis pipeline:
   ```bash
   bash analysis_commands.sh
   ```
3. Generate the figures:
   ```bash
   python generate_all_figures.py
   ```
4. (Optional) Render structural views:
   ```bash
   pymol pymol_structure_visualization.py
   ```

See `COMPLETE_FIGURE_GUIDE.txt` for the mapping of each output to its manuscript figure.

---

## Data availability

The trajectory outputs, analysis scripts, and figure source data are archived on Zenodo:

**https://doi.org/10.5281/zenodo.XXXXXXX**  *[insert the Zenodo DOI for THIS repository]*

---

## Citation

Please cite both the paper and the software archive:

**Paper**
> Pham D.-T., *et al.* Computationally Engineered Peptide-Exosome Nanocarriers for Continuous Bioelectronic Monitoring of 3D Epidermal Regeneration. *Advanced Functional Materials*, 2026. DOI: *[to be added]*

**Software / data**
> Pham D.-T. MD Simulation Analysis: CD63 vs CD9 for R9-Exosome Engineering. Zenodo, 2026. https://doi.org/10.5281/zenodo.XXXXXXX

---

## License

Released under the MIT License — see [`LICENSE`](LICENSE).

## Contact

Duc-Trung Pham — *[email]*
BioMEMS & Bio-impedance Laboratory, Gachon University
