# Main Quantitative Evidence Map — DOC-001

Scope: `jama_combes_2025_oi_250087_1766516490.94011.pdf#page=1` through `#page=10` (all 10 PDF pages). Direct PDF was inspected with `pdftotext -layout`; the ten source-matched native page files were used only as locators. Locations below are PDF pages, not printed journal-page numbers. No candidate judgment is made here.

## Page-by-page coverage

| PDF page | Result-relevant evidence mapped |
|---:|---|
| 1 | Abstract: randomized N=205; 101 vs 104; baseline age/sex/etiology; primary and selected secondary/adverse-event results. |
| 2 | Study dates, 11 ICUs, eligibility time window, 1:1 allocation/minimization details, and intervention dose/timing. |
| 3 | Outcome definitions, 30- and 60-day time points, sample-size assumptions, models/tests and analysis population. |
| 4 | Figure 1 flow; enrolled/randomized/analysis totals; baseline narrative; treatment delivery; primary and secondary narrative results. |
| 5 | Table 1 baseline characteristics, denominators, missing-data brackets, units, and footnotes. |
| 6 | Table 2 primary/secondary results and Figure 2 risk-set/event counts, model estimate, and median observation times. |
| 7 | Table 3 adverse events and Figure 3 subgroup results/interaction P value; matching Results narrative. |
| 8 | Discussion/limitations repeats: full dose >95%, successful weaning 68%, 60-day mortality 26%, assumed vs observed weaning-failure rates 50% vs 32%; no new primary trial-result table. |
| 9 | Article information and references only; no applicable primary-study result relationship. |
| 10 | References only; no applicable primary-study result relationship. |

## Trial and analysis definitions

| Location | Direct-source extraction |
|---|---|
| p1 Abstract | 11 French ICUs; enrolment Aug 27, 2021–Sep 10, 2024; final follow-up Nov 10, 2024; 205 adults with VA-ECMO started in preceding 48 h; levosimendan n=101 and placebo n=104. |
| p2 Methods | 1:1 randomized double-blind trial; minimization probability 0.8 after first 20, balanced randomness initially; factors: cardiogenic-shock etiology and center. Starting infusion 0.15 μg/kg/min, increased to 0.20 after 2 h absent rate-limiting adverse effects, over 24 h. |
| p3 Outcomes | Primary: time to successful ECMO weaning within 30 days after randomization. Success requires alive without ECMO/other mechanical support/transplant 30 days after removal; competing events: weaning failure and death on ECMO. Secondary outcomes include 30-/60-day mortality, durations/free days, cardiac events, and ICU/hospital stay. |
| p3 Sample size | Placebo cumulative successful-weaning incidence assumed 50%; total N=206 (103/group), 80% power for sHR 1.75 (estimated intervention success 70%), two-sided alpha .05. |
| p3 Statistics | ITT primary/secondary analyses; primary adjusted for minimization factors; Gray test and Fine-Gray sHR/95% CI for three competing events; cause-specific Cox sensitivity analysis. Categorical: chi-square/Fisher; continuous: Wilcoxon rank sum; censored outcomes: Kaplan-Meier/restricted mean survival time/log-rank; two-sided alpha .05; R 4.4.2. |

## Results transcription

### Participant flow and baseline narrative

| Location | Extracted relationship/value |
|---|---|
| p4 Fig 1 | 209 assessed; 4 excluded (one each: lack of consent, past seizures, resuscitation >30 min before ECMO, end-stage cardiomyopathy); 205 randomized: 101 levosimendan, 104 placebo; all included in primary analysis. |
| p4 Fig 1 | Received assigned regimen: 101/101 levosimendan and 102/104 placebo; no placebo: 2. Definitive interruption: 11 vs 3. Lost follow-up: 2 levosimendan (1 before and 1 after primary-end-point collection). Follow-up to day 60. |
| p4 narrative | Randomization median 25 h (IQR 18–41) after ECMO. Overall median age 58 (IQR 50–67); women 56 (27.3%); postcardiotomy 79 (38.5%), acute MI 56 (27.3%), myocarditis 28 (13.7%); median SOFA 12 (IQR 9–15). |
| p4 narrative | LV venting: IABP/microaxial pump 37.6%/5.0% levosimendan and 36.5%/5.8% placebo. Initial 0.15±0.01 dose in 97% overall (99% vs 94%); increased 0.20±0.01 in 93% vs 96%; interrupted before 24 h in 14 (11 vs 3). |

