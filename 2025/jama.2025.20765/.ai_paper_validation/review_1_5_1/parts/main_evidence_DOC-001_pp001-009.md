# Main Quantitative Evidence Map — DOC-001, PDF pp. 1-9

## Scope, method, and source authority

- **Direct source:** `jama_zahid_2025_oi_250093_1768590553.08463.pdf`, PDF pp. 1-9 (printed pp. 336-344).
- **Reusable locator:** `document_outputs/DOC-001/normalized_text/page-001.txt` through `page-009.txt`.
- **Direct confirmation:** page-selected native/layout extraction from the direct PDF at `review_1_5_1/preprocessing/main_mapper_direct/DOC-001_pp001-009_layout.txt`. The table on PDF p. 6 was additionally visually confirmed from a direct rendering at `review_1_5_1/preprocessing/main_mapper_direct/DOC-001-p006.png`; reusable rendered pages were used as visual locators for pp. 4-7.
- **Mapping convention:** `M-N` IDs are numeric/reporting relationships and `M-S` IDs are inferential-statistical relationships local to this shard. They are not global IDs and are not candidate IDs. “Diagnostic rule” names a later reproducible check only; it is not an adjudication or finding.

## Page coverage

| PDF page | Printed page | Content and coverage result |
|---:|---:|---|
| 1 | 336 | Abstract: population, allocation, primary and selected secondary outcome results mapped in M-N001-M-N002 and M-S003/M-S011. |
| 2 | 337 | Background/methods plus Key Points. The Key Points repeat population and primary proportions (M-N003). Other numeric background citations are not study-result claims. |
| 3 | 338 | Intervention schedule, outcome definitions, sample-size inputs, and statistical analysis plan mapped in M-N004-M-N005 and M-S001-M-S002. |
| 4 | 339 | Results narrative and Figure 1 participant flow. All displayed flow counts, primary-result narrative, secondary-result narrative, and adverse-event percentages mapped in M-N006 and M-N011-M-N014; inferential claims in M-S003-M-S004 and M-S013. |
| 5 | 340 | Table 1 baseline characteristics and repeated results narrative mapped in M-N007-M-N010 and M-N012-M-N014. |
| 6 | 341 | Table 2: every outcome row, denominators, percentages, intervals, crude/adjusted estimates, ICCs, and footnotes mapped in M-N015-M-N018 and M-S005-M-S012. |
| 7 | 342 | Figure 2, a graphical Bayesian cluster-probability display, mapped in M-N019 and M-S014. It supplies cluster IDs, group membership, cluster follow-up sizes, posterior means, observed proportions, and 95% credible-interval whiskers, but no printed per-cluster probability or interval values. |
| 8 | 343 | Discussion/limitations. Repeats the trial 4.8% 6-month mortality and observed ICC 0.19; mapped as repeated claims in M-N020. Other numbers concern cited external studies and are not trial-result relationships. |
| 9 | 344 | References only; no locally reported trial result, table, figure, or statistical relationship applicable to this mapping scope. |

## Numeric and reporting relationships

### M-N001 — Abstract trial population, allocation, retention, and primary outcome

- **Locations / repeated occurrence key:** PDF p. 1 Abstract Results; match key `DOC001|ITT-primary-abstinence|month-6|CO<10ppm|mHealth-vs-usual-care`.
- **Printed values:** 9232 assessed; 1080 randomized; mHealth `n = 720`, usual care `n = 360`; 985 retained throughout trial (91%). Primary verified continuous abstinence: mHealth `300/720 (41.7%)`; usual care `55/360 (15.3%)`; RR `3.0 (95% CI, 2.0-4.9)`.
- **Population/time/contrast/unit:** people with TB who smoked; 6 months; mHealth versus usual care; persons/proportion/percent.
- **Direct observation:** These are the printed abstract summary values.
- **Diagnostic rule for downstream check:** match to Figure 1, Table 2 ITT primary row, and Results narrative, allowing identical displayed precision.

