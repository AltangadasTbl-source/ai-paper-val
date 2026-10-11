# Workflow 1.6.2 Evidence-Asset Inventory

Second-pass fresh source confirmations: preprocessing/statistical_pass_2/main-full.txt (DOC-001 pp. 1-11), plan-full.txt (DOC-002 pp. 1-33), and supp-full.txt (DOC-003 pp. 1-19), all produced by direct pdftotext 26.01.0 with -layout on CPU. They are new confirmation derivatives; reusable assets remain unchanged. Exact commands are recorded in checkers/statistical_pass_2.md.

The entire existing audit area was enumerated by pathname. Only preprocessing assets exist in the legacy audit directories: 63 files, comprising eight native/layout texts, four PDF metadata records, one extraction provenance log, 44 canonical rendered pages and six overlapping rendered pages. No legacy candidate, screening, verifier, critic, classification or final-report content was read. There are no pre-existing OCR texts, extracted table/workbook files, page manifests or separate document/source-location maps beyond the listed PDF metadata and extraction log. Every listed file is hashed individually in `reused_artifact_hashes_before.sha256`; all are preserved unchanged.

Fitness is assessed against current direct sources. Every native/layout asset exactly matches current direct `pdftotext` output by SHA-256; every metadata asset exactly matches current `pdfinfo` output by byte comparison. Page segmentation uses physical page order separated by form feeds, with the trailing empty segment excluded. All 64 real pages have meaningful extraction appropriate to their content. Images are valid PNGs identified by `file`; canonical images have recorded rendering commands in the extraction log. Image-only numbers on supplementary pp. 17-19 are present in the reusable rendered pages, even though their native/layout text is only a partial locator for the graphical display. Canonical images provide unique location coverage; six alternate images are DUPLICATE coverage and their legacy rendering engine is not documented in a permitted provenance record. They are unnecessary for unique page coverage.

Direct inventory tools: Poppler `pdfinfo`, `pdftotext` and `pdftoppm` 26.01.0; `sha256sum` uutils coreutils 0.10.0; `file` for image format. Compute device: CPU. No OCR, Office conversion, fallback helper or temporary environment was used. Original canonical engine versions are not documented; current source matching establishes the text/metadata fitness. No new derivative file was generated during curation.

Source checks used the exact four source paths in `source_inventory.md`:

- `pdfinfo "SOURCE.pdf"` and comparison with its cached metadata record.
- `pdftotext "SOURCE.pdf" - | sha256sum` and comparison with the native asset hash.
- `pdftotext -layout "SOURCE.pdf" - | sha256sum` and comparison with the layout asset hash.
- `sha256sum -- "SOURCE.pdf"` and `sha256sum -- "ASSET"` for integrity manifests.
- `file "ASSET.png"` for every PNG; visual readability was additionally checked on canonical supplementary p. 18 and alternate main p. 8.

The extraction provenance log records canonical `pdftoppm -f N -l N -singlefile -png -r 180 "SOURCE.pdf" "OUTPUT_PREFIX"` commands. This was historical CPU rendering, not a command rerun in this stage. Main images are 1530 x 1980; supplement 2 landscape pages are 1980 x 1530; supplement 3 is 1488 x 2105. Alternate images have 1600- or 1800-pixel long edges. Exact source page in every image row is its filename mapping, verified by source identity and accompanying text/provenance.

