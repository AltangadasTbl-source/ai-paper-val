# Human Adjudication Report

## Audit scope and processing record

This report contains the five findings retained by the critic after evidence verification; the two **Uncertain** candidates and one **Rejected** candidate are not scientific issues in this report. No external sources were used. Scientific audit scope was DOC-001 (main article, PDF pages 1–9) and DOC-004 (results supplement, PDF pages 1–3). DOC-002 (protocol), DOC-003 (statistical analysis plan), and DOC-005 (administrative data-sharing statement) were **Not Audited by Design** for scientific findings.

Native PDF text was extracted first from all 12 audited pages. The validated OCR configuration was `rapidocr-cpu` (CPU execution; no CUDA); native text was sufficient for extraction, so further OCR was not required for extraction completion. Source PDFs were not modified.

## Scientific issues for adjudication

### 1. Double minus in the 24-month energy confidence interval

- **Issue statement:** The results supplement prints a double minus in the lower 95% CI bound for the control-group 24-month energy change, making that endpoint nonstandard and potentially ambiguous.
- **Category / severity:** Presentation inconsistency / Minor.
- **Evidence A — reported value:** DOC-004, `joi190140supp3_prod.pdf`, PDF p. 2, eTable, row **Energy (kcal/day)**, **Control**, **24-month**, Mean Change (95% CI): `-130.3 (--195.08, -65.52)`.
- **Evidence B — comparator:** DOC-001, `jama_parsons_2020_oi_190140.pdf`, PDF p. 7 (printed p. 146), Table 2, row **Energy**, **Control Group**, **24-Month Change**: `−130.3 (−195.08 to −65.52)`.
- **Direct comparison:** Reported lower bound `--195.08`; comparator/expected displayed bound `−195.08`; discrepancy is one extra minus sign before `195.08` (no unit change; energy is kcal/day).
- **Calculation or rule:** Input `--195.08`. Rule: a signed decimal CI endpoint conventionally has at most one leading minus. Removing the duplicated minus gives `−195.08`, which exactly equals Evidence B. No numerical rounding is involved.
- **Bounded impact:** The supplementary lower CI endpoint needs typographic correction or confirmation; the intended endpoint is recoverable from Table 2.
- **Verification instruction:** 1. Inspect the DOC-004 cell for `--195.08`. 2. Inspect the matched DOC-001 cell for `−195.08`. The issue is confirmed if the remaining point estimate and both other displayed CI components agree and only the extra minus differs.

### 2. Different 24-month between-arm energy P values

- **Issue statement:** The main article and results supplement attach `.01` and `<0.001`, respectively, to the same displayed 24-month between-arm energy contrast, so the reported strength of evidence is inconsistent.
- **Category / severity:** Cross-document inconsistency / Minor.
- **Evidence A — reported value:** DOC-001, `jama_parsons_2020_oi_190140.pdf`, PDF p. 7 (printed p. 146), Table 2, row **Energy**, **24-Month Change**: intervention `−250.01 (−315.43 to −184.59)`, control `−130.3 (−195.08 to −65.52)`, between-group difference `−119.71 (−211.78 to −27.65)`, `P = .01`; footnote d: `Changes in intervention compared with changes in control.`
- **Evidence B — comparator:** DOC-004, `joi190140supp3_prod.pdf`, PDF p. 2, eTable, row **Energy (kcal/day)**, **24-month**: intervention `−250.01 (−315.43, −184.59)`, control `−130.3 (--195.08, −65.52)`, between-arm `p-value† < 0.001`; dagger footnote: `changes in intervention compared to changes in control.`
- **Direct comparison:** Reported P value `.01`; comparator P value `<0.001`; discrepancy: Evidence A reports 0.01 at two decimal places, whereas Evidence B places the P value below 0.001. The arm estimates, CIs, time point, and comparison definitions match.
- **Calculation or rule:** Inputs: `−250.01 kcal/day` and `−130.30 kcal/day`. Formula: intervention minus control = `−250.01 − (−130.30) = −119.71 kcal/day`, matching Table 2. Rule: a value reported as `.01` at two decimals cannot also be `<.001` under conventional rounding; rounding tolerance is ±0.005 for `.01`, which does not overlap values below `.001`.
- **Bounded impact:** The P value for this reported contrast needs correction or confirmation. Both displayed P values are below .05 and the displayed contrast remains negative; this card does not determine which P value is correct.
- **Verification instruction:** 1. Confirm the DOC-001 P cell `.01`, arm values, and footnote d. 2. Confirm the DOC-004 `<0.001`, arm values, and dagger footnote. 3. Recalculate `−250.01 − (−130.30)`. The issue is confirmed if the comparison is the same in both documents and the P-value strings remain as reported.

