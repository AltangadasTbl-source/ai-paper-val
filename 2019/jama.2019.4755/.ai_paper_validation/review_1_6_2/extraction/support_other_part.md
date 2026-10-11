# Support quantitative evidence: SAP, results supplement, availability statement

Fresh support mapping shard; no candidate diagnosis or prior AI conclusions used. Exact scope: DOC-003 `joi190039supp2_prod.pdf` PDF pp.1–10 (PLAN), DOC-004 `joi190039supp3_prod.pdf` pp.1–8 (REPORT), DOC-005 `joi190039supp4_prod.pdf` p.1 (REPORT). All 19 assigned units inspected and mapped; all are reusable-backed. Scientific coverage gaps: none. No Office/workbook/CSV source is in this shard; formula versus cached-value distinction is not applicable.

## Evidence provenance and transcription rules

Curator-confirmed reusable layout assets: `.ai_paper_validation/review_1_5_1/preprocessing/support/DOC-003_pp1-10_layout.txt`, `DOC-004_pp1-3_layout.txt`, and `DOC-005_p1_layout.txt` in that same directory. DOC-004 pp.4–8 use `.ai_paper_validation/document_outputs/doc-b45e07a04d82/normalized_pages/page-N.txt` and corresponding reusable page images. Supplied PDF content is authoritative. Direct CPU visual confirmation of DOC-004 p.7 used Poppler pdftoppm 26.01.0: `pdftoppm -f 7 -l 7 -singlefile -r 110 -png joi190039supp3_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/support-other-DOC004-p7`; output `preprocessing/support-other-DOC004-p7.png`. No fresh OCR required.

Transcription limitation resolved by visual mapping: DOC-004 p.7 normalized/native text includes women's PPV point-difference tokens -18.2, -25.7, -21.6, whereas both reusable and fresh source render show only a dash in each point-estimate cell. Below, the visual printed reading is `—`; embedded text-layer values are retained separately as derivative/source-layer metadata. These are not substituted into the displayed table. All CIs and other cells are visible. No finding is inferred here.

Relationship identifiers N200–N205 are numeric/display groups; S200–S217 are statistical plan relationships; S218–S221 cover every inferential result row in eTables 3–6. Grouping preserves all cells and does not limit checking. Each grouped result relationship names every row explicitly below.

## Page coverage

| Source | PDF page | Role | Complete content mapped | Relationship IDs |
|---|---:|---|---|---|
| DOC-003 | 1 | PLAN | SAP title, EudraCT 2011-005603-32, internal study K357; no result-relevant quantitative analysis on title page | No-applicable administrative unit |
| DOC-003 | 2 | PLAN | Objectives, diagnostic metrics, two tests, study design, target population, medication, sample schedule | N200, S200, S201 |
| DOC-003 | 3 | PLAN | Sampling flexibility, colonoscopy timing, delayed-colonoscopy sensitivity analysis, dropout, datasets | S201, S202 |
| DOC-003 | 4 | PLAN | Full/per-protocol/intention-to-screen definitions; age/eligibility; day-numbering footnote | S203, S204, N200 |
| DOC-003 | 5 | PLAN | Remaining eligibility and medication timing/safety thresholds | N200 |
| DOC-003 | 6 | PLAN | Demographic variables, primary/secondary endpoints, thresholds, disease categories | S205, S206 |
| DOC-003 | 7 | PLAN | Auxiliary timing variables, missingness, flow, baseline tests, compliance, primary analysis introduction | S207, S208, S209 |
| DOC-003 | 8 | PLAN | Primary hypothesis/analysis/CIs; secondary definitions, ROC, mixed model, analysis populations | S210, S211, S212, S213, S214 |
| DOC-003 | 9 | PLAN | Time comparisons, combined samples, safety, subgroups, software, changes to primary population and missingness | S215, S216, S217 |
| DOC-003 | 10 | PLAN | References 4–10, including binomial intervals and ROC methods; no new quantitative relationship | No-applicable bibliography unit |
| DOC-004 | 1 | REPORT | Contents names all six eTables and matching outcomes; no additional result values | Matching keys below |
| DOC-004 | 2 | REPORT | eTable 1 inclusion and first exclusion criteria | N201 |
| DOC-004 | 3 | REPORT | eTable 1 exclusion criteria continuation | N201 |
| DOC-004 | 4 | REPORT | eTable 2 every count, schedule, actual-day column, and footnote | N202 |
| DOC-004 | 5 | REPORT | eTable 3 all 9 rows, 2x2 counts, sensitivity/specificity and differences/CIs | N203, S218 |
| DOC-004 | 6 | REPORT | eTable 4 all 9 per-protocol rows, 2x2 counts, sensitivity/specificity and differences/CIs | N204, S219 |
| DOC-004 | 7 | REPORT | eTable 5 all 9 PPV/NPV rows, differences/CIs, visible versus text-layer distinction | N205, S220 |
| DOC-004 | 8 | REPORT | eTable 6 all 9 site-effect rows, random-intercept SD, likelihood-ratio P values and hypothesis | S221 |
| DOC-005 | 1 | REPORT | Availability: protocol citation, statistical-code contact, dataset unavailable; no quantitative results or analysis plan | No-applicable availability unit |

