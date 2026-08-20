# Support Quantitative Evidence Map — support-006

## Scope, method, and completion

- **Assigned direct-source units:** DOC-004 `joi240158supp3_prod_1742927563.7911.pdf`, PDF pp. 1-26 (reusable-backed); DOC-005 `joi240158supp4_prod_1742927563.8061.pdf`, PDF pp. 1-6 (fresh-required); and DOC-006 `joi240158supp5_prod_1742927563.8111.pdf`, PDF p. 1 (fresh-required).
- **Completed units:** 33/33 PDF pages. DOC-004 reusable page-native text was read completely and table/figure pages were checked against direct-PDF text and fresh 120-dpi source renders (pp. 14-25). DOC-005 and DOC-006 were freshly extracted from the direct PDFs with `pdftotext` native and layout modes; their fresh layout/native files are under `preprocessing/support-006/`.
- **Evidence convention:** every PDF location below is a physical PDF page (not the printed supplemental page number). This is an evidence map, not a candidate diagnosis. Values are transcribed as displayed; a zero P value is not present in this shard.
- **Main-paper matching keys:** `HEALEY ALS Platform Trial; Regimen C (CNM-Au8); CNM-Au8 pooled active versus shared placebo; FAS; ERO/regimen-only; ALSFRS-R; SVC; PAV; DRR; serum/plasma NfL; TEAE`.

## DOC-004: eMethods, result tables, and eFigure

### Administrative/protocol and analysis definitions (pp. 1-13)

- **p. 1:** contents page: eMethods; eTables 1-5; eFigure. This page contains no result values beyond the contents labels.
- **pp. 2-4, Trial design/randomization/intervention:** randomized, double-blind, placebo-controlled Regimen C at 54 NEALS centers, enrolled July 2020-March 2022. Eligibility includes ALS disease duration **<=36 months** and vital capacity **>=50% predicted**. Regimen allocation and within-regimen treatment schedules were stratified by riluzole/edaravone use (**4 strata**); treatment blocks were size **8** (**3** 30-mg, **3** 60-mg, **2** placebo). Allocation was **3:3:2** to 60 mg, 30 mg, and placebo. Trial duration **24 weeks**; clinic weeks **0, 4, 8, 16, 24**, telephone weeks **2, 12, 20**, final telephone follow-up week **28**. Each daily dose used two **60-mL** bottles; each contained **30 mg** for the 60-mg dose or **15 mg** for the 30-mg dose.
- **pp. 5-7, endpoints/populations:** primary endpoint is change from baseline through 24 weeks in ALSFRS-R plus survival, modeled jointly. Secondary outcomes in hierarchy: (1) CAFS, joint rank of ALSFRS-R decline and survival free of PAV; PAV means ventilation **>22 h/day for >7 days**; (2) percent-predicted-normal SVC decline; (3) survival free of PAV. The primary combined-dose analysis compares 30-mg plus 60-mg CNM-Au8 with placebo; dose-specific analyses are prespecified exploratory. FAS includes all Regimen-C active, Regimen-C placebo, and placebo from Regimens A/B/D; regimen-only analyses include Regimen-C participants. Safety FAS excludes shared-placebo participants known ineligible because of gold allergy. Longitudinal primary-analysis visits are weeks **0, 4, 8, 12, 16, 20, 24** (early termination/ad hoc visits may substitute).
- **pp. 7-9, primary model/statistical definition:** Bayesian shared-parameter function/survival model. Disease rate ratio (DRR) is the ALSFRS-R-slope ratio in the functional component and hazard ratio in the survival component; **DRR <1** indicates slower progression and **DRR 0.50** denotes **50%** slowing. Illustrations: 6-point decline over 6 months in control would occur over 12 months at DRR 0.50; median survival 9 months in control would be 18 months at DRR 0.50. Function component: covariate-adjusted linear repeated-measures model; survival component: exponential proportional-hazards model; shared controls handled in Bayesian hierarchical meta-analytic framework. MCMC used **at least 500,000** posterior samples with thinning **10**. Futility interim starts at **40** randomized active participants (**30** active, **10** placebo), every **12 weeks** thereafter; stop if posterior probability is **<5%** that CNM-Au8 slows ALSFRS-R decline by **>=10%**. No early-success rule.
- **pp. 10-12, secondary/exploratory statistical definitions:** SVC is assessed with repeated-measures linear mixed and random-slopes models (months since onset, prebaseline delta-FRS, baseline riluzole/edaravone and time interactions; FAS models include random regimen-specific intercepts). Death, PAV/death-equivalent, and hospitalization are Cox proportional-hazards outcomes with delta-FRS, onset months, riluzole, edaravone, and age; a supportive analysis adds baseline serum NfL and NfL-by-visit. Serum Simoa testing uses two replicates; repeats occur for below-detection/one replicate or replicate CV **>25%**; <LOQ values are imputed with assay LOD. NfL is log transformed before analysis. Serum NfL FAS is prespecified but a regimen-only analysis is reported because plates differed; plasma NfL is described as post hoc. MMRM covariates are delta-FRS, onset months, riluzole, edaravone, covariate-by-visit and treatment-by-visit. Prespecified neurofilament analysis excludes no outliers; a post-hoc sensitivity exclusion (<**4 pg/mL** or <**2%** of a participant maximum) removes **one** placebo baseline NfL observation. Exploratory time-to-event Cox analyses include hospitalization, feeding tube, assisted ventilation, King stage 4, death, and death/PAV; King stage is interval censored, other variables right censored.
- **p. 13, subgroup model:** prespecified subgroups are riluzole, edaravone, age (<65/65+), sex, race, ethnicity, weight, BMI, chronic kidney disease, onset (<18/18+ months), El Escorial/onset, symptom severity, early disease, urate (<5.5/>=5.5 mg/dL), serum NfL median split, site of onset, delta-FRS median split, and site (sites with <5 pooled). A random-slopes model includes subgroup, subgroup-by-time, and subgroup-by-treatment-by-time for primary/secondary efficacy endpoints.

