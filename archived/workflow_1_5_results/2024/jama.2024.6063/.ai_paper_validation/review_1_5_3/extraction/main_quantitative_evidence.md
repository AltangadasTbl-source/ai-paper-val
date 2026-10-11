# Main-paper quantitative evidence map

## Scope and method

- **Direct source:** `jama_laslett_2024_oi_240048_1727199125.7595.pdf` (`DOC-JAMA2024-6063-MAIN-2f574565`), PDF pages 1-10.
- **Assigned unit partition:** reusable native/layout text for PDF pp. 1-9; fresh direct extraction for PDF p. 10.
- **Reusable locators used:** `.ai_paper_validation/preprocessing/DOC-JAMA2024-6063-MAIN-2f574565/normalized_text/page-001.txt` through `page-009.txt`; the reusable page-006 rendered image was also visually read to preserve the Table 2 column headings, values, and footnotes.
- **Fresh p. 10 derivatives:** `preprocessing/main_p010_native.txt` and `preprocessing/main_p010_layout.txt`, both produced from the direct supplied PDF with `pdftotext` on 2026-08-18.
- **Source-location convention:** each page citation below means the direct supplied PDF page, for example `jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6`.
- **Mapping boundary:** this is a complete evidence inventory, not a candidate assessment, diagnosis, or adjudication.

## Page coverage

| PDF page | Evidence content and mapping status |
|---|---|
| 1 | Abstract: population, allocation, primary result, completion, and adverse-event counts mapped. |
| 2 | Key Points, eligibility, recruitment period, randomization, intervention composition mapped; no additional analyzed outcome estimates. |
| 3 | Figure 1 flow; outcome definitions, scales, thresholds, and time points mapped. |
| 4 | Outcome measurement details, reliability estimate, power calculation, analysis population, and model specification mapped. |
| 5 | Table 1 baseline population, counts, percentages, means/SDs, medians/IQRs, units, and scale footnotes mapped. |
| 6 | Table 2 primary, secondary, laboratory, and post hoc results mapped; all displayed confidence intervals and P values retained. |
| 7 | Figure 2 definition; analysis narrative, follow-up counts, adherence, Omega-3 Index time course, and narrative primary/secondary/adverse-event results mapped. |
| 8 | Table 3 adverse-event counts and participant percentages, definitions, and quantitative discussion comparisons mapped. |
| 9 | Conclusions and quantitative discussion/limitations statements mapped; no new table or inferential estimate. |
| 10 | Fresh direct native/layout extraction completed. Reference list only; **no applicable main-study result-relevant numeric/statistical relationship**. |

## Numeric/reporting relationships

### M-N001 — trial identity, population, allocation, and duration

- **Locations:** PDF pp. 1-3.
- Multicenter, randomized, double-blind, placebo-controlled trial in 5 Australian cities; recruited December 2016-June 2019; final follow-up February 7, 2020 (p. 1-2).
- Intervention: 2 g/d krill oil, `n = 130`, versus matching placebo, `n = 132`, for 24 weeks (p. 1). Randomization was 1:1, computer-generated adaptive allocation/minimization and stratified by study site (p. 2).
- Eligibility included age at least 40 years, VAS pain at least 40 on a 0-100 screening scale (100 worst pain), and MRI effusion-synovitis grade at least 1 on a 0-3 scale (3 severe) (p. 2).
- The intervention was two 1-g softgels daily; each krill softgel contained 190 mg/g EPA and 100 mg/g DHA, supplying total omega-3 350 mg/g and omega-6 12 mg/g (ratio 1:29). Placebo had no EPA/DHA and less than 5 mg/g (0.5%) other omega-3 (pp. 2-3).

### M-N002 — abstract population, completion, demographics, and primary result

- **Location:** PDF p. 1, Results.
- `262` randomized; mean age `61.6 (SD 9.6)` years; `53%` women; `222 (85%)` completed.
- VAS change: krill oil `−19.9` versus placebo `−20.2`; displayed between-group mean difference `−0.3`, `95% CI −6.9 to 6.4`, over 24 weeks.
- The primary VAS scale is 0-100, with 0 least pain; stated minimum clinically important improvement is 15.

### M-N003 — abstract adverse-event relationship

- **Location:** PDF p. 1, Results.
- One or more adverse events: krill oil `67/130 (51%)`; placebo `71/132 (54%)`.
- Musculoskeletal/connective-tissue disorders: `32` events with krill oil and `42` with placebo; component counts: knee pain `10` and `9`, lower-extremity pain `1` and `5`, hip pain `3` and `2`, respectively.

