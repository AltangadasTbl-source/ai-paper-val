# Human Adjudication Report - JAMA 2025.16450

Prepared solely from the supplied package. This screen is not a legal opinion. Processing continued because user/institutional permission was reported; that does not alter the supplied-material rights classifications.

## Package Manifest

| Document ID | Source PDF | Pages | Classification | Scientific audit status / scope |
|---|---|---:|---|---|
| JAMA2025-16450-MAIN | `jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf` | 11 | Main article | Audited, pp. 1-11 |
| JAMA2025-16450-SUPP01-PROTOCOL | `joi250072supp1_prod_1761000786.68881.pdf` | 35 | Protocol | **Not Audited by Design**; no result-page scope |
| JAMA2025-16450-SUPP02-MANUAL | `joi250072supp2_prod_1761000786.6938.pdf` | 162 | Manual of Operations / administrative | **Not Audited by Design**; no result-page scope |
| JAMA2025-16450-SUPP03-SAP | `joi250072supp3_prod_1761000786.6988.pdf` | 48 | Statistical analysis plan | **Not Audited by Design**; no result-page scope |
| JAMA2025-16450-SUPP04-RESULTS | `joi250072supp4_prod_1761000786.6988.pdf` | 16 | Results supplement | Audited, pp. 1-16 (eTables 1-8) |

Protocol, manual, and SAP records are explicitly Not Audited by Design: no scientific extraction, OCR, rendering, or checking was performed. They may be opened only for a specifically requested targeted comparison.

## AI Training Restriction Summary

| Document ID | Status | Exact evidence location | Human Compliance Review |
|---|---|---|---|
| JAMA2025-16450-MAIN | Explicit AI Training Restriction | PDF pp. 1-11, repeated footer: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Yes |
| JAMA2025-16450-SUPP01-PROTOCOL | No AI Training Restriction Located in Provided Materials | Metadata; PDF pp. 1-2 and 34-35; focused keyword screen found no copyright, license, rights, TDM, or AI-use language. | No |
| JAMA2025-16450-SUPP02-MANUAL | No AI Training Restriction Located in Provided Materials | Metadata; PDF pp. 1-2 and 161-162; focused keyword screen found no copyright, license, rights, TDM, or AI-use language. | No |
| JAMA2025-16450-SUPP03-SAP | No AI Training Restriction Located in Provided Materials | Metadata; PDF pp. 1-2 and 47-48; focused keyword screen found no copyright, license, rights, TDM, or AI-use language. | No |
| JAMA2025-16450-SUPP04-RESULTS | Explicit AI Training Restriction | PDF pp. 1-16, repeated footer: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Yes |

For records marked "No AI Training Restriction Located," the supplied-material absence finding is not permission. This compliance summary is separate from the scientific findings.

## Scientific Findings

### C-01 - Undisclosed GDB-status denominators

- **Category / severity:** Presentation inconsistency / Minor.
- **Exact location:** Results supplement, PDF p. 2, eTable 1, "GDB status (up to 120 days postnatal age), n (%)" and footnotes.
- **Compared values:** Headers: ITT 641, ITT excluding untreated 635, SAF 635, PP 617. Status counts respectively: 340+189+16+86=631; 337+189+16+86=628; 337+189+16+86=628; 329+184+15+84=612. No nonmissing denominator or missing/unknown row is displayed.
- **Calculation / logical basis:** Printed percentages use the row sums: 340/631=53.9% (not 340/641=53.0%); 337/628=53.7% (not 337/635=53.1%); 329/612=53.8% (not 329/617=53.3%). The undisclosed differences are 10, 7, 7, and 5 participants.
- **Verification instruction:** Sum the four status rows per column; recompute using both header and row-sum denominators; confirm whether to add nonmissing denominators or a missing/unknown row.

### C-02 - eTable 3 B+S percentages imply n=321, not header n=322

- **Category / severity:** Presentation inconsistency / Minor.
- **Exact location:** Results supplement, PDF p. 5, eTable 3, Budesonide + Surfactant column; complete notes, PDF p. 6.
- **Compared values:** Header `n=322`; cells: 242 (75.4), 240 (74.8), 214 (66.7), and 22 (6.9). Notes give no alternate denominator.
- **Calculation / logical basis:** At 322: 242/322=75.2%, 240/322=74.5%, 214/322=66.5%, 22/322=6.8%. At 321, each reproduces the printed percentage to one decimal: 75.4%, 74.8%, 66.7%, 6.9%.
- **Verification instruction:** Compare the p. 5 header/cells with p. 6 notes; confirm whether the denominator is 321 and disclose it (or use n/N), otherwise correct the header or percentages.

### C-03 - Baseline FIO2 control-arm total differs between Table 1 and Figure 2