### 3. Comma-decimal lower bounds in two legume confidence intervals

- **Issue statement:** Two control-group legume CI cells in the results supplement use a comma as the decimal mark inside a comma-separated interval, making the lower endpoints malformed or ambiguous.
- **Category / severity:** Presentation inconsistency / Minor.
- **Evidence A — reported values:** DOC-004, `joi190140supp3_prod.pdf`, PDF p. 2, eTable, row **Legumes (servings/day)**, **Control**, **12-month** Mean Change (95% CI): `0.03 (-0,03, 0.1)`; same row and group, **24-month**: `0.03 (-0,03, 0.1)`.
- **Evidence B — comparator values:** DOC-001, `jama_parsons_2020_oi_190140.pdf`, PDF p. 7 (printed p. 146), Table 2, row **Legumes**, **Control Group**, **12-Month Change**: `0.03 (−0.03 to 0.1)`; **24-Month Change**: `0.03 (−0.03 to 0.1)`.
- **Direct comparison:** Reported lower endpoint in each supplementary cell `-0,03`; comparator `−0.03`; discrepancy: decimal comma replaces the decimal point in both lower endpoints (servings/day).
- **Calculation or rule:** Inputs: strings `-0,03, 0.1` and `−0.03 to 0.1`. Rule: DOC-004 otherwise uses decimal points within values and commas between CI endpoints. Substituting a point for the first comma produces `−0.03`, exactly matching both Table 2 values. No numerical rounding is involved.
- **Bounded impact:** The two supplementary lower CI endpoints need punctuation correction or confirmation; the intended values are recoverable from Table 2.
- **Verification instruction:** 1. Inspect both DOC-004 legume/control cells. 2. Inspect the matching DOC-001 12- and 24-month cells. The issue is confirmed if the point estimates and upper endpoints match and only the lower-bound punctuation differs.

### 4. Unit omitted from the total-vegetables eFigure panel

- **Issue statement:** The Total vegetables panel in the eFigure lacks a measurement unit although the corresponding tables identify the outcome as servings per day, preventing the panel from independently stating its scale.
- **Category / severity:** Presentation inconsistency / Minor.
- **Evidence A — reported figure content:** DOC-004, `joi190140supp3_prod.pdf`, PDF p. 3, eFigure, left panel: title `Total vegetables`; y-axis ticks `0` through `15`; x-axis labels `Baseline`, `12 m`, `24 m`. Neither the panel axis nor the figure caption states a unit.
- **Evidence B — table comparators:** DOC-004, `joi190140supp3_prod.pdf`, PDF p. 2, eTable, row label `Total vegetables (servings/day)`; DOC-001, `jama_parsons_2020_oi_190140.pdf`, PDF p. 7 (printed p. 146), Table 2, row label `Total vegetables, servings/d`.
- **Direct comparison:** The figure reports the outcome as `Total vegetables` without a unit; both table comparators report the same outcome in `servings/day` (or `servings/d`). The omitted element is the unit, not a numerical value.
- **Calculation or rule:** Inputs: identical outcome label and shared time points (baseline, 12 months, 24 months) in the eFigure/eTable context. Rule: for independent interpretation of an outcome scale, the panel must state its measurement unit or explicitly incorporate it in its axis/caption. No numerical calculation or rounding applies.
- **Bounded impact:** The eFigure panel’s unit needs confirmation or addition; the unit is available in the linked tables. This does not establish that the plotted numerical values are incorrect.
- **Verification instruction:** 1. Inspect the DOC-004 p. 3 left panel, axes, and caption for a unit. 2. Confirm the cited eTable and Table 2 row labels. The issue is confirmed if no unit appears in the panel/caption and both tables specify servings per day.

