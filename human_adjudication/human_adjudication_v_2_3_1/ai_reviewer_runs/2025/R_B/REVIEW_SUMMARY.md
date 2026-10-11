# v.2.3.1 primary review, 2025, role R_B: summary

Reviewer ID: `AI-sim-ClaudeOpus5.5-2025-R_B` (AI-simulated reviewer, Claude Opus 5.5 agent; not a human adjudicator).

Files in this folder:

- `judgments.json`: 131 judgments, each with a workbook note (R), the evidence inspected, and the rationale with recomputations.
- `human_adjudication_v_2_3_1_2025_R_B_completed.xlsx`: built with `fill_review.py` from the release template, which was not modified.

## Method

- I read the Start, Setup, Codebook and Rule_defaults sheets. I then read the Candidates, Evidence, Links and Relations sheets for each paper.
- For every candidate I checked the cited pages in the original PDFs. Main-article tables and figures, and all supplements with custom-encoded text layers, were rendered to images and read. Where the text layer was clean, I searched it as well.
- Numerical claims were recomputed in Python (scipy/numpy): percentages, sums, CI log-midpoints, crude OR/RR with Woolf CIs, chi-square, Fisher and Wilcoxon P values, t tests, exponential event-rate checks, sample-size and design-effect arithmetic, and Lan-DeMets boundaries.
- I used exclude when the apparent discrepancy had a satisfactory explanation, and retain otherwise. I never used retain + not_issue or non_inconsistency.

## Counts

| | n |
|---|---|
| D = retain | 112 |
| D = exclude | 19 |
| D = discuss | 0 |
| E = statistical_results | 50 |
| E = report_internal_inconsistency | 43 |
| E = plan_material | 23 |
| E = protocol_report | 15 |
| E changed from AI suggestion | 0 |

Disposition compared with the AI suggestion:

- AI retain, I retained: 112.
- AI retain, I excluded: 11.
- AI exclude, I excluded: 8.
- AI exclude, I retained: 0.

Outcome codes (retained rows only):

- H (statistical issue): confirmed_issue 44, probable_issue 4.
- I (substantiveness): substantive 27, minor_presentation 21.
- J (downstream impact): direct 26, possible 4, unlikely 18.
- K (internal/plan inconsistency): minor_presentation 47, substantive_inconsistency 8, indeterminate 1.
- L (protocol interpretation): substantive_difference 5, version_timing 2, minor_presentation 1.

Of the 27 substantive statistical rows, 26 are the corrupted SMD confidence-interval column in jama.2025.11178 Table 3 (C008-C033). The 27th is the jama.2025.19563 multiple-imputation risk difference whose sign conflicts with its pooled percentages (C007).

## Discuss list

None. I found no candidate where the evidence was unreadable or where the judgment depended on information missing from the package in a way that left the disposition open.

The one residual uncertainty, jama.2025.24175 C006, was recorded as retain with K = indeterminate rather than discuss. That candidate concerns the historical PROVIDE death count (14 vs 11), and the figure does not state its time window.

## Disagreements with the AI

### Disposition: AI retain, I excluded (11)

- **jama.2025.15185 C010.** FMA and FMMA are synonymous abbreviations; the SAP defines FMMA for the same instrument.
- **jama.2025.15440 C002.** Stroke subtype rows are participant-level time-to-first-event outcomes, so they need not sum to "any stroke".
- **jama.2025.19843 C001.** P = .78 is a fixed-time 2x2 test: the Yates chi-square reproduces 0.776. The figure's .56 is explicitly a log-rank test.
- **jama.2025.16450 C004.** The 2020 manual gave GMFCS 3-5 explicitly as a provisional example. The SAP fixes 4-5.
- **jama.2025.16450 C007.** The SAP states that the final alpha depends on which looks occurred and that unspent alpha may be recovered. After the futility stop, a final alpha of .049 is plausible: a Lan-DeMets O'Brien-Fleming check gives about 0.048-0.050. The primary RR was 1.00.
- **jama.2025.16450 C008.** "15 centers in the NRN" describes the network's size, not a planned site count.
- **jama.2025.16450 C009 and C010.** Footnotes disclose that OR approximations were used for sparse rows. The printed values reproduce the crude ORs, and OR is close to RR at these risks.
- **jama.2025.19563 C005.** "(p<0.05)" states the significance threshold. The confusing copied footnote is retained separately as C004.
- **jama.2025.9110 C005 and C006.** The % sign is used inconsistently, but the [n (%)] header defines the unit and every value is correct.

