# Statistical Consistency Review — Pass 2

## Scope, independence, and method

This independent second pass revisited all 29 canonical statistical relationships: S001--S017 (DOC-001) and S1001--S1012 (DOC-002--DOC-003). It used only the supplied PDFs and the current fresh source assets, the complete numeric and cross-source checker outputs, pass-1 output, the stable candidate ledger (C001--C005), and the mechanical evidence recheck. Earlier audit derivatives were not evidence inputs.

For every relationship, this pass checked applicable denominator and arithmetic implications, point-estimate containment, interval ordering, sign/direction, effect-measure and scale labels, duplicate values, cross-location repetitions, and candidate/recheck implications. Exact P-value, test-statistic, or SE reconciliation was performed only where compatible rules were supplied. It was not performed for the adjusted-risk-difference results because the sources specify that aRDs/CIs are transformed from logistic-regression ORs/CIs while P values are Hochberg-adjusted logistic-regression P values; the package does not supply the raw ORs, covariance, variance estimator, sidedness for individual reported tests, degrees of freedom, or a joint CI/P rule.

All arithmetic described below is a diagnostic calculation from displayed values, not a reconstruction of the reported model.

## Complete relationship recheck

| S ID | PASS_2_COMPLETE recheck record |
|---|---|
| S001 | DOC-001 p. 3 planning totals remain coherent: 4 x 320 = 1280; 4 x 400 = 1600; 1280/(1-0.20) = 1600. The stated 80% power cannot be recreated because simulation inputs and the comparison-wise alpha allocation are not fully supplied. No duplicate or cross-source arithmetic contradiction is established. |
| S002 | DOC-001 p. 3 labels respondent/nonrespondent chi-square and adjusted/unadjusted cluster-aware GEE logistic analyses; Table 3’s model footnote is compatible. Working correlation, variance estimator, degrees of freedom, and covariate-selection details are absent, so statistic/SE/P reconciliation is not defined. |
| S003 | DOC-001 pp. 3 and 7 consistently label the reported quantities as adjusted risk differences converted from adjusted logistic ORs/CIs using observed control prevalence. The adjusted-risk subtractions reproduce displayed aRDs where both values appear. Raw ORs, conversion algorithm, and covariance are not supplied; no interval reconstruction is valid. |
| S004 | The final article’s Hochberg-adjusted P-value label and post hoc 20-imputation-set description are internally repeated. DOC-002’s planned Bonferroni rule is a different planned procedure, not a matched final-result comparator; final decision-rule/change documentation is unavailable. No candidate beyond the ledger is supported. |
| S005 | DOC-001 p. 6’s `P < .001` respondent/nonrespondent summary is compatible with DOC-003 pp. 3--4’s matched chi-square bounds `<.0001`. C002/C003 concern eTable 2 percentage and denominator disclosure, not these P bounds. No test statistic, degrees of freedom, or correction rule is supplied for reproducing the chi-square P values. |
| S006 | DOC-001 pp. 1, 6--7 repeats supine mHealth aRD 8.9% (95% CI 5.3% to 11.7%): the estimate is contained in ordered endpoints; 89.1-80.2 = 8.9 points; direction, outcome label, and repeated locations agree. The P inequality is compatible directionally, but no common transformed-CI/Hochberg-P inversion rule is supplied. |
| S007 | DOC-001 p. 7 supine NQI-only aRD -1.7% is inside the ordered -10.1% to 4.7% CI, and 78.5-80.2 = -1.7 points. The negative direction and null-containing interval agree with the labeled P=.74. P/CI inversion is not defined under the supplied layers. |
| S008 | DOC-001 p. 7 correctly distinguishes the NQI-only 2.6% aRD (-3.1% to 7.2%) from the separate multiplicative interaction P=.01. The estimate is contained, 82.8-80.2 = 2.6 points, and labels/direction agree. No duplicate-value, scale, or candidate conflict remains after the corrected canonical contrast label. |
| S009 | DOC-001 p. 7’s combined-intervention supine aRD 9.4% lies within 2.9% to 13.6%; 89.6-80.2 = 9.4 points and direction/contrast labels agree. The Hochberg P=.03 and transformed CI are not mechanically invertible under supplied definitions. |
| S010 | DOC-001 p. 7 room-sharing NQI aRD 3.7% lies within -0.4% to 7.2%; 74.1-70.4 = 3.7 points; labels and direction agree. The null-containing CI and P=.07 are directionally compatible, with no supplied exact inversion rule. |
| S011 | DOC-001 pp. 1, 6--7 consistently repeats room-sharing mHealth aRD 12.4% (9.3% to 15.1%): containment and endpoint order hold, and 82.8-70.4 = 12.4 points. The separately labeled interaction P=.08 is not conflated with the effect P. C001 concerns a raw control percentage in the Table 3/eTable 5 repetition, not this adjusted mHealth result. |
| S012 | DOC-001 p. 7 no-soft-bedding NQI aRD 3.3% lies in -1.4% to 7.8%; 70.9-67.6 = 3.3 points. Positive direction, effect label, and null-containing CI agree; no duplicate or cross-source mismatch is supplied. |
| S013 | DOC-001 pp. 1, 6--7 consistently repeats no-soft-bedding mHealth aRD 11.8% (8.1% to 15.2%); 79.4-67.6 = 11.8 points and signs/labels agree. Interaction P=.29 is distinct. No fully defined CI/P inversion rule is available. |
| S014 | DOC-001 p. 7 pacifier NQI aRD 6.8% lies within 1.4% to 11.9%, with 66.6-59.8 = 6.8 points and coherent direction/scale. The CI excludes zero while Hochberg P=.07; this is not a candidate because the source expressly identifies distinct transformed-CI and multiplicity-adjusted-P layers and provides no joint rule. |
| S015 | DOC-001 pp. 1, 6--7 consistently repeats pacifier mHealth aRD 8.7% (3.9% to 13.1%); 68.5-59.8 = 8.7 points and directions/labels agree. Interaction P=.54 is separate; no matched contradiction or model-compatible inversion is supplied. |
| S016 | DOC-001 p. 7 says the imputation supine interaction was not significant; DOC-003 p. 7 prints p=.05. This is not mechanically contradictory without the final threshold, unrounded adjusted P, and applicability of the multiplicity rule to interaction tests. Main versus imputed effects have different analysis sets; the stated broadly positive mHealth directions agree. |
| S017 | DOC-001 pp. 7--8 post hoc race narrative has no supplied stratum effect estimate, test statistic, P value, variance, or adjustment rule. The qualitative significance statement is therefore not statistically reconstructable. The age-boundary conflict in C005 is separately source-grounded and does not supply a test for the narrative. |
| S1001 | DOC-002 p. 13’s factorial hospital-randomized GEE logistic model and DOC-001 pp. 3, 7 final cluster-aware GEE description are compatible at supplied detail. Protocol language permits confounders; absent final working correlation/variance details prevent a stricter statistic comparison. |
| S1002 | DOC-002 p. 13’s interaction-then-main-effects branching rule is compatible with DOC-001 Table 3’s multiplicative interaction label and interaction-model supine display. The source does not provide the final interaction decision criterion, so no stricter branch-test rule is inferred. |
| S1003 | DOC-002 pp. 13--14 planned Bonferroni alpha .0125 and DOC-001/DOC-003 final Hochberg-adjusted P labels are distinct procedures. Neither is evidence that the same matched P value should equal another; amendment/history and final rule documentation are missing. |
| S1004 | DOC-002 p. 13 provides planned mediation and breastfeeding model definitions but no matched final numeric effect, CI, P value, or test statistic in supplied sources. Absence of a final duplicate is not a reporting-consistency candidate. |
| S1005 | DOC-002 p. 14’s 1600 enrollment, 1280 analysis total, and 320/group arithmetic agrees with DOC-001 planning. The protocol’s 96% main-effect and 80% combined-versus-one powers concern different stated contrasts; DOC-001’s 80% wording does not identify an identical simulation estimand. |
| S1006 | DOC-003 pp. 3--4 chi-square labels and P values .5206, .2039, and `<.0001` have compatible main-article P-bound repetitions. C002 confirms a separate 917/1263 percentage discrepancy and C003 confirms unlabeled reduced bases in different eTable 2 blocks; neither creates a P/test contradiction. Statistic, degrees of freedom, and test correction remain unreported. |
| S1007 | DOC-003 p. 8 clearly distinguishes aR, aRD derived from logistic ORs/CIs, Hochberg-adjusted logistic P values, multiplicative interaction P values, and the soft-bedding covariate exception. The labels rule out treating raw count differences as aRD recalculations beyond display-level checks. Model covariance and transformation procedure remain missing. |
| S1008 | DOC-003 p. 7 imputed supine effects have ordered CIs containing 2.8% and 9.0%; 81.6-78.8 = 2.8 and 87.8-78.8 = 9.0 points. Signs, outcome direction, and adjustment labels agree. p=.05 interaction is not assigned a significance interpretation without the required final rule. |
| S1009 | DOC-003 p. 7 imputed room-sharing effects have ordered CIs containing 3.9% and 12.0%; 73.6-69.7 = 3.9 and 81.7-69.7 = 12.0 points. P labels, outcome direction, and effect scale agree; `<.001` is an inequality display, not a display zero. |
| S1010 | DOC-003 p. 7 imputed no-soft-bedding effects have ordered CIs containing 3.4% and 11.7%; 70.8-67.4 = 3.4 and 79.1-67.4 = 11.7 points. The stated omitted SAFE-rate covariate is a label distinction, not an inconsistency. |
| S1011 | DOC-003 pp. 7--8 imputed pacifier effects have ordered CIs containing 5.7% and 6.8%; 65.9-60.2 = 5.7 and 67.0-60.2 = 6.8 points. The 0.0 CI endpoint is a rounded interval boundary, not a P-value display. Exact P/CI inversion is unavailable under the stated Hochberg/OR-to-aRD framework. |
| S1012 | DOC-003 pp. 9--11 raw frequency display arithmetic and all matched Table 3/eTable 5 values were revisited. C001 remains the distinct 205/291 display conflict (70.4% versus 70.5%); C005 remains the distinct `≥60` versus `>60` linked table/figure label conflict. Every other eTable 5 displayed count/denominator/percentage and the figure’s 0--100 percentage scale are compatible at displayed precision. No test/effect estimate is supplied for the post hoc strata. |

