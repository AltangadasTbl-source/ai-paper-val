# Support Quantitative Evidence Map

## Assignment and evidence handling

- **Assigned direct-source scope:** DOC-002, `joi180151supp1_prod.pdf`, PDF pp. 1-7; and DOC-003, `joi180151supp2_prod.pdf`, PDF pp. 1-29.
- **Reusable locators:** `.ai_paper_validation/rights_screen/joi180151supp1_prod.txt` and `.ai_paper_validation/rights_screen/joi180151supp2_prod.txt`, using their form-feed page boundaries.
- **Direct inspection:** DOC-003 PDF pp. 7-26 were rendered at 180 dpi to `.ai_paper_validation/review_1_3_1/preprocessing/support_pages/doc003-07.png` through `doc003-26.png` and visually inspected. Targeted CPU Tesseract was additionally used on pp. 22-26 only to assist transcription of embedded forest-plot text; every recorded forest-plot value below was checked against the direct page render. The reusable source artifacts were not modified.
- **Purpose:** this is a relationship-ready extraction, not a consistency judgment. It records printed definitions, values, labels, populations, contrasts, and exact pages. No candidate is diagnosed here.
- **Matching convention:** `A` means aspirin/experimental; `N` means no aspirin/control. Bracketed intervals in eFigure 4 are printed 95% confidence intervals. `fx wt/rx wt` means the displayed fixed-effect/random-effects percentage weights.

## DOC-002 — Meta-analysis protocol (PDF pp. 1-7)

### Protocol identity and quantitative scope

| Local record | PDF page | Relationship-ready evidence |
|---|---:|---|
| P-001 | 1 | Protocol supplement for the same Zheng and Roddick aspirin primary-prevention meta-analysis; this supplies prospective definitions and analysis rules, not outcome results. |
| P-002 | 2 | Aim: cardiovascular efficacy and bleeding risk of aspirin in primary-prevention populations. Population: participants without cardiovascular disease. Intervention: aspirin, any dose. Comparator: placebo or no aspirin. |
| P-003 | 2 | Primary cardiovascular composite: cardiovascular mortality, non-fatal myocardial infarction, and non-fatal stroke. Secondary cardiovascular outcomes: all-cause mortality, cardiovascular mortality, all myocardial infarction, all stroke, and all ischaemic stroke. Primary safety outcome: major bleeding. Secondary safety outcomes: intracranial haemorrhage and major gastrointestinal bleeding. Exploratory cancer outcomes: incident cancer and cancer mortality. These names are the main-paper/supplement matching keys. |
| P-004 | 3 | Original search update: earlier review search date January 6, 2015; update planned from January 1, 2015 through the search date. The same page also says databases from inception through August 31, 2018. MEDLINE, Embase, and CENTRAL were specified. |
| P-005 | 3 | Screening assignment: two authors divide the list evenly without overlap at title/abstract screening; later review by both authors in parallel and independently. |
| P-006 | 4 | Inclusion thresholds: randomized clinical trial; participants without known cardiovascular disease; aspirin vs placebo/no treatment; follow-up at least 12 months; more than 1000 participants; at least one prespecified cardiovascular or bleeding outcome; English language. Secondary analyses could contribute when the original trial met these criteria. |
| P-007 | 5 | Two authors independently extract data. Quantitative extraction fields include follow-up duration; demographics and percentages; event counts in treatment/control; reported RR or HR; 95% confidence limits; and P values for all prespecified cardiovascular and bleeding outcomes. |

### Prespecified analysis rules

| Local record | PDF page | Relationship-ready evidence |
|---|---:|---|
| P-008 | 6 | Primary analysis: Bayesian hierarchical pairwise meta-analysis in GeMTC/R 3.4.1. Fixed or random effects selected by the smallest DIC. MCMC used. Results expressed as HR with 95% CrI, aspirin vs no aspirin. |
| P-009 | 6 | When a trial did not report HRs, event counts, total number, and follow-up duration were to enter a Poisson-likelihood/log-link model to generate HR estimates. |
| P-010 | 6 | Frequentist pairwise meta-analysis was to generate RRs for absolute-risk calculations. Printed protocol rule: multiply the RR and its 95% limits by the placebo event rate, then subtract from placebo risk. Negative ARD favors aspirin; positive ARD favors no aspirin. |
| P-011 | 6 | Prespecified sensitivity exclusions: open-label studies; studies randomizing to daily aspirin doses greater than 100 mg; and studies published before 2000. |
| P-012 | 6 | Additional frequentist cardiovascular and bleeding analyses were to be supplied in the supplement. Frequentist significance rule: two-sided P-value cutoff 0.05. |
| P-013 | 7 | Overall high risk of bias rule: high risk in at least 1 of allocation concealment or blinding, or unclear risk in at least 3 domains. |
| P-014 | 7 | Protocol change: add sensitivity analysis excluding trials enrolling patients with asymptomatic peripheral vascular disease identified by ABPI. |
| P-015 | 7 | Protocol change: add primary-composite sensitivity analysis excluding ASCEND because ASCEND included only ischemic stroke whereas the other studies' composite stroke definitions included ischemic, hemorrhagic, and unknown etiologies. |
| P-016 | 7 | Protocol change: extend search from database inception through November 1, 2018 and have both authors search independently in duplicate. |

## DOC-003 — eMethods and model selection (PDF pp. 1-6)

### Contents and detailed statistical definitions

