# Mechanical relationship ID consolidation

No relationship row is selected or removed. All provisional rows in all four completed mapper artifacts are retained. Source order is main article, original/early final plan, remaining final plan, then plan appendices and results supplements. Tables with their source context and definitions are transferred into the canonical inventories; exact source locations remain in the complete maps.

| Mapping artifact | Provisional numeric IDs | Canonical numeric IDs | Provisional statistical IDs | Canonical statistical IDs |
|---|---|---|---|---|
| extraction/main_quantitative_evidence.md | M-N001 through M-N062 | N001 through N062 | M-S001 through M-S036 | S001 through S036 |
| extraction/parts/plan_001.md | P1-N001 through P1-N022 | N063 through N084 | P1-S001 through P1-S011 | S037 through S047 |
| extraction/parts/plan_002.md | P2-N001 through P2-N024 | N085 through N108 | P2-S001 through P2-S032 | S048 through S079 |
| extraction/parts/support_003.md | P3-N001 through P3-N032 | N109 through N140 | P3-S001 through P3-S031 | S080 through S110 |

Engine: awk section transfer and Perl deterministic ID-offset substitution. Source paths in part tables are adjusted by one relative directory level. Numeric checking scope1 is N001 through N084 and scope2 is N085 through N140; each is below120 relationships. Statistical passes each cover all110 S relationships.

Bare within-P3 numeric cross-references were resolved by provenance: original P3 N021 means canonical N129, and P3 N026 means canonical N134. The complete mapper source values were not changed.
