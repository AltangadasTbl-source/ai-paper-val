# Numeric Consistency Review

## Scope and method

Complete numeric-consistency review of canonical relationships `N001` through `N047`, one-to-one with the fresh mapper records in `relationships/numeric_relationship_inventory.md`. Direct evidence was read from the supplied PDFs and the fresh native/layout extracts; rendered PDF pages were used for Table 1 and Supplement 3 eTables 2 and 4. Checks applied where relevant were arithmetic; mutually exclusive-category totals; count/denominator/percentage reconciliation to displayed precision; median/IQR ordering; missingness and analysis-population labels; units, scale, measure, arm, and direction identities; repeated-value agreement; and rate/count distinctions. This is a quality-control review, not an adjudication.

Percentage tolerance: a displayed one-decimal percentage was accepted when the exact ratio rounded to that precision (half-unit tolerance 0.05 percentage points, allowing ordinary conventional half rounding). Integer counts require exact reconciliation. For a median (IQR), the printed lower quartile must be no greater than the median and the printed upper quartile must be no less than the median. A result with an unprinted row-specific denominator is not assumed to be erroneous; it is recorded as a candidate only where it conflicts with a displayed table arm total and prevents reproduction of the printed percentage.

## Complete relationship records

| Canonical ID | Exact fresh-source location(s) | Checks and reproducible result | Outcome |
|---|---|---|---|
| N001 | DOC-001, main PDF pp. 1, 3, 5 | Allocation: 477 + 484 = 961 enrolled. | PASS |
| N002 | DOC-001, PDF p. 3, Figure 1 | 3695 assessed − 2734 excluded = 961 randomized; 961 + 1773 = 2734 excluded. | PASS |
| N003 | DOC-001, PDF p. 3, Figure 1 | Ineligible reasons: 323+268+193+98+50+27+2 = 961. | PASS |
| N004 | DOC-001, PDF p. 3, Figure 1 | Not-enrolled reasons: 705+348+296+256+57+55+12+44 = 1773. | PASS |
| N005 | DOC-001, PDF pp. 3, 5 | 475+2=477 and 480+4=484; losses total 6 and match the Results text. | PASS |
| N006 | DOC-001, PDF pp. 1-2 | Six-ICU, 1:1, block-size, and date quantities are compatible labels/design quantities; no arithmetic comparator is printed. | PASS_NO_FURTHER_NUMERIC_IDENTITY |
| N007 | DOC-001, PDF pp. 2-3 | Tidal-volume targets, 1 mL/kg PBW/h adjustment, and pressure thresholds retain the stated mL/kg PBW and cm H2O units and arm direction. | PASS |
| N008 | DOC-001, PDF p. 3 | Sex-specific PBW equations and 28-day maximum strategy duration are consistently labelled; no incompatible application is printed. | PASS |
| N009 | DOC-001, PDF p. 4 | VFD day-28 definition distinguishes ventilation days, alive status, and a >24-hour unassisted period; zero assignment is conditional on >28 ventilation days, not a rate/count substitution. | PASS |
| N010 | DOC-001, PDF p. 4 | Planned 476/group × 2 = 952. The protocol's 397×1.20=476.4 is within one-person whole-participant rounding of 476/group. | PASS |
| N011 | DOC-001, PDF p. 4 | Two-sided alpha, complete-case primary missingness rule, and model/population descriptions do not conflict with a displayed count or percentage. | PASS |
| N012 | DOC-001, PDF p. 5, Table 1 | Male counts/percentages reconcile: 312/477=65.4% and 309/484=63.8%; continuous-value units and IQR ordering are coherent. | PASS |
| N013 | DOC-001, PDF p. 5, Table 1 | Severity scales/ranges are correctly labelled. The at-risk-ARDS and septic-shock count/percent entries do not reproduce from the displayed arm totals; NF002 and NF003, respectively. | CANDIDATE_NF002_NF003 |
| N014 | DOC-001, PDF p. 5, Table 1 | Tobacco categories sum to 475/482 and their percentages reproduce from 475/482, not header n=477/484; NF004. | CANDIDATE_NF004 |
| N015 | DOC-001, PDF p. 5, Table 1 | Alcohol categories sum to 475/482 and their percentages reproduce from 475/482, not header n=477/484; NF005. | CANDIDATE_NF005 |
| N016 | DOC-001, PDF p. 5, Table 1 | Surgical+medical: 82+393=475 and 79+403=482. Their percentages reproduce these unlabelled totals rather than header n=477/484; NF010. | CANDIDATE_NF010 |
| N017 | DOC-001, PDF p. 5, Table 1 | Fourteen intubation-reason categories sum to 477 and 484; one-decimal percentages reconcile to the arm totals. | PASS |
| N018 | DOC-001, PDF p. 5, Table 1 | Ventilation-mode categories: 143+98+236=477 and 154+91+239=484; percentages reconcile. | PASS |
| N019 | DOC-001, PDF p. 5, Table 1 and Results | Table 1 arm-specific pre-randomization medians and Results pooled timing medians describe distinct populations/time origins; no direct same-measure contradiction. | PASS |
| N020 | DOC-001, PDF p. 5, Table 1 | Respiratory measures retain distinct units (mL/kg PBW, cm H2O, /min, fraction, mm Hg); all printed IQR endpoints bracket their medians. | PASS |
| N021 | DOC-001, PDF pp. 1, 5-6 | VFD mean/SD, median/IQR, n=475/480, mean difference, and abstract repetition agree; direction is low minus intermediate (15.2−15.5≈−0.3, printed −0.27). | PASS |
| N022 | DOC-001, PDF p. 6, Table 2 | Surviving-patient ventilation-days group summaries, IQR ordering, and low-minus-intermediate difference direction (5.4−6.0≈−0.6) agree to displayed precision. | PASS |
| N023 | DOC-001, PDF pp. 1, 6-7 | ICU-stay mean-difference and Kaplan-Meier HR displays are distinct effect measures for the same outcome, explicitly labelled; no count/rate substitution or contradictory direction is printed. | PASS |
| N024 | DOC-001, PDF pp. 1, 6-7 | Hospital-stay mean-difference and Kaplan-Meier HR displays are distinct labelled analyses; medians/IQRs and low-minus-intermediate mean difference are directionally coherent. | PASS |
| N025 | DOC-001, PDF pp. 1, 6-7 | ICU, hospital, 28-day, and 90-day mortality numerators/denominators round to all displayed percentages; repeated abstract/Figure 2B values match after population/time matching. | PASS |
| N026 | DOC-001, PDF pp. 1, 6 | ARDS and pneumonia fractions reproduce printed percentages (17/448=3.8%, 23/462=5.0%, 19/450=4.2%, 17/462=3.7%) and abstract repetitions match. | PASS |
| N027 | DOC-001, PDF pp. 1, 6 | Pneumothorax and atelectasis fractions reproduce printed percentages; event counts are not reported as person-time rates. | PASS |
| N028 | DOC-001, PDF p. 6, Table 2 | Extrapulmonary infection and sepsis fractions reproduce printed percentages: 20/448=4.5%, 28/463=6.0%, 12/448=2.7%, 16/463=3.5%. | PASS |
| N029 | DOC-001, PDF p. 6, Table 2 | Delirium and tracheostomy fractions reproduce printed percentages; differing delirium denominators are explicitly printed and do not conflict with the allocation totals. | PASS |
| N030 | DOC-001, PDF p. 6, Results | ICU-location subgroup differences are directionally compatible with the listed group means in Supplement 3 eTable 5. The intervals are explicitly printed as IQR in the main text; no further interval identity is supplied here. | PASS |
| N031 | DOC-001, PDF p. 7, Figure 2A | Free-from-ventilation curve uses days and risk sets, while caption gives observation summaries; they are labelled different quantities. Risk sets do not exceed their initial displayed counts. | PASS |
| N032 | DOC-001, PDF p. 7, Figure 2B | 90-day survival curve risk sets do not exceed day-0 sets; HR 1.07 (0.87-1.31) is identical to the matched 90-day result. | PASS |
| N033 | DOC-001, PDF p. 7, Figure 2C | ICU-stay curve uses at-risk sets/HR, distinct from Table 2 mean difference; sequence of risk sets is nonincreasing. | PASS |
| N034 | DOC-001, PDF p. 7, Figure 2D | Hospital-stay curve uses at-risk sets/HR, distinct from Table 2 mean difference; sequence of risk sets is nonincreasing. | PASS |
| N035 | DOC-001, PDF p. 7 | Discussion values (approximately 7 and 9 mL/kg PBW) are on-treatment summaries, not pre-randomization Table 1 values; units and arm ordering remain consistent. | PASS |
| N036 | DOC-002, PDF pp. 17-19; DOC-003, PDF pp. 10-11 | Protocol/SAP plan total: 476 per arm ×2=952. Pre-expansion 397 per arm times 1.20 gives 476.4, compatible with whole-participant rounding to 476. | PASS |
| N037 | DOC-002, PDF pp. 20-23; DOC-003, PDF pp. 7-8 | Lower/low 4-6 and higher/intermediate 8-10 mL/kg PBW labels, PBW formulas, thresholds, and timepoints remain distinct and matched. | PASS |
| N038 | DOC-002, PDF pp. 26-30; DOC-003, PDF pp. 8-9 | Supplied VFD definitions retain the day-28, alive, and ≥24-consecutive-hour elements; no measure or scale mismatch is printed. | PASS |
| N039 | DOC-002, PDF p. 48 | ARDS PaO2/FiO2 bands, PEEP requirement, and APACHE/SAPS/MRC scale ranges have ordered thresholds and correct units. | PASS |
| N040 | DOC-004, PDF p. 5, eTable 1 | All reported count/total percentages reproduce under one-decimal rounding; all median/IQR triples are ordered. Smaller ABG denominators are expressly attributed to missing ABG measurements. | PASS |
| N041 | DOC-004, PDF p. 6, eTable 2 | Mode strata partition eTable 1 N at each timepoint (e.g., after titration 309+110+33=452 and 362+73+28=463). One intermediate-arm PEEP IQR is printed with reversed endpoint 5-1; NF001. | CANDIDATE_NF001 |
| N042 | DOC-004, PDF p. 7, eTable 3 | ABG count/total percentages reproduce; `---` accompanies 0/59 vs 0/67 and 0/18 vs 0/18 as an uncomputed P cell, not a display-zero P value. The `7/20 (35.)` display is numerically equivalent to 35.0% and is not a count/percentage contradiction. | PASS |
| N043 | DOC-004, PDF p. 8, eTable 4 | Explicit fractions using 454/464 reproduce. Sedative, analgesic, neuromuscular-blockade, and vasopressor count/percent pairs do not reproduce from displayed header n=477/484 and omit row totals; NF006-NF009. | CANDIDATE_NF006_NF009 |
| N044 | DOC-004, PDF p. 9, eTable 5 | For every subgroup, printed low-minus-intermediate mean difference is directionally consistent with displayed means to rounding (including ICU start −2.50 and outside ICU 1.45). | PASS |
| N045 | DOC-004, PDF p. 10, eFigure 1 | Graph has curve/axis/arm labels but no printed numeric estimate or table to reconcile; matched endpoint identity retained. | PASS_NO_PRINTED_NUMERIC_COMPARATOR |
| N046 | DOC-004, PDF pp. 11-13, eFigures 2-4 | Graphical distributions show no printed numerical estimates, intervals, totals, or P values requiring numerical reconciliation. | PASS_NO_PRINTED_NUMERIC_COMPARATOR |
| N047 | DOC-005, PDF p. 1 | Data-availability statement has no result-relevant numeric relationship. | PASS_NO_APPLICABLE_NUMERIC_SCOPE |

