# Numeric consistency check

## Scope and method

This checker reviewed every stable numeric relationship `N001` through `N036` in `relationships/numeric_relationship_inventory.md`, using the canonical main and support evidence maps and their cited source components. Direct sources remain authoritative. The checks applied were, where the displayed data permitted: count sums, numerator/denominator/percentage reconciliation, missingness partitions, arm totals, row/category totals, printed difference and unit/scale labels, repeated-value agreement, and rate-versus-count distinction. Percentages printed to one decimal were assessed with a rounding tolerance of plus or minus 0.05 percentage points; integer count identities have zero tolerance.

Inferential estimates, confidence intervals, test statistics, and P values linked from the N inventory were inventoried as numeric context but are assigned to the separate statistical-review stages for inferential compatibility. No P-value display was treated as a candidate merely because of finite display precision.

## Complete N-inventory coverage and noncandidate outcomes

| N ID | Atomic scope checked | Outcome |
|---|---|---|
| N001 | Main randomized total, three allocation counts, abstract demographic percentages, dates | `NONCANDIDATE`: 776 + 778 + 777 = 2331; the Figure 1 count of 2333 is separately explained by 2 usual-care participants randomized in error and excluded from the primary analysis. |
| N002 | Main adjusted primary percentages/RRs and matched abstract occurrence | `NONCANDIDATE_NUMERIC`: printed adjusted percentages are explicitly model-based, not numerator/denominator proportions; matched result is routed to statistical/cross-source checking. |
| N003 | Eligibility, PEG, BPI item-count/range and threshold definitions | `NONCANDIDATE`: 3-item PEG (0-30) and 11-item BPI-SF/4-item intensity-subscale labels agree across the mapped direct sources. |
| N004 | Individual 1:1:1 allocation, four strata, block sizes 3/6/9 | `NONCANDIDATE`: design labels and units are coherent. |
| N005 | PROMIS and PGIC scale ranges, directions, and cut points | `NONCANDIDATE`: stated scales/directions are internally coherent; worksheet cutoff-label defects are separately recorded below. |
| N006 | Planned n=2331, 777/arm, 90% power, 7.5% difference, 15% UC rate, 80% retention | `NONCANDIDATE`: planning quantities are labeled as plans and are not conflated with observed follow-up denominators. |
| N007 | 7628 screened, 2331 analysis-randomized, exclusion/enrollment flow | `CANDIDATE_NUM-01`: Figure 1's displayed further-ineligibility components do not reconcile to their displayed subtotal. |
| N008 | Follow-up, adherence/session, withdrawal/death, and analysis counts | `NONCANDIDATE`: arm-specific follow-up and primary-analysis Ns agree with Figure 1 and the support missingness records; attrition events are not asserted to be mutually exclusive from prior follow-up. |
| N009 | Table 1 demographic n/N/% cells | `NONCANDIDATE`: every displayed count/denominator/percentage triplet is compatible with one-decimal rounding and the stated exclusion of missing data. |
| N010 | Table 1 race, residence, and social-determinant n/N/% cells | `NONCANDIDATE`: race-category sums reconcile to each arm's displayed nonmissing denominator; remaining triplets meet rounding tolerance. |
| N011 | Table 1 pain, treatment, condition, and opioid cells | `NONCANDIDATE`: displayed n/N/% triplets and stated site-limited opioid denominator are coherent; nonexclusive pain-condition rows were not incorrectly summed. |
| N012 | Table 1 health/outcome cells and denominator qualifiers | `NONCANDIDATE`: displayed cells meet rounding tolerance and missing-data qualifiers explain changing denominators. |
| N013 | Hospitalization, event, death, and patient-initiated adverse-event counts/rates | `NONCANDIDATE`: participant rates match their applicable randomized-arm denominators; event counts are not confused with participant counts. |
| N014 | Figure 2 observed assessment Ns | `NONCANDIDATE`: 3/6/12-month arm counts agree with Figure 1 and DOC-005 eTable 1; plotted percentages are identified as adjusted quantities. |
| N015 | Protocol history, timing windows, site/encounter and surgery definitions | `NONCANDIDATE`: planned definitions are consistently labeled and not compared as observed results. |
| N016 | Protocol enrollment/randomization targets, arm/dose/assessment definitions | `NONCANDIDATE`: the 2380 enrollment target and 2331 randomized target are explicitly distinct. |
| N017 | Protocol outcome/population/subgroup/mediator/economic matching keys | `NONCANDIDATE`: all are plans/definitions with no incompatible observed count. |
| N018 | Protocol interview/delivery quantities and timings | `NONCANDIDATE`: approximate qualitative-sampling quantities are not analysis denominators. |
| N019 | Protocol MCID, secondary, and economic formula definitions | `NONCANDIDATE`: units, endpoint and formula labels are coherent as planned definitions. |
| N020 | SAP document/amendment and planned target/arm/population definitions | `NONCANDIDATE`: the earlier SAP target is clearly a planning value, not a claimed achieved sample size. |
| N021 | SAP subgroup cut points, economic and safety definitions | `NONCANDIDATE`: definitions/plans only; no count-total relationship is claimed. |
| N022 | TIDieR dose/training/outreach/fidelity quantities | `NONCANDIDATE`: direct DOC-004 p6 shows 299/4626 = 6.5%, 89/1791 = 5%, 8/299 = 2.7%, and 11/299 = 3.7%; the 193 training-period count has no printed percent. |
| N023 | DOC-005 outcome scales, MCID and clinical cut points | `NONCANDIDATE`: item counts, ranges, direction and cut points agree with the main evidence map. |
| N024 | DOC-005 follow-up/missingness denominators and follow-up-pattern totals | `CANDIDATE_NUM-02` through `CANDIDATE_NUM-04`: eTable 1 pattern rows do not reconcile to the at-least-one-follow-up totals overall and in two arms. |
| N025 | DOC-005 covariate selection/model covariate sets | `NONCANDIDATE`: model-selection threshold and covariate labels are definitions, not count claims. |
| N026 | DOC-005 imputation/weighted-estimator count and weight inputs | `NONCANDIDATE`: 2036 persons x 3 visits = 6108 records; 6108 - (1798 + 1790 + 1861) = 659 missing values, as printed. |
| N027 | Complete-case/worst-best sensitivity denominators and subset counts | `NONCANDIDATE_NUMERIC`: stated subsets and denominators are coherent; effect estimates are routed to statistical checking. |
| N028 | eTable 9, every 3-arm n/N/% triplet and RR label | `NONCANDIDATE`: all 27 n/N/% triplets on DOC-005 PDF p15 meet one-decimal rounding tolerance; values are correctly labeled relative risks, not rates. |
| N029 | eTable 10 median/IQR and unadjusted mean-difference labels | `NONCANDIDATE_NUMERIC`: medians/IQRs are not treated as inputs to the separately reported GEE mean differences; inferential checks are statistical-stage scope. |
| N030 | eTable 11 raw-score median/IQR and difference labels | `NONCANDIDATE_NUMERIC`: rows retain distinct raw-score, median/IQR, and mean-difference labels; inferential checks are statistical-stage scope. |
| N031 | Workbook title, category denominators, flags, P-value labels/notes | `NONCANDIDATE`: displayed column Ns are 2331/295/468/1568 and no populated cells contain formulas; finite P-value displays are not arithmetic candidates. |
| N032 | Workbook clinical-site/demographic counts and percentages, A4:J48 | `NONCANDIDATE`: clinical-site category totals and category/denominator percentages reconcile within rounding tolerance. |
| N033 | Workbook clinical-characteristic values/missing counts, A49:J94 | `CANDIDATE_NUM-05`: the current-depression count/percentage cell conflicts with its column denominator and missing count. Other checked count/% rows reconcile within tolerance. |
| N034 | Workbook baseline primary/secondary values and missing counts, A95:J109 | `CANDIDATE_NUM-06` and `CANDIDATE_NUM-07`: two cutoff rows are labeled `mean (sd)` while their displayed values are counts/percentages. Other displayed numeric cells and missing rows reconcile. |
| N035 | Workbook cached P values and no-formula status | `NONCANDIDATE`: P-value cell displays match the cached numeric values at stated precision; no literal display-zero issue occurs. |
| N036 | Direct-source no-applicable support units | `NONCANDIDATE`: each retained no-applicable unit has no result-relevant numeric relationship to test. |

