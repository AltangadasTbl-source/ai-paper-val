# Workflow 1.6 Evidence Asset Inventory

Inventory covers every existing native/OCR text, rendered page, page manifest, extraction/document record and source map below the pre-existing audit area. No table/workbook extraction, layout-text files, CSV records or Office derivatives were present. Legacy scientific artifacts are excluded. USABLE means a readable current-source locator/transcription aid, not a scientific verification. PARTIAL means usable for the exact stated subset but incomplete for the full source. DUPLICATE aggregates add no unique units. STALE records are preserved and excluded from scientific input.

Fitness was assessed using exact source/page identities in manifests, all five matched source hashes, nonempty page-text sizes, labeled physical-page delimiters in combined text, PNG file signatures/dimensions, and source-title/content agreement. Individual native pages cover 21 unique source units; overlapping OCR/images/metadata do not increase that number. Existing extraction engine is PyMuPDF/fitz (version not recorded), rendered with fitz.Matrix(2.5,2.5) at 180 dpi; existing OCR is Tesseract CPU (historical version not recorded). Existing scripts were read only for engine provenance and were not executed. Current direct engines are Poppler 26.01.0 and Tesseract 5.5.0. Fresh derivatives must record their own command and engine.

| Asset path | Source / exact locations | Kind / engine | Fitness | Reused | Coverage and limitation |
|---|---|---|---|---|---|
| .ai_paper_validation/document_outputs/DOC-001/ai_training_restriction_record.json | DOC-001 PDF pp.1-11 | Administrative document record | STALE | NO | Administrative record; no scientific extraction coverage; preserved without reuse. |
| .ai_paper_validation/document_outputs/DOC-001/document_status.json | DOC-001 PDF pp.1-11 | Document record | STALE | NO | Contains embedded legacy scientific dispositions; excluded entirely from scientific input. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text.txt | DOC-001 PDF pp.1-11 | Combined native / PyMuPDF | DUPLICATE | YES | Duplicates individually enumerated page text; physical-page delimiters retained. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_001.txt | DOC-001 PDF p.1 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_002.txt | DOC-001 PDF p.2 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_003.txt | DOC-001 PDF p.3 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_004.txt | DOC-001 PDF p.4 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_005.txt | DOC-001 PDF p.5 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_006.txt | DOC-001 PDF p.6 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_007.txt | DOC-001 PDF p.7 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_008.txt | DOC-001 PDF p.8 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_009.txt | DOC-001 PDF p.9 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_010.txt | DOC-001 PDF p.10 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-001/normalized_text/page_011.txt | DOC-001 PDF p.11 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-001/ocr_metadata/page_003.json | DOC-001 PDF p.3 | OCR extraction metadata | USABLE | YES | Exact OCR input/output path; historical Tesseract version absent. |
| .ai_paper_validation/document_outputs/DOC-001/ocr_metadata/page_005.json | DOC-001 PDF p.5 | OCR extraction metadata | USABLE | YES | Exact OCR input/output path; historical Tesseract version absent. |
| .ai_paper_validation/document_outputs/DOC-001/ocr_metadata/page_006.json | DOC-001 PDF p.6 | OCR extraction metadata | USABLE | YES | Exact OCR input/output path; historical Tesseract version absent. |
| .ai_paper_validation/document_outputs/DOC-001/ocr_metadata/page_007.json | DOC-001 PDF p.7 | OCR extraction metadata | USABLE | YES | Exact OCR input/output path; historical Tesseract version absent. |
| .ai_paper_validation/document_outputs/DOC-001/ocr_metadata/page_008.json | DOC-001 PDF p.8 | OCR extraction metadata | USABLE | YES | Exact OCR input/output path; historical Tesseract version absent. |
| .ai_paper_validation/document_outputs/DOC-001/ocr_text/page_003.txt | DOC-001 PDF p.3 | OCR / Tesseract CPU | USABLE | YES | Secondary aid; source confirmation required for table alignment and glyphs. |
| .ai_paper_validation/document_outputs/DOC-001/ocr_text/page_005.txt | DOC-001 PDF p.5 | OCR / Tesseract CPU | USABLE | YES | Secondary aid; source confirmation required for table alignment and glyphs. |
| .ai_paper_validation/document_outputs/DOC-001/ocr_text/page_006.txt | DOC-001 PDF p.6 | OCR / Tesseract CPU | USABLE | YES | Secondary aid; source confirmation required for table alignment and glyphs. |
| .ai_paper_validation/document_outputs/DOC-001/ocr_text/page_007.txt | DOC-001 PDF p.7 | OCR / Tesseract CPU | USABLE | YES | Secondary aid; source confirmation required for table alignment and glyphs. |
| .ai_paper_validation/document_outputs/DOC-001/ocr_text/page_008.txt | DOC-001 PDF p.8 | OCR / Tesseract CPU | USABLE | YES | Secondary aid; source confirmation required for table alignment and glyphs. |
| .ai_paper_validation/document_outputs/DOC-001/page_manifest.json | DOC-001 PDF pp.1-11 | Page location/extraction manifest | PARTIAL | YES | Only source/page/extraction identity reused; old selected scope superseded. |
| .ai_paper_validation/document_outputs/DOC-001/rendered_pages/page_003.png | DOC-001 PDF p.3 | Render / PyMuPDF 180 dpi | USABLE | YES | PNG readable, 1530x1980; source identity anchored by page manifest. |
| .ai_paper_validation/document_outputs/DOC-001/rendered_pages/page_005.png | DOC-001 PDF p.5 | Render / PyMuPDF 180 dpi | USABLE | YES | PNG readable, 1530x1980; source identity anchored by page manifest. |
| .ai_paper_validation/document_outputs/DOC-001/rendered_pages/page_006.png | DOC-001 PDF p.6 | Render / PyMuPDF 180 dpi | USABLE | YES | PNG readable, 1530x1980; source identity anchored by page manifest. |
| .ai_paper_validation/document_outputs/DOC-001/rendered_pages/page_007.png | DOC-001 PDF p.7 | Render / PyMuPDF 180 dpi | USABLE | YES | PNG readable, 1530x1980; source identity anchored by page manifest. |
| .ai_paper_validation/document_outputs/DOC-001/rendered_pages/page_008.png | DOC-001 PDF p.8 | Render / PyMuPDF 180 dpi | USABLE | YES | PNG readable, 1530x1980; source identity anchored by page manifest. |
| .ai_paper_validation/document_outputs/DOC-002/ai_training_restriction_record.json | DOC-002 PDF pp.1-60; no extraction | Administrative document record | STALE | NO | Administrative record; no scientific extraction coverage; preserved without reuse. |
| .ai_paper_validation/document_outputs/DOC-002/document_status.json | DOC-002 PDF pp.1-60; no extraction | Document record | STALE | NO | Contains embedded legacy scientific dispositions; excluded entirely from scientific input. |
| .ai_paper_validation/document_outputs/DOC-003/ai_training_restriction_record.json | DOC-003 PDF pp.1-5; no extraction | Administrative document record | STALE | NO | Administrative record; no scientific extraction coverage; preserved without reuse. |
| .ai_paper_validation/document_outputs/DOC-003/document_status.json | DOC-003 PDF pp.1-5; no extraction | Document record | STALE | NO | Contains embedded legacy scientific dispositions; excluded entirely from scientific input. |
| .ai_paper_validation/document_outputs/DOC-004/ai_training_restriction_record.json | DOC-004 PDF pp.1-2,16-23 | Administrative document record | STALE | NO | Administrative record; no scientific extraction coverage; preserved without reuse. |
| .ai_paper_validation/document_outputs/DOC-004/document_status.json | DOC-004 PDF pp.1-2,16-23 | Document record | STALE | NO | Contains embedded legacy scientific dispositions; excluded entirely from scientific input. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text.txt | DOC-004 PDF pp.1-2,16-23 | Combined native / PyMuPDF | DUPLICATE | YES | Duplicates individually enumerated page text; physical-page delimiters retained. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_001.txt | DOC-004 PDF p.1 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_002.txt | DOC-004 PDF p.2 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_016.txt | DOC-004 PDF p.16 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_017.txt | DOC-004 PDF p.17 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_018.txt | DOC-004 PDF p.18 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_019.txt | DOC-004 PDF p.19 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_020.txt | DOC-004 PDF p.20 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_021.txt | DOC-004 PDF p.21 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_022.txt | DOC-004 PDF p.22 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-004/normalized_text/page_023.txt | DOC-004 PDF p.23 | Native text / PyMuPDF | USABLE | YES | Exact-source locator only; adds no duplicate unit counts. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_metadata/page_016.json | DOC-004 PDF p.16 | OCR extraction metadata | USABLE | YES | Exact OCR input/output path; historical Tesseract version absent. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_metadata/page_017.json | DOC-004 PDF p.17 | OCR extraction metadata | USABLE | YES | Exact OCR input/output path; historical Tesseract version absent. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_metadata/page_018.json | DOC-004 PDF p.18 | OCR extraction metadata | USABLE | YES | Exact OCR input/output path; historical Tesseract version absent. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_metadata/page_019.json | DOC-004 PDF p.19 | OCR extraction metadata | USABLE | YES | Exact OCR input/output path; historical Tesseract version absent. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_metadata/page_020.json | DOC-004 PDF p.20 | OCR extraction metadata | USABLE | YES | Exact OCR input/output path; historical Tesseract version absent. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_metadata/page_021.json | DOC-004 PDF p.21 | OCR extraction metadata | USABLE | YES | Exact OCR input/output path; historical Tesseract version absent. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_metadata/page_022.json | DOC-004 PDF p.22 | OCR extraction metadata | USABLE | YES | Exact OCR input/output path; historical Tesseract version absent. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_metadata/page_023.json | DOC-004 PDF p.23 | OCR extraction metadata | USABLE | YES | Exact OCR input/output path; historical Tesseract version absent. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_text/page_016.txt | DOC-004 PDF p.16 | OCR / Tesseract CPU | USABLE | YES | Secondary aid; source confirmation required for table alignment and glyphs. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_text/page_017.txt | DOC-004 PDF p.17 | OCR / Tesseract CPU | USABLE | YES | Secondary aid; source confirmation required for table alignment and glyphs. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_text/page_018.txt | DOC-004 PDF p.18 | OCR / Tesseract CPU | USABLE | YES | Secondary aid; source confirmation required for table alignment and glyphs. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_text/page_019.txt | DOC-004 PDF p.19 | OCR / Tesseract CPU | USABLE | YES | Secondary aid; source confirmation required for table alignment and glyphs. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_text/page_020.txt | DOC-004 PDF p.20 | OCR / Tesseract CPU | USABLE | YES | Secondary aid; source confirmation required for table alignment and glyphs. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_text/page_021.txt | DOC-004 PDF p.21 | OCR / Tesseract CPU | USABLE | YES | Secondary aid; source confirmation required for table alignment and glyphs. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_text/page_022.txt | DOC-004 PDF p.22 | OCR / Tesseract CPU | USABLE | YES | Secondary aid; source confirmation required for table alignment and glyphs. |
| .ai_paper_validation/document_outputs/DOC-004/ocr_text/page_023.txt | DOC-004 PDF p.23 | OCR / Tesseract CPU | USABLE | YES | Secondary aid; source confirmation required for table alignment and glyphs. |
| .ai_paper_validation/document_outputs/DOC-004/page_manifest.json | DOC-004 PDF pp.1-2,16-23 | Page location/extraction manifest | PARTIAL | YES | Only source/page/extraction identity reused; old selected scope superseded. |
| .ai_paper_validation/document_outputs/DOC-004/rendered_pages/page_016.png | DOC-004 PDF p.16 | Render / PyMuPDF 180 dpi | USABLE | YES | PNG readable, 1530x1980; source identity anchored by page manifest. |
| .ai_paper_validation/document_outputs/DOC-004/rendered_pages/page_017.png | DOC-004 PDF p.17 | Render / PyMuPDF 180 dpi | USABLE | YES | PNG readable, 1530x1980; source identity anchored by page manifest. |
| .ai_paper_validation/document_outputs/DOC-004/rendered_pages/page_018.png | DOC-004 PDF p.18 | Render / PyMuPDF 180 dpi | USABLE | YES | PNG readable, 1530x1980; source identity anchored by page manifest. |
| .ai_paper_validation/document_outputs/DOC-004/rendered_pages/page_019.png | DOC-004 PDF p.19 | Render / PyMuPDF 180 dpi | USABLE | YES | PNG readable, 1530x1980; source identity anchored by page manifest. |
| .ai_paper_validation/document_outputs/DOC-004/rendered_pages/page_020.png | DOC-004 PDF p.20 | Render / PyMuPDF 180 dpi | USABLE | YES | PNG readable, 1530x1980; source identity anchored by page manifest. |
| .ai_paper_validation/document_outputs/DOC-004/rendered_pages/page_021.png | DOC-004 PDF p.21 | Render / PyMuPDF 180 dpi | USABLE | YES | PNG readable, 1530x1980; source identity anchored by page manifest. |
| .ai_paper_validation/document_outputs/DOC-004/rendered_pages/page_022.png | DOC-004 PDF p.22 | Render / PyMuPDF 180 dpi | USABLE | YES | PNG readable, 1530x1980; source identity anchored by page manifest. |
| .ai_paper_validation/document_outputs/DOC-004/rendered_pages/page_023.png | DOC-004 PDF p.23 | Render / PyMuPDF 180 dpi | USABLE | YES | PNG readable, 1530x1980; source identity anchored by page manifest. |
| .ai_paper_validation/document_outputs/DOC-005/ai_training_restriction_record.json | DOC-005 PDF p.1; no extraction | Administrative document record | STALE | NO | Administrative record; no scientific extraction coverage; preserved without reuse. |
| .ai_paper_validation/document_outputs/DOC-005/document_status.json | DOC-005 PDF p.1; no extraction | Document record | STALE | NO | Contains embedded legacy scientific dispositions; excluded entirely from scientific input. |
| .ai_paper_validation/preprocessing/README.md | All five source documents / identity and extraction provenance | Preprocessing documentation | STALE | NO | Legacy instructions supply no authoritative extraction coverage. |
| .ai_paper_validation/preprocessing/current_run_manifest.json | All five source documents / identity and extraction provenance | Source identity/extraction manifest | PARTIAL | YES | All five hashes source-matched; old selective scope superseded. |
| .ai_paper_validation/preprocessing/ocr_backend.json | All five source documents / identity and extraction provenance | Historical OCR engine metadata | PARTIAL | YES | CPU provenance only; historical absolute executable path not used; version absent. |
| .ai_paper_validation/package_manifest.md | All five source documents / filename and page count identity | Source-location inventory | PARTIAL | YES | Identity metadata only; legacy selective scientific scope superseded. |

