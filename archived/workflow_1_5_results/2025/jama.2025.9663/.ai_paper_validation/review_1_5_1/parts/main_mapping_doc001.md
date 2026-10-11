# DOC-001 Main-Paper Quantitative Evidence Map

## Scope and method

- **Direct source:** `jama_martin_2025_oi_250042_1753377747.91025.pdf`, PDF pp. 1-11 (printed article pp. 398-408).
- **Scope completed:** every direct-source page. Native reusable text was used to locate content, then all values below were confirmed against a fresh direct `pdftotext -layout` extraction of the PDF. Pages 8-11 contain conclusion, article information, and references only; no additional trial-result relationships beyond the repeated conclusion occur there.
- **ID convention:** `MAIN-N` is a numeric/reporting relationship; `MAIN-S` is an inferential/statistical relationship. These are provisional mapper IDs, not candidate IDs or judgments.
- **Candidate observation convention:** observations below preserve a source-grounded issue for later independent checking; they are not adjudications.

## PDF p. 1 — Abstract (printed p. 398)

| ID | Relationship and exact printed evidence | Population/time/contrast and cross-location link |
|---|---|---|
| MAIN-N001 | Trial population: 97 UK ICUs; 16,500 mechanically ventilated adults receiving supplemental oxygen; enrollment May 2021-November 2024; follow-up completed February 2025. | All randomized population; matches p. 3 Results and Figure 1 site/randomized totals. |
| MAIN-N002 | Intervention: conservative oxygen `n = 8258`, lowest possible inspired oxygen fraction to maintain SpO2 90% (range 88%-92%); usual oxygen `n = 8242`, clinician discretion. | Randomized contrast; matches Figure 1, p. 3. |
| MAIN-S001 | Primary outcome is all-cause mortality at 90 days. | Prespecified primary endpoint; Table 2 and p. 4 text. |
| MAIN-N003 | Primary-outcome data available: 16,394/16,500, comprising 8211 conservative and 8183 usual. Median age 60 years (IQR 48-71); females 38.2% in both groups, combined `n = 5652`. | Matches Figure 1 and Table 1 (female counts 2803 + 2849 = 5652). |
| MAIN-N004 | Supplemental-oxygen exposure was 29% lower in conservative therapy. Death by day 90: 2908 (35.4%) conservative vs 2858 (34.9%) usual. | Matches p. 4 exposure (29.3%, 20.3 vs 28.7 100%-equivalent hours) and Table 2 death counts. |
| MAIN-S002 | Adjusted 90-day risk difference (RD) `0.7 percentage points (95% CI, -0.7 to 2.0; P = .28)`. | Conservative minus usual; matches Table 2 multiply imputed and p. 4 primary-outcome text. |

## PDF p. 2 — Design, methods, and analysis specifications (printed p. 399)

| ID | Relationship and exact printed evidence | Population/time/contrast/model/unit |
|---|---|---|
| MAIN-N005 | Randomization was 1:1, permuted variable blocks, stratified by site and hierarchical diagnostic subgroup: HIE, sepsis, acute brain injury except HIE, or none. | Allocation definition relevant to adjusted models/subgroups. |
| MAIN-N006 | Conservative target SpO2 90%; allowed range 88%-92%; intervention continued through day 90 or ICU discharge, whichever came first. | Intervention time and scale. |
| MAIN-N007 | Oxygen exposure: FIO2 above room air (0.21); 1 hour at FIO2 1.0 or 2 hours at 0.605 each equal one 100%-equivalent hour (additional 79% oxygen). Enhanced data: first 10 patients/site then random 10% of subsequent patients, approximately 15% overall. | Exposure definition used for Figure 2/p. 4. |
| MAIN-N008 | Sample-size inputs: CMP April 28, 2017-March 2019 `n = 96,028`; Risk II April 2014-March 2016 `n = 82,075`; anticipated usual 90-day mortality 37%; 6% loss to follow-up; sample size 16,500; 90% power at P < .05 for absolute reduction 2.5 percentage points to 34.5%. Interim analyses after 4500 and 10,000; Haybittle-Peto P < .001 for effectiveness/harm. | Planning quantities, not observed outcomes. |
| MAIN-S003 | Tests two-sided, significance P < .05 unless specified; effects with 95% CIs; no multiple-testing adjustment. Primary models adjusted for site, diagnostic subgroup, age, randomization SpO2, randomization PaO2:FIO2, COVID-19, and randomization date; all models account for site clustering. | General inferential framework. |
| MAIN-S004 | Binary outcomes: logistic regression; ICU/hospital survivor duration: Fine-Gray subdistribution hazards (death competing risk); organ-support-free days: ordered logistic; time to death: Cox model, censoring at earliest withdrawal, 365 days, or trial end. RD/RR via marginal standardization; missing secondary outcomes via chained-equation imputation. | Defines Table 2 labels/models. |
| MAIN-S005 | Prespecified primary-outcome subgroups: diagnostic subgroup, COVID-19, ethnicity; interactions tested on OR scale (jointly for multi-category variables). Post hoc: illness severity and data-collection subgroup. | Defines Figure 3 interaction P values. |

