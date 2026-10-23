# v.2.4.1 reviewer runs (2026-10-13, 2025 addendum and 2019 revision 2026-10-14)

The eight completed workbooks in this folder were produced by Claude Opus 5.5 agent sessions (high reasoning effort), not by people. On 2026-10-13 eight sessions ran, one for each year and reviewer label. R_A and R_Bulun are the reviewer labels used in every file; each session worked alone, without subagents. No person reviewed any candidate. Agreement between R_A and R_Bulun is therefore agreement between two runs of the same model reading the same evidence, not inter-rater reliability. On 2026-10-14 two further Claude Opus 5.5 sessions (high reasoning effort), one per label, reviewed the 24 candidates of jama.2025.11178 and jama.2025.15185, whose reports were completed after the first round. Their rows were merged into the 2025 files, so the 2025 results come from two sessions per label. The reviewers did not modify the blank workbooks. The 2025 blanks were rebuilt on 2026-10-14 to add the two papers (`../2025/VALIDATION.md`). The 2019 blanks were rebuilt on 2026-10-14 without jama.2019.14231, an observational study that was removed from the cohort (see Setup). All eight blanks match `../<year>/output_hashes.json`.

## Layout

```
fill_review.py      judgments JSON -> copy of the blank workbook (rule checks; refuses overwrite or writing next to the blanks)
                    R_A uses the R_A blank; R_Bulun uses the R_B blank, with Setup!B2 and B4 set to R_Bulun
recalc_check.py     recalculates a completed workbook with the `formulas` interpreter; reports G and Checks
compare_roles.py    post hoc R_A vs R_Bulun agreement (descriptive), with paper-level bootstrap intervals
summarize_runs.py   counts per year and role; checks each workbook cell by cell against its judgments.json
ocr_page.py         renders PDF pages (annotations off) and OCRs them with RapidOCR on the GPU
<year>/<role>/judgments.json                                   every judgment with the evidence inspected and the rationale/recomputation
2025/<role>/judgments_11178_15185.json                          the 24 addendum judgments as delivered (merged unchanged into judgments.json)
<year>/<role>/human_adjudication_v_2_4_1_<year>_<role>_completed.xlsx
<year>/<role>/REVIEW_SUMMARY.md                                counts, departures from the AI cards, out-of-set observations, source issues, OCR use, limitations
<year>/compare_<year>.txt                                      compare_roles.py output, including every disagreement
```

Run the workbook scripts with `../../human_adjudication_v_2_3_1/2019/.venv/bin/python` (openpyxl 3.1.5, formulas 1.3.4). Run `ocr_page.py` with `~/venvs/stt/bin/python` (rapidocr-onnxruntime 1.4.4, onnxruntime-gpu 1.28.0, PyMuPDF 1.28.0). That venv's onnxruntime finds the CUDA 13 and cuDNN libraries bundled under `nvidia/` only after `onnxruntime.preload_dlls()`; the script does this and prints the provider in use.

## Setup

- **Sources.** Each reviewer read from a copy of the paper packages that holds only the original PDFs and image or xlsx supplements, `final_report_1_6_2.md`/`.html` and `QUALITY_CONTROL_SCOPE.md`. Pipeline `AGENTS.md` files, internal pipeline outputs and `Detailed_Errors_On_C1_C3_C5.docx` were not copied. This avoided the v.2.3.1 problem of package instructions loading when a PDF was opened.
- **Working folders.** Each reviewer had its own working folder from the start. Nothing was written to a shared location.
- **Procedure.** Reviewers followed `../REVIEWER_GUIDE_EN.md`, the Codebook and the two review decisions in `../README.md`. Disclosed plan–report changes are retained with "disclosed" in R, and L is optional. Reviewers judged from the PDFs before reading each card. Recomputations were done in R 4.5.2 or Python and are recorded in each rationale.
- **OCR.** Reviewers used RapidOCR on the RTX 5070 laptop GPU for pages with missing or garbled text layers, and rendered pages for visual checks. The pages are listed in each `REVIEW_SUMMARY.md`.
- **2025 addendum (2026-10-14).** The two addendum sessions used the same prompt as the 2025 sessions, with these changes:
  - they read a new source copy of the two papers in which the reader highlights on jama.2025.11178 supplement 4 p. 7 were deleted (page text unchanged);
  - they were also barred from this README and the `compare_<year>.txt` files, which list the first-round disagreements;
  - each could reread its own earlier 2025 `REVIEW_SUMMARY.md` and `judgments.json`, so that it applied the same rules within the year;
  - each wrote its 24 judgments to `judgments_11178_15185.json` and appended an addendum to its `REVIEW_SUMMARY.md`.

  The coordinator merged the rows unchanged into `judgments.json` and rebuilt the completed workbooks with `fill_review.py`. It also corrected one Files bullet in each addendum to record the merge.
