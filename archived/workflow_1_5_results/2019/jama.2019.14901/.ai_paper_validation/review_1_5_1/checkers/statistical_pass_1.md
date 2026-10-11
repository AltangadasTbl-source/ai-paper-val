# Statistical Consistency Review — Pass 1

## Scope and method

- **Pass:** 1 of 2, independent statistical review.
- **Assigned relationships:** S001-S039 (39/39), mapped in `statistics/relationship_inventory.md` and its main/support parts.
- **Evidence used:** the supplied direct PDFs, with the mapper and numeric relationship inventories used as locators and crosswalks. Direct source checks covered the main article at PDF pp. 1, 4, and 6-8; protocol Supplement 1 at PDF pp. 33-34; and Supplement 2 at PDF pp. 2-4 and 6-9.
- **Checks applied where source-supported:** point-estimate containment; interval endpoint order; sign/direction, contrast, scale and label agreement; count/denominator arithmetic; matched cross-location repetitions; duplicate-value checks; and interval/P/test/statistic/SE compatibility only where the supplied source identifies compatible inferential definitions.
- **Boundary:** No test sidedness, degrees of freedom, covariance, variance estimator, CI-construction method, multiplicity adjustment, or unstated model/estimand mapping was inferred. Any numerical approximation below is explicitly diagnostic only.

## Provisional statistical candidates

These are pass-1 observations for later stable-ID registration and mechanical source recheck. They do not assign severity, validity, acceptance, correction, or any disposition.

### STAT1-CAND-001 — Matched day-7 respiratory-failure absolute difference differs across main-article locations

- **Relationship:** S004 / MAIN-S004.
- **Category:** Statistical reporting inconsistency.
- **Exact source locations:** `jama_thille_2019_oi_190108.pdf#page=1`, Abstract Results; `jama_thille_2019_oi_190108.pdf#page=6`, Results; `jama_thille_2019_oi_190108.pdf#page=8`, Table 2.
- **Direct observation:** The abstract and Results text print a day-7 postextubation respiratory-failure difference of **-8.7%** (95% CI -15.2% to -1.8%; P = .01). Table 2, for the same outcome, arms, day-7 window, CI, and P value, prints **-8.5%** (95% CI -15.2% to -1.8%; P = .01), alongside 88/302 (29%) for HFNO alone and 70/339 (21%) for HFNO with NIV.
- **Comparator and rule:** For the displayed arm order, the count-derived risk difference is 70/339 - 88/302 = -0.0849, or **-8.5 percentage points** to one decimal. The Table 2 value is consistent with this calculation; -8.7 is a distinct printed value for the matched result.
- **Observation versus inference:** The differing printed values are direct observations. The calculation is a diagnostic reproduction from the supplied counts; it does not identify the production mechanism for the narrative value.
- **Alternative source-grounded interpretation:** The package’s correction notice says that some current-version outcome data were corrected, but it does not identify this value or furnish a prior value. The two prose locations may share a retained transcription value while the table reflects the count-derived value.
- **Exact human question:** Which absolute difference was intended for the day-7 respiratory-failure result in the supplied corrected version, and should the abstract and Results text be reconciled with Table 2 and its displayed counts?

### STAT1-CAND-002 — Matched nonhypercapnic day-7 reintubation P values differ between the main article and eTable 4

- **Relationship:** S019 / MAIN-S019 and S036 / SUPPORT-S013.
- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** `jama_thille_2019_oi_190108.pdf#page=7`, subgroup Results; `joi190108supp2_prod.pdf#page=7`, eTable 4.
- **Direct observation:** The main Results text gives the nonhypercapnic day-7 reintubation comparison as 13% with HFNO plus NIV versus 18% with HFNO alone, difference -5.0% (95% CI -11.2% to 1.1%), **P = .10**. eTable 4 gives the same subgroup, outcome, arm counts (35/276 versus 45/254), difference, and CI, but prints **P = .1057**.
- **Comparator and rule:** These are distinct printed P values attached to the same matched population, contrast, endpoint, and displayed effect/CI. The main article states that reintubation proportions at the predefined times were compared by chi-square, but eTable 4 does not restate the calculation convention used for its P column. The observation is therefore a cross-location P-value discrepancy, not a claim that a particular unstated rounding convention must apply.
- **Observation versus inference:** The two printed P values and the matched result identity are direct observations. A diagnostic check of the counts is compatible with a two-group proportion comparison but cannot establish the exact calculation, continuity handling, or main-text display rule from the package alone.
- **Alternative source-grounded interpretation:** The main text may use a different display precision, truncation rule, or a separately generated analysis output; none of those explanations is specified in the supplied sources.
- **Exact human question:** Were P = .10 and P = .1057 intentionally generated or displayed under different documented conventions for this same subgroup comparison, or should one source location be amended to match the other?

