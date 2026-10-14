# v.2.4.1 independent primary review, 2019: reviewer R_A

Reviewer R_A. Independence: I reviewed all 87 candidates from the original PDFs in the 2019 source mirror. Each candidate's card in `final_report_1_6_2.md` was read only after I had formed a judgment. I did not open or list the other reviewer's folder, any other year or role folder under `reviewer_runs/`, `human_adjudication_v_2_3_1/`, `human_adjudication/previous/`, `meta_report/`, the repository paper packages, any `.ai_paper_validation/` folder, or git history. I worked alone and used no delegated reviewers.

## Files

- `human_adjudication_v_2_4_1_2019_R_A_completed.xlsx`: completed workbook. Built with `fill_review.py` from the blank R_A template. `recalc_check.py` reports 87/87 rows `PRIMARY READY` and Checks `Workflow status` = `PRIMARY READY`, with 0 discuss and 0 unfinished rows.
- `judgments.json`: one row per candidate. Each row holds D, E, H–L, the column R note, the evidence (files, pages, and whether pages were rendered or OCR'd) and the full rationale with recomputations.
- `REVIEW_SUMMARY.md`: this file.

## Counts

Dispositions: 82 retain, 5 exclude, 0 discuss (87 total).

| Review domain (final E) | retain | exclude | discuss | total |
|---|---:|---:|---:|---:|
| statistical_results | 25 | 5 | 0 | 30 |
| report_internal_inconsistency | 0 | 0 | 0 | 0 |
| plan_material | 5 | 0 | 0 | 5 |
| protocol_report | 52 | 0 | 0 | 52 |

E changed from the pipeline suggestion (1):

- `2019::jama.2019.4755::C001`, protocol_report → plan_material. The conflict is inside the protocol: §3.9 and §7.2 call sensitivity, specificity and AUC the "primary endpoint", while §3.4, §6.1 and §7.1 name sensitivity only. The report agrees with the SAP and with the protocol's formal endpoint lists.

Exclusions (5):

- `2019::jama.2019.14231::C003`: the cerebrovascular unadjusted 8-year risk-difference CI includes 0 while the adjusted Cox HR is significant. These are different estimands, as the table footnotes state.
- `2019::jama.2019.14231::C007`: eTable 8 year-5 hemoglobin −0.1 (−0.2, 0) with P < .001 is reproducible within one-decimal rounding (for example, −0.14 [−0.24, −0.04] with z ≈ 3.5).
- `2019::jama.2019.2210::C005`: genotype percentages use available-case denominators that can be derived by summing the rows. All 42 cells reproduce; one trivial rounding slip.
- `2019::jama.2019.2210::C007`: age-adjusted HR 0.66 (0.43–0.99), P = .048. A strict log-Wald reconstruction gives P of .043–.047. A gap of under .001 is within Wald-versus-likelihood test differences, and the interval and P agree on significance.
- `2019::jama.2019.7505::C007`: three Table 2 rows with a CI limit printed as 0 and P < .05 are reproducible within display rounding, using SEs recomputed from the printed SDs and group sizes.

## Outcome codes (retained rows)

statistical_results (25 retained):

- H: confirmed_issue 22, probable_issue 3 (`0556::C010`, `14231::C008`, `17380::C016`), not_issue 0, indeterminate 0.
- I: substantive 11, minor_presentation 13, indeterminate 1 (`14231::C008`).
- J (optional, all filled): direct 4, possible 9, unlikely 12.

Confirmed or probable and substantive (11):

- `0556::C010`: CACE MDD odds ratios cannot follow from the stated ratio method. The supplement odds ratio reverses direction (ITT 1.06 vs CACE 0.84), and the therapy CACE 0.78 does not reproduce (0.90 expected).
- `12618::C005`: missed-dose summaries 4.6 (1.0) vs 4.3 (0.5) give a Welch P of .009, not the printed .87.
- `14231::C002`: five 8-year absolute risk differences do not equal the difference of the displayed cumulative incidences.
- `14630::C007`: the 12-month alcohol interval −0.2 (−0.4 to 0.1) cannot coexist with P = .01. The feasible range is P .12–.33.
- `14630::C009`: eFigure 2 percentage labels are interchanged against the bars in 6 of 7 pairs.
- `17380::C012`: forest-plot participant counts are assigned to the opposite treatment column in Figures 3–4 and eFigures 2–3.
- `17380::C018`: the favor labels on the albuminuria ratio forests are reversed.
- `2210::C006`: the Table 2 footnote reverses the HR direction.
- `7505::C001`: the primary "RR" 0.93 (0.83–1.04) is labeled OR in eFigure 12 and is neither (true RR 0.90, OR 0.88).
- `7505::C004`: every binary "risk ratio" in Table 3 and eTable 8 equals P(high PEEP | event)/P(high PEEP | no event); exposure and outcome are reversed (for example, pleural effusion printed 1.35, true RR 2.04).
- `7505::C010`: the in-hospital mortality CI is not reproducible by the construction used for every other row (true RR 2.40).

K (plan_material, 5 retained): minor_presentation 5. These are `12618::C008` (power-table sequence labels), `12618::C009` ("17%" for a 25-point difference), `17380::C014` (2000 IU given as 40 µg), `17380::C015` (interaction equation without a time main effect) and `4755::C001`.

L (protocol_report, 52 retained): substantive_difference 37, minor_presentation 5, indeterminate 3, version_timing 2, non_inconsistency 0. Left blank: 5 (`12618::C001`, `14231::C006`, `14630::C006`, `17380::C009`, `2210::C003`). All five are planned outputs or technical specifications whose importance I chose not to grade; for example, a risk ratio is not reported but the counts allow it to be computed. Disclosed changes were retained and marked "disclosed" in R, per the fixed review decision: `0556::C007`, `10517::C005`, `14630::C001`, `17380::C001` and `2210::C004`.

## Discuss list

None. Candidates I considered for discuss:

- `0556::C010`: the CACE structural model is unspecified. I coded probable_issue rather than discuss because the direction reversal is hard to reconcile with any instrumental-variable CACE.
- `14231::C008`: the E-value transformation is unstated. I coded probable_issue.
- `2210::C007`: a near-miss P value. I excluded it, as explained above.
- `14231::C004`: whether the plan's pointer to "eTable 1" already contained the primary-diagnosis rule. I retained it with L = indeterminate.

## Where I disagreed with or went beyond the AI card

- `7505::C004`, C001, C009, C010, C013: the card leaves the estimand mapping "unidentified". I identified it. All 21 Table 3 ratios and their CIs reproduce exactly as the ratio with outcome and exposure exchanged, so the reported risk ratios are systematically wrong and attenuated, not merely mislabeled.
- `14231::C008`: the card places the problem in the primary E-value pair. I found that the primary pair matches the common-outcome (square-root) conversion and the other rows use the rare-outcome formula. The undisclosed mix of methods is the issue, and it likely overstates the secondary E-values (for example, mortality 2.81 vs 2.24).
- `2210::C007` and `14231::C007`: the card registers interval/P conflicts. I excluded both as rounding or test-construction effects.
- `0556::C003`: I added the plausibility argument (1451/5965 excluded for "BMI <15" is implausible; only 18 were excluded at telephone screening for BMI <25).
- `17380::C016`: I found that both vitamin D SGLT2 cells fail, not only the placebo cell. I coded probable rather than confirmed, because SGLT2 use was first asked at year 5.
- `4755::C001`: domain changed to plan_material (see above).

## Possible errors outside the candidate set (observed, not adjudicated)

- jama.2019.0556, Table 2 footnote d: 22/256 (8.6%) is labeled "supplements without therapy" (should be "with therapy"). eAppendix 10 Table B prints the baseline GAD-7 P as "0".
- jama.2019.10517, Table 1 hyperlipidemia: 18 (29.0) [n = 64] and 19 (29.7) [n = 62]. The percentages match the counts swapped between columns (19/64 = 29.7; 18/62 = 29.0).
- jama.2019.14231: the main text (p. 7) gives "95% CI" for the 8-year weight (20.3 kg) and HbA1c differences, while eTable 8 labels the same contrasts with 98.8% intervals that differ slightly.
- jama.2019.17380, eTable 7: the footnote says the complete-case table "accounts for missing data using multiple imputation".
- jama.2019.2210: the Figure 3 caption says numbers at risk are not given for panel C, but panel C shows them. Table 1 ApaI placebo GT 61/150 = 40.7% is printed as 40.
- jama.2019.7505, Table 2: "Heat rate" (typographic).

## Template or source issues

- jama.2019.12618 Supplement 2 (protocol): pages 15, 19, 74, 80, 81, 84, 89–91, 94, 96, 105, 107, 109, 116, 118, 120, 133, 134 and 136 have no text layer. The candidate locations p. 80, 81 and 136 are among them.
- jama.2019.7505 protocol p. 32: the coma threshold "≤ 8" is printed as an underlined "<". The text layer gives "< 8", so the glyph had to be read from the rendered page.
- jama.2019.14901: the report cites "a predefined statistical analysis plan" that is not in the package. Only the protocol is supplied, so C003 rests on the protocol alone.
- jama.2019.4755 C001 and jama.2019.12618 C002–C004: the column C location strings are long joined lists, but every cited page could be located.
- No mismatch was found between workbook titles or keys and the card numbers.

## OCR and rendering use

- OCR (RapidOCR, 300 dpi): jama.2019.12618 Supplement 2 pp. 15, 80, 81, 136 (scanned protocol pages). The p. 81 lab-threshold table was checked against the rendered image.
- Rendered and read visually:
  - 0556 main p. 3 (Figure 1 BMI label, 250 dpi).
  - 14231 main p. 7 (Table 2, 200 dpi). eTable 1 bold spans were checked through PDF font data.
  - 14630 main p. 7 alcohol rows (250 dpi) and Supplement 3 p. 26 (eFigure 2, 220 dpi).
  - 17380 main pp. 7–9 and Supplement 2 pp. 7, 11, 12, 18, 19 (170 dpi).
  - 2210 main pp. 6–8 (170 dpi).
  - 7505 main pp. 7–10 (180 dpi), Supplement 4 pp. 29, 38, 42 (170 dpi) and protocol p. 32 coma line (300 dpi).
- All other pages were read from the PyMuPDF text layer.

## Limitations

- Recomputations use the printed summary data. Where authors used model-based, bootstrap, Rubin-pooled or nonstandard constructions, as in the CACE structural model, the cumulative-incidence ARDs and the E-value conversions, I cannot reproduce their exact fits. I graded certainty accordingly (probable rather than confirmed).
- Protocol and SAP version chronology is incomplete for several papers (0556, 17380, 2210). Version-dependent L codes are therefore approximate.
- L was left blank for five retained protocol_report rows. As the review decisions state, blank means "not described", not "no difference".
- Substantiveness judgments (I, L) involve reviewer judgment about likely extraction and interpretation. Another reviewer could reasonably grade borderline rows differently, for example `7505::C002` and `17380::C013`.
