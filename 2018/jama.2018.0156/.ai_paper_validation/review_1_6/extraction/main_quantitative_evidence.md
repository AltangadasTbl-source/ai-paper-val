# Main-paper quantitative evidence map

Scope: DOC-001, `jama_jabre_2018_oi_180004.pdf`, PDF pp. 1–9 (printed pp. 779–787), document role REPORT throughout. All nine pages inspected through complete, source-matched reusable Poppler layout text; no fresh-required units. This map records printed evidence without diagnosing candidates. Local row keys M01–M103 are extraction locators, not registered N/S relationship IDs. There are 103 mapped relationship groups; each group preserves all displayed components, including paired table cells and matching occurrences.

Controls read: QUALITY_CONTROL_SCOPE.md; workflow_1_6/review_contract.md; source_coverage.md; evidence_asset_inventory.md; tooling_record.md. Reused locator: `.ai_paper_validation/review_1_5_2/preprocessing/layout_text/jama_jabre_2018_oi_180004.txt` (historical Poppler, byte match to current Poppler 25.03.0 per inventory). Direct-source alignment confirmation: `pdftoppm -f 6 -l 6 -scale-to 1800 -singlefile -png jama_jabre_2018_oi_180004.pdf .ai_paper_validation/review_1_6/preprocessing/main/page-006`, Poppler 25.03.0; visually inspected PNG confirms both tables, their exact unusual printed values, P-value block placement, and footnotes. No Python extraction, OCR, GPU, external literature, or old scientific audit conclusions used. Source and reused assets unchanged.

## Page coverage

| PDF page | Printed page | Inspection and mapped units | Status |
|---|---|---|---|
| 1 | 779 | Abstract: design, dates, sample/sex/age/completion, primary and secondary results, adverse events, interpretation | COMPLETE |
| 2 | 780 | Key Points; design, centers, allocation, enrollment and eligibility; intervention and rescue definitions | COMPLETE |
| 3 | 781 | Follow-up window, endpoint definitions, all statistical rules and sample-size hypotheses, post-hoc methods | COMPLETE |
| 4 | 782 | All Figure flow boxes and reasons; populations; all outcome/adverse/post-hoc narrative results | COMPLETE |
| 5 | 783 | Every Table 1 row, denominator, unit, percentile label and footnote | COMPLETE |
| 6 | 784 | Every Table 2/Table 3 row/cell and footnote; post-hoc exclusion totals; directly rendered | COMPLETE |
| 7 | 785 | Matching outcome discussion, CPR quantities, reported historical numeric comparisons | COMPLETE |
| 8 | 786 | Conclusions and multiplicity statement; article information/references contain no additional applicable result quantities | COMPLETE |
| 9 | 787 | References only; bibliographic years/volumes/pages are not quantitative scientific results; no applicable additional relationship | COMPLETE |

Evidence links below are relative to this extraction file. PDF page numbers are physical PDF pages. Table row names are exact locators. BMV and ETI columns always retain that order unless explicitly stated otherwise. Percentages printed as % are proportions of patients, not person-time rates. No person-time, standard error or test statistic is displayed anywhere in the assigned main-paper scope.

## Population, design, timing and endpoint definitions

