# Statistical Consistency Candidates

- Checker: `statistical_consistency_checker`
- Main article: `DOC-001-MAIN`, `jama_debar_2025_oi_250046_1755300121.13587.pdf`
- Results supplement: `DOC-005-RESULTS`, `joi250046supp4_prod_1755300121.15587.pdf`
- Evidence maps used: `DOC-001-MAIN/main_text_evidence.md` and `DOC-005-RESULTS/results_evidence.md`
- Source verification: rendered source pages and source-linked normalized text for the locations below
- Excluded by design: protocol, SAP, and TIDieR documents
- External sources: none
- Model caution: no candidate is based only on confidence-interval symmetry. CI/P candidates use only null inclusion/exclusion; standardized-effect candidates use the article's explicit definition or the requirement that a point estimate lie within its own reported interval.

## Candidate 1 - eTable 3 has multiple CI/P-value contradictions

- **Status:** Candidate
- **Category:** Statistical reporting inconsistency
- **Exact location:** `DOC-005-RESULTS`, PDF p. 8, eTable 3, "Imputation step 1: Summary of fitted imputation model for primary analysis."
- **Reported values:**
  - Pattern: 2 observed follow-ups: estimate -0.28, 95% CI -0.47 to -0.08, P = .150.
  - Pattern: 1 observed follow-up: estimate -0.20, 95% CI -0.36 to -0.03, P = .226.
  - Pattern 2 | painTRAINER: estimate -0.30, 95% CI -0.58 to -0.02, P = .280.
  - Pattern 2 | Health Coach: estimate -0.47, 95% CI -0.74 to -0.19, P = .090.
  - Site 3: estimate 0.19, 95% CI 0.08 to 0.29, P = .069.
  - Site 4: estimate 0.15, 95% CI 0.05 to 0.24, P = .124.
  - The second row labeled "Education: AA degree (ref = High school or less)": estimate 0.16, 95% CI 0.07 to 0.25, P = .077.
- **Reasoning:** Each 95% CI excludes the coefficient null value of 0, but each adjacent P value is greater than .05. Supplement p. 5 states that the imputation model was fit as a modified linear model using GEE with robust standard errors, and eTable 3 presents estimates, 95% CIs, and row-level P values from that fitted model. If the CI and P value test the same coefficient with the same two-sided inferential procedure, the null conclusions conflict. This check does not depend on CI symmetry.
- **Verification instruction:** Regenerate the coefficient table from the fitted step-1 model and confirm row alignment of the estimate, robust 95% CI, and two-sided P value, especially across the pattern, site, and education rows.

## Candidate 2 - Main Table 3 standardized point estimates fall outside their own 95% CIs

- **Status:** Candidate
- **Category:** Statistical reporting inconsistency
- **Exact locations:** `DOC-001-MAIN`, Table 3, PDF p. 10 / JAMA p. 601 and PDF p. 11 / JAMA p. 602.
- **Reported values:**
  - Pain severity, 12 months: painTRAINER vs usual care SMD -0.25 (95% CI, -0.24 to 0.01); health coach vs usual care SMD -0.36 (-0.35 to -0.12).
  - Pain intensity, 12 months: health coach vs usual care SMD -0.27 (-0.26 to -0.12).
  - Pain-related interference, 12 months: painTRAINER vs usual care SMD -0.26 (-0.25 to 0.01); health coach vs usual care SMD -0.37 (-0.36 to -0.11).
  - PGIC-pain, 12 months: painTRAINER vs usual care SMD -0.55 (-0.50 to 0.05); health coach vs usual care SMD -0.57 (-0.54 to -0.08); health coach vs painTRAINER SMD -0.29 (-0.25 to 0.14).
- **Reasoning:** In every listed cell, the point estimate is numerically below the printed lower confidence limit, so the estimate is not contained in its own reported 95% CI. This is an interval-order/containment check, not a symmetry check.
- **Verification instruction:** Compare the source model output with the Table 3 standardized-effect cells and determine whether the point estimate, one or both CI limits, or the cell placement is incorrect.

## Candidate 3 - Main Table 3 prints reversed standardized-effect CI limits

