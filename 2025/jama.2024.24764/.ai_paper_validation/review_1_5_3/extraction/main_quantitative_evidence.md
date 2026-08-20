# Main Quantitative Evidence Mapping — DOC-001

## Scope, method, and boundaries

- **Document:** `jama_atherton_2025_oi_240145_1741627844.85412.pdf` (DOC-001), PDF pp. 1-11.
- **Assignment:** All 11 reusable-backed PDF pages; no fresh-required unit in this shard.
- **Authority and method:** The supplied PDF was inspected directly with native/layout extraction (`pdfinfo` confirms 11 unencrypted pages; `pdftotext -layout`), using the current-run approved reusable page-delimited native text as a locator/transcription aid. Existing rendered/OCR companions were used to corroborate Figure 1, Tables 1-3, and Figure 2. No OCR was newly required. Exact evidence locations below always refer to the supplied PDF.
- **Mapping rule:** `N` IDs identify numeric/reporting relationships; `S` IDs identify inferential/statistical relationships. These are evidence-map identifiers, not candidates, judgments, or findings.
- **Population and contrast:** Adults undergoing emergency laparotomy; iNPWT versus surgeon's preference wound dressing. Unless stated otherwise, treatment-group values are iNPWT then surgeon's preference.

## Complete page-by-page coverage ledger

| PDF page | Printed page | Result-relevant content mapped | Coverage status | Exact source location |
|---:|---:|---|---|---|
| 1 | 853 | Abstract: design population, randomized/analysis totals, primary and LOS results, conclusion | COMPLETE | `jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=1` |
| 2 | 854 | Key Points; eligibility, sites, randomization context; no additional main results table/figure | COMPLETE — no additional applicable result relationship beyond N001/N002 | `jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=2` |
| 3 | 855 | Figure 1 participant flow, exclusions, allocation, follow-up, deaths, and footnotes | COMPLETE | `jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=3` |
| 4 | 856 | Outcome definitions, analysis/model labels, power target, recruitment totals | COMPLETE | `jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=4` |
| 5 | 857 | Table 1 baseline data, first portion | COMPLETE | `jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=5` |
| 6 | 858 | Table 1 continuation; recruitment/descriptive results, adherence, primary/secondary/safety narratives | COMPLETE | `jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=6` |
| 7 | 859 | Table 2 intraoperative data and table footnotes | COMPLETE | `jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=7` |
| 8 | 860 | Table 3; remote-assessment descriptive SSI data | COMPLETE | `jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=8` |
| 9 | 861 | Figure 2 subgroup event counts, RRs, CIs, interaction P values | COMPLETE | `jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=9` |
| 10 | 862 | Generalizability comparison, conclusion; no new trial-results table/figure | COMPLETE | `jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=10` |
| 11 | 863 | References only; no applicable trial result relationship | COMPLETE — no applicable unit | `jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=11` |

All 11 of 11 assigned source pages are mapped. Pages 2, 10, and 11 are explicitly recorded where no additional applicable trial-result relationship is displayed.

## Definitions, populations, and model context

| ID | Complete relationship / source claim | Exact location |
|---|---|---|
| N001 | Trial population and follow-up: 840 adults were randomized (536 UK, 304 Australia); 52% female; mean age 63.8 years (range 18.8-95.3). Recruitment was December 18, 2018-May 25, 2021, at 22 UK and 12 Australian hospitals; follow-up was 30 days postprocedure and database closure August 25, 2021. | PDF p. 1 Results; PDF p. 4 Recruitment |
| N002 | After postrandomization exclusions `N = 52`, 394 participants per group were in the primary analysis. Abstract primary occurrence: 112/394 (28.4%) vs 108/394 (27.4%), RR 1.03 (95% CI 0.83-1.28), P=.78. | PDF p. 1 Results |
| N003 | Primary outcome: CDC-defined SSI through 30 days, with superficial or deep incisional SSI coded binary yes; assessments on postoperative days 7-10/discharge and near day 30. A participant with an SSI before death, withdrawal, or loss was counted as an event; otherwise leaving before the day-30 assessment was missing. | PDF p. 4 Outcomes |
| N004 | Secondary outcome time/scales: LOS; wound-related/other complications through 30 days (6-level Clavien-Dindo); wound-related readmission through 30 days; 10-point pain at days 7 and 30; SF-12 at days 7/30; EQ-5D-5L at days 7/14/21/30; SAEs including postoperative mortality through day 30. | PDF p. 4 Outcomes |
| S001 | Power/design target: detect a 40% relative SSI reduction, or 10% absolute difference from 25% to 15%, with 90% power, type-I error 5% (`alpha=.05`), predicted 20% attrition; required 420 per group, 840 total. | PDF p. 4 Statistical Analysis |
| S002 | Primary analyses were complete-case and intention-to-treat. Minimization variables were covariates and center a random effect; 95% CIs were reported. Mixed-effects binomial model used a log link for adjusted RR and identity link for adjusted RD. | PDF p. 4 Statistical Analysis |
| S003 | Categorical secondary outcomes used the primary-outcome approach. LOS used mixed-effect linear regression after log transformation, exponentiated to a ratio of geometric means. Longitudinal SF-12/EQ-5D-5L used mixed-effect linear regression for adjusted mean difference, treatment-by-time interaction, independent covariance. | PDF p. 4 Statistical Analysis |
| S004 | Prespecified primary-outcome subgroups: contamination, stoma, procedure, skin preparation, BMI, country, assessment method, and randomization before/on-or-after March 11, 2020; subgroup-by-treatment interaction was included in each binomial model. | PDF p. 4 Statistical Analysis |