### M-N002 — Abstract selected secondary outcomes

- **Locations / match keys:** PDF p. 1 Abstract Results; `adherence|month-6`, `TB-success|month-6`, `death|month-6`, `default|month-6`, `failure|month-6`.
- **Printed values:** adherence mean (SD), `174.3 (21.5)` days mHealth versus `178.0 (12.1)` usual care, `P = .23`; treatment success `89.3%` versus `85.6%`, RR `1.2 (95% CI, 0.9-1.6)`; treatment failure `0.1%` versus `0.5%`; default `3.1%` versus `1.9%`; mortality `3.5%` versus `7.5%`, HR `0.4 (95% CI, 0.2-0.9)`.
- **Direct observation:** Printed abstract outcome summary.
- **Diagnostic rule:** match values and effect-measure labels to PDF pp. 4 and 6; distinguish HR for death from RR rows.

### M-N003 — Key Points repetition of trial sample and primary proportions

- **Location / match key:** PDF p. 2 Key Points, `ITT-primary-abstinence|month-6|CO-supported`.
- **Printed values:** trial included `1080` patients with TB who smoked; self-reported continuous abstinence at 6 months supported by biochemical verification: `41.7%` mHealth versus `15.3%` usual care.
- **Direct observation:** The Key Points omit numerator/denominator and interval but repeat the principal comparison.
- **Diagnostic rule:** cross-location identity with M-N001/M-N011/M-N015 after matching outcome definition and precision.

### M-N004 — Intervention exposure and outcome-definition quantities

- **Locations:** PDF pp. 1 and 3.
- **Printed values:** mHealth `n=720`, text messages daily for `2 months` then monthly for `4 months`; `134` unique messages over `6 months`: `100` (3-4/day) in first month, `30` (1/day) in second month, and `4` (1/month) over next four months. Primary abstinence definition: no more than `5` cigarettes/bidis/water-pipe sessions since quit date, which was `5 days` after enrollment; CO `<10 ppm` at month 6; urine cotinine negative where baseline smokeless tobacco was concomitantly used. Point abstinence was prior `7 days`, assessed week `9` and month `6`; default was interruption for `>=2 months`.
- **Direct observation:** Printed intervention schedule and definitions needed to identify outcome scale/time/threshold.
- **Diagnostic rule:** ensure like-for-like matching of the `<10 ppm`, `<6 ppm`, ITT, PP, continuous, and last-7-day outcomes.

### M-N005 — Sample-size planning inputs

- **Location / match key:** PDF p. 3 Sample size paragraph, `sample-size-plan|cluster-RCT`.
- **Printed values:** `90%` power, `5%` two-sided significance, planned abstinence probabilities `18%` mHealth and `8%` usual care at 6 months, ICC `0.02`, cluster size `26`, design effect `1.5`, anticipated attrition `20%`, target `1080` participants and `27` clusters, capped at `40` participants/cluster.
- **Direct observation:** These are planned design quantities, not observed results.
- **Diagnostic rule:** later distinguish planned ICC/design effect from observed Table 2 ICCs.

### M-N006 — Participant flow and exclusions (Figure 1 plus results narrative)

