# Mechanical evidence recheck — Workflow 1.6.2

Status: COMPLETE. Runtime agent: /root/evidence_recheck. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Exact scope: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, including every affected or corroborating location retained by the ledger, screen and three initial checkers. Covered stable IDs: 13/13. Every ID remains Pending Human Adjudication.

Authority: the supplied PDFs themselves, freshly read with direct Poppler pdftotext 25.03.0, plus direct-source CPU renders inspected visually for the numerical tables and both time-to-success figures. Existing evidence maps and checker transcriptions served as locators. No source or reused artifact was modified. The scope, review contract, ledger, screening decisions, checker findings and both source maps were consulted. Classification follows content, with precedence P_R > P_P > S_C > S_W. This record assigns evidence facts, not a human disposition.

Fresh derivatives, all below preprocessing/, use Poppler 25.03.0 on CPU: recheck-main-layout.txt (pdftotext -layout, main pp.1–11), recheck-protocol-layout.txt (pdftotext -layout, protocol pp.1–25), recheck-supplement-layout.txt (pdftotext -layout, support pp.1–13); recheck-main-p5.png, recheck-main-p6.png, recheck-main-p7.png (pdftoppm, 110 dpi); recheck-main-p8.png and recheck-supplement-p4.png (pdftoppm, 100 dpi). No OCR or fallback capability was required. Text records preserve PDF form-feed page boundaries. Every evidence link below points to its supplied PDF, not to a derivative.

The normative numerical precision comparison allows a half-unit interval for **every** displayed input, including displayed counts treated as continuous bounds for this check. Exact-count arithmetic is recorded separately as a sensitivity; it does not replace that allowance. CI-versus-test comparisons use the route A category 1 exemption and are not removed by a relative-gap threshold. Logical definitions and absent planned summaries have no numerical precision interval to compare.

| ID | Review domain | Relationship type | All relationships | Evidence state | Classification recheck |
|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R, P_P | reproduced | Ledger classification confirmed; protocol/form conflict independently supports P_P. |
| C002 | protocol_report | P_R | P_R | reproduced | Confirmed. |
| C003 | protocol_report | P_R | P_R | reproduced | Confirmed; two report documents agree on the published window. |
| C004 | protocol_report | P_R | P_R | reproduced | Confirmed; two report documents agree on the published duration definition. |
| C005 | protocol_report | P_R | P_R | reproduced | Confirmed; comparison concerns stopping rules, not a contradiction of realized calendar dates. |
| C006 | protocol_report | P_R | P_R | reproduced | Confirmed; planned summaries and displayed results are distinct quantities. |
| C007 | statistical_results | S_W | S_W | reproduced | Confirmed; calculation refined to allow every input its half-unit interval. |
| C008 | statistical_results | S_W | S_W | reproduced | Confirmed; both Other cells sustain the issue under the normative precision rule; two other examined cells do not independently exceed its threshold. |
| C009 | statistical_results | S_W | S_W | reproduced | Confirmed; all three printed zero-endpoint/test conflicts matched. |
| C010 | statistical_results | S_W | S_W | reproduced | Confirmed; checker S_C suggestion is not retained because the separately adjusted supplement only corroborates a possible ordering. |
| C011 | statistical_results | S_W | S_W | reproduced | Confirmed; difference CI and within-grade test compared, interaction test kept separate. |
| C012 | plan_material | P_P | P_P | reproduced | Confirmed; all conflicting clauses are PLAN, with main results only identifying affected context. |
| C013 | protocol_report | P_R | P_R | reproduced | Confirmed; original supplied protocol is the PLAN comparator, observed interim calculation is REPORT. |

No source value or source page in the stable registration required transcription correction. C007 and C008 require calculation refinements, described below, rather than a changed source transcription. There are 13 reproduced states, 0 reproduced_after_transcription_correction states and 0 not_reproduced states. Missing implementation definitions remain bounded human questions.

## C001 — Primary difficult-airway subgroup criteria

