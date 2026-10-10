# v.2.1.5.3 — Excel-only workflow

Review, handoff, checking, completion checks and result delivery require only Excel. Four annual files retain 45 paper sheets and 412 candidates, unchanged source text and methodological option meanings. Every cell, sheet and workbook structure is unprotected. Backups preserve records; this is not a tamper-proof audit system.

Setup B6 is the stage selector. The 18-column C_ layout remains shared. Complete uses no, primary_done and checker_done; initial completion cannot finish checking. M displays blank throughout primary review and the frozen initial summary during checking.

Primary_snapshot contains key, eight effective assessment fields, initial completion, reviewer ID and summary. In primary stage it looks up answers by Candidate key. At handoff the user saves a primary backup, creates a checker copy and pastes snapshot values in place before switching to checker. Unfrozen snapshot formulas return NOT FROZEN in checker stage. Missing or partially frozen snapshots block final readiness. Key-based lookups preserve alignment after sorting.

Checker answers are direct edits. Blank means blank; no inherited overrides or clear sentinel. Agree requires equality with the effective initial assessment. Inactive fields normalize to not_applicable in results, while stale literal input prevents readiness. Required and optional active answers are checked against their option codes. Disagree, unable and primary discuss require resolved discussion and a note.

G owns per-candidate readiness. Checks summarizes Decisions status. Decisions includes both assessments and checker/discussion records. Outcomes remain blank until FINAL READY. Paper_counts withholds final counts until the entire paper is final. Protocol_plan_table preserves P_R/P_P descriptions. Final annual workbooks are the deliverables; managers may combine result sheets with Paste Values.

Retained substantive S_C/S_W statistical confirmed/probable findings enter primary_temporal; retained substantive report-internal findings enter secondary_temporal. P_R/P_P remain protocol_descriptive/plan_descriptive. Other final records are not_eligible. Visible-answer checking is not blinded inter-rater reliability.

Schema xlsx-adjudication-excel-9; version v.2.1.5.3. Maintenance uses JavaScript artifact tooling. A small OOXML post-processing step sets every style to unlocked and automatic recalculation, capabilities unavailable in the documented authoring surface. Reviewers never need maintenance tools. No Python files or dependency installation are part of this release workflow.
