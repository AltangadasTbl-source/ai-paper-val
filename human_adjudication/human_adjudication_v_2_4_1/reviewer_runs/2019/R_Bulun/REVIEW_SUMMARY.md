# Review summary, 2019 cohort (v.2.4.1 independent primary review)

> Coordinator note (2026-10-14): jama.2019.14231 is an observational study and was removed from the v.2.4.1 cohort after this review was completed. Its 8 judgments were deleted from `judgments.json`, the workbook was refilled from the rebuilt 79-candidate blank, and the counts, lists and sentences below that cited the paper were revised to exclude it. The judgments for the other 79 candidates are unchanged, and nothing else in this summary was edited. The 87-candidate version is in git history.

Reviewer R_Bulun, year 2019, 9 papers, 79 candidates. Independence: I did not open or list the other reviewer's folder or any other reviewer-run folder, any working folder other than my own, anything under `human_adjudication_v_2_3_1/` or `human_adjudication/previous/`, `meta_report/`, the repository paper packages, any `.ai_paper_validation/` folder, or git history. I worked only from the read-only source mirror (original PDFs, `final_report_1_6_2.md` cards, `QUALITY_CONTROL_SCOPE.md`). For each candidate I formed a judgment from the PDFs first and read the card afterwards; where the card changed or extended my view, the workbook note says so.

## Files

- `judgments.json`: one record per candidate (D, E, active H to L fields, note, evidence, full rationale with recomputations).
- `human_adjudication_v_2_4_1_2019_R_Bulun_completed.xlsx`: completed workbook built from the blank R_B template with `fill_review.py`. `recalc_check.py` reports all 79 rows and the Checks sheet as PRIMARY READY (0 unfinished, 0 discuss).
- `REVIEW_SUMMARY.md`: this file.
- Supporting material (private working folder, not a deliverable): extracted text, renders, OCR output and the R scripts used for recomputation (`R/p0556.R`, `p12618.R`, `p17380.R`, `p2210.R`, `p7505.R`; R 4.5.2, base `stats`, no stochastic steps).

## Counts

Disposition: retain 76, exclude 3, discuss 0.

| Review domain (final E) | Retain | Exclude | Discuss |
|---|---:|---:|---:|
| statistical_results | 23 | 3 | 0 |
| protocol_report | 48 | 0 | 0 |
| plan_material | 5 | 0 | 0 |
| report_internal_inconsistency | 0 | 0 | 0 |
| Total | 76 | 3 | 0 |

E changed from the AI suggestion (1):

- `2019::jama.2019.4755::C001`, protocol_report to plan_material. The conflict about which diagnostic metrics form the primary endpoint lies between protocol sections (§3.4/§6.1 and the SAP name sensitivity only; §3.9/§7.2 add specificity and AUC); the article follows the SAP and the endpoint sections.

Exclusions (3):

- `2019::jama.2019.2210::C005`: genotype percentages reproduce with available-case (genotyped) denominators that the counts reveal; only one cell has a 1-point rounding slip.
- `2019::jama.2019.2210::C007`: adjusted HR 0.66 (0.43-0.99), P = .048; a symmetric Wald calculation over the rounding intervals gives P = .043 to .047, a gap of at most 0.001 that a likelihood-ratio or score P would explain.
- `2019::jama.2019.7505::C007`: three Table 2 rows with a CI limit printed as 0 and P < .05 are reproducible from the printed means and SDs once one-decimal rounding of the limits is allowed.

## Outcome codes (retained rows)

statistical_results (23 retained):

| H | minor_presentation | substantive | Total |
|---|---:|---:|---:|
| confirmed_issue | 17 | 5 | 22 |
| probable_issue | 0 | 1 | 1 |
| not_issue / indeterminate | 0 | 0 | 0 |

J (all 23 answered): unlikely 10, possible 9, direct 4.

Confirmed or probable and substantive (6):

- `2019::jama.2019.0556::C010` (probable): the CACE odds ratios cannot be reproduced from the stated estimator; the supplement CACE (0.84) reverses the direction of the ITT estimate (1.06), which a ratio-to-compliance estimator cannot do.
- `2019::jama.2019.14630::C009`: printed percentages in eFigure 2 contradict the bar heights (labels mostly swapped between arms).
- `2019::jama.2019.7505::C001`: the primary effect 0.93 (0.83-1.04) is called a risk ratio in the article and an odds ratio in the supplement and reproduces as neither (crude RR 0.90, 0.77-1.06; OR 0.88).
- `2019::jama.2019.7505::C004`: the "risk ratio" column throughout the report is not the ratio of group risks; for most rows it equals the high-PEEP risk divided by the pooled risk (e.g., pleural effusion printed 1.35, crude 2.04).
- `2019::jama.2019.7505::C010`: in-hospital mortality RR 1.41 (0.95-1.81) for 12 vs 5 deaths; crude RR 2.40 (0.85-6.77).
- `2019::jama.2019.7505::C013`: per-protocol cardiopulmonary edema 1.36 (1.02-1.82) with P = .09; crude RR 2.13 (0.87-5.20).

K (5 plan_material rows): minor_presentation 5.

L (48 protocol_report rows): substantive_difference 39, minor_presentation 7, version_timing 2, indeterminate 0; none left blank. Disclosed changes (for example the 2016 change of primary outcome in jama.2019.17380, the interim scope in jama.2019.14630, post hoc labels) were retained as differences with "disclosed" in the note, following the pre-distribution decision.

## Discuss list

None. Candidates I considered for discuss and why I did not use it:

- `2019::jama.2019.0556::C010`: a latent-class SEM with MI could depart from a simple ratio estimator, but no IV construction under the stated assumptions reverses the sign of the ITT effect; coded probable_issue rather than deferred.
- `2019::jama.2019.2210::C007`: decidable once the attainable P range was computed; excluded.

