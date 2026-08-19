# Workflow 1.5.4 Usage

1. Export `OPENROUTER_API_KEY` in the shell that will launch the workflow and review
   `OPENROUTER_SETUP.md`. Do not add `[model_providers.openrouter.auth]` to a paper package: Codex
   ignores project-scoped provider/auth configuration, and this workflow uses `env_key` instead.
2. Back up the package-root `AGENTS.md`. Leave an existing or read-only `.codex/` unchanged.
3. Copy the current `AGENTS.md`, `OPENROUTER_SETUP.md`, common controls, `.codex/agents/` presets, and
   `workflow_1_5_4/` into the package root. Re-copy these updated control files into any paper package
   created from an older 1.5.4 template. The launcher requires the nine supplied role presets; merge
   them without overwriting unrelated `.codex` controls. They contain no provider credentials.
   Preserve every supplied source and every old `.ai_paper_validation/` record.
4. From the package root, optionally run
   `bash workflow_1_5_4/scripts/launch_openrouter.sh --preflight-only`, then run
   `bash workflow_1_5_4/scripts/launch_openrouter.sh`. Do not use plain `codex` or `resume`; the launcher
   uses `codex exec --ignore-user-config`, injects the complete OpenRouter provider with
   `env_key="OPENROUTER_API_KEY"`, fixes the coordinator and every default/named subagent at
   `~openai/gpt-latest`/`high`, performs a real ephemeral authentication request, and sends the
   complete `START_PROMPT.md` as the first review request.
5. Confirm that `.ai_paper_validation/review_1_5_4/routing_preflight.md` reports `PASS`, provider
   `openrouter`, model `~openai/gpt-latest`, reasoning effort `high`, `Authentication probe: PASS`,
   `Credential source: OPENROUTER_API_KEY via env_key`, `User config: IGNORED`, and
   `Named agent presets: PASS` before scientific work begins.
6. Confirm these outputs:

   - `.ai_paper_validation/final_report_1_5_4.md`
   - `.ai_paper_validation/final_report_1_5_4.html`
   - `.ai_paper_validation/review_1_5_4/review_validation.json`
   - `.ai_paper_validation/review_1_5_4/token_usage_summary.md`
   - `.ai_paper_validation/review_1_5_4/token_usage_summary.json`

The review must start from supplied sources rather than old OCR, extraction, candidate, or report
records. The actual evidence determines the candidate count. Set a package-specific timing range from
complete source inventory, fresh-mapping burden, formats, and conversion/OCR needs. Do not infer timing from
SAP or page count alone; the prior 102-total-page package is a calibration example only. Timing never
permits skipped sources, statistical pass 2, candidates, or report cards.

The token summary covers the coordinator and every manifested agent through the finalized review
cutoff. It reports authoritative known usage by agent and model. The bundled pricing file intentionally
contains no rate for the dynamic `~openai/gpt-latest` route, so exact token totals remain available but
the complete USD price is blank. Add dated rates only for the exact resolved model reported by the
runtime; do not price the moving alias with a stale fixed-model rate.
