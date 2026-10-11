# v.2.3.1 primary review, 2025, role R_A (AI-simulated)

Reviewer ID: `AI-sim-ClaudeOpus5.5-2025-R_A`. This is an AI-simulated reviewer (a Claude Opus 5.5 agent), not a human adjudicator.
Scope: 15 papers and 131 candidates. Every candidate was checked against the source PDFs and supplements. The AI rationale was not taken on trust.

Files
- `judgments.json`: one row per candidate (D, E, H-L, R note, evidence pages, rationale).
- `human_adjudication_v_2_3_1_2025_R_A_completed.xlsx`: built with `fill_review.py` from the release template, which was not modified.

## Counts

| | n |
|---|---|
| D = retain | 106 |
| D = exclude | 25 |
| D = discuss | 0 |
| E = statistical_results | 50 (45 retain, 5 exclude) |
| E = report_internal_inconsistency | 43 (35 retain, 8 exclude) |
| E = plan_material | 23 (17 retain, 6 exclude) |
| E = protocol_report | 15 (9 retain, 6 exclude) |
| E changed from the AI suggestion | 0 |

Outcome codes (retained rows only):
- **H (45 statistical_results rows):** confirmed_issue 42, probable_issue 3.
- **I:** substantive 29, minor_presentation 16. By H x I: confirmed/substantive 28, confirmed/minor 14, probable/substantive 1, probable/minor 2.
- **J (optional):** direct 29, unlikely 14, possible 2.
- **K (52 report_internal_inconsistency or plan_material rows):** substantive_inconsistency 9, minor_presentation 43.
- **L (9 protocol_report rows, optional):** substantive_difference 6, minor_presentation 2, version_timing 1.

Of the 29 substantive statistical_results rows, 26 come from one paper (jama.2025.11178, C008-C033). That paper's Table 3 SMD 95% CIs are systematically corrupted: intervals exclude their own point estimates or have reversed endpoints, and they conflict with the adjusted mean differences they are said to be derived from.

Disposition by paper (retain/exclude):
- 24764: 4/4
- 27643: 7/1
- 11178: 37/0
- 15185: 11/1
- 15440: 1/1
- 16450: 3/7
- 19563: 6/1
- 19843: 0/1
- 20765: 11/2
- 24175: 10/4
- 4390: 3/0
- 7583: 2/1
- 7710: 4/0
- 9110: 4/2
- 9663: 3/0

Conventions applied:
- **exclude:** used when the apparent discrepancy has a satisfactory explanation (a different valid test or definition, rounding, a multiple-response item, a different time window) or rests on a misreading of the source. This follows the Codebook ("for example because the apparent mismatch has a satisfactory explanation"). retain + not_issue/non_inconsistency was not used.
- **retain:** used for any real discrepancy, however small. Importance was then graded in I/K/L.
- **E:** the AI-suggested domain was kept unless clearly the wrong branch. None needed changing. Several numeric cross-location conflicts sit in report_internal_inconsistency under the AI's choice and could equally be coded statistical_results.

## Discuss list

None. No candidate remained undecidable after checking the sources.

## Disagreements with the AI

**Disposition: AI retain, R_A exclude (17)**
- **24764 C002-C004:** surgeon-grade rows are multiple-response (more than one grade can operate or close). Every percentage reproduces from the arm n.
- **24764 C005:** Figure 1 counts all 25 deaths during follow-up. Text and Table 3 report 30-day mortality (24). The day-30 window ran to day 44, so the counts measure different windows.
- **27643 C006:** the plasma NfL CI differences come from rounding; eTable 3B rounds to integers.
- **15185 C010:** FMA and FMMA are the same instrument (defined in the SAP).
- **15440 C002:** Figure 4B rows are separate time-to-first-event analyses. Participants with both stroke types appear in both subtype rows but once in "any stroke" (69 participants), so 60 + 12 = 72 vs 69 is expected.
- **16450 C007:** the final alpha of .049 vs the planned .0440 follows from the SAP's provision to recover alpha from interim looks that were not performed. Simulated overall alpha is about 0.049.
- **16450 C009, C010:** the RR approximated by the OR is disclosed in footnotes and the Methods. Recomputed ORs match.
- **19563 C005:** "(p<0.05)" states the significance criterion, not a reported P value.
- **19843 C001:** P = .78 reproduces a continuity-corrected chi-square test of 28/101 vs 26/104 (p = 0.7765), the stated method for categorical outcomes. The eFigure's p = 0.56 is the log-rank test.
- **20765 C008, C010:** the design-effect totals follow from rounding cluster size up to whole participants per site: 1616.2/36 gives 45 per site and 1620 in total; 1056/27 gives 40 per site and 1080.
- **7583 C002:** 142 x 1.2 = 170.4, rounded to 171 per group (342 in total). This is a common attrition-inflation convention, used consistently in the protocol, SAP and article.
- **9110 C005, C006:** inconsistent percent-sign notation under an "[n (%)]" header is equivalent notation. All percentages reproduce.

