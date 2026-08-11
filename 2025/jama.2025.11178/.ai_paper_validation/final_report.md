# Package Manifest

Package: `jama.2025.11178`

| Source file | Pages | Classification | Scientific audit scope |
|---|---:|---|---|
| [jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf) | 14 | Main article | Pages 1-14 |
| [joi250046supp1_prod_1755300121.14087.pdf](../joi250046supp1_prod_1755300121.14087.pdf) | 77 | Protocol | Not Audited by Design; specific comparison only |
| [joi250046supp2_prod_1755300121.15087.pdf](../joi250046supp2_prod_1755300121.15087.pdf) | 29 | Statistical analysis plan | Not Audited by Design; specific comparison only |
| [joi250046supp3_prod_1755300121.15087.pdf](../joi250046supp3_prod_1755300121.15087.pdf) | 7 | Intervention description / TIDieR | Not Audited by Design |
| [joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf) | 19 | Results supplement | Pages 3-18; page 2 context only |
| [joi250046supp5_prod_1755300121.16087.xlsx](../joi250046supp5_prod_1755300121.16087.xlsx) | N/A | Results workbook, sheet `eTable 3` | Entire sheet |

Source PDFs were preserved unchanged. [joi250046supp5_prod_1755300121.16087.xlsx](../joi250046supp5_prod_1755300121.16087.xlsx) is a supplied result artifact and is not subject to the PDF-only rights-record requirement.

# AI Training Restriction Summary

This screen is separate from the scientific findings and is not a legal opinion. The coordinator reports institutional permission for AI use as granted.

| Source file | Status | Exact evidence location and quotation | Human Compliance Review |
|---|---|---|---|
| [jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf) | Explicit AI Training Restriction | PDF p. 1 footer; also pp. 2-14: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Yes |
| [joi250046supp1_prod_1755300121.14087.pdf](../joi250046supp1_prod_1755300121.14087.pdf) | No AI Training Restriction Located in Provided Materials | Embedded document information/XMP; targeted review pp. 1-2; supplied-file keyword screen. No AI-training, fine-tuning, or model-improvement restriction language located. | No |
| [joi250046supp2_prod_1755300121.15087.pdf](../joi250046supp2_prod_1755300121.15087.pdf) | No AI Training Restriction Located in Provided Materials | Embedded document information/XMP, `dc:title`/PDF Title: “CONFIDENTIAL”; targeted review pp. 1-2; supplied-file keyword screen. No AI-training, fine-tuning, or model-improvement restriction language located. | No |
| [joi250046supp3_prod_1755300121.15087.pdf](../joi250046supp3_prod_1755300121.15087.pdf) | Explicit AI Training Restriction | PDF p. 1 footer; also pp. 2-7: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Yes |
| [joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf) | Explicit AI Training Restriction | PDF p. 1 footer; also pp. 2-19: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Yes |

# Audit Method and Revision Status

- This report uses only the supplied article-package files. No web search, external retrieval, or unstated external knowledge was used.
- Each disposition below preserves the original candidate identifier so it can be traced to `candidate_set.md`, the checker outputs, the verifier record, and the critic record.
- **Verified** means that the reported inconsistency can be reproduced directly from the supplied files without assuming an unstated statistical test or an unreported data-generating mechanism.
- **Uncertain** means that the printed values are confirmed but the claimed inconsistency depends on an inferential assumption that the supplied files do not define.
- This revision incorporates a parent-requested second source reading of C02 and C03. C02 is changed from Verified to **Uncertain** because eTable 3 does not define the row-level P-value hypothesis or confirm that its confidence intervals and P values use the same two-sided construction. C03 remains Verified, with the workbook-wide search and recoverable percentage documented explicitly.
- Final disposition: **9 verified scientific findings, 1 uncertain candidate, 0 rejected candidates**. Uncertain candidates are not counted as final scientific findings.

## Candidate Disposition Summary

