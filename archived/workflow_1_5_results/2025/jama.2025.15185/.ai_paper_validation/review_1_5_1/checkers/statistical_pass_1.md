# Statistical Consistency Pass 1

## Scope and method

Independent pass-1 review of the complete statistical inventory `S001` through `S021`. Direct supplied PDFs were authoritative; source-linked extraction was used only as a locator. Each relationship was checked for point-estimate containment, ordered interval endpoints, sign/direction, repeated occurrence, and measure/scale label agreement. Interval/P/test/SE calculations were performed only where the supplied source stated compatible inferential definitions. No displayed `P = 0`, `p = 0.000`, or equivalent display-zero P value was found in this scope.

Statuses are pass-1 coverage records, not adjudications. `PASS` means no source-grounded inconsistency was identified under the supplied definitions. `UNRESOLVED` identifies an unavailable definition without manufacturing a candidate. `CANDIDATE_PROPOSAL` is a local proposal for coordinator registration and remains pending human adjudication.

## Relationship-level records

### S001 — PASS_1_COMPLETE — PASS

Primary adjusted FMA difference is `-0.90` with 95% CI `-3.78 to 1.98` and `P = .54` in DOC-001 PDF pp. 1 and 6; the pp. 4 analysis definition identifies baseline-FMA-adjusted linear regression. The estimate is contained in correctly ordered endpoints, direction is levodopa minus placebo in both locations, and the abstract, Results, and Discussion agree. The supplied information supports a two-sided 95% CI/P compatibility check only diagnostically because the model’s residual degrees of freedom and pooled imputation variance are not printed; the visible interval is compatible with the non-significant P-value.

### S002 — PASS_1_COMPLETE — PASS

DOC-001 PDF p. 4 states a two-sided alpha `.05` analysis, treatment effect with 95% CI and P value, baseline-FMA adjustment, and imputation for eligible survivors. This agrees with the primary-result presentation in pp. 1 and 6. No unreported degrees of freedom, variance estimator, or multiplicity rule was inferred.

### S003 — PASS_1_COMPLETE — PASS

DOC-001 PDF p. 6 reports PROMIS-29 adjusted mean difference `-0.37`, 95% CI `-3.34 to 2.61`. The estimate lies inside ordered endpoints and the stated levodopa-versus-placebo direction is compatible with the displayed group means (unadjusted means are not treated as a required equality with the adjusted estimate). PROMIS-29 domain direction is explicitly variable; no unsupported common-scale inference was made.

### S004 — PASS_1_COMPLETE — PASS

DOC-001 PDF p. 6 reports PROMIS-10 adjusted mean difference `0.18`, 95% CI `-0.98 to 1.33`. The estimate is contained by ordered endpoints. The positive effect direction is compatible with the stated higher-is-better PROMIS-10 scale and with the rounded descriptive means; no P value or compatible SE is supplied.

### S005 — PASS_1_COMPLETE — PASS

DOC-001 PDF p. 6 and DOC-004 PDF p. 15 agree on the adjusted secondary FMA effects: affected upper `-0.73 [-2.97, 1.50]`, affected lower `-0.13 [-1.02, 0.77]`, and unaffected-side total `0.63 [-0.72, 1.99]`. Each estimate is within ordered endpoints. Unadjusted group-mean directions need not equal adjusted-effect directions; all three labels distinguish affected from unaffected side. The detailed supplement reports the SMD direction convention only implicitly, so it was not used to require equality or sign agreement with the adjusted mean difference.

### S006 — PASS_1_COMPLETE — PASS

DOC-001 PDF p. 6 and DOC-004 PDF p. 15 agree on NIHSS `-0.14 [-0.61, 0.33]` and Rivermead `-0.33 [-1.04, 0.37]`. Estimates are inside ordered intervals. The source defines higher NIHSS as worse and higher Rivermead as better; their estimate signs and labels do not create a source contradiction. No compatible P value, SE, or inferential test statistic is printed.

### S007 — PASS_1_COMPLETE — PASS

DOC-001 PDF p. 6 reports ordinal-logistic adjusted OR `0.93 [0.69, 1.23]` for levodopa compared with placebo while describing odds of better functional outcome across mRS categories; mRS higher values are worse (DOC-001 p. 3). The ratio estimate is positive and lies within ordered positive endpoints; its value below 1 is directionally compatible with the stated comparison. No model coding, proportional-odds parameterization, SE, or P value is printed, so none was inferred. DOC-004 p. 15 repeats the numeric OR and interval without contradiction.

