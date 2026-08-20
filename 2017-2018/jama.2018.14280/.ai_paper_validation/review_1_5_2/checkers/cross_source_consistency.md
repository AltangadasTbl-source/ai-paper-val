# Cross-source consistency review

## Scope and matching rule

This independent lane reviewed every fresh mapped relationship in the canonical numeric inventory (`N001`–`N047`) and statistical inventory (`S001`–`S038`) against the supplied direct sources only: the main article (DOC-001), protocol (DOC-002), SAP/amendments (DOC-003), supplementary results (DOC-004), and data-sharing statement (DOC-005). It also checked the main article's abstract, narrative, Tables 1–2, Figure 1, Figure 2, captions, and footnotes.

A printed difference was treated as comparable only after matching population, analysis set, time point, arm contrast, effect measure, direction, model, unit, reference group, and displayed precision. Protocol/SAP quantities were treated as planned values unless an unresolved contradiction with a final reported value remained after amendment matching. Display-zero P values and `---` P cells were not treated as candidates.

## Complete matched-key coverage

| Canonical relationships checked | Source/result scope and matching outcome |
|---|---|
| N001–N006 | DOC-001 enrollment, flow, allocation, site/date and randomization quantities. Allocation and flow sums reconcile; the end-date cross-document comparison is recorded as XF004. |
| N007–N011 | Intervention targets, PBW scale, VFD definition, power, and global analysis rules. Final primary-model change is explicitly documented by DOC-003 amendment material; no additional unresolved planned-versus-final candidate. |
| N012–N020 | DOC-001 Table 1 demographic, baseline, category-total, ventilation, and measurement-unit rows. Group/time distinctions were preserved. Header-to-percentage denominator discrepancies are recorded as XF003. |
| N021–N035 | DOC-001 primary/secondary outcomes, abstract/narrative/Table 2/Figure 2 repetitions, risk sets, subgroup result, and discussion on-treatment summary. Repeated compatible results agree at displayed precision; the subgroup interval label is recorded as XF001. Curve risk sets were not compared with allocation or outcome denominators unless the curve's analysis population matched. |
| N036–N039 | DOC-002/DOC-003 planned sample size, ventilation definitions, VFD definition, and ARDS thresholds. Five versus six planned/final centers and planned method changes are not candidates because the sources identify planned versus final material or do not state an incompatible final result. |
| N040–N046 | DOC-004 eTables 1–5 and eFigures 1–4. All-mode and mode-stratified results were compared only at the same timepoint/mode/measure; count percentages were recalculated from stated denominators where supplied. The invalid printed eTable 2 interval is recorded as XF002; eTable 4 percentage/denominator display is recorded as XF005. |
| N047 | DOC-005 was confirmed to contain no applicable numeric result. |
| S001–S007 | DOC-001 primary VFD, stay, mortality and survival-model comparisons. Mean differences, risk ratios, hazard ratios, and curve quantities were not interchanged; the final paper's t-test primary analysis matches the SAP amendment. |
| S008–S023 | DOC-001 binary secondary, subgroup, longitudinal, and global P-value relationships. Reported repeated statistics agree at printed precision except the interval-type inconsistency recorded as XF001. |
| S024–S030 | DOC-002/DOC-003 planned analyses, model changes, and amendments. These are planned-versus-final comparisons and were not registered solely for a plan change. |
| S031–S038 | DOC-004 eTable/eFigure and DOC-005 statistical relationships. `<.001`, `1.00`, `NA`, and `---` displays were handled according to their stated/compatible meanings; no candidate was based solely on finite display precision. |

Coverage count: **47/47 numeric/reporting relationships and 38/38 inferential-statistical relationships checked.**

## Qualifying cross-source or matched-result candidates

All items below are **Pending Human Adjudication**. They are quality-control candidates, not corrections, severity assessments, or validity judgments.

### XF001 — Main-paper subgroup intervals labeled IQR while the matching supplement labels them 95% CI

