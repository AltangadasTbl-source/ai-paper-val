# Main quantitative evidence map — main-001

## Scope and method

- **Source ID:** JAMA2025_9110_D01_MAIN
- **Direct source:** `jama_summers_2025_oi_250040_1753124024.36498.pdf`
- **Assigned unit union:** PDF pages 1-10 (complete; 10/10 inspected).
- **Direct confirmation:** fresh `pdftotext` native and layout extraction was made from each assigned PDF page under `preprocessing/main-001/`. Direct PDF-rendered visual confirmation was used for Figure 1 and the printed tables/figures on pages 5 and 7. Source PDF page numbers below are physical PDF pages and evidence links use `jama_summers_2025_oi_250040_1753124024.36498.pdf#page=N`.
- **Reusable locators:** source-matched native/normalized text, the page manifest, and targeted image/OCR assets A03-A08 listed in `evidence_asset_inventory.md`. They were used as locators only; printed source is authoritative.
- **Conventions:** `M-N` IDs map numeric/reporting relationships; `M-S` IDs map inferential/statistical relationships. Repeated text is listed as a matching occurrence, rather than remapped as a new result. Candidate seeds are unadjudicated observations for the downstream checker, not findings or dispositions.

## Page-by-page coverage

| PDF page | Result-relevant units inspected | Relationship IDs / result |
|---:|---|---|
| 1 | Abstract: trial design, interventions, population, primary and secondary results | M-N001 to M-N007; M-S001 to M-S007 |
| 2 | Methods: setting, eligibility, randomization, intervention concentrations and delivery limit | M-N008 to M-N010 |
| 3 | Figure 1 participant flow; primary-outcome definition; secondary-outcome definitions; sample-size setup | M-N011 to M-N014 |
| 4 | Power assumptions; analysis populations/models; Results population and delivery summaries; primary descriptive result | M-N015 to M-N016; M-S008 |
| 5 | Table 1 baseline results; narrative secondary/biochemical/subgroup/adverse-event results | M-N017 to M-N023; M-S012 to M-S013 |
| 6 | Figure 2 protein/calorie displays and day-specific denominators | M-N024 |
| 7 | Table 2, all primary/secondary/sensitivity results, discharge/readmission summaries and footnotes | M-N025 to M-N027; matching M-S001 to M-S011 |
| 8 | Figure 3, all subgroup strata, contrasts and interaction P values | M-N028; M-S012 to M-S015 |
| 9 | Discussion/conclusion and administrative/reference content | Matching conclusion only (M-N002); no new result-relevant relationship |
| 10 | Reference content only | No applicable result-relevant relationship |

## Numeric/reporting relationships

### M-N001 — Trial design, intervention and enrolled population

- **Locations:** [p1](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1), abstract; [p2](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=2), Methods.
- **Printed values/labels:** 8 Australian/New Zealand ICUs; recruitment May 23, 2022-August 23, 2023; final follow-up November 21, 2023; cluster randomized crossover open-label design. Formulae: augmented protein 100 g/L versus usual protein 63 g/L, both isocaloric. Four ICUs commenced each formula; sequential 3-month formula periods over 12 months.
- **Population/contrast/unit:** critically ill patients receiving enteral nutrition; augmented versus usual protein. Abstract total is 3397, median (IQR) age 61 (48-71) years, 2157 (64%) male.
- **Matching occurrences:** p2 identifies patients aged at least 16 years and the inclusion/exclusion setting; p3 Figure 1 and p4 Results identify the analysis population.
- **Checks supported:** intervention label/concentration, population and time identity, cluster/period totals.

### M-N002 — Primary-outcome definition and descriptive primary result

- **Locations:** [p1](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1), abstract; [p3](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=3), Outcome Measures; [p4](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=4), Primary Outcome; [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7), Table 2; [p9](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=9), conclusion.
- **Definition/scale/direction:** days free of the index hospital and alive at day 90 = 90 minus post-formula index-hospital days and index-hospital readmission days within 90 days; patients dying in that period receive 0. Footnote e: a reduction is worse.
- **Printed group values:** augmented 62 (IQR 0-77) days; usual 64 (0-77) days; intention-to-treat denominators 1681 and 1716. p4 additionally reports 497/1681 (29.6%) and 475/1716 (27.7%) with zero days free and alive at day 90.
- **Checks supported:** definition-to-zero assignment, descriptive denominators/proportions, matched-result agreement, direction.

