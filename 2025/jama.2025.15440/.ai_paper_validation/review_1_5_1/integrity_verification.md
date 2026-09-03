# Post-Review Integrity Verification

- **Verification time:** After Markdown assembly and token-accounting cutoff.
- **Command:** `sha256sum --check .ai_paper_validation/review_1_5_1/source_hashes_before.sha256`
- **Direct-source result:** 4 of 4 files returned `OK`.
- **Command:** `sha256sum --check .ai_paper_validation/review_1_5_1/reused_artifact_hashes_before.sha256`
- **Reused-artifact result:** 51 of 51 files returned `OK`.
- **Conclusion:** All supplied direct sources and all inventoried reused evidence assets were unchanged.