## Participant flow and recruitment

| ID | Complete relationship / values | Exact location |
|---|---|---|
| N005 | Figure 1 screening: 2916 screened; 2076 excluded: 709 ineligible, 525 staff unavailable, 497 not identified before procedure, 132 declined, 34 procedure did not go ahead, 34 initially laparoscopic then converted to open laparotomy, 27 dressing unavailable, 23 recruitment suspended, 95 other/unknown; 840 randomized. | PDF p. 3 Figure 1 |
| N006 | Ineligibility footnote: preceding abdominal operation 286; long-term incapacity/unable to consent 114; not emergency laparotomy 100; expected reopening within 30 days 56; unable/unwilling follow-up at 30 days 49; incision <5 cm 47; skin not primarily closed 26; consultee/legal representative unavailable 22; younger than 16 years 9. | PDF p. 3 Figure 1 footnote a |
| N007 | Allocation flow: initially randomized iNPWT 424 and surgeon preference 416. Pre-retained exclusions: iNPWT 13 (11 did not consent; 2 requested data removal); surgeon preference 6 (5 did not consent; 1 requested removal). Retained allocation: 411 and 410, respectively. | PDF p. 3 Figure 1; PDF p. 4 Recruitment |
| N008 | Received allocated intervention: iNPWT 404/411 as randomized, 6 not as randomized, 1 undetermined; surgeon preference 402/410 as randomized, 8 not as randomized. Narrative reports 98% adherence in each group. | PDF p. 3 Figure 1; PDF p. 6 Adherence |
| N009 | Follow-up/primary analysis flow: iNPWT exclusions 12 (5 withdrew, 5 died, 2 lost), 399 completed day-30 follow-up, 394 primary analysis, 5 excluded owing to missing CDC-criteria data; surgeon preference exclusions 12 (8 died, 2 withdrew, 2 lost), 398 completed, 394 primary analysis, 4 excluded owing to missing CDC-criteria data. | PDF p. 3 Figure 1 and footnote c |
| N010 | Death footnote: 25 total deaths reported (10 iNPWT, 15 surgeon preference); 12 supplied primary-outcome data before death (5, 7) and were included in primary analysis. | PDF p. 3 Figure 1 footnote b |
| N011 | Recruitment narrative: 19 were withdrawn after randomization before trial-related data (16 Australia consent-paperwork issues; 3 withdrew); remaining `n=821` was iNPWT 411 and surgeon preference 410. | PDF p. 4 Recruitment |
| N012 | Retained-population description: mean age 63.8 (range 18.8-95.3); 390/821 (48%) male; mean BMI 27.1; ASA class 3-5 444/821 (54%); clean 197/821 (24%), clean-contaminated 351/821 (43%), contaminated 160/821 (19%), dirty 113/821 (14%). | PDF p. 6 Results—Recruitment |
| N013 | iNPWT durability: 382/411 (93%) retained dressing at least 3 days or until earlier discharge; 264/411 (64%) retained it all 7 days or until earlier discharge. | PDF p. 6 Adherence |

## Table 1 — baseline data

**Table label and denominators:** Table 1, `No. of participants (%)`; iNPWT `n=411`, surgeon preference `n=410`, except stated row denominators. All values below are iNPWT vs surgeon preference.

