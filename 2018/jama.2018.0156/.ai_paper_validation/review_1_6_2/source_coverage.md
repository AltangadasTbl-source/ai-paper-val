# Complete source coverage ledger

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_jabre_2018_oi_180004.pdf | PDF_PAGE | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-002 | joi180004supp1_prod.pdf | PDF_PAGE | 134 | 134 | 0 | 134 | COMPLETE |
| DOC-003 | joi180004supp2_prod.pdf | PDF_PAGE | 3 | 3 | 0 | 3 | COMPLETE |

Initial inventory state: total 146 unique physical PDF pages; 146 reusable-backed; zero fresh-required derivative units; zero scientifically mapped. The coordinator updates mapped counts and COMPLETE only after durable mapper artifacts cover every unit.

Completed scientific mapping: main_quantitative_evidence.md records DOC-001 pp1–9; support_001.md records DOC-002 pp1–63; support_002.md records DOC-002 pp64–107; support_003.md records DOC-002 pp108–134 and DOC-003 pp1–3. Every unit has an explicit page row, including no-applicable units. The three support parts were merged without content loss into extraction/support_quantitative_evidence.md, adjusting only relative PDF link depth. Total mapped units: 146. Fresh CPU source rendering confirmed embedded IDS displays on pp52 and103; the reusable image already covered p103 despite its layout omission.

DOC-001 pp.1–9 and DOC-003 pp.1–3 have complete current-source-matched native and layout extraction. DOC-002 pp.1–107 and110–125 have substantial layout text; p52 also has supplied OCR and a matching image to supplement incomplete native extraction. Scanned pp108–109 and126–133 have source-hash-matched supplied OCR, matching metadata, and readable page images. DOC-002 p134 has a readable legacy rendered page at .ai_paper_validation/review_1_6_1/preprocessing/support_final/DOC-002-p134.png, showing SAP page9of9 with header/footer and an otherwise blank body; this image is its reusable evidence unit, requiring downstream visual mapping. No page is omitted because it contains little or no numerical content.

Derivative limitation: DOC-002 pp108–109 and126–134 lack native text; p134 has no OCR. Reusable images and supplied OCR cover these units. The unavailable local OCR executable imposes no unassigned scientific unit. Legacy GPU-generated OCR is reused as supplied evidence; this run uses CPU and invokes no GPU.
