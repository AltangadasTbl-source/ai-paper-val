# Final Evidence-Quality Audit — Workflow 1.5.1

## Audit outcome

The complete stable candidate set is **C001, C002, C003, C004, C005, C006**. All six IDs occur in the candidate ledger and mechanical evidence recheck, and every cited candidate location was found in the supplied direct-source PDFs. Each candidate has printed evidence and a comparator, an applicable reproducible rule, a direct-observation/inference distinction, source-grounded alternatives, an exact human question, and neutral wording. No candidate is based on `P = 0`, `p = 0.000`, mathematical nonzero-tail reasoning, or another display-zero-only argument. All six remain **Pending Human Adjudication**.

Scientific source-unit coverage is complete: four direct PDFs, **115/115 mapped PDF pages**, partitioned as **42 reusable-backed + 73 fresh-required = 115 total**. The global quantitative inventories contain **N001–N068 (68/68)** and **S001–S036 (36/36)**. Numeric and cross-source checkers cover all 104 global relationships. Both statistical artifacts give an explicit completion record for every S ID. Discovery restarted from the complete source-linked evidence maps; the artifacts state that legacy candidate/queue/disposition/report records were not scientific inputs, and no count, top-N, or earlier 10-candidate boundary controlled discovery.

The two required statistical passes are separately manifested as fresh `gpt-5.6-terra`/`high` agents: `/root/statistical_pass_1` and `/root/statistical_pass_2`. Their runtime IDs are distinct and non-placeholder. Candidate-stage manifest scopes enumerate every applicable ID rather than using ranges. Every current coverage-manifest row contains one plain relative artifact path, and every listed completed artifact exists. The coordinator still must change the evidence-quality row from `ASSIGNED` to `COMPLETE` and add the required `report_generation` row after the report artifact is generated.

## Repair re-audit and remaining coordinator closure

The previously reported S013 transcription defect is resolved. The component support map, merged support map, numeric inventory, and statistical inventory now state that Results Supplement pp. 28 and 31 both directly print `P<0.001`; the earlier `p>0.001` locator transcription is explicitly retained only as a corrected noncandidate provenance record. This agrees with both statistical passes and does not produce a stable candidate.

The candidate ledger now opens with the correct six-candidate count and retains C001–C006 without deletion, merging, or renumbering. Its PDF links resolve from the ledger directory. PDF links in the main quantitative extraction, numeric checker, cross-source checker, statistical pass 2, evidence recheck, and this audit also resolve to existing package sources and physical pages. Targeted re-audit counted all 78 main-extraction source-link occurrences and found zero broken links.

After this updated artifact is complete, the coordinator must change the C001–C006 evidence-quality row in `coverage_manifest.md` from `ASSIGNED` to `COMPLETE`. The required `report_generation` row must be added with all six IDs and one plain report artifact path after report assembly.

No evidence-quality, source-coverage, relationship-coverage, stable-ID, candidate-card, calculation, or source-link defect remains open in the audited artifacts. The remaining items are expected coordinator stage-closure and downstream reporting tasks. They do not add, delete, merge, rank, suppress, or adjudicate a stable candidate.

## C001 — Invasive-ventilation descriptive summary is labeled mean (SD) but displays two endpoints

