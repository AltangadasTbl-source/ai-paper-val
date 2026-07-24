# Figure and participant-flow check — D001 main article and D003 results supplement

## Scope

- Checked the D001 main-article participant-flow Figure and its caption on PDF source p. 6 (printed p. 718), including all visible nodes, arrows, labels, annotations, and counts.
- Checked D001 rendered result-table pages 4–7 where captions, headings, or visible table structure were relevant to nearby text.
- Checked the D003 result-relevant rendered eTables on PDF source pp. 7–15 and their headings, column labels, row labels, footnotes, and visible cell placement.
- Used only supplied package artifacts. D002 protocol was not opened. No web or external source was used.

## Retained local candidates

### FFC-01 — eTable 5 title says the outcomes are “Among 7-month Responders,” but its Missing=Vaping rows use the full randomized denominators

- **Category:** Presentation inconsistency
- **Status:** Candidate — high confidence
- **Exact location:** D003 `joi240078supp2_prod_1739900423.24574.pdf`, PDF source p. 14, **eTable 5**, title, column headers, “No. responses,” “No. abstinent,” and both “Missing=Vaping” rows ([rendered page](../document_outputs/D003_results_supplement/preprocessing/page_images/page_014.png); [page text](../document_outputs/D003_results_supplement/preprocessing/native_text/page_014.txt)).
- **Visible/source values:**
  - Title: “Vaping Cessation Outcomes Among 7-month Responders, % (95% CI).”
  - Column headers: intervention `n=759`; control `n=744`.
  - 30-day ppa: `No. responses` 521 and 543; `No. abstinent` 287 and 208; CCA 55.1% and 38.3%; Missing=Vaping 37.8% and 28.0%.
  - Repeated ppa: `No. responses` 517 and 538; `No. abstinent` 131 and 61; CCA 25.3% and 11.3%; Missing=Vaping 17.3% and 8.2%.
- **Logical basis:** The CCA percentages are responder-only (`287/521=55.1%`, `208/543=38.3%`; `131/517=25.3%`, `61/538=11.3%`). The Missing=Vaping percentages instead use all randomized participants (`287/759=37.8%`, `208/744=28.0%`; `131/759=17.3%`, `61/744=8.2%`). Therefore, the table includes analyses that are not “among 7-month responders,” contrary to the unqualified title.
- **Verification instruction:** On original supplement PDF p. 14, recompute all four displayed Missing=Vaping percentages using both the response counts and the column-header denominators; confirm that only `759/744`, not `521/543` or `517/538`, reproduce the displayed values. Adjudicate whether the title should be broadened or the Missing=Vaping rows explicitly identified as full randomized-sample analyses.

### FFC-02 — eTable 4 labels motivation and confidence summaries as median (IQR), but the displayed form is inconsistent with that label and with the same variables in main Table 1

- **Category:** Presentation inconsistency
- **Status:** Candidate — high confidence
- **Exact locations:**
  - D003 supplement PDF source p. 12, **eTable 4**, rows “Motivation to quit vaping, median (IQR)” and “Confidence to quit vaping, median (IQR)” ([rendered page](../document_outputs/D003_results_supplement/preprocessing/page_images/page_012.png); [page text](../document_outputs/D003_results_supplement/preprocessing/native_text/page_012.txt)).
  - D001 main article PDF source p. 4 (printed p. 716), **Table 1**, corresponding rows ([rendered page](../document_outputs/D001_main_article/preprocessing/page_images/page_004.png); [page text](../document_outputs/D001_main_article/preprocessing/native_text/page_004.txt)).
- **Visible/source values:**
  - eTable 4 motivation: nonresponders `4.1 (0.8)`, responders `4.1 (0.8)`, while the row says `median (IQR)`.
  - eTable 4 confidence: nonresponders `3.2 (1.1)`, responders `3.5 (1.1)`, while the row says `median (IQR)`.
  - Main Table 1 expresses the same variables as medians with interval-form IQRs: motivation `4.0 (4.0-5.0)` in both groups; confidence `3.0 (3.0-4.0)` in both groups.
  - On the same eTable 4 page, other median (IQR) rows use interval-form parentheses, for example days per month vaping `30.0 (27.0-30.0)` vs `29.0 (26.0-30.0)` and concern about health consequences `4.0 (3.0-5.0)` vs `3.0 (3.0-4.0)`.
