# Support Quantitative Evidence Mapping

Fresh-source mapping limited to DOC-002 (`joi170077supp1_prod.pdf`, protocol/research strategy, PDF pp. 1-21) and DOC-003 (`joi170077supp2_prod.pdf`, results supplement, PDF pp. 1-12). Evidence used only the new native/layout page text and the matching fresh 200-dpi renders listed in `evidence_asset_inventory.md`. Direct observation is distinguished below from any calculation; this document registers no candidate.

## Page-by-page coverage

| Source/page | Coverage disposition | Result-relevant quantitative content / reason |
|---|---|---|
| DOC-002 pp. 1-4 | COMPLETE — contextual only | Background literature and prior-study values (including >15,000 surveys/interviews, 30%, 66%, 42%, 29%, 523/390 [75%], 85%) are not results or definitions for this trial; no concrete comparator to the reported trial result. |
| DOC-002 p. 5 | COMPLETE | Four-arm cluster-randomized trial design, planned hospital/mother/group/follow-up totals, and Figure 1. |
| DOC-002 pp. 6-7 | COMPLETE — methods/context | Curriculum details; the only numerical values are a prior intervention’s 42% to 75% adherence, video duration ~2 minutes, 5-7 videos and `>1`/`1` race-group descriptors. They are not trial results. |
| DOC-002 p. 8 | COMPLETE | mHealth timing/frequency and Table 1 intervention algorithm; focus-group eligibility and planned group size/incentives begin here. |
| DOC-002 p. 9 | COMPLETE | Table 2: 32 SAFE hospitals, annual births, quarters; baseline sampling/recruitment and 25% Black enrollment target. |
| DOC-002 pp. 10-12 | COMPLETE | eligibility, planned recruitment, follow-up timing/procedures, response target, and survey/data-management definitions. |
| DOC-002 pp. 13-14 | COMPLETE | prespecified factorial GEE analysis plan, outcomes, covariates, multiplicity rule, planned sample and simulated power. |
| DOC-002 p. 15 | COMPLETE | self-report limitation and five-year recruitment/follow-up timeline (planned 1,600 mothers). |
| DOC-002 pp. 16-20 | COMPLETE — references only | Bibliographic pages; no protocol result/definition needing comparison. |
| DOC-002 p. 21 | COMPLETE — no applicable content | Printed page number only (894), visually confirmed by fresh render. |
| DOC-003 p. 1 | COMPLETE | Contents enumerate eTables 1-5/eFigure and define supplement scope. |
| DOC-003 p. 2 | COMPLETE | eTable 1, 24 video topics (11 safe-sleep and 13 breastfeeding topics); intervention-content inventory, no outcome number. |
| DOC-003 pp. 3-4 | COMPLETE | eTable 2 respondent/nonrespondent characteristics, totals, counts, percentages and chi-square P values. |
| DOC-003 pp. 5-6 | COMPLETE | eTable 3 baseline SAFE participant characteristics for the four trial groups; all displayed group N/count/percent values. |
| DOC-003 pp. 7-8 | COMPLETE | eTable 4 imputation analysis: four outcomes, counts/percentages, adjusted risks/risk differences/CIs/P values, interaction P values, definitions/adjustments. |
| DOC-003 pp. 9-10 | COMPLETE | eTable 5 race/ethnicity-stratified control versus combined safe-sleep counts, denominators and percentages; eFigure scope note. |
| DOC-003 p. 11 | COMPLETE | eFigure graphical rendering of eTable 5 outcomes; label uses `>60 days` whereas eTable 5 uses `≥60 days`. No numeric plot labels beyond the 0-100 percentage axis; data key is eTable 5. |
| DOC-003 p. 12 | COMPLETE — references only | Two eReferences; no result/definition needing comparison. |

## Protocol quantitative definitions and planned relationships (DOC-002)

### Design, units, populations, timing, and contrasts

