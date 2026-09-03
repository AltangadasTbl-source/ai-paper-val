# Cross-Source Quantitative Consistency Check

## Scope and method

Checked the complete mapped relationship inventories `N001`--`N033` and `S001`--`S021` against the supplied direct PDFs for DOC-001 through DOC-007. Reused extraction was used only to locate occurrences; printed values cited below were checked in the direct PDFs. A comparison was made only after matching the available population, time, contrast, measure, scale, unit, and (where applicable) model/estimand. Protocol and SAP statements were treated as planned definitions, not as observed-result duplicates.

Status meanings: `PASS` = matched occurrence(s) agree at their displayed precision; `UNRESOLVED` = no same-result comparator exists, or population/model/precision prevents a valid numerical comparison; `CANDIDATE_PROPOSAL` = a concrete printed inconsistency is documented below. These are proposals only and have no C ID or adjudication.

## Match-family completion record

| Inventory ID(s) | Checked match family and direct locations | Result |
|---|---|---|
| N001 | Randomization/allocation and dose: DOC-001 [p. 1](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1) versus p. 5/Figure 1 | PASS: 610, 307 levodopa, 303 placebo; 100/25 mg three times daily and 39-day treatment are consistently identified. |
| N002, N004 | Randomized baseline total, deaths, survivor primary-analysis total: DOC-001 pp. 1 and 5/Figure 1 | PASS: 28 deaths and 582/610 eligible (296/286 by arm); arm deaths 11/17 agree. |
| N003, N015, S001 | Primary 3-month FMA descriptive and adjusted result: DOC-001 pp. 1, 2, 6, 7, 8 and DOC-004 [p. 13](joi250066supp3_prod_1761597796.4701.pdf#page=13), [p. 23](joi250066supp3_prod_1761597796.4701.pdf#page=23) | PASS: descriptive medians 68 (42-85) versus 64 (44-83); matched primary estimand is -0.90 [-3.78, 1.98]. Narrative conclusion is consistent with that estimate. |
| N005 | Rehabilitation exposure and >=80% adherence: DOC-001 p. 5 and DOC-004 p. 13/eTable 2 estimand definitions | UNRESOLVED: eTable 2 uses the adherence threshold in a distinct on-treatment estimand but does not repeat the arm exposure/descriptive totals. |
| N006 | Baseline demographics, medical history, residence, and vessel territory: DOC-001 [p. 4](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4) Table 1 versus DOC-004 [pp. 10-11](joi250066supp3_prod_1761597796.4701.pdf#page=10) eTable 1 | CANDIDATE_PROPOSAL QC001 for stroke-type rows; remaining matched rows (allocation, sex, age, histories, residence, and listed vessel territories) PASS at displayed precision. |
| N007 | Baseline FMA, mRS, NIHSS, and onset-to-randomization time: DOC-001 p. 4/Table 1 and p. 5/Results versus DOC-004 pp. 10-11/eTable 1 | CANDIDATE_PROPOSAL QC002 (NIHSS) and QC003 (time); FMA and mRS values PASS. |
| N008, S009 | Primary scale/timing/sample-size plan: DOC-001 p. 3 versus DOC-002 pp. 8-10 and DOC-003 pp. 2-18 | UNRESOLVED: plans provide definitions rather than a same-result calculation with all inputs/versions needed for equality testing; no observed-result contradiction identified. |
| N009 | Outcome scale/range/direction definitions: DOC-001 p. 3 versus DOC-003 planned endpoint text and DOC-004 pp. 8-9, 15 | PASS where the same FMA/NIHSS/mRS definitions are repeated; PROMIS-29 direction is domain-specific, so no unsupported directional comparison was made. |
| N010-N012 | Serious and prespecified adverse-event totals/classifications: DOC-001 pp. 1, 6-7/Table 2 versus DOC-004 [p. 16](joi250066supp3_prod_1761597796.4701.pdf#page=16) eTable 5 and [p. 17](joi250066supp3_prod_1761597796.4701.pdf#page=17) eTable 6 | PASS for serious-event total 255 (126/129) and arm classification counts. CANDIDATE_PROPOSAL QC008 for prespecified-AE overall total. |
| N013, S003-S007 | Three-month secondary outcomes: DOC-001 [p. 6](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) versus DOC-004 [p. 15](joi250066supp3_prod_1761597796.4701.pdf#page=15) eTable 4 | CANDIDATE_PROPOSAL QC004 (PROMIS-29), QC005 (PROMIS-10), and QC007 (PRAI count). PASS for affected/unaffected FMA, NIHSS, Rivermead, and mRS displayed estimates after matching the indicated measure. The eTable mRS n=596 cannot be compared with the FMA full-analysis n=582 without an explicit analysis-set definition, so that denominator is UNRESOLVED rather than a proposal. |
| N014, S008 | Five-week FMA: DOC-001 p. 6 versus DOC-004 p. 15/eTable 4 | CANDIDATE_PROPOSAL QC006 for placebo SD. Mean and levodopa SD agree on ordinary displayed rounding. |
| N016-N019 | Detailed baseline supplement rows: DOC-004 pp. 10-11 versus DOC-001 p. 4-5 | CANDIDATE_PROPOSAL QC001-QC003 as above; all other repeated baseline rows PASS. |
| N020-N022, S010-S016 | Primary/post hoc estimand populations and effects: DOC-001 pp. 3-6 versus DOC-003 p. 2 and DOC-004 pp. 12-14/eTables 2-3 | PASS for primary treatment-policy estimand: survivors with imputed missing/incomplete FMA, n=582, -0.90 [-3.78, 1.98]. Other eTable 2/3 values are explicitly distinct estimands or post hoc analyses and do not constitute conflicting duplicates. |
| N023-N024, S017 | Secondary table effects: DOC-001 p. 6 versus DOC-004 p. 15/eTable 4 | CANDIDATE_PROPOSAL QC004-QC007 for the particular descriptive rows above; adjusted mean differences/intervals and matched secondary FMA effects PASS. |
| N025-N026 | Supplement safety-detail rows: DOC-004 pp. 16-17 versus DOC-001 pp. 6-7 | CANDIDATE_PROPOSAL QC008; serious-event rows PASS. |
| N027, S018 | Baseline-interaction and 3-df spline labels: DOC-001 pp. 4-5 versus DOC-004 p. 18/eTables 7-8 | PASS: the main text identifies post hoc nonlinearity/interaction checks without substituting one model for the other. |
| N028, S012 | Eligibility/timing definition: DOC-001 pp. 2-3 versus DOC-002 pp. 8-10, DOC-003 p. 2, and DOC-004 p. 20/eFigure 1 | PASS for acute stroke, <=7 days before randomization, clinically meaningful hemiparesis, and three-month primary time point. |
| N029 | Cumulative enrollment display: DOC-001 p. 5 versus DOC-004 p. 22/eFigure 3 | UNRESOLVED: the supplement plot does not print source-faithful site/time coordinates for numerical equality testing; no contradictory printed total was found. |
| N030, S019 | Eight FMA estimands/eFigure 4: DOC-001 p. 6 versus DOC-004 pp. 12-13/eTable 2 and pp. 23-24/eFigure 4 | PASS: visual direction and plotted primary point agree with eTable 2 and the main primary result; differing points represent named estimands. |
| N031 | Center display/eFigure 5: DOC-001 p. 5 versus DOC-004 p. 25 | UNRESOLVED: source has a graphical center-specific display, not a duplicate printed estimate for the main pooled result. |
| N032, S020 | Baseline-to-3-month spline/eFigure 6: DOC-001 p. 5 versus DOC-004 p. 26 | PASS for the stated nonlinear post hoc association and separate no-interaction conclusion; no exact graphical coordinate is printed for additional comparison. |
| N033, S021 | Post hoc/subgroup forest plot/eFigure 7: DOC-001 p. 5-6 versus DOC-004 p. 27 | PASS: death-imputed-zero, adherence/rehabilitation, and subgroup analyses are explicitly distinct post hoc analyses, not alternate prints of the primary result. |
| S002 | Primary linear-regression/two-sided 95% CI specification: DOC-001 p. 4 versus DOC-003 planned methods and DOC-004 pp. 6-7 | PASS: reported analysis description is compatible with the matched primary treatment-policy result; plan terminology alone is not treated as a numerical conflict. |
| S013-S014 | Software and multiple-imputation implementation: DOC-001 p. 5 versus DOC-004 pp. 6-7 | PASS: R 4.3.1 and 100 chained-equation imputations/Rubin rules agree. |

## Candidate proposals

### QC001 — Baseline stroke-type counts differ for the levodopa arm

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 [p. 4, Table 1](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4); DOC-004 [pp. 10-11, eTable 1](joi250066supp3_prod_1761597796.4701.pdf#page=10).
- **Matched identity:** randomized baseline population; levodopa arm, n=307; stroke type; count and percentage.
- **Printed values:** Main Table 1 prints levodopa ischemic `260 (84.7%)` and hemorrhagic `47 (15.3%)`. eTable 1 prints levodopa ischemic `263 (85.7%)` and hemorrhagic `44 (14.3%)`. The placebo values (`259`, `44`) and overall values (`519`, `91`) are the same across the two tables.
- **Reproducible rule:** For the same randomized arm and mutually exclusive stroke-type rows, the same count should print at both locations. Each table's levodopa rows separately total 307, but three participants are assigned differently between the two documents.
- **Supported alternatives:** a transcription/column error in either table; a source-specific classification update is possible only if an unstated different definition or data cut was used.
- **Human verification:** compare the source data/case classification for the three discrepant levodopa records and confirm which table is intended to carry the final stroke-type coding.

### QC002 — Baseline NIHSS summary conflicts between the main table and eTable 1

- **Category:** Cross-document numeric inconsistency and measure/label inconsistency.
- **Exact source locations:** DOC-001 [p. 4, Table 1](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4) and [p. 5, Results](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5); DOC-004 [pp. 10-11, eTable 1](joi250066supp3_prod_1761597796.4701.pdf#page=10).
- **Matched identity:** randomized baseline population; NIHSS at randomization; levodopa/placebo arms and overall descriptive summary.
- **Printed values:** Main Table 1 prints median (IQR) NIHSS `7 (5-11)` levodopa and `8 (5-10)` placebo; main Results prints overall median (IQR) `7 (5-10)`. eTable 1 labels its row `Median NIHSS at randomization [IQR]` but prints overall/placebo/levodopa `8.2 (3.9)`, `8.3 (3.8)`, and `8.2 (3.9)`.
- **Reproducible rule:** A median [IQR] is not expressed as a single value followed by a parenthetical single value; and these eTable arm values do not equal the main table's same-population median/IQR values. Matching cannot make `8.2 (3.9)` equal to `7 (5-11)` or `8 (5-10)` by ordinary precision rounding because the summary statistic/dispersion format differs.
- **Supported alternatives:** eTable 1 may contain means (SD) with a stale median/IQR label, or the documents may have used a different unreported derivation/data cut.
- **Human verification:** inspect the analysis dataset and eTable-generation code to determine whether `8.2 (3.9)` is mean (SD), then confirm the intended label and any reason for divergence from Table 1.

### QC003 — Baseline time from stroke onset to randomization differs

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 [p. 4, Table 1](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4); DOC-004 [p. 11, eTable 1](joi250066supp3_prod_1761597796.4701.pdf#page=11).
- **Matched identity:** randomized baseline population; time from stroke onset to randomization; days; placebo and levodopa arms.
- **Printed values:** Main Table 1 prints `3.0 (2.0-5.0)` days for each arm. eTable 1 prints overall `7 [5,10]`, placebo `8 [5,10]`, and levodopa `7 [5-11]`, but the supplement row does not visibly print a unit.
- **Reproducible rule:** Same named baseline time variable, population, and arms should not yield medians of 3 versus 7/8 under a common day unit and derivation; because the supplement unit is omitted, the comparison is conditional on confirming that unit.
- **Supported alternatives:** the supplement may use a different unit, onset date/interval, or data cut; no such distinction is stated in the row.
- **Human verification:** confirm the supplement unit, then trace the time-variable definition and raw timestamps used for both Table 1 and eTable 1.

### QC004 — Levodopa PROMIS-29 descriptive mean differs from eTable 4

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 [p. 6, Secondary Outcomes](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6); DOC-004 [p. 15, eTable 4](joi250066supp3_prod_1761597796.4701.pdf#page=15).
- **Matched identity:** 3-month PROMIS-29; levodopa versus placebo; mean (SD); same reported secondary-outcome comparison.
- **Printed values:** Main text prints levodopa `66 (14)` and placebo `65 (14)`. eTable 4 prints levodopa `64.74 (14.33)` and placebo `65.11 (13.79)`.
- **Reproducible rule:** At whole-number precision, `64.74` rounds to `65`, whereas the main levodopa mean is printed as `66`; the placebo values are compatible with `65 (14)`.
- **Supported alternatives:** a nonstandard undisclosed rounding rule or a source-specific analysis set/data cut; the eTable row prints n=582, the primary survivor analysis population.
- **Human verification:** reproduce the PROMIS-29 group summary from the final secondary-outcome analysis dataset and verify the main-text transcription/rounding policy.

### QC005 — PROMIS-10 descriptive means differ from eTable 4

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 [p. 6, Secondary Outcomes](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6); DOC-004 [p. 15, eTable 4](joi250066supp3_prod_1761597796.4701.pdf#page=15).
- **Matched identity:** 3-month PROMIS-10; levodopa versus placebo; mean (SD); same reported secondary-outcome comparison.
- **Printed values:** Main text says both groups had `28 (6)`. eTable 4 prints placebo `29.87 (5.74)` and levodopa `30.04 (5.73)`.
- **Reproducible rule:** At the main text's displayed whole-number precision, both eTable means round to `30` (with SD `6`), not `28`.
- **Supported alternatives:** documents may use different PROMIS-10 scoring/analysis versions or one location may be a transcription error; neither location states a different score scale for this comparison.
- **Human verification:** confirm the PROMIS-10 scoring transformation and analysis population used in each output, then reproduce both group summaries.

### QC006 — Placebo five-week FMA SD does not agree with the detailed table

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 [p. 6, Secondary Outcomes](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6); DOC-004 [p. 15, eTable 4](joi250066supp3_prod_1761597796.4701.pdf#page=15).
- **Matched identity:** affected-side FMA total at 5 weeks; placebo arm; mean (SD); n=582 table row.
- **Printed values:** Main text prints placebo `56 (26)`. eTable 4 prints placebo `56.27 (25.20)`; levodopa values are `57 (27)` and `57.37 (26.70)` respectively.
- **Reproducible rule:** Ordinary whole-number rounding of eTable placebo SD `25.20` is `25`, not the main-text `26`; its mean rounds to `56`.
- **Supported alternatives:** an undisclosed alternate SD convention, analysis set, or transcription error. The cited locations do not identify a different placebo population.
- **Human verification:** reproduce the placebo five-week FMA SD and confirm the rounding convention used for narrative results.

### QC007 — Placebo PRAI no-improvement count differs from eTable 4

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 [p. 6, Secondary Outcomes](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6); DOC-004 [p. 15, eTable 4](joi250066supp3_prod_1761597796.4701.pdf#page=15).
- **Matched identity:** patient-reported assessment of relevance of motor improvement (PRAI); 3 months; placebo arm; no/relevant improvement category; denominator 270.
- **Printed values:** Main text prints `52 of 270 (19%)` placebo participants. eTable 4 prints `51 (18.89%) (n = 270)` placebo participants. The levodopa result is `51 of 276` in both locations at their displayed precision.
- **Reproducible rule:** With the same named outcome and denominator, a numerator cannot be both 52 and 51. Also, 51/270 is 18.89%, while 52/270 is 19.26%.
- **Supported alternatives:** a narrative transcription error or a differently defined response category that is not stated in the two locations.
- **Human verification:** inspect the PRAI response coding and denominator-270 extract; confirm which placebo numerator belongs in the final report.

### QC008 — Prespecified adverse-event overall total conflicts with arm totals and eTable 6

- **Category:** Denominator, proportion, or total inconsistency; cross-document numeric inconsistency.
- **Exact source locations:** DOC-001 [p. 6, Table 2 and Adverse Events](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) and [p. 7](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=7); DOC-004 [p. 17, eTable 6](joi250066supp3_prod_1761597796.4701.pdf#page=17).
- **Matched identity:** prespecified adverse events of interest; event count (not participant count); entire study and treatment arms.
- **Printed values:** Main Table 2 and text print `146` events, `79` levodopa and `67` placebo. eTable 6 prints overall `n=145`, placebo `67`, levodopa `79`. Its intensity rows total 146 (`58+86+2`), and outcome rows total 146 (`1+29+116`); both arm totals are also 146 (`67+79`).
- **Reproducible rule:** An overall event total for the same two arms should equal `67 + 79 = 146`; the eTable's mutually exhaustive intensity and outcome totals also yield 146. Thus `n=145` cannot reconcile with the printed arm totals/rows and conflicts with the main report.
- **Supported alternatives:** an eTable overall-header typographical error is supported by the displayed arithmetic; a different event inclusion rule is not stated and would not explain both category sums without further source evidence.
- **Human verification:** trace the AE dataset/event IDs and eTable header generation; verify whether the intended overall count is 146 and whether any duplicate/categorization convention was applied.

## Limitations

DOC-002 protocol and DOC-003 SAP are plan documents. They were checked as definition/model comparators but do not supply a second observed-result table for most relationships. DOC-004 eFigures 3, 5, 6, and 7 are primarily graphical and do not print all coordinates; no numerical proposal was inferred from visual position. No display-zero P-value issue was observed or proposed.

**Completion count:** 24 match-family records covering all 33 numeric and 21 statistical inventory IDs; 8 distinct candidate proposals; 12 PASS records (including grouped pass families) and 4 UNRESOLVED records. All proposals remain pending human adjudication.
