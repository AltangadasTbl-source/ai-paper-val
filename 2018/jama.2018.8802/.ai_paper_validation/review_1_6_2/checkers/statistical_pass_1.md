# Statistical pass 1

Runtime agent: /root/stat1. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. PASS_1_COMPLETE.

Scope: all44 mapped source pages, covering120 stable relationships S001–S120. These include all86 separate estimate/95%CI/P tuples in main Tables2/3 and eTables3/4, all10 eTable2 P values, symptomatic intracerebral hemorrhage, both Kaplan–Meier/log-rank panels, and21 statistical-design/method relationships. No sampling, finding quota, old audit input, external source, unapproved Python helper, or inferred preferred analysis was used. Source roles by content: main article and non-plan supplement REPORT; protocol bundle PLAN. Direct pdftotext Poppler25.03.0 stdout reads of main pp.3–5,8, protocol pp.13–19 and supplement pp.2,5–9 confirmed cited source text; reusable DOC-001-p08.png confirmed Table3 signs and P values. Compute device CPU; no derivative changed or produced.

Pass-1 output:4 findings and9 excluded apparent-observation rows. Reconciled checks, missing reproducibility inputs, all printed effect tuples and source-grounded method matches are recorded individually in [relationship inventory](../statistics/relationship_inventory.md). The strongest direct inferential discrepancy is the in-hospital death interval/P conflict. Other findings concern primary outcome definition, clinical time origin and primary-analysis population attribution. Each requires the independent inclusion screen; no C ID or adjudication is assigned here.

## Findings

### F-ST1-001

**Title:** In-hospital mortality absolute-difference interval includes zero while its P value is below .05.

**Relationships:** S035, S117. Proposed primary relationship type S_W; all relationships S_W.

