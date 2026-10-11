# Source-linked evidence asset inventory

Inventory scope: all existing extraction assets below the audit area, excluding this new run. There are 277 eligible artifact files: 238 native/layout/raw text pages; 31 rendered PNG files (30 unique, one byte-identical duplicate); two page manifests; five mixed-content document records; one mixed-content package source-location manifest. No OCR text, standalone extracted tables, workbook extraction, Office structure, CSV extraction or other eligible document/source-location map is present. All assets remain unchanged.

Fitness values apply to the artifact, not to whole-source coverage. Sparse graphic-only text is PARTIAL and is completed by the listed image for the same unit. The duplicate image is inventoried but not reused or included in reused_artifact_hashes_before.sha256. All other 276 files are hashed because their permitted source-linked evidence or metadata is reused. Unique page counts are computed as the union, with no extra units for overlapping derivatives or metadata.

Commands and engines: `rg --files --hidden` enumerated package files; `pdfinfo SOURCE` 26.01.0 established full stable source-page counts; direct `sha256sum -- PATH` hashed sources/assets; `file PATH` checked PNG readability and resolution. Every one of 238 page-text assets was compared with direct source using `cmp -s ASSET <(pdftotext MODE -f N -l N SOURCE -)` with Poppler 26.01.0: all matched byte-exactly. Main/results native_text files match `-layout`; their normalized_text files match `-raw`; support *_native files match default reading order; support *_layout files match `-layout`. The source-matching validation writes no fresh derivatives. Original main/results manifests record pdftotext/pdftoppm 26.01.0 with renders at 300 dpi; support renders have approximately 180 dpi dimensions, original renderer version not recorded independently. Images are source/page locators, to be viewed directly by mappers and checked against supplied PDFs when a stable candidate cites them. Engine provenance beyond what the local metadata records establish is not inferred.

Mixed metadata caveat: document/package records include eligible source identity and extraction metadata beside old scientific audit summaries. Initial metadata inspection exposed those summaries; none is used to define scientific coverage, relationships, discovery, findings or classification. Only identity/extraction/location metadata portions are eligible for reuse. All old scientific review files are excluded from input.

Exact visual complements: DOC-001 pp. 3,4,6,7,8; DOC-002 pp. 36,37,49,50,51,52,59,60,61,62; DOC-003 pp. 17-30; DOC-004 p. 2. Sparse graphic pages requiring visual mapping are DOC-002 pp. 51,52,62 and DOC-004 p. 2; DOC-003 tables require layout/spatial inspection. The text+image union covers every unit, leaving zero fresh-required units at inventory. No scientific mapping is claimed by this curation stage.

