# Global Numeric and Reporting Relationship Inventory

Stable global IDs are assigned in deterministic source/page/shard order. Each entry preserves its mapper-local provenance and full mapped evidence.

## N001 — Abstract trial population, allocation, retention, and primary outcome

- **Mapper-local relationship:** M-N001
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Locations / repeated occurrence key:** PDF p. 1 Abstract Results; match key `DOC001|ITT-primary-abstinence|month-6|CO<10ppm|mHealth-vs-usual-care`.
- **Printed values:** 9232 assessed; 1080 randomized; mHealth `n = 720`, usual care `n = 360`; 985 retained throughout trial (91%). Primary verified continuous abstinence: mHealth `300/720 (41.7%)`; usual care `55/360 (15.3%)`; RR `3.0 (95% CI, 2.0-4.9)`.
- **Population/time/contrast/unit:** people with TB who smoked; 6 months; mHealth versus usual care; persons/proportion/percent.
- **Direct observation:** These are the printed abstract summary values.
- **Diagnostic rule for downstream check:** match to Figure 1, Table 2 ITT primary row, and Results narrative, allowing identical displayed precision.


## N002 — Abstract selected secondary outcomes

- **Mapper-local relationship:** M-N002
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Locations / match keys:** PDF p. 1 Abstract Results; `adherence|month-6`, `TB-success|month-6`, `death|month-6`, `default|month-6`, `failure|month-6`.
- **Printed values:** adherence mean (SD), `174.3 (21.5)` days mHealth versus `178.0 (12.1)` usual care, `P = .23`; treatment success `89.3%` versus `85.6%`, RR `1.2 (95% CI, 0.9-1.6)`; treatment failure `0.1%` versus `0.5%`; default `3.1%` versus `1.9%`; mortality `3.5%` versus `7.5%`, HR `0.4 (95% CI, 0.2-0.9)`.
- **Direct observation:** Printed abstract outcome summary.
- **Diagnostic rule:** match values and effect-measure labels to PDF pp. 4 and 6; distinguish HR for death from RR rows.


## N003 — Key Points repetition of trial sample and primary proportions

- **Mapper-local relationship:** M-N003
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location / match key:** PDF p. 2 Key Points, `ITT-primary-abstinence|month-6|CO-supported`.
- **Printed values:** trial included `1080` patients with TB who smoked; self-reported continuous abstinence at 6 months supported by biochemical verification: `41.7%` mHealth versus `15.3%` usual care.
- **Direct observation:** The Key Points omit numerator/denominator and interval but repeat the principal comparison.
- **Diagnostic rule:** cross-location identity with M-N001/M-N011/M-N015 after matching outcome definition and precision.


## N004 — Intervention exposure and outcome-definition quantities

- **Mapper-local relationship:** M-N004
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Locations:** PDF pp. 1 and 3.
- **Printed values:** mHealth `n=720`, text messages daily for `2 months` then monthly for `4 months`; `134` unique messages over `6 months`: `100` (3-4/day) in first month, `30` (1/day) in second month, and `4` (1/month) over next four months. Primary abstinence definition: no more than `5` cigarettes/bidis/water-pipe sessions since quit date, which was `5 days` after enrollment; CO `<10 ppm` at month 6; urine cotinine negative where baseline smokeless tobacco was concomitantly used. Point abstinence was prior `7 days`, assessed week `9` and month `6`; default was interruption for `>=2 months`.
- **Direct observation:** Printed intervention schedule and definitions needed to identify outcome scale/time/threshold.
- **Diagnostic rule:** ensure like-for-like matching of the `<10 ppm`, `<6 ppm`, ITT, PP, continuous, and last-7-day outcomes.


## N005 — Sample-size planning inputs

- **Mapper-local relationship:** M-N005
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location / match key:** PDF p. 3 Sample size paragraph, `sample-size-plan|cluster-RCT`.
- **Printed values:** `90%` power, `5%` two-sided significance, planned abstinence probabilities `18%` mHealth and `8%` usual care at 6 months, ICC `0.02`, cluster size `26`, design effect `1.5`, anticipated attrition `20%`, target `1080` participants and `27` clusters, capped at `40` participants/cluster.
- **Direct observation:** These are planned design quantities, not observed results.
- **Diagnostic rule:** later distinguish planned ICC/design effect from observed Table 2 ICCs.


## N006 — Participant flow and exclusions (Figure 1 plus results narrative)

- **Mapper-local relationship:** M-N006
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Locations / match key:** PDF p. 4 Figure 1 and Participants text, `participant-flow|enrolment-randomization-month-6`.
- **Printed values:** `249` clusters / `9232` patients assessed; `222` clusters / `8152` patients excluded; exclusion items: `7069` not current smoker, `2783` not diagnosed pulmonary TB, `1820` not diagnosed within 4 weeks, `1290` no mobile-phone access, `385` age <15, `273` not willing to quit, `236` unable to read and no household reader, `6` refused; clinic items `182` new TB registrations <50/month and `40` not fit. The figure footnote says participants could be excluded for more than one reason. `27` clinics randomized: mHealth `18` clusters, `720` participants, cluster size `40`; usual care `9` clusters, `360` participants, cluster size `40`; both received allocated care and all `720`/`360` were included in primary analysis. Follow-up loss: mHealth `53` (`25` died, `18` no contact, `10` withdrew); usual care `42` (`27` died, `9` no contact, `6` withdrew); no clusters lost in either group.
- **Additional printed narrative:** six refused and `8146` did not meet inclusion criteria; `8.8%` did not provide primary outcome, described as `4.8%` died, `1.5%` withdrew, `2.5%` lost contact.
- **Direct observation:** Figure and adjacent text report the complete values above.
- **Diagnostic rules:** flow arithmetic within each allocated group (`720-53=667`, `360-42=318`); exclusions are explicitly non-exclusive, so individual reason counts are not intended to sum to excluded patients.


## N007 — Table 1 cluster-level baseline characteristics

- **Mapper-local relationship:** M-N007
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location / match key:** PDF p. 5 Table 1, `baseline|cluster-characteristics`.
- **Printed values (mHealth; usual care):** total clusters `18; 9`; cluster size `40; 40`; rural setting `11; 7`; average TB cases/month `142; 93`.
- **Direct observation:** Table 1 values, with no percentage label for the cluster rows.
- **Diagnostic rule:** group allocation totals should correspond to M-N001/M-N006 and participant totals below.


## N008 — Table 1 participant demographics and education

- **Mapper-local relationship:** M-N008
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location / match key:** PDF p. 5 Table 1, `baseline|participants-demographics-education`.
- **Printed values (mHealth; usual care):** total `720; 360`; age mean (SD) years `48.7 (15.8); 48.7 (15.9)`; male `698 (96.9%); 345 (95.8%)`; female `22 (3.1%); 15 (4.2%)`; BMI median (IQR) `18.7 (4); 18.6 (4)`.
- **Education, No. (%):** no formal education `315 (43.8); 155 (43.1)`; primary `175 (24.3); 114 (31.7)`; middle `109 (15.1); 43 (11.9)`; secondary `89 (12.4); 36 (10)`; higher `32 (4.4); 12 (3.3)`.
- **Direct observation:** Printed Table 1 values. BMI footnote defines kg divided by height in meters squared.
- **Diagnostic rule:** counts/percentages and mutually exclusive education categories can be mechanically checked against group denominators, subject to displayed rounding.


## N009 — Table 1 social/employment, reading, and clinical-severity characteristics

- **Mapper-local relationship:** M-N009
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location / match key:** PDF p. 5 Table 1, `baseline|social-employment-reading-TB-stage`.
- **Printed values (mHealth; usual care):** marital: single `83 (11.5); 37 (10.3)`, married `607 (84.3); 304 (84.4)`, separated/divorced `30 (4.2); 19 (5.3)`; employment: employed `560 (77.8); 275 (76.4)`, dependents `128 (17.8); 71 (19.7)`, retired `32 (4.4); 14 (3.9)`; able to read messages `425 (59.0); 225 (62.5)`; TB stage 1 `629 (87.4); 326 (90.6)`, stage 2 `45 (6.3); 20 (5.6)`, stage 3 `46 (6.4); 14 (3.9)`.
- **Definitions:** dependents = unemployed, homemakers, students, or otherwise not actively employed. Stage 1 mild-moderate, stage 2 severe, stage 3 very severe TB disease.
- **Direct observation:** Printed Table 1 values/footnotes.
- **Diagnostic rule:** check mutually exclusive category sums and denominator precision separately for each treatment group.


## N010 — Table 1 tobacco-related baseline characteristics

- **Mapper-local relationship:** M-N010
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location / match key:** PDF p. 5 Table 1, `baseline|tobacco-history`.
- **Printed values (mHealth; usual care):** smoking type: cigarettes `679 (94.3); 326 (90.6)`, hookah `61 (8.5); 35 (9.7)`, bidi `21 (2.9); 21 (5.8)`, concurrent smokeless use `50 (6.9); 8 (2.2)`. Tobacco use/day median (IQR): bidi `8 (10.0); 15 (14.0)`, cigarettes `5 (6.0); 7 (6.0)`, hookah `3 (4.0); 3 (2.0)`. Smoking allowed inside homes `482 (66.9); 189 (52.5)`; attempted quit in past `178 (24.7); 33 (9.2)`; mean smoking duration (SD), years `24.8 (15.1); 24.6 (15.2)`; median smoking start age (IQR), years `20 (9.0); 20 (8.0)`; low-addiction Heaviness of Smoking Index `514 (75.7); 212 (65.0)`.
- **Direct observation:** Printed Table 1 values. Smoking-type rows can overlap; the table does not label them as mutually exclusive.
- **Diagnostic rule:** compare repeated cigarette/smokeless use, daily medians, and prior quit percentages to p. 4 narrative; do not sum overlapping smoking types.


## N011 — Primary-outcome narrative occurrences