## Stable-ledger and mechanical-recheck reconciliation

The complete ledger ID set (`C001`, `C002`, `C003`, `C004`, `C005`) equals the complete mechanical-recheck ID set. Every recheck cited location was found and reproduced its direct printed comparator/rule/calculation. The following implications were revisited in this pass:

| Stable ID | Statistical-pass-2 implication |
|---|---|
| C001 | Relevant to S011/S1012. It is an independent raw count/percentage and cross-location display conflict for 205/291, not an adjusted-effect or P-value inconsistency. The recheck confirms its source locations and calculation. |
| C002 | Relevant to S005/S1006. It is a direct eTable 2 count/denominator percentage issue. The ledger and recheck identify the exact location as DOC-003 PDF p. 3; an earlier provisional numeric-checker link to p. 4 was corrected. The main narrative’s nonidentical 8--12-week wording remains a limitation; the within-eTable 917/1263 calculation is independently reproducible. |
| C003 | Relevant to S005/S1006. It concerns the disclosure of eTable 2 education and marital-status percentage bases, not the chi-square P values. Variable-specific nonmissing denominators/missingness definitions are not supplied. |
| C004 | Relevant to the denominator/scale context of DOC-003 baseline tables, but no distinct inferential relationship has an unreported test or P value to reconcile. The recheck confirms reduced category totals and percentage bases; missingness handling remains undefined. |
| C005 | Relevant to S017/S1012. It is a direct linked-display population-boundary label issue (`≥60` versus `>60`), not a derived claim about any exactly-60-day record or a statistical-significance contradiction. |

