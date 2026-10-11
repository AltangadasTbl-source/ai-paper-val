# Workflow 1.6 Stable Candidate Ledger

Pending Human Adjudication. Discovery began from the complete source maps, not previous candidates. All 44 pages were mapped. The first checker wave emitted 25 observations: 7 main numeric, 6 support numeric, 9 cross-source, and 3 statistical. Six repeated observations were merged before IDs, leaving 19 distinct candidates. No assigned ID may be deleted, merged, renumbered, or suppressed. Missing definitions and source-grounded alternatives remain explicit.

Classification is finalized from the mandatory mechanical recheck. Evidence states are evidence-record facts; suggested review dispositions are mechanically derived pre-fills for human review, not adjudications. All candidates remain Pending Human Adjudication. Roles are assigned by content: DOC-001 REPORT, DOC-002 PLAN, DOC-003 REPORT.

## Classification table

| ID | Primary category | Relationship type | All relationships | Compared document roles | Review domain | Evidence state | Suggested review disposition |
|---|---|---|---|---|---|---|---|
| C001 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT main Results/Table2 vs REPORT main Figure1 | statistical_results | recorded_candidate | retain |
| C002 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT main Table1 CAD count/total vs REPORT same-table percentage | statistical_results | recorded_candidate | retain |
| C003 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT main Table1 EMS count/total vs REPORT same-table percentage | statistical_results | recorded_candidate | retain |
| C004 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main Key Points vs REPORT main Outcomes/Table2 | report_internal_inconsistency | recorded_candidate | retain |
| C005 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main Clinical Events vs REPORT main Outcomes/Table3/Figure2 | report_internal_inconsistency | recorded_candidate | retain |
| C006 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main Discussion vs REPORT main Figure2 axis | report_internal_inconsistency | recorded_candidate | retain |
| C007 | Numeric or arithmetic inconsistency | S_W | S_W | REPORT main NIHSS imputation paragraph vs REPORT main Table1 medians | statistical_results | record_input_error | discuss |
| C008 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT results supplement eTable4 control antithrombotic fraction vs REPORT same-cell percentage | statistical_results | recorded_candidate | retain |
| C009 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT results supplement eTable4 control anticoagulation fraction vs REPORT same-cell percentage | statistical_results | recorded_candidate | retain |
| C010 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT results supplement eTable4 control lipid-lowering fraction vs REPORT same-cell percentage | statistical_results | recorded_candidate | retain |
| C011 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT results supplement eTable4 control antidiabetic fraction vs REPORT same-cell percentage | statistical_results | recorded_candidate | retain |
| C012 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN protocol opportunity example vs PLAN protocol measure list | plan_material | record_input_error | discuss |
| C013 | Measure, label, or scale inconsistency | P_R | P_R, S_C, S_W | REPORT main/results-supplement LDL labels vs PLAN protocol definition and REPORT results-supplement definition | protocol_report | recorded_candidate | retain |
| C014 | Denominator, proportion, or total inconsistency | S_C | S_C | REPORT main baseline-survey total vs REPORT results-supplement per-cluster recruitment | statistical_results | recorded_candidate | retain |
| C015 | Cross-document numeric inconsistency | S_C | S_C | REPORT main Table1 dyslipidemia counts vs REPORT results-supplement eTable2 counts | report_internal_inconsistency | recorded_candidate | retain |
| C016 | Cross-document numeric inconsistency | S_C | S_C | REPORT main Table1 NIHSS arm medians vs REPORT results-supplement eTable2 availability medians | report_internal_inconsistency | recorded_candidate | retain |
| C017 | Measure, label, or scale inconsistency | P_R | P_R, S_C | REPORT main composite aggregation vs PLAN protocol aggregation and REPORT results-supplement aggregation | protocol_report | recorded_candidate | retain |
| C018 | Statistical reporting inconsistency | S_W | S_W | REPORT main mortality prose vs REPORT main Table3 in-hospital AD P value | statistical_results | recorded_candidate | retain |
| C019 | Statistical reporting inconsistency | S_W | S_W | REPORT main Table3 in-hospital AD confidence interval vs REPORT same-row AD P value | statistical_results | recorded_candidate | retain |