- **Mapper-local relationship:** M-N011
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location / match key:** PDF p. 4 Primary Outcome, `ITT-primary-abstinence|month-6|CO<10ppm`; repeated on PDF pp. 1-2.
- **Printed values:** self-report only: `47.5%` mHealth versus `19.4%` usual care. Biochemically verified ITT at CO `<10 ppm`: mHealth `41.7% (95% CI, 38.0%-45.4%)`; usual care `15.3% (95% CI, 11.7%-19.4%)`; RR `3.0 (95% CI, 2.0-4.9)`. Post-hoc adjusted RR `3.2 (95% CI, 2.2-5.2)` after age, sex, education, occupation, smoking duration. Among verified abstainers, CO mean (SD) ppm `3.54 (2.1)` mHealth and `4.38 (2.8)` usual care. Sensitivity CO `<6 ppm`: RR `3.7 (95% CI, 2.4-5.8)`.
- **Direct observation:** Narrative reports the listed values; Table 2 supplies the matching counts and additional intervals.
- **Diagnostic rule:** matching by CO threshold, ITT status, and adjustment status is required before cross-occurrence comparison.


## N012 — Secondary-outcome narrative occurrences

- **Mapper-local relationship:** M-N012
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location / match keys:** PDF pp. 4-5 Results, `point-abstinence|week-9/month-6`, `adherence|month-6`, `TB-success|month-6`, `failure/default/death|month-6`.
- **Printed values:** mean adherence: `174.3 (SD 21.5)` versus `178.0 (SD 12.1)` days, `P=.23`; treatment success `643/720 (89.3%)` versus `308/360 (85.6%)`, RR `1.2 (95% CI, 0.9-1.6)`; treatment failure `1/720 (0.1%)` versus `2/360 (0.5%)`; default `22/720 (3.1%)` versus `7/360 (1.9%)`; deaths `3.5%` versus `7.5%`, HR `0.4 (95% CI, 0.2-0.9)`; TB disease cause of death `32/52 (61.5%)`.
- **Direct observation:** These values are printed Results narrative; point-abstinence values are referenced to Table 2 rather than repeated numerically.
- **Diagnostic rule:** match counts/denominators to Table 2; distinguish total deaths `52` across groups from ITT denominators and Cox HR.


## N013 — Attrition, fidelity, and descriptive results

- **Mapper-local relationship:** M-N013
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location:** PDF p. 4 Participants section.
- **Printed values:** all mHealth participants confirmed message receipt. At month 6, `8.8%` lacked primary outcome; `4.8%` died, `1.5%` withdrew, `2.5%` lost contact. No outcome data were missing beyond these participants.
- **Direct observation:** Printed descriptive/operational claims.
- **Diagnostic rule:** compare the component percentages and group-level Figure 1 counts with the stated overall denominator and rounding conventions.


## N014 — Adverse-event percentages

- **Mapper-local relationship:** M-N014
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location / match key:** PDF p. 5 Adverse Events, `adverse-events|mHealth-vs-usual-care`.
- **Printed percentages (mHealth versus usual care):** nausea `23.0 vs 22.3`; diarrhea `7.5 vs 7.5`; dry mouth `62.7 vs 55.7`; epigastric pain `27.7 vs 40.4`; headache `45.1 vs 49.1`; insomnia `35.3 vs 33.5`; abnormal dreams `10 vs 13.2`; irritability `40.5 vs 43.4`; anxiety `33.3 vs 36.8`; palpitations `31 vs 28.4`; musculoskeletal pain `61.4 vs 60.8`. Narrative says dry mouth, irritability, and anxiety were more common in mHealth.
- **Direct observation:** The main paper gives percentages only and points to eTable 10 for further detail.
- **Diagnostic rule:** retain label, direction, and percent scale; no numerator/denominator is printed here.


## N015 — Table 2 primary outcome rows (all count/proportion/absolute-difference fields)

- **Mapper-local relationship:** M-N015
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location / match key:** PDF p. 6 Table 2, `Table2|primary-abstinence|threshold-analysis-population`.
- **Rows, printed mHealth; usual care; absolute difference (95% CI):**
  - CO `<10 ppm`, ITT: `300/720`, `41.7 (38.0-45.4)%`; `55/360`, `15.3 (11.7-19.4)%`; `26.4 (21.0-31.6)` percentage points.
  - CO `<10 ppm`, PP: `300/667`, `45 (41.2-48.8)%`; `55/318`, `17.3 (13.3-21.9)%`; `27.7 (22.1-33.3)`.
  - CO `<6 ppm`, ITT: `264/720`, `36.7 (33.1-40.3)%`; `38/360`, `10.6 (7.6-14.2)%`; `26.1 (21.2-30.7)`.
  - CO `<6 ppm`, PP: `264/667`, `39.6 (35.9-43.4)%`; `38/318`, `11.9 (8.6-16.1)%`; `27.7 (22.5-32.8)`.
  - Continuous abstinence self-reported only, ITT: `342/720`, `47.5 (43.8-51.2)%`; `70/360`, `19.4 (15.5-23.9)%`; `28.1 (22.6-33.5)`.
- **Direct observation:** Table 2 reports number of outcomes/total group total, as defined by footnote b. CO cutoffs are defined by footnote e.
- **Diagnostic rule:** denominators should align with Figure 1 allocated/lost counts for ITT and PP; primary outcome threshold/analysis labels must not be interchanged.


## N016 — Table 2 secondary outcome rows (all count/proportion/absolute-difference fields)

- **Mapper-local relationship:** M-N016
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


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


## N017 — Table 2 model/measure labels and applicability

- **Mapper-local relationship:** M-N017
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location:** PDF p. 6 Table 2 column headings and footnotes.
- **Printed definitions:** RR = relative risk; HR = hazard ratio; ICC = intraclass correlation coefficient; ITT = intention-to-treat; PP = per-protocol; NA = not applicable. Adjusted for age, sex, education, occupation, smoking duration; adjusted RR analyses account for clustering via mixed-effects models and adjusted HR uses shared-frailty Cox model. ICC is reported for RR models only. Death HR is Cox proportional-hazards frailty estimate. Mixed-effects models could not be estimated for default/failure owing to very low event numbers across clusters.
- **Direct observation:** Printed Table 2 labels/footnotes.
- **Diagnostic rule:** effect measure and NA/ICC applicability must be matched to the corresponding row and model.


## N018 — Visually confirmed printed adjusted self-report interval

- **Mapper-local relationship:** M-N018
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location / match key:** PDF p. 6 Table 2, continuous abstinence self-reported only (ITT), adjusted column; direct rendering confirmation.
- **Printed value:** adjusted RR `2.8 (1.9 to 42)`, ICC `0.19`.
- **Direct observation:** The native/layout text reads `42`; direct visual confirmation shows the endpoint printed as `42` (not `4.2`).
- **Diagnostic rule:** later evaluate interval/estimate compatibility and any matching occurrence using the direct-source printed value `42`; no normalization has been applied in this map.


## N019 — Figure 2 Bayesian cluster display

- **Mapper-local relationship:** M-N019
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location / match key:** PDF p. 7 Figure 2, `Bayesian-cluster-quit-probability|month-6`.
- **Printed structure:** panel A mHealth, cluster IDs `18` through `1`, follow-up cluster sizes `38, 39, 37, 39, 38, 39, 34, 36, 34, 40, 38, 36, 36, 39, 35, 33, 40, 36`; panel B usual care, cluster IDs `9` through `1`, sizes `35, 37, 36, 30, 38, 36, 33, 38, 35`. Both panels have probability percentage axis `0, 20, 40, 60, 80, 100`; posterior means and observed cluster proportions are plotted; whiskers indicate 95% credible intervals. Caption says posterior means include fixed + random effects.
- **Direct observation:** The chart has no printed numeric posterior mean, observed proportion, or CI endpoint for an individual cluster.
- **Diagnostic rule:** only graphical direction/label/cluster-size mapping is available locally; avoid transcribing unprinted plotted values as exact numbers.


## N020 — Discussion/limitations repetitions relevant to trial results

