# AI Paper Validation Report

## Package Manifest

| Document ID | Source PDF | Classification | Pages | Scientific-audit scope/status |
|---|---|---|---:|---|
| DOC-001-main-article | `jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf` | Main article | 11 | Audited: PDF pp. 1-11. Native extraction pp. 1-11; rendered/OCR pp. 5-9. |
| DOC-002-protocol | `joi250084supp1_prod_1765403089.61351.pdf` | Protocol | 90 | **Not Audited by Design**: no scientific extraction, rendering, OCR, or checking. Rights screen only. |
| DOC-003-results-supplement | `joi250084supp2_prod_1765403089.61751.pdf` | Results supplement | 69 | Audited: PDF pp. 34-35 and 38-66. Pages 36-37 comparison-only and unprocessed; pp. 1-33 and 67-69 Not Audited by Design. |

Human authorization to resume the scoped processing was recorded on 2026-07-21. Source PDFs were not modified.

## AI Training Restriction Summary

This separate compliance screen reports supplied-file language only; it is not a legal opinion.

| Document ID | Status | Exact evidence location | Evidence | Human Compliance Review |
|---|---|---|---|---|
| DOC-001-main-article | Explicit AI Training Restriction | `jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf`, PDF p. 1 footer; repeated pp. 2-11 | “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Required; user authorization recorded 2026-07-21 |
| DOC-002-protocol | No AI Training Restriction Located in Provided Materials | `joi250084supp1_prod_1765403089.61351.pdf`, screened title page p. 1, confidentiality p. 41, publication/data-sharing p. 44, end matter pp. 89-90, and document/XMP metadata | No language expressly restricting or conditioning AI training, fine-tuning, or model improvement was located in the screened supplied material. | No for this AI-training screen; no inference of permission |
| DOC-003-results-supplement | Explicit AI Training Restriction | `joi250084supp2_prod_1765403089.61751.pdf`, PDF p. 1 footer; repeated pp. 2-69 | “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Required; user authorization recorded 2026-07-21 |

## Scientific Findings

### 1. C-06 — Cross-document inconsistency — Major

- **Location:** DOC-001 PDF p. 8, Figure 3B; DOC-001 p. 3, Outcomes; DOC-003 PDF p. 57, eTable 14.
- **Compared values/statements:** Figure 3B ranked axes end at Human 149 and AI 151. Vector inspection identified at least 117 Human-colored and 121 AI-colored nonzero bars. eTable 14 reports HbA1c-change populations of Human `N=103` and AI `N=106`. DOC-001 limits this endpoint to baseline HbA1c 5.7%-6.4%.
- **Basis:** The figure demonstrably displays a larger HbA1c analysis set than the co-cited table without caption explanation. Exact underlying figure N is not asserted.
- **Verification instruction:** Count plotting-data records and reconcile the Figure 3B inclusion rule with eTable 14 and the stated HbA1c restriction.

### 2. C-01 — Arithmetic inconsistency — Minor

- **Location:** DOC-003 PDF p. 55, eTable 12, second component-pattern row, Human-led DPP column.
- **Compared values:** Column denominator `N=59`; cell `10 (19%)`; preceding row reports the same numerator as `10 (17%)`.
- **Basis:** `10/59 × 100 = 16.95%`, which rounds to 17%, not 19%.
- **Verification instruction:** Inspect the cited cell and denominator and recompute `10/59`.

### 3. C-03 — Presentation inconsistency — Minor

- **Location:** DOC-001 PDF p. 6, main Table footnote a; DOC-003 PDF pp. 39-47.
- **Compared statements:** The footnote cites eTable 4 “overall,” eTable 6 “by site,” and eTable 7 “by baseline HbA1c.” Matching supplement titles are eTable 3 (p. 39, overall), eTable 5 (p. 42, by site), and eTable 6 (p. 44, by baseline A1C). eTable 4 concerns eligibility and eTable 7 completion status.
- **Basis:** All three cited table numbers do not match their parenthetical descriptors.
- **Verification instruction:** Compare each descriptor with the supplement title; verify whether citations should be eTables 3, 5, and 6.

### 4. C-04 — Statistical reporting inconsistency — Minor

- **Location:** DOC-003 PDF pp. 53-54, eTable 11, age row and footnotes 1-2.
- **Compared values/statements:** Footnote 1 reports age `P=.010`, sex `P=.041`, and all other characteristics `P>.05`. Footnote 2 reports age `P=.014` and says all other baseline characteristics were similar (`P>.05`).
- **Basis:** The table assigns age two unexplained P values; footnote 2 also conflicts with the significant sex result.
- **Verification instruction:** Establish which age P value applies to the eTable 11 `N=151/N=149` population and identify or remove the other footnote.

### 5. C-05 — Presentation inconsistency — Minor

