# Statistical pass 1 — support shard A

- Runtime task ID: /root/statistics_pass1_support_a
- Model and effort: gpt-6.1-sol / high; fresh pass-1 statistical shard
- Scope: REPORT DOC-004 joi180108supp3_prod.pdf, eTable 1 p5 all 48 variable–occasion tuples; eTable 2 p6 all 72 variable–mode–occasion tuples; matched eFigures 2–4 pp11–13 within nine existing tuples.
- Relationship inventory: statistics/parts/support_a_inventory.md, stable S201–S320 in source-row order; all 120 explicitly PASS_1_COMPLETE.
- Findings: 1; excluded observations: 1 consolidated row; scientific coverage gaps: 0.
- Source roles: DOC-004 REPORT by methods/results content. Main REPORT and SAP PLAN are used solely to establish context; they do not create additional assigned relationships here.

The full normative QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read before checking. Every assigned tuple was checked for median/IQR containment and endpoint order, units and effect-measure identity, printed P and applicable stated statistical rules, matched figure direction and attribution, and analysis logic. The IQRs are not treated as confidence intervals for between-group estimates. No contrast confidence intervals, standard errors or test statistics appear in these tuples. No superiority, noninferiority, equivalence, interim, stopping or sample-size decision occurs in the assigned displays.

The main article specifies two-sided P values and .05 significance without multiplicity adjustment. It describes a repeated-measures mixed model for longitudinal tidal volumes, not an explicit model/test mapping for each separate mode/day table or cumulative-distribution panel. Continuous P values cannot be reproduced solely from medians/IQRs without that mapping and observations; this absence supplies no independent contradiction. Eight binary comparisons were assessed against printed n/N and percent values and a labelled uncorrected Pearson χ² diagnostic; all reconcile under display precision. The ABG footnote supplies the binary denominators, so headers are not substituted. All nine figure comparisons match table mode, day, contrast, direction and printed P (including .027 versus .03 after precision). These reconciling checks are recorded in the inventory, not as excluded observations.

## Findings

### F-ST1-201

**Observation:** The intermediate-arm PEEP median and interquartile-range entry after titration in the other-ventilation-mode section does not satisfy quartile ordering or contain its median.

**Exact locations and roles:** REPORT [DOC-004 eTable 2, physical p6](../../../../joi180108supp3_prod.pdf#page=6), “Other Mode of Ventilation,” “After titration on day of randomization,” PEEP, cmH2O, intermediate tidal volume cell; REPORT footer on the same page defining the summaries as “median (interquartile range).” The table is a retrospective results display, not PLAN material. A direct source rendering confirms the printed reading (preprocessing/st1-a-source-p6.png; Poppler pdftoppm 25.03.0, CPU). Reusable layout text and the reusable image independently show the same digits.

**Printed values:** Intermediate PEEP is **8 (5–1)** cmH2O; low PEEP is **5 (5–10)** cmH2O; comparison **P=0.50**. Contributor headers are 33 low and 28 intermediate patients. No effect confidence interval is printed. This finding concerns the intermediate median/IQR, not the P value.

**Rule and calculation:** Any median (interquartile range) must satisfy Q1 ≤ median ≤ Q3, with Q1 ≤ Q3. The printed reading gives Q1=5, median=8 and Q3=1, so 5>1 and 8>1. Permitting integer display half-units gives Q1∈[4.5,5.5], median∈[7.5,8.5], Q3∈[0.5,1.5]. Thus even the largest displayed upper-quartile allowance, 1.5, is below the smallest allowed median, 7.5, by **6 cmH2O**, and below the smallest allowed lower quartile by **3 cmH2O**. Reordering the two endpoints to [1,5] would still leave its largest possible endpoint 5.5 below the smallest possible median 7.5 by 2 cmH2O.

**Recomputed interval and relative gap:** Given the printed median alone, the admissible upper-quartile interval is [7.5,∞) cmH2O; the printed upper-quartile half-unit interval is [0.5,1.5]. The minimum gap is 6 cmH2O and relative discrepancy against the printed upper quartile 1 is 6/1=**6.00**. The exact intended Q3 is not reconstructable from the supplied summaries. For the primary containment rule below, Route A category 1 is not screened by display precision; the half-unit calculation also demonstrates that this is not a precision reconciliation.

**Focus area:** B, estimate and interval logic.

**Proposed review domain:** statistical_results.

**Proposed relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route A, category 1. The displayed median lies outside its printed IQR under any endpoint order. The substituted or truncated upper-quartile digit is also consistent with category 2's printed-value-slip rule, but its production mechanism and intended digit are not inferred.

**Affected result or extracted value:** The intermediate-arm PEEP distribution after titration among patients ventilated in the “other mode” category, specifically its upper quartile and median/IQR to be extracted.

**Why context does not resolve it:** Route A category 1 requires registration of point-estimate/interval containment conflicts. The same-page footer establishes that the parentheses are an interquartile range; no intended upper quartile is provided in immediate context. Knowing that the Q3 must be at least the median does not identify its value for extraction.

**Source-grounded alternatives and missing definitions:** An upper-quartile digit may be absent or substituted, an endpoint may have been displaced, or the central value may belong to a different summary. The reported table footnote provides no alternative statistic or ordering convention. Reversing the two printed endpoints does not restore containment. No particular replacement digit or final correction is proposed. The per-row statistical test is not mapped, but that does not affect the arithmetic quartile relationship or establish a P discrepancy.

**Exact human question:** What are the intended median and first and third quartiles for intermediate-arm PEEP after titration in the other-ventilation-mode group, and which upper-quartile value should a reader extract from eTable 2?

**Related relationship:** S313. The single cell's ordering and containment conflicts are consolidated into this one finding.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-004 eTable 2 p6 PSV VT day 2 (S275) versus eFigure 3 p12 PSV day 2; diagnostic binary P checks eTable 1 p5 pHa<7.25 day 1/day 2 (S242, S243) | Figure P=.027 versus table P=.03 has overlapping half-unit intervals [.0265,.0275] and [.025,.035], gap 0. For the labelled uncorrected Pearson χ² diagnostics, P≈.390901 versus .40 and P≈.715260 versus .71 produce point-diagnostic residual gaps .004099/.40≈.01025 and .000260/.71≈.000367 before any input allowance, both ≤.05; the diagnostic is not asserted as the authors' test. These apparent precision differences are one consolidated pattern and do not establish significance or interval conflicts. | ROUNDING_OR_DISPLAY_PRECISION |

## Limitations and handoff

No assigned scientific unit is omitted. The table/figure P algorithm, individual continuous-variable measured sample sizes, degrees of freedom, covariance and variance estimator are not fully supplied or mapped; no such specification is inferred, and no t-test or rank-test approximation is substituted for continuous P reproduction. The inventory separates IQRs from confidence intervals and records all tuple-specific printed values and status. Curves were inspected visually for attribution, axes, median direction and P rather than digitized for invented exact quantiles. Count/denominator diagnostics found no qualifying observation in this scope. Pass 2 must be executed by a different fresh runtime agent after the merged ledger, screening log and mechanical recheck exist.

Artifact paths: checkers/parts/statistical_pass_1_support_a.md; statistics/parts/support_a_inventory.md. New source derivative: preprocessing/st1-a-source-p6.png, direct Poppler pdftoppm 25.03.0, CPU. Reused images inspected: review_1_5_2/preprocessing/rendered_pages/joi180108supp3_prod-p5.png, p6.png, p11.png, p12.png, p13.png; source-matched reusable assets preserved unchanged.

