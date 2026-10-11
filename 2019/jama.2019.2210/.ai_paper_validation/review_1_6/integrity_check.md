# Workflow 1.6 Final Integrity Check

- Direct source files: 4; before/after SHA-256 lists identical; PASS.
- Reused evidence assets: 289; before/after SHA-256 lists identical; PASS.
- Recorded workflow controls: 4; before/after SHA-256 lists identical; PASS.
- No source, reused asset or earlier audit artifact was written by this run.
- Full source coverage: 96 total = 50 reusable + 46 fresh-required = 96 mapped.
- Statistical coverage: 148 unique S IDs, with each row PASS_1_COMPLETE and PASS_2_COMPLETE.
- Candidate coverage: C001-C015 retained in ledger, recheck, audit and complete report.

Final hash files are source_hashes_after.sha256, reused_artifact_hashes_after.sha256 and workflow_control_hashes_after.sha256. Direct sha256sum and lossless diff were used; no Python reasoning or extraction was used.
