# Fresh Direct-Source Inventory

This source-first inventory includes only the direct research sources. Package instructions, workflow controls, `.codex` presets, Windows metadata, failed rendering experiments, and legacy audit derivatives are outside the evidence chain.

| Source ID | Package-relative source path | Type | Size (bytes) | SHA-256 | Stable units | Likely role | Fresh extraction method | Result-relevant scope |
|---|---|---|---:|---|---:|---|---|---|
| DOC-001 | jama_wang_2018_oi_180070.pdf | PDF 1.4 | 505453 | f921847452d4f5ab012a3eaaa58f25542a73c2f06a858974efc443be4af70fb9 | 10 PDF pages | Main research article | Installed local Acrobat COM direct word extraction and coordinate-layout extraction, complete for pp. 1-10. | All pp. 1-10: abstract, narrative, tables, figures/captions, notes, and result displays. |
| DOC-002 | joi180070supp1_prod.pdf | PDF 1.5 | 735518 | 5faf07d9e18fb1b9dcc415818622846fb502b410d67255be7ab28aca5e52d138 | 25 PDF pages | First supplied supplement/support document | Installed local Acrobat COM direct word extraction and coordinate-layout extraction, complete for pp. 1-25. | All pp. 1-25: protocol/support narrative, result-relevant definitions, tables, figures/captions, notes, and numeric displays. |
| DOC-003 | joi180070supp2_prod.pdf | PDF 1.5 | 334922 | 78ebed75675211c520c6eae88b8a1963c9b1f00dc66b2b6ff324d957a1e39645 | 9 PDF pages | Second supplied supplement/support document | Installed local Acrobat COM direct word extraction and coordinate-layout extraction, complete for pp. 1-9. | All pp. 1-9: eAppendix, eTables, definitions, footnotes, and numeric displays. |

## Source classification notes

- Stable IDs preserve main article first, then supplied support PDFs.
- No DOC, DOCX, XLS, XLSX, or CSV direct sources are present.
- `jama_wang_2018_oi_180070.pdf:Zone.Identifier` is operating-system metadata, not a research source.
- The failed `capture_window.ps1` and `rendered_pages/*test.png` files are non-evidence experiments and are not used for mapping.
- No pre-existing audit output was used as evidence.
