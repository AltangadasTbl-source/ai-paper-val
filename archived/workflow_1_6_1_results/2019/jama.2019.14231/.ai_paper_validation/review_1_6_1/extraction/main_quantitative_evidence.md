# Main article quantitative evidence map

## Scope, provenance, and coverage

Fresh scientific mapping of DOC-001, REPORT, `jama_aminian_2019_oi_190103.pdf`, all physical PDF pages 1-12 (printed 1271-1282). Every page was read through its reusable source-matched native text and a fresh direct layout transcription. This artifact does not select or diagnose reporting issues. Definitions and all displayed quantitative result rows are retained, including non-significant and descriptive results. Derived text is a locator; supplied PDF remains authority.

Direct command: `pdftotext -layout jama_aminian_2019_oi_190103.pdf .ai_paper_validation/review_1_6_1/extraction/main_direct_layout.txt`, Poppler 26.01.0, CPU native/layout extraction. Targeted direct visual confirmation: `pdftoppm -f 7 -l 7 -r 110 -singlefile -png jama_aminian_2019_oi_190103.pdf .ai_paper_validation/review_1_6_1/extraction/main_direct_page_007`, Poppler renderer; image inspected for Table 2, Figure 2, captions, and longitudinal/adverse-event prose. No OCR was needed. All twelve source pages already have reusable native coverage; fresh-required unit count is zero. No reused asset was changed.

| Physical page | Content mapped | Status |
|---|---|---|
| 1 | Abstract cohort, baseline summaries, follow-up, primary and mortality results | COMPLETE |
| 2 | Key Points, source/cohort definitions, enrollment/exclusion and endpoint definitions | COMPLETE |
| 3 | Figure 1 complete participant flow, overlapping exclusion categories, endpoint risk-set rules, statistical methods start | COMPLETE |
| 4 | Matching, models, imputation, tests, sensitivity methods; procedures, BMI, follow-up, primary/secondary narrative | COMPLETE |
| 5 | Table 1 demographics and all medical-history rows | COMPLETE |
| 6 | Table 1 laboratory/medication rows and all footnotes; proportional hazards narrative | COMPLETE |
| 7 | Figure 2 all panels/risk counts/caption; Table 2 all eight outcomes and footnotes; weight/HbA1c and adverse-event narrative | COMPLETE |
| 8 | Figure 3 all six panels/risk counts/caption; sensitivity narrative | COMPLETE |
| 9 | Figure 4 both panels/axes/estimates/caption; sensitivity and discussion result matches | COMPLETE |
| 10 | Figure 5 all six panels/axes/P values/caption; primary composite discussion | COMPLETE |
| 11 | Discussion result direction, limitations relevant to interpretation and analysis; historical contextual numbers identified separately | COMPLETE |
| 12 | Article disclosures, references and bibliographic numbers; no applicable new study quantitative result | COMPLETE_NO_APPLICABLE_RESULT |

Every link below uses physical PDF page numbers. Baseline columns always mean surgery n=2287; eligible nonsurgical before matching n=39267; matched nonsurgical n=11435. Outcome contrast for Cox HR is surgery versus matched nonsurgical; absolute risk difference (ARD) is nonsurgical minus surgery, percentage points. No person-time numerator totals, test statistics, or numerical standard errors are printed in the main article. Cause-specific rates per 100 patient-years are defined but numerical rates are delegated to supplement eTable 4. Graphical trajectories have no exact numeric point labels beyond the estimates transcribed here; their axes, ordering, confidence shading, times, and linked numeric supplement tables are mapped without inventing digitized values.

## Numeric relationship inventory

N001-N059 are fresh main-paper numeric relationships. Each grouped relationship tracks all its displayed rows and associated denominators; the complete Table 1 transcription below preserves every component value.

