# Main numeric/reporting relationship inventory — DOC-001

Provisional `MN` IDs are mapper-local. Each record identifies a checkable printed relationship and its exact main-PDF locations; it does not assert a candidate.

| ID | Relationship / exact printed values | Rule or comparator | Locations | Cross-source key |
|---|---|---|---|---|
| MN001 | Enrollment 961; allocation 477 low + 484 intermediate | allocation sum equals enrollment | PDF pp.1,3,5 | POP:ITT-961 |
| MN002 | 3695 screened; 2734 excluded; 961 randomized | 3695−2734=961 | p.3 Fig 1 | FLOW:screened-to-randomized |
| MN003 | Ineligible reason counts 323+268+193+98+50+27+2=961 | category sum | p.3 Fig 1 | FLOW:ineligible-961 |
| MN004 | Not-enrolled reason counts 705+348+296+256+57+55+12+44=1773 | category sum | p.3 Fig 1 | FLOW:not-enrolled-1773 |
| MN005 | 475+2=477; 480+4=484; total losses=6 | flow reconciliation and Results repeat | pp.3,5 | FLOW:analysis-475:480 |
| MN006 | Randomization blocks min 2/max 6; 6 ICUs; dates 2014-09-01 to 2017-08-20 | design quantities | pp.1-2 | DESIGN:trial |
| MN007 | Low target 6 down to 4 mL/kg PBW; intermediate starts 10; adjustment 1 mL/kg/h; pressure thresholds 5,8,25 cm H2O | intervention label/unit/direction | pp.2-3 | INT:tidal-volume-targets |
| MN008 | PBW sex equations and maximum strategy duration 28 d | formula/unit/time definition | p.3 | SCALE:PBW |
| MN009 | VFD day 28: alive/free from ventilation, >24h unassisted period; >28 ventilation days=0; one day≈15% expected time | outcome definition/scale | p.4 | OUTCOME:VFD28-definition |
| MN010 | Power: n=952/476 per group, 80%, 1 day, SD 5, alpha .05, 20% dropout | planned design relation | p.4 | PLAN:primary-power |
| MN011 | Two-sided P values, alpha .05, primary missing <1%, complete case | inferential-definition quantities | p.4 | P:two-sided |
| MN012 | Table 1 demographics: age, male count/%, BMI, PBW values | baseline display values | p.5 Table 1 | BASE:demography |
| MN013 | Table 1 severity: SAPS, LIPS/ARDS-risk, SOFA, septic shock values/scales | baseline display values and scale direction | p.5 Table 1 | BASE:severity |
| MN014 | Tobacco categories sum 475 per group (not allocation 477/484) | category sum / displayed denominator | p.5 Table 1 | BASE:tobacco |
| MN015 | Alcohol categories sum 475/482 | category sum / displayed denominator | p.5 Table 1 | BASE:alcohol |
| MN016 | Surgical/medical 82+393=475 and 79+403=482; displayed 17.3/82.7 vs16.4/83.6 | category sum, percent denominator | p.5 Table 1 | BASE:admission |
| MN017 | 14 intubation reason categories sum to 477/484 | category sum, percent denominator | p.5 Table 1 | BASE:intubation-reason |
| MN018 | Ventilation modes 143+98+236=477; 154+91+239=484 | category sum | p.5 Table 1 | BASE:pre-rand-ventilation |
| MN019 | Pre-randomization timing 0.9 h (0.3-2.0) vs 0.9 (0.4-2.1); Results timing 0.88 (0.36-2.01)/0.57 (0.23-1.00) | population/timepoint distinctness | p.5 Table 1/Results | INT:timing |
| MN020 | Baseline respiratory row values (TV, plateau, RR, PEEP, driving pressure, FiO2, PaO2/FiO2, PaCO2, pH) | units/scales and low/intermediate pairing | p.5 Table 1 | BASE:respiratory |
| MN021 | VFD mean/SD 15.2/11.6 vs15.5/11.4; median/IQR 21(0-26) both | main result repeated in abstract | pp.1,5,6 | OUT:VFD28 |
| MN022 | Ventilation-days survivors mean/SD 5.4/6.6 vs6.0/7.3; median 3(1-6) vs3(1-8) | group contrast/definition | p.6 Table 2 | OUT:vent-days-survivors |
| MN023 | ICU stay mean/SD 9.6/13.3 vs9.2/9.9; median 6(3-11) both | table/abstract/Fig2 quantities identify different measures | pp.1,6,7 | OUT:ICU-stay |
| MN024 | Hospital stay mean/SD 20.4/23.8 vs21.0/21.1; median 14(6-26) vs15(8-26) | table/abstract/Fig2 quantities identify different measures | pp.1,6,7 | OUT:hospital-stay |
| MN025 | Mortality numerators/denominators/percentages for ICU, hospital, 28-day,90-day | percent against stated denominator; matched repetition | pp.1,6,7 | OUT:mortality |
| MN026 | ARDS/pneumonia event counts, denominators, percentages | percent against stated denominator; abstract repeat | pp.1,6 | OUT:ARDS-pneumonia |
| MN027 | Pneumothorax/atelectasis event counts, denominators, percentages | percent against stated denominator; abstract repeat | pp.1,6 | OUT:pneumothorax-atelectasis |
| MN028 | Extrapulmonary infection/sepsis counts, denominators, percentages | percent against stated denominator | p.6 Table 2 | OUT:infection-sepsis |
| MN029 | Delirium/tracheostomy counts, denominators, percentages | percent against stated denominator | p.6 Table 2 | OUT:delirium-tracheostomy |
| MN030 | Intubation-location subgroup MD −2.50 (IQR −4.63 to−0.36) vs 1.45 (IQR −0.52 to3.43) | subgroup label, interval type, P interaction | p.6 Results | OUT:subgroup-intubation-location |
| MN031 | Fig2A risk sets at 0–21 d and observation summaries 4.4 vs4.3 days | curve label versus risk sets | p.7 Fig 2A | FIG:VFD-curve |
| MN032 | Fig2B risk sets at 0–90 d and survival observation note | curve label versus 90-d mortality | p.7 Fig 2B | FIG:90d-survival |
| MN033 | Fig2C risk sets at 0–20 d and 8.0-d observation summaries | curve label versus ICU stay | p.7 Fig 2C | FIG:ICU-stay-curve |
| MN034 | Fig2D risk sets at 0–48 d and 21.0-d observation summaries | curve label versus hospital stay | p.7 Fig 2D | FIG:hospital-stay-curve |
| MN035 | Discussion summary: six centres, 3-year enrolment, low 7 and intermediate 9 mL/kg PBW | narrative numbers distinguished from pre-randomization table | p.7 | DISCUSSION:tidal-volume-summary |
