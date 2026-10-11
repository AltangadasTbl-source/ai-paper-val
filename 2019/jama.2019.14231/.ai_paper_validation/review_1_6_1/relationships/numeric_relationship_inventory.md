# Stable numeric relationship inventory

Fresh numeric_consistency_reviewer, runtime root/numeric_checker. Complete assigned scope: DOC-001 REPORT physical PDF pp. 1–12; DOC-002 REPORT pp. 1–20; DOC-003 PLAN pp. 1–7. All 77 numeric groups are retained under their mapper IDs, N001–N059 and N101–N118; unused IDs N060–N100 are reserved, not missing groups. The mapping crosswalk is identity: each numeric inventory ID below maps to the same ID in its named evidence map. Every member row, subgroup, time point and treatment in each group was reviewed; grouping is never sampling. Full values remain in the source-linked evidence maps. No legacy conclusions or external evidence were used.

Population keys: surgery 2287, eligible nonsurgical 39267, matched nonsurgical 11435. Matching separates endpoint-specific risk sets, repeated observations versus distinct persons, event rates versus cumulative incidence, modeled contrasts versus crude arithmetic, index-date characteristics versus follow-up quantities, and REPORT versus PLAN content. Exact integers retain their integer meaning; for conservative display checks an optional half-unit interval on integer inputs was also allowed. Each printed decimal value retains a half-unit interval at its displayed final decimal place. Source codes and historical/reference quantities are mapped, but are not outcome counts.

## Main crosswalk and complete member scope

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


## Support crosswalk and complete member scope

