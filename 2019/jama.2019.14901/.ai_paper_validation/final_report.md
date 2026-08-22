# Human Adjudication Report

**Human Adjudication Required.** This report contains four critic-accepted findings (0 Major, 4 Minor, 0 Uncertain). It reports only the retained evidence and does not determine the underlying analysis or correction.

## Processing note

Source PDFs were read without modification. Selective visual OCR used `rapidocr-cpu`; no GPU or CUDA provider was available. Native text extraction was available for every scientific-audit page. CPU OCR completed for DOC-001 p. 3 and DOC-003 pp. 2–9; DOC-001 pp. 5–8 had bounded CPU-OCR execution limitations, with native text and retained page images used instead. The cited numerical/table evidence should be checked in the source PDFs during adjudication.

## Scientific issues

### 1. Day-7 respiratory-failure absolute difference conflicts within the main article

- **Category:** Arithmetic inconsistency
- **Severity:** Minor
- **Issue statement:** For postextubation respiratory failure at day 7, the narrative reports an absolute difference of −8.7 percentage points whereas Table 2 reports −8.5 percentage points for the same outcome, and the displayed counts reproduce −8.5 percentage points.
- **Evidence A — reported narrative value:** **DOC-001-main-article**, `jama_thille_2019_oi_190108.pdf`, PDF p. 6 (printed p. 1470), Results—Secondary Outcomes, first paragraph: “21% vs 29%; difference, **−8.7% [95% CI, −15.2% to −1.8%]; P = .01**.”
- **Evidence B — comparator table value:** **DOC-001-main-article**, `jama_thille_2019_oi_190108.pdf`, PDF p. 8 (printed p. 1472), Table 2, Secondary Outcomes, row “Postextubation respiratory failure at day 7”: high-flow nasal oxygen alone **88 (29)**, `n=302`; high-flow nasal oxygen with NIV **70 (21)**, `n=339`; absolute difference **−8.5% (95% CI, −15.2% to −1.8%)**; **P=.01**.
- **Direct comparison:** Reported narrative value = **−8.7 percentage points**; count-consistent Table 2 comparator = **−8.5 percentage points**; discrepancy = **−0.2 percentage point** (the narrative is 0.2 percentage point more negative). The endpoint, time point, confidence interval, and P value match.
- **Reproducible calculation:** Inputs: NIV `70/339`; oxygen alone `88/302`. Formula: `(70/339 − 88/302) × 100`. Result: `20.64897 − 29.13907 = −8.49010` percentage points, which rounds to **−8.5 percentage points** at one decimal place. Rounding tolerance at one decimal place: ±0.05 percentage point; −8.49010 is not compatible with a displayed −8.7 percentage points under that rule.
- **Bounded impact:** The displayed point estimate requires correction or confirmation; the reported counts, direction, confidence interval, P value, and nominal-significance interpretation are unchanged by this comparison.
- **Verification instruction:**
  1. Check the −8.7% value in the Secondary Outcomes sentence on DOC-001 PDF p. 6.
  2. Check the `88/302`, `70/339`, and −8.5% entries in Table 2 on DOC-001 PDF p. 8.
  3. Recalculate `(70/339 − 88/302) × 100`; a result of approximately −8.4901 percentage points confirms the count-consistent −8.5% value. If the source analysis specifies a different estimand for the narrative, that documentation would resolve the discrepancy; otherwise the two displays need standardization.

### 2. Day-7 respiratory-failure P values conflict between the main article and results supplement

