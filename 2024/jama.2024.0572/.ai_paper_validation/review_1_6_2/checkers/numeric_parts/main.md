# Main numeric consistency review

Scope: DOC-001, REPORT, all 14 physical PDF pages and all relationships N001–N120. All 120 records were checked, including every table row, figure stratum, outcome count and matched abstract/body occurrence. Administrative/reference pages 12–14 contain no additional result relationship. Review uses the complete scope and review contract, current mapping, direct Poppler source extraction and reusable page images 5, 7 and 9. No legacy scientific conclusions were used. Inferential test reconciliation is separately assigned to the statistical reviewers; numeric containment and direction were checked here.

## Findings

### F-NUM-001

**Title:** Follow-up MRI analysis-population count does not reconcile between report locations.

**Compared locations and document roles:** REPORT DOC-001 [physical p. 4, Results, final baseline-imaging sentence](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4); REPORT DOC-001 [physical p. 9, Association of Follow-Up Infarct Volume and Infarct Growth](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9); REPORT DOC-001 [physical p. 11, discussion of MR diffusion follow-up](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=11). Relationships N019 and N113; both compared locations are within the same REPORT, proposed relationship S_W.

**Printed inputs:** p. 4 states, “Follow-up imaging modality was MRI in 8 of 336 patients (2%) and CT in 328 of 336 patients (98%).” p. 9 explicitly identifies patients with “MR diffusion follow-up (n = 204 [61%])” for infarct-growth analysis. p. 11 describes MR diffusion follow-up as comprising two-thirds of the population. The total analysis population is 336.

**Rule and calculation:** A follow-up MRI subgroup of 204 cannot be contained in a total follow-up MRI group of 8 under the same modality/time-point definition. Counts 8 and 204 have half-unit intervals [7.5, 8.5] and [203.5, 204.5], respectively: minimum gap 195 patients, relative discrepancy 195/8 = 24.375. Percentage copies 2% and 61% have intervals [1.5, 2.5] and [60.5, 61.5]: gap 58 percentage points, relative discrepancy 58/2 = 29. Allowing count and denominator half-units gives 8/336 a percentage range [100×7.5/336.5, 100×8.5/335.5] = [2.229, 2.534]% and 204/336 [100×203.5/336.5, 100×204.5/335.5] = [60.475, 60.954]%. The internal count/percentage pairs individually reconcile; the conflict is between populations labeled follow-up MRI.

**Focus area:** A, analysis-population size and matched imaging count.

**Proposed review domain:** statistical_results.

**Qualifying route:** Route B.

**Affected result or extracted value:** The size and modality composition of the follow-up MRI population used for infarct-growth results, including the medians 68, 95 and 125 mL in the p. 9 analysis.

**Why context does not resolve it:** Both locations explicitly say follow-up imaging. The p. 9 analysis population exceeds the p. 4 total MRI follow-up count by 196 patients. This changes the population size for a reported analysis, so the comparison is not peripheral. The source does not distinguish separate follow-up windows or alternative modality definitions that reconcile the counts.

**Alternatives and missing definition:** Table 1 p. 5 baseline MR DWI counts are 3 + 5 = 8, which may suggest that p. 4 refers to baseline rather than follow-up imaging, but that is an inferred explanation; its printed temporal label remains follow-up. Alternatively, distinct follow-up acquisitions or subsets could have been intended, but no such count definition is supplied at the compared locations. The p. 11 approximate fraction corroborates a substantially larger follow-up group and is not separately registered.

**Exact human question:** Which acquisition time point and MRI population does the p. 4 count 8/336 represent, and how should it be reconciled with the p. 9 MR diffusion follow-up population of 204?

### F-NUM-002

**Title:** Large-core EVT outcome proportions in the discussion do not reconcile with the printed mRS distribution.

**Compared locations and document roles:** REPORT DOC-001 [physical p. 7, Figure 2B, EVT core ≥100 mL, n = 51](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7); REPORT DOC-001 [physical p. 10, Discussion, paragraph beginning “EVT benefit in ordinal analysis”](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=10). Relationships N073 and N117. Proposed relationship S_W.

**Printed inputs:** Figure 2B displays percentages 2, 6, 10 and 20 in the mRS 0, 1, 2 and 3 categories of the EVT ≥100-mL group. Its mRS 5 and 6 segments show 10 and 53; the legend-color-defined mRS 4 segment is absent, not printed as a numeral zero. The discussion describes the core ≥100-mL EVT population as approximately 80% having mRS 4 or worse and says “1 in 5 patients still achieved independent ambulation after EVT.” Independent ambulation is explicitly mRS 0–3 (p. 3 and Table 2).