- **Locations / match key:** PDF p. 4 Figure 1 and Participants text, `participant-flow|enrolment-randomization-month-6`.
- **Printed values:** `249` clusters / `9232` patients assessed; `222` clusters / `8152` patients excluded; exclusion items: `7069` not current smoker, `2783` not diagnosed pulmonary TB, `1820` not diagnosed within 4 weeks, `1290` no mobile-phone access, `385` age <15, `273` not willing to quit, `236` unable to read and no household reader, `6` refused; clinic items `182` new TB registrations <50/month and `40` not fit. The figure footnote says participants could be excluded for more than one reason. `27` clinics randomized: mHealth `18` clusters, `720` participants, cluster size `40`; usual care `9` clusters, `360` participants, cluster size `40`; both received allocated care and all `720`/`360` were included in primary analysis. Follow-up loss: mHealth `53` (`25` died, `18` no contact, `10` withdrew); usual care `42` (`27` died, `9` no contact, `6` withdrew); no clusters lost in either group.
- **Additional printed narrative:** six refused and `8146` did not meet inclusion criteria; `8.8%` did not provide primary outcome, described as `4.8%` died, `1.5%` withdrew, `2.5%` lost contact.
- **Direct observation:** Figure and adjacent text report the complete values above.
- **Diagnostic rules:** flow arithmetic within each allocated group (`720-53=667`, `360-42=318`); exclusions are explicitly non-exclusive, so individual reason counts are not intended to sum to excluded patients.

### M-N007 — Table 1 cluster-level baseline characteristics

- **Location / match key:** PDF p. 5 Table 1, `baseline|cluster-characteristics`.
- **Printed values (mHealth; usual care):** total clusters `18; 9`; cluster size `40; 40`; rural setting `11; 7`; average TB cases/month `142; 93`.
- **Direct observation:** Table 1 values, with no percentage label for the cluster rows.
- **Diagnostic rule:** group allocation totals should correspond to M-N001/M-N006 and participant totals below.

### M-N008 — Table 1 participant demographics and education

- **Location / match key:** PDF p. 5 Table 1, `baseline|participants-demographics-education`.
- **Printed values (mHealth; usual care):** total `720; 360`; age mean (SD) years `48.7 (15.8); 48.7 (15.9)`; male `698 (96.9%); 345 (95.8%)`; female `22 (3.1%); 15 (4.2%)`; BMI median (IQR) `18.7 (4); 18.6 (4)`.
- **Education, No. (%):** no formal education `315 (43.8); 155 (43.1)`; primary `175 (24.3); 114 (31.7)`; middle `109 (15.1); 43 (11.9)`; secondary `89 (12.4); 36 (10)`; higher `32 (4.4); 12 (3.3)`.
- **Direct observation:** Printed Table 1 values. BMI footnote defines kg divided by height in meters squared.
- **Diagnostic rule:** counts/percentages and mutually exclusive education categories can be mechanically checked against group denominators, subject to displayed rounding.

### M-N009 — Table 1 social/employment, reading, and clinical-severity characteristics

- **Location / match key:** PDF p. 5 Table 1, `baseline|social-employment-reading-TB-stage`.
- **Printed values (mHealth; usual care):** marital: single `83 (11.5); 37 (10.3)`, married `607 (84.3); 304 (84.4)`, separated/divorced `30 (4.2); 19 (5.3)`; employment: employed `560 (77.8); 275 (76.4)`, dependents `128 (17.8); 71 (19.7)`, retired `32 (4.4); 14 (3.9)`; able to read messages `425 (59.0); 225 (62.5)`; TB stage 1 `629 (87.4); 326 (90.6)`, stage 2 `45 (6.3); 20 (5.6)`, stage 3 `46 (6.4); 14 (3.9)`.
- **Definitions:** dependents = unemployed, homemakers, students, or otherwise not actively employed. Stage 1 mild-moderate, stage 2 severe, stage 3 very severe TB disease.
- **Direct observation:** Printed Table 1 values/footnotes.
- **Diagnostic rule:** check mutually exclusive category sums and denominator precision separately for each treatment group.

### M-N010 — Table 1 tobacco-related baseline characteristics