### eTable 1 — ALSFRS-R observed distribution (p. 14)

Table columns are CNM-Au8 pooled, shared placebo, and regimen placebo, each as **n; mean (SD)**. Values by visit are:

| Visit | CNM-Au8 pooled | Shared placebo | Regimen placebo |
|---|---|---|---|
| Baseline | 120; 34.3 (6.6) | 164; 35.1 (6.7) | 41; 36.1 (5.9) |
| Week 4 | 120; 33.0 (7.0) | 160; 34.5 (7.0) | 40; 35.4 (6.7) |
| Week 8 | 115; 32.3 (7.3) | 155; 33.4 (7.4) | 38; 34.3 (7.1) |
| Week 12 | 115; 31.4 (7.7) | 152; 32.7 (7.9) | 39; 33.7 (7.9) |
| Week 16 | 110; 30.5 (7.7) | 148; 31.8 (8.3) | 36; 32.5 (7.5) |
| Week 20 | 111; 29.7 (7.8) | 143; 31.2 (8.6) | 36; 32.6 (7.9) |
| Week 24 | 111; 29.1 (7.9) | 143; 30.2 (8.7) | 35; 31.4 (8.2) |

### eTable 2 — Bayesian shared-parameter primary efficacy analysis (p. 15)

| Parameter | Median | Mean (SD) | 95% credible interval | Pr(DRR <1.0) | Pr(DRR <0.9) |
|---|---:|---:|---|---:|---:|
| DRR, function and mortality | 0.96 | 0.97 (0.099) | (0.783, 1.175) | 0.6450 | 0.2505 |
| ALSFRS-R slope, Regimen-C placebo with sharing (points/month) | -1.03 | -1.03 (0.073) | (-1.181, -0.894) | — | — |
| ALSFRS-R slope, pooled CNM-Au8 (points/month) | -1.00 | -1.00 (0.075) | (-1.143, -0.847) | — | — |
| Mortality event rate, shared placebo (events/month) | 0.010 | 0.010 (0.0026) | (0.0054, 0.0154) | — | — |
| Mortality event rate, pooled CNM-Au8 (events/month) | 0.009 | 0.009 (0.0025) | (0.0052, 0.0150) | — | — |
| Covariate: months since onset | 1.03 | 1.03 (0.046) | (0.938, 1.120) | — | — |
| Covariate: prebaseline slope | 1.39 | 1.40 (0.079) | (1.255, 1.565) | — | — |
| Covariate: edaravone use | 1.13 | 1.13 (0.101) | (0.949, 1.344) | — | — |
| Covariate: riluzole use | 1.03 | 1.03 (0.093) | (0.854, 1.220) | — | — |

