# Numeric Consistency Review

## Scope and method

This review covers all 59 stable numeric/reporting relationships (`N001` through `N059`) in `relationships/numeric_relationship_inventory.md`. It used the two cited relationship parts and the main/support quantitative evidence maps as locators and transcription aids. Direct PDF confirmation was performed for the main outcome table and for eTable 2, including a rendered visual check of Supplement 2 PDF page 4. No old candidate, checker, verifier, critic, quality, or report artifact was read.

Checks applied where the printed inputs permitted them: count and subgroup totals; numerator/denominator percentages; rounding; flow and population identities; missing-data denominators; matched main/supplement values; absolute differences; units, labels, scales, and reference direction; rate/count/proportion distinctions; and duplicate/repeated-result checks. A percentage printed to a whole percent was treated as reconciling when the exact percentage rounds to that integer (tolerance: 0.5 percentage point, subject to ordinary half-rounding convention). A one-decimal absolute difference was treated as reconciling within 0.05 percentage point.

## Results summary

- Relationships checked: 59.
- Relationships with one or more qualifying candidate observations: 2 (`N011`, `N050`).
- Distinct provisional checker candidates: 3.
- Relationships with no qualifying candidate: 57.
- Candidate status: all observations below are pending human adjudication; this checker assigns no stable `C` ID, severity, validity, or disposition.

## Per-relationship coverage record

