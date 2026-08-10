# AI Paper Validation Workflow

The root thread acts as the `Coordinator`. It owns article-package inventory, task routing,
candidate selection, and final consolidation. Child agents are read-only and must not edit files.

## Workflow

1. Confirm the complete article package: main article and all supplementary files.
2. Run `main_text_extractor`, `supplement_table_checker`, `figure_flow_checker`, and
   `statistical_consistency_checker` in parallel.
3. Deduplicate and prioritize the returned evidence. Send no more than 10 candidate issues per
   article package to `evidence_verifier`.
4. Send verified findings to `critic`. The critic may retain no more than 10 final issues.
5. Send accepted findings to `report_generator`.
6. Submit the report for `Human Adjudication`.

## Limits

- Maximum candidate issues per article package: 10.
- Maximum final issues per article package: 10.
- Maximum verification rounds per candidate: 2.
- The workflow ends after one verification stage and one critic stage.

## Evidence Standard

Each final issue requires an exact file, page, table or figure label when applicable, source values
or statements, a calculation or logical basis, and a concise verification instruction. The workflow
must classify unsupported findings as `Rejected` or `Uncertain`.

## Scope

Allowed issue categories are `Arithmetic inconsistency`, `Cross-document inconsistency`,
`Statistical reporting inconsistency`, `Participant flow inconsistency`, and `Presentation inconsistency`.

Do not assess research misconduct, raw-data validity, clinical appropriateness, general methodological
limitations, novelty, or information not contained in the article package. Do not use web search,
external retrieval, or unstated external knowledge.
