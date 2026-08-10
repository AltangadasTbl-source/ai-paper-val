# Figure and participant-flow check

- Agent: `figure_flow_checker`
- Audited documents: `JAMA2025-16450-MAIN` and `JAMA2025-16450-SUPP04-RESULTS`
- Scope: main-article Figure 1, nearby participant-flow text, main Tables 1-2 denominator propagation, Supplement 4 eTables 1, 2, 5, and 8, and their retained page images.
- Excluded by design: protocol, manual of operations, and SAP.

## Candidate finding 1

- **Status:** Candidate
- **Taxonomy:** Presentation inconsistency
- **Confidence:** High
- **Location:** `joi250072supp4_prod_1761000786.6988.pdf`, PDF page 2, eTable 1, "GDB status (up to 120 days postnatal age), n (%)".
- **Visible evidence:** The eTable column headers give ITT `n=641`, ITT excluding untreated `n=635`, SAF `n=635`, and PP `n=617`. The four displayed GDB-status rows are:
  - ITT: discharged 340, still hospitalized 189, transferred 16, death 86.
  - ITT excluding untreated: 337, 189, 16, 86.
  - SAF: 337, 189, 16, 86.
  - PP: 329, 184, 15, 84.
  No missing/unknown-status row or alternate denominator is printed in the table or footnotes.
- **Calculation / logical basis:** The displayed status counts total `631`, `628`, `628`, and `612`, respectively, rather than the column populations `641`, `635`, `635`, and `617`. Thus `10`, `7`, `7`, and `5` participants are not represented in the disposition rows. The printed percentages are calculated from the smaller unstated totals, not the stated column denominators: for example, ITT `340/631=53.9%`, `189/631=30.0%`, `16/631=2.5%`, and `86/631=13.6%`; using `n=641` would give different percentages. The same pattern holds for the other three columns.
- **Why this is local and document-verifiable:** The count sums, column denominators, percentages, and absence of a missing-status explanation are all directly visible in eTable 1. The issue is incomplete denominator labeling/accounting, not an inference about participants' true outcomes.
- **Concise verification instruction:** On Supplement 4 PDF page 2, sum the four GDB-status rows in each population column and recompute their percentages using both the column-header `n` and the row-sum denominator; then confirm whether a missing/unknown row or a nonmissing-denominator footnote was omitted.

## Rejected interpretations

1. **Figure 1 "5 vs 6 untreated" - Rejected as unsupported.**  
   Main article PDF page 4, Figure 1 shows 3 untreated infants in each randomized arm (6 total), while footnote j says the primary model for the untreated-excluded sensitivity analysis "also excluded" 5 untreated participants. This is reconciled by the visible endpoint overlap: the main ITT analysis has 639 observed primary endpoints, and the untreated-excluded analysis has 634 observed endpoints, while Supplement 4 eTable 1 defines the full untreated-excluded population as 635 with 1 endpoint ending early. One untreated infant was already among the two participants without a primary endpoint. Main text on PDF page 7 also correctly states that the population excluded 6 untreated infants. No contradiction retained.

2. **Figure 1 sensitivity-analysis arm count 319 vs eTable 1 population count 320 - Rejected as unsupported.**  
   Main article PDF page 4, Figure 1 reports 319 budesonide-group participants included in the primary sensitivity analysis, and Table 2 on PDF page 7 reports `218/319`; Supplement 4 eTable 1 reports 320 members in that randomized-treatment population but only 634/635 endpoint completions overall. The values describe analyzed participants with observed endpoints versus population membership and are compatible.

3. **eTable 1 GDB deaths 86 vs eTable 8 deaths by 120 days 94 - Rejected as ambiguous.**  
   Supplement 4 PDF page 2 reports a categorical "GDB status" count of 86 deaths, whereas PDF page 15 eTable 8 reports 50+44=94 all-cause in-hospital deaths through 120 days. The supplied pages do not establish that the GDB disposition category and the death outcome must be identical; transferred status or database-status timing could make the measures non-equivalent. No contradiction retained without inferring beyond the document.

## Flow checks with no retained issue

- Figure 1 arithmetic is internally consistent: `5353-4711=642`; exclusions `3000+1268+443=4711`; post-withdrawal randomized groups `323+318=641`; budesonide-arm treatment categories `319+1+3=323`; surfactant-arm categories `312+3+3=318`; primary-analysis groups `321+318=639`.
- Figure 1 and Supplement 4 eTable 1 consistently propagate the six untreated infants: `641-6=635`. The as-treated safety groups also reconcile with crossovers: budesonide plus surfactant `319+3=322`, surfactant alone `312+1=313`.
- The per-protocol population reconciles across the main text and Supplement 4: `635-18=617`, with eTable 5 reporting 11+7=18 participants with any major deviation/violation.
