# Support Quantitative Evidence Map

## Scope and extraction record

- **Mapper scope:** D002 `joi240078supp1_prod_1739900423.22574.pdf`, PDF pp. 1-15; D003 `joi240078supp2_prod_1739900423.24574.pdf`, PDF pp. 1-16.
- **Unit coverage:** 31/31 assigned PDF pages mapped. D002 pp. 1-15 and D003 pp. 2-3,16 were freshly extracted from the direct PDFs with `pdftotext -layout`; fresh outputs are in `preprocessing/support_fresh/`. D003 pp. 1,4-15 used the designated reusable page-native layout text, with the direct source retained as evidence authority.
- **Fresh extraction outputs:** `preprocessing/support_fresh/D002_p01_layout.txt` through `D002_p15_layout.txt`; `preprocessing/support_fresh/D003_p02_layout.txt`, `D003_p03_layout.txt`, and `D003_p16_layout.txt`.
- **OCR:** not used. The direct and reusable layout text were readable and preserved table labels, values, and footnotes.
- **Main-paper matching convention:** matching keys below name the uniquely identified result/population/time/contrast. They are mapping keys, not a claim that a cross-source comparison has yet been adjudicated.
- **Boundary:** this is an evidence/relationship map only. It contains no candidate diagnosis, disposition, severity, or correction.

## D002 — Supplement 1: Study protocol (fresh pp. 1-15)

### Page-by-page coverage

| PDF page | Content and quantitative mapping status |
|---|---|
| 1 | Protocol contents and section/page index. No result-relevant quantitative relationship beyond section pagination (Background pp. 2-3; Methods pp. 3-5; Protection pp. 6-9; DSMB pp. 8-10; References pp. 11-12; changes p. 13). |
| 2 | Background/program description and historic/preliminary quantities mapped below. |
| 3 | Preliminary-program/young-adult trial results and current-study design/sample plan mapped below. |
| 4 | Randomization, intervention schedules, anticipated follow-up, incentives, and fraud-screening threshold mapped below. |
| 5 | Measurement schedule and primary/secondary outcome definitions mapped below. |
| 6 | Analysis, missing-data sensitivity, and mediation definitions mapped below. |
| 7 | Enrollment definition, consent sequence, and payment maxima mapped below. |
| 8 | Protection/DSMB heading only; no additional result-relevant quantitative relationship. |
| 9 | Safety-administration content; adverse-event definition enumerates six serious-event criteria and a 24-hour reporting target, but no trial result. Recorded as administrative/protocol content, not a result relationship. |
| 10 | DSMB process. Planned interim-analysis frequency/masking is to be determined; quorum is half of standing members plus one and explicitly three members. Administrative/protocol content; no reported result. |
| 11 | Ethical/control-arm and payment rationale only; no additional result-relevant quantitative relationship. |
| 12 | References 1-14 only; no applicable study result. |
| 13 | References 15-28 only; no applicable study result. |
| 14 | References 29-32 only; no applicable study result. |
| 15 | Protocol-change record: baseline measures added (Roberts Loneliness Scale and PEARLS; approvals 2021-10-13 and 2021-11-16), decisional-capacity revision (2021-12-07), and fraud-prevention/attention-check additions (2022-09-08 and 2022-09-14). Definitions relevant to later missingness/measure availability; no outcome result. |

### D002 protocol relationships and definitions

