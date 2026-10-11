# Support evidence map: DOC-002, physical PDF pages 33–64

Status: COMPLETE. Exact assigned scope: `joi180109supp1_prod.pdf`, DOC-002, physical PDF pages 33–64 inclusive (32 unique pages). Document role: PLAN throughout. This is the initial protocol portion of the supplied bundle, whose page footer identifies `P150912_nifc-HIGH-Patient_v1-0-20160212`. The footer date/version is preserved as source identity; this shard does not infer when a later protocol or SAP superseded it. Runtime CODEX_THREAD_ID: `01a129b4-9407-7911-8acb-78005de23e07`.

The full QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md, current source inventory, source coverage, evidence asset inventory and tooling record were read. No old candidates, checker decisions, classifications, or reports were consulted. This artifact maps evidence without diagnosing or registering findings. Local relationship keys below are shard keys for coordinator assignment to the complete N/S inventory; repeated endpoint occurrences are linked rather than treated as independent outcomes. Matching main-paper keys are semantic join keys, not assertions that a result was reported: the main paper is outside this shard's assigned scope.

## Assets and direct-source inspection

All 32 pages have usable reusable native and layout text at `.ai_paper_validation/review_1_5_2/preprocessing/native_text/pages/DOC-002/pNNN.txt` and `.ai_paper_validation/review_1_5_2/preprocessing/layout_text/pages/DOC-002/pNNN.txt`. Complete per-page layout was read anew for all assigned pages, with native text as a complementary transcription aid. Existing source-linked rendered PNGs for pp.40,42,50,51,53,54 were visually inspected; p.40 contains Figure 4, including graphical labels absent from native/layout text. Images are under `.ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-pNNN.png`. Their original engine version is unspecified in the existing assets. No asset was modified.

Direct `pdftotext -layout -f N -l N joi180109supp1_prod.pdf -` was run for each N=33 through 64 and compared byte-for-byte with its existing layout page file using `cmp -s`; all 32 were identical. Engine: Poppler pdftotext 25.03.0, CPU, process-stream output only. No new derivative file, rendering, OCR, Office extraction or fallback tooling was required. Fresh-required units: 0. Scientific mapped units: 32/32. Reusable units: 32/32. No extraction gaps remain. There are no workbook formulas, cached/displayed workbook values, CSV fields, or supplied Office units in this assigned scope.

## Every-page coverage

All source references below are physical PDF pages, with protocol printed line numbers where present. Each page is COMPLETE, including pages with no applicable inferential result or design item.