| Local record | PDF page | Relationship-ready evidence |
|---|---:|---|
| M-001 | 1 | Contents register eMethods 1-3, eTables 1-6, and eFigures 1-4; all are mapped below. |
| M-002 | 2 | Final search date November 1, 2018. Search terms combine aspirin/acetylsalicylic acid, cardiovascular/mortality/myocardial infarction/stroke, and primary prevention. |
| M-003 | 3 | Estimated 10-year cardiovascular risk: in each trial, calculate primary-composite risk in the no-aspirin group, divide by mean follow-up years to obtain an annualized event rate, and multiply by 10. Confidence intervals assume Poisson-distributed events. The primary composite is cardiovascular mortality, non-fatal MI, and non-fatal stroke. |
| M-004 | 3 | Primary Bayesian tools: gemtc in R 3.4.1 and JAGS 4.3.0. Frequentist tool: meta package. |
| M-005 | 3 | Use log reported HR and corresponding SE when available; otherwise use event number and follow-up person-years. Constant event rate over follow-up is assumed for those trials. |
| M-006 | 3 | Fixed- and random-effects models use Poisson likelihood/log link and non-informative vague priors. MCMC: 5,000 adaptation iterations followed by 100,000 iterations in each of 4 chains. Convergence criterion: PSRF cutoff 1.05. |
| M-007 | 3 | Heterogeneity labels: I2 <25% low; 25%-50% moderate; >50% high. |
| M-008 | 4 | DIC model selection: a difference >3 units is important and the lower-DIC model is used. When models are within 3 DIC units, choose random effects if fixed-effect I2 >25%; otherwise fixed. |
| M-009 | 4 | Bayesian statistical-significance rule: 95% CrI excluding 1. |
| M-010 | 4 | Baseline absolute risk is no-aspirin events divided by no-aspirin participants. RR and 95% CI come from random-effects frequentist Mantel-Haenszel meta-analysis; combine RR and baseline risk to calculate ARD and 95% CI. Negative ARD indicates reduced risk with aspirin; positive ARD indicates increased risk. NNT/NNH is calculated only for statistically significant reductions/increases. |
| M-011 | 4 | Exploratory outcomes: incident cancer means new cancer diagnosis; cancer mortality is separate. Trial publications and related cancer publications/meta-analyses could supply data. |

### eMethods 3: every displayed DIC/model-selection row

The table columns are population, outcome, fixed DIC, random DIC, fixed-effect I2 (%), and selected model. Every row below is printed on DOC-003 pp. 5-6.

| Population | Outcome | Fixed DIC | Random DIC | I2 (%) | Selected model | Page |
|---|---|---:|---:|---:|---|---:|
| All patients | Composite outcome | 19.38 | 21.24 | 0 | fixed | 5 |
| All patients | All-cause mortality | 14.28 | 16.27 | 0 | fixed | 5 |
| All patients | Cardiovascular mortality | 24.56 | 26.53 | 0 | fixed | 5 |
| All patients | All myocardial infarction | 48.96 | 38.72 | 42 | random | 5 |
| All patients | Total stroke | 30.13 | 31.30 | 1 | fixed | 5 |
| All patients | Ischemic stroke | 25.81 | 25.72 | 18 | fixed | 5 |
| All patients | Major bleeding | 27.17 | 28.48 | 0 | fixed | 5 |
| All patients | Intracranial bleeding | 25.40 | 27.24 | 0 | fixed | 5 |
| All patients | Major GI bleeding | 28.46 | 29.74 | 0 | fixed | 5 |
| All patients | Incident cancer | 27.06 | 27.93 | 25 | random | 5 |
| All patients | Cancer mortality | 29.66 | 29.25 | 17 | fixed | 5 |
| Low risk | Composite outcome | 8.04 | 9.81 | 0 | fixed | 5 |
| Low risk | All-cause mortality | 7.47 | 8.93 | 0 | fixed | 5 |
| Low risk | Cardiovascular mortality | 9.15 | 10.55 | 0 | fixed | 5 |
| Low risk | All myocardial infarction | 15.68 | 14.81 | 32 | random | 5 |
| Low risk | Total stroke | 17.22 | 16.97 | 26 | random | 5 |
| Low risk | Ischemic stroke | 14.45 | 13.75 | 33 | random | 5 |
| Low risk | Major bleeding | 11.88 | 13.46 | 11 | fixed | 5 |
| Low risk | Intracranial bleeding | 11.45 | 13.00 | 0 | fixed | 5 |
| Low risk | Major GI bleeding | 13.81 | 15.15 | 9 | fixed | 5 |
| Low risk | Incident cancer | 11.45 | 11.03 | 41 | random | 5 |
| Low risk | Cancer mortality | 13.30 | 11.53 | 42 | random | 5 |
| High risk | Composite outcome | 12.71 | 14.05 | 0 | fixed | 5 |
| High risk | All-cause mortality | 8.79 | 10.02 | 0 | fixed | 6 |
| High risk | Cardiovascular mortality | 16.69 | 18.68 | 14 | fixed | 6 |
| High risk | All myocardial infarction | 26.93 | 26.03 | 26 | random | 6 |
| High risk | Total stroke | 18.33 | 19.38 | 11 | fixed | 6 |
| High risk | Ischemic stroke | 16.93 | 18.25 | 8 | fixed | 6 |
| High risk | Major bleeding | 17.14 | 17.39 | 10 | fixed | 6 |
| High risk | Intracranial bleeding | 15.05 | 16.28 | 0 | fixed | 6 |
| High risk | Major GI bleeding | 16.61 | 16.80 | 15 | fixed | 6 |
| High risk | Incident cancer | 14.23 | 15.52 | 3 | fixed | 6 |
| High risk | Cancer mortality | 14.74 | 16.33 | 0 | fixed | 6 |
| Diabetes | Composite outcome | 12.47 | 14.06 | 0 | fixed | 6 |
| Diabetes | All-cause mortality | 7.50 | 8.74 | 0 | fixed | 6 |
| Diabetes | Cardiovascular mortality | 10.15 | 10.34 | 51 | random | 6 |
| Diabetes | All myocardial infarction | 26.40 | 27.29 | 13 | fixed | 6 |
| Diabetes | Total stroke | 20.79 | 21.49 | 13 | fixed | 6 |
| Diabetes | Ischemic stroke | 8.65 | 6.41 | 77 | random | 6 |
| Diabetes | Major bleeding | 6.06 | 7.02 | 0 | fixed | 6 |
| Diabetes | Intracranial bleeding | 6.03 | 6.20 | 1 | fixed | 6 |
| Diabetes | Major GI bleeding | 6.06 | 6.25 | 1 | fixed | 6 |
| Diabetes | Incident cancer | 6.55 | 6.98 | 34 | random | 6 |
| Diabetes | Cancer mortality | 8.57 | 8.90 | 39 | random | 6 |

The table footnote states that the I2 values are from the fixed-effect model.

## DOC-003 eTable 1 — Trial-level outcome-definition map (PDF pp. 7-9)

This table is a matching key for interpreting cross-trial counts and pooled outcomes. `ATT-ND` below means the displayed text is “ATT meta-analysis (Not defined).” ACM means all-cause mortality; CVM means cardiovascular mortality; MI means myocardial infarction; ICH means intracranial bleeding; GI means gastrointestinal bleeding.

