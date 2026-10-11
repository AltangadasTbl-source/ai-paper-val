# Reusable evidence asset inventory

The complete existing audit area contains 128 eligible extraction, image, and extraction-provenance artifacts, all inventoried below and hashed in reused_artifact_hashes_before.sha256. No other legacy files were present in this package inventory. No old scientific conclusions were read. Every asset has one row and an exact source-unit locator. Images and OCR are transcription/locator aids; candidate confirmation uses the supplied direct source.

Fitness: USABLE means sufficient reusable evidence for its named unit or metadata purpose; PARTIAL means text is incomplete for listed pages; DUPLICATE means an alternate extraction or rendered view overlaps canonical coverage. No asset is judged STALE or UNREADABLE. Unique coverage is counted once across overlapping assets, not once per artifact.

Fresh direct pdftotext 25.03.0 stdout and fresh direct pdftotext -layout stdout were byte-compared with all six legacy Poppler native/layout files using cmp -s. All six match the current sources exactly. Current plan source SHA-256 70106d31b08e3a9d7eaac8a0e035bbf8d92a43b51f2483b634d7349b0c5f6913 also matches the supplied OCR manifest and page metadata. Poppler native/layout page separators match 9,134,3 physical pages. PyMuPDF alternate text uses matching form-feed counts; its recorded engine is PyMuPDF 1.28.0 CLI gettext -mode simple/layout. No new PyMuPDF invocation was made.

Supplied OCR provenance: rapidocr_onnxruntime, selected rapidocr-cuda, historical NVIDIA GeForce RTX 5070 Laptop GPU, 11 completed pages (52,108,109,126–133), recorded render scale 2.25. This is pre-existing evidence, not a GPU computation in this run. Legacy two-page OCR files have no independently recorded engine and are secondary locators. Historical rendered-page engine/version is not recorded except the OCR image render scale; indexed filenames map the exact physical PDF pages. p. 134 image was visually inspected and is readable; mapper must still inspect its direct source/unit.

Canonical text coverage: DOC-001 pp. 1–9 and DOC-003 pp. 1–3 complete; DOC-002 native incomplete p. 52,108–109,126–134; DOC-002 layout has substantial p. 52 text but omits scan contents on 108–109,126–134. Canonical native characters: DOC-001 53005, DOC-002 262924, DOC-003 2358. Counts from wc -m; conservative shard byte counts from awk: plan layout pp. 1–63: 168852, pp. 64–107: 128002, pp. 108–134: 40209. Recommended disjoint support shards are DOC-002 pp. 1–63; DOC-002 pp. 64–107; DOC-002 pp. 108–134 plus DOC-003 pp. 1–3. Read selected layout sections first and use native only for targeted transcription. Each shard needs at most 32 visual page opens; all source units receive mapping even without quantities. Target suggestion 45–65 minutes is based on complete reusable coverage, several plan versions, scan/OCR sections, three support shards, and mandatory independent specialist waves, not page count alone.

No table/workbook extraction, Office structure, CSV extraction, separate page manifest, document record, or source-location map was present outside the explicit extraction metadata/provenance listed here. Fresh-required derivative gaps: none after combining current-matched text, OCR and images. Scientific mapping remains pending for all 146 pages.

