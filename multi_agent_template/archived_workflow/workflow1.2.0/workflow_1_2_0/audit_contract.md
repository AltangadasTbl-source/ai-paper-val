# Workflow 1.2.0 audit contract

## Evidence scope

Detect reporting inconsistencies reproducible from the supplied package. Cover all result-relevant
relationships in the main paper and support files: populations, arms, counts, exclusions, follow-up,
missingness, outcomes, time points, contrasts, numerators, denominators, percentages, estimates,
intervals, P values, test statistics, standard errors, subgroup labels, units, table headers,
footnotes, figures, captions, axes, and narrative claims.

Protocol, SAP, administrative, author-list, rights, and data-sharing material is not a default
scientific target. Open it only for a concrete relationship already identified in the result record.
The separate content-use restriction screen still covers every supplied source at document level.

## Source formats and citation truth

- **PDF:** native text first; render/OCR only selected pages. Final evidence links end in `#page=N`.
- **DOCX:** prefer a locally converted derived PDF. If conversion is unavailable, use the original
  DOCX and the locally extracted stable paragraph (`P####`) or table/cell (`T### R### C###`) IDs.
- **XLSX/XLS:** cite the actual workbook, exact worksheet, and cell/range. Use extracted formula and
  cached/displayed values as separate fields. Do not claim that a cached formula result was freshly
  recalculated unless it was.
- **CSV:** cite the actual file and exact row/column or keyed record.

Never fabricate PDF pagination for an Office source. Never silently normalize suspicious values.

## Candidate lifecycle

1. Checkers emit every distinct candidate without a count limit.
2. Merge genuine duplicates before IDs and preserve all checker/source provenance.
3. Assign stable IDs `C001`, `C002`, ... once.
4. Mechanical recheck returns each ID and factual fields; no disposition.
5. The second statistics pass may append IDs, never renumber old IDs; recheck appended IDs.
6. Quality audit returns every ID and repairs card completeness without deletion.
7. Queue routing selects at most 10 for current human review. The ledger remains complete.

For every candidate, record: source location found; source value matched; comparator matched;
calculation reproducible; inputs available; source-grounded alternative; observed discrepancy
independent of proposed mechanism; exact missing evidence; exact human question; queue routing.

## Queue policy

Historical/significance/severity labels are not ranking inputs. Rank by this tuple, highest first:

1. both compared locations found;
2. printed comparison/calculation reproducible;
3. necessary inputs available;
4. discrepancy observable independently of an inferred mechanism;
5. cross-location/document corroboration;
6. fewer incomplete evidence-card fields;
7. natural stable-ID order.

Nonqueued IDs retain one routing reason: `GENUINE_DUPLICATE_RELATIONSHIP`,
`OUTSIDE_ALLOWED_TAXONOMY`, `SOURCE_LOCATION_NOT_RECOVERABLE`, or `DEFERRED_BY_REVIEW_CAP`. These are
workflow routes, not validity decisions.

## Statistical coverage

Create one stable relationship ID per outcome/population/time/contrast/model/location combination.
First-pass checks cover ordering/containment, sign/direction, explicitly compatible interval/P-value
relationships, repetitions, cross-location agreement, determinable count/effect direction, reported
SE/test/P formulas, denominators/populations, notation/scale, and narrative claims.

Never assume an interval and P value share a test or infer unreported sidedness, degrees of freedom,
variance estimator, covariance, multiplicity, denominator, or estimand mapping. Label approximations.

The second pass revisits every relationship using the complete cross-lane ledger and recheck facts.
Each relationship in `statistics/coverage_matrix.json` must have both `pass_1 = COMPLETE` and
`pass_2 = COMPLETE`, or the validator fails.

## Coverage manifest

`.ai_paper_validation/coverage_manifest.json` is authoritative for execution completeness. Each stage
has unique `expected_units`, unique `completed_units`, and one or more relative nonempty `artifacts`.
Expected and completed sets must be equal. Source/page/sheet/paragraph/relationship/candidate units are
stable strings; a unit belongs exactly once to each applicable stage.

Use this shape (extend the arrays; do not rename stages):

```json
{
  "schema_version": 1,
  "stages": {
    "source_inventory": {
      "expected_units": ["DOC001", "DOC002"],
      "completed_units": ["DOC001", "DOC002"],
      "artifacts": ["package_manifest.md"]
    },
    "statistics_pass_1": {
      "expected_units": ["S001"],
      "completed_units": ["S001"],
      "artifacts": ["checkers/statistical_pass_1.md", "statistics/coverage_matrix.json"]
    }
  }
}
```

Required stage keys are `source_inventory`, `rights_screen`, `preprocessing`, `main_extraction`,
`support_extraction`, `table_arithmetic`, `figure_flow`, `statistics_pass_1`, `evidence_recheck`,
`statistics_pass_2`, `evidence_quality`, `queue_selection`, and `report_generation`. The first three
use every DOC ID. Both statistics stages use every S ID. Recheck, quality, and queue selection use
every C ID; report generation uses exactly the queued C IDs. An applicable stage with no units keeps
empty expected/completed arrays but still has a nonempty not-applicable artifact.

`statistics/coverage_matrix.json` uses:

```json
{
  "schema_version": 1,
  "relationships": [
    {
      "id": "S001",
      "outcome_population_time_contrast_model_location": "complete identifying text",
      "pass_1": "COMPLETE",
      "pass_2": "COMPLETE",
      "checks": [],
      "missing_inputs": [],
      "candidate_ids": []
    }
  ]
}
```

## Rights-language screen

For every direct source, retain one status: `Explicit AI Training Restriction`,
`Conditional / Permission Required`, `No AI Training Restriction Located in Provided Materials`, or
`Not Stated / Undetermined`, with exact local location and language when present. The screen is not a
legal opinion, not a scientific candidate, and not authorization for processing.
