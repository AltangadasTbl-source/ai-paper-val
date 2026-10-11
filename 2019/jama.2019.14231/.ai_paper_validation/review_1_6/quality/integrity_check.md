# Source, reused evidence, and workflow integrity

The coordinator recomputed SHA-256 values after scientific review on 2026-10-11T01:36Z. Each after-inventory is byte-identical to its before-inventory. A subsequent final validation independently rehashes every supplied source and every reused artifact.

| Inventory | Files | Result |
|---|---:|---|
| source_hashes_before.sha256 vs source_hashes_after.sha256 | 3 | UNCHANGED |
| reused_artifact_hashes_before.sha256 vs reused_artifact_hashes_after.sha256 | 90 | UNCHANGED |
| workflow_controls_before.sha256 vs workflow_controls_after.sha256 | All inventoried original workflow/configuration controls | UNCHANGED |

Commands used `sha256sum` on each recorded path, then `cmp` on each pair. All commands exited 0. No original source, reused artifact, role preset, configuration, or workflow helper was modified. The current-provider validation copy is separately documented in [the override record](../validation_override/README.md).
