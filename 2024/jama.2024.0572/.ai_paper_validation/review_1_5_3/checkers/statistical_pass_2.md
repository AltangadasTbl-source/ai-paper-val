# Statistical Consistency Review — Pass 2

## Scope and method

This independent pass revisited every stable inferential relationship, `S001` through `S077`, after review of the complete numeric-consistency and cross-source checker outputs, the complete stable candidate ledger (`C001`, `C002`), and the mechanical evidence recheck. Direct-PDF facts in the recheck were treated as controlling for the two matched-source issues. The pass rechecked, where applicable, denominator and population identity, displayed arithmetic, duplicate/repeated results, point-estimate containment, confidence-interval ordering, sign/direction, measure/scale/reference labels, figure implications, and matched-source implications.

No P value was challenged merely because of finite display precision. No mapped relationship is printed as `P = 0`, `p = 0.000`, or an equivalent display zero; `DISPLAY_ZERO_NOT_CANDIDATE` records in this pass: 0. No sidedness, degrees of freedom, covariance, variance estimator, multiplicity procedure, denominator, model, or estimand mapping was inferred when it was not supplied.

`PASS_2_COMPLETE` is a coverage marker only. It does not determine any candidate's validity, severity, correction, acceptance, or other adjudication outcome.

## Relationship-by-relationship pass-2 records

