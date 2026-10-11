# Statistical Relationship Inventory — Workflow 1.6

Fresh statistical pass 2: `/root/stats2`, gpt-6.1-sol, high, FRESH_SPAWN; distinct from pass 1. All 112 original S IDs retain PASS_1_COMPLETE and now carry PASS_2_COMPLETE plus an explicit checked outcome/recheck implication. Pass-1 observations below are preserved as historical discovery provenance; the pass-2 lines supersede unsupported alignments identified in the complete current recheck. Two new endpoint-time-label observations P2-A/P2-B use existing S020/S038/S103 and S021/S039/S104, respectively; no relationship or candidate ID was deleted or added solely for another check rule. Complete records and candidate cards: checkers/statistical_pass_2.md; bounded parts: checkers/parts/statistical_pass_2_001.md, statistical_pass_2_002.md, statistical_pass_2_003.md.

Fresh statistical pass 1: `/root/stats1`, gpt-6.1-sol, high, FRESH_SPAWN. Scope comprises all 26 main-paper inferential families, all 46 support mapper keys, every historical comparative-score row, additional historical scalar statistics, model/code definitions, multiplicity, and ICU scale/aggregation definitions. Canonical inventory: **112 relationships**. This one shard contains fewer than the configured 120-relationship context bound. IDs S001–S026 retain the new main-mapper keys; S027–S039 separately track identity-link differences to avoid conflating them with ratio fits. Eight candidate observations are transmitted in the checker; no stable C IDs are assigned here.

Source identity by content: DOC-001 jama_parshuram_2018_oi_180015.pdf REPORT; DOC-002 joi180015supp1_prod.pdf PLAN; DOC-003 joi180015supp2_prod.pdf PLAN; DOC-004 joi180015supp3_prod.pdf REPORT. PLAN includes historical studies within the protocol. Exact physical PDF pages and table rows are recorded below.

Evidence engines: source-linked mapping artifacts and native/layout transcripts; targeted direct Poppler pdftotext -layout reads of DOC-001 pp1,4–8; DOC-002 pp1–7,14–16,19–20,29–30; DOC-003 all pp1–7; DOC-004 pp12–14. No output derivative, source or reused artifact changed. No Python, GPU, network or external sources. Main/supplement mapper graph readings are locators; exact printed values and definitions control statistical comparisons.

Checks for each inferential record: point-estimate containment, endpoint ordering, sign/direction, effect measure and scale, matched repetitions, and interval/P/test/statistic/SE compatibility only with source-supported inferential definitions. Where exact variance, reference distribution, P-to-model allocation or other inputs are missing, checks stop at the printed relationships and name that limitation. Approximations below are diagnostics, never replacements for reported analyses. There are no coherent displayed-zero P values in the mapped supplied results; no zero-format candidate was emitted.

## Complete support-key binding

SUP-H01–SUP-H22 → S040–S061 individually in order; SUP-H23 → S062. SUP-P01 → S026; SUP-P02 → S063; SUP-P03 → S064; SUP-P04 → S065; SUP-P05 → S066. SUP-G01 → S027 (fitted mortality rate difference) and S023 (slope interpretation); SUP-G02 → S008. SUP-E01 → S024; SUP-E02 → S025; SUP-E03–SUP-E15 → S067–S079 individually in order; SUP-E16 → S080. These bindings cover every support inferential key; historical Table 1 adds S081–S088, and additional definitions/results add S089–S112.

## S001 — Heart-rate documentation

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** 0.58 lies within −0.11–1.26; heart-rate frequency is a per-patient 24-hour mean, not a patient-day event rate. Raw .10 and Holm .30 stay distinct. C004 concerns an extremum, not these assessment totals; no new candidate.
- **Locations and document roles:** DOC-001 p6 Table 2 REPORT.
- **Printed inputs:** 0.58 (−0.11,1.26); P=.10; Holm=.30.
- **Model, test and inferential definitions:** Gaussian identity GEE; exchangeable hospital clusters; hospital baseline mean and group.
- **Checks and outcome:** Contained; ordered; positive estimate with interval crossing zero; raw/adjusted P direction coherent; no numeric narrative repetition. 
- **Missing definitions / limits:** Exact covariance estimator and reference distribution absent; no exact CI/P equivalence asserted.

## S002 — Respiratory-rate documentation

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** 0.85 lies within 0.02–1.68; narrative/table match. A raw P rounded to .05 is compatible with a positive CI at displayed precision; .18 is separately multiplicity-adjusted. No new candidate.
- **Locations and document roles:** DOC-001 p6 Table 2 and narrative REPORT.
- **Printed inputs:** 0.85 (0.02,1.68); P=.05; Holm=.18.
- **Model, test and inferential definitions:** Gaussian identity GEE; same hospital/baseline definition.
- **Checks and outcome:** Contained; ordered; positive; narrative repeats; CI excludes zero but two-decimal raw P can round to .05. Diagnostic normal z≈2.01 gives P≈.045; Holm four remaining comparisons can give .18. No candidate. 
- **Missing definitions / limits:** Diagnostic approximation only; exact estimator, reference distribution and unrounded P absent.

## S003 — Systolic-pressure documentation

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** 1.12 lies within 0.59–1.65; positive documentation direction and repeated <.001 agree. Hospital/baseline adjustment is explicit; neither crude mean subtraction nor event-rate conversion reconstructs this fit. No new candidate.
- **Locations and document roles:** DOC-001 p6 Table 2 and narrative REPORT.
- **Printed inputs:** 1.12 (0.59,1.65); raw/Holm P<.001.
- **Model, test and inferential definitions:** Gaussian identity GEE; hospital/baseline definition.
- **Checks and outcome:** Contained; ordered; positive interval and increase narrative coherent; repetition matches. 
- **Missing definitions / limits:** Exact variance/reference distribution absent; exact CI/P calculation not attempted.

## S004 — Oxygen-saturation documentation

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** 1.06 lies within 0.27–1.85; narrative repetition matches. Raw .009 and Holm .04 have different adjustment roles, with adjusted P no smaller. No new candidate.
- **Locations and document roles:** DOC-001 p6 Table 2 and narrative REPORT.
- **Printed inputs:** 1.06 (0.27,1.85); P=.009; Holm=.04.
- **Model, test and inferential definitions:** Gaussian identity GEE; hospital/baseline definition.
- **Checks and outcome:** Contained; ordered; positive; matches narrative. Diagnostic normal z≈2.63/P≈.0085 can round to .009 and fivefold Holm≈.0425 to .04; no contradiction. 
- **Missing definitions / limits:** Diagnostic only; exact covariance/reference distribution and unrounded P missing.

## S005 — Respiratory-effort documentation

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** 4.67 lies within 3.23–6.12; respiratory-effort frequency direction and narrative match. Assessment count is the sampling denominator, not the event count. No new candidate.
- **Locations and document roles:** DOC-001 p6 Table 2 and narrative REPORT.
- **Printed inputs:** 4.67 (3.23,6.12); raw/Holm P<.001.
- **Model, test and inferential definitions:** Gaussian identity GEE; hospital/baseline definition.
- **Checks and outcome:** Contained; ordered; positive; matched narrative and multiplicity bounds coherent. 
- **Missing definitions / limits:** Exact covariance/reference distribution absent.

## S006 — Capillary-refill documentation

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** 4.65 lies within 3.49–5.80; capillary-refill frequency direction and repeated values match. No ledger/recheck fact changes this model or scale. No new candidate.
- **Locations and document roles:** DOC-001 p6 Table 2 and narrative REPORT.
- **Printed inputs:** 4.65 (3.49,5.80); raw/Holm P<.001.
- **Model, test and inferential definitions:** Gaussian identity GEE; hospital/baseline definition.
- **Checks and outcome:** Contained; ordered; positive; matched narrative and multiplicity bounds coherent. 
- **Missing definitions / limits:** Exact covariance/reference distribution absent.

## S007 — Oxygen-therapy documentation

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** 0.37 lies within −0.71–1.46; crossing zero and raw .50 are compatible qualitatively. Holm >.99 is an adjusted probability bound, not a conflicting raw test. No new candidate.
- **Locations and document roles:** DOC-001 p6 Table 2 REPORT.
- **Printed inputs:** 0.37 (−0.71,1.46); P=.50; Holm>.99.
- **Model, test and inferential definitions:** Gaussian identity GEE; hospital/baseline definition.
- **Checks and outcome:** Contained; ordered; interval crosses zero; raw nonsignificant; adjusted near one coherent with final Holm multiplier. 
- **Missing definitions / limits:** Exact covariance/reference distribution and unrounded P absent.

## S008 — Observation completeness ≥5/7

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** 38.1 percentage points lies within 20.8–55.4; 960/1270,2563/2588,883/1419,1725/2832 define last observation-set completeness. Those binary proportions differ from seven documentation-frequency means. Main/eFigure direction agrees; no inference from graph bars or crude differences. No new candidate.
- **Locations and document roles:** DOC-001 p6 Table 2/narrative REPORT; DOC-004 p4–5 eFigure 2 REPORT; mapper SUP-G02.
- **Printed inputs:** 38.1 percentage points (20.8,55.4); raw/Holm P<.001; 960/1270,2563/2588,883/1419,1725/2832.
- **Model, test and inferential definitions:** Binomial identity GEE; hospital baseline proportion; last observation set; eFigure same last-set/≥5 definition.
- **Checks and outcome:** Contained; ordered; positive interval; supplement significance/direction agrees. Counts/denominators differ from frequency means as expected. No invented effect from graphical bars. 
- **Missing definitions / limits:** Exact covariance/reference distribution/unrounded P absent. eFigure gives no separate numeric CI/P.

## S009 — Hospital mortality ratio

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** OR1.01 lies within 0.61–1.69; hospital-discharge exposure agrees with mortality counts and repeated main result. C005 changes a site maximum only, leaving total94366 intact; C001–C003 affect graph attribution/time wording, not a different numerical OR. No new candidate.
- **Locations and document roles:** DOC-001 p1 abstract,p6 narrative,p7 Table 3,p8 discussion REPORT; DOC-003 p1–3 PLAN model definitions.
- **Printed inputs:** OR 1.01 (0.61,1.69); P=.96; denominator hospital discharges.
- **Model, test and inferential definitions:** Logistic GEE; baseline adjusted; exchangeable hospital clusters; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; positive ratio scale. No reduction claim; CI crosses one; repetitions agree. No exact CI/P compatibility conclusion. 
- **Missing definitions / limits:** 95% confidence level and main two-sided .05 supplied; variance estimator, covariance, exact reference distribution and P-column assignment to a particular model are not explicitly supplied.

## S010 — Mortality without DNR ratio

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** OR2.05 lies within 0.64–6.61; without-DNR endpoint and nonsignificance match main repetitions. Difference S028 is a distinct identity-link fit; no aggregate OR reconstruction. No new candidate in this fitted result.
- **Locations and document roles:** DOC-001 p6 narrative,p7 Table 3,p8 discussion REPORT; DOC-003 p1–3 PLAN model definitions.
- **Printed inputs:** OR 2.05 (0.64,6.61); P=.23; denominator hospital discharges.
- **Model, test and inferential definitions:** Logistic GEE; baseline adjusted; exchangeable hospital clusters; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; positive ratio scale. Positive OR direction; nonsignificant narrative and CI crossing one agree. No exact CI/P compatibility conclusion. 
- **Missing definitions / limits:** 95% confidence level and main two-sided .05 supplied; variance estimator, covariance, exact reference distribution and P-column assignment to a particular model are not explicitly supplied.

## S011 — Significant clinical deterioration ratio

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** RR0.77 lies within 0.61–0.97; P=.03 and reduction narrative align qualitatively. C011/C012 retain fluid-boundary/conjunction definition questions; affected event counts are absent. S029 uses baseline-unadjusted identity fit and need not share null exclusion. No new candidate.
- **Locations and document roles:** DOC-001 p1 abstract,p6 narrative,p7 Table 3,p9 discussion REPORT; DOC-003 p1–3 PLAN model definitions.
- **Printed inputs:** RR 0.77 (0.61,0.97); P=.03; denominator ward patient-days.
- **Model, test and inferential definitions:** Poisson log GEE; baseline adjusted; exchangeable hospital clusters; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; positive ratio scale. Reduction/CI below one/raw significance agree. Its separate identity model S029 is baseline-unadjusted; differing null exclusion is not a contradiction. No exact CI/P compatibility conclusion. 
- **Missing definitions / limits:** 95% confidence level and main two-sided .05 supplied; variance estimator, covariance, exact reference distribution and P-column assignment to a particular model are not explicitly supplied.

