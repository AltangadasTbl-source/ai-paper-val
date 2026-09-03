# Cross-source quantitative consistency check

## Scope and matching rule

This checker reviewed the complete current evidence union: the main article (DOC-001), protocol (DOC-002), SAP (DOC-003), TIDieR supplement (DOC-004), results supplement (DOC-005), and workbook (DOC-006). It used the current main and support evidence maps plus the numeric inventory N001 through N036 and statistical inventory S001 through S109. Direct supplied files remain the authority; extracted text was used as a locator.

A value was compared only when population, visit/time, outcome construct and scale, arm/reference contrast, analysis set, model/adjustment state, and displayed precision were compatible. A protocol/SAP target or superseded plan, an unadjusted or sensitivity analysis, a missingness-pattern cohort, and a pairwise versus omnibus P value are not the same result as an adjusted primary-analysis display and were recorded as not comparable rather than as differences.

## Provisional cross-source consistency candidates for human verification

These are source-grounded observations only. They have no stable candidate IDs and remain pending human adjudication.

### Provisional observation A — Female total differs between the article and supplied workbook

- **Exact source locations:** [main article, PDF p. 1](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=1), Abstract Results; [main article, PDF p. 6](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=6), Table 1, Sex; [workbook](../../../joi250046supp5_prod_1755300121.16087.xlsx), worksheet `eTable 3`, cells A11:B11.
- **Printed values:** the abstract states `1712 [74%] women`. Table 1 prints female counts PT `571/776`, HC `572/778`, and UC `569/777`; their count sum is `1712`. The workbook prints `1713 (73.5)` for Female in its Overall column (N=2331).
- **Matching rationale/rule:** all three locations report a female count/percentage for the randomized overall trial population (N=2331), and Table 1's arm counts sum to the abstract count. Like-for-like comparability is conditional: Table 1 footnote b specifies self-report with EHR fallback, whereas workbook row 11 is footnoted as EHR-derived. If these derivations are intended to represent the same variable, the counts should agree.
- **Calculation:** `571 + 572 + 569 = 1712`; `1712 / 2331 = 73.444873...%` (73.4% to one decimal). The workbook's `1713 / 2331 = 73.487773...%` (73.5% to one decimal). The count differs by one and the one-decimal percentages also differ under standard rounding.
- **Supported alternatives:** the two printed derivation rules may intentionally define different variables; the workbook may also reflect a data update or inclusion rule not otherwise stated.
- **Human verification steps:** inspect the underlying participant-level sex derivation/version used for workbook cell B11 and Table 1; confirm whether one participant's survey/EHR sex value was revised after Table 1 production; confirm the intended published count.
- **Provenance:** main N001/N014; support-005 DOC-006 `eTable 3` A11:B11; numeric inventory N001, N009, and N031-N035.

### Provisional observation B — Narrative depression percentage differs from its displayed numerator/denominator records

- **Exact source locations:** [main article, PDF p. 4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), Results baseline summary; [main article, PDF p. 6](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=6), Table 1, moderate to severe depression; [workbook](../../../joi250046supp5_prod_1755300121.16087.xlsx), worksheet `eTable 3`, cells A82:B82.
- **Printed values:** the narrative says `47.8% had current depression`, defined as PHQ-8 score at least 10. Table 1 prints PT `373/775 (48.1)`, HC `373/777 (48.0)`, and UC `370/777 (47.6)`. The workbook prints `1116 (47.9)` for Current depression (PHQ-8 >=10), Overall.
- **Matching rationale/rule:** all locations use the same PHQ-8 >=10 definition and randomized cohort baseline; Table 1's applicable nonmissing denominators sum to 2329 and its event counts sum to 1116, which is the workbook numerator.
- **Calculation:** `373 + 373 + 370 = 1116`; `775 + 777 + 777 = 2329`; `1116 / 2329 × 100 = 47.9176%`, displayed as `47.9%` at one decimal. This does not reproduce the narrative `47.8%` at the same stated one-decimal precision.
- **Supported alternatives:** the prose might use a different unprinted denominator or a more precise source value. The Table 1 and workbook display two missing values and supply no alternative numerator/denominator that produces 47.8% under the stated PHQ-8 definition.
- **Human verification steps:** confirm the numerator and denominator used to generate the narrative sentence; determine whether a pre-table data snapshot or an unprinted weighting/rounding convention was used; confirm the intended one-decimal percentage.
- **Provenance:** main N010/N017/N018; support-005 DOC-006 A82:B82; numeric inventory N012 and N033.

