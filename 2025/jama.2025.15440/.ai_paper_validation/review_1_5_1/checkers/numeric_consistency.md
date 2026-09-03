# Numeric Consistency Check

## Scope and method

Complete review of stable numeric/reporting relationships **N001-N062** in
`relationships/numeric_relationship_inventory.md`. I used the two current evidence
maps as locators and checked the printed values against the supplied main article and
supplement PDFs at the cited pages. Checks applied where relevant were: count and
subgroup sums; numerator/denominator/percentage calculations; rounding at the displayed
precision; total and missingness reconciliation; matched repeated values; analysis
population and time-window identity; rate/proportion/count distinctions; and
measure/label/scale consistency. A displayed value was treated as compatible where its
unrounded value could produce the shown value at the stated precision. No legacy
candidate, checker, reviewer, or report artifact was used.

Direct source files used:

- `jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf` (DOC-001), PDF pp. 1-9.
- `joi250068supp1_prod_1760999665.28862.pdf` (DOC-002), PDF pp. 20-22 for the
  quantitative protocol tables.
- `joi250068supp2_prod_1760999665.29862.pdf` (DOC-003), PDF pp. 7-22 for planned
  populations, definitions, and planning quantities.
- `joi250068supp3_prod_1760999665.30362.pdf` (DOC-004), PDF pp. 2 and 4-11 for
  supplementary results tables and figures.

## Per-relationship coverage

`PASS` means that the applicable numeric checks reconciled at printed precision, or
that the relationship is a definition/planning/display record with no unsupported
arithmetic contradiction. `FLAGGED` means a distinct provisional candidate is detailed
below; it is not an adjudication or disposition.

