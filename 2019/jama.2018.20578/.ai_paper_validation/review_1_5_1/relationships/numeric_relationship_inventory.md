# Canonical Numeric Relationship Inventory

## Scope and identification

This is the complete numeric/reporting inventory for the assigned 1.5.1 numeric-review lane. It merges the 60 main-paper records `MN001` through `MN060` and the 8 support-source records `SN001` through `SN008` without treating topic similarity as identity. Canonical IDs are stable within this inventory. Direct PDF pages are the authority; extraction artifacts are retained provenance and a locator only.

The inventory contains 68 canonical `N` relationships. `N001` through `N060` retain one-to-one provenance from `relationships/parts/main_numeric_relationships.md`; `N061` through `N068` retain one-to-one provenance from `relationships/parts/support_numeric_relationships.md`. All mapped inferential relationships were also considered when they supplied a numeric, denominator, unit, rounding, or label check; their `MS`/`SS` cross-references are recorded below.

| Canonical ID | Shard provenance | Exact direct source location(s) | Printed relationship / inputs retained | Numeric consistency coverage |
|---|---|---|---|---|
| N001 | MN001 | DOC-001 pp. 1-2 | 36-week trial; 4 centers; acute treatment up to 12 weeks; 8-week qualifying period; November 2011-June 2017; follow-up June 13, 2017. | Repeated design/time values agree. |
| N002 | MN002 | DOC-001 pp. 2-3 | Three phases; acute age 18-85; 8-week stabilization; randomization requires MMSE at least 24. | Phase and population labels are compatible. |
| N003 | MN003 | DOC-001 pp. 1-2 | Sertraline 150-200 mg/d in 50-mg pills; olanzapine 15-20 mg/d in 5-mg pills; randomized medians 150 and 15 mg/d. | Dose, pill-strength, and median/IQR labels agree. |
| N004 | MN004 | DOC-001 pp. 1, 4 | Allocations 64 and 62; 1:1 blocks 4-8; age/remission/site strata; 4-week taper. | Allocation total is 126 and matches design labels. |
| N005 | MN005 | DOC-001 p. 1 | 126 randomized; mean age 55.3 (SD 14.9); 78 women (61.9%). | 78/126 = 61.90%, compatible after one-decimal rounding. |
| N006 | MN006 | DOC-001 p. 1; Fig. 1 p. 3 | 114/126 (90.5%) completed. | 114/126 = 90.48%; branch-state reconciliation checked with N019-N020. |
| N007 | MN007 | DOC-001 pp. 1, 2, 6 | Relapse 13 (20.3%) and 34 (54.8%); results specify 13/64 and 34/62. | Both percentages reconcile and all repeated values agree. |
| N008 | MN008 | DOC-001 p. 1; MS006 p. 7; Table 4 p. 8 | Eight abstract daily-rate estimates and CIs, including HbA1c -0.0002 mg/dL. | Estimates/intervals match MS006; HbA1c unit is separately proposed for human review. |
| N009 | MN009 | DOC-001 p. 2 | HDRS at least 21; delusion at least 3; conviction at least 2; IQCODE at least 4; 3-month exclusion. | Threshold and time labels are internally coherent. |
| N010 | MN010 | DOC-001 pp. 2-3 | Full remission HDRS at most 10 for 2 weeks; near remission HDRS 11-15 and at least 50% reduction after 12 weeks. | Categories are distinct and correctly bounded. |
| N011 | MN011 | DOC-001 pp. 1, 4 | Relapse primary outcome; specified metabolic outcomes; repeated-measure schedule. | Outcome identities and frequency labels agree. |
| N012 | MN012 | DOC-001 p. 4 | Weekly visits for 8 weeks then every 4 weeks to week 36; four alternative relapse criteria. | Schedule and endpoint conditions are not numerically contradictory. |
| N013 | MN013 | DOC-001 pp. 4, 6 | Simpson-Angus 0-40 narrative/0-36 table; Barnes 0-5; AIMS item 0-5/global 0-4. | Different total/item/global constructions explain distinct ranges; no merged-scale error established. |
| N014 | MN014 | DOC-001 p. 4 | UKU 0-3 on 48 items; adverse-effect and >7% weight thresholds. | Definitions use compatible scales and directions. |
| N015 | MN015 | DOC-001 p. 4; MS012 | Planned n=176, 80% power, 20% risk difference, up to 15% attrition; revised n=128. | Calculation inputs are incomplete; no unsupported reconstruction made. |
| N016 | MN016 | DOC-001 Fig. 1 p. 3 | 350 - 81 = 269; 269 - 74 = 195; 195 - 33 = 162. | Every displayed flow subtraction reconciles. |
| N017 | MN017 | DOC-001 Fig. 1 p. 3 | Acute discontinuations 31+21+7+5+1+9 = 74. | Component sum reconciles. |
| N018 | MN018 | DOC-001 Fig. 1 p. 3 | Stabilization discontinuations 4+2+1+1+7 = 15; 162-15=147; 147-21=126. | Component and phase totals reconcile. |
| N019 | MN019 | DOC-001 Fig. 1 p. 3 | Olanzapine: 64 = 43 remission/near remission + 13 relapse + 8 discontinued. | Branch total, received-treatment, and ITT labels reconcile. |
| N020 | MN020 | DOC-001 Fig. 1 p. 3 | Placebo: 62 = 24 remission/near remission + 34 relapse + 4 discontinued. | Branch total, received-treatment, and ITT labels reconcile. |
| N021 | MN021 | DOC-001 Table 1 p. 5 | Age mean/SD and 36+28=64; 36+26=62. | Counts and one-decimal percentages reconcile. |
| N022 | MN022 | DOC-001 Table 1 p. 5 | Men/women 27+37=64 and 21+41=62. | Counts and percentages reconcile. |
| N023 | MN023 | DOC-001 Table 1 p. 5 | Race 54+6+4=64 and 49+9+4=62; Hispanic is a separate attribute. | Race totals reconcile; ethnicity is not incorrectly summed with race. |
| N024 | MN024 | DOC-001 Table 1 p. 5 | Marital categories total 64 and 62. | Subgroup sums and percentages reconcile within rounding. |
| N025 | MN025 | DOC-001 Table 1 p. 5 | Living categories total 64 and 60; education is continuous. | Placebo living rows total 60, leaving two unreported/missing rather than a falsely exhaustive labeled total. |
| N026 | MN026 | DOC-001 Table 1 p. 5 | Site counts 16+15+9+24=64 and 15+14+10+23=62. | Site totals and percentage rounding reconcile. |
| N027 | MN027 | DOC-001 Table 1 p. 5 | Episode counts; medians with stated n=60,62,61. | Denominators are explicitly measure-specific; no total identity is imposed. |
| N028 | MN028 | DOC-001 Table 1 p. 5 | Suicide attempt and treatment-resistance counts/percentages. | Numerators and arm denominators reconcile. |
| N029 | MN029 | DOC-001 Table 1 p. 5 | Hyperlipidemia 18 (29.0) under n=64 and 19 (29.7) under n=62; hypertension and diabetes counts/percentages. | Hyperlipidemia does not reconcile within arms and exactly matches opposite-arm denominators; separately registered for human review. Other diagnosis percentages reconcile. |
| N030 | MN030 | DOC-001 Table 1 p. 5 | Premorbid weight means, SDs, n=60/59, lb-to-kg factor 0.45. | Unit/conversion label is coherent. |
| N031 | MN031 | DOC-001 Table 2 p. 6 | HDRS means; delusion and hallucination 64/64 and 62/62 (100%). | Full-arm counts and scale ranges reconcile. |
| N032 | MN032 | DOC-001 Table 2 p. 6 | HADS/CORE/CIRS-G medians/IQRs, placebo HADS n=61. | Measure-specific missingness is explicit. |
| N033 | MN033 | DOC-001 Table 2 p. 6 | MMSE and DKEFS means/SDs with n=61/59 and 60/58. | Scale labels and partial denominators are coherent. |
| N034 | MN034 | DOC-001 Table 2 p. 6 | Barnes 3.0 (4.7), 2.0 (3.2); AIMS 2.0 (3.1), 2.0 (3.2); Simpson-Angus medians. | Decimal-formatted integer counts yield the printed percentages; formatting alone is not a numeric contradiction. |
| N035 | MN035 | DOC-001 Table 2 p. 6 | Both arms: sertraline 150 (150-200), olanzapine 15 (10-20) mg/d. | Cross-table dose values agree with N003. |
| N036 | MN036 | DOC-001 pp. 4, 6 | Conversion factors and movement-scale labels. | Unit/scale checks completed; see N013 for range interpretation. |
| N037 | MN037 | DOC-001 pp. 6-7; MS002-MS003 | Treatment and covariate HR/CI/P vector. | Containment/order and matched repeat checks completed; no numeric conflict in this vector. |
| N038 | MN038 | DOC-001 Table 3 p. 7 | Relapse-event-type counts by arm; footnote permits more than one event. | Counts are not required to equal relapse totals because the footnote explicitly makes them nonexclusive. |
| N039 | MN039 | DOC-001 Fig. 2 p. 7 | At-risk series, 36-week and 19.5-week median observation. | At-risk declines and branch totals are compatible; censoring reasons are not fully printed. |
| N040 | MN040 | DOC-001 p. 7 | HR-based NNT 2.8; sensitivity exclusion n=7. | NNT is labeled HR-based, not a raw risk-difference inverse; no conflation imposed. |
| N041 | MN041 | DOC-001 p. 7 | Statins 6+6=12; hypoglycemic 2+1=3. | Component totals reconcile. |
| N042 | MN042 | DOC-001 p. 7 | Akathisia 4.7%/4.8%; tardive dyskinesia 0%/3.2%. | Percentages are compatible with 3/64, 3/62, 0/64, and 2/62. |
| N043 | MN043 | DOC-001 p. 7 | Five paired UKU percentages. | "More than 5%" applies to effects observed in either arm; no rate/count confusion found. |
| N044 | MN044 | DOC-001 pp. 7-8 | Falls 20/64 and 11/62; serious events 12/64 and 12/62; one death. | Percentages reconcile under rounding and death wording is compatible. |
| N045 | MN045 | DOC-001 p. 8; Table 3 p. 7 | Hospitalization among relapses 6/13 and 11/34. | Percentages and Table 3 counts reconcile. |
| N046 | MN046 | DOC-001 Table 4 p. 8 | Weight baseline/termination means, n, and within-arm differences/CIs. | Difference is not required to equal displayed marginal means under printed missing-data caveat. |
| N047 | MN047 | DOC-001 Table 4 p. 8 | Waist baseline/termination means, n, and differences/CIs. | Same paired-data/missingness caveat applied. |
| N048 | MN048 | DOC-001 Table 4 p. 8 | Total-cholesterol means, n, and differences/CIs. | Same paired-data/missingness caveat applied. |
| N049 | MN049 | DOC-001 Table 4 p. 8 | LDL means, n, and differences/CIs. | Same paired-data/missingness caveat applied. |
| N050 | MN050 | DOC-001 Table 4 p. 8 | HDL means, n, and differences/CIs. | Same paired-data/missingness caveat applied. |
| N051 | MN051 | DOC-001 Table 4 p. 8 | HbA1c percentage means, n, and differences/CIs. | Table identifies HbA1c as percent; this supplies the comparator for N008. |
| N052 | MN052 | DOC-001 Table 4 p. 8 | Triglyceride medians/IQRs, n, and differences/CIs. | Median/paired-analysis labels and caveat retained. |
| N053 | MN053 | DOC-001 Table 4 p. 8 | Glucose medians/IQRs, n, and differences/CIs. | Median/paired-analysis labels and caveat retained. |
| N054 | MN054 | DOC-001 Table 4 p. 8 | Seven visibly blank baseline-n cells; unit/conversion footnote; missing-data caveat. | Blank cells are documented as missing display values, not inferred zeros. |
| N055 | MN055 | DOC-001 Table 5 p. 9 | Total cholesterol 9/64 (14.1%) vs 6/62 (9.7%), difference 4.3 points. | Numerators/percentages reconcile; displayed difference is separately proposed for human review. |
| N056 | MN056 | DOC-001 Table 5 p. 9 | LDL 9/64 (14.1%) vs 6/62 (9.7%), difference 4.3 points. | Numerators/percentages reconcile; displayed difference is separately proposed for human review. |
| N057 | MN057 | DOC-001 Table 5 p. 9 | Triglyceride 4/64 (6.3%) vs 2/62 (3.2%), difference 3.0 points. | Exact raw difference 3.024 points rounds to 3.0. |
| N058 | MN058 | DOC-001 Table 5 p. 9 | Glucose 4/64 (6.3%) vs 4/62 (6.5%), difference -0.2 points. | Exact raw difference -0.202 points rounds to -0.2. |
| N059 | MN059 | DOC-001 pp. 7, 9 | Incident-high definition, exact-CI labels, conversions. | Threshold, percentage-point, and exact-CI labels are distinct and coherent. |
| N060 | MN060 | DOC-001 pp. 8-9 | Time distribution, NNT 2.8, 50% observed <=20 weeks, 45% no placebo relapse. | Repeated NNT agrees; percentages have stated denominator context. |
| N061 | SN001 | DOC-002 pp. 2-7 | Protocol endpoints, eligibility, ARD sign/definition, sensitivity exclusions. | Risk, rate, RR/HR, ARD, and NNT labels are differentiated. |
| N062 | SN002 | DOC-003 pp. 5-6 | 44 DIC/fixed/random/I2/model entries and selection rule. | Full matrix checked; one printed rule/model conflict is proposed for human review. |
| N063 | SN003 | DOC-003 p. 15 | ARD/interval/NNT-NNH matrix across four subgroups. | NNT/NNH values are compatible with unrounded ARDs; endpoint-at-zero displays are not overinterpreted. |
| N064 | SN004 | DOC-003 p. 16 | Total-stroke events/totals, ARR, HR/CrI, I2 by subgroup. | Event risk, model-based ARR, HR, and CrI are kept as distinct measures; 1.004 endpoint footnote resolves display rounding. |
| N065 | SN005 | DOC-003 p. 17 | Event-rate matrix per 10,000 participant-years. | Rates are not treated as risks/proportions; person-time totals are not printed. |
| N066 | SN006 | DOC-003 p. 18 | Four sensitivity-analysis Ns and HR/CrI matrix. | Labels, endpoint ordering, and 0.9989 footnote support stated rounding. |
| N067 | SN007 | DOC-003 pp. 19-20 | Flow: 1,385=668+717; 235 duplicates; 1,150 screened; 1,131 exclusions; 21 publications/13 trials; bias counts. | All flow and risk-bias component totals reconcile. |
| N068 | SN008 | DOC-003 pp. 9, 16, 24; DOC-002 p. 7 | eTable 4 all-stroke 12 studies/73,883/72,317; forest 13 rows/81,623/80,057 including ASCEND 7,740/arm. | Matched endpoint/count and repeated-row checks completed; the source conflict is separately proposed for human review. |

## Checked relationship results

- All flow arithmetic, arm sums, mutually exclusive baseline categories, printed percentages, explicit missingness, and direct repeated values in DOC-001 reconcile within the stated one-decimal display precision or an explicit source caveat.
- Table 4 raw within-arm changes are not checked against simple marginal subtraction as an identity because its footnote expressly states that missing data can make those values differ.
- DOC-003 rates are rates per person-time, not participant risks. Bayesian HR/CrI, frequentist RR/CI, ARD, NNT/NNH, and event-rate results are not substituted for one another.
- The six source-grounded candidate proposals arising from the full inventory are recorded, with calculations and alternatives, in `checkers/numeric_consistency.md`. They have no stable candidate IDs and remain pending human adjudication.

## Limits of the numeric lane

This lane did not reconstruct unprinted paired observations, person-time denominators, unrounded model estimates, the power calculation, or unavailable degrees of freedom. Such inputs are identified in the individual check records rather than guessed.