| ID | Pass-2 reconciliation record | Status |
|---|---|---|
| S001 | Main PIM/aGenOR and modified-Poisson/robust-SE definitions retain the stated ITT versus within-arm contexts; no cross-lane conflict beyond C002's `aRR` expansion. No coefficient, SE, or variance estimator is supplied for reconstruction. | PASS_2_COMPLETE |
| S002 | Bootstrap-CI/g-computation and exploratory two-sided-testing definitions match the mapped results; no statistic, SE, or multiplicity-adjusted rule is supplied for a compatibility calculation. | PASS_2_COMPLETE |
| S003 | The 203/336 population and longer-time direction agree with the printed `P<.001`; test type, statistic, SE, and sidedness are not supplied. | PASS_2_COMPLETE |
| S004 | Figure 1 ASPECTS 0-2 estimate 1.52 lies in 0.94-2.46; endpoints and EVT-favouring direction agree. | PASS_2_COMPLETE |
| S005 | Figure/narrative repeat 1.82 (1.40-2.35) for ASPECTS 3-5; the 277-person stratum and `.80` interaction group are compatible. No interaction statistic/SE is printed. | PASS_2_COMPLETE |
| S006 | ASPECTS 6-10 estimate 1.55 lies in 0.81-2.98 with the stated ordinal direction. | PASS_2_COMPLETE |
| S007 | ASPECTS 3 estimate 1.71 lies in 1.04-2.81; labels and direction agree. | PASS_2_COMPLETE |
| S008 | ASPECTS 4 estimate 2.01 lies in 1.19-3.40; labels and direction agree. | PASS_2_COMPLETE |
| S009 | ASPECTS 5 estimate 1.85 lies in 1.22-2.79; the repeated `.80` is attached to the stated 3/4/5 interaction set. | PASS_2_COMPLETE |
| S010 | Core <70 mL estimate 1.78 lies in 1.24-2.56; the 156-person stratum is complementary to S011. | PASS_2_COMPLETE |
| S011 | Core >=70 mL estimate 1.63 lies in 1.23-2.16 and repeats identically in the abstract; 156+180=336. | PASS_2_COMPLETE |
| S012 | Core <100 mL estimate 1.91 lies in 1.44-2.55; 236 is complementary to S013's 100. | PASS_2_COMPLETE |
| S013 | Core >=100 mL estimate 1.41 lies in 0.99-2.02 and repeats in the abstract; its `.29` interaction uses the stated matched strata. | PASS_2_COMPLETE |
| S014 | Core <150 mL estimate 1.82 lies in 1.42-2.34; 296 is complementary to S015's 40. | PASS_2_COMPLETE |
| S015 | Core >=150 mL estimate 1.47 lies in 0.84-2.56 and repeats in the abstract; direction agrees with the ordinal scale. | PASS_2_COMPLETE |
| S016 | No-mismatch (1.2/10) estimate 2.11 lies in 0.97-4.58; 29+307=336 with S017. | PASS_2_COMPLETE |
| S017 | Mismatch (1.2/10) estimate 1.75 lies in 1.38-2.24; `.96` uses the displayed matched comparison. | PASS_2_COMPLETE |
| S018 | No-mismatch (1.8/15) estimate 1.68 lies in 1.17-2.40; 120+216=336 with S019. | PASS_2_COMPLETE |
| S019 | Mismatch (1.8/15) estimate 1.79 lies in 1.33-2.42; direction and `.92` interaction label agree. | PASS_2_COMPLETE |
| S020 | Table 2 within-arm per-ASPECTS aGenORs 0.91 (0.82-1.00) and 0.89 (0.80-0.99) have ordered containing intervals and the worsening-per-decrease direction; no interaction statistic/SE is supplied. | PASS_2_COMPLETE |
| S021 | Per-10-mL aGenORs 0.92 (0.89-0.95) and 0.95 (0.92-0.98) are interval-compatible; the EVT result repeats in the abstract and uses the as-treated Table 2 context. | PASS_2_COMPLETE |
| S022 | Table 2 mRS 0-2 aRR values/intervals and interaction labels are internally ordered; C002 separately records the supplied absolute-reduction versus ratio-scale label conflict. | PASS_2_COMPLETE |
| S023 | Table 2 mRS 0-3 aRR values/intervals and interaction labels are internally ordered; C002 is the sole related measure-label record. | PASS_2_COMPLETE |
| S024 | Table 2 mRS 5-6 aRR values/intervals and interaction labels are internally ordered; C002 is the sole related measure-label record. | PASS_2_COMPLETE |
| S025 | Narrative per-10-mL EVT aGenOR/aRR values repeat Table 2 values with matching direction and population; its `aRR` expansion is the C002 comparator, not a new issue. | PASS_2_COMPLETE |
| S026 | Trend directions agree with `.71` and `<.001` displays and Supplement 5 eFigures; no test/statistic/model definition supports reconstruction. | PASS_2_COMPLETE |
| S027 | Table 3 1.2/10 aGenORs lie in ordered intervals; as-treated subgroup denominators partition 170/166 and interaction `.88` is correctly labeled. | PASS_2_COMPLETE |
| S028 | The MM aRR/aRD intervals contain their estimates; the blank EVT effect cell remains a source display rather than an inferred zero. C002 covers the aRR label conflict. | PASS_2_COMPLETE |
| S029 | Both arm aRR/aRD estimates are contained in ordered intervals; their signs align with the stated mismatch-versus-reference contrast and `.47` label. | PASS_2_COMPLETE |
| S030 | Both arm aRR/aRD estimates are contained in ordered intervals; their signs align with the stated contrast and `.65` label. | PASS_2_COMPLETE |
| S031 | Table 3 1.8/15 aGenORs lie in ordered intervals; as-treated denominators partition 170/166 and interaction `.92` is positioned with the matching profile. | PASS_2_COMPLETE |
| S032 | Table 3 1.8/15 mRS 0-2 aRR/aRD values are interval- and direction-compatible; C002 remains the related label issue. | PASS_2_COMPLETE |
| S033 | Table 3 1.8/15 mRS 0-3 aRR/aRD values are interval- and direction-compatible; C002 remains the related label issue. | PASS_2_COMPLETE |
| S034 | Table 3 1.8/15 mRS 5-6 aRR/aRD values are interval- and direction-compatible; `P>.99` is an inequality, not a display zero. | PASS_2_COMPLETE |
| S035 | Follow-up infarct-volume group values and `.43` narrative agree; test, statistic, variance rule, and SE are absent. | PASS_2_COMPLETE |
| S036 | EVT age/timing aRR intervals and directions are compatible; C002 captures the shared supplied aRR expansion issue. | PASS_2_COMPLETE |
| S037 | Protocol allocation probabilities, weights, and covariate-adaptive formulas remain internally ordered; these are planning definitions, not final estimates. | PASS_2_COMPLETE |
| S038 | Protocol WMW/GLR/CMH primary-analysis definition is distinguished from the exploratory PIM result; no unsupported model identity was assumed. | PASS_2_COMPLETE |
| S039 | Planning distribution, 0.34 standardized effect, sample-size and one-sided-alpha quantities retain their planned context; no observed-result comparison is applicable. | PASS_2_COMPLETE |
| S040 | Adaptive-simulation scenario labels, sample sizes, and power measures retain their stated scenario definitions; raw simulation output is absent. | PASS_2_COMPLETE |
| S041 | Protocol secondary-test, interaction, and missing-data rules are definition records; no unreported final statistic or imputation result is inferred. | PASS_2_COMPLETE |
| S042 | Bayesian priors, posterior threshold inequalities, and probability directions remain ordered; posterior data are not supplied. | PASS_2_COMPLETE |
| S043 | Allocation/interim-bound formula symbols and bounds are internally consistent as printed; no observed Z statistic or covariance is supplied. | PASS_2_COMPLETE |
| S044 | Trial SAP planned maximum/interim and actual-recruitment quantities remain explicitly distinguished from final exploratory reporting. | PASS_2_COMPLETE |
| S045 | Trial-SAP ITT outcome definitions, mRS 5/6 merge, and main-paper definitions agree at the supplied label level. | PASS_2_COMPLETE |
| S046 | Trial-SAP CI, multiplicity, MAR/imputation, and tipping-point definitions are present, but final imputation outputs are absent. | PASS_2_COMPLETE |
| S047 | WMW, ARD, NNT, and generalized-odds definitions retain distinct scales; no mapping of these planned measures onto final PIM estimates is assumed. | PASS_2_COMPLETE |
| S048 | SAP modified-Poisson RR rule supports the ratio-scale comparator used for C002; it supplies no estimate-level statistic or SE for reconstruction. | PASS_2_COMPLETE |
| S049 | Planned subgroup, table, figure, and interaction strata match later displays only where population/analysis context matches; no test is inferred. | PASS_2_COMPLETE |
| S050 | Secondary-SAP as-treated, exploratory, multiplicity, and missing-data definitions agree with the main within-arm context. | PASS_2_COMPLETE |
| S051 | Secondary-SAP imaging and discordance profile definitions match the scale/reference labels of the mapped supplementary displays. | PASS_2_COMPLETE |
| S052 | Secondary-SAP PIM and robust-Poisson definitions support the reported measure classes; coefficients, SEs, and variance details are absent. | PASS_2_COMPLETE |
| S053 | Secondary-SAP subgroup/sensitivity/interactions are planned scope definitions; a plan-versus-observed difference alone is not treated as a conflict. | PASS_2_COMPLETE |
| S054 | Supplement eMethod's lower-AIC/BIC and higher-AUC directions agree with eTable 6 metrics and thresholds. | PASS_2_COMPLETE |
| S055 | eFigure 5 trend P values and directions match main-text CTP/MRI trend descriptions; test statistic is absent. | PASS_2_COMPLETE |
| S056 | eFigure 6 uses `<.001` trend displays with coherent direction; this is not a display-zero case. | PASS_2_COMPLETE |
| S057 | eFigure 7 RR estimates lie in ordered containing intervals; count/denominator and reference labels remain compatible across mapped strata. | PASS_2_COMPLETE |
| S058 | eFigure 8 RR estimates lie in ordered containing intervals; core-volume strata and labels are compatible. | PASS_2_COMPLETE |
| S059 | eFigure 9 RR estimates lie in ordered containing intervals; mismatch-profile labels and interaction positions are compatible. | PASS_2_COMPLETE |
| S060 | eFigure 10 GenOR estimates lie in ordered containing intervals; >1 direction and imaging-definition labels agree. | PASS_2_COMPLETE |
| S061 | eFigure 11 curve axes, 95% CI presentation, and labels are coherent; no printed point estimate permits reconstruction. | PASS_2_COMPLETE |
| S062 | eFigure 12 curve axes, 95% CI presentation, and labels are coherent; no printed point estimate permits reconstruction. | PASS_2_COMPLETE |
| S063 | eFigure 13 curve axes, 95% CI presentation, and labels are coherent; no printed point estimate permits reconstruction. | PASS_2_COMPLETE |
| S064 | eFigure 14 probability/odds axes and age/core direction are coherent; no pixel-derived result is used. | PASS_2_COMPLETE |
| S065 | eFigure 15 probability/odds axes and time/core direction are coherent; no pixel-derived result is used. | PASS_2_COMPLETE |
| S066 | eFigure 16 GenOR estimates are contained in ordered intervals and interaction/imaging-definition labels are compatible. | PASS_2_COMPLETE |
| S067 | eFigure 17 axes and adjusted probability/odds labels are coherent; no printed point estimate permits reconstruction. | PASS_2_COMPLETE |
| S068 | eFigure 18 aRR estimates are interval- and direction-compatible; its ratio-scale use is a supporting comparator for existing C002, not a new candidate. | PASS_2_COMPLETE |
| S069 | eFigure 19 aRR estimates are interval- and direction-compatible; no test statistic or SE is printed. | PASS_2_COMPLETE |
| S070 | eFigure 20 has no inferential estimate; category directions and denominators were considered with C001, whose exact Figure 2/eTable 2 scope is separately recorded. | PASS_2_COMPLETE |
| S071 | eTable 3 aGenOR/aRR estimates lie in ordered containing intervals; site-adjudicated sensitivity population is separately labeled. | PASS_2_COMPLETE |
| S072 | eTable 4 CTP-only estimates lie in ordered containing intervals; `N/A` cells remain distinct from zero or missing estimates. | PASS_2_COMPLETE |
| S073 | eTable 5 per-10-mL composite-core estimates lie in ordered containing intervals; adjustment and interaction labels are source-specified. | PASS_2_COMPLETE |
| S074 | eTable 6 AUC estimates lie in ordered containing intervals; AIC/BIC direction agrees with S054's supplied definition. | PASS_2_COMPLETE |
| S075 | eTable 7 adjusted GenOR/RR/RD and interaction displays are interval-, sign-, denominator-, and label-compatible; aRR/aRD remain distinct labels. | PASS_2_COMPLETE |
| S076 | eTables 8-10 discordance GenOR/aRR/aRD displays are contained in ordered intervals with population/reference labels preserved; existing C002 is the only aRR-expansion issue. | PASS_2_COMPLETE |
| S077 | eTables 11-13 P values and model-adjacent descriptives use inequalities such as `<.001`; compatible test/statistic definitions are absent and no display-zero candidate applies. | PASS_2_COMPLETE |