- **Logical basis:** The single-number parenthetical summaries `0.8`, `1.1` do not have the same displayed IQR form as every nearby median (IQR) row, while the central values also differ from the integer median style used for the same measures in main Table 1. The row labels are therefore likely mislabeled, most plausibly showing mean (SD), but the proposed correction must be checked against the analysis output.
- **Verification instruction:** Inspect the eTable 4 source/output definition for these two rows and determine whether `4.1 (0.8)`, `3.2 (1.1)`, and `3.5 (1.1)` are means (SDs). If so, change only those two row labels from median (IQR) to mean (SD); do not infer the correction solely from formatting.

### FFC-03 — The expansion of GAIN-SS changes from “Global Appraisal” in eTable 1 to “Global Assessment” elsewhere in the supplied article package

- **Category:** Presentation inconsistency
- **Status:** Candidate — high confidence
- **Exact locations:**
  - D003 supplement PDF source p. 8, **eTable 1 continued**, row header: “Global Appraisal of Individual Needs - Short Screener (GAIN-SS)” ([rendered page](../document_outputs/D003_results_supplement/preprocessing/page_images/page_008.png); [page text](../document_outputs/D003_results_supplement/preprocessing/native_text/page_008.txt)).
  - D003 supplement PDF source p. 15, **eTable 6**, row header: “Global Assessment of Individual Needs - Short Screener (GAIN-SS)” ([rendered page](../document_outputs/D003_results_supplement/preprocessing/page_images/page_015.png); [page text](../document_outputs/D003_results_supplement/preprocessing/native_text/page_015.txt)).
  - D001 main article PDF source p. 5 (printed p. 717), Table 1 abbreviation legend: “GAIN-SS, Global Assessment of Individual Needs–Short Screener” ([rendered page](../document_outputs/D001_main_article/preprocessing/page_images/page_005.png); [page text](../document_outputs/D001_main_article/preprocessing/native_text/page_005.txt)).
- **Logical basis:** The same acronym is visibly expanded with two different words—“Appraisal” on eTable 1 and “Assessment” in both the main article and eTable 6. At least one package label is inconsistent.
- **Verification instruction:** Compare the three supplied locations and correct the outlying eTable 1 expansion if the source instrument name in the article’s own measure definition agrees with “Assessment.” No external instrument knowledge is needed to verify the package inconsistency.

### FFC-04 — eTable 3 has visibly colliding/misaligned numeric cells that obscure column boundaries

- **Category:** Presentation inconsistency
- **Status:** Candidate — medium/high confidence; verify in the original PDF viewer before acceptance
- **Exact location:** D003 supplement PDF source p. 11, **eTable 3, Sensitivity of Intervention Effects to Missing Data Assumptions**, body rows ([rendered page](../document_outputs/D003_results_supplement/preprocessing/page_images/page_011.png); [page text preserving intended columns](../document_outputs/D003_results_supplement/preprocessing/native_text/page_011.txt)).
- **Visible evidence:** In the rendered supplied page, several adjacent cells visibly run together or appear displaced. Examples include:
  - `OR.miss=1/20`: P0 `53.49` and Diff.vape `13.94` appear as `53.4913.94`.
  - `OR.miss=1/10`: P0 `52.15` and Diff.vape `13.71` appear as `52.1513.71`.
  - `OR.miss=1/5`: OR.vape `1.73` and P value `<.0001` visually collide.
  - Similar collisions or irregular horizontal placement recur in the `4/5`, `5/4`, `3/2`, and `2` rows.
- **Logical basis:** The table header defines separate P0, Diff.vape, RR.vape, OR.vape, and P-val columns, but visible text placement makes multiple body cells read as concatenated values. The native text layer preserves separable values, indicating a layout/presentation problem rather than a numerical contradiction.
- **Verification instruction:** Open original supplement PDF p. 11 in an independent PDF viewer at 100% and 200% zoom and render it again with a second renderer. Accept only if the overlaps/misplacements are present in the source PDF rather than introduced by the preprocessing renderer; if confirmed, typeset the cells with sufficient column spacing.

## Lower-priority visible presentation checks