### Provisional observation C — painTRAINER 3-month pain-severity SMD differs in narrative and Table 3

- **Exact source locations:** [main article, PDF p. 7](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=7), Secondary Outcomes narrative; [main article, PDF p. 10](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, Pain severity, 3 months, painTRAINER vs usual care plus SMD.
- **Printed values:** the narrative states `3-month SMD, −0.26` for painTRAINER versus usual care plus. Table 3 prints `−0.25` with 95% CI `−0.28 to −0.02` in the same contrast column.
- **Matching rationale/rule:** both explicitly identify standardized effect size of change in pain severity at 3 months, painTRAINER versus usual care plus, under the Table 3 adjusted analysis. The narrative expressly cites Table 3.
- **Calculation:** direct value comparison at two decimal places: `−0.26 ≠ −0.25`; absolute displayed difference `0.01`.
- **Supported alternatives:** a less-rounded internal estimate could yield one of the two printed values only if the locations used different rounding/output versions; no different population, model, scale, or reference group is printed. The CI's internal compatibility is a separate numerical issue and is not used as the cross-source rule here.
- **Human verification steps:** check the Table 3 source output and narrative source output for the painTRAINER-versus-usual-care 3-month SMD; verify intended estimate and associated CI before choosing a correction.
- **Provenance:** main S005/S007 and S018; statistical inventory S011 and S032.

### Provisional observation D — Health-coach 3-month pain-severity SMD differs in narrative and Table 3

- **Exact source locations:** [main article, PDF p. 7](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=7), Secondary Outcomes narrative; [main article, PDF p. 10](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, Pain severity, 3 months, health coach versus usual care plus SMD.
- **Printed values:** the narrative states `3-month SMD, −0.36` for health coach versus usual care plus. Table 3 prints `−0.34` with 95% CI `−0.36 to −0.13` in the same contrast column.
- **Matching rationale/rule:** both explicitly identify standardized effect size of change in pain severity at 3 months, health coach versus usual care plus, under the Table 3 adjusted analysis. The narrative expressly cites Table 3.
- **Calculation:** direct value comparison at two decimal places: `−0.36 ≠ −0.34`; absolute displayed difference `0.02`.
- **Supported alternatives:** different rounding or source-output versions may explain the difference, but neither location prints a distinct population, model, scale, time, or reference group. The Table 3 CI is not used to infer this cross-source observation.
- **Human verification steps:** check the health-coach-versus-usual-care 3-month SMD source output and the narrative drafting source; verify the intended estimate and CI.
- **Provenance:** main S005/S007 and S018; statistical inventory S011 and S032.

## Explicit matched-result passes

| Matched result family | Exact source locations and printed comparison | Result |
|---|---|---|
| Randomized allocation and assessment counts | Main abstract p1: total 2331, PT 776/HC 778/UC 777; main Figure 1 p5 and supplement eTable 1 p7 give the same analysis allocation. Follow-up at 3/6/12 months is UC `621/622/639`, PT `542/547/583`, HC `635/621/639` in main Figure 1 p5/Figure 2 p8 and DOC-005 pp4/7. | PASS: exact count agreement. |
| Primary outcome definition | Main p3/Table 2 p9, protocol pp13/19/56, current SAP pp20-21, and DOC-005 p2: >=30% decrease from baseline in overall 11-item BPI-SF pain severity, primary 3-month visit, with PT/HC versus UC comparisons. | PASS: population/construct/time/contrast labels agree. |
| Outcome scale labels | Main p3 and DOC-005 p2: overall BPI-SF 11 items, intensity 4, interference 7, each 0-10 and higher worse; main p3 and DOC-005 p2: PROMIS social-role/physical-function T scores, mean 50/SD 10, higher better, <=40 limitation. | PASS: exact definitions and direction agree. |
| Randomization and adjustment framework | Main pp3-4; protocol p56; SAP p17 and pp20-21: individual 1:1:1 allocation, strata sex/baseline pain/site/rural-underserved, modified Poisson GEE for binary MCID, 3/6/12-month interactions, and stated adjustment variables. | PASS: compatible current-plan/method record. |
| Main adjusted primary RRs replicated in results supplement | Main Table 2 p9 versus DOC-005 eTable 4 p9: 3-mo PT-UC `1.28 (1.06-1.55)`, HC-UC `1.54 (1.30-1.82)`, HC-PT `1.20 (1.03-1.40)`; 6-mo `1.44 (1.21-1.70)`, `1.62 (1.39-1.90)`, `1.13 (0.98-1.30)`; 12-mo `1.32 (1.13-1.54)`, `1.41 (1.25-1.59)`, `1.07 (0.96-1.19)`. | PASS: all 9 matched adjusted RRs/CIs agree exactly. |
| Main abstract/narrative/figure/Table 2 3-month primary display | Main abstract p1, Results p4/p7, Figure 2 p8, Table 2 p9: PT `26.6 (23.4-30.2)`, HC `32.0 (29.3-35.0)`, UC `20.8 (18.0-24.0)`; corresponding RRs above. | PASS: exact matched values. |
| Main narrative/Table 2 6- and 12-month primary display | Main narrative p7 and Table 2 p9: pain-severity adjusted percentages PT/HC/UC at 6 months `32.9/37.1/22.9` and at 12 months `35.9/38.3/27.1`, with the Table 2 RRs. | PASS: matched narrative/table values agree. |
| Any-follow-up analysis set | Main Table 2 p9 and Table 3 pp10-11: PT/HC/UC `643/690/703`; DOC-005 p7: at least one follow-up `643/690/703`, total 2036; DOC-005 p9 estimator: 2036 persons/6108 observations. | PASS: the three group counts sum to 2036 and identify the same observed-follow-up pool. |
| Baseline workbook quantities that share the same overall definition | Main Table 1/narrative and workbook: mean age `58.8`; rural/underserved `1030` (44% main; 44.2% workbook); pain severity >=7 `594 (25.5%)`; moderate/severe anxiety `648 (27.8%)`; sleep disturbance `1005` (43.3%); long-term opioid use `163` (9.6%, three-site qualifier). | PASS after stated rounding and missing/three-site denominator rules. |
| Protocol/TIDieR intervention dose definitions | Protocol pp13/43 and TIDieR pp2-4: eight active sessions over at most 12 weeks; main Figure 1 p5 and TIDieR p5 both identify 776 painTRAINER-assigned participants where applicable. | PASS: compatible matching definitions; no same-cell efficacy result. |

## Explicit non-comparable records (not candidates)

| Relationship family | Why not comparable under the matching rule |
|---|---|
| Protocol target enrollment 2380 and randomization target 2331; earlier SAP target 1368/456 per arm | These are dated planning/target populations, not the same achieved enrollment/result display. Main observed randomized population is 2331. |
| Earlier SAP primary endpoint at 6 months versus current protocol/SAP/main primary endpoint at 3 months | The SAP amendment/history explicitly documents plan changes. These are different planned time-point versions, not competing displays of one observed result. |
| Main adjusted Table 2/3 values versus DOC-005 eTables 9-11 unadjusted analyses | eTables 9-11 explicitly state no adjustment, weighting, or imputation; their n/N and unadjusted GEE estimates therefore do not match the adjusted primary-analysis estimand/model. |
| Main primary values versus eTable 7 missing-data sensitivity values and eTable 8 enhancement/reminder subsets | Complete-case, extreme-assumption, pre/post-enhancement, and reminder-letter restrictions use different analysis sets/assumptions. |
| Main treatment-group baseline Table 1 versus workbook missingness-pattern columns | Workbook columns partition outcome-observation patterns (missing all, missing 1/2, all observed), not randomized treatment arms. |
| Main omnibus P values versus eTable 4 pairwise P values; workbook P columns | They test different stated hypotheses/selection relations. No same-test comparator is printed. |
| Supplementary model coefficients, imputation/weight diagnostics, fidelity/outreach quantities, planned economics/mediation/safety definitions | No duplicate matched result is printed in the main article at the same population/time/contrast/model/measure. These were inspected as standalone or definition records. |
| Figure 1’s 2333 randomized versus 2331 primary-analysis eligible randomized | Figure 1 explicitly identifies two usual-care participants randomized in error and excluded for EHR ineligibility; the figures label different populations. |

## Relationship-level completion record

The following completion record is intentionally exhaustive. `MATCHED_PASS` means at least one same-result cross-source comparison was made and passed. `MATCHED_OBSERVATION_RECORDED` refers only to the provisional observations above. `NO_MATCHED_COMPARATOR` means that the source unit was inspected but did not print another result meeting every matching key; it is not a negative finding about the source.

| Inventory IDs | Cross-source completion status |
|---|---|
| N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014 | MATCHED_PASS except N001/N009 include provisional observation A; N012 includes provisional observation B. All other inspected same-result occurrences passed or were governed by stated denominator/rounding rules. |
| N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027 | MATCHED_PASS for current definitions/methods; historical targets and superseded timing are explicitly non-comparable above. |
| N028, N029, N030 | NO_MATCHED_COMPARATOR: DOC-005 eTables 9-11 are expressly unadjusted; their same-outcome main-table records are adjusted and do not meet the model/analysis-set key. |
| N031, N032, N033, N034, N035 | MATCHED_PASS for the workbook/main quantities listed above, with provisional observations A and B retained; remaining workbook cells are missingness-predictor or baseline descriptive records without a same-result article comparator. |
| N036 | NO_MATCHED_COMPARATOR: direct-source administrative/no-applicable support units. |
| S001, S002, S003, S004, S005, S006, S007, S008, S009, S010 | S001 MATCHED_PASS for current model conventions; S002-S004 MATCHED_PASS against eTable 4; S005-S010 NO_MATCHED_COMPARATOR because available supplement binary displays are unadjusted or sensitivity/subset analyses. |
| S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032 | S011 contains provisional observations C and D through the explicit Table 3 narrative citation. S012-S031 have no same-model supplementary continuous-result comparator; S032 otherwise MATCHED_PASS for qualitative/table linkage. |
| S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061 | MATCHED_PASS where current protocol/SAP/main method/definition records share the same current definition; NO_MATCHED_COMPARATOR for historical-plan-only or planned-method-only records. No observed-result contradiction was found after distinguishing plan version and result. |
| S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106 | NO_MATCHED_COMPARATOR: these are eTables 9-11 unadjusted outcome estimates. Each was checked against the corresponding main outcome only after confirming the printed unadjusted/no-imputation/no-weighting qualifier; therefore no adjusted-main comparison was made. |
| S107, S108, S109 | NO_MATCHED_COMPARATOR: workbook cached/displayed P values and bolding/no-formula metadata have no same-test/same-model repeated source display. Display precision, including threshold notation, was not treated as a candidate. |

## Limitations

- DOC-002 and parts of DOC-003 have font-encoding limitations; their direct rendered pages and current evidence maps were used for definition/model matching, not legacy conclusions.
- DOC-005 p3 has a histogram caption without reusable bin-level transcription. No bin-level article comparator was printed, so it does not create an unresolved matched-result comparison.
- This stage does not reclassify internal arithmetic, interval, or label defects that are not a cross-source comparison; those remain within the numeric/statistical check scopes.