| Page | Exact content inspected | Applicable mapped evidence or explicit no-applicable record |
|---:|---|---|
| 33 | Section 10, lines 523–532, participating network | Administrative context: Grrr-OH centres; all in France except centre identifiers 14 and 15 in Belgium. No result estimate or analysis specification. |
| 34 | Participating ICU table, identifiers 1–24 | Administrative site list; no outcome result, statistical definition, or decision rule. Site labels are retained in the recruitment table below. Telephone/contact digits are administrative identifiers, not quantitative relationships. |
| 35 | Participating ICU table continuation, identifiers 25–26 | Administrative site list continuation; no result-relevant statistical item. |
| 36 | Expected recruitment table, rows 1–24 | N-P2-001, complete monthly and 24-month planning quantities below. |
| 37 | Recruitment rows 25–26 and total; lines 536–538 | N-P2-001: total 26 centres, 34/month, 816/24 months; N-P2-002: 14 additional invited centres, response pending. |
| 38 | Section 11, lines 539–560 | S-P2-001 primary objective and S-P2-003 complete secondary objectives. |
| 39 | Section 12, lines 561–580 | S-P2-001 noninferiority design; S-P2-002 general margin rationale. |
| 40 | Lines 581–594, Figure 4 plus accompanying interpretation | S-P2-002 one-sided interval illustration, efficacy contrast, direction, null and margin geometry. |
| 41 | Lines 595–598, continuation of Figure 4 interpretation | S-P2-002 lower one-sided confidence limit defines trial result; point estimates deliberately omitted from illustration. |
| 42 | Lines 599–617, design and inclusion criteria | S-P2-004 exact 9%/95% decision statement; S-P2-005 analysis population; S-P2-006 inclusion criteria. |
| 43 | Lines 618–638, inclusion, exclusion, intervention | S-P2-006 oxygen-need thresholds, DNI eligibility, exclusions; S-P2-007 open two-strategy comparison and control device options. |
| 44 | Lines 639–657, intervention dosing | S-P2-007 control target and discharge rule; S-P2-008 HFNO flow, FiO2, target, use during procedures/intubation/extubation and exceptions. |
| 45 | Lines 658–677, stopping and subgroups | S-P2-009 HFNO stopping, eligibility timing; S-P2-010 stratification and all four predefined subgroups. |
| 46 | Lines 678–698, subgroup interactions and endpoints | S-P2-010 ICU-mortality interaction wording; S-P2-001 primary endpoint; S-P2-003 secondary endpoint details and DNI outcomes. |
| 47 | Lines 699–719, endpoint continuation and practical difficulties | S-P2-003 post-intubation mortality and satisfaction; N-P2-003 administrative workload/recruitment planning. |
| 48 | Lines 720–722, usual-care legal classification | No applicable quantitative result, statistical design element, margin, or rule. Usual-care regulatory description only. |
| 49 | Section 13, lines 723–737, anticipated interpretation | S-P2-011 noninferiority decision implications, 28-day mortality, superiority hypotheses for secondary endpoints. Preliminary-study benefits are background without printed quantitative results. |
| 50 | Section 14, lines 738–751, randomisation | S-P2-012 patient assessment, printed centre randomisation unit, 1:1 parallel groups, two strata, eight lists, concealed fixed permutation blocks. |
| 51 | Section 15, lines 752–763, sample size | S-P2-013: 26% baseline mortality, 9% margin, alpha 5%, power 80%, 816 total/408 each, 24-month recruitment and 6-month follow-up. |
| 52 | Section 16, lines 764–783, bias and comparisons | S-P2-014 ITT and administrative censoring; S-P2-015 baseline no tests and secondary two-sided tests; printed primary hypothesis wording retained. |
| 53 | Lines 784–804, comparisons, interim, populations and missingness | S-P2-016 primary-endpoint interactions; S-P2-017 PP plus ITT requirement; S-P2-018 no interim; S-P2-019 full set excluding consent withdrawal; S-P2-020 missing outcome time-to-event strategy. |
| 54 | Lines 805–824, missing predictors and endpoint analyses | S-P2-021 multiple imputation; S-P2-022 primary RR/95% CI/adjustment; S-P2-023 Gail–Simon interactions; S-P2-024 competing risks/Gray/Cox; S-P2-025 ICU length-of-stay estimators. |
| 55 | Lines 825–831, longitudinal analyses and software | S-P2-026 joint models with right censoring; SAS and R named, no software versions. |
| 56 | Section 17, lines 832–851, data collection | S-P2-027 process-of-care definition and collection timing; N-P2-004 staffing counts. Other content is administrative. |
| 57 | Lines 852–872, investigators and monitoring | S-P2-028 consent/reconsent, adherence and missing-data completion; six monitored items recorded. No inferential result display. |
| 58 | Lines 873–885, approvals and database access | No applicable quantitative result or statistical decision rule. Named data custodian is responsible for statistical analyses/tables/figures; governance only. |
| 59 | Section 18, lines 886–906, safety definitions | S-P2-029 adverse-event, unanticipated-event, serious-event definitions and study-period/ICU safety context. |
| 60 | Lines 907–927, safety definitions and reporting | S-P2-029 serious-event continuation and attribution classes; S-P2-030 reporting inclusion conditions and 5-working-day/24-hour timing. |
| 61 | Lines 928–936, DSMB | S-P2-030 7-calendar-day and 15-calendar-day notification timing; S-P2-031 printed scheduled-interim safety-review statement. |
| 62 | Section 19 references 1–9, lines 937–957 | Explicit no-applicable unit: bibliography only; years, journal volumes/issues, page ranges and reference numbers are citation metadata, not trial outcome or sample-size data. |
| 63 | References 10–17, lines 958–977 | Explicit no-applicable unit: bibliography only; reference 13 identifies FLORALI background and reference 14 the Stephan trial cited for design rationale; no new quantitative trial relationship. |
| 64 | References 18–26, lines 978–997 | Explicit no-applicable unit: bibliography only; title mentioning six oxygen devices is historical bibliographic wording, not a HIGH study quantity. |

## Numeric and operational planning inventory

### N-P2-001 — Full recruitment projection table

