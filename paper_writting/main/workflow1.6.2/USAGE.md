# Workflow 1.6.2 Usage

1. Review `CODEX_SETUP.md`. The run uses the provider and authentication of the current Codex
   session; no provider is configured for this workflow. Keep credentials out of the paper package.
2. Confirm that the paper package contains reusable OCR, text, table, workbook, page, or document-map
   assets. Workflow 1.6.2 reuses those assets; it does not replace a source-first preprocessing run.
3. Local tools: poppler (`pdfinfo`, `pdftotext`, `pdftoppm`), `tesseract`, and LibreOffice are used
   when installed but are not required. When one is missing, the run creates a temporary Python
   environment inside `.ai_paper_validation/review_1_6_2/tooling/`, installs pinned PyMuPDF and pypdf
   (plus CPU OCR only if needed), uses the bundled fallback helper, and removes the environment at the
   end. Nothing is installed into the global Python. This needs `python3` (3.9 or newer) and network
   access for `pip`; see `CODEX_SETUP.md` for enabling network access in the Codex sandbox, or
   pre-create the environment yourself from the package root before starting Codex:
   `python3 workflow_1_6_2/scripts/bootstrap_tooling.py create --ocr`.
4. Back up the package-root `AGENTS.md` and any unrelated `.codex/` controls.
5. Copy the current `AGENTS.md`, `CODEX_SETUP.md`, common controls, `.codex/agents/` presets,
   `.codex/rules/workflow-1-6-2.rules`, `.codex/config.toml`, and `workflow_1_6_2/` into the package root.
   Add the ten `qc162-*` role presets while preserving unrelated `.codex` controls. Older `qc15-*` or
   `qc16-*` presets may remain; workflow 1.6.2 uses only the `qc162_*` roles. Do not move, rename, or overwrite
   scientific records under `.ai_paper_validation/`.
6. From the package root run `codex --approve-for-me`. After the interactive session opens, send
   `Read START_PROMPT.md completely and execute Workflow 1.6.2 now.` as the first request.
7. Confirm that `.ai_paper_validation/review_1_6_2/routing_preflight.md` reports `PASS`, the run model
   (default `gpt-6.1-sol`, or the exact ID you chose when asked), coordinator
   `gpt-6.1-sol`/`high`, ordinary specialists `gpt-6.1-sol`/`medium`, statistical specialists
   `gpt-6.1-sol`/`high`, screening, recheck and audit specialists `gpt-6.1-sol`/`high`, `Provider: CURRENT_SESSION`, `Coordinator inference:
   PASS`, `Execution mode: INTERACTIVE_CLI`, and `Named agent presets: PASS` before scientific mapping.
8. Confirm these outputs:

   - `.ai_paper_validation/final_report_1_6_2.md`
   - `.ai_paper_validation/final_report_1_6_2.html`
   - `.ai_paper_validation/review_1_6_2/screening/inclusion_screen.md` with one decision per finding
   - `.ai_paper_validation/review_1_6_2/candidate_ledger.md` with its classification table
   - `.ai_paper_validation/review_1_6_2/tooling_record.md` showing the tools used and, if a fallback
     environment was created, `Fallback environment removed: YES`
   - `.ai_paper_validation/review_1_6_2/review_validation.json` with status `PASS`

The inclusion threshold, applied finding by finding, determines the candidate count. There is no
expected or target number, and the workflow must not create a count-limited review queue or a
`DEFERRED_BY_REVIEW_CAP` route. Set a package-specific timing range from complete
source inventory, fresh-mapping burden, formats, and conversion/OCR needs. Do not infer timing from SAP or
page count alone; the prior 102-total-page package is a calibration example only. Timing is not a hard
timeout.

Each candidate's review domain, relationship type, evidence state, and inclusion audit appear in the
candidate ledger and on its report card. These fields support human adjudication; the human reviewer
makes every decision, including the disposition.
