# Support numeric consistency review

Assigned scope: all DOC-004 support numeric relationships from eTables1–7 (pp.17–23), toolkit PLAN samples/prospective forms (pp.2–16), and plotted count/rate definitions (pp.24–27). The complete inventory is relationships/parts/numeric_support.md, stable IDs N190–N298,109 rows. Main-paper counts are comparators only. PLAN sample-size and decision-rule families are assigned to statistical review; plan-report design matching is assigned to cross-source review.

I read QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md completely, checked the recorded local tooling and content-based roles, and independently reread exact source pp.17–23 using direct Poppler layout extraction. Complete transcriptions and source-image toolkit readings are in extraction/support_quantitative_evidence.md. No old conclusions, external evidence, web tools or unapproved Python were used. Sources and reused assets remain unchanged.

## Findings

No observation in this assigned numeric scope meets all four inclusion criteria. Counts, denominator-based percentages, population totals, step/arm totals and effect-measure labels reconcile. No F-NUM-201 or later heading is emitted.

The source establishes a model-based origin for eTable2 marginal effects, eTables5–6 ORs and eTable7 differences/ORs. Their effect labels do not conflict with an evident crude computation. Components of an expanded composite may overlap; adding event components is not a source-established identity. eTable1 immediate headers and signed values identify missing minus complete follow-up despite the generic intervention/control footnote.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT [eTable1 p.17](../../../../joi170166supp3_prod.pdf#page=17), footnotea and all17 rows | Generic footnote says intervention minus control; actual headers identify complete/missing follow-up and every sign identifies missing minus complete at once. | CONTEXT_RESOLVES |
| REPORT [eTable1 p.17](../../../../joi170166supp3_prod.pdf#page=17), symptom-to-door and creatinine; REPORT [eTable2 p.18](../../../../joi170166supp3_prod.pdf#page=18), triglycerides | Displayed266−246=20 vs21;1.0−1.0=0 vs0.1;121−121=0 vs1 all admit overlapping half-unit input/output intervals, as calculated in inventory. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [eTable2 p.18](../../../../joi170166supp3_prod.pdf#page=18), all17 baseline rows; REPORT [eTables5–7 pp.21–23](../../../../joi170166supp3_prod.pdf#page=21), all54 outcome rows/adjustment vectors | Modeled baseline estimates and adjusted RD/OR may differ from crude raw percentages, differences or ratios; stated mixed models establish their origin. | MODEL_VERSUS_CRUDE |
| REPORT [eTables3–4 pp.19–20](../../../../joi170166supp3_prod.pdf#page=19), continuous variables with incomplete measurements | Participant totals cannot be assumed to be measurement-contributor counts for weighted aggregation; medians/IQRs cannot be algebraically pooled from summaries. | CONDITIONAL_OR_UNREPORTED |
| REPORT [eTable7 p.23](../../../../joi170166supp3_prod.pdf#page=23), expanded composite and its individual components | Summing component counts would assume absence of participant-level overlap, which the source does not establish. | CONDITIONAL_OR_UNREPORTED |
| PLAN [toolkit pp.3–14](../../../../joi170166supp3_prod.pdf#page=3), all sample numerical displays | Historical sample scores, gender percentages, events, comparison-hospital groups and repeated templates do not represent trial outcome counts or analysis populations; their internal display details cannot change a primary/key secondary result or decision rule. | PERIPHERAL_COMPARISON |
| PLAN [toolkit pp.10–11](../../../../joi170166supp3_prod.pdf#page=10), age/stent display totals | Sample age comparison totals99% and stent total101% reconcile when integer percentages retain half-unit rounding intervals. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN [checklists pp.15–16](../../../../joi170166supp3_prod.pdf#page=15), operational dose/timing entries | Standalone dose/timing preferences and clinical appropriateness are outside numeric reporting reconciliation; intervention matching remains assigned cross-source work. | OUT_OF_FOCUS |
| REPORT [eFigures1A–2B pp.24–27](../../../../joi170166supp3_prod.pdf#page=24), hospital points/intervals | Exact graph event counts and denominators are not printed; reading plot coordinates cannot establish a numeric denominator contradiction. | CONDITIONAL_OR_UNREPORTED |
| REPORT [eFigure1B p.25](../../../../joi170166supp3_prod.pdf#page=25), percent decrease label | Positive decrease means C−I, whereas adjusted table differences use I−C; the word decrease resolves direction immediately. | TERMINOLOGY_OR_WORDING |

## Coverage and limitations

109 numeric relationship rows completed, including all seven eTables, 116 raw count/percentage pairs, six categorical overall/arm aggregation families, step populations, all adjusted effect identities, seven toolkit sample/form families and three figure families covering all four figure pages. Findings0; excluded observations10. Scientific coverage gaps0. Source-printed individual hospital denominators and step-specific measurement contributors are unavailable; no unsupported values were inferred. Statistical inference and planned analysis families are separate assigned scopes.

