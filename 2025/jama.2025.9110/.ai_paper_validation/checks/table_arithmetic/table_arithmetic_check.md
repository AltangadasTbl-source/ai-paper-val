# Table Arithmetic Check - JAMA 2025.9110

## Scope and method

- **Checker:** `table_arithmetic_checker`
- **Sources used:** `JAMA2025_9110_D01_MAIN` main-article result evidence and page-linked preprocessing artifacts; `JAMA2025_9110_D04_RESULTS_SUPP` results-supplement evidence map and page-linked preprocessing artifacts.
- **Excluded by design:** protocol (`D02`), statistical analysis plan (`D03`), administrative material, and result figures. No external sources or raw data were used.
- **Tables inspected:** Main article Table 1 (p. 5) and Table 2 (p. 7); supplement eTables 3-14 (pp. 9-22). eTables 1-2 (pp. 7-8) contain eligibility/outcome definitions rather than result counts, so no arithmetic test applied.
- **Method:** checked displayed numerators/denominators and rounded percentages, mutually exclusive row totals, column totals, period-by-treatment subtotals, repeated treatment totals, and visible adjacent-column relationships. Rendered source pages were used to confirm the candidate and selected count-heavy tables; native/OCR text was used only as page-linked reading support.

## Candidate issues

### TA-01 - Sex rows do not account for the displayed Period 3 augmented-protein denominator

- **Category:** Arithmetic inconsistency
- **Confidence:** High
- **Exact location:** `joi250040supp3_prod_1753124024.38098.pdf` (`JAMA2025_9110_D04_RESULTS_SUPP`), source PDF p. 10, eTable 4, **Sex [n (%)]**, **Period 3 - Augmented Protein (4 units, n = 551)** column.
- **Source values:** Male `359 (65.2)`; Female `190 (34.5)`; column header `n = 551`.
- **Calculation:** `359 + 190 = 549`, which is `2` fewer than the displayed denominator of `551`. The displayed percentages likewise total `65.2 + 34.5 = 99.7%`, leaving `0.3%` unaccounted for.
- **Reasoning:** The Sex section displays only Male and Female and provides no missing/other-sex row or footnote for this column. Thus the visible sex-category counts do not reconcile to its stated group total. As a corroborating table relationship, summing the four augmented-period sex counts gives Male `303 + 187 + 359 + 220 = 1069` and Female `177 + 111 + 190 + 132 = 610` (combined `1679`), whereas Main article Table 1 reports `1070` male and `611` female of `1681` augmented participants.
- **Verification instruction:** Recheck the source table's Period 3 augmented-sex data and the period aggregation. Correct the displayed count(s), or explicitly disclose a missing/other category if intended.

## Tested checks that passed

- **Main article Table 1 (p. 5):** Sex, ICU-admission reason, diagnosis category, and ICU-source counts each sum to their respective treatment denominator (`1681` augmented; `1716` usual); displayed percentages are consistent with rounding.
- **Main article Table 2 (p. 7):** Discharge-destination rows total `1681` and `1716`; all visible binary-outcome percentages agree with their stated denominators. The sensitivity-analysis exclusions reconcile to their stated totals (`144 + 90 = 234`; `17 + 10 = 27`).
- **Supplement eTable 3 (p. 9):** Site and region counts total the two sequence denominators (`2044`, `1353`), and `2044 + 1353 = 3397`.
- **Supplement eTable 4 (pp. 10-12), other rows:** Period-by-treatment denominators total `1681` augmented and `1716` usual. ICU-admission type, diagnosis, source, treatment-goal, ventilation, vasopressor, kidney-replacement, and diabetes counts reconcile within columns and aggregate to the corresponding Main article Table 1 counts where the same measure is reported.
- **Supplement eTables 5-7 (pp. 13-15):** displayed treatment denominators and day-specific observation counts are internally plausible; parenteral-nutrition and protein-supplement percentages reproduce from their shown fractions. eTable 6's ideal-body-weight availability (`1681 - 369 = 1312`; `1716 - 410 = 1306`) matches its visible missing counts and the corresponding main-table footnote.
- **Supplement eTable 8 (p. 16):** category participant counts and event counts sum exactly to the total deviations for both groups (participants `151`/`95`; events `158`/`99`).
- **Supplement eTable 9 (p. 17):** all audit-category rows total each audit-period column and the overall `568` episodes; shown percentages are rounded consistently.
- **Supplement eTable 10 (p. 18):** every ICU-discharge-destination column sums to its displayed period/treatment denominator. Period totals reconcile to Main article Table 2 for day-90 survival (`1221`, `1269`), tracheostomy (`134`, `121`), new kidney replacement therapy (`122`, `127`), and post-index hospital readmission (`161`, `172`).
- **Supplement eTables 12-13 (pp. 20-21):** adverse-event and serious-adverse-event period cells sum to the treatment-group totals (`3` vs `1` AEs; `1` vs `1` SAEs).
- **Supplement eTable 14 (p. 22):** each displayed readmission-frequency distribution totals its treatment denominator. The Main article Table 2 `161`/`172` hospital-readmission values match eTable 14's post-index hospital readmission rows rather than its broader combined ICU-and-hospital distribution.

## Disposition

One document-verifiable candidate was identified. No additional local arithmetic candidates were retained.
