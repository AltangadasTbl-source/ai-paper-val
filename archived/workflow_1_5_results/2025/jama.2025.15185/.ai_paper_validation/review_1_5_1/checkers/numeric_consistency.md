# Numeric Consistency Check

## Scope and method

This independent numeric check covers the complete stable relationship inventory N001-N033. The direct authorities were `jama_engelter_2025_oi_250066_1761597796.45511.pdf` (DOC-001) and `joi250066supp3_prod_1761597796.4701.pdf` (DOC-004), checked against the current canonical extraction maps and mapper relationship parts. DOC-002/DOC-003 plan material, DOC-005 collaborator material, DOC-006 code supplement, and DOC-007 data-sharing statement contain no observed result table applicable to a numeric contradiction. Existing text was used as a locator; direct PDF page content was the authority.

Tolerance for printed counts and exact repeated estimates was 0. For one-decimal percentages, the accepted interval was the printed value plus or minus 0.05 percentage points after calculating `100*n/denominator`; for whole-number descriptive values, ordinary nearest-integer rounding was allowed. A display zero for a P value was not treated as a candidate.

## Per-relationship accounting

| ID | Checks applied and direct locations | Outcome |
|---|---|---|
| N001 | DOC-001 pp.1,5: `307 + 303 = 610`; Figure 1 repeats the same allocation. | PASS |
| N002 | DOC-001 p.1: `252/610*100 = 41.31%`, `28/610*100 = 4.59%`, and `582/610*100 = 95.41%`; all round to printed values. | PASS |
| N003 | DOC-001 pp.1,2,6: three occurrences give FMA medians/IQRs `68 (42-85)` levodopa and `64 (44-83)` placebo, with the same 0-100 scale/direction. | PASS |
| N004 | DOC-001 pp.1,5: deaths `11 + 17 = 28`; survivors `307-11=296`, `303-17=286`, and `296+286=582`; complete/imputed cases are `282+14=296` and `269+17=286`. | PASS |
| N005 | DOC-001 p.5: adherence `252/307=82.08%` and `244/303=80.53%`, both consistent with 82.1% and 80.5%. Therapy measures retain their stated session/hour units. | PASS |
| N006 | DOC-001 p.4/Table 1 and DOC-004 pp.10-11/eTable 1: sex, living-situation, and stroke-type category sums/percentages were checked. Sex sums are 307 and 303; living-situation sums are 307 and 303. The levodopa stroke-type count conflicts across the two direct tables; see QN001. Other count/percentage checks pass within rounding. | CANDIDATE_PROPOSAL QN001 |
| N007 | DOC-001 p.4/Table 1 and DOC-004 pp.10-11/eTable 1: mRS counts sum to arm denominators (`2+0+6+37+170+92=307`; `0+2+3+32+169+97=303`). Same-population NIHSS and onset-to-randomization values conflict across tables; see QN002-QN003. | CANDIDATE_PROPOSAL QN002-QN003 |
| N008 | DOC-001 p.3: planned `548` and 10% inflation to `610` are directionally/arithmetic-compatible (`548/0.90=608.9`, rounded up to 610); 3 months plus/minus 14 days and the 0-100 FMA definition are internally coherent. | PASS |
| N009 | DOC-001 p.3: stated component/range checks pass: 50 FMA items x maximum 2 = 100; upper 66 + lower 34 = 100. Direction labels distinguish PROMIS-29 domains from uniformly directed measures. | PASS |
| N010 | DOC-001 pp.1,6,7 and DOC-004 p.16: serious-event totals `126+129=255`; the main text's 255 events/177 participants is measure-consistent. Prespecified-event overall total is discrepant in DOC-004 p.17; see QN008. | CANDIDATE_PROPOSAL QN008 |
| N011 | DOC-001 p.6/Table 2 and DOC-004 p.16/eTable 5: serious-event arm totals agree (`126`, `129`; overall 255). Classification rows are not assumed mutually exclusive because nested labels and event classifications can overlap. In eTable 5, `28` participants died but `29` SAE outcomes say participant died; this can be explained by event-level versus participant-level counting, but the table does not state it explicitly. | UNRESOLVED (no proposal: measure-unit alternative prevents a direct contradiction) |
| N012 | DOC-001 p.6/Table 2: arm headers `79 + 67 = 146`, matching narrative 146. DOC-004 p.17/eTable 6 instead prints overall `n=145`, while its arm totals and each complete category distribution total 146; see QN008. | CANDIDATE_PROPOSAL QN008 |
| N013 | DOC-001 p.6 and DOC-004 p.15/eTable 4: unaffected/affected FMA, lower FMA, NIHSS, Rivermead, and mRS values are compatible after rounding and adjusted-versus-unadjusted distinction. Same endpoint/time/group records conflict for PROMIS-29, PROMIS-10, and PRAI numerator; see QN005-QN007. | CANDIDATE_PROPOSAL QN005-QN007 |
| N014 | DOC-001 p.6 and DOC-004 p.15: 5-week FMA means and the levodopa SD are compatible after whole-number rounding, but the placebo SD is not: detailed `25.20` rounds to 25 rather than the main-text 26; adjusted difference is distinct from the raw difference. See registered C007 (cross-source proposal QC006). | CANDIDATE_PROPOSAL QC006 / C007 |
| N015 | DOC-001 pp.1,7-8: `-0.90` is less than one point in absolute magnitude on the stated 100-point scale; CI crosses zero and P=.54 is consistent with “not statistically significant.” | PASS |
| N016 | DOC-004 pp.10-11/eTable 1: `303+307=610`; female `133+119=252`; arm/overall percentages are within the stated rounding interval. | PASS |
| N017 | DOC-004 p.10/eTable 1: age/BMI medians and IQR ordering are internally valid; no pooled median arithmetic was imposed. | PASS |
| N018 | DOC-004 pp.10-11/eTable 1: medical-history and vessel-location overall counts equal arm sums where categories are simple totals; multiple vascular territories are explicitly nonexclusive. Stroke ischemic/hemorrhagic arm values conflict with DOC-001 p.4; see QN001. | CANDIDATE_PROPOSAL QN001 |
| N019 | DOC-004 p.11/eTable 1: FMA component medians stay within 66/34/100 ranges; main/supplement affected-side FMA medians are compatible. NIHSS and onset-to-randomization fields conflict with DOC-001 p.4; see QN002-QN003. | CANDIDATE_PROPOSAL QN002-QN003 |
| N020 | DOC-004 pp.12-13/eTable 2: primary full analysis set `582` equals survivor total in DOC-001 p.5; modified ITT `551` equals complete cases `282+269`. | PASS |
| N021 | DOC-004 pp.12-13/eTable 2: estimand labels, populations, and endpoint definitions distinguish mean difference from win ratio. Estimand 4 is repeated with discordant upper CI bound; see QN004. | CANDIDATE_PROPOSAL QN004 |
| N022 | DOC-004 p.14/eTable 3: post hoc estimand 9 repeats the primary estimate and n=582 with the correct change-from-baseline label; estimands 10-11 use distinct populations/strategies. | PASS |
| N023 | DOC-004 p.15/eTable 4 and DOC-001 p.6: unaffected-side FMA raw means and whole-number narrative values are compatible; SMD/difference labels distinguish standardized and adjusted effects. | PASS |
| N024 | DOC-004 p.15/eTable 4 and DOC-001 p.6: affected-side upper/lower FMA, NIHSS, Rivermead, and mRS checks are compatible with rounding/adjustment. PROMIS and PRAI discrepancies are recorded under QN005-QN007. | CANDIDATE_PROPOSAL QN005-QN007 |
| N025 | DOC-004 p.16/eTable 5: `129+126=255`; severity rows total 255 and arm totals; outcome rows total 255 and arm totals. Death-row measure ambiguity is retained under N011. | UNRESOLVED (no proposal) |
| N026 | DOC-004 p.17/eTable 6: `67+79=146`; intensity rows `58+86+2=146`, outcome rows `1+29+116=146`, and relation rows `2+66+23+2+39+14=146`, all contrary to printed overall `n=145`. | CANDIDATE_PROPOSAL QN008 |
| N027 | DOC-004 p.18/eTables 7-8: interaction versus spline (3 df) labels are distinct and do not claim a new numeric result. | PASS |
| N028 | DOC-004 p.20/eFigure 1: threshold labels are internally coherent as eligibility definitions, not observed results. | PASS |
| N029 | DOC-004 p.22/eFigure 3: visual cumulative plot has no printed point values for reliable exact arithmetic. | UNRESOLVED (visual-only; no numeric proposal) |
| N030 | DOC-004 pp.23-24/eFigure 4: plotted directions and estimates visually accord with eTable 2. The title/legend say `FMA` while the x-axis says `FMMA points`; DOC-003 p.2 separately defines FMMA as the same assessment, but the local switch is unqualified. See QN009. | CANDIDATE_PROPOSAL QN009 |
| N031 | DOC-004 p.25/eFigure 5: center display pools centers with fewer than 50 recruitments; no exact plotted values are printed for a reproducible arithmetic test. | UNRESOLVED (visual-only; no numeric proposal) |
| N032 | DOC-004 p.26/eFigure 6: nonlinear spline display has no printed point estimates, and its model description is compatible with eTable 8. | UNRESOLVED (visual-only; no numeric proposal) |
| N033 | DOC-004 p.27/eFigure 7: legend definitions (death imputed as 0; intake/rehabilitation exclusion; FMA subgroup threshold) distinguish post hoc analyses. No printed graphical values allow an exact arithmetic comparison. | UNRESOLVED (visual-only; no numeric proposal) |