## S012 — ICU mortality ratio

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** OR0.89 lies within 0.51–1.57 on ICU-discharge scale. C013's blanket ICU-day wording does not convert this explicitly discharge-based binary outcome into a duration rate; patient cohort S024 is distinct. No new candidate.
- **Locations and document roles:** DOC-001 p7 Table 3,p9 discussion REPORT; DOC-003 p1–3 PLAN model definitions.
- **Printed inputs:** OR 0.89 (0.51,1.57); P=.69; denominator ICU discharges.
- **Model, test and inferential definitions:** Logistic GEE; baseline adjusted; exchangeable hospital clusters; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; positive ratio scale. CI crosses one; no-significant-reduction narrative agrees; admission-event aggregate differs from S024 per-patient cohort. No exact CI/P compatibility conclusion. 
- **Missing definitions / limits:** 95% confidence level and main two-sided .05 supplied; variance estimator, covariance, exact reference distribution and P-column assignment to a particular model are not explicitly supplied.

## S013 — ICU mortality ratio

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** OR0.95 lies within 0.48–1.86; hospital-discharge denominator separates it from S012 despite common mortality numerator. Their unequal estimates are not duplicate-value errors. No new candidate.
- **Locations and document roles:** DOC-001 p7 Table 3,p9 discussion REPORT; DOC-003 p1–3 PLAN model definitions.
- **Printed inputs:** OR 0.95 (0.48,1.86); P=.88; denominator hospital discharges.
- **Model, test and inferential definitions:** Logistic GEE; baseline adjusted; exchangeable hospital clusters; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; positive ratio scale. CI crosses one; interpretation coherent; distinct denominator from S012 retained. No exact CI/P compatibility conclusion. 
- **Missing definitions / limits:** 95% confidence level and main two-sided .05 supplied; variance estimator, covariance, exact reference distribution and P-column assignment to a particular model are not explicitly supplied.

## S014 — Cardiac arrest ratio

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** RR1.02 lies within 0.65–1.62; ward-day exposure and nonsignificance align. C008 retains PLAN intensity-code contradiction without quantifiable effect on reported59 events. Rounded S032 zero is an effect estimate, not a displayed P zero. No new candidate.
- **Locations and document roles:** DOC-001 p6 narrative,p7 Table 3,p9 discussion REPORT; DOC-003 p1–3 PLAN model definitions.
- **Printed inputs:** RR 1.02 (0.65,1.62); P=.92; denominator ward patient-days.
- **Model, test and inferential definitions:** Poisson log GEE; baseline adjusted; exchangeable hospital clusters; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; positive ratio scale. Near-null positive ratio; CI crosses one; interpretation agrees. No exact CI/P compatibility conclusion. 
- **Missing definitions / limits:** 95% confidence level and main two-sided .05 supplied; variance estimator, covariance, exact reference distribution and P-column assignment to a particular model are not explicitly supplied.

## S015 — Potentially preventable cardiac arrest ratio

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** RR0.87 lies within 0.49–1.54; C009 affects the PLAN threshold at rating4 but supplies no rating matrix or count change. Main threshold includes4; no numerical RR contradiction reproduced. No new candidate.
- **Locations and document roles:** DOC-001 p6 narrative,p7 Table 3,p9 discussion REPORT; DOC-003 p1–3 PLAN model definitions.
- **Printed inputs:** RR 0.87 (0.49,1.54); P=.62; denominator ward patient-days.
- **Model, test and inferential definitions:** Poisson log GEE; baseline adjusted; exchangeable hospital clusters; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; positive ratio scale. Negative log-ratio direction; CI crosses one; interpretation agrees. No exact CI/P compatibility conclusion. 
- **Missing definitions / limits:** 95% confidence level and main two-sided .05 supplied; variance estimator, covariance, exact reference distribution and P-column assignment to a particular model are not explicitly supplied.

## S016 — Immediate resuscitation-team calls ratio

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** RR0.98 lies within 0.82–1.17 and matches narrative. Small positive S034 difference is separately fitted; no source-supplied identity forces its sign to match log-link RR. No new candidate.
- **Locations and document roles:** DOC-001 p7 Table 3,p8 narrative REPORT; DOC-003 p1–3 PLAN model definitions.
- **Printed inputs:** RR 0.98 (0.82,1.17); P=.83; denominator ward patient-days.
- **Model, test and inferential definitions:** Poisson log GEE; baseline adjusted; exchangeable hospital clusters; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; positive ratio scale. CI crosses one; repeated ratio/P match. Opposite sign of tiny S034 identity difference can arise from separately fitted links; no common-estimator identity supplied. No exact CI/P compatibility conclusion. 
- **Missing definitions / limits:** 95% confidence level and main two-sided .05 supplied; variance estimator, covariance, exact reference distribution and P-column assignment to a particular model are not explicitly supplied.

## S017 — Immediate physician calls ratio

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** RR1.17 lies within 0.73–1.88; narrative/table agree. C028 recheck removes assumed generic-adjusted=baseline-adjusted equivalence for S035; ratio remains separate and baseline-adjusted. No new candidate.
- **Locations and document roles:** DOC-001 p7 Table 3,p8 narrative REPORT; DOC-003 p1–3 PLAN model definitions.
- **Printed inputs:** RR 1.17 (0.73,1.88); P=.52; denominator ward patient-days.
- **Model, test and inferential definitions:** Poisson log GEE; baseline adjusted; exchangeable hospital clusters; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; positive ratio scale. CI crosses one; repeats match; S035 identity model unadjusted; no forced covariance. No exact CI/P compatibility conclusion. 
- **Missing definitions / limits:** 95% confidence level and main two-sided .05 supplied; variance estimator, covariance, exact reference distribution and P-column assignment to a particular model are not explicitly supplied.

## S018 — Urgent ICU consultations <15 min ratio

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** RR1.05 lies within 0.85–1.30; consultation <15-min endpoint, ward-day exposure, and repetitions agree. Do not use ICU durations as denominator. No new candidate.
- **Locations and document roles:** DOC-001 p7 Table 3,p8 narrative REPORT; DOC-003 p1–3 PLAN model definitions.
- **Printed inputs:** RR 1.05 (0.85,1.30); P=.64; denominator ward patient-days.
- **Model, test and inferential definitions:** Poisson log GEE; baseline adjusted; exchangeable hospital clusters; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; positive ratio scale. CI crosses one; repeats and interpretation match. No exact CI/P compatibility conclusion. 
- **Missing definitions / limits:** 95% confidence level and main two-sided .05 supplied; variance estimator, covariance, exact reference distribution and P-column assignment to a particular model are not explicitly supplied.

## S019 — Urgent ICU admission ratio

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** RR0.95 lies within 0.82–1.09; urgent-admission events828/1178 are not unique patients686/967. C015 patient/discharge PIM question cannot force these distinct populations equal. No new candidate.
- **Locations and document roles:** DOC-001 p7 Table 3,p9 discussion REPORT; DOC-003 p1–3 PLAN model definitions.
- **Printed inputs:** RR 0.95 (0.82,1.09); P=.45; denominator ward patient-days.
- **Model, test and inferential definitions:** Poisson log GEE; baseline adjusted; exchangeable hospital clusters; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; positive ratio scale. CI crosses one; negative log-ratio coherent. No exact CI/P compatibility conclusion. 
- **Missing definitions / limits:** 95% confidence level and main two-sided .05 supplied; variance estimator, covariance, exact reference distribution and P-column assignment to a particular model are not explicitly supplied.

## S020 — ICU readmission <48 h ratio

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** OR1.11 lies within 0.77–1.61; C014 denominator conflict and C016 Poisson/logistic label conflict remain separate. Recheck removes nonexistent protocol ICU-readmission logit comparator: C016 P_R only. New P2-A: REPORT Table3 <48h label differs from REPORT eTable1 before-third-midnight cutoff, admitting a70h example. No affected event count inferred.
- **Locations and document roles:** DOC-001 p6 narrative,p7 Table 3 REPORT; DOC-003 p1–3 PLAN model definitions.
- **Printed inputs:** OR 1.11 (0.77,1.61); P=.58; denominator ICU discharges.
- **Model, test and inferential definitions:** Logistic GEE; baseline adjusted; exchangeable hospital clusters; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; positive ratio scale. CI/P narrative coherent. SAP p5 Poisson shell gives candidate ST-E label/model comparison; see S103. No exact CI/P compatibility conclusion. 
- **Missing definitions / limits:** 95% confidence level and main two-sided .05 supplied; variance estimator, covariance, exact reference distribution and P-column assignment to a particular model are not explicitly supplied.

## S021 — Hospital readmission <48 h ratio

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** OR0.93 lies within 0.61–1.41; C017 Poisson/logistic model conflict retains protocol hospital-readmission comparator. New P2-B: REPORT Table3 <48h label differs from REPORT eTable1 before-third-midnight cutoff, admitting a70h example. Separate endpoint from P2-A; hospital-discharge denominator remains coherent.
- **Locations and document roles:** DOC-001 p6 narrative,p7 Table 3 REPORT; DOC-003 p1–3 PLAN model definitions.
- **Printed inputs:** OR 0.93 (0.61,1.41); P=.74; denominator hospital discharges.
- **Model, test and inferential definitions:** Logistic GEE; baseline adjusted; exchangeable hospital clusters; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; positive ratio scale. CI/P narrative coherent. SAP p5 Poisson shell gives candidate ST-F label/model comparison; see S104; protocol p16 corroborates logistic. No exact CI/P compatibility conclusion. 
- **Missing definitions / limits:** 95% confidence level and main two-sided .05 supplied; variance estimator, covariance, exact reference distribution and P-column assignment to a particular model are not explicitly supplied.

## S022 — Preventability inter-rater weighted kappa

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Weighted kappa .35 lies within .15–.51 and its scale bounds. C009 is an endpoint dichotomy threshold question; preventable proportions21/27 and29/32 do not supply kappa weights, rating matrix or variance. No new candidate.
- **Locations and document roles:** DOC-001 p7 Table 3 footnote i REPORT.
- **Printed inputs:** weighted κ=.35 (.15,.51), 95%; 21/27 vs 29/32 preventable; third arbitration 5.
- **Model, test and inferential definitions:** Two blinded reviewers; six-point preventability; weighted kappa method not further specified.
- **Checks and outcome:** Contained; ordered; κ within −1 to1. Proportions are event classifications, not significance tests or CI denominators. No matched repetition discrepancy. 
- **Missing definitions / limits:** Kappa weights, SE/variance, interval construction and underlying rating matrix absent; P absent.

## S023 — Mortality fitted slopes and slope-difference test

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Slopes .57/.53 and difference P=.94 do not contradict without slope SE/covariance and test definitions. C001/C002 reproduce reversed group encoding; C003 reproduces x-axis time wording against hospital C coordinates. These are existing label candidates, not newly reconstructed fitted statistics. No new candidate.
- **Locations and document roles:** DOC-001 p8 Figure 2 caption REPORT; DOC-004 p2–3 eFigure 1 REPORT.
- **Printed inputs:** BP slope .57; UC slope .53; difference P=.94; equal-slopes assumption.
- **Model, test and inferential definitions:** Linearized baseline-versus-intervention mortality fits; slope-difference test unspecified.
- **Checks and outcome:** Printed slope difference .04 and high P can coexist without supplied slope SEs. Caption says slope difference not different from zero, not both slopes zero. Color/line assignment issues remain cross-source/numeric lane; no inferential candidate. 
- **Missing definitions / limits:** Slope covariance/SE, fit weights and test/reference distribution absent; no CI. Do not impute plotted coordinates.

## S024 — Urgent-ICU patient mortality

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** −1.55 lies within −4.90–1.80 percentage points; main/eTable4 repetitions agree. 42+67=109 deaths and686+967=1653 unique patients reconcile. Admission-event mortality S012/S013 has different aggregation; C013 scope wording does not alter this explicitly patient-based result. No new candidate.
- **Locations and document roles:** DOC-001 p8 Other Outcomes REPORT; DOC-004 p12–13 eTable 4 REPORT; SUP-E01.
- **Printed inputs:** −1.55 percentage points (−4.90,1.80), P=.36; 42/686=6.1%,67/967=6.9%; total 109.
- **Model, test and inferential definitions:** Patient-level binomial identity GEE; baseline outcome adjustment; hospital clustering; excludes cross-period patients.
- **Checks and outcome:** Contained; ordered; negative; CI crosses zero and narrative nonsignificance coherent. Exact main/supplement estimate/CI/P repetitions agree. Distinguish S012/S013 admission-event populations. 
- **Missing definitions / limits:** Exact covariance estimator/reference distribution absent; no exact CI/P test reconstruction.

