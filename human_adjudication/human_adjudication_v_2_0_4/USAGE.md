# Using the v.2.0.4 two-stage human-adjudication files

## Purpose

V.2.0.4 is an exploratory primary-review plus visible-answer second-person-check workflow. It preserves the primary assessment, checker response, and checker-proposed final assessment separately. The HTML reminds users that practitioners remain responsible for interpretation and use.

The 412 candidate flags and relationship counts are unchanged from v.2.0.3: `P_R=45`, `P_P=50`, `S_C=65`, and `S_W=252`. The former `P_O` and `P_B` labels remain consolidated within `P_P`.

## What changed

The form no longer asks for flag verification, duplicate status, an exact-duplicate key, potential consequence, evidence personally checked, or primary assessment rationale. Reproduction checking and duplicate resolution belong to the earlier final-report construction stage and are not repeated here.

The statistical module still includes **Potential downstream impact**. This is a domain-specific interpretation field and is distinct from the deleted general **Potential consequence** field.

Review-domain labels show the corresponding relationship symbols used by the coding scheme:

| Relationship | AI starting review domain |
|---|---|
| `S_C`, `S_W` | Statistical results (`S_C / S_W`) or internal nonstatistical (`S_C / S_W`) |
| `P_R` | Protocol-report (`P_R`) |
| `P_P` | Plan material (`P_P`) |

These are starting mappings, not locked choices. Every candidate's Review domain menu contains all four labeled domains, and the reviewer may change the AI value.

## AI starting values

Each HTML contains editable AI starting values derived from the current meta-report results. Candidate membership still comes exclusively from the frozen v.2.0.3 annual HTML payloads. The meta-report JSON initializes relationship-consistent domain and candidate disposition; it is not a candidate source. Prior `recorded_candidate` and `repaired_residual` results start as `Retain`, `not_reproduced` starts as `Do not retain`, and `record_input_error` starts as `Needs discussion`. This carries forward the prior AI result without asking the human reviewer to repeat a reproduction check.

The same initial values are written as `ai_initial_state_v_2_0_4_YEAR.json` files beside the HTML. When a reviewer creates a new primary record, the HTML shows these starting values in the form. They remain editable and do not count as a completed human assessment.

The single **Import / resume v.2.0.4 JSON** action recognizes all supported files:

- For an `ai_initial_state` JSON, first enter the human reviewer ID; importing creates an incomplete editable primary record under that ID.
- For a primary snapshot, leaving the ID blank or using the primary reviewer's ID resumes primary review. Entering a different ID starts checker stage when the primary snapshot is complete.
- For a checker snapshot, importing resumes that checker record.

## Stage 1: primary review

1. Open the HTML for the assigned year.
2. Enter a stable reviewer ID and optional display name, then select **Create / load primary reviewer**.
3. Review the candidate evidence, AI starting disposition, and editable review domain.
4. Complete the conditional module when retaining a candidate. A `Needs discussion`, `Do not retain`, or out-of-scope item requires only its disposition and valid domain.
5. Select **Mark primary review complete** for each candidate.
6. Export the JSON snapshot regularly. Send the completed annual JSON to the checker.

The optional related-cluster field groups distinct, related findings. It does not perform deduplication.

## Stage 2: visible-answer check

1. Open the same year's v.2.0.4 HTML.
2. Enter a checker ID different from the primary reviewer ID.
3. Select **Import / resume v.2.0.4 JSON** and choose a complete primary snapshot. Because the entered ID differs from the primary reviewer ID, the page enters checker stage automatically.
4. Review the locked primary assessment.
5. Record agreement, clarification, disagreement, or inability to resolve. A non-agreement result requires a checker comment.
6. Edit the proposed final assessment when needed, mark the check complete, and export the checker JSON.

Unresolved items can be discussed outside the page and then updated in the proposed final assessment. The primary record is retained unchanged.

## 2018 secondary-stage test

Use `secondary_stage_test_primary_v_2_0_4_2018_all_needs_discussion.json` with the 2018 HTML. It is a complete primary snapshot with reviewer ID `tester`, reviewer name `Workflow Tester`, and all 119 dispositions set to `Needs discussion`.

1. Open `candidate_flag_review_v_2_0_4_2018.html`.
2. Enter any checker ID other than `tester`.
3. Choose **Load bundled 2018 checker test**. The test primary is embedded in the HTML, so no file selection is required.
4. Confirm that the locked primary records show `Needs discussion` and the checker controls are active.

The separate JSON remains available for testing the unified **Import / resume v.2.0.4 JSON** path. Compatible imports are checked by schema, version, year, and the complete candidate-key set; rebuilding the same candidate set does not block checker entry merely because its digest changed.

## Relative document locations

Keep the year directories and `human_adjudication` as siblings under the OneDrive or repository root:

```text
2018/
2019/
2024/
2025/
human_adjudication/
  human_adjudication_v_2_0_4/
    candidate_flag_review_v_2_0_4_2018.html
    ...
```

From each HTML, local document links use `../../YEAR/...`. No absolute `/home/...` or `file://` location is embedded. The folder can be moved as a unit while preserving access to the four year directories.

## Analysis labels and disclaimer

Derived labels are convenience outputs for exploration:

- Primary temporal eligible: retained `S_C`/`S_W`, statistical domain, confirmed or probable statistical error, substantive.
- Secondary temporal eligible: retained `S_C`/`S_W`, internal-nonstatistical domain, substantive internal inconsistency.
- Protocol-report descriptive: retained `P_R`.
- Other plan-material descriptive: retained `P_P`.

Any final report using these outputs should state that the workflow is exploratory, AI starting values were human-reviewable, and interpretation and downstream use remain the responsibility of the practitioner.

## Compatibility and rebuild

V.2.0.4 uses schema 7 and imports only matching v.2.0.4 snapshots. Build it from the repository root with:

```bash
python3 human_adjudication/human_adjudication_v_2_0_4/build_v_2_0_4.py
```

Use v.2.0.1, v.2.0.2, and v.2.0.3 as the valid design lineage. All `v_1_0_*` builds, including v1.0.2, v1.0.3, and v1.0.4, are failed construction versions and must not be used as references or migration inputs.