### M-N004 — Figure 1 participant flow and analysis population

- **Location:** PDF p. 3, Figure 1.
- `476` adults assessed; `214` excluded: severe knee OA `82`, insufficient effusion `36`, serious medical illness `11`, VAS score too low `10`, did not meet ACR criteria `6`, other inflammatory arthritis `6`, inability to conduct MRI `4`, opted for surgery `4`, medication contraindication `3`, significant knee injury `2`, arthroscopic/open surgery less than 12 months `2`, seafood allergy `1`, other reasons `32`, unknown reasons `15`.
- `262` randomized: krill oil `130`, placebo `132`; both initiated assigned treatment.
- Completion/discontinuation: krill oil `113` completed, `17` discontinued (adverse event `7`, lack of efficacy `4`, could not contact `6`); placebo `111` completed, `21` discontinued (adverse event `8`, lack of efficacy `6`, could not contact `6`, withdrew consent `1`).
- Knee-pain assessment at 24 weeks: krill oil `106`, placebo `109`; primary outcome analysis: `130` and `132`, respectively.

### M-N005 — outcome definitions, scales, time points, and responder rule

- **Locations:** PDF pp. 3-4.
- Primary outcome: change in 7-day self-reported knee-pain VAS from baseline to 24 weeks; scale 0-100 (0 no pain, 100 worst pain), MCII `15`.
- Secondary timing: MRI at screening and 24 weeks; questionnaires at weeks 4, 8, 16, and 20; study visits at weeks 0, 12, and 24. Blood samples at screening, 12, and 24 weeks; mean screening-to-week-0 gap `52` days (p. 3).
- Secondary measures: WOMAC pain (total, weight-bearing, non-weight-bearing) range 0-500 and function range 0-1700; 500/1700 indicate worst pain; MCII `12%` increase from baseline for each (p. 3). Effusion-synovitis volume change at 24 weeks (mL; MCII unknown); hand/back VAS changes at all time points; lower-limb strength at 12 and 24 weeks; AQoL-6D range `−0.04` to `1.0`, MCII `0.06`; analgesic use; and adverse events (pp. 3-4).
- OMERACT-OARSI response: either at least `50%` improvement with absolute change at least `20` points in VAS pain or WOMAC function, or at least `20%` improvement plus absolute change at least `10 mm` in at least 2 of pain, function, and global assessment, assessed at weeks 4, 8, 12, 16, 20, and 24 (p. 3).
- Laboratory MCII/MCID values: HDL `0.26 mmol/L`; LDL `0.10 mmol/L`; triglycerides `0.09`; high-sensitivity C-reactive protein `0.5 mg/dL` (p. 3).
- ICOAP response-item scale 0-4; rescaled total 0-44, constant 0-20, intermittent 0-24 to 0-100, with 100 worst pain. MCIIs: total `18.5`, constant `18.7`, intermittent `18.4` (p. 4).

### M-N006 — measurement reliability, power, and model/analysis labels

- **Location:** PDF p. 4.
- Effusion-synovitis intraclass correlation: `0.96`, `95% CI 0.94-0.97`, from `50` randomly selected participants; scale 0-1 and 1 indicates perfect agreement.
- Power calculation: `130` per group, `90%` power, detectable VAS difference `10` points (pain-change SD `23.8` points) and effusion-synovitis-volume change `4.5 mL`, at type-I error probability `5%` (`α = .05`).
- Analysis model: linear mixed model with treatment, month, treatment × month, and baseline outcome if Table 1 differences had `P ≤ .10`; analysis population was all randomized participants with at least one value for the relevant outcome. Individual participant and trial center were random intercepts and month a random slope; within-group changes and between-group changes were linear combinations of estimated coefficients.
- Missing-data statements: no values imputed; age was the only variable associated with primary-outcome missingness; age/missingness sensitivity analysis showed no meaningful/significant result difference (pp. 4 and 6 footnote a). Statistical software Stata 13.0 and R 4.0; two-sided `P < .05` statistically significant; secondary outcomes exploratory (p. 7).

### M-N007 — Table 1 baseline population values