## S025 — PIM-2 predicted mortality

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** +.69 lies within −.54–1.92 percentage points; repeated main/eTable result matches. C015 retains SAP patient/discharge label conflict; C023 is upper example's conditional cap/rounding question, not a proof predictions or fitted mean difference are wrong. Rounded expected counts are not binomial observations. No new candidate.
- **Locations and document roles:** DOC-001 p8 Other Outcomes REPORT; DOC-004 p12–13 eTable 4 REPORT; SUP-E02.
- **Printed inputs:** +.69 percentage points (−.54,1.92), P=.27; predicted5.5% vs4.6%.
- **Model, test and inferential definitions:** Baseline-adjusted patient GEE; inverse-logit prediction averaged over admissions then summed across patients; exact continuous-versus-binary fitting choice not expressly bound to this row.
- **Checks and outcome:** Contained; ordered; positive point estimate with zero-crossing interval; exact REPORT repetitions agree. Predicted integer sums are rounded expectations, not observed binary deaths. 
- **Missing definitions / limits:** Exact row variance/family/SE/reference distribution missing; do not treat rounded predicted counts as observed binomial data.

## S026 — Mortality sample-size/power

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** C007 scale contradiction persists: .9/1000=.09%, whereas PLAN appendix gives .9%. C006 recheck supports2397=20×119.85 power beds versus2322 participating-site beds; do not carry unsupported same-basis alignment into power. Compelling1/1000 and detectable.9/1000 remain distinct; no new candidate.
- **Locations and document roles:** DOC-001 p4 Sample Size REPORT; DOC-002 p1,p14,p29 PLAN; SUP-P01.
- **Printed inputs:** baseline5.1/1000; compelling1/1000 reduction (to4.1); detectable.9/1000≈.09%; RRR18%/.178; p29 printed ARR.9%;20hospitals,119/119.85beds,occupancy.9,LOS4,k.15,power.8,two-sidedα.05; allow1–2attrition→22.
- **Model, test and inferential definitions:** Cluster method named; formula absent from package. Distinguish compelling clinical target1 from detectable.9.
- **Checks and outcome:** Power not independently recalculated absent formula; arithmetic scale check gives ST-A: .9/1000=.09%, while p29 says .9%. RRR .178×5.1=.9078/1000 consistent with .9/1000; .9% is ten times. 
- **Missing definitions / limits:** Exact power formula, cluster-size derivation/time basis missing; no invented cluster variance.

## S027 — hospital mortality identity-link difference

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** .01 lies within −.80–.81 per1000 hospital discharges; matches eFigure caption. Narrative .8 uses fewer decimals and reconciles endpoint precision. C001–C003 graph labeling does not alter this difference. Ratio P=.96 is not assigned to identity fit. No new candidate.
- **Locations and document roles:** DOC-001 p7 Table 3 and footnote a REPORT; DOC-003 p1–3 PLAN; SUP-G01; DOC-004 p3 caption REPORT.
- **Printed inputs:** .01 (−.80,.81) per1000 corresponding denominator;95%CI.
- **Model, test and inferential definitions:** binomial identity GEE; adjusted; hospital clustering; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; interval crosses zero; scale per1000 events or discharges as labeled. Separate fitted ratio S009 tracked independently. No P expressly allocated to this identity-link model; do not compare row P with this CI. Repetitions agree where provided. 
- **Missing definitions / limits:** Difference-specific P/test/SE/variance/reference distribution absent. Model nonconvergence fallback expressly disclosed; do not infer equality with baseline-adjusted ratio. Main p8 states the CI excludes differences greater than 0.8 deaths per1000 in either direction. The displayed upper endpoint +0.81 rounds to +0.8 at the narrative's one-decimal precision, and −0.80 rounds to −0.8. This coherent change of displayed precision does not independently support a candidate; no supplied exact-boundary or different rounding rule contradicts it.

## S028 — mortality without DNR identity-link difference

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** .36 lies within −.53–1.25 per1000 hospital discharges; matches main narrative. Separate logistic ratio S010 is not a deterministic transform of this identity fit. No difference-specific P supplied; no new candidate.
- **Locations and document roles:** DOC-001 p7 Table 3 and footnote a REPORT; DOC-003 p1–3 PLAN; .
- **Printed inputs:** .36 (−.53,1.25) per1000 corresponding denominator;95%CI.
- **Model, test and inferential definitions:** binomial identity GEE; adjusted; hospital clustering; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; interval crosses zero; scale per1000 events or discharges as labeled. Separate fitted ratio S010 tracked independently. No P expressly allocated to this identity-link model; do not compare row P with this CI. Repetitions agree where provided. 
- **Missing definitions / limits:** Difference-specific P/test/SE/variance/reference distribution absent. Model nonconvergence fallback expressly disclosed; do not infer equality with baseline-adjusted ratio.

## S029 — significant clinical deterioration identity-link difference

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** −.34 lies within −.73–.05 per1000 ward days; repetitions match. C027 recheck identifies unsupported generic-adjusted=baseline-adjusted assumption: clustering persists while baseline adjustment was removed. C011/C012 endpoint questions remain bounded; ratio .77/P=.03 cannot be assigned to this fit. No new candidate.
- **Locations and document roles:** DOC-001 p7 Table 3 and footnote a REPORT; DOC-003 p1–3 PLAN; ;DOC-001 p1 abstract,p6 narrative REPORT.
- **Printed inputs:** −.34 (−.73,.05) per1000 corresponding denominator;95%CI.
- **Model, test and inferential definitions:** Poisson identity GEE; unadjusted baseline; hospital clustering; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; interval crosses zero; scale per1000 events or discharges as labeled. Separate fitted ratio S011 tracked independently. No P expressly allocated to this identity-link model; do not compare row P with this CI. Repetitions agree where provided. 
- **Missing definitions / limits:** Difference-specific P/test/SE/variance/reference distribution absent. Model nonconvergence fallback expressly disclosed; do not infer equality with baseline-adjusted ratio. Independent ST-G comparison: abstract/narrative call this difference adjusted, whereas footnote a explicitly says SCDE model was not adjusted for baseline. This concerns adjustment labeling, not differing ratio/difference null exclusion.

## S030 — ICU mortality /ICU discharges identity-link difference

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** −3.01 lies within −12.26–6.25 per1000 ICU discharges; denominator differs from S031. C014 pertains readmission, not imposing hospital denominator on this separately labeled mortality row. No new candidate.
- **Locations and document roles:** DOC-001 p7 Table 3 and footnote a REPORT; DOC-003 p1–3 PLAN; .
- **Printed inputs:** −3.01 (−12.26,6.25) per1000 corresponding denominator;95%CI.
- **Model, test and inferential definitions:** binomial identity GEE; adjusted; hospital clustering; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; interval crosses zero; scale per1000 events or discharges as labeled. Separate fitted ratio S012 tracked independently. No P expressly allocated to this identity-link model; do not compare row P with this CI. Repetitions agree where provided. 
- **Missing definitions / limits:** Difference-specific P/test/SE/variance/reference distribution absent. Model nonconvergence fallback expressly disclosed; do not infer equality with baseline-adjusted ratio.

## S031 — ICU mortality /hospital discharges identity-link difference

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** −.11 lies within −.73–.51 per1000 hospital discharges; common death numerator does not make this an ICU-discharge fit. Model and scale remain separate from S030. No new candidate.
- **Locations and document roles:** DOC-001 p7 Table 3 and footnote a REPORT; DOC-003 p1–3 PLAN; .
- **Printed inputs:** −.11 (−.73,.51) per1000 corresponding denominator;95%CI.
- **Model, test and inferential definitions:** binomial identity GEE; adjusted; hospital clustering; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; interval crosses zero; scale per1000 events or discharges as labeled. Separate fitted ratio S013 tracked independently. No P expressly allocated to this identity-link model; do not compare row P with this CI. Repetitions agree where provided. 
- **Missing definitions / limits:** Difference-specific P/test/SE/variance/reference distribution absent. Model nonconvergence fallback expressly disclosed; do not infer equality with baseline-adjusted ratio.

## S032 — cardiac arrest identity-link difference

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** 0 lies within −.06–.07 per1000 ward days, with baseline adjustment removed as disclosed. Displayed zero is a rounded difference estimate, not P=0. C008 retains scale-code question without event-level impact reconstruction. No new candidate.
- **Locations and document roles:** DOC-001 p7 Table 3 and footnote a REPORT; DOC-003 p1–3 PLAN; .
- **Printed inputs:** 0 (−.06,.07) per1000 corresponding denominator;95%CI.
- **Model, test and inferential definitions:** Poisson identity GEE; unadjusted baseline; hospital clustering; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; interval crosses zero; scale per1000 events or discharges as labeled. Separate fitted ratio S014 tracked independently. No P expressly allocated to this identity-link model; do not compare row P with this CI. Repetitions agree where provided. 
- **Missing definitions / limits:** Difference-specific P/test/SE/variance/reference distribution absent. Model nonconvergence fallback expressly disclosed; do not infer equality with baseline-adjusted ratio.

## S033 — potentially preventable cardiac arrest identity-link difference

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** −.02 lies within −.07–.02 per1000 ward days. C009 threshold question does not supply event ratings to change numerator or fit. Separate S015 ratio fit retained; no new candidate.
- **Locations and document roles:** DOC-001 p7 Table 3 and footnote a REPORT; DOC-003 p1–3 PLAN; .
- **Printed inputs:** −.02 (−.07,.02) per1000 corresponding denominator;95%CI.
- **Model, test and inferential definitions:** Poisson identity GEE; adjusted; hospital clustering; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; interval crosses zero; scale per1000 events or discharges as labeled. Separate fitted ratio S015 tracked independently. No P expressly allocated to this identity-link model; do not compare row P with this CI. Repetitions agree where provided. 
- **Missing definitions / limits:** Difference-specific P/test/SE/variance/reference distribution absent. Model nonconvergence fallback expressly disclosed; do not infer equality with baseline-adjusted ratio.

## S034 — resuscitation-team calls identity-link difference

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** .02 lies within −.07–.10 per1000 ward days and main narrative matches. Separate RR .98 may differ in near-null direction under different links; no same-estimator constraint exists. C021 is historical power-unit wording, not this final fitted estimate. No new candidate.
- **Locations and document roles:** DOC-001 p7 Table 3 and footnote a REPORT; DOC-003 p1–3 PLAN; DOC-001 p8 REPORT repeat.
- **Printed inputs:** .02 (−.07,.10) per1000 corresponding denominator;95%CI.
- **Model, test and inferential definitions:** Poisson identity GEE; adjusted; hospital clustering; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; interval crosses zero; scale per1000 events or discharges as labeled. Separate fitted ratio S016 tracked independently. No P expressly allocated to this identity-link model; do not compare row P with this CI. Repetitions agree where provided. 
- **Missing definitions / limits:** Difference-specific P/test/SE/variance/reference distribution absent. Model nonconvergence fallback expressly disclosed; do not infer equality with baseline-adjusted ratio.

## S035 — physician calls identity-link difference

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** 3.10 lies within −1.92–8.11 per1000 ward days and narrative matches. C028 recheck replaces alleged baseline-adjustment contradiction with undefined generic adjustment dimension; clustering can remain. C020 historical product does not recalculate trial effect. No new candidate.
- **Locations and document roles:** DOC-001 p7 Table 3 and footnote a REPORT; DOC-003 p1–3 PLAN; DOC-001 p8 REPORT repeat.
- **Printed inputs:** 3.10 (−1.92,8.11) per1000 corresponding denominator;95%CI.
- **Model, test and inferential definitions:** Poisson identity GEE; unadjusted baseline; hospital clustering; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; interval crosses zero; scale per1000 events or discharges as labeled. Separate fitted ratio S017 tracked independently. No P expressly allocated to this identity-link model; do not compare row P with this CI. Repetitions agree where provided. 
- **Missing definitions / limits:** Difference-specific P/test/SE/variance/reference distribution absent. Model nonconvergence fallback expressly disclosed; do not infer equality with baseline-adjusted ratio. Independent ST-H comparison: p8 calls this same difference adjusted, while Table 3 footnote a says physician-call difference was not adjusted for baseline.

## S036 — urgent ICU consultations identity-link difference

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** .16 lies within −.57–.89 per1000 ward days; main repetition matches. Consultation endpoint differs from ICU admission and ICU resource durations; none supplies a denominator substitution. No new candidate.
- **Locations and document roles:** DOC-001 p7 Table 3 and footnote a REPORT; DOC-003 p1–3 PLAN; DOC-001 p8 REPORT repeat.
- **Printed inputs:** .16 (−.57,.89) per1000 corresponding denominator;95%CI.
- **Model, test and inferential definitions:** Poisson identity GEE; adjusted; hospital clustering; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; interval crosses zero; scale per1000 events or discharges as labeled. Separate fitted ratio S018 tracked independently. No P expressly allocated to this identity-link model; do not compare row P with this CI. Repetitions agree where provided. 
- **Missing definitions / limits:** Difference-specific P/test/SE/variance/reference distribution absent. Model nonconvergence fallback expressly disclosed; do not infer equality with baseline-adjusted ratio.

