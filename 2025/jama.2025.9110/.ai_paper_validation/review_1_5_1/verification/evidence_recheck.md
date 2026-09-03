# Evidence Recheck — Workflow 1.5.1

## Scope and method

This artifact rechecks every stable candidate ID in `candidate_ledger.md` (C001–C006). Each cited location was inspected in the supplied direct-source PDF. Native PDF text was used for location and transcription, and rendered source pages were inspected where layout or punctuation was material. Reusable derivatives were not treated as final authority. No candidate is adjudicated here.

## C001 — Invasive-ventilation descriptive summary is labeled mean (SD) but displays two endpoints

- **Status:** Pending Human Adjudication.
- **Location found:** Yes. [Main article, Table 2, PDF p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7), secondary-outcomes row `Duration of invasive ventilation, mean (SD), h`; supporting [abstract, PDF p1](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1); and [Results Supplement, eTable 10, PDF p18](../../../joi250040supp3_prod_1753124024.38098.pdf#page=18), row `Hours of invasive mechanical ventilation in ICU`.
- **Source value/text matched:** Yes. Table 2 visibly prints augmented protein `84.0 (35.0 to 178.9)` and usual protein `78.0 (33.2 to 161.0)` under the label `mean (SD)`. It separately prints `Mean difference, 6.8 (−3.0 to 16.5)`. The abstract prints the same mean-difference effect and confidence interval.
- **Comparator matched:** Yes. eTable 10 visibly presents period-specific ventilation summaries as a central value followed by two comma-separated bounds, including `72.0 (32.0, 148.0)`, and states at the foot of the page that data are presented as `median (IQR) or n (%)`.
- **Consistency rule applicable:** Yes. A `mean (SD)` descriptive display contains one mean and one SD per group. A parenthesis containing two ordered endpoints is not, as printed, a single SD.
- **Calculation or logical comparison reproduced:** Yes. The augmented display contains two distinct ordered values, `35.0 < 178.9`; the usual-protein display likewise contains `33.2 < 161.0`. Thus the printed form does not conform to the printed `mean (SD)` label. The separately reported model-based mean difference does not define those descriptive endpoints.
- **Necessary inputs available:** The printed label, both group displays, effect label/value, and matched supplementary descriptive convention are available. The supplied sources do not define what `35.0 to 178.9` and `33.2 to 161.0` specifically represent in Table 2, and do not state whether the intended group summary is median (IQR), mean with another interval, range, or another statistic.
- **Source-grounded alternative interpretation:** The Table 2 label could be a production/copy error while the values are intended as median and IQR, consistent with eTable 10. Alternatively, `to` or one endpoint could be a production error and a mean/SD summary may have been intended. The supplied sources do not distinguish these possibilities.
- **Direct observation versus inferred explanation:** Direct observations are the `mean (SD)` label, the two-endpoint group displays, the mean-difference effect, and eTable 10's median/IQR convention. The possible production mechanisms and the identity of the intended descriptive statistic are inferred explanations.
- **Exact remaining human question:** What descriptive statistic and interval/dispersion do `84.0 (35.0 to 178.9)` and `78.0 (33.2 to 161.0)` represent, and which printed element—the `mean (SD)` label or the displayed values/format—should express that intended statistic?

## C002 — eTable 10 uses a comma in one one-decimal survival percentage

- **Status:** Pending Human Adjudication.
- **Location found:** Yes. [Results Supplement, eTable 10, PDF p18](../../../joi250040supp3_prod_1753124024.38098.pdf#page=18), row `Alive at day 90 [n (%)]`, column `Period 2 – Usual Protein (4 units, n = 530)`.
- **Source value/text matched:** Yes. Direct page inspection visibly confirms `383 (72, 3%)`, including the comma and space between `72` and `3`.
- **Comparator matched:** Yes. The same row visibly prints point-decimal percentages in all seven neighboring cells: `67.3%`, `77.0%`, `76.8%`, `74.0%`, `73.4%`, `74.1%`, and `74.1%`. The target column header supplies `n = 530`.
- **Consistency rule applicable:** Yes. A table using point-decimal notation should represent a one-decimal percentage consistently; the printed count divided by the printed denominator provides an independent arithmetic comparator.
- **Calculation or logical comparison reproduced:** Yes. `383 / 530 × 100 = 72.2641509…%`, which rounds to `72.3%` at one decimal. This matches the numeric reading of `72,3%` under comma-decimal convention but not the table's otherwise uniform point-decimal typography.
- **Necessary inputs available:** The count, denominator, target punctuation, comparison cells, and stated `n (%)` format are available. No numerical input is missing. The source does not state that this isolated cell intentionally switches decimal conventions.
- **Source-grounded alternative interpretation:** The comma can serve as a decimal separator and therefore need not alter the numerical meaning; it may be a localized punctuation or typesetting artifact. Its isolated use within this English table remains a visible notation inconsistency.
- **Direct observation versus inferred explanation:** Direct observations are the printed `383 (72, 3%)`, the denominator `530`, and neighboring point-decimal cells. The reading `72.3%` and the proposed typesetting/localization mechanism are inferences supported by arithmetic and context.
- **Exact remaining human question:** Is the visibly printed comma-and-space intentional, or should the cell use the table's point-decimal convention to display the percentage corresponding to `383/530`?

## C003 — Bayesian quantile row is labeled mean (SD) despite its associated median estimand and two-endpoint group displays

- **Status:** Pending Human Adjudication.
- **Location found:** Yes. [Main article, Table 2, PDF p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7), Bayesian quantile mixed-model row; [Results Supplement methods, PDF p5](../../../joi250040supp3_prod_1753124024.38098.pdf#page=5), `Secondary analyses`; and [Results Supplement, eFigure 6, PDF p27](../../../joi250040supp3_prod_1753124024.38098.pdf#page=27).
- **Source value/text matched:** Yes. Table 2 visibly labels the Bayesian row `mean (SD)`, prints augmented protein `62.0 (0 to 77)` and usual protein `64.0 (0 to 77)`, and prints `Median difference, −1.50 (−3.86 to 0.90)`.
- **Comparator matched:** Yes. Supplement p5 states that the Bayesian quantile mixed-effects model coefficient is a `difference in medians` and that the 95% credible interval uses the posterior distribution's 2.5th and 97.5th percentiles. eFigure 6 visibly prints `Median Difference: −1.50 (95% CrI: −3.86, 0.90)`.
- **Consistency rule applicable:** Yes. For the same outcome, groups, and Bayesian quantile analysis, a group-summary label should accurately identify its descriptive statistic and should not conflict without explanation with the row's median estimand and two-bound display.
- **Calculation or logical comparison reproduced:** Yes. Both group parentheses contain two ordered endpoints (`0 < 77`), not one SD. The row's effect and both supplementary locations independently identify a median difference. No numerical transformation is needed or warranted.
- **Necessary inputs available:** The row label, group values, effect label/value, model description, and plotted effect are available. The supplied sources do not explicitly define the Table 2 group summaries for this Bayesian row or state that independently calculated means/SDs were intentionally paired with a median-based model.
- **Source-grounded alternative interpretation:** The `mean (SD)` text may have carried over from the immediately preceding linear mixed-model row. Alternatively, independently calculated descriptive statistics could intentionally accompany a median estimand, but the two-bound group displays and absence of an explanatory statement do not establish that convention.
- **Direct observation versus inferred explanation:** Direct observations are the labels and numbers on Table 2, the supplement's difference-in-medians method statement, and eFigure 6's median-difference label/value. Copy-forward and intentional mixed-summary explanations are inferences.
- **Exact remaining human question:** What statistic and interval do `62.0 (0 to 77)` and `64.0 (0 to 77)` represent in the Bayesian row, and was `mean (SD)` intended there or carried over from the linear mixed-model row?

## C004 — Discussion describes the matched day-10 urea summaries as means while Results reports medians (IQR)

- **Status:** Pending Human Adjudication.
- **Location found:** Yes. [Main article, Results, PDF p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5), `Biochemical Outcomes`, and [Main article, Discussion, PDF p8](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=8).
- **Source value/text matched:** Yes. Results visibly states: `By day 10, median (IQR) blood urea concentration was 13.0 (8.2-18.8) mmol/L` in the augmented-protein group and `10.6 (7.1-15.4) mmol/L` in the usual-protein group.
- **Comparator matched:** Yes. Discussion visibly states that `mean urea concentrations at day 10 were higher in the augmented protein group`. The analyte, day, group comparison, units context, and direction match the Results passage.
- **Consistency rule applicable:** Yes. A matched quantitative comparison should use the same summary-statistic term unless a distinct analysis is identified. Mean and median are not interchangeable labels.
- **Calculation or logical comparison reproduced:** Yes. Matching analyte (`urea`), time (`day 10`), groups, and direction ties the passages together. Results labels the printed values `median (IQR)`; Discussion calls the matched concentrations `mean`. This is a terminology comparison, not a calculation of a mean from median/IQR values.
- **Necessary inputs available:** The Results values and summary label and the Discussion wording are available. The supplied article does not print distinct day-10 mean urea values, define an additional mean-based day-10 analysis, or provide participant-level values from which a mean could be reproduced.
- **Source-grounded alternative interpretation:** `Mean` may be used informally in the Discussion to mean average/typical concentration, may be a copy-editing substitution, or may refer to an unprinted mean analysis. The supplied source does not identify which interpretation applies.
- **Direct observation versus inferred explanation:** Direct observations are the Results' median/IQR label and values and the Discussion's `mean` wording. Any claim about informal usage, copy editing, or an unprinted analysis is inferred.
- **Exact remaining human question:** Does the Discussion sentence refer to the printed day-10 median (IQR) comparison, or to a distinct unprinted mean analysis; if the latter, where are the mean values and their definition reported?

## C005 — eTable 10 tracheostomy row switches percent-sign notation across period cells

- **Status:** Pending Human Adjudication.
- **Location found:** Yes. [Results Supplement, eTable 10, PDF p18](../../../joi250040supp3_prod_1753124024.38098.pdf#page=18), row `Tracheostomy in ICU [n (%)]`, across the eight period-by-treatment columns.
- **Source value/text matched:** Yes. In column order, the first four cells visibly print `27 (5.6)`, `36 (10.7)`, `29 (9.7)`, and `24 (4.5)` without percent signs. The final four visibly print `35 (6.4%)`, `38 (10.3%)`, `43 (12.2%)`, and `23 (4.8%)` with percent signs.
- **Comparator matched:** Yes. The eight column headers respectively print denominators `n = 480`, `n = 335`, `n = 298`, `n = 530`, `n = 551`, `n = 368`, `n = 352`, and `n = 483`. The row header specifies `[n (%)]`; therefore the parenthetical entries occupy the same percentage field despite their different sign patterns.
- **Consistency rule applicable:** Yes. Matched cells in one `n (%)` row should use one percent-sign convention. Count/denominator arithmetic independently tests whether every parenthetical value is a percentage rather than another measure.
- **Calculation or logical comparison reproduced:** Yes. In column order: `27/480 × 100 = 5.625% → 5.6%`; `36/335 × 100 = 10.746…% → 10.7%`; `29/298 × 100 = 9.732…% → 9.7%`; `24/530 × 100 = 4.528…% → 4.5%`; `35/551 × 100 = 6.352…% → 6.4%`; `38/368 × 100 = 10.326…% → 10.3%`; `43/352 × 100 = 12.216…% → 12.2%`; and `23/483 × 100 = 4.762…% → 4.8%`. Each printed number reconciles at one decimal. The observed mismatch is the transition from four unsigned percentage values to four signed percentage values, not a count/denominator discrepancy.
- **Necessary inputs available:** All eight counts, denominators, one-decimal values, percent-sign patterns, and the row's `[n (%)]` definition are printed. No numerical input is missing. The source does not state whether omission of `%` in the first four cells or inclusion in the last four was the intended production convention.
- **Source-grounded alternative interpretation:** The shared `[n (%)]` row header makes every unsigned parenthetical value understandable as a percentage, so repeated percent signs are not necessary for numeric interpretation. That convention does not explain why the final four matched cells explicitly include `%` while the first four do not.
- **Direct observation versus inferred explanation:** Direct observations are the row label, all eight printed cells, the eight denominators, and the first-four/last-four percent-sign split. That the unsigned values are percentages is supported directly by the row header and reproduced arithmetic. A typesetting, template, or production-boundary explanation for the switch is inferred and is not stated in the source.
- **Exact remaining human question:** Was the within-row switch in percent-sign usage intentional, and which single convention should apply to all eight tracheostomy `n (%)` cells?

## C006 — eTable 10 new-KRT row switches percent-sign notation across period cells

- **Status:** Pending Human Adjudication.
- **Location found:** Yes. [Results Supplement, eTable 10, PDF p18](../../../joi250040supp3_prod_1753124024.38098.pdf#page=18), row `New kidney replacement therapy commenced during index ICU admission after commencing trial enteral nutrition [n (%)]`, across the eight period-by-treatment columns.
- **Source value/text matched:** Yes. In column order, the first four cells visibly print `33 (6.9)`, `26 (7.8)`, `22 (7.4)`, and `35 (6.6)` without percent signs. The final four visibly print `38 (6.9%)`, `33 (9.0%)`, `29 (8.2%)`, and `33 (6.8%)` with percent signs.
- **Comparator matched:** Yes. The eight column headers respectively print denominators `n = 480`, `n = 335`, `n = 298`, `n = 530`, `n = 551`, `n = 368`, `n = 352`, and `n = 483`. The shared row header specifies `[n (%)]`, identifying each parenthetical value as the same percentage field.
- **Consistency rule applicable:** Yes. All cells in one `n (%)` row should follow one percent-sign convention. Count/denominator arithmetic can establish whether the unsigned entries are percentages and whether the issue is notation rather than numerical inconsistency.
- **Calculation or logical comparison reproduced:** Yes. In column order: `33/480 × 100 = 6.875% → 6.9%`; `26/335 × 100 = 7.761…% → 7.8%`; `22/298 × 100 = 7.383…% → 7.4%`; `35/530 × 100 = 6.604…% → 6.6%`; `38/551 × 100 = 6.897…% → 6.9%`; `33/368 × 100 = 8.967…% → 9.0%`; `29/352 × 100 = 8.239…% → 8.2%`; and `33/483 × 100 = 6.832…% → 6.8%`. All eight reconcile at one decimal. The observable mismatch is the first-four/last-four percent-sign switch, not a rate/count discrepancy.
- **Necessary inputs available:** All eight counts, denominators, one-decimal values, percent-sign patterns, and the `[n (%)]` row definition are available. No numerical input is missing. The source supplies no statement identifying which percent-sign convention was intended.
- **Source-grounded alternative interpretation:** Because `[n (%)]` appears in the row label, the first four unsigned values remain interpretable as percentages. That compact convention does not explain the explicit percent signs in only the final four otherwise matched cells.
- **Direct observation versus inferred explanation:** Direct observations are the complete row text, all eight cells and denominators, and the sign-pattern split. The percentage interpretation of unsigned values is source-grounded and arithmetically reproduced. Any attribution to a typesetting, template, or production transition is inferred.
- **Exact remaining human question:** Was the within-row percent-sign switch intentional, and which single convention should apply to all eight new-KRT `n (%)` cells?

## Recheck completion

- **Stable IDs covered:** C001, C002, C003, C004, C005, C006.
- **Direct-source location coverage:** All locations cited for these six IDs were found and inspected.
- **Unresolved source limitations:** C001 lacks a definition of the two descriptive endpoints and the intended summary statistic; C003 lacks an explicit definition of the Bayesian row's group summaries; C004 lacks any printed matched day-10 mean analysis. C002's punctuation is visually clear, while authorial intent for the isolated comma-and-space is not stated. C005 and C006 have complete numerical inputs, but the intended percent-sign convention is not stated.
- **Disposition:** Every ID remains Pending Human Adjudication.
