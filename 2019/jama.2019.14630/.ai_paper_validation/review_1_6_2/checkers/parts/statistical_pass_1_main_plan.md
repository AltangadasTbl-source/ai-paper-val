# Statistical pass 1: main report and plan specifications

Runtime agent: `/root/stat1_main`; mandatory fresh statistics-pass-1 shard; run model `gpt-6.1-sol`; reasoning effort `high`; start mode `FRESH_SPAWN`. Exact assigned scope is the 92 relationships S001–S064, S400–S419 and S801–S808, individually enumerated with `PASS_1_COMPLETE` in [the inventory](../../statistics/parts/main_plan.md). No other relationship is claimed as assigned coverage. Findings are source-grounded observations awaiting independent inclusion screening, not adjudications.

The complete scope and review contract were read. Inputs were the newly reconstructed main, protocol and support maps and their source-linked reusable text. Every assigned relationship was checked for applicable containment, endpoint order, direction, null/significance agreement, effect/test/method identity, design/population/household/missingness logic, planned rules and sample-size implications. Exact direct-source pages were freshly read with available Poppler `pdftotext -layout` 26.01.0; no new extraction derivative was saved and sources were preserved. Source confirmation included main pp.1,3,4,7,8,11; SAP pp.5,9–12,26; results pp.23–24; protocol pp.52–54. A retained source-linked main p.7 render (`review_1_5_1/preprocessing/evidence_recheck/doc001-p007.png`) was inspected visually to confirm both alcohol rows. CPU processing. No external evidence or previous findings were used.

Confidence intervals are 95%; main p.4 explicitly specifies two-sided tests and significance P<.05. Continuous differences use null zero; ratios use null one. No printed standard errors, test statistics, degrees of freedom, MI pooling details or covariance matrices are supplied for the main rows. Exact numerical P reconstruction is therefore not asserted where those inputs are absent. Diagnostic normal approximations are labelled and do not replace a reported analysis. All main displayed point estimates are contained in their intervals and all interval endpoints are ordered. Except for F-ST1-001, their printed interval/null and P/significance statements agree. Figure 4's arm-specific proportion intervals are not intervals for a between-arm contrast, and were not treated as such. No noninferiority or equivalence claim or margin occurs. Clinical-event interim thresholds are kept separate from this exploratory dietary analysis, which reports no trial stopping decision.

## Findings

### F-ST1-001

**Title:** Alcohol change intervals include zero while the adjacent P values indicate significance.

**Relationships:** S042, S043; S005 supplies the test rule. Proposed relationship type `S_W`; all relationships `S_W`. **Focus area:** B. **Proposed review domain:** `statistical_results`.

**Exact locations and document roles:** REPORT [main p.7, Table 3, Total Alcohol, 6- and 12-month between-group columns](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=7); REPORT [main p.4, Statistical Analysis](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4); REPORT [main p.8, Table 3 footnote b](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=8).

**Printed values:** At 6 months the between-group difference is −0.2 percentage points of energy, 95% CI −0.4 to 0, P=.01. At 12 months it is −0.2, 95% CI −0.4 to 0.1, P=.01. Both arm changes are printed −0.3 (SD3.0) and −0.1 (SD3.0). The column explicitly labels 95% CIs and Table 3 footnote attributes the between-group estimates to mixed-effect models with site and couple random factors. Main p.4 states two-sided tests and P<.05 significance.

**Rule and reproduced comparison:** Both printed intervals contain the null 0: −0.4≤0≤0 at 6 months and −0.4<0<0.1 at 12 months. Both P=.01 values are below .05. For an interval and corresponding two-sided test under the stated levels, these significance readings do not reconcile. Point containment and endpoint order themselves reconcile. The display-precision rule is inapplicable to this route-A-category-1 conflict; the zero endpoint is not discarded as rounding. No unreported variance estimator, sidedness or degrees of freedom is assumed, and no exact replacement P is proposed.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** The 6- and 12-month intervention-versus-control alcohol-energy change effects, their CIs and their significance readings.

**Why context does not resolve it:** This is an always-register printed interval-versus-P conflict. Both rows are attached to the same between-group contrast; the report does not identify different inferential procedures for the CI and P.

**Alternatives and missing definition:** CIs and P values might derive from different procedures, models or pooling calculations, but no such distinction is supplied. At 6 months an underlying negative upper endpoint could print as zero; route A retains the printed conflict. The 12-month upper endpoint is positive even at its one-decimal half-unit lower limit (.05).

**Exact human question:** Which model, MI pooling calculation and test produced each alcohol CI and P value, and which interval and P should be extracted for each time point?