### S008 — PASS_1_COMPLETE — PASS

DOC-001 PDF p. 6 and DOC-004 PDF p. 15 agree on the five-week FMA adjusted difference `0.02 [-2.81, 2.84]`. The estimate is within ordered endpoints and is distinct from the three-month primary endpoint. No compatible P value or SE is supplied.

### S009 — PASS_1_COMPLETE — PASS

DOC-001 PDF p. 3 states the prospective calculation: SD `25`, calculated `n = 548`, 80% power, two-sided alpha `.05`, 6-point target difference, and planned enrollment `610` for anticipated 10% dropout and at least `549` analysable participants. The printed calculation inputs and rounded dropout plan are mutually coherent (`610 - 61 = 549`). The exact allocation ratio and sample-size formula used by the software are not printed, so no independent recomputation was used as a contradiction rule.

### S010 — PASS_1_COMPLETE — PASS

DOC-003 PDF p. 2 identifies the SAP primary objective as levodopa/carbidopa `100/25 mg` three times daily versus placebo and three-month FMA functional recovery. This matches the final trial intervention and endpoint definitions in DOC-001 PDF pp. 1 and 3. It is a plan-definition relationship, not a test-result occurrence.

### S011 — PASS_1_COMPLETE — PASS

DOC-003 PDF p. 2 states a secondary objective concerning survival and general health. This is not a repeated final inferential effect estimate, and no matched source result with compatible population/estimand was supplied for a numerical reconciliation. No candidate was manufactured from the absence of an effect estimate.

### S012 — PASS_1_COMPLETE — PASS

DOC-002 PDF pp. 8-10 and DOC-003 PDF p. 2 provide protocol/SAP timing, eligibility, and planned-primary-endpoint definitions. They are compatible at the relevant level with the final three-month FMA primary outcome in DOC-001 PDF pp. 1 and 3. Plan-level wording was not treated as a contradiction of a final analysis without a matched population, estimand, and model comparator.

### S013 — PASS_1_COMPLETE — PASS

DOC-004 PDF p. 6 records R `4.3.1` and named data, modelling, visualization, and quality-control packages. This is an analysis-software provenance record, not a numerical test result; no conflicting software specification is supplied.

### S014 — PASS_1_COMPLETE — PASS

DOC-004 PDF p. 7 specifies 100 chained-equation imputations, model fitting on each imputed data set, and Rubin-rule combination of estimates and variances. It is compatible with DOC-001 PDF p. 4’s missing/incomplete-outcome handling and the primary-result description. The page also discloses defined departures for mRS, PRAI, and SAP wording; disclosure alone is not a numerical inconsistency.

### S015 — PASS_1_COMPLETE — CANDIDATE_PROPOSAL (QS001, QS002, QS003)

DOC-004 PDF pp. 12-13 eTable 2 gives primary and sensitivity estimands. Mean-difference estimands 1-3 and 5-8 have estimates contained in ordered intervals and agree with the plotted mean-difference scale in eFigure 4 (DOC-004 p. 23). Estimand 4 is a separately described composite win-ratio estimand, so it was not expected to appear on that mean-difference plot.

- **QS001 — Statistical reporting inconsistency.** On DOC-004 PDF p. 12, the eTable 2 narrative reports Estimand 4 as odds ratio `1.06` with 95% CI `0.86 to 1.25`. The Estimand 4 table row on PDF p. 13 reports the same estimate as `1.06 [0.86 - 1.26]`. Population (full analysis set, `610`), endpoint (death and three-month FMA), and composite strategy match. The upper endpoint differs by `0.01`; direct observation is the mismatch, not a reconstructed interval. Human question: which printed upper endpoint is the intended rounded 95% CI?
- **QS002 — Measure, label, or scale inconsistency.** The eTable 2 column header on DOC-004 PDF p. 13 labels its effect field `Estimated Effect of Levodopa: Mean Difference on FMA, [CI]`. Estimand 4 in that same table identifies its population-level summary as a `win ratio [95% CI]` for death and three-month FMA and prints `1.06 [0.86 - 1.26]`. A win ratio is not labelled as an FMA mean difference by the row itself. Human question: should the column heading be qualified for Estimand 4 or should the row’s stated measure be changed?
- **QS003 — Measure, label, or scale inconsistency.** On DOC-004 PDF p. 12, the narrative calls Estimand 4 an `odds ratio` of `1.06`; the matched table row on PDF p. 13 identifies the effect as a `win ratio [95% CI]`. This is a direct label discrepancy for the same composite estimand. Whether a particular modelling implementation makes these terms numerically related cannot be inferred from the supplied source and is not asserted. Human question: which measure name is intended for Estimand 4?

