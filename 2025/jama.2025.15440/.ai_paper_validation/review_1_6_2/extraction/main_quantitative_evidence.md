# Main-paper quantitative evidence map

## Scope, source, method and coverage

Fresh scientific reconstruction of DOC-001, REPORT, all nine physical pages of `jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf`. Printed journal pages 1349–1357 correspond to PDF pages 1–9. This map transcribes evidence and defines relationships for checking; it does not diagnose or classify findings. No old candidate, checker, screening, recheck, audit or final report was read.

Sources consulted: complete reusable native text `document_outputs/doc_001_main_article/normalized_text/page_001.txt` through `page_008.txt`; reusable native page 9 `review_1_5_1/preprocessing/doc001_page_009_native.txt`; retained source-page images `document_outputs/doc_001_main_article/page_images/page_004.png` through `page_007.png`, visually consulted for every flow, table and figure. Paths here are relative to `.ai_paper_validation/`. Native/render engine is legacy PyMuPDF, version not retained; page 9 native engine not retained. All source values remain printed readings. No new extraction, rendering or OCR was needed. All direct-source units have usable reusable evidence; no fresh-required units exist in this main scope.

| PDF page | Printed page | Complete mapped content | Status |
|---|---:|---|---|
| [1](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=1) | 1349 | Abstract, design/population/intervention, primary and exploratory results | COMPLETE |
| [2](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=2) | 1350 | Key Points; eligibility, randomization and intervention; contextual numerical claims | COMPLETE |
| [3](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=3) | 1351 | Outcome hierarchy, sample size/power, all statistical methods, censoring/missing follow-up and multiplicity | COMPLETE |
| [4](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=4) | 1352 | Figure 1 exhaustive participant flow; follow-up and population narrative; primary AF results | COMPLETE |
| [5](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=5) | 1353 | Complete baseline table and footnote; every narrative AF, patch, oral anticoagulation, death and stroke result | COMPLETE |
| [6](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=6) | 1354 | All Figure 2 rows/tests and Figure 3 values/at-risk counts/caption; matching discussion | COMPLETE |
| [7](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=7) | 1355 | All Figure 4A values/at-risk counts and Figure 4B outcome rows; complete caption; matching discussion | COMPLETE |
| [8](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=8) | 1356 | Limitations/conclusions matching primary and exploratory claims; article information; references 1–9 | COMPLETE |
| [9](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=9) | 1357 | References 10–27 inspected: bibliographic numbers only; no additional applicable trial quantitative results | COMPLETE_NO_ADDITIONAL_APPLICABLE_RESULTS |

## Common analysis definitions

Patch means intervention; usual care means control. Randomized allocation is individual, 1:1, parallel-group, unblinded. Each arm includes 2520 participants, total 5040. Eligibility is age ≥65 years, CHA2DS2VASc ≥3 for men or ≥4 for women, without previous AF or atrial flutter. Minimization balances age, sex and residual CHA2DS2VASc score. The active intervention is a single self-applied 14-day continuous single-lead ECG patch sent and returned by post. General practitioners managed clinically actionable patch findings at their discretion; trial supplied no treatment management instructions beyond guideline references. Access to tabulated outcomes by allocation was unavailable to investigators/statisticians/GPs before finalizing SAP and main analyses (p. 2).

Primary outcome: presence of AF in primary care records between randomization and 2.5 years, ITT. Secondary outcome assessments: comparisons of primary outcome separately by age (<80/≥80) and sex. Sensitivities: same primary/secondary comparisons using AF in either primary or secondary care records. Exploratory: time to AF, time with known AF, oral anticoagulation exposure to 2.5 years; long-term randomized stroke and all-cause/cardiovascular death comparisons (p. 3). Distinguish proportion-based analysis from censored time-to-event rate ratio and Kaplan–Meier display.

