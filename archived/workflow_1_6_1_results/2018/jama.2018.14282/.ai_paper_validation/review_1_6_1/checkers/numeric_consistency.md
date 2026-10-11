# Numeric consistency review

COMPLETE. Exact scope: every applicable numeric relationship from four supplied PDFs,144 pages, reconstructed from109 main map groups and152 support map groups. Newly registered 96 stable N relationships in relationships/numeric_relationship_inventory.md. Every N001–N096 reviewed for counts, denominators, totals, percentages, repeated values, subset bounds, and effect-measure identity within its supplied context. Administrative/background groups explicitly recorded. No prior findings or report conclusions used. Direct source confirmation of compared report statement and arm denominators: Poppler pdftotext 25.03.0, fresh layout extraction of DOC-001 pp.4–7, preprocessing/numeric_confirmation/main-p4-p7.txt. Source PDF remains authority.

Findings: 1. Excluded observations: 13 consolidated patterns. No candidate IDs or adjudications assigned. Statistical and cross-source lanes independently cover inferential/design questions; there is no assumed crude-to-Cox correspondence.

### F-NUM-001

**Title:** Organ-support statement associates overall-cohort percentages with treatment-arm counts.

**Relationship:** N052, with N001 denominator context. Focus area A (counts and denominators). Proposed review domain: statistical_results. Proposed relationship type: S_W.