## PDF p. 4 — Participant flow and Results population (printed p. 400-401)

| ID | Relationship and exact printed evidence | Comparator/reconciliation |
|---|---|---|
| MAIN-N009 | Figure 1: screened 52,747; excluded 3514 = 3239 FIO2=0.21 during first 12 hours but met age + 243 age <18 but met FIO2 + 32 age <18 and FIO2=0.21; met inclusion 49,233. | `52,747 - 3,514 = 49,233`; exclusion components sum 3514. |
| MAIN-N010 | Figure 1: 10,754 exclusion-criteria exclusions = 10,582 one arm indicated/contraindicated + 108 previously randomized in last 90 days + 64 extracorporeal membrane oxygenation; 38,479 potentially eligible. | `49,233 - 10,754 = 38,479`; components sum 10,754. |
| MAIN-N011 | Figure 1: 21,979 eligible but not randomized = 14,865 missed/too late + 6589 clinical decision + 272 nonclinical decision + 213 prospectively refused + 40 no reason; 16,500 randomized. | `38,479 - 21,979 = 16,500`; components sum 21,979. |
| MAIN-N012 | Figure 1 arms: conservative 8258 and usual 8242; each received assigned/usual therapy. Requested all trial data removed: 28 conservative and 38 usual. Included primary analysis: 8230 and 8204. | Arm sum `8258 + 8242 = 16,500`; after removal `8258-28=8230`, `8242-38=8204`. |
| MAIN-N013 | Figure 1 primary data: conservative 8211; usual 8183; consent for linkage secondary outcomes 7463 and 7595; 12-month follow-up 6534 and 6518. Footnote: 40 primary outcomes could not link; 3382 had not reached 12 months at final linkage. | `8211 + 8183 = 16,394`; 16,434 primary-analysis population minus 16,394 recorded = 40. |
| MAIN-N014 | Results text: 97 sites, screening May 4, 2021-November 27, 2024; 52,747 screened; 38,479 potentially eligible; 16,500 enrolled. 66 (0.4%) requested data removal; another 40 (0.2%) primary outcome could not be linked. Imputed primary analysis `n=16,434` (8230/8204); recorded 8211/8183; 13,052 reached 12 months. | `28+38=66`; `8230+8204=16,434`; `6534+6518=13,052`. |
| MAIN-N015 | Baseline narrative: each group median age 60 (IQR 48-71), 5652 (38.2%) female; randomization 5 hours (IQR 2-8) in both. Pre-randomization SpO2 97% (94%-99%) vs 96% (94%-99%). | Matches Table 1. |
| MAIN-N016 | Diagnostic totals among all participants: HIE 1504 (9.2%); sepsis 5443 (33.1%); acute brain injury 363 (2.2%); none 9124 (55.5%); COVID-19 1099 (6.7%). | First four hierarchical categories sum 16,434; COVID is nonexclusive. Table 1 arm data match these sums. |
| MAIN-N017 | Enhanced collection selected 2489/16,434: 1252 conservative, 1237 usual. COVID proportion: nonrandom first-10 group 13.4%, subsequent random sample 5.3%, standard collection 6.4%. | Figure 2 denominators start at 1252/1237. |

## PDF p. 5 — Table 1 baseline characteristics (printed p. 402)

