# Inferential relationship inventory — statistical pass 1

Runtime ID: 01a12869-8c20-7fb1-b42a-ba626d66dcf5. Model/effort: gpt-6.1-sol/high; FRESH_SPAWN. Scope: all result-relevant inferential relationships mapped across five supplied documents and all 88 physical pages. Reconstructed independently from current main/support maps and supplied-source derivatives; no historical checker, candidate, or report conclusions read. Every relationship below is independent by population, test, threshold and outcome; repeated occurrences are joined only for the same result. Stable IDs S001–S120, 120 total. Pass 2 completed by three different fresh high-effort runtime agents; exact per-relationship results are retained in checkers/statistical_pass_2.md.

Source roles: DOC-001 main article REPORT; DOC-004 results supplement REPORT; DOC-002 protocol and DOC-003 SAP PLAN, including their historical results; DOC-005 availability statement REPORT, without an inferential result. Administrative dates, budgets, doses, eligibility thresholds and safety event counts are in numeric mapping; they do not create invented inferential results. All methods without observed result are retained in the definition register below.

## Source-grounded definition register

D1: Main article [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) Statistical Analyses and Outcomes; SAP [joi190039supp2_prod.pdf#page=8](../../../joi190039supp2_prod.pdf#page=8), with day renumbering [joi190039supp2_prod.pdf#page=4](../../../joi190039supp2_prod.pdf#page=4) and disclosed primary ITS/missing-day amendments [joi190039supp2_prod.pdf#page=9](../../../joi190039supp2_prod.pdf#page=9). Advanced neoplasm = CRC or advanced adenoma. Sensitivity TP/(TP+FN), specificity TN/(TN+FP), PPV TP/(TP+FP), NPV TN/(TN+FN). Arm contrast aspirin minus placebo from signed count differences. Units percent for arm estimates and percentage points for differences; no OR/RR/HR, standardized effect or person-time rate. Qualitative positivity includes positive/weakly positive per SAP p8.

D2: Main article p3 and SAP p8 name Agresti–Coull adjusted Wald proportion intervals and Agresti–Caffo difference intervals. Confidence level 95%. Significance two-sided P<.05; no multiple-test adjustment, secondary analyses exploratory. Neither source specifies the difference-P test formula, pooled versus unpooled variance, null variance, continuity correction for the actual result tests, exact statistic or SE. The protocol's continuity correction in sample-size calculation is not a definition of the result-P test. Exact P/CI inversion is therefore not authorized. Where a P is printed, its qualitative null-inclusion and narrative direction are checked, without claiming identical interval/test construction.

D3: All displayed diagnostic arm differences use paired population/test/cutoff/time identification within their own analysis population. Main Table 2 versus eTable 4 differ ITS versus PP; eTable 3 differs multi-day aggregation. Those values are not equality repetitions. Main p4 male PP sensitivity differences do match eTable 4. PPV/NPV counts in main Table 3 locate in main Table 2; eTable 5 locate in eTable 4. No raw data supplied.

D4: Optional Agresti–Caffo reconstruction is a **diagnostic approximation** of the named adjusted-Wald method, not a replacement reported analysis: qA=(xA+1)/(nA+2), qP=(xP+1)/(nP+2); diagnostic CI = 100[(qA−qP) ± 1.95996398454 sqrt(qA(1−qA)/(nA+2)+qP(1−qP)/(nP+2))]. Inputs and resulting endpoints are printed for every diagnostic table relationship. Direct containment/order/sign checks use source printed values, independent of this reconstruction. All diagnostic endpoints differ from printed endpoints by at most 0.12 percentage points; no method-identity inference is made for a P value. Differences in rounded percentages versus raw-count differences are retained.

D5: Main p3/p5 and eTable 6 p8 site sensitivity analysis: binomial GLMM with site random intercept; likelihood-ratio null SD=0 versus alternative SD>0. No LRT statistic/log likelihoods, boundary reference-distribution rule, fixed effects complete coding, estimator or SE is printed. A common mixture reference distribution is not inferred from convention. SD is a random-effect parameter, not a standard error or diagnostic percentage. The supplement caption denotes correct classification conditional on disease status. All table P values .16–.50 match main p5 range and non-significance. **No displayed P=0 exists in eTable 6.** SD=0 with P=.50 is source-correct and is not a P-display-zero case. DISPLAY_ZERO_NOT_CANDIDATE applies to coherent display-zero P values if encountered; none were found here.

D6: Sex interaction main p3 method/p4 result: binomial generalized linear model; SAP p9 logit link interaction coefficient, two-sided level .05. Main p4 supplies only pooled range P=.08–.49 across six sensitivity/specificity interactions. Each inferential contrast is separately tracked with the shared constraint; individual P, coefficients, statistic, SE, covariance, test type and degrees of freedom are absent. A significant within-stratum result does not itself contradict a non-significant interaction.

D7: Plan-only inferential methods without supplied estimates: SAP p7 chi-square OR Fisher baseline arm comparison; p8 LR definitions, total/partial AUC at specificity .8 and DeLong OR bootstrap, Agresti–Coull wording for numbers of tests/colonoscopies needed (transform not printed), binomial logit repeated-participant random intercept with arm/sex/test/day; day0-vs2/3/4 PP changes and multi-day combinations; p9 sex/age60/smoking/BMI25 strata, pathology strata and logit interaction, Fisher primary-test missingness independence. Protocol p28 ITT test performance at specificity>90%, sex/pathology/day contrasts and ROC. These are retained scope definitions, no result-specific CI/P compatibility claim is possible without estimates/inputs. Main site-intercept analysis is separately described D5; it is not assumed identical to planned repeated-participant GLMM. No omission of these definitions is justified by the lack of observed results.

D8: eTable 5 cutoff-unit header visibly reads only '[µg', whereas eTable 4 p6 prints '[µg Hb/g]'; native text contains displaced Hb/g] fragments. Candidate SP1-LABEL-2 pertains to the missing visible cutoff-label components, distinct from three missing PPV difference magnitudes. Applies to S073,S074,S075,S076,S077,S078,S079,S080,S081,S082,S083,S084,S085,S086,S087,S088,S089,S090. The definition µg Hb/g is corroborated by matching table definitions; this is a report-internal label relationship, not a conflicting PLAN relationship.


## Registered statistical result relationships

### Table 2: intention-to-screen; sample scheduled day 2

#### S001

- **Scope and source:** All; Quantitative; cutoff 10.2 µg Hb/g; Sensitivity; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 2, All row 1, Sensitivity difference/CI columns; role REPORT; map M046.
- **Exact printed inputs:** aspirin 40.2%; placebo 30.4%; difference 9.8 percentage points; 95% CI [-3.1, 22.2]. Numerator/denominator inputs aspirin 45/112, placebo 31/102, from the same row; full TP,FN,TN,FP A=(45,67,755,163), P=(31,71,807,103).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 9.7864. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -3.1<22.2; printed difference 9.8 lies within [-3.1, 22.2].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-3.0591, 22.2224]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** P=.14, main pp1 and4; qualitatively non-significant with CI spanning zero, matching stated two-sided .05 interpretation. Exact P/CI inversion unavailable (D2).
- **Matched occurrences:** Main p5 table matches main p4 result text, p1 abstract, p2 Key Points, p5 discussion and p6 conclusion; no conflicting repeated estimate/CI/P.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S002

- **Scope and source:** All; Quantitative; cutoff 10.2 µg Hb/g; Specificity; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 2, All row 1, Specificity difference/CI columns; role REPORT; map M047.
- **Exact printed inputs:** aspirin 82.2%; placebo 88.7%; difference -6.4 percentage points; 95% CI [-9.6, -3.2]. Numerator/denominator inputs aspirin 755/918, placebo 807/910, from the same row; full TP,FN,TN,FP A=(45,67,755,163), P=(31,71,807,103).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -6.4373. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -9.6<-3.2; printed difference -6.4 lies within [-9.6, -3.2].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-9.6431, -3.202]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** P=<.001, main p4; qualitatively significant with CI excluding zero, matching stated two-sided .05 interpretation. Exact P/CI inversion unavailable (D2).
- **Matched occurrences:** Main p5 table matches main p4 result text; no conflicting repeated estimate/CI/P.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S003

- **Scope and source:** All; Quantitative; cutoff 17 µg Hb/g; Sensitivity; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 2, All row 2, Sensitivity difference/CI columns; role REPORT; map M048.
- **Exact printed inputs:** aspirin 28.6%; placebo 22.5%; difference 6 percentage points; 95% CI [-5.7, 17.5]. Numerator/denominator inputs aspirin 32/112, placebo 23/102, from the same row; full TP,FN,TN,FP A=(32,80,842,76), P=(23,79,863,47).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 6.0224. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -5.7<17.5; printed difference 6 lies within [-5.7, 17.5].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-5.7432, 17.4841]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** P=.32, main pp1 and4; qualitatively non-significant with CI spanning zero, matching stated two-sided .05 interpretation. Exact P/CI inversion unavailable (D2).
- **Matched occurrences:** Main p5 table matches main p4 result text, p1 abstract, p2 Key Points, p5 discussion and p6 conclusion; no conflicting repeated estimate/CI/P.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S004

- **Scope and source:** All; Quantitative; cutoff 17 µg Hb/g; Specificity; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 2, All row 2, Specificity difference/CI columns; role REPORT; map M049.
- **Exact printed inputs:** aspirin 91.7%; placebo 94.8%; difference -3.1 percentage points; 95% CI [-5.4, -0.8]. Numerator/denominator inputs aspirin 842/918, placebo 863/910, from the same row; full TP,FN,TN,FP A=(32,80,842,76), P=(23,79,863,47).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -3.114. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -5.4<-0.8; printed difference -3.1 lies within [-5.4, -0.8].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-5.4091, -0.8037]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** P=.008, main p4; qualitatively significant with CI excluding zero, matching stated two-sided .05 interpretation. Exact P/CI inversion unavailable (D2).
- **Matched occurrences:** Main p5 table matches main p4 result text; no conflicting repeated estimate/CI/P.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S005

- **Scope and source:** All; Qualitative; cutoff 10.2 µg Hb/g; Sensitivity; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 2, All row 3, Sensitivity difference/CI columns; role REPORT; map M050.
- **Exact printed inputs:** aspirin 34.7%; placebo 22%; difference 12.7 percentage points; 95% CI [0.1, 24.7]. Numerator/denominator inputs aspirin 35/101, placebo 22/100, from the same row; full TP,FN,TN,FP A=(35,66,732,141), P=(22,78,798,71).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 12.6535. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints 0.1<24.7; printed difference 12.7 lies within [0.1, 24.7].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [0.1319, 24.673]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** P=.048, main p4; qualitatively significant with CI excluding zero, matching stated two-sided .05 interpretation. Exact P/CI inversion unavailable (D2).
- **Matched occurrences:** Main p5 table matches main p4 result text; no conflicting repeated estimate/CI/P.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S006

- **Scope and source:** All; Qualitative; cutoff 10.2 µg Hb/g; Specificity; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 2, All row 3, Specificity difference/CI columns; role REPORT; map M051.
- **Exact printed inputs:** aspirin 83.8%; placebo 91.8%; difference -8 percentage points; 95% CI [-11, -4.9]. Numerator/denominator inputs aspirin 732/873, placebo 798/869, from the same row; full TP,FN,TN,FP A=(35,66,732,141), P=(22,78,798,71).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -7.9809. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -11<-4.9; printed difference -8 lies within [-11, -4.9].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-11.0139, -4.9105]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** P=<.001, main p4; qualitatively significant with CI excluding zero, matching stated two-sided .05 interpretation. Exact P/CI inversion unavailable (D2).
- **Matched occurrences:** Main p5 table matches main p4 result text; no conflicting repeated estimate/CI/P.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S007

- **Scope and source:** Men; Quantitative; cutoff 10.2 µg Hb/g; Sensitivity; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 2, Men row 1, Sensitivity difference/CI columns; role REPORT; map M052.
- **Exact printed inputs:** aspirin 42.9%; placebo 27.8%; difference 15.1 percentage points; 95% CI [-1.6, 30.6]. Numerator/denominator inputs aspirin 33/77, placebo 15/54, from the same row; full TP,FN,TN,FP A=(33,44,360,90), P=(15,39,387,68).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 15.0794. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -1.6<30.6; printed difference 15.1 lies within [-1.6, 30.6].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-1.6332, 30.5663]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S008

- **Scope and source:** Men; Quantitative; cutoff 10.2 µg Hb/g; Specificity; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 2, Men row 1, Specificity difference/CI columns; role REPORT; map M053.
- **Exact printed inputs:** aspirin 80%; placebo 85.1%; difference -5.1 percentage points; 95% CI [-10, -0.1]. Numerator/denominator inputs aspirin 360/450, placebo 387/455, from the same row; full TP,FN,TN,FP A=(33,44,360,90), P=(15,39,387,68).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -5.0549. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -10<-0.1; printed difference -5.1 lies within [-10, -0.1].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-9.978, -0.0905]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S009

- **Scope and source:** Men; Quantitative; cutoff 17 µg Hb/g; Sensitivity; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 2, Men row 2, Sensitivity difference/CI columns; role REPORT; map M054.
- **Exact printed inputs:** aspirin 32.5%; placebo 24.1%; difference 8.4 percentage points; 95% CI [-7.5, 23.3]. Numerator/denominator inputs aspirin 25/77, placebo 13/54, from the same row; full TP,FN,TN,FP A=(25,52,408,42), P=(13,41,424,31).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 8.3935. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -7.5<23.3; printed difference 8.4 lies within [-7.5, 23.3].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-7.4504, 23.2732]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main p4 male sensitivity/specificity range endpoint matches this table value and CI; no conflicting repetition.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S010

- **Scope and source:** Men; Quantitative; cutoff 17 µg Hb/g; Specificity; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 2, Men row 2, Specificity difference/CI columns; role REPORT; map M055.
- **Exact printed inputs:** aspirin 90.7%; placebo 93.2%; difference -2.5 percentage points; 95% CI [-6.1, 1.1]. Numerator/denominator inputs aspirin 408/450, placebo 424/455, from the same row; full TP,FN,TN,FP A=(25,52,408,42), P=(13,41,424,31).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -2.5201. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -6.1<1.1; printed difference -2.5 lies within [-6.1, 1.1].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-6.0874, 1.0652]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main p4 male sensitivity/specificity range endpoint matches this table value and CI; no conflicting repetition.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S011

- **Scope and source:** Men; Qualitative; cutoff 10.2 µg Hb/g; Sensitivity; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 2, Men row 3, Sensitivity difference/CI columns; role REPORT; map M056.
- **Exact printed inputs:** aspirin 39.4%; placebo 21.8%; difference 17.6 percentage points; 95% CI [1.3, 32.6]. Numerator/denominator inputs aspirin 28/71, placebo 12/55, from the same row; full TP,FN,TN,FP A=(28,43,354,74), P=(12,43,400,48).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 17.6184. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints 1.3<32.6; printed difference 17.6 lies within [1.3, 32.6].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [1.2776, 32.5604]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main p4 male sensitivity/specificity range endpoint matches this table value and CI; no conflicting repetition.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S012

- **Scope and source:** Men; Qualitative; cutoff 10.2 µg Hb/g; Specificity; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 2, Men row 3, Specificity difference/CI columns; role REPORT; map M057.
- **Exact printed inputs:** aspirin 82.7%; placebo 89.3%; difference -6.6 percentage points; 95% CI [-11.2, -2]. Numerator/denominator inputs aspirin 354/428, placebo 400/448, from the same row; full TP,FN,TN,FP A=(28,43,354,74), P=(12,43,400,48).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -6.5754. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -11.2<-2; printed difference -6.6 lies within [-11.2, -2].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-11.1516, -1.9543]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main p4 male sensitivity/specificity range endpoint matches this table value and CI; no conflicting repetition.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S013