- **PDF p. 5, direct observation.** Planned sampling frame: 32 SAFE hospitals; 16 selected sites. Hospitals are matched in sets of four, then randomized to four groups, **four hospitals/group**. Planned enrollment is **1,600 mothers** (100/hospital; 400/group); estimated follow-up response is **80%**, yielding **320 mothers/group**. Figure 1 labels Group 1 Safe Sleep NQI + Breastfeeding mHealth; Group 2 Breastfeeding NQI + Safe Sleep mHealth; Group 3 Safe Sleep NQI + Safe Sleep mHealth; Group 4 Breastfeeding NQI + Breastfeeding mHealth. Analysis/randomization unit: hospital; participant/sample unit: mother (with infant-care report). Main-paper match key: `design_2x2_factorial_16_hospitals_1600_enrolled`.
- **PDF p. 8, direct observation.** Within 72 hours of enrollment, emails begin and are sent twice weekly until infant age 2 months; messages are group-assigned and tailored. Focus-group mothers: English-speaking, infant <6 months, regular (at least weekly) email access; 3-5 focus groups/subgroup, then more until saturation; 6-8 people/group; $50 maternal and $25 nursery-staff gift cards.
- **PDF p. 9, direct observation.** SAFE probability sample: US hospitals delivering ≥100 newborns/year; 32 hospitals listed in Table 2. Each hospital plans ~40 mothers/year in assigned quarter, total ~1,250/year (2011-2013). Site matching considers racial/ethnic mix, hospital size and baseline adherence; mother sampling is designed so 25% of enrolled mothers are Black. All eight completed-quarter-1 hospitals supplied support letters.
- **PDF p. 10, direct observation.** At each hospital, 100 recruited mothers are exposed to hospital-assigned NQI and mHealth curriculum, providing baseline and 2-5-month survey data. Eligibility/exclusions include US residence, healthy infant/well nursery, English speaking and email ability; for multiple births, one infant randomly selected. Planning assumptions: 85% eligible and 75% of eligible agree; approach ~160 mothers/hospital to recruit 100/hospital.
- **PDF pp. 11-12, direct observation.** Initial interview occurs in postpartum stay. Follow-up is one survey at 2-5 months, online or telephone. Online noncompletion prompts second email at one week; then telephone one week later. Telephone nonresponse triggers at least 10 attempts; then mail survey and second mailing after two weeks. Follow-up incentive $10; planned/SAFE response rate 80%. Main-paper match key: `followup_maternal_survey_2_to_5_months` and `loss_to_followup_337_of_1600`.

### Prespecified outcomes, model, adjustment, and thresholds

- **PDF p. 13, direct observation.** 2x2 factorial design; hospital-level randomization; GEE logistic regression accounts for within-hospital clustering and permits individual/hospital covariates. Primary safe-sleep outcomes: supine sleep position, no bed sharing, pacifier use, avoiding soft bedding. Interaction model includes NQI indicator, mHealth indicator, and interaction; covariates include hospital pre-intervention outcome prevalence and individual child age (2-5 months). If interaction is significant, use interaction model for individual and combined effects; otherwise a main-effect model describes NQI and mHealth effects. Main-paper match key: `GEE_logistic_primary_safe_sleep_outcomes`.
- **PDF p. 13, direct observation.** Planned primary multiplicity: four safe-sleep outcomes; Bonferroni overall two-tailed alpha 0.05, comparison-wise alpha **0.0125**. Secondary mediation uses Baron-Kenny sequence, GEE linear regression for mediator and GEE logistic regression for sleep position. Breastfeeding secondary outcomes are exclusive and any breastfeeding, each in the two weeks before follow-up and at discharge; evaluated with GEE logistic regression.
- **PDF p. 14, direct observation.** Planned enrollment 100 mothers × 16 hospitals = 1,600 (400/group); 80% follow-up yields 320/group, 1,280 overall. Simulation scenario: baseline prevalence 0.50-0.60; 10 percentage-point improvement for each intervention and 20 points for both; Bonferroni alpha 0.0125; average intracluster correlation 0.002; reported planned power **96%** for either main effect and **80%** for both interventions versus one alone. These are protocol projections, not observed trial estimates.
- **PDF p. 15, direct observation.** Timeline projects 200 mothers per recruitment period and cumulative recruitment of 1,600, with projected maternal follow-ups shown as 80/160 per periods; timeline is an operational projection, not observed flow.

