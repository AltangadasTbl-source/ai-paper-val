# Fresh Direct-Source Inventory

Prepared from the package root on a source-first basis. Existing audit outputs were not consulted.

| Source ID | Package-relative source path | Type | Size (bytes) | SHA-256 | Units | Likely role | Fresh evidence availability |
|---|---|---|---:|---|---:|---|---|
| DOC-001 | jama_cooper_2018_oi_180132.pdf | PDF | 587537 | 14987ad9741b9c9f617a24af239ae72407ffe41ee14953df33665f1593e35253 | 10 PDF pages | Main randomized clinical-trial article; abstract, methods, participant flow, results, tables, figures, discussion, references | Native and layout text; PDF metadata; rendered PNG pages 1-10 |
| DOC-002 | joi180132supp1_prod.pdf | PDF | 8274204 | 305596802f9ac59c1e76fd9233529b98d92ef918d13fccd35112109ed60cb547 | 194 PDF pages | Supplement 1: historical and current POLAR protocols, SAP/update references, DSMC stopping rules and interim reports | Native and layout text; PDF metadata; rendered PNG pages 1-194 |
| DOC-003 | joi180132supp2_prod.pdf | PDF | 2045910 | b00fbac777719817be84e45f350898aa031a3eb6d17fb73a42de710239f1ab7d | 24 PDF pages | Supplement 2: supplementary results, eTables/eFigures, per-protocol, as-treated, and post-hoc analyses | Native and layout text; PDF metadata; rendered PNG pages 1-24 |
| DOC-004 | joi180132supp3_prod.pdf | PDF | 20983 | 7d6634553269ddfc0208a4e0d7b46639b8212f3126d59e3add8b4b033d42ebf3 | 1 PDF page | Supplement 3 data-sharing statement | Native and layout text; PDF metadata; rendered PNG page 1 |

## Page and content classification

- **DOC-001:** pages 1-8 contain title/abstract, methods, participant flow, results, outcome tables, figures, and discussion; page 9 contains author/contribution and disclosure material; page 10 contains references. The source is result-relevant overall, with primary visual evidence concentrated on pages 1 and 4-8.
- **DOC-002:** pages 1-51 contain the earlier protocol version and appendices; pages 52-138 contain the published/current protocol material and substudies; page 139 contains protocol-change material; pages 140-162 are embedded blank/non-substantive PDF pages; pages 163-179 contain historical appendix and amendment/change records; pages 180-187 contain ethics/SAP-update reference material and blank separator pages; pages 188-194 contain DSMC stopping-rule context, interim reports, tables, and figures. All pages were retained as fresh source units; results/quantitative-definition relevance is present across protocol/SAP/DSMC material, especially pages 14-15, 19, 25-28, 69-83, 108-132, 179, and 188-194.
- **DOC-003:** pages 1-24 are result-relevant supplementary content: eTables, eFigures, per-protocol/as-treated analyses, missingness/post-hoc analyses, and references.
- **DOC-004:** page 1 is a data-sharing statement. It contains no reported trial-result table or inferential result, but remains a complete direct-source unit.

## Direct-source tool observations

- `pdfinfo` identified 10, 194, 24, and 1 pages respectively; all four PDFs are unencrypted.
- No direct DOC, DOCX, XLS, XLSX, or CSV source was present in the package root. Therefore no Office conversion or Office structure extraction was applicable.
- Stable source IDs were assigned only from the direct supplied sources above and will be used by later stages.
