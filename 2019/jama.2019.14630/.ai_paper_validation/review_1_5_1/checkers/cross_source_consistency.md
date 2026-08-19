# Cross-source consistency check

## Scope and method

This check covered every result-relevant quantitative or statistical occurrence mapped for DOC-001 through DOC-005: the main article’s abstract, Key Points, narrative, Tables 1-3, Figures 1-4 and captions; the protocol and SAP definitions; all eTables 1-9 and eFigures 1-3 in the results supplement; and the data-sharing statement. The direct PDFs were the authority. Current mapping artifacts were used only as locators. No legacy candidate, checker, verifier, critic, or report artifact was read.

Each proposed comparison was first matched on analysis population, time point, treatment contrast, model or missing-data handling, measure, scale/unit, reference group, and displayed precision. Planned protocol/SAP quantities were not treated as comparators for observed 12-month estimates unless the source identified the same result. Differences attributable to a stated sensitivity analysis, a completer-only population, a different missing-data procedure, a graphical-only display, or ordinary displayed rounding are recorded as nonmatches rather than candidates.

## Coverage and counts

- Direct sources checked: 5 of 5 (149 PDF pages).
- Cross-location result families checked: 31 (participant flow and analysis sets; baseline table; four diet scores; 22 food rows; 13 nutrient rows; 11 risk-factor rows; Figure 4 proportions; three eFigures; protocol/SAP definitions and plans).
- Coherent matched-result comparisons recorded: 26 families.
- Defined nonmatches excluded from direct comparison: 12 families.
- Visual-only relationships with no truthfully printable comparator value: 3 eFigure families.
- Preliminary qualifying candidates: 6.

All items below are preliminary quality-control candidates, not stable candidate IDs and not adjudications.

## Qualifying preliminary candidates

