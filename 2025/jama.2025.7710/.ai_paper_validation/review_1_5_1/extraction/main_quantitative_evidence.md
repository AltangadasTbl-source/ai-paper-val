# Complete main-paper quantitative evidence extraction

## Scope and method

Current direct source: `jama_kumar_2025_oi_250034_1750956984.08518.pdf`, PDF pp.1-11. Fresh native and layout extraction was run across pp.1-11 because all earlier DOC-001 derivatives were stale for the current source hash. Every page was inspected, including Figure 1 (p.4), Table 1 (p.5), Table 2 (p.6), Table 3 (p.7), Figure 2 and Table 4 (p.8), and narrative results/discussion (pp.1, 2, 3, 4, 5, 6, 7, 9). No OCR was needed: native and layout PDF text were readable, and layout extraction preserved table/figure structure.

## Complete relationship inventory

This extraction’s local numeric relationship records `MN001`-`MN043`, including all result-relevant displayed counts, denominators, percentages, distribution summaries, times, units, population labels, tables/figures, and narrative matches, are in:

- `parts/relationships/main_numeric.md`

This extraction’s local statistical relationship records `MS001`-`MS027`, including effects, intervals, P values, models, thresholds, direction, and inferential narrative matches, are in:

- `parts/relationships/main_statistical.md`

## Page-level coverage

| PDF page | Directly inspected content | Mapping result |
|---:|---|---|
| 1 | Abstract, intervention, primary/secondary results | Mapped MN001-002, MN007-008, MN026, MS001/MS010/MS027. |
| 2 | Background earlier-trial numerical result; Methods start | Mapped MN039/MS026; no additional current-trial results. |
| 3 | Outcomes, sample size, models, interim boundary | Mapped MN008, MN040-041, MS024-025. |
| 4 | Figure 1, missing-pH plan, statistical convention, Results narrative | Mapped MN003-006, MN030, MN042 and related statistical relationships. |
| 5 | Table 1 and baseline-result narrative | Mapped MN009-018 and MP-MN01. |
| 6 | Table 2, primary-results narrative | Mapped MN019-025, MN026, MN030, MS001/MS003/MS011. |
| 7 | Table 3, results, site-specific outcomes | Mapped MN027-031 and MS002-010/MS019. |
| 8 | Figure 2 and Table 4 | Mapped MN032-038 and MS012-023. |
| 9 | Discussion/limitations and conclusion | Mapped MN043; checked primary/site/interaction narrative matches. |
| 10 | Article information and references | No applicable study-result quantitative unit. |
| 11 | References | No applicable study-result quantitative unit. |

## Direct-source artifacts

- `preprocessing/DOC-001.native.txt`
- `preprocessing/DOC-001.layout.txt`

## Potential consistency material retained for later checking

The only apparent display difference was resolved in mapper record `MP-MN01`: placebo Australia/New Zealand ethnicity is 874 (53.7%) in Table 1 using its stated nonmissing denominator of 1629 and 874 (53.6%) in the abstract/Results using 1631 randomized participants. It has no candidate ID. No consistency proposal was generated.

## Limitations

No visual OCR was required. Table 1/2 descriptive rows do not supply inferential tests; none was inferred.
