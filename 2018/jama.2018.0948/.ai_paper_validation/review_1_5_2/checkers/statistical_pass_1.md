# Statistical Consistency Review — Pass 1

## Independent review scope

- **Reviewer runtime agent ID:** `/root/statistics_pass_1`.
- **Required configuration:** fresh `gpt-5.6-terra` agent at `high` reasoning effort.
- **Relationship inventory reviewed:** `statistics/relationship_inventory.md`, including `statistics/parts/main_statistical_relationships.md` and `statistics/parts/support_statistical_relationships.md`.
- **Fresh mapping artifacts reviewed:** `extraction/main_quantitative_evidence.md`, `extraction/support_quantitative_evidence.md`, `relationships/numeric_relationship_inventory.md`, and `preprocessing/tool_and_page_status.md`.
- **Assigned direct-source scope:** DOC-001 PDF pp. 1-11; DOC-002 PDF pp. 1-37; DOC-003 PDF pp. 1-7; DOC-004 PDF pp. 1-14 (69 page units total).

## Relationship coverage

The canonical inferential-statistical inventory contains **0 `S` relationships**. Each of the 69 page units has a fresh structural page record, but no page has fresh native text, layout text, rendered image, or OCR text. Thus no estimate, interval, P value, test statistic, standard error, confidence level, model/adjustment definition, population, time point, contrast, reference group, scale, direction, table/figure/caption, or statistical footnote is source-accessible.

**Pass-1 status:** `PASS_1_COMPLETE` for the complete empty `S` set (0/0). This status documents completion of the assigned review procedure; it does not assert that the supplied PDFs contain no inferential results and it is not a finding that any result passes statistical reconciliation.

## Required check-family disposition

| Required statistical check family | Disposition | Exact basis |
|---|---|---|
| Point-estimate containment | NOT MECHANICALLY APPLICABLE | No source-accessible point estimate or interval. |
| Interval endpoint ordering | NOT MECHANICALLY APPLICABLE | No source-accessible interval endpoints. |
| Sign/direction agreement | NOT MECHANICALLY APPLICABLE | No source-accessible estimate, direction, event definition, label, narrative, or figure. |
| Effect-measure and scale labels | NOT MECHANICALLY APPLICABLE | No source-accessible effect measure, transform, unit, scale, reference group, or label. |
| Cross-location repetitions | NOT MECHANICALLY APPLICABLE | No source-accessible result occurrence, table, caption, narrative, abstract display, or support result that can be matched by population, time point, contrast, and model. |
| Interval/P-value/test/statistic/SE compatibility | NOT MECHANICALLY APPLICABLE | No source-accessible inferential values or definitions of test, sidedness, confidence level, model, variance estimator, multiplicity adjustment, denominator, or estimand mapping. No diagnostic approximation was attempted. |
| Denominator, arithmetic, population, duplicate-value, label/scale, rate/count, figure, and cross-source implications | NOT MECHANICALLY APPLICABLE | These pass-1 cross-lane checks require an `S` record and readable source content; neither exists in the fresh evidence assets. |

## P-value display-zero rule

No P-value display is source-accessible. Accordingly, no relationship can be marked `DISPLAY_ZERO_NOT_CANDIDATE`, and no candidate was generated from display-zero notation. The `P = 0` / `p = 0.000` exclusion was observed: finite-precision display-zero notation would not itself qualify as a candidate absent an independently supplied contradiction.

## Candidate output

**Pass-1 candidates emitted:** 0.

No `C` ID is proposed. The absence of a proposed candidate follows from the absence of source-readable statistical values and comparators, not from an inference that the paper has no results or no possible reporting inconsistency. A future review with fresh readable assets would need to register and review all resulting `S` relationships before source-grounded statistical reconciliation is possible.

## Limitation

The local fresh-preprocessing record reports unavailable `pdftotext`, `pdftotext -layout`, `pdftoppm`/`pdftocairo`, and `tesseract` for every direct PDF page. Structural page counts support complete page-unit scope coverage only; they cannot disclose scientific content or support statistical inference.
