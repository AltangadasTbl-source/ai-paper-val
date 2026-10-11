# Statistical Consistency Pass 1

## Scope, method, and boundary

- **Pass:** `PASS_1_COMPLETE`.
- **Assigned scope:** every canonical inferential relationship, `S001` through `S044` (44/44).
- **Evidence boundary:** only the fresh, page-addressable Acrobat native-text assets and the fresh canonical relationship, extraction, and numeric inventories under `review_1_5_2/`. No web source, old audit derivative, or old candidate set was used.
- **Checks applied when source-defined:** point-estimate containment; endpoint order; null, sign, direction, effect-measure, scale, and comparator labels; matched repeated results; rate/count boundaries; and P-value/interval compatibility only when the reported model, contrast, null, confidence level, and test purpose support it. Unreported sidedness, degrees of freedom, covariance, variance estimator, estimand mapping, and multiplicity handling were not inferred.
- **Diagnostic convention:** for a two-sided 95% interval with an explicitly stated null, a rough normal-scale value computed as estimate divided by `(CI half-width / 1.96)`, or its log-scale analogue for ratios/HRs, is labelled a *diagnostic approximation*. It is not treated as the reported test because multiple imputation/Rubin rules, Cox models, and unspecified finite-sample inference may use different degrees of freedom or variance rules.
- **Display-zero check:** no mapped relationship prints `P = 0`, `p = 0.000`, or equivalent. Therefore no `DISPLAY_ZERO_NOT_CANDIDATE` record was required in this scope.

## Relationship records

### S001 — PASS_1_COMPLETE

DOC-001 PDF p.3 states 80% power for a 2.3 mL/min/1.73 m² active-placebo eGFR-change difference, two-sided alpha .05, assuming 80% follow-up. This is a planning projection, not an observed inferential result. The planned contrast, scale, direction, and alpha label are internally stated. The supplied source does not provide the simulation/variance inputs needed to recompute power. No candidate proposal.

### S002 — PASS_1_COMPLETE

DOC-001 PDF p.3 defines the primary random-intercept linear mixed model, categorical baseline/year-2/year-5 time, treatment-by-time terms, age/sex terms, and additional baseline-ACR adjustment for eGFR. The model label and eGFR scale agree with Table 2 (DOC-001 p.8) and eTables 4-5 (DOC-003 pp.9-10). No coefficient, SE, or test statistic is supplied here for mechanical reconciliation. No candidate proposal.

### S003 — PASS_1_COMPLETE

DOC-001 PDF p.3 specifies the treatment-by-year-5 interaction as the treatment test, a two-tailed .05 criterion, 20 imputations, and Rubin rules. The year-5 P-value purpose agrees with Table 2 footnote c (DOC-001 p.8). Multiplicity adjustment, degrees of freedom, and the imputation model beyond the stated summary are not supplied; they were not inferred. No candidate proposal.

### S004 — PASS_1_COMPLETE

DOC-001 PDF p.3 identifies Cox proportional-hazards models for categorical outcomes and Schoenfeld-residual assessment; DOC-001 p.6 reports no significant proportional-hazards violations. Table 3 (DOC-001 p.9) labels Cox HRs and tests the null HR=1, consistently with this model family. No residual statistic or test definition is printed for a numerical recheck. No candidate proposal.

### S005 — PASS_1_COMPLETE

DOC-001 PDF p.4 reports year-2 25(OH)D means 41.4 (SD 11.0) versus 29.8 (SD 11.1) ng/mL, `P < .001`. Direction (active vitamin D higher) is compatible with the intervention and the stated units. Group sample sizes, test type, and variance rule are absent, so no P/SD reconstruction was attempted. No candidate proposal.

### S006 — PASS_1_COMPLETE

DOC-001 PDF p.4 reports year-2 omega-3-index means 3.6% (SD 1.0%) versus 2.3% (SD 0.8%), `P < .001`. Direction and percent scale agree with the omega-3 biomarker definition. Group sample sizes, test type, and variance rule are absent. No candidate proposal.

### S007 — PASS_1_COMPLETE

DOC-001 p.4 and Table 2 (p.8) repeat the vitamin-D year-5 difference 0.9 (95% CI -0.7 to 2.5), `P = .25`. The estimate is contained, endpoints are ordered, the positive active-minus-placebo direction is explicitly defined, and the null is 0. A diagnostic normal approximation from the rounded CI gives z about 1.10 and two-sided P about .27; .25 is compatible with rounding and the stated imputed mixed-model analysis, whose degrees of freedom/variance rule are not supplied. No candidate proposal.

