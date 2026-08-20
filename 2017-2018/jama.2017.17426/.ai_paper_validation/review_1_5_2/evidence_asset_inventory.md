# Fresh Evidence-Asset Inventory

## Tools and execution environment

- `file` was used to classify direct sources: all were PDF documents.
- `sha256sum` was used to record direct-source checksums in the source inventory and the coordinator-owned hash artifact.
- `pdfinfo` version 26.01.0 (Poppler) was run directly on each PDF. All sources were unencrypted; page counts were 10, 69, and 2 respectively.
- `pdftotext` version 26.01.0 (Poppler) was run directly once in native mode and once with `-layout` for each PDF.
- `pdftoppm` version 26.01.0 (Poppler) was used at 180 dpi, PNG, only for the documented result-relevant pages.
- `tesseract` version 5.5.0 with `-l eng --psm 6` was used directly on CPU for the sole result-relevant page with unusable native/layout text (DOC-002 PDF page 66). No GPU was probed or used. No software was installed, no web resources were accessed, and no source was modified.

## Per-source asset register

| Source ID | Asset path | Method and exact source scope | Usability and limitation |
|---|---|---|---|
| DOC-001 | preprocessing/jama_thomas_2017_oi_170130.pdfinfo.txt | `pdfinfo -- jama_thomas_2017_oi_170130.pdf` | Metadata usable; confirms 10 pages and no encryption. |
| DOC-001 | preprocessing/native_text/jama_thomas_2017_oi_170130.txt | `pdftotext -- jama_thomas_2017_oi_170130.pdf ...` | Usable native text for all 10 pages (58,556 bytes). |
| DOC-001 | preprocessing/layout_text/jama_thomas_2017_oi_170130.layout.txt | `pdftotext -layout -- jama_thomas_2017_oi_170130.pdf ...` | Usable layout text for all 10 pages (103,420 bytes), including aligned tables. |
| DOC-001 | preprocessing/rendered_pages/DOC-001-p{1,2,3,4,5,6,7,8,9}.png | `pdftoppm -f N -l N -singlefile -png -r 180 -- jama_thomas_2017_oi_170130.pdf ...` for each enumerated N | Nine result-relevant pages rendered. Page 10 was not rendered because it is disclosures/references; text assets cover it. |
| DOC-002 | preprocessing/joi170130supp1_prod.pdfinfo.txt | `pdfinfo -- joi170130supp1_prod.pdf` | Metadata usable; confirms 69 pages and no encryption. |
| DOC-002 | preprocessing/native_text/joi170130supp1_prod.txt | `pdftotext -- joi170130supp1_prod.pdf ...` | Usable native text on 68 pages (117,698 bytes total); page 66 produced only a 69-character footer and was unsuitable for its flowchart. |
| DOC-002 | preprocessing/layout_text/joi170130supp1_prod.layout.txt | `pdftotext -layout -- joi170130supp1_prod.pdf ...` | Usable layout text on 68 pages (139,609 bytes total); page 66 likewise lacked the flowchart content. |
| DOC-002 | preprocessing/rendered_pages/DOC-002-p{1,5,7,8,9,10,11,12,13,14,15,16,25,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69}.png | `pdftoppm -f N -l N -singlefile -png -r 180 -- joi170130supp1_prod.pdf ...` for each enumerated N | Fifty-three pages rendered. This is the complete visual result-definition/protocol/SAP scope; administrative/consent/reference pages outside it retain fresh text/layout assets. |
| DOC-002 | preprocessing/ocr_text/DOC-002-p66.txt | `tesseract preprocessing/rendered_pages/DOC-002-p66.png preprocessing/ocr_text/DOC-002-p66 -l eng --psm 6` | OCR captured the SAP flowchart labels and placeholders. Some diagram text is imperfect (for example, line breaks and a few character substitutions); the rendered PNG is the authoritative visual evidence. |
| DOC-003 | preprocessing/joi170130supp2_prod.pdfinfo.txt | `pdfinfo -- joi170130supp2_prod.pdf` | Metadata usable; confirms 2 pages and no encryption. |
| DOC-003 | preprocessing/native_text/joi170130supp2_prod.txt | `pdftotext -- joi170130supp2_prod.pdf ...` | Usable native text for both pages (2,192 bytes). |
| DOC-003 | preprocessing/layout_text/joi170130supp2_prod.layout.txt | `pdftotext -layout -- joi170130supp2_prod.pdf ...` | Usable layout text for both pages (2,914 bytes), including the eTable's aligned columns. |
| DOC-003 | preprocessing/rendered_pages/DOC-003-p{1,2}.png | `pdftoppm -f N -l N -singlefile -png -r 180 -- joi170130supp2_prod.pdf ...` for each enumerated N | Both pages rendered; page 2 is the multiple-imputation eTable. |

## Extraction commands

The commands above were executed with fully resolved package-relative source paths. For each source, native text used `pdftotext -- SOURCE DESTINATION` and table-preserving text used `pdftotext -layout -- SOURCE DESTINATION`. Each PNG was produced with `pdftoppm -f N -l N -singlefile -png -r 180 -- SOURCE DESTINATION_PREFIX`. No OCR was run for pages whose relevant native/layout extraction was usable.

## Completeness and limitations

All three direct PDFs have fresh metadata, native text, and layout text. Rendering produced 64 selected result-relevant PNG pages (DOC-001: 9; DOC-002: 53; DOC-003: 2). One rendered page received targeted CPU OCR. DOC-002 page 66 is a graphical SAP flowchart whose native and layout text omit the diagram; reviewers should use its rendered PNG as primary evidence and the OCR only as a navigation aid. No other relevant native/layout text was unusable.
