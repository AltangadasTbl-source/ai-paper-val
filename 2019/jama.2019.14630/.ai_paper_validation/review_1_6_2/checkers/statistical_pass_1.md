# Statistical pass 1: main report and plan specifications

Runtime agent: `/root/stat1_main`; mandatory fresh statistics-pass-1 shard; run model `gpt-6.1-sol`; reasoning effort `high`; start mode `FRESH_SPAWN`. Exact assigned scope is the 92 relationships S001–S064, S400–S419 and S801–S808, individually enumerated with `PASS_1_COMPLETE` in [the inventory](../statistics/parts/main_plan.md). No other relationship is claimed as assigned coverage. Findings are source-grounded observations awaiting independent inclusion screening, not adjudications.

The complete scope and review contract were read. Inputs were the newly reconstructed main, protocol and support maps and their source-linked reusable text. Every assigned relationship was checked for applicable containment, endpoint order, direction, null/significance agreement, effect/test/method identity, design/population/household/missingness logic, planned rules and sample-size implications. Exact direct-source pages were freshly read with available Poppler `pdftotext -layout` 26.01.0; no new extraction derivative was saved and sources were preserved. Source confirmation included main pp.1,3,4,7,8,11; SAP pp.5,9–12,26; results pp.23–24; protocol pp.52–54. A retained source-linked main p.7 render (`review_1_5_1/preprocessing/evidence_recheck/doc001-p007.png`) was inspected visually to confirm both alcohol rows. CPU processing. No external evidence or previous findings were used.

Confidence intervals are 95%; main p.4 explicitly specifies two-sided tests and significance P<.05. Continuous differences use null zero; ratios use null one. No printed standard errors, test statistics, degrees of freedom, MI pooling details or covariance matrices are supplied for the main rows. Exact numerical P reconstruction is therefore not asserted where those inputs are absent. Diagnostic normal approximations are labelled and do not replace a reported analysis. All main displayed point estimates are contained in their intervals and all interval endpoints are ordered. Except for F-ST1-001, their printed interval/null and P/significance statements agree. Figure 4's arm-specific proportion intervals are not intervals for a between-arm contrast, and were not treated as such. No noninferiority or equivalence claim or margin occurs. Clinical-event interim thresholds are kept separate from this exploratory dietary analysis, which reports no trial stopping decision.

## Findings

### F-ST1-001

**Title:** Alcohol change intervals include zero while the adjacent P values indicate significance.

**Relationships:** S042, S043; S005 supplies the test rule. Proposed relationship type `S_W`; all relationships `S_W`. **Focus area:** B. **Proposed review domain:** `statistical_results`.

**Exact locations and document roles:** REPORT [main p.7, Table 3, Total Alcohol, 6- and 12-month between-group columns](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=7); REPORT [main p.4, Statistical Analysis](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4); REPORT [main p.8, Table 3 footnote b](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=8).

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

