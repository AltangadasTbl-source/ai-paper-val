# Statistical-consistency check

Scope: main article `jama_rathinam_2019_oi_190092.pdf` and results supplement
`joi190092supp1_prod.pdf`; protocol and SAP not used. Checked reported point
estimates against their stated confidence intervals, CI null inclusion against P
values, direction, repeated estimates/P values, subgroup labels, and displayed
denominators.

## Candidate 1 — displayed denominator conflicts with reported percentages

- **Category / severity:** Statistical reporting inconsistency / low (denominator
  presentation; does not change the event counts).
- **Reported item:** In `JAMA2019-12618-MAIN`,
  `jama_rathinam_2019_oi_190092.pdf`, PDF p. 8, Table 3, the column header is
  “Mycophenolate Mofetil (n = 109)”. In that column the nonserious-laboratory row
  reports “Elevated ALT or AST …: 8 (7.4)”, and the nonserious-systemic row reports
  “Headache: 45 (41.7)”. Footnote b says, “One patient in the mycophenolate
  mofetil group never received mycophenolate mofetil due to medical
  contraindication discovered postrandomization.”
- **Comparator:** In `JAMA2019-12618-SUPP-RESULTS`, `joi190092supp1_prod.pdf`,
  PDF pp. 10–12, eTables 4–6 label the corresponding mycophenolate denominator
  as `N = 108` and state that this excludes the one patient who never received
  mycophenolate.
- **Reproducible check:** With the displayed Table 3 denominator, `8 / 109 × 100
  = 7.339…%`, which rounds to **7.3%** at one decimal; `45 / 109 × 100 =
  41.284…%`, which rounds to **41.3%**. The printed values instead equal the
  supplement's denominator: `8 / 108 × 100 = 7.407…% → 7.4%` and `45 / 108 ×
  100 = 41.666…% → 41.7%`. The discrepancy (0.1 and 0.4 percentage points,
  respectively) is larger than the maximum 0.05-point tolerance from rounding a
  one-decimal percentage using 109, while both values are consistent with 108.
- **Bounded impact:** The numerical event counts are unchanged; the Table 3
  header/footnote does not explicitly state that its percentages use 108 rather
  than the displayed 109, so its denominator presentation is internally
  inconsistent and can mislead a reader calculating event rates.
- **Human verification:**
  1. Inspect Table 3's header and footnote b on main-PDF p. 8.
  2. Recalculate 8/109 and 45/109 to one decimal. Values of 7.3% and 41.3%
     confirm the conflict with the printed 7.4% and 41.7%.
  3. Inspect eTables 4–6, supplement PDF pp. 10–12. Their explicit `N = 108`
     labels and matching percentages confirm that Table 3 used a different
     denominator from its header. An explicit Table 3 statement that rates were
     calculated among 108 treated participants would resolve the presentation
     issue.

## Candidate 2 — percentage in the stated N=20 column is calculated using N=29

- **Category / severity:** Arithmetic inconsistency / low (one adverse-event
  percentage; count unaffected).
- **Reported item:** In `JAMA2019-12618-SUPP-RESULTS`,
  `joi190092supp1_prod.pdf`, PDF p. 15, eTable 9 (“Six- to 12-Month Adverse
  Events … in Patients Switching to the Other Antimetabolite”), the headers state
  “Methotrexate (N=29)” and “Mycophenolate Mofetil (N=20)”. In the serious-systemic
  row, `Diarrhea` is reported as `0 (0.0)` and `1 (3.4)`, respectively.
- **Reproducible check:** In the mycophenolate column, `1 / 20 × 100 = 5.0%`.
  The printed `3.4%` instead equals `1 / 29 × 100 = 3.448…%`, rounded to one
  decimal. No rounding tolerance can reconcile 5.0% with 3.4% at the stated
  denominator.
- **Bounded impact:** The serious-diarrhea count remains one patient, but the
  reported event rate for the N=20 mycophenolate switching group is understated
  by 1.6 percentage points (printed 3.4% vs 5.0%).
- **Human verification:**
  1. Inspect eTable 9's two column headers and serious-systemic `Diarrhea` row
     on supplement-PDF p. 15.
  2. Divide the displayed count (1) by the displayed denominator (20). A result
     of 5.0% confirms the inconsistency; a corrected column denominator of 29
     would instead resolve it.

## Checks with no candidate

The primary 6-month estimate (risk difference 9.5%, 95% CI −5.3% to 21.8%; OR
1.50, 95% CI 0.81 to 2.81; P=.20), both anatomical subgroup estimates, the
India/site/country interaction labels and P values, the 12-month estimates, and
the multiple-imputation sensitivity analysis were internally directionally
consistent: each CI's inclusion/exclusion of its stated null agreed with the
reported two-sided P value. Repeated primary/subgroup figures in the abstract,
narrative, Table 2, and Figure 2 matched within displayed rounding. CI symmetry
was not assessed because the stated regression/permutation methods do not make
that a valid document-grounded check.
