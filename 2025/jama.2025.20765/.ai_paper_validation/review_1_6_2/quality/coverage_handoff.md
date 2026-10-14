# Coverage and reusable-asset fitness handoff

# Direct-source inventory

Curator runtime: 01a12c3a-ad69-7ce3-9b2b-fe66c6bb1a9e; canonical task: /root/asset_curator; model gpt-6.1-sol; reasoning effort medium.

The package contains exactly three direct PDFs. No supplied DOC, DOCX, XLS, XLSX, or CSV source exists outside the audit/tooling area. Software dependency test data inside the new fallback environment are not supplied scientific sources. Every PDF page is a stable unit, including front matter and administrative pages. Earlier exclusions do not constrain this run.

| Source ID | Source path | Format | Unit type | Total units | Document role | Content basis |
|---|---|---|---|---:|---|---|
| DOC-001 | jama_zahid_2025_oi_250093_1768590553.08463.pdf | PDF 1.4 | PDF_PAGE | 9 | REPORT | Published cluster randomized clinical trial article, with abstract, methods, participant flow, tables, figures and results. |
| DOC-002 | joi250093supp1_prod_1768590553.08963.pdf | PDF 1.6 | PDF_PAGE | 109 | PLAN | Bound study protocol versions, amendment/change note, statistical analysis plan, and prospective intervention SMS materials; table of contents visually confirms this content. |
| DOC-003 | joi250093supp2_prod_1768590553.09463.pdf | PDF 1.6 | PDF_PAGE | 16 | REPORT | Non-plan results supplement: contents, steering committee, eTables and eFigure. |

No bundle mixes REPORT results and PLAN specifications. DOC-002 contains multiple PLAN components. All direct sources are unencrypted. PDF counts were confirmed using the recorded missing-capability fallback: `.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py info SOURCE`; engine PyMuPDF 1.26.4. Direct `file` and `sha256sum` were available. Hashes are recorded with package-relative paths in `source_hashes_before.sha256`.

All pages of each source are assigned to downstream mapping. DOC-001 goes to the main mapper. DOC-002 pp. 1-109 and DOC-003 pp. 1-16 go to support mapping; visual PLAN mapping must be sharded within the 32 rendered-page context bound.

# Complete source-coverage ledger

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_zahid_2025_oi_250093_1768590553.08463.pdf | PDF_PAGE | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-002 | joi250093supp1_prod_1768590553.08963.pdf | PDF_PAGE | 109 | 109 | 0 | 109 | COMPLETE |
| DOC-003 | joi250093supp2_prod_1768590553.09463.pdf | PDF_PAGE | 16 | 16 | 0 | 16 | COMPLETE |

Total unique units: 134; reusable: 134; fresh-required: 0; mapped finally: 134. Rendered pages are eligible reusable evidence assets under the contract. Reusable assets do not constitute completed scientific mapping. Every page requires a fresh mapper review; only the extraction burden is reusable.

Exact reusable partition: DOC-001 pp. 1-9 have native/normalized text and a whole-document layout extraction. DOC-002 pp. 1-109 have rendered JPEG page locators; garbled layout text does not contribute text coverage. DOC-003 pp. 1-2 have reusable 1.5.1 layout text, and pp. 3-16 have normalized text plus rendered images. No unit lacks usable reusable evidence entirely.

Derivative limitations: DOC-002 native/layout text is semantically garbled; 12 OCR files are empty and seven nonempty OCR pages have variable quality. Every DOC-002 page must therefore be inspected from its rendered image; targeted new OCR is optional as a transcription aid. The initial DOC-003 manifest covers only pp. 3-16, but later layout assets close pp. 1-2. Prior inventory exclusions have no effect on this run. New mapper artifacts cover all 134 units; all mapped counts and COMPLETE statuses are now closed.

# Reusable evidence-asset inventory

Curator: /root/asset_curator; runtime 01a12c3a-ad69-7ce3-9b2b-fe66c6bb1a9e. This inventory contains 386 eligible legacy extraction/metadata/image artifacts. Each is preserved and hashed with its package-relative path in reused_artifact_hashes_before.sha256. There are no supplied workbook, CSV, Office-structure or independent table-extraction assets. Scientific reviewer/checker/candidate/screening/quality/report outputs were excluded entirely. Files named extractor_response and processing_status were not used as source-linked extraction evidence. Legacy inventory and preprocessing metadata are used only for document identity and location mapping; their older exclusions do not bound coverage.

## Fitness and unique-unit accounting

