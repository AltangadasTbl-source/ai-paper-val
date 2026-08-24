# Complete Numeric Relationship Inventory and Numeric-Check Status

## Scope and method

This artifact mechanically consolidates the fresh mapper records in
`relationships/parts/main_numeric_relationships.md` (N001--N037) and
`relationships/parts/support_numeric_relationships.md` (N300--N315). It covers all 53 assigned
numeric relationships. Checks used only supplied PDF evidence and fresh text/layout assets under
`preprocessing/`; page references below are PDF pages. A `PASS` means that the printed relationship
reconciles under its stated rule, or that no source-grounded contradiction was identified. It is not a
validity conclusion. `LIMITED` means that the available printed definition prevents a mechanical
calculation; it is not a candidate unless a concrete printed contradiction is present.

## Main article: DOC-001 (`jama_huffman_2018_oi_170166.pdf`)

| ID | Preserved mapped observation and location | Applied review and status |
|---|---|---|
| N001 | p.1 abstract, control 10,066; steps 2,915+2,649+2,251+1,422+829+0. | **PASS:** sum = 10,066. |
| N002 | p.1 abstract, intervention 11,308; steps 0+662+1,265+2,432+3,214+3,735. | **PASS:** sum = 11,308. |
| N003 | p.1 abstract, 21,374 eligible and 21,079 completed (99%). | **PASS:** 21,079/21,374 = 98.62%, which rounds to 99% (whole-percent tolerance ±0.5 percentage point). |
| N004 | p.1 abstract, age 60.6 (SD 12.0) y; men 16,183 (76%); STEMI 13,689 (64%). | **PASS:** 16,183/21,374 = 75.72% -> 76%; 13,689/21,374 = 64.05% -> 64%. Age/SD have no stated arithmetic comparator. |
| N005 | p.4 Fig.1/p.5 narrative, recruited 22,557; excluded 1,183; eligible 21,374. | **PASS:** 22,557 - 1,183 = 21,374. |
| N006 | p.5 narrative, exclusions 954 biomarkers +132 transfer +91 outside period +6 timeline. | **PASS:** components sum to 1,183. |
| N007 | p.4 Fig.1, enrolled/lost/included/excluded by steps: 3,107/42/2,915/192; 2,765/45/2,649/116; 2,328/54/2,251/77; 1,450/27/1,422/28; 844/2/829/15; 1,001/9/896/105. | **PASS:** for every step, enrolled = included + excluded; lost-to-follow-up is stated in the figure footnote as included in analysis and is smaller than included count. Do not subtract it a second time. |
| N008 | p.4 Fig.1, cohort 1 analytic counts 439,662,542,654,605,648. | **PASS:** exact duplication in p.8 Fig.2 grid; sum 3,550 is a cohort total, not an independent trial total. |
| N009 | p.4 Fig.1, cohort 2 400,379,723,785,727,600; cohort 3 858,910,827,993,1,022,964. | **PASS:** values duplicate p.8 Fig.2. |
| N010 | p.4 Fig.1, cohort 4 477,629,730,679,860,627; cohort 5 741,731,694,743,829,896. | **PASS:** values duplicate p.8 Fig.2. |
| N011 | p.6 narrative, incomplete data 295 (1%) = 215 site non-follow-up +80 unreached. | **PASS:** 215+80=295; 295/21,374=1.38%, which rounds to 1% at whole-percent precision. |
| N012 | p.6 narrative, intervention 11,308 (53%); control 10,066 (47%). | **PASS:** groups sum to 21,374; 52.91% -> 53% and 47.09% -> 47%. |
| N013 | p.5 Table 1 categorical baseline rows: male, tobacco, diabetes, transfer, no insurance, STEMI; counts/% and crude differences. | **PASS:** each count/10,066 or count/11,308 reproduces the printed one-decimal percentage; raw intervention-minus-control differences reconcile within 0.1 percentage point rounding. |
| N014 | p.5 Table 1 continuous rows: age, symptom-to-door, weight, SBP, heart rate with stated available n, units, and differences. | **PASS:** units/scales are consistently labelled; differences are descriptive contrasts and medians/means are not mechanically interchangeable. |
| N015 | p.5 Table 1 laboratory rows: troponin, LDL, triglyceride, creatinine, glucose, hemoglobin with stated n/units. | **PASS:** missing-by-measure denominators are explicitly displayed; units and measure summaries are consistent. Exact difference reproduction is limited for medians and model-free CI construction. |
| N016 | p.5 Table 1 hospital type: 9/12/42 hospitals and treatment counts/% by government/nonprofit/private. | **PASS:** hospital categories sum 63; control counts 4,097+2,785+3,184=10,066 and intervention counts 3,036+2,964+5,308=11,308. |
| N017 | p.5 Table 1 size: 5/15/24/19 hospitals and treatment counts/%. | **PASS:** categories sum 63; control 1,853+3,561+3,847+805=10,066 and intervention 1,707+4,962+3,568+1,071=11,308. |
| N018 | p.5 Table 1 catheterization laboratory: 3 installed/17 no/43 yes and treatment counts/%. | **PASS:** categories sum 63; control 171+1,998+7,897=10,066 and intervention 325+1,554+9,429=11,308. |
| N019 | p.6 Table 2 six medication numerator/denominator/% pairs. | **PASS:** all 12 printed percentages reproduce from printed numerators/denominators to one decimal (±0.05 percentage point). Adjusted effects are not raw percentage differences. |
| N020 | p.6 Table 2 echo, angiography, PCI, primary PCI numerator/denominator/% pairs. | **PASS:** every displayed percentage reconciles at one decimal; STEMI denominators are consistently marked for primary PCI. |
| N021 | p.6 Table 2, door-balloon 65 (53-105), n=4,022 vs 77 (55-118), n=3,639; door-needle 44 (30-67), n=1,455 vs 45 (27-75), n=1,433. | **PASS:** all are medians (IQR), minutes, and subgroup n values; the beta coefficient is a model result, not the raw median difference. |
| N022 | p.6 Table 2, STEMI thrombolysis, reperfusion, rescue PCI numerator/denominator/% pairs. | **PASS:** all percentages reproduce at one decimal; 6,891/6,767 rescue-PCI denominators are separately printed applicable populations. |
| N023 | p.6 Table 2, six discharge/counseling numerator/denominator/% pairs. | **PASS:** every percentage reproduces at one decimal. Different denominators are consistent with printed discharge/eligibility and contraindication footnotes. |
| N024 | p.7 Table 3, MACE 645/10,066 (6.4%) vs 602/11,308 (5.3%). | **PASS:** 6.407% -> 6.4%; 5.324% -> 5.3%; matched abstract and narrative values agree at printed precision. |
| N025 | p.7 Table 3, 30-day mortality and cardiovascular mortality count/% pairs. | **PASS:** each percentage reconciles. Cardiovascular death is no greater than all-cause death in both groups (494<=509; 434<=445). |
| N026 | p.7 Table 3, in-hospital death, reinfarction, stroke, GUSTO bleed count/% pairs. | **PASS:** count/total percentages reconcile at one decimal. These outcomes need not sum because component overlap and time windows are not stated as mutually exclusive. |
| N027 | p.7 Table 3, optimal inpatient 3,122 (31.7)/3,878 (35.8); discharge 5,454 (61.8)/6,483 (64.0); tobacco 3,526 (96.0)/2,618 (94.7). | **PASS:** implied denominators are 9,848/10,833; 8,826/10,130; and about 3,673/2,765, respectively. They are table-specific eligible populations defined by footnotes, not the overall allocation denominators. |
| N028 | p.8 Fig.2 repeats the Fig.1 cohort-step n grid for MACE/mortality panels. | **PASS:** exact matched counts; repetition is intentional, not duplicated results. |
| N029 | pp.8-9 narrative, expanded MACE 7.0% intervention vs 9.1% control; adjusted RD -1.34%. | **PASS:** this is a distinct expanded endpoint/time composition; crude difference (-2.1 pp) is not required to equal adjusted RD. |
| N030 | p.9 Fig.3 age subgroup event/total/% pairs. | **PASS:** all six printed percentages reproduce to one decimal; adjusted RD/OR are model-derived and cannot be mechanically equated to crude subgroup contrasts. |
| N031 | p.9 Fig.3 sex and cardiac-status event/total/% pairs. | **PASS:** all eight percentages reproduce. |
| N032 | p.9 Fig.3 hospital-size event/total/% pairs. | **PASS:** all eight percentages reproduce; each treatment-size partition sums to allocation total. |
| N033 | p.9 Fig.3 hospital-type event/total/% pairs. | **PASS:** all six percentages reproduce; each treatment-type partition sums to allocation total. |
| N034 | p.9 Fig.3 partition denominators total 11,308 intervention and 10,066 control for age, sex, status, size, and type. | **PASS:** each complete partition sums exactly to the allocation totals; MACE-event totals also sum to 602 intervention and 645 control. |
| N035 | pp.2-3, 63 hospitals, five 4-month steps over 24 months; 12/13 hospital crossovers. | **PASS:** baseline plus five successive 4-month periods is 24 months; 12+13+13+13+12=63. |
| N036 | p.6 Table 2 discharge beta-blocker: RD 6.69% (4.43-8.95), OR 1.48 (1.30-1.68); p.7 narrative: RD 6.63% (4.43-8.95), OR 1.47 (1.30-1.68). | **PROVISIONAL CANDIDATE NC-001:** exact same named outcome, contrast, and CI endpoints have discordant point estimates. See numeric checker. |
| N037 | p.6 narrative, included versus missing follow-up initial troponin 1.3 vs 4.6 ng/mL, P<.001; eTable 1 is cited. | **PASS:** values match DOC-004 p.17 eTable 1. The nonzero displayed P value has no numeric contradiction in this lane. |