## Candidate consistency observations

### NF001 — Reversed endpoint in an eTable 2 PEEP interquartile range

- **Primary category:** Numeric or arithmetic inconsistency
- **Exact source location:** DOC-004, `joi180108supp3_prod.pdf`, PDF p. 6, eTable 2, Other Mode of Ventilation, “After titration on day of randomization,” Intermediate Tidal Volume, PEEP (cm H2O). Fresh layout evidence: `preprocessing/layout_text/joi180108supp3_prod.txt`, printed table row at lines 246-248 of native extraction vicinity.
- **Printed inputs:** Median PEEP is printed as `8 (5 – 1)` cm H2O, with P=.50 for the arm comparison.
- **Direct observation:** The PDF and fresh native/layout text all show the same printed interval `5 – 1`; this is not an extraction-only artifact.
- **Rule and calculation:** In `median (IQR)`, lower quartile ≤ median ≤ upper quartile. Here the printed lower endpoint 5 ≤ median 8, but printed upper endpoint 1 < median 8 and is also < lower endpoint 5. No rounding tolerance can reverse an IQR's endpoint order.
- **Inference versus observation:** The defective ordering is directly observable. An intended upper endpoint such as 10 is only a possible explanation and has not been substituted for the printed value.
- **Alternative source-grounded interpretation:** This table's `Other Mode` group includes protocol-disallowed modes and its low-arm cell is `5 (5 – 10)`, but neither fact supplies the intermediate cell's missing/correct upper endpoint.
- **Quality-control relevance:** An unreproducible dispersion interval can be copied as a ventilator-setting summary or used in an extraction table.
- **Human question:** What is the intended upper IQR endpoint for the intermediate tidal-volume PEEP value after titration, and should the published entry be corrected?

