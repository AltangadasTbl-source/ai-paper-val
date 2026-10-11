# Mechanical Evidence Recheck

This source-first recheck covers every stable candidate ID in the ledger: C001, C002, C003, C004, C005, C006, C007, and C008. Direct supplied PDFs are the authority. Fresh native and layout text were used only to locate passages, and the cited pages were extracted again directly from the supplied PDFs for this recheck. No prior audit derivative was inspected. The available direct extractor does not decode a few mathematical glyphs cleanly, and no PDF renderer is available; those exact limitations are stated below. These records are evidence facts for human adjudication and are not dispositions.

## C001 — Intraoperative adverse-event threshold definitions differ within the main article

- **Cited location found:** Yes. The methods definitions are on [DOC-001 PDF p. 3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=3), and the Table 3 definitions are on [DOC-001 PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- **Source printed value/text matched:** The p. 3 text identifies hypoxemia at SpO2 92% for more than 1 minute and hypotension at systolic arterial pressure below 90 mm Hg for more than 2 minutes. The direct text layer omits the inequality glyph immediately before `92%`; nearby prose on the same page says `92% or lower`, but a visual reading of that one glyph was unavailable.
- **Comparator printed value/text matched:** The p. 10 footnotes define hypoxemia as SpO2 of 92% or less, or a decline greater than 5% when SpO2 was previously below 92%. They define hypotension as systolic pressure below 90 mm Hg, or a decrease greater than 10 mm Hg when systolic pressure was previously below 90 mm Hg. Neither footnote prints the p. 3 duration condition.
- **Consistency rule applicable:** Yes. The same named Table 3 outcomes should use the same operational criteria across methods and table footnotes, or one location should identify itself as an abbreviation, extension, or superseding definition.
- **Calculation or logical comparison reproduced:** The methods criteria contain duration requirements of more than 1 minute and more than 2 minutes. The Table 3 criteria omit those durations and add baseline-dependent alternative branches. The two printed rule sets are therefore not textually identical.
- **Necessary inputs available; exact missing inputs or definitions:** Both threshold texts, outcome names, values, and duration statements are available. Missing are a package statement identifying which rule set generated the Table 3 numerators, whether the p. 3 durations apply to both p. 10 alternative branches, and a visually decoded p. 3 inequality glyph.
- **Source-grounded alternative interpretation:** The p. 3 methods text may be a shortened summary while the p. 10 footnotes give the complete table-specific criteria. The package does not explicitly establish that relationship.
- **Direct observation:** The durations appear only on p. 3, while the baseline-dependent alternatives appear only on p. 10.
- **Inferred explanation:** A shortened methods description or expanded table footnote could have produced the difference; the production mechanism and any effect on event counts are not directly shown.
- **Exact remaining human question:** Which complete hypoxemia and hypotension algorithms generated the Table 3 event counts, including durations and baseline-dependent branches, and how should the two printed descriptions be related?

## C002 — White-blood-cell magnitude and unit are on incompatible printed scales

- **Cited location found:** Yes. The Table 1 row is on [DOC-001 PDF p. 6](../../../jama_bluth_2019_oi_190055_16092.pdf#page=6), and the leukocyte threshold definition is on [DOC-005 PDF p. 20](../../../joi190055supp4_prod_16092.pdf#page=20).
- **Source printed value/text matched:** DOC-001 p. 6 gives the white-blood-cell row with values `8224 (2346)` and `8347 (2758)` under a unit whose direct text layer returns an undecodable multiplication glyph followed by `10^9/L`. The cited `×10^9/L` reading is consistent with the remaining text, but the multiplication glyph could not be visually inspected.
- **Comparator printed value/text matched:** DOC-005 p. 20 defines leukocytosis or leucopenia using white-blood-cell counts below `4000 cells/mm3` or above `12000 cells/mm3`.
- **Consistency rule applicable:** Yes. A laboratory value and its printed unit must represent the same scale; the supplement supplies an internal cells-per-cubic-millimetre scale for this laboratory measure.
- **Calculation or logical comparison reproduced:** Because 1 litre equals 1,000,000 cubic millimetres, `8224 cells/mm3 = 8.224 ×10^9/L` and `8347 cells/mm3 = 8.347 ×10^9/L`. Conversely, `8224 ×10^9/L = 8,224,000 cells/mm3`. The table values and the `×10^9/L` label differ by a factor of 1000 under these conversions.
- **Necessary inputs available; exact missing inputs or definitions:** The row values, exponent, per-litre denominator, and supplement thresholds are available. Missing are the intended Table 1 unit, the intended decimal placement of the displayed means and standard deviations, and the original laboratory export scale.
- **Source-grounded alternative interpretation:** The intended unit may be `cells/mm3`, or the intended values under `×10^9/L` may be approximately `8.224 (2.346)` and `8.347 (2.758)`.
- **Direct observation:** The main table combines four-digit values with a per-litre `10^9` exponent, while the supplement expresses comparable leukocyte magnitudes as four-digit cells-per-cubic-millimetre thresholds.
- **Inferred explanation:** A unit-label carryover or omitted decimal scaling could explain the display; the source package does not identify which field produced it.
- **Exact remaining human question:** Is the Table 1 unit intended to be cells/mm3, or are the displayed white-blood-cell values and standard deviations intended to be divided by 1000 under the `×10^9/L` label?

## C003 — Per-protocol effect estimates are generically labeled and do not reproduce as crude ratios

- **Cited location found:** Yes. eTable 8 is on [DOC-005 PDF p. 29](../../../joi190055supp4_prod_16092.pdf#page=29). The analogous main Table 3 uses a `Risk Ratio (95% CI)` heading on [DOC-001 PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), with its risk-ratio footnote on [DOC-001 PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- **Source printed value/text matched:** eTable 8 prints only `Effect Estimate 95% CI`. It gives postoperative pulmonary complications as `186/917 (20.3)` versus `209/912 (22.9)`, effect `0.92 (0.82 to 1.04)`; pleural effusion as `38/917 (4.1)` versus `18/912 (2.0)`, effect `1.37 (1.14 to 1.65)`; and cardiopulmonary edema as `15/917 (1.6)` versus `7/912 (0.8)`, effect `1.36 (1.02 to 1.82)`.
- **Comparator printed value/text matched:** Main Table 3 explicitly labels its analogous effect column `Risk Ratio (95% CI)` and states that its data are risk ratios unless otherwise indicated. That table is an intention-to-treat display, so it supplies a label comparator rather than the per-protocol numerical comparator.
- **Consistency rule applicable:** Yes. A generic effect column needs a defined measure, direction, and model when its displayed estimates cannot be obtained as the evident crude ratios from the same row's exact counts and denominators.
- **Calculation or logical comparison reproduced:** For the three eTable 8 rows, crude high-versus-low risk ratios are `(186/917)/(209/912) = 0.885`, `(38/917)/(18/912) = 2.100`, and `(15/917)/(7/912) = 2.131`. Crude odds ratios are `0.856`, `2.147`, and `2.150`. These do not equal the printed `0.92`, `1.37`, and `1.36` at displayed precision. These direct recalculations differ slightly from the ledger's diagnostic rounding but reproduce the same nonidentity.
- **Necessary inputs available; exact missing inputs or definitions:** Exact event counts, denominators, printed estimates, intervals, and P values are available. Missing are the effect-measure name, numerator/reference direction, estimand, adjustment variables, model form, variance method, confidence-interval method, and test definition used for eTable 8.
- **Source-grounded alternative interpretation:** The eTable 8 estimates may be adjusted or otherwise model-based rather than crude risk ratios or odds ratios. Such an analysis could account for the numerical differences, but its definition is not printed in the table or footnote.
- **Direct observation:** The table's header is generic, and the printed effects do not equal crude risk ratios or odds ratios from the displayed per-protocol counts.
- **Inferred explanation:** Adjustment, clustering, site effects, time-to-event modelling, or another model could explain the estimates; none of those mechanisms is identified by the supplied eTable 8 text.
- **Exact remaining human question:** What named effect measure, reference direction, model, adjustment set, variance method, and test produced the eTable 8 estimates and intervals, and where should those definitions be printed?

## C004 — eFigure 11 body text assigns mortality statistics to extra-pulmonary complications

- **Cited location found:** Yes. eFigure 11 is on [DOC-005 PDF p. 41](../../../joi190055supp4_prod_16092.pdf#page=41), eFigure 10 is on [DOC-005 PDF p. 40](../../../joi190055supp4_prod_16092.pdf#page=40), and the matched 5-day mortality row is on [DOC-001 PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- **Source printed value/text matched:** DOC-005 p. 41 is titled `Probability of death in the first 5 postoperative days` and prints 0.5% versus 0.3%, hazard ratio for 5-day mortality `1.67`, 95% confidence interval `0.40 to 6.97`, and `P=0.484`. Its body sentence nevertheless calls the rate `postoperative extra-pulmonary complications`.
- **Comparator printed value/text matched:** DOC-005 p. 40 separately labels postoperative extra-pulmonary complications and prints 16.9% versus 15.2%, hazard ratio `1.12`, 95% confidence interval `0.89 to 1.39`, and `P=0.314`. DOC-001 p. 10 prints mortality at 5 days as 5 events (0.5%) versus 3 events (0.3%) with hazard ratio `1.67 (0.40 to 6.97)` and P value `.48`.
- **Consistency rule applicable:** Yes. A figure's outcome name in its body sentence should agree with its title, estimate label, and matched result elsewhere in the package.
- **Calculation or logical comparison reproduced:** The p. 41 percentages and hazard ratio match the main article's 5-day mortality result and do not match the p. 40 extra-pulmonary-complication percentages or hazard ratio. Mortality and extra-pulmonary complications are therefore distinct supplied outcomes attached to distinct statistic sets.
- **Necessary inputs available; exact missing inputs or definitions:** The figure titles, body sentences, outcome-specific values, and main-table comparator are available. A rendered view of the p. 41 plotted curves, axes, and at-risk display is unavailable, so the visual identity of the plotted outcome is an exact missing input.
- **Source-grounded alternative interpretation:** The extra-pulmonary-complications phrase on p. 41 may be a repeated sentence from eFigure 10 while the eFigure 11 title and mortality statistics are intended.
- **Direct observation:** The p. 41 title and hazard-ratio phrase identify mortality, while the same page's body outcome phrase identifies extra-pulmonary complications.
- **Inferred explanation:** A production carryover from eFigure 10 is plausible but is not directly documented.
- **Exact remaining human question:** Does the eFigure 11 plot itself represent 5-day mortality, and is the body phrase `postoperative extra-pulmonary complications` intended to name mortality or to be replaced with the mortality outcome name?

## C005 — Abstract hypoxemia confidence interval loses the negative sign on its upper endpoint

- **Cited location found:** Yes. The abstract result is on [DOC-001 PDF p. 1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1), and the Table 3 result is on [DOC-001 PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9).
- **Source printed value/text matched:** The abstract prints hypoxemia as 5.0% versus 13.6%, difference `-8.6%`, 95% confidence interval `-11.1% to 6.1%`, and `P < .001`. The direct source text does not print a plus sign before 6.1; the endpoint is positive because no minus sign is present.
- **Comparator printed value/text matched:** Table 3 prints 49 (5.0%) versus 134 (13.6%) and difference `-8.6` with 95% confidence interval `-11.1 to -6.1`.
- **Consistency rule applicable:** Yes. Repeated displays of the same population, outcome, contrast, estimate, and confidence interval should have the same endpoint signs.
- **Calculation or logical comparison reproduced:** `49/989 × 100 = 4.9545%`, `134/987 × 100 = 13.5765%`, and their unrounded difference is `-8.6220` percentage points, consistent with the printed `-8.6`. The Table 3 interval is wholly negative and contains `-8.6`; the abstract interval crosses zero. The upper endpoints `6.1` and `-6.1` cannot be reconciled by rounding.
- **Necessary inputs available; exact missing inputs or definitions:** The counts, denominators, rounded percentages, estimate, both endpoint displays, and P value are available. Missing are the intended abstract upper-endpoint sign and a package statement identifying the authoritative production value.
- **Source-grounded alternative interpretation:** The abstract may have omitted a minus sign while Table 3 retained the intended interval, or the table may be the intended primary display. The package does not document which endpoint was intended.
- **Direct observation:** The two locations differ only in the sign attached to the upper endpoint of the matched confidence interval.
- **Inferred explanation:** A typographical sign omission is plausible, but its production history is not supplied.
- **Exact remaining human question:** Is the abstract's upper confidence-limit endpoint intended to be `-6.1%`, and which source record establishes the intended sign?

## C006 — Matched synthetic-colloid-use rows print different P values

- **Cited location found:** Yes. Main Table 2 is on [DOC-001 PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), and supplement eTable 3 is on [DOC-005 PDF p. 24](../../../joi190055supp4_prod_16092.pdf#page=24).
- **Source printed value/text matched:** DOC-001 p. 8 prints synthetic-colloid use as 74 (7.5%) versus 56 (5.7%), absolute difference `1.8 (-0.3 to 4.0)`, and P value `.09`.
- **Comparator printed value/text matched:** DOC-005 p. 24 has high- and low-PEEP headers `n=989` and `n=987`, prints synthetic colloids as 74 (7.5%) versus 56 (5.7%), and gives P value `0.10` for that row. A separate `0.09` on the next line belongs to a different displayed summary and is not the synthetic-colloid-use P-value cell.
- **Consistency rule applicable:** Yes. A matched population, contrast, binary row, and display precision should give the same P value unless the sources identify different tests or analysis rules.
- **Calculation or logical comparison reproduced:** The source values compare directly as `.09` versus `.10`. The underlying proportions are `74/989 = 7.4823%` and `56/987 = 5.6738%`, with an unrounded difference of `1.8085` percentage points. No tail probability was reconstructed because the exact test definitions are absent.
- **Necessary inputs available; exact missing inputs or definitions:** Group sizes, event counts, percentages, main-table difference and interval, and both P values are available. Missing are the exact statistical test, sidedness, continuity treatment, variance rule, unrounded P value, and rounding pipeline used at each location.
- **Source-grounded alternative interpretation:** The two displays may use different undocumented tests or different rounding pipelines; alternatively, one P-value cell may reflect a transcription difference.
- **Direct observation:** The same displayed group sizes, counts, and percentages are paired with P values that differ by 0.01 at the shown precision.
- **Inferred explanation:** A test-method or production-pipeline difference is possible but is not named in either cited display.
- **Exact remaining human question:** Were different tests or rounding rules intentionally used for the two synthetic-colloid-use rows, and what P value follows the specified analysis for this matched result?

## C007 — Neuromuscular-monitoring percentages do not match their printed fractions

- **Cited location found:** Yes. The complete row is on [DOC-001 PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8).
- **Source printed value/text matched:** The row prints monitoring of neuromuscular function as `632/982 (64.9%)` in the high-PEEP group and `651/984 (67.7%)` in the low-PEEP group.
- **Comparator printed value/text matched:** The same row prints absolute difference `-1.8` percentage points with 95% confidence interval `-6.0 to 2.4` and P value `.40`.
- **Consistency rule applicable:** Yes. Within a `No./total No. (%)` display, each percentage should reproduce from its adjacent numerator and denominator under the shown one-decimal precision.
- **Calculation or logical comparison reproduced:** `632/982 × 100 = 64.3585%`, which rounds to 64.4%, not 64.9%. `651/984 × 100 = 66.1585%`, which rounds to 66.2%, not 67.7%. The count-derived difference is `-1.8001` percentage points, which rounds to `-1.8`, whereas the two printed percentages differ by `64.9 - 67.7 = -2.8` percentage points.
- **Necessary inputs available; exact missing inputs or definitions:** Both numerators, denominators, percentages, the difference, interval, and P value are available. Missing are the authoritative values for the four fraction/percentage fields and any alternative denominators, weighting, adjustment, or rounding rule used to generate the displayed percentages.
- **Source-grounded alternative interpretation:** One or more counts, denominators, or percentages may be transcribed differently from the analysis output. The printed difference numerically agrees with the displayed fractions rather than with the displayed percentages.
- **Direct observation:** Neither printed percentage equals its adjacent fraction to one decimal, and the printed percentage subtraction differs from the row's printed difference.
- **Inferred explanation:** The agreement between the fraction-derived difference and `-1.8` suggests that the difference may have been generated from the counts, but the table does not state its calculation method.
- **Exact remaining human question:** Which numerators, denominators, percentages, and difference are intended for the monitoring row, and were any unprinted denominators or adjustments used?

## C008 — Neuromuscular-reversal percentages do not match their printed fractions

- **Cited location found:** Yes. The complete row is on [DOC-001 PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8).
- **Source printed value/text matched:** The row prints reversal as `724/982 (74.3%)` in the high-PEEP group and `723/984 (75.2%)` in the low-PEEP group.
- **Comparator printed value/text matched:** The same row prints absolute difference `0.2` percentage points with 95% confidence interval `-3.6 to 4.1` and P value `.90`.
- **Consistency rule applicable:** Yes. Within a `No./total No. (%)` display, each percentage should reproduce from its adjacent numerator and denominator under the shown one-decimal precision.
- **Calculation or logical comparison reproduced:** `724/982 × 100 = 73.7271%`, which rounds to 73.7%, not 74.3%. `723/984 × 100 = 73.4756%`, which rounds to 73.5%, not 75.2%. The count-derived difference is `0.2515` percentage points, which ordinarily rounds to `0.3` at one decimal; it is close to but not exactly the printed `0.2` under ordinary rounding. The two printed percentages instead imply `74.3 - 75.2 = -0.9` percentage points, opposite in sign to the printed difference.
- **Necessary inputs available; exact missing inputs or definitions:** Both numerators, denominators, percentages, the difference, interval, and P value are available. Missing are the authoritative row values and the exact rule, model, unrounded inputs, or alternative denominators used to calculate the difference, interval, and percentages.
- **Source-grounded alternative interpretation:** One or more counts, denominators, or percentages may be transcribed differently from the analysis output. A model-based or differently rounded difference might explain `0.2`, but the table does not identify such a rule.
- **Direct observation:** Neither printed percentage equals its adjacent fraction to one decimal, and the printed percentages imply a negative difference while the row prints a positive difference.
- **Inferred explanation:** The proximity of the fraction-derived `0.2515` to the printed `0.2` may indicate a calculation from more precise or model-based inputs, but that mechanism is not supplied.
- **Exact remaining human question:** Which numerators, denominators, percentages, and difference are intended for the reversal row, and what exact calculation produced the positive `0.2` difference?

## Scope completion

All eight stable IDs were rechecked separately against their cited direct-source pages. The exact unresolved limitations are the unavailable visual decoding of the p. 3 inequality glyph and p. 6 multiplication glyph, the unavailable visual identity of the eFigure 11 plot, and the unreported analysis definitions named within the relevant candidate records.
