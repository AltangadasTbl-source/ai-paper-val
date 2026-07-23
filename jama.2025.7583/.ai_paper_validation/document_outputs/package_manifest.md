# Package manifest

Package root: `C:\Users\juliz\Documents\Document_Agent_Reading\AI_paper_validation_multi_agents_1\jama.2025.7583`  
Inventory date: 2026-07-22  
Source-PDF handling: source PDFs inspected read-only; none modified.

| Document ID | Source filename | SHA-256 | Pages | Native text layer | Likely content type | Scientific audit scope and routing |
|---|---|---|---:|---|---|---|
| DOC-001-MAIN | jama_shotar_2025_oi_250033_1750956987.75881.pdf | 65E9D37FBEF50085482A007406B8E26D470FDB662D3BBD87A7E0C7660E305D6F | 9 | Available on all sampled pages; substantial extractable text | Main article | Audit pp. 1-9. Results and tables are principally pp. 4-7; Figure 1/flow and Table 1 are p. 4, Tables 2-3 pp. 6-7. |
| DOC-002-PROTOCOL | joi250033supp1_prod_1750956987.76581.pdf | AF301D1383975666A95BBC92D6408FC58B1AEAE8F275EAAF3DA832E40BB3A09E | 63 | Available on title, table-of-contents, and sampled end pages | Protocol | Not Audited by Design. Do not preprocess/extract/OCR routinely. Available only for a specific requested protocol-to-report comparison; table of contents is p. 3. |
| DOC-003-ADMIN | joi250033supp3_prod_1750956987.77681.pdf | BE4D36F65E4DFB32B0A2C3B5BFDC5421A13A48C3759E997074636CFDEC40D1A5 | 23 | Available on title, table-of-contents, and sampled end pages | Administrative material | Not Audited by Design. Protocol addenda: investigator/contact lists, reporting forms, CE-mark/data-sheet material, and radiological-classification appendix. Do not preprocess/extract/OCR routinely. |
| DOC-004-RESULTS-SUPP | joi250033supp4_prod_1750956987.77981.pdf | 8697A4E305DAB143E199F7A39CB4011F561D3D3F9439D92077A55608A8839333 | 15 | Available on all pages; substantive extractable text | Results supplement | Audit pp. 1-15, with results-focused priority pp. 8-13 (eFigures 1-2 and eTables 1-3). pp. 2-6 are eMethods supporting analyses/procedures; pp. 14-15 are contextual comparative eTable 4. |
| DOC-005-SAP | joi250033supp5_prod_1750956987.78281.pdf | DD0147546B53B054ED749C9A99D77F8DD8BF5F4DC3464652AC4F7208968CF88B | 9 | Available on title, table of contents, and sampled end pages | Statistical analysis plan | Not Audited by Design. Do not preprocess/extract/OCR routinely. May be opened for a specific parent-requested comparison; contents map is p. 2 and planned analyses pp. 3-9. |

## Classification evidence

- **DOC-001-MAIN:** p. 1 identifies a JAMA randomized clinical trial: Meningeal Embolization for Preventing Chronic Subdural Hematoma Recurrence After Surgery: The EMPROTECT Randomized Clinical Trial. Its main text explicitly directs readers to Supplements 1, 3, 4, and 5.
- **DOC-002-PROTOCOL:** p. 1 says EMPROTECT protocol version 1.1; p. 3 is a table of contents for synopsis, objectives, research design, and related protocol sections.
- **DOC-003-ADMIN:** p. 1 says List of Addenda; p. 2 lists investigator pairs, SAE/incident/pregnancy forms, CE mark/data sheet, and radiological classifications.
- **DOC-004-RESULTS-SUPP:** p. 1 lists eMethods, eFigures 1-2, and eTables 1-4. The result-relevant figures and tables occupy pp. 8-15.
- **DOC-005-SAP:** p. 1 identifies STATISTICAL ANALYSIS PLAN VERSION 2; p. 2 contents list objectives/endpoints, sample-size calculation, analysis populations, primary/secondary analyses, and missing-data management.

## Completeness and routing notes

- Five source PDFs were present in the root and are all represented above. `Supplement 2` is cited by the main article but no corresponding root PDF was supplied; it is not a source document and has no document record.
- Every document requires a separate AI Training Restriction Record before full-text model-mediated processing, including the three documents marked Not Audited by Design.
- Stable IDs are tied to the recorded source filename and SHA-256 fingerprint. Reassign only if the source bytes change.
