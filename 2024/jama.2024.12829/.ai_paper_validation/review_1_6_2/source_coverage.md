# Complete direct-source coverage

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_sun_2024_oi_240088_1746815064.14747.pdf | PDF_PAGE | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 | joi240088supp1_prod_1746815064.21247.pdf | PDF_PAGE | 25 | 25 | 0 | 25 | COMPLETE |
| DOC-003 | joi240088supp2_prod_1746815064.36071.pdf | PDF_PAGE | 167 | 165 | 2 | 167 | COMPLETE |

Total unique source units: 203. Reusable units: 201. Fresh-required units: 2. Reusable and fresh-required units partition each source; overlapping derivatives are never counted twice. Mapped units total203 and are confirmed from the new mapper artifacts.

DOC-001 coverage: individual layout-preserving native-page text for every page 1-11, plus retained images for pages 5-9.

DOC-002 coverage: individual native-page text for pages 1-2 and 10-25 under document_outputs/basis_results_supplement; individual native/layout text for pages 3-9 under review_1_5_3/preprocessing/doc002_pp003-009. Images complete sparse or image-only figures on pages 6-13. Page 9 native/layout text is partial; its image and OCR provide reusable coverage. Page 12 OCR is empty, but its retained image is usable and must be inspected visually. Pages 10-13 sparse native text requires retained-image inspection.

DOC-003 coverage: individual native/layout text spans pages 1-167 across six disjoint retained preprocessing directories. Page 144 has only headers, line numbers, and a footer; its retained render confirms an otherwise blank page, so its native/layout text is usable for the full page. Embedded-table pages46 and48 required fresh rendering; their visual mapping closed those derivative gaps.

Derivative limitations: OCR is approximate and image-only content is not fully machine-readable; page images are the mandatory reuse aid for those units. These are derivative limitations, with no scientific coverage omitted. Source-linked extractions and legacy document records are retained unmodified; prior selection or exclusion statements are not carried forward.

Coordinator coverage correction: DOC-003 pp46 and48 need fresh rendering because their device tables are raster content absent from retained text and no retained image was found. The assigned plan mapper inspects preprocessing/plan-page-46.png and preprocessing/plan-page-48.png (CPU PyMuPDF 1.26.4, 200 dpi). Reusable count is therefore165 and fresh-required count2 for this source. The coverage table records this final partition. DOC-003 pp108-110 have usable retained renders and remain reusable-backed.

Scientific mapping completion: main mapper confirms DOC-00111/11, support mapper confirms DOC-00225/25 and DOC-003 tail7/7; three optional plan sharding agents confirm DOC-0031-64 (64/64),65-128 (64/64),129-160 (32/32). Union is203/203 mapped. Fresh rendering and visual inspection closed pp46/48. Merged support evidence is generated from all seven parts without scientific omissions.
