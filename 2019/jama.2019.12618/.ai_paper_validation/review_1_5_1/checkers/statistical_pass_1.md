# Statistical consistency pass 1

## Scope, method, and boundaries

- **Assigned scope:** every inferential-statistical relationship `S001` through `S101` in `statistics/relationship_inventory.md`; completed `101/101`.
- **Evidence used:** the named mapper evidence and direct supplied PDF pages only: main article `jama_rathinam_2019_oi_190092.pdf`, Supplement 1 `joi190092supp1_prod.pdf`, Supplement 2 `joi190092supp2_prod.pdf`, and Supplement 3 `joi190092supp3_prod.pdf`. No legacy candidate, checker, ledger, or report conclusion was used.
- **Checks applied where definitions permitted:** point-estimate containment and endpoint ordering; sign/direction; effect-measure, scale, population, time-point, contrast, and reference labels; repetition across supplied locations; and interval/P-value/test/statistic/SE compatibility only under a supplied compatible definition. Protocol and SAP records are planned definitions unless a matching observed result establishes the same population, time, contrast, model, and precision.
- **Display-zero rule:** no registered S relationship contains `P = 0`, `p = 0.000`, or equivalent. `DISPLAY_ZERO_NOT_CANDIDATE` records: `0`.
- **Diagnostic convention:** any calculation labelled diagnostic below is a rounding-aware screening calculation, not a substitute for the reported analysis. No sidedness, degrees of freedom, covariance, variance estimator, multiplicity adjustment, denominator, model, or estimand was inferred when absent.

## Per-relationship completion record

