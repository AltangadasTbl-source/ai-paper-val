# Numeric consistency review

Stage: numeric_consistency_reviewer. Runtime agent: root/numeric_checker. Fresh complete review of DOC-001 REPORT pp.1–12, DOC-002 REPORT pp.1–20, DOC-003 PLAN pp.1–7. The stable inventory `relationships/numeric_relationship_inventory.md` records complete coverage of N001–N059 and N101–N118, 77 grouped relationships with every member. All counts, denominator pairs, partitions, repeated values, risk-set definitions and numeric effect identities were considered. Statistical-family checks retain outcome/time/population/model alignment; detailed inferential logic remains independently covered by statistical specialists.

One finding meets the inclusion threshold after self-screening. No desired finding count was applied. The 17 excluded observations below have exactly one reason code each. Source PDFs control all transcriptions; direct Poppler layout extraction was used to confirm main Table2 and supplement eTable3. Main physical p7 was visually read from the freshly rendered source image `extraction/main_direct_page_007.png`. No external sources, legacy decisions or raw-data assumptions were used.

## Findings

### F-NUM-001

**Title:** Five nonfatal endpoint absolute eight-year risk differences do not reconcile with the displayed cumulative incidences under the table's stated subtraction.

**Compared exact source locations and document roles:** REPORT DOC-001 [Table2, physical PDF p7](../../../jama_aminian_2019_oi_190103.pdf#page=7), heart failure, coronary artery disease, cerebrovascular disease, nephropathy and atrial fibrillation rows, their two cumulative-incidence columns, absolute eight-year risk-difference column and footnotes a/b. REPORT DOC-002 [eTable5, physical PDF p7](../../../joi190103supp1_prod.pdf#page=7), corresponding Year8 rows, corroborates the printed incidence values; it is corroboration rather than an additional conflicting relationship. REPORT DOC-001 [Abstract p1](../../../jama_aminian_2019_oi_190103.pdf#page=1) identifies all seven secondary outcomes in its results. No PLAN location is a side of this comparison.

**Printed inputs, rule and calculation:** Footnote a defines the absolute risk contrast as “nonsurgical control group − metabolic surgery” for the eight-year absolute risks and identifies 95% bootstrap CIs, 1000 samples. Footnote b separately identifies HRs/P values as adjusted Cox quantities. Every affected incidence and point difference is printed to one decimal. Allow each risk ±0.05 percentage points, giving the subtraction ±0.10; allow each printed ARD ±0.05. The allowable intervals are disjoint in all five rows.

| Outcome; initial surgery/control risk set | Surgery incidence% | Control incidence% | Control−surgery from displayed centers, percentage points | Allowable subtraction interval | Printed ARD% | Allowable printed ARD interval |
|---|---:|---:|---:|---|---:|---|
| Heart failure;2049/10093 |6.8|18.9|12.1|12.00–12.20|12.9|12.85–12.95|
| Coronary artery disease;2050/10331 |7.9|11.6|3.7|3.60–3.80|4.2|4.15–4.25|
| Cerebrovascular disease;2245/11077 |4.1|5.6|1.5|1.40–1.60|1.8|1.75–1.85|
| Nephropathy;1937/9190 |6.1|16.3|10.2|10.10–10.30|11.1|11.05–11.15|
| Atrial fibrillation;2135/10734 |7.9|13.6|5.7|5.60–5.80|6.5|6.45–6.55|

The primary16.9,secondary10.6,mortality7.8 differences in the same table reconcile with their incidence pairs. Printed affected ARD CIs are respectively10.4–15.1,1.9–6.8,−0.03–3.4,8.8–13.6,4.4–8.7; those intervals are retained as reported and are not reconstructed by subtracting separate marginal CI bounds. The table and eTable5 give the same outcome-specific incidences and time; no population/time mismatch accounts for the point differences.

**Relationship inventory cross-reference:** N105 and main Table2 S004–S008 (corroboration S104).

**Focus area:** A/B: numeric absolute-risk contrast identity and estimate interpretation.

**Proposed review domain:** statistical_results.

**Proposed primary relationship:** S_W; **All relationships:** S_W. The supplied results supplement confirms one side, so it does not add S_C.

**Affected result or extracted value:** Eight-year absolute risk reductions for heart failure, coronary artery disease, cerebrovascular disease, nephropathy and atrial fibrillation, with their associated reported bootstrap intervals. A downstream extractor could take the ARD-column points or subtract the printed same-row risks and obtain distinct values.

**Why context does not resolve it:** The discrepancy is a repeated five-outcome pattern, exceeds display precision, and is not an isolated obvious symbol/decimal slip. The column title and footnote specify an eight-year absolute-risk subtraction, but provide no distinct adjusted-risk, composite-with-death, bootstrap-average, or alternative population definition for those point estimates. The HRs are explicitly adjusted and separate; that explanation does not automatically extend to the ARD column. Neither the adjacent risks nor the contrast column can be selected as the intended extracted result at once. These are outcome results reported among the abstract's secondary outcomes, rather than peripheral contributor counts.

**Source-grounded alternative interpretations and missing definition:** The incidence columns may be the intended inputs to the ARD subtraction; alternatively, the ARD column may come from a separate risk estimation or bootstrap point-summary procedure whose identity is not described. The package does show outcome-or-death *rates* in eTable4, but those rates are a separate person-time quantity and do not establish an alternative eight-year absolute-risk point definition here. No explanation of the cause is asserted.

**Exact human question:** For each of the five listed outcomes, which eight-year absolute-risk contrast should be extracted, and what risk inputs/population/point-estimation definition produce the printed ARD and its bootstrap interval?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-001 p3 Figure1,N003 | Exclusion-category sums657/67489 exceed unique excluded470/49676; caption explicitly states multiple criteria can apply. | CONTEXT_RESOLVES |
| DOC-001 pp4–5,N006 and N013/N015/N017/N018/N043 | Whole-percent prose and one-decimal baseline-table quantities agree when their distinct display intervals are allowed. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p5 Table1 men eligible-control cell,N009 |18895/39267=48.119% versus printed48.2%; the exhaustive sex counts give a clear denominator and isolate a small baseline display slip. Intended fraction is immediately recoverable. | CONTEXT_RESOLVES |
| DOC-001 p6 Table1 UACR eligible-control missing cell,N037 |14665/39267=37.3469% versus37.4%; exact count and fixed column N identify the fraction immediately. | CONTEXT_RESOLVES |
| DOC-002 p5 eTable3 biguanides surgery,N103 |1530/2287=66.8999% versus67.9%; isolated baseline medication percentage has fixed N and printed count, permitting immediate recovery; it does not change a primary/key-secondary outcome or population. | CONTEXT_RESOLVES |
| DOC-001 pp5–6 standardized-difference footnote/cells,N059 | Footnote calls values absolute; displayed negative entries consistently retain group direction. Signed/absolute convention is immediately identifiable; means and pooled SDs needed for continuous-value reconstruction are not printed. | TERMINOLOGY_OR_WORDING |
| DOC-001 pp5/7–8 nephropathy,N023/N049 | Baseline nephropathy history191/1219 alone does not reproduce initial risk set1937/9190; explicit additional baseline eGFR<60 and dialysis exclusions establish that history alone is not the denominator rule. | CONTEXT_RESOLVES |
| DOC-001 pp1/4/7,N045–N047;DOC-002 pp6–7,N104/N105 | Crude cumulative event fractions differ from eight-year KM incidence, Cox HR and cause-specific rate; those are explicitly distinct time-to-event/model quantities. | MODEL_VERSUS_CRUDE |
| DOC-001 p7,N050 |29.1−8.7=20.4 versus reported20.3 kg; input intervals yield20.30–20.50 and printedcontrast20.25–20.35, with nonempty overlap. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 pp7/9 and DOC-002 p12,N050/N107 | Main95% and supplementBonferroni98.8% weight/HbA1c interval displays have distinct stated coverage; kg versus percentage weight-loss contrasts have different scales. | CONTEXT_RESOLVES |
| DOC-002 p12,N107 | Pounds/kg conversions and some nutritional CIs collapse to the same one-decimal endpoints; allowed rounding intervals contain the points and permit conversion. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 Table1 missingness versus DOC-002 p13,N108 | Baseline available measurements differ from distinct patients with follow-up measurements after each time threshold; these are distinct windows and repeated-observation populations. | PERIPHERAL_COMPARISON |
| DOC-001 p6 medication baselineN11435 versus DOC-002 p14 timezeroN11433,N109 | Time-point medication contributor count differs by2 from matched cohort N; no replacement of the endpoint analysis population is stated, and this is a peripheral longitudinal contributor comparison. | PERIPHERAL_COMPARISON |
| DOC-001 p7 early adverse events versus DOC-002 p15 intervention KM,N053/N110 |90-day crude intervention proportions differ from1/2/5/8-year cumulative incidences; windows and estimators differ. | CONTEXT_RESOLVES |
| DOC-002 p20,N113 | HR-based E-values cannot be uniquely regenerated without the conversion/estimation formula; package does not supply that formula. Numeric ordering and paired directions reconcile. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 pp3/6,N115/N117;DOC-002 p18,N112 | Plan sentence reverses one-to-five matching orientation, whereas planp6 and actual cohort clearly identify1surgery:5controls; graphical5:1/10:1 ratio notation is reciprocal orientation with readily resolved meaning. | TERMINOLOGY_OR_WORDING |
| DOC-001 pp9–11 historical examples,N058;DOC-002 pp2–4 diagnosis identifiers,N101/N102 | Historical-study numbers and diagnosis/procedure codes are not current-cohort event quantities; a raw-data/code-validity audit is outside this quantitative consistency assignment. | OUT_OF_FOCUS |

## Scope completion and limitations

All77numeric groups and every member were checked. Participant flow, categorical partitions, medication-class partitions, event counts, endpoint risk sets, repeated counts and numeric effect identity are covered in the stable inventory. 138 three-column Table1 count/percentage cells were arithmetically inspected, plus all BP missingness pairs,24supplement medication pairs,80risk counts,120measurement availability counts,48outcome cumulative-incidence points,24intervention points,52longitudinal effect triplets and ancillary modeled quantities. All points retained their own outcome/time/group/scale/model keys.

Limitations: no raw data, person-time totals, exact unannotated graph values or fitted-model covariance is supplied. These limit independent reconstruction of modeled estimates; they do not omit a supplied numeric relationship. Direct and reused sources were preserved. Findings1; excluded observations17; scientific coverage gaps0.