### M-N003 — Day-90 survival counts and proportions

- **Locations:** [p1](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1), abstract; [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5), narrative; [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7), Table 2.
- **Population/time/contrast:** full ITT groups, alive at day 90: augmented 1221/1681 (72.6%); usual 1269/1716 (74.0%).
- **Checks supported:** numerator/denominator/percentage rounding, abstract-table-narrative identity, effect measure in M-S002.

### M-N004 — Hospital-free days among survivors

- **Locations:** [p1](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1), abstract; [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5); [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7), Table 2.
- **Printed values:** days free of index hospital at day 90 in survivors, median (IQR): augmented 72 (57-80), usual 72 (59-80).
- **Checks supported:** survivor-population label, time/scale, matched reporting, M-S003 effect.

### M-N005 — Invasive-ventilation duration summaries

- **Locations:** [p1](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1), abstract (effect only); [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5), narrative; [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7), Table 2 and footnote j.
- **Printed values:** table label says “Duration of invasive ventilation, mean (SD), h”; augmented 84.0 (35.0 to 178.9), usual 78.0 (33.2 to 161.0). Footnote j defines duration as total ICU invasive-ventilation hours including reintubation and ventilation before trial nutrition.
- **Checks supported:** unit, summary-statistic label and displayed form, M-S004 effect.

### M-N006 — ICU/hospital duration summaries

- **Locations:** [p1](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1), abstract; [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5); [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7), Table 2/footnote a.
- **Printed values:** duration of ICU admission, median (IQR), days: 6.6 (3.1-18.0) augmented, 6.2 (3.0-15.0) usual. Hospital duration: 21.4 (10.2-80.0), 21.1 (10.1-68.9). Footnote a says these median/IQR values derive from cumulative incidence functions treating death as competing risk.
- **Checks supported:** time-to-live-discharge/competing-risk label, scale, M-S005/M-S006 hazard-ratio direction.

### M-N007 — Tracheostomy and new kidney-replacement therapy counts

- **Locations:** [p1](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1), abstract; [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5); [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7), Table 2.
- **Printed values:** tracheostomy during index hospitalization: 134/1681 (8.0%) versus 121/1716 (7.1%). New KRT during index ICU admission after formula commencement: 122/1681 (7.3%) versus 127/1716 (7.4%).
- **Checks supported:** count/risk/proportion distinction, percentage rounding, population/time wording, M-S007 risk ratios.

### M-N008 — Eligibility and exposure-duration parameters

- **Locations:** [p2](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=2).
- **Printed values:** eligible age at least 16 years; first four sites began May 23, 2022 and four began August 23, 2022; each ICU recruited 12 months. Exclusion included at least 12 hours of nontrial enteral nutrition. Formula delivered while clinically indicated for up to 90 days, ICU discharge, or death, whichever came first; duration recorded in hours.
- **Checks supported:** population/time/denominator identity and outcome/exposure unit.

### M-N009 — Randomization configuration

- **Locations:** [p2](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=2); [p3](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=3), Figure 1.
- **Printed values:** two groups of four sites began three months apart; balanced two groups of four clusters; randomized in two strata of blocks of four. Figure 1 specifies four alternating 3-month periods in each sequence.
- **Checks supported:** cluster/period labels and Figure 1 sequence reconciliation.

### M-N010 — Protein concentration contrast

- **Locations:** [p1](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1); [p2](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=2).
- **Printed values:** augmented Nutrison Protein Intense 100 g protein/L; usual Nutrison Protein Plus 63 g protein/L; both isocaloric.
- **Checks supported:** intervention scale/unit and Figure 2 protein versus calorie distinction.

### M-N011 — Secondary and tertiary outcome list

- **Location:** [p3](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=3).
- **Printed definitions:** secondary outcomes include survivors’ day-90 hospital-free days, day-90 survival, invasive ventilation hours for ventilated patients, ICU/hospital time to live discharge in days, tracheostomy/new KRT incidence and discharge destination. Tertiary biochemical data are prespecified-day measurements.
- **Checks supported:** label/population/time/unit identity for Table 2 and biochemical narrative.

