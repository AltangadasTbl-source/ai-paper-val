# Numeric consistency checker: support shard

Agent runtime ID: 01a129b6-b5e9-7d52-bfde-e8d7b31f3a04. Model: gpt-6.1-sol. Reasoning effort: medium. Start mode: FRESH_SPAWN. Scope contract and review contract read completely; tooling record confirms CPU and available direct Poppler tools.

## Complete assigned scope

Support-only numeric, count, denominator, intervention-dose and power-input arithmetic for DOC-002 PLAN pp.1–66; DOC-003 PLAN pp.1–40; DOC-004 REPORT pp.1–2; DOC-005 REPORT p.1. Stable relationships N111–N166 are documented in `relationships/parts/numeric_support_inventory.md`: 56 checked relationships. Every one of the 13 numeric subgroup rows and all five subgroup partitions was checked. Full source maps determine applicability for administrative, reference and signing pages. Main-only arithmetic and planned-versus-reported comparisons are disjoint assignments owned by other checkers. Statistical method and interval/P compatibility checks likewise belong to statistical checkers.

The support canonical extraction is source-linked evidence, not an earlier scientific decision. Targeted native/layout source checks used direct CPU Poppler `pdftotext -f N -l N -layout SOURCE -`; DOC-002 pp.26,27,29,40,49,50,60 were reopened. DOC-004 p.2 source-linked reusable rendered image was opened visually, confirming all printed rows, n labels, forest positions and caption. Source and reused artifacts were preserved.

## Findings

No qualifying support numeric finding was emitted. Arithmetic for five dose-table rows, dose concentration/cap, equal allocation, absolute and relative power-input reductions, instrument ranges, Poisson mean/SD and printed recruitment-decision cutoffs reconciles. The subgroup sex, operation, age and ERAS partitions each sum to557. No arm-specific event numerator is supplied in the subgroup figure, so adjusted relative risks cannot be independently reconstructed from those n labels.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT [DOC-004 p.2](../../../../joi240139supp3_prod_1741633738.18862.pdf#page=2), N157 | Intended-duration groups total271+261=532 whereas other binary partitions total557. Required half-unit propagation gives duration total[531,533] and operation/sex total[556,558], gap23;23/557=.041293<.05. Even unrounded25/557=.044883<.05. This apparent difference is below the mandated display-precision threshold; it is not a finding. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN [DOC-002 p.60](../../../../joi240139supp1_prod_1741633738.16362.pdf#page=60), N136 | Illustrative OBAS inputs1+4+0+0+0+1+(4−1) yield9 whereas example prints8. Applying mandated half-unit intervals to seven displayed inputs gives[5.5,12.5] (or[7,12.5] after restricting zero symptom scores to nonnegative values), overlapping printed8 interval[7.5,8.5];gap0,relative discrepancy0. Actual reported participant scores are not supplied in this example. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN [DOC-002 p.27](../../../../joi240139supp1_prod_1741633738.16362.pdf#page=27), N119 | 50kg dose-table rate prints3.75ml without '/hour'; column is infusion rate and adjacent rows use hourly units, while22.5/6=45/12=3.75. No printed numeric value differs. | NOTATION_OR_TYPOGRAPHY |
| PLAN [DOC-003 p.32](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=32), N137 | PONV appendix prints '=5' versus dummy table≥5 and complete protocol instrument≥5; isolated symbol variation resolved by the full supplied scale and complementary<5/≥5 categories. No reported participant value conflicts. | NOTATION_OR_TYPOGRAPHY |
| PLAN [DOC-003 p.18](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=18) and [p.31](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=31), N140 | Physiological POSSUM range12–88 may appear narrower than12×8=96, but source does not say every physiological variable permits score8. Item-specific attainable maxima are not supplied. Assuming all12 items have the largest category is unsupported. | CONDITIONAL_OR_UNREPORTED |
| PLAN [DOC-002 p.49](../../../../joi240139supp1_prod_1741633738.16362.pdf#page=49), N130 | Summing full-month exposures for two new sites each month6–11 would yield42centre-months rather than printed36. Exact within-month opening times are absent; midpoint activation gives2×(5.5+4.5+3.5+2.5+1.5+.5)=36. No source-supported activation date contradicts36. | CONDITIONAL_OR_UNREPORTED |
| PLAN [DOC-002 p.49](../../../../joi240139supp1_prod_1741633738.16362.pdf#page=49), N131 | Naive562/(12×20)=2.342 versus3.3 recruits per centre-month assumes all12sites accrue throughout20months, although text explicitly describes staged opening. The complete accrued centre-month denominator is not supplied as a fixed observed quantity. | CONDITIONAL_OR_UNREPORTED |

## Limitations and scope handoff

No scientific coverage gap remains in this shard. The absent arm-specific event counts, item-specific POSSUM score maxima, and within-month site activation dates are named inputs and prohibit unsupported conditional arithmetic. These are not omissions of source units. Inferential confidence convention, subgroup interaction testing, sample-size/power reproduction and planned-versus-reported comparison are retained for their assigned checker agents; this shard supplies their exact numeric source inputs without evaluating their findings.

Counts: 56 relationships; 0 findings; 7 excluded observations; all 13 subgroup numeric rows and five partitions complete. Primary output: `checkers/parts/numeric_support.md`. Companion: `relationships/parts/numeric_support_inventory.md`.