| Artifact path | Source ID | Exact source units | Evidence type / engine | Fitness | Reuse / gap action |
|---|---|---|---|---|---|
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/native_text/page-001.txt | DOC-001 | PDF p. 1 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/native_text/page-002.txt | DOC-001 | PDF p. 2 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/native_text/page-003.txt | DOC-001 | PDF p. 3 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/native_text/page-004.txt | DOC-001 | PDF p. 4 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/native_text/page-005.txt | DOC-001 | PDF p. 5 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/native_text/page-006.txt | DOC-001 | PDF p. 6 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/native_text/page-007.txt | DOC-001 | PDF p. 7 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/native_text/page-008.txt | DOC-001 | PDF p. 8 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/native_text/page-009.txt | DOC-001 | PDF p. 9 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/native_text/page-010.txt | DOC-001 | PDF p. 10 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/normalized_text/page-001.txt | DOC-001 | PDF p. 1 | Raw native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/normalized_text/page-002.txt | DOC-001 | PDF p. 2 | Raw native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/normalized_text/page-003.txt | DOC-001 | PDF p. 3 | Raw native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/normalized_text/page-004.txt | DOC-001 | PDF p. 4 | Raw native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/normalized_text/page-005.txt | DOC-001 | PDF p. 5 | Raw native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/normalized_text/page-006.txt | DOC-001 | PDF p. 6 | Raw native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/normalized_text/page-007.txt | DOC-001 | PDF p. 7 | Raw native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/normalized_text/page-008.txt | DOC-001 | PDF p. 8 | Raw native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/normalized_text/page-009.txt | DOC-001 | PDF p. 9 | Raw native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/normalized_text/page-010.txt | DOC-001 | PDF p. 10 | Raw native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/page_images/page-003.png | DOC-001 | PDF p. 3 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/page_images/page-004.png | DOC-001 | PDF p. 4 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/page_images/page-006.png | DOC-001 | PDF p. 6 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/page_images/page-007.png | DOC-001 | PDF p. 7 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/page_images/page-008.png | DOC-001 | PDF p. 8 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/preprocessing/page_manifest.md | DOC-001 | PDF pp. 1-10 | Page extraction/location manifest; recorded Poppler 26.01.0 | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-MAIN/record.md | DOC-001 | PDF pp. 1-10 | Source identity/extraction metadata; mixed legacy record | PARTIAL | Reuse metadata only; historical audit summaries excluded |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-SUPP-01-PROTOCOL/record.md | DOC-002 | PDF pp. 1-66 | Source identity/extraction metadata; mixed legacy record | PARTIAL | Reuse metadata only; historical audit summaries excluded |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-SUPP-02-SAP/record.md | DOC-003 | PDF pp. 1-40 | Source identity/extraction metadata; mixed legacy record | PARTIAL | Reuse metadata only; historical audit summaries excluded |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-SUPP-03-RESULTS/preprocessing/native_text/page-001.txt | DOC-004 | PDF p. 1 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-SUPP-03-RESULTS/preprocessing/native_text/page-002.txt | DOC-004 | PDF p. 2 | Layout text; pdftotext 26.01.0, source-exact | PARTIAL | Reuse with same-page render; mapper must inspect graphics |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-SUPP-03-RESULTS/preprocessing/normalized_text/page-001.txt | DOC-004 | PDF p. 1 | Raw native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-SUPP-03-RESULTS/preprocessing/normalized_text/page-002.txt | DOC-004 | PDF p. 2 | Raw native text; pdftotext 26.01.0, source-exact | PARTIAL | Reuse with same-page render; mapper must inspect graphics |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-SUPP-03-RESULTS/preprocessing/page_images/page-002.png | DOC-004 | PDF p. 2 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-SUPP-03-RESULTS/preprocessing/page_manifest.md | DOC-004 | PDF pp. 1-2 | Page extraction/location manifest; recorded Poppler 26.01.0 | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-SUPP-03-RESULTS/record.md | DOC-004 | PDF pp. 1-2 | Source identity/extraction metadata; mixed legacy record | PARTIAL | Reuse metadata only; historical audit summaries excluded |
| .ai_paper_validation/document_outputs/JAMA-2024-23898-SUPP-04-DATA-SHARING/record.md | DOC-005 | PDF p. 1 | Source identity/extraction metadata; mixed legacy record | PARTIAL | Reuse metadata only; historical audit summaries excluded |
| .ai_paper_validation/package_manifest.md | DOC-001, DOC-002, DOC-003, DOC-004, DOC-005 | PDF pp. 1-10; 1-66; 1-40; 1-2; 1 | Source identity/extraction metadata; mixed legacy record | PARTIAL | Reuse metadata only; historical audit summaries excluded |
| .ai_paper_validation/review_1_5_3/preprocessing/rechecker/doc004-page-002.png | DOC-004 | PDF p. 2 | Rendered PNG; Poppler or legacy render provenance as above | DUPLICATE | Not reused; byte-identical to DOC-004 preprocessing page-002.png |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-001.txt | DOC-002 | PDF p. 1 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-002.txt | DOC-002 | PDF p. 2 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-003.txt | DOC-002 | PDF p. 3 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-004.txt | DOC-002 | PDF p. 4 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-005.txt | DOC-002 | PDF p. 5 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-006.txt | DOC-002 | PDF p. 6 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-007.txt | DOC-002 | PDF p. 7 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-008.txt | DOC-002 | PDF p. 8 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-009.txt | DOC-002 | PDF p. 9 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-010.txt | DOC-002 | PDF p. 10 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-011.txt | DOC-002 | PDF p. 11 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-012.txt | DOC-002 | PDF p. 12 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-013.txt | DOC-002 | PDF p. 13 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-014.txt | DOC-002 | PDF p. 14 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-015.txt | DOC-002 | PDF p. 15 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-016.txt | DOC-002 | PDF p. 16 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-017.txt | DOC-002 | PDF p. 17 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-018.txt | DOC-002 | PDF p. 18 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-019.txt | DOC-002 | PDF p. 19 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-020.txt | DOC-002 | PDF p. 20 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-021.txt | DOC-002 | PDF p. 21 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-022.txt | DOC-002 | PDF p. 22 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-023.txt | DOC-002 | PDF p. 23 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-024.txt | DOC-002 | PDF p. 24 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-025.txt | DOC-002 | PDF p. 25 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-026.txt | DOC-002 | PDF p. 26 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-027.txt | DOC-002 | PDF p. 27 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-028.txt | DOC-002 | PDF p. 28 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-029.txt | DOC-002 | PDF p. 29 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-030.txt | DOC-002 | PDF p. 30 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-031.txt | DOC-002 | PDF p. 31 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-032.txt | DOC-002 | PDF p. 32 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-033.txt | DOC-002 | PDF p. 33 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-034.txt | DOC-002 | PDF p. 34 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-035.txt | DOC-002 | PDF p. 35 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-036.txt | DOC-002 | PDF p. 36 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-037.txt | DOC-002 | PDF p. 37 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-038.txt | DOC-002 | PDF p. 38 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-039.txt | DOC-002 | PDF p. 39 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-040.txt | DOC-002 | PDF p. 40 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-041.txt | DOC-002 | PDF p. 41 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-042.txt | DOC-002 | PDF p. 42 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-043.txt | DOC-002 | PDF p. 43 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-044.txt | DOC-002 | PDF p. 44 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-045.txt | DOC-002 | PDF p. 45 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-046.txt | DOC-002 | PDF p. 46 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-047.txt | DOC-002 | PDF p. 47 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-048.txt | DOC-002 | PDF p. 48 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-049.txt | DOC-002 | PDF p. 49 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-050.txt | DOC-002 | PDF p. 50 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-051.txt | DOC-002 | PDF p. 51 | Layout text; pdftotext 26.01.0, source-exact | PARTIAL | Reuse with same-page render; mapper must inspect graphics |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-052.txt | DOC-002 | PDF p. 52 | Layout text; pdftotext 26.01.0, source-exact | PARTIAL | Reuse with same-page render; mapper must inspect graphics |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-053.txt | DOC-002 | PDF p. 53 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-054.txt | DOC-002 | PDF p. 54 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-055.txt | DOC-002 | PDF p. 55 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-056.txt | DOC-002 | PDF p. 56 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-057.txt | DOC-002 | PDF p. 57 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-058.txt | DOC-002 | PDF p. 58 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-059.txt | DOC-002 | PDF p. 59 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-060.txt | DOC-002 | PDF p. 60 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-061.txt | DOC-002 | PDF p. 61 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-062.txt | DOC-002 | PDF p. 62 | Layout text; pdftotext 26.01.0, source-exact | PARTIAL | Reuse with same-page render; mapper must inspect graphics |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-063.txt | DOC-002 | PDF p. 63 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-064.txt | DOC-002 | PDF p. 64 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-065.txt | DOC-002 | PDF p. 65 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_layout/page-066.txt | DOC-002 | PDF p. 66 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-001.txt | DOC-002 | PDF p. 1 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-002.txt | DOC-002 | PDF p. 2 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-003.txt | DOC-002 | PDF p. 3 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-004.txt | DOC-002 | PDF p. 4 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-005.txt | DOC-002 | PDF p. 5 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-006.txt | DOC-002 | PDF p. 6 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-007.txt | DOC-002 | PDF p. 7 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-008.txt | DOC-002 | PDF p. 8 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-009.txt | DOC-002 | PDF p. 9 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-010.txt | DOC-002 | PDF p. 10 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-011.txt | DOC-002 | PDF p. 11 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-012.txt | DOC-002 | PDF p. 12 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-013.txt | DOC-002 | PDF p. 13 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-014.txt | DOC-002 | PDF p. 14 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-015.txt | DOC-002 | PDF p. 15 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-016.txt | DOC-002 | PDF p. 16 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-017.txt | DOC-002 | PDF p. 17 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-018.txt | DOC-002 | PDF p. 18 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-019.txt | DOC-002 | PDF p. 19 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-020.txt | DOC-002 | PDF p. 20 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-021.txt | DOC-002 | PDF p. 21 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-022.txt | DOC-002 | PDF p. 22 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-023.txt | DOC-002 | PDF p. 23 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-024.txt | DOC-002 | PDF p. 24 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-025.txt | DOC-002 | PDF p. 25 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-026.txt | DOC-002 | PDF p. 26 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-027.txt | DOC-002 | PDF p. 27 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-028.txt | DOC-002 | PDF p. 28 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-029.txt | DOC-002 | PDF p. 29 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-030.txt | DOC-002 | PDF p. 30 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-031.txt | DOC-002 | PDF p. 31 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-032.txt | DOC-002 | PDF p. 32 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-033.txt | DOC-002 | PDF p. 33 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-034.txt | DOC-002 | PDF p. 34 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-035.txt | DOC-002 | PDF p. 35 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-036.txt | DOC-002 | PDF p. 36 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-037.txt | DOC-002 | PDF p. 37 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-038.txt | DOC-002 | PDF p. 38 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-039.txt | DOC-002 | PDF p. 39 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-040.txt | DOC-002 | PDF p. 40 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-041.txt | DOC-002 | PDF p. 41 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-042.txt | DOC-002 | PDF p. 42 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-043.txt | DOC-002 | PDF p. 43 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-044.txt | DOC-002 | PDF p. 44 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-045.txt | DOC-002 | PDF p. 45 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-046.txt | DOC-002 | PDF p. 46 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-047.txt | DOC-002 | PDF p. 47 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-048.txt | DOC-002 | PDF p. 48 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-049.txt | DOC-002 | PDF p. 49 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-050.txt | DOC-002 | PDF p. 50 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-051.txt | DOC-002 | PDF p. 51 | Native text; pdftotext 26.01.0, source-exact | PARTIAL | Reuse with same-page render; mapper must inspect graphics |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-052.txt | DOC-002 | PDF p. 52 | Native text; pdftotext 26.01.0, source-exact | PARTIAL | Reuse with same-page render; mapper must inspect graphics |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-053.txt | DOC-002 | PDF p. 53 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-054.txt | DOC-002 | PDF p. 54 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-055.txt | DOC-002 | PDF p. 55 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-056.txt | DOC-002 | PDF p. 56 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-057.txt | DOC-002 | PDF p. 57 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-058.txt | DOC-002 | PDF p. 58 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-059.txt | DOC-002 | PDF p. 59 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-060.txt | DOC-002 | PDF p. 60 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-061.txt | DOC-002 | PDF p. 61 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-062.txt | DOC-002 | PDF p. 62 | Native text; pdftotext 26.01.0, source-exact | PARTIAL | Reuse with same-page render; mapper must inspect graphics |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-063.txt | DOC-002 | PDF p. 63 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-064.txt | DOC-002 | PDF p. 64 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-065.txt | DOC-002 | PDF p. 65 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc002_native/page-066.txt | DOC-002 | PDF p. 66 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-001.txt | DOC-003 | PDF p. 1 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-002.txt | DOC-003 | PDF p. 2 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-003.txt | DOC-003 | PDF p. 3 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-004.txt | DOC-003 | PDF p. 4 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-005.txt | DOC-003 | PDF p. 5 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-006.txt | DOC-003 | PDF p. 6 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-007.txt | DOC-003 | PDF p. 7 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-008.txt | DOC-003 | PDF p. 8 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-009.txt | DOC-003 | PDF p. 9 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-010.txt | DOC-003 | PDF p. 10 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-011.txt | DOC-003 | PDF p. 11 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-012.txt | DOC-003 | PDF p. 12 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-013.txt | DOC-003 | PDF p. 13 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-014.txt | DOC-003 | PDF p. 14 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-015.txt | DOC-003 | PDF p. 15 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-016.txt | DOC-003 | PDF p. 16 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-017.txt | DOC-003 | PDF p. 17 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-018.txt | DOC-003 | PDF p. 18 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-019.txt | DOC-003 | PDF p. 19 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-020.txt | DOC-003 | PDF p. 20 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-021.txt | DOC-003 | PDF p. 21 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-022.txt | DOC-003 | PDF p. 22 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-023.txt | DOC-003 | PDF p. 23 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-024.txt | DOC-003 | PDF p. 24 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-025.txt | DOC-003 | PDF p. 25 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-026.txt | DOC-003 | PDF p. 26 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-027.txt | DOC-003 | PDF p. 27 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-028.txt | DOC-003 | PDF p. 28 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-029.txt | DOC-003 | PDF p. 29 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-030.txt | DOC-003 | PDF p. 30 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-031.txt | DOC-003 | PDF p. 31 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-032.txt | DOC-003 | PDF p. 32 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-033.txt | DOC-003 | PDF p. 33 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-034.txt | DOC-003 | PDF p. 34 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-035.txt | DOC-003 | PDF p. 35 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-036.txt | DOC-003 | PDF p. 36 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-037.txt | DOC-003 | PDF p. 37 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-038.txt | DOC-003 | PDF p. 38 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-039.txt | DOC-003 | PDF p. 39 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_layout/page-040.txt | DOC-003 | PDF p. 40 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-001.txt | DOC-003 | PDF p. 1 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-002.txt | DOC-003 | PDF p. 2 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-003.txt | DOC-003 | PDF p. 3 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-004.txt | DOC-003 | PDF p. 4 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-005.txt | DOC-003 | PDF p. 5 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-006.txt | DOC-003 | PDF p. 6 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-007.txt | DOC-003 | PDF p. 7 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-008.txt | DOC-003 | PDF p. 8 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-009.txt | DOC-003 | PDF p. 9 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-010.txt | DOC-003 | PDF p. 10 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-011.txt | DOC-003 | PDF p. 11 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-012.txt | DOC-003 | PDF p. 12 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-013.txt | DOC-003 | PDF p. 13 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-014.txt | DOC-003 | PDF p. 14 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-015.txt | DOC-003 | PDF p. 15 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-016.txt | DOC-003 | PDF p. 16 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-017.txt | DOC-003 | PDF p. 17 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-018.txt | DOC-003 | PDF p. 18 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-019.txt | DOC-003 | PDF p. 19 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-020.txt | DOC-003 | PDF p. 20 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-021.txt | DOC-003 | PDF p. 21 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-022.txt | DOC-003 | PDF p. 22 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-023.txt | DOC-003 | PDF p. 23 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-024.txt | DOC-003 | PDF p. 24 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-025.txt | DOC-003 | PDF p. 25 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-026.txt | DOC-003 | PDF p. 26 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-027.txt | DOC-003 | PDF p. 27 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-028.txt | DOC-003 | PDF p. 28 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-029.txt | DOC-003 | PDF p. 29 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-030.txt | DOC-003 | PDF p. 30 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-031.txt | DOC-003 | PDF p. 31 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-032.txt | DOC-003 | PDF p. 32 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-033.txt | DOC-003 | PDF p. 33 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-034.txt | DOC-003 | PDF p. 34 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-035.txt | DOC-003 | PDF p. 35 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-036.txt | DOC-003 | PDF p. 36 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-037.txt | DOC-003 | PDF p. 37 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-038.txt | DOC-003 | PDF p. 38 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-039.txt | DOC-003 | PDF p. 39 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc003_native/page-040.txt | DOC-003 | PDF p. 40 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc005_layout/page-001.txt | DOC-005 | PDF p. 1 | Layout text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/doc005_native/page-001.txt | DOC-005 | PDF p. 1 | Native text; pdftotext 26.01.0, source-exact | USABLE | Reuse; no uncovered unit |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc002-appendix-59.png | DOC-002 | PDF p. 59 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc002-appendix-60.png | DOC-002 | PDF p. 60 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc002-appendix-61.png | DOC-002 | PDF p. 61 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc002-appendix-62.png | DOC-002 | PDF p. 62 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc002-recruitment-49.png | DOC-002 | PDF p. 49 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc002-recruitment-50.png | DOC-002 | PDF p. 50 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc002-recruitment-51.png | DOC-002 | PDF p. 51 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc002-recruitment-52.png | DOC-002 | PDF p. 52 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc002-schedule-36.png | DOC-002 | PDF p. 36 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc002-schedule-37.png | DOC-002 | PDF p. 37 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc003-dummy-17.png | DOC-003 | PDF p. 17 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc003-dummy-18.png | DOC-003 | PDF p. 18 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc003-dummy-19.png | DOC-003 | PDF p. 19 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc003-dummy-20.png | DOC-003 | PDF p. 20 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc003-dummy-21.png | DOC-003 | PDF p. 21 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc003-dummy-22.png | DOC-003 | PDF p. 22 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc003-dummy-23.png | DOC-003 | PDF p. 23 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc003-dummy-24.png | DOC-003 | PDF p. 24 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc003-dummy-25.png | DOC-003 | PDF p. 25 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc003-dummy-26.png | DOC-003 | PDF p. 26 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc003-dummy-27.png | DOC-003 | PDF p. 27 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc003-dummy-28.png | DOC-003 | PDF p. 28 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc003-dummy-29.png | DOC-003 | PDF p. 29 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |
| .ai_paper_validation/review_1_5_3/preprocessing/support_mapper/rendered/doc003-dummy-30.png | DOC-003 | PDF p. 30 | Rendered PNG; Poppler or legacy render provenance as above | USABLE | Reuse visual content; mapper must inspect image |