DOC-001: 9/9 pages have usable native/normalized text; full layout locators and selected figure/table images provide corroboration. DOC-003: pp. 1-2 are covered by later layout text; pp. 3-16 by normalized text and images. DOC-002: 109/109 pages have readable rendered JPEG locators at 180 dpi (1530 by 1980), while its layout extraction is semantically garbled. Twelve of its 19 OCR files are empty. Nonempty OCR pp. 29, 41, 77, 78, 82, 83 and 96 are PARTIAL aids, and p. 96 is particularly sparse. Unique units are counted once across overlapping assets: total 134, reusable 134, fresh-required 0. Complete new scientific mapping is still mandatory for every page. In particular, all PLAN pages need visual reading; empty/garbled text must never be substituted for that reading. Targeted new approved GPU OCR may aid transcription but is not required to make the rendered locators eligible.

`USABLE` means source-matched, accessible locator/transcription aid; it does not establish any scientific finding. `PARTIAL` metadata or OCR contributes only its explicitly named locations and needs image confirmation. `UNREADABLE` denotes empty or garbled text. `DUPLICATE` denotes a second full-document or image representation of locations already mapped by canonical assets. No asset was found to have a demonstrated source-identity mismatch requiring STALE. Source-matching uses exact source names, page counts, page manifests, page identifiers and sampled content; source PDFs remain final authority.

## Engines and command provenance

Existing normalized/native text was produced by native PDF extraction according to preserved page manifests; exact historical engine versions are not recorded. Existing layout text is a pdftotext-style native layout extraction, with historical version unrecorded. Existing OCR engine/version is not documented; no engine attribution is fabricated. Existing rendered pages carry page-number identifiers; DOC-002 JPEGs are 180 dpi. Images in legacy evidence_recheck and main_mapper_direct are raw rendered locators only; adjacent legacy scientific records are not read. New PDF page counts use bundled pdf_tools.py info with PyMuPDF 1.26.4 because direct pdfinfo is absent. Hashes use direct sha256sum. No new extraction, rendering or OCR was performed by the curator.

All listed paths below are package-relative, exact files; no unresolved wildcard defines review scope. Every image maps to its source PDF page, and whole-document text maps to the stated full range. The mapper should select canonical per-page text/images, while alternate representations remain optional locators and preserved provenance.


## Numeric relationship enumeration

