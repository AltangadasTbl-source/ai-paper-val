# Numeric consistency review — Workflow 1.6.2

Runtime task ID: /root/numeric_checker. Fresh numeric_consistency_reviewer, gpt-6.1-sol / medium. Assigned scope: all 96 mapped pages across DOC001 (9 REPORT pages), DOC002 (45 PLAN pages), DOC003 (41 REPORT pages), and DOC004 (1 REPORT page). Read QUALITY_CONTROL_SCOPE.md and review_contract.md completely, settings, tooling, coverage, and all four current checking maps. This stage owns only this artifact and relationships/numeric_relationship_inventory.md. Stable numeric inventory: N001–N105, 105 grouped relationships. Each table/panel group retains every constituent count, denominator, percentage, risk-set, location, and applicable unit; checks are explicit in the inventory. No numerical row or source unit was selected by candidate expectation. No scientific coverage gap remains.

## Check execution and exact-source authority

Rebuilt and checked participant assessment/exclusions/randomization/receipt/analysis/follow-up; cessation time/reason totals; both safety denominators; all 25 Table1 category groups; all 24 Table3 outcome cells; main primary, death and component-event counts; baseline and achieved-mean subgroup populations; all mean-serum table percentages; all four main subgroup risk tables; both main whole-arm risk tables; both mean-serum risk tables; all 35 genotype/post hoc panel risk tables (280 counts); all disjoint subgroup risk partitions; numeric sample-size allocation, accrual, block orders, dose arithmetic and unit definitions. Matching copies were compared only after outcome, population, timepoint and model matching. Independent inferential-statistical testing is tracked in the S inventory and two statistical passes.

Current source-linked maps serve as transcription locators. Re-read direct Poppler pdftotext layout output for DOC001 pp.3–4,7–8, DOC003 p.4 and DOC002 p.30. Visually inspected the reusable DOC001 p.7 150-dpi render against the exact page location for the finding. Engine: existing source-linked rasterization; fresh read-only text commands: direct pdftotext -layout -f N -l N source.pdf -. Compute device CPU. No source or reused asset was modified; no extra derivative was written. No old candidates or report conclusions were read.

## Findings

### F-NUM-001

**Issue:** Table2's HR-direction footnote reverses the treatment-effect reading used for the same report's adverse outcomes.

**Relationships:** N054 (Table2 labels/direction) and N097 (model identity and matching estimates). Proposed relationship type S_W. All compared locations are REPORT within DOC001.

