# Workflow 1.6.2 Canonical Statistical Relationship Inventory

The canonical set is S001–S099, each with individual PASS_1_COMPLETE and PASS_2_COMPLETE facts below. Mapper-provenance tokens support3:S-301 through support3:S-317 refer to the original unhyphenated extraction keys in extraction/parts/support_plan_065_094.md; the hyphenated display distinguishes mapper-local keys from canonical relationship IDs without adding relationships. Those original mapper records are integrated at the explicit canonical records and remain preserved unchanged.

### S001

- **Mapper provenance:** main S001; P1-S001; S-P2-001; S-P2-011; support3:S-301; support3:S-303; P4-02; P1-N001.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=3), p.3 Statistical Analysis. Original grant design noninferiority margin 9%; changed to superiority following FLORALI/jury as condition of grant; revised IRB protocol published.
- **PASS_1_COMPLETE:** The report explicitly discloses the grant-stage noninferiority-to-superiority transition. Final PLAN pp.71–72,95,97 states superiority and mortality day 28. The report makes no noninferiority conclusion; the obsolete 9% margin is not applied to its superiority result. Outcome-status consequences are tracked at S070.
- **PASS_2_COMPLETE:** The report explicitly discloses NI 9% to superiority redesign; final PLAN superiority supports the reported hypothesis. No NI or equivalence conclusion uses the obsolete margin. Outcome-status history is already screened through F-ST1-008/F-XS-010; no additional inference conflict.

### S002

- **Mapper provenance:** main S002; support3:S-302; support3:S-317; P4-13.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=3), p.3 sample size; p.7 strengths. Expected C day 28 mortality 30%, H20%; alpha 5%, power 90%; required 779 patients (389 each group). p.7 claims assumptions for sample-size estimation met.
- **PASS_1_COMPLETE:** The final PLAN pp.90–91,103 prints 778=2×389; report p.3 prints 779 with 389 each. A one-person total discrepancy has relative display gap zero after half-unit intervals or less than 0.05. Diagnostic independent-proportions normal power formula with p C=.30,p H=.20,z(.975)=1.95996,z(.90)=1.28155 gives about 392/arm, close to 389; allowing printed integer percentage half-units includes 389. Exact design formula/continuity adjustment/interim adjustment are not supplied; no exact formula inferred. Report p.7 'assumptions ... met' is examined in excluded observations.
- **PASS_2_COMPLETE:** 779 total versus 2×389 and PLAN 778 has overlapping half-unit intervals, gap 0. The normal independent-proportions calculation is diagnostic, approximately 392 per arm; rounded 30%/20% inputs include 389. Exact power formula/interim adjustment is absent; wording about assumptions supplies no conflicting realized-power number.

### S003

- **Mapper provenance:** main S003; S-P2-018; S-P2-031; P4-10; P4-14; P4-22 (interim portion).
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=3), pp.3,5 interim. Scheduled at 100 deaths; Haybittle-Peto P threshold.001; Bayesian posterior mortality/log OR using uniform noninformative prior for futility/efficacy, no specific stopping rules prespecified. Interim observed P=.94, continued.
- **PASS_1_COMPLETE:** Observed interim P=.94 exceeds Haybittle–Peto .001; continuation follows the printed boundary. Final PLAN pp.102–103 agrees. Bayesian posterior rates/log OR and uniform prior are described without a numerical decision threshold, so no posterior threshold is inferred. Initial PLAN p.53 no interim differs from revised design; report explicitly discloses redesign. Safety DSMB interim wording at initial p.61 can be periodic safety review rather than the efficacy test.
- **PASS_2_COMPLETE:** Interim P=.94 is above the stated .001 Haybittle–Peto boundary and supports continuation. Final PLAN retains 100-death trigger and .05 terminal threshold. Uniform prior is stated but no posterior stopping threshold is supplied; one is not inferred.

### S004

- **Mapper provenance:** main S004; S-P2-005; S-P2-014; S-P2-019; support3:S-305; P4-05 (analysis-set portion).
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=3), p.3 population/missing data. Intent-to-treat assigned arm; only postrandomization exclusions withdrawn consent; no exclusion because missing/incomplete data; medians(IQR) and proportions descriptive.
- **PASS_1_COMPLETE:** 389 randomized per arm minus one consent withdrawal per arm gives 388; 2×388=776 analyzed. Report says no exclusions for missing data, not that every longitudinal measurement is observed. PLAN consent pp.74,79 permits data-use decisions on withdrawal. Final all-randomized ITT wording and source consent exclusions do not identify a conflicting analyzable count. Missing measurement denominators do not imply deletion from primary analysis.
- **PASS_2_COMPLETE:** 389−1=388 in each arm and 2×388=776. Consent exclusions are expressly allowed; incomplete measurements do not imply primary-set exclusion. Subgroup population mapping remains the already-screened F-NUM-003 issue; no additional count or missing-data conflict.

### S005

- **Mapper provenance:** main S005; S-P2-022; support3:S-307; P4-17 (primary-model portion).
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=3), p.3 primary methods. Kaplan-Meier overall mortality; administrative censoring alive in ICU day 28; absolute risk difference 95% CI and univariable Cox HR95% CI; proportional-hazards weighted-residual P=.72.
- **PASS_1_COMPLETE:** REPORT p.3 gives Kaplan–Meier mortality, absolute RD and univariable Cox HR; PLAN pp.54,82,104 instead specifies binary day-28 RR and confounder-adjusted analyses. F-ST1-002 records the primary-analysis departure. Weighted-residual PH P=.72 is not significant; no numerical residual/test statistic, df or covariance is supplied, so exact reproduction is unavailable.
- **PASS_2_COMPLETE:** Kaplan–Meier/RD/univariable Cox are affirmatively reported; PH residual P=.72 is nonsignificant. Final PLAN binary RR, adjustment and PP departures are already screened under F-XS-004. Exact residual statistic/df/covariance is unavailable; no preferred model is proposed.

### S006

- **Mapper provenance:** main S006; S-P2-024; support3:S-309; support3:S-310; P4-18.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=3), pp.3-4 IMV methods. Death without IMV competing risk; nonparametric cumulative incidence; Gray test; univariable cause-specific Cox HR.
- **PASS_1_COMPLETE:** REPORT pp.3–4 gives death without IMV as competitor, nonparametric cumulative incidence, Gray comparison and univariable cause-specific Cox HR. PLAN pp.54,82,105 includes live ICU discharge as additional competitor and confounder adjustment. F-ST1-004 records that changed framework. Supplement e Figure 1 test label is independently tracked at S079.
- **PASS_2_COMPLETE:** Report IMV death competitor, cumulative incidence, Gray and univariable cause-specific Cox map coherently within the named framework. PLAN discharge/adjustment differences are already F-XS-006; supplemental log-rank mapping is already F-XS-003. Missing event times prevent a refit, without creating a further observation.

### S007

- **Mapper provenance:** main S007; P4-18 (infection-test portion).
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=4), p.4 infection methods. Two proportions compared by chi-square; Table 2 relative measure recorded separately in S016.
- **PASS_1_COMPLETE:** REPORT p.4 names chi-square comparison for infection proportions; P=.91 is compatible diagnostically with continuity-corrected chi-square for 39/388 versus 41/388 (about.906). Continuity correction is not stated and is not assigned as the definitive test. Final PLAN p.105 instead describes Gray comparison/cause-specific Cox adjustment, tracked in F-ST1-004.
- **PASS_2_COMPLETE:** Infection proportions explicitly use chi-square; a continuity-corrected diagnostic gives about .906 for 39/388 versus 41/388, compatible with .91 but not assigned as the exact unstated variant. Planned incidence/Gray/adjustment comparison is already F-XS-006, and HR interval construction already F-ST1-011.

### S008

- **Mapper provenance:** main S008; S-P2-025; support3:S-311; P4-19.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=4), p.4 quantitative methods. Wilcoxon rank-sum for comfort/dyspnea visual analog scales, respiratory rate and ICU stay; relative risk for ICU and hospital mortality.
- **PASS_1_COMPLETE:** REPORT Wilcoxon rank-sum is internally coherent for independent randomized groups and quantitative available observations; it is not compared numerically to a mean-difference CI as if the same statistic were tested. PLAN survival/competing-risk LOS analyses and survivor/decedent analyses differ; F-ST1-006. Joint models separately S062.
- **PASS_2_COMPLETE:** Independent-group Wilcoxon comparisons are internally coherent with the randomized design. Mean differences are not equated to median differences or Wilcoxon statistics. Planned ICU-stay analyses already F-XS-008; planned longitudinal methods already F-XS-007. No paired-design contradiction is supplied.

### S009

- **Mapper provenance:** main S009; S-P2-010; S-P2-016; S-P2-023; support3:S-308; P4-06 (interaction portion); P4-17 (interaction portion).
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=4), p.4 subgroups; p.7 caption. Cox HRs in stratification-defined subgroups, Gail and Simon interaction test; named flow/vasopressors/ICU-time strata; figure adds oxygenation, diagnosis and malignancy displays.
- **PASS_1_COMPLETE:** Each printed interaction P belongs to a paired subgroup comparison, not the P for an individual HR. All interaction P values are ≥.05 except IMV hematologic-malignancy P=.01. The statement of no interaction applies to the three named stratification subgroups, whose printed P=.15,.39,.15 (mortality) and .17,.65,.83 (IMV) are nonsignificant. No df, variance or full Gail–Simon statistic is supplied. Changed subgroup boundaries tracked at S067/F-ST1-007; Figure 3 explicitly calls all displayed subgroups predefined; the unknown-diagnosis and hematologic-malignancy analyses are absent from the supplied prospective subgroup specifications, F-ST1-014.
- **PASS_2_COMPLETE:** Stratification interactions .15/.39/.15 for mortality and .17/.65/.83 for IMV are nonsignificant, agreeing with the three-strata statement. Malignancy IMV .01 is a different exploratory interaction; its prespecification and cutpoints are already F-XS-014/F-XS-012. No Gail–Simon statistic or variance is supplied.

### S010

