Apply workflow 1.6 to this paper package now. Perform the complete quantitative quality-control
review without any candidate-count limit, while reusing all usable existing OCR, native text, layout
text, table/workbook extraction, rendered pages, and document maps. Do not read an old candidate set,
review queue, verifier/critic disposition, endetail section, classification record, or final report as
a scientific input or candidate source. Treat reuse only as an optimization: freshly inspect and map
every supplied-source unit that lacks usable reusable extraction.

This interactive session must run as `gpt-6.1-sol`/`high`. Before scientific work, verify all nine
named presets against the fixed 1.6 model matrix and write `routing_preflight.md` with
`Coordinator inference: PASS`, `Named agent presets: PASS`, and `Execution mode: INTERACTIVE_CLI`.
Every role uses `gpt-6.1-sol`. Use `medium` reasoning for ordinary specialist roles, distinct fresh
`gpt-6.1-sol`/`high` agents for statistical passes 1 and 2, and `gpt-6.1-sol`/`high` for mechanical
evidence recheck with classification confirmation and for the final evidence-quality and
classification audit. Do not use `~openai/gpt-latest` or another moving alias.

Use a fresh, distinct runtime agent for every mandatory specialist stage. Prefer the configured named
role. If a named role is unavailable, spawn a fresh default agent with the complete role contract and
the exact model and reasoning effort required for that role. Never omit the model override on a
fallback, reuse one agent for two mandatory stages, or use follow-up to change its model or effort.

Before source inventory, probe local tools with `workflow_1_6/scripts/pdf_tools.py probe`. If PDF
information, text, or rendering tools are missing, create the temporary package-local fallback
environment with `workflow_1_6/scripts/bootstrap_tooling.py create` (add `--ocr` only when OCR may be
needed and tesseract is absent), use the bundled fallback helper only for missing capabilities, record
everything in `tooling_record.md`, and remove the environment before final validation. Never install
into the global Python environment.

Follow AGENTS.md from inventory through a passing validator result. Use the agent-first workflow and
durable artifact handoffs. Keep Python auxiliary: use direct local PDF, hashing, rendering, Office,
and CPU OCR tools whenever applicable, and use only the optional Office extractor, HTML renderer, and
validator Python helpers supplied by this workflow.

Set a package-specific latency target after inventory using total units, fresh-mapping burden, source
formats, OCR/conversion needs, and expected review waves. Do not assume a fixed SAP or package length.
Treat the earlier 102-total-page, 81-fresh-page run only as calibration for comparable workloads, not
as a universal 35–50 minute default. Spawn distinct new `gpt-6.1-sol`/`high` agents for statistical
passes 1 and 2, record them in `agent_execution_manifest.md`, and never use follow-up to change an
agent's contract. Treat timing as a planning goal, never as permission to sample evidence, stop early,
cap candidates, or omit cards.

Record every actual runtime agent in `agent_execution_manifest.md`, including the coordinator,
mappers, checkers, report generator, repairs, and both statistical agents.

Focus the review on numeric, arithmetic, denominator/proportion/total, statistical-reporting,
cross-document numeric, effect-measure/label/scale, and rate-versus-count consistency. Retain
analysis-unit or population issues only when they create a concrete reported numeric or statistical
inconsistency. Report the actual number of candidates, including zero or more than 10, and include
every stable candidate in both the Markdown and standalone HTML reports.

Classify every stable candidate under `QUALITY_CONTROL_SCOPE.md`: assign document roles by content,
one primary relationship type (`P_R`, `P_P`, `S_C`, or `S_W`) with precedence `P_R` > `P_P` > `S_C` >
`S_W`, all relationships, the derived review domain, the evidence state from the mechanical recheck,
and the derived suggested review disposition. These fields pre-fill human review; they are not
adjudications.

Do not treat a coherent very small P value displayed as `P = 0`, `p = 0.000`, or equivalent as a
candidate. Record it as `DISPLAY_ZERO_NOT_CANDIDATE` when needed for coverage. Assign a candidate only
for an independent supplied-source contradiction, and describe that contradiction rather than the
display-zero shorthand.

Use professional English throughout. Frame the work as publication quality control and prevention of
avoidable defects entering downstream evidence synthesis, not as an effort to expose severe errors.
Preserve every source and legacy artifact, use truthful relative source links, mark all candidates
Pending Human Adjudication, use exact `__` placeholders for all five human adjudication fields, place
only one artifact path in each coverage-manifest row, and finish only when
`review_validation.json` reports `PASS`. Validation must not require a writable root `.codex`.
