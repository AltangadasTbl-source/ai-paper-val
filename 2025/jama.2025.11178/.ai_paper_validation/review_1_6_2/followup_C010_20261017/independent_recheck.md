# Focused independent recheck: C010

Scope: C010 only, including all fourteen registered point/interval tuples. Other stable IDs were not assigned to this focused part. Existing artifacts and supplied sources were preserved. No new extraction or OCR was needed; the recorded scientific compute device is CPU.

## Source authority and classification

The supplied main article Table 3 was inspected visually in its complete rendered PDF pages: [PDF page 10, journal page 601](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), and [PDF page 11, journal page 602](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11). The corresponding existing renderings were `document_outputs/DOC-001-MAIN/page_images/page_010.png` and `page_011.png`. Headers, outcome/time rows, contrast columns, signs, decimal values, and parentheses were read together. The main methods page 4 was also inspected visually using the existing `preprocessing/cross_source_review/main-4.png` rendering. Text/ledger/report content served as locators, not final authority.

Both compared locations are REPORT: a published result point and its stated 95% CI within the same Table 3. Primary relationship `S_W`; all relationships `S_W`; review domain `statistical_results`. This classification agrees with the ledger. Supplementary unadjusted results only provide context and do not introduce `S_C`; no PLAN content is in conflict. No classification correction is needed.

## Exact tuple checks

PT = painTRAINER; HC = health coach; UC = usual care plus. Printed endpoint order is preserved. Every location was found; every point, comparator endpoint, row, and contrast matched the registered tuple.

| Source page; outcome/time | Contrast | Printed SMD (95% CI) | Reproduced comparison after numerical endpoint sorting | Half-unit point/nearest-bound intervals | Remaining gap |
|---|---|---|---|---|---:|
| 10; pain severity, 12 months | PT/UC | −0.25 (−0.24 to 0.01) | −0.25 < −0.24 | [−.255,−.245] vs [−.245,−.235] | 0 |
| 10; pain severity, 12 months | HC/UC | −0.36 (−0.35 to −0.12) | −0.36 < −0.35 | [−.365,−.355] vs [−.355,−.345] | 0 |
| 10; pain intensity, 12 months | HC/UC | −0.27 (−0.26 to −0.12) | −0.27 < −0.26 | [−.275,−.265] vs [−.265,−.255] | 0 |
| 10; pain-related interference, 12 months | PT/UC | −0.26 (−0.25 to 0.01) | −0.26 < −0.25 | [−.265,−.255] vs [−.255,−.245] | 0 |
| 10; pain-related interference, 12 months | HC/UC | −0.37 (−0.36 to −0.11) | −0.37 < −0.36 | [−.375,−.365] vs [−.365,−.355] | 0 |
| 10; physical functioning, 6 months | PT/UC | 0.15 (0.09 to −0.06) | 0.15 > 0.09 | [.145,.155] vs [.085,.095] | .05 |
| 10; physical functioning, 6 months | HC/UC | 0.02 (−0.03 to −0.18) | 0.02 > −0.03 | [.015,.025] vs [−.035,−.025] | .04 |
| 10; physical functioning, 6 months | HC/PT | 0.22 (0.16 to 0.05) | 0.22 > 0.16 | [.215,.225] vs [.155,.165] | .05 |
| 10; physical functioning, 12 months | PT/UC | 0.20 (0.18 to −0.03) | 0.20 > 0.18 | [.195,.205] vs [.175,.185] | .01 |
| 10; physical functioning, 12 months | HC/UC | 0.07 (0.04 to −0.16) | 0.07 > 0.04 | [.065,.075] vs [.035,.045] | .02 |
| 10; physical functioning, 12 months | HC/PT | 0.27 (0.25 to 0.09) | 0.27 > 0.25 | [.265,.275] vs [.245,.255] | .01 |
| 11; PGIC–pain, 12 months | PT/UC | −0.55 (−0.50 to 0.05) | −0.55 < −0.50 | [−.555,−.545] vs [−.505,−.495] | .04 |
| 11; PGIC–pain, 12 months | HC/UC | −0.57 (−0.54 to −0.08) | −0.57 < −0.54 | [−.575,−.565] vs [−.545,−.535] | .02 |
| 11; PGIC–pain, 12 months | HC/PT | −0.29 (−0.25 to 0.14) | −0.29 < −0.25 | [−.295,−.285] vs [−.255,−.245] | .03 |

