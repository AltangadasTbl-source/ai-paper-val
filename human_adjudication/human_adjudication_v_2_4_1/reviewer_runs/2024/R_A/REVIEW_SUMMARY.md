# v.2.4.1 independent primary review, 2024 — reviewer R_A

Reviewer R_A reviewed all 113 candidates in the 2024 workbook against the original PDFs in the source mirror. For each candidate the judgment was formed from the PDFs first, and the final report card (`final_report_1_6_2.md`) was read afterwards. R_A did not open or list the other reviewer's folder, any other year or role folder under `reviewer_runs/`, `human_adjudication_v_2_3_1/`, `human_adjudication/previous/`, `meta_report/`, the repository paper packages or any `.ai_paper_validation/` folder, or `2024/jama.2024.2302/Detailed_Errors_On_C1_C3_C5.docx`. Git history was not used.

## Files

- `judgments.json`: 113 rows (D, E, H–L, column R note, evidence, rationale with recomputations).
- `human_adjudication_v_2_4_1_2024_R_A_completed.xlsx`: built with `fill_review.py`. `recalc_check.py` reports 113/113 rows `PRIMARY READY`, Checks workflow status `PRIMARY READY`, 0 discuss and 0 unfinished rows.
- `REVIEW_SUMMARY.md`: this file.

Working files (text extractions, renders, OCR output, R scripts) are in the private scratch folder and are not deliverables.

## Counts

Disposition: 103 retain, 10 exclude, 0 discuss.

| Review domain (final E) | Retain | Exclude | Discuss | Total |
|---|---:|---:|---:|---:|
| statistical_results | 46 | 5 | 0 | 51 |
| protocol_report | 42 | 0 | 0 | 42 |
| plan_material | 11 | 5 | 0 | 16 |
| report_internal_inconsistency | 4 | 0 | 0 | 4 |
| Total | 103 | 10 | 0 | 113 |

E changed from the AI suggestion (4):

- `2024::jama.2024.0572::C008` statistical_results → report_internal_inconsistency. The conflict is about which core-volume variable (CTP/MRI vs composite) the age/time prediction surfaces use. It is a labeling conflict, not a numerical error.
- `2024::jama.2024.11057::C003` protocol_report → report_internal_inconsistency. Main text (6 prequit weeks) conflicts with the results supplement (1 week). The protocol only corroborates the supplement.
- `2024::jama.2024.12829::C006` protocol_report → statistical_results. The printed P values reproduce exactly with Fisher's test, which is the method the SAP specifies. The problem is the report's "chi-square" footnote label, not a deviation from the plan.
- `2024::jama.2024.23898::C009` protocol_report → plan_material. The report's Cox models follow SAP section 11.4. The conflict is between that section and the SAP's own shell tables and sample code.

Exclusions (10):

- `0572::C005`: aGenOR 0.91 (0.82–1.00) and aRR 0.97 (0.93–1.00) are called significant. Upper limits that round to 1.00 are compatible with P < .05, so this is a rounding boundary.
- `0572::C011`, `0572::C012`: inconsistencies in the protocol's background summary of the earlier SELECT cohort. These are not design elements.
- `0572::C013`: orientation of the parent trial's interim Wilcoxon hypothesis. Real, but not relied on by this exploratory analysis.
- `0572::C019`: final-stage subgroup rescue branch that differs between protocol and trial SAP. It was never executed, and this analysis does not rely on it.
- `12829::C007`: original-protocol sample-size forecast (91 events is the required count at 90% power; 686 participants matches 80% power). Superseded by the amended 512-patient design.
- `19585::C001`: the ED absolute difference (CrI) and the rate ratio come from explicitly different models.
- `19585::C006`: sadness OR (0.26–0.99) with P = .05. This is a rounding boundary.
- `25786::C008`: SSI OR (CI excludes 1) and RD (CI includes 0) come from different models. No inconsistency is demonstrable.
- `25786::C010`: the "ICU admission" subgroup counts reconcile with the immediate-destination-ICU variable, not the ICU-admission outcome.

## Outcome codes (retained rows)