- **Location:** PDF p. 5, Table 1. Columns are krill oil `n = 130` and placebo `n = 132`.
- Age mean (SD), y: `61.4 (9.9)`; `61.7 (9.3)`. Female: `64 (49%)`; `76 (58%)`. Male: `66 (51%)`; `56 (42%)`.
- BMI mean (SD): `29.3 (5.6)`; `29.9 (6.5)`; BMI at least 35: `16 (13%)`; `25 (20%)`.
- Knee-pain VAS mean (SD): `47.8 (20.3)`; `50.2 (20.4)`. Effusion-synovitis volume median (IQR), mL: `4.3 (2.5-9.2)`; `5.2 (2.8-11.0)`.
- Whole-Organ MRI score: score 1, `42 (33%)` and `38 (29%)`; score 2, `29 (23%)` and `25 (19%)`; score 3, `57 (45%)` and `66 (51%)`.
- WOMAC mean (SD): pain `186.3 (98.2)` and `209.6 (99.6)`; function `575.7 (312.4)` and `617.9 (333.2)`.
- Hand-pain VAS `21.7 (26.3)` and `24.4 (28.5)`; back-pain VAS `26.7 (25.9)` and `33.0 (30.5)`; lower-limb strength, N, `66.5 (38.1)` and `65.8 (37.1)`; AQoL-6D `0.77 (0.15)` and `0.75 (0.17)`.
- ICOAP mean (SD): intermittent `39.9 (18.4)` and `40.4 (20.2)`; constant `27.7 (20.3)` and `32.7 (22.1)`; total `34.3 (17.2)` and `36.7 (19.3)`. Pressure-pain threshold median (IQR), kPa/s: `4.2 (3.1-6.1)` and `4.3 (3.0-6.2)`; testing was only at Melbourne and Perth (krill `n = 43`; placebo `n = 40`).
- Medication use, No. (%): acetaminophen `38 (30%)` and `35 (27%)`; NSAIDs `25 (20%)` and `40 (31%)`; glucosamine `11 (9%)` and `19 (15%)`; turmeric `5 (4%)` and `8 (6%)`.
- Laboratory measures: hsCRP median (IQR), mg/dL, `1.4 (0.7-2.9)` and `1.9 (1.0-3.8)`; triglycerides mean (SD), mmol/L, `1.4 (1.1)` and `1.3 (0.7)`; HDL `1.6 (0.4)` and `1.5 (0.4)`; LDL `3.0 (0.9)` and `3.2 (0.9)`; fasting glucose `5.3 (0.7)` and `5.3 (1.0)`; Omega-3 Index, %, `6.5 (1.6)` and `6.5 (1.5)`.
- Sites, No. (%): Hobart `64 (49.2%)` and `61 (46.2%)`; Melbourne `27 (20.8%)` and `27 (20.5%)`; Adelaide `11 (8.5%)` and `19 (14.4%)`; Sydney `6 (4.6%)` and `4 (3.0%)`; Perth `22 (16.9%)` and `21 (15.9%)`.
- Table 1 scale/unit notes: VAS range 0-100 (0 no pain to 100 unbearable); MRI score 0-3; WOMAC pain 0-500 and function 0-1700; AQoL-6D 1.00 full health, 0.00 death-equivalent, −0.04 worse than death; ICOAP 0-100 (0 no pain to 100 unbearable); Omega-3 Index is EPA + DHA as percentage of total RBC-membrane fatty acids. BMI is kg/m².

### M-N008 — follow-up, adherence, and Omega-3 Index time course

- **Location:** PDF p. 7, Results and Process Measures.
- Screened `476`; enrolled/randomized `262`; withdrawals/losses `40 (15%)`: krill `17 (13.1%)`, placebo `23 (17.4%)`; completed `222 (84.7%)`.
- Followed-up counts: week 4 `241`; week 8 `235`; week 12 `230`; week 16 `226`; week 20 `224`; week 24 `222`. Mean age `61.6` years (range `40-88`); women `53%`.
- Mean adherence among those returning softgels: placebo `96%`, krill `99%`; `95%` consumed at least `80%` of softgels over 24 weeks.
- Mean Omega-3 Index: krill oil `6.5%` baseline, `7.8%` week 12, `8.0%` week 24; placebo `6.5%`, `6.5%`, `6.6%`, respectively.

### M-N009 — Figure 2 plot definition

- **Location:** PDF p. 7, Figure 2 caption.
- Figure 2 displays knee-pain VAS scores at baseline and 24 weeks, ordered by baseline VAS ascending for krill oil and descending for placebo. X marks baseline values without 24-week follow-up. The right-panel outcome is participant change (`24 wk − baseline`) excluding missing follow-up; box limits are first/third quartiles, solid line median, dashed line mean, and whiskers within `1.5 × IQR`.