**Rule and calculation:** The printed mRS 0–3 segments sum to 2 + 6 + 10 + 20 = 38%, whereas one in five represents 20%. Allowing every whole-percentage input ±0.5 gives [36, 40]%. A whole-percentage 20 has [19.5, 20.5]%; minimum gap is 15.5 percentage points, relative discrepancy 15.5/20 = 0.775. Conversely, the complement of mRS 0–3 gives 62% mRS ≥4 with interval [60, 64]%, versus the 80% interval [79.5, 80.5]%; gap 15.5 percentage points, relative discrepancy 15.5/80 = 0.19375. Summing the two visible mRS 5–6 segments gives 63%, compatible with 62% after independent rounding. It does not approach 80%. The broad word “approximately” supplies no quantitative alternative interval; ordinary whole-percentage precision leaves a substantial conflict.

**Focus area:** A, primary mRS outcome distribution and derived functional-outcome threshold.

**Proposed review domain:** statistical_results.

**Qualifying route:** Route B.

**Affected result or extracted value:** The 90-day outcome distribution and independent-ambulation proportion among EVT patients with core ≥100 mL, specifically whether mRS 0–3 is about 20% or about 38% and mRS ≥4 about 80% or about 62%.

**Why context does not resolve it:** The figure and discussion identify the same core threshold and EVT population. The difference changes the extraction and interpretation of the primary mRS outcome distribution; it is not merely a peripheral secondary time-point comparison. Figure legend colors and caption identify categories, and the definition of independent ambulation is explicit. The 18-percentage-point difference exceeds the precision rule. The two complementary percentages are one repeated pattern, consolidated here.

**Alternatives and missing definition:** Figure 2 is intention-to-treat, while “received EVT” in the discussion could refer to as-treated classification. The report describes only two MM-to-EVT crossovers; such a change cannot explain a reduction from about 38% to about 20% in a 51-person stratum without additional unreported population changes. Another possibility is a different core-volume threshold or outcome cut point, but neither is stated in the discussion sentence. No alternative is adopted as a correction.

**Exact human question:** Which population, core-volume threshold and mRS cut point underlie the discussion’s approximately 80% mRS ≥4 and one-in-five independent-ambulation statements, and how do they reconcile with Figure 2B?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p. 5 Table 1, coronary artery disease; N033 | Header n168 gives 39/168 = 23.214% vs 23.5% and 25/168 = 14.881% vs 15.4%. Even treating counts as exact, gaps after the printed ±0.05% interval are 0.236/23.5 = 0.0100 and 0.469/15.4 = 0.0305; allowing count/denominator half-units only reduces them. Both are below 0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p. 5 Table 1, tenecteplase, thrombolytics and anesthesia; N053, N054 | Tenecteplase is nested in thrombolytic recipients, not all168 participants: 4/33 = 12.121% vs12.5% and 1/28 = 3.571% vs3.7%; residual relative gaps are below0.05 even with exact counts. Anesthesia100/168 =59.524% vs59.9%, thrombolytics28/168 =16.667% vs16.8%, also within threshold. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p. 7 Figure 2, all four arm rows; N071, N072, N073, N074 | Whole-percentage segment totals are101,101,101,99. Independent half-unit intervals contain100; category colors, rather than text extraction order, establish missing-width categories. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 pp. 6, 7 and9, aRR abbreviation expansion; N080, N083, N086, N090, N092, N094, N098, N100, N102 | “Absolute risk reduction” expansion differs from the ratio quantity evident from modified Poisson methods, null1, ratio-valued intervals and footnotes stating higher rate ratio. The ratio interpretation is immediately identifiable; no conflict with an evidently computed alternate numeric measure was reproduced. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001 p. 9 Table3; N088, N090, N092, N094, N096, N098, N100, N102 | Crude within-arm mismatch/no-mismatch outcome ratios and median comparisons differ from some adjusted estimates; the table explicitly adjusts age, NIHSS, time and core. Direction reversals relative to crude counts do not establish a numeric conflict. | MODEL_VERSUS_CRUDE |
| REPORT DOC-001 p. 11 discussion “two-thirds” versus p. 9 204(61%); N113 | Approximate prose fraction is not an additional independent population discrepancy; the materially different p. 4 count is retained in F-NUM-001. | DUPLICATE_OF_INCLUDED |

## Completion and limitations

All N001–N120 received an explicit review result in the companion inventory. Findings: 2. Excluded-observation rows: 6. Scientific coverage gaps: None. Exact patient category counts are not printed in Figure 2, and Figure 3 provides no exact pointwise prediction table; its plotted directions, category colors, axis scales and definitions were reviewed without inventing values. Inferential significance conflicts at rounded interval endpoints are the statistical lane's assigned checks and are not treated as rounding exclusions here.
