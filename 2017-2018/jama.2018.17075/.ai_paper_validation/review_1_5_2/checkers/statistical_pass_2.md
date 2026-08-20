# Statistical Consistency Review — Pass 2

**Runtime agent ID:** `/root/statistics_pass_2`  
**Execution:** fresh `gpt-5.6-terra`, high reasoning effort; distinct from pass 1.  
**Scope:** Every canonical inferential-statistical relationship, `S001`--`S032`, revisited after registration of the complete `C001`--`C008` ledger and the independent mechanical evidence recheck. Only fresh supplied-source evidence and current fresh-run artifacts were used; no legacy audit derivative or external source was used.

## Pass-2 rule

For each S record, this pass revisited denominators, displayed arithmetic, estimate containment, interval endpoint ordering, sign/direction, effect-measure and scale labels, duplicate/repeated values, cross-source comparators, and all applicable ledger/recheck implications. Interval/P-value/test/statistic/SE compatibility was assessed only where supplied evidence defined a compatible analysis rule. Missing sidedness, degrees of freedom, coefficient/SE, covariance, variance estimator, continuity-correction choice, information fraction, multiplicity rule, model-to-estimand mapping, or participant/imputed data is named below rather than inferred. Any count-based calculation noted in the linked ledger/recheck remains a diagnostic approximation, not a reconstruction of the reported analysis.

## Complete S-ID recheck