- **British Doctors' Study (1988), p. 7:** primary = MI, stroke (ischemic, hemorrhagic, unknown), vascular death including sudden death, pulmonary embolism and hemorrhage; ACM = any death; CVM = not specified; MI = not specified; all stroke = ischemic, hemorrhagic, unknown; ischemic stroke = clinician diagnosis without CT; major bleeding/ICH/GI = ATT-ND.
- **Physicians' Health Study (1989), p. 7:** primary = CVM, MI, and stroke of ischemic/hemorrhagic/unknown type; ACM = any death; CVM = cardiovascular “mechanism” of death; MI = 1971 WHO definition; all stroke = ischemic/hemorrhagic/unknown by ICD codes; ischemic stroke = neurologist judgment; major bleeding/ICH/GI = ATT-ND.
- **Hypertension Optimal Treatment (1998), p. 7:** primary = fatal/nonfatal MI, fatal/nonfatal stroke of ischemic/hemorrhagic/unknown type, and all other cardiovascular deaths; ACM = any death; CVM = death within 28 days of a cardiovascular event without obvious noncardiovascular cause; MI = two of central chest pain >15 minutes, enzyme elevation, or typical ECG change, with new Q/QS waves without clinical signs treated as silent MI; all stroke = ischemic/hemorrhagic/unknown; ischemic stroke not separately included because etiology was not specified; major bleeding/ICH/GI = ATT-ND.
- **Thrombosis Prevention Trial (1998), p. 7:** primary = coronary death, all MI, and all stroke; ACM = any death; CVM and MI = not specified; all stroke = ischemic/hemorrhagic/unknown; ischemic stroke based on imaging or necropsy; major bleeding/ICH/GI = ATT-ND.
- **Primary Prevention Project (2001), p. 7:** primary = CVM, MI, and stroke of ischemic/hemorrhagic/unknown type; ACM = any death; CVM = death within 28 days of a cardiovascular event with no other cause, sudden death, heart-failure death, and ICD-9 cardiovascular death; MI = two of typical chest pain, enzyme elevation, or typical ECG change; all stroke = ischemic/hemorrhagic/unknown; ischemic stroke based on imaging/necropsy when available; major bleeding/ICH/GI = ATT-ND.
- **Women's Health Study (2005), p. 8:** primary = CVM, nonfatal MI, and nonfatal ischemic/hemorrhagic stroke; ACM = any death; CVM confirmed from autopsy/death certificate/medical record/next-of-kin evidence; MI = WHO symptoms plus enzymes or ECG change; all stroke = ischemic or hemorrhagic; ischemic stroke based on CT/MRI; major bleeding/ICH/GI = ATT-ND.
- **POPADAD (2008), p. 8:** primary = coronary-heart-disease or stroke death, nonfatal MI, and nonfatal stroke; ACM = any death; CVM = coronary-heart-disease/stroke death by study definition; MI = WHO; all stroke = WHO definition, presumed ischemic plus hemorrhagic; ischemic stroke, major bleeding, and ICH = not reported; GI = not specified.
- **JPAD (2008), p. 8:** primary = fatal/nonfatal coronary heart disease and fatal/nonfatal cerebrovascular disease; ACM = any death; CVM = death from ischemic stroke or MI; MI = not specified; all stroke = ischemic/hemorrhagic; ischemic stroke = not specified; major bleeding = severe GI bleeding plus hemorrhagic stroke; ICH = hemorrhagic stroke, not specified; GI = major GI bleeding, not specified.
- **AAA (2010), p. 8:** primary = fatal/nonfatal coronary event or ischemic/hemorrhagic/unknown stroke; ACM = any death; CVM = coronary or ischemic/hemorrhagic/unknown stroke death; MI = not specified; all stroke = ischemic/hemorrhagic/unknown; ischemic stroke = not specified; major bleeding = hemorrhagic stroke, subarachnoid hemorrhage, or GI/other hemorrhage requiring hospital admission and intervention; ICH = hemorrhagic stroke or subarachnoid hemorrhage; GI = GI bleeding requiring admission for intervention.
- **JPPP (2014), p. 8:** primary = CVM, nonfatal MI, and nonfatal ischemic/hemorrhagic stroke; ACM = any death; CVM = not specified; MI = ESC/ACC; all stroke = ischemic or hemorrhagic including subarachnoid; ischemic stroke requires imaging evidence plus an acute regional neurologic deficit maintained 24 hours; major bleeding = serious extracranial hemorrhage requiring hospitalization/transfusion plus ICH; ICH = intracranial or subarachnoid hemorrhage; GI not included in analysis and not specified.
- **ASCEND (2018), p. 9:** primary = nonfatal MI, nonfatal ischemic stroke or TIA, and vascular death; ACM = any death; CVM = vascular death excluding hemorrhagic stroke; MI = MI; all stroke not included because only ischemic stroke was reported; ischemic stroke = ischemic stroke; bleeding-definition cells are blank on the printed row.
- **ARRIVE (2018), p. 9:** primary = cardiovascular death, nonfatal MI, and nonfatal ischemic/hemorrhagic/unknown stroke; ACM = any death; CVM/MI/ischemic stroke = not specified; all stroke = ischemic/hemorrhagic/unknown; major bleeding = GUSTO; ICH = hemorrhagic stroke; GI = severe GI bleed.
- **ASPREE (2018), p. 9:** primary = coronary-heart-disease death, ESC/ACC nonfatal MI, and fatal/nonfatal ischemic/hemorrhagic/uncertain/subarachnoid stroke; ACM = any death; CVM = stroke or coronary-heart-disease death; MI = ESC/ACC; all stroke = ischemic/hemorrhagic/uncertain/subarachnoid; ischemic stroke = ischemic stroke; major bleeding = hemorrhagic stroke plus clinically significant nonstroke bleeding requiring transfusion, hospitalization >24 h, prolongation >24 h, or causing death; ICH = hemorrhagic stroke or subdural/extradural/subarachnoid hemorrhage; GI = upper or lower GI bleed.

## DOC-003 eTable 2 — Risk-of-bias evidence map (PDF pp. 10-14)

The displayed domain order below is sequence generation, allocation concealment, blinding, detection, attrition, reporting, overall. This maps labels and the quantitative attrition/follow-up statements; it does not adjudicate study quality.