### Table 1 baseline participant characteristics (p5)

All values are levosimendan (n=101) | placebo (n=104), unless an explicit denominator is printed.

| Measure (unit/statistic) | Extracted values |
|---|---|
| Age, median (IQR), y | 59 (50–68) | 58 (48–67) |
| Female / male, n (%) | 26 (25.7) / 75 (74.3) | 30 (28.8) / 74 (71.2) |
| BMI, median (IQR) | 26 (23–30) | 26 (23–31); kg/m² definition in footnote |
| SOFA median (IQR) | 12 (10–15) [n=98] | 12 (9–14) [n=100]; range 0–24, higher worse |
| SAPS II median (IQR) | 43 (32–56) | 38 (26–58); range 0–163, higher worse |
| Time since ECMO, median (IQR), h | 24 (18–41) [n=99] | 27 (18–41) |
| Mechanical ventilation / kidney replacement, n (%) | 87 (86.1) / 9 (8.9) | 80 (76.9) / 15 (14.4) |
| Etiology: postcardiotomy / acute MI / myocarditis / other, n (%) | 39 (38.6) / 29 (28.7) / 12 (11.9) / 21 (20.8) | 40 (38.5) / 27 (26.0) / 16 (15.4) / 21 (20.2) |
| History: hypertension / current smoking / PCI / hypercholesterolemia / long-term dialysis, n (%) | 39 (38.6) / 29 (28.7) / 26 (25.7) / 22 (21.8) / 1 (1.0) | 40/103 (38.8) / 33/103 (32.0) / 12 (11.5) / 21/103 (20.4) / 0 |
| LVEF %, aortic VTI cm, MAP mm Hg, heart rate /min; median (IQR) | 15 (10–25) [n=82]; 8 (6–10) [n=76]; 74 (68–82) [n=100]; 93 (80–106) | 15 (10–25) [n=94]; 8 (6–11) [n=91]; 75 (69–82) [n=103]; 99 (84–111) |
| pH / <7.30 n (%) | 7.43 (7.37–7.49) / 8 (7.9) | 7.45 (7.40–7.49) / 11 (10.6) |
| Lactate mmol/L / >=2 n (%) | 2.0 (1.4–2.9) / 53 (52.5) | 1.9 (1.4–2.6) / 47 (45.2) |
| Creatinine mg/dL / >=1.5 n (%) | 1.3 (1.0–2.1) / 47 (46.5) | 1.3 (0.9–2.0) / 43 (41.3) |
| ALT U/L / >=80 n (%) | 89 (42–203) [n=99] / 52/99 (52.5) | 72 (33–205) [n=103] / 49/103 (47.6) |
| AST U/L / >=80 n (%) | 221 (90–502) [n=99] / 81/99 (81.8) | 173 (88–536) / 80 (76.9) |
| hs-troponin ng/L | 4328 (998–12 990) [n=86] | 2027 (390–9950) [n=87] |
| Any vasopressor/inotrope; inotropic score | 96 (95.0); 29 (10–58) μg/kg/min | 99 (95.2); 23 (10–65) μg/kg/min |
| Norepinephrine n (%); dose μg/kg/min | 72 (71.3); 0.20 (0.00–0.50) | 76 (73.1); 0.18 (0.00–0.56) |
| Dobutamine n (%); dose μg/kg/min | 81 (80.2); 7 (3–10) | 88 (84.6); 8 (4–11) |
| Epinephrine / other medication, n (%) | 2 (2.0) / 6 (5.9) | 0 / 4 (3.8) |

### Table 2, Figure 2, Table 3, Figure 3, and matched narrative (pp6–7)