### NF002 — At-risk-for-ARDS percentages do not reproduce from Table 1 arm totals

- **Primary category:** Denominator, proportion, or total inconsistency
- **Exact source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 5, Table 1, header `n=477`/`n=484`, “Patients at risk for ARDS.”
- **Printed inputs; rule/calculation; tolerance:** `292 (61.6)` and `290 (60.3)`; 292/477=61.2% and 290/484=59.9%, outside the 0.05-point one-decimal rounding tolerance. Denominators 474 and 481, respectively, reproduce the printed percentages.
- **Direct observation versus inference:** Header, counts, and percentages are direct observations. Available-case denominators are an inference; no row total/missingness footnote is printed.
- **Alternative and human question:** The row may use 474/481 available cases. Were these intended denominators, and should they and missing counts be stated?
- **Quality-control relevance:** The baseline risk proportions are not reproducible from the displayed arm totals.

### NF003 — Septic-shock percentages do not reproduce from Table 1 arm totals

- **Primary category:** Denominator, proportion, or total inconsistency
- **Exact source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 5, Table 1, header `n=477`/`n=484`, “Septic shock.”
- **Printed inputs; rule/calculation; tolerance:** `82 (17.6)` and `74 (15.5)`; 82/477=17.2% and 74/484=15.3%, outside tolerance. Approximate denominators 466 and 477 would reproduce the displayed rounded percentages.
- **Direct observation versus inference:** Printed header/counts/percentages are direct; the alternative row-specific denominators are diagnostic inference only.
- **Alternative and human question:** This may be available-case reporting. What exact denominators were used, and should the missingness/denominators be printed?
- **Quality-control relevance:** The reported baseline septic-shock proportions cannot be reproduced from the stated arm totals.

