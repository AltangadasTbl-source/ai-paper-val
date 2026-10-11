# Workflow 1.5.1 Run State

- **Package:** `jama.2019.14231`
- **Profile:** `1.5.1`
- **Run status:** COMPLETE
- **Target basis:** Three supplied PDFs contain 39 direct-source pages (12-page main article, 20-page results supplement, and 7-page protocol); reusable native text provisionally covers 27 pages, leaving 12 pages for fresh direct-source mapping. The package is materially smaller and has a lower fresh-extraction burden than the 102-unit/81-fresh calibration package, but still requires complete main/support mapping, two independent statistical passes, cross-lane review, candidate recheck, audit, and report generation.
- **Total source units:** 39
- **Fresh-source units:** 12
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-08-18T22:17:16Z
- **Finished UTC:** 2026-08-18T23:02:13Z
- **Observed elapsed minutes:** 45.0
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Final evidence-quality audit identified two source-grounded omissions requiring stable-ID append, direct-source recheck, and audit closure; full 11-card report assembly.
- **Source inventory status:** COMPLETE
- **Reuse inventory status:** COMPLETE — 59 active artifacts, 27 reusable-backed source units
- **Coverage manifest status:** CREATED_BEFORE_SCIENTIFIC_MAPPING
- **Scientific mapping status:** COMPLETE — 39/39 pages, 38 numeric and 25 statistical relationships
- **Candidate ledger status:** COMPLETE — C001 through C011, 11 stable candidates after audit repair
- **Evidence recheck status:** COMPLETE — C001 through C011 rechecked against direct PDFs
- **Evidence quality status:** COMPLETE — 11/11 stable IDs and all coverage rows audited
- **Report generation status:** COMPLETE — 11/11 candidate cards assembled
- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE — 11 manifested agents have explicit UNAVAILABLE rows; known subtotal 0 tokens and USD 0.000000; complete total unavailable
- **Validation status:** PASS

## Coordinator Notes

- The UTC start was captured before source hashing and scientific review.
- Direct-source page counts use `pdfinfo`; the main article reports 12 pages despite the `file` utility summarizing 10 pages, so the authoritative stable-unit count is 12.
- Legacy candidate, verifier, critic, adjudication, quality, and report outputs are excluded as scientific inputs.
- No web or external literature will be used.
- Final integrity checks reproduced all 3 direct-source hashes and all 59 actively reused-artifact hashes.
- Standalone HTML rendering completed and the Workflow 1.5.1 validator reported PASS.
