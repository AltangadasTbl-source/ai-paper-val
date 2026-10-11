# Independent inclusion screen — initial stage

Scope: all 18 defined findings in the current canonical numeric, cross-source and statistical-pass-1 artifacts. Read QUALITY_CONTROL_SCOPE.md completely and the review contract, including its inclusion-screen section. Decisions apply reproduced AND (Route A OR all Route B criteria), after the cross-location comparison tier. No candidate-count target, prior AI conclusion, external literature, severity or disposition was used. The coordinator assigned C001 through C009 after this independent screen; every included row in a consolidated group names the same stable ID.

## Screening table

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | SCREENED_OUT | NOT_REPRODUCED | — |
| F-NUM-101 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C008 |
| F-NUM-102 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C009 |
| F-XS-001 | cross_source_consistency_reviewer | initial | SCREENED_OUT | NOT_REPRODUCED | — |
| F-XS-002 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-XS-003 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-XS-004 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-XS-005 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-XS-006 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-XS-007 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C006 |
| F-XS-008 | cross_source_consistency_reviewer | initial | SCREENED_OUT | TERMINOLOGY_OR_WORDING | — |
| F-ST1-001 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C007 |
| F-ST1-002 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-ST1-003 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-ST1-004 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-ST1-005 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C006 |
| F-ST1-201 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C007 |
| F-ST1-202 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C009 |
| F-ST2-001 | statistics_pass_2 | pass_2 | INCLUDE | MEETS_THRESHOLD | C005 |

## One-sentence independent justifications

- **F-NUM-001:** The reproduced source distinguishes unavailable nutritional information from completed follow-up, so 5776 nutritional completers is not an independently supplied visit-completion count contradicting 6583 and the numerical discrepancy depends on aligning different quantities.
- **F-NUM-101:** Route B qualifies because the intervention baseline red-wine median 33 exceeds its upper quartile 29 even after half-unit allowances (minimum gap 3, relative discrepancy 0.09091), leaving a named extracted baseline quantity unresolved within its own display.
- **F-NUM-102:** Route A, category 1 qualifies through the same issue documented in F-ST1-202 because several in-bar percentages are outside their own plotted 95% intervals, while the repeated bar/label direction and magnitude conflicts also satisfy Route B.
- **F-XS-001:** Missing nutritional records do not reproduce an incompatible count of completed visits, and the source's endpoint-specific missingness confirms that nutritional completeness and follow-up completion cannot be substituted without an unreported attendance definition.
- **F-XS-002:** Route A, category 5 qualifies because the supplied plans' primary body-weight and intermediate dietary/biomarker statuses change in the interim report, with the publication-specific hierarchy retained as an alternative scope interpretation.
- **F-XS-003:** Route B qualifies because the report applies a baseline nutritional restriction to the reported weight as well as dietary analysis set, the supplied plans do not identify that membership rule for primary weight, and the distinction affects which 6583-versus-6874 population is extracted.
- **F-XS-004:** Route B qualifies because SAP completer-main/MI-sensitivity ordering differs from the report's MI-principal/completer-post-hoc ordering and changes selection between the named weight estimates −2.9 and −3.1 kg without a supplied interim-specific priority rule.
- **F-XS-005:** Route B qualifies because positive prospective and reported imputation specifications differ in method, count, target missingness and predictors for the named interim results, with the risk-specific supplement description retained without assuming it is the same nutritional analysis.
- **F-XS-006:** Route A, category 5 qualifies because additional covariate-adjusted and household-member-exclusion analyses are positively prespecified for the trial's primary-weight framework but no such separate analysis is reported alongside the supplied Y1 weight result.
- **F-XS-007:** Route B qualifies because the SAP explicitly includes Y1 waist and ancillary Bonferroni confidence intervals while the report explicitly adopts unadjusted exploratory inference and supplies no ancillary waist interval, affecting the interval specification available for that named result.
- **F-XS-008:** The graph's word “overall” is not defined as pooled across arms rather than cumulative over the six-year horizon, so treating it as a second population-specific numeric power input depends on a terminology interpretation rather than a reproduced conflicting number.
- **F-ST1-001:** Route A, category 1 qualifies because the main alcohol 6- and 12-month 95% intervals include zero while their adjacent two-sided P=.01 values indicate significance, and neither the printed zero upper limit nor a different inferential construction removes this category.
- **F-ST1-002:** Route A, category 5 qualifies for the same outcome-status change as F-XS-002, preserving all cited dietary, weight and intermediate-marker locations in one issue.
- **F-ST1-003:** Route B qualifies for the same prospective-versus-reported analysis-priority issue as F-XS-004 because it leaves extraction of the principal dietary and weight analyses dependent on an unspecified interim exception.
- **F-ST1-004:** Route B qualifies for the same imputation-specification issue as F-XS-005 because SAP chained equations/20 and report MCMC/8 are positively stated procedures whose relationship to the named interim dietary analysis is not supplied.
- **F-ST1-005:** Route B qualifies for the same Y1 waist multiplicity-specification issue as F-XS-007 because the explicit prospective ancillary interval and reported no-adjustment framework differ without a supplied timing exception.
- **F-ST1-201:** Route A, category 1 qualifies for the repeated alcohol interval-versus-P pattern because both sensitivity-analysis 6-month intervals end at printed zero while P=.02 indicates significance, preserving these populations separately within the same issue as F-ST1-001.
- **F-ST1-202:** Route A, category 1 qualifies because the eFigure2 labels for MUFA, MUFA:SFA, fruit, vegetables and sugary dessert sit outside their own colored bars' plotted 95% intervals, with all seven categories retained as one repeated label-to-graphic association issue.

