# Numeric consistency review

The fresh numeric review covers all count, denominator, percentage, partition, repeated-count, descriptive-range and effect-identity relationships mapped for the five supplied PDFs: 94 source pages, 108 stable grouped N relationships, all main Table 1 and Table 2 rows, every flow component and Figure 2 risk count, and all supplementary eTables 1–5 numeric cells. Compound cells and exact locations are enumerated in ../relationships/numeric_relationship_inventory.md and the two fresh mapper artifacts. Every relationship is marked COMPLETE. No earlier candidate or report conclusion was used.

Two findings were retained after self-screening. Six apparent observations or repeated observation families were excluded, each with one reason code. The review used half-unit input and output intervals before the relative-gap threshold of 0.05. Reconciled checks are recorded in the inventory and are not excluded observations.

## Findings

### F-NUM-001

The reported binary risk ratios require clarification of which risk is being compared.

**Exact source locations and document roles:** REPORT main article [physical page 6, Table 2, Development of ARDS and Extrapulmonary infection rows and footnote c](../../../jama_simonis_2018_oi_180108.pdf#page=6); REPORT [physical page 1, abstract ARDS result](../../../jama_simonis_2018_oi_180108.pdf#page=1); REPORT [physical page 4, Statistical Analysis, binary outcomes method](../../../jama_simonis_2018_oi_180108.pdf#page=4). All ten Table 2 RR rows share the same footnote and exhibit the same approximate alternative calculation pattern; their complete inputs and calculations are in N047–N056. Only ARDS and extrapulmonary infection independently exceed the display-precision threshold for the point comparison. No inference is made that the other eight isolated point comparisons exceed it.

**Printed inputs:** ARDS 17/448 (3.8%) versus 23/462 (5.0%), RR 0.86 (95% CI 0.59–1.24), P=.38; extrapulmonary infection 20/448 (4.5%) versus 28/463 (6.0%), RR 0.84 (95% CI 0.60–1.18), P=.28. The abstract repeats the ARDS RR, interval and P value. Table 2 defines RR as risk ratio and footnote c says the effect estimate is risk ratio, with Wald likelihood ratio approximation intervals and chi-square P values. The main binary-outcome method states the same without naming an adjusted model for these rows.

**Rule and calculation:** For event risks in the low versus intermediate randomized arms, RR=(a/nLow)/(b/nIntermediate). ARDS gives (17/448)/(23/462)=0.762228. Allowing each displayed count and denominator ±0.5 yields [0.722479, 0.803849]. The printed 0.86 interval is [0.855,0.865], so the minimum gap is 0.051151 and relative discrepancy 0.051151/0.86=0.059478. Extrapulmonary infection gives (20/448)/(28/463)=0.738202, input interval [0.705568,0.772108], printed interval [0.835,0.845], gap 0.062892 and relative discrepancy 0.074872. Both exceed 0.05. Percentages themselves reconcile with the counts.

As a diagnostic alternative, comparing allocation proportions among people with and without the event gives [a/(a+b)]/[(nLow−a)/(nLow+nIntermediate−a−b)]. This is 0.857889 for ARDS and 0.840148 for extrapulmonary infection, which round to the printed values. This reverse conditioning also approximately follows the ten-row pattern. Square roots of crude odds ratios follow a similar approximate pattern in several rows. Neither diagnostic establishes the producing method: for example, some rows do not reproduce exactly under either diagnostic. The finding concerns the numerical risk-ratio interpretation, rather than a claim about a particular production mechanism or a reconstructed interval.

**Focus area:** A and C.

**Proposed review domain:** statistical_results.

**Proposed relationship:** S_W; all compared locations are REPORT content within the main article.

**Qualifying route:** Route B.

**Affected result or extracted value:** The ARDS RR 0.86 and extrapulmonary infection RR 0.84, including the ARDS value copied into the abstract; these represent materially different relative magnitudes from the displayed armwise event risks. The other Table 2 RR rows corroborate the repeated identity pattern and should be clarified together if the same method produced them.

**Why context does not resolve it:** The printed armwise events and method identify a binary risk comparison but do not explain a different conditioning, estimator, adjustment, or transformation. A reader cannot determine whether the extracted RR represents the risk of the clinical event by assigned strategy or a differently defined risk. This observation is in focus, survives the precision rule, and bears on numerical effect extraction. It is not based on comparing a stated adjusted or modeled binary estimate with a crude ratio: no such binary model is identified in the cited method.

**Alternatives and missing definition:** An unreported modeled or standardized risk ratio could differ from the armwise calculation; a reverse-conditioned risk ratio or transformed odds ratio could instead explain some displayed values. If these are model-based risks, the model, conditioning and target population are needed. The supplied Cox models concern mortality event times and are not used as a crude comparator here. No alternative is asserted as the intended interpretation.

**Exact human question:** What risk-ratio estimand, conditioning, and calculation produced theTable 2 binary RR rows, particularly ARDS 0.86 and extrapulmonary infection 0.84, and how do those values relate to the printed armwise event counts and denominators?

### F-NUM-002

The PEEP interquartile range in one supplementary cell is reversed and does not contain its median.

**Exact source location and document role:** REPORT [joi180108supp3_prod.pdf physical page 6, eTable 2, Other Mode of Ventilation, After titration on day of randomization, Intermediate Tidal Volume, PEEP row](../../../joi180108supp3_prod.pdf#page=6). The same page footer defines the entries as median (interquartile range). The exact source-linked page image and current direct layout extraction both show the printed cell.

**Printed inputs:** PEEP 8 (5–1) cm H2O; intermediate-arm contributors 28; low-arm counterpart 5 (5–10). Other intermediate PEEP cells are 8 (5–8) on day 1, 10 (6–12) on day 2, and 6 (5–8) on day 3. These counterparts locate the cell but are not substituted for it.

**Rule and calculation:** A printed first-to-third-quartile range must have lower limit≤upper limit and contain the median. With half-unit integer display intervals, median 8 allows [7.5,8.5], lower quartile 5 allows [4.5,5.5], and upper quartile 1 allows [0.5,1.5]. The smallest lower-versus-upper gap is 4.5−1.5=3, relative discrepancy 3/1=3.0 against the upper printed value. The smallest median-versus-upper gap is 7.5−1.5=6, relative discrepancy 6/8=0.75 against the median. No display-precision combination gives an ordered range containing the median.

**Focus area:** A and B, descriptive numerical range logic.

**Proposed review domain:** statistical_results.

**Proposed relationship:** S_W, within the REPORT supplement.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** The upper PEEP quartile for intermediate-volume ventilation in the Other Mode group immediately after titration; the printed value is 1 cm H2O.

**Why context does not resolve it:** Route A category 2 applies because a printed numerical interval limit changes the magnitude reading beyond the precision rule. The intended upper quartile cannot be uniquely recovered from the adjacent cells, even though the reversed reading is apparent.

**Alternatives and missing definition:** A substituted or omitted digit is possible, but the supplied display does not establish which numerical upper quartile was intended. Reversing 5 and 1 would still fail to contain median 8. No replacement is proposed.

**Exact human question:** What upper quartile should be used for the intermediate-group Other Mode PEEP cell printed as 8 (5–1) cm H2O immediately after titration?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT [main p5, Table 1 LIPS risk, septic shock, tobacco, alcohol and admission rows](../../../jama_simonis_2018_oi_180108.pdf#page=5) | Some percentages imply available-data denominators below randomized headers 477/484; tobacco, alcohol and admission partitions total 475/482. For example 82/477=17.191% versus 17.6%; allowing half units gives [17.068,17.314], gap to 17.55 divided by 17.6=0.01339. LIPS cells have relative gaps 0.0027/0.0028; every implicit pair and partition remains≤0.05. Consolidated once as the shared denominator observation. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [supplement p8, eTable 4 sedatives, analgesics, neuromuscular blockade and vasopressors](../../../joi180108supp3_prod.pdf#page=8) | Against headers 477/484, all eight implicit percentages show a similar available-data denominator pattern. Recomputed half-input intervals and relative gaps: sedative low[66.911,67.261] vs70.6%,0.04658; intermediate[68.627,68.976] vs72.1%,0.04263; analgesic low[57.906,58.237] vs61.1%,0.04604; intermediate[56.244,56.567] vs59.1%,0.04202; NMBA low[10.995,11.228] vs11.7%,0.03609; intermediate[12.281,12.513] vs13.0%,0.03362; vasopressor low[75.916,76.285] vs80.0%,0.04581; intermediate[72.755,73.113] vs76.4%,0.04237. Each output interval uses±0.05 percentage points; all remaining relative gaps≤0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [main p6 primary/secondary headers](../../../jama_simonis_2018_oi_180108.pdf#page=6) and [p7 Figure 2 initial risk counts](../../../jama_simonis_2018_oi_180108.pdf#page=7) | Outcome-specific available-case counts and initial risk sets differ, notably hospital stay Figure 2D458/456 versus table secondary header475/481. The reports do not equate these sets; an isolated contributor-count comparison for different displays is peripheral and does not establish a conflicting primary analysis size. | PERIPHERAL_COMPARISON |
| REPORT [main p6 subgroup narrative](../../../jama_simonis_2018_oi_180108.pdf#page=6) and [supplement p9 eTable 5](../../../joi180108supp3_prod.pdf#page=9) | Narrative calls the intervals around the subgroup mean differences IQR, while eTable 5 specifies 95% CI and gives the identical numerical limits. Immediate mean-difference context and matching full table identify the intended interval; no printed numerical value differs. | TERMINOLOGY_OR_WORDING |
| REPORT [main p6 Table 2](../../../jama_simonis_2018_oi_180108.pdf#page=6) | Global Mean Difference heading coexists with explicit RR/HR row labels and defining footnotes. Each row-specific quantity is immediately identifiable; the heading does not require extracting a ratio as a mean difference. | CONTEXT_RESOLVES |
| REPORT [supplement pp5–7 respiratory-variable tables](../../../joi180108supp3_prod.pdf#page=5) | Aggregate median driving pressure need not equal aggregate median plateau pressure minus median PEEP; median minute ventilation need not equal the product of separate tidal-volume and respiratory-rate medians. These observations rely on unsupported arithmetic on separate marginal summaries, with no stated reproducing identity. | CONDITIONAL_OR_UNREPORTED |

## Limitations and integrity

No numeric coverage gap remains. Patient-level data, exact curve-coordinate data, survivor-only and subgroup sample sizes, and row-specific implicit available-data denominators are not supplied. The two numerical findings are direct printed observations; the alternatives remain explicitly diagnostic. Exact source confirmation used supplied raster images plus direct Poppler 25.03.0 layout text. Fresh targeted derivative locations and engine details are recorded in the inventory. No source or reusable artifact was modified. No candidate IDs, adjudications, severity, validity, or dispositions were assigned.