- **Category / severity:** Presentation inconsistency / Minor.
- **Exact location:** Main article, PDF p. 6 / printed p. 1457, Table 1 "FIO2 at baseline" and "High FIO2 (>=0.5)"; PDF p. 9 / printed p. 1460, Figure 2 "Baseline FIO2" and footnote c.
- **Compared values:** Table 1: B+S n=228, high 86/228; surfactant-alone n=230, high 81/230. Figure 2: B+S <0.50=142 and >=0.50=86; surfactant-alone <0.50=150 and >=0.50=81. Both describe last pretreatment FIO2.
- **Calculation / logical basis:** B+S reconciles: 142+86=228. Table 1 implies surfactant-alone <0.50=230-81=149; Figure 2 reports 150 and totals 231. Figure 2 total=459=641-182 excluded; Table 1 total=458. No visible note explains the one-participant difference.
- **Verification instruction:** Compare Table 1 with Figure 2 and footnote c; check the subgroup input to establish whether surfactant-alone <0.50 is 149 or 150.

### C-04 - eTable 4 expands RR as "risk difference"

- **Category / severity:** Presentation inconsistency / Minor.
- **Exact location:** Results supplement, PDF p. 7, eTable 4 header and RR-labelled binary estimates; PDF p. 8, abbreviation line and binary-outcome methods note.
- **Compared statements:** Header: "Relative Risk (RR) or Mean Difference (MD) (95% CI)"; binary rows use RR; methods: binary outcomes report relative risks estimated by robust Poisson regression; abbreviation line: `RR = risk difference`.
- **Logical basis:** The abbreviation conflicts with the header, estimate labels, and methods. Main article PDF p. 8 / printed p. 1459, Table 3, separately defines RD as risk difference and RR as relative risk.
- **Verification instruction:** Compare the p. 7 header/RR estimates with the p. 8 abbreviation and methods lines; if confirmed, change the expansion to `RR = relative risk`.

## Rejected and Uncertain Candidates

| ID | Disposition | Exact location / compared values | Basis | Verification instruction |
|---|---|---|---|---|
| C-05 | Rejected | Results supplement pp. 2, 7-8, 15-16: eTable 1 SAF GDB "Death"=86/628 displayed statuses; eTables 4 and 8 death=50/321+44/313=94/634. | GDB is a mutually exclusive disposition distribution; eTables 4/8 are cumulative all-cause in-hospital death and use a different nonmissing subset. Equivalence is not established. | Compare the definitions on pp. 2, 8, and 15; do not require 86=94 without participant-level status-to-death mapping. |
| R-01 | Rejected | Main p. 7/Table 2 and supplement p. 2: ITT-excluding-untreated=635 vs analyzed 319+315=634. | eTable 1 documents 634/635 primary-endpoint completions and one early end. | Confirm population membership separately from observed-endpoint denominator. |
| R-02 | Rejected | Main p. 7/Table 2 vs supplement p. 15/eTable 8: 49/321 and 42/318 vs 48/321 and 41/313. | As-randomized/ITT and as-treated/safety populations differ. | Compare population definitions before treating counts as contradictory. |
| U-01 | Uncertain | Main p. 9/Figure 2 "Other" race subgroup: crude 7/21 vs 4/17; adjusted RR 0.93 (0.33-2.66). | Aggregate output cannot verify an adjusted robust-Poisson estimate; adjustment may change direction. | Review model strata/output if an adjustment-specific check is requested. |
| R-03 | Rejected | Main pp. 1-2, 6-9; supplement pp. 5-8. | Reviewed CIs, nulls, and P values were compatible; no contradiction located. | No corrective action indicated from the reviewed displays. |
| Flow checks | Rejected | Main p. 4/Figure 1; main p. 7/Table 2; supplement p. 2/eTable 1. | Apparent untreated and sensitivity denominators reconcile through endpoint overlap and nonmissing endpoint counts. | Retain population-vs-analysis distinction in any recheck. |
| Extraction signs | Rejected | Native extracted main Tables 2-3 text. | Minus-sign mojibake was an extraction artifact; visual table renders resolved it. | Use the visual PDF/table render, not mangled native text. |

## Human Adjudication Checklist

- [ ] Confirm C-01 through C-04 against the cited PDF pages and calculations.
- [ ] Decide and document the correction for each confirmed presentation issue; do not infer an unverified underlying-data correction.
- [ ] Confirm that C-05 and the listed rejected/uncertain items remain outside the scientific-issue list unless new supplied-document evidence establishes the missing equivalence or model output.
- [ ] Record acknowledgement of the two Human Compliance Review flags and the reported institutional permission; this report makes no legal conclusion.
- [ ] Preserve the Not Audited by Design status for protocol, manual, and SAP unless a specific comparison is authorized.
