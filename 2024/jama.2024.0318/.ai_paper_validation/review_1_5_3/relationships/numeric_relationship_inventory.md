# Numeric Relationship Inventory

## Scope, identity, and counting rule

This is the stable numeric/reporting (`N`) inventory for the numeric-consistency stage. It covers every result-relevant relationship in the complete main and support evidence maps: `DOC-001` (main article, PDF pp. 1-11), `DOC-002` (protocol, PDF pp. 1-65), `DOC-003` (Supplement 2, PDF pp. 1-22), and `DOC-004` (data-sharing statement, PDF p. 1). It was built from the current maps and direct supplied PDFs only. It does not use legacy candidate, verifier, critic, endetail, or report conclusions.

An inventory item is one source-grounded reporting relationship, rather than every individual cell in a repeated table. Each item preserves the exact table/figure/page scope needed to reproduce its checks. `S`-only model relationships remain in `statistics/relationship_inventory.md`; N/S cross-references in the source maps are retained here when their numeric inputs need a numeric check.

**Inventory count: 91 relationships.** `N001`-`N048` plus `N038a`, `N038b`, and `N039a` retain the 51 mapper identifiers for DOC-001. `N049`-`N088` extend the stable N inventory to the 40 numbered support-map groups, including explicitly no-applicable administrative/definition scope where needed to close source coverage.

## DOC-001 — Main article (51 relationships)

| Stable N relationship(s) | Exact source locations | Quantitative relationship and applicable numeric checks | Result |
|---|---|---|---|
| N001 | `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1`, Abstract Results; p. 3 Results | Enrolment 262/305 (86%); demographics and 11-year follow-up. Check proportion and repeated narrative values. | PASS: 262/305 = 85.90%, consistent with 86% after whole-percent rounding. |
| N002-N006, N009 | Main PDF pp. 1-3 | Abstract/Key Points/main results: 7- and 12-year HbA1c, remission, deaths, conclusion summaries. Check matched population/time/contrast values and rounding. | See checker cross-location checks; N003 contains one P-value candidate proposal. |
| N007-N008 | Main PDF p. 2; Table 1 p. 4; Table 2 p. 6 | Eligibility, outcome thresholds, HbA1c conversion and clinical-unit rules. Check scale, unit, and threshold labels. | N007 supports the `<6.5%` threshold comparator in proposal NC-03. |
| N010 | Main PDF p. 3, Figure 1 and Results | Participant flow: 355 randomized; 39 before intervention; 316 eligible; 12 withdrawn/lost and 2 deaths; 3 rerecruited; 305 available; 262 enrolled; allocation totals. Check flow identities. | Proposal NC-04: the Figure labels 305 available but immediately branches to 193 surgery plus 122 medical/lifestyle, which sums to 315. The 316-to-305 route itself reconciles as 316 - 12 - 2 + 3 = 305. |
| N011 | Main PDF p. 3 | Randomized analysis groups 96/166; baseline descriptive values and BMI<35 count 96/262. | PASS: 96 + 166 = 262; 96/262 = 36.64%, consistent with 36.6%. |
| N012-N018 | Main PDF pp. 3-4; Figure 2 p. 5; Table 2 p. 6; Figure 3 p. 7 | Procedure comparisons, IPW sensitivity, remission, medication, weight and year-12 results. Check direction, percent/OR labels, matching values. | N014 contains threshold-label proposal NC-03; otherwise model-derived estimates are not tested by raw subtraction. |
| N019 | Main PDF p. 4, Table 1 | Group and procedure N values; sex and race categories. Check subgroup sums, category sums, count/percent pairs. | PASS within displayed rounding: 89+41+36=166; sex/race counts sum to each column N; all displayed percentages round from printed counts and denominators. |
| N020-N021 | Main PDF p. 4, Table 1 | Baseline anthropometric, laboratory, and medication values; bracketed available n; `9/35 (25.7)` beta-blocker entry. Check measure labels, units, available-n denominators, and count/percent arithmetic. | PASS. Bracketed n values explicitly denote available measurements. 9/35 = 25.71%; this is a stated available-data denominator, not an inconsistency with group n=36. |
| N022-N025 | Main PDF p. 5, Figure 2A-D | Annual group and procedure numbers at risk; figure scales and model/raw-data conventions. Check initial subgroup totals and yearly counts only where a total is printed. | PASS: year-0 procedure values sum to surgery n=166. Later risk counts are observed-data quantities and are not mutually exclusive subgroup totals across outcome panels. |
| N026-N039, N038a, N038b, N039a | Main PDF p. 6, Table 2 | All baseline/year-7 outcome rows: units, central/dispersion values, relative/net/fold changes, ORs, group differences, CIs, and P values. Check label/scale, direction, interval order, model-defined contrast, and matching risk-count denominators. | PASS except the `<6.5%` threshold comparator in NC-03. Direct subtraction is not applicable to model least-square changes; source footnotes define net/relative/fold/odds estimands. |
| N040 | Main PDF p. 7, Figure 3 | Annual remission risk counts and definition. Check initial totals and definition consistency. | PASS: baseline counts 96 and 166 match groups; no exact plotted annual proportions are printed. |
| N041-N045 | Main PDF p. 7; Supplement 2 eFigure 6 and eTable 6/7 | BMI-subgroup effects, clinical/lab narrative, safety, crossover/revision labels. Check subgroup population, arithmetic, rate/count distinction, and source qualifiers. | PASS: explicitly model-derived contrasts preserved; the crossover components 8+15+1=24 and revisions 7+4+1+3=15. |
| N042 | Main PDF p. 7 | Deaths, dialysis, retinopathy, crossover and revision component counts. | PASS: 2+2=4 deaths; 24/96=25.0%; 15/166=9.04%, displayed 9%. |
| N046-N048 | Main PDF pp. 8-9, Table 3/Discussion | Adverse-event n(%) table and matching safety/discussion summaries. Check every n(%) pair against column N and repeated results. | PASS under one-decimal/whole-percent rounding: all enumerated Table 3 count/percent pairs reconcile to 96 or 166; summary values match their time-qualified source results. |