| ID | Exact printed values (conservative; usual) | Definition/cross-location |
|---|---|---|
| MAIN-N018 | Age: 60 (IQR 48-71) years `[8230]`; 60 (48-71) `[8204]`. | Primary analysis groups. |
| MAIN-N019 | Sex: female 2803/7340 (38.2%); 2849/7465 (38.2%). Male 4537/7340 (61.8%); 4616/7465 (61.8%). | Linkage-consent availability; each sex pair sums to stated denominator. |
| MAIN-N020 | Ethnicity: Asian 263/7340 (3.6%); 243/7465 (3.3%). Black 138 (1.9%); 153 (2.0%). White 6072 (82.7%); 6207 (83.1%). Mixed 52 (0.7%); 60 (0.8%). Other/not stated 815 (11.1%); 802 (10.7%). | Categories sum to 7340 and 7465, respectively. |
| MAIN-N021 | BMI: <18.5, 264/7111 (3.7%); 259/7225 (3.6%). 18.5-<25, 2291 (32.2%); 2299 (31.8%). 25-<30, 2129 (29.9%); 2250 (31.1%). 30-<40, 1918 (27.0%); 1881 (26.0%). >=40, 509 (7.2%); 536 (7.4%). | Categories sum to stated denominators. |
| MAIN-N022 | Preexisting severe respiratory disease 171/7310 (2.3%); 172/7436 (2.3%). Prior hospital stay 1 (IQR 1-3) days `[7293]`; 1 (1-3) `[7419]`. Prior invasive ventilation 5 (2-8) hours `[8230]`; 5 (2-8) `[8204]`. | Severe disease defined in footnote as dyspnea with light activity from pulmonary disease, evident within 6 months. |
| MAIN-N023 | Diagnosis: sepsis 2738/8230 (33.3%); 2705/8204 (33.0%). HIE 754 (9.2%); 750 (9.1%). Acute brain injury 183 (2.2%); 180 (2.2%). None 4555 (55.3%); 4569 (55.7%). COVID-19 536 (6.5%); 563 (6.9%). | First four hierarchical categories sum to arm totals; COVID nonexclusive. |
| MAIN-N024 | SpO2 median 97 (94-99)% `[8230]`; 96 (94-99)% `[8204]`. Categories: <88: 138 (1.7%);146 (1.8%); 88-92:995 (12.1%);1085 (13.2%);93-95:1979 (24.0%);1913 (23.3%);>95:5118 (62.2%);5060 (61.7%). | SpO2 category counts sum arm totals. |
| MAIN-N025 | FIO2 median 0.45 (0.35-0.60) `[8230]`; 0.45 (0.35-0.60) `[8204]`. PaO2 median 90 (75-116) mm Hg `[7638]`; 89 (74-114) `[7620]`. | SI conversion: multiply PaO2 and PaO2:FIO2 by 0.133 for kPa. |
| MAIN-N026 | PaO2:FIO2: <=100, 933/7638 (12.2%);936/7620 (12.3%). >100-<=200, 2635 (34.5%);2664 (35.0%). >200-<=300,1978 (25.9%);1977 (25.9%). >300,2092 (27.4%);2043 (26.8%). | Counts sum to PaO2 denominators. |
| MAIN-N027 | ICNARCH-2023 predicted death mean (SD) 0.35 (0.29) `[6882]`;0.34 (0.29) `[7014]`. APACHE II median 16 (12-21) `[7317]`;16 (12-21) `[7437]`; score range 0-71, higher is more severe. | Footnote details model covariates and first-24-hour physiological measures. |

## PDF p. 6 — Oxygen exposure, adherence, outcomes narrative (printed p. 403)

