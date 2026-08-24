# Fresh preprocessing tool availability

Checked in the package working environment on 2026-08-24 UTC before source processing.

| Tool | Required use | Availability | Version / result | Consequence |
|---|---|---|---|---|
| `pdfinfo` | PDF metadata and independent page count | unavailable (`command -v` returned no path) | `NOT_INSTALLED_OR_ON_PATH` | No fresh `pdfinfo` metadata asset can be produced; page boundaries are instead recorded from direct extractor output. |
| `/mnt/c/Program Files/Git/mingw64/bin/pdftotext.exe` | Native PDF text | available with host permission and Windows UNC source/output paths | `pdftotext version 4.00` | Fresh native text was created for all six direct PDFs. |
| `/mnt/c/Program Files/Git/mingw64/bin/pdftotext.exe -layout` | Layout-preserving PDF text | available with host permission and Windows UNC source/output paths | `pdftotext version 4.00` | Fresh layout text was created for all six direct PDFs. |
| `pdftoppm` | Render result-relevant pages | unavailable (`command -v` returned no path) | `NOT_INSTALLED_OR_ON_PATH` | No fresh rendered-page image can be produced. |
| `pdftocairo` | Render result-relevant pages | unavailable (`command -v` returned no path) | `NOT_INSTALLED_OR_ON_PATH` | No fresh rendered-page image can be produced. |
| `tesseract` | CPU OCR only after unusable native/layout text | unavailable (`command -v` returned no path) | `NOT_INSTALLED_OR_ON_PATH` | OCR was not attempted: all source pages have non-empty native and layout text, no renderer is present, and the OCR backend is absent. |
| `libreoffice` / `soffice` | Office conversion | unavailable (`command -v` returned no path) | `NOT_INSTALLED_OR_ON_PATH` | Not applicable to this all-PDF direct-source set. |
| `file` | File/type inspection | available | `file-5.45` | Used to confirm PDF signatures and page-count strings. |
| `sha256sum` | Source integrity hashing | available | `GNU coreutils 9.4` | Used for fresh source hashes; the coordinator owns the canonical hash artifact. |
| `pandoc` | Report rendering only | available | `pandoc 3.1.3` | Not used to read, convert, or extract PDF evidence. |

No substitute PDF reader, converter, OCR engine, Python PDF library, web service, GPU tool, or pre-existing audit derivative was used. The workflow permits recording missing direct tools and continuing only unblocked work; it does not permit treating an unverified substitute or an old derivative as fresh evidence.

## Commands executed

```text
command -v pdfinfo
command -v pdftoppm
command -v pdftocairo
command -v tesseract
command -v libreoffice
command -v soffice
command -v pandoc
command -v file
command -v sha256sum
file -- <each direct PDF>
sha256sum -- <each direct PDF>
'/mnt/c/Program Files/Git/mingw64/bin/pdftotext.exe' -v
'/mnt/c/Program Files/Git/mingw64/bin/pdftotext.exe' -q "\\\\wsl.localhost\\Ubuntu\\...\\source.pdf" "\\\\wsl.localhost\\Ubuntu\\...\\preprocessing\\native_text\\DOC-XXX.txt"
'/mnt/c/Program Files/Git/mingw64/bin/pdftotext.exe' -q -layout "\\\\wsl.localhost\\Ubuntu\\...\\source.pdf" "\\\\wsl.localhost\\Ubuntu\\...\\preprocessing\\layout_text\\DOC-XXX.txt"
tr -cd '\\f' < <each text asset> | wc -c
```

The native command was run once for each DOC-001 through DOC-006 source, and then the layout command was run once for each source. The initial layout invocation placed `-layout` after the output argument and correctly produced no derivative; it was immediately rerun with valid option ordering (`-q -layout` before the source and output arguments). Only the successful assets listed in `evidence_asset_inventory.md` are evidence assets.
