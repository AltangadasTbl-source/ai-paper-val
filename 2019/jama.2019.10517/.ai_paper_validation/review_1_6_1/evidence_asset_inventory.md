# Reusable Evidence-Asset Inventory

Existing OCR/native/normalized/layout text, rendered pages, extraction maps, source records, page manifests and extraction metadata were inventoried under the existing audit area. Old checker, candidate, queue, screening, verification, classification and final-report content was excluded. Preprocessing executable scripts, rights-only records and backend diagnostic files are controls rather than evidence assets and are not reused. All listed assets are preserved unchanged and are hashed in `reused_artifact_hashes_before.sha256`, including overlapping aids and metadata.

## Engines and fitness

Legacy protocol and data-sharing native/layout derivatives were produced by direct Poppler `pdftotext` extraction; current direct `pdftotext -layout` reproduces the protocol aggregate byte-for-byte. Document-output native assets and renderings retain their supplied extraction metadata; legacy records identify earlier OCR as rapidocr-cuda. Those existing OCR files are reused read-only as transcription aids; no GPU is probed or invoked in this run. Current tooling is direct CPU-only and available as recorded in `tooling_record.md`. Source-linked native text, images and records establish reusable coverage, while every scientific relationship is newly mapped.

USABLE means readable and source-located for its intended function; PARTIAL means useful as an aid but incomplete for graphical content; DUPLICATE means byte-identical to an earlier inventoried aid and adds no unique coverage. No stale or unreadable artifact was identified. Metadata and document records establish identity/location rather than statistical conclusions. The field-specific extraction maps contain evidence without candidate adjudication and are reused only for source location and transcription. Every chart page also has readable rendered evidence. Sparse chart native/normalized/OCR text does not provide exact unprinted plotted values.

Commands used: `rg --files --hidden .ai_paper_validation`, `wc -m`, `head`, source-linked `cat`/`sed`, `pdfinfo`, `pdftotext`, `cmp`, `sha256sum`, and image-header `file`. No new extraction derivative was written in the curator stage. Native and layout aggregate text uses form-feed separators; a missing terminal form feed is not a missing final page.

## Individual assets