| Location/result | Extracted values and labels |
|---|---|
| p6 Table 2, primary successful weaning day 30 | 69/101 (68.3%) vs 71/104 (68.3%); absolute risk difference 0.0% (95% CI −12.8 to 12.7); sHR 1.02 (0.74–1.39); P=.92. Fine-Gray adjusted for cardiogenic-shock etiology. |
| p6 Table 2, competing events | Weaning failure 15 (14.9%) vs 21 (20.2%): RD −5.3% (−15.2 to 4.6), sHR .72 (.37–1.38), P=.32. Death before weaning 15 (14.9%) vs 12 (11.5%): RD 3.3% (−5.6 to 12.1), sHR 1.32 (.62–2.79), P=.47. |
| p6 Table 2, mortality | Day 30: 26 (25.7%) vs 23 (22.1%), RD 3.6% (−8.0 to 15.4), RR 1.16 (.71–1.90). Day 60: 28 (27.7%) vs 26 (25.0%), RD 2.7% (−9.0 to 15.3), RR 1.11 (.70–1.75). |
| p6 Table 2, durations | ECMO-free days by d30 median (IQR): 24 (0–26) vs 23 (12–26), difference 1 (−1 to 4). ECMO days: 5 (4–7) vs 6 (4–11), −1 (−2 to 1). ICU days by d60 mean (SD): 18 (15) [n=100] vs 19 (15), −1 (−5 to 3). Hospital days: 28 (18) [n=100] vs 35 (19), −7 (−12 to −2). |
| p6 Table 2, ventricular arrhythmias | 18 (17.8%) vs 9 (8.7%); RD 9.2% (0.4–18.1); RR 2.06 (.97–4.37). Secondary-outcome P values intentionally not reported for multiple-testing concerns. |
| p6 Fig 2 | At risk d0/d5/d10/d15: 101/88/20/10 vs 104/76/37/19. Cumulative-event counts: 0/36/84/93 vs 0/41/70/89. Curves truncated d15. Median observation for successful weaning by reverse Kaplan-Meier: 11 (IQR 9–20) vs 16 (12–19) d. |
| p7 Table 3 | Any serious AE 59 (58.4%) vs 61 (58.7%), ARD −0.2%; any arrhythmia 63 (62.4) vs 55 (52.9), 9.5%; AF 35 (34.7) vs 29 (27.9), 6.8%; SV tachyarrhythmia 49 (48.5) vs 48 (46.2), 2.4%; bradycardia 4 (4.0) vs 1 (1.0), 3.0%; torsades 0 vs 0, 0.0%; VF/VT 18 (17.8) vs 9 (8.7), 9.2%; VF/VT with shock 4 (4.0) vs 1 (1.0), 3.0%; hypokalemia 1 (1.0) vs 2 (1.9), −0.9%; cessation-related suspected event 12 (11.9) vs 4 (3.8), 8.0%. |
| p7 Fig 3 | All: 71/104 (68.3%) vs 69/101 (68.3%), sHR 1.02 (.74–1.39). Postcardiotomy 32/40 (80.0) vs 28/39 (71.8), .73 (.46–1.15); acute MI 17/27 (63.0) vs 15/29 (51.7), .73 (.37–1.40); myocarditis 10/16 (62.5) vs 11/12 (91.7), 2.16 (.97–4.80); other 12/21 (57.1) vs 15/21 (71.4), 1.61 (.78–3.33); interaction P=.74. |
| p4/p6/p7 matched narrative | Primary, 60-day mortality, ECMO/ICU duration, and ventricular-arrhythmia values match Table 2; adverse-event narrative matches Table 3. p8 repeats 68% successful weaning and approximately 26% 60-day mortality, and describes assumed 50% vs observed 32% weaning-failure rate. |

## Explicit no-applicable units

PDF pp9–10 contain article information/references and no newly reported primary-study numeric or inferential result. On p8, numbers from prior literature are cited contextual evidence rather than a new LEVOECMO trial result; main-trial repeats and limitation assumptions are mapped above.