- **Mapper provenance:** main S010; S-P2-015 (secondary-sidedness portion); P4-15 (secondary-sidedness portion).
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=4), pp.4,8 multiplicity/post hoc. No handling of secondary multiple-comparison type I inflation; secondary exploratory; post hoc site primary frailty model, intubated subset; no strata-adjusted treatment estimates(p.8).
- **PASS_1_COMPLETE:** Exploratory secondary status and absence of multiplicity correction are explicitly stated. No multiplicity-controlled superiority claim is printed. The .01 malignancy interaction is treated as exploratory. Post hoc frailty/site and intubated-subset labels examined against supplied plans, with the latter tracked F-ST1-008.
- **PASS_2_COMPLETE:** Secondary multiplicity handling is explicitly absent and conclusions are exploratory; no controlled secondary rejection claim conflicts with a stated rule. Center frailty is expressly post hoc. Intubated-subset status change is already F-XS-010, rather than a new multiplicity issue.

### S011

- **Mapper provenance:** main S011; support3:S-313; P4-12 (software portion); S-P2-026 (software portion).
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=5), p.5 P rules/software. All P two-sided; significant P<.05; R3.1.0. No test statistic or standard error printed.
- **PASS_1_COMPLETE:** All REPORT P values are two-sided and alpha=.05. All displayed CIs are 95%. No test statistics or standard errors are directly printed. SAS/R in PLAN and R3.1.0 in REPORT are compatible, not a result-changing discrepancy.
- **PASS_2_COMPLETE:** REPORT states two-sided P<.05 and prints 95% CIs. No test statistic or standard error is printed. PLAN SAS/R and REPORT R3.1.0 are compatible. No absent df/model/test detail is inferred from convention.

### S012

- **Mapper provenance:** main S012.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=1), p.1 Abstract mortality. H35.6%/C36.1%; difference-0.5 percentage points(CI-7.3,+6.3); HR 0.98(.77,1.24), P=.94; nonsignificant day 28.
- **PASS_1_COMPLETE:** RD −.5 is within[−7.3,6.3], HR .98 within[.77,1.24]; both intervals include null and P=.94>.05; direction and nonsignificant conclusion agree. Exact P from HR CI is not asserted without a specified HR test. Same primary occurrences are preserved at S013,S029.
- **PASS_2_COMPLETE:** Abstract RD−.5 within [−7.3,6.3] and HR.98 within [.77,1.24] have ordered null-containing intervals; P=.94 and the nonsignificant primary conclusion agree. Table 2 matches; no exact HR-Wald P is assumed.

### S013

- **Mapper provenance:** main S013.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=5), p.5 Table 2 primary and Primary Outcome. H138/388(35.6%), C140/388(36.1%); absolute RD-0.5(-7.3,6.3); HR.98(.77,1.24), P=.94; matched Abstract, Key Points p.2, Conclusions pp.1/8; no significant interaction 3 predefined subgroups narrative.
- **PASS_1_COMPLETE:** 138/388=35.567% and 140/388=36.082%; difference−.51546pp, printed−.5. RD and HR CIs ordered/contain estimates and include null; P=.94 nonsignificant. Abstract/body agree. Figure 3 contrast differs (F-ST1-001). Diagnostic log-HR interval based on sqrt(1/138+1/140) reproduces its displayed endpoints within half-units; not an exact Cox refit.
- **PASS_2_COMPLETE:** 138/388=35.567% and 140/388=36.082%; RD−.51546 pp matches −.5 at half-unit precision. Both primary intervals include null and P=.94 agrees. Figure 3 reference discrepancy already F-NUM-004; model covariance and Table 2 P mapping remain unavailable.

### S014

- **Mapper provenance:** main S014.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=1), p.1 Abstract IMV. H38.7%/C43.8%; difference-5.1(-12.3,+2.0) percentage points, nonsignificant.
- **PASS_1_COMPLETE:** RD−5.1 within[−12.3,2.0]; zero included; abstract conclusion nonsignificant agrees with paired main result P=.17. Risks match Table 2 under rounding.
- **PASS_2_COMPLETE:** IMV RD−5.1 lies within [−12.3,2.0], includes 0 and supports the abstract nonsignificance. Risks 38.7/43.8 match 150/388 and 170/388; matched body P=.17 is nonsignificant. No additional abstract/body conflict.

### S015

- **Mapper provenance:** main S015.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=5), p.5 Table 2 IMV; p.6 Secondary. H150(38.7%)/C170(43.8%); RD-5.1(-12.3,2.0); cause-specific HR.85(.68,1.06); P=.17; cumulative intubation nonsignificant, e Figure 1 pointer.
- **PASS_1_COMPLETE:** 150/388=38.660%,170/388=43.814%,RD−5.15464pp. RD and cause-specific HR .85 [.68,1.06] are contained, ordered, include null and agree with P=.17 and narrative. Diagnostic log-event interval with sqrt(1/150+1/170) gives[.68244,1.05870], matching display. Full risk sets/competing-event times and fitted covariance are unavailable.
- **PASS_2_COMPLETE:** IMV RD−5.1 and cause-specific HR.85 lie within their ordered null-containing 95% CIs; P=.17 and narrative agree. Event-count log-interval construction is diagnostic and reproduces [.68,1.06]. Forest direction and test-name mapping remain existing F-NUM-004/F-XS-003 issues.

### S016

- **Mapper provenance:** main S016.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=5), p.5 Table 2 infection; pp.1,6. H39(10.0%)/C41(10.6%); RD-.6(-4.6,4.1); cause-specific HR 1.01(.96,1.06); P=.91; nonsignificant, abstract/narrative repeat risks and RD.
- **PASS_1_COMPLETE:** 39/388=10.052%,41/388=10.567%; RD−.51546pp. RD−.6 and HR 1.01 each contained in ordered intervals; both nulls included; P=.91 nonsignificant. Main abstract/body match. The HR interval [.96,1.06] does not reproduce under the event-count diagnostic that reproduces the other HR rows in this same display; F-ST1-011. The source-specific infection HR variance/interval construction is the human question.
- **PASS_2_COMPLETE:** Infection RD−.6 within [−4.6,4.1] and HR 1.01 within [.96,1.06] both include null, consistent with P=.91. Risks/counts pass half-unit precision. The narrower HR interval is already F-ST1-011; distinct proportion P is not forced into an HR-Wald test.

### S017

- **Mapper provenance:** main S017.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=5), p.5 Table 2 ICU mortality. H123(31.7%)/C122(31.4%); RD.3(-6.3,6.8); RR 1.01(.82,1.24); P=.64.
- **PASS_1_COMPLETE:** 123/388=31.701%,122/388=31.443%;RD+.25773pp and RR123/122=1.00820, matching+.3 and 1.01 under half-units. Ordered CIs contain estimates/null, P=.64>.05. No stated secondary mortality test beyond effect measure permits exact P reconstruction.
- **PASS_2_COMPLETE:** ICU123/388 and 122/388 yield RD+.25773 pp andRR1.00820, matching+.3/1.01. CIs[−6.3,6.8]/[.82,1.24] contain point/null;P=.64 is nonsignificant. The source does not name the secondary mortality test, so an exact P calculation is not assigned.

### S018

- **Mapper provenance:** main S018.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=5), p.5 Table 2 hospital mortality. H160(41.2%)/C162(41.7%); RD-.5(-7.5,6.4); RR.99(.84,1.17); P=.77.
- **PASS_1_COMPLETE:** 160/388=41.237%,162/388=41.753%;RD−.51546pp and RR160/162=.98765, matching−.5/.99. Ordered CIs contain estimates/null, P=.77>.05. Test mapping unspecified; exact P not inferred.
- **PASS_2_COMPLETE:** Hospital 160/388 and 162/388 yield RD−.51546 pp andRR.98765, matching−.5/.99 at precision. CIs[−7.5,6.4]/[.84,1.17] are ordered and contain point/null;P=.77 is nonsignificant. Missing named test limits exact P reproduction.

### S019

- **Mapper provenance:** main S019.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=5), p.5 Table 2 ICU stay; pp.1,6. H median 8(4-14)/C6(4-13) days; mean difference.6(-1.0,2.2) days; relative difference NA; P=.07.
- **PASS_1_COMPLETE:** ICU medians 8/6 and their IQRs are ordered. Mean difference+.6 in[−1.0,2.2] and Wilcoxon P=.07 both nonsignificant. A difference of medians 2 is not the stated mean difference. Planned LOS methods examined in S008.
- **PASS_2_COMPLETE:** ICU mean difference+.6 within [−1.0,2.2] and WilcoxonP=.07 are both nonsignificant. Medians 8/6 with ordered IQRs do not define the mean contrast. Planned ICU estimator/population differences already F-XS-008.

### S020

- **Mapper provenance:** main S020.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=5), p.5 Table 2 hospital stay; pp.1,6. H median 24(14-40)/C27(15-42) days; mean difference-2(-7.3,3.3) days; relative difference NA; P=.60.
- **PASS_1_COMPLETE:** Hospital medians 24/27 and IQRs ordered; mean difference−2 within[−7.3,3.3], null included, P=.60>.05. The difference of medians−3 is not equated to the mean difference. Hospital-stay test/CI estimator not further specified.
- **PASS_2_COMPLETE:** Hospital mean difference−2 within [−7.3,3.3] and P=.60 agree in nonsignificance. Medians 24/27 and ordered IQRs are distinct summaries; no median-equality rule applies. Hospital test/CI construction is not specified sufficiently for exact refit.

### S021

- **Mapper provenance:** main S021; R4-02 (respiratory row).
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=1), p.1 Abstract respiratory. After 6h H25/C26 per min; difference-1.8(-3.2,-0.2)/min; significantly lower.
- **PASS_1_COMPLETE:** Mean difference−1.8 contained in[−3.2,−.2], both endpoints<0 and significant claim agrees. Body upper endpoint−.3 differs; comparing half-unit intervals [−.25,−.15] and[−.35,−.25] yields zero gap, so rounding. Median 25/26 is not equated to mean difference.
- **PASS_2_COMPLETE:** Abstract respiratory difference−1.8 is contained in[−3.2,−.2], excluding 0 and supporting lower-rate conclusion. Body upper−.3 and abstract−.2 half-unit intervals touch at−.25, gap 0; no significance reversal.

### S022

- **Mapper provenance:** main S022; R4-02 (respiratory row).
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=6), p.6 Secondary respiratory. After 6h H25/C26 per min; mean difference-1.8(-3.2,-0.3)/min; significantly lower; e Figure 2/e Table supplement 2 pointer.
- **PASS_1_COMPLETE:** Mean difference−1.8 contained in[−3.2,−.3], excluding 0; significant narrative agrees. e Table medians 25/26 and graph approximate means are separate summaries. No P/statistic printed for precise reproduction.
- **PASS_2_COMPLETE:** Body respiratory difference−1.8 is contained in ordered[−3.2,−.3], excluding 0 with matching significant narrative. Supplement medians 25/26 are a separate summary. No printed individual P or statistic allows a stronger exact test comparison.

