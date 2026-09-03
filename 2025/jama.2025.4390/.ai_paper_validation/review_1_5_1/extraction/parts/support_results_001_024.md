# DOC-004 Support Quantitative Evidence Map: Pages 1-24

## Scope and direct-source method

- **Direct source:** `joi250019supp3_prod_1749674951.30054.pdf` (DOC-004), PDF pages 1-24 of 49.
- **Fresh extraction:** native and layout `pdftotext` across pp. 1-24, saved as `preprocessing/support_results_001_024/native_pp001_024.txt` and `preprocessing/support_results_001_024/layout_pp001_024.txt`.
- **Visual confirmation:** rendered direct-source pages 11, 12, 19, 23, and 24. Page 22 was also rendered to establish that it is a location-only clinic map. The displayed numbers below for figures came from the rendered current PDF; the unsuccessful OCR of page 11 was not used as evidence.
- **Boundary:** This map reconstructs support evidence only. It makes no candidate finding, assigns no C ID, and does not use legacy candidate/checker/report material.

## Result-relevant quantitative and statistical relationships

### R-D004-001 — event adjudication source, acceptance, and rejection counts

**Source locations:** DOC-004 pp. 10-12, Section 3 and Fig. 3-1 (p. 11) / continuation (p. 12).

**Definition and comparison key:** Fig. 3-1 divides *potential reported events* into accepted (blue) and rejected (orange), by reporting source. Reporting sources are not mutually exclusive; a single event can occur in more than one source category. Therefore source-category counts must not be summed to form the overall count. The printed `rejected/total (percent)` annotations reconcile to the stacked bar totals subject to displayed percentage rounding.

| Outcome | Reporting source | Rejected / total (%) | Accepted (derived total minus rejected) |
|---|---|---:|---:|
| Death | Administrative data | 0 / 165 | 165 |
| Death | Participant reported | 0 / 112 | 112 |
| Death | Overall | 0 / 175 | 175 |
| Acute coronary syndrome | Hospital diagnosis | 1 / 70 (1.4%) | 69 |
| Acute coronary syndrome | ED diagnosis | 21 / 71 (29.6%) | 50 |
| Acute coronary syndrome | Participant reported | 7 / 53 (13.2%) | 46 |
| Acute coronary syndrome | Overall | 28 / 115 (24.3%) | 87 |
| Heart failure | Hospital diagnosis | 1 / 41 (2.4%) | 40 |
| Heart failure | ED diagnosis | 5 / 61 (8.2%) | 56 |
| Heart failure | Participant reported | 16 / 42 (38.1%) | 26 |
| Heart failure | Overall | 22 / 95 (23.2%) | 73 |
| Stroke | Hospital diagnosis | 1 / 38 (2.6%) | 37 |
| Stroke | ED diagnosis | 6 / 42 (14.3%) | 36 |
| Stroke | Participant reported | 6 / 42 (14.3%) | 36 |
| Stroke | Overall | 12 / 71 (16.9%) | 59 |
| All-cause unplanned hospitalization/ED visit | Hospital diagnosis | 471 / 735 (64.1%) | 264 |
| All-cause unplanned hospitalization/ED visit | ED diagnosis | 183 / 1950 (9.4%) | 1767 |
| All-cause unplanned hospitalization/ED visit | Participant reported | 354 / 1220 (29.0%) | 866 |
| All-cause unplanned hospitalization/ED visit | Overall | 1008 / 3048 (33.1%) | 2040 |
| Hip fracture | Administrative data | 2 / 48 (4.2%) | 46 |
| Hip fracture | Participant reported | 0 / 36 | 36 |
| Hip fracture | Overall | 2 / 53 (3.8%) | 51 |
| Glaucoma | Administrative data | 67 / 111 (60.4%) | 44 |
| Glaucoma | Participant reported | 32 / 101 (31.7%) | 69 |
| Glaucoma | Overall | 79 / 161 (49.1%) | 82 |
| Non-vertebral fracture | Administrative data | 10 / 243 (4.1%) | 233 |
| Non-vertebral fracture | Participant reported | 62 / 301 (20.6%) | 239 |
| Non-vertebral fracture | Overall | 71 / 389 (18.3%) | 318 |

**Matching main-paper keys:** accepted event counts for death, ACS, heart failure, stroke, hip fracture, glaucoma, non-vertebral fracture, and unplanned hospital/ED visits; outcome definitions and adjudication population. The figure is a potential-event adjudication flow, not an allocation-group efficacy comparison, hazard ratio, or event rate.

### R-D004-002 — ABPM nested-sample timing, data-quality thresholds, and flow

**Source locations:** DOC-004 p. 18, Section 4; Fig. 4-1, p. 19.

**Population/time point:** consecutive volunteers in six Alberta communities; intended assessment at 6 months post-randomization, actually median 9.6 months (IQR 7.1-29.2). The ABPM sample is not all trial participants.