## Provisional document-grounded candidates

All records below are pending human adjudication. They have no stable candidate IDs, severity, validity determination, or disposition.

### CANDIDATE_NUM-01 — Figure 1 further-ineligibility component subtotal

- **Category:** Numeric or arithmetic inconsistency.
- **Exact source location:** `jama_debar_2025_oi_250046_1755300121.13587.pdf#page=5`, Figure 1, “4481 Ineligible” box.
- **Direct observation:** The figure prints 4481 ineligible, composed of 2993 with no high-impact chronic pain, 245 with PEG score <12, and 1243 with “One or more of” six further reasons. The six printed further-reason counts are 411, 273, 189, 121, 95, and 34.
- **Rule and calculation:** If the six displayed further reasons exhaust the “one or more of” subtotal, their component counts must be at least the number of persons with one or more such reasons (overlap can only make their sum larger than the union). `411 + 273 + 189 + 121 + 95 + 34 = 1123`, which is 120 below the printed 1243. At integer precision the tolerance is 0.
- **Direct observation versus inference:** The printed values and their 120-count gap are direct/reproducible observations. It is an inference that the displayed list was intended to be exhaustive.
- **Alternative source-grounded interpretation:** The wording “one or more of” permits overlap, but overlap cannot explain a component sum below the union. The figure could intentionally omit one or more additional further reasons, or one displayed count/subtotal may be erroneous.
- **Quality-control relevance:** A flow-chart reason subtotal can be extracted as a screening denominator or eligibility reason in downstream evidence work.
- **Exact human question:** Does the Figure 1 list exhaust the categories represented by the 1243 subtotal? If so, which printed count or subtotal should reconcile the 120-person difference?

