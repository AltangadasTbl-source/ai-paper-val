# Complete Source Coverage

Unit type is `PDF_PAGE`. Reusable and fresh-required units partition each source total. `Mapped units` records an assigned, source-linked mapping route: reusable-backed units are linked to the listed legacy derivatives, and fresh-required units are assigned for direct-source extraction. No page is omitted because of a legacy scope label.

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_courcoulas_2024_oi_240004_1721756962.76052.pdf | PDF_PAGE | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 | joi240004supp1_prod_1721756962.80052.pdf | PDF_PAGE | 65 | 0 | 65 | 65 | COMPLETE |
| DOC-003 | joi240004supp2_prod_1721756962.82552.pdf | PDF_PAGE | 22 | 15 | 7 | 22 | COMPLETE |
| DOC-004 | joi240004supp3_prod_1721756962.84052.pdf | PDF_PAGE | 1 | 0 | 1 | 1 | COMPLETE |

## Exact unit partition and downstream mapper assignment

| Source ID | Reusable-backed exact units and assets | Fresh-required exact units | Downstream mapper assignment | Gap and fitness disposition |
|---|---|---|---|---|
| DOC-001 | PDF pp. 1-11: `document_outputs/DOC-001/preprocessing/normalized_text/page-001.txt` through `page-011.txt`; PDF pp. 3-8 additionally: matching `page_images/page-003.png` through `page-008.png` | None | Main quantitative mapper: reusable-backed DOC-001 pp. 1-11 | Native layout text is USABLE for every page; renders are USABLE visual confirmation for pp. 3-8. |
| DOC-002 | None | PDF pp. 1-65 | Support quantitative mapper: fresh direct-source DOC-002 pp. 1-65 | No legacy extraction, OCR, table/workbook extraction, or rendering. The document record is only a PARTIAL document-level locator and does not cover page evidence. |
| DOC-003 | PDF pp. 8-13: matching rendered PNGs; native text is PARTIAL. PDF pp. 14-22: matching native layout text and rendered PNGs | PDF pp. 1-7 | Support quantitative mapper: reusable-backed DOC-003 pp. 8-22; fresh direct-source DOC-003 pp. 1-7 | Renders are USABLE for pp. 8-13; native text there is PARTIAL because plot text is sparse. Native text and renders are USABLE for pp. 14-22. No derivative covers pp. 1-7. |
| DOC-004 | None | PDF p. 1 | Support quantitative mapper: fresh direct-source DOC-004 p. 1 | No legacy extraction, OCR, table/workbook extraction, or rendering. The document record is only a PARTIAL document-level locator. |

Totals: 99 unique units; 26 reusable units; 73 fresh-required units; 99 mapped units.

Limitations: legacy audit labels excluded DOC-002, DOC-003 pp. 1-7, and DOC-004 from scientific processing. Those labels are not a workflow 1.5.3 coverage boundary; the 73 affected pages have explicit fresh direct-source assignments above. DOC-003 pp. 8-13 lack usable native plot text, but their exact source-matched rendered pages are reusable visual evidence; any numeric transcription from those plots still requires direct-PDF confirmation.
