# Numeric Consistency Review

## Scope and outcome

This numeric-consistency review processed all **91** stable N relationships in `relationships/numeric_relationship_inventory.md`, using the complete current main and support evidence maps and direct supplied PDFs. It applied arithmetic, total, subgroup-sum, numerator/denominator/percentage, missingness/population, rounding, unit/scale/reference-group, rate/risk/proportion/count, repeated-value, and displayed-table checks where the source establishes a compatible relationship.

**Candidate proposals: 4 distinct document-grounded proposals.** They are proposals for later registration and human adjudication only. This artifact assigns no stable C IDs, severity, validity, disposition, or correction.

## Complete check record

| Scope | Relationship count | Checks applied | Result |
|---|---:|---|---|
| DOC-001 population, flow, baseline Table 1, Figures 1-3 | 25 | Totals, subgroup sums, count/percentage identities, risk-count starting Ns, available-data denominators, labels/scales | NC-04 flow allocation total and NC-03 threshold-label conflict. The 316-to-305 route itself reconciles once the three rerecruited participants are accounted for. |
| DOC-001 Table 2, results and safety Table 3 | 26 | Table totals, n(%), model-estimand labels, units, reference direction, interval ordering, matched narrative values | No arithmetic/denominator candidate. All Table 3 n(%) values reconcile to 96/166 at displayed precision. Model-based Table 2 changes were not incorrectly treated as raw subtraction. |
| DOC-002 protocol and Appendix 2 | 20 | Planned-population and endpoint identities, formula labels, power/count relationships, units and scale | No candidate. Planning quantities and parent-study/contextual values are not conflated with observed long-term results. |
| DOC-003 eFigures/eTables and DOC-004 | 20 | Count/percentage, subgroup totals, longitudinal N labels, timepoint/footnote labels, LS-estimate direction, repeated exact results | NC-01 and NC-02 from eTable 2; all other checked numeric identities pass within stated rounding. DOC-004 has no applicable result relationship. |

## Candidate proposals