| Asset ID | Artifact path | Kind / engine | Exact source units | Fitness | Coverage and use |
|---|---|---|---|---|---|
| A001 | .ai_paper_validation/review_1_5_2/preprocessing/extraction_log.md | Extraction/source-location provenance / direct command log | DOC-001 pp. 1-11; DOC-002 pp. 1-33; DOC-003 pp. 1-19; DOC-004 p. 1 | USABLE | Command and rendering location metadata only; no scientific candidate content |
| A002 | .ai_paper_validation/review_1_5_2/preprocessing/layout_text/jama_de_boer_2019_oi_190122.txt | Layout text / pdftotext -layout | DOC-001 pp. 1-11 | USABLE | Source-matched row/column locator; form-feed page boundaries; image displays require images |
| A003 | .ai_paper_validation/review_1_5_2/preprocessing/layout_text/joi190122supp1_prod.txt | Layout text / pdftotext -layout | DOC-002 pp. 1-33 | USABLE | Source-matched row/column locator; form-feed page boundaries; image displays require images |
| A004 | .ai_paper_validation/review_1_5_2/preprocessing/layout_text/joi190122supp2_prod.txt | Layout text / pdftotext -layout | DOC-003 pp. 1-19 | USABLE | Source-matched row/column locator; form-feed page boundaries; image displays require images |
| A005 | .ai_paper_validation/review_1_5_2/preprocessing/layout_text/joi190122supp3_prod.txt | Layout text / pdftotext -layout | DOC-004 p. 1 | USABLE | Source-matched row/column locator; form-feed page boundaries; image displays require images |
| A006 | .ai_paper_validation/review_1_5_2/preprocessing/metadata/jama_de_boer_2019_oi_190122.pdfinfo.txt | PDF document record / pdfinfo | DOC-001 pp. 1-11 | USABLE | Current exact metadata match; page count and document identity; not quantitative evidence |
| A007 | .ai_paper_validation/review_1_5_2/preprocessing/metadata/joi190122supp1_prod.pdfinfo.txt | PDF document record / pdfinfo | DOC-002 pp. 1-33 | USABLE | Current exact metadata match; page count and document identity; not quantitative evidence |
| A008 | .ai_paper_validation/review_1_5_2/preprocessing/metadata/joi190122supp2_prod.pdfinfo.txt | PDF document record / pdfinfo | DOC-003 pp. 1-19 | USABLE | Current exact metadata match; page count and document identity; not quantitative evidence |
| A009 | .ai_paper_validation/review_1_5_2/preprocessing/metadata/joi190122supp3_prod.pdfinfo.txt | PDF document record / pdfinfo | DOC-004 p. 1 | USABLE | Current exact metadata match; page count and document identity; not quantitative evidence |
| A010 | .ai_paper_validation/review_1_5_2/preprocessing/native_text/jama_de_boer_2019_oi_190122.txt | Native text / pdftotext | DOC-001 pp. 1-11 | USABLE | Source-matched text locator; form-feed page boundaries; image displays require images |
| A011 | .ai_paper_validation/review_1_5_2/preprocessing/native_text/joi190122supp1_prod.txt | Native text / pdftotext | DOC-002 pp. 1-33 | USABLE | Source-matched text locator; form-feed page boundaries; image displays require images |
| A012 | .ai_paper_validation/review_1_5_2/preprocessing/native_text/joi190122supp2_prod.txt | Native text / pdftotext | DOC-003 pp. 1-19 | USABLE | Source-matched text locator; form-feed page boundaries; image displays require images |
| A013 | .ai_paper_validation/review_1_5_2/preprocessing/native_text/joi190122supp3_prod.txt | Native text / pdftotext | DOC-004 p. 1 | USABLE | Source-matched text locator; form-feed page boundaries; image displays require images |
| A014 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p1.png | Rendered page / pdftoppm 180 dpi | DOC-001 p. 1 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A015 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p10.png | Rendered page / pdftoppm 180 dpi | DOC-001 p. 10 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A016 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p11.png | Rendered page / pdftoppm 180 dpi | DOC-001 p. 11 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A017 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p2.png | Rendered page / pdftoppm 180 dpi | DOC-001 p. 2 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A018 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p3.png | Rendered page / pdftoppm 180 dpi | DOC-001 p. 3 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A019 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p4.png | Rendered page / pdftoppm 180 dpi | DOC-001 p. 4 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A020 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p5.png | Rendered page / pdftoppm 180 dpi | DOC-001 p. 5 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A021 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p6.png | Rendered page / pdftoppm 180 dpi | DOC-001 p. 6 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A022 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p7.png | Rendered page / pdftoppm 180 dpi | DOC-001 p. 7 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A023 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p8.png | Rendered page / pdftoppm 180 dpi | DOC-001 p. 8 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A024 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/jama_de_boer_2019_oi_190122-p9.png | Rendered page / pdftoppm 180 dpi | DOC-001 p. 9 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A025 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p11.png | Rendered page / pdftoppm 180 dpi | DOC-002 p. 11 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A026 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p12.png | Rendered page / pdftoppm 180 dpi | DOC-002 p. 12 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A027 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p13.png | Rendered page / pdftoppm 180 dpi | DOC-002 p. 13 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A028 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p14.png | Rendered page / pdftoppm 180 dpi | DOC-002 p. 14 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A029 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p15.png | Rendered page / pdftoppm 180 dpi | DOC-002 p. 15 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A030 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p16.png | Rendered page / pdftoppm 180 dpi | DOC-002 p. 16 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A031 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p17.png | Rendered page / pdftoppm 180 dpi | DOC-002 p. 17 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A032 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p18.png | Rendered page / pdftoppm 180 dpi | DOC-002 p. 18 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A033 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p19.png | Rendered page / pdftoppm 180 dpi | DOC-002 p. 19 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A034 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p20.png | Rendered page / pdftoppm 180 dpi | DOC-002 p. 20 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A035 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p31.png | Rendered page / pdftoppm 180 dpi | DOC-002 p. 31 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A036 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p32.png | Rendered page / pdftoppm 180 dpi | DOC-002 p. 32 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A037 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp1_prod-p33.png | Rendered page / pdftoppm 180 dpi | DOC-002 p. 33 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A038 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p1.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 1 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A039 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p10.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 10 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A040 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p11.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 11 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A041 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p12.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 12 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A042 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p13.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 13 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A043 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p14.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 14 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A044 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p15.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 15 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A045 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p16.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 16 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A046 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p17.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 17 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A047 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p18.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 18 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A048 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p19.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 19 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A049 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p2.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 2 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A050 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p3.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 3 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A051 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p4.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 4 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A052 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p5.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 5 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A053 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p6.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 6 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A054 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p7.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 7 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A055 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p8.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 8 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A056 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp2_prod-p9.png | Rendered page / pdftoppm 180 dpi | DOC-003 p. 9 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A057 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/joi190122supp3_prod-p1.png | Rendered page / pdftoppm 180 dpi | DOC-004 p. 1 | USABLE | Canonical full-page visual locator; no extra unique count beyond text page |
| A058 | .ai_paper_validation/review_1_6_1/preprocessing/numeric-main-p8.png | Rendered page / legacy engine unrecorded | DOC-001 p. 8 | DUPLICATE | Overlapping alternate resolution; canonical matching page already available; no unique page increment |
| A059 | .ai_paper_validation/review_1_6_1/preprocessing/numeric-main-p9.png | Rendered page / legacy engine unrecorded | DOC-001 p. 9 | DUPLICATE | Overlapping alternate resolution; canonical matching page already available; no unique page increment |
| A060 | .ai_paper_validation/review_1_6_1/preprocessing/numeric-supp2-p12.png | Rendered page / legacy engine unrecorded | DOC-003 p. 12 | DUPLICATE | Overlapping alternate resolution; canonical matching page already available; no unique page increment |
| A061 | .ai_paper_validation/review_1_6_1/preprocessing/numeric-supp2-p18.png | Rendered page / legacy engine unrecorded | DOC-003 p. 18 | DUPLICATE | Overlapping alternate resolution; canonical matching page already available; no unique page increment |
| A062 | .ai_paper_validation/review_1_6_1/preprocessing/numeric-supp2-p19.png | Rendered page / legacy engine unrecorded | DOC-003 p. 19 | DUPLICATE | Overlapping alternate resolution; canonical matching page already available; no unique page increment |
| A063 | .ai_paper_validation/review_1_6_1/preprocessing/st2b-supp2-p17.png | Rendered page / legacy engine unrecorded | DOC-003 p. 17 | DUPLICATE | Overlapping alternate resolution; canonical matching page already available; no unique page increment |