| ID | Measure / complete values | Exact location |
|---|---|---|
| N014 | Age, mean (SD), years: 63.8 (15.9) vs 63.7 (16.4). | PDF p. 5 Table 1 |
| N015 | Sex: male 204 (49.6%) vs 186 (45.4%); female 207 (50.4%) vs 224 (54.6%). | PDF p. 5 Table 1 |
| N016 | BMI, mean (SD) [No.]: 27.1 (7.4) [398] vs 27.2 (7.0) [388]. | PDF p. 5 Table 1 |
| N017 | Smoking (total No. 405 vs 402): never 220 (53.5%) vs 223 (54.4%); currently 95 (23.1%) vs 70 (17.1%); previously 90 (21.9%) vs 109 (26.6%). | PDF p. 5 Table 1 |
| N018 | Diabetes: 40 (9.7%) vs 40 (9.8%). Management among diabetes totals: diet 13/40 (32.5%) vs 9/40 (22.5%); tablet 16/40 (40.0%) vs 21/40 (52.5%); insulin 11/40 (27.5%) vs 10/40 (25.0%). | PDF p. 5 Table 1 |
| N019 | Serum albumin, mean (SD), g/L [No.]: 33.9 (8.4) [406] vs 34.6 (8.0) [405]. Immunosuppressive therapy: 39 (9.5%) vs 41 (10.0%). | PDF p. 5 Table 1 |
| N020 | Clinically jaundiced or bilirubin >50 micromol/L: 4 (1.0%) vs 1 (0.2%). Active malignancy: 84 (20.4%) vs 76 (18.5%). | PDF p. 5 Table 1 |
| N021 | Country: UK 264 (64.2%) vs 265 (64.6%); Australia 147 (35.8%) vs 145 (35.4%). | PDF p. 5 Table 1 |
| N022 | Operative contamination: clean 98 (23.8%) vs 99 (24.1%); clean-contaminated 175 (42.6%) vs 176 (42.9%); contaminated 81 (19.7%) vs 79 (19.3%); dirty 57 (13.9%) vs 56 (13.7%). | PDF p. 5 Table 1 |
| N023 | Stoma present: preexisting 22 (5.3%) vs 27 (6.6%); formed during operation 131 (31.9%) vs 126 (30.7%). | PDF p. 5 Table 1 |
| N024 | ASA class: I 29 (7.1%) vs 29 (7.1%); II 162 (39.4%) vs 157 (38.3%); III 173 (42.1%) vs 178 (43.4%); IV 43 (10.5%) vs 43 (10.5%); V 4 (1.0%) vs 3 (0.7%). | PDF p. 5 Table 1 |
| N025 | Prophylactic antibiotics: induction 310 (75.4%) vs 332 (81.0%); during procedure 80 (19.5%) vs 61 (14.9%); induction and during procedure 8 (1.9%) vs 8 (2.0%); continued postoperatively 234 (56.9%) vs 236 (57.6%). | PDF p. 5 Table 1 |
| N026 | Skin preparation (total No. 411 vs 409): 2% alcoholic chlorhexidine 192 (46.7%) vs 183 (44.6%); 0.5% alcoholic chlorhexidine 56 (13.6%) vs 62 (15.1%); aqueous povidone-iodine 54 (13.1%) vs 52 (12.7%); alcoholic povidone-iodine 44 (10.7%) vs 46 (11.2%); 2% aqueous chlorhexidine 34 (8.3%) vs 32 (7.8%); 0.5% aqueous chlorhexidine 28 (6.8%) vs 33 (8.0%); other 3 (0.7%) vs 1 (0.2%). | PDF p. 6 Table 1 continuation |

## Table 2 — intraoperative data

**Table label and denominators:** Table 2, `No. of participants (%)`; iNPWT `n=411`, surgeon preference `n=410`, except stated row denominators. Table footnotes define colonic/noncolonic/nonbowel procedures, wound-edge device, incise drape, and seniority equivalents.