## S037 — urgent ICU admission identity-link difference

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** −.18 lies within −.67–.30 per1000 ward days. Urgent-admission event counts and unique ICU patients are different quantities; C010 historical-cohort alignment is unsupported and does not establish final-trial rate inconsistency. No new candidate.
- **Locations and document roles:** DOC-001 p7 Table 3 and footnote a REPORT; DOC-003 p1–3 PLAN; .
- **Printed inputs:** −.18 (−.67,.30) per1000 corresponding denominator;95%CI.
- **Model, test and inferential definitions:** Poisson identity GEE; adjusted; hospital clustering; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; interval crosses zero; scale per1000 events or discharges as labeled. Separate fitted ratio S019 tracked independently. No P expressly allocated to this identity-link model; do not compare row P with this CI. Repetitions agree where provided. 
- **Missing definitions / limits:** Difference-specific P/test/SE/variance/reference distribution absent. Model nonconvergence fallback expressly disclosed; do not infer equality with baseline-adjusted ratio.

## S038 — ICU readmission identity-link difference

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** 4.95 lies within −1.62–11.52 per1000 ICU discharges. C014 denominator and C016 corrected P_R-only model comparisons survive. New P2-A endpoint window label also affects interpretation of this same readmission difference; no difference-specific P or changed numerator inferred.
- **Locations and document roles:** DOC-001 p7 Table 3 and footnote a REPORT; DOC-003 p1–3 PLAN; .
- **Printed inputs:** 4.95 (−1.62,11.52) per1000 corresponding denominator;95%CI.
- **Model, test and inferential definitions:** binomial identity GEE; adjusted; hospital clustering; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; interval crosses zero; scale per1000 events or discharges as labeled. Separate fitted ratio S020 tracked independently. No P expressly allocated to this identity-link model; do not compare row P with this CI. Repetitions agree where provided. 
- **Missing definitions / limits:** Difference-specific P/test/SE/variance/reference distribution absent. Model nonconvergence fallback expressly disclosed; do not infer equality with baseline-adjusted ratio.

## S039 — hospital readmission identity-link difference

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** −.71 lies within −4.92–3.49 per1000 hospital discharges; baseline-unadjusted identity model separate from logistic S021. New P2-B endpoint window label affects interpretation of this same difference, separately from C017 family label; no forced CI/P equivalence or changed numerator inferred.
- **Locations and document roles:** DOC-001 p7 Table 3 and footnote a REPORT; DOC-003 p1–3 PLAN; .
- **Printed inputs:** −.71 (−4.92,3.49) per1000 corresponding denominator;95%CI.
- **Model, test and inferential definitions:** binomial identity GEE; unadjusted baseline; hospital clustering; BP versus UC.
- **Checks and outcome:** Contained; endpoints ordered; interval crosses zero; scale per1000 events or discharges as labeled. Separate fitted ratio S021 tracked independently. No P expressly allocated to this identity-link model; do not compare row P with this CI. Repetitions agree where provided. 
- **Missing definitions / limits:** Difference-specific P/test/SE/variance/reference distribution absent. Model nonconvergence fallback expressly disclosed; do not infer equality with baseline-adjusted ratio.

## S040 — Historical Bedside-PEWS All

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .87 lies within .85–.89;1388 controls+686 cases=2074. Case median8 exceeds2 and both fall within ordered IQRs. C026 concerns a different historical abbreviated range; not this table. P test unspecified; no new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H01.
- **Printed inputs:** AUC .87 (.85,.89),95%CI; printed P<.0001; control n/median(IQR) 1388;2(1,4); case 686;8(5,12).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S041 — Historical Bedside-PEWS Urgent ICU

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .92 lies within .90–.94;772 controls+381 cases=1153 urgent-ICU category. ICU and code-blue strata sum to total controls/cases with S042. Median10 versus2 and IQRs ordered; no new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H02.
- **Printed inputs:** AUC .92 (.90,.94),95%CI; printed P<.0001; control n/median(IQR) 772;2(1,4); case 381;10(7,13).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S042 — Historical Bedside-PEWS Code Blue

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .81 lies within .78–.84;616 controls+305 cases=921 code-blue category. 772+616=1388 and381+305=686 reconcile category counts. Median6 versus2/IQRs agree; no new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H03.
- **Printed inputs:** AUC .81 (.78,.84),95%CI; printed P<.0001; control n/median(IQR) 616;2(1,4); case 305;6(3,10).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S043 — Historical Bedside-PEWS Age <3 months

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .83 lies within .79–.86;333/190 count pair belongs age<3months, not an ICU denominator. Medians2/7 contained in IQRs. Five age strata total1388/686; no new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H04.
- **Printed inputs:** AUC .83 (.79,.86),95%CI; printed P<.0001; control n/median(IQR) 333;2(1,4); case 190;7(4,10).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S044 — Historical Bedside-PEWS Age 3–<12 months

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .86 lies within .82–.90;362/164 age3–<12months counts enter age totals without overlap under displayed labels. Medians2/8 contained in IQRs. No new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H05.
- **Printed inputs:** AUC .86 (.82,.90),95%CI; printed P<.0001; control n/median(IQR) 362;2(1,4); case 164;8(6,11).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S045 — Historical Bedside-PEWS Age 1–<5 years

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .90 lies within .87–.93;286/134 age1–<5years counts and medians2/9 are coherent. C026 abbreviated endpoint does not alter this explicit range; no new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H06.
- **Printed inputs:** AUC .90 (.87,.93),95%CI; printed P<.0001; control n/median(IQR) 286;2(1,4); case 134;9(5,13).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S046 — Historical Bedside-PEWS Age5–12 years

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .89 lies within .84–.93;221/110 age5–12years counts and medians2/10 fall within their IQRs. Repeated nearby AUCs are different subgroup results with different intervals, not proven duplication. No new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H07.
- **Printed inputs:** AUC .89 (.84,.93),95%CI; printed P<.0001; control n/median(IQR) 221;2(1,3); case 110;10(5,13).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S047 — Historical Bedside-PEWS Age >12 years

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .91 lies within .87–.95;186/88 age>12years counts complete five age strata. Medians3/11 and IQRs ordered. Same rounded AUC/CI as hospital3 is possible without identical samples. No new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H08.
- **Printed inputs:** AUC .91 (.87,.95),95%CI; printed P<.0001; control n/median(IQR) 186;3(2,4); case 88;11(6,14).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S048 — Historical Bedside-PEWS Hospital1

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .88 lies within .85–.90;658/324 hospital1 counts and medians2/9 coherent. Four hospital groups sum1388/686; no trial21-hospital denominator imposed on historical validation. No new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H09.
- **Printed inputs:** AUC .88 (.85,.90),95%CI; printed P<.0001; control n/median(IQR) 658;2(1,4); case 324;9(6,12).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S049 — Historical Bedside-PEWS Hospital2

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .89 lies within .86–.92;478/238 hospital2 counts and medians1/6 coherent. Equal rounded AUC to other hospitals does not demonstrate reused output. No new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H10.
- **Printed inputs:** AUC .89 (.86,.92),95%CI; printed P<.0001; control n/median(IQR) 478;1(1,3); case 238;6(4,9).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S050 — Historical Bedside-PEWS Hospital3

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .91 lies within .87–.95;164/80 hospital3 counts and medians5/12 contained in ordered IQRs. Duplicate rounded AUC/CI with age>12 does not establish duplication; no new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H11.
- **Printed inputs:** AUC .91 (.87,.95),95%CI; printed P<.0001; control n/median(IQR) 164;5(2,6); case 80;12(9,15.5).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S051 — Historical Bedside-PEWS Hospital4

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .89 lies within .83–.96;88/44 hospital4 counts complete four-hospital totals. Medians2/9/IQRs coherent; larger CI versus another .89 point estimate is expected to remain distinct, not a numeric conflict. No new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H12.
- **Printed inputs:** AUC .89 (.83,.96),95%CI; printed P<.0001; control n/median(IQR) 88;2(1,3); case 44;9(4,12).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S052 — Historical Bedside-PEWS Transplant

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .94 lies within .90–.98;73/58 transplant counts are subgroup membership, not exhaustive categories. Medians2/11 coherent. Chronic disease groups may overlap; no forced subgroup sum. No new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H13.
- **Printed inputs:** AUC .94 (.90,.98),95%CI; printed P<.0001; control n/median(IQR) 73;2(1,3); case 58;11(7,12).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S053 — Historical Bedside-PEWS Heart disease

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .84 lies within .81–.88;386/233 heart-disease counts and medians3/8 coherent. Historical subgroup denominator cannot substitute for trial ICU patients. No new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H14.
- **Printed inputs:** AUC .84 (.81,.88),95%CI; printed P<.0001; control n/median(IQR) 386;3(2,5); case 233;8(6,11).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S054 — Historical Bedside-PEWS Severe cerebral palsy

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .92 lies within .86–.98;34/62 cerebral-palsy counts and medians2/10 coherent. Case subgroup larger than controls is possible; no mandatory fixed case/control ratio supplied. No new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H15.
- **Printed inputs:** AUC .92 (.86,.98),95%CI; printed P<.0001; control n/median(IQR) 34;2(1,4); case 62;10(7,13).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S055 — Historical Bedside-PEWS Tracheostomy

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .76 lies within .67–.86;36/57 tracheostomy counts and medians4/7 contained in ordered IQRs. Device categories are not exclusive/exhaustive; no subgroup-sum assertion. No new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H16.
- **Printed inputs:** AUC .76 (.67,.86),95%CI; printed P<.0001; control n/median(IQR) 36;4(1.5,5.5); case 57;7(4,11).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S056 — Historical Bedside-PEWS Feeding tube

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .86 lies within .82–.91;112/138 feeding-tube counts and medians3/10 coherent. Different interval from age3–<12 despite same rounded AUC retained. No new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H17.
- **Printed inputs:** AUC .86 (.82,.91),95%CI; printed P<.0001; control n/median(IQR) 112;3(1,5); case 138;10(6,13).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S057 — Historical Bedside-PEWS Home oxygen

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .79 lies within .69–.90;27/47 home-oxygen counts and medians5/8 coherent. P<.0001 is not attributed to AUC null without source definition. No new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H18.
- **Printed inputs:** AUC .79 (.69,.90),95%CI; printed P<.0001; control n/median(IQR) 27;5(2,7); case 47;8(6,11).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S058 — Historical Bedside-PEWS Seizures >15min

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .74 lies within .48–.99;6/47 seizure counts and medians2/6 coherent. P=.1146 and an interval including .5 raise no source-grounded contradiction; test mapping unspecified. No new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H19.
- **Printed inputs:** AUC .74 (.48,.99),95%CI; printed P.1146; control n/median(IQR) 6;2(2,4); case 47;6(3,10).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S059 — Historical Bedside-PEWS >3services

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .87 lies within .83–.91;136/164 >3-services counts and medians3/9 coherent. Complexity subgroup overlaps other groups; no forced total. No new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H20.
- **Printed inputs:** AUC .87 (.83,.91),95%CI; printed P<.0001; control n/median(IQR) 136;3(1,5); case 164;9(6,12).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S060 — Historical Bedside-PEWS >10medications/day

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .85 lies within .81–.90;109/162 >10-medications/day counts and medians3/10 coherent. No ledger fact changes these historical PLAN inputs; no new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H21.
- **Printed inputs:** AUC .85 (.81,.90),95%CI; printed P<.0001; control n/median(IQR) 109;3(1,5); case 162;10(6,13).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S061 — Historical Bedside-PEWS Recent service transfer

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** AUC .89 lies within .75–1.00;upper endpoint1.00 respects probability bounds. 5/18 transfer counts and medians1/7 coherent. P=.0040 is finite and its test undefined, not a display zero; no new candidate.
- **Locations and document roles:** DOC-002 p20 Table 2 PLAN; SUP-H22.
- **Printed inputs:** AUC .89 (.75,1.00),95%CI; printed P.0040; control n/median(IQR) 5;1(0,2); case 18;7(3,8).
- **Model, test and inferential definitions:** Historical 2074-patient four-hospital case/control validation; AUC discrimination; adjacent P column not defined as AUC test.
- **Checks and outcome:** AUC contained; endpoints ordered within0–1; case median exceeds control; every median contained within IQR and IQR endpoints ordered. No independent mismatch. P is not mechanically linked to AUC CI; do not infer AUC null or score-test method. 
- **Missing definitions / limits:** P test, sidedness, AUC variance/CI construction, tie method and score distribution absent. Counts/IQR cannot reconstruct P. Historical PLAN role retained.

