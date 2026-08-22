# Table Arithmetic / Internal-Consistency Check — DOC-001 Table 1–2 and DOC-004 eTable

## Scope and method

- **Audited source tables only:** DOC-001 `jama_parsons_2020_oi_190140.pdf`, Table 1 (PDF p. 5 / printed p. 144) and Table 2 (PDF p. 7 / printed p. 146); DOC-004 `joi190140supp3_prod.pdf`, eTable (PDF p. 2).
- **Source confirmation:** Native extraction was checked against the rendered source pages: `.ai_paper_validation/preprocessing/DOC-001/page_images/page-005.png`, `page-007.png`, and `.ai_paper_validation/preprocessing/DOC-004/page_images/rendered_page.png`.
- **Excluded by design:** DOC-002 protocol, DOC-003 SAP, DOC-005 administrative material, and all non-table items.

## Candidate issues for verification

### T-01 — Double minus sign makes one printed CI bound non-numeric

- **Category / severity:** Presentation inconsistency / low.
- **Exact location:** DOC-004, `joi190140supp3_prod.pdf`, PDF p. 2, eTable, **Energy (kcal/day)**, Control, 24-month, Mean Change (95% CI).
- **Verbatim reported value:** Mean change `-130.3`; CI `(--195.08, -65.52)`.
- **Direct comparator:** DOC-001, `jama_parsons_2020_oi_190140.pdf`, PDF p. 7 / printed p. 146, Table 2, Energy, Control Group, 24-Month Change: `−130.3 (−195.08 to −65.52)`.
- **Calculation / logical check:** A 95% CI should contain two signed numeric bounds. The eTable token `--195.08` has two consecutive minus signs and therefore is not a valid conventional numeric representation. Removing one minus yields `−195.08`, exactly the bound printed for the same mean change in Table 2.
- **Reasoning and bounded impact:** This is a visible typographic/presentation defect in the supplementary eTable. It obstructs unambiguous reading of one CI bound; the main-article comparator supports the intended bound but does not establish which source was corrected first.
- **Human verification:** 1. Inspect the PDF p. 2 cell and confirm the displayed string is `(--195.08, -65.52)`. 2. Inspect Table 2 PDF p. 7 and confirm `(-195.08 to -65.52)`. 3. Resolve by correcting the eTable cell if it is intended to reproduce the Table 2 result.

### T-02 — Same Energy 24-month between-group comparison has incompatible reported P values

- **Category / severity:** Cross-document inconsistency / moderate.
- **Exact locations:** DOC-004, PDF p. 2, eTable, **Energy (kcal/day)**, MEAL Intervention, 24-month, `p-value†`; DOC-001, PDF p. 7 / printed p. 146, Table 2, Energy, 24-Month, Between-Group Difference, P Value (footnote d).
- **Verbatim reported values:** eTable: intervention change `−250.01 (−315.43, −184.59)`, control change `−130.3 (--195.08, −65.52)`, `p-value† < 0.001`. Table 2: intervention `−250.01 (−315.43 to −184.59)`, control `−130.3 (−195.08 to −65.52)`, difference `−119.71 (−211.78 to −27.65)`, `P = .01`.
- **Comparison rule (verbatim footnotes):** eTable `† changes in intervention compared to changes in control`; Table 2 footnote d `Changes in intervention compared with changes in control.`
- **Calculation / logical check:** The displayed change contrast is `−250.01 − (−130.30) = −119.71`, exactly the Table 2 between-group estimate. Thus the two P values label the same displayed 24-month contrast but differ: `<.001` versus `.01`. As an additional display-only check, the Table 2 CI midpoint is `(−211.78 + −27.65)/2 = −119.715` and its half-width is `92.065`; the estimate is not compatible with a conventional two-sided 95%-CI/Wald display yielding `P<.001` (its approximate z is `119.715/(92.065/1.96)=2.55`, P approximately .011).
- **Reasoning and bounded impact:** The direction and reported CI/estimate are unchanged, but the reported strength of evidence for this dietary comparison differs materially by source. No raw data are needed to verify the conflicting printed labels.
- **Human verification:** 1. Verify the two footnote definitions. 2. Confirm the three change estimates and each P-value cell in the PDFs. 3. Check the analysis output or erratum to determine whether `.01` or `<.001` is the intended 24-month between-group P value.

### T-03 — Same saturated-fat 12-month between-group comparison is reported with different P thresholds

