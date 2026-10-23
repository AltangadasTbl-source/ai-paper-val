# Workflow 1.6.2 Artifact and Report Specification

## Canonical artifacts

Write new artifacts only below `.ai_paper_validation/review_1_6_2/`, except for the two versioned
reports stored directly below `.ai_paper_validation/`:

```text
.ai_paper_validation/
├── final_report_1_6_2.md
├── final_report_1_6_2.html
└── review_1_6_2/
    ├── routing_preflight.md
    ├── tooling_record.md
    ├── tooling/bootstrap_log.json (only when a fallback environment was created)
    ├── run_state.md
    ├── source_inventory.md
    ├── source_hashes_before.sha256
    ├── reused_artifact_hashes_before.sha256
    ├── evidence_asset_inventory.md
    ├── source_coverage.md
    ├── coverage_manifest.md
    ├── agent_execution_manifest.md
    ├── extraction/main_quantitative_evidence.md
    ├── extraction/support_quantitative_evidence.md
    ├── relationships/numeric_relationship_inventory.md
    ├── statistics/relationship_inventory.md
    ├── checkers/numeric_consistency.md
    ├── checkers/statistical_pass_1.md
    ├── checkers/cross_source_consistency.md
    ├── checkers/statistical_pass_2.md
    ├── screening/inclusion_screen.md
    ├── candidate_ledger.md
    ├── verification/evidence_recheck.md
    ├── quality/evidence_quality_audit.md
    ├── limitations.md
    └── review_validation.json
```

The interactive coordinator creates `routing_preflight.md` before scientific work. Its successful
first response is the real provider/authentication inference check. The artifact records
`Coordinator inference: PASS`, execution mode `INTERACTIVE_CLI`, `Provider: CURRENT_SESSION`, the run model and its source, the single-model role matrix, and verification that all ten named presets contain their
required model/effort pairs. It must not claim
PASS if a fixed model is rejected or the first mandatory specialist cannot obtain a model response.
Begin the artifact with these exact lines, replacing only the timestamp and, when the user selected
another model, every `gpt-6.1-sol` value with that exact ID and `Run model source` with `USER_SELECTED`. The run uses the provider of
the current Codex session and records it only as `CURRENT_SESSION`; never record a credential:

```markdown
# Workflow 1.6.2 Routing Preflight

- Status: PASS
- Provider: CURRENT_SESSION
- Run model: gpt-6.1-sol
- Run model source: DEFAULT
- Coordinator model: gpt-6.1-sol
- Coordinator reasoning effort: high
- Ordinary specialist model: gpt-6.1-sol
- Ordinary specialist reasoning effort: medium
- Statistical specialist model: gpt-6.1-sol
- Statistical specialist reasoning effort: high
- Screening, recheck, and audit specialist model: gpt-6.1-sol
- Screening, recheck, and audit specialist reasoning effort: high
- Fixed model matrix: PASS
- Named agent presets: PASS
- Named agent preset count: 10
- Mandatory specialist stages: 11
- Mandatory agent start contract: FRESH_DISTINCT
- Coordinator inference: PASS
- Execution mode: INTERACTIVE_CLI
- Launch command: codex --approve-for-me
- Checked UTC: YYYY-MM-DDTHH:MM:SSZ
```

Follow it with a table that verifies each named `qc162_*` preset against its required model and effort.

Stage-specific shard parts may live in `parts/` subdirectories. Every part must be listed in
`coverage_manifest.md` on its own row and merged without loss into the canonical artifact. The
`Artifact` cell always contains one plain relative path.

## Candidate identity

Use `## C001 — ...`, `## C002 — ...`, and so on in the candidate ledger, evidence recheck, quality
audit, and final report. These four ID sets must be identical. There is no review queue and no count
target. If complete coverage produces no candidates, all four files must explicitly state that the
stable candidate set is empty with the exact sentence `No stable candidates were identified` followed
by the scope statement.

Each final report card contains these exact bold labels:

- **Candidate statement:**
- **Review domain:**
- **Relationship type:**
- **All relationships:**
- **Compared document roles:**
- **Evidence state:**
- **Inclusion audit:**
- **Finding IDs:**
- **Qualifying route:**
- **Classification rationale:**
- **Classification ambiguity:**
- **Exact source locations:**
- **Source evidence:**
- **Reported-versus-comparator:**
- **Reasoning procedure:**
- **Calculation:**
- **Affected result or extracted value:**
- **Why context does not resolve it:**
- **Alternative source-grounded interpretations:**
- **Mechanical evidence recheck:**
- **Potential downstream evidence impact:**

The classification fields use the exact codes and values from the classification table in
`candidate_ledger.md` and the definitions in `QUALITY_CONTROL_SCOPE.md`:

