# Audit protocol

## Purpose

Detect reporting inconsistencies that a human can reproduce from the supplied paper package. Produce candidates for human adjudication, not AI verdicts.

## Scope

Allowed candidate categories are:

- `Arithmetic inconsistency`
- `Cross-document inconsistency`
- `Statistical reporting inconsistency`
- `Participant flow inconsistency`
- `Presentation inconsistency`

Do not assess misconduct, raw-data validity, clinical appropriateness, novelty, causal truth, or general methodological limitations. A failure to reproduce a displayed value is a candidate only when the source supplies the required inputs and reconciliation rule. Otherwise, state the missing input as a human-review question.

## Package and document records

Inventory direct PDF/DOC/DOCX sources in the current paper directory and converted Office supplements under `audit/preprocessing/converted_pdf/`. Ignore parent and sibling directories. For every document retain:

- stable document ID and actual filename;
- source or derived-conversion status;
- SHA-256 from the batch run metadata when available;
- page count, native-text status, selected audit pages, and extraction method per page;
- main article, results supplement, protocol/SAP, administrative, or unknown classification;
- processing status and explicit reason for any page or document not audited.

Main-article results pages and result-relevant supplement pages are default audit targets. Protocol, SAP, author-list, administrative, and data-sharing sections are opened only for a concrete comparison requested by the coordinator. Do not use silence in excluded pages as evidence.

## Evidence extraction

Build a location-preserving map of every reported result needed for checking:

- populations, arms, randomized/analyzed counts, exclusions, follow-up, and missingness;
- every outcome/time point/comparison displayed in the abstract, main results, tables, figures, and result supplements;
- numerator, denominator, percentage, count, total, mean, median, dispersion, effect estimate, confidence interval, P value, test statistic, and subgroup label;
- table headers, spanners, footnotes, units, legends, axes, and analysis-population definitions;
- workbook-like evidence only after it has been converted or rendered to a PDF source view.

Never silently normalize a suspicious value. Preserve the printed representation and units.

## Candidate discovery

Check all result-relevant evidence; do not stop after finding several issues. Each checker emits an unbounded list. Merge candidates only when they describe the same inconsistency using the same underlying values. A merged candidate retains all original locations and checker provenance.

Candidate IDs are assigned only after the first merge. When the statistical second pass adds candidates, append new IDs without renumbering earlier candidates.

## Context-safe coverage

Complete evidence belongs in durable files, not only in agent messages. Use
`audit/context_coverage.md` to record each stage, shard ID, exact assigned source pages or candidate
IDs, output path, and completion status. If a role is sharded, every part must have a disjoint scope and
a unique path; merge all parts into the canonical artifact before the next dependent stage.

The configured shard thresholds are workload boundaries for one specialist call. They do not permit
sampling, stopping early, dropping a candidate, or leaving a result-relevant page uncovered. A
compacted or restarted coordinator must reload the recorded artifacts and continue from the first
incomplete coverage row.

## Mechanical evidence recheck

For every candidate, reopen the original or converted PDF pages and record these separate facts:

- cited location found: yes/no;
- reported source text/value matches the card: yes/no;
- comparator text/value matches the card: yes/no/not applicable;
- displayed calculation reproducible: yes/no/not applicable;
- necessary inputs available: yes/no, with missing inputs named;
- alternative source-grounded interpretation present: yes/no, with the exact evidence;
- exact human question that remains.

These fields are not a `Verified`, `Rejected`, or `Uncertain` disposition. Never delete a candidate because one field is `no`.

## Evidence-quality audit

The quality auditor checks completeness and overclaiming. It must return every candidate ID with:

- missing evidence-card fields;
- unsupported assumptions or inferred mechanisms;
- incorrect or non-reproducible arithmetic;
- duplicate relationships;
- source-link or page-number defects;
- required repair action or human question.

It cannot assign severity, decide scientific validity, suppress candidates, or merge stable candidate IDs. It may flag a possible duplicate relationship for human review, but every assigned ID remains in the registry and final report.

## Human boundary

Use neutral wording such as “candidate inconsistency,” “the displayed values do not reconcile under the stated rule,” and “requires human adjudication.” Leave validity, importance, severity, and correction decisions to the human reviewer.