## Fresh confirmation derivatives produced during mapping

| Artifact path | Source ID | Exact source units | Evidence type / engine | Fitness | Reuse / gap action |
|---|---|---|---|---|---|
| .ai_paper_validation/review_1_6_2/preprocessing/sap-results-doc003-page032.png | DOC-003 | PDF p.32 | Fresh direct-source PNG; pdftoppm 26.01.0, 150 dpi, CPU | USABLE | Supplemental glyph confirmation of a reusable-backed page; not part of reused-asset hash set |

| Artifact path | Source ID | Exact source units | Evidence type / engine | Fitness | Reuse / gap action |
|---|---|---|---|---|---|
| .ai_paper_validation/review_1_6_2/preprocessing/protocol/page-27.png | DOC-002 | PDF p.27 | Fresh PNG; pdftoppm 26.01.0, 120 dpi, CPU | USABLE | Supplemental direct-source visual confirmation |
| .ai_paper_validation/review_1_6_2/preprocessing/protocol/page-47.png | DOC-002 | PDF p.47 | Fresh PNG; pdftoppm 26.01.0, 120 dpi, CPU | USABLE | Supplemental direct-source visual confirmation |
| .ai_paper_validation/review_1_6_2/preprocessing/protocol/page-48.png | DOC-002 | PDF p.48 | Fresh PNG; pdftoppm 26.01.0, 120 dpi, CPU | USABLE | Supplemental direct-source visual confirmation |

