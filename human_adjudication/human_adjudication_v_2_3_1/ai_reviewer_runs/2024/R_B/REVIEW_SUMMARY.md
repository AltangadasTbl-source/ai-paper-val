# Primary review summary: v.2.3.1, 2024, role R_B

Reviewer: AI-sim-ClaudeOpus5.5-2024-R_B (an AI-simulated reviewer, not a human adjudicator)
Scope: 10 papers, 91 candidates
Outputs (this folder):
- `judgments.json`: one row per candidate with D, E, H–L, the workbook note R, the evidence inspected, and the rationale with recomputations
- `human_adjudication_v_2_3_1_2024_R_B_completed.xlsx`: built with `fill_review.py` from the read-only release template

I did not read R_A outputs, AI pipeline folders (`.ai_paper_validation/`, `workflow_*`, `meta_report/`, `archived/`), earlier adjudication versions, or git history. I also did not open `2024/jama.2024.2302/Detailed_Errors_On_C1_C3_C5.docx`: its name suggests a prior error annotation, so opening it could have compromised independence.

## Method

- **Reading the PDFs.** The Read tool could not render PDFs here because `pdftoppm` is not installed. I installed `pypdf` and `pdfplumber` (with `pypdfium2`) into a virtual environment in the session scratchpad, outside the repository. I used it to extract per-page text and to render pages as images. Every figure-based candidate was checked visually from a rendered image. These included flow diagrams, stacked mRS bars, forest plots, posterior-density eFigures and a rotated CONSORT diagram.
- **Recomputation.** I recomputed every numerical claim in Python: percentages from counts, sums and flows, Wald risk-difference CIs, P values back-calculated from CIs, denominators implied by printed percentages, beta-distribution quantiles (seed 20241010) and Monte Carlo SE comparisons. The arithmetic is recorded in each row's rationale.
- **Domain (E) rule.** I followed the Codebook. A candidate whose judgment rests on a numerical value (a count, percentage, interval, P value or estimate sign) goes to `statistical_results`. A label or wording conflict between the main paper and the results supplement goes to `report_internal_inconsistency`, even when a protocol or SAP also agrees with one side. `protocol_report` is kept for genuine plan-versus-report differences where the report documents agree with each other.

## Counts

| Field | Counts |
|---|---|
| D (disposition) | retain 87, exclude 4, discuss 0 |
| E (domain) | statistical_results 56, report_internal_inconsistency 23, plan_material 6, protocol_report 6 |
| E changed from AI suggestion | 18 of 91 |
| D differing from AI suggested disposition | 3 (AI retain to my exclude). The one AI-suggested exclude (19585 C001) I also excluded |
| H (retained statistical_results, n=53) | confirmed_issue 50, probable_issue 3 |
| I (n=53) | minor_presentation 41, substantive 12 |
| J (optional, n=53) | direct 8, possible 29, unlikely 16 |
| K (retained report-internal/plan, n=29) | minor_presentation 26, substantive_inconsistency 3 |
| L (retained protocol_report, n=5) | substantive_difference 3, minor_presentation 2 |

Excluded rows (4): 12829 C003 and C008 (statistical_results); 19585 C001 (statistical_results); 2302 C005 (protocol_report).

### E changes (AI suggestion to my choice)

To `statistical_results` (the judgment rests on a recomputed number):

| Candidate | From | What it concerns |
|---|---|---|
| 0318 C003 | report_internal | P value incompatible with its CI |
| 0572 C001 | report_internal | Reconstruction of mRS counts from Figure 2 |
| 12829 C016 | report_internal | Primary-outcome event count 9 vs 11 |
| 19585 C002 | report_internal | Rejected share 6.4% vs 10.5% |
| 25786 C003 | report_internal | Adjusted OR upper limit 1.41 vs 1.39 |
| 25786 C004 | report_internal | Subgroup percentage error |
| 25786 C005 | report_internal | Subgroup percentage error |
| 25786 C006 | report_internal | eTable 10 totals and denominators |
| 4183 C007 | report_internal | Sign and direction of a primary contrast |
| 6063 C012 | report_internal | Sign of the primary estimate in Key Points |
| 6063 C013 | report_internal | Adverse-event count 6 vs 5 |
| 6063 C016 | report_internal | Adherence 95% vs 97.6% |

