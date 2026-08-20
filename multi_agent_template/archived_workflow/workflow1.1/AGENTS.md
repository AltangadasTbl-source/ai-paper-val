# Agent-first AI Paper Validation

This Git repository is one paper collection. Each direct, non-management child directory is one
paper package containing one main article and zero or more supplements. Shared instructions, models,
skills, scripts, and tool rules live only at the collection root.

Use English only in prompts, generated artifacts, logs, and reports.

## Choose the operating mode

Determine the mode from the working directory and the user's request.

### Collection coordinator

Use this mode when the working directory is the repository root and the user requests one or more
paper packages.

- Remain the user-facing agent. Do not inspect or analyze paper contents in the root context.
- Discover only direct child package names and source-file presence.
- Read `ai-validation.toml` and honor its worker, runtime, OCR, and tool settings.
- For strict per-paper context isolation, invoke the thin `batch/run_batch.py` launcher with the
  requested package names and concurrency. The launcher starts a fresh ephemeral `codex exec` for
  each package and contains no scientific workflow logic.
- When running under WSL, use `runtime.wsl_python`; when running natively on Windows, use
  `runtime.windows_python`. Resolve `~` only in the selected environment.
- If the environment cannot execute the configured Codex CLI, report that strict isolated-worker
  mode is unavailable. Do not silently process multiple papers in one model context.
- After workers exit, read only their `audit/result.json` summaries unless the user asks to open a
  specific report. Confirm that every completed package has its own `audit/final_report.html` and
  present results in natural package-name order.

### Paper worker

Use this mode when the working directory is exactly one direct child paper package. Invoke
`$ai-validation` and complete the package audit in this agent context. Specialist agents may read only
this package's sources and artifacts.

## Paper-package isolation

- Never inspect sibling paper packages or import findings from another paper.
- Parent-level management files may be read only to run the shared workflow.
- Preserve source files unchanged and write all derived artifacts below `./audit/`.
- If evidence is missing, record it as missing; do not search siblings, the web, or external sources.

## Session and context sufficiency

- Every package in a multi-paper run must be launched by a separate `codex exec --ephemeral --cd
  <package>` process. Never use `resume`, reuse a process, or place two packages in one model session.
- Concurrent package workers have independent full model contexts; concurrency does not divide one
  context window among packages. `--ephemeral` isolates session history, not the operating system.
- Keep the paper-worker coordinator context compact. Specialist agents must write complete results to
  their assigned paths below `audit/` and return only a short status, scope, counts, unresolved items,
  and artifact paths.
- Read the `[context]` thresholds in `ai-validation.toml`. When a stage exceeds either its text/page
  threshold or its candidate threshold, split it into disjoint page, section, relationship, or
  candidate-ID shards. Run as many waves as needed; a shard size is never a finding-count limit.
- Record every shard, its exact scope, status, and artifact path in `audit/context_coverage.md`. Every
  eligible page, relationship, and stable candidate ID must be covered exactly once per applicable
  stage before final synthesis. Do not generate the final report from incomplete shards.
- If the coordinator context is compacted or restarted, reconstruct state from the durable `audit/`
  artifacts and coverage record instead of relying on prior chat messages.

## Scientific workflow invariants

- Keep every distinct candidate. There is no candidate or finding count limit.
- Do not assign `Major`, `Minor`, `Uncertain`, `Verified`, `Rejected`, acceptance, exclusion, severity,
  validity, or equivalent AI judgments.
- Deduplicate only genuine duplicates before stable IDs are assigned. Never remove or merge a stable ID.
- Give statistical checking equal or greater priority than every other checking lane and complete its
  mandatory second reconciliation pass.
- Generate detailed Markdown and standalone HTML in the initial audit. Do not require a later
  detailing prompt.
- Produce `<package>/audit/final_report.html` independently for every requested paper package. A
  package is failed, not completed, when its nonempty HTML report or passing validator record is absent.
- Make every evidence citation a relative link to the exact PDF page ending in `#page=N`.
- Submit every candidate as `Pending Human Adjudication`.
- Keep the coordinator on `gpt-5.6-sol` with high reasoning, every Terra role on ultra reasoning, and
  never use a Luna model.

## OCR and source formats

The paper worker, not the launcher, decides whether OCR is necessary. Use native PDF text first.
Read the exact backend from `ai-validation.toml`; never change a configured GPU task to CPU or switch
CPU engines implicitly. A missing configured backend blocks only work that actually requires OCR.

Convert direct DOC/DOCX supplements to derived PDFs inside the paper worker before analyzing their
content. Keep the source unchanged. Treat XLSX and other non-PDF evidence as manual-review material.

## Allowed categories

- `Arithmetic inconsistency`
- `Cross-document inconsistency`
- `Statistical reporting inconsistency`
- `Participant flow inconsistency`
- `Presentation inconsistency`

Do not assess misconduct, raw-data validity, clinical appropriateness, general methodological
limitations, novelty, or information outside the paper package.
