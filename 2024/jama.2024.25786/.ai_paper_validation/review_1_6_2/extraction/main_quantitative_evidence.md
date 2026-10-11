# Main quantitative evidence map — Workflow 1.6.2

Status: COMPLETE. Assigned source: DOC-001, REPORT, jama_arleth_2024_oi_240147_1738701765.27201.pdf, all source PDF pages 1–11 (printed pages 479–489). Runtime task: /root/main_mapper; named main quantitative mapper, gpt-6.1-sol/medium. This is extraction only; no candidate judgments are made.

Read completely: QUALITY_CONTROL_SCOPE.md; workflow_1_6_2/review_contract.md; settings.toml; current source inventory, source coverage, evidence asset inventory and tooling record. Reused locator/transcription asset: .ai_paper_validation/preprocessed/DOC-001.txt, page-delimited pypdf native text, historical version unrecorded. Reused spatial assets: full-page DOC-001 renders, historical engine unrecorded; pp. 3,4,6,7,8 visually inspected for flow/table/figure alignment. Every page's full native text was read. No new preprocessing derivative, rendering or OCR was needed. Compute device: CPU. Fresh-required units: none. Scientific coverage gaps: none. Unreported legacy rendering-engine metadata is an asset provenance limitation only.

All R/L pairs below mean restrictive oxygen / liberal oxygen, in that order. A paired row is one relationship linking its two group values and labels; arrays preserve every displayed time-column quantity. Inferential relationships cross-reference count rows rather than duplicate them. MAIN-local IDs below are mapping group IDs; authoritative global N and S IDs are assigned by later checkers. MAIN-N001–MAIN-N066: 66 numeric/reporting relationships. MAIN-S001–MAIN-S034: 34 inferential/statistical relationships. Total: 100 relationship records. Locations are source PDF pages, never printed-page offsets.

## Page coverage

| Source page | Mapped content | Applicability |
|---|---|---|
| 1 | Abstract: intervention, population, outcomes, primary estimates, adverse events | Applicable |
| 2 | Key Points; trial design, interim analyses, eligibility, randomization | Applicable |
| 3 | Figure 1 all nodes/branches; intervention doses | Applicable |
| 4 | Entire Patient Characteristics Table, all rows/footnotes; sampling windows and endpoint definitions | Applicable |
| 5 | Complete analysis specification, sample-size inputs, population narrative | Applicable |
| 6 | Figure 2 all outcomes; results narrative; intervention exposure | Applicable |
| 7 | Figure 3 all panels, axes, events/at-risk rows/caption; contextual oxygen thresholds | Applicable |
| 8 | Figure 4 all subgroups, interaction tests, footnotes; exclusions narrative | Applicable |
| 9 | Limitations and conclusions; article administrative information | Applicable to result interpretation and sample-size target; administrative remainder has no applicable quantitative result |
| 10 | Acknowledgments continuation and references 1–37 | No applicable trial-result relationships; citations, years, volume/page numbers are bibliographic quantities |
| 11 | References 38–48 | No applicable trial-result relationships; no omitted results table or figure |

## Numeric and reporting relationships