### M-N012 — Figure 1 total screening, exclusion and randomization flow

- **Location:** [p3](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=3), Figure 1 (direct visual confirmation).
- **Printed flow:** 8 randomized ICUs, split as 4/4 with 1429 and 2170 patients assessed (total 3599). Sequence-period screening cells are: 683 augmented, 746 usual, 1130 augmented, 1040 usual (total 3599). Excluded: 33 = 20 contraindicated + 9 nontrial nutrition >12 h + 4 previously enrolled; 43 = 32 + 5 + 6; 87 = 40 + 41 + 6; 25 = 22 + 3. Remaining/randomized: 650 augmented and 703 usual in first sequence, then 1043 augmented and 1015 usual in second sequence; 12 and 2 consent-withdrawal exclusions, leaving 1031 and 1013. Final primary analysis: augmented 1681 (=650+1031) and usual 1716 (=703+1013).
- **Matching occurrence:** p4 says 3599 required enteral nutrition, 3411 enrolled, 14 withdrew retention consent, leaving 3397 (1681/1716).
- **Checks supported:** all flow subtotal/total arithmetic and final population reconciliation.

### M-N013 — Primary-outcome calculation rule

- **Location:** [p3](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=3).
- **Printed rule:** 90 days minus all post-commencement index-hospital days minus index-hospital readmission days within 90 days; death during period assigned zero. Death after discharge through day 90 ascertained via local health records/national death index linkage.
- **Checks supported:** primary zero assignment, rate/count distinction, time horizon and denominator definition.

### M-N014 — Sample-size/power design inputs

- **Locations:** [p3](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=3); [p4](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=4).
- **Printed values:** 8-cluster/4-period design; cluster-period size at least 60 for 80% power and at least 80 for 90% power to detect one-day difference. Within-cluster within-period correlation range 0.01-0.05 (base 0.02), cluster autocorrelation 0.64-0.96 (base 0.8), cluster-size CV 0.5. The reported implementation has four clusters in each treatment sequence; with four clusters and at least 60 patients per cluster-period, >80% power to detect a two-day difference.
- **Checks supported:** stated cluster count and power/difference labels (planning evidence; not a result).

### M-N015 — Analysis population, delivery timing and volume

- **Location:** [p4](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=4).
- **Printed values:** 3599 required enteral nutrition; 3411 enrolled; 14 withdrew, leaving 3397 ITT (1681/1716). Time ICU admission to formula, median (IQR) hours: 19.0 (9.2-37.7) versus 19.3 (9.5-39.8). Formula duration: 87 (36-187) versus 84 (34-182) hours. Volume per observed calendar day: 696 (408-951) versus 676 (405-957) mL/day.
- **Checks supported:** flow reconciliation; time/unit/summary-type labels; Figure 2 denominators.

### M-N016 — Primary zero-day count/proportion

- **Location:** [p4](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=4).
- **Printed values:** 497 augmented participants (29.6%) and 475 usual participants (27.7%) “had zero days free of the index hospital and were alive at day 90.”
- **Checks supported:** denominator/percentage rounding and exact outcome wording; compare to M-N002 definition.

### M-N017 — Table 1 age and sex

- **Location:** [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5), Table 1.
- **Printed values:** age median (IQR), years: 61 (48-70) augmented vs 61 (48-71) usual. Male: 1070 (63.7%) vs 1087 (63.3%); female: 611 (36.3%) vs 629 (36.7%).
- **Checks supported:** within-column sex count/percentage totals and table population denominators.

### M-N018 — Table 1 admission reason and diagnosis categories

- **Location:** [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5), Table 1.
- **Printed values:** reason: nonsurgical 1068 (63.5)/1100 (64.1), emergency surgical 379 (22.5)/361 (21.0), elective surgical 234 (13.9)/255 (14.9). Diagnosis: neurological 374 (22.2)/350 (20.4), respiratory 325 (19.3)/360 (21.0), cardiovascular 300 (17.8)/310 (18.1), trauma 204 (12.1)/209 (12.2), gastrointestinal 168 (10.0)/190 (11.1), other 162 (9.6)/163 (9.5), sepsis 148 (8.8)/134 (7.8).
- **Checks supported:** mutually exclusive category count/percentage totals, APACHE-II category label.