- **Mapper-local relationship:** M-N020
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/main_evidence_DOC-001_pp001-009.md`


- **Location / match keys:** PDF p. 8 Discussion/Limitations, `death|month-6|trial-total` and `observed-ICC|primary-analysis`.
- **Printed values:** `4.8%` of trial participants died of TB within 6 months; observed ICC `0.19`, compared with sample-size assumed ICC `0.02`; participants almost entirely male (`>96%`); CO verifies recent `24-48` hour abstinence due to half-life `5-6` hours.
- **Direct observation:** Narrative claims/repetitions. The p. 8 death wording says “died of TB,” while pp. 4/6 label the outcome simply death and p. 5 states TB disease was cause for `32/52 (61.5%)` deaths.
- **Diagnostic rule:** match populations/outcome definition and compare numeric repetitions without assuming unreported cause attribution for every death.

## Inferential-statistical relationships


## N021 — Background burden and association values

- **Mapper-local relationship:** A-N001
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 7 states TB affects “>10 million” people annually; “approx. 1.5 million” die; smoking is responsible for “16%” of total TB disease burden; smoking increases chances of acquiring TB infection and TB disease by two- and three-fold, respectively; and smoking doubles the risk of TB-related deaths.
- **Population/time/label:** Background statements, not trial outcomes; annual/global burden and cited associations.
- **Calculation/check key:** Preserve the qualifiers (`>`, `approx.`, and cited causal/association wording). These are not denominators or trial estimates.


## N022 — Primary outcome definition

- **Mapper-local relationship:** A-N002
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 8 defines the primary endpoint as biochemically verified continuous abstinence at 6 months post-randomisation. Abstinence means self-report of no more than 5 cigarettes, bidis, or water-pipe sessions since quit date, plus CO <10 ppm at month 6. For concurrent smokeless-tobacco use, cotinine strip level <3 (described as equivalent to 100-200 ng/mL cotinine) is considered tobacco abstinence; an elevated CO >10 ppm or active-use cotinine overrides self-report.
- **Population/time/contrast/label:** Randomised TB patients who smoke daily; month 6; endpoint definition rather than effect result.
- **Calculation/check key:** Match any main-paper primary cessation outcome only after confirming the 6-month time point, continuous-abstinence rule, CO threshold/direction, and cotinine exception.


## N023 — Secondary point-abstinence outcome

- **Mapper-local relationship:** A-N003
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 8 defines point abstinence as self-report of no tobacco use in the previous 7 days, assessed at week 9 and month 6.
- **Calculation/check key:** Do not equate this 7-day point-prevalence outcome with the N002 continuous-abstinence outcome.


## N024 — TB-programme outcome categories

- **Mapper-local relationship:** A-N004
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF pp. 8-9 states that at month 6 the TB register (TB03) will record proportions with treatment success (cured plus completed treatment), treatment failure, defaulted, and died. It defines cure, completed treatment, treatment failure (initially smear-positive and remains smear-positive at month 5 or later), default (interrupted for 2 consecutive months or more), died, and relapse.
- **Calculation/check key:** For a complete mutually exclusive outcome tabulation, treatment success is explicitly `cured + completed treatment`; preserve the stated month-6 and TB03-register population.


## N025 — Trial phases and comparisons

- **Mapper-local relationship:** A-N005
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 9 describes four phases. Phase 3 is a 12-month superiority trial (6 months recruitment + 6 months follow-up) comparing intervention A (mTB-Tobacco) with C (usual care). Phase 4 is another 12-month non-inferiority trial (6+6 months), comparing A with B (face-to-face behavioural support).
- **Calculation/check key:** Comparisons are A vs C in Phase 3 and A vs B in Phase 4; retain phase and superiority/non-inferiority labels when matching results.


## N026 — Country burden/prevalence table

- **Mapper-local relationship:** A-N006
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 10 table prints Bangladesh: TB 221 per 100,000; TB cases 357,000; TB deaths 47,000; tobacco prevalence 35%. Pakistan: TB 265 per 100,000; cases 562,000; deaths 44,000; tobacco prevalence 20%.
- **Calculation/check key:** These are country-level contextual quantities with distinct units (rate per 100,000, count, percentage); do not combine them as trial denominators.


## N027 — Protocol sample-size plan, Phase 3 and Phase 4

- **Mapper-local relationship:** A-N007
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 10 says total required is 2,384 TB smokers, approximately 50 recruits from 44 health facilities, assuming 10% lack primary-outcome data; includes first 16 pilot participants. Phase 3 compares 16 clusters randomised to A and 8 to C, assuming 8% abstinence in usual care and 18% with mTB-Tobacco at 6 months. Phase 4 has 20 clusters each in A and B, assumes 18% face-to-face abstinence at six months and an 8% non-inferiority margin. It states natural cessation is 2%, so face-to-face effect is 16% (=18%-2%), and an 8% margin preserves at least 50% (=8/16) of that effect.
- **Calculation/check key:** Explicit displayed arithmetic: `18% - 2% = 16%`; `8 / 16 = 50%`. The 2,384 total is a protocol design target, not an analysed denominator.


## N028 — Eligibility age and diagnostic window

- **Mapper-local relationship:** A-N008
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 11 requires age at least 15 years and diagnosis with drug-sensitive pulmonary TB in the last four weeks; exclusion includes age below 15 years.
- **Calculation/check key:** The age boundary is inclusive at 15 years; retain this eligibility population separately from all-randomised/analysed populations.


## N029 — Consent/reimbursement timing and amounts

- **Mapper-local relationship:** A-N009
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 12 gives eligible patients 24 hours to consider participation and states reimbursement about 200 PKR/visit, 113 BDT/visit, and £0.97/visit.
- **Calculation/check key:** Values are country/currency-specific visit reimbursements, not a common monetary scale.


## N030 — Cluster allocation ratio

- **Mapper-local relationship:** A-N010
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 13 specifies cluster (health-facility) randomisation 2:2:1 to A, B, and C, respectively, with minimisation by average monthly TB-patient volume and country/geographic location.
- **Calculation/check key:** Allocation occurs at facility/cluster level, not individual-patient level; expected cluster-count ratio is 2:2:1.


## N031 — Flow-diagram recruitment and cluster totals

- **Mapper-local relationship:** A-N011
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF pp. 13-14 flow diagram prints: total TB patients recruited in Phases 2-4 = 2,384 (37 patients/site); Phase 3 = 24 sites, 888 + 16 pilot = 904 patients; Bangladesh Phase-3 branch = 14 sites (the visible recruitment total is continued on p. 14); Pakistan Phase-3 branch = 10 sites, `10 x 37 = 370 + 8 (pilot) = 378`; Phase-3 allocation A 16 sites and Control 8 sites. Phase 4 = 40 sites and 1,480 patients; Bangladesh 24 sites, `24 x 37 = 888`; Pakistan 16 sites, `16 x 37 = 592`; allocation A 20 sites and B 20 sites.
- **Calculation/check key:** Displayed components reconcile: `904 + 1,480 = 2,384`; `888 + 592 = 1,480`; `16 + 8 = 24`; `20 + 20 = 40`; `24 + 16 = 40`; `10x37 + 8 = 378`. The flow diagram is a source location for matching N007 design totals.


## N032 — Pilot size and country split

- **Mapper-local relationship:** A-N012
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 15 states the Phase-2 pilot has 16 participants, 8 each in Bangladesh and Pakistan; it is embedded in Phase 3.
- **Calculation/check key:** `8 + 8 = 16`; distinguish pilot participants from the Phase-3 non-pilot recruitment figure in the flow diagram.


## N033 — mTB-Tobacco delivery dose

- **Mapper-local relationship:** A-N013
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 16 states every intervention-group participant receives 178 SMS messages over 6 months: first 2 months, 4-5 messages/day; next 2 months, 2-3/day; last 2 months, 1-2/week.
- **Calculation/check key:** Dose is a planned intervention schedule with ranges; it is not an observed message-receipt count.


## N034 — Face-to-face behavioural-support session timing/duration

- **Mapper-local relationship:** A-N014
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 17 states intervention B has sessions at day 0 and day 5 (±2), lasting 10 and 5 minutes, respectively, with further support at week 5 if needed.
- **Calculation/check key:** Keep session durations paired with their specified visits and distinguish a conditional further contact from the two core sessions.


## N035 — Assessment schedule/time points

- **Mapper-local relationship:** A-N015
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 17 specifies assessments at day 0, week 9, and month 6. Table entries: screening eligibility and written consent; self-reported tobacco use/abstinence at baseline, week 9, month 6; CO at month 6; sociodemographics and tobacco/quit history at baseline; nicotine dependency baseline/week 9/month 6; economic outcomes baseline/month 6; process outcomes week 9/month 6; TB-medication compliance, adverse-event review week 9/month 6; TB outcomes month 6. Face-to-face/phone interaction at week 9 applies only to Phase-2 pilot participants.
- **Calculation/check key:** Match outcome values only to the schedule’s time point and applicable population (especially the Phase-2-only footnote).


## N036 — Visit windows

- **Mapper-local relationship:** A-N016
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 18 says treatment-period visits should be completed within 2 days of scheduled date; follow-up assessments no more than 5 days before scheduled visit; rescheduled follow-up no more than 5 days from original date; if more than 5 days late, conduct an additional visit as soon as possible.
- **Calculation/check key:** These are operational windows, not alternative endpoint time points.


## N037 — Measurement/data-source definitions

- **Mapper-local relationship:** A-N017
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF pp. 18-19 says socio-demographics and tobacco use/withdrawal data are collected once at baseline; economic data include delivery cost, health-service use, and quality of life; CO verification is for people reporting abstinence at final follow-up; TB adherence/outcomes come from routine TB records and are validated through CRFs.
- **Calculation/check key:** Distinguish source (routine TB register vs CRF), baseline-only measures, and final-follow-up biochemical verification when comparing reported values.


## N038 — Retention and withdrawn-participant data rule

- **Mapper-local relationship:** A-N018
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 20 says no further assessments after withdrawal of consent, but already collected data remain on file and are included in final study analysis; data are archived at least 10 years.
- **Calculation/check key:** Do not infer treatment/outcome status from the data-retention rule; it is relevant only if an analysis-population statement requires reconciliation.


## N039 — Trial-number structure and retention period

- **Mapper-local relationship:** A-N019
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF pp. 22-23 says screening forms contain a site identifier and a screening number (the patient TB registration number), unique at that site; follow-up forms for randomised individuals contain a trial number unique across the trial. It repeats minimum 10-year data retention.
- **Calculation/check key:** Site-level screening identifiers and trial-wide post-randomisation identifiers are not interchangeable participant counts.


## N040 — Repeated sample-size specification

- **Mapper-local relationship:** A-N020
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 26 repeats total 2,384 TB smokers, but describes “~50 recruits from 48 health clinics [clusters]”; 10% missing primary outcome; first 16 pilot participants; Phase-3 16 A/8 C clusters, 90% power at 5%; assumed 8% usual-care and 18% mTB-Tobacco abstinence at 6 months; Phase-4 20 clusters each A/B, 90% power at one-sided 2.5%, 18% face-to-face abstinence, 8% margin; 2% natural cessation, 16% treatment effect, 50% preservation.
- **Matching key:** This is a repeated occurrence of the N007 sample-size parameter set. Preserve exact printed wording, especially **44 health facilities on PDF p. 10** versus **48 health clinics on PDF p. 26**, for downstream cross-source verification; the source alone does not state a resolution.


## N041 — Economic endpoints and calculation quantities

- **Mapper-local relationship:** A-N021
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 27 states Phase-3 CEA has a 12-month horizon, uses EQ-5D-5L to calculate QALYs, and presents incremental cost per QALY and cost per additional quitter. Phase 4 calculates and compares costs and differences in costs/QALYs, yielding ICERs. It specifies 5,000 bootstrap replications, 95% CIs for ICERs, and CEACs over threshold values.
- **Calculation/check key:** Preserve scale/unit (cost per QALY vs cost per additional quitter), phase, and 12-month horizon; ICER is explicitly calculated from between-arm cost and QALY differences.


## N042 — Adverse-event reporting statement

- **Mapper-local relationship:** A-N022
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 29 says the interventions are behavioural and the proposed CO/data-collection methods have minimal risk; “no adverse events will be reported to the sponsor for this study.”
- **Calculation/check key:** This is a planned reporting statement, not a numerical zero-event result.


## N043 — Monitoring committee minimum composition/frequency

- **Mapper-local relationship:** A-N023
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp001-032.md`