| ID | Exact location | Quantity, population, labels, units and printed values |
|---|---|---|
| MAIN-N001 | p.1 Abstract design; p.5 Trial Population | Recruitment Dec 7, 2021–Sep 12, 2023; 15 prehospital bases and 5 major trauma centers, Denmark/Netherlands/Switzerland; follow-up 30 days ending Oct 12, 2023 (p.1). |
| MAIN-N002 | p.1 Abstract Results; p.5 Trial Population; p.2 Key Points | 1979 randomized; 1508 completed trial; R750/L758 completed (p.5). Key Points call 1508 randomized adult trauma patients. |
| MAIN-N003 | p.1 Abstract Results | Completed-trial population age median 50, IQR31–65 years; 73% male; median ISS14, IQR9–22. |
| MAIN-N004 | p.1 Abstract Interventions; p.5 Trial Population | Abstract randomized allocation 1:1, R n733/L n724; p.5 primary data 1457 (96.6%), R733/L724, of completed-trial 1508. |
| MAIN-N005 | p.3 Figure 1 screening | 5441 assessed at trauma center; 3462 excluded; 1979 randomized. Caption: prehospital eligibility-assessment information unavailable. |
| MAIN-N006 | p.3 Figure 1 screening exclusions | Hospital stay <24 h767; missed research teams649; age<18 y587; secondary transfer558; other injury than blunt/penetrating359; prerandomization cardiac arrest143; no trauma-team activation89; suspected CO intoxication9; other301. Footnote other includes incompatible coenrollment, prior enrollment, acute medical calls labeled trauma activation, unknown trauma time. |
| MAIN-N007 | p.3 Figure 1 allocation | 2 excluded because envelopes lost; R983/L994 randomized into group branches. |
| MAIN-N008 | p.3 Figure 1 R postrandomization exclusions | 59 excluded: age<18 y12; prior cardiac arrest7; previous inclusion4; Swiss-law consent withdrawal4; secondary transfer3; suspected CO intoxication1; other28. |
| MAIN-N009 | p.3 Figure 1 L postrandomization exclusions | 71 excluded: prior cardiac arrest13; age<18 y10; previous inclusion6; Swiss-law consent withdrawal4; secondary transfer3; other35. |
| MAIN-N010 | p.3 Figure 1 secondary exclusions | R174/L165; secondary survey no/minor injury and expected discharge within <24 h. |
| MAIN-N011 | p.3 Figure 1 intervention | R750/L758 received strategy for 8 h. |
| MAIN-N012 | p.3 Figure 1 follow-up | R17 excluded during 30-day follow-up: consent withdrawal15, lost2. L34: consent withdrawal32, lost2. R733/L724 included primary analysis. |
| MAIN-N013 | p.8 Limitations | Postrandomization exclusions471, either after randomization or secondary exclusions. |
| MAIN-N014 | p.2 Patients | Age≥18 y; blunt/penetrating trauma directly transported, full trauma-team activation, anticipated stay≥24 h. Exclude suspected CO intoxication/prerandomization arrest; secondary exclusions no/minor injury discharge anticipated within24 h. AIS coding≥4 weeks posttrauma. |
| MAIN-N015 | pp.1–3 Oxygen Interventions | 8-hour strategy, R minimum oxygen≥21% targeting SpO2 94%; no oxygen if saturation maintained≥94%. L15 L/min nonrebreather if nonintubated, FiO2 1.0 if intubated in prehospital/resuscitation/transport settings. In operating room/PACU/ICU/ward reduce to12 L/min or FiO2≥0.6 if SpO2≥98%. Abstract summarizes L12–15 L/min or FiO2 0.6–1.0. Brief high oxygen permitted in both groups at physician discretion. |
| MAIN-N016 | p.4 intervention measurements; Table footnote f | Patient location, dose, SpO2 and delivery recorded hourly; arterial blood gases at1 h±30 min and6 h±2 h after randomization. |
| MAIN-N017 | p.4 Table age | R48 (29–64), n749; L51 (33–66), n757; median (IQR), years. Table full group n750/n758. |
| MAIN-N018 | p.4 Table sex | Male R540/748 (72.2%), L555/756 (73.4%); female R208/748 (27.8%), L201/756 (26.6%). |
| MAIN-N019 | p.4 Table active smoker | R161/590 (27.3%), L201/587 (34.2%); p.5 narrative says higher proportion in L. |
| MAIN-N020 | p.4 Table pneumonia on admission | Active treatment R16/728 (2.2%), L10/712 (1.4%). |
| MAIN-N021 | p.4 Table comorbidity total | R347/735 (47.2%), L341/725 (47.0%). Footnote a permits multiple comorbidities, so subsections need not sum. |
| MAIN-N022 | p.4 Table cardiovascular disease | R142/735 (19.3%), L137/725 (18.9%). Definition: hypertension, angina, atrial fibrillation, heart failure, coronary artery disease, other. |
| MAIN-N023 | p.4 Table psychiatric disease | R78/735 (10.6%), L82/725 (11.3%). Substantial psychiatric diagnoses classified as systemic illness in ASA physical status system. |
| MAIN-N024 | p.4 Table lung disease | R60/735 (8.2%), L70/725 (9.7%). COPD, asthma, lung fibrosis, lung cancer, positive COVID-19 admission test, other. |
| MAIN-N025 | p.4 Table other comorbidities | R262/735 (35.6%), L267/725 (36.8%). |
| MAIN-N026 | p.4 Table predominant injury | Blunt R667/749 (89.1%), L678/757 (89.6%); penetrating R82/749 (10.9%), L79/757 (10.4%). |
| MAIN-N027 | p.4 Table initial intubation | R177/750 (23.6%), L184/758 (24.3%), intubated at randomization. |
| MAIN-N028 | p.4 Table site of inclusion | In-hospital R442/750 (58.9%), L451/758 (59.4%); prehospital R308/750 (41.1%), L307/758 (40.6%). p.8 narrative41% enrolled prehospital. |
| MAIN-N029 | p.4 Table injury-to-center time | Median (IQR) minutes R58 (43–75), n633; L55 (40–77), n635. |
| MAIN-N030 | p.4 Table supplemental oxygen before randomization | R333/713 (46.7%), L351/718 (48.9%); prehospital or in-hospital use. |
| MAIN-N031 | p.4 Table oxygen duration before randomization; p.8 Discussion | Median (IQR) min R32 (19–51), n234; L30 (15–53), n247. p.8: one-quarter received supplemental oxygen >50 min before randomization. |
| MAIN-N032 | p.4 Table initial systolic pressure | <90 mm Hg R44/640 (6.9%), L53/646 (8.2%). |
| MAIN-N033 | p.4 Table initial heart rate | >110 beats/min R95/665 (14.3%), L97/673 (14.4%). |
| MAIN-N034 | p.4 Table initial respiratory rate | >24 breaths/min R93/514 (18.1%), L114/549 (20.8%). |
| MAIN-N035 | p.4 Table initial SpO2 | <90% R91/669 (13.6%), L108/674 (16.0%). |
| MAIN-N036 | p.4 Table initial GCS | <9 R113/641 (17.6%), L125/654 (19.1%). Footnote b: range3–15; lower worse neurological function; <9 severe consciousness impairment. |
| MAIN-N037 | p.4 Table head AIS | ≥3 R233/750 (31.1%), L202/753 (26.8%). Footnote c: range0–6, higher worse,≥3 serious injury, classified by certified specialists. |
| MAIN-N038 | p.4 Table thoracic AIS | ≥3 R265/750 (35.3%), L260/753 (34.5%); same AIS footnote. |
| MAIN-N039 | p.4 Table ISS | Median (IQR) R14 (9–22), n749; L14 (9–22), n745. Footnote d: range0–75; higher worse; severe generally>15; certified specialists calculate. Table abbreviation prints Injury Severity Scale; prose uses Injury Severity Score. |
| MAIN-N040 | p.4 Table transport | Ground R583/747 (78.0%), L585/743 (78.7%); helicopter R140/747 (18.7%), L141/743 (19.0%); other R24/747 (3.2%), L17/743 (2.3%). Footnote e: combination ground/helicopter, private vehicle, walk-in, police. |
| MAIN-N041 | p.4 Table destination after resuscitation | Ward R299/741 (40.4%), L331/739 (44.8%); ICU R276/741 (37.2%), L242/739 (32.7%); operating room R166/741 (22.4%), L166/739 (22.5%). |
| MAIN-N042 | p.4 Table PaO2 first blood gas | Hour1±30 min; median(IQR) mm Hg R85 (71–109), n614; L280 (145–390), n614. |
| MAIN-N043 | p.4 Table PaO2 second blood gas | Hour6±2 h; median(IQR) mm Hg R86 (74–101), n490; L230 (128–304), n498. |
| MAIN-N044 | pp.5–6 Oxygenation During Intervention | Nonintubated 8-hour oxygen median(IQR) L/min R0 (0–1), L12 (12–15). Intubated FiO2 median(IQR) R0.28 (0.21–0.36), L0.60 (0.60–0.80). Narrative considerable arterial pressure/saturation separation, refers Table and supplement eFigure. |
| MAIN-N045 | p.6 intervention adherence | Major protocol violations R50 (6.7%), L102 (13.7%); denominators not printed in sentence; pointer supplement eTable3. |
| MAIN-N046 | pp.1,2,6; p.6 Figure2 primary row; p.8 Figure4 all patients | Primary death and/or major respiratory complications within30 days R118/733 (16.1%), L121/724 (16.7%). Key Points16.1% vs16.7%; inference MAIN-S010. |
| MAIN-N047 | p.6 Figure2 death | Within30 days R63/733 (8.6%), L53/724 (7.3%); inference MAIN-S011. |
| MAIN-N048 | p.6 Figure2 major respiratory complications | Within30 days R65/733 (8.9%), L78/724 (10.8%); inference MAIN-S012. |
| MAIN-N049 | p.6 Figure2 hypoxemic episodes | R44/737 (6.0%), L28/737 (3.8%); any hourly SpO2<90% during8-hour intervention; inference MAIN-S013. |
| MAIN-N050 | p.6 Figure2 ICU readmission | R17/368 (4.6%), L18/352 (5.1%); initial hospital admission, not readmission; inference MAIN-S014. |
| MAIN-N051 | p.6 Figure2 sepsis | R19/736 (2.6%), L31/727 (4.3%); initial hospital admission; inference MAIN-S015. |
| MAIN-N052 | p.6 Figure2 surgical site infection | R23/736 (3.1%), L32/724 (4.4%); within30 days; inference MAIN-S016. |
| MAIN-N053 | p.6 Figure2 pneumonia postdischarge | R27/640 (4.2%), L24/620 (3.9%); within30 days; inference MAIN-S017. |
| MAIN-N054 | pp.1,6 adverse events | Atelectasis R27.6%/L34.7%, less frequent R; no numerator or denominator here; references eTable9. Other adverse and serious adverse events described similar/comparable. |
| MAIN-N055 | p.6 outcome-assessor allocation guesses; p.8 Discussion | Correct R50.6%/L51.0%; discussion approximately50%; no counts/denominators here. |
| MAIN-N056 | p.7 Figure3 panel A | Days columns0,5,10,15,20,25,30. R death events15,26,5,4,0,2,1; R respiratory events4,38,17,2,1,2,1; R at risk748,664,636,627,626,622,619. L death6,27,3,3,1,1,2; L respiratory3,40,17,14,3,1,0; L at risk756,663,634,619,614,610,605. Caption Kaplan–Meier primary incidence during30-day follow-up. |
| MAIN-N057 | p.7 Figure3 panel B | Same days. R death events15,30,7,5,1,3,2; R at risk748,699,687,681,680,677,674. L events6,31,7,3,1,3,2; L at risk756,699,686,682,680,676,673. |
| MAIN-N058 | p.7 Figure3 panel C | Same days. R respiratory events4,38,17,2,1,2,1; R at risk748,664,636,630,626,624,619. L events3,40,17,14,3,1,0; L at risk756,663,634,619,612,610,610. |
| MAIN-N059 | p.7 Figure3 all panels | Vertical cumulative incidence,% ticks0,5,10,15,20; horizontal days0–30 in5-day steps; R dark blue, L orange. Direct curve labels: primary L above R at end; death R above L; respiratory L above R. No numerical curve endpoint labels or interval bands printed. |
| MAIN-N060 | p.8 Figure4 intubation subgroup | No R56/558 (10.0%), L50/543 (9.2%); yes R62/175 (35.4%), L71/181 (39.2%). Inference MAIN-S018–MAIN-S020. |
| MAIN-N061 | p.8 Figure4 ICU admission subgroup | No R42/458 (9.2%), L50/481 (10.4%); yes R74/271 (27.3%), L68/238 (28.6%). Inference MAIN-S021–MAIN-S023. |
| MAIN-N062 | p.8 Figure4 TBI subgroup | AIS<3 R45/500 (9.0%), L48/473 (10.1%); AIS≥3 R73/233 (31.3%), L73/202 (36.1%). Footnote a: AIS0–6; head<3 mild,≥3 moderate/severe TBI; isolated brain-injury codes only, excludes neck injuries. Inference MAIN-S024–MAIN-S026. |
| MAIN-N063 | p.8 Figure4 known lung disease subgroup | No R97/667 (14.5%), L105/643 (16.3%); yes R19/59 (32.2%), L14/69 (20.3%). Inference MAIN-S027–MAIN-S029. |
| MAIN-N064 | p.8 Figure4 inclusion-site subgroup | Prehospital R48/303 (15.8%), L54/296 (18.2%); in-hospital R70/430 (16.3%), L67/428 (15.7%). Inference MAIN-S030–MAIN-S032. |
| MAIN-N065 | p.8 Figure4 ISS subgroup | ≤15 R22/380 (5.8%), L19/389 (4.9%); >15 R95/352 (27.0%), L100/329 (30.4%). Footnote b: ISS0–75; below15 mild/moderate,>15 severe; inference MAIN-S033–MAIN-S034. |
| MAIN-N066 | pp.3,5–9 context/interpretation | Pilot R target94% maintained24 h; observational oxygen administration first8–10 h (p.3). Sample-size context pilot rates20%/33%, other mortality6%–12%, ICU pneumonia14%–28% (p.5). Discussion other trial n68, FiO2 80% vs50%,6-month neurological outcome (p.6); other trials SpO2 down to88%, conservative94%–98% (p.7), perioperative FiO2 80% (p.8). Limitations aim5-percentage-point risk reduction;1%–2% clinically relevant; ongoing Mega-ROX40000 ICU patients (p.9). These are supplied contextual claims, not TRAUMOX2 outcome estimates. |