| ID | Locations | Relationship members and matching key |
|---|---|---|
| N101 | DOC-002 p2 eTable 1 | Every diagnosis/procedure code in 16 conditions/procedure categories; preserve code systems and primary-diagnosis bolding instruction. Codes are identifiers, not event counts. Nephropathy requires at least two eGFR measures below 60 mL/min, separated by ≥90 days, no intervening value ≥60, MDRD equation. Match main endpoint definitions and plan p4. |
| N102 | DOC-002 pp3–4 eTable 2 | Acute pulmonary complications; acute renal failure plus dialysis; DVT/PE; transfusion; TPN; endoscopy; interventional radiology; cholecystectomy; abdominal wall hernia; abdominal surgery including revisions, adhesions, internal hernia and other procedures. Each full code list is retained in source blocks; conjunctive renal/dialysis condition retained. Match main adverse-event results and protocol amendment. |
| N103 | DOC-002 p5 eTable 3 | Surgery N=2287, matched nonsurgical N=11435; 12 rows: alpha-glucosidase 6(0.3)/26(0.2); amylin 7(0.3)/27(0.2); biguanides 1530(67.9)/7606(66.5); bile acid sequestrants 8(0.3)/55(0.5); dopamine agonists 3(0.1)/14(0.1); DPP-4 214(9.4)/1202(10.5); GLP-1 270(11.8)/841(7.4); insulin 776(33.9)/3806(33.3); meglitinides 20(0.9)/79(0.7); sulfonylureas 509(22.3)/3404(29.8); SGLT2 43(1.9)/143(1.3); thiazolidinediones 286(12.5)/1083(9.5). All percentages as printed; match baseline index-date medication classification, not follow-up drug denominators. |
| N104 | DOC-002 p6 eTable 4 | Surgery/control cause-specific rates per 100 patient-years at eight years: primary 4.51/7.45; secondary 2.11/3.64; death 1.19/2.22; HF .92/2.49; CAD 1.03/1.55; cerebrovascular .45/.73; nephropathy .89/2.07; AF 1.14/1.77. Parentheses give outcome-or-death composites: HF 1.84/3.7; CAD 1.98/3.36; cerebrovascular 1.55/2.74; nephropathy 1.77/3.47; AF 2.16/3.42. Differences and CI are S103; do not match these rates to risk percentages. |
| N105 | DOC-002 p7 eTable 5 | All 48 cumulative incidence percentages at 2,5,8 years, exact outcome/treatment/time keys in source block. Eight-year primary 30.8(27.6,34) vs47.7(46.1,49.2); secondary17(14.3,19.7) vs27.6(26.2,29); death10(7.8,12.2) vs17.8(16.6,19). Match main cumulative incidence displays using time and risk sets. |
| N106 | DOC-002 p11 eFigure 2 | HbA1c (%) and percent taking noninsulin drugs versus time0–4 years; surgery/nonsurgery × baseline BMI<35/≥35 kg/m². Graphical values have no printed numeric point labels; no exact digitization implied. All eight curves inspected. |
| N107 | DOC-002 p12 eTable 8 | Thirteen rows: weight pounds and equivalent kg; HbA1c%; protein, albumin, hemoglobin g/dL; vitaminD25 ug/L; six medication classes expressed in percentage points. All four time points1,2,5,8 have exact estimate/CI/P cells in source block. Weight kg estimates −25.7,−33.4,−20.5,−20.3; HbA1c −1.5,−1.6,−1.0,−1.1. Table heading says average change from baseline in surgery vs nonsurgery. Match main longitudinal change summaries with S109 model key. |
| N108 | DOC-002 p13 eTable 9 | All120 counts retained, distinguished as total observations vs distinct patients available after each time point0,1,2,5,8, surgery/nonsurgery; six variables HbA1c, weight, albumin, hemoglobin, protein, vitaminD25. These are repeated-measure availability counts, not randomized or endpoint risk-set totals. |
| N109 | DOC-002 p14 eTable 10 | Medication proportion sample sizes at0,1,2,5,8 years respectively surgery/control:2287/11433,1820/10309,1444/8762,784/4235,348/1219. Exact title/key retained. |
| N110 | DOC-002 p15 eTable 11 | All24 cumulative intervention incidences/95% CIs at1,2,5,8 years, surgery only; six rows TPN, endoscopy, interventional radiology, abdominal surgical procedure, abdominal wall hernia repair, cholecystectomy. Abdominal surgery excludes hernia repair/cholecystectomy. |
| N111 | DOC-002 p16 eFigure 3 | Four nutritional absolute mean trend panels0–8 years: albumin/hemoglobin/protein g/dL and vitaminD25 ug/L, surgery/nonsurgery. No printed exact point estimates. All eight curves inspected; match eTable8 differences by model/scale before comparison. |
| N112 | DOC-002 pp17–18 | Five random date assignments × ratios1:1,1:5,1:10 =15 datasets. Significant HRs in all15 for primary,secondary,death,HF,nephropathy;13 cerebrovascular,12CAD,11AF. Full model, treatment surgery/control; no individual graphic estimate has numeric annotation. |
| N113 | DOC-002 p20 eTable12 | E-value pairs for HR/upper95% limit: primary2.15/1.92;secondary2.62/2.11;death2.81/2.13;HF4.69/3.52;CAD2.27/1.55;cerebrovascular2.35/1.31;nephropathy4.46/3.29;AF1.9/1.21. All40 comparison risk-factor HRs and intervals retained, including changing reference categories. |
| N114 | DOC-003 p2 | Jan6,2019 original protocol; EHR throughDec31,2018; surgery throughDec31,2017; age18–80;BMI≥30;T2DM HbA1c>6.4% or medication;closest priorBMI required. ED admission5-day exclusion;cancer1-year;EF<20%;liver/heart/lung transplant;upperGI cancer/peptic-ulcer hospitalization exclusions. |
| N115 | DOC-003 p3 | Controls:single random surgical index date;last follow-up on/before date excluded;death before orwithin30days excluded;HbA1c<6.5 ANDno diabetes medication excluded;age<18/>80;BMI<30;closest prior BMI otherwise nearest absolute-time value. Five replicated control derivations. Base T2DM cohort approximatelyN287438, earliest datesJan1,1998–Dec31,2017. Abnormal glucose random>200mg/dL or fasting>125mg/dL. |
| N116 | DOC-003 pp4–5 | Six individual outcomes death,CAD,cerebrovascular,HF,nephropathy,AF;primary composite of all six;secondary death,MI,ischemic stroke. First occurrence after index date;baseline conditions omitted from composite definitions;individual historical outcome excluded from risk set;nephropathy excludes baseline eGFR<60/history dialysis. |
| N117 | DOC-003 p6 | Rates per100patient-years;five imputed datasets;alpha.05;95%CI;five date samples ×three matching ratios=15datasets;single1:5 dataset reported;time-varying HRs2,5,8 years;R3.5.0. |
| N118 | DOC-003 p7 | AmendmentAug2,2019;early adverse events<90days aftersurgery;late interventions until last follow-up;E-values for all8composite/individual endpoints, HR point and95%CI limitclosest null. |


