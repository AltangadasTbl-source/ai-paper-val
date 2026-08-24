# Cross-source quantitative consistency check

## Scope, source basis, and matching rule

This checker reviewed the complete canonical relationship set: numeric/reporting relationships `N001` through `N055` and inferential-statistical relationships `S001` through `S031`. It used only the current-run extraction maps, relationship inventories and freshly prepared native/layout text for DOC-001 through DOC-006. No prior audit derivative, external source, web material, renderer substitute, OCR substitute, or structured-data file was used.

Before comparing printed material, each possible match was checked for population/analysis set, time window, intervention contrast, outcome definition, model or test, effect measure, scale, units, reference group, and displayed precision. Planned protocol/SAP material was not compared as an observed result unless it stated the same final analysis definition. A different analysis set (for example, modified intention-to-treat versus per-protocol), a different summary statistic (mean versus median), or a different estimand (risk ratio versus hazard ratio) was not treated as a numerical conflict.

## Complete cross-source coverage

| Canonical relationships reviewed | Matched locations and comparison coverage | Result of cross-source comparison |
|---|---|---|
| N001-N006; S001-S003 | DOC-001 abstract, methods, flow figure, narrative, Table 3 footnotes; DOC-002 protocol; DOC-003 change history; DOC-004 SAP; DOC-005 eMethods | Population, allocation/analysis totals, assigned PEEP/tidal volume, outcome window, thresholds, sample-size chronology and final primary-analysis definitions were checked. Protocol history was separated from final analysis. The final primary alpha of .044 is concordant between DOC-001 p. 4 and DOC-004 p. 2; the generic .05 wording in DOC-001 applies to other tests and is not a conflicting primary threshold. No qualifying candidate from these relationships. |
| N007-N016 | DOC-001 Table 1, Figure 2 subgroup denominators, and related eligibility/ARISCAT material in DOC-002 pp. 10, 29 and DOC-005 pp. 18, 22 | Baseline percentages reconcile to their stated denominators at displayed precision. Figure 2 uses defined subgroup denominators, rather than the full modified intention-to-treat total, where appropriate. ARISCAT score values and the >=26 threshold match across support sources. No qualifying candidate. |
| N017-N027; S004-S006 | DOC-001 narrative/Table 2 and DOC-005 eTables 3-6; DOC-002/DOC-005 intervention and rescue definitions | Intervention levels, units, and arm denominators match. Repeated total-fluid P value (.79), crystalloid-amount P value (.97), vasoactive-use values (491/989 [49.6%] versus 439/987 [44.5%], P=.02), and general surgery/anesthetic descriptions match when the same outcome is displayed. Mean amounts in eTable 3 and median volumes in Table 2 are different summary statistics and were not compared as interchangeable values. One repeated same-count P value is recorded below. |
| N028-N037; S007-S014 | DOC-001 abstract, Key Points, results narrative, Table 3, Figure 2, discussion, and DOC-005 eTables 7-9/eFigures 8-12 | The primary modified intention-to-treat PPC result is repeated as 211/989 (21.3%) versus 233/987 (23.6%), difference -2.3% (95% CI -5.9% to 1.4%), RR 0.93 (95% CI 0.83 to 1.04), P=.23. Per-protocol eTable 8 and sensitivity eTable 9 use expressly different analysis sets/models and were not compared to that risk ratio as identical results. Time-to-event eFigures use hazard ratios and are not conflicting with the Table 3 risk ratios. The abstract-to-Table 3 hypoxemia interval and eFigure 11 outcome label are recorded below. |
| N038-N042; S015-S018 | DOC-002 protocol, DOC-003 protocol-change record, DOC-004 SAP, DOC-001 final methods | Original and revised sample-size plans, interim looks/boundaries, and the shift from earlier protocol wording to the finalized SAP were checked as time-stamped planned definitions. The 1912 maximum plus 5% dropout = 2013 enrollment plan matches DOC-002/DOC-003 and the final 2013 randomized count. No qualifying candidate. |
| N043-N049; S019-S026 | DOC-005 eTables 1 and 3-9 against DOC-001 Tables 1-3 and narrative | ARISCAT table values, arm size (989/987), need for vasoactive drugs, fluid categories, and outcome totals were checked. Pain/dyspnea tables have daily observed denominators and no same-value counterpart in the main article beyond a qualitative comparability statement. Per-protocol and model-specific sensitivity values are explicitly separate from the main modified intention-to-treat estimates. One synthetic-colloid P-value discrepancy is recorded below. |
| N050-N054; S027-S031 | DOC-005 eFigures 1-12, captions/legends, DOC-001 results/Table 3, DOC-006 availability statement | eFigures 1-7 and 12 supply series definitions/captions but no recoverable plotted coordinates in fresh text; no numeric comparison was invented. eFigures 8-10 have outcome-specific hazards and rates matching the corresponding main outcome counts at displayed precision, without treating HR and RR as the same measure. eFigure 11's title and mortality statistic match the main mortality result, but its body text names another outcome; this is recorded below. DOC-006 supplies no outcome data. |

