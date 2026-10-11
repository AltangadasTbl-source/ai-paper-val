# Support quantitative evidence: SAP, result supplement, and availability statement

## Scope and provenance

Exclusive assigned scope: DOC-003 `joi190039supp2_prod.pdf`, PLAN, physical PDF pages 1-10; DOC-004 `joi190039supp3_prod.pdf`, REPORT, physical PDF pages 1-8; DOC-005 `joi190039supp4_prod.pdf`, REPORT, physical PDF page 1. All 19 pages mapped. Source roles follow content. No Office, workbook, CSV, formulas, cached workbook values, or workbook display values occur in this scope. No figure is supplied in these three sources; the SAP prospectively specifies plots. No old conclusions, candidate records, or outside evidence were used. This mapping makes no candidate judgments.

Read the complete scope, review contract, settings, inventories, tooling record and coverage manifest. Canonical reusable assets: `.ai_paper_validation/review_1_5_1/preprocessing/support/DOC-003_pp1-10_layout.txt` (form-feed segment N = physical page N); `.ai_paper_validation/review_1_5_1/preprocessing/support/DOC-004_pp1-3_layout.txt`; `.ai_paper_validation/document_outputs/doc-b45e07a04d82/normalized_pages/page-N.txt` for DOC-004 pages 4-8; `.ai_paper_validation/review_1_5_1/preprocessing/support/DOC-005_p1_layout.txt`. Their direct-source comparisons and Poppler engine provenance are recorded in the curator inventory. All assigned pages are reusable-backed, with zero fresh-required pages. Partial historical OCR/native transcriptions were not substituted for canonical text.

Targeted direct confirmation used `pdftotext -layout -f 7 -l 7 joi190039supp3_prod.pdf -` (Poppler 26.01.0) and `pdftoppm -f 7 -l 7 -singlefile -scale-to 2400 -png joi190039supp3_prod.pdf .ai_paper_validation/review_1_6_1/preprocessing/other_support/DOC-004-p7-direct`. The fresh render uses direct Poppler CPU. Both the reusable full-page image and the fresh source render were inspected. No OCR, fallback helper, Python extraction, or GPU was needed. The source PDF remains final authority for later recheck.

Links in this part are package-relative from `extraction/parts/`; the canonical merged support artifact must adjust paths if links are relocated.

## Page-by-page coverage

| Source | Physical page | Role | Content opened and mapped | Applicable mapping | Status |
|---|---:|---|---|---|---|
| DOC-003 | 1 | PLAN | SAP cover; EudraCT 2011-005603-32; internal K357 | Administrative identity; no applicable result quantity | COMPLETE |
| DOC-003 | 2 | PLAN | Objectives, design, sample target, intervention and initial collection schedule | OP01-OP03 | COMPLETE |
| DOC-003 | 3 | PLAN | Timing, colonoscopy window, sensitivity analysis, data sets | OP04-OP05 | COMPLETE |
| DOC-003 | 4 | PLAN | Analysis-set definitions, inclusion criteria, day-renumbering footnote | OP06-OP09 | COMPLETE |
| DOC-003 | 5 | PLAN | Remaining exclusion criteria | OP09 | COMPLETE |
| DOC-003 | 6 | PLAN | Demographic variables, primary and secondary variables, cutoffs, finding categories | OP10-OP12 | COMPLETE |
| DOC-003 | 7 | PLAN | Auxiliary dates, missingness, disposition, descriptive tests, compliance, primary analysis start | OP13-OP16 | COMPLETE |
| DOC-003 | 8 | PLAN | Primary inferential rules; secondary definitions, ROC and mixed model | OP17-OP20 | COMPLETE |
| DOC-003 | 9 | PLAN | Across-day differences, subgroups, software, changes to plan, references 1-3 | OP21-OP24; bibliography has no additional applicable quantitative relationship | COMPLETE |
| DOC-003 | 10 | PLAN | References 4-10 | No applicable result quantity; citations identify methods already mapped | COMPLETE |
| DOC-004 | 1 | REPORT | Supplement contents and titles | Table attribution, endpoint, dose, timing keys | COMPLETE |
| DOC-004 | 2 | REPORT | eTable 1 inclusion/exclusion criteria first part | OR01 eligibility | COMPLETE |
| DOC-004 | 3 | REPORT | eTable 1 continuation | OR01 eligibility | COMPLETE |
| DOC-004 | 4 | REPORT | eTable 2 and all three footnotes | OR02; all 20 count rows | COMPLETE |
| DOC-004 | 5 | REPORT | eTable 3 and abbreviation footnote | OR03; all 9 result rows | COMPLETE |
| DOC-004 | 6 | REPORT | eTable 4 and abbreviation footnote | OR04; all 9 result rows | COMPLETE |
| DOC-004 | 7 | REPORT | eTable 5 and abbreviation footnote; text/render distinction | OR05; all 9 result rows | COMPLETE |
| DOC-004 | 8 | REPORT | eTable 6, model definition, hypotheses and all values | OR06; all 9 result rows | COMPLETE |
| DOC-005 | 1 | REPORT | Protocol/code/data availability | OR07; no applicable result quantity | COMPLETE |

Coverage counts: 19/19 physical pages; DOC-003 10/10, DOC-004 8/8, DOC-005 1/1. Result tables eTables 2-6 contain 56 fully transcribed rows (20+9+9+9+9). eTable 1 eligibility spans two pages and is mapped completely. The local keys OP01-OP24 and OR01-OR07 identify 31 relationship/definition groups; these are source mapping keys, not scientific finding IDs or canonical N/S inventory IDs. No scientific coverage gap remains.

## PLAN definitions and relationships

Each row provides the exact source page and a semantic matching key for the main-paper mapper/checkers. Main-paper locations and values are not asserted in this disjoint support assignment.

