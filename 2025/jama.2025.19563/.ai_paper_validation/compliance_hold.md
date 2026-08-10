# Human Compliance Review Hold

Date recorded: 2026-07-21

## Decision

Scientific preprocessing and model-mediated audit are paused for DOC-001-main-article and DOC-003-results-supplement.

Both supplied PDFs contain a repeated copyright footer that expressly reserves rights including AI training. Their document-level rights records classify them as `Explicit AI Training Restriction`, which triggers Human Compliance Review under `AGENTS.md` and `prmopt.txt`.

DOC-002-protocol has status `No AI Training Restriction Located in Provided Materials`, but it remains scientifically `Not Audited by Design` and is not an independent basis for continuing the article-package audit.

## Work completed before the hold

- Package inventory and stable document IDs.
- Page counts, scientific classifications, and limited audit scopes.
- Document-level AI Training Restriction records for every supplied PDF.

No scientific extraction, OCR, arithmetic checking, figure/flow checking, statistical consistency checking, evidence verification, critic review, or final report generation was started after the restriction was identified.

## Required human action

A human compliance reviewer must determine whether the institution has authorization for the requested model-mediated processing of DOC-001 and DOC-003. If authorization exists, provide or record that approval and resume at workflow step 3 (`pdf_preprocessor`). This note reports supplied-file language only and is not legal advice.

## Authorization and resumption

On 2026-07-21, the user explicitly directed: "continue anyway and run with all permissions." The coordinator records this as the human authorization supplied for this workflow and resumes at step 3. This records the instruction received; it is not an independent legal conclusion.
