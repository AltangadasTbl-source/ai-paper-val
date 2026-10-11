# Workflow 1.6.2 mechanical evidence recheck

Runtime agent: /root/recheck. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Scope: the complete stable ledger, C001, C002, C003, C004, including every repeated and contextual location named below. All candidates remain **Pending Human Adjudication**. Evidence states record reproduced source facts and are not human dispositions.

The complete START_PROMPT.md, QUALITY_CONTROL_SCOPE.md and review_contract.md were read. The current ledger, independent screening artifact and checker facts were used to identify the registered comparisons, not as the final evidence authority. Every location below was checked on a fresh rendering of the exact supplied PDF page and with direct same-source layout extraction. CPU direct Poppler 25.03.0 was used for `pdftotext -layout` and `pdftoppm` at 120 dpi. No OCR, web, unapproved Python helper, nested agent, legacy review input, source mutation or reused-artifact mutation was used. The full 11-page/22-derivative provenance record is [recheck_derivative_record.md](../preprocessing/recheck_derivative_record.md). PDF links below name physical source pages and resolve from this artifact.

### Direct-source derivative log

Every derivative is under review_1_6_2/preprocessing/. All commands completed successfully. For each row, `pdftotext` means direct layout extraction with `-layout -f N -l N`; `pdftoppm` means direct rendering with `-r 120 -f N -l N -singlefile -png`. All 11 PNGs were viewed and their disputed wording, numbers and layout checked.

| Source path | PDF page | Derivative filename | Engine | Version | Device |
|---|---:|---|---|---|---|
| jama_wang_2018_oi_180070.pdf | 1 | recheck-main-p1.txt | pdftotext, Poppler | 25.03.0 | CPU |
| jama_wang_2018_oi_180070.pdf | 1 | recheck-main-p1.png | pdftoppm, Poppler | 25.03.0 | CPU |
| jama_wang_2018_oi_180070.pdf | 3 | recheck-main-p3.txt | pdftotext, Poppler | 25.03.0 | CPU |
| jama_wang_2018_oi_180070.pdf | 3 | recheck-main-p3.png | pdftoppm, Poppler | 25.03.0 | CPU |
| jama_wang_2018_oi_180070.pdf | 4 | recheck-main-p4.txt | pdftotext, Poppler | 25.03.0 | CPU |
| jama_wang_2018_oi_180070.pdf | 4 | recheck-main-p4.png | pdftoppm, Poppler | 25.03.0 | CPU |
| jama_wang_2018_oi_180070.pdf | 5 | recheck-main-p5.txt | pdftotext, Poppler | 25.03.0 | CPU |
| jama_wang_2018_oi_180070.pdf | 5 | recheck-main-p5.png | pdftoppm, Poppler | 25.03.0 | CPU |
| jama_wang_2018_oi_180070.pdf | 6 | recheck-main-p6.txt | pdftotext, Poppler | 25.03.0 | CPU |
| jama_wang_2018_oi_180070.pdf | 6 | recheck-main-p6.png | pdftoppm, Poppler | 25.03.0 | CPU |
| jama_wang_2018_oi_180070.pdf | 7 | recheck-main-p7.txt | pdftotext, Poppler | 25.03.0 | CPU |
| jama_wang_2018_oi_180070.pdf | 7 | recheck-main-p7.png | pdftoppm, Poppler | 25.03.0 | CPU |
| jama_wang_2018_oi_180070.pdf | 8 | recheck-main-p8.txt | pdftotext, Poppler | 25.03.0 | CPU |
| jama_wang_2018_oi_180070.pdf | 8 | recheck-main-p8.png | pdftoppm, Poppler | 25.03.0 | CPU |
| joi180070supp1_prod.pdf | 16 | recheck-plan-p16.txt | pdftotext, Poppler | 25.03.0 | CPU |
| joi180070supp1_prod.pdf | 16 | recheck-plan-p16.png | pdftoppm, Poppler | 25.03.0 | CPU |
| joi180070supp1_prod.pdf | 18 | recheck-plan-p18.txt | pdftotext, Poppler | 25.03.0 | CPU |
| joi180070supp1_prod.pdf | 18 | recheck-plan-p18.png | pdftoppm, Poppler | 25.03.0 | CPU |
| joi180070supp1_prod.pdf | 19 | recheck-plan-p19.txt | pdftotext, Poppler | 25.03.0 | CPU |
| joi180070supp1_prod.pdf | 19 | recheck-plan-p19.png | pdftoppm, Poppler | 25.03.0 | CPU |
| joi180070supp2_prod.pdf | 2 | recheck-supp-p2.txt | pdftotext, Poppler | 25.03.0 | CPU |
| joi180070supp2_prod.pdf | 2 | recheck-supp-p2.png | pdftoppm, Poppler | 25.03.0 | CPU |

## C001 — Primary composite definition and weighting

**Finding provenance:** F-XS-003, F-ST1-002.

**Location found; source value/text matched; comparator matched:** Yes for every row. Direct visual reading agrees with fresh layout extraction and the registered wording and values.

