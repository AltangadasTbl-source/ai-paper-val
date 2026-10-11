# Workflow 1.6 Source Coverage

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_urashima_2019_oi_190023.pdf | PDF_PAGE | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-002 | joi190023supp1_prod.pdf | PDF_PAGE | 45 | 0 | 45 | 45 | COMPLETE |
| DOC-003 | joi190023supp2_prod.pdf | PDF_PAGE | 41 | 41 | 0 | 41 | COMPLETE |
| DOC-004 | joi190023supp3_prod.pdf | PDF_PAGE | 1 | 0 | 1 | 1 | COMPLETE |

Totals: 96 unique source units; 50 reusable; 46 fresh-required; 96 mapped. Reusable and fresh-required counts partition the full physical-page scope. Distinct main and support mapper artifacts now document completion of every physical page, including source units without applicable quantitative results.

## Canonical reusable coverage and fresh assignments

- DOC-001 pp. 1-8: layout-native extraction and normalized page text in `document_outputs/DOC-JAMA-2019-2210-MAIN/`; rendered pp. 4-8. DOC-001 p. 9: native page text at `document_outputs/JAMA2019-2210-DOC-01/native_text_pages/page-009.txt`. The latter collection also supplies alternate native text for pp. 1-8 and OCR for pp. 4-7. Main mapper must map all pp. 1-9.
- DOC-002 pp. 1-45: no reusable extraction or rendering. Support mapper must freshly extract and map each page, including both protocol/SAP versions and operational appendices; direct native/layout extraction first and targeted rendering/OCR only if required.
- DOC-003 pp. 1-41: layout-native and normalized page text in `document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/`; rendered pp. 2-41. Alternate native page text in `document_outputs/JAMA2019-2210-DOC-03/` covers pp. 1-41; OCR covers pp. 2-16. Missing OCR outside these ranges is not a source-unit coverage gap because native text and source-matched images exist. Support mapper must map all pp. 1-41.
- DOC-004 p. 1: no reusable extraction or rendering. Support mapper must freshly extract and map the direct page and record any no-applicable-relationship conclusion explicitly.

All derivative paths above are under `.ai_paper_validation/`. Overlapping assets are counted once per source page. Missing source-page images for text-only pages do not mandate fresh extraction when usable native text is present, but every candidate still requires direct-source recheck.
