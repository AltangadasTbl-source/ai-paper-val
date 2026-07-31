# Figure, flow-diagram, and presentation check — JAMA2019-12618

Scope: visual inspection of all main-article figures/tables (main PDF pp. 3 and 5–8, including Figure 1 and Figure 2) and result-relevant supplementary tables (Supplement 1 PDF pp. 5–16). Protocol, SAP, and administrative PDFs were not inspected. Figure 1's displayed patient and eye totals reconcile at each shown transition; Figure 2's displayed subgroup and sensitivity-analysis numerators/denominators also reconcile. The local candidates below are the only issues identified.

## Candidate 1 — Incorrect percentage in eTable 9

- **Category / severity:** Arithmetic inconsistency / low.
- **Issue statement:** The mycophenolate-mofetil serious-diarrhea percentage is reported as 3.4% despite the table's stated denominator of 20 and count of 1, for which the one-decimal percentage is 5.0%.
- **Exact location:** `JAMA2019-12618-SUPP-RESULTS`, `joi190092supp1_prod.pdf`, PDF p. 15, eTable 9, *Serious Systemic* section, *Diarrhea* row, *Mycophenolate Mofetil (N=20)* column.
- **Reported visual values:** The column label is “Mycophenolate Mofetil (N=20)”; the row reads “1 (3.4)”.
- **Comparator:** Other entries in that same N=20 column use N=20 (for example, *Low hemoglobin* reads “1 (5.0)”).
- **Calculation:** `1 / 20 × 100 = 5.0%`. At one decimal place, the usual rounding interval for 5.0% is 4.95% to 5.05%; 3.4% is 1.6 percentage points lower and instead equals `1 / 29 × 100` rounded to one decimal.
- **Bounded impact:** The event count remains 1; only the displayed percentage for this single adverse-event row is affected.
- **Human verification:**
  1. Confirm the eTable 9 denominator for the mycophenolate-mofetil column is 20.
  2. Confirm the underlying serious-diarrhea count is 1.
  3. A count of 1 among 20 confirms that the displayed percentage should be 5.0%; a different analytic denominator would resolve the issue only if it is explicitly substituted in the table header.

## Candidate 2 — Incorrect rounding in eTable 4

- **Category / severity:** Arithmetic inconsistency / low.
- **Issue statement:** The mycophenolate-mofetil *Eye floaters* percentage is printed as 4.7% although 5 events among the stated 108 patients rounds to 4.6% at one decimal place.
- **Exact location:** `JAMA2019-12618-SUPP-RESULTS`, `joi190092supp1_prod.pdf`, PDF p. 10, eTable 4, *Eye floaters* row, *Mycophenolate Mofetil (N=108)* column.
- **Reported visual values:** The table header and footnote specify 108 mycophenolate-mofetil recipients; the row reports “5 (4.7)”.
- **Comparator:** In the same N=108 column, *Frustration* in eTable 5 (PDF p. 11) is “5 (4.6),” consistent with a denominator of 108.
- **Calculation:** `5 / 108 × 100 = 4.6296…%`, which rounds to **4.6%** to one decimal place. A one-decimal 4.7% requires a value at least 4.65%; the reported value is 0.1 percentage point high and matches `5 / 107 × 100 = 4.6729…%` when rounded.
- **Bounded impact:** The count is unaffected; the error is confined to one displayed percentage.
- **Human verification:**
  1. Confirm the eTable 4 mycophenolate-mofetil denominator is 108 recipients.
  2. Confirm that five recipients reported eye floaters.
  3. These inputs confirm 4.6% at the displayed precision; an explicitly documented denominator other than 108 would be needed to resolve the issue.

## Candidate 3 — Unexplained 12-month continuing-treatment cohort mismatch