## Consolidated included issue groups

The suggested source order below uses the earliest affected REPORT location, followed by the supplement locations; the coordinator assigns stable C IDs. Groups are distinct by failed rule rather than by checker provenance. All 15 included findings are retained as INCLUDE provenance, with nine issue groups. No included issue is suppressed as a duplicate. Human questions below do not suggest a correction or disposition.

### Group 1 — Outcome hierarchy in the interim report

- **Finding IDs:** F-XS-002, F-ST1-002.
- **Suggested placement:** Main PDF p.1; earliest main source occurrence among these groups.
- **Qualifying route:** Route A, category 5.
- **Proposed domain and relationships:** protocol_report; P_R; all relationships P_R.
- **REPORT locations:** [main p.1 abstract primary outcome](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=1), [p.2 interim exploratory description](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=2), [p.3 Outcomes](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=3), [p.4 Outcomes and exploratory secondary analyses](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4).
- **PLAN locations:** [protocol p.13 objectives](../../../joi190106supp1_prod_1635377898.47058.pdf#page=13), [p.31 weight outcome](../../../joi190106supp1_prod_1635377898.47058.pdf#page=31), [p.38 intermediate markers](../../../joi190106supp1_prod_1635377898.47058.pdf#page=38); [SAP p.5 objectives](../../../joi190106supp2_prod_1635377898.49605.pdf#page=5), [p.9 primary weight/Y1 and secondary waist timeline](../../../joi190106supp2_prod_1635377898.49605.pdf#page=9), [p.10 intermediate dietary/nutrient/BP/lipid timeline](../../../joi190106supp2_prod_1635377898.49605.pdf#page=10).
- **Independent source comparison:** Plans identify CVD and weight as primary; SAP schedules weight at M6/Y1/Y6 and diet/nutrients/BP/lipids as intermediate. Report calls Y1 er-MedDiet primary and weight, dietary scores, food/nutrients and risk factors secondary, with all secondary analyses exploratory. Categorical status comparison requires no display-precision arithmetic. No finding is made about uncompleted long-term CVD results.
- **Affected results:** er-MedDiet difference 2.2 (2.1–2.4), body-weight difference −2.9 kg (−3.2 to −2.6), and status fields for the reported nutrient and risk outcomes.
- **Alternative:** A report-specific exploratory hierarchy can coexist with the parent-trial hierarchy; that alternative is recorded and does not remove a reproduced category-5 status change.
- **Human question:** Which prospective interim hierarchy should be used to code the reported outcomes, and is its relationship to the parent-trial hierarchy specified in an additional plan or amendment?

### Group 2 — Baseline nutritional filtering and the weight analysis set

- **Finding IDs:** F-XS-003.
- **Suggested placement:** Main p.3 Figure1, continuing p.4 analysis-set definition.
- **Qualifying route:** Route B; focus D, unresolved planned membership rule, named analysis-population size and weight effect.
- **Proposed domain and relationships:** protocol_report; P_R; all relationships P_R.
- **PLAN locations:** [protocol p.52 all-analysis ITT](../../../joi190106supp1_prod_1635377898.47058.pdf#page=52), [SAP p.13 full-data and MI ITT populations](../../../joi190106supp2_prod_1635377898.49605.pdf#page=13).
- **REPORT locations:** [main p.3 Figure1](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=3), [p.4 baseline exclusions and principal population](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4), [results p.23 eTable9 weight](../../../joi190106supp3_prod_1635377898.49725.pdf#page=23).
- **Independent source comparison:** Figure1 and p.4 specify 53 absent baseline FFQs and 238 baseline energy outliers, restricting 6874 randomized participants to I3272/C3311=6583; the weight MI display uses those same counts. SAP defines retention of assigned group and full-data/MI approaches, but does not name this baseline nutritional filter for its primary weight analysis. The issue is the prospective membership specification, not a claim that ITT terminology alone prohibits every exclusion, nor an arithmetic conflict between different explicit populations. No numeric display-precision test applies to the membership-rule comparison.
- **Alternative:** A deliberate nutritional-publication cohort or an unsupplied interim exception may govern these results; absence of baseline dietary data can be relevant to dietary outcomes, while the weight-population linkage remains the specific question.
- **Human question:** Was the baseline FFQ/energy restriction prospectively intended for the Y1 primary-weight framework, and what analysis-population definition should accompany its −2.9 kg result?

### Group 3 — Principal and sensitivity analysis ordering

- **Finding IDs:** F-XS-004, F-ST1-003.
- **Suggested placement:** Main p.4 Statistical Analysis.
- **Qualifying route:** Route B; focus D, unresolved priority, named principal weight and diet estimates.
- **Proposed domain and relationships:** protocol_report; P_R; all relationships P_R.
- **PLAN locations:** [SAP p.13 population alternatives](../../../joi190106supp2_prod_1635377898.49605.pdf#page=13), [p.26 lines777–779](../../../joi190106supp2_prod_1635377898.49605.pdf#page=26).
- **REPORT locations:** [main p.4 principal/post-hoc methods](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4), [p.5 Table2 MI header](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5); [results p.9 completer sensitivity title](../../../joi190106supp3_prod_1635377898.49725.pdf#page=9), [p.23 eTable9 MI/completer weight columns](../../../joi190106supp3_prod_1635377898.49725.pdf#page=23).
- **Independent source comparison:** SAP explicitly prioritizes completers as main and MI as sensitivity; report explicitly prioritizes MI as principal and completers as post hoc sensitivity. General availability of both approaches on SAP p.13 does not remove p.26 ordering. Weight MI −2.9 (−3.2 to −2.6) and completer −3.1 (−3.4 to −2.7) are distinct analyses, not mismatched copies. Categorical priority requires no rounding calculation.
- **Alternative:** The report may use a separate interim priority while preserving future trial priorities, but a supplied interim exception is not identified.
- **Human question:** Which prospective priority applies to this interim dietary and Y1 weight report, and how should the principal estimate be selected for extraction?

### Group 4 — Imputation specification

- **Finding IDs:** F-XS-005, F-ST1-004.
- **Suggested placement:** Main p.4 imputation paragraph.
- **Qualifying route:** Route B; focus C/D, positive differing specifications, named dietary and weight MI results.
- **Proposed domain and primary relationship:** protocol_report; P_R.
- **All relationships independently supported for the consolidated issue:** P_R.
- **PLAN location:** [SAP p.26 lines788–794](../../../joi190106supp2_prod_1635377898.49605.pdf#page=26).
- **REPORT locations:** [main p.4 imputation paragraph](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4), [results p.24 risk-factor MI footnote](../../../joi190106supp3_prod_1635377898.49725.pdf#page=24).
- **Independent source comparison:** SAP specifies chained equations, 20 imputations, missing outcomes after losses of at least two years, and a 13-category predictor list including weight, disease history and second household member. Main specifies MCMC, 8 imputations, follow-up missingness, and sex/age/smoking/education/BMI/PA/group/energy/baseline outcome predictors. The 20 and 8 printed-count intervals [19.5,20.5] and [7.5,8.5] have gap 11 and relative gap 11/20=.55; categorical method/predictor differences do not depend on rounding. The risk-factor footnote specifies chained equations and the report's nine predictor categories, without a count.
- **Classification refinement and ambiguity:** F-XS-005 proposed additional S_C for main-versus-risk method descriptions, but the main paragraph is situated in nutritional analysis and eTable9 applies to risk factors; different outcome-specific engines do not independently reproduce a same-analysis conflict, so that proposed relationship is preserved here as a considered interpretation rather than automatically added to All relationships. The positive prospective-versus-reported specification differences support P_R, including the plan-versus-risk-footnote predictor comparison. The exact intended scope of SAP ≥2-year-loss wording is also an alternative, not presumed to cover every partial Y1 missing measure.
- **Affected results:** er-MedDiet 2.2 (2.1–2.4), reported MI dietary/nutrient effects, and weight −2.9 (−3.2 to −2.6).
- **Human question:** Which prospective imputation rule applies to each interim outcome, and what interim-specific specification links the reported engines, counts, missingness and predictors to the supplied SAP?

### Group 5 — Additional planned primary-weight analyses not reported

- **Finding IDs:** F-XS-006.
- **Suggested placement:** Main p.4 analysis listing, then main p.8 weight/risk reporting and results p.23.
- **Qualifying route:** Route A, category 5.
- **Proposed domain and relationships:** protocol_report; P_R; all relationships P_R.
- **PLAN locations:** [protocol p.52 lines1661–1664 household exclusion](../../../joi190106supp1_prod_1635377898.47058.pdf#page=52), [SAP p.5 primary weight](../../../joi190106supp2_prod_1635377898.49605.pdf#page=5), [p.9 Y1 weight timing](../../../joi190106supp2_prod_1635377898.49605.pdf#page=9), [p.25 lines764–765 covariates](../../../joi190106supp2_prod_1635377898.49605.pdf#page=25), [p.26 lines766–767 continuation](../../../joi190106supp2_prod_1635377898.49605.pdf#page=26).
- **REPORT locations:** [main p.4 listed principal/sensitivity analyses](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4), [p.8 risk reporting](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=8), [results p.23 weight estimates](../../../joi190106supp3_prod_1635377898.49725.pdf#page=23), [p.24 model/imputation footnotes](../../../joi190106supp3_prod_1635377898.49725.pdf#page=24).
- **Independent source comparison:** SAP positively specifies additional weight-model adjustment for recruitment center, sex, age, education, smoking, baseline hypertension/dyslipidemia/diabetes/family CHD/PA; protocol positively specifies sensitivity excluding second household members. The report supplies MI/completer weight estimates and site/couple random-factor descriptions without a separate additional covariate-adjusted or household-excluded result. Direct whole-report/whole-supplement term searches corroborated the complete current maps: adjustment references otherwise concern historical score validation, imputation predictors or the no-multiplicity-adjustment statement; reported sensitivities are completers and baseline replacement. Covariates used to impute a value do not demonstrate a separate outcome-model analysis, and a household random factor does not demonstrate exclusion of the second member. Presence/absence comparison has no numeric precision calculation.
- **Alternative:** These parent-trial analyses may be reserved for another publication; the report recasts weight as interim secondary. That explanation does not remove a reproduced category-5 planned-primary-analysis absence and no unprinted numerical result is inferred.
- **Human question:** Where are the planned additional adjusted and second-household-member-excluded Y1 primary-weight analyses, or what interim reporting specification explains their deferral?

### Group 6 — Ancillary multiplicity intervals for Y1 waist

- **Finding IDs:** F-XS-007, F-ST1-005.
- **Suggested placement:** Main p.4 no-adjustment statement.
- **Qualifying route:** Route B; focus D, expressly differing planned/reported rule, named Y1 waist interval.
- **Proposed domain and relationships:** protocol_report; P_R; all relationships P_R.
- **PLAN locations:** [SAP p.9 Y1 secondary waist](../../../joi190106supp2_prod_1635377898.49605.pdf#page=9), [p.12 lines282–291 and 27-comparison footnote](../../../joi190106supp2_prod_1635377898.49605.pdf#page=12).
- **REPORT locations:** [main p.4 exploratory/no additional adjustment](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4), [p.8 waist result](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=8), [results p.23 eTable9 waist](../../../joi190106supp3_prod_1635377898.49725.pdf#page=23).
- **Independent source comparison:** SAP requires nominal and ancillary Bonferroni intervals for 27 named secondary comparisons, explicitly including waist; Y1 is a scheduled waist time. Report expressly makes all secondary analyses exploratory without additional adjustment, and gives only nominal 95% MI waist −3.3 (−3.6 to −2.9) and completer −3.3 (−3.7 to −3.0). Planned ancillary confidence level is 1−.05/27=.998148148 (99.8148148%). This concerns the specified interval form, not a fabricated adjusted interval or a claim that significance would change. No rounding calculation applies to the categorical rule comparison.
- **Alternative:** Ancillary adjustment may belong to a future comprehensive report; the supplied package does not identify that exception for the directly reported Y1 waist outcome.
- **Human question:** Does the prospective ancillary Bonferroni rule apply to this Y1 waist report, and is the interval or an interim-specific timing exception supplied?

### Group 7 — Repeated alcohol interval-versus-P conflict

- **Finding IDs:** F-ST1-001, F-ST1-201.
- **Suggested placement:** Main p.7 Table3, retaining supplement pp.15 and22 as occurrences of the same pattern.
- **Qualifying route:** Route A, category 1.
- **Proposed domain and primary relationship:** statistical_results; S_W.
- **All relationships:** S_W; the issue is each display's internal interval/test conflict rather than a claim that different analysis populations should yield matching effects.
- **REPORT locations:** [main p.7 Table3 alcohol M6/M12](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=7), [main p.4 two-sided/P<.05 test rule](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4), [main p.8 Table3 footnote](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=8), [results p.15 eTable5 alcohol M6](../../../joi190106supp3_prod_1635377898.49725.pdf#page=15), [results p.22 eTable8 alcohol M6](../../../joi190106supp3_prod_1635377898.49725.pdf#page=22).
- **Independent source comparison:** Main M6 −0.2 (95% CI −0.4 to 0), P=.01; main M12 −0.2 (−0.4 to 0.1), P=.01; completer M6 −0.2 (−0.4 to 0), P=.02; baseline-replacement M6 −0.2 (−0.3 to 0), P=.02. All printed intervals contain null zero and all adjacent P values are below .05. Preserve main/replacement I3272/C3311 and M6 completer I2862/C2883; no equivalence of those populations is assumed.
- **Precision and alternatives:** Category1 never uses a rounding exemption: printed 0 upper endpoints remain part of the issue, including if underlying negative limits rounded to 0. Different CI and P procedures or pooling rules remain alternatives even if later supplied. No replacement P, test statistic, degrees of freedom or CI is inferred.
- **Human question:** What unrounded intervals and test/pooling constructions produced each of the four alcohol contrasts, and how should the printed CI and P classifications be reconciled for extraction?

### Group 8 — Red-wine median and upper quartile

- **Finding IDs:** F-NUM-101.
- **Suggested placement:** Results p.7 eTable2.
- **Qualifying route:** Route B; focus A/B, unresolved within-display numerical ordering, named extracted baseline statistic.
- **Proposed domain and relationships:** statistical_results; S_W; all relationships S_W.
- **REPORT location:** [results p.7 eTable2 Red wine, intervention baseline median(IQR)](../../../joi190106supp3_prod_1635377898.49725.pdf#page=7).
- **Independent source comparison:** Text and source render both show 33 (0,29) g/week, explicitly median(IQR). Median must not exceed Q3 for the same distribution. Median [32.5,33.5] and Q3 [28.5,29.5] leave minimum gap3; relative gap3/33=.09091>.05. The recomputed compatible median interval permitted by displayed Q1/Q3 is at most [−.5,29.5], or [0,29.5] if restricted to nonnegative intake. Baseline copies in other tables are peripheral comparators and not used to choose a replacement.
- **Alternative:** A substituted median/quartile or a mixture of descriptive computations could explain the printed triple, but neither intended value is identified in the display.
- **Human question:** Which median and quartiles correspond to intervention baseline red-wine intake, and what does the printed 33 (0,29) represent?

### Group 9 — eFigure2 in-bar labels versus bars and confidence intervals

- **Finding IDs:** F-NUM-102, F-ST1-202.
- **Suggested placement:** Results p.26 eFigure2.
- **Qualifying route:** Route A, category 1; the repeated direction/magnitude conflict also meets Route B, and changed printed directional readings fit category2.
- **Proposed domain and relationships:** statistical_results; S_W; all relationships S_W.
- **REPORT location:** [results p.26 all seven eFigure2 pairs, labels, bars, intervals, axis, legend and caption](../../../joi190106supp3_prod_1635377898.49725.pdf#page=26).
- **Independent source observation:** Legend assigns purple Intervention and gray Control; vertical axis identifies percentages with95% CI and title identifies12months. Labels I/C are fat34/32, MUFA72/77, MUFA:SFA79/86, fruit58/63, vegetables56/64, meat60/62, sugary dessert59/58. The first six pairs' heights reverse the printed label ordering: approximate I/C tops are32/34,77/72,86/79,63/58,64/56,62/60. Dessert purple is approximately68 and gray60, so a global arm swap cannot reconcile all pairs. MUFA, MUFA:SFA, fruit, vegetables and dessert intervention labels are visibly outside their own plotted intervals; the respective control MUFA/MUFA:SFA/fruit/vegetable labels likewise lie outside their intervals. Fat and meat are retained as repeated association-pattern locations rather than independent precision-qualified findings.
- **Numeric precision corroboration:** Conservative top intervals I/C MUFA:SFA[85,87]/[78,80] versus label intervals[78.5,79.5]/[85.5,86.5] give gaps5.5 and relative gaps.06962/.06395; fruit[62,64]/[57,59] versus[57.5,58.5]/[62.5,63.5] give gaps3.5 and.06034/.05556; vegetables[63,65]/[55,57] versus[55.5,56.5]/[63.5,64.5] give gaps6.5 and.11607/.10156; dessert intervention deliberately broad plotted-region[65,71] versus[58.5,59.5] gives gap5.5 and.09322. These intervals allow visual uncertainty and do not assert unprinted exact plotted values. Direct point-versus-own95%CI containment is category1 and not subject to a rounding exemption.
- **Preserved printed P values:** Fat .14; MUFA, MUFA:SFA, fruit, vegetables and dessert <.001; meat .08. No exact P reconstruction is attempted without denominators/test details, and arm-specific intervals are distinguished from between-arm contrast intervals.
- **Alternative:** A label/bar mapping, population or legend association could differ, but only one arm legend/time point is supplied; neither a single global swap nor swapping first-six labels explains dessert. Exact numerical CI endpoints and arm denominators remain unavailable.
- **Human question:** Which arm-specific percentages and95% limits belong to each of the seven12-month categories, and what mapping reconciles the printed labels, bar heights and legend, including dessert?

## Source reread and limitations

Direct Poppler pdftotext26.01.0, CPU, was run to stdout on selected exact PDF pages: DOC-001 pp.1–5,7–8; DOC-002 pp.13,31,38,52–54; DOC-003 pp.5,7,9–13,25–26; DOC-004 pp.7,9,15,22–24,26. For planned-analysis absence, direct whole DOC-001 and DOC-004 text streams were searched for adjustment, sensitivity, household, covariates and exclusion terms. No extraction derivative was saved or source/reusable artifact modified.

Visual source confirmation used existing current-run direct Poppler CPU renders preprocessing/stat1-support-b-p26.png (DOC-004p.26), preprocessing/protocol_p054.png (DOC-002p.54), preprocessing/numeric_support/results-p7.png (DOC-004p.7), plus the curated source-linked retained review_1_6_1/preprocessing/sap-results-sap-p7.png (DOC-003p.7; retained engine version unspecified). No old scientific conclusion or candidate artifact was read.

The two completion findings reproduce all printed numbers but not a contradiction between matching completion counts: unavailable nutrition does not establish absent visits, and main p.5 identifies different imputed counts even for different dietary instruments (517 er-MedDiet values versus807 MDS/MEDAS/PDQS atY1). Consequently6066 er-MedDiet records,5776 FFQ-based completer records and6583 MI members are not interchangeable measures of completed attendance. The screen does not certify an attendance count; that detail is unreported in the cited package.

The power-label finding was visually checked in both plans: “10% (overall) in6yr” is printed, but whether “overall” means pooled arms is not supplied; the diagnostic constant-hazard calculation is an assumed reading and does not reproduce an independently stated second input. This is the wording reason for exclusion, without a claim that any sample-size calculation has been reproduced.

Graphical endpoints and denominators are not numerically printed in eFigure2, so its quantities remain visual bounds; the directly observed point/own-interval and directional conflicts do not require exact digitization. No screening coverage gap remains.

Counts:18/18 finding decisions;15 INCLUDE rows consolidated into9 included issues;3 SCREENED_OUT rows, comprising NOT_REPRODUCED2 and TERMINOLOGY_OR_WORDING1. All other exclusion reason-code counts are0. All included issues remain Pending Human Adjudication once registered by the coordinator.

## Fresh pass-2 screening and consolidation

F-ST2-001 was independently included under Route A category5 by fresh high agent root/inclusion_pass2 and extends C005 rather than creating a new stable ID. The positive SAP p.26 lines781-785 subgroup promise, scheduled Y1 primary-weight key and supplied-report absence are preserved with explicit unresolved outcome/time applicability. The complete independent source reread, differing reviewer interpretations, consolidation rationale and exact new locations are in inclusion_screen_pass_2.md.

Final screening totals after pass2: 19 findings, 16 INCLUDE provenance rows consolidated into nine stable candidates, three SCREENED_OUT findings (NOT_REPRODUCED2; TERMINOLOGY_OR_WORDING1). Every other screened-out reason-code count is zero. Initial decisions remain unchanged.
