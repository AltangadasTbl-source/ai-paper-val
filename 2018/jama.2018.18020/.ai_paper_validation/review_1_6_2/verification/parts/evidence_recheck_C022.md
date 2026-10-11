## C022 — Two baseline total means do not reconcile with displayed genotype aggregation

Pending Human Adjudication.

**Evidence state:** reproduced.
**Review domain:** statistical_results.
**Relationship type:** S_W.
**All relationships:** S_W.
**Compared document roles:** REPORT main article Table 2 baseline total/genotype means p.7, Table 2 population labels and footnotes p.8, available-data context p.4, and corroborating Table 1 genotype headers p.5.
**Qualifying route recorded at registration:** Route A, category 4.
**Classification ambiguity:** None in document roles or relationship type; actual baseline observation membership and weights remain unavailable.

Fresh appended-ID mechanical rechecker `/root/evidence_recheck_append`, fixed `gpt-6.1-sol`/`high`, covered exactly C022 and both affected rows. The complete scope and review contract, C022 ledger card, and complete pass-2 inclusion-screen artifact were read. This card records evidence facts and classification; it does not assign a disposition.

### Location found and exact-source values matched

All cited locations were found. Exact-source page renders produced from the supplied PDF using direct Poppler 25.03.0 CPU rendering were independently visually inspected: `preprocessing/recheck/main-p4.png`, `main-p5.png`, `main-p7.png`, and `main-p8.png`. Their commands, page assignments and engine are documented in `preprocessing/recheck/derivative_record.md`. Direct source extraction with `pdftotext -layout -f 7 -l 8 jama_stunnenberg_2018_oi_180136.pdf -` supplied additional transcription assistance; the visual page readings were authoritative. No new derivative, OCR, GPU step, or source/reusable-asset modification was needed.

| Exact supplied-source location | Role by content | Source reading confirmed | Recheck use |
|---|---|---|---|
| [Main Table 2, PDF p.7](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=7), title and baseline column header | REPORT | Total nondystrophic myotonia group N=27; baseline column is Mean (SD). | Confirms the nominal total population label and that compared values are baseline means, separate from treatment-period changes and treatment effects. |
| [Main Table 2, PDF p.7](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=7), Handgrip action myotonia, fifth attempt and immediately following genotype rows | REPORT | Total 1.36 (1.25) seconds; CLCN1 0.93 (0.41); SCN4A 2.59 (3.00). | Confirms every affected mean and its row/column alignment; parenthetical values are SDs, not mean comparators. |
| [Main Table 2, PDF p.7](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=7), Handgrip dynamometry transient paresis, fifth attempt and immediately following genotype rows | REPORT | Total 20.30 (18.75)%; CLCN1 24.35 (23.11)%; SCN4A 9.12 (10.33)%. | Confirms the second affected total and both genotype means, with percentage scale. |
| [Main Table 2, PDF p.7](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=7), IVR stiffness and genotype baseline rows | REPORT | Total 5.65 (1.78); CLCN1 6.45 (1.71); SCN4A 4.34 (2.02). | Confirms the same-display comparator. |
| [Main Table 2 continued, PDF p.8](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=8), footnote a | REPORT | IVR results use a linear mixed model; other secondary-outcome mean treatment effects use dependent t tests; n=16 CLCN1 and n=11 SCN4A are printed in that treatment-effect footnote. | Confirms nominal genotype counts, while preserving that this footnote does not expressly supply each row's baseline available-case n. |
| [Main Table 2 continued, PDF p.8](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=8), footnotes b, h and l | REPORT | IVR baseline means use daily calls in the 14-day baseline period. Other baseline measures use visit 1 at the start of the first treatment period. Handgrip action myotonia measures relaxation after forceful contraction for 5 seconds; transient paresis is maximal percentage decline in peak force, 0–100%, from five trials. | Confirms baseline time and outcome scale. No affected-row baseline sample count or weighting formula is supplied. |
| [Main Table 1, PDF p.5](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=5), genotype column headers and baseline summary labels | REPORT | CLCN1 N=16 and SCN4A N=11; relevant Table 1 descriptive summaries are medians (IQRs). | Corroborates nominal genotype populations only. Table 1 medians are not compared with Table 2 means as competing copies. |
| [Main statistical context and Numbers Analyzed, PDF p.4](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=4) | REPORT | 27 completers contributed 31 treatment sets: 23 one-set patients and four two-set patients. Secondary assessments collected were 2676 of 2728 possible; missingness was described as relatively small and assumed at random, with no multiple imputation. Analyses included all available data. | Confirms a source-grounded possibility of outcome-specific available-case observations, without identifying the actual baseline subsets. |

All source and comparator readings agree with registration. No transcription or location correction was needed. Footnote a's population counts are retained as nominal labels, rather than asserted to be each affected baseline row's actual denominators.

### Consistency rule and reproduced calculation

For a total ordinary mean constructed from the same observations partitioned into two disjoint genotype groups, the aggregation identity is `(nC × meanC + nS × meanS) / (nC + nS)`. The registered display-based calculation substitutes nominal printed nC=16, nS=11 and N=27. The identity is mathematically applicable to that displayed-population comparison; its application to the actual underlying baseline summaries requires their observation/weight mapping, which the source does not provide. The source does not expressly identify these non-IVR baseline means as adjusted model estimates. Footnote a describes treatment-effect methods and does not establish a baseline weighting rule.

