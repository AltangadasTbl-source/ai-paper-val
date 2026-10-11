# Reusable Evidence-Asset Inventory

Eligible reusable assets were inventoried only from `.ai_paper_validation/document_outputs/` and the package source-location map. Legacy candidates, checkers, verifier/critic/endetail material, and reports were neither read nor used as discovery scope. Every listed asset is hashed in `reused_artifact_hashes_before.sha256`.

| Asset family and exact path(s) | Source mapping | Method / fitness | Classification | Coverage consequence |
|---|---|---|---|---|
| `.ai_paper_validation/package_manifest.md` | DOC-001 pp. 1-11; DOC-002 pp. 1-46; DOC-003 pp. 1-23 | Source-location map; complete package identity/page enumeration, but its earlier DOC-002 audit-exclusion statement conflicts with this workflow's full-source requirement | STALE | Use only for source identity; DOC-002 pp. 1-46 are fresh-required |
| `document_outputs/DOC-001/document_record.md` | DOC-001 pp. 1-11 | Document record naming source, unit range, method, and derivative locations | USABLE | Supports native/page-map reuse |
| `document_outputs/DOC-001/page_manifest.csv` | DOC-001 pp. 1-11 | Page manifest with a one-row-per-page source location and native/rendered-path map | USABLE | Maps every DOC-001 page to reusable native text |
| `document_outputs/DOC-001/native_text/page-001.txt` through `page-011.txt` | DOC-001 pp. 1-11 respectively | Native PDF text; readable UTF-8; 11 exact one-page files | USABLE | Reusable coverage for DOC-001 pp. 1-11 |
| `document_outputs/DOC-001/normalized_text.txt` | DOC-001 pp. 1-11 | Document-level normalized native text; overlaps the page-level native files and is less exact for page citation | DUPLICATE | No additional reusable units |
| `document_outputs/DOC-001/images/page-005.png` through `page-009.png` | DOC-001 pp. 5-9 respectively | Rendered source pages, RGB PNG; needed as visual confirmation for Figure 1, Tables 1-3, and Figure 2 | USABLE | Visual support for pp. 5-9; no gap for other pages because native text is usable |
| `document_outputs/DOC-002/document_record.md` | DOC-002 pp. 1-46 | Document record only; says no scientific derivative was created and earlier scope was excluded | PARTIAL | No reusable unit; fresh direct mapping required for pp. 1-46 |
| `document_outputs/DOC-003/document_record.md` | DOC-003 pp. 1-23 | Document record naming source, unit range, method, and derivative locations | USABLE | Supports native/page-map reuse |
| `document_outputs/DOC-003/page_manifest.csv` | DOC-003 pp. 1-23 | Page manifest with a one-row-per-page source location and native/rendered-path map | USABLE | Maps every DOC-003 page to reusable native text |
| `document_outputs/DOC-003/native_text/page-001.txt` through `page-023.txt` | DOC-003 pp. 1-23 respectively | Native PDF text; readable UTF-8; 23 exact one-page files | USABLE | Reusable coverage for DOC-003 pp. 1-23 |
| `document_outputs/DOC-003/normalized_text.txt` | DOC-003 pp. 1-23 | Document-level normalized native text; overlaps the page-level native files and is less exact for page citation | DUPLICATE | No additional reusable units |
| `document_outputs/DOC-003/images/page-002.png` through `page-021.png` | DOC-003 pp. 2-21 respectively | Rendered source pages, RGB PNG; preserves eTables 1-12 and eFigures 1-3 | USABLE | Visual support for pp. 2-21; no gap for pp. 1, 22-23 because native text is usable |

## Exact file-to-source-location map

### DOC-001 native text

`page-001.txt`→p.1; `page-002.txt`→p.2; `page-003.txt`→p.3; `page-004.txt`→p.4; `page-005.txt`→p.5; `page-006.txt`→p.6; `page-007.txt`→p.7; `page-008.txt`→p.8; `page-009.txt`→p.9; `page-010.txt`→p.10; `page-011.txt`→p.11. All paths are under `.ai_paper_validation/document_outputs/DOC-001/native_text/`.

### DOC-001 rendered pages

`images/page-005.png`→p.5; `images/page-006.png`→p.6; `images/page-007.png`→p.7; `images/page-008.png`→p.8; `images/page-009.png`→p.9. All paths are under `.ai_paper_validation/document_outputs/DOC-001/`.

### DOC-003 native text

`page-001.txt`→p.1; `page-002.txt`→p.2; `page-003.txt`→p.3; `page-004.txt`→p.4; `page-005.txt`→p.5; `page-006.txt`→p.6; `page-007.txt`→p.7; `page-008.txt`→p.8; `page-009.txt`→p.9; `page-010.txt`→p.10; `page-011.txt`→p.11; `page-012.txt`→p.12; `page-013.txt`→p.13; `page-014.txt`→p.14; `page-015.txt`→p.15; `page-016.txt`→p.16; `page-017.txt`→p.17; `page-018.txt`→p.18; `page-019.txt`→p.19; `page-020.txt`→p.20; `page-021.txt`→p.21; `page-022.txt`→p.22; `page-023.txt`→p.23. All paths are under `.ai_paper_validation/document_outputs/DOC-003/native_text/`.

### DOC-003 rendered pages

`images/page-002.png`→p.2; `images/page-003.png`→p.3; `images/page-004.png`→p.4; `images/page-005.png`→p.5; `images/page-006.png`→p.6; `images/page-007.png`→p.7; `images/page-008.png`→p.8; `images/page-009.png`→p.9; `images/page-010.png`→p.10; `images/page-011.png`→p.11; `images/page-012.png`→p.12; `images/page-013.png`→p.13; `images/page-014.png`→p.14; `images/page-015.png`→p.15; `images/page-016.png`→p.16; `images/page-017.png`→p.17; `images/page-018.png`→p.18; `images/page-019.png`→p.19; `images/page-020.png`→p.20; `images/page-021.png`→p.21. All paths are under `.ai_paper_validation/document_outputs/DOC-003/`.

## Asset totals and gaps

- Eligible assets: 67 (34 native per-page text files, 2 normalized-text duplicates, 25 rendered pages, 2 page manifests, 3 document records, and 1 source-location map).
- No reusable OCR, layout text, table extraction, workbook extraction, DOC/DOCX conversion, or structured-workbook asset exists.
- Fitness totals: USABLE 63, PARTIAL 1, STALE 1, DUPLICATE 2, UNREADABLE 0.
- Fresh-required scientific-coverage gap: only DOC-002 PDF pp. 1-46, assigned in `source_coverage.md`; all other source pages have usable page-level native text, with rendered-page support where visual content requires it.