| Trial | Domain vector | Displayed quantitative attrition/follow-up evidence | Page |
|---|---|---|---:|
| British Doctors' Study | Low; Unclear; High; Unclear; Low; Low; High | mortality thought complete and morbidity virtually complete | 10 |
| Physicians' Health Study | Low; Unclear; Low; Unclear; Low; Low; Low | 99.7% still supplied morbidity information; vital status known for all 22,071 doctors | 10 |
| HOT | Low; Low; Low; Unclear; Low; Low; Low | 2.6% lost to follow-up; aspirin dose quoted as 75 mg daily | 10 |
| TPT | Low; Low; Low; Low; Low; Low; Low | 1.1% lacked information on possible nonfatal events; four treatment groups mentioned | 10 |
| PPP | Low; Low; High; Low; Low; Low; High | 92.3% had clinical follow-up at study end | 11 |
| WHS | Low; Unclear; Low; Unclear; Low; Low; Low | morbidity follow-up 97.2% and mortality follow-up 99.4%; questionnaires every 12 months | 11 |
| POPADAD | Low; Low; Low; Low; Low; Low; Low | 1,074 of 1,276 had final follow-up; visits every 6 months; aspirin 100 mg; four groups and allocation blocks of 8 | 11 |
| JPAD | Low; Low; High; Low; Low; Low; High | 193 of 2,539 lost; follow-up every 2 weeks in clinic and every 4 weeks in hospital | 12 |
| AAA | Low; Low; Low; Low; Low; Low; Low | 10 participants (0.3%) censored; aspirin 100 mg; allocation blocks of 8 | 12 |
| JPPP | Low; Low; High; Low; Low; Low; High | 194 patients (1.3%) excluded from randomized population | 13 |
| ASCEND | Low; Low; Low; Unclear; Low; Low; Low | complete data for 15,341 participants (99.1%); aspirin 100 mg; questionnaires every 6 months | 13 |
| ARRIVE | Low; Low; Low; Low; Low; Low; Low | 29.6% terminated prematurely: 29.4% aspirin and 29.9% placebo | 13-14 |
| ASPREE | Low; Low; Low; Low; Low; Low; Low | lost to follow-up: 1.5% aspirin and 1.6% placebo | 14 |

The eTable has 13 trials and 7 displayed domains. The matching eFigure 2 graphic is separately mapped below.

## DOC-003 eTable 3 — ARD and NNT/NNH (PDF p. 15)

Each cell is `ARD (95% CI); displayed NNT/NNH when present`. The page does not explicitly print an ARD unit. Negative ARD favors aspirin; positive ARD favors no aspirin. NNT/NNH is printed only when the ARD is statistically significant.

| Outcome | All patients | Low risk | High risk | Diabetes |
|---|---|---|---|---|
| Composite | -0.41 (-0.59 to -0.23); NNT 242 | -0.34 (-0.52 to -0.14); NNT 297 | -0.63 (-1.04 to -0.18); NNT 160 | -0.65 (-1.17 to -0.09); NNT 153 |
| All-cause mortality | -0.13 (-0.32 to 0.07) | -0.01 (-0.27 to 0.27) | -0.43 (-0.84 to 0.02) | -0.24 (-0.91 to 0.49) |
| Cardiovascular mortality | -0.07 (-0.17 to 0.04) | -0.07 (-0.16 to 0.03) | -0.04 (-0.32 to 0.27) | -0.05 (-0.94 to 1.27) |
| All MI | -0.28 (-0.47 to -0.05); NNT 361 | -0.27 (-0.49 to 0.00); NNT 366 | -0.32 (-0.74 to 0.16) | -0.26 (-0.88 to 0.47) |
| All stroke | -0.09 (-0.20 to 0.04) | -0.04 (-0.21 to 0.14) | -0.19 (-0.49 to 0.16) | -0.77 (-1.48 to 0.16) |
| Ischemic stroke | -0.19 (-0.30 to -0.06); NNT 540 | -0.16 (-0.29 to -0.02); NNT 623 | -0.28 (-0.63 to 0.12) | -0.83 (-1.70 to 0.50) |
| Incident cancer | 0.03 (-0.37 to 0.46) | 0.41 (-0.13 to 1.01) | -0.30 (-0.76 to 0.19) | -0.68 (-2.09 to 0.95) |
| Cancer mortality | 0.05 (-0.11 to 0.23) | 0.16 (-0.06 to 0.42) | -0.13 (-0.41 to 0.17) | 0.16 (-0.56 to 1.02) |
| Major bleeding | 0.47 (0.34 to 0.62); NNH 210 | 0.40 (0.25 to 0.57); NNH 249 | 0.64 (0.35 to 0.97); NNH 152 | 0.80 (0.29 to 1.39); NNH 121 |
| Intracranial bleeding | 0.11 (0.04 to 0.18); NNH 927 | 0.13 (0.05 to 0.22); NNH 796 | 0.07 (-0.04 to 0.21) | 0.12 (-0.09 to 0.43) |
| Major GI bleeding | 0.30 (0.20 to 0.41); NNH 334 | 0.27 (0.15 to 0.40); NNH 376 | 0.39 (0.16 to 0.69); NNH 255 | 0.41 (0.06 to 0.86); NNH 243 |

## DOC-003 eTable 4 — Total stroke outcomes (PDF p. 16)

| Population | Studies | A events/N | N events/N | ARR (95% CI) | HR (95% CrI) | I2 |
|---|---:|---|---|---|---|---:|
| All | 12 | 1,116/73,883 | 1,136/72,317 | 0.10 (-0.03 to 0.22) | 0.93 (0.86 to 1.02) | 1 |
| Low risk | 6 | 752/56,212 | 788/56,354 | 0.04 (-0.15 to 0.20) | 0.95 (0.79 to 1.16) | 6 |
| High risk | 7 | 381/17,671 | 380/15,963 | 0.22 (-0.07 to 0.49) | 0.89 (0.77 to 1.03) | 11 |
| Diabetes | 7 | 128/4,048 | 156/3,960 | 0.50 (-0.05 to 0.97) | 0.78 (0.61 to 1.00)* | 13 |

Footnote: the unrounded diabetes HR upper CrI is 1.004.

## DOC-003 eTable 5 — Events per 10,000 participant-years (PDF p. 17)

Each cell is `A / N`.

