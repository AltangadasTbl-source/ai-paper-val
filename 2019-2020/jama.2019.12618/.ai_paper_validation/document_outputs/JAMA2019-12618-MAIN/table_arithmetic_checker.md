# Table arithmetic check — JAMA2019-12618-MAIN

## Scope and outcome

- **Source:** `jama_rathinam_2019_oi_190092.pdf` (read only).
- **Audited result-relevant tables:** Table 1 (PDF p. 5), Table 2 (PDF p. 6), and Table 3 (PDF p. 8).
- **Checks performed:** visible numerators, stated denominators, displayed percentages, category subtotals where the table supplied an assessable denominator, and adjacent treatment-column relationships. Table 1 and Table 2 produced no candidate issue from these checks. Table 3 produced the one candidate below.
- **Rounding rule used:** for a value displayed to one decimal percent, the acceptable ordinary nearest-tenth interval is the displayed value plus or minus 0.05 percentage points (with the usual half-way convention immaterial here).

## Candidate TA-01 — Table 3 percentage does not match the stated numerator and denominator

- **Category / severity:** Arithmetic inconsistency / Minor.
- **Issue statement:** The methotrexate percentage reported for nonserious elevated ALT or AST is inconsistent with the visible count `14` and the table header denominator `n = 107`.
- **Exact location:** `JAMA2019-12618-MAIN`; `jama_rathinam_2019_oi_190092.pdf`, PDF page 8; **Table 3**, *Nonserious laboratory* section, row **“Elevated ALT or AST (2 to 5 times upper limit of normal <28 d)”**, **Methotrexate (n = 107)** column.
- **Source values (verbatim):** Table header: `Methotrexate (n = 107)`. Target cell: `14 (13.0)` under the table measurement header `No. (%) of Patients Reporting ≥1 Adverse Event`.
- **Calculation:** `14 / 107 × 100 = 13.084112…%`, which rounds to **13.1%** to one decimal. The reported **13.0%** differs by `0.084112…` percentage points; it lies outside the 13.0% rounding interval `[12.95%, 13.05%)`.
- **Concise reasoning:** Both the numerator and denominator are printed in the same table, and the column is explicitly a number-and-percent patient measure. Thus the displayed percentage cannot be obtained by ordinary one-decimal rounding from the visible inputs.
- **Bounded impact:** This is a `0.1`-percentage-point display discrepancy limited to this adverse-event cell; the visible count remains 14 and no table total is derived from this percentage.
- **Human verification steps:**
  1. Confirm in the source PDF that the cell is `14 (13.0)` and that its column header is `Methotrexate (n = 107)`.
  2. Compute `14 ÷ 107 × 100`; a result of `13.084…%` confirms the candidate, while evidence of a different analysis denominator would resolve it.
