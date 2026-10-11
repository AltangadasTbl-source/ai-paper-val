# v.2.3.1 primary review: 2019, role R_A

Reviewer ID entered in Setup: `AI-sim-ClaudeOpus5.5-2019-R_A`. This is an AI-simulated reviewer (a Claude Opus 5.5 agent), not a human adjudicator. The review was independent: I did not read R_B output, pipeline folders, earlier adjudication versions, or `records/`.

## Files

- `judgments.json`: all 62 judgments, each with a workbook note (R), the pages inspected, and a full rationale.
- `human_adjudication_v_2_3_1_2019_R_A_completed.xlsx`: the completed workbook, built with `fill_review.py`.

## Counts

- **Disposition (D):** retain 58, exclude 4, discuss 0.
- **Domain (E):**

  | Domain | Total | Retain | Exclude |
  |---|---|---|---|
  | report_internal_inconsistency | 25 | 25 | 0 |
  | statistical_results | 23 | 22 | 1 |
  | plan_material | 7 | 7 | 0 |
  | protocol_report | 7 | 4 | 3 |

- **E changed from the AI suggestion:** 3.
  - 14901 C005: report_internal_inconsistency to statistical_results. The question is whether P = .1057 was correctly rounded to .10.
  - 7505 C001: report_internal_inconsistency to statistical_results. The abstract CI sign error can be recomputed from the counts.
  - 2210 C002: statistical_results to report_internal_inconsistency. This is a caption-versus-display conflict, not a numeric error.
- **D differing from the AI's baseline "retain":** 4 exclusions.
  - 12618 C003: block sizes. The report matches both SAP versions; only the superseded 2012 MOP differs.
  - 14231 C007: 2-patient denominator difference between eTable 3 and the eTable 10 analytic-sample table. No printed value changes.
  - 17380 C007: M = 20 vs 10 imputations. The method is as planned, and M affects only Monte Carlo precision.
  - 2210 C008: the time origin is described as randomization in the report and as supplement start in the protocol. The article states these are the same visit.

### Outcome codes (retained rows only)

- **Statistical results (n = 22).**
  - H: confirmed_issue 22.
  - I: substantive 9, minor_presentation 13.
  - J: direct 7, possible 7, unlikely 8.
- **Confirmed and substantive statistical issues (9):**
  - 12618 C005
  - 14231 C002-C006
  - 14901 C003, C004
  - 7505 C002
- **K (report_internal_inconsistency and plan_material, n = 32):** substantive_inconsistency 1 (2210 C009), minor_presentation 31.
- **L (protocol_report retained, n = 4):**
  - substantive_difference 2: 12618 C004, 14901 C002.
  - minor_presentation 2: 14231 C001, 2210 C004.

## Discuss list

None. Every candidate could be settled from the supplied documents. I considered `discuss` for two rows and rejected it:

- **7505 C002.** The DIC row itself is unambiguously wrong. The broader concern about the RR column (below) is recorded in the rationale as an exploratory observation, not as the basis of the disposition.
- **12618 C005.** The summary statistics and the P value are mutually incompatible. Which one is wrong cannot be determined, but under the Codebook that is still a confirmed issue.

## Where I disagreed with or went beyond the AI rationale

