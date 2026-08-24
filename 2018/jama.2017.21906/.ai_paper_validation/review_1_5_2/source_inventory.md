# Direct Source Inventory

This is a fresh, source-first inventory. No prior audit text, findings, or extraction was used to classify sources. All paths are package-relative. The direct-source set contains four PDFs and 80 PDF-page units; no DOC, DOCX, XLS, XLSX, or CSV direct source was present.

| Source ID | Source path | Type | Size (bytes) | SHA-256 | Pages | Likely role | Fresh extraction status |
|---|---|---|---:|---|---:|---|---|
| DOC-001 | jama_huffman_2018_oi_170166.pdf | PDF | 545410 | 11311a6bb5c7a4be734ed60776b308f525ad101671ccc8d34bab18735aaca5f5 | 12 | Main randomized clinical-trial article | Native and layout text extracted; result pages rendered |
| DOC-002 | joi170166supp1_prod.pdf | PDF | 1006762 | 0e13bdfc6e5e3c8b86e187f54f0a3d7d0217fc0614be9fbdbbb7839dbab9004a | 32 | Trial protocol | Native and layout text extracted |
| DOC-003 | joi170166supp2_prod.pdf | PDF | 934674 | d49019c3cf6ee0766fb319f254f27f87751a73bfec66c34d38bae16a956bb1c6 | 9 | Statistical analysis plan | Native and layout text extracted; sample-size page rendered |
| DOC-004 | joi170166supp3_prod.pdf | PDF | 912421 | 511f4a907e4c48d920f1c6b89d444fe76c7c91e11bbae84cdee834fa0393f3ec | 27 | Online supplement: toolkit, tables, and figures | Native and layout text extracted; eTables/eFigures rendered; source-matched supplied OCR is fallback only for pp. 3-16 |

## Complete page-unit inventory

`NATIVE+LAYOUT` means fresh direct `pdftotext` and `pdftotext -layout` output is usable for the page's text layer. `SUPPLIED_OCR_FALLBACK` means that both fresh direct outputs contain only the copyright line or otherwise lack the visible page content; the supplied page OCR has the same source filename, SHA-256, and page number. It is not a previous audit finding and does not define discovery.