### M-N019 — Table 1 admission source and diabetes

- **Location:** [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5), Table 1.
- **Printed values:** emergency department 589 (35.0)/618 (36.0); operating theater 575 (34.2)/595 (34.7); hospital ward 227 (13.5)/243 (14.2); other hospital 181 (10.8)/168 (9.8); transfer another ICU 109 (6.5)/92 (5.4); diabetes 429 (25.5)/451 (26.3).
- **Checks supported:** mutually exclusive source total and percentages; diabetes is a separate nonexclusive characteristic.

### M-N020 — Table 1 anthropometry/severity/frailty scales

- **Location:** [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5), Table 1 and notes.
- **Printed values:** weight kg 80.0 (68.0-94.4)/80.0 (67.0-96.5); BMI 27.6 (24.1-32.6)/27.5 (23.8-32.3); ideal weight 65.8 (56.8-73.0)/65.8 (56.8-73.0); APACHE II 19.0 (15.0-24.0)/19.0 (14.0-25.0); frailty 3 (3-4)/3 (3-4). Ideal-weight data: 2618 total (1312/1306). APACHE II range 0-71, higher worse; frailty scale 1-8 with named anchors.
- **Checks supported:** scale/unit labels, missing-data denominator and component sum.

### M-N021 — Table 1 baseline treatment-status and commencement timing

- **Location:** [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5), Table 1.
- **Printed values:** invasive ventilation at formula start 1385 (82.4%)/1355 (79.0%); vasopressor/inotrope 926 (55.1%)/921 (53.7%); new KRT before formula 122 (7.3%)/119 (6.9%); ICU-to-formula time, median (IQR), 19.0 (9.2-37.7)/19.3 (9.5-39.8) h.
- **Checks supported:** denominator/proportion; baseline KRT definition versus Figure 3; timing matched to M-N015.

### M-N022 — Blood urea values and conversion instruction

- **Location:** [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5).
- **Printed values:** at formula commencement, urea mmol/L median (IQR): 7.3 (4.8-12.4) augmented versus 7.5 (4.8-11.8) usual; at day 10: 13.0 (8.2-18.8) versus 10.6 (7.1-15.4). To convert to mg/dL, divide by 0.357.
- **Checks supported:** time/group/unit and stated conversion-factor label.

### M-N023 — Adverse-event counts

- **Location:** [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5).
- **Printed values:** four adverse events, three augmented and one usual; two serious adverse events, one in each group.
- **Checks supported:** component sum and group/event-type distinction.

### M-N024 — Figure 2 treatment-exposure displays

- **Location:** [p6](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=6), Figure 2.
- **Printed axes/labels:** panel A total protein from trial enteral nutrition, g/day, y-axis 0-400; panel B total calories, kcal/day, y-axis 0-4000. Trial days 1, 2, 3, 4, 5, 10, 20, 30. Boxes show medians and 25th/75th percentiles; dots are outside-IQR values.
- **Day-specific numbers of patients, identical in both panels:** augmented 1680, 1584, 1229, 1005, 817, 341, 100, 43; usual 1711, 1608, 1247, 998, 823, 347, 91, 34.
- **Checks supported:** protein versus calorie unit/scale, time-specific denominator, visualization-summary labels. Exact plotted medians/quartiles are not printed as values.

### M-N025 — Table 2 model-specific primary descriptive values and sensitivity exclusions

- **Location:** [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7), Table 2 and footnotes b/c/g/h.
- **Printed values:** primary quantile model: 62.0 (0-77) vs 64.0 (0-77). Linear mixed model, mean (SD): 47.5 (34.0) vs 48.9 (33.5). Bayesian quantile model: 62.0 (0-77) vs 64.0 (0-77); credible (not otherwise CI) interval and posterior probability of any benefit 0.109. Sensitivity excluding known nontrial formula: 64 (0-78) vs 65 (0-78), exclusions 234 (144/90). Sensitivity excluding palliative care/organ donation: 63 (0-77) vs 64 (0-77), exclusions 27 (17/10).
- **Checks supported:** model/interval-type labels, exclusion totals, repeat values, corresponding M-S IDs.

