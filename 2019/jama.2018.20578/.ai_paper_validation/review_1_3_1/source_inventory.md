# Direct-Source Inventory

Inventory scope is the current paper-package root only. Every direct PDF, DOC, DOCX, XLS, XLSX, and
CSV was sought. Three PDFs were found; no Office or CSV source was present. All sources remain in place
and unchanged. Hashes are recorded in `source_hashes_before.sha256`.

| Document ID | Package-relative source | SHA-256 | Size | Pages | Direct inspection | Stable identity and role |
|---|---|---|---:|---:|---|---|
| DOC-001 | `jama_flint_2019_oi_190079.pdf` | `bc0a0760a27cbb664dd094b4ee12659acb000baf7c1207930f2558cb39affa45` | 473,952 bytes | 10 | PDF 1.4; unencrypted; text layer present on all pages | JAMA 2019 original investigation, Flint et al., DOI `10.1001/jama.2019.10517`; direct main-article source for its own document identity |
| DOC-002 | `joi180151supp1_prod.pdf` | `d47557e5447470a6d517fe82e52441b897d764ab96736d65d0e94ca564ce7e58` | 49,416 bytes | 7 | PDF 1.5; unencrypted; tagged; text layer present on all pages | Supplement 1 meta-analysis protocol, Zheng and Roddick, DOI `10.1001/jama.2018.20578` |
| DOC-003 | `joi180151supp2_prod.pdf` | `971a6088660ab2c02bbe5e73540d0c3231c779ca551a77a561295738500fb8a0` | 1,897,017 bytes | 29 | PDF 1.6; unencrypted; tagged; text layer present on all pages | Supplement 2 methods/tables/figures, Zheng and Roddick, DOI `10.1001/jama.2018.20578` |

## Identity and linkage note

The supplied filenames and internal identities represent two DOIs: DOC-001 identifies
`10.1001/jama.2019.10517`, while DOC-002 and DOC-003 identify `10.1001/jama.2018.20578`. This is a
source-identity fact, not a scientific disposition. All three direct sources are registered for
workflow 1.3.1 coverage, and downstream mapping must not import the old manifest's exclusion decision.

## Direct-source completeness

- PDF sources: 3 files, 46 pages.
- DOC/DOCX sources: 0.
- XLS/XLSX sources: 0.
- CSV sources: 0.
- Unreadable or encrypted sources: 0.
- Direct-source coverage gaps: none at the file/page identity level.