**Exact source locations:** [DOC001 PDF p.7, Table2 footnote a and all nine outcome/stratum estimates](../../../jama_urashima_2019_oi_190023.pdf#page=7); [DOC001 PDF p.3, Statistical Analysis and model contrast](../../../jama_urashima_2019_oi_190023.pdf#page=3); [DOC001 PDF p.4, Effects of Vitamin D Supplementation](../../../jama_urashima_2019_oi_190023.pdf#page=4); [DOC001 PDF p.6, middle-baseline competing-risk relapse result](../../../jama_urashima_2019_oi_190023.pdf#page=6). Document role of every compared location: REPORT.

**Printed inputs:** Table2 footnote: “Hazard ratio (HR) values greater than 1 indicate that vitamin D supplementation was associated with a decreased probability of the outcome.” Relapse subdistribution HRs, total/low/middle: 0.75 (0.48–1.17), 1.18 (0.64–2.19), 0.44 (0.21–0.89). Cancer-specific death HRs: 1.09 (0.58–2.01), 1.45 (0.63–3.38), 0.78 (0.29–2.10). Noncancer death HRs: 0.70 (0.29–1.73), 1.11 (0.26–4.65), 0.39 (0.11–1.39). The adverse-outcome definitions are relapse, cancer-specific death, and noncancer death. The body describes the middle-baseline relapse result, subdistribution HR0.44, as significantly lower in vitamin D; the primary adverse composite HR0.76 is discussed as vitamin D versus placebo and a nonsignificant reduction.

**Rule and calculation:** For HR = hazard(vitamin D)/hazard(placebo), HR>1 describes a higher event hazard and HR<1 a lower event hazard. The footnote instead assigns decreased outcome probability to HR>1. A common reversal of the contrast cannot reconcile the footnote with the matched body interpretations: for the middle relapse estimate, 0.44<1, the narrative calls the hazard lower, whereas the footnote assigns the decreased direction to the other side of 1. This is a single repeated direction-definition pattern applying to the entire footnoted table, not nine independent findings. No crude risk ratio was substituted for the Cox or competing-risk estimate.

**Display-precision check:** The relevant two-decimal values retain their sides of 1 throughout their half-unit intervals: 1.18→[1.175,1.185], 1.09→[1.085,1.095], 1.45→[1.445,1.455], 1.11→[1.105,1.115]; lower-direction 0.44→[0.435,0.445]. This is a categorical direction rule, so a recomputed count/percentage interval and a relative discrepancy between two copies are not applicable. As a numerical contrast diagnostic only, reversing the reference for the printed0.44 would give inverse interval [1/0.445,1/0.435]=[2.247191,2.298851], disjoint from [0.435,0.445]; the interval gap divided by0.44 is4.09589. This diagnostic does not propose replacing the estimate; it shows that opposite reference directions cannot be treated as display rounding.

**Focus area:** B, direction of effect across estimate, label and narrative.

**Proposed review domain:** statistical_results.

**Qualifying route:** Route A, category2 (a direction/reference-group statement reverses the printed values).

**Affected result or extracted value:** The direction assigned to the nine Table2 treatment comparisons, particularly the significant middle-baseline relapse estimate0.44 and the above-null low-baseline relapse1.18 and death estimates1.45/1.11. A reader extracting the reference direction from the footnote can reverse benefit/harm coding.

**Why context does not resolve it:** RouteA category2 applies to the printed reversal even when the body supplies a reconstructible direction. The footnote explicitly purports to define the extraction rule for the table and remains source-visible; common language about hazard versus probability does not account for reversing greater-than1 to decreased.

**Source-grounded alternatives:** The footnote may describe the reciprocal treatment contrast, or may have intended the opposite inequality. Neither reading is specified in Table2, and a reciprocal contrast conflicts with the body interpretation of the same0.44 result. The printed HR values themselves are not claimed to require replacement.

**Exact human question:** Which treatment-reference direction and greater/less-than1 interpretation should be applied to the Table2 HR and subdistribution-HR values, given the footnote's decreased-outcome statement and the body interpretations of the same estimates?

### F-NUM-002

**Issue:** Table1 genotype count/percentage cells do not reconcile with their printed arm denominators; a different available-case denominator is reconstructible but not stated in the display.

**Relationships:** N033–N038 (BsmI,Cdx2,ApaI,TaqI,DBP1,DBP2 category groups), N095 (locus populations). Proposed relationship S_W. Document role REPORT throughout.

**Exact source location:** [DOC001 PDF p.5, Table1 continued: repeated Vitamin D n=251 and Placebo n=166 headers; BsmI,Cdx2,ApaI,TaqI,DBP1,DBP2 rows; all three footnotes](../../../jama_urashima_2019_oi_190023.pdf#page=5). Direct PDF text and page image independently inspected. Footnote a states percentages may not sum100% because rounding; no footnote states genotype-specific percentage denominators or missing genotype counts.

**Printed inputs, rule and full calculation:** The table pairs each count with a percentage under the arm headers251/166. For each cell, recompute100×count/header. Allow count and header half-unit intervals and printed integer percentage±0.5. The recomputed interval is[100(c−0.5)/(n+0.5),100(c+0.5)/(n−0.5)]. Relative discrepancy is the gap from printed[p−0.5,p+0.5], divided by the printed percentagep. The following22 cells remain above.05; all other genotype/header pairs were checked and do not exceed the rule.

| Locus / genotype | Arm and printed denominator | Printed count (%) | Recomputed interval, % | Printed percentage interval | Relative discrepancy |
|---|---|---|---|---|---|
| BsmI GG | Vitamin D,251 | 175 (76) | [69.383698,70.059880] | [75.5,76.5] | 0.071581 |
| BsmI GG | Placebo,166 | 119 (79) | [71.171171,72.205438] | [78.5,79.5] | 0.079678 |
| Cdx2 GG | Vitamin D,251 | 89 (39) | [35.188867,35.728543] | [38.5,39.5] | 0.071063 |
| Cdx2 GA | Vitamin D,251 | 103 (45) | [40.755467,41.317365] | [44.5,45.5] | 0.070725 |
| Cdx2 AA | Vitamin D,251 | 38 (17) | [14.910537,15.369261] | [16.5,17.5] | 0.066514 |
| Cdx2 GG | Placebo,166 | 49 (33) | [29.129129,29.909366] | [32.5,33.5] | 0.078504 |
| Cdx2 GA | Placebo,166 | 77 (51) | [45.945946,46.827795] | [50.5,51.5] | 0.072004 |
| ApaI GG | Vitamin D,251 | 96 (42) | [37.972167,38.522954] | [41.5,42.5] | 0.070882 |
| ApaI GT | Vitamin D,251 | 104 (45) | [41.153082,41.716567] | [44.5,45.5] | 0.061854 |
| ApaI GG | Placebo,166 | 69 (46) | [41.141141,41.993958] | [45.5,46.5] | 0.076218 |
| ApaI GT | Placebo,166 | 61 (40) | [36.336336,37.160121] | [39.5,40.5] | 0.058497 |
| TaqI TT | Vitamin D,251 | 172 (74) | [68.190855,68.862275] | [73.5,74.5] | 0.062672 |
| TaqI TT | Placebo,166 | 115 (77) | [68.768769,69.788520] | [76.5,77.5] | 0.087162 |
| TaqI TC | Placebo,166 | 31 (21) | [18.318318,19.033233] | [20.5,21.5] | 0.069846 |
| DBP1 TT | Vitamin D,251 | 134 (58) | [53.081511,53.692615] | [57.5,58.5] | 0.065645 |
| DBP1 TG | Vitamin D,251 | 87 (38) | [34.393638,34.930140] | [37.5,38.5] | 0.067628 |
| DBP1 TT | Placebo,166 | 82 (55) | [48.948949,49.848943] | [54.5,55.5] | 0.084565 |
| DBP1 TG | Placebo,166 | 57 (39) | [33.933934,34.743202] | [38.5,39.5] | 0.096328 |
| DBP2 CC | Vitamin D,251 | 115 (50) | [45.526839,46.107784] | [49.5,50.5] | 0.067844 |
| DBP2 CA | Vitamin D,251 | 91 (39) | [35.984095,36.526946] | [38.5,39.5] | 0.050591 |
| DBP2 CC | Placebo,166 | 81 (54) | [48.348348,49.244713] | [53.5,54.5] | 0.078802 |
| DBP2 CA | Placebo,166 | 58 (39) | [34.534535,35.347432] | [38.5,39.5] | 0.080835 |

**Focus area:** A, count/denominator/percentage relationships within one display.

**Proposed review domain:** statistical_results.

**Qualifying route:** Route A, category3 (counts within one display).

**Affected result or extracted value:** The baseline genotype proportions and their denominators for the prespecified SNP subgroup populations. A data extractor applying the explicit headers uses251/166; a data extractor reconstructing the category sums uses231/150 for BsmI,ApaI,TaqI,DBP2,230/150 forCdx2,and231/148 forDBP1. Those are distinct extraction populations.

**Why context does not resolve it:** RouteA category3 applies after the printed header discrepancy is reproduced. The implied available-case denominators account for the percentages, but are an inference from category sums, not stated denominator context. Their recoverability does not remove the printed count/header/percentage mismatch. Ordinary rounding alone cannot explain the22 above-threshold cells.

**Source-grounded alternative:** Mutually exclusive genotype-category sums give the likely available-case denominators above; using those instead of251/166 makes all displayed percentage cells satisfy the precision rule. Supplement genotype risk tables corroborate most category counts, with a separate below-threshold DBP1 TG placebo57-versus59 occurrence. Thus unavailable genotypes rather than replacement counts is a plausible explanation. No replacement percentage, preferred denominator or adjudication is proposed.

**Exact human question:** Are Table1 genotype percentages based on locus-specific available-case populations rather than the displayed251/166 arm denominators, and which denominator should be retained for each baseline genotype proportion and subgroup-population extraction?

## Excluded observations

Only apparent discrepancies actually examined and not emitted appear below; reconciled checks are in the N inventory. Each row has exactly one scope reason code.

| Location | Observation | Reason code |
|---|---|---|
| DOC001 p.4 population narrative versus p.5 Table1 stageII | Pooled stageII111/417=26.619% versus printed26%; half-unit output [25.5,26.5] and recomputation interval [110.5/417.5×100,111.5/416.5×100]=[26.467,26.771] overlap, so discrepancy0. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC001 p.5 Table1 middle baseline25(OH)D vitamin D | 142/248=57.258% versus58%; count half-unit recomputation [141.5/248.5×100,142.5/247.5×100]=[56.9416,57.5758], printed [57.5,58.5] overlap; no qualifying numeric gap. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC001 p.5 Table1 DBP1 TG placebo versus DOC003 p.23 eFigure3Q year-zero placebo risk | 57 versus59; half-unit intervals[56.5,57.5] and[58.5,59.5], gap1/57=.01754≤.05. Locus sums148 versus150 reflect the same occurrence. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC001 p.5 Table1 BMI/baseline25(OH)D/FokI percentages versus whole-arm headers | Recomputed every displayed cell using explicit251/166 headers as well as category sums; every apparent gap remains within half-unit intervals or relative.05. The above-threshold cells in the other six loci are included inF-NUM-002 rather than excluded by available-case assumptions. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC001 pp.1,4 primary and death event counts versus five-year survival77/69 and82/81 | Whole-follow-up crude event proportions have different estimands from five-year survival in a censored survival analysis. | MODEL_VERSUS_CRUDE |
| DOC001 p.6 serum25(OH)D medians versus printed87% change ratio | (41−21)/21=95.24% is the change in printed group medians, not the participant change-ratio distribution compared by Mann–Whitney. No claim equates those quantities. | CONDITIONAL_OR_UNREPORTED |
| DOC003 pp.2–4 achieved-mean serum population413 versus DOC001 pp.4–6 baseline population410 | Trial-average values use baseline and annual samples, whereas baseline groups exclude seven missing baseline results; differing availability definitions do not establish conflicting analysis-population counts. | CONTEXT_RESOLVES |
| DOC001 p.7 Figure3 caption versus visible panelC risk table | Caption says numbers at risk for panelC not given because weighting, but panelC visibly supplies both risk rows; this figure-pointer/caption difference supplies no alternative printed count or result and is a peripheral comparison. | PERIPHERAL_COMPARISON |
| DOC002 initial pp.9,12 versus final pp.25,28,45 | Initial1200IU/day=2×600 versus initial capsule paragraph1000IU; reported trial relies on the disclosed pretrial amendment and final2000IU=2×1000. This historical plan-version inconsistency does not change the reported intervention or statistical decision rule. | PERIPHERAL_COMPARISON |

## Completion and limitations

105 grouped N relationships complete; 2 findings; 9 excluded observations. Scientific coverage gaps: none. All table cells and risk counts were reviewed in the complete current keyed maps, with source-linked visual mapper coverage and targeted direct-page confirmation for both findings. No participant raw data, unprinted curve coordinates, exact box-plot summaries, or subgroup event numerators are supplied. Available-case denominators arise partly from category sums and are recorded as alternatives; they do not screen out reproduced printed-header conflicts. Full interval/P, model, sample-size-method, outcome-status and planned-analysis review belongs to the distinct statistical and cross-source stages; the numeric checks do not substitute assumptions for those analyses.