| Exact supplied-source location | Role by content | Directly confirmed content and comparison function |
|---|---|---|
| [Protocol p.16, lines216–220](../../../joi180070supp1_prod.pdf#page=16) | PLAN: prospective outcome definition | Composite is the total number of interventions performed among eligible patients divided by the total number of possible interventions among eligible patients. All-or-none is separately defined as the proportion of eligible patients receiving every performance-measure intervention. This is the planned composite definition compared with the main report. |
| [Results supplement p.2, eAppendix](../../../joi180070supp2_prod.pdf#page=2) | REPORT: account of the completed prerandomization survey | It explicitly states that it used the same endpoint definition as the randomized phase, then gives the total-performed/total-possible definition among eligible patients. Baseline composite values are 80.2% versus 79.5%. This is an independently differing report definition, not a prospective plan merely because it concerns a prerandomization phase. |
| [Main p.3, Outcomes, composite paragraph](../../../jama_wang_2018_oi_180070.pdf#page=3) | REPORT: completed-trial outcome description | The ratio is defined for a given patient and the composite is calculated for each patient and then averaged. This is the conflicting comparator to both total-over-total descriptions. |
| [Main p.7, Table 2 composite row and footnote a](../../../jama_wang_2018_oi_180070.pdf#page=7) | REPORT: primary results display | Mean (SD) 88.2 (15.1)% versus 84.8 (18.2)%; adjusted absolute difference 3.5 (95% CI 0.7–6.4) percentage points, P=.02; population-average OR 1.39 (1.12–1.72), P=.003. The footnote identifies patient/hospital adjustment. This identifies the affected result; no crude recomputation is substituted for the adjusted contrast. |
| [Main p.1, abstract primary composite result](../../../jama_wang_2018_oi_180070.pdf#page=1) and [p.5, adherence results](../../../jama_wang_2018_oi_180070.pdf#page=5) | REPORT: same-trial result copies | The composite means are 88.2% versus 84.8%; the absolute difference is 3.54 (0.68–6.40) percentage points, P=.02. These are more precise copies identifying the same affected result, not additional conflicts. |
| [Protocol p.18, lines266–274](../../../joi180070supp1_prod.pdf#page=18) and [p.19, lines275–279](../../../joi180070supp1_prod.pdf#page=19) | PLAN: prospective statistical analysis | GEE accounts for within-hospital correlation; each eligible care opportunity supplies a binary observation. The example gives five observations, three fulfilled and two unfulfilled. These passages corroborate a separate opportunity-level inferential description and do not add an internal-plan conflict. |
| [Main p.4, Data Analysis, composite/opportunity paragraph](../../../jama_wang_2018_oi_180070.pdf#page=4) | REPORT: analysis description | Each care opportunity supplies a binary observation, and the effects are population-average odds ratios. The same five-opportunity example appears. This is contextual analysis evidence, not another conflicting composite mean definition. |

**Consistency rule applicable:** Yes. Focus D, planned-versus-reported primary-outcome definition; Route A, category 5, composite-definition change. Report-to-report definition agreement is also checked. The source describes eligible measures that depend on patient characteristics, so a total-over-total ratio and equal patient averaging are distinct definitions.

**Calculation or logical comparison reproduced:** Let r_i be fulfilled opportunities, k_i>0 eligible opportunities, p_i=r_i/k_i, and n the number of included patients. The plan/supplement total-over-total description is A=Σr_i/Σk_i=Σk_i p_i/Σk_i. The main description is B=Σp_i/n. A weights patients by k_i; B weights each patient equally. Algebraically A−B=Cov_n(k_i,p_i)/mean(k_i). Thus the definitions need not produce the same value when eligibility counts vary, although equal counts or zero covariance can make them coincide in particular data. The printed definitional discrepancy is reproduced; an actual trial-level difference between A and B is not established or claimed.

**Display-precision interval check:** Not applicable to the substantive definition/formula comparison because it has no disputed printed numerical recomputation. The result copies themselves reconcile: Table 2 difference [3.45,3.55] intersects the abstract [3.535,3.545]; lower limits [0.65,0.75] and [0.675,0.685] intersect; upper limits [6.35,6.45] and [6.395,6.405] intersect. Each gap is zero and relative discrepancy is zero. They are not an additional candidate pattern.

**Necessary inputs available:** Yes for the source-grounded logical comparison: both explicit definitions, outcome identification, variable eligibility context and opportunity-model description are printed. **Exact missing inputs or definitions:** Individual r_i and k_i, any analytic weights, the implemented composite scoring algorithm, construction of the adjusted absolute difference, and a supplied statement equating the two descriptions or documenting an amendment. Those omissions prevent trial-level numeric reanalysis, not comparison of the printed definitions.

**Source-grounded alternative interpretation:** Total-over-total language may have been intended as a within-patient definition followed by patient averaging; alternatively, the descriptive mean and opportunity-level inferential estimand may intentionally differ. The printed opportunity-level model supports the latter possibility but does not identify how the planned/supplementary composite formula maps to the descriptive means or adjusted difference.

**Direct observation versus inferred explanation:** Direct observation is the explicit patient-average instruction versus aggregate total-over-total wording and the supplement's same-endpoint statement. The weighting distinction follows algebraically from their literal readings. An implemented analysis change, an amendment, or any change in numerical outcome magnitude would be an explanation requiring additional evidence; none is inferred.

**Classification confirmation:** Document roles are as recorded in the location table. Primary relationship type **P_R**; all relationships **P_R, S_C**; review domain **protocol_report**. PLAN p.16 versus REPORT main p.3 supplies P_R; REPORT supplement p.2 versus REPORT main p.3 supplies S_C. P_R has precedence. Opportunity-analysis descriptions and primary-result copies are supporting context, not additional P_P or S_W relationships. No classification correction is needed. **Classification ambiguity:** Aggregate wording may have been shorthand or an amendment may exist outside the supplied evidence; neither is documented here.

**Evidence state:** **reproduced**. Determining recheck fact: direct PDF reading preserves all three explicit descriptions, including the main instruction to calculate each patient's composite and then average. No transcribed value or cited location needed correction.

**Exact remaining human question:** Which weighting and implemented scoring rule generated the planned and reported composite outcome, its mean percentages and adjusted absolute difference, and how does the eAppendix's same-endpoint statement reconcile the total-over-total and patient-average descriptions?

## C002 — Primary-analysis population counts

**Finding provenance:** F-NUM-001, F-XS-001, F-ST1-004.

**Location found; source value/text matched; comparator matched:** Yes for every row. The fresh source rendering confirms that both figure bottom boxes explicitly say primary analysis, and that the loss counts precede them.

| Exact supplied-source location | Role by content | Directly confirmed content and comparison function |
|---|---|---|
| [Main p.4, Results opening](../../../jama_wang_2018_oi_180070.pdf#page=4) | REPORT: participant/analysis account | 4800 patients enrolled prospectively and included in the primary analysis, referring to Figure 1. This is the disputed primary-analysis total. |
| [Main p.4, final baseline/follow-up paragraph](../../../jama_wang_2018_oi_180070.pdf#page=4) | REPORT: completed follow-up account | 2003 (83.5%) intervention and 1977 (82.4%) control patients completed 12-month follow-up. These identify the origin of the smaller counts. |
| [Main p.5, Figure 1, enrollment, 12-month follow-up and bottom analysis boxes](../../../jama_wang_2018_oi_180070.pdf#page=5) | REPORT: trial flow display | 2400 enrolled and received allocated intervention/control in each arm. Losses are 397 intervention and 423 control. Bottom boxes show 20 hospitals each and 2003/1977 patients included in primary analysis. Both affected arm occurrences are confirmed. |
| [Main p.7, Table 2 all-or-none row](../../../jama_wang_2018_oi_180070.pdf#page=7) | REPORT: co-primary result display | 1290/2400 (53.8%) versus 1147/2400 (47.8%). Both 2400 denominators are confirmed; the row provides the full randomized denominator for the co-primary result. |
| [Main p.1, abstract design/interventions and Results](../../../jama_wang_2018_oi_180070.pdf#page=1) | REPORT: same-trial summary | 4800 enrolled, 2400 per arm, 3980 (82.9%) completed 12-month follow-up. This corroborates total enrollment and follow-up completion without introducing another inconsistent copy. |

**Consistency rule applicable:** Yes. Focus A, primary-analysis counts and denominators, with analysis-population attribution. Route B: B1 this changes the named primary-analysis population size; B2 both source locations explicitly use primary analysis without specifying separate primary outcomes; B3 extracting the primary population from the flow yields 3980 rather than the 4800 in Results or 2400-per-arm co-primary denominators.

**Calculation reproduced:** 2003+1977=3980; 2400−397=2003; 2400−423=1977; 4800−397−423=3980. Therefore losses and completed follow-up reconcile internally, but the two printed populations carrying the primary-analysis designation differ by 820 patients in total, 397 and 423 by arm. This does not establish actual computational exclusion from any primary analysis.

**Display-precision interval check:** Conservatively allowing displayed integers their half-unit intervals, the Figure 1 sum is [2002.5+1976.5,2003.5+1977.5]=[3979,3981]; Results total is [4799.5,4800.5]. Gap=4799.5−3981=818.5, relative discrepancy=818.5/4800=0.1705208333>0.05. Intervention figure [2002.5,2003.5] versus Table 2 denominator [2399.5,2400.5] gives gap396, relative396/2400=0.165>0.05. Control [1976.5,1977.5] versus [2399.5,2400.5] gives gap422, relative422/2400=0.1758333333>0.05. Actual counts are discrete; these deliberately conservative intervals cannot bridge the difference.

**Necessary inputs available:** Yes for the comparison and arithmetic: both primary-analysis labels, all four enrollment/analysis arm counts, both losses and co-primary denominators are printed. **Exact missing inputs or definitions:** Which outcome-specific analysis set the figure bottom boxes denote and whether that label was intended to denote follow-up completion; no patient-level analytic inclusion flags or exact primary model dataset are supplied. Those flags are not needed to reproduce the printed count comparison.

**Source-grounded alternative interpretation:** The bottom boxes may describe patients with completed 12-month clinical follow-up, whereas inpatient adherence was measured among all enrolled patients. The figure's ordering, identical follow-up counts, explicit Results completion statement and Table 2 denominator all support that possibility, but no outcome-specific qualifier connects the figure's primary-analysis label to a separately named analysis.

**Direct observation versus inferred explanation:** The direct facts are the two sets of printed counts with their identical primary-analysis designation and the exact arithmetic match of smaller counts to completers. A flow-label explanation is plausible, not evidence that participants were computationally omitted from the co-primary analysis. No loss-driven outcome bias or analysis preference is inferred.

**Classification confirmation:** Every compared and supporting location is **REPORT**, in the same article. Primary relationship type **S_W**; all relationships **S_W**; review domain **statistical_results**. Counts and denominators invoke the scope's explicit statistical_results rule, even though attribution to an analysis set also matters. No P_R or S_C relationship arises. No classification correction is needed. **Classification ambiguity:** The intended outcome-specific population is unresolved, but the within-report relationship and counts domain are supported.

**Evidence state:** **reproduced**. Determining recheck fact: fresh exact-source rendering confirms 2003 and 1977 explicitly labeled included in primary analysis, while Results explicitly assigns 4800 to primary analysis and Table 2 uses 2400 each. The interval gap remains above the display threshold. No transcription or location correction is required.

**Exact remaining human question:** Which analysis population do Figure 1's 2003 and 1977 primary-analysis boxes denote, and how should those labels be reconciled with 4800 primary-analysis patients and Table 2's 2400-per-arm co-primary denominators?

## C003 — Clinical follow-up time origin

**Finding provenance:** F-XS-002, F-ST1-003.

**Location found; source value/text matched; comparator matched:** Yes for every row and for each affected 3-, 6- and 12-month reference. Direct source rendering confirms the discharge wording and all onset wording.

| Exact supplied-source location | Role by content | Directly confirmed content and comparison function |
|---|---|---|
| [Main p.5, Clinical Events opening](../../../jama_wang_2018_oi_180070.pdf#page=5) | REPORT: attribution of the reported clinical results | Table 3 is said to show in-hospital and long-term mortality, new clinical vascular events and disability at 3, 6 and 12 months after discharge. The following vascular effects are −2.03, −2.18 and −3.13 percentage points at those three time points. This is the differing result-origin statement. |
| [Main p.3, Outcomes secondary-outcome paragraph](../../../jama_wang_2018_oi_180070.pdf#page=3) | REPORT: outcome definitions | The secondary outcomes include in-hospital death, new vascular events, disability and all-cause mortality at 3, 6 and 12 months after initial symptom onset. This is an onset-based comparator for the same named clinical outcomes. |
| [Main p.4, Data Analysis, right-column clinical analysis paragraph](../../../jama_wang_2018_oi_180070.pdf#page=4) | REPORT: outcome-analysis specification | Clinical vascular events and mortality at discharge and 3, 6 and 12 months after initial symptom onset are time-to-event outcomes. A binary mixed model is named for 3-, 6- and 12-month disability. This distinguishes the inpatient result from onset-based follow-up results. |
| [Main p.8, Table 3, vascular/disability/death 3-, 6- and 12-month rows and disability footnote b](../../../jama_wang_2018_oi_180070.pdf#page=8) | REPORT: same clinical-result display | All three nominal time points appear for each outcome. Footnote b places disability at 3, 6 and 12 months after stroke onset. Vascular adjusted differences are −2.0, −2.2, −3.1 percentage points; disability differences are −3.7, −3.9, −3.1. The candidate concerns attribution of these displayed results, not differences from their more precise narrative copies. |
| [Main p.8, Figure 2 panels A/B axes and caption](../../../jama_wang_2018_oi_180070.pdf#page=8) | REPORT: vascular/death follow-up display | Both axes read Days After Stroke Symptom Onset. The caption says the log-rank comparison uses days after stroke symptom onset to new clinical vascular events or death; follow-up medians are 364 and 365 days. Both affected panels and the caption are confirmed. |
| [Main p.6, Table 1 length-of-stay row](../../../jama_wang_2018_oi_180070.pdf#page=6) | REPORT: contextual descriptive result | Intervention median 13 days (IQR10–15); control 12 days (IQR9.5–15). This shows nonzero hospitalization context, but is not an individual symptom-onset-to-discharge conversion. |
| [Protocol p.16, lines223–230](../../../joi180070supp1_prod.pdf#page=16) and [p.19, lines280–282](../../../joi180070supp1_prod.pdf#page=19) | PLAN: prospective clinical outcome and analysis specifications | Outcomes, telephone follow-up and Cox/Kaplan–Meier description use initial symptom onset for 3-, 6-, 12-month follow-up. These passages corroborate the report's onset wording and are not independent conflicting relationships. |
| [Main p.1, abstract vascular results](../../../jama_wang_2018_oi_180070.pdf#page=1) | REPORT: key secondary result summary | Vascular differences −2.03, −2.18 and −3.13 percentage points at 3, 6 and 12 months identify the key secondary extraction affected by the time-origin question. The abstract does not itself specify discharge versus onset. |

**Consistency rule applicable:** Yes. Route B applies to attribution of named key secondary results to different time origins: B1 time point and analysis/result mapping are in scope; B2 the same Table 3 outcome set is assigned to discharge and symptom onset without distinct analysis windows; B3 the time horizon used for extracting the vascular and related clinical effects differs according to which origin is taken. This is more than an interchangeable outcome name because the statement assigns a temporal origin to the same numeric results.

**Logical comparison reproduced:** A nominal follow-up time t measured after symptom onset is onset_i+t; a time t measured after discharge is discharge_i+t. Their difference is discharge_i−onset_i, which is patient-specific and not supplied. The report prints both origins for the same 3-, 6- and 12-month clinical-result descriptions without declaring separate windows. Median hospital stays cannot identify that difference for any patient, so no conversion or event-rate recomputation is made.

**Display-precision interval check:** Not applicable to the time-origin comparison: the dispute concerns a definition attached to named results, not a rounded numerical value. The printed 3/6/12-month labels agree in their nominal durations; permitting numeric half-unit intervals for those labels would not make symptom onset and discharge the same origin. No relative numerical discrepancy is claimed.

**Necessary inputs available:** Yes for the printed logical comparison: both origins, matching clinical outcomes/time points, Table 3 pointer, onset-based footnote and both figure axes/caption. **Exact missing inputs or definitions:** Individual onset, discharge, contact and event dates; nominal visit-window rules; whether discharge wording describes contact logistics or a separately analyzed window; and any declared mapping between onset-based and postdischarge follow-up. These are needed for outcome/date reanalysis, not reproduction of the source attribution conflict.

**Source-grounded alternative interpretation:** The Clinical Events wording may informally describe follow-up after hospitalization while all outcome windows actually use onset. Alternatively, clinical table summaries and survival figures may have distinct windows. Onset-based definitions, analyses, footnote and figure support the first possibility, but the package supplies no explicit distinction connecting the discharge sentence to those windows.

**Direct observation versus inferred explanation:** Direct observation is that the paragraph assigning Table 3 results uses discharge while their definitions and onset-labelled analyses/figure use symptom onset. An actual change in analysis dates, altered clinical event counts, or its quantitative effect would require additional inputs and is not inferred. The hospitalization medians are only context.

**Classification confirmation:** The conflicting locations are all **REPORT** within the same article. Primary relationship type **S_W**; all relationships **S_W**; review domain **report_internal_inconsistency** because the dispute is which time origin a reported result belongs to. The prospective protocol is **PLAN**, but only corroborates one report side; it does not add P_R. No classification correction is needed. **Classification ambiguity:** Informal discharge language or distinct windows may explain the attribution; neither is explicitly connected in the supplied content.

**Evidence state:** **reproduced**. Determining recheck fact: direct source p.5 assigns the Table 3 clinical results to months after discharge, while p.3/p.4 and p.8 retain onset-based outcome/analysis and disability/figure definitions. No transcription or location correction is required.

**Exact remaining human question:** Which time origin governs each Table 3 clinical result and the corresponding disability and survival analyses, and does the Results wording after discharge describe the same onset-based windows, contact logistics, or distinct follow-up windows?

## C004 — In-hospital mortality interval and P value

**Finding provenance:** F-NUM-002, F-XS-004, F-ST1-001.

**Location found; source value/text matched; comparator matched:** Yes for every row. Direct source rendering independently confirms the positive 0.2 endpoint and the separate alignment of the two P columns.

| Exact supplied-source location | Role by content | Directly confirmed content and comparison function |
|---|---|---|
| [Main p.8, Table 3 Death/In hospital row](../../../jama_wang_2018_oi_180070.pdf#page=8) | REPORT: mortality result display | 11/2400 (0.5%) intervention; 23/2400 (1.0%) control; absolute difference −0.7 percentage points, 95% CI −1.1 to positive 0.2; adjacent difference P=.009. The distinct HR column gives 0.96 (0.90–1.02), with its own rightmost P=.14. Every compared sign/value and column association is found. |
| [Main p.8, Table 3 heading and footnote a](../../../jama_wang_2018_oi_180070.pdf#page=8) | REPORT: effect/adjustment specification | Both effects have 95% CIs and adjustment for listed patient and hospital characteristics. The absolute difference is not labelled a crude count difference. |
| [Main p.4, Data Analysis confidence/significance rules](../../../jama_wang_2018_oi_180070.pdf#page=4) | REPORT: inferential rule | Comparative cumulative incidences and absolute differences have 95% CIs; P<.05 is statistically significant and all tests are two-sided. These provide the applicable null-exclusion levels. |
| [Main p.5, Clinical Events mortality sentence](../../../jama_wang_2018_oi_180070.pdf#page=5) | REPORT: contextual mortality interpretation | No significant difference in total mortality in hospital and at 3, 6 and 12 months is stated, with Figure 2B referenced. This may reflect HR-based inference; it is not substituted for the difference-column P value. |

**Consistency rule applicable:** Yes. Focus B, Route A category 1: an interval including the difference null while the paired P value is significant under the stated levels. No standard-error formula, crude comparison, identical CI/test implementation assumption, or symmetric-normal approximation is needed for this specified inclusion check. If separate CI/test constructions are intended, that is retained as an alternative interpretation.

**Calculation reproduced:** −1.1≤0≤+0.2, so the displayed 95% difference interval includes the null. The adjacent P=.009 is below .05 under the stated two-sided significance rule. Point containment and endpoint order themselves reconcile: −1.1<−0.7<+0.2. The separate HR interval includes 1 and its P=.14 is above .05, so those columns have a different, internally compatible null-exclusion reading and must not replace the difference's P=.009.

**Display-precision interval check:** Route A category 1 cannot be screened out as rounding. For an additional source-reading check, lower endpoint −1.1 has interval [−1.15,−1.05], upper endpoint +0.2 has [0.15,0.25], and P=.009 has [.0085,.0095]. Every admissible lower/upper pair still straddles zero and every admissible P remains below .05. Relative-gap calculations are not an applicable exclusion criterion for this interval-versus-test rule. No diagnostic recreation of an unstated inferential procedure is used to determine the evidence state.

**Necessary inputs available:** Yes for the reproduced interval/null/P comparison: confidence level, endpoints, paired P column, null value and significance/sidedness rules are supplied. **Exact missing inputs or definitions:** Difference-specific model specification and test/variance estimator, confidence-interval construction, any distinction between datasets or estimands used for the CI and P, cluster covariance/output, and patient-level analytic data. These prevent exact reanalysis of the adjusted result but do not prevent the printed null/P comparison.

**Source-grounded alternative interpretation:** The confidence interval and difference P may arise from distinct inferential procedures or analyses that the methods do not distinguish. The nonsignificant HR/P may explain the mortality narrative. Both are retained as possibilities; neither changes which P value is adjacent to the printed absolute-difference interval or removes the Route A category 1 record.

**Direct observation versus inferred explanation:** Direct observation is the positive CI upper limit and the adjacent P=.009, read from the actual source columns. The incompatible null-exclusion readings follow from the stated levels. A numeric production mechanism, intended endpoint sign, intended P, or preferred inferential method is not inferred, and no correction is proposed.

**Classification confirmation:** Every compared/contextual location is **REPORT** within one article. Primary relationship type **S_W**; all relationships **S_W**; review domain **statistical_results** because the issue is an adjusted estimate/interval/test pairing. No classification correction is needed. **Classification ambiguity:** None for role, relationship or domain; the CI/test construction remains unspecified.

**Evidence state:** **reproduced**. Determining recheck fact: exact-source visual confirmation of −1.1 to positive 0.2 and the adjacent P=.009 under 95%/two-sided P<.05 rules reproduces the interval/P conflict. No transcribed value, alignment or location correction is needed.

**Exact remaining human question:** Which analyses and inferential procedures produced the in-hospital mortality absolute-difference interval and P=.009, and how should a reader reconcile the interval's inclusion of zero with that P value?

## Recheck completion

Final field strings for coordinator transfer, with all location roles independently confirmed in the respective card tables:

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state |
|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R, S_C | PLAN protocol composite definition vs REPORT main composite definition; REPORT results supplement composite definition vs REPORT main composite definition | reproduced |
| C002 | statistical_results | S_W | S_W | REPORT main primary-analysis statement vs REPORT main Figure 1 primary-analysis counts and Table 2 denominators | reproduced |
| C003 | report_internal_inconsistency | S_W | S_W | REPORT main Clinical Events follow-up origin vs REPORT main outcome/method definitions and Table 3/Figure 2 time origins | reproduced |
| C004 | statistical_results | S_W | S_W | REPORT main Table 3 in-hospital death absolute-difference interval vs REPORT main paired P value and significance rule | reproduced |

Covered stable IDs: C001, C002, C003, C004. All four evidence states are reproduced; no source-value transcription correction or classification correction was required. All registered conflicting locations and repeated pattern occurrences were found and reread, including both flow arms, all three clinical follow-up time points, both Figure 2 axes, all three composite-definition locations and the Table 3 adjacent/separate P columns. Source roles and classification precedence were independently confirmed by content.

Unresolved items are the four exact human questions and the specifically named missing individual analytic data, weighting/score implementation, time-window definitions and CI/test construction. There is no exact-source location gap in this recheck scope. Ledger, screening, manifest and source assets were not edited by this specialist; the coordinator can copy these final classification/evidence fields into the ledger. All IDs remain Pending Human Adjudication.

# Appended pass-2 mechanical recheck

## C005 — Three-month vascular-death interval and P relationship

**Appended recheck provenance:** Runtime agent /root/recheck5; model gpt-6.1-sol; reasoning effort high; start mode FRESH_SPAWN. Assigned stable ID C005 only, including every affected location and all eleven supporting difference rows. Finding F-ST2-001; independent pass-2 screening INCLUDE. The complete QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read. This card records evidence facts; C005 remains **Pending Human Adjudication**.

**Location found; source value/text matched; comparator matched:** Yes for every location below and every tuple in the twelve-row calculation table. Exact supplied-source rendering controls signs, column pairing and display precision; extraction is a transcription aid. Direct CPU Poppler 25.03.0 extraction and fresh rendering of supplement pp.6–7 were used. The existing current-run direct-source main p.4 extraction and rendering were reread and visually inspected. No legacy scientific conclusions, web, OCR, unapproved Python, nested agents, source changes or reused-asset changes were used.

| Exact supplied-source location | Role by content | Source-confirmed content and comparison function |
|---|---|---|
| [Results supplement p.6, eTable 3, three-month vascular-death row](../../../joi180070supp2_prod.pdf#page=6) | REPORT: completed-trial secondary-outcome results | Intervention 46/2400 (1.9%); control 67/2400 (2.8%); adjusted absolute difference −1.43 percentage points, 95% CI −2.33 to −0.54; its immediately adjacent P is printed **0.001**. These are the registered compared values. The separate HR 0.62 (0.42–0.92) has its own P=.02; that separate P is not substituted for the difference P. |
| [Results supplement p.6, all eleven other eTable 3 absolute-difference rows](../../../joi180070supp2_prod.pdf#page=6) | REPORT: same completed-trial results display | Ischemic stroke, hemorrhagic stroke and myocardial infarction at 3, 6 and 12 months, plus vascular death at 6 and 12 months. Every estimate, endpoint and adjacent difference P is reproduced in the full numerical table below. These are comparator rows supporting the diagnostic relationship, not eleven additional registered inconsistencies. |
| [Results supplement p.7, eTable 3 footnote a](../../../joi180070supp2_prod.pdf#page=7) | REPORT: explanation of completed-trial adjusted results | Adjustment is for patient and hospital characteristics: age, gender, ischemic-stroke history, hypertension, diabetes, hyperlipidemia, atrial fibrillation, coronary disease/previous myocardial infarction, ever smoking, admission NIHSS, hospital grade, region, stroke unit, teaching status and neurological-ward beds. This confirms adjusted quantities and does not prescribe the difference-specific CI/test formula. Footnote * permits multiple types of new vascular event per patient; no disjoint-count assumption is used. |
| [Main p.4, Data Analysis](../../../jama_wang_2018_oi_180070.pdf#page=4) | REPORT: completed-trial analysis description | Comparative outcomes have adjusted cumulative incidences and absolute differences with 95% CIs. A P value less than .05 is significant; all tests are two-sided. Clinical vascular events/mortality are time-to-event outcomes, with multivariable Cox models described. The page does not name the absolute-difference CI/test construction, covariance estimator or a distinct construction for this row. This corroborates confidence level, sidedness and adjustment; it is not a conflicting cross-document value. |

**Consistency rule applicable:** Yes for a source-supported diagnostic under focus B and Route A, category 1. The two-sided normal-Wald relation is empirically supported by all eleven other absolute-difference rows of the same display after full half-unit input allowances. The method is labelled diagnostic because its exact use by the authors is not stated. The supplied scope treats a numerical interval/P conflict under a same-display supported relationship as registerable even when the undisclosed construction remains a human question. No crude count ratio is substituted for the adjusted difference. Both the printed CI and P indicate significance below .05; no significance reversal is claimed.

**Calculation or logical comparison reproduced:** Yes. With q=Φ⁻¹(.975)=1.959963984540054, use SE=(U−L)/(2q), z=|b|/SE, and diagnostic P=2Φ(−z). For b=−1.43, L=−2.33 and U=−0.54, central SE=0.456641043948, z=3.131562567477 and P=0.001738787319.

Normal tails were independently evaluated in JavaScript by composite Simpson integration of the standard-normal density from 0 to z using 20,000 subintervals. Repeating the decisive lower bound with 10,000 subintervals changed P by approximately 8.44×10⁻¹⁵. These calculations refine the checker's approximate normal-tail numbers and agree with the independently screened values; they do not recreate patient-level model estimation.

**Display-precision interval check:** Every displayed estimate and CI endpoint in these rows has two decimal places and receives ±.005. For C005:
- b∈[−1.435,−1.425], L∈[−2.335,−2.325], U∈[−0.545,−0.535].
- Independent attainable width U−L∈[1.780,1.800], SE∈[0.454089976663,0.459192111232], and |z|∈[3.103276308855,3.160166649230].
- Conservative independently varying input P envelope: [0.001576789229,0.001913908588].
- Printed 0.001 receives ±.0005, so its interval is [0.000500000000,0.001500000000].
- Minimum interval gap=0.000076789229; relative discrepancy=gap/0.001=0.076789228826>0.05. The two intervals do not overlap. Route A category 1 is not screened out as rounding; the explicit gap also exceeds the general display threshold.

A symmetric-Wald construction additionally requires b=(L+U)/2. To avoid claiming support merely from inconsistent independent choices, intersect the endpoint rectangle with 2b_low≤L+U≤2b_high. Evaluate the linear-fractional magnitude |q(L+U)/(U−L)| at all feasible rectangle vertices and intersections of each rectangle edge with both sum boundaries. This yields the centered C005 P envelope [0.001576789229,0.001777726117], still disjoint from the printed P interval. All eleven comparison rows retain overlap when this same centering constraint is applied.

**Complete same-display comparator calculation:** All source tuples below were directly matched to the fresh p.6 rendering and layout extraction. Actual printed P precision is retained: ischemic stroke at 3 months prints **0.40**, and hemorrhagic stroke at 12 months prints **0.80**, each with ±.005 rather than ±.05. The screen's rendered numerical tuples abbreviated them as 0.4 and 0.8, but its actual P intervals already used ±.005. Thus this table restores the true printed notation without changing C005's registered source values, comparator interval calculations or evidence state. The estimates −0.10, −1.40, −0.80 and 0.30 also retain their actual two-decimal display.

| Relationship; eTable 3 difference row | Printed b (L to U); paired P | Central diagnostic P | Independent-input P envelope | Printed P interval | Centered-Wald P envelope | Centered comparison |
|---|---|---:|---|---|---|---|
| S053; Ischemic stroke, 3 months | -0.57 (-1.91 to 0.76); 0.40 | 0.402683322 | [0.396798477, 0.408575678] | [0.395000000, 0.405000000] | [0.396798477, 0.402683322] | Overlap; gap 0 |
| S055; Hemorrhagic stroke, 3 months | -0.35 (-0.92 to 0.22); 0.23 | 0.228788052 | [0.218142721, 0.239603511] | [0.225000000, 0.235000000] | [0.222207459, 0.235506219] | Overlap; gap 0 |
| S057; Myocardial infarction, 3 months | -0.10 (-0.36 to 0.17); 0.48 | 0.459537248 | [0.428638325, 0.490435101] | [0.475000000, 0.485000000] | [0.459537248, 0.490435101] | Overlap; gap 0 |
| S059; Vascular death, 3 months | -1.43 (-2.33 to -0.54); 0.001 | 0.001738787 | [0.001576789, 0.001913909] | [0.000500000, 0.001500000] | [0.001576789, 0.001777726] | No overlap; gap 0.000076789 |
| S061; Ischemic stroke, 6 months | -1.40 (-2.82 to 0.02); 0.05 | 0.053315228 | [0.051641210, 0.055022111] | [0.045000000, 0.055000000] | [0.052469670, 0.054172138] | Overlap; gap 0 |
| S063; Hemorrhagic stroke, 6 months | -0.25 (-0.80 to 0.30); 0.38 | 0.372986726 | [0.359117819, 0.386923907] | [0.375000000, 0.385000000] | [0.363502921, 0.382622273] | Overlap; gap 0 |
| S065; Myocardial infarction, 6 months | -0.03 (-0.35 to 0.29); 0.86 | 0.854212231 | [0.827605378, 0.880159945] | [0.855000000, 0.865000000] | [0.830257707, 0.878301920] | Overlap; gap 0 |
| S067; Vascular death, 6 months | -1.06 (-2.08 to -0.04); 0.04 | 0.041667550 | [0.039733005, 0.043661214] | [0.035000000, 0.045000000] | [0.040671937, 0.042673706] | Overlap; gap 0 |
| S069; Ischemic stroke, 12 months | -1.84 (-3.45 to -0.23); 0.03 | 0.025093595 | [0.024256456, 0.025950216] | [0.025000000, 0.035000000] | [0.024644060, 0.025547363] | Overlap; gap 0 |
| S071; Hemorrhagic stroke, 12 months | -0.08 (-0.71 to 0.55); 0.80 | 0.803450268 | [0.789811729, 0.816932748] | [0.795000000, 0.805000000] | [0.791441212, 0.815505906] | Overlap; gap 0 |
| S073; Myocardial infarction, 12 months | -0.13 (-0.46 to 0.21); 0.45 | 0.446906154 | [0.422666664, 0.471171043] | [0.445000000, 0.455000000] | [0.446906154, 0.471171043] | Overlap; gap 0 |
| S075; Vascular death, 12 months | -1.94 (-3.26 to -0.62); 0.004 | 0.003969780 | [0.003744049, 0.004205958] | [0.003500000, 0.004500000] | [0.003834005, 0.004108833] | Overlap; gap 0 |

For each of the eleven comparison rows the independent-input and centered intervals overlap the printed P interval, hence the discrepancy and relative discrepancy are both zero. For S059/C005 both constructions have the same lower bound and the positive gap reported above. Rounded central values alone do not establish compatibility for several comparison rows; their half-unit input envelopes are essential.

**Necessary inputs available:** Yes for direct-source tuple matching and the supported diagnostic: all twelve adjusted absolute-difference/95%-CI/P tuples, printed decimal precision, 95% confidence level, two-sided tests, adjustment context and exact column pairing are supplied. The complete same-display comparison is available and reproduced.

**Exact missing inputs or definitions:** The actual difference-specific confidence-interval formula, paired P-value test and null statistic, whether CI and P use the same variance estimator/estimand/model dataset, model covariance and unrounded output, and patient-level event/censoring times with covariate/cluster records. These prevent asserting the authors' construction or recreating the fitted adjusted estimates. They do not prevent reproducing the displayed tuple and diagnostic mismatch supported by the other rows.

**Source-grounded alternative interpretation:** The P may derive from a test, variance estimator, confidence construction, dataset or estimand distinct from the displayed difference interval. The source's adjusted time-to-event and Cox context supports the possibility of several inferential procedures, while the separate HR/P pair visibly supplies a distinct contrast. No row-specific difference procedure is identified, and the HR P=.02 is not the printed P adjacent to the difference. An alternative method could explain the tuple, but its identity and linkage are not supplied. No intended replacement value or preferred analysis is proposed.

**Direct observation versus inferred explanation:** Direct observation is the p.6 tuple −1.43 (−2.33 to −0.54) with adjacent 0.001, the eleven supporting tuples, and the p.7/main p.4 context. The calculated fact is disjoint diagnostic versus printed P intervals under the empirically supported normal-Wald relation, including exact symmetric centering. That this relation was actually used by the authors, that a different dataset was used, or how the printed tuple was produced are explanations requiring evidence; none is asserted. The extracted numerical P and its relationship to the adjusted difference's inferential precision are affected, while the displayed significance conclusion is unchanged.

**Classification confirmation:** All source and comparator locations are **REPORT** by their completed-trial content. Primary relationship type **S_W**; all relationships **S_W**; review domain **statistical_results**. The conflicting tuple and all supporting difference rows lie within one results supplement; this is an estimate/interval/test issue. Main p.4 merely corroborates inference conventions and p.7 merely explains adjustment. Neither adds a conflicting S_C relationship. No PLAN content is compared, so P_R/P_P are absent. S_W is therefore the highest and only applicable relationship under precedence P_R > P_P > S_C > S_W. No classification correction is needed. **Classification ambiguity:** None for source roles, relationship or domain; the actual inference construction remains unresolved.

**Evidence state:** **reproduced**. Determining recheck fact: direct current-PDF rendering and extraction confirm C005's registered tuple and pairing; the independently reproduced normal-Wald P envelope remains above the printed P interval with relative gap 0.076789228826, while all eleven support rows overlap under the same calculation. No registered C005 value or source location required transcription correction. Restoring trailing zeros in the support-screen presentation is transparently documented above and does not change the already-correct half-unit arithmetic.

**Exact remaining human question:** Which difference-specific confidence-interval and testing procedures produced −1.43 (95% CI −2.33 to −0.54) with P=0.001 for three-month vascular death, and how does that pairing reconcile with the two-sided normal-Wald relationship supported by all eleven other absolute-difference rows of eTable 3?

### C005 derivative provenance

Compute device CPU, as recorded in tooling_record.md. Source PDFs and every pre-existing derivative remain unchanged. The four uniquely named new derivatives below were generated directly from supplied supplement pages; both PNGs were visually inspected. Main p.4 derivatives were generated earlier in this same workflow by /root/recheck; both were reread here, with the PNG visually inspected.

| Supplied source | Physical PDF page | Derivative below preprocessing/ | Engine | Version | Device | Operation |
|---|---:|---|---|---|---|---|
| joi180070supp2_prod.pdf | 6 | recheck5-supp-p6.txt | pdftotext, Poppler | 25.03.0 | CPU | Fresh direct layout extraction |
| joi180070supp2_prod.pdf | 6 | recheck5-supp-p6.png | pdftoppm, Poppler | 25.03.0 | CPU | Fresh direct rendering, 150 dpi |
| joi180070supp2_prod.pdf | 7 | recheck5-supp-p7.txt | pdftotext, Poppler | 25.03.0 | CPU | Fresh direct layout extraction |
| joi180070supp2_prod.pdf | 7 | recheck5-supp-p7.png | pdftoppm, Poppler | 25.03.0 | CPU | Fresh direct rendering, 150 dpi |
| jama_wang_2018_oi_180070.pdf | 4 | recheck-main-p4.txt | pdftotext, Poppler | 25.03.0 | CPU | Existing current-run direct layout extraction, reread |
| jama_wang_2018_oi_180070.pdf | 4 | recheck-main-p4.png | pdftoppm, Poppler | 25.03.0 | CPU | Existing current-run direct rendering, 120 dpi, visually inspected |

Fresh commands, separately instantiated for N=6 and N=7:
```text
pdftotext -layout -f N -l N joi180070supp2_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/recheck5-supp-pN.txt
pdftoppm -f N -l N -singlefile -r 150 -png joi180070supp2_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/recheck5-supp-pN
```
Both engines report version 25.03.0. All four extraction/render commands completed with exit code 0. No OCR or fallback capability was needed. Derivative limits: none affecting transcription; actual model data and difference-specific constructions remain unavailable as named above. The standalone part uses source-link prefix ../../../../; this canonical merge uses ../../../, relative to verification/evidence_recheck.md.


Final mechanical coverage is C001, C002, C003, C004, C005, all reproduced; the appended record is part of this canonical artifact. The earlier four-ID completion table is the initial-stage transfer record.
