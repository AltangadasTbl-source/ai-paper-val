# Package Manifest

Package: `jama.2025.11178`

| Document ID | Source file | Pages | Classification | Scientific audit scope |
|---|---|---:|---|---|
| DOC-001-MAIN | `jama_debar_2025_oi_250046_1755300121.13587.pdf` | 14 | Main article | Pages 1-14 |
| DOC-002-PROTOCOL | `joi250046supp1_prod_1755300121.14087.pdf` | 77 | Protocol | Not Audited by Design; specific comparison only |
| DOC-003-SAP | `joi250046supp2_prod_1755300121.15087.pdf` | 29 | Statistical analysis plan | Not Audited by Design; specific comparison only |
| DOC-004-INTERVENTION | `joi250046supp3_prod_1755300121.15087.pdf` | 7 | Intervention description / TIDieR | Not Audited by Design |
| DOC-005-RESULTS | `joi250046supp4_prod_1755300121.15587.pdf` | 19 | Results supplement | Pages 3-18; page 2 context only |
| DOC-006-XLSX | `joi250046supp5_prod_1755300121.16087.xlsx` | N/A | Results workbook, sheet `eTable 3` | Entire sheet |

Source PDFs were preserved unchanged. DOC-006-XLSX is a supplied result artifact and is not subject to the PDF-only rights-record requirement.

# AI Training Restriction Summary

This screen is separate from the scientific findings and is not a legal opinion. The coordinator reports institutional permission for AI use as granted.

| Document ID | Status | Exact evidence location and quotation | Human Compliance Review |
|---|---|---|---|
| DOC-001-MAIN | Explicit AI Training Restriction | PDF p. 1 footer; also pp. 2-14: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Yes |
| DOC-002-PROTOCOL | No AI Training Restriction Located in Provided Materials | Embedded document information/XMP; targeted review pp. 1-2; supplied-file keyword screen. No AI-training, fine-tuning, or model-improvement restriction language located. | No |
| DOC-003-SAP | No AI Training Restriction Located in Provided Materials | Embedded document information/XMP, `dc:title`/PDF Title: “CONFIDENTIAL”; targeted review pp. 1-2; supplied-file keyword screen. No AI-training, fine-tuning, or model-improvement restriction language located. | No |
| DOC-004-INTERVENTION | Explicit AI Training Restriction | PDF p. 1 footer; also pp. 2-7: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Yes |
| DOC-005-RESULTS | Explicit AI Training Restriction | PDF p. 1 footer; also pp. 2-19: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Yes |

# Scientific Findings

1. **Category:** Participant flow inconsistency  
   **Severity:** Major  
   **Location:** DOC-005-RESULTS, PDF p. 7, eTable 1; corroboration: DOC-001-MAIN, PDF p. 5, Figure 1; DOC-006-XLSX, `eTable 3`, B2:E3.  
   **Values/statements:** Overall randomized N=2331; at least 1 follow-up=2036; no/one/two/three follow-ups=295/188/283/1568. painTRAINER: 776; 643; 133/77/103/464. Health Coach: 778; 690; 88/47/81/564.  
   **Calculation/logical basis:** Overall pattern total `295+188+283+1568=2334`, 3 above 2331; follow-up pattern total `188+283+1568=2039`, 3 above 2036. painTRAINER totals are 777 and 644; Health Coach totals are 780 and 692. Workbook partition is `295+468+1568=2331`.  
   **Verification instruction:** Reconcile eTable 1 pattern cells with participant-flow totals and source analysis output.

2. **Category:** Statistical reporting inconsistency  
   **Severity:** Major  
   **Location:** DOC-005-RESULTS, PDF p. 8, eTable 3.  
   **Values/statements:** `-0.28 (-0.47 to -0.08), P=.150`; `-0.20 (-0.36 to -0.03), P=.226`; `-0.30 (-0.58 to -0.02), P=.280`; `-0.47 (-0.74 to -0.19), P=.090`; `0.19 (0.08 to 0.29), P=.069`; `0.15 (0.05 to 0.24), P=.124`; `0.16 (0.07 to 0.25), P=.077`.  
   **Calculation/logical basis:** Each printed 95% CI excludes 0 while its paired P value exceeds .05.  
   **Verification instruction:** Compare the seven rows with fitted-model output and restore coefficient, CI, and P-value alignment.

3. **Category:** Arithmetic inconsistency  
   **Severity:** Minor  
   **Location:** DOC-006-XLSX, `eTable 3`, E3 and A82:E83.  
   **Values/statements:** Group N=1568; missing=2; current depression=711 (73.2).  
   **Calculation/logical basis:** Nonmissing denominator=`1568-2=1566`; `711/1566=45.4%`, not 73.2%.  
   **Verification instruction:** Recalculate E82 from source analysis output.

4. **Category:** Statistical reporting inconsistency  
   **Severity:** Major  
   **Location:** DOC-001-MAIN, Table 3, PDF pp. 10-11 / JAMA pp. 601-602.  
   **Values/statements:** Eight cited SMD point estimates lie outside printed CIs, including pain severity at 12 months: `-0.25 (-0.24 to 0.01)` and `-0.36 (-0.35 to -0.12)`; PGIC-pain at 12 months: `-0.55 (-0.50 to 0.05)`, `-0.57 (-0.54 to -0.08)`, and `-0.29 (-0.25 to 0.14)`. All 18 SMD cells in social-role and physical-function blocks across 3, 6, and 12 months display descending interval endpoints. Four cited SMDs have signs opposite to corresponding adjusted mean differences.  
   **Calculation/logical basis:** Point estimates must fall within their stated CIs; CI limits should be lower-to-upper; Table 3 footnote d defines SMD as adjusted mean difference divided by a positive usual-care change SD, which cannot reverse sign.  
   **Verification instruction:** Compare all affected SMD estimates, intervals, and comparison placement with source output and the stated standardization rule.

