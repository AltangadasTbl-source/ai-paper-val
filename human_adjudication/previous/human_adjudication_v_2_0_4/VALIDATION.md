# V.2.0.4 build validation

- Build time: 2026-09-13 00:08 UTC
- Direct candidate base: `human_adjudication/previous/human_adjudication_v_2_0_3` frozen v.2.0.3 annual HTML payloads
- Base candidate SHA256: `2b20312e0af5d96b9517d939d860cd4f0ba723cf438795a40c1db7102a892818`
- Meta-report results used only for editable AI starting assessments: `meta_report/consistency_reclassification_2026-09-04/reclassified_candidates.json`
- Meta-report result SHA256: `b785b1bb4ce418e5ce5d6d5dc84f911da9854b0d64d8f1e04d481c90fe2ef470`
- Candidate extraction from meta-report/reclassification JSON: none
- Candidate keys: 412 unique keys
- Relationship counts: P_R=45, P_P=50, S_C=65, S_W=252
- AI starting dispositions: retain=402, exclude=9, discuss=1
- Referenced final-report paths: all present
- Local document locations: portable relative links rooted at ../../YEAR/
- Embedded candidate JSON: parsed and reconciled for every output
- Unified JSON import recognizes AI initial-state, primary, and checker records
- Two-stage workflow markers: primary, checker, locked primary, proposed final, reset action, and bundled 2018 test entry present
- Removed review fields: flag verification, duplicate status/key, potential consequence, evidence checked, and primary rationale
- Review schema: 7 (v.2.0.4 snapshots only; no automatic migration from earlier versions)

| Year | Papers | Candidates | Output |
|---|---:|---:|---|
| 2018 | 10 | 119 | `candidate_flag_review_v_2_0_4_2018.html`; `ai_initial_state_v_2_0_4_2018.json` |
| 2019 | 10 | 71 | `candidate_flag_review_v_2_0_4_2019.html`; `ai_initial_state_v_2_0_4_2019.json` |
| 2024 | 10 | 91 | `candidate_flag_review_v_2_0_4_2024.html`; `ai_initial_state_v_2_0_4_2024.json` |
| 2025 | 15 | 131 | `candidate_flag_review_v_2_0_4_2025.html`; `ai_initial_state_v_2_0_4_2025.json` |

Local report/evidence/source links checked: 1812
Secondary-stage test snapshot: `secondary_stage_test_primary_v_2_0_4_2018_all_needs_discussion.json`; reviewer `tester` / `Workflow Tester`; 119/119 complete and Needs discussion

Result: **PASS**
