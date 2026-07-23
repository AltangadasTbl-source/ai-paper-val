# Human Adjudication Report

## Package inventory and audit scope

| Document ID | File | Classification | Scope |
|---|---|---|---|
| DOC-001 | `jama_dupuis_2024_oi_240111_1733431204.38761.pdf` | Main article, 11 pp | Audited; native text pp. 1–11; rendered pp. 5–9; no OCR |
| DOC-002 | `joi240111supp1_prod_1733431204.57929.pdf` | Protocol/SAP, 46 pp | Not Audited by Design; rights screen only |
| DOC-003 | `joi240111supp2_prod_1733431204.76024.pdf` | Results supplement, 23 pp | Audited; native text pp. 1–23; rendered pp. 2–21; no OCR |

## AI Training Restriction Summary

This is a separate compliance screen, not a scientific finding or legal opinion.

| Document ID | Status | Exact evidence location | Human Compliance Review |
|---|---|---|---|
| DOC-001 | Explicit AI Training Restriction | Footer, PDF pp. 1–11: “© 2024 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Required before full-text processing; treated as approved under the user's instruction to assume all permissions were given |
| DOC-002 | No AI Training Restriction Located in Provided Materials | Supplied PDF pp. 1–46 and embedded metadata; no training, fine-tuning, or model-improvement restriction located | Not required by this document-level screen |
| DOC-003 | No AI Training Restriction Located in Provided Materials | Supplied PDF pp. 1–23 and embedded metadata; no training, fine-tuning, or model-improvement restriction located | Not required by this document-level screen |

## Final scientific issues

### 1. Statistical reporting inconsistency — Minor

- **Location:** DOC-003, eTable 10, PDF pp. 13–15; eMethods, PDF p. 22.
- **Source evidence:** eTable 10 labels its comparison columns “Difference (95% CI).” For diarrhea documentation among participants with SSPedi score ≥1, it reports 5/26 versus 2/56 and an estimate of 6.43 (95% CI, 1.16–35.74). The eMethods states that these logistic models estimate odds ratios.
- **Basis:** The crude odds ratio is `(5/21) / (2/54) = 6.43`. The risk difference is `5/26 - 2/56 = 0.157`. The displayed estimate is an odds ratio, not a difference.
- **Human verification:** Compare the eTable 10 headings with the p. 22 eMethods and independently calculate the example odds ratio. Confirm the intended effect-measure label.

### 2. Presentation inconsistency — Minor

- **Location:** DOC-001, Figure 2, PDF p. 8 / printed p. 1988; Table 2, PDF p. 7 / printed p. 1987; Results, PDF p. 4 / printed p. 1984.
- **Source evidence:** Figure 2 displays separate Baseline and Week 8 panels, but its unqualified caption states that the participant numbers are 198 in the symptom-screening group and 209 in the usual-care group. Table 2 and the Results report baseline denominators of 216 and 213 and week-8 denominators of 198 and 209.
- **Basis:** The global caption supplies only the week-8 denominators for a two-time-point figure. It does not give baseline denominators or state that the baseline panel was restricted to week-8 complete cases. This finding does not establish that any plotted bar is numerically wrong.
- **Human verification:** Compare both Figure 2 panel labels and its caption with the time-specific denominators in Table 2 and the Results. Clarify which denominator applies to each panel.

### 3. Presentation inconsistency — Minor

- **Location:** DOC-003, eFigure 3, PDF p. 21; DOC-001, Table 2, PDF p. 7 / printed p. 1987.
- **Source evidence:** Each eFigure 3 annotation has the form estimate `[lower, upper; third value]`, but the legend defines only the mean difference and 95% CI. The third values—.95, .66, .41, .34, .22, .71, .83, and .45—match the adjusted P values for the same PedsQL domains in DOC-001 Table 2.
- **Basis:** The figure displays P values without identifying the third annotation value in the legend.
- **Human verification:** Match each eFigure 3 third value to Table 2's adjusted P-value column and confirm that the legend omits the definition. Add an explicit legend definition if these are the intended P values.

## Disposition summary

- One candidate was **Uncertain**: the article calls a comparison significant while displaying `P=.05`, but the package does not provide the unrounded P value needed to determine whether it was below .05.
- One candidate was **Rejected**: sparse zero-cell odds-ratio CI/P-value combinations were reproducible using a 0.5 correction for the OR/CIs and two-sided Fisher exact tests.
- Neither candidate is included in the final issue list.

## Limitations and scope

The assessment used only the supplied article package and was limited to arithmetic, cross-document, statistical reporting, participant flow, and presentation inconsistencies. DOC-002 scientific content was Not Audited by Design. The audit did not assess research misconduct, raw-data validity, clinical appropriateness, general methodological limitations, novelty, or information outside the package.

**Submit for Human Adjudication.**