### S008 — PASS_1_COMPLETE

DOC-001 p.4 and Table 2 (p.8) repeat the omega-3 year-5 difference 0.9 (-0.7 to 2.6), `P = .27`. Containment, endpoint order, active-minus-placebo direction, null 0, and scale are coherent. The rounded-CI diagnostic gives z about 1.09 and P about .28, compatible with .27 under the same limitation on imputation inference details. No candidate proposal.

### S009 — PASS_1_COMPLETE

DOC-001 p.4 reports no significant factorial treatment-assignment interaction (`P = .42`), consistent with the no-interaction comparison framework in the final analysis plan (DOC-002 p.32) and the main model description (DOC-001 p.3). The interaction coefficient, SE, and test statistic are not supplied. No candidate proposal.

### S010 — PASS_1_COMPLETE

DOC-001 p.4 gives full-analytic eGFR change -12.7 (-13.6 to -11.7) and complete-case change -12.4 (-13.3 to -11.4), n=932. Both estimates lie within ordered intervals and have the same decline direction. They concern expressly different analysis populations, so their difference is not a cross-location contradiction. No candidate proposal.

### S011 — PASS_1_COMPLETE

DOC-001 p.4 and Table 3 (p.9) agree that the vitamin-D composite HR is 0.92 (0.68-1.25) and is not significant. The HR is contained in its ordered CI, and the CI contains the stated null 1. Table 3 identifies the Cox model and null. No P is repeated in the narrative for a direct numerical comparison. No candidate proposal.

### S012 — PASS_1_COMPLETE

DOC-001 p.4 and Table 3 (p.9) agree that the omega-3 composite HR is 1.11 (0.81-1.50) and is not significant. Containment, endpoint order, ratio null 1, and narrative direction are coherent. No candidate proposal.

### S013 — PASS_1_COMPLETE

DOC-001 Table 3 p.9 reports vitamin-D HR 0.97 (0.63-1.51), `P = .90`, with a Cox-model null HR=1. The estimate is contained and the CI includes 1. On the log scale, the rounded-CI diagnostic gives z about 0.14 and P about .89, compatible with .90. Cox variance/test details remain unspecified. No candidate proposal.

### S014 — PASS_1_COMPLETE

DOC-001 Table 3 p.9 reports vitamin-D ACR-event HR 1.34 (1.00-1.80), `P = .05`, with null HR=1. Estimate containment and endpoint order hold; the printed lower endpoint equals the null after rounding. A log-CI diagnostic gives z about 1.95 and P about .05, compatible with the printed value. No candidate proposal.

### S015 — PASS_1_COMPLETE

DOC-001 Table 3 p.9 reports omega-3 HR 0.99 (0.64-1.54), `P = .97`; containment, endpoint order, ratio scale, and null HR=1 are coherent. A rounded log-CI diagnostic gives z about 0.03 and P about .97. No candidate proposal.

### S016 — PASS_1_COMPLETE

DOC-001 Table 3 p.9 reports omega-3 ACR-event HR 1.08 (0.81-1.44), `P = .60`; containment, endpoint order, ratio scale, and null HR=1 are coherent. A rounded log-CI diagnostic gives z about 0.52 and P about .60. No candidate proposal.

### S017 — PASS_1_COMPLETE

DOC-001 Table 3 p.9 footnotes directly define Cox HRs and P values testing HR=1. This definition is consistently applied to S011-S016. No candidate proposal.

### S018 — PASS_1_COMPLETE

DOC-001 Figure 3 p.8 supplies six interaction P values (.58, .36, .15, .18, .79, .42) after the six displayed vitamin-D subgroup families and identifies adjusted active-minus-placebo eGFR-change estimates. All values exceed .05 and are compatible with the p.4 statement of no significant vitamin-D subgroup heterogeneity. The native text is not layout-preserving, so exact row-to-P assignment is missing and was not inferred. No candidate proposal.

### S019 — PASS_1_COMPLETE