## Candidate proposals

### QN001 — Baseline index-stroke type count differs between main Table 1 and eTable 1

- **Direct locations:** DOC-001 [p.4](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4), Table 1; DOC-004 [pp.10-11](joi250066supp3_prod_1761597796.4701.pdf#page=10), eTable 1.
- **Printed inputs:** Main Table 1: levodopa ischemic `260 (84.7%)`, hemorrhagic `47 (15.3%)`; placebo `259 (85.5%)`, `44 (14.5%)`. eTable 1: levodopa ischemic `263 (85.7%)`, hemorrhagic `44 (14.3%)`; placebo `259 (85.5%)`, `44 (14.5%)`; overall `519 (85.1%)` and `91 (14.9%)`.
- **Rule/calculation:** Identically labelled randomized treatment-arm baseline stroke type should agree across two tables. Main levodopa `260+47=307`; supplement levodopa `263+44=307`; each is arithmetically possible, but ischemic differs by `+3` and hemorrhagic by `-3`. Exact repeated-count tolerance is 0.
- **Observation/inference:** Direct observation of discordant printed counts. The inference is that at least one presentation needs reconciliation; alternative explanation is an unstated recoding/analysis population, but neither table labels a different population.
- **Quality-control relevance:** Baseline stroke-type denominators and percentages feed trial-characteristic extraction and subgroup summaries.
- **Human question:** Which levodopa arm stroke-type counts (`260/47` or `263/44`) are correct for the randomized baseline population, and should either table state a different classification rule if one was used?

### QN002 — Reported time from stroke onset to randomization differs by several days across baseline tables

- **Direct locations:** DOC-001 [p.4](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4), Table 1; DOC-004 [p.11](joi250066supp3_prod_1761597796.4701.pdf#page=11), eTable 1.
- **Printed inputs:** Main Table 1, `Time from stroke onset to randomization, median (IQR), d`: levodopa `3.0 (2.0-5.0)`, placebo `3.0 (2.0-5.0)`. eTable 1, `Median time from stroke onset to randomization [IQR]`: overall `7 [5,10]`, placebo `8 [5,10]`, levodopa `7 [5-11]`; that supplement row does not visibly print a unit.
- **Rule/calculation:** Same labelled variable and baseline randomized arms should match under a common unit and derivation. If the supplement values are days, the arm medians differ by 4 days (levodopa `7-3=4`) and 5 days (placebo `8-3=5`), far beyond rounding tolerance.
- **Observation/inference:** Direct observation is the same variable wording with incompatible printed distributions. Calling the supplement values days, or invoking a different time origin/unit, is inferred because the supplement row omits the unit.
- **Quality-control relevance:** Timing after stroke is a trial eligibility/baseline characteristic and can materially change downstream interpretation of treatment timing.
- **Human question:** What unit, time origin, and data definition produced the supplement row, and which values/label should be corrected?

### QN003 — Baseline NIHSS is reported as incompatible summary statistics across Table 1 and eTable 1

- **Direct locations:** DOC-001 [p.4](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4), Table 1; DOC-004 [p.11](joi250066supp3_prod_1761597796.4701.pdf#page=11), eTable 1.
- **Printed inputs:** Main Table 1 reports NIHSS median (IQR): levodopa `7 (5-11)`, placebo `8 (5-10)`. eTable 1 labels the row `Median NIHSS at randomization [IQR]` but prints overall `8.2 (3.9)`, placebo `8.3 (3.8)`, levodopa `8.2 (3.9)`.
- **Rule/calculation:** A median-with-IQR field should use a median and interval, not a decimal central value with a parenthesized single value; if it is intended as mean (SD), it also conflicts in statistic/label with the same baseline measure in the main table. Exact summary-statistic label tolerance is 0.
- **Observation/inference:** Direct observation of differing statistic formats and central values. Alternative explanation: the eTable label may be wrong and values may be mean (SD), which would resolve only the formatting issue, not the need to distinguish summary methods.
- **Quality-control relevance:** NIHSS is a principal baseline severity measure; summary type and value affect comparability and evidence extraction.
- **Human question:** Are eTable 1 values `8.2 (3.9)`, etc., means (SDs) or another measure, and should the eTable label or the main/supplement values be reconciled?

### QN004 — Estimand 4 win-ratio CI upper bound differs within eTable 2

- **Direct locations:** DOC-004 [p.12](joi250066supp3_prod_1761597796.4701.pdf#page=12), eTable 2 narrative Results; DOC-004 [p.13](joi250066supp3_prod_1761597796.4701.pdf#page=13), eTable 2 Results table.
- **Printed inputs:** Narrative: odds ratio/win ratio `1.06 (95% CI, 0.86 to 1.25)`. Results table for Estimand 4: `1.06 [0.86 - 1.26]`.
- **Rule/calculation:** A repeated estimate for the same estimand must have identical printed CI endpoints; `1.25 != 1.26` (absolute difference `0.01`, exact duplicate tolerance 0).
- **Observation/inference:** Direct within-document repeated-value contradiction. Alternative is a one-hundredth transcription/rounding discrepancy; it remains unresolved which endpoint is authoritative.
- **Quality-control relevance:** CI endpoints are routinely abstracted into evidence syntheses and affect precision reporting.
- **Human question:** Is the Estimand 4 upper 95% CI bound 1.25 or 1.26, and which occurrence should be corrected?

### QN005 — Main text and eTable 4 disagree on PROMIS-29 group means

- **Direct locations:** DOC-001 [p.6](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), Secondary Outcomes; DOC-004 [p.15](joi250066supp3_prod_1761597796.4701.pdf#page=15), eTable 4.
- **Printed inputs:** Main: levodopa `66 (14)`, placebo `65 (14)`. eTable 4: levodopa `64.74 (14.33)`, placebo `65.11 (13.79)`.
- **Rule/calculation:** Whole-number rounding of eTable means gives levodopa `65` and placebo `65`, not `66` and `65`; `64.74` is 0.26 below 65 and 1.26 below 66. The raw eTable contrast `64.74-65.11=-0.37` agrees with the printed adjusted difference `-0.37`, strengthening the table’s internal alignment.
- **Observation/inference:** Direct same-endpoint, same-time, same-arm discrepancy. Alternative is an unstated different PROMIS-29 scoring transformation in the narrative; no such distinction is printed.
- **Quality-control relevance:** The sign and reported descriptive comparison can be abstracted as a secondary outcome.
- **Human question:** Which PROMIS-29 group means are intended, and if the narrative uses a different scoring scale, where is that scale/transform specified?

### QN006 — Main text and eTable 4 disagree on PROMIS-10 group means

- **Direct locations:** DOC-001 [p.6](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), Secondary Outcomes; DOC-004 [p.15](joi250066supp3_prod_1761597796.4701.pdf#page=15), eTable 4.
- **Printed inputs:** Main: `28 (6)` in both arms. eTable 4: placebo `29.87 (5.74)`, levodopa `30.04 (5.73)`.
- **Rule/calculation:** Whole-number rounding of eTable values is placebo `30 (6)` and levodopa `30 (6)`, not `28 (6)`. The eTable raw contrast `30.04-29.87=0.17` aligns with adjusted `0.18`, but the two-point main-text difference cannot be rounding.
- **Observation/inference:** Direct same-endpoint/time/group discrepancy. Alternative is an unstated distinct PROMIS-10 scoring approach, absent from the table/text.
- **Quality-control relevance:** Two-point descriptive values and scoring scale affect comparability of a patient-reported secondary outcome.
- **Human question:** Are the main-text `28 (6)` values or eTable 4 `29.87/30.04` values correct, and do they represent the same PROMIS-10 scoring scale?

### QN007 — Placebo PRAI no-improvement numerator differs between main text and eTable 4

- **Direct locations:** DOC-001 [p.6](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), Secondary Outcomes; DOC-004 [p.15](joi250066supp3_prod_1761597796.4701.pdf#page=15), eTable 4.
- **Printed inputs:** Main: levodopa `51/276 (18%)`, placebo `52/270 (19%)`. eTable 4: placebo `51 (18.89%) (n=270)`, levodopa `51 (18.48%) (n=276)`.
- **Rule/calculation:** eTable placebo `51/270*100=18.89%`, and levodopa `51/276*100=18.48%`, exactly as printed. Main placebo `52/270*100=19.26%` can round to 19% but differs in numerator by 1 from the eTable. Exact repeated numerator tolerance is 0.
- **Observation/inference:** Direct mismatch for the same assessment, time, treatment arm, and denominator. Alternative explanation is a different handling rule for one response, but no distinction is reported.
- **Quality-control relevance:** A count/denominator discrepancy can change event-rate extraction and pooled binary-outcome inputs.
- **Human question:** Is the placebo numerator 51 or 52, and if both reflect different missingness/response definitions, should those definitions and denominators be reported?

### QN008 — eTable 6 overall prespecified-adverse-event total is one lower than arms, categories, and main report

- **Direct locations:** DOC-001 [p.6](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), Table 2 and Adverse Events; DOC-004 [p.17](joi250066supp3_prod_1761597796.4701.pdf#page=17), eTable 6.
- **Printed inputs:** Main Table 2 headers: levodopa `n=79`, placebo `n=67`; narrative: `146` prespecified events. eTable 6 header: overall `n=145`, placebo `67`, levodopa `79`. eTable 6 intensity sums `58+86+2=146`; outcome sums `1+29+116=146`; drug-relation sums `2+66+23+2+39+14=146`.
- **Rule/calculation:** `67+79=146`, not 145. Every mutually exhaustive eTable 6 classification totals 146. Difference is `146-145=1`, tolerance 0.
- **Observation/inference:** Direct arithmetic and cross-document contradiction. The congruent arm/category/main totals make the printed overall `145` the apparent discordant field, but correction remains for human adjudication.
- **Quality-control relevance:** The overall adverse-event count is a safety denominator/input likely to be extracted independently of arm counts.
- **Human question:** Should eTable 6 overall `n` be 146, or is one event intentionally excluded from the overall count and, if so, why do all classifications total 146?

### QN009 — eFigure 4 switches locally from FMA to FMMA without qualification

- **Direct locations:** DOC-004 [p.23](joi250066supp3_prod_1761597796.4701.pdf#page=23), eFigure 4 title/legend/x-axis; DOC-003 [p.2](joi250066supp2_prod_1761597796.4701.pdf#page=2), SAP objective; DOC-001 [pp.1,3,6](jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1), FMA definitions/results.
- **Printed inputs:** eFigure 4 title/legend use `FMA`, while its x-axis says `Adjusted Mean Difference (FMMA points)`. The SAP separately defines `Fugl-Meyer Motor Assessment (FMMA)` for the same assessment.
- **Rule/calculation:** A figure should use one locally clear outcome abbreviation or qualify synonymous abbreviations; the local title/legend-to-axis switch is not explained.
- **Observation/inference:** Direct observation is the local FMA/FMMA switch. Typographic error is only one inference; intentional synonymous use is source-grounded by the SAP definition.
- **Quality-control relevance:** A measure-label defect can misidentify a graphical effect measure in downstream extraction.
- **Human question:** Is the local FMA/FMMA switch intentional, and should the figure use one abbreviation or define both locally?

## Limitations

The graphical eFigures 3 and 5-7 do not print exact point values, so their visual trends were not reverse-engineered into pseudo-precise calculations. No raw participant data were supplied. The eTable 5 death-row difference was not proposed because a credible event-versus-participant unit explanation remains, whereas QN001-QN009 each retain a direct printed inconsistency or a direct arithmetic failure.
