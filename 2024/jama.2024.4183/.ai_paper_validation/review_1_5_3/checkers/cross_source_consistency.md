# Cross-source quantitative consistency review

## Scope and method

This review compared every result match available in the canonical main and support evidence maps against the current direct PDFs: the abstract, main Results/Discussion/Table/Figures, Supplement 2 eAppendix 4/eFigures/eTables, and Protocol 2014-0213 planning Figure/Table material.  A comparison was made only after matching the population, phase, time point, contrast, estimator, measure, reference condition, analysis set, unit, and displayed precision.  Protocol simulations and planned quantities were not compared with observed trial results.  Exact source PDFs were used as the authority; reusable text was used as a locator.

The candidates below are distinct printed inconsistencies.  They have no stable IDs, no severity, and no automated disposition; each is pending human adjudication.

## Qualifying candidates

### Candidate 1 — Abstract phase-2 allocation percentages use incompatible denominators within each stated nonabstainer population

- **Locations and printed values:** The abstract states that among 191 CNRT phase-1 nonabstainers, the continuation, increase, and switch groups are `90 (47%)`, `50 (33%)`, and `51 (34%)`, respectively ([main PDF p. 1](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1)).  It similarly states that among 157 varenicline nonabstainers, increase, switch, and continuation are `39 (32%)`, `41 (34%)`, and `77 (49%)`.  Figure 2 states that 40 CNRT and 35 varenicline nonattenders were imputed into the corresponding continuation analysis group ([main PDF p. 6](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6)).
- **Comparison logic:** Within the stated denominators, the three CNRT percentages sum to 114% and the three varenicline percentages sum to 115%.  The continuation percentages use the full nonabstainer analysis denominators (`90/191=47%`; `77/157=49%`), whereas the increase/switch percentages reproduce the rerandomized denominators (`50/151=33%`, `51/151=34%`; `39/122=32%`, `41/122=34%`).  Thus, the displayed parenthetical percentages are not all percentages of the population introduced by the same sentence.
- **Supported alternatives:** The counts and Figure 2 support either (a) presenting all three percentages using each full nonabstainer analysis denominator, or (b) explicitly separating the rerandomized allocation percentages from the continuation analysis count that includes nonattenders.  The present source does not establish which editorial presentation was intended.
- **Human verification:** Confirm the intended denominator for each abstract parenthetical percentage from the analysis/output tables, then check whether the abstract should distinguish the 151/122 rerandomized populations from the 191/157 phase-1 nonabstainer analysis populations.

### Candidate 2 — CNRT dose-increase primary-outcome credible interval differs between the abstract and matched Results/eTable contrast