### NF004 — Tobacco category totals and percentages use unlabelled denominators

- **Primary category:** Denominator, proportion, or total inconsistency
- **Exact source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 5, Table 1, tobacco-use rows under header `n=477`/`n=484`.
- **Printed inputs; rule/calculation; tolerance:** Categories total 106+97+75+197=475 and 111+97+80+194=482? The printed intermediate total is 482, while its printed percentages such as 111/482=23.0% reproduce 482; low percentages reproduce 475. Neither total matches its header (477/484).
- **Direct observation versus inference:** Counts, percentages, and header are direct. Unreported available-case denominators/missing data are inferred.
- **Alternative and human question:** The table may deliberately use 475/482. Were these denominators intended, and why are they not supplied despite an `Unknown` category?
- **Quality-control relevance:** Tobacco-category proportions and completeness cannot be extracted reproducibly.

### NF005 — Alcohol category totals and percentages use unlabelled denominators

- **Primary category:** Denominator, proportion, or total inconsistency
- **Exact source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 5, Table 1, alcohol-use rows under header `n=477`/`n=484`.
- **Printed inputs; rule/calculation; tolerance:** Categories total 121+47+26+59+222=475 and 92+61+30+56+243=482. Printed percentages reproduce 475/482, not header 477/484; e.g., 121/475=25.5% and 92/482=19.1%.
- **Direct observation versus inference:** Printed values are direct; missing/available-case explanation is inference.
- **Alternative and human question:** Were 475/482 intended row denominators, and should the corresponding missing data or denominator note be supplied?
- **Quality-control relevance:** Baseline alcohol distributions cannot be reproduced from the displayed arm totals.

### NF010 — ICU-admission-reason categories use unlabelled denominators

- **Primary category:** Denominator, proportion, or total inconsistency
- **Exact source location:** DOC-001, `jama_simonis_2018_oi_180108.pdf`, PDF p. 5, Table 1, “Reason for ICU admission,” header `n=477`/`n=484`.
- **Printed inputs; rule/calculation; tolerance:** Surgical/medical counts total 82+393=475 and 79+403=482. Printed percentages reproduce those totals: 82/475=17.3%, 393/475=82.7%, 79/482=16.4%, and 403/482=83.6%, rather than displayed header totals 477/484.
- **Direct observation versus inference:** Header, mutually exclusive category counts, and percentages are direct; an available-case/missing-data explanation is inference.
- **Alternative and human question:** The two-category row may intentionally use 475/482. Were these the intended denominators, and should omitted patients or a denominator note be reported?
- **Quality-control relevance:** The table's ICU-admission distribution cannot be reproduced from its displayed arm totals.

