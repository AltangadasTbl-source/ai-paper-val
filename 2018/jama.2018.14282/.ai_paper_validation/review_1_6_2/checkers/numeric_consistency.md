# Numeric consistency checker

Status: COMPLETE. Runtime CODEX_THREAD_ID: 01a129b8-e16e-7732-8986-717ce7785e24. Role: numeric_consistency_reviewer. Scientific inputs: completely read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md; current source/evidence inventory; structured main mapper records before its transcription appendix; complete support mapper records. No prior findings, candidate records, decisions, or reports were used.

Scope: all counts, denominators, percentages, participant flow, treated and analyzed populations, subgroup numerators and totals, repeated count locations, numeric planned design inputs and effect-measure identity in four supplied PDFs, 144 mapped physical pages. Canonical inventory: [numeric_relationship_inventory.md](../relationships/numeric_relationship_inventory.md), N001–N104, 104 completed numeric records. H means high-flow oxygen; C means standard oxygen. Historical studies inside the PLAN bundle remain historical.

Methods: direct Poppler 25.03.0 source layout text for main article pp.1–7 and results eTable p.2; source-linked reusable native/layout records for all mapped pages; existing exact-source images of main pp.4 and 7 inspected visually. CPU; no new rendering/OCR or source modifications. All printed-input arithmetic uses half-unit intervals, including integer counts ±0.5. Percentage half-units match printed precision (one decimal ±0.05 percentage points; integer percent ±0.5). For sums, input intervals are added. Relative gap is the remaining interval gap divided by the absolute reference printed value. No model-based HR is equated with a crude event ratio. Inferential test compatibility and prospective model/outcome changes are assigned to independent statistical and cross-source specialists; all numeric source inputs are retained here.

Four qualifying findings are emitted, with repeated patterns consolidated. Ten excluded apparent observations are listed once below. Passing arithmetic belongs in the inventory. No severity, candidate identifiers, validity or disposition is assigned.

## Findings

### F-NUM-001

**Observation:** Four Table 1 count/percentage pairs do not reconcile with their printed arm denominator.