Footnote/label: DRR = disease rate ratio. Model covariates: baseline edaravone, baseline riluzole, months since symptom onset, and prebaseline ALSFRS-R slope.

### eTable 3A — FAS repeated-measures secondary/exploratory results (p. 16)

Outcome columns are 24-week change estimate by active and shared placebo, then active minus shared-placebo difference (SE), 95% CI, P value.

| Contrast and endpoint | Active change | Shared-placebo change | Difference (SE) | 95% CI | P |
|---|---:|---:|---:|---|---:|
| Pooled CNM-Au8 (n=120) vs shared placebo (n=164): ALSFRS-R total score | -5.47 (0.43) | -5.51 (0.36) | 0.0 (0.55) | -1.03, 1.11 | 0.94 |
| Pooled: SVC (% predicted) | -9.32 (1.36) | -8.53 (1.15) | -0.78 (1.77) | -4.25, 2.68 | 0.66 |
| CNM-Au8 30 mg (n=59) vs shared placebo (n=164): ALSFRS-R | -5.70 (0.59) | -5.51 (0.36) | -0.19 (0.69) | -1.53, 1.16 | 0.79 |
| 30 mg: SVC (% predicted) | -7.84 (1.84) | -8.53 (1.15) | 0.69 (2.19) | -3.55, 4.92 | 0.75 |
| CNM-Au8 60 mg (n=61) vs shared placebo (n=164): ALSFRS-R | -5.24 (0.59) | -5.51 (0.36) | 0.27 (0.68) | -1.07, 1.60 | 0.69 |
| 60 mg: SVC (% predicted) | -10.79 (1.99) | -8.53 (1.15) | -2.26 (2.29) | -6.75, 2.24 | 0.33 |

### eTable 3B — ERO/regimen-only repeated-measures results (p. 17)

| Contrast and endpoint | Active change | Regimen-placebo change | Difference (SE, if shown) | 95% CI | P |
|---|---:|---:|---:|---|---:|
| Pooled CNM-Au8 (n=120) vs regimen placebo (n=41): ALSFRS-R | -5.45 (0.44) | -5.39 (0.71) | -0.07 (0.83) | -1.71, 1.57 | 0.94 |
| Pooled: SVC (% predicted) | -9.57 (1.38) | -6.74 (2.29) | -2.83 (2.67) | -8.10, 2.44 | 0.29 |
| Pooled: plasma NfL (% change) | -2.3 | 7.9 | -9.5 | -18.0, 0 | 0.04 |
| Pooled: serum NfL (% change) | 0.4 | 26.8 | -26.4 | -50.3, -2.6 | 0.03 |
| CNM-Au8 30 mg (n=59): ALSFRS-R | -5.56 (0.60) | -5.39 (0.71) | -0.17 (0.93) | -2.00, 1.66 | 0.85 |
| 30 mg: SVC (% predicted) | -7.61 (1.86) | -6.74 (2.29) | -0.87 (2.94) | -6.69, 4.95 | 0.77 |
| 30 mg: plasma NfL (% change) | -1.3 | 7.9 | -8.5 | -18, 2 | 0.10 |
| 30 mg: serum NfL (% change) | 1.4 | 26.8 | -25.5 | -52.2, 1.3 | 0.06 |
| CNM-Au8 60 mg (n=61): ALSFRS-R | -5.35 (0.61) | -5.39 (0.71) | 0.04 (0.93) | -1.79, 1.87 | 0.97 |
| 60 mg: SVC (% predicted) | -11.53 (1.98) | -6.74 (2.29) | -4.79 (3.03) | -10.76, 1.19 | 0.12 |
| 60 mg: plasma NfL (% change) | -3.4 | 7.9 | -10.5 | -20, 0 | 0.04 |
| 60 mg: serum NfL (% change) | -0.5 | 26.8 | -27.4 | -45.1, -0.7 | 0.05 |

Footnote/labels: FAS includes shared placebos; ERO includes regimen-specific placebo only. ALSFRS-R, SVC, CI, SE, and NfL are defined in the source; `GMR – geometric mean ratio`. Serum/plasma NfL were modeled on a log scale then exponentiated to original scale. Models adjust for time since symptom onset, prebaseline ALSFRS-R slope, baseline edaravone, baseline riluzole, and their interactions with visit.

### eTable 4 — subgroup forest plot, pooled CNM-Au8 versus shared placebo (pp. 18-20)

