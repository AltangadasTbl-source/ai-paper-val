# Independent inclusion screen — pass 2

Runtime agent: `/root/inclusion_screen_pass_2`; model `gpt-6.1-sol`; reasoning effort `high`; fresh mandatory pass-2 screener. Exact scope: the one new finding `F-ST2-001` in `checkers/statistical_pass_2.md`. The complete QUALITY_CONTROL_SCOPE.md and review contract, including the inclusion-screen section, were read. Source pages were reread independently of the checker decision. No external evidence, earlier-run conclusions, or candidate-count target was used. The coordinator alone assigns a stable candidate ID and appends this decision to the canonical screening table.

## Screening table

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-ST2-001 | statistics_pass_2 | pass_2 | INCLUDE | MEETS_THRESHOLD | C022 |

**F-ST2-001 — INCLUDE:** Route A, category 4 applies because the displayed genotype-weighted aggregate-mean identity reproduces the same-display stiffness baseline within full display precision but leaves relative interval gaps of 0.105414439 and 0.057667999 for the printed fifth-handgrip and fifth transient-paresis baseline totals, respectively, with outcome-specific available-case observations and weights unresolved.

## Independent source confirmation

All cited locations are REPORT content in the supplied main article, `jama_stunnenberg_2018_oi_180136.pdf`:

- [Table 2 p.7](../../../jama_stunnenberg_2018_oi_180136.pdf#page=7): total N=27 in the title; baseline fifth-handgrip mean 1.36 seconds, CLCN1 0.93 and SCN4A 2.59; baseline fifth transient-paresis mean 20.30%, CLCN1 24.35% and SCN4A 9.12%; baseline stiffness comparator 5.65, CLCN1 6.45 and SCN4A 4.34. Values are in the baseline mean column, separate from the period-change and treatment-effect columns.
- [Table 2 footnotes a/b p.8](../../../jama_stunnenberg_2018_oi_180136.pdf#page=8): n=16 CLCN1 and n=11 SCN4A; dependent t tests concern the non-IVR mean treatment effects. Non-IVR baseline measurements are from visit 1 at the start of the first treatment period; IVR baselines summarize daily calls in the 14-day baseline period. The footnotes supply no outcome-specific baseline sample counts or weights.
- [Table 1 p.5](../../../jama_stunnenberg_2018_oi_180136.pdf#page=5): genotype headers independently corroborate 16 and 11. Its median summaries are not treated as competing copies of the Table 2 baseline means.
- [Numbers Analyzed and statistical context p.4](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4): 27 completers contributed 31 treatment sets; 2676 of 2728 possible secondary-outcome assessments were collected; multiple imputation was not performed; analyses included all available data. These statements make outcome-specific subsets plausible without identifying either affected row's actual baseline observations or weights.

Exact-source renders visually inspected: `preprocessing/recheck/main-p7.png`, `main-p8.png`, `main-p5.png`, and `main-p4.png`. Their source-page production is documented in `preprocessing/recheck/derivative_record.md`: direct Poppler 25.03.0 CPU rendering from the supplied PDF. No new rendering, OCR, or modification of those assets occurred. The images agree with all compared source values and locations.

## Independent display-precision calculation

For the displayed aggregation, recompute `(nC × meanC + nS × meanS) / N`. Apply the normative continuous half-unit rule to every input: nC in [15.5,16.5], nS in [10.5,11.5], N in [26.5,27.5], and each mean within ±0.005. The printed total mean also receives ±0.005. For these positive means, the conservative recomputed lower bound uses both minimum counts and means with maximum N; the upper bound uses both maximum counts and means with minimum N. Allowing counts to vary independently makes the interval at least as wide as imposing nC+nS=N; the discrepancies survive this conservative relaxation.

| Baseline row | Nominal recomputation | Recomputed interval | Printed total interval | Interval gap | Relative gap |
|---|---:|---|---|---:|---:|
| Fifth handgrip, seconds | 1.606296296 | [1.508363636,1.708301887] | [1.355,1.365] | 0.143363636 | 0.105414439 |
| Fifth transient paresis, % | 18.145185185 | [17.202000000,19.124339623] | [20.295,20.305] | 1.170660377 | 0.057667999 |
| Comparator stiffness | 5.590370370 | [5.287818182,5.904716981] | [5.645,5.655] | 0 | 0 |

Relative gaps divide by the absolute printed totals 1.36 and 20.30. Both affected rows exceed 0.05. The stiffness intervals overlap; its nominal discrepancy is not claimed to be an exact arithmetic identity. Calculations were independently evaluated with JavaScript arithmetic; Python was not used for scientific screening or classification.

## Scope, alternatives, and consolidation

This is a within-display baseline estimate-aggregation relationship, not a comparison of descriptive baseline copies across documents or tables. It falls in focus area C and proposed review domain `statistical_results`; provisional relationship type and all relationships are `S_W`. No PLAN content conflicts. The extracted results at issue are the baseline fifth-handgrip total 1.36 seconds and fifth transient-paresis total 20.30%, together with their relationship to the displayed genotype means and population sizes.

The reproducing nominal group-aggregation method and the above-threshold printed gaps establish the category-4 inclusion route. The source does not label these baseline means adjusted model estimates. Outcome-specific available-case denominators, differing total/subgroup membership, or weights may reconcile the underlying summaries, and the missing-assessment statement provides a supplied-source basis for these alternatives. The nominal genotype counts are not asserted to be each row's actual available-case counts. The stiffness comparator likewise does not establish equal observation weights across outcomes. No complete-patient-data assumption, reconstructed participant measurements, or treatment-effect consequence is asserted. Category 4 retains the absent observation/weight mapping as the human question rather than screening the printed mismatch as conditional.

The two affected rows share the same aggregation rule and unavailable baseline mapping, so they form one included issue with both locations retained. Existing C015 was inspected only to decide consolidation within this current run: it concerns the treatment-effect versus treatment-period paired-mean difference identity across eleven rows. Its rule, compared columns, and human question differ from the present total-versus-genotype baseline aggregation. Overlap in outcome names and a general possibility of missing-data weights do not establish the same issue or cause. Do not consolidate F-ST2-001 into C015.

**Remaining human question:** Which baseline observations, row-specific denominators, total/subgroup memberships and weights produced the printed total and genotype means for fifth handgrip and fifth transient paresis, and how do those mappings reconcile the displayed summaries?

## Counts and handoff

Findings screened: 1. Included issues: 1. Screened-out findings: 0; every screened-out reason-code count is zero. Candidate ID remains PENDING. No supplied-source location was inaccessible. Available-case baseline mappings remain a bounded evidence limitation. Every registered candidate remains Pending Human Adjudication.

Canonical-table row to append after coordinator registration:

`| F-ST2-001 | statistics_pass_2 | pass_2 | INCLUDE | MEETS_THRESHOLD | C022 |`