For proportion comparisons, participants with no AF record before death, withdrawal or primary care loss to follow-up before 2.5 years are grouped with no AF. For time-to-first primary care AF, censor at earliest death, withdrawal, primary care loss to follow-up or 2.5 years. Oral anticoagulation, stroke and death log-rank outcomes do not censor at primary care loss to follow-up. For oral anticoagulation dispensing, exact dates unavailable; only calendar month/year, so elapsed time is months; dispensing in month of randomization counts toward baseline, not postrandomization (p. 3).

## Numeric relationships

Each row records an entire local arithmetic/matching relationship. Percentages are printed percentages, with denominator stated or supplied by the local display. Both arms are ordered patch / usual care throughout. N identifiers are disjoint from the support map. Inferential outputs are mapped under S IDs below, with links back to numeric inputs.

| ID | Exact DOC-001 location | Printed quantities, population and matching claims |
|---|---|---|
| N001 | p. 1 abstract Design; p. 2 Study Design; p. 3 Results opening | Recruitment 27 UK primary care practices; May 2, 2019–February 28, 2022 in abstract, May 2019–February 2022 in Results; last follow-up August 29, 2024; statistical analysis May–July 2025. Administrative locators, no recruitment denominator inferred. |
| N002 | p. 1 abstract Intervention/Results; p. 2 Randomization/Key Points; pp. 3–4 Results; p. 4 Figure 1 | 5040 randomized, 2520 patch and 2520 usual care; 1:1 allocation; 22 044 invited; 5040 (22.9%) of invited randomized. Key Points total 5040. |
| N003 | p. 1 abstract Results; p. 4 Results baseline paragraph | Mean (SD) age 78 (6) years; female 47% in abstract and 2360 (47%) in body; median (IQR) CHA2DS2VASc 4 (3–5). Main table sex rows N017/N018 and score distribution N028–N031. |
| N004 | p. 4 Figure 1 upper box/footnote | 368 000 individuals assessed for eligibility; footnote explicitly states this total is estimated. |
| N005 | p. 4 Figure 1 invitation/reply branches | 22 044 invited; 1186 excluded because GP practice participated in another trial; 20 858 included; 5116 replies received; 76 excluded = 72 negative replies + 4 positive but incomplete consent and no response; 5040 randomized. Branch relationships are explicitly hierarchical. |
| N006 | p. 4 Figure 1 patch branch; pp. 1,4 Results | 2520 allocated patch; 394 no patch ECG data = 206 not returned + 188 returned unworn; 2126 patch ECG data. Narrative/abstract: 2126 (84.4%) wore and returned patch. |
| N007 | p. 4 Figure 1 patch follow-up box | 112 incomplete primary care follow-up at 2.5 y = 106 moved to nonparticipating GP + 6 withdrew consent; 2408 complete = 2310 alive + 98 died; 2520 ITT. Dashed arrow connects no patch data to follow-up, so follow-up is not restricted to patch users. |
| N008 | p. 4 Figure 1 usual-care follow-up box | 110 incomplete primary care follow-up at 2.5 y = 103 moved to nonparticipating GP + 7 withdrew consent; 2410 complete = 2292 alive + 118 died; 2520 ITT. |
| N009 | p. 4 Results follow-up paragraph | Complete primary care follow-up patch 2408 (95.6%), usual care 2410 (95.6%); denominators 2520/2520. Matches N007/N008 count definitions. |
| N010 | p. 4 Results follow-up paragraph | Complete secondary care data patch 2514 (99.8%), usual care 2512 (99.7%); denominators 2520/2520. Separate ascertainment source from primary care follow-up. |
| N011 | p. 4 baseline paragraph | Hypertension 4528 (90%) overall; prior stroke/TIA 963 (19%) overall; CHA2DS2VASc <3: 68 (1.3%); anticoagulant prior to randomization 7%; history prior thromboembolism 12%. Overall denominator 5040. Table links N028,N032,N034,N036,N048. |
| N012 | p. 4 adherence paragraph | Patch-user population 2126; median (IQR) analyzable ECG duration 14 (13–14) days; eTable 1 referenced. Higher adherence in lower CHA2DS2VASc and no heart failure; eTable 2 referenced; no numeric adherence contrast printed here. |
| N013 | p. 5 Table heading | Baseline characteristics at randomization; counts (%) within patch n=2520 / usual care n=2520; no baseline comparison P values printed. Diagnoses and medication rows are not declared mutually exclusive. |
| N014 | p. 5 Table, Age <75 y | 683 (27.1) / 683 (27.1). |
| N015 | p. 5 Table, Age ≥75 to <80 y | 1032 (41.0) / 1061 (42.1). |
| N016 | p. 5 Table, Age ≥80 y | 805 (31.9) / 776 (30.8). Age categories exhaust displayed randomized groups; <80 subgroup counts Figure 2 derive from first two categories. |
| N017 | p. 5 Table, Male | 1340 (53.2) / 1340 (53.2). |
| N018 | p. 5 Table, Female | 1180 (46.8) / 1180 (46.8); matching aggregate N003. |
| N019 | p. 5 Table, Race/ethnicity Asian | 27 (1.1) / 29 (1.2). |
| N020 | p. 5 Table, Black | 2 (0.1) / 9 (0.4). |
| N021 | p. 5 Table, White | 2045 (81.2) / 2056 (81.6). |
| N022 | p. 5 Table, Other; footnote a | 21 (0.8) / 22 (0.9). Combined footnote: multiracial n=22 and secondary-care “any other ethnicity” code S n=21. |
| N023 | p. 5 Table, Race/ethnicity Missing; p. 2 Participants | 425 (16.9) / 404 (16.0). Categories N019–N023 partition table groups. Most frequently recorded primary care category chosen from pre-/up-to-2.5-year records; secondary care substituted when no informative primary care category. |
| N024 | p. 5 Table, BMI <25 | 488 (19.4) / 516 (20.5). BMI defined as kg/m². |
| N025 | p. 5 Table, BMI 25 to <30 | 751 (29.8) / 788 (31.3). |
| N026 | p. 5 Table, BMI ≥30 | 571 (22.7) / 572 (22.7). |
| N027 | p. 5 Table, BMI Missing | 710 (28.2) / 644 (25.6). BMI categories N024–N027 partition groups. |
| N028 | p. 5 Table, CHA2DS2VASc <3; p. 4 baseline paragraph | 33 (1.3) / 35 (1.4); overall 68 (1.3%). Body suggests changes to primary care coding after eligibility check. |
| N029 | p. 5 Table, CHA2DS2VASc 3 | 685 (27.2) / 674 (26.7). |
| N030 | p. 5 Table, CHA2DS2VASc 4 | 983 (39.0) / 976 (38.7). |
| N031 | p. 5 Table, CHA2DS2VASc ≥5 | 819 (32.5) / 835 (33.1); categories N028–N031 partition groups. Score acronym defined by congestive heart failure, hypertension, age, diabetes, prior stroke/TIA, vascular disease, sex category. |
| N032 | p. 5 Table, prior hypertension | 2255 (89.5) / 2273 (90.2); aggregate N011. |
| N033 | p. 5 Table, prior diabetes | 713 (28.3) / 719 (28.5). |
| N034 | p. 5 Table, prior stroke/TIA | 485 (19.2) / 478 (19.0); aggregate N011. |
| N035 | p. 5 Table, chronic kidney disease stage ≥3 | 438 (17.4) / 463 (18.4). |
| N036 | p. 5 Table, prior thromboembolism | 271 (10.8) / 319 (12.7); aggregate N011. |
| N037 | p. 5 Table, prior myocardial infarction | 269 (10.7) / 255 (10.1). |
| N038 | p. 5 Table, prior heart failure | 244 (9.7) / 259 (10.3). |
| N039 | p. 5 Table, prior peripheral artery disease | 214 (8.5) / 206 (8.2). |
| N040 | p. 5 Table, prior statin | 1739 (69.0) / 1737 (68.9). |
| N041 | p. 5 Table, prior RAAS inhibitor | 1599 (63.5) / 1545 (61.3); RAAS=renin-angiotensin-aldosterone system. |
| N042 | p. 5 Table, prior PPI or H2 antagonist | 1265 (50.2) / 1276 (50.6); PPI=proton pump inhibitor. |
| N043 | p. 5 Table, prior calcium channel blocker | 1200 (47.6) / 1289 (51.2). |
| N044 | p. 5 Table, prior diuretic | 713 (28.3) / 709 (28.1). |
| N045 | p. 5 Table, prior aspirin or dipyridamole | 705 (28.0) / 674 (26.7). |
| N046 | p. 5 Table, prior β-blocker | 619 (24.6) / 586 (23.3). |
| N047 | p. 5 Table, prior P2Y12 inhibitor | 363 (14.4) / 320 (12.7). |
| N048 | p. 5 Table, prior oral anticoagulant | 174 (6.9) / 168 (6.7); narrative N011 rounds overall prevalence to 7%. |
| N049 | p. 5 Table, prior direct oral anticoagulant | 128 (5.1) / 148 (5.9). |
| N050 | p. 5 Table, prior vitamin K antagonist | 59 (2.3) / 32 (1.3). Table does not state that medication subcategories are mutually exclusive. |
| N051 | p. 5 Table, prior insulin | 117 (4.6) / 113 (4.5). |
| N052 | pp. 1,2,4,6 primary AF outcomes | 172/2520 (6.8% abstract/Key Points; 6.83% body/Figure 2) vs 136/2520 (5.4% abstract/Key Points; 5.40% body/Figure 2), at 2.5 years, primary care. Key Points says statistically significant difference; S003/S004 give tests/intervals. |
| N053 | p. 6 Figure 2 age <80 | AF 94/1715 (5.48) / 74/1744 (4.24), matching baseline age N014+N015 for denominators. |
| N054 | p. 6 Figure 2 age ≥80 | AF 78/805 (9.69) / 62/776 (7.99); denominators N016; age subgroup numerator and denominator sums connect to N052. |
| N055 | p. 6 Figure 2 Female | AF 76/1180 (6.44) / 46/1180 (3.90); denominators N018. |
| N056 | p. 6 Figure 2 Male | AF 96/1340 (7.16) / 90/1340 (6.72); denominators N017; sex subgroup numerator and denominator sums connect to N052. |
| N057 | p. 5 first Results paragraph | Among participants with postrandomization primary care AF: median (IQR) diagnosis day 103 (43–539) patch / 530 (276–688) usual care. Conditioning is on AF diagnosis, not all randomized. |
| N058 | p. 5 first Results paragraph; p. 6 Figure 3 | Control observed 5.6% vs predicted 1.75% at 2.5 years; body describes higher-than-expected clinical diagnosis. Figure 3 is Kaplan–Meier time-to-first AF, not primary 136/2520 proportion. |
| N059 | p. 6 Figure 3 risk table | Time since randomization years 0,0.5,1.0,1.5,2.0,2.5; patch at risk 2520,2403,2338,2283,2219,2150; usual care 2520,2473,2416,2338,2253,2175. At-risk values are start of six-month period; outcome censoring as p. 3. |
| N060 | p. 6 Figure 3 axes/curves/caption | Y: participants with primary care record of AF (%), ticks 0,2,4,6,8,10; X: years, ticks 0–2.5 by 0.5. Observed solid patch orange/usual care blue; original estimates dotted. Patch curve stays above usual care; predicted curves refer to protocol section 8 assumptions. No exact coordinate values printed beyond axes and S011. |
| N061 | p. 5 patch findings; p. 1 abstract | Patch AF n=89; 3.53% of 2520 randomized to patch; 4.19% of 2126 wore/returned patch (abstract 4.2%); denominator distinctions explicit. |
| N062 | p. 5 patch findings; eTable 3/eFigure 4 pointers | Further 13 atrial flutter; combined AF and/or flutter display n=102. Full patch findings referenced eTable 3; combined patch findings referenced eFigure 4. |
| N063 | p. 5 patch findings; eFigure 2A pointer | First monitoring day detected AF in 51/89 (57%). |
| N064 | p. 5 patch findings; pp. 1,7,8 matching statements | Patch AF burden 100% in 29/89 (33%); burden <10% in 49/89 (55%). Abstract says 55% <10%; discussion/conclusion says more than half below 10%, distribution bimodal. |
| N065 | p. 5 longest AF episode; eFigure 2C/D pointer | ≥24 h 37 (42%); 6–24 h 18 (20%); 6 min–6 h 26 (29%); 30 sec–6 min 8 (9%); patch AF n=89. Wording “between” preserves printed category wording, no endpoint convention added. |
| N066 | p. 5 patch diagnosis follow-up; eFigure 3 pointer | 83/89 (93%) patch AF have postrandomization primary care AF record; 78 within 3 months GP informed. Median reporting time 14 days (95% CI 9–26); interval mapped S014. |
| N067 | p. 5 patch findings | Complete, high-grade or Mobitz type II atrioventricular block in 23 individuals; denominator not printed in sentence; context is intervention patch monitoring. Maximum/minimum AF heart rate distributions are referenced to eFigure 2E/F without numeric main-paper summaries. |
| N068 | p. 5 oral anticoagulation | Oral anticoagulation prescribed up to 2.5 years to 364/2520 (14.4%) patch vs 322/2520 (12.8%) usual care; proportion-based relative risk S015; time-to-event S016. Distinct from baseline N048. |
| N069 | p. 7 Figure 4A risk table | Time since randomization months 0,6,12,18,24,30; patch at risk 2520,2321,2236,2200,2138,2057; usual care 2520,2389,2313,2235,2165,2081. At-risk values at six-month period starts. |
| N070 | p. 7 Figure 4A axes/curves/caption | Y participants with oral anticoagulation record (%), ticks 0,5,10,15,20; X months 0,6,12,18,24,30. Orange patch curve above blue usual care curve. Kaplan–Meier time to first oral anticoagulation; dispensing month handling p. 3; exact graph coordinate values unprinted. |
| N071 | pp. 5,7 Figure 4B Any death | Patch 103 (4.1%) / usual care 126 (5.0%), denominators 2520 each; events between randomization and 2.5 years in secondary care record. Distinguish from primary-care complete-follow-up deceased N007/N008. |
| N072 | p. 7 Figure 4B Cardiovascular death | Patch 32 (1.3%) / usual care 43 (1.7%), denominators 2520 each. |
| N073 | p. 7 Figure 4B Noncardiovascular death | Patch 71 (2.8%) / usual care 83 (3.3%), denominators 2520 each. Cardiovascular + noncardiovascular death counts match all-cause branch N071. |
| N074 | pp. 1,5,7 Figure 4B Any stroke | Patch 69 (2.7%) / usual care 64 (2.5%), denominators 2520 each; p. 1 interval S023; pp. 5,7 interval S024. Records from secondary care and primary care (stroke only) per caption. |
| N075 | p. 7 Figure 4B Presumed ischemic stroke | Patch 60 (2.4%) / usual care 58 (2.3%), denominators 2520 each. Caption includes unspecified stroke types assuming majority ischemic. |
| N076 | p. 7 Figure 4B Hemorrhagic stroke | Patch 12 (0.5%) / usual care 6 (0.2%), denominators 2520 each. Caption calls displayed values number of events (%); body N074 calls any-stroke participants. Figure does not explicitly declare stroke categories mutually exclusive per participant. |
| N077 | p. 7 Figure 4B axis/labels/caption | Rate ratio (95% CI) axis ticks 0.2,1,2; left of 1 favors patch, right favors usual care. All-death/any-stroke diamonds; component outcomes squares sized by statistical information; intervals not multiplicity-adjusted. |
| N078 | p. 2 introduction | Contextual, supplied-text claims: presumed cardioembolic AF strokes up to one-third of ischemic strokes; anticoagulation in high-risk AF reduces stroke risk approximately two-thirds and all-cause mortality one-quarter. Not AMALFI outcome inputs. |
| N079 | p. 7 discussion | Contextual external-study summary contained in supplied text: two recent trials; approximate 35% relative stroke/systemic embolism reduction, 30%–35% relative major bleeding increase; stroke 0.9%–1.2% per person per year. Not AMALFI results; no external sources followed. |
| N080 | pp. 6–8 discussion, limitations and conclusion | AMALFI met primary endpoint; remote 14-day screening gives modest long-term AF diagnosis and anticoagulation exposure increases; control/patch-unrelated diagnosis higher than predicted, groups closer than expected; exploratory strokes show no trends within 2.5 years, trial not powered for clinical outcomes. Conclusions: limited possible stroke impact at 2.5 years and >half AF burden <10%. Matching S003/S011/S017/S024 and N064. No further numerical trial result on p. 8. |