| Outcome | All | Low risk | High risk | Diabetes |
|---|---|---|---|---|
| Composite | 60.2 / 65.2 | 41.3 / 46.4 | 109.2 / 117.9 | 103.6 / 114.1 |
| All-cause mortality | 69.4 / 70.0 | 50.5 / 50.4 | 118.5 / 124.9 | 134.2 / 137.6 |
| Cardiovascular mortality | 19.1 / 19.5 | 10.7 / 11.9 | 40.7 / 40.7 | 38.3 / 40.4 |
| All MI | 28.1 / 31.2 | 17.2 / 21.0 | 56.5 / 59.8 | 59.8 / 62.6 |
| Total stroke | 24.0 / 25.0 | 19.9 / 20.9 | 41.5 / 44.9 | 59.0 / 74.2 |
| Ischemic stroke | 18.4 / 21.4 | 14.7 / 17.1 | 30.8 / 36.9 | 40.3 / 46.7 |
| Cancer incidence | 105.4 / 105.5 | 97.7 / 93.8 | 121.8 / 132.4 | 162.7 / 166.2 |
| Cancer mortality | 31.2 / 30.1 | 23.8 / 21.6 | 48.8 / 51.9 | 61.9 / 60.9 |
| Major bleeding | 23.1 / 16.4 | 19.2 / 13.4 | 37.7 / 28.3 | 54.7 / 42.4 |
| Intracranial bleeding | 6.7 / 5.1 | 6.5 / 4.6 | 7.4 / 6.3 | 10.0 / 8.3 |
| Major GI bleeding | 12.9 / 8.2 | 10.5 / 6.7 | 19.5 / 12.6 | 22.6 / 16.7 |

Risk groups are defined by estimated 10-year primary-composite risk: low <10%, high at least 10%. WHS lacked a high-risk subgroup count and was excluded from high-risk event-rate calculations.

## DOC-003 eTable 6 — Sensitivity analyses (PDF p. 18)

Columns are: dose at most 100 mg/day (`11 studies; N=134,470`); double-blind placebo-controlled (`9; N=135,043`); published since 2000 (`9; N=113,140`); and excluding asymptomatic PAD (`11; N=156,874`). Every cell is HR (95% CrI).

| Outcome | <=100 mg | Double-blind | Since 2000 | Exclude PAD |
|---|---|---|---|---|
| Composite | 0.89 (0.83 to 0.95) | 0.88 (0.83 to 0.94) | 0.91 (0.84 to 0.98) | 0.88 (0.83 to 0.93) |
| All-cause mortality | 0.95 (0.87 to 1.03) | 0.96 (0.88 to 1.03) | 0.94 (0.85 to 1.04) | 0.94 (0.88 to 1.01) |
| Cardiovascular mortality | 0.91 (0.80 to 1.05) | 0.96 (0.84 to 1.09) | 0.88 (0.73 to 1.06) | 0.92 (0.82 to 1.04) |
| All MI | 0.87 (0.76 to 1.00)* | 0.84 (0.70 to 1.03) | 0.94 (0.81 to 1.08) | 0.80 (0.68 to 0.95) |
| Total stroke | 0.90 (0.82 to 0.98) | 0.93 (0.84 to 1.02) | 0.89 (0.80 to 0.98) | 0.95 (0.87 to 1.03) |
| Ischemic stroke | 0.79 (0.74 to 0.85) | 0.85 (0.69 to 1.06) | 0.80 (0.74 to 0.86) | 0.81 (0.76 to 0.87) |
| Major bleeding | 1.43 (1.30 to 1.57) | 1.41 (1.28 to 1.55) | 1.39 (1.26 to 1.53) | 1.42 (1.30 to 1.56) |
| Intracranial bleeding | 1.31 (1.11 to 1.56) | 1.33 (1.11 to 1.60) | 1.34 (1.13 to 1.60) | 1.33 (1.13 to 1.57) |
| Major GI bleeding | 1.55 (1.36 to 1.77) | 1.54 (1.35 to 1.76) | 1.48 (1.28 to 1.71) | 1.57 (1.38 to 1.79) |
| Incident cancer | 1.01 (0.92 to 1.08) | 0.99 (0.89 to 1.06) | 1.01 (0.91 to 1.10) | 1.02 (0.98 to 1.07) |
| Cancer mortality | 1.04 (0.96 to 1.12) | 1.04 (0.96 to 1.12) | 1.03 (0.95 to 1.12) | 1.05 (0.97 to 1.13) |

The starred all-MI upper CrI under <=100 mg is 0.9989 before rounding.

## DOC-003 eFigures 1-3 (PDF pp. 19-21)

### eFigure 1 study flow, p. 19

- Identified: 1,385 records, comprising 668 Embase plus 717 Medline.
- Duplicates removed: 235; titles/abstracts screened: 1,150.
- Excluded: 1,131, subdivided as not relevant 605; not primary prevention 244; trial protocol 147; conference publication 60; review 45; systematic review/meta-analysis 13; non-relevant subgroup 10; non-English publication 7.
- Two articles were identified from meta-analyses. Final inclusion: 21 publications reporting 13 trials.

### eFigure 2 risk-of-bias summary, p. 20

The graphic uses a 0%-100% axis with Low/High/Unclear color segments. Sequence generation, reporting, and attrition are drawn as 100% low. Allocation concealment is drawn as approximately 77% low/23% unclear. Blinding and overall risk are drawn as approximately 69% low/31% high. Detection is drawn as approximately 69% low/31% unclear. These are graphical proportions without printed numeric data labels; the 13 trial-level vectors in eTable 2 are the exact categorical source for any recomputation.

### eFigure 3 funnel plot, p. 21

- Plot: primary cardiovascular outcome, risk ratio on the x-axis and standard error on the y-axis; 10 study points are visible.
- Printed Egger test: coefficient -0.47, standard error 0.77, t=-0.59, P=0.57.

## DOC-003 eFigure 4 — Frequentist forest-plot records (PDF pp. 22-26)

The caption defines Experimental as aspirin, Control as no aspirin, RR as risk ratio, and CI as confidence interval. Each study row below is `study: A events/A total vs N events/N total; RR [95% CI]; fx wt/rx wt`. Pooled lines preserve both model estimates, analysis totals, I2, tau-squared, and heterogeneity P values.

### Composite outcome, p. 22

