# Candidate ledger — Workflow 1.5.1

## Registration scope and merge record

This ledger consolidates only the completed new checker artifacts `numeric_consistency.md`, `cross_source_consistency.md`, and `statistical_pass_1.md`. A record was merged before stable-ID assignment only where it concerned the same printed value(s), comparator, and reconciliation rule.

- **Stable candidates:** 6 (C001–C006).
- **Merged duplicate checker records:** 2: `NC01` + `XC01` → C001; `NC02` + `XC04` → C002.
- **Distinct cross-source records retained separately:** `XC02` → C003 and `XC03` → C004, because they concern different rows/summary-statistic wording.
- **Statistical pass-1 local candidate records:** none.

## C001 — Invasive-ventilation descriptive summary is labeled mean (SD) but displays two endpoints

- **Category:** Measure, label, or scale inconsistency.
- **Checker provenance:** numeric `NC01`; cross-source `XC01`.
- **Exact source evidence:** [Main article, PDF p7, Table 2](../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7), row `Duration of invasive ventilation, mean (SD), h`, prints augmented protein `84.0 (35.0 to 178.9)` and usual protein `78.0 (33.2 to 161.0)`. The row’s separately reported model effect is `Mean difference, 6.8 (−3.0 to 16.5)` hours. The abstract [p1](../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1) also reports the mean-difference effect; Results Supplement [eTable 10, p18](../../joi250040supp3_prod_1753124024.38098.pdf#page=18) presents period-specific ventilation descriptives as a central value plus two bounds (for example, `72.0 (32.0, 148.0)`).
- **Reported versus comparator:** The Table 2 descriptive-row label is `mean (SD)`; its two group displays each contain two ordered endpoints joined by `to`. An SD presentation has one dispersion value, while the companion descriptive format contains a central value and two bounds.
- **Reproducible rule/calculation:** Test the printed form against its label. `35.0 < 178.9` and `33.2 < 161.0`; therefore each parenthesis is a two-endpoint interval/range-form display, not a single SD. No rounding tolerance applies: this is a categorical label-versus-display comparison. The model-based mean-difference effect does not itself convert the descriptive two-endpoint display into `mean (SD)`.
- **Direct observation versus inference:** The label, all values, and the separate mean-difference effect are direct observations. The inference is that at least one printed element—the descriptive label or its two-endpoint format—does not express the intended summary. The package does not identify whether the endpoints are IQR, range, or another interval.
- **Source-grounded alternatives:** A production error may have inserted `to` where one SD was intended; conversely, the label may have been copied from another row while the displayed values are a median-plus-interval summary. The supplied pages do not distinguish these alternatives.
- **Quality-control relevance:** The discrepancy can cause a data extractor to record an interval as an SD or misidentify the descriptive statistic for a duration outcome.
- **Human question:** What descriptive statistic and dispersion/range are `84.0 (35.0 to 178.9)` and `78.0 (33.2 to 161.0)` intended to represent, and should the Table 2 label or displayed format be revised?
- **Status:** Pending Human Adjudication.

## C002 — eTable 10 uses a comma in one one-decimal survival percentage

- **Category:** Measure, label, or scale inconsistency.
- **Checker provenance:** numeric `NC02`; cross-source `XC04`.
- **Exact source evidence:** [Results Supplement, PDF p18, eTable 10](../../joi250040supp3_prod_1753124024.38098.pdf#page=18), `Alive at day 90 [n (%)]`, `Period 2 – Usual Protein (4 units, n = 530)`, prints `383 (72, 3%)`. In the same matched row, neighboring cells use point decimals, including `323 (67.3%)`, `258 (77.0%)`, `229 (76.8%)`, and `408 (74.0%)`.
- **Reported versus comparator:** The cell reports `72, 3%`; the row’s prevailing English-table decimal convention is `72.3%`-style point notation, and its own count/denominator supports one-decimal 72.3%.
- **Reproducible rule/calculation:** `383 / 530 × 100 = 72.2641509…%`. To one decimal, this is `72.3%`; with conventional half-unit rounding, values in `[72.25%, 72.35%)` round to 72.3%. The direct issue is the comma in a point-decimal row, not a count/denominator mismatch.
- **Direct observation versus inference:** The printed comma, count, denominator, and surrounding point-decimal cells are direct observations. The likely intended string `72.3%` is an inference from arithmetic and the table’s own notation.
- **Source-grounded alternatives:** A comma may function as a decimal separator in some locales and thus retain the numeric meaning. Its isolated use inside this English point-decimal table still leaves a rendering inconsistency.
- **Quality-control relevance:** The punctuation can impair automated or manual extraction of a period-specific day-90 survival percentage without implying a changed trial conclusion.
- **Human question:** Should the Period 2 usual-protein cell be standardized to `383 (72.3%)`?
- **Status:** Pending Human Adjudication.

## C003 — Bayesian quantile row is labeled mean (SD) despite its associated median estimand and two-endpoint group displays

- **Category:** Measure, label, or scale inconsistency.
- **Checker provenance:** cross-source `XC02`.
- **Exact source evidence:** [Main article, PDF p7, Table 2](../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7) labels the Bayesian row `No. of days free of the index hospital and alive at day 90 (bayesian quantile mixed model), mean (SD)`, gives `62.0 (0 to 77)` versus `64.0 (0 to 77)`, and reports `Median difference, −1.50 (−3.86 to 0.90)`. Results Supplement [p5](../../joi250040supp3_prod_1753124024.38098.pdf#page=5) specifies that the Bayesian quantile model reports a difference in medians and a 95% credible interval; [eFigure 6, p27](../../joi250040supp3_prod_1753124024.38098.pdf#page=27) repeats `−1.50` with 95% CrI `−3.86 to 0.90`.
- **Reported versus comparator:** The Table 2 group-summary label says `mean (SD)`, whereas its associated effect and matched final-method/result locations identify a median-based Bayesian quantile estimand. The listed group parentheses have two ordered endpoints rather than one SD.
- **Reproducible rule/calculation:** For this matched outcome, population, contrast, and model, compare the Table 2 label with the Table 2 effect label and the supplement’s explicit method statement. `0 < 77` in each group display establishes a two-bound parenthesis. The directly printed estimand is `Median difference`; no supplied statement says that Table 2 intentionally presents separate means/SDs for this Bayesian row.
- **Direct observation versus inference:** The labels, group values, median effect, credible interval, and supplementary method text are direct observations. The inference is that the `mean (SD)` label may not identify the intended group summary; the package does not establish the production source of the mismatch.
- **Source-grounded alternatives:** The label may have been copied from the preceding linear mixed-model row. Alternatively, authors may have intentionally displayed separately calculated means/SDs alongside a median estimand, but the two-endpoint display and absence of a statement of that convention leave this unresolved.
- **Quality-control relevance:** The label may lead downstream extractors to misclassify both the descriptive summary and the analysis-scale context for the primary outcome.
- **Human question:** Were the Bayesian-row group values intended as median (IQR) values, and should `mean (SD)` be replaced with the descriptive label actually intended?
- **Status:** Pending Human Adjudication.

## C004 — Discussion describes the matched day-10 urea summaries as means while Results reports medians (IQR)

- **Category:** Cross-document numeric inconsistency.
- **Checker provenance:** cross-source `XC03`.
- **Exact source evidence:** Main article [Results, PDF p5, Biochemical Outcomes](../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5) calls the day-10 blood-urea values *median (IQR)* and prints augmented protein `13.0 (8.2-18.8)` versus usual protein `10.6 (7.1-15.4)` mmol/L. Main article [Discussion, PDF p8](../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=8) says that `mean urea concentrations at day 10 were higher in the augmented protein group`.
- **Reported versus comparator:** The same analyte, time point, groups, direction, and mmol/L comparison is called a median (IQR) result in Results but a mean result in Discussion. No matched day-10 mean values are printed in Results.
- **Reproducible rule/calculation:** Match population (trial groups), analyte (urea), time (day 10), and comparison direction, then compare the stated summary-statistic labels. This is a label identity rule, not an attempt to calculate a mean from medians/IQRs; no rounding tolerance is applicable.
- **Direct observation versus inference:** The Results’ median label and values and the Discussion’s `mean` wording are direct observations. The inference is that one location may use an inconsistent summary-statistic term. Both locations agree directionally that the augmented group is higher.
- **Source-grounded alternatives:** `Mean` may be nontechnical prose, a copy-editing substitution, or a reference to unprinted group means. The supplied paper does not print a distinct matched day-10 mean analysis that resolves the wording.
- **Quality-control relevance:** A reader or evidence extractor may incorrectly report the study’s biochemical summary statistic, even though the stated direction remains the same.
- **Human question:** Does the Discussion sentence refer to the reported median day-10 urea comparison and, if so, should `mean` be changed to `median`, or should a distinct day-10 mean analysis be identified?
- **Status:** Pending Human Adjudication.

## Noncandidate reconciliation notes

- **RRT/renal-failure interaction seed:** The new numeric and cross-source checkers initially retained a locator-derived inequality question. Direct visual inspection documented in both checkers shows Results Supplement [eFigure 7, p28](../../joi250040supp3_prod_1753124024.38098.pdf#page=28) prints `p<0.001`, matching [ICEMAN, p31](../../joi250040supp3_prod_1753124024.38098.pdf#page=31), `P<0.001`. There is no source-page contradiction to register.
- **Coherent display-zero rule:** None of the three checkers identified a `P = 0`, `p = 0.000`, or equivalent display-zero-only record. No stable ID is assigned for display precision.
- **Prospective versus final context:** Protocol, SAP, PRO-SCAN, and external-feasibility planning/materials did not supply a same-population, same-time, same-estimand final-result comparator for a stable candidate; their nonidentical planned values or methods are not registered.

## Ledger counts

- **Stable ID set:** C001, C002, C003, C004, C005, C006 (6).
- **All candidate records:** Pending Human Adjudication.

## Appended after statistical pass 2

Pass 2 supplied two `NEW_CANDIDATE_FOR_APPEND` records. Each is distinct from C001–C004 and from the other append: they concern a different eTable 10 outcome row, different printed values, and a distinct within-row percent-sign comparator/rule. Neither is merged with C002, which concerns the comma decimal separator in the alive-at-day-90 row.

## C005 — eTable 10 tracheostomy row switches percent-sign notation across period cells

- **Category:** Measure, label, or scale inconsistency.
- **Checker provenance:** statistical pass 2 `NEW_CANDIDATE_FOR_APPEND` (tracheostomy percent-sign notation).
- **Exact source evidence:** [Results Supplement, PDF p18, eTable 10](../../joi250040supp3_prod_1753124024.38098.pdf#page=18), row `Tracheostomy in ICU [n (%)]`. The first four period/treatment cells print `27 (5.6)`, `36 (10.7)`, `29 (9.7)`, and `24 (4.5)` without percent signs. The next four cells in the same row print `35 (6.4%)`, `38 (10.3%)`, `43 (12.2%)`, and `23 (4.8%)` with percent signs.
- **Reported versus comparator:** All eight entries are percentage displays within the same `n (%)` row, but the first four omit `%` while the next four include it.
- **Reproducible rule/calculation:** Verify each unsigned cell against its printed eTable column denominator: `27/480 × 100 = 5.625% → 5.6%`; `36/335 × 100 = 10.746...% → 10.7%`; `29/298 × 100 = 9.732...% → 9.7%`; `24/530 × 100 = 4.528...% → 4.5%`. The arithmetic is compatible at one decimal (half-unit rounding tolerance 0.05 percentage points); the observable rule failure is the inconsistent percent-sign notation for matched percentage cells.
- **Direct observation versus inference:** The row header and first-four/next-four punctuation forms are direct observations. The inference is that a single notation convention was likely intended; arithmetic establishes that the unsigned values are percentages, not bare counts.
- **Source-grounded alternatives:** The `n (%)` header can make the omitted signs understandable, but it does not account for the unexplained within-row switch to explicitly signed values.
- **Quality-control relevance:** Mixed notation may cause an extractor to misread or inconsistently parse period-specific tracheostomy percentages.
- **Human question:** Should all eight tracheostomy percentages in this eTable 10 row be rendered with the same percent-sign convention?
- **Status:** Pending Human Adjudication.

## C006 — eTable 10 new-KRT row switches percent-sign notation across period cells

- **Category:** Measure, label, or scale inconsistency.
- **Checker provenance:** statistical pass 2 `NEW_CANDIDATE_FOR_APPEND` (new-KRT percent-sign notation).
- **Exact source evidence:** [Results Supplement, PDF p18, eTable 10](../../joi250040supp3_prod_1753124024.38098.pdf#page=18), row `New kidney replacement therapy commenced during index ICU admission after commencing trial enteral nutrition [n (%)]`. The first four period/treatment cells print `33 (6.9)`, `26 (7.8)`, `22 (7.4)`, and `35 (6.6)` without percent signs. The next four cells print `38 (6.9%)`, `33 (9.0%)`, `29 (8.2%)`, and `33 (6.8%)` with percent signs.
- **Reported versus comparator:** All eight entries are percentage displays in a single `n (%)` row, but `%` is absent from the first four and present in the final four.
- **Reproducible rule/calculation:** Check the four unsigned cells using their printed column denominators: `33/480 × 100 = 6.875% → 6.9%`; `26/335 × 100 = 7.761...% → 7.8%`; `22/298 × 100 = 7.383...% → 7.4%`; `35/530 × 100 = 6.604...% → 6.6%`. All reconcile at one decimal (half-unit rounding tolerance 0.05 percentage points). The observed issue is notation consistency, not a rate/count discrepancy.
- **Direct observation versus inference:** The row header and distinct punctuation forms are direct observations. The inference is that the first-four values were intended as percentages despite their missing signs, supported by their count/denominator calculations.
- **Source-grounded alternatives:** The shared row header can make the unsigned values intelligible, but it does not explain why otherwise matched cells switch to explicit percent signs halfway through the row.
- **Quality-control relevance:** The within-row notation change creates a risk of inconsistent manual or automated extraction of period-specific KRT percentages.
- **Human question:** Should all eight new-KRT percentages in this eTable 10 row be rendered with the same percent-sign convention?
- **Status:** Pending Human Adjudication.

## Updated ledger counts after pass 2

- **Stable ID set:** C001, C002, C003, C004, C005, C006 (6).
- **Pass-2 append count:** 2 (C005–C006); no prior stable record was merged, altered, or renumbered.
- **All candidate records:** Pending Human Adjudication.
