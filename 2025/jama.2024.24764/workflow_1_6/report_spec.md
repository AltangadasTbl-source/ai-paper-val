# Workflow 1.6 Artifact and Report Specification

## Canonical artifacts

Write new artifacts only below `.ai_paper_validation/review_1_6/`, except for the two versioned
reports stored directly below `.ai_paper_validation/`:

```text
.ai_paper_validation/
├── final_report_1_6.md
├── final_report_1_6.html
└── review_1_6/
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
    ├── candidate_ledger.md
    ├── verification/evidence_recheck.md
    ├── quality/evidence_quality_audit.md
    ├── limitations.md
    └── review_validation.json
```

The interactive coordinator creates `routing_preflight.md` before scientific work. Its successful
first response is the real provider/authentication inference check. The artifact records
`Coordinator inference: PASS`, execution mode `INTERACTIVE_CLI`, the fixed `gpt-6.1-sol` role matrix, and
verification that all nine named presets contain their required model/effort pairs. It must not claim
PASS if a fixed model is rejected or the first mandatory specialist cannot obtain a model response.
Begin the artifact with these exact lines, replacing only the timestamp:

```markdown
# Workflow 1.6 Routing Preflight

- Status: PASS
- Provider: openrouter
- Coordinator model: gpt-6.1-sol
- Coordinator reasoning effort: high
- Ordinary specialist model: gpt-6.1-sol
- Ordinary specialist reasoning effort: medium
- Statistical specialist model: gpt-6.1-sol
- Statistical specialist reasoning effort: high
- Recheck and audit specialist model: gpt-6.1-sol
- Recheck and audit specialist reasoning effort: high
- Fixed model matrix: PASS
- Named agent presets: PASS
- Named agent preset count: 9
- Mandatory specialist stages: 10
- Mandatory agent start contract: FRESH_DISTINCT
- Coordinator inference: PASS
- Execution mode: INTERACTIVE_CLI
- Launch command: codex --approve-for-me
- Checked UTC: YYYY-MM-DDTHH:MM:SSZ
```

Follow it with a table that verifies each named `qc16_*` preset against its required model and effort.

Stage-specific shard parts may live in `parts/` subdirectories. Every part must be listed in
`coverage_manifest.md` on its own row and merged without loss into the canonical artifact. The
`Artifact` cell always contains one plain relative path.

## Candidate identity

Use `## C001 — ...`, `## C002 — ...`, and so on in the candidate ledger, evidence recheck, quality
audit, and final report. These four ID sets must be identical. There is no review queue and no count
cap. If complete coverage produces no candidates, all four files must explicitly state that the stable
candidate set is empty.

Each final report card contains these exact bold labels:

- **Candidate statement:**
- **Category:**
- **Relationship type:**
- **All relationships:**
- **Compared document roles:**
- **Review domain:**
- **Evidence state:**
- **Suggested review disposition:**
- **Classification rationale:**
- **Classification ambiguity:**
- **Exact source locations:**
- **Source evidence:**
- **Reported-versus-comparator:**
- **Reasoning procedure:**
- **Calculation:**
- **Alternative source-grounded interpretations:**
- **Mechanical evidence recheck:**
- **Quality-control relevance:**
- **Potential downstream evidence impact:**
- **Human verification steps:**
- **Human adjudication fields:**

The classification fields use the exact codes and values from the classification table in
`candidate_ledger.md` and the definitions in `QUALITY_CONTROL_SCOPE.md`:

```markdown
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 2 vs REPORT main article abstract
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Both compared values are printed in the main article; no plan or supplement is a conflicting comparator.
**Classification ambiguity:** None
```

`Classification rationale` explains the role assignment and, for mixed candidates, the precedence
decision. `Classification ambiguity` is `None` or a bounded description of the uncertainty. The
suggested review disposition is a mechanical pre-fill for human review, not an adjudication.

The final field must use this exact mechanically verifiable blank template; do not substitute a dash,
empty checkbox, omitted value, or prose:

```markdown
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
```

`Potential downstream evidence impact` must be bounded: identify what a systematic review,
meta-analysis, guideline, or data extractor could copy if the candidate is confirmed; do not claim
that propagation or conclusion change has occurred.

Do not create a card for a coherent very small P value displayed as `P = 0` or equivalent. If a card
mentions a display-zero P value because the same result has an independent supplied-source
contradiction, add this conditional field:

```markdown
**Independent contradiction beyond P=0 display:** Exact conflicting value, rule, and source location.
```

The field must identify the independent mismatch; finite precision, underflow, and the claim that an
exact P value cannot mathematically be zero are not qualifying values.

## Final report order

1. Title framed as a quantitative quality-control consistency review.
2. Prominent `Pending Human Adjudication` notice.
3. Executive Quality-Control Summary with the actual candidate count and no severity language.
4. Package and Reused-Evidence Provenance.
5. Scope, Complete Coverage, and Exclusions.
6. Quantitative and Statistical Relationship Coverage, including both statistical passes.
7. Document-Role Classification Summary: counts of stable candidates by relationship type, by review
   domain, and by evidence state, each reconciling to the candidate count, with the four relationship
   definitions stated briefly.
8. Candidate Index containing every stable ID with its category, relationship type, review domain,
   and evidence state.
9. Candidate Evidence Cards containing every stable ID.
10. Downstream Evidence-Chain Considerations, stated generically and without assumed harm.
11. Limitations and Missing Definitions.
12. Human Adjudication Checklist.
13. Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata, including target
    basis, source-unit counts, selected target, observed elapsed minutes, target status, bounded
    exceedance causes, and every agent with its model and reasoning effort.

Do not reproduce old AI dispositions or classifications, a top-10 list, a severity ranking, or a
deferred-by-cap section.

## Evidence links

From a report stored directly in `.ai_paper_validation/`:

- source PDF: `[main.pdf — PDF p. 8](<../main.pdf#page=8>)`;
- reused rendered/OCR derivative: name it as provenance, then link the source PDF page as evidence;
- converted Office PDF inside this run: `[derived.pdf — PDF p. 3](<review_1_6/preprocessing/converted_pdf/derived.pdf#page=3>)`;
- workbook: link `../support.xlsx` and state worksheet plus exact cell/range;
- CSV: link `../support.csv` and state exact row/column or keyed record;
- DOC/DOCX without a derived PDF: link `../support.docx` and state stable paragraph/table IDs.

Every evidence-card PDF link ends in `#page=N`. Preserve complete actual filenames and stable document
IDs. Do not fabricate PDF pages for Office evidence.

## HTML

Render with:

```bash
python3 workflow_1_6/scripts/render_report.py \
  .ai_paper_validation/final_report_1_6.md \
  .ai_paper_validation/final_report_1_6.html \
  --profile 1.6
```

Use Pandoc when available and the dependency-free local fallback otherwise. HTML must be standalone
UTF-8 HTML5 with embedded CSS, a table of contents, responsive/print styling, stable candidate
anchors, and unchanged local relative links. It must load nothing from the web.
