# Human adjudication v.2.0.2: design decisions

## Decision basis

V.2.0.2 integrates two sources of direction:

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
| `P_P` | 41 | Separate plan-material descriptive results |
| `P_O` | 2 | Separate plan–operations descriptive results |
| `P_B` | 7 | Background-data appendix/descriptive results |
| `S_C` | 65 | Human-adjudicated temporal candidates when substantive |
| `S_W` | 252 | Human-adjudicated temporal candidates when substantive |

The current item-level non-protocol starting subset is therefore 317 (`S_C + S_W`), not the earlier preliminary count of 287. Human adjudication, duplicates, clusters, and scope decisions will determine the final analysis counts.

## Review boundaries

- **Flag verification** records whether the stated discrepancy can be reproduced; it does not by itself call the finding an error.
- **Candidate disposition** records retention, exclusion, scope, or need for discussion separately from severity.
- **Statistical-results candidates** receive explicit error status, substantiveness, and downstream-impact judgments.
- **Internal nonstatistical candidates** are described as inconsistencies unless the evidence supports a more specific conclusion.
- **Protocol–report candidates** record documentation, justification, interpretation, and possible consequence. Use “no documentation located in the materials reviewed,” not an absolute claim that authors never documented a change.
- **Minor/presentation-only findings** remain recorded for descriptive reporting but do not enter the substantive temporal outcomes.
- **Exact duplicates** and **related clusters** are recorded separately because paper-level clustering alone does not correct candidate splitting.

The reclassification in `meta_report/consistency_reclassification_2026-09-04` is displayed as read-only routing context. Its relationship codes, rationale, subtype, evidence state, ambiguity, mechanism, and evidence paths are not human-adjudication results.

## Derived analysis outcomes

V.2.0.2 derives outcomes only from a completed primary record or, once checking is complete, the checker-proposed final record.

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

V.2.0.2 uses schema 5 and its own browser-storage namespace. V.2.0.1 snapshots are not migrated automatically because the older state contains only one independent-review layer and cannot safely imply a completed two-stage record. The archived v.2.0.1 files remain under `human_adjudication/previous/` for provenance.
