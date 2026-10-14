# Numeric consistency review

Mandatory fresh numeric_consistency_reviewer, gpt-6.1-sol, reasoning medium. Complete scope: 233 stable N relationships across DOC-001 REPORT pages 1–11, DOC-003 REPORT pages 1–29, and DOC-002 PLAN pages 1–136. The scope and review contract were read completely. Only supplied sources, current source-linked maps, and raw reusable derivatives were consulted. No historical checker, candidate, screening, or report conclusions were read. Sources and reusable assets were preserved.

## Complete relationship assessment

Each assigned ID has an explicit NUMERIC_REVIEW_COMPLETE entry in these bounded assessment parts, incorporated into this checker:

- [Main assessment](parts/numeric-main.md): 87 relationships; all main counts, denominators, percentages, category totals, and matched numeric claims.
- [Support assessment](parts/numeric-support.md): 39 grouped relationships; every constituent table cell, all 97 site counts, and 222 explicit numerator/denominator/percentage cells, without sampling.
- [Remaining plan assessment](parts/numeric-plan.md): 107 relationships; all planned numeric definitions, populations, decision inputs, and version matches.

All 233 relationships are complete. The explicit support percentage cells pass half-unit interval arithmetic and the 0.05 relative-discrepancy threshold. Participant flow, subgroup partitions, and matched primary mortality counts reconcile. Detailed arithmetic is retained in the parts. Inferential methods are cross-linked to the S inventory for the independent statistical passes. One plan-internal decision-metric issue qualifies in this numeric lane.

## Findings

### F-NUM-001

**Title:** SAP pilot progression applies an adherence threshold to the fraction with protocol deviations.

