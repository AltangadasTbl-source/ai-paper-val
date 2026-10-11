# DOC-003 complete SAP and addendum quantitative/design map

Scope: DOC-003, `joi250066supp2_prod_1761597796.4701.pdf`, physical PDF pages 1–18, all inspected visually. Local relationship keys use prefix SAP; coordinator can assign global N/S IDs. No candidate discovery or diagnosis is performed here. All content is PLAN by prospective objectives, definitions, and planned analyses. The cover and repeated watermark say Final Report; no realized trial estimates, event counts, confidence intervals or P values occur in this document. Classification is by content rather than watermark.

## Evidence and tooling provenance

Read QUALITY_CONTROL_SCOPE.md, workflow_1_6_2/review_contract.md, current source coverage, source inventory, DOC-003 evidence asset inventory, and tooling record. Reused source-linked renders: `.ai_paper_validation/review_1_5_1/preprocessing/support_mapper/doc003/page-01.png` through `page-18.png`, each opened visually. Reusable native layout is blank and does not supply scientific evidence. Each page is readable; no fresh higher-resolution rendering needed. Fresh OCR is an auxiliary locator/transcription aid and was generated on CPU with Tesseract 5.5.0, English, PSM 3:

```bash
for n in $(seq -w 1 18); do
  tesseract .ai_paper_validation/review_1_5_1/preprocessing/support_mapper/doc003/page-$n.png .ai_paper_validation/review_1_6_2/preprocessing/sap_mapper/page-$n -l eng --psm 3
done
```

Completed outputs: `preprocessing/sap_mapper/page-01.txt` through `page-05.txt`, relative to review_1_6_2. The OCR loop terminated with exit 143 before completion; pages 6–18 were mapped visually and do not require OCR to close scientific coverage. Source images, not OCR, determine all entries below. No supplied or preexisting artifacts were changed. No workbook, cached values, formulas or CSV records are within this shard.

Every source link below is relative from this extraction artifact to package root, using `../../../joi250066supp2_prod_1761597796.4701.pdf#page=N`.

## Complete page coverage

| Physical page | Content role | Complete mapped content | Keys | Status |
|---|---|---|---|---|
| 1 | PLAN | Cover, September 27, 2024; study title Enhancement of Stroke Rehabilitation with Levodopa; internal DKF ID me16Engelter; background reference to meta-analysis of 6 RCTs, historical rather than current-trial result | SAP-001 | COMPLETE |
| 2 | PLAN | Primary and secondary objectives; 100/25 mg three times daily; FMMA at 3 months | SAP-002 | COMPLETE |
| 3 | PLAN | Randomized multicenter superiority design and entire Figure 1 visit/treatment flow | SAP-003 | COMPLETE |
| 4 | PLAN | FAS/mITT and mortality footnote; all 6 inclusion criteria and first 8 exclusion criteria | SAP-004, SAP-005 | COMPLETE |
| 5 | PLAN | Remaining 2 exclusion criteria; primary outcome scale, scoring and components; secondary outcome list and footnote | SAP-005, SAP-006, SAP-007 | COMPLETE |
| 6 | PLAN | Mobility threshold; harm outcomes and horizons; 5 intercurrent events; estimand framework and primary treatment attribute | SAP-007, SAP-008, SAP-009 | COMPLETE |
| 7 | PLAN | Primary estimand continuation, complete-case estimand II, FAS/death-imputation estimand III | SAP-009 | COMPLETE |
| 8 | PLAN | Composite/death win-ratio estimand and mortality footnote, hypothetical estimand, on-treatment I start | SAP-009, SAP-013 | COMPLETE |
| 9 | PLAN | On-treatment I continuation, on-treatment II, measurement-window estimand, independent DSMB safety assessment | SAP-009, SAP-015 | COMPLETE |
| 10 | PLAN | Baseline summaries, primary model/inference/diagnostics/footnote, all secondary-model rules | SAP-010, SAP-011 | COMPLETE |
| 11 | PLAN | Missing data, imputation/pooling, center interaction, secondary-estimand analysis and full win-ratio algorithm/decision/multiplicity footnote | SAP-012, SAP-013, SAP-014 | COMPLETE |
| 12 | PLAN | Remaining estimand models; all 7 subgroup definitions and interaction analysis; R version | SAP-014, SAP-016 | COMPLETE |
| 13 | PLAN | Signatures dated September 27, 2024 and Pocock 2012 reference; no additional applicable quantitative relationship | SAP-001 | COMPLETE; quantitative content not applicable beyond metadata |
| 14 | PLAN | Addendum Final Report from 04.10.2024; contents and page pointers; no numeric results | SAP-017 | COMPLETE; quantitative content not applicable beyond metadata |
| 15 | PLAN | Complete 7-row clinical subgroup table: dichotomies and prior direction hypotheses | SAP-016 | COMPLETE |
| 16 | PLAN | Biomarker subgroup table, all 6 biomarkers/panels, hypothesis directions and panel analytes | SAP-018 | COMPLETE |
| 17 | PLAN | Biomarker-table continuation; 2 genetic subgroup rows and other exploratory genetic analyses | SAP-018, SAP-019 | COMPLETE |
| 18 | PLAN | All 4 predefined analysis rows, positivity-dependence labels, direction hypotheses, dated signature | SAP-020 | COMPLETE |

