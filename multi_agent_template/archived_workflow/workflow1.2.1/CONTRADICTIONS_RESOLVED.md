# Workflow 1.0/1.1 contradictions resolved in the 1.2.x family

This document is normative. When an older instruction conflicts with a resolution below, the 1.2.x
resolution controls.

| ID | Earlier contradiction or enforcement gap | 1.2.x resolution |
|---|---|---|
| R01 | 1.0 requires `Rejected/Uncertain` labels, sends only “verified” findings to the critic, lets the critic retain `Uncertain`, then sends only “accepted” findings to the report. A printed discrepancy can disappear because its explanation is uncertain. | Separate raw records, an unbounded candidate ledger, mechanical recheck facts, and a human queue. No AI disposition controls visibility. |
| R02 | 1.0 applies the top-10 limit before verification even though each checker may return up to 10, conflating evidence retention with review workload. | Discovery, lineage, ledger, and recheck have no count limit. Only the final human review queue is capped at 10. Deferred records remain durable. |
| R03 | 1.0 critic receives only verified findings but is also told to label retained findings `Uncertain`; its “remove unsupported” role conflicts with preserving unresolved questions. | No critic adjudication stage. Mechanical recheck and evidence-quality audit return every stable ID. Missing definitions become explicit human questions. |
| R04 | The 1.0 endetail prompt independently reclassifies C01-C10 but forbids new findings outside the approved set, so it cannot restore checker records lost before stable selection. It also assumes all C01-C10 exist. | 1.2.2 harvests every endetail card and then scans all legacy candidate-bearing artifacts; recovered records without IDs receive deterministic R IDs. Counts are discovered, never assumed. |
| R05 | The endetail pass overwrites `final_report.md/html`, destroying an easy comparison point. | 1.2.1/1.2.2 never overwrite legacy reports; they create versioned reports and hash-check all legacy artifacts. |
| R06 | 1.0 relies on coordinator chat handoffs and read-only agents while requiring every response to be retained; persistence is not mechanically enforced. | Specialists write complete results to unique durable paths; validators check required artifacts and ID preservation. |
| R07 | 1.1 says XLSX is manual-review evidence, but inventory ignores it, the audit protocol requires workbook-like evidence to become PDF, reports require every citation to be a PDF page, the result schema requires `pdf_page_links`, and no XLSX conversion/extraction path is supplied. | Inventory includes XLS/XLSX/CSV. XLSX cells/formulas are extracted locally. Reports may cite actual workbook + worksheet + exact cells; PDF page links are required only for PDF evidence. |
| R08 | 1.1 claims source hashes are recomputed and source modification fails validation, but `validate_audit.py` does not compare run hashes to current sources. | Preparation records SHA-256 and size for every direct source; final validators recompute both and fail on any change. Recovery validators also hash-check every legacy artifact. |
| R09 | 1.1 claims complete, disjoint, exactly-once shard coverage and two complete statistical passes, but its validator checks only that stage names and nonempty artifact paths exist. | `coverage_manifest.json` records explicit expected/completed unit IDs. Validation checks equality, uniqueness, artifact existence, candidate-stage IDs, and both pass statuses for every statistical relationship. |
| R10 | 1.1 preserves every candidate directly in the final report, making human review unbounded even when the operational reason for a 10-item limit is valid. | Preserve every candidate in the ledger, but deterministically prioritize no more than 10 evidence cards for the human-facing report. |
| R11 | 1.1 permanently freezes stable duplicate IDs even when later quality review finds a duplicate relationship, forcing duplicate human review. | Deduplicate genuine duplicates before ID freeze. Later possible duplicates retain lineage/IDs but only one can enter the active queue; the routing link is explicit and non-adjudicative. |
| R12 | 1.1 default GPU OCR and WSL-specific runtime paths can block or slow packages on the target Linux CPU-only machine. | All 1.2.x profiles are Linux CPU-only, reuse native/legacy text first, perform targeted CPU OCR only, never probe GPU, and record unavailable pages without changing backend. |
| R13 | 1.1 promises mandatory HTML, but rendering hard-fails when Pandoc is missing. | Use Pandoc when installed and a dependency-free local HTML5 renderer otherwise; both outputs require TOC, embedded CSS, UTF-8, and valid local links. |
| R14 | 1.1 accepts DOC/DOCX in discovery but exact page citations depend on successful Office-to-PDF conversion; missing LibreOffice can make the whole workflow fail even when DOCX structure is readable. | Prefer derived PDF when LibreOffice exists; otherwise extract DOCX paragraphs/tables locally and cite the actual DOCX plus stable paragraph/table identifiers. Record old binary DOC as a bounded limitation if it cannot be converted. |
| R15 | 1.0 has an AI-training-restriction screen; 1.1 silently drops it. The 1.0 wording can also be read as though the model-mediated screen itself grants processing permission. | Restore a separate package-only rights-language record for every source. It is informational, not a legal opinion, not a finding, not part of the queue, and never treated as authorization; actual authority remains institutional/user-side. |
| R16 | Statistical P-value/CI checks can overclaim when test, sidedness, variance estimator, degrees of freedom, multiplicity, or estimand mapping is absent. | Mechanically separate printed relationships from model-dependent diagnostics. Missing definitions become named human questions; diagnostic approximations are labelled and never replace the reported model. |
| R17 | 1.1 batch/process/WSL orchestration adds failure modes unrelated to a single-paper scientific audit and provides no legacy reuse route. | The 1.2.x family is copied into one paper package and run in a fresh per-paper Codex session. No batch launcher, WSL bridge, sibling discovery, or session reuse is required. |
| R18 | `NEEDS_HUMAN_INPUT` can be treated as worker completion while every report is already pending human adjudication, conflating a normal review boundary with an execution blocker. | Machine execution status is `PASS/FAIL`; `Pending Human Adjudication` is a separate report state. Missing evidence appears as a bounded limitation, not a worker-status ambiguity. |

## Shared invariants

- Source files are immutable and hash-checked.
- Local package evidence only; no web or external literature.
- Durable artifacts contain complete specialist work; chat summaries are not evidence.
- All result-relevant source units are covered or explicitly marked with a reason.
- Candidate identity, mechanical evidence state, queue routing, and human adjudication are separate.
- The ledger is unbounded; the review queue is at most 10.
- Every queued item is `Pending Human Adjudication` with blank human decision fields.
- CPU-only means no GPU probing or fallback.
- PDF, DOCX, and spreadsheet sources each have a truthful citation scheme.