- **Scope and source:** Women; Quantitative; cutoff 10.2 µg Hb/g; Sensitivity; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 2, Women row 1, Sensitivity difference/CI columns; role REPORT; map M058.
- **Exact printed inputs:** aspirin 34.3%; placebo 33.3%; difference 1 percentage points; 95% CI [-19.1, 21.4]. Numerator/denominator inputs aspirin 12/35, placebo 16/48, from the same row; full TP,FN,TN,FP A=(12,23,395,73), P=(16,32,420,35).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 0.9524. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -19.1<21.4; printed difference 1 lies within [-19.1, 21.4].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-19.0891, 21.3594]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S014

- **Scope and source:** Women; Quantitative; cutoff 10.2 µg Hb/g; Specificity; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 2, Women row 1, Specificity difference/CI columns; role REPORT; map M059.
- **Exact printed inputs:** aspirin 84.4%; placebo 92.3%; difference -7.9 percentage points; 95% CI [-12, -3.8]. Numerator/denominator inputs aspirin 395/468, placebo 420/455, from the same row; full TP,FN,TN,FP A=(12,23,395,73), P=(16,32,420,35).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -7.906. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -12<-3.8; printed difference -7.9 lies within [-12, -3.8].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-11.9834, -3.7511]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S015

- **Scope and source:** Women; Quantitative; cutoff 17 µg Hb/g; Sensitivity; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 2, Women row 2, Sensitivity difference/CI columns; role REPORT; map M060.
- **Exact printed inputs:** aspirin 20%; placebo 20.8%; difference -0.8 percentage points; 95% CI [-17.9, 17.2]. Numerator/denominator inputs aspirin 7/35, placebo 10/48, from the same row; full TP,FN,TN,FP A=(7,28,434,34), P=(10,38,439,16).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -0.8333. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -17.9<17.2; printed difference -0.8 lies within [-17.9, 17.2].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-17.9222, 17.1654]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S016

- **Scope and source:** Women; Quantitative; cutoff 17 µg Hb/g; Specificity; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 2, Women row 2, Specificity difference/CI columns; role REPORT; map M061.
- **Exact printed inputs:** aspirin 92.7%; placebo 96.5%; difference -3.7 percentage points; 95% CI [-6.7, -0.8]. Numerator/denominator inputs aspirin 434/468, placebo 439/455, from the same row; full TP,FN,TN,FP A=(7,28,434,34), P=(10,38,439,16).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -3.7485. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -6.7<-0.8; printed difference -3.7 lies within [-6.7, -0.8].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-6.6669, -0.7869]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S017

- **Scope and source:** Women; Qualitative; cutoff 10.2 µg Hb/g; Sensitivity; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 2, Women row 3, Sensitivity difference/CI columns; role REPORT; map M062.
- **Exact printed inputs:** aspirin 23.3%; placebo 22.2%; difference 1.1 percentage points; 95% CI [-17.7, 20.9]. Numerator/denominator inputs aspirin 7/30, placebo 10/45, from the same row; full TP,FN,TN,FP A=(7,23,378,67), P=(10,35,398,23).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 1.1111. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -17.7<20.9; printed difference 1.1 lies within [-17.7, 20.9].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-17.6813, 20.8728]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S018

- **Scope and source:** Women; Qualitative; cutoff 10.2 µg Hb/g; Specificity; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 2, Women row 3, Specificity difference/CI columns; role REPORT; map M063.
- **Exact printed inputs:** aspirin 84.9%; placebo 94.5%; difference -9.6 percentage points; 95% CI [-13.5, -5.5]. Numerator/denominator inputs aspirin 378/445, placebo 398/421, from the same row; full TP,FN,TN,FP A=(7,23,378,67), P=(10,35,398,23).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -9.593. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -13.5<-5.5; printed difference -9.6 lies within [-13.5, -5.5].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-13.5319, -5.5457]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

### Table 3: intention-to-screen; sample scheduled day 2

#### S019

- **Scope and source:** All; Quantitative; cutoff 10.2 µg Hb/g; PPV; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3, All row 1, PPV difference/CI columns; role REPORT; map M064.
- **Exact printed inputs:** aspirin 21.6%; placebo 23.1%; difference -1.5 percentage points; 95% CI [-10.7, 7.4]. Numerator/denominator inputs aspirin 45/208, placebo 31/134, from Table 2 p5; full TP,FN,TN,FP A=(45,67,755,163), P=(31,71,807,103).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -1.4997. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -10.7<7.4; printed difference -1.5 lies within [-10.7, 7.4].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; PPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-10.6864, 7.4371]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with main Table 2 p5.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S020

- **Scope and source:** All; Quantitative; cutoff 10.2 µg Hb/g; NPV; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3, All row 1, NPV difference/CI columns; role REPORT; map M065.
- **Exact printed inputs:** aspirin 91.8%; placebo 91.9%; difference -0.1 percentage points; 95% CI [-2.7, 2.5]. Numerator/denominator inputs aspirin 755/822, placebo 807/878, from Table 2 p5; full TP,FN,TN,FP A=(45,67,755,163), P=(31,71,807,103).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -0.0643. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -2.7<2.5; printed difference -0.1 lies within [-2.7, 2.5].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; NPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-2.68, 2.5388]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with main Table 2 p5.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S021

- **Scope and source:** All; Quantitative; cutoff 17 µg Hb/g; PPV; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3, All row 2, PPV difference/CI columns; role REPORT; map M066.
- **Exact printed inputs:** aspirin 29.6%; placebo 32.9%; difference -3.2 percentage points; 95% CI [-17.2, 10.5]. Numerator/denominator inputs aspirin 32/108, placebo 23/70, from Table 2 p5; full TP,FN,TN,FP A=(32,80,842,76), P=(23,79,863,47).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -3.2275. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -17.2<10.5; printed difference -3.2 lies within [-17.2, 10.5].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; PPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-17.1861, 10.5195]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with main Table 2 p5.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S022

- **Scope and source:** All; Quantitative; cutoff 17 µg Hb/g; NPV; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3, All row 2, NPV difference/CI columns; role REPORT; map M067.
- **Exact printed inputs:** aspirin 91.3%; placebo 91.6%; difference -0.3 percentage points; 95% CI [-2.8, 2.3]. Numerator/denominator inputs aspirin 842/922, placebo 863/942, from Table 2 p5; full TP,FN,TN,FP A=(32,80,842,76), P=(23,79,863,47).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -0.2904. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -2.8<2.3; printed difference -0.3 lies within [-2.8, 2.3].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; NPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-2.8375, 2.2542]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with main Table 2 p5.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S023

- **Scope and source:** All; Qualitative; cutoff 10.2 µg Hb/g; PPV; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3, All row 3, PPV difference/CI columns; role REPORT; map M068.
- **Exact printed inputs:** aspirin 19.9%; placebo 23.7%; difference -3.8 percentage points; 95% CI [-14.4, 6.5]. Numerator/denominator inputs aspirin 35/176, placebo 22/93, from Table 2 p5; full TP,FN,TN,FP A=(35,66,732,141), P=(22,78,798,71).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -3.7696. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -14.4<6.5; printed difference -3.8 lies within [-14.4, 6.5].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; PPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-14.4269, 6.4553]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with main Table 2 p5.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S024

- **Scope and source:** All; Qualitative; cutoff 10.2 µg Hb/g; NPV; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3, All row 3, NPV difference/CI columns; role REPORT; map M069.
- **Exact printed inputs:** aspirin 91.7%; placebo 91.1%; difference 0.6 percentage points; 95% CI [-2.1, 3.3]. Numerator/denominator inputs aspirin 732/798, placebo 798/876, from Table 2 p5; full TP,FN,TN,FP A=(35,66,732,141), P=(22,78,798,71).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 0.6334. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -2.1<3.3; printed difference 0.6 lies within [-2.1, 3.3].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; NPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-2.0731, 3.3185]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with main Table 2 p5.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S025

- **Scope and source:** Men; Quantitative; cutoff 10.2 µg Hb/g; PPV; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3, Men row 1, PPV difference/CI columns; role REPORT; map M070.
- **Exact printed inputs:** aspirin 26.8%; placebo 18.1%; difference 8.8 percentage points; 95% CI [-3, 19.8]. Numerator/denominator inputs aspirin 33/123, placebo 15/83, from Table 2 p5; full TP,FN,TN,FP A=(33,44,360,90), P=(15,39,387,68).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 8.757. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -3<19.8; printed difference 8.8 lies within [-3, 19.8].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; PPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-3.0214, 19.7743]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with main Table 2 p5.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S026

- **Scope and source:** Men; Quantitative; cutoff 10.2 µg Hb/g; NPV; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3, Men row 1, NPV difference/CI columns; role REPORT; map M071.
- **Exact printed inputs:** aspirin 89.1%; placebo 90.8%; difference -1.7 percentage points; 95% CI [-5.9, 2.4]. Numerator/denominator inputs aspirin 360/404, placebo 387/426, from Table 2 p5; full TP,FN,TN,FP A=(33,44,360,90), P=(15,39,387,68).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -1.7362. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -5.9<2.4; printed difference -1.7 lies within [-5.9, 2.4].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; NPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-5.8524, 2.3765]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with main Table 2 p5.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S027

- **Scope and source:** Men; Quantitative; cutoff 17 µg Hb/g; PPV; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3, Men row 2, PPV difference/CI columns; role REPORT; map M072.
- **Exact printed inputs:** aspirin 37.3%; placebo 29.5%; difference 7.8 percentage points; 95% CI [-10.3, 24.8]. Numerator/denominator inputs aspirin 25/67, placebo 13/44, from Table 2 p5; full TP,FN,TN,FP A=(25,52,408,42), P=(13,41,424,31).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 7.768. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -10.3<24.8; printed difference 7.8 lies within [-10.3, 24.8].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; PPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-10.2905, 24.7833]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with main Table 2 p5.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S028

- **Scope and source:** Men; Quantitative; cutoff 17 µg Hb/g; NPV; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3, Men row 2, NPV difference/CI columns; role REPORT; map M073.
- **Exact printed inputs:** aspirin 88.7%; placebo 91.2%; difference -2.5 percentage points; 95% CI [-6.4, 1.4]. Numerator/denominator inputs aspirin 408/460, placebo 424/465, from Table 2 p5; full TP,FN,TN,FP A=(25,52,408,42), P=(13,41,424,31).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -2.4871. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -6.4<1.4; printed difference -2.5 lies within [-6.4, 1.4].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; NPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-6.3741, 1.4175]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with main Table 2 p5.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S029

- **Scope and source:** Men; [blank Test cell; proposed qualitative identity from count matches, not printed]; cutoff 10.2 µg Hb/g; PPV; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3, Men row 3, PPV difference/CI columns; role REPORT; map M074.
- **Exact printed inputs:** aspirin 27.5%; placebo 20%; difference 7.5 percentage points; 95% CI [-6.4, 20.2]. Numerator/denominator inputs aspirin 28/102, placebo 12/60, from Table 2 p5; full TP,FN,TN,FP A=(28,43,354,74), P=(12,43,400,48).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 7.451. Qualitative identity is conditional because the printed Test cell is blank.
- **Ordering and containment:** endpoints -6.4<20.2; printed difference 7.5 lies within [-6.4, 20.2].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; numeric direction agrees; Test label omission SP1-LABEL-1 affects row identity; PPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-6.3854, 20.2192]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with main Table 2 p5.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. Intended test label not printed; human question recorded in checker.
- **Candidate connection:** SP1-LABEL-1
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S030

- **Scope and source:** Men; [blank Test cell; proposed qualitative identity from count matches, not printed]; cutoff 10.2 µg Hb/g; NPV; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3, Men row 3, NPV difference/CI columns; role REPORT; map M075.
- **Exact printed inputs:** aspirin 89.2%; placebo 90.3%; difference -1.1 percentage points; 95% CI [-5.3, 3]. Numerator/denominator inputs aspirin 354/397, placebo 400/443, from Table 2 p5; full TP,FN,TN,FP A=(28,43,354,74), P=(12,43,400,48).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -1.1247. Qualitative identity is conditional because the printed Test cell is blank.
- **Ordering and containment:** endpoints -5.3<3; printed difference -1.1 lies within [-5.3, 3].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; numeric direction agrees; Test label omission SP1-LABEL-1 affects row identity; NPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-5.2797, 2.9999]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with main Table 2 p5.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. Intended test label not printed; human question recorded in checker.
- **Candidate connection:** SP1-LABEL-1
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S031

- **Scope and source:** Women; Quantitative; cutoff 10.2 µg Hb/g; PPV; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3, Women row 1, PPV difference/CI columns; role REPORT; map M076.
- **Exact printed inputs:** aspirin 14.1%; placebo 31.4%; difference -17.3 percentage points; 95% CI [-31.8, -2.5]. Numerator/denominator inputs aspirin 12/85, placebo 16/51, from Table 2 p5; full TP,FN,TN,FP A=(12,23,395,73), P=(16,32,420,35).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -17.2549. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -31.8<-2.5; printed difference -17.3 lies within [-31.8, -2.5].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; PPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-31.7628, -2.5031]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with main Table 2 p5.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S032

- **Scope and source:** Women; Quantitative; cutoff 10.2 µg Hb/g; NPV; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3, Women row 1, NPV difference/CI columns; role REPORT; map M077.
- **Exact printed inputs:** aspirin 94.5%; placebo 92.9%; difference 1.6 percentage points; 95% CI [-1.7, 4.8]. Numerator/denominator inputs aspirin 395/418, placebo 420/452, from Table 2 p5; full TP,FN,TN,FP A=(12,23,395,73), P=(16,32,420,35).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 1.5773. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -1.7<4.8; printed difference 1.6 lies within [-1.7, 4.8].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; NPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-1.7061, 4.815]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with main Table 2 p5.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S033

- **Scope and source:** Women; Quantitative; cutoff 17 µg Hb/g; PPV; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3, Women row 2, PPV difference/CI columns; role REPORT; map M078.
- **Exact printed inputs:** aspirin 17.1%; placebo 38.5%; difference -21.4 percentage points; 95% CI [-42.2, 0.8]. Numerator/denominator inputs aspirin 7/41, placebo 10/26, from Table 2 p5; full TP,FN,TN,FP A=(7,28,434,34), P=(10,38,439,16).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -21.3884. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -42.2<0.8; printed difference -21.4 lies within [-42.2, 0.8].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; PPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-42.1874, 0.8253]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with main Table 2 p5.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S034

- **Scope and source:** Women; Quantitative; cutoff 17 µg Hb/g; NPV; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3, Women row 2, NPV difference/CI columns; role REPORT; map M079.
- **Exact printed inputs:** aspirin 93.9%; placebo 92%; difference 1.9 percentage points; 95% CI [-1.4, 5.2]. Numerator/denominator inputs aspirin 434/462, placebo 439/477, from Table 2 p5; full TP,FN,TN,FP A=(7,28,434,34), P=(10,38,439,16).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 1.9059. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -1.4<5.2; printed difference 1.9 lies within [-1.4, 5.2].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; NPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-1.4018, 5.1857]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with main Table 2 p5.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S035

- **Scope and source:** Women; Qualitative; cutoff 10.2 µg Hb/g; PPV; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3, Women row 3, PPV difference/CI columns; role REPORT; map M080.
- **Exact printed inputs:** aspirin 9.5%; placebo 30.3%; difference -20.8 percentage points; 95% CI [-37.8, -4]. Numerator/denominator inputs aspirin 7/74, placebo 10/33, from Table 2 p5; full TP,FN,TN,FP A=(7,23,378,67), P=(10,35,398,23).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -20.8436. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -37.8<-4; printed difference -20.8 lies within [-37.8, -4].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; PPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-37.7587, -4.0458]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with main Table 2 p5.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S036