## S062 — Historical adult outreach mortality

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Historical OR .52 lies within .32–.85 and reduction narrative agrees;16wards in one800-bed hospital over32weeks define a different cluster structure from EPOCH. No estimator or trial denominator transferred; no new candidate.
- **Locations and document roles:** DOC-002 p3 PLAN;SUP-H23.
- **Printed inputs:** .52 OR (.32,.85),95%;16wards/800-bed hospital/32weeks.
- **Model, test and inferential definitions:** Historical cluster study; model details not supplied.
- **Checks and outcome:** Contained; ordered; positive OR below1; reduced-mortality wording coherent. 
- **Missing definitions / limits:** P absent; exact covariance/cluster estimator/test/model absent.

## S063 — Lower-baseline mortality power

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Historical lower-baseline power scenario .199×3.2=.6368/1000 is diagnostic only. Distinguish it from S026 mortality scenario and C007 printed .9% discrepancy; no separately printed ARR for this scenario contradicts the product. No new candidate.
- **Locations and document roles:** DOC-002 p29 PLAN;SUP-P02.
- **Printed inputs:** RRR.199 at3.2/1000;20hospitals;119.85beds;LOS4;occupancy.90;k.15;α.05,z1.96,power.8.
- **Model, test and inferential definitions:** Logistic analysis named; cluster sample-size method cited.
- **Checks and outcome:** Implied ARR .6368/1000, not separately printed; positivity/reduction scales coherent. No source formula allows exact power calculation. 
- **Missing definitions / limits:** Power formula/cluster-size time basis/variance absent; derived ARR diagnostic only.

## S064 — SCDE power

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** SCDE baseline2/1000×RRR.31=.62/1000 reconciles. C010 recheck does not establish identity of annual and two-year1052 cohorts; C018/C019 retain conditional historical fraction/rounding questions without reconstructing power. No new candidate.
- **Locations and document roles:** DOC-002 p14–15,p30 PLAN;SUP-P03.
- **Printed inputs:** baseline2/1000 patient-days; RRR31%;ARR.62/1000;20sites,k.15,α.05two-sided,power.8;40%of1052SCDE assumptions.
- **Model, test and inferential definitions:** Cluster count/power method; baseline rate.
- **Checks and outcome:** 2×.31=.62 per1000; reduction and units agree. Protocol p14 annual1052 versus p30 two-year counts deferred numeric lane; no inferred power test. 
- **Missing definitions / limits:** No exact cluster formula; 40% approximate; annual/two-year historical basis must not be silently aligned.

## S065 — Code-blue power and absolute-reduction units

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** C021 nested unit cue reproduced: .75×.41=.3075≈.3 events/1000days; extra /1000 is a literal dimensional ambiguity, not proof the power engine used another divisor. Preserve named intended-unit question; no new candidate.
- **Locations and document roles:** DOC-002 p30 section3 PLAN;SUP-P04.
- **Printed inputs:** baseline.75/1000 patient-days;RRR.41; ARR '0.3/1000 events per thousand patient days';20sites,z1.96,α.05,power.8,k.15,119.85beds,LOS4.
- **Model, test and inferential definitions:** Cluster count analysis power; relative-to-absolute reduction identity.
- **Checks and outcome:** .75×.41=.3075 events/1000days≈.3 events/1000days. Literal printed double denominator gives .0003 events/1000days: ST-C unit ambiguity. Exact power not reconstructed. 
- **Missing definitions / limits:** Need intended denominator wording; no formula for power.

## S066 — Stat-call power and absolute reduction

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** C020 reproduced:8.13×.181=1.47153/1000, with nearest-input product bounds1.4665625–1.4765025 disjoint from displayed1.45 bounds. No unprinted power scenario inferred. No new candidate beyond registered product mismatch.
- **Locations and document roles:** DOC-002 p30 section4 PLAN;SUP-P05.
- **Printed inputs:** baseline8.13/1000 patient-days;RRR.181;printedARR1.45/1000days;20sites,z1.96,α.05,power.8,k.15,119.85beds,LOS4.
- **Model, test and inferential definitions:** Poisson analysis; cluster count power; ARR=baseline×RRR.
- **Checks and outcome:** 8.13×.181=1.47153/1000days versus1.45; nearest displayed-input rounding range1.4665625–1.4765025 excludes printed1.445–1.455: ST-B arithmetic candidate. 
- **Missing definitions / limits:** Actual unrounded power output and any distinct analytic conversion absent; exact power not reconstructed.

## S067 — Urgent-ICU PIM score

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** .13 lies within −.11–.37 on PIM logit-score scale; P=.29 qualitatively nonsignificant. C023 inverse-logit upper example does not convert this score difference into a probability difference. Patient393/686/531/967 population retained; no new candidate.
- **Locations and document roles:** DOC-004 p12 row and p13 footnotes REPORT;DOC-003 p7 PLAN;SUP-E03.
- **Printed inputs:** .13 (−.11,.37),95%CI;P=.29;n baseline/post BP393/686,UC531/967.
- **Model, test and inferential definitions:** Gaussian identity;PIM logit score;baseline-adjusted GEE hospital clusters;one record/patient after removing55cross-period patients.
- **Checks and outcome:** Contained; endpoints ordered; difference scale/units coherent; interval crosses zero and nonsignificant P direction agree. Raw arm means/percentages are not baseline-adjusted differences. Adjacent identical rounded P values have no supplied deterministic uniqueness rule; no duplicate candidate. 
- **Missing definitions / limits:** Exact covariance estimator/SE/reference distribution/small-sample correction absent; no exact CI/P compatibility assertion. Individual observations unavailable.

## S068 — Urgent-ICU ICU total length of stay

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** 1.28 lies within −.97–3.53 days; total stay is sum across a patient's admissions. C013 retains blanket ICU-day label question but eTable patient-day duration difference is explicitly coherent. No crude mean subtraction forced; no new candidate.
- **Locations and document roles:** DOC-004 p12 row and p13 footnotes REPORT;DOC-003 p7 PLAN;SUP-E04.
- **Printed inputs:** 1.28 (−.97,3.53),95%CI;P=.27;n baseline/post BP393/686,UC531/967.
- **Model, test and inferential definitions:** Gaussian identity;sum days across admissions;baseline-adjusted GEE hospital clusters;one record/patient after removing55cross-period patients.
- **Checks and outcome:** Contained; endpoints ordered; difference scale/units coherent; interval crosses zero and nonsignificant P direction agree. Raw arm means/percentages are not baseline-adjusted differences. Adjacent identical rounded P values have no supplied deterministic uniqueness rule; no duplicate candidate. 
- **Missing definitions / limits:** Exact covariance estimator/SE/reference distribution/small-sample correction absent; no exact CI/P compatibility assertion. Individual observations unavailable.

## S069 — Urgent-ICU ICU mean length of stay

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** 1.04 lies within −.91–2.99 days; mean stay across admissions differs from total stay S068. Equal rounded P=.29 to PIM score is not duplicate evidence. C013 unit-scope question retained; no new candidate.
- **Locations and document roles:** DOC-004 p12 row and p13 footnotes REPORT;DOC-003 p7 PLAN;SUP-E05.
- **Printed inputs:** 1.04 (−.91,2.99),95%CI;P=.29;n baseline/post BP393/686,UC531/967.
- **Model, test and inferential definitions:** Gaussian identity;mean days across admissions;baseline-adjusted GEE hospital clusters;one record/patient after removing55cross-period patients.
- **Checks and outcome:** Contained; endpoints ordered; difference scale/units coherent; interval crosses zero and nonsignificant P direction agree. Raw arm means/percentages are not baseline-adjusted differences. Adjacent identical rounded P values have no supplied deterministic uniqueness rule; no duplicate candidate. 
- **Missing definitions / limits:** Exact covariance estimator/SE/reference distribution/small-sample correction absent; no exact CI/P compatibility assertion. Individual observations unavailable.

## S070 — Urgent-ICU Ventilator-free days

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** .26 lies within −1.04–1.57 ventilator-free days;28-day first-admission window distinguishes it from all-admission technology duration. C013 does not turn days per patient into event rates. No new candidate.
- **Locations and document roles:** DOC-004 p12 row and p13 footnotes REPORT;DOC-003 p7 PLAN;SUP-E06.
- **Printed inputs:** .26 (−1.04,1.57),95%CI;P=.69;n baseline/post BP393/686,UC531/967.
- **Model, test and inferential definitions:** Gaussian identity;first admission/28day window;baseline-adjusted GEE hospital clusters;one record/patient after removing55cross-period patients.
- **Checks and outcome:** Contained; endpoints ordered; difference scale/units coherent; interval crosses zero and nonsignificant P direction agree. Raw arm means/percentages are not baseline-adjusted differences. Adjacent identical rounded P values have no supplied deterministic uniqueness rule; no duplicate candidate. 
- **Missing definitions / limits:** Exact covariance estimator/SE/reference distribution/small-sample correction absent; no exact CI/P compatibility assertion. Individual observations unavailable.

## S071 — Urgent-ICU Mechanical ventilation days

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** .69 lies within −.99–2.36 mechanical-ventilation days. Same rounded .69 point as predicted mortality S025 is on different units/intervals, not a copied result identity. C013 duration-unit question retained; no new candidate.
- **Locations and document roles:** DOC-004 p12 row and p13 footnotes REPORT;DOC-003 p7 PLAN;SUP-E07.
- **Printed inputs:** .69 (−.99,2.36),95%CI;P=.42;n baseline/post BP393/686,UC531/967.
- **Model, test and inferential definitions:** Gaussian identity;per-patient days;baseline-adjusted GEE hospital clusters;one record/patient after removing55cross-period patients.
- **Checks and outcome:** Contained; endpoints ordered; difference scale/units coherent; interval crosses zero and nonsignificant P direction agree. Raw arm means/percentages are not baseline-adjusted differences. Adjacent identical rounded P values have no supplied deterministic uniqueness rule; no duplicate candidate. 
- **Missing definitions / limits:** Exact covariance estimator/SE/reference distribution/small-sample correction absent; no exact CI/P compatibility assertion. Individual observations unavailable.

## S072 — Urgent-ICU Mechanical ventilation use

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** −.93 lies within −7.46–5.61 percentage points for any mechanical ventilation, distinct from days S071. Patient denominators retained; no interpretation as −.93% relative change or rate ratio. No new candidate.
- **Locations and document roles:** DOC-004 p12 row and p13 footnotes REPORT;DOC-003 p7 PLAN;SUP-E08.
- **Printed inputs:** −.93 (−7.46,5.61),95%CI;P=.78;n baseline/post BP393/686,UC531/967.
- **Model, test and inferential definitions:** Binomial identity;any use percentage-point RD;baseline-adjusted GEE hospital clusters;one record/patient after removing55cross-period patients.
- **Checks and outcome:** Contained; endpoints ordered; difference scale/units coherent; interval crosses zero and nonsignificant P direction agree. Raw arm means/percentages are not baseline-adjusted differences. Adjacent identical rounded P values have no supplied deterministic uniqueness rule; no duplicate candidate. 
- **Missing definitions / limits:** Exact covariance estimator/SE/reference distribution/small-sample correction absent; no exact CI/P compatibility assertion. Individual observations unavailable.

## S073 — Urgent-ICU HFOV use

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** −1.17 lies within −2.52–.19 percentage points for HFOV;P=.09 qualitatively agrees with zero crossing. No exact normal or small-sample P derived absent estimator; no new candidate.
- **Locations and document roles:** DOC-004 p12 row and p13 footnotes REPORT;DOC-003 p7 PLAN;SUP-E09.
- **Printed inputs:** −1.17 (−2.52,.19),95%CI;P=.09;n baseline/post BP393/686,UC531/967.
- **Model, test and inferential definitions:** Binomial identity;any use percentage-point RD;baseline-adjusted GEE hospital clusters;one record/patient after removing55cross-period patients.
- **Checks and outcome:** Contained; endpoints ordered; difference scale/units coherent; interval crosses zero and nonsignificant P direction agree. Raw arm means/percentages are not baseline-adjusted differences. Adjacent identical rounded P values have no supplied deterministic uniqueness rule; no duplicate candidate. 
- **Missing definitions / limits:** Exact covariance estimator/SE/reference distribution/small-sample correction absent; no exact CI/P compatibility assertion. Individual observations unavailable.

## S074 — Urgent-ICU Nitric oxide use

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** −.38 lies within −1.91–1.15 percentage points for nitric oxide;P=.63 and direction coherent. Unique patient-use denominator distinct from treatment-day durations; no new candidate.
- **Locations and document roles:** DOC-004 p12 row and p13 footnotes REPORT;DOC-003 p7 PLAN;SUP-E10.
- **Printed inputs:** −.38 (−1.91,1.15),95%CI;P=.63;n baseline/post BP393/686,UC531/967.
- **Model, test and inferential definitions:** Binomial identity;any use percentage-point RD;baseline-adjusted GEE hospital clusters;one record/patient after removing55cross-period patients.
- **Checks and outcome:** Contained; endpoints ordered; difference scale/units coherent; interval crosses zero and nonsignificant P direction agree. Raw arm means/percentages are not baseline-adjusted differences. Adjacent identical rounded P values have no supplied deterministic uniqueness rule; no duplicate candidate. 
- **Missing definitions / limits:** Exact covariance estimator/SE/reference distribution/small-sample correction absent; no exact CI/P compatibility assertion. Individual observations unavailable.

