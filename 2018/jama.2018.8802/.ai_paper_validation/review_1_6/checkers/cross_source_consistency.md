# Complete cross-source consistency review

Status: COMPLETE. Fresh role qc16_cross_source_consistency_reviewer, gpt-6.1-sol/medium, runtime task /root/cross_checker. Scope: all matched quantitative results and definitions in DOC-001 main article (REPORT, 10 pages), DOC-002 protocol/SAP (PLAN, 25 pages), and DOC-003 results supplement (REPORT, 9 pages). Read current complete main/support maps, normative scope, performance profile, review contract, report specification/settings, and tooling record. No old candidate, classification, checker, or final report was read. No source/reused asset was changed. No external evidence, Python extraction, packages, OCR or GPU was used.

Tools: source-matched reusable Poppler layout text and current maps; direct Poppler 25.03.0 `pdftotext -layout` confirmation of DOC-001 pp3–8, DOC-002 pp15–16, DOC-003 pp2–3,5. Direct source PDF locations below are authority. This artifact uses local cross-review keys X01–X73 and finding labels F-A–F-I, not stable candidate IDs. Quantities within one row are bundled matched-result relationships; every component is assessed. There are 73 coverage groups and 9 distinct preliminary candidates; no count limit was applied.

## Comparison rules and complete coverage

For every row, compare population/phase, time origin and horizon, intervention-control reference, model/adjustment, measure, scale/unit and displayed precision before comparing values. REPORT eTable2 partitions the 4800 randomized patients by mRS availability, not randomization; baseline survey is a different phase. Primary versus sensitivity eligible populations differ. Absolute differences are adjusted percentage-point effects, not necessarily raw subtraction; ORPA, OR and HR are not interchangeable. Individual event totals do not partition composite patient totals because patients may experience multiple types. Vascular death is not all-cause mortality. Curve risk sets are censoring/event-dependent, not the number who completed telephone follow-up.

In coverage rows M refers to DOC-001, P to DOC-002, R to DOC-003; these indicate REPORT/PLAN/REPORT respectively. All page numbers are physical PDF pages. Complete linked evidence for each finding follows the table. Source-linked maps contain all scalar transcriptions referenced here.

