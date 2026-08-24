# Evidence Recheck

## Scope and method

This recheck covers every stable candidate in [`candidate_ledger.md`](../candidate_ledger.md):
C001 through C004. Each
candidate was checked separately against the cited location in the supplied main-article PDF,
using the fresh simple and layout text only to locate and transcribe the PDF evidence. No source,
candidate ID, or candidate proposition was changed. All four candidates remain Pending Human
Adjudication.

The supplied main article resolves at
[`jama_jabre_2018_oi_180004.pdf`](../../../jama_jabre_2018_oi_180004.pdf) and contains 9 PDF pages.
The cited `#page=4` and `#page=6` targets are therefore within the document. Both fresh locator
files also resolve:

- [fresh simple text](../preprocessing/pymupdf_simple_text/DOC-001_jama_jabre_2018_oi_180004.txt)
- [fresh layout text](../preprocessing/pymupdf_layout_text/DOC-001_jama_jabre_2018_oi_180004.txt)

## C001 — Per-protocol ETI ROSC percentage versus numerator, denominator, and signed difference

- **Cited location found:** Yes. DOC-001, [main article Table 2, PDF p. 6](../../../jama_jabre_2018_oi_180004.pdf#page=6), Per-Protocol Analysis, row “Return of spontaneous circulation.”
- **Source printed value/text matched:** Yes. The row prints BMV `342 (34.4)`, ETI `377 (30.0)`, proportion difference `−5.6 (−9.9 to −1.3)`, and `P = .01`. The per-protocol column denominators immediately above the row are BMV `n = 995` and ETI `n = 943`. The column heading identifies the effect as `BMV(%) − ETI(%) (95% CI)`.
- **Comparator printed value/text matched:** Yes. The ETI count `377`, ETI denominator `943`, ETI display `30.0%`, and signed BMV-minus-ETI display `−5.6` all occur in the cited table block.
- **Consistency rule applicable:** Yes. In a column headed “No. of Patients (%),” the parenthetical percentage can be compared with `100 × count / stated analysis denominator`, allowing ordinary one-decimal rounding. The displayed BMV-minus-ETI proportion difference can also be compared with the two count-derived rates on the heading’s signed scale.
- **Calculation or logical comparison reproduced:** `100 × 342/995 = 34.371859%`, which rounds to the printed BMV `34.4%`. `100 × 377/943 = 39.978791%`, which rounds to `40.0%`, 9.978791 percentage points above the printed ETI `30.0%`. The count-derived signed difference is `100 × (342/995 − 377/943) = −5.606932` percentage points, which rounds to the printed `−5.6`. By contrast, the two displayed percentages give `34.4 − 30.0 = +4.4` percentage points.
- **Necessary inputs available:** The printed counts, per-protocol denominators, displayed percentages, effect direction, point difference, CI, and P value are available. Inputs needed to reproduce the count-derived percentage and signed difference are complete.
- **Exact missing inputs or definitions:** The paper does not print an alternate denominator for this ETI row, a row-specific weighting rule, retained-precision rate different from `377/943`, or source data identifying which printed element was intended.
- **Source-grounded alternative interpretation:** If the ETI percentage used another unprinted analysis population of approximately 1257 patients, `377` could display as about `30.0%`; however, the cited per-protocol ETI column prints `n = 943`, and the count-derived BMV-minus-ETI difference using `943` reproduces `−5.6`. Another possibility is a production or transcription issue affecting one of the four printed elements, but the supplied source does not identify which one.
- **Direct observation versus inferred explanation:** Direct observations are the cited row label, denominators, counts, percentages, signed difference, CI, P value, and column direction. `40.0%` is only the arithmetic result of applying the printed count and denominator; treating it as intended text would be an inference. An alternate denominator or production issue is also inferred, not directly stated.
- **Exact remaining human question:** Which printed element defines the intended per-protocol ETI ROSC result: `377`, `n = 943`, `30.0%`, or the count-derived signed difference `−5.6`; and was any analysis denominator or weighting rule omitted from Table 2?

## C002 — Per-protocol day-28 survival point difference versus printed counts and denominators

- **Cited location found:** Yes. DOC-001, [main article Table 2, PDF p. 6](../../../jama_jabre_2018_oi_180004.pdf#page=6), Per-Protocol Analysis, row “Survival at 28 d.”
- **Source printed value/text matched:** Yes. The row prints BMV `54 (5.4)`, ETI `51 (5.4)`, proportion difference `0.1 (−10 to 9.7)`, and `P = .99`, beneath the per-protocol denominators BMV `n = 995` and ETI `n = 943`.
- **Comparator printed value/text matched:** Yes. The printed point difference `0.1` is in the `BMV(%) − ETI(%)` column beside the two count/percentage pairs and their stated analysis denominators.
- **Consistency rule applicable:** Yes. If the printed counts and per-protocol denominators define the displayed proportion-difference estimator, the point difference is `100 × (54/995 − 51/943)` and can be compared at the table’s one-decimal precision.
- **Calculation or logical comparison reproduced:** `100 × 54/995 = 5.427136%`; `100 × 51/943 = 5.408271%`; therefore `100 × (54/995 − 51/943) = 0.018864` percentage points. Ordinary one-decimal rounding gives `0.0`, while the table prints `0.1`. The absolute separation between the printed point difference and the count-derived difference is `0.081136` percentage points, greater than half of one one-decimal display unit (`0.05`). The two printed group percentages both round to `5.4%`, so subtracting the displayed percentages also yields `0.0`.
- **Necessary inputs available:** The counts, per-protocol denominators, displayed group percentages, effect direction, point difference, CI, and P value are available. These inputs are complete for the direct count-derived rate-difference check.
- **Exact missing inputs or definitions:** The source does not state whether the point difference used an estimator other than the displayed count/denominator pairs, an alternate denominator, adjusted or weighted rates, or retained values not determined by the printed integer counts. No row-specific point-estimate formula is supplied beyond the proportion-difference heading.
- **Source-grounded alternative interpretation:** A separately computed estimator or unprinted analysis denominator could produce a retained value that rounds to `0.1`, but neither is described for this row. The methods say that differences for secondary criteria expressed as rates were calculated, without specifying a different point estimator for this table cell.
- **Direct observation versus inferred explanation:** Direct observations are the row values, denominators, effect label, CI, P value, and the methods’ general statement. The `0.0` result is conditional on the printed count/denominator pairs defining the point estimator. An unprinted retained-precision or alternate-estimator explanation is inferred.
- **Exact remaining human question:** What exact estimator, analysis denominator, and retained group rates generated the printed `0.1` percentage-point per-protocol survival difference, and do they differ from `54/995` and `51/943`?

## C003 — Per-protocol day-28 survival CI scale versus matched rates and inferential display

- **Cited location found:** Yes. DOC-001, [main article Table 2, PDF p. 6](../../../jama_jabre_2018_oi_180004.pdf#page=6), Per-Protocol Analysis, row “Survival at 28 d,” including the table heading and footnote.
- **Source printed value/text matched:** Yes. The row prints BMV `54 (5.4)`, ETI `51 (5.4)`, difference `0.1`, 95% CI `−10 to 9.7`, and `P = .99`; the per-protocol denominators are `995` and `943`.
- **Comparator printed value/text matched:** Yes. The heading labels the effect and interval as `BMV(%) − ETI(%) (95% CI)`. Footnote `a` says P values were calculated using a chi-square test or Fisher exact test. The methods state that, for secondary criteria expressed as rates, a chi-square test on proportions was used and corresponding 95% CIs on odds ratios and differences were calculated.
- **Consistency rule applicable:** Yes. An interval printed in the proportion-difference column should be on the percentage-point scale of the matched group rates. Its magnitude can be checked diagnostically against a standard unpooled binomial risk-difference calculation, while keeping the exact source-specific CI construction distinct because it is not identified.
- **Calculation or logical comparison reproduced:** The displayed counts yield `5.427136%` and `5.408271%`, with count-derived difference `+0.018864` percentage points. A diagnostic unpooled binomial standard error is `1.028756` percentage points, giving an approximate two-sided 95% interval of `−1.997498` to `2.035226` percentage points. The printed interval spans `19.7` percentage points (`−10` to `9.7`), rather than approximately `4.03` percentage points under this diagnostic construction. The printed `P = .99` is a near-unit P value and is directionally compatible with nearly equal observed rates; it does not supply the missing CI construction.
- **Necessary inputs available:** Counts, denominators, rates, point display, CI display, effect scale, P value, test alternatives, and the general methods statement are available. These are sufficient for the scale/span diagnostic calculation.
- **Exact missing inputs or definitions:** The exact CI formula, software procedure/options, continuity correction, pooled versus unpooled variance choice, any stratification or weighting, any adjusted estimator, and the actual chi-square-versus-Fisher selection for this row are not supplied. The source also does not state whether `−10` or `9.7` lost a decimal during production.
- **Source-grounded alternative interpretation:** A nonstandard or adjusted interval could differ from the diagnostic interval, but the paper does not name such a method for this row. A decimal or transcription issue in one or both limits could also explain the displayed span, but no intended limits are supplied. The table heading grounds the interval on the proportion-difference scale rather than an odds-ratio scale.
- **Direct observation versus inferred explanation:** Direct observations are the counts, denominators, percentages, point difference, interval, P value, heading, footnote, and general methods text. The diagnostic interval comes from an explicitly identified standard approximation and is not an observed or proposed replacement interval. Decimal loss, transcription, adjustment, or method choice are inferred explanations.
- **Exact remaining human question:** Which exact CI method and software settings generated `−10 to 9.7` for the per-protocol survival proportion difference, and do the printed limits contain a decimal or transcription issue?

## C004 — Centre-5 pause result count outcome versus seconds unit

- **Cited location found:** Yes. DOC-001, [main article Results, PDF p. 4](../../../jama_jabre_2018_oi_180004.pdf#page=4), “Post-Hoc Analyses.” The outcome definition also appears in the Methods on [PDF p. 3](../../../jama_jabre_2018_oi_180004.pdf#page=3).
- **Source printed value/text matched:** Yes. The Results say the analysis determined “the number of pauses greater than 2 seconds during CPR” and report BMV `27`, ETI `16`, “difference, `11 seconds` [95% CI, 7 to 15]; `P < .001`.” The same paragraph separately reports chest-compression fraction as ETI `87%`, BMV `86%`, difference `−1%` (95% CI, `−4% to 2%`; `P = .70`).
- **Comparator printed value/text matched:** Yes. The Results’ outcome phrase is a number of qualifying pauses, while `seconds` is attached to the corresponding difference. The Methods call the measure “number of pauses lasting more than 2 seconds”; thus, `2 seconds` is the event-defining threshold in both locations.
- **Consistency rule applicable:** Yes. A difference between two values explicitly presented as numbers of events carries a count unit. A duration unit applies only if `27` and `16` are time summaries rather than event counts. The threshold “greater than 2 seconds” does not by itself change a count of qualifying pauses into elapsed time.
- **Calculation or logical comparison reproduced:** `27 − 16 = 11`. The arithmetic reproduces the printed point difference, but on the stated count interpretation it is 11 pauses, whereas the paragraph labels the difference `11 seconds`. No numerical tolerance is relevant to the count-versus-time-unit comparison.
- **Necessary inputs available:** The outcome wording, threshold, group values, arithmetic difference, reported unit, CI limits, P value, centre subgroup sizes (BMV `56`, ETI `59`), and separate CCF measure are available. These are sufficient for the arithmetic and categorical unit check.
- **Exact missing inputs or definitions:** The source does not define whether `27` and `16` are totals, means, medians, or another summary; does not state the unit intended for those group values or the CI; does not give the CI method; and does not supply patient-level monitor data or total pause durations.
- **Source-grounded alternative interpretation:** The values could be unlabelled duration summaries, in which case `seconds` could apply to the difference, but that reading conflicts with the repeated phrase “number of pauses.” Conversely, they could be pause counts, in which case the `seconds` label attaches the event threshold’s unit to the count difference. The source does not choose between these interpretations explicitly.
- **Direct observation versus inferred explanation:** Direct observations are the named count outcome, 2-second threshold, values `27` and `16`, difference `11 seconds`, CI `7 to 15`, P value, subgroup sizes, and distinct CCF result. Treating the unit label or the outcome description as the production problem is inferred; the source does not identify an intended change.
- **Exact remaining human question:** Were `27` and `16` counts of qualifying pauses or duration summaries, what summary statistic was used, and what unit was intended for the difference and its 95% CI?

## Coverage and limitations

- Stable IDs assigned: 4.
- Stable IDs separately rechecked: 4 (`C001`, `C002`, `C003`, `C004`).
- Cited PDF locations found: 4 of 4.
- Source printed value/text blocks matched: 4 of 4.
- Comparator blocks matched: 4 of 4.
- Arithmetic or logical comparisons reproduced: 4 of 4.
- Candidates with all inputs needed for the stated direct or diagnostic check: 4 of 4.
- Candidates with unprinted information needed to identify the intended source value, exact estimator, exact interval construction, or underlying measure definition: 4 of 4.
- Unresolved source-definition items: C001 (intended ETI ROSC element or alternate denominator), C002 (exact point estimator/retained rates), C003 (exact CI construction and possible decimal/transcription issue), and C004 (group-summary definition and intended count/time unit).

Fresh derivatives were used as locators and transcription aids; they do not provide source data,
unprinted estimators, intended production text, or an adjudication. No candidate is based on a
display-zero P value.