| Stable ID | Numeric consistency checks completed | Exact checked source location(s) | Result |
|---|---|---|---|
| N001 | Allocation and analysis identity: 306 + 342 = 648 randomized; 302 + 339 = 641 analyzed; 219/641 = 34.2%, consistent with 34% whole-percent display. | `jama_thille_2019_oi_190108.pdf#page=1`, pp. 3-4 | NO_CANDIDATE |
| N002 | Every displayed Figure 1 exclusion subtotal reconciles: 927+414+101+18=1460; 3121-1460=1661; 274+182+119+41+39+37=692; 1661-692=969; 270+51=321; 969-321=648; arm decrements give 302 and 339. | `jama_thille_2019_oi_190108.pdf#page=3` | NO_CANDIDATE |
| N003 | Treatment-flow, duration, pressure, volume, oxygen, and time-unit labels are internally coherent; no result-level arithmetic comparator is printed. | `jama_thille_2019_oi_190108.pdf#page=2`, `jama_thille_2019_oi_190108.pdf#page=3`, pp. 6-7 | NO_CANDIDATE |
| N004 | Day-7, 48-hour, 72-hour, ICU-discharge, and mortality windows are distinct and consistently labelled; respiratory-failure and reintubation thresholds are not conflated. | `jama_thille_2019_oi_190108.pdf#page=4` | NO_CANDIDATE |
| N005 | Planned sample-size arithmetic: 590 x 1.10 = 649, displayed as target 650 after whole-person rounding; planned 18% versus 10% is an 8-point difference. | `jama_thille_2019_oi_190108.pdf#page=4` | NO_CANDIDATE |
| N006 | Sex, intubation-reason, weaning, ventilation-mode, and breathing-trial mutually exclusive rows sum to 302 and 339. Chronic-disease subrows are explicitly nonexclusive. | `jama_thille_2019_oi_190108.pdf#page=5`, `jama_thille_2019_oi_190108.pdf#page=6` | NO_CANDIDATE |
| N007 | Continuous-value measure labels and units are coherent; no invalid sum was applied to means, SDs, medians, or IQRs. | `jama_thille_2019_oi_190108.pdf#page=5`, `jama_thille_2019_oi_190108.pdf#page=6` | NO_CANDIDATE |
| N008 | Available-case labels are explicit. PaO2/pH/PaCO2 share 221/302 and 241/339 available cases; cough and secretion fractions use their printed, distinct denominators. | `jama_thille_2019_oi_190108.pdf#page=6` | NO_CANDIDATE |
| N009 | 87/302=28.8% and 126/339=37.2%, reconciling with 29% and 37%; baseline-imbalance label and adjustment context do not conflict. | `jama_thille_2019_oi_190108.pdf#page=5`, `jama_thille_2019_oi_190108.pdf#page=6`, pp. 4, 7 | NO_CANDIDATE |
| N010 | Primary counts yield 55/302=18.21%, 40/339=11.80%, and NIV minus HFNO = -6.41 points, reconciling with -6.4. Abstract, Key Points, narrative, Figure 2, and Table 2 are matched by population/time/contrast. | `jama_thille_2019_oi_190108.pdf#page=1`, pp. 2, 6-8 | NO_CANDIDATE |
| N011 | Day-7 respiratory-failure counts/percentages and the repeated absolute-difference statement were checked. One direct cross-location discrepancy is recorded as `NUM-CAND-001`. | `jama_thille_2019_oi_190108.pdf#page=1`, pp. 6, 8 | CANDIDATE_RECORDED: NUM-CAND-001 |
| N012 | All reintubation time-window counts yield the displayed rounded percentages and absolute differences; windows are nested rather than mutually exclusive, as their labels indicate. | `jama_thille_2019_oi_190108.pdf#page=8` | NO_CANDIDATE |
| N013 | ICU and hospital median/IQR outcomes retain day units and direction of displayed median differences; medians/IQRs were not inappropriately summed. | `jama_thille_2019_oi_190108.pdf#page=8` | NO_CANDIDATE |
| N014 | Mortality counts yield displayed rounded percentages and absolute differences: ICU -2.4, hospital +0.7, day 28 +0.6, day 90 -3.2 points. | `jama_thille_2019_oi_190108.pdf#page=1`, `jama_thille_2019_oi_190108.pdf#page=8` | NO_CANDIDATE |
| N015 | Exploratory numerator/denominator relationships reconcile, including 21/59=36%, 11/41=27%, and their displayed -8.8-point difference. | `jama_thille_2019_oi_190108.pdf#page=8` | NO_CANDIDATE |
| N016 | PaO2:FiO2 retains mm Hg scale; hypercapnia is a proportion; time-to-reintubation retains hours. Printed differences have consistent direction and units. | `jama_thille_2019_oi_190108.pdf#page=7` | NO_CANDIDATE |
| N017 | 39+57=96 of 100 reintubations, matching narrative 96%; 12/28=42.9%, reconciling with 43%. Reason/criterion component rows are not summed because overlap is stated or inherent in the criteria. | `jama_thille_2019_oi_190108.pdf#page=7`, `joi190108supp2_prod.pdf#page=2` | NO_CANDIDATE |
| N018 | 106/302=35.10%, 86/339=25.37%, and NIV minus HFNO=-9.73 points reconcile with 35%, 25%, and -9.7. | `jama_thille_2019_oi_190108.pdf#page=7` | NO_CANDIDATE |
| N019 | PaCO2 strata partition the analysis set: 48+63=111; 254+276=530; 111+530=641. Subgroup day-7 counts sum to the primary counts. | `jama_thille_2019_oi_190108.pdf#page=6`, pp. 7-8; `joi190108supp2_prod.pdf#page=3`, pp. 6-7 | NO_CANDIDATE |
| N020 | At-risk sets begin at their arm denominators and decrease monotonically; they are not event-count totals. Figure time label is days and matches correction-note context in the supplied current version. | `jama_thille_2019_oi_190108.pdf#page=7`, `jama_thille_2019_oi_190108.pdf#page=8` | NO_CANDIDATE |
| N021 | Adjusted OR 0.60 has an ordered CI containing the estimate; reference group, covariates, and hospital random-effect comparison are labelled without numeric contradiction. | `jama_thille_2019_oi_190108.pdf#page=4`, `jama_thille_2019_oi_190108.pdf#page=7` | NO_CANDIDATE |
| N022 | Correction notice is provenance context, not a current competing numeric result. No pre-correction source is supplied for a matched numeric comparison. | `jama_thille_2019_oi_190108.pdf#page=9` | NO_CANDIDATE |
| N023 | Disclosures/group information/references contain no applicable result relationship. | `jama_thille_2019_oi_190108.pdf#page=10`, `jama_thille_2019_oi_190108.pdf#page=11` | NO_CANDIDATE |
| N024 | Trial contrast, 1:1 allocation, center and PaCO2 stratification agree with the main article. | `joi190108supp1_prod.pdf#page=28`, pp. 29-30 | NO_CANDIDATE |
| N025 | Protocol primary outcome uses the same planned-extubation/day-7 population and time window as the main result. | `joi190108supp1_prod.pdf#page=9`, pp. 25, 33 | NO_CANDIDATE |
| N026 | Secondary windows and measure labels are distinct; no protocol/result mismatch after matching the defined outcome and time point. | `joi190108supp1_prod.pdf#page=9`, pp. 10, 25 | NO_CANDIDATE |
| N027 | Protocol p. 11 decomposes 51 months as 39 study months plus 12 analysis months, with 36 months' inclusion and 3 months' participant follow-up. Protocol p. 32 prints 51 months while naming only 36 study months plus 12 analysis months; 36+12=48. | `joi190108supp1_prod.pdf#page=11`, `joi190108supp1_prod.pdf#page=32` | CANDIDATE — C006 (coordinator quality-audit repair) |
| N028 | Eligibility thresholds retain their stated units and inequalities; they do not conflict with the separately defined analysis population. | `joi190108supp1_prod.pdf#page=10`, pp. 11, 26 | NO_CANDIDATE |
| N029 | Control HFNC dose, duration, saturation target, and weaning-test quantities use consistent units. | `joi190108supp1_prod.pdf#page=29` | NO_CANDIDATE |
| N030 | NIV-session, pressure, tidal-volume, PEEP, flow, ramp, and cycling scales are internally coherent and match the intervention definition. | `joi190108supp1_prod.pdf#page=30` | NO_CANDIDATE |
| N031 | ARF continuation criteria and reintubation criteria have deliberately different RR, FiO2, and PaO2:FiO2 thresholds; labels prevent rate/criterion conflation. | `joi190108supp1_prod.pdf#page=30` | NO_CANDIDATE |
| N032 | Weaning-screen and poor-tolerance thresholds were checked as protocol definitions; units and directional inequalities are coherent. | `joi190108supp1_prod.pdf#page=27`, `joi190108supp1_prod.pdf#page=28`, `joi190108supp1_prod.pdf#page=42` | NO_CANDIDATE |
| N033 | Protocol sample-size arithmetic and planned rate contrast match main-method planning values; 590 x 1.10 rounds to 650. | `joi190108supp1_prod.pdf#page=34`, `jama_thille_2019_oi_190108.pdf#page=4` | NO_CANDIDATE |
| N034 | Expected/pilot rates are explicitly prospective or historical and are not treated as competing observed trial estimates. | `joi190108supp1_prod.pdf#page=34`, `joi190108supp1_prod.pdf#page=35` | NO_CANDIDATE |
| N035 | Preliminary cohort 26/168 and subgroup risks are historical rationale; reported percentages have no source-matched current-trial comparator. | `joi190108supp1_prod.pdf#page=19` | NO_CANDIDATE |
| N036 | External RCT table count/percentage pairs reconcile to their printed study denominators under whole-percent rounding; they are not current-trial results. | `joi190108supp1_prod.pdf#page=17` | NO_CANDIDATE |
| N037 | eTable 1 day-7 respiratory-failure and ICU-discharge reintubation counts, percentages, and P values match Table 2 after outcome/time matching. | `joi190108supp2_prod.pdf#page=2`, `jama_thille_2019_oi_190108.pdf#page=8` | NO_CANDIDATE |
| N038 | ARF component fractions use arm denominators 302/339 and reconcile by ordinary rounding; components may overlap and were not summed. | `joi190108supp2_prod.pdf#page=2` | NO_CANDIDATE |
| N039 | Reintubation criteria and severe-respiratory subcriteria are overlapping, not mutually exclusive; printed arm percentages reconcile with 302/339. | `joi190108supp2_prod.pdf#page=2` | NO_CANDIDATE |
| N040 | Reasons may overlap; each displayed count/percentage is compatible with arm denominators. No invalid subgroup sum applied. | `joi190108supp2_prod.pdf#page=2` | NO_CANDIDATE |
| N041 | Subgroup denominators partition the 641 analysis population exactly. | `joi190108supp2_prod.pdf#page=3`, `joi190108supp2_prod.pdf#page=4` | NO_CANDIDATE |
| N042 | Chronic-lung-disease counts and whole-percent displays reconcile with each subgroup denominator; disease subtypes remain nonexclusive where stated. | `joi190108supp2_prod.pdf#page=3` | NO_CANDIDATE |
| N043 | Hypercapnic pre-SBT tidal-volume results retain distinct mL and mL/kg measures; no unit/scale switch or duplicated-result inconsistency. | `joi190108supp2_prod.pdf#page=4` | NO_CANDIDATE |
| N044 | Nonhypercapnic baseline category rows sum to arm denominators where mutually exclusive, and all displayed percentages reconcile under whole-percent rounding. | `joi190108supp2_prod.pdf#page=3` | NO_CANDIDATE |
| N045 | Hypercapnic baseline category rows sum to 48 and 63 where mutually exclusive; percentages and units reconcile. | `joi190108supp2_prod.pdf#page=3` | NO_CANDIDATE |
| N046 | Nonhypercapnic pre-SBT mode rows are complementary (37+217=254; 45+231=276); percentages, units, and duplicate measure labels reconcile. | `joi190108supp2_prod.pdf#page=4` | NO_CANDIDATE |
| N047 | Hypercapnic pre-SBT mode rows are complementary (5+43=48; 4+59=63); percentages, units, and repeated pressure/volume measures reconcile. | `joi190108supp2_prod.pdf#page=4` | NO_CANDIDATE |
| N048 | Nonhypercapnic end-SBT mode rows sum to 254/276. Cough and secretion fractions reconcile with their printed available-case denominators and percentages. | `joi190108supp2_prod.pdf#page=4` | NO_CANDIDATE |
| N049 | Nonhypercapnic end-SBT mode rows sum to 254/276. Cough and secretion fractions reconcile with their printed available-case denominators and percentages. | `joi190108supp2_prod.pdf#page=4` | NO_CANDIDATE |
| N050 | Hypercapnic end-SBT cough and secretion numerator/denominator percentage labels were checked. Two distinct printed-row inconsistencies are recorded as `NUM-CAND-002` and `NUM-CAND-003`; all other values in this relationship reconcile. | `joi190108supp2_prod.pdf#page=4` | CANDIDATES_RECORDED: NUM-CAND-002, NUM-CAND-003 |
| N051 | Hypercapnic day-7 counts yield 10/48=20.8%, 5/63=7.9%, and -12.9 points; main narrative/Figure 3/eTable match with allowable P-value precision. | `joi190108supp2_prod.pdf#page=6`, `jama_thille_2019_oi_190108.pdf#page=7`, `jama_thille_2019_oi_190108.pdf#page=8` | NO_CANDIDATE |
| N052 | Hypercapnic secondary count/percentage pairs and absolute differences reconcile under their 48/63 denominators; nested time windows not summed. | `joi190108supp2_prod.pdf#page=6` | NO_CANDIDATE |
| N053 | Hypercapnic mortality and composite count relationships reconcile; mortality-among-reintubated uses the stated 10 and 6 denominators. | `joi190108supp2_prod.pdf#page=6` | NO_CANDIDATE |
| N054 | Nonhypercapnic day-7 counts yield 45/254=17.7%, 35/276=12.7%, and -5.0 points; matched main narrative is precision-compatible. | `joi190108supp2_prod.pdf#page=7`, `jama_thille_2019_oi_190108.pdf#page=7` | NO_CANDIDATE |
| N055 | Nonhypercapnic secondary count/percentage pairs and differences reconcile under 254/276 denominators; no improper sum of nested outcomes. | `joi190108supp2_prod.pdf#page=7` | NO_CANDIDATE |
| N056 | Nonhypercapnic mortality/composite values reconcile; reintubated-mortality denominators sum to main ICU-discharge reintubation counts. | `joi190108supp2_prod.pdf#page=7` | NO_CANDIDATE |
| N057 | For all 30 centers, arm denominators sum to center totals and arm event counts sum to center events. The printed total reconciles: 95/641, 55/302, 40/339. Center percentages are compatible with whole-percent rounding. | `joi190108supp2_prod.pdf#page=8` | NO_CANDIDATE |
| N058 | Overall survival at-risk sets begin at 302 and 339 and decrease monotonically; these are person-at-risk counts, not survival percentages or event totals. | `joi190108supp2_prod.pdf#page=9` | NO_CANDIDATE |
| N059 | The data-availability statement contains no quantitative trial-result relation to test. | `joi190108supp3_prod.pdf#page=1` | NO_CANDIDATE |

