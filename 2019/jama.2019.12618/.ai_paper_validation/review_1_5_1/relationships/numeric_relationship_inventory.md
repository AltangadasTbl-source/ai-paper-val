# Numeric/reporting relationship inventory

## Canonical identity rule

`N001`-`N039` are the complete main-article records in `extraction/main_quantitative_evidence.md`; their source pages, printed values, labels, populations, contrasts, and mapper provenance are retained there. The support records below are distinct source relationships, assigned globally unique continuation identifiers. A semicolon-separated local-key list is an exact one-to-one ordered crosswalk to consecutive IDs in the stated span; complete printed evidence remains in the named support shard and canonical support map.

| Global IDs | Source local keys, in order | Direct units / provenance | Relationship class and matching keys |
|---|---|---|---|
| N040-N062 | N-P001 through N-P023 | DOC-003 pp. 1-32; `parts/support_protocol_pp001_032.md` | Protocol background/planned N, eligibility, endpoint, safety, dose, prednisone, visit, laboratory, and QoL definitions; match keys retained verbatim. |
| N063-N099 | N-SP33-01, N-SP34-01, N-SP34-02, N-SP35-01, N-SP36-01, N-SP37-01, N-SP38-01, N-SP39-01, N-SP40-01, N-SP40-02, N-SP41-01, N-SP42-01, N-SP43-01, N-SP43-02, N-SP43-03, N-SP44-01, N-SP44-02, N-SP45-01, N-SP46-01, N-SP47-01, N-SP47-02, N-SP47-03, N-SP48-01, N-SP49-01, N-SP50-01, N-SP51-01, N-SP52-01, N-SP52-02, N-SP53-01, N-SP54-01, N-SP55-01, N-SP56-01, N-SP57-01, N-SP58-01, N-SP59-01, N-SP60-01, N-SP61-01 | DOC-003 pp. 33-64; `parts/support_protocol_pp033_064.md` | Measurement scales/units, grading thresholds, eye/patient definitions, safety thresholds, data/quality conventions, monitoring timing. |
| N100-N123 | N-P065-01 through N-P065-24 | DOC-003 pp. 65-96; `parts/support_protocol_pp065_096.md` | Protocol outcome, visit, withdrawal, randomization, and planned-analysis numeric definitions. |
| N124-N156 | Numeric relationship records in DOC-003 pp. 97-128, in source order | DOC-003 pp. 97-128; `parts/support_protocol_pp097_128.md` | Direct page-complete protocol measurement, scale, threshold, schedule, and data-quality definitions. |
| N157-N186 | N129-01, N129-02, N129-03, N130-01, N131-01, N131-02, N132-01, N133-01, N133-02, N134-01, N135-01, N135-02, N135-03, N136-01, N136-02, N137-01, N138-01, N139-01, N139-02, N140-01, N141-01, N142-01, N143-01, N145-01, N148-01, N149-01, N150-01, N151-01, N152-01, N153-01 | DOC-003 pp. 129-153; `parts/support_protocol_pp129_153.md` | Protocol scale/OCT/laboratory/safety/data/revision relationships. (The span reserves only source rows that are numeric/reporting records; statistical rows are in the S inventory.) |
| N187-N230 | SAP pp. 1-32 N001-N044, in order | DOC-004 pp. 1-32; `parts/support_sap_pp001_032.md` | SAP endpoint, analysis-population, coding, planned results, power, missingness, interim, and data-convention relationships. |
| N231-N249 | N-SAP33-001 through N-SAP33-019 | DOC-004 pp. 33-64; `parts/support_sap_pp033_064.md` | SAP planned statistical-output definitions and numeric assumptions. |
| N250-N274 | N-SAP065-01, N-SAP065-02, N-SAP065-03, N-SAP065-04, N-SAP065-05, N-SAP066-01, N-SAP066-02, N-SAP066-03, N-SAP067-01, N-SAP067-02, N-SAP067-03, N-SAP068-01, N-SAP068-02, N-SAP069-01, N-SAP069-02, N-SAP070-01, N-SAP071-01, N-SAP072-01, N-SAP073-01, N-SAP074-01, N-SAP075-01, N-SAP076-01, N-SAP079-01, N-SAP080-01, N-SAP081-01 | DOC-004 pp. 65-83; `parts/support_sap_pp065_083.md` | SAP planned endpoint, power, population, imputation, interim, rate/proportion, and administrative definitions. |
| N275-N280 | N-DOC002-001 through N-DOC002-006 | DOC-002 pp. 8,10-12,14-16; `parts/support_supp_results_pp001_016.md` | Enrollment and six-/12-month AE tables, with all 195 printed count/percentage cells, table labels, denominators, and footnotes. |
| N281 | N-DOC002-DRAFT-001 | DOC-002 p. 15; `parts/support_supp_results_pp001_016.md` | Source-grounded relationship: eTable 9 MMF N=20, serious diarrhea 1 (3.4), versus 1/20=5.0% to one decimal; pending independent checking, not a candidate/adjudication. |
| N282 | N-DOC002-DRAFT-002 | DOC-002 pp. 5,14; `parts/support_supp_results_pp001_016.md` | Source-grounded label relationship: serious ocular `>24mm Hg` versus eTable 1 serious surgery-required/non-serious >=24-mm-Hg definitions; pending independent checking, not a candidate/adjudication. |

## No-applicable support units

DOC-005 p. 1 has zero numeric/reporting relationships. Protocol and SAP bibliography, covers, and purely administrative pages are explicitly mapped as no-applicable in their listed shards; they do not receive N IDs. No supplied support workbook, CSV, formula cell, or cached workbook/display value exists.

## Scope limitation

The inventory is an evidence map, not an arithmetic or candidate disposition. Every range preserves ordered mapper provenance; no genuinely distinct source record was merged merely because it shares a topic or matching main-paper key.