- **Location:** DOC-001 PDF p. 8, Figure 3 footnote a; comparator main Table, PDF p. 6.
- **Compared values/statements:** Figure 3 labels `32.2 (28.2-35.9) kg/m²` and `32.5 (29.3-37.7) kg/m²` as baseline median “weight.” The Table reports the identical values as BMI.
- **Basis:** The unit and values identify BMI rather than weight.
- **Verification instruction:** Compare Figure 3 footnote a with the Table `BMI, median (IQR)` row.

### 6. C-07 — Cross-document inconsistency — Minor

- **Location:** DOC-003 PDF p. 34, eFigure 3 row label and footnote 3; DOC-001 PDF p. 3 and Figure 2, p. 7.
- **Compared statements:** The supplement states `0.2% A1C reduction`; the main article defines an absolute decrease of at least `0.2 percentage points`. Both report `35/130` in each arm.
- **Basis:** Percent and percentage points are not equivalent; matching counts show the same endpoint is labeled differently.
- **Verification instruction:** Compare the exact endpoint wording and revise the supplement label if it represents the same endpoint.

## Rejected and Uncertain Candidates

| Status | Candidate/check | Location | Retained disposition and basis |
|---|---|---|---|
| Uncertain | C-02 | DOC-003 PDF p. 59, eTable 16 | MI-pooled primary-outcome percentages are 32.2% AI and 31.9% human, while RD is `-1.1` percentage points. Direct subtraction is `+0.3`, but the package states that 20 imputed datasets were combined using Rubin’s rules and risk differences were estimated by binomial regression. The supplied material does not establish whether `-1.1` is separately modeled. Verify by reproducing MI pooling and binomial-regression estimation and identifying the estimand. |
| Rejected | Main Table arithmetic | DOC-001 PDF p. 6 | Site, demographic, BMI, and diet counts reconcile to visible arm denominators (`N=183`, `N=185`); displayed percentages are compatible with rounding. |
| Rejected | Participant-flow arithmetic | DOC-001 PDF p. 5, Figure 1 | Recruitment, exclusion, randomization, follow-up, and restricted-population counts reconcile, including `183+185=368`, restricted populations `151/149`, and 12-month attendance `157/156`. |
| Rejected | Figure 4 engagement matrix arithmetic | DOC-001 PDF p. 9 | Arm totals, row/column totals, and displayed percentages reconcile to 183 AI and 185 human participants. |
| Rejected | Main Figure 2 versus eFigure 3 risk differences | DOC-001 PDF p. 7; DOC-003 PDF p. 34 | Main Figure 2 is unadjusted; eFigure 3 is explicitly age-adjusted. Different estimates are labeled as different analyses. |
| Rejected | Supplement table totals and outcome/sensitivity arithmetic | DOC-003 PDF pp. 38-66 | Checked eTable totals, percentages, missingness/follow-up counts, outcome/sensitivity counts, and adverse-event totals reconcile within displayed precision, except retained C-01. Grade-2-and-later eTable 20d condition detail beyond p. 66 was outside scope. |
| Rejected | eFigure 4 subgroup arithmetic | DOC-003 PDF p. 35 | Subgroup denominators and achiever totals reconcile to arm totals and displayed percentages/risk differences within rounding. |
| Uncertain | eTable 7 threshold wording | DOC-003 PDF p. 47, eTable 7 footnote 1 | “No baseline characteristics were statistically significant different between groups (p<0.05)” may be a significance-threshold statement; underlying P values were not provided to establish a document-verifiable issue. |
| Uncertain | BMI-subgroup narrative | DOC-001 PDF p. 6; DOC-003 PDF p. 35 | “Lower BMI strata” may describe an overall pattern rather than every stratum; wording does not establish a definite contradiction. |
| Uncertain | Figure 3 physical-activity timing label | DOC-001 PDF p. 8 | “Physical Activity at 12 Months” and “Weekly physical activity over 12 mo” may be shortened endpoint wording; the visible figure does not resolve the intended time window. |

## Human Adjudication Checklist

- [ ] Confirm each retained finding against the cited PDF page, table, figure, and footnote.
- [ ] For C-06, inspect Figure 3B plotting data and reconcile its analysis population with eTable 14 and the HbA1c eligibility rule.
- [ ] For C-01, recompute `10/59` and confirm the reported eTable 12 cell.
- [ ] For C-03 through C-05, confirm the intended labels, cross-references, and footnotes in the production source.
- [ ] For C-07, determine whether eFigure 3 is intended to report the same HbA1c endpoint as the main article.
- [ ] Resolve C-02 only with the supplied analysis output/specification; retain its Uncertain status absent demonstrable estimator mismatch.
- [ ] Retain DOC-002 as Not Audited by Design; do not treat protocol material as scientifically audited.
- [ ] Complete the separate Human Compliance Review records for DOC-001 and DOC-003 as applicable.
