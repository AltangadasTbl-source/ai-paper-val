# Support Quantitative Evidence Map — DOC-002 PDF pp. 31–60

## Scope, method, and coverage

- **Direct source:** `joi250084supp1_prod_1765403089.61351.pdf`, PDF pp. 31–60 (30 pages), fresh-required scope only.
- **Fresh extraction retained:** `preprocessing/DOC-002/p031-p060/native.txt` and `layout.txt`; both were produced with `pdftotext` but are glyph-encoded and unsuitable for transcription. Rendered direct-source pages are retained in `preprocessing/DOC-002/p031-p060/` and were used for the readable material below. CPU OCR was attempted only as a confirmation aid; it was not relied on where incomplete/unreadable.
- **Nature of this scope:** protocol/SAP material. Values below are planned assumptions, definitions, thresholds, or analysis rules, not trial results. No candidate diagnosis or adjudication was performed.
- **Main-paper matching keys:** dDPP (fully automated digital Diabetes Prevention Program), hDPP (standard/human Diabetes Prevention Program), CDC type-2-diabetes risk-reduction benchmark, A1C, weight, physical activity (PA), ITT, and program completer/per-protocol population.

## Numeric/reporting relationships

### D2B-N001 — Glycemic rescue and withdrawal definitions

- **Location:** DOC-002 PDF p. 31, sections 6.6–7.4.
- **Population/time/definition:** a participant with A1C **>=6.5%** during the trial triggers a letter to the primary-care physician; loss to follow-up is failure to return for the **12-month** study visit plus inability to contact site staff. The site attempts rescheduling within **30 days**; before loss-to-follow-up determination it attempts, where possible, **3 telephone calls** and then a certified letter. Study-end criterion includes completion of the **12-month** visit (and, for hDPP only, 12 months from first hDPP visit).
- **Use for matching:** planned thresholds/time windows; not a reported efficacy result.

### D2B-N002 — Planned CONSORT enrollment and allocation totals

- **Location:** DOC-002 PDF p. 32, section 8.1 CONSORT diagram.
- **Printed values:** assessed for eligibility **n≈460**; randomized **n=368**; allocated dDPP **n=184** and hDPP **n=184**. Exclusion, receipt, loss-to-follow-up, discontinuation, and analyzed cells are blank templates.
- **Rule/contrast:** two-arm allocation, dDPP versus hDPP; 184 + 184 = 368. Eligibility n≈460 is an approximate planned screening count, not a denominator for a completed flow result.

### D2B-N003 — Physical measurements, laboratory failure, activity completeness, and PA recording

- **Location:** DOC-002 PDF pp. 32–33, section 8.2.
- **Printed definitions/units:** height to nearest **0.1 cm**; weight to nearest **0.1 kg**. A1CNow+ result is obtained in **5 minutes**. A1CNow+ failure is **two** quality-control/error messages during a visit, excluding messages **<4.0** or **>13.0**; failure requires serum hemoglobin A1C for that visit. ActiGraph is worn for **7 consecutive days** at enrollment and approximately every **1 month**, returned at **12 months**; a period with actual wear time **<75%** is repeated and prior incomplete/invalid data disregarded. Self-reported PA records number of minutes of moderate/brisk PA in the preceding week; reported no activity is recorded as **0 minutes**.
- **Population/time/scale:** participant-level protocol procedures; PA is minutes/week, and wear-time validity is percentage of the 7-day period.

### D2B-N004 — AE reporting windows and escalation threshold

- **Location:** DOC-002 PDF pp. 35–36, sections 8.4.4–8.4.6.
- **Printed definitions:** reportable events from consent through **7 days** after last participation for nonserious AEs (grades 1–2) and **30 days** for serious AEs (grades 3–5). Coordinators notify the PI within **1–2 business days** for an AE and immediately by phone for serious events; a serious event is reported to the IRB within **24 hours**. Death/immediately life-threatening SAE: sponsor/reviewing IRB within **3 working days**, lead PI within **24 hours**; other SAE: no later than **10 working days** after awareness. FDA notification of an unanticipated adverse-device effect: no later than **10 calendar days** after awareness. DSMB/IRB/NIH notification is triggered when **five grade-3 AEs** are judged probably related.
- **Use for matching:** protocol safety definitions/timing, not observed event rates.

