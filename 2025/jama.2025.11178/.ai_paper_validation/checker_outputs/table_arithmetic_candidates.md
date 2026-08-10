# Table arithmetic and internal-consistency candidates

Scope checked: only result-relevant tables in DOC-001-MAIN, DOC-005-RESULTS (PDF pp. 3-18), and DOC-006-XLSX (`eTable 3`, A1:J115). Source PDFs and workbook were not modified. The candidates below are visible, document-verifiable inconsistencies; no raw-data inference was used.

## Candidate 1 - Follow-up-pattern counts do not reconcile to the reported totals

- **Category:** Arithmetic inconsistency

- **Location:** DOC-005-RESULTS, Supplement 4 PDF p. 7, eTable 1, rows "At least 1 follow-up," "No follow-up," and "One/Two/Three observed follow-ups."

- **Source values:** Overall: randomized 2331; at least 1 follow-up 2036; no follow-up 295; one/two/three observed follow-ups 188, 283, and 1568. painTRAINER: randomized 776; no/one/two/three 133, 77, 103, 464; at least 1 follow-up 643. Health Coach: randomized 778; no/one/two/three 88, 47, 81, 564; at least 1 follow-up 690.

- **Calculation:** Overall pattern categories sum to `295 + 188 + 283 + 1568 = 2334`, not 2331; the observed-follow-up categories sum to `188 + 283 + 1568 = 2039`, not 2036. For painTRAINER, `133 + 77 + 103 + 464 = 777`, not 776, and `77 + 103 + 464 = 644`, not 643. For Health Coach, `88 + 47 + 81 + 564 = 780`, not 778, and `47 + 81 + 564 = 692`, not 690.

- **Reasoning:** The mutually exclusive follow-up-pattern rows should partition the randomized cohort (and their nonzero-pattern subset). They overcount by 3 overall, with the same discrepancy distributed as 1 in painTRAINER and 2 in Health Coach.

## Candidate 2 - Displayed p values conflict with their own 95% confidence intervals

- **Category:** Statistical reporting inconsistency

- **Location:** DOC-005-RESULTS, Supplement 4 PDF p. 8, eTable 3 ("Imputation step 1"), coefficient rows.

- **Source values and calculation:** Each of the following displayed 95% CIs excludes the null value of 0 while the corresponding displayed two-sided p value is greater than .05: Pattern: 2 observed follow-ups, estimate -0.28, 95% CI -0.47 to -0.08, p=.150; Pattern: 1 observed follow-up, -0.20, -0.36 to -0.03, p=.226; Pattern 2 | painTRAINER, -0.30, -0.58 to -0.02, p=.280; Pattern 2 | Health Coach, -0.47, -0.74 to -0.19, p=.090; Site 3, 0.19, 0.08 to 0.29, p=.069; Site 4, 0.15, 0.05 to 0.24, p=.124.

- **Reasoning:** For a row-specific two-sided 95% CI and p value testing that coefficient against zero, exclusion of 0 entails p<.05. The table labels each p value at the row level and provides no alternative test definition that would explain the conflict.

## Candidate 3 - A 3-month Health Coach vs painTRAINER result is duplicated in the estimation-model table

- **Category:** Presentation inconsistency

- **Location:** DOC-005-RESULTS, Supplement 4 PDF p. 9, eTable 4, rows between "Health Coach (vs. Usual care plus)" and "Health Coach vs. painTRAINER 6M."

- **Source values:** "Health Coach vs. painTRAINER 3M" is displayed twice, both times as RR 1.20, 95% CI 1.03 to 1.40, p=.019.

- **Calculation:** Exact repeated row/value comparison: `(3M, 1.20, 1.03-1.40, .019)` equals the later `(3M, 1.20, 1.03-1.40, .019)`.

- **Reasoning:** The duplicate occupies one of the time-specific comparison rows, while 6M and 12M appear once each. This is a visible duplicate entry and should be checked for an omitted or mislabeled comparison.

## Candidate 4 - Duplicate education labels have conflicting estimates

- **Category:** Presentation inconsistency

- **Location:** DOC-005-RESULTS, Supplement 4 PDF p. 8 eTable 3 and p. 9 eTable 4, the two adjacent rows both labeled "Education: AA degree (ref = High school or less)" (eTable 3) / "Education: AA degree (vs./ref vs. HS or less)" (eTable 4).

- **Source values:** In eTable 3 the duplicate AA-degree labels have estimates -0.02 (95% CI -0.11 to 0.08; p=.866) and 0.16 (0.07 to 0.25; p=.077). In eTable 4 they have RRs 0.97 (0.82 to 1.16; p=.770) and 1.16 (1.00 to 1.33; p=.046).

- **Calculation:** Identical displayed exposure/reference labels are paired with unequal estimates: `-0.02 != 0.16` and `0.97 != 1.16`.

- **Reasoning:** A single categorical contrast cannot have two different row-specific estimates under the same stated label. One or both labels appear incomplete or erroneous, preventing unambiguous interpretation.

## Candidate 5 - Workbook percentage is incompatible with its displayed count and denominator

- **Category:** Arithmetic inconsistency

- **Location:** DOC-006-XLSX, worksheet `eTable 3`, cells A82:E83; specifically E82, "Current depression (PHQ-8 >=10)," and the missing-count row E83.

- **Source values:** E82 displays `711 (73.2)` for the All Observed group; E3 gives its denominator as N=1568; E83 gives 2 missing values. The other cells in row 82 are B82 `1116 (47.9)`, C82 `162 (54.9)`, and D82 `243 (51.9)`.

- **Calculation:** The relevant nonmissing denominator is `1568 - 2 = 1566`; `711 / 1566 x 100 = 45.4%` (one decimal), not 73.2%. The counts themselves reconcile: `162 + 243 + 711 = 1116`; B82 also reconciles as `1116 / (2331 - 2) x 100 = 47.9%`.

- **Reasoning:** The All Observed percentage is not compatible with its own visible numerator and stated missing-value convention, whereas the count is compatible with the overall and the other subgroup counts. This supports a percentage-cell error rather than a raw-count inference.

No additional document-verifiable arithmetic candidates were identified in the checked main-article tables, eTables 7-11, or the remaining workbook rows.