Each value is printed to two decimals, so its half-unit allowance is ±.005. The gap is max(0, absolute displayed point-to-nearest-bound separation minus .010). Five .01 separations have closed half-unit intervals that just touch. Nine retain positive gaps. Thus it would overstate the precision calculation to say all fourteen have positive gaps after the rounding allowance. Conversely, closed intervals touching does not establish that one consistent monotone rounding convention can turn an underlying contained point into the printed outside point. No unrounded values or tie-handling convention are supplied.

The applicable workflow consistency rule is focus B / route A category 1: a point estimate outside its printed interval. The local scope explicitly excludes this category from precision-based removal. All fourteen printed readings are reproduced under that registered rule; endpoint sorting does not restore containment. The evidence state for C010 is exactly **reproduced**. The determining fact is direct confirmation of these fourteen point/interval pairs, with nine remaining separated under half-unit expansion. This is an evidence-record fact; status remains **Pending Human Adjudication**.

## Definitions and limits

The Table 3 header explicitly reads “Standardized mean difference (95% CI).” Its footnote d defines SMD as: “The adjusted between-group mean difference divided by the standard deviation in the change in outcome at the given time point among the usual care plus group.” The methods on [main PDF page 4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4) describe linear regression with GEE and estimation of adjusted differences, confidence intervals, and SMDs.

The issue is the pairing of an SMD point with its own printed confidence bounds. C003 instead compares SMD point construction with the stated denominator or between-contrast relationships. Those are separate comparisons; C010 does not require reconstructing the SMD denominator to observe its point/interval pairing.

Necessary inputs for the printed comparison are available: point, both endpoints, CI header, outcome, time, contrast, and stated SMD definition. Necessary inputs for reconstructing intended numerical tuples are absent: unrounded SMD points and limits, exact SMD interval construction including any denominator uncertainty/transformation, relevant model covariance or resampling output, and intended tuple alignment. One should not assert a universal theorem that every conceivable confidence interval must contain its point estimate. A distinct interval construction or a different underlying contrast/analysis could explain an outside point in principle; the supplied description does not identify such a construction or assignment for these tuples. Six reversed physical-function endpoint orders are directly visible, but merely exchanging their order still leaves all six points outside.

The supplement was checked visually: [Supplement 4 page 16, eTable 10](../../../joi250046supp4_prod_1755300121.15587.pdf#page=16), [page 17, eTable 11](../../../joi250046supp4_prod_1755300121.15587.pdf#page=17), and [page 18, its footnote](../../../joi250046supp4_prod_1755300121.15587.pdf#page=18). These supply unadjusted medians/interquartile ranges and unadjusted mean differences with GEE-based intervals; they do not supply replacement adjusted SMD tuples or the missing SMD interval construction.

Direct observations: fourteen outside-point readings, six reversed endpoint orders, five boundary-touching precision expansions, and nine positive precision gaps. Inferred explanations: contrast/time misalignment, different interval construction, or transcription during report production. None of those mechanisms is established by the supplied sources, and no replacement value is determined.

Exact remaining human question: For each of the fourteen outcome/time/contrast pairs, which adjusted SMD point and 95% interval belong together, what method produced that interval, and do the printed assignments and endpoint orders express that method as intended?

## Bounded downstream implications

The candidate directly affects extraction and interpretation of Table 3 SMD point/interval tuples. Deriving a standard error or inverse-variance weight from these limits under an assumed conventional interval could produce an unsupported pairing or uncertainty estimate; a synthesis that uses SMDs may consequently be affected. Quantitative changes to pooled effects, weights, significance, or treatment ranking cannot be established without intended tuples and a specified downstream analysis. There is no demonstrated change to the main binary-outcome RR or the trial's primary conclusion from C010 alone. No alternative analysis or replacement interval is proposed.
