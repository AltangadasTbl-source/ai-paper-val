# Table arithmetic check — JAMA2019-12618-SUPP-RESULTS

## Scope and outcome

- **Source:** `joi190092supp1_prod.pdf` (read only).
- **Result-relevant tables audited:** eTable 2 (PDF p. 8), eTables 4–6 (PDF pp. 10–12), eTable 7 (PDF p. 13), and eTables 8–9 (PDF pp. 14–16), as classified in the package manifest and `result_relevant_evidence_map.md`.
- **Excluded by design:** eTable 1 (adverse-event definitions) and eTable 3 (dose-reduction guidance), which are methods/administrative tables rather than reported-result tables.
- **Checks performed:** visible numerators, denominators, percentages, enrollment total/percent total, repeated values, and adjacent-column relationships. eTable 2 totals reconcile (`216`; displayed whole-percent entries sum to `100%`). All assessed number/percent cells in eTables 4–8 reconcile with their stated denominators and ordinary rounding. eTable 9 produced the one candidate below.
- **Rounding rule used:** for a value displayed to one decimal percent, the acceptable ordinary nearest-tenth interval is the displayed value plus or minus 0.05 percentage points.

## Candidate TA-02 — eTable 9 percentage uses an incompatible denominator

- **Category / severity:** Arithmetic inconsistency / Minor.
- **Issue statement:** The mycophenolate mofetil percentage for serious systemic diarrhea is incompatible with its visible numerator `1` and column denominator `N = 20`.
- **Exact location:** `JAMA2019-12618-SUPP-RESULTS`; `joi190092supp1_prod.pdf`, PDF page 15; **eTable 9**, *Serious Systemic* section, row **“Diarrheaᵇ”**, **Mycophenolate Mofetil (N=20)** column.
- **Source values (verbatim):** Table header: `Mycophenolate Mofetil (N=20)`. Measurement header: `Number of Patients Reporting at Least One Event (%)`. Target cell: `1 (3.4)`.
- **Calculation:** `1 / 20 × 100 = 5.0%`. The displayed `3.4%` differs by `1.6` percentage points and is outside its rounding interval `[3.35%, 3.45%)`. By comparison, `1 / 29 × 100 = 3.448…%`, which rounds to `3.4%` and is the percentage associated with a one-patient cell in the adjacent methotrexate `(N=29)` column.
- **Concise reasoning:** The count, percentage, and denominator are visibly supplied in the same eTable. A count of one among 20 participants must display as 5.0% to one decimal; no ordinary rounding tolerance can produce 3.4%. The adjacent-column relationship makes a denominator/copying error a document-grounded possibility, but the source alone cannot determine which printed field should change.
- **Bounded impact:** The inconsistency is confined to the displayed percentage for this serious-adverse-event cell. It does not alter the visible count of one or establish any unreported patient-level fact.
- **Human verification steps:**
  1. Confirm that the PDF places `1 (3.4)` in the *Mycophenolate Mofetil (N=20)* column, rather than the adjacent methotrexate `(N=29)` column.
  2. Compute `1 ÷ 20 × 100`; a result of `5.0%` confirms the arithmetic inconsistency. Check the publication production source or an erratum only if authorized to determine whether the intended correction is the percentage, count, or denominator.
