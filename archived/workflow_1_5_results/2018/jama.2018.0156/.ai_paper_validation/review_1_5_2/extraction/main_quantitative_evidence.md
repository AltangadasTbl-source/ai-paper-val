# Main Article Quantitative Evidence Map

## Scope and source

- Source: `jama_jabre_2018_oi_180004.pdf` (DOC-001), PDF pages 1-9; article printed pages 779-787.
- Evidence was mapped from the direct PDF and its fresh 1.5.2 native/layout text assets. Locations below use `jama_jabre_2018_oi_180004.pdf#page=N`.
- BMV is bag-mask ventilation; ETI is endotracheal intubation. The main randomized/ITT denominators are BMV 1018 and ETI 1022 unless a row supplies another denominator.

## Design, endpoint definitions, and analysis framework

| Location | Printed quantitative evidence and definition |
|---|---|
| PDF p1 | 2043 randomized; BMV n=1020, ETI n=1023; enrollment March 9, 2015 to January 2, 2017; follow-up ended January 26, 2017. Mean age 64.7 years; 665 women (32%); 2040 (99.8%) completed trial. |
| PDF p1, p3 | Primary endpoint: favorable neurologic outcome/survival at 28 days, CPC 1 or 2. Noninferiority margin is 1% absolute. The reported primary contrast is BMV minus ETI. |
| PDF p2-p3 | Participants were adults aged at least 18 years. Trial period involved 20 EMS centers (15 France, 5 Belgium); randomized 1:1 in blocks of size 4-8, stratified by center. Follow-up window 28-35 days. Chest-compression-to-breath ratio before ETI: 30:2. |
| PDF p3 | CCF is proportion of each minute with compressions; pauses are those lasting more than 2 seconds; recorded in center 5 for at most 15 minutes of CPR or until ROSC. BMV VAS runs 0-100 mm. Difficult intubation is IDS >5. |
| PDF p3 | Historical/sample-size inputs: 650 000-patient registry; BMV favorable outcome 3%, OR 0.38 (95% CI 0.36-0.39) vs ETI 1.1%; other cited ETI rate 2%. Presumed rates 3% and 2%; 1% noninferiority margin; 956/group gives 80% power using a 95% two-sided CI and 5000 Newcombe-Wilson simulations; target total 2000. |
| PDF p3 | Primary analysis calculates a 95% two-sided CI for pi_BMV minus pi_ETI; noninferiority requires lower limit > -1%. ITT includes all randomized; PP includes randomized and treated without major violation/deviation; safety population is treated according to treatment actually received. Secondary rate endpoints: chi-square tests, 95% CIs on odds ratios and differences; quantitative endpoints: t or Mann-Whitney test; two-sided alpha .05 without multiplicity adjustment. Post hoc hierarchical risk difference has a 97.5% CI and random center effect. |

## Participant flow and populations

| Location | BMV | ETI | Cross-location / arithmetic context |
|---|---:|---:|---|
| PDF p4 Figure; p1 abstract | Randomized 1020 | Randomized 1023 | Sum 2043; matches abstract. |
| PDF p4 Figure | Received assigned BMV 1014; did not receive 6: not cardiac arrest 2, directly intubated owing to massive regurgitation 1, immediate decision not to resuscitate 3 | Received ETI 979; did not receive 44: attempted impossible then BMV 21, randomized ETI but received BMV 14, no attempted resuscitation 9 (directive 3, early ROSC 1, immediate decision 5) | 1014+6=1020; 979+44=1023. Reasons under the 9 are components, not necessarily all reasons for every row. |
| PDF p4 Figure | Lost to follow-up 0; rescue intubation 146 (ventilation failure 55; gastric regurgitation during ventilation 100) | Lost to follow-up 0; discontinued ETI 0 | Figure footnote: several exclusion reasons may be present for the same patient. |
| PDF p4 Figure | ITT 1018; 2 excluded (not cardiac arrest) | ITT 1022; 1 excluded (aged <18 y) | 1018+1022=2040; matches abstract. |
| PDF p4 Figure | PP 995; 23 excluded: not cardiac arrest 2, did not receive BMV 6, no insurance 1, suspected massive aspiration 19 | PP 943; 80 excluded: aged <18 y 1, did not receive ETI 44, no insurance 3, prisoner 1, suspected massive aspiration 36 | Exclusion subcounts can overlap (figure footnote); PP total 1938. |
| PDF p4 Figure | Safety 1028: 1014 randomized to BMV and received BMV; 14 randomized to ETI but received BMV | Safety 999; 24 excluded: 14 ETI-randomized but BMV, no resuscitation 9, aged <18 y 1 | Safety sum 2027; narrative repeats 1028 and 999. |

## Baseline and resuscitation data (Table 1; ITT)

All entries are `BMV | ETI`, location `jama_jabre_2018_oi_180004.pdf#page=5`. Percentages use the denominators printed in the table or row header.