**Relationship:** 151 bedtime and 151 morning participants underwent/ultimately contributed ABPM analysis (302 total). Adequacy required at least 5 successful overnight and 8 successful daytime readings. Measurements were typically every 30 minutes by day and every 45 minutes overnight, with a typical declared sleep window of 11 PM-7 AM.

| Flow element | Morning | Bedtime | Total / relation |
|---|---:|---:|---:|
| Consecutive participants invited | 346 | 356 | 702 = 346 + 356 |
| Did not consent | 193 | 202 | 395 = 193 + 202 |
| Underwent ABPM | 153 | 154 | 307 = 153 + 154 |
| Inadequate reports forwarded to research team | 5 | 7 | 12 = 5 + 7 |
| Repeated ABPM, repeat adequate | 3 | 4 | 7 = 3 + 4 |
| Declined repeat | 2 | 3 | 5 = 2 + 3 |
| Analyzed | 151 | 151 | 302 = 151 + 151 |

The printed non-consent reason subtotals reconcile within each arm: morning 32 location/moved/transport + 15 previous negative experience/disrupts routine + 17 too busy + 11 not interested + 7 BP cuff fitting concerns + 4 current health problems + 4 COVID-19 concerns + 103 no reason = 193; bedtime 34 + 22 + 17 + 16 + 6 + 4 + 3 + 101 = 202. Page 18 also says seven bedtime and five morning reports were additionally judged inadequate; 3/7 bedtime and 2/5 morning declined repetition, requiring the same count of consecutively selected replacements. This agrees with Fig. 4-1's arm-specific flow.

**Matching main-paper keys:** 24-hour ABPM secondary analysis; bedtime versus morning allocation; sample `n=151` per allocation group; time since randomization; ambulatory BP measure/unit (mm Hg when reported elsewhere). No ABPM treatment-effect value, interval, or P value is printed on pp. 18-19.

### R-D004-003 — analysis definitions and statistical framework

**Source locations:** DOC-004 pp. 20-21, Section 5.

**Definitions/relationships to match against results:**

- Lost to follow-up: alternate-contact process begins after 10 unanswered phone/email attempts, 2 consecutive missed interviews (unreachable 5 weeks after scheduled interview), or disconnected/nonfunctional phone; clinic inquiry follows if alternate contacts are not reached within 1 week.
- Categorical variables: count and percent. Recorded-variable distributions: mean or median plus SD or IQR. These are descriptive-display definitions, not effect measures.
- Missing covariates: assumed missing at random; categorical values replaced by the modal observation and continuous values by the mean. **No outcome data were imputed.**
- Primary/secondary outcome model family: Cox proportional hazards models; reduced models where group sizes/event numbers were limited to avoid overfitting. Covariates entered in predefined presumed-importance order.
- Primary adjusted hazard-ratio covariate set: age, sex, Tilburg physical frailty score, current smoker, number of non-BP medications, EQ-5D-5L Overall Health Score, prior 6-month hospitalization, heart failure, diabetes, coronary artery disease, stroke/TIA, chronic kidney disease, dialysis, BMI >35 kg/m2, BMI <20 kg/m2, sleep apnea, exercise-day count, and province of residence.
- Allocation-group proportional-hazards assessment: Kolmogorov-type supremum test on summed martingale residuals over 1000 simulated patterns; text reports no allocation-group violation for all outcomes. This is a model-check description; it prints no outcome-specific statistic/P value.
- Secondary-outcome changes, made while blinded: 12-month Overall Health Score changed from change-from-baseline to on-treatment score; total cost expanded from acute-care costs; non-vertebral fracture added; syncope, falling, glaucoma diagnosis, nocturia frequency, and dementia-consistent impairment added as safety outcomes. The text says non-vertebral fracture was captured by administrative data throughout but participant ascertainment began mid-trial, causing less-sensitive early participant capture.

**Matching main-paper keys:** adjusted versus unadjusted hazard ratios, analysis populations, Cox model labels, covariate adjustment, confidence intervals/P values, 12-month Overall Health Score, total cost of care, and listed secondary/safety outcomes. No numerical effect estimate is printed here.

### R-D004-004 — baseline antihypertensive medication counts by allocation

**Source locations:** DOC-004 pp. 23-24, eFigure 2. **Groups:** morning, bedtime. Values are medication-use counts, not mutually exclusive participant totals: a participant may use multiple medications, so summing bars is not a randomized-group denominator or participant count.