| Asset ID | Package-relative asset path | Source ID | Exact source units | Kind | Fitness | Engine/provenance and limitation |
|---|---|---|---|---|---|---|
| A001 | .ai_paper_validation/preprocessing/joi180004supp1_prod/gpu_ocr_backend_report.json | DOC-002 | 52,108,109,126–133 | METADATA | USABLE | Legacy OCR manifest/metadata; source SHA-256 matched |
| A002 | .ai_paper_validation/preprocessing/joi180004supp1_prod/images/page_052.png | DOC-002 | 52 | RENDERED_PAGE | USABLE | Supplied OCR input render scale 2.25; hash-matched manifest |
| A003 | .ai_paper_validation/preprocessing/joi180004supp1_prod/images/page_108.png | DOC-002 | 108 | RENDERED_PAGE | USABLE | Supplied OCR input render scale 2.25; hash-matched manifest |
| A004 | .ai_paper_validation/preprocessing/joi180004supp1_prod/images/page_109.png | DOC-002 | 109 | RENDERED_PAGE | USABLE | Supplied OCR input render scale 2.25; hash-matched manifest |
| A005 | .ai_paper_validation/preprocessing/joi180004supp1_prod/images/page_126.png | DOC-002 | 126 | RENDERED_PAGE | USABLE | Supplied OCR input render scale 2.25; hash-matched manifest |
| A006 | .ai_paper_validation/preprocessing/joi180004supp1_prod/images/page_127.png | DOC-002 | 127 | RENDERED_PAGE | USABLE | Supplied OCR input render scale 2.25; hash-matched manifest |
| A007 | .ai_paper_validation/preprocessing/joi180004supp1_prod/images/page_128.png | DOC-002 | 128 | RENDERED_PAGE | USABLE | Supplied OCR input render scale 2.25; hash-matched manifest |
| A008 | .ai_paper_validation/preprocessing/joi180004supp1_prod/images/page_129.png | DOC-002 | 129 | RENDERED_PAGE | USABLE | Supplied OCR input render scale 2.25; hash-matched manifest |
| A009 | .ai_paper_validation/preprocessing/joi180004supp1_prod/images/page_130.png | DOC-002 | 130 | RENDERED_PAGE | USABLE | Supplied OCR input render scale 2.25; hash-matched manifest |
| A010 | .ai_paper_validation/preprocessing/joi180004supp1_prod/images/page_131.png | DOC-002 | 131 | RENDERED_PAGE | USABLE | Supplied OCR input render scale 2.25; hash-matched manifest |
| A011 | .ai_paper_validation/preprocessing/joi180004supp1_prod/images/page_132.png | DOC-002 | 132 | RENDERED_PAGE | USABLE | Supplied OCR input render scale 2.25; hash-matched manifest |
| A012 | .ai_paper_validation/preprocessing/joi180004supp1_prod/images/page_133.png | DOC-002 | 133 | RENDERED_PAGE | USABLE | Supplied OCR input render scale 2.25; hash-matched manifest |
| A013 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_manifest.json | DOC-002 | 52,108,109,126–133 | METADATA | USABLE | Legacy OCR manifest/metadata; source SHA-256 matched |
| A014 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_metadata/page_052.json | DOC-002 | 52 | METADATA | USABLE | Legacy OCR manifest/metadata; source SHA-256 matched |
| A015 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_metadata/page_108.json | DOC-002 | 108 | METADATA | USABLE | Legacy OCR manifest/metadata; source SHA-256 matched |
| A016 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_metadata/page_109.json | DOC-002 | 109 | METADATA | USABLE | Legacy OCR manifest/metadata; source SHA-256 matched |
| A017 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_metadata/page_126.json | DOC-002 | 126 | METADATA | USABLE | Legacy OCR manifest/metadata; source SHA-256 matched |
| A018 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_metadata/page_127.json | DOC-002 | 127 | METADATA | USABLE | Legacy OCR manifest/metadata; source SHA-256 matched |
| A019 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_metadata/page_128.json | DOC-002 | 128 | METADATA | USABLE | Legacy OCR manifest/metadata; source SHA-256 matched |
| A020 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_metadata/page_129.json | DOC-002 | 129 | METADATA | USABLE | Legacy OCR manifest/metadata; source SHA-256 matched |
| A021 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_metadata/page_130.json | DOC-002 | 130 | METADATA | USABLE | Legacy OCR manifest/metadata; source SHA-256 matched |
| A022 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_metadata/page_131.json | DOC-002 | 131 | METADATA | USABLE | Legacy OCR manifest/metadata; source SHA-256 matched |
| A023 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_metadata/page_132.json | DOC-002 | 132 | METADATA | USABLE | Legacy OCR manifest/metadata; source SHA-256 matched |
| A024 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_metadata/page_133.json | DOC-002 | 133 | METADATA | USABLE | Legacy OCR manifest/metadata; source SHA-256 matched |
| A025 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_pages/page_052.txt | DOC-002 | 52 | OCR_TEXT | USABLE | Supplied rapidocr-cuda; source hash matched |
| A026 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_pages/page_108.txt | DOC-002 | 108 | OCR_TEXT | USABLE | Supplied rapidocr-cuda; source hash matched |
| A027 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_pages/page_109.txt | DOC-002 | 109 | OCR_TEXT | USABLE | Supplied rapidocr-cuda; source hash matched |
| A028 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_pages/page_126.txt | DOC-002 | 126 | OCR_TEXT | USABLE | Supplied rapidocr-cuda; source hash matched |
| A029 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_pages/page_127.txt | DOC-002 | 127 | OCR_TEXT | USABLE | Supplied rapidocr-cuda; source hash matched |
| A030 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_pages/page_128.txt | DOC-002 | 128 | OCR_TEXT | USABLE | Supplied rapidocr-cuda; source hash matched |
| A031 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_pages/page_129.txt | DOC-002 | 129 | OCR_TEXT | USABLE | Supplied rapidocr-cuda; source hash matched |
| A032 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_pages/page_130.txt | DOC-002 | 130 | OCR_TEXT | USABLE | Supplied rapidocr-cuda; source hash matched |
| A033 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_pages/page_131.txt | DOC-002 | 131 | OCR_TEXT | USABLE | Supplied rapidocr-cuda; source hash matched |
| A034 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_pages/page_132.txt | DOC-002 | 132 | OCR_TEXT | USABLE | Supplied rapidocr-cuda; source hash matched |
| A035 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_pages/page_133.txt | DOC-002 | 133 | OCR_TEXT | USABLE | Supplied rapidocr-cuda; source hash matched |
| A036 | .ai_paper_validation/preprocessing/joi180004supp1_prod/ocr_scope.json | DOC-002 | 52,108,109,126–133 | METADATA | USABLE | Legacy OCR manifest/metadata; source SHA-256 matched |
| A037 | .ai_paper_validation/review_1_5_2/preprocessing/layout_text/jama_jabre_2018_oi_180004.txt | DOC-001 | 1–9 | LAYOUT_TEXT | USABLE | Poppler pdftotext -layout; current-source byte match |
| A038 | .ai_paper_validation/review_1_5_2/preprocessing/layout_text/joi180004supp1_prod.txt | DOC-002 | 1–134 | LAYOUT_TEXT | PARTIAL | Poppler pdftotext -layout; current-source byte match |
| A039 | .ai_paper_validation/review_1_5_2/preprocessing/layout_text/joi180004supp2_prod.txt | DOC-003 | 1–3 | LAYOUT_TEXT | USABLE | Poppler pdftotext -layout; current-source byte match |
| A040 | .ai_paper_validation/review_1_5_2/preprocessing/native_text/jama_jabre_2018_oi_180004.txt | DOC-001 | 1–9 | NATIVE_TEXT | USABLE | Poppler pdftotext; current-source byte match |
| A041 | .ai_paper_validation/review_1_5_2/preprocessing/native_text/joi180004supp1_prod.txt | DOC-002 | 1–134 | NATIVE_TEXT | PARTIAL | Poppler pdftotext; current-source byte match |
| A042 | .ai_paper_validation/review_1_5_2/preprocessing/native_text/joi180004supp2_prod.txt | DOC-003 | 1–3 | NATIVE_TEXT | USABLE | Poppler pdftotext; current-source byte match |
| A043 | .ai_paper_validation/review_1_5_2/preprocessing/ocr_text/DOC-002-p052.txt | DOC-002 | 52 | OCR_TEXT | DUPLICATE | Legacy engine unrecorded; secondary locator |
| A044 | .ai_paper_validation/review_1_5_2/preprocessing/ocr_text/DOC-002-p103.txt | DOC-002 | 103 | OCR_TEXT | DUPLICATE | Legacy engine unrecorded; secondary locator |
| A045 | .ai_paper_validation/review_1_5_2/preprocessing/pymupdf_extraction_log.md | DOC-001,DOC-002,DOC-003 | DOC-001 pp. 1–9;DOC-002 pp. 1–134;DOC-003 pp. 1–3 | METADATA | USABLE | PyMuPDF 1.28.0 recorded extraction commands/page delimiter counts |
| A046 | .ai_paper_validation/review_1_5_2/preprocessing/pymupdf_layout_text/DOC-001_jama_jabre_2018_oi_180004.txt | DOC-001 | 1–9 | ALTERNATE_TEXT | DUPLICATE | PyMuPDF 1.28.0 gettext simple/layout; canonical text takes precedence |
| A047 | .ai_paper_validation/review_1_5_2/preprocessing/pymupdf_layout_text/DOC-002_joi180004supp1_prod.txt | DOC-002 | 1–134 | ALTERNATE_TEXT | PARTIAL | PyMuPDF 1.28.0 gettext simple/layout; canonical text takes precedence |
| A048 | .ai_paper_validation/review_1_5_2/preprocessing/pymupdf_layout_text/DOC-003_joi180004supp2_prod.txt | DOC-003 | 1–3 | ALTERNATE_TEXT | DUPLICATE | PyMuPDF 1.28.0 gettext simple/layout; canonical text takes precedence |
| A049 | .ai_paper_validation/review_1_5_2/preprocessing/pymupdf_simple_text/DOC-001_jama_jabre_2018_oi_180004.txt | DOC-001 | 1–9 | ALTERNATE_TEXT | DUPLICATE | PyMuPDF 1.28.0 gettext simple/layout; canonical text takes precedence |
| A050 | .ai_paper_validation/review_1_5_2/preprocessing/pymupdf_simple_text/DOC-002_joi180004supp1_prod.txt | DOC-002 | 1–134 | ALTERNATE_TEXT | PARTIAL | PyMuPDF 1.28.0 gettext simple/layout; canonical text takes precedence |
| A051 | .ai_paper_validation/review_1_5_2/preprocessing/pymupdf_simple_text/DOC-003_joi180004supp2_prod.txt | DOC-003 | 1–3 | ALTERNATE_TEXT | DUPLICATE | PyMuPDF 1.28.0 gettext simple/layout; canonical text takes precedence |
| A052 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p001.png | DOC-001 | 1 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A053 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p004.png | DOC-001 | 4 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A054 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p005.png | DOC-001 | 5 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A055 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p006.png | DOC-001 | 6 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A056 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-001-p008.png | DOC-001 | 8 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A057 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p009.png | DOC-002 | 9 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A058 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p010.png | DOC-002 | 10 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A059 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p011.png | DOC-002 | 11 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A060 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p015.png | DOC-002 | 15 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A061 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p016.png | DOC-002 | 16 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A062 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p017.png | DOC-002 | 17 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A063 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p021.png | DOC-002 | 21 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A064 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p022.png | DOC-002 | 22 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A065 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p024.png | DOC-002 | 24 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A066 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p036.png | DOC-002 | 36 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A067 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p037.png | DOC-002 | 37 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A068 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p050.png | DOC-002 | 50 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A069 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p051.png | DOC-002 | 51 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A070 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p052.png | DOC-002 | 52 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A071 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p053.png | DOC-002 | 53 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A072 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p054.png | DOC-002 | 54 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A073 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p064.png | DOC-002 | 64 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A074 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p065.png | DOC-002 | 65 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A075 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p066.png | DOC-002 | 66 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A076 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p070.png | DOC-002 | 70 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A077 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p071.png | DOC-002 | 71 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A078 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p072.png | DOC-002 | 72 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A079 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p076.png | DOC-002 | 76 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A080 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p077.png | DOC-002 | 77 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A081 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p079.png | DOC-002 | 79 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A082 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p091.png | DOC-002 | 91 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A083 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p092.png | DOC-002 | 92 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A084 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p101.png | DOC-002 | 101 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A085 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p102.png | DOC-002 | 102 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A086 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p103.png | DOC-002 | 103 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A087 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p104.png | DOC-002 | 104 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A088 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p105.png | DOC-002 | 105 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A089 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p110.png | DOC-002 | 110 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A090 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p111.png | DOC-002 | 111 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A091 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p112.png | DOC-002 | 112 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A092 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p114.png | DOC-002 | 114 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A093 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p115.png | DOC-002 | 115 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A094 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p116.png | DOC-002 | 116 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A095 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p117.png | DOC-002 | 117 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A096 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p119.png | DOC-002 | 119 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A097 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p120.png | DOC-002 | 120 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A098 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p121.png | DOC-002 | 121 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A099 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p122.png | DOC-002 | 122 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A100 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p123.png | DOC-002 | 123 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A101 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-002-p124.png | DOC-002 | 124 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A102 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p002.png | DOC-003 | 2 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A103 | .ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/DOC-003-p003.png | DOC-003 | 3 | RENDERED_PAGE | USABLE | Legacy indexed rendering; engine unrecorded |
| A104 | .ai_paper_validation/review_1_5_2/preprocessing/reused_ocr/DOC-002_authorized_ocr_provenance.md | DOC-002 | 52,108,109,126–133 | METADATA | USABLE | Supplied OCR source hash and location provenance index |
| A105 | .ai_paper_validation/review_1_6_1/preprocessing/recheck_initial/main-p2.png | DOC-001 | 2 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A106 | .ai_paper_validation/review_1_6_1/preprocessing/recheck_initial/main-p5.png | DOC-001 | 5 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A107 | .ai_paper_validation/review_1_6_1/preprocessing/recheck_initial/main-p7.png | DOC-001 | 7 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A108 | .ai_paper_validation/review_1_6_1/preprocessing/recheck_initial/main-p8.png | DOC-001 | 8 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A109 | .ai_paper_validation/review_1_6_1/preprocessing/recheck_initial/main-p9.png | DOC-001 | 9 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A110 | .ai_paper_validation/review_1_6_1/preprocessing/recheck_initial/results-p1.png | DOC-003 | 1 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A111 | .ai_paper_validation/review_1_6_1/preprocessing/recheck_initial/results-p2.png | DOC-003 | 2 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A112 | .ai_paper_validation/review_1_6_1/preprocessing/screen_initial/main-layout.txt | DOC-001 | 1–9 | LAYOUT_TEXT | DUPLICATE | Legacy Poppler layout; complete alternate text |
| A113 | .ai_paper_validation/review_1_6_1/preprocessing/screen_initial/main-p1.png | DOC-001 | 1 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A114 | .ai_paper_validation/review_1_6_1/preprocessing/screen_initial/main-p3.png | DOC-001 | 3 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A115 | .ai_paper_validation/review_1_6_1/preprocessing/screen_initial/main-p4.png | DOC-001 | 4 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A116 | .ai_paper_validation/review_1_6_1/preprocessing/screen_initial/main-p6.png | DOC-001 | 6 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A117 | .ai_paper_validation/review_1_6_1/preprocessing/screen_initial/plan-p110.png | DOC-002 | 110 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A118 | .ai_paper_validation/review_1_6_1/preprocessing/screen_initial/plan-p121.png | DOC-002 | 121 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A119 | .ai_paper_validation/review_1_6_1/preprocessing/screen_initial/plan-p122.png | DOC-002 | 122 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A120 | .ai_paper_validation/review_1_6_1/preprocessing/screen_initial/plan-p124.png | DOC-002 | 124 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A121 | .ai_paper_validation/review_1_6_1/preprocessing/screen_initial/plan-p130.png | DOC-002 | 130 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A122 | .ai_paper_validation/review_1_6_1/preprocessing/screen_initial/plan-p131.png | DOC-002 | 131 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A123 | .ai_paper_validation/review_1_6_1/preprocessing/screen_initial/plan-p133.png | DOC-002 | 133 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A124 | .ai_paper_validation/review_1_6_1/preprocessing/screen_initial/plan-p15.png | DOC-002 | 15 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A125 | .ai_paper_validation/review_1_6_1/preprocessing/screen_initial/plan-p71.png | DOC-002 | 71 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A126 | .ai_paper_validation/review_1_6_1/preprocessing/screen_initial/results-layout.txt | DOC-003 | 1–3 | LAYOUT_TEXT | DUPLICATE | Legacy Poppler layout; complete alternate text |
| A127 | .ai_paper_validation/review_1_6_1/preprocessing/screen_initial/results-p3.png | DOC-003 | 3 | RENDERED_PAGE | DUPLICATE | Legacy indexed rendering; engine unrecorded |
| A128 | .ai_paper_validation/review_1_6_1/preprocessing/support_final/DOC-002-p134.png | DOC-002 | 134 | RENDERED_PAGE | USABLE | Legacy indexed rendering; visual fitness confirmed |

Physical PDF p. 52 corresponds to printed original-protocol p51, section17.4, Intubation Difficulty Scale Score: embedded scoring table, calculation rules and illustrations. Native text alone does not transcribe this display; use the supplied source-hash-matched OCR and image. Visual fitness was checked for p. 52 and p. 134 only at curation; downstream mappers own complete scientific mapping.

Recorded current inventory engines/commands: Poppler pdfinfo 25.03.0 for complete page counts; Poppler pdftotext 25.03.0 and pdftotext -layout with stdout compared using cmp -s for source freshness; GNU sha256sum for all direct and reused-artifact hashes; file for image structure; wc -m for character counts; awk with form-feed record separator for exact page segmentation. No derivative was created outside the five assigned inventory/hash artifacts. Legacy executable absolute paths in extraction logs describe historical provenance only and were not invoked.
