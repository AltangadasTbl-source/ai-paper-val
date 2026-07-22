# Table Arithmetic and Internal-Consistency Check

## Scope and evidence reviewed

- DOC-001-main-article: `jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf`, main Table, PDF p. 6 (journal p. 2084).
- DOC-003-results-supplement: `joi250084supp2_prod_1765403089.61751.pdf`, result-relevant eTables on PDF pp. 38-66 only (eTables 2-20d). Pages 36-37 and all protocol material were not audited.
- Source-linked native text was used, with visual confirmation of DOC-001 p. 6 and DOC-003 pp. 47, 55, and 59.

## Candidate issues for verification

### TBL-01 - Arithmetic inconsistency

- **Location:** DOC-003-results-supplement PDF p. 59, eTable 16, *Sensitivity Analysis Imputing Outcomes in Those with Missing 12 Month Outcomes Data Using Multiple Imputation by Chain Equations*.
- **Source values:** AI-based DPP 32.2% achieving the primary outcome (MI-pooled); human-coach-based DPP 31.9%; reported risk difference `-1.1` percentage points (one-sided 95% CI, `-11.5`). The table does not label the risk difference as adjusted.
- **Calculation:** 32.2 - 31.9 = **+0.3 percentage points**, not -1.1 percentage points. The difference between the displayed risk difference and the arithmetic difference is 1.4 percentage points and reverses direction.
- **Reasoning:** Under the displayed, unqualified pooled percentages, the risk difference is internally inconsistent. Rounding to one decimal place cannot account for a 1.4-point, direction-reversing discrepancy.
- **Verification instruction:** Reproduce the MI pooling and the reported risk-difference calculation. If the `-1.1` estimate is adjusted or otherwise uses a different estimand, label it and provide the corresponding adjusted group estimates; otherwise correct the displayed risk difference or percentages.

### TBL-02 - Presentation inconsistency

- **Location:** DOC-001-main-article PDF p. 6 (journal p. 2084), main Table footnote a; compare DOC-003 PDF pp. 39-45.
- **Source values:** The main-table footnote directs readers to “eTable 4 (overall), eTable 6 (by site), and eTable 7 (by baseline hemoglobin A1c status)” for additional characteristics. In the supplement, the matching tables are eTable 3, *Baseline Characteristics of the Randomized Population* (PDF pp. 39-40); eTable 5, *Baseline Characteristics by Site* (pp. 42-43); and eTable 6, *Baseline Characteristics by Baseline A1C Status* (pp. 44-45). eTable 4 is *DPP Eligibility Breakdown* (p. 41), while eTable 7 is *Baseline Characteristics by Trial Completion Status* (pp. 46-47).
- **Logical basis:** Two of the three referenced eTable numbers identify a different table than the stated parenthetical description, and the overall table is cited as eTable 4 rather than eTable 3.
- **Verification instruction:** Check the final supplement numbering and correct main-table footnote a to cite eTable 3 (overall), eTable 5 (by site), and eTable 6 (by baseline A1C status), if those are the intended cross-references.

### TBL-03 - Presentation inconsistency

- **Location:** DOC-003-results-supplement PDF pp. 53-54, eTable 11, *Baseline Characteristics for participants with 12-month outcome data who did not initiate prohibited medications*.
- **Source values:** The age row carries superscript 2. Footnote 1 states: “Age differed between study groups (p = 0.010).” Footnote 2 states: “Age differed between study groups (p = 0.014); all other baseline characteristics were similar (p > 0.05).” The table labels its two columns AI-based DPP (N=151) and human-coach-based DPP (N=149), without explaining that the two P values pertain to different populations or analyses.
- **Logical basis:** The same displayed age comparison is associated with two different P values, 0.010 and 0.014. A difference in analysis population could explain this, but the table provides no such distinction.
- **Verification instruction:** Confirm which P value applies to the eTable 11 restricted population. Retain that value in the table-specific footnote and remove or explicitly identify the other value as a cross-reference to a different population.

## Rejected and uncertain observations

- **Rejected - main Table arithmetic:** DOC-001 PDF p. 6. Site, sex, race, ethnicity, marital-status, education, BMI-classification, and diet-category counts sum to their visible arm denominators (AI 183; human 185); each displayed percentage is compatible with its count and denominator after rounding.
- **Rejected - eTable 2 and eTable 4 totals:** DOC-003 pp. 38 and 41. Human-DPP site allocations sum to 185 (63+60+3+59); randomized eligibility categories sum to 183 and 185, and restricted-population categories sum to 151 and 149. Displayed percentages agree with these denominators at shown precision.
- **Rejected - baseline/completion/restricted subgroup tables:** DOC-003 pp. 39-47 and 53-54, eTables 3 and 5-7 and 11. Checked mutually exclusive demographic, site, BMI, and diet distributions reconcile to their stated table denominators, and cross-table subgroup counts reconcile to the randomized totals where directly comparable.
- **Rejected - missingness and follow-up tables:** DOC-003 pp. 48-52, eTables 8a-10b. Visible counts and percentages agree with N=183 or N=185; 12-month missing counts (26+29=55) reconcile to the reported dropout/lost-to-follow-up count, and medication-participant counts (6+7=13) reconcile to listed instances.
- **Rejected - outcome and sensitivity counts:** DOC-003 pp. 55 and 57-62, eTables 12 and 14-19. eTable 12 cell counts total 58, 59, and 117 by column; eTable 15 and eTables 17-19 raw risk differences agree with their displayed numerators, denominators, and rounded percentages. eTable 14 denominators agree with the restricted population and baseline-prediabetes subset. eTable 16 is excepted as TBL-01.
- **Rejected - adverse-event totals within available scope:** DOC-003 pp. 63-66, eTables 20a-20d. eTable 20a category counts sum to 100 AI and 25 human events, agreeing with eTables 20b-c; eTable 20d visible grade-1 condition counts sum to 13 AI and 5 human events. Grade-2 and later condition detail continues beyond the scoped page and was not totaled.
- **Uncertain - eTable 7 threshold wording:** DOC-003 PDF p. 47, eTable 7 footnote 1 says “No baseline characteristics were statistically significant different between groups (p<0.05).” This is potentially misleading because an absence of significant differences would conventionally be described as all P values >0.05, but the parenthetical can also be read as defining the significance criterion. No candidate is advanced without the underlying P values.
- **Uncertain - repeated age footnotes in eTables 5-7:** DOC-003 PDF pp. 42-47. The repeated footnote 2 reports age P=0.014 even where the table columns are site, baseline-A1C, or completion-status strata. It may be an intentional cross-reference to the randomized arm comparison rather than a result for the visible columns; it is not advanced independently beyond the directly ambiguous eTable 11 instance (TBL-03).

## Result

Three local, document-verifiable candidates are supplied for evidence verification. No source PDFs were modified.
