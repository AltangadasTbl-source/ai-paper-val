# Cross-Source Consistency Review

## Scope and method

This checker reviewed every current 1.5.1 mapped result-relevant relationship for a repeat or a possible comparator across the abstract, Key Points, narrative, Tables 1-5, Figures 1-2, captions and footnotes in DOC-001; the protocol definitions in DOC-002; and eMethods, eTables, and eFigures in DOC-003. The current mapping inputs were `extraction/main_quantitative_evidence.md`, `extraction/support_quantitative_evidence.md`, `relationships/parts/main_numeric_relationships.md`, `relationships/parts/support_numeric_relationships.md`, `statistics/parts/main_statistical_relationships.md`, and `statistics/parts/support_statistical_relationships.md`. Direct PDF pages cited below were checked by native extraction and targeted rendered-page inspection. Reused OCR/text was used only to locate material.

Every comparison was first matched for population, analysis set, time, contrast, endpoint, model, effect measure, scale, unit, reference group, and displayed precision. A different result was not treated as a proposal where any of those attributes did not match.

## Coverage record

- **Matched or potentially matched relationship groups checked:** 22.
- **Matched repetitions with no cross-source discrepancy identified:** 15.
- **Non-comparable apparent differences recorded, not proposed:** 5.
- **Distinct qualifying proposals:** 2.
- **Status of every proposal in this artifact:** Pending Human Adjudication.

The two direct sources are scientifically different studies: DOC-001 is the STOP-PD II randomized trial of sertraline plus olanzapine versus sertraline plus placebo in persons with psychotic depression; DOC-002 and DOC-003 are an aspirin primary-prevention meta-analysis protocol and supplement. Their populations, interventions, outcomes, and analysis structures do not match. No number was compared between DOC-001 and DOC-002/DOC-003 as if it were a repeated study result.

## Qualifying proposals

### Proposal 1 — HbA1c daily-rate result is labeled mg/dL in text but percent in the source table

**Category:** Measure, label, or scale inconsistency.

**Exact source locations:**