### CANDIDATE_NUM-02 — eTable 1 overall follow-up-pattern partition

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** `joi250046supp4_prod_1755300121.15587.pdf#page=7`, eTable 1, Overall column.
- **Direct observation:** The table prints 2036 participants with “At least 1 follow-up.” It prints 188 with one observed follow-up, 283 with two, and 1568 with three.
- **Rule and calculation:** These three mutually exclusive count-of-observed-follow-up categories should partition participants with at least one follow-up: `188 + 283 + 1568 = 2039`, not 2036. Difference = 3 participants; integer tolerance = 0.
- **Direct observation versus inference:** Values and arithmetic are direct. The partition rule follows the row labels “One,” “Two,” and “Three observed follow-ups”; no model assumption is required.
- **Alternative source-grounded interpretation:** A pattern-row count, the at-least-one total, or its source-data definition may differ. No footnote in the cited table supplies an alternative population for these rows.
- **Quality-control relevance:** Follow-up-pattern denominators inform missing-data interpretation and may be transcribed into evidence tables.
- **Exact human question:** Which Overall eTable 1 value(s) correctly define the follow-up-pattern partition, and should the printed 2036 or one/more pattern counts be corrected?

### CANDIDATE_NUM-03 — eTable 1 painTRAINER follow-up-pattern partition

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** `joi250046supp4_prod_1755300121.15587.pdf#page=7`, eTable 1, painTRAINER column.
- **Direct observation:** The table prints 643 painTRAINER participants with at least one follow-up and pattern counts of 77 (one), 103 (two), and 464 (three observed follow-ups).
- **Rule and calculation:** `77 + 103 + 464 = 644`, which is one higher than the printed 643 at-least-one-follow-up total. Integer tolerance = 0.
- **Direct observation versus inference:** Values/arithmetic are direct; the partition rule follows the mutually exclusive pattern-row labels.
- **Alternative source-grounded interpretation:** One pattern count or the arm total may contain a one-person transcription/tabulation discrepancy. No separate denominator is printed for these pattern rows.
- **Quality-control relevance:** The arm-level pattern total feeds differential-follow-up and missing-data assessment.
- **Exact human question:** Which painTRAINER eTable 1 count is authoritative: 643 at least one follow-up or the 644 summed pattern rows?

### CANDIDATE_NUM-04 — eTable 1 Health Coach follow-up-pattern partition

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** `joi250046supp4_prod_1755300121.15587.pdf#page=7`, eTable 1, Health Coach column.
- **Direct observation:** The table prints 690 Health Coach participants with at least one follow-up and pattern counts of 47 (one), 81 (two), and 564 (three observed follow-ups).
- **Rule and calculation:** `47 + 81 + 564 = 692`, which is two higher than the printed 690 at-least-one-follow-up total. Integer tolerance = 0.
- **Direct observation versus inference:** Values/arithmetic are direct; the partition rule follows the mutually exclusive pattern-row labels.
- **Alternative source-grounded interpretation:** One or more pattern counts or the arm total may be transcribed/tabulated differently. The cited table provides no alternate denominator.
- **Quality-control relevance:** The arm-specific missingness distribution can be reused in evidence extraction and sensitivity-analysis interpretation.
- **Exact human question:** Which Health Coach eTable 1 count is authoritative: 690 at least one follow-up or the 692 summed pattern rows?