- **Direct observation:** PDF p. 30 describes a committee with a chair and at least two other independent members including a statistician; it will meet at least annually or more often as appropriate.
- **Calculation/check key:** “At least” establishes lower bounds, not a realised count/frequency.

## Inferential-statistical relationships


## N044 — Contextual burden/effect statements and primary objective

- **Mapper-local relationship:** B-N001
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Locations:** DOC-002 PDF p. 45 (printed p. 5), lines 1254-1263 and 1286-1288 (`joi250093supp1_prod_1768590553.08963.pdf#page=45`).
- **Direct observation:** background states TB affects `>10 million` people yearly; approximately `1.5 million` die; smoking is responsible for `16%` of total TB disease burden; smoking increases TB infection and disease chances by `two-` and `three-fold`, respectively; and doubles risk of TB-related deaths and recurrence. The primary objective is effectiveness and cost-effectiveness of mTB-Tobacco for continuous abstinence for `at least six months` among people with TB who smoke daily.
- **Interpretive status:** contextual/background claims and prospective objective, not a reported study effect. Matching main-paper key: continuous abstinence at 6 months, mTB-Tobacco, daily smokers with TB.


## N045 — Primary endpoint definition and biochemical thresholds

- **Mapper-local relationship:** B-N002
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 46 (printed p. 6), lines 1292-1304 (`joi250093supp1_prod_1768590553.08963.pdf#page=46`).
- **Direct observation:** primary endpoint is biochemically verified continuous abstinence at `6 months post randomisation`. Abstinence is self-report of not using more than `5` cigarettes, bidis, or water-pipe sessions since quit date, verified at month 6 by breath CO `<10 ppm`. With smokeless-tobacco use, cotinine strip level is `0-6`; level `<3` (equivalent to `100-200 ng/mL` cotinine) is considered tobacco abstinence. Self-reported abstinence with CO `>10 ppm`, or cotinine in concomitant users indicating active tobacco, is overridden and classified as tobacco use.
- **Source-grounded rule:** any later matched result must preserve population, continuous-versus-point abstinence, 6-month time point, biochemical rule, and threshold direction. The page gives no statistical test or observed event count.


## N046 — Secondary endpoint definitions and TB-outcome time point

- **Mapper-local relationship:** B-N003
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 46 (printed p. 6), lines 1305-1327 (`joi250093supp1_prod_1768590553.08963.pdf#page=46`).
- **Direct observation:** point abstinence is self-report of no tobacco in preceding `7 days`, measured at `week 9` and `month 6`. TB-programme outcomes are proportions of success (cured/completed), failure, defaulted, and died from TB register TB03 at month 6. Definitions include cure (initially smear-positive and smear-negative last treatment month at month 6 and at least one earlier occasion), completed treatment (month 6 but not cure/failure), treatment failure (initially smear-positive and smear-positive at month 6/later), defaulted (interrupted `2 consecutive months or more`), died (any cause during treatment), and relapse (previously treated then recurrent TB).
- **Source-grounded rule:** match later TB results separately from smoking-abstinence outcomes; retain the month-6 and category definition.


## N047 — Eligibility thresholds and planned population

- **Mapper-local relationship:** B-N004
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 47 (printed p. 8), lines 1360-1395 (`joi250093supp1_prod_1768590553.08963.pdf#page=47`).
- **Direct observation:** facility inclusion requires minimum turnover `50` new TB patients/month. Participant inclusion includes age `at least 15 years`, drug-sensitive pulmonary TB diagnosed in previous `4 weeks`, current daily tobacco use or stopping/reducing since TB diagnosis, willingness to quit, and mobile-phone access. Exclusion includes age `<15 years`, retreatment/MDR/miliary/extrapulmonary TB, and tobacco-dependence pharmacotherapy.
- **Source-grounded rule:** these define planned recruitment eligibility, not an observed analysis denominator; use only if a later result identifies this population.

### Design, allocation, planned numbers, and intervention exposure


## N048 — Consent timing and reimbursement values

- **Mapper-local relationship:** B-N005
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 48 (printed p. 9), lines 1404-1425 (`joi250093supp1_prod_1768590553.08963.pdf#page=48`).
- **Direct observation:** eligible patients receive `24 hours` to consider participation. Reimbursement is `400 PKR/visit (fixed amount)` in Pakistan; up to `150 BDT/visit` in Bangladesh depending on travel distance; and `£1.10/visit` for week-9 and 6-month follow-up visits.
- **Interpretive status:** operational/prospective amounts, not outcome data. No calculation or cross-document comparator is supplied on this page.


## N049 — Cluster randomization level, ratio, and balancing variables

- **Mapper-local relationship:** B-N006
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 49 (printed p. 10), lines 1445-1453 (`joi250093supp1_prod_1768590553.08963.pdf#page=49`).
- **Direct observation:** interventions are delivered at group level; health facilities/clusters are allocated `2:2:1` to A, B, or standard care/control. An independent statistician uses computer-generated random-number lists and minimization based on average TB patients/month and country (Bangladesh/Pakistan).
- **Source-grounded rule:** allocation is cluster-level, not participant-level. Diagram and sample-size relationships below split it by phase: Phase 3 uses A/C (2:1) and Phase 4 A/B (1:1).


## N050 — Diagram 1 planned recruitment and allocation flow

- **Mapper-local relationship:** B-N007
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Locations:** DOC-002 PDF pp. 49-50 (printed pp. 10-11), Diagram 1 (`joi250093supp1_prod_1768590553.08963.pdf#page=49`, `#page=50`).
- **Direct observation:** total planned recruitment in phases 2-4 is `2,716`. Phase 3: `27` sites, `1,080 + 16 (pilot) = 1,096`, with `6-month recruitment + 6-month follow-up = 12 months`; Bangladesh `15 × 40 = 600 + 8 pilot = 608`, Pakistan `12 × 40 = 480 + 8 pilot = 488`; A has Bangladesh `10` + Pakistan `8` sites, `40` patients/site; control Bangladesh `5` + Pakistan `4` sites, `40`/site. Phase 4: `36` sites, `1,620`, same 12-month schedule; Bangladesh `22 × 45 = 990`, Pakistan `14 × 45 = 630`; A Bangladesh `11` + Pakistan `7`, `45`/site; B Bangladesh `11` + Pakistan `7`, `45`/site.
- **Direct arithmetic observations:** `608 + 488 = 1,096`; `600 + 480 = 1,080`; `990 + 630 = 1,620`; `1,096 + 1,620 = 2,716`; Phase-3 A has 18 sites and C has 9, and Phase-4 A/B each have 18 sites. The displayed diagram arithmetic reconciles.
- **Matching key:** planned recruitment/flow only; do not match it as an observed CONSORT count.


## N051 — Phase 2 pilot number and PPI group size

- **Mapper-local relationship:** B-N008
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Locations:** DOC-002 PDF pp. 50-51 (printed pp. 11-12), lines 1501-1517 (`joi250093supp1_prod_1768590553.08963.pdf#page=50`, `#page=51`).
- **Direct observation:** PPI group will comprise `six-eight` members in Bangladesh and Pakistan. Pilot testing has `16` participants, `8` per country, embedded in Phase 3; user experience and real-time engagement are evaluated.
- **Repeated occurrence:** the `16` pilot and `8` Bangladesh/`8` Pakistan split recur in Diagram 1 (B-N007) and the sample-size section (B-N017).


## N052 — Intervention A message dose and schedule

- **Mapper-local relationship:** B-N009
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 51 (printed p. 12), lines 1521-1532 (`joi250093supp1_prod_1768590553.08963.pdf#page=51`).
- **Direct observation:** each intervention participant receives total `134` SMS messages over `6 months`: first `2` months, `4 to 5` messages/day; next `2` months, `1 to 2`/day; final `2` months, `1`/week. Phase 3 also provides educational leaflets.
- **Source-grounded rule:** a later process/fidelity result needs the stated six-month dose/schedule and intervention arm A, rather than merely a generic mHealth label.


## N053 — Intervention B delivery timing and duration

- **Mapper-local relationship:** B-N010
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 52 (printed p. 13), lines 1552-1559 (`joi250093supp1_prod_1768590553.08963.pdf#page=52`).
- **Direct observation:** face-to-face behavioural support has two sessions: day `0` and day `5 (±2)`, lasting `10` and `5` minutes respectively; additional support may occur at week `5`.
- **Source-grounded rule:** comparator B is dose/timing-specific; retain it when comparing a Phase-4 outcome against a protocol label.

### Assessment schedule, TAM selection, and data scale


## N054 — Assessment schedule table

- **Mapper-local relationship:** B-N011
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 52 (printed p. 13), table headed Assessment / Screening / Day 0 baseline / Week 9 / Month 6 (`joi250093supp1_prod_1768590553.08963.pdf#page=52`).
- **Direct observation:** eligibility and written consent occur at screening. Self-reported tobacco use/abstinence is scheduled at baseline, week 9, and month 6; CO measurement at month 6; nicotine dependency at baseline, week 9, month 6; economic outcomes baseline/month 6; process outcomes week 9/month 6; TB medication compliance and adverse-event review week 9/month 6; TB outcomes month 6. Face-to-face/phone-based interaction is marked at week 9 and footnote `*` limits it to Phase-2 pilot participants. The TAM questionnaire is marked at month 6 and footnote `**` limits it to Phases 3 and 4 mTB-Tobacco groups.
- **Source-grounded rule:** endpoint timing and data-collection schedule are distinct from actual counts. The table corroborates B-N002/B-N003 for outcome timing.


