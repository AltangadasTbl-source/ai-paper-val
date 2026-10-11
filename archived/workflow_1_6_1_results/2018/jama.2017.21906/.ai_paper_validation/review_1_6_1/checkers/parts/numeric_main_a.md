# Numeric consistency review: main shard A

## Scope and evidence

Completed disjoint stable numeric scope N001–N100: abstract/narrative population relationships N001–N020; all 20 Figure 1 boxes N021–N040; all 27 Table 1 rows N041–N067; all 21 Table 2 rows N068–N088; all 10 Table 3 rows N089–N098; first two age subgroup rows N099–N100, using age ≥70 only to close the age partition. Every compared source location has role REPORT. No PLAN comparison is diagnosed in this shard. Source: [DOC-001 main article](../../../../jama_huffman_2018_oi_170166.pdf#page=1), physical pages 1–7, 9, and contextual p. 10.

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