### M-N026 — Table 2 discharge destinations

- **Location:** [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7), Table 2.
- **Printed values, augmented/usual:** home 634 (37.7)/723 (42.1); died 378 (22.5)/380 (22.1); other acute hospital 321 (19.1)/306 (17.8); rehabilitation 244 (14.5)/215 (12.5); long-term care 61 (3.6)/49 (2.9); other hospital ICU 27 (1.6)/23 (1.3); other 16 (1.0)/20 (1.2).
- **Rule/label:** summary statistics only; no statistical comparison performed (footnote k).
- **Checks supported:** category count/percentage reconciliation and analysis/no-comparison label.

### M-N027 — Table 2 readmission summaries

- **Location:** [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7), Table 2.
- **Printed values:** at least one hospital readmission before day 90: 161 (9.6%) versus 172 (10.0%); days readmitted to ICU before day 90, median (IQR): 6.0 (3.0-12.0) versus 6.0 (3.8-12.2). No statistical comparison performed.
- **Checks supported:** time horizon, summary/unit labels and percentages.

### M-N028 — Figure 3 subgroup population counts and descriptive medians

- **Location:** [p8](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=8), Figure 3.
- **Printed strata (augmented n/median [IQR] vs usual):** no mechanical ventilation 296/69.0 (46.0-81.0) vs 361/67.0 (34.0-77.0); ventilation 1385/60.0 (0-76.0) vs 1355/63.0 (0-77.0). No baseline new KRT 1559/65.0 (0-78.0) vs 1597/65.0 (0-78.0); yes 122/15.0 (0-59.8) vs 119/24.0 (0-64.0). Age <70: 1231/65.0 (0-77.5) vs 1211/67.0 (24.0-79.0); age >=70: 450/53.5 (0-75.0) vs 505/51.0 (0-73.0). BMI <35: 1066/62.0 (0-76.0) vs 1074/65.0 (0-77.0); BMI >=35: 222/65.5 (8.5-77.0) vs 206/59.5 (0-75.8).
- **Definition:** baseline KRT = new KRT between hospital admission and formula commencement in ICU.
- **Checks supported:** subgroup component counts versus 1681/1716, definition and all linked M-S interaction/effect relationships.

## Statistical/inferential relationships

### M-S001 — Primary quantile mixed-model effect (abstract)

- **Locations:** [p1](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1); matching [p4](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=4), [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7).
- **Result:** adjusted-for-period median difference augmented minus usual −1.97 days (95% CI −7.24 to 3.30), P=.46; M-N002 scale/direction.

### M-S002 — Day-90 survival risk ratio

- **Locations:** [p1](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1); matching [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5), [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7).
- **Result:** RR 0.99 (95% CI 0.95-1.03), P=.47 in Table 2; 1221/1681 versus 1269/1716; M-N003.

### M-S003 — Survivors’ hospital-free-day difference

- **Locations:** [p1](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1); matching [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5), [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7).
- **Result:** median difference 0.01 days (95% CI −1.94 to 1.96), P=.995; M-N004.

### M-S004 — Invasive-ventilation difference

- **Locations:** [p1](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1); matching [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5), [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7).
- **Result:** mean difference 6.8 h (95% CI −3.0 to 16.5), P=.17; M-N005.

### M-S005 — ICU time-to-live-discharge hazard ratio

- **Locations:** [p1](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1); matching [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5), [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7).
- **Result:** cause-specific HR 0.93 (95% CI 0.88-1.00), P=.04; death in ICU competing risk; M-N006.

### M-S006 — Hospital time-to-live-discharge hazard ratio

- **Locations:** [p1](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1); matching [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5), [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7).
- **Result:** cause-specific HR 0.96 (95% CI 0.90-1.02), P=.15; death in hospital competing risk; M-N006.

### M-S007 — Tracheostomy/KRT risk ratios

- **Locations:** [p1](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1); matching [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5), [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7).
- **Results:** tracheostomy RR 1.15 (95% CI 0.66-2.01), P=.57; new KRT RR 0.97 (95% CI 0.81-1.16), P=.69; M-N007.

