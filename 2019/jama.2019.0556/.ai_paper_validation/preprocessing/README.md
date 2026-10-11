# Preprocessing status

Native PDF text was successfully extracted for the scoped main-article and results-supplement pages; each selected page was assessed as usable. OCR recovery is not required for those pages.

Visual verification OCR remains required for main-article pages 3, 5, 6, 7, and 8 and results-supplement pages 16 through 23. The required backend-selection command used the active interpreter because `~/venvs/stt/bin/python` is absent. Its report selected `unavailable`, so OCR and preprocessing are blocked rather than silently skipped. See `ocr_backend.json` and `current_run_manifest.json`.

Pre-existing OCR derivatives are retained without modification but are not accepted as output of this run because their metadata names a different interpreter. Source PDFs were not modified.