## Complete review record

| IDs | Checks applied to every member | Result and explicit qualifications |
|---|---|---|
| N001, N002 | Base split, each flow subtraction, eligible and matched totals, ratio, repeated cohort totals | COMPLETE: 2818+284620=287438; 2818−61−470=2287; 284620−195677=88943; 88943−49676=39267; 39267−27832=11435; 2287+11435=13722; 11435=5×2287. 116031+79646=195677. |
| N003 | All seven surgical and eight control exclusion reason counts against enrollment exclusions | COMPLETE: reason sums 657 and 67489 exceed 470 and 49676; explicit multiple-criteria footnote resolves this. |
| N004, N114, N115 | Every numeric cohort threshold/window/date and supplied definition; role/population matching | COMPLETE: age, BMI, glucose/HbA1c, transplant/EF and date windows preserved; no unsupported raw-data reconstruction. HbA1c >6.4 versus ≥6.5 terminology considered at usual display scale; plan matching direction interpreted with p6 and actual cohort. |
| N005, N006 | All procedure and BMI partitions and percentages, prose/table matches | COMPLETE: 1443+730+109+5=2287; 1713+465+109=2287. Whole-percent narrative agrees with one-decimal table after precision allowance. |
| N007, N008, N010, N012, N014 | Every median/IQR, unit, missingness and repeated narrative occurrence | COMPLETE: all medians contained by IQRs; time/quantity keys agree. No means or SDs invented from medians/IQRs. |
| N009, N011, N013, N015, N016 | Every categorical cell, percentage and row/column partition in all three populations | COMPLETE: sex, BMI, race, smoking and location category sums equal each column N. 18895/39267 gives 48.119%, compared with printed 48.2%; screened as immediate-context baseline display slip. |
| N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029 | Every baseline medical count/percentage and relevant initial-risk-set subtraction | COMPLETE: HF 2287−238=2049,11435−1342=10093; CAD 2287−237=2050,11435−1104=10331; AF 2287−152=2135,11435−701=10734; cerebrovascular 2287−42=2245,11435−358=11077. Nephropathy risk set has additional baseline eGFR/dialysis exclusion, so baseline history alone is not its denominator rule. Conditions overlap and are not a partition. |
| N030, N031, N032, N033, N034, N035, N036, N037 | Every lab median/IQR, missing count/percentage, scale and conversion factor | COMPLETE: coherent median/IQR ordering and missing counts within each population; BP missing 0/234/54 reconciles. UACR eligible-control missing 14665/39267=37.3469% versus printed 37.4% is screened as immediate-context display slip. Conversion units preserved. |
| N038, N039, N040, N041, N042, N043, N044 | Every medication count/percentage, noninsulin class partition and prose match | COMPLETE: surgery 418+1088+560+221=2287 and users1088+560+221=1869; eligible controls6839+18206+10084+4138=39267 and users32428; matched2182+5218+2929+1106=11435 and users9253. Other classes overlap; no summation across classes imposed. |
| N045, N046, N047 | All event counts and matching denominators in abstract, prose, tables and figures | COMPLETE: primary385/3243,secondary194/1765,deaths112/1111 agree between matched occurrences; all within N2287/11435. Crude risks differ from eight-year KM values by estimand and censoring; adjusted HRs are not crude ratios. |
| N048, N049 | Every one of 80 figure risk counts, all endpoint medians/IQRs, initial risk sets and decreasing time order | COMPLETE: nonnegative nonincreasing risk sequences; all time-zero values match Table2 and history exclusions. Counts at years2/4/6/8 are contributor counts, not eight-year analyzed cohort totals. |
| N050, N051 | Both weight-reduction means, kg contrast, percent-loss contrast, HbA1c contrast and repeated locations | COMPLETE: 29.1−8.7 gives20.4 at central displayed values, but allowable difference20.30–20.50 overlaps20.3 interval20.25–20.35; no finding. Kg and percent effects are different scales; 95% and98.8% intervals are different coverage levels. |
| N052, N057 | All six medication panels, scales/time windows, newer-agent exposure statement | COMPLETE: graphical proportions bounded by scale; no unprinted exact values inferred. Prescription proportions distinguished from actual consumption. |
| N053, N054 | Every early adverse-event count/percentage, zero cerebrovascular events, denominator/window and length-of-stay summary | COMPLETE: all eight printed early count/percentage pairs reconcile at surgery N2287; overlapping adverse events are not a partition. Median2 within IQR2–3. Unpaired endoscopy/radiology/TPN percentages have no printed counts to reconstruct. |
| N055, N112, N117 | Every sensitivity dataset count, ratio, time and endpoint count | COMPLETE: five date samples ×three ratios=15 datasets; eight endpoints imply120 plotted treatment effect pairs; supplied significance counts13/12/11 ≤15. Five imputations are a different dataset operation. |
| N056 | Primary and mortality narrative repetitions and all endpoint directions | COMPLETE: primary47.7/30.8 rounds to48/31; mortalityARD7.8 agrees; all constant adjusted HRs <1. |
| N058 | Every supplied historical quantitative example | COMPLETE: recorded and separated from study results; no external verification or raw-data interpretation required. |
| N059 | All signed standardized-difference cells and footnote definition | COMPLETE: signed versus absolute convention is immediately apparent; exact mean-based reconstruction unavailable from median/IQR display and pooled SD is not supplied. |
| N101, N102, N116, N118 | Every code/threshold/window and outcome/adverse-event definition | COMPLETE: code numbers are identifiers; primary six/secondary three/total eight endpoints agree. Amendment discloses added adverse-event/E-value analyses; late intervention probabilities are not early90-day crude proportions. |
| N103 | All24 index-date medication count/percentage pairs, two denominators | COMPLETE: surgery biguanides1530/2287=66.8999% versus67.9%; isolated one-digit baseline display inconsistency screened conservatively as context resolves; every other pair reconciles. |
| N104 | All16 individual rates, ten parenthetic outcome-or-death rates, eight control−surgery differences | COMPLETE: rate differences2.94,1.53,1.03,1.57,.52,.28,1.18,.63 reconcile exactly from displayed rates. Person-time denominators are not printed; no HR=rate-ratio identity imposed. |
| N105 | All48 cumulative incidence estimates and96 CI bounds at years2/5/8; main matched eight-year rows | COMPLETE: every estimate lies inside ordered interval and estimates increase over time. All main/eTable5 matched values agree. Table2 five nonfatal ARDs do not reconcile with their incidences; F-NUM-001. |
| N106, N111 | All curves and time/scale/BMI keys in eFigures2/3 | COMPLETE: no exact digitization; modeled differences distinguished from plotted absolute levels. |
| N107 | All52 longitudinal effect/interval/P triplets, weight unit conversion, all13 rows at four times | COMPLETE: points contained in intervals and bounds ordered; four kg/lb conversions reconcile with rounding. Bonferroni98.8% interval level retained. No unreported covariance implied. |
| N108 | All120 repeated-observation and distinct-person counts at five times/six variables/two groups | COMPLETE: each observation count ≥distinct patients; all patient counts ≤group N; both count types decrease with later availability threshold. Follow-up measurements do not equal baseline missingness counts. |
| N109 | All10 proportion denominators at five times/two groups | COMPLETE: declining series within group N; nonsurgical time-zero11433 versus baseline11435 is a peripheral contributor-count comparison, not a replacement of the endpoint analysis population. |
| N110 | All24 intervention cumulative incidences and48 bounds | COMPLETE: coherent nondecreasing cumulative incidence and all estimates inside ordered CIs; mutually overlapping intervention categories and explicit abdominal exclusions preserved. |
| N113 | All16 E-values,40 covariate HR/CI pairs and reference directions | COMPLETE: E-values ≥1 with point E-value ≥CI-limit E-value; all covariate point estimates inside ordered intervals. No conversion formula supplied, so no unique unsupported reconstruction imposed. |

138 three-column Table1 count/percentage cells were also evaluated with JavaScript arithmetic in the direct tool orchestrator; the two isolated baseline display observations above were the only non-overlaps after correct cell alignment. The six two-column BP missingness cells and all remaining count/percentage groups were inspected separately. The arithmetic helper did not classify findings or replace source reasoning. All77groups reviewed; no quantitative relationship omitted.

## Limitations

Printed cumulative incidence/rate/HR displays do not supply raw risk histories, person-time totals, Cox coefficients/covariance, or individual longitudinal observations. Exact unannotated graph points are unavailable. These limitations restrict reconstruction but do not create a scientific coverage gap. Source and reusable evidence remain unchanged.
