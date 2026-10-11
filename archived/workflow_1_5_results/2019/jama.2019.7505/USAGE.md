# Workflow 1.5.2 Usage

1. Back up the package-root `AGENTS.md`. Leave an existing or read-only `.codex/` unchanged.
2. Copy `AGENTS.md`, the common controls, and `workflow_1_5_2/` into the package root. The supplied
   `.codex/` presets may be merged only when safe; they are not required by the validator. Preserve
   every supplied source and every old `.ai_paper_validation/` record.
3. Start a fresh Codex session at the package root. Do not use `resume`.
4. Send the complete `START_PROMPT.md` as the first request.
5. Confirm these outputs:

   - `.ai_paper_validation/final_report_1_5_2.md`
   - `.ai_paper_validation/final_report_1_5_2.html`
   - `.ai_paper_validation/review_1_5_2/review_validation.json`
   - `.ai_paper_validation/review_1_5_2/token_usage_summary.md`
   - `.ai_paper_validation/review_1_5_2/token_usage_summary.json`

The review must start from supplied sources rather than old OCR, extraction, candidate, or report
records. The actual evidence determines the candidate count. Set a package-specific timing range from
complete source inventory, fresh-mapping burden, formats, and conversion/OCR needs. Do not infer timing from
SAP or page count alone; the prior 102-total-page package is a calibration example only. Timing never
permits skipped sources, statistical pass 2, candidates, or report cards.

The token summary covers the coordinator and every manifested agent through the finalized review
cutoff. It reports authoritative known usage by agent and model. Its USD amount is a token-only
API-equivalent estimate under `workflow_1_5_2/token_pricing.toml`, not a subscription or vendor bill.
Refresh that dated snapshot deliberately when a different pricing date is required.