## Display-zero exclusion

**DISPLAY_ZERO_NOT_CANDIDATE records: 0.** No assigned relationship prints `P = 0`, `p = 0.000`, or an equivalent finite-precision zero. `P < .001` and `<.0001` are inequality displays, not display zeros. No tail probability was derived.

## New-candidate register

**STAT2-NEW candidates: 0.** No additional distinct candidate was emitted. The recheck found no new supplied-source contradiction separate from C001--C005. In particular, no candidate is created from an unreported model detail, protocol-versus-final-method difference without a same-result comparator, transformed-CI/Hochberg-P apparent tension, an analysis-set difference, or finite-precision notation.

## Limitations and missing definitions

- No raw logistic ORs, covariance, variance estimator, working correlation, degrees of freedom, individual-test sidedness, exact aRD conversion procedure, or common CI/P inversion rule is supplied.
- The protocol gives planned Bonferroni rules, while the results give final Hochberg-adjusted P labels; final amendment/decision-rule documentation is not supplied.
- No stratum effect estimates/tests support mechanical checking of the qualitative post hoc race significance narrative.
- C001 lacks production percentage/export rules; C002 lacks its exact production basis and has a nonidentical narrative age-bin label; C003/C004 lack variable-specific missingness denominators; C005 lacks the operational age filter and the number of exactly-60-day records.

## Pass-2 counts

- **Relationships explicitly completed:** 29 (S001--S017; S1001--S1012).
- **Stable ledger IDs reconciled:** 5 (C001; C002; C003; C004; C005).
- **New distinct candidates:** 0.
- **DISPLAY_ZERO_NOT_CANDIDATE records:** 0.