- [DOC-001, abstract, PDF p. 1](../../../jama_flint_2019_oi_190079.pdf#page=1): the randomized population and treatment-by-linear-time result are reported as “HbA1c levels (−0.0002 mg/dL; 95% CI, −0.0021 to 0.0016).”
- [DOC-001, Results narrative, PDF p. 7](../../../jama_flint_2019_oi_190079.pdf#page=7): the same treatment-by-linear-time result is repeated as “HbA1c levels (−0.0002 mg/dL [95% CI, −0.0021 to 0.0016], adjusted P = .99).”
- [DOC-001, Table 4, PDF p. 8](../../../jama_flint_2019_oi_190079.pdf#page=8): the corresponding analyte is printed as “HbA1c, %,” with baseline and termination values such as 5.9 (1.5), 5.7 (1.1), and a within-group difference of −0.2 (−0.5 to 0.2).

**Printed-values comparison:** The abstract and narrative agree with each other on the estimate and interval, but each prints the unit as `mg/dL`. The table explicitly identifies HbA1c as `%`; the table’s displayed HbA1c values are on the percent scale rather than a mass-concentration scale.

**Comparison logic:** The population (126 randomized participants), intervention contrast (continued olanzapine versus placebo with sertraline), outcome (HbA1c), and randomized-period context match. The comparison is limited to the outcome unit/scale; Table 4's unadjusted baseline-to-termination values are not treated as a numerical comparator for the adjusted treatment-by-time estimate. HbA1c is identified as percent in the directly displayed table, whereas the same trial result is labeled mg/dL in two summary-text occurrences. The printed texts therefore contain an unresolved unit/scale conflict, independent of any difference between the analyses.

**Supported alternatives:** The `mg/dL` labels in the abstract and narrative could be a repeated unit-labeling error, while the Table 4 `%` label could be the intended unit. Conversely, a human reviewer should confirm whether any laboratory-specific transformation or reporting convention in the supplied source supports mg/dL. The source does not provide such a transformation or convention on these pages.

**Human verification steps:**

1. Open the three cited direct PDF pages and confirm the HbA1c unit and all printed digits against the publisher PDF.
2. Confirm in the study’s analysis output or author-approved source whether the treatment-by-time coefficient was modeled on HbA1c percentage points per day.
3. Determine whether `mg/dL` in the abstract and Results text should be aligned to the Table 4 percent unit, and preserve the displayed estimate and precision unless a source-backed correction establishes otherwise.

### Proposal 2 — ASCEND is marked not included for all-stroke analysis but appears in the total-stroke forest plot

**Category:** Cross-document numeric inconsistency; Measure, label, or scale inconsistency.

**Exact source locations:**

- [DOC-003, eTable 1, PDF p. 9](../../../joi180151supp2_prod.pdf#page=9): the ASCEND row under `All strokes` says “Not included in analysis – only reports ischemic stroke.” The same row identifies ASCEND's primary stroke definition as ischemic only.
- [DOC-003, eTable 4, PDF p. 16](../../../joi180151supp2_prod.pdf#page=16): `Total stroke outcomes` reports 12 studies, aspirin 1,116/73,883 and no aspirin 1,136/72,317 for all participants.
- [DOC-003, eFigure 4, PDF p. 24](../../../joi180151supp2_prod.pdf#page=24): the `Total stroke` frequentist forest plot visibly includes an `ASCEND` row of 240/7,740 versus 263/7,740 (RR 0.91 [0.77; 1.08]) and reports 13 displayed study rows totaling 81,623 and 80,057.
- [DOC-002, protocol change, PDF p. 7](../../../joi180151supp1_prod.pdf#page=7): the protocol says ASCEND's stroke events in its primary cardiovascular outcome are exclusively ischaemic, unlike the other studies' primary-composite stroke definitions.

**Printed-values comparison:** eTable 4's 12-study totals differ from eFigure 4's 13-row totals by exactly 7,740 participants in each arm: 81,623 − 73,883 = 7,740 and 80,057 − 72,317 = 7,740. These are the displayed ASCEND per-arm totals in the forest plot. eTable 1 explicitly says that ASCEND reports only ischaemic stroke and is not included in the all-strokes analysis, yet eFigure 4 displays the ASCEND ischaemic-stroke counts in the panel headed `Total stroke`.

**Comparison logic:** The compared supplement locations all concern aspirin versus no aspirin and a total/all-stroke endpoint in the overall trial set. The comparison keeps the models separate: eTable 4 reports a 12-study Bayesian HR/CrI result, while eFigure 4 reports a 13-row frequentist RR/CI result; their effect estimates are not compared as interchangeable. The qualifying conflict is instead the endpoint-membership and count identity: the eFigure's added participants are precisely the ASCEND row that eTable 1 states is unavailable for all-stroke analysis because it reports only ischaemic stroke. No supplied page explains a distinct endpoint convention permitting the ischemic-only ASCEND row in the forest plot labelled `Total stroke`.

**Supported alternatives:** The forest plot may intentionally use a frequentist endpoint definition that permits ASCEND's ischaemic-only stroke count, whereas eTable 4 uses a stricter all-stroke Bayesian endpoint; the eFigure caption does not state that distinction. Alternatively, the total-stroke forest plot may have included ASCEND contrary to the eTable 1 endpoint definition. The protocol statement is limited to ASCEND's exclusion from the *primary cardiovascular outcome*, so it does not by itself resolve which interpretation governs the total-stroke forest plot.

**Human verification steps:**

1. Confirm the ASCEND row, its 240/7,740 and 263/7,740 counts, the 13 plotted rows, and the 81,623/80,057 totals directly on DOC-003 p. 24.
2. Confirm the exact `All strokes` cell for ASCEND on DOC-003 p. 9 and the 12-study totals on p. 16.
3. Inspect the frequentist-analysis dataset/code or author-approved outcome-extraction record to determine whether the total-stroke forest plot deliberately admitted an ischaemic-only ASCEND endpoint.
4. If the analyses use different endpoint conventions, label that difference explicitly at the forest plot and table; if not, identify which endpoint membership/count vector is intended.

## Matched repetitions with no discrepancy identified

The following were matched for their displayed attributes and showed no cross-location numerical, measure, unit, scale, or reference-group conflict in the supplied source:

1. DOC-001 randomized allocation: 64 olanzapine and 62 placebo (abstract p. 1; Methods p. 4; Figure 1 p. 3; Results p. 6).
2. DOC-001 randomized cohort: 126 participants, mean age 55.3 years (SD 14.9), and 78 women (61.9%) (abstract p. 1; Table 1 p. 5 for arm components).
3. DOC-001 relapse result: 13/64 (20.3%) versus 34/62 (54.8%) (abstract p. 1; Key Points p. 2; Figure 1 p. 3; Results p. 6).
4. DOC-001 primary adjusted treatment effect: HR 0.25 (95% CI 0.13-0.48; P<.001) (abstract p. 1; Results p. 6); Figure 2 p. 7's log-rank P<.001 is directionally and display-precision compatible but is a distinct test rather than a duplicate HR.
5. DOC-001 secondary treatment-by-time values for weight, waist circumference, total cholesterol, LDL, HDL, triglyceride, glucose, and HbA1c: the abstract p. 1 and Results p. 7 repeat the same displayed estimates and intervals. Proposal 1 is the sole unit conflict within this matched set.
6. DOC-001 Figure 1 randomized-branch counts reconcile with the narrative relapse denominators and counts (pp. 3 and 6).
7. DOC-001 Table 2 p. 6 baseline movement-scale labels and values are not used as duplicate incidence estimates for the later Results narrative, which explicitly reports incident akathisia and tardive dyskinesia (p. 7).
8. DOC-001 falls, serious-adverse-event, death, and relapse-hospitalization counts/percentages in the narrative are each attached to their stated randomized or relapse subpopulation; no conflicting duplicate printed value was located (pp. 7-8).
9. DOC-003 eTable 3's NNT/NNH entries are presented only where its own ARD interval excludes null, as stated in its p. 15 footnote.
10. DOC-003 eTable 5 consistently labels its entries as events per 10,000 participant-years (p. 17); no count/risk substitution was identified within that table.
11. DOC-003 eTable 6's `<=100 mg/day` MI upper bound printed as 1.00 is qualified by the p. 18 footnote as 0.9989; this is coherent displayed rounding, not a difference.
12. DOC-003 eFigure 4 labels aspirin as Experimental, no aspirin as Control, and the effect measure as RR with 95% CI (pp. 22-26); these labels are internally consistent across its five panels.
13. DOC-003 eFigure 3 supplies the coherent matched estimate, SE, t statistic, and P-value display for its Egger test (p. 21); no independent cross-source contradiction was found.
14. DOC-002's protocol lists all stroke and all ischaemic stroke as distinct secondary outcomes (p. 2), consistent with the separate endpoint columns in DOC-003 eTable 1 (pp. 7-9).
15. DOC-002's protocol change explains ASCEND's primary-composite exclusion by its ischemic-only stroke definition (p. 7), consistently repeated by DOC-003 eTable 1's endpoint description (p. 9).

## Non-comparable apparent differences and exclusions

1. DOC-001 Table 4 p. 8 reports unadjusted within-group raw baseline-to-termination changes, while the abstract/Results p. 1 and p. 7 report adjusted treatment-by-linear-time interaction estimates. The different estimands, models, and missing-data context preclude a numerical comparison; only the HbA1c unit conflict is proposed above.
2. DOC-001 Table 3 p. 7 reports types of relapse events and permits more than one event per relapse case; it is not a denominator-matched duplicate of the 13 and 34 people who relapsed.
3. DOC-003 eTable 3 p. 15 reports ARD under its stated signed convention and frequentist RR-based method, while eTable 4 p. 16 labels an ARR and reports Bayesian HR/CrI. Their signed absolute-risk values are not treated as competing copies because measure, model, and stated sign convention do not match.
4. DOC-003 eTable 5 p. 17 reports person-time event rates, whereas eTable 4 p. 16 and eFigure 4 p. 24 report event/participant counts. No person-time denominator shared by those displays permits a direct rate/count reconciliation.
5. DOC-003 eTable 6 p. 18 reports Bayesian sensitivity-analysis HR/CrI results in restricted study sets, whereas eFigure 4 pp. 22-26 reports frequentist full-set RR/CI forest plots. Neither population nor model/measure matches.

## Limitations

The supplied package contains no structured dataset, analysis code, author correspondence, or raw outcome-extraction worksheet. The ASCEND proposal therefore remains an endpoint-membership conflict in the printed sources, not a determination of which analysis is correct. This checker did not use web sources, old candidate records, legacy checker conclusions, or final reports.
