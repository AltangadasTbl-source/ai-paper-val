# Stable Candidate Ledger

## Registration method

This ledger reconciles the temporary propositions in `checkers/numeric_consistency.md`,
`checkers/statistical_pass_1.md`, and `checkers/cross_source_consistency.md` against the
fresh DOC-001 evidence. Propositions were merged only where they compare the same printed
values using the same comparator and consistency rule. All candidates remain **Pending Human
Adjudication**. No severity, validity judgment, correction, or disposition is assigned.

| Stable ID | Merged temporary proposition(s) | Merge rationale |
|---|---|---|
| C001 | NUM-CAND-001; STAT1-CAND-002; CROSS-CAND-001 | Same PP ROSC cell, numerator/denominator, percentage, and signed difference; same percentage/denominator and direction rule. |
| C002 | NUM-CAND-002; STAT1-CAND-001 | Same PP day-28-survival counts, denominators, displayed point difference, and one-decimal percentage-point rounding rule. |
| C003 | CROSS-CAND-002 | Distinct comparator and rule from C002: the printed 95% CI/P-value scale versus the matched rates, rather than the displayed point-difference rounding. |
| C004 | NUM-CAND-003 | Distinct Centre-5 count-versus-time-unit rule and printed narrative evidence. |

## C001 — Per-protocol ETI ROSC percentage does not reconcile with its printed numerator, denominator, and signed difference

