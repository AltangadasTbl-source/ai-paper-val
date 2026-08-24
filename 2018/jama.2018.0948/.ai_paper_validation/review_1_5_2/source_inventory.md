# Fresh Direct-Source Inventory

Prepared from the four supplied root-level PDFs only. No legacy audit derivative was inspected or used as evidence.

| Source ID | Package-relative source path | Type | Size (bytes) | SHA-256 | Stable PDF pages | Likely role | Fresh processing status |
|---|---|---|---:|---|---:|---|---|
| DOC-001 | jama_parshuram_2018_oi_180015.pdf | PDF 1.4 | 467257 | 92c3a3edd598a1073e39f8d0733352b3aea3bec30731b9ef0326e68f2e6088ba | 11 | Main JAMA article | Inventory and structural page mapping complete; direct text/layout/render/OCR tools unavailable. |
| DOC-002 | joi180015supp1_prod.pdf | PDF 1.3 | 444859 | 67409a1493b032cb49b26a4444e37eabeb2a432d2d0b5576914baac310490306 | 37 | Supplementary PDF 1; numbered supporting material | Inventory and structural page mapping complete; direct text/layout/render/OCR tools unavailable. |
| DOC-003 | joi180015supp2_prod.pdf | PDF 1.5 | 372878 | 6dab9fdc7fa6ca0da2031d5a483a58ba8ad9a3b0c6c4e7c45eb17708535465a4 | 7 | Supplementary PDF 2; numbered supporting material | Inventory and structural page mapping complete; direct text/layout/render/OCR tools unavailable. |
| DOC-004 | joi180015supp3_prod.pdf | PDF 1.6, compressed object streams | 237508 | 3b58616d0af25610fe9e4bab11ac42c7e38dae588e3d965ec306b8e5b55d1eb3 | 14 | Supplementary PDF 3; numbered supporting material; specific scientific content is indeterminate without text extraction or rendering | Inventory and structural page mapping complete; direct text/layout/render/OCR tools unavailable. |

## Page-count determination

`pdfinfo` was not installed. Counts were therefore determined from each PDF's root `/Pages` tree, not from the shallow heuristic emitted by `file`: DOC-001 root count 11; DOC-002 root count 37; DOC-003 root count 7; DOC-004 root count 14. DOC-004's root pages object is stored in a compressed PDF object stream; a local Perl `Compress::Zlib` read-only structural fallback decompressed that stream solely to inspect the `/Count 14` value. This was not text extraction, OCR, rendering, or scientific review.

The root-level `file` command identified DOC-001, DOC-002, and DOC-003 as 10, 8, and 7 pages respectively; the first two values reflect nested child `/Pages` nodes and are not their root-page totals.

## Direct-source scope

There are no root-level DOC, DOCX, XLS, XLSX, or CSV direct sources. All 69 direct source units are PDF pages. Specific supplementary contents cannot be reliably named without native/layout extraction or visual rendering; their numbered-support role is therefore intentionally conservative.
