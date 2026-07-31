# Evidence Verification — Eight Supplied Candidates

## Scope and decision summary

- Sources reopened: DOC-001, `jama_parsons_2020_oi_190140.pdf`; DOC-004, `joi190140supp3_prod.pdf`.
- No external sources were used and no new issues were sought.
- Verification rounds: one source-text check and one source-page visual check at most per candidate.
- Decisions: **Accepted (Verified): 5**; **Uncertain: 2**; **Rejected: 1**.

## 1. Energy control 24-month CI contains a double minus

- **Decision:** **Accepted (Verified)**
- **Category / severity:** Presentation inconsistency / Low.
- **Issue statement:** The supplementary eTable prints a nonstandard double minus in the lower 95% CI bound for the control-group 24-month energy change.
- **Source:** DOC-004, `joi190140supp3_prod.pdf`, PDF p. 2, eTable, Energy (kcal/day), Control, 24-month, Mean Change (95% CI): `-130.3 (--195.08, -65.52)`.
- **Comparator:** DOC-001, `jama_parsons_2020_oi_190140.pdf`, PDF p. 7 (printed p. 146), Table 2, Energy, Control Group, 24-Month Change: `−130.3 (−195.08 to −65.52)`.
- **Logical basis:** A CI bound must be a signed numeric value; `--195.08` is not a conventional numeric representation. Removing one minus gives `−195.08`, exactly the bound in the main table.
- **Bounded impact:** One supplementary CI bound is typographically malformed; the intended numeric result remains recoverable from the main table.
- **Verification:** (1) Inspect the DOC-004 p. 2 Energy/control/24-month cell for `--195.08`. (2) Inspect DOC-001 p. 7 for the corresponding single-minus `−195.08`.

## 2. Energy 24-month between-arm P value differs across documents

- **Decision:** **Accepted (Verified)**
- **Category / severity:** Cross-document inconsistency / Moderate.
- **Issue statement:** The same displayed 24-month energy contrast is reported with mutually incompatible P values, `.01` and `<.001`.
- **Source:** DOC-001, PDF p. 7 (printed p. 146), Table 2, Energy, 24-Month Change: intervention `−250.01 (−315.43 to −184.59)`, control `−130.3 (−195.08 to −65.52)`, between-group difference `−119.71 (−211.78 to −27.65)`, `P = .01`; footnote d: “Changes in intervention compared with changes in control.”
- **Comparator:** DOC-004, PDF p. 2, eTable, Energy, 24-month: intervention `−250.01 (−315.43, −184.59)`, control `−130.3 (--195.08, −65.52)`, intervention `p-value† < 0.001`; dagger footnote: “changes in intervention compared to changes in control.”
- **Calculation / logic:** `−250.01 − (−130.30) = −119.71` kcal/day, exactly the Table 2 contrast. A value reported as `.01` to two decimals is not `<.001`; the statements are mutually exclusive under conventional rounding.
- **Bounded impact:** The direction and significance at the .05 level agree, but the stated strength of evidence for this dietary contrast differs.
- **Verification:** (1) Check `.01` in DOC-001 p. 7. (2) Check `<0.001` and the dagger definition in DOC-004 p. 2. (3) Confirm the identical displayed arm changes and subtraction.

## 3. Saturated-fat 12-month between-arm thresholds `<.001` and `<.01`

- **Decision:** **Rejected**
- **Reason:** The source values are confirmed but are logically compatible, not contradictory.
- **Source:** DOC-001, PDF p. 7 (printed p. 146), Table 2, Saturated fat, 12-Month Between-Group Difference: `−1.25 (−1.79 to −0.70)`, `P < .001`.
- **Comparator:** DOC-004, PDF p. 2, eTable, Saturated fat, 12-month: intervention `−1.69 (−2.07, −1.3)`, control `−0.44 (−0.82, −0.06)`, `p-value† < 0.01`.
- **Calculation / logic:** `−1.69 − (−0.44) = −1.25`. Every P value `<.001` is also `<.01`; the supplement merely uses a less precise threshold. No reporting inconsistency is established.
- **Verification:** (1) Confirm both thresholds and the between-arm footnotes. (2) Apply the set relation `p < .001 ⇒ p < .01`.

## 4. eTable follow-up N headers versus article diet-analysis counts

- **Decision:** **Uncertain**
- **Category / severity if resolved as an error:** Cross-document inconsistency / Moderate.
- **Source:** DOC-004, PDF p. 2, eTable headers: intervention `Baseline N=237`, `12-month N=236`, `24-month N=233`; control `Baseline N=241`, `12-month N=240`, `24-month N=238`.
- **Comparator:** DOC-001, PDF p. 5 (printed p. 144), Correlative Outcomes: at 12 months intervention `n=208`, control `n=199`; at 24 months intervention `190`, control `185`. The paragraph identifies these as participants for the Table 2 diet-composition results.
- **Calculation:** Header minus article count: intervention `236−208=28` at 12 months and `233−190=43` at 24 months; control `240−199=41` and `238−185=53`.
- **Why uncertain:** The counts visibly differ, and the eTable does not define what its N headers represent. The article states that linear mixed models can include partially complete records, while DOC-004 gives no analysis-population or available-case definition. Thus the PDFs do not establish that the two sets of N values denote the same population/counting rule.
- **Missing evidence:** A definition or model-output record showing whether each eTable N is the number with observations at that visit, the randomized set, or another mixed-model analysis set.
- **Bounded impact:** The eTable’s sample-size context is ambiguous; no conclusion about the estimates or participant inclusion is supported.
- **Verification:** (1) Confirm all four follow-up header Ns and four article counts. (2) Check an analysis-data/model record for the eTable N definition. Equal definitions would verify an error; distinct documented definitions would reject it.