Fresh-required exact assignments: DOC-002 PDF pp.1–60; DOC-003 pp.1–5; DOC-004 pp.3–15,24–25; DOC-005 p.1. This totals 81 unique source units. Reusable units: DOC-001 pp.1–11; DOC-004 pp.1–2,16–23 (21 unique units). Every unit receives new mapping. Page text/OCR/render pairs and their extraction metadata are individually inventoried; overlaps add no unique pages. There are 78 asset records: 67 actually reused and individually hashed; 11 stale non-reused document/administrative/documentation records preserved unchanged.

Existing preprocessing source code is not an evidence extraction asset and is not reused or executed; it was inspected only to identify the native/render engine. No old candidate, verifier, critic, endetail or final-report document was opened. Embedded legacy scientific disposition fields encountered in document-status metadata are excluded and the corresponding records are not reused. No STALE record contributes reusable units. Inventory and hash commands use direct local rg, file, wc, pdfinfo, pdftotext and sha256sum; no Python orchestration, external sources or sibling packages were used.

## Current-run derivative provenance index

These201 derivatives are new run outputs and are excluded from the67-artifact reusable baseline. All exact commands, source identities and expanded physical-page assignments are preserved in the owning evidence artifacts below. Every extraction/render engine is direct CPU Poppler26.01.0; no new OCR or Office conversion was performed.

