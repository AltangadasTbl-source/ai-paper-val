# Statistical pass 1 — support shard B

- Runtime agent ID: /root/statistics_pass1_support_b
- Model and reasoning effort: gpt-6.1-sol / high
- Start mode: FRESH_SPAWN
- Exact scope: DOC-004 REPORT, joi180108supp3_prod.pdf, physical pages 7–9; all 72 eTable 3 mode–variable–occasion tuples, all 30 eTable 4 rows, and all 16 eTable 5 subgroup estimate/95% CI rows with all eight shared pair interaction P values.
- Stable relationship IDs: S321–S438, 118 relationships, each PASS_1_COMPLETE.
- Findings: 1, F-ST1-501.
- Excluded apparent observations: 4 rows.
- Scientific coverage gaps: 0.

QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely. Current evidence maps and narrowly relevant main REPORT/SAP method excerpts were used; earlier checker/candidate/report conclusions and the web were not read. Exact supplement pages were checked against direct Poppler pdftotext 25.03.0 layout extraction and source-matched reusable page images. New derivative: preprocessing/st1-b-supp-p7-9.txt, produced by `pdftotext -layout -f 7 -l 9 joi180108supp3_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/st1-b-supp-p7-9.txt`. Page images for pages 7, 8, and 9 were visually read on CPU; their historical rendering engine is UNKNOWN_LEGACY_RENDERER. Sources and reused assets were preserved.

Every tuple's detailed pass record appears in statistics/parts/support_b_inventory.md. Continuous eTable 3/4 ranges are IQRs, not CIs; overlapping IQRs and equal rounded medians were not treated as null-effect tests. Binary counts/denominators/percentages were checked with displayed-input/output half-unit intervals and the scope's relative-gap cutoff. All 16 subgroup point estimates lie within ordered CIs and agree with the direction and rounding intervals of the printed group means. Only the ICU-start subgroup CI excludes zero; its P=.01 belongs to the interaction pair, not to that subgroup alone. The main REPORT p4 states two-sided P values, significance .05, no multiplicity adjustment, Gaussian GLM interaction analyses, and exploratory subgroup analyses. No noninferiority/equivalence margin or numeric interim/stopping boundary appears in the assigned tables. Exact subgroup sample sizes and inferential mapping are not supplied, as recorded below.

## Findings

### F-ST1-501

**Title:** Pre-randomization ventilation subgroup labels do not align with the two numerical result rows.

**Relationships:** S435 and S436.

