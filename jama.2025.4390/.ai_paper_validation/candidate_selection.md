# Coordinator Candidate Selection

- Package: `jama.2025.4390`
- Selection stage: post-checker deduplication, pre-verification
- Unique candidates selected: 7 of maximum 10
- Verification round authorized: 1 of maximum 2

| Candidate | Category | Primary location | Concise basis |
|---|---|---|---|
| TAC-01 | Presentation inconsistency | Results supplement PDF p. 37, eTable 5, Ethnicity | `Other` duplicates `White/Caucasian` in both allocation groups, producing impossible displayed ethnicity totals. |
| SCI-01 | Presentation inconsistency | Main article PDF p. 9, Figure 3; Table 2 p. 8 | Columns headed `Rate per 100 patient-years` contain 71.0 values that behave as hundreds of patient-years, while Table 2 rates are 2.30 and 2.44. |
| SCI-02 | Statistical reporting inconsistency | Main article PDF p. 9, Figure 3; Results p. 6 and Table 2 p. 8 | Figure says all confidence intervals are unadjusted, but the all-patients CI repeats the adjusted primary result. |
| SCI-03 | Statistical reporting inconsistency | Results supplement PDF p. 39, eTable 5 | Two rows with identical counts and group denominators report different P values. |
| FFC-01 | Arithmetic inconsistency | Results supplement PDF p. 22, eFigure 1 | British Columbia city counts sum to 44 while the province header reports 43. |
| FFC-02 | Presentation inconsistency | Results supplement PDF p. 26, eFigure 4; eTable 6 p. 42 | Bedtime diuretic categories are 278/138/8 in the figure versus 277/139/8 in the table. |
| FFC-03 | Arithmetic inconsistency | Main article PDF p. 6, Table 1; results supplement PDF p. 32, eTable 3 | `479/1677` is printed as 28.2% in both places; it calculates to 28.6% rounded to one decimal. |

## Deduplication record

- Figure/flow corroborations of `SCI-01`, `SCI-02`, and `TAC-01` were merged into those candidates.
- No protocol or SAP candidate was selected; those documents remain `Not Audited by Design`.