Measure is ALSFRS-R slope (points/month) with displayed interval; difference is active minus placebo slope with 95% CI. The caption states that every subgroup CI crosses no difference. The P values displayed on selected subgroup headings are interaction/group-comparison P values as laid out in the source.

| Subgroup level | CNM-Au8 slope | Placebo slope | Difference (95% CI) | P if displayed |
|---|---|---|---|---:|
| All participants | -0.98 (-1.13,-0.82) | -1.01 (-1.13,-0.88) | 0.03 (-0.16,0.23) | — |
| Riluzole N / Y | -1.07 (-1.39,-0.75) / -0.95 (-1.12,-0.78) | -0.88 (-1.15,-0.61) / -1.05 (-1.19,-0.90) | -0.19 (-0.60,0.22) / 0.10 (-0.12,0.32) | 0.22 |
| Edaravone N / Y | -1.00 (-1.17,-0.83) / -0.91 (-1.22,-0.60) | -0.96 (-1.10,-0.81) / -1.17 (-1.43,-0.90) | -0.04 (-0.27,0.18) / 0.26 (-0.14,0.66) | 0.19 |
| Neither / riluzole only / edaravone only / both | -1.15 (-1.49,-0.81) / -0.94 (-1.14,-0.75) / -0.49 (-1.45,0.47) / -0.96 (-1.28,-0.64) | -0.82 (-1.10,-0.54) / -1.01 (-1.18,-0.83) / -1.38 (-2.27,-0.49) / -1.15 (-1.43,-0.88) | -0.33 (-0.77,0.10) / 0.06 (-0.20,0.32) / 0.89 (-0.42,2.20) / 0.19 (-0.23,0.61) | — |
| Age <65 / >=65 | -0.97 (-1.15,-0.80) / -0.95 (-1.23,-0.68) | -1.03 (-1.18,-0.88) / -0.95 (-1.19,-0.71) | 0.05 (-0.18,0.28) / 0.00 (-0.36,0.36) | 0.81 |
| Sex F / M | -0.98 (-1.22,-0.74) / -0.99 (-1.18,-0.80) | -1.10 (-1.33,-0.87) / -0.97 (-1.12,-0.81) | 0.12 (-0.21,0.45) / -0.02 (-0.27,0.22) | 0.50 |
| Race: White | -0.95 (-1.10,-0.80) | -1.01 (-1.14,-0.88) | 0.06 (-0.14,0.25) | — |
| Ethnicity: not Hispanic/Latino | -0.97 (-1.13,-0.82) | -1.01 (-1.14,-0.88) | 0.04 (-0.16,0.24) | — |
| Weight <56 / 56-<77 / 77-<150 kg | -1.39 (-2.02,-0.76) / -0.93 (-1.18,-0.68) / -0.95 (-1.14,-0.75) | -1.14 (-1.73,-0.55) / -1.04 (-1.25,-0.83) / -0.97 (-1.14,-0.80) | -0.25 (-1.11,0.60) / 0.11 (-0.21,0.43) / 0.03 (-0.23,0.28) | — |
| BMI <18.5 / 18.5-<25 / 25-<30 / 30-<40 / >=40 kg/m2 | -0.43 (-1.50,0.63) / -1.03 (-1.29,-0.78) / -0.95 (-1.18,-0.72) / -1.00 (-1.32,-0.68) / -0.35 (-1.26,0.56) | -1.40 (-2.30,-0.49) / -1.07 (-1.28,-0.85) / -0.93 (-1.13,-0.73) / -1.09 (-1.36,-0.82) / -0.15 (-1.05,0.76) | 0.96 (-0.43,2.35) / 0.03 (-0.30,0.36) / -0.02 (-0.33,0.28) / 0.09 (-0.33,0.50) / -0.21 (-1.49,1.07) | — |
| CKD stage <=1 / stage 2 | -0.99 (-1.16,-0.81) / -0.92 (-1.22,-0.63) | -1.04 (-1.20,-0.88) / -0.92 (-1.15,-0.69) | 0.05 (-0.18,0.29) / 0.00 (-0.38,0.37) | — |
| Onset <18 / >=18 months | -0.99 (-1.28,-0.69) / -0.96 (-1.18,-0.75) | -0.95 (-1.22,-0.68) / -1.04 (-1.23,-0.85) | -0.04 (-0.37,0.30) / 0.08 (-0.16,0.32) | 0.59 |
| Definite+<18 / not definite+<18 months | -1.05 (-1.40,-0.71) / -0.95 (-1.12,-0.77) | -1.25 (-1.65,-0.86) / -0.97 (-1.11,-0.84) | 0.20 (-0.29,0.69) / 0.03 (-0.19,0.24) | 0.53 |
| All ALSFRS-R items >=2 / >=1 item <2 | -0.99 (-1.31,-0.67) / -0.99 (-1.17,-0.81) | -0.88 (-1.11,-0.65) / -1.08 (-1.25,-0.91) | -0.11 (-0.50,0.27) / 0.09 (-0.13,0.32) | 0.38 |
| NfL <median / >=median | -0.85 (-1.07,-0.64) / -1.04 (-1.25,-0.83) | -0.95 (-1.12,-0.78) / -1.07 (-1.26,-0.88) | 0.10 (-0.17,0.36) / 0.03 (-0.25,0.31) | 0.74 |
| dFRS <median / >=median | -0.84 (-1.07,-0.62) / -1.16 (-1.41,-0.90) | -0.91 (-1.09,-0.72) / -1.14 (-1.36,-0.93) | 0.06 (-0.21,0.34) / -0.01 (-0.29,0.27) | 0.70 |