| Candidate | Disposition | Category | Severity |
|---|---|---|---|
| C01 | Verified | Participant flow inconsistency | Major |
| C02 | Uncertain | Potential statistical reporting inconsistency | Major if confirmed |
| C03 | Verified | Arithmetic inconsistency | Minor |
| C04 | Verified | Statistical reporting inconsistency | Major |
| C05 | Verified | Statistical reporting inconsistency | Minor |
| C06 | Verified | Presentation inconsistency | Minor |
| C07 | Verified | Presentation inconsistency | Minor |
| C08 | Verified | Presentation inconsistency | Minor |
| C09 | Verified | Presentation inconsistency | Minor |
| C10 | Verified | Presentation inconsistency | Minor |

# Verified Scientific Findings

## C01 — Follow-up-pattern counts do not reconcile

- **Evidence status:** Verified
- **Category:** Participant flow inconsistency
- **Severity:** Major
- **Location:** [joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf), PDF p. 7, eTable 1; corroboration in [jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf), PDF p. 5, Figure 1, and [joi250046supp5_prod_1755300121.16087.xlsx](../joi250046supp5_prod_1755300121.16087.xlsx), sheet `eTable 3`, B2:E3.
- **Reported values:** Overall randomized `N=2331`; at least 1 follow-up `N=2036`; no/one/two/three observed follow-ups `295/188/283/1568`. Usual care plus: randomized `777`, at least 1 follow-up `703`, patterns `74/64/99/540`. painTRAINER: randomized `776`, at least 1 follow-up `643`, patterns `133/77/103/464`. Health Coach: randomized `778`, at least 1 follow-up `690`, patterns `88/47/81/564`.

**Reasoning procedure**

1. Treat the no/one/two/three-follow-up rows as mutually exclusive and exhaustive categories, as their labels describe the number of observed assessments out of the three scheduled assessments.
2. Sum the four overall pattern rows: `295 + 188 + 283 + 1568 = 2334`, which is 3 more than the reported analysis population of 2331.
3. Sum the three nonzero-follow-up rows: `188 + 283 + 1568 = 2039`, which is 3 more than the reported 2036 participants with at least one follow-up.
4. Repeat the calculation by arm. Usual care reconciles: `74 + 64 + 99 + 540 = 777` and `64 + 99 + 540 = 703`. painTRAINER gives `777` rather than `776` and `644` rather than `643`. Health Coach gives `780` rather than `778` and `692` rather than `690`.
5. Check Figure 1. It reports 643 painTRAINER and 690 Health Coach participants completing any follow-up. It also shows 779 randomized to usual care, including 2 randomized in error, leaving 777 in the primary analysis. This confirms that the discrepancy is not caused by confusing the 2333 originally randomized participants with the 2331-person analysis population.
6. Check the workbook partition: no follow-up `295`, missing one or two follow-ups `468`, and all three observed `1568`. These sum exactly to `2331`, whereas eTable 1's one- and two-observed rows sum to `188 + 283 = 471`, again 3 too many.

- **Supported conclusion:** eTable 1 overcounts the mutually exclusive follow-up-pattern categories by 3, localized as +1 in painTRAINER and +2 in Health Coach. The error is within the one- and/or two-observed-follow-up cells; the supplied files do not identify the exact corrected allocation between those two rows.
- **Verification instruction:** Reproduce participant-level follow-up-pattern counts by arm and correct the affected eTable 1 cells while preserving the verified totals of 643, 690, and 2331.

## C03 — The current-depression percentage is incompatible with its count and denominator

- **Evidence status:** Verified
- **Category:** Arithmetic inconsistency
- **Severity:** Minor
- **Location:** [joi250046supp5_prod_1755300121.16087.xlsx](../joi250046supp5_prod_1755300121.16087.xlsx), sheet `eTable 3`, E3 and A82:E83; footnote a at A110.
- **Reported values:** E3=`(N=1568)` for the `All Observed` group; E82=`711 (73.2)` for `Current depression (PHQ-8 ≥10), No. (%)`; E83=`2` missing. The other group cells are B82=`1116 (47.9)`, C82=`162 (54.9)`, and D82=`243 (51.9)`.

**Reasoning procedure**

1. Apply footnote a, which states that missing observations are excluded from the percentage denominator.
2. Calculate the E-column nonmissing denominator: `1568 - 2 = 1566`.
3. Calculate the percentage from the printed count: `711 / 1566 × 100 = 45.402...%`, which rounds to `45.4%`, not `73.2%`.
4. Cross-check the count across groups: `162 + 243 + 711 = 1116`, exactly reproducing the overall current-depression count.
5. Cross-check the overall percentage: `1116 / (2331 - 2) × 100 = 47.9%`, exactly reproducing B82.
6. Search the complete workbook. `73.2` occurs only once, in E82. E82 is a static displayed string rather than a formula; no other cell, formula, comment, or supplied workbook record identifies a different intended location for `73.2`.