### NC-04 — Figure 1 labels 305 available participants but its two randomized-treatment allocations total 315

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3`, Figure 1, “305 Available for long-term follow-up and randomized,” immediately followed by “193 Randomized to undergo bariatric surgery” and “122 Randomized to undergo medical/lifestyle intervention.” The adjoining Results text states 305 available and 262 enrolled.
- **Printed inputs:** available cohort `305`; treatment allocations `193` surgery and `122` medical/lifestyle; enrolled counts `166` and `96`.
- **Direct observation:** The two allocation counts are displayed as branches of the Figure 1 305-participant box, but `193 + 122 = 315`, not 305. In contrast, enrolled counts reconcile: `166 + 96 = 262`; and the upstream flow reconciles: `316 - 12 - 2 + 3 rerecruited = 305`.
- **Reproducible rule and calculation:** A displayed parent flow box partitioned into two mutually exclusive treatment-allocation branches must equal their sum. Calculation: `193 + 122 - 305 = 10`. Tolerance: zero for participant counts.
- **Inference distinguished from observation:** The printed ten-participant discrepancy is direct. It is unresolved inference whether the parent total, either allocation count, or the Figure's use of “available ... and randomized” is erroneous or refers to different populations.
- **Alternative source-grounded interpretations:** (1) `193` and `122` are original-randomization counts from another population, while 305 is the long-term available cohort; (2) one displayed allocation count is a typo; (3) 305 is a typo. The arrows and wording do not label the allocation counts as a different denominator.
- **Quality-control relevance:** Flow totals identify analysis population and treatment denominators; an inconsistent branch total can propagate to extraction of allocation, retention, and missingness.
- **Exact human question:** Do the Figure 1 counts of 193 and 122 refer to the 305 available participants or to another explicitly defined cohort, and which printed total/count(s) should be corrected or relabeled so the flow denominator is unambiguous?

### NC-01 — eTable 2 is headed and populated as a year-12 table, but its rules label the changes and comparisons as year-7 quantities

- **Category:** Measure, label, or scale inconsistency; cross-document/timepoint numeric inconsistency.
- **Exact source locations:** `joi240004supp2_prod_1721756962.82552.pdf#page=15`, eTable 2 title and columns; `joi240004supp2_prod_1721756962.82552.pdf#page=16`, footnotes a-c.
- **Printed inputs:** The title reads, “eTable 2. Laboratory and clinical outcomes at year 12 and changes from baseline.” Its value columns are headed “Year 12” for each group. Footnote a states that descriptive values are presented “for baseline and year-7 data” and changes/comparisons are least-square estimates; footnote b calls binary changes “odds ratios (7-year over baseline)”; footnote c defines numeric comparisons using each group’s “7-year change” and binary comparisons as odds “at year 7.”
- **Direct observation:** The same printed eTable pairs “Year 12” title/column labels with three footnote rules that explicitly say “year-7.” This applies to continuous and binary rows, including the displayed 12-year HbA1c values 7.9/7.3 and 12-year remission values 0%/12.7%.
- **Reproducible rule and calculation:** For one table, the timepoint in a column title and the timepoint used by the footnote definition of that column’s change/comparison must agree. Comparison: `Year 12 != year 7`; no numerical rounding tolerance can reconcile different time labels. Tolerance: exact text identity required.
- **Inference distinguished from observation:** It is an inference, not a verified correction, that “year-7” is a residual/copied footnote label: the title, column headings, and values are all printed as year 12, but the supplied source does not state which label controls the estimand.
- **Alternative source-grounded interpretations:** (1) The three footnotes are erroneous carryovers and the estimates are year-12 analyses; (2) the title/column headings are wrong; (3) descriptive values are year 12 but footnoted changes/comparisons are actually year 7. The latter would require an unexplained mixing of timepoints in a table headed year 12.
- **Quality-control relevance:** Timepoint identifies the outcome estimand. A data extractor could attach 7-year change/OR definitions to 12-year values or vice versa.
- **Exact human question:** Which timepoint—year 12 as printed in the eTable title/columns, or year 7 as printed in footnotes a-c—was used for each eTable 2 change, group comparison, and binary odds ratio, and should the conflicting labels be corrected?

### NC-02 — The 12-year HbA1c group comparison has incompatible printed P-value displays across matched sources

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1`, Abstract Results (12-year HbA1c difference −1.1%, 95% CI −1.7% to −0.5%; `P = .002`); main PDF p. 3, Results (same timepoint/result, `P = .002`); `joi240004supp2_prod_1721756962.82552.pdf#page=15`, eTable 2 HbA1c row (difference −1.1%, 95% CI −1.7% to −0.5%; `P < .001`).
- **Printed inputs:** Main article: effect `−1.1%`, CI `−1.7% to −0.5%`, `P = .002`. eTable 2: effect `−1.1`, CI `−1.7, −0.5`, `P < .001`; the table title and cells label this as year 12.
- **Direct observation:** Matched effect estimate, CI, contrast (surgery minus medical/lifestyle change), and stated 12-year timepoint are printed identically at the displayed precision, but the P-value displays differ: `.002` versus `<.001`.
- **Reproducible rule and calculation:** For a matched result with same population, timepoint, contrast, effect, and displayed CI, the reported P display must be the same or compatible by its stated inequality. `0.002 < 0.001` is false; thus an exact `P = .002` cannot satisfy `P < .001`. Tolerance: none, because the comparator is a strict printed inequality and .002 has three printed decimal places.
- **Inference distinguished from observation:** Whether a different unprinted analysis, rounding convention, or the timepoint-label problem in NC-01 explains the mismatch is unresolved inference. The printed incompatibility itself is direct.
- **Alternative source-grounded interpretations:** (1) the main article’s `.002` is the intended P value; (2) eTable 2’s `<.001` is the intended value and the main value is wrong; (3) eTable 2’s footnotes mean its change/comparison is a different (year-7) analysis despite the year-12 title/cells. The source supplies no statement selecting an alternative.
- **Quality-control relevance:** A review or meta-analysis that extracts the 12-year primary-effect P value encounters non-interchangeable values and may misclassify statistical evidence.
- **Exact human question:** Are the main article and eTable 2 reporting the same 12-year HbA1c group-comparison analysis, and if so, which P value (`.002` or `<.001`) is correct; if not, what different analysis/timepoint does the supplement P value represent?

