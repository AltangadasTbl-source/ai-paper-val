# Reusable Evidence-Asset Inventory — Workflow 1.5.1

This inventory covers eligible pre-existing evidence assets below `.ai_paper_validation/` only. It does not use legacy candidate, verifier, critic, checker, endetail, or final-report content as a discovery scope. All listed assets were hashed before scientific mapping in `reused_artifact_hashes_before.sha256`; no listed file was modified.

| Asset path | Asset class and method | Exact source location coverage | Coverage and fitness | Reuse decision / gap |
|---|---|---|---|---|
| .ai_paper_validation/document_outputs/package_manifest.md | Package document map, locally recorded PDF inventory | DOC-001 pp. 1–10; DOC-002 pp. 1–16; DOC-003 pp. 1–153; DOC-004 pp. 1–83; DOC-005 p. 1 | PARTIAL — source identity and page-count map only | Reuse for source identity; it does not substitute for page evidence. |
| .ai_paper_validation/document_outputs/JAMA2019-12618-MAIN/document_record.md | Document record | DOC-001 pp. 1–10 | USABLE — source identity, page count, and native-text availability | Reuse as document metadata only. |
| .ai_paper_validation/document_outputs/JAMA2019-12618-SUPP-RESULTS/document_record.md | Document record | DOC-002 pp. 1–16 | USABLE — source identity, page count, and native-text availability | Reuse as document metadata only. |
| .ai_paper_validation/document_outputs/JAMA2019-12618-PROTOCOL/document_record.md | Document record | DOC-003 pp. 1–3 headings; document identity pp. 1–153 | PARTIAL — no page-level reusable extraction | Fresh map DOC-003 pp. 1–153. |
| .ai_paper_validation/document_outputs/JAMA2019-12618-SAP/document_record.md | Document record | DOC-004 pp. 1–3 headings; document identity pp. 1–83 | PARTIAL — no page-level reusable extraction | Fresh map DOC-004 pp. 1–83. |
| .ai_paper_validation/document_outputs/JAMA2019-12618-DATA-SHARING/document_record.md | Document record | DOC-005 p. 1 | PARTIAL — record only; no page extraction | Fresh map DOC-005 p. 1. |
| .ai_paper_validation/preprocessing/manifests/JAMA2019-12618-MAIN-page-manifest.md | Page manifest for native PDF extraction | DOC-001 pp. 1–10, one named text file per page | USABLE — complete page-to-text map | Reuse with the 10 listed native-text assets. |
| .ai_paper_validation/preprocessing/manifests/JAMA2019-12618-SUPP-RESULTS-page-manifest.md | Page manifest for native PDF extraction | DOC-002 pp. 1–16, one named text file per page | USABLE — complete page-to-text map; p. 16 is intentionally sparse footnote text | Reuse with the 16 listed native-text assets. |
| .ai_paper_validation/document_outputs/JAMA2019-12618-MAIN/main_article_result_evidence.md | Source-location map | DOC-001 pp. 1–10, with result-location sections and selected visual confirmations on pp. 3 and 6 | PARTIAL — locator and transcription aid, not page-complete replacement evidence | Reuse as a locator; page-level native text supplies complete reusable coverage. |
| .ai_paper_validation/document_outputs/JAMA2019-12618-SUPP-RESULTS/result_relevant_evidence_map.md | Source-location map | DOC-002 pp. 8 and 10–16 result tables; contextual exclusions noted for pp. 1–7 and 9 | PARTIAL — result-location map, not a complete page extraction | Reuse as a locator; page-level native text supplies complete reusable coverage. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-001.txt | Native layout-preserving PDF text | DOC-001 p. 1 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-002.txt | Native layout-preserving PDF text | DOC-001 p. 2 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-003.txt | Native layout-preserving PDF text | DOC-001 p. 3 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-004.txt | Native layout-preserving PDF text | DOC-001 p. 4 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-005.txt | Native layout-preserving PDF text | DOC-001 p. 5 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-006.txt | Native layout-preserving PDF text | DOC-001 p. 6 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-007.txt | Native layout-preserving PDF text | DOC-001 p. 7 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-008.txt | Native layout-preserving PDF text | DOC-001 p. 8 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-009.txt | Native layout-preserving PDF text | DOC-001 p. 9 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-MAIN/native_text/page-010.txt | Native layout-preserving PDF text | DOC-001 p. 10 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-001.txt | Native layout-preserving PDF text | DOC-002 p. 1 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-002.txt | Native layout-preserving PDF text | DOC-002 p. 2 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-003.txt | Native layout-preserving PDF text | DOC-002 p. 3 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-004.txt | Native layout-preserving PDF text | DOC-002 p. 4 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-005.txt | Native layout-preserving PDF text | DOC-002 p. 5 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-006.txt | Native layout-preserving PDF text | DOC-002 p. 6 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-007.txt | Native layout-preserving PDF text | DOC-002 p. 7 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-008.txt | Native layout-preserving PDF text | DOC-002 p. 8 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-009.txt | Native layout-preserving PDF text | DOC-002 p. 9 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-010.txt | Native layout-preserving PDF text | DOC-002 p. 10 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-011.txt | Native layout-preserving PDF text | DOC-002 p. 11 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-012.txt | Native layout-preserving PDF text | DOC-002 p. 12 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-013.txt | Native layout-preserving PDF text | DOC-002 p. 13 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-014.txt | Native layout-preserving PDF text | DOC-002 p. 14 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-015.txt | Native layout-preserving PDF text | DOC-002 p. 15 | USABLE | Reuse. |
| .ai_paper_validation/preprocessing/JAMA2019-12618-SUPP-RESULTS/native_text/page-016.txt | Native layout-preserving PDF text | DOC-002 p. 16; eTable 9 footnotes | USABLE — sparse by source design, with nonzero text and manifest support | Reuse. |

## Asset-class totals and gaps

| Asset class | Existing assets | USABLE | PARTIAL | STALE | DUPLICATE | UNREADABLE | Direct-source unit gap |
|---|---:|---:|---:|---:|---:|---:|---|
| Native/layout text | 26 | 26 | 0 | 0 | 0 | 0 | None for DOC-001 pp. 1–10 and DOC-002 pp. 1–16; 237 units remain uncovered in DOC-003 through DOC-005. |
| OCR text | 0 | 0 | 0 | 0 | 0 | 0 | No existing OCR asset; no gap where usable native text exists. |
| Table/workbook extraction | 0 | 0 | 0 | 0 | 0 | 0 | No table/workbook source or extraction supplied. |
| Rendered page | 0 | 0 | 0 | 0 | 0 | 0 | No existing rendered-page asset. |
| Page manifest | 2 | 2 | 0 | 0 | 0 | 0 | No manifest for DOC-003 through DOC-005. |
| Document record / package map | 6 | 2 | 4 | 0 | 0 | 0 | Records identify all sources but do not provide page evidence for DOC-003 through DOC-005. |
| Source-location map | 2 | 0 | 2 | 0 | 0 | 0 | Maps are locators only; native text closes DOC-001 and DOC-002 page coverage. |

No eligible asset was classified STALE, DUPLICATE, or UNREADABLE. The 237 uncovered source pages are explicit fresh direct-source assignments in `source_coverage.md`.
