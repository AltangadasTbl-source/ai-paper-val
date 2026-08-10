# Human Adjudication Report

## Scope and disposition

This report contains the nine findings retained by critic review (all **Minor**); one additional candidate was rejected and is not presented as an issue. Scientific review was limited to the main article (DOC-001, PDF pp. 1–10) and result-relevant pages of the results supplement (DOC-004, PDF pp. 10–27). The protocol, SAP, administrative, analysis-code, and data-sharing PDFs were **Not Audited by Design** for scientific findings; their rights screens were retained. Source PDFs were not modified. This report is for human adjudication and the separate compliance screen is not legal advice.

## Scientific evidence cards

### 1. eTable 6 overall adverse-event total is one event short

- **Category / severity:** Arithmetic inconsistency / Minor.
- **Issue:** The results supplement reports 145 prespecified adverse events overall, although its arm totals and each displayed classification block total 146, requiring confirmation of the supplement header.
- **Evidence:** **Reported overall:** DOC-004 (`supplement_3_results`), `joi250066supp3_prod_1761597796.4701.pdf`, PDF p. 17, eTable 6 header: `n=145`; placebo `67`; levodopa `79`. **Breakdowns:** same location, intensity `58, 86, 2`; outcome `1, 29, 116`; drug relation `2, 66, 23, 2, 39, 14`. **Comparator:** DOC-001 (`main_article`), `jama_engelter_2025_oi_250066_1761597796.45511.pdf`, PDF p. 6, Table 2 and *Adverse Events* text: arm totals `79` and `67`, overall `146`.
- **Direct comparison:** Reported overall `145`; comparator/expected from all displayed components `146`; discrepancy `+1 event` versus the header.
- **Reproducible check:** `67 + 79 = 146`; `58 + 86 + 2 = 146`; `1 + 29 + 116 = 146`; `2 + 66 + 23 + 2 + 39 + 14 = 146`. Counts are integers; rounding tolerance `0` events.
- **Bounded impact:** One-event error in the supplement header; this evidence does not show which, if any, arm count or classification count is wrong.
- **Verification:** 1. Check eTable 6’s source table/header and all row totals. 2. Confirm whether the intended overall total is 146; confirmation resolves the header discrepancy, while a verified component correction would identify the alternative resolution.

### 2. Stroke-type arm counts do not reconcile

- **Category / severity:** Cross-document inconsistency / Minor.
- **Issue:** The supplement’s levodopa stroke-type counts conflict with both its stated overall counts and the main article, so the stroke-type values require confirmation.
- **Evidence:** **Supplement:** DOC-004, `joi250066supp3_prod_1761597796.4701.pdf`, PDF p. 10, eTable 1, Type of stroke: ischemic overall/placebo/levodopa `519/259/263`; hemorrhagic `91/44/44`. **Main article comparator:** DOC-001, `jama_engelter_2025_oi_250066_1761597796.45511.pdf`, PDF p. 4, Table 1, Type of stroke: levodopa ischemic `260 (84.7%)`, hemorrhagic `47 (15.3%)`; placebo ischemic `259 (85.5%)`, hemorrhagic `44 (14.5%)`.
- **Direct comparison:** Supplement values yield ischemic `522` versus reported overall `519` (`+3`) and hemorrhagic `88` versus `91` (`-3`). Main-article values yield the supplement overall counts exactly.
- **Reproducible check:** Supplement: `259 + 263 = 522 ≠ 519`; `44 + 44 = 88 ≠ 91`. Main article: `259 + 260 = 519`; `44 + 47 = 91`. Counts are integers; rounding tolerance `0` participants.
- **Bounded impact:** The documents differ by three levodopa participants in each category; arm totals remain 307. The supplied evidence does not establish which classification is correct.
- **Verification:** 1. Check the randomized stroke-type dataset or final table-production output for the levodopa arm. 2. Confirm `260/47` or document a corrected overall/arm set; either result resolves the cross-document inconsistency.

### 3. Onset-to-randomization timing differs by 4–5 median days