- **Ledger and recheck presence:** Present in both canonical artifacts with matching title, source values, comparator, and human question.
- **Category audit:** `Measure, label, or scale inconsistency` follows the permitted scope.
- **Exact direct-source locations:** [Main article, Table 2, PDF p. 7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7) and [Results Supplement, eTable 10, PDF p. 18](../../../joi250040supp3_prod_1753124024.38098.pdf#page=18).
- **Printed evidence and comparator:** Table 2 labels the row `Duration of invasive ventilation, mean (SD), h` and prints `84.0 (35.0 to 178.9)` versus `78.0 (33.2 to 161.0)`. The same row separately prints the model effect `Mean difference, 6.8 (−3.0 to 16.5)`. Supplement eTable 10 describes its central-value/two-bound summaries as median (IQR).
- **Applicable rule and reproduction:** A `mean (SD)` group display has one mean and one SD. Each printed parenthesis instead has two distinct ordered endpoints: `35.0 < 178.9` and `33.2 < 161.0`. The separately modelled mean difference does not identify either descriptive parenthesis as one SD. No rounding rule is involved.
- **Evidence-card completeness:** Exact location, source evidence, comparator, rule, calculation/logical comparison, direct-versus-inferred separation, alternatives, relevance, bounded downstream concern, and exact human question are present.
- **Direct versus inferred:** The label, values, unit, and supplementary convention are direct observations. The identity of the intended descriptive statistic and any production mechanism remain inferred.
- **Alternatives and missing definition:** The label may have been copied incorrectly while the values represent median (IQR), or the displayed endpoints/`to` text may be wrong while a mean/SD summary was intended. The package does not define the two endpoints.
- **Duplicate assessment:** Distinct from C003 because it concerns a different outcome row, group values, model effect, and intended descriptive definition.
- **Wording and impact audit:** Neutral and limited to the risk that an extractor could misclassify an interval as an SD; it does not claim a changed trial conclusion.
- **Exact human question:** What descriptive statistic and interval/dispersion do the two group displays represent, and which printed element should be revised to express it?
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — eTable 10 uses a comma in one one-decimal survival percentage

- **Ledger and recheck presence:** Present in both canonical artifacts with matching direct evidence and arithmetic.
- **Category audit:** `Measure, label, or scale inconsistency` follows the permitted scope.
- **Exact direct-source location:** [Results Supplement, eTable 10, PDF p. 18](../../../joi250040supp3_prod_1753124024.38098.pdf#page=18), `Alive at day 90 [n (%)]`, Period 2 usual protein, `n = 530`.
- **Printed evidence and comparator:** The target cell visibly prints `383 (72, 3%)`; all seven matched neighboring cells use point-decimal percentages.
- **Applicable rule and reproduction:** `383 / 530 × 100 = 72.2641509…%`, which rounds to `72.3%` at one decimal. The issue is the isolated comma-and-space relative to the table's point-decimal convention, not a numerator/denominator discrepancy.
- **Evidence-card completeness:** Exact location, printed evidence, full comparator, arithmetic, rounding basis, direct-versus-inferred separation, alternative, relevance, bounded downstream concern, and exact human question are present.
- **Direct versus inferred:** The punctuation, count, denominator, and neighboring notation are direct observations. The proposed `72.3%` rendering and any localization/typesetting mechanism are inferences.
- **Alternative and missing definition:** A comma can be a decimal separator and preserves the numeric meaning here. The source does not state that this isolated notation change was intentional.
- **Duplicate assessment:** Distinct from C005 and C006 because it concerns a decimal-separator inconsistency in a different outcome row, not a percent-sign switch.
- **Wording and impact audit:** Neutral and bounded to possible manual or automated extraction ambiguity; no conclusion change is asserted.
- **Exact human question:** Is the comma-and-space intentional, or should the cell use the table's point-decimal convention for the percentage corresponding to `383/530`?
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Bayesian quantile row is labeled mean (SD) despite its associated median estimand and two-endpoint group displays

- **Ledger and recheck presence:** Present in both canonical artifacts with matching source evidence and model comparator.
- **Category audit:** `Measure, label, or scale inconsistency` follows the permitted scope.
- **Exact direct-source locations:** [Main article, Table 2, PDF p. 7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7), [Results Supplement methods, PDF p. 5](../../../joi250040supp3_prod_1753124024.38098.pdf#page=5), and [Results Supplement eFigure 6, PDF p. 27](../../../joi250040supp3_prod_1753124024.38098.pdf#page=27).
- **Printed evidence and comparator:** The Bayesian row says `mean (SD)`, prints `62.0 (0 to 77)` versus `64.0 (0 to 77)`, and reports `Median difference, −1.50 (−3.86 to 0.90)`. The supplement explicitly defines the Bayesian quantile coefficient as a difference in medians and repeats the median-difference/CrI result.
- **Applicable rule and reproduction:** Both group parentheses contain two ordered endpoints (`0 < 77`), not one SD. The row's effect label and matched supplement identify a median estimand. No supplied text explains an intentional separate mean/SD display, and the displayed form is not one mean plus one SD.
- **Evidence-card completeness:** Exact locations, printed evidence, comparator, rule, logical comparison, direct-versus-inferred separation, alternatives, relevance, bounded downstream concern, and exact human question are present.
- **Direct versus inferred:** All labels, group values, model result, and supplement method are direct observations. Copy-forward and the identity of the intended group summary are inferred.
- **Alternatives and missing definition:** The label may have carried over from the preceding linear-model row. Independently calculated descriptive summaries could accompany a median estimand, but the source neither defines that convention nor explains the two endpoints.
- **Duplicate assessment:** Distinct from C001 because the printed values, outcome, comparator, and Bayesian median-estimand rule differ.
- **Wording and impact audit:** Neutral and bounded to possible misclassification of descriptive and analysis-scale information by an extractor; no model invalidity or conclusion change is claimed.
- **Exact human question:** What statistic and interval do the two Bayesian-row group displays represent, and was `mean (SD)` intended or carried over from the preceding row?
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Discussion describes the matched day-10 urea summaries as means while Results reports medians (IQR)

- **Ledger and recheck presence:** Present in both canonical artifacts with matching locations, terms, and values.
- **Category audit:** `Cross-document numeric inconsistency` is used as the primary category for the matched cross-location report. The issue is specifically a summary-statistic label mismatch, within the permitted quantitative-reporting scope.
- **Exact direct-source locations:** [Main article Results, PDF p. 5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5) and [Main article Discussion, PDF p. 8](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=8).
- **Printed evidence and comparator:** Results reports day-10 `median (IQR)` blood urea of `13.0 (8.2–18.8)` versus `10.6 (7.1–15.4)` mmol/L. Discussion says `mean urea concentrations at day 10 were higher in the augmented protein group`.
- **Applicable rule and reproduction:** Matching analyte, day, intervention groups, and direction links the two passages. Mean and median are different summary-statistic labels. No mean can or should be reconstructed from the supplied medians/IQRs.
- **Evidence-card completeness:** Exact locations, printed evidence, comparator, matching rule, direct-versus-inferred separation, alternatives, missing input, relevance, bounded downstream concern, and exact human question are present.
- **Direct versus inferred:** The Results label/values and Discussion wording are direct. Whether `mean` is informal prose, a copy edit, or a reference to an unprinted analysis is inferred.
- **Alternative and missing input:** Discussion may use `mean` nontechnically or refer to unprinted group means. The package supplies no matched day-10 mean values or participant-level values.
- **Duplicate assessment:** Distinct from C001/C003 because it is a cross-location mean-versus-median term mismatch for biochemical results, not a Table 2 label-versus-display issue.
- **Wording and impact audit:** Neutral and bounded to possible extraction of the wrong summary-statistic type; both passages retain the same direction and the card does not claim a changed conclusion.
- **Exact human question:** Does Discussion refer to the printed median (IQR) comparison or a distinct unprinted mean analysis; if the latter, where are the mean values and definition reported?
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — eTable 10 tracheostomy row switches percent-sign notation across period cells

- **Ledger and recheck presence:** Present in both canonical artifacts after pass-2 append, without renumbering or alteration of C001–C004.
- **Category audit:** `Measure, label, or scale inconsistency` follows the permitted scope.
- **Exact direct-source location:** [Results Supplement, eTable 10, PDF p. 18](../../../joi250040supp3_prod_1753124024.38098.pdf#page=18), `Tracheostomy in ICU [n (%)]`.
- **Printed evidence and comparator:** The first four cells print `27 (5.6)`, `36 (10.7)`, `29 (9.7)`, and `24 (4.5)` without `%`; the last four print `35 (6.4%)`, `38 (10.3%)`, `43 (12.2%)`, and `23 (4.8%)` with `%`.
- **Applicable rule and reproduction:** The `[n (%)]` header and denominators 480, 335, 298, 530, 551, 368, 352, and 483 identify one percentage field. All eight count/denominator calculations reproduce the printed one-decimal values: 5.6%, 10.7%, 9.7%, 4.5%, 6.4%, 10.3%, 12.2%, and 4.8%. The mismatch is the within-row sign convention, not arithmetic.
- **Evidence-card completeness:** Exact location, every source/comparator cell, denominators, calculations, direct-versus-inferred separation, alternative, relevance, bounded downstream concern, and exact human question are present.
- **Direct versus inferred:** The header, cells, denominators, and sign split are direct. A template or production-boundary mechanism is inferred and not claimed as fact.
- **Alternative and missing definition:** The row header makes the unsigned values intelligible without repeated signs, but it does not explain the switch to explicit signs for only the final four cells. Intended typography is not stated.
- **Duplicate assessment:** Distinct from C006 under the required merge rule because the outcome row and every printed count/percentage comparator differ. Distinct from C002 because the latter concerns a decimal separator.
- **Wording and impact audit:** Neutral and bounded to possible inconsistent parsing of period-specific percentages; no effect estimate or conclusion is challenged.
- **Exact human question:** Was the within-row switch intentional, and which one percent-sign convention should apply to all eight tracheostomy cells?
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — eTable 10 new-KRT row switches percent-sign notation across period cells

- **Ledger and recheck presence:** Present in both canonical artifacts after pass-2 append, without renumbering or alteration of earlier IDs.
- **Category audit:** `Measure, label, or scale inconsistency` follows the permitted scope.
- **Exact direct-source location:** [Results Supplement, eTable 10, PDF p. 18](../../../joi250040supp3_prod_1753124024.38098.pdf#page=18), `New kidney replacement therapy commenced during index ICU admission after commencing trial enteral nutrition [n (%)]`.
- **Printed evidence and comparator:** The first four cells print `33 (6.9)`, `26 (7.8)`, `22 (7.4)`, and `35 (6.6)` without `%`; the last four print `38 (6.9%)`, `33 (9.0%)`, `29 (8.2%)`, and `33 (6.8%)` with `%`.
- **Applicable rule and reproduction:** The `[n (%)]` header and the same eight column denominators identify one percentage field. All eight count/denominator calculations reproduce the printed one-decimal values: 6.9%, 7.8%, 7.4%, 6.6%, 6.9%, 9.0%, 8.2%, and 6.8%. The mismatch is the within-row sign convention, not arithmetic or a rate/count confusion.
- **Evidence-card completeness:** Exact location, every source/comparator cell, denominators, calculations, direct-versus-inferred separation, alternative, relevance, bounded downstream concern, and exact human question are present.
- **Direct versus inferred:** The header, cells, denominators, and sign split are direct. Any typesetting/template mechanism is inferred and not asserted.
- **Alternative and missing definition:** The row header makes the unsigned values interpretable as percentages, but no source statement explains why only the final four cells include signs or which convention was intended.
- **Duplicate assessment:** Distinct from C005 because it concerns a different clinical outcome row with different printed values and comparator cells; distinct from C002's decimal punctuation issue.
- **Wording and impact audit:** Neutral and bounded to possible inconsistent extraction of period-specific KRT percentages; it does not claim an incorrect risk ratio or altered conclusion.
- **Exact human question:** Was the within-row switch intentional, and which one percent-sign convention should apply to all eight new-KRT cells?
- **Status:** Pending Human Adjudication.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Complete-set reconciliation

- **Ledger IDs:** C001, C002, C003, C004, C005, C006.
- **Recheck IDs:** C001, C002, C003, C004, C005, C006.
- **Quality-audit IDs:** C001, C002, C003, C004, C005, C006.
- **Missing rechecks:** None.
- **Unsupported candidate arithmetic:** None found.
- **Candidate-only display-zero basis:** None.
- **Post-ID merging, deletion, suppression, or renumbering:** None.
- **Ranking or adjudication assigned:** None; every ID remains Pending Human Adjudication.
- **Remaining limitations:** Listed in `limitations.md` and in the candidate-specific missing-definition notes above.
