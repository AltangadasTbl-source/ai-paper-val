# Fresh Evidence-Asset Inventory

## Preparation boundary

This inventory was prepared afresh from the four direct PDF sources below. No pre-existing audit extraction, OCR, table asset, candidate artifact, or report was read or used as evidence. There are no direct Office, workbook, or CSV sources.

## Native-text method and tool identity

The standard Linux executables \`pdfinfo\`, \`pdftotext\`, \`pdftoppm\`, \`pdftocairo\`, \`tesseract\`, \`libreoffice\`, and \`soffice\` were not available on \`PATH\` or in \`/usr/bin\` and \`/usr/local/bin\`. No permitted Linux PDF renderer was found. \`pandoc\` was present but was not used because it does not natively extract or render supplied PDFs. A separate Windows-path Tesseract executable existed but its direct \`--version\` invocation failed with \`WSL (2 - ) ERROR: UtilBindVsockAnyPort:307: socket failed 1\`; it was not used.

Fresh native text was instead extracted page-by-page by local 32-bit Adobe Acrobat COM automation using \`/mnt/c/Windows/SysWOW64/WindowsPowerShell/v1.0/powershell.exe\` and \`AcroExch.PDDoc\`, \`AcroExch.HiliteList\`, \`AcquirePage\`, \`CreatePageHilite\`, \`GetNumText\`, and \`GetText(segmentIndex)\`. The local script is \`preprocessing/extract_acrobat_native_text.ps1\`. It writes \`===== PDF PAGE N OF TOTAL =====\` before each page's direct Acrobat text segments, in UTF-8 without a byte-order mark. Source and output were accessed through explicit \`\\\\wsl.localhost\\Ubuntu\\...\` paths. The executed fixed form was:

\`\`\`text
/mnt/c/Windows/SysWOW64/WindowsPowerShell/v1.0/powershell.exe -NoProfile -ExecutionPolicy Bypass -File \\\\wsl.localhost\\Ubuntu\\...\\preprocessing\\extract_acrobat_native_text.ps1 -PdfPath \\\\wsl.localhost\\Ubuntu\\...\\SOURCE.pdf -OutputPath \\\\wsl.localhost\\Ubuntu\\...\\native_text\\DOC-NNN-acrobat-native.txt -DeclaredPageCount N
\`\`\`

This is direct, source-native text rather than OCR. It preserves page identity and text segment order but is not layout-preserving: display words and table cells can be separated across lines. The unavailable \`pdftotext -layout\` method remains a limitation for visual table alignment. No software was installed, no web resource was accessed, and no GPU was probed or used.

## Source-level assets and usability

| Source ID | Direct source and role | Declared units | Fresh assets | Native extraction outcome | Text usability and remaining limitation |
|---|---|---:|---|---|---|
| DOC-001 | \`jama_de_boer_2019_oi_190122.pdf\` — main article | 11 PDF pages | \`preprocessing/metadata/DOC-001_file_metadata.txt\`; \`preprocessing/native_text/DOC-001-acrobat-native.txt\` | Acrobat PDDoc reported 11 pages; 11 page markers; 78,971 Unicode characters. | Usable page-addressable native text for all 11 units. Segment-per-line ordering and unavailable layout extraction may require direct PDF visual confirmation for tables/figures when rendering becomes available. |
| DOC-002 | \`joi190122supp1_prod.pdf\` — Supplement 1 | 33 PDF pages | \`preprocessing/metadata/DOC-002_file_metadata.txt\`; \`preprocessing/native_text/DOC-002-acrobat-native.txt\` | Acrobat PDDoc reported 33 pages; 33 page markers; 154,569 Unicode characters. | Usable page-addressable native text for all 33 units. Segment-per-line ordering and unavailable layout extraction may require direct PDF visual confirmation for tables/figures when rendering becomes available. |
| DOC-003 | \`joi190122supp2_prod.pdf\` — Supplement 2 | 19 PDF pages | \`preprocessing/metadata/DOC-003_file_metadata.txt\`; \`preprocessing/native_text/DOC-003-acrobat-native.txt\` | Acrobat PDDoc reported 19 pages; 19 page markers; 38,003 Unicode characters. | Usable page-addressable native text for all 19 units. Segment-per-line ordering and unavailable layout extraction may require direct PDF visual confirmation for tables/figures when rendering becomes available. |
| DOC-004 | \`joi190122supp3_prod.pdf\` — Supplement 3 | 1 PDF page | \`preprocessing/metadata/DOC-004_file_metadata.txt\`; \`preprocessing/native_text/DOC-004-acrobat-native.txt\` | Acrobat PDDoc and the final linearization page count both report 1 page; 1 page marker; 1,274 Unicode characters. The three raw `/Type /Page` occurrences are successive incremental revisions of the same page object, not three source units. | Usable page-addressable native text for the one final PDF page. Segment-per-line ordering and unavailable layout extraction may require direct PDF visual confirmation for tables/figures when rendering becomes available. |

## Additional fresh fallback assets

Four earlier fresh \`strings -a\` byte-string captures remain under \`preprocessing/native_text/\` as non-page-addressable fallback records. They were not used to assess scientific content after valid Acrobat native text became available, and are not substitutes for the page-marked Acrobat extraction.

## Rendering and OCR status

No result-relevant page image was created because \`pdftoppm\` and \`pdftocairo\` were unavailable. Consequently no direct CPU OCR was performed: Tesseract requires a rendered image input, and the only located executable was nonfunctional in this environment. This is a tooling limitation, not a claim that all source text is visually unambiguous.

| Asset class | Count | Notes |
|---|---:|---|
| Direct PDF sources prepared | 4 | DOC-001 through DOC-004; 64 declared PDF-page units. |
| File metadata captures | 4 | One per direct PDF. |
| Fresh Acrobat page-marked native-text files | 4 | 64 declared page markers total; native text accessible for all 64 units. |
| Native \`pdftotext\` captures | 0 | Executable unavailable. |
| Layout \`pdftotext -layout\` captures | 0 | Executable unavailable. |
| Byte-string fallback captures | 4 | Not used as scientific text evidence after Acrobat extraction. |
| Rendered result-relevant page images | 0 | Permitted renderer unavailable. |
| Direct CPU Tesseract OCR outputs | 0 | No rendered input and executable unavailable/nonfunctional. |
| Office conversions/structure assets | 0 | No direct Office source. |

## Handoff limitation

Fresh preparation establishes source identity, integrity, and page-addressable native text for every one of the 64 declared source pages. Quantitative mapping may proceed from the fresh Acrobat outputs, while treating layout-sensitive table/figure interpretation as a documented evidence gap pending a permitted direct visual method.