- **Category / severity:** Cross-document inconsistency / moderate (candidate; cohort definition requires confirmation).
- **Issue statement:** The supplement labels its 6-to-12-month adverse-event table as patients continuing treatment after treatment success but gives denominators of 62 and 56, whereas the main article's identically described continuing-treatment 12-month cohort is 60 and 54.
- **Exact locations and evidence:**
  - `JAMA2019-12618-MAIN`, `jama_rathinam_2019_oi_190092.pdf`, PDF p. 3, Figure 1, 12-month secondary-analysis boxes: “60 Continued methotrexate … included in the 12-month secondary analysis” and “54 Continued mycophenolate … included in the 12-month secondary analysis.”
  - `JAMA2019-12618-MAIN`, same PDF, p. 6, Table 2, *Treatment success at 12 mo* / *Continued on randomized antimetabolite* row: “48/60 (80)” and “40/54 (74)”; footnote g specifies that 60 and 54 patients who achieved six-month success continued on the same antimetabolite through 12 months.
  - `JAMA2019-12618-SUPP-RESULTS`, `joi190092supp1_prod.pdf`, PDF p. 14, eTable 8 title: “Patients Continuing on Treatment after Treatment Success”; column headers: “Methotrexate (N=62)” and “Mycophenolate Mofetil (N=56).”
- **Comparison / logical chain:** For each treatment, eTable 8's displayed population exceeds both Figure 1 and Table 2's described continuing-after-success population by 2 patients: methotrexate `62 − 60 = 2`; mycophenolate mofetil `56 − 54 = 2`.
- **Bounded impact:** This affects the stated denominator for every eTable 8 adverse-event percentage and leaves four additional participants unexplained by the displayed cohort descriptions. The evidence does not establish which denominator is correct; eTable 8 could represent a differently defined safety population that is not stated.
- **Human verification:**
  1. Check the eTable 8 analysis dataset and inclusion rule for the 62 and 56 participants.
  2. Compare that rule with Figure 1 and Table 2 footnote g (six-month success followed by continuing the same treatment).
  3. If the cohorts are identical, one set of denominators requires correction; if eTable 8 is a distinct safety population, an explicit caption/footnote defining the extra two participants per arm resolves the presentation inconsistency.

## Candidate 4 — Main Table 3 displays an n=109 header while its mycophenolate percentages use 108

- **Category / severity:** Presentation inconsistency / low (candidate; the footnote indicates why one patient may be excluded but does not identify the percentage denominator).
- **Issue statement:** Table 3 labels the mycophenolate-mofetil column “n = 109,” but visible count/percentage pairs are calculated with 108 recipients, so the displayed column header does not state the denominator used for its percentages.
- **Exact locations and evidence:**
  - `JAMA2019-12618-MAIN`, `jama_rathinam_2019_oi_190092.pdf`, PDF p. 8, Table 3 header: “Mycophenolate Mofetil (n = 109)” under “No. (%) of Patients Reporting ≥1 Adverse Event.” Table 3 reports, among others, ocular hypertension “13 (12.0),” decrease in vision “19 (17.6),” and systemic infection “27 (25.0).” Footnote b says one participant “never received mycophenolate mofetil.”
  - `JAMA2019-12618-SUPP-RESULTS`, `joi190092supp1_prod.pdf`, PDF p. 10, eTable 4 explicitly labels the recipient cohort “Mycophenolate Mofetil (N=108)” and repeats decrease in vision as “19 (17.6).”
- **Calculation:** With the header n=109, `13/109 × 100 = 11.9%`, `19/109 × 100 = 17.4%`, and `27/109 × 100 = 24.8%` (one decimal). With n=108, those values are 12.0%, 17.6%, and 25.0%, exactly matching Table 3. Thus the visible percentages use 108, not the header's 109.
- **Bounded impact:** The reported adverse-event counts are not contradicted; the ambiguity is the percentage denominator for the complete Table 3 mycophenolate column.
- **Human verification:**
  1. Confirm whether Table 3 is intended to report percentages among randomized patients (109) or medication recipients (108).
  2. If recipient-based, revise the header or add an explicit denominator note; if randomized-population based, recompute the displayed percentages.
  3. Verify the decision across Table 3 and the related six-month eTables 4–6 to ensure a consistent labeling convention.
