Apply workflow 1.4.1 to this paper package now. Restart the complete quantitative quality-control
review without any candidate-count limit, while reusing all usable existing OCR, native text, layout
text, table/workbook extraction, rendered pages, and document maps. Do not read an old top-10 set,
review queue, verifier/critic disposition, endetail section, or final report as a scientific input or
candidate source.

Follow AGENTS.md from inventory through a passing validator result. Use the agent-first workflow and
durable artifact handoffs. Keep Python auxiliary: use direct local PDF, hashing, rendering, Office,
and CPU OCR tools whenever applicable, and use only the optional Office extractor, HTML renderer, and
validator Python helpers supplied by this workflow.

Use the workflow 1.4 latency profile: target 20–25 minutes for a typical single-paper package, use
medium reasoning for ordinary Terra roles, retain high reasoning only for the statistical consistency
role, and avoid redundant agent waves. Treat the target as a planning goal, never as permission to
sample evidence, stop early, cap candidates, or omit report cards.

Focus the review on numeric, arithmetic, denominator/proportion/total, statistical-reporting,
cross-document numeric, effect-measure/label/scale, and rate-versus-count consistency. Retain
analysis-unit or population issues only when they create a concrete reported numeric or statistical
inconsistency. Report the actual number of candidates, including zero or more than 10, and include
every stable candidate in both the Markdown and standalone HTML reports.

Use professional English throughout. Frame the work as publication quality control and prevention of
avoidable defects entering downstream evidence synthesis, not as an effort to expose severe errors.
Preserve every source and legacy artifact, use truthful relative source links, mark all candidates
Pending Human Adjudication, and finish only when `review_validation.json` reports `PASS`.
