# Quantitative Quality-Control Consistency Review

## Pending Human Adjudication

All 12 candidate consistency issues in this report are **Pending Human Adjudication**. They are source-grounded quantitative reporting quality-control observations, not findings about study validity, author intent, or the paper's conclusions.

## Executive Quality-Control Summary

Complete local review of seven supplied PDFs (159 stable PDF-page units) registered 12 distinct candidates (`C001`-`C012`). The candidates concern cross-location values, totals, statistical interval display, and measure or label consistency. Small preventable reporting defects can matter if later evidence users copy them; this report does not assert that copying, conclusion change, or harm occurred.

## Package and Reused-Evidence Provenance

The package contains the main article and six supplied supplements: `jama_engelter_2025_oi_250066_1761597796.45511.pdf`, `joi250066supp1_prod_1761597796.4601.pdf` through `joi250066supp6_prod_1761597796.4801.pdf`. Direct-source identity and the seven-source inventory are recorded in [source_inventory.md](review_1_5_1/source_inventory.md); before/after source and reused-asset integrity checks are recorded in [source_hashes_before.sha256](review_1_5_1/source_hashes_before.sha256) and [reused_artifact_hashes_before.sha256](review_1_5_1/reused_artifact_hashes_before.sha256). Reused extraction, OCR, layout text, table maps, and rendered pages were used as locators and transcription aids; exact supplied PDF pages remained the evidence authority.

## Scope, Complete Coverage, and Exclusions

All seven direct sources are complete in [source_coverage.md](review_1_5_1/source_coverage.md): 159 total units, 28 reusable-backed units, 131 fresh-required units, and 159 mapped units. [coverage_manifest.md](review_1_5_1/coverage_manifest.md) records disjoint completed scopes and one artifact path per row. The review covered quantitative reporting consistency only: arithmetic, totals, denominators, statistical displays, matched cross-document results, measures, labels, scales, and rate/count distinctions. It excluded external sources, raw data reconstruction, broad methodology review, clinical assessment, misconduct assessment, and any ranked-count or cap-based process.

## Quantitative and Statistical Relationship Coverage

The complete numeric inventory contains `N001`-`N033`; the inferential-statistical inventory contains `S001`-`S021`. Numeric and cross-source checks are recorded in [numeric_consistency.md](review_1_5_1/checkers/numeric_consistency.md) and [cross_source_consistency.md](review_1_5_1/checkers/cross_source_consistency.md). Both independent statistical passes cover every S relationship: [statistical_pass_1.md](review_1_5_1/checkers/statistical_pass_1.md) and [statistical_pass_2.md](review_1_5_1/checkers/statistical_pass_2.md). Coherent display-zero P values were not registered as candidates; no stable candidate in this report mentions a display-zero P value.

## Candidate Index

| ID | Candidate statement | Primary category | Status |
|---|---|---|---|
| C001 | Baseline index-stroke type counts differ across baseline tables | Cross-document numeric inconsistency | Pending Human Adjudication |
| C002 | Baseline NIHSS statistic and label do not reconcile across tables | Measure, label, or scale inconsistency | Pending Human Adjudication |
| C003 | Time from stroke onset to randomization differs across baseline tables | Cross-document numeric inconsistency | Pending Human Adjudication |
| C004 | Estimand 4 confidence-interval upper endpoint differs within eTable 2 | Statistical reporting inconsistency | Pending Human Adjudication |
| C005 | Levodopa PROMIS-29 descriptive mean differs between main text and eTable 4 | Cross-document numeric inconsistency | Pending Human Adjudication |
| C006 | PROMIS-10 descriptive means differ between main text and eTable 4 | Cross-document numeric inconsistency | Pending Human Adjudication |
| C007 | Placebo five-week FMA standard deviation differs from eTable 4 | Cross-document numeric inconsistency | Pending Human Adjudication |
| C008 | Placebo PRAI no-improvement numerator differs between main text and eTable 4 | Cross-document numeric inconsistency | Pending Human Adjudication |
| C009 | eTable 6 overall adverse-event total is one below arms and category sums | Denominator, proportion, or total inconsistency | Pending Human Adjudication |
| C010 | eFigure 4 switches locally from FMA to FMMA without qualification | Measure, label, or scale inconsistency | Pending Human Adjudication |
| C011 | Estimand 4 win ratio appears under an FMA mean-difference column heading | Measure, label, or scale inconsistency | Pending Human Adjudication |
| C012 | Estimand 4 is called an odds ratio in prose and a win ratio in the table | Measure, label, or scale inconsistency | Pending Human Adjudication |

