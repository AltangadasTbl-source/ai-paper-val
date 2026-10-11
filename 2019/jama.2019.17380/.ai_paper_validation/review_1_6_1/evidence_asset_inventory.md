# Reusable Evidence Asset Inventory

Inventory covers every eligible existing asset below the audit area. Only `.ai_paper_validation/review_1_5_2/preprocessing/` contains legacy assets: 57 files comprising four native text files, four layout text files, four PDF metadata records, 44 rendered page images, and one extraction provenance/page manifest. No OCR text, standalone table extraction, workbook extraction, or separate paragraph/cell/source-location map is present. No legacy scientific checker, candidate, screening, verifier, critic, endetail, classification or final-report content was read.

## Fitness and source identity

All eight native/layout files were compared with direct extraction from the exact current source using `cmp <(pdftotext "SOURCE.pdf" -) "ASSET.txt"` and `cmp <(pdftotext -layout "SOURCE.pdf" -) "ASSET.txt"`. All eight comparisons passed byte-for-byte. Direct `pdfinfo` agrees with each legacy document's page count. Form-feed page boundaries partition the files into exactly 11, 33, 19 and 1 nonempty source-page records. Native/layout assets are USABLE as source-matched transcription and location aids, not final authority for graphical content. All 44 images are readable PNGs with page-specific names, supported by the reusable rendering manifest; `file` confirms valid PNG headers and portrait/landscape dimensions. Protocol addendum cover p. 31 was visually inspected and matches its native/layout source content.

Fitness classification vocabulary: USABLE, PARTIAL, STALE, DUPLICATE, UNREADABLE. Every listed file is USABLE for its stated scope and purpose. Native/layout pairs are complementary reading orders, not duplicate artifacts; page metadata and manifest files establish identity/provenance but are not counted as independently extracted pages. The rendered-page collection is PARTIAL for DOC-002 (13 of 33 pages), with gaps pp. 1-10 and 21-30; it is complete for DOC-001, DOC-003 and DOC-004. Those 20 protocol pages remain reusable through source-matched text. There are no STALE or UNREADABLE assets and no missing source units.

## Engines, commands and unique coverage

- Text engines: direct Poppler `pdftotext`, current verification version 26.01.0. Legacy provenance records `pdftotext "SOURCE.pdf" "native_text/SOURCE.txt"` and `pdftotext -layout "SOURCE.pdf" "layout_text/SOURCE.txt"`; legacy engine version is not supplied.
- Metadata engine: direct Poppler `pdfinfo`; legacy provenance records `pdfinfo "SOURCE.pdf" > "metadata/SOURCE.pdfinfo.txt"`.
- Image engine: direct Poppler `pdftoppm`, current version 26.01.0; provenance records `pdftoppm -f N -l N -singlefile -png -r 180 "SOURCE.pdf" "rendered_pages/SOURCE-pN"`. Legacy version is not supplied. No OCR/GPU or new persistent extraction is used in curation.
- Integrity: `sha256sum` hashes every exact eligible asset path in `reused_artifact_hashes_before.sha256`. No reused artifact was modified.
- Unique reusable text-page coverage is DOC-001 pp. 1-11; DOC-002 pp. 1-33; DOC-003 pp. 1-19; DOC-004 p. 1. Total 64 unique pages; fresh-required 0. Existing visual renders cover 44 of those pages and add no duplicate units.

## Individual assets

Paths in this table are package-relative. Physical PDF pages identify source locations; form-feed ordinal N in text corresponds to PDF page N. Each image names exactly its physical page.