| S ID | Direct evidence and pass-1 check | Outcome |
|---|---|---|
| S001 | Main PDF pp. 1, 4, 6-7: MTX-minus-MMF RD 9.5% (−5.3% to 21.8%) contains the estimate and is ordered; OR 1.50 (0.81-2.81) contains 1.50 and crosses 1; both favor MTX and match the 64/96 versus 56/98 direction. The supplied logistic/permuted-P definition permits no direct SE reconstruction. | PASS_1_COMPLETE — no candidate. |
| S002 | Main PDF p. 6: failure-reason block P=.55 has no stated test, statistic, analytic denominator by row, or model. No incompatible comparator is printed. | PASS_1_COMPLETE — compatible test/model definition missing. |
| S003 | Main PDF pp. 1, 5-6: each RD interval contains its estimate and is ordered; each OR interval contains its OR and has direction matching its subgroup counts. Approximate log-OR diagnostics are compatible with P=.07 and .02 after rounding; the interaction P=.004 is a separately defined heterogeneity result. | PASS_1_COMPLETE — no candidate. |
| S004 | Main PDF p. 4: for MTX-minus-MMF, the −5.3% lower 95% CI bound is above the stated −10% noninferiority boundary, so the printed direction/decision are compatible. | PASS_1_COMPLETE — no candidate. |
| S005 | Main PDF pp. 4, 6-7: continued and switched 12-month ORs lie within ordered CIs; directions agree with the original-assignment table labels and the prose's current-treatment description after the supplied switching footnotes are applied. Approximate log-OR diagnostics are compatible with P=.47 and .02. | PASS_1_COMPLETE — no candidate. |
| S006 | Main PDF pp. 4 and 6: Table 2 reports MTX 4.6 (SD 1.0)% and MMF 4.3 (SD 0.5)% under n=96 and n=98, while methods name a Welch t test and the table/prose print P=.87. This requires the draft below. | PASS_1_COMPLETE — candidate draft emitted. |
| S007 | Main PDF pp. 4 and 6: eye-level contrast directions, CIs, and P values are mutually compatible at printed precision. The methods phrase “linear regression model clustering on patient” and Table 2 phrase “linear mixed-effects model” do not supply enough covariance/model detail to establish a contradiction; the SAP's planned mixed model is not proof of the fitted model. | PASS_1_COMPLETE — compatible fitted-model definition missing; no candidate. |
| S008 | Main PDF pp. 6-7: dose-reduction P=.27 and India/country interaction P=.15/.45 match the stated analyses; Supplement 1 p. 13 repeats India .15 and country .45. No compatible estimate/CI/statistic is supplied for the interactions. | PASS_1_COMPLETE — no candidate. |
| S009 | Main PDF p. 7: each Figure 2 OR lies inside ordered CI limits and its direction matches the displayed counts; approximate log-OR diagnostics are compatible with printed P=.20, .93, .08, and .17 subject to random-effect/permutation details. | PASS_1_COMPLETE — no candidate. |
| S010 | Main PDF p. 7: imputation OR 1.4 lies within 0.8-2.4 and has direction matching the imputed proportions. The imputation pooling/statistic/variance rule is not supplied at the observed-result level, so P=.27 is not mechanically reconstructed. | PASS_1_COMPLETE — compatible inferential definition missing; no candidate. |
| S011 | Main PDF p. 4: this is a planned sample-size/power statement, not an observed estimate. The supplied text lacks the exact allocation/site/design-effect calculation needed to recompute it. | PASS_1_COMPLETE — planned definition; no candidate. |
| S012 | Main PDF p. 4: primary patient-level logistic model, six-month population, fixed treatment and random site label match S001/Table 2. No independent incompatible observed model statement is supplied. | PASS_1_COMPLETE — no candidate. |
| S013 | Main PDF p. 4: secondary-method labels identify logistic, clustered eye-level, Fisher, Welch, permutation, and two-sided conventions. They do not alone define all fitted-result variance/test details. | PASS_1_COMPLETE — definitions retained; no candidate. |
| S014 | Supplement 2 PDF pp. 9, 13: planned block randomization/masking definition only; no observed test, CI, or P value. | PASS_1_COMPLETE — planned definition; no candidate. |
| S015 | Supplement 2 PDF pp. 9-10, 15, 18: primary six-month success-rate/proportion estimand definition only; matching requires all endpoint components and population. | PASS_1_COMPLETE — planned definition; no candidate. |
| S016 | Supplement 2 p. 10: secondary outcomes are heterogeneous estimand types without a supplied common estimator/test. | PASS_1_COMPLETE — planned definition; no candidate. |
| S017 | Supplement 2 p. 43: low-vision logMAR conversion table/values are absent; no observed conversion-dependent result is linked. | PASS_1_COMPLETE — conversion definition missing; no candidate. |
| S018 | Supplement 2 p. 46: planned NEI/Davis concordance has no statistic, model, threshold, or observed result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S019 | Supplement 2 p. 47: planned inter-observer variation has no agreement metric, model, threshold, or observed result. | PASS_1_COMPLETE — definition missing; no candidate. |
| S020 | Supplement 2 p. 60: interim analysis is planned but supplies no alpha-spending boundary or model; no observed interim result is supplied. | PASS_1_COMPLETE — definition missing; no candidate. |
| S021 | Supplement 2 pp. 72-74: planned primary six-month proportion comparison supplies no test, CI, adjustment, missing-data, or P-value definition in this range. | PASS_1_COMPLETE — planned definition; no candidate. |
| S022 | Supplement 2 pp. 73, 78-79: planned allocation/masking definition only. | PASS_1_COMPLETE — planned definition; no candidate. |
| S023 | Supplement 2 pp. 73-74: planned secondary/subgroup outcome list lacks a subgroup interaction, censoring, multiplicity, or model definition. | PASS_1_COMPLETE — planned definition; no candidate. |
| S024 | Supplement 2 pp. 80-83: planned composite endpoint algorithm is not an observed inferential result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S025 | Supplement 2 pp. 92-96: visit/retention definitions contain no analysis-population, imputation, covariance, or missing-primary-endpoint rule. | PASS_1_COMPLETE — definition missing; no candidate. |
| S026 | Supplement 2 p. 127: planned NEI-Miami/photo comparison has no reported coefficient, model, population, time point, CI, P-value convention, or missing-data rule. | PASS_1_COMPLETE — planned definition; no candidate. |
| S027 | Supplement 2 p. 129: planned inter-observer agreement has no named metric or observed result. | PASS_1_COMPLETE — definition missing; no candidate. |
| S028 | Supplement 2 p. 139: analysis-committee/R role supplies no model, estimand, CI, test, or P-value rule. | PASS_1_COMPLETE — definition missing; no candidate. |
| S029 | Supplement 2 p. 144: interim timing is supplied but stopping guidelines are undefined and no interim result is printed. | PASS_1_COMPLETE — definition missing; no candidate. |
| S030 | Supplement 2 p. 148: revision-history regression note omits outcome, link, variance, and inference; it cannot be compared as a matched observed model. | PASS_1_COMPLETE — definition missing; no candidate. |
| S031 | Supplement 2 p. 153: REDCap allocation implementation is not an analysis model or observed inferential result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S032 | Supplement 3 p. 16: SAP primary logistic model/LRT definition is planned; no matched observed statistic is printed on this SAP page. | PASS_1_COMPLETE — planned definition; no candidate. |
| S033 | Supplement 3 p. 16: displayed planned logit equation defines the treatment coefficient but has no observed coefficient/statistic. | PASS_1_COMPLETE — planned definition; no candidate. |
| S034 | Supplement 3 pp. 16-17: planned site/country interaction alternatives do not establish a later fitted model. | PASS_1_COMPLETE — planned definition; no candidate. |
| S035 | Supplement 3 p. 17: planned two-sided permutation P rule matches the main-paper method label, with no conflicting observed definition. | PASS_1_COMPLETE — no candidate. |
| S036 | Supplement 3 p. 17: planned anatomic interaction model is definition evidence only; do not infer that it supplies the exact observed interaction calculation. | PASS_1_COMPLETE — planned definition; no candidate. |
| S037 | Supplement 3 pp. 17-18: planned sensitivity/diagnostic convention has no observed result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S038 | Supplement 3 p. 18: planned 12-month Wald/joint-test definition is not a matched observed result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S039 | Supplement 3 p. 18: planned Cox/supplementary survival analyses have no observed hazard estimate/test. | PASS_1_COMPLETE — planned definition; no candidate. |
| S040 | Supplement 3 pp. 18-19: planned BSCVA mixed model has no observed coefficient/CI/statistic. | PASS_1_COMPLETE — planned definition; no candidate. |
| S041 | Supplement 3 p. 19: planned QOL mixed model has no observed result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S042 | Supplement 3 p. 19: planned polytomous/Fisher discontinuation analysis has no observed test result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S043 | Supplement 3 pp. 19-20: planned steroid-discontinuation/macular-edema/thickness tests have no matched observed estimate. | PASS_1_COMPLETE — planned definition; no candidate. |
| S044 | Supplement 3 p. 20: planned Bayesian analysis has no observed posterior quantity. | PASS_1_COMPLETE — planned definition; no candidate. |
| S045 | Supplement 3 p. 20: planned vitreous-haze clustered model/McNemar alternative has no observed result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S046 | Supplement 3 p. 20: planned AE rate/proportion and dose-reduction analyses are not observed tests. | PASS_1_COMPLETE — planned definition; no candidate. |
| S047 | Supplement 3 p. 21: planned rescue logistic model has no matched observed result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S048 | Supplement 3 p. 21: planned rescue rates/CIs and alpha convention have no observed comparator. | PASS_1_COMPLETE — planned definition; no candidate. |
| S049 | Supplement 3 p. 22: diagnostic-test list is planned only. | PASS_1_COMPLETE — planned definition; no candidate. |
| S050 | Supplement 3 p. 22: robust/bootstrap-SE response is conditional planning, not an observed SE/result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S051 | Supplement 3 pp. 22-23: primary sample-size formula/assumptions are planning values; exact simulation/design calculation is not an observed test. | PASS_1_COMPLETE — planned definition; no candidate. |
| S052 | Supplement 3 p. 23: planned simulation/interim adjustment/reassessment contains no observed result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S053 | Supplement 3 p. 24: time-to-control sample-size formula is planning only. | PASS_1_COMPLETE — planned definition; no candidate. |
| S054 | Supplement 3 pp. 24-25: secondary-power methods are planning only. | PASS_1_COMPLETE — planned definition; no candidate. |
| S055 | Supplement 3 p. 26: Aim 2 availability equation is planning only. | PASS_1_COMPLETE — planned definition; no candidate. |
| S056 | Supplement 3 p. 26: Aim 2 power equation is planning only. | PASS_1_COMPLETE — planned definition; no candidate. |
| S057 | Supplement 3 p. 28: planned rescue LRT/failure-reason alpha rule has no observed statistic. | PASS_1_COMPLETE — planned definition; no candidate. |
| S058 | Supplement 3 pp. 28-29: planned MI/GLMM hierarchy has no observed pooled result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S059 | Supplement 3 p. 29: planned MI/hot-deck statistic has no observed comparator. | PASS_1_COMPLETE — planned definition; no candidate. |
| S060 | Supplement 3 p. 29: planned multiplicity gate has no observed familywise-result claim. | PASS_1_COMPLETE — planned definition; no candidate. |
| S061 | Supplement 3 p. 30: planned interim alpha-spending timing has no observed interim result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S062 | Supplement 3 p. 31: planned Fisher/chi-square rule has no observed test result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S063 | Supplement 3 p. 34: planned Lan-DeMets/Hwang-Shih-DeCani interim efficacy rule has no observed boundary crossing/result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S064 | Supplement 3 pp. 35-36: planned AE proportion/rate models distinguish logistic proportions from Poisson/negative-binomial recurrent-event rates; no observed result is paired. | PASS_1_COMPLETE — planned definition; no candidate. |
| S065 | Supplement 3 p. 35: planned absence of a futility rule is not an observed inferential assertion. | PASS_1_COMPLETE — planned definition; no candidate. |
| S066 | Supplement 3 p. 56: revised planned six-month logistic random-intercept model/LRT has no printed observed statistic; it is compatible in broad model class with the main article but does not establish identity of every fitting detail. | PASS_1_COMPLETE — planned definition; no candidate. |
| S067 | Supplement 3 p. 56: revised planned permutation P/two-sided alpha rule has no conflicting observed result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S068 | Supplement 3 p. 57: planned anatomic interaction/relative-risk analyses have no observed matched result definition. | PASS_1_COMPLETE — planned definition; no candidate. |
| S069 | Supplement 3 p. 57: planned secondary-analysis convention has no observed result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S070 | Supplement 3 p. 57: planned 12-month primary-model/Wald procedure has no observed model statistic. | PASS_1_COMPLETE — planned definition; no candidate. |
| S071 | Supplement 3 pp. 57-58: planned Cox/supplementary survival models have no observed hazard/result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S072 | Supplement 3 p. 58: planned BSCVA mixed model/LRT has no observed coefficient/CI/statistic. | PASS_1_COMPLETE — planned definition; no candidate. |
| S073 | Supplement 3 p. 59: planned QOL model/Wald t test has no observed result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S074 | Supplement 3 p. 59: planned discontinuation regression/Fisher test has no observed test result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S075 | Supplement 3 p. 59: planned steroid/macular-edema analysis has no observed comparator. | PASS_1_COMPLETE — planned definition; no candidate. |
| S076 | Supplement 3 p. 59: planned baseline-adjusted thickness regression has no observed coefficient/test. | PASS_1_COMPLETE — planned definition; no candidate. |
| S077 | Supplement 3 pp. 59-60: planned Bayesian/alternative-success analyses have no observed posterior/result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S078 | Supplement 3 p. 60: planned clustered vitreous-haze analysis has no observed estimate. | PASS_1_COMPLETE — planned definition; no candidate. |
| S079 | Supplement 3 p. 60: planned AE rate/proportion/dose-reduction analyses have no observed test. | PASS_1_COMPLETE — planned definition; no candidate. |
| S080 | Supplement 3 p. 60: planned one-sided noninferiority rule and orientation are not a matched observed analysis definition. | PASS_1_COMPLETE — exact orientation/observed test definition missing; no candidate. |
| S081 | Supplement 3 p. 61: planned rescue analysis has no observed result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S082 | Supplement 3 pp. 62-63: planned validation/sensitivity procedures have no observed diagnostic statistic. | PASS_1_COMPLETE — planned definition; no candidate. |
| S083 | Supplement 3 pp. 63-64: planned primary power/sample-size statement has no observed test result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S084 | Supplement 3 p. 65: planned time-to-control sample-size formula has no observed result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S085 | Supplement 3 p. 65: planned BSCVA t-test power framework has no observed comparison. | PASS_1_COMPLETE — planned definition; no candidate. |
| S086 | Supplement 3 p. 65: planned SF-36 simplified t-test framework has no observed comparison. | PASS_1_COMPLETE — planned definition; no candidate. |
| S087 | Supplement 3 p. 66: planned rescue-success CI comparison has no matched observed result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S088 | Supplement 3 p. 67: planned two-proportion power formula has no observed test. | PASS_1_COMPLETE — planned definition; no candidate. |
| S089 | Supplement 3 p. 68: planned missing-final-outcome sensitivity/MI rule has no observed imputation detail. | PASS_1_COMPLETE — planned definition; no candidate. |
| S090 | Supplement 3 p. 68: planned longitudinal GLMM hierarchy has no observed fitted result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S091 | Supplement 3 p. 69: planned overall-test gatekeeping has no observed multiplicity claim. | PASS_1_COMPLETE — planned definition; no candidate. |
| S092 | Supplement 3 p. 70: planned interim alpha-spending use has no observed interim result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S093 | Supplement 3 p. 71: literally printed “2 N Fisher's exact test” lacks a defined dimensionality; no observed test is printed and no correction is inferred. | PASS_1_COMPLETE — test definition missing; no candidate. |
| S094 | Supplement 3 p. 73: planned DSMC interim review is administrative/planning evidence without an observed result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S095 | Supplement 3 p. 74: planned efficacy stopping boundary has no observed boundary/result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S096 | Supplement 3 p. 74: planned no-futility rule has no observed application. | PASS_1_COMPLETE — planned definition; no candidate. |
| S097 | Supplement 3 p. 75: planned safety-event proportion versus recurrent-rate models have no observed result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S098 | Supplement 3 p. 76: planned Fisher proportion versus Poisson/negative-binomial rate rule has no observed result. | PASS_1_COMPLETE — planned definition; no candidate. |
| S099 | Supplement 1 p. 13: India×treatment interaction P=.15 matches main PDF p. 7; the source supplies interaction-term P only, without estimate, CI, statistic, df, variance, or direction. | PASS_1_COMPLETE — compatible reconstruction definition missing; no candidate. |
| S100 | Supplement 1 p. 13: site×treatment P=.20 has no main-paper matched value and no supplied estimate, CI, statistic, df, variance, or direction. | PASS_1_COMPLETE — compatible reconstruction definition missing; no candidate. |
| S101 | Supplement 1 p. 13: country×treatment interaction P=.45 matches main PDF p. 7; the source supplies interaction-term P only, without estimate, CI, statistic, df, variance, or direction. | PASS_1_COMPLETE — compatible reconstruction definition missing; no candidate. |