- **Scope and source:** Women; Qualitative; cutoff 10.2 µg Hb/g; NPV; intention-to-screen; sample scheduled day 2; [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5), Table 3, Women row 3, NPV difference/CI columns; role REPORT; map M081.
- **Exact printed inputs:** aspirin 94.3%; placebo 91.9%; difference 2.3 percentage points; 95% CI [-1.1, 5.8]. Numerator/denominator inputs aspirin 378/401, placebo 398/433, from Table 2 p5; full TP,FN,TN,FP A=(7,23,378,67), P=(10,35,398,23).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 2.3475. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -1.1<5.8; printed difference 2.3 lies within [-1.1, 5.8].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; NPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-1.1497, 5.7907]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with main Table 2 p5.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

### eTable 3: combined samples scheduled days 2, 3, 4; up to three samples

#### S037

- **Scope and source:** All; Quantitative; cutoff 10.2 µg Hb/g; Sensitivity; combined samples scheduled days 2, 3, 4; up to three samples; [joi190039supp3_prod.pdf#page=5](../../../joi190039supp3_prod.pdf#page=5), eTable 3, All row 1, Sensitivity difference/CI columns; role REPORT; map B042.
- **Exact printed inputs:** aspirin 55.8%; placebo 45.8%; difference 10 percentage points; 95% CI [-3.3, 22.8]. Numerator/denominator inputs aspirin 63/113, placebo 49/107, from the same row; full TP,FN,TN,FP A=(63,50,685,261), P=(49,58,774,161).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 9.9578. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -3.3<22.8; printed difference 10 lies within [-3.3, 22.8].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-3.2558, 22.8171]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S038

- **Scope and source:** All; Quantitative; cutoff 10.2 µg Hb/g; Specificity; combined samples scheduled days 2, 3, 4; up to three samples; [joi190039supp3_prod.pdf#page=5](../../../joi190039supp3_prod.pdf#page=5), eTable 3, All row 1, Specificity difference/CI columns; role REPORT; map B042.
- **Exact printed inputs:** aspirin 72.4%; placebo 82.8%; difference -10.4 percentage points; 95% CI [-14.1, -6.6]. Numerator/denominator inputs aspirin 685/946, placebo 774/935, from the same row; full TP,FN,TN,FP A=(63,50,685,261), P=(49,58,774,161).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -10.3706. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -14.1<-6.6; printed difference -10.4 lies within [-14.1, -6.6].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-14.0851, -6.6107]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S039

- **Scope and source:** All; Quantitative; cutoff 17 µg Hb/g; Sensitivity; combined samples scheduled days 2, 3, 4; up to three samples; [joi190039supp3_prod.pdf#page=5](../../../joi190039supp3_prod.pdf#page=5), eTable 3, All row 2, Sensitivity difference/CI columns; role REPORT; map B043.
- **Exact printed inputs:** aspirin 38.9%; placebo 32.7%; difference 6.2 percentage points; 95% CI [-6.4, 18.7]. Numerator/denominator inputs aspirin 44/113, placebo 35/107, from the same row; full TP,FN,TN,FP A=(44,69,816,130), P=(35,72,852,83).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 6.2278. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -6.4<18.7; printed difference 6.2 lies within [-6.4, 18.7].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-6.4477, 18.6535]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S040

- **Scope and source:** All; Quantitative; cutoff 17 µg Hb/g; Specificity; combined samples scheduled days 2, 3, 4; up to three samples; [joi190039supp3_prod.pdf#page=5](../../../joi190039supp3_prod.pdf#page=5), eTable 3, All row 2, Specificity difference/CI columns; role REPORT; map B043.
- **Exact printed inputs:** aspirin 86.3%; placebo 91.1%; difference -4.9 percentage points; 95% CI [-7.7, -2]. Numerator/denominator inputs aspirin 816/946, placebo 852/935, from the same row; full TP,FN,TN,FP A=(44,69,816,130), P=(35,72,852,83).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -4.8651. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -7.7<-2; printed difference -4.9 lies within [-7.7, -2].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-7.7124, -1.9952]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S041

- **Scope and source:** All; Qualitative; cutoff 10.2 µg Hb/g; Sensitivity; combined samples scheduled days 2, 3, 4; up to three samples; [joi190039supp3_prod.pdf#page=5](../../../joi190039supp3_prod.pdf#page=5), eTable 3, All row 3, Sensitivity difference/CI columns; role REPORT; map B044.
- **Exact printed inputs:** aspirin 47.7%; placebo 32.4%; difference 15.3 percentage points; 95% CI [2.3, 27.8]. Numerator/denominator inputs aspirin 53/111, placebo 35/108, from the same row; full TP,FN,TN,FP A=(53,58,714,222), P=(35,73,779,146).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 15.3403. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints 2.3<27.8; printed difference 15.3 lies within [2.3, 27.8].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [2.3439, 27.7768]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S042

- **Scope and source:** All; Qualitative; cutoff 10.2 µg Hb/g; Specificity; combined samples scheduled days 2, 3, 4; up to three samples; [joi190039supp3_prod.pdf#page=5](../../../joi190039supp3_prod.pdf#page=5), eTable 3, All row 3, Specificity difference/CI columns; role REPORT; map B044.
- **Exact printed inputs:** aspirin 76.3%; placebo 84.2%; difference -7.9 percentage points; 95% CI [-11.5, -4.3]. Numerator/denominator inputs aspirin 714/936, placebo 779/925, from the same row; full TP,FN,TN,FP A=(53,58,714,222), P=(35,73,779,146).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -7.9342. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -11.5<-4.3; printed difference -7.9 lies within [-11.5, -4.3].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-11.5151, -4.3176]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S043

- **Scope and source:** Men; Quantitative; cutoff 10.2 µg Hb/g; Sensitivity; combined samples scheduled days 2, 3, 4; up to three samples; [joi190039supp3_prod.pdf#page=5](../../../joi190039supp3_prod.pdf#page=5), eTable 3, Men row 1, Sensitivity difference/CI columns; role REPORT; map B045.
- **Exact printed inputs:** aspirin 59.7%; placebo 48.3%; difference 11.5 percentage points; 95% CI [-5.5, 27.8]. Numerator/denominator inputs aspirin 46/77, placebo 28/58, from the same row; full TP,FN,TN,FP A=(46,31,311,148), P=(28,30,362,102).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 11.4644. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -5.5<27.8; printed difference 11.5 lies within [-5.5, 27.8].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-5.4849, 27.8056]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S044

- **Scope and source:** Men; Quantitative; cutoff 10.2 µg Hb/g; Specificity; combined samples scheduled days 2, 3, 4; up to three samples; [joi190039supp3_prod.pdf#page=5](../../../joi190039supp3_prod.pdf#page=5), eTable 3, Men row 1, Specificity difference/CI columns; role REPORT; map B045.
- **Exact printed inputs:** aspirin 67.8%; placebo 78%; difference -10.3 percentage points; 95% CI [-15.9, -4.5]. Numerator/denominator inputs aspirin 311/459, placebo 362/464, from the same row; full TP,FN,TN,FP A=(46,31,311,148), P=(28,30,362,102).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -10.2613. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -15.9<-4.5; printed difference -10.3 lies within [-15.9, -4.5].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-15.912, -4.5241]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S045

- **Scope and source:** Men; Quantitative; cutoff 17 µg Hb/g; Sensitivity; combined samples scheduled days 2, 3, 4; up to three samples; [joi190039supp3_prod.pdf#page=5](../../../joi190039supp3_prod.pdf#page=5), eTable 3, Men row 2, Sensitivity difference/CI columns; role REPORT; map B046.
- **Exact printed inputs:** aspirin 44.2%; placebo 37.9%; difference 6.2 percentage points; 95% CI [-10.5, 22.4]. Numerator/denominator inputs aspirin 34/77, placebo 22/58, from the same row; full TP,FN,TN,FP A=(34,43,384,75), P=(22,36,408,56).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 6.2248. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -10.5<22.4; printed difference 6.2 lies within [-10.5, 22.4].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-10.5017, 22.4427]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S046

- **Scope and source:** Men; Quantitative; cutoff 17 µg Hb/g; Specificity; combined samples scheduled days 2, 3, 4; up to three samples; [joi190039supp3_prod.pdf#page=5](../../../joi190039supp3_prod.pdf#page=5), eTable 3, Men row 2, Specificity difference/CI columns; role REPORT; map B046.
- **Exact printed inputs:** aspirin 83.7%; placebo 87.9%; difference -4.3 percentage points; 95% CI [-8.8, 0.3]. Numerator/denominator inputs aspirin 384/459, placebo 408/464, from the same row; full TP,FN,TN,FP A=(34,43,384,75), P=(22,36,408,56).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -4.2709. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -8.8<0.3; printed difference -4.3 lies within [-8.8, 0.3].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-8.7622, 0.2539]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S047

- **Scope and source:** Men; Qualitative; cutoff 10.2 µg Hb/g; Sensitivity; combined samples scheduled days 2, 3, 4; up to three samples; [joi190039supp3_prod.pdf#page=5](../../../joi190039supp3_prod.pdf#page=5), eTable 3, Men row 3, Sensitivity difference/CI columns; role REPORT; map B047.
- **Exact printed inputs:** aspirin 54.7%; placebo 32.2%; difference 22.5 percentage points; 95% CI [5.6, 38]. Numerator/denominator inputs aspirin 41/75, placebo 19/59, from the same row; full TP,FN,TN,FP A=(41,34,343,111), P=(19,40,372,89).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 22.4633. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints 5.6<38; printed difference 22.5 lies within [5.6, 38].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [5.5576, 37.9595]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S048

- **Scope and source:** Men; Qualitative; cutoff 10.2 µg Hb/g; Specificity; combined samples scheduled days 2, 3, 4; up to three samples; [joi190039supp3_prod.pdf#page=5](../../../joi190039supp3_prod.pdf#page=5), eTable 3, Men row 3, Specificity difference/CI columns; role REPORT; map B047.
- **Exact printed inputs:** aspirin 75.6%; placebo 80.7%; difference -5.1 percentage points; 95% CI [-10.5, 0.2]. Numerator/denominator inputs aspirin 343/454, placebo 372/461, from the same row; full TP,FN,TN,FP A=(41,34,343,111), P=(19,40,372,89).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -5.1435. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -10.5<0.2; printed difference -5.1 lies within [-10.5, 0.2].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-10.471, 0.2251]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S049

- **Scope and source:** Women; Quantitative; cutoff 10.2 µg Hb/g; Sensitivity; combined samples scheduled days 2, 3, 4; up to three samples; [joi190039supp3_prod.pdf#page=5](../../../joi190039supp3_prod.pdf#page=5), eTable 3, Women row 1, Sensitivity difference/CI columns; role REPORT; map B048.
- **Exact printed inputs:** aspirin 47.2%; placebo 42.9%; difference 4.4 percentage points; 95% CI [-16.7, 25.1]. Numerator/denominator inputs aspirin 17/36, placebo 21/49, from the same row; full TP,FN,TN,FP A=(17,19,374,113), P=(21,28,412,59).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 4.3651. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -16.7<25.1; printed difference 4.4 lies within [-16.7, 25.1].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-16.6683, 25.1306]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S050

- **Scope and source:** Women; Quantitative; cutoff 10.2 µg Hb/g; Specificity; combined samples scheduled days 2, 3, 4; up to three samples; [joi190039supp3_prod.pdf#page=5](../../../joi190039supp3_prod.pdf#page=5), eTable 3, Women row 1, Specificity difference/CI columns; role REPORT; map B048.
- **Exact printed inputs:** aspirin 76.8%; placebo 87.5%; difference -10.7 percentage points; 95% CI [-15.4, -5.8]. Numerator/denominator inputs aspirin 374/487, placebo 412/471, from the same row; full TP,FN,TN,FP A=(17,19,374,113), P=(21,28,412,59).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -10.6767. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -15.4<-5.8; printed difference -10.7 lies within [-15.4, -5.8].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-15.4279, -5.8279]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S051

- **Scope and source:** Women; Quantitative; cutoff 17 µg Hb/g; Sensitivity; combined samples scheduled days 2, 3, 4; up to three samples; [joi190039supp3_prod.pdf#page=5](../../../joi190039supp3_prod.pdf#page=5), eTable 3, Women row 2, Sensitivity difference/CI columns; role REPORT; map B049.
- **Exact printed inputs:** aspirin 27.8%; placebo 26.5%; difference 1.2 percentage points; 95% CI [-17.4, 20.4]. Numerator/denominator inputs aspirin 10/36, placebo 13/49, from the same row; full TP,FN,TN,FP A=(10,26,432,55), P=(13,36,444,27).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 1.2472. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -17.4<20.4; printed difference 1.2 lies within [-17.4, 20.4].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-17.4227, 20.4155]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S052

- **Scope and source:** Women; Quantitative; cutoff 17 µg Hb/g; Specificity; combined samples scheduled days 2, 3, 4; up to three samples; [joi190039supp3_prod.pdf#page=5](../../../joi190039supp3_prod.pdf#page=5), eTable 3, Women row 2, Specificity difference/CI columns; role REPORT; map B049.
- **Exact printed inputs:** aspirin 88.7%; placebo 94.3%; difference -5.6 percentage points; 95% CI [-9.1, -2]. Numerator/denominator inputs aspirin 432/487, placebo 444/471, from the same row; full TP,FN,TN,FP A=(10,26,432,55), P=(13,36,444,27).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -5.5612. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -9.1<-2; printed difference -5.6 lies within [-9.1, -2].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-9.0663, -1.9983]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S053

- **Scope and source:** Women; Qualitative; cutoff 10.2 µg Hb/g; Sensitivity; combined samples scheduled days 2, 3, 4; up to three samples; [joi190039supp3_prod.pdf#page=5](../../../joi190039supp3_prod.pdf#page=5), eTable 3, Women row 3, Sensitivity difference/CI columns; role REPORT; map B050.
- **Exact printed inputs:** aspirin 33.3%; placebo 32.7%; difference 0.7 percentage points; 95% CI [-19, 20.7]. Numerator/denominator inputs aspirin 12/36, placebo 16/49, from the same row; full TP,FN,TN,FP A=(12,24,371,111), P=(16,33,407,57).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 0.6803. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -19<20.7; printed difference 0.7 lies within [-19, 20.7].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-18.9951, 20.7495]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S054

- **Scope and source:** Women; Qualitative; cutoff 10.2 µg Hb/g; Specificity; combined samples scheduled days 2, 3, 4; up to three samples; [joi190039supp3_prod.pdf#page=5](../../../joi190039supp3_prod.pdf#page=5), eTable 3, Women row 3, Specificity difference/CI columns; role REPORT; map B050.
- **Exact printed inputs:** aspirin 77%; placebo 87.7%; difference -10.7 percentage points; 95% CI [-15.5, -5.9]. Numerator/denominator inputs aspirin 371/482, placebo 407/464, from the same row; full TP,FN,TN,FP A=(12,24,371,111), P=(16,33,407,57).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -10.7446. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -15.5<-5.9; printed difference -10.7 lies within [-15.5, -5.9].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-15.5003, -5.888]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

### eTable 4: per-protocol; sample collected exactly day 2

#### S055

- **Scope and source:** All; Quantitative; cutoff 10.2 µg Hb/g; Sensitivity; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=6](../../../joi190039supp3_prod.pdf#page=6), eTable 4, All row 1, Sensitivity difference/CI columns; role REPORT; map B051.
- **Exact printed inputs:** aspirin 42.9%; placebo 29.1%; difference 13.8 percentage points; 95% CI [-0.1, 27.1]. Numerator/denominator inputs aspirin 42/98, placebo 25/86, from the same row; full TP,FN,TN,FP A=(42,56,635,136), P=(25,61,691,85).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 13.7874. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -0.1<27.1; printed difference 13.8 lies within [-0.1, 27.1].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-0.1478, 27.0568]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S056

- **Scope and source:** All; Quantitative; cutoff 10.2 µg Hb/g; Specificity; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=6](../../../joi190039supp3_prod.pdf#page=6), eTable 4, All row 1, Specificity difference/CI columns; role REPORT; map B051.
- **Exact printed inputs:** aspirin 82.4%; placebo 89%; difference -6.7 percentage points; 95% CI [-10.1, -3.2]. Numerator/denominator inputs aspirin 635/771, placebo 691/776, from the same row; full TP,FN,TN,FP A=(42,56,635,136), P=(25,61,691,85).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -6.6858. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -10.1<-3.2; printed difference -6.7 lies within [-10.1, -3.2].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-10.1479, -3.1905]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S057