| ID | Measure / complete values | Exact location |
|---|---|---|
| N027 | Actual procedure: bowel colonic 202 (49.1%) vs 198 (48.3%); bowel noncolonic 97 (23.6%) vs 99 (24.1%); nonbowel 112 (27.3%) vs 112 (27.3%); other 0 vs 1 (0.2%). | PDF p. 7 Table 2 |
| N028 | Surgical approach: open midline 359 (87.3%) vs 366 (89.3%); open nonmidline 18 (4.4%) vs 9 (2.2%); laparoscopic assisted/converted 34 (8.3%) vs 35 (8.5%). | PDF p. 7 Table 2 |
| N029 | Incision length, median (IQR), cm [No.]: 20 (15-25) [395] vs 17.3 (14-23) [392]. WHO safety checklist: 402 (97.8%) vs 402 (98.0%). MRSA colonization: 3 (0.7%) vs 9 (2.2%). Malignancy present: 106 (25.8%) vs 110 (26.8%). | PDF p. 7 Table 2 |
| N030 | Estimated blood loss (total No. 407 vs 406): <100 mL 274 (66.7%) vs 249 (60.7%); 100-500 mL 115 (28.0%) vs 144 (35.1%); 501-1000 mL 16 (3.9%) vs 9 (2.2%); >1000 mL 2 (0.5%) vs 4 (1.0%). | PDF p. 7 Table 2 |
| N031 | Intraoperative blood transfusion: 13 (3.2%) vs 15 (3.7%). Inotropes at end: 74 (18.0%) vs 79 (19.3%). Wound-edge protection device: 107 (26.0%) vs 99 (24.1%). Triclosan-impregnated suture: 3 (0.7%) vs 8 (2.0%). Catheters for local anesthetic infiltration: 169 (41.1%) vs 205 (50.0%). | PDF p. 7 Table 2 |
| N032 | Adhesive/incise drape: iodine-impregnated 18 (4.4%) vs 23 (5.6%); plain 68 (16.5%) vs 64 (15.6%). Wound/incision wash: povidone-iodine 72 (17.5%) vs 73 (17.8%); saline/water 104 (25.3%) vs 113 (27.6%); other 21 (5.1%) vs 20 (4.9%). | PDF p. 7 Table 2 |
| N033 | Gloves changed before closing: 148 (36.0%) vs 148 (36.1%). Instruments changed: 39 (9.5%) vs 39 (9.5%). Skin closure: staples 233 (56.7%) vs 215 (52.4%); continuous sutures 178 (43.3%) vs 190 (46.3%); interrupted sutures 0 vs 5 (1.2%). | PDF p. 7 Table 2 |
| N034 | Operating surgeon level: consultant 319 (77.6%) vs 318 (77.6%); registrar 123 (29.9%) vs 110 (26.8%); senior house officer 4 (1.0%) vs 1 (0.2%). | PDF p. 7 Table 2 |
| N035 | Surgeon closing fascia: consultant 201 (48.9%) vs 193 (47.1%); registrar 218 (53.0%) vs 225 (54.9%); senior house officer 26 (6.3%) vs 15 (3.7%). Surgeon closing skin: consultant 115 (28.0%) vs 102 (24.9%); registrar 214 (52.1%) vs 241 (58.8%); senior house officer 96 (23.4%) vs 73 (17.8%). | PDF p. 7 Table 2 continuation |
| N036 | Total operation duration, median (IQR), min [No.]: 120 (90-180) [408] vs 120 (90-180) [405]. | PDF p. 7 Table 2 continuation |

## Primary, secondary, and safety outcome relationships

**Table label and interpretation:** Table 3 is adjusted for minimization variables. It reports `No./total No. (%)` unless otherwise indicated. Relative risks <1 and absolute differences <0 favor iNPWT. LOS effects are ratio of geometric means after log transformation. SF-12 scores range 0-100 (higher better); pain 1-10 (1=no pain, 10=worst); acceptability 1-10 (1=completely acceptable, 10=totally unacceptable).

