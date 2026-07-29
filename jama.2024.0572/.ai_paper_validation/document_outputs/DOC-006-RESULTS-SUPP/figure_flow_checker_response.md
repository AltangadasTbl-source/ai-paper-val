# Figure / Flow Consistency Audit — DOC-001-MAIN and DOC-006-RESULTS-SUPP

**Audit status:** Complete  
**Scope:** DOC-001-MAIN PDF pp. 1-14 and DOC-006-RESULTS-SUPP result-relevant figures/flow material, PDF pp. 5-34. No protocol, SAP, administrative document, or external source was inspected.  
**Candidate count:** 4

## Candidate FF-01 — Main text says EVT probabilities increase with mismatch volume, but eFigure 17 shows both outcome curves decreasing

- **Category / severity:** Statistical reporting inconsistency / Moderate
- **Issue statement:** The main article reports increasing probabilities of functional independence and independent ambulation with increasing mismatch volume in EVT patients, while the explicitly cited eFigure 17 displays downward-sloping curves for both outcomes as mismatch volume increases.
- **Reported claim:** DOC-001-MAIN, `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 8, “Association of Mismatch With EVT Treatment Effect and Functional Outcomes,” paragraph continuing across columns: “as mismatch volume increased, the marginal probability of functional independence and independent ambulation increased for patients receiving EVT but decreased in patients receiving medical management only (eFigure 17 in Supplement 5).”
- **Comparator:** DOC-006-RESULTS-SUPP, `joi240006supp5_prod_1708623115.01733.pdf`, PDF p. 23, eFigure 17, panels A and B. The x-axes increase from approximately −100 to 400 mL. In panel A (mRS 0-2), both visible curves decline from left to right; in panel B (mRS 0-3), both visible curves also decline from left to right. Thus, no displayed arm curve increases with mismatch volume.
- **Logical check:** The text's claimed EVT direction requires a positive curve slope as mismatch volume increases. The cited panels show negative slopes for both curves. This conclusion does not depend on assigning the unlabeled colors to treatment arms because neither curve rises.
- **Bounded impact:** The direction of the modeled mismatch-volume association in EVT recipients is unclear; this does not by itself invalidate the categorical mismatch treatment-effect results.
- **Human verification:**
  1. Read the quoted sentence on DOC-001 PDF p. 8.
  2. Inspect eFigure 17 panels A-B on DOC-006 PDF p. 23 and follow each curve from the leftmost to rightmost mismatch-volume value.
  3. Confirm the issue if neither curve rises while the text says the EVT probability increased; resolve it if the published plot axes or curves have a documented contrary interpretation not visible on the page.

## Candidate FF-02 — eFigure 13 reverses the “favours” direction for the adverse mRS 5-6 outcome

- **Category / severity:** Presentation inconsistency / Moderate
- **Issue statement:** eFigure 13 labels relative risks below 1 as favoring medical management even though the plotted outcome is complete dependence or death and the same-outcome eFigure 9 correctly labels values below 1 as favoring thrombectomy.
- **Primary location:** DOC-006-RESULTS-SUPP, PDF p. 19, eFigure 13, forest-plot x-axis. The left side of 1 is labeled “Favours Medical Management” and the right side “Favours Thrombectomy.”
- **Visible evidence:** The outcome in the caption is “complete dependence or death (mRS 5-6).” Example row, NCCT core <70 mL: thrombectomy 27 (39.71%) vs medical management 39 (60.94%), displayed RR 0.68 (0.49-0.95), plotted left of 1. A lower rate of this adverse outcome favors thrombectomy, not medical management.
- **Direct comparator:** DOC-006-RESULTS-SUPP, PDF p. 15, eFigure 9, the same mRS 5-6 outcome. Its x-axis labels the left side “Favours Thrombectomy” and right side “Favours Medical Management.”
- **Logical check:** For an adverse outcome, RR <1 means lower risk in the numerator group (thrombectomy). The displayed percentages also have 39.71% <60.94%. Therefore the eFigure 13 axis annotations are reversed.
- **Bounded impact:** The numeric estimates remain visible, but the direction-of-benefit annotation can invert a reader's interpretation of the forest plot.
- **Human verification:**
  1. Confirm the eFigure 13 outcome and axis annotations on PDF p. 19.
  2. Check the NCCT <70-mL row percentages and RR.
  3. Compare with the same-outcome axis on eFigure 9, PDF p. 15. The issue is confirmed if eFigure 13 retains the opposite favor labels.

## Candidate FF-03 — eFigures 18-19 and the main text disagree on whether prediction panels hold CTP/MRI or composite core volume constant

- **Category / severity:** Cross-document inconsistency / Moderate
- **Issue statement:** The prediction figures inconsistently identify the core-volume covariate as CTP/MRI core versus composite core, while the plotted panel headings say only “Core Volume,” leaving the modeled quantity unresolved.
- **Evidence A:** DOC-006-RESULTS-SUPP, PDF p. 24, eFigure 18 title: “with CTP/MRI core volume set at a) 70ml, b) 100ml and c) 150ml.” The immediately following caption text instead says the relationship is consistent across “composite core volume estimates” and decreases as “composite core volume” increases.
- **Evidence B:** DOC-006-RESULTS-SUPP, PDF p. 25, eFigure 19 title and text specify “composite core volume” at 70, 100, and 150 mL.
- **Evidence C:** DOC-001-MAIN, PDF p. 10, “Association of Age and Time With Functional Outcome After EVT,” after citing both eFigures 18 and 19: “The relationship was consistent across estimated CT perfusion/MRI core volumes set at 70 mL, 100 mL, and 150 mL.”
- **Visible comparator:** The panels on DOC-006 pp. 24-25 are headed only “Core Volume 70,” “Core Volume 100,” and “Core Volume 150,” so the graphs do not resolve the caption conflict.
- **Logical check:** CTP/MRI core and composite core are separately defined quantities in the package; the latter is the larger of CTP/MRI core and CT-hypodensity volume (DOC-006 PDF p. 37, eTable 1 footnote). The labels therefore are not interchangeable.
- **Bounded impact:** A reader cannot determine which imaging estimate underlies the displayed predicted probabilities, particularly for eFigure 19.
- **Human verification:**
  1. Compare the eFigure 18 title with its own explanatory text on PDF p. 24.
  2. Compare the eFigure 19 title on PDF p. 25 with the collective main-text statement on DOC-001 PDF p. 10.
  3. Check the model code/specification. CTP/MRI core would confirm the main/eFigure 18-title label; composite core would confirm the eFigure 19 and eFigure 18-body label.

## Candidate FF-04 — eFigure 6A subgroup labels are displaced from the four bar pairs

- **Category / severity:** Presentation inconsistency / Low
- **Issue statement:** eFigure 6A visibly mispositions the four CTP/MRI-core stratum labels, making the bar-to-stratum mapping ambiguous.
- **Location:** DOC-006-RESULTS-SUPP, PDF p. 12, eFigure 6, panel A.
- **Visible evidence:** Panel A has four paired blue/orange bar groups with values 2%/98%, 6%/94%, 13%/87%, and 28%/73%. The four labels “0-49 ml,” “50-99 ml,” “100-149 ml,” and “150 ml or larger” are not centered beneath the four pairs: the first two labels sit under the first pair, subsequent labels are shifted left, and the final pair has no centered label beneath it.
- **Comparator:** On the same page, panel B displays the same four strata with each label centered beneath its corresponding paired bars.
- **Logical check:** Four strata require a one-to-one mapping to four paired groups. Panel B provides the intended layout; panel A's visible placement does not.
- **Bounded impact:** The percentages are readable, but their core-volume-stratum attribution can be misread without using the caption/trend context.
- **Human verification:**
  1. Inspect the x-axis of eFigure 6A at full page width.
  2. Compare each label position with the center of its paired bars.
  3. Compare to panel B. Confirm if panel A retains the displaced labels in the source PDF.

## Reconciled checks / no candidate

- DOC-006 PDF p. 8, eFigure 3 participant flow closes exactly: 958 − 606 = 352; 352 − 4 − 12 = 336; 168 + 168 = 336; as-treated 170 + 166 = 336, including 2 MM-to-EVT crossovers. The 15 listed screening-exclusion counts sum to 606, and the three imaging-exclusion counts sum to 12.
- Those flow values agree with DOC-001 PDF pp. 1 and 4 and the analysis-set headers on pp. 5, 7, and 9.
- DOC-001 Figures 1-2 and DOC-006 eFigures 7-9/20 were checked for subgroup denominators and displayed mRS percentages. Apparent missing categories in stacked bars are zero-width/zero-count segments; no contradictory count was retained.
- Figure 2 percentage totals of 99%-101% are compatible with whole-percentage rounding.
