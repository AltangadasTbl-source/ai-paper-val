# Numeric consistency review: main shard A

## Scope and evidence

Completed disjoint stable numeric scope N001–N100: abstract/narrative population relationships N001–N020; all 20 Figure 1 boxes N021–N040; all 27 Table 1 rows N041–N067; all 21 Table 2 rows N068–N088; all 10 Table 3 rows N089–N098; first two age subgroup rows N099–N100, using age ≥70 only to close the age partition. Every compared source location has role REPORT. No PLAN comparison is diagnosed in this shard. Source: [DOC-001 main article](../../../jama_huffman_2018_oi_170166.pdf#page=1), physical pages 1–7, 9, and contextual p. 10.

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md completely, current tooling and source inventory, and current main evidence mapping. Direct source layout extraction with pdftotext (Poppler 25.03.0) confirmed the printed inputs and table/flow alignment. Existing native/layout assets were used as locators only. No historical checker, candidate, screening, adjudication, or report conclusions were read. No web, GPU, Python, or source alteration was used.

## Checks and results

Every relationship has a complete row in [the owned inventory shard](../../relationships/parts/numeric_main_a.md). Flow totals reconcile: 22557 enrolled −1183 excluded =21374 included; 10066 control +11308 intervention =21374. All 20 box exclusion sums reconcile. Exclusion reasons sum to 954 marker,132 transfer,91 outside-period,6 timeline exclusions, totaling1183. Lost follow-up sums295, agreeing with215+80 and21374−21079. The Figure 1 caption expressly keeps lost participants included in analysis. The five randomized hospital cohorts sum12+13+13+13+12=63; remaining control hospitals63,51,38,25,12 reconcile with each crossover.

All displayed Table 1 and Table 2 count/percentage pairs reconcile. Every Table 1 hospital type, size, and catheterization partition totals the displayed group and hospital counts. Every displayed Table 1 crude difference reconciles with counts or the separate rounded continuous inputs. Every Table 3 clinical event percentage reconciles with its group denominator. The medication composites and counseling use expressly defined eligible subsets. Age subgroup events and participants sum to the primary result and group totals. Abstract and Key Points primary results match Table 3. Adjusted effects retain the specified hospital/time models rather than a crude identity.

Display arithmetic allowed every input its half-unit interval at its printed decimal place. For a displayed one-decimal percentage p, the interval is [p−0.05,p+0.05]; whole percentages use ±0.5. Decimal means and differences retain independent intervals, as do SDs and interval endpoints. Exact count calculations already lie within the displayed percentage intervals; widening displayed integer inputs by half a unit cannot create a discrepancy. No numeric finding remains after self-screening.

## Findings

None. Finding count: 0. No candidate IDs, severity, validity, or dispositions are assigned.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 pp. 1,5–7,9; N002–N003,N010–N014,N016,N018–N019,N041–N067,N068–N077,N079,N081–N088,N089–N095,N099–N100 | Recomputed percentages and crude baseline differences can differ from the final printed digit when displayed percentages rather than counts are subtracted; all reconcile when each input keeps its half-unit interval. Completion98.6198% prints99%; missing1.3802% prints1%; thirteen changes among1247 primary events gives1.0425%, printing1%. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p. 4 Figure 1; N021–N040 | Subtracting both excluded and lost participants from enrollment would undercount the included boxes. The caption expressly states that lost participants were included in analysis; enrolled minus excluded equals included in every box. | CONTEXT_RESOLVES |
| REPORT DOC-001 pp. 1,6–7,9; N004,N068–N098,N099–N100 | Crude event risks, ratios, or differences do not reproduce adjusted estimates, and adjusted directions can differ from crude group directions. Table titles, footnotes, and methods identify cluster/time models. | MODEL_VERSUS_CRUDE |
| REPORT DOC-001 pp. 6–7 Table 2 footnote b and Table 3 footnote a; N068–N098 | Footnotes describe odds ratios using difference-in-marginal-effects language. Separate difference and odds-ratio columns, logistic models, the OR label and reference1 identify the intended quantities at once; no displayed computation establishes an odds ratio computed as a risk difference. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001 p. 6 Table 2 door-to-balloon and door-to-needle rows; N078,N080 | The common difference-column heading contains a percent sign for rows expressly identified in minutes; footnote c identifies beta coefficients. The immediate time-row units make the unit context apparent. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-001 p. 6 Table 2 time rows; N078,N080 | The adjusted difference column and beta coefficients are distinct printed outputs. Inferring a computational identity between6.18 and13.00 or0.40 and5.00 would require model details absent from the supplied row; the crude median difference is not that identity. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 p. 7 Table 3; N096–N098 | Dividing process-composite or counseling counts by trial-group header totals does not reproduce their percentages, but footnotes explicitly restrict to eligible all-medication recipients, eligible discharged recipients, or discharged baseline smokers. No exact subset denominator is printed, so a contradiction cannot be established. | CONTEXT_RESOLVES |
| REPORT DOC-001 p. 7 Table 3; N089–N095 | Individual event component counts sum above the composite. Death, reinfarction, stroke and bleeding are not stated to be disjoint; a participant may contribute more than one component. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 p. 6 Table 2; N075,N088 | Diagnostic angiography and rehabilitation regression effects are nonestimable; no explanation or exact modeling inputs are printed. Nonestimability alone does not establish a count discrepancy. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 p. 5 Table 1; N057 | Hemoglobin is labeled mg/dL while the values13.3 and13.2 identify the familiar hemoglobin scale in context; this unit slip cannot change the intended extracted numeric values. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-001 pp. 2,10; N008–N009,N015 | Historical registries, external trials, personnel eligibility, software versions and contextual mortality are not matched ACS QUIK quantitative outcomes or analysis-population counts. | OUT_OF_FOCUS |
| REPORT DOC-001 p. 6 Table 2; N077–N078 | Door-to-balloon sample counts4022/3639 exceed primary-PCI counts3476/3234. The timing-row label does not state that timing contributors are precisely the primary-PCI-only subset, so the putative containment rule is unestablished. | CONDITIONAL_OR_UNREPORTED |

## Limitations and handoff

Exact eligible subset denominators in Table 3 and individual-level/model inputs are not printed. Numeric checking therefore does not infer them from rounded percentages or reconstruct adjusted models from crude counts. No assigned scientific coverage gap remains. Neighboring narrative relationships N173–N189 are owned by the other main numeric shard; the coordinator was informed of their source-linked comparators so findings are not duplicated.

Completed scope100 relationships; included findings0; excluded observations12. Durable outputs: checkers/parts/numeric_main_a.md and relationships/parts/numeric_main_a.md.

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
| REPORT [p. 9, Figure 3 N101–N112](../../../jama_huffman_2018_oi_170166.pdf#page=9); REPORT [pp. 6–7, narrative N173–N187](../../../jama_huffman_2018_oi_170166.pdf#page=6) | Subgroup count-derived percentages and rounded process/outcome narrative percentages can differ at their final digit. All reconcile under each displayed input's half-unit interval. For example, 375/8529 = 4.3968%, matching 4.4%; narrative in-hospital beta-blocker 43%/37% matches table 42.6%/37.2%. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [p. 9, Figure 3 N101–N112](../../../jama_huffman_2018_oi_170166.pdf#page=9); REPORT [pp. 6–8, narrative N173–N187](../../../jama_huffman_2018_oi_170166.pdf#page=7) | Several adjusted directions or effect sizes differ from crude differences and ratios, including STEMI and private-hospital subgroups and reperfusion/ACE inhibitor process results. The supplied text explicitly specifies mixed-effects adjustment for hospital clustering and temporal trends; these comparisons do not establish an effect-measure identity conflict. | MODEL_VERSUS_CRUDE |
| REPORT [p. 6, Table 2 N072/N085 and in-hospital beta-blocker narrative N176](../../../jama_huffman_2018_oi_170166.pdf#page=6); REPORT [p. 7, discharge beta-blocker narrative N184](../../../jama_huffman_2018_oi_170166.pdf#page=7) | Consolidated matched narrative/table process-detail pattern: in-hospital beta-blocker RD CI upper limit is 8.10 in the narrative and 8.40 in Table 2. Half-unit intervals [8.095,8.105] and [8.395,8.405] do not overlap. Discharge beta-blocker narrative RD 6.63 differs from Table 2 6.69: [6.625,6.635] versus [6.685,6.695]. Narrative OR 1.47 versus table 1.48 has intervals meeting at the rounding boundary, with no material change in direction or interpretation. Individual beta-blocker process measures are not the primary MACE endpoint or a key secondary endpoint under the supplied scope; optimal medication composites are distinct results. These details do not change a primary/key result, an analysis-population size, or a planned decision rule. | PERIPHERAL_COMPARISON |
| REPORT [p. 8, Figure 2 N113–N172](../../../jama_huffman_2018_oi_170166.pdf#page=8); REPORT [pp. 8–9, expanded endpoint N189](../../../jama_huffman_2018_oi_170166.pdf#page=8) | Reconstructing exact events from visually estimated Figure 2 percentages, or assigning an exact expanded-endpoint numerator from rounded 7.0%/9.1%, would require unestablished numerical inputs. No exact event counts are printed for these relationships; no event discrepancy is registered from inferred numerators. | CONDITIONAL_OR_UNREPORTED |
| REPORT [p. 7, N185 process narrative and Table 3 tobacco counseling N098](../../../jama_huffman_2018_oi_170166.pdf#page=7) | The narrative calls tobacco cessation counseling high (>95%) in both groups while the table prints 96.0% and 94.7%. The immediately adjacent table makes the intended high, similar rates evident, so the shorthand does not prevent extraction of either displayed value. | TERMINOLOGY_OR_WORDING |
| REPORT [p. 8, N188 exposure-interaction narrative](../../../jama_huffman_2018_oi_170166.pdf#page=8) | No numerical interaction estimate, event count, denominator, or test statistic is printed in the main narrative. A numeric discrepancy cannot be established by assuming an unreported value; the supplement pointer does not supply a main-paper count. | CONDITIONAL_OR_UNREPORTED |

## Limitations and handoff

Completed relationships: 89. Findings: 0. Excluded observation patterns: 6. No assigned scientific coverage gap remains. Figure 2's exact numerical rate/CI coordinates and underlying event numerators are absent from the printed figure; adjusted model calculations cannot be rebuilt from crude counts alone. These are bounded evidence limitations, not observations qualifying for registration.

Durable artifacts: relationships/parts/numeric_main_b.md and checkers/parts/numeric_main_b.md. Source links are truthful physical-page links relative to these shard directories; a coordinator copying content to canonical parent-directory artifacts must adjust the relative prefix by one directory.

# Support numeric consistency review

Assigned scope: all DOC-004 support numeric relationships from eTables1–7 (pp.17–23), toolkit PLAN samples/prospective forms (pp.2–16), and plotted count/rate definitions (pp.24–27). The complete inventory is relationships/parts/numeric_support.md, stable IDs N190–N298,109 rows. Main-paper counts are comparators only. PLAN sample-size and decision-rule families are assigned to statistical review; plan-report design matching is assigned to cross-source review.

I read QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md completely, checked the recorded local tooling and content-based roles, and independently reread exact source pp.17–23 using direct Poppler layout extraction. Complete transcriptions and source-image toolkit readings are in extraction/support_quantitative_evidence.md. No old conclusions, external evidence, web tools or unapproved Python were used. Sources and reused assets remain unchanged.

## Findings

No observation in this assigned numeric scope meets all four inclusion criteria. Counts, denominator-based percentages, population totals, step/arm totals and effect-measure labels reconcile. No F-NUM-201 or later heading is emitted.

The source establishes a model-based origin for eTable2 marginal effects, eTables5–6 ORs and eTable7 differences/ORs. Their effect labels do not conflict with an evident crude computation. Components of an expanded composite may overlap; adding event components is not a source-established identity. eTable1 immediate headers and signed values identify missing minus complete follow-up despite the generic intervention/control footnote.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT [eTable1 p.17](../../../joi170166supp3_prod.pdf#page=17), footnotea and all17 rows | Generic footnote says intervention minus control; actual headers identify complete/missing follow-up and every sign identifies missing minus complete at once. | CONTEXT_RESOLVES |
| REPORT [eTable1 p.17](../../../joi170166supp3_prod.pdf#page=17), symptom-to-door and creatinine; REPORT [eTable2 p.18](../../../joi170166supp3_prod.pdf#page=18), triglycerides | Displayed266−246=20 vs21;1.0−1.0=0 vs0.1;121−121=0 vs1 all admit overlapping half-unit input/output intervals, as calculated in inventory. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [eTable2 p.18](../../../joi170166supp3_prod.pdf#page=18), all17 baseline rows; REPORT [eTables5–7 pp.21–23](../../../joi170166supp3_prod.pdf#page=21), all54 outcome rows/adjustment vectors | Modeled baseline estimates and adjusted RD/OR may differ from crude raw percentages, differences or ratios; stated mixed models establish their origin. | MODEL_VERSUS_CRUDE |
| REPORT [eTables3–4 pp.19–20](../../../joi170166supp3_prod.pdf#page=19), continuous variables with incomplete measurements | Participant totals cannot be assumed to be measurement-contributor counts for weighted aggregation; medians/IQRs cannot be algebraically pooled from summaries. | CONDITIONAL_OR_UNREPORTED |
| REPORT [eTable7 p.23](../../../joi170166supp3_prod.pdf#page=23), expanded composite and its individual components | Summing component counts would assume absence of participant-level overlap, which the source does not establish. | CONDITIONAL_OR_UNREPORTED |
| PLAN [toolkit pp.3–14](../../../joi170166supp3_prod.pdf#page=3), all sample numerical displays | Historical sample scores, gender percentages, events, comparison-hospital groups and repeated templates do not represent trial outcome counts or analysis populations; their internal display details cannot change a primary/key secondary result or decision rule. | PERIPHERAL_COMPARISON |
| PLAN [toolkit pp.10–11](../../../joi170166supp3_prod.pdf#page=10), age/stent display totals | Sample age comparison totals99% and stent total101% reconcile when integer percentages retain half-unit rounding intervals. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN [checklists pp.15–16](../../../joi170166supp3_prod.pdf#page=15), operational dose/timing entries | Standalone dose/timing preferences and clinical appropriateness are outside numeric reporting reconciliation; intervention matching remains assigned cross-source work. | OUT_OF_FOCUS |
| REPORT [eFigures1A–2B pp.24–27](../../../joi170166supp3_prod.pdf#page=24), hospital points/intervals | Exact graph event counts and denominators are not printed; reading plot coordinates cannot establish a numeric denominator contradiction. | CONDITIONAL_OR_UNREPORTED |
| REPORT [eFigure1B p.25](../../../joi170166supp3_prod.pdf#page=25), percent decrease label | Positive decrease means C−I, whereas adjusted table differences use I−C; the word decrease resolves direction immediately. | TERMINOLOGY_OR_WORDING |

## Coverage and limitations

109 numeric relationship rows completed, including all seven eTables, 116 raw count/percentage pairs, six categorical overall/arm aggregation families, step populations, all adjusted effect identities, seven toolkit sample/form families and three figure families covering all four figure pages. Findings0; excluded observations10. Scientific coverage gaps0. Source-printed individual hospital denominators and step-specific measurement contributors are unavailable; no unsupported values were inferred. Statistical inference and planned analysis families are separate assigned scopes.