- **Location / match key:** PDF p. 5 Table 1, `baseline|tobacco-history`.
- **Printed values (mHealth; usual care):** smoking type: cigarettes `679 (94.3); 326 (90.6)`, hookah `61 (8.5); 35 (9.7)`, bidi `21 (2.9); 21 (5.8)`, concurrent smokeless use `50 (6.9); 8 (2.2)`. Tobacco use/day median (IQR): bidi `8 (10.0); 15 (14.0)`, cigarettes `5 (6.0); 7 (6.0)`, hookah `3 (4.0); 3 (2.0)`. Smoking allowed inside homes `482 (66.9); 189 (52.5)`; attempted quit in past `178 (24.7); 33 (9.2)`; mean smoking duration (SD), years `24.8 (15.1); 24.6 (15.2)`; median smoking start age (IQR), years `20 (9.0); 20 (8.0)`; low-addiction Heaviness of Smoking Index `514 (75.7); 212 (65.0)`.
- **Direct observation:** Printed Table 1 values. Smoking-type rows can overlap; the table does not label them as mutually exclusive.
- **Diagnostic rule:** compare repeated cigarette/smokeless use, daily medians, and prior quit percentages to p. 4 narrative; do not sum overlapping smoking types.

### M-N011 — Primary-outcome narrative occurrences

- **Location / match key:** PDF p. 4 Primary Outcome, `ITT-primary-abstinence|month-6|CO<10ppm`; repeated on PDF pp. 1-2.
- **Printed values:** self-report only: `47.5%` mHealth versus `19.4%` usual care. Biochemically verified ITT at CO `<10 ppm`: mHealth `41.7% (95% CI, 38.0%-45.4%)`; usual care `15.3% (95% CI, 11.7%-19.4%)`; RR `3.0 (95% CI, 2.0-4.9)`. Post-hoc adjusted RR `3.2 (95% CI, 2.2-5.2)` after age, sex, education, occupation, smoking duration. Among verified abstainers, CO mean (SD) ppm `3.54 (2.1)` mHealth and `4.38 (2.8)` usual care. Sensitivity CO `<6 ppm`: RR `3.7 (95% CI, 2.4-5.8)`.
- **Direct observation:** Narrative reports the listed values; Table 2 supplies the matching counts and additional intervals.
- **Diagnostic rule:** matching by CO threshold, ITT status, and adjustment status is required before cross-occurrence comparison.

### M-N012 — Secondary-outcome narrative occurrences

- **Location / match keys:** PDF pp. 4-5 Results, `point-abstinence|week-9/month-6`, `adherence|month-6`, `TB-success|month-6`, `failure/default/death|month-6`.
- **Printed values:** mean adherence: `174.3 (SD 21.5)` versus `178.0 (SD 12.1)` days, `P=.23`; treatment success `643/720 (89.3%)` versus `308/360 (85.6%)`, RR `1.2 (95% CI, 0.9-1.6)`; treatment failure `1/720 (0.1%)` versus `2/360 (0.5%)`; default `22/720 (3.1%)` versus `7/360 (1.9%)`; deaths `3.5%` versus `7.5%`, HR `0.4 (95% CI, 0.2-0.9)`; TB disease cause of death `32/52 (61.5%)`.
- **Direct observation:** These values are printed Results narrative; point-abstinence values are referenced to Table 2 rather than repeated numerically.
- **Diagnostic rule:** match counts/denominators to Table 2; distinguish total deaths `52` across groups from ITT denominators and Cox HR.

### M-N013 — Attrition, fidelity, and descriptive results

- **Location:** PDF p. 4 Participants section.
- **Printed values:** all mHealth participants confirmed message receipt. At month 6, `8.8%` lacked primary outcome; `4.8%` died, `1.5%` withdrew, `2.5%` lost contact. No outcome data were missing beyond these participants.
- **Direct observation:** Printed descriptive/operational claims.
- **Diagnostic rule:** compare the component percentages and group-level Figure 1 counts with the stated overall denominator and rounding conventions.

### M-N014 — Adverse-event percentages