| Derivative group | Count | Source locations | Engine and command basis | Complete assignment artifact |
|---|---:|---|---|---|
| preprocessing/main-layout-001-011.txt | 1 | DOC-001 pp1–11 | pdftotext -layout -f1 -l11 | extraction/main_quantitative_evidence.md |
| preprocessing/support-sS-pP-native.txt and support-sS-pP-layout.txt | 162 | DOC-002 pp1–60; DOC-003 pp1–5; DOC-004 pp3–15,24–25; DOC-005 p1 | pdftotext selected page, native and -layout | extraction/support_quantitative_evidence.md |
| preprocessing/support-s1-pP.png | 5 | DOC-002 pp12,25,31,32,38 | pdftoppm selected page, -r110 -singlefile -png | extraction/support_quantitative_evidence.md |
| preprocessing/numeric-main-p4-layout.txt | 1 | DOC-001 p4 | pdftotext selected page, -layout | relationships/parts/numeric-main.md |
| preprocessing/stats1-main-p4.png, stats1-s1-p16.png and stats1-s3-p22.png | 3 | DOC-001 p4; DOC-002 p16; DOC-004 p22 | pdftoppm selected page, -r110 -singlefile -png | statistics/relationship_inventory.md |
| preprocessing/recheck-PREFIX-pN.png | 23 | DOC-001 pp1–2; DOC-002 pp8,9,14,17,18,23,26,28,30,34,35,36,37,43; DOC-003 pp2,4; DOC-004 pp3,4,5,6,12 | pdftoppm selected page, -r100 -singlefile -png | verification/evidence_recheck.md |
| preprocessing/visualrepair-sS-images.txt | 4 | Complete DOC-002–DOC-005 raster-object inventories | pdfimages -list | extraction/parts/support_plan_p26_visual_repair.md |
| preprocessing/visualrepair-s1-p1.png and visualrepair-s2-p1.png | 2 | DOC-002 p1; DOC-003 p1 | pdftoppm selected page, -r110 -singlefile -png | extraction/parts/support_plan_p26_visual_repair.md |

Total new derivatives:201=164text extractions+33page images+4raster inventories. Existing source-matched images and new p26 render were reused across current review stages without duplication. Every direct source page is still counted once in source_coverage.md.