| Unit | Status / content scope |
|---|---|
| DOC-001 p. 1 | NATIVE+LAYOUT; title, abstract, trial summary |
| DOC-001 p. 2 | NATIVE+LAYOUT; introduction and methods |
| DOC-001 p. 3 | NATIVE+LAYOUT; methods |
| DOC-001 p. 4 | NATIVE+LAYOUT; participant flow and results |
| DOC-001 p. 5 | NATIVE+LAYOUT; Table 1 |
| DOC-001 p. 6 | NATIVE+LAYOUT; Table 2 |
| DOC-001 p. 7 | NATIVE+LAYOUT; Table 3 |
| DOC-001 p. 8 | NATIVE+LAYOUT; Figure 2 and results |
| DOC-001 p. 9 | NATIVE+LAYOUT; Figure 3 and results |
| DOC-001 p. 10 | NATIVE+LAYOUT; results and discussion |
| DOC-001 p. 11 | NATIVE+LAYOUT; discussion and disclosures |
| DOC-001 p. 12 | NATIVE+LAYOUT; references |
| DOC-002 p. 1 | NATIVE+LAYOUT; protocol front matter |
| DOC-002 p. 2 | NATIVE+LAYOUT; protocol front matter |
| DOC-002 p. 3 | NATIVE+LAYOUT; contents |
| DOC-002 p. 4 | NATIVE+LAYOUT; contents |
| DOC-002 p. 5 | NATIVE+LAYOUT; abbreviations |
| DOC-002 p. 6 | NATIVE+LAYOUT; study schema |
| DOC-002 p. 7 | NATIVE+LAYOUT; study synopsis |
| DOC-002 p. 8 | NATIVE+LAYOUT; background/rationale |
| DOC-002 p. 9 | NATIVE+LAYOUT; objectives/outcomes |
| DOC-002 p. 10 | NATIVE+LAYOUT; eligibility |
| DOC-002 p. 11 | NATIVE+LAYOUT; procedures |
| DOC-002 p. 12 | NATIVE+LAYOUT; procedures/data capture |
| DOC-002 p. 13 | NATIVE+LAYOUT; follow-up/data capture |
| DOC-002 p. 14 | NATIVE+LAYOUT; time/events and withdrawal |
| DOC-002 p. 15 | NATIVE+LAYOUT; withdrawal criteria |
| DOC-002 p. 16 | NATIVE+LAYOUT; safety reporting |
| DOC-002 p. 17 | NATIVE+LAYOUT; safety reporting |
| DOC-002 p. 18 | NATIVE+LAYOUT; intervention toolkit |
| DOC-002 p. 19 | NATIVE+LAYOUT; monitoring/interim analysis |
| DOC-002 p. 20 | NATIVE+LAYOUT; consent |
| DOC-002 p. 21 | NATIVE+LAYOUT; audit/data monitoring |
| DOC-002 p. 22 | NATIVE+LAYOUT; protocol deviations |
| DOC-002 p. 23 | NATIVE+LAYOUT; records retention |
| DOC-002 p. 24 | NATIVE+LAYOUT; references |
| DOC-002 p. 25 | NATIVE+LAYOUT; references |
| DOC-002 p. 26 | NATIVE+LAYOUT; consent form |
| DOC-002 p. 27 | NATIVE+LAYOUT; consent form |
| DOC-002 p. 28 | NATIVE+LAYOUT; consent form |
| DOC-002 p. 29 | NATIVE+LAYOUT; consent form |
| DOC-002 p. 30 | NATIVE+LAYOUT; consent signatures |
| DOC-002 p. 31 | NATIVE+LAYOUT; contact appendix |
| DOC-002 p. 32 | NATIVE+LAYOUT; contact appendix |
| DOC-003 p. 1 | NATIVE+LAYOUT; SAP title/front matter |
| DOC-003 p. 2 | NATIVE+LAYOUT; SAP introduction/objectives |
| DOC-003 p. 3 | NATIVE+LAYOUT; outcomes |
| DOC-003 p. 4 | NATIVE+LAYOUT; sample size |
| DOC-003 p. 5 | NATIVE+LAYOUT; outcomes/data |
| DOC-003 p. 6 | NATIVE+LAYOUT; statistical analysis |
| DOC-003 p. 7 | NATIVE+LAYOUT; disposition/subgroups |
| DOC-003 p. 8 | NATIVE+LAYOUT; substudies/safety |
| DOC-003 p. 9 | NATIVE+LAYOUT; DSMB |
| DOC-004 p. 1 | NATIVE+LAYOUT; supplement title and contents |
| DOC-004 p. 2 | NATIVE+LAYOUT; eAppendix title |
| DOC-004 p. 3 | SUPPLIED_OCR_FALLBACK; toolkit visual content |
| DOC-004 p. 4 | SUPPLIED_OCR_FALLBACK; toolkit visual content |
| DOC-004 p. 5 | SUPPLIED_OCR_FALLBACK; toolkit visual content |
| DOC-004 p. 6 | SUPPLIED_OCR_FALLBACK; toolkit visual content |
| DOC-004 p. 7 | SUPPLIED_OCR_FALLBACK; toolkit visual content |
| DOC-004 p. 8 | SUPPLIED_OCR_FALLBACK; toolkit visual content |
| DOC-004 p. 9 | SUPPLIED_OCR_FALLBACK; toolkit visual content |
| DOC-004 p. 10 | SUPPLIED_OCR_FALLBACK; toolkit visual content |
| DOC-004 p. 11 | SUPPLIED_OCR_FALLBACK; toolkit visual content |
| DOC-004 p. 12 | SUPPLIED_OCR_FALLBACK; toolkit visual content |
| DOC-004 p. 13 | SUPPLIED_OCR_FALLBACK; toolkit visual content |
| DOC-004 p. 14 | SUPPLIED_OCR_FALLBACK; toolkit visual content |
| DOC-004 p. 15 | SUPPLIED_OCR_FALLBACK; toolkit visual content |
| DOC-004 p. 16 | SUPPLIED_OCR_FALLBACK; toolkit visual content |
| DOC-004 p. 17 | NATIVE+LAYOUT; eTable 1 |
| DOC-004 p. 18 | NATIVE+LAYOUT; eTable 2 |
| DOC-004 p. 19 | NATIVE+LAYOUT; eTable 3 |
| DOC-004 p. 20 | NATIVE+LAYOUT; eTable 4 |
| DOC-004 p. 21 | NATIVE+LAYOUT; eTable 5 |
| DOC-004 p. 22 | NATIVE+LAYOUT; eTable 6 |
| DOC-004 p. 23 | NATIVE+LAYOUT; eTable 7 |
| DOC-004 p. 24 | NATIVE+LAYOUT; eFigure 1A |
| DOC-004 p. 25 | NATIVE+LAYOUT; eFigure 1B |
| DOC-004 p. 26 | NATIVE+LAYOUT; eFigure 2A |
| DOC-004 p. 27 | NATIVE+LAYOUT; eFigure 2B |

Total inventoried unique units: 80 PDF pages.
