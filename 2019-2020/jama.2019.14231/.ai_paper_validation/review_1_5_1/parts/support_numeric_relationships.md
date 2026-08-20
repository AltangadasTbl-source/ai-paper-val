# Support Numeric Relationship Inventory — Temporary Keys

Temporary `UN` keys are complete scope records for coordinator canonicalization; they are not candidates or adjudications.

| Temporary key | Source locations | Relationship and exact rule/labels | Matching key |
|---|---|---|---|
| UN001 | DOC-002 p. 5, eTable 3 | Medication-class counts and percentages use surgery N=2287 and nonsurgical N=11435. Classes are not mutually exclusive; do not sum rows. | Main baseline treatment totals/medication table. |
| UN002 | DOC-002 p. 6, eTable 4 | Eight-year event rates are **per 100 patient-years**; difference equals nonsurgical minus surgery; 95% bootstrap CI uses 1,000 samples. Parentheses are death-with-individual-outcome composite rates. | Main outcome rate/result key. |
| UN003 | DOC-002 p. 7, eTable 5 | Eight outcomes × years 2/5/8 × treatment group: cumulative incidence percentage with 95% CI; endpoint/time/treatment must match before comparison. | Main outcome cumulative-incidence key. |
| UN004 | DOC-002 p. 8, eFigure 1 | Primary-composite subgroup labels, dichotomies, adjusted HRs and interaction P values; age/eGFR cut at medians. | Main primary composite subgroup key. |
| UN005 | DOC-002 p. 9, eTable 6 | Eight overall fully adjusted surgery-vs-nonsurgery HRs, 95% CIs, outcome P values and PH-assumption P values; last column only is PH test. | Main overall Cox-result key. |
| UN006 | DOC-002 pp. 10,19, eTable 7 | Eight time-varying fully adjusted HRs at 2/5/8 years; duplicate table requires equality across pages. | Main time-varying/sensitivity key. |
| UN007 | DOC-002 p. 11, eFigure 2 | Figure-only HbA1c percent and non-insulin-medication percentage curves, surgery/no surgery, BMI <35/at least 35; no exact point labels. | Longitudinal metabolic/medication key. |
| UN008 | DOC-002 p. 12, eTable 8 | Treatment-group difference in average change from baseline at 1/2/5/8 years: units lbs/kg/percentage points/g/dL/ug/L/percentage points; 98.8% Bonferroni CI. | Main longitudinal treatment-contrast key. |
| UN009 | DOC-002 p. 13, eTable 9 | Total observations and distinct patients by six measures, timepoint, and treatment; distinct patients are the relevant participant denominator, not total observations. | Longitudinal availability key. |
| UN010 | DOC-002 p. 14, eTable 10 | Medication-proportion denominators: surgery 2287/1820/1444/784/348 and nonsurgery 11433/10309/8762/4235/1219 at years 0/1/2/5/8. | eTable 8 medication percentage key. |
| UN011 | DOC-002 p. 15, eTable 11 | Surgery-only Kaplan-Meier cumulative intervention incidences and 95% CIs at years 1/2/5/8; abdominal procedure excludes hernia repair and cholecystectomy. | Post-surgery intervention key. |
| UN012 | DOC-002 p. 16, eFigure 3 | Figure-only nutritional curves: albumin/protein/hemoglobin g/dL and vitamin-D-25 ug/L over 8 years by treatment; p. 12 gives numeric counterparts. | Longitudinal nutrition key. |
| UN013 | DOC-002 p. 17 | Sensitivity design: five index-date samples × three ratios = 15 datasets; reported significant-dataset counts 15 for five endpoints, 13/12/11 for cerebrovascular/coronary/AF. | Sensitivity analysis key. |
| UN014 | DOC-002 p. 18, eFigure 4 | Visual 15-dataset HR/95% CI display for eight outcomes; no exact plotted values printed. | Sensitivity analysis key. |
| UN015 | DOC-002 pp. 19-20 | E-value is on risk-ratio scale; estimate and upper-CI E-values are endpoint-specific and distinct from HRs for named known risk factors. | Main sensitivity/E-value key. |
| UN016 | DOC-003 pp. 2-3 | Protocol eligibility, comparator-index sampling and propensity matching definitions; 1:5 means five surgical patients per nonsurgical patient as printed. | Main population/matching key. |
| UN017 | DOC-003 pp. 4-5 | Protocol primary/secondary composite and outcome-specific risk-set definitions, including nephropathy eGFR/dialysis rules. | Main endpoint/population key. |
| UN018 | DOC-003 p. 6 | Planned rate/cumulative-incidence/Cox/PH/imputation/multiplicity/sensitivity definitions and 15-dataset construction. | Main methods/result-definition key. |
| UN019 | DOC-003 p. 7 | Amendment definitions for adverse-event timing and E-value method; all eight endpoints and HR/nearest-null CI limit. | Support sensitivity key. |
| UN020 | DOC-002 p. 5 versus p. 14 | Nonsurgical baseline printed denominator is 11435 in eTable 3 but 11433 in medication-proportion table at year 0; populations/table denominators require explicit matching before any reconciliation. | Baseline medication denominator key. |
| UN021 | DOC-002 p. 19 | Time-varying-HR prose cross-reference says eTable 4 while the printed table below is eTable 7. This is a source label relationship requiring later exact-source comparison. | Supplement table-reference key. |

No workbook, CSV, DOC/DOCX, formula cell, cached workbook value, or non-PDF support unit is assigned or present in this scope.
