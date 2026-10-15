# Numeric consistency review — main-paper shard

Scope: N001–N113, all113 main-paper relationships, REPORT DOC-001 PDF pages1–10. The complete per-relationship checks are in relationships/numeric_main_inventory.md. Counts, denominators, totals, event hierarchies, repeated values and effect-measure identity were checked. All applicable percentage comparisons allow half-unit intervals. No old checker, candidate, screening or report conclusion was used. Direct source PDF p6 was rendered and visually inspected using PyMuPDF1.26.4 CPU (preprocessing/numeric-main-p6.png); current native extraction and historical layout assets served as locators.

Main-shard findings:1. Excluded observations:7. No count target applied.

### F-NUM-001

**Statement:** The serious-adverse-event hierarchy in Table 2 contains counts that do not reconcile with its printed parent totals after display precision is allowed: the levodopa top-level categories sum 143 versus 126 overall serious events, and the placebo infection subtypes sum 52 versus 44 infections. These are consolidated as one repeated event-hierarchy count pattern in one display.

**Exact source locations and document roles:** REPORT main article [PDF p6, Table 2, serious-adverse-event headings and all top-level rows, and placebo Infection row and its six subtypes](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6). REPORT main article [PDF p6, Adverse Events narrative](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) corroborates126 serious events for levodopa and 44 infections for placebo; it supplies no conflicting alternative total. All compared inconsistent quantities are within REPORT Table 2, so the proposed relationship is S_W. Relationships N068–N093 and N112 supply the corresponding mapping records.

**Printed inputs:** Levodopa top-level serious categories: infection 55; stroke16; major extracranial bleeding5; cardiac event12; cancer/malignant neoplasm4; trauma4; kidney failure6; epileptic seizure3; deep vein thrombosis/pulmonary embolism3; electrolyte disorder2; fracture1; traumatic intracerebral hemorrhage0; other32. Column heading n=126. Placebo infection parent44; pulmonary17, urinary tract15, abdominal7, meningoencephalitis/encephalitis2, unspecified2, other9. The table is headed “Events, No.” Subtypes of stroke, cardiac events, and trauma are not double-counted in the top-level sum.

**Rule and calculation:** Compare an event total with the sum of its displayed categories. Levodopa55+16+5+12+4+4+6+3+3+2+1+0+32=143. With thirteen displayed integer inputs each allowed±0.5, recomputed interval=[136.5,149.5]; printed126 interval=[125.5,126.5]; gap=10; relative discrepancy=10/126=0.079365>0.05. Placebo infection 17+15+7+2+2+9=52. Six half-unit inputs give[49,55]; printed44 gives[43.5,44.5]; gap=4.5; relative discrepancy=4.5/44=0.102273>0.05. Symmetric intervals are conservative because even a printed zero input is allowed−0.5 here; restricting to nonnegative counts cannot remove either discrepancy. No percentage or model assumption is needed.

**Focus area:** A (counts and totals).

**Proposed review domain:** statistical_results.

**Qualifying route:** Route A, category 3.

**Affected result or extracted value:** The levodopa total serious-adverse-event count126 and the placebo infection-event count44, compared with their displayed component counts; an extractor could copy either the parent or category-derived total.

**Why context does not resolve it:** Route A, category 3 is the always-register counts-within-one-display category. “Events, No.” distinguishes event counts from affected participants, and the hierarchy does not explain why the categories exceed their parents. The narrative repeats the parent totals without supplying a reconciliation. The missing classification definition does not remove the printed count comparison.

**Alternative source-grounded interpretations:** The same serious event may have been assigned more than one top-level diagnosis, or the same infection may involve more than one anatomical site. The display does not state mutual exclusivity or a multiple-classification rule, so those possibilities are not asserted as facts. A different counting unit for parent totals and categories is another possibility, although the common “Events, No.” heading does not identify such a distinction. Some parent or component counts may require clarification; no replacement is proposed. The placebo overall serious sum 139 versus 129 and levodopa infection sum 59 versus 55 are below the display-precision inclusion threshold and are listed separately as excluded observations.

**Exact human question:** Do the Table 2 serious-event and infection categories count mutually exclusive events or multiple classifications of the same events, and what counting definition reconciles the levodopa category sum 143 with 126 serious events and the placebo infection-subtype sum 52 with 44 infections?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT main article PDF p6 Table 2, levodopa Infection and six subtypes, N069–N075 | Six subtype counts sum 59 versus parent55. Half-unit sum[56,62] versus parent[54.5,55.5] has gap0.5;0.5/55=0.009091≤0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main article PDF p6 Table 2, placebo top-level serious-event rows, N068–N093 | Top-level sum 139 versus 129. Half-unit sum[132.5,145.5] versus[128.5,129.5] has gap3;3/129=0.023256≤0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main article PDF p4 Table 1, age≥80 row, N023 | Label “Median age≥80y” accompanies90(29.3%) and 112(37.0%); adjacent count-percent layout makes the age-category meaning immediate. Both percentages reconcile to307/303. | TERMINOLOGY_OR_WORDING |
| REPORT main article PDF pp1,2,5,6 primary FMA summaries, N005,N008,N047,N067 | Median68−64=4 differs from adjusted mean difference−0.90. The source explicitly distinguishes medians from a baseline-adjusted regression coefficient; no crude/adjusted identity is asserted. | MODEL_VERSUS_CRUDE |
| REPORT main article PDF p5 rehabilitation exposure and Figure2, N065,N067 | Exposure-specific participant counts and exact per-panel n are absent, but no printed count conflicts. Missing denominators alone do not supply a numeric finding. | CONDITIONAL_OR_UNREPORTED |
| REPORT main article PDF p4 Table 1, mRS categories, N051–N056 | Rounded category percentages sum 100.2%/100.1%; counts sum 307/303 exactly. The percentage-sum half-unit intervals include100%, so gap0. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main article PDF p1 intervention summary versus p3 phase schedule, N002,N013 | Abstract summarizes dosing as3times daily for39days; detailed schedule makes dose escalation, full-dose phase and taper explicit within the report. This is the regimen shorthand rather than an unresolved count/denominator value. | TERMINOLOGY_OR_WORDING |

## Limitations

No main-paper scientific coverage gap remains. Exact individual plotted values, exposure-specific denominators, and unprinted model details are not recoverable from the supplied article alone. They were not invented. Statistical sample-size, model/test logic, and PLAN–REPORT comparisons are independently assigned; numeric checks do not substitute crude summaries for adjusted effects. The event-category classification rule remains the bounded missing definition in F-NUM-001.