Unique coverage and gap assignments:

| Source | Reusable text units | Reusable canonical visual units | Unit-level gaps | Downstream complete mapping assignment |
|---|---|---|---|---|
| DOC-001 | pp. 1-11 | pp. 1-11 | None | Main mapper pp. 1-11, including every figure/table/caption |
| DOC-002 | pp. 1-33 | pp. 11-20 and 31-33 | Images absent pp. 1-10 and 21-30; usable text closes extraction coverage | Support mapper pp. 1-33, including protocol and addendum; exact-source inspection for any image-specific need |
| DOC-003 | pp. 1-19 | pp. 1-19 | Native/layout misses image-display values pp. 17-19; canonical images close extraction coverage | Support mapper pp. 1-19, with explicit image-assisted inspection pp. 17-19 |
| DOC-004 | p. 1 | p. 1 | None | Support mapper p. 1 |

No STALE or UNREADABLE assets were found. Six alternate page images are DUPLICATE; the remaining 57 files are USABLE for their described purpose. A text asset is a transcription locator, not proof of complete scientific mapping or authority over the supplied PDF. There are 64 reusable source units and zero fresh-required units. Scientific mapped units remain zero until the mapper artifacts document complete coverage. Suggested artifact organization is main article alone, then support sections by source with protocol/addendum boundaries kept explicit; context sharding is permitted only to keep complete coverage within the configured context bound.