### D2B-N005 — Noninferiority hypothesis and margin

- **Location:** DOC-002 PDF pp. 36–37, section 9.1.
- **Outcome/contrast:** binary composite primary endpoint: CDC benchmark attainment for type-2-diabetes risk reduction; dDPP experimental arm versus hDPP standard arm. Assumed success is **50%** in each arm; equivalence/noninferiority limit **d=15 percentage points**.
- **Printed hypotheses:** H0: πs >= πe + 15; Ha: πs − 15 < πe (where πs is hDPP and πe dDPP). This encodes noninferiority of dDPP against hDPP within 15 percentage points.
- **Supporting quantities:** landmark DPP risk difference for 5% weight-loss attainment at 12 months **46.7% (95% CI, 43.1%–50.2%)**; the protocol describes its margin as approximately **32%** of that effect and below a **50%** FDA-suggested threshold. In subset hDPP programs, **N=5**, completer proportions were **50% (range 47%–60%)** for 5% weight loss and **50% (range 29%–80%)** for the combined 4% weight-loss/150-minutes-PA outcome; the ITT trial expectation is πs closer to **30%–40%**.

### D2B-N006 — Sample-size derivation and retained analysis population

- **Location:** DOC-002 PDF p. 37, section 9.2.
- **Inputs/outputs:** 1:1 randomization; alpha **5%**; power **80%**; assumed success **50%** per arm; **138** enrollees per arm, total **n=276**, before attrition. With assumed **25%** attrition at **12 months**, adjusted enrollment is **184 per group (368 total)** to retain **276** analyzable participants. The target is **80%** probability that the upper one-sided 95% CI excludes an hDPP-favoring difference greater than **15%**.
- **Arithmetic linkage:** 276 / (1 − 0.25) = 368; 138 / 0.75 = 184 per arm. This matches the p. 32 planned CONSORT allocation.

### D2B-N007 — Analysis populations, tests, and models

- **Location:** DOC-002 PDF pp. 37–38, sections 9.3–9.4.1 and 9.4.7–9.4.8.
- **Population rule:** ITT includes all participants by initial randomization regardless of adherence/protocol deviations; effectiveness analysis excludes study/consent withdrawals. Per-protocol analysis uses completers as defined in section 3.3. Primary effectiveness analyses are unadjusted, two-sided significance tests; pooled two-site data are analyzed with site-clustering accounted for.
- **Definitions/models:** continuous baseline measures: mean/median/frequency counts; categorical measures: proportions/frequency counts. Baseline tests: unpaired t test or Wilcoxon signed-rank for continuous measures and chi-square or Fisher exact for categorical measures. Primary and binary secondary outcomes: mixed-effects logistic regression; continuous secondary outcomes: linear regression; interaction terms test effect modification. Primary endpoint uses ITT logistic regression with CDC benchmark attainment dependent variable and treatment primary exposure.
- **Secondary endpoints/scales:** binary benchmark components at **6- and 12-month** points use logistic regression; A1C change, absolute and percentage weight change use linear regression; PA includes average minutes/week by intensity, MET-hours/week, and steps/day. Likert-item responses use Spearman correlation or chi-square; aggregate Likert scores use Pearson correlation or t test.

### D2B-N008 — Missing data, sensitivity, covariates, and site/within-arm analyses

- **Location:** DOC-002 PDF p. 38 and p. 39 opening text, sections 9.4.2–9.4.6 and continuation.
- **Missingness rule:** if more than **5%** of a PA outcome is missing, primary analysis uses multiple imputation; sensitivity analysis is complete case with **100% valid PA data**. A1C and weight are expected to have low missingness; PA measurement occurs at **1-month intervals**.
- **Other planned analyses:** sensitivity analyses account for JHH versus Reading site; covariate-adjusted logistic/linear models are supportive where baseline characteristics or time-varying exposures differ; within-arm exploratory analyses examine dDPP and hDPP success and a dDPP single-arm analysis. No numeric effect estimate is printed here.

### D2B-N009 — Cost-effectiveness model, horizons, discounting, and outcome scale

