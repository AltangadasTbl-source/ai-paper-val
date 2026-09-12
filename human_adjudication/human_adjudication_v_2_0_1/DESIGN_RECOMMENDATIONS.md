# Human adjudication v.2.0.1: design recommendations

## Purpose

Version v.2.0.1 should treat the 412 AI outputs as candidate flags requiring human review. A reproduced discrepancy is not automatically an error. Only candidates assigned to the statistical-results domain receive an explicit statistical-error determination.

The interface should also preserve the distinction between independent first-stage review and later joint reconciliation. The current reviewers are still working independently, so v.2.0.1 records one reviewer's assessment per snapshot and does not present a field called “Joint decision.”

## Recommended decision structure

The previous single decision—retain as error, minor error, reject error, or discuss—combined several different judgments. Version v.2.0.1 separates them:

1. Can the reported flag be reproduced from the supplied sources?
2. What is the relevant review domain and document relationship?
3. Should the candidate flag be retained for later synthesis?
4. If it is statistical, does the reviewer consider it a confirmed or probable statistical reporting error?
5. If it is not statistical, what kind of inconsistency or discrepancy was observed, without automatically calling it an error?
6. Is it eligible for either prespecified temporal outcome?

## Review tracks

| Candidate type | Human determination | Terminology | Intended use |
|---|---|---|---|
| Statistical reporting candidate | Reproducibility, statistical error status, substantiveness, downstream impact | “Confirmed/probable statistical reporting error” is permitted | Primary temporal outcome |
| Internal nonstatistical candidate | Reproducibility and whether a substantive internal inconsistency exists | “Inconsistency” or “flag,” not automatically “error” | Secondary temporal outcome |
| Report/results supplement vs protocol/SAP (`P_R`) | Reproducibility, documentation, justification, and interpretation | “Protocol–report discrepancy” or “change”; not automatically “error” | Descriptive Results and supplementary table |
| Protocol/SAP internal (`P_P`) | Reproducibility and nature of the plan-material inconsistency | “Plan-material inconsistency” | Separate descriptive results |
| Protocol vs operational document (`P_O`) | Reproducibility and nature of the relationship | “Plan–operations discrepancy” | Separate descriptive results |
| Historical/background result inside protocol (`P_B`) | Reproducibility and nature of the background-data issue | “Background-data candidate” | Appendix or separate descriptive results |

For protocol reporting, the defensible wording is “no documentation located in the materials reviewed,” not an absolute assertion that the authors never documented the change.

## Reclassification context

The post-hoc reclassification in `meta_report/consistency_reclassification_2026-09-04` should be merged by the unique candidate key and displayed as read-only context. Its `primary`, `relations`, rationale, subtype, evidence state, ambiguity, protocol mechanism, and evidence paths are useful routing information, but they are not human adjudication results.

The mutually exclusive reclassification counts are:

| Relationship | Count |
|---|---:|
| `P_R` | 45 |
| `P_P` | 41 |
| `P_O` | 2 |
| `P_B` | 7 |
| `S_C` | 65 |
| `S_W` | 252 |

The main/non-plan-report primary subset is therefore 317 (`S_C + S_W`), not 287. Any use of the earlier 287-candidate preliminary subset should first be reconciled against the newer item-level coding.

## Temporal outcomes

V.2.0.1 should derive eligibility from completed review fields.

- Primary temporal outcome: a retained, reproduced or partly reproduced `S_C`/`S_W` candidate assigned to the statistical-results domain, judged a confirmed or probable statistical error, and judged substantive.
- Secondary temporal outcome: a retained, reproduced or partly reproduced `S_C`/`S_W` candidate assigned to the internal-nonstatistical domain and judged a substantive internal inconsistency.
- Protocol-related candidates are excluded from both temporal outcomes and retained for descriptive analyses.

The primary and secondary outcomes should be reported separately. Combining them would erase the distinction requested by the reviewers.

## Candidate granularity

Paper-level clustering alone does not resolve variation in how one underlying issue was divided into multiple candidate flags. The review therefore needs separate fields for exact duplicates and related issue clusters. Analyses can then include candidate-level counts and a cluster-level sensitivity analysis.

## Versioning and migration

V.2.0.1 must use a new browser-storage namespace and a new state schema. V1 decisions must not automatically populate v.2.0.1 fields because “accept/minor/reject” is not semantically equivalent to the new multidimensional review. If v1 data are consulted later, they should be retained as read-only legacy context during reconciliation.

