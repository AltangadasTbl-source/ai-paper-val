---
name: ai-validation
description: Coordinate or perform local research-paper validation for document-grounded arithmetic, statistical-reporting, participant-flow, cross-document, and presentation inconsistencies. Use at a collection Git root to route requested child paper packages into isolated Codex workers, or inside exactly one paper package to produce an exhaustive candidate ledger plus a detailed source-linked HTML report for human adjudication.
---

# Coordinate or Audit Paper Packages

## Route by working directory

If the current directory is the collection Git root containing `ai-validation.toml`, follow the
collection-coordinator rules in `AGENTS.md`. Discover package names only and invoke the thin launcher
for the requested direct child packages. Do not read scientific references or paper contents in the
collection context.

Continue below only when the current directory is exactly one paper package, including an isolated
worker launched by the collection coordinator.

Treat the current directory as the complete paper package. Read parent management files only to load
the shared configuration, agent definitions, and this skill. Never inspect sibling paper packages,
the web, or external literature. Preserve sources and write derived files only below `./audit/`.

Read these references completely before auditing the package:

- [audit protocol](references/audit-protocol.md)
- [statistical checks](references/statistical-checks.md)
- [report specification](references/report-spec.md)

## Fixed boundaries

- Preserve every distinct candidate without a top-N limit.
- Leave validity, importance, severity, acceptance, rejection, and uncertainty judgments to humans.
- Merge genuine duplicates only before stable candidate IDs are assigned. Never suppress or merge a
  stable ID during verification, quality review, or reporting.
- Give statistical checking equal or greater coverage than every other lane. Complete both passes.
- Restrict findings to inconsistencies demonstrable from supplied files.
- Cite actual PDF filenames and exact pages with relative links ending in `#page=N`.
- Use English for all generated content.

## Protect the package context

The outer worker already owns one fresh full Codex context for this package. Do not spend that context
on large specialist transcripts. Read `[context]` from the root configuration and use artifact-first
handoffs:

1. Create `audit/context_coverage.md` before extraction using the required table in the report
   specification. List every required stage and either its complete scope or its disjoint shard scopes.
2. Shard a stage when it exceeds the configured normalized-text, rendered-page, or candidate count.
   Split on page/section boundaries for extraction, on table/figure/statistical-relationship groups for
   checking, and on stable candidate-ID ranges for verification, quality review, and report cards.
3. Give every specialist one scope and one unique output path below `audit/`. A specialist writes its
   complete result there and returns no more than `specialist_return_max_lines` containing status,
   scope, counts, unresolved items, and artifact paths.
4. Run additional waves until every eligible source location, statistical relationship, and stable
   candidate ID is covered. Sharding limits one call only; it never limits total pages or candidates.
5. Merge part files into the canonical artifacts without discarding content, mark coverage complete,
   and only then proceed to the dependent stage. On context compaction, reload the canonical artifacts
   and `audit/context_coverage.md`.

Never let two agents write the same part or canonical file concurrently. Specialists may write only to
their assigned paths below `audit/`; source files remain read-only.

## Initialize the worker

1. Resolve the Git root and read `<root>/ai-validation.toml`.
2. Honor an explicit `runtime.platform`; when it is `auto`, detect WSL/Linux versus native Windows.
   Use `runtime.wsl_python` and Bash on WSL/Linux; use `runtime.windows_python` and PowerShell on
   Windows. Do not silently replace the configured Python.
3. Create `audit/run_metadata.json` with the detected environment, configuration path, model tiers,
   start time, and SHA-256 for every direct source file.
4. If direct DOC/DOCX files exist, run `scripts/convert_office_to_pdf.py` with the configured Python,
   current package path, and root configuration. Audit those supplements only through the derived PDFs.

## Run the audit

1. Ask `package_inventory` to inventory direct sources and converted PDFs, assign stable document IDs,
   and create the package manifest and document records.
2. Ask `pdf_preprocessor` to extract native text first and render only needed pages. If a page truly
   requires OCR, run `scripts/run_ocr.py` with the configured Python, root configuration, and package
   path. The exact configured backend must validate; implicit fallback is forbidden.
3. Plan and record complete stage coverage in `audit/context_coverage.md`; use disjoint shards and
   additional waves wherever the configured context thresholds require them.
4. Run `main_text_extractor` and `results_supplement_extractor` in parallel, or in parallel shard waves.
5. Run `table_arithmetic_checker`, `figure_flow_checker`, and the first
   `statistical_consistency_checker` pass in parallel.
6. Deduplicate genuine duplicates, retain every source location, assign stable IDs `C001`, `C002`, and
   so on, and write `audit/candidate_registry.md`.
7. Run `evidence_verifier` over every candidate, in candidate-ID shards when needed. Record mechanical
   recheck facts without adjudication.
8. Run the mandatory second `statistical_consistency_checker` pass over all evidence, cross-lane
   candidates, and recheck facts. Append and verify every newly discovered candidate.
9. Run `evidence_quality_auditor` over every stable candidate ID. Repair missing card elements where
   source evidence permits, but do not remove or merge a stable candidate ID.
10. Run `report_generator`; use candidate-card part files when needed, then assemble detailed Markdown
    and standalone HTML in this initial run without omitting any stable ID.
11. Recompute source hashes, update `audit/run_metadata.json`, and fail source-integrity validation if
    any supplied source changed.
12. Mark every coverage row complete, run `scripts/validate_audit.py`, and repair correctable report or
    link defects.

## Script invocation pattern

Resolve the scripts from this loaded skill directory. Typical WSL commands are:

```text
~/venvs/stt/bin/python <skill>/scripts/convert_office_to_pdf.py <package> --config <root>/ai-validation.toml
~/venvs/stt/bin/python <skill>/scripts/run_ocr.py --config <root>/ai-validation.toml --package <package> detect
~/venvs/stt/bin/python <skill>/scripts/run_ocr.py --config <root>/ai-validation.toml --package <package> page <image> <text> --metadata <json>
~/venvs/stt/bin/python <skill>/scripts/render_report.py <markdown> <html> --config <root>/ai-validation.toml
~/venvs/stt/bin/python <skill>/scripts/validate_audit.py <audit-directory>
```

On native Windows, use `runtime.windows_python` and Windows paths for the same Python scripts. Use
`scripts/windows_tools.ps1` only for the reviewed Windows GPU check or Office conversion fallback.

## Completion

Every paper package requires its own nonempty `audit/final_report.html`; a report generated for another
package or only at the collection root never satisfies this requirement. Do not finish until all
canonical package artifacts exist and `audit/audit_validation.json` reports `PASS`. In an isolated
launcher worker, return JSON matching `batch/result.schema.json`. In an interactive paper session,
return a concise completion summary and a link to this package's `audit/final_report.html` without
making an adjudication.