## N055 — TAM sampling narrative and table values

- **Mapper-local relationship:** B-N012
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 53 (printed p. 14), lines 1564-1575 and 1591-1600 (`joi250093supp1_prod_1768590553.08963.pdf#page=53`).
- **Direct observation:** narrative states that at end of Phase 3, `20%` of mTB-Tobacco intervention participants in each country will complete TAM; at end of Phase 4, `all` mTB-Tobacco intervention participants will complete it. The page table shows Phase 3: Bangladesh `10 sites × 40 × 20% = 80`; Pakistan `8 × 40 × 20% = 64`. Phase 4: Bangladesh `11 × 45 = 495`; Pakistan `7 × 45 = 315`.
- **Direct arithmetic observations:** Phase-3 equations yield 80 and 64 exactly; 80+64 = 144, which is 20% of 720 Phase-3 A participants. Phase-4 equations yield 495 and 315 exactly; total 810, identical to all 18 Phase-4 A sites ×45.


## N056 — TAM questionnaire header percentage versus narrative/equations

- **Mapper-local relationship:** B-N013
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 53 (printed p. 14), table continuation/header and footnote `**` (`joi250093supp1_prod_1768590553.08963.pdf#page=53`).
- **Direct observation:** the table row label reads `TAM questionnaire (30% of participants in the mTB-Tobacco groups)**`. On the same page, the preceding narrative says `20%` in Phase 3 and `all` in Phase 4; the table arithmetic uses 20% for Phase 3 and 100% for Phase 4.
- **Source-grounded comparison rule:** one row label (`30%`) is not numerically aligned with the contemporaneous Phase-3 equations/narrative (`20%`) or Phase-4 all-participant equations/narrative (`100%`). This is an observed label-versus-definition relationship for later checking; no diagnostic conclusion is assigned here.


## N057 — Visit-window rules and TAM scale

- **Mapper-local relationship:** B-N014
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 53 (printed p. 14), lines 1576-1600 (`joi250093supp1_prod_1768590553.08963.pdf#page=53`).
- **Direct observation:** visits should be completed within `2 days` when unable to attend on scheduled day; follow-up assessments no more than `5 days before`; rescheduling no more than `5 days` from original date; a participant more than `5 days late` receives an additional visit. TAM takes about `5 to 10 minutes`.
- **Interpretive status:** measurement/visit timing, no observed result.


## N058 — TAM data structure

- **Mapper-local relationship:** B-N015
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 54 (printed p. 15), lines 1606-1626 (`joi250093supp1_prod_1768590553.08963.pdf#page=54`).
- **Direct observation:** TAM questionnaire has `12` statements, each on a `five-point Likert scale` from strongly disagree to strongly agree. Data collection is baseline once for sociodemographic/self-report outcomes; biochemical verification at final follow-up for those reporting abstinence.
- **Source-grounded rule:** later TAM summaries need retain a 12-item five-point ordinal scale; the protocol does not state a score-combination or statistical rule on this page.

### Statistics/sample-size calculation and diagram relationships


## N059 — Later protocol high-level total and stated cluster average

- **Mapper-local relationship:** B-N016
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 62 (printed p. 21), lines 1859-1863 (`joi250093supp1_prod_1768590553.08963.pdf#page=62`).
- **Direct observation:** statistics section states total `2,716` smokers with TB, approximately `50 recruits from 48 health clinics [clusters]`, assuming `10%` do not provide primary outcome data; includes first `16` pilot participants.
- **Repeated/matching occurrences:** 2,716 and pilot 16 match Diagram 1 (B-N007) and the earlier high-level text on PDF p. 46 (B-S002/B-S003). The stated `48` clinics and approximate `50` recruits/clinic do not match the Diagram 1 total of `63` sites (27 Phase-3 +36 Phase-4), nor the displayed overall ratio 2,716/48 ≈56.6 or 2,716/63 ≈43.1. This is an explicit planned-number cross-location relationship for later checking, not an adjudication.


## N060 — Pilot allocation calculation

- **Mapper-local relationship:** B-N017
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 62 (printed p. 21), lines 1864-1881 (`joi250093supp1_prod_1768590553.08963.pdf#page=62`).
- **Direct observation:** pilot is at `4` randomly selected TB facilities (`2` Bangladesh, `2` Pakistan), randomly assigned to control and intervention; total `n=16` smokers with TB. Diagram: total `4` facilities, `N=16 (Pk=8, Bg=8)`; intervention `2` sites (`nPK=4, nBG=4`) and control `2` sites (`nPK=4, nBG=4`).
- **Direct arithmetic observation:** country and arm components each sum to 16. This differs in stated facility count from the earlier flow diagram's accounting of 16 pilot participants as 8 per country added to Phase-3 country totals, but the Diagram 1 itself does not state number of pilot facilities; no source contradiction is established from those two statements alone.


## N061 — Phase 3 attrition arithmetic and rounding relationship

- **Mapper-local relationship:** B-N018
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 63 (printed p. 22), lines 1894-1898 (`joi250093supp1_prod_1768590553.08963.pdf#page=63`).
- **Direct observation:** printed calculation is `587 + (587 × 0.2) = 704`, total clusters 27, and `704/27 = 26`.
- **Arithmetic comparison rule:** 587 ×1.2 = 704.4; the displayed 704 is a plausible integer rounding/truncation convention not stated. 704/27 ≈26.07, displayed as 26. Record the exact rounding inputs; no conclusion is assigned without an explicit protocol rounding rule.


## N062 — Phase 3 flow reconciliation including pilot

- **Mapper-local relationship:** B-N019
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Locations:** DOC-002 PDF pp. 49-50 and 63 (printed pp. 10-11 and 22), Diagram 1/Phase-3 diagram (`joi250093supp1_prod_1768590553.08963.pdf#page=49`, `#page=50`, `#page=63`).
- **Direct observation:** later Phase-3 diagram covers 1,080 recruitment excluding pilot. Earlier Diagram 1 labels Phase 3 `1,080 + 16 (pilot) = 1,096`.
- **Source-grounded rule:** values reconcile when pilot inclusion is retained; do not compare 1,080 and 1,096 as the same population without distinguishing pilot inclusion.


## N063 — Phase 4 attrition/design-effect arithmetic and recruitment flow

- **Mapper-local relationship:** B-N020
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp033-064.md`


- **Location:** DOC-002 PDF p. 64 (printed p. 23), lines 1933-1953 (`joi250093supp1_prod_1768590553.08963.pdf#page=64`).
- **Direct observation:** with `20%` attrition, printed `N = 864 + (864*0.2) = 1036`; 36 clusters (`18` each arm), `1036/36 =29`; `DE = 1+0.02(29-1)=1.56`; `ESS = 1036*1.56 = 1620 (45 subjects for each site)`. Diagram reports total Phase-4 recruitment `1620`, `36` sites, Bangladesh `22×45=990`, Pakistan `14×45=630`, A 11 Bangladesh/7 Pakistan and face-to-face B 11 Bangladesh/7 Pakistan, all 45/site.
- **Arithmetic comparison rule:** 864×1.2=1,036.8; 1,036/36≈28.78; 1,036×1.56=1,616.16, while 36×45=1,620. The direct source does not specify rounding conventions for 1,036.8→1,036 or 1,616.16→1,620. Keep the printed values and calculations for later checker review; no conclusion is assigned here.


## N064 — Phase 4 diagram phase-label relationship

- **Mapper-local relationship:** B-N021
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp065-096.md`


- **Location:** DOC-002 PDF p. 64 (printed p. 23), Phase-4 diagram, box beneath total recruitment (`joi250093supp1_prod_1768590553.08963.pdf#page=64`).
- **Direct observation:** the surrounding heading says `Phase 4`, and all immediately preceding text describes Phase 4/non-inferiority/A vs face-to-face. The diagram box nevertheless prints `Total clusters in Phase 3 (Superiority trial) = 36 sites`, followed by `Patients to be recruited =1620`.
- **Source-grounded comparison rule:** the box's Phase-3/Superiority label differs from its local Phase-4/non-inferiority context and from the 36-site allocation details. This is a label-versus-context relationship for later evidence checking; it is not adjudicated here.

## Cross-page links and check-ready observations

1. **Total recruitment:** B-N007's 1,096 Phase-3 including pilot +1,620 Phase-4 equals B-N016's 2,716. However B-N016's `48 health clinics`/approximately `50 recruits` differs from Diagram 1's 63 sites and its displayed per-site recruitment. Population/phase inclusion should be checked before any merge.
2. **Attrition assumptions:** PDF p. 46 high-level sample-size text uses `10%` no primary-outcome data, whereas detailed phase calculations on pp. 62-63 use `20%` attrition. The source does not on these pages state whether one supersedes the other; preserve as a version/internal-protocol relationship.
3. **Pilot:** the 16 pilot participants reconcile in country totals and in the 2,716 total only when Phase-3 1,080 is treated as excluding the pilot. The detailed pilot has 4 facilities, but no contrary facility count for the pilot is stated in Diagram 1.
4. **TAM:** 30% row label, 20% Phase-3 narrative/equations, and all-participant Phase-4 narrative/equations are separate printed quantities. They require later source-based comparison, not a silent normalization.
5. **Rounding/calculation inputs:** preserve p. 62's 704, 26, 1.50, 1,080; and p. 63's 1,036, 29, 1.56, 1,620 exactly. The source supplies formulas but not a rounding convention.

## No candidate/adjudication statement