### NF006 — Sedative-infusion percentages omit their effective denominators

- **Primary category:** Denominator, proportion, or total inconsistency
- **Exact source location:** DOC-004, `joi180108supp3_prod.pdf`, PDF p. 8, eTable 4, Sedative infusion, header `n=477`/`n=484`.
- **Printed inputs; rule/calculation; tolerance:** `320 (70.6)` and `333 (72.1)`; 320/477=67.1% and 333/484=68.8%, far outside one-decimal tolerance. Approximate denominators 453/462 reproduce the percentages.
- **Direct observation versus inference:** Header/counts/percentages and the “number / total (%)” footnote are direct; 453/462 are inferred.
- **Alternative and human question:** An available-case medication denominator may have been used. What exact totals apply, and should they be printed?
- **Quality-control relevance:** Sedative-use prevalence cannot be independently reproduced.

### NF007 — Analgesic-infusion percentages omit their effective denominators

- **Primary category:** Denominator, proportion, or total inconsistency
- **Exact source location:** DOC-004, `joi180108supp3_prod.pdf`, PDF p. 8, eTable 4, Analgesic infusion, header `n=477`/`n=484`.
- **Printed inputs; rule/calculation; tolerance:** `277 (61.1)` and `273 (59.1)`; 277/477=58.1% and 273/484=56.4%, outside tolerance; 277/453 and 273/462 reproduce the displayed values.
- **Direct observation versus inference:** Printed information is direct; row-specific available-case denominators are inferred.
- **Alternative and human question:** Were 453/462 or different denominators intended, and should the table identify them?
- **Quality-control relevance:** Analgesic-use prevalence cannot be reproduced from stated arm totals.

### NF008 — Neuromuscular-blockade percentages omit their effective denominators

- **Primary category:** Denominator, proportion, or total inconsistency
- **Exact source location:** DOC-004, `joi180108supp3_prod.pdf`, PDF p. 8, eTable 4, Neuromuscular blockade, header `n=477`/`n=484`.
- **Printed inputs; rule/calculation; tolerance:** `53 (11.7)` and `60 (13.0)`; 53/477=11.1% and 60/484=12.4%, outside tolerance; 53/453=11.7% and 60/462=13.0%.
- **Direct observation versus inference:** Printed values are direct; denominators 453/462 are a calculation-based inference.
- **Alternative and human question:** Did this row use an available-case population, and what exact denominators should be reported?
- **Quality-control relevance:** The intervention co-use proportions cannot be reproduced.

### NF009 — Vasopressor-use percentages omit their effective denominators

- **Primary category:** Denominator, proportion, or total inconsistency
- **Exact source location:** DOC-004, `joi180108supp3_prod.pdf`, PDF p. 8, eTable 4, Use of vasopressors, header `n=477`/`n=484`.
- **Printed inputs; rule/calculation; tolerance:** `363 (80.0)` and `353 (76.4)`; 363/477=76.1% and 353/484=72.9%, outside tolerance; 363/454=80.0% and 353/462=76.4%.
- **Direct observation versus inference:** Header/counts/percentages are direct; distinct row denominators are not printed.
- **Alternative and human question:** Was a medication available-case denominator used, and what exact denominators should be stated?
- **Quality-control relevance:** Vasopressor-use prevalence cannot be reproduced consistently.

## Non-candidate conventions and limitations

- No displayed `P=0`, `p=0.000`, or equivalent literal-zero P value was identified in this assigned numeric inventory. The `---` cells in eTable 3 are uncomputed P cells alongside zero event counts and were not treated as display-zero P values.
- P values and inferential compatibility beyond directly supplied numeric identities are assigned to the separate statistical lanes. No candidate here is a statistical adjudication.
- The review does not infer unpublished patient-level denominators, correct a printed value, or decide whether a candidate is valid. All observations require human adjudication.

**Coverage conclusion:** 47/47 canonical N relationships explicitly checked; 41 pass/no-applicable outcomes and 6 candidate-tagged relationship records yielding 10 distinct lane-local candidate observations (`NF001`-`NF010`).