| Key | Matched locations and facts | Comparison outcome |
|---|---|---|
| X01 | M 1–6; P 4,7: 40 clusters, 20/20, 1:1, 4800 patients, 2400/2400 | Reconciled; replaced 3 hospitals still leaves 40 randomized, no excluded randomized cluster |
| X02 | M 1,4,6: women 1757/4800; men 1553+1490 | Reconciled:4800−3043=1757,36.6% |
| X03 | M 1,4,5:3980,2003+1977,397+423 losses,83.5%/82.4%,82.9% | Reconciled as 12-month follow-up, separately from primary analysis |
| X04 | M 4 primary 4800; M 5 Figure 1 primary 2003/1977; M 7 Table 2 denominator 2400/2400 | F-A |
| X05 | M 4,6 hospital proportions 72.5%,62.5%,62.5% and beds 77(61–178) | Reconciled; "annual number of beds" wording has no conflicting printed value |
| X06 | M 1,4 meanage 65; M 6 medianage 65/64 | Different summary statistic, no inconsistency established |
| X07 | M 6 survey 40 hospitals/801patients; R 2 20patients/cluster | F-B |
| X08 | M 4/P 17 baseline composite 80%; R 2 80.2%/79.5% | Reconciled as rounded premise; pooled/mean aggregation definition separately F-F |
| X09 | R 2 rtPA 22.6/13.0 versus M 7 formal 21.7/11.3 | Different phase, no matched-result conflict |
| X10 | R 2 antithrombotic 95.4/88.4 versus M 7 98.0/96.7 | Different phase |
| X11 | R 2 dysphagia 79.6/88.1 versus M 7 96.9/95.4 | Different phase |
| X12 | R 2 DVT 14.4/7.8 versus M 7 27.6/11.1 | Different phase |
| X13 | R 2 dischargeantithrombotic 91.6/91.6 versus M 7 97.8/92.9 | Different phase |
| X14 | R 2 AF 14.8/28.2 versus M 7 40.6/28.5 | Different phase |
| X15 | R 2 lipid 66.9/64.6 versus M 7 95.5/93.0 | Different phase |
| X16 | R 2 hypertension 69.4/71.2 versus M 7 82.2/77.5 | Different phase |
| X17 | R 2 diabetes 83.2/78.2 versus M 7 89.7/84.0 | Different phase |
| X18 | M 6 arm 2400+2400; R 5 availability 3949+851 | Reconciled 4800; supplies partition identity used below |
| X19 | M 6 males 1553+1490; R 5 2497+546 | Reconciled 3043 |
| X20 | M 6 ischemicstroke 666+722; R 5 1137+251 | Reconciled 1388 |
| X21 | M 6 diabetes 577+509; R 5 890+196 | Reconciled 1086 |
| X22 | M 6 hypertension 1550+1540; R 5 2552+538 | Reconciled 3090 |
| X23 | M 6 dyslipidemia 305+291; R 5 285+62 | F-C |
| X24 | M 6 CAD 311+298; R 5 512+97 | Reconciled 609; main 311(13.05) arithmetic assigned numeric lane |
| X25 | M 6 AF 118+127; R 5 200+45 | Reconciled 245 |
| X26 | M 6 smoking 1057+1059; R 5 1736+380 | Reconciled 2116 |
| X27 | M 6 NIHSS medians 4/4; R 5 medians 3/3; M 4 imputationmedian 3 | F-D |
| X28 | M 6 armagemedians 65/64; R 5 availability 65/64 | Partition medians not additive; no contradiction from these observations |
| X29 | M 4 followup 3980; R 5 mRS 3949; M 8 disability 1852+1798 and deaths 139+160 | mRS 3650+299=3949 supports availability including deaths; followup and mRS not required identical,31difference not independently candidate |
| X30 | M 1,2 enrollmentAug 10,2014–June 20,2015; followupJuly 30,2016; M 9 intervention 11months | Different recruitment durations/horizon descriptions; no exact numeric conflict |
| X31 | M 2/P 6–7 adults, AISwithin 7days, CT/MRI; hospitalssecondary/tertiary; exclusions | Definitions broadly aligned;≥18 versus olderthan 18 not registered without a displayed patient-number consequence |
| X32 | M 3/P 7 randomization province/grade/baselinequality,1:1, SAS 9.3; M 5 selectiongrade/region | Selection and randomization distinct stages; no concrete count conflict |
| X33 | M 3/P 8 two staff,2-dayworkshop, first 7days/dischargeplan | Reconciled |
| X34 | M 3,5/P 11–13 weeklymonitoring,30patientbatches,4batches/3feedbackloops,120planned | Different operational counts;4×30=120,3interveningloops; no conflict |
| X35 | M 3/P 13–15/R 3 9measures,4acute/5discharge; M 4/P 19 illustrative 5of 7 eligible | Example 7 not a new total definition; no conflict |
| X36 | M 3,7/P 10,14/R 3,9 rtPAarrival 2h/treatment 3h | Reconciled full definition; abbreviated 2Hour versus 3hour labels describe different timing components |
| X37 | M 3,7/P 10,14/R 3,9 earlyantithrombotic 48h/2days | Reconciled; R 9 concatenated 48hours 2days does not change numeric threshold |
| X38 | M 3,7/P 14/R 3,9 dysphagiabeforeoralintake | Reconciled |
| X39 | M 3,7/P 14–15/R 3,9 DVTnonambulatory/endday 2 | Reconciled |
| X40 | M 3,7/P 15/R 3 dischargeantithrombotic | Reconciled |
| X41 | M 3,7/P 15/R 3 AF/fluttereligibility | Main row AF is abbreviated; full definition includes flutter, no proven numerator conflict |
| X42 | M 3,7/P 15/R 3,8 LDL>100 versus≥100mg/dL | F-E |
| X43 | M 3,7/P 15/R 3 hypertensionhistory/current | Reconciled full definitions |
| X44 | M 3,7/P 15/R 3 diabetes history/current | Reconciled full definitions |
| X45 | M 3–5/P 15–16,19/R 3–4,8–9 contraindications/deaths/exclusions | Primary eligible and sensitivity broader denominator distinction coherent |
| X46 | M 3 perpatientaverage; M 4 careopportunityGEE; P 16/R 2 pooled interventionformula | F-F for definition; descriptive versus inferential unit distinguished |
| X47 | M 3,6–7/P 16 all-or-noneeligiblepatientproportion | Reconciled definition and denominator 2400/2400 |
| X48 | M 4/P 17 power 4800/40/120,80%/5%, ICC.02,5%improvement | Reconciled; exact formula unavailable, no external recalculation |
| X49 | M 4/P 4,18 ITTalloutcomes; M 5primary flow | F-A is concrete issue; no generalized ITT methodology candidate |
| X50 | M 4/P 18–19 compositebinary opportunity GEE, ORPA; R 8labelORPA | Reconciled modeled measure; not raw OR of reported mean scores |
| X51 | M 4,8/P 19 vascular/deathCoxHR; M 4,8 disabilitybinaryOR | Reconciled ratio-column alignment; P 19 genericclinicalmodel does not independently establish disabilityHR claim |
| X52 | M 4,7–8/R 6–9 adjustedpatient/hospitalcovariates,95%CIs, referenceIvsC | Reconciled; AD/ratio Ps separate; exact variance/test details not printed |
| X53 | M 1,2,5,7,9 composite 88.2/84.8, AD 3.54(.68–6.40)→3.5(.7–6.4), P.02, ORPA 1.39(1.12–1.72), P.003, ICC.02 | Reconciled rounding; rawdifference 3.4 atM 9 is distinct from adjusted 3.54 |
| X54 | M 1,2,5–7,9 allnone 53.8/47.8, AD 6.69(−.41–13.79)→6.7(−.4–13.8), P.06, ORPA 1.19(.85–1.67), P.31, ICC.07 | Reconciled rounding and nonsignificance |
| X55 | M 5–7 all 9adherencenumericallyhigher; onlyDVT/antidiabeticsignificant | Reconciled primary AD andORPA Ps; sensitivity effects not same analysis |
| X56 | M 1,5,8 vascular 3mo 3.9/5.3, AD−2.03(−3.51–−.55)→−2.0(−3.5–−.6), P.007, HR.65(.49–.86) | Reconciled rounding/significance |
| X57 | M 1,5,8 vascular 6mo 6.3/7.8, AD−2.18(−4.0–−.35)→−2.2(−4.0–−.4), P.02, HR.72(.57–.90) | Reconciled rounding;−.35 exact boundary may round−.4 with half-away rule |
| X58 | M 1,5,8 vascular 12mo 9.1/11.8, AD−3.13(−5.28–−.97)→−3.1(−5.3–−1.0), P.005, HR.72(.60–.87), FigureP<.001 | Reconciled; ADP versusHRPdistinct |
| X59 | M 5,8 disability 3mo 19.2/21.0, AD−3.72(−6.7–−.79), OR.76(.63–.91) | Reconciled rounding, ORlabel/interpretation |
| X60 | M 5,8 disability 6mo 15.8/17.9, AD−3.86(−6.60–−1.13), OR.74(.61–.89) | Reconciled rounding |
| X61 | M 5,8 disability 12mo 12.7/14.7, AD−3.13(−5.80–−.46), OR.74(.59–.93) | Reconciled rounding |
| X62 | M 5 no significantmortalityhospital/3/6/12mo; M 8ADPs.009/.08/.38/.05; HRPs.14/.23/.81/.21 | F-G conditional forhospital; other horizons consistent thresholdP<.05 |
| X63 | M 8 death 12moHR.86(.68–1.09), P.21, Table 3/Figure 2B | Reconciled; probabilities/events versusHR remain different measures |
| X64 | M 5 clinicalevents 3/6/12monthsafter discharge; M 3,4,8/P 16 after symptom onset | F-H; plan corroborates onset side only |
| X65 | M 5 hemorrhage 1/46,2/23,2.2/8.7, P.26; M 7rtPAnumerators 46/23 | Reconciled treated-patient denominator; not primary eligible 212/204 |
| X66 | M 5 sensitivity 85.3/80.91, AD 4.20(1.77–6.63), ORPA 1.36(1.11–1.67), P.003; R 8 85.3/80.9, sameeffects | Reconciled precision; P.003alignedratio, ADP<.001inR 8 |
| X67 | M 7 versusR 8 all 9individualmeasurecounts, denominators, percentages, effects, Ps | Every numeratoridentical:46/23,2307/2253,2255/2040,178/66,2272/2141,63/39,1415/1439,1510/1372,653/557. Sensitivitydenominators≥primaryeacharm; all nine effect/P differences corresponddifferent overall population, not matched-resultconflicts |
| X68 | M 8 versusR 6–7 3/6/12month composite/individualeventcounts, HRs, ADs | All 12individualtime/type rows checked; event component sumsI 107/169/242, C 147/213/323≥composite 93/150/218, C 127/186/282; footnoteexplains multipleevents. ComponentHR/AD not required equalcomposite |
| X69 | M 8death 66/76,103/101,139/160 versusR 6vascular-death 46/67,70/82,91/125 | Eachvascular-deathcount≤all-causedeathcorrespondingarm/time; distinct endpoints coherent |
| X70 | M 8Figure 2risksets at 0/90/180/270/360; M 5followup 2003/1977 | At 0 all 2400, arrays nonincreasing; event-free set≤deathriskset atmatched arm/time; terminal follow-up completers different quantity; no count/rate conflict |
| X71 | M 7 "HR curves" versusM 8CumulativeIncidence axes 0–.15 | F-I |
| X72 | M 3,6,7 LDLmg/dLconversion×.0259; M 8mRS 3–5/R 5NIHSS 0–42 | Reconciled units/scales; mRSendpointband is not full scale; no external conversion required |
| X73 | M 8medianfollowup 364/365days, IQR 364–365; M 1finalfollowupdate/M 9one-yearhorizon; P 17followupconfirmation | Reconciled nominal 12months/approximately 1year; fixed calendar closing date and individual follow-up length are distinct |