## Support documents

| ID | Preserved mapped observation and location | Applied review and status |
|---|---|---|
| N300 | DOC-002 pp.6-7; DOC-003 p.3: 4-month baseline and transitions at months 4,8,12,16,20; protocol 12-14 hospitals/cohort, SAP 12/cohort. | **PASS:** planning schedule counts are internally coherent; protocol/SAP design quantities are not final-result denominators. |
| N301 | DOC-002 pp.6,10,18; DOC-003 p.4: planned 60-70 hospitals, 2 years, 15,750 subjects; n=15,000 inflated for up to 5% dropout. | **PASS:** 15,000/(1-0.05)=15,789.5, compatible with rounded planning target 15,750; final N is explicitly distinct. |
| N302 | DOC-002 pp.9,16,18; DOC-003 pp.4-5: 30-day MACE component and secondary-endpoint definitions. | **PASS:** supplied endpoint labels match the main article's MACE definition; components are not asserted mutually exclusive. |
| N303 | DOC-002 pp.10-13; DOC-003 pp.5-8: 30-day follow-up, 2,200 subsample, ITT population. | **PASS:** population/time definitions distinguish all database patients from the substudy. |
| N304 | DOC-002 pp.18,21; DOC-003 pp.4,8: alpha .05, 80% power, 2.4% from 10.4%, ICC .05, audit samples and interim boundaries. | **PASS:** planning/calibration quantities are consistently labelled and not used as final results. |
| N305 | DOC-004 pp.3-5: illustrative report dates and R3M/percentile definitions. | **PASS:** expressly illustrative toolkit material, not trial outcome estimates. |
| N306 | DOC-004 pp.6-9: eligible-opportunity proportions, STEMI/NSTEMI/discharge definitions and time thresholds. | **PASS:** labels distinguish proportions from median-minute measures. |
| N307 | DOC-004 pp.15-16: checklist doses/frequencies/thresholds. | **PASS:** operational toolkit numeric labels, not analyzed outcomes; no matched numerical claim requires reconciliation. |
| N308 | DOC-004 p.17 eTable 1: complete n=21,079/missing n=295; footnote says difference=intervention-control. | **PROVISIONAL CANDIDATE NC-002:** the footnote comparator conflicts with the displayed complete/missing columns. See numeric checker. |
| N309 | DOC-004 p.18 eTable 2: control n=10,066/intervention n=11,308 and adjusted marginal effects/differences. | **PASS:** correct comparator footnote (intervention-control) and matched allocation totals; model effects are not raw Table 1 differences. |
| N310 | DOC-004 p.19 eTable 3: step-by-status counts 2,915; 2,649/662; 2,251/1,265; 1,422/2,432; 829/3,214; 3,735. | **PASS:** exact match to main Figure 1 allocation pattern and eTable 4 step totals. |
| N311 | DOC-004 p.20 eTable 4: step totals 2,915,3,311,3,516,3,854,4,043,3,735; creatinine NA steps 1-2. | **PASS:** totals equal N310 control+intervention per step; NA is explained by collection beginning at step 3. |
| N312 | DOC-004 p.21 eTable 5: 40 sensitivity OR (95% CI) values. | **PASS:** every OR lies within its ordered positive CI; labels identify four separate adjustment sets, so repeated nearby values are not duplicates. |
| N313 | DOC-004 p.22 eTable 6: 10 interaction-exposure OR (95% CI) values. | **PASS:** all ORs lie within ordered positive CIs; each is an interaction result, distinct from primary effects. |
| N314 | DOC-004 p.23 eTable 7: control N=10,066/intervention N=11,308; four outcome rows, counts, percentages, model results, ICCs. | **PASS:** displayed percentages reconcile with allocation denominators to one decimal; CIs contain their displayed estimates and ICCs are labelled as correlations rather than rates. |
| N315 | DOC-004 pp.24-27 eFigures: residual MACE, within-hospital rate difference, temporal MACE/death rates. | **LIMITED:** figures supply no exact point labels for arithmetic re-calculation. Axis/legend labels distinguish residuals, differences, and rates; no concrete conflict found. |

## Candidate index

Two distinct provisional candidates were emitted: **NC-001** (N036) and **NC-002** (N308). Both remain **Pending Human Adjudication**. No status here assigns severity, validity, correction, or disposition.