### S016 — PASS_1_COMPLETE — PASS

DOC-004 PDF p. 14 eTable 3 identifies post hoc Estimand 9 as change from baseline, `-0.90 [-3.78, 1.98]`, with `582` participants; it matches the primary-estimand values while having its own explicitly stated endpoint transformation. Estimand 10 (`-0.03 [-3.27, 3.21]`, `610`) and Estimand 11 (`0.32 [-3.25, 3.89]`, `395`) have contained estimates and ordered endpoints. eFigure 7 (p. 27) visually agrees in direction/zero-crossing with the PH1/PH2 display. No P values, SEs, or source-supplied model details permit a stricter test.

### S017 — PASS_1_COMPLETE — PASS

DOC-004 PDF p. 15 eTable 4 supplies secondary-outcome group means (SD), SMDs, adjusted effects, intervals, and participant totals. All reported adjusted estimates are inside their ordered intervals. Descriptive means are unadjusted and the source does not define SMD sign orientation; consequently, modest differences between unadjusted mean direction, SMD display, and adjusted effect are diagnostic context only, not contradiction. The mRS row correctly uses an OR-scale estimate (`0.93 [0.69, 1.23]`) rather than treating the median as a mean difference.

### S018 — PASS_1_COMPLETE — UNRESOLVED

DOC-004 PDF p. 18 titles eTable 7 as a baseline-FMA-by-treatment interaction model and eTable 8 as a no-interaction model with a 3-degree-of-freedom baseline-FMA spline. The supplied page does not show parameter estimates, intervals, test statistics, or a fitted model output from which compatibility could be mechanically assessed. The model labels themselves do not contradict one another because they designate different specified models. Missing definitions: interaction contrast/coding, spline basis/knots, fitted coefficients, and inferential procedure.

### S019 — PASS_1_COMPLETE — PASS

Direct visual check of DOC-004 PDF pp. 23-24 eFigure 4 shows mean-difference estimates for Estimands 1-3 and 5-8 on an adjusted FMA-points axis, with zero marked and directions labelled favoring placebo/levodopa. The visible forest-plot positions and interval directions agree with eTable 2 (p. 13): all plotted mean-difference intervals cross zero, and Estimand 7 alone has a small positive point estimate. Estimand 4’s different win-ratio scale is not plotted. Exact graphical coordinates are not printed, so this was a visual direction/containment check, not numerical transcription.

### S020 — PASS_1_COMPLETE — PASS

Direct visual check of DOC-004 PDF p. 26 eFigure 6 shows a nonlinear positive association between baseline affected-side FMA and predicted three-month affected-side FMA, with wider uncertainty at the high end. The title, axes, and caption consistently identify FMA/FMAA and the spline-model context. No treatment-effect estimate, interval endpoint, P value, or compatible model coefficient is printed; none was inferred from the curve.

### S021 — PASS_1_COMPLETE — PASS

Direct visual check of DOC-004 PDF p. 27 eFigure 7 shows PH1, PH2, and two PH3 subgroup estimates on a common estimate axis with a zero reference. The legend defines PH1 as death-imputed-zero, PH2 as the low-intake/minimal-rehabilitation exclusion, and PH3 as the baseline-FMA subgroup comparison. The direction and zero-crossing presentation agrees with eTable 3 for PH1 (Estimand 10) and PH2 (Estimand 11); the figure does not print exact subgroup values, so no exact numerical equality was asserted.

## Pass-1 summary

- Statistical relationships completed: 21 of 21 (`S001`-`S021`).
- PASS: 19; UNRESOLVED: 1; CANDIDATE_PROPOSAL relationship: 1.
- Distinct local proposals for coordinator consideration: 3 (`QS001`-`QS003`); no stable candidate IDs assigned.
- Display-zero P-value records: 0; no display-zero P-value candidate proposed.
- Limitations: model degrees of freedom, covariance/variance estimators, multiplicity implementation, spline basis, and exact graphical coordinates were not supplied for several relationships. These omissions were documented and were not inferred from convention.