## Candidate Evidence Cards

## C001 — Baseline index-stroke type counts differ across baseline tables

**Candidate statement:** The same randomized levodopa arm has different ischemic/hemorrhagic index-stroke counts in two baseline tables. **Pending Human Adjudication.**

**Category:** Cross-document numeric inconsistency

**Exact source locations:** DOC-001, [main article — PDF p. 4](<../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4>), Table 1; DOC-004, [Supplement 3 — PDF p. 10](<../joi250066supp3_prod_1761597796.4701.pdf#page=10>) and [PDF p. 11](<../joi250066supp3_prod_1761597796.4701.pdf#page=11>), eTable 1.

**Source evidence:** Main Table 1 prints levodopa `n=307`: ischemic `260 (84.7%)`, hemorrhagic `47 (15.3%)`. eTable 1 prints levodopa `n=307`: ischemic `263 (85.7%)`, hemorrhagic `44 (14.3%)`; placebo values match.

**Reported-versus-comparator:** Main `260/47` versus supplement `263/44` for the same named arm and categories.

**Reasoning procedure:** Compare matched arm, population label, and mutually exclusive category labels across the two tables.

**Calculation:** `260 + 47 = 307`; `263 + 44 = 307`; the category changes are `+3/-3` at an unchanged arm total.

**Alternative source-grounded interpretations:** An unstated recoding or data cut could explain the difference; neither table identifies one.

**Mechanical evidence recheck:** Both cited locations and printed values were found; the identity comparison reproduced. Group labels and totals are present; a recoding/data-version definition is missing. Direct observation is the different pairs, while a cause is inferred.

**Quality-control relevance:** A same-arm baseline-category mismatch requires source confirmation before use as a trial characteristic.

**Potential downstream evidence impact:** If confirmed, a data extractor or systematic review could copy an incorrect stroke-type count.

**Human verification steps:** Confirm the intended levodopa pair and whether a classification rule or data version differs.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Baseline NIHSS statistic and label do not reconcile across tables

**Candidate statement:** eTable 1 labels its NIHSS row as median [IQR] but prints a decimal-plus-one-parenthesized-value form that does not identify the same summary as the main table. **Pending Human Adjudication.**

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** DOC-001, [main article — PDF p. 4](<../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4>), Table 1, and [PDF p. 5](<../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5>), Results; DOC-004, [Supplement 3 — PDF p. 11](<../joi250066supp3_prod_1761597796.4701.pdf#page=11>), eTable 1.

**Source evidence:** Main values are median (IQR) `7 (5-11)` levodopa, `8 (5-10)` placebo, and overall `7 (5-10)`. eTable 1 labels `Median NIHSS at randomization [IQR]` yet prints `8.2 (3.9)`, `8.3 (3.8)`, and `8.2 (3.9)`.

**Reported-versus-comparator:** A labelled median/IQR row with two-endpoint main summaries versus one decimal and one parenthesized value in the supplement.

**Reasoning procedure:** Assess whether the declared statistic and displayed form supply reconcilable central and IQR summaries.

**Calculation:** Main summaries contain a central value and two IQR endpoints; each supplement summary has one central decimal and one parenthesized number, so mapping requires a missing definition.

**Alternative source-grounded interpretations:** The supplement values may be means (SDs) under a stale label, or may use an unstated one-number convention; neither interpretation is stated there.

**Mechanical evidence recheck:** Locations, labels, and values were found. The measure/label rule applies; the statistic represented by `8.2 (3.9)` and meaning of `(3.9)` are missing. Mean (SD) is an inference, not a source fact.

**Quality-control relevance:** The baseline-severity summary should have an unambiguous statistic and dispersion label.

**Potential downstream evidence impact:** If confirmed, baseline NIHSS could be extracted with the wrong statistic or dispersion measure.

**Human verification steps:** Identify the statistic and dispersion for each supplement value and confirm whether the label or values should change.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Time from stroke onset to randomization differs across baseline tables

**Candidate statement:** Same-named time-to-randomization summaries differ across tables; the supplement omits the unit needed to make the cross-source comparison unconditional. **Pending Human Adjudication.**

**Category:** Cross-document numeric inconsistency

**Exact source locations:** DOC-001, [main article — PDF p. 4](<../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4>), Table 1; DOC-004, [Supplement 3 — PDF p. 11](<../joi250066supp3_prod_1761597796.4701.pdf#page=11>), eTable 1.

**Source evidence:** Main prints `Time from stroke onset to randomization, median (IQR), d`: `3.0 (2.0-5.0)` for both arms. eTable 1 prints `7 [5,10]` overall, `8 [5,10]` placebo, and `7 [5-11]` levodopa without a visible unit.

**Reported-versus-comparator:** Main arm medians `3.0/3.0` versus supplement `8/7` for the same named variable.

**Reasoning procedure:** Compare wording and arms, conditioning any day-based identity claim on confirmation that the omitted supplement unit and derivation match.

**Calculation:** If the supplement values are days, levodopa differs by `7-3=4` days and placebo by `8-3=5` days; these are not rounding differences.

**Alternative source-grounded interpretations:** A different unstated unit, time origin, derivation, population, or data version may be used.

**Mechanical evidence recheck:** Locations and values were found. The comparison is conditionally applicable because the supplement unit, time origin, derivation, and population definition are absent. The values are observed; treating the supplement as days is inferred.

**Quality-control relevance:** Cross-source timing summaries need an explicit common unit and derivation before they can be treated as identical.

**Potential downstream evidence impact:** If confirmed under the same unit, a trial-timing value could be copied incorrectly into evidence extraction.

**Human verification steps:** Confirm the supplement unit, time origin, and intended arm-specific values.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Estimand 4 confidence-interval upper endpoint differs within eTable 2

**Candidate statement:** Two matched Estimand 4 displays in eTable 2 have different upper 95% CI endpoints. **Pending Human Adjudication.**

**Category:** Statistical reporting inconsistency

**Exact source locations:** DOC-004, [Supplement 3 — PDF p. 12](<../joi250066supp3_prod_1761597796.4701.pdf#page=12>), eTable 2 narrative; [PDF p. 13](<../joi250066supp3_prod_1761597796.4701.pdf#page=13>), Estimand 4 row.

**Source evidence:** Narrative: `1.06 (95% CI, 0.86 to 1.25)`. Matched full-analysis-set composite row: `1.06 [0.86-1.26]`.

**Reported-versus-comparator:** Identical point estimate/lower endpoint with upper endpoint `1.25` versus `1.26`.

**Reasoning procedure:** Match estimand number, population, composite endpoint, confidence level, and estimate, then compare the repeated interval endpoints.

**Calculation:** `1.06=1.06`, `0.86=0.86`, and `1.26-1.25=0.01`.

**Alternative source-grounded interpretations:** A rounding-boundary or one-hundredth transcription difference is possible; no unrounded output or separate calculation is supplied.

**Mechanical evidence recheck:** Both displays were found and reproduced. The repeated-result rule applies; unrounded upper-bound output and an explanation of any display difference are missing. Mechanism is inferred.

**Quality-control relevance:** A repeated statistical interval should have one traceable displayed endpoint.

**Potential downstream evidence impact:** If confirmed, an effect-precision endpoint could be copied inconsistently into a meta-analysis or evidence table.

**Human verification steps:** Confirm the intended upper endpoint using the analysis output and document any rounding rule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Levodopa PROMIS-29 descriptive mean differs between main text and eTable 4

**Candidate statement:** The main-text levodopa PROMIS-29 mean does not follow ordinary whole-number rounding of the matched eTable 4 mean. **Pending Human Adjudication.**

**Category:** Cross-document numeric inconsistency

**Exact source locations:** DOC-001, [main article — PDF p. 6](<../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6>), Secondary Outcomes; DOC-004, [Supplement 3 — PDF p. 15](<../joi250066supp3_prod_1761597796.4701.pdf#page=15>), eTable 4.

**Source evidence:** Main: levodopa `66 (14)`, placebo `65 (14)`. eTable: levodopa `64.74 (14.33)`, placebo `65.11 (13.79)`, effect `-0.37`.

**Reported-versus-comparator:** Main levodopa `66 (14)` versus detailed `64.74 (14.33)`.

**Reasoning procedure:** Check whether detailed same-outcome, same-arm descriptive values reproduce the narrative display under ordinary whole-number rounding.

**Calculation:** `64.74` rounds to `65`, not `66`; `64.74-65.11=-0.37`, matching the eTable effect.

**Alternative source-grounded interpretations:** An unstated scoring transformation, analysis set, or descriptive-versus-model summary could differ.

**Mechanical evidence recheck:** Pages and values were found; the rounding comparison reproduced. Scoring version, analysis population, and unrounded main-text inputs are unavailable. An explanation is inferred.

**Quality-control relevance:** Matched secondary-outcome descriptive values should identify a common scoring and analysis basis.

**Potential downstream evidence impact:** If confirmed, a PROMIS-29 mean could be copied incorrectly into a secondary-outcome extraction.

**Human verification steps:** Confirm the intended levodopa mean, score transformation, and analysis population.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — PROMIS-10 descriptive means differ between main text and eTable 4

**Candidate statement:** Both detailed PROMIS-10 means are near 30, whereas the main text prints 28 for both arms. **Pending Human Adjudication.**

**Category:** Cross-document numeric inconsistency

**Exact source locations:** DOC-001, [main article — PDF p. 6](<../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6>), Secondary Outcomes; DOC-004, [Supplement 3 — PDF p. 15](<../joi250066supp3_prod_1761597796.4701.pdf#page=15>), eTable 4.

**Source evidence:** Main prints `28 (6)` in both arms. eTable prints placebo `29.87 (5.74)` and levodopa `30.04 (5.73)`, with adjusted effect `0.18`.

**Reported-versus-comparator:** Main `28 (6)`/`28 (6)` versus eTable `29.87 (5.74)`/`30.04 (5.73)`.

**Reasoning procedure:** Compare matched instrument and arm summaries; keep the adjusted effect separate from the raw descriptive contrast.

**Calculation:** `29.87` and `30.04` each round to `30`, not `28`; `30.04-29.87=0.17`, while the labelled adjusted effect is `0.18`.

**Alternative source-grounded interpretations:** An unstated PROMIS-10 scoring version or analysis population may differ.

**Mechanical evidence recheck:** Both pages and values were found. The rounding comparison reproduced; scoring/version, analysis-population, and unrounded narrative inputs are missing. The alternative is not established.

**Quality-control relevance:** Instrument summaries should be traceable to the same score scale and population across locations.

**Potential downstream evidence impact:** If confirmed, a PROMIS-10 descriptive mean could be copied incorrectly into evidence extraction.

**Human verification steps:** Confirm the score transformation, population, and intended group means.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Placebo five-week FMA standard deviation differs from eTable 4

**Candidate statement:** The main placebo five-week FMA SD does not follow ordinary whole-number rounding of eTable 4. **Pending Human Adjudication.**

**Category:** Cross-document numeric inconsistency

**Exact source locations:** DOC-001, [main article — PDF p. 6](<../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6>), Secondary Outcomes; DOC-004, [Supplement 3 — PDF p. 15](<../joi250066supp3_prod_1761597796.4701.pdf#page=15>), eTable 4.

**Source evidence:** Main placebo mean (SD) is `56 (26)`; eTable placebo is `56.27 (25.20)`. Levodopa `57 (27)` aligns with `57.37 (26.70)`.

**Reported-versus-comparator:** Placebo SD `26` versus detailed `25.20`.

**Reasoning procedure:** Compare same-arm five-week FMA mean (SD) and reproduce ordinary whole-number rounding.

**Calculation:** `56.27` rounds to `56`; `25.20` rounds to `25`, not `26`; levodopa `57.37 (26.70)` rounds to `57 (27)`.

**Alternative source-grounded interpretations:** An unstated population, imputation summary, or SD convention could differ.

**Mechanical evidence recheck:** Cited values were found and rounding reproduced. Unrounded main inputs, population/imputation definition, and nonstandard rounding rule are missing. Causes are inferred.

**Quality-control relevance:** Descriptive dispersion values should remain traceable across matched results.

**Potential downstream evidence impact:** If confirmed, a placebo FMA SD could be copied incorrectly into descriptive-variance extraction.

**Human verification steps:** Confirm the intended placebo SD and common population/rounding convention.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Placebo PRAI no-improvement numerator differs between main text and eTable 4

**Candidate statement:** The placebo PRAI no-improvement numerator differs by one at the same printed denominator. **Pending Human Adjudication.**

**Category:** Cross-document numeric inconsistency

**Exact source locations:** DOC-001, [main article — PDF p. 6](<../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6>), Secondary Outcomes; DOC-004, [Supplement 3 — PDF p. 15](<../joi250066supp3_prod_1761597796.4701.pdf#page=15>), eTable 4.

**Source evidence:** Main placebo is `52/270 (19%)`; eTable placebo is `51 (18.89%) (n=270)`. Levodopa is `51/276` in both.

**Reported-versus-comparator:** Same placebo denominator `270` with numerator `52` versus `51`.

**Reasoning procedure:** Match arm, denominator, time point, and binary outcome wording; check each percentage against its own numerator.

**Calculation:** `51/270=18.888...%`, matching `18.89%`; `52/270=19.259...%`, compatible with `19%`. The printed numerator differs by one.

**Alternative source-grounded interpretations:** Different handling of `no improvement` and `no relevant improvement` could affect one record, but no distinct rule is supplied.

**Mechanical evidence recheck:** Values, denominator, and category labels were found; the percentage calculations reproduced. Record-level classifications and any response-category definition are missing. Recoding is inferred.

**Quality-control relevance:** A matched binary-outcome numerator should use a clearly defined response category.

**Potential downstream evidence impact:** If confirmed, a binary-outcome count could be copied incorrectly into an evidence table or meta-analysis input.

**Human verification steps:** Confirm the intended placebo numerator and whether identical PRAI response categories were used.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — eTable 6 overall adverse-event total is one below arms and category sums

**Candidate statement:** eTable 6 prints an overall adverse-event total of 145 although arm and exhaustive category totals are 146. **Pending Human Adjudication.**

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** DOC-001, [main article — PDF p. 6](<../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6>), Table 2 and narrative, and [PDF p. 7](<../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=7>); DOC-004, [Supplement 3 — PDF p. 17](<../joi250066supp3_prod_1761597796.4701.pdf#page=17>), eTable 6.

**Source evidence:** Main reports 146 events: 79 levodopa and 67 placebo. eTable header gives overall `n=145`, placebo `67`, levodopa `79`; its intensity, outcome, and relation rows also provide complete classifications.

**Reported-versus-comparator:** Header `145` versus arms and category sums `146`.

**Reasoning procedure:** Reconcile the overall event header against arm counts and each exhaustive classification in the same table.

**Calculation:** `67+79=146`; intensity `58+86+2=146`; outcome `1+29+116=146`; relation `2+66+23+2+39+14=146`.

**Alternative source-grounded interpretations:** One event might be subject to an unstated exclusion or duplicate-event rule, but no footnote supports a different overall set.

**Mechanical evidence recheck:** All cited totals were found and each reconciliation reproduced. An exclusion/duplicate-event rule is missing. The explanations are inferred, not observed.

**Quality-control relevance:** Event totals and classification totals should identify one consistent event set.

**Potential downstream evidence impact:** If confirmed, a safety-event total could be copied incorrectly into evidence extraction.

**Human verification steps:** Confirm whether the overall total should be 146 or document the rule that makes 145 intentional.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — eFigure 4 switches locally from FMA to FMMA without qualification

**Candidate statement:** eFigure 4 uses `FMA` in its title/legend and `FMMA` on its axis without a local qualification. **Pending Human Adjudication.**

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** DOC-004, [Supplement 3 — PDF p. 23](<../joi250066supp3_prod_1761597796.4701.pdf#page=23>), eFigure 4; DOC-003, [Supplement 2 — PDF p. 2](<../joi250066supp2_prod_1761597796.4701.pdf#page=2>), SAP objective; DOC-001, [main article — PDF p. 1](<../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1>), [PDF p. 3](<../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3>), and [PDF p. 6](<../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6>).

**Source evidence:** eFigure 4 title/legend use `FMA`; its axis reads `Adjusted Mean Difference (FMMA points)`. The SAP defines Fugl-Meyer Motor Assessment as `FMMA`.

**Reported-versus-comparator:** Within the same figure, `FMA` versus `FMMA` for the stated assessment.

**Reasoning procedure:** Compare the local figure terminology, then check supplied source definitions before characterizing the abbreviation switch.

**Calculation:** No numeric calculation applies; the reproduced comparison is the local unqualified abbreviation switch.

**Alternative source-grounded interpretations:** The SAP's explicit `FMMA` definition supports that `FMMA` may be an intentional synonym for the FMA used in the article; it is not evidence of a numeric error.

**Mechanical evidence recheck:** Direct source rendering confirmed the figure title `FMA Total Score` and axis `FMMA points`. The SAP definition was found. The observation is local terminology; an intentional synonym is source-grounded and unresolved.

**Quality-control relevance:** A figure should use one locally clear abbreviation or qualify synonymous abbreviations.

**Potential downstream evidence impact:** If confirmed as a presentation issue, an extractor could copy inconsistent outcome terminology; no numeric or conclusion impact is established.

**Human verification steps:** Confirm whether the switch is intentional and whether the figure should use one abbreviation or define both locally.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — Estimand 4 win ratio appears under an FMA mean-difference column heading

**Candidate statement:** Estimand 4's win ratio is displayed under a column headed as an FMA mean difference. **Pending Human Adjudication.**

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** DOC-004, [Supplement 3 — PDF p. 13](<../joi250066supp3_prod_1761597796.4701.pdf#page=13>), eTable 2 column heading and Estimand 4 row.

**Source evidence:** The heading reads `Estimated Effect of Levodopa: Mean Difference on FMA, [CI]`. Estimand 4 identifies a death-and-3-month-FMA composite summary as `win ratio [95% CI]` and prints `1.06 [0.86-1.26]`.

**Reported-versus-comparator:** A dimensionless win ratio row versus an FMA-point mean-difference heading.

**Reasoning procedure:** Compare the row-specific effect definition and displayed scale with the spanning column heading.

**Calculation:** No arithmetic is required: a win ratio and an FMA-point mean difference are different measures/scales under the supplied labels.

**Alternative source-grounded interpretations:** The heading may be intended for all rows except Estimand 4, but no exception or qualifying footnote is shown.

**Mechanical evidence recheck:** Heading and row were found on the same page. The label/scale comparison applies; an intended header scope or exception is missing. A row-specific override is an alternative, not a resolution.

**Quality-control relevance:** Table headings should make the effect measure and scale for each row unambiguous.

**Potential downstream evidence impact:** If confirmed, an effect estimate could be copied under the wrong measure into an evidence table or meta-analysis dataset.

**Human verification steps:** Confirm the intended heading scope and amend the heading or row label as appropriate.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C012 — Estimand 4 is called an odds ratio in prose and a win ratio in the table

**Candidate statement:** Matched Estimand 4 displays label the same `1.06` effect as an odds ratio in prose and a win ratio in the table. **Pending Human Adjudication.**

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** DOC-004, [Supplement 3 — PDF p. 12](<../joi250066supp3_prod_1761597796.4701.pdf#page=12>), eTable 2 narrative; [PDF p. 13](<../joi250066supp3_prod_1761597796.4701.pdf#page=13>), Estimand 4 row.

**Source evidence:** Narrative calls `1.06 (95% CI, 0.86 to 1.25)` an `odds ratio`; the matched full-analysis-set composite row calls `1.06 [0.86-1.26]` a `win ratio [95% CI]`.

**Reported-versus-comparator:** `Odds ratio` in prose versus `win ratio` in the matched table row.

**Reasoning procedure:** Match estimand, population, composite, estimate, and interval before comparing the declared measure labels.

**Calculation:** No arithmetic is required: odds ratio and win ratio are not interchangeable labels under the supplied definitions.

**Alternative source-grounded interpretations:** A modelling relationship may exist, but the supplied package does not define the terms as synonyms.

**Mechanical evidence recheck:** Both labels, matched estimate, and locations were found. The measure-label comparison applies; a model definition equating terms is absent. Such a relationship is inferred, not established.

**Quality-control relevance:** A repeated estimand should have one identifiable effect-measure label.

**Potential downstream evidence impact:** If confirmed, an effect estimate could be extracted under the wrong measure by an evidence user.

**Human verification steps:** Confirm the intended Estimand 4 measure and align the narrative or table label.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

Confirmed reporting inconsistencies can matter when a data extractor, systematic reviewer, meta-analyst, guideline developer, or other downstream evidence user copies a count, summary, interval endpoint, effect-measure label, or outcome terminology. This is a bounded quality-control consideration only: the supplied package does not establish any actual propagation, paper-level conclusion change, or harm.

## Limitations and Missing Definitions

See the bounded source-specific limitations in [limitations.md](review_1_5_1/limitations.md). This review uses supplied package evidence only and cannot resolve missing units, derivations, raw analysis output, scoring definitions, event-counting rules, or model definitions.

## Human Adjudication Checklist

- Confirm each cited source location and printed value against the supplied PDF.
- Determine whether matched results use the same population, timing, outcome definition, analysis set, scale, and rounding convention.
- Obtain the missing source definitions or analysis output where identified in each card.
- Record any disposition, importance, action, initials, and notes only in the card's blank human adjudication fields.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

The direct-source and reused-artifact hash baselines were recomputed at audit and returned `OK` for all 7 direct sources and 88 reused artifacts. Canonical evidence, relationship, recheck, and quality-control artifacts are linked from [coverage_manifest.md](review_1_5_1/coverage_manifest.md). The complete stable candidate set is documented in [candidate_ledger.md](review_1_5_1/candidate_ledger.md), [evidence_recheck.md](review_1_5_1/verification/evidence_recheck.md), and [evidence_quality_audit.md](review_1_5_1/quality/evidence_quality_audit.md).

### Agent execution

Every coordinator and specialist execution is listed in [agent_execution_manifest.md](review_1_5_1/agent_execution_manifest.md). The two statistical passes used distinct fresh high-effort Terra runtime agents and cover `S001`-`S021`.

### Performance

- **Target basis:** Seven supplied PDFs contain 159 pages, including a 94-page protocol, an 18-page SAP, and a 27-page results supplement; 131 pages initially lack reusable page extraction, and several result-relevant tables and cross-document relationships require fresh mapping and two independent statistical passes.
- **Total source units:** 159
- **Fresh-source units:** 131
- **Target elapsed minutes:** 60-90
- **Started UTC:** 2026-09-03T03:42:25Z
- **Finished UTC:** 2026-09-03T06:49:32Z
- **Observed elapsed minutes:** 187.1
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Host load averages near 609 on 8 CPUs caused prolonged shared-filesystem and tool latency; protocol/SAP native encoding failures required fresh direct layout/render inspection; targeted source-page visual confirmation and audit repairs were completed.

### Token accounting

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Output tokens | Total tokens | Token-only API-equivalent estimate (USD) |
|---|---:|---:|---:|---:|
| gpt-5.6-sol | 0 | 0 | 0 | 0.000000 known; complete estimate unavailable |
| gpt-5.6-terra | 0 | 0 | 0 | 0.000000 known; complete estimate unavailable |

Per-agent detail is in [token_usage_summary.md](review_1_5_1/token_usage_summary.md). Amounts are token-only API-equivalent estimates under the dated pricing snapshot, not invoices; non-token tools, containers, storage, subscriptions, taxes, and other vendor charges are excluded.
