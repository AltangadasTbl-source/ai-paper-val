# Table arithmetic and internal-consistency check

- Agent: `table_arithmetic_checker`
- Scope: result-relevant tables only: main-article Tables 1-3 and Supplement 4 eTables 1-8. Protocol, SAP, manual, and administrative material were not opened. Native page text was checked against the retained table renders for the cited Supplement 4 pages and main-article Table 2 page.
- Result: 3 document-verifiable candidates. No source PDF was modified.

## Candidates for verification

### TA-01 - 120-day death count conflicts within the safety population

- **Taxonomy:** Arithmetic inconsistency
- **Confidence:** High
- **Exact location:** `joi250072supp4_prod_1761000786.6988.pdf`, PDF p.2, eTable 1, SAF column, `GDB status (up to 120 days postnatal age) - Death`; PDF p.7, eTable 4, `Death before 120 days PNA`; and PDF p.15, eTable 8, `Died by 120 days PNA`.
- **Source values:** eTable 1 reports 86 deaths in SAF (n=635). eTables 4 and 8 each report 50/321 deaths in B+S and 44/313 in SA.
- **Calculation:** 50 + 44 = **94**, which is 8 greater than eTable 1's **86** for the same as-treated safety population and 120-day timepoint.
- **Reasoning:** The eTable 1 row and eTables 4/8 each identify the safety population and a 120-day postnatal-age death status; the supplied tables do not state a differing analysis subset that resolves 86 vs 94.
- **Verification instruction:** Confirm the intended SAF death count and any distinct data cutoff/subset. Correct the eTable 1 death row or label the relevant differing population/timepoint.

### TA-02 - eTable 1 GDB-status percentages use undisclosed denominators rather than the displayed column n

- **Taxonomy:** Presentation inconsistency
- **Confidence:** High
- **Exact location:** `joi250072supp4_prod_1761000786.6988.pdf`, PDF p.2, eTable 1, `GDB status (up to 120 days postnatal age), n (%)`, all four population columns.
- **Source values and calculation:**
  - ITT header n=641; status counts 340 + 189 + 16 + 86 = **631**, while the printed percentages 53.9 + 30.0 + 2.5 + 13.6 = **100.0%**. For example, 340/641=53.0%, not 53.9%; 340/631=53.9%.
  - ITT excluding untreated and SAF headers n=635; each has 337 + 189 + 16 + 86 = **628**. For example, 337/635=53.1%, not 53.7%; 337/628=53.7%.
  - PP header n=617; 329 + 184 + 15 + 84 = **612**. 329/617=53.3%, not 53.8%; 329/612=53.8%.
- **Reasoning:** The row is labeled `n (%)` under columns with stated n values, but the displayed percentages consistently use smaller unreported denominators (631, 628, and 612). No missing-GDB-status category or denominator note is printed in the table.
- **Verification instruction:** Confirm whether 10, 7, 7, and 5 participants respectively lack GDB status, then add the nonmissing denominators/missing category or recompute the percentages against the displayed column n.

### TA-03 - eTable 3 B+S percentages conflict with its displayed n=322 column header

- **Taxonomy:** Presentation inconsistency
- **Confidence:** High for the arithmetic mismatch; medium for the intended correction.
- **Exact location:** `joi250072supp4_prod_1761000786.6988.pdf`, PDF p.5, eTable 3, B+S column headed `n=322`; rows `Experienced Any AEs`, `Any of interest`, `Hyperglycemia`, and `Any fatal`.
- **Source values and calculation:** The table prints 242 (75.4), 240 (74.8), 214 (66.7), and 22 (6.9). Against the displayed n=322, these are 242/322=75.2%, 240/322=74.5%, 214/322=66.5%, and 22/322=6.8% (one decimal). The displayed percentages instead equal denominators of 321: 242/321=75.4%, 240/321=74.8%, 214/321=66.7%, and 22/321=6.9%.
- **Reasoning:** Unlike eTable 4, eTable 3 does not provide row-specific n/N values or a nonmissing-denominator note. Its stated B+S column n is therefore not the denominator supported by these visible percentages. eTable 8 separately shows 22/321 (6.9), which confirms the apparent alternate denominator for the fatal-SAE row but does not explain it in eTable 3.
- **Verification instruction:** Confirm whether B+S AE analyses intentionally used n=321. If so, label the nonmissing denominator in eTable 3 (or use n/N); otherwise correct the percentages/header.

## Checks completed without a candidate

- Main-article Table 1 category totals and visible n/total percentages reconcile after honoring the printed denominators; overlapping resuscitation rows were not summed.
- Main-article Tables 2-3 visible fractions and ordinal-category totals reconcile. Modeled risk/mean differences were not judged against unadjusted fractions.
- Supplement 4 eTable 2 one/two-dose totals, eTable 4 visible fractions, eTable 5 PP reconciliation (635 - [11+7] = 617), eTable 6 event-category/severity/relationship/action/outcome totals, eTable 7 corresponding event totals, and eTable 8 primary-cause totals all reconcile.
- **Rejected extraction artifact:** native text renders minus signs in main-article Tables 2-3 as mojibake (`鈭?`). The retained visual rendering confirms the signs in Table 2; this extraction artifact is not a reporting candidate. No conclusion was drawn from the ambiguously extracted signed Table 3 mean-difference cells.