### CANDIDATE_NUM-05 — Workbook current-depression percentage incompatible with displayed count

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** `joi250046supp5_prod_1755300121.16087.xlsx`, worksheet `eTable 3`, cells `A82:E83`; column E heading is `All Observed (N=1568)` in `E2:E3` and missing count is `E83=2`.
- **Direct observation:** The “Current depression (PHQ-8 >=10), No. (%)” row prints `E82 = 711 (73.2)` for All Observed. The same row prints B/C/D values `1116 (47.9)`, `162 (54.9)`, and `243 (51.9)`; the missing row prints `2 | 0 | 0 | 2`.
- **Rule and calculation:** The footnote states missing values are excluded from percentage denominators. Thus the E-column denominator is `1568 - 2 = 1566`; `711 / 1566 x 100 = 45.40%`, which rounds to 45.4%, not 73.2%. Even using the header N, `711 / 1568 x 100 = 45.34%`. The discrepancy is at least 27.8 percentage points, far beyond plus or minus 0.05 percentage points.
- **Direct observation versus inference:** The count, percentage, header N, and missing count are direct workbook observations; 45.4% is a deterministic diagnostic calculation.
- **Alternative source-grounded interpretation:** The 711 count may be correct with a mistyped percentage, or the displayed percentage may belong to another value/denominator. The count sum `162 + 243 + 711 = 1116` supports the displayed count rather than 73.2%.
- **Quality-control relevance:** This is a baseline characteristic by follow-up-completion group and could be copied as a prevalence/selection predictor.
- **Exact human question:** Should E82 report 711 (45.4%) using the stated missing-excluded denominator, or is either its count/denominator different from the workbook display?

### CANDIDATE_NUM-06 — Workbook social-role cutoff row uses a continuous-summary label for count/percentage values

- **Category:** Measure, label, or scale inconsistency.
- **Exact source location:** `joi250046supp5_prod_1755300121.16087.xlsx`, worksheet `eTable 3`, cells `A103:E104`.
- **Direct observation:** `A103` labels the cutoff row “PROMIS Social role functioning <=40, mean (sd).” Cells B103:E103 print `818 (35.7) | 113 (38.8) | 180 (38.7) | 525 (34.2)`, followed by missing counts in B104:E104.
- **Rule and calculation:** A `mean (sd)` label describes continuous-summary values, whereas each displayed entry is syntactically and numerically a count with percentage. For example, the all-observed value is `525/(1568-31) x 100 = 34.16%`, rounding to the printed 34.2%; it therefore behaves as `N (%)`, not mean (SD). This is a label/type mismatch, not a rounding issue.
- **Direct observation versus inference:** The row label, values, and missing counts are direct. The `N (%)` interpretation is supported by the count/denominator calculation and table conventions.
- **Alternative source-grounded interpretation:** The intended label may be `N (%)`, or a formatting/template error may have carried `mean (sd)` from the preceding continuous PROMIS row.
- **Quality-control relevance:** The cutoff defines a categorical clinical limitation; an incorrect summary label can cause incorrect measure extraction.
- **Exact human question:** Should the `<=40` social-role cutoff row be labeled `N (%)` rather than `mean (sd)`?

### CANDIDATE_NUM-07 — Workbook physical-function cutoff row uses a continuous-summary label for count/percentage values

- **Category:** Measure, label, or scale inconsistency.
- **Exact source location:** `joi250046supp5_prod_1755300121.16087.xlsx`, worksheet `eTable 3`, cells `A106:E107`.
- **Direct observation:** `A106` labels the cutoff row “PROMIS Physical functioning <=40, mean (sd).” Cells B106:E106 print `1709 (74.1) | 209 (72.6) | 357 (76.8) | 1143 (73.6)`, followed by missing counts in B107:E107.
- **Rule and calculation:** The displayed values are count/percentage pairs, not means/SDs. For the all-observed column, `1143/(1568-14) x 100 = 73.55%`, which rounds to the printed 73.6%; hence the values behave as `N (%)`. This is a label/type mismatch, not a rounding issue.
- **Direct observation versus inference:** The label, values, and missing counts are direct; the `N (%)` diagnostic follows from the reproduced proportion.
- **Alternative source-grounded interpretation:** The intended label may be `N (%)`, or `mean (sd)` may be a formatting/template carryover from the preceding continuous physical-function row.
- **Quality-control relevance:** The cutoff is a categorical functional-limitation measure and must not be presented as a continuous summary.
- **Exact human question:** Should the `<=40` physical-function cutoff row be labeled `N (%)` rather than `mean (sd)`?

## Limitations

- Direct-source text on portions of the protocol and SAP has font-encoding limitations; these sources supply planned definitions rather than the observed numeric candidates above, and their mapped direct-rendered provenance was used.
- Adjusted percentages and effect estimates are not raw proportions unless a source supplies a numerator/denominator pair. They were not forced through unsupported arithmetic rules.
- DOC-005 p3's adherence histogram has no tabulated bin values in the reusable extraction; it was not converted into unverified numeric counts.
- The result is a complete numeric-check coverage record, not human adjudication. Each listed provisional candidate remains pending human adjudication.