| S ID | Pass-2 record | Result, candidate linkage, and exact limitation |
|---|---|---|
| S001 | `PASS_2_COMPLETE`. Revisited the randomized-group/no-imputation definition, unadjusted chi-square, RR/RD and 95% CI conventions against the main displays. | Definition-only; no point/interval or cross-location result is supplied here. No new observation. The chi-square continuity correction and variance/CI implementation are not supplied. |
| S002 | `PASS_2_COMPLETE`. Rechecked the adjusted log-binomial RR `0.98 (0.87-1.11), P=.75` and its covariate/random-effect label. | Point is contained in an ordered positive CI; CI contains RR null 1 and label/direction agree. No new observation. Coefficient, SE, random-effect variance, confidence construction, and P-value rule are absent. |
| S003 | `PASS_2_COMPLETE`. Rechecked ordinal OR `0.97 (0.71-1.34), P=.88` and time-to-death HR `1.13 (0.76-1.69), P=.54`, including the DOC-003 HR repeat. | Each point is in its ordered CI and every ratio CI includes 1; measure labels/directions are coherent and the HR repeat is exact. No new observation. Ordinal coefficient/SE and Cox/log-rank test inputs are absent. |
| S004 | `PASS_2_COMPLETE`. Rechecked subgroup interaction labels and `P=.43`/`.33`, plus the cooling-time chi-square definition. | Row placement, outcome direction, and interaction labels are coherent. No new observation. Interaction coefficients, contrast cells, SEs, and exact test variants are not supplied. |
| S005 | `PASS_2_COMPLETE`. Revisited per-protocol/as-treated definitions, two-sided alpha, and stated absence of multiplicity adjustment. | Definition-only; no matched inferential estimate to reconcile. No new observation. A full secondary-comparison model-to-estimand/multiplicity mapping is not supplied. |
| S006 | `PASS_2_COMPLETE`. Rechecked ITT favorable-outcome RR/RD/CI/P locations and C002 recheck facts. | RR `0.99 (0.82-1.19), P=.94` and adjusted RR `0.98 (0.87-1.11), P=.75` are contained in ordered CIs with coherent labels. **Ledger linkage:** C002 is the directly rechecked abstract/body/table signed-RD mismatch; it remains a source comparison, not an inferred correction. No new observation. Adjusted-model coefficient/SE and abstract contrast definition are absent. |
| S007 | `PASS_2_COMPLETE`. Rechecked ordinal OR, six-month mortality RR, and mortality HR labels/intervals. | Points are contained in ordered ratio CIs, all include 1, and higher hypothermia mortality agrees with RR/HR directions. RR and HR are distinct supplied estimands. No new observation. Survival-model/test details are absent. |
| S008 | `PASS_2_COMPLETE`. Rechecked Table 2 secondary-outcome RR/CI/P alignment and C003/C004 recheck facts. | Most points are contained in ordered CIs with count-consistent directions. **Ledger linkage:** C003 and C004 are direct row-specific count/RR and matched P-value contradictions; their raw-RR and two-proportion calculations are diagnostic only. No new observation. The stated unadjusted chi-square rule lacks continuity-correction/test-variant details for exact P reconstruction. |
| S009 | `PASS_2_COMPLETE`. Rechecked subgroup RRs/CIs, row P values, and interaction P values. | Each RR is in an ordered CI including 1; labels, population denominators, and interactions are attached to the printed subgroup rows. No new observation. Interaction coefficients/SEs and exact test definitions are absent. |
| S010 | `PASS_2_COMPLETE`. Rechecked per-protocol and as-treated pneumonia RRs/CIs/Ps against matching eTables. | `1.23 (1.04-1.47), P=.02` and `1.29 (1.09-1.53), P=.003` are contained in ordered CIs above 1; repeats and analysis-population labels agree. No new observation. Exact test/model details are absent. |
| S011 | `PASS_2_COMPLETE`. Revisited secondary proportional-odds/sliding-dichotomy estimand labels. | Definition-only; no result estimate/interval is supplied. No new observation. No model output or estimand-to-final-result mapping is supplied. |
| S012 | `PASS_2_COMPLETE`. Revisited stated ordinal reference `ln(OR)=0.62`, one-sided rank test, `182`/arm, and 96% one-sided power. | No printed internal contradiction. No new observation. Ordinal distribution, allocation/attrition implementation, variance rule, and power formula are absent, so no independent power reconstruction is made. |
| S013 | `PASS_2_COMPLETE`. Revisited Version-9 alpha/interim/multiplicity definitions and protocol-version context. | These are version-specific definitions, not matched final estimands; no conflict is established. No new observation. The cited detailed SAP/update text is not embedded in supplied sources. |
| S014 | `PASS_2_COMPLETE`. Rechecked DSMC normal-approximation/binomial rule, `|Z|>=3`, final `|Z|>=1.975`, alpha, and multiplicity wording. | Labels and boundary directions are coherent. No new observation. Sequential information fractions, alpha-spending inputs, and implementation details are absent, so no boundary recalculation is made. |
| S015 | `PASS_2_COMPLETE`. Rechecked 2015 DSMB GOS-E/outcome P-value array against the displayed groups, counts, and labels. | P values have stated row association; no duplicate final-study comparator is supplied. No new observation. Exact test/variance definitions for this monitoring display are absent. |
| S016 | `PASS_2_COMPLETE`. Rechecked 2016 DSMB P-value array and figure context. | The supplied denominators distinguish GOS-E `321` from six-month survival `341`; row labels, count directions, and P placement are coherent. No new observation. Exact test definitions are absent. |
| S017 | `PASS_2_COMPLETE`. Rechecked 2017 DSMB P-value array and figure context. | The supplied denominators distinguish GOS-E `364` from survival `390`; row labels, count directions, and P placement are coherent. No new observation. Exact test definitions are absent. |
| S018 | `PASS_2_COMPLETE`. Revisited mixed-linear-model eFigure 1, 95% CI, and participant random-effect labels. | The figure has no printed numeric estimates/endpoints for containment or arithmetic checking; no visual value was invented. No new observation. Covariance/SE and numeric graph data are absent. |
| S019 | `PASS_2_COMPLETE`. Rechecked the matching main/supplement Kaplan-Meier/Cox mortality HR. | The exact repeat is `1.13 (0.76-1.69), P=.54`; the point lies in an ordered CI including 1 and the mortality direction agrees. No new observation. Cox/log-rank reconstruction inputs are absent. |
| S020 | `PASS_2_COMPLETE`. Rechecked eTable 2 randomization/timing P-value row linkage and control-temperature `NA` fields. | P values remain aligned to their labelled quantities; `NA` is expressly displayed rather than a missing P value. No new observation. Baseline-test family and distribution assumptions are absent. |
| S021 | `PASS_2_COMPLETE`. Rechecked eTable 4 row wrapping against the rendered page. | `<.0001` is an inequality, not a display zero; `P=.16` remains aligned to receiving adrenaline and `P=.90` to duration. No new observation. Test definitions are absent. |
| S022 | `PASS_2_COMPLETE`. Rechecked eTable 5 outcome P values and displayed outcome order. | P values are in the listed outcome order; no paired estimate/CI or duplicate comparator establishes an inconsistency. No new observation. Test/distribution definitions are absent. |
| S023 | `PASS_2_COMPLETE`. Rechecked eTable 6 adverse-event P values against DOC-001 Table 2 and C003/C004 recheck facts. | **Ledger linkage:** C003 and C004 are direct matched-row P conflicts and row-specific count/effect contradictions. `<.0001` for bradycardia is an inequality, not a display zero. No new observation. Exact chi-square implementation is not supplied. |
| S024 | `PASS_2_COMPLETE`. Rechecked eTable 7 favorable-GOS-E P=.09, temperature-tertile population, and CIs. | Printed points lie in ordered CIs and labels identify the outcome/tertiles. No new observation. Trend/test specification is absent, so no P/CI compatibility reconstruction is made. |
| S025 | `PASS_2_COMPLETE`. Rechecked eTable 8 per-protocol baseline P-value row labels. | Values remain attached to defined baseline variables; no effect/interval contradiction is supplied. No new observation. Baseline test rules are absent. |
| S026 | `PASS_2_COMPLETE`. Rechecked eTable 9 per-protocol RRs/CIs/Ps, interactions, denominators, and labels. | Every RR is in an ordered positive CI; CI/null patterns, analysis population, outcome labels, and interactions are coherent. No new observation. Exact P reconstruction lacks test/model details. |
| S027 | `PASS_2_COMPLETE`. Rechecked per-protocol sensitivity primary RR `1.00 (0.77-1.30), P=.98`. | Point is contained in an ordered CI including 1; sensitivity population, outcome, and direction agree. No new observation. Exact test variant is absent. |
| S028 | `PASS_2_COMPLETE`. Rechecked as-treated baseline P labels and `No. (%)` cells against C005/C006 rechecks. | **Ledger linkage:** C005 and C006 are direct denominator/header/token-order observations for distinct CT rows; their token-reversal readings are diagnostic, not corrections. Baseline P values remain row-aligned. No new observation. Test rules and any row-specific denominator/missingness definition are absent. |
| S029 | `PASS_2_COMPLETE`. Rechecked as-treated RRs/CIs/Ps, interaction P values, denominators, and the adjusted-row outcome label. | Points are contained in ordered CIs. The adjusted row is expressly labelled unfavorable outcome while the unadjusted primary row is favorable outcome; no supplied mapping establishes a direction contradiction. No new observation. Exact adjustment/test details are absent. |
| S030 | `PASS_2_COMPLETE`. Rechecked as-treated sensitivity RR `1.02 (0.80-1.31), P=.85`. | Point is contained in an ordered CI including 1; outcome/population/measure labels agree. No new observation. Exact test variant is absent. |
| S031 | `PASS_2_COMPLETE`. Rechecked missing-outcome scenario RRs/RDs/CIs/Ps and stated chi-square/CMH/Miettinen-Nurminen definitions. | All printed points are within ordered CIs; RR/RD null inclusion is coherent with the reported P-value direction. No new observation. Imputed records, CMH strata, and score-limit inputs are absent, so no exact scenario-3 reconstruction is made. |
| S032 | `PASS_2_COMPLETE`. Rechecked adequate-cooling methods, unadjusted OR `0.91 (0.59-1.41), P=.68`, time estimands, and C007 recheck facts. | Unadjusted estimate is contained in an ordered CI and correctly labelled. **Ledger linkage:** C007 is the direct malformed adjusted-OR interval string; neither `275` nor intended endpoints are inferred. Mean-time `P=.01` and median-time `P=.02` are distinct supplied estimands. No new observation. Adjusted coefficient, SE/covariance, and valid CI endpoints are absent. |

