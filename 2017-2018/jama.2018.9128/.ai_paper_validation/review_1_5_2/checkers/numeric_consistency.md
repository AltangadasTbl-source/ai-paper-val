# Numeric consistency review — N001–N064

**Scope and method.** All 64 canonical numeric/reporting relationships in `relationships/numeric_relationship_inventory.md` were checked against the newly prepared maps and, where a printed comparison mattered, the supplied PDFs and fresh layout text. Checks included arithmetic, numerator/denominator and rounding (tolerance: the last displayed percentage unit, normally 0.05 percentage point), category totals, stated missingness, population/time and scale labels, repeated values, and rate/count distinctions. This is a pre-candidate record only: no stable IDs, severity, validity decision, or disposition is assigned. A displayed finite-precision zero P value would not be a candidate without an independent contradiction; no such display-zero issue occurred here.

## Complete relationship status register

| ID | Status | Checks completed and result |
|---|---|---|
| N001 | CHECKED—no discrepancy | Trial frame, 610 pairs, dates, setting, and age range are internally descriptive; no incompatible repeated count. |
| N002 | CHECKED—no discrepancy | Allocation 304+306=610; exposure labels are not conflated with visit counts. |
| N003 | CHECKED—no discrepancy | Eligibility percentile limits and BMI kg/m² definition are distinct and compatible; outcome count is descriptive. |
| N004 | CHECKED—no discrepancy | Individual-pair randomization label is compatible with allocation/ITT population. |
| N005 | CHECKED—no discrepancy | 612+486+418=1516; 2126−1516=610 exactly. |
| N006 | CHECKED—no discrepancy | 301 received+3 immediately dropped=304; control 306 received=306 allocated. |
| N007 | PRE-CANDIDATE NUM-P01 | Each Figure 1 row balances to 304, but its printed BMI-measured/retained counts conflict with Figure 2/eTable 1 at multiple times; detailed below. |
| N008 | PRE-CANDIDATE NUM-P01 | Each Figure 1 row balances to 306, but its printed BMI-measured/retained counts conflict with Figure 2/eTable 1 at multiple times; detailed below. |
| N009 | CHECKED—no discrepancy | ITT 304/306 equals randomization totals; missingness is explicitly handled separately. |
| N010 | CHECKED—no discrepancy | Six occasions (baseline plus five follow-ups) and stated measurement units are internally coherent. |
| N011 | CHECKED—no discrepancy | Planned 600×80%=480; protocol power table’s 0.4/90% cell is 480. |
| N012 | CHECKED—no discrepancy | 278/304=91.45%→91.4%; 272/306=88.89%→88.9%; combined 550/610=90.16%→90.2%. Baseline percentages are compatible with stated denominators/rounding. |
| N013 | CHECKED—no discrepancy | BMI-category denominators 302/301 reconcile to 2 and 5 out-of-range children; 568+42=610 adults; stated score ranges are compatible with labels. |
| N014 | CHECKED—no discrepancy | 154/304=50.66%→50.7%; 162/306=52.94%→52.9%. |
| N015 | CHECKED—no discrepancy | Means/SDs retain child BMI kg/m² versus BMI-z as distinct scales. |
| N016 | CHECKED—no discrepancy | I 193+109=302 and C 203+98=301; percentages total 100.0 in each arm. |
| N017 | CHECKED—no discrepancy | Child waist/skin-fold denominators and units are explicit; missing counts reconcile to arm totals where applicable. |
| N018 | CHECKED—no discrepancy | Daily activity measures are minutes; component values are not asserted to be an exhaustive 24-hour partition. |
| N019 | CHECKED—no discrepancy | Macronutrients: I 28.5+55.4+16.1=100.0%; C 28.2+56.1+15.7=100.0%; diet denominators are explicit. |
| N020 | CHECKED—no discrepancy | Race counts sum I=303 and C=304; displayed percentages total 100.1%/100.0% within rounding. |
| N021 | CHECKED—no discrepancy | Adult-sex percentages: 300/304=98.68%→98.7%; 300/306=98.04%→98.0%. |
| N022 | CHECKED—no discrepancy | Adult waist total 285+283=568 matches footnote; pregnancy nonmeasurement 42 gives 610. |
| N023 | CHECKED—no discrepancy | Adult-race counts sum I=304, C=306; percentage totals 100.1%/99.9% are rounding-consistent. |
| N024 | CHECKED—no discrepancy | Time-in-US and acculturation denominators are stated; acculturation n=274+272=546 is not the eligible 556 because ten values are unavailable, not a contradiction. |
| N025 | CHECKED—no discrepancy | Employment counts sum 303/306 and percentages total 100.0% in both arms. |
| N026 | CHECKED—no discrepancy | Marital-status counts and percentages sum 303/305 and 100.0%. |
| N027 | CHECKED—no discrepancy | Relationship counts sum 303/306; percentages total 100.0%/100.0%. |
| N028 | CHECKED—no discrepancy | 257/302=85.10%→85.1%; 273/304=89.80%→89.8%. |
| N029 | CHECKED—no discrepancy | Income counts sum 304/306; percentages total 100.0% in both arms. |
| N030 | CHECKED—no discrepancy | Education counts sum 304/306; percentages total 100.0%. |
| N031 | CHECKED—no discrepancy | 71/303=23.43%→23.4%; 59/306=19.28%→19.3%; threshold is on stated 0–60 scale. |
| N032 | CHECKED—no discrepancy | Food-security counts sum 302/304 and each arm’s displayed percentages total 100.0%. |
| N033 | CHECKED—no discrepancy | Center-use categories sum 303/305 and percentages total 100.0%; dichotomization is stated. |
| N034 | CHECKED—no discrepancy | 36-month observed means/SDs agree in abstract, Key Points, Table/narrative, and DOC-003 eTable 1. |
| N035 | PRE-CANDIDATE NUM-P01 | Figure 2 counts agree with DOC-003 eTable 1, but differ from Figure 1’s counts described as BMI measured/retained; detailed below. |
| N036 | CHECKED—no discrepancy | Axis units and box-plot summary labels are coherent; no unprinted coordinate was inferred. |
| N037 | CHECKED—no discrepancy | Fitted trajectory/difference plot distinguishes model estimates from observed counts and gives consistent I−C direction/zero reference. |
| N038 | CHECKED—no discrepancy | Table 2 footnote model, BH family sizes, and original six-point center-use scale are labelled distinctly. |
| N039 | CHECKED—no discrepancy | One described event and no additional related events are count statements without conflicting denominator. |
| N040 | CHECKED—no discrepancy | Table 3 confirms obese 98/276=35.5% and 93/272=34.2%; adaptive counts are operational counts, not outcome denominators. |
| N041 | CHECKED—no discrepancy | Obesity cutoff, Poisson RR, and five-comparison BH correction distinguish rate/risk and count measures. |
| N042 | CHECKED—no discrepancy | Dose/fidelity percentages have distinct denominators/exposure phases and are not added or compared as counts. |
| N043 | CHECKED—no discrepancy | Food insecurity 42.6% matches baseline summary; other discussion figures are contextual and not a repeated outcome total. |
| N044 | CHECKED—no discrepancy | Conclusion contains no new numeric claim and is compatible with the reported primary result. |
| N045 | CHECKED—no discrepancy | Protocol eligibility age/BMI/language/data-validity conditions match the trial frame without changing the observed ITT count. |
| N046 | CHECKED—no discrepancy | 3×200=600; 100+100=200; 4×50=200. These are planned, versus observed 610, and are labelled as such. |
| N047 | CHECKED—no discrepancy | Protocol explicitly lists baseline plus 3,9,12,24,36 months; exposure arithmetic/control 12 quarterly sessions is coherent. |
| N048 | PRE-CANDIDATE NUM-P03 | Original protocol labels primary outcome BMI Percentile/BMI%, while final SAP/manuscript results specify BMI kg/m²; detailed below. |
| N049 | CHECKED—no discrepancy | Planned validity thresholds, kcal/day plausibility example, and different measurement schedules are labels/definitions, not conflicting results. |
| N050 | CHECKED—no discrepancy | 3×200=600; approximately 50/3=16.67 families/session and 600/16.67≈36; stated 54=18+36. Approximation is labelled. |
| N051 | CHECKED—no discrepancy | 0.80×200=160 and 3×160=480; planned mixed-model all-case statement is distinct from observed follow-up counts. |
| N052 | CHECKED—no discrepancy | Original/final power tables have identical displayed numeric cells; 0.4/90%=480 matches N011. |
| N053 | CHECKED—no discrepancy | Six occasions/three years and 600/480 planning thresholds are internally consistent; “about 20%” is approximate by label. |
| N054 | CHECKED—no discrepancy | Nadir formulas are symbolic only; no coefficients or numerical value are supplied to test. |
| N055 | PRE-CANDIDATE NUM-P02 | Final-SAP prose calls the schedule six time points but enumerates only five occasions, omitting 24 months; detailed below. |
| N056 | PRE-CANDIDATE NUM-P01 | 3-month eTable n=279/271 agrees with Figure 2 but conflicts with Figure 1 288/277 BMI-measured counts. |
| N057 | PRE-CANDIDATE NUM-P01 | 9-month eTable n=280/280 agrees with Figure 2 but conflicts with Figure 1 282/282 BMI-measured counts. |
| N058 | PRE-CANDIDATE NUM-P01 | 12-month eTable n=274/275 agrees with Figure 2 but conflicts with Figure 1 275/276 BMI-measured counts. |
| N059 | PRE-CANDIDATE NUM-P01 | 24-month eTable n=278/266 agrees with Figure 2 but conflicts with Figure 1 280/267 BMI-measured counts. |
| N060 | PRE-CANDIDATE NUM-P01 | 36-month eTable n=276/272 and Figure 2 n=276/272 conflict with Figure 1 278 retained/272 retained, whose caption defines retained as BMI collected. |
| N061 | CHECKED—no discrepancy | eFigure 1 is qualitative/model-estimated; axes/reference percentile curves do not supply numerical coordinate claims. |
| N062 | CHECKED—no discrepancy | eFigure 2 prints no effect, CI endpoints, denominator, or formula; no numerical reconciliation can be validly calculated. |
| N063 | CHECKED—no discrepancy | eFigure 3’s time and BMI axes, food-security labels, and model-estimated status are compatible with the moderation context; no unprinted value inferred. |
| N064 | CHECKED—cross-reference C010/C012 | DOC-002 p64 labels T1–T6/six points but lists seven occasions through 48 months (C010); its seven 45-minute control sessions imply 315 minutes (5.25 hours), the revised-protocol exposure component reconciled through C012. No new candidate created. |