### S023

- **Mapper provenance:** main S023; R4-02 (oxygenation row).
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=1), pp.1,6 oxygenation. H150/C119; mean difference 19.5(4.4,34.6) PaO2:FIO2; significantly higher; abstract time label PaO2:FIO2 over 3 days after intubation, narrative until day 4.
- **PASS_1_COMPLETE:** Mean difference 19.5 in[4.4,34.6], interval ordered/excludes 0; higher-oxygenation conclusion agrees. Median 150/119 is not equated to a mean difference 19.5. Abstract outcome window '3 days after intubation' differs from supplement 6h after randomization and repeated randomization-day figure; F-ST1-009. PLAN day 1–3 oxygenation/joint-model analyses separately S062,S070.
- **PASS_2_COMPLETE:** Oxygenation 19.5 within [4.4,34.6] excludes 0 and agrees with higher oxygenation. Paired medians 150/119 are not a mean contrast. Population/time-origin conflict already F-XS-001; planned joint model/component omissions already F-XS-007/F-XS-009. Undefined plot stars are not a P value.

### S024

- **Mapper provenance:** main S024; R4-06; R4-07.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=1), pp.1,6 comfort/dyspnea. No significant group difference at any time; e Figure 3 supplement 2 pointer; no numeric score/test printed main paper.
- **PASS_1_COMPLETE:** Comfort/dyspnea nonsignificance has no printed individual P or 95% between-group CI in REPORT. Supplement bars have no definition; they are not assumed confidence intervals or used to reverse significance. Planned joint models and Borg measure examined S062,S070.
- **PASS_2_COMPLETE:** Comfort/dyspnea nonsignificance has no individual P or defined 95% between-arm CI to contradict it. Undefined graphical bars are not treated as CIs. Positive planned joint models and Borg omission already F-XS-007/F-XS-009.

### S025

- **Mapper provenance:** main S025.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=6), p.6 intubation time. Among needed IMV, median 1(IQR0-2) day; mean difference-.5(-1.2,.1) days; no significant difference.
- **PASS_1_COMPLETE:** Mean time difference−.5 lies within ordered[−1.2,.1], includes 0 and agrees with nonsignificance. IQR0–2 contains median 1. Individual timings/variance and test not supplied.
- **PASS_2_COMPLETE:** Intubation-time mean difference−.5 is within ordered[−1.2,.1], including 0 and matching nonsignificance. Median 1 is inside IQR0–2. Individual time distribution, variance and test are absent; none is supplied by convention.

### S026

- **Mapper provenance:** main S026; P1-S005 (post-intubation mortality); S-P2-003; S-P2-010 (intubated subgroup).
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=6), p.6 intubated mortality. H55.3%/C52.3%; RD+3(-8.5,+14.5) percentage points; P=.65; no significant difference.
- **PASS_1_COMPLETE:** 55.3−52.3=3.0pp; estimate+3 within[−8.5,14.5], includes 0, P=.65>.05 agrees. Denominators are intubated subsets 150/170, not whole arms. Prespecified post-intubation mortality in initial PLAN versus REPORT post hoc status is F-ST1-008.
- **PASS_2_COMPLETE:** Intubated mortality 55.3−52.3=3 pp;3 is inside[−8.5,14.5] and P=.65 is nonsignificant. Intubated subsets 150/170 are the relevant denominator context. Secondary-to-post-hoc history already F-XS-010; no new estimate/test conflict.

### S027

- **Mapper provenance:** main S027.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=6), p.6 cancer comparison. Patients with/without cancer as immunosuppression cause; day 28 RD+1.8(-10.8,+14.3); P=.50, nonsignificant. No armwise risks printed.
- **PASS_1_COMPLETE:** Difference+1.8 in ordered[−10.8,14.3], includes 0, P=.50>.05 agrees. This is the cancer versus no-cancer comparison described in narrative, not the treatment-by-hematologic-malignancy interaction in Figure 3. Arm/cancer risks and test not supplied.
- **PASS_2_COMPLETE:** Cancer-comparison RD 1.8 within [−10.8,14.3] includes 0 and agrees with P=.50. This narrative comparison is not Figure 3 treatment-by-hematologic interaction. No armwise cancer risks, covariance or named test is supplied for exact calculation.

### S028

- **Mapper provenance:** main S028.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=6), p.6 site effect. Mortality P=.33; intubation P=.07; both nonsignificant.
- **PASS_1_COMPLETE:** Mortality site P=.33 and IMV site P=.07 are both>.05, consistent with nonsignificance. Mortality frailty analysis explicitly post hoc; no statistic/covariance/df supplied. No exact reconstruction attempted.
- **PASS_2_COMPLETE:** Site mortalityP=.33 and intubationP=.07 are above.05 and agree with nonsignificance. Site/frailty analysis is separately named post hoc; no statistic/df/variance is available. Neither P is mapped to a treatment HR.

### S029

- **Mapper provenance:** main S029.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=6), p.6 Figure 2. Log-rank P=.85; Kaplan-Meier day 28 mortality curves; median survival not reached. Risk sets in N058.
- **PASS_1_COMPLETE:** Figure 2 log-rank P=.85>.05 agrees with mortality-null CIs and nonsignificance. Table 2 P=.94 versus figure log-rank .85 need not be the same named test; the source does not assign Table 2 P specifically to log-rank. PH residual test P=.72 is a third, distinct hypothesis. At-risk counts are tracking, not additive deaths. No median survival is claimed.
- **PASS_2_COMPLETE:** Figure 2 log-rankP=.85 is nonsignificant, agreeing with primary null-containing intervals. Table 2P=.94 is not expressly assigned to that log-rank test; PH P=.72 is another hypothesis. No same-analysis interval/P conflict is reproduced. Risk sets are not additive deaths.

### S030

- **Mapper provenance:** main S030.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=5), p.5 Table 2 footnotes. Header Mean Difference,%(95% CI); footnote b absolute risk difference binary mortality/IMV/infections, difference in means quantitative stay; d cause-specific HR; e stay effect cannot be HR; no lost follow-up.
- **PASS_1_COMPLETE:** Footnote explicitly defines binary absolute RD and quantitative difference of means despite common header. No HR claimed for LOS. All Table 2 estimates contained and endpoint orders checked. HR footnote labels IMV/infection as cause-specific, and both are examined with their corresponding method/text.
- **PASS_2_COMPLETE:** Table 2 footnotes distinguish binary RD from quantitative mean difference and cause-specific HR from RR; no LOS HR is supplied. All points are contained and endpoints ordered. Infection interval construction and IMV forest contrast remain previously screened issues.

### S031

- **Mapper provenance:** main S031.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3A ICU time 0-1d. Deaths H120/321,C118/330; HR.95(.74,1.22).
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.
- **PASS_2_COMPLETE:** Mortality ICU0–1 HR.95 in[.74,1.22] includes 1;120≤321 and 118≤330. No individual subgroup P is printed. ICU-time definition and shared contrast are already F-XS-012/F-NUM-004; interaction.15 tests the paired subgroups.

### S032

- **Mapper provenance:** main S032.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3A ICU time>=2d. Deaths H18/67,C22/58; HR 1.55(.83,2.90); time interaction P=.15 shared with S031.
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.
- **PASS_2_COMPLETE:** Mortality ICU≥2 HR 1.55 in[.83,2.90] includes 1;18≤67 and 22≤58. Paired interaction.15 is nonsignificant and is not this HR test. Day 2 regrouping and reference issue are already F-XS-012/F-NUM-004.

### S033

- **Mapper provenance:** main S033.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3A PaO2:FIO2<200. Deaths H99/237,C95/251; HR.89(.68,1.19).
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.
- **PASS_2_COMPLETE:** Mortality PaO2<200 HR.89 in[.68,1.19] includes 1;99≤237 and 95≤251. No subgroup P is printed. Reduced covariate-population accounting already F-NUM-003; figure reference already F-NUM-004.

### S034

- **Mapper provenance:** main S034.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3A PaO2:FIO2>=200. Deaths H16/65,C10/35; HR 1.18(.54,2.60); oxygenation interaction P=.52 shared with S033.
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.
- **PASS_2_COMPLETE:** Mortality PaO2≥200 HR 1.18 in[.54,2.60] includes 1;16≤65 and 10≤35. Paired interaction.52 is nonsignificant and not a subgroup P. Population and shared-reference questions are already F-NUM-003/F-NUM-004.

### S035

- **Mapper provenance:** main S035.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3A flow<=9L/min. Deaths H122/348,C127/347; HR 1.06(.83,1.36).
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.
- **PASS_2_COMPLETE:** Mortality flow≤9 HR 1.06 in[.83,1.36] includes 1;122≤348 and 127≤347. Flow partitions with S036 sum to 388/388 and 138/140 deaths. Plan/report equality boundary already F-XS-012; reference already F-NUM-004.

### S036

- **Mapper provenance:** main S036.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3A flow>9L/min. Deaths H16/40,C13/41; HR.76(.36,1.57); flow interaction P=.39 shared with S035.
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.
- **PASS_2_COMPLETE:** Mortality flow>9 HR.76 in[.36,1.57] includes 1;16≤40 and 13≤41. Interaction.39 is nonsignificant. Exact 9 L boundary and shared contrast are already F-XS-012/F-NUM-004; crude counts do not establish a fitted HR.

### S037

- **Mapper provenance:** main S037.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3A catecholamines No. Deaths H121/355,C126/349; HR 1.08(.84,1.39).
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.
- **PASS_2_COMPLETE:** Mortality catecholamine No HR 1.08 in[.84,1.39] includes 1;121≤355 and 126≤349. Together with S038 the denominators and deaths sum to full arms. Shared figure-reference issue already F-NUM-004; no individual subgroup P.

### S038

- **Mapper provenance:** main S038.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3A catecholamines Yes. Deaths H17/33,C14/39; HR.62(.31,1.26); catecholamine interaction P=.15 shared with S037.
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.
- **PASS_2_COMPLETE:** Mortality catecholamine Yes HR.62 in[.31,1.26] includes 1;17≤33 and 14≤39. Interaction.15 is a separate nonsignificant test. No covariance/event-time data permit a refit; shared contrast issue already F-NUM-004.

### S039