- **Scope and source:** All; Quantitative; cutoff 17 µg Hb/g; Sensitivity; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=6](../../../joi190039supp3_prod.pdf#page=6), eTable 4, All row 2, Sensitivity difference/CI columns; role REPORT; map B052.
- **Exact printed inputs:** aspirin 29.6%; placebo 20.9%; difference 8.7 percentage points; 95% CI [-4, 20.8]. Numerator/denominator inputs aspirin 29/98, placebo 18/86, from the same row; full TP,FN,TN,FP A=(29,69,704,67), P=(18,68,735,41).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 8.6616. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -4<20.8; printed difference 8.7 lies within [-4, 20.8].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-4.0236, 20.8418]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S058

- **Scope and source:** All; Quantitative; cutoff 17 µg Hb/g; Specificity; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=6](../../../joi190039supp3_prod.pdf#page=6), eTable 4, All row 2, Specificity difference/CI columns; role REPORT; map B052.
- **Exact printed inputs:** aspirin 91.3%; placebo 94.7%; difference -3.4 percentage points; 95% CI [-5.9, -0.8]. Numerator/denominator inputs aspirin 704/771, placebo 735/776, from the same row; full TP,FN,TN,FP A=(29,69,704,67), P=(18,68,735,41).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -3.4065. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -5.9<-0.8; printed difference -3.4 lies within [-5.9, -0.8].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-5.9497, -0.8472]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S059

- **Scope and source:** All; Qualitative; cutoff 10.2 µg Hb/g; Sensitivity; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=6](../../../joi190039supp3_prod.pdf#page=6), eTable 4, All row 3, Sensitivity difference/CI columns; role REPORT; map B053.
- **Exact printed inputs:** aspirin 34.9%; placebo 22.6%; difference 12.3 percentage points; 95% CI [-1.4, 25.4]. Numerator/denominator inputs aspirin 30/86, placebo 19/84, from the same row; full TP,FN,TN,FP A=(30,56,617,119), P=(19,65,683,62).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 12.2647. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -1.4<25.4; printed difference 12.3 lies within [-1.4, 25.4].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-1.4199, 25.3628]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S060

- **Scope and source:** All; Qualitative; cutoff 10.2 µg Hb/g; Specificity; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=6](../../../joi190039supp3_prod.pdf#page=6), eTable 4, All row 3, Specificity difference/CI columns; role REPORT; map B053.
- **Exact printed inputs:** aspirin 83.8%; placebo 91.7%; difference -7.8 percentage points; 95% CI [-11.2, -4.5]. Numerator/denominator inputs aspirin 617/736, placebo 683/745, from the same row; full TP,FN,TN,FP A=(30,56,617,119), P=(19,65,683,62).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -7.8463. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -11.2<-4.5; printed difference -7.8 lies within [-11.2, -4.5].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-11.1519, -4.5009]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S061

- **Scope and source:** Men; Quantitative; cutoff 10.2 µg Hb/g; Sensitivity; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=6](../../../joi190039supp3_prod.pdf#page=6), eTable 4, Men row 1, Sensitivity difference/CI columns; role REPORT; map B054.
- **Exact printed inputs:** aspirin 47.7%; placebo 24.4%; difference 23.2 percentage points; 95% CI [5, 39.5]. Numerator/denominator inputs aspirin 31/65, placebo 11/45, from the same row; full TP,FN,TN,FP A=(31,34,310,78), P=(11,34,344,58).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 23.2479. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints 5<39.5; printed difference 23.2 lies within [5, 39.5].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [4.9535, 39.505]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 per-protocol male sensitivity repeats this exact difference and CI; REPORT vs REPORT agreement.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S062

- **Scope and source:** Men; Quantitative; cutoff 10.2 µg Hb/g; Specificity; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=6](../../../joi190039supp3_prod.pdf#page=6), eTable 4, Men row 1, Specificity difference/CI columns; role REPORT; map B054.
- **Exact printed inputs:** aspirin 79.9%; placebo 85.6%; difference -5.7 percentage points; 95% CI [-10.9, -0.4]. Numerator/denominator inputs aspirin 310/388, placebo 344/402, from the same row; full TP,FN,TN,FP A=(31,34,310,78), P=(11,34,344,58).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -5.6752. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -10.9<-0.4; printed difference -5.7 lies within [-10.9, -0.4].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-10.9221, -0.3828]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S063

- **Scope and source:** Men; Quantitative; cutoff 17 µg Hb/g; Sensitivity; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=6](../../../joi190039supp3_prod.pdf#page=6), eTable 4, Men row 2, Sensitivity difference/CI columns; role REPORT; map B055.
- **Exact printed inputs:** aspirin 35.4%; placebo 20%; difference 15.4 percentage points; 95% CI [-1.8, 30.9]. Numerator/denominator inputs aspirin 23/65, placebo 9/45, from the same row; full TP,FN,TN,FP A=(23,42,350,38), P=(9,36,373,29).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 15.3846. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -1.8<30.9; printed difference 15.4 lies within [-1.8, 30.9].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-1.8481, 30.9367]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S064

- **Scope and source:** Men; Quantitative; cutoff 17 µg Hb/g; Specificity; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=6](../../../joi190039supp3_prod.pdf#page=6), eTable 4, Men row 2, Specificity difference/CI columns; role REPORT; map B055.
- **Exact printed inputs:** aspirin 90.2%; placebo 92.8%; difference -2.6 percentage points; 95% CI [-6.5, 1.4]. Numerator/denominator inputs aspirin 350/388, placebo 373/402, from the same row; full TP,FN,TN,FP A=(23,42,350,38), P=(9,36,373,29).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -2.5799. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -6.5<1.4; printed difference -2.6 lies within [-6.5, 1.4].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-6.4987, 1.3502]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S065

- **Scope and source:** Men; Qualitative; cutoff 10.2 µg Hb/g; Sensitivity; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=6](../../../joi190039supp3_prod.pdf#page=6), eTable 4, Men row 3, Sensitivity difference/CI columns; role REPORT; map B056.
- **Exact printed inputs:** aspirin 42.1%; placebo 19.6%; difference 22.5 percentage points; 95% CI [4.5, 38.6]. Numerator/denominator inputs aspirin 24/57, placebo 9/46, from the same row; full TP,FN,TN,FP A=(24,33,311,63), P=(9,37,353,40).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 22.54. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints 4.5<38.6; printed difference 22.5 lies within [4.5, 38.6].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [4.4814, 38.5977]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 per-protocol male sensitivity repeats this exact difference and CI; REPORT vs REPORT agreement.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S066

- **Scope and source:** Men; Qualitative; cutoff 10.2 µg Hb/g; Specificity; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=6](../../../joi190039supp3_prod.pdf#page=6), eTable 4, Men row 3, Specificity difference/CI columns; role REPORT; map B056.
- **Exact printed inputs:** aspirin 83.2%; placebo 89.8%; difference -6.7 percentage points; 95% CI [-11.5, -1.8]. Numerator/denominator inputs aspirin 311/374, placebo 353/393, from the same row; full TP,FN,TN,FP A=(24,33,311,63), P=(9,37,353,40).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -6.6668. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -11.5<-1.8; printed difference -6.7 lies within [-11.5, -1.8].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-11.4868, -1.7962]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S067

- **Scope and source:** Women; Quantitative; cutoff 10.2 µg Hb/g; Sensitivity; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=6](../../../joi190039supp3_prod.pdf#page=6), eTable 4, Women row 1, Sensitivity difference/CI columns; role REPORT; map B057.
- **Exact printed inputs:** aspirin 33.3%; placebo 34.1%; difference -0.8 percentage points; 95% CI [-21.8, 20.6]. Numerator/denominator inputs aspirin 11/33, placebo 14/41, from the same row; full TP,FN,TN,FP A=(11,22,325,58), P=(14,27,347,27).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -0.813. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -21.8<20.6; printed difference -0.8 lies within [-21.8, 20.6].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-21.8163, 20.6202]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S068

- **Scope and source:** Women; Quantitative; cutoff 10.2 µg Hb/g; Specificity; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=6](../../../joi190039supp3_prod.pdf#page=6), eTable 4, Women row 1, Specificity difference/CI columns; role REPORT; map B057.
- **Exact printed inputs:** aspirin 84.9%; placebo 92.8%; difference -7.9 percentage points; 95% CI [-12.3, -3.4]. Numerator/denominator inputs aspirin 325/383, placebo 347/374, from the same row; full TP,FN,TN,FP A=(11,22,325,58), P=(14,27,347,27).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -7.9244. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -12.3<-3.4; printed difference -7.9 lies within [-12.3, -3.4].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-12.3488, -3.407]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S069

- **Scope and source:** Women; Quantitative; cutoff 17 µg Hb/g; Sensitivity; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=6](../../../joi190039supp3_prod.pdf#page=6), eTable 4, Women row 2, Sensitivity difference/CI columns; role REPORT; map B058.
- **Exact printed inputs:** aspirin 18.2%; placebo 22%; difference -3.8 percentage points; 95% CI [-21.6, 15]. Numerator/denominator inputs aspirin 6/33, placebo 9/41, from the same row; full TP,FN,TN,FP A=(6,27,354,29), P=(9,32,362,12).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -3.7694. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -21.6<15; printed difference -3.8 lies within [-21.6, 15].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-21.5602, 15.0486]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S070

- **Scope and source:** Women; Quantitative; cutoff 17 µg Hb/g; Specificity; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=6](../../../joi190039supp3_prod.pdf#page=6), eTable 4, Women row 2, Specificity difference/CI columns; role REPORT; map B058.
- **Exact printed inputs:** aspirin 92.4%; placebo 96.8%; difference -4.4 percentage points; 95% CI [-7.6, -1.1]. Numerator/denominator inputs aspirin 354/383, placebo 362/374, from the same row; full TP,FN,TN,FP A=(6,27,354,29), P=(9,32,362,12).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -4.3632. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -7.6<-1.1; printed difference -4.4 lies within [-7.6, -1.1].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-7.5873, -1.0822]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S071

- **Scope and source:** Women; Qualitative; cutoff 10.2 µg Hb/g; Sensitivity; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=6](../../../joi190039supp3_prod.pdf#page=6), eTable 4, Women row 3, Sensitivity difference/CI columns; role REPORT; map B059.
- **Exact printed inputs:** aspirin 20.7%; placebo 26.3%; difference -5.6 percentage points; 95% CI [-25.1, 15.3]. Numerator/denominator inputs aspirin 6/29, placebo 10/38, from the same row; full TP,FN,TN,FP A=(6,23,306,56), P=(10,28,330,22).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -5.6261. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -25.1<15.3; printed difference -5.6 lies within [-25.1, 15.3].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Sensitivity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-25.1209, 15.2822]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S072

- **Scope and source:** Women; Qualitative; cutoff 10.2 µg Hb/g; Specificity; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=6](../../../joi190039supp3_prod.pdf#page=6), eTable 4, Women row 3, Specificity difference/CI columns; role REPORT; map B059.
- **Exact printed inputs:** aspirin 84.5%; placebo 93.8%; difference -9.2 percentage points; 95% CI [-13.7, -4.6]. Numerator/denominator inputs aspirin 306/362, placebo 330/352, from the same row; full TP,FN,TN,FP A=(6,23,306,56), P=(10,28,330,22).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -9.2196. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -13.7<-4.6; printed difference -9.2 lies within [-13.7, -4.6].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; Specificity probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-13.6932, -4.6311]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** No second numeric occurrence supplied for the identical contrast; definitions D1–D3 apply.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

### eTable 5: per-protocol; sample collected exactly day 2

#### S073

- **Scope and source:** All; Quantitative; cutoff 10.2 µg Hb/g; PPV; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=7](../../../joi190039supp3_prod.pdf#page=7), eTable 5, All row 1, PPV difference/CI columns; role REPORT; map B060.
- **Exact printed inputs:** aspirin 23.6%; placebo 22.7%; difference 0.9 percentage points; 95% CI [-9.3, 10.7]. Numerator/denominator inputs aspirin 42/178, placebo 25/110, from eTable 4 p6; full TP,FN,TN,FP A=(42,56,635,136), P=(25,61,691,85).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 0.8682. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -9.3<10.7; printed difference 0.9 lies within [-9.3, 10.7].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; PPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-9.3225, 10.6717]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with eTable 4 p6.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S074

- **Scope and source:** All; Quantitative; cutoff 10.2 µg Hb/g; NPV; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=7](../../../joi190039supp3_prod.pdf#page=7), eTable 5, All row 1, NPV difference/CI columns; role REPORT; map B060.
- **Exact printed inputs:** aspirin 91.9%; placebo 91.9%; difference 0 percentage points; 95% CI [-2.8, 2.8]. Numerator/denominator inputs aspirin 635/691, placebo 691/752, from eTable 4 p6; full TP,FN,TN,FP A=(42,56,635,136), P=(25,61,691,85).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 0.0075. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -2.8<2.8; printed difference 0 lies within [-2.8, 2.8].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; NPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-2.8359, 2.8313]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with eTable 4 p6.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S075

- **Scope and source:** All; Quantitative; cutoff 17 µg Hb/g; PPV; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=7](../../../joi190039supp3_prod.pdf#page=7), eTable 5, All row 2, PPV difference/CI columns; role REPORT; map B061.
- **Exact printed inputs:** aspirin 30.2%; placebo 30.5%; difference -0.3 percentage points; 95% CI [-15.3, 14.2]. Numerator/denominator inputs aspirin 29/96, placebo 18/59, from eTable 4 p6; full TP,FN,TN,FP A=(29,69,704,67), P=(18,68,735,41).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -0.3001. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -15.3<14.2; printed difference -0.3 lies within [-15.3, 14.2].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; PPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-15.3108, 14.2403]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with eTable 4 p6.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S076

- **Scope and source:** All; Quantitative; cutoff 17 µg Hb/g; NPV; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=7](../../../joi190039supp3_prod.pdf#page=7), eTable 5, All row 2, NPV difference/CI columns; role REPORT; map B061.
- **Exact printed inputs:** aspirin 91.1%; placebo 91.5%; difference -0.5 percentage points; 95% CI [-3.3, 2.3]. Numerator/denominator inputs aspirin 704/773, placebo 735/803, from eTable 4 p6; full TP,FN,TN,FP A=(29,69,704,67), P=(18,68,735,41).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -0.458. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -3.3<2.3; printed difference -0.5 lies within [-3.3, 2.3].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; NPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-3.2559, 2.3342]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with eTable 4 p6.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S077

