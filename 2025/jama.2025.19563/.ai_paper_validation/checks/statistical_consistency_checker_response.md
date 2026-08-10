# Statistical Consistency Check: DOC-001 and DOC-003

## Scope and evidence

- Main article: `jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf` (DOC-001), PDF pp. 1-11.
- Results supplement: `joi250084supp2_prod_1765403089.61751.pdf` (DOC-003), PDF pp. 34-35 and 38-66 only.
- Evidence used: package and preprocessing manifests, main-text evidence map, results-supplement evidence map, retained native text, and retained page images. The protocol and all out-of-scope supplement pages were not opened.
- Human authorization to resume processing is recorded in `.ai_paper_validation/compliance_hold.md`.
- This check uses only document-grounded arithmetic and logical relationships. It does not infer CI symmetry or other model-dependent properties.

## Local candidate issues

### Candidate SC-01 - Incorrect percentage for 10 of 59 participants

- Category: `Arithmetic inconsistency`
- Location: DOC-003, PDF p. 55, eTable 12, second outcome-pattern row (check marks for >=5% weight loss and >=4% weight loss plus >=150 min/week physical activity), Human-led DPP column.
- Source values: the cell reports `10 (19%)`; the column denominator is `Human-led DPP N = 59`. The table footnote states that percentages use participants who achieved the composite outcome within each group.
- Basis: `10 / 59 x 100 = 16.949%`, which rounds to `17%`, not `19%`. The first row in the same column correctly reports the same numerator and denominator as `10 (17%)`.
- Verification instruction: visually inspect DOC-003 p. 55, confirm the second-row cell is 10 (19%) and the column denominator is 59, then recompute 10/59.

### Candidate SC-02 - HbA1c-change display and table use different analysis-set sizes without an explanation

- Category: `Cross-document inconsistency`
- Locations: DOC-001, PDF p. 8, Figure 3B (`Change in HbA1c at 12 mo`); DOC-001, PDF p. 3, `Outcomes`; DOC-003, PDF p. 57, eTable 14, `Change in A1C (Baseline to 12 Months)`.
- Source values/statements: Figure 3B displays the Human-led and AI-led ranked participant sequences with endpoints `149` and `151`, the same complete-data/no-prohibited-medication group sizes used in panels A and C. The main article states that the HbA1c-change endpoint applies only to participants with baseline HbA1c 5.7%-6.4%. eTable 14 reports the HbA1c-change row with `N=106` AI and `N=103` Human, while its other continuous outcomes use `N=151` and `N=149`.
- Basis: the plotted HbA1c analysis appears to use all 300 restricted-analysis participants, whereas the supplement table uses the 209 baseline-prediabetes participants. No Figure 3 footnote explains a different HbA1c population, so the displayed analysis set conflicts with both the outcome-applicability statement and eTable 14.
- Verification instruction: count or obtain the source-data row count for Figure 3B and verify whether it contains 151 AI plus 149 Human observations; compare its inclusion rule with the 106/103 row in eTable 14 and the main-text HbA1c eligibility statement.

### Candidate SC-03 - eTable 5 gives incompatible age P values and incompatible significance summaries

- Category: `Statistical reporting inconsistency`
- Location: DOC-003, PDF pp. 42-43, eTable 5, footnotes 1 and 2.
- Source statements: footnote 1 says trial sites differ for age (`P=.017`), race, marital status, educational attainment, and MVPA (each latter `P<.001`). Footnote 2, attached to the age row, says age differed between study groups (`P=.014`) and `all other baseline characteristics were similar (P>.05)`.
- Basis: the same table associates age with two P values, .017 and .014, without distinguishing the comparison populations. The statement that all other characteristics were similar also conflicts with footnote 1's four other significant characteristics. This is consistent with an inapplicable repeated footnote rather than a single coherent table-specific summary.
- Verification instruction: inspect both footnotes on DOC-003 p. 43 and determine from the table analysis output which comparison and P value belong to eTable 5; remove or relabel the inapplicable statement.

### Candidate SC-04 - eTable 6 simultaneously reports age as nonsignificant and significant

- Category: `Statistical reporting inconsistency`
- Location: DOC-003, PDF pp. 44-45, eTable 6, footnotes 1 and 2.
- Source statements: footnote 1 reports site (`P=.024`) and ethnicity (`P=.018`) as different between baseline-A1c groups and says `all other baseline characteristics were similar (P>.05)`. Footnote 2, attached to age, says age differed between study groups (`P=.014`).
- Basis: age is included in `all other` in footnote 1, implying P>.05, but footnote 2 gives P=.014. The same table therefore gives incompatible significance classifications for age.
- Verification instruction: inspect DOC-003 p. 45 and compare the age-test output for the two eTable 6 columns; retain the correct table-specific P value and significance summary.

### Candidate SC-05 - eTable 7 says no baseline characteristic differed, then reports age P=.014

- Category: `Statistical reporting inconsistency`
- Location: DOC-003, PDF pp. 46-47, eTable 7, footnotes 1 and 2.
- Source statements: footnote 1 says `No baseline characteristics were statistically significant different between groups (p<0.05)`. Footnote 2, attached to age, says age differed between study groups (`P=.014`).
- Basis: P=.014 is below .05 and directly contradicts the no-difference statement. In addition, the parenthetical `p<0.05` denotes the conventional significance region and is logically inconsistent with the preceding word `No`.
- Verification instruction: inspect DOC-003 p. 47, verify the completer-versus-dropout age test, and correct both the age statement and the inequality in the no-difference statement.

