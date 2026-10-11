# Statistical review pass 1 — main-paper shard

Fresh agent: `/root/stat1_main`; named `qc162_statistical_consistency_reviewer` preset, run model `gpt-6.1-sol`, reasoning effort `high`, start mode `FRESH_SPAWN`. The coordinator records the spawn-return runtime agent ID in the execution manifest. This agent performs pass 1 only.

Exact assigned scope: S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092. There are 92 main relationships. S501–S571 are the disjoint support shard; their pass records and findings are merged by the coordinator.

Scope and review contract were read completely. Sources: supplied REPORT article `jama_huffman_2018_oi_170166.pdf`, physical pp.1–12, the new main quantitative evidence map and canonical relationship inventory. Support evidence was used only to locate source-established method context for sample-size and troponin checks; support findings are not duplicated here. No prior scientific review conclusions or external sources were used.

Direct evidence: Poppler `pdftotext -layout` extracted the supplied main PDF to `preprocessing/st1-main/main-layout.txt`. Direct targeted layout extractions of protocol p.18 and report supplement p.17 are `preprocessing/st1-main/protocol-p18.txt` and `preprocessing/st1-main/report-supp-p17.txt`. Existing run-local direct-source renderings of main pp.5,6,8,9 were visually inspected, covering all main baseline/process rows, 60 Figure 2 points and their 120 interval endpoints, and all 14 Figure 3 rows and markers. Compute device CPU; no OCR was required. Derivatives preserve source text and were not used to normalize printed values.

For each relationship, checks include applicable counts and denominators, interval containment/order, direction and effect identity, matching reported analyses, stated method and design, and conclusions against the interim/final decision rule. Nulls are 0 for differences/coefficients and 1 for odds ratios. All displayed result intervals are 95%. The paper states two-sided final α=.048 and interim α=.005; it reports no result-specific test statistic or standard error, and only S092 supplies a P value. No unreported sidedness, degrees of freedom, covariance, variance estimator, adjustment, denominator, or model is inferred. Crude estimates are recomputed only in explicitly crude Table 1; adjusted Table 2/3/Figure 3 estimates are not equated with crude arithmetic.

## Findings

### F-ST1-001

**Title:** Two time-outcome contrasts lack a distinct estimand and analysis mapping.

**Relationships:** S004, S046, S048. **Focus areas:** B (estimate logic), C (statistical method logic). **Proposed review domain:** `statistical_results`. **Proposed primary relationship:** `S_W`; **All relationships:** `S_W`.