| Class | Medication: morning / bedtime counts |
|---|---|
| ACE inhibitor | ramipril 314/271; perindopril 205/207; lisinopril 35/34; trandolapril 27/26; enalapril 21/21; fosinopril 15/10; cilazapril 8/3; quinapril 6/13 |
| ARB | candesartan 144/171; irbesartan 99/89; telmisartan 79/97; valsartan 70/87; losartan 46/60; olmesartan 30/32; eprosartan 2/0; azilsartan 1/0 |
| Calcium-channel blocker | amlodipine 347/336; nifedipine (XL/XR) 51/59; diltiazem 33/26; diltiazem CD 17/10; diltiazem XC 17/12; felodipine 15/7; felodipine ER 4/4; verapamil 4/6; verapamil SR 4/3; amlodipine and atorvastatin 0/3; nifedipine 0/2 |
| Diuretic | HCTZ 297/292; furosemide 53/44; chlorthalidone 40/30; indapamide 36/43; spironolactone 34/34; HCTZ-triamterene 21/14; amiloride + HCTZ 3/3; amiloride 2/3; ethacrynic acid 1/0; HCTZ-spironolactone 0/3 |
| Beta blocker | metoprolol 111/111; bisoprolol 97/96; atenolol 29/41; propranolol 12/16; carvedilol 8/10; labetalol 5/1; sotalol 5/2; acebutolol 3/5; propranolol LA 3/2; nadolol 2/3; metoprolol SR 1/0; nebivolol 1/3; pindolol 1/0 |
| Other antihypertensive | clonidine 9/10; hydralazine 4/4; terazosin 3/7; doxazosin 2/3; aliskiren 1/2; isosorbide mononitrate 1/0; prazosin 1/2 |
| Combination antihypertensive | perindopril/indapamide 68/78; valsartan HCTZ 53/47; telmisartan & HCTZ 34/21; irbesartan HCTZ 32/35; candesartan & HCTZ 21/31; ramipril HCTZ 20/30; losartan HCTZ 18/14; amlodipine eprosartan & HCTZ 14/10; lisinopril 12/8; amlodipine & telmisartan 10/14; lisinopril HCTZ 8/9; candesartan HCTZ DS 4/3; quinapril HCTZ 3/7; cilazapril/HCTZ 2/3; enalapril HCTZ 1/1; atenolol & chlorthalidone 0/3; pindolol & HCTZ 0/1 |

**Matching main-paper keys:** baseline medication use, allocation group, baseline sample denominator, and medication-class wording. The eFigure itself does not print percentages, P values, or a population denominator.

## Page-complete map, including no-applicable-evidence units

| PDF page | Direct-source content | Quantitative-evidence disposition |
|---:|---|---|
| 1 | Supplement contents | No result values; identifies eAppendix/eFigures/eTables. |
| 2 | Staff and start of participating-clinic list | Recruitment-site `provider` and `rand` counts begin; administrative/recruitment context only, no analyzed outcome or statistical result. |
| 3 | Participating-clinic list | Same: clinic-level provider/randomization counts, not a treatment/outcome result. |
| 4 | Participating-clinic list | Same: clinic-level provider/randomization counts, not a treatment/outcome result. |
| 5 | Participating-clinic list ends | Same: clinic-level provider/randomization counts, not a treatment/outcome result. |
| 6 | Administrative outcome-code definitions | Definitions only; R-D004-001 outcome-name/ascertainment match support. |
| 7 | Hip-fracture code/qualification definitions | Definitions only; no result value. |
| 8 | Glaucoma and dementia code/qualification definitions | Definitions only; no result value. |
| 9 | Non-vertebral fracture/nursing-home/last-service-date definitions | Definitions only, including provincial data coverage dates; no result value. |
| 10 | Adjudication process narrative | Defines the potential-outcome and acceptance/rejection framework for R-D004-001; no new tabulated result. |
| 11 | Fig. 3-1, first panels | R-D004-001 (death, ACS, HF, stroke). |
| 12 | Fig. 3-1, continuation panels | R-D004-001 (unplanned hospital/ED, hip fracture, glaucoma, non-vertebral fracture). |
| 13 | General adjudication rules | Definitions/rules; no outcome-result number. |
| 14 | ACS/HF and stroke adjudication rules | Definitions/rules, including the >24-hour stroke criterion; no outcome-result number. |
| 15 | Stroke/unplanned hospital-ED/hip-fracture rules | Definitions/rules; contains two isolated excluded-event examples, not allocation comparison results. |
| 16 | Hip fracture/death/glaucoma/nursing home/fracture rules | Definitions/rules; no outcome-result number. |
| 17 | Non-vertebral-fracture rules | Definitions only; no result value. |
| 18 | ABPM methods/sample/timing | R-D004-002. |
| 19 | ABPM flow diagram | R-D004-002. |
| 20 | Follow-up definition, covariates, descriptive/model methods | R-D004-003. |
| 21 | Model-assumption statement and outcome changes | R-D004-003. |
| 22 | eFigure 1 clinic-location map | No displayed numeric or statistical result. |
| 23 | eFigure 2 baseline medication panels | R-D004-004. |
| 24 | eFigure 2 continuation | R-D004-004. |

## Extraction limitations

- Pages 11, 12, 19, 22, 23, and 24 are figure-heavy. The native PDF text did not carry the plotted values; values were transcribed from rendered current-source pages. Tesseract did not yield usable page-11 graphic text, so it was not relied on.
- The support PDF provides no workbook formulas/cached values, CSV, DOC/DOCX, or standalone statistical-output table within this assigned scope.
- No direct source gap remains for DOC-004 pp. 1-24. Exact comparison with main-paper values is reserved for the cross-source/checking stages.