### eTable 5 — TEAEs (pp. 21-24)

Columns are pooled CNM-Au8 **N=120**, CNM-Au8 30 mg **N=59**, CNM-Au8 60 mg **N=61**, shared placebo **N=163**, and regimen-specific placebo **N=41**. Every cell is `participants n (percent), event count`; the title includes events with >=5% incidence in either group. Exact rows, in the above column order:

- **p. 21:** Any TEAE: 111 (92.5%), 723; 54 (91.5%), 293; 57 (93.4%), 430; 146 (89.6%), 889; 38 (92.7%), 228. Mild: 41 (34.2%), 500; 21 (35.6%), 205; 20 (32.8%), 295; 68 (41.7%), 673; 13 (31.7%), 151. Moderate: 44 (36.7%), 165; 22 (37.3%), 66; 24 (39.3%), 99; 53 (32.5%), 164; 15 (36.6%), 61. Severe: 24 (20%), 58; 11 (18.6%), 22; 13 (21.3%), 36; 25 (15.3%), 47; 10 (24.4%), 16. Serious TEAEs: 16 (13.3%), 20; 6 (10.2%), 9; 10 (16.4%), 11; 15 (9.2%), 21; 7 (17.1%), 12. Treatment-related serious TEAE: 0 (0.0%), 0; 0 (0.0%), 0; 0 (0.0%), 0; 2 (1.2%), 3; 1 (2.4%), 2. Deaths: 4 (3.3%), 4; 1 (1.7%), 1; 3 (4.9%), 3; 4 (2.5%), 4; 2 (4.9%), 2. Leading to study-drug withdrawal: 8 (6.7%), 8; 4 (6.8%), 4; 4 (6.6%), 4; 11 (6.7%), 17; 3 (7.3%), 4. Leading to study-drug interruption: 9 (7.5%), 15; 6 (10.2%), 11; 3 (4.9%), 4; 12 (7.4%), 24; 4 (9.8%), 6.
- **p. 22:** Leading to reduction: 3 (2.5%), 5; 0 (0.0%), 0; 3 (4.9%), 5; 5 (3.1%), 12; 1 (2.4%), 1. Fall: 26 (21.7%), 44; 13 (22.0%), 22; 13 (21.3%), 22; 43 (26.4%), 79; 13 (31.7%), 17. Muscular weakness: 24 (20.0%), 39; 10 (16.9%), 18; 14 (23.0%), 21; 45 (27.6%), 67; 12 (29.3%), 17. Diarrhoea: 23 (19.2%), 33; 9 (15.3%), 12; 14 (23.0%), 21; 12 (7.4%), 14; 4 (9.8%), 5. Nausea: 17 (14.2%), 21; 9 (15.3%), 10; 8 (13.1%), 11; 14 (8.6%), 16; 6 (14.6%), 8. Fatigue: 13 (10.8%), 17; 6 (10.2%), 8; 7 (11.5%), 9; 30 (18.4%), 33; 9 (22.0%), 9. Headache: 17 (14.2%), 26; 9 (15.3%), 17; 8 (13.1%), 9; 19 (11.7%), 23; 4 (9.8%), 6. Neuromyopathy: 14 (11.7%), 21; 6 (10.2%), 8; 8 (13.1%), 13; 22 (13.5%), 33; 6 (14.6%), 7. Constipation: 17 (14.2%), 19; 4 (6.8%), 4; 13 (21.3%), 15; 20 (12.3%), 24; 3 (7.3%), 4. Dyspnoea: 13 (10.8%), 14; 7 (11.9%), 8; 6 (9.8%), 6; 10 (6.1%), 11; 4 (9.8%), 5. Dysarthria: 15 (12.5%), 16; 9 (15.3%), 10; 6 (9.8%), 6; 11 (6.7%), 13; 2 (4.9%), 2. Dysphagia: 10 (8.3%), 10; 6 (10.2%), 6; 4 (6.6%), 4; 18 (11.0%), 22; 5 (12.2%), 6. Oedema peripheral: 7 (5.8%), 13; 2 (3.4%), 3; 5 (8.2%), 10; 12 (7.4%), 15; 4 (9.8%), 4. Tension headache: 7 (5.8%), 10; 1 (1.7%), 1; 6 (9.8%), 9; 10 (6.1%), 15; 4 (9.8%), 4.
- **p. 23:** Urinary tract infection: 10 (8.3%), 13; 4 (6.8%), 6; 6 (9.8%), 7; 10 (6.1%), 10; 1 (2.4%), 1. Arthralgia: 6 (5.0%), 12; 3 (5.1%), 8; 3 (4.9%), 4; 6 (3.7%), 6; 3 (7.3%), 3. Vomiting: 6 (5.0%), 9; 4 (6.8%), 5; 2 (3.3%), 4; 6 (3.7%), 6; 2 (4.9%), 2. Amyotrophic lateral sclerosis: 8 (6.7%), 10; 2 (3.4%), 2; 6 (9.8%), 8; 1 (0.6%), 1; 0 (0.0%), 0. Skin laceration: 6 (5.0%), 7; 2 (3.4%), 2; 4 (6.6%), 5; 4 (2.5%), 8; 2 (4.9%), 2. Cough: 7 (5.8%), 7; 1 (1.7%), 1; 6 (9.8%), 6; 4 (2.5%), 4; 1 (2.4%), 1. Decreased appetite: 5 (4.2%), 5; 2 (3.4%), 2; 3 (4.9%), 3; 12 (7.4%), 13; 3 (7.3%), 3. Insomnia: 5 (4.2%), 6; 0 (0.0%), 0; 5 (8.2%), 6; 2 (1.2%), 2; 2 (4.9%), 2. Salivary hypersecretion: 5 (4.2%), 6; 1 (1.7%), 1; 4 (6.6%), 5; 9 (5.5%), 9; 2 (4.9%), 2. Depression: 3 (2.5%), 3; 1 (1.7%), 1; 2 (3.3%), 2; 8 (4.9%), 8; 4 (9.8%), 4. Faeces discoloured: 7 (5.8%), 7; 1 (1.7%), 1; 6 (9.8%), 6; 0 (0.0%), 0; 0 (0.0%), 0. Post-traumatic pain: 4 (3.3%), 4; 2 (3.4%), 2; 2 (3.3%), 2; 6 (3.7%), 6; 3 (7.3%), 3. Weight decreased: 2 (1.7%), 2; 0 (0.0%), 0; 2 (3.3%), 2; 5 (3.1%), 5; 5 (12.2%), 5. Pain in extremity: 5 (4.2%), 7; 1 (1.7%), 1; 4 (6.6%), 6; 9 (5.5%), 10; 1 (2.4%), 1.
- **p. 24:** Pruritus: 6 (5.0%), 8; 0 (0.0%), 0; 6 (9.8%), 8; 4 (2.5%), 6; 0 (0.0%), 0. Dizziness: 4 (3.3%), 4; 3 (5.1%), 3; 1 (1.6%), 1; 10 (6.1%), 13; 2 (4.9%), 3. Increased upper airway secretion: 5 (4.2%), 6; 3 (5.1%), 4; 2 (3.3%), 2; 4 (2.5%), 4; 1 (2.4%), 1. Anxiety: 4 (3.3%), 4; 0 (0.0%), 0; 4 (6.6%), 4; 8 (4.9%), 8; 2 (4.9%), 2. COVID-19: 3 (2.5%), 3; 2 (3.4%), 2; 1 (1.6%), 1; 11 (6.7%), 11; 3 (7.3%), 3. Pulmonary embolism: 5 (4.2%), 5; 1 (1.7%), 1; 4 (6.6%), 4; 2 (1.2%), 2; 1 (2.4%), 1. Sinusitis: 6 (5.0%), 6; 4 (6.8%), 4; 2 (3.3%), 2; 0 (0.0%), 0; 0 (0.0%), 0. Asthenia: 4 (3.3%), 5; 0 (0.0%), 0; 4 (6.6%), 5; 2 (1.2%), 2; 1 (2.4%), 1. Back pain: 5 (4.2%), 6; 3 (5.1%), 4; 2 (3.3%), 2; 4 (2.5%), 10; 0 (0.0%), 0. Flatulence: 5 (4.2%), 5; 0 (0.0%), 0; 5 (8.2%), 5; 0 (0.0%), 0; 0 (0.0%), 0. Complication associated with device: 3 (2.5%), 4; 3 (5.1%), 4; 0 (0.0%), 0; 3 (1.8%), 3; 0 (0.0%), 0. Alanine aminotransferase increased: 3 (2.5%), 3; 3 (5.1%), 3; 0 (0.0%), 0; 2 (1.2%), 2; 0 (0.0%), 0. Aspartate aminotransferase increased: 3 (2.5%), 3; 3 (5.1%), 3; 0 (0.0%), 0; 1 (0.6%), 1; 0 (0.0%), 0.