statistical_results (46 retained):

- H: 45 confirmed_issue, 1 probable_issue.
- I: 15 substantive, 31 minor_presentation.
- J: 4 direct, 11 possible, 31 unlikely.

Confirmed or probable and substantive (15): `0318::C003`, `0572::C001`, `0572::C004`, `0572::C006`, `0572::C007`, `0572::C018`, `2302::C001`, `25786::C001`, `4183::C002`, `4183::C004`, `4183::C005`, `4183::C009`, `6063::C008`, `6063::C009`, `6063::C010`.

K, for 11 retained plan_material and 4 retained report_internal_inconsistency rows:

| K code | plan_material | report_internal_inconsistency |
|---|---:|---:|
| minor_presentation | 6 | 2 |
| substantive_inconsistency | 3 | 2 |
| indeterminate | 2 | 0 |

L, for 42 retained protocol_report rows:

| L code | Rows |
|---|---:|
| substantive_difference | 37 |
| indeterminate | 3 (`0318::C005`, `25786::C002`, `25786::C006`) |
| minor_presentation | 1 (`0318::C006`) |
| blank | 1 (`23898::C007`) |

`23898::C007` was left blank because the omitted unadjusted displays are real but of low importance. Disclosed changes were retained as differences, with "disclosed" or "documented in SAP" noted in column R: `2302::C002` (GEE after nonconvergence), `23898::C006` (post-analysis SAP correction of the link function), `25786::C003`, `C004` and `C007` (changes documented in the prospectively approved SAP), and `4183::C001` (assignment of nonreturners).

## Discuss list

None. Candidates considered for discuss:

- `25786::C002`: population for the 1600 accrual cap.
- `2302::C003`: which prior width was actually used.
- `4183::C002`: weights for 75 nonrandomized continuers.
- `0572::C014`: rule applied at the unscheduled 300-patient look.
- `6063::C011`: effusion power that does not reproduce.

In each case the existence of the inconsistency or difference could be established from the documents. Only its cause or consequence could not, so these were retained with indeterminate codes, or with the reason stated, rather than deferred.

Scope exclusions of parent-trial or superseded plan material (`0572::C013`, `C019`; `12829::C007`) are judgment calls the coordinator may wish to compare with the other review.

## Where I disagreed with or went beyond the AI card

- `0572::C006`: I identified the mechanism. Figure 2B's category colours are shifted by one: there is no mRS 2 segment for EVT and no mRS 1–2 segment for MM. With the shift, the figure reconciles exactly with eFigures 7–8 and the discussion.
- `0572::C004`: the placeholder interval 0.37–2.72 equals exp(±1). The same figure marks other non-estimable rows with "*".
- `12829::C002`: the headers of Tables S7 and S8 are swapped. S7's events and site totals match the primary population; S8's percentages match the per-protocol denominators. `12829::C003`: the BA cell of Table S6 was copied from the per-protocol table (9/233 = 3.9%).
- `12829::C006`: this is not a plan deviation (see E changes).
- `19585::C005` and `C007`: the ORs and CIs reproduce exactly with a 0.5 continuity correction (Woolf). The P values reproduce exactly with Fisher's exact test, not the logistic regression named in the footnote.
- `25786::C010`: excluded. The card did not consider the Table's destination-after-resuscitation row.
- `25786::C013`: 5.3% is a misprint for 0.5% (column sums). `25786::C015`: the percentages are shares of excluded patients. `25786::C012`: other receiving-centre percentages are also slightly off.
- `4183::C002`: I added the substantive concern that the nonrandomized nonreturners make up 40/90 and 35/77 of the continuation reference arms.
- `4183::C009`: the main-text CNRT six-month figures are risk differences presented as arm rates.
- `6063::C013`: every row of eTable 5 prints pooled percentages, not arm-specific ones.
- `6063::C008` and `C012`: the hsCRP 12-week and glucose 12-week contrast tuples are the same hybrid row.
- `6063::C005`: the protocol's primary power also does not reproduce (SD 25.5 with 117 per group gives 85%, not 90%).
- `0318::C013`: the report's flow (39 withdrew before intervention, 316 eligible) also differs from the plan's 325 initiated.
- Three candidates I retained as differences although the report follows a later, prospectively approved SAP (`25786::C003`, `C004`, `C007`), consistent with the fixed decision that documented changes remain differences.