## Candidate draft(s) for coordinator registration

### Draft: reported missed-dose summary versus Welch-test P value

- **Potential category:** Statistical reporting inconsistency.
- **Exact supplied locations:** `jama_rathinam_2019_oi_190092.pdf#page=6`, Table 2, “Missed doses, mean (SD), %”; Table 2 patient-level column headers `Methotrexate (n = 96)` and `Mycophenolate Mofetil (n = 98)`; `jama_rathinam_2019_oi_190092.pdf#page=4`, Statistical Analyses; and PDF p. 6 narrative immediately below Table 2.
- **Direct observation:** Table 2 and its narrative repeat MTX 4.6% (SD 1.0%) versus MMF 4.3% (SD 0.5%), with `P = .87`. The methods expressly state that missed doses were compared by group using a Welch t test.
- **Consistency rule:** A two-group Welch t test using the table's group headers and printed mean/SD summaries should have its P value compatible with the displayed between-group mean difference and standard deviations, allowing normal display rounding.
- **Diagnostic calculation (not the reported analysis):** using the printed values and `n=96, 98`, the standard-error diagnostic is `sqrt(1.0^2/96 + 0.5^2/98) ≈ 0.114`; the mean-difference diagnostic is `0.3/0.114 ≈ 2.63`, corresponding to a two-sided Welch P of approximately `.01`, rather than `.87`. The table/narrative rounding precision is not enough to bridge this difference at these displayed group sizes.
- **Alternative source-grounded interpretation and exact human question:** determine from the analysis dataset whether the missed-dose row used a different unprinted analytic sample, a differently scaled/unrounded value, a different summary/denominator, or a P value associated with another comparison. The supplied article does not print subject-level values, the unrounded summaries, or a separate row-specific analytic N; those items are required to determine the production source of the mismatch.
- **No display-zero issue:** this draft does not concern finite-precision P-value display.

## Pass-1 totals and limitations

- **Relationships completed:** `101/101` (`S001`-`S101`), each explicitly marked `PASS_1_COMPLETE` above.
- **Candidate drafts emitted:** `1` (the missed-dose Welch-test compatibility draft; no stable candidate ID assigned here).
- **Display-zero records:** `0`.
- **Limitations:** most support S records are planned definitions without matched observed inferential results; many observed P-only results lack statistic, degrees of freedom, variance, covariance, adjustment, or exact analytic-population details. These missing definitions were not inferred.
