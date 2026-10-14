# v.2.4.1 independent primary review, 2024 cohort: reviewer R_Bulun

Reviewer R_Bulun; 10 papers, 113 candidates. Independence: I worked only from the read-only source mirror (original PDFs, `final_report_1_6_2.md/.html`, `QUALITY_CONTROL_SCOPE.md`) and the blank R_B workbook. I did not open or list the R_A folder or any other year or role folder under `reviewer_runs/`, anything under `human_adjudication_v_2_3_1/` or `human_adjudication/previous/`, `meta_report/`, the repository paper packages or any `.ai_paper_validation/` folder, or `2024/jama.2024.2302/Detailed_Errors_On_C1_C3_C5.docx`, and I did not consult git history. For each candidate I formed a judgment from the PDFs first and read the AI's card afterwards.

## Files

- `human_adjudication_v_2_4_1_2024_R_Bulun_completed.xlsx`: completed workbook built from the R_B blank (Setup B4 = R_Bulun). All 113 rows are `PRIMARY READY`; Checks reports workflow status `PRIMARY READY`, 0 unfinished rows and 0 discuss rows.
- `judgments.json`: per-candidate D, E and H–L codes, the column R note, the evidence inspected (files, pages, whether rendered or OCR'd) and the full rationale, including recomputations.
- `REVIEW_SUMMARY.md`: this file.

## Counts

Dispositions: 107 retain, 6 exclude, 0 discuss.

| Review domain (final E) | Retain | Exclude | Discuss | Total | AI suggestion |
|---|---:|---:|---:|---:|---:|
| statistical_results | 45 | 4 | 0 | 49 | 51 |
| report_internal_inconsistency | 5 | 0 | 0 | 5 | 2 |
| plan_material | 13 | 2 | 0 | 15 | 15 |
| protocol_report | 44 | 0 | 0 | 44 | 45 |
| Total | 107 | 6 | 0 | 113 | 113 |

E changed from the AI suggestion (3):

- `2024::jama.2024.0572::C008`, statistical_results to report_internal_inconsistency: the conflict is which core-volume definition (CTP/MRI vs composite) conditions the eFigure 18/19 surfaces, a labeling question rather than a numerical error.
- `2024::jama.2024.11057::C003`, protocol_report to report_internal_inconsistency: the main article's 6-week prequit messaging period conflicts with the results supplement's 1 week; the protocol only corroborates the supplement, and an intervention description is not a statistical design element.
- `2024::jama.2024.25786::C010`, statistical_results to report_internal_inconsistency: "ICU admission" labels two different populations (direct ICU destination for the subgroup; any ICU admission for the exploratory outcome); the counts themselves are coherent.

Exclusions (6):

- `2024::jama.2024.0572::C005`: CIs with an upper limit printed as 1.00 accompany significance statements; unrounded limits below 1.000 are compatible with them, and no conflicting P value is printed.
- `2024::jama.2024.0572::C011`: inconsistency in historical SELECT cohort results quoted in the protocol background, not a design element; the 1.00 lower limits are also compatible with rounding.
- `2024::jama.2024.0572::C012`: "significantly increased" applied to P = .072 in the same background paragraph; wording about prior-study results, not a design element.
- `2024::jama.2024.19585::C001`: the ED absolute difference (credible interval) and the rate ratio come from different, disclosed models (footnote b); no contradiction.
- `2024::jama.2024.19585::C006`: sadness OR 0.51 (0.26–0.99), P = .05; the CI implies P ≈ .048, which rounds to .05 and is below .05.
- `2024::jama.2024.25786::C008`: an SSI odds ratio and risk difference from different models disagree at the null boundary, and the report makes no significance claim after FDR control. I record separately that the RD method is undescribed (see "Possible errors outside the candidate set").

## Outcome codes (retained rows)

statistical_results (45 retained):

- H: confirmed_issue 43; probable_issue 2 (`0318::C010`, `4183::C002`); not_issue 0; indeterminate 0.
- I: substantive 11; minor_presentation 33; indeterminate 1 (`4183::C002`).
- J: direct 7; possible 12; unlikely 26; unknown 0; none left blank.

Confirmed or probable issues rated substantive (11, all confirmed): `0572::C001` (follow-up MRI population 8 vs 204), `0572::C004` (finite RR for an all-zero subgroup), `0572::C006` (Figure 2B mRS categories shifted by 1), `0572::C007` (narrative direction contradicts eFigure 17), `0572::C018` (discordant-profile counts swapped between arms; disjoint counts exceed totals), `12829::C004` (risk-difference CI −2.4 to −1.7 for a point of −0.4; the upper limit should be +1.7), `2302::C001` (abstract says 320 had operative repair; 281 did), `25786::C011` (liberal AIS <3 denominator 473 vs implied 522), `4183::C005` (direction of the varenicline switch contrast reversed), `6063::C009` (adverse-event rows attributed to the wrong arm in Table 3), `6063::C010` (SAE relatedness "none related" vs possible or probable in eTable 8).

K (18 retained plan_material or report_internal_inconsistency rows): substantive_inconsistency 4 (`0572::C010`, `0572::C014`, `0572::C019`, `11057::C003`); minor_presentation 11; indeterminate 3 (`12829::C007`, `4183::C010`, `6063::C011`); non_inconsistency 0.

L (44 retained protocol_report rows; optional): substantive_difference 37; minor_presentation 2 (`0318::C005`, `12829::C006`); indeterminate 3 (`0318::C006`, `23898::C009`, `25786::C002`); version_timing 0; non_inconsistency 0; left blank 2 (`23898::C007`, `23898::C010`, both planned outputs of low importance that I chose not to characterize). Disclosed changes are retained as differences and marked "disclosed" in column R (for example, `2302::C002` GEE after nonconvergence, `4183::C001` assignment of nonattenders to continuation).

## Discuss list

None. Candidates I considered for discuss and settled:

- `0572::C014` (efficacy stop at an unscheduled 300-patient look while the SAP says no additional interim analysis was incorporated): retained as substantive_inconsistency because the contradiction is explicit in the SAP text; which boundary was applied would need the DSMB report.
- `4183::C002` (IPW weight for 75 nonattenders): retained as probable_issue with I indeterminate; analysis code would resolve it.
- `25786::C002` (1600 maximum vs 1979 randomized): retained with L indeterminate because the plan does not define the population for the cap.
- `25786::C008` (SSI OR vs RD): excluded, because the claim concerns two different estimators; a description of the RD method would clarify the broader RD concern noted below.

## Where I disagreed with or went beyond the AI card

- Exclusions: all six excluded candidates carry a "CONFIRMED" inclusion audit on their cards. I excluded three because rounding or disclosed differences between models explain them (`0572::C005`, `19585::C001`, `19585::C006`) and two because protocol background on prior studies is not a design element (`0572::C011`, `0572::C012`). I excluded `25786::C008` because the OR and RD are different estimators and no claim is made.
- E changes: 3, listed above.
- `19585::C007` and `C005`: I showed that the sparse-cell ORs and CIs in eTable 10 are Haldane–Anscombe (0.5-corrected) Wald values and the P values are Fisher exact tests (6/57 vs 0/70: OR 17.80 [0.98–323.06], Fisher P = .0070; 6/111 vs 0/130: Fisher P = .0089). This explains the CI–P conflict as an undisclosed mixture of methods. The card left the method unidentified.
- `25786::C011`: the liberal AIS subgroups sum to 675, not 724; 48/522 = 9.2% and 522 + 202 = 724, so the denominator 473 is probably wrong in both displays. The card raised 522 only as a possibility.
- `25786::C015`: the gap between N = 130 and 55 + 67 = 122 equals the 4 + 4 participants "omitted according to Swiss law" in Figure 1.
- `0572::C006`: I checked segment colors against the legend at 300 dpi and showed that both bars of Figure 2B fit the supplementary counts if each segment is shifted one mRS category.
- `6063::C008`: I identified the sources of the copied values (weight-bearing week 4 duplicates the function row; hsCRP week 12 shows the glucose contrast). For `6063::C012` I accepted only the glucose week-12 interval (identical to hsCRP's) and rejected the root-sum-of-squares width rule for WOMAC week 24, because arm changes from a treatment × month mixed model share coefficients and need not be independent.
- `12829::C006`: the printed P values reproduce Fisher's exact test, the planned test, so I described the difference as labeling-level (L minor_presentation). The card reports the same reproduction.
- `12829::C007`: Schoenfeld calculations give 56 (80% power) or 75 (90% power) required events and about 65 expected events, compared with the 91 stated.
- `6063::C011`: I also found that the primary power statement does not reproduce (SD 25.5 requires 276 participants for 90% power, not 234).
- `23898::C002`: the Figure 1 placebo safety box sums to 278 (256 + 22; 246 + 32), not the 279 printed.
- `0318::C014`: White race is 177 in Table 1 arm counts but 176 in eTable 1 and the abstract.

## Possible errors outside the candidate set (observed, not adjudicated)

- jama.2024.0318: Figure 1 arm boxes 122 + 193 = 315, but 316 were eligible. Table 1 White count 59 + 118 = 177 (67.6%) vs abstract and eTable 1 176 (67.2%).
- jama.2024.0572: main p9 MM infarct growth IQR 56–125 mL vs eTable 11 56–135 mL; Table 2 abbreviations define aRR as "absolute risk reduction" for quantities that are adjusted risk ratios; "two-thirds" (p11) vs 204/336 = 61%.
- jama.2024.12829: "343 (69.1%) were male" (343/501 = 68.5%; 69.1% is the balloon-arm figure); lead-center enrollment 258 (main p4) vs 256 (Table S7).
- jama.2024.23898: PONV day 2 (5/223 vs 19/226) is not tested; a crude Fisher test gives P = .005, against the abstract's "no significant difference in any secondary end point".
- jama.2024.25786: the RD estimation method in Figure 2 is undescribed, and printed RDs depart from crude differences more than the ORs do (major respiratory complications: crude −1.91 vs printed −0.61; SSI: crude −1.29 vs printed −3.04). eTable 2 firearm row denominator 724 vs 742 in the other rows.
- jama.2024.4183: Table sex row "Male 145 (57.1)" in both arms (105 + 145 = 250 ≠ 245; 57.1% = 140/245); Figure 2 CNRT box "245 randomized; 245 received; 1 did not receive" (implies 246); main p4 "who did attend rerandomization" should read "did not"; eTable 4 phase-1 abstainer contrast −4% to 16% vs main text −5% to 16%; supplement p11 cites "E-Table 7" for a contrast in eTable 9.
- jama.2024.6063: Table 3 placebo "pain in extremity" 6 vs eTable 7 and the abstract 5; the direction of the between-group contrast (placebo minus krill) is never defined.
- jama.2024.19585: Table 3 model-based absolute differences do not track crude rates (unplanned clinic visits: 5.1 vs 3.0 per 100 patient-weeks, model difference −0.01); this may be legitimate marginalization but could not be checked.

## Template or source issues

- jama.2024.0572 Supplement 3 (trial SAP v1.0.0, 40 pages) is a scan with no text layer. A "Confidential" watermark caused OCR to drop lines, including the key sentence for C014.
- Protocol PDFs for jama.2024.0318 (model equations) and jama.2024.4183 (Greek symbols in the decision threshold, contrast formulas) have garbled text layers; content was legible enough to judge, and the 0.90 threshold in 4183 is unambiguous.
- No mismatches between workbook keys or titles and the cards were found. Column C locations matched the cited pages in every case I checked. Several column C cells are very long (for example, 0572 C016, 23898 C007), as documented in the README.

## OCR and rendering use

- OCR (RapidOCR, 250 dpi): jama.2024.0572 Supplement 3 pages 2, 9–14, 17, 18, 31, 39, 40 (scanned SAP). Pages 9 and 12 were also rendered at 140 dpi and read directly, because OCR omitted lines under the watermark.
- Rendered and viewed (110–300 dpi) where layout or values mattered: 0318 main p6 and supp 2 pp14–16; 0572 main pp7, 10 (Figure 2 crop at 300 dpi), supp 5 pp13–15, 19, 23–25; 11057 supp 2 p14; 12829 main pp5, 7, 8 and supp 1 pp13, 19–21, 23–24; 19585 main p9 and supp 2 pp13–15, 17; 23898 main pp3, 6–8 and supp 3 p2; 25786 main p8 and supp 2 pp9–10, 14–15, 18, 20–21, 24; 4183 main pp6–7 and supp 2 pp15–16; 6063 main pp6, 8 and supp 3 pp2, 5–6, 8, 10–11, 14. Everything else was read from the PyMuPDF text layer.

## Limitations

- The review was carried out by one reviewer. Severity codes (I, K, L) involve judgment, particularly where I separated substantive from minor presentation issues and where L is optional.
- Several determinations rely on the reviewer's own recomputation under stated conventions (Wald and log-Wald intervals, Fisher and chi-square tests, Schoenfeld event counts, two-sample t power, beta quantiles). These are approximations to the authors' unreported methods; R code is summarized in each rationale.
- Model-based estimates (GEE, mixed models, IPW, Bayesian posteriors) could not be reproduced without participant-level data. Where a discrepancy might be explained by the model, I used probable_issue or indeterminate, or excluded the candidate.
- I did not view every page of every supplement. For absence checks I searched the full text layers of all report documents. eFigure 20 of 0572 (relevant to C018) was not inspected; the eTable arithmetic was sufficient.
- Plan documents outside the package (registry entries, separately published protocols) were not consulted. Where a version sequence was documented in the supplied plans, I did not use version_timing.