## Pre-candidates requiring human adjudication

### NUM-P01 — BMI follow-up observation counts conflict across supplied result displays

**Sources and exact locations.** Main article Figure 1, [DOC-001 PDF p. 3](../../../jama_barkin_2018_oi_180075.pdf#page=3), prints intervention BMI measured 288, 282, 275, 280 at 3/9/12/24 months and 278 “Retained at 36 mo”; control 277, 282, 276, 267 and 272, respectively. Its caption says the retained number represents children “for whom BMI was collected.” Main-article Figure 2, [DOC-001 PDF p. 7](../../../jama_barkin_2018_oi_180075.pdf#page=7), prints 279/271, 280/280, 274/275, 278/266, 276/272. Supplement 2 eTable 1, [DOC-003 PDF p. 2](../../../joi180075supp2_prod.pdf#page=2), prints the same Figure 2 group counts.

**Rule, calculation, and tolerance.** For the same arm, time point, and labelled observed BMI quantity, repeated observation counts should be identical (integer tolerance 0) unless a source explicitly defines a distinct analytic subset. Differences (Figure 1 minus Figure 2/eTable 1) are intervention: +9, +2, +1, +2, +2; control: +6, +2, +1, +1, 0 at 3/9/12/24/36 months. Figure 1 itself arithmetically balances at every follow-up (measured + missing + cumulative permanent loss equals randomized total), so this is not an internal flow-sum error.

**Observation, inference, and alternatives.** The counts are directly printed. The contradiction is a direct repeated-label/count conflict for 3–36 months, strengthened by Figure 1’s caption. A possible alternative is that Figure 1’s “BMI measured/retained” count includes records not eligible for the Figure 2/eTable observed-BMI summaries (for example, an unstated cleaning/exclusion rule); no such definition was found in the supplied pages. This affects denominators underlying displayed observed BMI and obesity percentages, hence is quantitatively relevant.

**Human question.** What precisely distinguishes the Figure 1 counts described as BMI collected from the Figure 2/eTable 1 observed-BMI counts at each arm and visit, and should one display be corrected or annotated to state that distinction?

### NUM-P02 — Final SAP calls five enumerated occasions “6 time points”

**Sources and exact locations.** Final SAP, [DOC-002 PDF p. 110](../../../joi180075supp1_prod.pdf#page=110), says assessments occur “over 6 time points” and then enumerates baseline; 12 weeks/3 months; and 9, 12, and 36 months—five occasions. The protocol schedule, [DOC-002 PDF pp. 14–15](../../../joi180075supp1_prod.pdf#page=14), and eTable 1, [DOC-003 PDF p. 2](../../../joi180075supp2_prod.pdf#page=2), explicitly include 24 months, yielding baseline+3+9+12+24+36=6.

**Rule, calculation, and tolerance.** A stated count of visits must equal the distinct visits enumerated (integer tolerance 0): 1 baseline + 1 three-month + 3 later listed visits = 5, not 6. Adding 24 months makes 6.

**Observation, inference, and alternatives.** The missing 24-month item is directly observable in the final-SAP prose; the intended sixth point is an inference supported by two supplied documents. It may be an editorial omission rather than an analysis omission. It matters because the SAP defines the repeated-measures schedule/population used for its primary model.

**Human question.** Was 24 months intentionally included in the final analysis schedule, and if so should the final SAP’s enumerated schedule be amended to name it?

### NUM-P03 — Original-protocol primary-outcome label/scale differs from final analytic outcome

**Sources and exact locations.** Original protocol, [DOC-002 PDF p. 16](../../../joi180075supp1_prod.pdf#page=16), calls the primary outcome “child’s BMI Percentile” and “BMI%,” although its adjoining instrument row shows weight (kg)/height (m²). Final SAP, [DOC-002 PDF p. 110](../../../joi180075supp1_prod.pdf#page=110), calls the level-1 outcome time-varying BMI. The manuscript defines BMI as kg/m², [DOC-001 PDF p. 3](../../../jama_barkin_2018_oi_180075.pdf#page=3), and reports observed BMI values in kg/m²; eTable 1 likewise reports BMI values such as 16.7, 17.2, and 17.8, [DOC-003 PDF p. 2](../../../joi180075supp2_prod.pdf#page=2).

**Rule, calculation, and tolerance.** A primary outcome label must identify its scale. BMI percentile/BMI% and raw BMI kg/m² are noninterchangeable measures; this is a categorical label/scale check (no numerical rounding tolerance applies).

**Observation, inference, and alternatives.** The divergent labels/scales are direct observations. It is not established from the supplied packet whether the original wording was a nomenclature error, a pre-specified outcome change, or a transition to a different analysis specification; the final-SAP change summary does document model-test changes but does not resolve this label difference in the mapped evidence. The issue is relevant because the reported primary result’s scale determines its interpretation and comparability.

**Human question.** Does “BMI Percentile/BMI%” on the original protocol page mean raw BMI kg/m² in this study, or was the primary outcome scale changed; where is the authoritative clarification/amendment?

## Limitations

This lane did not invent numerical values from qualitative figures, treat planned values as observed results, or infer an error merely from a small/displayed-zero P value. Statistical calculations and cross-source candidate consolidation are assigned to separate lanes. The Figure 1 versus Figure 2/eTable denominator distinction cannot be resolved from supplied wording alone.

## N064 direct-source cross-reference (no new candidate)

**Source and printed inputs.** Revised protocol, [DOC-002 PDF p. 64](../../../joi180075supp1_prod.pdf#page=64), says “6-points in time (T1-T6)” and “six data collection points,” but lists baseline, 3, 9, 12, 24, 36, and 48 months. The same page states that intervention and control participants “will receive a 45-minutes school readiness/school success program during each of the 7 data collection points.”

**Count/list rule and calculation.** The seven distinct printed occasions give `count = 7`, not 6 (integer tolerance 0): baseline + 3 + 9 + 12 + 24 + 36 + 48 months. This is the exact direct-source basis already preserved under **C010**, not a separate candidate.

**Exposure rule and calculation.** The revised-protocol component implies `7 sessions × 45 minutes/session = 315 minutes = 5.25 hours` for each condition. This count-duration product is not equal to the other supplied descriptions of control exposure—original protocol `12 × 60 = 720 minutes` and article `6 × 30 = 180 minutes`—without a stated distinction between planned, ancillary, and delivered components. That cross-document issue is already preserved under **C012**; no additional candidate is registered here.

**Direct observation, alternative, and human question.** The count/list and duration inputs are directly printed; whether 48 months was an extra follow-up outside T1–T6, and whether the seven 45-minute programs were ancillary rather than the reported control exposure, cannot be resolved from p64 alone. Human adjudication should use the existing C010/C012 questions to identify the authoritative schedule and control-component accounting.
