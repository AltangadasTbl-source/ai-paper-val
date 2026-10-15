# Statistical pass 1 — raw-score shard

Fresh runtime task: /root/stat1_raw; model gpt-6.1-sol; reasoning effort high. Pass: 1. Exact assigned scope: REPORT DOC-005 eTable 11, physical PDF pp.17–18, all21 rows and all columns/notes. Context read solely for these relationships: REPORT DOC-005 pp.2,4–5,15 and REPORT DOC-001 pp.4,11. Complete relationship record: statistics/parts/raw_inventory.md, S601–S626, each PASS_1_COMPLETE.

Direct source p17 and p18 were rendered afresh with pinned fallback PyMuPDF1.26.4, CPU,200dpi, and visually read. P15 and main p11 finding contexts were also rendered and visually read. No web, external literature, prior candidates or prior checker conclusions were used. No plan inconsistency is asserted. All21 row tuples,63 mean-difference estimate/CI tuples,63 raw central-summary/percentile tuples and21 omnibus Ps were checked. All model point estimates are inside ordered CIs; raw centers lie in ordered percentile ranges; contrast additivity is compatible with rounding. There is no SMD in this display and no pairwise P, printed test statistic or standard error.

## Findings

### F-ST1-601

**Title:** Several raw PGIC values labeled as medians do not reproduce as medians of the specified single seven-category item.

**Exact locations and roles:** REPORT [DOC-005 p17, eTable11 title and Raw Score Median (25%-tile,75%tile) header, PGIC–Pain 6/12months PT and 12months UC; PGIC–General 3months PT and 6months UC](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=17). REPORT [DOC-001 p11, Table3 footnotes h/i](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11) defines both PGIC outcomes as one item, range1–7, with seven response scores enumerated1,2,3,4,5,6,7. REPORT [DOC-005 p15, Additional Unadjusted Data and Analyses](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=15) describes eTable11 as providing unadjusted mean secondary outcomes and specifies no adjustment, weighting or imputation. REPORT [DOC-005 p18 note b](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=18) identifies the between-group quantities as linear-GEE means/95%CIs; it does not redefine raw-score medians.

**Printed values:** PGIC–Pain PT6months2.8(2.7,2.9), PT12months2.8(2.7,2.9), UC12months2.2(2.1,2.3); PGIC–General PT3months2.7(2.6,2.7), UC6months1.8(1.7,1.9). These treatment assignments follow the printed raw PT/HC/UC headings exactly, without permutation.

**Rule and reproduced calculation:** For an observed sample of responses in the stated score set {1,2,3,4,5,6,7}, an ordinary empirical median is an observed middle category when odd, or the average of the two middle categories when even. Its possible values therefore lie in {1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7}. The seven category scores are exact definitions, not rounded observations. Allow each printed one-decimal raw center its half-unit rounding interval. Distance to the closest eligible median yields:

| Exact eTable11 raw location | Printed center | Printed interval | Closest eligible median | Gap | Relative discrepancy |
|---|---:|---|---:|---:|---:|
| PGIC–Pain,6months,PT | 2.8 | [2.75,2.85] | 3.0 | 0.15 | 0.05357 |
| PGIC–Pain,12months,PT | 2.8 | [2.75,2.85] | 3.0 | 0.15 | 0.05357 |
| PGIC–Pain,12months,UC | 2.2 | [2.15,2.25] | 2.0 | 0.15 | 0.06818 |
| PGIC–General,3months,PT | 2.7 | [2.65,2.75] | 2.5 | 0.15 | 0.05556 |
| PGIC–General,6months,UC | 1.8 | [1.75,1.85] | 2.0 | 0.15 | 0.08333 |

The relative gaps are each greater than0.05. This is a check of the stated score and labeled statistic; it does not calculate or substitute a preferred analysis and does not assume that a median equals a model mean. An interpolation or score transformation that permits these medians has not been supplied for the single-item PGIC raw scores.

**Focus area:** C, statistical method logic and effect-summary identity.

**Proposed review domain:** statistical_results.

**Proposed relationship type:** S_C. **All relationships:** S_C,S_W. The supplied main REPORT defines the PGIC scale; the results supplement REPORT labels and prints the summary. The supplement's own mean description is an additional S_W quantity-definition tension. No PLAN document is a conflicting party.

**Qualifying route:** Route B.

**Affected result or extracted value:** Raw PGIC–Pain and PGIC–General outcome summaries at the five listed treatment/timepoint locations, and whether a data extractor should treat each center and pair of bounds as a median/IQR or another summary.

**Why context does not resolve it:** B1: the discrepancy concerns the statistical identity of specific reported outcome values. B2: the table explicitly labels median/percentiles, while its introductory paragraph refers to means; the linear-GEE note describes only between-group differences. No supplied score transformation or median construction explains the five values on the defined single-item scale. B3: median/IQR versus mean/interval is a different extracted quantity and determines which summary can be used in evidence synthesis. The source does not identify the intended statistic at once.

