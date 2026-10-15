# Statistical Pass 1 — Main-Paper Shard

Runtime agent: /root/stat1_main; fresh gpt-6.1-sol/high. Exact scope: DOC-001 main REPORT, physical PDF pages 1–14; MAIN001–MAIN116; S001–S110. All 270 estimate–95% interval tuples and 30 omnibus tests reviewed; all 27 NNT and 63 SMD tuples included. Findings: 6 consolidated patterns. Excluded observations: 7. Each relationship is PASS_1_COMPLETE. This part does not adjudicate candidates.

Read completely: QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md. Used current fresh main map, supplied main PDF native text and exact original rendered source pages; all tables and cited signs/order on pages 9–11 visually confirmed. No web or old review conclusions used. Supplement statistical rows and plan-internal relationships are disjoint peer assignments. Links below target the supplied main PDF. All compared locations have role REPORT; proposed primary relationship S_W and all relationships S_W.

### F-ST1-001

A Table 2 NNT point lies beyond its printed confidence interval.

- Exact locations and roles: REPORT [main PDF p. 9](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), Table 2, pain intensity at 12 months, health coach vs painTRAINER NNT column; see MAIN085 derived-family record S038.
- Focus area: B.
- Proposed review domain: statistical_results.
- Proposed relationship type: S_W; all relationships: S_W.
- **Qualifying route:** Route A, category 1.
- Printed values, rule and calculation: The tuple is 63 (95% CI, 18–38). A confidence interval must contain its point estimate. Here 63 > 38. Even half-unit intervals leave the point at least 62.5 and the upper endpoint at most 38.5, a gap of 24 (24/63 = 0.381). Category 1 is not screened by display precision.

- **Affected result or extracted value:** Health coach vs painTRAINER NNT for ≥30% pain-intensity improvement at 12 months.
- **Why context does not resolve it:** The printed point and interval fail the category-1 containment rule; reconstructing a possible intended endpoint does not resolve which interval to extract.
- Alternatives and missing definitions: A substituted interval endpoint, a point attached to another row or a differently derived interval could explain the display; no replacement value is inferred.
- Exact human question: What point estimate and 95% interval should a reader use for the 12-month pain-intensity health-coach vs painTRAINER NNT?

### F-ST1-002

Repeated Table 3 SMD points lie outside their printed intervals.