All evidence links below are relative to this extraction file (three directory levels below package root).

## SAP quantitative and statistical relationships

### N200 — planned enrollment, intervention and eligibility

[DOC-003 pp.2–5](../../../joi190039supp2_prod.pdf#page=2), PLAN. Target 2400; eligible age 40–80 years; randomized double-blind multicenter placebo-controlled trial. Single 300 mg ASA versus placebo. Two iFOBT types, four kits of each, eight total. Premenopausal women need negative pregnancy test; postmenopause means no menstrual bleeding at least 12 months or surgical sterilization. Exclusion timing: anticoagulants/antiplatelets within two weeks, ASA within one week, NSAIDs/COX-2 inhibitors within three days; severe kidney disease GFR <30 ml/min; myocardial infarction within past six months; intended methotrexate ≥15 mg/week. These eligibility values support matching of analysis populations rather than outcome effects.

### S200 — objectives and outcome hierarchy

[DOC-003 p.2](../../../joi190039supp2_prod.pdf#page=2), PLAN. Objective diagnostic performance (sensitivity, specificity, PPV, NPV, likelihood ratios, area under curve) of two iFOBTs for advanced colorectal neoplasms after single ASA versus placebo. Secondary objectives: gender-specific performance, possible gain from sampling multiple days, safety; optional additional secondary blood biomarkers. Main-paper matching keys: primary sensitivity, qualitative-test sensitivity, sex strata, multiple-sample analyses, adverse events; no result assertion here.

### S201 — timing and numbering

[DOC-003 pp.2–4](../../../joi190039supp2_prod.pdf#page=2), PLAN. Original visit day 0, medication day 1, baseline day 0/1 before medication, subsequent samples days 3,4,5 preferably consecutive; if baseline impossible, skip it and take medication day 1. Sampling can move to subsequent day for constipation/other reasons; only two samples (baseline plus day 3) permitted. One kit per test at each time point, actual collection day documented. p.4 footnote explicitly changes numbering to medication day 0; original days 3/4/5 become days 2/3/4. This disclosed renumbering is essential for matching main day 2 and supplement schedule ≤0,2,3,4.

### S202 — colonoscopy timing, exclusions and datasets

[DOC-003 p.3](../../../joi190039supp2_prod.pdf#page=3), PLAN. At least four ASA-free days between dose and colonoscopy; maximum study-start-to-colonoscopy interval three months. Sensitivity analyses for colonoscopy postponed >3 months; no colonoscopy classified dropout. Colonoscopy/histology extracted blinded. Main analysis dataset includes blood/stool collection, diary, colonoscopy, iFOBT, questionnaire, demographic/randomization and auxiliary variables; eCRF includes eligibility, timing, demographics/randomization, vital signs, end-of-study and adverse events. Matching keys: available colonoscopy result and prolonged-delay sensitivity analysis.

### S203 — full and per-protocol analysis sets

[DOC-003 p.4](../../../joi190039supp2_prod.pdf#page=4), PLAN. Full set: all recruited subjects complying with protocol inclusion/exclusion; used for demographic and sampling-compliance tabulation. Per-protocol: at least one stool sample on exactly expected collection day; first any time before or same day as medication (described as minor deviation from protocol's baseline day -1 or 0); later sample day 2,3,4. Eligibility, valid result, colonoscopy after sample apply. Matching key: eTable 4/5 per-protocol and main per-protocol sensitivity analyses.

### S204 — intention-to-screen analysis set

[DOC-003 p.4](../../../joi190039supp2_prod.pdf#page=4), PLAN. Participants providing at least one stool sample with valid result collected before colonoscopy (or timing information unavailable). Matching key: main primary intention-to-screen results, eTable 2 valid-result footnote and eTable 6 analysis population. Read alongside explicit p.9 changes in S217.

### S205 — primary endpoint and disease definition

[DOC-003 p.6](../../../joi190039supp2_prod.pdf#page=6), PLAN. Primary variable FOBGold Tube Screen sensitivity for advanced neoplasms, specified as colorectal cancer or advanced adenoma. Quantitative outcome ng Hb/ml buffer; categorical positive/negative/invalid. Manufacturer threshold 17 μg Hb/g feces and lower threshold printed `10.2 Hb/g feces` (p.8 supplies μg). Colonoscopy categories: cancer, advanced adenoma, sessile serrated polyp ≥1 cm, sessile serrated polyp <1 cm, nonadvanced adenoma, hyperplastic polyp, undefined polyp, no finding. Matching keys: main advanced-neoplasm composite and thresholds 10.2/17.

### S206 — secondary endpoints and qualitative categories

[DOC-003 p.6](../../../joi190039supp2_prod.pdf#page=6), PLAN. FD Hb/Hp Complex quick-test sensitivity, FOBGold ROC AUC, both tests' specificity, LR, PPV, NPV; iFOBTs and colonoscopies after positive iFOBT needed per advanced neoplasm. Qualitative outcome positive/weakly positive/negative/invalid. Demographic variables sex, consent year, birth year, screening/diagnostic indication, weight kg, height cm, current smoker/nonsmoker. Matching keys: main secondary diagnostics and supplementary PPV/NPV.

### S207 — missing/invalid and same-day duplicate samples

[DOC-003 p.7](../../../joi190039supp2_prod.pdf#page=7), PLAN. Test-outcome missingness and missing sample-collection day excluded; invalid test results treated as missing and excluded. If multiple samples of given test same day, use first valid sample in scheduled-iFOBT sequence. Date differences sample-minus-medication and colonoscopy-minus-sample measured days define analysis sets. Read alongside p.9 change for missing collection day, S217.

### S208 — disposition and baseline comparison

[DOC-003 p.7](../../../joi190039supp2_prod.pdf#page=7), PLAN. CONSORT numbers recruited, full set and excluded by reason; baseline age, sex, colonoscopy indication and outcome. Age consent year minus birth year, grouped 5-year classes. Absolute/percent frequencies overall and per arm; chi-square or Fisher exact comparison. Matching keys: main flow and Table 1 baseline; no adjustment model asserted here.

### S209 — compliance tabulations

[DOC-003 p.7](../../../joi190039supp2_prod.pdf#page=7), PLAN. Absolute sample frequencies by actual collection day, missing/invalid status, stratified expected day, test and intervention group. Main matching key eTable 2; all its columns mapped under N202.

### S210 — original primary analysis and inferential method

[DOC-003 pp.7–8](../../../joi190039supp2_prod.pdf#page=8), PLAN. Sensitivity = positive among diseased. Thresholds manufacturer 17 μg Hb/g feces and FD Hb/Hp threshold 10.2 μg Hb/g feces. Null no change in sensitivity ASA versus placebo. Originally per-protocol day-2 samples. Wald adjusted CIs: Agresti–Coull for sensitivity, Agresti–Caffo for arm difference. Significance two-sided P<.05. Subsequent amendment is S217, not silently merged. Matching keys main sensitivity estimates, 95% CIs/differences and P values; eTable 4 per-protocol results.

### S211 — secondary metric definitions

[DOC-003 p.8](../../../joi190039supp2_prod.pdf#page=8), PLAN. Qualitative positivity positive or weakly positive. Specificity negative among healthy; PPV diseased among positives; NPV healthy among negatives; LR for given result = proportion with that result among diseased / proportion among healthy. ROC horizontal coordinate positive among healthy, vertical sensitivity, over increasing positivity thresholds. Number iFOBTs per detected advanced neoplasm = total tests / positive diseased; colonoscopies after positive test per detected advanced neoplasm = total positive tests / positive diseased. Matching keys main performance metrics; eTable 5 PPV/NPV.

### S212 — secondary binomial tests and intervals

[DOC-003 p.8](../../../joi190039supp2_prod.pdf#page=8), PLAN. Test no ASA-placebo change in qualitative sensitivity, both tests' specificity/PPV/NPV. Agresti–Coull adjusted Wald metric CIs and Agresti–Caffo arm-difference CIs; two-sided P<.05. Adjusted Wald CIs also planned for number iFOBTs/colonoscopies per advanced neoplasm. Secondary day-2 analyses in per-protocol and intention-to-screen. Main matching keys secondary performance and eTables 4/5; denominators depend on disease/test-result conditioning.

### S213 — ROC analysis

[DOC-003 p.8](../../../joi190039supp2_prod.pdf#page=8), PLAN. Total and partial AUC, partial truncated at specificity .8; significance .05, DeLong or bootstrap via pROC R; ROC plotted. Matching keys main AUC and ROC display, both total/partial-AUC status.

### S214 — repeated-measure mixed model

[DOC-003 p.8](../../../joi190039supp2_prod.pdf#page=8), PLAN. Generalized mixed-effects binomial model with logit link; sensitivity or specificity response; group, sex, test and stool-collection day explanatory variables; participant random intercept for repeated measurements. Matching keys main analysis methods and repeated-day assessment. Participant random intercept here is distinct from study-site random intercept eTable 6.

### S215 — across-day, combined-day and safety analyses

[DOC-003 pp.8–9](../../../joi190039supp2_prod.pdf#page=9), PLAN. Per-protocol sensitivity/specificity computed baseline “0” before medication and days 2,3,4; plot across days and differences each post-dose day versus baseline. Combined-day performance also evaluated; serious adverse events evaluated/listed. Matching keys main Figure over sampling days, multiple-day eTable 3, safety narrative.

### S216 — subgroup analyses and software

[DOC-003 p.9](../../../joi190039supp2_prod.pdf#page=9), PLAN. Sensitivity/specificity strata sex, age <60/≥60 years, current smoking, BMI <25/≥25 kg/m², BMI weight/(height in meters)². Sensitivity additionally by most advanced colonoscopy finding (sessile serrated polyp ≥1 cm and advanced adenoma). Interaction binomial GLM logit and interaction coefficient significance .05. All analyses R; PropCIs for sensitivity/specificity CI; pROC for ROC/AUC significance. Matching keys main subgroup status, including sex, age, smoking, BMI and colonoscopy-finding interactions.

### S217 — explicitly disclosed SAP changes

[DOC-003 p.9 section 7](../../../joi190039supp2_prod.pdf#page=9), PLAN. Primary analysis now intention-to-screen day-2 samples. Missing sample day included consistent with intention-to-screen. Independence between missing primary-endpoint test outcome (FOBGold day 2 intention-to-screen) and treatment allocation tested by Fisher exact; missing proportion evaluated; treatment decision based on both evaluations. No explicit numerical imputation rule stated on this page. Matching keys main primary population and reported missingness handling; retain this change when comparing earlier S203/S207/S210.

## Results supplement eligibility

### N201 — eTable 1 full eligibility, DOC-004 pp.2–3

[DOC-004 p.2](../../../joi190039supp3_prod.pdf#page=2), REPORT. Inclusion age 40–80, negative pregnancy test for premenopausal, postmenopause ≥12 months no menstrual bleeding or surgical sterilization; planned screening/diagnostic colonoscopy; German understanding/consent/compliance. Exclusions: inflammatory bowel disease, positive-FOBT-driven colonoscopy, cancer history, angiodysplasia, rectal blood loss; anticoagulants/antiplatelets past two weeks, ASA past week, NSAID/COX-2 past three days. Safety exclusions: acute ulcer signs, thrombocytopenia, infection, dehydration, allergy, severe/uncontrolled asthma, severe kidney/liver disease (GFR<30 ml/min, cirrhosis), severe heart failure, uncontrolled hypertension, other symptoms; histories severe gastrointestinal bleed, bleeding diathesis, aspirin-sensitive asthma, drug hypersensitivity/intolerance, gout, oxaluria, G6PD/glutathione peroxidase deficiency, epilepsy, severe cardiac disease including MI past six months; intended anticoagulants/antiplatelets/NSAIDs, methotrexate≥15 mg/week, systemic glucocorticoids, SSRI, valproic acid; surgery/dental treatment; alcohol/illicit-drug abuse, pregnancy, suspected noncompliance, another trial. Matching key main eligibility and SAP N200; no result numbers on these two pages.

## N202 — eTable 2 sample counts, every cell

[DOC-004 p.4](../../../joi190039supp3_prod.pdf#page=4), REPORT. Intervention N=1075; control N=1059. Rows count sample results, not necessarily unique participants. Scheduled days relative to tablet intake. Valid result requires valid test and sample before colonoscopy (or timing information unavailable). Footnote c marks actual-day-2 samples used for per-protocol analysis. Actual-day columns count valid results, with `Missing` meaning actual collection timing missing. `Any` is sum across scheduled rows. Main matching keys analysis-set flow, compliance and per-protocol/day-2 denominators.

| Arm | Test | Scheduled day | Returned | Valid | Actual Missing | <0 | 0 | 1 | 2 | 3 | 4 | >4 |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Intervention | Quantitative | ≤0 | 1044 | 1026 | 82 | 152 | 781 | 9 | 1 | 0 | 0 | 1 |
| Intervention | Quantitative | 2 | 1045 | 1030 | 77 | 2 | 11 | 126 | 758 | 48 | 5 | 3 |
| Intervention | Quantitative | 3 | 989 | 975 | 77 | 1 | 0 | 9 | 105 | 700 | 65 | 18 |
| Intervention | Quantitative | 4 | 955 | 944 | 64 | 1 | 0 | 0 | 7 | 93 | 677 | 102 |
| Intervention | Quantitative | Any | 4033 | 3975 | 300 | 156 | 792 | 144 | 871 | 841 | 747 | 124 |
| Intervention | Qualitative | ≤0 | 1037 | 970 | 78 | 149 | 733 | 8 | 1 | 0 | 0 | 1 |
| Intervention | Qualitative | 2 | 1040 | 974 | 75 | 2 | 9 | 121 | 719 | 42 | 4 | 2 |
| Intervention | Qualitative | 3 | 979 | 922 | 71 | 1 | 0 | 9 | 97 | 663 | 65 | 16 |
| Intervention | Qualitative | 4 | 955 | 887 | 60 | 1 | 0 | 0 | 7 | 88 | 638 | 93 |
| Intervention | Qualitative | Any | 4011 | 3753 | 284 | 153 | 742 | 138 | 824 | 793 | 707 | 112 |
| Control | Quantitative | ≤0 | 1016 | 1000 | 80 | 159 | 753 | 5 | 2 | 0 | 0 | 1 |
| Control | Quantitative | 2 | 1024 | 1012 | 78 | 2 | 4 | 136 | 747 | 38 | 4 | 3 |
| Control | Quantitative | 3 | 987 | 979 | 75 | 1 | 1 | 5 | 114 | 706 | 58 | 19 |
| Control | Quantitative | 4 | 959 | 947 | 72 | 1 | 0 | 1 | 1 | 104 | 656 | 112 |
| Control | Quantitative | Any | 3986 | 3938 | 305 | 163 | 758 | 147 | 864 | 848 | 718 | 135 |
| Control | Qualitative | ≤0 | 1026 | 968 | 76 | 149 | 735 | 5 | 2 | 0 | 0 | 1 |
| Control | Qualitative | 2 | 1024 | 969 | 72 | 2 | 4 | 126 | 720 | 39 | 3 | 3 |
| Control | Qualitative | 3 | 979 | 934 | 73 | 1 | 1 | 5 | 108 | 677 | 51 | 18 |
| Control | Qualitative | 4 | 956 | 905 | 66 | 1 | 0 | 1 | 1 | 103 | 627 | 106 |
| Control | Qualitative | Any | 3985 | 3776 | 287 | 153 | 740 | 137 | 831 | 819 | 681 | 128 |

## N203 / S218 — eTable 3 combined samples, every row

[DOC-004 p.5](../../../joi190039supp3_prod.pdf#page=5), REPORT. Advanced neoplasms colorectal cancer or advanced adenoma; single 300 mg ASA/placebo; at least one positive from up to three samples scheduled days 2,3,4. Header does not independently name analysis population. Cutoffs μg Hb/g; Se/Sp and differences percentage units, CIs 95%. Reference contrast aspirin minus placebo. TP true positive, FN false negative, TN true negative, FP false positive. Each arm tuple below is TP/FN/TN/FP; Se and Sp must be matched to its disease/healthy denominator. No P values printed. Main matching key multiple-day secondary analysis, not primary single-day estimates.

| Sex | Test | Cutoff | ASA TP/FN/TN/FP | ASA Se/Sp % | Placebo TP/FN/TN/FP | Placebo Se/Sp % | Se difference [95% CI] | Sp difference [95% CI] |
|---|---|---:|---|---|---|---|---|---|
| All | Quantitative | 10.2 | 63/50/685/261 | 55.8/72.4 | 49/58/774/161 | 45.8/82.8 | 10.0 [-3.3,22.8] | -10.4 [-14.1,-6.6] |
| All | Quantitative | 17.0 | 44/69/816/130 | 38.9/86.3 | 35/72/852/83 | 32.7/91.1 | 6.2 [-6.4,18.7] | -4.9 [-7.7,-2.0] |
| All | Qualitative | 10.2 | 53/58/714/222 | 47.7/76.3 | 35/73/779/146 | 32.4/84.2 | 15.3 [2.3,27.8] | -7.9 [-11.5,-4.3] |
| Men | Quantitative | 10.2 | 46/31/311/148 | 59.7/67.8 | 28/30/362/102 | 48.3/78.0 | 11.5 [-5.5,27.8] | -10.3 [-15.9,-4.5] |
| Men | Quantitative | 17.0 | 34/43/384/75 | 44.2/83.7 | 22/36/408/56 | 37.9/87.9 | 6.2 [-10.5,22.4] | -4.3 [-8.8,0.3] |
| Men | Qualitative | 10.2 | 41/34/343/111 | 54.7/75.6 | 19/40/372/89 | 32.2/80.7 | 22.5 [5.6,38.0] | -5.1 [-10.5,0.2] |
| Women | Quantitative | 10.2 | 17/19/374/113 | 47.2/76.8 | 21/28/412/59 | 42.9/87.5 | 4.4 [-16.7,25.1] | -10.7 [-15.4,-5.8] |
| Women | Quantitative | 17.0 | 10/26/432/55 | 27.8/88.7 | 13/36/444/27 | 26.5/94.3 | 1.2 [-17.4,20.4] | -5.6 [-9.1,-2.0] |
| Women | Qualitative | 10.2 | 12/24/371/111 | 33.3/77.0 | 16/33/407/57 | 32.7/87.7 | 0.7 [-19.0,20.7] | -10.7 [-15.5,-5.9] |

Native text prints men quantitative 10.2 Se CI separator as `[-5.5. 27.8]`; numbers retained without assigning scientific meaning to separator punctuation. There are no additional figure panels on this page.

## N204 / S219 — eTable 4 per-protocol day 2, every row

[DOC-004 p.6](../../../joi190039supp3_prod.pdf#page=6), REPORT. Advanced neoplasms colorectal cancer or advanced adenoma; single 300 mg ASA/placebo; day 2 per-protocol explicitly labeled. Cutoffs μg Hb/g; Se/Sp and differences percentage units; 95% CIs. Contrast aspirin minus placebo. Tuple definitions identical to N203; no P values printed. Main matching key per-protocol sensitivity/specificity and sex strata, distinct from intention-to-screen primary Table 2.

| Sex | Test | Cutoff | ASA TP/FN/TN/FP | ASA Se/Sp % | Placebo TP/FN/TN/FP | Placebo Se/Sp % | Se difference [95% CI] | Sp difference [95% CI] |
|---|---|---:|---|---|---|---|---|---|
| All | Quantitative | 10.2 | 42/56/635/136 | 42.9/82.4 | 25/61/691/85 | 29.1/89.0 | 13.8 [-0.1,27.1] | -6.7 [-10.1,-3.2] |
| All | Quantitative | 17.0 | 29/69/704/67 | 29.6/91.3 | 18/68/735/41 | 20.9/94.7 | 8.7 [-4.0,20.8] | -3.4 [-5.9,-0.8] |
| All | Qualitative | 10.2 | 30/56/617/119 | 34.9/83.8 | 19/65/683/62 | 22.6/91.7 | 12.3 [-1.4,25.4] | -7.8 [-11.2,-4.5] |
| Men | Quantitative | 10.2 | 31/34/310/78 | 47.7/79.9 | 11/34/344/58 | 24.4/85.6 | 23.2 [5.0,39.5] | -5.7 [-10.9,-0.4] |
| Men | Quantitative | 17.0 | 23/42/350/38 | 35.4/90.2 | 9/36/373/29 | 20.0/92.8 | 15.4 [-1.8,30.9] | -2.6 [-6.5,1.4] |
| Men | Qualitative | 10.2 | 24/33/311/63 | 42.1/83.2 | 9/37/353/40 | 19.6/89.8 | 22.5 [4.5,38.6] | -6.7 [-11.5,-1.8] |
| Women | Quantitative | 10.2 | 11/22/325/58 | 33.3/84.9 | 14/27/347/27 | 34.1/92.8 | -0.8 [-21.8,20.6] | -7.9 [-12.3,-3.4] |
| Women | Quantitative | 17.0 | 6/27/354/29 | 18.2/92.4 | 9/32/362/12 | 22.0/96.8 | -3.8 [-21.6,15.0] | -4.4 [-7.6,-1.1] |
| Women | Qualitative | 10.2 | 6/23/306/56 | 20.7/84.5 | 10/28/330/22 | 26.3/93.8 | -5.6 [-25.1,15.3] | -9.2 [-13.7,-4.6] |

## N205 / S220 — eTable 5 predictive values, every row

[DOC-004 p.7](../../../joi190039supp3_prod.pdf#page=7), REPORT. PPV and NPV % for advanced neoplasms colorectal cancer or advanced adenoma at day 2, single 300 mg ASA/placebo, explicitly per-protocol. Contrast aspirin minus placebo, 95% CIs, no P values or explicit denominators on this page. Matching numeric inputs reside in eTable 4 (N204); PPV conditions on positive tests, NPV on negative tests. Main matching key predictive values and per-protocol secondary analyses. Cutoff column visual header shows `[μg` on first line; content/table context μg Hb/g.

| Sex | Test | Cutoff | ASA PPV/NPV % | Placebo PPV/NPV % | Displayed PPV difference [95% CI] | NPV difference [95% CI] |
|---|---|---:|---|---|---|---|
| All | Quantitative | 10.2 | 23.6/91.9 | 22.7/91.9 | 0.9 [-9.3,10.7] | 0.0 [-2.8,2.8] |
| All | Quantitative | 17.0 | 30.2/91.1 | 30.5/91.5 | -0.3 [-15.3,14.2] | -0.5 [-3.3,2.3] |
| All | Qualitative | 10.2 | 20.1/91.7 | 23.5/91.3 | -3.3 [-14.8,7.7] | 0.4 [-2.6,3.3] |
| Men | Quantitative | 10.2 | 28.4/90.1 | 15.9/91.0 | 12.5 [-0.2,24.1] | -0.9 [-5.2,3.4] |
| Men | Quantitative | 17.0 | 37.7/89.3 | 23.7/91.2 | 14.0 [-4.9,31.1] | -1.9 [-6.1,2.2] |
| Men | Qualitative | 10.2 | 27.6/90.4 | 18.4/90.5 | 9.2 [-5.9,22.8] | -0.1 [-4.4,4.2] |
| Women | Quantitative | 10.2 | 15.9/93.7 | 34.1/92.8 | — [-34.7,-1.3] | 0.9 [-2.9,4.6] |
| Women | Quantitative | 17.0 | 17.1/92.9 | 42.9/91.9 | — [-48.4,-0.7] | 1.0 [-2.7,4.8] |
| Women | Qualitative | 10.2 | 9.7/93.0 | 31.2/92.2 | — [-38.9,-3.9] | 0.8 [-3.2,4.8] |

Text-layer-only tokens: women quantitative 10.2 PPV difference -18.2; women quantitative 17.0 -25.7; women qualitative 10.2 -21.6. Reused normalized/native layout breaks these values onto successive lines; visual rendering retains only dash glyph. They are not claimed as visible numeric point estimates. All CI values above are visual/source confirmed.

## S221 — eTable 6 study-site sensitivity analysis, every row

[DOC-004 p.8](../../../joi190039supp3_prod.pdf#page=8), REPORT. Estimated generalized linear mixed-model study-site random-intercept standard deviations (St. Dev.) and likelihood-ratio-test P values. Null SD=0 versus alternative SD>0. Successful outcome agreement between test and colonoscopy detection of advanced neoplasms colorectal cancer or advanced adenoma day 2 after single 300 mg ASA/placebo. Explicit intention-to-screen population. Cutoffs μg Hb/g. Separate sensitivity and specificity fits; no CIs, test statistics, degrees of freedom or treatment effects printed. Main matching key post hoc/site-effect sensitivity analysis methods and eTable 6 citation; do not conflate with SAP participant random intercept S214.

| Sex | Test | Cutoff | Sensitivity SD | Sensitivity P | Specificity SD | Specificity P |
|---|---|---:|---:|---:|---:|---:|
| All | Quantitative | 10.2 | 0.00E+00 | 0.50 | 5.49E-03 | 0.38 |
| All | Quantitative | 17.0 | 1.97E-01 | 0.16 | 0.00E+00 | 0.50 |
| All | Qualitative | 10.2 | 0.00E+00 | 0.50 | 9.23E-03 | 0.30 |
| Men | Quantitative | 10.2 | 0.00E+00 | 0.50 | 1.00E-14 | 0.50 |
| Men | Quantitative | 17.0 | 0.00E+00 | 0.50 | 1.47E-02 | 0.40 |
| Men | Qualitative | 10.2 | 0.00E+00 | 0.50 | 1.13E-02 | 0.35 |
| Women | Quantitative | 10.2 | 0.00E+00 | 0.50 | 1.79E-12 | 0.50 |
| Women | Quantitative | 17.0 | 1.67E-01 | 0.40 | 0.00E+00 | 0.50 |
| Women | Qualitative | 10.2 | 4.35E-16 | 0.50 | 0.00E+00 | 0.50 |

## DOC-005 availability record

[DOC-005 p.1](../../../joi190039supp4_prod.pdf#page=1), REPORT. Protocol identified as open-access ASTER phase III randomized double-blind placebo-controlled protocol, Tikk et al. BMC Cancer 2018;18(1):914. Statistical code available from Silvia Calderazzo; dataset not available. This is an availability statement, not an additional analysis plan, workbook, or results record. Bibliographic numerals are not trial results. No applicable quantitative relationship.

## Shard completion and matching handoff

Mapped 19/19 pages: SAP 10/10, results supplement 8/8, availability 1/1. Relationships: six numeric/display groups N200–N205 and 22 inferential/statistical groups S200–S221. eTable 2 contributes 20 count rows; eTables 3–6 contribute 36 result rows (nine each), including all estimates, intervals, P values, labels, units and footnotes. Complete primary/secondary SAP specifications and the explicit changes in section 7 are represented. No formula/cached workbook values exist in assigned sources. No scientific-coverage limitation; visual versus embedded-text distinction on DOC-004 p.7 retained explicitly. Main-paper keys are matching descriptors for the coordinator's main map; no main-source page was inspected outside this disjoint shard.

Final inventory read: current `source_coverage.md` identifies all 19 assigned pages as reusable-backed; `evidence_asset_inventory.md` assets A105/A106/A107 identify SAP, supplementary cover/eligibility, availability layout; A052–A056 identify supplement normalized text; A067 identifies reusable p.7 visual with A055 PARTIAL cell reading. Fresh render above provides direct visual confirmation, without changing reusable unit counts.
