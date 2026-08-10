# Figure and Participant-Flow Check

## Scope and status

- Main article: `jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf` (DOC-001), Figures 1-4 on PDF pp. 5, 7-9; nearby Results text and the baseline table on PDF pp. 4-6 were used for explicit comparisons.
- Results supplement: `joi250084supp2_prod_1765403089.61751.pdf` (DOC-003), eFigures 3-4 on PDF pp. 34-35; scoped eTable 14 on PDF p. 57 was used for an explicit comparison.
- Source-linked page images were inspected at `.ai_paper_validation/document_outputs/<document_id>/page_images/page-XXX.png`; retained native text was used as a searchable companion, not as a substitute for the images.
- Protocol/SAP/administrative and other out-of-scope pages were not opened. Human authorization is recorded in `.ai_paper_validation/compliance_hold.md`.
- Candidate count: 3 (maximum 10).

## Candidate issues

### FFC-01 - Figure 3 footnote calls BMI values "weight"

- **Category:** Presentation inconsistency
- **Exact location:** DOC-001, `jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf`, PDF p. 8 (journal p. 2086), Figure 3, footnote a. Comparator: the baseline-characteristics table on PDF p. 6 (journal p. 2084), `BMI, median (IQR)` row.
- **Visible/source evidence:** Figure 3 footnote a states, "Baseline median (IQR) weight: 32.2 (28.2-35.9) kg/m2 in the AI-led DPP group and 32.5 (29.3-37.7) kg/m2 in the human-led DPP group." The baseline table labels those same values and units as BMI: AI 32.2 (28.2-35.9) and human 32.5 (29.3-37.7).
- **Logical basis:** kg/m2 is the displayed BMI unit, and the values exactly reproduce the table's BMI row. The footnote therefore labels BMI as "weight" in a figure about percent weight change.
- **Verification instruction:** Inspect Figure 3 footnote a on PDF p. 8 and compare its label, units, and two values with the `BMI, median (IQR)` row on PDF p. 6; confirm whether "weight" should read "BMI."

### FFC-02 - Figure 3 HbA1c panel visually indicates 149/151 participants, whereas cited eTable 14 reports 103/106

- **Category:** Cross-document inconsistency
- **Exact location:** DOC-001, `jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf`, PDF p. 8 (journal p. 2086), Figure 3 panel B, `Change in HbA1c at 12 mo`; comparator DOC-003, `joi250084supp2_prod_1765403089.61751.pdf`, PDF p. 57, eTable 14, `Change in A1C (Baseline to 12 Months)` row. The main Results text on DOC-001 PDF p. 5 explicitly co-cites Figure 3 and eTable 14 for the continuous components.
- **Visible/source evidence:** In Figure 3 panel B, the x-axis/group brackets run from 149 to 1 for Human-led DPP and from 1 to 151 for AI-led DPP, the same visual count labels used in panels A and C. eTable 14 instead reports HbA1c-change N=103 for Human and N=106 for AI, while its weight and physical-activity rows report N=149 and N=151.
- **Logical basis:** The figure visually presents the HbA1c panel as containing 149 human and 151 AI observations (300 total), but the corresponding continuous HbA1c row in the supplement contains 103 and 106 (209 total), a difference of 46 human and 45 AI observations. Neither the Figure 3 caption nor footnote b explains a different HbA1c analysis population from the co-cited table.
- **Verification instruction:** Count or inspect the plotting-data denominator for Figure 3 panel B and confirm whether the endpoint numbers are intended as participant counts. Compare against eTable 14's N=103/106 and determine whether the panel, table, or caption/denominator annotation requires correction.

### FFC-03 - Supplement eFigure 3 changes an absolute 0.2 percentage-point HbA1c threshold to "0.2%"

