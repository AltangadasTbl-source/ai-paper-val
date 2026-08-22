# Support Evidence Mapping Part 003: DOC-003 to DOC-005

## Scope and method

This part covers the complete assigned disjoint union: DOC-003 `joi190140supp2_prod.pdf` PDF pp. 1-11 (fresh direct native and layout text extraction), DOC-004 `joi190140supp3_prod.pdf` PDF pp. 1-3 (reusable per-page native text plus direct visual confirmation of the eTable and eFigure), and DOC-005 `joi190140supp4_prod.pdf` PDF p. 1 (fresh direct native and layout text extraction). The PDFs remain authoritative. Fresh extraction was usable; CPU OCR was not needed. DOC-004 visual confirmation resolved native-text dash/spacing artifacts in table confidence intervals.

Relationship identifiers in this shard are provisional only: `P3-N001` through `P3-N028` and `P3-S001` through `P3-S016`. Detailed numeric and statistical inventories are in the two sibling parts.

## Page-complete coverage

| Source and page | Content and mapping outcome |
|---|---|
| DOC-003 [p. 1](<../../../joi190140supp2_prod.pdf#page=1>) | Statistical-analysis-plan (SAP) administrative/protocol context and amendments. Planned endpoint/time: time to clinical progression, follow-up two years. Records the first May-2014 interim review at 80 subjects with progression or two-year completion; PSA-doubling-time revision; eligibility limits and approximately 464 randomized participants. Mapped: P3-N018, P3-N019, P3-S001. |
| DOC-003 [p. 2](<../../../joi190140supp2_prod.pdf#page=2>) | Randomization/stratification, follow-up schedule, clinical-progression definition, PSA-doubling-time formula and measurement rule. Mapped: P3-N019, P3-N020, P3-S001. |
| DOC-003 [p. 3](<../../../joi190140supp2_prod.pdf#page=3>) | Central-versus-local pathology rule; TTP definition/censoring; design assumptions and sample size/power/event target/dropout/enrolment; objectives. Mapped: P3-N020, P3-N021, P3-S002. |
| DOC-003 [p. 4](<../../../joi190140supp2_prod.pdf#page=4>) | Secondary objectives, out-of-SAP correlative/dietary recall analyses, ITT and modified ITT definitions, planned baseline summaries. Mapped: P3-N022, P3-S003. |
| DOC-003 [p. 5](<../../../joi190140supp2_prod.pdf#page=5>) | Planned baseline category tables; primary Kaplan-Meier/Greenwood/log-rank analysis; adjusted Cox supportive analysis; Gleason-only sensitivity definition. Mapped: P3-N022, P3-N023, P3-S004, P3-S005, P3-S006. |
| DOC-003 [p. 6](<../../../joi190140supp2_prod.pdf#page=6>) | Additional Gleason-only Cox and progression-free survival analyses; secondary time-to-treatment and Fisher exact analyses; exploratory anthropometry, MRI biopsy, and Nutrition Self-Efficacy Scale plans. Mapped: P3-N023, P3-N024, P3-S007, P3-S008. |
| DOC-003 [p. 7](<../../../joi190140supp2_prod.pdf#page=7>) | Longitudinal quality-of-life/anxiety analyses, summaries and four named instruments; MAX-PC, EPIC-26, FACT-P Wilcoxon plans. Mapped: P3-N025, P3-S009, P3-S010, P3-S011. |
| DOC-003 [p. 8](<../../../joi190140supp2_prod.pdf#page=8>) | IPSS analysis; significance/multiplicity/interaction rules; missing-data rules. Mapped: P3-N025, P3-N026, P3-S012, P3-S013. |
| DOC-003 [p. 9](<../../../joi190140supp2_prod.pdf#page=9>) | Appendix A administrative memo: central-pathology spreadsheet discrepancies were not further resolved; eligibility re-review and statement that no primary-population/endpoint-analysis update was needed. Mapped: P3-N020, P3-N022. |
| DOC-003 [p. 10](<../../../joi190140supp2_prod.pdf#page=10>) | Appendix B scoring definitions, item counts, possible ranges, and 0-100 transformation direction for MAX-PC, FACT-P, EPIC-26, and IPSS. Mapped: P3-N027, P3-S014. |
| DOC-003 [p. 11](<../../../joi190140supp2_prod.pdf#page=11>) | References only. No result-relevant quantitative relationship or statistical definition beyond bibliographic pagination; explicitly no applicable item. |
| DOC-004 [p. 1](<../../../joi190140supp3_prod.pdf#page=1>) | Supplement cover/index only. No result-relevant quantitative item; explicitly no applicable item. |
| DOC-004 [p. 2](<../../../joi190140supp3_prod.pdf#page=2>) | eTable, visually confirmed: dietary-pattern baseline means and follow-up mean changes with 95% CIs, sample sizes, within-group and intervention-versus-control P values. Mapped: P3-N001-P3-N016 and P3-S015. |
| DOC-004 [p. 3](<../../../joi190140supp3_prod.pdf#page=3>) | eFigure, visually confirmed: boxplots for total vegetables, cruciferous vegetables (gm/day), and lycopene at baseline/12/24 months, black control and red intervention. Mapped: P3-N017, P3-S016. |
| DOC-005 [p. 1](<../../../joi190140supp4_prod.pdf#page=1>) | Data-sharing statement, including availability with publication and approved-researcher/signed-agreement access conditions. It reports no trial result, result denominator, effect estimate, or statistical relationship; explicitly no applicable item. |

## Source-linked matching keys

- Trial identity: Men’s Eating and Living (MEAL) Study / CALGB 70807 [Alliance]; intervention versus control; active-surveillance prostate-cancer participants.
- Time conventions: SAP follow-up is two years/24 months; dietary eTable/eFigure time points are baseline, 12 months, and 24 months.
- Population conventions: eTable columns report the displayed participant count at each arm/time point; SAP distinguishes all-randomized ITT from modified ITT excluding later centrally pathology-ineligible subjects.
- eTable statistic key: `p-value*` is a within-group change at each follow-up versus baseline. `p-value†` is intervention change compared with control change. The page footnote says P values use a mixed-model analysis; it does not state a distinct effect-scale formula or covariance specification.
- eFigure key: central box = quartiles; in-box line = median; filled circle = mean; whiskers extend to the smallest/largest observations not suspected to be outliers; black = control and red = intervention. Figure supplies graphic distributions, not printed numeric estimates.

## Extraction limitations and observations

- DOC-003 is a planned SAP plus administrative appendices, not a results table. Its planned assumptions and analysis definitions must not be treated as observed trial results without a matched result location.
- DOC-004 eTable has one visible typographic double hyphen before `195.08` in the control 24-month energy confidence interval; visual inspection shows the printed interval is `(-195.08, -65.52)`. This is recorded as a transcription/layout fact only, not an adjudication or candidate.
- DOC-004 p. 3 does not print boxplot quartiles, medians, means, whisker endpoints, or outlier values numerically; only the axes, labels, colors, and graphical marks are available.
- No workbook, formula, cached workbook value, spreadsheet, CSV, DOC/DOCX, or Office-cell/paragraph source is assigned in this part.