**Grading or substance differences (retained rows)**
- **4390 C001 (broader than flagged):** the entire Figure 3 "Rate per 100 patient-years" column is person-time in hundreds of patient-years, not rates. Every subgroup pair sums to 71.0, and 163/7100 x 100 = 2.30 matches Table 2. Graded substantive_inconsistency.
- **11178 C005:** raised to substantive. 711/1566 = 45.4%, not the printed 73.2%, and the error reverses an apparent gradient.
- **24175 C005:** retained for a different reason than the AI gave. The dropout step is fine, but 117 per arm does not follow from the stated inputs (about 110-111).
- **24175 C009:** also noted that the article's own eTable 1 lists 29 sites, not the 33 stated in the article.
- **24175 C011:** substantive. The misprinted OR 1.194 (true value 1.94) lies inside its own CI and would be extracted unnoticed.
- **20765 C001 and 24175 C013 (dropped-digit errors: CI 1.9-42, OR 0.11):** graded confirmed/minor_presentation with J = direct. The intended values (4.2, 1.11) are evident from context, but the printed value is what an extractor would copy.
- **19563 C007:** probable rather than confirmed, because an unstated adjusted estimand cannot be excluded.
- **27643 C008:** probable/minor. The 13 vs 14 event counts are explained by one event after week 24, but one "to week 24" label is still wrong.
- **7583 C003:** probable/minor. 146 + 18 = 164 > 163. A bilateral patient treated with both techniques could explain it, but nothing in the paper says so.

Agreed with the AI's own exclude for all 8 candidates it marked exclude (16450 C002, C003, C005, C006; 24175 C002, C003, C004, C014).

## Sources and reading method

- **Unreadable sources:** none.
- **Read tool:** `pages` rendering failed because pdftoppm is not installed. Only the 9-page main article for 15440 was read directly with the Read tool.
- **Other PDFs:** text was extracted page by page with PyMuPDF (`fitz`), which is available only in the system `python3` user site-packages, not the 2019 venv. Wherever layout mattered, pages were rendered to PNG and read visually, including every table or figure cited for a numeric judgment.
- **Arithmetic:** done in the 2019 venv (scipy for test statistics); shown in each rationale.
- **No usable text layer (read from rendered images):**
  - 15185 SAP (joi250066supp2) and 19843 SAP (joi250087supp2): scanned.
  - 9663 SAP p. 118: garbled font encoding.
  - 16450 protocol/SAP, 19563 protocol supplement, 20765 Supplement 1 and 24175 Supplement 1: partly or fully garbled font encoding.
- **Parallel work:** the review was split by paper across forked instances of the same agent, using shared written conventions, and merged here. Disposition and grading conventions were checked for consistency at merge. No R_B material, pipeline outputs (`.ai_paper_validation/`, `workflow_*`, `meta_report/`) or earlier adjudication versions were read.

## recalc_check output

```
G: {'PRIMARY READY': 131}
Checks 2 Reviewer role -> R_A
Checks 3 Candidates -> 131
Checks 4 Primary ready rows -> 131
Checks 5 Unfinished rows -> 0.0
Checks 6 Discuss / unresolved rows -> 0
Checks 7 Workflow status -> PRIMARY READY
Checks 10 Ready discuss rows -> 0
```
`fill_review.py --check`: keys = 131, judged = 131, missing = 0, 0 errors.

## Notes on the workbook, scripts and package

- **Scripts:** both ran without errors. `fill_review.py` sets F = primary_done for every judged row; that is intended here, but it means the "manual review complete" flag is set by script. Desktop Excel smoke testing of the completed file has not been done (only the `formulas` recalculation).
- **AGENTS.md:** each paper folder contains a pipeline `AGENTS.md`. Opening a PDF in the 15440 folder caused that file to be injected into this agent's context automatically. It was ignored, but it is a potential independence leak for AI-simulated reviewers.
- **Lock file:** `2025/jama.2025.11178/` contains a pre-existing Office lock file (`~$joi250046supp5...xlsx`). It was not touched.
- **Links:** some Candidates/Links rows carry `evidencePaths` links into `.ai_paper_validation/`. They were not followed.
- **Possible issues outside any candidate (not judged):**
  - 15185 main Table 2: the n = 126/129 column headers appear to be serious adverse event counts.
  - 20765 eTable 4: percentage slips.
  - 24175 protocol PROVIDE Table 2: percentage errors.
  - 11178 Table 3: further implausible SMD intervals not flagged as candidates.