- **Scope and source:** All; Qualitative; cutoff 10.2 µg Hb/g; PPV; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=7](../../../joi190039supp3_prod.pdf#page=7), eTable 5, All row 3, PPV difference/CI columns; role REPORT; map B062.
- **Exact printed inputs:** aspirin 20.1%; placebo 23.5%; difference -3.3 percentage points; 95% CI [-14.8, 7.7]. Numerator/denominator inputs aspirin 30/149, placebo 19/81, from eTable 4 p6; full TP,FN,TN,FP A=(30,56,617,119), P=(19,65,683,62).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -3.3226. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -14.8<7.7; printed difference -3.3 lies within [-14.8, 7.7].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; PPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-14.7985, 7.6654]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with eTable 4 p6.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S078

- **Scope and source:** All; Qualitative; cutoff 10.2 µg Hb/g; NPV; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=7](../../../joi190039supp3_prod.pdf#page=7), eTable 5, All row 3, NPV difference/CI columns; role REPORT; map B062.
- **Exact printed inputs:** aspirin 91.7%; placebo 91.3%; difference 0.4 percentage points; 95% CI [-2.6, 3.3]. Numerator/denominator inputs aspirin 617/673, placebo 683/748, from eTable 4 p6; full TP,FN,TN,FP A=(30,56,617,119), P=(19,65,683,62).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 0.3689. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -2.6<3.3; printed difference 0.4 lies within [-2.6, 3.3].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; NPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-2.5617, 3.2729]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with eTable 4 p6.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S079

- **Scope and source:** Men; Quantitative; cutoff 10.2 µg Hb/g; PPV; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=7](../../../joi190039supp3_prod.pdf#page=7), eTable 5, Men row 1, PPV difference/CI columns; role REPORT; map B063.
- **Exact printed inputs:** aspirin 28.4%; placebo 15.9%; difference 12.5 percentage points; 95% CI [-0.2, 24.1]. Numerator/denominator inputs aspirin 31/109, placebo 11/69, from eTable 4 p6; full TP,FN,TN,FP A=(31,34,310,78), P=(11,34,344,58).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 12.4983. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -0.2<24.1; printed difference 12.5 lies within [-0.2, 24.1].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; PPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-0.1968, 24.0517]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with eTable 4 p6.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S080

- **Scope and source:** Men; Quantitative; cutoff 10.2 µg Hb/g; NPV; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=7](../../../joi190039supp3_prod.pdf#page=7), eTable 5, Men row 1, NPV difference/CI columns; role REPORT; map B063.
- **Exact printed inputs:** aspirin 90.1%; placebo 91%; difference -0.9 percentage points; 95% CI [-5.2, 3.4]. Numerator/denominator inputs aspirin 310/344, placebo 344/378, from eTable 4 p6; full TP,FN,TN,FP A=(31,34,310,78), P=(11,34,344,58).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -0.889. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -5.2<3.4; printed difference -0.9 lies within [-5.2, 3.4].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; NPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-5.2118, 3.4017]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with eTable 4 p6.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S081

- **Scope and source:** Men; Quantitative; cutoff 17 µg Hb/g; PPV; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=7](../../../joi190039supp3_prod.pdf#page=7), eTable 5, Men row 2, PPV difference/CI columns; role REPORT; map B064.
- **Exact printed inputs:** aspirin 37.7%; placebo 23.7%; difference 14 percentage points; 95% CI [-4.9, 31.1]. Numerator/denominator inputs aspirin 23/61, placebo 9/38, from eTable 4 p6; full TP,FN,TN,FP A=(23,42,350,38), P=(9,36,373,29).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 14.0207. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -4.9<31.1; printed difference 14 lies within [-4.9, 31.1].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; PPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-4.901, 31.0915]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with eTable 4 p6.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S082

- **Scope and source:** Men; Quantitative; cutoff 17 µg Hb/g; NPV; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=7](../../../joi190039supp3_prod.pdf#page=7), eTable 5, Men row 2, NPV difference/CI columns; role REPORT; map B064.
- **Exact printed inputs:** aspirin 89.3%; placebo 91.2%; difference -1.9 percentage points; 95% CI [-6.1, 2.2]. Numerator/denominator inputs aspirin 350/392, placebo 373/409, from eTable 4 p6; full TP,FN,TN,FP A=(23,42,350,38), P=(9,36,373,29).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -1.9123. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -6.1<2.2; printed difference -1.9 lies within [-6.1, 2.2].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; NPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-6.0509, 2.2283]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with eTable 4 p6.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S083

- **Scope and source:** Men; Qualitative; cutoff 10.2 µg Hb/g; PPV; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=7](../../../joi190039supp3_prod.pdf#page=7), eTable 5, Men row 3, PPV difference/CI columns; role REPORT; map B065.
- **Exact printed inputs:** aspirin 27.6%; placebo 18.4%; difference 9.2 percentage points; 95% CI [-5.9, 22.8]. Numerator/denominator inputs aspirin 24/87, placebo 9/49, from eTable 4 p6; full TP,FN,TN,FP A=(24,33,311,63), P=(9,37,353,40).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 9.2189. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -5.9<22.8; printed difference 9.2 lies within [-5.9, 22.8].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; PPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-5.8678, 22.8319]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with eTable 4 p6.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S084

- **Scope and source:** Men; Qualitative; cutoff 10.2 µg Hb/g; NPV; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=7](../../../joi190039supp3_prod.pdf#page=7), eTable 5, Men row 3, NPV difference/CI columns; role REPORT; map B065.
- **Exact printed inputs:** aspirin 90.4%; placebo 90.5%; difference -0.1 percentage points; 95% CI [-4.4, 4.2]. Numerator/denominator inputs aspirin 311/344, placebo 353/390, from eTable 4 p6; full TP,FN,TN,FP A=(24,33,311,63), P=(9,37,353,40).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -0.1058. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -4.4<4.2; printed difference -0.1 lies within [-4.4, 4.2].
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; printed sign/direction coherent; NPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-4.4242, 4.1587]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with eTable 4 p6.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S085

- **Scope and source:** Women; Quantitative; cutoff 10.2 µg Hb/g; PPV; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=7](../../../joi190039supp3_prod.pdf#page=7), eTable 5, Women row 1, PPV difference/CI columns; role REPORT; map B066.
- **Exact printed inputs:** aspirin 15.9%; placebo 34.1%; difference minus glyph only; no visible magnitude; 95% CI [-34.7, -1.3]. Numerator/denominator inputs aspirin 11/69, placebo 14/41, from eTable 4 p6; full TP,FN,TN,FP A=(11,22,325,58), P=(14,27,347,27).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -18.2043. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -34.7<-1.3; source containment cannot be tested for an absent point-estimate magnitude; count-derived diagnostic -18.2043 is contained.
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; minus glyph and negative interval agree with sign, magnitude omitted (SP1-CLIP-1); PPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-34.6831, -1.2815]; uses named-method approximation and actual count inputs, consistent at displayed precision. Native extraction magnitude fragment 18.2 is a locator, not a visible printed estimate.
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with eTable 4 p6.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. Source magnitude clipped/hidden; human question recorded in checker.
- **Candidate connection:** SP1-CLIP-1
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S086

- **Scope and source:** Women; Quantitative; cutoff 10.2 µg Hb/g; NPV; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=7](../../../joi190039supp3_prod.pdf#page=7), eTable 5, Women row 1, NPV difference/CI columns; role REPORT; map B066.
- **Exact printed inputs:** aspirin 93.7%; placebo 92.8%; difference 0.9 percentage points; 95% CI [-2.9, 4.6]. Numerator/denominator inputs aspirin 325/347, placebo 347/374, from eTable 4 p6; full TP,FN,TN,FP A=(11,22,325,58), P=(14,27,347,27).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 0.8792. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -2.9<4.6; printed difference 0.9 lies within [-2.9, 4.6].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; NPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-2.8606, 4.5737]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with eTable 4 p6.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S087

- **Scope and source:** Women; Quantitative; cutoff 17 µg Hb/g; PPV; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=7](../../../joi190039supp3_prod.pdf#page=7), eTable 5, Women row 2, PPV difference/CI columns; role REPORT; map B067.
- **Exact printed inputs:** aspirin 17.1%; placebo 42.9%; difference minus glyph only; no visible magnitude; 95% CI [-48.4, -0.7]. Numerator/denominator inputs aspirin 6/35, placebo 9/21, from eTable 4 p6; full TP,FN,TN,FP A=(6,27,354,29), P=(9,32,362,12).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -25.7143. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -48.4<-0.7; source containment cannot be tested for an absent point-estimate magnitude; count-derived diagnostic -25.7143 is contained.
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; minus glyph and negative interval agree with sign, magnitude omitted (SP1-CLIP-2); PPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-48.4279, -0.6908]; uses named-method approximation and actual count inputs, consistent at displayed precision. Native extraction magnitude fragment 25.7 is a locator, not a visible printed estimate.
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with eTable 4 p6.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. Source magnitude clipped/hidden; human question recorded in checker.
- **Candidate connection:** SP1-CLIP-2
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S088

- **Scope and source:** Women; Quantitative; cutoff 17 µg Hb/g; NPV; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=7](../../../joi190039supp3_prod.pdf#page=7), eTable 5, Women row 2, NPV difference/CI columns; role REPORT; map B067.
- **Exact printed inputs:** aspirin 92.9%; placebo 91.9%; difference 1 percentage points; 95% CI [-2.7, 4.8]. Numerator/denominator inputs aspirin 354/381, placebo 362/394, from eTable 4 p6; full TP,FN,TN,FP A=(6,27,354,29), P=(9,32,362,12).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 1.0352. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -2.7<4.8; printed difference 1 lies within [-2.7, 4.8].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; NPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-2.7466, 4.7918]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with eTable 4 p6.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S089

- **Scope and source:** Women; Qualitative; cutoff 10.2 µg Hb/g; PPV; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=7](../../../joi190039supp3_prod.pdf#page=7), eTable 5, Women row 3, PPV difference/CI columns; role REPORT; map B068.
- **Exact printed inputs:** aspirin 9.7%; placebo 31.2%; difference minus glyph only; no visible magnitude; 95% CI [-38.9, -3.9]. Numerator/denominator inputs aspirin 6/62, placebo 10/32, from eTable 4 p6; full TP,FN,TN,FP A=(6,23,306,56), P=(10,28,330,22).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference -21.5726. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -38.9<-3.9; source containment cannot be tested for an absent point-estimate magnitude; count-derived diagnostic -21.5726 is contained.
- **Direction/label/scale:** negative raw aspirin-minus-placebo direction; minus glyph and negative interval agree with sign, magnitude omitted (SP1-CLIP-3); PPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-38.901, -3.9299]; uses named-method approximation and actual count inputs, consistent at displayed precision. Native extraction magnitude fragment 21.6 is a locator, not a visible printed estimate.
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with eTable 4 p6.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. Source magnitude clipped/hidden; human question recorded in checker.
- **Candidate connection:** SP1-CLIP-3
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S090

