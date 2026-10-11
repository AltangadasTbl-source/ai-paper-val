# Support quantitative evidence map — Workflow 1.6.2

Scope: DOC-002, joi180070supp1_prod.pdf, PDF pp. 1–25 (PLAN); DOC-003, joi180070supp2_prod.pdf, PDF pp. 1–9 (REPORT). Mapped: 34/34 pages. Reusable-backed: 34; fresh-required: 0. This artifact reconstructs evidence without selecting findings or candidates. Relationship-ready keys below are local matching keys; final N/S identifiers belong to the checker inventory.

Method: read every page of the canonical reusable Acrobat COM layout text, using native text and canonical page images as locators; curator's current Poppler 25.03.0 per-page source identity/fitness checks establish supplied-source correspondence. Visually inspected reusable images DOC-002 pp. 5, 9, 12, 13, 18, 19 and DOC-003 pp. 6, 8, including every image-only protocol diagram. No derivative was produced or changed by this mapper. Compute device: CPU. Canonical assets are .ai_paper_validation/review_1_5_2/preprocessing/layout_text/DOC-002.txt and DOC-003.txt; corresponding native_text and rendered_pages/DOC-00N-pNN.png are locators. Historical image renderer/version is unrecorded. TSV maps use literal backslash-t separators. Exact source remains the final authority. No old scientific audit output was read.

## Complete page coverage

| Source/page | Content inspected | Mapping outcome |
|---|---|---|
| DOC-002 p.1 | Protocol title, organization, date 2014/4/17 | PLAN identity; no numeric result |
| DOC-002 p.2 | Participating investigator/hospital names | Administrative list; no result-relevant numeric relationship |
| DOC-002 p.3 | Background and study motivation | Historical annual stroke-care cost 5.76 billion US dollars; not a trial result or design input |
| DOC-002 p.4 | Aim and design | PLAN-DESIGN, PLAN-STATUS |
| DOC-002 p.5 | Figure 1, entire image-only flow diagram | PLAN-FLOW |
| DOC-002 p.6 | Cluster network and Table 1 beginning | PLAN-ELIGIBILITY |
| DOC-002 p.7 | Table 1 completion, eligibility narrative, randomization | PLAN-ELIGIBILITY, PLAN-RANDOMIZATION |
| DOC-002 p.8 | Randomization/blinding completion and intervention | PLAN-RANDOMIZATION, PLAN-INTERVENTION |
| DOC-002 p.9 | Figure 2 and clinical-pathway description | PLAN-INTERVENTION; form/manual illustration inspected |
| DOC-002 p.10 | Four written care protocols | PLAN-INTERVENTION, PLAN-MEASURES |
| DOC-002 p.11 | Coordinator and monitoring/feedback system | PLAN-INTERVENTION |
| DOC-002 p.12 | Figure 3 and cycle description | PLAN-MONITORING |
| DOC-002 p.13 | Figure 4, primary outcomes, Table 2 acute measures | PLAN-CYCLES, PLAN-STATUS, PLAN-MEASURES |
| DOC-002 p.14 | Table 2 discharge measures, Table 3 beginning | PLAN-MEASURES |
| DOC-002 p.15 | Table 3 continuation and eligibility footnote | PLAN-MEASURES, PLAN-DENOMINATORS |
| DOC-002 p.16 | Footnote completion, composite/all-or-none, secondary outcomes | PLAN-DENOMINATORS, PLAN-STATUS, PLAN-FOLLOWUP |
| DOC-002 p.17 | Follow-up ascertainment and sample size | PLAN-FOLLOWUP, PLAN-POWER |
| DOC-002 p.18 | SAP analysis sets, summaries, univariate and GEE methods | PLAN-SAP |
| DOC-002 p.19 | SAP opportunity-level example, Cox, sensitivity and software; ethics | PLAN-SAP, PLAN-SENSITIVITY; no additional numeric ethics result |
| DOC-002 p.20 | Consent, organization, early termination remit | PLAN-FOLLOWUP, PLAN-STOPPING; administrative remainder |
| DOC-002 p.21 | Prospective data collection, 20% audit, monthly review; references 1–5 | PLAN-DATAQUALITY; references have no applicable trial relationship |
| DOC-002 p.22 | References 6–11 | Explicit no-applicable trial result/design unit; external historical counts not imported |
| DOC-002 p.23 | References 12–19 | Explicit no-applicable trial result/design unit |
| DOC-002 p.24 | References 20–27 | Explicit no-applicable trial result/design unit |
| DOC-002 p.25 | Reference 27 completion, references 28–29 | Explicit no-applicable trial result/design unit |
| DOC-003 p.1 | Supplement title and content index | REPORT identity; no quantitative result |
| DOC-003 p.2 | Entire baseline survey appendix | SUPP-BASELINE |
| DOC-003 p.3 | eTable 1, nine definitions and eligibility footnote | SUPP-MEASURES, SUPP-DENOMINATORS |
| DOC-003 p.4 | eTable 1 footnote completion | SUPP-DENOMINATORS |
| DOC-003 p.5 | Entire eTable 2 and footnote | SUPP-MRS-BASELINE |
| DOC-003 p.6 | Entire eTable 3, twelve event rows | SUPP-VASCULAR |
| DOC-003 p.7 | eTable 3 footnotes | SUPP-VASCULAR-METHOD |
| DOC-003 p.8 | Entire eTable 4, composite and nine individual rows; abbreviations | SUPP-SENSITIVITY |
| DOC-003 p.9 | eTable 4 definitions and adjustment footnote | SUPP-SENSITIVITY-METHOD |