- **Category:** Cross-document inconsistency
- **Exact location:** DOC-003, `joi250084supp2_prod_1765403089.61751.pdf`, PDF p. 34, eFigure 3, outcome-row label and footnote 3. Comparators: DOC-001, `jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf`, PDF p. 3 (journal p. 2081), `Outcomes`; and PDF p. 7 (journal p. 2085), Figure 2 row and footnote c.
- **Visible/source evidence:** eFigure 3 labels the component `0.2% A1C Reduction`, and footnote 3 repeats `0.2% A1C reduction outcome`. The main article defines the endpoint as "an absolute decrease in HbA1c of at least 0.2 percentage points" (PDF p. 3), while Figure 2 says `Reduction in HbA1c >=0.2 percentage points` and repeats `0.2 percentage points` in footnote c (PDF p. 7). The participant counts are otherwise the same: 35/130 in each group.
- **Logical basis:** A relative 0.2% reduction and an absolute reduction of 0.2 percentage points are not the same notation. The supplement figure's row and footnote conflict with the explicit main-article endpoint definition.
- **Verification instruction:** Compare the eFigure 3 outcome label and footnote 3 on supplement PDF p. 34 with the endpoint definition on main PDF p. 3 and Figure 2 on main PDF p. 7; confirm that the supplement should use "0.2 percentage points" (and retain the threshold sign if intended).

## Rejected observations

1. **Figure 1 participant flow arithmetic - Rejected as an issue.** DOC-001 PDF p. 5: recruitment-source counts sum to 2944; 427 assessed minus 59 excluded equals 368 randomized; allocations are 183+185=368. AI missed-visit reasons reconcile (19 withdrew + 7 lost contact = 26; withdrawal subreasons 11+6+2=19), as do human reasons (19+10=29; 9+8+1+1=19). Restricted exclusions reconcile: AI 26+5+1=32 and 183-32=151; human 29+3+3+1=36 and 185-36=149. These also match 157 and 156 12-month attendees in supplement eTable 9 (DOC-003 PDF p. 51) and total 313 completers in the main Results.
2. **Figure 4 engagement matrix arithmetic - Rejected as an issue.** DOC-001 PDF p. 9: AI rows total 125 and 58, columns total 12, 54, and 117, grand total 183; human rows total 126 and 59, columns total 32, 60, and 93, grand total 185. The displayed percentages agree after rounding (for example, 3/12=25%, 43/117=36.8% -> 37%, 9/59=15.3% -> 15%). Initiation totals also reproduce 171/183=93.4% and 153/185=82.7% from nearby Results text.
3. **Main Figure 2 versus supplement eFigure 3 risk differences - Rejected as an issue.** DOC-001 PDF p. 7 labels unadjusted values such as primary RD -0.2 (-8.2), whereas DOC-003 PDF p. 34 is expressly titled `Adjusted Binary Outcome Differences` and footnote 1 identifies age adjustment, producing -2.0 (-9.8). The different estimates are transparently labeled as different analyses.
4. **eFigure 4 subgroup arithmetic - Rejected as an issue.** DOC-003 PDF p. 35: every subgroup partition returns the arm totals and outcome totals. For example, BMI denominators sum to 55+70+33+25=183 and 47+57+47+34=185; achievers sum to 17+20+11+10=58 and 13+23+16+7=59. Displayed percentages and crude risk differences agree within rounding.

## Uncertain observations

1. **Main-text characterization of the BMI subgroup pattern - Uncertain, not advanced.** DOC-001 PDF p. 6 says the AI-led DPP "appeared less effective ... in lower BMI strata" and better in severe obesity, referring to DOC-003 eFigure 4 on PDF p. 35. The eFigure shows RD +3.2 for overweight, -11.8 for class I obesity, -0.7 for class II, and +19.4 for class III. "Lower BMI strata" may mean performance relative to class III rather than a uniform negative AI-vs-human difference, and the exploratory one-sided CIs do not establish interaction; the wording is too ambiguous for a document-verifiable contradiction.
2. **Figure 3 physical-activity timing label - Uncertain, not advanced.** DOC-001 PDF p. 8 is titled `...Physical Activity at 12 Months`, while panel C says `Weekly physical activity over 12 mo`; the Outcomes section on PDF p. 3 says `mean weekly physical activity at 12 months`. "Over 12 mo" could be a shortened endpoint label rather than an across-month aggregation, and the visible figure alone does not resolve the intended time window.

## Overall disposition

Three candidates are forwarded for evidence verification. No participant-flow count inconsistency was located in the inspected figures.
