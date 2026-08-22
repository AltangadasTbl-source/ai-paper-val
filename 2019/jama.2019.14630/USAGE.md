# Workflow 1.5.1 Usage

1. Confirm that the paper package contains reusable OCR, text, table, workbook, page, or document-map
   assets. Use workflow 1.5.2 when those assets are absent or a source-first restart is required.
2. Back up the package-root `AGENTS.md`. Leave an existing or read-only `.codex/` unchanged.
3. Copy `AGENTS.md`, the common controls, and `workflow_1_5_1/` into the package root. The supplied
   `.codex/` presets may be merged only when safe; they are not required by the validator. Do not move,
   rename, or overwrite scientific records under `.ai_paper_validation/`.
4. Start a fresh Codex session at the package root. Do not use `resume`.
5. Send the complete `START_PROMPT.md` as the first request.
6. Confirm these outputs:

   - `.ai_paper_validation/final_report_1_5_1.md`
   - `.ai_paper_validation/final_report_1_5_1.html`
   - `.ai_paper_validation/review_1_5_1/review_validation.json`
   - `.ai_paper_validation/review_1_5_1/token_usage_summary.md`
   - `.ai_paper_validation/review_1_5_1/token_usage_summary.json`

The actual evidence determines the candidate count. The workflow must not create a count-limited
review queue or a `DEFERRED_BY_REVIEW_CAP` route. Set a package-specific timing range from complete
source inventory, fresh-mapping burden, formats, and conversion/OCR needs. Do not infer timing from SAP or
page count alone; the prior 102-total-page package is a calibration example only. Timing is not a hard
timeout.

The token summary covers the coordinator and every manifested agent through the finalized review
cutoff. It reports authoritative known usage by agent and model. Its USD amount is a token-only
API-equivalent estimate under `workflow_1_5_1/token_pricing.toml`, not a subscription or vendor bill.
Refresh that dated snapshot deliberately when a different pricing date is required.