| ID | Complete relationship / reported values | Exact location |
|---|---|---|
| S005 | **Primary SSI within 30 days:** 112/394 (28%; narrative/abstract 28.4%) vs 108/394 (27%; narrative/abstract 27.4%); adjusted RD 0.010 (95% CI -0.050 to 0.071); adjusted RR 1.03 (0.83-1.28); P=.78. Matching narrative calls the finding robust. | PDF p. 8 Table 3; PDF p. 6 Primary Outcome; PDF p. 1 Results |
| S006 | Per-protocol primary sensitivity: RR 1.00 (95% CI 0.80-1.25), P=.98; narrative directs to eFigure 3, Supplement 3. Table 3/primary narrative also direct to eTable 6, Supplement 3. | PDF p. 6 Primary Outcome |
| S007 | LOS, UK only, median (IQR) days: 9 (7-15) vs 11 (7-16); ratio of geometric means 0.91 (0.82-1.02); P=.12. | PDF p. 8 Table 3; PDF p. 6 Secondary Outcomes |
| S008 | LOS, UK and Australia, median (IQR) days: 8 (6-14) vs 9 (6-14.5); ratio of geometric means 0.96 (0.88-1.06); P=.21. | PDF p. 8 Table 3; PDF p. 6 Secondary Outcomes; PDF p. 1 Results |
| S009 | SF-12 physical component at 30 days, mean (SD): 36.1 (9.8) vs 37.2 (10.2); adjusted mean difference -0.86 (-2.83 to 1.11); P=.39. | PDF p. 8 Table 3 |
| S010 | SF-12 mental component at 30 days, mean (SD): 46.9 (11.8) vs 47.7 (12.0); adjusted mean difference -1.90 (-4.28 to 0.47); P=.12. | PDF p. 8 Table 3 |
| S011 | Pain at primary laparotomy site, day 7, mean (SD): 2.6 (2.1) vs 3.0 (2.2); adjusted mean difference -0.41 (-0.70 to -0.12); P=.01. Narrative describes difference as 0.4 points on a 10-point Likert scale. | PDF p. 8 Table 3; PDF p. 6 Secondary Outcomes/Discussion |
| S012 | Pain at primary laparotomy site, day 30, mean (SD): 1.8 (1.5) vs 1.8 (1.6); adjusted mean difference -0.06 (-0.28 to 0.16); P=.61. | PDF p. 8 Table 3 |
| N037 | Dressing acceptability, mean (SD): 2.5 (2.5) vs 2.1 (2.2); Table 3 reports no effect estimate, interval, or P value. | PDF p. 8 Table 3 |
| S013 | Wound-related hospital readmission by 30 days: 11/399 (3%) vs 11/398 (3%); RD 0.010 (-0.014 to 0.034); RR 1.02 (0.45-2.31); P=.96. | PDF p. 8 Table 3; PDF p. 6 Secondary Outcomes |
| S014 | Wound complications through 30 days: 73/392 (19%) vs 71/397 (18%); RD 0.007 (-0.046 to 0.060); RR 1.04 (0.78-1.39); P=.79. | PDF p. 8 Table 3; PDF p. 6 Secondary Outcomes |
| N038 | Wound-complication Clavien-Dindo grades: I 53 vs 47; II 16 vs 17; III 4 vs 7; IV 0 vs 0; V 0 vs 0. | PDF p. 8 Table 3 |
| N039 | Safety: patients with at least one SAE 158/411 (38%) vs 165/410 (40%); total SAEs 237 vs 259; 30-day mortality 10/411 (2%; narrative 2.4%) vs 14/410 (3%; narrative 3.4%). Narrative total SAEs 496. | PDF p. 8 Table 3; PDF p. 6 Safety Outcomes |
| N040 | Specific SAE narrative: enterocutaneous fistulae 0/411 vs 1/410; adverse skin reactions 5/411 vs 2/410. | PDF p. 6 Safety Outcomes |
| N041 | Remote-assessment SSI descriptive data: in-person 77/214 (36%) vs 78/209 (37%); video 15/72 (21%) vs 16/76 (21%); phone-only 9/76 (12%) vs 13/76 (17%). | PDF p. 8 Discussion text |
| N042 | Discussion comparison: overall reported SSI rate 28%; no separate effect estimate supplied in this sentence. | PDF p. 8 Discussion text |
| N043 | Generalizability comparison: current-study 30-day mortality 2.9% versus 9.6% in cited UK National Emergency Laparotomy Audit data. | PDF p. 10 Limitations |

## Figure 2 — primary-outcome subgroup relationships

**Figure label/context:** Figure 2; each displayed row reports number with SSI within 30 days and RR (95% CI). Primary analysis denominators are 394 per group. The family P value is the displayed subgroup interaction P value. The pandemic family is UK-based patients only.