## Preliminary candidates

All nine observations remain Pending Human Adjudication. The checker assigns no stable C IDs, severity, validity, disposition or correction. Relationship codes below are classification suggestions for coordinator confirmation.

### F-A — Primary-analysis population differs between text/table and flow labels

Compared locations: [main p4 Results/Data Analysis](../../../jama_wang_2018_oi_180070.pdf#page=4), REPORT: 4800 enrolled and included in primary analysis; ITT for all outcomes. [main p5 Figure1](../../../jama_wang_2018_oi_180070.pdf#page=5), REPORT: bottom boxes say 2003/1977 patients included in primary analysis. [main p7 Table2](../../../jama_wang_2018_oi_180070.pdf#page=7), REPORT: all-or-none denominators 2400/2400.

Direct observation: 2003+1977=3980 differs from 4800 by 820. The figure's 397+423 patients lost to 12-month follow-up explains the subtraction, but does not reconcile the primary-analysis label. Alternative: bottom boxes describe follow-up completers or a different analysis population. Human question: which patients entered the co-primary analyses, and what do the figure's labels mean? Suggested category: Analysis-unit or population inconsistency; S_W. PLAN ITT only corroborates; no P_R asserted.

### F-B — Baseline-survey total differs from stated per-cluster recruitment

[main p6 Table1](../../../jama_wang_2018_oi_180070.pdf#page=6), REPORT: baseline survey 40 hospitals, 801 patients. [results supplement p2 eAppendix](../../../joi180070supp2_prod.pdf#page=2), REPORT: 20 patients per cluster were prospectively included in this prerandomization phase.

Direct numbers give 40×20=800, rather than 801. No rounding required. Alternative: 20 was nominal recruitment and one cluster included 21, or survey snapshots differed. Human question: was 20 exact or a target, and do both descriptions concern the same final survey? Verify per-cluster recruitment. Suggested category: Denominator, proportion, or total inconsistency; S_C.

### F-C — Dyslipidemia counts differ across exhaustive cohort partitions

[main p6 Table1](../../../jama_wang_2018_oi_180070.pdf#page=6), REPORT: intervention 305/2400 (12.7%), control 291/2400 (12.1%). [results supplement p5 eTable2](../../../joi180070supp2_prod.pdf#page=5), REPORT: with 1-year mRS 285/3949 (7.2%), loss to mRS 62/851 (7.3%).

Direct sums: 596 versus 347, difference 249. Derived identity rule: a fixed baseline characteristic total is invariant under two exhaustive partitions of the same 4800 patients. Denominators reconcile, as do the sex, ischemic stroke, diabetes, hypertension, CAD/MI, AF and smoking sums. Alternative: an undisclosed definition, recode or dataset snapshot differs, or a row was mislabeled/transcribed. Human question: did dyslipidemia definitions and snapshots match, and which counts describe the 4800 cohort? Suggested category: Cross-document numeric inconsistency; S_C. No PLAN discrepancy.

### F-D — Admission NIHSS medians cannot represent the same distribution under the printed partitions

[main p6 Table1](../../../jama_wang_2018_oi_180070.pdf#page=6), REPORT: each arm has 2400 patients, NIHSS median 4 (IQR 2–6). [results supplement p5 eTable2](../../../joi180070supp2_prod.pdf#page=5), REPORT: availability groups of 3949 and 851, each median 3 (IQR 2–6). [main p4 imputation paragraph](../../../jama_wang_2018_oi_180070.pdf#page=4), REPORT: one missing NIHSS replaced by median 3.

Direct comparison: same admission-score label, differing partition medians. Derived order-statistic diagnostic: each even group of 2400 with median 4 can contain at most 1200 integer scores ≤3 under conventional medians. Together that permits at most 2400. Odd groups of 3949 and 851 with median 3 require at least 1975+426=2401 scores ≤3. Both cannot describe identical records. The imputation paragraph is contextual evidence only; its separate comparison with Table1 has an unknown reference population and belongs to the numeric lane. It does not extend this candidate beyond S_C.

Alternative: scores or nonmissing sample sizes differed, imputation used a subset, summaries were rounded under an unusual quantile convention, or there is a transcription error. Human question: what exact observations, imputation stage, convention and snapshot underlie each summary? Verify that both median rows cover all 4800. Suggested category: Cross-document numeric inconsistency; S_C. No clinical inference or PLAN discrepancy.

### F-E — Lipid-lowering eligibility uses both >100 and ≥100 mg/dL

[main p3 Outcomes](../../../jama_wang_2018_oi_180070.pdf#page=3), REPORT: LDL more than 100 mg/dL or undocumented. [main p7 Table2](../../../jama_wang_2018_oi_180070.pdf#page=7), REPORT: LDL >100, with fractions 1415/1481 and 1439/1547. [results supplement p3 eTable1](../../../joi180070supp2_prod.pdf#page=3), REPORT: LDL ≥100, previous lipid-lowering treatment, or undocumented LDL. [results supplement p8 eTable4](../../../joi180070supp2_prod.pdf#page=8), REPORT: LDL >100, fractions 1415/1517 and 1439/1586. [protocol p15 Table3](../../../joi180070supp1_prod.pdf#page=15), PLAN: LDL ≥100, prior treatment, or undocumented LDL.

Direct boundary mismatch: 100 satisfies ≥100 but not >100 for the same named performance measure. No count of patients exactly 100 is supplied, so no denominator change is inferred. Omission of prior treatment from abbreviated main wording is not independently counted. Alternative: abbreviated labels, with all analyses following full specifications, or a different implemented threshold. Human question: which eligibility rule produced primary and sensitivity denominators? Suggested category: Measure, label, or scale inconsistency; P_R, S_C and S_W. PLAN defines the conflicting boundary substantively.

### F-F — Composite descriptive measure uses patient-average versus pooled-opportunity formulas

[main p3 Outcomes](../../../jama_wang_2018_oi_180070.pdf#page=3), REPORT: ratio for a given patient, calculated per patient and then averaged. [main p7 Table2](../../../jama_wang_2018_oi_180070.pdf#page=7), REPORT: composite mean (SD) 88.2 (15.1) versus 84.8 (18.2). [protocol p16 lines216–219](../../../joi180070supp1_prod.pdf#page=16), PLAN: total interventions performed among eligible patients divided by total possible interventions among eligible patients. [results supplement p2 eAppendix](../../../joi180070supp2_prod.pdf#page=2), REPORT: same aggregate formula, states same endpoint definition used in randomized phase, baseline 80.2%/79.5%. [main p4 Data Analysis](../../../jama_wang_2018_oi_180070.pdf#page=4), REPORT: separate binary care-opportunity model.

Direct wording difference concerns the reported composite measure. Derived rule: mean(m_i/e_i) generally differs from sum(m_i)/sum(e_i) when eligible opportunities e_i differ. Patient-level opportunities are unavailable; no printed percentage is claimed wrong. The descriptive patient mean and inferential care-opportunity GEE can coexist; that modeling distinction is not a contradiction. Alternative: the aggregate description implicitly meant ratios at patient level followed by averaging, or baseline used different aggregation. Human question: which weights and aggregation generated the baseline and randomized summaries? Suggested category: Measure, label, or scale inconsistency; P_R and S_C. No additional P_P from descriptive versus inferential units.

### F-G — Blanket in-hospital mortality nonsignificance differs from the printed AD P value

[main p5 Clinical Events](../../../jama_wang_2018_oi_180070.pdf#page=5), REPORT: no significant difference in total mortality rates in hospital and at 3/6/12 months. [main p8 Table3](../../../jama_wang_2018_oi_180070.pdf#page=8), REPORT: in-hospital death 11/2400 versus 23/2400; adjusted AD −0.7 (95% CI −1.1 to 0.2), P=.009; adjusted HR 0.96 (0.90–1.02), P=.14. [main p4](../../../jama_wang_2018_oi_180070.pdf#page=4), REPORT: two-sided significance P<.05.

Direct unrestricted narrative differs from .009<.05. HR P=.14 supports prose if prose referred exclusively to HR. This is a conditional interpretation/attribution candidate; AD and HR tests are not equated, and CI/P compatibility is a separate statistical-lane check. Alternative: narrative refers only to HR, or AD P was misprinted. Human question: what mortality estimand/test underlies the blanket statement? Verify the in-hospital AD P and intended prose scope. Suggested category: Statistical reporting inconsistency; S_W.

### F-H — Identical clinical estimates are assigned conflicting time origins

[main p5 Clinical Events](../../../jama_wang_2018_oi_180070.pdf#page=5), REPORT: Table3 outcomes at 3/6/12 months after discharge, followed by the same vascular/disability estimates as Table3. [main p3 Outcomes](../../../jama_wang_2018_oi_180070.pdf#page=3), REPORT: after initial symptom onset. [main p8 Table3 footnote/Figure2](../../../jama_wang_2018_oi_180070.pdf#page=8), REPORT: disability after stroke onset; axes "Days After Stroke Symptom Onset". [protocol p16](../../../joi180070supp1_prod.pdf#page=16), PLAN, corroborates onset.

Direct time-label difference applies to matched numeric results. Derived identity: clocks from onset and discharge differ by the onset-to-discharge interval. Main Table1 has stay medians 13/12 days; exact onset-to-discharge times are unavailable. No effect on counts is calculated. Alternative: after discharge loosely describes contact rather than assessment horizon, or a narrative time-origin error. Human question: which clock generated clinical assessments and 90/180/360-day plots? Suggested category: Measure, label, or scale inconsistency; S_W only. PLAN corroborates one main-report side, so no P_R.

### F-I — Cumulative-incidence plots are called HR curves

[main p7 discussion](../../../jama_wang_2018_oi_180070.pdf#page=7), REPORT: "The HR curves" of new vascular events were separated in the first 30 days. [main p8 Figure2A](../../../jama_wang_2018_oi_180070.pdf#page=8), REPORT: ordinate Cumulative Incidence, ticks 0/.05/.10/.15, separate arm curves; fixed annotation HR .72 (.60–.87), P<.001.

Direct label mismatch: plotted arm-specific cumulative probabilities are not HR as a function of time. Curves start at zero; HR is a comparative ratio with null 1. Alternative: loose shorthand for incidence curves accompanying Cox HR. Human question: which plotted measure was intended in the discussion? Verify the figure ordinate and ensure probability curves remain distinct from HR during extraction. No claim that HR .72 is wrong. Suggested category: Measure, label, or scale inconsistency; S_W.

## Limits and handoff

All assigned matched relationships were examined; there is no scientific-coverage gap. Visual source-matched images of main p6 and supplement p5 confirm the dyslipidemia and NIHSS transcriptions. The mechanical rechecker should inspect exact source pages for every registered finding. Aggregate reports do not expose raw distributions, exact snapshots, patients exactly 100 mg/dL, patient composite opportunity counts, per-cluster survey recruitment, or exact AD test/variance construction. These are named human questions. No person-time denominator is printed; prose "rates" generally denotes risks/proportions, and no standalone rate-versus-count candidate is established. No display-zero P candidate was registered. This lane preserves the separate AD, ORPA, OR and HR estimands and P columns; the statistical lane covers inferential compatibility.