**Exact locations and document roles:** REPORT [DOC-004 joi180108supp3_prod.pdf physical p9, eTable 5, “Ventilation before randomization” block](../../../../joi180108supp3_prod.pdf#page=9), including the first numerical line at the section heading, the second numerical line beside “> 6 hours,” and the “≤ 6 hours” label below both numerical lines. REPORT [DOC-001 main article physical p4, subgroup method paragraph](../../../../jama_simonis_2018_oi_180108.pdf#page=4) confirms that >6 hours versus ≤6 hours before randomization are the intended two categories but does not supply category-specific results resolving their placement. The main REPORT corroborates the comparison definition; the inconsistency lies within the supplement display.

**Printed values:** First numerical line: low 16.5 ± 11.6, intermediate 16.8 ± 10.7, mean difference −0.29 (95% CI −7.04 to 6.45). Second numerical line: low 15.2 ± 11.6, intermediate 15.4 ± 11.5, mean difference −0.21 (95% CI −1.72 to 1.28). The label “> 6 hours” is printed beside the second numerical line; “≤ 6 hours” is printed below it without a numerical row beside it. Shared interaction P=.98 is placed between the numerical lines. The source image confirms this placement rather than merely an extraction-spacing discrepancy.

**Rule and calculation:** A subgroup estimate/CI row must be mapped to one stated subgroup category for extraction. Sequential category order suggests >6 hours first and ≤6 hours second, whereas direct horizontal alignment puts >6 hours beside the second numerical line and leaves the first line and ≤6-hour label without aligned counterparts. The two CIs have widths 6.45−(−7.04)=13.49 days and 1.28−(−1.72)=3.00 days, a width ratio of 4.50; the extraction choice therefore changes the interval taken for a specified category. Display precision cannot determine which category labels belong to which line. No rounding reconstruction or assumption about subgroup sample size is used to choose a category.

**Focus area:** B, estimate/contrast attribution; the numerical subgroup result cannot be assigned unambiguously to its comparison category.

**Proposed review domain:** report_internal_inconsistency.

**Proposed relationship type / all relationships:** S_W / S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** The >6-hour and ≤6-hour pre-randomization ventilation subgroup means, mean differences, and 95% CIs for ventilator-free days at day 28, especially whether the >6-hour subgroup takes CI −7.04 to 6.45 or −1.72 to 1.28.

**Why context does not resolve it:** This is a label-to-result assignment that changes which numerical result applies, rather than a wording variant. Category sequence and horizontal row alignment give different assignments. The table supplies no subgroup sample sizes or alternative category-specific result location, and the main subgroup paragraph lists the categories without resolving these two numerical rows. A data extractor cannot select an assignment from the supplied label placement alone.

**Alternatives and missing definition:** A vertical layout displacement may have moved both subgroup labels down by one numerical row, making the first numerical line the >6-hour result and the second the ≤6-hour result. Alternatively, the >6-hour label may identify the second numerical line as its printed alignment suggests, with the first line belonging to the other category. Neither assignment is made here. The needed definition is the intended category-to-numerical-line mapping; subgroup sample sizes could corroborate it but are not printed. The shared interaction P=.98 does not distinguish the assignments.

**Exact human question:** Which numerical line in eTable 5 is intended for ventilation >6 hours before randomization, and which is intended for ventilation ≤6 hours: 16.5 versus 16.8 days with mean difference −0.29 (95% CI −7.04 to 6.45), or 15.2 versus 15.4 days with mean difference −0.21 (95% CI −1.72 to 1.28)?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-004 p8 eTable 4, sedative infusion, analgesic infusion, neuromuscular blockade and vasopressor use; headers 477/484 | The eight count/percentage cells differ from using the arm headers as denominators. Permitting count/header half-unit intervals and percentage ±0.05 yields recomputed intervals and remaining relative gaps: 320/477 versus 70.6%, [66.911,67.261], gap/70.6=.04658; 333/484 versus 72.1%, [68.627,68.976], .04263; 277/477 versus 61.1%, [57.906,58.237], .04604; 273/484 versus 59.1%, [56.244,56.567], .04202; 53/477 versus 11.7%, [10.995,11.228], .03609; 60/484 versus 13.0%, [12.281,12.513], .03362; 363/477 versus 80.0%, [75.916,76.285], .04581; 353/484 versus 76.4%, [72.755,73.113], .04237. All are ≤.05. Exact integers in place of count/header half-unit intervals likewise leave all relative gaps below .05. No row-specific denominator is invented. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-004 p9 eTable 5, eight subgroup pairs, especially pneumonia; REPORT DOC-001 p4 Gaussian interaction-model paragraph | A hypothetical independent normal contrast using subgroup CI widths gives approximate interaction P values .473, .188, .318, .958, .203, .255, .982, .0077 versus printed .16, .17, .32, .96, .23, .26, .98, .01. This is a **diagnostic approximation**, using SE≈CI width/3.92 and SE of the difference≈sqrt(SE1²+SE2²), not a reconstruction of the reported GLM. Subgroup sample sizes, the method producing these CIs, degrees of freedom, link/covariates, variance estimator, covariance and mapping between subgroup CI estimators and the interaction model are not supplied. Independence/covariance is not inferred. The diagnostic does not reproduce all other pairs under the display-precision rule and cannot establish category 4; both pneumonia CIs include zero and its interaction P=.16 is nonsignificant, so there is also no individual CI-versus-null-test contradiction. The pair P tests a different null from either subgroup CI. Preserve this apparent issue and its missing inputs for fresh pass 2. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-004 p7 eTable 3, other-mode respiratory acidosis after titration, low arm | The percentage is printed “35.” for 7/20. Its reading is 35%, and no numeric value or inference changes. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-004 p9 eTable 5 footer | “Data are mean ()” leaves an empty parenthesis despite the ± dispersion shown in each arm; the ± values and the separate mean-difference 95% CI columns remain identifiable. No estimate, interval, P value or extraction assignment conflicts merely because the dispersion abbreviation is absent. | NOTATION_OR_TYPOGRAPHY |

## Limitations and closure

All 118 assigned relationships have PASS_1_COMPLETE records. No source unit/cell in the assigned scope remains unread or unmapped. Exact continuous test names for eTables 3/4, exact sparse binary test/continuity-correction choices, subgroup sample sizes, and CI-to-interaction model mappings are not supplied. Missing details without a reproduced conflict were not treated as findings. No SE, covariance, degrees of freedom, estimand mapping, or model adjustment was inferred from convention. Family-level planned-versus-reported checks remain with the separate plan assignment. A fresh pass-2 agent must reread every stable record and every excluded observation under route A and the display-precision rule.

