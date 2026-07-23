# Human Adjudication Report

## Package Manifest

| Document ID | Source PDF | Classification | Scientific processing outcome |
|---|---|---|---|
| DOC-001-main-article | `jama_martin_2025_oi_250042_1753377747.91025.pdf` | Main article; 11 pages | Complete: native extraction pp. 1-11; selective render/OCR pp. 1 and 3-10. |
| DOC-002-supplement-1-protocol-sap | `joi250042supp1_prod_1753377747.92525.pdf` | Combined protocol and SAP; 136 pages | **Not Audited by Design**: no scientific extraction, rendering, or OCR; retained for rights screening only. |
| DOC-003-supplement-2-results | `joi250042supp2_prod_1753377747.93025.pdf` | Results supplement; 29 pages | Complete: native extraction pp. 2-27; selective render/OCR pp. 8-27; pp. 1 and 28-29 not audited by design. |

Source PDFs were unchanged. No external sources were used.

## AI Training Restriction Summary

This document-level compliance screen is separate from the scientific findings. User-reported AI-use permission allowed processing to continue; this screen does not provide legal advice.

| Document ID | Status | Exact evidence location and notice | Human Compliance Review |
|---|---|---|---|
| DOC-001-main-article | Explicit AI Training Restriction | PDF p. 1 (printed p. 398), footer: "© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies." The same footer was sampled on PDF pp. 2, 10, and 11. | Yes; user-reported permission allowed continuation. |
| DOC-002-supplement-1-protocol-sap | No AI Training Restriction Located in Provided Materials | PDF pp. 1 and 136; embedded document-information/XMP metadata; PDF structure; and literal embedded-term scan: no AI-training, fine-tuning, model-improvement, rights, license, permissions, or terms notice located. | No. |
| DOC-003-supplement-2-results | Explicit AI Training Restriction | PDF p. 1, top copyright notice: "© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies." The same notice appears in native text on PDF pp. 1-29. | Yes; user-reported permission allowed continuation. |

## Scientific Findings

Five findings were accepted, all Minor.

### C1 — Incorrect supplementary-figure citation for time to death

- **Category / severity:** Cross-document inconsistency / Minor.
- **Exact location:** Main article, PDF p. 6, Results, "Primary and Secondary Outcomes"; results supplement, PDF pp. 11-12, eFigures 4-5.
- **Compared statements:** The main text reports time to death, adjusted HR 1.01 (95% CI, 0.96-1.05), and cites "eFigure 4 in Supplement 2." eFigure 4 (supplement p. 11) shows FiO2/SpO2 separation. eFigure 5 (p. 12) is the Kaplan-Meier all-cause mortality plot and reports HR 1.01 (95% CI, 0.96-1.05; P=.82).
- **Basis:** The main-text estimate matches eFigure 5, not eFigure 4.
- **Verification:** Compare main-article p. 6 with supplement pp. 11-12 and confirm that the citation should identify eFigure 5.

### C2 — UK-ROX achieved-oxygenation summary does not identify its metric-specific source-row change

- **Category / severity:** Presentation inconsistency / Minor.
- **Exact location:** Results supplement, PDF p. 27, eTable 10; PDF p. 21, eTable 5; main article, PDF p. 6, "Oxygen Exposure."
- **Compared values:** eTable 10 gives UK-ROX SpO2 93.3% vs 95.2%, PaO2 71.5 vs 79.5 mm Hg, and FiO2 0.31 vs 0.35. eTable 5 gives overall vs oxygen-only values: SpO2 93.3% vs 95.1% / 93.3% vs 95.2%; PaO2 71.5 vs 79.5 / 73.8 vs 81.4 mm Hg; FiO2 0.31 vs 0.35 / 0.35 vs 0.37. The main text reports the overall pairs.
- **Basis:** eTable 10 uses the oxygen-only SpO2 pair but the overall PaO2 and FiO2 pairs without identifying the metric-specific analytic subset. No numeric value is established as wrong.
- **Verification:** Compare eTable 10 with both eTable 5 rows; confirm the intended source row for each metric and label the subset explicitly or harmonize the rows.

### C4 — HOT-ICU publication year is truncated

- **Category / severity:** Presentation inconsistency / Minor.
- **Exact location:** Results supplement, PDF p. 27, eTable 10, "Year published," HOT-ICU column.
- **Compared values:** HOT-ICU is `202`; adjacent trial entries are 2025, 2024, 2023, 2022, 2021, and 2020.
- **Basis:** `202` is a three-digit entry in a four-digit-year row; the supplied documents do not establish the missing digit.
- **Verification:** Check the production/source table and replace `202` with the intended four-digit year.

### C5 — FiO2 fractions are mislabeled as percentages in eTable 6

- **Category / severity:** Presentation inconsistency / Minor.
- **Exact location:** Results supplement, PDF p. 22, eTable 6; comparison: PDF p. 21, eTable 5, and PDF p. 27, eTable 10.
- **Compared values/statements:** eTable 6 labels "Patient median FiO2, %" and "Patient median FiO2 when receiving O2, %" while displaying fractions including 0.32 vs 0.35, 0.30 vs 0.35, 0.36 vs 0.37, and 0.34 vs 0.37. eTable 5 omits percent signs and uses the fractional scale; eTable 10 defines FiO2 as fraction of inspired oxygen and reports fractions such as 0.31 and 0.35.
- **Basis:** The displayed scale is fractional, while the eTable 6 labels assign percent units.
- **Verification:** Confirm removal of the two percent signs. If percent units were intended, verify consistent conversion of all associated values and differences.

### C6 — PILOT recruitment-date asterisk is undefined

- **Category / severity:** Presentation inconsistency / Minor.
- **Exact location:** Results supplement, PDF p. 27, eTable 10, PILOT "Recruitment dates" and table footnotes.
- **Compared statements:** Recruitment dates are `07/2018 to 08/2021*`. The footnote area defines only superscript `a` for "Achieved oxygenation"; it has no asterisked note or legend.
- **Basis:** The visible annotation marker has no corresponding explanation.
- **Verification:** Check the production/source table; restore the omitted asterisk note or remove the marker if unintended.

## Rejected and Uncertain Candidates

- **Rejected:** None.
- **C3 — Uncertain; Presentation inconsistency.** Results supplement PDF p. 26, eTable 9, leaves both overall "Events, No." cells blank while adjacent patient cells show 58 (0.7%) and 29 (0.4%). Listed event counts total 64 conservative events (`2+12+16+19+7+1+1+1+1+1+1+0+1+1`) and 37 usual events (`1+8+15+11+0+0+0+0+0+0+0+2+0+0`). The package does not establish that totals were intended in the blank cells. **Verification:** Ask the production/source-table owner whether the cells were intentionally blank and, if not, verify intended totals before correction.

## Human Adjudication Checklist

- Confirm C1, C2, C4, C5, and C6 against the cited original PDF pages.
- For C1, confirm the eFigure 5 cross-reference.
- For C2, confirm the intended analytic subset for each eTable 10 metric.
- Confirm the intended source-table correction for C4-C6; do not infer the missing HOT-ICU year digit.
- Resolve C3 only with production/source-table confirmation; it is not an accepted scientific finding.
- Review the separate AI Training Restriction Summary and document-level processing outcomes, including DOC-002 as Not Audited by Design.
