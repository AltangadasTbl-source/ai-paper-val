# Statistical pass 1

Fresh runtime agent: `/root/statistical_pass_1`; fixed model gpt-6.1-sol, reasoning effort high. Full assigned scope personally reviewed: 195 stable S relationships, comprising 40 main-article, 37 support/opening-plan and 118 further-plan records. Bounded assessment records are in `parts/statistical-pass-1-report.md` and `parts/statistical-pass-1-plan.md`; every ID receives PASS_1_COMPLETE. Sources and reusable assets were preserved. No earlier scientific conclusions or external literature were used.

All displayed effect intervals were checked for point containment, endpoint order and direction. All outcome-level clinical P values agree with printed CI null inclusion: no reproduced interval-versus-P significance conflict was found. Subgroup interaction tests were kept distinct from row treatment effects. Exact unrounded P/estimate compatibility was not inferred where the source gives no matching statistic, variance, covariance, or complete estimation procedure. Marginal/bootstrap/model results were not replaced by crude ratios or assumed Wald calculations.

Four findings meet the checker inclusion threshold. Independent screening and human adjudication remain downstream. No candidate IDs or dispositions are assigned here.

## Findings

### F-ST1-001

**Issue:** Missing hospital-stay durations are described as censored at 1 hour in the main table and 1 day in the results supplement.

