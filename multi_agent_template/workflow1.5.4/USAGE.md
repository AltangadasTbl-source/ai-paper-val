# Workflow 1.5.4 Usage

1. Verify the machine-level OpenRouter configuration and environment in `OPENROUTER_SETUP.md`.
2. Back up the package-root `AGENTS.md`. Leave an existing or read-only `.codex/` unchanged.
3. Copy `AGENTS.md`, `OPENROUTER_SETUP.md`, the common controls, and `workflow_1_5_4/` into the package root. The supplied
   `.codex/` presets may be merged only when safe; they are not required by the validator. Preserve
   every supplied source and every old `.ai_paper_validation/` record.
4. From the package root, run `bash workflow_1_5_4/scripts/launch_openrouter.sh`. Do not use plain
   `codex` or `resume`; the launcher applies the highest-precedence coordinator/default-subagent model
   overrides, verifies them, and sends the complete `START_PROMPT.md` as the first request.
5. Confirm that `.ai_paper_validation/review_1_5_4/routing_preflight.md` reports `PASS`, provider
   `openrouter`, model `~openai/gpt-latest`, and `Named agent presets: PASS` before scientific work
   begins.
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