| Measure | BMV | ETI |
|---|---:|---:|
| Group denominator; age mean (SD), years; female No. (%) | 1018; 65.7 (15.5); 332 (32.6) | 1022; 63.8 (15.6); 332 (32.5) |
| Estimated BMI median (25th-75th), kg/m2 | 26.0 (22.9-29.4) | 26.1 (23.4-29.4) |
| Hypertension; coronary artery disease; diabetes | 337 (33.1); 194 (19.1); 185 (18.2) | 358 (35.0); 189 (18.5); 199 (19.5) |
| Tobacco use; COPD; chronic heart failure | 176 (17.3); 126 (12.4); 107 (10.5) | 195 (19.1); 113 (11.1); 111 (10.9) |
| Chronic alcohol abuse; neurologic disorder; cancer | 90 (8.8); 78 (7.7); 72 (7.1) | 82 (8.0); 79 (7.7); 80 (7.8) |
| Psychiatric disorder; dementia; liver disease; chronic renal failure with dialysis; HIV | 53 (5.2); 33 (3.2); 25 (2.5); 25 (2.5); 7 (0.7) | 81 (7.9); 22 (2.2); 17 (1.7); 23 (2.3); 5 (0.5) |
| Activity limitation denominator; good health; moderate limitation; chronic disease; severe restriction | n=934; 492 (52.7); 255 (27.3); 115 (12.3); 72 (7.7) | n=936; 528 (56.4); 254 (27.1); 91 (9.7); 63 (6.7) |
| Arrest at home; etiology denominator; cardiac; noncardiac medical; traumatic | 776 (76.2); n=1014; 692 (68.2); 271 (26.7); 51 (5.0) | 811 (79.4); n=1015; 668 (65.8); 277 (27.3); 70 (6.9) |
| Bystander-witnessed arrest; bystander CPR; bystander ventilation; EMS-witnessed arrest | 719 (70.6); 487 (47.8); 62 (6.1); 164 (16.1) | 708 (69.3); 512 (50.1); 66 (6.5); 170 (16.6) |
| No-flow duration median (IQR), min; collapse-to-ALS median (IQR), min | 5 (1-11); 20 (14-28) | 5 (1-12); 20 (13-29) |
| Shockable first rhythm; mechanical chest-compression device | 169 (16.6); 213 (20.9) | 157 (15.4); 227 (22.2) |
| Initial-rhythm denominator; asystole; pulseless electrical activity; ventricular fibrillation; ventricular tachycardia | n=1016; 729 (71.8); 118 (11.6); 164 (16.1); 5 (0.5) | n=1020; 743 (72.8); 120 (11.8); 151 (14.8); 6 (0.6) |
| Epinephrine; dose median (IQR), mg; amiodarone; lidocaine; fibrinolytic | 962 (94.5); 5 (3-9); 200 (19.7); 11 (1.1); 15 (1.5) | 974 (95.3); 6 (4-9); 188 (18.4); 13 (1.3); 21 (2.1) |
| ECMO-CPR; uncontrolled donation after circulatory death | 35 (3.4); 12 (1.2) | 23 (2.3); 21 (2.1) |

Table 1 labels BMI as kg/m2; no-flow is collapse to start of basic life support; activity/etiology/initial-rhythm denominators are explicitly smaller than ITT denominators. The narrative at PDF p4 says baseline groups were balanced except age and history of psychiatric disorder, with no observed difference considered clinically significant.

## Main outcomes, secondary outcomes, and adverse events