- **12618 C002.** The AI framed 68 against 74. Figure 1 accounts for every failure (20 + 9 + 3 and 29 + 11 + 2). Eligible (non-safety) failures are therefore 69, so 68 matches neither total. The arm percentages use all failures, not eligible ones.
- **12618 C005.** Agree with the incompatibility, and add two checks. P = .87 would need an SE of about 1.83, and treating the SDs as SEs still gives P of about .79. The SDs (1.0 and 0.5 on means of about 4.5%) look implausible.
- **14231 C002-C006.** The AI treated these as 5 separate arithmetic slips. Every row with no competing risk of death reconciles exactly (composites and all-cause mortality). Every nonfatal single outcome does not, and the bootstrap CIs are centred on the printed ARDs. This points to a systematic, undocumented estimator difference, such as 1-KM versus competing-risk cumulative incidence.
- **14231 C007.** Excluded rather than retained (see above).
- **14630 C005.** The 544 SD also appears in eTable 5 (completers), and Table 3's 555 equals the control SD. This points to a transcription error in the main table.
- **14901 C001-C006.** The workbook gives no source location and no Evidence rows for any candidate in this paper. I located every passage myself.
- **14901 C003-C004.** The counts are correct, because they sum with the nonhypercapnic counts to main Table 1. The percentages are complements, which reverses the apparent prevalence (69% printed vs 31% actual). I rated these substantive.
- **17380 C003-C006.** By cross-matching the factorial-cell means between Figures 3 and 4 and eFigures 2 and 3, I confirmed that only the N columns are transposed. The means and ratios follow the headings.
- **2210 C002.** Figure 2C (the competing-risk panel) is the panel that actually lacks numbers at risk. The caption sentence was most likely misplaced from Figure 2 into Figure 3.
- **2210 C007.** I disagree with the AI's claim that the BMI percentages show the smaller denominator. They round identically with 249 or 251 (and with 165 or 166).
- **2210 C008.** Excluded, because the article itself states the two time origins are equivalent.
- **2210 C009.** The AI suggested report_internal_inconsistency without a severity. I rated it a substantive inconsistency because the footnote reverses the direction of effect for the table holding the subgroup and cause-specific estimates.
- **4755 C001-C003.** I could not reproduce the AI's "detached 18.2/25.7/21.6 text fragment" in my own extraction of PDF p. 7. Only the visible hyphens are confirmed. All three women's rows, the only negative two-digit values, are affected, consistent with column clipping.
- **7505 C002 (beyond the candidate; exploratory).** The DIC RR of 2.00 equals the high-PEEP risk divided by the pooled risk, (1/989)/(1/1976). That ratio reproduces most Table 3 RRs to within 0.01. Examples, with the crude high-vs-low RR in parentheses:
  - pleural effusion 1.34 (crude 2.04)
  - mortality 1.41 (crude 2.40)
  - ARDS 1.50 (crude 2.99)
  - pneumothorax 0.50 (crude 0.33)

  It does not reproduce some common outcomes: primary outcome 0.95 vs printed 0.93 vs crude 0.90, and hypotension 1.29 vs 1.43 vs 1.84. The printed CIs are also narrower than the counts support. The whole RR column, including the abstract's primary RR, should be checked against the analysis code. This was computed post hoc and has not been verified.

## Other observations outside the candidates (not adjudicated)

- **12618 eTable 8.** The headers (N = 62/56) differ from the Figure 1 12-month continuing counts (60/54).
- **14231 Table 1.** Several after-matching standardized differences remain large (systolic 30.1, diastolic -44.2).
- **14630 eTable 5 and eTable 9.** Baseline values for the completers-only populations are identical to the all-randomized values despite smaller Ns.
- **17380.** The plan's ITT definition (participants returning at least one follow-up biosample) is narrower than the article's ("regardless of adherence or follow-up").

## Sources and tooling

- **Unreadable sources:** none. Two PDF pages have no text layer (12618 `joi190092supp2_prod.pdf` pp. 80-81). I rendered them as images and read them.
- **PDF reading method:** the Read tool could not render PDFs (no poppler). The project venv has no PDF library. I therefore used the system `python3` with the user-installed PyMuPDF (`fitz` 1.28.2) to extract text and render pages to PNG. All other computation used `V/2019/.venv/bin/python`.
- **Shared scratchpad:** the scratchpad was shared with other agents. Before moving my work into a private subfolder, I wrote a few files at the scratchpad root:
  - `tools/pdft.py`
  - `txt/jama.2019.*`
  - `img/`
  - a temporary `cands.txt`, which I later deleted

  If another agent had a file of the same name there, it may have been overwritten. I did not read any other agent's files.

## Workbook and script observations

- **Missing context for paper 14901.** All 6 candidates have empty source locations (column C and `locations`) and no Evidence rows. Their only Links point into `.ai_paper_validation/`, which reviewers in this run may not open. A human reviewer would have to locate everything from scratch.
- **Scripts.** `fill_review.py` and `recalc_check.py` behaved as documented. I found no bugs.

## recalc_check output

```
G: {'PRIMARY READY': 62}
Checks 1 Check -> Result
Checks 2 Reviewer role -> R_A
Checks 3 Total candidates -> 62
Checks 4 Primary ready -> 62
Checks 5 Unfinished -> 0.0
Checks 6 Discuss / unresolved -> 0
Checks 7 Workflow status -> PRIMARY READY
Checks 8 Ready discuss rows -> 0
Checks 9 Papers with counts -> 9
Checks 10 Next action -> Save and deliver this independent review with its built-in results.
Checks 11 Scope -> Entry checks and independent completion only. Discuss is not a confirmed absence of error. Review the evidence; preserve ordinary Excel backups.
```