## Inferential/statistical relationships

| ID | Exact location | Complete method or printed inference and linked numeric relationship |
|---|---|---|
| MAIN-S001 | pp.2–3 Methods | Open-label parallel-group superiority randomized trial, blinded primary outcome assessors. Randomization1:1 in variable blocks4,6,8; strata specific prehospital base/trauma center and initial endotracheal intubation. Primary hypothesis restrictive early8-hour strategy reduces composite within30 days. |
| MAIN-S002 | p.2 oversight | Two interim analyses after392 (27.6%) and764 (53.8%) enrolled. No stopping boundary/result printed in main article. |
| MAIN-S003 | p.5 sample size |710/group; total1420; hypothesized dropout3.5%; restrictive10% versus liberal15%;33% relative risk reduction;80% power;5% significance. Trial planned to end30 days after inclusion of1420 evaluable patients. Context MAIN-N066. |
| MAIN-S004 | pp.4–5 outcomes/analysis population | Primary composite death and/or pneumonia (CDC criteria) and/or ARDS (Berlin definition) within30 days; two key secondary outcomes death and major respiratory complications separately. Two independent blinded assessors/site, disagreement discussion then third assessor if needed. Medical-record assessment to hospital discharge within30 days; no information obtained after discharge in those assessments. Modified intention-to-treat all included-patient outcomes, modification secondary exclusion criterion MAIN-N014. Per-protocol primary and key secondary; supplement pointer. |
| MAIN-S005 | p.5 primary/key secondary model | Binary logistic regression OR with95% CI; adjusted for stratification variables inclusion site and initial intubation. Additional analysis adds age, sex, ISS, first available GCS after trauma. Site clustering adjusted via generalized estimating equations with covariance matrix assuming clustering-by-site structure. |
| MAIN-S006 | p.5 missing-data/weighting | Differential dropout late consent withdrawal or unreachable follow-up estimated by logistic regression and adjusted through inverse probability weighting; GEE supplies inference with weighted data; supplement pointer. |
| MAIN-S007 | p.5 exploratory analysis | Same adjustment as primary/key secondary; logistic or linear regression according to outcome type. Exploratory set hypoxemia during8 h, ICU readmission, sepsis, SSI, pneumonia postdischarge. Adverse events atelectasis radiologist identified, airway mucosal irritation healthcare staff noted; serious adverse events death/life threatening/prolonged stay including readmission/disability/congenital anomaly (pp.4–5). |
| MAIN-S008 | p.5 predefined subgroups | Initial intubation, ICU admission, moderate/severe TBI AIS≥3, known lung disease, prehospital/in-hospital inclusion, major trauma ISS>15. Figure4 caption stratification-adjusted ORs; further adjustment in supplement eTable7. |
| MAIN-S009 | p.5 significance/multiplicity/software | Primary/key secondary significance5%,95% CI; tests2-sided. Exploratory P values evaluated against significance level controlling FDR below5%. R4.3.1. Statistician/coauthors blinded; groups A/B; two alternative manuscripts approved before unblinding. |
| MAIN-S010 | pp.1,6 primary narrative; Figure2; p.8 Figure4 all patients | MAIN-N046: OR1.01 (95% CI0.75–1.37), P=.94; absolute difference0.56 percentage points (95% CI−2.70–3.82), Figure2 calls risk difference. Figure2/Figure4 forest axis0.25,1,4; left favors restrictive, right favors liberal. Narrative no significant reduction; subsequent further-adjusted/per-protocol/subgroups similar (p.6). Conclusion repeats pp.1,2,6,8,9. |
| MAIN-S011 | p.6 Figure2 death | MAIN-N047: OR1.28 (0.85–1.92); risk difference1.06 percentage points (−1.21–3.33); no row P printed. |
| MAIN-S012 | p.6 Figure2 respiratory complications | MAIN-N048: OR0.84 (0.59–1.19); risk difference−0.61 percentage points (−3.29–2.08). Narrative secondary components opposing trends, neither significantly different (pp.6,9). |
| MAIN-S013 | p.6 Figure2 hypoxemia | MAIN-N049: OR1.67 (1.02–2.70); risk difference2.40 percentage points (0.17–4.54). |
| MAIN-S014 | p.6 Figure2 ICU readmission | MAIN-N050: OR0.59 (0.26–1.37); risk difference−1.33 percentage points (−4.62–1.95). |
| MAIN-S015 | p.6 Figure2 sepsis | MAIN-N051: OR0.55 (0.30–1.02); risk difference−1.21 percentage points (−2.96–0.54). |
| MAIN-S016 | p.6 Figure2 surgical site infection | MAIN-N052: OR0.50 (0.25–0.99); risk difference−3.04 percentage points (−6.87–0.79). |
| MAIN-S017 | p.6 Figure2 pneumonia postdischarge | MAIN-N053: OR1.06 (0.60–1.85); risk difference0.02 percentage points (−1.99–2.04). MAIN-S013–MAIN-S017 no row P printed; Figure2 caption says OR stratification-adjusted, further adjustments eTables4/5. Narrative no exploratory outcomes significant after multiple-testing adjustment (p.6). |
| MAIN-S018 | p.8 Figure4 intubated No | MAIN-N060: OR1.12 (95% CI0.75–1.67). |
| MAIN-S019 | p.8 Figure4 intubated Yes | MAIN-N060: OR0.90 (0.57–1.41). |
| MAIN-S020 | p.8 Figure4 intubation interaction | P=.48, linked MAIN-S018/MAIN-S019. |
| MAIN-S021 | p.8 Figure4 ICU No | MAIN-N061: OR0.98 (0.64–1.49). |
| MAIN-S022 | p.8 Figure4 ICU Yes | MAIN-N061: OR0.96 (0.63–1.49). |
| MAIN-S023 | p.8 Figure4 ICU interaction | P=.95, linked MAIN-S021/MAIN-S022. |
| MAIN-S024 | p.8 Figure4 AIS<3 | MAIN-N062: OR1.06 (0.68–1.64). |
| MAIN-S025 | p.8 Figure4 AIS≥3 | MAIN-N062: OR0.81 (0.53–1.25). |
| MAIN-S026 | p.8 Figure4 TBI interaction | P=.41, linked MAIN-S024/MAIN-S025. |
| MAIN-S027 | p.8 Figure4 lung disease No | MAIN-N063: OR0.88 (0.65–1.22). |
| MAIN-S028 | p.8 Figure4 lung disease Yes | MAIN-N063: OR1.85 (0.73–4.55); interval continues past plotted maximum4, right arrow. |
| MAIN-S029 | p.8 Figure4 lung disease interaction | P=.15, linked MAIN-S027/MAIN-S028. |
| MAIN-S030 | p.8 Figure4 prehospital | MAIN-N064: OR0.81 (0.51–1.28). |
| MAIN-S031 | p.8 Figure4 in-hospital | MAIN-N064: OR1.19 (0.81–1.79). |
| MAIN-S032 | p.8 Figure4 inclusion site interaction | P=.20, linked MAIN-S030/MAIN-S031. |
| MAIN-S033 | p.8 Figure4 ISS≤15 | MAIN-N065: OR1.33 (0.69–2.56). |
| MAIN-S034 | p.8 Figure4 ISS>15 and ISS interaction | MAIN-N065: OR0.86 (0.60–1.23); interaction P=.25. All Figure4 estimates stratification-adjusted;95% CI; forest0.25/1/4; lower favors restrictive and higher favors liberal; primary outcome within30 days. |