**Compared locations and document roles:** REPORT [main article PDF p.8, Table3, Death/In hospital, adjusted absolute-difference and adjacent P columns](../../../jama_wang_2018_oi_180070.pdf#page=8); REPORT [p.4 Data Analysis significance/confidence rule](../../../jama_wang_2018_oi_180070.pdf#page=4). REPORT [p.5 Clinical Events](../../../jama_wang_2018_oi_180070.pdf#page=5) states no significant total-mortality difference in hospital or3/6/12mo; p.8 HR column is an alternative inferential summary, not substituted for the adjacent difference P value.

**Printed values:** I11/2400(0.5%), C23/2400(1.0%); adjusted absolute difference −0.7 percentage points (95%CI −1.1 to0.2), P=.009. The separate adjusted HR is0.96(0.90–1.02), P=.14. Methods state95%CIs, all tests two-sided and statistical significance atP<.05.

**Rule and calculation:** Difference null0 lies in[−1.1,0.2], while .009<.05. Thus the printed confidence interval and its adjacent test disagree about exclusion of the null at the stated levels. Endpoint order and point containment themselves hold: −1.1<−.7<.2. The P interval[.0085,.0095] remains below .05, and the upper-CI interval[.15,.25] remains above0. These are explanatory display bounds; routeA category1 is never excluded through the display-precision rule.

**Diagnostic approximation:** If one assumes the symmetric normal CI pattern that fits the other Table3 difference rows, its printed midpoint is(−1.1+.2)/2=−.45 rather than−.7. Allowing endpoint rounding gives midpoint[−.50,−.40], whereas the point's interval is[−.75,−.65], leaving a gap.15/|−.7|≈.214. A normal-width diagnostic givesSE=(.2−(−1.1))/(2×1.95996)≈.3316 and|z|≈2.111, P≈.035, not.009. This approximation does not establish the actual CI/test construction and is not the basis of the null-crossing finding.

**Focus area:** B (estimate and test logic). **Proposed review domain:** statistical_results.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** In-hospital mortality adjusted absolute difference, its uncertainty interval and significant/nonsignificant interpretation; extraction ofP=.009 versus the interval's null inclusion.

**Why context does not resolve it:** RouteA category1 expressly registers interval/P conflicts. The separate HR/P and nonsignificant narrative do not remove the adjacent difference/CI/P conflict.

**Source-grounded alternatives and missing definition:** The difference test and CI may use different procedures or analyses; the source does not name a difference-specific CI construction or test/variance estimator. A non-symmetric interval could explain midpoint asymmetry but not supply a missing explanation for the displayed null/P decisions. The HR concerns a different estimand and has its own P column. Any different-analysis explanation must be documented for human interpretation.

**Exact human question:** Which stated analysis and inferential procedure produced the in-hospital mortality absolute difference,95%CI andP=.009, and how should a reader reconcile the interval's inclusion of0 with that P value?

### F-ST1-002

**Title:** Primary composite adherence is described using aggregate opportunity weighting in plan/supplement and patient averaging in the main report.

**Relationships:** S104, S105, S100. Proposed primary relationship type P_R; all relationships P_R, S_C.

**Compared locations and document roles:** PLAN [protocol PDF p.16 lines216–219](../../../joi180070supp1_prod.pdf#page=16); REPORT [main article PDF p.3 Outcomes, composite-definition paragraph](../../../jama_wang_2018_oi_180070.pdf#page=3); REPORT [non-plan supplement PDF p.2 eAppendix, “same endpoint definition used in the randomized phase” and composite formula](../../../joi180070supp2_prod.pdf#page=2). PLAN [pp.18–19 opportunity-level analysis](../../../joi180070supp1_prod.pdf#page=18) and REPORT [main p.4 opportunity-level OR analysis](../../../jama_wang_2018_oi_180070.pdf#page=4) help distinguish the analysis quantities.

**Printed statements:** Plan defines composite as total interventions performed among eligible patients divided by total possible interventions among eligible patients. Report supplement repeats this definition and says it used the same endpoint definition as the randomized phase. Main report defines eligible measures performed divided by eligible measures “for a given patient,” then says “The composite measure was calculated for each patient and then averaged.” Table2 reports composite mean(SD)88.2(15.1)% versus84.8(18.2)%, adjusted difference3.5(0.7–6.4)%,P=.02; main narrative/abstract has3.54(0.68–6.40)%.

**Rule and reproduced logical comparison:** Write patienti eligible opportunities k_i and fulfilled opportunities r_i. The plan/supplement formula reads Σr_i/Σk_i=Σk_i(r_i/k_i)/Σk_i, an opportunity-weighted average. Main formula reads (1/n)Σ(r_i/k_i), a patient-unweighted average. Their weighting differs when eligibility counts differ; equality requires equal k_i or a special balance not stated. The source describes multiple eligibility criteria and opportunity-level binary modeling, so these are distinguishable descriptions of the primary composite, not OR-versus-crude-ratio arithmetic. The individual k_i/r_i are not supplied, so the actual numerical difference between definitions is not computable and is not claimed. Display-precision arithmetic is not applicable to the reproduced formula/definition comparison.

**Focus area:** D (planned versus reported statistical design), with C (method/estimand mapping). **Proposed review domain:** protocol_report.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The primary composite adherence measure represented by88.2% versus84.8% and its3.54-point adjusted contrast; baseline80% used for power is also described with the aggregate formula.

**Why context does not resolve it:** RouteA category5 covers planned-versus-reported composite/outcome definitions. The main text explicitly averages patient values, while plan and supplement explicitly give total-over-total, and the supplement asserts same endpoint definition. Source text supplies no statement equating the two weightings or identifying a disclosed amendment.

**Source-grounded alternatives and missing definition:** The aggregate wording may be intended as shorthand for a within-patient calculation, or the descriptive patient mean may intentionally differ from the opportunity-level OR estimand. The latter is partly supported by p.4 binary-opportunity analysis but does not identify which weighting the plan's composite formula intended. The number of eligible opportunities for each patient and the exact construction of the adjusted absolute difference are not supplied.

**Exact human question:** Was the prespecified composite adherence outcome an aggregate opportunity-weighted ratio or an average of patient-specific ratios, and which definition generated the reported means, adjusted difference and baseline sample-size input?

### F-ST1-003

**Title:** The same clinical follow-up results are attributed to time after discharge and time after symptom onset.

**Relationships:** S109, S112. Proposed primary relationship type S_W; all relationships S_W. Plan corroborates the onset description and is not an independent conflict.

**Compared locations and document roles:** REPORT [main article PDF p.5 Clinical Events, opening sentence referring to Table3](../../../jama_wang_2018_oi_180070.pdf#page=5); REPORT [p.3 Outcomes, secondary-outcome definition](../../../jama_wang_2018_oi_180070.pdf#page=3); REPORT [p.4 Data Analysis, clinical time-to-event specification](../../../jama_wang_2018_oi_180070.pdf#page=4); REPORT [p.8 Table3 disability footnote b and Figure2 axes/caption](../../../jama_wang_2018_oi_180070.pdf#page=8). PLAN [p.16 lines223–230](../../../joi180070supp1_prod.pdf#page=16) and [p.19 lines280–282](../../../joi180070supp1_prod.pdf#page=19) corroborate onset.

**Printed statements/values:** Clinical Events says Table3 shows clinical vascular events and disability at3,6,12 months “after discharge.” Outcome definition and Cox specification say3,6,12 months after “initial symptom onset.” Table3 disability footnote says after stroke onset; Figure2 axes/caption say days after stroke symptom onset. Table3 vascular effects at3,6,12mo include adjusted differences−2.0(−3.5 to−.6),−2.2(−4.0 to−.4),−3.1(−5.3 to−1.0)% andHR.65,.72,.72. Disability corresponding adjusted differences are−3.7,−3.9,−3.1%.

**Rule and reproduced logical comparison:** Discharge and symptom onset are distinct origins for the same displayed3/6/12mo outcome results. No numerical conversion is made from median hospital stay because patient-specific admission/discharge/onset times are unavailable. The comparison concerns attribution of the reported time point, not a typographic symbol or rounded number; display intervals/relative discrepancy do not apply.

**Focus area:** B/C (time-to-event/outcome-result interpretation). **Proposed review domain:** report_internal_inconsistency.

**Qualifying route:** Route B.

**Affected result or extracted value:** The abstract's key secondary new vascular-event results and Table3 vascular/disability/mortality results at each nominal follow-up point; extraction as onset-based versus postdischarge risks.

**Why context does not resolve it:** B1: result/time-point attribution and clinical analysis mapping are in scope. B2: the sentence assigns the whole Table3 set to discharge, while outcome methods and figure assign onset; it does not identify an alternative visit window or different analysis. B3: onset-based versus discharge-based follow-up changes which time horizon the same effect estimate is taken to represent. Several locations support onset, but that support does not supply a patient-level discharge/onset mapping for the narrative statement.

**Source-grounded alternatives and missing definition:** The narrative may use discharge informally for follow-up contact, while actual analyses use onset. Alternatively different clinical summaries could use different visit windows. The supplied package does not state a separate discharge-based analysis or explain the switch in origin.

**Exact human question:** Are all Table3 clinical results defined at3,6,12 months after initial symptom onset, after discharge, or according to distinct windows, and which time-origin description should govern extraction of these estimates?

### F-ST1-004

**Title:** Figure1 primary-analysis patient counts correspond to completed follow-up rather than the4800-patient primary-analysis population stated elsewhere.

**Relationships:** S106, S108, S116. Proposed primary relationship type S_W; all relationships S_W.

**Compared locations and document roles:** REPORT [main article PDF p.5 Figure1 bottom patient boxes and12-Month Follow-up boxes](../../../jama_wang_2018_oi_180070.pdf#page=5); REPORT [p.4 Results, “4800 patients ... included in the primary analysis” and completed follow-up paragraph](../../../jama_wang_2018_oi_180070.pdf#page=4); REPORT [p.7 Table2, all-or-none denominator2400 each](../../../jama_wang_2018_oi_180070.pdf#page=7); REPORT [p.1 abstract3980 completed](../../../jama_wang_2018_oi_180070.pdf#page=1).

**Printed values/statements:** Figure1 labels2003 intervention and1977 control patients “included in primary analysis,” after397/423 lost to12-month follow-up. Text says4800 enrolled/included in primary analysis;2003/1977 are those who completed12-month follow-up. All-or-none co-primary result uses1290/2400 versus1147/2400.

**Rule and calculation:**2003+1977=3980;4800−397−423=3980. Thus the flow's values reproduce completed-follow-up counts, while the stated primary population and Table2 denominators sum4800. Treating printed integers conservatively with half-unit intervals, summed figure interval is[3979,3981]; text total interval[4799.5,4800.5]. Gap818.5,relative to4800≈.17052>.05. Within each arm, figure versus2400 has gaps396 and422,relative.165 and.17583. These exceed the display rule; no actual participant count is inferred from rounding.

**Focus area:** A/C (analysis-population count and attribution). **Proposed review domain:** report_internal_inconsistency.

**Qualifying route:** Route B.

**Affected result or extracted value:** Analysis population size attached to the co-primary adherence result:3980 from Figure1 versus4800/2400-per-arm from text and Table2.

**Why context does not resolve it:** B1: primary analysis-set size is in scope. B2: the figure explicitly uses the same primary-analysis label as the4800-patient statement without an outcome-specific qualification. B3: a reader extracting trial analysis population from the flow may select3980 while primary results use4800. The12-month heading suggests an alternative explanation but leaves the printed primary-analysis designation conflicting.

**Source-grounded alternatives and missing definition:** Figure1 may intend its bottom boxes to describe12-month clinical follow-up, whereas adherence was measured during hospitalization in all enrolled patients. The narrative and Table2 support that interpretation; no source statement explicitly renames the figure's analysis set. Different populations for individual clinical outcomes also appear (disability available/alive denominators), which do not make the flow count the co-primary population.

**Exact human question:** Which analysis population do Figure1's2003 and1977 primary-analysis patient boxes denote, and how should they be reconciled with the stated4800-patient primary analysis and Table2's2400-per-arm co-primary denominators?

## Excluded observations

Only apparent issues considered and not emitted are listed; fully reconciled checks remain in S records.

| Location | Observation | Reason code |
|---|---|---|
| PLAN p.17 Sample size; REPORT MAIN p.4 Sample Size, S100 | A binary-proportion sample-size approximation would depend on treating the patient-level composite as binary and on a chosen variance formula. Source gives no composite SD/formula/unequal-size allowance; no source-grounded sample-size conflict reproduced. | CONDITIONAL_OR_UNREPORTED |
| REPORT MAIN Tables2/3 pp.7–8 and REPORT SUPP eTables3/4 pp.6,8; S001–S042,S053–S096 | Adjusted absolute differences and OR/HR values differ from crude differences/ratios of printed events. Footnotes explicitly state adjusted patient/hospital models. | MODEL_VERSUS_CRUDE |
| REPORT MAIN p.6 Table1 versus REPORT SUPP p.5 eTable2; S116 | Descriptive NIHSS medians and dyslipidemia baseline copies differ across randomized-arm and one-year-mRS availability displays, without changing a reported outcome or population size. | PERIPHERAL_COMPARISON |
| REPORT MAIN p.3 LDL wording; PLAN p.15 Table3; REPORT SUPP p.3 eTable1; S102 | Main summary saysLDL>100 while detailed cited eligibility uses≥100/prior lipid therapy/undocumented LDL. Detailed specifications resolve the summary's terminology for a field reader; no displayed result at the boundary supplies a numeric conflict. | TERMINOLOGY_OR_WORDING |
| PLAN p.19 lines276–279 and REPORT MAIN p.4 illustrative example; S105 | Example says5 eligible of7 although trial predefined9 measures; it is explicitly a worked hypothetical patient, and3+2=5 observations is coherent. | CONTEXT_RESOLVES |
| REPORT MAIN p.4 logistic/GEE and mixed-model binary wording; p.8 footnote b; S110 | Binary disability model described as logistic and mixed model; these labels can describe a binary mixed logistic model. No supplied covariance/test output contradicts a printed estimate. | CONDITIONAL_OR_UNREPORTED |
| PLAN p.19 general sensitivity specification; REPORT MAIN p.5/REPORT SUPP p.8 eTable4; S113 | Separate all-or-none sensitivity result is absent, but the plan does not explicitly prespecify that contrast; it gives a general contraindication-inclusive strategy which the report implements for composite/individual measures. | CONDITIONAL_OR_UNREPORTED |
| PLAN p.17 three feedback cycles×30 versus120/cluster; PLAN p.13 Figure4; S118 | Figure4 depicts four30-patient batches and three between-batch feedback loops; distinguishing patient batches from loops reconciles120 patients with three improvement cycles. | CONTEXT_RESOLVES |
| REPORT MAIN pp.4–5, symptomatic intracerebral hemorrhage; S097 | Broad categorical χ² wording does not specify the sparse comparison's exact test or cluster variance; raw Pearson P≈.210 differs from .26, while two-sided Fisher exact diagnostic P≈.25593 reproduces .26. This observation depends on assuming the unadjusted asymptotic implementation, with no interval or test statistic supplied. | CONDITIONAL_OR_UNREPORTED |

## Limits and handoff

No registered finding relies on an unstated model variance, crude ratio replacing an adjusted effect, diagnostic P-value recreation, or external literature. Source lacks event times/risk-set histories for exact Cox/log-rank recreation, ranks for Wilcoxon, detailed variance/CI procedures, patient-specific eligibility/fulfilled-care data, and primary composite SD/sample-size equation. These are precise reproduction limits, not a scientific coverage gap. Both borderlineP=.05 difference/ratio rows and all86 interval tuples were checked individually under the strictP<.05 rule. No separate standard errors/test statistics were supplied. All4 findings retain neutral questions for independent screening and later human adjudication.


## Explicit documentary pass-one coverage index

Coordinator production repair: the original specialist's scope S001–S120 and 120 individually documented PASS_1_COMPLETE checks are expanded below for mechanical cross-artifact reconciliation. These rows transcribe the specialist-authored per-ID completion records already present in statistics/relationship_inventory.md; they add no scientific reassessment, finding, classification or candidate. The complete per-ID source tuples and original pass-one implications remain in that linked inventory.

| Statistical relationship | Original individual pass-one record | State |
|---|---|---|
| S001 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S002 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S003 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S004 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S005 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S006 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S007 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S008 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S009 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S010 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S011 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S012 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S013 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S014 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S015 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S016 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S017 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S018 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S019 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S020 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S021 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S022 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S023 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S024 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S025 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S026 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S027 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S028 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S029 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S030 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S031 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S032 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S033 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S034 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S035 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S036 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S037 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S038 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S039 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S040 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S041 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S042 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S043 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S044 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S045 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S046 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S047 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S048 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S049 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S050 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S051 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S052 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S053 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S054 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S055 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S056 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S057 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S058 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S059 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S060 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S061 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S062 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S063 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S064 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S065 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S066 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S067 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S068 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S069 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S070 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S071 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S072 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S073 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S074 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S075 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S076 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S077 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S078 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S079 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S080 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S081 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S082 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S083 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S084 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S085 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S086 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S087 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S088 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S089 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S090 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S091 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S092 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S093 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S094 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S095 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S096 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S097 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S098 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S099 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S100 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S101 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S102 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S103 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S104 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S105 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S106 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S107 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S108 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S109 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S110 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S111 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S112 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S113 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S114 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S115 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S116 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S117 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S118 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S119 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
| S120 | Original specialist-authored inventory row retained | PASS_1_COMPLETE |