- **Mapper provenance:** main S039.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3A unknown diagnosis No. Deaths H99/297,C95/303; HR.93(.70,1.23).
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs. The figure's predefined status for this clinical subgroup is F-ST1-014.
- **PASS_2_COMPLETE:** Mortality diagnosis No HR.93 in[.70,1.23] includes 1;99≤297 and 95≤303. Paired populations/event totals sum correctly. Shared contrast already F-NUM-004 and predefined status already F-XS-014; no individual subgroup P.

### S040

- **Mapper provenance:** main S040.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3A unknown diagnosis Yes. Deaths H39/91,C45/85; HR 1.39(.90,2.13); diagnosis interaction P=.12 shared with S039.
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs. The figure's predefined status for this clinical subgroup is F-ST1-014.
- **PASS_2_COMPLETE:** Mortality diagnosis Yes HR 1.39 in[.90,2.13] includes 1;39≤91 and 45≤85. Interaction.12 is nonsignificant and is not a subgroup P. Diagnosis predefined status and shared contrast are already F-XS-014/F-NUM-004.

### S041

- **Mapper provenance:** main S041.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3A hematologic malignancy No. Deaths H66/199,C72/198; HR 1.11(.79,1.55).
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs. The figure's predefined status for this clinical subgroup is F-ST1-014.
- **PASS_2_COMPLETE:** Mortality hematologic No HR 1.11 in[.79,1.55] includes 1;66≤199 and 72≤198. Reduced subgroup-population mapping already F-NUM-003; predefined status already F-XS-014 and reference already F-NUM-004.

### S042

- **Mapper provenance:** main S042.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3A hematologic malignancy Yes. Deaths H64/167,C65/181; HR.94(.67,1.33); malignancy interaction P=.5 shared with S041.
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs. The figure's predefined status for this clinical subgroup is F-ST1-014.
- **PASS_2_COMPLETE:** Mortality hematologic Yes HR.94 in[.67,1.33] includes 1;64≤167 and 65≤181. Paired interaction.5 is nonsignificant. Death-sum gaps below 5% remain screened; population, prespecification and contrast questions already recorded.

### S043

- **Mapper provenance:** main S043.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3A all. Deaths H138/388,C140/388; HR 1.02(.81,1.29).
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.
- **PASS_2_COMPLETE:** All-patient mortality HR 1.02 in[.81,1.29] includes 1;138/388 and 140/388 match Table 2 counts. Table 2 point-copy precision gap.030/.98=.030612 is below 5%; shared forest direction pattern already F-NUM-004.

### S044

- **Mapper provenance:** main S044.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3B ICU time 0-1d. IMV H128/321,C142/330; HR 1.1(.87,1.40).
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.
- **PASS_2_COMPLETE:** IMV ICU0–1 HR 1.1 in[.87,1.40] includes 1;128≤321 and 142≤330. With S045 counts total 150/170 among 388/388. Time regrouping and figure-reference questions already F-XS-012/F-NUM-004.

### S045

- **Mapper provenance:** main S045.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3B ICU time>=2d. IMV H22/67,C28/58; HR 1.69(.96,2.95); time interaction P=.17 shared with S044.
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.
- **PASS_2_COMPLETE:** IMV ICU≥2 HR 1.69 in[.96,2.95] includes 1;22≤67 and 28≤58. Interaction.17 is nonsignificant, distinct from the individual HR test. Day 2 membership and shared contrast already F-XS-012/F-NUM-004.

### S046

- **Mapper provenance:** main S046.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3B PaO2:FIO2<200. IMV H99/237,C117/251; HR 1.17(.90,1.53).
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.
- **PASS_2_COMPLETE:** IMV PaO2<200 HR 1.17 in[.90,1.53] includes 1;99≤237 and 117≤251. No individual subgroup P. Covariate-population deficit already F-NUM-003 and shared reference already F-NUM-004; no crude-HR equality is imposed.

### S047

- **Mapper provenance:** main S047.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3B PaO2:FIO2>=200. IMV H27/65,C13/35; HR.88(.46,1.71); oxygenation interaction P=.44 shared with S046.
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.
- **PASS_2_COMPLETE:** IMV PaO2≥200 HR.88 in[.46,1.71] includes 1;27≤65 and 13≤35. Interaction.44 is nonsignificant and is a different hypothesis. Population/contrast accounting already F-NUM-003/F-NUM-004.

### S048

- **Mapper provenance:** main S048.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3B flow<=9L/min. IMV H136/348,C151/347; HR 1.15(.91,1.45).
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.
- **PASS_2_COMPLETE:** IMV flow≤9 HR 1.15 in[.91,1.45] includes 1;136≤348 and 151≤347. With S049 events/denominators sum to full arms. Exact 9 L membership and reference remain already F-XS-012/F-NUM-004.

### S049

- **Mapper provenance:** main S049.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3B flow>9L/min. IMV H14/40,C19/41; HR 1.37(.68,2.72); flow interaction P=.65 shared with S048.
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.
- **PASS_2_COMPLETE:** IMV flow>9 HR 1.37 in[.68,2.72] includes 1;14≤40 and 19≤41. Interaction.65 is nonsignificant, distinct from the HR test. Flow boundary and shared-reference questions already screened.

### S050

- **Mapper provenance:** main S050.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3B catecholamines No. IMV H137/355,C154/349; HR 1.18(.94,1.49).
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.
- **PASS_2_COMPLETE:** IMV catecholamine No HR 1.18 in[.94,1.49] includes 1;137≤355 and 154≤349. With S051 events and denominators match 150/170 and 388/388. Shared reference already F-NUM-004; no individual subgroup P.

### S051

- **Mapper provenance:** main S051.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3B catecholamines Yes. IMV H13/33,C16/39; HR 1.09(.52,2.26); catecholamine interaction P=.83 shared with S050.
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.
- **PASS_2_COMPLETE:** IMV catecholamine Yes HR 1.09 in[.52,2.26] includes 1;13≤33 and 16≤39. Interaction.83 is nonsignificant and is not a subgroup P. No fitted covariance/event times are available; shared reference already recorded.

### S052

- **Mapper provenance:** main S052.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3B unknown diagnosis No. IMV H114/297,C135/303; HR 1.18(.92,1.52).
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs. The figure's predefined status for this clinical subgroup is F-ST1-014.
- **PASS_2_COMPLETE:** IMV diagnosis No HR 1.18 in[.92,1.52] includes 1;114≤297 and 135≤303. Paired events/populations sum to full arms. Shared reference and predefined status already F-NUM-004/F-XS-014; no individual subgroup P.

### S053

- **Mapper provenance:** main S053.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3B unknown diagnosis Yes. IMV H36/91,C35/85; HR 1.15(.72,1.82); diagnosis interaction P=.9 shared with S052.
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs. The figure's predefined status for this clinical subgroup is F-ST1-014.
- **PASS_2_COMPLETE:** IMV diagnosis Yes HR 1.15 in[.72,1.82] includes 1;36≤91 and 35≤85. Interaction.9 is nonsignificant. Positive predefined claim already F-XS-014; shared contrast already F-NUM-004.

### S054

- **Mapper provenance:** main S054.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3B hematologic malignancy No. IMV H61/199,C89/198; HR 1.61(1.16,2.23).
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval[1.16,2.23] excludes 1; no individual subgroup P is printed, so no interval/P conflict can be assessed. The paired hematologic-malignancy interaction P=.01 is significant and is a different hypothesis. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs. The figure's predefined status for this clinical subgroup is F-ST1-014.
- **PASS_2_COMPLETE:** IMV hematologic No HR 1.61 is within [1.16,2.23], excluding 1;61≤199 and 89≤198. No individual subgroup P exists to contradict that interval. Paired interaction.01 is a different significant exploratory test; status/population/reference already screened.

### S055

- **Mapper provenance:** main S055.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3B hematologic malignancy Yes. IMV H78/167,C77/181; HR.89(.65,1.22); malignancy interaction P=.01 shared with S054.
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs. The figure's predefined status for this clinical subgroup is F-ST1-014.
- **PASS_2_COMPLETE:** IMV hematologic Yes HR.89 in[.65,1.22] includes 1;78≤167 and 77≤181. Interaction.01 may coexist with this null-containing subgroup interval because it tests heterogeneity. Prespecification, population and shared-reference issues already recorded.

### S056

- **Mapper provenance:** main S056.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3B all. IMV H150/388,C170/388; HR 1.17(.94,1.46).
- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.
- **PASS_2_COMPLETE:** All-patient IMV HR 1.17 in[.94,1.46] includes 1;150/388 and 170/388 match Table 2. Table 2.85 versus 1.17 precision gap.310/.85=.364706 is already F-NUM-004; reciprocal diagnostic does not identify the model/reference.

### S057

- **Mapper provenance:** main S057.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=7), p.7 Figure 3 legend/geometry. Both panels HR95% CI, log ticks.2,1,10; left Favors H, right Favors C; null 1. Marker square sides proportional subgroup sizes except open all-patient squares; bars 95% CI; Gail and Simon test. No explicit numerator-reference statement in caption beyond favors labels and H/C count columns.
- **PASS_1_COMPLETE:** REPORT Figure 3 left favors H/right favors C requires H/C event HR. IMV all-row HR 1.17 with that orientation conflicts with Table 2 H/C .85 and its lower-event direction; inverse .85≈1.176. F-ST1-001 consolidates the 26 row pattern and both panels. Individual model HRs are not expected to equal crude risk ratios.
- **PASS_2_COMPLETE:** Favors-H below 1 and favors-C above 1 remain printed for both panels. All 26 ordered 95% CIs contain their point estimates; the all-IMV contrast/reference discrepancy already F-NUM-004. Marker-size and log-axis definitions introduce no additional estimate or test conflict.

### S058

- **Mapper provenance:** main S058.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=2), pp.2,6,8 interpretations. Key Points mortality 35.6%/36.1% not significantly reduced; discussion no survival/IMV/infection/comfort/dyspnea/ICU-stay benefit; conclusion no significantly decreased day 28 mortality.
- **PASS_1_COMPLETE:** Key Points/abstract/conclusion all assert no statistically significant day 28 mortality reduction; RD and HR null-containing intervals and P=.94/.85 support that reading. This does not assert equivalence or noninferiority.
- **PASS_2_COMPLETE:** Key Points, abstract and conclusion consistently state no significant day 28 mortality reduction, supported by null-containing CIs and P=.94/.85. They claim neither equivalence nor noninferiority. No multiplicity or stopping conclusion reverses the final superiority reading.