| Asset path | Asset type | Source ID | Exact source scope | Engine | Fitness | Use and limitation |
|---|---|---|---|---|---|---|
| .ai_paper_validation/review_1_5_2/preprocessing/extraction_log.md | PAGE_MANIFEST | DOC-001, DOC-002, DOC-003, DOC-004 | DOC-001 pp. 1-11; DOC-002 pp. 1-33; DOC-003 pp. 1-19; DOC-004 p. 1 | Recorded direct-tool commands | USABLE | Provenance and exact render-page list; no scientific selection input |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/jama_de_boer_2019_oi_190122.txt | LAYOUT_TEXT | DOC-001 | PDF pp. 1-11 | pdftotext -layout | USABLE | Source-matched layout and table alignment; graphics require visual evidence |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/joi190122supp1_prod.txt | LAYOUT_TEXT | DOC-002 | PDF pp. 1-33 | pdftotext -layout | USABLE | Source-matched layout and table alignment; graphics require visual evidence |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/joi190122supp2_prod.txt | LAYOUT_TEXT | DOC-003 | PDF pp. 1-19 | pdftotext -layout | USABLE | Source-matched layout and table alignment; graphics require visual evidence |
| .ai_paper_validation/review_1_5_2/preprocessing/layout_text/joi190122supp3_prod.txt | LAYOUT_TEXT | DOC-004 | PDF pp. 1-1 | pdftotext -layout | USABLE | Source-matched layout and table alignment; graphics require visual evidence |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/jama_de_boer_2019_oi_190122.pdfinfo.txt | DOCUMENT_RECORD | DOC-001 | PDF pp. 1-11 document identity | pdfinfo | USABLE | Page count and document metadata, not scientific text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/joi190122supp1_prod.pdfinfo.txt | DOCUMENT_RECORD | DOC-002 | PDF pp. 1-33 document identity | pdfinfo | USABLE | Page count and document metadata, not scientific text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/joi190122supp2_prod.pdfinfo.txt | DOCUMENT_RECORD | DOC-003 | PDF pp. 1-19 document identity | pdfinfo | USABLE | Page count and document metadata, not scientific text |
| .ai_paper_validation/review_1_5_2/preprocessing/metadata/joi190122supp3_prod.pdfinfo.txt | DOCUMENT_RECORD | DOC-004 | PDF pp. 1-1 document identity | pdfinfo | USABLE | Page count and document metadata, not scientific text |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/jama_de_boer_2019_oi_190122.txt | NATIVE_TEXT | DOC-001 | PDF pp. 1-11 | pdftotext | USABLE | Source-matched text; graphics require visual evidence |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/joi190122supp1_prod.txt | NATIVE_TEXT | DOC-002 | PDF pp. 1-33 | pdftotext | USABLE | Source-matched text; graphics require visual evidence |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/joi190122supp2_prod.txt | NATIVE_TEXT | DOC-003 | PDF pp. 1-19 | pdftotext | USABLE | Source-matched text; graphics require visual evidence |
| .ai_paper_validation/review_1_5_2/preprocessing/native_text/joi190122supp3_prod.txt | NATIVE_TEXT | DOC-004 | PDF pp. 1-1 | pdftotext | USABLE | Source-matched text; graphics require visual evidence |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p1.png | RENDERED_PAGE | DOC-001 | PDF p. 1 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p10.png | RENDERED_PAGE | DOC-001 | PDF p. 10 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p11.png | RENDERED_PAGE | DOC-001 | PDF p. 11 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p2.png | RENDERED_PAGE | DOC-001 | PDF p. 2 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p3.png | RENDERED_PAGE | DOC-001 | PDF p. 3 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p4.png | RENDERED_PAGE | DOC-001 | PDF p. 4 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p5.png | RENDERED_PAGE | DOC-001 | PDF p. 5 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p6.png | RENDERED_PAGE | DOC-001 | PDF p. 6 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p7.png | RENDERED_PAGE | DOC-001 | PDF p. 7 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p8.png | RENDERED_PAGE | DOC-001 | PDF p. 8 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p9.png | RENDERED_PAGE | DOC-001 | PDF p. 9 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p11.png | RENDERED_PAGE | DOC-002 | PDF p. 11 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p12.png | RENDERED_PAGE | DOC-002 | PDF p. 12 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p13.png | RENDERED_PAGE | DOC-002 | PDF p. 13 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p14.png | RENDERED_PAGE | DOC-002 | PDF p. 14 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p15.png | RENDERED_PAGE | DOC-002 | PDF p. 15 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p16.png | RENDERED_PAGE | DOC-002 | PDF p. 16 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p17.png | RENDERED_PAGE | DOC-002 | PDF p. 17 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p18.png | RENDERED_PAGE | DOC-002 | PDF p. 18 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p19.png | RENDERED_PAGE | DOC-002 | PDF p. 19 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p20.png | RENDERED_PAGE | DOC-002 | PDF p. 20 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p31.png | RENDERED_PAGE | DOC-002 | PDF p. 31 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p32.png | RENDERED_PAGE | DOC-002 | PDF p. 32 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p33.png | RENDERED_PAGE | DOC-002 | PDF p. 33 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p1.png | RENDERED_PAGE | DOC-003 | PDF p. 1 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p10.png | RENDERED_PAGE | DOC-003 | PDF p. 10 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p11.png | RENDERED_PAGE | DOC-003 | PDF p. 11 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p12.png | RENDERED_PAGE | DOC-003 | PDF p. 12 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p13.png | RENDERED_PAGE | DOC-003 | PDF p. 13 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p14.png | RENDERED_PAGE | DOC-003 | PDF p. 14 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p15.png | RENDERED_PAGE | DOC-003 | PDF p. 15 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p16.png | RENDERED_PAGE | DOC-003 | PDF p. 16 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p17.png | RENDERED_PAGE | DOC-003 | PDF p. 17 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p18.png | RENDERED_PAGE | DOC-003 | PDF p. 18 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p19.png | RENDERED_PAGE | DOC-003 | PDF p. 19 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p2.png | RENDERED_PAGE | DOC-003 | PDF p. 2 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p3.png | RENDERED_PAGE | DOC-003 | PDF p. 3 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p4.png | RENDERED_PAGE | DOC-003 | PDF p. 4 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p5.png | RENDERED_PAGE | DOC-003 | PDF p. 5 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p6.png | RENDERED_PAGE | DOC-003 | PDF p. 6 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p7.png | RENDERED_PAGE | DOC-003 | PDF p. 7 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p8.png | RENDERED_PAGE | DOC-003 | PDF p. 8 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p9.png | RENDERED_PAGE | DOC-003 | PDF p. 9 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |
| .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp3_prod-p1.png | RENDERED_PAGE | DOC-004 | PDF p. 1 | pdftoppm -r 180 | USABLE | Page-specific visual transcription aid; final authority is supplied PDF |

