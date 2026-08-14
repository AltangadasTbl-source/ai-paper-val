# Workflow 1.2.1 recovery contract

## Purpose and non-goals

Patch an existing workflow-1.0 paper package without repeating the original audit. The durable 1.0
artifacts are an evidence cache and provenance record, not disposable intermediate files. Recovery
must exploit them before touching the source PDFs again.

This patch does not claim exhaustive discovery beyond what the legacy run inspected. It recovers and
rechecks what the legacy records contain, including records suppressed between checker, verifier,
critic, and report stages. It may follow a recovered discrepancy to its directly implicated source
location, but it must not start a new page-by-page search for unrelated findings.

## The 1.0 contradiction

The contradiction is structural rather than merely terminological:

- The evidence standard requires unsupported findings to be labelled `Rejected` or `Uncertain`.
- The workflow then says to send “verified findings” to the critic and “accepted findings” to the
  report generator.
- The critic itself may retain `Uncertain` findings, but the report generator receives only accepted
  findings and describes its input as accepted findings.
- Therefore uncertainty about an explanation, test definition, or mechanism can be mistaken for
  absence of a directly printed discrepancy and can remove the record from the final report.
- The global top-10 candidate limit is applied before verification, while individual checkers may each
  return up to 10. Candidate prioritization can therefore hide records even though their raw checker
  evidence remains on disk.
- The later endetail prompt cannot repair the second loss because it forbids new findings outside the
  already approved C01-C10 set.

Patch 1.2.1 repairs this by separating four layers:

1. **Raw legacy record:** immutable historical output and labels.
2. **Recovered candidate ledger:** every distinct candidate-like record, with no count limit.
3. **Mechanical recheck:** factual source-location and calculation fields, with no AI disposition.
4. **Human review queue:** at most 10 evidence cards selected for review efficiency.

The number 10 limits only layer 4.

## Legacy artifact precedence

Use this order to minimize repeated work:

1. Package manifest and document-ID mapping.
2. Page manifests, normalized native text, OCR text, and rendered pages.
3. Main/supplement extraction maps and document-level agent records.
4. Checker outputs and `candidate_set.md`.
5. Evidence-verifier and critic outputs.
6. Original concise `final_report.md` and HTML, if present.
7. Exact original PDF/workbook location for final confirmation.

Derived text is a locator and transcription aid. The source PDF/workbook remains the final evidence.
Do not discard a legacy record when an OCR transcription differs; record the discrepancy and inspect
the exact rendered/source page.

Use truthful format-specific locations: PDF `#page=N`; workbook worksheet plus exact cells; CSV row
and column; DOC/DOCX paragraph/table identifier or a locally derived PDF page. Never fabricate PDF
pagination for Office evidence. Any targeted Office extraction belongs under
`patch_1_2_1/targeted_preprocessing/`.

## Candidate identity and lineage

- Preserve an existing C identifier whenever it unambiguously refers to one relationship.
- Assign `R001`, `R002`, ... in deterministic artifact-path and appearance order to distinct records
  that never received a stable C identifier.
- Merge only the same underlying source values/statement and comparator. Similar topics, neighboring
  rows, shared causes, or repeated consequences are not enough to merge.
- A merge retains every artifact path, original wording, old label, checker lane, and source location.
- Once written to the recovered ledger, an ID is never deleted or renumbered.
- Old labels are stored only in `lineage_map.md` under `Historical pipeline label (non-authoritative)`.

## Mechanical recheck fields

For every recovered ID record separately:

- cited location found: yes/no;
- source printed value/text matched: yes/no;
- comparator printed value/text matched: yes/no/not applicable;
- displayed calculation or logical comparison reproduced: yes/no/not applicable;
- necessary inputs supplied by the package: yes/no, naming missing inputs;
- source-grounded alternative interpretation: yes/no, with location;
- observed discrepancy independent of proposed explanation: yes/no;
- exact remaining human question.

These fields must never be collapsed into `Verified`, `Rejected`, or `Uncertain`.

## Deterministic review-queue policy

Construct a queue of at most 10 after rechecking. Historical AI labels and severity are forbidden
ranking inputs. Rank eligible candidates by the following tuple, highest first:

1. both source and comparator locations found;
2. printed calculation/comparison reproducible;
3. necessary inputs available;
4. discrepancy observable independently of its proposed mechanism;
5. cross-location or cross-document corroboration present;
6. fewer unresolved evidence-card fields;
7. existing stable C identifier before recovered R identifier;
8. natural identifier order.

A candidate with a confirmed printed mismatch may remain eligible when a model definition or proposed
explanation is missing. Phrase the missing element as a human question. This is the principal recovery
path for legacy `Uncertain` records.

Every nonqueued ledger entry receives exactly one structural queue status:

- `GENUINE_DUPLICATE_BEFORE_FREEZE` with the retained ID;
- `OUTSIDE_ALLOWED_TAXONOMY`;
- `SOURCE_LOCATION_NOT_RECOVERABLE`;
- `DEFERRED_BY_REVIEW_CAP`;
- `CONTEXT_ONLY_NOT_A_CANDIDATE` (raw lineage entry only).

These are routing reasons, not scientific dispositions. `DEFERRED_BY_REVIEW_CAP` records remain
available for a later human-requested queue.

## CPU-only and targeted preprocessing

The Linux target has no GPU. Never call `nvidia-smi`, CUDA, or a GPU OCR provider. Reuse legacy OCR
before attempting new OCR. If one exact page requires new work, prefer native `pdftotext`, then render
that page only, then use the configured CPU OCR backend. Put any new derivative under
`patch_1_2_1/targeted_preprocessing/` with source filename, PDF page, command/backend, and timestamp.
If the CPU backend is absent or fails, record the page as unresolved and continue without asking the
user or switching to GPU.

## Autonomy

Do not ask the user whether to execute, continue, enable parallelism, use tools, choose a queue item,
or apply a safe repair. Make deterministic, reversible choices under this contract. A hard failure is
recorded in `recovery_log.md`; all independent work still proceeds.
