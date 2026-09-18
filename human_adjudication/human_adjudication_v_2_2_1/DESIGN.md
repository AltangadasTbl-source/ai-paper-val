# Design and provenance — v.2.2.1

This release converts v.2.1.5.3 to a Markdown-only review package. Each year directory contains exactly one Markdown file for each paper. Year follows the frozen catalog, not the year embedded in a DOI.

## Changes from v.2.1.5.3

- Annual workbooks become individual paper files.
- Candidate identity, full source fields, evidence, links, and relation rows stay with each candidate.
- Primary and Checker / final columns preserve the two assessments in one record. Primary is the saved initial assessment after handoff.
- Initial domain choices are blank; AI suggested domains remain visible reference values for explicit human confirmation.
- Manual checklists replace formula validation, and manual candidate counts replace workbook summaries. No calculation or automatic blocking is implied.
- Protocol and plan descriptions stay in their candidate records: statement, relationship, final disposition, interpretation, inconsistency, notes, and discussion. There is no second editable result copy.
- All delivered files are Markdown. Reviewers need no scripts, dependencies, workbook, HTML application, or PDF guide. Original source documents remain linked.

## Source

Frozen source catalog: `human_adjudication/previous/human_adjudication_v_2_1_5_3/resources/source_catalog_v_2_1_5_3.xlsx`.

Source catalog SHA-256: `d663598f70f1a06f19baa64c6bcf999762fd67f44d47479de248f2ded18adbc5`.

Codebook and review logic: v.2.1.5.3 annual workbooks and maintenance/build.mjs. No v.2.1.5.4 or TEST human answers were imported. Existing versions and user edits remain untouched. The catalog contains 412 candidates, 1,624 evidence rows, 1,400 links, and 468 relation rows.

Original link destinations are preserved, with relative paths adjusted for the new year-directory depth. Original catalog paths remain verbatim as provenance. Candidates, source text, and scientific classifications have not been reassessed. Six candidates in jama.2019.14901 have no catalog evidence excerpts; each is explicitly marked and retains its source links.

## Frozen catalog manifest

| field | value |
| --- | --- |
| version | v.2.1.5.3 |
| schema | xlsx-adjudication-1 |
| stage | catalog |
| createdAt | 2026-09-13T00:38:29+00:00 |
| sourceSignature | 8d587aec1fb0cf06a9e1afdc45fef5a9c87a35785e6b71679cfea702de42afdd |
| legacy\_2018\_sha256 | 22a2c21c5cbf4fd341b77b2a98283439817fe12911a6d1033a82896b11219484 |
| legacy\_2019\_sha256 | 1063a3ff2b273dcb25e598a9ddd89a3c2fb49fdce23bb3ab41e45fe0ab91eee2 |
| legacy\_2024\_sha256 | 114330e1ad8af7ab5501bea7fb23a5d4cc3ec835d5509079cba9d946f08ace67 |
| legacy\_2025\_sha256 | 9e90b08e03b63cc6252a3e8765d852c25977a1d6d7eadc949cf65def6204b0db |
| provenance | v.2.0.1 -\> v.2.0.2 -\> v.2.0.3 -\> v.2.0.4; no v\_1\_0\_\* inputs |
| humanRecordsImported | none; bundled tester snapshot explicitly excluded |
| parentCatalogVersion | v.2.1.5.2 |
| parentCatalogSignature | 8d587aec1fb0cf06a9e1afdc45fef5a9c87a35785e6b71679cfea702de42afdd |
| suggestedDomainsRenamed | 0 |
| catalogChange | No source record changes; all worksheet, cell and workbook protection removed |

## Version and limits

Version: v.2.2.1. Schema: markdown-adjudication-1. All statuses and outcome counts are manually maintained. Markdown cannot enforce valid options, prevent edits to primary answers, or recalculate after changes. Preserve a primary backup or version-history reference. A paper is final only after all its candidates meet the documented readiness rules. Unfinished counts remain blank, never zero.

Do not use v_1_0_* builds as a methodological reference, codebook source, migration input, or provenance baseline. The valid historical design lineage remains v.2.0.1 → v.2.0.2 → v.2.0.3 → v.2.0.4.