```markdown
**Review domain:** statistical_results
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 2 vs REPORT main article Figure 2
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-NUM-001, F-ST1-002
**Classification rationale:** Both compared values are printed in the main article; no plan or supplement is a conflicting comparator.
**Classification ambiguity:** None
```

`Classification rationale` explains the role assignment and, for mixed candidates, the precedence
decision. `Classification ambiguity` is `None` or a bounded description of the uncertainty. When the
auditor questioned the inclusion, follow `**Inclusion audit:** QUESTIONED` on the next line with the
auditor's reason.

For a repeated pattern, `Exact source locations` lists every affected location with its own evidence
link. `Affected result or extracted value` names the specific result or value. `Why context does not
resolve it` states concretely why a statistically literate reader in the field could not identify the
intended value or meaning at once from the immediate context.

`Qualifying route` is `Route A, category N` (N = 1 to 5, as numbered in `QUALITY_CONTROL_SCOPE.md`)
or `Route B`. For route A, `Why context does not resolve it` names the category instead of a
context argument.

Cards contain no human verification steps and no human adjudication fields; human adjudication is
recorded later in the review workbook.

`Potential downstream evidence impact` must be bounded: identify what a systematic review,
meta-analysis, guideline, or data extractor could copy if the candidate is confirmed; do not claim
that propagation or conclusion change has occurred.

A very small P value displayed as `P = 0` or equivalent is never a candidate. If a card mentions a
display-zero P value because the same result has an independent supplied-source contradiction, add
this conditional field:

```markdown
**Independent contradiction beyond P=0 display:** Exact conflicting value, rule, and source location.
```

The field must identify the independent inconsistency; finite precision, underflow, and the claim that
an exact P value cannot mathematically be zero are not qualifying values.

Never describe a candidate, a value, or the authors' work with the words error, mistake, defect,
erroneous, wrong, or incorrect in any generated artifact. Established statistical and clinical terms
(standard error, type I or type II error, measurement error, sampling error, error bars, refractive
error, medication error, septal defect) are allowed. The
validator checks the report, ledger, recheck, audit, and screening log for these words outside quoted
source text.

## Final report order

1. Title framed as a quantitative quality-control consistency review.
2. Prominent `Pending Human Adjudication` notice.
3. Executive Quality-Control Summary with the actual candidate count and no severity language.
4. Package and Reused-Evidence Provenance.
5. Scope, Complete Coverage, and Exclusions.
6. Quantitative and Statistical Relationship Coverage, including both statistical passes.
7. Inclusion Screening Summary: the number of findings screened, the number included, and the number
   screened out by each reason code, reconciling to the screening log, with the inclusion threshold
   stated briefly.
8. Review-Domain Summary: counts of stable candidates by review domain, by relationship type, and by
   evidence state, each reconciling to the candidate count, with the four review domains defined
   briefly.
9. Candidate Index containing every stable ID with its review domain, relationship type, evidence
   state, and inclusion audit.
10. Candidate Evidence Cards containing every stable ID.
11. Downstream Evidence-Chain Considerations, stated generically and without assumed harm.
12. Limitations and Missing Definitions.
13. Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata, including target
    basis, source-unit counts, selected target, observed elapsed minutes, target status, bounded
    exceedance causes, and every agent with its model and reasoning effort.

Do not reproduce old AI dispositions or classifications, a ranked list, a severity ranking, a
suggested disposition, or a deferred-by-cap section. Do not list screened-out observations as cards;
the screening summary counts them.

## Evidence links

From a report stored directly in `.ai_paper_validation/`:

- source PDF: `[main.pdf — PDF p. 8](<../main.pdf#page=8>)`;
- reused rendered/OCR derivative: name it as provenance, then link the source PDF page as evidence;
- converted Office PDF inside this run: `[derived.pdf — PDF p. 3](<review_1_6_2/preprocessing/converted_pdf/derived.pdf#page=3>)`;
- workbook: link `../support.xlsx` and state worksheet plus exact cell/range;
- CSV: link `../support.csv` and state exact row/column or keyed record;
- DOC/DOCX without a derived PDF: link `../support.docx` and state stable paragraph/table IDs.

Every evidence-card PDF link ends in `#page=N`. Preserve complete actual filenames and stable document
IDs. Do not fabricate PDF pages for Office evidence.

## HTML

Render with:

```bash
python3 workflow_1_6_2/scripts/render_report.py \
  .ai_paper_validation/final_report_1_6_2.md \
  .ai_paper_validation/final_report_1_6_2.html \
  --profile 1.6.2
```

Use Pandoc when available and the dependency-free local fallback otherwise. HTML must be standalone
UTF-8 HTML5 with embedded CSS, a table of contents, responsive/print styling, stable candidate
anchors, and unchanged local relative links. It must load nothing from the web.