## Mechanical source-recheck derivatives

All five derivatives use direct CPU Poppler pdftoppm 26.01.0, default 150 DPI before the recorded longest-side pixel constraint. No fixed final output DPI is claimed; no OCR was needed. Exact commands are in verification/evidence_recheck.md. These are fresh confirmation derivatives of reusable-backed units, excluded from the reused-asset hash set.

| Artifact path | Source ID | Exact source units | Evidence type / engine | Fitness | Reuse / gap action |
|---|---|---|---|---|---|
| .ai_paper_validation/review_1_6_2/preprocessing/recheck-main-3.png | DOC-001 | PDF p.3 | Fresh PNG; pdftoppm 26.01.0, CPU, -scale-to 1700 | USABLE | Exact visual recheck |
| .ai_paper_validation/review_1_6_2/preprocessing/recheck-main-6.png | DOC-001 | PDF p.6 | Fresh PNG; pdftoppm 26.01.0, CPU, -scale-to 1700 | USABLE | Exact visual recheck |
| .ai_paper_validation/review_1_6_2/preprocessing/recheck-main-7.png | DOC-001 | PDF p.7 | Fresh PNG; pdftoppm 26.01.0, CPU, -scale-to 1700 | USABLE | Exact visual recheck |
| .ai_paper_validation/review_1_6_2/preprocessing/recheck-main-8.png | DOC-001 | PDF p.8 | Fresh PNG; pdftoppm 26.01.0, CPU, -scale-to 1700 | USABLE | Exact visual recheck |
| .ai_paper_validation/review_1_6_2/preprocessing/recheck-subgroup-2.png | DOC-004 | PDF p.2 | Fresh PNG; pdftoppm 26.01.0, CPU, -scale-to 1900 | USABLE | Exact visual recheck |

