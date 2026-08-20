# AI Paper Validation Workflow 1.2.0 — Fresh Single-Paper Run

The current directory is exactly one new paper package. It contains one main paper and zero or more
support files, normally PDF, DOCX, XLSX, XLS, or CSV. There are no workflow-1.0/1.1 audit records to
recover. If legacy `.ai_paper_validation` markers are detected, stop this profile with a diagnostic
that selects 1.2.1 or 1.2.2; do not ask the user which action to take.

Use English only in generated audit artifacts and reports. Preserve every supplied source unchanged.
Write every derivative only below `.ai_paper_validation/`.

## Fully autonomous execution

Start immediately. “Turbo” means fully autonomous execution: do not ask whether to execute, enable,
confirm, continue, choose a mode, or approve a recoverable workflow choice. Use safe defaults from
`workflow_1_2_0/settings.toml`, perform independent specialist work in parallel, prevent concurrent
writes to one artifact, and finish all work local evidence permits. Record missing tools or evidence
as bounded limitations and continue; never turn a recoverable diagnostic into a user question.

The target is Linux CPU-only. Never run `nvidia-smi`, probe for CUDA, wait for a GPU, or call a GPU OCR
provider. Use native text first and targeted CPU OCR only on pages that need it. If CPU OCR is absent,
record affected pages and continue all unblocked stages.

## Read and initialize

Read completely before examining scientific content:

- `CONTRADICTIONS_RESOLVED.md`
- `workflow_1_2_0/audit_contract.md`
- `workflow_1_2_0/report_spec.md`

Then run:

```bash
python3 workflow_1_2_0/scripts/prepare_package.py --package .
```

The command must report `FRESH_PACKAGE`. It inventories and hashes direct sources, extracts native PDF
text when tools are available, extracts DOCX structure and XLSX cells with CPU-only local code, and
converts Office files to derived PDFs only when a local LibreOffice executable is already present. It
must not install software, use the web, or modify a source.

## Fixed architecture

1. Ask `fresh_package_inventory` to classify every direct source and derived Office PDF, identify the
   main paper and support roles, write package manifests and one record per direct source.
2. Ask `content_use_restriction_checker` to perform the separate package-only rights-language screen.
   It is informational, not legal advice or a substitute for institutional authorization, and it does
   not count toward the candidate queue.
3. Ask `fresh_source_preprocessor` to assess native/Office extraction. Render and CPU-OCR only exact
   pages that need it. Create page/sheet/paragraph source units and the machine-readable coverage plan.
4. Run `fresh_main_evidence_extractor` and `fresh_support_evidence_extractor` in parallel over disjoint
   recorded source units. Extract every result-relevant relationship, not only key/significant ones.
5. Run `fresh_table_arithmetic_checker`, `fresh_figure_flow_checker`, and the first pass of
   `fresh_statistical_consistency_checker` in parallel. There is no discovery count limit.
6. Deduplicate genuine duplicates before stable IDs, retain all source locations and provenance, then
   assign `C001`, `C002`, ... and write the unbounded candidate ledger.
7. Run `fresh_evidence_rechecker` over every stable ID. Record mechanical facts, never an AI
   disposition.
8. Run the mandatory second statistical pass across every statistical relationship, cross-lane
   candidate, denominator, label, and recheck result. Append new IDs without renumbering and recheck
   every new ID.
9. Construct a deterministic human review queue of at most 10. The cap applies only to this queue, not
   discovery, the ledger, rechecking, or coverage.
10. Run `fresh_evidence_quality_auditor` across every ledger ID, coverage unit, link, and queue route.
11. Run `fresh_report_generator` to create `.ai_paper_validation/final_report_1_2_0.md` and standalone
    `.ai_paper_validation/final_report_1_2_0.html`. Include exactly the queue IDs and link to the full
    deferred ledger.
12. Recompute source hashes and run:

```bash
python3 workflow_1_2_0/scripts/validate_fresh.py --package .
```

Repair correctable defects until `.ai_paper_validation/audit_validation_1_2_0.json` reports `PASS`.

## Scientific and human boundaries

- Allowed candidate categories: `Arithmetic inconsistency`, `Cross-document inconsistency`,
  `Statistical reporting inconsistency`, `Participant flow inconsistency`, and
  `Presentation inconsistency`.
- Use only the supplied package. Do not browse the web or use external literature.
- Do not assess misconduct, raw-data validity, clinical appropriateness, novelty, causal truth, or
  general methodological limitations.
- Preserve all distinct candidates in the ledger. Merge only genuine duplicates before stable IDs.
- Do not assign current `Verified`, `Rejected`, `Uncertain`, `Major`, `Minor`, severity, validity,
  acceptance, exclusion, or correction labels.
- Every queued candidate is `Pending Human Adjudication` with blank human fields.
- Cite PDFs by actual filename and exact `#page=N`; cite workbooks by actual filename, worksheet, and
  exact cells; cite DOCX by actual filename and exact paragraph/table identifier or its derived PDF.

## Completion

Completion requires: all direct sources inventoried and hash-stable; all recorded coverage units
completed exactly once per applicable stage; both statistical passes complete for every relationship;
ledger/recheck/quality ID equality; at most 10 queue IDs; queue/report ID equality; working local
evidence links; standalone HTML with a table of contents; and validator status `PASS`.