| N ID | Recorded status |
|---|---|
| N001 | COMPLETE |
| N002 | COMPLETE |
| N003 | COMPLETE |
| N004 | COMPLETE |
| N005 | COMPLETE |
| N006 | COMPLETE |
| N007 | COMPLETE |
| N008 | COMPLETE |
| N009 | COMPLETE |
| N010 | COMPLETE |
| N011 | COMPLETE |
| N012 | COMPLETE |
| N013 | COMPLETE |
| N014 | COMPLETE |
| N015 | COMPLETE |
| N016 | COMPLETE |
| N017 | COMPLETE |
| N018 | COMPLETE |
| N019 | COMPLETE |
| N020 | COMPLETE |
| N021 | COMPLETE |
| N022 | COMPLETE |
| N023 | COMPLETE |
| N024 | COMPLETE |
| N025 | COMPLETE |
| N026 | COMPLETE |
| N027 | COMPLETE |
| N028 | COMPLETE |
| N029 | COMPLETE |
| N030 | COMPLETE |
| N031 | COMPLETE |
| N032 | COMPLETE |
| N033 | COMPLETE |
| N034 | COMPLETE |
| N035 | COMPLETE |
| N036 | COMPLETE |
| N037 | COMPLETE |
| N038 | COMPLETE |
| N039 | COMPLETE |
| N040 | COMPLETE |
| N041 | COMPLETE |
| N042 | COMPLETE |
| N043 | COMPLETE |
| N044 | COMPLETE |
| N045 | COMPLETE |
| N046 | COMPLETE |
| N047 | COMPLETE |
| N048 | COMPLETE |
| N049 | COMPLETE |
| N050 | COMPLETE |
| N051 | COMPLETE |
| N052 | COMPLETE |
| N053 | COMPLETE |
| N054 | COMPLETE |
| N055 | COMPLETE |
| N056 | COMPLETE |
| N057 | COMPLETE |
| N058 | COMPLETE |
| N059 | COMPLETE |
| N060 | COMPLETE |
| N061 | COMPLETE |
| N062 | COMPLETE |
| N063 | COMPLETE |
| N064 | COMPLETE |
| N065 | COMPLETE |
| N066 | COMPLETE |
| N067 | COMPLETE |
| N068 | COMPLETE |
| N069 | COMPLETE |
| N070 | COMPLETE |
| N071 | COMPLETE |
| N072 | COMPLETE |
| N073 | COMPLETE |
| N074 | COMPLETE |
| N075 | COMPLETE |
| N076 | COMPLETE |
| N077 | COMPLETE |
| N078 | COMPLETE |
| N079 | COMPLETE |
| N080 | COMPLETE |
| N081 | COMPLETE |
| N082 | COMPLETE |
| N083 | COMPLETE |
| N084 | COMPLETE |
| N085 | COMPLETE |
| N086 | COMPLETE |
| N087 | COMPLETE |
| N088 | COMPLETE |
| N089 | COMPLETE |
| N090 | COMPLETE |
| N091 | COMPLETE |
| N092 | COMPLETE |
| N093 | COMPLETE |
| N094 | COMPLETE |
| N095 | COMPLETE |
| N096 | COMPLETE |
| N097 | COMPLETE |
| N098 | COMPLETE |
| N099 | COMPLETE |
| N100 | COMPLETE |
| N101 | COMPLETE |
| N102 | COMPLETE |
| N103 | COMPLETE |
| N104 | COMPLETE |
| N105 | COMPLETE |
| N106 | COMPLETE |
| N107 | COMPLETE |
| N108 | COMPLETE |
| N109 | COMPLETE |
| N110 | COMPLETE |
| N111 | COMPLETE |
| N112 | COMPLETE |
| N113 | COMPLETE |
| N114 | COMPLETE |
| N115 | COMPLETE |
| N116 | COMPLETE |
| N117 | COMPLETE |
| N118 | COMPLETE |
| N119 | COMPLETE |
| N201 | COMPLETE |
| N202 | COMPLETE |
| N203 | COMPLETE |
| N204 | COMPLETE |
| N205 | COMPLETE |
| N206 | COMPLETE |
| N207 | COMPLETE |
| N208 | COMPLETE |
| N209 | COMPLETE |
| N210 | COMPLETE |
| N211 | COMPLETE |
| N212 | COMPLETE |
| N213 | COMPLETE |
| N214 | COMPLETE |
| N215 | COMPLETE |
| N216 | COMPLETE |
| N217 | COMPLETE |
| N218 | COMPLETE |
| N219 | COMPLETE |
| N220 | COMPLETE |
| N221 | COMPLETE |
| N222 | COMPLETE |
| N223 | COMPLETE |
| N224 | COMPLETE |
| N225 | COMPLETE |
| N226 | COMPLETE |
| N227 | COMPLETE |
| N228 | COMPLETE |
| N229 | COMPLETE |
| N230 | COMPLETE |
| N231 | COMPLETE |
| N232 | COMPLETE |
| N233 | COMPLETE |
| N234 | COMPLETE |
| N235 | COMPLETE |
| N236 | COMPLETE |
| N237 | COMPLETE |
| N238 | COMPLETE |
| N239 | COMPLETE |
| N240 | COMPLETE |
| N241 | COMPLETE |
| N242 | COMPLETE |
| N243 | COMPLETE |
| N244 | COMPLETE |
| N245 | COMPLETE |
| N246 | COMPLETE |
| N247 | COMPLETE |
| N248 | COMPLETE |
| N249 | COMPLETE |
| N250 | COMPLETE |
| N251 | COMPLETE |
| N252 | COMPLETE |
| N253 | COMPLETE |
| N254 | COMPLETE |
| N255 | COMPLETE |
| N256 | COMPLETE |
| N257 | COMPLETE |
| N258 | COMPLETE |
| N259 | COMPLETE |
| N260 | COMPLETE |
| N261 | COMPLETE |
| N262 | COMPLETE |
| N263 | COMPLETE |
| N264 | COMPLETE |
| N265 | COMPLETE |
| N266 | COMPLETE |
| N267 | COMPLETE |
| N268 | COMPLETE |
| N269 | COMPLETE |
| N270 | COMPLETE |
| N271 | COMPLETE |
| N272 | COMPLETE |
| N273 | COMPLETE |
| N274 | COMPLETE |
| N275 | COMPLETE |
| N276 | COMPLETE |
| N277 | COMPLETE |
| N278 | COMPLETE |
| N279 | COMPLETE |
| N280 | COMPLETE |
| N281 | COMPLETE |
| N282 | COMPLETE |
| N283 | COMPLETE |
| N284 | COMPLETE |
| N285 | COMPLETE |
| N286 | COMPLETE |
| N287 | COMPLETE |
| N288 | COMPLETE |
| N289 | COMPLETE |
| N290 | COMPLETE |
| N291 | COMPLETE |
| N292 | COMPLETE |
| N293 | COMPLETE |
