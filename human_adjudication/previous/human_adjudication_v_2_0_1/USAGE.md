# Using the v.2.0.1 independent-review HTML files

## What this version does

V.2.0.1 supports the first, independent stage of human review. Each snapshot belongs to one reviewer. It does not combine two reviewers' answers or create a final joint adjudication.

The four HTML files are self-contained and cover the 2018, 2019, 2024, and 2025 candidate sets. They display the original candidate record together with read-only document-role coding from `meta_report/consistency_reclassification_2026-09-04`.

## Recommended workflow

1. Open the HTML for the year being reviewed.
2. Enter a stable reviewer ID, such as initials, and optionally a display name. Select **Create / load reviewer**.
3. Review the cited source material. Record what was actually checked rather than relying only on the AI summary.
4. Complete the universal fields: flag verification, candidate disposition, review domain, duplicate/cluster information, evidence checked, and rationale.
5. Complete the conditional module shown for the selected domain:
   - Statistical-results candidates receive statistical error, substantiveness, and downstream-impact fields.
   - Protocol–report candidates receive documentation, justification, interpretation, and consequence fields.
   - Other candidates receive a non-error inconsistency assessment and consequence field.
6. Select **Mark independent review complete**. The HTML will list any required fields that remain incomplete.
7. Frequently download a JSON snapshot. At the end of a session, also download an annotated HTML if a portable copy is useful.

## Independent reviewers

Each reviewer must use a different reviewer ID. A reviewer should not import the other reviewer's snapshot during independent review. Separate IDs use separate browser-storage records even when the same browser is used.

After both reviewers finish, their JSON snapshots can be compared in a later reconciliation stage. V.2.0.1 deliberately does not show another reviewer's answers.

## Meaning of the main fields

- **Flag verification** asks only whether the stated discrepancy can be reproduced.
- **Candidate disposition** determines whether the flag should remain in the review dataset, be excluded as unsupported, or receive discussion.
- **Review domain** controls which assessment module appears. The initial value is a routing suggestion, not a conclusion.
- **Statistical error status** appears only in the statistical-results module.
- **Protocol documentation** records what was located in the reviewed materials. “No documentation located” is not a claim about materials that were unavailable.
- **Related cluster ID** groups distinct flags that may arise from one underlying reporting mechanism. Use the same locally agreed identifier for all related flags.
- **Exact duplicate** should be used only when two candidate IDs represent the same underlying discrepancy, not merely related rows or outcomes.

## Derived temporal-analysis labels

The interface derives these labels; reviewers do not select them directly.

- **Primary temporal eligible** requires `S_C` or `S_W`, a completed retained and reproduced/partly reproduced review, statistical-results domain, confirmed/probable statistical error, and substantive status.
- **Secondary temporal eligible** requires `S_C` or `S_W`, a completed retained and reproduced/partly reproduced review, internal-nonstatistical domain, and substantive internal inconsistency.
- `P_R` candidates are shown as protocol–report descriptive candidates after reproduction and retention.
- Other plan-material relationships are descriptive only.

## Saving and exchanging work

Browser auto-save is a convenience, not the archival record. Browser handling of storage for local `file://` pages varies. Use **Export reviewer snapshot (JSON)** regularly.

The annotated HTML contains the active reviewer's state. The JSON snapshot is preferable for comparison and later reconciliation. CSV is intended for tabular inspection and analysis.

V1 snapshots are not accepted by this interface and are not migrated automatically. Preserve v1 exports separately.

## Source links

The archived v.2.0.1 files are stored three directory levels below the repository root. Their links are generated for this archived location and point back into the paper packages and validation records in this repository. If the HTML files are moved elsewhere, source links may need to be rebuilt.

## Rebuilding and validating

From the repository root, run:

```bash
python3 human_adjudication/previous/human_adjudication_v_2_0_1/build_v_2_0_1.py
```

The builder verifies all 412 unique keys, expected per-year counts, document-relationship totals, referenced report paths, embedded JSON, and required v.2.0.1 markers before writing `VALIDATION.md`.
