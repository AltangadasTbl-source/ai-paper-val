# Main-paper quantitative evidence map — DOC-001

Scope: `jama_lappe_2017_oi_170019.pdf`, PDF pp. 1-10. Evidence was mapped from the fresh native/layout assets in `preprocessing/` and the supplied PDF/page renderings for Figure 1, Tables 1-3, and Figure 2. Locations below use PDF page numbers, with the printed journal page when useful. This is an evidence inventory only; it makes no candidate determination or adjudication.

## Page coverage

| PDF page | Printed page | Result-relevant coverage | Records |
|---:|---:|---|---|
| 1 | 1234 | Abstract: design, intervention, cohort, completion, primary incidence, KM/Cox, adverse events | MN001-MN008; MS001-MS004 |
| 2 | 1235 | Methods: population, allocation/intervention, outcome definition and follow-up cadence | MN009-MN012 |
| 3 | 1236 | Sample-size assumptions; analysis populations, models, time rule, post-hoc definitions | MN013-MN016; MS005-MS006 |
| 4 | 1237 | Figure 1 and results baseline/flow/completion totals | MN017-MN020; MS007 |
| 5 | 1238 | Tables 1-2 baseline and longitudinal numeric displays | MN021-MN030; MS008-MS012 |
| 6 | 1239 | Figure 2, primary/breast-cancer analyses, event composition, covariate/adherence results | MN031-MN035; MS013-MS019 |
| 7 | 1240 | Table 3, discontinuation/adverse events, post-hoc cancer and 25(OH)D results | MN036-MN042; MS020-MS022 |
| 8 | 1241 | Discussion repeats/defines exploratory post-hoc interpretation and comparative quantitative context | MN043-MN046; MS023-MS024 |
| 9 | 1242 | Conclusion repeats population, baseline level, intervention comparison and 4-year endpoint | MN047; MS025 |
| 10 | 1243 | References only; no main-study result unit or result-defining quantitative display | NONE |

## Numeric/reporting relationships

