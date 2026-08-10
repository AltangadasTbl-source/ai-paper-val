# Human Adjudication Report

## Package Manifest

Package: `jama.2024.6063`. Sources unchanged; no web search, external retrieval, or unstated external knowledge used. Permissions were assumed given for this workflow.

| Document ID | Source PDF | Pages | Classification | Scientific audit scope/status |
|---|---|---:|---|---|
| `DOC-JAMA2024-6063-MAIN-2f574565` | `jama_laslett_2024_oi_240048_1727199125.7595.pdf` | 10 | Main article | Pages 1–9 audited; page 10 Not Audited by Design |
| `DOC-JAMA2024-6063-SUPP1-317ff46a` | `joi240048supp1_prod_1727199125.7845.pdf` | 15 | Protocol | Not Audited by Design |
| `DOC-JAMA2024-6063-SUPP2-57681138` | `joi240048supp2_prod_1727199125.8245.pdf` | 1 | Statistical analysis plan | Not Audited by Design |
| `DOC-JAMA2024-6063-SUPP3-67e172cd` | `joi240048supp3_prod_1727199125.83025.pdf` | 15 | Results supplement | Pages 1–15 audited; result items pages 2–15 |

## AI Training Restriction Summary

This supplied-materials screen is not legal advice and is separate from the scientific findings. No permission is inferred from silence.

| Document ID | Status | Exact evidence location | Human Compliance Review |
|---|---|---|---|
| `DOC-JAMA2024-6063-MAIN-2f574565` | No AI Training Restriction Located in Provided Materials | PDF page 1 (printed p 1997) footer, repeated PDF pages 2–10: “© 2024 American Medical Association. All rights reserved.” Metadata reviewed; no AI/training/fine-tuning/model-improvement rights language located. | No |
| `DOC-JAMA2024-6063-SUPP1-317ff46a` | No AI Training Restriction Located in Provided Materials | PDF page 1, pages 13–15, all native text, and XMP/document metadata reviewed; no applicable AI-training or rights quotation located. | No |
| `DOC-JAMA2024-6063-SUPP2-57681138` | No AI Training Restriction Located in Provided Materials | PDF page 1, footer/end matter, and PDF Info metadata reviewed. End matter: “This statistical analysis plan is an excerpt from ‘Krill oil trial protocol V2.doc’, dated 02 Feb 2016.” No rights or AI-training restriction located. | No |
| `DOC-JAMA2024-6063-SUPP3-67e172cd` | No AI Training Restriction Located in Provided Materials | PDF footers, pages 1–15: “© 2024 American Medical Association. All rights reserved.” Metadata reviewed; no AI/training/fine-tuning/model-improvement rights language located. | No |

## Scientific Findings

1. **C04 — Arithmetic inconsistency — Major**  
   **Location:** Results supplement PDF page 5, eTable 4, WOMAC weight-bearing-pain week 4.  
   **Compared values:** Krill final/baseline `100/127`, change `−84 (−122 to −46)`; placebo `108/141`, change `−103 (−141 to −65)`; between-group `+3 (−10 to 16)`, P=.66. The adjacent Function week-4 row repeats `−84 (−122 to −46)` and `−103 (−141 to −65)` and reports between-group `−19`.  
   **Basis:** Endpoint differences are approximately −27 and −33; the printed arm changes imply −19 rather than +3 and duplicate the Function-row values.  
   **Verification:** Trace the weight-bearing-pain row and compare its change cells with Function character-for-character.

2. **C05 — Presentation inconsistency — Major**  
   **Location:** Results supplement PDF page 6, eTable 4, lower-leg-strength week 12 and back-pain week 4.  
   **Compared values:** Strength final/baseline `72.6/66.5` and `70.2/65.9`; changes `−2.8 (−6.0 to 0.4)` and `−4.2 (−7.4 to −1.1)`; between-group `−1.4 (−5.9 to 3.0)`, P=.53. The entire change/inference block is identical to back-pain week 4.  
   **Basis:** Exact duplication across unrelated rows while the displayed strength means rise.  
   **Verification:** Compare every change-through-P-value cell for the two rows.

3. **C07 — Cross-document inconsistency — Major**  
   **Location:** Main article PDF page 8, Table 3, versus results supplement PDF pages 11–12, eTable 7, injury/procedural-complication category.  
   **Compared values:** Main Table 3 totals are krill/placebo `11/6`; visible eTable 7 terms sum to `6/6`.  
   **Basis:** Placebo totals agree; the krill total differs by five events.  
   **Verification:** Sum every eTable 7 preferred term within the category and compare with Table 3.