- **Scope and source:** Women; Qualitative; cutoff 10.2 µg Hb/g; NPV; per-protocol; sample collected exactly day 2; [joi190039supp3_prod.pdf#page=7](../../../joi190039supp3_prod.pdf#page=7), eTable 5, Women row 3, NPV difference/CI columns; role REPORT; map B068.
- **Exact printed inputs:** aspirin 93%; placebo 92.2%; difference 0.8 percentage points; 95% CI [-3.2, 4.8]. Numerator/denominator inputs aspirin 306/329, placebo 330/358, from eTable 4 p6; full TP,FN,TN,FP A=(6,23,306,56), P=(10,28,330,22).
- **Population/model/definition:** D1–D4; raw aspirin-minus-placebo probability difference, displayed in percentage points; raw-count difference 0.8303. Population/test/cutoff row alignment explicit.
- **Ordering and containment:** endpoints -3.2<4.8; printed difference 0.8 lies within [-3.2, 4.8].
- **Direction/label/scale:** positive raw aspirin-minus-placebo direction; printed sign/direction coherent; NPV probability denominator and percentage-point difference agree with D1, no rate/count or OR/RR/HR reinterpretation.
- **Diagnostic adjusted-Wald reconstruction:** D4 endpoints [-3.1586, 4.7682]; uses named-method approximation and actual count inputs, consistent at displayed precision. 
- **Interval/P/test/statistic/SE compatibility:** Not printed; exact interval/P/statistic/SE check not applicable.
- **Matched occurrences:** Main article p4 says 'Overall, no significant differences' for ITS/PP predictive values. For All population rows this CI spans zero; subgroup-only zero exclusions do not independently contradict 'Overall'. Arm/count identity compared with eTable 4 p6.
- **Missing inputs/limits:** actual result-P formula/statistic/SE not provided; no inference of continuity correction or variance from CI name. No additional definition is needed for direct ordering/containment/sign checks.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

### eTable 6: eighteen site-random-intercept SD/P relationships

#### S091

- **Scope and source:** All Q10.2 Sensitivity; intention-to-screen day2; [joi190039supp3_prod.pdf#page=8](../../../joi190039supp3_prod.pdf#page=8) eTable6 exact sex/test/cutoff row, Sensitivity St.Dev. and p-value columns; REPORT; B069. Main matching REPORT locations [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) sensitivity-analysis method, [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5) result range.
- **Exact printed inputs:** SD=0; P=0.50. No estimate CI, LRT statistic, SE or arm-specific counts printed. SD zero/near-zero is a random-effect estimate, not a displayed P zero.
- **Population/model/definition:** D5; binomial GLMM site random intercept, null SD=0 vs SD>0, outcome agreement for disease-status-specific sensitivity or specificity. No participant-repeated random effect inferred.
- **Ordering/containment:** no interval present; SD nonnegative and P in [0,1]; interval endpoint/point-containment checks not applicable.
- **Sign/direction/label/scale:** SD nonnegative, caption/header accurately labels model parameter; P=0.50>.05 agrees with main non-significance. No probability-scale interpretation of SD.
- **Interval/P/test/statistic/SE compatibility:** direct hypothesis/label check coherent; exact LRT-P calculation unavailable because statistic, likelihoods and boundary reference-distribution rule missing. No inferential diagnostic derived from SD alone.
- **Matched occurrences:** 0.50 lies in main p5 range .16–.50; global minimum .16 and maximum .50 occur across this inventory; subgroup values do not conflict with the range.
- **Missing inputs/limits:** D5 exact model fit, LRT statistic and null-reference definition absent; numeric inversion not attempted. No independent supplied-source contradiction. P-display-zero policy retained; DISPLAY_ZERO_NOT_CANDIDATE is not assigned to SD=0 because its P is not zero.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S092

- **Scope and source:** All Q10.2 Specificity; intention-to-screen day2; [joi190039supp3_prod.pdf#page=8](../../../joi190039supp3_prod.pdf#page=8) eTable6 exact sex/test/cutoff row, Specificity St.Dev. and p-value columns; REPORT; B069. Main matching REPORT locations [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) sensitivity-analysis method, [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5) result range.
- **Exact printed inputs:** SD=0.00549; P=0.38. No estimate CI, LRT statistic, SE or arm-specific counts printed. SD zero/near-zero is a random-effect estimate, not a displayed P zero.
- **Population/model/definition:** D5; binomial GLMM site random intercept, null SD=0 vs SD>0, outcome agreement for disease-status-specific sensitivity or specificity. No participant-repeated random effect inferred.
- **Ordering/containment:** no interval present; SD nonnegative and P in [0,1]; interval endpoint/point-containment checks not applicable.
- **Sign/direction/label/scale:** SD nonnegative, caption/header accurately labels model parameter; P=0.38>.05 agrees with main non-significance. No probability-scale interpretation of SD.
- **Interval/P/test/statistic/SE compatibility:** direct hypothesis/label check coherent; exact LRT-P calculation unavailable because statistic, likelihoods and boundary reference-distribution rule missing. No inferential diagnostic derived from SD alone.
- **Matched occurrences:** 0.38 lies in main p5 range .16–.50; global minimum .16 and maximum .50 occur across this inventory; subgroup values do not conflict with the range.
- **Missing inputs/limits:** D5 exact model fit, LRT statistic and null-reference definition absent; numeric inversion not attempted. No independent supplied-source contradiction. P-display-zero policy retained; DISPLAY_ZERO_NOT_CANDIDATE is not assigned to SD=0 because its P is not zero.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S093

- **Scope and source:** All Q17.0 Sensitivity; intention-to-screen day2; [joi190039supp3_prod.pdf#page=8](../../../joi190039supp3_prod.pdf#page=8) eTable6 exact sex/test/cutoff row, Sensitivity St.Dev. and p-value columns; REPORT; B069. Main matching REPORT locations [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) sensitivity-analysis method, [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5) result range.
- **Exact printed inputs:** SD=0.197; P=0.16. No estimate CI, LRT statistic, SE or arm-specific counts printed. SD zero/near-zero is a random-effect estimate, not a displayed P zero.
- **Population/model/definition:** D5; binomial GLMM site random intercept, null SD=0 vs SD>0, outcome agreement for disease-status-specific sensitivity or specificity. No participant-repeated random effect inferred.
- **Ordering/containment:** no interval present; SD nonnegative and P in [0,1]; interval endpoint/point-containment checks not applicable.
- **Sign/direction/label/scale:** SD nonnegative, caption/header accurately labels model parameter; P=0.16>.05 agrees with main non-significance. No probability-scale interpretation of SD.
- **Interval/P/test/statistic/SE compatibility:** direct hypothesis/label check coherent; exact LRT-P calculation unavailable because statistic, likelihoods and boundary reference-distribution rule missing. No inferential diagnostic derived from SD alone.
- **Matched occurrences:** 0.16 lies in main p5 range .16–.50; global minimum .16 and maximum .50 occur across this inventory; subgroup values do not conflict with the range.
- **Missing inputs/limits:** D5 exact model fit, LRT statistic and null-reference definition absent; numeric inversion not attempted. No independent supplied-source contradiction. P-display-zero policy retained; DISPLAY_ZERO_NOT_CANDIDATE is not assigned to SD=0 because its P is not zero.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S094

- **Scope and source:** All Q17.0 Specificity; intention-to-screen day2; [joi190039supp3_prod.pdf#page=8](../../../joi190039supp3_prod.pdf#page=8) eTable6 exact sex/test/cutoff row, Specificity St.Dev. and p-value columns; REPORT; B069. Main matching REPORT locations [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) sensitivity-analysis method, [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5) result range.
- **Exact printed inputs:** SD=0; P=0.50. No estimate CI, LRT statistic, SE or arm-specific counts printed. SD zero/near-zero is a random-effect estimate, not a displayed P zero.
- **Population/model/definition:** D5; binomial GLMM site random intercept, null SD=0 vs SD>0, outcome agreement for disease-status-specific sensitivity or specificity. No participant-repeated random effect inferred.
- **Ordering/containment:** no interval present; SD nonnegative and P in [0,1]; interval endpoint/point-containment checks not applicable.
- **Sign/direction/label/scale:** SD nonnegative, caption/header accurately labels model parameter; P=0.50>.05 agrees with main non-significance. No probability-scale interpretation of SD.
- **Interval/P/test/statistic/SE compatibility:** direct hypothesis/label check coherent; exact LRT-P calculation unavailable because statistic, likelihoods and boundary reference-distribution rule missing. No inferential diagnostic derived from SD alone.
- **Matched occurrences:** 0.50 lies in main p5 range .16–.50; global minimum .16 and maximum .50 occur across this inventory; subgroup values do not conflict with the range.
- **Missing inputs/limits:** D5 exact model fit, LRT statistic and null-reference definition absent; numeric inversion not attempted. No independent supplied-source contradiction. P-display-zero policy retained; DISPLAY_ZERO_NOT_CANDIDATE is not assigned to SD=0 because its P is not zero.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S095

- **Scope and source:** All L10.2 Sensitivity; intention-to-screen day2; [joi190039supp3_prod.pdf#page=8](../../../joi190039supp3_prod.pdf#page=8) eTable6 exact sex/test/cutoff row, Sensitivity St.Dev. and p-value columns; REPORT; B069. Main matching REPORT locations [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) sensitivity-analysis method, [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5) result range.
- **Exact printed inputs:** SD=0; P=0.50. No estimate CI, LRT statistic, SE or arm-specific counts printed. SD zero/near-zero is a random-effect estimate, not a displayed P zero.
- **Population/model/definition:** D5; binomial GLMM site random intercept, null SD=0 vs SD>0, outcome agreement for disease-status-specific sensitivity or specificity. No participant-repeated random effect inferred.
- **Ordering/containment:** no interval present; SD nonnegative and P in [0,1]; interval endpoint/point-containment checks not applicable.
- **Sign/direction/label/scale:** SD nonnegative, caption/header accurately labels model parameter; P=0.50>.05 agrees with main non-significance. No probability-scale interpretation of SD.
- **Interval/P/test/statistic/SE compatibility:** direct hypothesis/label check coherent; exact LRT-P calculation unavailable because statistic, likelihoods and boundary reference-distribution rule missing. No inferential diagnostic derived from SD alone.
- **Matched occurrences:** 0.50 lies in main p5 range .16–.50; global minimum .16 and maximum .50 occur across this inventory; subgroup values do not conflict with the range.
- **Missing inputs/limits:** D5 exact model fit, LRT statistic and null-reference definition absent; numeric inversion not attempted. No independent supplied-source contradiction. P-display-zero policy retained; DISPLAY_ZERO_NOT_CANDIDATE is not assigned to SD=0 because its P is not zero.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S096

- **Scope and source:** All L10.2 Specificity; intention-to-screen day2; [joi190039supp3_prod.pdf#page=8](../../../joi190039supp3_prod.pdf#page=8) eTable6 exact sex/test/cutoff row, Specificity St.Dev. and p-value columns; REPORT; B069. Main matching REPORT locations [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) sensitivity-analysis method, [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5) result range.
- **Exact printed inputs:** SD=0.00923; P=0.30. No estimate CI, LRT statistic, SE or arm-specific counts printed. SD zero/near-zero is a random-effect estimate, not a displayed P zero.
- **Population/model/definition:** D5; binomial GLMM site random intercept, null SD=0 vs SD>0, outcome agreement for disease-status-specific sensitivity or specificity. No participant-repeated random effect inferred.
- **Ordering/containment:** no interval present; SD nonnegative and P in [0,1]; interval endpoint/point-containment checks not applicable.
- **Sign/direction/label/scale:** SD nonnegative, caption/header accurately labels model parameter; P=0.30>.05 agrees with main non-significance. No probability-scale interpretation of SD.
- **Interval/P/test/statistic/SE compatibility:** direct hypothesis/label check coherent; exact LRT-P calculation unavailable because statistic, likelihoods and boundary reference-distribution rule missing. No inferential diagnostic derived from SD alone.
- **Matched occurrences:** 0.30 lies in main p5 range .16–.50; global minimum .16 and maximum .50 occur across this inventory; subgroup values do not conflict with the range.
- **Missing inputs/limits:** D5 exact model fit, LRT statistic and null-reference definition absent; numeric inversion not attempted. No independent supplied-source contradiction. P-display-zero policy retained; DISPLAY_ZERO_NOT_CANDIDATE is not assigned to SD=0 because its P is not zero.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S097

- **Scope and source:** Men Q10.2 Sensitivity; intention-to-screen day2; [joi190039supp3_prod.pdf#page=8](../../../joi190039supp3_prod.pdf#page=8) eTable6 exact sex/test/cutoff row, Sensitivity St.Dev. and p-value columns; REPORT; B069. Main matching REPORT locations [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) sensitivity-analysis method, [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5) result range.
- **Exact printed inputs:** SD=0; P=0.50. No estimate CI, LRT statistic, SE or arm-specific counts printed. SD zero/near-zero is a random-effect estimate, not a displayed P zero.
- **Population/model/definition:** D5; binomial GLMM site random intercept, null SD=0 vs SD>0, outcome agreement for disease-status-specific sensitivity or specificity. No participant-repeated random effect inferred.
- **Ordering/containment:** no interval present; SD nonnegative and P in [0,1]; interval endpoint/point-containment checks not applicable.
- **Sign/direction/label/scale:** SD nonnegative, caption/header accurately labels model parameter; P=0.50>.05 agrees with main non-significance. No probability-scale interpretation of SD.
- **Interval/P/test/statistic/SE compatibility:** direct hypothesis/label check coherent; exact LRT-P calculation unavailable because statistic, likelihoods and boundary reference-distribution rule missing. No inferential diagnostic derived from SD alone.
- **Matched occurrences:** 0.50 lies in main p5 range .16–.50; global minimum .16 and maximum .50 occur across this inventory; subgroup values do not conflict with the range.
- **Missing inputs/limits:** D5 exact model fit, LRT statistic and null-reference definition absent; numeric inversion not attempted. No independent supplied-source contradiction. P-display-zero policy retained; DISPLAY_ZERO_NOT_CANDIDATE is not assigned to SD=0 because its P is not zero.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S098

- **Scope and source:** Men Q10.2 Specificity; intention-to-screen day2; [joi190039supp3_prod.pdf#page=8](../../../joi190039supp3_prod.pdf#page=8) eTable6 exact sex/test/cutoff row, Specificity St.Dev. and p-value columns; REPORT; B069. Main matching REPORT locations [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) sensitivity-analysis method, [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5) result range.
- **Exact printed inputs:** SD=1e-14; P=0.50. No estimate CI, LRT statistic, SE or arm-specific counts printed. SD zero/near-zero is a random-effect estimate, not a displayed P zero.
- **Population/model/definition:** D5; binomial GLMM site random intercept, null SD=0 vs SD>0, outcome agreement for disease-status-specific sensitivity or specificity. No participant-repeated random effect inferred.
- **Ordering/containment:** no interval present; SD nonnegative and P in [0,1]; interval endpoint/point-containment checks not applicable.
- **Sign/direction/label/scale:** SD nonnegative, caption/header accurately labels model parameter; P=0.50>.05 agrees with main non-significance. No probability-scale interpretation of SD.
- **Interval/P/test/statistic/SE compatibility:** direct hypothesis/label check coherent; exact LRT-P calculation unavailable because statistic, likelihoods and boundary reference-distribution rule missing. No inferential diagnostic derived from SD alone.
- **Matched occurrences:** 0.50 lies in main p5 range .16–.50; global minimum .16 and maximum .50 occur across this inventory; subgroup values do not conflict with the range.
- **Missing inputs/limits:** D5 exact model fit, LRT statistic and null-reference definition absent; numeric inversion not attempted. No independent supplied-source contradiction. P-display-zero policy retained; DISPLAY_ZERO_NOT_CANDIDATE is not assigned to SD=0 because its P is not zero.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S099

- **Scope and source:** Men Q17.0 Sensitivity; intention-to-screen day2; [joi190039supp3_prod.pdf#page=8](../../../joi190039supp3_prod.pdf#page=8) eTable6 exact sex/test/cutoff row, Sensitivity St.Dev. and p-value columns; REPORT; B069. Main matching REPORT locations [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) sensitivity-analysis method, [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5) result range.
- **Exact printed inputs:** SD=0; P=0.50. No estimate CI, LRT statistic, SE or arm-specific counts printed. SD zero/near-zero is a random-effect estimate, not a displayed P zero.
- **Population/model/definition:** D5; binomial GLMM site random intercept, null SD=0 vs SD>0, outcome agreement for disease-status-specific sensitivity or specificity. No participant-repeated random effect inferred.
- **Ordering/containment:** no interval present; SD nonnegative and P in [0,1]; interval endpoint/point-containment checks not applicable.
- **Sign/direction/label/scale:** SD nonnegative, caption/header accurately labels model parameter; P=0.50>.05 agrees with main non-significance. No probability-scale interpretation of SD.
- **Interval/P/test/statistic/SE compatibility:** direct hypothesis/label check coherent; exact LRT-P calculation unavailable because statistic, likelihoods and boundary reference-distribution rule missing. No inferential diagnostic derived from SD alone.
- **Matched occurrences:** 0.50 lies in main p5 range .16–.50; global minimum .16 and maximum .50 occur across this inventory; subgroup values do not conflict with the range.
- **Missing inputs/limits:** D5 exact model fit, LRT statistic and null-reference definition absent; numeric inversion not attempted. No independent supplied-source contradiction. P-display-zero policy retained; DISPLAY_ZERO_NOT_CANDIDATE is not assigned to SD=0 because its P is not zero.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S100

- **Scope and source:** Men Q17.0 Specificity; intention-to-screen day2; [joi190039supp3_prod.pdf#page=8](../../../joi190039supp3_prod.pdf#page=8) eTable6 exact sex/test/cutoff row, Specificity St.Dev. and p-value columns; REPORT; B069. Main matching REPORT locations [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) sensitivity-analysis method, [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5) result range.
- **Exact printed inputs:** SD=0.0147; P=0.40. No estimate CI, LRT statistic, SE or arm-specific counts printed. SD zero/near-zero is a random-effect estimate, not a displayed P zero.
- **Population/model/definition:** D5; binomial GLMM site random intercept, null SD=0 vs SD>0, outcome agreement for disease-status-specific sensitivity or specificity. No participant-repeated random effect inferred.
- **Ordering/containment:** no interval present; SD nonnegative and P in [0,1]; interval endpoint/point-containment checks not applicable.
- **Sign/direction/label/scale:** SD nonnegative, caption/header accurately labels model parameter; P=0.40>.05 agrees with main non-significance. No probability-scale interpretation of SD.
- **Interval/P/test/statistic/SE compatibility:** direct hypothesis/label check coherent; exact LRT-P calculation unavailable because statistic, likelihoods and boundary reference-distribution rule missing. No inferential diagnostic derived from SD alone.
- **Matched occurrences:** 0.40 lies in main p5 range .16–.50; global minimum .16 and maximum .50 occur across this inventory; subgroup values do not conflict with the range.
- **Missing inputs/limits:** D5 exact model fit, LRT statistic and null-reference definition absent; numeric inversion not attempted. No independent supplied-source contradiction. P-display-zero policy retained; DISPLAY_ZERO_NOT_CANDIDATE is not assigned to SD=0 because its P is not zero.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S101

- **Scope and source:** Men L10.2 Sensitivity; intention-to-screen day2; [joi190039supp3_prod.pdf#page=8](../../../joi190039supp3_prod.pdf#page=8) eTable6 exact sex/test/cutoff row, Sensitivity St.Dev. and p-value columns; REPORT; B069. Main matching REPORT locations [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) sensitivity-analysis method, [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5) result range.
- **Exact printed inputs:** SD=0; P=0.50. No estimate CI, LRT statistic, SE or arm-specific counts printed. SD zero/near-zero is a random-effect estimate, not a displayed P zero.
- **Population/model/definition:** D5; binomial GLMM site random intercept, null SD=0 vs SD>0, outcome agreement for disease-status-specific sensitivity or specificity. No participant-repeated random effect inferred.
- **Ordering/containment:** no interval present; SD nonnegative and P in [0,1]; interval endpoint/point-containment checks not applicable.
- **Sign/direction/label/scale:** SD nonnegative, caption/header accurately labels model parameter; P=0.50>.05 agrees with main non-significance. No probability-scale interpretation of SD.
- **Interval/P/test/statistic/SE compatibility:** direct hypothesis/label check coherent; exact LRT-P calculation unavailable because statistic, likelihoods and boundary reference-distribution rule missing. No inferential diagnostic derived from SD alone.
- **Matched occurrences:** 0.50 lies in main p5 range .16–.50; global minimum .16 and maximum .50 occur across this inventory; subgroup values do not conflict with the range.
- **Missing inputs/limits:** D5 exact model fit, LRT statistic and null-reference definition absent; numeric inversion not attempted. No independent supplied-source contradiction. P-display-zero policy retained; DISPLAY_ZERO_NOT_CANDIDATE is not assigned to SD=0 because its P is not zero.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S102

- **Scope and source:** Men L10.2 Specificity; intention-to-screen day2; [joi190039supp3_prod.pdf#page=8](../../../joi190039supp3_prod.pdf#page=8) eTable6 exact sex/test/cutoff row, Specificity St.Dev. and p-value columns; REPORT; B069. Main matching REPORT locations [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) sensitivity-analysis method, [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5) result range.
- **Exact printed inputs:** SD=0.0113; P=0.35. No estimate CI, LRT statistic, SE or arm-specific counts printed. SD zero/near-zero is a random-effect estimate, not a displayed P zero.
- **Population/model/definition:** D5; binomial GLMM site random intercept, null SD=0 vs SD>0, outcome agreement for disease-status-specific sensitivity or specificity. No participant-repeated random effect inferred.
- **Ordering/containment:** no interval present; SD nonnegative and P in [0,1]; interval endpoint/point-containment checks not applicable.
- **Sign/direction/label/scale:** SD nonnegative, caption/header accurately labels model parameter; P=0.35>.05 agrees with main non-significance. No probability-scale interpretation of SD.
- **Interval/P/test/statistic/SE compatibility:** direct hypothesis/label check coherent; exact LRT-P calculation unavailable because statistic, likelihoods and boundary reference-distribution rule missing. No inferential diagnostic derived from SD alone.
- **Matched occurrences:** 0.35 lies in main p5 range .16–.50; global minimum .16 and maximum .50 occur across this inventory; subgroup values do not conflict with the range.
- **Missing inputs/limits:** D5 exact model fit, LRT statistic and null-reference definition absent; numeric inversion not attempted. No independent supplied-source contradiction. P-display-zero policy retained; DISPLAY_ZERO_NOT_CANDIDATE is not assigned to SD=0 because its P is not zero.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S103

- **Scope and source:** Women Q10.2 Sensitivity; intention-to-screen day2; [joi190039supp3_prod.pdf#page=8](../../../joi190039supp3_prod.pdf#page=8) eTable6 exact sex/test/cutoff row, Sensitivity St.Dev. and p-value columns; REPORT; B069. Main matching REPORT locations [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) sensitivity-analysis method, [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5) result range.
- **Exact printed inputs:** SD=0; P=0.50. No estimate CI, LRT statistic, SE or arm-specific counts printed. SD zero/near-zero is a random-effect estimate, not a displayed P zero.
- **Population/model/definition:** D5; binomial GLMM site random intercept, null SD=0 vs SD>0, outcome agreement for disease-status-specific sensitivity or specificity. No participant-repeated random effect inferred.
- **Ordering/containment:** no interval present; SD nonnegative and P in [0,1]; interval endpoint/point-containment checks not applicable.
- **Sign/direction/label/scale:** SD nonnegative, caption/header accurately labels model parameter; P=0.50>.05 agrees with main non-significance. No probability-scale interpretation of SD.
- **Interval/P/test/statistic/SE compatibility:** direct hypothesis/label check coherent; exact LRT-P calculation unavailable because statistic, likelihoods and boundary reference-distribution rule missing. No inferential diagnostic derived from SD alone.
- **Matched occurrences:** 0.50 lies in main p5 range .16–.50; global minimum .16 and maximum .50 occur across this inventory; subgroup values do not conflict with the range.
- **Missing inputs/limits:** D5 exact model fit, LRT statistic and null-reference definition absent; numeric inversion not attempted. No independent supplied-source contradiction. P-display-zero policy retained; DISPLAY_ZERO_NOT_CANDIDATE is not assigned to SD=0 because its P is not zero.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S104

- **Scope and source:** Women Q10.2 Specificity; intention-to-screen day2; [joi190039supp3_prod.pdf#page=8](../../../joi190039supp3_prod.pdf#page=8) eTable6 exact sex/test/cutoff row, Specificity St.Dev. and p-value columns; REPORT; B069. Main matching REPORT locations [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) sensitivity-analysis method, [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5) result range.
- **Exact printed inputs:** SD=1.79e-12; P=0.50. No estimate CI, LRT statistic, SE or arm-specific counts printed. SD zero/near-zero is a random-effect estimate, not a displayed P zero.
- **Population/model/definition:** D5; binomial GLMM site random intercept, null SD=0 vs SD>0, outcome agreement for disease-status-specific sensitivity or specificity. No participant-repeated random effect inferred.
- **Ordering/containment:** no interval present; SD nonnegative and P in [0,1]; interval endpoint/point-containment checks not applicable.
- **Sign/direction/label/scale:** SD nonnegative, caption/header accurately labels model parameter; P=0.50>.05 agrees with main non-significance. No probability-scale interpretation of SD.
- **Interval/P/test/statistic/SE compatibility:** direct hypothesis/label check coherent; exact LRT-P calculation unavailable because statistic, likelihoods and boundary reference-distribution rule missing. No inferential diagnostic derived from SD alone.
- **Matched occurrences:** 0.50 lies in main p5 range .16–.50; global minimum .16 and maximum .50 occur across this inventory; subgroup values do not conflict with the range.
- **Missing inputs/limits:** D5 exact model fit, LRT statistic and null-reference definition absent; numeric inversion not attempted. No independent supplied-source contradiction. P-display-zero policy retained; DISPLAY_ZERO_NOT_CANDIDATE is not assigned to SD=0 because its P is not zero.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S105

- **Scope and source:** Women Q17.0 Sensitivity; intention-to-screen day2; [joi190039supp3_prod.pdf#page=8](../../../joi190039supp3_prod.pdf#page=8) eTable6 exact sex/test/cutoff row, Sensitivity St.Dev. and p-value columns; REPORT; B069. Main matching REPORT locations [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) sensitivity-analysis method, [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5) result range.
- **Exact printed inputs:** SD=0.167; P=0.40. No estimate CI, LRT statistic, SE or arm-specific counts printed. SD zero/near-zero is a random-effect estimate, not a displayed P zero.
- **Population/model/definition:** D5; binomial GLMM site random intercept, null SD=0 vs SD>0, outcome agreement for disease-status-specific sensitivity or specificity. No participant-repeated random effect inferred.
- **Ordering/containment:** no interval present; SD nonnegative and P in [0,1]; interval endpoint/point-containment checks not applicable.
- **Sign/direction/label/scale:** SD nonnegative, caption/header accurately labels model parameter; P=0.40>.05 agrees with main non-significance. No probability-scale interpretation of SD.
- **Interval/P/test/statistic/SE compatibility:** direct hypothesis/label check coherent; exact LRT-P calculation unavailable because statistic, likelihoods and boundary reference-distribution rule missing. No inferential diagnostic derived from SD alone.
- **Matched occurrences:** 0.40 lies in main p5 range .16–.50; global minimum .16 and maximum .50 occur across this inventory; subgroup values do not conflict with the range.
- **Missing inputs/limits:** D5 exact model fit, LRT statistic and null-reference definition absent; numeric inversion not attempted. No independent supplied-source contradiction. P-display-zero policy retained; DISPLAY_ZERO_NOT_CANDIDATE is not assigned to SD=0 because its P is not zero.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S106

- **Scope and source:** Women Q17.0 Specificity; intention-to-screen day2; [joi190039supp3_prod.pdf#page=8](../../../joi190039supp3_prod.pdf#page=8) eTable6 exact sex/test/cutoff row, Specificity St.Dev. and p-value columns; REPORT; B069. Main matching REPORT locations [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) sensitivity-analysis method, [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5) result range.
- **Exact printed inputs:** SD=0; P=0.50. No estimate CI, LRT statistic, SE or arm-specific counts printed. SD zero/near-zero is a random-effect estimate, not a displayed P zero.
- **Population/model/definition:** D5; binomial GLMM site random intercept, null SD=0 vs SD>0, outcome agreement for disease-status-specific sensitivity or specificity. No participant-repeated random effect inferred.
- **Ordering/containment:** no interval present; SD nonnegative and P in [0,1]; interval endpoint/point-containment checks not applicable.
- **Sign/direction/label/scale:** SD nonnegative, caption/header accurately labels model parameter; P=0.50>.05 agrees with main non-significance. No probability-scale interpretation of SD.
- **Interval/P/test/statistic/SE compatibility:** direct hypothesis/label check coherent; exact LRT-P calculation unavailable because statistic, likelihoods and boundary reference-distribution rule missing. No inferential diagnostic derived from SD alone.
- **Matched occurrences:** 0.50 lies in main p5 range .16–.50; global minimum .16 and maximum .50 occur across this inventory; subgroup values do not conflict with the range.
- **Missing inputs/limits:** D5 exact model fit, LRT statistic and null-reference definition absent; numeric inversion not attempted. No independent supplied-source contradiction. P-display-zero policy retained; DISPLAY_ZERO_NOT_CANDIDATE is not assigned to SD=0 because its P is not zero.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S107

- **Scope and source:** Women L10.2 Sensitivity; intention-to-screen day2; [joi190039supp3_prod.pdf#page=8](../../../joi190039supp3_prod.pdf#page=8) eTable6 exact sex/test/cutoff row, Sensitivity St.Dev. and p-value columns; REPORT; B069. Main matching REPORT locations [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) sensitivity-analysis method, [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5) result range.
- **Exact printed inputs:** SD=4.35e-16; P=0.50. No estimate CI, LRT statistic, SE or arm-specific counts printed. SD zero/near-zero is a random-effect estimate, not a displayed P zero.
- **Population/model/definition:** D5; binomial GLMM site random intercept, null SD=0 vs SD>0, outcome agreement for disease-status-specific sensitivity or specificity. No participant-repeated random effect inferred.
- **Ordering/containment:** no interval present; SD nonnegative and P in [0,1]; interval endpoint/point-containment checks not applicable.
- **Sign/direction/label/scale:** SD nonnegative, caption/header accurately labels model parameter; P=0.50>.05 agrees with main non-significance. No probability-scale interpretation of SD.
- **Interval/P/test/statistic/SE compatibility:** direct hypothesis/label check coherent; exact LRT-P calculation unavailable because statistic, likelihoods and boundary reference-distribution rule missing. No inferential diagnostic derived from SD alone.
- **Matched occurrences:** 0.50 lies in main p5 range .16–.50; global minimum .16 and maximum .50 occur across this inventory; subgroup values do not conflict with the range.
- **Missing inputs/limits:** D5 exact model fit, LRT statistic and null-reference definition absent; numeric inversion not attempted. No independent supplied-source contradiction. P-display-zero policy retained; DISPLAY_ZERO_NOT_CANDIDATE is not assigned to SD=0 because its P is not zero.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S108

- **Scope and source:** Women L10.2 Specificity; intention-to-screen day2; [joi190039supp3_prod.pdf#page=8](../../../joi190039supp3_prod.pdf#page=8) eTable6 exact sex/test/cutoff row, Specificity St.Dev. and p-value columns; REPORT; B069. Main matching REPORT locations [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3) sensitivity-analysis method, [jama_brenner_2019_oi_190039.pdf#page=5](../../../jama_brenner_2019_oi_190039.pdf#page=5) result range.
- **Exact printed inputs:** SD=0; P=0.50. No estimate CI, LRT statistic, SE or arm-specific counts printed. SD zero/near-zero is a random-effect estimate, not a displayed P zero.
- **Population/model/definition:** D5; binomial GLMM site random intercept, null SD=0 vs SD>0, outcome agreement for disease-status-specific sensitivity or specificity. No participant-repeated random effect inferred.
- **Ordering/containment:** no interval present; SD nonnegative and P in [0,1]; interval endpoint/point-containment checks not applicable.
- **Sign/direction/label/scale:** SD nonnegative, caption/header accurately labels model parameter; P=0.50>.05 agrees with main non-significance. No probability-scale interpretation of SD.
- **Interval/P/test/statistic/SE compatibility:** direct hypothesis/label check coherent; exact LRT-P calculation unavailable because statistic, likelihoods and boundary reference-distribution rule missing. No inferential diagnostic derived from SD alone.
- **Matched occurrences:** 0.50 lies in main p5 range .16–.50; global minimum .16 and maximum .50 occur across this inventory; subgroup values do not conflict with the range.
- **Missing inputs/limits:** D5 exact model fit, LRT statistic and null-reference definition absent; numeric inversion not attempted. No independent supplied-source contradiction. P-display-zero policy retained; DISPLAY_ZERO_NOT_CANDIDATE is not assigned to SD=0 because its P is not zero.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

### Sex-interaction relationships: one outcome-specific unit per reported interaction

#### S109

- **Scope and source:** aspirin×sex interaction for Q10.2 sensitivity, intention-to-screen scheduled day2; REPORT [jama_brenner_2019_oi_190039.pdf#page=4](../../../jama_brenner_2019_oi_190039.pdf#page=4) interaction narrative, methods p3 and corresponding Table2 male/female rows p5; PLAN [joi190039supp2_prod.pdf#page=9](../../../joi190039supp2_prod.pdf#page=9) stratification model definition. Main M022; methods A051(11).
- **Exact printed inputs:** all interaction P values not statistically significant, shared range .08–.49. No outcome-specific exact P printed; this S record holds that shared bound, not an invented individual value. Applicable male/female arm probabilities and CIs reside in S001–S018 for matching test/outcome.
- **Population/model/definition:** D6, binomial GLM with sex-by-arm interaction; logit link specified in SAP. Coefficient, SE/covariance, statistic, test type, degrees of freedom and precise analysis-specific fit absent.
- **Ordering/containment:** no coefficient CI; .08<.49, bound within [0,1]. Exact result-specific endpoint/containment not available.
- **Sign/direction/label/scale:** narrative non-significance matches entire supplied P range >.05; interaction and within-stratum arm differences represent distinct hypotheses. No sign inferred for an unprinted coefficient.
- **Compatibility/repetitions:** interaction range coheres with source significance rule; no repeated outcome-specific interaction estimate/CI/P or compatible statistic is supplied. Different subgroup significance statuses do not reproduce an interaction contradiction.
- **Missing inputs/limits:** outcome-specific P allocation and model fit details named above. No candidate is emitted solely for unreported details.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S110

- **Scope and source:** aspirin×sex interaction for Q10.2 specificity, intention-to-screen scheduled day2; REPORT [jama_brenner_2019_oi_190039.pdf#page=4](../../../jama_brenner_2019_oi_190039.pdf#page=4) interaction narrative, methods p3 and corresponding Table2 male/female rows p5; PLAN [joi190039supp2_prod.pdf#page=9](../../../joi190039supp2_prod.pdf#page=9) stratification model definition. Main M022; methods A051(11).
- **Exact printed inputs:** all interaction P values not statistically significant, shared range .08–.49. No outcome-specific exact P printed; this S record holds that shared bound, not an invented individual value. Applicable male/female arm probabilities and CIs reside in S001–S018 for matching test/outcome.
- **Population/model/definition:** D6, binomial GLM with sex-by-arm interaction; logit link specified in SAP. Coefficient, SE/covariance, statistic, test type, degrees of freedom and precise analysis-specific fit absent.
- **Ordering/containment:** no coefficient CI; .08<.49, bound within [0,1]. Exact result-specific endpoint/containment not available.
- **Sign/direction/label/scale:** narrative non-significance matches entire supplied P range >.05; interaction and within-stratum arm differences represent distinct hypotheses. No sign inferred for an unprinted coefficient.
- **Compatibility/repetitions:** interaction range coheres with source significance rule; no repeated outcome-specific interaction estimate/CI/P or compatible statistic is supplied. Different subgroup significance statuses do not reproduce an interaction contradiction.
- **Missing inputs/limits:** outcome-specific P allocation and model fit details named above. No candidate is emitted solely for unreported details.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S111

- **Scope and source:** aspirin×sex interaction for Q17.0 sensitivity, intention-to-screen scheduled day2; REPORT [jama_brenner_2019_oi_190039.pdf#page=4](../../../jama_brenner_2019_oi_190039.pdf#page=4) interaction narrative, methods p3 and corresponding Table2 male/female rows p5; PLAN [joi190039supp2_prod.pdf#page=9](../../../joi190039supp2_prod.pdf#page=9) stratification model definition. Main M022; methods A051(11).
- **Exact printed inputs:** all interaction P values not statistically significant, shared range .08–.49. No outcome-specific exact P printed; this S record holds that shared bound, not an invented individual value. Applicable male/female arm probabilities and CIs reside in S001–S018 for matching test/outcome.
- **Population/model/definition:** D6, binomial GLM with sex-by-arm interaction; logit link specified in SAP. Coefficient, SE/covariance, statistic, test type, degrees of freedom and precise analysis-specific fit absent.
- **Ordering/containment:** no coefficient CI; .08<.49, bound within [0,1]. Exact result-specific endpoint/containment not available.
- **Sign/direction/label/scale:** narrative non-significance matches entire supplied P range >.05; interaction and within-stratum arm differences represent distinct hypotheses. No sign inferred for an unprinted coefficient.
- **Compatibility/repetitions:** interaction range coheres with source significance rule; no repeated outcome-specific interaction estimate/CI/P or compatible statistic is supplied. Different subgroup significance statuses do not reproduce an interaction contradiction.
- **Missing inputs/limits:** outcome-specific P allocation and model fit details named above. No candidate is emitted solely for unreported details.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S112

- **Scope and source:** aspirin×sex interaction for Q17.0 specificity, intention-to-screen scheduled day2; REPORT [jama_brenner_2019_oi_190039.pdf#page=4](../../../jama_brenner_2019_oi_190039.pdf#page=4) interaction narrative, methods p3 and corresponding Table2 male/female rows p5; PLAN [joi190039supp2_prod.pdf#page=9](../../../joi190039supp2_prod.pdf#page=9) stratification model definition. Main M022; methods A051(11).
- **Exact printed inputs:** all interaction P values not statistically significant, shared range .08–.49. No outcome-specific exact P printed; this S record holds that shared bound, not an invented individual value. Applicable male/female arm probabilities and CIs reside in S001–S018 for matching test/outcome.
- **Population/model/definition:** D6, binomial GLM with sex-by-arm interaction; logit link specified in SAP. Coefficient, SE/covariance, statistic, test type, degrees of freedom and precise analysis-specific fit absent.
- **Ordering/containment:** no coefficient CI; .08<.49, bound within [0,1]. Exact result-specific endpoint/containment not available.
- **Sign/direction/label/scale:** narrative non-significance matches entire supplied P range >.05; interaction and within-stratum arm differences represent distinct hypotheses. No sign inferred for an unprinted coefficient.
- **Compatibility/repetitions:** interaction range coheres with source significance rule; no repeated outcome-specific interaction estimate/CI/P or compatible statistic is supplied. Different subgroup significance statuses do not reproduce an interaction contradiction.
- **Missing inputs/limits:** outcome-specific P allocation and model fit details named above. No candidate is emitted solely for unreported details.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S113

- **Scope and source:** aspirin×sex interaction for L10.2 sensitivity, intention-to-screen scheduled day2; REPORT [jama_brenner_2019_oi_190039.pdf#page=4](../../../jama_brenner_2019_oi_190039.pdf#page=4) interaction narrative, methods p3 and corresponding Table2 male/female rows p5; PLAN [joi190039supp2_prod.pdf#page=9](../../../joi190039supp2_prod.pdf#page=9) stratification model definition. Main M022; methods A051(11).
- **Exact printed inputs:** all interaction P values not statistically significant, shared range .08–.49. No outcome-specific exact P printed; this S record holds that shared bound, not an invented individual value. Applicable male/female arm probabilities and CIs reside in S001–S018 for matching test/outcome.
- **Population/model/definition:** D6, binomial GLM with sex-by-arm interaction; logit link specified in SAP. Coefficient, SE/covariance, statistic, test type, degrees of freedom and precise analysis-specific fit absent.
- **Ordering/containment:** no coefficient CI; .08<.49, bound within [0,1]. Exact result-specific endpoint/containment not available.
- **Sign/direction/label/scale:** narrative non-significance matches entire supplied P range >.05; interaction and within-stratum arm differences represent distinct hypotheses. No sign inferred for an unprinted coefficient.
- **Compatibility/repetitions:** interaction range coheres with source significance rule; no repeated outcome-specific interaction estimate/CI/P or compatible statistic is supplied. Different subgroup significance statuses do not reproduce an interaction contradiction.
- **Missing inputs/limits:** outcome-specific P allocation and model fit details named above. No candidate is emitted solely for unreported details.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S114

- **Scope and source:** aspirin×sex interaction for L10.2 specificity, intention-to-screen scheduled day2; REPORT [jama_brenner_2019_oi_190039.pdf#page=4](../../../jama_brenner_2019_oi_190039.pdf#page=4) interaction narrative, methods p3 and corresponding Table2 male/female rows p5; PLAN [joi190039supp2_prod.pdf#page=9](../../../joi190039supp2_prod.pdf#page=9) stratification model definition. Main M022; methods A051(11).
- **Exact printed inputs:** all interaction P values not statistically significant, shared range .08–.49. No outcome-specific exact P printed; this S record holds that shared bound, not an invented individual value. Applicable male/female arm probabilities and CIs reside in S001–S018 for matching test/outcome.
- **Population/model/definition:** D6, binomial GLM with sex-by-arm interaction; logit link specified in SAP. Coefficient, SE/covariance, statistic, test type, degrees of freedom and precise analysis-specific fit absent.
- **Ordering/containment:** no coefficient CI; .08<.49, bound within [0,1]. Exact result-specific endpoint/containment not available.
- **Sign/direction/label/scale:** narrative non-significance matches entire supplied P range >.05; interaction and within-stratum arm differences represent distinct hypotheses. No sign inferred for an unprinted coefficient.
- **Compatibility/repetitions:** interaction range coheres with source significance rule; no repeated outcome-specific interaction estimate/CI/P or compatible statistic is supplied. Different subgroup significance statuses do not reproduce an interaction contradiction.
- **Missing inputs/limits:** outcome-specific P allocation and model fit details named above. No candidate is emitted solely for unreported details.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

### Plan/background and planning inferential relationships

#### S115

- **Scope and source:** Overall sample-size power; REPORT main p3/p6 and PLAN protocol p28; [jama_brenner_2019_oi_190039.pdf#page=3](../../../jama_brenner_2019_oi_190039.pdf#page=3); matching Protocol p28, main p6. Relevant map A003,A004,A016,A017,A020,A033–A035 or main M012/M084 as specified by the inputs.
- **Exact printed inputs:** 90% power; two-sided α=.05; sensitivity 60% versus36%, absolute increment24 percentage points; advanced-neoplasm prevalence10%; protocol100 diseased per arm and analysisN2000, targetN2400; continuity correction specified for planning.
- **Population/model/definition:** stated planning/historical population only; not a trial observed diagnostic contrast. Definition register D1–D7 provides matching boundaries; no plan method is used as an unprinted historical inferential definition.
- **Ordering/containment, sign/direction, label/scale, repeated-location and interval/P/test/statistic/SE checks:** Difference60−36=24; direction increase; probabilities and power/alpha within[0,1]. Mainp6 absolute24% matches mainp3 and protocolp28. No interval printed. Exact achieved power cannot be independently asserted without sample-size test formulation/variance/rounding; named continuity correction is a planning definition only. No observed trial P-test definition inferred.
- **Missing inputs/limits:** Exact planning test equation, rounding and allocation/variance not fully supplied.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S116

- **Scope and source:** Sex-specific sample-size power; PLAN protocol p28; [joi190039supp1_prod.pdf#page=28](../../../joi190039supp1_prod.pdf#page=28); matching Historical sensitivity71% planning context. Relevant map A003,A004,A016,A017,A020,A033–A035 or main M012/M084 as specified by the inputs.
- **Exact printed inputs:** 90% power; two-sidedα=.05 with continuity correction; expected aspirin sensitivity70% vs placebo36%; increment34 percentage points.
- **Population/model/definition:** stated planning/historical population only; not a trial observed diagnostic contrast. Definition register D1–D7 provides matching boundaries; no plan method is used as an unprinted historical inferential definition.
- **Ordering/containment, sign/direction, label/scale, repeated-location and interval/P/test/statistic/SE checks:** 70−36=34 percentage points; sign and probability labels coherent. No CI or result-P. Sex-specific diseased denominator not stated, so do not infer half of100 or equal sex balance. It is a distinct planning contrast from S115, not conflicting trial sensitivity.
- **Missing inputs/limits:** Exact sex-specific diseased sample size, sex ratio, planning equation/variance missing.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S117

- **Scope and source:** Shared expected specificity precision; PLAN protocol pp28–29; [joi190039supp1_prod.pdf#page=29](../../../joi190039supp1_prod.pdf#page=29); matching Protocolp28 sample-size assumptions and95%confidence definition. Relevant map A003,A004,A016,A017,A020,A033–A035 or main M012/M084 as specified by the inputs.
- **Exact printed inputs:** Expected specificity90% in both groups, expected95% CI88–92%; implied900 nondiseased/arm from100 diseased/arm,10%prevalence andN2000 assumptions.
- **Population/model/definition:** stated planning/historical population only; not a trial observed diagnostic contrast. Definition register D1–D7 provides matching boundaries; no plan method is used as an unprinted historical inferential definition.
- **Ordering/containment, sign/direction, label/scale, repeated-location and interval/P/test/statistic/SE checks:** 88<90<92; symmetric ordering/containment and probability scale coherent. Shared expectation for both arms is one common planning statement, not two independent observed results. Diagnostic simple normal proportion approximation at n900:90%±1.959964sqrt(.9×.1/900)×100≈[88.04,91.96]%, compatible with coarse integer endpoints. Diagnostic only; denominator is conditional on protocol assumptions, no new reported estimate.
- **Missing inputs/limits:** Actual precision method and explicit nondiseased denominator at this paragraph not printed;900 is conditional on plan assumptions.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S118

- **Scope and source:** Historical observational advanced-neoplasm sensitivity; PLAN protocolpp10,15; [joi190039supp1_prod.pdf#page=10](../../../joi190039supp1_prod.pdf#page=10); matching Protocolp15 repeats;mainp5 describes historical increase without numerical result. Relevant map A003,A004,A016,A017,A020,A033–A035 or main M012/M084 as specified by the inputs.
- **Exact printed inputs:** Aspirin70.8% vs nonuser35.9%; P=.001; prior prospective cohortN1979 atp15.
- **Population/model/definition:** stated planning/historical population only; not a trial observed diagnostic contrast. Definition register D1–D7 provides matching boundaries; no plan method is used as an unprinted historical inferential definition.
- **Ordering/containment, sign/direction, label/scale, repeated-location and interval/P/test/statistic/SE checks:** Positive34.9percentage-point historical difference matches narrative and .001 significance. Repeated percentages/P agree across protocolpp10,15. No CI/statistic/SE, exact diseased denominator or model printed;N1979 is cohortsize, not substituted as diseased denominator. Trial primary results S001/S003 use different population/drug regimen and are not repetitions.
- **Missing inputs/limits:** Historical disease-specific arm counts, sidedness, test/model/variance/multiplicity and inferential inputs absent.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S119

- **Scope and source:** Historical male AUC; PLAN protocolpp10,15 and graphical p16; [joi190039supp1_prod.pdf#page=15](../../../joi190039supp1_prod.pdf#page=15); matching Protocolp10 repeats;Figure1p16 ROC directions. Relevant map A003,A004,A016,A017,A020,A033–A035 or main M012/M084 as specified by the inputs.
- **Exact printed inputs:** Male ASA AUC.87 vs nonuser.68; P=.003; ROC Figure1 sensitivity%vertical and100−specificity%horizontal; cutpoints8,4,2,1µg/g.
- **Population/model/definition:** stated planning/historical population only; not a trial observed diagnostic contrast. Definition register D1–D7 provides matching boundaries; no plan method is used as an unprinted historical inferential definition.
- **Ordering/containment, sign/direction, label/scale, repeated-location and interval/P/test/statistic/SE checks:** Both AUCs in[0,1]; positive AUC increment.19 agrees with ROC/narrative greater discrimination. Repeated AUC/P agree acrosspp10,15. Figure curve orientation and axis complement coherent. No AUC CI, teststatistic/SE, covariance, groupdenominator or test method supplied; exact CI/P compatibility not available. Planned SAP DeLong/bootstrap is not presumed historical method.
- **Missing inputs/limits:** Historical AUC test/covariance/SE/sidedness/denominators absent; exact ROC coordinates not tabulated.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

#### S120

- **Scope and source:** Other historical aspirin/NSAID cohort sensitivity; PLAN protocolpp16–17; [joi190039supp1_prod.pdf#page=16](../../../joi190039supp1_prod.pdf#page=16); matching Different historical cohort; no corresponding randomized-trial contrast. Relevant map A003,A004,A016,A017,A020,A033–A035 or main M012/M084 as specified by the inputs.
- **Exact printed inputs:** Aspirin/NSAID advanced-neoplasm sensitivity increased51.2%→66.7%, described no significant difference and no specificity loss; no numericP.
- **Population/model/definition:** stated planning/historical population only; not a trial observed diagnostic contrast. Definition register D1–D7 provides matching boundaries; no plan method is used as an unprinted historical inferential definition.
- **Ordering/containment, sign/direction, label/scale, repeated-location and interval/P/test/statistic/SE checks:** Increase15.5percentagepoints; positive direction and probability scale coherent. Non-significant qualitative result cannot be contradicted from effect magnitude without denominator/variance. Distinct mixed aspirin/NSAID historical population and twoFITcontext; do not merge withS118. No CI/statistic/SE/P printed.
- **Missing inputs/limits:** Exact denominator, interval, P, test/model/sidedness/variance not supplied.
- **Candidate connection:** None from pass 1.
- **Pass 1:** PASS_1_COMPLETE
- **Pass 2:** PASS_2_COMPLETE

## Coverage closure and pass status

All 120 independent result relationships are registered. Observed trial tablepairs=108 (main36, eTables3–5 54, eTable6 18); sex-interaction contrasts=6; planning/background resultrelationships=6. No result relationship omitted for lack of a statistical model definition; missing definitions are recorded per S unit. Method-only prospective relationships are completely enumerated in D7, with no invented observed tests. Five lane-local candidates retain their exact compared locations/roles in checkers/statistical_pass_1.md; coordinator assigns stable C IDs later. All 120 relationships PASS_1_COMPLETE; all 120 PASS_2_COMPLETE. Source and reused assets unchanged. No web, GPU or arbitrary Python used.

