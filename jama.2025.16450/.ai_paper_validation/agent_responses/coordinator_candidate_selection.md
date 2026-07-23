# Coordinator candidate selection

- Package: `jama.2025.16450`
- Candidate limit: 10
- Unique candidates selected: 5
- Selection basis: deduplicated outputs from the table-arithmetic, figure-flow, and statistical-consistency checks.
- Scientific scope: main article and results supplement only. Protocol, Manual of Operations, and SAP remain Not Audited by Design.

## Candidates sent to evidence verification

### C-01 — eTable 1 GDB-status percentages use unstated smaller denominators

- Source agents: `TA-02`, figure-flow candidate 1 (deduplicated).
- Proposed category: Presentation inconsistency.
- Location: `joi250072supp4_prod_1761000786.6988.pdf`, PDF p.2, eTable 1, GDB-status rows.
- Evidence: header denominators are 641, 635, 635, and 617, but displayed status counts sum to 631, 628, 628, and 612. Printed percentages use the smaller totals, leaving 10, 7, 7, and 5 participants without a displayed status or denominator note.
- Verification focus: inspect the original table image and all footnotes; confirm the arithmetic and absence of a missing/nonmissing-denominator disclosure.

### C-02 — eTable 3 B+S percentages imply n=321 despite a displayed n=322 header

- Source agent: `TA-03`.
- Proposed category: Presentation inconsistency.
- Location: `joi250072supp4_prod_1761000786.6988.pdf`, PDF p.5, eTable 3, B+S column.
- Evidence: 242 (75.4), 240 (74.8), 214 (66.7), and 22 (6.9) match denominator 321 rather than header n=322. No alternate denominator is stated in eTable 3.
- Verification focus: inspect the original table and footnotes; determine whether a row-specific or nonmissing denominator resolves the apparent mismatch.

### C-03 — Baseline FIO2 control-arm denominator differs between Table 1 and Figure 2

- Source agent: `SC-01`.
- Proposed category: Presentation inconsistency.
- Location: `jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf`, PDF p.6 Table 1 and PDF p.9 Figure 2.
- Evidence: Table 1 gives control baseline FIO2 n=230, including 81 at FIO2 >=0.50, implying 149 below 0.50. Figure 2 gives 150 below 0.50 and 81 at or above 0.50, totaling 231.
- Verification focus: inspect original Table 1 and Figure 2 images and their footnotes; confirm that the same baseline variable/population is intended and that no visible note explains the extra participant.

### C-04 — eTable 4 expands RR as “risk difference”

- Source agent: `SC-02`.
- Proposed category: Presentation inconsistency.
- Location: `joi250072supp4_prod_1761000786.6988.pdf`, PDF pp.7-8, eTable 4.
- Evidence: the table header and methods describe relative risks and label estimates RR, while the abbreviation line says `RR = risk difference`; the main article separately uses `RD` for risk difference.
- Verification focus: inspect the original header, abbreviation line, and methods note; confirm the exact visible wording.

### C-05 — 120-day death counts differ within the displayed safety population

- Source agent: `TA-01`; disputed by figure-flow checker.
- Proposed category: Arithmetic inconsistency.
- Coordinator priority: Uncertain pending verification.
- Location: `joi250072supp4_prod_1761000786.6988.pdf`, PDF p.2 eTable 1, PDF p.7 eTable 4, and PDF p.15 eTable 8.
- Evidence: eTable 1 shows 86 deaths in SAF; eTables 4 and 8 show 50/321 plus 44/313 = 94.
- Competing interpretation: “GDB status” may be a non-equivalent categorical status/database measure rather than the all-cause death outcome, and transferred or status-timing rules may explain the difference.
- Verification focus: use only visible supplied-document definitions and footnotes. Accept only if the source explicitly establishes equivalence of population, outcome definition, and timepoint; otherwise classify Rejected or Uncertain.

## Checker-level rejected or uncertain interpretations retained for the final audit trail

- Figure 1 “5 vs 6 untreated”: Rejected; endpoint overlap reconciles the apparent difference.
- Figure 1 sensitivity analysis 319 vs eTable 1 population 320: Rejected; analyzed nonmissing denominator differs from population membership.
- ITT-excluding-untreated 635 vs Table 2 analyzed 634: Rejected; eTable 1 documents one missing/early-ended endpoint.
- Main versus supplement death counts at 36 weeks: Rejected; the compared values use different as-randomized versus as-treated populations.
- “Other” race subgroup adjusted direction versus crude proportions: Uncertain; model-dependent and not verifiable from supplied aggregate output.
- CI/null/P-value checks: Rejected; no contradiction located.
- Native-text minus-sign mojibake: Rejected extraction artifact after visual comparison.