**Compared locations and document roles:** All are PLAN content in the supplied protocol/SAP bundle. [Original SAP Table 1 and footnote, PDF page 95](../../../joi250042supp1_prod_1753377747.92525.pdf#page=95); [final SAP Table 1 and footnote, PDF page 118](../../../joi250042supp1_prod_1753377747.92525.pdf#page=118); [original SAP §3.2.2 continuation, PDF page 98](../../../joi250042supp1_prod_1753377747.92525.pdf#page=98). [Final protocol Table 2, PDF page 69](../../../joi250042supp1_prod_1753377747.92525.pdf#page=69) corroborates the definition based on settings adjusted according to protocol. Core numeric records: N4008 and N4014; companion statistical records: S4005 and S4010.

**Printed inputs:** Both SAP Table 1 copies label the row “Treatment adherence” and give Green ≥75% of cases, Amber 50–75%, and Red <50%. Their footnotes define the percentage using conservative-arm patients with one or more adjudicated protocol deviations. Original SAP page 98 defines patient-level adherence as having experienced no protocol deviation. Protocol page 69 describes cases whose ventilator settings or supplemental oxygen were adjusted according to protocol. Progression material states that all green permits unchanged progression, amber leads to amendment, and red stops the trial, subject to funder approval.

**Rule and calculation:** Let d be the fraction with at least one deviation among conservative participants. Patient-level adherence as defined on page 98 is a=1−d. Applying Green ≥0.75 to d implies a≤0.25; applying Green to adherence implies a≥0.75, or d≤0.25. Applying Red <0.50 to d implies a>0.50, reversing the adherence metric. These are complementary numerators on the same population. Display-precision interval and relative discrepancy are not applicable to this definitional conflict: the event definitions and inequalities are printed, and no observed pilot fraction is inferred. An illustrative a=.80, d=.20 would be Green by adherence and Red by the footnote definition; these are algebraic demonstration values, not trial data.

**Focus area:** D, planned decision rule; C, quantity-changing numerator definition.

**Proposed review domain:** plan_material.

**Proposed relationship type:** P_P. **All relationships:** P_P. Report adherence values merely corroborate the distinction and are not a conflicting relationship in this finding.

**Qualifying route:** Route B.

**Affected result or extracted value:** Internal-pilot adherence progression classification and the numerator a reader would extract when reproducing its ≥75%/50–75%/<50% decision rule.

**Why context does not resolve it:** This decision metric has contradictory explicit numerator definitions. The SAP table and footnote send increasing deviation frequency toward Green; the patient-level definition and protocol send increasing adherence toward Green. Both SAP copies retain the footnote. No disclosed amendment identifies an overriding numerator. The issue is in focus under D, leaves the applied metric unresolved, and changes the interpretation of a planned progression rule. An observed pilot result need not be supplied for this prospective decision rule to be in focus.

**Alternatives and missing definition:** The thresholds may have been intended for the fraction without deviation, while the footnote describes separately reported nonadherence. Alternatively the footnote may define a different pilot quantity, but its color-threshold direction and protocol counterpart then need clarification. The missing definition is which numerator was applied to progression thresholds. Neither the intended reading nor the actual pilot decision is adjudicated here.

**Exact human question:** Was the SAP pilot adherence percentage calculated from conservative participants with no adjudicated deviation or with at least one deviation, and which definition was used for Green/Amber/Red progression?

**Direct-source confirmation:** Source-linked CPU rasters of pages 95, 98, and 118 were visually inspected. The deviation footnotes and page 98 no-deviation definition are legible. The reusable page 121 image was also inspected; its final-SAP continuation does not repeat the page 98 sentence and is not cited as an independent definition. The two Table 1 footnotes are one repeated pattern and one finding.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-003 REPORT page 24 eTable 7 vs DOC-001 REPORT page 8 Table 2; N1017/N068 | Organ-support-free missing 1639 vs 16434−7327−7444=1663. Half-unit recomputed interval [1661.5,1664.5], printed interval [1638.5,1639.5], gap 22; relative discrepancy 22/1639=.01342≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 REPORT page 24 eTable 7 vs DOC-001 REPORT page 5 Table 1; N1017/N027 | Ethnic missing 1630 vs 16434−7340−7465=1629; half-unit intervals overlap. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 REPORT page 6 adherence; N059 | 526/1252=42.0128% vs 42.1%; recomputed interval [41.9561,42.0695], printed interval [42.05,42.15] overlap. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 REPORT pages 21–23 eTables 5/6; N1015/N1016 | Several mean differences vary by 0.1 from subtraction of rounded means, including 35.5 vs 62.6−27.2 and first-10 room-air 11.4 vs 37.3−26.0; all half-unit intervals overlap. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 REPORT page 22 eTable 6; N1016 | FiO2 labels include a percent sign while cells are fractions; the values and adjacent FiO2 definitions make the unit apparent without changing a printed digit. | NOTATION_OR_TYPOGRAPHY |
| DOC-003 REPORT page 27 eTable 10 vs page 21 eTable 5; N1020/N1015 | UK-ROX usual SpO2 95.2 vs overall 95.1; 95.2 also appears as the explicit conditional-on-oxygen value in eTable 5. This comparison does not change a primary or key secondary result. | PERIPHERAL_COMPARISON |
| DOC-002 PLAN pages 29/70/94/117 sample size; N2002/N3024/N4004 | 15444/.94=16429.8 vs 16500; allowing the 6% half-unit interval [.055,.065] gives inflated interval approximately [16342.3,16518.2], overlapping the target. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-002 PLAN site target 100 vs DOC-001 REPORT achieved 97; N1028/N2015/N001 | Planned vs achieved site count is administrative and does not change an analysis-population size or planned decision rule. | PERIPHERAL_COMPARISON |
| DOC-003 REPORT page 1 contents; N1001 | Contents titles for eTables 1–4 differ from actual captions; the actual tables identify their quantities, with no result reassigned by these pointers. | PERIPHERAL_COMPARISON |

Excluded-observation count: 9. Reconciled checks are retained in the assessment parts. No route A issue was screened out using a context or peripheral-comparison reason. No candidate IDs or adjudication dispositions were assigned.

## Limitations

No assigned scientific relationship remains uncovered. Individual participant data, exact unprinted curve ordinates, and some person-time denominators are unavailable; these were not reconstructed. PLAN extraction can omit lines, so source-image-confirmed maps and targeted visual checks control. The current mapper correction of the page 132 fallback bootstrap count to 1000 was acknowledged as a derivative transcription matter; it does not produce a supplied-source finding. Full statistical compatibility and planned-versus-reported model specifications also receive the separate mandatory specialist review.