### F-ST1-002

**Title:** Outcome hierarchy changes between the supplied plans and the interim report.

**Relationships:** S006, S400, S405, S417, S801 and S808; report effects S008, S012, S027–S051, S052–S064. Proposed relationship type `P_R`; all relationships `P_R`. **Focus area:** D. **Proposed review domain:** `protocol_report`.

**Exact locations and document roles:** PLAN [SAP p.5, objectives](../../../../joi190106supp2_prod_1635377898.49605.pdf#page=5), PLAN [SAP p.9, Table 1 primary body-weight row](../../../../joi190106supp2_prod_1635377898.49605.pdf#page=9), PLAN [SAP p.10, intermediate diet/nutrients, BP and lipids rows](../../../../joi190106supp2_prod_1635377898.49605.pdf#page=10); PLAN [protocol p.38, intermediate markers](../../../../joi190106supp1_prod_1635377898.47058.pdf#page=38); REPORT [main p.1, Main Outcomes and Measures](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=1), REPORT [main p.3, Outcomes](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=3), REPORT [main p.4, continued Outcomes](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4).

**Printed statements:** SAP lists two primary endpoints, incident composite CVD and weight loss/maintenance. Table 1 expressly assigns body-weight change primary status at M6 and Y1 as well as Y6; diet (17-/14-item scores) and nutrients, BP and lipids are intermediate outcomes at M6/Y1. Protocol also places dietary and biochemical markers in its intermediate-marker section. Main calls 12-month er-MedDiet change the primary endpoint for this interim analysis; MEDAS, other scores, nutrients/food intake and cardiovascular risk factors including body weight, BP and lipids are secondary endpoints/outcomes.

**Rule and reproduced comparison:** Match the same body-weight and dietary/marker constructs at the same Y1 window. Planned primary body weight is reported as secondary; planned intermediate dietary adherence is reported as primary, and planned intermediate nutrients/BP/lipids are reported as secondary. This is a status comparison, so numeric display precision is not applicable. CVD follow-up remains ongoing and is not alleged to have been omitted from a completed CVD analysis.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecification and outcome-status fields for the primary er-MedDiet 12-month difference 2.2 (2.1–2.4), body-weight change and the dietary/biochemical outcomes reported at 12 months.

**Why context does not resolve it:** Changed prespecified outcome status is an always-register category. The report expressly identifies an interim exploratory analysis and a primary endpoint for that analysis; this is an alternative scope explanation, but does not remove the observed status change from the supplied plans.

**Alternatives and missing definition:** The interim report may deliberately adopt a publication-specific hierarchy while leaving the overall-trial hierarchy intact. An interim-specific plan or amendment could authorize that hierarchy, but none is supplied in the mapped package. No protocol violation or outcome-switching mechanism is inferred.

**Exact human question:** Which supplied or additional interim-specific plan defines the report's outcome hierarchy, and how should primary/secondary/intermediate status and prespecification be recorded for its 12-month outcomes?

### F-ST1-003

**Title:** Main and sensitivity priorities for completer and imputed analyses are reversed.

**Relationships:** S002, S004, S407, S412. Proposed relationship type `P_R`; all relationships `P_R`. **Focus area:** D. **Proposed review domain:** `protocol_report`.

**Exact locations and document roles:** PLAN [SAP p.26, lines777–780](../../../../joi190106supp2_prod_1635377898.49605.pdf#page=26); PLAN [SAP p.13, lines305–308](../../../../joi190106supp2_prod_1635377898.49605.pdf#page=13); REPORT [main p.4, Statistical Analysis](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4); REPORT [main p.5, Table 2 header](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5); REPORT [results p.23, eTable9 MI and completer columns](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=23).

**Printed statements:** SAP p.13 provides both full-data and MI ITT analyses; its more specific p.26 says main analyses use completers only and MI repeats are sensitivity analyses. Main p.4 says principal analyses include baseline-eligible participants regardless of incomplete follow-up, with MI; completer-only analyses are described as post hoc sensitivities. Table 2's main header is MI, I3272/C3311. For the matching planned primary body-weight result, eTable9 prints MI difference −2.9 kg (−3.2 to−2.6) and completer difference −3.1 (−3.4 to−2.7).

**Rule and reproduced comparison:** The two analysis approaches are present in both documents, but their assigned principal/sensitivity status differs. SAP p.13's general availability does not eliminate p.26's explicit ordering. The comparison is of analysis designation rather than effect arithmetic; no precision test is applicable.

**Qualifying route:** Route B.

**Affected result or extracted value:** Which analysis is considered principal for the interim primary er-MedDiet effect and for 12-month body weight, including the distinct printed body-weight estimates −2.9 versus −3.1 kg.

**Why context does not resolve it:** The supplied SAP does not describe an exception for this interim report; the report's post hoc designation does not state that it supersedes SAP ordering. The designation affects selection of an analysis for extraction even though both are reported.

**Alternatives and missing definition:** The interim analysis could deliberately use a different principal approach, or SAP wording could apply chiefly to long-term event analyses. An interim-specific rule defining the intended ordering is missing. Both descriptions retain randomized assignment; the observation does not question that coherent ITT grouping rule.

**Exact human question:** Does the supplied SAP's completer-main/MI-sensitivity ordering apply to these interim outcomes, or is there an interim-specific amendment defining MI as principal and completers as post hoc?

### F-ST1-004

**Title:** Reported nutritional imputation specifications differ from the supplied SAP.

**Relationships:** S003, S413. Proposed relationship type `P_R`; all relationships `P_R`. **Focus area:** D. **Proposed review domain:** `protocol_report`.

**Exact locations and document roles:** PLAN [SAP p.26, Missing data, lines788–794](../../../../joi190106supp2_prod_1635377898.49605.pdf#page=26); REPORT [main p.4, Statistical Analysis, imputation paragraph](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4).

**Printed statements:** SAP specifies chained equations, 20 imputations for each missing measurement, outcomes among participants lost for at least 2 years, with sex, age, smoking, leisure PA, baseline BMI/weight, diabetes, hypertension, hypercholesterolemia, family CHD, intervention, second household member and education predictors. Report nutritional main analysis specifies iterative Markov chain Monte Carlo, 8 imputations per missing measurement, follow-up only, with sex, age, smoking, education, BMI, PA, study group, energy and baseline value of the imputed variable. Report has 6- and 12-month missingness.

**Rule and reproduced comparison:** The algorithm name, number, target missingness and predictor list differ. Twenty versus eight is an integer count difference, not a rounded measurement; their half-unit intervals [19.5,20.5] and [7.5,8.5] have gap11, relative to20 equal .55. The algorithm and predictor comparisons are categorical and need no display interval. This is one imputation-specification issue with all changed fields, not separate findings per field.

**Qualifying route:** Route B.

**Affected result or extracted value:** The MI analysis underlying the 12-month er-MedDiet effect and main nutrient/food effects, and their characterization as following the supplied analysis plan.

**Why context does not resolve it:** The SAP provides a positive named method and count, and the report positively provides a different method and count. There is no statement linking the nutritional interim procedure to a separate supplied plan; this is more than an unreported modeling detail.

**Alternatives and missing definition:** The SAP's ≥2-year-loss language may target future clinical outcomes, with a deliberately separate interim nutritional procedure. That scope explanation would distinguish both procedures, but no interim-specific specification is supplied. The eTable9 risk-factor footnote itself describes chained equations; it covers risk-factor outcomes and is not asserted to contradict the nutritional algorithm for the same variable.

**Exact human question:** Which imputation specification applies prospectively to these nutritional interim outcomes, and was the stated MCMC/8-imputation procedure defined separately from the SAP's chained-equations/20-imputation procedure?

### F-ST1-005

**Title:** Planned ancillary multiplicity-adjusted waist intervals are absent under the report's no-adjustment rule.

**Relationships:** S005, S406, S405 and S063. Proposed relationship type `P_R`; all relationships `P_R`. **Focus area:** D. **Proposed review domain:** `protocol_report`.

**Exact locations and document roles:** PLAN [SAP p.12, lines282–291 and footnote comparison2](../../../../joi190106supp2_prod_1635377898.49605.pdf#page=12); PLAN [SAP p.9, secondary waist at M6/Y1/Y6](../../../../joi190106supp2_prod_1635377898.49605.pdf#page=9); REPORT [main p.4, Statistical Analysis](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4); REPORT [main p.8, Risk Factors](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=8); REPORT [results p.23, eTable9 waist row](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=23).

**Printed statements:** SAP requires nominal 95% intervals and ancillary Bonferroni intervals for 27 secondary comparisons, explicitly naming waist change. The Y1 waist outcome is scheduled as secondary. Main states all secondary analyses exploratory and that no additional adjustment for type I error was conducted. The waist result is presented with 95% CI: MI −3.3 cm (−3.6 to−2.9), P<.001; completer −3.3 (−3.7 to−3.0), P<.001. No ancillary adjusted interval is provided in the mapped report materials.

**Rule and reproduced comparison:** The plan calls for an additional interval form, while the report explicitly states no secondary adjustment and prints only nominal intervals. Planned confidence is 1−.05/27=.998148148, approximately99.815%, versus nominal95%; this calculation states the planned rule, and does not attempt to reconstruct an unprinted adjusted CI without variance/pooling details. Display precision is not applicable to the categorical presence/absence of the planned analysis.

**Qualifying route:** Route B.

**Affected result or extracted value:** The 12-month waist effect's interval type and whether its prespecified ancillary multiplicity analysis is available for extraction.

**Why context does not resolve it:** The SAP names waist as a member of the adjustment family and schedules Y1 assessment. The report's exploratory rationale states a different rule but does not identify an interim-specific exception to the planned ancillary analysis. This does not challenge the report's nominal significance itself.

**Alternatives and missing definition:** The Bonferroni family may have been intended for a later comprehensive report; an interim-specific exception could leave nominal inference appropriate here. The package does not define that timing boundary. Intermediate diet/nutrient outcomes were not in the SAP's 27-item family and are not alleged to require its adjustment.

**Exact human question:** Was the planned ancillary Bonferroni waist interval deferred or replaced for the Y1 interim analysis, and is an interim-specific multiplicity rule or adjusted interval available?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| PLAN SAP p.7, weight power; PLAN protocol p.54, corresponding calculation; S402/S807 | With printed point inputs, a diagnostic equal-group normal approximation gives 2(1.959964+.841621)^2×8²/2²=251.164 participants/arm (ceiling252), compared with337. Allowing whole-kg half-unit intervals SD[7.5,8.5] and explicit net difference[1.5,2.5] gives a diagnostic range[141.280,504.072]; it overlaps the printed337 interval[336.5,337.5]. SAP confirms net2; protocol's independent arm-input intervals are even wider. No precision-qualified discrepancy remains and no exact sample-size formula is stated. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN SAP pp.6–7/figure; PLAN protocol pp.53–54/figure; S401/S806 | Graph wording '10% overall' versus prose 'at least10% in control' could denote the event-rate horizon or a pooled-arm rate. No numerical curve point is printed and no explicit required-power target is stated. The ambiguous single-word reading alone does not establish conflicting numeric assumptions. | TERMINOLOGY_OR_WORDING |
| REPORT Table3 p.7, S038–S039 | Model differences .3/.2 differ from subtraction of displayed arm means .6−.4/.7−.5; point values and intervals still contain one another. A mixed-model contrast is not replaced by crude rounded-mean subtraction. | MODEL_VERSUS_CRUDE |
| REPORT main p.4/table footnotes; PLAN SAP pp.25–26, S001/S411/S802–S803 | Fixed-covariate adjustment details and protocol diagnostic outputs are not printed for each current risk result. That absence alone does not demonstrate that a covariate/diagnostic step was absent from the analysis, and the stated mixed models are coherent with site/household/repeated observations. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p.8 Risk Factors, S063, Figures3–4 | 'Clinically meaningful favorable changes' appears beside modest mean contrasts. Immediate context also reports proportions reaching explicitly defined individual-change thresholds; the narrative does not state that the mean contrast itself exceeds every threshold. | CONTEXT_RESOLVES |

## Coverage and limitations

92/92 assigned relationships have explicit `PASS_1_COMPLETE` records; 5 findings; 5 excluded observations. No inferential relationship or source-backed specification in the assigned shard was omitted. No assigned numerical point-containment or endpoint-order conflict was found. Method-specific exact P reconstruction is limited by unprinted degrees of freedom/variance/MI pooling inputs; proportion comparison test and denominators are not specified in Figure4; CVD power has no printed exact curve point or target power; unlabelled boxplot ordinates are not fabricated. These limitations do not remove the categorical checks or positive plan/report comparisons above.

## Explicit per-relationship pass records

This table is the checker completion record. The detailed printed evidence and per-relationship check results are in the companion inventory; `—` means no finding is linked to that relationship, not that checks were omitted.

| Relationship ID | Pass 1 | Finding links |
|---|---|---|
| S001 | PASS_1_COMPLETE | — |
| S002 | PASS_1_COMPLETE | F-ST1-003 |
| S003 | PASS_1_COMPLETE | F-ST1-004 |
| S004 | PASS_1_COMPLETE | F-ST1-003 |
| S005 | PASS_1_COMPLETE | F-ST1-001, F-ST1-005 |
| S006 | PASS_1_COMPLETE | F-ST1-002 |
| S007 | PASS_1_COMPLETE | — |
| S008 | PASS_1_COMPLETE | F-ST1-002 |
| S009 | PASS_1_COMPLETE | — |
| S010 | PASS_1_COMPLETE | — |
| S011 | PASS_1_COMPLETE | — |
| S012 | PASS_1_COMPLETE | F-ST1-002 |
| S013 | PASS_1_COMPLETE | — |
| S014 | PASS_1_COMPLETE | — |
| S015 | PASS_1_COMPLETE | — |
| S016 | PASS_1_COMPLETE | — |
| S017 | PASS_1_COMPLETE | — |
| S018 | PASS_1_COMPLETE | — |
| S019 | PASS_1_COMPLETE | — |
| S020 | PASS_1_COMPLETE | — |
| S021 | PASS_1_COMPLETE | — |
| S022 | PASS_1_COMPLETE | — |
| S023 | PASS_1_COMPLETE | — |
| S024 | PASS_1_COMPLETE | — |
| S025 | PASS_1_COMPLETE | — |
| S026 | PASS_1_COMPLETE | — |
| S027 | PASS_1_COMPLETE | — |
| S028 | PASS_1_COMPLETE | — |
| S029 | PASS_1_COMPLETE | — |
| S030 | PASS_1_COMPLETE | — |
| S031 | PASS_1_COMPLETE | — |
| S032 | PASS_1_COMPLETE | — |
| S033 | PASS_1_COMPLETE | — |
| S034 | PASS_1_COMPLETE | — |
| S035 | PASS_1_COMPLETE | — |
| S036 | PASS_1_COMPLETE | — |
| S037 | PASS_1_COMPLETE | — |
| S038 | PASS_1_COMPLETE | — |
| S039 | PASS_1_COMPLETE | — |
| S040 | PASS_1_COMPLETE | — |
| S041 | PASS_1_COMPLETE | — |
| S042 | PASS_1_COMPLETE | F-ST1-001 |
| S043 | PASS_1_COMPLETE | F-ST1-001 |
| S044 | PASS_1_COMPLETE | — |
| S045 | PASS_1_COMPLETE | — |
| S046 | PASS_1_COMPLETE | — |
| S047 | PASS_1_COMPLETE | — |
| S048 | PASS_1_COMPLETE | — |
| S049 | PASS_1_COMPLETE | — |
| S050 | PASS_1_COMPLETE | — |
| S051 | PASS_1_COMPLETE | — |
| S052 | PASS_1_COMPLETE | — |
| S053 | PASS_1_COMPLETE | — |
| S054 | PASS_1_COMPLETE | — |
| S055 | PASS_1_COMPLETE | — |
| S056 | PASS_1_COMPLETE | — |
| S057 | PASS_1_COMPLETE | — |
| S058 | PASS_1_COMPLETE | — |
| S059 | PASS_1_COMPLETE | — |
| S060 | PASS_1_COMPLETE | — |
| S061 | PASS_1_COMPLETE | — |
| S062 | PASS_1_COMPLETE | — |
| S063 | PASS_1_COMPLETE | F-ST1-002, F-ST1-005 |
| S064 | PASS_1_COMPLETE | — |
| S400 | PASS_1_COMPLETE | F-ST1-002 |
| S401 | PASS_1_COMPLETE | — |
| S402 | PASS_1_COMPLETE | — |
| S403 | PASS_1_COMPLETE | — |
| S404 | PASS_1_COMPLETE | — |
| S405 | PASS_1_COMPLETE | F-ST1-002, F-ST1-005 |
| S406 | PASS_1_COMPLETE | F-ST1-005 |
| S407 | PASS_1_COMPLETE | F-ST1-003 |
| S408 | PASS_1_COMPLETE | — |
| S409 | PASS_1_COMPLETE | — |
| S410 | PASS_1_COMPLETE | — |
| S411 | PASS_1_COMPLETE | — |
| S412 | PASS_1_COMPLETE | F-ST1-003 |
| S413 | PASS_1_COMPLETE | F-ST1-004 |
| S414 | PASS_1_COMPLETE | — |
| S415 | PASS_1_COMPLETE | — |
| S416 | PASS_1_COMPLETE | — |
| S417 | PASS_1_COMPLETE | F-ST1-002 |
| S418 | PASS_1_COMPLETE | — |
| S419 | PASS_1_COMPLETE | — |
| S801 | PASS_1_COMPLETE | F-ST1-002 |
| S802 | PASS_1_COMPLETE | — |
| S803 | PASS_1_COMPLETE | — |
| S804 | PASS_1_COMPLETE | — |
| S805 | PASS_1_COMPLETE | — |
| S806 | PASS_1_COMPLETE | — |
| S807 | PASS_1_COMPLETE | — |
| S808 | PASS_1_COMPLETE | F-ST1-002–005 |