| Local ID | Exact source location | Direct observation / relationship | Main-paper matching key |
|---|---|---|---|
| SUP-N01 | [D002 p. 2](<../../joi240078supp1_prod_1739900423.22574.pdf#page=2>) | Historical background: US high-school e-cigarette use increased from 11.3% (2016) to 27.5% (2019); middle-school use increased 4.3% to 10.5%. Program assessments: at day 14, A=same amount, B=less, C=no JUUL; at days 30/60/90, A=past 7 days, B=8-30 days, C=>30 days. | Context only; outcome-definition precursor for point-prevalence timing. |
| SUP-N02 | [D002 p. 3](<../../joi240078supp1_prod_1739900423.22574.pdf#page=3>) | Preliminary cohort: roughly 27,000 users; about three quarters set a quit date; interactive keyword use 45.5% teens and 38.4% young adults; response 36.9% at day 14 and 21.0% at day 90; 60.8% of day-14 respondents reduced/stopped; day-90 7-day PPA 25% and 30-day PPA 16%. These are prior-program context, not the current RCT result. | Context only. |
| SUP-S01 | [D002 p. 3](<../../joi240078supp1_prod_1739900423.22574.pdf#page=3>) | Prior young-adult RCT (n=2,588, age 18-24): ITT/missing=vaping abstinence 24.1% intervention vs 18.6% control; OR 1.39, 95% CI 1.15-1.68, P<.001. Population and study differ from the assigned adolescent RCT. | Context only; do not match to adolescent primary result. |
| SUP-N03 | [D002 pp. 3-4](<../../joi240078supp1_prod_1739900423.22574.pdf#page=3>) | Planned adolescent study: three arms, with 1,800 randomized to the two main arms (900/arm) and target 450 waitlist; age 13-17, past-30-day e-cigarette use, US residence, interested in quitting within 30 days. Randomization after completed online baseline by survey-software algorithm; complete enrollment requires reply to the first program text within 24 hours. | Trial population/enrollment and randomization key; compare only after population/analysis set is matched. |
| SUP-N04 | [D002 p. 4](<../../joi240078supp1_prod_1739900423.22574.pdf#page=4>) | Intervention: This is Quitting. Assessment-only control: monthly e-cigarette assessments; waitlist: contacts only at 1 and 7 months. Expected follow-up: >=75% at 1 month and 65% at 7 months. Follow-up reimbursement up to $30 per assessment; retention texts $5 each. Bot score <0.5 means likely bot. | Arm/contact schedule and 7-month follow-up key. |
| SUP-N05 | [D002 p. 5](<../../joi240078supp1_prod_1739900423.22574.pdf#page=5>) | Assessments at baseline, 1 month, and 7 months post-randomization. **Primary outcome:** self-reported 30-day point-prevalence abstinence (PPA) at 7 months. Other outcomes: motivation to quit, quit attempts, e-cigarette-use reduction, 7-day PPA, continuous abstinence at each follow-up; satisfaction/recommendation scale 0-10. | **Primary outcome / 7-month 30-day PPA / intervention vs assessment-only control**; also secondary 7-day/repeated PPA key. |
| SUP-S02 | [D002 pp. 5-6](<../../joi240078supp1_prod_1739900423.22574.pdf#page=5>) | Planned primary comparison: logistic regression of 7-month PPA between treatment and control, adjusted for baseline confounders; moderators assessed using treatment-by-selected-variable interactions. Secondary logistic models: quit attempt, reduction, confidence/self-efficacy. | Primary analysis model and moderation key. |
| SUP-S03 | [D002 p. 6](<../../joi240078supp1_prod_1739900423.22574.pdf#page=6>) | Planned missingness: (1) ITT, missing follow-up assumed treatment failure/vaping; (2) multiple imputation under NMAR, with sensitivity range from equal missingness odds OR=1 to fivefold greater missingness for treatment failures OR=5. | **Missing=vaping / MI sensitivity / 7-month PPA** key; compare direction/range only with specified final methods. |
| SUP-S04 | [D002 p. 6](<../../joi240078supp1_prod_1739900423.22574.pdf#page=6>) | Planned mediation: social support and quitting self-efficacy at baseline, 1 month, and 7 months. Proposed conditions: X-Z effect A, Z-Y effect B, X-Y effect C, and attenuation of C when A and B are jointly included. | Mediation-analysis definition; no reported mediation estimate in this protocol. |
| SUP-N06 | [D002 pp. 6-7](<../../joi240078supp1_prod_1739900423.22574.pdf#page=6>) | Enrollment target restated as 1,800 adolescent users. Enrollment occurs only after consent, decisional-capacity check, baseline, random allocation, and response to initial system text. All seven decisional-capacity questions must be correct. | Enrollment/analysis-population definition key. |
| SUP-N07 | [D002 p. 7](<../../joi240078supp1_prod_1739900423.22574.pdf#page=7>) | Follow-ups at 1 and 7 months; $20 each, +$10 if response within 24 hours; intervention and assessment-only arms receive $5 for each of seven text assessments. Claimed maximum total compensation: $95 (=2×$20 + $10 + 7×$5). | Retention/incentive context; potential interpretation key for response analysis only. |
| SUP-N08 | [D002 p. 10](<../../joi240078supp1_prod_1739900423.22574.pdf#page=10>) | DSMB to determine interim-analysis frequency and masking. This is an administrative planned-analysis statement, not evidence of a completed interim analysis or an efficacy result. | Administrative content; no applicable result. |
| SUP-N09 | [D002 p. 15](<../../joi240078supp1_prod_1739900423.22574.pdf#page=15>) | PEARLS and Roberts Loneliness Scale added after launch; missingness for such measures may therefore reflect timing of administration. | Baseline PEARLS/loneliness availability and missingness key. |

## D003 — Supplement 2: results supplement (pp. 1,4-15 reusable-backed; pp. 2-3,16 fresh)

### Page-by-page coverage

| PDF page | Content and quantitative mapping status |
|---|---|
| 1 | Contents. Identifies eAppendices A-D and eTables 1-6; no result values. |
| 2 | eAppendix A intervention detail and sample messages; fresh direct extraction. Message volume/schedule and Day-14 assessment mapping recorded below. |
| 3 | eAppendix A baseline assessment definitions; fresh direct extraction. Demographic response categories and cited external context recorded; no trial outcome table. |
| 4 | eAppendix B multiple-imputation definition, formula components, and sensitivity ranges. |
| 5 | eAppendix C IPRW/complete-case definitions and 7-month responder results. |
| 6 | eAppendix D moderation-model definition and interpretation. |
| 7-8 | eTable 1 item responses: complete value transcription below. |
| 9-10 | eTable 2 assessment-only versus waitlist baseline comparison: complete value transcription below. |
| 11 | eTable 3 missing-data sensitivity table and formulas: complete transcription below. |
| 12-13 | eTable 4 responder versus non-responder baseline comparison: complete transcription below. |
| 14 | eTable 5 7-month responder cessation outcomes: complete transcription below. |
| 15 | eTable 6 moderation coefficients, SEs, nominal and Holm-adjusted P values: complete transcription below. |
| 16 | eReferences only; fresh direct extraction. No applicable study result, formula, or table value. |

### D003 method, definition, and formula relationships

| Local ID | Exact source location | Direct observation / relationship | Main-paper matching key |
|---|---|---|---|
| SUP-N10 | [D003 p. 2](<../../joi240078supp2_prod_1739900423.24574.pdf#page=2>) | This is Quitting schedule: one week before quit date and eight weeks after; 1-3 daily messages until about day 30, then roughly alternate days; no-quit-date users receive 1-3 daily messages for four weeks; roughly one third of messages are interactive. | Intervention dose/schedule key. |
| SUP-N11 | [D003 pp. 2-3](<../../joi240078supp2_prod_1739900423.24574.pdf#page=2>) | Day-14 question: same amount / less / no vaping. Days 30,60,90 question: last vaping in past 7 days / 8-30 days / >30 days. Confidence responses TOTALLY/SOSO/MEH; helpfulness 1-10. | Outcome/instrument timing and response-category key. |
| SUP-N12 | [D003 p. 3](<../../joi240078supp2_prod_1739900423.24574.pdf#page=3>) | Baseline categories: grade (6th through >12th, ungraded/other, not student); gender (male/female/non-binary/other/prefer not); race multi-select; ethnicity yes/no/prefer not; sexuality straight/gay or lesbian/bisexual/other/prefer not. External contextual values: 2021 current vaping 19.8% LGB vs 13.2% heterosexual; 2020-21 gap increase 32% current vaping and 26% ever vaping. | Baseline moderator/population category key; external context not a trial result. |
| SUP-S05 | [D003 p. 4](<../../joi240078supp2_prod_1739900423.24574.pdf#page=4>) | MI sensitivity method: OR.miss is the association of survey nonresponse with vaping; OR.miss=1 is MAR, OR.miss=+infinity means all missing are vaping, all non-1 values are NMAR. Imputation stratifies observed abstinence odds by dichotomized baseline E-cigarette Dependence Scale (median split); M=10,000 imputations per OR.miss. FMI is between-imputation variance / total variance for log(OR.vape). | Missing-data sensitivity / primary 7-month 30-day PPA key. |
| SUP-S06 | [D003 p. 4](<../../joi240078supp2_prod_1739900423.24574.pdf#page=4>) | As OR.miss rises 1/100 to 100, P1-P0 falls 14.16% to 9.92%; OR.vape falls 1.83 to 1.57; RR.vape rises 1.26 to 1.35. Authors state all three metrics remain positive and highly significant and chose RR for the abstract because its range (1.26-1.35) is narrower than OR (1.57-1.84). | Abstract RR / missing=vaping primary result key. |
| SUP-S07 | [D003 p. 5](<../../joi240078supp2_prod_1739900423.24574.pdf#page=5>) | IPRW: model response probability conditional on eTable-4 baseline characteristics, divide by arm-specific overall response rate, then invert stabilized ratios. IPRW balance criterion: SMD 0.2 pooled SD after weighting. Survey-weighted logistic models use R survey package 4.0.2. | Complete-case/IPRW 7-month 30-day and repeated PPA key. |
| SUP-S08 | [D003 p. 5](<../../joi240078supp2_prod_1739900423.24574.pdf#page=5>) | CCA 30-day PPA: 55.1% (287/521) intervention vs 38.3% (208/543) control, RR 1.44 (95% CI 1.26-1.64), P<.001; IPRW RR 1.42 (1.24-1.63), P<.001. Repeated PPA CCA: 25.3% (131/517) vs 11.3% (61/538), RR 2.24 (1.70-2.94), P<.001; IPRW RR 2.21 (1.67-2.93), P<.001. Reported response rates: 68.6% intervention vs 73.0% control, difference 4.4 percentage points. | Complete-case/IPRW 7-month PPA and repeated-PPA key. |
| SUP-S09 | [D003 p. 6](<../../joi240078supp2_prod_1739900423.24574.pdf#page=6>) | Moderation models contain treatment, baseline moderator, and treatment×moderator. Assessment-only control is reference. Beta is treatment-vs-control difference in log-odds of abstinence per moderator unit (or target-vs-reference contrast); multi-category italic overall P values drive Holm adjustment, individual contrasts are illustrative only. | Moderator eTable 6 key. |

### eTable 1 — baseline item responses (D003 pp. 7-8)

Columns are Intervention n=759 and Assessment-only control n=744 unless a bracketed available denominator is supplied. Entries are No. (%) of yes/positive response unless noted. Repeated items appearing under multiple instruments are intentionally retained because the source presents them under separate instrument labels.

| Instrument/item | Intervention | Assessment-only control |
|---|---:|---:|
| Penn State index: usual daily uses, available N | 733 | 727 |
| 0-4; 5-9; 10-14; 15-19; 20-29; 30+ times/day | 121 (16.5); 168 (22.9); 183 (25.0); 96 (13.1); 63 (8.6); 102 (13.9) | 116 (16.0); 164 (22.6); 193 (26.5); 91 (12.5); 62 (8.5); 101 (13.9) |
| Vape within 30 min waking; awakens at night; nights/week if yes mean (SD) | 594 (78.3); 293 (38.6); 3.7 (2.1) | 552 (74.2); 298 (40.1); 3.4 (2.0) |
| Vapes because hard to quit; strong cravings | 575 (75.8); 646 (85.1) | 542 (72.8); 613 (82.4) |
| Urges: no/slight; moderate/strong; very/extremely strong | 94 (12.4); 487 (64.2); 178 (23.5) | 90 (12.1); 461 (62.0); 193 (25.9) |
| Hard to avoid vaping where prohibited | 533 (70.2) | 531 (71.4) |
| On stopping: irritable; nervous/restless/anxious | 625 (82.3); 621 (81.8) | 631 (84.8); 599 (80.5) |
| Hooked on Nicotine Checklist: tried to stop but could not; hard to quit; felt addicted; strong cravings; really needed to vape; hard to avoid where prohibited | 643 (84.7); 575 (75.8); 681 (89.7); 646 (85.1); 635 (83.7); 533 (70.2) | 627 (84.3); 542 (72.8); 663 (89.1); 613 (82.4); 618 (83.1); 531 (71.4) |
| Hooked checklist on stopping: poor concentration; strong need/urge; irritable; nervous/restless/anxious | 538 (70.9); 655 (86.3); 625 (82.3); 621 (81.8) | 555 (74.6); 633 (85.1); 631 (84.8); 599 (80.5) |
| E-cigarette Dependence Scale: reaches without thinking; drops everything to buy; vapes more before prohibited situation; cravings intolerable after hours unable to vape, mean (SD) | 2.6 (1.1); 1.5 (1.1); 2.8 (1.1); 2.1 (1.2) | 2.5 (1.0); 1.5 (1.1); 2.8 (1.1); 2.1 (1.1) |
| e-FTCD: usual daily uses, available N | 733 | 727 |
| e-FTCD daily-use categories 0-4; 5-9; 10-14; 15-19; 20-29; 30+ | 121 (16.5); 168 (22.9); 183 (25.0); 96 (13.1); 63 (8.6); 102 (13.9) | 116 (16.0); 164 (22.6); 193 (26.5); 91 (12.5); 62 (8.5); 101 (13.9) |
| e-FTCD: hard where prohibited | 533 (70.2) | 531 (71.4) |
| e-FTCD preferred time: morning; meals; stressful situation; none | 158 (20.8); 88 (11.6); 470 (61.9); 43 (5.7) | 162 (21.8); 80 (10.8); 451 (60.6); 51 (6.9) |
| e-FTCD: within 30 min waking; more first 2 hours; vapes while bed-ill | 594 (78.3); 322 (42.4); 402 (53.0) | 552 (74.2); 302 (40.6); 369 (49.6) |
| PEARLS available N | 631 | 617 |
| PEARLS adverse events: caregiver jailed; unsupported; caregiver mental-health issue; insulted; caregiver substance problem; lacked care; witnessed screaming; pushed/grabbed/slapped; sexual abuse; caregiver relationship change | 177 (28.1); 440 (69.7); 374 (59.3); 401 (63.5); 272 (43.1); 182 (28.8); 300 (47.5); 217 (34.4); 237 (37.6); 257 (40.7) | 178 (28.8); 410 (66.5); 375 (60.8); 386 (62.6); 261 (42.3); 187 (30.3); 269 (43.6); 203 (32.9); 218 (35.3); 235 (38.1) |
| PEARLS social determinants: violence; discrimination; housing; food; separated caregiver; caregiver serious illness; caregiver died; detained/arrested; romantic-partner abuse | 344 (54.5); 327 (51.8); 167 (26.5); 148 (23.5); 39 (6.2); 83 (13.2); 58 (9.2); 82 (13.0); 218 (34.5) | 347 (56.2); 330 (53.5); 158 (25.6); 147 (23.8); 53 (8.6); 72 (11.7); 53 (8.6); 72 (11.7); 185 (30.0) |
| GAIN-SS internalizing: trapped/lonely/sad; sleep; anxious; reminded of past | 683 (90.0); 650 (85.6); 664 (87.5); 662 (87.2) | 672 (90.3); 656 (88.2); 649 (87.2); 657 (88.3) |
| GAIN-SS substance: alcohol/drugs weekly; much time obtaining/using; continued despite problems; work/school/home problems; withdrawal | 643 (84.7); 582 (76.7); 324 (42.7); 388 (51.1); 296 (39.0) | 630 (84.7); 557 (74.9); 329 (44.2); 392 (52.7); 314 (42.2) |

**eTable 1 relationship key (SUP-N13):** [D003 pp. 7-8](<../../joi240078supp2_prod_1739900423.24574.pdf#page=7>) — baseline nicotine-dependence/psychosocial items, intervention n=759 vs assessment-only n=744; bracketed denominators identify item-specific missingness. Main-paper key: baseline participant characteristics and moderator covariates.

### eTable 2 — assessment-only versus waitlist baseline comparison (D003 pp. 9-10)

Columns are assessment-only n=744, waitlist n=178, SMD. `a` means No. (%) unless otherwise noted; `b` means range 1-5 (1=not at all, 5=very much).

| Characteristic | Assessment-only | Waitlist | SMD |
|---|---:|---:|---:|
| Age, mean (SD) | 16.4 (0.8) | 16.4 (0.8) | 0.05 |
| Grade available N; 6th-8th; 9th; 10th; 11th; 12th; >12th; ungraded/other/not student | 743; 7 (0.9); 29 (3.9); 129 (17.4); 253 (34.1); 277 (37.3); 20 (2.7); 28 (3.8) | 177; 0 (0.0); 7 (4.0); 30 (16.9); 62 (35.0); 70 (39.5); 4 (2.3); 4 (2.3) | 0.17 |
| Gender available N; female; male; non-binary/other | 742; 369 (49.7); 314 (42.3); 59 (8.0) | N not printed; 93 (52.2); 69 (38.8); 16 (9.0) (displayed categories sum to 178) | 0.08 |
| Sexuality available N; LGBQ+; heterosexual | 734; 311 (42.4); 423 (57.6) | 175; 85 (48.6); 90 (51.4) | 0.13 |
| Race available N; American Indian/Alaskan Native; Asian; Black; Native Hawaiian/Other Pacific Islander; White; multiracial; other | 737; 7 (0.9); 20 (2.7); 76 (10.3); 2 (0.3); 461 (62.6); 136 (18.5); 35 (4.7) | 171; 3 (1.8); 4 (2.3); 15 (8.8); 1 (0.6); 117 (68.4); 26 (15.2); 5 (2.9) | 0.18 |
| Hispanic available N; yes; no | 735; 117 (15.9); 618 (84.1) | 174; 33 (19.0); 141 (81.0) | 0.08 |
| Days/month vaping, median (IQR) | 30.0 (26.0-30.0) | 30.0 (25.0-30.0) | 0.04 |
| Motivation; confidence; health-consequence concern, median (IQR) | 4.0 (4.0-5.0); 3.0 (3.0-4.0); 3.0 (3.0-4.0) | 4.0 (3.0-5.0); 3.0 (3.0-4.0); 3.0 (3.0-4.0) | 0.07; 0.04; 0.02 |
| Past-year quit attempts none; 1-2; 3-5; >=6 | 100 (13.4); 249 (33.5); 302 (40.6); 93 (12.5) | 26 (14.6); 63 (35.4); 63 (35.4); 26 (14.6) | 0.11 |
| Penn State index, mean (SD), available N | 11.7 (4.3), 727 | 12.0 (4.4), 171 | 0.06 |
| Dependence Scale; e-FTCD available N; Hooked checklist, mean (SD) | 8.9 (3.3); 4.9 (2.3), 727; 8.1 (2.2) | 9.2 (3.5); 4.9 (2.5), 171; 8.2 (2.2) | 0.07; 0.01; 0.07 |
| Vaping <30 min after waking | 552 (74.2) | 142 (80.0) | 0.13 |
| Perceived addiction: very; somewhat; not at all; don't know | 291 (39.1); 400 (53.8); 16 (2.2); 37 (5.0) | 71 (39.9); 96 (53.9); 3 (1.7); 8 (4.5) | 0.04 |
| GAIN-SS internalizing; substance problems; loneliness, median (IQR) | 4.0 (3.0-4.0); 3.0 (2.0-5.0); 8.0 (6.0-10.0) | 4.0 (3.0-4.0); 3.0 (2.0-4.0); 8.5 (6.0-11.0) | 0.07; 0.05; 0.10 |
| PEARLS available N; high; intermediate; low | 617; 443 (71.8); 143 (23.2); 31 (5.0) | 109; 87 (79.8); 16 (14.7); 6 (5.5) | 0.22 |
| Past-30-day cigarettes; cigars/cigarillos; nicotine pouches; marijuana/cannabis | 257 (34.5); 104 (14.0); 86 (11.6); 549 (73.8) | 49 (27.5); 18 (10.1); 17 (9.6); 119 (66.9) | 0.15; 0.12; 0.07; 0.15 |

Scale footnotes: Penn State 0-20 (0-3 not dependent; 4-8 low; 9-12 medium; >=13 high); Dependence Scale 0-16, higher=greater dependence; e-FTCD 0-10 (0-2 low; 3-4 low/moderate; 5-7 moderate; >=8 high); Hooked 0-10 (>0 indicates loss of some independence); GAIN-SS internalizing 0-4 and substance 0-5 with 0 low, 1-2 moderate, >=3 high; Roberts UCLA Loneliness 0-12, higher=greater loneliness. PEARLS was added after launch, so missing data are due to timing.

**eTable 2 relationship key (SUP-N14):** [D003 pp. 9-10](<../../joi240078supp2_prod_1739900423.24574.pdf#page=9>) — assessment-only vs waitlist baseline distribution/SMD comparison; main-paper key: waitlist-control comparator and planned analysis population.

### eTable 3 — sensitivity to missing-data assumptions (D003 p. 11)

Definitions printed in source: OR.miss=OR associating vaping and survey nonresponse; FMI=fraction of missing information in MI estimate of log(OR.vape); P1/P0=intervention/control abstinence rate (%); Diff.vape=P1-P0; RR.vape=P1/P0; OR.vape=[P1/(1-P1)]/[P0/(1-P0)].

| OR.miss | FMI | P1 | P0 | Diff.vape | RR.vape | OR.vape | P-value |
|---:|---:|---:|---:|---:|---:|---:|---|
| -infinity | 0 | 69.17 | 54.97 | 14.20 | 1.26 | 1.84 | — |
| 1/100 | 2 | 68.71 | 54.55 | 14.16 | 1.26 | 1.83 | .0001 |
| 1/20 | 6 | 67.43 | 53.49 | 13.94 | 1.26 | 1.80 | <.0001 |
| 1/10 | 11 | 65.86 | 52.15 | 13.71 | 1.26 | 1.77 | <.0001 |
| 1/5 | 16 | 63.14 | 49.75 | 13.39 | 1.27 | 1.73 | <.0001 |
| 1/3 | 19 | 60.33 | 47.37 | 12.96 | 1.27 | 1.69 | <.0001 |
| 1/2 | 22 | 57.65 | 45.06 | 12.59 | 1.28 | 1.66 | <.0001 |
| 2/3 | 23 | 55.48 | 43.18 | 12.30 | 1.28 | 1.64 | <.0001 |
| 4/5 | 23 | 53.99 | 41.86 | 12.13 | 1.29 | 1.63 | <.0001 |
| 1 | 23 | 52.26 | 40.48 | 11.79 | 1.29 | 1.61 | .0001 |
| 5/4 | 23 | 50.59 | 39.02 | 11.57 | 1.30 | 1.60 | .0001 |
| 3/2 | 22 | 49.39 | 37.89 | 11.51 | 1.30 | 1.60 | .0001 |
| 2 | 20 | 47.54 | 36.31 | 11.24 | 1.31 | 1.59 | .0001 |
| 3 | 18 | 45.10 | 34.21 | 10.89 | 1.32 | 1.58 | .0001 |
| 5 | 14 | 42.46 | 31.97 | 10.49 | 1.33 | 1.57 | .0001 |
| 10 | 9 | 40.30 | 30.07 | 10.23 | 1.34 | 1.57 | .0001 |
| 20 | 5 | 39.16 | 29.08 | 10.08 | 1.35 | 1.57 | .0001 |
| 100 | 1 | 37.98 | 28.06 | 9.92 | 1.35 | 1.57 | .0001 |
| +infinity | 0 | 37.98 | 28.06 | 9.92 | 1.35 | 1.57 | .0001 |

**eTable 3 relationship key (SUP-S10):** [D003 p. 11](<../../joi240078supp2_prod_1739900423.24574.pdf#page=11>) — 7-month 30-day abstinence intervention vs assessment-only control under stated OR.miss models. The P-value `.0001`/`<.0001` displays are source values; no inference about them is made here.

### eTable 4 — 7-month nonresponders versus responders (D003 pp. 12-13)

Columns are nonresponders n=439, responders n=1,064, SMD, nominal P, and Holm-adjusted P. Entries are No. (%) unless noted; bracketed N is item availability.

| Characteristic | Nonresponder | Responder | SMD | P-nom / P-adj |
|---|---:|---:|---:|---|
| Age mean (SD) | 16.4 (0.9) | 16.4 (0.8) | 0.01 | .882 / 1.000 |
| Grade N; 6th-8th; 9th; 10th; 11th; 12th; >12th; ungraded/other | 436; 7 (1.6); 22 (5.0); 74 (17.0); 139 (31.9); 167 (38.3); 14 (3.2); 13 (3.0) | 1,064; 11 (1.0); 35 (3.3); 175 (16.4); 377 (35.4); 411 (38.6); 21 (2.0); 34 (3.2) | 0.14 | .357 / 1.000 |
| Gender N; female; male; non-binary/other | 436; 254 (58.3); 153 (35.1); 29 (6.7) | 1,057; 501 (47.4); 475 (44.9); 81 (7.7) | 0.22 | .001 / .025 |
| Sexuality N; LGBQ+; heterosexual | 432; 203 (47.0); 229 (53.0) | 1,046; 425 (40.6); 621 (59.4) | 0.13 | .028 / .364 |
| Race N; American Indian/Alaskan; Asian; Black; Native Hawaiian/Other Pacific; White; multiracial; other | 432; 5 (1.2); 7 (1.6); 32 (7.4); 0 (0.0); 301 (69.7); 62 (14.4); 25 (5.8) | 1,053; 13 (1.2); 29 (2.8); 120 (11.4); 5 (0.5); 629 (59.7); 213 (20.2); 44 (4.2) | 0.28 | .002 / .034 |
| Hispanic N; yes; no | 434; 76 (17.5); 358 (82.5) | 1,051; 165 (15.7); 886 (84.3) | 0.05 | .433 / 1.000 |
| Days/month vaping median (IQR) | 30.0 (27.0-30.0) | 29.0 (26.0-30.0) | 0.04 | <.001 / <.025 |
| Motivation; confidence; health concern, median (IQR) | 4.1 (0.8); 3.2 (1.1); 4.0 (3.0-5.0) | 4.1 (0.8); 3.5 (1.1); 3.0 (3.0-4.0) | 0.08; 0.25; 0.08 | .125/.960; <.001/<.025; .120/.960 |
| Quit attempts none; 1-2; 3-5; >=6 | 63 (14.4); 163 (37.1); 150 (34.2); 63 (14.4) | 128 (12.0); 346 (32.5); 451 (42.4); 139 (13.1) | 0.17 | .028 / .364 |
| Penn State index mean (SD), N | 12.5 (4.3), 428 | 11.5 (4.2), 1,025 | 0.25 | <.001 / <.025 |
| Dependence Scale; e-FTCD mean (SD), N; Hooked, mean (SD) | 9.3 (3.6); 5.2 (2.3), 428; 8.3 (2.1) | 8.8 (3.4); 4.8 (2.3), 1,025; 8.0 (2.3) | 0.16; 0.19; 0.13 | .003/.045; <.001/<.025; .053/.530 |
| Within 30 min waking | 363 (82.7) | 783 (73.6) | 0.22 | <.001 / <.025 |
| Perceived addiction: very; somewhat; not; don't know | 212 (48.3); 204 (46.5); 8 (1.8); 15 (3.4) | 397 (37.3); 594 (55.8); 25 (2.3); 48 (4.5) | 0.22 | .001 / .025 |
| GAIN-SS internalizing; substance; loneliness, median (IQR) | 4.0 (4.0-4.0); 3.0 (2.0-5.0); 8.0 (5.0-11.0) | 4.0 (3.0-4.0); 3.0 (2.0-4.0); 8.0 (6.0-10.0) | 0.15; 0.05; 0.04 | .002/.034; .236/1.000; .082/.738 |
| PEARLS N; low; intermediate; high | 362; 22 (6.1); 58 (16.0); 282 (77.9) | 886; 42 (4.7); 208 (23.5); 636 (71.8) | 0.19 | .010 / .140 |
| Past-30-day cigarettes; cigars/cigarillos; nicotine pouches; marijuana/cannabis | 129 (29.4); 39 (8.9); 41 (9.3); 329 (74.9) | 370 (34.8); 159 (14.9); 119 (11.2); 797 (74.9) | 0.12; 0.19; 0.06; <0.01 | .047/.517; .001/.025; .313/1.000; 1.000/1.000 |

Footnotes reproduce the eTable-2 scale definitions above; `SMD`=standardized mean difference; `P-adj`=Holm multiplicity-adjusted P value.

**eTable 4 relationship key (SUP-N15/SUP-S11):** [D003 pp. 12-13](<../../joi240078supp2_prod_1739900423.24574.pdf#page=12>) — response-status baseline comparison for 7-month follow-up, all study arms combined (439 nonresponders + 1,064 responders = 1,503). Main-paper key: 7-month response/retention and missing-data covariates.

### eTable 5 — vaping cessation among 7-month responders (D003 p. 14)

| Outcome / analysis | Intervention | Control | Rate difference (95% CI) | Rate ratio (95% CI) | Odds ratio (95% CI) | P-value |
|---|---|---|---|---|---|---|
| 30-day PPA: no. responses | 521 | 543 | — | — | — | — |
| 30-day PPA: no. abstinent | 287 | 208 | — | — | — | — |
| 30-day PPA CCA | 55.1 (50.6,60.0) | 38.3 (34.7,42.3) | 16.8 (10.9,22.7) | 1.44 (1.26,1.64) | 1.98 (1.55,2.52) | <.001 |
| 30-day PPA IPRW | 53.9 (49.6,58.2) | 37.9 (33.8,42.0) | 16.0 (10.0,22.0) | 1.42 (1.24,1.63) | 1.92 (1.50,2.24) | <.001 |
| 30-day PPA missing=vaping | 37.8 (34.4,41.3) | 28.0 (24.9,31.3) | 9.9 (5.1,14.5) | 1.35 (1.17,1.57) | 1.57 (1.26,1.95) | <.001 |
| Repeated PPA: no. responses | 517 | 538 | — | — | — | — |
| Repeated PPA: no. abstinent | 131 | 61 | — | — | — | — |
| Repeated PPA CCA | 25.3 (21.7,29.6) | 11.3 (9.0,14.2) | 14.0 (9.4,18.6) | 2.24 (1.70,2.94) | 2.65 (1.90,3.70) | <.001 |
| Repeated PPA IPRW | 25.1 (21.6,29.2) | 11.4 (9.0,14.4) | 13.7 (9.0,18.4) | 2.21 (1.67,2.93) | 2.61 (1.87,3.65) | <.001 |
| Repeated PPA missing=vaping | 17.3 (14.7,20.1) | 8.2 (6.4,10.4) | 9.1 (5.7,12.4) | 2.10 (1.58,2.80) | 2.34 (1.69,3.22) | <.001 |

Definitions: PPA=point-prevalence abstinence; CCA=complete-case analysis; IPRW=inverse probability of retention weighting.

**eTable 5 relationship key (SUP-N16/SUP-S12):** [D003 p. 14](<../../joi240078supp2_prod_1739900423.24574.pdf#page=14>) — 7-month 30-day and repeated PPA, intervention n=759 vs assessment-only control n=744, under CCA/IPRW/missing=vaping. Arithmetic anchors: 287/521=55.09%; 208/543=38.31%; 287/759=37.81%; 208/744=27.96%; 131/517=25.34%; 61/538=11.34%; 131/759=17.26%; 61/744=8.20% (rounded source displays).

### eTable 6 — moderators of intervention effect on 30-day PPA (D003 p. 15)

Beta is the treatment-by-moderator interaction log-odds coefficient as defined in eAppendix D. Overall multi-category tests have blank beta/SE values.

| Moderator / reference | Beta | SE | P-nom | P-adj |
|---|---:|---:|---:|---:|
| Age | .008 | .130 | .949 | 1.000 |
| Grade overall (ref 6th-8th) | — | — | .292 | 1.000 |
| Grade: 9th; 10th; 11th; 12th; >12th; ungraded/other/not student | -.185; .982; .820; .747; .647; -.358 | 1.149; 1.024; 1.006; 1.005; 1.277; 1.168 | .872; .337; .415; .458; .612; .759 | — |
| Gender overall (ref male) | — | — | .950 | 1.000 |
| Gender: female; non-binary/other | -.053; .067 | .232; .437 | .820; .878 | — |
| LGBQ+ (ref heterosexual) | -.148 | .229 | .519 | 1.000 |
| Racial minority (ref White) | .514 | .227 | .024 | .552 |
| Hispanic ethnicity (ref non-Hispanic) | .187 | .306 | .542 | 1.000 |
| Vaping >=21 days/month (ref <=20) | -.477 | .312 | .126 | 1.000 |
| Motivation; confidence to quit; health-consequence concern | .288; .169; .021 | .135; .104; .095 | .033; .103; .826 | .693; 1.000; 1.000 |
| Quit attempts overall (ref none) | — | — | .436 | 1.000 |
| Quit attempts: 1-2; 3-5; >=6 | -.337; .030; -.361 | .378; .366; .439 | .372; .935; .412 | — |
| Penn State index; Dependence Scale; e-FTCD; Hooked checklist | -.017; .034; -.036; -.032 | .027; .033; .050; .048 | .519; .298; .463; .500 | 1.000; 1.000; 1.000; 1.000 |
| Vape <30 min after waking | -.281 | .254 | .269 | 1.000 |
| Perceived addiction overall (ref very addicted) | — | — | .026 | .572 |
| Perceived addiction: somewhat; not at all; don't know | .465; .056; 1.653 | .713; .720; .896 | .515; .938; .065 | — |
| GAIN-SS internalizing; substance problems; loneliness | -.313; -.027; -.061 | .121; .067; .035 | .010; .685; .080 | .250; 1.000; 1.000 |
| PEARLS overall (ref low risk) | — | — | .482 | 1.000 |
| PEARLS: intermediate; high | .176; .626 | .291; .572 | .544; .274 | — |
| Cigarettes; cigars/cigarillos; nicotine pouches; marijuana/cannabis in past 30 days | .346; -.024; -.362; -.012 | .237; .328; .348; .254 | .144; .942; .298; .962 | 1.000; 1.000; 1.000; 1.000 |

**eTable 6 relationship key (SUP-S13):** [D003 p. 15](<../../joi240078supp2_prod_1739900423.24574.pdf#page=15>) — treatment×baseline-moderator effects on 7-month 30-day PPA, assessment-only control reference; all nominal and Holm-adjusted P values as displayed.

## Cross-source matching index for later reviewers

| Support result key | Exact support locations | Matched result identity to seek in main-paper evidence |
|---|---|---|
| Primary ITT/missing=vaping PPA | D002 pp. 5-6; D003 pp. 4,11,14 | 7-month, 30-day point-prevalence abstinence; intervention vs assessment-only control; intervention n=759/control n=744; 37.8% vs 28.0%; RR 1.35 (1.17-1.57), OR 1.57 (1.26-1.95), RD 9.9 (5.1-14.5). |
| Complete-case and IPRW PPA | D003 pp. 5,14 | 7-month responder analysis: 30-day and repeated PPA, denominators 521/543 and 517/538 respectively; distinguish CCA from IPRW. |
| MI sensitivity | D003 pp. 4,11 | OR.miss grid, P1/P0, difference, RR, OR, FMI, and stated MAR/NMAR meanings. |
| Retention/missingness | D002 pp. 4-7; D003 pp. 5,12-13 | 7-month response rates (68.6% intervention, 73.0% control) and responder/nonresponder population definition. |
| Moderator analysis | D002 pp. 5-6; D003 pp. 6,15 | 30-day PPA treatment×moderator logistic interaction; assessment-only reference; nominal vs Holm-adjusted P label. |
| Baseline dependence/psychosocial measures | D002 pp. 5,15; D003 pp. 7-10,12-13 | Table-1 baseline measure labels, scale ranges, item-specific denominators, and PEARLS post-launch timing. |

## Explicit no-applicable-unit record

The following assigned units were inspected and contain no result-relevant support relationship beyond the administrative/reference context stated above: D002 pp. 1, 8-14; D003 pp. 1 and 16. D002 pp. 9-10 contain protocol safety/DSMB numerical administration details, recorded above, but no trial result. No workbook, CSV, DOC/DOCX, formula-cached value, figure-panel value, or OCR-dependent unit is in this assigned support scope.