4. **C01 — Statistical reporting inconsistency — Minor**  
   **Location:** Main article PDF page 2, Key Points; page 1 Abstract; page 6, Table 2; page 7, Results; results supplement page 2, eTable 1; page 5, eTable 4.  
   **Compared values:** Key Points gives `+0.30` (95% CI `−6.9 to 6.4`; P=.94); the other locations give approximately `−0.3` with the same CI/P, including eTable 1 `−0.27 (−6.92 to 6.38)`, P=.94.  
   **Basis:** `−20.2 − (−19.9)=−0.3`; reversal of the contrast would also reverse CI endpoints, but only the Key Points estimate is positive.  
   **Verification:** Compare all six locations and confirm only Key Points is positive.

5. **C02 — Arithmetic inconsistency — Minor**  
   **Location:** Main article PDF page 8, Table 3, “Participants with an adverse event,” krill arm.  
   **Compared values:** Header `n=130`; reported `67 (50.7)`.  
   **Basis:** `67/130 × 100 = 51.5%`; `50.7%` corresponds to `67/132` after rounding.  
   **Verification:** Divide 67 by the displayed krill denominator.

6. **C03 — Cross-document inconsistency — Minor**  
   **Location:** Main article PDF page 8, Table 3 and narrative, versus results supplement PDF pages 10–11, eTable 7.  
   **Compared values:** Main krill/placebo counts: pain in extremity `1/6`, gastroesophageal reflux disease `1/3`, abdominal discomfort `0/3`, diarrhea `2/1`. eTable 7: `1/5`, `3/1`, `3/0`, `1/2`, respectively. The main narrative gives extremity pain `1/5`.  
   **Basis:** Same-term conflicts; three gastrointestinal rows are arm-reversed and extremity pain differs by one placebo event.  
   **Verification:** Compare the four named rows and narrative column-by-column.

7. **C06 — Arithmetic inconsistency — Minor**  
   **Location:** Results supplement PDF page 8, eTable 5, WORMS totals.  
   **Compared values:** Totals are 107 krill and 109 placebo. Printed/calculated percentages: `10 (12%)` versus `9.3%`; `16 (12%)` versus `14.7%`; `80 (72%)` versus `74.8%`; `75 (72%)` versus `68.8%`; `12/107=11.2%`, not 12%.  
   **Basis:** Multiple displayed percentages do not equal count divided by displayed arm total.  
   **Verification:** Recalculate every category using 107 and 109.

8. **C08 — Cross-document inconsistency — Minor**  
   **Location:** Results supplement PDF page 3, eTable 2 overall adherence row and footnote; main article PDF page 7, adherence text.  
   **Compared values:** eTable row `n=167`: krill `82 (98.8%)`, placebo `81 (96.4%)`; footnote `n=165`. Main text states 95% consumed at least 80% of softgels.  
   **Basis:** Percentages imply denominators `83+84=167`; `163/167=97.6%`, not 95%; `163/165` is also not 95%.  
   **Verification:** Infer arm denominators from percentages; compare with row/footnote n and main-text summary.

9. **C09 — Presentation inconsistency — Minor**  
   **Location:** Main article PDF page 8, Table 3 footnotes; results supplement PDF page 1, contents and eTable headings.  
   **Compared values:** Main footnotes direct detailed adverse events to eTable 4 and serious events to eTables 5 and 6. Supplement identifies eTable 4 as secondary endpoints, eTable 5 as WORMS, eTable 6 as analgesic use, eTable 7 as adverse events, and eTable 8 as serious adverse events.  
   **Basis:** The footnotes refer to unrelated supplement tables.  
   **Verification:** Match every Table 3 footnote citation to the supplement contents and headings.

10. **C10 — Presentation inconsistency — Minor**  
    **Location:** Results supplement PDF page 15, eFigure.  
    **Compared values/statements:** Caption identifies baseline as “left” and 24 weeks as “right”; renderings are vertically stacked and unlabeled.  
    **Basis:** No left/right pair maps to the displayed layout, leaving time-point assignment ambiguous.  
    **Verification:** Inspect source PDF page 15 and confirm top/bottom unlabeled renderings with a left/right caption.

## Rejected and Uncertain Candidates

None after verification and critic review. Before verification, the speculative eTable 4 hs-CRP/fasting-glucose week-12 duplication was excluded because coincidence could not be excluded from the supplied materials.

## Human Adjudication Checklist

- Confirm each cited source PDF page, table, figure, and displayed value.
- Reperform the stated arithmetic and row/column comparisons.
- Determine whether each discrepancy is a reporting, transcription, layout, or correction-status matter.
- Preserve protocol and SAP as Not Audited by Design unless a specific comparison is authorized.
- Record adjudication disposition for all 10 findings and any required correction follow-up.
