# Fresh Evidence-Asset Inventory

This inventory records fresh, source-only preprocessing attempts. No asset from an earlier audit was reused.

## Tool availability and actions

| Tool or method | Version/status | Exact source scope | Output path | Result and limitation |
|---|---|---|---|---|
| `file` | Available | DOC-001 through DOC-004 | None; command output recorded in this inventory | Confirmed PDF format/version for all sources. Its reported page count was not trusted where it represented a child page-tree count. |
| `sha256sum` | Available | DOC-001 through DOC-004 | `source_hashes_before.sha256` | Completed before preprocessing. |
| Raw PDF page-tree inspection | Available shell and local Perl `Compress::Zlib` structural fallback | DOC-001 pp. 1-11; DOC-002 pp. 1-37; DOC-003 pp. 1-7; DOC-004 pp. 1-14 | `preprocessing/tool_and_page_status.md` | Completed solely to establish exact page counts and one page-unit record per page. DOC-004 required decompression of its PDF object stream to read its root `/Count`; no text was decoded. |
| `pdfinfo` | Not found on PATH | All 69 PDF pages | No asset possible | Native PDF metadata call unavailable. |
| `pdftotext` | Not found on PATH | All 69 PDF pages | `preprocessing/native_text/` and `preprocessing/layout_text/` intentionally contain no fabricated output | Native and `-layout` text extraction unavailable. |
| `pdftoppm` / `pdftocairo` | Neither found on PATH | All 69 PDF pages | `preprocessing/rendered_pages/` intentionally contains no fabricated output | Result-relevant page rendering unavailable; visual table/figure identification could not be completed. |
| `tesseract` | Not found on PATH | No rendered pages available for OCR | `preprocessing/ocr_text/` intentionally contains no fabricated output | CPU OCR unavailable and not attempted without rendered inputs. No GPU was probed or used. |
| `libreoffice` / `soffice` | Neither found on PATH | Not applicable: no Office direct source | `preprocessing/converted_pdf/` and `preprocessing/office_structure/` | No Office conversion or structure extraction needed. |

## Reproducible command provenance

All commands below were run at the package root. They are limited to file identification, integrity hashing, command discovery, and PDF page-tree structure. They did not decode article prose, extract tables, render pages, perform OCR, or make scientific inferences.

### Available tools and versions

| Tool | Exact version output |
|---|---|
| `file` | `file-5.45`; `magic file from /etc/magic:/usr/share/misc/magic` |
| `sha256sum` | `sha256sum (GNU coreutils) 9.4` |
| Shell used for pipelines | `GNU bash, version 5.2.21(1)-release (x86_64-pc-linux-gnu)` |
| Page-tree fallback | `perl 5.38.2`; `Compress::Zlib 2.204` |
| `pdfinfo`, `pdftotext`, `pdftoppm`, `pdftocairo`, `tesseract`, `libreoffice`, `soffice` | Not found on PATH; no version exists to record in this runtime. |

### Exact inventory and integrity commands

```bash
file -- jama_parshuram_2018_oi_180015.pdf joi180015supp1_prod.pdf joi180015supp2_prod.pdf joi180015supp3_prod.pdf
sha256sum -- jama_parshuram_2018_oi_180015.pdf joi180015supp1_prod.pdf joi180015supp2_prod.pdf joi180015supp3_prod.pdf
command -v pdfinfo pdftotext pdftoppm pdftocairo tesseract libreoffice soffice || true
```

Relevant `file` output was `PDF document, version 1.4, 10 page(s)` for DOC-001; `PDF document, version 1.3, 8 page(s)` for DOC-002; `PDF document, version 1.5, 7 page(s)` for DOC-003; and `PDF document, version 1.6 (zip deflate encoded)` for DOC-004. The first two page values are child-tree counts, not root-page totals. The hash command output exactly matches `source_hashes_before.sha256`.

### Exact root `/Pages` count checks

For DOC-001, DOC-002, and DOC-003, the following read-only commands exposed the PDF page trees:

```bash
strings -n 3 -- jama_parshuram_2018_oi_180015.pdf | rg -n '/Type/Pages|/Count|/Type/Page[^s]' | tail -30
strings -n 3 -- joi180015supp1_prod.pdf | rg -n '/Type/Pages|/Count|/Type/Page[^s]' | head -40
strings -n 3 -- joi180015supp2_prod.pdf | rg -n '/Type/Pages|/Count|/Type/Page[^s]' | tail -30
```

The root nodes report `/Count 11` for DOC-001, `/Count 37` for DOC-002, and `/Count 7` for DOC-003. The DOC-001 parent lists child nodes with counts 10 and 1; DOC-002 parent lists child nodes with counts 8, 8, 8, 8, and 5. These reconciled totals establish 11 and 37 respectively.

DOC-004 stores the root `/Pages` object in a Flate-compressed PDF object stream, so `strings` alone cannot display its count. The following local, read-only structural fallback was run; it decompresses only objects labelled `ObjStm` and prints a stream only when it contains a page-tree or the object-number marker, without interpreting page content:

```bash
perl -MCompress::Zlib=uncompress -0777 -ne 'while(/(\d+)\s+(\d+)\s+obj\s*(<<.*?>>)\s*stream\r?\n(.*?)\r?\nendstream/sg){my($n,$d,$s)=($1,$3,$4); next unless $d=~/ObjStm/; my $u=uncompress($s); print "OBJECT $n\n$u\n" if defined($u) && ($u=~/(?:^|\s)71\s+0\s|\/Type\s*\/Pages|\/Count\b/)}' joi180015supp3_prod.pdf
```

Its relevant output is `71 0 72 52 73 143 <</Count 14/Kids[72 0 R 107 0 R 73 0 R]/Type/Pages>>`, which establishes DOC-004's root count of 14. This fallback was used solely because the required `pdfinfo` executable was absent.

## Fresh assets actually created

| Asset path | Scope | Method | Completeness |
|---|---|---|---|
| `preprocessing/tool_and_page_status.md` | Every PDF page, DOC-001 through DOC-004 | Direct local structural inspection plus command-availability checks | Complete page-unit status record; no scientific content extraction possible in this environment. |

## Result-relevant evidence limitation

Because neither native/layout extraction nor rendering is locally available, table, figure, caption, and result-specific page identification cannot be made reliably from the supplied PDFs in this preprocessing stage. Every page remains assigned and structurally mapped; downstream quantitative mapping must treat this as a source-access limitation rather than infer absent results.
