# Statistical pass 1 — Workflow 1.6.2

Runtime agent: /root/statistics_pass1. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. This is a fresh pass-1 agent, not a promoted mapper. Exact scope: every relationship S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120, S121, S122, S123, S124. All52 groups receive PASS_1_COMPLETE in statistics/relationship_inventory.md, which retains every printed component and calculation.

Read completely: QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md. The independent inclusion screener must examine the finding below; no C IDs or dispositions are assigned here. Count:1 finding;9 excluded apparent observations. No route A category 1 interval–test conflict was reproduced. Every primary/sensitivity estimate/interval, all 31 supplementary P comparisons, all 9 initial power rows, all 5 whole-trial updated power rows and all 6 subgroup power rows were checked, including values that reconcile or have named unavailable implementation inputs.

## Finding

### F-ST1-001

**Title:** Age-under-75 subgroup power at trial size 5000 and two-sided .01 does not reproduce under the calculation that tracks the other table cells.

**Compared locations and document roles:**
- PLAN DOC-002, [protocol physical PDF page 22, Table 4](../../../joi250068supp1_prod_1760999665.28862.pdf#page=22), age <75 row, rightmost “Power for total of 5000,2p<0.01” cell:34%.
- PLAN DOC-002, same table/row, “Power for total of 4000,2p<0.01”:20%, corresponding .05 powers 41%/52%, sample sizes 2924(.05)/4048(.01), population 25%, active AF2.96%, control 1.18%, ratio 2.5. Every other row's power cells in this same table provide reconstruction comparators; all affected/comparator cells are on this page.
- PLAN DOC-002, [protocol physical PDF page 20, Table 2](../../../joi250068supp1_prod_1760999665.28862.pdf#page=20), explicitly “Total sample size (continuity corrected)” for the original two-proportion power calculations; all 9 rows inspected. [Page 21 Table 3](../../../joi250068supp1_prod_1760999665.28862.pdf#page=21) corroborates the reconstruction with updated whole-trial sizes/powers and is contextual support rather than a separate conflict.

**Printed values:** Table 4 age <75 has population 25%, patch rate 2.52%, active2.5-year rate 2.96%, active/control ratio 2.5, implied control 1.18%; sample sizes 2924/4048 for 90% at .05/.01; powers for total trial 4000 .05/.01 and5000 .05/.01 are41%,20%,52%,34%. The rightmost 34% is the affected value. Source image was opened directly;34% is a visual source reading, not an OCR substitution.

**Rule and calculation:** Reconstruct the same table's two-proportion power using an equal 1:1 comparison and continuity correction. Let p0=.0118,p1=.0296,pbar=(p0+p1)/2,d=p1−p0,A=√[2pbar(1−pbar)],B=√[p0(1−p0)+p1(1−p1)]. For total trial T and subgroup fraction f, per-arm m=Tf/2; zα=Φ⁻¹(1−α/2). The reconstructed power is

100×{Φ[(√m d−zα A−1/√m)/B]+Φ[(-√m d−zα A−1/√m)/B]}.

For T=5000,f=.25,m=625,α=.01,zα=2.575829304, this gives 28.585281%, versus 34% printed. At T=4000,m=500, same alpha, it gives 20.530754%, tracking the printed 20%. At .05 it gives 41.851153%/52.055448%, tracking41%/52% within the scope's display-precision rule. The complete calculation table in statistics/relationship_inventory.md shows all 24 cells, not a selected subset. Each of the other 23 power cells has remaining relative discrepancy at most .05, including cells whose precise normal-approximation values do not round to the exact printed integer. Table 4 sample-size diagnostics also track all 12 printed outputs; e.g. under 75 diagnostic 2905.288/4024.585 versus 2924/4048, <1% differences.

This reconstruction is an explicitly labeled **diagnostic normal approximation and empirically reproducing same-display method**. The source does not identify its exact software/function or continuity-correction implementation for Table 4. It is not assumed to be the universal power algorithm or the algorithm of any reported treatment-effect analysis. Route A category 4 permits the unstated method to become the human question when one method tracks the other rows.

**Display-precision calculation:** Inputs' half-unit intervals are control [1.175,1.185]%, active [2.955,2.965]%, population [24.5,25.5]%; T=5000 is the specified design size. Conservatively allowing these three intervals to vary independently, the minimum/maximum reconstructed powers at their monotonic extrema are 27.354722% and 29.840489%. This envelope also allows departures from the displayed exact ratio 2.5; enforcing that constraint cannot enlarge it. The printed 34% interval is [33.5,34.5]%. The minimum gap is 33.5−29.840489=3.659511 percentage points. Relative discrepancy=3.659511/34=.107633, above .05. Even allowing T∈[4999.5,5000.5] gives an envelope of 27.350760–29.844732%, with gap 3.655268/34=.107508; the discrepancy persists.

**Focus area:** D, internally stated planned sample-size/power relationships; statistical-method reproduction under C.

**Proposed review domain:** plan_material.

**Proposed relationship type:** P_P. **All relationships:** P_P. All conflicting/comparator specifications are PLAN content within one protocol. REPORT merely supplies broader trial context and is not a side of this discrepancy.

**Qualifying route:** Route A, category 4.

**Affected result or extracted value:** The printed 34% power for the planned age-under-75 analysis of the primary AF proportion, at total trial size 5000 and two-sided .01. It can affect extraction of subgroup power from the supplied prospective design material. This does not establish a difference in the report's primary outcome result or age80/sex .05 power claims.

**Why context does not resolve it:** Category4 applies: the 34% cell remains outside the full input/printed-value rounding envelope under a method tracking the rest of the same table. The table specifies a different significance level in its .05 column and a different total trial size in its4000 column, so simply reading an adjacent cell does not identify a supported 34% calculation.

**Source-grounded alternatives and missing definition:** Table 4 does not name the exact power implementation. An uncorrected two-proportion normal calculation gives 35.699810% for this cell, within the scope 5% threshold of 34%; however it gives 27.416397% for the same row's4000/.01 cell, which does not track the printed 20%. A different correction, underlying unrounded assumptions, or a different effective subgroup size might explain a distinct cell calculation, but those inputs/rules are not supplied. No preferred method, corrected power, or final disposition is proposed.

**Exact human question:** Which power calculation and underlying inputs produced34% in Table 4's age <75,total trial 5000,2p<.01 cell, and how do those rules account for the same row's20% at total trial 4000 and the remaining same-table cells?

## Excluded observations

Only apparent issues considered and not emitted are listed here; ordinary checks that reconcile remain in the relationship inventory. Each row has exactly one reason code. None is a reproduced always-register category.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p3, S010 | Printed exp(O−E÷V) lacks grouping around O−E, but adjacent text explicitly names observed−expected as the single quantity whose variance is V; the numerical output is not independently shown to use another expression. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-001 p1 versus pp5,7, S023/S024 | Any-stroke CI .76–1.53 versus .77–1.51: lower-limit printed intervals[.755,.765]/[.765,.775] touch; upper intervals[1.525,1.535]/[1.505,1.515] have gap.010/reference1.53=.00654. Both include 1. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 pp1,5, S017 | OAC mean difference .50 versus central subtraction1.63−1.14=.49: recomputed interval[.480,.500] overlaps printed[.495,.505]. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-002 p21 Table 3 and p22 Table 4, S117/S118 | Small residual diagnostic sample-size/power differences outside direct integer rounding, including original whole trial 5000/.01 power99% and female5000/.01 power75%, stay below the 5% relative discrepancy threshold; the under 75/5000/.01 cell is separately emitted. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-003 p20 §6.4.4 versus REPORT DOC-001 pp3,7, S112 | SAP says no hypothesis testing for future exploratory clinical events; report gives log-rank rate estimates/CIs but no death/stroke test P or significance claim. An estimate/CI alone does not establish that a prohibited hypothesis test was performed. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-003 pp8–9,18 versus REPORT DOC-001 p3, S103/S107 | Five-year AF-days secondary analyses are not shown in the 2.5-year report; the longer prespecified window and shorter expressly exploratory version distinguish pending follow-up from replacement/omission of an available key result. | CONTEXT_RESOLVES |
| PLAN DOC-003 pp20–21 versus REPORT DOC-001 p5, S111 | Full nonrandomized exploratory diagnosis route/OAC comparison is not reported; it is neither primary/key secondary nor claimed prespecified for an unsupplied reported number. | PERIPHERAL_COMPARISON |
| REPORT DOC-001 pp3,5, S013/S017 | Independently propagating group mean CIs would produce narrower difference CIs for AF days/OAC months under an assumed common Wald construction, but the supplied source states permutation testing without the mean/difference CI construction; every printed difference CI/P<.001 combination has coherent null exclusion. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 p3 versus DOC-004 p10, S014/S123 | “Same method” language for urgent-report delay follows log-rank discussion while the printed delay result is a single-group median/KM curve. Immediate survival-analysis context identifies the descriptive delay result; no missing-comparator RR/P is printed or extracted. | TERMINOLOGY_OR_WORDING |

## Evidence and computational limitations

Sources were preserved. No additional OCR was required by this agent. Protocol Tables 1–4 were read from fresh CPU renders of the supplied PDF, with GPU OCR only as a locator; retained main/result source-page images were visually read. Rendering provenance: PyMuPDF1.26.4,200 dpi CPU for protocol; retained images' legacy engine version unavailable. Native text/mapped derivatives were locators and transcription aids. Arithmetic used JavaScript; no Python scientific orchestration/calculation was used.

Exact log-rank reconstruction lacks O−E,V and event time inputs; permutation mean/CI reproduction lacks individual/imputed observations, simulation count and CI construction; median CI lacks its construction/event times; continuous T/ordinal trend implementations are not fully specified; separate outcome derivation and economic plans are not supplied. All such relationships were checked for their available printed logical and numeric implications and explicitly marked PASS_1_COMPLETE. No scientific coverage gap remains in this assigned scope.

