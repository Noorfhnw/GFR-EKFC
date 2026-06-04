# EKFC eGFR Calculator

A desktop application for estimating kidney function using the **European Kidney Function Consortium (EKFC)** equation. Built with Python and Tkinter.

## What It Does

Calculates **estimated Glomerular Filtration Rate (eGFR)** — a standard measure of kidney function reported in mL/min/1.73m². The result helps classify chronic kidney disease (CKD) stages and guide clinical decisions.

## The EKFC Equation

The EKFC equation uses a sex- and age-specific reference creatinine value (Q) to normalise serum creatinine before estimating GFR:

```
eGFR = 107.3 × (Scr / Q)^α × 0.990^(age − 40)   [if age > 40]
```

Where:
- **α = −0.322** if Scr/Q < 1
- **α = −1.132** if Scr/Q ≥ 1
- The age-adjustment term applies only for age > 40

### Q values

| Age | Female | Male |
|-----|--------|------|
| ≤ 25 years | Calculated from cubic polynomial | Calculated from cubic polynomial |
| > 25 years | 62.0 µmol/L (fixed) | 80.0 µmol/L (fixed) |

## Requirements

- Python 3.7+
- Tkinter (included with most Python distributions)
- No external packages required

## Running the App

```bash
python EKFC.py
```

> On some Linux systems, Tkinter must be installed separately:
> ```bash
> sudo apt-get install python3-tk
> ```

## Usage

1. Enter the patient's **age** in years
2. Enter the **serum creatinine** value
3. Select the creatinine **unit** (µmol/L or mg/dL — mg/dL is auto-converted)
4. Select **sex** (Male / Female)
5. Click **Calculate**

The eGFR result is displayed in mL/min/1.73m².

### CKD Staging Reference

| eGFR (mL/min/1.73m²) | CKD Stage |
|-----------------------|-----------|
| ≥ 90 | G1 — Normal or high |
| 60–89 | G2 — Mildly decreased |
| 45–59 | G3a — Mildly to moderately decreased |
| 30–44 | G3b — Moderately to severely decreased |
| 15–29 | G4 — Severely decreased |
| < 15 | G5 — Kidney failure |

## Reference
https://pipette.sulm.ch/files/pipette/2020-06/pipette_6-2020-004_Lorenz-Risch_EKFC-Gleichung-zur-Schaetzung-der-Nierenfuntion.pdf

## Disclaimer

This tool is intended for **informational and research purposes only**. It is not a substitute for clinical judgment. Always interpret eGFR results in the context of the full clinical picture.
