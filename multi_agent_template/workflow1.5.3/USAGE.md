# Workflow 1.5.3 Usage

1. Export `OPENROUTER_API_KEY` in the shell that will launch the workflow and review
   `OPENROUTER_SETUP.md`. Do not add `[model_providers.openrouter.auth]` to a paper package: Codex
   ignores project-scoped provider/auth configuration, and this workflow uses `env_key` instead.
2. Confirm that the paper package contains reusable OCR, text, table, workbook, page, or document-map
   assets. Use workflow 1.5.4 when those assets are absent or a source-first restart is required.
3. Back up the package-root `AGENTS.md`. Leave an existing or read-only `.codex/` unchanged.
4. Copy the current `AGENTS.md`, `OPENROUTER_SETUP.md`, common controls, `.codex/agents/` presets, and
   `workflow_1_5_3/` into the package root. Re-copy these updated control files into any paper package
   created from an older 1.5.3 template. The launcher requires the nine supplied role presets; merge
   them without overwriting unrelated `.codex` controls. They contain no provider credentials. Do not
   move, rename, or overwrite scientific records under `.ai_paper_validation/`.
5. From the package root, optionally run
   `bash workflow_1_5_3/scripts/launch_openrouter.sh --preflight-only`, then run
   `bash workflow_1_5_3/scripts/launch_openrouter.sh`. Do not use plain `codex` or `resume`; the launcher
   uses `codex exec --ignore-user-config`, injects the complete OpenRouter provider with
   `env_key="OPENROUTER_API_KEY"`, fixes the coordinator and every default/named subagent at
   `~openai/gpt-latest`/`high`, performs a real ephemeral authentication request, and sends the
   complete `START_PROMPT.md` as the first review request.
6. Confirm that `.ai_paper_validation/review_1_5_3/routing_preflight.md` reports `PASS`, provider
   `openrouter`, model `~openai/gpt-latest`, reasoning effort `high`, `Authentication probe: PASS`,
   `Credential source: OPENROUTER_API_KEY via env_key`, `User config: IGNORED`, and
   `Named agent presets: PASS` before scientific work begins.
7. Confirm these outputs:

   - `.ai_paper_validation/final_report_1_5_3.md`
   - `.ai_paper_validation/final_report_1_5_3.html`
   - `.ai_paper_validation/review_1_5_3/review_validation.json`
   - `.ai_paper_validation/review_1_5_3/token_usage_summary.md`
   - `.ai_paper_validation/review_1_5_3/token_usage_summary.json`

The actual evidence determines the candidate count. The workflow must not create a count-limited
review queue or a `DEFERRED_BY_REVIEW_CAP` route. Set a package-specific timing range from complete
source inventory, fresh-mapping burden, formats, and conversion/OCR needs. Do not infer timing from SAP or
page count alone; the prior 102-total-page package is a calibration example only. Timing is not a hard
timeout.

The token summary covers the coordinator and every manifested agent through the finalized review
cutoff. It reports authoritative known usage by agent and model. The bundled pricing file intentionally
contains no rate for the dynamic `~openai/gpt-latest` route, so exact token totals remain available but
the complete USD price is blank. Add dated rates only for the exact resolved model reported by the
runtime; do not price the moving alias with a stale fixed-model rate.