### Candidate SC-06 - eTable 11 repeats incompatible age P values and contradicts its sex result

- Category: `Statistical reporting inconsistency`
- Location: DOC-003, PDF pp. 53-54, eTable 11, footnotes 1 and 2.
- Source statements: footnote 1 reports age `P=.010` and sex `P=.041`, with all other characteristics P>.05. Footnote 2, attached to age, reports age `P=.014` and says all other baseline characteristics were similar (`P>.05`).
- Basis: the same restricted-analysis table assigns age two P values (.010 and .014). Footnote 2's `all other` statement also conflicts with the sex result P=.041 in footnote 1.
- Verification instruction: inspect DOC-003 p. 54 and the restricted-population comparison output; verify the age and sex tests and delete or relabel the non-table-specific footnote.

### Candidate SC-07 - Figure 3 labels BMI values as weight

- Category: `Presentation inconsistency`
- Location: DOC-001, PDF p. 8, Figure 3, footnote a.
- Source statement/values: `Baseline median (IQR) weight: 32.2 (28.2-35.9) kg/m2` for AI-led DPP and `32.5 (29.3-37.7) kg/m2` for Human-led DPP. The same values are reported as baseline BMI in the main Table (DOC-001, PDF p. 6) and eTable 3 (DOC-003, pp. 39-40).
- Basis: kg/m2 and the repeated 32.2/32.5 values identify BMI, not weight. The figure footnote therefore mislabels the statistic.
- Verification instruction: compare Figure 3 footnote a with the main baseline Table BMI row and revise `weight` to `BMI` if those values are intended.

## Uncertain observations (not advanced as findings)

### U-01 - MI-pooled percentages and reported risk difference have opposite signs

- Location: DOC-003, PDF p. 59, eTable 16.
- Values: pooled achievement is 32.2% AI versus 31.9% Human, an arithmetic difference of +0.3 percentage points, but the reported risk difference is -1.1 (-11.5).
- Why uncertain: the table does not say whether the risk difference is covariate-adjusted or otherwise model-derived. An adjusted estimate could differ from the displayed marginal percentages, and the package does not give enough analysis detail on this page to prove that simple subtraction is the intended estimator. Verify against the analysis specification/output and label the estimate as adjusted if applicable.

### U-02 - `Directionally consistent` is not literally true by the signs of all component point estimates

- Locations: DOC-001, PDF p. 5, `Secondary Outcomes`; DOC-001, PDF p. 7, Figure 2.
- Values: primary RD -0.2; component RDs -3.1, +0.1, and 0.0 percentage points.
- Why uncertain: if `directionally` means sign, the +0.1 and 0.0 estimates are not negative like the primary estimate. If it means that every lower one-sided CI remains above the -15-point noninferiority margin, the claim is coherent. The intended meaning is not sufficiently explicit for a verified issue.

### U-03 - Main-text `lower BMI strata` summary is broader than the subgroup values

- Locations: DOC-001, PDF p. 6, `Exploratory Analyses`; DOC-003, PDF p. 35, eFigure 4.
- Values: BMI-stratum RDs are +3.2 (overweight), -11.8 (class I), -0.7 (class II), and +19.4 (class III) percentage points.
- Why uncertain: the main text says the AI-led DPP appeared less effective in `lower BMI strata` and better in severe obesity. Class I and II estimates are negative, but the overweight estimate is positive. The phrase may describe an overall pattern rather than every lower category, so the package does not establish a definite contradiction.

## Rejected checks

- Primary outcome repetition: 58/183 (31.7%) versus 59/185 (31.9%), RD -0.2, lower one-sided 95% CI -8.2 is consistent in the abstract, Results, Figure 2, and eFigure 4. eFigure 3 is explicitly age-adjusted and therefore its -2.0 (-9.8) is not a repetition error.
- Point estimate versus lower confidence bound: every checked one-sided lower bound is less than or equal to its point estimate. No invalid ordering was found. CI symmetry was not assessed.
- Null/margin logic: all primary, restricted, and sensitivity lower bounds (-8.2, -9.8, -8.9, -11.5, -14.3, -8.8, -4.8, and -6.8) remain above the reported -15-point noninferiority margin, supporting the article's statement that sensitivity findings were consistent with the primary noninferiority result.
- Reported secondary P values are compatible with the displayed 2x2 counts under the stated chi-square comparisons: initiation 171/183 versus 153/185 gives Pearson P about .0015 (reported .001); completion 117/183 versus 93/185 gives P about .0081 (reported .008); diabetes-range A1c 8/183 versus 7/185 gives P about .776 (reported .78). eTable 10b's 6/183 versus 7/185 gives P about .793, matching its reported .793.
- Numerator-denominator percentages checked in the main primary/component results, Figure 4 engagement matrix, eFigures 3-4, eTables 2-11, eTables 13 and 15-20, and adverse-event participant totals were consistent to displayed rounding, apart from SC-01.
- One-sided CI presentation: the tables and figures consistently show a point estimate followed by a single lower bound and explicitly label it a one-sided 95% CI. Absence of an upper endpoint is therefore not an error.

## Disposition

Seven local candidates are returned. SC-03 through SC-06 are manifestations of the same repeated-footnote pattern but have distinct table-local contradictions and can be consolidated by the coordinator if desired. Three observations are retained as uncertain, and the remaining checked relationships are rejected as issues.
