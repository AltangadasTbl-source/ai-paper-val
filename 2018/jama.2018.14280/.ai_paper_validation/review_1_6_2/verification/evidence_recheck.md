# Mechanical evidence recheck — Workflow 1.6.2

Pending Human Adjudication. This fresh recheck covers exactly C001, C002, C003, C004, C005, C006, C007, C008, and C009. It records evidence facts and classification fields, without a disposition. Every registered affected location is addressed below. C006 includes four clinical primary-VFD analysis families; its ancillary economic comparison is outside the assigned registered scope.

The authority is the supplied PDF, not a previous checker, OCR, map, or extracted table. Exact physical PDF pages were independently read through fresh direct native/layout extraction. Source page images were independently rendered and inspected for the numeric Table 2, the two ambiguous supplementary tables, the change-matrix continuation, and the image-bearing report figures needed for the nonreporting check. All derivatives are below preprocessing, use direct Poppler 25.03.0 on CPU, and do not alter sources or reused assets. Native text was usable; no OCR or fallback environment was used. PDF page numbers below are physical pages, not printed journal or protocol pagination. Evidence links are relative to this verification directory.

## Classification and evidence-state summary

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Recheck fact determining the state |
|---|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT main abstract, methods, and Table 2 | reproduced | Source RR labels and two event-risk calculations retain interval gaps with relative discrepancy above 0.05. |
| C002 | protocol_report | P_R | P_R, P_P | PLAN protocol endpoint, ascertainment item, Berlin appendix, and SAP endpoint versus REPORT new-ARDS result | reproduced | Restricted moderate/severe prospective collection contrasts with generic ARDS endpoint/report wording linked to all-grade Berlin criteria; the event-grade definition remains unresolved. |
| C003 | protocol_report | P_R | P_R, P_P | PLAN original protocol versus PLAN updated SAP and REPORT eligibility | reproduced | The explicit low-oxygenation/direct-risk-factor exception is present only in the original list. |
| C004 | protocol_report | P_R | P_R | PLAN protocol endpoint versus REPORT endpoint; PLAN SAP contextual | reproduced | Three original-plan ICU-admission anchors contrast with the explicit report randomization anchor. |
| C005 | protocol_report | P_R | P_R, P_P | PLAN original protocol versus PLAN prospective updated SAP and REPORT primary analysis | reproduced | Original primary Cox specification is replaced by updated-SAP and reported t-test specification; the replacement is explicitly disclosed. |
| C006 | protocol_report | P_R | P_R | PLAN clinical primary-analysis specifications and change annotations versus REPORT supplied analysis/results | reproduced | The four planned clinical-primary-analysis families have no identifiable supplied REPORT result; three omissions are explicitly described in the matrix. |
| C007 | protocol_report | P_R | P_R | PLAN updated-SAP subgroup model versus REPORT methods and subgroup results; matrix contextual | reproduced | Updated SAP specifies zero-inflated subgroup models and report specifies Gaussian, with post-hoc change disclosure. |
| C008 | statistical_results | S_W | S_W | REPORT eTable 2 cell versus REPORT table summary definition | reproduced | Visually confirmed 8 (5–1) cannot satisfy quartile order or median containment after half-unit allowances. |
| C009 | report_internal_inconsistency | S_W | S_W | REPORT eTable 5 subgroup labels versus REPORT numerical row positions; main methods contextual | reproduced | The first numeric line aligns with a wrapped heading, second with >6 hours, and ≤6 hours has no numeric line. |

The sole classification change is C006: remove P_P from All relationships. The matrix is the plan-comparison/change annotation attached to the SAP; its “IN THE PAPER” descriptions do not prescribe an opposing prospective plan. The respiratory-rate entry describes claimed reporting, whereas the prospective subgroup specification also includes respiratory rate. Those PLAN locations therefore do not conflict with each other about the planned subgroup. Their comparison with the actual REPORT remains P_R. The matrix's reporting annotation is not an independent plan-to-plan relationship. No evidence-state change is implied by this classification change. All other provisional classifications are retained for the reasons below. No transcribed number or physical source page required amendment; all nine states are reproduced.

## C001 — Binary risk-ratio identity requires clarification

