# Statistical Consistency Review — Pass 1

## Scope, evidence, and completion

Fresh independent statistical pass-1 review of every canonical inferential relationship, **S001-S052** (52/52). This review used only the current canonical statistical and numeric inventories, current main/support quantitative maps, and targeted direct-PDF confirmation. It did not use prior candidate, checker, verification, quality, or report conclusions.

Checks applied where source definitions permitted: point-estimate containment, interval ordering, direction/sign, effect-measure and scale labels, matched repetitions, count/denominator arithmetic, and test/interval/P-value compatibility. Exact inferential reconstruction was not attempted where sidedness, variance estimator, covariance/correlation structure, CI construction, multiplicity adjustment, denominator, or external-study model was not supplied. Diagnostic calculations below are explicitly approximations and do not replace the reported analyses.

Two uncapped internal sweeps were completed: (1) relationship-by-relationship inferential review; (2) cross-location, denominator/arithmetic, label/scale, and duplicate-value recheck. Every record below is marked `PASS_1_COMPLETE`. This is distinct from the required later independent statistical pass 2.

## Provisional quality-control candidates (no stable C IDs assigned)

### P1-STAT-01 — Stated sample-size attrition arithmetic does not reconcile from the printed inputs

- **Affected relationships:** S003, S012, S022, S029.
- **Direct source evidence:** The final SAP states that 142 patients per group are necessary, then states that, assuming 20% loss to follow-up, 342 total (171 per group) are required ([SAP PDF p. 5](<../../../joi250033supp5_prod_1750956987.78281.pdf#page=5>)). The protocol’s planned-statistics section supplies the same 142-per-group, 20%-loss, and 342-total sequence ([protocol PDF p. 50](<../../../joi250033supp1_prod_1750956987.76581.pdf#page=50>)). The main article reports the related final planning summary (15% versus 5%, 80% power, two-sided 5%, 20% loss, total 342) ([main PDF p. 3](<../../../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=3>)).
- **Direct observation and arithmetic:** 142 per group is 284 participants. If 284 is the stated post-loss target and 20% of recruited participants are expected to be lost, the stated inputs imply 284 / 0.80 = 355 recruits (before any stated rounding), rather than 342. Conversely, 342 × 0.80 = 273.6, below 284.
- **Why it is a candidate:** The printed sample-size statements do not reconcile under the stated attrition rule. This is a planning/reporting arithmetic issue, not a claim about the trial’s realized analysis.
- **Exact human question:** Was 142 per group a pre-attrition target, was the 20% figure applied under an unstated alternative convention, or was a separate sequential-design calculation/rounding rule used? The supplied text does not provide the calculation output or an attrition denominator that would reconcile all three printed values.

### P1-STAT-02 — Final-SAP endpoint threshold differs from the matched main/protocol/result definition

- **Affected relationships:** S026; matched primary-endpoint/model records S001-S002, S014, S034, S042-S043, and S051-S052 were checked as comparator context.
- **Direct source evidence:** The final SAP defines the primary outcome using a midline shift **`> 5mm`** ([SAP PDF p. 3](<../../../joi250033supp5_prod_1750956987.78281.pdf#page=3>)). The main article defines the endpoint as a midline shift **`of 5 mm or greater`** ([main PDF p. 3](<../../../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=3>)); the protocol and results-supplement EMPROTECT summary use **`≥ 5 mm`** ([protocol PDF p. 27](<../../../joi250033supp1_prod_1750956987.76581.pdf#page=27>); [results supplement PDF p. 15](<../../../joi250033supp4_prod_1750956987.77981.pdf#page=15>)).
- **Direct observation:** `>5 mm` excludes a measurement exactly equal to 5 mm; `≥5 mm` includes it. These are distinct printed endpoint definitions.
- **Why it is a candidate:** The threshold/scale label is not matched across supplied prospective/final analysis and reported-result sources. No claim is made about whether any participant had a measured shift exactly equal to 5 mm.
- **Exact human question:** Which threshold governed final endpoint adjudication and the reported imputed primary analysis, and should all source documents use that same expression?

## Relationship-by-relationship pass-1 record

| S ID | Pass-1 checks and direct-source result | Candidate linkage / missing definition | Status |
|---|---|---|---|
| S001 | Main primary logistic analysis, adjustment variables, full-analysis/imputation handling, and omitted random center are internally described; final-model documentation is consistent with final SAP/results support. | Center omission is explicitly attributed to estimated zero random-effect variance; no candidate. | PASS_1_COMPLETE |
| S002 | OR 0.64 and CI 0.36-1.14 are ordered and contain 1; adjusted risk difference -6% and CI -14% to 2% contain 0; both point toward lower recurrence with embolization and agree with P=.13/narrative. A labelled diagnostic Wald approximation from the OR/CI gives two-sided P about .13. | Exact CI/P construction after imputation is not printed; diagnostic only. | PASS_1_COMPLETE |
| S003 | Main planning record is directionally/label-consistent with protocol/SAP sequential plan and 342 enrolled total. | Linked to P1-STAT-01 because the source sequence needs its 142-per-group comparator to test stated attrition arithmetic. `129`/`37.5%` information fraction is not independently challenged: its information denominator is not supplied. | PASS_1_COMPLETE |
| S004 | Both interaction P values (.32 localization; .18 medication) are nonzero, direction-neutral interaction results and match Figure 2 labels. | Interaction test degrees of freedom and covariance are not supplied; no exact reconstruction. | PASS_1_COMPLETE |
| S005 | Local-assessor sensitivity OR .61 (CI .35-1.06) is ordered, contains 1, has direction matching its nonsignificant narrative and P=.08. Diagnostic log-OR/CI approximation gives P about .08. | Exact imputation/model/CI method for the sensitivity is not supplied; diagnostic only. | PASS_1_COMPLETE |
| S006 | Repeat-surgery difference -4.0% (CI -9.4 to 1.4) is ordered, contains 0, and directionally matches 7/162 versus 13/157 and P=.14. Diagnostic uncorrected Pearson 2x2 calculation gives P about .14. | Source names Pearson chi-square; continuity handling is not stated, so approximation is diagnostic only. | PASS_1_COMPLETE |
| S007 | mRS risk differences and CIs are ordered and contain 0 at both time points; directions match printed group rates and P=.22/.79. GEE binary-outcome label and mRS scale are consistent. | Working correlation, variance estimator, and exact contrast/P-value derivation are not supplied; no exact recalculation. | PASS_1_COMPLETE |
| S008 | Mortality differences/CIs contain 0 and match equal 1-month counts/P=1.00 and lower embolization mortality at six months/P=.38. Fisher-exact labels are consistent. | Exact two-sided Fisher convention is not supplied; no reconstruction beyond printed compatibility. | PASS_1_COMPLETE |
| S009 | Hospital-stay median difference 1 day (CI -1 to 5) is ordered, contains 0, and matches P=.12 and Wilcoxon label. | CI method for a median/difference is not supplied; no exact reconstruction. | PASS_1_COMPLETE |
| S010 | Exploratory/no-multiplicity wording, two-sided-test label, and R version are repeated without conflicting inferential claim. | No candidate. | PASS_1_COMPLETE |
| S011 | Table 3 supplies no between-group P value/formal test; the narrative’s non-difference wording cannot be mechanically equated with a missing test statistic. | No test/model/estimand is printed for that narrative comparison; missing definition recorded, not a candidate. | PASS_1_COMPLETE |
| S012 | Protocol planning effect, power, alpha, sequential design, and total match the corresponding plan records. | Linked to P1-STAT-01; no separate candidate. | PASS_1_COMPLETE |
| S013 | Protocol two-stage Lan-DeMets/O'Brien-Fleming labels, 129 interim, .001 interim, and .05 final agree with repeated plan sources. | Information-fraction denominator/alpha-spending calculation is not supplied; no exact numerical audit. | PASS_1_COMPLETE |
| S014 | Prospective mixed-logistic model and strata match the planned model; the final main article explains why center random effect was omitted. | Prospective-to-realized model difference is source-explained, not a contradiction. | PASS_1_COMPLETE |
| S015 | Allocation strata and centralized randomization labels agree with planned adjustment variables. | No candidate. | PASS_1_COMPLETE |
| S016 | Primary/secondary outcome wording distinguishes rates/proportions/duration and does not mislabel a measure in the matched sources. | No candidate. | PASS_1_COMPLETE |
| S017 | Protocol descriptive-statistic conventions distinguish categorical n/%/missing from quantitative mean/SD or median/IQR. | No candidate. | PASS_1_COMPLETE |
| S018 | Planned adjusted mixed-logistic model and stated Mantel-Haenszel fallback are coherent with protocol record and later final-model documentation. | Fallback was conditional, not claimed as used. | PASS_1_COMPLETE |
| S019 | Sequential alpha plan matches S013/S023/S029/S037. | Alpha-spending curve details not supplied; no exact derivation. | PASS_1_COMPLETE |
| S020 | GEE mRS model labels arm, visit, and interaction consistently with SAP/main secondary analysis. | Correlation/variance definition absent; no exact P/CI reconstruction. | PASS_1_COMPLETE |
| S021 | Secondary-test plan distinguishes t/Wilcoxon, chi-square/Fisher, and AE frequency reporting; matches SAP. | Choice within each “as appropriate” alternative is not supplied prospectively. | PASS_1_COMPLETE |
| S022 | Power assumptions repeat the same printed 15%/5%, 80%, 5%, and sequential plan. | Linked to P1-STAT-01; no separate candidate. | PASS_1_COMPLETE |
| S023 | Two-sided .05 final and .001 interim rules match all planning repetitions. | No candidate. | PASS_1_COMPLETE |
| S024 | Efficacy/futility stopping concepts and DSMB role are consistently labelled. | Conditional-power calculation/threshold is not numerically defined; no inference made. | PASS_1_COMPLETE |
| S025 | Randomized ITT and multiple-imputation handling align with final main/result descriptions. | No candidate. | PASS_1_COMPLETE |
| S026 | Final SAP uses `>5 mm` in the primary endpoint. | Linked to P1-STAT-02; no separate candidate. | PASS_1_COMPLETE |
| S027 | SAP mRS 0-6 and >=4 disability definition/time points agree with main Table 2 footnotes and reported outcomes. | No candidate. | PASS_1_COMPLETE |
| S028 | Planned flow labels are definitional and do not conflict with the reported flow. | No candidate. | PASS_1_COMPLETE |
| S029 | SAP repeats 142/arm, 20% loss, 342 total, 129/37.5%, and alpha plan. | Linked to P1-STAT-01. The 37.5% information fraction remains non-reconcilable only because its denominator is unnamed; no candidate on that point. | PASS_1_COMPLETE |
| S030 | ITT and nonembolized-participant sensitivity labels agree with main/result-supplement sensitivity descriptions. | No candidate. | PASS_1_COMPLETE |
| S031 | SAP descriptive conventions match protocol and results-supplement conventions. | No candidate. | PASS_1_COMPLETE |
| S032 | Interim model/death-as-failure text is prospective and matches the earlier SAP version’s role. | This is not directly compared as a final result because later source text documents a final-version death-definition change. | PASS_1_COMPLETE |
| S033 | SAP explicitly states interim stopping rule was not met and DSMB continued trial; main article repeats that disposition. | No numerical interim statistic is supplied; no exact test audit. | PASS_1_COMPLETE |
| S034 | Final-model, bootstrap adjusted-risk-difference, imputation, subgroup, and sensitivity labels agree with main/result-support records. | Bootstrap resampling details and CI/P relationship are not supplied; no exact reconstruction. | PASS_1_COMPLETE |
| S035 | SAP explicitly records the version change from any-death interim failure handling to neurologic/undetermined-cause death for final analysis; final article follows the stated final definition. | Documented version change, not an unmatched same-version result. | PASS_1_COMPLETE |
| S036 | Secondary-test labels (chi-square/Fisher, GEE, Wilcoxon, Poisson) are consistent with the relevant planned outcome types. | Estimator/test choice for each realized AE comparison is not printed. | PASS_1_COMPLETE |
| S037 | Two-sided .05 and .001 interim stopping labels match other plan records. | No candidate. | PASS_1_COMPLETE |
| S038 | MICE 10 datasets/Rubin pooling and named covariates align with the results supplement and main imputation description. | Imputation draws and pooled variance inputs are unavailable; no reconstruction. | PASS_1_COMPLETE |
| S039 | Results-supplement descriptive n/% and median/IQR conventions are consistent with main/protocol/SAP. | No candidate. | PASS_1_COMPLETE |
| S040 | Results-supplement missing-data and neurologic/unknown-death recurrence rule matches final main/SAP definition. | No candidate. | PASS_1_COMPLETE |
| S041 | R/MICE 10-dataset/Rubin implementation agrees with SAP implementation record. | No candidate. | PASS_1_COMPLETE |
| S042 | Committee-adjudicated recurrence, logistic covariates, OR/95% CI, and benefit direction agree with main primary-result record. | Exact model variance/CI method not supplied. | PASS_1_COMPLETE |
| S043 | Imputed primary OR .64 (.36-1.14), P=.13 agrees across abstract, narrative, Table 2/Figure 2, and results-supplement summary; CI contains 1 and direction agrees with lower observed recurrence. | Labelled diagnostic log-OR/CI approximation is compatible with P=.13; exact post-imputation CI/P construction not supplied. | PASS_1_COMPLETE |
| S044 | Complete-case sensitivity OR .64 (.35-1.14), P=.13 has ordered CI containing 1 and compatible direction. | Exact model/variance and displayed figure data extraction are not sufficiently defined for exact test reconstruction. | PASS_1_COMPLETE |
| S045 | On-site sensitivity 27/162 versus 38/156, OR .61 (.35-1.06), P=.08 has compatible CI/P/direction. | Diagnostic log-OR/CI approximation is about .08; exact imputation/model definition remains unavailable. | PASS_1_COMPLETE |
| S046 | No-imputation sensitivity OR .66 (.37-1.19), P=.17 has ordered CI containing 1 and compatible direction. | Diagnostic log-OR/CI approximation is about .16-.17; exact model details not supplied. | PASS_1_COMPLETE |
| S047 | Excluding nonembolized participants gives OR .71 (.39-1.30), P=.27; CI contains 1 and direction agrees with counts. | Diagnostic log-OR/CI approximation is about .27; exact model details not supplied. | PASS_1_COMPLETE |
| S048 | External EMBOLISE summary prints RR .36 (.11-.80), P=.008; interval excludes 1 and direction/P agree. | Group denominators and external-study model/test are not supplied in this table; no exact reconstruction. | PASS_1_COMPLETE |
| S049 | External STEM summary prints OR .36 (.20-.66), P=.001; interval excludes 1 and direction/P agree. | External-study model/test/variance inputs are not supplied; no exact reconstruction. | PASS_1_COMPLETE |
| S050 | External MAGIC-MT summary prints intervention 24 (6.7%), usual care 9.9%, difference -3.3 percentage points (CI -7.4 to .8), P=.10; CI contains 0 and direction/P agree. | Usual-care numerator/denominator and test/model are not printed; no rate/arithmetic reconstruction. | PASS_1_COMPLETE |
| S051 | EMPROTECT external-summary endpoint definition, N=342, centers, and particle scale agree with main/support material apart from the final-SAP threshold issue recorded separately. | Linked comparator context for P1-STAT-02; no separate candidate. | PASS_1_COMPLETE |
| S052 | EMPROTECT summary repeats observed 24/162 (14.8%) versus 33/157 (21.0%) and imputed OR .64 (.36-1.14), p=.13; matched main occurrences agree. | Observed counts are distinguishable from the imputed effect estimate in the source context; no candidate. | PASS_1_COMPLETE |

## Display-zero review

No S001-S052 relationship prints `P = 0`, `p = 0.000`, or an equivalent display-zero P value. Therefore no `DISPLAY_ZERO_NOT_CANDIDATE` record was applicable. P=1.00 is not a display zero and was evaluated only as reported for S008.

## Counts and limitations

- **Relationships completed:** 52/52 (`PASS_1_COMPLETE`).
- **Provisional candidates emitted:** 2 distinct records (P1-STAT-01 and P1-STAT-02); no C IDs, severity, validity, acceptance, correction, or adjudication assigned.
- **Diagnostic approximations:** 4 (S002, S005, S006, S045-S047 grouped as sensitivity OR/CI diagnostics); all are labelled and not substitutes for reported models.
- **Key missing definitions retained:** information-fraction denominator/alpha-spending computation; imputed-model CI/P construction and variance inputs; GEE working correlation/variance; secondary-outcome CI methods; exact Fisher convention; external-trial denominators and models/tests; conditional-power calculation/futility limit.
