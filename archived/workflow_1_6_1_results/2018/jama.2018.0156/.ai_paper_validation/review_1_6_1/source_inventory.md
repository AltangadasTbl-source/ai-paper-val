# Direct Source Inventory

The inventory is restricted to this paper package. A hidden-file-aware, case-insensitive extension scan found three direct PDFs and no DOC, DOCX, XLS, XLSX, or CSV source. The existing audit area contains derivatives only. Source hashes are stored in source_hashes_before.sha256 using package-relative paths. No source or existing derivative was modified. Roles were assigned from source content, not supplement names.

| Source ID | Source path | Format | Document role | Content and stable unit scope | Total units | Native characters | Layout characters |
|---|---|---|---|---|---:|---:|---:|
| DOC-001 | jama_jabre_2018_oi_180004.pdf | PDF | REPORT | Main randomized-trial article; PDF pages 1-9, including abstract, methods, results, tables, figures, discussion, and references | 9 | 53005 | 86656 |
| DOC-002 | joi180004supp1_prod.pdf | PDF | PLAN | Cover contents page 1; original protocol pages 2-56; final protocol pages 57-109; amendments and change summaries pages 110-116; original SAP pages 117-125; scanned prospective documents pages 126-133; page 134 requires direct visual characterization | 134 | 262924 | 321567 |
| DOC-003 | joi180004supp2_prod.pdf | PDF | REPORT | Non-plan results supplement; contents page 1, investigator contribution eTable 1 page 2, post-hoc analyses eTable 2 page 3 | 3 | 2358 | 4346 |

DOC-002 is a bound plan bundle containing multiple protocol versions and SAP/operational documents. No report/plan mixed bundle was identified. Its background or sample forms do not convert it to REPORT. Page 134 has no native text and cannot be classified more narrowly until visual mapping; it remains assigned with the PLAN bundle.

Stable units are physical one-based PDF pages, independent of printed page numbers. Total unique source units: 146. Character counts are Unicode character counts from existing source-matched Poppler text, including whitespace and form-feed boundaries; these conservative upper bounds support the 200000 normalized-character shard limit. DOC-002 must be sharded rather than passed as one whole-text mapper input.

Inventory engines: pdfinfo 25.03.0 for all three page counts and metadata; pdftotext 25.03.0 for direct text comparison; sha256sum for source identity; rg --files --hidden, file, awk, cmp, wc, and shell for file/segment inspection. Direct-source SHA-256 values: DOC-001 114e922542bbb1f8369ca9b5c19be65d93856e16cf4ff295c483439e4e208839; DOC-002 70106d31b08e3a9d7eaac8a0e035bbf8d92a43b51f2483b634d7349b0c5f6913; DOC-003 937e18794fc87074907b1e9ab792f9a35d2f2d895d586dd27e7cbf44d5ed8d46.

Whitespace-normalized Unicode character counts (each whitespace run replaced with one space, physical page boundaries retained as locators): DOC-001 native 52584 / layout 52849; DOC-002 native 261371 / layout 261484; DOC-003 native 2260 / layout 2264. Conservative unnormalized layout shard bounds: DOC-002 pages 1-56 = 139637 characters; DOC-002 pages 57-134 = 181930 characters. The latter plus DOC-003 full layout = 186276 before supplementary OCR; the support mapper must select only necessary OCR and record any additional context split if its combined normalized input approaches 200000 characters.

Completed direct characterization of DOC-002 page134: support-final mapper rendered the source page with CPU Poppler25.03.0 and visually inspected it. It is the final SAP page, dated18.FEB.2015, printed9of9, with header/footer and an empty body. Its document role is PLAN and its quantitative mapping is explicitly no-applicable. This closes the inventory handoff's pending characterization; all146 source pages are now mapped.
