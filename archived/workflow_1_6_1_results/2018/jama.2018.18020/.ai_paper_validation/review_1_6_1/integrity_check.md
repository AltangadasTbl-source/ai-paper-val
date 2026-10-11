# Final Source and Reused-Asset Integrity Check

Source integrity: PASS. All four recomputed source SHA-256 records match source_hashes_before.sha256 byte for byte.

Reused-asset integrity: PASS. All 95 recomputed asset SHA-256 records match reused_artifact_hashes_before.sha256 byte for byte.

Engine: direct sha256sum; exact package-relative paths from the before manifests; comparisons: direct cmp. After manifests are source_hashes_after.sha256 and reused_artifact_hashes_after.sha256. Supplied sources and pre-existing audit artifacts were preserved.
