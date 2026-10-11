# Workflow 1.6.1 Direct-Source Inventory

Inventory is restricted to the current paper package. A recursive search outside the audit and workflow/control areas identified exactly five supplied PDFs and no supplied DOC, DOCX, XLS, XLSX, or CSV sources. All 102 PDF pages are scientific-coverage units, including covers, references, administrative pages, and table-of-contents pages. PDF page numbers are physical file pages, independent of printed pagination.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content basis |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_bot_2019_oi_190007.pdf | PDF | PDF_PAGE | 11 | REPORT | Original investigation reporting the MooDFOOD randomized clinical trial, methods, participant flow, outcome estimates, tables, figures, and references. |
| DOC-002 | joi190007supp1_prod.pdf | PDF | PDF_PAGE | 60 | PLAN | MooDFOOD prospective protocol, version 7 dated July 11, 2017, with final amendments; prospective objectives, interventions, statistical design, safety, operational procedures, and references. |
| DOC-003 | joi190007supp2_prod.pdf | PDF | PDF_PAGE | 5 | PLAN | MooDFOOD Analysis Plan Prevention Trial Data: prospective research question, primary/secondary outcomes, analysis specifications, and sensitivity analyses. |
| DOC-004 | joi190007supp3_prod.pdf | PDF | PDF_PAGE | 25 | REPORT | Supplementary Online Content: contextual intervention descriptions and retrospective results appendices, outcome tables, trajectory figure, moderation, complete-case and CACE results. These descriptions are part of a results supplement, not a separately versioned prospective plan bundle. |
| DOC-005 | joi190007supp4_prod.pdf | PDF | PDF_PAGE | 1 | REPORT | Published Data Sharing Statement linked to the completed article; administrative reporting content and no supplied individual-level data. |

No supplied bundle combines separately identifiable REPORT and PLAN documents. A protocol supplied as a supplement remains PLAN. Role assignments derive from contents inspected directly with Poppler pdftotext, not supplement numbering.

## Stable identity and tooling

The complete SHA-256 values are in `source_hashes_before.sha256`, with package-relative source paths. All five values match source integrity records in the eligible legacy preprocessing manifest `.ai_paper_validation/preprocessing/current_run_manifest.json`.

Direct commands: `pdfinfo "SOURCE.pdf"`; `pdftotext -f 1 -l 2 "SOURCE.pdf" -`; `sha256sum -- "SOURCE.pdf"`. Engines: Poppler 26.01.0 PDF information/text; uutils coreutils 0.10.0 SHA-256. No fallback, Office conversion, OCR rerun, GPU, external literature, sibling package, or old scientific-review output was used.

## Coverage assignment

Main mapping owns DOC-001 PDF pp. 1-11. Support mapping owns DOC-002 pp. 1-60, DOC-003 pp. 1-5, DOC-004 pp. 1-25, and DOC-005 p. 1. Existing derivatives cover all units. Every page nevertheless requires new quantitative mapping from source-backed assets; derivative reuse does not reuse an earlier selection of relationships or findings.
