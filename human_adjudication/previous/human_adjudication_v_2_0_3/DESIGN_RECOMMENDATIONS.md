# Human adjudication v.2.0.3: design decisions

## Decision basis

V.2.0.3 carries forward the adjudication design of v.2.0.2 and makes one classification change: the former `P_O` and `P_B` strata are consolidated into `P_P` because they contain only 2 and 7 candidates, respectively, and do not support useful separate analysis.

The inherited design integrates two sources of direction:

- The August 25 meeting proposed reciprocal year assignments: Bulun reviews 2019 and 2025, Shiyin reviews 2018 and 2024, and each person then checks the other's years.
- The September email discussion retained protocol–report discrepancies in the paper as descriptive findings, while narrowing the temporal comparison to substantive statistical reporting errors and internal inconsistencies in submitted reports and non-protocol supplements.

Given the available time, the implementation uses **primary review followed by a visible-answer check**. It is faster than two blinded independent reviews but must not be described as such.

## Three preserved record layers

Each completed checker snapshot contains three logically distinct layers:

1. **Primary assessment**: the first reviewer's completed structured record, locked during checking.
2. **Checker response**: agreement status, explanation, reviewer identity, and completion metadata.
3. **Proposed final assessment**: a copy of the primary assessment that the checker may clarify or revise without overwriting the original.

Unresolved disagreements require discussion. The resulting final assessment and comment should document what changed and why. This makes reconciliation auditable without requiring a separate merge script for ordinary use.

## Broad review and narrower temporal scope

The 412 AI outputs are candidate flags rather than established errors. A reproduced discrepancy is not automatically an error. All candidates remain available for descriptive characterization.

| Relationship | Count | Intended use |
|---|---:|---|
| `P_R` | 45 | Protocol–report descriptive results and supplementary table |
| `P_P` | 50 | Other plan-material descriptive results; includes the 2 former plan–operations and 7 former protocol-background candidates |
| `S_C` | 65 | Human-adjudicated temporal candidates when substantive |
| `S_W` | 252 | Human-adjudicated temporal candidates when substantive |

The current item-level non-protocol starting subset is therefore 317 (`S_C + S_W`), not the earlier preliminary count of 287. Human adjudication, duplicates, clusters, and scope decisions will determine the final analysis counts.

## Consolidated `P_P` logic

In v.2.0.3, `P_P` is the single relationship code for plan material that is not a current report/results-supplement versus protocol/SAP comparison. It includes:

- inconsistencies within a protocol/SAP or between plan versions;
- comparisons between protocol/SAP and a separate prospective operational manual; and
- historical or background results reproduced inside protocol/SAP material.

The last two groups were coded `P_O` and `P_B` in v.2.0.1/v.2.0.2. Their substantive distinctions may still be described in the candidate rationale, but they are no longer independent relationship categories, filters, review domains, or analysis strata. This consolidation is pragmatic rather than ontological: an operational manual and historical background data still play different documentary roles, but counts of 2 and 7 are too sparse to justify separate categories.

The consolidation prevents sparse labels from complicating tables and reviewer decisions while preserving the key scope boundary. All 50 `P_P` candidates remain plan-material descriptive findings and remain outside the temporal outcomes. `P_R` remains separate because current report-versus-plan discrepancies have a distinct interpretation and dedicated documentation/justification assessment.

## Review boundaries

- **Flag verification** records whether the stated discrepancy can be reproduced; it does not by itself call the finding an error.
- **Candidate disposition** records retention, exclusion, scope, or need for discussion separately from severity.
- **Statistical-results candidates** receive explicit error status, substantiveness, and downstream-impact judgments.
- **Internal nonstatistical candidates** are described as inconsistencies unless the evidence supports a more specific conclusion.
- **Protocol–report candidates** record documentation, justification, interpretation, and possible consequence. Use “no documentation located in the materials reviewed,” not an absolute claim that authors never documented a change.
- **Minor/presentation-only findings** remain recorded for descriptive reporting but do not enter the substantive temporal outcomes.
- **Exact duplicates** and **related clusters** are recorded separately because paper-level clustering alone does not correct candidate splitting.

`duplicateStatus` is candidate-register bookkeeping, separate from verification and disposition. An exact duplicate points to one canonical candidate so that the same underlying problem is counted once in a later independent-problem dataset. A related cluster links distinct candidates that may share one cause or correction. The browser preserves both for auditability and does not silently remove either or change its candidate-level derived label; deduplication or cluster collapse must be explicit in the analysis handoff.

V.2.0.3 does not read or extract any reclassification JSON. Its only candidate-data base is the frozen annual payload already embedded in the valid v.2.0.2 HTML files. During carry-forward, v.2.0.3 normalizes the inherited `P_O` and `P_B` values to `P_P` and retains the former labels only as non-analytic provenance. The inherited routing rationale, subtype, evidence state, ambiguity, mechanism, and evidence paths remain context rather than human-adjudication results.

## Derived analysis outcomes

V.2.0.3 derives outcomes only from a completed primary record or, once checking is complete, the checker-proposed final record.

- **Primary temporal outcome**: retained, reproduced or partly reproduced `S_C`/`S_W` candidate; statistical-results domain; confirmed or probable statistical error; substantive.
- **Secondary temporal outcome**: retained, reproduced or partly reproduced `S_C`/`S_W` candidate; internal-nonstatistical domain; substantive internal inconsistency.
- **Protocol descriptive outcome**: retained and reproduced or partly reproduced `P_R` candidate.

Primary and secondary temporal outcomes should be analyzed and reported separately. Protocol-related candidates are not temporal outcomes, but should be summarized by type, documentation, justification, and consequence.

## Statistical handoff

After adjudication, first report candidate- and paper-level descriptive summaries. For temporal comparisons, use paper as the clustering/resampling unit because flags within a paper are dependent. A practical sequence is:

1. inspect paper-level counts, zeros, dispersion, and the small number of papers per year;
2. fit a transparent count model only if its assumptions are defensible;
3. use a paper-cluster nonparametric bootstrap as a sensitivity analysis, resampling papers within year rather than individual flags; and
4. repeat key results after collapsing related candidate clusters and excluding exact duplicates.

The visible-answer checker design does not support a conventional blinded inter-rater reliability claim. Report check-status frequencies and disagreement resolution descriptively instead.

## Versioning

V.2.0.3 uses schema 6 and its own browser-storage namespace. Earlier snapshots are not migrated automatically because the relationship vocabulary changed and an earlier snapshot cannot safely imply a completed v.2.0.3 record.

The valid design baseline for this release is limited to human-adjudication v.2.0.1 and v.2.0.2. All `v_1_0_*` builds, including v1.0.2, v1.0.3, and v1.0.4, are failed construction versions and must be excluded from later methodological references, codebook inheritance, migration logic, and provenance claims. They may remain on disk only as historical artifacts. V.2.0.2 is the direct implementation base for v.2.0.3; v.2.0.1 is retained as the earlier valid provenance point.
