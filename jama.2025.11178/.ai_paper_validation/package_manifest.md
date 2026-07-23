# Package Manifest

Package: `jama.2025.11178`

Inventory date: 2026-07-22

Source files are preserved unchanged. Derived artifacts are restricted to `.ai_paper_validation/`.

| Document ID | Source file | Pages | Classification | Scientific audit scope | SHA-256 |
|---|---|---:|---|---|---|
| DOC-001-MAIN | `jama_debar_2025_oi_250046_1755300121.13587.pdf` | 14 | Main article | Pages 1-14 | `9F2CBC621AB2226B4E288F98C21AB084CA115EEF5D301F1999F78F14BC53CA9D` |
| DOC-002-PROTOCOL | `joi250046supp1_prod_1755300121.14087.pdf` | 77 | Protocol | Not Audited by Design; specific comparison only | `B94033E19E7781F6EA0A7100E9CCB9B32D6226C23FD268B13F81183361880AF0` |
| DOC-003-SAP | `joi250046supp2_prod_1755300121.15087.pdf` | 29 | Statistical analysis plan | Not Audited by Design; specific comparison only | `2CA40F50CDCC33AD6DFB9D6E9FB2241DFC59737C62C96803ACFB70830D7B4AB3` |
| DOC-004-INTERVENTION | `joi250046supp3_prod_1755300121.15087.pdf` | 7 | Intervention description / TIDieR | Not Audited by Design | `148B4CEBF4693E1FB2B5022CA5FF394AA440454049564B5407C693DBB10F8FF7` |
| DOC-005-RESULTS | `joi250046supp4_prod_1755300121.15587.pdf` | 19 | Results supplement | Pages 3-18; page 2 for context only | `6F306B566E39FAEE811B38D451D5E98E84F836D392AE2A5C11617DEFF0F9422F` |
| DOC-006-XLSX | `joi250046supp5_prod_1755300121.16087.xlsx` | N/A | Results workbook, sheet `eTable 3` | Entire sheet, 115 rows x 10 columns | `5FF42DC1BE5BF16B3FC27AB339D526E73C00B7F3940F9679A0AB4366DFA53893` |

## Text-layer assessment

- DOC-001-MAIN, DOC-004-INTERVENTION, and DOC-005-RESULTS: usable native text.
- DOC-002-PROTOCOL and DOC-003-SAP: embedded text is glyph-encoded/unusable; scientific content is excluded by design.
- DOC-006-XLSX: native spreadsheet cells.

## PDF preprocessing status

| Document ID | Selected page range | Extraction status | Render/OCR scope |
|---|---|---|---|
| DOC-001-MAIN | Pages 1-14 | Complete | Native text on all pages; images retained for pp. 5-11; rotated/reversed native tables on pp. 9-11 coordinate-reconstructed with OCR check text retained. |
| DOC-002-PROTOCOL | Not Audited by Design | Complete record | No scientific extraction, rendering, or OCR. |
| DOC-003-SAP | Not Audited by Design | Complete record | No scientific extraction, rendering, or OCR. |
| DOC-004-INTERVENTION | Not Audited by Design | Complete record | No scientific extraction, rendering, or OCR. |
| DOC-005-RESULTS | Pages 3-18; p. 2 context only | Complete | Native text on pp. 2-18; images retained for pp. 3, 7-11, and 14-18; OCR check text retained for p. 3 eFigure. |
| DOC-006-XLSX | Native workbook, deferred | Not PDF-preprocessed by design | Reserved for the results-supplement extractor and downstream checkers. |

## Rights-screen scope

All five PDFs require an AI Training Restriction Record. The workbook is logged as a supplied result artifact but is not subject to the PDF-only rights-record requirement in the project instructions.