No standard errors, test statistics, explicit person-time denominators, incidence-rate quantities or means/SDs are printed for the TRAUMOX2 trial in this main article. Continuous values here are medians/IQRs, not means/SDs. Figure3 counts are transcribed as labeled, without assigning an unstated interval definition to “No. of events.” No exact curve values were invented from pixels.

## Matching narrative and display locators

- Primary numeric/inferential occurrence: Abstract p.1; Key Points p.2 (rates and conclusion); Outcomes p.6; Figure2 p.6; Figure3 panel A p.7; Figure4 all-patient row p.8; Conclusions p.9. MAIN-S010/MAIN-N046 preserve this relationship.
- Secondary components: abstract p.1 no significant differences; Outcomes p.6 opposing nonsignificant trends; Figure2 death/respiratory p.6; Figure3 B/C p.7; Limitations p.9 opposite directions. MAIN-S011/MAIN-S012 and MAIN-N047/MAIN-N048/MAIN-N057/MAIN-N058 preserve the separate quantities.
- Exploratory outcomes: p.5 names/specification and multiplicity; p.6 Figure2 all five rows and narrative; supplement eTables5/6 pointer. No exploratory row is omitted on significance grounds.
- Oxygen exposure: abstract p.1, intervention pp.2–3, measurement windows/Table p.4, oxygenation pp.5–6, discussion pp.7–8. Protocol/per-protocol pointers pp.5–6 go to supplement eTables3/8; no support content is assigned to this mapper.
- Figure/table labels: Figure1 “Screening, Randomization, and Follow-Up of Patients in the TRAUMOX2 Trial”; unnumbered Table “Patient Characteristics” plus same-page continued section; Figure2 “Patient Outcomes”; Figure3 “Cumulative Incidence of Death and/or Major Respiratory Complications,” panels A composite/B death/C respiratory; Figure4 “Subgroup Analysis of Death and/or Major Respiratory Complications Within 30 Days.”

## Truthful source evidence links

[Source p.1](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=1), [p.2](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=2), [p.3](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=3), [p.4](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=4), [p.5](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=5), [p.6](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=6), [p.7](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=7), [p.8](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8), [p.9](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=9), [p.10](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=10), [p.11](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=11).