- **Status:** Candidate
- **Category:** Presentation inconsistency
- **Exact location:** `DOC-001-MAIN`, Table 3, PDF p. 10 / JAMA p. 601, standardized mean difference columns for social role and physical functioning.
- **Reported examples:**
  - Social role functioning, 3 months: painTRAINER vs usual care 0.12 (95% CI, 0.23 to 0.11); health coach vs usual care 0.01 (0.12 to -0.00); health coach vs painTRAINER 0.20 (0.29 to 0.19).
  - Physical functioning, 3 months: painTRAINER vs usual care 0.09 (0.16 to 0.07); health coach vs usual care -0.02 (0.05 to -0.04); health coach vs painTRAINER 0.16 (0.22 to 0.15).
  - The same descending-limit pattern recurs in the 6- and 12-month standardized-effect cells for both outcomes.
- **Reasoning:** The value printed before "to" is greater than the value printed after "to" in these cells. The rest of the article reports intervals from lower to upper limit. The defect is directly visible and does not require assumptions about interval symmetry.
- **Verification instruction:** Check the ordered CI endpoints in the source output and the column mapping used to populate all social-role and physical-function standardized-effect cells at 3, 6, and 12 months.

## Candidate 4 - Standardized and unstandardized effect directions conflict with Table 3's definition

- **Status:** Candidate
- **Category:** Statistical reporting inconsistency
- **Exact locations:** `DOC-001-MAIN`, Table 3, PDF pp. 10-11 / JAMA pp. 601-602; footnote d on PDF p. 11.
- **Reported values:**
  - Physical functioning, 3 months, health coach vs usual care: adjusted mean difference +0.7 (95% CI, 0.2 to 1.2), but SMD -0.02 (0.05 to -0.04).
  - Physical functioning, 6 months, health coach vs painTRAINER: adjusted mean difference -0.3 (-0.8 to 0.3), but SMD +0.22 (0.16 to 0.05).
  - Physical functioning, 12 months, health coach vs painTRAINER: adjusted mean difference -0.1 (-0.7 to 0.5), but SMD +0.27 (0.25 to 0.09).
  - PGIC-pain, 12 months, health coach vs painTRAINER: adjusted mean difference +0.1 (-0.1 to 0.2), but SMD -0.29 (-0.25 to 0.14).
- **Reasoning:** Table 3 footnote d defines the SMD as the adjusted between-group mean difference divided by the standard deviation of change in the usual-care group at that time point. A standard deviation is positive, so this transformation must preserve the sign of the corresponding adjusted mean difference. The listed pairs have opposite signs.
- **Verification instruction:** Recalculate each SMD from the corresponding adjusted mean difference and usual-care change SD, then check whether the last two SMD comparison columns were transposed or otherwise mis-populated.

## Candidate 5 - The 3-month pain-severity SMDs differ between Results text and Table 3

- **Status:** Candidate
- **Category:** Statistical reporting inconsistency
- **Exact locations:** `DOC-001-MAIN`, Results - Secondary Outcomes, PDF p. 7 / JAMA p. 598; Table 3, Pain severity, 3 months, PDF p. 10 / JAMA p. 601.
- **Reported values:**
  - Results text: painTRAINER vs usual care SMD -0.26; health coach vs usual care SMD -0.36.
  - Table 3: painTRAINER vs usual care SMD -0.25; health coach vs usual care SMD -0.34.
- **Reasoning:** These are repeated descriptions of the same outcome, time point, and treatment comparisons, but the point estimates differ at the reported two-decimal precision. The health-coach discrepancy (-0.36 vs -0.34) is too large to be explained by ordinary rounding of one common value to two decimals.
- **Verification instruction:** Identify the authoritative 3-month standardized estimates in the analysis output and reconcile both the Results sentence and the Table 3 cells.

## Candidate 6 - eTable 4 duplicates the identical 3-month health-coach comparison

- **Status:** Candidate
- **Category:** Presentation inconsistency
- **Exact location:** `DOC-005-RESULTS`, PDF p. 9, eTable 4.
- **Reported values:** "Health Coach vs. painTRAINER 3M" appears twice, each time with RR 1.20, 95% CI 1.03 to 1.40, and P = .019. One occurrence follows the two 3-month intervention coefficients; the second appears again after the 6- and 12-month health-coach vs usual-care rows.
- **Reasoning:** The label, time point, estimate, CI, and P value are exactly repeated within the same fitted-model table. This makes one row redundant and raises the possibility that another intended row or label was displaced.
- **Verification instruction:** Compare the eTable 4 row sequence with the fitted-model coefficient names and confirm whether the second 3-month row should be deleted or relabeled.

## Candidate 7 - eTables 3-4 do not uniquely identify site and education coefficients