## S075 — Urgent-ICU ECMO use

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** −1.03 lies within −2.45–.38 percentage points for ECMO;P=.15 and zero crossing coherent. Eligibility of hospitals with ECMO does not change this reported patient-level use denominator by convention. No new candidate.
- **Locations and document roles:** DOC-004 p12 row and p13 footnotes REPORT;DOC-003 p7 PLAN;SUP-E11.
- **Printed inputs:** −1.03 (−2.45,.38),95%CI;P=.15;n baseline/post BP393/686,UC531/967.
- **Model, test and inferential definitions:** Binomial identity;any use percentage-point RD;baseline-adjusted GEE hospital clusters;one record/patient after removing55cross-period patients.
- **Checks and outcome:** Contained; endpoints ordered; difference scale/units coherent; interval crosses zero and nonsignificant P direction agree. Raw arm means/percentages are not baseline-adjusted differences. Adjacent identical rounded P values have no supplied deterministic uniqueness rule; no duplicate candidate. 
- **Missing definitions / limits:** Exact covariance estimator/SE/reference distribution/small-sample correction absent; no exact CI/P compatibility assertion. Individual observations unavailable.

## S076 — Urgent-ICU Dialysis use

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** .96 lies within −1.25–3.17 percentage points for dialysis;P=.40 coherent qualitatively. Overlap among therapies prevents forced sum-to100; no new candidate.
- **Locations and document roles:** DOC-004 p12 row and p13 footnotes REPORT;DOC-003 p7 PLAN;SUP-E12.
- **Printed inputs:** .96 (−1.25,3.17),95%CI;P=.40;n baseline/post BP393/686,UC531/967.
- **Model, test and inferential definitions:** Binomial identity;any use percentage-point RD;baseline-adjusted GEE hospital clusters;one record/patient after removing55cross-period patients.
- **Checks and outcome:** Contained; endpoints ordered; difference scale/units coherent; interval crosses zero and nonsignificant P direction agree. Raw arm means/percentages are not baseline-adjusted differences. Adjacent identical rounded P values have no supplied deterministic uniqueness rule; no duplicate candidate. 
- **Missing definitions / limits:** Exact covariance estimator/SE/reference distribution/small-sample correction absent; no exact CI/P compatibility assertion. Individual observations unavailable.

## S077 — Urgent-ICU ICU technology days

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** 1.13 lies within −.99–3.25 total technology days per patient. Technology days may overlap, so mechanical-ventilation days do not exhaust the total. C013 scope ambiguity retained; no new candidate.
- **Locations and document roles:** DOC-004 p12 row and p13 footnotes REPORT;DOC-003 p7 PLAN;SUP-E13.
- **Printed inputs:** 1.13 (−.99,3.25),95%CI;P=.30;n baseline/post BP393/686,UC531/967.
- **Model, test and inferential definitions:** Gaussian identity;sum technology days across admissions;baseline-adjusted GEE hospital clusters;one record/patient after removing55cross-period patients.
- **Checks and outcome:** Contained; endpoints ordered; difference scale/units coherent; interval crosses zero and nonsignificant P direction agree. Raw arm means/percentages are not baseline-adjusted differences. Adjacent identical rounded P values have no supplied deterministic uniqueness rule; no duplicate candidate. 
- **Missing definitions / limits:** Exact covariance estimator/SE/reference distribution/small-sample correction absent; no exact CI/P compatibility assertion. Individual observations unavailable.

## S078 — Urgent-ICU PELOD entire ICU

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** −.12 lies within −1.62–1.37 PELOD score units; entire-ICU mean differs from first24h S079. P=.87 and direction coherent; no extra patient-time denominator or duplicate constraint. No new candidate.
- **Locations and document roles:** DOC-004 p12 row and p13 footnotes REPORT;DOC-003 p7 PLAN;SUP-E14.
- **Printed inputs:** −.12 (−1.62,1.37),95%CI;P=.87;n baseline/post BP393/686,UC531/967.
- **Model, test and inferential definitions:** Gaussian identity;per-patient mean score;baseline-adjusted GEE hospital clusters;one record/patient after removing55cross-period patients.
- **Checks and outcome:** Contained; endpoints ordered; difference scale/units coherent; interval crosses zero and nonsignificant P direction agree. Raw arm means/percentages are not baseline-adjusted differences. Adjacent identical rounded P values have no supplied deterministic uniqueness rule; no duplicate candidate. 
- **Missing definitions / limits:** Exact covariance estimator/SE/reference distribution/small-sample correction absent; no exact CI/P compatibility assertion. Individual observations unavailable.

## S079 — Urgent-ICU PELOD first24h

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** −.29 lies within −1.06–.49 PELOD score units;P=.47 and zero crossing coherent. First24h and entire-stay populations/aggregation remain distinguished. C015 is PIM prediction labeling, not PELOD; no new candidate.
- **Locations and document roles:** DOC-004 p12 row and p13 footnotes REPORT;DOC-003 p7 PLAN;SUP-E15.
- **Printed inputs:** −.29 (−1.06,.49),95%CI;P=.47;n baseline/post BP393/686,UC531/967.
- **Model, test and inferential definitions:** Gaussian identity;per-patient mean score;baseline-adjusted GEE hospital clusters;one record/patient after removing55cross-period patients.
- **Checks and outcome:** Contained; endpoints ordered; difference scale/units coherent; interval crosses zero and nonsignificant P direction agree. Raw arm means/percentages are not baseline-adjusted differences. Adjacent identical rounded P values have no supplied deterministic uniqueness rule; no duplicate candidate. 
- **Missing definitions / limits:** Exact covariance estimator/SE/reference distribution/small-sample correction absent; no exact CI/P compatibility assertion. Individual observations unavailable.

## S080 — Bayesian intercluster coefficient

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Bayesian k=.43 lies within .17–.77. C006 recheck supports constant-size anticipated beds versus observed participating-site count. Rounded SD/mortality plug-in ratio does not identify posterior Bayesian k without supplied prior/likelihood/mapping. Absolute SD decline and relative CV rise can coexist; no new candidate.
- **Locations and document roles:** DOC-004 p14 eTable 5 REPORT;SUP-E16.
- **Printed inputs:** k=.43 (.17,.77),95%;anticipated.15;SD anticipated.00076/actual.00071;deathrate5.1/1.7 per1000.
- **Model, test and inferential definitions:** Bayesian recalculation of CV; prior/likelihood/interval type unspecified.
- **Checks and outcome:** Contained; ordered; positive CV; interval scale coherent. Posterior CV need not equal ratio of rounded SD to rounded mortality; no plug-in identity asserted. Main p8 discussion refers absolute variability, not necessarily identical CV. 
- **Missing definitions / limits:** Prior, posterior calculation, credible-versus-confidence interval convention and mapping of printed SD to Bayesian estimate absent.

## S081 — Historical comparative score Bristol

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Bristol AUC.52, sensitivity99%,specificity63% are within bounds; >1 trigger uses its own criteria. Comparative2074-person cohort is explicitly distinct from development evidence. No matched-statistic contradiction; no new candidate.
- **Locations and document roles:** DOC-002 p19 Table 1/caption PLAN.
- **Printed inputs:** AUC.52;Sens99%,Spec63%;>1criterion.
- **Model, test and inferential definitions:** 10triggers+3diagnostic triggers+concern;objective score components evaluated on2074patients/fourhospitals.
- **Checks and outcome:** AUC where present is within0–1; sensitivity/specificity within0–100%; direction/threshold labels transcribed. No CI/P. Different evaluation cohort and operationalized criteria expressly described; do not equate these AUCs to original-development narrative values. 
- **Missing definitions / limits:** No uncertainty, denominator cell table, model or inferential test supplied; NA remains NA. Exact > versus narrative threshold score differs across evaluations; no unsupported threshold alignment.

## S082 — Historical comparative score Brighton

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Brighton AUC.53, sensitivity71%,specificity91% coherent on their scales;score>5 is a comparative operational threshold. Different cohort from S089 prevents forced identity with .89/78/82. No new candidate.
- **Locations and document roles:** DOC-002 p19 Table 1/caption PLAN.
- **Printed inputs:** AUC.53;Sens71%,Spec91%;score>5.
- **Model, test and inferential definitions:** score0–11,7items;objective score components evaluated on2074patients/fourhospitals.
- **Checks and outcome:** AUC where present is within0–1; sensitivity/specificity within0–100%; direction/threshold labels transcribed. No CI/P. Different evaluation cohort and operationalized criteria expressly described; do not equate these AUCs to original-development narrative values. 
- **Missing definitions / limits:** No uncertainty, denominator cell table, model or inferential test supplied; NA remains NA. Exact > versus narrative threshold score differs across evaluations; no unsupported threshold alignment.

## S083 — Historical comparative score Toronto2006

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Toronto AUC.87,sensitivity78%,specificity95% coherent; sixteen-item score differs from seven-item BedsidePEWS. Equality of some development operating characteristics does not establish common AUC cohort. No new candidate.
- **Locations and document roles:** DOC-002 p19 Table 1/caption PLAN.
- **Printed inputs:** AUC.87;Sens78%,Spec95%;score>5.
- **Model, test and inferential definitions:** score0–26,9static/7dynamicitems;objective score components evaluated on2074patients/fourhospitals.
- **Checks and outcome:** AUC where present is within0–1; sensitivity/specificity within0–100%; direction/threshold labels transcribed. No CI/P. Different evaluation cohort and operationalized criteria expressly described; do not equate these AUCs to original-development narrative values. 
- **Missing definitions / limits:** No uncertainty, denominator cell table, model or inferential test supplied; NA remains NA. Exact > versus narrative threshold score differs across evaluations; no unsupported threshold alignment.

## S084 — Historical comparative score Melbourne

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Melbourne AUC.73 is bounded; sensitivity/specificity are absent, not zero. >1criterion is retained without a fabricated contingency table. No ledger recheck changes this historical PLAN row; no new candidate.
- **Locations and document roles:** DOC-002 p19 Table 1/caption PLAN.
- **Printed inputs:** AUC.73;sensitivity/specificitynotprovided;>1criterion.
- **Model, test and inferential definitions:** 8triggers+concern;objective score components evaluated on2074patients/fourhospitals.
- **Checks and outcome:** AUC where present is within0–1; sensitivity/specificity within0–100%; direction/threshold labels transcribed. No CI/P. Different evaluation cohort and operationalized criteria expressly described; do not equate these AUCs to original-development narrative values. 
- **Missing definitions / limits:** No uncertainty, denominator cell table, model or inferential test supplied; NA remains NA. Exact > versus narrative threshold score differs across evaluations; no unsupported threshold alignment.

## S085 — Historical comparative score Cincinnati

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Cincinnati AUC NA remains missing, not a probability estimate. Subjective triggers and >1criterion cannot supply an inferred sensitivity/test. No new candidate from missing precision.
- **Locations and document roles:** DOC-002 p19 Table 1/caption PLAN.
- **Printed inputs:** AUCNA;noSens/Spec;>1criterion.
- **Model, test and inferential definitions:** 4subjectivetriggers+staff/parentconcern;objective score components evaluated on2074patients/fourhospitals.
- **Checks and outcome:** AUC where present is within0–1; sensitivity/specificity within0–100%; direction/threshold labels transcribed. No CI/P. Different evaluation cohort and operationalized criteria expressly described; do not equate these AUCs to original-development narrative values. 
- **Missing definitions / limits:** No uncertainty, denominator cell table, model or inferential test supplied; NA remains NA. Exact > versus narrative threshold score differs across evaluations; no unsupported threshold alignment.

## S086 — Historical comparative score Baltimore

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Baltimore AUC NA remains missing; eight subjective items/two arrest types are criterion definitions, not event frequencies. No denominator or test manufactured; no new candidate.
- **Locations and document roles:** DOC-002 p19 Table 1/caption PLAN.
- **Printed inputs:** AUCNA;noSens/Spec;>1criterion.
- **Model, test and inferential definitions:** 8subjectiveitems+2arresttypes+concern;objective score components evaluated on2074patients/fourhospitals.
- **Checks and outcome:** AUC where present is within0–1; sensitivity/specificity within0–100%; direction/threshold labels transcribed. No CI/P. Different evaluation cohort and operationalized criteria expressly described; do not equate these AUCs to original-development narrative values. 
- **Missing definitions / limits:** No uncertainty, denominator cell table, model or inferential test supplied; NA remains NA. Exact > versus narrative threshold score differs across evaluations; no unsupported threshold alignment.