- **Category:** Cross-document inconsistency
- **Severity:** Minor
- **Issue statement:** The identical displayed day-7 postextubation-respiratory-failure comparison reports P=.01 in the main article and P=.02 in the results supplement without a label identifying different tests, leaving the exact reported P value and test implementation to be confirmed.
- **Evidence A — reported main-article value:** **DOC-001-main-article**, `jama_thille_2019_oi_190108.pdf`, PDF p. 8 (printed p. 1472), Table 2, Secondary Outcomes, row “Postextubation respiratory failure at day 7”: **88 (29)** of 302 versus **70 (21)** of 339; absolute difference **−8.5% (95% CI, −15.2% to −1.8%)**; **P=.01**. Same document, PDF p. 6 (printed p. 1470), Results—Secondary Outcomes, first paragraph, also reports **P=.01**.
- **Evidence B — comparator supplement value:** **DOC-003-results-supplement**, `joi190108supp2_prod.pdf`, PDF p. 2, eTable 1, first row “Post-extubation respiratory failure at day 7, No. (%)”: **88 (29)** of 302 versus **70 (21)** of 339; **P=.02**.
- **Evidence C — stated test:** **DOC-001-main-article**, `jama_thille_2019_oi_190108.pdf`, PDF p. 4 (printed p. 1468), Statistical Analysis: χ² test specified.
- **Direct comparison:** Reported P in the main article = **.01**; comparator P in eTable 1 = **.02**; discrepancy = `.02 − .01 = .01` (supplement higher). The endpoint, time point, arms, denominators, counts, and rounded percentages are identical across the two displays.
- **Reproducible calculation / logical chain:** Inputs: oxygen alone `88/302`, NIV `70/339`; reported test label: χ². Rule: identical displayed comparison values require the same P value unless separately labelled tests or implementations are documented. Reported numerical discrepancy: `.02 − .01 = .01`. From the displayed 2×2 counts, uncorrected Pearson χ² gives `P≈.012786` (display `.01`), while continuity-corrected calculation gives `P≈.016490` (display `.02`). These are possible explanations only; the cited records do not identify the intended unlabelled implementation. Rounding to two decimals is consistent with each displayed value.
- **Bounded impact:** The exact P value and intended χ² implementation need correction or confirmation. Both reported P values are below .05; this comparison does not change the nominal-significance conclusion.
- **Verification instruction:**
  1. Check the endpoint, denominators, counts, and P=.01 in DOC-001 Table 2 (PDF p. 8) and the same values with P=.02 in DOC-003 eTable 1 (PDF p. 2).
  2. Check the χ²-test statement in DOC-001 Statistical Analysis (PDF p. 4).
  3. Check the prespecified analysis settings or production output for continuity correction and the exact P value. A documented, separately labelled test for each table resolves the issue; otherwise standardize the P value to the prespecified analysis.

### 3. Nonhypercapnic subgroup P value is not consistently rounded

- **Category:** Statistical reporting inconsistency
- **Severity:** Minor
- **Issue statement:** For day-7 reintubation in the nonhypercapnic subgroup, the main narrative reports P=.10 whereas eTable 4 reports P=.1057 for the same displayed comparison, which rounds to .11 rather than .10 at ordinary two-decimal nearest rounding.
- **Evidence A — reported narrative value:** **DOC-001-main-article**, `jama_thille_2019_oi_190108.pdf`, PDF p. 7 (printed p. 1471), Results—Subgroup Analysis and Additional Analyses, first paragraph: among **530** patients with PaCO2 ≤45 mm Hg, reintubation at day 7 was “13% with noninvasive ventilation vs 18% with high-flow nasal oxygen alone; difference, **−5.0% [95% CI, −11.2% to 1.1%]; P=.10**.”
- **Evidence B — comparator eTable value:** **DOC-003-results-supplement**, `joi190108supp2_prod.pdf`, PDF p. 7, eTable 4, Primary outcome row “Reintubation at day 7, No. (%)”: oxygen alone **45 (18)** of 254; oxygen with NIV **35 (13)** of 276; difference **−5.0% (95% CI, −11.2% to 1.1%)**; **P=.1057**.
- **Direct comparison:** Reported narrative P = **.10**; comparator exact eTable P = **.1057**. The subgroup total reconciles: `254 + 276 = 530`; the subgroup, endpoint, time point, percentages, difference, and confidence interval match. At two-decimal nearest rounding, `.1057` rounds to **.11**, not **.10**.
- **Reproducible calculation:** Inputs: exact P `.1057`; display precision: two decimal places. Rule: ordinary nearest-hundredth rounding. Calculation: `.1057 → .11`; values in `[.0950, .104999…]` round to `.10`, whereas `.1057` lies in the `.11` interval. The reported verification calculation from displayed `45/254` and `35/276` 2×2 counts is uncorrected Pearson χ² `P≈.1057337`, reproducing eTable 4 to four decimals. Rounding tolerance considered: half of 0.01, i.e., ±.005 around a two-decimal displayed value.
- **Bounded impact:** Numerical consistency and reproducibility require correction or confirmation. Both reported P values exceed .05 and the reported confidence interval crosses zero; this comparison does not change the reported nonsignificant conclusion.
- **Verification instruction:**
  1. Check the subgroup, endpoint, effect, confidence interval, and P=.10 in DOC-001 Results—Subgroup Analysis and Additional Analyses (PDF p. 7).
  2. Check the same comparison and P=.1057 in DOC-003 eTable 4 (PDF p. 7).
  3. Check the statistical output and intended formatting rule. An exact P near .1057 confirms ordinary two-decimal nearest rounding to .11; a separately specified analysis or formatting convention yielding .10 resolves the issue.