- **Category / severity:** Cross-document inconsistency / Minor.
- **Issue:** Identically described arm-specific onset-to-randomization timing is reported as 3 days in the main article and 7–8 days in the supplement, leaving incompatible descriptive values.
- **Evidence:** **Main article:** DOC-001, `jama_engelter_2025_oi_250066_1761597796.45511.pdf`, PDF p. 4, Table 1, “Time from stroke onset to randomization, median (IQR), d”: levodopa `3.0 (2.0-5.0)`, placebo `3.0 (2.0-5.0)`. **Supplement comparator:** DOC-004, `joi250066supp3_prod_1761597796.4701.pdf`, PDF p. 11, eTable 1, “Median time from stroke onset to randomization [IQR]”: placebo `8 [5,10]`, levodopa `7 [5-11]` (overall `7 [5,10]`).
- **Direct comparison:** Levodopa `7` versus `3.0` days (`+4` days); placebo `8` versus `3.0` days (`+5` days).
- **Reproducible check:** `7 − 3 = 4 days`; `8 − 3 = 5 days`. The difference exceeds any display-precision rounding (main value shown to 0.1 day; supplement to whole days); no rounding tolerance can reconcile 3 with 7 or 8.
- **Bounded impact:** The package contains incompatible timing descriptions; it does not establish the correct value or a change in treatment-effect estimates.
- **Verification:** 1. Check the analysis dataset variable and table shells defining onset-to-randomization. 2. Confirm the median/IQR for each randomized arm and amend the discrepant table if the same population and endpoint are intended.

### 4. PRAI placebo numerator differs by one participant

- **Category / severity:** Cross-document inconsistency / Minor.
- **Issue:** The main article gives 52/270 placebo participants with no or no relevant improvement, whereas the supplement gives 51/270, so the placebo numerator requires confirmation.
- **Evidence:** **Main article:** DOC-001, `jama_engelter_2025_oi_250066_1761597796.45511.pdf`, PDF p. 6, *Secondary Outcomes*: levodopa `51/276 (18%)`; placebo `52/270 (19%)`. **Supplement comparator:** DOC-004, `joi250066supp3_prod_1761597796.4701.pdf`, PDF p. 15, eTable 4, PRAI row: levodopa `51/276 (18.48%)`; placebo `51/270 (18.89%)`.
- **Direct comparison:** Placebo reported numerator `52` versus comparator `51`, a difference of `1 participant`; the associated unrounded rates differ by `0.37 percentage points`.
- **Reproducible check:** `52/270 × 100 = 19.26%`, which rounds to `19%`; `51/270 × 100 = 18.89%`, matching eTable 4. Rounding tolerance: main article reports a whole percentage; it cannot distinguish 19.26% from 18.89%, but the numerator contradiction remains exact.
- **Bounded impact:** One placebo participant and 0.37 percentage points differ; denominators and levodopa values agree.
- **Verification:** 1. Check the PRAI derivation/count for the 270 placebo participants. 2. Confirm whether the numerator is 51 or 52 and align the corresponding reported percentage/table text.

### 5. Estimands 3 and 4 use a population label inconsistent with its definition

- **Category / severity:** Statistical reporting inconsistency / Minor.
- **Issue:** eTable 2 labels Estimands 3 and 4 “Full analysis set,” although that set excludes deaths and these estimands report N=610 including 28 deaths.
- **Evidence:** DOC-004, `joi250066supp3_prod_1761597796.4701.pdf`: PDF p. 12, eTable 2 population definition: participants who died before the 3-month assessment were excluded from the full analysis set; PDF p. 13, eTable 2: Estimand 1, Full analysis set, `N=582`; Estimand 3, Full analysis set, deceased participants’ FMA values imputed, `N=610`; Estimand 4, Full analysis set, death-and-FMA endpoint, `N=610`; PDF p. 16, eTable 5: `28` participant deaths.
- **Direct comparison:** Defined full analysis set `582` versus labelled Estimands 3/4 `610`; discrepancy `+28 participants`, exactly the death count.
- **Reproducible check:** `610 − 28 = 582`, matching Estimand 1; equivalently `582 + 28 = 610`. N is an integer; rounding tolerance `0` participants.
- **Bounded impact:** The labels conflict with the supplied definition. The N values and death-handling text identify the apparent populations; this evidence does not show that numerical estimates are wrong.
- **Verification:** 1. Check the estimand/population definitions and table labels against the analysis output. 2. Confirm whether Estimands 3/4 use an all-randomized/death-inclusive population and relabel or revise the definition accordingly.

### 6. Estimand 11’s written conjunction cannot produce its reported N