| Local key | Source location | Complete relationship or definition | Matching main-paper key |
|---|---|---|---|
| OP01 | DOC-003 p.2 §1.1 | Evaluate sensitivity, specificity, PPV, NPV, likelihood ratios and AUC of two immunochemical FOBTs for advanced colorectal neoplasms after single ASA dose versus placebo. Secondary objectives: sex-specific performance, multiple-day sampling gain, single-dose safety; optional blood biomarkers. | Objectives; primary/secondary diagnostic endpoints; sex subgroup; safety |
| OP02 | DOC-003 p.2 §1.2 | Randomized, double-blind, placebo-controlled multicenter study; planned 2400 participants aged 40-80 with no recent ASA; screening or diagnostic colonoscopy, excluding history of colorectal cancer. No power, assumed prevalence, effect size, allocation ratio, stopping or interim calculation is stated in these SAP pages. | Sample-size target; trial design; recruitment population |
| OP03 | DOC-003 pp.2-3 §1.2 | Single 300 mg ASA versus placebo. Four kits for each of two tests, eight total: FOBGold Tube Screen quantitative and FD Hb/Hp Complex quick test qualitative. Baseline day 0 or 1 before medication, medication day 1; skip baseline if unable, retain day-1 medication. Subsequent samples from day 3 on three preferably consecutive days 3,4,5; allow postponement or only baseline and day-3 samples; one kit each test per collection point; document actual day. | Intervention dose; FIT types; scheduled and actual sampling days |
| OP04 | DOC-003 p.3 §1.2 | At least four ASA-free days between drug and colonoscopy; maximum study-start-to-colonoscopy interval three months. Sensitivity analyses for colonoscopy delayed more than three months; no colonoscopy = drop-out. Samples precede bowel preparation; independently planned colonoscopy/histology define reference findings, extracted blinded using participant number. | Colonoscopy reference standard; timing; delayed-colonoscopy sensitivity analysis; withdrawals |
| OP05 | DOC-003 p.3 §1.3 | Main analysis data: blood/stool collections, diary, colonoscopy, test results, questionnaire, demography/randomization and auxiliary variables. eCRF: eligibility/compliance, colonoscopy timing, demography/randomization, vital signs, end of study and adverse events. | Analysis data sources; population exclusion information |
| OP06 | DOC-003 p.4 §2.1 | Full analysis set = all recruited subjects complying with protocol inclusion/exclusion criteria; used for demographics and compliance with stool timing. | Full analysis set; analyzed population |
| OP07 | DOC-003 p.4 §2.1 and footnote 1 | Per-protocol set: at least one valid stool sample on exactly expected day; baseline any time before or same day as medication (identified as minor protocol deviation from day -1 or 0), later samples day 2,3,4; eligibility and colonoscopy after sample apply. Footnote renumbers days relative to medication intake day 0: §1.2 days 3,4,5 become days 2,3,4. | Per-protocol definition; day 2; baseline and repeated-sample timing |
| OP08 | DOC-003 p.4 §2.1 | Intention-to-screen set = participants with at least one valid test result from sample before colonoscopy, or timing information unavailable. | Intention-to-screen definition; valid sample eligibility |
| OP09 | DOC-003 pp.4-5 §2.2 | Eligibility complete transcription below; age 40-80; postmenopause at least 12 months or surgical sterilization; drug-free intervals 2 weeks anticoagulants/antiplatelets, 1 week ASA, 3 days NSAIDs; severe kidney disease example GFR <30 ml/min; past MI within 6 months; intended methotrexate ≥15 mg/week excluded. | Inclusion/exclusion; recent aspirin; safety population |
| OP10 | DOC-003 p.6 §3.1 | Sex male/female; consent year and birth year in years; primary colonoscopy indication screening/diagnostic; weight Kg; height cm; smoking current smoker/nonsmoker; variables used for stratification or full-set description. | Baseline descriptors; subgroup variables; measurement units |
| OP11 | DOC-003 p.6 §3.2 | Primary variable: FOBGold sensitivity for advanced neoplasms = colorectal cancer or advanced adenoma. Quantitative outcome ng Hb/ml buffer; categorical positive/negative/invalid; manufacturer 17 µg Hb/g feces and lower 10.2 Hb/g feces thresholds. Source lower-threshold phrase omits µg after 10.2; retain this literal distinction while §5.4 supplies µg. Most advanced finding has eight levels: colorectal cancer, advanced adenoma, sessile serrated polyp ≥1cm, sessile serrated polyp <1cm, non-advanced adenoma, hyperplastic polyp, undefined polyp, none. | Primary endpoint; assay units/cutoffs; advanced-neoplasm definition; histology categories |
| OP12 | DOC-003 p.6 secondary variables | Secondary: qualitative-test sensitivity; quantitative AUC; both tests' specificity, likelihood ratios, PPV, NPV; FITs and colonoscopies after positive FIT needed per advanced neoplasm. Qualitative test result four levels positive, weakly positive, negative, invalid. | Secondary endpoint inventory; qualitative positivity |
| OP13 | DOC-003 p.7 §§3.3,4 | Date differences in days: stool minus medication and colonoscopy minus stool; define PP and intention-to-screen. Initial missingness rule excludes missing test outcomes, missing collection day and invalid results; invalid = missing. Multiple samples same test/day: use first valid in scheduled sequence. | Missing/invalid tests; missing sampling dates; repeated samples |
| OP14 | DOC-003 p.7 §5.1 | CONSORT displays recruited, full-set included, excluded counts/reasons; full-set exclusions consequently exclude from PP. | Participant flow; randomized/analyzed counts |
| OP15 | DOC-003 p.7 §5.2 | Age = consent year minus birth year, grouped in five-year classes; absolute/percentage frequencies overall and each allocation group for demographics, indication, colonoscopy; chi-square or Fisher exact compares groups. | Baseline distributions/tests; age grouping |
| OP16 | DOC-003 p.7 §5.3 | Absolute sample frequencies across actual day, missing/invalid samples, stratified expected day, test and treatment/placebo. | eTable 2; sample disposition |
| OP17 | DOC-003 pp.7-8 §5.4 | Primary sensitivity positive among diseased; quantitative manufacturer cutoff 17 µg Hb/g and qualitative-test corresponding cutoff 10.2 µg Hb/g considered. Null no sensitivity change ASA versus placebo. Initially PP day-2 participants. Adjusted Wald CIs: Agresti-Coull for sensitivity, Agresti-Caffo for between-group difference; significance two-sided P<.05. §7 later changes primary set. No multiplicity correction/margin is stated here. | Primary contrast/test; cutoff hierarchy; CI method; population amendment |
| OP18 | DOC-003 p.8 §5.5 | Qualitative positivity positive OR weakly positive. Specificity negative among healthy; PPV diseased among positive; NPV healthy among negative; likelihood ratio at given result = result proportion diseased divided by result proportion healthy. FITs needed = total FITs / positive diseased subjects; colonoscopies needed = total positive FITs / positive diseased subjects. | Sensitivity/specificity/PPV/NPV definitions; likelihood ratios; screening burden |
| OP19 | DOC-003 p.8 §5.5 | Test null no change in qualitative sensitivity and both tests' specificity/PPV/NPV ASA versus placebo; adjusted Wald Agresti-Coull CIs for values, Agresti-Caffo for differences; two-sided P<.05. Adjusted Wald Agresti-Coull CIs also specified for FIT/colonoscopy numbers needed. Analyses in PP and intention-to-screen sets with day-2 samples. | Secondary inference; eTables 4-5; analysis sets |
| OP20 | DOC-003 p.8 §5.5 | ROC plots positive proportion in healthy versus sensitivity over increasing thresholds; total and partial AUC truncated at specificity .8; significance level .05 via DeLong or bootstrap in pROC. Additional binomial mixed effects logit model: sensitivity/specificity response; intervention, sex, test, collection day explanatory variables; participant random intercept for replicates. | ROC/AUC; partial AUC; repeated-measures model |
| OP21 | DOC-003 pp.8-9 §5.5 | PP sensitivity/specificity at day 0 before medication and days 2,3,4; differences each post-dose day versus day 0; plot across days; evaluate combined multiple-day results; list serious adverse events. | Across-day changes; combined positivity eTable 3; safety |
| OP22 | DOC-003 p.9 §5.6 | Stratify sensitivity/specificity by sex, age <60/≥60, smoking, BMI <25/≥25 Kg/m² with BMI weight/height-in-metres squared; additionally sensitivity by most advanced finding sessile serrated polyp ≥1cm and advanced adenoma. Binomial GLM logit with interaction coefficient significance at .05. | Prespecified subgroups; sex interaction; age/BMI groups |
| OP23 | DOC-003 p.9 §6 | R; PropCIs for sensitivity/specificity CIs; pROC for ROC plot, AUC, significance. | Statistical software/packages |
| OP24 | DOC-003 p.9 §7 Changes to the plan | Primary now intention-to-screen day-2 set. Missing collection day included consistently with that framework. Fisher exact tests independence between missing primary quantitative day-2 outcome and allocation; evaluate missing proportion; missing-value treatment decision based on both evaluations. No numerical decision threshold or final imputation rule is printed in §7. | Primary analysis population amendment; missingness assessment; Fisher exact |

All percentages in result tables measure proportions; group differences are percentage points. For interpreting tables use Se=TP/(TP+FN), Sp=TN/(TN+FP), PPV=TP/(TP+FP), NPV=TN/(TN+FN), as derived from the SAP's explicit definitions. These are reading relationships rather than assertions that every reported interval uses a particular unstated formula. No formula parameters beyond named CI methods are supplied here.

## REPORT table relationships and matching keys