## S087 — Historical comparative score Cardiff

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Cardiff AUC.62/sensitivity70%/specificity90% coherent; suggestedscore>2 belongs comparative validation. S090's .86/69/90 has different development cohort; no exact threshold/case mix alignment. No new candidate.
- **Locations and document roles:** DOC-002 p19 Table 1/caption PLAN.
- **Printed inputs:** AUC.62;Sens70%,Spec90%;suggestedscore>2.
- **Model, test and inferential definitions:** score0–8,7items;objective score components evaluated on2074patients/fourhospitals.
- **Checks and outcome:** AUC where present is within0–1; sensitivity/specificity within0–100%; direction/threshold labels transcribed. No CI/P. Different evaluation cohort and operationalized criteria expressly described; do not equate these AUCs to original-development narrative values. 
- **Missing definitions / limits:** No uncertainty, denominator cell table, model or inferential test supplied; NA remains NA. Exact > versus narrative threshold score differs across evaluations; no unsupported threshold alignment.

## S088 — Historical comparative score BedsidePEWS

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** BedsidePEWS AUC.87/sensitivity82%/specificity93% coherent; score>8 comparative setting differs from single-center threshold8. Multicenter AUC repeats S040 coherently; no new candidate.
- **Locations and document roles:** DOC-002 p19 Table 1/caption PLAN.
- **Printed inputs:** AUC.87;Sens82%,Spec93%;score>8.
- **Model, test and inferential definitions:** score0–26,7items;objective score components evaluated on2074patients/fourhospitals.
- **Checks and outcome:** AUC where present is within0–1; sensitivity/specificity within0–100%; direction/threshold labels transcribed. No CI/P. Different evaluation cohort and operationalized criteria expressly described; do not equate these AUCs to original-development narrative values. 
- **Missing definitions / limits:** No uncertainty, denominator cell table, model or inferential test supplied; NA remains NA. Exact > versus narrative threshold score differs across evaluations; no unsupported threshold alignment.

## S089 — Historical Brighton development performance

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Brighton development AUC.89/sensitivity78%/specificity82% on valid scales;2979children/51transfers identify a separate cohort from Table1. Neither count nor later historical P supplies test covariance. No new candidate.
- **Locations and document roles:** DOC-002 p4 PLAN.
- **Printed inputs:** AUC.89;Sens78%,Spec82%;score5;2979children/51transfers.
- **Model, test and inferential definitions:** Cincinnati validation of Brighton score; cohort explicitly separate from comparativeTable1.
- **Checks and outcome:** AUC/proportions valid scales; threshold/direction coherent. .89 versus Table1.53 is not a matched-cohort repetition. 
- **Missing definitions / limits:** No CI,P,test or contingency table; no reconstructable uncertainty.

## S090 — Historical Cardiff development performance

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Cardiff development AUC.86/sensitivity69%/specificity90% coherent. Shared90% specificity with comparative row does not prove reused data; no CI/P or counts supplied to force equality. No new candidate.
- **Locations and document roles:** DOC-002 p4 PLAN.
- **Printed inputs:** AUC.86;Sens69%,Spec90%;threshold2.
- **Model, test and inferential definitions:** Development cohort;separate fromTable1 comparative2074patients.
- **Checks and outcome:** Scales within bounds; no containment applicable. Development specificity90% equals comparator90% without implying common cohort; no mismatch. 
- **Missing definitions / limits:** No CI/P,test or contingency table.

## S091 — Original16-item PEWS performance

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Original16-item AUC.91/sensitivity78%/specificity95% coherent; distinct score and development cohort separate it from seven-item analyses. Rounded repetitions across other score results do not establish duplication. No new candidate.
- **Locations and document roles:** DOC-002 p4 PLAN.
- **Printed inputs:** AUC.91;Sens78%,Spec95%;threshold5;16items.
- **Model, test and inferential definitions:** Original score development;distinct from7-item model.
- **Checks and outcome:** AUC/sensitivity/specificity scales coherent; no CI/P. TorontoTable1 evaluation.87 distinct cohort explicitly labeled. 
- **Missing definitions / limits:** No CI,P,test or contingency table.

## S092 — Seven-item single-center Bedside-PEWS performance

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Seven-item single-center AUC.91/sensitivity83%/specificity95% coherent. Summary82% identification and >80% overview lack exact sample/threshold/time alignment to83%; retain missing alignment, do not invent contradiction. No new candidate.
- **Locations and document roles:** DOC-002 p1,p2,p4 PLAN.
- **Printed inputs:** AUC.91;Sens83%,Spec95%;threshold8;≥1hournotice;summary82%identified,overview>80%.
- **Model, test and inferential definitions:** Frequency-matched case-control development;single-center validation.
- **Checks and outcome:** AUC/scales coherent; summary82%identified versus83%sensitivity not forced exact identity absent explicit matching threshold/sample. Multicenter.87 is separate S040. No candidate solely absent denominator matching. 
- **Missing definitions / limits:** Definition/sample/time alignment for82% summary versus83%threshold8 not supplied; no CI/test.

## S093 — Historical score reliability ICC

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** ICC .92 and .90 respect bounds; educator/new-staff and786 real-patient comparisons are distinct populations. One difference>2 is not an ICC estimator input sufficient for reconstruction; no new candidate.
- **Locations and document roles:** DOC-002 p1,p5,p8 PLAN.
- **Printed inputs:** ICC.92 in summary/educators-newstaff;786real-patientscorecomparisonsICC.90;one difference>2;120frontlinestaff in development.
- **Model, test and inferential definitions:** Inter-rater ICC populations different; operational validation.
- **Checks and outcome:** Values lie within ICC bounds; .92 repeats agree; .90 has distinct real-patient cohort. Count of discordances cannot reconstruct ICC. 
- **Missing definitions / limits:** ICC formulation,weights,SE/CI,rating variance matrix absent.

## S094 — Adult early-warning AUC range

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** C026 literal AUC0.83–86 scale ambiguity survives exact recheck; suffix86 may intend .86. Preserve shorthand alternative and source-unavailable endpoint question; no historical computation86 alleged. No new candidate.
- **Locations and document roles:** DOC-002 p6 systematic-review paragraph PLAN.
- **Printed inputs:** printed AUCROC0.83–86.
- **Model, test and inferential definitions:** Discrimination of ICU versus high-dependency patients; cited review not supplied.
- **Checks and outcome:** Literal endpoint86 exceeds AUC0–1 domain; ST-D scale candidate. Conventional shorthand could intend .86, which source does not spell out. 
- **Missing definitions / limits:** Underlying review unavailable; do not browse or prescribe exact corrected range.

## S095 — Protocol mortality logistic specification

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Mortality logit/OR versus identity probability difference distinctions remain explicit. Report disclosed dropping size stratum for three large hospitals; GEE/weights revisions lack a concrete inferential-number contradiction. Protocol says DNR analyses both with and without atp10, so p16 following-DNR list does not disprove reported nonDNR subset. No new candidate.
- **Locations and document roles:** DOC-002 p16 PLAN;DOC-003 p1–2 PLAN;DOC-001 p4–5,p7 REPORT.
- **Printed inputs:** Dependent hospital logit; treatment+baseline logit+size stratum;size weights;SAPbinomialGEE;REPORTOR anddifference models;stratum removed because3largehospitals.
- **Model, test and inferential definitions:** Protocol weighted hospital logit regression; SAP GEE grouped hospitals; report GEE exchangeable.
- **Checks and outcome:** OR/logit and binomial identity distinctions retained. REPORT expressly discloses removing size stratum. Evolution of fitting procedure without a demonstrated number/label contradiction is not a broad-methodology candidate. 
- **Missing definitions / limits:** No effect of weight/GEE revision on a reported number inferable; raw fit objects/variance estimator unavailable.

## S096 — Protocol count-rate specification

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Poisson event counts with ward-day exposure give named rate ratios and separately fitted differences. C011/C012 endpoint-definition questions and C022 symbolic exposure scale persist without model-output reconstruction. Baseline fallback prevents forced common-fit inference. No new candidate.
- **Locations and document roles:** DOC-002 p16 PLAN;DOC-003 p2–3 PLAN;DOC-001 p7 REPORT.
- **Printed inputs:** SCDE/codeblue/stat/urgentconsults /1000patientdays;Poissonhospitalaggregate;treatment,baseline,stratum;SAPlog/identity separated.
- **Model, test and inferential definitions:** Poisson count mean linked to exposure; report RR versus separate rate difference.
- **Checks and outcome:** Log-link ratio versus identity difference labels compatible; baseline fallback disclosed in report. Do not equate difference and ratio inference. 
- **Missing definitions / limits:** Exposure-specific covariance,finite-sample correction and actual code not supplied.

## S097 — Protocol continuous/observation specification

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Duration/score differences are means on source-defined patient aggregation, not ICU-day event rates. C013 retains blanket-unit scope ambiguity; C025 heading retains summary-versus-response taxonomy ambiguity. Model-unit changes alone imply no effect-size error. No new candidate.
- **Locations and document roles:** DOC-002 p16 PLAN;DOC-003 p4,p7 PLAN;DOC-001 p6/p8 REPORT;DOC-004 p12–13 REPORT.
- **Printed inputs:** Hospitalmean linear regression,size weights exceptdocumentation;PIM/PELOD/ventilatorfree/ICUdays/therapydays;SAPindividualGEE;REPORTmean differences.
- **Model, test and inferential definitions:** Protocol/SAP continuous families with hospitalbaseline; repeated observations aggregated perpatient.
- **Checks and outcome:** Mean-difference units coherent; stated hospital-level versus patient-level approaches are tracked without unreported numeric fit comparison. Other numeric/endpoint changes remain independently reviewable. 
- **Missing definitions / limits:** Actual model output/rawdata missing; no effect-size change deducible merely from unit choice.

## S098 — SAP binary two-model definitions and code

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Binomial logit odds versus identity probability differences supplied as separate fits. Baseline zero adjustments apply to predictor construction; no display-zero P occurs. C016/C017 concern specific shell rows, not an inconsistency in these two-model definitions. No new candidate.
- **Locations and document roles:** DOC-003 p1–2 PLAN;DOC-001 p7 REPORT.
- **Printed inputs:** Binomial logit OR versusidentity probability/RD;events x/discharges n;baselinezero add.5numerator and1denominator;formulacbind(x,n−x)~Intervention+baseline;exchangeable.
- **Model, test and inferential definitions:** Two separate models; individualbinary y alternative also supplied.
- **Checks and outcome:** Probability/proportion versus odds scales explicit; zero adjustment baseline only. No result-level contradiction or inference from tiny probabilities; no displayedzero P. 
- **Missing definitions / limits:** No unrounded estimates, actual fit/code provenance, covariance estimator.

## S099 — SAP log-rate illustrative code

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Illustrative unclosed offset expression lacks executable-output provenance; retain missing actual model code. C022 separate exact exposure scale comparison does not imply this malformed example generated reported estimates. No new candidate from code syntax alone.
- **Locations and document roles:** DOC-003 p2–3 PLAN lines82–112.
- **Printed inputs:** Text predictor intervention+baseline;offsetlog(patientdays);printedformula x~offset(log(N)+Intervention+logBaseline,... ).
- **Model, test and inferential definitions:** Intended Poisson log GEE; printed illustrative expression has predictors inside unclosed offset call.
- **Checks and outcome:** Checked parentheses and placement: literal expression is not executable as intended predictor formula; source supplies no model execution artifact linking it to a reported number. Record explanatory-code limitation rather than invent output or a method-only candidate. 
- **Missing definitions / limits:** Actual executed code unavailable; illustrative transcription cannot establish reported coefficient or P change.

## S100 — SAP identity-rate exposure/coefficient code

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** C022 reproduced symbolically: E[x]=Nα/1000+NIβ+NBγ, so per1000 rate isα+1000Iβ+1000Bγ. Treatment coefficient needs explicit scale conversion; fitted output/conversion missing. Dollar-sign/name syntax not separately tied to a reported value. No new candidate.
- **Locations and document roles:** DOC-003 p3 PLAN lines114–131.
- **Printed inputs:** Nlin=N/1000;GNlin=N*(d$Group==BedsidePEWS);EPOCH$$BNlin=N*Baseline;formula x~Nlin+GNlin+BNlin−1;Poissonidentity;commentsNlinG/NlinB.
- **Model, test and inferential definitions:** Rate model with exposure interaction; interceptscaledper1000,treatment regressorunscaled;literal $$ and d ambiguity.
- **Checks and outcome:** Dimensional check: coefficient on Nlin has /1000-day units; coefficient on unscaled GNlin has /day units. Different scaling is algebraically permissible if reported treatment coefficient multiplied1000; no executed coefficient/scale mapping supplied. $$ and d reference do not yield independently demonstrated reported-number contradiction. 
- **Missing definitions / limits:** Actual d object, corrected/executed formula and per1000 output conversion missing. Do not execute untrusted/incomplete illustrative code or infer output.