To `report_internal_inconsistency` (the conflict sits between the main paper and the results supplement, or within the main paper):

| Candidate | From | What it concerns |
|---|---|---|
| 11057 C001 | protocol_report | Pre-quit message period, 6 weeks vs 1 week |
| 12829 C009 | protocol_report | 30-day visit window, ±3 vs ±7 days |
| 2302 C001 | protocol_report | SAE label, ≥1 vs >1, with identical counts |
| 23898 C003 | protocol_report | Readmission window, 30 days in Methods vs 90 days in Table 3 |
| 23898 C007 | protocol_report | ERAS adherence subgroup, 2 vs 3 levels |
| 4183 C004 | statistical_results | Wording conflict on who was imputed to continuation |

## Discuss list

None. Every candidate could be settled from the supplied documents once the relevant page or figure was rendered and the numbers recomputed. I used `probable_issue` where a plausible alternative explanation could not be excluded:

- 23898 C006: no overall EQ-5D test is reported.
- 25786 C003: the covariate sets of the two adjusted models are not fully stated.
- 6063 C016: the denominator behind "95%" is not stated.

## Substantive findings (I = substantive, K = substantive_inconsistency, L = substantive_difference)

- **0318 C001.** Figure 1 branches 193 + 122 = 315 under a parent box of 305. Arm-specific participation in the long-term cohort cannot be recovered.
- **0572 C001.** Figure 2 ITT mRS percentages each admit a unique count vector. That vector gives mRS 0–2 of 39/14 and mRS 0–3 of 75/39, against 34/12 and 65/31 in eTable 2. mRS 5–6 and deaths agree.
- **11057 C001.** The main text says pre-quit messaging lasts 6 weeks; the results supplement and protocol say 1 week.
- **12829 C010.** Protocol V2.0 gives the stroke eligibility window as 21–90 days in the synopsis and body but 14–90 days in section 8.1.
- **12829 C016.** Table S6 (center-adjusted) shows 9 BA primary events; the main analysis shows 11. The cell matches the per-protocol table.
- **12829 C017.** Table 2 prints -0.4 (95% CI -2.4 to -1.7). Wald recomputation gives -0.38 (-2.44 to 1.67), so the printed interval has a sign error that makes it exclude 0, against the row's own P = .72.
- **19585 C002.** The main text gives 6.4% rejected; eTable 3 gives 142/1350 = 10.5%.
- **2302 C003.** The reported intervention prior (95% CrI 0.33–3.0, SD about 0.56 on the log scale) differs from the SAP prior of Normal(0, 0.7), whose 95% interval is 0.25–3.94.
- **23898 C002.** Opioid consumption is reported up to 24 hours; the protocol and SAP plan 72 hours.
- **23898 C003.** Readmission is defined as within 30 days in Methods but labelled 90 days in Table 3.
- **23898 C004.** The ERAS subgroup cut points differ from the protocol's example bands. The eFigure footnote discloses this.
- **4183 C005 and C006.** The abstract gives the CrI for the CNRT rescue contrasts as 6%–11%; Results and eTable 4 give 2%–11% or 2%–10%.
- **4183 C007.** For varenicline switch vs stay, the sign and stated direction of the primary contrast conflict across the abstract, Results and eTable 4.
- **4183 C018.** For phase-1 abstainers at EOT+30, the supplement narrative gives ARD 1.1%; eTable 11 gives 11%. The narrative value looks plausible, so it could be extracted as is.
- **6063 C009, C010 and C011.** eTable 4 rows were copied from other rows: week-4 weight-bearing pain, week-12 lower-leg strength, and week-12 glucose between-group. The correct values are not reported anywhere.

