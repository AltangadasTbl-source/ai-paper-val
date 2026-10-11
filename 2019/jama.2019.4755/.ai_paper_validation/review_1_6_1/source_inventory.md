# Workflow 1.6.1 Direct Source Inventory

The current paper package contains five direct PDFs and no direct DOC, DOCX, XLS, XLSX, or CSV source. Inventory used package-local file enumeration, Poppler pdfinfo 26.01.0, direct title/heading inspection with pdftotext 26.01.0, and sha256sum. Stable units are physical PDF pages, counted once regardless of overlapping derivatives. Current SHA-256 values match the reusable package manifest. Historical audit scope and historical scientific dispositions in metadata are not discovery inputs.

| Source ID | Source path | Format | Document role | Role basis by content | Exact units | Unit count | SHA-256 |
|---|---|---|---|---|---|---:|---|
| DOC-001 | jama_brenner_2019_oi_190039.pdf | PDF | REPORT | Main original investigation with abstract, methods, results, participant flow, and Tables 1-3 | PDF pages 1-7 | 7 | 799606a7244357dc9942c50cf7782001d00bfbd6fcdc821ccad1aeca67fae328 |
| DOC-002 | joi190039supp1_prod.pdf | PDF | PLAN | Clinical study protocol version 1.5 dated 24 July 2015; prospective trial procedures and statistical approach | PDF pages 1-62 | 62 | 5143f7e4da1ae6c98ec6233a3dee86053082e1fb85e4b5a6b70d2f4e74f4a14b |
| DOC-003 | joi190039supp2_prod.pdf | PDF | PLAN | Statistical Analysis Plan for the ASA enhanced early-detection study | PDF pages 1-10 | 10 | 5704a644014e515ba117d6f77ba50b0f0fe6d9633442bf5c967d77192029ce81 |
| DOC-004 | joi190039supp3_prod.pdf | PDF | REPORT | Non-plan supplement with eligibility criteria and eTables 2-6 reporting sample counts and diagnostic results | PDF pages 1-8 | 8 | b45e07a04d8267f58d72e1809f785a46f932101412f35ef3448689e2638c0e0d |
| DOC-005 | joi190039supp4_prod.pdf | PDF | REPORT | Retrospective availability statement for trial protocol, statistical code, and dataset; contains no prospective analysis specification | PDF page 1 | 1 | ded78f53da7bbb5e05d0afb3070dbccaac6c35cd7a0087309dd23442bfb17f5a |

No supplied source bundles both REPORT and PLAN content. The availability supplement cites an external publication; that publication is not supplied and will not be retrieved. Every supplied page remains within mapping scope, including covers, references, appendices, and availability material; pages without quantitative relationships require an explicit mapped coverage statement.

## Canonical reusable source-page map and downstream assignment

| Source ID | Exact pages | Preferred asset or path rule | Unicode text characters | Downstream mapper assignment |
|---|---|---|---:|---|
| DOC-001 | 1-7, individually | .ai_paper_validation/document_outputs/doc-799606a72443/normalized_pages/page-N.txt where N is the exact PDF page | 66427 | main_quantitative_mapper |
| DOC-002 | 1-62 | .ai_paper_validation/review_1_5_1/preprocessing/support/DOC-002_pp1-62_layout.txt; form-feed segment N is PDF page N | 171004 | support_quantitative_mapper protocol shard |
| DOC-003 | 1-10 | .ai_paper_validation/review_1_5_1/preprocessing/support/DOC-003_pp1-10_layout.txt; form-feed segment N is PDF page N | 28194 | support_quantitative_mapper remaining-support shard |
| DOC-004 | 1-3 | .ai_paper_validation/review_1_5_1/preprocessing/support/DOC-004_pp1-3_layout.txt; form-feed segment N is PDF page N | 5693 | support_quantitative_mapper remaining-support shard |
| DOC-004 | 4-8, individually | .ai_paper_validation/document_outputs/doc-b45e07a04d82/normalized_pages/page-N.txt where N is the exact PDF page | 12219 | support_quantitative_mapper remaining-support shard |
| DOC-005 | 1 | .ai_paper_validation/review_1_5_1/preprocessing/support/DOC-005_p1_layout.txt | 478 | support_quantitative_mapper remaining-support shard |

Main page character counts in page order: 5694, 9410, 8261, 10541, 9095, 11147, 12279. DOC-004 pages 4-8 counts: 4094, 2225, 2180, 1983, 1737. Full support text totals 217588 characters, so a single support shard would exceed the configured 200000-character bound. The recommended disjoint support shards contain protocol pages 1-62 (171004 characters) and all remaining support pages (46584 characters). These bounds govern context, not candidate counts.

## Mapper fitness reassessment

DOC-002 canonical layout is insufficient on physical PDF p.20 (flow-chart font encoding) and p.49 (empty native text on signed approval form). The protocol mapper inspected fresh CPU Poppler renders of both pages. DOC-002 therefore partitions as 60 reusable units and 2 fresh-required units, with no scientific unit omitted. Initial byte equivalence established derivative identity but could not alone establish visual-content fitness on these pages.

Final mapper reassessment additionally covers DOC-002 p.16: background figure axes and cutpoint required direct visual inspection. Final source partition is DOC-002 59 reusable + 3 fresh-required (pp.16,20,49), all 62 mapped; package total 85 reusable + 3 fresh-required = 88 mapped. Retained Poppler CPU derivatives: extraction/parts/DOC-002-p16.png, extraction/parts/DOC-002-p20.png, extraction/parts/DOC-002-p49.png beneath review_1_6_1. Every other source is fully reusable-backed. DOC-004 p.7 source-native and visible-render readings were preserved; reusable full-page image already covers it, so targeted source confirmation adds no fresh-required unit.