No supplied workbook, DOC/DOCX, CSV, formula, cached workbook value, additional supplement figure, or structured source belongs to this scope. All reference-only pages were opened; no quantitative coverage gap remains.

## Protocol: design, eligibility, intervention, and measurement keys

Source links are relative from this artifact: [protocol](../../../joi180070supp1_prod.pdf#page=4) and [report supplement](../../../joi180070supp2_prod.pdf#page=2).

PLAN-DESIGN / PLAN-RANDOMIZATION — DOC-002 pp.4,7–8: multicenter, 2-arm, open-label, parallel, cluster-randomized controlled trial, blinded adjudication of outcomes, intention-to-treat. Forty Mainland China hospitals; hospital is randomization unit. Stratify by province, hospital grade (secondary/tertiary), baseline stroke-care quality; independent statistician uses SAS 9.3 random number generation; randomized within strata, 1:1 intervention versus standard care. Sequence concealed until intervention assignment; independent outcome evaluators blinded. Matching main keys: Methods Trial Design, Randomization, sample size, analysis population.

PLAN-FLOW — [DOC-002 p.5 Figure 1](../../../joi180070supp1_prod.pdf#page=5): network hospitals → randomization → intervention/usual care → patient recruitment in both arms → exclusions (ineligible; refused to participate) → inpatient data collection → patient 3-,6-,12-month data collection → lost to follow-up → medical record audit → analyzed/excluded from analyses. Intervention box enumerates 1 clinical pathway; 2 written care protocols; 3 quality coordinator; 4 monitoring/feedback system. Diagram contains no realized participant counts, proportions or effect estimates.

PLAN-ELIGIBILITY — [DOC-002 pp.6–7 Table 1](../../../joi180070supp1_prod.pdf#page=6): network context 563 hospitals, 27 provinces and 4 municipalities, about 20 hospitals per province/municipality. Hospital inclusion: network membership; secondary or tertiary public hospital in major urban area; emergency department and neurological wards receiving AIS patients; capacity for IV rt-PA thrombolysis. Hospital exclusion: primary/private/rural hospital; fewer than 10 suspected AIS patients per month. Patient inclusion: older than 18; ischemic stroke within 7 days of index event; direct admission after physician evaluation or arrival through ED; patient/legal representative able to give informed consent; CT/MRI-confirmed event within 7 days of symptom onset. Exclusion: final diagnosis of another cerebrovascular condition (hemorrhagic stroke, TIA, cerebral venous sinus thrombosis, etc.) or noncerebrovascular condition. Narrative requires CT/MRI for every suspected enrolled stroke patient in either arm. Matching main keys: hospital and participant eligibility, randomized and analyzed populations.

PLAN-INTERVENTION — [DOC-002 pp.8–11](../../../joi180070supp1_prod.pdf#page=8): evidence-based clinical pathway, written care protocols, full-time quality coordinator, and monitoring/feedback for AIS performance measures, implemented by local QCI team. Two providers per intervention cluster (neurology director/local investigator and physician/nurse coordinator) attend a 2-day workshop and cascade training with video/slides. Clinical pathway starts on every eligible admission in ED or inpatient ward; daily care plan for first 7 days and discharge; medical/nursing/therapist/discharge activities checked, initialed, dated each day. Figure 2 p.9 illustrates a clinical-pathway form and three protocol covers (IV rt-PA, DVT prevention/management, swallowing screening/assessment/treatment). Tiny clinical checkboxes are background intervention examples; no reported outcome or numeric analysis appears in that illustration. Text p.10 gives IV rt-PA protocol for arrival within 2 h after last seen normal and treatment within 3 h; DVT risk/Wells assessment; swallowing management; evidence-based medications by end of day two and at discharge (antithrombotic, AF anticoagulation, statin, antihypertensive, hypoglycemic). Coordinator assures components used, finds barriers, trains staff. The protocol does not specify a calendar length of randomized implementation; its duration is described by patient batches and monitoring cycles. Matching main keys: randomized intervention components and implementation duration.

PLAN-MONITORING / PLAN-CYCLES — [DOC-002 pp.11–13](../../../joi180070supp1_prod.pdf#page=12): registry-based indicators viewable at any time, recommended weekly; compare with prior performance and anonymized other clusters. After each 30 consecutive patients discharged alive or dead, performance indicators assessed; central Improvement Committee and local QCI conference review and improvement; repeats every 30 patients. Figure 3 p.12: eligible recruitment by independent CRA → data entry by independent CRA → network transmission → central database → centralized follow-up, independent CRO checking, regular quality reporting → feedback → multidisciplinary quality meeting → continuous improvement → care-quality assessment. Decorative chart has no numeric outcome axes. Figure 4 p.13: randomization; intervention begins at start; FOUR consecutive data-collection batches each labeled 30 patients, with THREE feedback/conference/improvement loops between batches; control arm collection labeled 120 patients. Thus the diagram distinguishes number of patient batches from number of intervening improvement cycles. Matching main keys: intervention cycles, patient target and power.

## Planned outcome hierarchy, definitions, and denominators

PLAN-STATUS — [DOC-002 p.4 aim](../../../joi180070supp1_prod.pdf#page=4), [pp.13–16 primary/secondary outcomes](../../../joi180070supp1_prod.pdf#page=13): aim names adherence to individual, composite and all-or-none measures, and reduction in in-hospital death, new vascular event, disability and all-cause death at 3,6,12 months. Heading “Primary outcomes” says adherence to predefined evidence-based performance measures in AIS patients without contraindications; Tables 2/3 specify nine measures. p.16 expresses adherence as composite or all-or-none. No single measure is designated the sole primary outcome, and no ordered testing hierarchy is printed in this plan. Secondary outcomes: in-hospital death; new clinical vascular event composite (ischemic stroke, hemorrhagic stroke, myocardial infarction, vascular death); disability mRS=3–5; all-cause mortality at 3,6,12 months after initial symptom onset. These are separate status/definition matching keys, not interchangeable outcomes. Matching main keys: primary composite, individual and all-or-none status; all secondary outcome definitions/time points, mRS disability threshold, new vascular composite components.

PLAN-MEASURES / SUPP-MEASURES — DOC-002 Table 2 pp.13–14 and Table 3 pp.14–15; DOC-003 eTable 1 p.3. Item-level definitions:

| Key | Protocol Table 2 | Protocol Table 3 and report eTable 1 |
|---|---|---|
| IV-rtPA | Arrival within 2 h after last seen well, treated within 3 h | Arrival within 2 h after initial symptom onset, treated within 3 h; report explicitly says within 3 h of symptom onset |
| EARLY-ANTITHROMBOTIC | Prescribed within 48 h of admission | Antiplatelet or anticoagulant prescribed within 48 h hospitalization (protocol); within 2 days hospitalization (report) |
| DVT | Within 48 h of admission among at-risk patients | Nonambulatory at-risk patients; by end hospital day two; pneumatic compression, warfarin sodium or heparin sodium |
| DYSPHAGIA | Before any oral intake | Before any oral intake |
| DISCHARGE-ANTITHROMBOTIC | Antithrombotic prescribed at discharge | Same |
| AF-ANTICOAGULATION | Discharge anticoagulation in documented AF | AF or atrial flutter documented during hospitalization |
| LDL-LOWERING | Statin at discharge with LDL ≥100 mg/dL | Lipid-lowering at discharge if LDL ≥100 mg/dL, prior lipid-lowering treatment, OR LDL not documented |
| HYPERTENSION | Discharge antihypertensive in documented hypertension | History of hypertension OR hypertension documented during hospitalization |
| DIABETES | Discharge hypoglycemic in documented diabetes | History of diabetes OR diabetes documented during hospitalization |

PLAN-DENOMINATORS / SUPP-DENOMINATORS — [DOC-002 pp.15–16](../../../joi180070supp1_prod.pdf#page=15), [DOC-003 pp.3–4](../../../joi180070supp2_prod.pdf#page=3): for each applicable measure, exclude documented contraindication/reason for nontreatment (intolerance, excessive adverse-reaction risk, patient/family refusal, terminal illness/comfort care only). Exclude discharge to hospice/another short-term general hospital and departure against advice before end day two. Acute/beginning-hospitalization measures except rt-PA exclude death before end day two. rt-PA excludes missing or unsuitable onset/arrival/treatment timing, started IV t-PA at outside hospital, or initiation after 180 min from onset. Discharge measures exclude inpatient death. Exact source uses a technical timing-quality adjective; it is not an assessment by this review.

PLAN-COMPOSITE / PLAN-ALL-OR-NONE — [DOC-002 p.16 lines216–220](../../../joi180070supp1_prod.pdf#page=16): composite = total interventions performed among eligible patients / total possible interventions among eligible patients; all-or-none = proportion of eligible patients receiving ALL performance-measure interventions. SUPP-BASELINE p.2 repeats the same composite formula. These define denominator types: care opportunities versus patients. Main matching keys: composite descriptive mean/SD, opportunity-level OR, all-or-none patient proportion.

PLAN-FOLLOWUP — pp.16–17,20: blinded personnel with standardized telephone scripts at 3,6,12 months after initial symptom onset; caregiver interviewed if patient communication difficult/unreliable; stroke recurrence and rehospitalization verified with attended hospitals; fatality verified by death certificate from registry/hospital, or when neither available, reports in two consecutive follow-up periods from different agencies. Written patient/family consent for calls. No printed replacement/imputation rule for missing follow-up or mRS is present. Matching main keys: follow-up origin/time points, ascertainment, missing outcome handling.

## Planned statistical methods and power

PLAN-POWER — [DOC-002 p.17 lines241–251](../../../joi180070supp1_prod.pdf#page=17): prerandomization survey mean composite score 80%; detect 5% improvement; 80% power; 5% significance; ICC .02 based on pilot; randomize 40 clusters and approximately 4800 patients; median 120 AIS patients/cluster. Three monitoring/feedback/improvement cycles expected; 30 patients enrolled per cycle per cluster, pointing to Figure 4. Figure 4 has four 30-patient collection batches and three intervening feedback loops, as mapped above. No SD of composite, unequal-size coefficient, explicit equation, attrition allowance,-sidedness, or primary-outcome multiplicity adjustment is printed on this page. Matching main keys: 80% baseline, 5% target improvement, power, alpha, ICC, 40×120=4800, cluster count, survey estimates and cycle count. Missing inputs are source-description facts, not findings.

PLAN-SAP — [DOC-002 pp.18–19](../../../joi180070supp1_prod.pdf#page=18): intention-to-treat. Hospital/patient baseline characteristics assess cluster differences and identify possible control variables for final models. Categorical proportions; normally distributed continuous mean/SD; skewed continuous median/IQR. Univariate χ² for categorical; Student t or Mann–Whitney U for continuous. Multivariate generalized estimation equation accounting for within-hospital correlation, intervention versus control at patient/hospital levels, proportions and quantitative variables. Qualitative effects: population-average OR; quantitative: mean difference, both 95% CI. Composite analysis: every eligible care opportunity contributes one binary observation (1 met,0 not met). Example: eligible for 5 of 7 performance measures, 3 received → 5 observations, three 1s/two 0s. Preserve printed example's “7” separately from the nine item definitions; it is an illustrative example rather than realized analyzed denominator. No named working correlation/link function/fixed list of covariates appears in the SAP. Matching main keys: GEE, clustering, patient versus opportunity analysis unit, ORPA/mean difference, adjustment list, 95% CI and univariate tests.

PLAN-EVENT-ANALYSIS — DOC-002 p.19 lines280–282: vascular events and mortality at discharge and at 3,6,12 months after initial symptom onset displayed by Kaplan–Meier curves, compared using proportional-hazards Cox models. No printed frailty/robust variance specification, hazard-ratio confidence formula, or model for disability appears here. Matching main keys: Cox/HR, Kaplan–Meier, endpoint/time origin and adjustment.

PLAN-SENSITIVITY — DOC-002 p.19 lines282–284: include patients with contraindications to evidence-based interventions in overall-population denominator. SAS 9.3; internal analysis Beijing laboratory; external statistical verification UNC. No other prespecified subgroup or sensitivity list is printed on pp.18–19 or elsewhere in the 25-page plan. Matching main keys: overall-population performance sensitivity, imputation sensitivity and subgroup prespecification.

PLAN-STOPPING / PLAN-DATAQUALITY — [DOC-002 p.20](../../../joi180070supp1_prod.pdf#page=20): executive committee assesses progress/safety and decisions on early termination, modification, continuation. No numeric interim efficacy/futility boundary, number/timing of statistical looks, alpha-spending scheme, multiplicity rule, NI/equivalence margin or hypothesis is supplied. p.21: prospective independent coordinator data capture, range/logic checks; random 20% recruitment sample checked by independent CRO; monthly hospital/registry data-quality meeting. These administrative checks are distinguished from inferential interim analyses.

## Report supplement: baseline survey

SUPP-BASELINE — [DOC-003 p.2 eAppendix](../../../joi180070supp2_prod.pdf#page=2): before randomization; 20 prospectively included eligible patients per cluster, same patient eligibility and endpoint definitions as randomized phase; independent trained coordinator, chart/file/prescription review, same web capture system. Objective: assess baseline comparability and obtain sample-size inputs. Narrative says no statistically significant composite differences between later-randomized arms, without printed test/CI/P. Intervention/control percentages:

| Matching key | Intervention % | Control % |
|---|---:|---:|
| Composite | 80.2 | 79.5 |
| IV-rtPA <2 h | 22.6 | 13.0 |
| Early antithrombotics | 95.4 | 88.4 |
| Dysphagia screening | 79.6 | 88.1 |
| DVT prophylaxis | 14.4 | 7.8 |
| Discharge antithrombotics | 91.6 | 91.6 |
| AF/flutter anticoagulation | 14.8 | 28.2 |
| LDL lipid lowering | 66.9 | 64.6 |
| Hypertension treatment | 69.4 | 71.2 |
| Diabetes treatment | 83.2 | 78.2 |

No individual numerators/denominators are supplied; do not infer them from 20 per cluster. Matching main keys: baseline cluster survey composite and power assumptions, baseline intervention/control comparability.

## Report supplement: mRS availability baseline table

SUPP-MRS-BASELINE — [DOC-003 p.5 eTable 2](../../../joi180070supp2_prod.pdf#page=5). Columns: one-year mRS available, loss to one-year mRS, P. Counts denote availability strata, not randomized treatment arms. Every fraction/percentage and median/IQR transcribed below.

| Characteristic | One-year mRS available | Loss to one-year mRS | P |
|---|---|---|---|
| Age, years median (IQR) | 65 (56–74) | 64 (56–74) | .81 |
| Male | 2497/3949 (63.2%) | 546/851 (64.2%) | .61 |
| Ischemic stroke history | 1137/3949 (28.8%) | 251/851 (29.5%) | .68 |
| Diabetes | 890/3949 (22.5%) | 196/851 (23.0%) | .75 |
| Hypertension | 2552/3949 (64.6%) | 538/851 (63.2%) | .44 |
| Dyslipidemia | 285/3949 (7.2%) | 62/851 (7.3%) | .94 |
| CAD/previous MI | 512/3949 (13.0%) | 97/851 (11.4%) | .21 |
| AF | 200/3949 (5.1%) | 45/851 (5.3%) | .79 |
| Ever smoking | 1736/3949 (44.0%) | 380/851 (44.7%) | .71 |
| Admission NIHSS median (IQR) | 3 (2–6) | 3 (2–6) | .99 |

Footnote: one-year group has data of one-year modified Rankin Scale; NIHSS range0–42; CAD coronary artery disease; MI myocardial infarction; mRS modified Rankin Scale; ED emergency department; EMS emergency medical service; IQR interquartile range. No test labels in this table. Availability totals provide 3949+851=4800 matching key; inferential method to be matched to main Methods. Main key: one-year mRS missingness and imputation/complete-case populations, not treatment baseline group comparisons.

## Report supplement: individual vascular-event table

SUPP-VASCULAR — [DOC-003 p.6 eTable 3](../../../joi180070supp2_prod.pdf#page=6). Outcome group headed “Secondary outcomes.” Rows at 3,6,12 months; contrast intervention minus control for adjusted absolute difference (percentage points), HR intervention/control; each estimate has its own P column. Every denominator is 2400. Intervals below use an explicit separator to preserve negative signs. Do not combine the two model-estimate columns or substitute crude differences for adjusted values.

| Time, event | Intervention n/N (%) | Control n/N (%) | Adjusted absolute difference % (95% CI) | P difference | Adjusted HR (95% CI) | P HR |
|---|---|---|---|---|---|---|
| 3 mo ischemic stroke | 44/2400 (1.8) | 55/2400 (2.3) | −0.57 (−1.91 to 0.76) | .40 | .89 (.59–1.36) | .59 |
| 3 mo hemorrhagic stroke | 14/2400 (0.6) | 20/2400 (0.8) | −0.35 (−0.92 to 0.22) | .23 | .85 (.40–1.83) | .68 |
| 3 mo myocardial infarction | 3/2400 (0.1) | 5/2400 (0.2) | −0.10 (−0.36 to 0.17) | .48 | .58 (.13–2.67) | .48 |
| 3 mo vascular death | 46/2400 (1.9) | 67/2400 (2.8) | −1.43 (−2.33 to −0.54) | .001 | .62 (.42–.92) | .02 |
| 6 mo ischemic stroke | 74/2400 (3.1) | 102/2400 (4.3) | −1.40 (−2.82 to 0.02) | .05 | .72 (.53–.99) | .04 |
| 6 mo hemorrhagic stroke | 17/2400 (0.7) | 21/2400 (0.9) | −0.25 (−0.80 to 0.30) | .38 | .92 (.46–1.82) | .80 |
| 6 mo myocardial infarction | 8/2400 (0.3) | 8/2400 (0.3) | −0.03 (−0.35 to 0.29) | .86 | .78 (.27–2.24) | .64 |
| 6 mo vascular death | 70/2400 (2.9) | 82/2400 (3.4) | −1.06 (−2.08 to −0.04) | .04 | .78 (.56–1.10) | .16 |
| 12 mo ischemic stroke | 117/2400 (4.9) | 160/2400 (6.7) | −1.84 (−3.45 to −0.23) | .03 | .73 (.57–.93) | .01 |
| 12 mo hemorrhagic stroke | 23/2400 (1.0) | 24/2400 (1.0) | −0.08 (−0.71 to 0.55) | .80 | 1.02 (.55–1.88) | .96 |
| 12 mo myocardial infarction | 11/2400 (0.5) | 14/2400 (0.6) | −0.13 (−0.46 to 0.21) | .45 | .71 (.30–1.67) | .43 |
| 12 mo vascular death | 91/2400 (3.8) | 125/2400 (5.2) | −1.94 (−3.26 to −0.62) | .004 | .71 (.54–.94) | .02 |

SUPP-VASCULAR-METHOD — [DOC-003 p.7 footnotes](../../../joi180070supp2_prod.pdf#page=7): patients can have different vascular events, so sum of event counts exceeds number of patients with any new vascular event during follow-up. Both adjusted columns carry footnote a. Patient adjustment: age, gender, history of ischemic stroke, hypertension, diabetes, hyperlipidemia, AF, CAD/previous MI, ever smoking, admission NIHSS. Hospital adjustment: grade, region, stroke unit, teaching status, number neurological ward beds. No printed test statistic or person-time appears. Main matching keys: new vascular-event composite counts and definition; component-specific timing; Cox HR and adjusted absolute differences. Within each row the absolute difference/CI/P and HR/CI/P are separate inferential relationships. Across rows count monotonicity and denominator/percentage are numeric relationships.

## Report supplement: overall-population sensitivity table

SUPP-SENSITIVITY — [DOC-003 p.8 eTable 4](../../../joi180070supp2_prod.pdf#page=8). Title specifies adherence to individual performance measures of overall population for sensitivity analysis; includes composite mean/SD plus nine individual rows. The first effect column is adjusted absolute difference % (95% CI), second is adjusted population-average OR (ORPA;95% CI), each with separate P. Contrast intervention versus control. Composite is mean percentage (SD), not n/N.

| Measure | Intervention n/N (%) or mean (SD) | Control n/N (%) or mean (SD) | Adjusted absolute difference % (95% CI) | P difference | Adjusted ORPA (95% CI) | P ORPA |
|---|---|---|---|---|---|---|
| Composite | 85.3 (15.2) | 80.9 (17.1) | 4.20 (1.77–6.63) | <.001 | 1.36 (1.11–1.67) | .003 |
| IV rt-PA 2 Hour | 46/254 (18.11) | 23/238 (9.66) | 5.81 (−4.57 to 16.19) | .27 | 2.60 (.76–8.87) | .13 |
| Early antithrombotics | 2307/2400 (96.1) | 2253/2400 (93.9) | 2.68 (.48–4.87) | .02 | 1.73 (1.05–2.87) | .03 |
| Dysphagia screening | 2255/2328 (96.9) | 2040/2139 (95.4) | 1.72 (−1.95 to 5.40) | .36 | 2.37 (.69–8.18) | .17 |
| DVT prophylaxis | 178/672 (26.5) | 66/606 (10.9) | 14.79 (3.16–26.42) | .01 | 2.09 (.95–4.62) | .07 |
| Discharge antithrombotics | 2272/2400 (94.7) | 2141/2400 (89.3) | 5.32 (.44–10.20) | .03 | 1.89 (.99–3.64) | .05 |
| AF anticoagulation | 63/182 (34.6) | 39/174 (22.5) | 12.90 (−3.51 to 29.3) | .12 | 1.78 (.61–5.14) | .29 |
| Lipid lowering for LDL >100 mg/dL | 1415/1517 (93.3) | 1439/1586 (90.8) | 2.46 (−2.03 to 6.95) | .28 | 1.17 (.61–2.24) | .63 |
| Antihypertensive medication | 1510/1870 (80.7) | 1372/1803 (76.1) | 6.32 (−.58 to 13.21) | .07 | 1.47 (.97–2.23) | .07 |
| Antidiabetic medication | 653/743 (87.9) | 557/688 (81.1) | 6.16 (1.70–10.62) | .007 | 1.59 (1.11–2.23) | .01 |

SUPP-SENSITIVITY-METHOD — [DOC-003 p.9](../../../joi180070supp2_prod.pdf#page=9): IV rt-PA arrival within 2 h after initial symptom onset/treatment within 3 h of onset; early antithrombotics described as within “48 hours2 days” hospitalization; dysphagia prior to oral intake; nonambulatory DVT prevention by end hospital day two. Adjustment footnote a: same patient and hospital list as eTable3. Abbreviations p.8: CI confidence interval, DVT deep vein thrombosis, ICC intracluster correlation, IV intravenous, LDL low-density lipoprotein, ORPA population-average OR, rt-PA recombinant tissue plasminogen activator, SD standard deviation. All individual n/N percent tuples need arithmetic matching; absolute difference/CI/P and OR/CI/P need independent estimate/test matching. Main keys: planned contraindication-inclusive denominator sensitivity; reported primary composite sensitivity; individual performance denominators, GEE ORPA and covariates. There are no additional sensitivity/subgroup numerical results in this supplement.

## Handoff coverage and limitations

The map covers all nine performance definitions item by item, every primary/secondary status definition, all planned analysis and eligibility elements, all four protocol figures, all three protocol tables, baseline appendix (10 percentage pairs), eTable1 definitions/footnote, eTable2 (10 data rows), eTable3 (12 rows with 24 estimate/CI/P triples), and eTable4 (10 rows with 20 estimate/CI/P triples). Therefore there are 44 supplementary effect/CI/P triples and 10 eTable2 P values, plus the SAP/power inferential specifications. Scientific source coverage: DOC-002 25/25; DOC-003 9/9. Administrative and reference-only content has explicit no-applicable records. No new N/S or C identifiers are assigned here; no observation is classified as a finding.

Limitations: historical extraction/image tool versions are unrecorded; canonical page images omit protocol pp.22–25 but complete readable native/layout text covers those reference-only pages. Figure2 miniature clinical form has very small clinical checklist text, inspected as intervention illustration; it contains no effect display or statistical specification, while all result-relevant thresholds/intervention definitions are present in the adjoining protocol text and Tables2/3. Exact-page confirmation is reserved for the evidence rechecker. No OCR was necessary, and no missing tool prevented scientific mapping. No unresolved assigned unit remains.