## Cross-lane candidate and recheck reconciliation

- **C001:** The direct-PDF recheck establishes matching ITT labels, arm denominators, Figure 2 legend order, and the unique nearest-whole-percent count vectors. The Figure-derived mRS 0-2/0-3 counts differ from eTable 2 while mRS 5-6 and mortality reconcile. This pass found no additional inferential contradiction beyond that registered cross-source/denominator candidate. Its unresolved definitions are the raw category counts, unrounded percentages, figure dataset/version, and percentage-calculation rule.
- **C002:** The direct-PDF recheck establishes that the main narrative and Tables 2-3 expand `aRR` as absolute risk reduction while the footnote explicitly uses a greater-than-1 rate-ratio interpretation, values/intervals are ratio-scale, `aRD` is separately absolute, and SAPs specify modified-Poisson relative-risk context. This pass found no independent new issue beyond the registered measure/label/scale candidate. The exact intended `aRR` expansion and whether it means risk ratio or rate ratio remain absent.

## Result and limitations

- Relationships revisited: 77 (`S001`-`S077`).
- Existing stable candidates reconsidered: 2 (`C001`, `C002`).
- Genuinely new pass-2 candidates emitted for coordinator append/recheck: 0.
- Interval/P-value/test/statistic/SE reconstruction was not performed where compatible test, sidedness, degrees of freedom, covariance, variance estimator, statistic, or SE was not supplied.
- No new candidate was based on a P-value display convention.
