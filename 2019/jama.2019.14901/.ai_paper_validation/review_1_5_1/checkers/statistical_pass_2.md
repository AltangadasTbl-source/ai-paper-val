# Statistical Consistency Review — Pass 2

## Scope and method

- **Pass:** 2 of 2, performed by a fresh runtime agent distinct from pass 1.
- **Assigned relationships:** S001-S039 (39/39), using the complete `statistics/relationship_inventory.md`, both statistical part inventories, all three checker artifacts, the then-current stable ledger C001-C005, and `verification/evidence_recheck.md`. The quality-audit repair later appended non-inferential C006; its cross-lane reconciliation is recorded below.
- **Direct-source reread:** main article PDF pp. 1, 4, and 6-8; protocol PDF pp. 30-34; results supplement PDF pp. 2-9. The PDF text was used to re-read the printed values; the recorded visual evidence recheck is the source-page confirmation for C001-C006 after the post-audit C006 append.
- **Checks revisited:** denominator and arithmetic reconciliation, point-estimate containment, interval endpoint ordering, sign/direction, effect measure and scale labels, repeated values, cross-location matches, and the cross-lane/recheck implications. Interval/P-value/test/statistic/SE compatibility was considered only where compatible definitions are supplied. No sidedness, degrees of freedom, covariance, variance estimator, multiplicity method, denominator, model, or estimand mapping was inferred from convention.

## Cross-lane and ledger reconciliation

- **C001:** The direct article mismatch remains tied to S004: prose prints -8.7 percentage points and Table 2 prints -8.5 for the same labelled day-7 respiratory-failure contrast; `70/339 - 88/302 = -8.4901` points is a diagnostic count-derived check consistent with -8.5. The source does not define a distinct prose estimand or denominator.
- **C002:** The direct protocol/article definition mismatch remains tied to S001/S024: pH <7.35 versus pH <7.25 for the same reintubation respiratory-acidosis criterion. Amendment/operational-definition history is not supplied.
- **C003 and C004:** These are numeric-lane eTable 2 fraction/percentage conflicts, not additional inferential relationships. Their fractions, denominators, complementary percentages, and aggregate-table implications were reviewed as cross-lane inputs; they do not create an additional S-based candidate.
- **C005:** The matched nonhypercapnic day-7 result remains tied to S019/S036: main text prints P=.10 and eTable 4 prints P=.1057 with matching population, counts, difference, and CI. A diagnostic uncorrected Pearson calculation can reproduce .1057, but the package does not specify the full subgroup test or main-text display rule; this pass makes no ungrounded conclusion about mechanism.
- **C006 post-audit reconciliation:** C006 was appended after pass 2 from numeric relationship N027. It concerns protocol duration arithmetic (36+12 versus the printed total 51, with an adjacent 3-month participation period) and has no S identifier, inferential statistic, or implication that changes any S001-S039 pass record.

## Relationship-by-relationship pass-2 record