| ID | Relationship and exact printed evidence | Population/time/contrast |
|---|---|---|
| MAIN-N028 | Median FIO2 mean (SD): 0.31 (0.14) conservative vs 0.35 (0.15) usual. Total supplemental-oxygen exposure: 20.3 vs 28.7 100%-equivalent hours, 29.3% lower, difference -8.4 hours (95% CI -10.8 to -6.0). | Enhanced-data patients; matches abstract rounded 29% and Figure 2. |
| MAIN-N029 | Conservative median SpO2 mean (SD) 93.3% (2.8%) and median PaO2 71.5 (13.9) mm Hg; usual values printed as `95.1% (2.4%) mm Hg and 79.5 (17.9) mm Hg`, respectively. | See candidate observation O-001 below; intended paired measures require direct recheck. |
| MAIN-N030 | Hours mean (SD): SpO2 88%-92%, 62.6 (62.3) conservative vs 27.2 (39.1) usual; no supplemental oxygen, 39.7 (55.1) vs 26.1 (45.1); SpO2 <88%, 3.2 (6.5) vs 2.3 (7.3). | Enhanced data; Figure 2/eFigures/eTable 5 cited. |
| MAIN-N031 | Conservative enhanced-data adherence: 526 (42.1%) had >=1 nonadherence period; 10.6% of ICU time; 2271 periods >=3 h: staffing/lack awareness 857, other clinical priorities 413, low PaO2 127, unsupported clinical decision to suspend 265, reason undocumented 609. | Reason counts sum 2271. |
| MAIN-N032 | Primary mortality 2908/8211 (35.4%) vs 2858/8183 (34.9%). Unadjusted RD 0.5 pp (95% CI -1.0 to 2.0); adjusted RD 0.7 pp (95% CI -0.7 to 2.0; P=.28). PaO2:FIO2 was singly imputed from SpO2:FIO2 when otherwise missing. | Matches abstract/Table 2. |
| MAIN-S006 | Secondary mortality at ICU discharge, 60 days, 1 year; time-to-death adjusted HR 1.01 (95% CI 0.96-1.05); survivor hospital stay HR 0.98 (0.94-1.02); organ-support-free days proportional OR 1.01 (0.96-1.07), all reported not significant. | Table 2/eFigure sources. |
| MAIN-N033 | Survivor hospital stay: 20 days (IQR 11-40) conservative vs 21 (10-42) usual. Serious adverse events 58 (0.7%) vs 29 (0.4%). | Table 2 supports stay values; SAE is eTable 9. |
| MAIN-S007 | No statistically significant interactions for diagnostic subgroup, COVID-19, or ethnicity; post hoc collection subgroup described weak evidence of increased harm in first 10/site but no difference random enhanced sample vs standard. | Figure 3/eFigure 7; qualitative statistical claims. |

## PDF p. 7 — Figure 2, exposure trajectories (printed p. 404)

| ID | Relationship and exact printed evidence | Population/time/scale |
|---|---|---|
| MAIN-N034 | Figure 2 enhanced-data baseline counts: usual 1237, conservative 1252. FIO2 plot counts at days 2/4/6/8/10: usual 1011/801/639/501/403; conservative 1012/777/609/499/400. SpO2-with-oxygen plot: usual 837/637/500/378/287; conservative 647/493/386/313/240. | 0-10 days after randomization; plotted means with no numeric y-values printed beyond axes. |
| MAIN-N035 | Figure 2 categorized-SpO2 plot counts: conservative 1252/1012/777/609/499/400 and usual 1237/1011/801/639/501/403 at days 0/2/4/6/8/10. Categories `>92 without oxygen`, `>95 with oxygen`, `93-95 with oxygen`, `88-92`, `<88`; 88-92 includes participants whether or not receiving oxygen. | Percentage stacked display. |
| MAIN-N036 | Figure 2 cumulative exposure plot, 100%-oxygen-equivalent hours, usual and conservative; counts at days 0/2/4/6/8/10 identical to MAIN-N034 FIO2 plot. | Plotted endpoints are consistent with PDF p. 6 narrative 28.7 vs 20.3 hours, subject to visual—not tabular—precision. |

## PDF p. 8 — Table 2 primary and secondary outcomes (printed p. 405)