This mapping does not diagnose a candidate, assign a C ID, severity, disposition, or correction. It records direct observations and source-grounded comparison rules for the later numeric/statistical/cross-source stages.
# Fresh support quantitative evidence map — DOC-002 PDF pp. 65–96

## Scope and method

Direct source: `joi250093supp1_prod_1768590553.08963.pdf`, PDF pp. 65–96.  All 32 assigned pages were visually inspected from the current-run 180-dpi JPEG derivatives in `review_1_5_1/preprocessing/DOC-002/page_images/`; the direct PDF is the authority.  Fresh native/layout text was not relied on because this PDF's font encoding is garbled.  Tesseract was not used because the supplied workflow record reports it nonresponsive.

This is a relationship inventory and an observation log, not an adjudication.  Local IDs beginning `C-N` and `C-S` are only shard-local handles; they are not stable candidate IDs and every item remains pending human review by the coordinator.

## Per-page coverage

| PDF page | Printed page | Coverage result |
|---:|---:|---|
| 65 | 24 | Sample-size assumptions for phases 3/4; cost-effectiveness analysis plan, including 5,000 bootstrap replications. |
| 66 | 25 | Cost-effectiveness and primary statistical-model plan (GLMM, log link, Poisson, cluster random effect; crude/adjusted RRs and 95% CIs). |
| 67 | 26 | Translation and adverse-event administrative text; no result-relevant quantitative relationship. |
| 68 | 27 | Oversight membership text; no result-relevant quantitative relationship. |
| 69 | 28 | Ethics/consent administrative text; no result-relevant quantitative relationship. |
| 70 | 29 | Data-protection administrative text; no result-relevant quantitative relationship. |
| 71 | 30 | Protocol-deviation reporting intervals (every 3 months; within 3 days); administrative, not a study result. |
| 72 | 31 | Record retention/end-of-study timelines (3 years, 90/15 days, 1 year); administrative, not a study result. |
| 73 | 32 | Insurance/stakeholder/reporting administrative text; no result-relevant quantitative relationship. |
| 74 | 33 | Publication/contract timelines (5 years, 30 days, 3 months, 1 year); administrative, not a study result. |
| 75 | 34 | References only; no result-relevant relationship. |
| 76 | 35 | References only; no result-relevant relationship. |
| 77 | 1 | Version-change log: revised endpoint wording, phase sample sizes, clusters, and 20% TAM subsample. |
| 78 | 1 | SAP introduction/design: four phases; phase-3 and phase-4 duration and contrast. |
| 79 | 2 | Phase-3 intervention and PPI pilot size (16; 8 per country). |
| 80 | 3 | Intervention dose/schedule (134 SMS in six months) and data-capture population. |
| 81 | 4 | Phase-4 intervention dose/timing and primary-objective endpoint duration. |
| 82 | 5 | Randomization ratio; country burden table; phase-3/4 sample-size calculations. |
| 83 | 7 | Primary outcome definition/thresholds and TB secondary-outcome definitions. |
| 84 | 8 | MPSS and SUTS scale definitions/ranges; AE collection through week 9. |
| 85 | 9 | Assessment schedule table (screening, baseline, week 9, six months). |
| 86 | 10 | Blank continuation of schedule; no additional quantitative relationship. |
| 87 | 11 | Dataset timepoints: baseline, week 9, month 6; no reported results. |
| 88 | 12 | Data-query numbering 1–999 and checking intervals; administrative/data-management only. |
| 89 | 13 | Interim/descriptive analysis plan. |
| 90 | 14 | Primary-outcome analysis plan and adverse-event statistical rule. |
| 91 | 15 | EQ-5D-5L, adjusted, missing-data, and subgroup analysis rules. |
| 92 | 16 | Subgroup contrasts and planned software. |
| 93 | 17 | Blank sociodemographic template table; no observed values. |
| 94 | 18 | Blank tobacco-use template table; no observed values. |
| 95 | 19 | Blank continuation template; no observed values. |
| 96 | 20 | Blank continuation template; no observed values. |

## Numeric and reporting relationships


## N065 — Phase-3 and phase-4 version-change quantities

- **Mapper-local relationship:** C-N001
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp065-096.md`


**Observation.** DOC-002 PDF p. 77 (`#page=77`) says Phase 3 increased from **888 participants**, **16 intervention** and **8 usual-care clusters** (v4) to **1,080 participants**, **18 intervention** and **9 usual-care clusters** (v6).  It says Phase 4 increased from **1,480 participants in 40 clusters** to **1,620 participants in 36 clusters**, and that the combined two-phase sample increased accordingly.  The same page says a Technology Assessment Model (TAM) substudy selects **20%** of phase-3 mTB-Tobacco participants in each country, whereas all phase-4 mTB-Tobacco participants are asked to complete TAM.

**Matching keys.** Version 6; Phase 3 superiority, mTB-Tobacco versus usual care; Phase 4 non-inferiority, mTB-Tobacco versus face-to-face; participant and cluster totals.

**Source-grounded checks.** Phase totals reconcile with the later SAP overall total: 1,080 + 1,620 = 2,700 (p. 82).  Cluster counts reconcile: 27 Phase-3 centers plus 36 Phase-4 centers = 63 total centers (p. 82).  The allocation detail differs across phases and must not be compared as a common three-arm allocation.


## N066 — Phase-3 intervention-pilot and message dose

- **Mapper-local relationship:** C-N002
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp065-096.md`


**Observation.** On p. 79 (`#page=79`), the pilot embedded in Phase 3 has **16 patients**, **8 each in Bangladesh and Pakistan**.  On p. 80 (`#page=80`), each intervention participant is to receive **134 SMS messages over 6 months**: first month **3–4/day**, next month **1/day**, and last four months **1/month**.

**Rule/check.** The qualitative frequency description permits a 134-message total: months 2–6 contribute about 34 messages, leaving 100 messages for month 1, which lies between 3 and 4 messages/day over a 30-day month.  Exact calendar-day and scheduling rules are not specified, so this is not a contradiction.


## N067 — Phase-4 session dose and objective time horizon

- **Mapper-local relationship:** C-N003
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp065-096.md`


**Observation.** On p. 81 (`#page=81`), Phase-4 face-to-face support has two sessions at **day 0** and **day 5 (+2)**, lasting **10** and **5 minutes**, respectively; further support can occur at **week 5**.  The primary objective is continuous abstinence for a minimum of **six months**.  These are intervention/endpoint definitions, not reported outcome values.


## N068 — Country-burden table

- **Mapper-local relationship:** C-N004
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp065-096.md`


**Observation.** DOC-002 p. 82 (`#page=82`) reports: Bangladesh TB **221 per 100,000**, **357,000** cases, **47,000** deaths, tobacco prevalence **35%**; Pakistan TB **265 per 100,000**, **562,000** cases, **44,000** deaths, tobacco prevalence **20%**.  The preceding prose repeats case/death/prevalence values exactly.  No denominator for the absolute annual country case/death counts is supplied on this page, so they are not arithmetic-comparable to the incidence column.


## N069 — Total sample and cluster allocation

- **Mapper-local relationship:** C-N005
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp065-096.md`


**Observation.** DOC-002 p. 82 says the study requires **2,700** smokers newly diagnosed with pulmonary TB, approximately **43 recruits from 63 TB centres**, assuming **20%** might not provide primary-outcome data.  It includes the first **16** pilot participants.  It specifies a cluster randomization ratio **2:2:1** for mTB-Tobacco (A), face-to-face (B), and standard care (control), but its phase-specific descriptions are two-arm comparisons.

**Rule/check.** The stated approximate center average is compatible with 2,700/63 = 42.86.  The total 2,700 equals 1,080 + 1,620 as above.  The protocol does not state a single three-arm allocation for the entire pooled 2,700; the 2:2:1 statement requires phase/context matching before any cross-document comparison.


## N070 — Phase-3 design-effect arithmetic observation

- **Mapper-local relationship:** C-N006
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp065-096.md`


**Observation.** DOC-002 p. 82 states Phase 3 has **90% power**, **5%** significance, expected 6-month abstinence **18%** for mTB-Tobacco and **8%** for normal treatment, **27** centers at **2:1** intervention:control, **20%** attrition, and a sample size **704**, around **26** individuals/cluster.  It then states ICC = **0.02**, design effect = **1.50**, and “This results in an effective sample size of around **1,080** people (or **40 subjects per site**).”

**Direct observation.** The printed 27 sites × 40 subjects/site = 1,080; and 27 × about 26 = about 702, close to the stated 704 after rounding.

**Derived diagnostic reasoning.** If the displayed design effect is applied multiplicatively to the displayed 704-person figure, 704 × 1.50 = **1,056**, not 1,080.  Conversely, 1,080/704 = **1.5341**, not 1.50.  The 24-person difference cannot be explained by the printed integer figures alone.

**Local candidate flag: C-N006.** This is a source-grounded numeric/arithmetic observation, not an adjudication.  The coordinator should check whether 704 is a rounded uninflated individual-level requirement while 1,080 is a cluster-rounded recruitment target, and whether “effective sample size” was intended to mean design-effect-inflated rather than information-equivalent sample size.  No other source in this shard supplies that missing calculation convention.


## N071 — Phase-4 non-inferiority planning quantities

- **Mapper-local relationship:** C-N007
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp065-096.md`


**Observation.** DOC-002 pp. 82–83 states Phase 4 has **90%** power, a **one-sided 2.5%** significance level, **18 clusters per arm**, assumed 6-month face-to-face abstinence **18%**, a non-inferiority margin **8%**, natural cessation **2%**, an established effect **16% (18% − 2%)**, ICC **0.02**, design effect **1.50**, **1,620** participants / **45** per site, and preservation **50% (8/16)**.

**Rule/check.** The printed arithmetic 18% − 2% = 16% and 8/16 = 50% reconciles.  Thirty-six clusters × 45/site = 1,620.  No uninflated phase-4 participant requirement is printed, so its stated design effect cannot be independently multiplied here.


## N072 — Primary endpoint thresholds and scale

- **Mapper-local relationship:** C-N008
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp065-096.md`


