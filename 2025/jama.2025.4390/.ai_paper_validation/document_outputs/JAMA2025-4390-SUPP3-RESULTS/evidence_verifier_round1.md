# Evidence Verifier - Results Supplement Copy, Round 1

- Document ID: `JAMA2025-4390-SUPP3-RESULTS`
- Source PDF: `joi250019supp3_prod_1749674951.30054.pdf`
- Package response: `.ai_paper_validation/agent_outputs/evidence_verifier_round1.md`
- Relevant verified candidates: `TAC-01`, `SCI-03`, `FFC-01`, `FFC-02`, `FFC-03`
- Round outcome for this document: **5 Verified; 0 Uncertain; 0 Rejected**

## TAC-01 - Verified

- **Location:** PDF p. 37, eTable 5, `Ethnicity - no. (%)`, `White/Caucasian` and `Other`.
- **Evidence:** Morning n=44 has `40 (90.9)` in both rows; bedtime n=57 has `53 (93.0)` in both rows. All eight displayed ethnicity rows sum to 85 and 111, or 193.2% and 194.7%. The full-cohort eTable 3 ethnicity categories on p. 29 partition exactly to their allocation totals and no eTable 5 footnote authorizes overlap.
- **Basis:** The `Other` cells visibly duplicate the `White/Caucasian` cells in both groups.
- **Human check:** Inspect the eTable 5 source export for the intended `Other` cells or row placement.

## SCI-03 - Verified

- **Location:** PDF p. 39, eTable 5, `Type of BP-lowering med - no. (%)`; denominators on p. 37.
- **Evidence:** With morning n=44 and bedtime n=57, both `Diuretic` and `Combination BP med` show `9 (20.5)` versus `16 (28.1)`, but P values are 0.34 and 0.38.
- **Basis:** The displayed 2-by-2 cells are identical (9/35 versus 16/41), yet the table states no different denominator, adjustment, or row-specific procedure. The same unadjusted binary comparison must return the same P value.
- **Human check:** Re-run or inspect both source comparisons and identify whether a count or P value is wrong.

## FFC-01 - Verified

- **Location:** PDF p. 22, eFigure 1, British Columbia column; comparison: eTable 1 p. 27.
- **Evidence:** British Columbia header is 43, while its 14 city counts sum to 44. Province headers `43+326+22+29+16` sum to 436, matching the 436 PCPs reported in eTable 1.
- **Basis:** The British Columbia city list exceeds its header by one.
- **Human check:** Recount p. 22 and inspect the figure source data to identify the incorrect header or city count.

## FFC-02 - Verified

- **Location:** PDF p. 26, eFigure 4, bedtime/PM diuretic bar; comparison: eTable 6 p. 42.
- **Evidence:** Figure: `278/138/8`; table: `277/139/8` for as allocated/off allocation/twice or more daily. Both sum to n=424.
- **Basis:** One medication is assigned differently between the first two categories.
- **Human check:** Compare the figure and table with the 6-month medication-timing source export.

## FFC-03 - Verified

- **Location:** PDF p. 32, eTable 3, `Calcium channel blocker`; comparison: main article Table 1, PDF p. 6.
- **Evidence:** Bedtime n=1677 and `479 (28.2)` in both tables. `479/1677*100 = 28.5629%`, which rounds to 28.6%, not 28.2%. Morning and overall cells reconcile.
- **Basis:** The same one-decimal arithmetic error is repeated in both documents.
- **Human check:** Confirm the intended count and denominator in the source table and correct the repeated cell.