- **Status:** Candidate
- **Category:** Presentation inconsistency
- **Exact locations:** `DOC-005-RESULTS`, eTable 3 on PDF p. 8 and eTable 4 on PDF p. 9.
- **Reported labels and values:**
  - eTable 3 contains two separate rows both labeled "Education: AA degree (ref = High school or less)," with estimates -0.02 (95% CI, -0.11 to 0.08; P = .866) and 0.16 (0.07 to 0.25; P = .077).
  - eTable 4 again contains two "Education: AA degree" rows, with RRs 0.97 (0.82 to 1.16; P = .770) and 1.16 (1.00 to 1.33; P = .046).
  - eTable 4 contains three consecutive rows all labeled only "Site," with RRs 1.07, 1.15, and 1.17. The corresponding rows in eTable 3 are uniquely labeled Site 2, Site 3, and Site 4.
- **Reasoning:** Distinct coefficients cannot be mapped to unique covariate levels from the printed eTable 4 site labels, and the duplicated education label assigns different estimates to the same stated comparison in both model tables. The intended missing education category is not inferred here.
- **Verification instruction:** Compare the model design-matrix level names with both tables and restore unique labels for each site and education coefficient.

## Candidate 8 - The supplement's treatment-group definition duplicates UC and omits HC

- **Status:** Candidate
- **Category:** Presentation inconsistency
- **Exact location:** `DOC-005-RESULTS`, PDF p. 5, Missing Data - Imputation (MNAR), explanatory text immediately after the step-1 model equation.
- **Reported statement:** The intervention-group variable is described as having levels "(UC, PT, and UC)."
- **Reasoning:** UC is listed twice and HC is omitted, although the supplied article consistently identifies the three randomized groups as usual care plus (UC), painTRAINER (PT), and health coach (HC), including eTables 3-4 on pp. 8-9.
- **Verification instruction:** Confirm the coded factor levels in the imputation model and correct the explanatory text to list each of the three groups once.

## Candidate 9 - eTable 11 raw-score group headings appear permuted

- **Status:** Candidate
- **Category:** Presentation inconsistency
- **Exact location:** `DOC-005-RESULTS`, PDF p. 17, eTable 11.
- **Reported values:**
  - Header order is painTRAINER, Health Coach, Usual Care plus.
  - Pain severity, 3 months: raw-score cells 5.1, 4.6, 4.6; reported comparisons PT vs UC -0.5, HC vs UC -0.5, HC vs PT 0.0.
  - Social role functioning, 3 months: raw-score cells 43.4, 44.6, 44.8; reported comparisons +1.2, +1.4, +0.2.
  - PGIC-general, 3 months: raw-score cells 2.7, 2.0, 1.6; reported comparisons -0.8, -1.1, -0.3.
- **Reasoning:** Across outcomes, the comparison directions and approximate magnitudes align if the three raw-score columns are read as Usual Care plus, painTRAINER, Health Coach, not as the printed header order. For example, the social-role values give 44.6 - 43.4 = 1.2, 44.8 - 43.4 = 1.4, and 44.8 - 44.6 = 0.2. The same proposed permutation resolves the pain-severity and PGIC-general directions. Because the table labels the raw summaries as medians while the comparisons are mean differences, this is retained as a candidate for source-output verification rather than treated as proven solely by subtraction.
- **Verification instruction:** Compare the eTable 11 raw-score export column order with the header labels and verify the treatment assignment of every raw-score column.

## Candidate 10 - eTable 8 labels randomized denominators as 3-month counts in the pre-enhancement subset

- **Status:** Candidate
- **Category:** Presentation inconsistency
- **Exact location:** `DOC-005-RESULTS`, PDF p. 14, eTable 8, first subset heading ("Randomized prior to 8/9/2021").
- **Reported statement:** "N=454; 366 with at least 1 follow-up; PT=149, HC=153, UC=152 at 3-months."
- **Calculation:** 149 + 153 + 152 = 454.
- **Reasoning:** Counts explicitly labeled "at 3-months" sum to the entire randomized subset (454), even though only 366 participants are stated to have any follow-up at all. Therefore the three counts cannot all be observed 3-month denominators. They appear more consistent with randomized group denominators, but the intended label is not inferred as fact.
- **Verification instruction:** Check the subset analysis dataset and revise either the "at 3-months" label or the three group counts so the heading distinguishes randomized denominators from observed/imputed analytic counts.

## Scope conclusion

Ten local candidates were retained. No candidate relies on protocol, SAP, TIDieR, web material, external knowledge, or CI symmetry. The native workbook was not required to establish any retained candidate; all retained findings are directly verifiable from the main article and results supplement pages above.