- Exact locations and roles: REPORT [main PDF p. 10](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, severity 12 months, intensity 12 months, interference 12 months, physical functioning 6 and 12 months; REPORT [main PDF p. 11](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11), Table 3 continuation, PGIC–pain at 12 months. Derived-family records: S056, S065, S074, S089, S092, S101.
- Focus area: B.
- Proposed review domain: statistical_results.
- Proposed relationship type: S_W; all relationships: S_W.
- **Qualifying route:** Route A, category 1.
- Printed values, rule and calculation: Fourteen printed tuples are listed below. For containment, compare the point with both interval endpoints; it lies beyond both in each tuple. Sorting the physical-function endpoints still does not contain the point. Examples: severity 12-month painTRAINER vs usual care −0.25 < −0.24; physical 6-month painTRAINER vs usual care 0.15 > 0.09; PGIC–pain 12-month painTRAINER vs usual care −0.55 < −0.50. These are direct category-1 observations without inferential-method assumptions; display precision cannot screen them.
| Outcome/time | Contrast | Printed SMD (95% CI) |
|---|---|---|
| Severity 12 mo | painTRAINER vs usual care plus | -0.25(-0.24 to 0.01) |
| Severity 12 mo | health coach vs usual care plus | -0.36(-0.35 to-0.12) |
| Intensity 12 mo | health coach vs usual care plus | -0.27(-0.26 to-0.12) |
| Interference 12 mo | painTRAINER vs usual care plus | -0.26(-0.25 to 0.01) |
| Interference 12 mo | health coach vs usual care plus | -0.37(-0.36 to-0.11) |
| Physical 6 mo | painTRAINER vs usual care plus | 0.15(0.09 to-0.06) |
| Physical 6 mo | health coach vs usual care plus | 0.02(-0.03 to-0.18) |
| Physical 6 mo | health coach vs painTRAINER | 0.22(0.16 to 0.05) |
| Physical 12 mo | painTRAINER vs usual care plus | 0.20(0.18 to-0.03) |
| Physical 12 mo | health coach vs usual care plus | 0.07(0.04 to-0.16) |
| Physical 12 mo | health coach vs painTRAINER | 0.27(0.25 to 0.09) |
| PGIC pain 12 mo | painTRAINER vs usual care plus | -0.55(-0.50 to 0.05) |
| PGIC pain 12 mo | health coach vs usual care plus | -0.57(-0.54 to-0.08) |
| PGIC pain 12 mo | health coach vs painTRAINER | -0.29(-0.25 to 0.14) |

- **Affected result or extracted value:** The fourteen standardized-effect points or intervals listed below, across severity, intensity, interference, physical functioning and PGIC–pain.
- **Why context does not resolve it:** The category-1 point-containment failure remains under either printed or sorted physical-function endpoint order; the immediate table does not identify an extractable replacement.
- Alternatives and missing definitions: Endpoints or point estimates might have been attached to different contrasts or time points. The SMD CI construction is not stated sufficiently to reconstruct replacements; no reordering or replacement is performed.
- Exact human question: Which SMD point and 95% interval belong together for each listed outcome, time point and contrast?

### F-ST1-003

The social-role and physical-function SMD interval endpoints descend throughout Table 3.

- Exact locations and roles: REPORT [main PDF p. 10](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, social-role functioning and physical functioning, all three time points and all three SMD columns: S077, S080, S083, S086, S089, S092.
- Focus area: B.
- Proposed review domain: statistical_results.
- Proposed relationship type: S_W; all relationships: S_W.
- **Qualifying route:** Route B.
- Printed values, rule and calculation: All eighteen intervals in the table below print their first limit above their second. For example, social role 3-month painTRAINER vs usual care is 0.12 (0.23 to 0.11): lower-limit rounding range [0.225,0.235] remains above upper-limit range [0.105,0.115], minimum order gap 0.110; relative to 0.23 this is 0.478. The smallest remaining order gap is physical 3-month health coach vs painTRAINER, 0.22 to 0.15: minimum gap 0.060, relative 0.273. Every row exceeds display tolerance. Reversing endpoint order is numerical interval reading rather than a symbol or wording slip.
| Outcome/time | painTRAINER vs usual care | Health coach vs usual care | Health coach vs painTRAINER |
|---|---|---|---|
| Social 3 mo | 0.12(0.23 to 0.11) | 0.01(0.12 to-0.00) | 0.20(0.29 to 0.19) |
| Social 6 mo | 0.18(0.23 to 0.05) | 0.06(0.11 to-0.06) | 0.26(0.30 to 0.15) |
| Social 12 mo | 0.19(0.21 to 0.01) | 0.07(0.09 to-0.10) | 0.27(0.28 to 0.12) |
| Physical 3 mo | 0.09(0.16 to 0.07) | -0.02(0.05 to-0.04) | 0.16(0.22 to 0.15) |
| Physical 6 mo | 0.15(0.09 to-0.06) | 0.02(-0.03 to-0.18) | 0.22(0.16 to 0.05) |
| Physical 12 mo | 0.20(0.18 to-0.03) | 0.07(0.04 to-0.16) | 0.27(0.25 to 0.09) |

- **Affected result or extracted value:** The ordered lower and upper limits for all eighteen social-role/physical-function standardized-effect intervals.
- **Why context does not resolve it:** Although descending order is visible, the surrounding table also contains incompatible SMD points and formulas (separate findings), so sorting does not establish which interval belongs to which effect. This bears directly on extraction of confidence limits.
- Alternatives and missing definitions: The endpoints might be globally reversed, or columns/limits may be misattached; sorting alone cannot address physical-function containment. No preferred CI method is proposed.
- Exact human question: What are the lower and upper SMD confidence limits, and their contrast assignments, for the listed social-role and physical-function rows?

### F-ST1-004

Printed SMDs do not reproduce the stated common usual-care change-SD construction.

- Exact locations and roles: REPORT [main PDF p. 4](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), Statistical Analysis, SMD definition; REPORT [main PDF p. 11](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11), Table 3 footnote d repeats it; REPORT [main PDF p. 10](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) and [main PDF p. 11](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11), Table 3 SMD/MD columns, all outcome-time rows except severity 6 months. Records S010 and twenty derived-family records listed in the inventory.
- Focus area: B and C.
- Proposed review domain: statistical_results.
- Proposed relationship type: S_W; all relationships: S_W.
- **Qualifying route:** Route A, category 4.
- Printed values, rule and calculation: The source states SMD = adjusted between-group mean difference / SD of change among usual-care participants for that outcome/time. A positive shared denominator requires SMD(HC–PT) = SMD(HC–UC) − SMD(PT–UC). Each displayed SMD has half-unit ±0.005, so subtracting two allows ±0.010; the third has ±0.005. Seventeen rows fail beyond relative gap 0.05, listed below. Three more rows satisfy this additive identity but do not share a denominator with their printed MDs: severity 12 months, intensity 3 months, interference 12 months. From the PT–UC MD and SMD and the rounded-zero HC–PT MD (±0.05), the recomputed HC–PT SMD ranges are respectively [−0.03643,0.03643], [−0.043,0.043], [−0.02944,0.02944]; printed HC–PT SMDs are −0.11, −0.08, −0.12 (±0.005). Minimum gaps/printed magnitudes = 0.06857/0.11=0.623, 0.032/0.08=0.400, 0.08556/0.12=0.713. Also physical-function 3-month HC–UC MD 0.7 vs SMD −0.02; physical-function 6/12-month HC–PT MD −0.3/−0.1 vs SMD +0.22/+0.27; PGIC–pain 12-month HC–PT MD +0.1 vs SMD −0.29 reverse signs under any positive SD. These are exact algebra from the stated definition, not crude/model comparisons or approximate Wald diagnostics. Severity 6-month discrepancies are excluded once by precision.
| Outcome/time | Printed SMDs: PT–UC / HC–UC / HC–PT | Recomputed HC–PT interval from first two SMDs | Minimum gap / absolute printed HC–PT |
|---|---|---|---|
| Severity 3 mo | -0.25 / -0.34 / -0.13 | [-0.100, -0.080] | 0.025 / 0.13 = 0.192 |
| Intensity 6 mo | -0.17 / -0.27 / -0.04 | [-0.110, -0.090] | 0.045 / 0.04 = 1.125 |
| Intensity 12 mo | -0.16 / -0.27 / -0.03 | [-0.120, -0.100] | 0.065 / 0.03 = 2.167 |
| Interference 3 mo | -0.25 / -0.34 / -0.13 | [-0.100, -0.080] | 0.025 / 0.13 = 0.192 |
| Interference 6 mo | -0.27 / -0.37 / -0.14 | [-0.110, -0.090] | 0.025 / 0.14 = 0.179 |
| Social 3 mo | 0.12 / 0.01 / 0.2 | [-0.120, -0.100] | 0.295 / 0.20 = 1.475 |
| Social 6 mo | 0.18 / 0.06 / 0.26 | [-0.130, -0.110] | 0.365 / 0.26 = 1.404 |
| Social 12 mo | 0.19 / 0.07 / 0.27 | [-0.130, -0.110] | 0.375 / 0.27 = 1.389 |
| Physical 3 mo | 0.09 / -0.02 / 0.16 | [-0.120, -0.100] | 0.255 / 0.16 = 1.594 |
| Physical 6 mo | 0.15 / 0.02 / 0.22 | [-0.140, -0.120] | 0.335 / 0.22 = 1.523 |
| Physical 12 mo | 0.2 / 0.07 / 0.27 | [-0.140, -0.120] | 0.385 / 0.27 = 1.426 |
| PGIC pain 3 mo | -0.62 / -0.62 / -0.37 | [-0.010, 0.010] | 0.355 / 0.37 = 0.959 |
| PGIC pain 6 mo | -0.54 / -0.55 / -0.29 | [-0.020, -0.000] | 0.265 / 0.29 = 0.914 |
| PGIC pain 12 mo | -0.55 / -0.57 / -0.29 | [-0.030, -0.010] | 0.255 / 0.29 = 0.879 |
| PGIC general 3 mo | -0.66 / -0.66 / -0.4 | [-0.010, 0.010] | 0.385 / 0.40 = 0.963 |
| PGIC general 6 mo | -0.46 / -0.5 / -0.24 | [-0.050, -0.030] | 0.185 / 0.24 = 0.771 |
| PGIC general 12 mo | -0.53 / -0.58 / -0.28 | [-0.060, -0.040] | 0.215 / 0.28 = 0.768 |

- **Affected result or extracted value:** SMD points and their contrast assignments in twenty of the twenty-one continuous outcome/time rows.
- **Why context does not resolve it:** The supplied definition and table headings establish the denominator and comparisons, but the printed values do not reproduce them. A missing alternative standardization rule is the human question.
- Alternatives and missing definitions: Different contrast-specific standardizers, an outcome/time-column displacement, or SMDs from another analysis could produce different values; each differs from the printed shared-UC-SD definition and needs explicit mapping. Actual UC-change SD values are absent, but additivity/sign and the stated rounding bounds do not require their magnitude.
- Exact human question: Which adjusted mean differences, usual-care change SDs and contrast/time assignments produced the printed SMDs, and does the stated common-SD definition apply to every Table 3 row?

### F-ST1-005

Two NNT points exceed the display tolerance for the stated reciprocal formula.

- Exact locations and roles: REPORT [main PDF p. 4](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), NNT definition; REPORT [main PDF p. 9](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), Table 2 footnote d and health coach vs usual care NNT points for severity 6 months and interference 6 months; records S011, S026 and S044.
- Focus area: B and C.
- Proposed review domain: statistical_results.
- Proposed relationship type: S_W; all relationships: S_W.
- **Qualifying route:** Route A, category 4.
- Printed values, rule and calculation: Severity at 6 months: adjusted percentages 37.1% and 22.9%, NNT 8. Half-unit percentage intervals give RD [0.141,0.143], reciprocal [6.993007,7.092199]; printed NNT interval [7.5,8.5], gap 0.407801, relative 0.050975. Interference at 6 months: 40.9% and 24.3%, NNT 7; RD [0.165,0.167], reciprocal [5.988024,6.060606]; printed NNT interval [6.5,7.5], gap 0.439394, relative 0.062771. The stated reciprocal method reproduces other rows or leaves them within the precision rule; these two are above 0.05. Full tuple checks preserved in the inventory.

- **Affected result or extracted value:** Health coach vs usual care NNT points for six-month severity and interference response.
- **Why context does not resolve it:** The method/display discrepancy is reproduced above the fixed precision threshold. A possible upward integer-rounding rule is retained as an alternative rather than silently added to the supplied formula.
- Alternatives and missing definitions: Rounding NNTs upward rather than to nearest integer yields 8 and 7 here and can reconcile the table. The source does not state that convention; no claim is made that the estimated risk difference itself differs.
- Exact human question: Were these NNTs rounded upward to whole participants, and what unrounded reciprocal values and display rule generated the reported points?

### F-ST1-006

Finite positive NNT intervals accompany null-containing RR intervals for the same contrasts.

- Exact locations and roles: REPORT [main PDF p. 9](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), Table 2, health coach vs painTRAINER, severity 6/12 months, intensity 3/12 months, interference 6/12 months; Table 2 footnotes b,d,e; REPORT [main PDF p. 4](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), shared binary model and NNT definition. Records S026, S029, S032, S038, S044, S047.
- Focus area: B.
- Proposed review domain: statistical_results.
- Proposed relationship type: S_W; all relationships: S_W.
- **Qualifying route:** Route B.
- Printed values, rule and calculation: All six RR intervals include 1, while all six printed NNT intervals are finite and positive. RR=1 and risk difference=0 are the same equality-of-response null for these matched adjusted group responses. Footnote e explicitly requires an NNT interval including infinity, with a negative NNH branch, when its RD interval contains zero. Inverting the finite NNT intervals implies strictly positive RD intervals: severity 6 [1/186,1/12], severity 12 [1/76,1/17], intensity 3 [1/57,1/14], intensity 12 [1/38,1/18], interference 6 [1/67,1/11], interference 12 [1/79,1/16]. The observation is exact interval/null reading. Compatibility with a common confidence-set construction cannot be reproduced because the RD/NNT CI construction is not stated; different parameter-specific interval methods are an explicit alternative, not an inferred contradiction in a specific variance formula.
| Outcome/time | HC–PT RR (95% CI) | HC–PT NNT (95% CI) |
|---|---|---|
| Severity 6 mo | 1.13(0.98–1.30) | 24(12–186) |
| Severity 12 mo | 1.07(0.96–1.19) | 41(17–76) |
| Intensity 3 mo | 1.11(0.93–1.33) | 37(14–57) |
| Intensity 12 mo | 1.05(0.92–1.20) | 63(18–38) |
| Interference 6 mo | 1.10(0.96–1.27) | 26(11–67) |
| Interference 12 mo | 1.07(0.97–1.18) | 39(16–79) |

- **Affected result or extracted value:** The six HC–PT NNT intervals, whether they support a finite benefit interval and which limits an evidence extractor should record.
- **Why context does not resolve it:** The same table/source model prints opposite null coverage for the matched response contrasts and gives an infinity rule, but omits the RD confidence-interval method. Readers cannot determine whether different CI methods explain this or whether NNT limits need another assignment.
- Alternatives and missing definitions: RR and RD intervals may come from different valid interval constructions and have different finite-sample coverage; covariance, transformation and exact RD limits are not inferred. No pairwise P value is printed. The intensity 12-month point-containment issue is separately tracked in F-ST1-001.
- Exact human question: Which risk-difference confidence intervals and interval construction generated these six NNT intervals, and how should their null coverage be interpreted alongside the same-contrast RR intervals?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT main p.10, Table 3 severity 6 months, SMDs −0.26/−0.36/−0.12 | Shared-SD additivity predicts HC–PT [−0.110,−0.090], printed half-unit [−0.125,−0.115]; gap .005/.12=.0417. MD/SMD shared-denominator rounding discrepancy is likewise below .05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p.7 secondary narrative vs p.10 severity 3-month SMD row | Narrative −0.26/−0.36 vs table −0.25/−0.34: half-unit gaps0/.010, relative0/.0294. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p.10 physical functioning 6-month omnibus P=.05 and footnote p.11 pairwise gate P<.05 | The printed P rounding interval[.045,.055] includes values that satisfy the stated gate; exact unrounded gate result cannot be determined. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p.4 Sample Size | Exact 90% simulated power cannot be rebuilt without the complete simulation specification; 2331=777×3,7.5 percentage points andRR1.5 reconcile, with no contradicted sample size. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p.11 Table 3 PGIC headings/footnotes | Mean change label versus a since-start-of-study global-impression scale: scale coding and outcome meaning are evident from adjacent footnotes. | TERMINOLOGY_OR_WORDING |
| REPORT main p.3 primary scoring and p.7 Table1 footnote g | Requirement of all4 intensity and at least4/7 interference items versus mean of11-item instrument wording does not establish a conflicting reported score. | TERMINOLOGY_OR_WORDING |
| REPORT main pp.1,7 secondary benefit narrative vs physical-function rows p.10 | Overall-pattern statements summarize benefits while individual physical-function contrasts vary in null coverage; whether wording means every contrast is not established. | TERMINOLOGY_OR_WORDING |

## Scope closure and limitations

All S001–S110 records have PASS_1_COMPLETE. Every Table 2/Table 3 tuple and row-level omnibus test was checked. Figure 2 matches severity rows at all three time points; the abstract and primary-result narrative agree with primary estimates and intervals. Method checks cover analysis units, population, model, adjustment, missingness, sidedness, confidence, multiplicity, inference direction and power arithmetic. Main pages13–14 contain only references. Numeric-only Table1/flow/adverse-event arithmetic remains the numeric review assignment, while analysis-population implications were reviewed here. No main inferential relationship omitted.

Named limitations: exact sample-size simulation cannot be recreated from printed inputs alone; numeric test statistics, standard errors, robust degrees of freedom, actual UC-change SDs and the RD/NNT interval construction are absent. No missing model detail alone was emitted. Supplement/PLAN inferential rows are peer scopes. Direct PDF tools were absent; pinned PyMuPDF fresh native text and supplied-source page images provided coverage. No new Python helper written. No candidate IDs or adjudications assigned.