| Result / population / contrast | Printed result and matching locations |
|---|---|
| Primary outcome, ITT, BMV minus ETI | BMV 44/1018 (4.3%) vs ETI 43/1022 (4.2%); difference 0.11%; 1-sided 97.5% CI -1.64% to infinity; P for noninferiority .11. PDF pp1,4; Table 2 components are CPC 1+2: 35+9=44 and 37+6=43 at p6. |
| Primary outcome, hierarchical post hoc | Difference 0.05%; 1-sided 97.5% CI -1.70% to infinity, with center random effect. PDF p4. |
| Primary outcome, PP | Narrative: 4.3% vs 4.2%; difference 0.08%; 1-sided 97.5% CI -1.74% to infinity; P noninferiority .12. PDF p4. Table 2 components: CPC 1+2 = 35+8=43/995 and 34+6=40/943, consistent with the displayed rounded percentages. |
| ITT all-cause survival day 28 | 55/1018 (5.4%) vs 54/1022 (5.3%); BMV-ETI difference 0.1% (95% CI -1.8 to 2.1), P=.90. PDF pp1,4,6. |
| ITT CPC distribution | CPC 1: 35 (3.4) vs 37 (3.6); CPC 2: 9 (0.9) vs 6 (0.6); CPC 3: 4 (0.4) vs 7 (0.7); CPC 4: 7 (0.7) vs 4 (0.4); CPC 5/death: 963 (94.6) vs 968 (94.7); omnibus P=.68. PDF p6. |
| ITT survival to hospital admission | 294/1018 (28.9%) vs 333/1022 (32.6%); difference -3.7% (95% CI -7.7 to 0.3), P=.07. PDF pp1,4,6. |
| ITT ROSC | 348/1018 (34.2%) vs 397/1022 (38.9%); difference -4.7% (95% CI -8.8 to -0.5), P=.03. PDF pp4,6. |
| PP all-cause survival day 28 | 54/995 (5.4%) vs 51/943 (5.4%); difference 0.1% (95% CI -10 to 9.7), P=.99. Exact table printing at PDF p6. |
| PP CPC distribution | CPC 1: 35 (3.5) vs 34 (3.5); CPC 2: 8 (0.8) vs 6 (0.6); CPC 3: 4 (0.4) vs 7 (0.7); CPC 4: 7 (0.7) vs 4 (0.4); CPC 5/death: 941 (94.6) vs 892 (94.6); omnibus P=.76. PDF p6. |
| PP hospital survival | 289/995 (29.1%) vs 312/943 (33.1%); difference -4.0% (95% CI -7.6 to 0.6), P=.055. PDF p6. |
| PP ROSC | 342/995 (34.4%) vs 377/943 (30.0%); difference -5.6% (95% CI -9.9 to -1.3), P=.01. Exact table printing at PDF p6. |
| Adverse event: airway management difficulty, safety | BMV 186/1027 (18.1%) vs ETI 134/996 (13.4%); difference 4.7% (95% CI 1.5-7.9), P=.004. PDF pp1,4,6. Denominators differ from safety-population headings; Table 3 identifies the row as number/total number. |
| Adverse event: failure, safety | BMV 69/1028 (6.7%) vs ETI 21/996 (2.1%); difference 4.6% (95% CI 2.8-6.4), P<.001. PDF pp1,4,6. |
| Adverse event: gastric-content regurgitation, safety | BMV 156/1027 (15.2%) vs ETI 75/999 (7.5%); difference 7.7% (95% CI 4.9-10.4), P<.001. PDF pp1,4,6. |
| Other airway values, safety | BMV VAS median (IQR) 20 (5-55) mm; ETI NA. ETI IDS median (IQR) 1 (0-4); BMV NA. Mainstem ETI 20 (2.0%); recognized esophageal ETI 102 (10.2%); dental injury 7 (0.7%); extubation 5 (0.5%); BMV NA for each. PDF p6. |
| Airway definitions | IDS range 0 to infinity, >5 difficult. BMV VAS range 0=no difficulty to 100=maximum difficulty. Han difficult BMV >2: grade 1 easy, 2 needs oral airway/adjuvant, 3 needs two practitioners, 4 cannot mask ventilate. No unrecognized esophageal intubations. PDF p6. |
| Center 5 post hoc CCF and pauses | n=115 (BMV 56, ETI 59). CCF: ETI 87% vs BMV 86%, BMV-ETI -1% (95% CI -4 to 2), P=.70. Pauses >2 s: BMV 27 vs ETI 16; difference 11 seconds (95% CI 7-15), P<.001. PDF p4. |
| Other post hoc exclusions | CPR/other-procedure modifications (ECMO-CPR and donation) n=91; BMV then ETI before ROSC considered in ETI n=155; results said comparable; detailed values in supplement eTable 2. PDF p6. |

## Repeated narrative claims and numeric context

- PDF p2 Key Points repeats n=2043 and primary 4.3% BMV versus 4.2% ETI, stating the difference did not meet the 1% noninferiority margin.
- PDF p4 narrative repeats all principal ITT and adverse-event values and says the lower CI limit was greater than the noninferiority threshold but noninferiority was not demonstrated.
- PDF p7 repeats 4.3% versus 4.2%, says the study may have been underpowered, and says ETI had significantly higher ROSC whereas overall 28-day survival did not differ.
- PDF p7 cites external contextual numeric results: Japanese observational study 649,359 patients, 1.1% ETI vs 2.9% BMV; reported difficult out-of-hospital ETI rate 9%-11%; US trial n=1941, cardiac-arrest subgroup 1272, ETI success 91.8% after fewer than 3 attempts and difficult rate 9.2%. These are not study outcome rows.

## Mapping signals for downstream checking (no judgment)

1. Table 2 PP ROSC gives ETI `377/943 (30.0%)`, while the same row's BMV-ETI difference is `-5.6%`; direct quotient 377/943 is approximately 40.0%, and 34.4%-40.0%=-5.6%. Preserve as a denominator/percentage/difference reconciliation signal.
2. Table 2 PP survival at 28 days gives difference `0.1 (−10 to 9.7)` while the table labels the column as percentage points and other analogous CIs print decimal precision. Preserve exact printing for interval/scale review; do not infer an intended value.
3. Figure exclusion components state that several reasons may be present for a single patient; overlapping subcounts must not be tested as disjoint totals.

