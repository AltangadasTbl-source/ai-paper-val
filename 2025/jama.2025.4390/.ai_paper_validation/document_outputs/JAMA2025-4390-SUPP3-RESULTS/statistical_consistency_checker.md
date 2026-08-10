# Statistical Consistency Checker - Results Supplement

Source: `joi250019supp3_prod_1749674951.30054.pdf`

Processing status: Audited only on result-relevant pages specified by the package manifest. Source PDF unchanged.

## Candidate

1. **SCI-03 - Statistical reporting inconsistency, eTable 5, PDF p. 39.** With allocation denominators Morning n=44 and Bedtime n=57, the Diuretic and Combination BP med rows each report 9 (20.5%) versus 16 (28.1%), but their P values differ: .34 versus .38. Identical binary counts and denominators require the same P value under the same procedure. Inspect the analysis output to determine which row's count or P value is wrong.

## Negative and duplicate checks

- eTable 9 ABPM estimates, CIs, P values, and main-text repetitions were compatible.
- Allocation totals, loss-to-all-follow-up counts, and rounded adherence summaries matched the main article.
- eTable 5 PDF p. 37 duplicates White/Caucasian values in the `Other` ethnicity row. This confirmed issue is already retained as `TAC-01` by the table-arithmetic checker and is not duplicated here.