### QC-X0001 — eTable 2 labels the N=3,311 column as a second intervention group

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-004, PDF p. 3, Supplemental eTable 2](../../../joi190106supp3_prod_1635377898.49725.pdf#page=3); [DOC-001, PDF p. 5, Table 2](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5); [DOC-004, PDF p. 5, Supplemental eTable 2 continuation](../../../joi190106supp3_prod_1635377898.49725.pdf#page=5).
- **Printed values and labels:** On DOC-004 p. 3, the two eTable 2 headers read “Intervention group, N=3,272” and “Intervention group, N=3,311.” The p. 3 values use the two columns as treatment arms. The continuation on p. 5 prints the corresponding N=3,311 header as “Control group.” DOC-001 Table 2 also labels N=3,311 “Control Group.”
- **Comparison logic:** The arms have the same stated all-randomized population, food measures, time points, and between-group contrast. N=3,311 is explicitly the control arm in the main table and in the eTable continuation. Thus the first page’s repeated “Intervention group” label is not compatible with the matched arm identity.
- **Supported source-grounded alternatives:** The first-page label may be a single header typographical error; the numerical columns and subsequent continuation could still have been analysed correctly. This check does not infer a numerical effect-estimate error.
- **Human verification steps:** Inspect the formatted DOC-004 p. 3 header and the original table-production file if available; confirm whether the N=3,311 values are the control group and, if so, whether the header should read “Control group.”

### QC-X0002 — all-randomized red-wine baseline medians disagree across eTables 2 and 7

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-004, PDF p. 7, Supplemental eTable 2](../../../joi190106supp3_prod_1635377898.49725.pdf#page=7); [DOC-004, PDF p. 19, Supplemental eTable 7](../../../joi190106supp3_prod_1635377898.49725.pdf#page=19).
- **Printed values:** eTable 2, headed “MULTIPLE IMPUTATION: ALL RANDOMIZED PARTICIPANTS,” gives red-wine baseline median (IQR), g/week, as intervention `33 (0, 29)` and control `4 (0, 29)` (N=3,272 and N=3,311). eTable 7, headed “ALL RANDOMIZED PARTICIPANTS. Replacing all missing values with baseline value,” gives the same baseline row as `0 (0, 29)` for both arms with the same N=3,272 and N=3,311.
- **Comparison logic:** This is the same baseline food measure, unit, randomized analysis-set headers, treatment arms, and displayed IQR endpoints. Changing follow-up missing-data handling cannot itself change a baseline median when the stated group Ns and baseline measure are unchanged. In addition, eTable 2’s intervention median `33` exceeds its printed upper IQR endpoint `29`, which is not compatible with the standard ordering of a median within its IQR.
- **Supported source-grounded alternatives:** The eTable 2 `33` may be a transcription/printing error (for example, a misplaced digit), or the eTable 7 baseline may have been recalculated using an unstated baseline subset despite its identical N header. The supplied PDFs do not specify a distinct baseline subset.
- **Human verification steps:** Reproduce the two baseline summaries from the analysis dataset using the stated all-randomized N=3,272/N=3,311 groups; verify the intended treatment-column label on eTable 2 p. 3; then determine which red-wine medians and IQRs were supplied to table production.

### QC-X0003 — PDQS baseline mean is 21.1 in the principal table and 21.0 in the all-randomized baseline-value-carried-forward table

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-001, PDF p. 5, Table 2](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=5); [DOC-004, PDF p. 16, Supplemental eTable 6](../../../joi190106supp3_prod_1635377898.49725.pdf#page=16).
- **Printed values:** Main Table 2 reports the PDQS baseline mean (SD) as `21.1 (3.7)` in both the intervention N=3,272 and control N=3,311 groups. eTable 6, whose header gives those same arm Ns and states that missing values were replaced with baseline values, reports `21.0 (3.7)` in both arms.
- **Comparison logic:** The group Ns, baseline time point, score name/range (PDQS 0-42), and arm identity match. The printed baseline means differ at the displayed one-decimal precision. The main article states that its multiple imputation was used for follow-up data, not baseline data (DOC-001 p. 4), so no supplied statement explains why the baseline score itself would differ between these all-randomized displays.
- **Supported source-grounded alternatives:** The underlying unrounded mean could be near a rounding boundary and have been rounded under different conventions, or eTable 6 may use a baseline subset/handling rule not stated in its title or footnote. Neither alternative is documented in the supplied sources.
- **Human verification steps:** Confirm the PDQS baseline calculation and rounding convention for each arm in the analysis output; establish whether either table applied a baseline-data exclusion or imputation rule not printed in the PDFs.

### QC-X0004 — baseline intervention energy-intake SD differs between main Table 3 and all-randomized eTable 8

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-001, PDF p. 7, Table 3](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=7); [DOC-004, PDF p. 21, Supplemental eTable 8](../../../joi190106supp3_prod_1635377898.49725.pdf#page=21); [DOC-001, PDF p. 4, Statistical Analysis](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4).
- **Printed values:** Main Table 3 reports intervention baseline total energy, mean (SD), as `2355 (555)` kcal/d for N=3,272; the matched control value is `2369 (555)` for N=3,311. eTable 8 reports the same all-randomized group Ns and baseline mean as `2,355 (544)` kcal/d for intervention, while retaining control `2,369 (555)`.
- **Comparison logic:** Population, treatment group, baseline time point, unit, and displayed precision match. The main article explicitly says imputed missing values were used for follow-up data but not baseline data. eTable 8’s stated sensitivity procedure replaces missing values with baseline values; it does not state a different baseline population. Therefore `SD 555` and `SD 544` for the same intervention baseline summary do not reconcile as rounding.
- **Supported source-grounded alternatives:** eTable 8 may have used an unstated analysis subset or a separate baseline calculation, or one SD may be a table-production error. The control SD agrees across the two locations, which does not resolve the intervention discrepancy.
- **Human verification steps:** Recalculate the intervention baseline energy SD for all 3,272 participants and inspect the eTable 8 generation output; confirm whether a distinct baseline eligibility filter was applied only to the intervention column.

### QC-X0005 — baseline body-weight summaries differ between the main baseline table and eTable 9 despite the same displayed analysis Ns

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-001, PDF p. 4, Table 1](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4); [DOC-004, PDF p. 23, Supplemental eTable 9](../../../joi190106supp3_prod_1635377898.49725.pdf#page=23).
- **Printed values:** Main Table 1, “Participants Included in the Main Analyses,” reports baseline weight mean (SD), kg, as intervention `86.7 (13.0)` and control `86.4 (13.0)` for N=3,272/N=3,311. eTable 9’s “MULTIPLE IMPUTATION: all randomized participants” panel, carrying exactly N=3,272/N=3,311, reports `86.5 (12.9)` and `86.3 (13.0)`, respectively.
- **Comparison logic:** Both displays name the same two post-exclusion arm Ns, baseline time point, measure, unit, and treatment-arm comparison. Each intervention mean and the intervention SD differs at displayed precision; the control mean differs by 0.1 kg. Neither source prints a distinct baseline population for the two matched N headers.
- **Supported source-grounded alternatives:** eTable 9 could use an unstated baseline risk-factor availability/imputation set while retaining the overall arm N in its header. Its multiple-imputation footnote may be relevant, but it does not state that baseline weight values were imputed or that a different baseline subset was summarized.
- **Human verification steps:** Determine the exact nonmissing/imputed baseline weight denominator in eTable 9, compare it with Table 1’s denominator, and regenerate both summaries from the documented analysis datasets before choosing which printed values, if either, require correction.

### QC-X0006 — baseline BMI summaries differ between the main baseline table and eTable 9 despite the same displayed analysis Ns

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-001, PDF p. 4, Table 1](../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4); [DOC-004, PDF p. 23, Supplemental eTable 9](../../../joi190106supp3_prod_1635377898.49725.pdf#page=23).
- **Printed values:** Main Table 1 reports baseline BMI mean (SD), kg/m², as intervention `32.5 (3.4)` and control `32.5 (3.5)` for N=3,272/N=3,311. The matched all-randomized multiple-imputation panel of eTable 9 reports intervention `32.6 (3.4)` and control `32.6 (3.5)`.
- **Comparison logic:** Population header, group Ns, baseline time point, scale/unit, and arm assignment match. The means differ by 0.1 kg/m² in both arms at the displayed one-decimal precision, while the SDs agree. The sources provide no distinct baseline analysis-set definition that accounts for the differing means.
- **Supported source-grounded alternatives:** eTable 9 may summarize a differently handled or imputed baseline BMI value set despite printing the same arm Ns, or one display may use a different rounding/derivation convention. The PDFs do not identify either convention.
- **Human verification steps:** Verify whether BMI was recomputed from rounded or unrounded height/weight values in either table; confirm eTable 9’s exact baseline BMI denominator and imputation handling; reproduce both group means before deciding whether an editorial correction is warranted.

## Coherent matched results

The following matched families were checked and were coherent at their printed precision.

- **Primary diet score:** Abstract, Key Points, Table 2, primary-outcome narrative, and eFigure 1 agree on the intervention/control context; the exact 12-month Table 2 values are intervention change `4.7 (3.5)`, control `2.5 (3.4)`, and adjusted difference `2.2 (2.1 to 2.4), P<.001`. eTable 3 and eTable 6 are explicitly different sensitivity analyses and were not expected to reproduce that principal value.
- **Dietary-score labels and ranges:** DOC-001 Table 2 and DOC-004 eTables 1, 3, and 6 consistently identify er-MedDiet 0-17, MDS 0-9, MEDAS 0-14, and PDQS 0-42; higher scores indicate higher dietary quality/adherence.
- **Main narrative versus principal food table:** refined grains (`−309`, 95% CI `−340 to −277`), pastries (`−49`, `−59 to −39`), red meat (`−39`, `−51 to −28`), vegetables (`210`, `157 to 263`), fruits (`197`, `118 to 276`), and nuts (`35`, `27 to 43`), all g/week at 12 months, agree between DOC-001 pp. 6-8 and DOC-004 eTable 2. The same selected rows were confirmed against their units, direction, and P values.
- **Main narrative versus principal nutrient table:** baseline energy values and the 12-month difference `−102 kcal/d (−129 to −75), P<.001`; carbohydrate difference `−1.4% (−1.8 to −1.0)`; and MUFA difference `0.9% (0.6 to 1.2)` agree between DOC-001 Table 3/narrative and their matching principal-analysis values. eTables 5 and 8 use stated completer-only and baseline-value-carried-forward sensitivity approaches, respectively, so their different follow-up contrasts are defined nonmatches.
- **Main risk-factor narrative versus eTable 9 principal panel:** waist baseline `108 cm` in both arms and 12-month difference `−3.3 cm (−3.6 to −2.9), P<.001`; and systolic blood pressure baseline control `139`, intervention `140` mm Hg and difference `−1.9 (−2.7 to −1.1), P<.001` agree. These matches do not eliminate the separate baseline weight and BMI discrepancies above.
- **Figure 4:** all 11 risk-factor proportions, thresholds, and P values are internally coherent with the stated percentage/threshold labels. No supplemental display claims to be the same Figure 4 percentage analysis.
- **Participant flow and denominators:** DOC-001 Abstract, Figure 1, Results, Tables 1-3, and the matching all-randomized supplement tables agree on 6,874 randomized; 3,406/3,468 allocated; 3,272/3,311 in the main analyses; and 2,862/2,883 at 6 months and 2,833/2,943 at 12 months for the stated dietary completer sensitivity analyses. eTable 9’s separate risk-factor completer counts (2,840/2,946) are a different outcome-specific availability set, not a mismatch with the food/nutrient completer tables.
- **Protocol/SAP and main article definitions:** both planned documents and the article agree on the eligibility age/BMI bands, centre/sex/age randomization stratification, couple clustering, score ranges, longitudinal assessment timing, and the distinction between a 6-year cardiovascular-outcome trial and this 12-month interim adherence analysis. The protocol/SAP sample-size targets, interim boundaries, clinical thresholds, and planned models are not observed 12-month effect estimates and do not conflict with them.
- **Figures and captions:** eFigure 1’s score direction/ranges and P-value labels agree with score-table interpretation. eFigure 2 is explicitly a percentage-compliance display and eFigure 3 explicitly uses baseline-SD units; neither is confused with a count or raw-unit table in the main article.

## Defined nonmatches and limitations

- DOC-002 protocol and DOC-003 SAP contain planned/historical sample sizes, session schedules, intervention quantities, and model wording. They were compared as definitions, not as direct numerical comparators for the observed results. For example, the protocol’s planned free-nut provision of `500 g` at group sessions and the article’s actual free almond allotment of `125 g/mo` plus a recommended total nut intake of `500 g/mo` describe different delivery/recommendation constructs and do not supply a matched observed-outcome estimate.
- Completer-only eTables 3-5 and the risk-factor completer panel in eTable 9 have population-specific denominators; their differences from principal all-randomized estimates are not cross-source conflicts. Baseline-value-carried-forward eTables 6-8 state a different missing-follow-up handling and therefore their 6- and 12-month contrasts are not direct comparators to multiple-imputation contrasts.
- DOC-004 eFigures 1-3 and DOC-001 Figures 2-3 contain graphical trajectories/distributions without a complete set of printed point estimates or coordinates. Their readable labels, scales, units, and P-value descriptors were checked, but graphical marker coordinates were not invented as numerical comparisons.
- DOC-005 contains no result-relevant quantitative relationship. No supplied structured data, workbook, CSV, or protocol/SAP observed-outcome table exists.
- No candidate was created from `P<.001` or other finite-precision P-value display alone.

## Human review follow-up

The six entries above require direct comparison with the source analysis outputs or table-production files. The supplied PDFs establish the printed discrepancies and source-grounded alternatives, but they do not establish the intended replacement value or the mechanism that produced any discrepancy.