DOC-001 Figure 4 p.9 supplies five interaction P values (.72, .70, .73, .51, .42) and identifies adjusted active-minus-placebo eGFR-change estimates. All values exceed .05 and are compatible with the p.4 statement of no significant omega-3 subgroup heterogeneity. Exact row-to-P assignment is unavailable from non-layout native text and was not inferred. No candidate proposal.

### S020 — PASS_1_COMPLETE

DOC-001 Figures 3-4 pp.8-9 define estimates as active-placebo differences in baseline-to-year-5 eGFR change, adjusted for age, sex, and baseline ACR. This measure, direction, scale, and adjustment agree with Table 2 and S002. No candidate proposal.

### S021 — PASS_1_COMPLETE

DOC-001 p.4 states no significant subgroup heterogeneity and no significant biomarker-change/eGFR-change correlation. The former agrees with all displayed Figure 3-4 interaction P values. Correlation coefficients, sample sizes, and P values for the latter are not supplied in usable native text (DOC-003 p.17); no numerical inference was made. No candidate proposal.

### S022 — PASS_1_COMPLETE

DOC-001 p.3 labels prespecified secondary analyses exploratory because of possible type-I error from multiple comparisons. This is an interpretation boundary, not an inconsistent multiplicity claim: the source does not state a multiplicity correction. No candidate proposal.

### S023 — PASS_1_COMPLETE

DOC-001 p.4 describes continuous ACR change and no assignment difference; Table 3 p.9 reports a time-to-doubling ACR Cox estimand, while DOC-003 eTable 6 p.11 reports the continuous ratio-of-change estimand. The sources distinguish the models and scale (HR/null 1 versus ratio/null 1). These are nonidentical estimands, not duplicate values requiring equality. No candidate proposal.

### S024 — PASS_1_COMPLETE

DOC-001 p.7 interprets the primary CIs against a 0.75 mL/min/1.73 m²/year, or 3.75 over five years, surrogate benchmark. The multiplication is stated and agrees with the p.3 definition. This is an interpretation of CIs, not a new inferential test; no candidate proposal.

### S025 — PASS_1_COMPLETE

DOC-001 p.4 describes post-hoc composite outcomes as not significant and points to DOC-003 eTable 10 p.15. All eight listed eTable 10 HR CIs contain 1 and their printed P values (.88, .12, .17, .12, .77, .77, .44, .31) exceed .05. Narrative and table are compatible. No candidate proposal.

### S026 — PASS_1_COMPLETE

DOC-003 pp.2-4 describes cystatin-C calibration (5.49/5.961 multiplier; `0.006801 + 1.037603 × pre-shift`; QC r=.999). This is a laboratory transformation/QC statement, not an outcome inference. The multiplier direction is explicitly supplied and no external assay rule was imported. No candidate proposal.

### S027 — PASS_1_COMPLETE

DOC-002 p.17 records the original year-4 ACR ANCOVA/log-transform and eGFR equations, alpha .05, no multiple-comparison correction, chi-square for composite proportions, and conditional rank-sum use. It is an original-plan definition and cannot be mechanically equated to the later year-5 final plan absent a matched endpoint/model. No candidate proposal.

### S028 — PASS_1_COMPLETE

DOC-002 p.18 defines the original factorial interaction coefficient on log(ACR at year 4), its `P < .05` rule, and an additive contrast. The final reported interaction is a year-5 eGFR mixed-model result (S009/S033), so timepoint, endpoint, and scale do not match. No candidate proposal.

### S029 — PASS_1_COMPLETE

DOC-002 pp.18-19 defines original ANCOVA interpretations: `exp(beta2)-1` is relative ACR percent-change difference and eGFR beta2 is active-placebo difference. The source distinguishes ratio/percent and absolute eGFR scales; no conflicting final use was identified. No candidate proposal.

### S030 — PASS_1_COMPLETE

DOC-002 pp.19-20 gives original projected power values (including 90% at 17% ACR and 2.6 eGFR). These are assumptions/projections for an original sample/timepoint, not observed effects. No candidate proposal.

### S031 — PASS_1_COMPLETE

DOC-002 p.23 gives the Haybittle-Peto interim monitoring boundary z=3, P=.0027 for multiple looks. It is a stopping-rule definition, not a reported test result. Number/timing of actual looks and alpha-spending details beyond the rule are not used to infer a contradiction. No candidate proposal.

### S032 — PASS_1_COMPLETE

