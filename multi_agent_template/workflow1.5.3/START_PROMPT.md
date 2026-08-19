Apply workflow 1.5.3 to this paper package now. Restart the complete quantitative quality-control
review without any candidate-count limit, while reusing all usable existing OCR, native text, layout
text, table/workbook extraction, rendered pages, and document maps. Do not read an old top-10 set,
review queue, verifier/critic disposition, endetail section, or final report as a scientific input or
candidate source. Treat reuse only as an optimization: freshly inspect and map every supplied-source
unit that lacks usable reusable extraction.

Use the OpenRouter provider and `env_key` supplied by `launch_openrouter.sh`. Keep the coordinator,
every named role, and every default or repair subagent on `~openai/gpt-latest`/`high`; never substitute
a built-in model slug or lower the reasoning effort. The launcher ignores conflicting base user
defaults for this run.

Require the launcher-created `routing_preflight.md`, including `Authentication probe: PASS` and
`Named agent presets: PASS`, before scientific work. Use a fresh, distinct
runtime agent for every mandatory specialist stage. Prefer the configured named role; when it is not
available, spawn a fresh default agent with the complete role contract and explicit reasoning effort,
while omitting a model override so the launcher-enforced default remains in force. Never reuse one
agent for two mandatory stages or use follow-up to change its model or effort.

Follow AGENTS.md from inventory through a passing validator result. Use the agent-first workflow and
durable artifact handoffs. Keep Python auxiliary: use direct local PDF, hashing, rendering, Office,
and CPU OCR tools whenever applicable, and use only the optional Office extractor, HTML renderer, and
validator Python helpers supplied by this workflow.

Set a package-specific latency target after inventory using total units, fresh-mapping burden, source
formats, OCR/conversion needs, and expected review waves. Do not assume a fixed SAP or package length.
Treat the earlier 102-total-page, 81-fresh-page run only as calibration for comparable workloads, not
as a universal 35–50 minute default. Use high reasoning for every specialist role. Spawn distinct new
`~openai/gpt-latest`/`high` agents for statistical passes 1 and 2, record them in
`agent_execution_manifest.md`, and never use follow-up to change an agent's contract. Treat timing as a
planning goal, never as permission to sample evidence, stop early, cap candidates, or omit cards.

Record every actual runtime agent in `agent_execution_manifest.md`, including the coordinator,
mappers, checkers, report generator, repairs, and both statistical agents. Through the finalized
`Finished UTC` cutoff, capture exact response-level token usage from authoritative runtime/API
metadata in `token_usage_ledger.csv`. Summarize it by agent and model. The dynamic OpenRouter route is
unpriced by default; leave the complete price blank unless dated rates for the exact resolved model
have been deliberately configured. Cached input and cache writes are input
subsets, and reasoning is an output subset; never double count them. If runtime usage is unavailable,
use `TOTALS_ONLY` when exact input/output/total counts remain available, otherwise use `UNAVAILABLE`
and exact `__` token fields. Leave any unsupported complete total or price explicitly incomplete
rather than estimating from text.

Focus the review on numeric, arithmetic, denominator/proportion/total, statistical-reporting,
cross-document numeric, effect-measure/label/scale, and rate-versus-count consistency. Retain
analysis-unit or population issues only when they create a concrete reported numeric or statistical
inconsistency. Report the actual number of candidates, including zero or more than 10, and include
every stable candidate in both the Markdown and standalone HTML reports.

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