- **Supported conclusion:** The error is localized to the percentage printed in E82. The directly recoverable display is `711 (45.4)`. The count 711 is internally supported; the supplied workbook does not establish where `73.2` originated.
- **Verification instruction:** Replace only the E82 percentage after confirming the source export; do not infer a different count or claim that `73.2` belongs to another row or column.

## C04 — Multiple invalid standardized mean difference displays in Table 3

- **Evidence status:** Verified
- **Category:** Statistical reporting inconsistency
- **Severity:** Major
- **Location:** [jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf), Table 3, PDF pp. 10-11 / JAMA pp. 601-602; standardization definition in footnote d on PDF p. 11.

### A. Point estimates outside their printed 95% confidence intervals

| Outcome and time | Comparison | Printed SMD and 95% CI | Direct check |
|---|---|---|---|
| Pain severity, 12 months | painTRAINER vs usual care | `-0.25 (-0.24 to 0.01)` | `-0.25 < -0.24`; estimate is below the lower limit |
| Pain severity, 12 months | Health Coach vs usual care | `-0.36 (-0.35 to -0.12)` | `-0.36 < -0.35` |
| Pain intensity, 12 months | Health Coach vs usual care | `-0.27 (-0.26 to -0.12)` | `-0.27 < -0.26` |
| Pain-related interference, 12 months | painTRAINER vs usual care | `-0.26 (-0.25 to 0.01)` | `-0.26 < -0.25` |
| Pain-related interference, 12 months | Health Coach vs usual care | `-0.37 (-0.36 to -0.11)` | `-0.37 < -0.36` |
| PGIC-pain, 12 months | painTRAINER vs usual care | `-0.55 (-0.50 to 0.05)` | `-0.55 < -0.50` |
| PGIC-pain, 12 months | Health Coach vs usual care | `-0.57 (-0.54 to -0.08)` | `-0.57 < -0.54` |
| PGIC-pain, 12 months | Health Coach vs painTRAINER | `-0.29 (-0.25 to 0.14)` | `-0.29 < -0.25` |

For each cell, compare the point estimate with the two interval endpoints. A reported point estimate must lie between the stated lower and upper limits; all eight fail that containment check.

### B. Confidence-interval endpoints printed in descending order

The social-role and physical-function blocks each contain 3 time points × 3 pairwise comparisons, giving `2 × 3 × 3 = 18` SMD cells. In all 18, the first endpoint is larger than the second. Examples include social role at 3 months, `0.12 (0.23 to 0.11)`, and physical function at 3 months, `-0.02 (0.05 to -0.04)`. The direct check is simply `first endpoint > second endpoint`; the table convention elsewhere is lower-to-upper.

### C. SMD signs conflict with their defining adjusted mean differences

| Outcome and time | Comparison | Adjusted mean difference | Printed SMD |
|---|---|---:|---:|
| Physical function, 3 months | Health Coach vs usual care | `+0.7 (0.2 to 1.2)` | `-0.02 (0.05 to -0.04)` |
| Physical function, 6 months | Health Coach vs painTRAINER | `-0.3 (-0.8 to 0.3)` | `+0.22 (0.16 to 0.05)` |
| Physical function, 12 months | Health Coach vs painTRAINER | `-0.1 (-0.7 to 0.5)` | `+0.27 (0.25 to 0.09)` |
| PGIC-pain, 12 months | Health Coach vs painTRAINER | `+0.1 (-0.1 to 0.2)` | `-0.29 (-0.25 to 0.14)` |

Footnote d defines the SMD as the adjusted between-group mean difference divided by the usual-care group's change standard deviation at that time. A standard deviation is positive, so division cannot change the sign. Each listed pair violates that sign-preservation rule.