| ID | Exact location | Relationship and population/time keys |
|---|---|---|
| N001 | [Abstract/Key Points](../../../jama_aminian_2019_oi_190103.pdf#page=1), pp2-4 | Base 287438; matched surgery 2287 + controls 11435 = cohort 13722; ratio 1:5; EHR 1998-2017, follow-up through December 2018/December 31, 2018 |
| N002 | [Figure 1](../../../jama_aminian_2019_oi_190103.pdf#page=3) | Base split: 2818 metabolic/bariatric coded; 284620 nonsurgical. Surgery: 61 chart-review exclusion, 2757 potentially eligible, 470 enrollment exclusion, 2287 included. Control: 195677 initial exclusion (116031 diagnosis after assigned date; 79646 no follow-up), 88943 potentially eligible, 49676 enrollment exclusion, 39267 eligible, 27832 not matched, 11435 matched |
| N003 | [Figure 1 exclusions](../../../jama_aminian_2019_oi_190103.pdf#page=3) | Surgery enrollment reasons: diabetes evidence 240, BMI 133, cancer 99, ED within 5 days 29, age 24, transplant 19, EF<20% 13. Controls: BMI/missing 39821, age 12004, diabetes evidence 9888, cancer 3291, EF<20% 1006, transplant 855, ED within 5 days 537, died within 30 days 87. Footnote: some patients met multiple exclusion criteria; reason counts not a partition |
| N004 | [Eligibility](../../../jama_aminian_2019_oi_190103.pdf#page=2), p3 | Age 18-80; BMI>=30 kg/m²; HbA1c>=6.5% or >=1 diabetes medication. Exclusions include EF<20% at any prior time, gastrointestinal cancer within 1 year, ED within 5 days; control index-date exclusion includes death within 30 days. Index date first metabolic surgery or one randomly assigned surgical-cohort date |
| N005 | [Results procedures](../../../jama_aminian_2019_oi_190103.pdf#page=4) | Roux-en-Y bypass 1443 (63%), sleeve 730 (32%), banding 109 (5%), duodenal switch 5; surgery total 2287 |
| N006 | [Results BMI](../../../jama_aminian_2019_oi_190103.pdf#page=4), Table1 p5 | Surgery BMI>=40:1713 (75% prose/74.9 table);35-39.9:465 (20%/20.3);30-34.9:109 (5%/4.8) |
| N007 | [Follow-up](../../../jama_aminian_2019_oi_190103.pdf#page=4), Abstract p1/Figure2 p7 | Entire cohort median 3.9 y (IQR1.9-6.1); controls4.0 (2.1-6.1); surgery3.3 (1.2-6.3); composite event observation matches Figure2 caption |
| N008 | [Table1](../../../jama_aminian_2019_oi_190103.pdf#page=5) | Index-date median/IQR and standardized differences before/after matching |
| N009 | Table1 p5; Abstract p1 | Sex women/men counts, percentages, standardized differences; abstract women65.5/64.2 |
| N010 | Table1 p5; Abstract/Results pp1,4 | Age median/IQR; surgery52.5, matched54.8, eligible61.6 years |
| N011 | Table1 p5; Abstract/Results pp1,4 | BMI median/IQR, three categories/counts/percentages; kg/m² scale |
| N012 | Table1 p5; Results p4 | Weight median/IQR, kg; surgery126.5 vs matched120.2; eligible104.8 |
| N013 | Table1 p5; Results p4 | Race white/black/other/missing counts/%; prose black19% vs25% |
| N014 | Table1 p5 | Annual zip-code income median/IQR $, missing count/% |
| N015 | Table1 p5; Results p4 | Smoking never/former/current/missing; prose current7% vs14% |
| N016 | Table1 p5 | Ohio/Florida location counts/% |
| N017 | Table1 p5; Results p4 | Hypertension count/%; prose85% vs75% |
| N018 | Table1 p5; Results p4 | Dyslipidemia count/%; prose74% vs65% |
| N019 | Table1 p5 | Peripheral neuropathy count/% |
| N020 | Table1 p5; Table2 p7 | Baseline heart failure count/% and outcome initial risk sets |
| N021 | Table1 p5; Table2 p7 | Baseline coronary artery disease count/% and initial risk sets |
| N022 | Table1 p5 | COPD count/% |
| N023 | Table1 p5; Table2 p7 | Baseline nephropathy count/% and initial risk sets |
| N024 | Table1 p5; Table2 p7 | Baseline atrial fibrillation count/% and initial risk sets |
| N025 | Table1 p5 | Peripheral arterial disease count/% |
| N026 | Table1 p5 | Baseline myocardial infarction count/% |
| N027 | Table1 p5; Table2 p7 | Baseline cerebrovascular disease count/% and initial risk sets |
| N028 | Table1 p5 | Baseline ischemic stroke count/% |
| N029 | Table1 p5 | Baseline dialysis count/% |
| N030 | [Table1](../../../jama_aminian_2019_oi_190103.pdf#page=6), Abstract p1 | HbA1c median/IQR %, missing count/%; abstract7.1 vs7.1 |
| N031 | Table1 p6 | Systolic BP median/IQR mm Hg, missing count/% |
| N032 | Table1 p6 | Diastolic BP median/IQR mm Hg, missing count/% |
| N033 | Table1 p6 | eGFR median/IQR mL/min, missing; MDRD approximation footnote |
| N034 | Table1 p6 | HDL-C median/IQR mg/dL, missing; mmol/L multiplier0.0259 |
| N035 | Table1 p6 | LDL-C median/IQR mg/dL, missing; mmol/L multiplier0.0259 |
| N036 | Table1 p6 | Triglycerides median/IQR mg/dL, missing; mmol/L multiplier0.0113 |
| N037 | Table1 p6 | UACR median/IQR mg/g, missing |
| N038 | Table1 p6 | Noninsulin diabetes medication users, and class counts0/1/2/>=3; counts/% |
| N039 | Table1 p6 | Insulin count/% |
| N040 | Table1 p6 | Lipid-lowering medication count/% |
| N041 | Table1 p6 | Renin-angiotensin inhibitor count/%, includes ACE inhibitors/ARBs |
| N042 | Table1 p6 | Other antihypertensive medication count/% |
| N043 | Table1 p6; Results p4 | Aspirin count/%; prose32% vs40% |
| N044 | Table1 p6 | Warfarin count/% |
| N045 | [Primary results](../../../jama_aminian_2019_oi_190103.pdf#page=4), Abstract p1/Table2 p7/Figure2A p7 | End-of-study primary event counts385 surgery/3243 controls; denominators2287/11435; 8-year KM/ARD/HR are distinct estimands mapped in S001 |
| N046 | Results p4/Table2 p7/Figure2B p7 | Secondary3-component event counts194/1765; denominators2287/11435; inference S002 |
| N047 | Abstract p1/Results p4/Table2 p7/Figure3A p8 | All-cause deaths112/1111; denominators2287/11435; inference S003 |
| N048 | Figure2 p7 | Composite at-risk series at years0,2,4,6,8 transcribed below; both groups/all points |
| N049 | Figure3 p8 | All six individual-outcome risk series and outcome-specific observation medians/IQRs transcribed below |
| N050 | [Longitudinal weight](../../../jama_aminian_2019_oi_190103.pdf#page=7), Figure4 p9 | 8-year mean body-weight reduction surgery29.1kg (95%CI28.8-29.3), controls8.7kg (8.6-8.9); between-group20.3kg (20.1-20.6). Figure4 percent loss contrast14.7% (14.5-14.9), P<.001; separate kg and percent scales |
| N051 | p7/Figure4B p9 | Mean difference in HbA1c changes from baseline at8years1.1 percentage points (95%CI1.0-1.2), P<.001; plotted absolute HbA1c % trajectories |
| N052 | [Figure5](../../../jama_aminian_2019_oi_190103.pdf#page=10), prose p7/p11 | Six prescription proportions/95%pointwise CI trajectories; every0.1year through8years; exact values not printed in figure, numeric tables eTable8/eTable10. P values transcribed in S018-S023 |
| N053 | Adverse events p7 | Surgery denominator2287, 90-day window: bleeding/transfusion68 (3.0%), pulmonary58 (2.5%), VTE22 (1.0%), cardiac17 (0.7%), dialysis-requiring renal failure4 (0.2%), cerebrovascular0, abdominal intervention109 (4.8%), deaths15 (0.7%); endoscopy16.7%, interventional radiology1.6%, parenteral nutrition1.4% |
| N054 | Adverse events p7 | Postoperative stay median2days (IQR2-3) |
| N055 | Sensitivity pp4,8,9 | Random index dates5times × matching ratios1:1,1:5,1:10 =15data sets; eight endpoint Cox fits per set; time-varying HRs at2,5,8years; estimates delegated to supplement |
| N056 | Discussion p9 | Main primary8-year KM rounded in narrative: controls48% vs surgery31%; mortality8-year ARD7.8%; all six individual endpoints and3-component composite lower |
| N057 | [Limitations](../../../jama_aminian_2019_oi_190103.pdf#page=11) | Less than10% nonsurgical patients exposed to newer GLP-1 agonists/SGLT2 inhibitors; no exact numerator/denominator printed |
| N058 | Discussion pp9-11 | Context from cited prior studies, not current cohort: Look AHEAD weight8.6% vs0.7% at1year,6.0% vs3.5% at9years; Fisher5year HR0.60macrovascular/0.33death and annual rates2-3times lower; SOS343surgical/260controls,66%vertical banded gastroplasty/18%banding; nonsurgical weight5%; albuminuria resolution50%; nephropathy59%lower at5years. Retained as contextual quantities, no external verification |
| N059 | Table1 footnote p6/Results p4 | 37baseline covariates described; standardized difference footnote says absolute value of (surgery−control means/proportions)/pooled SD; every printed signed value retained in full table transcription |

## Statistical relationship inventory

All 24 S relationships below are inferential/method relationships. Every P value is a printed value; no statistical conclusion or finding is assigned here. Main article declares two-sided significance .05 and 95% CIs; secondary outcomes described as exploratory because multiple comparisons could generate type I error. Endpoint HRs are fully adjusted Cox, with all Table1 baseline variables; matching is nearest-neighbor propensity scoring from logistic model/logit, seven a priori confounders: index date, age, sex, BMI category30-34.9/35-39.9/>=40, Ohio/Florida, insulin use, diabetes-related end-organ complications. Missing baseline values imputed within each outcome data set using five chained-equation imputations: predictive mean matching numeric, logistic binary, polytomous logistic categorical; Rubin formula for imputation-corrected standard errors of estimates/contrasts. No numeric standard errors printed. Kaplan-Meier estimates are described as cumulative incidence. ARD CIs percentile bootstrap1000samples; no multiplicity-adjusted numerical threshold is stated.

| ID | Outcome/method; exact source | Surgery n / KM8y% (95%CI) | Controls n / KM8y% (95%CI) | ARD8y percentage points (95%CI) | Adjusted HR surgery/control (95%CI), P |
|---|---|---|---|---|---|
| S001 | Primary extended MACE; p1,p4,p7 Table2/Figure2A | 2287 /30.8 (27.6-34.0) |11435 /47.7 (46.1-49.2)|16.9 (13.1-20.4)|0.61 (0.55-0.69), <.001|
| S002 | Secondary3-component MACE; p4,p7 Table2/Figure2B |2287 /17.0 (14.3-19.7)|11435 /27.6 (26.2-29.0)|10.6 (7.5-13.6)|0.62 (0.53-0.72), <.001|
| S003 | All-cause mortality; p1,p4,p7Table2,p8Figure3A |2287 /10.0 (7.8-12.2)|11435 /17.8 (16.6-19.0)|7.8 (5.1-10.2)|0.59 (0.48-0.72), <.001|
| S004 | Heart failure; p7Table2,p8Figure3B |2049 /6.8 (4.9-8.6)|10093 /18.9 (17.6-20.2)|12.9 (10.4-15.1)|0.38 (0.30-0.49), <.001|
| S005 | Coronary artery disease; p7Table2,p8Figure3C |2050 /7.9 (5.9-9.8)|10331 /11.6 (10.5-12.6)|4.2 (1.9-6.8)|0.69 (0.54-0.87), .002|
| S006 | Cerebrovascular disease; p7Table2,p8Figure3D |2245 /4.1 (2.7-5.5)|11077 /5.6 (4.9-6.3)|1.8 (−0.03 to3.4)|0.67 (0.48-0.94), .02|
| S007 | Nephropathy; p7Table2,p8Figure3E |1937 /6.1 (4.4-7.8)|9190 /16.3 (15.0-17.6)|11.1 (8.8-13.6)|0.40 (0.31-0.52), <.001|
| S008 | Atrial fibrillation; p7Table2,p8Figure3F |2135 /7.9 (6.1-9.7)|10734 /13.6 (12.5-14.7)|6.5 (4.4-8.7)|0.78 (0.62-0.97), .03|

Primary extended MACE = first occurrence after index date of six components: all-cause mortality, coronary artery events (unstable angina, MI, coronary intervention/surgery), cerebrovascular events (ischemic or hemorrhagic stroke, carotid intervention/surgery), heart failure, nephropathy, atrial fibrillation. Secondary3-component MACE = all-cause mortality, MI, ischemic stroke. Composite risk sets exclude no patients, but a condition/event present at baseline does not count toward that composite during follow-up. Each individual nonmortality endpoint excludes patients already having that condition; mortality includes all. Death sources EHR, Social Security, State Death Indices. Endpoint definitions/codes cross-reference eTable1.

| ID | Location | Complete method/result relationship |
|---|---|---|
| S009 | Statistical Analysis pp3-4 | Doubly robust propensity plus outcome regression, matching/model/imputation and significance details above; baseline37covariates; full data structural keys retained |
| S010 | p4/p6 | Treatment PH assumption weighted residuals (Grambsch-Therneau); narrative says satisfied for composites/all individual outcomes except AF; exact PH P values eTable6, not printed main |
| S011 | p4,p6 | Time-varying HR method: restricted cubic spline observed follow-up interacted with treatment added to fully adjusted Cox; estimates at2,5,8years, especially AF; eTable7 |
| S012 | p4 | Primary subgroups: individual treatment×variable interaction in fully adjusted Cox; P and CI estimated; Results no heterogeneity for sex, age, BMI,HbA1c,eGFR, insulin,sulfonylurea,lipid-lowering use; eFigure1 |
| S013 | p4,p8,p9 | Sensitivity5random date samples×3matching ratios=15sets, fully adjusted Cox for all eight endpoints; reported differences negligible relative to primary1:5data set; eFigure4 |
| S014 | p4,p9,p11 | E-value assessment for unmeasured confounding, compared with known cardiovascular-risk-factor HRs; eTable12; narrative association robustness, no numeric E-values main |
| S015 | p4,p7,p9Figure4 | Longitudinal flexible regression4-knot spline on time interacted with treatment; weight absolutekg8y between-group20.3 (20.1-20.6); no separate kg P printed in paragraph |
| S016 | p9Figure4A | Percent weight-loss8y between-group delta14.7% (14.5-14.9), P<.001; smoothed mean percent change from baseline,95%CI shade; x0,2,4,6,8y; y0,−5,−10,−15,−20,−25%; controls above surgery (less negative) |
| S017 | p7,p9Figure4B | HbA1c8y between-group difference of changes1.1% (1.0-1.2), P<.001; plotted absolute HbA1c%, y5.5,6.0,6.5,7.0,7.5,8.0; x0,2,4,6,8; controls above surgery; CI shading |
| S018 | p4,p10Figure5A | Noninsulin drugs,8y P<.001; proportions/95%pointwiseCI,0.1y sampling; Figure5caption Fisher exact comparison at8y, statistical-method prose2-sample proportions test at1,2,5,8y; no exact8y proportion printed main |
| S019 | p4,p10Figure5B | Insulin,8y P=.008; same test and proportion keys |
| S020 | p4,p10Figure5C | Renin-angiotensin inhibitors,8y P<.001; same test and proportion keys |
| S021 | p4,p10Figure5D | Other antihypertensives,8y P<.001; same test and proportion keys |
| S022 | p4,p10Figure5E | Lipid-lowering,8y P<.001; same test and proportion keys |
| S023 | p4,p10Figure5F | Aspirin,8y P<.001; same test and proportion keys |
| S024 | p1,p4,p9,p10,p11 | Narrative alignment: all7prespecified secondary outcomes significantly favor surgery (abstract); all6individual components and3component composite lower (discussion); observational association/hypothesis generating, confirmation in RCT needed; medication proportions and HbA1c/weight lower; no procedure-specific comparisons because distribution nonuniform and would require separate matching. Severity of baseline conditions not used in matching/adjustment (p11) |

For all Figure5 panels, y-axis Taking Drug,% (95%CI), ticks10,30,50,70,90; x-axis Years Since Index Date ticks0,2,4,6,8. Controls are visually above surgery across post-index follow-up; no exact graph-point extraction is implied. Caption says prescription proportion, pointwise95%CIs, all6groups as labeled; RAS drugs include ACE inhibitors and ARBs. Prose p11 clarifies prescription orders need not equal actual use.

## Figure risk sets and observation-time quantities

Every list below is in year order0,2,4,6,8. Figure2 panels cumulative incidence axis0,10,20,30,40,50%; Figure3 panels0,5,10,15,20%; HR/CI/P inscriptions duplicate S001-S008 exactly. Both figures show controls above surgery throughout most follow-up. Caption source page and exact count arrays are retained.

| Location/outcome | Controls risk counts | Surgery risk counts | Controls observation median(IQR)y | Surgery observation median(IQR)y |
|---|---|---|---|---|
| p7Fig2A primary |11435,8050,4791,2244,838|2287,1372,910,535,293|4.0(2.1-6.1)|3.3(1.2-6.3)|
| p7Fig2B secondary |11435,8645,5543,2826,1130|2287,1438,991,610,336|4.0(2.1-6.1)|3.3(1.2-6.3)|
| p8Fig3A mortality |11435,8844,5789,3005,1224|2287,1460,1017,629,353|4.0(2.1-6.1)|3.3(1.2-6.3)|
| p8Fig3B heart failure |10093,7572,4845,2468,991|2049,1281,895,552,317|4.1(2.2-6.2)|3.3(1.1-6.4)|
| p8Fig3C coronary |10331,7776,4958,2516,995|2050,1283,878,538,299|4.0(2.1-6.1)|3.3(1.1-6.4)|
| p8Fig3D cerebrovascular |11077,8474,5492,2847,1149|2245,1418,982,607,338|4.0(2.1-6.1)|3.3(1.1-6.3)|
| p8Fig3E nephropathy |9190,7056,4515,2262,893|1937,1216,838,506,293|4.1(2.2-6.2)|3.3(1.1-6.3)|
| p8Fig3F AF |10734,8152,5212,2660,1072|2135,1328,915,555,319|4.0(2.1-6.1)|3.3(1.1-6.3)|

## Complete Table 1 row transcription

The following source-layout blocks preserve every Table1 value, column label, all missingness rows, signed standardized differences, units, IQR bounds, conversion factors, and footnotes. Column order: surgery; eligible controls; standardized difference before; matched controls; standardized difference after. They are cross-indexed by N008-N044 and N059. No normalization of numerical cells has been performed.

```text
              Table 1. Characteristics of Metabolic Surgery Patients and Nonsurgical Control Patients at the Index Date Before and After Matching
                                              Metabolic Surgery     Nonsurgical          Standardized Difference    Matched Nonsurgical Control   Standardized Difference
               Baseline Variable              (n = 2287)            (n = 39 267)a        Before Matchingb           (n = 11 435)                  After Matchingb
               Demographic Data
               Index date,                    1/2013                6/2014               −42.6                      7/2013                        −15.9
               median (IQR)                   (7/2010-4/2015)       (5/2012-2/2016)                                 (5/2011-4/2015)
               Sex, No. (%)
                 Women                        1499 (65.5)           20 372 (51.9)        28.0                       7339 (64.2)                   2.9
                 Men                          788 (34.5)            18 895 (48.2)        −28.0                      4096 (35.8)                   −2.9
               Age, median (IQR), y           52.5 (43.7-60.5)      61.6 (53.1-68.9)     −75.3                      54.8 (46.2-62.5)              −19.9
               BMI, median (IQR)c             45.1 (40-51.8)        35.9 (32.7-60.6)     113.5                      42.6 (39.4-47.2)              34.4
               BMI category,
               No. (%)
                 30-34.9                      109 (4.8)             17 110 (43.6)        −101.7                     495 (4.3)                     2.1
                 35-39.9                      465 (20.3)            11 320 (28.8)        −19.8                      2595 (22.7)                   −5.7
                 ≥40                          1713 (74.9)           10 837 (27.6)        107.4                      8345 (73.0)                   4.4
               Weight,                        126.5                 104.8                88.3                       120.2                         27.8
               median (IQR), kg               (110.2-148.0)         (93.0-119.0)                                    (106.8-136.5)
               Race, No. (%)
                 White                        1734 (75.8)           29 014 (73.9)        4.45                       7994 (69.9)                   13.3
                 Black                        441 (19.3)            8138 (20.7)          −3.6                       2804 (24.5)                   −12.7
                 Other                        54 (2.4)              874 (2.2)            0.9                        234 (2.1)                     2.1
                 Missing                      58 (2.5)              1241 (3.2)           −3.8                       403 (3.5)                     −5.8
               Annual zip code income,        49 855                50 378               0.7                        48 732                        10.8
               median (IQR), $                (39 964-62 273)       (37 958-65 536)                                 (36 951-61 512)
                 Missing, No. (%)             70 (3.1)              494 (1.3)            12.4                       125 (1.1)                     13.8
               Smoking status,
               No. (%)
                 Never                        1231 (53.8)           18 087 (46.1)        15.6                       5615 (49.1)                   9.5
                 Former                       828 (36.2)            15 531 (39.6)        −6.9                       4012 (35.1)                   2.3
                 Current                      170 (7.4)             5051 (12.9)          −18.1                      1607 (14)                     −21.5
                 Missing                      58 (2.5)              598 (1.5)            7.2                        201 (1.8)                     5.4
               Location, No. (%)
                 Ohio                         1816 (79.4)           35 482 (90.4)        −30.9                      9834 (86.0)                   −17.5
                 Florida                      471 (20.6)            3785 (9.6)           30.9                       1601 (14.0)                   17.5
               Medical History, No. (%)
               Hypertension                   1953 (85.4)           30 308 (77.2)        21.2                       8565 (74.9)                   26.5
               Dyslipidemia                   1686 (73.7)           27 717 (70.6)        7.0                        7457 (65.2)                   18.6
               Peripheral                     242 (10.6)            4569 (11.6)          −3.4                       1203 (10.5)                   0.2
               neuropathy
               Heart failure                  238 (10.4)            4470 (11.4)          −3.1                       1342 (11.7)                   −4.2
               Coronary artery                237 (10.4)            5863 (14.9)          −13.8                      1104 (9.7)                    2.4
               disease
               COPD                           206 (9.0)             4179 (10.6)          −5.5                       1188 (10.4)                   −4.7
               Nephropathy                    191 (8.4)             5069 (12.9)          −14.8                      1219 (10.7)                   −7.8
               Atrial fibrillation            152 (6.6)             3242 (8.3)           −6.1                       701 (6.1)                     2.1
               Peripheral arterial            123 (5.4)             3426 (8.7)           −13.1                      755 (6.6)                     −5.2
               disease
               Myocardial                     55 (2.4)              1201 (3.1)           −4.0                       211 (1.8)                     3.9
               infarction
               Cerebrovascular                42 (1.8)              1703 (4.3)           −14.5                      358 (3.1)                     −8.3
               disease
               Ischemic stroke                34 (1.5)              1385 (3.5)           −13.1                      298 (2.6)                     −7.9
               Dialysis                       14 (0.6)              322 (0.8)            −2.5                       78 (0.7)                      −0.9
```

```text
               Table 1. Characteristics of Metabolic Surgery Patients and Nonsurgical Control Patients at the Index Date Before and After Matching (continued)
                                                    Metabolic Surgery     Nonsurgical            Standardized Difference         Matched Nonsurgical Control      Standardized Difference
                   Baseline Variable                (n = 2287)            (n = 39 267)a          Before Matchingb                (n = 11 435)                     After Matchingb
                   Clinical and Laboratory Data
                   HbA1c, median (IQR), %           7.1 (6.3-8.2)         7 (6.4-8.1)            −2.3                            7.1 (6.4-8.4)                    −11.4
                     Missing, No. (%)               159 (7.0)             4899 (12.5)            −18.7                           1288 (11.3)                      −15.0
                   Blood pressure,
                   median (IQR), mm Hg
                     Systolic                       138 (127-148)         130 (120-142)          31.6                            130 (121-142)                    30.1
                         Missing, No. (%)           0                     234 (0.6)              −10.9                           54 (0.5)                         –9.7
                     Diastolic                      71 (65-79)            76 (69-82)             −35.3                           78 (70-84)                       −44.2
                         Missing, No. (%)           0                     234 (0.6)              −10.9                           54 (0.5)                         –9.7
                   eGFR, median (IQR), mL/mind      90 (72-108)           86 (68-105)            11.5                            92 (72-112)                      −8.1
                     Missing                        1 (0)                 1620 (4.1)             −28.9                           432 (3.8)                        −27.5
                   HDL-C, median (IQR), mg/dL       44 (37-52)            43 (36-52)             1.6                             43 (36-51)                       4.9
                     Missing, No. (%)               792 (34.6)            12 966 (33.0)          3.4                             3512 (30.7)                      8.4
                   LDL-C, median (IQR), mg/dL       92 (72-115)           89 (68-114)            5.5                             93 (72-118)                      −4.9
                     Missing, No. (%)               208 (9.1)             10 469 (26.7)          −47.1                           2947 (25.8)                      −45.1
                   Triglycerides,                   146 (101-209)         143 (101-205)          1.8                             146 (103-208)                    −1.4
                   median (IQR), mg/dL
                     Missing, No. (%)               160 (7)               6538 (16.7)            −30.2                           1816 (15.9)                      −28.2
                   UACR, median (IQR), mg/g         14 (6-40)             14 (5-40)              −0.5                            14 (5-43)                        −3.8
                     Missing, No. (%)               1003 (43.9)           14 665 (37.4)          13.3                            4224 (36.9)                      14.1
                   Medication History
                   Noninsulin diabetes              1869 (81.7)           32 428 (82.6)          −2.2                            9253 (80.9)                      2.1
                   medication, No. (%)e
                     0                              418 (18.3)            6839 (17.4)            2.2                             2182 (19.1)                      −2.1
                     1                              1088 (47.6)           18 206 (46.4)          2.4                             5218 (45.6)                      3.9
                     2                              560 (24.5)            10 084 (25.7)          −2.8                            2929 (25.6)                      −2.6
                     ≥3                             221 (9.7)             4138 (10.5)            −2.9                            1106 (9.7)                       0
                   Insulin, No. (%)                 776 (33.9)            10 811 (27.5)          13.9                            3806 (33.3)                      1.4
                   Lipid-lowering                   1195 (52.3)           23 963 (61.0)          −17.8                           5998 (52.5)                      −0.4
                   medications, No. (%)
                   Renin-angiotensin system         1396 (61.0)           25 375 (64.6)          −7.4                            7102 (62.1)                      −2.2
                   inhibitors, No. (%)f
                   Other antihypertensive           1649 (72.1)           28 710 (73.1)          −2.2                            8066 (70.5)                      3.5
                   medications, No. (%)
                   Aspirin                          731 (32.0)            18 961 (48.3)          −33.8                           4627 (40.5)                      −17.8
                   Warfarin                         190 (8.3)             3207 (8.2)             0.5                             943 (8.2)                        0.2
               Abbreviations: BMI, body mass index; COPD, chronic obstructive pulmonary                      or proportions between the groups (metabolic surgery − nonsurgical control
               disease; eGFR, estimated glomerular filtration rate; HbA1c, glycated                          group) divided by pooled standard deviation.
               hemoglobin; HDL-C, high-density lipoprotein cholesterol; LDL-C, low-density               c
                                                                                                             Calculated as weight in kilograms divided by height in meters squared.
               lipoprotein cholesterol; UACR, urinary albumin-creatinine ratio.                          d
                                                                                                             Approximated using the Modification of Diet in Renal Disease (MDRD)
               SI conversion factors: To convert HDL-C and LDL-C values to mmol/L, multiply                  Study equation.
               by 0.0259; triglyceride values to mmol/L, multiply by 0.0113.                             e
                                                                                                             Class of diabetes medications has been detailed in eTable 3 in Supplement 1.
               a
                   Starting with the base cohort of 287 438 patients with type 2 diabetes,               f
                                                                                                             Including angiotensin-converting enzyme inhibitors and angiotensin
                   an algorithm (Figure 1) was implemented that resulted in a total of 39 267
                                                                                                             receptor blockers.
                   nonsurgical patients before matching (see Methods).
               b
                   Standardized differences are the absolute value of the difference in means
```

The two-column footnote continues: "or proportions between the groups (metabolic surgery − nonsurgical control group) divided by pooled standard deviation." The statement is retained as printed. Table1's baseline means/proportions and pooled SD are not provided separately from its median/IQR and count/proportion displays.

## Completion and limitations

Mapped units: 12/12. Numeric relationship groups: 59 (N001-N059). Statistical relationships: 24 (S001-S024). All Table1 rows, Table2 rows, Figures1-5 panels, captions and footnotes and matching prose are mapped. No scientific coverage gap. Exact unlabeled graph trajectories are unavailable as printed numeric point values; main captions identify the companion supplement tables. Main native text and direct page7 image agree for Table2 numeric cells. Complete direct transcription is retained at `extraction/main_direct_layout.txt`; direct rendering at `extraction/main_direct_page_007.png`. No candidate judgment was made.
