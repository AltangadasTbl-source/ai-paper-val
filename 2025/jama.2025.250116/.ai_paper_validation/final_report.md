# Package Manifest

| Document ID | Source file | Pages | Classification | Scientific-processing status |
|---|---|---:|---|---|
| DOC-001-MAIN | `jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf` | 12 | Main article | Audited: PDF pp 1-9; pp 10-12 context only. |
| DOC-002-PROTOCOL | `joi250116supp1_prod_1771885794.26255.pdf` | 72 | Protocol/SAP/administrative material | Not Audited by Design; no targeted protocol-to-report comparison requested. |
| DOC-003-RESULTS-SUPP | `joi250116supp2_prod_1771885794.27755.pdf` | 54 | Results supplement | Audited: result-relevant PDF pp 6-8 and 14-53. |

Source PDFs were read only and retained unchanged.

# AI Training Restriction Summary

This compliance screen is separate from the scientific findings and is not a legal opinion.

| Document ID | Status | Exact evidence location | Human Compliance Review |
|---|---|---|---|
| DOC-001-MAIN | Explicit AI Training Restriction | PDF p 1 footer; repeated on pp 2-12: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Required; authorization recorded 2026-07-21. |
| DOC-002-PROTOCOL | No AI Training Restriction Located in Provided Materials | Reviewed PDF pp 1-2, 61-63, and 72; metadata/XMP, page-content keywords, raw PDF strings, attachments/catalog Names, and reviewed-page annotations. No qualifying language located. | Not triggered by this status. |
| DOC-003-RESULTS-SUPP | Explicit AI Training Restriction | PDF p 1; repeated throughout, including p 54: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Required; authorization recorded 2026-07-21. |

Recorded authorization: the project user authorized continuation of model-mediated processing for DOC-001-MAIN and DOC-003-RESULTS-SUPP on 2026-07-21. DOC-002-PROTOCOL remains Not Audited by Design unless a specific protocol-to-report comparison is requested.

# Scientific Findings

1. **C01 — Minor — Statistical reporting inconsistency**  
   **Location:** DOC-001-MAIN PDF p 6, Table 2; p 7, “Secondary End Points”; DOC-003-RESULTS-SUPP PDF p 22, eTable 10.  
   **Compared values:** Table 2 reports 52/131 (39.7%); narrative reports 51/131 (39.7%); eTable 10 strata are 12/25 and 40/106.  
   **Basis:** 12 + 40 = 52; 52/131 = 39.7%, whereas 51/131 = 38.9%.  
   **Verify:** Reconcile the narrative numerator and percentage with Table 2 and eTable 10.

2. **C02 — Minor — Arithmetic inconsistency**  
   **Location:** DOC-003-RESULTS-SUPP PDF p 22, eTable 10, “SII days 2-15” row.  
   **Compared values:** Reported 40/106 versus 29/122; OR 1.194 (95% CI, 1.09-3.45), P=.030.  
   **Basis:** Non-events are 66 and 93; cross-product OR = (40×93)/(66×29) = 1.9436. The printed CI is approximately compatible with 1.94.  
   **Verify:** Recalculate the displayed crude OR and confirm the intended reported point estimate.

3. **C03 — Minor — Statistical reporting inconsistency**  
   **Location:** DOC-003-RESULTS-SUPP PDF p 53, eFigure 9, panel B, APACHE II ≥25 entry.  
   **Compared values:** Reported OR 0.11 (95% CI, 0.36-3.42), P=.86; panel-A cells are 31/38 versus 32/40.  
   **Basis:** The reported point estimate lies outside its CI. Displayed cells yield (31×8)/(7×32) = 1.107, with approximate CI 0.358-3.421.  
   **Verify:** Confirm the point estimate, CI, and linked event cells in the source analysis.

4. **C04 — Major — Presentation inconsistency**  
   **Location:** DOC-003-RESULTS-SUPP PDF pp 51-52, eFigures 7-8, panel B.  
   **Compared values:** eFigure 8 repeats all six eFigure 7 panel-B OR/CI/P triplets, although eFigure 8 presents 28-day mortality with different displayed event cells.  
   **Basis:** eFigure 8 high-stratum mortality cells yield approximate ORs 0.66, 0.42, and 0.46, rather than the repeated 1.85, 5.79, and 3.08.  
   **Verify:** Compare eFigure 8 panel-B labels and annotations against its displayed mortality cells and source output.

5. **C05 — Major — Statistical reporting inconsistency**  
   **Location:** DOC-003-RESULTS-SUPP PDF pp 51 and 53, eFigures 7 and 9, panel B/captions; DOC-001-MAIN PDF p 8, “Post Hoc and Subgroup Analyses.”  
   **Compared statements:** eFigures 7 and 9 label high-stratum treatment ORs as interaction tests; the main text interprets selected entries as interactions.  
   **Basis:** eFigure 7 high-stratum ORs reconstruct as 1.846, 5.798, and 3.084; for SOFA, the low-stratum OR is 2.019, making the crude ratio of stratum-specific treatment ORs approximately 1.53, not 3.08. eFigure 9 high-stratum CCI and SOFA estimates similarly reconstruct as 0.4875 and 0.5253. This finding is independently supported without eFigure 8.  
   **Verify:** Confirm whether the panel-B values are within-high-stratum treatment effects or interaction-test estimates, and align figure labels/captions and main-text interpretation accordingly.

6. **C06 — Minor — Presentation inconsistency**  
   **Location:** DOC-003-RESULTS-SUPP PDF p 30, eTable 14, “severe” row, SII/rhIFNγ column.  
   **Compared value:** Displayed cell: `45 42.5)`.  
   **Basis:** The opening parenthesis is missing; 45/106 = 42.45%, which rounds to 42.5%.  
   **Verify:** Correct the cell notation while retaining the displayed count and percentage if confirmed.

7. **C07 — Minor — Presentation inconsistency**  
   **Location:** DOC-003-RESULTS-SUPP PDF p 30, eTable 14, “probably related” row, MALS/anakinra column.  
   **Compared value:** Displayed cell: `0 0 (0.0)`.  
   **Basis:** The table heading specifies `n (%)`; the first zero is duplicated.  
   **Verify:** Confirm the intended zero-event cell and remove the duplicate character.

# Rejected and Uncertain Candidates

Rejected: none.  
Uncertain: none.

# Human Adjudication Checklist

- Confirm the recorded Human Compliance Review authorization for DOC-001-MAIN and DOC-003-RESULTS-SUPP.
- Confirm DOC-002-PROTOCOL remains outside scientific audit scope absent a targeted comparison.
- Adjudicate each of the seven accepted findings against the cited PDF page and table/figure location.
- Determine required corrections to source values, labels, captions, and narrative text.
- Record the final disposition for C01-C07.