| Stable ID | Pass-2 result |
|---|---|
| S001 | **PASS_2_COMPLETE — C002 cross-lane implication reviewed.** Main/protocol respiratory-acidosis cutoffs differ; final operational definition/amendment is missing. |
| S002 | **PASS_2_COMPLETE — no new candidate.** 590 × 1.10 = 649, compatible with planned 650 after whole-person display; exact power-calculation inputs absent. |
| S003 | **PASS_2_COMPLETE — no new candidate.** Count-derived -6.4 is inside ordered CI and repeats consistently; stated primary chi-square framework supports only diagnostic P compatibility. |
| S004 | **PASS_2_COMPLETE — C001 cross-lane implication reviewed.** Prose -8.7 versus Table 2 -8.5 remains a direct matched-result discrepancy. |
| S005 | **PASS_2_COMPLETE — no new candidate.** -4.8 is count-consistent, contained by ordered CI, and directionally compatible with the stated proportion-comparison framework. |
| S006 | **PASS_2_COMPLETE — no new candidate.** -6.7 is count-consistent, contained by ordered CI, and aligned in direction/scale. |
| S007 | **PASS_2_COMPLETE — no new candidate.** -7.4 is count-consistent and repeated locations agree. |
| S008 | **PASS_2_COMPLETE — no new candidate.** Stay differences are within ordered CIs and use day units; unreported distributional/CI construction prevents treating rounded-median subtraction as a contradiction. |
| S009 | **PASS_2_COMPLETE — no new candidate.** Mortality estimates are contained by ordered CIs and agree with counts/labels; fixed-time and survival constructs were not conflated. |
| S010 | **PASS_2_COMPLETE — no new candidate.** Exploratory differences are count-consistent, contained by ordered CIs, and correctly on percentage-point scale. |
| S011 | **PASS_2_COMPLETE — no new candidate.** Reintubated-patient mortality difference is count-consistent and within ordered CI; small-sample test construction is missing. |
| S012 | **PASS_2_COMPLETE — no new candidate.** 291 - 254 = 37.0 mm Hg, contained by ordered CI; SD-based P approximation remains diagnostic only. |
| S013 | **PASS_2_COMPLETE — no new candidate.** 1.2 points is within ordered CI with direction/scale agreement; event counts and exact test definition are not supplied. |
| S014 | **PASS_2_COMPLETE — no new candidate.** -5.0 hours is within ordered CI; a reported median-difference statistic need not equal subtraction of rounded medians. |
| S015 | **PASS_2_COMPLETE — no new candidate.** 39/41 - 57/59 rounds to -1.5 points and is within ordered CI; exact small-sample test is missing. |
| S016 | **PASS_2_COMPLETE — no new candidate.** -9.7 points is count-consistent and within ordered CI; P<.01 is not a display-zero notation. |
| S017 | **PASS_2_COMPLETE — no new candidate.** Day-7 log-rank P=.02 and monotonically declining at-risk counts are coherent; censoring inputs are absent. |
| S018 | **PASS_2_COMPLETE — no new candidate.** -12.9 is count-consistent and within ordered CI; P=.049/.0489 are compatible precision displays, while Figure 3 labels a separate log-rank test. |
| S019 | **PASS_2_COMPLETE — C005 cross-lane implication reviewed.** Main P=.10 and eTable P=.1057 differ for the matched result; Figure 3 P=.11 is separately labelled log-rank. |
| S020 | **PASS_2_COMPLETE — no new candidate.** Adjusted OR 0.60 lies within 0.38-0.93 and has direction/scale agreement; coefficient and variance details are missing. |
| S021 | **PASS_2_COMPLETE — no new candidate.** Two explicitly distinct post hoc model specifications may share displayed P=.02; no source rule requires different rounded P values. |
| S022 | **PASS_2_COMPLETE — no new candidate.** Chronic-lung-disease counts/percentages and printed P=.02 agree in direction; baseline-test implementation is missing. |
| S023 | **PASS_2_COMPLETE — no new candidate.** Stated 11 prespecified secondary outcomes and six nonsignificant outcomes are not contradicted; adjustment definition is not supplied. |
| S024 | **PASS_2_COMPLETE — C002 cross-lane implication reviewed.** Protocol plan and pH<7.35 criterion were reconsidered against the final article pH<7.25 criterion. |
| S025 | **PASS_2_COMPLETE — no new candidate.** Protocol predictor/adjustment descriptions are prospective plans, not evidence that each model was executed. |
| S026 | **PASS_2_COMPLETE — no new candidate.** Planned Kaplan-Meier/log-rank/Cox framework does not identify an unreported final model mapping. |
| S027 | **PASS_2_COMPLETE — no new candidate.** Planned secondary/mortality methods are not a matched contradiction to final reported analyses. |
| S028 | **PASS_2_COMPLETE — no new candidate.** Prespecified subgroup labels define strata without a conflicting inferential result. |
| S029 | **PASS_2_COMPLETE — no new candidate.** Protocol sample-size hypothesis agrees arithmetically with S002. |
| S030 | **PASS_2_COMPLETE — no new candidate.** Historical-study P values lack a matched current-trial population/contrast/result. |
| S031 | **PASS_2_COMPLETE — no new candidate.** eTable 1 matched outcome P values/counts agree with the main table; overlapping components were not summed. |
| S032 | **PASS_2_COMPLETE — C003/C004 cross-lane implication reviewed; no new S candidate.** eTable 2 baseline P values have no supplied test definition, while the fraction/percentage conflicts are separately stable numeric candidates. |
| S033 | **PASS_2_COMPLETE — no new candidate.** Hypercapnic -12.9 is count-consistent and within ordered CI; .0489 agrees with rounded main display. |
| S034 | **PASS_2_COMPLETE — no new candidate.** Hypercapnic secondary differences are contained by ordered CIs; upper endpoint -0.10 is a negative finite-precision value, not a display-zero issue. |
| S035 | **PASS_2_COMPLETE — no new candidate.** Days and percentage-point measures remain labelled separately and estimates lie within ordered CIs. |
| S036 | **PASS_2_COMPLETE — C005 cross-lane implication reviewed.** Count-derived -5.0 and ordered CI agree; only the matched P-value discrepancy is retained. |
| S037 | **PASS_2_COMPLETE — no new candidate.** Nonhypercapnic secondary values are contained by ordered CIs; upper endpoint 0.0 with P=.0505 is coherent finite-precision endpoint display. |
| S038 | **PASS_2_COMPLETE — no new candidate.** Nonhypercapnic stay/mortality labels, scales, directions, and interval ordering agree; exact tests/SEs are not fully defined. |
| S039 | **PASS_2_COMPLETE — no new candidate.** Unadjusted 90-day survival log-rank P=.37 is not interchangeable with fixed-time Table 2 mortality P=.30. |

## Display-zero review

No assigned relationship prints `P = 0`, `p = 0.000`, or an equivalent literal display zero. S012 (`P<.001`) and S016 (`P<.01`) are not display-zero notation. Accordingly, no `DISPLAY_ZERO_NOT_CANDIDATE` record was needed and no candidate was emitted from P-value formatting.

## Pass-2 outcome and limitations

- **S relationships explicitly completed:** 39/39 (S001-S039).
- **Existing stable candidates at pass-2 execution reconsidered:** 5/5 (C001-C005).
- **Final-ledger reconciliation after quality-audit repair:** 6/6; appended C006 has no inferential-statistical implication and leaves S001-S039 complete.
- **New distinct candidates to append:** 0.
- **APPEND-CAND records:** none.
- **Limitations:** Raw data, analysis outputs, CI-construction details, degrees of freedom, variance estimators, subgroup-test/display conventions, multiplicity procedures, and amendment/operational-definition history are not supplied. Diagnostic arithmetic and Pearson compatibility checks are not replacements for the reported analyses.