DOC-002 p.32 specifies the final-plan chained-equation MI for missing year-5 eGFR using baseline plus year-2 eGFR/ACR and 10 datasets with Rubin rules. DOC-001 p.3 reports 20 imputations in the final article. The plans are temporally distinct supplied documents; no source equates the planned 10 with the executed 20, and a plan amendment/change is not itself an inconsistency. No candidate proposal.

### S033 — PASS_1_COMPLETE

DOC-002 p.32 supplies the final factorial eGFR mixed interaction model with categorical time 0, 2, 5, participant random effect, and beta6 `P < .05` criterion. DOC-001 p.4 reports the corresponding final interaction P=.42. Coefficient/SE are absent, but endpoint, timepoint, and test purpose align. No candidate proposal.

### S034 — PASS_1_COMPLETE

DOC-002 pp.32-33 defines final beta3 as the active-D3/placebo eGFR-change contrast, year-5 inferential focus, continuous log-ACR handling, and discrete Cox categorical outcomes. These labels agree with main Table 2 and Table 3/eTable 6 boundaries. No candidate proposal.

### S035 — PASS_1_COMPLETE

DOC-002 p.33 gives a 2,000-replication final power simulation with n=1,058, two-sided alpha .05, and 80% power for a 2.3 mL/min/1.73 m² year-5 difference. It is a planned projection, agreeing in threshold/scale with DOC-001 p.3 but not requiring equality of sample/planning assumptions. No candidate proposal.

### S036 — PASS_1_COMPLETE

DOC-003 eTable 4 p.9 defines adjusted/MI year-5 eGFR-change P values. Vitamin D is .87 (-.83, 2.58), P=.32; omega-3 is .09 (-1.61, 1.80), P=.92. Both estimates are contained in ordered CIs and CIs contain 0. Rounded-CI diagnostics give respectively z about 1.00/P .32 and z about .10/P .92. Main-table values differ only because this is the available-baseline/year-5 population (N=932), not the full analytic population. No candidate proposal.

### S037 — PASS_1_COMPLETE

DOC-003 eTable 5 p.10 defines the adherent-population version of the same adjusted/MI eGFR analysis: vitamin D .89 (-.74, 2.52), P=.28; omega-3 .42 (-1.22, 2.06), P=.61. Containment/order/null 0 all hold. Rounded-CI diagnostics give P about .28 and .61. The stated adherent population (N=1,032 per intervention dimension) distinguishes it from S036. No candidate proposal.

### S038 — PASS_1_COMPLETE

DOC-003 eTable 6 p.11 defines geometric ACR ratios and explicitly tests the year-5 difference in change: vitamin D .99 (.84, 1.17), P=.90; omega-3 .96 (.81, 1.14), P=.64. Estimates are contained, endpoints ordered, and null 1 is within both CIs. Log-CI diagnostics give P about .91 and .64, compatible with the printed values. No candidate proposal.

### S039 — PASS_1_COMPLETE

DOC-003 eTable 7 p.12 defines the paired-baseline/year-5 ACR population: vitamin D 1.03 (.86, 1.22), P=.77; omega-3 .93 (.78, 1.11), P=.44. Ratio scale/null 1, containment, and endpoint order hold. Log-CI diagnostics give P about .77 and .44. The source distinguishes this sensitivity population from S038. No candidate proposal.

### S040 — PASS_1_COMPLETE

DOC-003 eTable 8 p.13 defines the adherent ACR sensitivity: vitamin D 1.02 (.85, 1.22), P=.87; omega-3 .99 (.83, 1.19), P=.94. Ratio scale/null 1, containment, and ordering hold. Log-CI diagnostics give P about .87 and .94. No candidate proposal.

### S041 — PASS_1_COMPLETE

DOC-003 eTable 9 p.14 defines the UTI-symptom-visit-excluded ACR sensitivity: vitamin D .99 (.84, 1.17), P=.90; omega-3 .98 (.83, 1.16), P=.80. Ratio scale/null 1, containment, and ordering hold. Log-CI diagnostics give P about .90 and .80. No candidate proposal.

### S042 — PASS_1_COMPLETE

DOC-003 eTable 10 p.15 identifies eight post-hoc Cox HR records and P values testing HR=1. Each HR is contained in an ordered CI that includes 1, and each P exceeds .05. Rate differences are explicitly labelled per 100 person-years and are not treated as HRs. Diagnostic log-CI checks are compatible with the eight reported P values after rounding; model variance/df details are not supplied. No candidate proposal.