- **Removal of jama.2019.14231 (2026-10-14).** The paper is an observational study, so it was moved out of the paper set and into `archived/`. Both 2019 reviews had covered it (8 candidates each). The coordinator then took the following steps:
  - it deleted those 16 judgments from the two `judgments.json` files and left the other 79 rows per role unchanged;
  - it refilled both completed workbooks from the rebuilt 79-candidate blanks with `fill_review.py`;
  - it reran `compare_roles.py 2019` and `summarize_runs.py`;
  - it revised the counts and removed the paper's entries in both 2019 `REVIEW_SUMMARY.md` files, each of which now opens with a dated coordinator note.

  None of the 46 R_A–R_Bulun disagreements involved the paper. The 87-candidate versions are in git history. The figures below exclude it.

## Results

All eight completed workbooks recalculate with every row and the Checks sheet at `PRIMARY READY` under the `formulas` interpreter. For every row, D, E, F, the active H–L codes and R in each workbook equal its `judgments.json` (`summarize_runs.py`). Desktop Excel was not used.

| Year | Role | Candidates | Retain | Exclude | Discuss | Substantive* | E changed |
|---|---|---:|---:|---:|---:|---:|---:|
| 2018 | R_A | 115 | 105 | 10 | 0 | 17 | 0 |
| 2018 | R_Bulun | 115 | 107 | 8 | 0 | 15 | 0 |
| 2019 | R_A | 79 | 76 | 3 | 0 | 10 | 1 |
| 2019 | R_Bulun | 79 | 76 | 3 | 0 | 6 | 1 |
| 2024 | R_A | 113 | 103 | 10 | 0 | 20 | 4 |
| 2024 | R_Bulun | 113 | 107 | 6 | 0 | 15 | 3 |
| 2025 | R_A | 133 | 124 | 9 | 0 | 18 | 3 |
| 2025 | R_Bulun | 133 | 123 | 10 | 0 | 14 | 1 |

\*Substantive means one of two cases among retained rows, as in v.2.3.1:
- a statistical result with H = confirmed_issue or probable_issue and I = substantive;
- a report-internal or plan-material inconsistency with K = substantive_inconsistency.

Protocol_report rows are reported separately, because L is optional and describes a difference rather than an error. Each reviewer retained 42–68 protocol_report rows per year, and L was blank for 0–4 of them. Among the 209 rows that both reviewers retained as protocol_report, L was identical for 180 (blank counted as a category). Both coded substantive_difference for 163 of the 209.

R_A vs R_Bulun agreement, from `compare_roles.py`. The outcome column uses that script's derived categories: excluded, unresolved, statistical substantive vs other, inconsistency substantive vs other, and protocol_report. Intervals are 95% percentile intervals from 2,000 bootstrap resamples of papers (seed 20261013), because candidates are clustered within papers.

| Year | D agreement (kappa, 95% interval) | E agreement (kappa, 95% interval) | Outcome agreement (kappa, 95% interval) |
|---|---|---|---|
| 2018 | 0.965 (0.76, 0.55 to 0.94) | 1.000 (1.00) | 0.930 (0.90, 0.86 to 0.95) |
| 2019 | 1.000 (1.00) | 1.000 (1.00) | 0.924 (0.87, 0.82 to 0.93) |
| 2024 | 0.965 (0.73, 0.38 to 0.90) | 0.973 (0.96, 0.91 to 1.00) | 0.841 (0.79, 0.71 to 0.87) |
| 2025 | 0.947 (0.60, 0.29 to 0.85) | 0.970 (0.95, 0.90 to 1.00) | 0.895 (0.84, 0.80 to 0.90) |

When agreement is perfect, the percentile bootstrap gives a degenerate interval, so none is shown. The kappa values for D rest on 3–10 exclusions per reviewer and year, which explains the wide intervals. As stated at the top, none of these figures estimates human inter-rater reliability. Both reviews come from the same model, so their errors are likely correlated.

### Where R_A and R_Bulun differ

46 of the 440 candidates differ in outcome or domain (listed in `<year>/compare_<year>.txt`).