- **Status:** Pending Human Adjudication.
- **Category:** Denominator, proportion, or total inconsistency.
- **Source locations:** DOC-001, [main article Table 2, PDF p. 6](../../jama_jabre_2018_oi_180004.pdf#page=6), Per-Protocol Analysis, “Return of spontaneous circulation”; fresh layout evidence: `preprocessing/pymupdf_layout_text/DOC-001_jama_jabre_2018_oi_180004.txt` (Table 2).
- **Lane provenance:** NUM-CAND-001; STAT1-CAND-002; CROSS-CAND-001; canonical relationships N022 and S008.
- **Direct printed evidence:** BMV is `342 (34.4)` of PP `n = 995`; ETI is `377 (30.0)` of PP `n = 943`; the table prints BMV-minus-ETI difference `−5.6 (−9.9 to −1.3)` and `P = .01`.
- **Comparator:** The ETI count and stated PP denominator, plus the signed BMV-minus-ETI difference in the same matched PP ROSC row.
- **Reproducible rule and calculation:** A `No. of Patients (%)` entry must equal `100 × count / stated denominator`, to one decimal within 0.05 percentage points (pp). `100 × 377 / 943 = 39.979%`, which rounds to `40.0%`, not `30.0%`. Also, `100 × (342/995 − 377/943) = −5.607 pp`, compatible with the printed `−5.6 pp`; the displayed percentages instead give `34.4 − 30.0 = +4.4 pp`.
- **Tolerance:** The ETI percentage differs from the count-derived value by 9.979 pp, exceeding the 0.05-pp one-decimal rounding tolerance.
- **Direct observation versus inference:** Directly observed are the count, denominator, `30.0%`, and negative difference. The suggestion that `40.0%` is the intended display is an inference only; this ledger does not make that correction.
- **Source-grounded alternatives:** A different denominator near 1257 could yield 30.0%, but no such denominator is printed for this PP row. Alternatively, one or more of the printed count, denominator, percentage, or difference may require source verification.
- **Quality-control relevance:** This joins a proportion, denominator, and signed risk difference; a mismatch can mislead direct extraction of this secondary outcome for later evidence products.
- **Human question:** Which PP ROSC element is intended: does the ETI entry correspond to `377/943 (40.0%)`, or does another printed element use a different analysis population?

## C002 — Per-protocol day-28 survival point difference is not supported by the printed counts and denominators at one-decimal precision

- **Status:** Pending Human Adjudication.
- **Category:** Numeric or arithmetic inconsistency.
- **Source locations:** DOC-001, [main article Table 2, PDF p. 6](../../jama_jabre_2018_oi_180004.pdf#page=6), Per-Protocol Analysis, “Survival at 28 d”; fresh layout evidence: `preprocessing/pymupdf_layout_text/DOC-001_jama_jabre_2018_oi_180004.txt` (Table 2).
- **Lane provenance:** NUM-CAND-002; STAT1-CAND-001; canonical relationships N021 and S008.
- **Direct printed evidence:** The PP row prints BMV `54 (5.4)` of `n = 995`, ETI `51 (5.4)` of `n = 943`, and BMV-minus-ETI difference `0.1 (−10 to 9.7)`, `P = .99`.
- **Comparator:** The displayed BMV-minus-ETI percentage-point difference in the same PP survival row.
- **Reproducible rule and calculation:** For the stated percentage-point difference, `100 × (54/995 − 51/943) = 0.018864 pp`. Standard rounding to one decimal yields `0.0 pp`; a printed `0.1 pp` represents values from 0.05 pp through less than 0.15 pp under ordinary rounding.
- **Tolerance:** `|0.100000 − 0.018864| = 0.081136 pp`, exceeding the 0.05-pp one-decimal rounding tolerance.
- **Direct observation versus inference:** Directly observed are the counts, denominators, individual percentages, and `0.1` point difference. The conclusion that the point display should be `0.0` follows only if the printed count/denominator pairs define the displayed estimator; it is not a correction.
- **Source-grounded alternatives:** The table may use an unprinted retained-precision calculation, alternate denominator, or differently defined PP estimator. Neither the row nor its footnote supplies such an alternative. The separate printed individual percentages both round to 5.4%.
- **Quality-control relevance:** A point estimate that does not reproduce from its displayed numerator/denominator can affect quantitative extraction, even without judging the study conclusion.
- **Human question:** What estimator and denominator generated the printed PP survival difference of `0.1 pp`, and are they the same as the displayed `54/995` and `51/943`?

## C003 — Per-protocol day-28 survival confidence interval has a scale inconsistency with the displayed rates and same-row inferential display

- **Status:** Pending Human Adjudication.
- **Category:** Statistical reporting inconsistency.
- **Source locations:** DOC-001, [main article Table 2, PDF p. 6](../../jama_jabre_2018_oi_180004.pdf#page=6), Per-Protocol Analysis, “Survival at 28 d”; fresh simple/layout evidence: `preprocessing/pymupdf_simple_text/DOC-001_jama_jabre_2018_oi_180004.txt` and `preprocessing/pymupdf_layout_text/DOC-001_jama_jabre_2018_oi_180004.txt` (Table 2).
- **Lane provenance:** CROSS-CAND-002; canonical relationships N021 and S008.
- **Direct printed evidence:** The PP survival row prints BMV `54/995 (5.4%)`, ETI `51/943 (5.4%)`, difference `0.1`, 95% CI `−10 to 9.7`, and `P = .99`. The table heading defines the column as BMV(%) minus ETI(%), and its footnote says P values use chi-square or Fisher exact test.
- **Comparator:** The matched PP survival event rates and same-row near-unit P-value display, on the table’s percentage-point difference scale.
- **Reproducible rule and calculation:** The displayed counts yield rates `5.427%` and `5.408%` and a difference of `+0.018864 pp`. As a diagnostic approximation only, an unpooled binomial standard error from the displayed count/denominator pairs is about `1.03 pp`, giving an approximate 95% risk-difference interval of about `−2.00 to 2.04 pp`, rather than a printed interval spanning 19.7 pp (`−10 to 9.7`). The same-row `P = .99` is retained as observed near-null context; without the row-specific CI construction it does not independently contradict the printed interval.
- **Tolerance:** No rounding tolerance applies: the issue is the printed confidence-interval scale/span versus the matched supplied values. The approximate calculation is diagnostic, not a replacement CI method.
- **Direct observation versus inference:** Directly observed are the rates, point difference, CI, P value, column label, and test-method alternatives. The incompatibility diagnosis uses a standard unpooled binomial approximation; no row-specific CI construction, chi-square/Fisher selection, variance estimator, or intended CI limits are supplied.
- **Source-grounded alternatives:** A different CI method, alternate unprinted analysis set, or decimal/production issue could explain the display, but the source does not identify one. This candidate does not assert an intended replacement interval.
- **Quality-control relevance:** A confidence interval whose displayed scale does not reconcile with the matched effect display may affect statistical extraction and later evidence products.
- **Human question:** What generated 95% BMV-minus-ETI CI limits correspond to the PP survival analysis, and does the printed `−10 to 9.7` interval have a scale or transcription problem?

## C004 — Centre-5 pause difference uses a time unit for a named count outcome

- **Status:** Pending Human Adjudication.
- **Category:** Measure, label, or scale inconsistency.
- **Source locations:** DOC-001, [main article Results, PDF p. 4](../../jama_jabre_2018_oi_180004.pdf#page=4), “Post-Hoc Analyses”; fresh simple/layout evidence: `preprocessing/pymupdf_simple_text/DOC-001_jama_jabre_2018_oi_180004.txt` and `preprocessing/pymupdf_layout_text/DOC-001_jama_jabre_2018_oi_180004.txt` (Centre No. 5 text).
- **Lane provenance:** NUM-CAND-003; canonical relationship N025.
- **Direct printed evidence:** The report names the outcome “number of pauses greater than 2 seconds during CPR,” then reports BMV `27` versus ETI `16`, “difference, `11 seconds` [95% CI, 7 to 15]; P < .001.” It separately describes chest-compression fraction as `86%` versus `87%`.
- **Comparator:** The stated outcome measure, a number of pauses, versus the `seconds` unit attached to the corresponding difference and confidence interval.
- **Reproducible rule and calculation:** `27 − 16 = 11`, consistent with a count difference of 11 pauses. For a named count outcome, the difference and its interval should carry the count measure (pauses), whereas “greater than 2 seconds” is the threshold defining counted events rather than the unit of the count.
- **Tolerance:** None; this is a categorical measure/unit check.
- **Direct observation versus inference:** Directly observed are the phrase “number of pauses,” the counts 27 and 16, and the `11 seconds` difference/CI label. The inference is that the unit label, rather than the underlying data, may be the source of the mismatch; no correction is assigned.
- **Source-grounded alternatives:** The values 27 and 16 could be undisclosed time summaries, but that would conflict with the explicitly stated count outcome. The supplied paper does not provide the underlying monitor data or a separate duration summary.
- **Quality-control relevance:** Confusing a count with a duration can misstate the measure and unit available for quantitative evidence extraction.
- **Human question:** Were 27 and 16 counts of pauses, in which case should the difference/CI be labeled in pauses, or were they time quantities requiring the outcome description to be revised?

## Display-zero exclusion and registration totals

No candidate was registered solely because of a display-zero P value. The reviewed lanes report no `P = 0`, `p = 0.000`, or equivalent display-zero proposition; `P < .001` and `P < .0001` are threshold displays and are not candidates. Registration inputs: 7 temporary propositions. Genuine duplicate groups: 2 (C001 merges 3 propositions; C002 merges 2). Stable candidates: 4.

## Limitations

The ledger uses only supplied local evidence and fresh review-lane propositions. It does not establish an intended correction, source-data value, or study-level conclusion. C003 retains an explicitly labelled diagnostic approximation because the source does not supply a row-specific confidence-interval construction; this missing definition remains part of its human question.
