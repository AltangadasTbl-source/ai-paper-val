# Canonical inferential-statistical relationship inventory

**Pass status:** `PASS_1_COMPLETE` for S001-S071; `PASS_2_COMPLETE` for S001-S071. Detailed per-relationship records are in `checkers/statistical_pass_1.md` and `checkers/statistical_pass_2.md`.

**Evidence boundary:** normalized solely from the fresh maps `extraction/main_quantitative_evidence.md` and `extraction/support_quantitative_evidence.md`. This is a complete relationship inventory, not a candidate ledger or adjudication. Canonical order is deterministic: all `MS` records in ascending provisional-ID order, followed by all `PS` records in ascending provisional-ID order. Distinct records have not been merged; overlap is cross-referenced in the match-key field.

**Count:** 71 distinct mapped inferential-statistical relationships (`S001`-`S071`): 21 main-paper `MS` relationships and 50 support-source `PS` relationships.

## Field conventions

`Estimate/CI/P` reproduces the mapped printed statistical quantities, with `NR` meaning no numerical estimate was reported. `Rule` records the stated decision, correction, CI, or definitional rule. `Missing definitions` identifies what the mapping does not print or does not fully resolve; it is not a finding.

## Complete provisional-to-canonical mapping

| Provisional ID | Canonical ID | Source / PDF page |
|---|---|---|
| MS001 | S001 | DOC-001 p6 |
| MS002 | S002 | DOC-001 pp6-7 |
| MS003 | S003 | DOC-001 pp6-7 |
| MS004 | S004 | DOC-001 pp1,4,6-7 |
| MS005 | S005 | DOC-001 p4 |
| MS006 | S006 | DOC-001 p8 |
| MS007 | S007 | DOC-001 p8 |
| MS008 | S008 | DOC-001 pp1,6,8 |
| MS009 | S009 | DOC-001 p8 |
| MS010 | S010 | DOC-001 p8 |
| MS011 | S011 | DOC-001 pp6,8 |
| MS012 | S012 | DOC-001 p8 |
| MS013 | S013 | DOC-001 p8 |
| MS014 | S014 | DOC-001 p8 |
| MS015 | S015 | DOC-001 p8 |
| MS016 | S016 | DOC-001 pp1,7-8 |
| MS017 | S017 | DOC-001 pp7,9 |
| MS018 | S018 | DOC-001 p9 |
| MS019 | S019 | DOC-001 p9 |
| MS020 | S020 | DOC-001 p9 |
| MS021 | S021 | DOC-001 p9 |
| PS001 | S022 | DOC-002 pp37-38,108-109 |
| PS002 | S023 | DOC-002 pp92,110-112 |
| PS003 | S024 | DOC-002 pp93,112 |
| PS004 | S025 | DOC-002 p113 |
| PS005 | S026 | DOC-002 pp40-42,93-95 |
| PS006 | S027 | DOC-002 pp45-47,98-102 |
| PS007 | S028 | DOC-003 p2 |
| PS008 | S029 | DOC-003 p2 |
| PS009 | S030 | DOC-003 p2 |
| PS010 | S031 | DOC-003 p2 |
| PS011 | S032 | DOC-003 p2 |
| PS012 | S033 | DOC-003 pp3-4 |
| PS013 | S034 | DOC-003 pp3-4 |
| PS014 | S035 | DOC-003 pp3-4 |
| PS015 | S036 | DOC-003 pp3-4 |
| PS016 | S037 | DOC-003 pp3-4 |
| PS017 | S038 | DOC-003 pp3-4 |
| PS018 | S039 | DOC-003 pp3-4 |
| PS019 | S040 | DOC-003 pp3-4 |
| PS020 | S041 | DOC-003 pp3-4 |
| PS021 | S042 | DOC-003 pp3-4 |
| PS022 | S043 | DOC-003 pp3-4 |
| PS023 | S044 | DOC-003 pp3-4 |
| PS024 | S045 | DOC-003 pp3-4 |
| PS025 | S046 | DOC-003 pp3-4 |
| PS026 | S047 | DOC-003 pp3-4 |
| PS027 | S048 | DOC-003 pp3-4 |
| PS028 | S049 | DOC-003 pp3-4 |
| PS029 | S050 | DOC-003 pp3-4 |
| PS030 | S051 | DOC-003 pp3-4 |
| PS031 | S052 | DOC-003 pp3-4 |
| PS032 | S053 | DOC-003 pp3-4 |
| PS033 | S054 | DOC-003 pp3-4 |
| PS034 | S055 | DOC-003 pp3-4 |
| PS035 | S056 | DOC-003 pp3-4 |
| PS036 | S057 | DOC-003 pp3-4 |
| PS037 | S058 | DOC-003 pp3-4 |
| PS038 | S059 | DOC-003 pp3-4 |
| PS039 | S060 | DOC-003 pp3-4 |
| PS040 | S061 | DOC-003 pp3-4 |
| PS041 | S062 | DOC-003 pp3-4 |
| PS042 | S063 | DOC-003 pp3-4 |
| PS043 | S064 | DOC-003 pp3-4 |
| PS044 | S065 | DOC-003 pp3-4 |
| PS045 | S066 | DOC-003 pp3-4 |
| PS046 | S067 | DOC-003 pp3-4 |
| PS047 | S068 | DOC-003 pp3-4 |
| PS048 | S069 | DOC-003 pp3-4 |
| PS049 | S070 | DOC-003 pp3-4 |
| PS050 | S071 | DOC-003 p7 |