**Coverage count:** 55 of 55 `N` relationships and 31 of 31 `S` relationships reviewed; six direct sources reviewed; three distinct qualifying provisional candidates recorded. The remaining repeated quantitative material was either concordant at displayed precision or was not a like-for-like result after the stated matching rule.

## Qualifying provisional candidates

### XS-001 — Abstract hypoxemia confidence-interval upper limit lacks the negative sign shown in the results table

**Category:** Cross-document numeric inconsistency.

**Exact source locations:** [DOC-001 abstract — PDF p. 1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1); [DOC-001 Table 3 — PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9).

**Matched result:** Intraoperative hypoxemia among the same modified intention-to-treat population (high PEEP n=989 versus low PEEP n=987), with the same high-minus-low percentage-point contrast and 95% confidence interval.

**Printed values:** The abstract reports 5.0% versus 13.6%, difference -8.6% (95% CI, -11.1% to **6.1%**), P<.001. Table 3 reports hypoxemia as 49 (5.0%) versus 134 (13.6%), difference -8.6% (95% CI, -11.1% to **-6.1%**).

**Comparison logic:** The identical arm percentages and point difference identify the same outcome, population, contrast, and scale. A high-minus-low difference of -8.6 percentage points with a wholly negative interval is consistent with the Table 3 upper endpoint of -6.1%, not with the positive 6.1% printed in the abstract. The differing sign is not explainable by display precision because it changes the interval side of zero.

**Supported alternatives:** The abstract may have lost a typographic minus sign during production, or the table may be the intended canonical display. The supplied sources do not establish which production version governs; the observation concerns the two printed displays only.

**Human verification steps:** Open the supplied DOC-001 PDF at p. 1 and p. 9; verify the minus sign before the abstract upper endpoint and Table 3 upper endpoint; confirm both locations refer to intraoperative hypoxemia, high minus low PEEP, and the modified intention-to-treat denominators; then consult the final production record to establish the intended abstract interval.

### XS-002 — Same synthetic-colloid use counts have different displayed P values in the main table and supplement

**Category:** Cross-document numeric inconsistency.