### M-N010 — adverse-event relationship in Table 3 and narrative

- **Locations:** PDF pp. 7-8, Results/Table 3.
- `203` adverse events: krill oil `97` events among `67` participants; placebo `106` among `71` participants. One or more adverse events: `67/130 (51%; Table 3 50.7%)` and `71/132 (54%; Table 3 53.8%)`.
- Table 3 event counts, krill/placebo: total `97/106`; musculoskeletal/connective tissue `32/42` (knee pain `10/9`, extremity pain `1/6`, hip pain `3/2`); respiratory/thoracic/mediastinal `9/16` (upper respiratory infection `4/4`, nasopharyngitis `2/1`, cough `2/0`, lower respiratory infection `1/1`); gastrointestinal discomfort/disorders `13/6` (gastroesophageal reflux `1/3`, abdominal discomfort `0/3`, diarrhea `2/1`); investigations `10/8`; surgical/medical procedures `5/8`; injury/poisoning/procedural complications `11/6`; skin/subcutaneous tissue `5/3`; general system disorders `3/2`; nervous system disorders `2/3`.
- Participants with an adverse event: `67 (50.7%)` and `71 (53.8%)`; total serious adverse events `9/6`; treatment-related serious adverse events `0/0`. Specific event categories are limited to events in at least 3 participants. Serious-event definition is death; life-threatening, disabling, nonelective/prolonged hospitalization; or important events such as new cancer diagnosis.
- Narrative additional values: musculoskeletal events `32 (25%)` versus `42 (32%)`; gastrointestinal events `13 (10%)` versus `6 (4.5%)`; all `9` krill and `6` placebo serious events considered unrelated to treatment.

### M-N011 — quantitative comparative discussion and conclusion statements

- **Locations:** PDF pp. 8-9.
- Current-study exposure stated as 2 g/d krill oil containing `380 mg` EPA and `200 mg` DHA; Omega-3 Index `8.0%`. The cited comparator trial is described as 4 g/d, `880 mg/d` EPA+DHA (`600 mg` EPA and `280 mg` DHA), Omega-3 Index `9.0%`; baseline Omega-3 Index comparison `6.5%` versus `5.7%`; cited dietary limit less than `500 mg/d` omega-3 long-chain PUFA.
- Other quantitative discussion statements: two previous 30-day placebo-controlled RCTs; one described `300 mg/d` in `90` people with C-reactive protein greater than `1.0 mg/dL`; another 2 g/d in `50` people; a third 4 g/d trial in `235` adults over 26 weeks. These are cited external-study contextual claims, not analyzed KARAOKE estimates.
- Main-study conclusion: 2 g/d daily krill-oil supplementation did not improve knee pain over 24 weeks compared with placebo in people with knee OA, significant knee pain, and MRI effusion-synovitis (p. 9).

### M-N012 — fresh p. 10 no-applicable-unit record

- **Location:** PDF p. 10; direct native and layout derivatives named above.
- The page contains references 10-35 and publication footer only. It reports no KARAOKE result count, total, numerator, denominator, percentage, rate, person-time quantity, outcome value, effect estimate, interval, P value, test statistic, standard error, population/time/contrast/model result, table/figure label, or result footnote. **No applicable main-study quantitative relationship.**

## Inferential/statistical relationships from Table 2

**Common Table 2 context:** PDF p. 6, Table 2. Columns are krill oil mean (95% CI), `n = 130`, and placebo mean (95% CI), `n = 132`, at baseline, 24 weeks, and change; then between-group difference in change, mean (95% CI), and P value. Results are adjusted for baseline where Table 1 `P ≤ .10` (hsCRP, back pain, WOMAC total pain, WOMAC weight-bearing pain). No imputation. The primary analysis sensitivity analysis adjusted for age/missingness. Table footnotes define VAS 0-100 (unbearable pain at 100) and effusion-synovitis 0 mL to infinity (higher = more).