## Results supplement: complete displayed quantitative evidence (DOC-003)

### eTable 2 — respondents and nonrespondents (PDF pp. 3-4)

Direct observation. Population: enrolled mothers at birth hospitalization, respondents N=1,263, nonrespondents N=337, total N=1,600; P values are chi-square comparisons of respondents versus nonrespondents (footnote). Values are `respondent / nonrespondent / total`, each count (percent):

| Variable | Displayed values | Chi-square P |
|---|---|---:|
| Infant sex: male; female | 616 (48.8) / 171 (50.7) / 787 (49.2); 647 (51.2) / 166 (49.3) / 813 (50.8) | 0.5206 |
| Parity: 1; 2; ≥3 | 526 (41.6) / 140 (41.5) / 666 (41.6); 419 (33.2) / 98 (29.1) / 517 (32.3); 318 (25.2) / 99 (29.4) / 417 (26.1) | 0.2039 |
| Mother age: <20 y; 20-29 y; ≥30 y | 85 (6.7) / 37 (11.0) / 122 (7.6); 644 (51.0) / 205 (60.8) / 849 (53.1); 534 (42.3) / 95 (28.2) / 629 (39.3) | <.0001 |
| Race/ethnicity: NH White; NH Black; Hispanic; Other | 414 (32.8) / 71 (21.1) / 485 (30.3); 344 (27.2) / 133 (39.5) / 477 (29.8); 408 (32.3) / 112 (33.2) / 520 (32.5); 97 (7.7) / 21 (6.2) / 118 (7.4) | <.0001 |
| Education: <high school; high school/GED; some college; college+ | 88 (7.0) / 44 (13.1) / 132 (8.3); 312 (24.8) / 117 (34.8) / 429 (26.9); 438 (34.8) / 110 (32.7) / 548 (34.4); 420 (33.4) / 65 (19.3) / 485 (30.4) | <.0001 |
| Marital: married; never; separated/divorced/widowed | 640 (51.3) / 106 (31.9) / 746 (47.2); 552 (44.2) / 209 (63.0) / 761 (48.2); 56 (4.5) / 17 (5.1) / 73 (4.6) | <.0001 |
| Income: <$20,000; $20,000-49,999; ≥$50,000; unknown | 181 (14.3) / 53 (15.7) / 234 (14.6); 239 (18.9) / 73 (21.7) / 312 (19.5); 435 (34.4) / 57 (16.9) / 492 (30.8); 408 (32.3) / 154 (45.7) / 562 (35.1) | <.0001 |
| Respondent infant age at follow-up: 8-11; 12-15; 16-19; ≥20 weeks | 917 (72.7) / -- / 917 (72.7); 172 (13.6) / -- / 172 (13.6); 87 (6.9) / -- / 87 (6.9); 87 (6.9) / -- / 87 (6.9) | -- |

Cross-document match keys: `enrolled_1600_followed_1263_lost_337`; `respondent_demographics_table1`; `followup_age_distribution`.

### eTable 3 — pre-study SAFE baseline characteristics (PDF pp. 5-6)

Direct observation. Population: SAFE participants at birth hospitalization, used to calculate baseline practice rates. Columns are the four NQI/mHealth group combinations in this order: BF/BF N=417; Safe-Sleep-NQI/BF-mHealth N=387; BF-NQI/Safe-Sleep-mHealth N=421; Safe-Sleep/Safe-Sleep N=379. Displayed `count (percent)` values respectively:

| Characteristic/category | BF/BF | SS-NQI/BF-mH | BF-NQI/SS-mH | SS/SS |
|---|---|---|---|---|
| Sex male; female | 210 (50.4); 207 (49.6) | 203 (52.5); 184 (47.5) | 212 (50.5); 208 (49.5) | 198 (52.4); 180 (47.6) |
| Parity 1; 2; >3 | 184 (44.3); 137 (33.0); 94 (22.7) | 138 (35.8); 139 (36.0); 109 (28.2) | 149 (35.5); 142 (33.8); 129 (30.7) | 159 (42.0); 120 (31.7); 100 (26.4) |
| Mother age <20; 20-29; ≥30 y | 30 (7.2); 213 (51.1); 174 (41.7) | 33 (8.5); 197 (50.9); 157 (40.6) | 24 (5.7); 222 (52.7); 175 (41.6) | 39 (10.3); 213 (56.2); 127 (33.5) |
| NH White; NH Black; Hispanic; Other | 155 (37.3); 110 (26.4); 99 (23.8); 52 (12.5) | 93 (24.0); 183 (47.3); 72 (18.6); 39 (10.1) | 155 (36.8); 120 (28.5); 96 (22.8); 50 (11.9) | 117 (30.9); 97 (25.6); 130 (34.3); 35 (9.2) |
| Education <HS; HS/GED; some college; college+ | 20 (4.8); 86 (20.6); 139 (33.3); 172 (41.2) | 54 (14.0); 109 (28.2); 115 (29.7); 109 (28.2) | 17 (4.0); 100 (23.8); 155 (36.8); 149 (35.4) | 51 (13.5); 87 (23.1); 123 (32.6); 116 (30.8) |
| Married; never; separated/divorced/widowed | 232 (56.0); 166 (40.1); 16 (3.9) | 162 (41.9); 212 (54.8); 13 (3.4) | 243 (58.0); 157 (37.5); 19 (4.5) | 168 (44.6); 183 (48.5); 26 (6.9) |
| Income <$20k; $20-49,999; ≥$50k; unknown | 121 (29.0); 81 (19.4); 83 (19.9); 132 (31.7) | 161 (41.6); 81 (20.9); 44 (11.4); 101 (26.1) | 105 (24.9); 101 (24.0); 98 (23.3); 117 (27.8) | 156 (41.2); 79 (20.8); 68 (17.9); 76 (20.1) |
| Follow-up age 8-11; 12-15; 16-19; ≥20 weeks | 255 (61.2); 72 (17.3); 42 (10.1); 48 (11.5) | 253 (65.4); 51 (13.2); 44 (11.4); 39 (10.1) | 238 (56.5); 83 (19.7); 44 (10.5); 56 (13.3) | 209 (55.1); 79 (20.8); 35 (9.2); 56 (14.8) |

Footnote 1/2 identifies SAFE sources; `GED` means General Equivalency Diploma. Main-paper match key: `SAFE_baseline_table2_group_denominators_417_387_421_379`.

### eTable 4 — imputation analysis (PDF pp. 7-8)

Direct observation. Analysis population: imputed N=400 in each of four randomized cells. Columns: BF-NQI/BF-mHealth (control); SS-NQI/BF-mHealth; BF-NQI/SS-mHealth; SS-NQI/SS-mHealth. All outcomes refer to past two weeks at infant age ≥60 days. `aR` is adjusted risk (%) and `aRD` adjusted risk difference calculated from logistic-regression odds ratios and CIs. All listed adjusted models include infant age at survey/sex and maternal age, parity, race, education, marital status, income, and hospital pre-study SAFE outcome rate; soft-bedding model lacks that pre-study rate. P values are Hochberg-adjusted logistic-regression P values for multiple outcomes; interaction P is multiplicative-interaction logistic-regression test.