| Asset ID | Package-relative asset path | Source and exact unit scope | Method / function | Fitness | Basis |
|---|---|---|---|---|---|
| A001 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/document_record.yaml | DOC-001 PDF pp.1-10 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A002 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/main_text_extractor_response.yaml | DOC-001 PDF pp.1-10 | Legacy source-location evidence map | USABLE | Evidence-map locations only; no candidate selection reused |
| A003 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/native_extraction_quality.json | DOC-001 PDF pp.1-10 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A004 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-001.txt | DOC-001 PDF p.1 | Legacy native PDF text | USABLE | Readable source-linked text |
| A005 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-002.txt | DOC-001 PDF p.2 | Legacy native PDF text | USABLE | Readable source-linked text |
| A006 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-003.txt | DOC-001 PDF p.3 | Legacy native PDF text | USABLE | Readable source-linked text |
| A007 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-004.txt | DOC-001 PDF p.4 | Legacy native PDF text | USABLE | Readable source-linked text |
| A008 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-005.txt | DOC-001 PDF p.5 | Legacy native PDF text | USABLE | Readable source-linked text |
| A009 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-006.txt | DOC-001 PDF p.6 | Legacy native PDF text | USABLE | Readable source-linked text |
| A010 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-007.txt | DOC-001 PDF p.7 | Legacy native PDF text | USABLE | Readable source-linked text |
| A011 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-008.txt | DOC-001 PDF p.8 | Legacy native PDF text | USABLE | Readable source-linked text |
| A012 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-009.txt | DOC-001 PDF p.9 | Legacy native PDF text | USABLE | Readable source-linked text |
| A013 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-010.txt | DOC-001 PDF p.10 | Legacy native PDF text | USABLE | Readable source-linked text |
| A014 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-001.txt | DOC-001 PDF p.1 | Legacy normalized native/OCR text | USABLE | Readable source-linked transcription aid |
| A015 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-002.txt | DOC-001 PDF p.2 | Legacy normalized native/OCR text | USABLE | Readable source-linked transcription aid |
| A016 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-003.txt | DOC-001 PDF p.3 | Legacy normalized native/OCR text | USABLE | Readable source-linked transcription aid |
| A017 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-004.txt | DOC-001 PDF p.4 | Legacy normalized native/OCR text | USABLE | Readable source-linked transcription aid |
| A018 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-005.txt | DOC-001 PDF p.5 | Legacy normalized native/OCR text | USABLE | Readable source-linked transcription aid |
| A019 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-006.txt | DOC-001 PDF p.6 | Legacy normalized native/OCR text | USABLE | Readable source-linked transcription aid |
| A020 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-007.txt | DOC-001 PDF p.7 | Legacy normalized native/OCR text | USABLE | Readable source-linked transcription aid |
| A021 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-008.txt | DOC-001 PDF p.8 | Legacy normalized native/OCR text | USABLE | Readable source-linked transcription aid |
| A022 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-009.txt | DOC-001 PDF p.9 | Legacy normalized native/OCR text | USABLE | Readable source-linked transcription aid |
| A023 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/normalized_text/page-010.txt | DOC-001 PDF p.10 | Legacy normalized native/OCR text | USABLE | Readable source-linked transcription aid |
| A024 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_metadata/page-003.json | DOC-001 PDF p.3 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A025 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_metadata/page-005.json | DOC-001 PDF p.5 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A026 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_metadata/page-006.json | DOC-001 PDF p.6 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A027 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_metadata/page-007.json | DOC-001 PDF p.7 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A028 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_metadata/page-008.json | DOC-001 PDF p.8 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A029 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_metadata/page-009.json | DOC-001 PDF p.9 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A030 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_text/page-003.txt | DOC-001 PDF p.3 | Legacy OCR, engine retained in supplied metadata | USABLE | Source-linked transcription aid; direct-source authority retained |
| A031 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_text/page-005.txt | DOC-001 PDF p.5 | Legacy OCR, engine retained in supplied metadata | USABLE | Source-linked transcription aid; direct-source authority retained |
| A032 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_text/page-006.txt | DOC-001 PDF p.6 | Legacy OCR, engine retained in supplied metadata | USABLE | Source-linked transcription aid; direct-source authority retained |
| A033 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_text/page-007.txt | DOC-001 PDF p.7 | Legacy OCR, engine retained in supplied metadata | USABLE | Source-linked transcription aid; direct-source authority retained |
| A034 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_text/page-008.txt | DOC-001 PDF p.8 | Legacy OCR, engine retained in supplied metadata | USABLE | Source-linked transcription aid; direct-source authority retained |
| A035 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/ocr_text/page-009.txt | DOC-001 PDF p.9 | Legacy OCR, engine retained in supplied metadata | USABLE | Source-linked transcription aid; direct-source authority retained |
| A036 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/page_level_manifest.json | DOC-001 PDF pp.1-10 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A037 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/rendered_pages/page-003.png | DOC-001 PDF p.3 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A038 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/rendered_pages/page-005.png | DOC-001 PDF p.5 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A039 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/rendered_pages/page-006.png | DOC-001 PDF p.6 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A040 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/rendered_pages/page-007.png | DOC-001 PDF p.7 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A041 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/rendered_pages/page-008.png | DOC-001 PDF p.8 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A042 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/rendered_pages/page-009.png | DOC-001 PDF p.9 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A043 | .ai_paper_validation/document_outputs/JAMA2019-10517-D02/document_record.yaml | DOC-002 PDF pp.1-42 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A044 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/document_record.yaml | DOC-003 PDF pp.1-10 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A045 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/native_extraction_quality.json | DOC-003 PDF pp.1-10 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A046 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-001.txt | DOC-003 PDF p.1 | Legacy native PDF text | USABLE | Readable source-linked text |
| A047 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-002.txt | DOC-003 PDF p.2 | Legacy native PDF text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A048 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-003.txt | DOC-003 PDF p.3 | Legacy native PDF text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A049 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-004.txt | DOC-003 PDF p.4 | Legacy native PDF text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A050 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-005.txt | DOC-003 PDF p.5 | Legacy native PDF text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A051 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-006.txt | DOC-003 PDF p.6 | Legacy native PDF text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A052 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-007.txt | DOC-003 PDF p.7 | Legacy native PDF text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A053 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-008.txt | DOC-003 PDF p.8 | Legacy native PDF text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A054 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-009.txt | DOC-003 PDF p.9 | Legacy native PDF text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A055 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-010.txt | DOC-003 PDF p.10 | Legacy native PDF text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A056 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-001.txt | DOC-003 PDF p.1 | Legacy normalized native/OCR text | USABLE | Readable source-linked transcription aid |
| A057 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-002.txt | DOC-003 PDF p.2 | Legacy normalized native/OCR text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A058 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-003.txt | DOC-003 PDF p.3 | Legacy normalized native/OCR text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A059 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-004.txt | DOC-003 PDF p.4 | Legacy normalized native/OCR text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A060 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-005.txt | DOC-003 PDF p.5 | Legacy normalized native/OCR text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A061 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-006.txt | DOC-003 PDF p.6 | Legacy normalized native/OCR text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A062 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-007.txt | DOC-003 PDF p.7 | Legacy normalized native/OCR text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A063 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-008.txt | DOC-003 PDF p.8 | Legacy normalized native/OCR text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A064 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-009.txt | DOC-003 PDF p.9 | Legacy normalized native/OCR text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A065 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/normalized_text/page-010.txt | DOC-003 PDF p.10 | Legacy normalized native/OCR text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A066 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_metadata/page-002.json | DOC-003 PDF p.2 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A067 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_metadata/page-003.json | DOC-003 PDF p.3 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A068 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_metadata/page-004.json | DOC-003 PDF p.4 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A069 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_metadata/page-005.json | DOC-003 PDF p.5 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A070 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_metadata/page-006.json | DOC-003 PDF p.6 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A071 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_metadata/page-007.json | DOC-003 PDF p.7 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A072 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_metadata/page-008.json | DOC-003 PDF p.8 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A073 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_metadata/page-009.json | DOC-003 PDF p.9 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A074 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_metadata/page-010.json | DOC-003 PDF p.10 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A075 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_text/page-002.txt | DOC-003 PDF p.2 | Legacy OCR, engine retained in supplied metadata | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A076 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_text/page-003.txt | DOC-003 PDF p.3 | Legacy OCR, engine retained in supplied metadata | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A077 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_text/page-004.txt | DOC-003 PDF p.4 | Legacy OCR, engine retained in supplied metadata | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A078 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_text/page-005.txt | DOC-003 PDF p.5 | Legacy OCR, engine retained in supplied metadata | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A079 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_text/page-006.txt | DOC-003 PDF p.6 | Legacy OCR, engine retained in supplied metadata | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A080 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_text/page-007.txt | DOC-003 PDF p.7 | Legacy OCR, engine retained in supplied metadata | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A081 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_text/page-008.txt | DOC-003 PDF p.8 | Legacy OCR, engine retained in supplied metadata | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A082 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_text/page-009.txt | DOC-003 PDF p.9 | Legacy OCR, engine retained in supplied metadata | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A083 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/ocr_text/page-010.txt | DOC-003 PDF p.10 | Legacy OCR, engine retained in supplied metadata | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A084 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/page_level_manifest.json | DOC-003 PDF pp.1-10 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A085 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-002.png | DOC-003 PDF p.2 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A086 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-003.png | DOC-003 PDF p.3 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A087 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-004.png | DOC-003 PDF p.4 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A088 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-005.png | DOC-003 PDF p.5 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A089 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-006.png | DOC-003 PDF p.6 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A090 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-007.png | DOC-003 PDF p.7 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A091 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-008.png | DOC-003 PDF p.8 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A092 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-009.png | DOC-003 PDF p.9 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A093 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-010.png | DOC-003 PDF p.10 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A094 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/results_supplement_extractor_response.md | DOC-003 PDF pp.1-10 | Legacy source-location evidence map | USABLE | Evidence-map locations only; no candidate selection reused |
| A095 | .ai_paper_validation/document_outputs/JAMA2019-10517-D04/document_record.yaml | DOC-004 PDF pp.1-1 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A096 | .ai_paper_validation/document_outputs/package_manifest.yaml | DOC-001, DOC-002, DOC-003, DOC-004 PDF pp.1-63 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A097 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-001.txt | DOC-001 PDF p.1 | Legacy native PDF text | USABLE | Readable source-linked text |
| A098 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-002.txt | DOC-001 PDF p.2 | Legacy native PDF text | USABLE | Readable source-linked text |
| A099 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-003.txt | DOC-001 PDF p.3 | Legacy native PDF text | USABLE | Readable source-linked text |
| A100 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-004.txt | DOC-001 PDF p.4 | Legacy native PDF text | USABLE | Readable source-linked text |
| A101 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-005.txt | DOC-001 PDF p.5 | Legacy native PDF text | USABLE | Readable source-linked text |
| A102 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-006.txt | DOC-001 PDF p.6 | Legacy native PDF text | USABLE | Readable source-linked text |
| A103 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-007.txt | DOC-001 PDF p.7 | Legacy native PDF text | USABLE | Readable source-linked text |
| A104 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-008.txt | DOC-001 PDF p.8 | Legacy native PDF text | USABLE | Readable source-linked text |
| A105 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-009.txt | DOC-001 PDF p.9 | Legacy native PDF text | USABLE | Readable source-linked text |
| A106 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/native_text/page-010.txt | DOC-001 PDF p.10 | Legacy native PDF text | USABLE | Readable source-linked text |
| A107 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/ocr_text/page-003.txt | DOC-001 PDF p.3 | Legacy OCR, engine retained in supplied metadata | USABLE | Source-linked transcription aid; direct-source authority retained |
| A108 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/ocr_text/page-005.txt | DOC-001 PDF p.5 | Legacy OCR, engine retained in supplied metadata | USABLE | Source-linked transcription aid; direct-source authority retained |
| A109 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/page_ocr_metadata/page-003.json | DOC-001 PDF p.3 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A110 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/page_ocr_metadata/page-005.json | DOC-001 PDF p.5 | Source-location / extraction metadata | USABLE | Readable source-located metadata; historical scope restrictions ignored |
| A111 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/rendered_pages/page-003.png | DOC-001 PDF p.3 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A112 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/rendered_pages/page-005.png | DOC-001 PDF p.5 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A113 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/rendered_pages/page-006.png | DOC-001 PDF p.6 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A114 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/rendered_pages/page-007.png | DOC-001 PDF p.7 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A115 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/rendered_pages/page-008.png | DOC-001 PDF p.8 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A116 | .ai_paper_validation/preprocessing/JAMA2019-10517-D01/rendered_pages/page-009.png | DOC-001 PDF p.9 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A117 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-001.txt | DOC-003 PDF p.1 | Legacy native PDF text | USABLE | Readable source-linked text |
| A118 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-002.txt | DOC-003 PDF p.2 | Legacy native PDF text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A119 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-003.txt | DOC-003 PDF p.3 | Legacy native PDF text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A120 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-004.txt | DOC-003 PDF p.4 | Legacy native PDF text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A121 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-005.txt | DOC-003 PDF p.5 | Legacy native PDF text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A122 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-006.txt | DOC-003 PDF p.6 | Legacy native PDF text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A123 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-007.txt | DOC-003 PDF p.7 | Legacy native PDF text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A124 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-008.txt | DOC-003 PDF p.8 | Legacy native PDF text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A125 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-009.txt | DOC-003 PDF p.9 | Legacy native PDF text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A126 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/native_text/page-010.txt | DOC-003 PDF p.10 | Legacy native PDF text | PARTIAL | Chart text does not encode complete plotted content; corresponding rendering closes coverage |
| A127 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/rendered_pages/page-002.png | DOC-003 PDF p.2 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A128 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/rendered_pages/page-003.png | DOC-003 PDF p.3 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A129 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/rendered_pages/page-004.png | DOC-003 PDF p.4 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A130 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/rendered_pages/page-005.png | DOC-003 PDF p.5 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A131 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/rendered_pages/page-006.png | DOC-003 PDF p.6 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A132 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/rendered_pages/page-007.png | DOC-003 PDF p.7 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A133 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/rendered_pages/page-008.png | DOC-003 PDF p.8 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A134 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/rendered_pages/page-009.png | DOC-003 PDF p.9 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A135 | .ai_paper_validation/preprocessing/JAMA2019-10517-D03/rendered_pages/page-010.png | DOC-003 PDF p.10 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A136 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_all_pages.txt | DOC-002 PDF pp.1-42 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A137 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p01.txt | DOC-002 PDF p.1 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A138 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p02.txt | DOC-002 PDF p.2 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A139 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p03.txt | DOC-002 PDF p.3 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A140 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p04.txt | DOC-002 PDF p.4 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A141 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p05.txt | DOC-002 PDF p.5 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A142 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p06.txt | DOC-002 PDF p.6 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A143 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p07.txt | DOC-002 PDF p.7 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A144 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p08.txt | DOC-002 PDF p.8 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A145 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p09.txt | DOC-002 PDF p.9 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A146 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p10.txt | DOC-002 PDF p.10 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A147 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p11.txt | DOC-002 PDF p.11 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A148 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p12.txt | DOC-002 PDF p.12 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A149 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p13.txt | DOC-002 PDF p.13 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A150 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p14.txt | DOC-002 PDF p.14 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A151 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p15.txt | DOC-002 PDF p.15 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A152 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p16.txt | DOC-002 PDF p.16 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A153 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p17.txt | DOC-002 PDF p.17 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A154 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p18.txt | DOC-002 PDF p.18 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A155 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p19.txt | DOC-002 PDF p.19 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A156 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p20.txt | DOC-002 PDF p.20 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A157 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p21.txt | DOC-002 PDF p.21 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A158 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_pp01_21.txt | DOC-002 PDF pp.1-21 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A159 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_all_pages.txt | DOC-002 PDF pp.1-42 | Legacy native PDF text | USABLE | Readable source-linked text |
| A160 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p01.txt | DOC-002 PDF p.1 | Legacy native PDF text | USABLE | Readable source-linked text |
| A161 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p02.txt | DOC-002 PDF p.2 | Legacy native PDF text | USABLE | Readable source-linked text |
| A162 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p03.txt | DOC-002 PDF p.3 | Legacy native PDF text | USABLE | Readable source-linked text |
| A163 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p04.txt | DOC-002 PDF p.4 | Legacy native PDF text | USABLE | Readable source-linked text |
| A164 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p05.txt | DOC-002 PDF p.5 | Legacy native PDF text | USABLE | Readable source-linked text |
| A165 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p06.txt | DOC-002 PDF p.6 | Legacy native PDF text | USABLE | Readable source-linked text |
| A166 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p07.txt | DOC-002 PDF p.7 | Legacy native PDF text | USABLE | Readable source-linked text |
| A167 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p08.txt | DOC-002 PDF p.8 | Legacy native PDF text | USABLE | Readable source-linked text |
| A168 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p09.txt | DOC-002 PDF p.9 | Legacy native PDF text | USABLE | Readable source-linked text |
| A169 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p10.txt | DOC-002 PDF p.10 | Legacy native PDF text | USABLE | Readable source-linked text |
| A170 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p11.txt | DOC-002 PDF p.11 | Legacy native PDF text | USABLE | Readable source-linked text |
| A171 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p12.txt | DOC-002 PDF p.12 | Legacy native PDF text | USABLE | Readable source-linked text |
| A172 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p13.txt | DOC-002 PDF p.13 | Legacy native PDF text | USABLE | Readable source-linked text |
| A173 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p14.txt | DOC-002 PDF p.14 | Legacy native PDF text | USABLE | Readable source-linked text |
| A174 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p15.txt | DOC-002 PDF p.15 | Legacy native PDF text | USABLE | Readable source-linked text |
| A175 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p16.txt | DOC-002 PDF p.16 | Legacy native PDF text | USABLE | Readable source-linked text |
| A176 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p17.txt | DOC-002 PDF p.17 | Legacy native PDF text | USABLE | Readable source-linked text |
| A177 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p18.txt | DOC-002 PDF p.18 | Legacy native PDF text | USABLE | Readable source-linked text |
| A178 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p19.txt | DOC-002 PDF p.19 | Legacy native PDF text | USABLE | Readable source-linked text |
| A179 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p20.txt | DOC-002 PDF p.20 | Legacy native PDF text | USABLE | Readable source-linked text |
| A180 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_p21.txt | DOC-002 PDF p.21 | Legacy native PDF text | USABLE | Readable source-linked text |
| A181 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/native_pp01_21.txt | DOC-002 PDF pp.1-21 | Legacy native PDF text | USABLE | Readable source-linked text |
| A182 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/visual_p17.png | DOC-002 PDF p.17 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A183 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/visual_p21.png | DOC-002 PDF p.21 | Legacy PDF-page raster rendering | USABLE | Readable PNG source-page rendering |
| A184 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | DOC-002 PDF pp.22-42 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A185 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_native.txt | DOC-002 PDF pp.22-42 | Legacy native PDF text | USABLE | Readable source-linked text |
| A186 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-004_p1_layout.txt | DOC-004 PDF pp.1-1 | Poppler pdftotext layout | USABLE | Readable layout-preserving source text |
| A187 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-004_p1_native.txt | DOC-004 PDF pp.1-1 | Legacy native PDF text | USABLE | Readable source-linked text |