| Local statistical relationship | Outcome, population/time/contrast/model label | Krill oil baseline; 24 wk; change | Placebo baseline; 24 wk; change | Displayed between-group result |
|---|---|---|---|---|
| M-S001 | Primary: knee pain VAS, baseline to 24 wk | `47.8 (44.3-51.3)`; `26.5 (22.0-31.1)`; `−19.9 (−24.7 to −15.2)` | `50.2 (46.7-53.7)`; `29.3 (24.4-34.2)`; `−20.2 (−24.9 to −15.5)` | mean difference `−0.3 (−6.9 to 6.4)`; `P = .94` |
| M-S002 | Secondary: effusion-synovitis volume, median (IQR), mL, baseline to 24 wk | `4.3 (2.5-9.2)`; `5.4 (2.5-10.7) [n = 129]`; `0.81 (−0.17 to 1.79)` | `5.2 (2.8-11.0)`; `5.7 (3.1-9.7) [n = 128]`; `−0.94 (−1.92 to 0.04)` | mean difference `−1.75 (−3.13 to −0.37)`; `P = .01` |
| M-S003 | Secondary: WOMAC total pain | `186 (170-203)`; `110 (89-130) [n = 129]`; `−87 (−110 to −63)` | `210 (192-227)`; `130 (107-152) [n = 130]`; `−83 (−106 to −59)` | mean difference `3.0 (−24 to 31)`; `P = .81` |
| M-S004 | Secondary: WOMAC weight-bearing pain | `127 (116-138)`; `74 (61-87) [n = 106]`; `−51 (−61 to −42)` | `141 (130-151)`; `86 (72-101) [n = 111]`; `−48 (−58 to −39)` | mean difference `3 (−10 to 16)`; `P = .70` |
| M-S005 | Secondary: WOMAC non-weight-bearing pain | `60 (52-68)`; `36 (27-44) [n = 106]`; `−23 (−32 to −15)` | `69 (61-77)`; `43 (35-52) [n = 111]`; `−21 (−29 to −13)` | mean difference `2 (−10 to 14)`; `P = .70` |
| M-S006 | Secondary: WOMAC function | `578 (524-633)`; `319 (255-383) [n = 129]`; `−240 (−299 to −182)` | `618 (560-676)`; `419 (345-494) [n = 128]`; `−189 (−247 to −132)` | mean difference `51 (−31 to 133)`; `P = .22` |
| M-S007 | Secondary: hand-pain VAS | `21.7 (16.9-26.4)`; `14.4 (10.6-18.1) [n = 118]`; `−7.6 (−11.9 to −3.3)` | `24.4 (19.3-29.6)`; `17.6 (12.8-22.3) [n = 121]`; `−6.3 (−10.6 to −2.1)` | mean difference `1.3 (−4.8 to 7.3)`; `P = .69` |
| M-S008 | Secondary: back-pain VAS | `26.7 (22.0-31.4)`; `18.4 (14.2-22.7) [n = 120]`; `−7.6 (−12.2 to −3.0)` | `33.0 (27.5-38.5)`; `22.8 (18.0-27.5) [n = 121]`; `−8.9 (−13.5 to −4.4)` | mean difference `−1.3 (−7.9 to 5.2)`; `P = .69` |
| M-S009 | Secondary: lower-limb strength, N | `66.5 (59.8-73.2)`; `72.8 (65.7-79.8) [n = 126]`; `6.7 (2.6 to 10.7)` | `65.9 (59.4-72.3)`; `71.7 (64.3-79.1) [n = 130]`; `4.4 (0.5 to 8.4)` | mean difference `−2.2 (−7.9 to 3.4)`; `P = .44` |
| M-S010 | Secondary: AQoL-6D | `0.8 (0.7-0.8)`; `0.8 (0.8-0.9) [n = 125]`; `0.04 (0.02 to 0.06)` | `0.7 (0.7-0.8)`; `0.8 (0.8-0.8) [n = 129]`; `0.03 (0.01 to 0.05)` | mean difference `−0.01 (−0.04 to 0.01)`; `P = .38` |
| M-S011 | Secondary: OMERACT-OARSI response, No. (%) at final follow-up | `50 (47%) [n = 107]` | `45 (41%) [n = 110]` | displayed result `1.14 (0.84 to 1.55)` with superscript `f`; `P = .39` |
| M-S012 | Laboratory: hsCRP, median (IQR), mg/dL | `1.4 (0.7-2.9)`; `1.3 (0.8-2.3) [n = 104]`; `−0.76 (−1.60 to 0.08)` | `1.9 (1.0-3.8)`; `1.9 (1.1-3.3) [n = 103]`; `−0.12 (−0.97 to 0.73)` | mean difference `0.64 (−0.56 to 1.84)`; `P = .30` |
| M-S013 | Laboratory: triglycerides, mmol/L | `1.4 (1.2-1.6)`; `1.3 (1.2-1.4) [n = 128]`; `−0.08 (−0.21 to 0.05)` | `1.3 (1.2-1.4)`; `1.4 (1.3-1.6) [n = 129]`; `0.07 (−0.06 to 0.20)` | mean difference `0.15 (−0.04 to 0.33)`; `P = .11` |
| M-S014 | Laboratory: HDL cholesterol, mmol/L | `1.6 (1.5-1.6)`; `1.6 (1.5-1.6) [n = 127]`; `0.02 (−0.03 to 0.06)` | `1.5 (1.5-1.6)`; `1.5 (1.4-1.6) [n = 127]`; `−0.01 (−0.06 to 0.03)` | mean difference `−0.03 (−0.09 to 0.03)`; `P = .32` |
| M-S015 | Laboratory: LDL cholesterol, mmol/L | `3.0 (2.9-3.2)`; `3.0 (2.8-3.2) [n = 126]`; `−0.01 (−0.12 to 0.10)` | `3.2 (3.0-3.3)`; `3.2 (3.0-3.4) [n = 127]`; `0.0005 (−0.11 to 0.11)` | mean difference `0.01 (−0.14 to 0.17)`; `P = .90` |
| M-S016 | Laboratory: fasting glucose, mmol/L | `5.3 (5.2-5.5)`; `5.4 (5.2-5.6) [n = 127]`; `0.07 (−0.12 to 0.26)` | `5.3 (5.1-5.5)`; `5.4 (5.2-5.6) [n = 125]`; `0.11 (−0.08 to 0.29)` | mean difference `0.04 (−0.23 to 0.30)`; `P = .79` |
| M-S017 | Post hoc: ICOAP constant pain | `27.7 (24.2-31.2)`; `16.6 (12.7-20.5)`; `−10.7 (−14.4 to −6.99)` | `32.7 (28.9-36.5)`; `23.0 (19.0-26.9)`; `−7.8 (−11.4 to −4.11)` | mean difference `2.95 (−2.29 to 8.18)`; `P = .27` |
| M-S018 | Post hoc: ICOAP intermittent pain | `39.9 (36.7-43.1)`; `29.2 (25.8-32.7)`; `−9.7 (−13.5 to −6.0)` | `40.4 (36.9-43.9)`; `31.6 (27.9-35.4) [n = 131]`; `−8.2 (−11.9 to −4.5)` | mean difference `1.5 (−3.8 to 6.9)`; `P = .62` |
| M-S019 | Post hoc: ICOAP total pain | `34.3 (31.3-37.3)`; `23.4 (20.0-26.8)`; `−9.9 (−13.3 to −6.57)` | `36.7 (33.4-40.1)`; `27.4 (23.8-31.1)`; `−8.2 (−11.9 to −4.5)` | mean difference `2.05 (−2.64 to 6.74)`; `P = .39` |

