# Workflow 1.6.2 Source Coverage

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_cinciripini_2024_oi_240036_1716416465.98349.pdf | PDF_PAGE | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-002 | joi240036supp1_prod_1716416466.00349.pdf | PDF_PAGE | 45 | 45 | 0 | 45 | COMPLETE |
| DOC-003 | joi240036supp2_prod_1716416466.01349.pdf | PDF_PAGE | 36 | 36 | 0 | 36 | COMPLETE |

Unique total units: 91. Unique reusable units: 91. Fresh-required units: 0. Mapped units: 91. These counts refer to source pages, not derivative counts. Reusable plus fresh-required partitions the total. Durable full-source maps now cover every physical page of all three sources.

Usable primary text coverage is DOC-001 pp. 1-10 in review_1_5_3/preprocessing/main/page-NNN.txt; DOC-002 pp. 1-45 in review_1_5_3/preprocessing/support_doc002/layout_pN.txt; DOC-003 pp. 1-36 in review_1_5_3/preprocessing/support_doc003/layout_pN.txt, all below .ai_paper_validation/. Each file was mechanically matched against its exact current direct PDF page. Older DOC-003 preprocessing covers pp. 4-35, but the later reusable text closes pp. 1-3 and 36. The older absent DOC-002 preprocessing does not leave a gap because later native and layout extraction covers every page.

Assignments: main_quantitative_mapper maps DOC-001 pp. 1-10; support_quantitative_mapper maps DOC-002 pp. 1-45 and DOC-003 pp. 1-36. All page ranges include non-result pages with a documented content assessment. No unit requires fresh extraction due to an absent, stale, partial, or unreadable text asset.

Derivative limitations: existing rendered pages are supplemental locators and require direct-source confirmation when a graphic matters, because current main/supplement hashes differ from older identity records and render-engine provenance is incomplete. DOC-001 existing images cover pp. 3,5,6,7; DOC-002 pp. 10,16,17,28-34; DOC-003 pp. 14-35. Images for other pages are absent, but each has usable source-matched text. Mappers must inspect direct source as needed for graphic content, including targeted rendering where a page contains material not represented in text. This is mandatory direct visual confirmation, not an uncounted scientific omission. Stale metadata and overlapping derivatives do not make a source unit fresh-required when that unit has independently source-matched usable text.

Context-bounded support assignment suggestion: protocol shard DOC-002 pp. 1-45 (146,176 whitespace-collapsed characters) and results-supplement shard DOC-003 pp. 1-36 (68,968 characters). Their union exceeds 200,000 characters, so they should remain disjoint bounded shards, with separate durable parts merged without loss. No page is excluded by this division.