### 5. Different 12-month within-arm red-meat P values

- **Issue statement:** For identical displayed 12-month red-meat changes and CIs, the main article and results supplement report different within-arm P values for both arms, creating inconsistent numerical evidence statements.
- **Category / severity:** Cross-document inconsistency / Minor.
- **Evidence A — reported values:** DOC-001, `jama_parsons_2020_oi_190140.pdf`, PDF p. 7 (printed p. 146), Table 2, row **Red meat**, **12-Month Change**: intervention `−11.54 (−19.03 to −4.06)`, `P=.003`; control `−9.83 (−17.26 to −2.41)`, `P<.001`. Footnote c defines the within-group comparison as follow-up versus baseline.
- **Evidence B — comparator values:** DOC-004, `joi190140supp3_prod.pdf`, PDF p. 2, eTable, row **Red meat**, **12-month**: intervention `−11.54 (−19.03, −4.06)`, `p-value*=0.001`; control `−9.83 (−17.26, −2.41)`, `p-value*=0.01`. Asterisk footnote: `within-group changes, values at each follow-up compared to baseline`.
- **Direct comparison:** Intervention reported/comparator P values `.003` versus `.001` (difference `0.002` at displayed precision). Control P values `<.001` versus `.01`; the former is below `.001`, while the latter is reported as `.01`. Point estimates, CI endpoints, time point, and within-arm comparison definitions match.
- **Calculation or rule:** Inputs: the paired P strings and matching estimate/CI strings above. Rule: `.003` and `.001` are distinct values at three-decimal precision; `.01` is incompatible with `<.001` under conventional rounding (tolerance for `.01`: ±0.005, nonoverlapping with values <.001). No recomputation of a model P value is possible from supplied materials.
- **Bounded impact:** The four reported P-value statements for the two 12-month within-arm red-meat comparisons need correction or confirmation. All are displayed below .05; this card does not identify which document contains the correct values.
- **Verification instruction:** 1. Confirm the two DOC-001 P cells and footnote c. 2. Confirm the two DOC-004 P cells and asterisk footnote. 3. Confirm that each arm’s point estimate and CI endpoints match across documents. The issue is confirmed if those comparisons are the same and the P-value strings remain different.

## AI Training Restriction Summary

This screen is separate from the scientific issue list. It records only language located in the supplied PDFs and metadata; it is not a legal opinion. Institutional AI-training permission was assumed for this workflow.

| Document ID and filename | Status | Exact evidence location and excerpt | Human Compliance Review |
|---|---|---|---|
| DOC-001 — `jama_parsons_2020_oi_190140.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1 (printed p. 140; notice repeated on remaining pages): `© 2020 American Medical Association. All rights reserved.` Embedded metadata: no copyright, license, rights-and-permissions, terms, text-and-data-mining, AI, training, fine-tuning, or model-improvement condition located. | No |
| DOC-002 — `joi190140supp1_prod.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1 (protocol update cover), PDF p. 60 (end matter/model consent-form addendum), and embedded XMP metadata: no copyright, license, rights-and-permissions, terms, text-and-data-mining, AI, or model-use statement located. | No |
| DOC-003 — `joi190140supp2_prod.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1 (Statistical Analysis Plan title), PDF p. 11 (references/end matter), and embedded XMP metadata: no copyright, license, rights-and-permissions, terms, text-and-data-mining, AI, or model-use statement located. | No |
| DOC-004 — `joi190140supp3_prod.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1 (Supplementary Online Content title; repeated on pp. 2–3): `© 2019 American Medical Association. All rights reserved.` PDF information dictionary: no rights, license, or AI-use field; no embedded XMP metadata stream. | No |
| DOC-005 — `joi190140supp4_prod.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1 (Data Sharing Statement) and PDF information dictionary/metadata location: no copyright, license, rights-and-permissions, terms, text-and-data-mining, AI, or model-use statement located. The data-access language (`Researchers whose proposed use of the data has been approved`; `For a specified purpose`; `With a signed data access agreement`) concerns deidentified participant data, not AI training of this PDF. | No |