**Exact source locations:** [DOC-001 Table 2 — PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8); [DOC-005 eTable 3 — PDF p. 24](../../../joi190055supp4_prod_16092.pdf#page=24).

**Matched result:** Synthetic-colloid use during surgery in the same modified intention-to-treat arms, high PEEP n=989 versus low PEEP n=987; binary use measure, high-minus-low percentage-point contrast.

**Printed values:** DOC-001 Table 2 prints 74 (7.5%) versus 56 (5.7%), difference 1.8% (95% CI, -0.3% to 4.0%), **P=.09**. DOC-005 eTable 3 prints the same 74 (7.5%) versus 56 (5.7%), **P=.10**.

**Comparison logic:** Population, intraoperative period, contrast, numerator/denominator, percentage scale, and displayed two-decimal P-value precision all match. The two locations therefore present the same binary-use result but two different rounded P values. This is distinct from the eTable's immediately following amount row (50 [211] versus 35 [171], P=.09), which is a different mean-amount measure and is not the comparator.

**Supported alternatives:** The values may arise from different unnamed tests, continuity corrections, or calculation/rounding pipelines; the source package does not state a row-specific test in either location. If different tests were intentionally used, the result is a labeling/definition clarification rather than a transcription difference.

**Human verification steps:** Inspect the supplied PDF table headers and footnotes on DOC-001 p. 8 and DOC-005 p. 24; confirm that each P value belongs to the binary `Synthetic colloids, No. (%)` row rather than the amount row; obtain the prespecified or analysis-program test for this binary comparison; reproduce it from 74/989 versus 56/987 and determine which displayed precision follows the stated method.

### XS-003 — eFigure 11 title and mortality statistic conflict with its body-text outcome label

**Category:** Measure, label, or scale inconsistency.

**Exact source locations:** [DOC-005 eFigure 11 — PDF p. 41](../../../joi190055supp4_prod_16092.pdf#page=41); [DOC-001 Table 3, post hoc mortality — PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).

**Matched result:** Five-day mortality in the modified intention-to-treat high- versus low-PEEP comparison, assessed with a time-to-event hazard ratio.

**Printed values:** eFigure 11 is titled `Probability of death in the first 5 postoperative days` and prints 0.5% versus 0.3%, `hazard ratio for 5-day mortality, 1.67; 95% CI 0.40 to 6.97; P=.484`. Its body sentence instead states that the rate is for `postoperative extra-pulmonary complications`. DOC-001 Table 3 reports five-day mortality as 5 (0.5%) versus 3 (0.3%), HR 1.67 (95% CI 0.40 to 6.97), P=.48.

**Comparison logic:** The eFigure title, hazard-ratio label, rates, interval, and P value match the main-paper five-day mortality result at displayed precision. They cannot describe postoperative extrapulmonary complications, whose main-paper rates are 16.9% versus 15.2% and whose eFigure 10 HR is 1.12 (95% CI 0.89 to 1.39), P=.314. Thus the eFigure 11 body-text outcome label conflicts with its own displayed measure and with the matched main result.

**Supported alternatives:** The phrase `postoperative extra-pulmonary complications` in eFigure 11 may be a carryover from eFigure 10, while the mortality title/statistics may be intended. The package does not establish whether any underlying figure curve is also mislabeled because its plotted coordinates are not recoverable from fresh text.

**Human verification steps:** Open DOC-005 pp. 40-41 and DOC-001 p. 10; verify eFigure 10's extrapulmonary-complication values and eFigure 11's death title, body sentence, and mortality hazard ratio; confirm the main Table 3 mortality row; inspect the original figure labels/curve legend and final supplement production files to determine the intended outcome label.

## Noncandidate records and limitations

- The protocol's .05 design language and the SAP/main article's final .044 primary-outcome alpha were checked with their time and purpose matched. DOC-001 p. 4 explicitly states the .044 primary threshold, and DOC-004 p. 2 states the same threshold; this is not a candidate.
- The main primary PPC risk ratio (0.93) and eFigure 8 time-to-PPC hazard ratio (0.88) have the same population/window but different estimands and models. The values were not treated as conflicting.
- Main modified intention-to-treat estimates and eTable 8 per-protocol estimates have different analysis sets; eTable 9 random-effect, proportional-odds, GEE, and average-relative-effect values have different models/scales. They were not compared as repeated identical results.
- eFigures 1-7 and 12 could be checked for printed labels, captions, model descriptions, and available result text, but their plotted coordinates/P values are unavailable in the fresh text assets and no current-run renderer/OCR tool is available. No coordinate-level cross-source claim was made.
- No coherent finite-precision `P=0` or equivalent display-zero P value was encountered as a basis for a candidate.

**Checker limitation:** Fresh native/layout extraction partly scrambles Table 2 p. 7 and Table 3 p. 9 column alignment. This checker used only rows whose identity and comparator are explicitly recoverable in the fresh text and did not infer row-to-column assignments from the scramble.