**Exact locations and document roles:** REPORT [main PDF p.6](../../../jama_huffman_2018_oi_170166.pdf#page=6), Table 2, rows “Door-to-balloon time (STEMI), median (IQR), min ” and “Door-to-needle time (STEMI), median (IQR), min,” columns “Difference, % (95% CI)” and “Odds Ratio or β-Coefficient (95% CI),” plus footnotes b and c and Table 2 title. REPORT [main PDF p.3](../../../jama_huffman_2018_oi_170166.pdf#page=3), Statistical Analysis, describes hospital/time adjustment but supplies no separate time-outcome estimand mapping.

**Printed values and statements:** Door-to-balloon C median 65 minutes (IQR 53–105; n = 4022), I median 77 minutes (IQR 55–118; n = 3639); difference 6.18 (95% CI −4.78 to 17.14); β-coefficient 13.00 (95% CI 3.64–22.36). Door-to-needle C median 44 minutes (IQR 30–67; n = 1455), I median 45 minutes (IQR 27–75; n = 1433); difference 0.40 (95% CI −5.23 to 6.03); β-coefficient 5.00 (95% CI −5.20–15.20). Both effect-column headings cite footnote b. It describes the intervention-versus-control effects as the difference in marginal effects, intervention minus control, in mixed-effects logistic or quantile regression with hospital clustering and temporal trends. Footnote c identifies the time-row final column as β-coefficients. The table title places the outcomes under the same clustering/time adjustment.

**Rule and calculation:** Distinct values for a time contrast need a source-defined distinction in estimand or analysis so a reader can identify which reported effect is being extracted. A β-coefficient and a difference described by the same intervention-minus-control marginal-effect language cannot simply be interchanged here. No equivalence to raw median differences is imposed. At two-decimal display precision, door-to-balloon 6.18 represents [6.175,6.185], whereas 13.00 represents [12.995,13.005]; minimum gap 6.810, relative discrepancy 6.810/6.18=1.10194 (> 0.05). Door-to-needle 0.40 represents [0.395,0.405], whereas 5.00 represents [4.995,5.005]; minimum gap 4.590, relative discrepancy 4.590/0.40=11.475 (> 0.05). These comparisons establish that the two printed effects are numerically distinct, rather than assuming that either must replace the other.

The door-to-balloon difference CI has endpoint half-unit intervals [−4.785,−4.775] and [17.135,17.145], and contains zero. The β CI has endpoint intervals [3.635,3.645] and [22.355,22.365], and excludes zero. Each estimate is contained in its own correctly ordered CI. Thus the distinction also affects the null-inclusion conclusion. No P value or test statistic is printed for these rows, and no P value is manufactured from a CI. Door-to-needle endpoint intervals are [−5.235,−5.225]/[6.025,6.035] and [−5.205,−5.195]/[15.195,15.205]; both CIs contain zero despite materially different effect magnitudes.

**Qualifying route:** Route B. The issue is in focus, the joint method description does not identify which distinct time estimand or analysis generated each effect column, and choosing one contrast changes extraction and, for door-to-balloon, the null-inclusion reading.

**Affected result or extracted value:** Adjusted intervention effect on door-to-balloon time, 6.18 versus 13.00 with their respective 95% CIs, and on door-to-needle time, 0.40 versus 5.00 with their respective 95% CIs.

**Why context does not resolve it:** The separate β label identifies the final-column parameter, but the shared marginal-effect footnote does not distinguish its underlying estimand/model from the Difference column for either time row. The immediate row supplies minute units and raw medians, which do not identify the analysis producing each adjusted number. The generic percentage heading is a separate obvious unit-label observation and is not the basis of this finding.

**Source-grounded alternatives and missing definitions:** The Difference column might summarize a distinct marginal time effect while the β column reports a conditional quantile coefficient, or the columns might use different quantiles, populations, transformations, or adjustment models. Such distinctions could make both effects meaningful. The supplied text does not name the two row-specific estimands, quantile level, separate models, or any distinct analysis populations. The finding requests that mapping and does not propose a preferred analysis or replacement value.

**Exact human question:** Which estimand, model, units, quantile level (if applicable), adjustment terms, and analysis population generated each of the two adjusted effect columns for door-to-balloon and door-to-needle time, and how should the distinct 6.18 versus 13.00 and 0.40 versus 5.00 contrasts and their confidence intervals be interpreted and extracted?

## Excluded observations

Only apparent issues not emitted are listed. Reconciled checks appear in the relationship records below.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main p.6 Table 2 and p.6 narrative, in-hospital β-blocker; p.7 narrative and p.6 Table 2, discharge β-blocker | In-hospital RD upper limit 8.10 in narrative versus 8.40 in table: half-unit intervals [8.095,8.105] and [8.395,8.405], gap.290/8.40=.03452. Discharge RD 6.63 versus 6.69: intervals [6.625,6.635] and [6.685,6.695], gap.050/6.69=.00747. Discharge OR 1.47 versus 1.48: half-unit intervals touch at 1.475, gap zero. The display-precision rule screens this repeated small copy-difference pattern out. No interval-versus-test conflict is present. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p.5 Table 1, serum creatinine row | Difference and both CI limits printed 0.0. Their half-unit intervals are each [−.05,.05], allowing a nondegenerate underlying interval; the display alone does not establish zero uncertainty. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p.5 Table 1, hemoglobin row | Unit printed mg/dL beside values 13.3 and 13.2. The intended conventional hemoglobin scale is evident in this baseline row; this is an obvious unit-label observation with no conflicting printed value. | NOTATION_OR_TYPOGRAPHY |
| REPORT main p.6 Table 2, two time rows and Difference-column heading | The global Difference heading contains a percent sign although these row labels explicitly give minutes and the final-column footnote identifies β-coefficients. The row units are readily identifiable. This unit observation is separate from the unresolved distinct contrast mapping in F-ST1-001. | NOTATION_OR_TYPOGRAPHY |
| REPORT main pp.6–7 Table 2 footnote b/Table 3 footnote a | Footnotes describe ORs as differences in marginal effects, while the column headings, magnitudes, narrative OR labels and reference group consistently identify ratios and separate percentage-point differences. The isolated wording does not itself create a competing numerical extraction. | TERMINOLOGY_OR_WORDING |
| REPORT main p.3 Statistical Analysis and p.10 Limitations; PLAN protocol p.18 §8.2 | Power target 15,750 cannot be reconstructed uniquely from the report's total, hospitals, five steps, 80% power, 2.4 percentage-point reduction, ICC.05 and loss 5%. The plan supplies baseline MACE probability 10.4% and pre-inflation n = 15,000, but no cluster-period accrual vector or exact power implementation/formula. Absence of these implementation inputs alone is not a reproduced conflict. | CONDITIONAL_OR_UNREPORTED |
| REPORT main pp.3,4,6,7, intention-to-treat, missing outcomes and sensitivity analyses | The primary row includes eligible totals while some 30-day data are incomplete and multiple imputation is discussed as sensitivity. The text does not provide numerical imputation results or a component-level outcome-availability rule. Missing 30-day contact need not remove known in-hospital composite events; no alternative primary estimate is printed to contradict the stated analysis. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p.6 Results troponin comparison; REPORT supplement p.17 eTable 1, troponin row | P < .001 accompanies medians 1.3 versus 4.6, whereas the matched difference 3.3 has 95% CI .1 to 6.5. A diagnostic normal-Wald calculation would use SE=(6.5−.1)/3.92=1.63265, z=2.02125, two-sided P ≈.043; this is only a diagnostic approximation. The source supplies neither the test producing P nor the CI engine, sidedness, or a common estimand. Both outputs reject the null at.05, so no null-inclusion conflict is printed, and a method-specific incompatibility cannot be reproduced without the missing test-to-estimand mapping. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p.9 Discussion, expanded post hoc MACE; main pp.8–9 corresponding results | “Led to a lower rate ” describes the direction of an exploratory composite whose adjusted RD CI crosses zero and OR CI reaches 1.00. The same paragraph says chance is possible and labels the result hypothesis generating; it does not assert statistical significance. | TERMINOLOGY_OR_WORDING |

## Relationship pass records

Each ID was reviewed explicitly. “No supplied test/SE ” is a named limit on mechanical reproduction and is not a finding. For Table 1 continuous/median rows, every IQR and CI is ordered and includes its associated point; raw mean/median differences reconcile after allowing printed inputs their half units. No independent-sample variance formula or median-interval engine is substituted for an unstated source method. For binary baseline rows, count percentages and crude differences were recomputed directly; all intervals include their point estimates. For Table 2/3 and Figure 3, every raw count/percentage is checked with the row-specific population definition, and every modeled estimate is checked against its own CI and stated effect direction. A missing restricted denominator is named rather than inferred.

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

## Scope totals and limitations

Pass 1 main shard: 92 relationships, 92 explicit PASS_1_COMPLETE records, 1 consolidated finding, 9 excluded-observation rows. Direct main coverage includes all baseline/process/primary/secondary/subgroup rows, all 60 Figure 2 estimates and 120 CI endpoints, and source-grounded design/model/decision/outcome/missingness relationships.

Limits: no result-specific P/statistic/SE except the troponin P; no main numerical imputation results; no exact restricted Table 3 process denominators; no exact Figure 2 numerical endpoints or CI algorithm; no complete power implementation or period-accrual inputs. These limits are recorded without substituting methods or omitting relationships. Support shard covers its own 71 relationships and plan-to-report comparisons. No sources or pre-existing artifacts were modified.

---

# Statistical review pass 1 — disjoint support shard

The following artifact is merged without scientific changes. Its original links were rebased from the parts directory to this canonical checker directory. The preserved part remains the primary output of /root/stat1_support.

# Statistical pass 1 — support shard

Runtime agent: `/root/stat1_support`; fresh named statistical reviewer, `gpt-6.1-sol`, reasoning effort `high`. The coordinator records the exact canonical runtime task name returned at spawn using the manifest transport namespace. This artifact is owned only by this support pass-1 agent. Canonical merge must rebase its four-level source links by one level when placing the content directly in `checkers/statistical_pass_1.md`.

Exact assigned scope: S501, S502, S503, S504, S505, S506, S507, S508, S509, S510, S511, S512, S513, S514, S515, S516, S517, S518, S519, S520, S521, S522, S523, S524, S525, S526, S527, S528, S529, S530, S531, S532, S533, S534, S535, S536, S537, S538, S539, S540, S541, S542, S543, S544, S545, S546, S547, S548, S549, S550, S551, S552, S553, S554, S555, S556, S557, S558, S559, S560, S561, S562, S563, S564, S565, S566, S567, S568, S569, S570, S571. This is 71 relationships, disjoint from the main pass-1 shard S001–S092. Supporting count cells in eTables 1–4 and 7 and all eFigure panels were reviewed as implications of these relationships.

Read completely: `QUALITY_CONTROL_SCOPE.md` and `workflow_1_6_2/review_contract.md`. Inputs were the new canonical relationship inventory, current support plan/results evidence maps, main source matching context, tooling record, source inventory, direct-source PDF text and current page images. No earlier candidate, checker, screening, disposition, quality-control report, or external source was used.

## Source authority and calculation boundaries

Roles by content: protocol `joi170166supp1_prod.pdf` and SAP `joi170166supp2_prod.pdf` are PLAN; supplement `joi170166supp3_prod.pdf` pp. 2–16 is PLAN toolkit content, p. 1 and pp. 17–27 are REPORT; the main article is REPORT. Current source-derived images were opened for all results pages 17–24 and 26–27, relevant main methods and SAP subgroup pages, and newly rendered SAP p. 5/protocol p. 9. Native/layout text locates exact source text; cited findings use the exact displayed source values.

Supplemental eTables 1, 2, 5, 6 and 7 state 95% confidence intervals but print no P values, test statistics, standard errors, degrees of freedom, covariance matrices, or variance-estimator definitions. Null values are 0 for differences and residuals and 1 for odds ratios. Point containment, endpoint order and stated direction were checked without inferring model coefficients or sidedness. No noninferiority or equivalence claim/margin is stated. The primary superiority rule is the stated final two-sided .048 level after one interim analysis, not an invented multiplicity rule for all secondary displays. The article's primary nonsignificant result is compatible with this rule.

Fresh auxiliary derivatives use direct Poppler `pdftotext -layout` and `pdftoppm -singlefile -scale-to 1700 -png`, on CPU. Paths: `preprocessing/st1-support/supp3-layout.txt`, `preprocessing/st1-support/main3.txt`, `preprocessing/st1-support/sap5.png`, `preprocessing/st1-support/protocol9.png`. Sources and reused assets were preserved.

## Findings

### F-ST1-501 — LDL difference interval does not reproduce under the calculation reproducing other mean/SD rows

- **Relationships:** S541, with comparison rows S529, S537, S538, S539 and S545.
- **Locations and roles:** REPORT [Supplement 3, physical p. 17, eTable 1](../../../joi170166supp3_prod.pdf#page=17), LDL cholesterol row, the two group headers, and the age, weight, systolic pressure, heart-rate and hemoglobin rows of the same display.
- **Printed values:** complete follow-up n=21,079, LDL mean 122.4 (SD 40.8) mg/dL; missing follow-up n=295, LDL mean 131.4 (SD 46.0) mg/dL; difference 9.0 with 95% CI 3.2 to 14.8 mg/dL. The table gives no LDL-specific contributor counts or CI-method definition.
- **Rule and calculation:** a pooled two-sample mean-difference calculation has `s_p²=((n_C−1)s_C²+(n_M−1)s_M²)/(n_C+n_M−2)` and `SE=s_p sqrt(1/n_C+1/n_M)`. With a 1.96 multiplier, the LDL SE is 2.39649 and the calculated CI is approximately 4.3029 to 13.6971. This is a reproducing-method calculation, not an assertion that the authors used that method. It gives the same display's age CI −1.9897 to 0.7897, weight −2.0140 to 0.2140, systolic pressure −2.9270 to 3.7270 and heart rate 0.8279 to 5.1721, reproducing their printed endpoints; hemoglobin also overlaps after allowing its printed means and SDs their rounding intervals. A pooled t multiplier using the group counts differs negligibly at these sample sizes and leaves the discrepancy unchanged.
- **Display precision:** allow ±0.05 around each mean/SD and, conservatively, ±0.5 around each group n. LDL's recomputed lower endpoint spans 4.19321–4.41253 and upper endpoint spans 13.58747–13.80679. The printed limits allow 3.15–3.25 and 14.75–14.85. The lower gap is at least 0.94321/3.2=0.29475, and the upper gap is at least 0.94321/14.8=0.06373; both exceed 0.05. These are endpoint discrepancies, not a comparison of a modeled estimate with a crude ratio.
- **Focus area:** B and C. **Proposed review domain:** `statistical_results`. **Proposed relationship type / all relationships:** `S_W` / `S_W`.
- **Qualifying route:** Route A, category 4.
- **Affected result or extracted value:** the 95% confidence interval for the baseline LDL difference between missing and complete follow-up groups.
- **Why context does not resolve it:** the method reproduces the other mean/SD rows of the same display, but not this row; category 4 requires registration even when the producing method is unspecified. The table supplies no alternative contributor counts or LDL-specific CI construction to resolve the printed interval.
- **Alternatives / missing definitions:** LDL could have fewer observed values than the displayed group totals, or a different interval procedure could have been used for LDL. Either could explain the wider interval, but the corresponding counts and procedure are absent. This is not a request to adopt a preferred procedure.
- **Exact human question:** What complete- and missing-follow-up LDL contributor counts and confidence-interval procedure produced 9.0 mg/dL (95% CI, 3.2–14.8), given that the pooled calculation with the displayed group totals reproduces the other mean/SD rows but yields approximately 4.30–13.70 for LDL?

### F-ST1-502 — Reported in-hospital medication composite omits the planned statin component

- **Relationships:** S512 and S521; affected modeled results S554 and S564.
- **Locations and roles:** PLAN [SAP p. 5, §6.1.2, lines 1149–1151](../../../joi170166supp2_prod.pdf#page=5); REPORT [main article p. 3, Outcomes](../../../jama_huffman_2018_oi_170166.pdf#page=3), [p. 7, Table 3 optimal in-hospital medication and footnote c](../../../jama_huffman_2018_oi_170166.pdf#page=7); REPORT [Supplement 3 p. 21, eTable 5 footnote c](../../../joi170166supp3_prod.pdf#page=21) and [p. 22, eTable 6 footnote b](../../../joi170166supp3_prod.pdf#page=22).
- **Printed values / statements:** SAP defines optimal in-hospital use by five components: aspirin, ADP receptor antagonist, heparin, statin and beta blocker. Main Outcomes defines four components, aspirin, ADP antagonist, anticoagulant and beta blocker, and explicitly says in-hospital statin was predefined but data were not collected. Table 3 shows 3122 (31.7%) control versus 3878 (35.8%) intervention, primary OR 1.45 (1.28–1.64), for the four-component definition. eTable 5 likewise omits statin; eTable 6 lists aspirin, ADP antagonist, heparin and beta blocker.
- **Rule and logical calculation:** the planned all-component endpoint requires meeting five drug criteria, while the reported endpoint requires four. Removing statin changes both the composite event condition and eligibility to receive every component. The provided report acknowledges the missing collection but does not supply a result for the planned composite. No arithmetic correction or preferred analysis is proposed; display precision is not applicable to this set-membership difference.
- **Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship type / all relationships:** `P_R` / `P_R`.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** the optimal in-hospital medication event rates and adjusted odds ratios, and whether the extracted endpoint includes statin.
- **Why context does not resolve it:** category 5 expressly includes changes in a prespecified composite definition. Disclosure of noncollection explains why one component is absent but does not make the four-component endpoint the same quantity as the planned five-component endpoint.
- **Alternatives / missing definitions:** a prospective amendment could have changed the composite after the supplied SAP; alternatively, the reported definition is a disclosed adaptation caused by noncollection. No supplied amendment establishes its timing or the corresponding eligibility definition.
- **Exact human question:** Was optimal in-hospital medication use prospectively redefined to omit statin, and what amendment and eligibility rule should accompany extraction of the four-component rates and modeled results rather than the five-component endpoint in the supplied SAP?

### F-ST1-503 — Expanded MACE is a planned secondary objective but reported as post hoc

- **Relationships:** S504 and S567, matching main S091.
- **Locations and roles:** PLAN [protocol p. 9, §2.2.3, lines 259–263](../../../joi170166supp1_prod.pdf#page=9); PLAN [SAP pp. 2–3, §2.1.2, lines 1071–1074](../../../joi170166supp2_prod.pdf#page=3); REPORT [main p. 3, Outcomes and Statistical Analysis](../../../jama_huffman_2018_oi_170166.pdf#page=3), [p. 8, Secondary and Post Hoc Analyses](../../../jama_huffman_2018_oi_170166.pdf#page=8), [p. 9, continuation/discussion](../../../jama_huffman_2018_oi_170166.pdf#page=9); REPORT [Supplement 3 p. 23, eTable 7 title and first row](../../../joi170166supp3_prod.pdf#page=23).
- **Printed values / statements:** protocol and SAP place evaluation of intervention effects on in-hospital and 30-day expanded MACE under secondary objectives. The main report calls expansion by incident in-hospital heart failure, cardiogenic shock and cardiac arrest a post hoc analysis. eTable 7 calls it exploratory and reports 919 (9.1%) control versus 795 (7.0%) intervention; primary-model difference −1.34% (−2.72 to 0.04) and OR 0.84 (0.70–1.00).
- **Rule and logical calculation:** the supplied plan contains a secondary expanded-MACE objective before the reported analysis, whereas the report characterizes the expanded-MACE analysis as post hoc. The plan does not define the expanded components; consequently it does not establish whether the report's specific expansion equals the planned expansion or replaces it. This reproduced status/definition contrast must be registered under category 5. Display precision is inapplicable to prespecification status.
- **Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship type / all relationships:** `P_R` / `P_R`.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** prespecification and outcome status for the expanded-MACE counts, risk difference and odds ratio.
- **Why context does not resolve it:** category 5 covers prespecified outcome-status changes. The report's post hoc label and the plan's secondary objective coexist, but the supplied sources do not define the distinction between their expanded composites.
- **Alternatives / missing definitions:** the broad objective may have anticipated a different expanded endpoint and the report's particular component set may truly have been selected post hoc; alternatively, the same endpoint was already planned. The component definition and dated analysis specification are missing from the supplied plan.
- **Exact human question:** Does eTable 7's MACE-plus-heart-failure/shock/arrest composite implement the secondary expanded-MACE objective in the supplied protocol/SAP, or is it a distinct post hoc composite, and what prospective definition and outcome status should be used in extraction?

### F-ST1-504 — The reported prespecified subgroup set differs from the supplied subgroup plan

- **Relationships:** S513 and S520, matching main Figure 3 relationships.
- **Locations and roles:** PLAN [SAP p. 7, §7.5.2, lines 1243–1254](../../../joi170166supp2_prod.pdf#page=7) and [p. 5, §6.1.3](../../../joi170166supp2_prod.pdf#page=5); REPORT [main p. 3, Statistical Analysis](../../../jama_huffman_2018_oi_170166.pdf#page=3) and [p. 9, Figure 3 and accompanying subgroup narrative](../../../jama_huffman_2018_oi_170166.pdf#page=9). The supplied protocol and complete SAP were searched/read for an additional hospital-type or revised age subgroup specification; none is supplied.
- **Printed values / statements:** SAP lists a priori primary-endpoint subgroups: hospital size, use of toolkit components, age <65 and >65, sex, and STEMI/NSTEMI. The report describes age, sex, STEMI/NSTEMI, hospital size and hospital type as prespecified. Figure 3 instead divides age into <50, 50–69 and ≥70; adds government/nonprofit/private hospital groups with ORs 0.90 (0.61–1.33), 0.91 (0.59–1.40), and 1.16 (0.82–1.64); and supplies no toolkit-use subgroup result. Main p. 3 states the concurrent process evaluation will be reported separately, but does not identify the planned primary-outcome toolkit-use subgroup as deferred.
- **Rule and logical calculation:** compare the explicitly listed prospective subgroup partitions with the reported set called prespecified: the age partition changes, hospital type is added without a corresponding supplied prespecification, and toolkit-use effect heterogeneity is not reported. These form one subgroup-specification pattern. The <65/>65 equality boundary alone is not the observation. Display precision cannot equate the <65/>65 partition with <50/50–69/≥70.
- **Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship type / all relationships:** `P_R` / `P_R`.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** prespecification of the primary MACE age and hospital-type subgroup results, and availability of the planned primary MACE toolkit-use subgroup analysis.
- **Why context does not resolve it:** category 5 always registers an analysis called prespecified that the supplied plan does not contain and a planned primary analysis not reported. An unspecified separate process-evaluation publication does not establish whether these specific primary-outcome subgroup changes were prospective.
- **Alternatives / missing definitions:** a later dated analysis specification may establish the three age bands and hospital type and defer or replace toolkit use. Alternatively, the reported subgroup descriptions may refer to a different prospective source. That source and its timing are not supplied.
- **Exact human question:** Which dated prospective specification establishes Figure 3's age bands and hospital-type subgroup as prespecified, and where is the SAP's primary-MACE subgroup analysis by use of toolkit components reported or documented as replaced/deferred?

### F-ST1-505 — Residual sign definition reverses hospital-rate direction between the index and caption

- **Relationships:** S568 and S569.
- **Locations and roles:** REPORT [Supplement 3 p. 1, eFigure 1A index entry](../../../joi170166supp3_prod.pdf#page=1), and REPORT [p. 24, eFigure 1A axis/points and final caption sentence](../../../joi170166supp3_prod.pdf#page=24).
- **Printed values / statements:** index calls the quantity residual of 30-day MACE rate “Expected – Observed.” Figure p. 24 puts negative residuals on the left and positive residuals on the right; caption says the left-hand side depicts hospitals with MACE below the mean and the right-hand side hospitals above the mean. It describes the residuals as hospital-level departures from the mean (residual=0). The plotted axis includes −3, −2, −1, 0, 1 and 2.
- **Rule and logical calculation:** for the printed index contrast `r=Expected−Observed`, a hospital above the expected/mean rate has r<0, whereas the caption assigns above-mean hospitals to the positive right-hand side. Conversely, below-mean observed rates yield r>0 under the index formula but occupy the negative left-hand side under the caption. This is a direction reversal, not a residual magnitude reconstructed from pixels. Rounding cannot reverse the signs of the clearly nonzero plotted points; no imprecise graph digitization is used.
- **Focus area:** B. **Proposed review domain:** `statistical_results`. **Proposed relationship type / all relationships:** `S_W` / `S_W`.
- **Qualifying route:** Route A, category 2.
- **Affected result or extracted value:** the direction of the hospital departures in the MACE residual display and whether a positive residual represents above- or below-expected MACE.
- **Why context does not resolve it:** category 2 covers direction/reference definitions reversing printed values. The index supplies one subtraction order and the caption supplies the opposite association between residual sign and hospital rates. Choosing the caption as authoritative leaves the printed index definition unresolved.
- **Alternatives / missing definitions:** the graph may depict a hospital random effect or predicted-minus-mean residual rather than the expected-minus-observed quantity in the index. Alternatively, the subtraction order may differ from the caption's interpretation. The exact residual formula/scale is not supplied.
- **Exact human question:** What residual formula and subtraction order generated eFigure 1A, and does a positive residual denote higher or lower hospital MACE than expected, given the index's Expected−Observed label and the caption's opposite sign interpretation?

## Relationship completion records

Every row below records the full assigned relationship as `PASS_1_COMPLETE`, including checks for count, denominator, estimate/test, method and matched-source implications wherever applicable. A finding is referenced without assigning adjudication. “No printed conflict” does not claim unavailable model internals were reproduced.

| S ID | Pass 1 status | Checks and source-grounded outcome |
|---|---|---|
| S501 | PASS_1_COMPLETE | Five-cohort stepped-wedge schedule, random hospital effects and fixed periods match reported design. SAP's four-period sentence is separately excluded; no observed allocation or primary analysis conflict is established. |
| S502 | PASS_1_COMPLETE | Primary 30-day MACE components/GUSTO definition match main primary outcome and supplemental clinical labels; death versus all-cause death is resolved by definitions. |
| S503 | PASS_1_COMPLETE | Listed mortality, reinfarction, stroke, GUSTO bleeding and process secondary outcomes match report displays; in-hospital medication component implication is F-ST1-502. |
| S504 | PASS_1_COMPLETE | Expanded-MACE status comparison is F-ST1-503. Substudy outcomes are not identified as key secondary and omitted substudy results alone do not establish a qualifying primary/key-secondary omission. |
| S505 | PASS_1_COMPLETE | Follow-up definitions read including protocol's Discharge Date+30 Days diagram; report does not supply a conflicting explicit admission-versus-discharge follow-up origin. No origin was inferred from convention. |
| S506 | PASS_1_COMPLETE | Adult STEMI/NSTEMI eligibility, consent and analysis-population definitions reviewed; no contradictory report population rule found. |
| S507 | PASS_1_COMPLETE | Withdrawal/loss definitions compared with 295 missing outcomes; 215 not followed and 80 unreachable sum to 295, without inferring cause distributions absent from the plan. |
| S508 | PASS_1_COMPLETE | SAE definitions and expected clinical event capture distinguish safety from primary composite; no printed contradiction in stated surveillance cadence or reported safety decision. |
| S509 | PASS_1_COMPLETE | One one-year safety/efficacy interim and DSMB stop/continue role match article's 12-month interim. No numerical interim result or stopping recommendation is supplied for reproduction. |
| S510 | PASS_1_COMPLETE | Planned 15,000/15,750, ICC .05, alpha .05, power 80%, baseline 10.4%, difference 2.4 percentage points match reported assumptions. Inflation and unavailable per-period inputs appear once in exclusions; no formula was invented. |
| S511 | PASS_1_COMPLETE | Central computer-generated size-stratified randomization matches article. Notification lead-time difference is peripheral; no changed randomized comparison or decision rule established. |
| S512 | PASS_1_COMPLETE | Discharge drug composite matches. Five-component in-hospital definition versus four-component reported definition is F-ST1-502. |
| S513 | PASS_1_COMPLETE | Toolkit measurement/implementation and effect-modification plan reviewed; primary-outcome toolkit-use subgroup implication is F-ST1-504. Process evaluation publication itself is explicitly deferred. |
| S514 | PASS_1_COMPLETE | >80% medication-concordance/2,200 substudy definitions reviewed; no matching published value is supplied and these are not designated key secondary. No inferential mismatch manufactured. |
| S515 | PASS_1_COMPLETE | ITT allocation by randomized exposure and hospital random effects agree with report. Missing follow-up sensitivity descriptions considered jointly with S516; complete/missing 21,079+295=21,374. |
| S516 | PASS_1_COMPLETE | Three-call rule and planned complete-case/multiple-imputation sensitivity agree with report descriptions; report says results similar but supplies no imputed OR for a numerical reproduction. |
| S517 | PASS_1_COMPLETE | All baseline cells and count/percentage pairs in eTables 1, 3, 4 checked; 12, 60 and 36 pairs respectively reconcile with the display-precision rule. No denominator or dispersion conflict established. |
| S518 | PASS_1_COMPLETE | Primary mixed logistic, random hospital, fixed four-month periods match article/eTable 7 primary-model footnote. Supplemental sensitivity models remain separately identified. |
| S519 | PASS_1_COMPLETE | GRACE covariate sensitivity matches main covariate list and all eTable 5 GRACE model rows; creatinine availability does not establish undisclosed imputation in that model. |
| S520 | PASS_1_COMPLETE | All reported subgroup partitions/models compared with explicit SAP set; changes and missing toolkit-use result consolidated in F-ST1-504. |
| S521 | PASS_1_COMPLETE | Mixed-logistic secondary clinical outcome models agree with source labels; medication composite implication is F-ST1-502. Secondary exploratory interpretation does not by itself remove their explicit secondary-outcome labels. |
| S522 | PASS_1_COMPLETE | Substudy and SAE reporting plans read; no specific conflicting reported result, analysis set or decision supplied. General absence of these non-key-secondary results is excluded. |
| S523 | PASS_1_COMPLETE | O'Brien–Fleming interim/final thresholds match article: z2.797/.005 and z1.977/.048. Gaussian conversion differences are within displayed alpha intervals; no incompatible interim or final conclusion supplied. |
| S524 | PASS_1_COMPLETE | Semiannual safety reviews and at-least-annual DSMB plan are compatible with described one-year analysis; no additional inference or stopping result supplied. |
| S525 | PASS_1_COMPLETE | R3M/percentiles/boxplot definitions apply to operational audit examples, not inferential 95% CIs; no trial-result comparison made. |
| S526 | PASS_1_COMPLETE | Opportunity composites have source-defined 11 AMI/STEMI, 8 NSTEMI and 6 discharge items. These are separate operational measures, not the MACE or optimal-drug composite. |
| S527 | PASS_1_COMPLETE | Process timing/eligibility definitions checked against main process outcomes; source allows measure-specific denominators, and no conflicting printed threshold producing a result found. |
| S528 | PASS_1_COMPLETE | Admission/discharge checklist eligibility flags are coherent with excluding contraindications in main process measures; no preferred clinical regimen or method proposed. |
| S529 | PASS_1_COMPLETE | Age difference −.6 within ordered −2.0,.8; pooled mean/SD interval reproduces endpoints; no P printed. |
| S530 | PASS_1_COMPLETE | Male counts 15973/21079 and 210/295 reproduce proportions and −4.5904 percentage-point difference; unpooled binary Wald CI −9.7909,.6101 matches −9.8,.6. |
| S531 | PASS_1_COMPLETE | Tobacco counts/proportions reproduce 11.6 difference and ordered 5.9,17.3 interval; no contradictory test printed. |
| S532 | PASS_1_COMPLETE | Diabetes counts/proportions reproduce .7 difference and ordered −5.0,6.4 interval; null included; no test supplied. |
| S533 | PASS_1_COMPLETE | Transfer counts/proportions reproduce 5.2 difference and ordered −.5,10.9 interval; null included; no test supplied. |
| S534 | PASS_1_COMPLETE | Insurance counts/proportions reproduce 1.9 difference and ordered −3.1,6.9 interval; null included; no test supplied. |
| S535 | PASS_1_COMPLETE | STEMI counts/proportions reproduce −4.8 difference and ordered −10.4,.9 interval; null included; no test supplied. |
| S536 | PASS_1_COMPLETE | Median-based 21 difference can be obtained within 246/266 half-unit intervals; 21 lies in −38,80. No median-interval method inferred from IQRs. |
| S537 | PASS_1_COMPLETE | Weight −.9 within −2.0,.2; pooled mean/SD calculation reproduces CI. |
| S538 | PASS_1_COMPLETE | SBP .4 within −2.9,3.7; pooled mean/SD calculation reproduces CI, unlike an automatically assumed Welch procedure. |
| S539 | PASS_1_COMPLETE | Heart rate 3.0 within .8,5.2; pooled mean/SD interval reproduces. No P supplied; no conflicting statement of nonsignificance specifically tied to this interval. |
| S540 | PASS_1_COMPLETE | Troponin 3.3 within .1,6.5, direction matches missing minus complete medians. Main P<.001 and CI both exclude null at .05; Gaussian quantitative P reconstruction is only a diagnostic and cannot establish equality with an unstated median/rank test. |
| S541 | PASS_1_COMPLETE | LDL estimate 9.0 is inside ordered CI, but printed CI differs from same-display reproducing mean/SD calculation beyond display precision: F-ST1-501. |
| S542 | PASS_1_COMPLETE | Triglyceride medians reproduce 7 difference; ordered −3,17 contains 7; no confidence construction inferred from IQRs. |
| S543 | PASS_1_COMPLETE | Creatinine displayed medians 1.0/1.0 permit .1 difference within half-unit intervals; ordered −.2,.3 contains .1. |
| S544 | PASS_1_COMPLETE | Glucose medians reproduce 1 difference; ordered −6,8 contains 1; no unspecified quantile method reconstructed. |
| S545 | PASS_1_COMPLETE | Hemoglobin 0.0 inside −.3,.2; mean/SD calculation overlaps endpoints after mean rounding; printed unit issue excluded as notation. |
| S546 | PASS_1_COMPLETE | All 17 modeled differences and all 34 arm estimates are inside ordered CIs; direction agrees with marginal intervention-minus-control values after precision. Modeled-versus-crude contrast excluded. No P/test supplied; covariance not invented. |
| S547 | PASS_1_COMPLETE | All four MACE ORs inside ordered CIs, all include 1; matched main primary model distinguished from additional GRACE/transfer/insurance/aspirin adjustments. |
| S548 | PASS_1_COMPLETE | All four 30-day mortality ORs inside ordered CIs including 1; no P or significance conflict. |
| S549 | PASS_1_COMPLETE | All four cardiovascular mortality ORs inside ordered CIs including 1; similarity to all-cause rows alone supplies no contradiction. |
| S550 | PASS_1_COMPLETE | All four in-hospital mortality ORs inside ordered CIs including 1; no test supplied. |
| S551 | PASS_1_COMPLETE | All four reinfarction ORs inside ordered CIs including 1; model contrast consistently intervention/control. |
| S552 | PASS_1_COMPLETE | All four stroke ORs inside ordered CIs including 1; direction changes among adjustment models are allowed by distinct model definitions. |
| S553 | PASS_1_COMPLETE | All four GUSTO bleeding ORs inside ordered CIs including 1; wide intervals alone do not contradict sparse-event model results. |
| S554 | PASS_1_COMPLETE | All four in-hospital medication ORs inside ordered CIs excluding 1 above; no P. Endpoint-component change F-ST1-502. |
| S555 | PASS_1_COMPLETE | All four discharge medication ORs inside ordered CIs excluding 1 above; definition includes statin as planned. |
| S556 | PASS_1_COMPLETE | All four tobacco-advice ORs inside ordered CIs including 1; distinct covariate adjustment explains different point directions without a source conflict. |
| S557 | PASS_1_COMPLETE | MACE OR1.14 inside .76,1.70, null included; time-exposure interaction model distinguished from primary model; no interaction coefficient inferred. |
| S558 | PASS_1_COMPLETE | Mortality OR.98 inside .63,1.52, null included; no P/test supplied. |
| S559 | PASS_1_COMPLETE | Cardiovascular mortality OR1.00 inside .64,1.56; no P/test supplied. |
| S560 | PASS_1_COMPLETE | In-hospital mortality OR1.43 inside .83,2.46; no P/test supplied. |
| S561 | PASS_1_COMPLETE | Reinfarction OR2.81 inside .79,9.94; no P/test supplied. |
| S562 | PASS_1_COMPLETE | Stroke OR2.06 inside .58,7.36; no P/test supplied. |
| S563 | PASS_1_COMPLETE | GUSTO bleeding OR2.53 inside .50,12.94; no P/test supplied. |
| S564 | PASS_1_COMPLETE | In-hospital medication OR.87 inside .70,1.07, null included; different model from eTable 5 so direction not equated; component change F-ST1-502. |
| S565 | PASS_1_COMPLETE | Discharge medication OR1.45 inside 1.12,1.88, null excluded above; no contrary printed significance assertion. |
| S566 | PASS_1_COMPLETE | Tobacco advice OR.99 inside .37,2.66, null included; no P/test supplied. |
| S567 | PASS_1_COMPLETE | All 16 eTable 7 RD/OR point estimates inside ordered intervals; directions match within each stated model; all eight n/% pairs reconcile with 10066/11308. Expanded status F-ST1-503. Cluster OR upper1.00 vs RD upper−.01 has compatible rounding and no P/test, separately excluded. |
| S568 | PASS_1_COMPLETE | All visible hospital points contained in respective ordered bars; stated CI/nonzero rule is coherent. Cross-location residual direction discrepancy consolidated with S569 in F-ST1-505. Exact coefficients/IDs are absent; no decimal digitization substituted. |
| S569 | PASS_1_COMPLETE | Source index Expected−Observed definition compared with eFigure 1A plotted sign and caption: F-ST1-505. |
| S570 | PASS_1_COMPLETE | Every cohort×step MACE panel inspected; points/rates within 0–100%, visible CI segments contain points, open-to-filled crossover matches five-cohort schedule. No exact hospital events/Ns or confidence formula supplied. |
| S571 | PASS_1_COMPLETE | Every cohort×step mortality panel inspected with same checks; rates remain no greater than corresponding graphical MACE rates where recognizable. No exact decimal/statistical test inferred from pixels. |

## Additional reconciliation details

The six binary eTable 1 contrasts reproduce under the unpooled proportion-difference normal formula using their printed integer counts. This differs appropriately from the mean/SD calculation. All count-percent pairs in eTables 1, 3 and 4 reconcile after rounding (12+60+36=108 pairs), and all eight eTable 7 pairs reconcile. eTable 3's control counts sum to 10,066 and intervention counts to 11,308; paired step totals match eTable 4's 2,915, 3,311, 3,516, 3,854, 4,043 and 3,735, totaling 21,374. Every continuous mean/SD and median/IQR cell in eTables 3–4 was checked for nonnegative dispersion and ordered IQRs containing medians. Weighted means may depend on row-specific available observations; none were assumed for clinical measurements. Matching labels establish these tables as descriptive data, whereas eTable 2 explicitly uses marginal effects from logistic/linear/quantile models.

Log-symmetry checks for eTables 5–6 are diagnostics only: the ORs are approximately geometric centers of their CIs, and no point-outside-interval or endpoint reversal appears. No covariance, variance estimator, exact degrees of freedom, exposure coding, or interaction estimand was inferred. eTable 7's RD and OR are separately defined transformations and confidence calculations; null-boundary printing is not a supplied P value or stated test.

## Excluded observations

This table contains only apparent issues considered and not emitted, each once with exactly one reason code. Reconciled routine checks are recorded above instead.

| Location | Observation | Reason code |
|---|---|---|
| PLAN SAP p. 4 §5 vs p. 3 schedule | Randomization text says four time periods, but five switches and five cohorts are explicit in the immediate design/schema; no changed allocation or primary decision rule is shown. | CONTEXT_RESOLVES |
| PLAN SAP p. 4 sample inflation, protocol p. 18 | 15,000 divided by .95 is 15,789.47 rather than 15,750; the ~0.25% difference and displayed 5% input interval fall within the display-precision rule. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN sample-size paragraphs | Exact 80% stepped-wedge power cannot be recomputed without anticipated cluster-by-period sizes, their variability and the calculation implementation; no reproduced conflicting power result is supplied. | CONDITIONAL_OR_UNREPORTED |
| PLAN SAP p. 4 notification vs REPORT main p. 2 | Three-week planned versus two-week reported site notification changes an operational lead time, without a demonstrated outcome, analysis-population or decision-rule implication. | PERIPHERAL_COMPARISON |
| REPORT eTable 1 p. 17 footnote a | Intervention-minus-control terminology is attached to complete/missing follow-up columns; all displayed differences identify missing-minus-complete directly, resolving the intended comparison. | TERMINOLOGY_OR_WORDING |
| REPORT eTable 1 troponin CI and main p. 6 P<.001 | A Gaussian diagnostic from 3.3 and CI .1–6.5 suggests a different numerical P, but no common test or median-CI convention is supplied; both printed summaries exclude the null at .05 and the display does not establish a shared quantitative test. | CONDITIONAL_OR_UNREPORTED |
| REPORT eTables 1–4 hemoglobin unit | The printed mg/dL label for values near 13 is a unit-notation slip whose reading is evident; no numerical blood concentration disagreement is established. | NOTATION_OR_TYPOGRAPHY |
| REPORT eTable 2 p. 18 vs crude main baseline values | Marginal effects adjusted for hospital clustering/time differ from crude descriptive summaries; the source explicitly distinguishes the analyses. | MODEL_VERSUS_CRUDE |
| REPORT eTable 2 p. 18 footnote; eTable 6 p. 22 title | Row-specific model family, covariance construction, and time-exposure interaction coding/estimand are not fully printed; missing details alone do not conflict with a printed value or stated result. | CONDITIONAL_OR_UNREPORTED |
| REPORT eTable 7 p. 23 cluster expanded MACE row | RD CI upper−.01 excludes 0 while OR CI upper1.00 can round from below1; no P/test conflicts, and differently transformed interval boundaries can reconcile within display precision. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p. 3 secondary analyses vs PLAN secondary labels | Report still identifies the same secondary outcomes, while describing their unadjusted-for-multiplicity analyses as exploratory; this is an inferential caveat rather than an observable outcome-hierarchy change. | TERMINOLOGY_OR_WORDING |
| PLAN substudy/concordance/SAE plans vs REPORT | General absence of separate non-key-secondary substudy or safety summaries is not a reproduced conflicting primary/key-secondary result or decision rule; no specific qualifying omission identified. | OUT_OF_FOCUS |
| PLAN SAP p. 8 and REPORT main p. 3 z/alpha boundaries | Diagnostic two-sided Gaussian conversions of z2.797 (~.00516) and z1.977 (~.04804) are inside the printed alpha half-unit intervals; no supplied interim result or final conclusion conflicts. | ROUNDING_OR_DISPLAY_PRECISION |

## Limitations and handoff

All 71 assigned relationships have explicit `PASS_1_COMPLETE` records. Five findings are emitted (F-ST1-501 through F-ST1-505); 13 apparent observations are excluded once. All findings require the independent inclusion screen before candidate registration. No severity, acceptance, correction or adjudication is assigned.

Reproduction is limited by absent row-specific assay contributor counts, unpublished model internals and absence of exact hospital graph numbers/identifiers. Those limitations did not truncate coverage. Method diagnostics are identified as diagnostics or same-display reproducing checks rather than replacements for the reported analysis. No fresh OCR was required; exact candidate pages have usable current native text and direct visual confirmation.