| ID | Exact printed evidence | Model/contrast/reconciliation |
|---|---|---|
| MAIN-S008 | Primary 90-day mortality: 2908/8211 (35.4%) vs 2858/8183 (34.9%). Available-case adjusted RD 0.7 (-0.6 to 2.1), RR 1.02 (0.98-1.06), OR 1.04 (0.97-1.11). Multiply-imputed RD 0.7 (-0.7 to 2.0), RR 1.02 (0.98-1.06), OR 1.04 (0.97-1.11); P=.28. | Conservative vs usual; matches MAIN-S002/MN032. |
| MAIN-N037 | ICU stay median (IQR) days [No.]: overall 6.6 (3.1-13.3) [7333] vs 6.8 (3.1-13.8) [7448]; survivors 7.3 (3.6-14.9) [5211] vs 7.7 (3.8-15.3) [5290]; nonsurvivors 4.9 (1.7-10.4) [2122] vs 4.6 (1.7-9.8) [2158]. | Survivor+nonsurvivor counts exactly equal overall counts by arm. |
| MAIN-S009 | ICU survivor duration sHR 1.00 (0.96-1.04), available case and imputed; P=.97. | Fine-Gray competing-risk model. |
| MAIN-N038 | Acute hospital stay: overall 14 (7-30) [7323] vs 14 (7-31) [7434]; survivors 20 (11-40) [4791] vs 21 (10-42) [4906]; nonsurvivors 7 (3-14) [2532] vs 7 (3-13) [2528]. | Subcounts equal overall. |
| MAIN-S010 | Hospital survivor duration sHR 0.98 (0.94-1.02), available case and imputed; P=.27. | Fine-Gray competing-risk model. |
| MAIN-N039 | Days alive and free from organ support at 30 days: 16 (-1 to 25) [7327] vs 16 (-1 to 25) [7444]. Component 30-day mortality 2435/7449 (32.7%) vs 2427/7573 (32.0%); survivors free days 23 (16-26) [4933] vs 23 (15-26) [5054]. | Ordinal composite: death on/before day 30 = -1; survivors ranked by calendar days free of respiratory/cardiovascular/renal support from day 1-30. Distinct available denominators are printed without an explanatory missingness breakdown. |
| MAIN-S011 | Organ-support-free-days POR: available case 1.00 (0.95-1.06), multiply imputed 1.01 (0.96-1.07); P=.64. | Proportional odds model; matches PDF p. 6. |
| MAIN-S012 | ICU-discharge mortality: 2122/7334 (28.9%) vs 2161/7453 (29.0%); RD 0.2 (-1.2 to 1.6) available case, -0.1 (-1.3 to 1.1) imputed; P=.94. | Adjusted RD. |
| MAIN-S013 | Acute-hospital-discharge mortality: 2533/7335 (34.5%) vs 2535/7458 (34.0%); RD 0.9 (-0.6 to 2.3), 0.5 (-0.8 to 1.9); P=.46. | Available case then imputed. |
| MAIN-S014 | 60-day mortality: 2637/7449 (35.4%) vs 2617/7573 (34.6%); RD 1.1 (-0.2 to 2.5), 0.8 (-0.6 to 2.2); P=.25. | Available case then imputed. |
| MAIN-S015 | One-year mortality: 2295/5636 (40.7%) vs 2314/5755 (40.2%); RD 1.0 (-0.7 to 2.6), 3.3 (-0.7 to 7.3); P=.34. | Available case then imputed; denominator reflects available 1-year linkage, not all randomized participants. |
| MAIN-S016 | Table footnote: all regression models adjusted for ICU site, diagnostic stratum, COVID-19, restricted cubic splines of age/SpO2/PaO2:FIO2 and randomization date. Multiple-imputation exception/handling printed: primary analysis adjusted above with multiple imputation except ICU/hospital duration, and patients with missing time to discharge included censored 1 hour after randomization. | Exact model/handling label essential for comparisons. |

## PDF p. 9 — Figure 3 subgroup primary outcome (printed p. 406)

| ID | Exact printed event data and estimates | Interaction/model information |
|---|---|---|
| MAIN-S017 | Diagnosis-HIE: 437/754 (58.0%) vs 438/748 (58.6%), RD -1.3 (-6.2 to 3.6), OR 0.94 (0.76-1.17). Sepsis:1010/2734 (36.9%) vs 986/2699 (36.5%), RD 0.9 (-1.6 to3.3), OR1.04 (0.93-1.17). Brain injury:78/183 (42.6%) vs83/179 (46.4%), RD -3.2 (-12.8 to6.5), OR0.86 (0.56-1.34). None:1383/4540 (30.5%) vs1351/4557 (29.6%), RD1.0 (-0.8 to2.8), OR1.05 (0.96-1.16). | Diagnosis interaction P=.67. Category denominators and death counts sum to the primary-outcome totals 8211/8183 and 2908/2858. |
| MAIN-S018 | COVID no:2665/7677 (34.7%) vs2577/7623 (33.8%), RD1.0 (-0.4 to2.4), OR1.05 (0.98-1.13). COVID yes:243/534 (45.5%) vs281/560 (50.2%), RD -3.7 (-9.3 to2.0), OR0.85 (0.66-1.09). | Interaction P=.11. COVID strata sum primary denominators/deaths. |
| MAIN-S019 | Ethnicity Asian:98/263 (37.3%) vs90/241 (37.3%), RD1.9 (-6.1 to9.9), OR1.10 (0.74-1.63). Black:35/138 (25.4%) vs50/152 (32.9%), RD -6.1 (-15.7 to3.4), OR0.71 (0.41-1.22). White:2236/6070 (36.8%) vs2215/6201 (35.7%), RD1.3 (-0.3 to2.9), OR1.07 (0.99-1.15). Mixed:12/52 (23.1%) vs15/60 (25.0%), RD -0 (-15.0 to14.9), OR1.00 (0.39-2.52). Other/not stated:296/808 (36.6%) vs294/796 (36.9%), RD -0.3 (-4.6 to4.1), OR0.99 (0.79-1.23). | Interaction P=.64. These ethnicity denominators differ from Table 1 linkage denominators (by outcome availability); groups sum to 7331/7450, so not the full primary-outcome population. |
| MAIN-S020 | Figure footnote: estimates adjusted for site, diagnostic subgroup, age, SpO2, PaO2:FIO2, COVID-19, date; interaction P values from adjusted multilevel logistic-regression OR-scale tests. Negative RD = observed lower mortality in conservative group. | Sign/direction definition. |