## Where I disagreed with or went beyond the AI card

- Exclusions (3, listed above): the card registered each as a candidate; I concluded that display rounding, the test construction or available-case denominators explain the observation.
- Domain: `4755::C001` moved to plan_material (see above).
- L = version_timing for `0556::C002` and `C006`: the report follows an undated SAP that may postdate protocol v7.
- Additions to the card's analysis:
  - `0556::C010`: direction reversal of the supplement CACE relative to ITT.
  - `0556::C011`: the three site rows' upper limits appear rotated among rows.
  - `14630::C004`: the eTable 9 footnote (chained equations) contradicts the main text (MCMC, 8 imputations).
  - `14630::C007`: only the main-table 12-month row is a definite conflict; the eTables give -0.1 as the upper limit, so the main table has likely lost a minus sign.
  - `14901::C005`: the four printed percentages are exactly 100 minus the correct ones.
  - `17380::C016`: both vitamin D columns, not only placebo, are inconsistent with the denominators implied by every other year-5 row.
  - `12618::C008`: the power table also ignores the stated second-phase retention (r2 = 0.95).
  - `7505::C008`: the printed percentages use the neuromuscular-blockade denominators (974/961), whereas the differences use 982/984.
  - `7505::C010`: the mortality P value matches an uncorrected chi-square on the counts, but the estimate and interval do not.

## Possible errors outside the candidate set (observed, not adjudicated)

- jama.2019.0556: Table 2 footnote d labels 22/256 (8.6%) as "supplements without therapy" (should be with therapy).
- jama.2019.10517: 11/34 printed as 32.3% (32.4%); the NNT "based on the HR" of 2.8 differs from 1/(0.548 - 0.203) = 2.9.
- jama.2019.12618: Table 2 footnote letters appear shifted by one relative to the rows they annotate.
- jama.2019.14630: eTable 9 baseline weight 86.5 (12.9) kg vs Table 1 86.7 (13.0) kg for the same intervention group (n = 3272).
- jama.2019.14901: the abstract and text give the postextubation respiratory failure difference as -8.7%, Table 2 as -8.5% (88/302 - 70/339 = -8.49%); the protocol secondary outcome "ventilatory support-free days within 14 days" is not reported.
- jama.2019.2210: baseline 25(OH)D middle group, vitamin D arm, 142/248 = 57.3% printed 58%; ApaI placebo GT 61/150 = 40.7% printed 40%; missing-genotype counts are not stated.
- jama.2019.7505: the risk-ratio problem (C004) affects every binary row, including the subgroup forest plot (Figure 2), beyond the rows registered as separate candidates.

## Template or source issues

- jama.2019.12618: the protocol supplement (`joi190092supp2_prod.pdf`) has 20 image-only pages without a text layer, including cited pp. 15, 80, 81 and 136; these required OCR.
- jama.2019.7505 C012: the location cites a derived image (`protocol-p32-coma-detail.png`) that is not in the source mirror. The protocol p. 32 text layer drops the underline of the "less than or equal to" symbol, so text extraction alone reads "< 8"; only the rendered page shows the difference.
- Cards link to verification and audit files under `review_1_6_2/` that are not in the mirror; they were not needed.
- Column C for `jama.2019.10517::C002` is about 2,500 characters long. I found no wrong page locations and no mismatch between workbook titles and card titles.
- Several JAMA main-article text layers run words together; this did not affect any value I relied on, and table values were checked on rendered pages.

## OCR and rendering use

- OCR (RapidOCR, GPU, 300 dpi): jama.2019.12618 `joi190092supp2_prod.pdf` pp. 15, 80, 81, 136 (image-only protocol pages; table rows had confidence >= 0.91 and were checked against the rendered page).
- Rendering (PyMuPDF, 110-400 dpi), used where layout or symbols mattered:
  - jama.2019.0556: main p. 3 (Figure 1); supp3 p. 19 (Table B).
  - jama.2019.12618: SAP pp. 67-68 (power table); supp1 p. 15 (eTable 9).
  - jama.2019.14630: supp3 pp. 7, 15, 22-24, 26; main Table 3 alcohol rows (crop, 200 dpi).
  - jama.2019.14901: supp2 p. 4 (eTable 2).
  - jama.2019.17380: main pp. 7-9 (Figures 2-4, Tables 2-3); supp2 pp. 7, 12, 18, 19.
  - jama.2019.7505: main pp. 7-11 (Tables 2-3); supp4 pp. 29, 30, 38, 42; 400-dpi crop of protocol p. 32 and 300-dpi crop of supp4 p. 21 (coma definition).
- All other pages were read from the PDF text layer.

## Limitations

- One reviewer, one pass. I read each card after forming my own judgment, but for long candidates the card may still have influenced which supporting pages I checked.
- Absence claims (planned analysis not reported) rest on reading the cited sections and on text searches of all report PDFs; image-only report pages, if any, would not be searched. None of the report supplements in this cohort lacked a text layer.
- Several recomputations infer unstated quantities: arm denominators in `17380::C016`, bar heights read visually (about +/- 2 points) in `14630::C009`, and the reverse-engineered RR construction in `7505::C004`. The conclusions are stated with that uncertainty.
- L codes describe the size of the plan-report difference, not whether it was justified; they involve judgment, particularly for omitted conjunctive criteria (`10517::C001`, `14901::C001`) and technical analysis changes (`17380::C009`).
- I read the protocol and SAP sections cited by each candidate and searched them for related text, but did not read every page of the longer protocols (up to 153 pages), so plan content outside those sections could bear on a few protocol_report rows.