## Disagreements with the AI rationale or disposition

- **12829 C008, excluded.** The AI treated stenosis categories outside the 70%–99% range as a conflict. Figure 1 discloses these patients as adjudicated per-protocol exclusions (2 with stenosis <70%, and 1 occlusion per arm), and they match Table 1 exactly.
- **12829 C003, excluded.** The Table S4 header footnote explains the 241 denominator.
- **2302 C005, excluded.** Enrollment and randomization are used interchangeably in the protocol itself for the same 10-month window, and randomization happens at enrollment.
- **2302 C001.** Identical counts in the main paper and the eTable show the same endpoint was analyzed. The ">1" reads as a lost "≥", so this is a label inconsistency, not a different endpoint.
- **6063 C003–C008.** The AI treated these as six separate arithmetic errors. All six arise from one cause: eTable 5 prints pooled (n = 216) percentages in both arm columns.
- **23898 C005.** The AI leaned toward the legend's "99%" being correct because the SAP specifies 99%. The plotted bars match the printed intervals, and the overall row equals the main-text 95% CI, so the legend is the wrong label.
- **0318 C003.** Recomputation shows the main-text P = .002 is the value incompatible with the CI. The maximum P over CI rounding is about .0009.
- **4183 C010.** Beyond the flagged Beta(785, 869), the CNRT response row Beta(193, 210) also does not match its printed interval.

## Sources

No source needed for a judgment was unreadable. Text extraction failed for the rotated Figure 2 page in 4183, and that page was rendered and read as an image. The 0572 supplement 5 eFigure 3 (p.8) is image-only and was not rendered: the population counts it shows were taken from the main text and eTable 2. The only file deliberately not inspected was the 2302 `.docx` noted above.

## Possible errors noticed outside the candidate list (not added to the workbook)

- **12829 Table 1.** BA stenosis 90%–99% is printed as 25 (10.4); 25/249 = 10.0%.
- **23898.** Subgroup intervals appear to be 95%, while the SAP planned 99% CIs for subgroups.
- **2302.** The main-text main-effect prior range (0.33–3.0) coincides with the interaction-term prior. This suggests a description error rather than a changed model; it was not tested.

## recalc_check output

```
G: {'PRIMARY READY': 91}
Checks 1 Check -> Result
Checks 2 Candidates -> 91
Checks 3 Primary ready -> 91
Checks 4 Unfinished -> 0.0
Checks 5 Discuss / unresolved -> 0
Checks 6 Workflow status -> PRIMARY READY
Checks 7 Ready with discuss -> 0
Checks 8 Meaning -> PRIMARY READY means independent data entry is complete; discuss remains unresolved and prevents that paper's outcome counts.
Checks 9 Next action -> Inspect G on C_ sheets or filter Decisions readiness. Save the completed file and deliver it; preserve normal Excel backups.
```

`fill_review.py --check`: keys = 91, judged = 91, missing = 0, no errors.

## Notes on the workbook and scripts

- No script bugs were found.
- **`--check` exit code.** `fill_review.py --check` exits 0 even when keys are missing (it prints them as MISSING lines). That is by design, but a caller relying only on the exit code would miss incomplete files.
- **Pre-filled E column.** The release template's E column comes pre-filled with the AI-suggested domain, and the Candidates sheet carries an `ai_disposition` column. The Codebook says no AI disposition is preselected, which is true of column D, but the AI disposition is visible to reviewers in Candidates. Coordinators may want to confirm that this exposure is intended.
- **Evidence text placeholders.** Some candidates' Evidence text (all of 4183) contains generic placeholders ("Reproduce the stated arithmetic ... see source evidence") rather than the comparison itself, so reviewers have to go to the PDFs.