## Matching narrative occurrences for Table 2 relationships

- **M-S001:** abstract p. 1 reports `−19.9` versus `−20.2`, difference `−0.3`, 95% CI `−6.9 to 6.4`; Key Points p. 2 says mean difference `0.30`, 95% CI `−6.9 to 6.4`, `P = .94`; Results p. 7 reports `−19.9` versus `−20.2`, difference `−0.3`, same CI and `P = .94`; Figure 2 p. 7 depicts the same endpoint.
- **M-S002:** Results p. 7 reports `0.81 mL` versus `−0.94 mL`, between-group mean difference `−1.75 mL`, 95% CI `−3.13 to −0.37 mL`, `P = .01`.
- **M-S013 (12-week narrative endpoint distinct from Table 2’s 24-week endpoint):** Results p. 7 states krill oil `−0.11 mmol/L` versus placebo `0.14 mmol/L` over 12 weeks, displayed between-group mean difference `0.24 mmol/L`, 95% CI `0.07-0.42 mmol/L`, `P = .01`; it explicitly states this was not observed over 24 weeks.
- The Results narrative p. 7 states no significant between-group differences for other study outcomes and no changes in post hoc outcomes; it directs to Table 2 and Supplement 3 eTables 4-6.

## Relationship count and handoff

- **Numeric/reporting relationships:** 12 local relationships (`M-N001` through `M-N012`), including one explicit fresh no-applicable-unit record for p. 10.
- **Inferential/statistical relationships:** 19 local Table 2 relationships (`M-S001` through `M-S019`), plus the separately mapped reliability estimate in `M-N006`.
- **Total local relationships:** 31.
- **Coverage gap:** none within assigned main-paper pp. 1-10. The fresh-required p. 10 was directly extracted and mapped; it has no applicable main-study result relationship.