### S059

- **Mapper provenance:** main S059.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=6), p.6 vasopressors/renal replacement and discharge. N059 combined sentence says no statistical difference; discharge standard oxygen 3 L/min says no significant difference. No P/CI printed.
- **PASS_1_COMPLETE:** No significant vasopressor/renal-replacement or discharge difference asserted, but no paired P/CI available. Printed count attribution tracked numerically through main N059; no inferred denominator/test. Different treatment populations/time windows are not reconstructed.
- **PASS_2_COMPLETE:** Therapy count/percentage/arm attribution remains already F-NUM-002; pooled 153/776 and 31/776 reproduce percentages but not the printed arm attribution. No arm-by-therapy table or test can be reconstructed. Discharge 3 L/min nonsignificance has no paired P/CI conflict.

### S060

- **Mapper provenance:** main S060.
- **Exact locations and printed relationship:** REPORT [main article](../../../jama_azoulay_2018_oi_180109.pdf#page=6), p.6 treatment limitations/day 90. N061 treatment-limit deaths no significant group difference; N062 day 90 mortality nonsignificant. No P/CI printed.
- **PASS_1_COMPLETE:** Treatment limitation count 170, deaths 135 gives 79.4118%, matching 79.4. Day 90 risks 46.9/48.2 labeled nonsignificant with no counts,P,CI or test; lack of precision alone is not a finding. It is a separate post hoc horizon, not D28 primary.
- **PASS_2_COMPLETE:** 170/776=21.907% and 135/170=79.4118% reproduce 21.9/79.4. Treatment-limit and day 90 nonsignificance have no paired printed P/CI to contradict them. Day 90 is separately labeled and not substituted for primary day 28.

# Statistical relationship inventory — completed pass-2 support part

Runtime ID: 01a129db-42fe-7702-a208-6cf2e0d12816. Exact scope: S061–S099, 39 relationships. Original assigned sections and PASS_1_COMPLETE facts preserved; one individual PASS_2_COMPLETE conclusion added to every section. Links adjusted to this part's actual four-level depth. Canonical merge belongs to the coordinator.

### S061

- **Relationship:** Initial noninferiority power/sample size.
- **Mapper provenance:** P1-S006; S-P2-013.
- **Exact locations and printed relationship:** PLAN pp.6–7,51: control mortality 26%, noninferiority margin 9%, alpha 5%, power 80%,408 per arm and 816 overall; one-sided main interval.
- **Direct source locator:** [PLAN p.6](../../../joi180109supp1_prod.pdf#page=6).
- **PASS_1_COMPLETE:** 816=2×408. The alternative-arm event rate and exact calculation routine are absent. A diagnostic equal-rate normal approximation gives about 294 per arm but assumes an unreported alternative, so no finding rests on it. The report discloses redesign; S002 covers the final superiority calculation.
- **PASS_2_COMPLETE:** The 408-per-arm/816 total reconciles. The NI alternative rate and calculation routine are not supplied; the approximate equal-rate calculation remains explicitly diagnostic and cannot identify an operative discrepancy after the disclosed superiority redesign. The final superiority calculation is S002 in the other shard; no new finding.

### S062

- **Relationship:** Planned longitudinal joint models versus reported analyses.
- **Mapper provenance:** S-P2-026 (model portion); support3:S-312; P4-20.
- **Exact locations and printed relationship:** PLAN pp.55,82,105: longitudinal oxygenation, dyspnea and comfort joint models accounting for right censoring. REPORT p.4 names Wilcoxon symptom comparisons; pp.1,6 reports oxygenation difference 19.5 [4.4,34.6].
- **Direct source locator:** [PLAN p.55](../../../joi180109supp1_prod.pdf#page=55).
- **PASS_1_COMPLETE:** A positive planned joint-model commitment is not identified in supplied results, while a different symptom procedure is named. F-ST1-005 records this planned-versus-reported analysis comparison. No preferred model is proposed; exact joint-model components and covariance are absent.
- **PASS_2_COMPLETE:** Final-plan pp.105/82 retain joint-model commitments; the report names Wilcoxon/time-specific outputs without identifying those models. Current recheck C009 preserves that Route A5 observation and absent model/result mapping. It is already screened; no new finding.

### S063

- **Relationship:** Eligibility and target population across versions.
- **Mapper provenance:** P1-S003; S-P2-006; support3:S-314; P4-05 (eligibility portion); main N003.
- **Exact locations and printed relationship:** PLAN pp.6–7,42–43 initially includes HIV and oxygen need without a numeric minimum. Final pp.90,98 specifies age≥18, oxygen≥6L/min, Pa CO2≥50mm Hg exclusion and postoperative days 1–6 exclusion. REPORT p.2 specifies AHRF and excludes AIDS.
- **Direct source locator:** [PLAN p.6](../../../joi180109supp1_prod.pdf#page=6).
- **PASS_1_COMPLETE:** Final numeric eligibility thresholds substantially agree with the report. Initial definitions belong to the disclosed redesign. HIV/AIDs wording alone does not establish a changed analyzable count; no unsupported population count is inferred.
- **PASS_2_COMPLETE:** Final ≥6 L/min, age ≥18, PaCO2 ≥50 exclusion and postoperative-day window map to the reported design. Initial HIV/no-minimum eligibility belongs to the disclosed redesign. AIDS/HIV and cancer-care/chemotherapy wording supplies no numerical population conflict; no new finding.

### S064

- **Relationship:** Randomized oxygen delivery, duration and permitted crossover.
- **Mapper provenance:** P1-S002; S-P2-007; S-P2-008; S-P2-009; P4-03; P4-07; main N005/N006.
- **Exact locations and printed relationship:** PLAN pp.6–7,32,43–45 initially specifies 40L/min minimum and weaning below 2L/min. Final pp.96,99–100 specifies 50L/min for 3 days, up to 60L/min, SpO2≥95%, PaO2/FiO2>300 and weaning below 6L/min. Final p.99 prohibits control HFNO; REPORT pp.3,5 permits rescue in DNI controls and reports 30 switches.
- **Direct source locator:** [PLAN p.6](../../../joi180109supp1_prod.pdf#page=6).
- **PASS_1_COMPLETE:** Final dose and weaning match the report. F-ST1-013 records the final control prohibition versus the reported rescue exception used in 30/388 controls. The p.100 line 1637 exception wording is immediately resolved by its paragraph and is excluded; no clinical treatment preference is proposed.
- **PASS_2_COMPLETE:** Final 50 L/min first-three-day delivery, 60 L/min ceiling, SpO2≥95%, PaO2/FiO2>300 and <6 L/min weaning agree with the report. C003 already preserves final-plan control prohibition versus reported DNI rescue in 30 controls. The p.100 exception sentence resolves within the continuous-HFNO/temporary-Venturi paragraph; no new finding.

### S065

- **Relationship:** Primary outcome time origin and event definition.
- **Mapper provenance:** P1-S004; support3:S-315; P4-11; main N010.
- **Exact locations and printed relationship:** PLAN p.6 line 96 defines mortality 28 days after ICU admission; p.7 line 141 says 28 days after randomization. Final PLAN pp.97,102 and REPORT pp.1,3,5 use day 28 after randomization.
- **Direct source locator:** [PLAN p.6](../../../joi180109supp1_prod.pdf#page=6).
- **PASS_1_COMPLETE:** The final operational definition matches the reported result. The initial bilingual time-origin difference does not identify a conflicting reported primary value after redesign. SAP 'hospital death' follows classification as alive/dead at day 28; terminology is recorded in the excluded table.
- **PASS_2_COMPLETE:** Final day-28 randomization origin agrees with report results. Initial admission/randomization wording is superseded by the identified final rule; hospital-death language immediately follows binary alive/dead day-28 classification. No changed operative endpoint or new numerical conflict is supplied.

### S066

- **Relationship:** Initial noninferiority margin, confidence-bound geometry and criterion.
- **Mapper provenance:** S-P2-002; S-P2-004; S-P2-011 (decision portion).
- **Exact locations and printed relationship:** PLAN pp.39–41 Figure 4: efficacy new minus control, lower one-sided bound right of negative margin demonstrates noninferiority. PLAN p.42 says lower 95% CI boundary less than 9%; p.51 gives one-sided interval and margin 9%.
- **Direct source locator:** [PLAN p.39](../../../joi180109supp1_prod.pdf#page=39).
- **PASS_1_COMPLETE:** The literal criterion differs from the signed generic illustration. It belongs to the expressly superseded NI design and is not applied to a reported superiority result; excluded OUT_OF_FOCUS. No NI conclusion is inferred from the report's superiority confidence intervals.
- **PASS_2_COMPLETE:** The early lower-bound wording and generic signed NI illustration were reread without mapping a superiority CI to an NI decision. No reported NI conclusion relies on that superseded criterion. The final superiority and interim rules are separately identified; no new finding.

### S067

- **Relationship:** Randomization strata, unit, and subgroup boundaries.
- **Mapper provenance:** S-P2-010 (strata portion); S-P2-012; P4-06 (randomization portion); main N004; main S009.
- **Exact locations and printed relationship:** PLAN p.50 describes patient allocation but calls the randomization unit the centre. Final pp.98–99: ICU days 0–2/≥3, oxygen<9/≥9L/min, catecholamines, eight lists. REPORT p.2: days≤2/≥3, oxygen≤9/>9; Figure 3 time rows 0–1/≥2.
- **Direct source locator:** [PLAN p.50](../../../joi180109supp1_prod.pdf#page=50).
- **PASS_1_COMPLETE:** Patient allocation resolves the centre wording; no cluster model is inferred. Three binary strata produce 2^3=8 lists. Final-plan/report oxygen boundaries and report-internal time boundaries change subgroup membership: F-ST1-007.
- **PASS_2_COMPLETE:** Final three binary strata reproduce eight lists (2^3=8); individual patient allocation resolves the centre-unit phrase. C002 already records final-plan/report oxygen inequality and report-internal ICU-day subgroup boundaries; C015 covers unexplained available subgroup populations. Early two-factor/eight-list prose is superseded and does not establish a conflicting operative allocation rule; no new finding.

### S068

- **Relationship:** Planned primary per-protocol analysis.
- **Mapper provenance:** S-P2-017; P4-15 (PP portion).
- **Exact locations and printed relationship:** PLAN p.53 initially requires PP alongside ITT for noninferiority. Final p.104 line 1723 retains a per-protocol analysis. REPORT pp.3–8 and results supplement identify no primary PP population or result.
- **Direct source locator:** [PLAN p.53](../../../joi180109supp1_prod.pdf#page=53).
- **PASS_1_COMPLETE:** The positive retained final primary-analysis commitment is absent from the results: F-ST1-003. Missing PP membership rules alone are not a separate finding. Superiority redesign does not remove the retained final-plan sentence.
- **PASS_2_COMPLETE:** The final p.104 PP commitment remains positive despite redesign, while no supplied primary PP result/population is identified. This is already screened within consolidated C005 and directly rechecked. Missing PP membership rules are retained as a human input, not a separate finding.

### S069

- **Relationship:** Missing outcomes and predictors.
- **Mapper provenance:** S-P2-020; S-P2-021; P4-16.
- **Exact locations and printed relationship:** PLAN pp.53–54,104 specifies contingent time-to-event handling for missing primary outcomes and multiple imputation for missing predictors. REPORT pp.3,5 has no loss to follow-up and excludes consent withdrawals.
- **Direct source locator:** [PLAN p.53](../../../joi180109supp1_prod.pdf#page=53).
- **PASS_1_COMPLETE:** Zero loss leaves the primary missing-data contingency untriggered. Predictor imputation models, imputation count and the named competing event are absent; missing detail alone is not a finding. Available secondary measurements are not equated to the primary population.
- **PASS_2_COMPLETE:** The article supplies zero loss and consent-withdrawal exclusions; no demonstrated missing primary outcome triggers the contingent time-to-event rule. Predictor imputation count/models and secondary measurement availability are not supplied, but there is no conflicting implemented imputation claim. No new finding.

### S070

- **Relationship:** Outcome statuses, measures and secondary endpoint dictionary.
- **Mapper provenance:** P1-S005; S-P2-003; support3:S-316; P4-12 (endpoint portion); main N010/S026.
- **Exact locations and printed relationship:** Initial PLAN pp.6–7,38,46–47 lists infiltrate clearance, oxygen/ventilation-free survival, reintubation, intubation SpO2, post-intubation mortality, DNI analyses and satisfaction as secondary. Final pp.90,103 lists intubation, comfort VAS, dyspnea VAS/Borg, rate, oxygenation days 1–3, ICU stay and infection. REPORT pp.4,6 calls intubated analyses post hoc and supplies VAS dyspnea.
- **Direct source locator:** [PLAN p.6](../../../joi180109supp1_prod.pdf#page=6).
- **PASS_1_COMPLETE:** The prospective-secondary versus reported-post-hoc status is F-ST1-008, with redesign preserved as an alternative. The final Borg measure is absent: F-ST1-012. Removed initial non-key measures are not assumed to retain operational status after redesign.
- **PASS_2_COMPLETE:** C011 already preserves earlier secondary intubated-mortality versus reported post hoc status, including the redesign/final-list alternative. C004 preserves retained final Borg/lowest-SpO2 components without supplied results. Removed initial non-key measurements are not a claim of retained operational analysis; no new finding.

### S071

- **Relationship:** Participation, followup and withdrawal data use.
- **Mapper provenance:** support3:S-304; support3:S-306; support3:S-305 (consent portion).
- **Exact locations and printed relationship:** PLAN pp.72,74,79–80 specifies 30 months of research,6 months of participation and participant permission for previously collected data after withdrawal. REPORT outcomes include day 28 and post hoc day 90 mortality.
- **Direct source locator:** [PLAN p.72](../../../joi180109supp1_prod.pdf#page=72).
- **PASS_1_COMPLETE:** Participation is not randomized oxygen exposure. A day 28 primary endpoint can coexist with longer follow-up. Consent/data-use permissions reconcile S004 exclusions; no additional conflicting count is derived.
- **PASS_2_COMPLETE:** Consent distinguishes cessation from permission to reuse collected data; consent-withdrawal exclusions map to the reported set. Six-month participation and day-28/day-90 follow-up do not redefine randomized oxygen exposure. No additional numerator, denominator or test conflict arises.

### S072

- **Relationship:** Operational ascertainment and safety definitions.
- **Mapper provenance:** S-P2-027; S-P2-028; S-P2-029; S-P2-030; N-P2-004.
- **Exact locations and printed relationship:** PLAN pp.56–57 defines weekday capture, weekend arrangements and consent/assigned treatment delivery. PLAN pp.59–61 defines adverse events, seriousness, relatedness and reporting within 5 working days,24 hours for selected deaths and 7/15 calendar days for coordinating reports.
- **Direct source locator:** [PLAN p.56](../../../joi180109supp1_prod.pdf#page=56).
- **PASS_1_COMPLETE:** Operational ascertainment and safety rules contain no reported conflicting efficacy test or number. Administrative timelines are outside statistical-design focus. All units remain mapped without inventing a primary/key safety analysis.
- **PASS_2_COMPLETE:** Weekday/weekend ascertainment and 5-working-day/24-hour/7-calendar-day/15-calendar-day safety timelines concern distinct reporting steps. No supplied efficacy test, key safety-analysis result or operative statistical decision contradicts them. Scheduled safety review is not equated to the final efficacy interim boundary; no new finding.

### S073

- **Relationship:** Primary intervention label in plan analysis prose.
- **Mapper provenance:** S-P2-015 (NIV hypothesis portion); P4-15 (NIV hypothesis portion).
- **Exact locations and printed relationship:** PLAN p.52 names noninferiority of NIV; p.104 names superiority of NIV while surrounding methods consistently specify HFNO versus oxygen.
- **Direct source locator:** [PLAN p.52](../../../joi180109supp1_prod.pdf#page=52).
- **PASS_1_COMPLETE:** The intended intervention is immediately identifiable from the same paragraphs. Excluded TERMINOLOGY_OR_WORDING; no separate randomized NIV arm or changed numerical effect is inferred.
- **PASS_2_COMPLETE:** Both NIV hypothesis occurrences sit within explicit HFNO-versus-standard objectives and allocation descriptions. No printed estimate, arm count, reference group or effect extraction depends on interpreting a separate NIV randomized arm. Terminology alone does not establish Route A2; no new finding.

### S074

- **Relationship:** Original subgroup populations and decision condition.
- **Mapper provenance:** S-P2-010 (unstratified subset portion); S-P2-016; S-P2-023.
- **Exact locations and printed relationship:** PLAN pp.45–46 defines intubation, post-extubation, intubated-in-either-arm and DNI subsets with ICU mortality interaction wording. PLAN pp.53–54,104 specifies primary-endpoint Gail–Simon interactions and subset analyses after significant interaction.
- **Direct source locator:** [PLAN p.45](../../../joi180109supp1_prod.pdf#page=45).
- **PASS_1_COMPLETE:** Initial subgroup definitions remain preserved. Intubated-result status is F-ST1-008. Conditional inferential subset analyses do not forbid descriptive forest rows. Exact interaction statistics and covariance are absent; no preferred test is proposed.
- **PASS_2_COMPLETE:** Earlier subset descriptions and final Gail–Simon conditional analyses were reread. C011 preserves the intubated-analysis status change and C016 preserves positive predefined claims lacking supplied prospective mappings. Forest descriptive rows need not be conditional inferential subset analyses. Missing statistics/covariance are not inferred; no new finding.

### S075

- **Relationship:** ICU-acquired infection definition.
- **Mapper provenance:** P4-09; main S007/S016.
- **Exact locations and printed relationship:** PLAN p.101 lines 1654–1656 defines new infection more than 48 hours after ICU admission, new antibiotics and CDC definitions. REPORT Table 2 has 39/41 infections.
- **Direct source locator:** [PLAN p.101](../../../joi180109supp1_prod.pdf#page=101).
- **PASS_1_COMPLETE:** No different explicit report definition is supplied. An omitted repeated definition alone is not a discrepancy. Test framework and HR interval are examined at S007/S016.
- **PASS_2_COMPLETE:** The final infection definition supplies >48 hours after ICU admission, new antibiotics and CDC criteria; no different explicit report definition is stated. C006 preserves planned/report infection methods, and C013 preserves the nonreproducing same-display interval diagnostic. No additional definition conflict is established.

### S076

- **Relationship:** Outcome collection and measurement windows.
- **Mapper provenance:** P4-08; main N011.
- **Exact locations and printed relationship:** PLAN pp.100–101 specifies T0, worst physiological values and day 28 mortality, intubation, ICU/hospital stay and infection collection. REPORT p.3 gives comfort/dyspnea 0–10 scales; supplement table is at 6 hours and figures through day 7.
- **Direct source locator:** [PLAN p.100](../../../joi180109supp1_prod.pdf#page=100).
- **PASS_1_COMPLETE:** Hospital-stay collection does not by itself designate a separate key analysis. Undefined point summaries/bars are not assumed means, standard errors or confidence intervals. Repeated displays are checked at S080–S083.
- **PASS_2_COMPLETE:** Collection of worst physiological values and ICU/hospital outcomes does not independently specify an absent key hospital-stay analysis. Time origins and key oxygenation attribution are already C001. Figure summary/bar conventions remain undefined; no precise mean, median, standard error or CI is invented.

### S077

- **Relationship:** Prospective intubation predictor analysis.
- **Mapper provenance:** P4-22 (predictor portion).
- **Exact locations and printed relationship:** PLAN p.107 states an intention to analyze intubation predictors. REPORT gives intubation subgroups without an identified multivariable predictor model.
- **Direct source locator:** [PLAN p.107](../../../joi180109supp1_prod.pdf#page=107).
- **PASS_1_COMPLETE:** An exploratory intention without a primary/key model specification is not treated as an unreported primary/key analysis. No conflicting claim of prespecified predictor analysis appears. Missing optional exploratory output alone is not emitted.
- **PASS_2_COMPLETE:** The p.107 expectation to examine intubation predictors supplies no prespecified primary/key-secondary predictor model or positive claim that the reported subgroups are that model. A missing exploratory output alone is outside Route A5; no new finding.

### S078

- **Relationship:** Six-hour descriptive physiology and ventilation table.
- **Mapper provenance:** R4-02; main S021/S022/S023; main N056.
- **Exact locations and printed relationship:** REPORT supplement 2 p.2:388 per arm, IMV39(10.0%)/46(11.8%), non-intubated HFNO349(100%), standard oxygen 342(88.2%), NIV0/0. Medians: rate 25[20–30]/26[21–31], PaO2/FiO2 150[104–230]/119[86–165], flow 50[50–60]/8[6–15], HFNO FiO2 70[60–90].
- **Direct source locator:** [REPORT p.2](../../../joi180109supp2_prod.pdf#page=2).
- **PASS_1_COMPLETE:** 349=388−39 and 342=388−46; the 100% is 349/349 in the explicitly conditional non-intubated row. IQRs contain medians. Main medians match without equating their differences to mean contrasts. No P/CI printed here; window attribution is F-ST1-009.
- **PASS_2_COMPLETE:** At H6, 39+349=388 and 46+342=388; 349(100%) explicitly conditions on non-intubated high-flow recipients. Count percentages overlap their half-unit recomputations. All medians lie within ordered IQRs. No printed P/CI is attached; the time-origin question is C001, not a new finding.

### S079

- **Relationship:** Cumulative ventilation figure test identity.
- **Mapper provenance:** R4-03; main S006/S015.
- **Exact locations and printed relationship:** REPORT supplement 2 p.3 e Figure 1 labels cumulative mechanical-ventilation comparison log-rank P=.17. Main pp.3–4 names Gray comparison; Table 2/p.6 also gives P=.17.
- **Direct source locator:** [REPORT p.3](../../../joi180109supp2_prod.pdf#page=3).
- **PASS_1_COMPLETE:** The named procedures differ even when rounded P values agree. F-ST1-010 asks which generated the figure comparison. No interval/P significance conflict is asserted. Approximate curves and risk sets do not supply fitted event-time inputs.
- **PASS_2_COMPLETE:** Both printed .17 copies overlap [.165,.175]; distinct Gray/log-rank procedure labels remain C007, while final-plan competitor/adjustment mapping remains C006. Raw risk sets, exact events and variance are absent; no new interval/P conflict is inferred.

### S080

- **Relationship:** Respiratory-rate repeated display.
- **Mapper provenance:** R4-04; main S021/S022.
- **Exact locations and printed relationship:** REPORT supplement 2 p.4 e Figure 2A displays randomization,H6,days 1–7 and an H6 star. Paired counts:388/388 at baseline/H6/D1;346/345 D2–3;291/275 D4;257/237 D5;217/206 D6;196/169 D7.
- **Direct source locator:** [REPORT p.4](../../../joi180109supp2_prod.pdf#page=4).
- **PASS_1_COMPLETE:** Lower H6 HFNO direction matches the main negative confidence interval and significant statement. Undefined bars/star conventions prevent exact reconstruction; absence alone is not a finding. Counts need not equal primary N; planned joint models are S062.
- **PASS_2_COMPLETE:** The figure has an H6 star and lower high-flow rate, consistent with the negative main interval. Individual observation counts are not necessarily analysis-population counts. Undefined point/bar/star conventions prevent exact P/CI reconstruction; C009 covers joint-model mapping and C001 covers attribution; no new finding.

### S081

- **Relationship:** Oxygenation repeated display.
- **Mapper provenance:** R4-05; main S023.
- **Exact locations and printed relationship:** REPORT supplement 2 p.4 e Figure 2B has double stars at H6,D1–D3. Counts:318/311 H6;388/388 D1;293/210 D2–3;193/141 D4;158/129 D5;138/112 D6;126/96 D7.
- **Direct source locator:** [REPORT p.4](../../../joi180109supp2_prod.pdf#page=4).
- **PASS_1_COMPLETE:** Approximate higher HFNO oxygenation through day 4 matches the main positive interval. No bar confidence level or symbol threshold is supplied. 'Until day 4' versus star placement is not a reproduced numeric/test conflict without a symbol convention.
- **PASS_2_COMPLETE:** The higher early high-flow oxygenation direction agrees with 19.5 [4.4,34.6]. Double-star meaning and bar confidence level are not defined; day-4 wording versus star placement is not a reproduced interval/test conflict. C001/C004/C009 retain time, measurement and method implications; no new finding.

### S082

- **Relationship:** Comfort repeated display.
- **Mapper provenance:** R4-06; main S024.
- **Exact locations and printed relationship:** REPORT supplement 2 p.5 e Figure 3A comfort VAS counts:388/388 baseline;321/314 H6;298/276 D1;174/178 D2–3;126/113 D4;99/95 D5;81/70 D6;63/49 D7.
- **Direct source locator:** [REPORT p.5](../../../joi180109supp2_prod.pdf#page=5).
- **PASS_1_COMPLETE:** Approximate scores remain within 0–10. Different daily directions do not contradict reported nonsignificance. Undefined bars are not 95% between-group intervals. Joint models are S062; causes of lower observation counts are not inferred.
- **PASS_2_COMPLETE:** Comfort points remain on the 0–10 scale. Visual separation of undefined arm-summary bars cannot determine a Wilcoxon or between-group significance conflict. Time-specific contributor declines do not contradict primary follow-up. C009 retains the prospective joint-model issue; no new finding.

### S083

- **Relationship:** Dyspnea repeated display.
- **Mapper provenance:** R4-07; main S024.
- **Exact locations and printed relationship:** REPORT supplement 2 p.5 e Figure 3B dyspnea VAS counts:388/388 baseline;309/289 H6;218/224 D1;156/152 D2–3;117/96 D4;89/83 D5;76/63 D6;61/47 D7.
- **Direct source locator:** [REPORT p.5](../../../joi180109supp2_prod.pdf#page=5).
- **PASS_1_COMPLETE:** Scores remain within 0–10; no P or between-group interval permits exact significance reconstruction. No Borg panel/result is supplied, F-ST1-012. Joint models are S062.
- **PASS_2_COMPLETE:** Dyspnea VAS points remain on the 0–10 scale, with no exact P or defined between-group interval printed. Undefined bars cannot be read as 95% effect intervals. C004/C009 already retain Borg-result and joint-model implications; no new finding.

### S084

- **Relationship:** Bundle identity and design-change disclosures.
- **Mapper provenance:** P1-N001; main S001; P4-04.
- **Exact locations and printed relationship:** PLAN p.1 lists protocol/SAP versions and no amendment except added centres. REPORT p.3 discloses grant-stage conversion to superiority and different secondary outcomes.
- **Direct source locator:** [PLAN p.1](../../../joi180109supp1_prod.pdf#page=1).
- **PASS_1_COMPLETE:** Grant-stage revision explains initial/final design occurrences. Amendment wording may refer to formal post-approval changes; wording alone is not emitted. Explicit retained primary/key analysis commitments remain checked at S005,S062,S068,S070.
- **PASS_2_COMPLETE:** Source cover no-amendment language was read with the report's explicit grant-stage NI-to-superiority and secondary-endpoint revision. Formal-version nomenclature alone does not contradict a printed result or operative decision. Retained final commitments remain C004–C006/C009–C010; no new finding.

### S085

- **Relationship:** Historical early-versus-late intubation cohort.
- **Mapper provenance:** P1-N008; P1-N010(ref 42); P4-27(ref 42).
- **Exact locations and printed relationship:** PLAN pp.20,22,127–128: historical 175-person early/late intubation cohort, mortality 39.2%/66.7%,P=.001; extubation 37.7%/15.6%,P=.006.
- **Direct source locator:** [PLAN p.20](../../../joi180109supp1_prod.pdf#page=20).
- **PASS_1_COMPLETE:** Directions agree with narrative. No arm sizes, CI, standard errors or identified test/sidedness allow exact reproduction. Historical rationale is not a HIGH result; clipped later text adds no complete independent value.
- **PASS_2_COMPLETE:** Earlier mortality 39.2%/66.7% and extubation 37.7%/15.6% agree with stated historical directions and significant P=.001/.006. No arm sizes, CI, standard error, test or sidedness permit reconstruction. Clipped historical copies add no exact independent HIGH result; no new finding.

### S086

- **Relationship:** Historical FLORALI results.
- **Mapper provenance:** P1-N009; P1-N010(ref 13); P4-01; P4-27(ref 13).
- **Exact locations and printed relationship:** PLAN pp.21–22,95,128: historical FLORALI310 patients, intubation 38%/47%/50%; immunocompromised subset 8/26(31%),13/30(43%),17/26(65%),P=.04; HFNO/standard pair described as nonsignificant.
- **Direct source locator:** [PLAN p.21](../../../joi180109supp1_prod.pdf#page=21).
- **PASS_1_COMPLETE:** Count percentages round correctly. A significant three-arm comparison can coexist with a nonsignificant pair; exact test mapping/intervals are absent. No HIGH comparison is substituted.
- **PASS_2_COMPLETE:** Historical 8/26,13/30,17/26 reproduce rounded 31%,43%,65% after half-unit precision. An overall three-arm P=.04 can coexist with a nonsignificant named pair. No interval/test conflict or HIGH treatment-effect mapping is reproduced.

### S087

- **Relationship:** Other historical clinical-study rows.
- **Mapper provenance:** P1-N010 (remaining 10 rows); P4-27 (remainingrows).
- **Exact locations and printed relationship:** PLAN pp.22,127–128: remaining historical Table 4 rows N38,20,60,20,20,45,172,17,40;9/20(45%) success,40% intubation, NIV need 30% to 10%, ventilation 100% to 63%,P<.01.
- **Direct source locator:** [PLAN p.22](../../../joi180109supp1_prod.pdf#page=22).
- **PASS_1_COMPLETE:** Printed count relationships reconcile. Other directions lack CI/test inputs. Historical definitions are not applied to HIGH; right-edge clipping remains a source limitation.
- **PASS_2_COMPLETE:** Historical printed 9/20=45% and cohort quantities reconcile; other verbal/directional results lack precise interval/test inputs. Historical reference rows are not current trial outcomes or decision rules. Right-edge clipping limits those copies only; no new finding.

### S088

- **Relationship:** Historical surgery noninferiority.
- **Mapper provenance:** P1-N011; P1-N012(ref 14).
- **Exact locations and printed relationship:** PLAN pp.23–24: historical 830-person HFNO/Bi PAP noninferiority after surgery; skin breakdown higher with Bi PAP, no ICU mortality difference.
- **Direct source locator:** [PLAN p.23](../../../joi180109supp1_prod.pdf#page=23).
- **PASS_1_COMPLETE:** No margin, CI or computational method is supplied for the historical NI conclusion. It cannot be reproduced from the summary and is not an operational HIGH rule. Missing historical detail alone is not a finding.
- **PASS_2_COMPLETE:** The historical 830-person surgery NI summary supplies no margin, interval, statistic or decision calculation. Its missing detail alone does not establish an operative HIGH inconsistency or Route A finding; no new finding.

### S089

- **Relationship:** Historical extubation and preoxygenation studies.
- **Mapper provenance:** P1-N011; P1-N012 (remainingrows).
- **Exact locations and printed relationship:** PLAN pp.23–24: historical studies N20,105,340,50,17,155,67,101,124; lowest SpO291.5%/89.5%,P=.44;101-person before/after lowest 100%/94%.
- **Direct source locator:** [PLAN p.23](../../../joi180109supp1_prod.pdf#page=23).
- **PASS_1_COMPLETE:** No test identity, CI, standard error or paired covariance is supplied. P=.44 does not conflict with a descriptive difference without those inputs. Historical clinical/eligibility wording does not identify a reported HIGH discrepancy.
- **PASS_2_COMPLETE:** Historical 91.5%/89.5%,P=.44 lacks identified test/CI/standard error/paired covariance; a descriptive difference alone cannot reproduce a test conflict. The before/after label discrepancy is peripheral historical attribution with no HIGH key-result mapping; no new finding.

### S090

- **Relationship:** Historical 45-person hematologic cohort.
- **Mapper provenance:** P1-N014; N303.
- **Exact locations and printed relationship:** PLAN pp.27,93: historical 45-person cohort,15/45 recovered(33%); deaths 2/15(13.3% or 13%) and 26/30(86.7% or 87%).
- **Direct source locator:** [PLAN p.27](../../../joi180109supp1_prod.pdf#page=27).
- **PASS_1_COMPLETE:** 15+30=45 and printed percentages round correctly. Failure-group mortality direction agrees. No hospital-effect CI/test is supplied; not a HIGH randomized result.
- **PASS_2_COMPLETE:** Historical 15+30=45,15/45≈33%,2/15≈13.3%,26/30≈86.7%; both rounded copies overlap recomputed input intervals. The mortality direction agrees. No interval/test conflict or current-trial denominator is supplied.

### S091

- **Relationship:** Historical solid-tumor HFNO cohort.
- **Mapper provenance:** P1-N014; N304.
- **Exact locations and printed relationship:** PLAN pp.27,93:132/183(72%) historical solid-tumor HFNO patients;41% improved,44% stable,15% declined.
- **Direct source locator:** [PLAN p.27](../../../joi180109supp1_prod.pdf#page=27).
- **PASS_1_COMPLETE:** 132/183=72.131%;41+44+15=100%. Category counts and effect intervals are absent; no integer events are invented from rounded percentages.
- **PASS_2_COMPLETE:** Historical 132/183≈72.131% overlaps the 72% display interval, and 41+44+15=100%. Exact category counts and effect intervals are absent; no events are reverse-engineered from these rounded fractions. No new finding.

### S092

- **Relationship:** Historical 30-patient physiologic randomized study.
- **Mapper provenance:** P1-N014; N305.
- **Exact locations and printed relationship:** PLAN pp.27–28,93–94: historical 30-person advanced-cancer HFNO/Bi PAP2 hour study, similar VAS/Borg response, nonsignificant rate reduction and oxygenation improvement only with HFNO.
- **Direct source locator:** [PLAN p.27](../../../joi180109supp1_prod.pdf#page=27).
- **PASS_1_COMPLETE:** No changes, CIs, P values or standard errors are supplied. These verbal historical observations do not establish a conflicting current model or result.
- **PASS_2_COMPLETE:** Historical 30-person two-hour physiologic descriptions contain no printed change, CI, test statistic, standard error or P. Similar symptom response and an oxygenation direction for one arm supply no current-trial numerical contradiction; no new finding.

### S093

- **Relationship:** Historical lung-transplant intubation ARR/NNT.
- **Mapper provenance:** P1-N014; N306.
- **Exact locations and printed relationship:** PLAN pp.28,94: historical 37 lung-transplant recipients, ARR29.8% or 29%, NNT3.
- **Direct source locator:** [PLAN p.28](../../../joi180109supp1_prod.pdf#page=28).
- **PASS_1_COMPLETE:** Diagnostic reciprocals 1/.298=3.356 and 1/.29=3.448 lie in NNT3 half-unit interval[2.5,3.5]. ARR-copy relative gap.25/29.8=.00839≤.05. No reproduced result-changing gap.
- **PASS_2_COMPLETE:** Diagnostic reciprocal intervals from ARR29.8±.05% are approximately [3.3501,3.3613], and from ARR29±.5% [3.3898,3.5088]; each intersects NNT3±.5. ARR-copy half-unit gap .25/29.8=.00839≤.05. No reproduced numeric discrepancy.

### S094

- **Relationship:** Historical 50-person DNI cohort.
- **Mapper provenance:** P1-N014; N307.
- **Exact locations and printed relationship:** PLAN pp.28,94:50 historical DNI patients, approximately one third immunocompromised, with improved oxygenation and rate.
- **Direct source locator:** [PLAN p.28](../../../joi180109supp1_prod.pdf#page=28).
- **PASS_1_COMPLETE:** Approximate population fraction does not provide exact events or intervals. Background response is not a HIGH treatment effect. No subgroup count/test is inferred.
- **PASS_2_COMPLETE:** The historical 50-person DNI cohort and approximate one-third fraction supply no exact subgroup event/count/test. They do not map to a HIGH randomized effect, decision margin or analysis-set count; no new finding.

### S095

- **Relationship:** Historical 178-person retrospective propensity study.
- **Mapper provenance:** P1-N015; N308.
- **Exact locations and printed relationship:** PLAN pp.29,94:178 historical patients,76(43%) NIV+HFNO,74(42%) NIV+oxygen,20(11%) HFNO alone,8 oxygen alone; mortality 37%/52%,P=.04; separate propensity narrative says lower day 28 survival.
- **Direct source locator:** [PLAN p.29](../../../joi180109supp1_prod.pdf#page=29).
- **PASS_1_COMPLETE:** Counts total 178 and percentages round. Unadjusted and separate adjusted directions may differ; no adjusted coefficient/CI reproduces a conflict. Historical wording is peripheral to a reported HIGH result.
- **PASS_2_COMPLETE:** Historical treatment counts 76+74+20+8=178 and printed percentages reconcile. The crude lower-mortality and separate propensity lower-survival statements need not share an estimand or direction; no adjusted coefficient/CI is printed. No HIGH primary/key comparison is changed; no new finding.

### S096

- **Relationship:** Historical i VNIctus/374-person HFNO analyses.
- **Mapper provenance:** P1-N015; P1-N016; P1-N017; N308.
- **Exact locations and printed relationship:** PLAN pp.29–31,94: historical 374 participants,191/183 arms; deaths 46(24.1%)/50(27.3%),P=.47; failures 73(38.2%)/82(44.8%),P=.20;141/374(38%) HFNO. Figure groups 78,24,89,42,28,53,18,42.
- **Direct source locator:** [PLAN p.29](../../../joi180109supp1_prod.pdf#page=29).
- **PASS_1_COMPLETE:** Arms total 374; event fractions round, including 155/374=41.4%. Groups total 374 and HFNO groups 28+53+18+42=141. P values agree with verbal nonsignificance; exact tests/covariance absent. Bar heights are not exact events.
- **PASS_2_COMPLETE:** Historical 191+183=374; deaths/failures and 141/374≈38% overlap printed percentage intervals. Eight figure group sizes total374 and HFNO groups total141. P=.47/.20 agree with nonsignificance; exact tests/covariances and bar-event values are absent. No new finding.

### S097

- **Relationship:** Historical 115-person HFNO/NIV cohort.
- **Mapper provenance:** N309.
- **Exact locations and printed relationship:** PLAN p.94:115 historical patients,60(52%) HFNO/55(48%) NIV; NIV between-session HFNO 30(55%)/oxygen 25(45%). Intubation 55%/35%,P=.04; mortality 40%/20%,P=.02.
- **Direct source locator:** [PLAN p.94](../../../joi180109supp1_prod.pdf#page=94).
- **PASS_1_COMPLETE:** 60+55=115;30+25=55; percentages round. Higher NIV risks agree with narrative and significant P values. No adjusted coefficient/CI is supplied; no modeled effect is equated to crude risk.
- **PASS_2_COMPLETE:** Historical 60+55=115 and 30+25=55; all printed group percentages reconcile. NIV intubation55%/35% and mortality40%/20% directions agree with the prose and significant P values. No model-based estimate is replaced by a crude ratio; no new finding.

### S098

- **Relationship:** Background device/scales and rationale definitions.
- **Mapper provenance:** P1-N002–P1-N007; P1-N013; N302; P4-21; P4-24; P4-25; P4-26.
- **Exact locations and printed relationship:** PLAN pp.6,9–19,25–26,92,106,122–126: background device/measurement definitions, historical mortality 60%/40% and positive pressure up to 8 cmH2O.
- **Direct source locator:** [PLAN p.6](../../../joi180109supp1_prod.pdf#page=6).
- **PASS_1_COMPLETE:** Generic capacities are not HIGH assigned doses. Relevant measurement definitions link to S064/S076. No additional HIGH inferential result or operational decision rule is supplied.
- **PASS_2_COMPLETE:** Device capacities and historical mortality/pressure rationale are distinguished from assigned final interventions and current outcome effects. Outcome-scale definitions map to S064/S076. No additional operative sample-size input, inferential result or stopping rule is supplied; no new finding.

### S099

- **Relationship:** Administrative/no-applicable supporting records.
- **Mapper provenance:** N-P2-001–N-P2-003; N301; P4-23; R4-01; R4-08.
- **Exact locations and printed relationship:** PLAN pp.33–37,47,56,73,109: site/capture/provenance and 10 mL diagnostic tube. REPORT supplement covers identify the study; DOC004 p.1 states retrospective data availability.
- **Direct source locator:** [REPORT p.1](../../../joi180109supp3_prod.pdf#page=1).
- **PASS_1_COMPLETE:** No additional effect, test, primary/key analysis or prospective statistical decision rule is supplied. All inspected units remain covered. The data-sharing statement is REPORT by content. Administrative site/calendars are not used to infer a primary analysis-population change.
- **PASS_2_COMPLETE:** Administrative sites/calendars, capture details and 10mL sampling do not change primary/key results, analysis-population size or operative decision rules. The retrospective data-sharing statement is REPORT by content and contains no statistical plan. No additional inferential relationship is supplied.


