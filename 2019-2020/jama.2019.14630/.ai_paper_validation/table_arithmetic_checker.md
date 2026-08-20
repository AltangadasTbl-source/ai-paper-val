# Table arithmetic and internal-consistency check

**Scope.** Result-relevant tables only: DOC-001 Tables 1–3 (PDF pp. 4, 5, and 7–8) and DOC-004 eTables 2–9 (PDF pp. 3–7 and 9–24). Native normalized text was checked against source renders for the three candidates below (DOC-004 p. 7 and p. 10; DOC-001 p. 7 and DOC-004 p. 21). No OCR was used. Modeled between-group contrasts were not treated as simple arithmetic errors when their apparent difference was compatible with rounding or model adjustment.

## Candidate issues for verification

### 1. Reported red-wine median lies above its displayed IQR upper bound

- **Category / severity:** Arithmetic inconsistency / high-confidence presentation error.
- **Location:** DOC-004, `joi190106supp3_prod_1635377898.49725.pdf`, PDF p. 7, Supplemental eTable 2 (continuation), *Red wine (g/week)*, *Baseline, median (IQR)*, intervention-group column (N=3,272).
- **Reported source value:** `33 (0, 29)` g/week. The control column on the same row reads `4 (0, 29)`.
- **Comparator and calculation:** By the row label, the first value is the median and the parentheses are the IQR endpoints. A median must fall within the inclusive interval from Q1 to Q3. Here, `33 > 29`, so `33 − 29 = 4 g/week` above the printed upper quartile. No rounding tolerance can reconcile a displayed integer median with an upper IQR bound four whole g/week lower.
- **Bounded impact:** The intervention-group baseline red-wine summary in this table is internally impossible; this does not establish the intended value or alter the reported 6- or 12-month contrasts.
- **Verification steps:**
  1. Inspect the PDF p. 7 source table (render `document_outputs/DOC-004-supplement-3-results/page_images/table_check-07.png`) to confirm it prints `33 (0, 29)`.
  2. Check the table production source or analysis output for the intended intervention median/IQR; the issue is confirmed if the displayed values remain as printed.

### 2. A three-number baseline summary is labelled as mean (SD)

- **Category / severity:** Presentation inconsistency / high-confidence labelling error.
- **Location:** DOC-004, `joi190106supp3_prod_1635377898.49725.pdf`, PDF p. 10, Supplemental eTable 4, *Total olive oil (g/week)*, *Baseline, mean (SD)* row, intervention and control columns.
- **Reported source values:** Intervention `350 (175, 350)`; control `350 (175, 350)`.
- **Comparator and calculation:** A mean (SD) consists of a central value and one dispersion value, whereas the displayed parenthesis contains two comma-separated values. The immediately following food rows use the same three-number form under labels explicitly reading *median (IQR)*, e.g. refined olive oil `0 (0, 70)`. Thus `350 (175, 350)` is structurally an IQR-style summary but is labelled *mean (SD)*.
- **Bounded impact:** The baseline total-olive-oil summary’s statistical descriptor is ambiguous/mislabeled. The follow-up changes and between-group differences are unaffected by this label-only observation.
- **Verification steps:**
  1. Inspect PDF p. 10 (render `document_outputs/DOC-004-supplement-3-results/page_images/table_check-10.png`) to confirm the label and both displayed values.
  2. Verify in the table-generation output whether the intended label is *median (IQR)* or whether a missing/incorrect SD format was introduced in typesetting.

### 3. Intervention baseline energy-intake SD differs between two tables that state the same all-randomized sample

- **Category / severity:** Cross-document inconsistency / high-confidence numerical discrepancy, underlying intended value uncertain.
- **Locations:**
  - DOC-001, `jama_saynorea_2019_oi_190106_1635377898.43062.pdf`, PDF p. 7, Table 3, *Total Energy, Mean (SD), kcal/d*, *Baseline*, intervention group, `n=3272`.
  - DOC-004, `joi190106supp3_prod_1635377898.49725.pdf`, PDF p. 21, Supplemental eTable 8, *Total energy Intake (kcal/d)*, *Baseline, mean (SD)*, intervention group, `n=3,272`; the table describes all randomized participants with missing values replaced by baseline values.
- **Reported versus comparator:** Table 3 reports `2355 (555)` kcal/d; eTable 8 reports `2,355 (544)` kcal/d. Both report the same intervention sample size (3,272), the same mean (2,355), and the same baseline measure. The control baseline is `2369 (555)` in both tables.
- **Calculation / tolerance:** Difference in the reported intervention SD is `555 − 544 = 11 kcal/d`; this is not a rounding difference at the displayed whole-kcal precision. Because the eTable’s stated sensitivity procedure replaces *follow-up* missing values with baseline values, it does not itself describe a different baseline intervention sample.
- **Bounded impact:** The intervention baseline total-energy variability is reported inconsistently between the main and sensitivity tables. This finding does not identify which SD is correct and does not by itself invalidate the reported changes or treatment contrast.
- **Verification steps:**
  1. Inspect DOC-001 Table 3 PDF p. 7 (render `document_outputs/DOC-001-main-article/page_images/table_check-07.png`) and DOC-004 eTable 8 PDF p. 21 (render `document_outputs/DOC-004-supplement-3-results/page_images/table_check-21.png`) to confirm the printed SDs and identical Ns.
  2. Re-run or inspect the baseline descriptive output for the intervention N=3,272 cohort. The issue resolves if a documented cohort/variable-definition difference explains the SD; otherwise the unequal published values remain a reporting discrepancy.

## Checks with no candidate retained

- DOC-001 Table 1: sex and education subgroup counts sum to their displayed denominators; percentages are consistent with whole-percent rounding.
- DOC-001 Table 2 and DOC-004 eTables 2–9: visible treatment-contrast point estimates were checked against the two displayed group estimates. Apparent one-unit differences were compatible with rounding and/or the tables’ stated mixed-effects models, so none was retained as an arithmetic error.
- DOC-001 Table 3 and DOC-004 eTables 5 and 8: no other repeated baseline values with a non-rounding discrepancy were located in the reviewed cells.