Inventoried and hashed assets: 187.

## Exact page-to-primary-asset map

The primary aid for each page is listed once below. Other individual assets above remain available as corroborating aids; no overlapping derivative increases unit counts. Main tables/flow/figure pages and every supplementary figure additionally have exact page-linked rendered assets listed above. The page mapping identifies zero uncovered units.

| Source | PDF page | Primary asset path | Asset location within aggregate |
|---|---:|---|---|
| DOC-001 | 1 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-001.txt | Entire per-page file |
| DOC-001 | 2 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-002.txt | Entire per-page file |
| DOC-001 | 3 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-003.txt | Entire per-page file |
| DOC-001 | 4 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-004.txt | Entire per-page file |
| DOC-001 | 5 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-005.txt | Entire per-page file |
| DOC-001 | 6 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-006.txt | Entire per-page file |
| DOC-001 | 7 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-007.txt | Entire per-page file |
| DOC-001 | 8 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-008.txt | Entire per-page file |
| DOC-001 | 9 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-009.txt | Entire per-page file |
| DOC-001 | 10 | .ai_paper_validation/document_outputs/JAMA2019-10517-D01/preprocessing/native_text/page-010.txt | Entire per-page file |
| DOC-002 | 1 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p01.txt | Entire per-page file |
| DOC-002 | 2 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p02.txt | Entire per-page file |
| DOC-002 | 3 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p03.txt | Entire per-page file |
| DOC-002 | 4 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p04.txt | Entire per-page file |
| DOC-002 | 5 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p05.txt | Entire per-page file |
| DOC-002 | 6 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p06.txt | Entire per-page file |
| DOC-002 | 7 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p07.txt | Entire per-page file |
| DOC-002 | 8 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p08.txt | Entire per-page file |
| DOC-002 | 9 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p09.txt | Entire per-page file |
| DOC-002 | 10 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p10.txt | Entire per-page file |
| DOC-002 | 11 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p11.txt | Entire per-page file |
| DOC-002 | 12 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p12.txt | Entire per-page file |
| DOC-002 | 13 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p13.txt | Entire per-page file |
| DOC-002 | 14 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p14.txt | Entire per-page file |
| DOC-002 | 15 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p15.txt | Entire per-page file |
| DOC-002 | 16 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p16.txt | Entire per-page file |
| DOC-002 | 17 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p17.txt | Entire per-page file |
| DOC-002 | 18 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p18.txt | Entire per-page file |
| DOC-002 | 19 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p19.txt | Entire per-page file |
| DOC-002 | 20 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p20.txt | Entire per-page file |
| DOC-002 | 21 | .ai_paper_validation/review_1_5_1/preprocessing/support_001/layout_p21.txt | Entire per-page file |
| DOC-002 | 22 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 1, source PDF page 22 |
| DOC-002 | 23 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 2, source PDF page 23 |
| DOC-002 | 24 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 3, source PDF page 24 |
| DOC-002 | 25 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 4, source PDF page 25 |
| DOC-002 | 26 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 5, source PDF page 26 |
| DOC-002 | 27 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 6, source PDF page 27 |
| DOC-002 | 28 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 7, source PDF page 28 |
| DOC-002 | 29 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 8, source PDF page 29 |
| DOC-002 | 30 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 9, source PDF page 30 |
| DOC-002 | 31 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 10, source PDF page 31 |
| DOC-002 | 32 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 11, source PDF page 32 |
| DOC-002 | 33 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 12, source PDF page 33 |
| DOC-002 | 34 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 13, source PDF page 34 |
| DOC-002 | 35 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 14, source PDF page 35 |
| DOC-002 | 36 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 15, source PDF page 36 |
| DOC-002 | 37 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 16, source PDF page 37 |
| DOC-002 | 38 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 17, source PDF page 38 |
| DOC-002 | 39 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 18, source PDF page 39 |
| DOC-002 | 40 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 19, source PDF page 40 |
| DOC-002 | 41 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 20, source PDF page 41 |
| DOC-002 | 42 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-002_pp22-42_layout.txt | Form-feed page segment 21, source PDF page 42 |
| DOC-003 | 1 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/native_text/page-001.txt | Entire per-page file |
| DOC-003 | 2 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-002.png | Entire rendered PDF page |
| DOC-003 | 3 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-003.png | Entire rendered PDF page |
| DOC-003 | 4 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-004.png | Entire rendered PDF page |
| DOC-003 | 5 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-005.png | Entire rendered PDF page |
| DOC-003 | 6 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-006.png | Entire rendered PDF page |
| DOC-003 | 7 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-007.png | Entire rendered PDF page |
| DOC-003 | 8 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-008.png | Entire rendered PDF page |
| DOC-003 | 9 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-009.png | Entire rendered PDF page |
| DOC-003 | 10 | .ai_paper_validation/document_outputs/JAMA2019-10517-D03/preprocessing/rendered_pages/page-010.png | Entire rendered PDF page |
| DOC-004 | 1 | .ai_paper_validation/review_1_5_1/preprocessing/support_002/DOC-004_p1_layout.txt | Entire per-page file |

