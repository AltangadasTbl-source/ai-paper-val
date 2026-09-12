# Using the v.2.0.2 two-stage human-adjudication files

## Purpose

V.2.0.2 implements the time-saving **primary review + visible-answer second-person check** workflow. It is not a blinded dual-independent-review system. The primary assessment, the checker's response, and the checker-proposed final assessment are stored separately so that the original judgment is never overwritten.

All 412 candidate flags remain available for broad descriptive review. Protocol-related candidates are retained for descriptive results and a supplementary table, but are excluded from the narrower temporal comparison. Temporal eligibility is derived only from completed human assessments of eligible non-protocol relationships.

## Reviewer assignments

Use stable reviewer IDs agreed by the team; the examples below do not prescribe the exact ID strings.

| Year | Candidates | Primary reviewer | Second-person checker |
|---|---:|---|---|
| 2018 | 119 | Shiyin | Bulun |
| 2019 | 71 | Bulun | Shiyin |
| 2024 | 91 | Shiyin | Bulun |
| 2025 | 131 | Bulun | Shiyin |

This reciprocal allocation implements the August 25 meeting proposal while avoiding a separate blinded second pass.

## Stage 1: primary review

1. Open the v.2.0.2 HTML for the assigned year.
2. Enter the primary reviewer's stable ID and optional display name, then select **Create / load primary reviewer**.
3. Verify the cited source material and record what was actually checked.
4. Complete the universal fields and the conditional module shown for the selected review domain.
5. Select **Mark primary review complete** for each candidate. The page lists any required fields that are missing.
6. Export a JSON snapshot regularly. Once every candidate is complete, send the final JSON to that year's checker.

The main fields separate reproducibility, dataset disposition, domain, duplicate/cluster status, evidence, and rationale. A reproduced discrepancy is not automatically an error. Use **Outside the prespecified review scope** only when a candidate does not belong in the agreed review scope; do not silently omit minor or protocol-related findings.

## Stage 2: visible-answer second-person check

1. Open the same year's v.2.0.2 HTML.
2. Enter the checker's stable ID and name. The checker ID must differ from the primary reviewer ID.
3. Select **Start checker stage from primary JSON** and choose the completed primary JSON.
4. Inspect the locked primary assessment and verify the evidence.
5. Choose one check result:
   - **Agree with primary assessment**: no change is needed.
   - **Agree with clarification**: the conclusion is retained, but the final structured record or explanation is clarified.
   - **Disagree**: edit the proposed final assessment to the checker's recommended resolution.
   - **Unable to resolve**: refer the candidate for discussion.
6. Add a checker comment for every clarification, disagreement, or unresolved case.
7. Select **Mark second-person check complete** and export the checker JSON.

The checker can edit the proposed final assessment, but the primary fields remain read-only and are preserved in the export. Loading a checker JSON with **Resume from v.2.0.2 snapshot** restores both stages.

## Reconciliation and final data

The completed checker JSON is the analysis-ready adjudication artifact because it contains:

- the immutable primary assessment;
- the check status and comment;
- the checker-proposed final structured assessment; and
- timestamps and reviewer identities for both stages.

Cases marked **Disagree** or **Unable to resolve** should be discussed by both reviewers. After discussion, the checker reopens the item if necessary, updates the proposed final assessment and comment to document the resolution, marks it complete again, and exports a new checker JSON. Keep the earlier export for provenance.

Because the checker sees the primary answers, agreement percentages describe verification workload and process consistency; they should not be presented as blinded inter-rater reliability or used as an unbiased estimate of independent agreement.

## Analysis labels and scope

The page derives labels; reviewers do not select them directly.

- **Primary temporal eligible**: completed, retained, reproduced or partly reproduced `S_C`/`S_W` candidate in the statistical-results domain, judged a confirmed or probable statistical reporting error and substantive.
- **Secondary temporal eligible**: completed, retained, reproduced or partly reproduced `S_C`/`S_W` candidate in the internal-nonstatistical domain, judged a substantive internal inconsistency.
- **Protocol descriptive**: completed, retained and reproduced or partly reproduced `P_R` candidate. These remain in descriptive results but not the temporal outcomes.
- Other plan-material relationships remain descriptive only.

The current reclassification has 317 `S_C`/`S_W` candidates. This replaces the earlier preliminary count of 287 as the auditable item-level starting subset; human adjudication still determines the final eligible counts.

## Saving, compatibility, and source links

Browser auto-save is only a convenience. Export JSON at session boundaries and retain files in a shared, backed-up location. CSV is useful for inspection; JSON is the authoritative exchange format. Annotated HTML is a portable visual copy.

V.2.0.1 snapshots use a different schema and are not imported automatically. Finish active v.2.0.1 work there or re-review it in v.2.0.2; do not relabel an old export as v.2.0.2.

The HTML files are intended to remain in `human_adjudication/human_adjudication_v_2_0_2/`. Their relative links point to source packages and validation records elsewhere in this repository.

## Rebuilding and validating

From the repository root, run:

```bash
python3 human_adjudication/human_adjudication_v_2_0_2/build_v_2_0_2.py
```

The builder checks all 412 unique keys, expected per-year and relationship counts, referenced report paths, local source links, embedded JSON, and required v.2.0.2 two-stage markers before writing `VALIDATION.md`.