## Pass-2 occurrence source-recheck derivatives

All nine use direct CPU Poppler pdftoppm 26.01.0 at 110 dpi, command pattern pdftoppm -r 110 -f N -l N -singlefile -png SOURCE OUTPUT_PREFIX. Exact commands and source locations are recorded in verification/parts/pass_2_occurrence_recheck.md. These fresh derivatives are excluded from the reused-asset hash set.

| Artifact path | Source ID | Exact source units | Evidence type / engine | Fitness | Reuse / gap action |
|---|---|---|---|---|---|
| .ai_paper_validation/review_1_6_2/preprocessing/pass2-recheck-sap-20.png | DOC-003 | PDF p.20 | Fresh PNG; pdftoppm 26.01.0, 110 dpi, CPU | USABLE | Exact added-occurrence source confirmation |
| .ai_paper_validation/review_1_6_2/preprocessing/pass2-recheck-sap-21.png | DOC-003 | PDF p.21 | Fresh PNG; pdftoppm 26.01.0, 110 dpi, CPU | USABLE | Exact added-occurrence source confirmation |
| .ai_paper_validation/review_1_6_2/preprocessing/pass2-recheck-sap-25.png | DOC-003 | PDF p.25 | Fresh PNG; pdftoppm 26.01.0, 110 dpi, CPU | USABLE | Exact added-occurrence source confirmation |
| .ai_paper_validation/review_1_6_2/preprocessing/pass2-recheck-sap-26.png | DOC-003 | PDF p.26 | Fresh PNG; pdftoppm 26.01.0, 110 dpi, CPU | USABLE | Exact added-occurrence source confirmation |
| .ai_paper_validation/review_1_6_2/preprocessing/pass2-recheck-protocol-17.png | DOC-002 | PDF p.17 | Fresh PNG; pdftoppm 26.01.0, 110 dpi, CPU | USABLE | Exact added-occurrence source confirmation |
| .ai_paper_validation/review_1_6_2/preprocessing/pass2-recheck-protocol-18.png | DOC-002 | PDF p.18 | Fresh PNG; pdftoppm 26.01.0, 110 dpi, CPU | USABLE | Exact added-occurrence source confirmation |
| .ai_paper_validation/review_1_6_2/preprocessing/pass2-recheck-protocol-31.png | DOC-002 | PDF p.31 | Fresh PNG; pdftoppm 26.01.0, 110 dpi, CPU | USABLE | Exact added-occurrence source confirmation |
| .ai_paper_validation/review_1_6_2/preprocessing/pass2-recheck-main-4.png | DOC-001 | PDF p.4 | Fresh PNG; pdftoppm 26.01.0, 110 dpi, CPU | USABLE | Exact added-occurrence source confirmation |
| .ai_paper_validation/review_1_6_2/preprocessing/pass2-recheck-subgroup-2.png | DOC-004 | PDF p.2 | Fresh PNG; pdftoppm 26.01.0, 110 dpi, CPU | USABLE | Exact added-occurrence source confirmation |