- **Location / match key:** PDF p. 5 Adverse Events, `adverse-events|mHealth-vs-usual-care`.
- **Printed percentages (mHealth versus usual care):** nausea `23.0 vs 22.3`; diarrhea `7.5 vs 7.5`; dry mouth `62.7 vs 55.7`; epigastric pain `27.7 vs 40.4`; headache `45.1 vs 49.1`; insomnia `35.3 vs 33.5`; abnormal dreams `10 vs 13.2`; irritability `40.5 vs 43.4`; anxiety `33.3 vs 36.8`; palpitations `31 vs 28.4`; musculoskeletal pain `61.4 vs 60.8`. Narrative says dry mouth, irritability, and anxiety were more common in mHealth.
- **Direct observation:** The main paper gives percentages only and points to eTable 10 for further detail.
- **Diagnostic rule:** retain label, direction, and percent scale; no numerator/denominator is printed here.

### M-N015 — Table 2 primary outcome rows (all count/proportion/absolute-difference fields)

- **Location / match key:** PDF p. 6 Table 2, `Table2|primary-abstinence|threshold-analysis-population`.
- **Rows, printed mHealth; usual care; absolute difference (95% CI):**
  - CO `<10 ppm`, ITT: `300/720`, `41.7 (38.0-45.4)%`; `55/360`, `15.3 (11.7-19.4)%`; `26.4 (21.0-31.6)` percentage points.
  - CO `<10 ppm`, PP: `300/667`, `45 (41.2-48.8)%`; `55/318`, `17.3 (13.3-21.9)%`; `27.7 (22.1-33.3)`.
  - CO `<6 ppm`, ITT: `264/720`, `36.7 (33.1-40.3)%`; `38/360`, `10.6 (7.6-14.2)%`; `26.1 (21.2-30.7)`.
  - CO `<6 ppm`, PP: `264/667`, `39.6 (35.9-43.4)%`; `38/318`, `11.9 (8.6-16.1)%`; `27.7 (22.5-32.8)`.
  - Continuous abstinence self-reported only, ITT: `342/720`, `47.5 (43.8-51.2)%`; `70/360`, `19.4 (15.5-23.9)%`; `28.1 (22.6-33.5)`.
- **Direct observation:** Table 2 reports number of outcomes/total group total, as defined by footnote b. CO cutoffs are defined by footnote e.
- **Diagnostic rule:** denominators should align with Figure 1 allocated/lost counts for ITT and PP; primary outcome threshold/analysis labels must not be interchanged.

### M-N016 — Table 2 secondary outcome rows (all count/proportion/absolute-difference fields)

- **Location / match key:** PDF p. 6 Table 2, `Table2|secondary-outcomes|timepoint`.
- **Rows, printed mHealth; usual care; absolute difference (95% CI):**
  - point abstinence last 7 days, week 9 ITT: `353/720`, `49.0 (45.3-52.7)%`; `75/360`, `20.8 (16.7-25.4)%`; `28.2 (22.6-33.8)`.
  - point abstinence last 7 days, month 6 ITT: `400/720`, `55.6 (51.8-59.2)%`; `82/360`, `22.8 (18.5-27.5)%`; `32.8 (27.1-38.4)`.
  - TB treatment success (cured + completed): `643/720`, `89.3 (86.8-91.5)%`; `308/360`, `85.6 (81.5-89.0)%`; `3.8 (-0.5 to 8.2)`.
  - death: `25/720`, `3.5 (2.2-5.0)%`; `27/360`, `7.5 (5.0-10.7)%`; `4 (1.0-7.1)`.
  - treatment default (interruption >=2 months): `22/720`, `3.1 (1.9-4.6)%`; `7/360`, `1.9 (0.8-4.0)%`; `1.1 (-0.8 to 3.0)`.
  - TB treatment failure: `1/720`, `0.1 (0.01-0.8)%`; `2/360`, `0.5 (0.1-2.0)%`; `0.4 (-0.4 to 1.2)`.
