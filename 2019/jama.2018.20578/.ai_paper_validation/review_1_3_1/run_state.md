# Workflow 1.3.1 Run State

- Profile: `1.3.1`
- Lane: `qc13_reuse_asset_curator`
- Curator completion timestamp: `2026-08-17T21:48:22-07:00`
- Status: `COMPLETE`
- Direct-source inventory: 3 PDF files, 46 PDF pages total, 3 hashes recorded.
- Reused-asset inventory: 47 files, 47 hashes recorded.
- Reused-asset fitness counts: 29 `USABLE`, 5 `PARTIAL`, 2 `STALE`, 11 `DUPLICATE`, 0 `UNREADABLE`.
- Source modification: none.
- Reused-artifact modification: none.
- Python use: none.
- OCR/rendering run: none; existing CPU OCR and rendered pages were only inventoried.

## Governing materials read completely

- `QUALITY_CONTROL_SCOPE.md`
- `workflow_1_3_1/review_contract.md`
- `workflow_1_3_1/report_spec.md`
- `workflow_1_3_1/settings.toml`
- `workflow1.3.1/.codex/agents/qc13-reuse-asset-curator.toml`

## Scientific-input boundary

Legacy `final_report.md`, candidate, queue, verifier, critic, endetail, quality, and workflow-response
outputs were not opened or used as scientific inputs. Existing `package_manifest.md` and the three
`document_record.md` files were read only as document-identity and source-location maps. Their old
scientific-scope dispositions are not carried into workflow 1.3.1.

## Integrity and fitness checks performed

1. Enumerated package-local files with `rg --files -uu`; no sibling package or web resource was used.
2. Hashed the three direct PDFs with `sha256sum --` and recorded package-relative paths.
3. Inspected each PDF with `file` and `pdfinfo`; all are readable, unencrypted, and expose the stated
   10, 7, and 29 pages.
4. Re-extracted all three PDFs to temporary files with `pdftotext -layout` and verified byte-for-byte
   equality to each full rights-screen text asset.
5. Re-extracted DOC-001 one page at a time with `pdftotext -layout -f N -l N` and verified byte-for-byte
   equality to all ten page-level native-text assets.
6. Verified that each normalized DOC-001 page is exactly its native page with only the terminal form-feed
   byte removed.
7. Verified that every OCR text, OCR metadata, native/normalized text, and rendered PNG is nonempty.
8. Inspected PNG identity with `file`; dimensions agree with the manifest DPI/page-size descriptions.
9. Hashed every eligible reused artifact individually with `sha256sum --`.

Temporary comparison files were created under `/tmp` and removed after comparison.

## Tool versions and availability

| Tool | Version or availability | Use in this lane |
|---|---|---|
| `sha256sum` | uutils coreutils 0.8.0 | Source and reused-artifact hashes |
| `file` | 5.46 | PDF type/page hint and PNG integrity/dimensions |
| `pdfinfo` | Poppler 26.01.0 | Direct-PDF metadata, encryption, and page counts |
| `pdftotext` | Poppler 26.01.0 | Temporary reproducibility comparisons using `-layout` |
| `pdftoppm` | Poppler 26.01.0 | Available; not invoked for new output |
| `pdftocairo` | Poppler 26.01.0 | Available; not invoked for new output |
| `tesseract` | 5.5.0, Leptonica 1.86.0 | Available; not invoked |
| `libreoffice` / `soffice` | LibreOffice 26.2.4.2 | Available; no Office sources present and not invoked for conversion |

## Curator limitations requiring downstream attention

- `.ai_paper_validation/preprocessing/DOC-001/page_manifest.json` is `STALE`: it states that OCR was
  not run or retained for pages 7 and 9 and not completed for page 8, but completed OCR text and
  metadata files are present for all three pages. It also reports a page-6 mean confidence different
  from the page-6 OCR metadata. Use the page-level files and metadata as the asset record; do not use
  the stale manifest to infer absence.
- DOC-001 page 8 native and normalized layout text has an unusable table reading order. A 150-dpi
  page image and completed OCR text/metadata are available, but any candidate must still be checked
  against direct PDF page 8.
- DOC-002 and DOC-003 have complete full-document layout text but no reusable page-level native files,
  rendered pages, or OCR. DOC-003 tables/figures on PDF pages 7-26 require direct-PDF confirmation and
  targeted rendering only if needed.
- The existing package/document maps contain prior-profile scope decisions. Their identity, page-count,
  source-hash, and heading-location facts are reusable; their old audit exclusions are not.

## Curator artifacts

- `source_inventory.md`
- `source_hashes_before.sha256`
- `reused_artifact_hashes_before.sha256`
- `evidence_asset_inventory.md`
- `source_coverage.md`

## Coordinator completion

- Overall workflow status: `COMPLETE`.
- Direct-source coverage: 3/3 PDFs and 46/46 pages.
- Relationship coverage: 76/76 numeric relationships; 53/53 statistical relationships in both
  mandatory passes; 30/30 cross-source match groups.
- Stable candidate set: C001-C024, all `Pending Human Adjudication`, conserved across ledger,
  evidence recheck, quality audit, Markdown report, and HTML report.
- Final source/reused-asset integrity recomputation: `PASS` for 3/3 direct sources and 47/47 reused
  artifacts.
- Final validator: `PASS`, with zero errors and zero warnings.