## Duplicate-merge record

NUM-MAIN-01/F-A compare the same Figure1 primary-analysis labels with the same main primary total: C001. NUM-MAIN-05/F-H compare the same discharge/onset time-origin labels: C005. NUM-MAIN-06/F-I/STAT-C compare the same Discussion quantity name with Figure2's cumulative-incidence ordinate: C006 (two duplicate observations removed). NUMSUP-06/F-E compare the same >100 versus ≥100 lipid-measure labels/definition; repeated main/plan occurrences are preserved in C013. F-G/STAT-B compare the same blanket mortality nonsignificance statement with AD P=.009: C018. STAT-A uses a different comparator (CI/P), so remains C019. Main imputation median and the supplementary partition medians have different comparator/reference-population rules and remain C007/C016. Four eTable4 arithmetic cells remain separate C008–C011. Their shared table is not a reason to merge.

## C001 — Primary-analysis population labels give different totals

Provenance: NUM-MAIN-01; cross F-A. Relationships N001/N003/N014/N067 and X04/X49. Category: Denominator, proportion, or total inconsistency. Classification rationale: all conflicting primary-analysis labels are in DOC-001 REPORT; PLAN ITT only corroborates. Ambiguity: a follow-up-specific population may be intended in Figure1.

Source evidence: [main p4 Results/Data Analysis](../../jama_wang_2018_oi_180070.pdf#page=4) says 4800 enrolled and included in primary analysis, with ITT for all outcomes. [main p5 Figure1](../../jama_wang_2018_oi_180070.pdf#page=5) says 2003 intervention and 1977 control patients included in primary analysis. [main p7 Table2](../../jama_wang_2018_oi_180070.pdf#page=7) uses 2400 per arm for all-or-none. Compared roles: REPORT/REPORT.

Rule/calculation: 2003+1977=3980, which differs from 4800 by820; losses397+423=820 explain a follow-up-completion subtraction but do not qualify the primary-analysis label. Exact integer tolerance. Direct observation is conflicting totals; inference is that Figure1 labels follow-up completers. Alternative: separate analysis subset. Human question: what population do the figure's bottom labels intend, and which entered co-primary analyses? No claim that820 were actually omitted.

## C002 — Intervention CAD percentage and displayed count/total differ

Provenance NUM-MAIN-02; N031. Category: Denominator, proportion, or total inconsistency. Both compared inputs are REPORT Table1; S_W. Ambiguity: an unreported row-specific denominator could explain the fraction.

[Main p6 Table1](../../jama_wang_2018_oi_180070.pdf#page=6) intervention CAD/previous MI prints311(13.05), with2400 patients. Calculation100×311/2400=12.958333%, nearest two decimals12.96%, whereas13.05 differs by0.091667 percentage point, exceeding0.005-point precision tolerance. No row denominator is supplied; general imputation is onp4. Direct printed mismatch under table count/percent convention. Human question: which numerator/denominator produced13.05? A different denominator or transcription could explain it; no correction assigned.

## C003 — Control EMS percentage and count/total differ

Provenance NUM-MAIN-03; N035. Category: Denominator, proportion, or total inconsistency; REPORT/REPORT within main Table1, S_W. Ambiguity: possible row-specific missingness.

[Main p6 Table1](../../jama_wang_2018_oi_180070.pdf#page=6) control EMS transport236(9.9) among2400. Calculation100×236/2400=9.833333%, nearest one decimal9.8;9.9 differs by0.066667 percentage point, outside0.05-point tolerance. The adjacent238(9.9) onset-time row is a different variable. Human question: is an unreported EMS denominator intended, or which cell input should be reconciled? Counts, percentage and denominator are direct observations; any production explanation is inferred.

## C004 — Unqualified all-nine outcome label differs from eligible-measure definition

Provenance NUM-MAIN-04; N008/N009/N040/N041. Category: Measure, label, or scale inconsistency; S_W. Both locations REPORT; PLAN eligibility is only contextual. Ambiguity: ordinary shorthand for the nine-measure bundle may be intended.

[Main p2 Key Points](../../jama_wang_2018_oi_180070.pdf#page=2) calls the outcome adherence to all9 performance measures. [Main p3 Outcomes](../../jama_wang_2018_oi_180070.pdf#page=3) defines all measures for which each patient was eligible. [Main p7 Table2](../../jama_wang_2018_oi_180070.pdf#page=7) gives all-or-none1290/2400 and1147/2400, but rtPA receipt46/212 and23/204. A literal all-nine recipient must receive rtPA, so counts could not exceed46/23; displayed all-or-none exceeds these by1244/1124. This is a label-interpretation diagnostic, not a claim that the analysis used literal all-nine receipt. Human question: should the Key Points eligibility qualification be explicit? Exact integer/definition rule; shorthand is the source-grounded alternative.

## C005 — Matched clinical results use discharge and onset time origins

Provenance NUM-MAIN-05; F-H; N010/N050–N059/N062/N064; X64. Category: Measure, label, or scale inconsistency; S_W. Conflict wholly REPORT main article; protocolp16 corroborates onset without introducing P_R. Ambiguity: discharge may describe contact rather than assessment horizon.

[Main p5 Clinical Events](../../jama_wang_2018_oi_180070.pdf#page=5) labels3/6/12months after discharge and reports Table3 vascular/disability estimates. [Main p3 Outcomes](../../jama_wang_2018_oi_180070.pdf#page=3) specifies after initial symptom onset; [main p8 Table3/Figure2](../../jama_wang_2018_oi_180070.pdf#page=8) labels onset. Rule: time since discharge=time since onset−onset-to-discharge interval. [Table1 p6](../../jama_wang_2018_oi_180070.pdf#page=6) stay medians13/12days show different events, but no fixed shift in outcomes can be inferred. Human question: which clock generated the matched clinical outcomes and plot risk sets? Direct time-label difference, exact identity; possible shorthand or narrative error.

## C006 — Cumulative-incidence plots called HR curves

Provenance NUM-MAIN-06; F-I; STAT-C; N062/N064/N066; X71; S104. Category: Measure, label, or scale inconsistency; S_W, REPORT/REPORT. Ambiguity: loose shorthand for curves accompanied by a hazard ratio.

[Main p7 Discussion](../../jama_wang_2018_oi_180070.pdf#page=7) says HR curves separated in first30days. [Main p8 Figure2A](../../jama_wang_2018_oi_180070.pdf#page=8) has Cumulative Incidence ordinate,0/.05/.10/.15 ticks, separate arm curves and scalarHR0.72(0.60–0.87),P<.001. Figure2B likewise has incidence axes and separateHR0.86. Incidence probabilities and a comparative hazard ratio are different quantities; no tail-probability or HR reconstruction needed. Direct label mismatch; possible informal naming. Human question: which plotted quantity did the discussion intend? No claim that scalarHR is incorrect.

## C007 — NIHSS imputation median differs from displayed group medians

Provenance NUM-MAIN-07; N013/N034. Category: Numeric or arithmetic inconsistency; S_W, REPORT main/main. Ambiguity: imputation reference population and data stage are unspecified.

[Main p4 Data Analysis](../../jama_wang_2018_oi_180070.pdf#page=4) says one missing NIHSS score replaced by median3. [Main p6 Table1](../../jama_wang_2018_oi_180070.pdf#page=6) gives baseline801 and both2400-patient arm medians4. Conditional rule: adding one score equal to the observed pooled median3 preserves that median; pooled equal-arm conventional medians4 cannot yield pooled3. Even integer/half-integer display tolerances do not explain exact3 if both displayed medians4 reflect conventional rounded summaries. Direct observation is3 versus4; shared-population identity is an assumption requiring confirmation. Hospital-specific, external/subgroup median or different snapshot could reconcile. Human question: what population supplied median3 and how does it relate to Table1? This is distinct from C016's independent cross-document partition comparison.

Mechanical recheck: record_input_error. The source does not establish that the imputation median refers to the pooled trial cohort; this unsupported alignment prevents the registered pooled-median inconsistency from being settled. Suggested review disposition discuss is a mechanical pre-fill, not an adjudication.

## C008 — Sensitivity control discharge-antithrombotic fraction and percentage differ

Provenance NUMSUP-01; N564. Category: Denominator, proportion, or total inconsistency; S_W, REPORT same-cell.

[Results supplement p8 eTable4](../../joi180070supp2_prod.pdf#page=8) control discharge antithrombotics2141/2400(89.3). Computation89.208333%, rounds89.2 at one decimal;89.3 differs0.091667 percentage point, outside±0.05. Adjusted effect columns are distinct and not comparators. Alternative: undisclosed weighting/denominator or transcription. Human question: does the raw fraction use2141of2400 and what explains89.3? Direct printed inputs and mathematical mismatch; no correction.

## C009 — Sensitivity control AF-anticoagulation fraction and percentage differ

Provenance NUMSUP-02; N565. Category: Denominator, proportion, or total inconsistency; S_W, REPORT same-cell.

[Results supplement p8 eTable4](../../joi180070supp2_prod.pdf#page=8) control anticoagulation39/174(22.5). Computation22.413793%, rounds22.4; discrepancy0.086207 percentage point outside±0.05. Alternative: different raw inputs/weighted percentage not specified. Human question: which denominator/count or percentage convention produced22.5? Adjustment footnote applies to effects, not an alternative raw-percentage definition. No actual replacement input assigned.

## C010 — Sensitivity control lipid-lowering fraction and percentage differ

Provenance NUMSUP-03; N566. Category: Denominator, proportion, or total inconsistency; S_W, REPORT same-cell. This arithmetic issue is distinct from C013's eligibility-label comparison.

[Results supplement p8 eTable4](../../joi180070supp2_prod.pdf#page=8) control lipid-lowering1439/1586(90.8). Computation90.731400%, rounds90.7; discrepancy0.068600 percentage point outside±0.05. Human question: does the displayed raw fraction determine this percentage, or is another input/convention intended? Alternative: undisclosed denominator/weighting or transcription; none selected. Both source inputs directly observed.

## C011 — Sensitivity control antidiabetic fraction and percentage differ

Provenance NUMSUP-04; N568. Category: Denominator, proportion, or total inconsistency; S_W, REPORT same-cell.

[Results supplement p8 eTable4](../../joi180070supp2_prod.pdf#page=8) control antidiabetics557/688(81.1). Computation80.959302%, rounds81.0; discrepancy0.140698 percentage point outside±0.05. Human question: which inputs/convention explain81.1 in the No./Total(%) column? Possible transcription or undisclosed weighting; no correction assigned. Direct fraction/percent mismatch, not adjusted-effect arithmetic.

## C012 — PLAN example names seven measures while the PLAN specifies nine

Provenance NUMSUP-05; N520/N512. Category: Numeric or arithmetic inconsistency; P_P only. Ambiguity: explicitly hypothetical model illustration may not assert actual trial measure count.

[Protocol p19 lines276–279](../../joi180070supp1_prod.pdf#page=19) says eligible for5 of the7 measures, then3 met and2 not met. [Protocol p13 Table2](../../joi180070supp1_prod.pdf#page=13) and [p14 continuation](../../joi180070supp1_prod.pdf#page=14) list4 acute+5 discharge=9. Rule7≠9 for a shared inventory;5=3+2 itself is coherent. Direct numbers differ, but applying the actual-trial universe to an example is interpretive. Cross X35/statistical pass1 read7 as an illustrative example, not an independent trial total; this alternative must be tested explicitly during recheck. Human question: is the7 intentional hypothetical/subset wording? No allegation that actual estimates used7 measures. All conflicting locations are PLAN; main's parallel example merely corroborates.

Mechanical recheck: record_input_error. The source explicitly introduces a hypothetical example; aligning its seven-measure illustration with the actual trial inventory is unsupported. Whether a residual wording question remains cannot be settled from the package. Suggested review disposition discuss is a mechanical pre-fill, not an adjudication.

## C013 — Lipid-measure threshold/eligible-set labels differ across supplied definitions

Provenance NUMSUP-06; F-E; N566/N536; X42. Category: Measure, label, or scale inconsistency. Primary P_R; all P_R,S_C,S_W by precedence. REPORT main/results-supplement labels>100 conflict with PLAN≥100 definition; main vs results definition is S_C; results supplement title vs its definition is S_W. No PLAN-internal contradiction. Ambiguity: labels may abbreviate the full measure.

[Main p3 Outcomes](../../jama_wang_2018_oi_180070.pdf#page=3) more than100mg/dL or undocumented; [main p7 Table2](../../jama_wang_2018_oi_180070.pdf#page=7) LDL>100 fractions1415/1481 and1439/1547. [Results supplement p8 eTable4](../../joi180070supp2_prod.pdf#page=8) LDL>100 fractions1415/1517 and1439/1586. [Results supplement p3 eTable1](../../joi180070supp2_prod.pdf#page=3) LDL≥100,previous treatment,or undocumented; [protocol p15 Table3](../../joi180070supp1_prod.pdf#page=15) specifies the same broader eligibility. Exactly100 is included by≥ and excluded by>; prior-treatment/undocumented wording additionally broadens abbreviated titles. No count of boundary patients or eligibility implementation is available, so no denominator correction inferred. Human question: which eligible set generated primary/sensitivity denominators, and are titles shorthand? Direct definition difference; actual patient effect unknown.

## C014 — Baseline survey total differs from per-cluster statement

Provenance F-B; X07. Category: Denominator, proportion, or total inconsistency; S_C, REPORT main/results supplement. Ambiguity: nominal target or different snapshot.

[Main p6 Table1](../../jama_wang_2018_oi_180070.pdf#page=6) baseline40 hospitals/801 patients. [Results supplement p2 eAppendix](../../joi180070supp2_prod.pdf#page=2) states20patients per cluster prospectively included.40×20=800, differing by1 with exact-integer tolerance. Human question: was20 an exact count or target, and did one cluster recruit21? Source provides no per-cluster baseline records. Direct totals/statements; identity depends on same finalized phase and exact interpretation.

## C015 — Dyslipidemia totals differ across the same full cohort's partitions

Provenance F-C; X23; mainN030/supportN542. Category: Cross-document numeric inconsistency; S_C, REPORT/REPORT. Ambiguity: possible undocumented recoding/definition/snapshot.

[Main p6 Table1](../../jama_wang_2018_oi_180070.pdf#page=6) randomized arms305/2400 and291/2400 dyslipidemia patients (12.7/12.1%). [Results supplement p5 eTable2](../../joi180070supp2_prod.pdf#page=5) availability groups285/3949 and62/851 (7.2/7.3%). Both partitions sum4800; fixed characteristic sums596 versus347, difference249. Other seven matched characteristic totals reconcile. Counts of one baseline variable should be partition-invariant if definitions/snapshot/records match. Human question: which dataset/definition produced each total? Direct sums; same-characteristic identity named as assumption, no prevalence correction assigned.

## C016 — NIHSS medians differ across exhaustive cohort partitions

Provenance F-D; X27; mainN034/supportN546; S061. Category: Cross-document numeric inconsistency; S_C, REPORT/REPORT. Ambiguity: exact observation count, quantile convention or snapshot could differ. The main imputation paragraph is contextual only; its separate conflict is C007.

[Main p6 Table1](../../jama_wang_2018_oi_180070.pdf#page=6) two groups n2400 each, admissionNIHSS median4,IQR2–6. [Results supplement p5 eTable2](../../joi180070supp2_prod.pdf#page=5) groups3949/851 both median3,IQR2–6. For conventional medians of integer scores, each n2400 median4 allows at most1200 scores≤3, pooled≤2400. Odd groups median3 require at least1975+426=2401 scores≤3. Thus the same4800 observations cannot satisfy both summaries. This conditional order-statistic diagnostic cannot identify a replacement summary. The source reports one missing NIHSS score; one omitted observation can bridge this one-observation rank bound. Patient totals must not be silently treated as NIHSS-specific observation counts; imputation, missingness, quantile conventions and data stage must be checked. Human question: do both rows use all4800 admission scores with the same convention and imputation? No clinical implication inferred.

## C017 — Composite descriptions imply different aggregation weights

Provenance F-F; X46; mainN009/supportN515/N526. Category: Measure, label, or scale inconsistency; P_R and S_C, precedenceP_R. REPORT main per-patient average differs from PLAN and REPORT-supplement aggregate wording. Ambiguity: aggregate wording may implicitly denote patient-level ratios.

[Main p3 Outcomes](../../jama_wang_2018_oi_180070.pdf#page=3) calculates eligible received/possible ratio per patient then averages; [main p7 Table2](../../jama_wang_2018_oi_180070.pdf#page=7) reports composite mean(SD)88.2(15.1)/84.8(18.2). [Protocol p16 lines216–219](../../joi180070supp1_prod.pdf#page=16) total interventions performed among eligiblepatients/total possible interventions; [results supplement p2](../../joi180070supp2_prod.pdf#page=2) same aggregate formula and same endpoint definition as randomized phase,baseline80.2/79.5. Rule mean(m_i/e_i) generally differs fromΣm_i/Σe_i when e_i vary. No patient-level inputs provided to calculate actual difference. [Main p4](../../jama_wang_2018_oi_180070.pdf#page=4) opportunity-level GEE is a separate inferential construction and not a conflicting comparator. Human question: which weighting/aggregation generated each descriptive summary? No claim any printed percentage or conclusion is wrong.

## C018 — Mortality prose and in-hospital AD P value have different significance interpretations

Provenance F-G; STAT-B; X62; S035/S036. Category: Statistical reporting inconsistency; S_W, REPORT main/main. Ambiguity: prose may exclusively summarize HR tests.

[Main p5 Clinical Events](../../jama_wang_2018_oi_180070.pdf#page=5) no significant difference in total mortality in hospital and3/6/12months. [Main p8 Table3](../../jama_wang_2018_oi_180070.pdf#page=8) in-hospital ADP=.009,HRP=.14; [main p4](../../jama_wang_2018_oi_180070.pdf#page=4) statesP<.05. Direct comparison .009<.05 while blanket prose says no significance. HR.14>.05 supports prose if limited toHR. Distinct estimands need not agree and no CI reconstruction required. Human question: which test/estimand does the mortality sentence summarize and isADP correctly printed? This is distinct from C019's CI/P comparator.

## C019 — In-hospital death CI and paired P value show different inferential signals

Provenance STAT-A; S035; HR S036 context only. Category: Statistical reporting inconsistency; S_W, REPORT same Table3 row. Ambiguity: exact CI/test construction is not stated.

[Main p8 Table3](../../jama_wang_2018_oi_180070.pdf#page=8) in-hospital death11/2400vs23/2400, adjustedAD−0.7percentagepoint,95%CI−1.1to+0.2,ADP=.009. [Main p4](../../jama_wang_2018_oi_180070.pdf#page=4) states95%CIs,two-sidedtests,P<.05. Direct printedCI includes0 whilepairedP<.05. A CI formed by inversion of that same two-sided test would conflict, but shared construction is not supplied. Diagnostic midpoint−0.45 differs fromestimate−0.7 by0.25; rounding ranges midpoint[−0.50,−0.40] versusestimate[−0.75,−0.65] do not overlap for a symmetric original-scaleCI. Symmetry/Wald conventions are not established, so no correctedCI or reconstructedP is asserted. SeparateHR0.96(0.90–1.02),P=.14 is not theAD comparator. Human question: whichADmodel,CIalgorithm,test,variance,dfandfit produced these values? Different non-inverted/asymmetric inference or transcription could explain them.

# Registration completion

All19 stable IDs registered. Every preliminary observation is accounted for above. Recheck must confirm roles/relationships and assign exact evidence states separately for every ID; source links are relative to review_1_6 and end in truthful physical PDF page numbers. Neither candidate discovery nor reporting has a count boundary.