```text
HOT: 329/9399 vs 383/9391; 0.86 [0.74, 0.99]; 11.3%/10.8%
TPT (excluding warfarin): 105/1268 vs 138/1272; 0.76 [0.60, 0.97]; 4.1%/3.9%
PPP: 45/2226 vs 64/2269; 0.72 [0.49, 1.04]; 1.9%/1.6%
WHS: 477/19934 vs 522/19942; 0.91 [0.81, 1.03]; 15.4%/15.1%
BDS: 291/3429 vs 143/1710; 1.01 [0.84, 1.23]; 5.6%/6.2%
PHS: 307/11037 vs 370/11034; 0.83 [0.71, 0.96]; 10.9%/10.2%
AAA: 134/1675 vs 136/1675; 0.99 [0.78, 1.24]; 4.0%/4.3%
POPADAD: 127/638 vs 132/638; 0.96 [0.77, 1.20]; 3.9%/4.8%
JPAD: 56/1262 vs 70/1277; 0.81 [0.57, 1.14]; 2.1%/1.9%
JPPP: 193/7220 vs 207/7244; 0.94 [0.77, 1.14]; 6.1%/6.1%
ASCEND: 542/7740 vs 587/7740; 0.92 [0.83, 1.03]; 17.3%/17.9%
ARRIVE: 208/6270 vs 218/6276; 0.96 [0.79, 1.15]; 6.4%/6.5%
ASPREE: 329/9525 vs 372/9589; 0.89 [0.77, 1.03]; 10.9%/10.7%
Totals A/N=81623/80057. Fixed 0.90 [0.86, 0.94]; random 0.90 [0.86, 0.94]; I2=0%, tau2=0, P=0.75.
```

### All-cause mortality, p. 22

```text
HOT: 284/9399 vs 305/9391; 0.93 [0.79, 1.09]; 8.4%/7.9%
TPT (excluding warfarin): 113/1268 vs 110/1272; 1.03 [0.80, 1.32]; 3.0%/3.2%
PPP: 62/2226 vs 78/2269; 0.81 [0.58, 1.13]; 2.1%/1.9%
WHS: 609/19934 vs 642/19942; 0.95 [0.85, 1.06]; 17.7%/16.9%
BDS: 270/3429 vs 151/1710; 0.89 [0.74, 1.08]; 5.5%/5.5%
PHS: 217/11037 vs 227/11034; 0.96 [0.79, 1.15]; 6.2%/5.9%
AAA: 176/1675 vs 186/1675; 0.95 [0.78, 1.15]; 5.1%/5.3%
POPADAD: 94/638 vs 101/638; 0.93 [0.72, 1.21]; 2.8%/3.0%
JPAD: 34/1262 vs 38/1277; 0.91 [0.57, 1.43]; 1.0%/1.0%
JPPP: 297/7220 vs 303/7244; 0.98 [0.84, 1.15]; 8.3%/8.2%
ASCEND: 748/7740 vs 792/7740; 0.94 [0.86, 1.04]; 21.8%/22.4%
ARRIVE: 160/6270 vs 161/6276; 0.99 [0.80, 1.23]; 4.4%/4.3%
ASPREE: 558/9525 vs 494/9589; 1.14 [1.01, 1.28]; 13.5%/14.5%
Totals A/N=81623/80057. Fixed 0.97 [0.93, 1.02]; random 0.97 [0.93, 1.02]; I2=0%, tau2=0, P=0.60.
```

### Cardiovascular mortality, p. 23

```text
HOT: 133/9399 vs 140/9391; 0.95 [0.75, 1.20]; 13.8%/13.9%
TPT (excluding warfarin): 49/1268 vs 49/1272; 1.00 [0.68, 1.48]; 4.8%/5.1%
PPP: 17/2226 vs 31/2269; 0.56 [0.31, 1.01]; 3.0%/2.2%
WHS: 120/19934 vs 126/19942; 0.95 [0.74, 1.22]; 12.4%/12.4%
BDS: 119/3429 vs 59/1710; 1.01 [0.74, 1.37]; 7.8%/8.2%
PHS: 81/11037 vs 83/11034; 0.98 [0.72, 1.32]; 8.2%/8.3%
AAA: 35/1675 vs 30/1675; 1.17 [0.72, 1.89]; 3.0%/3.3%
POPADAD: 43/638 vs 35/638; 1.23 [0.80, 1.89]; 3.4%/4.1%
JPAD: 1/1262 vs 10/1277; 0.10 [0.01, 0.79]; 1.0%/0.2%
JPPP: 58/7220 vs 57/7244; 1.02 [0.71, 1.47]; 5.6%/5.8%
ASCEND: 210/7740 vs 226/7740; 0.93 [0.77, 1.12]; 22.2%/22.5%
ARRIVE: 38/6270 vs 39/6276; 0.98 [0.62, 1.52]; 3.8%/3.9%
ASPREE: 91/9525 vs 112/9589; 0.82 [0.62, 1.08]; 11.0%/10.2%
Totals A/N=81623/80057. Fixed 0.94 [0.86, 1.03]; random 0.95 [0.87, 1.03]; I2=0%, tau2=0, P=0.50.
```

### All myocardial infarction, p. 23

```text
HOT: 82/9399 vs 127/9391; 0.65 [0.49, 0.85]; 7.8%/8.1%
TPT (excluding warfarin): 83/1268 vs 107/1272; 0.78 [0.59, 1.03]; 6.6%/8.1%
PPP: 19/2226 vs 28/2269; 0.69 [0.39, 1.23]; 1.7%/3.3%
WHS: 198/19934 vs 193/19942; 1.03 [0.84, 1.25]; 11.9%/10.3%
BDS: 181/3429 vs 86/1710; 1.05 [0.82, 1.35]; 7.1%/8.8%
PHS: 139/11037 vs 239/11034; 0.58 [0.47, 0.72]; 14.7%/10.0%
AAA: 90/1675 vs 86/1675; 1.05 [0.78, 1.40]; 5.3%/7.9%
POPADAD: 76/638 vs 69/638; 1.10 [0.81, 1.50]; 4.2%/7.4%
JPAD: 12/1262 vs 14/1277; 0.87 [0.40, 1.87]; 0.9%/2.1%
JPPP: 27/7220 vs 37/7244; 0.73 [0.45, 1.20]; 2.3%/4.2%
ASCEND: 296/7740 vs 317/7740; 0.93 [0.80, 1.09]; 19.5%/11.4%
ARRIVE: 95/6270 vs 112/6276; 0.85 [0.65, 1.11]; 6.9%/8.3%
ASPREE: 171/9525 vs 184/9589; 0.94 [0.76, 1.15]; 11.3%/10.0%
Totals A/N=81623/80057. Fixed 0.87 [0.81, 0.93]; random 0.86 [0.76, 0.97]; I2=61%, tau2=0.0273, P<0.01.
```

