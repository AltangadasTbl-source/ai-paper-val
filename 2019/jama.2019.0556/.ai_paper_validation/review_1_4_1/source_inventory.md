# Direct Source Inventory

## Scope and method

This is a read-only inventory of direct paper-package sources. The package root was searched for PDF, DOC, DOCX, XLS, XLSX, and CSV files while excluding the workflow implementation directory, audit derivatives, and Git metadata. Five direct sources were found, all PDF files. No Office or CSV direct source is present.

Page counts, dimensions, file sizes, and PDF versions were obtained with `pdfinfo`; SHA-256 values were computed directly with `sha256sum`. The computed hashes match the source-integrity values in the reusable preprocessing manifest. Direct sources were not modified.

## Sources

| Document ID | Package-relative source | Classification from document map | Pages | Bytes | PDF version | SHA-256 |
|---|---|---|---:|---:|---:|---|
| DOC-001 / DOC-001-MAIN | `jama_bot_2019_oi_190007.pdf` | Main article | 11 | 593783 | 1.4 | `74b85a4b77870fda5ff0ce2f8287a2533a11ee81745d4031155f4af2986bd980` |
| DOC-002 | `joi190007supp1_prod.pdf` | Protocol | 60 | 1334053 | 1.5 | `b8f3980eacaa908929e57fc6aadd4de0e7a5691a4978be0e2fe4b544455858db` |
| DOC-003 | `joi190007supp2_prod.pdf` | Statistical analysis plan | 5 | 102826 | 1.5 | `b14aaebd8fbded6d36e1ca618cc9f51f2c76d50e486a8c18b4fa56fb183bced7` |
| DOC-004 / DOC-004-RESULTS-SUPP | `joi190007supp3_prod.pdf` | Results supplement | 25 | 1049650 | 1.7 | `eeb826267cc5662b7736f625a226f37bdeb9ce8cfc6d7556d7ef6fdba5b53246` |
| DOC-005 | `joi190007supp4_prod.pdf` | Administrative/data-sharing statement | 1 | 21467 | 1.4 | `207c317e14618cc7fa6c86853e12ef03bebd2dff3676fa2383762ca248688641` |

Total direct-source scope is 5 PDFs and 102 PDF pages.

## Inventory boundaries

- All five PDFs are direct sources and remain the final authority for evidence confirmation.
- Legacy document classifications are retained only as stable identity metadata. Earlier scientific-scope or disposition fields do not constrain Workflow 1.4.1 discovery.
- No sibling package, external source, or web resource was inspected.
- Source hashes are reported here for identity; the coordinator owns the canonical `source_hashes_before.sha256` artifact.