- **Severity only (26).** Both reviewers retained the row in the same domain and agree that an issue exists, but grade it differently: substantive vs minor_presentation for I or K. R_A gave the more severe grade in 21 of the 26.
- **Disposition (15).** One reviewer retained and the other excluded. R_A excluded 10 of the 15. Six turn on which plan documents count, a scope rule each reviewer applied consistently but drew differently:
  - superseded or parent-trial plan material (2018 14282 C011; 2024 0572 C013, C019; 12829 C007);
  - in 2025, R_A excluded a plan–report difference when the report follows an amendment made before follow-up ended (4390 C006, C007); R_Bulun retained these as differences.
  - In the other 9, the reviewers differ on whether a stated method, display rounding or a definition accounts for the discrepancy: 2018 0948 C001, 14280 C010, 6496 C011; 2024 25786 C010; 2025 27643 C012, C014, 19563 C010, 20765 C011, 9663 C005.
- **Domain only (5).** In 2025, a number attributed to the wrong quantity or outcome was filed as statistical_results by R_A and as report_internal_inconsistency by R_Bulun: 27643 C008, 20765 C012, 24175 C013. In 2024, the two reviewers differ on 12829 C006 (statistical_results vs protocol_report) and 23898 C009 (plan_material vs protocol_report).

No candidate had both reviewers retain it with one finding an issue and the other finding none (`not_issue` or `non_inconsistency`).

For the 24 addendum candidates (jama.2025.11178 and jama.2025.15185), D and E agreed on all 24 and the derived outcome on 22. The two outcome differences are 11178 C008 and C009, severity only: R_A coded the NNT intervals that appear to have lost a minus sign as substantive, while R_Bulun coded them as minor_presentation. Both reviewers excluded 11178 C004 because the NNTs follow round-up. Below the outcome level, H differs for 11178 C011 (probable vs confirmed) and 15185 C006 (probable_issue vs indeterminate). L differs for 11178 C001 and C007, where each reviewer coded one of the two as indeterminate.

## Limitations and independence record

- **No `discuss`.** As in v.2.3.1, no reviewer used `discuss` for any of the 880 role-candidate judgments, although each prompt asked reviewers to use it when the documents could not settle a candidate. Treat this as possible overconfidence. Several rationales state uncertainty that a human reviewer might have routed to `discuss`. Examples are model-based estimates that could not be reproduced and plan documents that were cited but not supplied.
- **Annotated source PDFs.** Several supplied PDFs carry earlier reader annotations: highlights and comments with author `AltanGadasTbl`, some marking suspected errors.

  | Paper | File | Annotated pages |
  |---|---|---|
  | jama.2024.2302 | main article | pp. 1, 3, 4 |
  | jama.2024.4183 | main article | pp. 5, 6 |
  | jama.2024.4183 | supplement 2 | pp. 10, 11, 18, 35 |
  | jama.2025.4390 | main article | pp. 6, 8, 9 |
  | jama.2025.4390 | supplement 3 | pp. 22, 29, 32, 37, 39; includes comments |
  | jama.2025.7710 | main article | pp. 1, 4, 5 |
  | jama.2025.11178 | supplement 4 | p. 7 |

  Two other files carry annotations by other authors that look like document-processing artifacts: jama.2024.27643 supplement 1 and jama.2025.7710 supplement 1. PyMuPDF draws annotations when it renders a page. 2025 R_A found the annotations partway through its review, and from then on renders were made with annotations off. Exposure, from the tool calls of each review:

  | Reviewer | Exposure |
  |---|---|
  | 2025 R_A | Saw highlights on 4390 supplement 3 pp. 37 and 39, and read the comment text through an annotation listing. It discloses this for 4390 C001, C011 and C012. R_A and R_Bulun agree on all three. |
  | 2024 R_Bulun | Viewed a render of 4183 main p. 6, which highlights two numbers, for 4183 C001. Neither reviewer's rationale for any 4183 candidate cites those numbers, and the two agree on C001. |
  | 2024 R_A | None |
  | 2025 R_Bulun | None; it read the annotated pages only through the text layer, which does not carry annotations |
  | 2018 and 2019 reviewers | None; no annotated files in those years |
  | 2025 addendum R_A and R_Bulun | None; the highlights on 11178 supplement 4 p. 7 were deleted from their source copy, and both report seeing no annotations |

  The same annotated files are in the paper packages that workflow 1.6.2 read. Their modification dates (2026-08-10 and 2026-08-14) are earlier than the 1.6.2 reports (2026-10-11), and the 4390 run records "existing source annotations" in its `review_1_6_2/limitations.md`. Whether the annotations helped the pipeline find any candidate has not been checked. Unannotated originals should replace these files before human review or any rerun.
