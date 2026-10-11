# Final source and reused-evidence integrity

Status: PASS. After complete Markdown assembly, direct GNU coreutils9.7 sha256sum recomputed all three supplied-source hashes and all102 reused-artifact hashes. Each after-list is byte-identical to its before-list; sha256sum -c reports105 successful checks and no failed check. Supplied sources and reused artifacts remain unchanged.

Durable records: source_hashes_before.sha256, source_hashes_after.sha256, reused_artifact_hashes_before.sha256, reused_artifact_hashes_after.sha256, source_hash_verification.txt and reused_hash_verification.txt. Newly created review derivatives are inventoried separately and do not alter the reused-artifact set.