### Rationale or severity: same disposition as the AI, different assessment

- **jama.2024.24764 C008.** The abstract reports only the nonprespecified UK+Australia length-of-stay result. The AI note said "not proven substitution".
- **jama.2024.27643 C005.** Exponential checks against the observed deaths show the eTable rates (0.010 and 0.009) are the coherent ones. The article's 0.007 and 0.006 appear wrong.
- **jama.2025.11178 C034.** The workbook's own note gives the same sex definition as Table 1, so the AI's EHR-only alternative does not apply.
- **jama.2025.15185 C002 and C003.** The eTable "time from onset" row actually contains the NIHSS medians. A median of 8 days would conflict with the 7-day eligibility window.
- **jama.2025.20765 C010.** Beyond the 1056 vs 1080 rounding, the design effect uses the pre-inflation cluster size of 26. At the planned 40 per site the design effect would be 1.78, so the phase 3 sample size is internally inconsistent. I rated this substantive.
- **jama.2025.4390 C001.** The Figure 3 "rate" column is follow-up time in hundreds of patient-years throughout the figure, not only in the all-patient row. For example, 163/71.0 = 2.30.
- **jama.2025.24175 C005.** 280 is consistent with roughly 15% dropout. However, 117 per arm does not reproduce from the stated inputs (d = 1.4, SD = 3.2), which give 111 per arm.
- **jama.2025.9663 C003.** Aside, outside the candidate: the same SAP footnote defines adherence as the percentage of patients with a protocol deviation, which reads as inverted.

## Sources not fully read

No source was unreadable. Text layers in several supplements were custom-encoded, so I rendered those pages: 16450 supp1-3, 19563 supp1, 20765 supp1, 24175 supp1, 9663 supp1 and 11178 supp1-2.

A few cited comparator pages were not inspected. Each instance is stated in the relevant rationale:

- jama.2025.4390 eTable 3 (p.29).
- jama.2025.9663 eTable 5.
- jama.2025.20765 protocol pp.51-52 diagram and the pp.101-109 message log.
- jama.2025.16450 supp4 p.7 table header.

No AI pipeline outputs (`.ai_paper_validation/`, `workflow_*`, `meta_report/`, `archived/`), earlier adjudication versions or git history were opened.

## Independence note (scratchpad)

Before the coordinator's instruction arrived, I wrote working files at the top level of the shared session scratchpad:

- `j1.json` through `j12.json` (my per-paper judgment drafts);
- `add.py` and `render.py` (helpers);
- the folder `rb/` (my sheet dumps, PDF text extractions and page renders).

I did not list, read or open any other scratchpad file or folder. In particular, I did not read `fork1_check.json`, `parts/`, `cands/`, `rows/`, or any R_A file.

However, my `cat > jN.json`, `add.py` and `render.py` writes did not check for existing files. If another agent had same-named files there, I may have overwritten them, and conversely they may have overwritten mine.

After the instruction:

- I moved `rb/` into the private folder `2025_R_B/`.
- I recreated `add.py` and `render.py` there from my own known content, without reading the top-level copies.
- I wrote the last judgment file (`j13.json`) only there.
- I left the top-level `j1-j12.json`, `add.py` and `render.py` untouched rather than delete files that might now belong to someone else.

I then audited `judgments.json`: all 131 rows are my own judgments, and the row count grew consistently as each of my files was merged.

## recalc_check output

```
G: {'PRIMARY READY': 131}
Checks 1 Check -> Result
Checks 2 Reviewer role -> R_B
Checks 3 Candidates -> 131
Checks 4 Primary ready rows -> 131
Checks 5 Unfinished rows -> 0.0
Checks 6 Discuss / unresolved rows -> 0
Checks 7 Workflow status -> PRIMARY READY
Checks 8 Interpretation -> Completion means independent entry is finished. Discuss remains unresolved; affected paper outcome counts are withheld.
Checks 9 Next action -> Filter Decisions status; return to C_ inputs. When primary-ready, save and deliver this file.
Checks 10 Ready discuss rows -> 0
```

## Workbook and script observations

- Neither script showed a bug. `fill_review.py --check` reported 0 errors and 0 missing.
- The Codebook and the column H header misspell "Statistcal".
- Many candidate statements contain the boilerplate "Pending Human Adjudication".
- The Links sheet lists `.ai_paper_validation/...` evidence paths, which reviewers were instructed not to open.
- `jama.2025.11178` contains an Office lock file, `~$joi250046supp5...xlsx`, in the source folder. I did not touch it.