- **Independence audit.** The coordinator scanned every tool call of the ten sessions (82 and 90 calls for the two addendum sessions). None opened the other role's folder, another year's folder, another reviewer's working folder, v.2.3.1 (other than its Python interpreter), `human_adjudication/previous/`, `meta_report/`, the paper packages or any `.ai_paper_validation/` folder. None ran git history commands or used subagents. The addendum sessions also did not open this README or any `compare_<year>.txt`. The prompts named the other role and the excluded locations, so each reviewer knew a second review existed.
- **Edits after writing.** Two `REVIEW_SUMMARY.md` files changed on disk after their reviewer wrote them, with no tool call from any session:
  - 2018 R_Bulun: "R 4.x" became "R";
  - 2025 R_Bulun: one character in one line changed.

  Neither change affects a judgment. For the two addendum summaries, every line on disk matches a write by its own session, except the Files bullet the coordinator corrected (see Setup).
- **Shared model.** Both labels are the same model with the same instructions and documents. Agreement is expected to be higher than between two human reviewers, and shared blind spots would not show up as disagreement.
- **Missing plan documents.** Several plan documents are cited but not supplied:
  - the 17075 published SAP;
  - the 14901 SAP;
  - the 27643 master SAP v2.0;
  - the 4390 final published protocol.

  The 4183 protocol supplied is dated 23 August 2023, after the trial ended in 2019. Protocol_report judgments for these papers rest on the plan documents as supplied.
- **Text layers.** Text layers are scanned or unusable in many plan documents, especially in 2025. OCR can drop light or watermarked lines, and reviewers rendered pages where wording was decisive. In 2018, R_A OCR'd only the scanned plan pages relevant to each candidate, so plan content on other scanned pages could have been missed.
- **Completion flags.** `fill_review.py` sets F = `primary_done` for every judged row. The desktop Excel smoke test in each year's VALIDATION.md is still pending.

## Source and template issues found by the reviewers

- **jama.2018.18020 C022:** column C has no file or page; this was already known.
- **jama.2018.9128 supplement 1:** the text layer silently drops numerals on some pages (e.g., pp. 36, 40) and p. 67 uses a shifted font.
- **jama.2018.14282 supplement 1:** pp. 70–81, listed as the final protocol, are the consent forms.
- **jama.2018.6496:** protocol p. 21 leaves the interim sample size blank, while supplement 2 quotes "500".
- **jama.2019.12618 supplement 2:** 20 pages have no text layer, including cited pp. 15, 80, 81 and 136.
- **jama.2019.7505 C012:** the location cites a derived image that is not in the package. The protocol p. 32 text layer reads "≤ 8" as "< 8".
- **jama.2024.0572 supplement 3:** the trial SAP is a 40-page scan; its watermark makes OCR drop lines.
- **jama.2024.6063:** the "SAP" is a one-page excerpt of protocol version 2. C008 and C012 share one table row.
- **jama.2025.20765 supplement 1:** the pages of protocol v4.0 carry "V6.0" running headers.
- **jama.2024.27643:** column C locations begin with a generic phrase instead of a role per page.
- **jama.2025.11178:** the protocol (supplement 1) and SAP (supplement 2) text layers are font-encoded garbage; both reviewers read them by OCR and checked against renders. Table 2 is printed rotated. C018 gives its locations as a table, which the 2025 build now parses (`../2025/VALIDATION.md`).
- **jama.2025.15185:** the SAP (supplement 2) has no text layer, and the protocol (supplement 1) and analysis code (supplement 5) layers are unusable. Supplement 1 holds two protocol versions (v1.1, pp. 1–46; v1.4, pp. 47–94) without a divider.
- **Reviewer guide paths:** the guide places the final reports under `.ai_paper_validation/`; in the reviewers' source copies they sat at the paper-folder root.
- **Cards:** they link to `review_1_6_2/` verification files that are outside the reviewer materials. No reviewer needed them.

No reviewer found a mismatch between workbook keys or titles and the cards, or a cited page that did not exist.

Each reviewer also recorded possible errors outside the candidate set, observed while checking candidates and not searched for systematically. These are listed in each `REVIEW_SUMMARY.md` and were not adjudicated. Several were found independently by both reviewers of a year, for example:
- 2018: 21906 text vs Table 2 β-blocker values;
- 2024: 0572 infarct-growth IQR (125 vs 135 mL);
- 2025: 24764 LOS ratio P = .21 against a CI that implies about .39;
- 2025 addendum: 11178 painTRAINER enhancement after about 140 enrollees (SAP) vs 454 (supplement 4 and eTable 8), and 1713 women in the xlsx vs 1712 in Table 1; 15185 PROMIS-10 means 28 in the text vs 29.87 and 30.04 in eTable 4, eTable 6 overall n 145 vs 146, and the eFigure 7 color legend vs its subgroup definition.