### S043 — PASS_1_COMPLETE

DOC-003 eFigure 1 p.17 states the correlation windows (markers baseline-year 2; eGFR baseline-year 5) and all-available-data population. Usable native text contains no coefficient, interval, sample size, or P value. No correlation magnitude or test was inferred. No candidate proposal.

### S044 — PASS_1_COMPLETE

DOC-003 eFigures 2-3 pp.18-19 title the figures as active treatment versus placebo ACR subgroup analyses and describe adjusted age/sex baseline-to-year-5 change estimates. However, each caption's final sentence says the estimate compares “the active treatment assignment to year 5,” which names a timepoint rather than the placebo comparator established by the figure titles, main article, and eTable 6. This repeated supplied-source label mismatch is proposed below as `SP001`.

## Candidate proposals for coordinator registration

### SP001 — eFigure 2 and eFigure 3 comparator wording is inconsistent with the stated active-versus-placebo contrast

- **Proposed category:** `Measure, label, or scale inconsistency`.
- **Exact source locations:** DOC-003 (Supplement 2) PDF p.18, eFigure 2 title/caption; DOC-003 PDF p.19, eFigure 3 title/caption; comparator context in DOC-001 PDF p.4 and DOC-003 PDF p.11, eTable 6.
- **Printed evidence:** eFigure 2 is titled “Effects of Vitamin D Versus Placebo …”; eFigure 3 is titled “Effects of Omega-3 Fatty Acids Versus Placebo …”. Each caption then states: “Estimates are difference in change in urine ACR from baseline to year 5, comparing the active treatment assignment to year 5, adjusted for age and sex.” DOC-003 eTable 6 p.11 explicitly labels its relevant contrast “Ratio of change from baseline, active to placebo,” and DOC-001 p.4 describes no difference according to active intervention versus its placebo.
- **Rule:** an effect estimate’s comparator must identify the comparison group, not a follow-up timepoint. A timepoint belongs to the outcome/change window; it is not the comparator in a title explicitly framed as active treatment versus placebo.
- **Calculation / logical comparison:** no arithmetic calculation. Direct comparison of the figure titles (`versus placebo`) and the repeated caption phrase (`active treatment assignment to year 5`) yields incompatible comparator labels. `baseline to year 5` is already the stated change window, so “to year 5” cannot also define an active-versus-control contrast.
- **Direct versus inferred:** Direct: both figure titles and both caption phrases above are printed in the supplied fresh native text. Inferred diagnostic: the intended comparator may have been placebo, based on the titles and matched main/eTable contrast; that possible intended wording is not asserted as a correction.
- **Alternative source-grounded interpretations:** the non-layout native-text extraction may have omitted or reordered a visual caption element; the supplied package does not include a permitted renderer/layout extraction to visually confirm glyph placement. Alternatively, both captions may carry the same repeated wording defect. The titles still directly identify placebo as the contrast.
- **Missing definitions / evidence:** visually rendered p.18-19 captions are unavailable in the current permitted tool environment; no plotted estimate/CI/P values are usable for a further numerical check.
- **Human question:** do the rendered source pages actually print “comparing the active treatment assignment to year 5”; if so, should the comparator wording identify placebo while retaining baseline-to-year-5 as the change window?
- **Status boundary:** candidate proposal only; `Pending Human Adjudication`. No severity, validity, correction, or acceptance is assigned here.

## Pass limitations

- Acrobat native text is fresh and page-addressable but not layout-preserving. This precludes a definitive row-to-P alignment for main Figures 3-4 and visual confirmation of Supplement 2 eFigure captions/plots.
- No source supplies enough model-specific information to reproduce exact MI/Rubin, Cox, correlation, power-simulation, or interaction-test calculations. All displayed interval/P approximations above are diagnostic only and support no claim beyond compatibility.
- Original and final analysis-plan records have different timepoints, populations, and/or analysis specifications. They were not treated as conflicting unless the supplied source explicitly claimed equality.

## Compact completion record

- **Relationships completed:** 44/44 (`S001`-`S044`).
- **Candidate proposals emitted:** 1 (`SP001`).
- **Coherent display-zero P values:** 0 observed; `DISPLAY_ZERO_NOT_CANDIDATE` records: 0.
- **Primary artifact:** `checkers/statistical_pass_1.md`.