## 5. Legume control CIs use comma-decimal lower bounds

- **Decision:** **Accepted (Verified)**
- **Category / severity:** Presentation inconsistency / Low.
- **Issue statement:** Two supplementary legume CI cells use a comma as the decimal mark inside a comma-separated CI, creating malformed/ambiguous numeric presentation.
- **Source:** DOC-004, PDF p. 2, eTable, Legumes (servings/day), Control, 12-month and 24-month Mean Change (95% CI): both print `0.03 (-0,03, 0.1)`.
- **Comparator:** DOC-001, PDF p. 7 (printed p. 146), Table 2, Legumes, Control Group, 12- and 24-Month Change: both report `0.03 (−0.03 to 0.1)`.
- **Logical basis:** DOC-004 otherwise uses decimal points and commas as CI endpoint separators. In `-0,03, 0.1`, the first comma is inconsistent with that convention; replacing it with a point produces the exact main-table bound `−0.03`.
- **Bounded impact:** Two supplementary CI bounds are less human- and machine-readable; the main table supplies the intended values.
- **Verification:** (1) Inspect both DOC-004 p. 2 legume/control cells. (2) Compare the corresponding DOC-001 p. 7 cells.

## 6. eFigure total-vegetables panel omits the measurement unit

- **Decision:** **Accepted (Verified)**
- **Category / severity:** Presentation inconsistency / Low.
- **Issue statement:** The eFigure’s Total vegetables panel supplies no unit, while its directly corresponding table labels specify servings per day.
- **Source:** DOC-004, PDF p. 3, eFigure, left panel: title `Total vegetables`, y-axis ticks `0`–`15`, and x-axis labels `Baseline`, `12 m`, `24 m`; neither panel nor caption states a unit.
- **Comparators:** DOC-004, PDF p. 2, eTable row `Total vegetables (servings/day)`; DOC-001, PDF p. 7 (printed p. 146), Table 2 row `Total vegetables, servings/d`.
- **Logical basis:** The same named dietary measure and time points are shown, but the figure omits the tabular measurement unit.
- **Bounded impact:** A reader cannot determine the total-vegetables scale from the figure alone; the unit is recoverable from the tables.
- **Verification:** (1) Inspect the DOC-004 p. 3 left panel, axes, and caption for a unit. (2) Confirm `servings/day` or `servings/d` in the corresponding rows on DOC-004 p. 2 and DOC-001 p. 7.

## 7. Vegetable-juice control 24-month CI excludes zero but P=.15

- **Decision:** **Uncertain**
- **Category / severity if common inference is confirmed:** Statistical reporting inconsistency / Moderate.
- **Source:** DOC-004, PDF p. 2, eTable, Vegetable juice (servings/day), Control, 24-month: mean change `−0.1`, 95% CI `(-0.13, -0.06)`, adjacent `p-value* = 0.15`; asterisk footnote: “within-group changes, values at each follow-up compared to baseline”; P values are based on a mixed-model analysis.
- **Comparison / logic:** The null change is `0 servings/day`. The CI’s upper bound is `−0.06`, so the interval excludes zero, whereas `.15 > .05`. These conflict if the CI and P value are the matched two-sided 95% interval/test for the same model contrast.
- **Why uncertain:** The table states the P-value method but does not state how the CIs were constructed or explicitly say that each CI is the inversion of the same test. Without the model output, a formal incompatibility cannot be established solely from the PDF.
- **Missing evidence:** Model output or a table-method definition confirming that the CI and P value use the same estimand, variance estimate, degrees of freedom, and two-sided test.
- **Bounded impact:** The cell gives apparently conflicting significance cues, but the intended P value or CI cannot be selected from the supplied documents.
- **Verification:** (1) Confirm the cell and asterisk footnote on DOC-004 p. 2. (2) Compare the underlying model interval/test output; matching methods would verify the inconsistency.

## 8. Red-meat 12-month within-arm P values differ across documents

- **Decision:** **Accepted (Verified)**
- **Category / severity:** Cross-document inconsistency / Low.
- **Issue statement:** For identical displayed 12-month red-meat changes and CIs, the main table and supplementary eTable report incompatible within-arm P values in both arms.
- **Source:** DOC-001, PDF p. 7 (printed p. 146), Table 2, Red meat, 12-Month Change: intervention `−11.54 (−19.03 to −4.06)`, `P=.003`; control `−9.83 (−17.26 to −2.41)`, `P<.001`. Footnote c defines within-group follow-up-versus-baseline changes.
- **Comparator:** DOC-004, PDF p. 2, eTable, Red meat, 12-month: intervention `−11.54 (−19.03, −4.06)`, `p-value*=0.001`; control `−9.83 (−17.26, −2.41)`, `p-value*=0.01`. The asterisk footnote gives the same within-group definition.
- **Logical basis:** The point estimates and both CI endpoints match exactly at displayed precision. For control, `<.001` and `.01` are mutually exclusive under conventional reporting; for intervention, `.003` and `.001` are distinct three-decimal values. The shared displayed estimates, CIs, comparison definitions, and mixed-model labeling support a repeated-result comparison.
- **Bounded impact:** All reported P values remain below .05, so direction and binary significance do not change; numerical evidence strength is inconsistently reported.
- **Verification:** (1) Check the two DOC-001 p. 7 red-meat P cells and footnote c. (2) Check the two DOC-004 p. 2 cells and the asterisk footnote. (3) Confirm the duplicated estimates and CI endpoints.
