# Source Coverage Ledger — Complete Mapping

Reusable and fresh-required counts are a complete, non-overlapping partition of the 170 direct PDF-page units. All reusable-backed and fresh-required pages have now been scientifically mapped in the disjoint mapping artifacts recorded by `coverage_manifest.md`.

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf | PDF_PAGE | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 | joi250084supp1_prod_1765403089.61351.pdf | PDF_PAGE | 90 | 0 | 90 | 90 | COMPLETE |
| DOC-003 | joi250084supp2_prod_1765403089.61751.pdf | PDF_PAGE | 69 | 31 | 38 | 69 | COMPLETE |

**Totals:** 170 PDF pages; 42 reusable; 128 fresh-required; 170 mapped; COMPLETE.

## Exact disjoint fresh-required assignments

| Source ID | Fresh-required unit scope | Reason |
|---|---|---|
| DOC-001 | None | A usable, source-linked native-text asset exists for every page 1-11; visual/OCR companions exist where the old page manifest identified figures, a table, or a flow diagram. |
| DOC-002 | PDF pp. 1-90 | Only a document-level record exists. It confirms source identity and warns of glyph-encoded sampled native text, but it does not extract or map any individual page. |
| DOC-003 | PDF pp. 1-33; 36-37; 67-69 | Usable page-linked native text exists only for pp. 34-35 and 38-66. These 38 pages have no usable page-level reusable extraction. |

The fresh-required ranges are pairwise disjoint and, with the reusable page sets, exhaust each direct source. Scientific mapping is complete; candidate checking is a separate downstream stage.

## Reusable page coverage

- DOC-001: native text for pp. 1-11; OCR and rendered-page companions for pp. 5-9.
- DOC-002: no reusable page-level text, OCR, rendered page, table, or source-location map.
- DOC-003: native text, OCR, and rendered-page companions for pp. 34-35 and 38-66 (31 pages).

## Curation limitations

The old page manifest and document records deliberately omitted the protocol and much of the results supplement under an earlier workflow. They are usable locators for the pages they name, but cannot define the current scientific scope. The all-pages native/OCR aggregate files duplicate individual page files and are not an independent coverage source. Native extraction can flatten multi-column text and table layout; rendered pages remain the visual-confirmation aid for applicable reused pages.