| Outcome/printed comparison | Cell counts and percents | Adjusted printed values |
|---|---|---|
| Usual supine position | 315 (78.8%); 302 (75.5%); 348 (87.0%); 364 (90.9%) | NQI: aRC=78.8, aRNQI=81.6, aRDNQI=2.8 (-3.7, 7.9), p=0.38. mHealth: aRC=78.8, aRmH=87.8, aRDmH=9.0 (4.2, 12.6), p=0.003. Interaction p=0.05. |
| Room sharing without bedsharing | 279 (69.7%); 298 (74.6%); 316 (79.0%); 340 (85.0%) | NQI: aRC=69.7, aRNQI=73.6, aRDNQI=3.9 (-1.1, 8.4), p=0.38. mHealth: aRC=69.7, aRmH=81.7, aRDmH=12.0 (8.1, 15.3), p<0.001. Interaction p=0.55. |
| No soft bedding use | 270 (67.4%); 271 (67.7%); 310 (77.5%); 326 (81.6%) | NQI: aRC=67.4, aRNQI=70.8, aRDNQI=3.4 (-2.6, 8.9), p=0.38. mHealth: aRC=67.4, aRmH=79.1, aRDmH=11.7 (6.9, 15.8), p<0.001. Interaction p=0.50. |
| Any pacifier use | 241 (60.2%); 264 (66.1%); 274 (68.6%); 295 (73.7%) | NQI: aRC=60.2, aRNQI=65.9, aRDNQI=5.7 (-1.0, 11.9), p=0.38. mHealth: aRC=60.2, aRmH=67.0, aRDmH=6.8 (0.0, 12.8), p=0.05. Interaction p=0.84. |

Definitions: soft bedding includes heavy blanket/quilt/comforter, rug, stuffed toys, cushion/pillow, adult sleeping bag, cloth diaper/towel, pad over sheet, bumpers, sleep positioners/wedges. Any pacifier use includes `usually` or `sometimes`. Main-paper match key: `imputation_analysis_four_safe_sleep_outcomes`.

### eTable 5 and eFigure — race/ethnicity results (PDF pp. 9-11)

Direct observation. Comparison is BF-NQI/BF-mHealth control versus SS-NQI/SS-mHealth combined intervention, at age ≥60 days in eTable 5. Each cell displays the relevant race-stratum denominator and event count/percent; layout text and render were used together because each N and count wrap across lines. Values are reported in `All; White; Black; Hispanic; Other` order as displayed.

| Outcome/group | Displayed stratum values (denominator, count [percent]) |
|---|---|
| Sleep position, BF/BF | 303, 243 (80.2%); 91, 82 (90.1%); 83, 55 (66.3%); 99, 82 (82.8%); 30, 24 (80.0%) |
| Sleep position, SS/SS | 318, 294 (92.5%); 127, 116 (91.3%); 70, 60 (85.7%); 109, 106 (97.2%); 12, 12 (100%) |
| Room sharing without bedsharing, BF/BF | 291, 205 (70.5%); 88, 64 (72.7%); 78, 53 (67.9%); 95, 70 (73.7%); 30, 18 (60.0%) |
| Room sharing without bedsharing, SS/SS | 313, 269 (85.9%); 126, 108 (85.7%); 66, 57 (86.4%); 109, 93 (85.3%); 12, 11 (91.7%) |
| Any pacifier use, BF/BF | 291, 174 (59.8%); 89, 53 (59.6%); 77, 51 (66.2%); 95, 57 (60.0%); 30, 13 (43.3%) |
| Any pacifier use, SS/SS | 315, 240 (76.2%); 127, 100 (78.7%); 68, 46 (67.6%); 108, 84 (77.8%); 12, 10 (83.3%) |
| No soft bedding, BF/BF | 299, 202 (67.6%); 90, 69 (76.7%); 80, 52 (65.0%); 98, 60 (61.2%); 31, 21 (67.7%) |
| No soft bedding, SS/SS | 320, 262 (81.9%); 128, 106 (82.8%); 70, 56 (80.0%); 110, 90 (81.8%); 12, 10 (83.3%) |

Footnotes: eFigure gives the graphical frequency display; `Other` race/ethnicity is excluded from eFigure. The eFigure title says age `>60 days` while eTable 5 says `≥60 days`; this is a label-boundary observation retained for cross-source review, not a candidate diagnosis here. Figure y axis is percentage 0-100 and has no additional printed data labels. Cross-document match keys: `posthoc_race_ethnicity_control_vs_combined_safe_sleep`, `four_outcomes_age_60_days`.

## Extraction limitations

No direct Office/CSV support source exists. DOC-003 eTable 5 uses dense wrapped layout; the stated denominators were checked against its fresh render and reproduce the printed event percentages to displayed precision. Protocol values are planned design/analysis specifications, not post-trial observations unless a match key identifies a later main-paper comparator.