### eFigure — serum NfL sensitivity analysis (p. 25)

Longitudinal samples are baseline, week 4 (plasma only), week 8 (serum only), week 16, and week 24. Exclude NfL <**4 pg/mL** or <**2%** of an individual's maximum, removing **one** baseline measure for **one** participant. Values use natural-log scale; plotted result is difference of least-square means. Back-transformed change: regimen placebo **+11.6%**, combined-dose CNM-Au8 **+0.8%**; placebo-versus-CNM-Au8 difference in change of geometric mean **+9.7%** (95% CI **-0.1% to +18.5%**, **P=0.051**).

- **p. 26:** rights/end matter only; explicitly no applicable quantitative result.

## DOC-005: nonauthor collaborators (fresh-direct extraction, pp. 1-6)

All six pages are a roster of the HEALEY ALS Platform Trial Study Group, persons, degrees, institution/location, and role/contribution. Fresh native and layout text were reviewed page by page. The only printed quantities are administrative page markers (`1 of 6` through `6 of 6`) and template/version `v 02-22`; no endpoints, study population totals, treatment denominators, results, statistics, units, formulas, tables of results, figures, sensitivity/subgroup results, or main-paper quantitative matching keys occur. **No-applicable result-relevant support unit: DOC-005 pp. 1-6.**

