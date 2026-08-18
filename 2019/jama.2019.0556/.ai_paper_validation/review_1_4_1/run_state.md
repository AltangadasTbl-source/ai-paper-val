# Workflow 1.4.1 Run State

- **Target elapsed minutes:** 20-25
- **Started UTC:** 2026-08-18T06:09:33Z
- **Finished UTC:** 2026-08-18T06:58:55Z
- **Observed elapsed minutes:** 49.4
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Final quality-audit repair required direct mapping of 81 pages without reusable extraction; runtime-profile repair reran both statistical passes at explicit Terra high effort; expanded coverage increased the relationship set to 95 numeric and 54 statistical units and the candidate set to 9.

## Execution Notes

- Review profile: 1.4.1 (reuse existing evidence assets and restart candidate discovery).
- Direct-source inventory and SHA-256 capture began at the recorded start time.
- Legacy candidate, queue, disposition, quality, and final-report records are excluded as scientific inputs.
- Runtime-profile repair: the initial statistical pass artifacts were produced through a pre-existing Terra-medium mapper session despite high-effort role instructions. Both passes were rerun by an explicitly configured `gpt-5.6-terra` high-effort specialist; the rerun corrected an S004 cross-location description and preserved the stable relationship/candidate sets.
- Coverage repair: the high-effort evidence-quality audit identified an unchecked sample-size arithmetic relationship and result-relevant content among 81 pages without reusable extraction. New disjoint support-mapping shards were assigned; no existing stable candidate ID will be renumbered.
