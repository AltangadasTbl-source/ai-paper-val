# Table Arithmetic and Internal-Consistency Check

## Scope and method

- **Documents audited:** DOC-001-MAIN (`jama_sarraj_2024_oi_240006_1708623114.96234.pdf`) and DOC-006-RESULTS-SUPP (`joi240006supp5_prod_1708623115.01733.pdf`).
- **Tables audited:** DOC-001 Table 1-3 and DOC-006 eTable 1-13, as designated result-relevant in the package manifest and results-supplement evidence map.
- **Checks performed:** visible count/denominator/percentage recomputation; displayed row and subgroup total reconciliation; repeated values; outcome nesting where applicable; and bounded checks of numerical range/order (including model-fit values and CIs). Percentages were accepted when within ordinary one-decimal rounding.
- **Out of scope:** protocol, SAP, administrative documents, figures, and claims requiring unavailable raw data.

## Candidate issues (3)

### TA-001 — Main Table 1 general-anesthesia percentage does not reproduce from its displayed count and column total

- **Category:** Arithmetic inconsistency
- **Location:** DOC-001-MAIN, `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 5, Table 1, *Additional characteristics*, EVT column headed `n = 168`, row `General anesthesia used`.
- **Source values:** `100 (59.9)`; stated EVT column total `n = 168`.
- **Calculation:** `100 / 168 × 100 = 59.5238%`, which rounds to **59.5%** (one decimal), not 59.9%.
- **Reasoning:** The displayed percentage differs by 0.4 percentage points and has no stated alternative denominator or missing-data qualifier. It also differs from the 59.5% shown for the same count in the as-treated eTable, although that eTable has its own denominator problem (TA-002).

### TA-002 — Supplement eTable 1 general-anesthesia percentage does not reproduce from its stated as-treated column total

- **Category:** Arithmetic inconsistency
- **Location:** DOC-006-RESULTS-SUPP, `joi240006supp5_prod_1708623115.01733.pdf`, PDF pp. 35-36, eTable 1, EVT column headed `N=170`, row `General Anesthesia Used`.
- **Source values:** `100 (59.5%)`; stated EVT column total `N=170`.
- **Calculation:** `100 / 170 × 100 = 58.8235%`, which rounds to **58.8%** (one decimal), not 59.5%.
- **Reasoning:** The reported 59.5% corresponds to 100/168 rather than the printed as-treated denominator 170. The table supplies no alternate denominator, so the percentage is not internally reproducible.

### TA-003 — Tenecteplase percentages are not reproducible from any stated nearby denominator

- **Category:** Presentation inconsistency
- **Location:** DOC-001-MAIN, PDF p. 5, Table 1, *Additional characteristics*, row `Tenecteplase used`; and DOC-006-RESULTS-SUPP, PDF pp. 35-36, eTable 1, same row.
- **Source values:**
  - DOC-001 Table 1: EVT column `n=168`, IV thrombolytics `33 (19.6)`, tenecteplase `4 (12.5)`; medical-care column `n=168`, IV thrombolytics `28 (16.8)`, tenecteplase `1 (3.7)`.
  - DOC-006 eTable 1: EVT column `N=170`, IV thrombolytics `33 (19.4%)`, tenecteplase `4 (12.5%)`; medical-care column `N=166`, IV thrombolytics `28 (17.0%)`, tenecteplase `1 (3.7%)`.
- **Calculations:**
  - Against the displayed full-column denominators, the percentages would be 4/168 = **2.4%** and 1/168 = **0.6%** in Table 1; 4/170 = **2.4%** and 1/166 = **0.6%** in eTable 1.
  - If instead intended as a subset of the immediately preceding IV-thrombolytic counts, they would be 4/33 = **12.1%** and 1/28 = **3.6%**, not 12.5% and 3.7%.
- **Reasoning:** Neither displayed column total nor the only visible plausible subgroup denominator reproduces the printed percentages. No table footnote identifies a different denominator or a missing-data subset. This is a document-verifiable denominator/presentation issue; the underlying counts cannot be adjudicated without additional source data.

## Completed checks with no additional candidates

- Table 1 / eTable 1 sex, race, transfer, and occlusion subrows reconciled to their relevant visible totals (allowing ordinary rounding).
- Table 2, Table 3, eTables 2, 5, 7-10: all displayed numerator/denominator/percentage pairs reproduced to the reported one decimal; displayed subgroup denominators reconciled within each table.
- eTable 2 nested outcomes and mortality counts were compatible with their denominators and with the displayed mRS 5-6 totals.
- eTable 7 mismatch strata reconciled to 170 EVT and 166 medical-care patients for both mismatch definitions; eTables 8-10 subgroup rows reconciled within their stated analysis subsets.
- eTable 11 reperfusion-status counts summed to the stated MR-DWI follow-up count (101 + 24 + 79 = 204); eTable 12 outcome strata each summed to 336; eTable 13 core-minus-follow-up values were 19, 50, and 82 mL, respectively, all meeting the stated >=10-mL criterion.
- eTable 6 AIC/BIC ordering, AUC bounds, and confidence-interval ordering showed no document-verifiable arithmetic anomaly.