- **Direct observation:** Table 2 values and labels.
- **Diagnostic rule:** counts/denominators/proportions, sign/direction of absolute differences, and rate-versus-count labels are separate checks. The table displays death's absolute difference as positive `4`, although mHealth's death percentage is lower; the table does not state an absolute-difference direction convention beyond its heading.

### M-N017 — Table 2 model/measure labels and applicability

- **Location:** PDF p. 6 Table 2 column headings and footnotes.
- **Printed definitions:** RR = relative risk; HR = hazard ratio; ICC = intraclass correlation coefficient; ITT = intention-to-treat; PP = per-protocol; NA = not applicable. Adjusted for age, sex, education, occupation, smoking duration; adjusted RR analyses account for clustering via mixed-effects models and adjusted HR uses shared-frailty Cox model. ICC is reported for RR models only. Death HR is Cox proportional-hazards frailty estimate. Mixed-effects models could not be estimated for default/failure owing to very low event numbers across clusters.
- **Direct observation:** Printed Table 2 labels/footnotes.
- **Diagnostic rule:** effect measure and NA/ICC applicability must be matched to the corresponding row and model.

### M-N018 — Visually confirmed printed adjusted self-report interval

- **Location / match key:** PDF p. 6 Table 2, continuous abstinence self-reported only (ITT), adjusted column; direct rendering confirmation.
- **Printed value:** adjusted RR `2.8 (1.9 to 42)`, ICC `0.19`.
- **Direct observation:** The native/layout text reads `42`; direct visual confirmation shows the endpoint printed as `42` (not `4.2`).
- **Diagnostic rule:** later evaluate interval/estimate compatibility and any matching occurrence using the direct-source printed value `42`; no normalization has been applied in this map.

### M-N019 — Figure 2 Bayesian cluster display

- **Location / match key:** PDF p. 7 Figure 2, `Bayesian-cluster-quit-probability|month-6`.
- **Printed structure:** panel A mHealth, cluster IDs `18` through `1`, follow-up cluster sizes `38, 39, 37, 39, 38, 39, 34, 36, 34, 40, 38, 36, 36, 39, 35, 33, 40, 36`; panel B usual care, cluster IDs `9` through `1`, sizes `35, 37, 36, 30, 38, 36, 33, 38, 35`. Both panels have probability percentage axis `0, 20, 40, 60, 80, 100`; posterior means and observed cluster proportions are plotted; whiskers indicate 95% credible intervals. Caption says posterior means include fixed + random effects.
- **Direct observation:** The chart has no printed numeric posterior mean, observed proportion, or CI endpoint for an individual cluster.
- **Diagnostic rule:** only graphical direction/label/cluster-size mapping is available locally; avoid transcribing unprinted plotted values as exact numbers.

### M-N020 — Discussion/limitations repetitions relevant to trial results

- **Location / match keys:** PDF p. 8 Discussion/Limitations, `death|month-6|trial-total` and `observed-ICC|primary-analysis`.
- **Printed values:** `4.8%` of trial participants died of TB within 6 months; observed ICC `0.19`, compared with sample-size assumed ICC `0.02`; participants almost entirely male (`>96%`); CO verifies recent `24-48` hour abstinence due to half-life `5-6` hours.
- **Direct observation:** Narrative claims/repetitions. The p. 8 death wording says “died of TB,” while pp. 4/6 label the outcome simply death and p. 5 states TB disease was cause for `32/52 (61.5%)` deaths.
- **Diagnostic rule:** match populations/outcome definition and compare numeric repetitions without assuming unreported cause attribution for every death.

## Inferential-statistical relationships

### M-S001 — Sample-size statistical plan

- **Location:** PDF p. 3.
- **Direct observation:** `90%` power, two-sided alpha `5%`, planned `18%` versus `8%` abstinence, ICC `0.02`, design effect `1.5`, 20% attrition.
- **Rule candidate:** planning computation can only be assessed with stated cluster-size/design-effect/attrition conventions; map separately from observed effect estimates.