## S101 — SAP continuous illustrative code

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Narrative Gaussian individual model supplies intended family; illustrative x/y symbol difference and omitted family lack source output linkage. C025 heading question is separate from this code example. No library default or effect change inferred; no new candidate.
- **Locations and document roles:** DOC-003 p4 PLAN lines135–150.
- **Printed inputs:** Text ycontinuous;commenty;codegeeglm(x~Intervention+x0,idHospital,dataEPOCH,corstrexchangeable) without printedfamily.
- **Model, test and inferential definitions:** NarrativeGaussianGEEindividualcontinuous;hospitalbaseline x0.
- **Checks and outcome:** Response-symbol x/y discrepancy and missing explicitGaussian family in example noted. Text supplies intended Gaussian definition; no output tied to literal example, so no standalone reported-value candidate. 
- **Missing definitions / limits:** Execution and actualfamily parameter missing; do not infer library defaults.

## S102 — SAP sensitivity models

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Eight logit/log-rate versus five probability/rate sensitivity approaches are different contrasts/fits, not thirteen repeated results. No sensitivity outputs exist for duplicate or cross-model effect checks; no new candidate.
- **Locations and document roles:** DOC-003 p4–5 PLAN.
- **Printed inputs:** 8logit/log-rate approaches;5probability/rate approaches;weightedlogit/lograteinversevariance;quasibinomial/Poisson;GEE/GLMERpostonly/pre+post/time×treatment/baselinecovariate.
- **Model, test and inferential definitions:** Alternative sensitivity fits enumerated; ratios/probabilities/rates separated.
- **Checks and outcome:** Transforms/weights/contrast labels recorded; no sensitivity result values supplied. No fabricated comparison or forced identity across models. 
- **Missing definitions / limits:** Sensitivity outputs,weights,estimates,CIs/P absent.

## S103 — SAP ICU-readmission model/measure label

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** C016 Poisson shell versus logistic OR survives; corrected comparison excludes nonexistent protocol ICU-readmission logit claim and remains P_R only. New P2-A separately compares <48h label with before-third-midnight operational cutoff; different consistency rule from model/denominator. No other new candidate.
- **Locations and document roles:** DOC-003 p5 shelltable PLAN;DOC-001 p7 ICUreadmission row/footnoted REPORT.
- **Printed inputs:** SAPB_icur/B_PatientDischargesICU andP_icur/P_PatientDischargesICU:Poisson;REPORTOR1.11(.77,1.61),P.58:logistic.
- **Model, test and inferential definitions:** Identical ICUreadmission48h endpoint/ICUdischarge denominator; SAP shell count/Poisson versus reported binomial odds.
- **Checks and outcome:** ST-E concrete reported effect-measure/model label comparison: Poisson lograte would produce rate ratio, not reported logistic OR. No claim resulting number necessarily wrong. 
- **Missing definitions / limits:** Need whether shell stale/mislabeled or disclosed analysis revision, and which fittedmodel producedOR. Do not infer raw counts determine OR exactly.

## S104 — SAP hospital-readmission model/measure label

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** C017 Poisson shell versus reported logistic OR and protocol hospital-readmission logit survives with both direct PLAN/REPORT and PLAN/PLAN comparisons. New P2-B separately compares <48h label with calendar-day operational cutoff; no OR transformation performed. No other new candidate.
- **Locations and document roles:** DOC-003 p5 shelltable PLAN;DOC-001 p7 hospitalreadmission row/footnoted REPORT;DOC-002 p16 PLAN.
- **Printed inputs:** SAPB__hr/B_PatientDischarges andP__hr/P_PatientDischarges:Poisson;REPORTOR.93(.61,1.41),P.74:logistic;protocolunplannedreadmissionlogit.
- **Model, test and inferential definitions:** Identical hospitalreadmission48h endpoint/hospitaldischarge denominator; shellPoisson versus reportlogistic;protocolcorroborates report.
- **Checks and outcome:** ST-F concrete model/measure label mismatch; protocolcorroboration does not create independent discrepancy unless compared to SAP separately. This patient endpoint distinct fromICU S103. 
- **Missing definitions / limits:** Need shellstatus/modelrevision and fittedmodel provenance; ratio cannot recalculated from aggregates absent baseline fits.

## S105 — Subgroup inferential definitions

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Subgroup interactions lack reported estimates/CIs/P; nonreporting disclosed. Stratum removal and counts do not reconstruct missing subgroup statistics. C024 overnight staffing coverage does not identify service subgroup effect denominators. No new candidate.
- **Locations and document roles:** DOC-002 p16 PLAN;DOC-003 p6 PLAN;DOC-001 p5 REPORT.
- **Printed inputs:** Protocol4subgroupssize≥200,<200;MET;ECMO;wardinitiatedurgentICU;SAP2servicegroupsECMO/MET,oneGEEtreatment×subgroupinteraction;mainsaysnotreported.
- **Model, test and inferential definitions:** Interaction contrasts; effectswithinservice strata.
- **Checks and outcome:** No numerical subgroup outputs supplied; definitions covered. No candidate from nonreporting alone or absent variance. Stratification removal expressly explained. 
- **Missing definitions / limits:** No interactionestimate/CI/P or subgroup output.

## S106 — ICU per-patient aggregation and population

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** 393+531=924 baseline and686+967=1653 post patients reconcile;55 cross-period exclusions explicitly establish unique patient cohort. Admission counts differ legitimately. C013/C015 unit/denominator definitions survive; C024 category exhaustiveness assumption does not affect this population. No new candidate.
- **Locations and document roles:** DOC-003 p7 PLAN;DOC-004 p12–13 REPORT;DOC-001 p4–5,p8 REPORT.
- **Printed inputs:** Patientrecord;crossperiod55removed;393/686/531/967;LOSsum/mean;PIMandPELODaverageoveradmissions;VFDfirstadmission;technologysum;binaryanyuse.
- **Model, test and inferential definitions:** Perpatientanalysis forUrgentICU resource outcomes;hospitalclusters.
- **Checks and outcome:** One record/patient supports distinctdenominators fromTable3admissionevents. EveryeTable4inferentialrow separately tracked S024,S025,S067–S079;medians/IQRs descriptive companion,notmeanCIs. 
- **Missing definitions / limits:** Individualrecords/admission linkage absent; cannot reconstructGEEvariance or phasespanning denominator precisely fromaggregates.

## S107 — PIM probability transform and scale

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** C023 upper example diagnostic99.9943306823% versus99.9% retains cap/truncation question; nearest rounding is conditional. BE−35 matches both direct pages; no sign candidate. Inverse-logit is monotone; rounded predicted totals cannot reconstruct mean variance. No new candidate.
- **Locations and document roles:** DOC-004 p7,p13 REPORT;DOC-003 p7 PLAN.
- **Printed inputs:** inverse-logit1/(1+exp(−PIM));minimum−8.4137→.02%;PaO240/BE−35→+9.7778→99.9%;predictedpatienttotalsroundedinteger.
- **Model, test and inferential definitions:** PIM logit score transformed to predicteddeathprobability;averageprobabilitiesoveradmissions.
- **Checks and outcome:** Directionmonotone;inverse-logitminimum≈.0222%;high≈99.9943% (diagnostic) suppliesextreme probability wording rather than observeddeathcount. Directp13 minus−35 atlineend agreesp7;mapperpositive35 is transcription error,notcandidate. 
- **Missing definitions / limits:** PIM coefficient formula absent;99.9 may be conservative/truncateddescription; no roundingconvention stated; no exact PIMscore reconstruction.

## S108 — PELOD organ-dysfunction scale

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Raw PELOD0–71 bounds do not bound signed difference intervals to positive values. S078/S079 time windows and negative differences coherent; score average is not percentage or event rate. No new candidate.
- **Locations and document roles:** DOC-004 p7,p13 REPORT;DOC-003 p7 PLAN.
- **Printed inputs:** PELOD0–71,higherworse;first24h/entirestaymeanperpatient;differences S078−.12,S079−.29.
- **Model, test and inferential definitions:** Continuousmean GEE baselineadjusted;two separatewindows.
- **Checks and outcome:** Observedmeanswithin0–71;negativeadjusteddifferences directionreducedscore coherent;CIs can be signed because differences notrawscores. No inventedclinicalsignificance. 
- **Missing definitions / limits:** Rawpatient scores/covariance absent; no P-to-scale equivalence.

## S109 — Documentation Holm multiplicity family

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Holm adjusted values are no smaller than raw probabilities; rounding permits .05/.18 and .009/.04 pairs. The eight Table2 entries can reconcile as a displayed adjustment family; full21 membership/unrounded P allocation not supplied, so do not infer one common21-test Holm family from convention. No new candidate.
- **Locations and document roles:** DOC-001 p5 methods,p6 Table2footnoted REPORT.
- **Printed inputs:** Eightshowncomparisons;rawP<.001×4,.009,.05,.10,.50;adjusted<.001×4,.04,.18,.30,>.99.
- **Model, test and inferential definitions:** Holm posthoc adjustments;raw rounded values and inequalitybounds.
- **Checks and outcome:** Sortedrounded values admit compatibleunderlyingunroundedP;adjustments monotonewithin bounds. RR .05×4=.20 is not exact contradiction because underlying .045 may give .18;oxygen saturation .009×5=.045 may round .04 ifunderlying<.009. No candidate. 
- **Missing definitions / limits:** Complete21-family rawP and fullprecision not supplied; exactHolmreconstruction impossible.

## S110 — Exploratory outcome Holm multiplicity family

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Ten raw Table3 exploratory P values all≥.45 can have Holm ceiling1, displayed>.99. No exact whole21-family reconstruction without membership/fullprecision; Table2's separate adjusted values do not prove one-family contradiction. No new candidate.
- **Locations and document roles:** DOC-001 p5 methods,p7 Table3footnoteg REPORT.
- **Printed inputs:** TenTable3posthocrawP .69,.88,.92,.62,.83,.52,.64,.45,.58,.74;Holmall>.99;methods21prespecified.
- **Model, test and inferential definitions:** Holm posthoc multiplicity adjustment;familymembership beyondprintedrows not specified.
- **Checks and outcome:** Eventen-outcomealone .45×10 exceeds1; alladjusted values atceiling1 compatible. >.99 printedcoherent; no contradiction from unavailablefull21family. 
- **Missing definitions / limits:** Complete21family and fullprecision not supplied; no prescribedreconstruction.

## S111 — Historical pilot statistically significant changes

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** Historical pilot significance claims have no effect/CI/P/model inputs; direction can be compared but no uncertainty or contradiction reconstructed. Distinct trial outcome/population does not refute pilot result. No new candidate.
- **Locations and document roles:** DOC-002 p2,p5 PLAN.
- **Printed inputs:** Pilot single-site reductionslate transfer/statcalls,improvedcommunication declaredstatisticallysignificant;noeffect/CI/Pprinted.
- **Model, test and inferential definitions:** Historical pilot study nottrialresult;directiononly.
- **Checks and outcome:** Significanceclaimwithouteffectsize cannot checkinterval/P identity; no autonomouscandidate solely missingquantification. Later trialnegative mortality isdistinctpopulation/interventionevaluation. 
- **Missing definitions / limits:** Historicalcounts,models,CI/P/testdefinitions missing.

## S112 — ICC competence and score-concordance thresholds

- **Pass 1 status:** PASS_1_COMPLETE
- **Pass 2 status:** PASS_2_COMPLETE
- **Pass 2 checked outcome and recheck implication:** ICC>.90 competence and >80% within-two agreement are different quantities/tasks; no conversion. ≥80% REPORT adherence is not a fitted ICC/P result. Threshold versions require exact task alignment before conflict, absent here. No new candidate.
- **Locations and document roles:** DOC-002 p7–9 PLAN;DOC-001 p2–3 REPORT.
- **Printed inputs:** CompetenceICC>.90,noindividualscoredifference>2;10vitalsets/3cases;weeklyimplementation>80%within2;>5/7itemsin>80%;REPORT≥80%adherence.
- **Model, test and inferential definitions:** ICCcriterion versus operationalproportioncriteria;differenttasks/historicalgroups.
- **Checks and outcome:** ICC iscorrelation,notpercentageagreement;no conversionforced. Thresholdsmodel/definitiontrackedfornumericcrosslanes; no inferentialestimateattached toweekly≥80% 
- **Missing definitions / limits:** ICCformulation and pertraineescorematrix absent; no inferentialP/CI.