| Key | Source | Population/time/contrast and relationships | Matching main-paper key |
|---|---|---|---|
| OR01 | DOC-004 pp.2-3 eTable 1 | Full eligibility, preserved below; all numeric bounds match the mapped SAP criteria semantically | Methods eligibility; study population |
| OR02 | DOC-004 p.4 eTable 2 | Intervention N=1075; control N=1059. Each quantitative/qualitative test has scheduled ≤0,2,3,4,Any rows; columns returned, valid, missing actual date, actual <0,0,1,2,3,4,>4. Count unit is test results/samples, so Any sums sample rows rather than unique participants. Footnotes define valid and day-2 PP cells. | Participant flow full-set counts; sample timing; intention-to-screen and PP denominators |
| OR03 | DOC-004 p.5 eTable 3 | Advanced neoplasm CRC or advanced adenoma; single 300 mg ASA versus placebo; positive if ≥1 of up to three samples scheduled days 2,3,4. Nine rows All/Men/Women × quantitative10.2/quantitative17.0/qualitative10.2 µg Hb/g. Counts TP,FN,TN,FP; Se,Sp%; ASA-minus-placebo Se/Sp differences and 95% CIs. Population title does not separately name PP or intention-to-screen. | Combined sampling secondary analysis; sex subgroup; cutoff |
| OR04 | DOC-004 p.6 eTable 4 | PP advanced-neoplasm detection on day 2 after 300 mg ASA or placebo; same nine sex/test/cutoff rows and count/estimate/difference fields. | Per-protocol sensitivity analysis; sex subgroup; day-2 counts |
| OR05 | DOC-004 p.7 eTable 5 | PP advanced-neoplasm day-2 PPV/NPV%; same nine sex/test/cutoff rows; ASA/placebo values, differences and 95% CIs. Join to OR04 by sex, test, cutoff, PP day2, dose, endpoint. Text/render detail below. | Predictive value sensitivity analysis; PP day2 |
| OR06 | DOC-004 p.8 eTable 6 | Intention-to-screen day2 site sensitivity analysis; generalized linear mixed model (family and link not explicitly supplied) random-intercept SD and likelihood-ratio P for Se and Sp in nine sex/test/cutoff rows. Null SD=0 vs alternative SD>0; successful outcome agreement between FIT and colonoscopy for advanced neoplasm; single300 mg ASA/placebo. | Study-site clustering sensitivity analysis; diagnostic agreement model |
| OR07 | DOC-005 p.1 | Protocol published open access; code available from Silvia Calderazzo; dataset unavailable. No numerical outcomes or prospective analysis specification. External cited publication not retrieved. | Availability statement only; no applicable quantitative comparison |

### Complete eTable 1 eligibility transcription


The complete supplied DOC-004 pages 1-3 layout follows, preserving the contents labels, all eligibility items and bounds. Corresponding PLAN criteria are at DOC-003 pp.4-5. The result supplement has no additional outcome quantities on its contents/eligibility pages.

```text
                          Supplementary Online Content



Brenner H, Calderazzo S, Seufferlein T, et al. Effect of a single aspirin dose prior to fecal
immunochemical testing on test sensitivity for detecting advanced colorectal neoplasms: a
Randomized Clinical Trial JAMA. doi:10.1001/jama.2019.4755

eTable 1. Full list of inclusion and exclusion criteria

eTable 2. Numbers of valid FIT results according to day of fecal sampling in relation
to day of tablet intake

eTable 3. Sensitivity and specificity for detecting advanced neoplasms (colorectal
cancer or advanced adenoma) after single 300 mg aspirin dose or placebo, based on
at least one positive test result from up to three stool samples scheduled on day 2, 3
and 4 after intake of aspirin or placebo

eTable 4. Sensitivity (Se) and specificity (Sp) for detecting advanced neoplasms
(colorectal cancer or advanced adenoma) at day 2 after single 300 mg aspirin dose
or placebo

eTable 5. Positive predictive value (PPV) and negative predictive value (NPV) in %
for detecting advanced neoplasms

eTable 6. Sensitivity analysis for the effect of study site



This supplementary material has been provided by the authors to give readers additional
information about their work.




                                               1
eTable 1. Full list of inclusion and exclusion criteria


Inclusion criteria
• Age 40 to 80 years (both males and females; premenopausal women must have a
    negative pregnancy test before inclusion into the trial, postmenopausal women are
    defined as women who have not had menstrual bleeding for at least 12 months or have
    been surgically sterilized)
• Planned screening or diagnostic colonoscopy
• Able to speak and understand German sufficiently to be able to give written informed
    consent and comply with the trial requirements

Exclusion criteria
• Factors potentially influencing the primary endpoint
       o Diseases/symptoms
               ▪ Chronic inflammatory bowel disease (e.g. Crohn’s disease, ulcerative
                   colitis)
               ▪ Colonoscopy due to positive fecal occult blood test
               ▪ History of colorectal cancer
               ▪ Angiodysplasia of the colon
               ▪ Anamnestic or observed blood loss per anum
       o Use of any of the following drugs
               ▪ Within 2 weeks before the trial
                        • Anticoagulants (including, but not limited to heparin, vitamin K
                            antagonists [e.g. phenprocoumon, warfarin], direct thrombin
                            inhibitors [e.g. dabigatran], or factor Xa inhibitors [e.g. apixaban,
                            rivaroxaban])
                        • Antiplatelet drugs (e.g. clopidogrel, prasugrel, ticlopidine)
               ▪ Within 1 week before the trial
                        • Acetylsalicylic acid
               ▪ Within 3 days before the trial
                        • NSAIDs including selective COX-2 inhibitors
• Factors potentially affecting the safety
       o Any current clinically relevant signs and symptoms, including
               ▪ Signs and symptoms suggesting acute peptic ulcer disease
               ▪ Known clinically relevant thrombocytopenia
               ▪ Acute infection
               ▪ Volume deficit (dehydration)
               ▪ Any currently present allergy with dermal reactions, pruritus, or urticaria
               ▪ Severe or insufficiently controlled asthma
               ▪ Severe kidney or liver diseases (e.g. GFR < 30 ml/min, liver cirrhosis)
               ▪ Severe, not sufficiently treated heart failure (as judged by the investigator)
               ▪ Severe, poorly controlled arterial hypertension
               ▪ Any other unclear symptoms needing further investigation in the opinion of
                   the investigator
       o Any of the following anamnestic findings
               ▪ History of severe gastrointestinal bleeding



                                                 2
               ▪  Known hemorrhagic diathesis, including, but not limited to,
                  hypoprothrombinemia, severe thrombocytopenia, hemophilia
               ▪ Asthma, except for patients who have used acetylsalicylic acid in the past
                  without negative effects
               ▪ Hypersensitivity against salicylic acid or other ingredients of the trial drugs
               ▪ Previous intolerance to NSAIDs including selective COX-2 inhibitors, or
                  antirheumatic medications
               ▪ Severe gout (e.g. recurrent attacks)
               ▪ Hereditary oxaluria
               ▪ Known glucose-6-phosphate dehydrogenase or glutathione peroxidase
                  deficiency
               ▪ Known epilepsy with generalized seizures
               ▪ Severe cardiac diseases (including, but not limited to, myocardial
                  infarction in the past 6 months)
       o Intention to use any of the following drugs during the trial
               ▪ Anticoagulants
               ▪ Antiplatelet drugs
               ▪ NSAIDs including selective COX-2 inhibitors
               ▪ Methotrexate ≥ 15 mg/week
               ▪ Systemically administered glucocorticoids
               ▪ Selective serotonin reuptake inhibitors (SSRIs)
               ▪ Valproic acid
       o Planned surgery/dental treatment during participation in the trial
•   Other factors
       o Known or suspected relevant alcohol abuse
       o Known or suspected illicit drug abuse
       o Pregnancy
       o Suspected non-compliance with the trial procedures
       o Participation in another clinical trial




                                               3
```

### OR02 — Complete eTable 2, DOC-004 physical page 4

