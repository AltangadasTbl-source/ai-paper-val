# Statistical consistency check — DOC-001 and DOC-004

## Scope and method

- **Sources:** DOC-001-main-article (`jama_saynorea_2019_oi_190106_1635377898.43062.pdf`), audited PDF pp. 1–11; and DOC-004-supplement-3-results (`joi190106supp3_prod_1635377898.49725.pdf`), audited PDF pp. 1–27.
- **Evidence maps used:** `DOC-001-main-article/main_text_extraction.md` and `DOC-004-supplement-3-results/results_supplement_evidence_map.md`.
- **Extraction:** native text was adequate for all cited values. The source renders retained for DOC-004 pp. 3 and 7 were visually checked; no additional OCR was required. The package selector records CPU-only OCR (`rapidocr-cpu`), not CUDA.
- **Checks applied:** estimate within reported CI; CI/null/P coherence where the row reports a single fitted comparison; median/IQR ordering; and treatment-column labels. No CI-symmetry inference was used.

## Candidates for verification (4)

### SC-01 — 12-month alcohol CI includes the null while the row reports P=.01

- **Category / severity:** Statistical reporting inconsistency / Moderate.
- **Locations:** DOC-001-main-article, source PDF p. 7 (journal p. 1492), Table 3, `Total Alcohol, %/d`, `12-mo change`, `Between-Group Difference (95% CI)` and `P Value`; model footnote b on the same table. The article says all statistical tests were two-sided on source PDF p. 4, *Statistical Analysis*.
- **Reported values:** intervention change `−0.3 (3.0)` %/d; control `−0.1 (3.0)` %/d; between-group difference `−0.2 (−0.4 to 0.1)` %/d; `P=.01`.
- **Direct comparison and rule:** the displayed 95% CI contains the null difference 0 (`−0.4 <= 0 <= 0.1`), whereas a two-sided P=.01 is below .05 and ordinarily corresponds to a 95% CI that excludes 0 for the same model/contrast. Table 3 identifies its between-group CIs as mixed-effect-model estimates and gives the P value in the same result row.
- **Rounding tolerance:** all three displayed CI values are to one decimal. Under ordinary nearest-tenth rounding, an upper endpoint printed as `0.1` lies roughly from +0.05 to +0.15, so it remains positive; rounding cannot make this printed CI exclude 0. This assessment does **not** assume symmetric CIs.
- **Bounded impact:** the 12-month between-group alcohol result is reported as statistically significant despite a displayed CI compatible with no difference; no primary-outcome result depends on this row.
- **Human verification:** (1) rerun/retrieve the exact 12-month alcohol mixed-model contrast; (2) verify whether the CI and P value came from the same model, imputation rule, and contrast; (3) correct whichever of CI/P/model labels is inconsistent. The issue resolves if the reported CI excludes 0 or if the reported P is at least .05 / explicitly shown to come from a different analysis.

### SC-02 — Reported intervention red-wine median lies above its stated upper IQR bound

- **Category / severity:** Statistical reporting inconsistency / Moderate.
- **Location:** DOC-004-supplement-3-results, source PDF p. 7, Supplemental eTable 2 (continuation), `Red wine (g/week)`, `Baseline, median (IQR)`, intervention group (`N=3,272`). The eTable footnote on that page defines baseline data as `median (IQR)`.
- **Reported values:** intervention `33 (0, 29)` g/week; control `4 (0, 29)` g/week.
- **Calculation / rule:** an IQR displayed as `(Q1, Q3)` must satisfy `Q1 <= median <= Q3`. Here `0 <= 33 <= 29` is false: the stated median exceeds Q3 by `33 − 29 = 4 g/week`.
- **Rounding tolerance:** values are whole g/week. Even allowing ±0.5 g/week rounding on each displayed value, the smallest possible median-minus-Q3 gap is `32.5 − 29.5 = 3.0 g/week`; the ordering cannot be reconciled by rounding.
- **Bounded impact:** this invalidates the intervention baseline descriptive summary for red wine; it does not by itself determine which value is wrong or invalidate the reported 6-/12-month change contrasts.
- **Human verification:** (1) check the source table/export for the intervention baseline red-wine median and quartiles; (2) compare against the original analysis dataset or table-generation output; (3) amend the mistaken statistic. The issue resolves only if a source value is different from one of `33`, `0`, or `29`, or the parenthetical is shown not to be an IQR.