## New targeted direct-source derivatives

These new artifacts are not reused assets and do not enter the frozen reused hash set. Engine: direct Poppler pdftoppm CPU rendering, command pattern `pdftoppm -f N -l N -scale-to 1800 -singlefile -png source.pdf output-prefix`; cross-source reviewer visually inspected all four. Text locators from direct pdftotext were stdout only.

| Artifact within review directory | Source location | Engine | Purpose |
|---|---|---|---|
| preprocessing/cross-main-p04.png | DOC-001 PDF p.4 | Poppler pdftoppm | Exact relapse endpoint text |
| preprocessing/cross-main-p05.png | DOC-001 PDF p.5 | Poppler pdftoppm | Exact metabolic sensitivity text |
| preprocessing/cross-plan-p12.png | DOC-002 PDF p.12 | Poppler pdftoppm | Exact planned relapse definition |
| preprocessing/cross-plan-p14.png | DOC-002 PDF p.14 | Poppler pdftoppm | Exact planned metabolic data handling |

Statistical pass 1 targeted derivatives: preprocessing/statistics_pass_1/protocol-p14.png and preprocessing/statistics_pass_1/protocol-p16.png correspond exactly to DOC-002 PDF pages 14 and 16, rendered and visually inspected using Poppler pdftoppm 26.01.0 on CPU. Exact commands and stdout-only direct text rereads are documented in statistics/relationship_inventory.md. These derivative files are new and do not enter reused-artifact hashes.

Initial screener new derivative: preprocessing/inclusion_screen/protocol-p10.png, DOC-002 PDF p.10, direct CPU Poppler pdftoppm 26.01.0, command and visual inspection recorded in screening/inclusion_screen.md. Source page confirms the glycemic designation in a screened-out observation. It is excluded from the frozen reused-artifact set.