**Exact source locations and document roles:** REPORT [main article physical p.4, Table 1](../../../jama_azoulay_2018_oi_180109.pdf#page=4), headers n=388 in both columns: chronic liver disease H row; chronic kidney disease C row; postextubation randomization H and C cells. REPORT same table footnotes a–f supply definitions but no alternate denominators. Canonical relationships N017, N018, N035. Every affected location is included in this single denominator-pattern finding.

**Printed inputs:** H liver 45(13.3%); C kidney 69(20.4%); postextubation H 14(4.1%), C 18(5.3%); denominator 388 for each arm.

**Rule and calculation:** For 100 n/d, allow n and d their ±0.5 intervals, then compare the output with the printed percentage ±0.05 percentage points.

| Affected cell | Central recomputation | Recomputed half-unit interval, % | Printed percentage interval, % | Relative discrepancy |
|---|---:|---|---|---:|
| H liver | 45/388×100=11.5979% | [11.4543,11.7419] | [13.25,13.35] | 1.5081/13.3=.113388 |
| C kidney | 69/388×100=17.7835% | [17.6319,17.9355] | [20.35,20.45] | 2.4145/20.4=.118359 |
| H postextubation | 14/388×100=3.6082% | [3.4749,3.7419] | [4.05,4.15] | .3081/4.1=.075138 |
| C postextubation | 18/388×100=4.6392% | [4.5045,4.7742] | [5.25,5.35] | .4758/5.3=.089775 |

All exceed 0.05 after display precision. Other numerator/denominator percentages in Table 1 were checked; they reconcile under the same rule. Numerators with explicitly smaller denominators, such as chemotherapy 221/294, were checked against those explicitly printed denominators.

**Focus area:** A, counts and denominators.
**Proposed review domain:** statistical_results.
**Proposed relationship:** S_W; all relationships S_W.
**Qualifying route:** Route A, category 3.
**Affected result or extracted value:** Baseline liver/kidney prevalences and the proportions randomized after extubation in each arm.
**Why context does not resolve it:** This is an always-register count/denominator/percentage conflict within one display. No row-specific available-case denominator is printed; the intended alternate denominator cannot be identified from the table.
**Alternatives:** Smaller available-case denominators might underlie the percentages, or counts/percentages might represent different source fields. A denominator near 338–339 would approximately explain these percentages, but the source does not state it. This is an inferred possible explanation, not a supplied denominator or proposed correction.
**Exact human question:** Which denominators and count/percentage pairs should be used for high-flow liver disease, standard-oxygen kidney disease, and postextubation randomization in both groups, and were any row-specific missing-data denominators omitted from Table 1?

### F-NUM-002

**Observation:** A post hoc paragraph assigns counts and pooled-population percentages to two randomized arms.

**Exact source locations and document roles:** REPORT [main article physical p.6, Post Hoc Outcomes, first paragraph](../../../jama_azoulay_2018_oi_180109.pdf#page=6). REPORT [p.5, Patients](../../../jama_azoulay_2018_oi_180109.pdf#page=5) and [p.3, Figure 1](../../../jama_azoulay_2018_oi_180109.pdf#page=3) establish randomized 389/389 and analyzed 388/388, pooled 776. Relationships N059, N008, N009; corresponding main mapper S059.

**Printed inputs:** “In the overall population,” vasopressors and renal replacement therapy needed in 153 patients(19.7%) randomized to H and 31 patients(4%) randomized to C; no statistical difference between groups. Both analysis arms 388; randomized arms 389.

**Rule and calculation:** H 153/388=39.4330%; half-unit interval[39.2535,39.6129]% versus printed 19.7 interval[19.65,19.75]%, relative gap 19.5035/19.7=.990027. C 31/388=7.9897%; half-unit interval[7.8507,8.1290]% versus printed integer 4 interval[3.5,4.5]%, relative gap 3.3507/4=.837677. Using 389 randomized denominators instead of 388 does not remove either discrepancy. Conversely,153/776=19.7165% with half-unit interval[19.6394,19.7937]% and 31/776=3.9948% with interval[3.9279,4.0619]%, both overlapping printed percentages. The count order could therefore belong to two therapies in the overall population rather than to two randomized groups; the printed sentence explicitly attaches them to the groups.

**Focus area:** A, counts and denominators.
**Proposed review domain:** statistical_results.
**Proposed relationship:** S_W; all relationships S_W.
**Qualifying route:** Route A, category 3.
**Affected result or extracted value:** Group-specific vasopressor and renal replacement counts/risks during follow-up and their attribution to the randomized intervention.
**Why context does not resolve it:** An always-register within-paragraph count/denominator/percentage conflict is reproduced. The pooled denominator reproduces the percentages, but does not identify which therapies and arm-specific quantities the sentence is reporting.
**Alternatives:** 153 and 31 might be overall counts for vasopressors and renal replacement, respectively, with arm labels attached in the sentence; alternatively they could be genuine arm counts with pooled percentages. The source provides no independent arm-by-therapy table to distinguish them. The statement of no group difference is retained; it is not recomputed under an assumed event cross-tabulation.
**Exact human question:** Do 153(19.7%) and 31(4%) describe vasopressors and renal replacement therapy in the entire 776-patient population, or separate randomized groups, and what are the arm-specific therapy counts and denominators?

### F-NUM-003

**Observation:** Figure 3 binary subgroup counts leave unreconciled denominators and events compared with its “All patients” rows.

**Exact source locations and document roles:** REPORT [main article physical p.7, Figure 3A and 3 B](../../../jama_azoulay_2018_oi_180109.pdf#page=7), PaO2:FIO2<200 and≥200 rows in both arms/both panels; hematologic malignancy No and Yes rows in H in both panels; All patients rows. REPORT [p.4, Table 1, hematologic malignancy](../../../jama_azoulay_2018_oi_180109.pdf#page=4) confirms 167 H and 181 C among 388/arm. REPORT [p.3, Statistical Analysis](../../../jama_azoulay_2018_oi_180109.pdf#page=3) states no participants excluded from analyses because of missing/incomplete data; it gives no subgroup-specific available-case rule. Numeric relationships N072, N076; main mapper S033, S034, S041, S042, S046, S047, S054, S055.

**Printed inputs:** All patients H 138/388, C 140/388 deaths; H 150/388, C 170/388 IMV. PaO2:FIO2 subgroups: H denominators 237+65, C 251+35; deaths H 99+16, C 95+10; IMV H 99+27, C 117+13. Hematologic malignancy H denominators 199+167, deaths 66+64, IMV61+78. The same subgroup denominators recur in both panels.

**Rule and calculation:** Sum the half-unit intervals for each two-category partition; compare with the half-unit All patients value. This consolidates the same unaccounted subgroup-population pattern across both panels.

| Displayed comparison | Central subgroup sum versus All patients | Sum interval | All-patient interval | Relative gap |
|---|---|---|---|---:|
| PaO2:FIO2 H denominator, panels A and B | 237+65=302 versus 388 | [301,303] | [387.5,388.5] |84.5/388=.217784|
| PaO2:FIO2 C denominator, panels A and B |251+35=286 versus 388|[285,287]|[387.5,388.5]|100.5/388=.259021|
| PaO2:FIO2 H deaths, panel A |99+16=115 versus 138|[114,116]|[137.5,138.5]|21.5/138=.155797|
| PaO2:FIO2 C deaths, panel A |95+10=105 versus 140|[104,106]|[139.5,140.5]|33.5/140=.239286|
| PaO2:FIO2 H IMV, panel B |99+27=126 versus 150|[125,127]|[149.5,150.5]|22.5/150=.150000|
| PaO2:FIO2 C IMV, panel B |117+13=130 versus 170|[129,131]|[169.5,170.5]|38.5/170=.226471|
| Hematologic malignancy H denominator, panels A and B |199+167=366 versus 388|[365,367]|[387.5,388.5]|20.5/388=.052835|
| Hematologic malignancy H IMV, panel B |61+78=139 versus 150|[138,140]|[149.5,150.5]|9.5/150=.063333|

H No hematologic malignancy would be 388−167=221, with subtraction interval[220,222], whereas printed 199 allows[198.5,199.5]; gap 20.5/199=.103015. The other subgroup partitions (ICU timing, oxygen flow, catecholamines, unknown diagnosis) reproduce both all-patient denominators and event counts. Standard-arm hematologic and H hematologic-death subtotals also differ numerically, but their relative half-unit gaps do not exceed 0.05; they are recorded once in excluded observations.

**Focus area:** A, counts and denominators.
**Proposed review domain:** statistical_results.
**Proposed relationship:** S_W; all relationships S_W.
**Qualifying route:** Route A, category 3.
**Affected result or extracted value:** PaO2:FIO2 and hematologic-malignancy subgroup analysis populations and their day-28 death/IMV event counts.
**Why context does not resolve it:** Counts within the same result display do not reconcile above the prescribed threshold. Binary partitions are printed alongside all-patient totals; the caption supplies no missing-covariate stratum, restricted population definition, or accounting for the absent patients/events.
**Alternatives:** The partitions may be available-case analyses with missing subgroup-defining variables, despite the report's general no-exclusion statement, or may represent a restricted diagnostic population. This could explain some count deficits but is not a supplied definition. A count transcription or alternate subgroup definition is another possibility. No raw-data inference about which patients are missing is made.
**Exact human question:** Which analysis populations and missing-covariate rules underlie the PaO2:FIO2 and hematologic-malignancy subgroup rows, and how do their displayed denominators and events account for the all-patient totals in Figure 3?

### F-NUM-004

**Observation:** The same all-patient IMV counts are accompanied by contrasting HR directions in Table 2 and Figure 3B.

**Exact source locations and document roles:** REPORT [main article physical p.5, Table 2, invasive mechanical ventilation](../../../jama_azoulay_2018_oi_180109.pdf#page=5), REPORT [p.6, Secondary Outcomes, first paragraph](../../../jama_azoulay_2018_oi_180109.pdf#page=6), and REPORT [p.7, Figure 3B, All patients row and favors labels](../../../jama_azoulay_2018_oi_180109.pdf#page=7). REPORT [p.4, Statistical Analysis](../../../jama_azoulay_2018_oi_180109.pdf#page=4) describes high-flow versus standard-oxygen Cox effect estimates for the subgroup display. Relationships N065, N077; main mapper S015, S056, S057.

**Printed inputs:** H 150/388 andC170/388 IMV in both displays. Table 2 and narrative cause-specific HR0.85(95%CI0.68–1.06). Figure 3B All patients HR1.17(0.94–1.46). Figure labels HR<1 as favoring H andHR>1 as favoring C. There is no explicit alternative numerator/reference statement in its caption.

**Rule and calculation:** Compare matched all-patient results and direction/reference labels, not Cox versus crude ratios. Table 2 HR interval from display precision[.845,.855]; Figure 3 HR[1.165,1.175]; interval gap.310, relative gap.310/.85=.364706>0.05. Lower limits[.675,.685] versus[.935,.945] have relative gap.250/.68=.367647; upper limits[1.055,1.065] versus[1.455,1.465] have relative gap.390/1.06=.367925. Inverting Table 2 gives 1/.85=1.17647 and reciprocalCI[1/1.06,1/.68]=[.94340,1.47059], approximately matching Figure 3. This is a diagnostic about contrast reversal, not proof of the computation used and not a proposed correction.

**Focus area:** B, direction and estimate identity; C, which Cox contrast produces the reported number.
**Proposed review domain:** statistical_results.
**Proposed relationship:** S_W; all relationships S_W.
**Qualifying route:** Route B.
**Affected result or extracted value:** The all-patient day-28 IMV hazard ratio and its treatment/reference direction, which could be extracted as 0.85 or 1.17.
**Why context does not resolve it:** The printed population, event counts and outcome match, while HR directions reverse and Figure 3 uses the same favors convention as a high-flow/standard contrast. A different Cox estimand or reference coding is not defined alongside the figure. Reversing reference coding would also require reconciling its favors labels.
**Alternatives:** Figure 3 could reverse treatment coding, or use a different hazard/competing-event model from the cause-specific model explicitly named in Table 2. The source does not specify a distinct all-patient model in Figure 3. No crude event ratio is used to demand numerical equality with a Cox estimate.
**Exact human question:** What event model and treatment/reference coding produced Figure 3B's all-patient HR1.17(0.94–1.46), and how should its direction and favors labels be reconciled with Table 2 and the narrative HR0.85(0.68–1.06)?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p.3 sample-size paragraph; PLAN DOC-002 pp.72,90–91,103 | Report 779 total versus 389 each(778) and plan 778: input sum interval[777,779] and printed 779 interval[778.5,779.5] overlap; exact copies 778/779 also touch at 778.5. Relative gap 0. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 pp.1,6 respiratory-rate CI upper limit | Upper limits−.2 and−.3: half-unit intervals[−.25,−.15] and[−.35,−.25] touch; gap 0. Both lower limits−3.2 and point−1.8 match. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p.5 Table 2 day 28 mortality and p.7 Figure 3A All patients | HR.98 versus 1.02: intervals[.975,.985],[1.015,1.025], gap.030/.98=.030612. Limits.77 versus.81 relative gap.030/.77=.038961;1.24 versus 1.29 gap.040/1.24=.032258. All≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p.7 Figure 3 hematologic rows | C denominators 198+181=379 vs 388 gap 7.5/388=.01933; H deaths 66+64=130 vs 138 gap 6.5/138=.04710; C deaths 72+65=137 vs 140 gap 1.5/140=.01071; C IMV89+77=166 vs 170 gap 2.5/170=.01471. Each is≤.05 under half-unit rule; qualifying other subgroup deficits are in F-NUM-003. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 pp.5,7 Table 2 infection and Figure 3 subgroup effects | Infection 39/41=.9512 differs from printed cause-specific HR1.01; some Figure 3 HRs differ from crude event risk ratios. Cox effects use time-at-risk and are not stated to be crude event RRs; no quantity identity is established solely by such differences. | MODEL_VERSUS_CRUDE |
| REPORT DOC-001 pp.1,5,6; REPORT DOC-003 pp.2,4 | Median group differences−1(respiratory),31(oxygenation),2(ICU stay),−3(hospital stay) differ from printed mean differences−1.8,19.5,.6,−2. Table 2 footnote expressly distinguishes means from displayed medians; graph points are not labeled as medians. | CONTEXT_RESOLVES |
| REPORT DOC-001 p.6 Figure 2 vertical-axis title and ticks | Axis says mortality probability,% while ticks are 0,.1,.2,.3,.4. Common probability versus percent scale is immediately clear from figure endpoints and trial risks; no printed event count changes. | NOTATION_OR_TYPOGRAPHY |
| PLAN DOC-002 pp.23–24,29,94 historical rationale | Historical eligibility ratio<300 in narrative versus<30 in Table 5; historical propensity “lower day 28 survival” wording after crude lower mortality. These are supplied background comparisons, not a current primary/key secondary result or relied-on planned decision rule. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 pp.3,6,90,95,97,107; REPORT DOC-001 pp.1,2 | Planned/reported site counts 26,30,31,32 and recruitment calendars differ across versions; no analyzed population or decision rule changes through these administrative counts. | PERIPHERAL_COMPARISON |
| REPORT DOC-001 p.4 Table 1 Charlson footnote | Footnote 19 categories/nominal 19–114 range accompanies arm medians 5 and IQR 3–7; this background comorbidity-scale description does not supply the trial endpoint scale or an inferential interval and does not change extraction of the clear baseline medians. | OUT_OF_FOCUS |

## Completion and limitations

Counts: 4 direct-source documents;144 mapped pages reviewed through the disjoint mapper union;104 canonical N relationships;4 findings;10 excluded observations;0 scientific-coverage gaps. All display count pairs, explicit denominators, row/subgroup totals and matching trial counts were checked; compound records retain all mapped values and cross-references.

Limits: supplied raw individual time-to-event data are unavailable; no mechanical Cox recalculation is asserted. Supplementary graph points/bar summaries and significance-symbol definitions are not numerically specified, so graphical geometry is not treated as a printed-value calculation. PLAN pp.127–128 historical Results cells are clipped at the source boundary; all visible material was reviewed. No Office/CSV/workbook source exists. These are source/reproduction limits, not omitted scientific units. Prospective endpoint/model/design and interval-versus-test comparisons are retained for the disjoint specialist stages.

Artifacts: relationships/numeric_relationship_inventory.md and checkers/numeric_consistency.md. All source and reused assets preserved.