### SC-03 — The second treatment column of eTable 2 is labelled “Intervention group” although its N and later continuation identify it as control

- **Category / severity:** Presentation inconsistency (treatment/subgroup label) / Moderate.
- **Locations:** DOC-004-supplement-3-results, source PDF p. 3, Supplemental eTable 2 header: first column `Intervention group, N=3,272`; second column also `Intervention group, N=3,311`. Source PDF p. 7, the continuation uses the same Ns but labels the second column `Control group`. DOC-001-main-article, source PDF p. 4, Table 1, identifies the analyzed treatment Ns as intervention `n=3,272` and control `n=3,311`.
- **Direct comparison / reasoning:** the PDF-p. 3 second column label conflicts with both the PDF-p. 7 continuation and the main article's group N. It is also directionally corroborated by the p. 3 olive-oil 12-month row: first-column change `36`, second-column change `44`, reported difference `−8`, i.e., `36 − 44 = −8`, consistent with intervention minus control rather than two intervention columns.
- **Rounding tolerance:** none; this is an exact textual-label conflict.
- **Bounded impact:** on p. 3, readers can misattribute the second column's baseline and change values (and thus the sign/meaning of contrasts) to the wrong treatment group. The p. 7 continuation itself supplies the apparent intended label.
- **Human verification:** (1) inspect the author table source/typesetting for p. 3; (2) confirm the N=3,311 column is the control arm; (3) replace the duplicate header. The candidate resolves if the page-3 header is corrected or a documented analysis population establishes two intervention columns, which would also require reconciling the main article and p. 7 labels.

### SC-04 — eTable 4 calls a two-bound baseline summary “mean (SD)” while the table footnote calls baseline values median (IQR)

- **Category / severity:** Presentation inconsistency (summary-statistic label) / Minor.
- **Locations:** DOC-004-supplement-3-results, source PDF p. 10, Supplemental eTable 4, `Total olive oil (g/week)`, baseline intervention and control cells labelled `Baseline, mean (SD)` and printed as `350 (175, 350)` for each arm. Source PDF p. 11, eTable 4 footnote: `Baseline data are median (IQR)`.
- **Direct comparison / rule:** `350 (175, 350)` has a central value plus two parenthetical bounds and is compatible with a median and IQR, but not a mean with a single SD. The detailed p. 10 row label conflicts with the eTable 4 footnote. As a within-package comparator, eTable 2 (PDF p. 3) labels the same-form olive-oil values `Baseline, median (IQR)`.
- **Rounding tolerance:** none; this is a label/format conflict, not an inference from distributional shape.
- **Bounded impact:** affects interpretation of the baseline olive-oil descriptive statistic in the completer sensitivity table, not its reported change CIs or P values.
- **Human verification:** (1) check the descriptive-statistics code and the eTable 4 source; (2) determine whether the baseline row is median (IQR) or mean (SD); (3) align the row and footnote. The candidate resolves if the table source establishes a single summary convention and its label is corrected.

## Checks not advanced

- eTable 3's asterisked er-MedDiet row has a separate, explicitly printed sample-size footnote on PDF p. 10. It is not treated as a contradiction with the table header without evidence that the footnote was intended to apply to all outcomes.
- eFigure 2 has continuous-change directions that differ from some plotted compliance percentages, but the figure omits its thresholds/denominators and uses a potentially different analysis set. This remains **uncertain**, not a reportable candidate.
- No CI-symmetry, visual-pixel, protocol, or SAP comparisons were used.