## Candidate observations

### NUM-CAND-001 — Day-7 postextubation respiratory-failure absolute difference differs between the outcome table and repeated narrative results

- **Potential primary category:** Numeric or arithmetic inconsistency.
- **Exact source locations:** [main article PDF p. 1](../../../jama_thille_2019_oi_190108.pdf#page=1), Abstract Secondary Results; [main article PDF p. 6](../../../jama_thille_2019_oi_190108.pdf#page=6), Secondary Outcomes narrative; [main article PDF p. 8](../../../jama_thille_2019_oi_190108.pdf#page=8), Table 2, `Postextubation respiratory failure at day 7`.
- **Printed inputs:** The abstract and p. 6 narrative each state 21% versus 29%, difference `-8.7%` (95% CI, `-15.2% to -1.8%`; `P=.01`). Table 2 reports 88 (29%) for HFNO alone and 70 (21%) for HFNO with NIV, difference `-8.5%` (95% CI, `-15.2% to -1.8%`; `P=.01`).
- **Reproducible rule and calculation:** For the table's named absolute difference in the order NIV minus HFNO: `(70 / 339 - 88 / 302) x 100 = -8.4901` percentage points, which rounds to `-8.5` at one decimal place. The table value is within the 0.05-point one-decimal tolerance. The repeated `-8.7` is 0.2099 points from the exact count-derived difference and is outside that tolerance.
- **Direct observation versus inference:** Direct observation: same outcome, arm percentages, CI, and P value are printed with `-8.7` in two narrative locations and `-8.5` in Table 2. Inference: because the table also supplies numerator/denominator inputs, the table's `-8.5` is compatible with ordinary unadjusted absolute-risk-difference arithmetic; the source does not label the narrative `-8.7` as a differently adjusted or differently defined measure.
- **Alternative source-grounded interpretations:** The narrative value could reflect an undocumented calculation convention, a value copied from an earlier version, or a table/narrative transcription error. The supplied source does not establish which printed value is intended.
- **Quality-control relevance:** A data extractor can reasonably treat the repeated abstract/narrative value as the same unadjusted Table 2 contrast because time point, population, arms, CI, and P value match. A 0.2-point conflict can therefore propagate into extracted effect estimates.
- **Exact human question:** For day-7 postextubation respiratory failure, should the repeated `-8.7%` be interpreted as a distinct adjusted/otherwise calculated contrast, or should it reconcile to the Table 2 count-derived `-8.5%`; if distinct, where is its calculation and label defined?

### NUM-CAND-002 — Hypercapnic eTable 2 ineffective-cough percentages are the complements of the printed numerator/denominator proportions

- **Potential primary category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** [Supplement 2 PDF p. 4](../../../joi190108supp2_prod.pdf#page=4), eTable 2, hypercapnic `Ineffective cough, No./total No. (%)` row; [main article PDF p. 6](../../../jama_thille_2019_oi_190108.pdf#page=6), Table 1, overall ineffective-cough row.
- **Printed inputs:** eTable 2 prints HFNO alone `14/45 (69%)` and HFNO with NIV `16/59 (73%)` under the label `Ineffective cough, No./total No. (%)`. The nonhypercapnic values on the same row are `51/239 (21%)` and `70/263 (27%)`. Main Table 1 prints overall `65/284 (23%)` and `86/322 (27%)`.
- **Reproducible rule and calculation:** `14 / 45 x 100 = 31.1%`, which rounds to 31%, not 69%; `16 / 59 x 100 = 27.1%`, which rounds to 27%, not 73%. The discrepancies are 37.9 and 45.9 points, far beyond the 0.5-point whole-percent tolerance. The printed 69% and 73% equal the complements (68.9% and 72.9%) of the displayed fractions. The counts and denominators themselves reconcile across strata: `51+14=65`, `239+45=284`, `70+16=86`, and `263+59=322`, matching main Table 1's aggregate fractions.
- **Direct observation versus inference:** Direct observation: the eTable row gives each fraction and the incompatible percentage under one label. Inference: the two percentages appear to be complements of their fractions, but the source does not state that the percentage column is an inverse measure or that `Ineffective cough` is labelled inversely.
- **Alternative source-grounded interpretations:** The denominator or numerator might be mislabeled; the percentages might intentionally refer to effective rather than ineffective cough; or the percentage values may be transcribed incorrectly. The row heading and main aggregate row provide no printed basis for an inverse interpretation.
- **Quality-control relevance:** The printed subpopulation percentages can be copied as baseline ineffective-cough prevalences and would reverse the apparent magnitude for both hypercapnic arms if read literally.
- **Exact human question:** In eTable 2's hypercapnic ineffective-cough row, what measure do 69% and 73% denote, and should the displayed `No./total No. (%)` values instead show the ordinary fraction percentages (31% and 27%) or use different labelled numerators/denominators?

### NUM-CAND-003 — Hypercapnic eTable 2 abundant-secretion percentages are the complements of the printed numerator/denominator proportions

- **Potential primary category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** [Supplement 2 PDF p. 4](../../../joi190108supp2_prod.pdf#page=4), eTable 2, hypercapnic `Abundant secretions, No./total No. (%)` row; [main article PDF p. 6](../../../jama_thille_2019_oi_190108.pdf#page=6), Table 1, overall abundant-secretions row.
- **Printed inputs:** eTable 2 prints HFNO alone `20/46 (57%)` and HFNO with NIV `23/61 (62%)` under `Abundant secretions, No./total No. (%)`. The nonhypercapnic row values are `101/242 (42%)` and `91/265 (34%)`. Main Table 1 prints overall `121/288 (42%)` and `114/326 (35%)`.
- **Reproducible rule and calculation:** `20 / 46 x 100 = 43.478%`, which rounds to 43% at the table's whole-percent precision, not 57%; `23 / 61 x 100 = 37.7%`, which rounds to 38%, not 62%. Either comparison is beyond the 0.5-point whole-percent tolerance. The printed 57% and 62% are the complements (56.5% and 62.3%) of the displayed fractions. Stratum counts and denominators reconcile to Table 1: `101+20=121`, `242+46=288`, `91+23=114`, and `265+61=326`.
- **Direct observation versus inference:** Direct observation: the fraction and percentage in each hypercapnic cell do not describe the same proportion under the printed abundant-secretions label. Inference: the percentages numerically resemble inverse proportions, but no inverse measure is named in the eTable or main table.
- **Alternative source-grounded interpretations:** The numerator/denominator labels could be wrong, the percentage could describe absence of abundant secretions, or the percentage may be a transcription error. The supplied evidence does not resolve the intended convention.
- **Quality-control relevance:** A reviewer using the supplement for hypercapnic baseline characteristics could record 57%/62% as abundant-secretions prevalence despite the stated fractions and aggregate table indicating otherwise.
- **Exact human question:** In eTable 2's hypercapnic abundant-secretions row, do 57% and 62% describe a different, inversely coded measure; if so, what is its correct label and numerator/denominator, and if not, which printed values should be corrected?

## Limitations

- This numeric checker did not adjudicate causal mechanisms or statistical-model conventions not supplied in the package.
- Means, SDs, medians, IQRs, Kaplan-Meier at-risk counts, and overlapping clinical criteria were checked only with valid source-stated relationships; they were not forced into invalid total or percentage calculations.
- The graphical survival curves were not digitized because exact plotted survival probabilities are not printed.
- No candidate was registered solely from P-value formatting or finite-precision display.