**Exact locations and document roles:** PLAN [SAP p.5, objectives](../../../joi190106supp2_prod_1635377898.49605.pdf#page=5), PLAN [SAP p.9, Table 1 primary body-weight row](../../../joi190106supp2_prod_1635377898.49605.pdf#page=9), PLAN [SAP p.10, intermediate diet/nutrients, BP and lipids rows](../../../joi190106supp2_prod_1635377898.49605.pdf#page=10); PLAN [protocol p.38, intermediate markers](../../../joi190106supp1_prod_1635377898.47058.pdf#page=38); REPORT [main p.1, Main Outcomes and Measures](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=1), REPORT [main p.3, Outcomes](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=3), REPORT [main p.4, continued Outcomes](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4).

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

**Exact locations and document roles:** PLAN [SAP p.26, lines777–780](../../../joi190106supp2_prod_1635377898.49605.pdf#page=26); PLAN [SAP p.13, lines305–308](../../../joi190106supp2_prod_1635377898.49605.pdf#page=13); REPORT [main p.4, Statistical Analysis](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4); REPORT [main p.5, Table 2 header](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5); REPORT [results p.23, eTable9 MI and completer columns](../../../joi190106supp3_prod_1635377898.49725.pdf#page=23).

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

**Exact locations and document roles:** PLAN [SAP p.26, Missing data, lines788–794](../../../joi190106supp2_prod_1635377898.49605.pdf#page=26); REPORT [main p.4, Statistical Analysis, imputation paragraph](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4).

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

**Exact locations and document roles:** PLAN [SAP p.12, lines282–291 and footnote comparison2](../../../joi190106supp2_prod_1635377898.49605.pdf#page=12); PLAN [SAP p.9, secondary waist at M6/Y1/Y6](../../../joi190106supp2_prod_1635377898.49605.pdf#page=9); REPORT [main p.4, Statistical Analysis](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4); REPORT [main p.8, Risk Factors](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=8); REPORT [results p.23, eTable9 waist row](../../../joi190106supp3_prod_1635377898.49725.pdf#page=23).

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

# Statistical pass 1 — supplementary change rows, support A

Runtime agent ID: root/stat1_support_a. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN.

Scope: S430, S431, S432, S433, S434, S435, S436, S437, S438, S439, S440, S441, S442, S443, S444, S445, S446, S447, S448, S449, S450, S451, S452, S453, S454, S455, S456, S457, S458, S459, S460, S461, S462, S463, S464, S465, S466, S467, S468, S469, S470, S471, S472, S473, S474, S475, S476, S477, S478, S479, S480, S481, S482, S483, S484, S485, S486, S487, S488, S489, S490, S491, S492, S493, S494, S495, S496, S497, S498, S499, S500, S501, S502, S503, S504, S505, S506, S507, S508, S509, S510, S511, S512, S513, S514, S515, S516, S517, S518, S519, S520, S521, S522, S523, S524, S525, S526, S527, S528, S529, S530, S531, S532, S533. Completed 104/104 relationships: eTable 2 MI food changes (44), eTable 3 completer dietary-score changes (8), eTable 4 completer food changes (44), and eTable 5 completer energy/protein/carbohydrate/fat changes (8). The last assigned row is S533, total fat at 12 months, DOC-004 p.14. Remaining eTable 5 rows belong to support B.

## Evidence and checks completed

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Source-linked reusable layout: .ai_paper_validation/document_outputs/DOC-004/supp3_layout.txt, with curator-confirmed direct-source byte identity (Poppler pdftotext 26.01.0). Reread the complete assigned table headers, every assigned row including its wrapped continuation, and all relevant footnotes. [Results source, eTable 2](../../../joi190106supp3_prod_1635377898.49725.pdf#page=3), [eTable 3](../../../joi190106supp3_prod_1635377898.49725.pdf#page=9), [eTable 4](../../../joi190106supp3_prod_1635377898.49725.pdf#page=10), [eTable 5](../../../joi190106supp3_prod_1635377898.49725.pdf#page=14). No new derivative/render/OCR was needed; processing device CPU. Sources and reused assets were preserved.

The exact model/test context is [DOC-001 REPORT p.4 Statistical Analysis](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4): mixed linear models at site, participant and cluster-family levels; completer and multiple-imputation analyses distinguished; all tests two-sided with P < .05 significant; secondary exploratory analyses have no additional multiplicity adjustment. DOC-004 table footnotes establish means with 95% confidence intervals and site/couple random factors. All compared result locations here are REPORT; the potential relationship would be S_W and the review domain statistical_results.

All 312 estimates (I change, C change, between-group change for each of 104 rows) are contained in their intervals, with lower endpoints no greater than upper endpoints. The zero-null status of each between-group 95% CI agrees with its printed P under the stated .05 threshold. There are no interval-versus-P/significance conflicts in this scope. Within-arm P values are absent and were not invented.

All 104 intervention-minus-control changes reconcile under half-unit display intervals. Twenty-four central displayed subtractions differ by one final display unit, but the recomputed contrast and printed-contrast intervals overlap in each case (gap 0, relative discrepancy 0). This checks the same-display model contrast; the source baseline values are medians/IQRs for most foods and were not used as crude substitutes for model-based changes.

A normal-tail diagnostic with CI-width-derived standard error was used only as an approximation, retaining rounding ranges. Every displayed exact P, allowing its own half-unit interval, and every printed '<.001' has compatible values in the diagnostic range. The actual statistic, degrees of freedom, variance estimator, covariance and exact MI pooling/test construction are not supplied, so no exact test reproduction is claimed. In particular, S520 prints P=.001 with contrast −61 (−95 to −27); the diagnostic range .000321–.000588 overlaps the displayed P interval .0005–.0015. No category-1 conflict is reproduced from those values.

S487 (extra-virgin olive oil, completers, 12 months) prints −8 (−16 to 0), P=.05. The printed interval includes zero and printed .05 does not satisfy P<.05, so the displayed null/threshold comparison agrees; no significance finding is emitted. Rounded endpoints/P do not establish any additional conclusion.

The score footnote exception was retained: er-MedDiet completer counts differ from the common table header as explicitly specified on p.10. The table labels, unit scales, population/time keys, randomization and repeated-measures description identify these analyses without a contradictory method step. No noninferiority, equivalence, interim or stopping decision is attached to these rows; no sample-size claim is tested outside this assigned result scope.

## Findings

None. Finding count: 0. Every assigned relationship is explicitly PASS_1_COMPLETE in statistics/parts/support_a.md. No candidate IDs or human dispositions were assigned.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-004 REPORT pp.3,5,6,7,9,10,11,12,14; S432, S436, S442, S450, S451, S465, S468, S480, S488, S491, S492, S496, S499, S502, S509, S510, S512, S513, S516, S517, S520, S521, S527, S533; exact row/outcome/time and calculation in statistics/parts/support_a.md | Repeated pattern: subtracting the printed central arm changes gives a contrast differing by one final displayed unit (1 g/week or kcal/day, or .1 score/percentage point) in 24 rows. Each arm input and printed contrast retain their own half-unit intervals. Every recomputed/printed range overlaps; gap 0 and relative discrepancy 0. For example S480 PDQS six-month: 4.6−2.3=2.3 versus 2.4; recomputed [2.20,2.40], printed [2.35,2.45]. | ROUNDING_OR_DISPLAY_PRECISION |

Excluded-observation count: 1 consolidated pattern (24 affected central-value subtractions). Checks that reconcile directly, absent details without a contradiction, and correctly rejoined wrapped P/CI lines are not additional excluded observations.

## Limitations and handoff

No scientific-coverage limitation within the assigned 104 relationships. Exact reproduction of numeric P values from CI widths is limited by absent test statistics, standard errors, degrees of freedom, variance/covariance and exact test/pooling definitions. The diagnostic approximation is clearly separated from the reported analysis and from mandatory zero-null/CI/P checks. The complete per-row records preserve all three printed estimates/intervals, P, source page, outcome/time/population, rounding ranges, diagnostic bounds and PASS_1_COMPLETE.

Artifacts: checkers/parts/statistical_pass_1_support_a.md; statistics/parts/support_a.md. The coordinator owns the canonical merge. This agent does not perform pass 2.

# Statistical pass 1: support shard B

Runtime agent: `/root/stat1_support_b`; model `gpt-6.1-sol`; effort `high`; start mode FRESH_SPAWN. Exact scope: S420, S421, S422 and each S534 through S640, inclusive (110 grouped relationships: 107 table rows plus 3 figure groups). eTable9 rows each include both MI and completers. Source role: REPORT. Findings: 2; excluded observations: 1. All 110 relationships have PASS_1_COMPLETE below and in `statistics/parts/support_b.md`; no Pass 2 review is claimed.

I read `QUALITY_CONTROL_SCOPE.md` and `workflow_1_6_2/review_contract.md` completely. Evidence: source-identical native layout `.ai_paper_validation/document_outputs/DOC-004/supp3_layout.txt` (full pp.14–24 and statistical footnotes), the new support evidence map's assigned locators, and source-linked retained figure renders at pp.25–27. No prior scientific conclusion, candidate set or report was used.

## Source confirmation and derivative provenance

All rendering uses CPU. Existing figure images: `.ai_paper_validation/review_1_5_1/preprocessing/DOC-004_visual-25.png`, `DOC-004_visual-26.png`, `DOC-004_visual-27.png`; retained Poppler render, historical version unspecified. For exact-source confirmation I newly rendered and visually opened DOC-004 pp.15,22,26 using direct Poppler `pdftoppm` version 26.01.0, 120 dpi, PNG. Commands and resulting package-relative artifacts:

| Source unit | Engine and device | Command | Derivative |
|---|---|---|---|
| DOC-004 p.15 | Poppler pdftoppm 26.01.0, CPU | pdftoppm -f 15 -l 15 -r 120 -singlefile -png joi190106supp3_prod_1635377898.49725.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat1-support-b-p15 | preprocessing/stat1-support-b-p15.png |
| DOC-004 p.22 | Poppler pdftoppm 26.01.0, CPU | pdftoppm -f 22 -l 22 -r 120 -singlefile -png joi190106supp3_prod_1635377898.49725.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat1-support-b-p22 | preprocessing/stat1-support-b-p22.png |
| DOC-004 p.26 | Poppler pdftoppm 26.01.0, CPU | pdftoppm -f 26 -l 26 -r 120 -singlefile -png joi190106supp3_prod_1635377898.49725.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat1-support-b-p26 | preprocessing/stat1-support-b-p26.png |

## Findings

### F-ST1-201

**Title:** Repeated 6-month alcohol confidence-interval versus P-value conflict in sensitivity analyses.

**Relationships:** S542 and S620. **Locations and roles:** REPORT [DOC-004 PDF p.15](../../../joi190106supp3_prod_1635377898.49725.pdf#page=15), eTable5, Total alcohol (%E), 6-month change, between-group columns; REPORT [DOC-004 PDF p.22](../../../joi190106supp3_prod_1635377898.49725.pdf#page=22), eTable8, same outcome/time, between-group columns. These are within the same results supplement: proposed primary relationship S_W, all relationships S_W. **Focus area:** B. **Proposed review domain:** statistical_results.

**Printed values:** Completers: intervention -0.3 (-0.4 to -0.2), control -0.1 (-0.2 to 0), contrast -0.2 (-0.4 to 0), P=.02. Baseline replacement: intervention -0.3 (-0.4 to -0.2), control -0.1 (-0.2 to 0), contrast -0.2 (-0.3 to 0), P=.02. Each table defines the changes as means with 95% CI from mixed models accounting for site and couples as random factors. Population keys differ and are retained: completers 2862/2883 at M6 versus replacement 3272/3311.

**Rule and calculation:** Null for the mean-change contrast is zero. In both rows, lower limit <0 and upper limit =0, so the printed 95% interval includes zero; .02<.05 indicates significance. The same printed row therefore gives incompatible null-exclusion and P classifications. Point estimates remain inside their intervals and endpoint order is coherent; the finding is specifically the printed interval-versus-P relationship. Display-precision intervals and relative-discrepancy calculations are not applied: category 1 explicitly has no rounding exemption. Even if an unrounded upper limit were negative and displayed as zero, this remains a category-1 candidate under the supplied scope.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** The 6-month intervention-minus-control alcohol energy-percentage contrast and its uncertainty/significance in both sensitivity analyses. A reader extracting -0.2 with either printed CI would include the null, while one extracting the P value would classify it as significant at .05.

**Why context does not resolve it:** This is the always-register interval-versus-P category. The source provides 95% confidence labels and a P value in the same contrast row, without a distinct analysis attribution that reconciles the printed readings.

**Alternatives and missing definitions:** The upper endpoint could be a rounded negative bound, or the P and CI could use different inferential constructions. These are alternatives rather than supplied explanations. Exact test implementation, denominator degrees of freedom, variance estimator and unrounded endpoint are not printed. The source does not establish that the P value belongs to an independently defined alternative contrast.

**Exact human question:** For each of the two 6-month alcohol contrasts, what are the unrounded 95% CI limits, and do the printed CI and P=.02 derive from the same mixed-model contrast and inferential construction?

### F-ST1-202

**Title:** Compliance percentages printed inside eFigure2 conflict with their colored bars and plotted intervals.

**Relationship:** S421. **Locations and roles:** REPORT [DOC-004 PDF p.26](../../../joi190106supp3_prod_1635377898.49725.pdf#page=26), eFigure2, all seven paired bars, percentage labels, 95% CI whiskers, y axis and intervention/control legend. Proposed primary relationship S_W; all relationships S_W. **Focus area:** B. **Proposed review domain:** statistical_results.

The title identifies participant percentages complying with intended dietary changes after 12 months. The legend assigns purple to intervention and gray to control; the y axis identifies percentages with 95% CI. The caption attributes P values to between-group comparisons of proportions. The exact printed percentages below are separated from approximate graph readings; no digitization or exact graphical endpoints are claimed.

| Paired bars | Printed I / C percentages | P | Approximate plotted I / C percentages from axis | Direct directional/interval observation |
|---|---|---|---|---|
| Decreased fat | 34 / 32 | .14 | 32 / 34 | Printed I>C, drawn I<C |
| Increased MUFA | 72 / 77 | <.001 | 77 / 72 | Printed I<C, drawn I>C; I label 72 is below its drawn 95% interval (visually about 75–79), C label 77 above its interval (about 70–74) |
| Increased MUFA:SFA | 79 / 86 | <.001 | 86 / 79 | Printed I<C, drawn I>C; I label 79 is below its drawn interval (about 84–88), C label 86 above its interval (about 77–81) |
| Increased fruit | 58 / 63 | <.001 | 63 / 58 | Printed I<C, drawn I>C; I label 58 is below its drawn interval (about 61–65), C label 63 above its interval (about 56–60) |
| Increased vegetables | 56 / 64 | <.001 | 64 / 56 | Printed I<C, drawn I>C; I label 56 is below its drawn interval (about 62–66), C label 64 above its interval (about 54–58) |
| Decreased meat | 60 / 62 | .08 | 62 / 60 | Printed I<C, drawn I>C |
| Decreased sugary dessert | 59 / 58 | <.001 | 68 / 60 | I label 59 is below its drawn 95% interval (about 66–70); the gray bar is also visibly near 60 rather than 58 |

**Rule and calculation:** A percentage labeling a group's bar should identify that bar's percentage and lie inside the group's displayed 95% interval. Multiple labels in this one display fail containment directly, especially MUFA, MUFA:SFA, fruit, vegetables and sugary dessert. The first six printed group contrasts also reverse the drawn order. For example MUFA labels yield I-C=72-77=-5 percentage points, whereas the purple bar is visibly above the gray bar by about +5; vegetables labels give 56-64=-8 while the bars show about +8. Half-unit ranges for those printed contrasts are [-6,-4] and [-9,-7], respectively, and cannot reverse sign. The drawn order is a direct graphical observation rather than an inferred model result.

As an additional conservative magnitude check for the dessert intervention label, enclose its visible bar/whisker region within the deliberately broad graphical range [65,71] percentage points. The printed 59% has half-unit range [58.5,59.5]. Their minimum gap is 65-59.5=5.5 percentage points; relative discrepancy 5.5/59=0.0932>0.05. This bound does not estimate the exact bar value. The point-versus-interval contradiction itself belongs to category 1 and therefore has no display-precision exemption. The P<.001 printed over the dessert pair further identifies why choosing between the tiny labeled contrast and the substantially separated bars matters; no exact P recomputation is claimed without the denominator/test definition.

**Qualifying route:** Route A, category 1 (printed point percentages outside their plotted 95% intervals); the reversals and dessert magnitude also meet the printed-value/direction category 2. Consolidated as one repeated label-to-bar association issue with every affected location retained.

**Affected result or extracted value:** Arm-specific percentages of participants achieving seven favorable dietary changes after 12 months, their intervention-minus-control direction, and the sugary-dessert contrast. Extracting the in-bar labels yields the opposite group direction for the first six categories; the dessert intervention percentage is 59% by label and approximately 68% by graphic.

**Why context does not resolve it:** The issue meets the always-register point-estimate/interval category. The same figure supplies a single arm legend and single time point, yet the percentages, bars and intervals cannot all identify the same group result. Reconstructing likely intended labels would not determine which supplied representation a data extractor should take.

**Alternatives and missing definitions:** Labels may have been associated with the other arm for the first six pairs, or a graphic/legend component may represent a different assignment. Neither a simple global reversal nor label exchange alone reconciles the dessert 59/58 labels with the drawn approximately 68/60 pair. Exact arm denominators, numeric plotted percentages and numeric CI endpoints are not printed. A label/bar population or time-point difference is not disclosed by the caption, and remains only an alternative.

**Exact human question:** Which arm-specific percentages and 95% confidence limits are intended for each of the seven 12-month compliance categories, and how should the printed labels, colored bars and arm legend be reconciled, including the sugary-dessert pair?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-004 p.27, eFigure3 (S422), all M6/M12 nutrient box-and-whisker panels | The figure does not define the whisker rule or print numeric endpoints; these graphical distributions do not supply a contradictory numerical interval, P value or inferential conclusion. Missing that detail alone does not reproduce an in-scope inconsistency. | CONDITIONAL_OR_UNREPORTED |

## Complete pass-1 relationship records

These rows reproduce the shard inventory record mechanically; the source-reading and scientific checks are documented above and in the inventory's scope/check definitions. `RECONCILES` does not assert recovery of unreported degrees of freedom, covariance or exact test implementation. It records ordered/containing intervals, compatible printed null/significance classifications, and no reproduced method or direction conflict for the stated analysis key.

| S ID | Exact source location; quantity | Printed contrast (95% CI); P, or graphical relationship | Pass 1 result | Pass 1 status |
|---|---|---|---|---|
| S420 | DOC-004 p.25 eFigure1, four scores at baseline/M6/M12 | Baseline P .13/.42/.98/.76; all M6/M12 P<.001; colored means and 95% CI | RECONCILES: higher scores favor intervention at follow-up; individual-arm intervals are not contrast intervals | PASS_1_COMPLETE |
| S421 | DOC-004 p.26 eFigure2, seven favorable dietary changes M12 | In-bar I/C percentages 34/32,72/77,79/86,58/63,56/64,60/62,59/58; P .14,<.001,<.001,<.001,<.001,.08,<.001 | F-ST1-202: labels conflict with colored-bar direction and plotted 95% intervals | PASS_1_COMPLETE |
| S422 | DOC-004 p.27 eFigure3, 12 nutrients M6/M12 | Common baseline-SD units, I/C box-and-whisker displays; no printed numerical endpoints or tests | Directions reconcile; whisker rule not specified, no contradictory inferential claim | PASS_1_COMPLETE |
| S534 | DOC-004 p.14 eTable5 SFA M6 | -0.4 (-0.6,-0.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S535 | DOC-004 p.14 eTable5 SFA M12 | -0.4 (-0.5,-0.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S536 | DOC-004 p.14 eTable5 MUFA M6 | 1.2 (0.9,1.4); <.001 | RECONCILES | PASS_1_COMPLETE |
| S537 | DOC-004 p.14 eTable5 MUFA M12 | 0.9 (0.6,1.2); <.001 | RECONCILES | PASS_1_COMPLETE |
| S538 | DOC-004 p.15 eTable5 MUFA:SFA M6 | 0.3 (0.2,0.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S539 | DOC-004 p.15 eTable5 MUFA:SFA M12 | 0.2 (0.2,0.2); <.001 | RECONCILES | PASS_1_COMPLETE |
| S540 | DOC-004 p.15 eTable5 PUFA M6 | 0.5 (0.4,0.6); <.001 | RECONCILES | PASS_1_COMPLETE |
| S541 | DOC-004 p.15 eTable5 PUFA M12 | 0.4 (0.3,0.5); <.001 | RECONCILES | PASS_1_COMPLETE |
| S542 | DOC-004 p.15 eTable5 alcohol %E M6 | -0.2 (-0.4,0); .02 | F-ST1-201: printed CI includes null, P<.05 | PASS_1_COMPLETE |
| S543 | DOC-004 p.15 eTable5 alcohol %E M12 | -0.3 (-0.4,-0.1); .01 | RECONCILES | PASS_1_COMPLETE |
| S544 | DOC-004 p.15 eTable5 fiber M6 | 24 (20,27); <.001 | RECONCILES | PASS_1_COMPLETE |
| S545 | DOC-004 p.15 eTable5 fiber M12 | 19 (16,22); <.001 | RECONCILES | PASS_1_COMPLETE |
| S546 | DOC-004 p.15 eTable5 omega-3 M6 | 0.7 (0.5,0.8); <.001 | RECONCILES | PASS_1_COMPLETE |
| S547 | DOC-004 p.15 eTable5 omega-3 M12 | 0.7 (0.5,0.9); <.001 | RECONCILES | PASS_1_COMPLETE |
| S548 | DOC-004 p.15 eTable5 cholesterol M6 | -53 (-93,-13); .009 | RECONCILES | PASS_1_COMPLETE |
| S549 | DOC-004 p.15 eTable5 cholesterol M12 | -12 (-52,29); .58 | RECONCILES | PASS_1_COMPLETE |
| S550 | DOC-004 p.15 eTable5 sodium M6 | -1.2 (-1.5,-0.9); <.001 | RECONCILES | PASS_1_COMPLETE |
| S551 | DOC-004 p.15 eTable5 sodium M12 | -1.3 (-1.7,-1.0); <.001 | RECONCILES | PASS_1_COMPLETE |
| S552 | DOC-004 p.16 eTable6 er-MedDiet M6 | 2.1 (2,2.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S553 | DOC-004 p.16 eTable6 er-MedDiet M12 | 2.0 (1.9,2.2); <.001 | RECONCILES | PASS_1_COMPLETE |
| S554 | DOC-004 p.16 eTable6 MDS M6 | 0.4 (0.3,0.5); <.001 | RECONCILES | PASS_1_COMPLETE |
| S555 | DOC-004 p.16 eTable6 MDS M12 | 0.4 (0.4,0.5); <.001 | RECONCILES | PASS_1_COMPLETE |
| S556 | DOC-004 p.16 eTable6 MEDAS M6 | 1.0 (0.9,1.1); <.001 | RECONCILES | PASS_1_COMPLETE |
| S557 | DOC-004 p.16 eTable6 MEDAS M12 | 0.9 (0.8,1.0); <.001 | RECONCILES | PASS_1_COMPLETE |
| S558 | DOC-004 p.16 eTable6 PDQS M6 | 2.1 (1.9,2.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S559 | DOC-004 p.16 eTable6 PDQS M12 | 1.9 (1.7,2.1); <.001 | RECONCILES | PASS_1_COMPLETE |
| S560 | DOC-004 p.17 eTable7 olive oil M6 | -3 (-9,3); .27 | RECONCILES | PASS_1_COMPLETE |
| S561 | DOC-004 p.17 eTable7 olive oil M12 | -7 (-13,-2); .01 | RECONCILES | PASS_1_COMPLETE |
| S562 | DOC-004 p.17 eTable7 refined olive oil M6 | -1 (-5,4); .72 | RECONCILES | PASS_1_COMPLETE |
| S563 | DOC-004 p.17 eTable7 refined olive oil M12 | 3 (-2,7); .26 | RECONCILES | PASS_1_COMPLETE |
| S564 | DOC-004 p.17 eTable7 EVOO M6 | -3 (-9,4); .47 | RECONCILES | PASS_1_COMPLETE |
| S565 | DOC-004 p.17 eTable7 EVOO M12 | -10 (-17,-3); .004 | RECONCILES | PASS_1_COMPLETE |
| S566 | DOC-004 p.17 eTable7 nuts M6 | 43 (36,51); <.001 | RECONCILES | PASS_1_COMPLETE |
| S567 | DOC-004 p.17 eTable7 nuts M12 | 28 (20,35); <.001 | RECONCILES | PASS_1_COMPLETE |
| S568 | DOC-004 p.17 eTable7 fruits M6 | 162 (92,233); <.001 | RECONCILES | PASS_1_COMPLETE |
| S569 | DOC-004 p.17 eTable7 fruits M12 | 154 (83,224); <.001 | RECONCILES | PASS_1_COMPLETE |
| S570 | DOC-004 p.17 eTable7 vegetables M6 | 171 (124,218); <.001 | RECONCILES | PASS_1_COMPLETE |
| S571 | DOC-004 p.17 eTable7 vegetables M12 | 169 (121,216); <.001 | RECONCILES | PASS_1_COMPLETE |
| S572 | DOC-004 p.17 eTable7 cereals M6 | -82 (-108,-55); <.001 | RECONCILES | PASS_1_COMPLETE |
| S573 | DOC-004 p.17 eTable7 cereals M12 | -96 (-123,-70); <.001 | RECONCILES | PASS_1_COMPLETE |
| S574 | DOC-004 p.18 eTable7 whole grains M6 | 184 (160,208); <.001 | RECONCILES | PASS_1_COMPLETE |
| S575 | DOC-004 p.18 eTable7 whole grains M12 | 141 (117,165); <.001 | RECONCILES | PASS_1_COMPLETE |
| S576 | DOC-004 p.18 eTable7 refined grains M6 | -303 (-332,-273); <.001 | RECONCILES | PASS_1_COMPLETE |
| S577 | DOC-004 p.18 eTable7 refined grains M12 | -264 (-294,-235); <.001 | RECONCILES | PASS_1_COMPLETE |
| S578 | DOC-004 p.18 eTable7 legumes M6 | 19 (15,23); <.001 | RECONCILES | PASS_1_COMPLETE |
| S579 | DOC-004 p.18 eTable7 legumes M12 | 17 (13,22); <.001 | RECONCILES | PASS_1_COMPLETE |
| S580 | DOC-004 p.18 eTable7 fish M6 | 55 (40,71); <.001 | RECONCILES | PASS_1_COMPLETE |
| S581 | DOC-004 p.18 eTable7 fish M12 | 63 (47,79); <.001 | RECONCILES | PASS_1_COMPLETE |
| S582 | DOC-004 p.18 eTable7 meat M6 | -25 (-42,-8); .01 | RECONCILES | PASS_1_COMPLETE |
| S583 | DOC-004 p.18 eTable7 meat M12 | -9 (-26,8); .31 | RECONCILES | PASS_1_COMPLETE |
| S584 | DOC-004 p.18 eTable7 red meat M6 | -40 (-51,-30); <.001 | RECONCILES | PASS_1_COMPLETE |
| S585 | DOC-004 p.18 eTable7 red meat M12 | -33 (-43,-22); <.001 | RECONCILES | PASS_1_COMPLETE |
| S586 | DOC-004 p.18 eTable7 processed meat M6 | -17 (-24,-10); <.001 | RECONCILES | PASS_1_COMPLETE |
| S587 | DOC-004 p.18 eTable7 processed meat M12 | -9 (-16,-1); .02 | RECONCILES | PASS_1_COMPLETE |
| S588 | DOC-004 p.18 eTable7 pastries M6 | -52 (-61,-43); <.001 | RECONCILES | PASS_1_COMPLETE |
| S589 | DOC-004 p.18 eTable7 pastries M12 | -39 (-48,-30); <.001 | RECONCILES | PASS_1_COMPLETE |
| S590 | DOC-004 p.19 eTable7 dairy M6 | 144 (83,205); <.001 | RECONCILES | PASS_1_COMPLETE |
| S591 | DOC-004 p.19 eTable7 dairy M12 | 137 (76,198); <.001 | RECONCILES | PASS_1_COMPLETE |
| S592 | DOC-004 p.19 eTable7 yogurt M6 | 95 (69,122); <.001 | RECONCILES | PASS_1_COMPLETE |
| S593 | DOC-004 p.19 eTable7 yogurt M12 | 81 (54,107); <.001 | RECONCILES | PASS_1_COMPLETE |
| S594 | DOC-004 p.19 eTable7 fermented dairy M6 | 89 (61,117); <.001 | RECONCILES | PASS_1_COMPLETE |
| S595 | DOC-004 p.19 eTable7 fermented dairy M12 | 76 (49,104); <.001 | RECONCILES | PASS_1_COMPLETE |
| S596 | DOC-004 p.19 eTable7 low-fat dairy M6 | 228 (170,285); <.001 | RECONCILES | PASS_1_COMPLETE |
| S597 | DOC-004 p.19 eTable7 low-fat dairy M12 | 234 (177,292); <.001 | RECONCILES | PASS_1_COMPLETE |
| S598 | DOC-004 p.19 eTable7 whole-fat dairy M6 | -49 (-78,-20); .001 | RECONCILES | PASS_1_COMPLETE |
| S599 | DOC-004 p.19 eTable7 whole-fat dairy M12 | -44 (-72,-15); .003 | RECONCILES | PASS_1_COMPLETE |
| S600 | DOC-004 p.19 eTable7 alcohol g/week M6 | -6 (-10,-3); .001 | RECONCILES | PASS_1_COMPLETE |
| S601 | DOC-004 p.19 eTable7 alcohol g/week M12 | -7 (-10,-3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S602 | DOC-004 p.19 eTable7 red wine M6 | -1 (-3,1); .36 | RECONCILES | PASS_1_COMPLETE |
| S603 | DOC-004 p.19 eTable7 red wine M12 | -1 (-3,1); .36 | RECONCILES | PASS_1_COMPLETE |
| S604 | DOC-004 p.21 eTable8 energy M6 | -85 (-108,-61); <.001 | RECONCILES | PASS_1_COMPLETE |
| S605 | DOC-004 p.21 eTable8 energy M12 | -88 (-111,-64); <.001 | RECONCILES | PASS_1_COMPLETE |
| S606 | DOC-004 p.21 eTable8 protein M6 | 0.9 (0.8,1); <.001 | RECONCILES | PASS_1_COMPLETE |
| S607 | DOC-004 p.21 eTable8 protein M12 | 0.9 (0.8,1.1); <.001 | RECONCILES | PASS_1_COMPLETE |
| S608 | DOC-004 p.21 eTable8 carbohydrate M6 | -1.3 (-1.6,-1); <.001 | RECONCILES | PASS_1_COMPLETE |
| S609 | DOC-004 p.21 eTable8 carbohydrate M12 | -1.2 (-1.5,-0.9); <.001 | RECONCILES | PASS_1_COMPLETE |
| S610 | DOC-004 p.21 eTable8 fat M6 | 0.6 (0.3,0.9); <.001 | RECONCILES | PASS_1_COMPLETE |
| S611 | DOC-004 p.21 eTable8 fat M12 | 0.4 (0.1,0.8); .006 | RECONCILES | PASS_1_COMPLETE |
| S612 | DOC-004 p.21 eTable8 SFA M6 | -0.4 (-0.5,-0.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S613 | DOC-004 p.21 eTable8 SFA M12 | -0.3 (-0.4,-0.2); <.001 | RECONCILES | PASS_1_COMPLETE |
| S614 | DOC-004 p.21 eTable8 MUFA M6 | 1.0 (0.8,1.2); <.001 | RECONCILES | PASS_1_COMPLETE |
| S615 | DOC-004 p.21 eTable8 MUFA M12 | 0.7 (0.5,1.0); <.001 | RECONCILES | PASS_1_COMPLETE |
| S616 | DOC-004 p.22 eTable8 MUFA:SFA M6 | 0.2 (0.2,0.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S617 | DOC-004 p.22 eTable8 MUFA:SFA M12 | 0.2 (0.1,0.2); <.001 | RECONCILES | PASS_1_COMPLETE |
| S618 | DOC-004 p.22 eTable8 PUFA M6 | 0.5 (0.4,0.5); <.001 | RECONCILES | PASS_1_COMPLETE |
| S619 | DOC-004 p.22 eTable8 PUFA M12 | 0.4 (0.3,0.5); <.001 | RECONCILES | PASS_1_COMPLETE |
| S620 | DOC-004 p.22 eTable8 alcohol %E M6 | -0.2 (-0.3,0); .02 | F-ST1-201: printed CI includes null, P<.05 | PASS_1_COMPLETE |
| S621 | DOC-004 p.22 eTable8 alcohol %E M12 | -0.2 (-0.3,-0.1); .01 | RECONCILES | PASS_1_COMPLETE |
| S622 | DOC-004 p.22 eTable8 fiber M6 | 21 (18,24); <.001 | RECONCILES | PASS_1_COMPLETE |
| S623 | DOC-004 p.22 eTable8 fiber M12 | 16 (13,19); <.001 | RECONCILES | PASS_1_COMPLETE |
| S624 | DOC-004 p.22 eTable8 omega-3 M6 | 0.6 (0.4,0.7); <.001 | RECONCILES | PASS_1_COMPLETE |
| S625 | DOC-004 p.22 eTable8 omega-3 M12 | 0.6 (0.4,0.7); <.001 | RECONCILES | PASS_1_COMPLETE |
| S626 | DOC-004 p.22 eTable8 cholesterol M6 | -44 (-79,-8); .02 | RECONCILES | PASS_1_COMPLETE |
| S627 | DOC-004 p.22 eTable8 cholesterol M12 | -6 (-41,30); .75 | RECONCILES | PASS_1_COMPLETE |
| S628 | DOC-004 p.22 eTable8 sodium M6 | -1.1 (-1.4,-0.8); <.001 | RECONCILES | PASS_1_COMPLETE |
| S629 | DOC-004 p.22 eTable8 sodium M12 | -1.1 (-1.4,-0.8); <.001 | RECONCILES | PASS_1_COMPLETE |
| S630 | DOC-004 p.23 eTable9 weight M12, MI / completers | -2.9 (-3.2,-2.6),<.001 / -3.1 (-3.4,-2.7),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S631 | DOC-004 p.23 eTable9 waist M12, MI / completers | -3.3 (-3.6,-2.9),<.001 / -3.3 (-3.7,-3.0),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S632 | DOC-004 p.23 eTable9 BMI M12, MI / completers | -1.1 (-1.2,-1.0),<.001 / -1.1 (-1.3,-1.0),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S633 | DOC-004 p.23 eTable9 cholesterol M12, MI / completers | -1.1 (-2.9,0.7),.23 / -1.1 (-2.8,0.7),.24 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S634 | DOC-004 p.23 eTable9 LDL M12, MI / completers | -0.6 (-2.2,1.0),.48 / -0.6 (-2.2,1.0),.45 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S635 | DOC-004 p.23 eTable9 HDL M12, MI / completers | 1.1 (0.7,1.6),<.001 / 1.3 (0.8,1.7),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S636 | DOC-004 p.24 eTable9 nonHDL M12, MI / completers | -1.9 (-3.6,-0.3),.02 / -2.5 (-4.2,-0.8),.004 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S637 | DOC-004 p.24 eTable9 cholesterol:HDL M12, MI / completers | -0.1 (-0.2,-0.1),<.001 / -0.1 (-0.2,-0.1),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S638 | DOC-004 p.24 eTable9 triglycerides M12, MI / completers | -9.9 (-13.6,-6.3),<.001 / -10.4 (-14,-6.9),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S639 | DOC-004 p.24 eTable9 SBP M12, MI / completers | -1.9 (-2.7,-1.1),<.001 / -1.7 (-2.6,-0.9),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S640 | DOC-004 p.24 eTable9 DBP M12, MI / completers | -1 (-1.4,-0.5),<.001 / -1.0 (-1.5,-0.6),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