| ID | Checks completed and result | Status |
|---|---|---|
| N001 | 5,040/22,044 = 22.86% -> 22.9%; 2,520 + 2,520 = 5,040. | PASS |
| N002 | 2,126/2,520 = 84.37% -> 84.4%; summary labels/units are compatible. | PASS |
| N003 | 89/2,126 = 4.19% -> 4.2% in the abstract; the p. 5 denominator clarification reconciles it. | PASS |
| N004 | 172/2,520 = 6.825% -> 6.8%; 136/2,520 = 5.397% -> 5.4%. | PASS |
| N005 | 1.63 - 1.14 = 0.49 months; independent values rounded to 0.01 can yield a displayed 0.50 difference. Difference CI is not derived by subtracting marginal CI endpoints. | PASS |
| N006 | 69/2,520 = 2.738% -> 2.7%; 64/2,520 = 2.540% -> 2.5%. | PASS |
| N007 | Practice, recruitment, follow-up, and analysis dates are identifiers/times, with no conflicting repeated total. | PASS |
| N008 | Fourteen-day intended monitoring and 1:1 allocation labels are compatible with 2,520 per arm. | PASS |
| N009 | Outcome, population, time window, subgroup, and sensitivity labels match their later displays. | PASS |
| N010 | Planning values are explicitly assumptions; no observed-result arithmetic is asserted by this relationship. | PASS |
| N011 | 20,858 + 1,186 = 22,044; 5,116 - 76 = 5,040; 72 + 4 = 76; 2,520 + 2,520 = 5,040. | PASS |
| N012 | 2,126 + 394 = 2,520; 206 + 188 = 394; 2,408 + 112 = 2,520; 2,310 + 98 = 2,408. | PASS |
| N013 | 2,410 + 110 = 2,520; 103 + 7 = 110; 2,292 + 118 = 2,410. | PASS |
| N014 | 2,408/2,520 = 95.56% and 2,410/2,520 = 95.63%, both 95.6%; secondary-care fractions round as printed. | PASS |
| N015 | 2,360/5,040 = 46.83% -> 47%; 4,528/5,040 = 89.84% -> 90%; 963/5,040 = 19.11% -> 19%; 68/5,040 = 1.35% -> 1.3%. | PASS |
| N016 | Exact displayed fractions and percentage CIs match the primary-result display. | PASS |
| N017 | 5.6% is a time-to-event curve value, whereas 5.40% is an ITT 2.5-year proportion; 136/2,410 complete primary-care follow-up = 5.64%, a compatible explanation. | PASS |
| N018 | 41 - 21 = 20 days. Marginal rounded CIs need not subtract to the reported contrast CI. | PASS |
| N019 | 89/2,520 = 3.53% and 89/2,126 = 4.19%; 51/89 = 57.3%; 29+49 are nonexclusive burden categories as labeled. | PASS |
| N020 | Episode counts 37+18+26+8 = 89; rounded percentages 42+20+29+9 = 100; 83/89 = 93.3%; 78 is a subset of 83. | PASS |
| N021 | 89 AF plus 13 flutter-without-AF = 102 AF and/or flutter participants; the wording identifies the 13 as additional. | PASS |
| N022 | 364/2,520 = 14.44% -> 14.4%; 322/2,520 = 12.78% -> 12.8%; direct risk ratio is 1.130. | PASS |
| N023 | Death: 103/2,520 = 4.09% -> 4.1%, 126/2,520 = 5.00%; stroke fractions round to 2.7% and 2.5%. | PASS |
| N024 | Age strata sum to 2,520 in each arm; sex strata sum to 2,520 in each arm; percentages are compatible with denominators. | PASS |
| N025 | Race/ethnicity categories including missing sum to 2,520 in each arm; percentages round from the displayed counts. | PASS |
| N026 | BMI categories including missing sum to 2,520 in each arm; row percentages reconcile. | PASS |
| N027 | CHA2DS2VASc strata sum to 2,520 in each arm; printed percentages reconcile. | PASS |
| N028 | Each diagnosis percentage is count/2,520 at the stated precision; diagnoses are not presented as exclusive. | PASS |
| N029 | Each medication percentage is count/2,520 at the stated precision; medication rows are not presented as exclusive. | PASS |
| N030 | <80 denominators are age-stratum sums (683+1,032=1,715; 683+1,061=1,744); 94+78=172 and 74+62=136; risks, absolute differences, and ratios reconcile after rounding. | PASS |
| N031 | Female and male denominators sum to 2,520 per arm; events sum to the overall 172/136; exact-count risk differences yield printed values after rounding. | PASS |
| N032 | 172/2,520 - 136/2,520 = 1.4286% -> 1.43%; ratio = 1.2647 -> 1.26. | PASS |
| N033 | Risk sets decline over time within each arm; they are at-risk counts, not event totals, and no unsupported subtraction rule applies. | PASS |
| N034 | Oral-anticoagulation risk sets decline over time within each arm; labels distinguish time-to-first-record from the prescription proportion. | PASS |
| N035 | Death components reconcile (32+71=103; 43+83=126). Patch stroke subtype counts exceed `Any stroke` (72 versus 69), whereas usual-care counts reconcile (64 versus 64); detailed below. | FLAGGED: NC001 |
| N036 | Discussion claims retain the correct direction/measure distinction and are qualified as exploratory/not powered for clinical outcomes. | PASS |
| N037 | Values are expressly external-study context rather than AMALFI results; no within-package AMALFI comparator is implied. | PASS |
| N038 | Directly mapped reference page; no result-relevant numeric relationship. | PASS |
| N039 | Table 1 control cumulative values equal 0.70 percentage points per year; active cumulative increments and labels are planning assumptions. | PASS |
| N040 | Table 2 control/active expected proportions and sample-size entries are labeled planning quantities; no inconsistent total or unit is printed. | PASS |
| N041 | Table 3 total-active and implied-control values conform to the stated ratio scenarios at displayed precision; required n/power cells are scenario outputs. | PASS |
| N042 | Table 4 subgroup proportions, ratios, and power/n cells are explicitly planning scenarios; subgroup shares sum to 100% for the complementary pairs. | PASS |
| N043 | SAP primary ITT outcome, population, 2.5-year window, age, and sex definitions match the result displays. | PASS |
| N044 | 1:1 allocation and two-week patch labels agree with DOC-001 and DOC-004 denominators. | PASS |
| N045 | Censoring/no-censoring labels distinguish the binary 2.5-year primary outcome from 5-year time-with-AF analysis; no population contradiction. | PASS |
| N046 | Planned shells use overall 5,040 and 2,520/arm correctly; listed quantities are distinct descriptive measures. | PASS |
| N047 | Anticoagulation count/proportion versus calendar-month exposure labels are distinct; 30/60-month windows are explicit. | PASS |
| N048 | Initial/expanded sample sizes, expected risks, ratio, and power are planning assumptions and agree at their displayed rounded precision. | PASS |
| N049 | AF definition (continuous tracing >=30 seconds) and 14-day maximum monitoring labels are compatible with the results tables. | PASS |
| N050 | 1,960+166=2,126; 1,960+166+188+206=2,520; all four printed percentages are compatible with n=2,520. | PASS |
| N051 | 43+18+8+97=166; percentages are each count/166 at displayed precision. | PASS |
| N052 | 2,126+394=2,520; every age and sex ECG/no-ECG pair sums to its overall count; category totals reproduce 2,126 and 394. | PASS |
| N053 | Race and BMI category pairs reconcile to their displayed overall strata and total 2,520; row percentages use their stated row denominators. | PASS |
| N054 | CHA2DS2VASc ECG/no-ECG pairs sum to overall rows; diagnosis rows use nonexclusive conditions and reconcile count splits. | PASS |
| N055 | Medication ECG/no-ECG counts sum to every overall row; medication rows are nonexclusive, so no column-sum identity is expected. | PASS |
| N056 | 89/2,520 = 3.53% and 89/2,126 = 4.19%; AF-with/without-flutter counts sum to 89; other-condition percentages use the two printed denominators. | PASS |
| N057 | Each nonurgent count divided by 2,520 and 2,126 yields the printed percentages at two decimal places; conditions are not exclusive. | PASS |
| N058 | Sensitivity overall and age cells reproduce denominators/event sums and displayed risks, absolute differences, and ratios at rounding precision. | PASS |
| N059 | Sensitivity sex cells reproduce denominator/event sums and displayed risks, absolute differences, and ratios at rounding precision. | PASS |
| N060 | Histogram axes and explicit grouped percentages are descriptive; no bin counts are printed from which a total can be required. | PASS |
| N061 | Risk set begins at 89 and declines 89,34,18,10,8,7,6; seven pre-report records are explicitly described as immediate events rather than a denominator inconsistency. | PASS |
| N062 | AF/AFL grouped percentages 10+26+18+46=100 after rounding; distribution is separately labeled AF/AFL, not AF-only. | PASS |

