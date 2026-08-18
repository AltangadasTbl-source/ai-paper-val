# Workflow 1.4.2 Usage

1. Back up the package-root `AGENTS.md` and `.codex/` management configuration.
2. Copy all workflow 1.4.2 content, including `.codex`, into the package root. Preserve every supplied
   source and every old `.ai_paper_validation/` record.
3. Start a fresh Codex session at the package root. Do not use `resume`.
4. Send the complete `START_PROMPT.md` as the first request.
5. Confirm these outputs:

   - `.ai_paper_validation/final_report_1_4_2.md`
   - `.ai_paper_validation/final_report_1_4_2.html`
   - `.ai_paper_validation/review_1_4_2/review_validation.json`

The review must start from supplied sources rather than old OCR, extraction, candidate, or report
records. The actual evidence determines the candidate count. The 20–25 minute target is a planning
target, not permission to skip sources, statistical pass 2, candidates, or report cards.