### STAT1-CAND-003 — Respiratory-acidosis cutoff in the reintubation definition differs between protocol and main article

- **Relationship:** S001 / MAIN-S001 and S024 / SUPPORT-S001; related definition records MAIN-N004 and SUPPORT-N009.
- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** `jama_thille_2019_oi_190108.pdf#page=4`, Outcomes; `joi190108supp1_prod.pdf#page=30`, section 5.4 continuing on PDF p. 31.
- **Direct observation:** For severe respiratory failure leading to reintubation, the main article requires at least two criteria and defines respiratory acidosis as **pH <7.25** with PaCO2 >45 mm Hg. The protocol’s reintubation definition requires at least two criteria and defines respiratory acidosis as **pH <7.35** with PaCO2 >45 mm Hg.
- **Comparator and rule:** These source locations describe the same named reintubation respiratory-failure criterion, retain the same PaCO2 threshold and two-criteria structure, but print nonidentical pH thresholds. The thresholds are numerically and clinically distinct; this is not a display-precision issue.
- **Observation versus inference:** The printed thresholds are direct observations. Whether the final threshold reflects a prespecified protocol amendment, an intentional published-analysis change, or a reporting discrepancy cannot be inferred from the supplied sources.
- **Alternative source-grounded interpretation:** The main article may have used a later or amended criterion than protocol version 4, dated October 17, 2017. No supplied amendment or explanation linking the two definitions was located.
- **Exact human question:** Was the pH threshold intentionally changed from <7.35 to <7.25 before final analysis, and if so, where is that amendment or rationale documented; otherwise, which threshold governed reintubation ascertainment in the reported trial?

## Relationship-by-relationship pass-1 record

