Apply workflow 1.3.2 to this paper package now. Restart the entire quantitative quality-control review
from the supplied source files, including fresh inventory, PDF/Office/text/table preparation,
quantitative relationship mapping, uncapped candidate discovery, source recheck, quality audit, and
reporting. Preserve but ignore all old OCR, extraction, candidate, queue, verifier/critic, endetail,
and report records as evidence inputs.

Follow AGENTS.md from source hashing through a passing validator result. Use the agent-first workflow
and durable artifact handoffs. Keep Python auxiliary: use direct local PDF, hashing, rendering,
Office, and CPU OCR tools whenever applicable, and use only the optional Office extractor, HTML
renderer, and validator Python helpers supplied by this workflow.

Focus the review on numeric, arithmetic, denominator/proportion/total, statistical-reporting,
cross-document numeric, effect-measure/label/scale, and rate-versus-count consistency. Retain
analysis-unit or population issues only when they create a concrete reported numeric or statistical
inconsistency. Report the actual number of candidates, including zero or more than 10, and include
every stable candidate in both the Markdown and standalone HTML reports.

Use professional English throughout. Frame the work as publication quality control and prevention of
avoidable defects entering downstream evidence synthesis, not as an effort to expose severe errors.
Preserve every source and old artifact, use truthful relative source links, mark all candidates
Pending Human Adjudication, and finish only when `review_validation.json` reports `PASS`.