- **Supported conclusion:** Table 3 contains multiple directly demonstrable invalid SMD displays: eight containment failures, 18 reversed endpoint displays, and four sign conflicts under the table's stated definition.
- **Limit on interpretation:** The supplied pages do not establish whether the cause is column mapping, transposition, row displacement, or another production error.
- **Verification instruction:** Recreate every affected SMD and interval from the authoritative adjusted differences and usual-care change standard deviations, then verify comparison-column placement.

## C05 — Results text and Table 3 report different 3-month SMDs

- **Evidence status:** Verified
- **Category:** Statistical reporting inconsistency
- **Severity:** Minor
- **Location:** [jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf), Results—Secondary Outcomes, PDF p. 7 / JAMA p. 598, and Table 3, PDF p. 10 / JAMA p. 601.
- **Reported values:** The text reports 3-month pain-severity SMDs of `-0.26` for painTRAINER vs usual care and `-0.36` for Health Coach vs usual care. Table 3 reports `-0.25` and `-0.34`, respectively, for the same outcome, time point, and comparisons.

**Reasoning procedure**

1. Match the outcome (`pain severity`), time point (`3 months`), and comparison labels across the Results sentence and Table 3.
2. Compare the displayed point estimates at the common two-decimal precision: `-0.26 ≠ -0.25` and `-0.36 ≠ -0.34`.
3. The `-0.36` and `-0.34` displays cannot both be ordinary two-decimal roundings of one underlying value, so the discrepancy is not explainable by routine rounding alone.

- **Supported conclusion:** The main article gives discordant published SMD point estimates for the same two effects.
- **Verification instruction:** Identify the authoritative model-output values and align the Results sentence and Table 3. The supplied article does not establish which location is correct.

## C06 — An eTable 4 coefficient row is duplicated exactly

- **Evidence status:** Verified
- **Category:** Presentation inconsistency
- **Severity:** Minor
- **Location:** [joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf), PDF p. 9, eTable 4.
- **Reported values:** `Health Coach vs. painTRAINER 3M` appears once immediately after the two main treatment rows and again after the 6- and 12-month Health Coach-vs-usual-care rows. Both instances report `RR 1.20`, `95% CI 1.03 to 1.40`, and `P=.019`.

**Reasoning procedure**

1. Compare the two row labels, time-point suffixes, point estimates, lower and upper CI limits, and P values.
2. All fields are identical within the same coefficient table.

- **Supported conclusion:** The same complete coefficient row is printed twice.
- **Limit on interpretation:** The supplied page does not show whether the second row should be deleted or relabeled as a different coefficient.
- **Verification instruction:** Compare the printed row sequence with the fitted-model coefficient names and remove or relabel the second occurrence only as supported by the source output.

## C07 — Education and site coefficients are not uniquely labeled

- **Evidence status:** Verified
- **Category:** Presentation inconsistency
- **Severity:** Minor
- **Location:** [joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf), PDF p. 8, eTable 3, and PDF p. 9, eTable 4.
- **Reported values:** eTable 3 contains two rows both labeled `Education: AA degree (ref = High school or less)` but reports `-0.02 (-0.11 to 0.08), P=.866` and `0.16 (0.07 to 0.25), P=.077`. eTable 4 repeats the AA-degree label with `0.97 (0.82 to 1.16), P=.770` and `1.16 (1.00 to 1.33), P=.046`. eTable 4 also contains three rows labeled only `Site`, with RRs `1.07`, `1.15`, and `1.17`; the positional rows in eTable 3 are labeled Site 2, Site 3, and Site 4.

**Reasoning procedure**

1. Within each table, identify identical printed covariate-level labels.
2. Compare their coefficient values; the values differ, so the rows cannot be unambiguously identified by the common label.
3. Compare site-row specificity between tables. eTable 3 supplies three distinct site levels, while eTable 4 omits all three level numbers.

- **Supported conclusion:** The printed labels do not uniquely assign the education and site coefficients to design-matrix levels.
- **Limit on interpretation:** The supplied files do not establish the missing education-level label; it must not be inferred from external conventions.
- **Verification instruction:** Restore the exact source design-matrix label for every education and site coefficient in both tables.

## C08 — The first eTable 8 subset header does not identify what its 3-month arm counts represent