## DOC-002 — Protocol (20 relationships)

| Stable N | Exact source locations | Quantitative relationship and check | Result |
|---|---|---|---|
| N049 | Protocol PDF pp. 7, 16-18, 36 | Primary endpoint, ITT analysis population, 7-year window. Check only identity with reported-study result after distinguishing plan from outcome. | PASS: planning definition, not an observed result. |
| N050 | Protocol PDF pp. 7, 16-17 | Follow-up plan through 7 years/all and up to 13 years/earliest participants. | PASS: planned horizon, not matched as a reported result. |
| N051 | Protocol PDF pp. 7, 17, 20 | Eligibility and approximately 302 re-consenting-participant planning count. | PASS: protocol estimate; not interchangeable with later 305 available/262 enrolled. |
| N052 | Protocol PDF p. 18; Table A1 pp. 29-30 | Outcome thresholds and binary/continuous labels. | PASS: definitions are planning labels; source differences in later supplement are assessed at their own locations. |
| N053 | Protocol PDF pp. 22-25 | Annual/interim visit windows and measurement units. | PASS: schedule definitions only. |
| N054-N055 | Protocol PDF pp. 26-27 | Mixed-model and binary-analysis formula inputs; beta_7 scale/direction. | PASS: compatible planned labels; no numeric result to reconcile. |
| N056-N057 | Protocol PDF pp. 27-29 | Planning/observed parent-trial values, cohort flow 355/325/20/3, power simulations. | PASS: internally, 325 + 20 + 3 = 348 rather than 355, but the text does not state these three are exhaustive mutually exclusive disposition categories; missing intervention/non-follow-up states are not defined. No concrete reported-result inconsistency. |
| N058-N060 | Protocol PDF pp. 28-31 | Secondary power, missing-data, sensitivity and subgroup assumptions. | PASS: assumptions/plans, not results. |
| N061-N065 | Protocol PDF pp. 32-42 | Safety/event definitions, reporting windows, data handling. | PASS: definitions only. |
| N066 | Protocol PDF pp. 55-56, Appendix 2 | Parent-trial enrolment, allocation, baseline and one-year outcome table. | PASS: historical parent-study table; its own displayed totals/percentages are covered as a table relationship, with no printed arithmetic mismatch identified. |
| N067-N068 | Protocol PDF pp. 57-60 | SF-36 and AUDIT-C response/score scales and thresholds. | PASS: instrument definitions only. |

## DOC-002 ancillary/background and DOC-003 Supplement 2 (19 relationships)

