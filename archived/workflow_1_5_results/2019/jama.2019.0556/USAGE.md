# Workflow 1.4.1 Usage

1. Confirm that the paper package contains reusable OCR, text, table, workbook, page, or document-map
   assets. Use workflow 1.4.2 when those assets are absent or a source-first restart is required.
2. Back up the package-root `AGENTS.md` and `.codex/` management configuration.
3. Copy all workflow 1.4.1 content, including `.codex`, into the package root. Do not move, rename, or
   overwrite existing scientific records under `.ai_paper_validation/`.
4. Start a fresh Codex session at the package root. Do not use `resume`.
5. Send the complete `START_PROMPT.md` as the first request.
6. Confirm these outputs:

   - `.ai_paper_validation/final_report_1_4_1.md`
   - `.ai_paper_validation/final_report_1_4_1.html`
   - `.ai_paper_validation/review_1_4_1/review_validation.json`

The actual evidence determines the candidate count. The workflow must not create a count-limited
review queue or a `DEFERRED_BY_REVIEW_CAP` route. The 20–25 minute target is a planning target, not a
hard timeout.