### NC-03 — The main-text HbA1c threshold is printed as ≤6.5%, whereas the corresponding Table 2 outcome is printed as <6.5%

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=4`, Results narrative: “threshold of HbA1c less than or equal to 6.5% (P = .002; Table 2)”; `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6`, Table 2 row: “HbA1c <6.5%, %” with group values 17.3% and 37.7%, OR 2.89 (95% CI, 1.48 to 5.64), `P = .002`; main PDF p. 2, Secondary Outcomes/remission definition uses HbA1c `<6.5%`.
- **Printed inputs:** Narrative threshold `HbA1c ≤6.5%`; corresponding table label `HbA1c <6.5%`; identical cited P `.002` and Table 2 locator.
- **Direct observation:** The text explicitly directs the reader to Table 2 for the same P value, but employs a nonidentical cutoff operator. `≤6.5%` includes values exactly 6.5%; `<6.5%` excludes them.
- **Reproducible rule and calculation:** The sets differ by the boundary value: `{x | x ≤ 6.5} = {x | x < 6.5} ∪ {6.5}`. Equality of the two printed outcome definitions is therefore false unless no values equal 6.5%, which is not supplied. Tolerance: none for a logical cutoff operator; no numerical rounding rule changes inclusion at exactly 6.5.
- **Inference distinguished from observation:** It is unknown whether any participant had HbA1c exactly 6.5% or which operator was used for analysis. The candidate is the observable reporting-label conflict, not an assertion that the counts/OR are incorrect.
- **Alternative source-grounded interpretations:** (1) the narrative “less than or equal” is imprecise and Table 2’s `<6.5%` controls; (2) the Table 2 label omits equality; (3) values were rounded before thresholding, although no supplied source says so.
- **Quality-control relevance:** Threshold definitions determine which participants are counted in a binary outcome and can be copied as an eligibility/outcome definition by downstream extractors.
- **Exact human question:** Was the reported HbA1c 6.5% binary outcome analyzed as `<6.5%` or `≤6.5%`, and should the narrative or Table 2 label be amended to make the threshold identical?

## Non-candidate diagnostic records

- **DISPLAY_ZERO_NOT_CANDIDATE (N084):** Supplement 2 eTable 2, PDF p. 16, prints medical 12-year remission as `0%` and its footnote explicitly states the rate was `2e-16`. This is an explained finite-precision display; it is not a candidate solely because a displayed percentage is zero.
- **Model-derived difference diagnostic (N026-N039, N083-N084, N086):** Table 2/eTable 2/eTable 4 changes and differences are least-square/model estimates under stated rules. Raw displayed means may not subtract exactly to printed model changes. No candidate was created without a direct contradiction.
- **Participant-flow diagnostic (N010):** The 316-to-305 route is explained by withdrawals/deaths plus three successfully rerecruited participants. The separate 305-to-(193+122) mismatch is retained as NC-04 because the Figure directly draws those allocation branches from the 305 box.

## Limitations

No participant-level data, unrounded least-square estimates, covariance matrices, exact annual plotted coordinates, or a statement resolving eTable 2’s timepoint labels is supplied. Those omissions prevent reconstruction of some model calculations but do not affect the three direct printed mismatches above. The review did not use external sources or the web.