Source: [DOC-002 p.36](../../../../joi180109supp1_prod.pdf#page=36), continuation [p.37](../../../../joi180109supp1_prod.pdf#page=37). Role PLAN. Columns mean expected patients recruited per month and expected total over 24 months. These are projections, not observed participant flow. The protocol says they derive from the recent iVNIctus trial; this historical derivation does not make them current observed results.

| Centre ID | Centre label | Expected patients/month | Expected total/24 months |
|---:|---|---:|---:|
| 1 | Saint Louis, Paris | 3 | 72 |
| 2 | Pitié-Salpêtrière, Paris | 2 | 48 |
| 3 | IGR, Villejuif | 1 | 24 |
| 4 | Cochin, Paris | 2 | 48 |
| 5 | Paoli-Calmettes, Marseille | 2 | 48 |
| 6 | Bichat, Paris | 1 | 24 |
| 7 | CHU, Angers | 1 | 24 |
| 8 | CHU, St-Etienne | 1 | 24 |
| 9 | CHRU, Lille | 2 | 48 |
| 10 | Cochin, Paris | 1 | 24 |
| 11 | Marseille Nord, Marseille | 1 | 24 |
| 12 | CHU, Caen | 1 | 24 |
| 13 | CHG, Orléans | 1 | 24 |
| 14 | University Hospital, Ghent, Belgium | 1 | 24 |
| 15 | Jules Bordet, Institute, Brussels, Belgium | 1 | 24 |
| 16 | Tenon, Paris | 1 | 24 |
| 17 | Edouard Herriot, Lyon | 2 | 48 |
| 18 | District Hospital, Les Oudairies | 1 | 24 |
| 19 | André Mignot, Le Chesnay | 1 | 24 |
| 20 | Victor Provo, Roubaix | 1 | 24 |
| 21 | Hôpital Brabois, Nancy | 1 | 24 |
| 22 | CHU, Amiens | 1 | 24 |
| 23 | CHU Nicolle, Rouen | 2 | 48 |
| 24 | CHU, Nantes | 1 | 24 |
| 25 | CHU, Grenoble | 1 | 24 |
| 26 | CHU, Montpellier | 1 | 24 |
| Printed total | 26 CENTRES | 34 | 816 PATIENTS |

Quantity joins: projected recruited total ↔ planned sample size S-P2-013; month duration ↔ p.47/p.51 recruitment timing. No displayed interval, P value or test attached to this planning table.

### N-P2-002 — Additional centres

[p.37](../../../../joi180109supp1_prod.pdf#page=37), lines 536–538: 14 additional Grrr-OH centres invited; responses awaited. Administrative projection distinct from the 26 confirmed table rows; no implied addition to an observed analysis denominator.

### N-P2-003 — Recruitment and staffing feasibility

[p.47](../../../../joi180109supp1_prod.pdf#page=47), lines 703–711: each ICU admits at least 50 immunocompromised patients/year on average; 26 centres to recruit 1–2 patients/month over 24 months; prior iVNIctus recruitment completed 6 months earlier than expected (historical). Workload at inclusion at least 1 hour/day, then 30 minutes on each subsequent study day; research assistant allocation 1 day/centre/week. Meeting date July 2, 2015 is administrative rationale, not outcome timing.

### N-P2-004 — Collection and monitoring quantities

[p.56](../../../../joi180109supp1_prod.pdf#page=56), lines 835–848: one CRT collects data in two ICUs; collection once daily Monday–Friday; weekend/holiday collection in real time or next working day depending on site resources; five investigator responsibilities. [p.57](../../../../joi180109supp1_prod.pdf#page=57), lines 865–871: six monitoring items—eligibility, consent, oxygen need, control oxygenation device, primary endpoint, secondary endpoints. These are operational quantities, not trial outcome observations.

## Statistical design and endpoint inventory

| Local key | Exact PLAN locations | Complete extracted specification | Matching main-paper semantic key |
|---|---|---|---|
| S-P2-001 | pp.38 lines 540–542;39 lines 561–568;46 lines 682–684;49 lines 731–734 | Primary objective/endpoint: HFNO noninferiority to usual-care oxygenation for all-cause day-28 mortality in hypoxemic critically ill immunocompromised patients. Noninferiority randomized active-controlled design; rationale includes benefits other than efficacy. | Primary endpoint, hypothesis direction, day-28 mortality, comparison arms. |
| S-P2-002 | pp.39 lines 573–580;40 lines 581–594/Figure 4;41 lines 595–596 | Margin determined before study onset. One-sided CI. Figure x axis: Difference in Efficacy (New Treatment Minus Active Control); zero at reference, negative side active control better, positive side new treatment better. Noninferiority-margin vertical dashed line left of zero. Top lower confidence limit left of margin: noninferiority not demonstrated. Bottom lower limit right of margin: noninferiority demonstrated. Both intervals extend right to infinity; no numeric margin scale or point estimate in this illustration. Trial result defined by lower one-sided confidence bound, not point estimate. Figure adapted from Kaji and Lewis JAMA 2015, source reference 65. | Planned noninferiority contrast, interval sidedness, decision rule. |
| S-P2-003 | pp.38 lines 543–559;46 lines 685–698;47 lines 699–700 | All listed secondary objectives hypothesize HFNO superiority. Endpoint-specific details enumerated below. These pages label them secondary; no separate key-secondary hierarchy is specified here. | Outcome names, statuses, scales, time points, subset denominators, secondary results. |
| S-P2-004 | p.42 lines 603–607;51 lines 757–760 | Margin 9%. Exact p.42 decision wording: “Non-inferiority of HFNO will thus be demonstrated if the lower boundary of the 95% CI is less than 9%.” p.51 refers to one-sided confidence interval of main outcome. Secondary comparisons are superiority tests. No normalization of the boundary/direction wording is made in this map. | Margin, confidence level, criterion, planned versus reported hypothesis. |
| S-P2-005 | p.42 lines 608–610 | Eligible at any stage of ICU stay while needing oxygen supplementation. “All randomized patients” included in full analysis set on intent-to-treat basis. | Analysis population and denominator. |
| S-P2-006 | pp.42 lines 612–617;43 lines 618–631 | Adult; immunosuppression by immunosuppressive drug, steroid duration >3 months or dose >0.5 mg/kg/day, solid-organ transplant, solid tumour, hematological malignancy or HIV; ICU admission for any reason. Oxygen need if one or more: respiratory distress with rate >30/min, cyanosis, laboured breathing, SpO2<90%, expected deterioration during procedure. Written patient/proxy consent. DNI patients eligible. Excluded: end-of-life ICU admission, refusal, hypercapnia with formal NIV indication, isolated cardiogenic pulmonary oedema with formal NIV indication, pregnancy/breastfeeding, anatomy preventing nasal cannula, no French statutory healthcare coverage. | Eligibility thresholds, DNI subgroup, population definition. |
| S-P2-007 | pp.43 lines 633–638;44 lines 639–645 | Open randomized comparison of two strategies. Control usual practice/best standard of care using any usual-care device or combination: nasal oxygen, mask ± reservoir, ± Venturi, NIV. Target SpO2≥95 (printed without percent on line 639). HFNO prohibited. NIV reasons recorded in eCRF. ICU discharge allowed with SpO2≥95% at oxygen <2 L/min. iVNIctus no difference in mortality/intubation is historical rationale without printed numerical result here. | Randomized comparator, NIV permission, oxygen targets, discharge criteria. |
| S-P2-008 | p.44 lines 647–657 | Experimental supplemental oxygen only continuous HFNO except stated intolerance exception. Start 50 L/min at FiO2 100%; if SpO2 target not reached increase to 60 L/min; taper FiO2 to SpO2≥95; minimum flow 40 L/min. Use during laryngoscopy and immediately after extubation, and before/during/after all ICU procedures. Decrease flow for discomfort until relieved. Significant prong discomfort/skin breakdown permits temporary Venturi mask until HFNO reusable; otherwise neither NIV nor standard oxygen. | HFNO dose/intensity, target, duration/use windows, treatment crossover/adherence. |
| S-P2-009 | p.45 lines 658–664 | Stop HFNO on clinical improvement of respiratory distress, PaO2/FiO2>300, and ability to sustain SpO2≥95% with oxygen <2 L/min through low-flow device. HFNO at ICU admission allowed. Intubated patients eligible immediately after extubation. NIV prohibited in experimental group; rationale cites higher mortality with HFNO+NIV in FLORALI (historical, no quantitative estimate here). | Intervention stopping rule, eligibility timing, treatment duration/NIV permission. |
| S-P2-010 | pp.45 lines 666–677;46 lines 678–680 | Randomization stratification: PaO2/FiO2<200 versus ≥200 at randomization; additional organ dysfunction beyond respiratory failure according to SOFA definition. Treatment-by-subset interaction may consider these strata. Four other predefined, unstratified subgroups with scheduled interaction tests: intubation after randomization/HFNO during intubation; HFNO after extubation; intubated in either group; DNI. Specific outcome pairings below. p.46 states interaction tests of between-arm benefit in ICU mortality for all these subsets. | Prespecified strata/subgroups, interaction analyses, subgroup endpoint/time pairing. |
| S-P2-011 | p.49 lines 724–736 | Noninferiority demonstration would support HFNO preference for comfort, dyspnea relief and workload benefits; all secondary endpoints hypothesize HFNO better than usual care. Failure to show 28-day mortality noninferiority requires analysis of reasons before concluding potential inferiority. No numeric test or result is reported. | Hypothesis interpretation and endpoint hierarchy. |
| S-P2-012 | p.50 lines 738–750 | Electronic eCRF/R randomization, centrally concealed website. Intervention impact assessed at patient level. Exact printed sentence: “The randomisation unit is the centre.” Patients randomized to two parallel groups in 1:1 ratio. Two stratification factors as S-P2-010. Printed number: eight different prespecified randomization lists, balanced fixed-size permutation blocks; size concealed from local investigators. | Randomization/analysis unit, allocation ratio, strata, block design. |
| S-P2-013 | p.51 lines 752–762 | Noninferiority, one-sided main-outcome interval. Historical iVNIctus overall day-28 mortality 26% (usual-care oxygen or NIV) used as input. Margin 9%, alpha 5%, power 80%; planned n=816, 408 per group. Recruitment 24 months; 6 additional months follow-up. No sample-size equation, software routine, attrition allowance, assumed experimental mortality, or numerical clustering parameter specified on this page. | Sample size, event-rate input, alpha/sidedness, power, margin, allocation. |
| S-P2-014 | p.52 lines 766–775 | Central randomization and concealed permutation-block size; primary ITT. Reference analysis date ensures administrative/noninformative right censoring for time-to-failure outcomes not fixed like 28-day mortality. | Primary analysis set, censoring, outcome-time definitions. |
| S-P2-015 | p.52 lines 776–783 | Baseline characteristics compared without formal tests to avoid inflating type I error. Main ITT comparison experimental versus control, full randomized set. Exact primary-hypothesis phrase: “non inferiority of the NIV in terms of 28-day mortality (primary outcome).” All secondary outcomes HFNO superiority to standard oxygen or NIV, with two-sided P values. No additional multiplicity adjustment specified here. | Baseline testing, primary intervention/hypothesis label, secondary sidedness/multiplicity. |
| S-P2-016 | p.53 lines 784–785 | Secondary and exploratory comparisons of primary endpoint seek treatment-by-covariate interactions for subsets above. | Prespecified primary-endpoint subgroup/exploratory analyses. |
| S-P2-017 | p.53 lines 786–787 | Per-protocol analysis performed; noninferiority required in both ITT and PP analyses. No PP membership rule on this page. | Sensitivity/PP population and joint noninferiority requirement. |
| S-P2-018 | p.53 lines 789–791 | “No interim analysis will be performed.” Final analysis starts after planned number enrolled. | Interim/stopping/final-analysis trigger. |
| S-P2-019 | p.53 lines 795–798 | Full set for main primary analysis: all randomized except those withdrawing consent; patients analyzed in assigned arm. Exact trailing wording retained: “except those who withdraw consent, who are analysed in the arm thy were allocated to.” | Analysis set, consent withdrawal, allocation-based analysis. |
| S-P2-020 | p.53 lines 800–804 | Missing primary outcome not expected; if present, time-to-event methods use contribution to failure-time distribution until loss to follow-up or study withdrawal, using competing-risk estimates. No competing event specifically named in this missing-primary-outcome paragraph. | Missing outcome handling, censoring and estimator. |
| S-P2-021 | p.54 line 805 | Missing predictor values imputed by multiple-imputation techniques. No imputation count or model named here. | Missing covariates and imputation. |
| S-P2-022 | p.54 lines 808–812 | Primary endpoint binary alive/dead at day 28 after complete follow-up. Printed effect label “relative risk of hospital death” experimental versus control, with 95% CI. Analyses adjusted on potential confounders performed; covariates and fitting model not named in this paragraph. | Primary endpoint/event definition, RR contrast, confidence level, adjusted analysis. |
| S-P2-023 | p.54 lines 812–814 | Intervention-by-subset interactions tested with Gail and Simon statistics; significant interaction triggers analyses separately in each subset. Threshold for significant interaction not specified here. | Interaction statistic and subgroup decision rule. |
| S-P2-024 | p.54 lines 816–821 | Competing-risk endpoints include intubation, ICU-acquired infection, time to clear infiltrates and reintubation. Cumulative incidences account for competition with death or discharge alive from ICU; compare using Gray test. Potential-confounder adjustment uses cause-specific Cox models. No covariate list specified here. | Intubation/infection/reintubation/infiltrate models, competing events, Gray test, adjusted hazard model. |
| S-P2-025 | p.54 lines 822–824 | ICU stay analyzed overall and separately among survivors and dead patients. Exact estimator attribution: “The former analysis will be based on Kaplan Meier estimate while the later on the competing-risk estimator, as described above.” | ICU stay population, censoring, estimator. |
| S-P2-026 | p.55 lines 825–830 | Longitudinal oxygenation, dyspnea and comfort analyzed using joint models accounting for right censoring. All analyses SAS and R; software versions absent. | Longitudinal repeated measures/model and censoring. |
| S-P2-027 | p.56 lines 834–845 | Process-of-care delivery in each patient defined by at least one process-of-care indicator plus no contraindication to that care item. Daily weekday collection; weekend/holiday real time or next working day. Main collected-data list referred to Appendix 1 outside this shard. | Measurement schedule and care/adherence definition. |
| S-P2-028 | p.57 lines 852–871 | Screen all ICU immunocompromised patients needing oxygen; patient/proxy written consent. Incompetent eligible patients included and asked for continuation consent upon regained competence. Provide assigned device; complete missing data. Monitoring includes primary and secondary endpoints. | Eligibility, consent/withdrawal population, adherence and data completeness. |
| S-P2-029 | pp.59 lines 898–906;60 lines 907–915 | Safety definitions detailed below. Safety surveillance described during ICU stay, adverse events as medical events during study. | Safety endpoint definition and ascertainment period. |
| S-P2-030 | pp.60 lines 917–927;61 lines 928–934 | Safety reporting definitions and timing detailed below. | Safety event inclusion/attribution and reporting windows. |
| S-P2-031 | p.61 lines 931–934 | Printed DSMB statement: “The Data Safety and Monitoring Board will also review all adverse events during scheduled interim analyses.” Periodic adverse-event-review written summaries distributed for respective IRBs. No efficacy boundary, interim count or interim sample size on this page. | Interim safety review specification. |

### Secondary outcome and subgroup dictionary (S-P2-003 and S-P2-010)

Source [p.38](../../../../joi180109supp1_prod.pdf#page=38), [p.45](../../../../joi180109supp1_prod.pdf#page=45), [p.46](../../../../joi180109supp1_prod.pdf#page=46), [p.47](../../../../joi180109supp1_prod.pdf#page=47). All are PLAN. Direction listed is the hypothesized benefit, not an observed result.

| Outcome | Planned status and direction | Measure/time/subset details |
|---|---|---|
| Intubation | Secondary; lower with HFNO | Proportion requiring invasive mechanical ventilation, days 3 and 28. |
| Patient comfort | Secondary; better | VAS score; no numeric range or specific measurement schedule in these endpoint paragraphs. |
| Dyspnea | Secondary; less | VAS and Borg scale; no numeric range in these pages. |
| Respiratory rate | Secondary; lower | Rate; threshold >30/min occurs in eligibility, not endpoint cutpoint definition. |
| Oxygenation | Secondary; better | Continuous SpO2 monitoring; lowest SpO2 from D1–D3; PaO2/FiO2 on D1, D2, D3. Objective paragraph says lowest SpO2 and PaO2/FiO2 from day 1 to day 3. |
| ICU stay length | Secondary; shorter | Overall and survivors/dead separately in analysis section; p.54 estimators as S-P2-025. |
| ICU-acquired infections | Secondary; lower incidence | ICU-acquired event, competing risks with death/discharge alive. |
| Pulmonary infiltrates | Secondary; faster resolution | Chest X-rays, Murray score; time to clearing, competing-risk analysis. |
| Oxygen-free and ventilation-free survival | Secondary; higher | p.38 “survival rates on day 28”; p.46 “survivals [days] by day 28.” Preserve both measure wordings for matching. |
| Reintubation | Secondary; lower | Patients extubated during study period. Subgroup paragraph specifically patients managed with HFNO after extubation. |
| Lowest SpO2 during intubation | Secondary; higher median | p.38 “Higher median value of the lowest SpO2 during intubation”; p.46 “Lowest median SpO2 during intubation,” patients intubated during study. Subgroup paragraph: median lowest SpO2 plus PaO2/FiO2 60 minutes after intubation, intubation after randomization with HFNO during procedure. |
| Mortality after intubation | Secondary; no higher mortality | p.38 absence of higher mortality in patients intubated after HFNO versus controls; p.47 mortality after HFNO versus control; p.45 subgroup intubated in both groups, D-28 mortality to assess possibly delayed intubation. |
| DNI outcomes | Secondary endpoint line, subgroup interest | Intubation rate, survival, comfort in DNI patients. |
| Patient and physician satisfaction | Secondary; better | VAS in objective paragraph, named without scale in endpoint continuation. |

The subgroup section also names both randomization strata as potential treatment-by-subset interactions, and p.46 assigns ICU mortality benefit as the interaction target for all these subsets. The statistical section additionally describes interactions of the primary endpoint as secondary/exploratory (p.53) and Gail–Simon testing followed by subset analyses if significant (p.54). These are mapped as distinct source statements without selecting an intended replacement wording.

### Safety endpoint definitions and operational decisions (S-P2-029 to S-P2-031)

Source [p.59](../../../../joi180109supp1_prod.pdf#page=59), [p.60](../../../../joi180109supp1_prod.pdf#page=60), [p.61](../../../../joi180109supp1_prod.pdf#page=61). Adverse event: any untoward medical event occurring during study. Unanticipated adverse event: nature, severity or frequency inconsistent with existing procedure-risk information. Serious adverse event: death, life-threatening event, hospitalization or prolongation, persistent/significant disability/incapacity, congenital anomaly, or medically important event requiring intervention to prevent listed outcomes. Relatedness classes: possibly, probably, clearly caused versus unrelated or unlikely related. Unanticipated non-adverse-event problems include overdose, eligibility deviations or failure to follow withdrawal criteria.

Report events only if principal investigator judges them unanticipated, serious, or possibly/probably/clearly intervention-caused. Investigators report nondeath adverse events to local IRB/clinical coordinating centre within 5 working days; locally occurring unanticipated possibly/probably/clearly related deaths within 24 hours; unanticipated other problems within 5 working days. Coordinating centre reports serious unexpected study-related events to DSMB within 7 calendar days by telephone/fax and in writing within 15 calendar days. DSMB also reviews all adverse events during scheduled interim analyses and distributes periodic summaries. No numeric efficacy-stopping criterion is specified in these pages.

## Evidence accounting and limitations

32 unique physical source pages mapped; 32 reusable-backed; 0 fresh-required; 0 omitted; 0 scientific-coverage gaps. Four numeric/operational relationship keys and 31 statistical/design relationship keys are recorded, including the complete 26-row recruitment table, complete secondary-outcome dictionary, and Figure 4 geometry. Four page units have exclusively administrative content without an applicable statistical item (33–35 and 58); page 48 has only regulatory usual-care description; three bibliography pages (62–64) contain no applicable quantitative trial relationship. Other operational pages are opened and their ascertainment/population/safety content is retained. No page was excluded because an earlier extraction or preview classified it as irrelevant.

Source-dependent limitations: this initial protocol shard does not itself name all covariates, PP membership rules, imputation counts, joint-model components or a sample-size computation formula. These are faithfully recorded absences in this assigned scope, not claims about the complete package. Comparator main-paper pages and later-plan versions belong to other disjoint mapping scopes. Figure 4 is an illustrative hypothesis diagram, not a trial result display; it has no numeric interval endpoints. No cached workbook value/formula ambiguity exists because there is no workbook source. No OCR or translation was necessary for scientific content in this shard; administrative French footer text establishes version identity only.
