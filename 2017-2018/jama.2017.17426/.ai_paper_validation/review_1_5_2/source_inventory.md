# Fresh Direct-Source Inventory

Prepared source-first on 2026-08-20. Existing audit derivatives were not inspected or used as evidence.

| Source ID | Package-relative source path | Type | Size (bytes) | SHA-256 | Stable units | Likely role | Fresh extraction status |
|---|---|---|---:|---|---:|---|---|
| DOC-001 | jama_thomas_2017_oi_170130.pdf | PDF | 431209 | `2638f5947ee9d89211beb4daa767e962939fda0df25a93e3546c2d442751c239` | 10 PDF pages | Main JAMA original investigation; abstract, methods, results, tables, figures, and discussion | Complete native and layout extraction; result-relevant rendering completed |
| DOC-002 | joi170130supp1_prod.pdf | PDF | 610103 | `d269a035b2f2542a9563005f41c6c7bf4f7b2a877bcd0c87def494c82bc57ee7` | 69 PDF pages | Supplement 1: original/final protocol, protocol-change summary, and statistical analysis plan (SAP) | Complete native and layout extraction; selected result-definition/protocol/SAP rendering completed; one targeted OCR page |
| DOC-003 | joi170130supp2_prod.pdf | PDF | 29890 | `890ac8383d825d992466a46e8edf0a1e8f5c776733742d5aab2023ab345e904c` | 2 PDF pages | Supplement 2: eTable of multiple-imputation intention-to-treat results | Complete native and layout extraction; both pages rendered |

## Stable-unit basis

PDF pages are the unique stable source units. The direct-source total is 81 PDF pages (10 + 69 + 2). No Office or structured-data direct sources were supplied.

## Result-relevant scope

- DOC-001: PDF pages 1-9 were rendered because they contain the abstract, endpoint definitions, results narrative, baseline and outcome tables, figures, adverse-event table, and discussion of reported results. Page 10 contains acknowledgments/disclosures/references rather than result displays; its native and layout text remain available for source-wide mapping.
- DOC-002: all 69 pages have fresh native/layout text. Rendered pages were 1, 5, 7-16, 25, 28-44, 47-51, and 52-69. This covers the supplement index; the original and final protocol's trial design, eligibility, allocation, outcome, hospital-day, follow-up, and flowchart definitions; the change summary; and the entire SAP, including proposed result tables and the rendered SAP flowchart on page 66. Unrendered protocol administrative, consent, questionnaire, and reference pages remain available in fresh text and layout derivatives and are mapped as source units.
- DOC-003: both pages were rendered because page 2 is the quantitative eTable and page 1 supplies its provenance and description.
