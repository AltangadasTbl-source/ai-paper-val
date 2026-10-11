# Statistical pass 1 — supplementary change rows, support A

Runtime agent ID: root/stat1_support_a. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN.

Scope: S430, S431, S432, S433, S434, S435, S436, S437, S438, S439, S440, S441, S442, S443, S444, S445, S446, S447, S448, S449, S450, S451, S452, S453, S454, S455, S456, S457, S458, S459, S460, S461, S462, S463, S464, S465, S466, S467, S468, S469, S470, S471, S472, S473, S474, S475, S476, S477, S478, S479, S480, S481, S482, S483, S484, S485, S486, S487, S488, S489, S490, S491, S492, S493, S494, S495, S496, S497, S498, S499, S500, S501, S502, S503, S504, S505, S506, S507, S508, S509, S510, S511, S512, S513, S514, S515, S516, S517, S518, S519, S520, S521, S522, S523, S524, S525, S526, S527, S528, S529, S530, S531, S532, S533. Completed 104/104 relationships: eTable 2 MI food changes (44), eTable 3 completer dietary-score changes (8), eTable 4 completer food changes (44), and eTable 5 completer energy/protein/carbohydrate/fat changes (8). The last assigned row is S533, total fat at 12 months, DOC-004 p.14. Remaining eTable 5 rows belong to support B.

## Evidence and checks completed

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Source-linked reusable layout: .ai_paper_validation/document_outputs/DOC-004/supp3_layout.txt, with curator-confirmed direct-source byte identity (Poppler pdftotext 26.01.0). Reread the complete assigned table headers, every assigned row including its wrapped continuation, and all relevant footnotes. [Results source, eTable 2](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=3), [eTable 3](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=9), [eTable 4](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=10), [eTable 5](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=14). No new derivative/render/OCR was needed; processing device CPU. Sources and reused assets were preserved.

The exact model/test context is [DOC-001 REPORT p.4 Statistical Analysis](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4): mixed linear models at site, participant and cluster-family levels; completer and multiple-imputation analyses distinguished; all tests two-sided with P < .05 significant; secondary exploratory analyses have no additional multiplicity adjustment. DOC-004 table footnotes establish means with 95% confidence intervals and site/couple random factors. All compared result locations here are REPORT; the potential relationship would be S_W and the review domain statistical_results.

All 312 estimates (I change, C change, between-group change for each of 104 rows) are contained in their intervals, with lower endpoints no greater than upper endpoints. The zero-null status of each between-group 95% CI agrees with its printed P under the stated .05 threshold. There are no interval-versus-P/significance conflicts in this scope. Within-arm P values are absent and were not invented.

All 104 intervention-minus-control changes reconcile under half-unit display intervals. Twenty-four central displayed subtractions differ by one final display unit, but the recomputed contrast and printed-contrast intervals overlap in each case (gap 0, relative discrepancy 0). This checks the same-display model contrast; the source baseline values are medians/IQRs for most foods and were not used as crude substitutes for model-based changes.

A normal-tail diagnostic with CI-width-derived standard error was used only as an approximation, retaining rounding ranges. Every displayed exact P, allowing its own half-unit interval, and every printed '<.001' has compatible values in the diagnostic range. The actual statistic, degrees of freedom, variance estimator, covariance and exact MI pooling/test construction are not supplied, so no exact test reproduction is claimed. In particular, S520 prints P=.001 with contrast −61 (−95 to −27); the diagnostic range .000321–.000588 overlaps the displayed P interval .0005–.0015. No category-1 conflict is reproduced from those values.

S487 (extra-virgin olive oil, completers, 12 months) prints −8 (−16 to 0), P=.05. The printed interval includes zero and printed .05 does not satisfy P<.05, so the displayed null/threshold comparison agrees; no significance finding is emitted. Rounded endpoints/P do not establish any additional conclusion.

The score footnote exception was retained: er-MedDiet completer counts differ from the common table header as explicitly specified on p.10. The table labels, unit scales, population/time keys, randomization and repeated-measures description identify these analyses without a contradictory method step. No noninferiority, equivalence, interim or stopping decision is attached to these rows; no sample-size claim is tested outside this assigned result scope.

## Findings

None. Finding count: 0. Every assigned relationship is explicitly PASS_1_COMPLETE in statistics/parts/support_a.md. No candidate IDs or human dispositions were assigned.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-004 REPORT pp.3,5,6,7,9,10,11,12,14; S432, S436, S442, S450, S451, S465, S468, S480, S488, S491, S492, S496, S499, S502, S509, S510, S512, S513, S516, S517, S520, S521, S527, S533; exact row/outcome/time and calculation in statistics/parts/support_a.md | Repeated pattern: subtracting the printed central arm changes gives a contrast differing by one final displayed unit (1 g/week or kcal/day, or .1 score/percentage point) in 24 rows. Each arm input and printed contrast retain their own half-unit intervals. Every recomputed/printed range overlaps; gap 0 and relative discrepancy 0. For example S480 PDQS six-month: 4.6−2.3=2.3 versus 2.4; recomputed [2.20,2.40], printed [2.35,2.45]. | ROUNDING_OR_DISPLAY_PRECISION |

Excluded-observation count: 1 consolidated pattern (24 affected central-value subtractions). Checks that reconcile directly, absent details without a contradiction, and correctly rejoined wrapped P/CI lines are not additional excluded observations.

## Limitations and handoff

No scientific-coverage limitation within the assigned 104 relationships. Exact reproduction of numeric P values from CI widths is limited by absent test statistics, standard errors, degrees of freedom, variance/covariance and exact test/pooling definitions. The diagnostic approximation is clearly separated from the reported analysis and from mandatory zero-null/CI/P checks. The complete per-row records preserve all three printed estimates/intervals, P, source page, outcome/time/population, rounding ranges, diagnostic bounds and PASS_1_COMPLETE.

Artifacts: checkers/parts/statistical_pass_1_support_a.md; statistics/parts/support_a.md. The coordinator owns the canonical merge. This agent does not perform pass 2.