**Alternatives and missing definitions:** The raw columns could be means with uncertainty intervals, consistent with the supplement p15 description; they could instead summarize a transformed PGIC score or a defined interpolated/aggregate quantity. The supplied text does not identify such a raw-score transformation, the median rule, or an interval construction for those raw columns. In the set-valued mathematical definition of a median, any point between two middle observations can be a median; the calculation above uses the ordinary empirical rule of their average. A disclosed alternative interpolation could therefore resolve the numerical restriction. No raw data identify those middle observations. This is a limitation for the independent inclusion screen, rather than an assertion that all possible median definitions exclude the printed centers. The between-group GEE contrasts remain distinct quantities and are not themselves challenged by this finding. A diagnostic column-permutation pattern is recorded separately in S624; it is not assumed in the calculation above.

**Exact human question:** For the five PGIC raw-score entries listed above, what score and summary statistic produced the centers and bounds: empirical medians/interquartile ranges of the defined1–7 item, means with intervals, or a transformed/aggregate score? Please identify the applicable definition and confirm which statistic a data extractor should take from the raw-score columns.

**Linked relationships:** S617,S618,S619,S620,S623.

## Excluded observations

Only apparent issues decided not to emit are listed here. Reconciled checks are recorded in the S inventory.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-005p17 PGIC remaining fractional raw centers: Pain PT3=2.9,UC3=1.9,HC6=2.1,UC6=2.1,HC12=2.1; General UC3=1.6,PT12=2.6,HC12=1.9,UC12=1.9 | These centers also fall between eligible ordinary single-item medians, but their half-unit interval gaps to the nearest eligible median are0.05 and relative discrepancies range0.0172–0.0313, at most0.05. These occurrences are outside the five-location finding under the display-precision rule. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-005p17 all21 raw-summary/contrast rows, p15 intro, p18 note b | Subtracting raw centers under printed PT/HC/UC headings differs from many GEE mean contrasts. A diagnostic UC/PT/HC permutation of raw columns makes all21 contrast triples feasible within one-decimal rounding. However the raw centers explicitly represent medians and the contrasts model means; no supplied method establishes equality between the two. This numerical permutation alone does not reproduce an arm-label or mean-difference inconsistency. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-005p17 physical functioning6/12months omnibusP=.005/.001; contextual DOC-001p11 footnote c and DOC-005p15 intro | A diagnostic same-covariance normal-CI, joint two-contrast Wald reconstruction matches social3 and physical3 Ps within rounding but yields physical6 approximateP=.015–.040 and physical12 approximateP=.0036–.020. eTable11 does not specify its exact omnibus reference distribution/degrees of freedom, normal-versus-t CI rule, or whether omnibus and CIs use the same fitted covariance. An exact conflict cannot be asserted by importing these choices from convention or another display; no null/significance contradiction exists at .05. | CONDITIONAL_OR_UNREPORTED |

## Diagnostic details and limitations

The omnibus diagnostic uses h=(upper−lower)/2, SE=h/1.959964, Var(c)=Var(a)+Var(b)−2Cov(a,b) for a=PT−UC,b=HC−UC,c=HC−PT, then a quadratic Wald statistic and a chi-square2 survival probability. This is expressly an approximation and is not the supplied eTable11 test definition. Numerical exploration allowed every printed estimate and CI endpoint its0.05 half-unit interval and constrained c=b−a and symmetric intervals around each estimate. A finite grid gave social3 P approximately0.00017–0.00182 and physical3 approximately0.1529–0.3124, both containing their printed three-decimal ranges; physical6 approximately0.01520–0.04009 and physical12 approximately0.00361–0.02028. These are diagnostic grid ranges, not certified global bounds, and no precise covariance, reference distribution or degrees of freedom are inferred as the source method. The diagnostic is preserved for fresh pass2 review rather than promoted as an exact calculation.

The individual repeated measures and HC clustering are described in the main methods; eTable11 specifies linear GEE and no adjustment/weighting/imputation. This combination is internally coherent. Missing per-outcome sample counts, covariance, variance estimator and raw summary definition limit full mechanical reconstruction; the last is a source-grounded conflict for the PGIC finding, while other absent details alone are not findings. No noninferiority/equivalence/interim/stopping rule or conclusion occurs in the assigned scope. All21 source rows were covered and no scientific source-unit gap remains.

Counts: pass1; exact display scope DOC-005pp17–18;26 stable S records;21 complete row tuples;1 consolidated finding;3 excluded-observation rows. Paths: statistics/parts/raw_inventory.md;checkers/parts/stat1_raw.md; fresh derivatives preprocessing/stat1_raw/.