[Direct source](../../../../joi190039supp3_prod.pdf#page=4). Every row is below. Footnote a: scheduled days relative to medication; b: valid test and sample before colonoscopy or timing information unavailable; c: actual-day-2 samples used for PP. Columns of actual day partition each row's valid results together with missing actual day. Returned versus valid quantities are distinct. Scheduled rows identify kit schedules; actual days identify collection timing.

```text
eTable 2. Numbers of valid FIT results according to day of fecal sampling in relation to day of tablet intake

Group                           Fecal sampling, return and testing                   Actual day of fecal sampling in relation to day of tablet intake
                 Test            Scheduled Daya Returned Valid Resultb              Missing    <0        0       1        2c       3        4       >4
                                                        N          N                   N        N        N       N         N       N        N        N

Intervention Quantitative               ≤0             1044           1026            82           152      781        9       1        0        0          1
N=1075                                   2             1045           1030            77             2       11      126     758       48        5          3
                                         3              989           975             77             1        0        9     105      700       65         18
                                         4              955           944             64             1        0        0       7       93      677        102
                                        Any            4033           3975            300          156      792      144     871      841      747        124

                 Qualitative            ≤0             1037           970             78           149      733        8       1        0        0          1
                                         2             1040           974             75             2        9      121     719       42        4          2
                                         3              979           922             71             1        0        9      97      663       65         16
                                         4              955           887             60             1        0        0       7       88      638         93
                                        Any            4011           3753            284          153      742      138     824      793      707        112

Control          Quantitative           ≤0             1016           1000            80           159      753        5       2        0        0          1
N=1059                                   2             1024           1012            78             2        4      136     747       38        4          3
                                         3              987           979             75             1        1        5     114      706       58         19
                                         4              959           947             72             1        0        1       1      104      656        112
                                        Any            3986           3938            305          163      758      147     864      848      718        135

                 Qualitative        ≤0            1026            968              76              149      735        5       2        0        0          1
                                     2            1024            969              72                2        4      126     720       39        3          3
                                     3             979            934              73                1        1        5     108      677       51         18
                                     4             956            905              66                1        0        1       1      103      627        106
                                    Any           3985           3776             287              153      740      137     831      819      681        128
a
  Day refers to scheduled day of stool sampling in relation to day of tablet intake
b
    Test result satisfying all the following conditions: (i) Valid test result; (ii) Sample collected before colonoscopy (or information not available)
c
    Samples used for per-protocol analysis


                                                                              4
```

### OR03 — Complete eTable 3, DOC-004 physical page 5

[Direct source](../../../../joi190039supp3_prod.pdf#page=5). Nine rows; contrast aspirin minus placebo; sensitivity and specificity with 95% CI for differences. TP/FN define disease denominator; TN/FP define nondisease denominator. Sex rows are constituent subgroups; quantitative cutoffs reuse their population while positivity changes. Preserve the printed men's quantitative10.2 sensitivity CI punctuation `[-5.5. 27.8]` in the text rather than silently editing it. No P values are printed in this table.

```text
eTable 3. Sensitivity (Se) and specificity (Sp) for detecting advanced neoplasms (colorectal cancer or advanced adenoma) after single 300 mg
aspirin dose or placebo, based on at least one positive test result from up to three stool samples scheduled on day 2, 3 and 4 after intake of
aspirin or placebo
Sex      Test             Cutoff               Aspirin group                    Placebo group                           Difference
                        [µg Hb/g]   TP    FN     TN FP Se         Sp   TP     FN TN FP Se            Sp Sensitivity [95% CI] Specificity [95% CI]
                                    N     N      N      N    %    %    N      N    N    N     %      %            %                    %

All      Quantitative      10.2      63    50 685 261 55.8 72.4          49    58 774 161 45.8 82.8 10.0          [ -3.3, 22.8 ] -10.4 [ -14.1, -6.6 ]
         Quantitative      17.0      44    69 816 130 38.9 86.3          35    72 852 83 32.7 91.1 6.2            [ -6.4, 18.7 ] -4.9 [ -7.7, -2.0 ]
         Qualitative       10.2      53    58 714 222 47.7 76.3          35    73 779 146 32.4 84.2 15.3          [ 2.3, 27.8 ] -7.9 [ -11.5, -4.3 ]

Men      Quantitative      10.2      46    31 311 148 59.7 67.8          28    30 362 102 48.3 78.0 11.5 [ -5.5. 27.8 ] -10.3 [ -15.9, -4.5 ]
         Quantitative      17.0      34    43 384 75 44.2 83.7           22    36 408 56 37.9 87.9 6.2 [ -10.5, 22.4 ] -4.3 [ -8.8, 0.3 ]
         Qualitative       10.2      41    34 343 111 54.7 75.6          19    40 372 89 32.2 80.7 22.5 [ 5.6, 38.0 ] -5.1 [ -10.5, 0.2 ]

 Women Quantitative        10.2       17 19 374 113 47.2 76.8 21 28 412 59 42.9 87.5 4.4 [ -16.7, 25.1 ] -10.7 [ -15.4, -5.8 ]
         Quantitative      17.0       10 26 432 55 27.8 88.7 13 36 444 27 26.5 94.3 1.2 [ -17.4, 20.4 ] -5.6 [ -9.1, -2.0 ]
         Qualitative       10.2       12 24 371 111 33.3 77.0 16 33 407 57 32.7 87.7 0.7 [ -19.0, 20.7 ] -10.7 [ -15.5, -5.9 ]
Abbreviations: CI, confidence interval; FN, false negatives; FP, false positives; g, gram; Hb, hemoglobin; Se, sensitivity; Sp, specificity; TN, true
negatives; TP, true positives




                                                                          5
```

### OR04 — Complete eTable 4, DOC-004 physical page 6

[Direct source](../../../../joi190039supp3_prod.pdf#page=6). Nine PP day2 rows; contrast aspirin minus placebo; count/estimate/CI columns as OR03. No P values printed. Matching criteria for OR05 are exact sex/test/cutoff/PP/day2/advanced neoplasm; do not join to a different analysis set or combined-day table.

```text
eTable 4. Sensitivity (Se) and specificity (Sp) for detecting advanced neoplasms (colorectal cancer or advanced adenoma) at day 2 after single
300 mg aspirin dose or placebo. Results of the per-protocol analysis.
Sex      Test             Cutoff            Aspirin group                       Placebo group                          Difference
                        [µg Hb/g]   TP    FN TN FP Se            Sp     TP    FN TN FP Se           Sp Sensitivity [95% CI] Specificity [95% CI]
                                    N     N   N      N    %      %      N     N    N    N     %     %            %                    %

All      Quantitative     10.2       42    56 635 136 42.9 82.4         25     61 691     85 29.1 89.0 13.8      [ -0.1, 27.1 ] -6.7   [ -10.1, -3.2 ]
         Quantitative     17.0       29    69 704 67 29.6 91.3          18     68 735     41 20.9 94.7 8.7       [ -4.0, 20.8 ] -3.4   [ -5.9, -0.8 ]
         Qualitative      10.2       30    56 617 119 34.9 83.8         19     65 683     62 22.6 91.7 12.3      [ -1.4, 25.4 ] -7.8   [ -11.2, -4.5 ]

Men      Quantitative     10.2       31    34 310      78 47.7 79.9     11     34 344     58 24.4 85.6 23.2      [ 5.0, 39.5 ] -5.7    [ -10.9, -0.4 ]
         Quantitative     17.0       23    42 350      38 35.4 90.2      9     36 373     29 20.0 92.8 15.4      [ -1.8, 30.9 ] -2.6   [ -6.5, 1.4 ]
         Qualitative      10.2       24    33 311      63 42.1 83.2      9     37 353     40 19.6 89.8 22.5      [ 4.5, 38.6 ] -6.7    [ -11.5, -1.8 ]

 Women Quantitative        10.2      11 22 325 58 33.3 84.9 14 27 347 27 34.1 92.8 -0.8 [ -21.8, 20.6 ] -7.9 [ -12.3, -3.4 ]
         Quantitative      17.0         6 27 354 29 18.2 92.4              9 32 362 12 22.0 96.8 -3.8 [ -21.6, 15.0 ] -4.4 [ -7.6, -1.1 ]
         Qualitative       10.2         6 23 306 56 20.7 84.5 10 28 330 22 26.3 93.8 -5.6 [ -25.1, 15.3 ] -9.2 [ -13.7, -4.6 ]
Abbreviations: CI, confidence interval; FN, false negatives; FP, false positives; g, gram; Hb, hemoglobin; Se, sensitivity; Sp, specificity; TN, true
negatives; TP, true positives




                                                                          6
```

### OR05 — Complete eTable 5, DOC-004 physical page 7

[Direct source](../../../../joi190039supp3_prod.pdf#page=7). Nine PP day2 rows; percentages for PPV/NPV and percentage-point ASA-minus-placebo differences with 95% CIs. No P values printed. The canonical and direct native layout put the women PPV differences across lines: minus sign followed by 18.2 (quantitative10.2), 25.7 (quantitative17.0), 21.6 (qualitative10.2). Thus native text quantities are -18.2, -25.7, -21.6 respectively. The supplied source's fresh Poppler page render and reusable full-page render display only a minus sign inside these three difference cells; the numerical portions are not visually shown. Likewise the header render shows truncated unit `[µg` whereas native extraction includes Hb/g across lines. Record both native-text content and the visible presentation; do not invent a visible value or treat a hidden text quantity as visually confirmed. All group percentages and CI endpoints are visible and match the native extraction. Render derivative: `.ai_paper_validation/review_1_6_1/preprocessing/other_support/DOC-004-p7-direct.png`, Poppler pdftoppm 26.01.0, single page scale-to2400 CPU. This is a source presentation distinction, not an OCR disagreement; no candidate judgment is made.

| Sex | Test | Cutoff µg Hb/g | Aspirin PPV | Aspirin NPV | Placebo PPV | Placebo NPV | Native-text PPV difference | PPV 95% CI | NPV difference | NPV 95% CI |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|
| All | Quantitative | 10.2 | 23.6 | 91.9 | 22.7 | 91.9 | 0.9 | [-9.3,10.7] | 0.0 | [-2.8,2.8] |
| All | Quantitative | 17.0 | 30.2 | 91.1 | 30.5 | 91.5 | -0.3 | [-15.3,14.2] | -0.5 | [-3.3,2.3] |
| All | Qualitative | 10.2 | 20.1 | 91.7 | 23.5 | 91.3 | -3.3 | [-14.8,7.7] | 0.4 | [-2.6,3.3] |
| Men | Quantitative | 10.2 | 28.4 | 90.1 | 15.9 | 91.0 | 12.5 | [-0.2,24.1] | -0.9 | [-5.2,3.4] |
| Men | Quantitative | 17.0 | 37.7 | 89.3 | 23.7 | 91.2 | 14.0 | [-4.9,31.1] | -1.9 | [-6.1,2.2] |
| Men | Qualitative | 10.2 | 27.6 | 90.4 | 18.4 | 90.5 | 9.2 | [-5.9,22.8] | -0.1 | [-4.4,4.2] |
| Women | Quantitative | 10.2 | 15.9 | 93.7 | 34.1 | 92.8 | -18.2; render minus only | [-34.7,-1.3] | 0.9 | [-2.9,4.6] |
| Women | Quantitative | 17.0 | 17.1 | 92.9 | 42.9 | 91.9 | -25.7; render minus only | [-48.4,-0.7] | 1.0 | [-2.7,4.8] |
| Women | Qualitative | 10.2 | 9.7 | 93.0 | 31.2 | 92.2 | -21.6; render minus only | [-38.9,-3.9] | 0.8 | [-3.2,4.8] |

The exact layout aid follows to preserve line positions rather than replacing the source presentation with the normalized table above.

```text
eTable 5. Positive predictive value (PPV) and negative predictive value (NPV) in % for detecting advanced neoplasms (colorectal cancer or
advanced adenoma) at day 2 after single 300 mg aspirin dose or placebo. Results of the per-protocol analysis.

Sex      Test           Cutoff     Aspirin      Placebo        Difference in PPV        Difference in NPV
                         [µg     PPV   NPV     PPV   NPV            [95% CI]                 [95% CI]
                                   group         group
                        Hb/g]
All      Quantitative   10.2     23.6   91.9   22.7   91.9 0.9      [ -9.3, 10.7 ]     0.0        [ -2.8, 2.8 ]
         Quantitative   17.0     30.2   91.1   30.5   91.5 -0.3     [ -15.3, 14.2 ]    -0.5       [ -3.3, 2.3 ]
         Qualitative    10.2     20.1   91.7   23.5   91.3 -3.3     [ -14.8, 7.7 ]     0.4        [ -2.6, 3.3 ]

Men      Quantitative   10.2     28.4   90.1   15.9   91.0 12.5     [ -0.2, 24.1 ]     -0.9       [ -5.2, 3.4 ]
         Quantitative   17.0     37.7   89.3   23.7   91.2 14.0     [ -4.9, 31.1 ]     -1.9       [ -6.1, 2.2 ]
         Qualitative    10.2     27.6   90.4   18.4   90.5 9.2      [ -5.9, 22.8 ]     -0.1       [ -4.4, 4.2 ]

Women Quantitative      10.2     15.9   93.7   34.1   92.8  -       [ -34.7, -1.3 ]     0.9       [ -2.9, 4.6 ]
      Quantitative      17.0     17.1   92.9   42.9   91.9 18.2
                                                            -       [ -48.4, -0.7 ]     1.0       [ -2.7, 4.8 ]
      Qualitative       10.2     9.7    93.0   31.2   92.2 25.7
                                                            -       [ -38.9, -3.9 ]     0.8       [ -3.2, 4.8 ]
                                                           21.6

Abbreviations: CI, confidence interval; FIT, fecal immunochemical test; g, gram; Hb, hemoglobin; NPV, negative predictive value; PPV, positive
predictive value




                                                                        7
```

### OR06 — Complete eTable 6, DOC-004 physical page 8

[Direct source](../../../../joi190039supp3_prod.pdf#page=8). Nine rows, each with sensitivity random-intercept SD/P and specificity random-intercept SD/P. Scientific notation preserved, including zero SDs and P=.50. Model SDs are not proportions or percentage points. Null SD0 versus one-direction SD>0; likelihood-ratio test stated; no further likelihood-mixture computation is supplied by this table. Model investigates study-site random intercept, distinct from SAP's participant repeated-measure random intercept in OP20.

```text
eTable 6. Sensitivity analysis for the effect of study site. Estimated generalized linear mixed model random intercept standard deviations (St. Dev.)
and corresponding p-values from the likelihood ratio test are shown. The null hypothesis of standard deviation equal to zero is tested against the
alternative hypothesis that the standard deviation is greater than zero. Agreement between test and colonoscopy result for the detection of
advanced neoplasms (colorectal cancer or advanced adenoma) at day 2 after single 300 mg aspirin dose or placebo are considered successful
outcomes. Results of the intention-to-screen analysis.
Sex           Test             Cutoff           Sensitivity                Specificity
                             [µg Hb/g]     St. Dev.     p-value       St. Dev.     p-value

All           Quantitative     10.2        0.00E+00           0.50    5.49E-03           0.38
              Quantitative     17.0        1.97E-01           0.16    0.00E+00           0.50
              Qualitative      10.2        0.00E+00           0.50    9.23E-03           0.30

Men           Quantitative     10.2        0.00E+00           0.50    1.00E-14           0.50
              Quantitative     17.0        0.00E+00           0.50    1.47E-02           0.40
              Qualitative      10.2        0.00E+00           0.50    1.13E-02           0.35

Women         Quantitative     10.2        0.00E+00           0.50    1.79E-12           0.50
              Quantitative     17.0        1.67E-01           0.40    0.00E+00           0.50
              Qualitative      10.2        4.35E-16           0.50    0.00E+00           0.50




                                                                          8
```

### OR07 — DOC-005 availability statement, physical page 1

[Direct source](../../../../joi190039supp4_prod.pdf#page=1). Opened fully: trial protocol cited as Tikk et al., ASTER trial, BMC Cancer2018;18(1):914; statistical code available from Silvia Calderazzo; dataset not available. This is retrospective REPORT content and has no prospective statistical rule. Bibliographic numbers are not outcome quantities. The external publication was not retrieved.

## Matching and completeness notes

Use disease definition advanced neoplasms (CRC or advanced adenoma), dose300 mg, quantitative/qualitative assay, cutoff, sex, collection day, combined-day versus single-day rule, and analysis set jointly to match results. eTable2 supplies sample timing/counts; eTable3 supplies combined-sample estimates; eTable4 supplies PP day2 estimates/counts; eTable5 supplies predictive values from that PP day2 setting; eTable6 supplies intention-to-screen site modeling. The main-paper mapper is responsible for main-paper locations; these semantic join keys expose all relevant matches without inspecting unassigned main pages.

No additional results are supplied on administrative cover/reference/availability units. All assigned units were opened; no page was inferred to lack quantitative content from missing reusable extraction. No supplied structured source or workbook exists within this assignment, hence formulas/cached values are not applicable. No inferential statistic, table row, subgroup, unit, or footnote was sampled or omitted. The SAP does not supply a final numerical missingness decision rule, numerical power assumptions, or multiplicity algorithm; these absences are bounded description facts for checker matching, not coverage gaps or candidate diagnoses.

## Complete SAP text locator appendix

For completeness of administrative and procedural units as well as every planned quantitative relationship, the entire source-matched DOC-003 layout aid is reproduced below. Form-feed segments 1-10 correspond exactly to physical PDF pages 1-10. OP01-OP24 above provide semantic matching keys. Additional collection quantity on page2: four optional blood tubes (two EDTA and two serum). All reference entries and identifiers are included as administrative coverage, without treating bibliography numbers as quantitative results.

```text
                 Statistical Analysis Plan


Use of Acetylsalicylic Acid (ASA) for Enhanced
   Early Detection of Colorectal Neoplasms


        EudraCT No.: 2011-005603-32
          Internal study code: K357
           Statistical Analysis Plan




                                                 1
                                     Statistical Analysis Plan

1     Background

1.1    Objectives

This document provides the statistical analysis plan for the study “Use of Acetylsalicylic (ASA)
for Enhanced Early Detection of Colorectal Neoplasms”. The study aims to investigate,
according to the study protocol v1.5, diagnostic performance (sensitivity, specificity, positive
and negative predictive values, likelihood ratios, area under the curve) of 2 immunochemical
Fecal Occult Blood Tests (iFOBTs) for detecting advanced colorectal neoplasms after a single
dose of acetylsalicylic acid as compared to placebo.

Secondary objectives, again according to the study protocol v1.5, comprise studying gender-
specific performance of the 2 iFOBTs and the possible gain in diagnostic performance by stool
sampling on multiple days, as well as studying the safety of single-dose acetylsalicylic acid in
the selected population. An optional additional secondary objective is to collect blood samples
for additional biomarker analyses.


1.2    Trial design

According to the study protocol v1.5:

The planned study is a randomized, double-blind, placebo-controlled, multicenter study.

Overall, 2,400 eligible participants with an age of 40 to 80 years and with no recent use of
acetylsalicylic acid will be recruited into this study when visiting one of the participating
gastroenterology private practices or hospitals (outpatient clinics) for an informative
appointment, which is routinely scheduled a few weeks before colonoscopy. In addition to
participants scheduled for a screening colonoscopy, patients visiting the study centers for a
diagnostic colonoscopy but excluding patients with a history of colorectal cancer (see list of in-
and exclusion criteria for details) will also be asked to participate. Thus, the colonoscopy
procedure is planned and conducted independently from our study.

During this first appointment (day 0), participants will be informed about the study, will receive
the printed study information, will have enough time for consideration and will have the
opportunity to ask questions. After obtaining written informed consent a detailed medical
history and information on the use of medication will be collected and in- and exclusion criteria
will be checked. Women who are not postmenopausal have a negative pregnancy test. If in-
and exclusion criteria are not met the patient will be considered as a “screening failure” (the
reasons will be documented in the patient identification list). If all criteria are met (and the
patient consented to the optional blood sampling) four extra tubes of blood (2 EDTA tubes and
2 serum tubes) will be taken for analysis of additional biomarkers (optional). In addition,
patients will receive four immunological FOBT-kits for each of two different iFOBTs
(FOBGold®Tube Screen, similar test used in our preliminary study (1), as well as the FD Hb/Hp
Complex quick test, an internationally well-established test (2,3) (www.frostdiagnostika.de)),
so eight kits in total, with instructions on when and how to use them, including a device which
is hung in the toilet and aids in easy collection of the stool samples (“Sammelhilfe”).
Participants will be randomized to receive either a single dose of 300 mg acetylsalicylic acid
or placebo (thereby, a unique participant number is generated and documented). Both
participants and their physicians will be blinded with respect to the study medication.
Participants will be asked to collect a baseline stool sample on day 0 or on day 1, before taking
the study medication. The study medication should be taken on day 1. If the participant cannot
collect a stool sample on the first day (e.g. due to severe constipation), this stool sample should
be skipped and the study medication should be taken on day 1 without a baseline stool sample.
Further stool samples are to be collected from day 3 onwards on 3 different, preferably
consecutive days (day 3, 4, and 5). If stool collection on these days is not possible because of
                                                                                                 2
                                       Statistical Analysis Plan

constipation or other reasons, stool collection may be postponed to the subsequent day. It is
allowed for the participant to give also only two stool samples (before taking study medications
and on day 3). At each time point at which stool samples are collected, 1 kit of each test should
be used and the actual day documented. The stool sampling devices ensures collection of
defined volumes of stool which are given to a buffer that hinders degradation of hemoglobin.
All stool samples should be collected at the participants’ homes and prior to initiation of large
bowel preparation for colonoscopy and sent by mail to the coordinating center (Heidelberg)
using special pre-paid and addressed mailing devices. Participants will receive a form
(Participant diary) on which they have to document when they took the study medication, and
the date of stool collection. Finally, participants will be asked to fill out a standardized
questionnaire addressing potential determinants of risk of colorectal neoplasms and of test
performance, including general participant characteristics, comorbidities, and lifestyle factors.
They can either do this during their visit to the study center or at home.

Colonoscopy is planned and conducted independently from our study. However, the
investigator will ensure that there are at least 4 acetylsalicylic acid-free days between taking
the study medication and the colonoscopy. Although a single dose of acetylsalicylic acid is not
considered a contra-indication for elective colonoscopy, this time interval was chosen to
minimize any possibility of an increased risk of bleeding at colonoscopy or endoscopic removal
of small polyps (see paragraph on safety for further details) (4-6). The colonoscopy is
performed in the setting of screening for colorectal cancer or diagnostic workup and as such,
it is not part of the study. However, the findings from screening colonoscopy will be collected
and used in our analysis.

The maximum time between start of the study and colonoscopy is set at 3 months. At the end
of the trial, sensitivity analyses are performed for participants whose colonoscopy is postponed
for more than 3 months for any reason. If the colonoscopy does not take place at all, the
participant will be considered as a drop-out.

Colonoscopy (and histology) reports will be pseudonymized (i.e. any personal data will be
removed and the participant number will be noted) and will be sent from the study center to
the coordinating center in Heidelberg following the end of the study for each participant. The
relationship between blood samples, stool samples, and colonoscopy results will be
established only by the participant number. The information from colonoscopy records will be
extracted in a standardized, blinded manner by trained staff.


1.3       Data-sets

The analysis will be performed on data contained in the following documents

      x    Main analysis data-set will contain information relative to the blood and stool sample
           collection, the participant’s diary, colonoscopy results, iFOBTs results, participant’s
           questionnaire, demographic and randomization information, and auxiliary variables;
      x    eCRF will contain information regarding compliance with inclusion and exclusion
           criteria, timing of the planned colonoscopy, demographic and randomization
           information, vital signs, information regarding the end of the study and about adverse
           events.




                                                                                                3
                                      Statistical Analysis Plan

2     Analysis sets

2.1    Definitions

The full analysis set will comprise all recruited subjects complying with the protocol inclusion
and exclusion criteria (see section 2.2). This set will be used to tabulate demographic
characteristics and compliance to requested timing of stool sample collection.

The per-protocol analysis set will comprise subjects providing at least one stool sample at
exactly the expected day of collection, i.e. the first stool sample any time before, or on the
same day, of medication intake (this represents a minor deviation from the protocol, which
specifies that the first stool sample can be taken at day -1 or 01), later stool samples at either
day 2, 3, or 4. Inclusion and exclusion criteria (see section 2.2), the requirement that the
sample provides a valid test result, and that colonoscopy is performed after the stool sample
is collected, will apply.

The intention-to-screen analysis set will be formed by participants providing at least one stool
sample leading to a valid test result and collected before colonoscopy (or information not
available).


2.2    Full list of inclusion and exclusion criteria

The following exclusion and inclusion criteria will apply, according to study protocol v1.5:

Inclusion criteria
x Age 40 to 80 years (both males and females; premenopausal women must have a negative
    pregnancy test before inclusion into the trial, postmenopausal women are defined as
    women who have not had menstrual bleeding for at least 12 months, or have been
    surgically sterilized)
x Planned screening or diagnostic colonoscopy
x Able to speak and understand German sufficiently to be able to give written informed
    consent and comply with the trial requirements

Exclusion criteria
x Factors potentially influencing the primary endpoint
       o Diseases/symptoms
                Chronic inflammatory bowel disease (e.g. Crohn’s disease, ulcerative
                   colitis)
                Colonoscopy due to positive fecal occult blood test
                History of colorectal cancer
                Angiodysplasia of the colon
                Anamnestic or observed blood loss per anum
       o Use of any of the following drugs
                Within 2 weeks before the trial
                       x Anticoagulants (including, but not limited to heparin, vitamin K
                            antagonists [e.g. phenprocoumon, warfarin], direct thrombin
                            inhibitors [e.g. dabigatran], or factor Xa inhibitors [e.g. apixaban,
                            rivaroxaban])

1 To improve clarity, the numbering of the days is now sequentially defined with respect to study
medication intake, which is assumed to take place at day 0. Consequently day 3, 4, and 5 of section
1.2, will now be referred to as day 2, 3, and 4.
                                                                                                 4
                                    Statistical Analysis Plan

                        x Antiplatelet drugs (e.g. clopidogrel, prasugrel, ticlopidine)
                Within 1 week before the trial
                        x Acetylsalicylic acid
                Within 3 days before the trial
                        x NSAIDs including selective COX-2 inhibitors
x   Factors potentially affecting the safety
       o Any current clinically relevant signs and symptoms, including
                Signs and symptoms suggesting acute peptic ulcer disease
                Known clinically relevant thrombocytopenia
                Acute infection
                Volume deficit (dehydration)
                Any currently present allergy with dermal reactions, pruritus, or urticaria
                Severe or insufficiently controlled asthma
                Severe kidney or liver diseases (e.g. GFR < 30 ml/min, liver cirrhosis)
                Severe, not sufficiently treated heart failure (as judged by the investigator)
                Severe, poorly controlled arterial hypertension
                Any other unclear symptoms needing further investigation in the opinion of
                   the investigator
       o Any of the following anamnestic findings
                History of severe gastrointestinal bleeding
                Known hemorrhagic diathesis, including, but not limited to,
                   hypoprothrombinemia, severe thrombocytopenia, hemophilia
                Asthma, except for patients who have used acetylsalicylic acid in the past
                   without negative effects
                Hypersensitivity against salicylic acid or other ingredients of the trial drugs
                Previous intolerance to NSAIDs including selective COX-2 inhibitors, or
                   antirheumatic medications
                Severe gout (e.g. recurrent attacks)
                Hereditary oxaluria
                Known G6PD or glutathione peroxidase deficiency
                Known epilepsy with generalized seizures
                Severe cardiac diseases (including, but not limited to, myocardial infarction
                   in the past 6 months)
       o Intention to use any of the following drugs during the trial
                Anticoagulants
                Antiplatelet drugs
                NSAIDs including selective COX-2 inhibitors
                Methotrexate ≥ 15 mg/week
                Systemically administered glucocorticoids
                Selective serotonin reuptake inhibitors (SSRIs)
                Valproic acid
       o Planned surgery/dental treatment during participation in the trial
x   Other factors
       o Known or suspected relevant alcohol abuse
       o Known or suspected illicit drug abuse
       o Pregnancy
       o Suspected non-compliance with the trial procedures
       o Participation in another clinical trial

                                                                                              5
                                        Statistical Analysis Plan

3     Analysis variables

3.1       Demography and baseline characteristics

The following demographic variables will be collected and used for stratification purposes or
description of the full analysis set:

      x    Sex Categorical variable with two levels: male or female;
      x    Year of consent Quantitative variable, expressed in years.
      x    Year of birth Quantitative variable, expressed in years.
      x    Primary indication of colonoscopy Categorical variable with two levels: screening or
           diagnostic.
      x    Weight Quantitative variable, expressed in Kg;
      x    Height Quantitative variable, expressed in cm;
      x    Smoking status Categorical variable with two levels: (current) smoker or nonsmoker.


3.2       Primary variables

The primary variable will be represented by the sensitivity of the FOBGold®Tube Screen test
to detect advanced neoplasms (colorectal cancer or advanced adenoma). It will be obtained
from the following observed variables:

      x    Quantitative test outcome of the FOBGold®Tube Screen test Quantitative variable,
           expressed in ng Hb/ml Buffer.

      x    Categorical test outcome of the FOBGold®Tube Screen test Categorical variable
           with three levels: positive, negative or invalid test result. Positivity is defined at the
           manufacturer’s threshold and a lower threshold (17 μg Hb/g feces and 10.2 Hb/g
           feces).

      x    Most advanced finding at colonoscopy Categorical variable with eight levels:
           colorectal cancer, advanced adenoma, sessile serrated polyp greater or equal to 1cm,
           sessile serrated polyp smaller than 1cm, non-advanced adenoma, hyperplastic polyp,
           undefined polyp, no finding.


Secondary variables

The secondary variables will include sensitivity of the FD Hb/Hp Complex quick test, the area
under the ROC curve for the FOBGold®Tube Screen test, as well as the specificities, the
likelihood ratios, and the positive and negative predictive values of both tests, for detection of
advanced neoplasms. Number of iFOBTs and number of colonoscopies after a positive iFOBT
needed to detect one advanced neoplasm will also be evaluated. The following additional
observed variable will be required:

      x    Test outcome of the FD Hb/Hp Complex quick test Categorical variable with four
           levels: positive, weakly positive, negative, or invalid test result.




                                                                                                   6
                                     Statistical Analysis Plan

3.3       Auxiliary variables

Two additional variables will be used to define the per-protocol and intention-to-screen analysis
sets:

      x    Difference between the date of stool sample collection and the date of study
           medication intake Quantitative variable, expressed in days.

      x    Difference between the date of colonoscopy and the date of stool sample
           collection Quantitative variable, expressed in days.


4     Handling of missing values

Missing values in the test outcomes, as well as missing values for the day of stool sample
collection, will be excluded from the analysis. Invalid test results in any of the test outcome
variables will be categorized as missing values and excluded from the analysis. If multiple
samples for a given test are collected on the same day, the first valid sample, i.e. the first in
the sequence of scheduled iFOBTs, will be used.


5     Statistical analyses / methods

5.1       Subject disposition

A CONSORT flowchart will summarize the process of exclusion of recruited subjects which will
not be included in the full analysis set (and consequently the per-protocol analysis set). In
particular, the flowchart will show the number of recruited subjects, the number of subjects
included in the full analysis set, and the number and reason of exclusion for the discarded
subjects.


5.2       Demography and baseline characteristics

The trial population will be described according to demographic characteristics (age, sex),
primary indication of colonoscopy and colonoscopy outcomes. Age will be obtained as the
difference between year of consent and year of birth, and categorized into 5-year classes.
Absolute and percent frequencies for the total population, as well as separately for the control
and intervention group population, will be provided.
Differences between the control and intervention group will be tested via a chi-square or
Fisher’s exact test.


5.3       Exposition to treatment/Compliance

Absolute frequencies displaying the distribution of test samples across days of stool sample
collection, as well as of missing and invalid samples will be tabulated. The frequencies will be
further stratified by expected day of stool sample collection, test, and intervention group
(treatment or placebo).


5.4       Primary analysis

The primary analysis will focus on the sensitivity of the FOBGold®Tube Screen test for the
detection of advanced neoplasms.

                                                                                               7
                                     Statistical Analysis Plan

Sensitivity is defined as the proportion of subjects obtaining a positive test result among the
diseased subjects.
Manufacturer’s threshold (17 μg Hb/g feces) as well as FD Hb/Hp Complex quick test threshold
for positivity (10.2 μg Hb/g feces) will be considered.
The analysis will test the null hypothesis of no change in sensitivity after the intake of a single
dose of acetylsalicylic acid, as compared to placebo. It will be performed on participants in the
per-protocol analysis set providing samples at day 2.
Wald adjusted confidence intervals will be computed for sensitivity values (Agresti-Coull
adjustment) (7) and the differences between placebo and intervention group (Agresti-Caffo
adjustment) (8). Statistical significance will be defined by a two-sided p-value <0.05.


5.5   Secondary analyses

The secondary analyses will evaluate the sensitivity of the FD Hb/Hp Complex quick test, the
area under the ROC curve for the FOBGold®Tube Screen test, as well as the specificities, the
likelihood ratios, the positive and negative predictive values for the detection of advanced
neoplasms for both tests, and number of iFOBTs and number of colonoscopies after a positive
iFOBT needed to detect one advanced neoplasm.
Positivity of the FD Hb/Hp Complex quick test will be defined by either a positive or weakly
positive test result.
Specificity is defined as the proportion of subjects obtaining a negative test result among the
healthy subjects. Positive predictive value is defined as the proportion of diseased subjects
among the subjects obtaining a positive test result, while negative predictive value is defined
as the proportion of healthy subjects among the subjects obtaining a negative test result.
Likelihood ratio for a given test result is defined as the ratio between the proportion of subjects
obtaining the given test result among the diseased subjects, and among the healthy subjects.
The ROC curve is obtained by plotting the proportion of subjects obtaining a positive test result
among the healthy subjects against sensitivity, for increasing thresholds of test positivity.
Number of iFOBTs and number of colonoscopies after a positive iFOBT needed to detect one
advanced neoplasm for a given test are defined as the ratio between the total number of
performed iFOBTs and the number of subjects obtaining a positive test result among the
diseased subjects, and the ratio between the total number of positive iFOBTs (thus leading to
colonoscopy) and the number of subjects obtaining a positive test result among the diseased
subjects, respectively.
The null hypothesis of no change in sensitivity of the FD Hb/Hp Complex quick test, as well as
specificities, positive or negative predictive values after the intake of single dose of
acetylsalicylic acid of both tests, as compared to placebo, will be tested. Wald adjusted
confidence intervals will be computed for the estimated values (Agresti-Coull adjustment) (7)
and the differences between placebo and intervention group (Agresti-Caffo adjustment) (8).
Statistical significance will be defined by a two-sided p-value <0.05. Wald adjusted confidence
intervals will also be computed for the estimated number of iFOBTs and number of
colonoscopies after a positive iFOBT needed to detect one advanced neoplasm (Agresti-Coull
adjustment) (7).
The total and partial area under the curve (truncated at specificity equal to 0.8) in ROC
analyses for the FOBGold®Tube Screen test will be computed, and their significance tested
at level 0.05, using the DeLong et al. (9) method or bootstrap, as implemented in the pROC R
package (10). The ROC curve will be plotted.
Additionally, a generalized mixed effects model for binomial data with logit link function having
sensitivity or specificity as response variables, and intervention group, sex, test and day of
stool sample collection as explanatory variables, will be fitted. Replicate measurements on the
same participant will be accounted for by a random intercept.
The analyses will be performed on participants in the per-protocol and intention-to-screen
analysis set providing samples at day 2.
Changes in sensitivity and specificity across days of stool sample collection will be plotted. The
specificity and sensitivity values will be computed for the per-protocol analysis set at day “0”
                                                                                                 8
                                     Statistical Analysis Plan

(before study medication), 2, 3 and 4. Differences will be taken between values at each of the
days 2, 3, and 4 with respect to values at day 0.
Finally, diagnostic performance when test results from multiple days are combined will also be
evaluated.
Serious adverse events will be evaluated and listed.


5.6     Planned subgroup analyses

Sensitivity and specificity analyses will be stratified by sex, age (as dichotomized in lower than
60 and greater or equal to 60 years old), smoking status and BMI (as obtained from the ratio
between the weight and the square of the height in meters, and dichotomized in lower than 25
and greater or equal to 25 Kg/m2). Sensitivity will be additionally stratified by most advanced
finding at colonoscopy (sessile serrated polyp>=1cm and advanced adenoma). Interaction with
the stratification variable will be assessed by fitting a generalized linear model for binomial
data with logit link function, and evaluating the statistical significance of the interaction
coefficient at level 0.05.


6     Software

All analyses will be performed with R statistical software. The PropCIs package will be used
for the sensitivity and specificity confidence intervals. The pROC package (10) will be used,
instead, for the computation and plotting of the ROC curve, as well as for estimating the area
under the ROC curve and its significance.


7     Changes to the plan

Primary analysis set

The primary analysis is now performed on participants in the intention-to-screen analysis set
providing samples at day 2

Treatment of missing values

Missing values for the day of stool sample collection are included consistently with the
intention-to-screen analysis framework. Independence between missing values for the test
outcome defining the primary endpoint (FOBGold®Tube Screen test on day 2, intention-to-
screen analysis set) and group allocation is tested via Fisher’s exact test. The proportion of
missing values is also evaluated. A decision on their treatment is based on the outcomes of
the two evaluations.


8     References

      1. Brenner H, Tao S, Haug U. Low-dose aspirin use and performance of immunochemical
         fecal occult blood tests. JAMA. 2010;304(22):2513-20.

      2. Levi Z, Rozen P, Hazazi R, Vilkin A, Waked A, Maoz E, et al. A quantitative
         immunochemical fecal occult blood test for colorectal neoplasia. Ann Intern Med.
         2007;146(4):244-55.

      3. Hundt S, Haug U, Brenner H. Comparative evaluation of immunochemical fecal occult
         blood tests for colorectal adenoma detection. Ann Intern Med. 2009;150(3):162-9.


                                                                                                9
                                 Statistical Analysis Plan

4. Santilli F, Rocca B, De Cristofaro R, Lattanzio S, Pietrangelo L, Habib A, et al. Platelet
   cyclooxygenase inhibition by low-dose aspirin is not reflected consistently by platelet
   function assays: implications for aspirin "resistance". J Am Coll Cardiol.
   2009;53(8):667-77.

5. Zisman E, Erport A, Kohanovsky E, Ballagulah M, Cassel A, Quitt M, et al. Platelet
   function recovery after cessation of aspirin: preliminary study of volunteers and surgical
   patients. Eur J Anaesthesiol. 2010;27(7):617-23.

6. Gibbs NM, Weightman WM, Thackray NM, Michalopoulos N, Weidmann C. The effects
   of recent aspirin ingestion on platelet function in cardiac surgical patients. J
   Cardiothorac Vasc Anesth. 2001;15(1):55-9

7. Agresti A, Coull B. Approximate is better than “exact” for interval estimation of binomial
   proportions. Am Statist 1998;52:119-26.

8. Agresti A, Caffo B. Simple and effective confidence intervals for proportions and
   difference of proportions result from adding two successes and two failures. The
   American Statistician 2000;54(4):280–288.

9. DeLong ER, DeLong DM, Clarke-Pearson DL. Comparing the areas under two or more
   correlated   receiver   operating  characteristic curves:  a    nonparametric
   approach. Biometrics 1988:44:837–845.

10. Robin X, Turck N, Hainard A, et al. pROC: an open-source package for R and S+ to
    analyze and compare ROC curves. BMC Bioinformatics 2011:7:77.




                                                                                          10
```

Audit precision repair: OR06 is described as a generalized linear mixed model with site random intercept; no site-model family/link is inferred from the separate SAP participant model. Numerical transcription is unchanged.
