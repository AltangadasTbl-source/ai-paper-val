# Direct source inventory

Inventory covers only the current paper package. Four direct sources are PDFs. No direct DOC, DOCX, XLS, XLSX, or CSV source is present. Stable units are one-based physical PDF pages. Sources and pre-existing extraction assets are preserved unchanged.

| Source ID | Source path | Format | Document role by content | Exact role scope and content | Unit type | Total units | SHA-256 |
|---|---|---|---|---|---|---:|---|
| DOC-001 | jama_huffman_2018_oi_170166.pdf | PDF | REPORT | pp. 1–12: main randomized-trial article, results, tables, figures and references | PDF_PAGE | 12 | 11311a6bb5c7a4be734ed60776b308f525ad101671ccc8d34bab18735aaca5f5 |
| DOC-002 | joi170166supp1_prod.pdf | PDF | PLAN | pp. 1–32: ACS QUIK protocol, version 22 September 2014, including prospective procedures and consent/contact appendices | PDF_PAGE | 32 | 0e13bdfc6e5e3c8b86e187f54f0a3d7d0217fc0614be9fbdbbb7839dbab9004a |
| DOC-003 | joi170166supp2_prod.pdf | PDF | PLAN | pp. 1–9: ACS QUIK statistical analysis plan, revised 17 June 2015 | PDF_PAGE | 9 | d49019c3cf6ee0766fb319f254f27f87751a73bfec66c34d38bae16a956bb1c6 |
| DOC-004 | joi170166supp3_prod.pdf | PDF | REPORT and PLAN bundle | p. 1: REPORT contents/index; pp. 2–16: PLAN operational toolkit, sample audit/feedback report and admission/discharge checklists; pp. 17–27: REPORT eTables 1–7 and eFigures 1A–2B | PDF_PAGE | 27 | 511f4a907e4c48d920f1c6b89d444fe76c7c91e11bbae84cdee834fa0393f3ec |

Total unique source units: 80 PDF pages. Document roles follow content rather than supplement number. The illustrative audit/feedback sample inside the toolkit is an operational example, rather than a separately reported trial result; location-specific role confirmation remains assigned to downstream mapping and recheck.

Direct inventory engines: `file`, `pdfinfo` (Poppler 25.03.0), and `sha256sum`. Each PDF is unencrypted; physical page counts are 12, 32, 9 and 27. The direct-source integrity baseline is `source_hashes_before.sha256`. DOC-001's modification metadata is August 2026; current native extraction and saved main-page image byte comparisons confirm eligible correspondence rather than assuming historical identity.

Every page is assigned to a downstream mapper: DOC-001 pp. 1–12 to the main quantitative mapper; DOC-002 pp. 1–32, DOC-003 pp. 1–9 and DOC-004 pp. 1–27 to the support quantitative mapper. Reusable eligibility and exact derivative limitations are in `evidence_asset_inventory.md`; mapping has not been performed by the curator.
