# Canonical Support Quantitative Evidence — DOC-002 and DOC-003

## Integration, scope, and no-applicable coverage

This is the canonical merge of all six current support mapper artifacts. It preserves every provisional mapper key, direct-source location, quantitative/statistical definition, table/figure occurrence, and no-applicable-page record from the parts named below. No candidate selection, diagnosis, or adjudication was performed.

| Source | PDF scope | Mapper artifact | Mapping status | Content status |
|---|---|---|---|---|
| DOC-002 | pp. 1-30 | `parts/mapping/support_DOC002_p001-p030.md` | COMPLETE, 30/30 fresh-required units | Protocol definitions, planned endpoints, schedules, eligibility, engagement, and operational quantities. |
| DOC-002 | pp. 31-60 | `parts/mapping/support_DOC002_p031-p060.md` | COMPLETE, 30/30 fresh-required units | Protocol/SAP thresholds, noninferiority/sample-size plan, models, missingness, and cost-effectiveness plan. |
| DOC-002 | pp. 61-90 | `parts/mapping/support_DOC002_p061-p090.md` | COMPLETE, 30/30 fresh-required units | Instrument formulas, units, thresholds, and collection definitions; no reported arm result. |
| DOC-003 | pp. 1-30 | `parts/mapping/support_DOC003_p001-p030.md` | COMPLETE, 30/30 fresh-required units | Measurement/method definitions and eTable/eFigure matching keys. |
| DOC-003 | pp. 31-60 | `parts/mapping/support_DOC003_p031-p060.md` | COMPLETE, 30/30 units (fresh pp. 31-33, 36-37; reusable pp. 34-35, 38-60) | eFigures, eTables 1-17, baseline, missingness, outcomes, and sensitivities. |
| DOC-003 | pp. 61-69 | `parts/mapping/support_DOC003_p061-p069.md` | COMPLETE, 9/9 units (reusable pp. 61-66; fresh pp. 67-69) | eTables 18-20d and references-only p. 69. |

All 159 support pages are explicitly covered. DOC-002 pp. 2-5, 11-12, 18-19, 21-27, 34, 40-60, 68-69, and 73-90 have explicit no-new-result/no-applicable records in their applicable mapper parts. DOC-003 pp. 1-6, 31-33, and 69 have explicit no-applicable records; pp. 32-33 are app screenshots and p. 69 references only.

## Numeric/reporting relationship crosswalk

| Global IDs | Provisional mapper keys | Direct-source location | Integrated content |
|---|---|---|---|
| N036-N049 | D2A-N001-D2A-N014 | DOC-002 pp. 1-30 | Protocol identity, planned total/allocation, endpoint/components, eligibility, schedule, incentives, engagement/completion, accrual, randomization, and exclusions. |
| N050-N058 | D2B-N001-D2B-N009 | DOC-002 pp. 31-39 | Rescue/withdrawal, planned CONSORT, measurement, safety reporting, noninferiority, sample size, models, missingness, and cost-effectiveness definitions. |
| N059-N065 | D2C-N01-D2C-N07 | DOC-002 pp. 61-72 | Questionnaire and WHO-5 formulas, NPS definition, local-DPP codes/units, health-use counts, COVID thresholds, and AE-collection rule. |
| N066-N090 | D3A-N001-D3A-N025 | DOC-003 pp. 7-30 | Endpoint rationale; A1C/accelerometry measurements; intervention exposure; cohort, outcome, eFigure/eTable, and sensitivity definitions. |
| N091-N111 | D3B-N01-D3B-N21 | DOC-003 pp. 34-60 | eFigures 3-4; version exposure; eTables 1-17 baseline, missingness, attendance, medications, outcomes, and sensitivities. |
| N112-N117 | D3C-N01-D3C-N06 | DOC-003 pp. 61-69 | eTables 18a-20d primary/cluster sensitivities and adverse-event quantities; references-only p. 69. |

## Statistical relationship crosswalk

| Global IDs | Provisional mapper keys | Direct-source location | Integrated content |
|---|---|---|---|
| S008 | D2A-S001 | DOC-002 pp. 6, 15-16 | Planned binary primary endpoint and noninferiority objective; later pages supply full inferential detail. |
| S009-S012 | D2B-S001-D2B-S004 | DOC-002 pp. 36-39 | Protocol noninferiority/sample-size relation, models/populations, missing-data rule, and cost-effectiveness specification. |
| S013-S019 | D3A-S001-D3A-S007 | DOC-003 pp. 8, 28-30 | Device threshold; eFigure 3/4 intervals; specified tests; MICE/Rubin rule. |
| S020-S032 | D3B-S01-D3B-S13 | DOC-003 pp. 34-60 | Age-adjusted and subgroup RDs; baseline/table P-value statements; attendance/medication tests; per-protocol and sensitivity one-sided bounds. |
| S033-S034 | D3C-S01-D3C-S02 | DOC-003 pp. 61-62 | One-sided best-case/all-attainment and cluster-robust confidence-bound reporting. |

## Detailed merged content and preservation rule

Every numeric value, formula, cached/displayed quantity (no Office source is supplied), table row, figure label, footnote, test/model label, sensitivity assumption, and exact no-applicable record remains in the six listed mapper artifacts. They are the component-level annexes of this canonical merge and are retained unchanged so that no flattened-table value or source-location provenance is lost. The global inventories `relationships/numeric_relationship_inventory.md` and `statistics/relationship_inventory.md` provide the stable, checker-ready identities and cross-source matching fields.

## Extraction limitations

DOC-002 native/layout text is glyph-encoded; current direct rendered pages were the transcription authority. DOC-003 fresh ranges used direct native/layout text and targeted rendering where table columns mattered; the p. 67 OCR output was unusable and was not relied on. These are derivative-extraction limitations only: all direct support units were mapped.
