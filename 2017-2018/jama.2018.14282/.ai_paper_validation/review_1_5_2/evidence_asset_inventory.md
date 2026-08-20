# Fresh evidence-asset inventory

## Source-only preprocessing record

This inventory was prepared from the four direct PDFs in the package. No pre-existing audit extraction, OCR, candidate, or report derivative was used as evidence. All assets below were newly created under `preprocessing/`.

| Source ID | Direct source | Role | PDF pages | Size (bytes) | SHA-256 | Native/layout outcome | Rendered pages | OCR |
|---|---|---|---:|---:|---|---|---|---|
| DOC-001 | `jama_azoulay_2018_oi_180109.pdf` | Main randomized clinical-trial article | 9 | 482157 | `515e58637dd5489fa605d597e7d637c52297a954616e3924f6fc14fa46d1f0b6` | Usable native and layout text for all 9 pages | 1-8 (8 pages) | 0 pages; no relevant page had unusable native/layout text |
| DOC-002 | `joi180109supp1_prod.pdf` | Protocol, final protocol, original statistical plan, and published protocol support | 129 | 1485227 | `8036657a65b8d2de9f209729822652f95ba1436079ce8e524d6538b64f7f87c3` | Usable native and layout text for all result-relevant pages; pp. 78 and 129 are sparse/non-result pages | 6-32, 36-55, 70, 72, 82-83, 90-107, 122-128 (76 pages; includes visual contextual pages alongside every result-relevant page) | 0 pages; sparse pp. 78 and 129 are non-result pages |
| DOC-003 | `joi180109supp2_prod.pdf` | Online eTable and eFigures support | 5 | 119596 | `13c31ed5f073920f8c5fcd98965e4ed6a19411480939559d4eb87a792276a868` | Usable native and layout text for all 5 pages | 1-5 (5 pages) | 0 pages; native/layout labels and values usable |
| DOC-004 | `joi180109supp3_prod.pdf` | Data-sharing statement | 1 | 29171 | `2fdd033524cf8076b380c2a1e9fe1bf12d2ad6b91e40781f50e3f2873442e528` | Usable native and layout text for its only page | None; page is context only | 0 pages; no result-relevant unit |

Total direct source units: **144 PDF pages**. Freshly mapped units: **144**. Rendered pages: **89** (every `RESULT_RELEVANT` page plus selected visual context). OCR pages: **0**.

## Tools and exact extraction methods

| Tool | Version observed | Method and output |
|---|---|---|
| `pdfinfo` | `pdfinfo version 26.01.0` | Direct metadata was saved per source in `preprocessing/pdfinfo/DOC-001_pdfinfo.txt` through `DOC-004_pdfinfo.txt`. |
| `pdftotext` | `pdftotext version 26.01.0` | Direct native text was saved once per complete source in `preprocessing/native_text/DOC-001.txt` through `DOC-004.txt`, then freshly re-extracted as one page-specific asset for every one of the 144 PDF pages under `preprocessing/native_text/pages/`. |
| `pdftotext -layout` | `pdftotext version 26.01.0` | Layout-preserving text was saved once per complete source in `preprocessing/layout_text/DOC-001.txt` through `DOC-004.txt`, then freshly re-extracted as one page-specific asset for every one of the 144 PDF pages under `preprocessing/layout_text/pages/`. |
| `pdftoppm` | `pdftoppm version 26.01.0` | Every result-relevant page, plus selected visual-context pages, was rendered at 200 dpi, one PNG per explicitly selected page, in `preprocessing/rendered_pages/`; 89 PNGs were produced. The largest source render scope (DOC-002) was handled as separate bounded page batches, each below the configured 32-page shard limit. |
| `tesseract` | `tesseract 5.5.0` | Not invoked. Direct native and layout text were usable for every result-relevant page. DOC-002 pp. 78 and 129 were sparse/blank but are non-result pages, so OCR would add no relevant evidence. CPU-only OCR policy was retained. |
| `sha256sum` | System utility | Source hashes were independently observed before this preprocessing; the authoritative package hash record is maintained separately in `source_hashes_before.sha256`. |

Exact direct command patterns used (with the actual quoted source path and output path substituted for each DOC ID) were:

```bash
pdfinfo "SOURCE.pdf" > preprocessing/pdfinfo/DOC-ID_pdfinfo.txt
pdftotext "SOURCE.pdf" preprocessing/native_text/DOC-ID.txt
pdftotext -layout "SOURCE.pdf" preprocessing/layout_text/DOC-ID.txt
pdftotext -f PAGE -l PAGE "SOURCE.pdf" preprocessing/native_text/pages/DOC-ID/pPAGE.txt
pdftotext -layout -f PAGE -l PAGE "SOURCE.pdf" preprocessing/layout_text/pages/DOC-ID/pPAGE.txt
pdftoppm -r 200 -f PAGE -l PAGE -singlefile -png "SOURCE.pdf" preprocessing/rendered_pages/DOC-ID-pPAGE
```

All `PAGE` values were explicit positive PDF-page numbers. The full per-page mapping, exact fresh text-asset paths, rendering decision, and OCR decision is in `preprocessing/page_unit_register.md`.

## Assets and coverage

| Asset family | Exact location | Count / scope |
|---|---|---|
| PDF metadata | `preprocessing/pdfinfo/` | 4 source-level `pdfinfo` records |
| Native full-source text | `preprocessing/native_text/DOC-001.txt` through `DOC-004.txt` | 4 assets, covering all sources |
| Native page text | `preprocessing/native_text/pages/` | 144 assets, one per PDF page |
| Layout full-source text | `preprocessing/layout_text/DOC-001.txt` through `DOC-004.txt` | 4 assets, covering all sources |
| Layout page text | `preprocessing/layout_text/pages/` | 144 assets, one per PDF page |
| Rendered source images | `preprocessing/rendered_pages/` | 89 result-relevant or visual-context PNGs |
| OCR text | `preprocessing/ocr_text/` | 0 assets; no applicable pages |
| Per-page text metric | `preprocessing/page_text_usability.tsv` | 144 rows; native and layout non-whitespace character counts |
| Per-page coverage register | `preprocessing/page_unit_register.md` | 144 stable source-page rows |

## Limitations

- DOC-002 pp. 78 and 129 have only 19 and 22 non-whitespace native characters respectively and are correspondingly sparse in layout extraction. They are consent/blank terminal material, not result-relevant content; no OCR was warranted.
- Figure plots are retained as 200-dpi source renders. Their native/layout text provides labels, visible numeric axes, and risk-set/table values where available; underlying plotted individual values are not supplied as tabular source data.
- No Office, workbook, CSV, or image-only direct source was present, so no conversion or Office-structure extraction was applicable.