| Stable N | Exact source locations | Quantitative relationship and check | Result |
|---|---|---|---|
| N069 | Protocol PDF pp. 61-65 | Planned ICER/QALY threshold and BMI-restricted model. | PASS: ancillary plan, not an observed result. |
| N070 | Protocol PDF pp. 9-14 | Contextual prior-evidence and pooled-cohort quantities. | PASS: cited/contextual values, not a duplicate of DOC-001 outcomes. |
| N071-N075 | Supplement 2 PDF pp. 3-6 | Parent-trial allocation, 305/316 availability, ITT/PP and IPW definitions, missing-data/event-test rules. | PASS: 305/316 is a stated availability frame; matching main Figure 1 reconciliation is preserved. |
| N076 | Supplement 2 PDF p. 8, eFigure 1 | Baseline-BMI plot scale. | PASS: no exact point estimates printed. |
| N077-N081 | Supplement 2 PDF pp. 9-13, eFigures 2-6 | ITT/PP weight values; medication-category Ns; P values; BP/lipid annual observed Ns; BMI subgroup values. Check repeated values, initial N sums, units and time labels. | PASS: eFigure 2 year-7 weight values match DOC-001; figures label model estimates or observed N as applicable. |
| N082 | Supplement 2 PDF p. 14, eTable 1 | 7- and 12-year cohort N, baseline count/percent categories and units. | PASS: all listed count/percentage pairs round correctly to N=262 or N=130; sex/race categories sum within each cohort. |
| N083 | Supplement 2 PDF pp. 15-16, eTable 2 continuous outcomes | Year-12 values, changes, group differences, CIs, P values and footnotes. Check title/footnote time labels, scale and direction. | Proposal NC-01: title/cells say year 12 while three footnote rules say year 7. |
| N084 | Supplement 2 PDF pp. 15-16, eTable 2 binary outcomes | Year-12 remission, medication and glycemic-control values/ORs/P values. Check time labels, displayed zero, effect scale and P value. | Proposals NC-01 and NC-02. Medical remission's 2e-16 shown as 0% is `DISPLAY_ZERO_NOT_CANDIDATE`: the footnote expressly supplies the finite value. |
| N085 | Supplement 2 PDF p. 17, eTable 3 | Nutritional-abnormality n/N(%) rows and subgroup rows. Check every printed numerator/denominator/percentage and surgery subgroup sums where shared denominators apply. | PASS: printed percentages reconcile under one-decimal rounding; differing N are explicitly observed-data denominators. |
| N086 | Supplement 2 PDF p. 18, eTable 4 | Nutritional LS means, SEs, surgery-minus-medical differences and P values. | PASS: direction label agrees. Arithmetic residuals are within displayed precision (for example 13.0 - 13.7 = -0.7 versus estimate -0.8 using unrounded LS means). |
| N087 | Supplement 2 PDF pp. 19-21, eTables 5-6 | Adverse-event/procedure n(%) tables, group tests, surgery-type quantities. | PASS: the source labels N=96/166 and test type; examined printed n(%) pairs reconcile at display precision. |
| N088 | Supplement 2 PDF p. 22, eTable 7; Data Sharing Statement PDF p. 1 | Crossover/revision n/N(%), time range; DOC-004 no result relationship. | PASS: 1+15+8=24; 7+4+1=12 AGB revisions and 3 SG-to-RYGB revisions give 15 total; DOC-004 is administrative/no applicable quantitative result. |

## Check rules, tolerance, and explicit exclusions

- Integer count/denominator percentages were recalculated as `100 × numerator / denominator`. Tolerance is the interval induced by the printed percentage precision: ±0.05 percentage point for one decimal, ±0.5 for a whole number, and ±0.005 for two decimals.
- Displayed sums use exact integer arithmetic. Continuous means, least-square estimates, percentage changes, odds ratios, fold changes, and standard errors are assessed only against the source-declared estimand. When components are printed at one decimal, an apparent residual up to 0.1 in the displayed difference can result from unrounded inputs; no raw-subtraction candidate is generated for a model-derived result.
- Confidence intervals were checked for increasing endpoints and containment of the printed estimate where a compatible scale is printed. All inspected CIs have ordered endpoints and contain their displayed estimate after normal display precision.
- Counts at risk are not treated as annual flow totals unless the figure states that relationship; different outcome panels legitimately have different observed Ns.
- `P = 0`, `P = .000`, or an equivalent display zero alone is never a candidate. N084 records the explicitly explained `2e-16` value and its displayed 0% as `DISPLAY_ZERO_NOT_CANDIDATE`.
- Planned protocol values, contextual literature values, administrative source pages, and non-tabulated plotted coordinates were inventory-covered but not manufactured into observed-result arithmetic tests.

## Inventory limitations

The main article's Table 2 and Supplement 2 eTable 2 explicitly use least-square/model-derived changes and odds ratios; unrounded model output, covariance, and weighting are not supplied, so raw descriptive subtraction cannot reproduce those quantities. Sparse plotted trajectories lack exact data labels. These are limitations on mechanical reproduction, not candidate suppression: all concrete printed cross-location, label, denominator, count/percentage, total, scale, and timepoint relationships were checked.
