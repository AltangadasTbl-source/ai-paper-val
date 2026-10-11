# Statistical relationship pass 1 records — main shard

Fresh agent /root/stat1_main, gpt-6.1-sol/high, pass 1 only. Assigned S001–S092. These 92 explicit records are a disjoint part for the coordinator’s canonical inventory merge. Source definitions remain in relationship_inventory.md.

| ID | Pass 1 status | Complete check record |
|---|---|---|
| S001 | PASS_1_COMPLETE | Hospital randomization, five one-way crossover cohorts, six four-month periods and admission-date allocation agree across main abstract, Methods and flow. Mixed model S004 represents hospital correlation and period effects; no paired-patient design is stated. |
| S002 | PASS_1_COMPLETE | Power inputs read at p.3; 15,750 exceeds planned 15,000 and achieved eligible n = 21,374 exceeds target. Observed outcome ICC.15–.40 exceeds planning.05, consistent with limitation wording. Exact cluster-period power implementation unavailable; excluded missing-input observation recorded. |
| S003 | PASS_1_COMPLETE | Main primary composite and Table 3 components agree. In-hospital medication composite explicitly discloses predefined statin not collected; four-drug reported composite is identified rather than silently equated with five-drug collection. Outcome status comparisons against plans are assigned to support/cross-source lanes. |
| S004 | PASS_1_COMPLETE | Primary logistic model includes random hospital and fixed four-month time effects; GRACE sensitivity covariates named. OR ratio versus RD scale remains distinguishable despite footnote wording. Time contrast mapping is F-ST1-001; no unreported variance model inferred. |
| S005 | PASS_1_COMPLETE | Eligible I/C totals 11,308/10,066 sum 21,374; complete follow-up 21,079 plus missing 295 equals 21,374. Figure 1 explicitly retains lost follow-up in analysis. Process exclusions are documented. Missing numerical imputation/outcome-availability detail alone is excluded. |
| S006 | PASS_1_COMPLETE | Interim at 12 months, z > 2.797 and two-sided.005; final z > 1.977 and.048. Diagnostic standard-normal tails approximately.00516 and.04804 are compatible with stated displayed thresholds. Primary CIs contain null and conclusion is nonsignificant under.048. No interim statistic is supplied; no stopping conflict or noninferiority/equivalence claim exists. No extra multiplicity correction is asserted. |
| S007 | PASS_1_COMPLETE | Prespecified interaction-testing statement and Figure 3 subgroup display mapped; no interaction P/statistic supplied. Similar-pattern claim does not imply equality of subgroup estimates. Time-exposure interaction and expanded composite explicitly post hoc in main. Support lane owns plan-to-report status comparisons. |
| S008 | PASS_1_COMPLETE | Monitoring description, 13 primary-event changes, and software statements mapped. Primary event total 645+602=1247 gives 13/1247=1.04%, matching displayed 1%; no analysis-method conflict follows. |
| S009 | PASS_1_COMPLETE | Age mean difference.6 is consistent with 60.9−60.3 allowing one-decimal input precision; CI .3 to 1.0 contains.6 and is ordered. No test/SE supplied; SDs and group n do not state the inferential engine. |
| S010 | PASS_1_COMPLETE | Male percentages 76.0/75.4 reproduce counts; crude RD −.61367 percentage points lies in printed −.6 half interval. CI −1.8 to.5 contains estimate; no supplied test. |
| S011 | PASS_1_COMPLETE | Tobacco percentages 37.5/25.1 and crude RD −12.34003 reconcile; CI −13.6 to −11.1 contains estimate, direction negative. |
| S012 | PASS_1_COMPLETE | Diabetes percentages 41.2/47.2 and crude RD 5.92347 reconcile; CI 4.6 to 7.3 contains estimate, direction positive. |
| S013 | PASS_1_COMPLETE | Transfer percentages 41.7/37.1 and crude RD −4.61148 reconcile; CI −5.9 to −3.3 contains estimate, direction negative. |
| S014 | PASS_1_COMPLETE | Uninsured percentages 68.3/76.6 and crude RD 8.28929 reconcile; CI 7.1 to 9.5 contains estimate, direction positive. |
| S015 | PASS_1_COMPLETE | STEMI percentages 68.8/59.9 and crude RD −8.90478 reconcile; CI −10.2 to −7.6 contains estimate, direction negative. |
| S016 | PASS_1_COMPLETE | Symptom-to-door medians 240/255 and IQRs 120–840/111–825 ordered; crude difference 15 matches medians, CI 4 to 26 contains 15. n = 9711/10,849 within group totals; quantile CI engine not supplied. |
| S017 | PASS_1_COMPLETE | Weight 63.6/63.3 yields −.3 at display precision, CI −.5 to.0 contains point; variable n = 10,065/11,304 within totals. No test/SE supplied. |
| S018 | PASS_1_COMPLETE | Systolic BP 138.1/139.0 yields.9, CI .1 to 1.7 contains point; variable n = 10,061/11,303 within totals. No test/SE supplied. |
| S019 | PASS_1_COMPLETE | Heart rate 80.0/79.9 yields −.1, CI −.6 to.5 contains point; variable n = 10,065/11,303 within totals. No test/SE supplied. |
| S020 | PASS_1_COMPLETE | Troponin medians 1.6/1.1 give −.5; IQRs and CI −.7 to −.4 ordered and contain respective points. n = 4566/4483; no unprinted median test inferred. |
| S021 | PASS_1_COMPLETE | LDL means 126.2/119.1 give −7.1; CI −8.4 to −5.8 contains point; n = 7288/7542. No test/SE supplied. |
| S022 | PASS_1_COMPLETE | Triglyceride medians 121/122 give 1; IQRs and CI −1 to 3 contain respective points; n = 7308/7552. No median CI formula supplied. |
| S023 | PASS_1_COMPLETE | Creatinine medians 1.0/1.0 and printed.0 difference/.0 CI endpoints permit hidden precision; n = 4246/9589 and IQRs ordered. Apparent degenerate display excluded under precision rule. |
| S024 | PASS_1_COMPLETE | Fasting glucose medians 124/130 give 6; IQRs and CI 4 to 8 contain respective points; n = 6658/6740. No median CI formula supplied. |
| S025 | PASS_1_COMPLETE | Hemoglobin means 13.3/13.2 give −.1; CI −.2 to.0 contains estimate; n = 9763/11,079. Unit-label observation excluded. |
| S026 | PASS_1_COMPLETE | Government patient percentages/counts and crude RD −13.85312 reconcile with printed −13.9; CI −15.1 to −12.6 contains point. Hospital n = 9 distinguished from patients. Hospital-type counts partition totals with S027/S028. |
| S027 | PASS_1_COMPLETE | Nonprofit percentages/counts and RD −1.45586 reconcile with −1.5; CI −2.7 to −.3 contains point. Hospital n = 12 distinguished from patients. |
| S028 | PASS_1_COMPLETE | Private percentages/counts and RD 15.30899 reconcile with 15.3; CI 14.0 to 16.6 contains point. Hospital n = 42; hospital types 9+12+42=63 and patient categories sum each arm. |
| S029 | PASS_1_COMPLETE | Extra-large percentages/counts and RD −3.31300 reconcile with −3.3; CI −4.3 to −2.3 contains point. Hospital n = 5 distinguished from participants. |
| S030 | PASS_1_COMPLETE | Large percentages/counts and RD 8.50392 reconcile with 8.5; CI 7.2 to 9.8 contains point. Hospital n = 15. |
| S031 | PASS_1_COMPLETE | Medium percentages/counts and RD −6.66488 reconcile with −6.7; CI −7.9 to −5.4 contains point. Hospital n = 24. |
| S032 | PASS_1_COMPLETE | Small percentages/counts and RD 1.47395 reconcile with 1.5; CI .7 to 2.2 contains point. Hospital sizes 5+15+24+19=63; size-category patient counts partition both arms. |
| S033 | PASS_1_COMPLETE | Newly installed cath-lab percentages/counts and RD 1.17528 reconcile with 1.2; CI .8 to 1.6 contains point. Hospital n = 3. |
| S034 | PASS_1_COMPLETE | No cath-lab percentages/counts and RD −6.10651 reconcile with −6.1; CI −7.1 to −5.1 contains point. Hospital n = 17. |
| S035 | PASS_1_COMPLETE | Cath-lab yes percentages/counts and RD 4.93123 reconcile with 4.9; CI 3.9 to 6.0 contains point. Status categories 3+17+43=63 and patient counts partition both arms. |
| S036 | PASS_1_COMPLETE | Prehospital aspirin eligible ratios reproduce 16.9/18.6%; modeled RD 3.80 and OR 1.40 have ordered containing CIs excluding respective nulls, positive direction. Table/narrative match. No P/test/SE supplied. |
| S037 | PASS_1_COMPLETE | Prehospital thrombolysis 25/6921 and 37/6768 reproduce .4/.5%; modeled RD −.04 and OR.95 both include null in CIs, negative adjusted direction. Crude increase is not compared to adjusted effect. |
| S038 | PASS_1_COMPLETE | In-hospital aspirin counts/eligible denominators reproduce 98.2/97.7%; modeled RD −.05/OR.98 CIs contain point and null, agreeing with high/similar narrative. |
| S039 | PASS_1_COMPLETE | In-hospital antiplatelet ratios reproduce 98.1/98.4%; modeled RD −.05/OR.98 CIs contain point and null. Crude/model direction difference is not a finding. |
| S040 | PASS_1_COMPLETE | In-hospital β-blocker ratios reproduce 37.2/42.6%; modeled RD 6.25/OR 1.46 CIs exclude nulls, direction positive. Table/narrative upper-RD limit copy difference is screened under precision rule. |
| S041 | PASS_1_COMPLETE | Anticoagulant ratios reproduce both 85.6%; modeled RD 2.60/OR 1.27 CIs exclude nulls, narrative identifies adjusted increase. Crude equal percentages do not contradict modeled effect. |
| S042 | PASS_1_COMPLETE | Echocardiography ratios reproduce 91.5/93.0%; modeled RD 5.62/OR 2.50 CIs contain point/exclude null, narrative consistent. C 91.5 rounded to whole-percent 92 is compatible. |
| S043 | PASS_1_COMPLETE | Diagnostic angiography ratios reproduce 61.4/57.5%; both modeled quantities explicitly Nonestimable. No estimate or inferential claim fabricated; narrative decrease describes crude rates. |
| S044 | PASS_1_COMPLETE | PCI ratios reproduce 52.5/46.6%; RD −1.66 CI −3.27 to −.04 and OR.87 CI .77–.99 contain point/exclude null, lower-I direction agrees with narrative. |
| S045 | PASS_1_COMPLETE | Primary PCI STEMI ratios reproduce 50.2/47.8%; RD −1.87 and OR.86 each contain point and include respective nulls. Full STEMI denominators agree with baseline status counts. |
| S046 | PASS_1_COMPLETE | Door-to-balloon medians/IQRs ordered; n = 4022/3639 are reported time contributors, not assumed equal to primary-PCI recipients. Each adjusted interval contains its point. Distinct contrast/CI mapping is F-ST1-001. No P/test supplied. |
| S047 | PASS_1_COMPLETE | STEMI thrombolysis ratios reproduce 23.1/23.2%; modeled RD 5.56/OR 1.59 CIs contain point/exclude nulls, adjusted-increase narrative agrees. |
| S048 | PASS_1_COMPLETE | Door-to-needle medians/IQRs ordered; n = 1455/1433 are within thrombolysis counts 1596/1571. Both adjusted CIs contain point/null. Distinct.40 versus 5.00 mapping is F-ST1-001. |
| S049 | PASS_1_COMPLETE | Any reperfusion ratios reproduce 73.2/71.0%; modeled RD 3.43/OR 1.24 CIs exclude nulls, positive adjusted direction; crude decrease is not a model conflict. |
| S050 | PASS_1_COMPLETE | Rescue-PCI ratios reproduce 9.3/15.2%; row-specific n = 6891/6767 respected. RD 2.45/OR 1.39 CIs contain point/exclude nulls; narrative agrees. No convention-based replacement denominator. |
| S051 | PASS_1_COMPLETE | Discharge aspirin ratios reproduce 97.5/98.1%; RD 1.36/OR 1.65 CIs contain point/exclude nulls, positive adjusted direction agrees with narrative. Eligibility restriction supplied. |
| S052 | PASS_1_COMPLETE | Discharge antiplatelet ratios reproduce 97.9/98.1%; RD.41/OR 1.24 CIs contain point/include nulls, high/similar narrative consistent. |
| S053 | PASS_1_COMPLETE | Discharge β-blocker ratios reproduce 65.3/66.8%; RD 6.69/OR 1.48 CIs contain point/exclude nulls. Narrative 6.63/1.47 screened under precision rule. |
| S054 | PASS_1_COMPLETE | Discharge statin ratios reproduce 96.6/97.3%; RD 1.21/OR 1.42 CIs contain point/exclude nulls; narrative agrees. |
| S055 | PASS_1_COMPLETE | ACE/ARB among discharged EF ≤ 40% ratios reproduce 51.9/43.0%; modeled RD 6.57/OR 1.45 CIs exclude nulls and positive adjusted direction agrees with narrative. No crude/model contrast finding. |
| S056 | PASS_1_COMPLETE | Rehabilitation ratios reproduce 25.6/30.8%; both adjusted quantities explicitly Nonestimable, narrative describes crude increase only. No missing-model candidate without a conflicting printed value. |
| S057 | PASS_1_COMPLETE | MACE 645/10,066 and 602/11,308 reproduce 6.4/5.3%; both cluster and primary RD/OR CIs ordered, contain point/null. Primary −.09(−1.32,1.14)/.98(.80,1.21) matches abstract, Key Points and text; no-reduction/nonsignificant conclusion consistent with final α.048. ICC.15> .05 planned. |
| S058 | PASS_1_COMPLETE | Mortality 509/10,066 and 445/11,308 reproduce 5.1/3.9%; cluster OR.87 upper 1.00 not taken as an unprinted significant test. Primary −.28 CI −1.35,.80 and OR.94 CI .74,1.19 include null; narrative agrees. All four CIs contain their points; ICC.18. |
| S059 | PASS_1_COMPLETE | CVD mortality 494/10,066 and 434/11,308 reproduce 4.9/3.8%; counts ≤ all-cause deaths. Both adjusted RDs/ORs have ordered containing CIs including null, no-difference narrative consistent; ICC.19. |
| S060 | PASS_1_COMPLETE | In-hospital mortality 331/10,066 and 321/11,308 reproduce 3.3/2.8%; counts ≤ 30-day deaths. Both adjustment models' CIs contain point/null; ICC.18. |
| S061 | PASS_1_COMPLETE | Reinfarction 121/10,066 and 135/11,308 reproduce 1.2/1.2%; modeled RDs positive/ORs > 1, all CIs contain point/null; no-difference narrative consistent; ICC.33. |
| S062 | PASS_1_COMPLETE | Stroke 60/10,066 and 90/11,308 reproduce .6/.8%; modeled RDs positive/ORs > 1, all CIs contain point/null; ICC.14. |
| S063 | PASS_1_COMPLETE | GUSTO bleeding 19/10,066 and 30/11,308 reproduce .2/.3%; defined event consistent with primary component. Modeled RDs positive/ORs > 1, all CIs contain point/null; ICC.20. |
| S064 | PASS_1_COMPLETE | Optimal in-hospital 3122(31.7)/3878(35.8) uses eligibility-for-all-drugs restriction, not full headers; exact eligible totals not supplied. Both models' RD/OR CIs contain point/exclude null, higher-medication narrative consistent; ICC.40. |
| S065 | PASS_1_COMPLETE | Optimal discharge 5454(61.8)/6483(64.0) restricted to discharged eligible-for-all-drugs participants; exact denominator not supplied. Both models' RD/OR CIs contain point/exclude null, positive direction agrees; ICC.28. |
| S066 | PASS_1_COMPLETE | Tobacco 3526(96.0)/2618(94.7) restricted to discharged baseline smokers; exact denominator not supplied. Both models' RD/OR CIs contain point/include null, no-effect narrative consistent; ICC.37. |
| S067 | PASS_1_COMPLETE | Age < 50 ratios reproduce 2.8/3.3%; adjusted RD 1.42/OR 1.53 CIs contain point/null; positive modeled direction corresponds to right-of-null forest marker. No interaction P supplied. |
| S068 | PASS_1_COMPLETE | Age 50–69 ratios reproduce 4.5/5.6%; RD −.57/OR.89 CIs contain point/null; negative direction agrees with left forest marker. |
| S069 | PASS_1_COMPLETE | Age ≥ 70 ratios reproduce 9.4/11.6%; RD −.23/OR.98 CIs contain point/null; forest marker near left null agrees. Three age groups sum events 602/645 and participants 11,308/10,066. |
| S070 | PASS_1_COMPLETE | Male ratios reproduce 4.4/5.3%; RD.05/OR 1.01 CIs contain point/null; right-of-null marker agrees. |
| S071 | PASS_1_COMPLETE | Female ratios reproduce 8.2/9.8%; RD −.57/OR.93 CIs contain point/null; left marker agrees. Sex strata sum full events/populations. |
| S072 | PASS_1_COMPLETE | STEMI ratios reproduce 5.9/6.7%; RD.57/OR 1.09 CIs contain point/null; adjusted positive direction agrees with right marker. |
| S073 | PASS_1_COMPLETE | NSTEMI ratios reproduce 4.4/5.7%; RD −1.46/OR.75 CIs contain point/null; left marker agrees. MI-type strata sum full events/populations. |
| S074 | PASS_1_COMPLETE | Extra-large ratios reproduce 3.0/4.1%; RD 1.83/OR 1.68 CIs contain point/null; forest marker right and right-tail arrow agrees with OR upper 3.32 beyond plotted 3.0. |
| S075 | PASS_1_COMPLETE | Large ratios reproduce 3.4/6.0%; RD −1.56/OR.71 CIs contain point/null; left marker agrees. |
| S076 | PASS_1_COMPLETE | Medium ratios reproduce 8.2/8.1%; RD −1.47/OR.83 CIs contain point/null; left modeled direction agrees with marker, not equated with crude. |
| S077 | PASS_1_COMPLETE | Small ratios reproduce 8.5/5.8%; RD 2.28/OR 1.45 CIs contain point/null; right marker/arrow agrees with upper 3.04 beyond 3.0. Size strata sum full events/populations and 63 hospitals. |
| S078 | PASS_1_COMPLETE | Government ratios reproduce 5.2/6.7%; RD −.55/OR.90 CIs contain point/null, marker left. |
| S079 | PASS_1_COMPLETE | Nonprofit ratios reproduce 6.3/6.9%; RD −.62/OR.91 CIs contain point/null, marker left. |
| S080 | PASS_1_COMPLETE | Private ratios reproduce 4.9/5.6%; RD.89/OR 1.16 CIs contain point/null, marker right. Type strata sum full events/populations and 63 hospitals. |
| S081 | PASS_1_COMPLETE | Figure 2A cohort 1 all six points and 12 endpoints visually inspected: containment/order maintained, open at step 0 and solid steps 1–5. Contributor counts 439,662,542,654,605,648 match printed rows. Rates/CIs approximate, no exact test/SE/count numerators supplied. |
| S082 | PASS_1_COMPLETE | Figure 2A cohort 2 all six points/12 endpoints inspected; containment/order maintained, open steps 0–1 and solid 2–5. Counts 400,379,723,785,727,600. Exact CI engine unavailable; no tests invented. |
| S083 | PASS_1_COMPLETE | Figure 2A cohort 3 all six points/12 endpoints inspected; containment/order maintained, open 0–2 and solid 3–5. Counts 858,910,827,993,1022,964. Graphical readings approximate. |
| S084 | PASS_1_COMPLETE | Figure 2A cohort 4 all six points/12 endpoints inspected; containment/order maintained, open 0–3 and solid 4–5. Counts 477,629,730,679,860,627. Graphical readings approximate. |
| S085 | PASS_1_COMPLETE | Figure 2A cohort 5 all six points/12 endpoints inspected; containment/order maintained, open 0–4 and solid 5. Counts 741,731,694,743,829,896. All-cohort counts sum 21,374, matching eligible total. |
| S086 | PASS_1_COMPLETE | Figure 2B cohort 1 all six points/12 endpoints inspected; containment/order maintained, open 0 and solid 1–5. Counts identical to panel A; mortality points no higher than matched MACE points at graphical precision. No test supplied. |
| S087 | PASS_1_COMPLETE | Figure 2B cohort 2 all six points/12 endpoints inspected; containment/order maintained, open 0–1 and solid 2–5. Counts identical to panel A; mortality versus composite directions agree. |
| S088 | PASS_1_COMPLETE | Figure 2B cohort 3 all six points/12 endpoints inspected; containment/order maintained, open 0–2 and solid 3–5. Counts identical to panel A; mortality points ≤ composite points at graphical precision. |
| S089 | PASS_1_COMPLETE | Figure 2B cohort 4 all six points/12 endpoints inspected; containment/order maintained, open 0–3 and solid 4–5. Counts identical to panel A; mortality points ≤ composite points at graphical precision. |
| S090 | PASS_1_COMPLETE | Figure 2B cohort 5 all six points/12 endpoints inspected; containment/order maintained, open 0–4 and solid 5. Counts identical to panel A; mortality points ≤ composite points at graphical precision. Narrative first intervention-step rates lower than concurrent control cohorts is visually compatible. |
| S091 | PASS_1_COMPLETE | Expanded MACE unadjusted 7.0/9.1%, cluster OR.89(.80,1.00), primary RD −1.34(−2.72,.04)/OR.84(.70,1.00): all CIs ordered/contain points; primary RD contains null and OR reaches it. Narrative direction/hypothesis-generating language excluded as wording, no asserted significance. Exact event denominators/numerators not printed in main. |
| S092 | PASS_1_COMPLETE | Follow-up troponin 1.3 versus 4.6/P < .001 matches supplement medians and difference 3.3 CI .1,6.5; CI excludes 0 and P < .001 is significant at.05. Test/CI-engine/common-estimand mapping absent; diagnostic normal-Wald magnitude comparison excluded rather than substituting a method. |