## Statistical and planned-design relationships

All intervals below are 95% confidence intervals unless a row gives an explicit alternative. Patch is numerator/reference contrast relative to usual care; absolute differences are patch minus usual care. Printed formula and analysis statements are preserved without filling in unreported implementation details. No standard errors, log-rank O−E values, V values, person-time totals or model covariates are printed for these displays.

| ID | Exact DOC-001 location | Statistical relationship, printed inputs/output and matching locations |
|---|---|---|
| S001 | p. 3 Statistical Analysis sample size paragraph | Initially 2500 increased to 5000 before unblinded data; predicted 2.5-year AF 4.4% patch vs 1.75% usual care, ratio 2.5; >90% power at two-sided P<.01 for 5000 and same level for smaller 2-fold rather than 2.5-fold difference; approximately 90% power at two-sided P<.05 for age <80/≥80 and separately sex subgroups. Subgroup size proportions not given in paragraph; actual table ages N014–N016 are not stated power assumptions. |
| S002 | p. 3 Statistical Analysis χ² paragraph; p. 3 Outcomes | ITT χ² compares primary proportion; same method within age and sex, χ² heterogeneity between two subgroups. Analogous methods for primary/secondary sensitivity with primary-or-secondary AF, and proportion with oral anticoagulation record. No covariate adjustment described. Primary population/censor handling follows Common analysis definitions. |
| S003 | p. 1 abstract; p. 2 Key Points; p. 4 primary result | Primary AF 172/2520 vs 136/2520; ratio of proportions 1.26 (1.02–1.57), P=.03. Primary statistically significant at two-sided .05 (S027), explicit Key Points significance claim. Abstract says consistent prespecified subgroups. |
| S004 | p. 4 primary result; p. 6 Figure 2 Overall | Patch proportion 6.83% (5.84%–7.81%); usual care 5.40% (4.51%–6.28%); overall absolute difference 1.43 percentage points (0.11–2.75); ratio 1.26 (1.02–1.57), P=.03. Denominators N052. |
| S005 | p. 6 Figure 2 age <80 | N053 inputs; absolute difference 1.24 percentage points (−0.20 to 2.67); ratio of proportions 1.29 (0.96–1.74); subgroup comparison P not printed individually. |
| S006 | p. 6 Figure 2 age ≥80 | N054 inputs; absolute difference 1.70 percentage points (−1.10 to 4.50); ratio 1.21 (0.88–1.67); subgroup comparison P not printed individually. |
| S007 | p. 6 Figure 2 Female | N055 inputs; absolute difference 2.54 percentage points (0.76–4.33); ratio 1.65 (1.16–2.36); subgroup comparison P not printed individually. |
| S008 | p. 6 Figure 2 Male | N056 inputs; absolute difference 0.45 percentage points (−1.48 to 2.37); ratio 1.07 (0.81–1.41); subgroup comparison P not printed individually. |
| S009 | p. 6 Figure 2 right-hand P column; p. 4 primary narrative | Age heterogeneity P=.78; sex heterogeneity P=.06. Visual alignment confirmed from retained p. 6 image, unlike native reading order. Narrative says no significant evidence of heterogeneity. Figure intervals are not adjusted for multiplicity, square area proportional to information, overall diamond; dashed line overall ratio. |
| S010 | p. 3 log-rank method paragraphs | Time-to-first AF log-rank ITT, censorship as Common analysis definitions; RR obtained from observed−expected events and variance, printed expression `exp(O − E ÷ V)`. Text calls O−E one quantity and V its variance; no numerical O−E/V inputs printed. Same method for urgent patch report to first primary care AF. Oral anticoagulation/stroke/death similarly log-rank but no primary care loss censorship. No survival-model covariate list printed. |
| S011 | p. 5 first result paragraph; p. 6 Figure 3 inset | AF time-to-event rate ratio 1.29 (1.03–1.61); log-rank P=.03; more frequent and earlier detection patch vs usual care. Risk counts N059, graph definitions N060, and conditional medians N057. This estimate is separate from primary ratio of proportions S003/S004. |
| S012 | p. 3 permutation/time-with-AF paragraph | Permutation compares mean days with AF across all randomized; time from first postrandomization primary care AF to 2.5 years/death/withdrawal (earliest); undiagnosed contribute zero. Lost-primary-care participants assumed same future days with AF as average remaining without AF in treatment group at loss time. No replication count or CI algorithm printed. |
| S013 | p. 5 first result paragraph | Mean AF days all randomized: 41 (37–45) patch vs 21 (17–25) usual care; difference 20 days (13–28), P<.001. Permutation test S012. Primary/secondary sensitivity using either care source said similar; points to eFigure 1 without main-paper sensitivity numbers. |
| S014 | p. 5 patch diagnosis follow-up paragraph | Median time to reporting 14 days (9–26), called 95% CI; 83/89 primary care AF records and 78 within three months N066. Urgent patch report to first AF log-rank method p. 3; eFigure 3 pointer. No between-arm estimate or P printed in sentence. |
| S015 | p. 5 oral anticoagulation paragraph | Proportion-based relative risk 1.13 (0.98–1.30), P=.08, counts 364/2520 vs 322/2520 at 2.5 years N068. χ² method S002. |
| S016 | p. 5 oral anticoagulation paragraph; p. 7 Figure 4A inset | Time-to-first oral anticoagulation rate ratio 1.15 (0.99–1.34), log-rank P=.07; months-from-randomization, ITT, risk counts N069. Separate from relative risk S015. |
| S017 | p. 1 abstract; p. 5 oral anticoagulation paragraph; p. 3 permutation statement | Mean anticoagulation exposure at 2.5 years among all randomized: patch 1.63 months (1.50–1.76), usual care 1.14 (1.01–1.26); difference 0.50 months (0.24–0.75), P<.001. Permutation compares total exposure by randomized allocation. Abstract and body same displayed outputs. |
| S018 | p. 7 Figure 4B Cardiovascular death | 32/2520 (1.3%) vs 43/2520 (1.7%); rate ratio 0.74 (0.47–1.17), no P printed. Log-rank time-to-event per pp. 3,7 caption; secondary care outcomes at 2.5 years. |
| S019 | p. 7 Figure 4B Noncardiovascular death | 71/2520 (2.8%) vs 83/2520 (3.3%); rate ratio 0.85 (0.62–1.17), no P printed. |
| S020 | p. 7 Figure 4B Any death; p. 5 count narrative | 103/2520 (4.1%) vs 126/2520 (5.0%); rate ratio 0.82 (0.63–1.06), no P printed. Component numeric links N072/N073. |
| S021 | p. 7 Figure 4B Presumed ischemic stroke | 60/2520 (2.4%) vs 58/2520 (2.3%); rate ratio 1.03 (0.72–1.48), no P printed; unspecified stroke included per caption. |
| S022 | p. 7 Figure 4B Hemorrhagic stroke | 12/2520 (0.5%) vs 6/2520 (0.2%); rate ratio 1.94 (0.77–4.90), no P printed. |
| S023 | p. 1 abstract Stroke | 69/2520 (2.7%) vs 64/2520 (2.5%); rate ratio 1.08 (0.76–1.53), no P printed. Same outcome/count/time wording matched with S024; values kept as printed at this exact location. |
| S024 | p. 5 final Results sentence; p. 7 Figure 4B Any stroke | Same counts N074; body `event RR` 1.08 (0.77–1.51), Figure 4B `rate ratio` 1.08 (0.77–1.51), no P printed; ITT time-to-event stroke up to 2.5 years. Caption describes rates from time-to-event and events in secondary or primary care. |
| S025 | pp. 2–3 outcome/rand/intervention definitions | Primary ITT AF proportion 2.5-year primary care; secondary age/sex primary comparisons; sensitivity both-care; exploratory outcomes named in Common definitions; individual minimization using age, sex, residual CHA2DS2VASc. Prespecified subgroup consistency claim pp. 1,4; analysis protocol and SAP pointers pp. 2,3 require support-source comparison, not inferred plan agreement. |
| S026 | p. 3 missing/censored observations | Proportion analyses treat no AF before death/withdrawal/primary care loss as no record; time-to-AF censors death/withdrawal/loss/2.5 years; time-to-anticoagulation/stroke/death does not censor primary care loss. AF-time imputation at loss as S012. Exact at-risk counts N059/N069 and follow-up data N007–N010 provide matched report inputs. |
| S027 | p. 3 significance/multiplicity paragraph; pp. 6,7 captions | Two-sided P<.05 significant for primary. Secondary, sensitivity and exploratory multiplicity allowed in interpretation without formal P adjustment; reported 95% CIs should not infer definitive treatment effects for these outcomes. Captions repeat 95% CIs not adjusted multiplicity. Sample-size design S001 has separate .01/.05 levels; no interim/stopping/multiplicity correction rule otherwise printed in article. |
| S028 | p. 3 software paragraph | Analyses/plotting SAS 9.4, R 4.5.0, RStudio 2025.05.0 build 496. No package/function-specific interval calculation printed; statistical method definitions retained S002/S010/S012/S017. |

