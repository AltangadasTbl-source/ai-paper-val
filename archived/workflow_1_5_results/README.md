# Workflow 1.5.x results archive

Created 2026-10-10 when the 44 paper packages in `2018/`, `2019/`, `2024/` and `2025/` were prepared
for workflow 1.6. `jama.2019.0556` was already moved to `archived/local_only/2019/` for a complete
rerun and is not part of this archive.

## What was moved here

3,060 files, by `archive_1_5_results.py --execute`. Each file keeps its package-relative path under
`<year>/<paper>/`, so `2019/jama.2019.10517/.ai_paper_validation/final_report_1_5_1.md` here came
from `2019/jama.2019.10517/.ai_paper_validation/final_report_1_5_1.md` in the repository.

- Workflow 1.5.1, 1.5.2 and 1.5.3 results:
  - `final_report_1_5_x.md`/`.html`;
  - the `review_1_5_x/` run directories, except their `preprocessing/` folders;
  - preserved prior runs (`review_1_5_2_prior_*`).
- Results from earlier workflows: `final_report.md`, human adjudication reports and submissions,
  candidate shortlists and dispositions, checker, critic, verifier and report-generator outputs,
  workflow status and trace files.
- Within `document_outputs/`: checker, candidate, critic, verifier and agent-response files.
- Package-root workflow controls for 1.5.x: `AGENTS.md`, `README.md`, `START_PROMPT.md`, `USAGE.md`,
  `PERFORMANCE_PROFILE.md`, `QUALITY_CONTROL_SCOPE.md`, `OPENROUTER_SETUP.md`, `workflow_1_5_x/`,
  `.codex/config.toml`, `.codex/agents/qc15-*.toml` and `.codex/rules/workflow-1-5-x.rules`.
- Two package-root files that workflow 1.6 would otherwise treat as paper sources:
  - `2024/jama.2024.2302/Detailed_Errors_On_C1_C3_C5.docx`, an earlier error annotation;
  - `2025/jama.2025.11178/~$joi250046supp5_prod_1755300121.16087.xlsx`, an Office lock file. It is
    ignored by git through the `~$*` rule.

## What stayed in the packages

Paper sources (PDF and XLSX), download notes and supplement images stayed at each package root.
Reusable extraction assets stayed under `.ai_paper_validation/`: OCR and native/layout text, rendered
pages, page and package manifests, document and preprocessing records, extractor outputs,
preprocessing scripts, and the `preprocessing/` folders of the 1.5.x run directories. Workflow 1.6
reuses these. Before the move, no kept file contained candidate headings (`## C001` style) or
"Pending Human Adjudication" text.

## Records and restoring

- `archive_manifest.csv` lists every moved file: year, paper, package-relative path, archive path,
  size and SHA-256. Each hash was checked after its move.
- `archive_1_5_results.py` holds the exact classification rules. Its dry run (no `--execute`)
  reports what it would move. It refuses to run again while `archive_manifest.csv` exists.
- To restore a file, move it from `<year>/<paper>/<path>` here back to `<year>/<paper>/<path>` in the
  repository. The 1.6 controls installed in each package do not overlap with any archived path.

## jama.2019.0556 (added 2026-10-10)

`jama.2019.0556` had been set aside in `archived/local_only/2019/` after a workflow 1.4.1 run. It was
moved back to `2019/jama.2019.0556/` and prepared for workflow 1.6 with `archive_0556_workflow_1_4_1.py`,
which applies the rules above plus 1.4.1-specific ones:

- 69 files went to `2019/jama.2019.0556/` here: the 1.4.1 and earlier final reports, the
  `review_1_4_1/` run directory, `validation_trace.md`, the per-document agent response traces, and
  the 1.4.1 controls (`workflow1.4.1/`, `workflow_1_4_1/`, root control documents,
  `.codex/config.toml`).
- 90 files of a locally unpacked tesseract install (`.ai_paper_validation/local_ocr/`, about 30 MB of
  binaries and `.deb` packages) went to `archived/local_only/2019/jama.2019.0556_workflow_1_4_1_local_ocr/`,
  which git ignores. Workflow 1.6 uses its own temporary fallback environment instead.
- Two empty folders, `.git` and `.agents`, were removed.
- `archive_manifest_jama.2019.0556.csv` lists all 159 moved files with SHA-256 hashes.

The package kept its five source PDFs and 82 extraction files (normalized text, OCR text, rendered
pages, page manifests, document status records, and preprocessing records).
