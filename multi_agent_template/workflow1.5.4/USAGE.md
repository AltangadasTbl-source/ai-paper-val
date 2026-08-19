# Workflow 1.5.4 Usage

1. Configure the provider in user-level `~/.codex/config.toml`, export `OPENROUTER_API_KEY` in the
   shell that will launch Codex, and review `OPENROUTER_SETUP.md`. Keep credentials out of the paper
   package.
2. Back up the package-root `AGENTS.md` and any unrelated `.codex/` controls.
3. Copy the current `AGENTS.md`, `OPENROUTER_SETUP.md`, common controls, `.codex/agents/` presets, and
   `workflow_1_5_4/` into the package root. Re-copy these updated control files into any paper package
   created from an older 1.5.4 template. Replace the nine `qc15-*` role presets with the current
   fixed-model versions while preserving unrelated `.codex` controls.
   Preserve every supplied source and every old `.ai_paper_validation/` record.
4. From the package root run `codex --approve-for-me`. After the interactive session opens, send
   `Read START_PROMPT.md completely and execute Workflow 1.5.4 now.` as the first request.
5. Confirm that `.ai_paper_validation/review_1_5_4/routing_preflight.md` reports `PASS`, coordinator
   `gpt-5.6-sol`/`high`, ordinary specialists `gpt-5.6-terra`/`medium`, statistical specialists
   `gpt-5.6-terra`/`high`, Sol specialists `gpt-5.6-sol`/`high`, `Coordinator inference: PASS`,
   `Execution mode: INTERACTIVE_CLI`, and `Named agent presets: PASS` before scientific mapping.
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
cutoff. It reports authoritative known usage by agent and model. Its USD amount is a token-only
API-equivalent estimate under the bundled dated Sol/Terra pricing snapshot, not a subscription or
vendor invoice.