- **Category / severity:** Cross-document inconsistency / low.
- **Exact locations:** DOC-004, PDF p. 2, eTable, **Saturated fat (gm/day)**, MEAL Intervention, 12-month, `p-value†`; DOC-001, PDF p. 7 / printed p. 146, Table 2, Saturated fat, 12-Month, Between-Group Difference, P Value (footnote d).
- **Verbatim reported values:** eTable: intervention change `−1.69 (−2.07, −1.3)`, control change `−0.44 (−0.82, −0.06)`, `p-value† < 0.01`. Table 2: same intervention and control changes, difference `−1.25 (−1.79 to −0.7)`, `P < .001`.
- **Calculation / logical check:** `−1.69 − (−0.44) = −1.25`, matching the Table 2 between-group estimate. The eTable and Table 2 therefore label the same displayed contrast but use different P thresholds. The Table 2 CI is also consistent with the more stringent threshold: midpoint `(−1.79 + −0.70)/2 = −1.245`; half-width `0.545`; approximate z `1.245/(0.545/1.96)=4.48`, two-sided P approximately `0.000008`.
- **Reasoning and bounded impact:** `<.001` necessarily also satisfies `<.01`, so this does not reverse the result. It is nevertheless an inconsistent precision/threshold report for the same comparison and should be reconciled.
- **Human verification:** 1. Confirm the footnote-dagger and footnote-d comparison definitions. 2. Confirm each P-value cell. 3. Compare against the model output and harmonize the intended reporting threshold.

### T-04 — eTable N labels conflict with the article’s stated diet-analysis sample counts for the reproduced results

- **Category / severity:** Cross-document inconsistency / moderate (candidate; population definition requires adjudication).
- **Exact locations:** DOC-004, PDF p. 2, eTable column headings; DOC-001, PDF p. 5 / printed p. 144, **Correlative Outcomes** paragraph referring to Table 2.
- **Verbatim reported values:** eTable headers: MEAL `Baseline N=237`, `12-month N=236`, `24-month N=233`; Control `Baseline N=241`, `12-month N=240`, `24-month N=238`. Article text: `At 12-month follow-up, intervention participants (n = 208) ... controls (n = 199)`; `At 24-month follow-up ... intervention group: 190; control group: 185`.
- **Direct linkage:** The eTable reproduces Table 2 values, including, for example, total-vegetables changes at 12/24 months of `2.43`/`2.01` for intervention and `0.45`/`0.37` for control, the same values explicitly cited in the article paragraph.
- **Calculation / logical check:** Header minus text count differences are: intervention `236−208=28` at 12 months and `233−190=43` at 24 months; control `240−199=41` and `238−185=53`, respectively. They exceed a rounding tolerance because they are whole participant counts. The eTable’s headers also exceed the Table 1 analysis-arm denominators (`226` intervention; `217` control) at every follow-up.
- **Reasoning and bounded impact:** Two tables/text passages representing the same diet results show different sample-size labels without a definition explaining the difference. The available documents do not establish whether the eTable includes randomized/ineligible participants or whether a heading is erroneous; this is a candidate, not a conclusion about the estimates.
- **Human verification:** 1. Confirm the four article-text counts and six eTable header counts. 2. Check whether the eTable uses a separately defined all-randomized dietary dataset. 3. If no such definition exists, correct or annotate the eTable N labels; if it exists, add that population definition to resolve the ambiguity.

### T-05 — Comma-decimal typo/ambiguity in two control-legume CI lower bounds

- **Category / severity:** Presentation inconsistency / low.
- **Exact location:** DOC-004, PDF p. 2, eTable, **Legumes (servings/day)**, Control, 12-month and 24-month Mean Change (95% CI).
- **Verbatim reported values:** Both cells print `0.03 (−0,03, 0.1)`.
- **Direct comparator:** DOC-001, PDF p. 7 / printed p. 146, Table 2, Legumes, Control Group: 12-month `0.03 (−0.03 to 0.1)`; 24-month `0.03 (−0.03 to 0.1)`.
- **Calculation / logical check:** The eTable uses decimal points throughout its other numeric cells and commas to separate the CI endpoints. In `−0,03, 0.1`, the first comma is therefore ambiguous; the Table 2 comparator displays the same bound as `−0.03`.
- **Reasoning and bounded impact:** This appears to be a repeated formatting typo rather than a change in the numerical estimate, but it makes two CI lower bounds less machine- and human-readable in the supplementary source.
- **Human verification:** 1. Inspect both eTable cells. 2. Compare them with the corresponding Table 2 cells. 3. Resolve by using a decimal point consistently if the eTable is meant to match Table 2.

## Checks with no candidate retained

- **Table 1:** All displayed percentages checked from their stated denominators round correctly to one decimal place. Fully enumerated race/ethnicity totals are `226` and `216`; region totals are `226` and `217`; tumor-stage totals are `225` and `217`. No arithmetic candidate retained. The displayed PSA rows are not treated as an error because the table does not state that those two ranges are exhaustive.
- **Table 2 arithmetic:** For every row, the displayed between-group mean change equals the displayed intervention minus control change exactly or within `0.01` in the last reported decimal. Because the table reports estimates from a mixed-effects model, these one-hundredth differences are compatible with unrounded model estimates; no within-table arithmetic candidate is retained on that basis.

## Audit status

Audited result-relevant tables only. Five document-verifiable candidates returned; no claim is made about raw data or unreported analyses.
