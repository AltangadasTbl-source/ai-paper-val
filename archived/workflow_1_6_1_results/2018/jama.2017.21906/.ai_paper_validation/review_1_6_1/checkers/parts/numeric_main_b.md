# Numeric consistency review: main continuation shard

## Scope and completed checks

Assigned scope: global N101–N189, 89 relationships in DOC-001, physical pages 6–9, role REPORT. The scope and 1.6.1 review contract were read completely; current tooling, source inventory, evidence-asset inventory, and main quantitative mapping were used. Evidence comes from the supplied main PDF, source-linked native/layout extraction and matched rendered pages DOC-001-06.png through DOC-001-09.png. Source pages 6–9 were visually inspected. No old candidate conclusions, web sources, GPU, unapproved Python, or changes to source/reused assets were used.

The accompanying relationship inventory records every assigned row individually. Completed checks cover 12 subgroup numerator/denominator pairs and subgroup partitions; all 60 Figure 2 cohort-step-outcome denominator/rate relationships; and all 17 narrative relationships. The exact Figure 2 denominators reconcile between panels, across phase-step sums, and with Figure 1 analyzed counts. Every subgroup partition yields intervention 602/11308 and control 645/10066 for primary MACE. Hospital-size and hospital-type partitions each yield 63 hospitals.

Every displayed input retains its half-unit rounding interval; all integer-centered subgroup percentages already lie within their displayed one-decimal intervals. Rounded narrative percentages were checked at their own whole-percent or one-decimal display precision. Modeled mixed-effects ORs and marginal differences were not treated as crude ratios. The figure has approximate graphical coordinates, not exact printed percentages or event counts.

## Findings

No finding in this assigned scope meets all four inclusion criteria. No finding ID is assigned.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT [p. 9, Figure 3 N101–N112](../../../../jama_huffman_2018_oi_170166.pdf#page=9); REPORT [pp. 6–7, narrative N173–N187](../../../../jama_huffman_2018_oi_170166.pdf#page=6) | Subgroup count-derived percentages and rounded process/outcome narrative percentages can differ at their final digit. All reconcile under each displayed input's half-unit interval. For example, 375/8529 = 4.3968%, matching 4.4%; narrative in-hospital beta-blocker 43%/37% matches table 42.6%/37.2%. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [p. 9, Figure 3 N101–N112](../../../../jama_huffman_2018_oi_170166.pdf#page=9); REPORT [pp. 6–8, narrative N173–N187](../../../../jama_huffman_2018_oi_170166.pdf#page=7) | Several adjusted directions or effect sizes differ from crude differences and ratios, including STEMI and private-hospital subgroups and reperfusion/ACE inhibitor process results. The supplied text explicitly specifies mixed-effects adjustment for hospital clustering and temporal trends; these comparisons do not establish an effect-measure identity conflict. | MODEL_VERSUS_CRUDE |
| REPORT [p. 6, Table 2 N072/N085 and in-hospital beta-blocker narrative N176](../../../../jama_huffman_2018_oi_170166.pdf#page=6); REPORT [p. 7, discharge beta-blocker narrative N184](../../../../jama_huffman_2018_oi_170166.pdf#page=7) | Consolidated matched narrative/table process-detail pattern: in-hospital beta-blocker RD CI upper limit is 8.10 in the narrative and 8.40 in Table 2. Half-unit intervals [8.095,8.105] and [8.395,8.405] do not overlap. Discharge beta-blocker narrative RD 6.63 differs from Table 2 6.69: [6.625,6.635] versus [6.685,6.695]. Narrative OR 1.47 versus table 1.48 has intervals meeting at the rounding boundary, with no material change in direction or interpretation. Individual beta-blocker process measures are not the primary MACE endpoint or a key secondary endpoint under the supplied scope; optimal medication composites are distinct results. These details do not change a primary/key result, an analysis-population size, or a planned decision rule. | PERIPHERAL_COMPARISON |
| REPORT [p. 8, Figure 2 N113–N172](../../../../jama_huffman_2018_oi_170166.pdf#page=8); REPORT [pp. 8–9, expanded endpoint N189](../../../../jama_huffman_2018_oi_170166.pdf#page=8) | Reconstructing exact events from visually estimated Figure 2 percentages, or assigning an exact expanded-endpoint numerator from rounded 7.0%/9.1%, would require unestablished numerical inputs. No exact event counts are printed for these relationships; no event discrepancy is registered from inferred numerators. | CONDITIONAL_OR_UNREPORTED |
| REPORT [p. 7, N185 process narrative and Table 3 tobacco counseling N098](../../../../jama_huffman_2018_oi_170166.pdf#page=7) | The narrative calls tobacco cessation counseling high (>95%) in both groups while the table prints 96.0% and 94.7%. The immediately adjacent table makes the intended high, similar rates evident, so the shorthand does not prevent extraction of either displayed value. | TERMINOLOGY_OR_WORDING |
| REPORT [p. 8, N188 exposure-interaction narrative](../../../../jama_huffman_2018_oi_170166.pdf#page=8) | No numerical interaction estimate, event count, denominator, or test statistic is printed in the main narrative. A numeric discrepancy cannot be established by assuming an unreported value; the supplement pointer does not supply a main-paper count. | CONDITIONAL_OR_UNREPORTED |

## Limitations and handoff

Completed relationships: 89. Findings: 0. Excluded observation patterns: 6. No assigned scientific coverage gap remains. Figure 2's exact numerical rate/CI coordinates and underlying event numerators are absent from the printed figure; adjusted model calculations cannot be rebuilt from crude counts alone. These are bounded evidence limitations, not observations qualifying for registration.

Durable artifacts: relationships/parts/numeric_main_b.md and checkers/parts/numeric_main_b.md. Source links are truthful physical-page links relative to these shard directories; a coordinator copying content to canonical parent-directory artifacts must adjust the relative prefix by one directory.