| Local ID | Exact source location and evidence | Population/time/contrast, labels and cross-document match key |
|---|---|---|
| MN001 | p1 Abstract: 4-year double-blind placebo-controlled trial in 31 rural counties, June 24 2009-August 26 2015; 2303 women aged >=55 randomized: 1156 treatment, 1147 placebo. | `MAIN:trial-design-randomized-N2303`; D3 2000 IU/d + calcium 1500 mg/d versus identical placebo. |
| MN002 | p1 Abstract: mean age 65.2 y (SD 7.0); baseline serum 25(OH)D 32.8 ng/mL (SD 10.5); 2064/2303 (90%) completed. | `MAIN:baseline-age-vitD-completion`; overall randomized cohort. |
| MN003 | p1 Abstract: year-1 25(OH)D 43.9 ng/mL treatment and 31.6 ng/mL placebo. | `MAIN:25OHD-12mo`; unit ng/mL. |
| MN004 | p1 Abstract: confirmed cancer 109 total: 45/1156 (3.89%) treatment and 64/1147 (5.58%) placebo; absolute difference 1.69% (95% CI -0.06% to 3.46%). | `MAIN:ITT-all-cancer-count-proportion`; all-type cancer, 4 years. |
| MN005 | p1 Abstract: 4-y KM incidence 0.042 (95% CI 0.032-0.056) treatment and 0.060 (0.048-0.076) placebo. | `MAIN:KM-all-cancer-4y`; follow-up subset as later specified. |
| MN006 | p1 Abstract: unadjusted Cox HR 0.70 (95% CI 0.47-1.02). | `MAIN:Cox-all-cancer-unadjusted`; treatment versus placebo. |
| MN007 | p1 Abstract: potential adverse events: renal calculi 16 treatment/10 placebo; elevated serum calcium 6/2. | `MAIN:adverse-events-calculi-hypercalcemia`. |
| MN008 | p1 Abstract primary outcome: all-type cancer excluding nonmelanoma skin cancers, evaluated with KM and proportional hazards modeling. | `MAIN:primary-outcome-definition`. |
| MN009 | p2 Methods: postmenopausal women >=55 from 31 of 93 Nebraska counties; recruitment lists covered about 99% occupied housing units. | `MAIN:population-geography-eligibility`. |
| MN010 | p2 Methods: block randomization block size 8; cholecalciferol 2000-IU capsule once daily + calcium carbonate 500-mg tablet three times daily; external vitamin D limited to 800 IU/d, additional calcium to 1500 mg/d; visits every 6 mo. | `MAIN:intervention-dose-followup`. |
| MN011 | p2 Methods: primary first diagnosis of any cancer excluding nonmelanoma skin cancer; participant with new cancer counted once; prespecified cancers breast/lung/colon and lymphoma/leukemia/myeloma. | `MAIN:outcome-event-counting-secondary-sites`. |
| MN012 | p2 Methods: diagnoses/tumors/adenomas reported each visit; medical record/pathology verification and cancer deaths captured. | `MAIN:outcome-ascertainment`. |
| MN013 | p3 Sample Size: prior study placebo 20/288=6.9% over 4 y, stated 1.78%/y; D3+calcium 13/446=2.9%, stated 0.74%/y; RR 2.9%/6.9% about 40%; planned detect 50% reduction. | `MAIN:sample-size-prior-study`. |
| MN014 | p3 Sample Size: 1000/group power 94.4% for annual rates 2% control/1% treatment; 86.2% for 1.5%/0.75%; 68.5% for 1%/0.5%. | `MAIN:sample-size-power-scenarios`. |
| MN015 | p3 Analysis: time enrollment to outcome/death/last or ninth visit; truncated at 4 y; cancers >4 y excluded. ITT all-site and breast; KM/censoring subset excludes pre-visit-2 withdrawal with no follow-up; post-hoc chi-square scores all randomized/no-follow-up as cancer-negative. | `MAIN:analysis-population-time-rule`. |
| MN016 | p3 Post hoc: years 2-4 excludes cancer/withdrawal before completing year 1; 25(OH)D Cox adjustment covariates age, smoking, BMI (kg/m2), hormone use, family history; two-sided alpha .05; SAS 9.4. | `MAIN:posthoc-definitions-model`. |
| MN017 | p4 Fig 1 flow: 5146 assessed; 2843 excluded (791 inclusion criteria: residence 60, age/sex/menopause 186, medical history 200, site access 96, prior study 239, reason missing 10; declined 2040; other 12); 2303 randomized. | `MAIN:CONSORT-screening-randomization`. |
| MN018 | p4 Fig 1: treatment 1156 received assigned; placebo 1147 received assigned. No-follow-up withdrawal 54 (7 lost,47 changed mind) versus 52 (5,47); partial-follow-up withdrawal 73 (15 lost,7 died,19 health,7 relocated,25 changed mind) versus 60 (9,9,10,6,26). | `MAIN:CONSORT-withdrawals`. |
| MN019 | p4 Fig 1: intervention discontinued 238 treatment (11 abnormal labs [10 calcium/creatinine,1 deficient 25(OH)D],93 adverse event,134 other [55 pills,28 own supplements,51 no reason]) versus 246 placebo (16 abnormal lab [10 calcium/creatinine,4 deficient 25(OH)D,2 bone density],76 adverse event,154 other [55,56,43]); primary analysis 1102 and 1095. | `MAIN:CONSORT-discontinuation-primary-analysis`. |
| MN020 | p4 narrative: randomization 1156 (50.2%) /1147; completion 2064/2303=89.6%, stated 89.0% treatment/90.2% placebo; deaths 16 (7/9); primary-analysis follow-up 1102/1095; completion difference 0.012 (95% CI -0.013 to 0.037), death difference 0.002 (-0.006 to 0.037); mean age 65.2, 99.5% non-Hispanic white. | `MAIN:flow-completion-baseline-narrative`. |
| MN021 | p5 Table 1 age/anthropometry: treatment vs placebo: age N1156 65.2 (SD6.9) vs N1147 65.2 (7.1) y; height N1135 162.1 (6.1) vs N1123 162.0 (6.3) cm; weight N1136 78.5 (18.0) vs N1124 79.3 (17.8) kg; BMI N1134 29.9 (6.6) vs N1121 30.2 (6.5). | `MAIN:T1-baseline-continuous`; BMI kg/m2. |
| MN022 | p5 Table 1 baseline supplements/diet, median (IQR): calcium mg/d N1156 600 (5-1050) vs N1147 600 (0-1000); vitamin D IU/d N1156 734 (100-1200) vs N1147 700 (0-1000); dietary calcium mg/d N1140 641 (460-893) vs N1116 641 (454-892); dietary D IU/d N1140 103 (60-176) vs N1116 107 (60-173). | `MAIN:T1-baseline-intake`. |
| MN023 | p5 Table 1 race/ethnicity N(%): white 1149(99.4)/1142(99.6); American Indian/Alaska Native 4(0.4)/4(0.3); Asian, black, unknown 3(0.3)/1(0.1); Hispanic 9(0.8)/2(0.2). | `MAIN:T1-race-ethnicity`. |
| MN024 | p5 Table 1 N(%): surgical menopause 423(36.6)/389(33.9); bilateral oophorectomy 315(27.3)/280(24.4); current smoking 75(6.5)/66(5.7); never smoking 768(66.4)/773(67.4); estrogen therapy 186(16.1)/168(14.7); estrogen agonist/antagonist 19(1.64)/38(3.3). | `MAIN:T1-baseline-clinical`. |
| MN025 | p5 Table 2 25(OH)D ng/mL treatment/placebo mean (95% CI): baseline N1156 33.0 (32.3-33.6)/N1146 32.7 (32.1-33.3; one unavailable); 12 mo N989 43.9 (43.2-44.7)/N1002 31.6 (30.9-32.3), difference 12.3 (11.3-13.3). | `MAIN:T2-25OHD-baseline-12mo`. |
| MN026 | p5 Table 2 25(OH)D: 24 mo N966 44.3 (43.6-45.0)/N966 31.7 (31.0-32.4), diff 12.6 (11.6-13.6); 36 mo N938 45.1 (44.3-45.9)/N925 32.4 (31.7-33.1), diff 12.7 (11.63-13.8); 48 mo N980 42.5 (41.7-43.3)/N992 30.9 (30.2-31.6), diff 11.6 (10.6-12.7). | `MAIN:T2-25OHD-24-48mo`. |
| MN027 | p5 Table 2 25(OH)D mean visits 2-9: N1047 43.6 (42.9-44.3)/N1056 31.6 (31.0-32.2), diff 12.0 (11.1-12.9) ng/mL. | `MAIN:T2-25OHD-visits2-9`. |
| MN028 | p5 Table 2 outside-study visit 2-9: D3 IU/d N1099 740 (691-789)/N1094 869 (803-934), diff -128.1 (-209.5 to 46.6); calcium mg/d N1099 500 (475-525)/N1994 [printed] 512 (489-536), diff -12.0 (-46.0 to 22.0). | `MAIN:T2-outside-supplements`; printed placebo calcium N is `1994`. |
| MN029 | p5 Table 2 dietary visit 1-9: D3 IU/d N1145 127.2 (121.7-132.7)/N1128 126.8 (121.4-132.2), diff 0.4 (-7.4 to 8.1); calcium mg/d N1145 680.2 (661.8-698.5)/N1128 672.1 (654.2-690.0), diff 8.1 (-17.6-33.7). SI conversion 25(OH)D: multiply by 2.496. | `MAIN:T2-dietary-intake-conversion`. |
| MN030 | p5 narrative repeats baseline mean 32.8 ng/mL and says no baseline between-group difference; postbaseline values higher treatment; 36-mo values 45.1 vs 32.4 ng/mL. | `MAIN:25OHD-36mo-narrative`. |
| MN031 | p6 Figure 2: y-axis proportion cancer 0-0.07; risk-set treatment 1102,1072,1042,1016,658 and placebo 1095,1069,1037,1008,659 at years 0-4; median follow-up 4 y both; excludes 54/52 no-follow-up. | `MAIN:Fig2-KM-risk-set`. |
| MN032 | p6 primary ITT repeats 45/1156 (3.89%) versus 64/1147 (5.58%); difference 1.69% (-0.06% to 3.46%); the analysis sets no-follow-up exclusions 54/52. | `MAIN:ITT-all-cancer-count-proportion`. |
| MN033 | p6 breast: 19 treatment/24 placebo, difference 0.005 (-0.007 to 0.016); KM breast incidence 0.018 (0.011-0.028) vs 0.023 (0.015-0.034). | `MAIN:breast-cancer-4y`. |
| MN034 | p6 event composition: 4/109 developed second primary, excluded; 2 second cancers (1 breast,1 colon) treatment/2 lymphomas placebo; first primaries 99 invasive/10 in situ; 194 adenomas in 181 participants, 2 in-situ colorectum cancers. | `MAIN:all-cancer-event-composition`. |
| MN035 | p6 adherence: D3/placebo 75.4% vs 76.6%, mean diff -1.17 (-3.88 to1.55); calcium/placebo 57.7% vs59.4%, diff -1.7 (-4.51 to1.10); includes discontinuers. | `MAIN:adherence-mean`. |
| MN036 | p7 Table 3 cancer-site rows as [Y1 treatment/placebo/total; Y2-4 treatment/placebo/total; Y1-4 treatment/placebo/total]: breast [4/5/9;12/18/30;16/23/39]; breast in situ [1/0/1;2/1/3;3/1/4]; colon/rectum [0/0/0;4/4/8;4/4/8]; colon/rectum in situ [0/0/0;0/2/2;0/2/2]. | `MAIN:T3-sites-breast-colorectal`. |
| MN037 | p7 Table 3: endometrium [0/1/1;2/2/4;2/3/5]; lung [1/0/1;4/2/6;5/2/7]; melanoma [0/1/1;1/1/2;1/2/3]; melanoma in situ [0/0/0;1/2/3;1/2/3]; neuroendocrine [1/0/1;1/4/5;2/4/6]; ovary [0/0/0;0/5/5;0/5/5]. | `MAIN:T3-sites-other`. |
| MN038 | p7 Table 3: other [4/5/9;7/10/17;11/15/26]; other in situ [0/0/0;0/1/1;0/1/1]; total [11/12/23;34/52/86;45/64/109]. Footnote other sites with <=2: anal,biliary,bladder,brain,cervix,esophagus,kidney,leukemia,lymphoma,meningioma,myeloma,pancreas,sarcoma,thyroid,vagina,unknown. | `MAIN:T3-sites-total-footnote`. |
| MN039 | p7: supplement stopped 304/2303=13.2% (12.4% treatment,14.0% placebo); calcium/placebo stopped 474/2303=20.6% (20.3%,20.8%); differences 0.017 (-0.011 to0.044) and 0.005 (-0.028 to0.038). | `MAIN:discontinuation-proportions`. |
| MN040 | p7 safety: renal calculi 26, 16/1156=1.4% vs10/1147=0.9%, difference 0.005 (-0.004 to0.015); one high calcium value in 8 (6/2), difference 0.003 (-0.002 to0.010). | `MAIN:safety-calculi-calcium`. |
| MN041 | p7 post-hoc years2-4: exclusions 84 treatment/78 placebo; cancer 34 treatment/52 placebo; chi-square proportions 3.17% vs4.86%, difference 1.7% (0.1%-3.4%). | `MAIN:posthoc-years2-4-count-proportion`. |
| MN042 | p7 post-hoc achieved 25(OH)D: coefficient -0.017; baseline comparison level 30 ng/mL; estimated HR 0.65 (0.44-0.97) for 30-55 ng/mL. | `MAIN:posthoc-25OHD-HR`. |
| MN043 | p8 discussion: assigned doses 1000-mg calcium/400-IU D daily WHI; 600 IU/d D age50-70 and800 IU/d >=70 NAM; current trial dose 2000 IU/d D plus1500 mg/d calcium. | `MAIN:discussion-dose-context`. |
| MN044 | p8 prior Lappe trial entire cohort baseline 25(OH)D 28.7 ng/mL (SD8.1); D3+calcium RR0.40 (0.20-0.82); calcium RR0.53 (0.27-1.03); excluding year1 D3+calcium RR0.23 (0.09-0.60), calcium RR0.59 (0.29-1.21). | `MAIN:discussion-prior-Lappe-comparative`. |
| MN045 | p8 external comparative context: UK 100000 IU D every4 mo RR1.11(0.86-1.42); RECORD 800 IU/d D+1000mg/d calcium; WHI nested case-control RR2.53(1.49-4.32); WHI stone HR1.17(1.02-1.34). | `MAIN:discussion-external-RCT-observational`. |
| MN046 | p8 current safety contextualizes calculi 1.4% treatment/0.9% placebo versus 0.3% over4y Rochester older women; adherence censoring threshold <80%. | `MAIN:safety-context-adherence`. |
| MN047 | p9 conclusion: healthy postmenopausal older women mean baseline 25(OH)D32.8ng/mL; D3+calcium vs placebo no significantly lower all-type cancer risk at4y. | `MAIN:conclusion-primary-result`. |

No additional result-relevant quantitative relationship appeared on PDF p10; bibliographic page-number data were not mapped as study results.