- **Locations and printed values:** For CNRT phase-1 nonabstainers at week 12, the abstract reports a 6% absolute RD with 95% CrI `6% to 11%` for either alternative versus continuation ([main PDF p. 1](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1)).  The Results reports the CNRT-dose-increase-versus-continuation RD as 6%, 95% CrI `2% to 11%` ([main PDF p. 5](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5)); Supplement 2 eTable 4 prints 6%, lower/upper CrI `2%` and `11%` for the same contrast ([Supplement 2 p. 21](../../../joi240036supp2_prod_1716416466.01349.pdf#page=21)).
- **Comparison logic:** These locations match the CNRT initial treatment, week-6 nonabstainer population, week-12 seven-day point-prevalence endpoint, increased-CNRT versus continuation contrast, Bayesian ARD measure, and percent scale.  The lower credible-limit value is printed as 6% in the abstract and 2% in the Results/eTable.
- **Supported alternatives:** The Results and eTable agree on `2% to 11%`; the abstract may contain a transcription error, or a different model/output may have been intended but is not identified in the printed material.
- **Human verification:** Retrieve the primary contrast output for CNRT increase minus continuation and confirm the intended 95% CrI before correcting the abstract or explaining a distinct analysis.

### Candidate 3 — CNRT switch primary-outcome credible interval differs across the abstract, Results, and eTable

- **Locations and printed values:** The abstract gives the shared CNRT alternative-versus-continuation RD as 6%, 95% CrI `6% to 11%` ([main PDF p. 1](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1)).  For CNRT switch to varenicline versus continuation, the Results prints 6%, `2% to 11%` ([main PDF p. 5](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5)), while eTable 4 prints 6%, lower/upper CrI `2%` and `10%` ([Supplement 2 p. 21](../../../joi240036supp2_prod_1716416466.01349.pdf#page=21)).
- **Comparison logic:** All three statements name the same phase-1 CNRT nonabstainer population, week-12 endpoint, switch-to-varenicline minus CNRT-continuation contrast, ARD scale, and percentage unit.  The printed 95% intervals are `6%-11%`, `2%-11%`, and `2%-10%`, which cannot all be the same displayed interval.
- **Supported alternatives:** The three locations may reflect separate output versions or transcription/rounding changes; the source does not label distinct estimands or models for these three values.
- **Human verification:** Compare the final analysis output for the CNRT-switch contrast with the abstract, Results, and eTable proofs; document whether one interval is authoritative or whether a model/version distinction exists.

### Candidate 4 — Varenicline-to-CNRT switch primary contrast has inconsistent sign/reference presentation

- **Locations and printed values:** The abstract and Results state that, relative to continuation on varenicline, switching to CNRT has an absolute RD of `−3%` (95% CrI `−4% to −1%`) and associate it with a posterior probability that continuing is worse than switching ([main PDF p. 1](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1); [main PDF p. 5](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5)).  eTable 4 labels the matched contrast `Varenicline-Non-Abst. -->CNRT (switch) vs. Varenicline-(stay)` and prints ARD `3%`, lower/upper CrI `1%` and `4%` ([Supplement 2 p. 21](../../../joi240036supp2_prod_1716416466.01349.pdf#page=21)).  The main Discussion describes the observed 3% continuation versus 0% switch values as a `3% decrement` ([main PDF p. 8](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=8)).
- **Comparison logic:** The population, time, endpoint, treatment pair, and absolute-percentage-point measure match.  If the table heading means switch minus stay, its positive 3% conflicts with both the observed 0% minus 3% direction and the negative-RD prose.  Conversely, the prose’s statement that continuation was worse than switching conflicts with its own negative RD under the stated `relative to continuation` wording and with the discussion’s decrement description.
- **Supported alternatives:** The sign may use continuation-minus-switch in prose despite the wording, the eTable heading may invert the intended reference, or one value/interpretation may be misprinted.  The supplied material does not resolve the intended ARD orientation.
- **Human verification:** Check the contrast coding and exported ARD direction for this exact switch-versus-stay row; then align the table label, reported sign/interval, and prose interpretation to one explicit reference group.

### Candidate 5 — Main baseline Table sex counts do not match their printed denominators and percentages

- **Locations and printed values:** The main Table labels both initial-treatment columns `n = 245`, then prints female `105 (42.9)` and male `145 (57.1)` for CNRT and the same values for varenicline ([main PDF p. 5](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5)).  The abstract/Results report 210 female participants among 490 analyzed participants ([main PDF p. 1](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1); [main PDF p. 4](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4)).
- **Comparison logic:** `105/245=42.9%`, but `145/245=59.2%`, not 57.1%; `105+145=250`, not 245, in each table column.  The displayed percentages sum to 100.0%, which with n=245 implies a male count of 140 per group.  The two displayed female counts sum to the separately reported 210 female participants.
- **Supported alternatives:** The male count may be `140` rather than `145`; alternatively the denominator or percentage could be wrong.  The source data needed to choose among these possibilities are not supplied.
- **Human verification:** Inspect the baseline dataset/table-generation output for sex and the phase-1 allocation totals; reconcile the male count, percentage, and column denominator in both treatment columns.

### Candidate 6 — Supplement 2 eTable 3 reverses count and percentage for one `n (%)` race/ethnicity cell

- **Locations and printed values:** eTable 3 labels the race/ethnicity rows `n (%)`.  In the VAR phase-1 nonabstainer to CNRT column, headed `N=41`, the `Other` cell is printed `4.9 (2)` ([Supplement 2 p. 19](../../../joi240036supp2_prod_1716416466.01349.pdf#page=19)).  The other populated cells in that row use count followed by percent, for example `2 (2.2)` and `1 (2.0)`.
- **Comparison logic:** With N=41, 2 participants correspond to 4.878%, displayed as 4.9%; thus the printed pair contains internally compatible values in the reverse order of the column’s declared `n (%)` format.
- **Supported alternatives:** The intended presentation is likely `2 (4.9)`, but direct data/output should determine whether the order, heading, or values were intended differently.
- **Human verification:** Check the table output or source record for this subgroup’s `Other` count and retain the established `n (%)` ordering consistently.

### Candidate 7 — Protocol Table 3 duplicates the `VAR vs. NPL` label for a contrast whose displayed estimate matches VAR versus NPL-plus

- **Locations and printed values:** Protocol Table 3 lists under Aim 2: `VAR vs. NPL`, estimate `0.370 (0.309-0.431)`; `NPL + vs. NPL`, `0.175 (0.125-0.228)`; and again `VAR vs. NPL`, `0.195 (0.119-0.269)` ([Protocol p. 34](../../../joi240036supp1_prod_1716416466.00349.pdf#page=34)).  The protocol’s Aim-2 description names the three contrasts as VAR versus continuation, augmentation versus continuation, and VAR versus augmentation ([Protocol p. 29](../../../joi240036supp1_prod_1716416466.00349.pdf#page=29)).  Its Table 2 planning cell estimates are VAR `0.399`, NPL+ `0.204`, and NPL `0.029` ([Protocol p. 33](../../../joi240036supp1_prod_1716416466.00349.pdf#page=33)).
- **Comparison logic:** The third displayed estimate is consistent with `0.399 − 0.204 = 0.195`, the VAR-versus-NPL+ contrast, whereas VAR versus NPL is represented by `0.399 − 0.029 = 0.370`, the first row.  The same `VAR vs. NPL` label therefore names two different planning contrasts.
- **Supported alternatives:** The third label may have lost the plus sign (`VAR vs. NPL+`), or Table 2/Table 3 may refer to differently defined outputs not stated in the protocol.
- **Human verification:** Check the Table 3 generation code or simulation contrast list and correct/clarify the third Aim-2 label without treating planning estimates as observed trial results.

### Candidate 8 — Detailed Supplement 2 prose reports a different EOT+30 CNRT-switch result and interval from the matched eFigure/eTable

- **Locations and printed values:** For initial-CNRT, week-6 nonabstainers who switched to varenicline, detailed prose reports `1.0% (7.0%-1.3%)` and switch-versus-continuation ARD `6.0% (3.0%-1.0%)` ([Supplement 2 p. 10](../../../joi240036supp2_prod_1716416466.01349.pdf#page=10)).  eFigure 2 prints `5/51`, `10%`, 95% CrI `7%-13%` ([Supplement 2 p. 15](../../../joi240036supp2_prod_1716416466.01349.pdf#page=15)); eTable 9 prints ARD `6% (3%-10%)` ([Supplement 2 p. 33](../../../joi240036supp2_prod_1716416466.01349.pdf#page=33)).
- **Comparison logic:** These sources match the same initial treatment, week-6 nonabstainer subgroup, switch arm, EOT+30 continuous-abstinence outcome, percentage scale, and switch-minus-continuation reference.  The prose’s 1.0% point estimate conflicts with the figure’s 10%, and its `7.0%-1.3%` and `3.0%-1.0%` interval text conflicts with the respective figure/table intervals.
- **Supported alternatives:** The prose may contain decimal/digit-order transcription errors (for example `10%`, `7%-13%`, and `3%-10%`), but the package does not authorize a correction without the analytical output.
- **Human verification:** Verify the EOT+30 switch-arm posterior output and ensure the narrative cell probability and ARD interval reproduce the figure/table values at the same displayed precision.

### Candidate 9 — Detailed Supplement 2 prose gives `1.1%` rather than the matched 11% upper credible limit for CNRT-plus at EOT+30

- **Locations and printed values:** The CNRT-plus EOT+30 detailed statement prints `8.0% (5.0%-1.1%)` ([Supplement 2 p. 10](../../../joi240036supp2_prod_1716416466.01349.pdf#page=10)).  eFigure 2 prints `4/50`, `8%`, 95% CrI `5%-11%` ([Supplement 2 p. 15](../../../joi240036supp2_prod_1716416466.01349.pdf#page=15)).
- **Comparison logic:** The population, CNRT-plus arm, EOT+30 continuous-abstinence outcome, and percent/credible-interval display match.  The prose upper limit `1.1%` is incompatible with the figure’s `11%`; its lower limit and point estimate agree after displayed precision.
- **Supported alternatives:** A misplaced decimal in the prose is supported by the figure, but the underlying output should be checked before change.
- **Human verification:** Confirm the CNRT-plus EOT+30 posterior interval and correct the prose only if the output supports `5%-11%`.

### Candidate 10 — Detailed Supplement 2 prose repeatedly gives `1.1%` rather than the matched 11% upper credible limit for varenicline-plus at EOT+30

- **Locations and printed values:** The detailed varenicline-plus EOT+30 cell and both stated 8.0% ARDs print `5.0%-1.1%` ([Supplement 2 pp. 10-11](../../../joi240036supp2_prod_1716416466.01349.pdf#page=10), [p. 11](../../../joi240036supp2_prod_1716416466.01349.pdf#page=11)).  eFigure 2 prints the VAR-plus cell as `3/39`, `8%`, `5%-11%`; eTable 9 prints VAR-plus versus continuation as `8% (5%-11%)`; and eTable 10 prints VAR-plus versus CNRT switch as `8% (5%-11%)` ([Supplement 2 pp. 15, 33-34](../../../joi240036supp2_prod_1716416466.01349.pdf#page=15), [p. 33](../../../joi240036supp2_prod_1716416466.01349.pdf#page=33), [p. 34](../../../joi240036supp2_prod_1716416466.01349.pdf#page=34)).
- **Comparison logic:** Each comparison is matched by treatment path, EOT+30 outcome, ARD/reference where applicable, scale, and displayed precision.  The repeated prose upper limit `1.1%` conflicts with the figure and both ARD tables’ `11%`.
- **Supported alternatives:** The repeated prose form may be a systematic decimal-placement transcription error; it could also reflect a separately unlabelled output, which the supplied sources do not identify.
- **Human verification:** Check the VAR-plus EOT+30 cell and both contrast outputs, then harmonize all three prose occurrences to the verified interval.

### Candidate 11 — EOT+30 abstainer ARD is printed as 1.1% in prose but 11% in the matched eTable

- **Locations and printed values:** For phase-1 abstainers continuing CNRT versus varenicline at EOT+30, prose reports CNRT `67% (58%-75%)`, varenicline `56% (48%-63%)`, posterior probability 97%, and `ARD = 1.1% (-1.0%-22%)` ([Supplement 2 p. 11](../../../joi240036supp2_prod_1716416466.01349.pdf#page=11)).  eFigure 2 supplies the same arm probabilities, and eTable 11 prints `11% (-1%-22%)`, probability 97% ([Supplement 2 pp. 15, 35](../../../joi240036supp2_prod_1716416466.01349.pdf#page=15), [p. 35](../../../joi240036supp2_prod_1716416466.01349.pdf#page=35)).
- **Comparison logic:** Population, time, outcome, treatment order (CNRT versus VAR), posterior probability, and interval endpoints match.  The raw displayed arm percentages also differ by 11 percentage points.  The prose point estimate is `1.1%`, while the matched table is `11%`.
- **Supported alternatives:** The prose may have an inserted decimal point; a separate model output is not labelled.
- **Human verification:** Confirm the EOT+30 abstainer contrast output and use one verified ARD representation across prose and eTable.

### Candidate 12 — Six-month abstainer prose conflicts with eTable 11 on interval magnitude and apparent reference direction

- **Locations and printed values:** For phase-1 abstainers at six months, prose reports CNRT `39% (30%-48%)`, varenicline `40% (33%-47%)`, posterior probability 55%, `ARD = 1.0% (-1.3%-1.1%)`, and a small benefit of varenicline continuation ([Supplement 2 p. 12](../../../joi240036supp2_prod_1716416466.01349.pdf#page=12)).  eFigure 3 prints the same 39% and 40% arm values ([Supplement 2 p. 16](../../../joi240036supp2_prod_1716416466.01349.pdf#page=16)).  eTable 11 is headed `ARD For CNRT vs. VAR` and prints `1% (-11%-12%)`, probability 56% ([Supplement 2 p. 35](../../../joi240036supp2_prod_1716416466.01349.pdf#page=35)).
- **Comparison logic:** The matched population, time, continuous-abstinence outcome, pair of treatments, percent scale, and probability-of-nonzero-difference statistic identify one result.  The prose interval `-1.3% to -1.1%` is a narrow entirely negative interval, whereas eTable 11 prints `-11% to 12%`; the probability is 55% versus 56%.  In addition, the prose calls the benefit varenicline while the table header states CNRT versus VAR with a positive 1% ARD.  The raw displayed probabilities (39% CNRT versus 40% VAR) are consistent with a one-point varenicline advantage, but not by themselves decisive about the Bayesian contrast sign.
- **Supported alternatives:** The prose could contain misplaced decimals and use a VAR-minus-CNRT reference, while the eTable may use or label a CNRT-minus-VAR reference; different rounding could account for 55% versus 56% but not the displayed interval magnitudes.
- **Human verification:** Inspect the exact six-month abstainer contrast coding/output.  Confirm the reference group, point-estimate sign, interval, and posterior probability, then make the prose, eTable header, and figure interpretation explicit and consistent.

### Candidate 13 — Six-month CNRT-switch narrative directs readers to the compliance table rather than the matched outcome table

- **Locations and printed values:** The six-month CNRT-nonabstainer prose reports switch-to-varenicline ARD `1.0% (-2.0%-3.0%)` and says `(see E-Table 7)` ([Supplement 2 p. 11](../../../joi240036supp2_prod_1716416466.01349.pdf#page=11)).  eTable 7 is titled `Phase 1 Visit and Medication Compliance` ([Supplement 2 p. 31](../../../joi240036supp2_prod_1716416466.01349.pdf#page=31)).  The same ARD is printed in eTable 9, `Phase 2 Outcomes`, as `1% (-2%-3%)` ([Supplement 2 p. 33](../../../joi240036supp2_prod_1716416466.01349.pdf#page=33)).
- **Comparison logic:** The numerical ARD agrees at displayed precision with eTable 9, which has the same outcome, time point, population, contrast, and reference.  eTable 7 contains a different measure (compliance) and no such outcome contrast, so the printed table reference does not identify the source of the stated quantitative result.
- **Supported alternatives:** `E-Table 7` may be a citation-label error for `E-Table 9`; a separate omitted table/version cannot be excluded from the package alone.
- **Human verification:** Check the supplement cross-reference in the authoring source and direct readers to the table containing the stated six-month ARD.

### Candidate 14 — Main Results reverses the attendance status for the 40 and 35 nonattender analysis assignments

- **Locations and printed values:** Main Results states that the `40` CNRT and `35` varenicline participants `who did attend rerandomization were assigned to continue treatment` ([main PDF p. 4](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4)).  The abstract says the 40 CNRT participants `did not return for rerandomization` and were assigned to continuation ([main PDF p. 1](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1)); Figure 2 labels 40 and 35 `did not attend re-randomization` and shows their inclusion in continuation analysis groups ([main PDF p. 6](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6)).
- **Comparison logic:** The locations refer to the same phase-1 nonabstainer counts and the same phase-2 continuation analysis assignment.  The main Results sentence directly reverses `did not attend` to `did attend`, changing the stated analysis-set pathway for 75 participants even though the count is unchanged.
- **Supported alternatives:** The Results wording may have omitted `not`; the package does not support treating the assigned continuation counts as a different population.
- **Human verification:** Verify the phase-2 attendance variable and ITT assignment rule in the trial record/analysis dataset, then correct the Results sentence if the Figure/abstract wording is confirmed.

## Non-candidate coverage notes

- The article’s 490 analyzed/randomized wording and the Figure 2 total of 491 phase-1 randomizations were not registered because the Results explicitly describes one post-randomization exclusion.
- The phase-2 compliance-table denominators (50 and 42) were not compared directly with the 90 and 77 outcome-analysis denominators: Figure 2 identifies the latter as including 40 and 35 nonattenders imputed into continuation, while the compliance table is an observed phase-2 compliance analysis set.
- Protocol and Supplement 2 planning/simulation values were not treated as conflicts with observed trial outcome estimates.
- No `P = 0` or equivalent display-zero value was registered; this package’s matched outcome displays use posterior probabilities and credible intervals.

## Completion and limitations

- **Matched result families reviewed:** abstract/main primary and secondary summaries; main Table and Figures 2-3; Supplement 2 eAppendices 2-5, eFigures 1-3, and eTables 3-12; Protocol 2014-0213 planned endpoint/contrast/Figure 2/Tables 2-3 relationships.
- **Qualifying candidates emitted:** 14.
- **Limitations:** Source PDFs provide printed values but not the analysis datasets or model-output files required to select a final correction.  Planning parameters were checked only against their own stated protocol relationships, not against observed trial results.  This review does not provide a validity conclusion or adjudication.