Apply the workflow's continuous half-unit interval to every displayed input: nC=[15.5,16.5], nS=[10.5,11.5], N=[26.5,27.5], each printed mean ±0.005, and each printed total mean ±0.005. For positive inputs, the conservative lower bound uses both minimum counts and means divided by maximum N; the upper bound uses both maximum counts and means divided by minimum N. Independent count variation deliberately relaxes nC+nS=N and widens the recomputed interval. It is a display-precision bound, not an assertion that fractional participants existed. The discrepancy survives this conservative relaxation.

| Baseline row | Nominal weighted mean | Recomputed interval | Printed total interval | Gap between intervals | Gap / absolute printed total |
|---|---:|---|---|---:|---:|
| Fifth handgrip, seconds | 1.606296296 | [1.508363636, 1.708301887] | [1.355, 1.365] | 0.143363636 | 0.105414439 |
| Fifth transient paresis, % | 18.145185185 | [17.202000000, 19.124339623] | [20.295, 20.305] | 1.170660377 | 0.057667999 |
| Comparator stiffness | 5.590370370 | [5.287818182, 5.904716981] | [5.645, 5.655] | 0 | 0 |

The affected rows both exceed the relative 0.05 display criterion. The stiffness comparator reconciles under this precision rule, but its nominal weighted mean is not exactly 5.65. Its 14-day call baseline differs from the non-IVR visit-1 baselines; comparator precision compatibility does not establish identical actual weights across outcomes. The interval calculations and alternatives below were independently evaluated in JavaScript arithmetic, with no Python scientific reasoning or classification.

**Calculation reproduced:** Yes, for both registered display-based aggregation comparisons, including all-input half-unit intervals. **Necessary inputs available:** All printed means, nominal population labels, scales, baseline-time definitions and relevant missing-data context are available. **Necessary inputs unavailable:** Row-specific visit-1 baseline participant/observation counts for total and each genotype group; exact membership of each summary; whether every patient's contribution is equally weighted; handling of missing/partial measurements within each fifth attempt; whether total and genotype summaries use the identical observation set; and the exact aggregation/summary specification. Participant raw data are not supplied. The overall 2676/2728 assessment count cannot supply these row-specific inputs.

### Source-grounded alternatives, direct observation and remaining human question

The available-data statements support an alternative in which nominal 16/11 trial groups contain different numbers of usable baseline observations for these outcomes, or summary weights differ. The printed totals lie between the corresponding genotype means and can therefore be expressed as weighted mixtures: the central printed values imply CLCN1 weights of 0.740963855 for fifth handgrip and 0.734077479 for fifth transient paresis, versus nominal 16/27=0.592592593. These implied weights are arithmetic diagnostics, not inferred observed counts.

Illustrative available-case subsets demonstrate why the missing mapping matters. Fifth-handgrip nC=14 and nS=5 would yield [1.361842105,1.371842105] allowing only the subgroup means' rounding intervals, which overlaps the printed [1.355,1.365]. Fifth transient paresis nC=11 and nS=4 would yield [20.283666667,20.293666667], with remaining gap 0.001333333 relative to 20.30 of 0.000065681, within the workflow's precision criterion. Both examples fit within nominal genotype group sizes. They are hypothetical existence demonstrations, not evidence that these subsets were used, and do not replace the mandatory calculation on the printed population inputs. Different actual weights could also reconcile the central values exactly.

The 31 treatment sets do not establish 31 replicated baseline observations: footnote b places non-IVR baseline at visit 1, the start of the first treatment period. No consequence for a treatment-effect estimate is inferred. No comparison with a PLAN document is needed, and no interpretation of adjusted treatment effects as crude means is imposed.

**Direct observation:** The source contains the two total means, their genotype means and nominal group sizes stated above; using those displayed sizes leaves the reproduced interval gaps. The displayed comparator is compatible under the workflow's rounding rule. **Inferred explanation:** Missing baseline measurements, different membership or weighting could account for the gaps; the source does not identify which, if any, applies. The absence of the actual row-specific mapping is a limitation, not a demonstrated production mechanism.

**Classification confirmed:** Every compared location is published results/method/context content within the same main article, hence REPORT. Primary relationship S_W and All relationships S_W are confirmed; no P_R, P_P or S_C relationship exists. Domain statistical_results is confirmed because the issue concerns reported means, population weights and aggregation logic, rather than competing labels for different outcomes. No classification correction is required.

**Determining recheck fact:** The exact source values and nominal population inputs match registration, and both display-based aggregation gaps exceed 0.05 after the full half-unit interval check; therefore the evidence state is reproduced. This state records that bounded comparison and does not establish the underlying available-case denominator or weights.

**Exact remaining human question:** Which visit-1 baseline observations, outcome-specific total and genotype denominators, memberships and weights produced the fifth-handgrip total 1.36 seconds and fifth transient-paresis total 20.30%, and how do those mappings reconcile each total with its displayed genotype means and nominal 16/11 population labels?

**Remaining limitation:** The supplied package does not provide the actual row-specific baseline observation/weight mapping or participant raw data. No cited location was inaccessible. C022 remains Pending Human Adjudication.