## PDF pp. 10-11 — Discussion, conclusion, article information, references (printed pp. 407-408)

| ID | Relationship and exact printed evidence | Cross-location |
|---|---|---|
| MAIN-N040 | Discussion restates observed adjusted absolute increase 0.7 percentage points, with 95% CI from 0.7-percentage-point reduction to 2.0-percentage-point increase; it states no significant primary subgroup or secondary-outcome differences. | Matches MAIN-S002/S008 and PDF p. 6 narrative. |
| MAIN-N041 | Discussion gives approximate usual-care SpO2 96% from external cited prior data and mentions 42.1% enhanced-data participants with nonadherence. | Former is context/reference; latter matches MAIN-N031. |
| MAIN-N042 | Conclusion: targeting SpO2 90% did not reduce 90-day all-cause mortality compared with usual oxygen. | Qualitative conclusion matches primary result; no newly printed numerical outcome. |

## Cross-location reconciliation observations

1. Abstract, Figure 1, PDF p. 4 Results, Table 1, Table 2, Figure 2, Figure 3, and discussion have been mapped. Repeated primary mortality, arm allocation, age, female count, exposure, and adjusted RD records agree at their stated precision and analysis population.
2. Table 1 denominators are often lower than primary-analysis denominators because its footnote identifies variables available only with linkage consent; Figure 3 ethnicity uses a still smaller outcome-available subset. These denominator changes are labeled in-source and are not independently treated as discrepancies here.
3. Table 2 printed component/outcome denominators differ across outcome-specific data availability; its footnote specifies imputation/censoring rules but does not supply all missingness breakdowns. This is retained for later source-grounded review, not inferred as a candidate.

## Candidate observations for independent checking (no judgment)

### O-001 — Possible unit carryover in arterial-oxygenation sentence

- **Exact source location:** DOC-001 PDF p. 6 (printed p. 403), Oxygen Exposure paragraph.
- **Printed text:** “Arterial oxygenation was lower in the conservative oxygen therapy group with a mean (SD) of the median SpO2 of 93.3% (2.8%) and the median PaO2 of 71.5 (13.9) mm Hg compared with 95.1% (2.4%) mm Hg and 79.5 (17.9) mm Hg, respectively, for the usual oxygen therapy group.”
- **Comparator/rule:** The sentence maps two paired measures by “respectively”: SpO2 is expressed as percent and PaO2 as mm Hg. The usual-group first paired value is printed `95.1% (2.4%) mm Hg`, placing both `%` and `mm Hg` after the SpO2 value, whereas the parallel conservative value is `93.3% (2.8%)` without `mm Hg`.
- **Direct observation versus inference:** Directly observed is the printed unit string. A possible copy-edit/unit carryover is an inference only. Confirm against the PDF visually and, if relevant, the supporting oxygen-exposure table before any candidate registration.

## Mapping limitation

The main article refers to eMethods/eTables/eFigures and supplements for supporting definitions and detailed outcomes. Those are separate direct sources/scopes and were not used to resolve or expand DOC-001 relationships in this assigned mapping.