18/18 unique pages mapped. Reusable-backed units 18; fresh-required units 0; OCR locator derivatives completed for pages 1–5; all 18 pages independently opened visually. No uninspected source unit or scientific coverage gap.

## Design, populations, eligibility and intervention

### SAP-001 — identity and historical material

[Page 1](../../../joi250066supp2_prod_1761597796.4701.pdf#page=1): cover dated September 27, 2024; Methods & Statistics, study title Enhancement of Stroke Rehabilitation with Levodopa, internal DKF ID me16Engelter, Document Status Final Report. Background refers to 6 historical RCTs and their differing populations, stroke types, dose/duration, follow-up and outcome measures; these are background statements, not ESTREL trial results or sample-size inputs. Footer on substantive SAP pages identifies September 20, 2024, revision 264857, numbered 1–13. [Page 13](../../../joi250066supp2_prod_1761597796.4701.pdf#page=13) sponsor-investigator and trial-statistician signatures dated 27.9.2024; reference is Pocock, Ariti, Collier & Wang 2012, win ratio, European Heart Journal 33(2):176–182. Reference is only mapped as supplied; no external source accessed.

### SAP-002 — objectives and contrast

[Page 2](../../../joi250066supp2_prod_1761597796.4701.pdf#page=2): levodopa/carbidopa 100/25 mg three times daily versus placebo, each added to standardized rehabilitation. Primary: improved functional recovery after 3 months in acute ischemic or hemorrhagic stroke, quantified using FMMA. Secondary objective: effects on survival and general health. Main-paper matching keys: randomized contrast, dose/frequency, primary FMMA and 3-month horizon.

### SAP-003 — study design and Figure 1

[Page 3](../../../joi250066supp2_prod_1761597796.4701.pdf#page=3): randomized multicenter superiority trial, 1:1 levodopa/carbidopa versus matching placebo. Figure 1 is a schedule, not participant-flow counts:

| Stage/visit | Printed time/window | Content |
|---|---|---|
| Prescreening | day −7 to 0 | Prior to baseline |
| Visit 1 | Baseline | Informed consent, screening, baseline clinical assessments, randomization |
| Dose escalation | day 1–day 6 | Treatment phase |
| Full dose | day 7–day 34 | Study treatment |
| Taper | day 35–day 39 | Tapering phase |
| Transition | day x during treatment | Transition to rehabilitation center |
| Visit 2 | 5 weeks ±7 days | End of treatment |
| Visit 3 | 3 months ±14 days | Primary outcome assessment; end of interventional phase |
| Visit 4 | 6 months ±20 days | Long-term clinical follow-up |
| Visit 5 | 12 months ±30 days | Long-term clinical follow-up |
| Visit 6 | 24 months ±30 days | Telephone follow-up, optional extension |
| Visit 7 | 36 months ±30 days | Telephone follow-up, optional extension |
| Visit 8 | 48 months ±30 days | Telephone follow-up, optional extension |
| Visit 9 | 60 months ±30 days | Telephone follow-up, optional extension |

Interventional phase bracket covers baseline to primary assessment; observational clinical phase covers visits 4–5; optional extended telephone phase covers visits 6–9. Main matching keys: allocation, study superiority status, intervention duration, 5-week treatment visit, 3/6/12-month outcome visits and outcome window.

### SAP-004 — analysis sets and death handling

[Page 4](../../../joi250066supp2_prod_1761597796.4701.pdf#page=4), section 3.2:

- Full analysis set FAS: all randomized patients.
- Missing FMMA in patients surviving to Visit 3: multiple imputation by chained equations, section 6.
- Patients who died before Visit 3: not imputed except Treatment policy strategy III.
- Footnote 1: deceased before Visit 3 remain in FAS but contribute only to Treatment policy III and composite strategy.
- Modified intention-to-treat mITT: all FAS patients with complete FMMA at Visit 3.

These set definitions must be carried together with estimand-specific inclusion rather than using FAS alone as a denominator definition. Main matching keys: randomized set, primary analysis population, survivor imputation, complete case, death sensitivity/composite analyses.

### SAP-005 — every eligibility criterion

[Pages 4–5](../../../joi250066supp2_prod_1761597796.4701.pdf#page=4), sections 3.3–3.4. Inclusion, item by item:

1. Acute ischemic or hemorrhagic stroke ≤7 days before randomization; hemorrhagic means intracerebral hemorrhage excluding subarachnoid hemorrhage and cerebral venous sinus thrombosis.
2. Clinically meaningful hemiparesis: total ≥3 points from NIH stroke scale motor arm, motor leg, limb ataxia; distal arm paresis equivalent to one of those items.
3. Randomization ≥24 hours after thrombolysis or thrombectomy.
4. In-hospital rehabilitation required.
5. Capable of standardized rehabilitation participation.
6. Informed consent from patient or next of kin.

Exclusion, item by item:

1. Age <18 years.
2. Parkinson disease.
3. Levodopa mandatory under treating physician judgment.
4. Inability/unwillingness to follow procedures including drug intake orally, nasogastric or percutaneous endoscopic gastrostomy tube.
5. Severe aphasia, unable to follow two-stage commands.
6. Previously dependent in basal activities of daily living, prestroke mRS >3.
7. Preexisting hemiparesis.
8. Hypersensitivity to levodopa/carbidopa or other contraindications under appended product-characteristic summary.
9. Pregnancy, breastfeeding or intended pregnancy; women of childbearing age must have pregnancy test for eligibility (p5).
10. Lack of safe contraception: unwilling/not using medically reliable method for whole study, with oral/injectable/implantable contraception, intrauterine device or other investigator-approved reliable method described. Surgical sterilization/hysterectomy or postmenopause >2 years means not childbearing potential (p5).

Eligibility definitions map target population and NIH/mRS thresholds; not realized analysis counts.

## Outcome hierarchy, scales, time points and harm

### SAP-006 — primary endpoint scale

[Page 5](../../../joi250066supp2_prod_1761597796.4701.pdf#page=5), section 4.1: final FMMA score at Visit 3, rather than an unadjusted change-score outcome. Stroke-specific motor impairment index. Item scale: 0 cannot perform, 1 performs partially, 2 performs fully, a 3-point ordinal scale. Total 0 (no movements) to 100 (normal movements): upper extremity 66, lower extremity 34. All assessment by trained outcome assessor. Section 5.2 footnote on p10 states baseline-adjusted final-score difference is equivalent to baseline-adjusted between-arm difference in change from baseline to Visit 3. Main matching keys: FMMA total, 3 months, 0–100, upper/lower components and adjusted final/change contrast.

### SAP-007 — every secondary outcome and horizon

[Pages 5–6](../../../joi250066supp2_prod_1761597796.4701.pdf#page=5), section 4.2: secondary outcomes assessed at Visit 2 end treatment, Visit 3 end interventional phase, Visits 4–5 long-term follow-up, except explicit harm horizons. No separate designation as key secondary occurs in this SAP.

| Outcome | Definition/status and horizon |
|---|---|
| FMMA total | Secondary at Visits 2, 4, 5; Visit 3 total is primary per footnote 2. Printed list ends with “Visit 5 months”; visit schedule establishes Visit 5 at 12 months. |
| FMMA upper extremity | Separate secondary score, 66-point component |
| FMMA lower extremity | Separate secondary score, 34-point component |
| FMMA affected side | Secondary; bilateral pathology excluded from this analysis per p10 |
| Stroke severity | NIH Stroke Scale Score |
| Disability/dependence | Modified Rankin Scale mRS |
| Patient-reported outcome | PROMIS-29 |
| Patient-reported outcome | PROMIS 10, 10-question short form |
| Patient assessment | Relevance of motor improvement; no numeric scale specified here |
| Mobility | Rivermead Mobility Index; continuous plus binary ability to walk independently, score ≥7, for comparison with DARS |
| Potential harm | All-cause mortality through Visit 5 |
| Potential harm | Recurrent stroke through Visit 5 |
| Potential harm | Serious adverse events through Visit 3 |
| Potential harm | Nonserious adverse events possibly related to IMP through Visit 3 |

Main matching keys: each endpoint status, score/component, horizon, independent-walking ≥7 threshold, harm definitions and mortality/recurrent-stroke horizons.

## Estimands and intercurrent events

### SAP-008 — full intercurrent-event catalogue

[Page 6](../../../joi250066supp2_prod_1761597796.4701.pdf#page=6), section 4.3: estimand has five attributes: treatment, population, endpoint, population-level summary, handling of intercurrent events. Five listed events:

(a) Death before Visit 3.

(b) SAE causing motor-impairing event before Visit 3, e.g., recurrent stroke, fracture, comparable complication.

(c) Intake <80% of study medication.

(d) At least one week with <5 rehabilitation sessions/week in a 4-week period.

(e) Visit 3 outside its window.

Primary analysis treatment policy; other estimands supportive only. Main matching keys: death, SAE, medication adherence 80%, rehabilitation 5/week over 4 weeks, primary visit window.

### SAP-009 — all eight estimands and each attribute

[Pages 6–9](../../../joi250066supp2_prod_1761597796.4701.pdf#page=6). Each estimand uses levodopa plus standardized rehabilitation versus placebo plus standardized rehabilitation. Endpoint ordinarily FMMA at Visit 3; summary ordinarily between-treatment-arm mean difference; randomized assignment is retained. The table spells out all departures.

| Section/name | Population | Endpoint | Population summary | Intercurrent-event handling |
|---|---|---|---|---|
| 4.3.1 Primary treatment policy | FAS as 3.2; survivor primary FMMA analysis as mortality footnote states | Visit 3 FMMA | Mean difference between arms | Analyze by randomization irrespective of events; survivor missing FMMA imputed under 3.2/6 |
| 4.3.2 Treatment policy II, complete case | mITT, complete Visit 3 FMMA | Visit 3 FMMA | Mean difference | Randomized assignment irrespective of events; complete observed endpoint |
| 4.3.3 Treatment policy III, FAS including deaths | FAS including deaths before Visit 3 | Visit 3 FMMA | Mean difference | Randomized assignment irrespective of events; FMMA for deceased also imputed |
| 4.3.4 Composite using win-ratios | FAS including deaths; footnote 3 says no FMMA needed for deceased | Death and Visit 3 FMMA | Printed “difference in win-ratio” at Visit 3 | Randomized assignment irrespective of events; death worst possible outcome; unmatched win-ratio algorithm on p11 |
| 4.3.5 Hypothetical | FAS minus participants with event (b) | Visit 3 FMMA | Mean difference | Exclude motor-impairing SAE before Visit 3; retain randomized assignment |
| 4.3.6 On treatment / While on treatment | FAS minus participants with event (c) | Visit 3 FMMA | Mean difference | Exclude intake <80%; retain randomized assignment |
| 4.3.7 On treatment II / While on treatment II | FAS minus participants with event (d) | Visit 3 FMMA | Mean difference | Exclude inadequate documented rehabilitation; retain randomized assignment |
| 4.3.8 Measured according to protocol / While measured according to protocol | FAS minus participants with event (e) | Visit 3 FMMA | Mean difference | Exclude assessments outside predefined Visit 3 window; retain randomized assignment |

Populations retain 3.2 death-handling context except death-inclusive III and composite. Blue text in source marks departures from primary estimand. Section 7.1 p11 prints “Treatment policy strategy III, complete case analysis” as the model heading; section 4.3.3 definition above explicitly specifies imputation of deceased patients. Both labels are transcribed without reconciliation or diagnosis. Main matching keys: complete case, death-imputation, composite, SAE exclusion, ≥80% medication adherence, rehabilitation adherence, outcome-window exclusion and sensitivity status.

## Models, inference and missing data

### SAP-010 — descriptive and primary analysis

[Page 10](../../../joi250066supp2_prod_1761597796.4701.pdf#page=10), sections 5.1–5.2:

- Demographic/baseline summaries in FAS and mITT, stratified by treatment arm.
- Categorical data frequencies/percentages; continuous mean/SD; nonnormal continuous median/IQR.
- Footnote 4 considers extra baseline tables restricted to the model-used patients for an estimand if its result deviates from main estimand.
- Primary FMMA Visit 3 modeled using linear model with baseline FMMA covariate and two-level treatment factor levodopa versus placebo as variable of interest.
- Treatment effect presented with P value and 95% CI; interpreted as FMMA mean difference levodopa versus placebo at Visit 3, adjusted for baseline.
- Footnote 5: adjusted final-score difference equivalent to adjusted difference in change from baseline to Visit 3.
- Model assumptions checked including residuals and leverage; data transformation considered if assumptions violated.
- Alpha 0.05, two-sided.
- Primary model specifies baseline FMMA and treatment; center and treatment×center are assigned separately to exploratory heterogeneity analysis p11.

Main matching keys: baseline-adjusted linear model, factor/reference contrast, mean difference, 95% CI, two-sided .05 and transformation/diagnostic provisions.

### SAP-011 — all secondary analysis rules

[Page 10](../../../joi250066supp2_prod_1761597796.4701.pdf#page=10), section 5.3:

- All secondary outcomes except potential harm use data-type appropriate regression, adjusted for baseline when available.
- Binary: logistic regression, GLM logit link with binomial distribution.
- Continuous: linear model.
- Ordinal: ordinal logistic regression.
- Diagnostics as primary; severe assumption violations/high-leverage outliers may prompt transformations, nonparametric tests or robust regression.
- Potential harm summarized by treatment arm.
- All secondary outcomes also descriptive tables/graphs, possibly separate publications if useful.
- Primary estimand applies to every secondary analysis; FMMA affected side excludes bilateral pathology.

Main matching keys: binary/ordinal/continuous model identities, baseline adjustment, harm descriptive analyses and affected-side exclusions.

### SAP-012 — missing-data and pooling specification

[Page 11](../../../joi250066supp2_prod_1761597796.4701.pdf#page=11), section 6:

- Number missing reported for every variable.
- 100 multiple imputations using chained equations.
- Imputation-generated values displayed in plots.
- Fit analysis model to each imputed data set.
- Combine estimates and variances using Rubin's rules for single parameter estimate/variance across imputations.
- Missing secondary outcomes imputed like primary analysis.
- Potential-harm outcomes not imputed.
- Mortality rules from 3.2/4.3 govern which primary/sensitivity values are imputed.

No list of imputation predictors, seed or imputation-specific distributions is supplied on these pages. This is an extraction statement only. Main matching keys: 100 MICE imputations, Rubin pooling, survivor versus deceased imputation, harm not imputed.

### SAP-013 — win-ratio calculation, hierarchy and decision

[Page 11](../../../joi250066supp2_prod_1761597796.4701.pdf#page=11), section 7.1 and footnote 6:

- Composite variable strategy uses unmatched Pocock et al 2012 approach.
- Every levodopa patient compared with every placebo patient.
- Rule 1: survivor to Visit 3 wins over death before Visit 3.
- Rule 2: if both die before Visit 3, longer survival wins.
- Rule 3: printed “If both patients survive up to end of study,” higher FMMA wins. Endpoint definition in 4.3.4 is FMMA Visit 3; both printed timing statements retained.
- Win ratio = number of comparisons won by treatment divided by number won by placebo.
- 95% CI estimated using 1000 bootstrap samples following cited statistical appendix.
- Repeat analysis on each imputed data set.
- CI excluding 1 taken as evidence of between-arm difference and discussed similarly to conventional sensitivity result P<0.05.
- Footnote 6: all analyses in section sensitivity analyses, no correction for multiple testing; discuss in context of primary analysis, not standalone evidence.

No separate tie algorithm or explicit cross-imputation bootstrap-CI pooling formula printed. Main matching keys: death/FMMA composite, pairwise hierarchy, unmatched win ratio, 1000 bootstrap, CI null 1, multiplicity/supportive status.

### SAP-014 — secondary-estimand, center and subgroup analysis

[Pages 11–12](../../../joi250066supp2_prod_1761597796.4701.pdf#page=11), section 7:

- Exploratory treatment heterogeneity across centers: add center and treatment×center to main model; plot stratified by center or groups of centers.
- Same primary-estimand model for policy II and policy III under section 7.1 headings, hypothetical, while on treatment I/II, and while measured according to protocol.
- Composite strategy method separately specified SAP-013.
- Each subgroup uses primary estimand, same main model plus subgroup variable and subgroup×treatment additional fixed effect.
- Subgroups displayed as forest plot.
- Underlying subgroup hypotheses prespecified with ICEMAN before subgroup analysis and recorded in addendum.
- Analyses performed in R 4.3.1 or higher.

Main matching keys: exploratory center interactions, same-model sensitivity analyses, subgroup interaction terms/forest plot, subgroup hypothesis/addendum, software.

### SAP-015 — safety oversight and absent design inputs

[Page 9](../../../joi250066supp2_prod_1761597796.4701.pdf#page=9), section 4.4: endpoints for potential harm considered important; DSMB investigates safety independently of results presented in this document. Main result considered potentially high impact for stroke management. Across all 18 pages no numerical power, sample-size calculation, anticipated effect/SD, loss inflation, noninferiority/equivalence margin, interim efficacy boundary, quantitative stopping rule or randomized stratum definition appears. Therefore those inputs cannot be extracted from this SAP shard; protocol shard may supply them. This is a complete-scope absence record rather than candidate reasoning.

## Addendum: complete subgroup and predefined-analysis tables

### SAP-016 — all seven clinical subgroup rows

[Page 12](../../../joi250066supp2_prod_1761597796.4701.pdf#page=12) lists groups; [page 15](../../../joi250066supp2_prod_1761597796.4701.pdf#page=15) provides table of dichotomization and prior hypothesized effect modification:

| Subgroup | Dichotomy | Prior direction/magnitude hypothesis |
|---|---|---|
| Age | <median vs ≥median | Younger may obtain more pronounced levodopa motor-learning enhancement than older, attributed to neuroplasticity/learning capacity |
| Sex | Male vs female | No expected difference in direction or magnitude of levodopa effect |
| Selective hand/wrist movement at baseline | NIHSS Distal Motor Function subscore 0 vs >0 | No expected levodopa effect difference with/without selective movement |
| Cortical dysfunction | Sum of NIHSS Best Language, Extinction and Inattention, Visual subscores 0 vs >0 | No expected treatment effect difference; dysfunction may affect learning and lead to poorer recovery |
| Baseline SSRI use | Yes vs no | No expected levodopa effect difference |
| Stroke type | Acute ischemic vs intracerebral hemorrhage | No expected levodopa effect difference |
| Baseline FMMA severity | <median vs ≥median | No expected levodopa effect difference across severity levels |

Page 12 baseline FMMA subgroup has no printed cutoff; page 15 supplies median split. Median numeric values not supplied in this document. Main matching keys: all seven subgroup definitions and predicted younger direction; separate 0/>0 selective-movement/cortical cutoffs; baseline-treatment and stroke-type labels.

### SAP-017 — addendum identity

[Page 14](../../../joi250066supp2_prod_1761597796.4701.pdf#page=14): Addendum to Methods & Statistics, Version Final Report from 04.10.2024. Contents references clinical ICEMAN subgroup hypotheses p2, biomarker hypotheses p4, genetic subgroup p5, predefined analyses p6. Physical addendum pages are 14–18; contents numbering is retained as supplied, not used to reassign PDF page locators. [Page 18](../../../joi250066supp2_prod_1761597796.4701.pdf#page=18) signature dated Basel 4.10.2024. All addendum entries are hypotheses and analyses to be performed, hence PLAN.

### SAP-018 — every biomarker table entry

[Pages 16–17](../../../joi250066supp2_prod_1761597796.4701.pdf#page=16), heading Prespecified Hypotheses of Biomarker Subgroups with ICEMAN. Column named Dichotomization lists biomarker names rather than numerical cutpoints. Each hypothesis anticipates concentration-associated differences in direction or magnitude of stroke recovery, while not anticipating levodopa treatment-effect difference between high and low concentrations.

| Category | Biomarker/panel | Printed concentration hypothesis |
|---|---|---|
| Neuroaxonal injury | Neurofilament light chain NfL | Recovery varies with NfL concentration; no levodopa effect modification high vs low |
| Neuroaxonal injury | Tau | Recovery varies with Tau concentration; no levodopa effect modification high vs low |
| Myocardial injury/dysfunction | Hs-troponinT | Recovery varies with Hs-troponinT; no levodopa effect modification high vs low |
| Myocardial injury/dysfunction | NT-pro-BNP | Recovery varies with NT-pro-BNP; no levodopa effect modification high vs low |
| Aging processes of immune system | GDF-15 | Recovery varies with GDF-15; no levodopa effect modification high vs low |
| Aging processes of immune system | Senescence-associated secretory phenotype panel | Recovery varies with panel; no levodopa effect modification high vs low; statement continues on p17 |

Panel contains exactly the listed analytes: IL-1b, IL-6, IL-10, MCP-1, TNFa, MMP-1, osteopontin. Numeric concentration thresholds, units, standardized panel score and separate fitted-model specification are not printed here. Main matching keys: biomarker exploratory/prespecified subgroup status and all names/threshold availability.

### SAP-019 — every genetic table entry

[Page 17](../../../joi250066supp2_prod_1761597796.4701.pdf#page=17), Prespecified Hypotheses of Genetic Subgroup Analyses with ICEMAN:

| SNP/label | Dichotomy | Hypothesis |
|---|---|---|
| Rs1842681 | Homozygous/heterozygous | Risk allele of SNP rs1842681 might contribute to unfavorable stroke recovery |
| ApoE | Homozygous/heterozygous | ApoE risk allele might contribute to unfavorable recovery among hemorrhagic stroke patients |

All other planned genetic analyses, including levodopa score, copy number variation and SNPs, exploratory because evidence on genetics in stroke recovery is limited. Specific risk-allele identity, numeric score definition, genetic model or multiplicity rule for this table not printed. Main matching keys: listed hypotheses, hemorrhagic-only ApoE hypothesis, exploratory status of other genetic analyses.

### SAP-020 — all four predefined analysis rows

[Page 18](../../../joi250066supp2_prod_1761597796.4701.pdf#page=18), Predefined Analyses. Table columns: Planned Analyses; Dependent on a positive result; A priori hypothesized direction of effect modification.

| Planned analysis | Printed dependence | Full analysis/hypothesis content |
|---|---|---|
| ESTREL participants versus Swiss Stroke Registry patients | NO | Compare participant outcomes to similarly affected national/Swiss registry nonparticipants; hypothesize better recovery among ESTREL participants |
| Type/amount of rehabilitation with and without levodopa | YES/NO | Investigate type/amount impact on motor recovery and whether levodopa effect depends on type/amount; greater motor rehabilitation built on motor-learning principles expected to improve recovery; levodopa effect hypothesized influenced by extent incorporating these principles |
| Levodopa association with poststroke fatigue | Blank | Motivational properties may be associated with reduced poststroke fatigue |
| Levodopa association with poststroke depression | Blank | Motivational properties may be associated with reduced poststroke depression |

No realized effects or numeric outcomes in this table. Blank dependence cells are retained rather than assigned an inferred status. Main matching keys: predefined registry/rehabilitation/fatigue/depression analyses and their dependence/status statements.

## Mapping summary and limits

Twenty local keyed relationship groups SAP-001–SAP-020 cover every assigned page and every table/figure item. Scientific analysis relationships are SAP-002–SAP-004, SAP-006–SAP-016, SAP-018–SAP-020; metadata/eligibility are separately retained where they define matching context. No realized inferential results occur. All pages reviewed, including signatures/contents and administrative material. No candidate IDs, findings, screening or dispositions supplied. No old AI conclusions read. Limits: image-only source requires visual reading/OCR locator; no unreadable source content; no scientific coverage gaps. Inputs not present within these 18 pages are explicitly named above and must not be imported from outside this assigned shard.