## DOC-006: data-sharing statement (fresh-direct extraction, p. 1)

Administrative content was completely reviewed. It identifies ClinicalTrials.gov IDs **NCT04297683** and **NCT04414345**, says data available: **No**, describes the sharing-review committee and temporary restrictions on placebo data, and states that analyses/design simulations were programmed in **SAS v9.4 or later**, **R v4.0 or later**, or **JAGS v4.3 or later**; code is not publicly available while the trial is ongoing. It contains no outcome estimate, denominator, result table/figure, statistical test result, effect measure, interval, P value, or result-relevant formula. **No-applicable result-relevant support unit: DOC-006 p. 1.**

## Mapping handoff counts and limitations

- **Source pages mapped:** DOC-004 26/26; DOC-005 6/6; DOC-006 1/1; total **33/33**.
- **Result-bearing tables/figures mapped:** eTables 1-5 and one eFigure (**6** labeled result displays); eMethods definitions and prespecified sensitivity/subgroup/statistical relationships mapped across pp. 2-13.
- **Administrative no-applicable pages:** DOC-004 pp. 1 and 26; DOC-005 pp. 1-6; DOC-006 p. 1 is data-sharing administration (software/version statements retained above).
- **Limitations/gaps:** none for assigned source-page coverage. Exact table values are source-PDF authoritative; native extraction of the multi-column TEAE table was corroborated against direct source-PDF text and fresh page renders. No OCR was needed.
