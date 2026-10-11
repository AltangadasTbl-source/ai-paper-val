# Workflow 1.6.2 Direct Source Inventory

Inventory is restricted to this package. Every supplied PDF, DOC, DOCX, XLS, XLSX, and CSV was searched; only the three PDFs below are direct sources. Audit-area page manifests are derivative assets, not additional direct sources. Source hashes were captured before mapping in source_hashes_before.sha256.

| Source ID | Source path | Format | Document role | Stable unit type | Total units | Content basis and complete boundaries |
|---|---|---|---|---|---:|---|
| DOC-001 | jama_dupuis_2024_oi_240111_1733431204.38761.pdf | PDF | REPORT | PDF_PAGE | 11 | Main randomized clinical trial article, physical PDF pp. 1–11, printed pp. 1981–1991. |
| DOC-002 | joi240111supp1_prod_1733431204.57929.pdf | PDF | PLAN | PDF_PAGE | 46 | Cover p. 1; final protocol pp. 2–18; original protocol pp. 19–30; document/amendment history p. 31; original/final SAP pp. 32–46. Entire bundle is PLAN by content; it contains no separate results report. |
| DOC-003 | joi240111supp2_prod_1733431204.76024.pdf | PDF | REPORT | PDF_PAGE | 23 | Results supplement: contents p. 1; eTables 1–12 pp. 2–17; eFigures 1–3 pp. 18–21; eMethods p. 22; references p. 23. |

## Identity and methods

Direct engine: Poppler pdfinfo 26.01.0 for page counts; Poppler pdftotext 26.01.0 for native/layout content matching; sha256sum (uutils coreutils) 0.10.0 for hashes. PDFs are unencrypted. No Office conversion, OCR, fresh derivative, fallback, or external source was needed for inventory. The before-hash file contains package-relative actual source paths.

## Mapper handoff

- Main mapper: DOC-001 PDF pp. 1–11. Read .ai_paper_validation/document_outputs/DOC-001/native_text/page-001.txt through page-011.txt and source-linked images/page-005.png through page-009.png. The files named native_text preserve layout. Optional full layout: .ai_paper_validation/review_1_5_3/preprocessing/main_quantitative_mapper/DOC-001-layout.txt. Collapse whitespace to single spaces across concatenated per-page text: 61,236 Unicode characters.
- Support mapper: DOC-002 PDF pp. 1–46 via .ai_paper_validation/review_1_5_3/preprocessing/support/doc002_native/page-001.txt through page-046.txt, with doc002_layout/page-001.txt through page-046.txt for table geometry. Normalized native text: 128,526 characters. DOC-003 PDF pp. 1–23 via .ai_paper_validation/document_outputs/DOC-003/native_text/page-001.txt through page-023.txt and images/page-002.png through page-021.png; p. 22 image additionally available at .ai_paper_validation/review_1_5_3/preprocessing/recheck/doc003-page-22.png. Normalized page text: 46,510 characters. Combined support text: 175,036 characters, below the 200,000-character shard bound; 21 unique rendered support pages, below the 32-image bound.
- 76 pages are reusable-backed. DOC-002 pp. 17, 18, 29 and 30 have only captions/footers in reusable text; their screenshot content required fresh CPU rendering and direct visual mapping, now complete. Every page still requires new quantitative mapping, including cover, references, appendices, graphical pages, and background pages, with explicit no-applicable-relationship entries as appropriate.

## Boundaries and limitations

Existing document records and manifests are used only for source identity, page mapping, engine provenance, and fitness. Their prior processing-status statements, selected audit scope, and role-specific review boundaries do not determine this run's scope. The DOC-002 legacy record predates its later complete page extraction: its claim that no scientific derivatives exist is not current coverage evidence. The present source-matched 46 native and 46 layout files establish complete coverage. No old candidate, checker, screening, verifier, critic, classification, endetail, or final-report content was read.

Selectable figure labels may omit graphical values, particularly DOC-003 pp. 20–21; retained source images are usable and must be visually mapped. Rendered images are locator/transcription aids, and final candidate confirmation remains against exact direct-source pages. No scientific coverage limitation was identified at inventory.
