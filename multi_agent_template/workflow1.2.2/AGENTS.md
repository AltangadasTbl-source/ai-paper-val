# Legacy AI Paper Validation Patch 1.2.2

This project root is exactly one paper package previously processed by workflow 1.0 **and then** by
`final_report_endetail_prompt.md`. This is an endetail-aware recovery run, not a fresh exhaustive audit.

Use English only in generated audit artifacts and reports. Preserve every supplied source file and
every existing file below `.ai_paper_validation/`. Write new work only to:

- `.ai_paper_validation/patch_1_2_2/`
- `.ai_paper_validation/final_report_1_2_2.md`
- `.ai_paper_validation/final_report_1_2_2.html`

## Immediate execution / turbo authorization

Start the patch immediately. “Turbo” means fully autonomous execution: do not ask whether to execute,
enable, confirm, continue, choose a mode, or approve a recoverable implementation choice. Use safe
defaults from `legacy_patch/settings.toml`, make reversible decisions, and complete every part that
local evidence permits. Use parallel specialist agents for independent work, while preventing
concurrent writes to the same artifact. If the preflight profile is wrong, the legacy directory is
absent, a source is missing, or a tool is unavailable, write an actionable diagnostic and finish all
unblocked work; do not turn the diagnostic into a question for the user.

## Required preflight

Run this before reading paper contents:

```bash
python3 legacy_patch/scripts/prepare_recovery.py --profile 1.2.2 --package .
```

The script must report `ENDDETAIL_DETECTED`. If it reports `NOT_DETAILED`, record that workflow 1.2.1 is
required and stop this profile without asking the user. Never bypass the profile check.

Read completely:

- `CONTRADICTIONS_RESOLVED.md`
- `legacy_patch/recovery_contract.md`
- `legacy_patch/report_spec.md`
- `.ai_paper_validation/patch_1_2_2/legacy_inventory.md`

## Recovery objective

Reuse the workflow-1.0 evidence base. Do not discard or regenerate usable normalized text, OCR text,
rendered pages, manifests, document records, extraction maps, checker outputs, candidate sets,
verification records, critic records, or the original final report.

Treat the endetail report as a high-value derived record: harvest its source links, reproduced
calculations, alternative interpretations, missing inferential definitions, revision explanations,
and every candidate appearing in Verified, Uncertain, or Rejected sections. It is not original source
evidence and its dispositions are not authoritative. Confirm harvested facts against exact package
sources, but do not redo a derivation that is already complete and source-matched.

The old workflow's contradiction must be repaired explicitly:

1. It required unsupported findings to be labelled `Rejected` or `Uncertain`.
2. It routed only “verified” or “accepted” findings downstream.
3. Its final report could therefore hide a real printed discrepancy merely because its explanation,
   inferential definition, or production mechanism was uncertain.
4. Its top-10 rule also conflated evidence retention with the size of the human review queue.

Patch 1.2.2 separates these concepts. Preserve all distinct legacy candidate records in a recovery
ledger without a numerical limit. Select at most 10 for the human-facing review queue. Prior
`Verified`, `Rejected`, `Uncertain`, `Major`, `Minor`, accepted, or excluded labels are historical
provenance only and must never operate as current decisions.

## Required workflow

1. Use `endetail_record_harvester` to inspect the endetail report and every candidate-bearing artifact
   listed by the preflight inventory. It writes the endetail harvest, complete source coverage,
   lineage, and an unbounded recovered ledger.
2. In parallel after the ledger exists, use `legacy_evidence_rechecker` and
   `legacy_statistical_reconciler`. Each writes only its assigned canonical artifact.
3. Reuse existing text/OCR/page images first. Reopen the exact original PDF pages for confirmation.
   Create only targeted new extraction or OCR when a cited page cannot otherwise be checked; never
   restart preprocessing for the whole package. The target Linux system is CPU-only: never probe for,
   wait for, or invoke a GPU. If targeted CPU OCR is unavailable, record the page limitation and
   continue autonomously. For DOCX/XLSX/CSV locations, or an optional LibreOffice-derived PDF, run
   `legacy_patch/scripts/extract_office_source.py SOURCE OUTPUT_DIR` with `OUTPUT_DIR` under
   `patch_1_2_2/targeted_preprocessing/`; a missing LibreOffice binary is non-fatal.
4. Deduplicate only genuine duplicates before the review queue is frozen. Preserve every raw-record
   lineage entry even when several entries map to one candidate.
5. Build `.ai_paper_validation/patch_1_2_2/review_queue.md` with no more than 10 candidates, following
   the deterministic prioritization in `recovery_contract.md`. An old `Uncertain` label is neither a
   penalty nor an exclusion reason.
6. Use `legacy_recovery_quality_auditor` to check all recovered ledger entries and the queue. Repair
   missing evidence fields where local sources permit; never erase a lineage entry.
7. Use `legacy_patch_report_generator` to write the versioned Markdown and standalone HTML report.
8. Recompute source hashes and run:

```bash
python3 legacy_patch/scripts/validate_patch.py --profile 1.2.2 --package .
```

Repair correctable failures until `patch_validation.json` reports `PASS`.

## Fixed boundaries

- Audit only inconsistencies demonstrable from the supplied package.
- Allowed categories remain: `Arithmetic inconsistency`, `Cross-document inconsistency`,
  `Statistical reporting inconsistency`, `Participant flow inconsistency`, and
  `Presentation inconsistency`.
- Do not assess misconduct, raw-data validity, clinical appropriateness, novelty, or general
  methodological quality.
- Do not browse the web or use external literature.
- Treat the Linux runtime as CPU-only. Do not run `nvidia-smi` or use CUDA/GPU OCR.
- Do not modify or overwrite `.ai_paper_validation/final_report.md` or its existing HTML.
- Do not rerun the original workflow and do not perform a new page-by-page discovery audit.
- Do not rewrite the endetail report in place or trust its AI dispositions as source evidence.
- Every report candidate is `Pending Human Adjudication`; leave validity, severity, correction, and
  acceptance decisions blank for the human reviewer.
- The queue cap is 10. The recovery ledger and lineage map have no count limit.

## Completion

Do not finish until the versioned Markdown and HTML exist, every candidate-bearing legacy artifact is
accounted for in `legacy_source_coverage.md`, queue/report IDs agree, source hashes are unchanged, and
`.ai_paper_validation/patch_1_2_2/patch_validation.json` reports `PASS`.