## Mapping handoff and gaps

Main mapper: all DOC-001 pp. 1-11, using native/layout assets and available renders. Support mapper: all DOC-002 pp. 1-33, DOC-003 pp. 1-19 and DOC-004 p. 1. The support scope includes the complete original protocol and analytic addendum, all table/figure pages and the data-sharing statement. Every page must receive a scientific evidence-map entry or an explicit no-applicable-relationship statement. Any graphical material absent from plain text must be inspected through an existing exact-page render or the supplied PDF. No fresh-required source unit exists at inventory; missing optional derivatives do not excuse missing scientific mapping.

## New targeted source-confirmation derivatives

These derivatives were produced during numeric checking, not reused from an earlier review. Direct CPU Poppler `pdftoppm` 26.01.0 rendered each exact supplied PDF page using `-f N -l N -singlefile -scale-to 1800 -png`. They close visual confirmation needs; the sources remain the evidence authority.

| New artifact | Direct source scope | Engine |
|---|---|---|
| preprocessing/numeric-main-p8.png | DOC-001 PDF p. 8 | pdftoppm 26.01.0 |
| preprocessing/numeric-main-p9.png | DOC-001 PDF p. 9 | pdftoppm 26.01.0 |
| preprocessing/numeric-supp2-p12.png | DOC-003 PDF p. 12 | pdftoppm 26.01.0 |
| preprocessing/numeric-supp2-p18.png | DOC-003 PDF p. 18 | pdftoppm 26.01.0 |
| preprocessing/numeric-supp2-p19.png | DOC-003 PDF p. 19 | pdftoppm 26.01.0 |

Pass-2 shard B produced `preprocessing/st2b-supp2-p17.png` from DOC-003 `joi190122supp2_prod.pdf` physical PDF p. 17 using direct CPU Poppler `pdftoppm` 26.01.0, command pattern `-f 17 -l 17 -singlefile -scale-to 1600 -png`. This is a new exact-page visual-confirmation derivative, not a reused asset, and does not change source-unit counts.