| Stable ID | Pass-1 result |
|---|---|
| S001 | **PASS_1_COMPLETE — STAT1-CAND-003.** The main final-outcome definition sets respiratory acidosis for reintubation at pH<7.25, whereas the matched protocol definition is pH<7.35; the chi-square test statement itself is a plan record. |
| S002 | **PASS_1_COMPLETE — no candidate.** Planned 590 participants, 80% power, 8-point difference (18% versus 10%), alpha .05, and 10% inflation to 650 are internally coherent (590 × 1.10 = 649, displayed as 650). Exact power-calculation inputs beyond those printed are unavailable. |
| S003 | **PASS_1_COMPLETE — no candidate.** 40/339 - 55/302 = -6.4 points to one decimal; the estimate lies within ordered CI -12.0 to -0.9, sign/arm direction agree, and all main locations match. The stated primary chi-square test supports a diagnostic P-consistency check; the printed P=.02 is compatible at displayed precision, while CI construction is not specified. |
| S004 | **PASS_1_COMPLETE — STAT1-CAND-001.** The matched prose difference -8.7 conflicts with Table 2’s -8.5 and the displayed-count diagnostic; interval, P, direction, and endpoint ordering otherwise agree. |
| S005 | **PASS_1_COMPLETE — no candidate.** 24/339 - 36/302 = -4.8 points to one decimal; CI -9.6 to -0.3 contains the estimate and is ordered. The predefined reintubation-proportion chi-square framework makes P=.04 directionally compatible; exact CI method is absent. |
| S006 | **PASS_1_COMPLETE — no candidate.** 30/339 - 47/302 = -6.7 points to one decimal; ordered CI -11.9 to -1.7 contains the estimate and P=.009 is compatible with the stated proportion-comparison framework at display precision. |
| S007 | **PASS_1_COMPLETE — no candidate.** 41/339 - 59/302 = -7.4 points to one decimal; all repeated main locations agree and the ordered CI -13.2 to -1.8 contains the estimate. |
| S008 | **PASS_1_COMPLETE — no candidate.** Both length-of-stay differences lie within ordered CIs and directions agree with the arm-specific medians. A difference based on full distributions need not equal a subtraction of rounded medians; the source does not state the CI/test construction for these values. |
| S009 | **PASS_1_COMPLETE — no candidate.** Each displayed mortality difference is contained in an ordered CI and agrees with the arm counts/percentages at printed precision. ICU/hospital mortality have a stated chi-square framework; day-28/day-90 P values may arise from the separately stated survival/log-rank framework, so no unsupported single-test diagnostic was applied. |
| S010 | **PASS_1_COMPLETE — no candidate.** Count-derived differences are -7.1 and -6.2 points to one decimal; each lies within its ordered CI with aligned direction. The article does not give an exact inferential construction for these exploratory outcomes. |
| S011 | **PASS_1_COMPLETE — no candidate.** 11/41 - 21/59 = -8.8 points to one decimal; estimate, ordered CI, arm direction, and P=.35 are mutually nonconflicting. Test/CI construction for this subgroup outcome is not supplied. |
| S012 | **PASS_1_COMPLETE — no candidate.** 291 - 254 = 37.0 mm Hg; the estimate lies in ordered CI 19.7 to 54.3 and direction/units agree. A simple unadjusted SD-based calculation is only diagnostic and is compatible with P<.001; the reported analysis/CI variance definition is not supplied. |
| S013 | **PASS_1_COMPLETE — no candidate.** The printed 1.2-point difference is inside ordered CI -5.4 to 7.7 with matching direction and P=.72. Exact event counts and test/CI method for this exploratory result are not printed. |
| S014 | **PASS_1_COMPLETE — no candidate.** Difference -5.0 h lies within ordered CI -42.0 to 32.0 and direction agrees. It need not equal subtraction of the rounded group medians (33 versus 39 h); the statistic/CI construction for a median difference is not stated. |
| S015 | **PASS_1_COMPLETE — no candidate.** 39/41 - 57/59 = -1.5 points to one decimal; ordered CI -13.0 to 7.4 contains the estimate. P=.99 is not contradicted by the supplied result; exact small-sample test choice is absent. |
| S016 | **PASS_1_COMPLETE — no candidate.** 86/339 - 106/302 = -9.7 points to one decimal; the estimate lies in ordered CI -16.8 to -2.6 and P<.01 has compatible direction. No literal display-zero P value is present. |
| S017 | **PASS_1_COMPLETE — no candidate.** Figure 2 explicitly labels a log-rank P=.02 for the stated day-7 time-to-reintubation curve; it is directionally consistent with the primary day-7 event result. At-risk counts decline without an impossible increase; exact censoring and survival-test inputs are not printed. |
| S018 | **PASS_1_COMPLETE — no candidate.** 5/63 - 10/48 = -12.9 points to one decimal; ordered CI -27.1 to -0.1 contains the estimate. Main P=.049 and eTable P=.0489 are compatible precision displays; Figure 3’s log-rank P=.049 is a separately identified test. Interaction P=.25 has no conflicting matched value. |
| S019 | **PASS_1_COMPLETE — STAT1-CAND-002.** Count, estimate, CI, and direction agree across locations; the main-text P=.10 and eTable-4 P=.1057 require reconciliation without assuming an unreported display convention. Figure 3’s log-rank P=.11 is a separately labelled survival test. |
| S020 | **PASS_1_COMPLETE — no candidate.** Adjusted OR 0.60 is inside ordered CI 0.38-0.93, is below the null in the stated treatment direction, and P=.02 is diagnostically compatible on the log-OR scale. The supplied model identifies adjustment covariates but not coefficient/variance details. |
| S021 | **PASS_1_COMPLETE — no candidate.** The post hoc hospital-random-effect model is explicitly distinguished from the model without that effect; the same rounded P=.02 does not create a duplicate-value contradiction because no expectation of unequal displayed P values is source-stated. Effect estimates and model variance details are unreported. |
| S022 | **PASS_1_COMPLETE — no candidate.** Chronic lung disease is 87/302 (29%) versus 126/339 (37%), with P=.02 as printed in the Table 1 footnote; direction supports its stated selection as the baseline imbalance. Exact baseline-test implementation is not specified. |
| S023 | **PASS_1_COMPLETE — no candidate.** The source states 11 prespecified secondary outcomes and six without significant difference. Enumerating the named secondary outcomes is compatible with that statement; multiplicity is acknowledged by the source and no adjusted inferential definition is claimed. |
| S024 | **PASS_1_COMPLETE — STAT1-CAND-003.** The protocol’s ITT chi-square plan is a planned framework; its same-endpoint reintubation definition uses pH<7.35, which differs from the main article’s pH<7.25 criterion. |
| S025 | **PASS_1_COMPLETE — no candidate.** Protocol predictor/adjustment methods are planning statements, explicitly not evidence that every planned model was used. No final-result comparator is asserted. |
| S026 | **PASS_1_COMPLETE — no candidate.** Protocol Kaplan-Meier/log-rank/Cox statements define a planned survival framework; no unreported final HR, relative risk, or model mapping was inferred. |
| S027 | **PASS_1_COMPLETE — no candidate.** Protocol secondary/mortality methods are planned frameworks. They do not create a contradiction with the final article’s explicitly described analyses. |
| S028 | **PASS_1_COMPLETE — no candidate.** The three prespecified subgroup strata provide labels/definitions. They are not an inferential estimate or duplicate result. |
| S029 | **PASS_1_COMPLETE — no candidate.** Protocol n=590, 80% power, two-sided alpha .05, 18% versus 10%, 8-point target, and 10% allowance to 650 agree with S002 and are arithmetically coherent. |
| S030 | **PASS_1_COMPLETE — no candidate.** Historical Table 1 P values belong to external RCTs. No population/contrast/time match to the current trial is supplied, so no inappropriate cross-trial comparison was made. |
| S031 | **PASS_1_COMPLETE — no candidate.** eTable 1 day-7 respiratory-failure and ICU-discharge reintubation P values match the corresponding main-table P values and counts. Components/reasons are expressly overlapping and were not summed. |
| S032 | **PASS_1_COMPLETE — no candidate.** eTable 2 has stratum-specific baseline P values with labels and denominators. The supplied plan allows multiple possible tests by variable type; exact calculation/variance rules are not reported, so no unsupported P reconstruction was used. |
| S033 | **PASS_1_COMPLETE — no candidate.** eTable 3 primary estimate -12.9 is contained in ordered CI -27.1 to -0.1, has count-consistent direction, and P=.0489 is compatible with the main rounded display. |
| S034 | **PASS_1_COMPLETE — no candidate.** All mapped hypercapnic secondary absolute differences lie inside ordered CIs and agree with arm counts/direction. The printed upper endpoint -0.10 for the 72-hour comparison is negative, not an endpoint-order or display-zero defect. |
| S035 | **PASS_1_COMPLETE — no candidate.** Hypercapnic stay/mortality estimates lie inside ordered CIs with aligned labels/scales; binary results are percentage-point differences and stay results are days. Exact tests/CI construction differ by outcome and are not fully specified. |
| S036 | **PASS_1_COMPLETE — no candidate.** 35/276 - 45/254 = -5.0 points to one decimal; CI -11.2 to 1.1 is ordered and contains the estimate. The eTable P=.1057 is recorded in STAT1-CAND-002 as the matched-location discrepancy with main text. |
| S037 | **PASS_1_COMPLETE — no candidate.** Nonhypercapnic secondary estimates are within ordered CIs and have count-consistent directions. The 72-hour upper endpoint `0.0` with P=.0505 is coherent finite-precision endpoint display, not a candidate; it is not a P-value display zero. |
| S038 | **PASS_1_COMPLETE — no candidate.** Nonhypercapnic stay/mortality estimates have ordered CIs, correct days versus percentage-point labels, and directions consistent with their arm values. No compatible source definition permits exact test/SE reconstruction for all rows. |
| S039 | **PASS_1_COMPLETE — no candidate.** The eFigure labels an unadjusted day-90 survival log-rank P=.37 and provides at-risk counts. It is not directly interchangeable with the Table 2 fixed-time day-90 mortality comparison (P=.30); the supplied source identifies different inferential constructs, so no cross-test contradiction was inferred. |

## Display-zero review

No assigned relationship contains a literal `P = 0`, `p = 0.000`, or equivalent finite-precision display zero. S016 contains `P<.01`, and S012 contains `P<.001`; neither is a display-zero notation. No candidate was discovered from P-value display formatting.

## Counts and limitations

- **Relationships reviewed:** 39 of 39.
- **Provisional candidates emitted:** 3 (`STAT1-CAND-001`, `STAT1-CAND-002`, `STAT1-CAND-003`).
- **DISPLAY_ZERO_NOT_CANDIDATE records:** 0; no literal display-zero P value was present in the assigned relationships.
- **Primary limitation:** Exact raw data, test-output records, CI construction rules, degrees of freedom, variance estimators, multiplicity adjustment details, and some exploratory-outcome test definitions are absent. This review therefore reports only direct mismatches and explicitly labelled diagnostics, without filling missing definitions from convention.