| Key | Source location | Complete printed quantities/definitions and linked occurrences |
|---|---|---|
| M01 | [Abstract p. 1](../../../jama_jabre_2018_oi_180004.pdf#page=1); [Results/Figure p. 4](../../../jama_jabre_2018_oi_180004.pdf#page=4) | Randomized/enrolled total 2043; BMV 1020; ETI 1023. Abstract 2040 (99.8%) completed; results ITT 2040. Key Points p. 2 also 2043. |
| M02 | Abstract p. 1; Table 1 p. 5 | Randomized mean age 64.7 years; 665 women [32%]. Table 1 ITT age and sex mapped separately with changed analysis population. |
| M03 | Abstract p. 1; Methods p. 2 | Enrollment March 9, 2015–January 2, 2017; 22 months; follow-up ended January 26, 2017. |
| M04 | [Methods p. 2](../../../jama_jabre_2018_oi_180004.pdf#page=2) | 2 countries, 20 EMS centers: 15 France, 5 Belgium; minimum ambulance team driver, nurse, emergency physician; 1 or more mobile intensive care units; 2-tiered EMS system. |
| M05 | Methods p. 2 | Allocation 1:1, stratified by center; random-size blocks 4 to 8. Adults aged ≥18 years; exclusions suspected massive aspiration before resuscitation, do-not-resuscitate order, known pregnancy, imprisonment. |
| M06 | Methods pp. 2–3 | BMV initial advanced airway management during CPR; ETI after ROSC or rescue for impossible BMV/massive regurgitation; ETI group difficult-laryngoscopy rescue bougie, laryngeal mask, video-assisted laryngoscopy. Primary rescuers may give BMV before medical team. Transport only stable ROSC at scene. Compression:breath ratio 30:2 before ETI; follow-up at day 28 within 28–35-day window. |
| M07 | [Outcomes p. 3](../../../jama_jabre_2018_oi_180004.pdf#page=3); Abstract; Table 2 footnote b | Primary survival at day 28 with favorable neurological function: CPC ≤2, explicitly CPC 1 or 2; blinded assessors. Secondary survival to admission, day-28 survival irrespective of CPC, ROSC, airway difficulty/failure/regurgitation. |
| M08 | Statistical Analysis pp. 3–4 | ITT all randomized irrespective of treatment/adequacy; PP randomized and treated without major violations/deviations; safety treated according to treatment received; attempted unsuccessful intubation adverse events assigned to ETI. Exact observed population exclusions mapped under flow. |
| M09 | Outcomes p. 3; Table 3 footnotes p. 6 | IDS range 0–infinity; >5 difficult ETI. BMV VAS 0–100 mm (0 no difficulty, 100 maximum), recorded after resuscitation. Han >2 difficult BMV; grades 1 easy, 2 difficult needing oral airway/adjuvant, 3 very difficult needing 2 practitioners, 4 unable to ventilate. |
| M10 | Outcomes p. 3 | Regurgitation event newly regurgitated gastric contents seen below glottis ETI or through mask BMV. CCF defined proportion of each minute receiving compressions; pauses >2 seconds; one center No. 5 Saint Pierre; monitoring ≤15 minutes or until ROSC, automatic Corpuls3. |
| M11 | Statistical Analysis p. 3 | Historical hypothesis registry 650 000; favorable survival BMV 3%, ETI 1.1%; odds ratio described as in favor of BMV 0.38 (95% CI 0.36–0.39). Gueugniaud ETI 2%. Presumed true primary rates BMV 3%, ETI 2%. |
| M12 | Statistical Analysis p. 3 | Absolute NI margin 1%; putative placebo ETI 2%, absent resuscitation null, preserving at least 50% reference effect. 956 per group, 80% power, 95% 2-sided CI, 5000 simulations Newcomb-Wilson score method; recruit total 2000. |
| M13 | Statistical Analysis p. 3 | Primary π bag − π tracheal; 95% 2-sided CI; NI accepted if lower limit higher than −1%; difference test if NI demonstrated. Observed results reported as 1-sided 97.5% CI. |
| M14 | Statistical Analysis pp. 3–4; Table 2/3 footnote a p. 6 | Secondary superiority: χ² on proportions; corresponding 95% CI for ORs and differences; quantitative t or Mann-Whitney according to Gaussian/nongaussian distribution; 2-sided threshold P=.05; no multiplicity adjustment; exploratory. Tables allow χ² or Fisher exact. No individual reported test choice/statistic, SE, or OR for secondary results in main paper. SAS 9.4. |
| M15 | Statistical Analysis pp. 3–4 | Post hoc: hierarchy with center random effect risk difference and 97.5% CI; CCF/pauses center No. 5; ITT exclude prolonged/modified procedures ECMO-CPR/organ donation; ITT consider patients intubated after BMV before ROSC in ETI. |

## Figure patient flow and population accounting

Every row below is [Figure p. 4](../../../jama_jabre_2018_oi_180004.pdf#page=4). Figure footnote a: several reasons may apply to the same patient, for rescue and exclusions. Assessed-for-eligibility total unavailable, explicitly stated. Reasons therefore must not be assumed mutually exclusive.

| Key | Flow unit | BMV printed content | ETI printed content |
|---|---|---|---|
| M16 | Assigned treatment receipt | 1020 randomized; 1014 received BMV; 6 did not | 1023 randomized; 979 received ETI; 44 did not |
| M17 | Reasons did not receive treatment | 2 not in cardiac arrest; 1 directly intubated because massive regurgitation did not allow BMV; 3 immediate medical decisions not to resuscitate | 21 ETI attempted but impossible, received BMV; 14 randomized ETI but received BMV; 9 no resuscitation attempt |
| M18 | ETI no-attempt reasons | Not applicable | 3 directive not to resuscitate; 1 early ROSC; 5 immediate medical decision not to resuscitate |
| M19 | Follow-up/discontinuation | 0 lost to follow-up; 146 rescue intubation; 55 ventilation failure; 100 regurgitation during ventilation | 0 lost to follow-up; 0 discontinued ETI |
| M20 | ITT | 1018 included; 2 excluded not in cardiac arrest | 1022 included; 1 excluded aged <18 years |
| M21 | PP | 995 included; 23 excluded; reasons 2 not in cardiac arrest, 6 did not receive BMV, 1 no insurance, 19 suspected massive aspiration before resuscitation | 943 included; 80 excluded; reasons 1 aged <18, 44 did not receive ETI, 3 no insurance, 1 prisoner, 36 suspected massive aspiration before resuscitation |
| M22 | Safety | 1028 included: 1014 randomized BMV and received BMV +14 randomized ETI but received BMV | 999 included; 24 excluded: 14 randomized ETI but received BMV, 9 no resuscitation attempt, 1 aged <18 |
| M23 | Narrative populations p. 4 | ITT total 2040; PP 995 | PP 943; safety total 2027 = BMV 1028 and ETI 999; center inclusions referenced eTable 1 Supplement 2 |

## Table 1 complete row map

All rows M24–M71 at [Table 1 p. 5](../../../jama_jabre_2018_oi_180004.pdf#page=5). Header ITT BMV n=1018, ETI n=1022. Count rows use header denominators unless a separate n is printed below. Parentheses are percentages for count rows, SD for age, 25th–75th percentile for BMI, IQR for specified other continuous rows. No P values in Table 1. Narrative p. 4 describes characteristics/process balanced except age and psychiatric disorder; no differences considered clinically significant.

| Key | Row/quantity | BMV | ETI |
|---|---|---|---|
| M24 | Age mean (SD), y | 65.7 (15.5) | 63.8 (15.6) |
| M25 | Female, No. (%) | 332 (32.6) | 332 (32.5) |
| M26 | Estimated BMI median (25th–75th percentile) | 26.0 (22.9–29.4) | 26.1 (23.4–29.4) |
| M27 | Hypertension | 337 (33.1) | 358 (35.0) |
| M28 | Coronary artery disease | 194 (19.1) | 189 (18.5) |
| M29 | Diabetes | 185 (18.2) | 199 (19.5) |
| M30 | Tobacco use | 176 (17.3) | 195 (19.1) |
| M31 | Chronic obstructive pulmonary disease | 126 (12.4) | 113 (11.1) |
| M32 | Chronic heart failure | 107 (10.5) | 111 (10.9) |
| M33 | Chronic alcohol abuse | 90 (8.8) | 82 (8.0) |
| M34 | Neurologic disorder | 78 (7.7) | 79 (7.7) |
| M35 | Cancer | 72 (7.1) | 80 (7.8) |
| M36 | Psychiatric disorder | 53 (5.2) | 81 (7.9) |
| M37 | Dementia | 33 (3.2) | 22 (2.2) |
| M38 | Liver disease | 25 (2.5) | 17 (1.7) |
| M39 | Chronic renal failure with dialysis | 25 (2.5) | 23 (2.3) |
| M40 | HIV | 7 (0.7) | 5 (0.5) |
| M41 | Activity limitation denominator | n=934 | n=936 |
| M42 | Good health | 492 (52.7) | 528 (56.4) |
| M43 | Moderate limitation of activity | 255 (27.3) | 254 (27.1) |
| M44 | Chronic disease | 115 (12.3) | 91 (9.7) |
| M45 | Severe restriction of activity | 72 (7.7) | 63 (6.7) |
| M46 | Arrest occurred at home | 776 (76.2) | 811 (79.4) |
| M47 | Etiology of cardiac arrest denominator | n=1014 | n=1015 |
| M48 | Cardiac | 692 (68.2) | 668 (65.8) |
| M49 | Noncardiac medical | 271 (26.7) | 277 (27.3) |
| M50 | Traumatic | 51 (5.0) | 70 (6.9) |
| M51 | Bystander-witnessed cardiac arrest | 719 (70.6) | 708 (69.3) |
| M52 | Bystander-initiated CPR | 487 (47.8) | 512 (50.1) |
| M53 | Bystander-initiated ventilation | 62 (6.1) | 66 (6.5) |
| M54 | EMS-witnessed cardiac arrest | 164 (16.1) | 170 (16.6) |
| M55 | No-flow duration median (IQR), min | 5 (1–11) | 5 (1–12) |
| M56 | Collapse to advanced life support median (IQR), min | 20 (14–28) | 20 (13–29) |
| M57 | Shockable first rhythm | 169 (16.6) | 157 (15.4) |
| M58 | Mechanical chest compression device | 213 (20.9) | 227 (22.2) |
| M59 | Initial cardiac rhythm denominator | n=1016 | n=1020 |
| M60 | Asystole | 729 (71.8) | 743 (72.8) |
| M61 | Pulseless electrical activity | 118 (11.6) | 120 (11.8) |
| M62 | Ventricular fibrillation | 164 (16.1) | 151 (14.8) |
| M63 | Ventricular tachycardia | 5 (0.5) | 6 (0.6) |
| M64 | Epinephrine before hospital arrival | 962 (94.5) | 974 (95.3) |
| M65 | Epinephrine dose median (IQR), mg | 5 (3–9) | 6 (4–9) |
| M66 | Amiodarone | 200 (19.7) | 188 (18.4) |
| M67 | Lidocaine | 11 (1.1) | 13 (1.3) |
| M68 | Fibrinolytic | 15 (1.5) | 21 (2.1) |
| M69 | ECMO-CPR resuscitation | 35 (3.4) | 23 (2.3) |
| M70 | Uncontrolled donation after circulatory death | 12 (1.2) | 21 (2.1) |
| M71 | Table footnotes/definitions | BMI kg/m². Activity good health no functional limitations; moderate mild–moderate due to chronic problem; chronic serious but nonincapacitating; severe includes bedridden/institutionalized. No-flow collapse to basic life support. Uncontrolled donation kidney graft retrieval from non-heart-beating donor after OHCA. | Same definitions apply |

## Primary inferential outcomes and repeated narrative

All differences use BMV minus ETI, proportion difference in percentage points printed as percentages. CI endpoints preserve original precision; infinity is printed, not inferred.

| Key | Source | Population, event counts/proportions | Difference and CI | P/model/narrative |
|---|---|---|---|---|
| M72 | [Abstract p. 1](../../../jama_jabre_2018_oi_180004.pdf#page=1); [Primary Outcome p. 4](../../../jama_jabre_2018_oi_180004.pdf#page=4) | ITT day-28 favorable survival BMV 44/1018 (4.3%), ETI 43/1022 (4.2%) | 0.11% [1-sided 97.5% CI −1.64% to infinity] | P for NI=.11. p. 4 exact wording: “The lower limit of the confidence interval was greater than the threshold of noninferiority, thus noninferiority was not demonstrated.” Record literal relational statement without interpretation. |
| M73 | Primary Outcome p. 4 | Hierarchical center random-effect modeling, primary endpoint | 0.05% [1-sided 97.5% CI −1.70% to infinity] | Very similar estimates; no P printed for this model. |
| M74 | Primary Outcome p. 4; Table 2 CPC cells p. 6 | PP favorable survival BMV 4.3%, ETI 4.2%; PP n=995/943 and CPC 1+2 cells 35+8 /34+6 | 0.08% [1-sided 97.5% CI −1.74% to infinity] | P for NI=.12; described as consistent with ITT. Counts are constituent cells, not independently printed primary numerators. |
| M75 | Key Points p. 2; Discussion pp. 6–7; Conclusions p. 8; Abstract p. 1 | Favorable neurological function at 28 days 4.3% vs 4.2%, NI margin 1% | Inconclusive NI/inferiority | Key Points did not meet margin. Discussion notes assumed higher BMV rate, observed close estimates, possible underpowering; equivalence/superiority needs further research. |

## Table 2 complete secondary/CPC map

All rows at [Table 2 p. 6](../../../jama_jabre_2018_oi_180004.pdf#page=6); difference header “Proportion Difference, BMV(%) − ETI(%) (95% CI)”. Header ITT n=1018/1022; PP n=995/943. Each count row preserves printed percentage. P=.68 and .76 are centered across their respective entire CPC blocks (confirmed direct rendering), not tests solely of CPC 3. Footnote b CPCs 1/2 success primary endpoint; footnote a χ² or Fisher exact.

| Key | Population/outcome | BMV No. (%) | ETI No. (%) | Difference (95% CI) | P |
|---|---|---|---|---|---|
| M76 | ITT survival 28 d | 55 (5.4) | 54 (5.3) | 0.1 (−1.8 to 2.1) | .90 |
| M77 | ITT CPC 1 good cerebral performance | 35 (3.4) | 37 (3.6) | Not printed | CPC block .68 |
| M78 | ITT CPC 2 moderate cerebral disability | 9 (0.9) | 6 (0.6) | Not printed | Same block |
| M79 | ITT CPC 3 severe cerebral disability | 4 (0.4) | 7 (0.7) | Not printed | Same block |
| M80 | ITT CPC 4 coma/vegetative | 7 (0.7) | 4 (0.4) | Not printed | Same block |
| M81 | ITT CPC 5 death | 963 (94.6) | 968 (94.7) | Not printed | Same block |
| M82 | ITT survival hospital admission | 294 (28.9) | 333 (32.6) | −3.7 (−7.7 to 0.3) | .07 |
| M83 | ITT ROSC | 348 (34.2) | 397 (38.9) | −4.7 (−8.8 to −0.5) | .03 |
| M84 | PP survival 28 d | 54 (5.4) | 51 (5.4) | 0.1 (−10 to 9.7) | .99 |
| M85 | PP CPC 1 good cerebral performance | 35 (3.5) | 34 (3.5) | Not printed | CPC block .76 |
| M86 | PP CPC 2 moderate cerebral disability | 8 (0.8) | 6 (0.6) | Not printed | Same block |
| M87 | PP CPC 3 severe cerebral disability | 4 (0.4) | 7 (0.7) | Not printed | Same block |
| M88 | PP CPC 4 coma/vegetative | 7 (0.7) | 4 (0.4) | Not printed | Same block |
| M89 | PP CPC 5 death | 941 (94.6) | 892 (94.6) | Not printed | Same block |
| M90 | PP survival hospital admission | 289 (29.1) | 312 (33.1) | −4.0 (−7.6 to 0.6) | .055 |
| M91 | PP ROSC | 342 (34.4) | 377 (30.0) | −5.6 (−9.9 to −1.3) | .01 |

Repeated outcomes: M76/M82 Abstract p. 1 and Secondary Outcomes p. 4 repeat identical counts, percentages, differences and CIs, without table P=.90/.07; narrative says survival measures not significantly different. M83 Secondary Outcomes p. 4 repeats 348/1018 (34.2%), 397/1022 (38.9%), −4.7% [−8.8% to −0.5%], P=.03; describes ETI ROSC significantly greater. Narrative p. 4 “These results were not modified in the per-protocol analysis (Table 2).” Discussion p. 7 repeats significantly higher ETI ROSC and no difference overall day-28 survival.

## Table 3 adverse event and scale map

[Table 3 p. 6](../../../jama_jabre_2018_oi_180004.pdf#page=6), safety population according to actual treatment; header “Absolute Difference, BMV(%) − ETI(%) (95% CI)”; χ²/Fisher footnote. NA explicitly means not applicable. Abstract p. 1 and Adverse Events p. 4 repeat all difficulty/failure/regurgitation numbers, differences, CIs and P values exactly as mapped.

| Key | Outcome/scale | BMV | ETI | Difference (95% CI) | P |
|---|---|---|---|---|---|
| M92 | BMV VAS median (IQR), mm | 20 (5–55) | NA | NA | NA |
| M93 | IDS median (IQR) | NA | 1 (0–4) | NA | NA |
| M94 | Rate of airway difficulty No./total (%) | 186/1027 (18.1) | 134/996 (13.4) | 4.7 (1.5–7.9) | .004 |
| M95 | BMV/ETI failure No./total (%) | 69/1028 (6.7) | 21/996 (2.1) | 4.6 (2.8–6.4) | <.001 |
| M96 | Complications denominators; regurgitation gastric content No. (%) | n=1027; 156 (15.2) | n=999; 75 (7.5) | 7.7 (4.9–10.4) | <.001 |
| M97 | Mainstem intubation | NA | 20 (2.0) | NA | NA |
| M98 | Recognized esophageal intubation | NA | 102 (10.2) | NA | NA |
| M99 | Dental injury; extubation | NA; NA | 7 (0.7); 5 (0.5) | NA; NA | NA; NA |

M97 footnote d detected in field by auscultation. M98 footnote e no unrecognized esophageal intubations. Definitions/scale bounds in M09. Discussion p. 7 repeats qualitative higher BMV regurgitation and failure; no additional exact outcome counts.

## Post hoc and historical narrative quantities

| Key | Source | Complete printed relationship |
|---|---|---|
| M100 | [Post-Hoc Analyses p. 4](../../../jama_jabre_2018_oi_180004.pdf#page=4); Discussion p. 7 | Center No. 5 sample 115: BMV 56, ETI 59; CCF ETI 87%, BMV 86%; difference −1% [95% CI −4% to 2%], P=.70. No significant CCF difference. Greater count of pauses >2 seconds BMV 27 vs ETI 16; “difference, 11 seconds [95% CI, 7 to 15]; P < .001.” Preserve literal seconds unit; no summary measure (mean/median) specified in this narrative. Discussion repeats 115, greater number of >2-second pauses and 30:2 CPR rhythm. |
| M101 | Post-Hoc Analyses pp. 4, 6 | After excluding ECMO-CPR/prolonged or modified resuscitation and organ donation n=91; after exclusion of patients intubated after BMV before ROSC considered in ETI n=155; results comparable, referred to eTable 2 Supplement 2. Methods p. 4 instead describe considering those patients in ETI; preserve both verbal formulations for alignment without assuming unprinted procedure. |
| M102 | [Discussion p. 7](../../../jama_jabre_2018_oi_180004.pdf#page=7); Statistical Analysis p. 3 | Historical Japanese registry 649 359 patients; favorable survival ETI 1.1% vs BMV 2.9%, compared with rounded sample-size hypothesis 650 000 and BMV 3%/ETI 1.1%, OR 0.38 [0.36–0.39] in M11. All these are REPORT narrative background quantities, not imported external source results. |
| M103 | Discussion p. 7 | France previously reported difficult-intubation rate 9%–11%, described comparable here; US multicenter 1941 patients, 1272 cardiac arrest; intubation success 91.8% after fewer than 3 attempts; ensuing “incidence of difficult intubation thus being 9.2%.” Both printed percentages preserved as narrative background reporting. |

## Mapping limits and handoff

All nine assigned direct-source units mapped; no scientific coverage gap. Historical results are captured only as printed main-paper content, without external verification. No unreported individual test selection, SE, test statistic, multiplicity-adjusted inference or person-time denominator inferred. Matching Supplement 2 and PLAN relationships require disjoint support mapping. Registered numeric/statistical IDs and consistency judgments belong to checkers/coordinator; this artifact supplies complete transcription and alignment inputs.