5. **Category:** Statistical reporting inconsistency  
   **Severity:** Minor  
   **Location:** DOC-001-MAIN, Results—Secondary Outcomes, PDF p. 7 / JAMA p. 598; Table 3, PDF p. 10 / JAMA p. 601.  
   **Values/statements:** Text reports 3-month pain-severity SMDs `-0.26` (painTRAINER vs usual care) and `-0.36` (Health Coach vs usual care); Table 3 reports `-0.25` and `-0.34`.  
   **Calculation/logical basis:** Published estimates for the same effects differ at two-decimal precision.  
   **Verification instruction:** Identify authoritative source-output values and align text and Table 3.

6. **Category:** Presentation inconsistency  
   **Severity:** Minor  
   **Location:** DOC-005-RESULTS, PDF p. 9, eTable 4.  
   **Values/statements:** `Health Coach vs. painTRAINER 3M` appears twice; both rows report `RR 1.20`, `95% CI 1.03 to 1.40`, `P=.019`.  
   **Calculation/logical basis:** Row label, time point, estimate, interval, and P value are exact duplicates within one table.  
   **Verification instruction:** Compare row sequence with coefficient export; determine whether the second row should be removed or relabeled.

7. **Category:** Presentation inconsistency  
   **Severity:** Minor  
   **Location:** DOC-005-RESULTS, PDF p. 8, eTable 3; PDF p. 9, eTable 4.  
   **Values/statements:** Each table contains two differently valued rows labeled `Education: AA degree (ref = High school or less)`. eTable 4 has three rows labeled only `Site`; corresponding eTable 3 rows are Site 2, Site 3, and Site 4.  
   **Calculation/logical basis:** Printed labels do not unambiguously assign distinct coefficients to covariate levels.  
   **Verification instruction:** Restore exact design-matrix level labels for education and site coefficients.

8. **Category:** Presentation inconsistency  
   **Severity:** Minor  
   **Location:** DOC-005-RESULTS, PDF p. 14, eTable 8, first subset header.  
   **Values/statements:** `Randomized prior to 8/9/2021, N=454; 366 with at least 1 follow-up; PT=149, HC=153, UC=152 at 3-months`.  
   **Calculation/logical basis:** `149+153+152=454`, the full randomized subset; this cannot represent observed 3-month counts when 366 had at least one follow-up at any assessed time.  
   **Verification instruction:** Check subset dataset and analysis definition to determine the correct label or counts.

9. **Category:** Presentation inconsistency  
   **Severity:** Minor  
   **Location:** DOC-005-RESULTS, PDF p. 15, section lead-in, eTable 9 title, and footnote b.  
   **Values/statements:** Section heading: `ADDITIONAL UNADJUSTED DATA AND ANALYSES`; text says no adjustment, weighting, or imputation; title says `adjusted relative risk`; footnote b says calculated `without adjustment`.  
   **Calculation/logical basis:** Title directly conflicts with the nearby description and footnote.  
   **Verification instruction:** Confirm model specification and make section text, title, and footnote consistent.

10. **Category:** Presentation inconsistency  
    **Severity:** Minor  
    **Location:** DOC-005-RESULTS, PDF p. 15 lead-in; PDF p. 17, eTable 11 title/header.  
    **Values/statements:** Lead-in describes `unadjusted mean secondary outcomes`; eTable 11 title says `Unadjusted Median and Interquartile Ranges`; raw-score columns are medians/percentile ranges while comparison columns are mean differences.  
    **Calculation/logical basis:** Prose and table give incompatible summary-statistic descriptions for raw treatment-group results.  
    **Verification instruction:** Compare eTable 11 with source analysis output and make prose, title, and headers use the correct description consistently.

# Rejected and Uncertain Candidates

No whole candidate was rejected. C01-C10 were verified; no candidate-level uncertainty was retained.

Excluded, not verified interpretations:

- **C04:** No evidence establishes a column-mapping, transposition, or other specific production mechanism.
- **C08:** No evidence establishes whether arm values are randomized denominators, imputed-analysis denominators, or another quantity; no replacement label or counts are established.
- **C10:** No evidence proves the proposed raw-score treatment-column permutation or establishes whether raw values should be means or medians.

Three cap-excluded candidates were outside the verifier’s C01-C10 scope and are **not verified**: the supplement p. 6 eFigure cross-reference, the eTable 8 RR-header footnote marker, and the supplement p. 5 duplicated treatment-level abbreviation. They are not retained as scientific findings.

# Human Adjudication Checklist

- Confirm that all 10 scientific findings remain within the stated evidence and issue taxonomy.
- Reconcile C01-C03 against participant-level, workbook, and fitted-model outputs.
- Reconcile C04-C05 against authoritative Table 3 analysis outputs.
- Confirm intended labels, row order, and summary-statistic descriptions for C06-C10.
- Do not treat excluded interpretations or cap-excluded candidates as findings without separate verification.
- Complete Human Compliance Review for DOC-001-MAIN, DOC-004-INTERVENTION, and DOC-005-RESULTS; institutional permission for AI use was reported granted.