### M-S008 — Primary-model specification

- **Location:** [p4](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=4).
- **Printed specification:** individual patient quantile mixed-effects model; fixed effects treatment, period, delayed start; ICU normal random effect (mean zero, variance component sigma squared sub c); block-bootstrap 95% CI; 2-sided P<.05 threshold.
- **Checks supported:** compatible-test/model condition for M-S001 and primary sensitivity/subgroup effects.

### M-S009 — Linear mixed-model primary secondary analysis

- **Location:** [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7), Table 2.
- **Result:** mean difference −1.26 days (95% CI −3.59 to 1.06), P=.29, ICC <0.001; group mean (SD) 47.5 (34.0) vs 48.9 (33.5); M-N025.

### M-S010 — Bayesian quantile mixed-model primary secondary analysis

- **Location:** [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7), Table 2/footnotes b/c/f.
- **Result:** median difference −1.50 (credible interval −3.86 to 0.90), ICC 0.023; posterior probability of any benefit 0.109. No P value printed. M-N025.

### M-S011 — Primary sensitivity analyses

- **Location:** [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7), Table 2/footnotes g/h.
- **Results:** excluding known nontrial formula, median difference −0.97 (95% CI −6.04 to 4.10), P=.71, ICC .009; excluding palliative-care/organ-donation patients, −1.12 (−7.17 to 4.93), P=.72, ICC .007. Both fitted using primary quantile model; M-N025.

### M-S012 — Subgroup interaction: mechanical ventilation

- **Locations:** [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5); [p8](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=8), Figure 3.
- **Result:** interaction P=.02, likelihood-ratio test; narrative calls credibility very low. Stratum median differences: no ventilation 2.7 (95% CI −5.24 to 10.64); ventilation −3.44 (−9.64 to 2.76). M-N028.

### M-S013 — Subgroup interaction: baseline new KRT

- **Locations:** [p5](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5); [p8](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=8), Figure 3.
- **Result:** interaction P<.001, likelihood-ratio test; narrative calls credibility moderate. No baseline KRT median difference 0 (−4.32 to 4.32); baseline KRT −13.19 (−50 to 23.62). M-N028.

### M-S014 — Subgroup interaction: age

- **Location:** [p8](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=8), Figure 3.
- **Result:** interaction P=.11; <70 median difference −3 (95% CI −8.48 to 2.49), >=70 0.85 (−8.98 to 10.68). M-N028.

### M-S015 — Subgroup interaction: BMI

- **Location:** [p8](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=8), Figure 3.
- **Result:** interaction P=.47; BMI <35 median difference −3.46 (95% CI −12.44 to 5.53), BMI >=35 7.23 (−3.56 to 18.02). M-N028.

## Candidate seeds for downstream checker (unadjudicated)

| Seed ID | Linked relationship | Direct observation and exact source location | Reproducible check to perform | Human question |
|---|---|---|---|---|
| MAIN-SEED-001 | M-N005 / M-S004 | Table 2 on [p7](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7) labels invasive-ventilation duration as **mean (SD)** but prints `84.0 (35.0 to 178.9)` and `78.0 (33.2 to 161.0)`, each a two-endpoint parenthetical range. The narrative/abstract report a **mean difference** of 6.8 h (95% CI −3.0 to 16.5). | Check whether the two parenthetical values are intended SD values, an IQR/range, or another summary; compare exact result matched in supplied supplements before any registration. This is a possible measure/label inconsistency only. | What summary statistic do `35.0 to 178.9` and `33.2 to 161.0` denote in the supplied study records? |

No display-zero P value is printed in this source. No candidate conclusion, severity, or disposition is made here.

## Limitations

- Native extraction preserved all ten pages. Layout extraction and direct PDF images were needed for Figure 1 and Tables/Figures 1-3; Figure 2’s plotted distribution values are graphical and no exact point values are printed, so its axes, display rule, and printed day-specific denominators are mapped rather than inferred.
- Pages 9-10 contain no new result table, figure, or numerical result beyond the p9 matching conclusion. This is a documented no-applicable-result scope, not an uninspected gap.