## Provisional numeric-consistency candidates

### NC001 — Stroke subtype event counts do not partition the displayed `Any stroke` count

- **Status:** Pending Human Adjudication. This is a checker-local provisional identifier only; it is not a stable candidate ID, severity, validity decision, or disposition.
- **Category:** Numeric or arithmetic inconsistency; potentially denominator/total and rate-versus-count labeling clarification.
- **Exact source locations:** DOC-001, `jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf`, PDF p. 7, Figure 4B, rows `Presumed ischemic stroke`, `Hemorrhagic stroke`, and `Any stroke`. The same main-paper text describes all as events through 2.5 years.
- **Direct observation:** Figure 4B prints, for patch/usual care respectively: presumed ischemic stroke 60 (2.4%)/58 (2.3%); hemorrhagic stroke 12 (0.5%)/6 (0.2%); and any stroke 69 (2.7%)/64 (2.5%). The Figure 4B legend states that these are time-to-event analyses for events occurring between randomization and 2.5 years, using the stated record sources; it defines presumed ischemic stroke as including unspecified stroke types.
- **Printed comparator and rule:** If the two displayed stroke-type rows are intended to be mutually exclusive participant-level components of the row labeled `Any stroke` on the same figure/time window, their sums should equal `Any stroke`.
- **Calculation:** Patch: 60 + 12 = 72, compared with any stroke 69 (excess 3). Usual care: 58 + 6 = 64, equal to any stroke 64. At displayed percentages, patch 2.4% + 0.5% = 2.9%, compared with 2.7%; usual care 2.3% + 0.2% = 2.5%, equal to 2.5%. Counts, not rounded percentages, establish the patch discrepancy. Tolerance is 0 participants because all three cells print integer event counts.
- **Inference versus observation:** The unequal patch sum is direct arithmetic. Treating it as an inconsistency is an inference conditional on the figure presenting mutually exclusive, participant-level stroke subtypes. The figure does not explicitly state whether a participant with multiple stroke records or both stroke classifications can contribute to more than one subtype row while being counted once in `Any stroke`.
- **Source-grounded alternatives:** The types may be overlapping event classifications; a participant could have more than one stroke record/type during follow-up; `Any stroke` may count unique participants whereas subtype rows may count events; or a classification/record-source rule may make unspecified and hemorrhagic events overlap. The legend supplies record sources and an assumption for unspecified stroke but does not resolve overlap/counting conventions.
- **Quality-control relevance:** A reader extracting component stroke outcomes could incorrectly assume that the subtype rows partition the all-stroke outcome. Confirmation would clarify the event/participant counting rule and preserve consistent quantitative reuse.
- **Exact human question:** Were Figure 4B `Presumed ischemic stroke` and `Hemorrhagic stroke` counted as mutually exclusive participant-level outcomes? If yes, please verify/correct the patch counts (60 + 12 versus `Any stroke` 69); if no, please specify the overlap and whether `Any stroke` counts unique participants while subtype rows count events or nonexclusive classifications.

## Summary and limitations

- **Relationships reviewed:** 62 of 62 (N001-N062), including the explicit no-applicable-result record N038.
- **Provisional qualifying candidates:** 1 (NC001).
- **No display-zero P-value candidate:** no candidate was created from a finite-precision P-value display.
- **Limitations:** DOC-002's native text layer is garbled, so its visually mapped planning tables were checked as displayed assumptions rather than reconstructed beyond their printed cells. Several differences/intervals are outputs of permutation, time-to-event, or other methods; marginal rounded CIs were not incorrectly treated as algebraic inputs for a contrast CI. No raw participant data or outcome-derivation file was supplied to resolve Figure 4B's possible subtype overlap.