## Canonical relationship records

| Canonical / provisional | Estimate / CI / P | Test / model | Population; time; contrast; scale; direction | Rule | Cross-source match key | Missing definitions |
|---|---|---|---|---|---|---|
| S001 / MS001 | B=0.05; 95% CI −0.29 to 0.38; P=.79 | ITT mixed-effects analysis | randomized children; 36 mo; intervention−control; BMI kg/m²; positive I−C | CI contains 0 | `BMI36_ADJ`; PS011/S032 | covariance/adjustment terms not restated here |
| S002 / MS002 | B=−0.082; CI −0.246 to 0.082; P=.33 | model-estimated trajectory coefficient | ITT children; 36-mo trajectory; I−C linear effect; BMI/year; negative I−C growth difference | CI contains 0 | `BMI_LINEAR`; final-SAP PS002 | full coefficient parameterization not printed here |
| S003 / MS003 | B=0.032; CI −0.014 to 0.078; P=.18 | model-estimated trajectory coefficient | ITT children; 36-mo trajectory; I−C quadratic effect; BMI/year²; positive I−C acceleration difference | CI contains 0 | `BMI_QUADRATIC`; final-SAP PS002 | full coefficient parameterization not printed here |
| S004 / MS004 | joint LRT P=.39 | likelihood-ratio test, df=2 | ITT children; 36-mo trajectory; joint linear+quadratic intervention effects; BMI kg/m² | H0 jointly zero; .05 level | `BMI_JOINT_LRT`; PS003/S024; `PRIMARY_CONCLUSION` | LR statistic not printed |
| S005 / MS005 | NR | 2-level time-within-child mixed-effects regression; ML; unstructured covariance; MAR | randomized children; repeated BMI over 36 mo; assignment terms at intercept/linear/quadratic, age baseline covariates; BMI kg/m² | quadratic selected a priori; sex at intercept only | `BMI_PRIMARY_MODEL`; PS002/S023 | exact formula/coefficient names not printed in main map |
| S006 / MS006 | −88.5; CI −142.1 to −34.9; P=.001; BH=.003 | OLS adjusted baseline outcome, age, sex | dietary-data children; 12 mo; I−C; kcal/day; negative=fewer intervention kcal | CI excludes 0; 3-comparison BH correction | `ENERGY_12` | exact analytic denominator eligibility beyond printed data counts not stated |
| S007 / MS007 | −82.8; CI −144.6 to −21.1; P=.009; BH=.009 | OLS adjusted baseline outcome, age, sex | dietary-data children; 24 mo; I−C; kcal/day; negative=fewer intervention kcal | CI excludes 0; BH | `ENERGY_24` | same as S006 |
| S008 / MS008 | −99.4; CI −160.7 to −38.0; P=.002; BH=.003 | OLS adjusted baseline outcome, age, sex | dietary-data children; 36 mo; I−C; kcal/day; negative=fewer intervention kcal | CI excludes 0; BH; prose reports unsigned magnitude | `ENERGY_36` | exact analytic denominator eligibility beyond printed data counts not stated |
| S009 / MS009 | 12/24/36 mo: −0.3 [−1.2,0.5], P=.45/BH=.45; −0.6 [−1.6,0.3], .20/.45; −0.4 [−1.4,0.5], .36/.45 | OLS adjusted baseline outcome, age, sex | dietary-data children; 12/24/36 mo; I−C; percentage energy from fat; signed I−C | all CIs contain 0; BH across 3 comparisons | `FAT_12_24_36` | separate timepoint estimates grouped in source record; denominator eligibility not stated |
| S010 / MS010 | 12/24/36 mo: 0.1 [−0.9,1.2], .83/.83; −0.4 [−1.5,0.7], .45/.80; −0.3 [−1.4,0.7], .53/.80 | OLS adjusted baseline outcome, age, sex | dietary-data children; 12/24/36 mo; I−C; percentage energy from carbohydrate; signed I−C | all CIs contain 0; BH | `CARB_12_24_36` | separate timepoint estimates grouped; denominator eligibility not stated |
| S011 / MS011 | 12/24/36 mo: 0.2 [−0.3,0.8], .46/.46; 1.0 [0.4,1.5], .001/.003; 0.7 [0.2,1.3], .01/.02 | OLS adjusted baseline outcome, age, sex | dietary-data children; 12/24/36 mo; I−C; percentage energy from protein; positive=higher intervention percentage | 24/36 CIs exclude 0; BH | `PROTEIN_12_24_36` | separate timepoint estimates grouped; denominator eligibility not stated |
| S012 / MS012 | 12/24/36 mo: −2.2 [−12.8,8.4], .68/.77; −1.5 [−11.7,8.6], .77/.77; 3.6 [−6.5,13.6], .49/.77 | OLS adjusted baseline outcome, age, sex, wear time | accelerometry-data children; 12/24/36 mo; I−C; sedentary min/day; signed I−C | all CIs contain 0; BH | `SEDENTARY_12_24_36` | separate timepoint estimates grouped; valid-data rule not stated |
| S013 / MS013 | 12/24/36 mo: 1.7 [−2.7,6.1], .45/.68; −0.2 [−4.7,4.4], .95/.95; −1.7 [−6.0,2.5], .43/.68 | OLS adjusted baseline outcome, age, sex, wear time | accelerometry-data children; 12/24/36 mo; I−C; MVPA min/day; signed I−C | all CIs contain 0; BH | `MVPA_12_24_36` | separate timepoint estimates grouped; valid-data rule not stated |
| S014 / MS014 | RR=1.47; CI 1.22 to 1.76; P<.001; BH<.001 | Poisson robust-SE; adjusted baseline center use | parent-report children; 12 mo; I vs C; at-least-once center use; RR>1 favors higher intervention use | CI excludes 1; BH | `CENTER_12` | exact RR reference coding not restated |
| S015 / MS015 | RR=1.21; CI 1.02 to 1.44; P=.03; BH=.03 | Poisson robust-SE; adjusted baseline center use | parent-report children; 24 mo; I vs C; at-least-once center use; RR>1 favors higher intervention use | CI excludes 1; BH | `CENTER_24` | exact RR reference coding not restated |
| S016 / MS016 | RR=1.29; CI 1.08 to 1.53; P=.004; BH=.006 | Poisson robust-SE; adjusted baseline center use | parent-report children; 36 mo; I vs C; at-least-once center use; RR>1 favors higher intervention use | CI excludes 1; BH | `CENTER_36` | exact RR reference coding not restated |
| S017 / MS017 | RR=.51; CI .29 to .92; P=.02; BH=.10 | Poisson robust-SE; adjusted baseline child BMI, age, sex | BMI-observed children; 3 mo; I vs C; obesity ≥95th percentile; RR<1 lower intervention obesity risk | CI excludes 1; BH across 5 comparisons | `OBESITY_3`; PS050/S071 | exact RR coding/analytic denominator rule not stated |
| S018 / MS018 | RR=.70; CI .42 to 1.15; P=.16; BH=.27 | Poisson robust-SE; adjusted baseline child BMI, age, sex | BMI-observed children; 9 mo; I vs C; obesity ≥95th percentile; RR<1 lower intervention obesity risk | CI contains 1; BH | `OBESITY_9` | exact RR coding/analytic denominator rule not stated |
| S019 / MS019 | RR=.73; CI .48 to 1.10; P=.13; BH=.27 | Poisson robust-SE; adjusted baseline child BMI, age, sex | BMI-observed children; 12 mo; I vs C; obesity ≥95th percentile; RR<1 lower intervention obesity risk | CI contains 1; BH | `OBESITY_12` | exact RR coding/analytic denominator rule not stated |
| S020 / MS020 | RR=.92; CI .70 to 1.21; P=.57; BH=.71 | Poisson robust-SE; adjusted baseline child BMI, age, sex | BMI-observed children; 24 mo; I vs C; obesity ≥95th percentile; RR<1 lower intervention obesity risk | CI contains 1; BH | `OBESITY_24` | exact RR coding/analytic denominator rule not stated |
| S021 / MS021 | RR=.99; CI .80 to 1.22; P=.90; BH=.90 | Poisson robust-SE; adjusted baseline child BMI, age, sex | BMI-observed children; 36 mo; I vs C; obesity ≥95th percentile; RR<1 lower intervention obesity risk | CI contains 1; BH | `OBESITY_36` | exact RR coding/analytic denominator rule not stated |
| S022 / PS001 | NR | original-SAP quadratic mixed model: BMI=β0C+β1I+β2(age−X)C+β3(age−X)²C+β4(age−X)I+β5(age−X)²I+… | planned child BMI trajectory; enrollment-centered age; I=1/C=0; arm-specific quadratic effects | original H0/tests β5 differs from β3 at .05; no linear-term hypothesis | original-versus-final model; PS004/S025; `BMI_PRIMARY_MODEL` | residual/covariate terms abbreviated; no observed estimate |
| S023 / PS002 | NR | final-SAP ITT multilevel mixed-effects linear model; ML missing-data handling; Level 1 BMI within Level 2 child | children ages 3-5; dates through 36 mo; BMI kg/m²; baseline age and assignment predict intercept/linear/quadratic, gender intercept | β12 linear and β22 acceleration are primary intervention terms | exact main-paper primary-model match: MS005/S005, MS002-S003 | full formula/covariance structure not printed in support map |
| S024 / PS003 | LRT P not reported in SAP; H0 β12=β22=0; df=2 | likelihood-ratio test | final primary child-BMI model; joint intervention linear+quadratic effects | effectiveness if joint P<.05 | main result MS004/S004 (`BMI_JOINT_LRT`) | LR statistic and observed SAP-test P absent |
| S025 / PS004 | NR | final-plan amendment from β5-vs-β3 quadratic test to 2-df joint β12/β22 LRT | planned primary BMI analysis; baseline age/gender retained; ethnicity and gender×age removed | homogeneous variance primary; heterogeneous secondary | final-SAP PS002-PS003; original SAP PS001 | no observed sensitivity comparison/estimate |
| S026 / PS005 | NR | planned predicted-observed graphs; extra covariates; linear/restricted cubic splines; cluster-robust SE; MCAR/MAR, standard/constrained/weighted MI and pattern mixture | planned primary BMI robustness analyses | 4 knots; 100 imputations for stated MI approaches | `BMI_PRIMARY_MODEL`; no observed sensitivity estimates | exact implementation/result for each check absent |
| S027 / PS006 | NR | planned 36-mo mean-BMI difference; 2×2/logistic, multiple regression, interaction, social-network, genetic-score and count models | planned secondary endpoints and contrasts | planned only; no observed estimates supplied | possible later result matches, none asserted | specific models/estimands vary by listed endpoint and are not individually observed |
| S028 / PS007 | −0.01; CI −0.12 to 0.13; P=.83; BH=.83 | longitudinal mixed-effects regression | eTable 1 children; 3 mo; I−C; BMI kg/m²; negative lower intervention BMI | CI contains estimate and 0; five difference P values BH corrected | `child BMI, 3 months, adjusted mixed-model difference`; primary model S023 | model covariates not restated in eTable record |
| S029 / PS008 | −0.04; CI −0.20 to 0.12; P=.63; BH=.83 | longitudinal mixed-effects regression | eTable 1 children; 9 mo; I−C; BMI kg/m²; negative lower intervention BMI | CI contains estimate and 0; BH | `child BMI, 9 months, adjusted mixed-model difference`; S023 | model covariates not restated |
| S030 / PS009 | −0.05; CI −0.23 to 0.13; P=.62; BH=.83 | longitudinal mixed-effects regression | eTable 1 children; 12 mo; I−C; BMI kg/m²; negative lower intervention BMI | CI contains estimate and 0; BH | `child BMI, 12 months, adjusted mixed-model difference`; S023 | model covariates not restated |
| S031 / PS010 | −0.03; CI −0.28 to 0.22; P=.80; BH=.83 | longitudinal mixed-effects regression | eTable 1 children; 24 mo; I−C; BMI kg/m²; negative lower intervention BMI | CI contains estimate and 0; BH | `child BMI, 24 months, adjusted mixed-model difference`; S023 | model covariates not restated |
| S032 / PS011 | 0.05; CI −0.29 to 0.38; P=.79; BH=.83 | longitudinal mixed-effects regression | eTable 1 children; 36 mo; I−C; BMI kg/m²; positive higher intervention BMI | CI contains estimate and 0; BH | MS001/S001 `BMI36_ADJ` | model covariates not restated |
| S033 / PS012 | 0.105; CI −0.081 to 0.292; P=.27 | longitudinal mixed-effects moderation regression | valid eTable2 children; baseline age moderator; linear I effect; BMI difference/year; positive interaction | CI contains estimate and 0 | `eTable2 age moderation`; S023 | exact age centering and interaction parameterization absent |
| S034 / PS013 | −0.024; CI −0.076 to 0.028; P=.37 | longitudinal mixed-effects moderation regression | valid eTable2 children; baseline age moderator; quadratic I effect; BMI difference/year²; negative interaction | CI contains estimate and 0 | `eTable2 age moderation`; S023 | exact age centering and interaction parameterization absent |
| S035 / PS014 | −0.143; CI −0.379 to 0.093; P=.24 | longitudinal mixed-effects moderation regression | eTable2 male category; linear intervention effect; BMI difference/year; negative I effect | CI contains estimate and 0 | `eTable2 gender category`; eFigure 1 | reference/category coding beyond label not stated |
| S036 / PS015 | 0.076; CI 0.010 to 0.143; P=.02 | longitudinal mixed-effects moderation regression | eTable2 male category; quadratic intervention effect; BMI difference/year²; positive I acceleration effect | CI contains estimate; CI excludes 0 | `eTable2 gender category`; eFigure 1 | reference/category coding beyond label not stated |
| S037 / PS016 | −0.025; CI −0.253 to 0.203; P=.83 | longitudinal mixed-effects moderation regression | eTable2 female category; linear intervention effect; BMI difference/year; negative I effect | CI contains estimate and 0 | `eTable2 gender category`; eFigure 1 | reference/category coding beyond label not stated |
| S038 / PS017 | −0.009; CI −0.072 to 0.055; P=.79 | longitudinal mixed-effects moderation regression | eTable2 female category; quadratic intervention effect; BMI difference/year²; negative I acceleration effect | CI contains estimate and 0 | `eTable2 gender category`; eFigure 1 | reference/category coding beyond label not stated |
| S039 / PS018 | −0.013; CI −0.043 to 0.017; P=.40 | longitudinal mixed-effects moderation regression | valid adult baseline BMI, n=563; linear intervention interaction; BMI difference/year | CI contains estimate and 0 | `eTable2 adult BMI moderation` | adult-BMI centering/scaling beyond kg/m² absent |
| S040 / PS019 | 0.001; CI −0.007 to 0.009; P=.81 | longitudinal mixed-effects moderation regression | valid adult baseline BMI, n=563; quadratic intervention interaction; BMI difference/year² | CI contains estimate and 0 | `eTable2 adult BMI moderation` | adult-BMI centering/scaling beyond kg/m² absent |
| S041 / PS020 | −0.062; CI −0.234 to 0.110; P=.48 | longitudinal mixed-effects moderation regression | Hispanic parent ethnicity; linear intervention effect; BMI difference/year | CI contains estimate and 0 | `eTable2 ethnicity moderation` | ethnicity reference/category coding absent |
| S042 / PS021 | 0.024; CI −0.024 to 0.073; P=.33 | longitudinal mixed-effects moderation regression | Hispanic parent ethnicity; quadratic intervention effect; BMI difference/year² | CI contains estimate and 0 | `eTable2 ethnicity moderation` | ethnicity reference/category coding absent |
| S043 / PS022 | −0.279; CI −0.827 to 0.269; P=.32 | longitudinal mixed-effects moderation regression | non-Hispanic parent ethnicity; linear intervention effect; BMI difference/year | CI contains estimate and 0 | `eTable2 ethnicity moderation` | ethnicity reference/category coding absent |
| S044 / PS023 | 0.106; CI −0.046 to 0.258; P=.17 | longitudinal mixed-effects moderation regression | non-Hispanic parent ethnicity; quadratic intervention effect; BMI difference/year² | CI contains estimate and 0 | `eTable2 ethnicity moderation` | ethnicity reference/category coding absent |
| S045 / PS024 | −0.207; CI −0.649 to 0.235; P=.36 | longitudinal mixed-effects moderation regression | valid baseline diet recall, n=609; child energy-intake moderator; linear intervention interaction; BMI difference/year | CI contains estimate and 0 | `eTable2 energy moderation` | energy scaling/centering absent |
| S046 / PS025 | 0.163; CI 0.039 to 0.286; P=.01 | longitudinal mixed-effects moderation regression | valid baseline diet recall, n=609; child energy-intake moderator; quadratic intervention interaction; BMI difference/year² | CI contains estimate; CI excludes 0 | `eTable2 energy moderation` | energy scaling/centering absent |
| S047 / PS026 | −0.012; CI −0.044 to 0.019; P=.45 | longitudinal mixed-effects moderation regression | valid baseline diet recall, n=609; percent-energy-fat moderator; linear intervention interaction; BMI difference/year | CI contains estimate and 0 | `eTable2 fat moderation` | percent scale/centering absent |
| S048 / PS027 | 0.004; CI −0.005 to 0.013; P=.40 | longitudinal mixed-effects moderation regression | valid baseline diet recall, n=609; percent-energy-fat moderator; quadratic intervention interaction; BMI difference/year² | CI contains estimate and 0 | `eTable2 fat moderation` | percent scale/centering absent |
| S049 / PS028 | 0.003; CI −0.023 to 0.029; P=.81 | longitudinal mixed-effects moderation regression | valid baseline diet recall, n=609; percent-energy-carbohydrate moderator; linear intervention interaction; BMI difference/year | CI contains estimate and 0 | `eTable2 carbohydrate moderation` | percent scale/centering absent |
| S050 / PS029 | −0.002; CI −0.009 to 0.005; P=.57 | longitudinal mixed-effects moderation regression | valid baseline diet recall, n=609; percent-energy-carbohydrate moderator; quadratic intervention interaction; BMI difference/year² | CI contains estimate and 0 | `eTable2 carbohydrate moderation` | percent scale/centering absent |
| S051 / PS030 | 0.018; CI −0.033 to 0.068; P=.49 | longitudinal mixed-effects moderation regression | valid baseline diet recall, n=609; percent-energy-protein moderator; linear intervention interaction; BMI difference/year | CI contains estimate and 0 | `eTable2 protein moderation` | percent scale/centering absent |
| S052 / PS031 | −0.002; CI −0.016 to 0.013; P=.82 | longitudinal mixed-effects moderation regression | valid baseline diet recall, n=609; percent-energy-protein moderator; quadratic intervention interaction; BMI difference/year² | CI contains estimate and 0 | `eTable2 protein moderation` | percent scale/centering absent |
| S053 / PS032 | −0.015; CI −0.041 to 0.012; P=.28 | longitudinal mixed-effects moderation regression | valid baseline accelerometry, n=604; percent wear-time sedentary moderator; linear intervention interaction; BMI difference/year | CI contains estimate and 0 | `eTable2 sedentary moderation` | valid-day and centering rules absent |
| S054 / PS033 | 0.003; CI −0.004 to 0.010; P=.45 | longitudinal mixed-effects moderation regression | valid baseline accelerometry, n=604; percent wear-time sedentary moderator; quadratic intervention interaction; BMI difference/year² | CI contains estimate and 0 | `eTable2 sedentary moderation` | valid-day and centering rules absent |
| S055 / PS034 | 0.019; CI −0.035 to 0.073; P=.48 | longitudinal mixed-effects moderation regression | valid baseline accelerometry, n=604; percent wear-time MVPA moderator; linear intervention interaction; BMI difference/year | CI contains estimate and 0 | `eTable2 MVPA moderation` | valid-day and centering rules absent |
| S056 / PS035 | −0.006; CI −0.021 to 0.009; P=.48 | longitudinal mixed-effects moderation regression | valid baseline accelerometry, n=604; percent wear-time MVPA moderator; quadratic intervention interaction; BMI difference/year² | CI contains estimate and 0 | `eTable2 MVPA moderation` | valid-day and centering rules absent |
| S057 / PS036 | −0.001; CI −0.018 to 0.016; P=.88 | longitudinal mixed-effects moderation regression | valid baseline BMI percentile plus ≥1 valid nonbaseline BMI, n=589; linear intervention interaction; BMI difference/year | CI contains estimate and 0 | `eTable2 baseline BMI-percentile moderation` | percentile reference/centering absent |
| S058 / PS037 | −0.0005; CI −0.0051 to 0.0042; P=.85 | longitudinal mixed-effects moderation regression | valid baseline BMI percentile plus ≥1 valid nonbaseline BMI, n=589; quadratic intervention interaction; BMI difference/year² | CI contains estimate and 0 | `eTable2 baseline BMI-percentile moderation` | percentile reference/centering absent |
| S059 / PS038 | −0.167; CI −0.600 to 0.266; P=.45 | longitudinal mixed-effects moderation regression | valid birthweight, n=405; birthweight-kg moderator; linear intervention interaction; BMI difference/year | CI contains estimate and 0 | `eTable2 birthweight moderation` | birthweight centering absent |
| S060 / PS039 | 0.078; CI −0.045 to 0.201; P=.21 | longitudinal mixed-effects moderation regression | valid birthweight, n=405; birthweight-kg moderator; quadratic intervention interaction; BMI difference/year² | CI contains estimate and 0 | `eTable2 birthweight moderation` | birthweight centering absent |
| S061 / PS040 | −0.092; CI −0.308 to 0.124; P=.41 | longitudinal mixed-effects moderation regression | valid food-security status, n=606; food-secure category; linear intervention effect; BMI difference/year | CI contains estimate and 0 | `food security moderation`; eFigure 3 | reference/category coding absent |
| S062 / PS041 | 0.026; CI −0.034 to 0.087; P=.39 | longitudinal mixed-effects moderation regression | valid food-security status, n=606; food-secure category; quadratic intervention effect; BMI difference/year² | CI contains estimate and 0 | `food security moderation`; eFigure 3 | reference/category coding absent |
| S063 / PS042 | 0.106; CI −0.203 to 0.415; P=.50 | longitudinal mixed-effects moderation regression | valid food-security status, n=606; insecure-without-hunger category; linear intervention effect; BMI difference/year | CI contains estimate and 0 | `food security moderation`; eFigure 3 | reference/category coding absent |
| S064 / PS043 | −0.017; CI −0.104 to 0.069; P=.70 | longitudinal mixed-effects moderation regression | valid food-security status, n=606; insecure-without-hunger category; quadratic intervention effect; BMI difference/year² | CI contains estimate and 0 | `food security moderation`; eFigure 3 | reference/category coding absent |
| S065 / PS044 | −0.499; CI −0.954 to −0.044; P=.03 | longitudinal mixed-effects moderation regression | valid food-security status, n=606; insecure-with-hunger category; linear intervention effect; BMI difference/year | CI contains estimate; CI excludes 0 | `food security moderation`; eFigure 3 | reference/category coding absent |
| S066 / PS045 | 0.149; CI 0.023 to 0.275; P=.02 | longitudinal mixed-effects moderation regression | valid food-security status, n=606; insecure-with-hunger category; quadratic intervention effect; BMI difference/year² | CI contains estimate; CI excludes 0 | `food security moderation`; eFigure 3 | reference/category coding absent |
| S067 / PS046 | −0.054; CI −0.231 to 0.124; P=.55 | longitudinal mixed-effects moderation regression | Community Center A category; linear intervention effect; BMI difference/year | CI contains estimate and 0 | `eTable2 center moderation` | center reference/coding and denominator absent |
| S068 / PS047 | 0.025; CI −0.025 to 0.074; P=.33 | longitudinal mixed-effects moderation regression | Community Center A category; quadratic intervention effect; BMI difference/year² | CI contains estimate and 0 | `eTable2 center moderation` | center reference/coding and denominator absent |
| S069 / PS048 | −0.240; CI −0.672 to 0.192; P=.28 | longitudinal mixed-effects moderation regression | Community Center B category; linear intervention effect; BMI difference/year | CI contains estimate and 0 | `eTable2 center moderation` | center reference/coding and denominator absent |
| S070 / PS049 | 0.069; CI −0.052 to 0.190; P=.26 | longitudinal mixed-effects moderation regression | Community Center B category; quadratic intervention effect; BMI difference/year² | CI contains estimate and 0 | `eTable2 center moderation` | center reference/coding and denominator absent |
| S071 / PS050 | no printed risk-difference estimate, CI endpoint, denominator, or P | eFigure 2 estimated 3-month obesity-risk difference plot; dotted estimate and capped 95% CI | unspecified plotted population; 3 mo; intervention compared with control; risk difference in obesity; graphical direction not numerically recoverable | exact main-paper comparator/definition required before numerical reconciliation | eFigure 2; MS017/S017 `OBESITY_3` | model formula, numerical effect/CI/P, denominator, and plotted scale values absent |

## Normalization notes

- S001 and S032 are distinct representations of the same printed 36-month adjusted BMI difference and are retained separately because they arise from different mapped source records; their match is explicitly recorded.
- S004 and S024 are distinct: S004 is the reported main-paper joint-LRT result, while S024 is its final-SAP test definition and decision rule.
- S017 and S071 concern 3-month obesity but preserve different estimands/representations: S017 is a printed adjusted risk ratio and S071 is an unquantified plotted risk-difference representation.
- Grouped main-table records S009-S013 retain all their mapped timepoint estimates in one canonical relationship each, matching the mapper's provisional-record granularity.