### Total stroke, p. 24

```text
HOT: 146/9399 vs 148/9391; 0.99 [0.79, 1.24]; 10.5%/10.7%
TPT (excluding warfarin): 18/1268 vs 26/1272; 0.69 [0.38, 1.26]; 1.8%/1.6%
PPP: 16/2226 vs 24/2269; 0.68 [0.36, 1.28]; 1.7%/1.4%
WHS: 221/19934 vs 266/19942; 0.83 [0.70, 0.99]; 18.9%/17.6%
BDS: 91/3429 vs 42/1710; 1.08 [0.75, 1.55]; 4.0%/4.2%
PHS: 119/11037 vs 98/11034; 1.21 [0.93, 1.58]; 7.0%/7.8%
AAA: 44/1675 vs 50/1675; 0.88 [0.59, 1.31]; 3.5%/3.5%
POPADAD: 37/638 vs 50/638; 0.74 [0.49, 1.12]; 3.5%/3.3%
JPAD: 28/1262 vs 32/1277; 0.89 [0.54, 1.46]; 2.3%/2.2%
JPPP: 128/7220 vs 128/7244; 1.00 [0.79, 1.28]; 9.1%/9.4%
ASCEND: 240/7740 vs 263/7740; 0.91 [0.77, 1.08]; 18.7%/18.6%
ARRIVE: 75/6270 vs 67/6276; 1.12 [0.81, 1.55]; 4.8%/5.1%
ASPREE: 195/9525 vs 203/9589; 0.97 [0.80, 1.17]; 14.4%/14.6%
Totals A/N=81623/80057. Fixed 0.94 [0.88, 1.02]; random 0.94 [0.87, 1.01]; I2=0%, tau2=0, P=0.51.
```

### Ischemic stroke, p. 24

```text
TPT (excluding warfarin): 10/1268 vs 18/1272; 0.56 [0.26, 1.20]; 1.9%/1.5%
PPP: 14/2226 vs 21/2269; 0.68 [0.35, 1.33]; 2.2%/1.9%
WHS: 170/19934 vs 221/19942; 0.77 [0.63, 0.94]; 23.4%/21.8%
BDS: 21/3429 vs 7/1710; 1.50 [0.64, 3.51]; 1.0%/1.2%
PHS: 91/11037 vs 82/11034; 1.11 [0.82, 1.49]; 8.7%/9.8%
AAA: 30/1675 vs 37/1675; 0.81 [0.50, 1.31]; 3.9%/3.8%
JPAD: 22/1262 vs 25/1277; 0.89 [0.50, 1.57]; 2.6%/2.7%
JPPP: 85/7220 vs 101/7244; 0.84 [0.63, 1.12]; 10.7%/10.5%
ASCEND: 240/7740 vs 263/7740; 0.91 [0.77, 1.08]; 27.9%/29.1%
ASPREE: 148/9525 vs 167/9589; 0.89 [0.72, 1.11]; 17.6%/17.9%
Totals A/N=65316/63752. Fixed 0.87 [0.80, 0.96]; random 0.87 [0.80, 0.96]; I2=0%, tau2=0, P=0.55.
```

### Incident cancer, p. 24

```text
HOT: 294/9399 vs 311/9391; 0.94 [0.81, 1.10]; 7.0%/9.5%
PPP: 86/2226 vs 80/2269; 1.10 [0.81, 1.48]; 1.8%/3.3%
WHS: 1438/19934 vs 1427/19942; 1.01 [0.94, 1.08]; 32.3%/21.9%
BDS: 119/3429 vs 58/1710; 1.02 [0.75, 1.39]; 1.8%/3.1%
AAA: 166/1675 vs 194/1675; 0.86 [0.70, 1.04]; 4.4%/6.8%
POPADAD: 45/638 vs 60/638; 0.75 [0.52, 1.09]; 1.4%/2.2%
JPAD: 149/1262 vs 169/1277; 0.89 [0.73, 1.10]; 3.8%/6.2%
JPPP: 332/7220 vs 271/7244; 1.23 [1.05, 1.44]; 6.1%/9.4%
ASCEND: 897/7740 vs 887/7740; 1.01 [0.93, 1.10]; 20.1%/18.6%
ASPREE: 981/9525 vs 952/9589; 1.04 [0.95, 1.13]; 21.5%/19.1%
Totals A/N=63048/61475. Fixed 1.01 [0.97, 1.05]; random 1.00 [0.95, 1.06]; I2=36%, tau2=0.0026, P=0.12.
```

### Cancer mortality, p. 25

```text
HOT: 108/9399 vs 105/9391; 1.03 [0.79, 1.34]; 7.2%/8.1%
TPT (excluding warfarin): 49/1268 vs 51/1272; 0.96 [0.66, 1.42]; 3.5%/4.4%
PPP: 31/2226 vs 29/2269; 1.09 [0.66, 1.80]; 2.0%/2.7%
WHS: 284/19934 vs 299/19942; 0.95 [0.81, 1.12]; 20.5%/16.7%
BDS: 75/3429 vs 47/1710; 0.80 [0.56, 1.14]; 4.3%/4.9%
PHS: 79/11037 vs 68/11034; 1.16 [0.84, 1.60]; 4.7%/5.9%
AAA: 78/1675 vs 90/1675; 0.87 [0.64, 1.16]; 6.2%/6.9%
POPADAD: 25/638 vs 31/638; 0.81 [0.48, 1.35]; 2.1%/2.5%
JPAD: 63/1262 vs 60/1277; 1.06 [0.75, 1.50]; 4.1%/5.3%
JPPP: 134/7220 vs 125/7244; 1.08 [0.84, 1.37]; 8.5%/9.5%
ASCEND: 309/7740 vs 315/7740; 0.98 [0.84, 1.14]; 21.6%/17.7%
ASPREE: 295/9525 vs 227/9589; 1.31 [1.10, 1.55]; 15.5%/15.5%
Totals A/N=75353/73781. Fixed 1.03 [0.96, 1.11]; random 1.03 [0.94, 1.12]; I2=21%, tau2=0.0044, P=0.24.
```