| ID | Subgroup family and interaction P | Category: iNPWT events vs surgeon-preference events; RR (95% CI) | Exact location |
|---|---|---|---|
| S015 | Primary analysis (no interaction P) | 112 vs 108; 1.03 (0.83-1.28). | PDF p. 9 Figure 2 |
| S016 | Contamination, P=.28 | Clean 18 vs 24; 0.75 (0.43-1.28). Clean-contaminated 44 vs 35; 1.28 (0.87-1.89). Contaminated 29 vs 23; 1.20 (0.77-1.87). Dirty 21 vs 26; 0.84 (0.55-1.29). | PDF p. 9 Figure 2 |
| S017 | Stoma, P=.14 | No 70 vs 59; 1.19 (0.89-1.60). Yes 42 vs 49; 0.86 (0.62-1.19). | PDF p. 9 Figure 2 |
| S018 | Surgical procedure, P=.81 | Bowel colonic 60 vs 60; 0.96 (0.72-1.28). Bowel noncolonic 29 vs 28; 1.09 (0.71-1.66). Nonbowel 23 vs 20; 1.14 (0.67-1.94). | PDF p. 9 Figure 2 |
| S019 | BMI, P=.81 | <18.5: 5 vs 4; 0.93 (0.30-2.89). 18.5-24.9: 33 vs 37; 0.94 (0.62-1.41). 25.0-29.9: 30 vs 30; 0.94 (0.62-1.42). >=30.0: 41 vs 32; 1.18 (0.82-1.70). | PDF p. 9 Figure 2 |
| S020 | Incision length, P=.42 | <15 cm: 21 vs 22; 1.28 (0.76-2.16). >=15 cm: 90 vs 81; 1.01 (0.79-1.29). | PDF p. 9 Figure 2 |
| S021 | Skin preparation, P=.68 | 2% alcoholic chlorhexidine 51 vs 44; 1.10 (0.79-1.55). Aqueous povidone-iodine 19 vs 16; 1.15 (0.69-1.94). All other 42 vs 48; 0.92 (0.65-1.30). | PDF p. 9 Figure 2 |
| S022 | Country, P=.52 | UK 79 vs 73; 1.08 (0.83-1.40). Australia 33 vs 35; 0.92 (0.61-1.39). | PDF p. 9 Figure 2 |
| S023 | Assessment method, P=.67 | In-person visualization 77 vs 78; 0.96 (0.75-1.23). Remote video/image 15 vs 16; 1.02 (0.54-1.91). Remote without visualization 9 vs 13; 0.67 (0.31-1.48). | PDF p. 9 Figure 2 |
| S024 | SARS-CoV-2 pandemic, P=.68, UK only | Before March 11, 2020: 60 vs 55; 1.11 (0.83-1.50). On/after March 11, 2020: 19 vs 18; 0.98 (0.58-1.65). | PDF p. 9 Figure 2 |

## Matching narrative claims and source cross-references

| ID | Matching claim / reference | Exact location |
|---|---|---|
| N044 | Key Points repeats that 840 adults were randomized and reports no statistically significant 30-day SSI difference, 28.4% vs 27.4%. | PDF p. 2 Key Points |
| N045 | Abstract says the primary finding was consistent across preplanned contamination, stoma, BMI, and skin-preparation subgroups and all preplanned sensitivity analyses. | PDF p. 1 Results |
| N046 | Narrative says no evidence treatment effect differed by participant or operative characteristics; this refers to Figure 2. | PDF p. 6 Primary Outcome; PDF p. 9 Figure 2 |
| N047 | Narrative says wound complications 19% vs 18%, RR 1.04 (0.78-1.39), P=.79, and wound-related readmission 3% vs 3%, RR 1.02 (0.45-2.31), P=.96; it directs to eTables 5a-5b in Supplement 3. | PDF p. 6 Secondary Outcomes |
| N048 | Narrative says no quality-of-life difference and directs to eTables 2-4 in Supplement 3. | PDF p. 6 Secondary Outcomes |
| N049 | Main article directs to eTable 6 (primary outcome), eFigure 3 (per-protocol), eFigure 2 (CDC criteria), and eFigure 4 (tipping-point analysis) in Supplement 3; these are cross-source result locations for downstream matching. | PDF pp. 4 and 6 |
| N050 | Conclusion claim: findings do not support routine iNPWT for SSI reduction in adults undergoing emergency laparotomy. It occurs in the abstract and conclusion. | PDF p. 1 Conclusions and Relevance; PDF p. 10 Conclusion |

## Mapping completion summary

- **Assigned direct-source units:** DOC-001 PDF pp. 1-11 (11 pages), all reusable-backed.
- **Mapped units:** 11/11; **fresh-required units in this assigned scope:** 0.
- **Relationships mapped:** 50 numeric/reporting relationships (`N001-N050`) and 24 statistical/model relationships (`S001-S024`), **74 total**.
- **Gaps:** No scientific-coverage gap in the assigned main-PDF scope. Some source text directs to Supplement 3 for eTables/eFigures; those linked direct-source units are outside this shard and are recorded as cross-source locators, not mapped here as substitute evidence.