**Location found:** Yes, every retained location. PLAN [protocol p.13 §5.1, printed lines 427–431](../../../joi180054supp1_prod.pdf#page=13); REPORT [main p.1 Main Outcomes](../../../jama_driver_2018_oi_180054.pdf#page=1), [p.2 Patient Selection](../../../jama_driver_2018_oi_180054.pdf#page=2), [p.4 Figure 1 definition](../../../jama_driver_2018_oi_180054.pdf#page=4), [p.7 Table 3 primary row](../../../jama_driver_2018_oi_180054.pdf#page=7); PLAN [operational form p.7 item 3a](../../../joi180054supp2_prod.pdf#page=7) and [p.9 item 12](../../../joi180054supp2_prod.pdf#page=9).

**Source value/text matched:** Main pp.1,2,4 each define the primary difficult subgroup using facial trauma and airway obstruction or edema, alongside body fluids, obesity, short neck, small mandible, large tongue and cervical immobilization. Table 3 identifies 380 patients, successes 191/198 and 150/182, difference 14 percentage points (95% CI 8 to 20). Form item 12 lists facial trauma and airway obstruction/edema, with examples foreign body, angioedema, anaphylaxis and infection. Form item 3a separately lists Facial Trauma and Neck Trauma among indication choices.

**Comparator matched:** Protocol §5.1 includes facial **or neck** trauma and airway **edema**, alongside its other listed difficult characteristics, and expressly assigns that subgroup to the primary analysis. The form is a blank prospective measurement instrument, not results content. It independently differs from the original protocol list and thus supports a genuine plan-internal comparison.

**Consistency rule applicable:** Focus D, route B: an analysis-population membership rule is not reconciled by names alone when a criterion is omitted or broadened. The primary count/result is the affected quantity; no actual change in its patient membership is asserted.

**Logical comparison reproduced / display precision:** Neck trauma is an independent item in the original protocol, not in the report/form difficult-feature lists; obstruction without edema is included in the report/form literal list but not expressly in the original list. Common criteria and nearby exclusions do not explicitly equate these rule sets. Cervical immobility/immobilization and blood/vomit/body-fluid descriptions alone are not used to sustain the candidate. Display-precision intervals are not applicable to categorical inclusion rules; the matching result counts are context, not a discrepant arithmetic computation.

**Necessary inputs available:** Yes for the printed list comparison and affected primary result. **Exact missing inputs or definitions:** implemented primary-population criteria, any amendment/version mapping, and a cross-classification of neck-only trauma or obstruction-without-edema cases.

**Source-grounded alternative interpretation:** The operational form may reflect an amendment; affected features may all overlap with other qualifying features, or exclusions may remove some obstruction examples. The supplied lists and exclusions do not establish these possibilities for the primary cohort.

**Direct observation versus inferred explanation:** Direct observation is the three content lists and the Table 3 result. Changes in membership, reasons for amendment, or effect on success rates are not observed and are not inferred as facts.

**Exact remaining human question:** Which criteria defined the 380-patient primary subgroup, and how were neck trauma without another qualifying feature and airway obstruction without edema handled?

**Classification confirmation:** REPORT main result/definition versus PLAN protocol and PLAN operational form. Primary P_R; all relationships P_R, P_P; domain protocol_report. P_R takes precedence over P_P. No S_C is added for a blank form. **Classification ambiguity:** whether the form is an amended operational specification is not dated by the supplied material.

**Evidence state:** reproduced. **Determining recheck fact:** the source-confirmed criterion lists remain different for the independent neck-trauma and obstruction items; no supplied mapping reconciles them.

## C002 — Randomization stratification criteria

**Location found:** Yes. PLAN [protocol p.11 §4.1.1, lines 373–378](../../../joi180054supp1_prod.pdf#page=11); REPORT [main p.2 Randomization opening](../../../jama_driver_2018_oi_180054.pdf#page=2), [p.3 continuation](../../../jama_driver_2018_oi_180054.pdf#page=3), and [p.7 primary result](../../../jama_driver_2018_oi_180054.pdf#page=7).

**Source value/text matched:** Main pp.2–3 specify 1:1 assignment, blocks of 2,4,6,8,10, and two strata: obesity or cervical immobilization versus neither. The affected Table 3 primary result is 191/198 versus 150/182.

**Comparator matched:** Protocol p.11 specifies the same ratio and block sizes, but the first stratum is any cervical collar, gestalt obesity or apparent facial/neck trauma; the second has none of those characteristics.

**Consistency rule applicable:** Focus D, route B: compare the stated allocation stratification rule, not the separately postprocedural primary-subgroup definition.

**Logical comparison reproduced / display precision:** A patient with apparent facial/neck trauma and neither obesity nor immobilization is assigned to the first stratum by the protocol description and second by the report description. This is a logical rule example, not an assertion that such a patient occurred. Equal ratio/block sizes do not settle the third criterion. Half-unit intervals are not applicable to a categorical stratification rule; no discrepant copied number is alleged.

**Necessary inputs available:** Yes for the rule comparison. **Exact missing inputs or definitions:** implemented allocation schedule, any amended stratum specification and the overlap of trauma with retained criteria.

**Source-grounded alternative interpretation:** The report may abbreviate an implemented fuller rule, or the rule may have been amended. All trauma patients may have also met immobilization, but the sources do not state this.

**Direct observation versus inferred explanation:** Direct: the written strata omit/include trauma differently. Inferred possibilities: an amendment or abbreviated reporting. No allocation imbalance or treatment-effect consequence is inferred.

**Exact remaining human question:** Was facial/neck trauma included in the actual allocation schedule, and which approved stratification specification underlies the reported trial?

**Classification confirmation:** REPORT main randomization versus PLAN protocol randomization; primary/all P_R; domain protocol_report. The primary-results location identifies affected context and does not add S_W. **Classification ambiguity:** possible undisclosed specification version.

**Evidence state:** reproduced. **Determining recheck fact:** the direct-source allocation descriptions retain different independent trauma criteria.

## C003 — Hypoxemia ascertainment window

**Location found:** Yes. PLAN [protocol p.9 §2.2(1),(4), lines 304–325](../../../joi180054supp1_prod.pdf#page=9) and [p.10 §3.2, lines 340–344,353–354](../../../joi180054supp1_prod.pdf#page=10). REPORT [main p.1 hypoxemia context](../../../jama_driver_2018_oi_180054.pdf#page=1), [p.3 Measurements/Trial Outcomes](../../../jama_driver_2018_oi_180054.pdf#page=3), [p.7 Table 3 composite rows/note b](../../../jama_driver_2018_oi_180054.pdf#page=7), [p.9 Table 5 hypoxemia row/note b](../../../jama_driver_2018_oi_180054.pdf#page=9), [supplement p.2 composite rows](../../../joi180054supp2_prod.pdf#page=2) and [p.3 hypoxemia note](../../../joi180054supp2_prod.pdf#page=3).

**Source value/text matched:** Main measurements run until one minute following the end of the first attempt. Both main notes and supplement note define hypoxemia during or within one minute after completion of the attempt. The main defines attempt duration by insertion/removal of the blade. Thresholds are <90%, or an absolute fall >10% when beginning below 90%. Table 3 composites: difficult-airway 156/191 versus 123/177, overall 317/371 versus 282/366; supplement reproduces these arm data. Table 5 standalone hypoxemia: 47/371 versus 50/364; abstract gives rounded 13%/14%.

**Comparator matched:** Protocol defines the same threshold, but capture ends one minute after ETT cuff inflation. Measurement §3.2 specifies recording every 20 seconds to that endpoint and the lowest value; standalone secondary 4 uses the same hypoxemia definition as composite secondary 1.

**Consistency rule applicable:** Focus D, route A category 5: a defined component/window of planned standalone and composite outcomes changes its terminal anchor.

**Logical comparison reproduced / display precision:** One minute after cuff inflation and one minute after first-attempt completion are different written windows. The sources do not equate the terminal events; in a first-attempt failure cuff inflation need not occur at that attempt. Matching the threshold cannot prove equal ascertainment. Display-precision intervals cannot reconcile categorical timestamp anchors. Counts/percentages are matched affected-result locations, not an asserted event-count discrepancy.

**Necessary inputs available:** Yes for both window definitions and all retained affected cells. **Exact missing inputs or definitions:** applied capture window, paired cuff/blade timestamps, failure-case observation rule and any approved amendment.

**Source-grounded alternative interpretation:** The anchors may be close in successful first attempts or an operational revision may have been implemented; these are possible explanations, not supplied equalities.

**Direct observation versus inferred explanation:** Direct: the two stated endpoints and reported counts. Inferred: whether any patient's hypoxemia status changed; no numerical change is claimed.

**Exact remaining human question:** Which terminal anchor was used for standalone and composite hypoxemia ascertainment, including failed first attempts, and was the planned cuff-inflation window revised?

**Classification confirmation:** PLAN protocol versus REPORT main article and REPORT results supplement. Primary/all P_R; domain protocol_report. The two report sources agree, so no S_C conflict is added. **Classification ambiguity:** possible amendment not supplied.

**Evidence state:** reproduced. **Determining recheck fact:** direct-source window descriptions retain distinct terminal anchors despite matching saturation thresholds.

## C004 — Duration endpoint

**Location found:** Yes. PLAN [protocol p.9 §2.2(2), lines 315–317](../../../joi180054supp1_prod.pdf#page=9), [p.10 §3.2, lines 346–347](../../../joi180054supp1_prod.pdf#page=10), [p.19 §8.1, lines 657–660](../../../joi180054supp1_prod.pdf#page=19). REPORT [main p.1 secondary/median result](../../../jama_driver_2018_oi_180054.pdf#page=1), [p.3 Trial Outcomes](../../../jama_driver_2018_oi_180054.pdf#page=3), [p.4 time methods](../../../jama_driver_2018_oi_180054.pdf#page=4), [p.5 secondary time results](../../../jama_driver_2018_oi_180054.pdf#page=5), [p.7 Table 3 duration rows/note c](../../../jama_driver_2018_oi_180054.pdf#page=7), [p.8 Figure 2](../../../jama_driver_2018_oi_180054.pdf#page=8), [supplement p.2 duration rows](../../../joi180054supp2_prod.pdf#page=2), [p.3 duration note](../../../joi180054supp2_prod.pdf#page=3), and [p.4 eFigure 1](../../../joi180054supp2_prod.pdf#page=4).

**Source value/text matched:** Main p.3 and Table 3 note c define duration from blade insertion to blade removal. Main difficult-airway medians are 39 (IQR29–52) and 40 (27–63) seconds, difference −1 (95% CI −6 to 3), P=.50; overall 38 (29–51) and 36 (25–54), difference 1 (4 to −1), P=.24. Supplement retains medians, prints differences −1 (−6 to3), P=.31 and 1 (−1 to4), P=.95, and states physician clustering. Figures/captions supply first-attempt time-to-success analysis, difficult HR1.29 (1.04–1.60), log-rank P=.02; overall HR1.12 (.97–1.30), log-rank P=.12. Abstract includes duration medians 38/36, establishing key-secondary relevance.

**Comparator matched:** Protocol defines time to intubation for the first attempt from attempt beginning to ETT cuff inflation with the tube in the trachea; stopwatch measurement refers to that definition. §8.1 describes time-to-event summaries; its absent specific summaries are separately rechecked in C006.

**Consistency rule applicable:** Focus D, route A category 5: the reported planned-secondary duration uses a distinct terminal event and no supplied result is separately identified as the planned cuff-inflation measure.

**Logical comparison reproduced / display precision:** Cuff inflation with tracheal placement and blade removal are distinct operational events. In failure cases, blade removal can terminate an attempt without successful cuff inflation at that attempt. The report does not state equality of these timestamps. No rounding interval comparison applies to the categorical endpoint change; medians are not recomputed or changed. C010 separately records the printed interval ordering.

**Necessary inputs available:** Yes for definitions and affected results. **Exact missing inputs or definitions:** approved endpoint revision, paired cuff/blade times, and any separately reported cuff-inflation result.

**Source-grounded alternative interpretation:** A revised operational endpoint may have been approved, or successful-attempt timestamps may be close; neither is documented as equivalence in the supplied package.

**Direct observation versus inferred explanation:** Direct: endpoint texts, labels, medians and time analyses. Inferred only as possibilities: amendment or close timing. No direction or size of a resulting median change is inferred.

**Exact remaining human question:** Was cuff-inflation time amended to blade-removal duration, and which reported result or documented revision represents the originally planned endpoint?

**Classification confirmation:** PLAN protocol versus REPORT main and REPORT results supplement; primary/all P_R; domain protocol_report. Report documents agree on blade removal; no S_C conflict. **Classification ambiguity:** unspecified amendment history.

**Evidence state:** reproduced. **Determining recheck fact:** the supplied plan and report define duration using different terminal events, with no stated equivalence or identified planned-endpoint result.

## C005 — Enrollment stopping rule

**Location found:** Yes. PLAN [protocol p.19 §8.2, lines 665–674](../../../joi180054supp1_prod.pdf#page=19); REPORT [main p.1 study interval/final sample](../../../jama_driver_2018_oi_180054.pdf#page=1), [p.2 Trial Design dates](../../../jama_driver_2018_oi_180054.pdf#page=2), [p.3 Statistical Analysis](../../../jama_driver_2018_oi_180054.pdf#page=3), [p.4 Figure 1/final population](../../../jama_driver_2018_oi_180054.pdf#page=4), and [p.7 Table 3 primary size](../../../jama_driver_2018_oi_180054.pdf#page=7).

**Source value/text matched:** Main p.3 says the difficult-airway count was monitored and the trial stopped when more than 374 such patients enrolled. Main gives September 2016 through August 2017, final 757 overall and 380 difficult-airway patients, distributed 198/182 for primary analysis.

**Comparator matched:** Protocol targets 374 difficult-airway patients but specifies one calendar year or 1000 total patients, whichever first, followed by IRB discussion of extension if 374 difficult-airway patients were not reached.

**Consistency rule applicable:** Focus D, route B: compare explicit statistical accrual decision rules underlying the final primary sample, not an administrative date-copy difference.

**Logical comparison reproduced / display precision:** A first-boundary rule based on calendar year/overall count is not identical to a difficult-subgroup trigger >374. The realized 380/757 and trial months can be compatible with both; the recheck does not claim an observed date violates either boundary. Numerical rounding cannot reconcile different predicates, so no half-unit discrepancy is asserted for 374 versus380.

**Necessary inputs available:** Yes for printed rules and final samples. **Exact missing inputs or definitions:** exact closure trigger/date, joint rule implementation, amendments and any extension decision.

**Source-grounded alternative interpretation:** Count and calendar limits may have coincided, a subgroup target may have supplemented the limit, or a revision may have replaced it. These are not excluded by the dates but are not distinguished by the text.

**Direct observation versus inferred explanation:** Direct: the two differently described triggers. Not directly observed: a departure in realized closure or its effect on precision.

**Exact remaining human question:** Did the >374 difficult-airway trigger replace, supplement or coincide with the calendar-year/1000-patient rule, and which rule governed final closure?

**Classification confirmation:** REPORT main statistical stopping rule versus PLAN protocol stopping rule; primary/all P_R; domain protocol_report. **Classification ambiguity:** undisclosed chronology or joint rule.

**Evidence state:** reproduced. **Determining recheck fact:** the two explicit trigger descriptions remain distinct; actual enrollment dates alone do not identify their relationship.

## C006 — Planned Kaplan–Meier percentile and censoring summaries

**Location found:** Yes. PLAN [protocol p.9 §2.2(2)](../../../joi180054supp1_prod.pdf#page=9) and [p.19 §8.1, lines 657–660](../../../joi180054supp1_prod.pdf#page=19). REPORT [main p.1 duration result](../../../jama_driver_2018_oi_180054.pdf#page=1), [p.4 time methods](../../../jama_driver_2018_oi_180054.pdf#page=4), [p.5 secondary time results](../../../jama_driver_2018_oi_180054.pdf#page=5), [p.7 duration rows](../../../jama_driver_2018_oi_180054.pdf#page=7), [p.8 Figure 2](../../../jama_driver_2018_oi_180054.pdf#page=8), [supplement p.2 eTable 1](../../../joi180054supp2_prod.pdf#page=2), [p.3 notes](../../../joi180054supp2_prod.pdf#page=3), and [p.4 eFigure 1](../../../joi180054supp2_prod.pdf#page=4). Fresh full-report native text searches for percentile, censoring, Kaplan and duration were combined with visual inspection of both figures.

**Source value/text matched:** Main Table 3 and eTable 1 provide duration median/IQR, between-group contrasts with CIs, and P values. Main methods name Kaplan–Meier estimates, log-rank testing and unadjusted Cox analysis. Main secondary text and Figure 2 provide HR1.29 (1.04–1.60), P=.02; overall text/eFigure1 HR1.12 (.97–1.30), log-rank P=.12. Figures have censoring ticks, event curves and risk counts; neither has percentile confidence limits or a printed percentage censored.

**Comparator matched:** Protocol §8.1 expressly prescribes KM estimates of the 25th,50th,75th percentiles with two-sided 95% confidence intervals and percentage censored. §2.2(2) identifies the planned secondary time outcome; main abstract reports duration, making it key secondary under the scope definition.

**Consistency rule applicable:** Focus D, route A category 5: a prescribed key-secondary analysis summary is not reported in the supplied results.

**Logical comparison reproduced / display precision:** A sample median/IQR is not three KM percentile estimates each with a confidence interval; a contrast CI or HR CI estimates another quantity. A risk table or plotted censoring tick is not the specified percentage censored. No specified percentile-CI set or censoring percentage was found in either supplied REPORT source. Half-unit intervals do not apply to absent distinct summaries. This comparison remains independently applicable even if the endpoint-anchor issue C004 were reconciled.

**Necessary inputs available:** Yes for the explicit plan and complete supplied report locations; enough to reproduce the absence of the specified summaries. **Exact missing inputs or definitions:** KM percentile CIs, censoring percentages, the analysis dataset/event/censoring times, and a documented replacement specification.

**Source-grounded alternative interpretation:** The displayed curves/HR strategy may have superseded the summaries or the summaries may exist outside this package. The sources do not document either; no external search was performed.

**Direct observation versus inferred explanation:** Direct: explicit planned quantities and the distinct printed analyses. Inference is confined to possible replacement or external availability; actual production/nonproduction of the missing summaries is not established.

**Exact remaining human question:** Were the prescribed KM percentile confidence intervals and censoring summaries produced, and where are they reported or their replacement documented?

**Classification confirmation:** PLAN protocol versus REPORT main and REPORT supplement; primary/all P_R; domain protocol_report. No S_C is added because report documents do not conflict about the omitted quantities. **Classification ambiguity:** a replacement specification is not supplied.

**Evidence state:** reproduced. **Determining recheck fact:** the explicitly specified percentile CIs and censoring percentage are absent from the complete supplied REPORT displays, despite other time-to-event results being printed.

## C007 — Initial oxygen-saturation denominators and missingness

**Location found:** Yes, all within REPORT [main p.5 Table 1 headers, saturation median/threshold rows and footnote b](../../../jama_driver_2018_oi_180054.pdf#page=5), confirmed with a new direct-source image.

**Source value/text matched:** Arm totals 381/376; saturation median99 (95–100)/99 (96–100); <90% rows44/352 (13)/40/344 (12); <80% rows21/352 (6)/11/344 (3). Both threshold rows use the same352/344 denominators.

**Comparator matched:** Footnote b states43 missing initial oxygen saturations,19 bougie and24 tube, after describing initial vital signs as first readings after enrollment and before intubation. It separately gives missing heart rates61 (29/32) and systolic pressures185 (94/91). These are matched as separately labeled comparator counts, not substituted for saturation.

**Consistency rule applicable:** Focus A, route A category3: within-display counts, data denominators and explicit missingness for the same initial measurement must reconcile, allowing every displayed input its precision interval.

**Calculation reproduced / display precision:** Normative continuous bounds:381±.5 minus352±.5 yields [28,30] missing bougie;376±.5 minus344±.5 yields [31,33] missing tube. Compare with19±.5=[18.5,19.5] and24±.5=[23.5,24.5]. Gaps8.5 and6.5 imply relative discrepancies8.5/19=.44737 and6.5/24=.27083. Combining the four arm/observed-count input intervals yields total missing [59,63]; printed 43±.5=[42.5,43.5], gap15.5, relative15.5/43=.36047. All exceed.05. If the separately displayed19+24 is summed instead of printed 43, its [42,44] interval also does not overlap [59,63], gap15, relative15/43=.34884. These are the normative calculations.

Exact-count sensitivity:381−352=29,376−344=32,total61 versus19/24,total43. Singleton gaps10/19=.52632,8/24=.33333,18/43=.41860 match the checker arithmetic but are not the normative relaxed-input comparison. Event percentages themselves are rounding-compatible with their printed denominators. The candidate compares expressly printed missing counts rather than dividing the mismatch by larger observed-data denominators.

**Necessary inputs available:** Yes for both threshold rows, headers and missingness arithmetic. **Exact missing inputs or definitions:** any threshold-specific eligibility/exclusion rule and whether median/IQR and threshold rows intentionally use different subsets.

**Source-grounded alternative interpretation:** Threshold rows could have further exclusions or distinct usable observations. Their denominators equal arm totals minus missing heart rates, which suggests a possible alignment explanation but does not establish origin or a replacement value.

**Direct observation versus inferred explanation:** Direct:352/344 and19/24, plus their printed measurement labels. Inference: possible exclusion or alignment mechanism. No replacement denominator is assigned.

**Exact remaining human question:** Do352/344 describe all participants with initial saturation available; if so, how do they reconcile with43 missing (19/24), and if not, which additional rule defines those threshold-row denominators?

**Classification confirmation:** Both sides are REPORT content within the same main-table display; primary/all S_W; domain statistical_results. **Classification ambiguity:** none about roles; data-availability definition is unresolved.

**Evidence state:** reproduced. **Determining recheck fact:** even the normative half-unit allowance leaves every arm/total comparison above .05. Source values matched; the refinement is arithmetic precision handling, not transcription correction.

## C008 — Medical-indication percentage denominator pattern

**Location found:** Yes. REPORT [main p.5 Table 1 arm headers, medical parent and all six nested medical indication rows](../../../jama_driver_2018_oi_180054.pdf#page=5), confirmed visually from the supplied PDF.

**Source value/text matched:** Headers 381/376. Medical parents 318 (83)/315 (84). All nested rows: altered mental status 185 (49)/173 (46); cardiac arrest 32 (8)/23 (6); septic shock 21 (6)/27 (7); seizure 20 (5)/28 (7); asthma/COPD/heart failure/pneumonia 16 (5)/23 (7); Other 44 (14)/41 (13). All four originally cited percentage cells and all contextual rows were found and matched.

**Comparator matched:** Arm headers are the denominator basis being tested. Medical parent counts are an alternative conditional basis. Counts sum185+32+21+20+16+44=318 and173+23+27+28+23+41=315. Neighboring equally indented altered-mental-status percentages agree with arm totals, not medical totals.

**Consistency rule applicable:** Focus A, route A category3: a count, displayed denominator and percentage within one display are compared under the normative half-unit allowance for every input. All examined locations remain recorded, while only comparisons beyond the required threshold independently sustain the reproduced issue.

**Calculation reproduced / display precision:** For c/n×100, the normative recomputed interval is [100(c−.5)/(n+.5),100(c+.5)/(n−.5)]; printed p uses[p−.5,p+.5].

| Examined cell | Inputs c/n | Recomputed interval, % | Printed interval, % | Gap, percentage points | Relative gap / printed p | Independent support under normative rule |
|---|---|---|---|---|---|---|
| Bougie asthma/COPD/heart failure/pneumonia | 16/381 | [4.06291,4.33640] | [4.5,5.5] | .16360 | .03272 | At most.05; does not independently support inclusion. |
| Tube asthma/COPD/heart failure/pneumonia | 23/376 | [5.97610,6.25832] | [6.5,7.5] | .24168 | .03453 | At most.05; does not independently support inclusion. |
| Bougie medical Other | 44/381 | [11.40236,11.69514] | [13.5,14.5] | 1.80486 | .12892 | Greater than.05; supports the reproduced pattern. |
| Tube medical Other | 41/376 | [10.75697,11.05193] | [12.5,13.5] | 1.44807 | .11139 | Greater than.05; supports the reproduced pattern. |

Exact-count sensitivity: percentages4.19948,6.11702,11.54856,10.90426 versus printed 5,7,14,13 have gaps.30052,.38298,1.95144,1.59574 after percentage rounding; relative.06010,.05471,.13939,.12275. Those checker values are retained as exact-count sensitivity, not the normative calculation. The normative allowance narrows independently supporting cells to the two medical Other cells, and preserves one stable repeated issue. No source transcription changed.

Using medical parents instead gives16/318=5.031%,23/315=7.302%,44/318=13.836%,41/315=13.016%, reproducing the four displayed percentages. But185/318=58.176% and173/315=54.921% differ from printed 49%/46%; one uniform conditional reading cannot explain the nested column. This is an observed denominator-pattern compatibility, not a claimed production mechanism.

**Necessary inputs available:** Yes for all four cited cells, all nested comparators, counts and normative precision calculations. **Exact missing inputs or definitions:** row-specific percentage denominator definition and any intended change between marginal and conditional percentages.

**Source-grounded alternative interpretation:** Some rows may intentionally use the medical-only base while others use the arm base. The table supplies no statement defining that change. Medical indentation alone does not explain the different basis across equally nested rows.

**Direct observation versus inferred explanation:** Direct: printed counts, percentages, hierarchy and headers; the two Other cells remain above the precision threshold. Inferred explanation: denominator switching during preparation; intentional mixed reporting also remains possible.

**Exact remaining human question:** Which denominator applies to each medical indication row, especially Other, and are the percentages intended to use a common marginal or conditional base?

**Classification confirmation:** REPORT main Table 1 versus REPORT same-table counts/headers; primary/all S_W; domain statistical_results. **Classification ambiguity:** none about content roles; denominator convention is missing.

**Evidence state:** reproduced. **Determining recheck fact:** both medical Other cells remain beyond .05 under the mandated all-input rounding intervals. The two respiratory/cardiac cells are retained as examined context and do not independently sustain inclusion under that rule. This is a calculation refinement, not reproduced_after_transcription_correction.

## C009 — Three process confidence intervals and tests

**Location found:** Yes. REPORT [main p.6 Table 2 senior-resident/fellow, junior-resident and video-screen-during-passage rows](../../../jama_driver_2018_oi_180054.pdf#page=6); REPORT [p.4 statistical methods](../../../jama_driver_2018_oi_180054.pdf#page=4). All three numerical rows were visually confirmed on a new direct-source render.

**Source value/text matched:** Senior/fellow318/381 versus334/376, difference−5 (95% CI−10 to0), P=.03; junior57/381 versus37/376, difference5 (0 to10), P=.03; video during passage75/377 versus98/372, difference−6 (−12 to0), P=.04.

**Comparator matched:** Each P is in the same row as its 95% difference interval. Methods specify binary chi-square tests and two-sided .05, with 95% CIs. The screen-use row uses377/372 data denominators rather than overall381/376; this alignment was confirmed.

**Consistency rule applicable:** Focus B, route A category1: printed confidence interval containing the zero null versus significant two-sided test at.05.

**Comparison reproduced / display precision:** Each printed interval contains zero, while.03,.03,.04<.05. Diagnostic endpoint rounding intervals are[-10.5,−9.5]/[−.5,.5], [−.5,.5]/[9.5,10.5], and[−12.5,−11.5]/[−.5,.5]. Printed P intervals[.025,.035],[.025,.035],[.035,.045] remain below .05. An unrounded zero-adjacent endpoint could be nonzero, but the scope expressly exempts category1 conflicts from the rounding/relative-discrepancy exclusion; no relative-gap threshold is used here.

**Necessary inputs available:** Yes for printed CI/test compatibility at stated levels. **Exact missing inputs or definitions:** exact difference-CI construction and unrounded interval endpoints for each row. Those are not necessary to reproduce the printed conflict.

**Source-grounded alternative interpretation:** Unrounded limits may exclude zero or CIs/tests may use different inferential constructions; the checker diagnostics illustrate such possibilities but do not establish actual methods or replace the printed quantities.

**Direct observation versus inferred explanation:** Direct: three printed zero endpoints with significant P values. Inferred: rounding or differing-method explanations. The same displayed pattern is consolidated into one stable issue; all three occurrences remain explicit.

**Exact remaining human question:** What are the unrounded limits and CI constructions for these three process rows, and how should their displayed zero endpoints be read alongside P=.03,.03,.04?

**Classification confirmation:** All compared content is REPORT main article; primary/all S_W; domain statistical_results. **Classification ambiguity:** none about roles or relationships.

**Evidence state:** reproduced. **Determining recheck fact:** all three printed 95% intervals include zero while their corresponding printed P values are below the stated .05 threshold.

## C010 — All-patient duration interval ordering

**Location found:** Yes. REPORT [main p.7 Table 3 all-patient duration row](../../../jama_driver_2018_oi_180054.pdf#page=7) and [p.4 continuous-analysis methods](../../../jama_driver_2018_oi_180054.pdf#page=4); REPORT [supplement p.2 corresponding eTable 1 row](../../../joi180054supp2_prod.pdf#page=2) and [p.3 clustering explanation](../../../joi180054supp2_prod.pdf#page=3). The main interval was visually confirmed from the supplied PDF.

**Source value/text matched:** Main row medians 38 (29–51)/36 (25–54) seconds, difference1 (95% CI4 to−1), P=.24. Methods name Hodges–Lehmann differences for continuous variables and Wilcoxon rank-sum tests.

**Comparator matched:** Main-table difference intervals otherwise use ascending endpoints, including difficult duration−6 to3 and successful-attempt duration2 to7. Supplement corresponding row gives1 (−1 to4), P=.95; its note explicitly recalculates difference/interval/P columns for physician clustering while leaving arm columns unchanged.

**Consistency rule applicable:** Focus B, route B: a lower/upper confidence interval requires its first lower position not to exceed its second upper position; this determines extracted endpoint fields.

**Comparison reproduced / display precision:** The main prints4>−1. First endpoint half-unit interval[3.5,4.5] and second[−1.5,−.5] retain minimum descending separation3.5−(−.5)=4 seconds. Gap relative to first printed endpoint4 is4/4=1.00>.05. Point estimate interval[.5,1.5] lies between the unordered extrema, but cannot make the printed order lower-to-upper. Supplement[-1,4] corroborates a possible reorder, not a reconstruction of the main inferential method. No P conflict is created by comparing explicitly different analyses.

**Necessary inputs available:** Yes for the printed ordering and precision rule. **Exact missing inputs or definitions:** unrounded main Hodges–Lehmann limits, original duration ranks/ties and CI construction sufficient to identify the intended endpoints.

**Source-grounded alternative interpretation:** Limits may have been transposed; a descending reporting convention would require a definition absent from the otherwise ascending display. The adjusted supplement supports one possible ascending reading but does not establish the original main limits.

**Direct observation versus inferred explanation:** Direct:4 to−1 printed in the main. Inferred: transposition or another intended numeric reading; no final replacement is assigned.

**Exact remaining human question:** Which value is the lower and which the upper95% limit for the all-patient duration difference, and what original main-analysis output establishes them?

**Classification confirmation:** REPORT main interval versus REPORT main interval-order convention/methods; primary/all S_W; domain statistical_results. The supplement is REPORT but only corroborates an alternative ordering under a distinct analysis, so the checker suggestion to add S_C is not retained. Ledger S_W only is confirmed. **Classification ambiguity:** none about roles; original interval output remains absent.

**Evidence state:** reproduced. **Determining recheck fact:** direct-source endpoints are descending and every permitted half-unit value retains that ordering. No transcribed source value was changed.

## C011 — Grade-4 confidence interval and test

**Location found:** Yes. REPORT [main p.7 Table 3 Cormack–Lehane Grade4 row](../../../jama_driver_2018_oi_180054.pdf#page=7), confirmed visually; REPORT [main p.4 significance methods](../../../jama_driver_2018_oi_180054.pdf#page=4).

**Source value/text matched:** Bougie 3/3,100% (95% CI29 to100); tube 2/5,40% (5 to85); difference 60 percentage points (95% CI17 to100); within-grade P=.09; interaction P=.78.

**Comparator matched:** The.09 value is the within-grade comparison P in the same row as the difference CI;.78 is separately labeled interaction P and concerns another hypothesis. Methods give chi-square tests,95% CIs and two-sided .05.

**Consistency rule applicable:** Focus B, route A category1: difference CI excludes zero although its corresponding test is nonsignificant at the stated level.

**Comparison reproduced / display precision:** [17,100] excludes zero and.09>.05. Half-unit lower endpoint[16.5,17.5] remains positive; upper[99.5,100.5] also positive; P[.085,.095] remains>.05. Difference estimate[59.5,60.5] is within possible ordered endpoint ranges; containment and ordering are not the conflict. Route A category1 has no relative-gap exclusion. Crude count difference100×(3/3−2/5)=60 matches the estimate, but is not asserted to identify its actual CI construction.

**Necessary inputs available:** Yes for printed CI/test compatibility. **Exact missing inputs or definitions:** the difference-CI method/unrounded limits and any deliberate difference between inferential constructions. These do not prevent the observed comparison.

**Source-grounded alternative interpretation:** A CI from a different construction and chi-square P may yield this display; the checker normal-interval/Pearson diagnostics are compatible explanations but are not supplied method identities.

**Direct observation versus inferred explanation:** Direct: positive difference interval and nonsignificant within-grade P. Inferred: method mismatch or interval capping; no chosen method or replacement result is assigned.

**Exact remaining human question:** Which method produced the17-to100% CI and which produced P=.09, and how should their different null-value conclusions be interpreted?

**Classification confirmation:** REPORT main interval and REPORT same-row test/methods; primary/all S_W; domain statistical_results. **Classification ambiguity:** none; interaction remains a separate hypothesis.

**Evidence state:** reproduced. **Determining recheck fact:** the same-row interval excludes zero while P remains above .05 even after permitted display rounding.

## C012 — Primary missing-data recovery target inside the plan

**Location found:** Yes. PLAN [protocol p.8 §2.1, lines280–282](../../../joi180054supp1_prod.pdf#page=8), [p.9 primary continuation/secondary1, lines284–312](../../../joi180054supp1_prod.pdf#page=9), [p.20 §8.4.1 and §8.6.1, lines693–697,719–720](../../../joi180054supp1_prod.pdf#page=20), [p.21 §8.6.1, lines721–722](../../../joi180054supp1_prod.pdf#page=21). REPORT [main p.7 primary/composite rows](../../../jama_driver_2018_oi_180054.pdf#page=7) is affected-result context only.

**Source value/text matched:** Protocol §2.1 defines primary first-pass tracheal-intubation success and §8.4.1 primary analysis in the difficult-airway subset. Its missing-data clause begins “For the primary outcome” on p.20, and continues on p.21 with video review to determine first-pass success **without hypoxemia**, excluding if video is unavailable.

**Comparator matched:** Protocol p.9 explicitly assigns success without hypoxemia to secondary outcome1, requiring both first-attempt success and no hypoxemia. Primary success alone is separately defined. Main Table 3 context distinguishes primary191/198 versus150/182 from secondary composite156/191 versus123/177; these results do not demonstrate actual use of the recovery pathway.

**Consistency rule applicable:** Focus D, route A category5: a planned primary-analysis ascertainment step adds the component assigned to a separate secondary composite.

**Logical comparison reproduced / display precision:** Primary predicate is success; stated primary-recovery predicate is success AND no hypoxemia. They differ for a successful first attempt with hypoxemia. This is a logical illustration, not a claim such an observation was recovered. Rounding intervals are not applicable to outcome predicates; no numerical primary-result change is inferred.

**Necessary inputs available:** Yes for the internal clause comparison. **Exact missing inputs or definitions:** whether video was to recover both component values separately, how primary success was derived, whether any patient's forms triggered this pathway and any clarification/amendment.

**Source-grounded alternative interpretation:** Video may have supplied separate success and hypoxemia values, retaining success alone for primary analysis; the composite phrase may not reflect implementation. No supplied implementation statement resolves the targets.

**Direct observation versus inferred explanation:** Direct: an internally different recovery criterion inside the protocol. Inferred possibilities: dual-component reconstruction or wording origin. No claim is made about a recovered patient's classification or effect on published counts.

**Exact remaining human question:** Was primary video recovery intended to determine success alone or success without hypoxemia, how was primary status derived, and was that pathway used?

**Classification confirmation:** Every conflicting location is PLAN in the same protocol; primary/all P_P; domain plan_material. REPORT Table 3 merely identifies affected outcomes and does not add P_R. Ledger classification is confirmed. **Classification ambiguity:** implementation is unknown, not document role.

**Evidence state:** reproduced. **Determining recheck fact:** the primary missing-data clause expressly adds no-hypoxemia to a target otherwise defined as success alone and elsewhere labels that composite secondary.

## C013 — Interim analysis population and continuation basis

**Location found:** Yes. PLAN [protocol p.20 §8.4.1/§8.5, lines693–706](../../../joi180054supp1_prod.pdf#page=20), [p.21 §8.6.2, lines730–742](../../../joi180054supp1_prod.pdf#page=21). REPORT [supplement p.6 eAppendix1 observed interim rates/continuation](../../../joi180054supp2_prod.pdf#page=6); REPORT [main p.3 primary-population paragraph](../../../jama_driver_2018_oi_180054.pdf#page=3) corroborates population context. The prospective protocol quotation on supplement p.6 was also found and matched.

**Source value/text matched:** Supplement reports after 507 enrolled, bougie 250/257 (97%), tube 213/250 (85%), then states that using the above assumptions the trial was not stopped for futility. Main separates difficult-airway primary and overall secondary analyses.

**Comparator matched:** Original protocol defines primary analysis in the difficult-airway ITT subset and overall analysis as secondary. §8.6.2 specifies interim after 500 enrolled, primary outcome only, and projected1000 equally allocated with unchanged tube success and bougie success15 percentage points higher in the second half, capped at100%. The quoted rule on supplement p.6 matches the original source; the original is used as the PLAN comparator.

**Consistency rule applicable:** Focus D, route A category5: the documented continuation calculation displays the entire enrolled population and supplies no separately identified planned primary-subgroup interim analysis.

**Calculation/logical comparison reproduced / display precision:** Exact denominators 257+250=507 account for all reported interim enrollment. With all displayed inputs allowed half units, denominator sum[506,508] overlaps enrolled507±.5=[506.5,507.5], gap0: no numerical count mismatch is alleged. Bougie percentage recomputation [100×249.5/257.5,100×250.5/256.5]=[96.89320,97.66082] overlaps97±.5=[96.5,97.5]; tube [100×212.5/250.5,100×213.5/249.5]=[84.83034,85.57114] overlaps85±.5=[84.5,85.5]. Relative gaps are0. Exact rates97.276%/85.2% also reproduce displayed percentages. The unresolved comparison is population identification and its link to continuation, not percentage arithmetic or500 versus507 timing.

The source does not report difficult-airway denominators/rates for this interim. The final 757-patient cohort contains 380 difficult-airway participants; therefore all 507 interim patients cannot have belonged to that subgroup under unchanged classification and complete final inclusion. Such a possibility would require a changed classification or inclusion specification, which the supplied package does not document. A separate difficult-only interim calculation might have existed but is not established by this display. The registered observable issue is the all-enrolled result presented as the supporting continuation calculation while the specified primary-subgroup result is not identified. Exact projection/test reproduction is not possible without the difficult-subgroup data and exact futility test definition.

**Necessary inputs available:** Yes for the original primary/interim specifications, observed overall denominators and the continuation sentence. **Exact missing inputs or definitions:** interim difficult-airway patient counts/successes, any separately performed primary-only result, exact projection/futility test and approved population amendment.

**Source-grounded alternative interpretation:** Displayed overall rates may supplement an unreported primary-only calculation, or a documented revision may have changed the interim population or classification. The suggestion that all 507 interim patients met the unchanged final primary definition does not reconcile with the final subgroup size of 380. No primary-subgroup futility result or undocumented revision is inferred.

**Direct observation versus inferred explanation:** Direct: complete-cohort denominators, population specifications and stated continuation. Inferred: use of these rates instead of an unreported calculation; the record does not establish that no primary-only analysis occurred.

**Exact remaining human question:** Was futility assessed in the difficult-airway primary subset or all 507 enrolled patients, and what primary-subgroup result or documented amendment supports the continuation decision?

**Classification confirmation:** PLAN original protocol versus REPORT observed interim results; primary/all P_R; domain protocol_report. The p.6 prospective quotation corroborates the original plan; it is not a second conflicting plan or an additional S_W relationship. Main p.3 supplies REPORT affected-population context. **Classification ambiguity:** quoted prospective content is distinguished from adjacent observed results by its heading/tense; no extra relationship is assigned merely because both occur on one physical page.

**Evidence state:** reproduced. **Determining recheck fact:** the reported continuation display accounts for all 507 enrolled and does not identify the difficult-airway primary-subgroup interim calculation specified by the original protocol. The state records this supplied-source mismatch/omitted planned result, not a conclusion about actual unseen implementation.

## Scope closure and unresolved definitions

All assigned stable IDs and every retained pattern occurrence have direct-source location matches. Classification agrees with the ledger for all 13 IDs. C010 differs from the initial checker’s ancillary S_C suggestion for the explicitly recorded corroboration reason; C012 has only plan-internal conflicting content. C007/C008 carry normative all-input half-unit calculations and preserve exact-count sensitivities for provenance. C008 requires a report/ledger narrative refinement: independently supporting cells are the two medical Other cells; the two respiratory/cardiac cells remain examined locations with relative gaps at most .05 under the normative rule.

No source-confirmation unit remains uninspected. Missing definitions are implementation/amendment history (C001–C006,C012,C013), row denominator/availability rules (C007,C008), unrounded CI construction (C009,C011), original duration interval output/ranks (C010), specified KM percentile/censoring summaries (C006), and interim subgroup data/exact futility calculation (C013). These restrict source-grounded explanations and human interpretation, not the direct printed comparisons recorded above. No severity, disposition, replacement value or preferred analysis is assigned.