- **Location:** DOC-002 PDF p. 39, section 9.4.9.
- **Perspective/contrast/time:** dDPP versus hDPP cost-effectiveness from health-system perspective at **12-month** and lifetime horizons. Future costs/effects discounted at **3%**. Trial resource use collected at baseline, **6 months**, and **12 months**.
- **Model/measure:** Markov model health states include normal glucose tolerance, impaired fasting glucose, impaired glucose tolerance, type-2 diabetes, and death. Effect is QALYs; ICER compares interventions and is assessed against willingness-to-pay threshold. Both univariate and probabilistic sensitivity analyses vary transition, utility, and cost parameters, with an acceptability curve.

## Statistical relationship records

### D2B-S001 — Noninferiority endpoint, hypotheses, and sample-size compatibility

- **Source:** DOC-002 PDF pp. 36–37, sections 9.1–9.2; matched key `primary composite endpoint / dDPP versus hDPP`.
- **Relationship:** 15-percentage-point noninferiority margin; 50% assumed arm success; 1:1 randomization, alpha 5%, 80% power; n=138/arm (276) before 25% attrition and n=184/arm (368) after attrition. The source explicitly states a one-sided 95% CI exclusion criterion.
- **Check prerequisites noted:** exact sample-size formula, confidence-interval method, and sidedness convention beyond the printed description are not provided in this scope; later statistical review must not infer them.

### D2B-S002 — Planned outcome models and analysis populations

- **Source:** DOC-002 PDF pp. 37–39, sections 9.3–9.4.8.
- **Relationship:** ITT primary logistic model and binary secondary logistic models; linear models for continuous A1C/weight/PA outcomes; mixed effects to account for site clustering; per-protocol completer benchmark; unadjusted primary analyses plus supportive covariate-adjusted sensitivity models.
- **Check prerequisites noted:** this is an analysis plan without observed coefficients, intervals, test statistics, or P values.

### D2B-S003 — Missing-data decision rule

- **Source:** DOC-002 PDF pp. 38–39, section 9.4.2 and continuation.
- **Relationship:** PA missingness >5% triggers multiple imputation; complete-case sensitivity is limited to 100% valid PA data. This is a conditional statistical rule, not a reported missing-data result.

### D2B-S004 — Cost-effectiveness analysis specification

- **Source:** DOC-002 PDF p. 39, section 9.4.9.
- **Relationship:** 12-month/lifetime horizons, 3% discounting, Markov model, QALY effect scale, ICER and probabilistic sensitivity analysis. No observed ICER, cost, QALY, uncertainty interval, or P value appears on the mapped page.

## Explicit no-applicable / non-result-relevant page coverage

| PDF page(s) | Coverage result |
|---|---|
| 31 | Protocol discontinuation/withdrawal rules; numeric thresholds mapped in D2B-N001; otherwise no result table or effect estimate. |
| 32 | Planned CONSORT and measurement procedures; mapped in D2B-N002–N003. |
| 33 | Assessment procedures; mapped in D2B-N003; no observed outcome results. |
| 34 | AE/SAE classifications and narrative definitions; no result-relevant numeric relationship. |
| 35 | AE expectedness/reporting procedures; reporting windows/escalation threshold mapped in D2B-N004; no observed event count/rate. |
| 36 | Safety reporting and statistical-hypothesis opening; mapped in D2B-N004–N005. |
| 37 | Hypotheses, sample size, analysis populations/models; mapped in D2B-N005–N007. |
| 38 | Missing-data and outcome-analysis plan; mapped in D2B-N007–N008. |
| 39 | Cost-effectiveness plan and missing-data continuation; mapped in D2B-N008–N009. |
| 40–60 | Direct fresh-source page range covered. These are protocol/SAP continuation and administrative/support material; no additional completed trial result table, figure, observed numerator/denominator, effect estimate, interval, P value, or cross-document matched result was identified in this assigned range beyond the planned relationships recorded above. |

## Limitations

- Embedded native text for this source range is glyph-encoded. Direct rendered pages, rather than the unusable native/layout extraction, are the authority for the transcribed pp. 31–39 material.
- The later statistical reviewers should compare these protocol plan keys against reported main-paper/supplement results only after matching population, time point, outcome definition, analysis population, and model; plan-versus-result differences alone are not a candidate.