## Possible errors outside the candidate set (observed, not adjudicated)

- 0318: eTable 1 gives White 176; main Table 1 sums to 177 (59 + 118). The abstract's 67.2% matches 176.
- 0572: MM infarct growth IQR is 56–125 mL in the main text (p9) but 56–135 in eTable 11. "aRR" is expanded as "absolute risk reduction" while the footnote describes a rate ratio (Table 2, p6–7).
- 4183: main p4 says the 40/35 nonreturners "did attend rerandomization"; the abstract and Figure 2 say they did not.
- 23898: 24-hour postoperative opioid medians (70.6 vs 45.0 mg OME) are reported without an effect estimate, while the text states no significant difference.
- 25786: Figure 2 risk differences depart from crude differences, in sign for the primary outcome (+0.56 printed; crude 16.1% − 16.7% = −0.6), and the RD method is not described. eTable 2 firearm row uses denominator 724 where the rest of the column uses 742. eTable 10 row N = 130 vs 55 + 67 = 122.
- 6063: Table 3 "pain in extremity" placebo is 6, but 5 in the abstract, text and eTable 7. "Participants with an adverse event" 67 (50.7%) should be 67/130 = 51.5% (50.7% is 67/132).

## Template or source issues

- `jama.2024.0572` Supplement 3 (trial SAP, 40 pages) has no text layer, so OCR was required.
- The 4183 protocol supplied as Supplement 1 is dated 23 August 2023, after trial completion (October 2019). Its relation to the prospective plan is unknown, which affects all of that paper's protocol_report rows.
- The 6063 "SAP" (Supplement 2) is a one-page excerpt of protocol version 2.
- Some candidates overlap: `6063::C008` and `C012` share the hsCRP/glucose 12-week tuple; `0318::C007` and `C009` both involve the added baseline HbA1c covariate.
- No mismatches between cards and workbook keys or titles were found. Column C entries were long but located the right pages throughout.

## OCR and rendering use

OCR (RapidOCR, GPU): 0572 Supplement 3 pages 1, 9–14, 17, 18, 31, 39 and 40. These are scanned pages of the trial SAP, needed for C010, C013–C015 and C019. Minimum line confidence was ≥0.94 on the lines used, and page 12 was checked against the rendered image.

Rendered and viewed:

| Paper | Pages | Purpose |
|---|---|---|
| 0318 | Main p6 (Table 2) | C001, C010 |
| 0572 | Main p7 (Figure 2) | C006 |
| 0572 | Supplement 5 pp13–14, 19, 23, 24 (eFigures 7, 8, 13, 17, 18; image-only forest plots and curves) | C004, C006, C007, C008, C017 |
| 12829 | Supplement 1 p13 (Figure S4) | C005 |
| 23898 | Supplement 3 p2 (subgroup eFigure, image) | C013 |
| 6063 | Supplement 3 pp10–11 (eTable 7) and p14 (eTable 8) | Column attribution, C009 and C010 |

All other values were read from the PyMuPDF text layer.

## Limitations

- Figure-based judgments rest on visual reading of curve directions and bar segments, without digitization: 0572 C006, C007; 23898 C013.
- Where a producing method is not described, the inference is by reproduction rather than documentation. Examples: continuity-corrected ORs and Fisher P values in 19585; geometric-midpoint checks for GEE ORs in 0318; root-sum-square interval widths in 6063.
- Scope exclusions of parent-trial or superseded plan material depend on reading "relies on" in the plan_material definition narrowly.
- I and L codes involve judgment about importance. In particular, several supplementary-table errors were coded minor because a correct copy exists elsewhere in the report, and coded substantive where no correct copy exists.
- The documents do not settle which prior (2302), weighting rule (4183) or interim boundary (0572) was actually applied. These rows are retained with the uncertainty stated.