## Existing-ledger and mechanical-recheck integration

| Stable candidate | Pass-2 relationship implication |
|---|---|
| C001 | Numeric-only N024 IQR-order observation; no canonical S relationship is assigned. Considered for cross-lane completeness; no new statistical observation. |
| C002 | Revisited through S006; signed-RD cross-location mismatch remains directly source-grounded. |
| C003 | Revisited through S008 and S023; matched P-value disagreement and count/RR linkage remain directly source-grounded. |
| C004 | Revisited through S008 and S023; matched P-value disagreement and count/RR linkage remain directly source-grounded. |
| C005 | Revisited through S028; header/denominator/token-order observation remains directly source-grounded. |
| C006 | Revisited through S028; denominator/percentage/token-order observation remains directly source-grounded. |
| C007 | Revisited through S032; malformed adjusted-CI string remains directly source-grounded. |
| C008 | Numeric-only N004/N020 count/percentage observation; no canonical S relationship is assigned. Considered for cross-lane completeness; no new statistical observation. |

## Display-zero exclusion

**`DISPLAY_ZERO_NOT_CANDIDATE` count: 0.** No assigned S relationship supplies a coherent result as `P=0`, `p=0.000`, or equivalent. The `<.0001` entries checked in S021 and S023 are inequalities rather than display zeros. No candidate observation is based on P-value display precision.

## New candidate observations

**None.** Complete pass-2 review identified no genuinely new supplied-source contradiction beyond the eight pre-existing ledger records. This is not an adjudication, correction, validity judgment, or severity assessment of any existing candidate.

## Completion and limitations

- **S-ID coverage:** 32/32, `S001`--`S032`, each explicitly marked `PASS_2_COMPLETE`.
- **Existing-candidate coverage:** 8/8, `C001`--`C008`, incorporated with the independent mechanical-recheck facts.
- **New candidate observations:** 0.
- **Limitations:** Supplied sources do not provide participant-level data, unrounded model outputs, model coefficients/SEs/covariances, all test variants, sidedness/df, sequential information fractions, stratum-level or imputation inputs, nor embedded cited SAP/update/correction text. These missing definitions prevent unsupported exact reconstructions but do not prevent the direct printed-value comparisons recorded in the ledger and recheck.