### M-S002 — Analysis methods and stated decision convention

- **Location:** PDF p. 3 Statistical Analysis.
- **Direct observation:** mixed-effects categorical models include intervention fixed effect and post-hoc covariates age, sex, education, occupation, smoking duration with cluster random effects; logistic regression, Bayesian hierarchical logistic model (brms) with 95% credible intervals, ICC from lme4 mixed-effects logistic variance components; death compared by Cox proportional-hazards frailty model adjusting site-level clustering; secondary outcomes exploratory and no multiple-comparison adjustment; analyses two-sided and `P<.05` statistically significant.
- **Rule candidate:** comparisons of reported RR/HR/ICC must retain model, adjustment, analysis set, and interval type (confidence versus credible) distinctions.

### M-S003 — Primary ITT verified abstinence effect

- **Locations / match key:** PDF pp. 1, 4, 6; `ITT-primary-abstinence|month-6|CO<10ppm`.
- **Direct observation:** RR `3.0 (95% CI, 2.0-4.9)`, primary proportions `41.7%` versus `15.3%`, counts `300/720` versus `55/360`, absolute difference `26.4 (21.0-31.6)`, ICC `0.18`.
- **Rule candidate:** match effect estimate to the CO <10 ppm ITT result; inspect point estimate/CI ordering and narrative/table/abstract identity.

### M-S004 — Primary adjusted and CO-threshold sensitivity effects

- **Locations:** PDF pp. 4 and 6.
- **Direct observation:** adjusted primary RR `3.2 (2.2-5.2)`, ICC `0.18`; CO <6 ppm ITT crude RR `3.7 (2.4-5.8)`, ICC `0.16`, adjusted RR `3.9 (2.4-6.9)`, ICC `0.18`; CO <6 ppm PP crude RR `3.6 (2.14-6.87)`, ICC `0.17`, adjusted RR `3.8 (2.3-7.7)`, ICC `0.18`.
- **Rule candidate:** threshold, ITT/PP status, and adjustment are necessary match fields; confidence intervals should contain their printed point estimate.

### M-S005 — Primary PP verified abstinence effect

- **Location:** PDF p. 6 Table 2.
- **Direct observation:** CO <10 ppm PP crude RR `2.9 (2.0-4.7)`, ICC `0.19`; adjusted RR `3.1 (2.1-5.2)`, ICC `0.19`; counts `300/667` versus `55/318`.
- **Rule candidate:** denominator linkage to Figure 1 non-loss counts and interval containment, preserving PP label.

### M-S006 — Self-reported-only continuous abstinence effect

- **Location:** PDF p. 6 Table 2.
- **Direct observation:** crude RR `2.7 (1.8-4.1)`, ICC `0.19`; adjusted RR `2.8 (1.9-42)`, ICC `0.19`; counts `342/720` versus `70/360`; absolute difference `28.1 (22.6-33.5)`.
- **Rule candidate:** check CI containment and label/scale; record that `42` is source-printed and direct-render confirmed (M-N018).

### M-S007 — Point-abstinence effects

- **Location:** PDF p. 6 Table 2.
- **Direct observation:** week 9 crude RR `2.6 (1.8-3.9)`, ICC `0.19`; adjusted `2.7 (1.8-4.3)`, ICC `0.18`. Month 6 crude RR `2.7 (2.0-3.8)`, ICC `0.19`; adjusted `2.7 (1.9-4.0)`, ICC `0.19`.
- **Rule candidate:** match last-7-day timepoint and ITT label; assess CI containment/ordering and crude-versus-adjusted field identity.

### M-S008 — TB-treatment-success effects