- **Category / severity:** Statistical reporting inconsistency / Minor.
- **Issue:** eTable 3 states that Estimand 11 excludes participants with both low rehabilitation and <80% medication, but that intersection-only rule cannot yield the reported N=395.
- **Evidence:** **Written rule and N:** DOC-004, `joi250066supp3_prod_1761597796.4701.pdf`, PDF p. 14, eTable 3, Estimand 11: exclusion of participants with low rehabilitation “and” less than 80% medication, `N=395`. **Comparator counts:** DOC-004, PDF p. 13, eTable 2: excluding low medication alone `N=496`; excluding low rehabilitation alone `N=450`; base full analysis set `N=582`. **Main-text comparator:** DOC-001, `jama_engelter_2025_oi_250066_1761597796.45511.pdf`, PDF p. 4, *Statistical Analyses*: post hoc analysis includes only participants meeting both adherence requirements.
- **Direct comparison:** Intersection-only exclusion must retain at least `496`, while reported N is `395` (`101 fewer`); N=395 instead is compatible with excluding the union of low-adherence sets.
- **Reproducible check:** Low medication `582−496=86`; low rehabilitation `582−450=132`. Their intersection is at most `86`; intersection-only exclusion retains at least `582−86=496`. Reported exclusion is `582−395=187`; union identity gives overlap `86+132−187=31`, a feasible nonnegative count. Counts are integers; rounding tolerance `0` participants.
- **Bounded impact:** The literal supplement rule is not reproducible. The main text and N support an apparent intended rule, but the estimate itself is not shown to be numerically wrong.
- **Verification:** 1. Check the Estimand 11 analysis code/table shell for its actual inclusion rule. 2. Confirm whether inclusion required both adherence criteria (equivalently excluding either failure) and correct the word “and”/rule if so.

### 7. eFigure 7 assigns incompatible PH3 subgroup labels

- **Category / severity:** Presentation inconsistency / Minor.
- **Issue:** eFigure 7’s color key labels do not match its threshold-defined PH3 subgroup labels, preventing confident mapping of plotted series to groups.
- **Evidence:** DOC-004, `joi250066supp3_prod_1761597796.4701.pdf`, PDF p. 27, eFigure 7: green key “moderate-severe impairment”; purple key “very severe impairment”; PH3 legend “severe impairment (<=35 points) vs. mild to moderate impairment (>35 points).”
- **Direct comparison:** Color-key descriptors “moderate-severe” and “very severe” versus threshold groups “severe (<=35)” and “mild to moderate (>35)”; no alternate color-to-threshold mapping is supplied.
- **Logical check:** A figure legend must assign each plotted series to a single stated subgroup. Here the two key labels are neither the two threshold labels nor an explicit mapping to them; no numerical rounding applies.
- **Bounded impact:** The two subgroup estimates cannot be confidently assigned to the stated threshold groups from the figure alone; plotted points and intervals are unchanged.
- **Verification:** 1. Check the figure-generation legend and source labels. 2. Confirm the green/purple assignment for FMA `<=35` and `>35`, then make the color key and threshold legend identical or explicitly mapped.

### 8. eTable 4 mislabels the mRS odds ratio as an FMA mean difference

- **Category / severity:** Presentation inconsistency / Minor.
- **Issue:** eTable 4 places the mRS estimate under an FMA mean-difference header although the matching main-text estimate is an adjusted odds ratio.
- **Evidence:** **Supplement:** DOC-004, `joi250066supp3_prod_1761597796.4701.pdf`, PDF p. 15, eTable 4, effect-column header “Estimated Effect of Levodopa: Mean Difference on FMA, [CI]”; mRS row `0.93 [0.69-1.23]`. **Main-article comparator:** DOC-001, `jama_engelter_2025_oi_250066_1761597796.45511.pdf`, PDF p. 6, *Secondary Outcomes*: adjusted odds ratio `0.93 (95% CI, 0.69-1.23)`.
- **Direct comparison:** Same numeric value/interval `0.93 [0.69–1.23]`; supplement label “mean difference on FMA” versus main-text metric “adjusted odds ratio.”
- **Logical check:** An odds ratio is a ratio measure, not a mean difference measured in FMA points. The matching estimate and CI require no numerical transformation; rounding tolerance is not applicable.
- **Bounded impact:** The supplement can cause the mRS metric to be misread; the main text supplies the correct metric and the numeric estimate agrees.
- **Verification:** 1. Check the eTable 4 column structure/source output for whether headers are outcome-specific. 2. Confirm the mRS effect measure is an adjusted odds ratio and amend the cell/header so it is not presented as an FMA mean difference.