**Location found:** Yes, at [main PDF p1, abstract adverse events](../../../jama_simonis_2018_oi_180108.pdf#page=1), [p4, Statistical Analysis, secondary binary outcomes](../../../jama_simonis_2018_oi_180108.pdf#page=4), and [p6, Table 2, all ten RR rows and footnote c](../../../jama_simonis_2018_oi_180108.pdf#page=6). The p6 rendering independently confirms every cell below. The p1 ARDS counterpart is 3.8% versus 5.0%, RR 0.86 (0.59–1.24), P=.38. It matches the p6 copy. The abstract also repeats pneumonia, atelectasis, and pneumothorax estimates consistently with p6.

**Source value/text matched:** Yes. Table 2 uses “RR” and footnote c defines the estimate as risk ratio, with 95% intervals calculated with the Wald likelihood ratio approximation test and P values with chi-square tests. The p4 method independently describes risk ratio and these interval/test procedures. No modeled binary-effect adjustment or alternative conditioning variable is identified for these rows.

**Comparator matched and every affected row:** Yes. The table supplies the following event counts, denominators, estimates, intervals, and P values. Columns list low then intermediate arms.

| Table 2 RR row | Events/denominator | Printed RR (95% CI), P | Event-risk RR from exact printed fractions | Recomputed half-unit RR interval | Printed half-unit RR interval | Interval gap / printed RR |
|---|---|---|---:|---|---|---:|
| ICU mortality | 132/450; 115/458 | 1.11 (0.96–1.27), .15 | 1.1682318841 | [1.1562189198, 1.1803750893] | [1.105, 1.115] | 0.0371341620 |
| Hospital mortality | 151/477; 140/484 | 1.06 (0.93–1.22), .35 | 1.0943995208 | [1.0846341600, 1.1042548150] | [1.055, 1.065] | 0.0185227924 |
| ARDS | 17/448; 23/462 | 0.86 (0.59–1.24), .38 | 0.7622282609 | [0.7224791859, 0.8038485413] | [0.855, 0.865] | 0.0594784404 |
| Pneumonia | 19/450; 17/462 | 1.07 (0.78–1.47), .67 | 1.1474509804 | [1.0829554463, 1.2159975731] | [1.065, 1.075] | 0.0074349966 |
| Pneumothorax | 8/448; 6/462 | 1.16 (0.73–1.84), .55 | 1.3750000000 | [1.1872909699, 1.5972574911] | [1.155, 1.165] | 0.0192163534 |
| Atelectasis | 51/449; 52/464 | 1.00 (0.81–1.23), .94 | 1.0135343498 | [0.9918639758, 1.0356744705] | [0.995, 1.005] | 0 |
| Extrapulmonary infection | 20/448; 28/463 | 0.84 (0.60–1.18), .28 | 0.7382015306 | [0.7055682685, 0.7721076689] | [0.835, 0.845] | 0.0748718228 |
| Extrapulmonary sepsis | 12/448; 16/463 | 0.87 (0.56–1.33), .50 | 0.7751116071 | [0.7187257187, 0.8352856371] | [0.865, 0.875] | 0.0341544402 |
| Delirium | 149/343; 132/361 | 1.15 (0.99–1.34), .06 | 1.1880245605 | [1.1762214715, 1.1999500430] | [1.145, 1.155] | 0.0184534535 |
| Need for tracheostomy | 54/477; 52/484 | 1.03 (0.84–1.26), .78 | 1.0537010160 | [1.0318524059, 1.0760195194] | [1.025, 1.035] | 0 |

**Consistency rule applicable:** Yes, the quantitative effect-measure identity under focus C and Route B, with the prescribed display-precision rule. The ten-row scope is the shared label/method pattern; only ARDS and extrapulmonary infection independently exceed the point-estimate threshold. A modeled effect must not automatically be equated with a crude ratio. This recheck grounds the question in the source's event-risk RR label and unqualified binary-outcome method rather than asserting that all adjusted estimates must equal printed fractions. No separate interval-versus-P conflict is claimed here.

**Calculation and display-precision check reproduced:** Yes. For low-arm a/n and intermediate c/m, the event-risk ratio is a*m/(n*c). Apply ±0.5 to each printed integer input as required by the review rule: the lower bound is (a−0.5)(m−0.5)/[(n+0.5)(c+0.5)], and the upper bound is (a+0.5)(m+0.5)/[(n−0.5)(c−0.5)]. Printed two-decimal RRs allow ±0.005. ARDS gap is 0.855−0.8038485413=0.0511514587, divided by 0.86 gives 0.0594784404. Infection gap is 0.835−0.7721076689=0.0628923311, divided by 0.84 gives 0.0748718228. Both exceed 0.05. All eight other rows have relative discrepancy at most 0.05, as independently calculated above. ARDS percentages from exact fractions are 3.794642857% and 4.978354978%; infection percentages are 4.464285714% and 6.047516199%. These fall inside their displayed one-decimal intervals [3.75,3.85], [4.95,5.05], [4.45,4.55], and [5.95,6.05]. There is no percentage inconsistency in these two rows. The two ARDS RR copies have identical [0.855,0.865] intervals and zero gap.

**Necessary inputs available:** Yes for the event-risk calculation and half-unit check, for every row. **Exact missing inputs or definitions:** The estimand's conditioning variable; any binary-outcome model, standardization, adjustment or stratification; the precise interval construction; and code/output showing how these displayed RRs were produced. Those inputs are necessary to decide the producing estimator, not to reproduce the printed identity question.

**Source-grounded alternative interpretation:** The article elsewhere reports explicit models for time-to-event mortality, length of stay, and subgroup analyses, so an undisclosed modeled/standardized binary estimand remains possible; no such model is selected as fact. A diagnostic calculation using the same printed counts, [a/(a+c)]/[(n−a)/(n+m−a−c)], yields 0.8578886311 for ARDS and 0.8401479751 for infection, close to the printed RRs, but it conditions allocation on event status and is not the reported event-risk definition. Numerical proximity cannot establish the authors' procedure. Cox time-to-event results concern separately labeled HR rows and do not supply this binary estimand.

**Direct observation versus inferred explanation:** Direct: labels, counts, printed estimates, method language and precision gaps. Inference: reverse conditioning or an undisclosed model as the production mechanism. No mechanism is established.

**Document roles and classification:** All opposing locations are REPORT content within one article. Primary S_W; All relationships S_W; domain statistical_results. PLAN risk-ratio wording would corroborate the report method and does not add P_R. No classification amendment is needed. Ambiguity: the producing binary estimand is not fully specified.

**Evidence state:** reproduced. **Determining recheck fact:** Two independently recalculated event-risk RRs retain relative interval gaps above 0.05 against the source's printed risk-ratio identity.

**Exact remaining human question:** Which conditioning variable, estimand and estimator produced the Table 2 binary RRs, especially ARDS 0.86 and extrapulmonary infection 0.84, and how do those estimands relate to the printed arm-specific event fractions?

## C002 — ARDS severity threshold is unresolved across plan and report

**Location found:** Yes, every registered occurrence: [protocol p26, secondary endpoints](../../../joi180108supp1_prod.pdf#page=26); [protocol p28, daily pulmonary-complication collection](../../../joi180108supp1_prod.pdf#page=28); [protocol p48, Berlin appendix](../../../joi180108supp1_prod.pdf#page=48); [SAP p9, secondary outcomes](../../../joi180108supp2_prod.pdf#page=9); [main p1, abstract adverse events](../../../jama_simonis_2018_oi_180108.pdf#page=1); [main p4, Outcomes](../../../jama_simonis_2018_oi_180108.pdf#page=4); and [main p6, Table 2 ARDS](../../../jama_simonis_2018_oi_180108.pdf#page=6).

**Source value/text matched:** Yes. The daily prospective collection item specifies moderate or severe ARDS (yes/no). **Comparator matched:** Yes. The protocol endpoint is development of ARDS linked to Appendix I, the SAP says development of new ARDS, and the report says development of new ARDS with the Berlin reference. The supplied Berlin table includes mild 200<PaO2/FiO2≤300, moderate 100<PaO2/FiO2≤200, and severe PaO2/FiO2≤100, with the other diagnostic/PEEP requirements. The reported event result is 17/448 (3.8%) versus 23/462 (5.0%), RR 0.86 (0.59–1.24), P=.38, appearing in the abstract and Table 2.

**Consistency rule applicable:** Yes, an outcome-definition comparison tied to an abstract key-secondary result under focus D and Route B. **Logical comparison reproduced:** Yes, the prospective ascertainment item restricts the grade, while the endpoint/criteria/report language does not tell whether mild cases are included. A patient meeting the other Berlin criteria with PaO2/FiO2=250 distinguishes all-grade ascertainment from moderate/severe ascertainment. This establishes non-equivalent possible case sets, not that a mild case actually contributed to the counts. **Display-precision interval check:** Not applicable to fixed diagnostic cutpoints or categorical grade restrictions; half-unit allowances cannot choose an ascertainment definition. The p1/p6 numeric copies match, with zero gap for the RR and percentages; their equality does not resolve case definition.

**Necessary inputs available:** Yes for identifying the printed restricted and generic specifications. **Exact missing inputs or definitions:** Event-grade ascertainment rule used for the 40 reported new cases; counts by mild/moderate/severe grade; and any amendment clarifying collection of mild ARDS. Individual diagnostic data are not required for this textual recheck.

**Source-grounded alternative interpretation:** “New ARDS” may be shorthand for new moderate/severe ARDS consistent with the collection item. Alternatively, the later endpoint could include all Berlin grades. Neither is established by the supplied result language.

**Direct observation versus inferred explanation:** Direct: grade-restricted collection and generic endpoint/result labels with an all-grade appendix. Inference: whether the operational endpoint broadened, or whether the clinical labels abbreviate a restriction. No case misclassification is asserted.

**Document roles and classification:** Protocol endpoint/collection/appendix and prospective SAP outcome are PLAN; article abstract/methods/results are REPORT. Primary P_R; All relationships P_R, P_P; domain protocol_report. P_P remains because the explicit original-plan collection restriction and generic original-plan endpoint/appendix leave the same planned case-set definition unresolved within PLAN material; it is not added merely because a plan corroborates the report. P_R has precedence. Classification ambiguity: the generic specification may implicitly retain the moderate/severe collection restriction.

**Evidence state:** reproduced. **Determining recheck fact:** The original moderate/severe collection wording is source-matched, while the generic planned/reported endpoint does not resolve which grade-defined event set generated the abstract result.

**Exact remaining human question:** Did the reported 17 and 23 new-ARDS cases include mild Berlin ARDS, or only moderate/severe cases, and which supplied plan statement or amendment governed that ascertainment?

## C003 — Low-oxygenation eligibility condition differs between supplied lists

**Location found:** Yes, [protocol p17, exclusions](../../../joi180108supp1_prod.pdf#page=17) and [p18, explanatory low-oxygenation exception](../../../joi180108supp1_prod.pdf#page=18); [SAP p6, eligibility and inclusion](../../../joi180108supp2_prod.pdf#page=6) and [p7, exclusions](../../../joi180108supp2_prod.pdf#page=7); [main p2, Patients](../../../jama_simonis_2018_oi_180108.pdf#page=2); and corroborating [main p5, Table 1 oxygenation](../../../jama_simonis_2018_oi_180108.pdf#page=5) and [results supplement p9, oxygenation subgroup](../../../joi180108supp3_prod.pdf#page=9).

**Source value/text matched:** Yes. The original list excludes clinical ARDS or possible ARDS with PaO2/FiO2<200; the following insert permits a patient below 200 only when the attending explicitly states no ARDS and no direct ARDS risk factor is present. **Comparator matched:** Yes. SAP p7 lists clinical Berlin ARDS as the exclusion and lacks that added low-oxygenation exception/condition. Main p2 lists ARDS strictly following the Berlin definition and says included lungs need not be healthy or uninjured, without the added condition. Main Table 1 oxygenation medians are 197 (127–298) and 195 (133–300). eTable 5 displays ≤200/>200 subgroups with mean differences −0.87 (−3.21 to 1.47) and 0.87 (−1.62 to 3.36), interaction P=.32.

**Consistency rule applicable:** Yes, a population-defining planned-versus-reported rule under focus D/Route B, tied to the primary-outcome population and oxygenation subgroups. **Logical comparison reproduced:** Yes. A patient with PaO2/FiO2=150, no clinical Berlin ARDS, and a direct risk factor fails the original exception but is not excluded on that additional basis by the later printed lists. This is a difference in stated rule sets, not proof that such a patient was randomized. **Display-precision interval check:** Not applicable to the fixed eligibility threshold and Boolean condition. The baseline medians and subgroup effects are corroborating applicability evidence, not copies claimed to conflict; their half-unit intervals cannot recover eligibility criteria.

**Necessary inputs available:** Yes for the rule-set comparison. **Exact missing inputs or definitions:** Governing eligibility version and effective date; whether the attending/no-direct-risk-factor exception remained operational; and any amendment explicitly removing it. Participant-level risk-factor cross-classification is absent, so no effect on randomized totals is calculated.

**Source-grounded alternative interpretation:** The detailed condition may have remained operational while omitted from later summaries; alternatively the updated SAP/report may reflect an amended rule. Both are compatible with the supplied descriptions.

**Direct observation versus inferred explanation:** Direct: the extra original criterion and its absence from complete later eligibility lists. Inference: operational removal, continued application, or a changed number of eligible patients. None is established.

**Document roles and classification:** Original protocol and prospective updated-SAP eligibility sections are PLAN; article eligibility, baseline results and eTable 5 are REPORT. Primary P_R; All relationships P_R, P_P; domain protocol_report. P_P compares two actual eligibility specifications, not corroboration. Main p5 and supplement p9 do not oppose one another and create no S_C. P_R has precedence. Classification ambiguity: amendment versus abbreviated restatement.

**Evidence state:** reproduced. **Determining recheck fact:** The source-confirmed original extra exclusion condition is absent from the source-confirmed later PLAN and REPORT lists.

**Exact remaining human question:** Which rule governed patients below PaO2/FiO2 200 with a direct ARDS risk factor but without clinical ARDS, and was the original attending/no-direct-risk-factor exception retained or prospectively amended?

## C004 — Primary ventilator-free-day time origin differs

**Location found:** Yes at all three repeated original-plan anchors: [protocol p10, summary](../../../joi180108supp1_prod.pdf#page=10), [p19, power endpoint](../../../joi180108supp1_prod.pdf#page=19), and [p33, primary analysis](../../../joi180108supp1_prod.pdf#page=33); contextual [SAP p8, primary definition](../../../joi180108supp2_prod.pdf#page=8); and REPORT [main p4, primary definition](../../../jama_simonis_2018_oi_180108.pdf#page=4), [p5, timing](../../../jama_simonis_2018_oi_180108.pdf#page=5), and [p6, Table 2 primary result](../../../jama_simonis_2018_oi_180108.pdf#page=6).

**Source value/text matched:** Yes, each of the three original occurrences says day 28 after ICU admission. **Comparator matched:** Yes, the report explicitly calculates the primary VFD outcome from the moment of randomization. SAP p8 says day 1 to day 28 without explicitly naming its origin. The report gives ventilation-start-to-randomization median 0.88 hours (0.36–2.01), and ventilation-in-ICU-start-to-randomization 0.57 hours (0.23–1.00). Neither is ICU-admission-to-randomization. Table 2 gives primary mean difference −0.27 (−1.74 to 1.19), P=.71, with 475/480 observed primary outcomes.

**Consistency rule applicable:** Yes, primary endpoint-window specification under focus D/Route B. **Logical comparison reproduced:** Yes, ICU admission and randomization are distinct named origin events. No equality of their timestamps is supplied. The day-1 language alone does not select either anchor. **Display-precision interval check:** Not applicable to different named events. The 0.57-hour median interval [0.565,0.575] is not an interval for the missing admission-to-randomization delay and cannot resolve the comparison. The p1/p6 primary mean-difference copies match [−0.275,−0.265] with zero gap. This candidate claims no numerical conflict in that mean difference or P value.

**Necessary inputs available:** Yes for the explicit-origin comparison. **Exact missing inputs or definitions:** Governing VFD origin definition or amendment, actual admission-to-randomization timing, and whether all VFD windows used the same origin. Patient-level recalculation is not possible and not attempted.

**Source-grounded alternative interpretation:** The later day-1 SAP wording may have intended randomization; the protocol's admission language may have been shorthand for near-coincident events. The report's timing and limitations describe a short intended randomization window but do not establish admission/randomization identity or disclose this particular origin amendment.

**Direct observation versus inferred explanation:** Direct: three admission anchors and one randomization anchor. Inference: actual magnitude or clinical consequence of changing origins. No changed primary estimate is asserted.

**Document roles and classification:** Protocol/SAP specifications are PLAN; article definition, timing and result are REPORT. Primary P_R; All relationships P_R; domain protocol_report. The SAP has no opposing explicit origin and provides context, not an extra P_P relationship. Classification ambiguity: unspecified SAP day-1 origin and possible shorthand/amendment.

**Evidence state:** reproduced. **Determining recheck fact:** The direct-source origin events differ exactly as registered, and the SAP does not explicitly reconcile them.

**Exact remaining human question:** Was the analyzed 28-day VFD window anchored to ICU admission or randomization, and which documented definition or amendment governed that origin?

## C005 — Original primary Cox analysis is replaced by a t-test analysis

**Location found:** Yes, [protocol p19, t-test power inputs](../../../joi180108supp1_prod.pdf#page=19), [protocol p33, primary Cox analysis](../../../joi180108supp1_prod.pdf#page=33), [SAP p12, primary t-test analysis](../../../joi180108supp2_prod.pdf#page=12), [SAP p21, original/update/paper primary row](../../../joi180108supp2_prod.pdf#page=21), [main p2, updated-plan disclosure](../../../jama_simonis_2018_oi_180108.pdf#page=2), [main p4, primary method](../../../jama_simonis_2018_oi_180108.pdf#page=4), and [main p6, Table 2 primary estimate and footnote a](../../../jama_simonis_2018_oi_180108.pdf#page=6). The database-lock/post-hoc footnotes continuing on [SAP p22](../../../joi180108supp2_prod.pdf#page=22) are also confirmed.

**Source value/text matched:** Yes. Original primary VFD analysis uses Cox regression and models possible imbalance. Original power inputs are a two-group t test, means 23/24, common SD 5, two-sided .05, power 80%, n=397 per arm before 20% increase to 476. **Comparator matched:** Yes. Updated SAP specifies Student's t test with mean difference; report specifies t tests and 95% CIs for superiority. Table 2 reports −0.27 (−1.74 to 1.19), P=.71, and footnote a identifies the primary t test. Matrix primary row labels original Cox, updated t test, paper t test, and post-hoc “None.” Its headings/footnotes give SAP closure November 24, 2017 and database locking December 30, 2017. The article says the updated SAP was written before closing the database.

**Consistency rule applicable:** Yes, originally planned primary analysis replaced in the supplied report, Route A category 5. **Logical comparison reproduced:** Yes. The two stated primary models differ. The updated prospective model and reported model agree; the discrepancy is with the original specified model. Full main/report-supplement text and result displays identify no primary-VFD Cox result. Figure 2's time-to-liberation hazard ratio concerns a different stated time-to-event analysis and does not instantiate the original primary VFD Cox specification. **Display-precision interval check:** Not applicable to categorical model identity. Mean-difference copies are identical within [−0.275,−0.265], with zero gap. The power paragraph is context; no independent power calculation failure is asserted.

**Necessary inputs available:** Yes for the specification/replacement comparison and explicit timing disclosure. **Exact missing inputs or definitions:** Whether the original primary Cox analysis was performed and where its output can be found, or confirmation that the updated SAP formally superseded that primary specification. The supplied dates cannot establish undisclosed access to outcome results or amendment procedures, and no such inference is made.

**Source-grounded alternative interpretation:** The pre-lock updated SAP may be the authorized governing amendment. That explicit disclosure is retained and explains prospective versus post-hoc status; it does not change the observation that the originally specified primary analysis was replaced. The report's Cox results apply to other outcomes.

**Direct observation versus inferred explanation:** Direct: original Cox, later t test, corresponding reported mean difference, and pre-lock disclosure. Inference: why replacement occurred or whether it changed the result. No motive or result change is asserted.

**Document roles and classification:** Original protocol and updated prospective SAP specifications are PLAN; article methods/results are REPORT. Matrix is PLAN comparison/change context. Primary P_R; All relationships P_R, P_P; domain protocol_report. P_P is supported by the actual original-versus-updated prospective model specifications, including a disclosed change, rather than by the matrix's retrospective paper description. P_R has precedence. T-test power versus Cox-analysis wording does not independently demonstrate an unreproduced power value and is contextual. Classification ambiguity: the prospective governing-SAP replacement is explicitly disclosed.

**Evidence state:** reproduced. **Determining recheck fact:** Direct-source original primary Cox and updated/reported t-test specifications differ, with no supplied primary-VFD Cox result.

**Exact remaining human question:** Did the November 24 updated SAP formally supersede the original primary-VFD Cox specification, and was the originally specified Cox analysis performed or reported elsewhere in supplied material?

## C006 — Four planned clinical primary-outcome analysis families lack supplied results

**Location found:** Yes for every registered PLAN location: [protocol p33, per-protocol promise](../../../joi180108supp1_prod.pdf#page=33); [SAP p13, first per-protocol exclusions](../../../joi180108supp2_prod.pdf#page=13), [p14, continued exclusions, nine subgroups and sensitivity](../../../joi180108supp2_prod.pdf#page=14), [p15, covariates and mediation](../../../joi180108supp2_prod.pdf#page=15), [p21, matrix additional/subgroup rows](../../../joi180108supp2_prod.pdf#page=21), and [p22, continuation/per-protocol/mediation](../../../joi180108supp2_prod.pdf#page=22). REPORT comparators found: [main p4, complete methods and subgroup list](../../../jama_simonis_2018_oi_180108.pdf#page=4), [p6, primary sensitivity and subgroup narrative](../../../jama_simonis_2018_oi_180108.pdf#page=6), and [results supplement p9, complete eTable 5](../../../joi180108supp3_prod.pdf#page=9). Nonreporting is a package search fact, not a fabricated absent-result page: all 9 main pages and all 13 results-supplement pages were searched/read for the families; main p7 and supplement pp10–13 image figures were also directly rendered and inspected. Supplement contents/eMethods/eTables/eFigures contain no result under the missing families. The one-page supplied data-sharing statement does not contain analysis results.

**Source value/text matched and comparator matched:** Yes, each constituent is separately confirmed.

| Clinical primary-VFD family | Exact supplied PLAN specification | Matched REPORT comparator and matrix context |
|---|---|---|
| Per-protocol | Protocol p33 promises per-protocol analysis; SAP pp13–14 define low-arm >6 and high-arm <8 mL/kg PBW first-two-day exclusion rules with the described tolerance/asynchrony/acidosis and pressure boundaries. | Main p4 reports complete-case analysis, main p6/Table 2 primary result and random-stratification sensitivity; no per-protocol primary effect, interval, P value or population size is identified. SAP p22 matrix says per-protocol analyses “Not described” in paper. |
| Covariate-adjusted zero-inflated sensitivity | SAP pp14–15 explicitly re-estimates primary outcome by zero-inflated GLM adjusted for baseline age, LIPS, SAPS II and PaO2/FiO2; it separately specifies a center/intubation-location random-effects GLMM. | Main p4/p6 sensitivity is the stratification-random-effects model, P=.72, not the four-covariate GLM. Matrix p21 explicitly says covariate GLM not reported. No four-covariate primary effect/interval/test is supplied. |
| Respiratory-rate subgroup | SAP p14 ninth primary-VFD subgroup is high versus low respiratory rate based on first-two-day median; matrix pp21–22 carries respiratory rate in the updated and in-paper subgroup lists. | Main p4 lists eight categories and eTable 5 p9 contains exactly those eight pairs: pneumonia, sepsis, oxygenation, LIPS, admission reason, SAPS II, prior ventilation and intubation location. No respiratory-rate pair or interaction is supplied. Respiratory-rate descriptive rows elsewhere are ventilation measurements, not VFD subgroup effects. |
| Mechanical-power mediation | SAP p15 explicitly assesses mediation of randomized treatment effects on VFD by mechanical power, deriving driving pressure from PEEP/plateau pressure and flow from respiratory rate, I:E ratio and tidal volume. | Main text/eTables/eFigures contain no mediation effect, coefficient or test; SAP p22 matrix's Other row contrasts planned mediation with paper “None.” Driving-pressure and respiratory-rate descriptive displays do not report mediation of VFD. |

**Consistency rule applicable:** Yes, planned clinical primary-outcome analyses absent from the supplied REPORT, Route A category 5. The sensitivity/exploratory labeling does not change that each explicitly estimates or analyzes the clinical primary VFD outcome. The separately deferred ancillary cost-effectiveness comparison is not one of these four constituents.

**Logical comparison reproduced:** Yes. The printed plan promises/specifications are present; no matching supplied REPORT result is found after complete report-family search and figure inspection. The reported random-effects sensitivity is a distinct second planned sensitivity, so its P=.72 does not substitute for the first four-covariate model. Likewise the eight subgroup pairs do not contain the ninth respiratory-rate pair. This is not proof that analyses were never performed. **Display-precision interval check:** Not applicable to presence/absence of a planned analysis or categorical model/covariate identity. Thresholds 6/8 mL/kg, 2 days, and 25 cm H2O are fixed operational cutpoints, not rounded estimates. No half-unit interval around P=.72 can identify a missing model output.

**Necessary inputs available:** Yes for establishing the four printed plans and supplied-result absence. **Exact missing inputs or definitions:** Per-protocol analyzed sizes and primary estimate/CI/test; adjusted sensitivity estimate/CI/test and confirmation of its four covariates/distribution; respiratory-rate subgroup cutoff, sizes, two effects/intervals and interaction; mediation estimand, implementation and output; or amendments withdrawing these plans. Raw data/code are unavailable and no analysis is recomputed.

**Source-grounded alternative interpretation:** The matrix explicitly acknowledges three nonreporting choices, and may describe an intended reporting version for respiratory rate. The analyses may have been performed elsewhere, omitted, abandoned, or not performed. The supplied material does not select among these alternatives or show a prospective withdrawal. The article explicitly defers ancillary costs, which is retained outside this clinical candidate.

**Direct observation versus inferred explanation:** Direct: four planned clinical families, no identifiable matching supplied results, and matrix reporting annotations. Inference: performance, abandonment, omission mechanism or manuscript-version history. No such explanation is established.

**Document roles and classification:** Protocol promises and prospective SAP specifications are PLAN; main article/eMethods/results displays are REPORT. The attached matrix is PLAN comparison/change context rather than an independent prospective analysis. Primary P_R; All relationships P_R; domain protocol_report. Remove provisional P_P: prospective subgroup list and matrix updated list both plan respiratory rate; the matrix “IN THE PAPER” entry concerns claimed reporting, not a contradictory plan. Matrix per-protocol/mediation/covariate entries corroborate the plan-versus-report comparison without creating new plan conflicts. Main and results supplement do not oppose each other, so their joint lack of results does not add S_C. Classification ambiguity: intended reporting version and undisclosed withdrawal remain unresolved.

**Evidence state:** reproduced. **Determining recheck fact:** Every planned family is read directly, and complete supplied REPORT text/result/figure inspection identifies no matching result. This is an evidence-record statement of supplied nonreporting, not an assertion about whether the analyses occurred.

**Exact remaining human question:** Where are the supplied results for each of the four clinical primary-VFD families, or which documented amendment withdrew each family; in particular, what does the matrix's respiratory-rate “IN THE PAPER” entry refer to?

## C007 — Reported subgroup distribution replaces the planned zero-inflated model

**Location found:** Yes, [SAP p14, subgroup model](../../../joi180108supp2_prod.pdf#page=14), [SAP p22, model change and post-hoc definition](../../../joi180108supp2_prod.pdf#page=22), [main p4, subgroup producing model](../../../jama_simonis_2018_oi_180108.pdf#page=4), [main p6, intubation-location result](../../../jama_simonis_2018_oi_180108.pdf#page=6), and [results supplement p9, every eTable 5 subgroup pair](../../../joi180108supp3_prod.pdf#page=9).

**Source value/text matched:** Yes. SAP subgroup interaction GLMs consider zero-inflated distributions. **Comparator matched:** Yes. Report interaction GLMs consider Gaussian distribution. Matrix p22 repeats updated zero-inflated and in-paper Gaussian, places the change according to the CLT in post-hoc modifications, and defines those as considered in neither original nor updated SAP. All affected printed subgroup outputs are independently source-matched below; effect and CI are in days.

| Pair in eTable 5 | First printed mean difference (95% CI) | Second printed mean difference (95% CI) | Interaction P |
|---|---|---|---|
| Pneumonia / non-pneumonia | 0.86 (−2.48 to 4.20) | −0.50 (−2.13 to 1.13) | .16 |
| Sepsis yes / no | −2.20 (−5.46 to 1.06) | 0.25 (−1.38 to 1.89) | .17 |
| PaO2/FiO2 ≤200 / >200 | −0.87 (−3.21 to 1.47) | 0.87 (−1.62 to 3.36) | .32 |
| LIPS ≥4 / <4 | −0.19 (−2.06 to 1.66) | −0.27 (−2.61 to 2.07) | .96 |
| Clinical / surgical admission | −0.70 (−2.32 to 0.92) | 1.70 (−1.62 to 5.03) | .23 |
| SAPS II ≥50 / <50 | −0.88 (−2.96 to 1.18) | 0.75 (−1.14 to 2.64) | .26 |
| Prior ventilation, first / second numerical line, attribution addressed in C009 | −0.29 (−7.04 to 6.45) | −0.21 (−1.72 to 1.28) | .98 |
| Intubation inside / outside ICU | −2.50 (−4.63 to −0.36) | 1.45 (−0.52 to 3.43) | .01 |

Main p6 prints the same inside/outside effects and .01 interaction. Its IQR notation is not a separately asserted numerical conflict; eTable 5 explicitly labels 95% CI.

**Consistency rule applicable:** Yes, replacement of a planned producing primary-outcome subgroup analysis, Route A category 5. **Logical comparison reproduced:** Yes, zero-inflated and Gaussian distributions are explicitly different specifications; the matrix discloses that change. The report's description as prespecified can apply to subgroup definitions while its producing distribution was changed. **Display-precision interval check:** Not applicable to model-family identity. All shared intubation-location numerical copies are identical: mean-difference intervals [−2.505,−2.495] and [1.445,1.455], corresponding CI endpoints ±0.005, and .01 interaction [0.005,0.015], with zero copy gaps. No effect/CI/P recalculation failure or magnitude of model-induced change is claimed.

**Necessary inputs available:** Yes for stated model comparison and affected-output identity. **Exact missing inputs or definitions:** Any zero-inflated subgroup outputs; effective model-change date or formal amendment beyond the retrospective post-hoc disclosure; and the precise Gaussian fitting details if numerical comparison of models were requested. The recheck does not require those to establish the printed replacement.

**Source-grounded alternative interpretation:** Subgroup definitions were prespecified, with the distribution changed post-hoc for the stated CLT rationale. This is directly disclosed in the matrix and does not imply subgroup definitions were invented after analysis.

**Direct observation versus inferred explanation:** Direct: prospective model family, reported family, disclosure and all eight printed pairs. Inference: how the choice affected effect estimates or interaction P=.01. No preferred model or changed result is asserted.

**Document roles and classification:** Updated subgroup specifications are PLAN; report method/results are REPORT; matrix is comparison/change context. Primary P_R; All relationships P_R; domain protocol_report. The matrix corroborates the actual change, not an independent conflicting prospective PLAN, so no P_P. Main and eTable 5 agree in the shared numbers, so no S_C. Classification ambiguity: “prespecified” definitions versus disclosed post-hoc distribution.

**Evidence state:** reproduced. **Determining recheck fact:** Direct-source zero-inflated and Gaussian producing distributions differ exactly as registered, with explicit post-hoc disclosure.

**Exact remaining human question:** Which specification governed the eight reported subgroup estimates/interactions, and were the zero-inflated subgroup analyses replaced entirely or also performed with results available in the supplied package?

## C008 — Printed PEEP upper quartile does not reconcile with its median

**Location found:** Yes, [results supplement p6, eTable 2, Other Mode of Ventilation, after titration on randomization day, intermediate-arm PEEP and summary footer](../../../joi180108supp3_prod.pdf#page=6). Exact source rendering independently confirms the terminal digit 1. All registered locators/corroborators on this page also match: intermediate contributor header 28; low-arm PEEP 5 (5–10); intermediate day-1 PEEP 8 (5–8), day-2 10 (6–12), and day-3 6 (5–8).

**Source value/text matched:** Yes, PEEP is 8 (5–1) cm H2O. **Comparator matched:** Yes, footer defines data as median (interquartile range), so the three numbers are median 8, Q1 5, Q3 1. The row's P=.50 is matched but is not the conflict.

**Consistency rule applicable:** Yes, quartile ordering and median containment, a printed numeric reading changing magnitude under Route A category 2. An IQR is not treated as a confidence interval.

**Calculation and display-precision interval check reproduced:** Yes. Median interval [7.5,8.5], Q1 [4.5,5.5], and Q3 [0.5,1.5]. To satisfy Q3≥median, an admissible Q3 must lie in [7.5,∞), separated from the printed Q3 interval by at least 7.5−1.5=6; relative gap against the printed Q3 1 is 6/1=6. Even Q3≥Q1 alone requires [4.5,∞), gap 4.5−1.5=3, relative gap 3/1=3. Both exceed 0.05. If the two printed endpoint values were interpreted in reverse order, their maximum [4.5,5.5] still lies below the median interval, with a 2-unit minimum gap. Rounding or endpoint reversal therefore cannot reconcile all three printed quantities.

**Necessary inputs available:** Yes for quartile order/containment; raw data are unnecessary. **Exact missing inputs or definitions:** The intended upper quartile and the original summary output or source data establishing it. Neighboring rows and the low-arm counterpart do not identify a unique replacement.

**Source-grounded alternative interpretation:** A missing terminal digit or another numeric transcription mechanism is possible, but the intended upper quartile cannot be selected from the supplied table. The summary footer and coherent adjacent median/IQR cells support the quartile interpretation, not an alternative interval definition.

**Direct observation versus inferred explanation:** Direct: 8 (5–1), the summary definition, source-confirmed locators and disjoint half-unit intervals. Inference: production mechanism or intended digit. Neither is established.

**Document roles and classification:** Both cell and footer are REPORT result content within one supplementary document. Primary S_W; All relationships S_W; domain statistical_results. No other document is a conflicting comparator. Classification ambiguity: intended Q3 is unavailable.

**Evidence state:** reproduced. **Determining recheck fact:** Independent direct source image confirms 8 (5–1), and allowed rounded quartiles cannot contain the median or retain Q1≤Q3.

**Exact remaining human question:** What upper quartile belongs to the intermediate-arm Other Mode PEEP summary after titration on randomization day, and what original summary output establishes it?

## C009 — Prior-ventilation subgroup labels leave numerical attribution unclear

**Location found:** Yes, [results supplement p9, eTable 5, Ventilation before randomization block](../../../joi180108supp3_prod.pdf#page=9), independently inspected in a direct rendering. The corroborating category definition is [main p4, subgroup list](../../../jama_simonis_2018_oi_180108.pdf#page=4).

**Source value/text matched:** Yes. First numerical line: low 16.5±11.6, intermediate 16.8±10.7, difference −0.29 (−7.04 to 6.45). Second line: low 15.2±11.6, intermediate 15.4±11.5, difference −0.21 (−1.72 to 1.28). Shared interaction P=.98. **Comparator matched:** Yes. The source first line aligns horizontally with the second line of the wrapped “Ventilation before randomization” heading. The >6-hours label aligns with the second numerical line. The ≤6-hours label lies below both numerical lines and has no numerical values horizontally alongside it. Main p4 defines >6 versus ≤6 hours but supplies no result-category assignment.

**Consistency rule applicable:** Yes, conflicting numerical attribution of primary-outcome results to populations within one REPORT, Route B. The comparison is not merely different terminology; it selects which distinct estimate/CI is extracted for each subgroup.

**Logical comparison and display-precision interval check reproduced:** Yes for the layout ambiguity. Reading rows by subgroup sequence suggests first numerical line >6, second ≤6; reading horizontal alignment suggests >6 receives the second line, leaving first-line attribution unresolved. The table supplies no subgroup counts or alternative key. Printed mean differences allow [−0.295,−0.285] and [−0.215,−0.205]. First CI endpoint allowances are [−7.045,−7.035] and [6.445,6.455], giving width [13.48,13.50]; second endpoints [−1.725,−1.715] and [1.275,1.285], width [2.99,3.01]. These distinct interval widths remain distinct after rounding, but are results for different possible subgroups, not conflicting copies of one numeric quantity; no relative-discrepancy threshold is applied to their difference. Rounding cannot assign a population label. No subgroup-CI versus interaction-P conflict is claimed.

**Necessary inputs available:** Yes for exact visual placement, values and the two possible attribution rules. **Exact missing inputs or definitions:** Explicit mapping of the two result lines to >6/≤6 hours, or subgroup counts/output that identifies the rows. Numerical imprecision does not supply that mapping.

**Source-grounded alternative interpretation:** The category sequence may reflect the intended mapping with vertically displaced cells; alternatively the numeric line aligned with >6 may be its intended row. Other table blocks are consistently aligned but do not establish which displacement occurred here. The report methods confirm only the category definitions, not the row identity.

**Direct observation versus inferred explanation:** Direct: labels, row positions, values and absence of counts. Inference: a displaced label, displaced numerical cells, and the intended row mapping. No choice is established by the recheck.

**Document roles and classification:** The compared labels/results are REPORT within one supplementary document; main methods are REPORT corroboration only. Primary S_W; All relationships S_W; domain report_internal_inconsistency. This issue concerns which population receives each result, not estimate arithmetic. Main definitions do not oppose the supplement's values and add no S_C. Classification ambiguity: sequence versus horizontal alignment.

**Evidence state:** reproduced. **Determining recheck fact:** The independently rendered source shows two numerical lines across three relevant label/heading lines, leaving the specific population-to-result mapping unresolved.

**Exact remaining human question:** Which printed numerical line and 95% interval belong to prior ventilation >6 hours, and which to ≤6 hours, as established by the subgroup analysis output or explicit subgroup counts?

## Derivative provenance and bounded limitations

| New derivative path relative to review_1_6_2 | Direct engine, device and source scope |
|---|---|
| preprocessing/recheck-main-layout.txt | pdftotext -layout, Poppler 25.03.0, CPU; main PDF pp1–9 |
| preprocessing/recheck-protocol-layout.txt | pdftotext -layout, Poppler 25.03.0, CPU; original protocol PDF pp1–49; only registered cited sections used for this recheck |
| preprocessing/recheck-sap-layout.txt | pdftotext -layout, Poppler 25.03.0, CPU; SAP PDF pp1–22; registered cited sections and matrix used |
| preprocessing/recheck-results-layout.txt | pdftotext -layout, Poppler 25.03.0, CPU; results supplement PDF pp1–13 |
| preprocessing/recheck-main-p6.png | pdftoppm PNG, Poppler 25.03.0, CPU, scale-to 1800; main PDF p6 |
| preprocessing/recheck-main-p7.png | pdftoppm PNG, Poppler 25.03.0, CPU, scale-to 1400; main PDF p7 |
| preprocessing/recheck-results-p6.png | pdftoppm PNG, Poppler 25.03.0, CPU, scale-to 1800; results supplement p6 |
| preprocessing/recheck-results-p9.png | pdftoppm PNG, Poppler 25.03.0, CPU, scale-to 1800; results supplement p9 |
| preprocessing/recheck-sap-p22.png | pdftoppm PNG, Poppler 25.03.0, CPU, scale-to 1800; SAP p22 |
| preprocessing/recheck-results-figure-10.png | pdftoppm PNG, Poppler 25.03.0, CPU, scale-to 1400; results supplement p10 |
| preprocessing/recheck-results-figure-11.png | pdftoppm PNG, Poppler 25.03.0, CPU, scale-to 1400; results supplement p11 |
| preprocessing/recheck-results-figure-12.png | pdftoppm PNG, Poppler 25.03.0, CPU, scale-to 1400; results supplement p12 |
| preprocessing/recheck-results-figure-13.png | pdftoppm PNG, Poppler 25.03.0, CPU, scale-to 1400; results supplement p13 |

No source-location confirmation is blocked by missing tooling. There is no unresolved page assignment or unconfirmed registered transcription. Producing estimands, operational definitions, governing amendments, unreported analysis outputs, intended upper quartile and subgroup row mapping remain exactly the human questions specified above. Nonreporting is limited to the supplied package and does not establish nonperformance. The rechecker did not modify candidate_ledger.md, any supplied source, or any reused artifact. The coordinator should apply the summary's evidence states and C006 relationship amendment without removing any ID.


# Fresh appended-ID recheck

# Appended stable-ID evidence recheck

Fresh runtime `/root/append_rechecker_c010`, `qc162_evidence_rechecker`, run model `gpt-6.1-sol`, reasoning effort `high`. Assigned scope is C010 only; C001–C009 are outside this part. QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely. Registration and the independent pass-2 inclusion screen were used to identify the exact comparison; the current supplied PDFs are final authority. No legacy scientific decisions, external evidence, or other candidates were used to select this issue. Sources and reused artifacts were preserved.

## C010 — Vasopressor-duration window and counting unit remain unresolved

**Review domain:** report_internal_inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 4 title vs its vasopressor-duration row and footer

**Evidence state:** reproduced

**Finding IDs:** F-ST2-501

**Qualifying route:** Route B

**Human review status:** Pending Human Adjudication

### Location found and source value/text matched

The exact supplied results supplement, `joi180108supp3_prod.pdf`, physical p8, was read using fresh selected-page native/layout extraction and independently viewed as a fresh direct-PDF rendering. This confirmed every affected location of the two-arm pattern. Evidence links below identify the source PDF, not the extraction or image as authority.

| Affected source location | Role by content | Found | Exact source content matched |
|---|---|---|---|
| [Physical p8, eTable 4 title](../../../joi180108supp3_prod.pdf#page=8) | REPORT: clinical result display | Yes | “Sedatives, analgesics, neuromuscular blockade, fluids, vasopressors and co-interventions during the first three days.” |
| [Physical p8, Days of vasopressor use, Low Tidal Volume column](../../../joi180108supp3_prod.pdf#page=8) | REPORT: observed duration distribution | Yes | `2 (1–4)` under the arm header `n = 477`. |
| [Physical p8, Days of vasopressor use, Intermediate Tidal Volume column](../../../joi180108supp3_prod.pdf#page=8) | REPORT: observed duration distribution | Yes | `2 (1–4)` under the arm header `n = 484`. |
| [Physical p8, P-value cell for Days of vasopressor use](../../../joi180108supp3_prod.pdf#page=8) | REPORT: between-arm comparison | Yes | `0.87`. This is matched context, not a conflicting value. |
| [Physical p8, summary footer](../../../joi180108supp3_prod.pdf#page=8) | REPORT: distribution definition attached to result | Yes | “Data are number / total (%) or median (interquartile range).” Thus the duration entries are medians with IQRs. |
| [Physical p8, vasopressor footnote a](../../../joi180108supp3_prod.pdf#page=8) | REPORT: exposure definition attached to result | Yes | Need of any dose of norepinephrine and/or epinephrine, and dopamine `>5 µg/kg/min`; no day-counting convention, start/end, or row-specific duration window is specified. |

Both arm cells belong to this one pattern and have been separately confirmed. No source transcription or location amendment is needed.

### Comparator matched and source-grounded context

The comparator is the **same table's first-three-days horizon**, read directly from its title, against the **upper quartile 4 days in each duration cell**, interpreted using its own median/IQR footer. This is a comparison within one REPORT, rather than a difference between a protocol and a report or between two result documents.

The following supplied REPORT locations were also reread directly as context. They do not introduce additional conflicting relationships:

| Context location | Found and matched | Consequence for this comparison |
|---|---|---|
| [Results supplement p5, eTable 1 title and column labels](../../../joi180108supp3_prod.pdf#page=5) | “Respiratory variables during the first three days of ventilation”; columns “After titration on day of randomization”, “Day 1”, “Day 2”, and “Day 3”. | Four measurement occasions are explicitly displayed under a first-three-days heading. Randomization date plus days 1–3 can support a calendar-date interpretation. They do not define vasopressor duration. |
| [Results supplement p6, eTable 2 title and repeated column labels](../../../joi180108supp3_prod.pdf#page=6) | “Ventilator settings during the first three days of ventilation”; after-titration randomization-day and day-1/day-2/day-3 columns in each mode block. | Corroborates the same possible date-label convention. Measurement occasions alone do not establish elapsed exposure length. |
| [Results supplement p7, eTable 3 title and repeated column labels](../../../joi180108supp3_prod.pdf#page=7) | “Respiratory variables during the first three days of ventilation”; after-titration randomization-day and day-1/day-2/day-3 columns in each mode block. | Corroborates the alternative but does not specify how eTable 4's duration row was computed. |
| [Results supplement p8, nearby duration and daily rows](../../../joi180108supp3_prod.pdf#page=8) | Sedative durations `0.6 (0.3–1.5)` / `0.6 (0.0–1.5)`, analgesic durations `0.7 (0.3–2.0)` / `0.7 (0.4–2.0)`; RASS and “Fluid balance in 24 hours” explicitly have Day 1, Day 2, Day 3 rows. | Fractional drug durations and integer vasopressor displays do not establish a shared or different counting convention. The explicit daily labels reinforce the observation-horizon question. |
| [Main article physical p4, Outcomes and Other Study Parameters](../../../jama_simonis_2018_oi_180108.pdf#page=4) | Describes secondary measures including sedatives, analgesics, neuromuscular blocking agents, transfusions, dead-space reduction and delirium; describes cumulative drug-use collection for economic measures. | Does not supply an exposure start/end or a definition of days for the vasopressor-duration cells. Cumulative drug-use collection is not assigned to this result by the main text. |
| [Main article physical p6, eTable 4 narrative reference](../../../jama_simonis_2018_oi_180108.pdf#page=6) | Narrative refers to need for, duration of, and amount of sedatives, analgesics and neuromuscular blocking agents, citing eTable 4; also discusses fluids, transfusion and rescue therapies. | Supplies no independent vasopressor-duration distribution or counting rule that chooses between elapsed time, dates touched, and a longer course. |

### Consistency rule applicable

The applicable logical rule is that an exposure duration computed **as elapsed time confined to a three-day window** cannot have an upper quartile above three days. If instead the quantity counts **exposed calendar dates including randomization date and days 1–3**, four can be an admissible upper quartile. These are different quantities for extraction; neither convention is selected as the authors' convention by this recheck.

The registered issue is the unresolved attribution of the two printed distributions to an observation window and counting unit. It is not a claim that four calendar dates cannot occur within the described study phase, a quartile-order issue, a between-arm discrepancy, or an interval-versus-P-value conflict. The IQR is a marginal distribution summary, not a confidence interval for a between-arm effect. P=.87 cannot be used to test its compatibility with either arm's IQR.

Scope permits a label that changes which quantity a value represents when the values do not identify the intended quantity. Here the named values are both arms' `2 (1–4)` vasopressor-duration distributions. The issue concerns their attached analysis window/counting definition, rather than merely different table headings or a peripheral copy of a descriptive value. The p5–7 headings are contextual support for an alternative; they are not independently registered differences. No primary/key-secondary designation is inferred for vasopressor duration.

### Calculation and logical comparison reproduced, including precision

For each arm separately:

| Check | Printed or recomputed intervals | Gap and conclusion |
|---|---|---|
| Median 2, Q1 1, Q3 4 rounding allowances | Median `[1.5,2.5]`; Q1 `[0.5,1.5]`; Q3 `[3.5,4.5]`. | Ordered quartiles containing the median are possible. No order or containment discrepancy is present. |
| Conditional elapsed-duration interpretation within exactly three days | Admissible Q3 interval `[0,3]`, compared with printed Q3 interval `[3.5,4.5]`. | Minimum gap `3.5−3=0.5` days; relative discrepancy `0.5/4=0.125`, exceeding `0.05`. The elapsed-window reading does not reconcile through display precision. |
| Conditional four-calendar-date counting interpretation | Admissible Q3 interval `[0,4]`, compared with printed Q3 interval `[3.5,4.5]`. | Intervals overlap on `[3.5,4]`; gap zero. Such counting can reconcile the numeric upper quartile. It remains an alternative because no vasopressor-specific counting definition is supplied. |
| Both arms' printed summaries compared as copies | Both medians and both quartiles have identical intervals. | Every copy-comparison gap is zero; no inter-arm numerical discrepancy is alleged. |

The phrase “first three days” is a declared observation window, not a rounded numeric estimate. The three-day upper bound in the elapsed-duration calculation is therefore exactly 3, not `[2.5,3.5]`. That calculation is expressly conditional on elapsed counting. A calendar-date count is discrete and may have value 4; no fractional-calendar-date convention is assumed. The printed rounding interval is a conservative display check, rather than a claim that the underlying count was fractional.

The logical reproduction is therefore: exact title and exact upper quartiles admit substantively different result quantities, one of which conflicts beyond rounding with an elapsed three-day bound and one of which can reconcile through calendar-date counting, while the source does not specify the convention. The mechanical check does **not** establish a source-authoritative elapsed-duration contradiction. It reproduces the registered unresolved quantity attribution.

### Necessary inputs available and exact missing inputs or definitions

**Available:** exact title, duration row label, both arm summaries, arm headers, distribution footer, vasopressor drug/dose criterion, P-value cell, adjacent explicit day labels, neighboring four-occasion displays, and relevant main-text references. These suffice to confirm the printed observation and the conditional precision comparisons.

**Missing:** the vasopressor-duration exposure start and stop, whether partial days are accumulated as elapsed fractions or count as calendar dates, whether randomization date is included in addition to days 1–3, whether the duration row is truncated to eTable 4's stated horizon or summarizes a longer course, the patient-level durations and contribution set, and a row-specific definition that maps the table title to this summary. Patient-level observations are unnecessary for the two conditional bounds but would be needed to reconstruct the actual distributions. Neither a day-counting rule nor the producing mechanism can be determined from drug names and dose threshold.

### Source-grounded alternative interpretation

The strongest supplied-context alternative is counting calendar dates with vasopressor use, including the randomization date plus day 1, day 2 and day 3. The adjacent tables explicitly display these four occasions under similar first-three-days headings. This would permit an upper quartile 4 and remove the conditional elapsed-bound discrepancy. Those respiratory-measurement labels do not explicitly extend their counting convention to the vasopressor-duration row.

A row summarizing a longer treatment course is also possible, but the supplied p8 row/footnote does not disclose a longer window. A different intended title or upper quartile could also be contemplated, but no alternative printed value is supplied. None of these possibilities is established or proposed as a correction. The remaining issue is which quantity the displayed values actually summarize.

### Direct observation versus inferred explanation

**Direct observation:** the REPORT title says first three days; both arm cells print median 2 and upper quartile 4; the footer identifies IQRs; the footnote defines drugs/dose but supplies no duration convention; adjacent tables show four measurement occasions under similar headings; relevant main text supplies no resolving vasopressor-duration definition.

**Conditional logical calculation:** an elapsed exposure limited to three days gives a 0.5-day minimum rounding-interval gap for Q3=4; a four-calendar-date interpretation gives zero gap. Both calculations reproduce.

**Inferred explanation, not established:** that the authors actually counted calendar dates, used a longer course, or intended another title/quartile. The recheck selects none. It also does not infer the individual-level vasopressor distribution or its generating analysis from the identical summaries and P=.87.

### Classification confirmation and ambiguity

Every conflicting location belongs to the same observed-results supplement and is REPORT by content. The within-document title/result-definition comparison gives **S_W** as the sole relationship, so precedence does not introduce another type. The contextual main-article references are REPORT but do not contain an opposing definition or result and therefore do not add S_C. No PLAN content participates in the comparison; there is no P_R or P_P relationship.

**report_internal_inconsistency** is confirmed because the registered question is which time-window/counting quantity the numbers belong to. It is not a claim that an identified statistical method, inter-arm estimate, interval or test fails. The provisional classification needs no correction.

**Classification ambiguity:** calendar-date counting including randomization date may reconcile the upper quartile with the heading, whereas an elapsed three-day interpretation does not. A longer course or different intended title/quartile remains possible. This ambiguity concerns result meaning, not the role or document identity.

### Evidence state and determining recheck fact

**reproduced.** The exact current supplied source confirms every registered location and numerical value without a transcription amendment; both conditional precision comparisons reproduce. No row-specific exposure or counting definition resolves which quantity receives the two duration distributions. The source-grounded calendar-date alternative is retained explicitly. This state records reproduction of the unresolved quantity-attribution candidate, not an adjudication or an assertion that elapsed duration is the authors' convention.

### Exact remaining human question

Which exposure start/end and definition of “days” produced both `2 (1–4)` summaries, and how does the four-day upper quartile relate to eTable 4's first-three-days horizon?

### Tooling, derivative provenance and limits

Compute device: CPU, as recorded in tooling_record.md. Exact current-source layout text was read with direct `pdftotext`, Poppler 25.03.0, for results supplement physical pp5–8 and main physical pp4/6. These selected-page extractions were returned to stdout; no text derivative was written. Fresh visual confirmation used direct `pdftoppm`, Poppler 25.03.0, `-f 8 -l 8 -singlefile -r 130 -png joi180108supp3_prod.pdf`, producing `preprocessing/recheck-C010-supp3-p8.png` within this run. The fresh image was viewed completely, confirming title, arm alignment, both cells, P value and footnotes against the current source. No OCR or fallback environment was used. Relative PDF links were checked mechanically and resolve to supplied files.

Scope completed: 1 assigned stable ID, C010; 1 two-arm pattern; all affected p8 locations and 5 contextual source pages reread. No scientific inspection gap remains in this scope. The duration convention and underlying observations remain unavailable in the supplied evidence and are recorded above as the human question. Sources/reused assets and coordinator-owned canonical artifacts were not changed.