- **Exact locations:** [DOC-001 PDF p. 6, Results](../../../jama_simonis_2018_oi_180108.pdf#page=6); [DOC-004 PDF p. 9, eTable 5](../../../joi180108supp3_prod.pdf#page=9).
- **Matched population/time/contrast/model:** VFD at day 28, low minus intermediate tidal volume, subgroups defined by intubation inside versus outside the ICU; the table labels its estimate as mean difference and its interval column as `Mean Difference (95% CI)`.
- **Printed values:** DOC-001 states inside ICU `mean difference, −2.50 [IQR, −4.63 to −0.36]` and outside ICU `1.45 [IQR, −0.52 to 3.43]`, with `P for interaction = .01`. DOC-004 eTable 5 prints the same point estimates and bounds, `−2.50 (−4.63 – −0.36)` and `1.45 (−0.52 – 3.43)`, under `Mean Difference (95% CI)` and gives interaction P `.01` for the intubation-location modifier.
- **Comparison logic:** Same subgroup definitions, outcome, contrast, estimates, bounds, and P value match; only the interval measure label differs. A mean-difference uncertainty interval with the supplied eTable 5 heading is a 95% CI, whereas the main narrative calls identical bounds an IQR.
- **Supported alternatives:** The main-paper `IQR` label is a typographical label error; or the eTable heading does not describe this row. The latter is less directly supported because eTable 5 uses one explicit interval heading for all rows.
- **Human verification question:** Confirm in the analysis output whether these subgroup bounds are 95% confidence intervals and, if so, whether DOC-001 should say `95% CI` rather than `IQR`.

### XF002 — eTable 2 prints an impossible ordering for an IQR bound

- **Exact location:** [DOC-004 PDF p. 6, eTable 2](../../../joi180108supp3_prod.pdf#page=6), Other Mode of Ventilation, after titration on the day of randomization, intermediate tidal-volume column, PEEP row.
- **Matched population/time/contrast/measure/unit:** Other-mode ventilation stratum; after titration on randomization day; PEEP in cm H2O; intermediate arm. The table footnote defines the continuous displays as median (interquartile range).
- **Printed value:** `8 (5 – 1)`, P=`0.50`.
- **Comparison logic:** In a median (IQR) display, the lower bound must not exceed the upper bound. The printed lower bound 5 exceeds upper bound 1 (`5 > 1`), while the median is 8. This is an internal displayed numeric inconsistency; no inferred replacement value is asserted.
- **Supported alternatives:** One of the two printed bounds is a transcription/typesetting error; or the dash/bound characters were rendered incorrectly in the source PDF. The fresh layout text and direct PDF display both preserve `8 (5 – 1)`.
- **Human verification question:** Check the analysis table/source data for this intermediate-other-mode PEEP cell and establish the intended IQR bounds without substituting a value from another cell.

### XF003 — Table 1 percentages for several categorical rows do not use the printed randomized arm totals and no alternate denominators are displayed

- **Exact location:** [DOC-001 PDF p. 5, Table 1](../../../jama_simonis_2018_oi_180108.pdf#page=5), headed low `n = 477` and intermediate `n = 484`.
- **Matched population/time/contrast/measure:** Baseline randomized-arm categorical characteristics, printed as `No. (%)`, before randomization. No different analysis set or variable-specific denominator is printed in the table or its footnotes.
- **Printed values and calculations:** Tobacco categories total 475 in the low arm and 482 in the intermediate arm; for example low never-use `106 (22.3)` gives `106/477 × 100 = 22.2%`, while `106/475 × 100 = 22.3%`. Intermediate never-use `111 (23.0)` gives `111/484 × 100 = 22.9%`, while `111/482 × 100 = 23.0%`. Alcohol categories total 475 low and 482 intermediate; ICU-admission categories total 475 low and 482 intermediate. For the latter, low surgical `82 (17.3)` corresponds to `82/475 = 17.3%`, not `82/477 = 17.2%`; intermediate surgical `79 (16.4)` corresponds to `79/482 = 16.4%`, not `79/484 = 16.3%`.
- **Comparison logic:** The table explicitly presents arm headers of 477 and 484 but several category blocks use smaller, unstated denominators or have category totals below those headers. This prevents a reader from determining the analysis denominator for each printed percentage from the article.
- **Supported alternatives:** These rows intentionally exclude patients with missing baseline data and need variable-specific denominators/footnote disclosure; or some percentages/counts were rounded or transcribed inconsistently. This candidate does not infer that missingness itself is erroneous.
- **Human verification question:** Obtain the intended denominator and missing-data count for each Table 1 categorical block, then verify the displayed percentages against that denominator and add a disclosure if appropriate.

### XF004 — Final enrollment end date differs between main paper and SAP

- **Exact locations:** [DOC-001 PDF p. 1, Abstract](../../../jama_simonis_2018_oi_180108.pdf#page=1) and [DOC-001 PDF p. 5, Results](../../../jama_simonis_2018_oi_180108.pdf#page=5); [DOC-003 PDF p. 3, abstract](../../../joi180108supp2_prod.pdf#page=3) and [DOC-003 PDF p. 5, introduction](../../../joi180108supp2_prod.pdf#page=5).
- **Matched population/time/measure:** Same PReVENT trial enrollment period, reported as a calendar end date rather than a planned statistical method.
- **Printed values:** DOC-001: recruitment/enrollment ran from September 1, 2014, **through August 20, 2017**. DOC-003: `Enrollment of patients was complete on **August 22, 2017**.`
- **Comparison logic:** Both sources purport to report completion of enrollment for the same trial; dates differ by two calendar days. DOC-003 does not frame this statement as a pre-enrollment target or a planned date, and the amendment table does not resolve the discrepancy.
- **Supported alternatives:** One source uses the last randomization date while the other uses a later administrative completion date; one printed date is inaccurate; or the SAP was finalized with a different operational date. Supplied sources do not define the distinction.
- **Human verification question:** Verify the trial randomization/enrollment log and clarify which operational event each date denotes; align or qualify the public reporting accordingly.

### XF005 — eTable 4 counts and percentages conflict with its displayed arm denominators

- **Exact location:** [DOC-004 PDF p. 8, eTable 4](../../../joi180108supp3_prod.pdf#page=8), headed low `n = 477` and intermediate `n = 484`; table footer says data are `number / total (%) or median (interquartile range)`.
- **Matched population/time/contrast/measure:** Co-interventions during the first three ventilation days, low versus intermediate randomized arms. No alternate denominator is printed for sedative infusion, analgesic infusion, neuromuscular blockade, or vasopressor use.
- **Printed values and calculations:** Low sedative infusion `320 (70.6)` is `320/477 = 67.1%`; intermediate `333 (72.1)` is `333/484 = 68.8%`. Low analgesic infusion `277 (61.1)` is `58.1%` of 477; intermediate `273 (59.1)` is `56.4%` of 484. Low neuromuscular blockade `53 (11.7)` is `11.1%` of 477; intermediate `60 (13.0)` is `12.4%` of 484. The displayed percentages are broadly compatible with unstated denominators near 453 and 462, but those totals are not printed for these rows.
- **Comparison logic:** Unlike blood-product rows in the same table, which explicitly print `number / total (%)` (for example `100 / 454 (22.0)`), these rows show a count and percentage that cannot be reconciled with the only displayed arm totals and omit a variable-specific total.
- **Supported alternatives:** The intended denominators are patients with complete three-day treatment information and were inadvertently omitted; the table headers should not be used as denominators for these rows; or one or more counts/percentages is incorrect. No replacement denominator is asserted.
- **Human verification question:** Confirm the denominator for each affected eTable 4 row and report it explicitly, then recalculate/reconcile the printed percentages.

## Non-candidates and limitations

- Abstract, narrative, Table 2, and Figure 2 repetitions matched where they describe the same endpoint and estimand. ICU/hospital stay mean differences and Kaplan-Meier hazard ratios were retained as different estimands, not compared as conflicting values.
- The protocol's five-center description, planned Cox primary analysis, and pre-final outcome set were not candidates by themselves: DOC-003 amendment material documents analytic changes and the supplied sources do not establish a remaining final-result contradiction from those planned descriptions.
- DOC-004 mode-stratified values were not compared with all-mode values without matching mode and time; eFigures 1–4 do not provide a compatible printed numeric estimate beyond the mapped labels/axes.
- This review is limited to supplied PDFs and their fresh native/layout/rendered assets. It does not determine intended source values, correction status, severity, or study validity.