- **Evidence status:** Verified as a presentation inconsistency
- **Category:** Presentation inconsistency
- **Severity:** Minor
- **Location:** [joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf), PDF p. 14, eTable 8, first subset header.
- **Reported statement:** `Randomized prior to 8/9/2021, N=454; 366 with at least 1 follow-up; PT=149, HC=153, UC=152 at 3-months`.

**Reasoning procedure**

1. Sum the arm values attached to `at 3-months`: `149 + 153 + 152 = 454`.
2. This equals the entire randomized subset, while the same header says only 366 had at least one follow-up at any assessed time.
3. Therefore, the arm values cannot be observed 3-month counts. They may be randomized or imputed-analysis denominators, but the header does not say so.

- **Supported conclusion:** As printed, the header is incomplete or misleading about the meaning of the 149/153/152 values; they cannot be read as observed 3-month counts.
- **Limit on interpretation:** The supplied PDF does not establish whether these are randomized denominators, imputed-analysis denominators, or another quantity, and it does not establish replacement values.
- **Verification instruction:** Check the subset analysis dataset and model specification, then label the values with their actual denominator definition or replace them with observed 3-month counts if that was the intended display.

## C09 — eTable 9 calls explicitly unadjusted relative risks adjusted

- **Evidence status:** Verified
- **Category:** Presentation inconsistency
- **Severity:** Minor
- **Location:** [joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf), PDF p. 15, section heading/lead-in, eTable 9 title, and footnote b.
- **Reported statements:** The section is headed `ADDITIONAL UNADJUSTED DATA AND ANALYSES` and says the analyses use `no adjustment, weighting or imputation`. The eTable 9 title says `adjusted relative risk`, while footnote b says the relative risks were calculated `without adjustment`.

**Reasoning procedure**

1. Read the analysis description immediately above the table.
2. Compare it with the table title and the table's own analytic footnote.
3. Two locations explicitly say unadjusted/without adjustment; the title alone says adjusted.

- **Supported conclusion:** The table title directly conflicts with both its surrounding description and its own footnote.
- **Verification instruction:** Confirm the fitted model specification and harmonize the title, lead-in, and footnote. If the lead-in and footnote are authoritative, change `adjusted relative risk` to `unadjusted relative risk`.

## C10 — The prose and eTable 11 conflict over mean versus median raw summaries

- **Evidence status:** Verified for the summary-statistic description only
- **Category:** Presentation inconsistency
- **Severity:** Minor
- **Location:** [joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf), PDF p. 15 lead-in and PDF p. 17, eTable 11 title/header; analytic footnote continues on PDF p. 18.
- **Reported statements:** The p. 15 lead-in says eTable 11 provides `unadjusted mean secondary outcomes`. The p. 17 title says `Unadjusted Median and Interquartile Ranges`, and the raw group columns are labeled `Raw Score Median (25%-tile, 75%tile)`. The comparison columns are separately labeled as mean differences.

**Reasoning procedure**

1. Identify the statistic assigned to the treatment-group raw summaries in the p. 15 prose (`mean`).
2. Identify the statistic assigned to those raw summaries in the p. 17 title and raw-column header (`median` with interquartile range).
3. These are different descriptive statistics and cannot both describe the same raw group cells.
4. Do not treat the presence of mean-difference comparison columns as an error by itself; a table may report group medians and model-based mean differences. The verified conflict is between the prose and the raw-summary title/header.

- **Supported conclusion:** The supplement gives incompatible descriptions of the raw treatment-group summaries.
- **Limit on interpretation:** A proposed permutation of the three raw treatment columns is not verified. Differences between medians need not equal differences between means, and the supplied files do not establish which raw-summary label is authoritative.
- **Verification instruction:** Compare eTable 11 with the source export and make the p. 15 prose, table title, and raw-column headers use the correct statistic consistently.

# Uncertain Candidate

## C02 — Seven eTable 3 confidence intervals and adjacent P values appear incompatible under conventional row-level inference

- **Evidence status:** Uncertain; not retained as a final scientific finding without model-output confirmation
- **Potential category:** Statistical reporting inconsistency
- **Potential severity if confirmed:** Major
- **Location:** [joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf), PDF p. 8, eTable 3; imputation-model description on PDF pp. 4-5.