### 4. Supplementary survival figure gives incompatible time origins

- **Category:** Presentation inconsistency
- **Severity:** Minor
- **Issue statement:** The supplementary eFigure caption describes survival from extubation while its x-axis is labelled days since intubation, giving incompatible time origins on the same figure and making the time origin require confirmation.
- **Evidence A — caption:** **DOC-003-results-supplement**, `joi190108supp2_prod.pdf`, PDF p. 9, eFigure caption: “Kaplan-Meier Curves of the Cumulative Probability of Survival **From Extubation to Day 90**.”
- **Evidence B — comparator axis label:** **DOC-003-results-supplement**, `joi190108supp2_prod.pdf`, PDF p. 9, eFigure plot x-axis: “**Days Since Intubation**.”
- **Direct comparison:** Reported caption time origin = **extubation**; comparator axis time origin = **intubation**. Direction/size discrepancy: the time origins are different labels; no numerical offset or transformation reconciling them is reported in the cited figure.
- **Reproducible logical chain:** Inputs: the quoted caption and x-axis label. Rule: a single time-to-event plot must identify one time origin, or explicitly define a transformation linking different labels. Result: the figure names extubation in the caption and intubation on the axis, with no cited reconciliation; time origin is therefore ambiguous from the figure itself. Rounding tolerance: not applicable.
- **Bounded impact:** The figure’s time-origin label or caption needs correction or confirmation. This card does not alter the displayed curves, at-risk counts, or log-rank P value.
- **Verification instruction:**
  1. Check that the caption on DOC-003 PDF p. 9 says “From Extubation to Day 90.”
  2. Check that the x-axis on the same figure says “Days Since Intubation.”
  3. Check the programmed survival-time variable or figure source. If day 0 is extubation, the x-axis should be corrected; if day 0 is intubation, the caption and related wording should be corrected.

## AI Training Restriction Summary

This separate screen records supplied-document language only; it is not a legal opinion and is not part of the scientific issue list. Institutional permission for AI training was assumed granted for this workflow.

| Document ID | Source file | Status | Exact evidence location and excerpt | Human Compliance Review |
|---|---|---|---|---|
| DOC-001-main-article | `jama_thille_2019_oi_190108.pdf` | Conditional / Permission Required | PDF p. 1, title-page footer (identical footer repeated PDF pp. 2–11): “© 2019 American Medical Association. All rights reserved.” Embedded PDF/XMP metadata: no AI-use, license, permission, terms, or text-and-data-mining statement located. | No — institutional permission assumed granted; without that stated approval, review would be required because rights are reserved. |
| DOC-002-protocol | `joi190108supp1_prod.pdf` | Conditional / Permission Required | PDF p. 2: “CONFIDENTIAL THIS DOCUMENT IS THE PROPERTY OF Poitiers UH. NO INFORMATION PUBLISHED IN THIS DOCUMENT MAY NOT BE DISCLOSED WITHOUT THE PRIOR WRITTEN PERMISSION OF Poitiers UH.” PDF p. 39, section 10, *Confidentiality and Property Rights*: “The investigator and any person under his authority agree to undertake to keep confidential and not to disclose the information to a third party without the prior written approval of the sponsor.” Embedded metadata: no AI-use or rights terms located. | No — institutional permission assumed granted for this task. |
| DOC-003-results-supplement | `joi190108supp2_prod.pdf` | No AI Training Restriction Located in Provided Materials | PDF pp. 1–3 footer: “© 2019 American Medical Association. All rights reserved.” Remaining pages and embedded PDF/XMP metadata: no AI-use, training, license, or rights-and-permissions terms of that type located. | No — institutional permission assumed granted for this task. |
| DOC-004-data-sharing-statement | `joi190108supp3_prod.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1, Data section: “Data available: No.” Complete page and embedded metadata: no copyright, license, rights-and-permissions, AI-use, or training terms located. | No — institutional permission assumed granted for this task. |

Silence in the supplied materials is not treated as permission. The DOC-001 general rights notice and DOC-002 confidentiality/disclosure language are recorded as supplied rights/permission conditions, not as express AI-training restrictions.