**Exact locations and roles:** REPORT main article [PDF p8, Table2 footnote b](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=8); REPORT results supplement [PDF p24, eTable7 hospital-stay row and footnote e](../../../joi250042supp2_prod_1753377747.93025.pdf#page=24). Both complete source-linked images were personally read. Relationships S006, S015, S1006, S1025 and related duration records.

**Printed inputs:** Main footnote: missing time to discharge for duration of ICU and acute hospital stay is included as censored 1 hour after randomization. Supplement: missing ICU stay censored at 1 hour, missing acute hospital stay at 1 day. Supplement identifies 1677 (10.2%) missing hospital durations. Reported adjusted hospital sHR is0.98 (95%CI0.94–1.02), P=.27, in both available-case and multiply-imputed columns.

**Rule and calculation:** The two statements describe the same missing hospital outcome and cannot specify the same censoring time. One day is24 hours, rather than1 hour. Even treating printed1 as rounded, the main interval is[0.5,1.5] hours and the supplemental interval[12,36] hours; their gap is10.5 hours and gap/reference1hour=10.5>0.05. As procedural definitions, the stated cutoffs are exact; the rounding calculation is conservative.

**Focus area:** C. **Proposed review domain:** statistical_results. **Proposed relationship:** S_C; all relationships S_C.

**Qualifying route:** Route B.

**Affected result or extracted value:** The missing-data censoring rule attached to the reported acute-hospital-stay sHR0.98 and its95%CI, affecting which analysis specification is extracted.

**Why context does not resolve it:** Both locations explicitly include hospital stay, and the supplement distinguishes its day-scale cutoff from the ICU hour-scale cutoff. The displayed sHR does not identify which cutoff was implemented.

**Alternatives and missing definition:** The main footnote may summarize only the ICU cutoff, while the supplement may supply the intended hospital cutoff; alternatively the main footnote may describe the implemented rule. The actual hospital censoring time is not identified by the effect estimate. No resulting change in sHR is asserted.

**Exact human question:** Were missing acute-hospital-stay durations censored at1 hour or1 day after randomization in the analysis producing Table2?

### F-ST1-002

**Issue:** The protocol-prespecified stratification-only companion analysis of the primary outcome is not reported in the supplied clinical results.

**Exact locations and roles:** PLAN original protocol [PDF p30, §4.2.2 primary analysis](../../../joi250042supp1_prod_1753377747.92525.pdf#page=30), repeated in PLAN final protocol [PDF p70, §4.2.2](../../../joi250042supp1_prod_1753377747.92525.pdf#page=70). REPORT main [PDF p3 statistical analysis](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=3), [PDF p6 primary outcome paragraph](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=6), [PDF p8 Table2 and footnotes](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=8). All supplied REPORT pages were covered, including supplement pp1–29. Final protocol p70 and main Table2 were personally confirmed on complete source-linked images. Relationships S001, S010–S012, S2004, S3011.

**Printed inputs:** The final protocol states the primary90-day mortality analysis will be performed both adjusted only for site/diagnostic stratification variables and adjusted for additional baseline covariates. The fully adjusted analysis is designated primary. Main methods specify site, diagnostic subgroup, age, SpO2, PaO2:FiO2, COVID and randomization date. Main Table2 supplies fully adjusted available-case and multiply-imputed effects: RD0.7 (−0.6,2.1) and0.7 (−0.7,2.0), RR1.02 and OR1.04. Main p6 also reports an unadjusted RD0.5 (−1.0,2.0). No stratification-only treatment effect is reported in either supplied REPORT document.

**Rule and reproduced comparison:** A model containing site/diagnostic strata alone is distinct from the fully adjusted model and from an unadjusted contrast. The available-case versus imputed columns vary missingness handling, rather than remove the added baseline covariates: footnotes specify the same adjustment. Complete REPORT coverage found neither a strata-only estimate nor a statement that its planned analysis was replaced. No numeric recomputation or display-rounding rule applies to an omitted analysis specification.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; all relationships P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The planned companion analysis for90-day mortality, needed to distinguish a strata-only effect from the reported fully adjusted and crude estimates.

**Why context does not resolve it:** This is a planned analysis of the primary outcome that is not reported, an always-register category. The crude RD cannot be identified as the site/diagnosis-only model.

**Alternatives and missing definition:** The later SAP [PDF pp126–127](../../../joi250042supp1_prod_1753377747.92525.pdf#page=126) details the fully adjusted model and may have been intended to replace the protocol companion analysis. It does not explicitly report the strata-only result or identify its removal. A separately available result outside the supplied package cannot be assumed.

**Exact human question:** Was the protocol-prespecified site/diagnostic-strata-only primary-outcome analysis performed, and where is its treatment effect reported or its replacement documented?

### F-ST1-003

**Issue:** The final SAP specifies all outcome variables in each outcome-imputation model; the results describe selected auxiliary outcomes, no auxiliary outcome for1-year mortality, and early censoring for missing stays.

**Exact locations and roles:** PLAN final SAP [PDF pp131–132, §7](../../../joi250042supp1_prod_1753377747.92525.pdf#page=132); REPORT main [PDF p3 imputation paragraph](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=3), [PDF p8 Table2 footnote b](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=8); REPORT results supplement [PDF p24, all outcome rows and footnotes of eTable7](../../../joi250042supp2_prod_1753377747.93025.pdf#page=24). SAP p132 and eTable7 were personally confirmed on complete source-linked images. Relationships S006, S1023, S1025, S5041–S5043.

**Printed inputs:** Final SAP: secondary outcomes expected missing after refusal/withdrawal; MICE with each imputation model including all adjusted baseline variables and all outcome variables; multiply-imputed primary analysis with complete-case results alongside, twenty datasets and Rubin combination. Reported eTable7 auxiliaries:90-day mortality uses acute-hospital duration; organ-support-free days use90-day and ICU-discharge mortality; ICU death uses90-day mortality; hospital death uses90-day mortality and hospital duration;60-day mortality uses90-day and1-year mortality;1-year mortality uses None. All adjusted baseline predictors are separately included by footnote a. ICU/hospital missing stays (1653/1677) use censoring rather than MICE, with N/A auxiliaries. Table2 explicitly excepts stay durations from outcome imputation. One-year mortality has1661/13052 missing (12.7%), and its imputed RD is3.3 (−0.7,7.3), versus available-case1.0 (−0.7,2.6).

**Rule and reproduced comparison:** The listed predictor sets are not all-outcome sets: for example the1-year model's None cannot designate inclusion of90-day mortality as an auxiliary outcome. The baseline predictor footnote does not supply the omitted outcomes. Missing-duration censoring is also different from the final paragraph's general MICE strategy for expected secondary missingness. This is a reproduced difference in a specified primary/secondary missing-data procedure, rather than an inference from unreported package settings. No rounding calculation applies to predictor membership or imputation versus censoring.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; all relationships P_R. These locations are one consolidated missing-data specification pattern, with all affected outcome rows retained.

**Qualifying route:** Route B.

**Affected result or extracted value:** The imputation specification for the primary90-day mortality and secondary mortality/organ-support estimates, including the one-year imputed RD3.3 and the censoring strategy for stay sHRs.

**Why context does not resolve it:** Both plan and report explicitly specify predictor inclusion and missing-outcome handling. The report does not identify how the all-outcome model specification maps to its selected auxiliary lists or duration exceptions. This bears directly on the analysis attached to the extracted estimates.

**Alternatives and missing definition:** The SAP may express a general framework that was operationally refined; eTable7 may describe the actual refined models. Alternatively the table may list only selected additional auxiliaries while other outcomes entered through an unprinted process, although its None and footnote a do not state that. The SAP permits computational alternatives but neither removes all-outcome predictors nor specifies early stay censoring. Its printed fallback is five datasets and1000 bootstraps, not the earlier derivative transcription100. No effect of this model difference on reported estimates is asserted.

**Exact human question:** Which outcomes entered each implemented imputation model, and how were selected/None auxiliary lists and early duration censoring reconciled with final SAP §7's all-outcome MICE specification?

### F-ST1-004

**Issue:** The final protocol specifies Wilcoxon stay tests stratified by survival; the final SAP and reported effects specify Fine-Gray competing-risk regression.

**Exact locations and roles:** PLAN original protocol [PDF p30, §4.2.2](../../../joi250042supp1_prod_1753377747.92525.pdf#page=30); PLAN final protocol [PDF pp70–71, §4.2.2](../../../joi250042supp1_prod_1753377747.92525.pdf#page=70); PLAN SAP v1.0 [PDF p104, §5.3.2](../../../joi250042supp1_prod_1753377747.92525.pdf#page=104) and final SAP [PDF p128, §5.3.4](../../../joi250042supp1_prod_1753377747.92525.pdf#page=128); REPORT main [PDF p3 statistical analysis](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=3) and [PDF p8 Table2](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=8). Final protocol pp70–71 and main Table2 were personally confirmed on complete source-linked images. Relationships S005, S014–S015, S2006, S3014, S4022 and S5027.

**Printed inputs:** Final protocol: analyses of duration of critical-care and acute-hospital stay will be performed by Wilcoxon rank-sum tests stratified by survival status. SAP: stay among survivors analyzed using proportional-hazards regression with Fine-Gray competing death. Report identifies Fine-Gray subdistribution hazards regression, with adjusted ICU sHR1.00 (0.96,1.04), P=.97, and acute-hospital sHR0.98 (0.94,1.02), P=.27. No Wilcoxon test result is supplied.

**Rule and reproduced comparison:** A Wilcoxon comparison of stay distributions within survival strata is not the stated adjusted Fine-Gray competing-risk analysis and does not yield a subdistribution hazard ratio. The final protocol therefore specifies a different method from the final SAP and current report. This is an explicit planned-versus-reported method difference, affecting the interpretation of the reported duration comparison, without proposing a preferred method. No arithmetic/display-precision calculation applies to these method specifications.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R; all relationships P_R, P_P. The protocol/SAP conflict is independently within PLAN; the final report implements the SAP side. Precedence assigns P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** Which planned analysis produced the ICU and hospital-stay comparison and its P value, and whether the extracted effects should be understood as Fine-Gray sHRs rather than survival-stratified rank-sum contrasts.

**Why context does not resolve it:** The final protocol retains an explicit Wilcoxon analysis statement. The supplied plan gives a distinct Fine-Gray specification and the report gives its hazard-ratio results without a reconciliation or companion Wilcoxon result. Both procedural statements can be extracted as the prespecified analysis.

**Alternatives and missing definition:** The SAP may have intentionally replaced the protocol analysis; its detail and the report's explicit statement establish what was reported. Alternatively both analyses may have been planned, with only Fine-Gray reported. The remaining question is the documented relationship between specifications, not whether Fine-Gray is an appropriate preferred analysis. No significance conflict between the two unpaired tests is inferred.

**Exact human question:** Did the SAP replace the protocol-prespecified Wilcoxon stay analyses, or were both retained; where is that relationship documented and any retained Wilcoxon result reported?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| Main p6/Table2; Figure3; supplementary eFigure7 | Adjusted mortality/subgroup RD/OR differs from crude contrasts computed from displayed counts; multilevel adjustment and marginal standardization are explicitly stated. | MODEL_VERSUS_CRUDE |
| Main p8 Table2,1-year mortality; final SAP pp126–127/132 | An assumed symmetric Wald reconstruction from RD3.3 and CI−0.7–7.3 gives a different diagnostic P from.34. It is not the supplied bootstrap/marginal/MI test, and exact paired variance/test definitions are absent. There is no null-inclusion/significance conflict. | CONDITIONAL_OR_UNREPORTED |
| Main Figure3; supplement eFigure7 | Pairing an omnibus interaction P with one row's treatment-effect CI creates an apparent conflict between distinct hypotheses. Matching the source attribution does not reproduce a conflict. | NOT_REPRODUCED |
| Main p3; supplement eFigure5 p12 | Cox estimation details for342 unknown exact death times are not printed; interval/left censoring is explicitly described in the caption. No internally contradictory Cox procedure or numeric result is established merely by assuming conventional partial likelihood. | CONDITIONAL_OR_UNREPORTED |
| PLAN pp98/121; main analysis description | Re-enrollment after≥90 days is permitted, but actual repeat contributions and a contradictory variance claim are not supplied. An assumed patient-dependence omission is conditional. | CONDITIONAL_OR_UNREPORTED |
| Original protocol pp20/39 versus final protocol pp61/81/87 and main p3 | Original90–93% oxygen target and89/94% alarms differ from final90±2%/88/92%; the amendment is explicitly disclosed before recruitment and final report matches it. | CONTEXT_RESOLVES |
| Original SAP p107 versus final SAP pp131–132/136 | Original extreme-case primary missingness sensitivity is absent from final specification; final SAP explicitly replaces/expands missing-data handling and report follows final MI strategy. No still-current promised sensitivity is established. | CONTEXT_RESOLVES |
| Final SAP p132; main p6 and supplement eTable9 p26 | A Fisher test is planned for any SAE but no P is reported. This non-key safety-only omission supplies no printed inferential contradiction or primary/key secondary replacement. | CONDITIONAL_OR_UNREPORTED |

## Coverage and named limits

195/195 relationships personally assessed;77 report/opening-plan records and118 further-plan records, all PASS_1_COMPLETE in the two bounded parts. Those parts are the complete explicit per-ID records, not a sampling limit. Relevant count/denominator implications include analysis flow16434 versus observed16394, retained40 missing primary outcomes, secondary consent populations, one-year eligible13052 versus complete11391, duration survival-subset totals, ordinal death-score reconstruction, and unique SAE patients versus overlapping event categories.

Power diagnostic: standard independent two-proportion normal approximation using risks.37/.345, two-sided alpha.05, power.90 gives15442.18 total before loss and16427.85 after division by.94; planned15444 and conservative rounded recruitment16500 reconcile under display precision. The source does not print an exact sample-size formula/continuity correction. This approximation is diagnostic and no contrary sample-size finding is emitted.

No printed standard errors or test statistics permit exact recovery of all unrounded tests. Bootstrap resampling implementation, full MI computation details, exact unknown-time survival estimation and unprinted graphical coordinates remain named reproducibility limits; they were not assumed. Direct source images resolved table signs/decimal points, the p132 fallback1000 transcription, and specific qualifying source statements. No scientific relationship coverage gap remains.

Totals:195 relationships;4 findings;8 excluded observations. No candidate/disposition count is assigned by this checker.

## Canonical completion registry

The coordinator merged this explicit registry mechanically from the complete 77-row and 118-row pass-1 assessment parts after initial validation. Each ID below already had a source-linked PASS_1_COMPLETE assessment; this registry adds no review inference, candidate or repeated scientific work. It spells out every ID for canonical-file validation.

| S ID | Pass 1 status |
|---|---|
| S001 | PASS_1_COMPLETE |
| S002 | PASS_1_COMPLETE |
| S003 | PASS_1_COMPLETE |
| S004 | PASS_1_COMPLETE |
| S005 | PASS_1_COMPLETE |
| S006 | PASS_1_COMPLETE |
| S007 | PASS_1_COMPLETE |
| S008 | PASS_1_COMPLETE |
| S009 | PASS_1_COMPLETE |
| S010 | PASS_1_COMPLETE |
| S011 | PASS_1_COMPLETE |
| S012 | PASS_1_COMPLETE |
| S013 | PASS_1_COMPLETE |
| S014 | PASS_1_COMPLETE |
| S015 | PASS_1_COMPLETE |
| S016 | PASS_1_COMPLETE |
| S017 | PASS_1_COMPLETE |
| S018 | PASS_1_COMPLETE |
| S019 | PASS_1_COMPLETE |
| S020 | PASS_1_COMPLETE |
| S021 | PASS_1_COMPLETE |
| S022 | PASS_1_COMPLETE |
| S023 | PASS_1_COMPLETE |
| S024 | PASS_1_COMPLETE |
| S025 | PASS_1_COMPLETE |
| S026 | PASS_1_COMPLETE |
| S027 | PASS_1_COMPLETE |
| S028 | PASS_1_COMPLETE |
| S029 | PASS_1_COMPLETE |
| S030 | PASS_1_COMPLETE |
| S031 | PASS_1_COMPLETE |
| S032 | PASS_1_COMPLETE |
| S033 | PASS_1_COMPLETE |
| S034 | PASS_1_COMPLETE |
| S035 | PASS_1_COMPLETE |
| S036 | PASS_1_COMPLETE |
| S037 | PASS_1_COMPLETE |
| S038 | PASS_1_COMPLETE |
| S039 | PASS_1_COMPLETE |
| S040 | PASS_1_COMPLETE |
| S1001 | PASS_1_COMPLETE |
| S1002 | PASS_1_COMPLETE |
| S1003 | PASS_1_COMPLETE |
| S1004 | PASS_1_COMPLETE |
| S1005 | PASS_1_COMPLETE |
| S1006 | PASS_1_COMPLETE |
| S1007 | PASS_1_COMPLETE |
| S1008 | PASS_1_COMPLETE |
| S1009 | PASS_1_COMPLETE |
| S1010 | PASS_1_COMPLETE |
| S1011 | PASS_1_COMPLETE |
| S1012 | PASS_1_COMPLETE |
| S1013 | PASS_1_COMPLETE |
| S1014 | PASS_1_COMPLETE |
| S1015 | PASS_1_COMPLETE |
| S1016 | PASS_1_COMPLETE |
| S1017 | PASS_1_COMPLETE |
| S1018 | PASS_1_COMPLETE |
| S1019 | PASS_1_COMPLETE |
| S1020 | PASS_1_COMPLETE |
| S1021 | PASS_1_COMPLETE |
| S1022 | PASS_1_COMPLETE |
| S1023 | PASS_1_COMPLETE |
| S1024 | PASS_1_COMPLETE |
| S1025 | PASS_1_COMPLETE |
| S1026 | PASS_1_COMPLETE |
| S1027 | PASS_1_COMPLETE |
| S1028 | PASS_1_COMPLETE |
| S1029 | PASS_1_COMPLETE |
| S1030 | PASS_1_COMPLETE |
| S1031 | PASS_1_COMPLETE |
| S1032 | PASS_1_COMPLETE |
| S1033 | PASS_1_COMPLETE |
| S1034 | PASS_1_COMPLETE |
| S1035 | PASS_1_COMPLETE |
| S1036 | PASS_1_COMPLETE |
| S1037 | PASS_1_COMPLETE |
| S2001 | PASS_1_COMPLETE |
| S2002 | PASS_1_COMPLETE |
| S2003 | PASS_1_COMPLETE |
| S2004 | PASS_1_COMPLETE |
| S2005 | PASS_1_COMPLETE |
| S2006 | PASS_1_COMPLETE |
| S2007 | PASS_1_COMPLETE |
| S2008 | PASS_1_COMPLETE |
| S2009 | PASS_1_COMPLETE |
| S2010 | PASS_1_COMPLETE |
| S2011 | PASS_1_COMPLETE |
| S2012 | PASS_1_COMPLETE |
| S2013 | PASS_1_COMPLETE |
| S2014 | PASS_1_COMPLETE |
| S2015 | PASS_1_COMPLETE |
| S2016 | PASS_1_COMPLETE |
| S2017 | PASS_1_COMPLETE |
| S3001 | PASS_1_COMPLETE |
| S3002 | PASS_1_COMPLETE |
| S3003 | PASS_1_COMPLETE |
| S3004 | PASS_1_COMPLETE |
| S3005 | PASS_1_COMPLETE |
| S3006 | PASS_1_COMPLETE |
| S3007 | PASS_1_COMPLETE |
| S3008 | PASS_1_COMPLETE |
| S3009 | PASS_1_COMPLETE |
| S3010 | PASS_1_COMPLETE |
| S3011 | PASS_1_COMPLETE |
| S3012 | PASS_1_COMPLETE |
| S3013 | PASS_1_COMPLETE |
| S3014 | PASS_1_COMPLETE |
| S3015 | PASS_1_COMPLETE |
| S3016 | PASS_1_COMPLETE |
| S3017 | PASS_1_COMPLETE |
| S3018 | PASS_1_COMPLETE |
| S3019 | PASS_1_COMPLETE |
| S3020 | PASS_1_COMPLETE |
| S3021 | PASS_1_COMPLETE |
| S3022 | PASS_1_COMPLETE |
| S3023 | PASS_1_COMPLETE |
| S4001 | PASS_1_COMPLETE |
| S4002 | PASS_1_COMPLETE |
| S4003 | PASS_1_COMPLETE |
| S4004 | PASS_1_COMPLETE |
| S4005 | PASS_1_COMPLETE |
| S4006 | PASS_1_COMPLETE |
| S4007 | PASS_1_COMPLETE |
| S4008 | PASS_1_COMPLETE |
| S4009 | PASS_1_COMPLETE |
| S4010 | PASS_1_COMPLETE |
| S4011 | PASS_1_COMPLETE |
| S4012 | PASS_1_COMPLETE |
| S4013 | PASS_1_COMPLETE |
| S4014 | PASS_1_COMPLETE |
| S4015 | PASS_1_COMPLETE |
| S4016 | PASS_1_COMPLETE |
| S4017 | PASS_1_COMPLETE |
| S4018 | PASS_1_COMPLETE |
| S4019 | PASS_1_COMPLETE |
| S4020 | PASS_1_COMPLETE |
| S4021 | PASS_1_COMPLETE |
| S4022 | PASS_1_COMPLETE |
| S4023 | PASS_1_COMPLETE |
| S4024 | PASS_1_COMPLETE |
| S4025 | PASS_1_COMPLETE |
| S4026 | PASS_1_COMPLETE |
| S4027 | PASS_1_COMPLETE |
| S4028 | PASS_1_COMPLETE |
| S4029 | PASS_1_COMPLETE |
| S4030 | PASS_1_COMPLETE |
| S4031 | PASS_1_COMPLETE |
| S5001 | PASS_1_COMPLETE |
| S5002 | PASS_1_COMPLETE |
| S5003 | PASS_1_COMPLETE |
| S5004 | PASS_1_COMPLETE |
| S5005 | PASS_1_COMPLETE |
| S5006 | PASS_1_COMPLETE |
| S5007 | PASS_1_COMPLETE |
| S5008 | PASS_1_COMPLETE |
| S5009 | PASS_1_COMPLETE |
| S5010 | PASS_1_COMPLETE |
| S5011 | PASS_1_COMPLETE |
| S5012 | PASS_1_COMPLETE |
| S5013 | PASS_1_COMPLETE |
| S5014 | PASS_1_COMPLETE |
| S5015 | PASS_1_COMPLETE |
| S5016 | PASS_1_COMPLETE |
| S5017 | PASS_1_COMPLETE |
| S5018 | PASS_1_COMPLETE |
| S5019 | PASS_1_COMPLETE |
| S5020 | PASS_1_COMPLETE |
| S5021 | PASS_1_COMPLETE |
| S5022 | PASS_1_COMPLETE |
| S5023 | PASS_1_COMPLETE |
| S5024 | PASS_1_COMPLETE |
| S5025 | PASS_1_COMPLETE |
| S5026 | PASS_1_COMPLETE |
| S5027 | PASS_1_COMPLETE |
| S5028 | PASS_1_COMPLETE |
| S5029 | PASS_1_COMPLETE |
| S5030 | PASS_1_COMPLETE |
| S5031 | PASS_1_COMPLETE |
| S5032 | PASS_1_COMPLETE |
| S5033 | PASS_1_COMPLETE |
| S5034 | PASS_1_COMPLETE |
| S5035 | PASS_1_COMPLETE |
| S5036 | PASS_1_COMPLETE |
| S5037 | PASS_1_COMPLETE |
| S5038 | PASS_1_COMPLETE |
| S5039 | PASS_1_COMPLETE |
| S5040 | PASS_1_COMPLETE |
| S5041 | PASS_1_COMPLETE |
| S5042 | PASS_1_COMPLETE |
| S5043 | PASS_1_COMPLETE |
| S5044 | PASS_1_COMPLETE |
| S5045 | PASS_1_COMPLETE |
| S5046 | PASS_1_COMPLETE |
| S5047 | PASS_1_COMPLETE |