### 9. eFigure 6 contains a conflicting embedded figure number

- **Category / severity:** Presentation inconsistency / Minor.
- **Issue:** The spline plot is headed eFigure 6 but its embedded caption calls it Figure 4, while eFigure 4 identifies a different forest plot, creating cross-reference ambiguity.
- **Evidence:** DOC-004, `joi250066supp3_prod_1761597796.4701.pdf`, PDF p. 26: heading “eFigure 6. Nonlinear association between baseline and three-month FMA (spline model)” and embedded caption “Figure 4: Main estimate including FMAA at baseline as spline: estimated marginal effects.” Comparator: same document, PDF pp. 23–24, eFigure 4, forest plot of FMA estimands at 3 months.
- **Direct comparison:** Identifier `eFigure 6` versus embedded `Figure 4`; PDF pp. 23–24 already assigns eFigure 4 to a separate plot.
- **Logical check:** A supplement figure identifier must identify one figure. Two identifiers are shown for the p. 26 plot and one is already used by another plot; no numerical rounding applies.
- **Bounded impact:** This is figure-numbering/cross-reference ambiguity only; the spline plot remains otherwise identifiable.
- **Verification:** 1. Check the supplement layout source and all figure cross-references. 2. Confirm the p. 26 spline plot’s intended identifier and make the page heading, embedded caption, and references consistent.

## Processing and audit record

| Document ID | Filename | Classification | Scientific processing/audit status |
|---|---|---|---|
| DOC-001 / main_article | `jama_engelter_2025_oi_250066_1761597796.45511.pdf` | Main article | Audited: native extraction/normalization pp. 1–10; visual rendering pp. 4–6. |
| supplement_1_protocol | `joi250066supp1_prod_1761597796.4601.pdf` | Protocol | **Not Audited by Design**: no scientific extraction, rendering, or OCR. |
| supplement_2_sap | `joi250066supp2_prod_1761597796.4701.pdf` | Statistical analysis plan | **Not Audited by Design**: no scientific extraction, rendering, or OCR. |
| DOC-004 / supplement_3_results | `joi250066supp3_prod_1761597796.4701.pdf` | Results supplement | Audited: native extraction/normalization and rendering pp. 10–27; OCR unavailable, with rendered visual evidence retained. |
| supplement_4_administrative | `joi250066supp4_prod_1761597796.4751.pdf` | Administrative supplement | **Not Audited by Design**: no scientific extraction, rendering, or OCR. |
| supplement_5_analysis_code | `joi250066supp5_prod_1761597796.4751.pdf` | Analysis-code supplement | **Not Audited by Design**: no scientific extraction, rendering, or OCR. |
| supplement_6_data_sharing | `joi250066supp6_prod_1761597796.4801.pdf` | Data-sharing statement | **Not Audited by Design**: no scientific extraction, rendering, or OCR. |

## AI Training Restriction Summary

This separate screen records supplied-materials evidence only. It does not determine legal permission.

| Document ID / filename | Status | Exact evidence location and evidence | Human Compliance Review |
|---|---|---|---|
| main_article / `jama_engelter_2025_oi_250066_1761597796.45511.pdf` | Explicit AI Training Restriction | PDF pp. 1–10, page footer (e.g., pp. 1, 10): “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Yes |
| supplement_1_protocol / `joi250066supp1_prod_1761597796.4601.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1, p. 94, and embedded XMP metadata screened; no relevant notice located. | No |
| supplement_2_sap / `joi250066supp2_prod_1761597796.4701.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1, p. 18, and embedded XMP metadata screened; no relevant notice located. | No |
| supplement_3_results / `joi250066supp3_prod_1761597796.4701.pdf` | Explicit AI Training Restriction | PDF pp. 1–27, page footer (e.g., pp. 1, 27): “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Yes |
| supplement_4_administrative / `joi250066supp4_prod_1761597796.4751.pdf` | No AI Training Restriction Located in Provided Materials | PDF pp. 1 and 8 and embedded XMP metadata screened; no relevant notice located. | No |
| supplement_5_analysis_code / `joi250066supp5_prod_1761597796.4751.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1 (complete document) and embedded XMP metadata screened; no relevant notice located. | No |
| supplement_6_data_sharing / `joi250066supp6_prod_1761597796.4801.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1 (complete document) and document metadata (no XMP stream) screened; no relevant notice located. | No |

For every “No AI Training Restriction Located” record, absence of a located statement is not an inference of permission.