| Coefficient row | Estimate | Printed 95% CI | Printed P | Conventional two-sided Wald P approximated from rounded CI* |
|---|---:|---|---:|---:|
| Pattern: 2 observed follow-ups | -0.28 | -0.47 to -0.08 | .150 | .0049 |
| Pattern: 1 observed follow-up | -0.20 | -0.36 to -0.03 | .226 | .0175 |
| Pattern 2 × painTRAINER | -0.30 | -0.58 to -0.02 | .280 | .0357 |
| Pattern 2 × Health Coach | -0.47 | -0.74 to -0.19 | .090 | .0008 |
| Site 3 | 0.19 | 0.08 to 0.29 | .069 | .0004 |
| Site 4 | 0.15 | 0.05 to 0.24 | .124 | .0020 |
| Second row printed as AA degree | 0.16 | 0.07 to 0.25 | .077 | .0005 |

\*Diagnostic approximation only: `SE ≈ (upper limit - lower limit) / (2 × 1.96)`, followed by `z = |estimate| / SE` and a two-sided normal-tail probability. The source CIs are rounded, so these are not claimed as authoritative replacement P values.

**Reasoning procedure**

1. Confirm the seven printed estimate/CI/P triples directly in eTable 3. In every row, the printed 95% CI excludes zero while the adjacent P value exceeds `.05`.
2. Under the conventional interpretation that each P value is a two-sided test of the adjacent coefficient's null hypothesis `H0: coefficient = 0`, constructed from the same inferential variance as its 95% CI, exclusion of zero is equivalent to `P < .05`. The diagnostic calculations show that the differences are too large to be explained by display rounding alone under that interpretation.
3. Read the source methods and table labels. The methods describe a pattern-mixture modified linear GEE with independent working correlation and robust standard errors. eTable 3 labels its columns only `Variable`, `Est.`, `95% CI`, and `p-value`; it does not define the tested null, sidedness, degrees of freedom, or whether the CI and P use the same construction.
4. Consider an omnibus interpretation. It is not the best-supported reading because eTable 3 prints different P values for separate levels of Pattern, Site, and Education, while eTables 7 and 8 explicitly label omnibus P values when they are used. Nevertheless, the supplied files do not prove that every eTable 3 P value is the matching row-level coefficient test.

- **Supported conclusion:** The seven printed triples are highly suspicious under ordinary row-level two-sided inference, but the package does not define enough of the P-value procedure to prove the contradiction solely from the published files.
- **Verification instruction:** Obtain the fitted-model export or table-generation code and document, for each P value, the tested parameter/contrast, null hypothesis, sidedness, degrees-of-freedom or small-sample correction, variance estimator, and row alignment. Promote C02 to a verified finding only if the P values and CIs are intended as matched inference for the same coefficient.

# Rejected and Excluded Interpretations

- **Rejected candidates:** None.
- **C04 excluded mechanism:** No evidence establishes column mapping, transposition, or a specific production-error mechanism.
- **C08 excluded interpretation:** No evidence identifies 149/153/152 as randomized, imputed, or another denominator; no corrected label or counts are established.
- **C10 excluded interpretation:** No evidence proves the proposed raw-score treatment-column permutation or establishes whether means or medians are authoritative.
- **C03 excluded interpretation:** No evidence identifies where `73.2` originated or assigns it to another cell; only the E82 percentage error is retained.
- **Cap-excluded, not verified:** The supplement p. 6 eFigure cross-reference, the eTable 8 RR-header footnote marker, and the supplement p. 5 duplicated treatment-level abbreviation were outside the C01-C10 verification scope and are not scientific findings.

# Human Adjudication Checklist

- Retain C01 and C03-C10 as the nine document-verifiable scientific findings, subject to human adjudication.
- Keep C02 Uncertain unless the fitted-model export establishes matched row-level, two-sided coefficient inference.
- Reconcile C01 with participant-level follow-up-pattern output and C03 with the authoritative workbook export.
- Reconcile C04-C05 against authoritative Table 3 analysis output.
- Confirm intended row labels, denominator descriptions, and summary-statistic descriptions for C06-C10.
- Do not promote excluded interpretations or cap-excluded candidates without separate verification.
- Complete Human Compliance Review for [jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf), [joi250046supp3_prod_1755300121.15087.pdf](../joi250046supp3_prod_1755300121.15087.pdf), and [joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf); institutional permission for AI use was reported granted.
