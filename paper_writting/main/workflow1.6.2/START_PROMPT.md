Apply workflow 1.6.2 to this paper package now. Perform the complete quantitative quality-control
review, while reusing all usable existing OCR, native text, layout text, table/workbook extraction,
rendered pages, and document maps. Do not read an old candidate set, review queue, screening log,
verifier/critic disposition, endetail section, classification record, or final report as a scientific
input or candidate source. Treat reuse only as an optimization: freshly inspect and map every
supplied-source unit that lacks usable reusable extraction.

The default run model is `gpt-6.1-sol`, and every role uses the run model. If it is rejected or
unavailable, or a different model is wanted, stop and ask the user for the exact model ID; never pick a
substitute yourself, and read every later mention of `gpt-6.1-sol` as the run model. Record `Run
model` and `Run model source` (`DEFAULT` or `USER_SELECTED`) in the preflight. This interactive session
runs as the run model at `high`. Before scientific work, verify all ten
named presets against the fixed 1.6.2 model matrix and write `routing_preflight.md` with
`Coordinator inference: PASS`, `Named agent presets: PASS`, `Execution mode: INTERACTIVE_CLI`, and
`Provider: CURRENT_SESSION`. Use the provider of this session; do not configure or change a provider. Every role uses `gpt-6.1-sol`. Use `medium` reasoning for
ordinary specialist roles, distinct fresh `gpt-6.1-sol`/`high` agents for statistical passes 1 and 2,
and `gpt-6.1-sol`/`high` for the inclusion screen, the mechanical evidence recheck, and the final
evidence-quality audit. Do not use `~openai/gpt-latest` or another moving alias.

Use a fresh, distinct runtime agent for every mandatory specialist stage. Prefer the configured named
role. If a named role is unavailable, spawn a fresh default agent with the complete role contract and
the exact model and reasoning effort required for that role. Never omit the model override on a
fallback, reuse one agent for two mandatory stages, or use follow-up to change its model or effort.

Before source inventory, probe local tools with `workflow_1_6_2/scripts/pdf_tools.py probe`. If PDF
information, text, or rendering tools are missing, create the temporary package-local fallback
environment with `workflow_1_6_2/scripts/bootstrap_tooling.py create` (add `--ocr` only when OCR may
be needed and tesseract is absent), use the bundled fallback helper only for missing capabilities,
record everything in `tooling_record.md`, and remove the environment before final validation. Never
install into the global Python environment. Rendering and OCR run on the CPU by default: tell the user
so before the first rendering or OCR step, and use a GPU only if the user explicitly asks; record
`Compute device` in `tooling_record.md`.

Follow AGENTS.md from inventory through a passing validator result. Use the agent-first workflow and
durable artifact handoffs. Keep Python auxiliary: use direct local PDF, hashing, rendering, Office,
and CPU OCR tools whenever applicable, and use only the optional Office extractor, tooling helpers,
HTML renderer, and validator Python helpers supplied by this workflow.

Set a package-specific latency target after inventory using total units, fresh-mapping burden, source
formats, OCR/conversion needs, and expected review waves. Treat timing as a planning goal, never as
permission to sample evidence, stop early, or omit cards. Record every actual runtime agent in
`agent_execution_manifest.md`.

Focus the review on four areas defined in `QUALITY_CONTROL_SCOPE.md`: counts and denominators,
estimate and test logic, statistical method logic, and planned versus reported statistical design.
Register a candidate when it is reproduced and qualifies by at least one route: route A, an
always-register category listed below; or route B, in focus, not resolved at once by a statistically
literate reader in the field from common sense or the immediate context, and able to change the
interpretation of a named result or the value a data extractor would take. Screen out differences
within the display-precision rule (each displayed input keeps its half-unit rounding interval; a
remaining relative discrepancy of at most 0.05 is rounding, above 0.05 it is not), `P = 0` and similar
display zeros, symbol slips that change no printed number (such as a missing `<` in a P value),
terminology and wording differences across the text, model-based estimates compared with crude
ratios, details the paper does not report when no printed value conflicts, and peripheral
cross-document comparisons (copies of baseline descriptive values between the main and supplementary
baseline tables, per-time-point counts, footnote pointers, numbers of sites, recruitment calendars,
and other plan-internal details) unless they change a primary or key secondary result, the size of an
analysis population, or a planned decision rule. Route A (always register, whenever reproduced): an interval
that conflicts with its P value or test, or an estimate outside its interval; a sign, digit, or
decimal slip in a printed result, or a reversed direction statement, that changes significance,
direction, or magnitude as printed, even when the intended value can be reconstructed; a count,
denominator, and percentage that do not reconcile within one display, including baseline tables; a
printed result that a method reproducing the other rows of the same display does not reproduce; and
a changed outcome status or composite, an analysis called prespecified but absent from the plan, or a
planned primary or key secondary analysis that is not reported. When in doubt about wording,
terminology, or a symbol, screen out; when in doubt about a printed number, interval, P value, count,
or planned-versus-reported element, register it. Register one candidate per issue, listing every
location of a repeated pattern. There is no expected, typical, minimum, maximum, or target number of candidates;
decide each finding on the criteria alone, and zero is a valid result.

Assign every candidate one of the four review domains (`statistical_results`,
`report_internal_inconsistency`, `protocol_report`, `plan_material`), its document roles, and one
relationship type (`P_R`, `P_P`, `S_C`, or `S_W`) with precedence `P_R` > `P_P` > `S_C` > `S_W`. These
fields pre-fill human review; they are not adjudications.

Write every prompt, generated artifact, log, and report in professional English only. Call each item a candidate or reporting issue and describe it as
an inconsistency, a discrepancy, or a result that does not reconcile; never describe a candidate, a
value, or the authors' work with the words error, mistake, defect, erroneous, wrong, or incorrect.
Preserve every source and legacy artifact, use truthful relative source links, mark all candidates
Pending Human Adjudication (human adjudication is recorded later in the review workbook, not in the
report), place only one artifact path in each coverage-manifest row, and finish only when `review_validation.json`
reports `PASS`. Validation must not require a writable root `.codex`.