### Major bleeding, p. 25

```text
HOT: 136/9399 vs 78/9391; 1.74 [1.32, 2.30]; 9.3%/10.0%
TPT (excluding warfarin): 8/1268 vs 4/1272; 2.01 [0.61, 6.65]; 0.5%/0.5%
PPP: 25/2226 vs 9/2269; 2.83 [1.32, 6.05]; 1.1%/1.3%
WHS: 127/19934 vs 91/19942; 1.40 [1.07, 1.83]; 10.9%/10.6%
BDS: 20/3429 vs 10/1710; 1.00 [0.47, 2.13]; 1.6%/1.3%
PHS: 48/11037 vs 30/11034; 1.60 [1.01, 2.52]; 3.6%/3.7%
AAA: 34/1675 vs 20/1675; 1.70 [0.98, 2.94]; 2.4%/2.6%
JPAD: 18/1262 vs 12/1277; 1.52 [0.73, 3.14]; 1.4%/1.5%
JPPP: 104/7220 vs 70/7244; 1.49 [1.10, 2.01]; 8.4%/8.5%
ASCEND: 314/7740 vs 245/7740; 1.28 [1.09, 1.51]; 29.3%/28.5%
ASPREE: 361/9525 vs 265/9589; 1.37 [1.17, 1.60]; 31.6%/31.5%
Totals A/N=74715/73143. Fixed 1.42 [1.30, 1.55]; random 1.42 [1.30, 1.55]; I2=0%, tau2=0, P=0.54.
```

### Intracranial bleeding, p. 25

```text
HOT: 14/9399 vs 15/9391; 0.93 [0.45, 1.93]; 5.8%/4.9%
TPT (excluding warfarin): 3/1268 vs 2/1272; 1.50 [0.25, 8.99]; 0.8%/0.8%
PPP: 4/2226 vs 3/2269; 1.36 [0.30, 6.07]; 1.1%/1.2%
WHS: 51/19934 vs 41/19942; 1.24 [0.83, 1.88]; 15.8%/15.5%
BDS: 13/3429 vs 6/1710; 1.08 [0.41, 2.84]; 3.1%/2.8%
PHS: 23/11037 vs 12/11034; 1.92 [0.95, 3.85]; 4.6%/5.4%
AAA: 11/1675 vs 7/1675; 1.57 [0.61, 4.04]; 2.7%/2.9%
JPAD: 8/1262 vs 7/1277; 1.16 [0.42, 3.18]; 2.7%/2.5%
JPPP: 52/7220 vs 36/7244; 1.45 [0.95, 2.21]; 13.9%/14.5%
ASCEND: 55/7740 vs 45/7740; 1.22 [0.83, 1.81]; 17.4%/16.9%
ARRIVE: 8/6270 vs 11/6276; 0.73 [0.29, 1.81]; 4.3%/3.1%
ASPREE: 107/9525 vs 72/9589; 1.50 [1.11, 2.01]; 27.7%/29.5%
Totals A/N=80985/79419. Fixed 1.33 [1.14, 1.57]; random 1.33 [1.13, 1.57]; I2=0%, tau2=0, P=0.93.
```

### Major gastrointestinal bleeding, p. 26

```text
HOT: 77/9399 vs 37/9391; 2.08 [1.41, 3.07]; 9.8%/10.8%
TPT (excluding warfarin): 6/1268 vs 2/1272; 3.01 [0.61, 14.88]; 0.5%/0.6%
PPP: 17/2226 vs 5/2269; 3.47 [1.28, 9.38]; 1.3%/1.7%
WHS: 127/19934 vs 91/19942; 1.40 [1.07, 1.83]; 24.0%/23.0%
PHS: 49/11037 vs 28/11034; 1.75 [1.10, 2.78]; 7.4%/7.7%
AAA: 9/1675 vs 8/1675; 1.12 [0.44, 2.91]; 2.1%/1.8%
JPAD: 5/1262 vs 4/1277; 1.26 [0.34, 4.70]; 1.0%/1.0%
ASCEND: 137/7740 vs 101/7740; 1.36 [1.05, 1.75]; 26.6%/25.4%
ARRIVE: 4/6270 vs 2/6276; 2.00 [0.37, 10.93]; 0.5%/0.6%
ASPREE: 162/9525 vs 102/9589; 1.60 [1.25, 2.05]; 26.8%/27.3%
Totals A/N=70336/70465. Fixed 1.56 [1.38, 1.78]; random 1.55 [1.37, 1.77]; I2=0%, tau2=0, P=0.54.
```

## Remaining assigned pages and coverage statement

- DOC-003 pp. 27-29 contain supplemental references 1-21. Their years, versions, volume/page citations, and reference numbers are bibliographic rather than paper-result relationships; no additional result-relevant quantitative unit is present.
- DOC-002 coverage is complete for 7/7 pages. DOC-003 coverage is complete for 29/29 pages, including direct visual inspection of every table/figure page 7-26.
- Registered quantitative coverage includes 44 DIC/model rows; 13 trial outcome-definition rows; 13 trial risk-of-bias vectors; 44 ARD cells and all 18 displayed NNT/NNH entries; 4 total-stroke population rows; 88 event-rate values; 44 sensitivity HR/CrI cells; all flow counts; 7 risk-of-bias graph domains; the Egger statistic; and 130 forest-plot study rows plus 11 fixed-effect and 11 random-effects pooled records.

## Explicit limitations and gaps

1. eTable 3 does not explicitly state the unit of ARD on p. 15; values are transcribed exactly without assigning an unstated unit.
2. eFigure 2 has no numeric segment labels. Its percentages above are visual readings from the 0%-100% axis; exact categorical trial-level inputs are preserved in the eTable 2 vectors.
3. eFigure 3 does not print numeric coordinates for its 10 study points. Only the plotted axes, visible point count, and printed Egger statistic are registered.
4. Forest-plot values are embedded graph text and absent from the reusable layout extraction. Targeted CPU OCR was used only as a transcription aid, followed by direct visual confirmation against PDF pp. 22-26. No unresolved forest-plot transcription gap remains at the displayed precision.
5. Several eTable 1 cells explicitly say “not specified,” “not defined,” “not reported,” or are blank; those are source-level missing definitions and are retained rather than inferred.

