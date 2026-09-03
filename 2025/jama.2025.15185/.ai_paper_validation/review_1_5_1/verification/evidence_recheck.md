# Mechanical Evidence Recheck

All 12 immutable stable candidate IDs were rechecked separately against the cited supplied PDFs. Fresh direct-source native/layout extraction was used for the cited pages, and the main-article table pages were also visually inspected. Extracted text was used only as a direct rendering of the supplied source, not as a substitute for document identity or page location. Each entry remains **Pending Human Adjudication**; the observations below are evidence facts, not dispositions.

## C001 — Baseline index-stroke type counts differ across baseline tables

- **Cited location found:** Yes. [Main article — PDF p. 4](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4), Table 1; [Supplement 3 — PDF p. 10](../../../joi250066supp3_prod_1761597796.4701.pdf#page=10) and [Supplement 3 — PDF p. 11](../../../joi250066supp3_prod_1761597796.4701.pdf#page=11), eTable 1.
- **Source printed value/text matched:** Yes. Main Table 1 labels the levodopa group `n = 307` and prints index-stroke type as ischemic `260 (84.7)` and hemorrhagic `47 (15.3)`.
- **Comparator printed value/text matched:** Yes. Supplement eTable 1 prints levodopa ischemic `263 (85.7)` and hemorrhagic `44 (14.3)`; its column identifies the levodopa group as `n=307`. The placebo pair is `259 (85.5)` and `44 (14.5)`, matching the main table.
- **Consistency rule applicable:** Yes. For the same randomized arm and the same index-stroke-type categories, counts should agree unless a different classification rule or data version is stated.
- **Calculation or logical comparison reproduced:** Main: `260 + 47 = 307`. Supplement: `263 + 44 = 307`. Relative to the main table, the supplement changes ischemic by `+3` and hemorrhagic by `-3`; the arm total is unchanged.
- **Necessary inputs available / exact missing inputs or definitions:** Group labels, arm size, category labels, counts, and percentages are present. Missing are any definition of a recoding rule, data-cut difference, or correction history that would explain the three-record reclassification.
- **Alternative source-grounded interpretation:** Both sources present a complete 307-participant levodopa split, so neither supports ordinary missingness as an explanation. An unstated recoding or revised classification remains possible, but the supplied pages do not document it.
- **Direct observation versus inferred explanation:** Direct observation is the two different count pairs under the same arm and labels. Reclassification, data-version drift, or transcription is inferred and is not established by the sources.
- **Exact remaining human question:** Which levodopa pair is intended—`260/47` or `263/44`—and was a different index-stroke classification or data version used?
- **Status:** Pending Human Adjudication

## C002 — Baseline NIHSS statistic and label do not reconcile across tables

- **Cited location found:** Yes. [Main article — PDF p. 4](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4), Table 1; [Main article — PDF p. 5](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5), Results; [Supplement 3 — PDF p. 11](../../../joi250066supp3_prod_1761597796.4701.pdf#page=11), eTable 1.
- **Source printed value/text matched:** Yes. Main Table 1 prints NIHSS at randomization as median (IQR) `7 (5-11)` for levodopa and `8 (5-10)` for placebo; the Results text prints the overall median (IQR) as `7 (5-10)`.
- **Comparator printed value/text matched:** Yes. eTable 1 labels the row `Median NIHSS at randomization [IQR]` and prints overall `8.2 (3.9)`, placebo `8.3 (3.8)`, and levodopa `8.2 (3.9)`.
- **Consistency rule applicable:** Yes, as a measure-and-label check. The supplement explicitly labels a median and IQR, while its decimal-plus-single-parenthesized-number presentation differs from both the main table and the two-endpoint IQR convention used by adjacent supplement rows.
- **Calculation or logical comparison reproduced:** The main summaries provide a central value and two IQR endpoints. Each supplement NIHSS summary provides one decimal central value and one parenthesized number, so the printed form cannot be mapped to the main median-plus-two-endpoint values without an additional definition.
- **Necessary inputs available / exact missing inputs or definitions:** All printed values and labels are available. Missing are the statistic represented by `8.2`, the meaning of `(3.9)`, and any statement that the supplement uses mean (SD), IQR width, or another dispersion convention.
- **Alternative source-grounded interpretation:** The supplement values resemble a mean (SD) presentation, especially because its adjacent eTable 4 uses that form, but eTable 1 itself does not state that interpretation. The row could instead have a stale label or an unstated one-number IQR convention.
- **Direct observation versus inferred explanation:** Direct observation is the explicit `Median ... [IQR]` label paired with `8.2 (3.9)`-style values and the different main summaries. Treating the supplement values as means (SDs) is an inference.
- **Exact remaining human question:** What statistics do `8.2 (3.9)`, `8.3 (3.8)`, and `8.2 (3.9)` represent, and should the eTable 1 label or values be changed?
- **Status:** Pending Human Adjudication

## C003 — Time from stroke onset to randomization differs across baseline tables

- **Cited location found:** Yes. [Main article — PDF p. 4](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4), Table 1; [Supplement 3 — PDF p. 11](../../../joi250066supp3_prod_1761597796.4701.pdf#page=11), eTable 1.
- **Source printed value/text matched:** Yes. Main Table 1 prints `Time from stroke onset to randomization, median (IQR), d` as `3.0 (2.0-5.0)` for both arms.
- **Comparator printed value/text matched:** Yes, with one ledger qualification: eTable 1 prints `Median time from stroke onset to randomization [IQR]` as overall `7 [5, 10]`, placebo `8 [5, 10]`, and levodopa `7 [5-11]`, but the supplement row does not visibly print a unit.
- **Consistency rule applicable:** Conditionally yes. The variable wording and arm labels match; under a common day unit and derivation, medians of 3 versus 7 or 8 cannot be a rounding difference. Exact cross-source identity also requires confirmation of the supplement's omitted unit.
- **Calculation or logical comparison reproduced:** Main arm medians are `3.0` and `3.0`; supplement arm medians are `7` and `8`. The absolute differences are 4 days for levodopa and 5 days for placebo if the supplement values are days.
- **Necessary inputs available / exact missing inputs or definitions:** Population, arm, variable wording, medians, and IQR endpoints are present. Missing are the supplement unit, any alternative time origin, derivation rule, analysis population distinction, and data-version statement.
- **Alternative source-grounded interpretation:** Because the supplement row omits an explicit unit, a different unit cannot be excluded from the page alone. A different time origin or derivation is also possible but is not described in either cited table.
- **Direct observation versus inferred explanation:** Direct observation is the same variable wording paired with `3.0` in the main table and `7/8` in eTable 1. Calling all supplement values days, or attributing the difference to a different time origin, is inferred.
- **Exact remaining human question:** What unit and time origin apply to the eTable 1 row, and which arm-specific values are intended for the shared variable?
- **Status:** Pending Human Adjudication

## C004 — Estimand 4 confidence-interval upper endpoint differs within eTable 2

- **Cited location found:** Yes. [Supplement 3 — PDF p. 12](../../../joi250066supp3_prod_1761597796.4701.pdf#page=12), eTable 2 Results narrative; [Supplement 3 — PDF p. 13](../../../joi250066supp3_prod_1761597796.4701.pdf#page=13), Estimand 4 row.
- **Source printed value/text matched:** Yes. The narrative prints Estimand 4 as `1.06 (95% CI, 0.86 to 1.25)`.
- **Comparator printed value/text matched:** Yes. The Estimand 4 row prints `1.06 [0.86 - 1.26]` for the full analysis set, death-and-FMA composite, and win-ratio strategy.
- **Consistency rule applicable:** Yes. A repeated point estimate and 95% CI for the same named estimand should have the same displayed endpoint unless a distinct computation or rounding rule is stated.
- **Calculation or logical comparison reproduced:** Point estimates match (`1.06 = 1.06`) and lower endpoints match (`0.86 = 0.86`), but upper endpoints differ by `1.26 - 1.25 = 0.01`.
- **Necessary inputs available / exact missing inputs or definitions:** Estimand number, strategy, estimate, confidence level, and both intervals are available. Missing are the unrounded upper bound, exact analysis output, and any indication that the narrative and row use different calculations or rounding.
- **Alternative source-grounded interpretation:** A boundary value combined with different rounding or a one-hundredth transcription difference could produce the two displays, but the cited pages do not identify either mechanism.
- **Direct observation versus inferred explanation:** Direct observation is the `1.25` versus `1.26` upper endpoint. Rounding, transcription, or separate analysis-output versions are inferred explanations.
- **Exact remaining human question:** Is the intended Estimand 4 upper 95% CI endpoint `1.25` or `1.26`, and what unrounded analysis output supports it?
- **Status:** Pending Human Adjudication

## C005 — Levodopa PROMIS-29 descriptive mean differs between main text and eTable 4

- **Cited location found:** Yes. [Main article — PDF p. 6](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), Secondary Outcomes; [Supplement 3 — PDF p. 15](../../../joi250066supp3_prod_1761597796.4701.pdf#page=15), eTable 4.
- **Source printed value/text matched:** Yes. The main text prints PROMIS-29 mean (SD) `66 (14)` for levodopa and `65 (14)` for placebo, with adjusted mean difference `-0.37`.
- **Comparator printed value/text matched:** Yes. eTable 4 prints placebo `65.11 (13.79)` and levodopa `64.74 (14.33)`, with estimated effect `-0.37 [-3.34 - 2.61]` and 582 participants.
- **Consistency rule applicable:** Yes. If the narrative is the whole-number display of the same group descriptive means, ordinary rounding should reproduce it.
- **Calculation or logical comparison reproduced:** `64.74` rounds to `65`, not `66`; `65.11` rounds to `65`. The eTable descriptive contrast is `64.74 - 65.11 = -0.37`, which equals the printed effect point estimate.
- **Necessary inputs available / exact missing inputs or definitions:** Group labels, means, SDs, point estimate, interval, and participant total are available. Missing are whether the main means came from the same imputed analysis set, the exact PROMIS-29 scoring transformation/version, and unrounded values underlying the main display.
- **Alternative source-grounded interpretation:** A different scoring transformation, analysis population, or descriptive-versus-model-based summary could explain the levodopa value, but neither cited location labels such a distinction.
- **Direct observation versus inferred explanation:** Direct observation is `66 (14)` versus `64.74 (14.33)` for levodopa and the exact eTable contrast. Different scoring or analysis-set use is inferred.
- **Exact remaining human question:** Which levodopa PROMIS-29 mean is intended, and do the narrative and eTable use the same scoring and analysis-population definition?
- **Status:** Pending Human Adjudication

## C006 — PROMIS-10 descriptive means differ between main text and eTable 4

- **Cited location found:** Yes. [Main article — PDF p. 6](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), Secondary Outcomes; [Supplement 3 — PDF p. 15](../../../joi250066supp3_prod_1761597796.4701.pdf#page=15), eTable 4.
- **Source printed value/text matched:** Yes. The main text prints PROMIS-10 mean (SD) `28 (6)` in both treatment groups and adjusted mean difference `0.18`.
- **Comparator printed value/text matched:** Yes. eTable 4 prints placebo `29.87 (5.74)` and levodopa `30.04 (5.73)`, with estimated effect `0.18 [-0.98 - 1.33]` and 582 participants.
- **Consistency rule applicable:** Yes. Whole-number summaries of the same descriptive means should follow the stated or ordinary rounding convention.
- **Calculation or logical comparison reproduced:** Both `29.87` and `30.04` round to `30`, not `28`. Their raw descriptive difference is `30.04 - 29.87 = 0.17`; the printed adjusted effect is `0.18`, which need not equal the raw contrast because it is labelled as estimated/adjusted in the paired sources.
- **Necessary inputs available / exact missing inputs or definitions:** Group means, SDs, effect estimate, interval, and participant total are present. Missing are the PROMIS-10 score transformation/version, whether narrative and eTable group means share the same analysis set, and the unrounded narrative inputs.
- **Alternative source-grounded interpretation:** An unstated alternative PROMIS-10 scoring transformation or population could yield values near 28 rather than 30, but no such distinction appears at the cited locations.
- **Direct observation versus inferred explanation:** Direct observation is `28 (6)` in both arms versus eTable means near 30. A scoring-version or population difference is inferred.
- **Exact remaining human question:** Which PROMIS-10 group means and scoring transformation are intended, and were the same participants summarized in both locations?
- **Status:** Pending Human Adjudication

## C007 — Placebo five-week FMA standard deviation differs from eTable 4

- **Cited location found:** Yes. [Main article — PDF p. 6](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), Secondary Outcomes; [Supplement 3 — PDF p. 15](../../../joi250066supp3_prod_1761597796.4701.pdf#page=15), eTable 4.
- **Source printed value/text matched:** Yes. The main text prints five-week FMA total mean (SD) as levodopa `57 (27)` and placebo `56 (26)`.
- **Comparator printed value/text matched:** Yes. eTable 4 prints placebo `56.27 (25.20)` and levodopa `57.37 (26.70)` for the affected-side five-week FMA total score.
- **Consistency rule applicable:** Yes. Under ordinary whole-number rounding, a detailed SD should reproduce the narrative SD if both summarize the same arm, outcome, time point, and population.
- **Calculation or logical comparison reproduced:** Placebo mean `56.27` rounds to `56`, but placebo SD `25.20` rounds to `25`, not `26`. Levodopa `57.37 (26.70)` rounds to `57 (27)`.
- **Necessary inputs available / exact missing inputs or definitions:** Outcome, time point, arm labels, detailed means/SDs, and narrative summaries are present. Missing are the unrounded main-text source values, any nonstandard rounding convention, and any analysis-population or imputation difference for the descriptive SD.
- **Alternative source-grounded interpretation:** Different analysis populations, imputation summaries, or an unstated SD convention could explain the one-unit whole-number difference, but none is labelled at these locations.
- **Direct observation versus inferred explanation:** Direct observation is placebo SD `26` versus `25.20`; the possible mechanisms are inferred.
- **Exact remaining human question:** What placebo five-week FMA SD should be reported, and do both locations use the same population and rounding rule?
- **Status:** Pending Human Adjudication

## C008 — Placebo PRAI no-improvement numerator differs between main text and eTable 4

- **Cited location found:** Yes. [Main article — PDF p. 6](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), Secondary Outcomes; [Supplement 3 — PDF p. 15](../../../joi250066supp3_prod_1761597796.4701.pdf#page=15), eTable 4.
- **Source printed value/text matched:** Yes. The main text prints levodopa `51 of 276 (18%)` and placebo `52 of 270 (19%)` reporting no improvement or no relevant improvement.
- **Comparator printed value/text matched:** Yes. eTable 4 prints PRAI no (relevant) improvement as placebo `51 (18.89)` with `n = 270` and levodopa `51 (18.48)` with `n = 276`.
- **Consistency rule applicable:** Yes. For the same arm, denominator, time point, and binary outcome category, the numerator should be identical unless a different response rule is stated.
- **Calculation or logical comparison reproduced:** `51 / 270 x 100 = 18.888...%`, matching `18.89%`; `52 / 270 x 100 = 19.259...%`, which rounds to `19%` at whole-percent precision. The percentages can each match their own numerators, but the placebo numerator differs by one.
- **Necessary inputs available / exact missing inputs or definitions:** Numerators, denominators, percentages, arm labels, and outcome wording are present. Missing are record-level classifications and any distinction between `no improvement` and `no relevant improvement` used in either summary.
- **Alternative source-grounded interpretation:** The main text combines `no improvement or no relevant improvement`, while the eTable label says `no (relevant) improvement`; an unstated category handling difference could affect one record, but the sources do not define different rules.
- **Direct observation versus inferred explanation:** Direct observation is placebo `52/270` versus `51/270`. A one-record recoding or response-rule difference is inferred.
- **Exact remaining human question:** Is the placebo numerator 51 or 52, and were identical PRAI response categories applied in both locations?
- **Status:** Pending Human Adjudication

## C009 — eTable 6 overall adverse-event total is one below arms and category sums

- **Cited location found:** Yes. [Main article — PDF p. 6](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), Table 2 and Adverse Events text; [Main article — PDF p. 7](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=7), continuation of the adverse-event narrative; [Supplement 3 — PDF p. 17](../../../joi250066supp3_prod_1761597796.4701.pdf#page=17), eTable 6.
- **Source printed value/text matched:** Yes. The main article prints a total of 146 prespecified adverse events of interest and arm counts of 79 levodopa and 67 placebo.
- **Comparator printed value/text matched:** Yes. eTable 6 prints overall `n 145`, placebo `67`, and levodopa `79`. It also prints complete intensity, outcome, and drug-relation classifications.
- **Consistency rule applicable:** Yes. The overall event count should equal the two arm counts and each exhaustive classification total when all refer to the same event set.
- **Calculation or logical comparison reproduced:** Arms: `67 + 79 = 146`. Intensity: `58 + 86 + 2 = 146`. Outcome: `1 + 29 + 116 = 146`. Drug relation: `2 + 66 + 23 + 2 + 39 + 14 = 146`. Each total differs from the eTable header `145` by one.
- **Necessary inputs available / exact missing inputs or definitions:** Overall header, arm totals, and all displayed category counts are present. Missing are any exclusion rule, duplicated-event rule, or footnote that would make the overall header use a different event set.
- **Alternative source-grounded interpretation:** One event could theoretically be excluded from an overall analysis while retained in classifications, but eTable 6 supplies no footnote or distinct denominator definition supporting that treatment.
- **Direct observation versus inferred explanation:** Direct observation is that every displayed reconciliation yields 146 while the header says 145. Exclusion, duplication, or transcription is inferred.
- **Exact remaining human question:** Should the eTable 6 overall `n` be 146, or what explicit event-counting rule makes 145 compatible with every displayed total?
- **Status:** Pending Human Adjudication

## C010 — eFigure 4 switches locally from “FMA” to “FMMA” without qualification

- **Cited location found:** Yes. [Supplement 3 — PDF p. 23](../../../joi250066supp3_prod_1761597796.4701.pdf#page=23) is eFigure 4. Coordinator direct-source rendering at 240 dpi confirmed the page title `Forest Plot of FMA Total Score Estimands at Three Months by Treatment Group (Levodopa vs. Placebo)` and the x-axis string `Adjusted Mean Difference (FMMA points)`. [Main article — PDF p. 1](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1), [p. 3](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3), and [p. 6](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) use `FMA`.
- **Source printed value/text matched:** Yes. The direct PDF page render visibly reads `Adjusted Mean Difference (FMMA points)`; the source page, rather than the derivative, remains the authority. The run-local render is `preprocessing/coordinator_confirmations/doc004-p23.png`.
- **Comparator printed value/text matched:** Yes. The figure title/legend and main article use `FMA`. DOC-003 SAP p.2 directly defines `Fugl-Meyer Motor Assessment (FMMA)` for the same assessment.
- **Consistency rule applicable:** Yes. A figure should use one locally clear outcome abbreviation or qualify synonymous abbreviations when switching between title/legend and axis.
- **Calculation or logical comparison reproduced:** This is a text-label comparison, not arithmetic: the visually confirmed axis uses `FMMA`, whereas the same figure's title/legend use `FMA`; no local equivalence note appears.
- **Necessary inputs available / exact missing inputs or definitions:** Figure identity, axis string, title/legend context, main-article FMA usage, and SAP FMMA definition are available. Missing is an explicit local statement that FMA and FMMA are intentionally synonymous on the figure.
- **Alternative source-grounded interpretation:** Intentional synonymous use is directly supported by the SAP's FMMA definition; a typographic label switch is possible but is not established.
- **Direct observation versus inferred explanation:** Direct observation is the local FMA/FMMA switch and the SAP's definition of FMMA for the same assessment. Whether the switch is intentional or typographic is inferred.
- **Exact remaining human question:** Is the local FMA/FMMA switch intentional, and should the figure use one abbreviation or define both locally?
- **Status:** Pending Human Adjudication

## C011 — Estimand 4 win ratio appears under an FMA mean-difference column heading

- **Cited location found:** Yes. [Supplement 3 — PDF p. 13](../../../joi250066supp3_prod_1761597796.4701.pdf#page=13), eTable 2 header and Estimand 4 row.
- **Source printed value/text matched:** Yes. The table-wide effect column is headed `Estimated Effect of Levodopa: Mean Difference on FMA, [CI]`.
- **Comparator printed value/text matched:** Yes. Estimand 4 describes `Difference in win-ratio at the three-month visit, win ratio [95% CI]` and prints `1.06 [0.86 - 1.26]` in that effect column.
- **Consistency rule applicable:** Yes. A dimensionless win ratio and a mean difference measured in FMA points are distinct effect measures; a spanning column heading should not label the row as the other measure without a qualification.
- **Calculation or logical comparison reproduced:** This is a measure/scale identity check. The row-specific label is `win ratio [95% CI]`, while the column label is `Mean Difference on FMA, [CI]`; the two labels are not textually or dimensionally identical.
- **Necessary inputs available / exact missing inputs or definitions:** Column heading, row label, estimand strategy, endpoint, point estimate, and interval are present. Missing is any header footnote excluding Estimand 4 or defining the column generically rather than as an FMA mean difference.
- **Alternative source-grounded interpretation:** The row-specific population-level summary may be intended to override a header written for the other estimands, but the displayed spanning header does not state that exception.
- **Direct observation versus inferred explanation:** Direct observation is the incompatible header and row measure labels. A header-scope oversight is inferred.
- **Exact remaining human question:** Is the effect-column heading intended to exclude Estimand 4, and what heading should explicitly identify the Estimand 4 win-ratio scale?
- **Status:** Pending Human Adjudication

## C012 — Estimand 4 is called an odds ratio in prose and a win ratio in the table

- **Cited location found:** Yes. [Supplement 3 — PDF p. 12](../../../joi250066supp3_prod_1761597796.4701.pdf#page=12), eTable 2 Results narrative; [Supplement 3 — PDF p. 13](../../../joi250066supp3_prod_1761597796.4701.pdf#page=13), Estimand 4 row.
- **Source printed value/text matched:** Yes. The narrative says Estimand 4 applies a composite strategy using win-ratios, `resulting in an odds ratio of 1.06 (95% CI, 0.86 to 1.25)`.
- **Comparator printed value/text matched:** Yes. The matched Estimand 4 row labels the population-level summary `win ratio [95% CI]` and prints `1.06 [0.86 - 1.26]`.
- **Consistency rule applicable:** Yes. The same named estimand and point estimate should use one effect-measure label unless the source explicitly defines a mathematical conversion or equivalence.
- **Calculation or logical comparison reproduced:** This is a measure-label comparison: `odds ratio` and `win ratio` are different printed terms attached to the same Estimand 4 value `1.06`. The supplied pages contain no identity rule equating them.
- **Necessary inputs available / exact missing inputs or definitions:** Estimand number, strategy, population-level summary label, estimate, and intervals are present. Missing are the statistical model definition and any statement that the reported odds ratio is a transformation of, or synonym for, the win ratio.
- **Alternative source-grounded interpretation:** The phrase `using win-ratios resulting in an odds ratio` may intend a particular modelling implementation, but the table calls the reported quantity itself a win ratio and the supplied pages do not explain a relationship between the measures.
- **Direct observation versus inferred explanation:** Direct observation is `odds ratio` in the narrative versus `win ratio` in the row. Modelling equivalence, loose terminology, or transcription is inferred.
- **Exact remaining human question:** Is `1.06` intended to be an odds ratio or a win ratio, and what analysis definition establishes the correct effect-measure label?
- **Status:** Pending Human Adjudication

## Recheck scope and limitations

- Stable IDs covered: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012 (12/12).
- Direct-source confirmation was completed for all cited printed numeric relationships and for the C011/C012 measure labels.
- C003 transcription qualification: Supplement 3 eTable 1 prints the `7/8/7` values but does not visibly state a unit on the row; describing those values as days requires confirmation.
- C010 visual confirmation: a targeted 240-dpi direct-source render confirms the critical rasterized axis string `FMMA points`; the source PDF page remains the authority.
- No stable ID was deleted, merged, renumbered, ranked, or assigned an adjudicative disposition.