**Observation.** DOC-002 p. 83 defines the primary endpoint as biochemically verified continuous abstinence at **6 months post-randomization**.  Abstinence is self-report of no more than **5** cigarettes/bidis/water-pipe sessions since quit date, verified by breath CO **<10 ppm** at month 6.  For concomitant smokeless tobacco, cotinine-strip level **0–6** is used and level **<3** (said equivalent to **100–200 ng/mL** cotinine) is tobacco abstinence.  A self-report with CO **>10 ppm**, or corresponding active-use cotinine, is classified tobacco use.

**Matching keys.** Primary abstinence; month 6; CO/cotinine verification; continuous rather than point-prevalence outcome.  No observed event counts or effects appear on this page.


## N073 — Outcome scales and assessment schedule

- **Mapper-local relationship:** C-N009
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp065-096.md`


**Observation.** DOC-002 p. 84 says MPSS has **five** domains rated on a **5-point** scale and summed **5–35**; SUTS ranges **0** (no urges) to **5** (extremely strong urges).  The assessment table on p. 85 places eligibility and consent at screening; sociodemographics and tobacco history at baseline; self-reported abstinence and CO/cotinine at 6 months; MPSS, nicotine dependency, and EQ-5D-5L at baseline/6 months; TB outcomes at baseline/week 9/6 months; adherence, sputum microscopy, and AE review at week 9/6 months; and mTB usage at week 9.

**Rule/check.** Five 1–5 item scores produce a 5–25 sum, not the printed 5–35 range, if “five domains” means one item per domain with no additional scoring components.  The page supplies no item count/subscale construction beyond the visible text.  This is an unresolved scale-definition issue, so it is retained as a local observation, not a candidate conclusion.

**Local candidate flag: C-N009.** Exact human question: does the intended MPSS instrument contain additional items or a non-unit scoring rule that makes the stated 5–35 total valid?  The supplied pp. 65–96 do not state one.

## Statistical relationships and definitions


## N074 — CRF baseline/template variables

- **Mapper-local relationship:** D-N001
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-002 PDF p. 97.
- **Direct observation:** The uncompleted form includes `Attempted to quit in the past`, `Smoking duration`, `Age starting`, and `Strength of Urges To Smoke (SUTS)`. The visible site identifiers are 3000 through 3007. The SUTS columns specify group, n, median (IQR), mean (SD), z value, and P value, but contain no filled values.
- **Matching/main-paper key:** baseline smoking history and SUTS variables; this page supplies only a planned data-collection/display schema.
- **Rule/interpretation boundary:** blank fields are not zero observations and are not inferential results.


## N075 — Primary-outcome and subgroup template definitions

- **Mapper-local relationship:** D-N002
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-002 PDF pp. 98-99.
- **Direct observation:** The blank mixed-model template labels self-reported abstinence at 9 weeks, self-reported last-7-days abstinence, CO and cotinine test, and CO/cotinine ITT, with columns `n/N(%)`, proportion (95% CI), RR (95% CI), adjusted RR (95% CI), and ICC. The continuation lists subgroup categories: age <40/>40, education, occupation, gender, and smoking duration <24/>24 years. No cell is completed.
- **Matching/main-paper key:** abstinence outcomes, RR/adjusted RR/ICC and subgroup analysis.
- **Rule/interpretation boundary:** these are planned labels only; no numerical estimate may be inferred from a blank template.


## N076 — Definitions relevant to matching

- **Mapper-local relationship:** D-N003
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-002 PDF p. 100.
- **Direct observation:** Glossary defines cRCT as cluster randomized controlled trial; CI as confidence interval; CO as carbon monoxide; ICC as intraclass correlation coefficient; IQR as interquartile range; ITT as intention to treat; RR as relative risk; SAP as statistical analysis plan; SMS as short message service; SUTS as strength of urges to smoke; TB as tuberculosis; and ppm as parts per million.
- **Matching/main-paper key:** defines the scale/measure labels used in DOC-003 eTables 3, 8, and 9.


## N077 — Intervention-message schedule and displayed quantity

- **Mapper-local relationship:** D-N004
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-002 PDF pp. 101-109.
- **Direct observation:** The log numbers messages 1-134 and prints a character count and scheduled timing for each. It states participants receive up to 5 text messages every day (message 3), begins the intervention at `Q(-8), Tx(+1)`, marks the quit date as `Q` / Tx(+8), and includes follow-up messages at Q(+52)/Tx(+61), Q(+112)/Tx(+121), and Q(+180)/Tx(+189). Selected explicit numeric claims include `6 months` regular treatment (message 18), `30%` lung-capacity increase after a few weeks without smoking (message 98), 10 deep breaths (message 118), 1.5 months (message 123), and two/four/six-month TB-treatment milestones (messages 132-134). Character counts range from 54 (message 74) to 163 (messages 4, 18, and 27) among visible entries.
- **Matching/main-paper key:** intervention dose/schedule and TB-treatment timepoints; not an outcome dataset.
- **Rule/interpretation boundary:** the message claims are protocol content. They do not report trial estimates, denominators, or tested effects.

## DOC-003 quantitative evidence


## N078 — Screening and ineligibility accounting

- **Mapper-local relationship:** D-N005
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-003 PDF p. 3, eTable 1.
- **Direct observation:** Total screenings 9,232; eligible 1,086; ineligible 8,146; consent not given 6 (3 not willing to follow procedures and 3 not willing to participate). Listed ineligibility reasons: age <15 years 385; not diagnosed with pulmonary TB 2,783; diagnosis not within last 4 weeks 1,820; not current smoker (defined as not smoking at least 25 days in the past month) 7,069; not willing to quit 273; no mobile phone 1,290; cannot read SMS/no household reader 236.
- **Rule available for later checking:** 1,086 + 8,146 = 9,232. The printed reason categories are not explicitly stated to be mutually exclusive; do not sum them as though they are.


## N079 — Prior quit attempts by cluster

- **Mapper-local relationship:** D-N006
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-003 PDF p. 4, eTable 2.
- **Direct observation:** Each of the 27 cluster rows has Yes plus No = 40 and percentages summing to 100.0. mHealth Yes counts (site: count [%]): 1002 13 [32.5], 1003 0 [0.0], 1005 7 [17.5], 1006 0 [0.0], 1007 23 [57.5], 1008 9 [22.5], 1011 16 [40.0], 1012 11 [27.5], 1013 1 [2.5], 1015 4 [10.0], 2001 9 [22.5], 2003 11 [27.5], 2005 19 [47.5], 2006 18 [45.0], 2007 5 [12.5], 2009 6 [15.0], 2010 16 [40.0]. Usual-care Yes counts: 1001 10 [25.0], 1004 1 [2.5], 1009 0 [0.0], 1010 0 [0.0], 1014 5 [12.5], 2002 3 [7.5], 2004 0 [0.0], 2008 4 [10.0], 2011 10 [25.0]. The paired No counts are the printed complement to 40 in each row.
- **Matching/main-paper key:** baseline quit-attempt distribution by randomized cluster.


## N080 — TB-treatment adherence by month

- **Mapper-local relationship:** D-N007
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-003 PDF p. 5, eTable 3.
- **Direct observation:** For months 1-6, respectively, mHealth median(IQR) is 30(30-30) each month; mean(SD) is 29.87(1.345), 29.59(2.757), 29.39(3.894), 29(5.092), 28.56(6.049), 27.88(7.397). Control median(IQR) is 30(30-30) each month; mean(SD) is 29.9(0.2), 29.8(0.6), 29.7(2.3), 29.5(3.3), 29.5(3.3), 29.3(3.9). Total: mHealth 180(180-180), 174.3(21.501); control 180(180-180), 178.0(12.1).
- **Statistical observation (D-S001):** Printed z/P pairs for month 1 through total are -0.86/0.388, 0.44/0.656, 1.64/0.101, 0.44/0.657, 0.95/0.34, 1.85/0.064, and 1.19/0.232. Test name, sidedness, and population denominators are not printed on this page.
- **Matching/main-paper key:** secondary outcome, TB-treatment adherence over months 1-6.


## N081 — Death causes by arm

- **Mapper-local relationship:** D-N008
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-003 PDF p. 6, eTable 4.
- **Direct observation:** Total deaths: overall 52, mHealth 25, usual care 27. Causes overall/mHealth/usual care: TB 32 (61.5%)/16 (64.0%)/16 (59.2%); cancer 3 (5.7%)/0/3 (11.1%); heart attack 8 (15.2%)/5 (20.0%)/3 (11.1%); fall/fever 2 (3.8%)/1 (4.0%)/1 (3.7%); stroke 2 (3.8%)/0/2 (7.4%); liver failure 2 (3.8%)/2 (8.0%)/0; drug user 1 (1.9%)/0/1 (7.4%); HIV/AIDS comorbidity 1 (1.9%)/1 (4.0%)/0; severe pneumonia 1 (1.9%)/0/1 (7.4%).
- **Rule available for later checking:** arm counts add to the overall count by cause and death totals 25 + 27 = 52.


## N082 — Kaplan-Meier survival display

- **Mapper-local relationship:** D-N009
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-003 PDF p. 7, eFigure/Figure S1.
- **Direct observation:** The figure labels time as number of days (0-200 shown) and survival probability (0.80-1.00 labelled). It displays Control and Intervention curves with shaded confidence bands; at approximately day 180, the plotted Control curve is about 0.93 and Intervention about 0.96. No exact event counts, model statistic, CI values, or P value are printed.
- **Matching/main-paper key:** survival/death outcome by trial group. Approximate axis reading is descriptive only, not an exact numeric comparator.


## N083 — Cluster recruitment and abstinence rates

- **Mapper-local relationship:** D-N010
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-003 PDF p. 8, eTable 5.
- **Direct observation:** Twenty-seven site rows each report recruitment `40/N (%)`, self-reported quitter at 6-month follow-up, verified quitter at 6-month follow-up, and 6-month ITT quitter. Every ITT denominator is 40. The table contains all cluster-level values, including: control 1001 4/40 (10) ITT; mHealth 1002 17/40 (42.5), 1003 35/40 (87.5), 1005 25/40 (62.5), 1011 29/40 (72.5), 2009 26/40 (65), and 2012 20/40 (50); controls 1004 7/40 (17.5), 1009 5/40 (12.5), 1010 9/40 (22.5), 1014 7/40 (17.5), 2002 6/40 (15), 2004 0/40 (0), 2008 12/40 (30), 2011 5/40 (12.5). Other printed mHealth ITT counts are: 1006 5, 1007 7, 1008 10, 1012 23, 1013 16, 1015 22, 2001 5, 2003 16, 2005 6, 2006 11, 2007 12, 2010 15 (all /40; printed percentages 12.5, 17.5, 25, 57.5, 40, 55, 12.5, 40, 15, 27.5, 30, 37.5 respectively).
- **Rule available for later checking:** each printed n/N percentage may be checked against its printed numerator and denominator, allowing stated display precision; self-reported and verified outcomes are distinct measures with denominators that may be below 40.


## N084 — Cluster-wise deaths

- **Mapper-local relationship:** D-N011
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-003 PDF p. 9, eTable 6.
- **Direct observation:** Death n(%) by cluster: 1001 1(2.5), 1002 0, 1003 0, 1004 0, 1005 2(5.0), 1006 0, 1007 0, 1008 0, 1009 4(10.0), 1010 2(5.0), 1011 1(2.5), 1012 1(2.5), 1013 4(10.0), 1014 2(5.0), 1015 0, 2001 0, 2002 3(7.5), 2003 2(5.0), 2004 4(10.0), 2005 3(7.5), 2006 1(2.5), 2007 3(7.5), 2008 5(7.5), 2009 0, 2010 3(7.5), 2011 6(15.0), 2012 5(12.5). Arm labels are printed with each row.
- **Matching/main-paper key:** death outcome by cluster; the denominator is not explicitly repeated on this page, though eTable 5 records 40 recruited for each cluster.
- **Rule available for later checking:** only after confirming a common denominator and population across tables, a printed percentage can be compared with its count.


## N085 — Cluster characteristics and unadjusted relative risks

- **Mapper-local relationship:** D-N012
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-003 PDF pp. 10-11, eTable 7.
- **Direct observation:** The 27 site rows provide age mean(SD), male n(%), smoking-duration mean(SD) in years, education categories (no formal, primary, middle, higher) and occupation (employed, dependent, retired). Each row is a cluster, usually n=40; exceptions visibly include site 1015 male 39(97.5), 2003 male 38(95), 2004 male 34(85), 2005 male 39(97.5), 2006 male 38(95), 2007 male 33(82.5), 2008 male 32(80), 2009 male 35(87.5), 2010 male 36(90), and 2011 male 39(97.5). Exact row values are on the cited two pages.
- **Statistical observation (D-S002):** Printed unadjusted relative risks (95% CI), in the order of displayed characteristics, are age 1.03 (1.01-1.04), male 0.83 (0.34-2.02), smoking duration 0.97 (0.95-0.99), education no-formal 1 [reference], primary 1.32 (0.88-1.97), middle 1.91 (1.16-3.15), higher 1.86 (1.16-2.99), occupation employed 1 [reference], dependent 2.01 (1.30-3.09), retired 1.00 (0.43-2.31).
- **Matching/main-paper key:** cluster-level characteristics, reference categories, and unadjusted relative-risk analysis.


## N086 — Subgroup analysis of verified 6-month abstinence

- **Mapper-local relationship:** D-N013
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-003 PDF p. 12, eTable 8.
- **Direct observation / statistical observation:** Unadjusted RR (95% CI) for verified abstinence at month 6: all 2.890 (1.983-4.709); age <40 2.672 (1.472-4.857), >=40 2.953 (2.048-5.092); no formal education 2.880 (1.566-5.542), primary years 1-5 2.638 (1.849-4.07), secondary or above >=6 years 2.719 (1.348-4.83); active job/business 2.989 (1.933-4.885), dependent/retired 2.587 (1.329-3.986); smoking duration <24 years 3.511 (1.884-7.127), >=24 years 2.446 (1.550-3.911); reading SMS yes 2.769 (1.743-4.318), no 2.198 (1.288-3.299).
- **Matching/main-paper key:** verified abstinence at 6 months; effect measure explicitly labelled RR and 95% CI.


## N087 — Post-hoc ITT sensitivity analysis excluding deaths

- **Mapper-local relationship:** D-N014
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-003 PDF pp. 13-14, eTable 9.
- **Direct observation:** Population denominators after exclusion of deaths are mHealth 695 and usual care 333. For biochemically verified abstinence at month 6, <10 ppm: 300/695, 43.2% (39.4-46.9) vs 55/333, 16.5% (12.7-20.9); absolute difference 26.7 (21.2-32.1); crude RR 2.9 (1.8-6.4), crude ICC 0.18; adjusted RR 3.1 (1.9-6.5), adjusted ICC 0.18. For <6 ppm: 264/695, 38.0% (34.4-41.7) vs 38/333, 11.4% (8.2-15.3); difference 26.6 (21.6-31.5); crude RR 3.6 (2.4-5.4), ICC 0.17; adjusted RR 3.8 (2.4-6.2), ICC 0.18.
- **Direct observation, continued:** Week-9 point abstinence: 353/695, 50.8% (47.0-54.6) vs 75/333, 22.5% (18.1-27.4); difference 28.3 (22.4-34.1); crude RR 2.5 (1.7-3.6), ICC 0.20; adjusted RR 2.6 (1.7-3.8), ICC 0.20. Month-6 point abstinence: 400/695, 57.5% (53.8-61.2) vs 82/333, 24.6% (20.1-29.6); difference 32.9 (27.0-38.8); crude RR 2.58 (1.8-3.6), ICC 0.20; adjusted RR 2.7 (1.8-4.0), ICC 0.20. Successful TB treatment: 643/695, 92.5% (90.3-94.4) vs 308/333, 92.5% (89.1-95.1); difference 0 (-3.4-3.5); crude RR 1.1 (0.7-1.6), ICC 0.25; adjusted RR 1.1 (0.7-1.5), ICC 0.23. Defaulted: 22/695, 3.2% (2.0-4.8) vs 7/333, 2.1% (0.8-4.3); difference 1.1 (-1.0-3.1); RRs/ICCs not printed. Treatment failures: 1/695, 0.1% (0.01-0.8) vs 2/333, 0.6% (0.1-2.2); difference 0.5 (-0.4-1.3); RRs/ICCs not printed.
- **Definitions (p. 14):** a=numerator/total group number; b=absolute difference; c=relative risk; d=intraclass correlation coefficient; e=adjusted for age, sex, education, occupation, smoking duration, accounting for clustering and mixed-effects models for RR; f=carbon-monoxide breath-test cutoff values.
- **Matching/main-paper key:** post-hoc sensitivity analysis, ITT population after deaths excluded; distinctions between crude/adjusted RR and ICC are explicit.


## N088 — Adverse events

- **Mapper-local relationship:** D-N015
- **Source map:** `.ai_paper_validation/review_1_5_1/parts/support_evidence_DOC-002_pp097-109_DOC-003_pp001-016.md`


- **Location:** DOC-003 PDF pp. 15-16, eTable 10.
- **Direct observation:** Each event has none/mild/moderate/severe categories reported as mHealth n(%) and control n(%). Group category counts sum to 699 mHealth and 334 control for nausea, diarrhoea, dry mouth, epigastric pain, headache, insomnia, abnormal dreams, irritability, anxiety, palpitations, and musculoskeletal pain.
- **Statistical observation (D-S005):** Printed X2/P pairs: nausea 6.5 with 0.084 (exact-test superscript); diarrhoea 1.0 with 0.825 (exact); dry mouth 31.2 with <.001; epigastric pain 18.2 with <.001 (exact); headache 2.7 with 0.426; insomnia 6.9 with 0.072; abnormal dreams 3.8 with 0.255 (exact); irritability 18.5 with <.001; anxiety 17.1 with <.001; palpitations 5.2 with 0.154 (exact); musculoskeletal pain 8.8 with 0.031. Page 16 defines superscript a as based on Exact test.
- **Matching/main-paper key:** adverse-event outcomes by study arm. The `<.001` presentations are threshold displays, not literal-zero P values.

## Source-linked observations reserved for downstream checking

These statements do not diagnose or adjudicate any candidate.

1. **D-N011:** eTable 6 prints site 2008 as 5 deaths (7.5%). eTable 5 prints 40 recruited at every cluster, including 2008. Any comparison must first confirm that both figures use the same analysis population and denominator; if they do, `5/40` is a relevant arithmetic relationship for a later independent checker.
2. **D-N010/D-N011/D-N014/D-N015:** Denominators vary by outcome and timepoint (cluster recruited n=40; some observed follow-up denominators <40; sensitivity denominators 695/333; adverse-event denominators 699/334). They must not be substituted for one another without a printed population/time match.
3. **D-S001/D-S005:** Test names and detailed test conventions are incompletely provided for some z/P and X2/P pairs. Later statistical review should use only the stated definitions, including the exact-test footnote, and should not infer a test model from the printed summaries alone.

## Limitations

DOC-002 pp. 97-109 contain blank CRF/template material and an intervention SMS log rather than completed trial results; no numerical outcome can be extracted from a blank field. DOC-003 eFigure p. 7 has no printed exact survival estimates or test output, so its values are only qualitative/axis-based. All DOC-003 table values above were confirmed visually against the direct page image; the normalized text was used only to assist exhaustive transcription.

## Inventory count

- **Numeric/reporting relationships:** 88.