These are document-verifiable but are not recommended ahead of the four candidates above if the coordinator needs to conserve the package-level candidate cap.

### FFC-L1 — Missing range separator in one eTable 2 IQR

- **Category:** Presentation inconsistency
- **Status:** Low-priority candidate
- **Location:** D003 supplement PDF p. 9, eTable 2, waitlist-control “Motivation to quit vaping, median (IQR)” cell ([rendered page](../document_outputs/D003_results_supplement/preprocessing/page_images/page_009.png); [page text](../document_outputs/D003_results_supplement/preprocessing/native_text/page_009.txt)).
- **Evidence:** The assessment-only value is `4.0 (4.0-5.0)`, but the waitlist value is printed `4.0 (3.0 5.0)`, with no separator between 3.0 and 5.0. Nearby IQRs use a hyphen/range separator.
- **Verification:** Confirm on original PDF p. 9 and insert the omitted range separator if the intended IQR is `3.0-5.0`.

### FFC-L2 — eTable 6 has one visibly displaced contrast row in the supplied rendering

- **Category:** Presentation inconsistency
- **Status:** Uncertain; renderer verification required
- **Location:** D003 supplement PDF p. 15, eTable 6, “Perceived addiction to vaping (Ref: Very Addicted)” contrasts, especially “Somewhat addicted” ([rendered page](../document_outputs/D003_results_supplement/preprocessing/page_images/page_015.png); [page text](../document_outputs/D003_results_supplement/preprocessing/native_text/page_015.txt)).
- **Evidence:** In the rendered page, the `Somewhat addicted` numeric entries `.465`, `.713`, `.515` appear far to the left of the Beta, Std. Error, and P-nom columns, unlike the two subsequent contrasts. The native text layer places them as Beta `.465`, SE `.713`, P-nom `.515`.
- **Verification:** Inspect the source PDF in another viewer/render. Reject if the displacement is only a preprocessing-renderer artifact; otherwise retain as a presentation problem.

## Participant-flow reconciliation results

No participant-flow candidate was retained.

- `19,495 screened − 13,778 excluded = 5,717 eligible`. The listed screen-exclusion reasons total more than 13,778, but the Figure explicitly labels them “not mutually exclusive,” so this is **rejected as an inconsistency**.
- `5,717 eligible − 3,273 excluded = 2,444 assented`; the four listed reasons sum to 3,273.
- `2,444 assented − 763 excluded = 1,681 randomized`; the five listed reasons sum to 763.
- Randomized allocation reconciles: `759 + 744 + 178 = 1,681`.
- One-month boxes reconcile within arm: intervention `609 + 150 + 0 = 759`; assessment-only `636 + 106 + 2 = 744`; waitlist `152 + 26 + 0 = 178`. Completed surveys reconcile with the main-text total: `609 + 636 + 152 = 1,397`; `1,397/1,681 = 83.1%`.
- Seven-month boxes reconcile within arm: `521 + 238 = 759`; `543 + 201 = 744`; `132 + 46 = 178`. Completed surveys reconcile with the main-text total: `521 + 543 + 132 = 1,196`; `1,196/1,681 = 71.1%`.
- The Discussion’s `70.8%` 7-month retention is **not contradictory** to the Results’ `71.1%`: `70.8% = (521+543)/(759+744) = 1,064/1,503`, the two main trial groups, whereas `71.1% = 1,196/1,681` includes the waitlist group.
- The Figure lists 2 assessment-only participants as withdrawn at 1 month but folds all 7-month noncompleters into `201 Lost to follow-up`. This was classified **Uncertain / not a candidate** because the 7-month box still reconciles exactly to 744 and the Figure does not define whether “lost to follow-up” is a mutually exclusive cumulative status at that later time point.
- The Figure appropriately includes the waitlist group in the randomized flow but lists only the two main groups as “Included in primary analysis”; its caption explicitly states the waitlist group was contextual and the main analysis sample was `n=1503`. This is **rejected as an inconsistency**.

## Supplement figure/flow inventory

D003 result-relevant pages contain no figures or participant-flow diagrams. Review therefore focused on visible eTable captions, headings, labels, footnotes, cell placement, and comparison with explicitly referenced main-article tables/text.