## New targeted confirmation derivatives

These derivatives were produced after reuse inventory from exact supplied sources. They do not alter the reusable/fresh-required partition because usable extraction already covered their source pages. They are outside the reused-asset hash manifest.

| Artifact path | Engine / device | Exact source scope | Purpose |
|---|---|---|---|
| .ai_paper_validation/review_1_6_2/preprocessing/numeric_checker/supp2-18.png | Poppler pdftoppm 26.01.0 / CPU | DOC-003 PDF p. 18 | Direct-source visual confirmation of eFigure 2 count columns |
| .ai_paper_validation/review_1_6_2/preprocessing/numeric_checker/supp2-19.png | Poppler pdftoppm 26.01.0 / CPU | DOC-003 PDF p. 19 | Direct-source visual confirmation of eFigure 3 count columns |
| .ai_paper_validation/review_1_6_2/preprocessing/statistical_pass_1/plan17-23.txt | Poppler pdftotext -layout 26.01.0 / CPU | DOC-002 PDF pp. 17-23 | Exact plan endpoint, analysis, power and monitoring confirmation |
| .ai_paper_validation/review_1_6_2/preprocessing/statistical_pass_1/plan31-33.txt | Poppler pdftotext -layout 26.01.0 / CPU | DOC-002 PDF pp. 31-33 | Exact amended analysis specification confirmation |
| .ai_paper_validation/review_1_6_2/preprocessing/statistical_pass_1/supp2-4.txt | Poppler pdftotext -layout 26.01.0 / CPU | DOC-003 PDF pp. 2-4 | Exact laboratory-method confirmation |

Numeric command: `pdftoppm -f 18 -l 19 -scale-to 2000 -png joi190122supp2_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/numeric_checker/supp2`. Statistical commands use `pdftotext -layout -f FIRST -l LAST SOURCE OUTPUT` with the exact source windows and output paths above. No OCR, conversion, or fallback was used.

Screening derivative details: `preprocessing/inclusion_initial/derivative_record.md` lists all 36 exact source windows, direct Poppler pdftotext -layout 26.01.0 engines and CPU device. These are new confirmation derivatives outside the reused-asset hash manifest.

Mechanical recheck derivatives: `preprocessing/evidence_recheck/derivative_record.md` records four complete-source text derivatives and three exact-page CPU renders; all seven are new confirmation derivatives outside the reused-asset hash manifest.