- **Locations:** PDF pp. 1, 5, 6.
- **Direct observation:** crude RR `1.2 (0.9-1.6)`, ICC `0.16`; adjusted RR `1.2 (0.9-1.5)`, ICC `0.15`; counts/proportions `643/720, 89.3%` versus `308/360, 85.6%`; absolute difference `3.8 (-0.5 to 8.2)`.
- **Rule candidate:** match treatment-success definition (`cured + completed`) and RR model; inspect CI containment and cross-occurrence identity.

### M-S009 — Mortality/death survival-model relationship

- **Locations:** PDF pp. 1, 5, 6.
- **Direct observation:** death `25/720, 3.5% (2.2-5.0)` mHealth versus `27/360, 7.5% (5.0-10.7)` usual care; absolute difference `4 (1.0-7.1)`; adjusted HR `0.4 (0.2-0.9)` using shared-frailty Cox model; no crude RR/ICC reported (NA).
- **Rule candidate:** distinguish a risk/proportion difference from a Cox HR and preserve the table’s unnamed absolute-difference direction convention.

### M-S010 — Default and treatment-failure low-event rows

- **Location:** PDF p. 6 Table 2.
- **Direct observation:** default and failure have NA in crude RR, crude ICC, adjusted RR/HR, and adjusted ICC columns; footnote attributes inability to estimate mixed-effects models to very low event numbers across clusters. Default counts `22/720` versus `7/360`; failure `1/720` versus `2/360`.
- **Rule candidate:** verify NA is consistent with the stated low-event model limitation and avoid treating NA as a zero effect estimate.

### M-S011 — Adherence comparison P value

- **Locations:** PDF pp. 1 and 5.
- **Direct observation:** mean adherence `174.3 (SD 21.5)` versus `178.0 (SD 12.1)` days; `P=.23`.
- **Rule candidate:** no test statistic, SE, exact test, or CI is printed in DOC-001. Retain the P value as an unpaired reported inferential value; do not infer a compatibility calculation without the missing inputs.

### M-S012 — Bayesian cluster-model result

- **Locations:** PDF pp. 4 and 7.
- **Direct observation:** Bayesian hierarchical model showed heterogeneity of cluster quitting probabilities, with generally higher fitted rates in mHealth; figure presents posterior means and 95% credible-interval whiskers, no printed numeric values.
- **Rule candidate:** check label consistency (credible, not confidence, intervals) and graphical claims only; no exact interval arithmetic can be reproduced from the figure.

### M-S013 — Results/discussion qualitative inferential wording

- **Locations:** PDF pp. 4-5, 8.
- **Direct observation:** primary association described as persisting after covariate adjustment; CO <6 sensitivity described as consistent/robust; point abstinence higher; adherence similar; death probability significantly higher in usual care; observed ICC `0.19` described as higher than planned `0.02` while primary effect remained statistically significant.
- **Rule candidate:** narrative interpretation should be matched to the appropriate result/model/threshold. “Significantly” has an explicit paper convention of two-sided P<.05 but no death P value is printed in DOC-001.

### M-S014 — Display-zero check

- **Scope result:** No `P=0`, `p=0.000`, or equivalent display-zero P value appears in DOC-001 pp. 1-9.
- **Direct observation:** The sole explicit p value in the main-paper result narrative is `P=.23` for adherence.

## Mapping limitations

- Figure 2 supplies graphical marks and exact cluster follow-up sizes but not printed numerical posterior means, observed proportions, or credible-interval endpoints; this map does not estimate plotted values.
- Main-paper narrative directs some detailed evidence to Supplement 2 (eTables/eFigure); those exact supplement records are intentionally outside this DOC-001-only shard.
- Direct PDF text on p. 6 and direct image rendering agree that the adjusted self-reported-only interval endpoint is printed as `42`; this map preserves that exact source value without deciding its meaning.

## Counts

- Numeric/reporting relationships: **20** (`M-N001`-`M-N020`).
- Inferential-statistical relationships: **14** (`M-S001`-`M-S014`).
- PDF coverage: **9/9 pages complete**; one no-applicable-results reference page (PDF p. 9).