## Exhaustive display and narrative matching index

Abstract primary AF and Key Points are N052/S003; full primary event proportions and intervals are S004; complete Figure 2 is N052–N056 and S004–S009. Abstract baseline/patch adherence/detection/burden map to N003/N006/N061/N064. Abstract anticoagulation map is S017. Abstract stroke map N074/S023 remains separately transcribed from Results/Figure 4B S024. Figure 1 entire tree is N004–N008; every baseline table data row is N014–N051 with denominator N013 and all footnote definitions incorporated. Figure 3 entire printed numerical display is N059/N060/S011. Figure 4A display is N069/N070/S016. Figure 4B entire printed table is N071–N077/S018–S024. Main outcome/analysis claims that support plan comparison are S001/S002/S010/S012/S017/S025–S027.

Qualitative narrative matches are recorded where stated: consistent age/sex results without significant heterogeneity (p. 4, S009); sensitivity analyses similar (p. 5, S013); AF detected earlier and more frequently (pp. 4–5, S011/N057); higher-than-predicted control diagnosis and smaller difference (pp. 5,7, N058); patch burden bimodal and more than half below 10% (pp. 5,7,8, N064); oral anticoagulation exposure increased (pp. 1,6,8, S017); no stroke trend and no clinical-outcome power (p. 8, N080).

## Limits and completion counts

All nine physical source pages are mapped, including the references-only ninth page. There are 80 numeric relationship rows (N001–N080) and 28 inferential/design relationship rows (S001–S028), 108 rows total. These IDs define coverage units rather than an expected finding count. Complete data values are included; no result subset was selected on significance. No scientific coverage gap remains in this assigned main-paper scope. Printed charts do not supply exact coordinates for all steps, and the article does not supply O−E/V, person-time, standard errors, covariance/CI implementation or numerical permutation settings; these absent inputs are limitations of available numerical reproduction, not omitted source units. References are mapped as bibliographic material; external literature was not consulted. Reusable text/images are locators, and any later registered candidate requires direct-source recheck under the contract.