**Exact source locations and roles:** REPORT main article [PDF p.6, Post Hoc Outcomes, second sentence](../../../jama_azoulay_2018_oi_180109.pdf#page=6); REPORT main article [PDF p.5, Patients](../../../jama_azoulay_2018_oi_180109.pdf#page=5),389 randomized and388 completed/analyzed in each arm; REPORT main article [PDF p.4, Table1 column headers](../../../jama_azoulay_2018_oi_180109.pdf#page=4),n = 388 each. All locations are REPORT content.

**Printed inputs:** The p.6 sentence states that, in the overall population, vasopressors and renal replacement therapy were needed in153 patients(19.7%) randomized to high-flow oxygen therapy and31 patients(4%) randomized to standard oxygen therapy, with no statistical difference between groups. Arm sizes are389 randomized/388 retained; total retained 776.

**Rule and calculation:** A count assigned to one treatment arm has that arm as denominator when presented as the arm-specific frequency, unless another denominator is specified. For388,100×153/388=39.433% and100×31/388=7.990%; for389 they are39.332% and7.969%. Printed19.7% and4% instead match153/776=19.716% and31/776=3.995%. Using half-unit intervals for all displayed inputs, 153 ±.5and388 ±.5 yield39.254%–39.613%, wholly outside19.7 ±.05%;31 ±.5and388 ±.5 yield7.851%–8.129%, wholly outside4 ±.5%. Using randomized389 ±.5 also leaves the intervals disjoint. The sentence therefore does not reconcile as a treatment-arm frequency statement. Overall-cohort arithmetic reconciles, but it does not settle whether the counts represent the two organ supports across the full cohort or the two treatment groups as grammatically assigned.

**Affected result or extracted value:** Numbers/proportions requiring vasopressors or renal replacement therapy by treatment arm in the reported post hoc outcomes. A data extractor could take153/388 and31/388 as arm-specific organ-support outcomes, or153/776 and31/776 as separate whole-cohort support outcomes; these are different quantities.

**Why context does not resolve it:** “In the overall population” supports a pooled-cohort reading, but the same sentence explicitly assigns153 to high-flow and31 to standard oxygen while also naming two different organ supports and asserting no statistical difference. There is no nearby outcome-by-arm table or separate vasopressor/renal-replacement count to identify which organ support each count belongs to, whether the counts are pooled or arm-specific, or the arm-specific values of the second support. Thus identifying776 as the arithmetic denominator does not identify the intended endpoint/population allocation.

**Source-grounded alternatives and missing definition:** (1)153 and 31are whole-cohort counts for vasopressors and renal replacement therapy respectively, with 776 denominator; (2)they are treatment-arm counts with percentages calculated over the full retained cohort; (3)each refers to an unspecified combined organ-support endpoint. The supplied sentence does not define whether “vasopressors and renal replacement therapy” means separate or combined outcomes and does not provide the required outcome-by-arm mapping. No alternative is adopted as fact.

**Exact human question:** Do153 and 31represent vasopressor and renal-replacement counts in the full cohort, counts in the high-flow and standard-oxygen arms, or a combined organ-support endpoint, and which endpoint-by-arm counts and denominators should be extracted?

## Excluded observations

Exactly one scope reason code per consolidated observation. Reconciled routine checks are documented in the96-row inventory; this table records apparent discrepancies or limitations considered during self-screening.

| Location | Observation | Reason code |
|---|---|---|
| DOC-001 pp.1–3,5;N001 | Abstract/KeyPoints776versus778randomized:two consent withdrawals and388 retainedperarm explicitly identify intended population. | CONTEXT_RESOLVES |
| DOC-001 p.3;DOC-002 pp.91,103;N010,N068 | Article779total versus389each:all arm targets,plan778,and observed778identify total778at once; no sample-size formula conclusion follows from one-person slip. | CONTEXT_RESOLVES |
| DOC-001 p.4 Table1;N015,N016,N026 | Liver45(13.3%),kidney69(20.4%),postextubation14(4.1%)and18(5.3%)imply about338rather than388. Available-case denominators are not printed; a claim that each must use388depends on an unestablished absence of missing baseline observations. Counts remain unambiguous. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 p.4 Table1;N014,N022,N025,N028,N029;DOC-001 p.5Table2N041,N042,N044;DOC-003p.2N082,N084 | Several last-decimal percentages/differences differ from fixed exact-count recomputation (e.g.,27/388=6.959%printed6.9%,39/388=10.052%printed10.0%,−5.155%printed−5.1%). With each displayed input retaining half-unit intervals, the printed output intervals are reachable. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p.4;N017 | Charlson footer19–114versuspatient scores5andIQR3–7:category-count/weight wording does not obscure which patient values are printed and is a field-resolvable scale description. | CONTEXT_RESOLVES |
| DOC-001 p.4;N019,N035,N036 | Immunosuppression/cause/topdiagnosis counts are not exhaustive mutually exclusive categories; forcing them to sum776depends on unsupported assumptions. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 pp.1,5–6;DOC-003p.2;N045,N047,N048,N054,N087 | Median differences differ from reported mean contrasts (ICU8−6versusmean.6;oxygen150−119versusmean19.5). Table2footnote and eTablemedianlabels distinguish summaries. | CONTEXT_RESOLVES |
| DOC-001 pp.5,7;N040–044,N065,N066 | Cox/cause-specificHRs differ from crude risks, including Figure3. No source states those HRs are crudeRRs; numeric lane does not use crude ratios as proof. Same-resultHRreference/direction belongs to independent statistical review. | MODEL_VERSUS_CRUDE |
| DOC-001 p.7;N060,N064 | PaO2andhematologic subgroup denominators do not sum388perarm. Lack of an explicit missing-subgroup-data convention prevents asserting an exhaustive complete-case partition; all eventcounts≤their denominators. | CONDITIONAL_OR_UNREPORTED |
| DOC-001p.6;DOC-003pp.3–5;N050,N089,N090,N092,N094,N095 | Timepoint risk/contributor counts differ across displays or repeat/rebound. Different outcomes, missing measurement availability and censoring make these distinct populations; they are peripheral contributor displays rather than primary analysis-set totals. | PERIPHERAL_COMPARISON |
| DOC-001p.6Figure2;DOC-003p.2;N050,N086 | Probability ticks.1–.4withpercentaxis andFiO2 70withoutpercentglyph: intended units identifiable immediately from scale and oxygen context. | NOTATION_OR_TYPOGRAPHY |
| DOC-003pp.4–5;N091,N093–095 | Exact graph centres/bar dispersion are unprinted; cannot reproduce exact estimate/CI/test or compare graph means with tablemedians without assumptions. | CONDITIONAL_OR_UNREPORTED |
| DOC-002background/adminunits;N079–081 | Historicalstudycounts,clippedhistoricalTable4,centrecounts,calendars,reference/page/line numbers anddata-sharingtime statements do not establishHIGHresult quantities or decision rules. | OUT_OF_FOCUS |

## Limitations and handoff

No scientific coverage gap in the assigned numeric scope. Limitations: no raw data or event times, no stated available-case denominators for several baseline/subgroup quantities, no exact plotted coordinates or defined dispersion for supplementary graphs. HistoricalPLANtablespp.127–128are source-clipped and out-of-focus; no missing text reconstructed. Direct-source confirmation engine and derivative are recorded above; source and reused assets unchanged. Source links resolve from this checker file. Independent inclusion screen must reread F-NUM-001 before any candidate registration.
