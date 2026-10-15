# Statistical consistency pass1 — complete disjoint review

The union of four fresh gpt-6.1-sol/high agent scopes covers all263statistical relationships. Prior Workflow1.6.2 contents are excluded.


<!-- Complete checker part: main -->

# Statistical Pass 1 — Main-Paper Shard

Runtime agent: /root/stat1_main; fresh gpt-6.1-sol/high. Exact scope: DOC-001 main REPORT, physical PDF pages 1–14; MAIN001–MAIN116; S001–S110. All 270 estimate–95% interval tuples and 30 omnibus tests reviewed; all 27 NNT and 63 SMD tuples included. Findings: 6 consolidated patterns. Excluded observations: 7. Each relationship is PASS_1_COMPLETE. This part does not adjudicate candidates.

Read completely: QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md. Used current fresh main map, supplied main PDF native text and exact original rendered source pages; all tables and cited signs/order on pages 9–11 visually confirmed. No web or old review conclusions used. Supplement statistical rows and plan-internal relationships are disjoint peer assignments. Links below target the supplied main PDF. All compared locations have role REPORT; proposed primary relationship S_W and all relationships S_W.

### F-ST1-001

A Table 2 NNT point lies beyond its printed confidence interval.

- Exact locations and roles: REPORT [main PDF p. 9](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), Table 2, pain intensity at 12 months, health coach vs painTRAINER NNT column; see MAIN085 derived-family record S038.
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

- Exact locations and roles: REPORT [main PDF p. 10](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, severity 12 months, intensity 12 months, interference 12 months, physical functioning 6 and 12 months; REPORT [main PDF p. 11](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11), Table 3 continuation, PGIC–pain at 12 months. Derived-family records: S056, S065, S074, S089, S092, S101.
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

- Exact locations and roles: REPORT [main PDF p. 10](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), Table 3, social-role functioning and physical functioning, all three time points and all three SMD columns: S077, S080, S083, S086, S089, S092.
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

- Exact locations and roles: REPORT [main PDF p. 4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), Statistical Analysis, SMD definition; REPORT [main PDF p. 11](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11), Table 3 footnote d repeats it; REPORT [main PDF p. 10](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) and [main PDF p. 11](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11), Table 3 SMD/MD columns, all outcome-time rows except severity 6 months. Records S010 and twenty derived-family records listed in the inventory.
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

- Exact locations and roles: REPORT [main PDF p. 4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), NNT definition; REPORT [main PDF p. 9](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), Table 2 footnote d and health coach vs usual care NNT points for severity 6 months and interference 6 months; records S011, S026 and S044.
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

- Exact locations and roles: REPORT [main PDF p. 9](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), Table 2, health coach vs painTRAINER, severity 6/12 months, intensity 3/12 months, interference 6/12 months; Table 2 footnotes b,d,e; REPORT [main PDF p. 4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), shared binary model and NNT definition. Records S026, S029, S032, S038, S044, S047.
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



<!-- Complete checker part: reports -->

# Statistical pass 1 — supplementary REPORT shard

Fresh agent: /root/stat1_reports; gpt-6.1-sol; high effort; FRESH_SPAWN. The coordinator records the actual spawn runtime ID in agent_execution_manifest.md.

Exact scope: DOC-005 PDF pages 1–16 and 19, eTables 1–10 and eFigures 1–2; inferential and statistical-method content of DOC-004 PDF pages 1–7 and DOC-006 worksheet eTable 3, A1:J115. DOC-005 eTable 11, PDF pages 17–18, belongs to the separate raw-score shard; MAIN inference rows and PLAN-internal statistical relationships belong to separate peers. All compared locations below are REPORT by content.

Read completely: QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md. Scientific input was limited to exact supplied sources and current fresh source maps. No prior 1.6.2 conclusions, candidate sets or screening records were read. Fresh source renders confirmed every cited PDF row. Direct permitted Office extraction confirmed workbook cells. Source-unit scientific gaps: none. No web used.

Pass-1 coverage: **63 stable relationships, S201–S263**, each explicitly PASS_1_COMPLETE in statistics/parts/reports_inventory.md. **6 findings; 9 excluded-observation rows.** Repeated instances of each pattern are consolidated. Proposed domains and relationship types pre-fill human review; no adjudication is assigned.

## Findings

### F-ST1-201

**Title:** Linear-imputation 95% intervals exclude zero while the corresponding P values exceed .05.

**Relationships:** S208; related method records S204, S205. Proposed primary relationship type: S_W; all relationships: S_W.

**Exact locations and document roles:** REPORT [DOC-005 PDF p.8, eTable 3](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8), seven rows listed below; REPORT [DOC-005 PDF pp.4–5, imputation method](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5). REPORT [DOC-001 PDF p.4, Statistical Analysis](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4) supplies the shared two-sided α=.05 test definition and corroborates, rather than conflicts with, the supplement.

**Printed values:**

| eTable 3 row | Estimate | Printed 95% CI | P value |
|---|---:|---|---:|
| Pattern: 2 observed follow-ups | −0.28 | −0.47, −0.08 | .150 |
| Pattern: 1 observed follow-up | −0.20 | −0.36, −0.03 | .226 |
| Pattern 2, painTRAINER interaction | −0.30 | −0.58, −0.02 | .280 |
| Pattern 2, Health Coach interaction | −0.47 | −0.74, −0.19 | .090 |
| Site 3 | 0.19 | 0.08, 0.29 | .069 |
| Site 4 | 0.15 | 0.05, 0.24 | .124 |
| Second Education: AA degree (reference High school or less) row | 0.16 | 0.07, 0.25 | .077 |

**Rule and calculation:** For each printed 95% interval, 0 is outside its limits, while the corresponding printed P is greater than .05. These are individual coefficient rows of the reported linear GEE imputation model, with working independence and robust standard errors accounting for coach and participant clustering. For example, −.47 < −.28 < −.08 < 0 but P=.150; 0 < .08 < .19 < .29 but P=.069. All seven estimates are contained in their intervals and their endpoints are ordered. The conflict concerns interval-versus-test significance. The display-precision rule is inapplicable to Route A category 1; no relative-discrepancy calculation is used to screen this pattern out.

**Focus area:** B, estimate and test logic.
**Proposed review domain:** statistical_results.
**Qualifying route:** Route A, category 1.
**Affected result or extracted value:** Significance and uncertainty of the missingness-pattern, pattern-by-arm, site and education coefficients used in the primary-outcome imputation model.
**Why context does not resolve it:** Each row contains the conflicting interval and P value under a 95% CI column and the common .05 test level. This is an always-register interval-versus-P pattern. The immediate table and accompanying method do not state that the columns represent different analyses.

**Alternatives and missing definitions:** P values and intervals might use different variance estimates, coefficient tests or confidence constructions, or one printed column might summarize a different analysis. The source does not supply the coefficient-test family, degrees of freedom or numeric standard errors needed to reconstruct the exact P values. Such an alternative must be stated by the human reviewer; it does not remove the directly printed null-significance conflict. No normal-Wald approximation is used as the reproduction criterion.

**Exact human question:** Which analysis, variance estimate and confidence-interval construction produced the seven listed eTable 3 intervals and P values, and which interval and P value should be extracted for each coefficient?

### F-ST1-202

**Title:** Significant coefficient P values accompany 95% intervals printed with a null-valued endpoint.

**Relationships:** S209 and S210. Proposed primary relationship type: S_W; all relationships: S_W.

**Exact locations and document roles:** REPORT [DOC-005 PDF p.9, eTable 4, Age ≥65 and second AA education rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); REPORT [DOC-005 PDF p.10, eTable 5, PEG score row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10). Shared significance definition: REPORT DOC-001 PDF p.4, all tests two-sided α=.05; this is corroborating context.

**Printed values:**

| Location and row | Effect | Printed 95% CI | P |
|---|---:|---|---:|
| eTable 4, Age ≥65 vs <65 | RR 1.15 | 1, 1.33 | .046 |
| eTable 4, second Education: AA degree vs HS or less | RR 1.16 | 1, 1.33 | .046 |
| eTable 5, PEG score | OR 0.96 | 0.92, 1.00 | .037 |

**Rule and calculation:** The ratio null is 1. The printed lower endpoint equals 1 in both eTable 4 rows, and the printed upper endpoint equals 1.00 in the eTable 5 row. Thus each displayed 95% interval includes the null, while its corresponding P is below .05. Point containment and interval ordering hold. The scope explicitly exempts interval-versus-P comparisons from display-precision screening; these boundary cases are therefore registered even though rounding can plausibly explain an exact endpoint close to 1.

**Focus area:** B, estimate and test logic.
**Proposed review domain:** statistical_results.
**Qualifying route:** Route A, category 1.
**Affected result or extracted value:** The printed 95% intervals and significance of age and education effects in the primary estimation model and PEG in the response-weight model.
**Why context does not resolve it:** The displayed interval includes its null and the P value is significant at the stated level. Route A category 1 requires registration; presumed unrounded endpoints cannot substitute for supplied printed values.

**Alternatives and missing definitions:** A true lower endpoint slightly above 1, or upper endpoint slightly below 1, may have rounded to the printed null; different interval and test constructions are another possibility. The source does not provide unrounded endpoint values or separate coefficient-test definitions. These are alternatives for human adjudication.

**Exact human question:** What are the unrounded 95% endpoints and the associated test definitions for these three rows, and how should their printed intervals and P values be represented for extraction?

### F-ST1-203

**Title:** The stated final weight-model covariates differ from the fitted weight-model display.

**Relationships:** S203, S207, S210, S256 and S262. Proposed primary relationship type: S_W; all relationships: S_W. DOC-006 only corroborates selection-test context and does not create an S_C conflict.

**Exact locations and document roles:** REPORT [DOC-005 PDF p.7, eTable 2, final additional variables for the nonresponse weight model](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); REPORT [DOC-005 PDF p.10, eTable 5, complete logistic weight-model coefficient display](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); REPORT [DOC-005 PDF pp.4–5, selection and weighting methods](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5).

**Printed values and statements:** eTable 2 lists additional weighting variables as PEG score, PHQ-8, GAD-7, any negative social determinant of health, and education (any college vs HS degree or less). Its base-variable list does not include employment. eTable 5 contains the first four of these variables, has no education coefficient, and instead reports Not employed OR1.49 (95% CI1.11–2.00), P=.008. The narrative describes adding the selected covariates to the final logistic model used to create weights for the primary analysis.

**Rule and calculation:** Compare membership of the explicitly stated final additional-covariate set with the full fitted-model coefficient set. Stated education has no displayed coefficient; displayed employment is absent from the final weighting list and the base list. This is a logical model-attribution comparison, with no rounding calculation applicable. Changing the treatment reference group in a logistic fit does not account for exchanging these covariates.

**Focus area:** C, statistical method logic.
**Proposed review domain:** statistical_results.
**Qualifying route:** Route B.
**Affected result or extracted value:** The nonresponse weights used in the primary weighted MCID analysis and the reported employment OR in the weighting model.
**Why context does not resolve it:** Both displays identify the final weight model, but they specify different applied adjustment sets. The table does not disclose an omitted education coefficient, substitution or subsequent model revision. A reader cannot identify which covariate set generated the actual weights from these statements.

**Alternatives and missing definitions:** Education may have been used but omitted from the displayed model, the final list may refer to an earlier selection stage, or employment may have been added subsequently. The workbook shows employment significant in both selection families (H18<.001, I18=.0228), but that corroboration does not resolve the printed final-model discrepancy. No preference for including either predictor is proposed.

**Exact human question:** Did the logistic model generating the primary nonresponse weights include education, employment, both or another set, and which coefficient display and final-variable list describe that model?

### F-ST1-204

**Title:** Education coding and repeated coefficient labels leave the applied education adjustment unclear.

**Relationships:** S203, S208, S209 and S261. Proposed primary relationship type: S_W; all relationships: S_W. Workbook categories are corroboration only.

**Exact locations and document roles:** REPORT [DOC-005 PDF p.7, eTable 2, additional imputation/estimation variables](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); REPORT [DOC-005 PDF p.8, eTable 3, all education coefficient rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8); REPORT [DOC-005 PDF p.9, eTable 4, all education coefficient rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9). REPORT DOC-006 eTable 3 A12:A16 provides distinct HS/associate/college/graduate categories as corroboration.

**Printed values and statements:** eTable 2 specifies education as “any college vs. HS degree or less.” eTable 3 prints three education coefficients: AA degree −.02 (−.11,.08), P=.866; a second AA degree .16 (.07,.25), P=.077; Graduate degree .39 (.29,.49), P<.001, all versus high school or less. eTable 4 likewise prints AA degree RR.97 (.82,1.16), P=.770; a second AA degree RR1.16 (1,1.33), P=.046; Graduate degree RR1.35 (1.13,1.61), P<.001.

**Rule and calculation:** A single binary any-college indicator is a different adjustment specification from three category-versus-reference coefficients. Further, two different coefficients have the same AA label and reference within each complete fitted model. The supplied category list makes a college label plausible for one row but does not state that mapping. This is a model-definition and numeric-result-attribution comparison; display precision does not resolve category assignment.

**Focus area:** C, statistical method logic; B, estimate attribution.
**Proposed review domain:** statistical_results.
**Qualifying route:** Route B.
**Affected result or extracted value:** The education adjustment in the primary imputation and estimation models, and the coefficient/RR assigned to associate versus college education.
**Why context does not resolve it:** The immediate coefficient tables offer two different estimates for the same labeled category, while the selection table specifies a binary contrast. Guessing which row belongs to the college category does not establish the coding actually used or the coefficient a data extractor should assign.

**Alternatives and missing definitions:** The applied education covariate may have been a four-level factor with one repeated label, or the selected binary covariate may have been expanded for the reported fits. The source does not explicitly disclose a recoding or map the duplicate labels. This observation is consolidated across both models because it is one education-definition pattern, rather than a separate finding for each repeated label.

**Exact human question:** Was education coded as any-college versus HS-or-less or as a multilevel factor in each primary model, and which category corresponds to each of the two printed AA rows?

### F-ST1-205

**Title:** Restricted primary subset analyses list a smaller covariate set than the primary estimation model.

**Relationships:** S220 and S263. Proposed primary relationship type: S_W; all relationships: S_W.

**Exact locations and document roles:** REPORT [DOC-005 PDF p.13, Protocol Change Subset Analyses](../../../joi250046supp4_prod_1755300121.15587.pdf#page=13); REPORT [DOC-005 PDF p.14, eTable 8, footnote b](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14); REPORT [DOC-005 PDF p.4, Adjustment](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4); REPORT [DOC-005 PDF p.7, eTable 2, final imputation/estimation list](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7).

**Printed values and statements:** The subset narrative says eTable 8 shows “results of the primary analysis restricting to subsets of the randomized population.” The primary imputation/estimation selection list adds education and unemployment, and the fitted models display both. eTable 8 footnote b instead lists sex, age, site, rural/urban residence, more than one musculoskeletal condition, mental-health diagnosis and baseline pain severity, without education or employment.

**Rule and calculation:** The stated restricted-primary-analysis model attribution and the explicit subset adjustment list do not name the same adjustment set. This is a logical analysis-definition comparison; no numeric rounding test applies. It concerns the explicit covariates, rather than inferring the absence of imputation or weighting from silence.

**Focus area:** C, statistical method logic.
**Proposed review domain:** statistical_results.
**Qualifying route:** Route B.
**Affected result or extracted value:** All eTable 8 adjusted percentages, RR and NNT estimates in the pre-enhancement, post-enhancement and reminder-letter subset analyses, including the 3-month primary-outcome subset estimates.
**Why context does not resolve it:** The narrative identifies a restricted version of the primary analysis, while the footnote describes a base-only adjustment. No explanation says that additional primary covariates were dropped, reselected or merely omitted from the footnote. The actual analysis producing these estimates is therefore not identifiable from the supplied description.

**Alternatives and missing definitions:** The primary model may have been refitted with only base covariates in subsets, additional predictors may have been reselected, or the footnote may abbreviate a fuller adjustment set. Any of these could be internally coherent if stated; the observation asks which was used and does not propose a preferred subset analysis.

**Exact human question:** Which covariates were included in each eTable 8 subset estimation model, and does “primary analysis restricting to subsets” mean the full primary adjustment set or the base-only set listed in footnote b?

### F-ST1-206

**Title:** Reminder-letter 6-month PT-versus-UC NNT does not reproduce from the printed adjusted percentages under the stated reciprocal method.

**Relationships:** S228; method S220. Proposed primary relationship type: S_W; all relationships: S_W. The numeric checker independently identified related MAIN occurrences; this shard registers its assigned occurrence for the inclusion screener to consolidate as appropriate.

**Exact locations and document roles:** REPORT [DOC-005 PDF p.14, eTable 8, Reminder Letters Added, 6-month row, PT and UC adjusted percentages and PT-versus-UC NNT](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14); REPORT same page, footnote d defining NNT.

**Printed values:** PT35.6% (30.6,41.4); UC21.3% (17.5,26.1); PT-versus-UC NNT8 (5,14). Footnote d defines NNT as one over the difference in adjusted improvement percentages (using probability units).

**Rule and calculation:** NNT=100/(35.6−21.3)=100/14.3=6.99300699. Give each printed percentage its half-unit interval: PT[35.55,35.65], UC[21.25,21.35]. Their difference is[14.20,14.40] percentage points, so the recomputed NNT interval is[100/14.40,100/14.20]=[6.94444444,7.04225352]. The printed integer NNT8 has half-unit interval[7.5,8.5]. The gap is7.5−7.04225352=.45774648; relative discrepancy=.45774648/8=.05721831>.05. The same reciprocal check across all45 contrasts in eTables7–8 leaves the other44 within the display-precision threshold; the method reproduces the other rows under that rule. Ceiling the reciprocal of the printed percentage centers6.99300699 gives7, but the true unrounded reciprocal may lie as high as7.04225352, whose ceiling is8. Thus an unstated upward-integer convention remains an alternative for this row too; no ceiling rule is assumed for the half-unit reproduction comparison. Endpoint uncertainty of the NNT confidence interval is not recomputed because the risk-difference variance is absent.

**Focus area:** B, estimate and test logic; C, statistical method logic.
**Proposed review domain:** statistical_results.
**Qualifying route:** Route A, category 4.
**Affected result or extracted value:** The PT-versus-UC adjusted NNT for pain-severity MCID at6 months among participants randomized after3/31/2022.
**Why context does not resolve it:** The specified reciprocal method reproduces the other rows within the scope threshold, but this printed8 remains separated by more than5% after input/output display precision. The printed result is an always-register reproducing-method discrepancy.

**Alternatives and missing definitions:** The NNT may have been calculated from another risk-difference estimand or model despite footnote d, or a different percentage pair may have been used. The printed row and footnote do not disclose another calculation. This card does not prescribe a replacement value.

**Exact human question:** What risk difference and calculation produced the printed NNT8 for the reminder-letter 6-month PT-versus-UC comparison, and is it the reciprocal of the same adjusted percentages printed in that row?

## Excluded observations

Only apparent issues decided against emission are listed; checks that reconcile remain in the S records.

| Location | Observation | Reason code |
|---|---|---|
| DOC-005 PDF p.7, eTable 1 completeness patterns; DOC-006 eTable 3 B3:E3 | Pattern counts 188+283+1568=2039 versus any-followup 2036; PT 644 vs 643 and HC 692 vs 690; implied visits 5458 vs 5449; workbook missing 1-or-2 is 468 versus 188+283=471. Half-unit pattern-total interval [2037.5,2040.5] versus [2035.5,2036.5] leaves gap 1/2036=.000491; visit totals [5455,5461] versus [5447.5,5450.5] leave gap 4.5/5449=.000826; the workbook comparison [470,472] versus [467.5,468.5] leaves gap 1.5/468=.003205. All are ≤.05; arm-total intervals overlap. The pattern is listed once. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-005 PDF pp.11/14, eTables7–8, other NNT point estimates | All44 reciprocal NNT comparisons other than F-ST1-206 either overlap under half-unit input/output intervals or have remaining relative gaps≤.05. Largest excluded gap: reminder-letter6M HC/UC NNT6 versus reciprocal[5.154639,5.208333], printed[5.5,6.5], relative.048611. Other apparent NNT differences are one consolidated display-precision pattern. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-005 PDF p.8, eTable3, quantitative CI-width/P diagnostics beyond the seven null conflicts | A normal-Wald diagnostic SE=(upper−lower)/(2×1.96), then two-sided P from estimate/SE, yields differences for additional rows (for example Time6M estimate.13,CI.07–.19 gives diagnostic z4.247 and Pabout.000022 versus.025). Coefficient-test family, degrees of freedom and interval construction are not stated; a specific exact numerical test cannot be established. The seven direct CI-null/P conflicts remain emitted separately as F-ST1-201. | CONDITIONAL_OR_UNREPORTED |
| DOC-005 PDF p.8, eTable3, arm coefficients versus improvement direction | Positive imputation coefficients cannot alone be interpreted as worse clinical response without a supplied sign convention for the imputation change, the missingness-pattern conditioning and the complete covariate context. No direct printed direction statement for these conditional coefficients conflicts. | CONDITIONAL_OR_UNREPORTED |
| DOC-005 PDF pp.5/9/10, weight normalization description and sums | “Scaled to the study sample size” could be read as2331 rather than2036, but eTable6 explicitly sums to2036, eTable4 to3×2036=6108, and imputation is among any-followup participants. These immediate displays identify the analysis sample for the scaling statement. | CONTEXT_RESOLVES |
| DOC-005 PDF p.7, eTable2 all-model list versus pp.4/8/9 | Baseline pain severity is omitted from eTable2's base-variable list, but the adjustment narrative and both complete primary model displays explicitly include it. Its applied inclusion is immediately identifiable and the omission changes no extractable coefficient assignment. | CONTEXT_RESOLVES |
| DOC-005 PDF p.15, eTable9 title | Title says “adjusted relative risk,” but the page explicitly says no adjustment, weighting or imputation, the coefficient heading says Relative Risk, and footnote b says “without adjustment.” The intended unadjusted analysis is immediately identified; point estimates also agree with the unadjusted proportions. | TERMINOLOGY_OR_WORDING |
| DOC-005 PDF p.16, eTable10 descriptive median heading versus mean-effect footnote | Group medians/IQRs do not need to reproduce between-group mean differences. The effect columns explicitly name means and95%CIs, while the descriptive columns name medians/IQRs; this distinction identifies the quantities a reader extracts. No direct numeric contradiction is established. | CONTEXT_RESOLVES |
| DOC-005 PDF p.3, eFigure1 Virtual Coach/VC labels | Virtual Coach names the Health Coach intervention in the surrounding three-arm trial context; no numeric result is attributed to a different intervention. | TERMINOLOGY_OR_WORDING |

## Checks and limitations

All coefficient, treatment, sensitivity and unadjusted-result tuples in the assigned scope were checked for point containment, endpoint order and direction. All individual CI/P null-level conflicts are registered above. Omnibus P values were matched to their three-arm Wald tests; they were not compared as individual pairwise P values. Printed NNT positive/negative limits were interpreted as the explicitly defined infinity-containing branches, not reversed finite intervals.

The source supplies two-sided α=.05 and95% intervals. It does not supply numeric coefficient standard errors, numeric test statistics, coefficient-test degrees of freedom or full covariance matrices. Exact P/SE/statistic compatibility beyond direct null-level conflicts is consequently not asserted; diagnostic approximations are labeled. The assigned supplement has no power/sample-size calculation, noninferiority/equivalence margin or statistical interim/stopping boundary. Fidelity thresholds in DOC-004 concern treatment delivery, not statistical trial stopping.

No scientific source-coverage gap remains in this assigned scope. Unlabeled histogram bins provide visual direction only, not exact counts. Workbook conversion to PDF is unavailable, but direct cell extraction supplies truthful worksheet/cell locations. Primary durable outputs: statistics/parts/reports_inventory.md and checkers/parts/stat1_reports.md. Fresh renders and Office extraction, with CPU PyMuPDF1.26.4 and the permitted Office helper, are under preprocessing/stat1_reports.



<!-- Complete checker part: plans -->

# Statistical pass 1 — complete PLAN shard

Fresh runtime task `/root/stat1_plans`, gpt-6.1-sol/high; the coordinator records the actual tool-returned runtime agent ID. Exact scope: DOC-002 protocol physical PDF pp.1–77 and DOC-003 SAP physical PDF pp.1–29, all inferential/statistical/method/design relationships. Stable inventory: S401 through S464, 64 records, all explicitly PASS_1_COMPLETE. Findings: 0. Excluded observations: 10. No candidate IDs, dispositions or final corrections are assigned.

QUALITY_CONTROL_SCOPE.md and the complete 1.6.2 review contract were read; the performance profile, settings and report specification were also read. Only current fresh maps, supplied sources and their current fresh renders supplied scientific input. Source roles are PLAN for both documents, determined by their prospective content. Source-confirmed critical pages and calculations are recorded in statistics/parts/plans_inventory.md.

The checked families include all primary/secondary/exploratory endpoint rows; randomization and strata; ITT, safety and conditional as-treated populations; every primary and subgroup sample-size/power tuple; the omnibus/pairwise gate, sidedness and significance; longitudinal mean-model equation, relative-risk estimand, adjustment and robust variance logic; missing-data patterns and sensitivities; seven subgroup definitions/interactions; mediation steps, equations, selection rule and weights; economic estimands, net-benefit equation, cost categories and sensitivities; safety ascertainment, halting and interim rules. All protocol/SAP pages, including histories, covers, administrative material and references, are covered through the complete current maps. Historical inferential quantities were distinguished from trial results.

## Findings

No qualifying finding was emitted within this disjoint PLAN statistical scope. This does not state a package-wide candidate count. REPORT fitted-estimate/test relationships and planned-versus-reported outcome/status/analysis judgments remain in their assigned peer scopes. A new pass-2 agent must revisit every stable S ID and every exclusion after the complete ledger, screen and mechanical recheck exist.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| PLAN DOC-002 PDF p.55, section15.1 and subgroup power table; PLAN DOC-003 PDF p.16, section5; REPORT DOC-001 PDF p.4, Sample Size, selectively read as context | A simple independent-proportion normal diagnostic yields567.072/arm rather than621; continuity-correction diagnostic593.439/arm. Subgroup diagnostics also depend on routine. Neither normal algorithm is stated; the REPORT explicitly describes10,000 modified-Poisson simulations. The necessary simulation inputs and success definition are absent, and no chosen diagnostic is established as a method reproducing other rows of this display. This is an approximation-dependent observation rather than reproduced stated-method conflict. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 PDF p.55; PLAN DOC-003 PDF p.16, narrative and power table | “Relative change150%” and the subgroup “Relative Change” values206.7/184.7/172.0% are explicitly defined by the table as active/UC ratio. Values and arithmetic reconcile; the label versus percentage-increase terminology does not change the available ratio or response rates. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-002 PDF p.22 and DOC-003 PDF p.11, binary interference responder row, brief-description cell | The description uses “pain intensity” while the row label and same sentence explicitly specify the7-item interference subscale and30% reduction. The intended scale is evident in that row. No printed number, composite definition or actual outcome status changes. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-002 PDF p.22 and DOC-003 PDF p.11, both binary subscale rows, measurement and timeframe cells; corroborating PLAN DOC-002 p.57/DOC-003 p.21 | Measurement cells list baseline,6,12-months while the immediately adjacent timeframe cells explicitly include primary baseline-to-3-months. The same displays identify the3-month analysis; subsequent analysis text confirms3-month primary time for secondary outcomes. No outcome is absent from the supplied plan and no numerical result conflicts. | CONTEXT_RESOLVES |
| PLAN DOC-002 PDF p.25, moderator introduction, versus pp.57–58, section15.7; PLAN DOC-003 pp.14,22 | Protocol table relates moderators to6-month severity MCID; analysis paragraph identifies3-month interaction comparison, and SAP says primary outcome/3-months. This is an ancillary plan-internal moderator-time comparison without a reported subgroup result in the current REPORT map. It does not alter the trial's primary3-month severity definition or sample size; planned-versus-reported omission/status screening is separately assigned to the cross-source checker. | PERIPHERAL_COMPARISON |
| PLAN DOC-003 PDF p.23, Step3a narrative, equation and inverse-probability weights | Narrative mentions baseline-confounder adjustment while the displayed logistic equation and weights show selected mediators without a Z term. The difference concerns the ancillary mediation method, for which no fitted mediation result is reported in the current REPORT map. It has no supplied numerical effect on primary/key-secondary results, population size or primary decision rule. Planned-versus-reported mediation omission/status screening is separately assigned. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 PDF pp.27,47,58; PLAN DOC-003 PDF pp.15,22–23 | Mediation prose says baseline-to-3-month changes for all three mediators, but perceived support is explicitly collected at notification of randomization and3-months. Protocol p.47 expressly says the notification survey serves as baseline potential mediator; the intended origin is stated. | CONTEXT_RESOLVES |
| PLAN DOC-002 PDF p.5 amendment history versus p.32 current eligibility; PLAN DOC-003 PDF pp.3,17 | Protocol history says two pain encounters at least30-days apart; current protocol/SAP eligibility says>60 days and SAP amendment specifies60 days. The history/current comparison does not demonstrate a changed actual effectiveness-population size, primary/key-secondary result or decision rule. Actual reported eligibility/population matching remains assigned cross-source scope. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 PDF p.61, qualitative frameworks section16 | RE-AIM/TFA component/domain count descriptions differ from the named list lengths. These framework descriptions do not represent trial participant/event counts, power inputs or statistical result/decision quantities. They fall outside the four quantitative focus areas. | OUT_OF_FOCUS |
| PLAN DOC-002 PDF p.50, systematic SAE review description; PLAN DOC-003 PDF p.3 amendment and p.26 current safety text, with SAP precedence p.10 | Routine hospitalization chart-review differs between protocol and current SAP, but the SAP amendment explicitly removes it and current text preserves death review and conditional hospitalization review. This is a disclosed procedural update; event definitions and the stated descriptive safety analysis remain clear. | CONTEXT_RESOLVES |

Source evidence: [DOC-002 p.55](../../../joi250046supp1_prod_1755300121.14087.pdf#page=55), [DOC-003 p.16](../../../joi250046supp2_prod_1755300121.15087.pdf#page=16), [DOC-001 p.4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), [DOC-002 p.22](../../../joi250046supp1_prod_1755300121.14087.pdf#page=22), [DOC-003 p.11](../../../joi250046supp2_prod_1755300121.15087.pdf#page=11), [DOC-002 p.25](../../../joi250046supp1_prod_1755300121.14087.pdf#page=25), [DOC-002 p.58](../../../joi250046supp1_prod_1755300121.14087.pdf#page=58), [DOC-003 p.23](../../../joi250046supp2_prod_1755300121.15087.pdf#page=23), [DOC-002 p.47](../../../joi250046supp1_prod_1755300121.14087.pdf#page=47), [DOC-003 p.15](../../../joi250046supp2_prod_1755300121.15087.pdf#page=15), [DOC-002 p.5](../../../joi250046supp1_prod_1755300121.14087.pdf#page=5), [DOC-002 p.32](../../../joi250046supp1_prod_1755300121.14087.pdf#page=32), [DOC-003 p.3](../../../joi250046supp2_prod_1755300121.15087.pdf#page=3), [DOC-003 p.17](../../../joi250046supp2_prod_1755300121.15087.pdf#page=17), [DOC-002 p.61](../../../joi250046supp1_prod_1755300121.14087.pdf#page=61), [DOC-002 p.50](../../../joi250046supp1_prod_1755300121.14087.pdf#page=50), [DOC-003 p.26](../../../joi250046supp2_prod_1755300121.15087.pdf#page=26), [DOC-003 p.10](../../../joi250046supp2_prod_1755300121.15087.pdf#page=10).

## Limits and coverage

No actual-trial fitted estimate/CI/P/test-statistic or standard error tuple is printed in these prospective PLAN documents. Historical OR intervals contain their point estimates and have ordered endpoints. No trial noninferiority/equivalence margin or formal efficacy/futility interim boundary occurs. Exact sample-size simulation, imputation/IPW coefficients, covariance/df, mediation fitted values and economic links are not supplied; no convention was used to fill them. Native/layout glyph encoding is covered by current complete visual maps and targeted source-page reading, with no assigned scientific unit gap. Diagnostic approximations are labelled and do not replace source analyses. Preserved source files were not changed; no web or external literature was used.

Durable handoff: statistics/parts/plans_inventory.md and checkers/parts/stat1_plans.md. Exact S set: S401,S402,S403,S404,S405,S406,S407,S408,S409,S410,S411,S412,S413,S414,S415,S416,S417,S418,S419,S420,S421,S422,S423,S424,S425,S426,S427,S428,S429,S430,S431,S432,S433,S434,S435,S436,S437,S438,S439,S440,S441,S442,S443,S444,S445,S446,S447,S448,S449,S450,S451,S452,S453,S454,S455,S456,S457,S458,S459,S460,S461,S462,S463,S464.


<!-- Complete checker part: raw -->

# Statistical pass 1 — raw-score shard

Fresh runtime task: /root/stat1_raw; model gpt-6.1-sol; reasoning effort high. Pass: 1. Exact assigned scope: REPORT DOC-005 eTable 11, physical PDF pp.17–18, all21 rows and all columns/notes. Context read solely for these relationships: REPORT DOC-005 pp.2,4–5,15 and REPORT DOC-001 pp.4,11. Complete relationship record: statistics/parts/raw_inventory.md, S601–S626, each PASS_1_COMPLETE.

Direct source p17 and p18 were rendered afresh with pinned fallback PyMuPDF1.26.4, CPU,200dpi, and visually read. P15 and main p11 finding contexts were also rendered and visually read. No web, external literature, prior candidates or prior checker conclusions were used. No plan inconsistency is asserted. All21 row tuples,63 mean-difference estimate/CI tuples,63 raw central-summary/percentile tuples and21 omnibus Ps were checked. All model point estimates are inside ordered CIs; raw centers lie in ordered percentile ranges; contrast additivity is compatible with rounding. There is no SMD in this display and no pairwise P, printed test statistic or standard error.

## Findings

### F-ST1-601

**Title:** Several raw PGIC values labeled as medians do not reproduce as medians of the specified single seven-category item.

**Exact locations and roles:** REPORT [DOC-005 p17, eTable11 title and Raw Score Median (25%-tile,75%tile) header, PGIC–Pain 6/12months PT and 12months UC; PGIC–General 3months PT and 6months UC](../../../joi250046supp4_prod_1755300121.15587.pdf#page=17). REPORT [DOC-001 p11, Table3 footnotes h/i](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11) defines both PGIC outcomes as one item, range1–7, with seven response scores enumerated1,2,3,4,5,6,7. REPORT [DOC-005 p15, Additional Unadjusted Data and Analyses](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15) describes eTable11 as providing unadjusted mean secondary outcomes and specifies no adjustment, weighting or imputation. REPORT [DOC-005 p18 note b](../../../joi250046supp4_prod_1755300121.15587.pdf#page=18) identifies the between-group quantities as linear-GEE means/95%CIs; it does not redefine raw-score medians.

**Printed values:** PGIC–Pain PT6months2.8(2.7,2.9), PT12months2.8(2.7,2.9), UC12months2.2(2.1,2.3); PGIC–General PT3months2.7(2.6,2.7), UC6months1.8(1.7,1.9). These treatment assignments follow the printed raw PT/HC/UC headings exactly, without permutation.

**Rule and reproduced calculation:** For an observed sample of responses in the stated score set {1,2,3,4,5,6,7}, an ordinary empirical median is an observed middle category when odd, or the average of the two middle categories when even. Its possible values therefore lie in {1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7}. The seven category scores are exact definitions, not rounded observations. Allow each printed one-decimal raw center its half-unit rounding interval. Distance to the closest eligible median yields:

| Exact eTable11 raw location | Printed center | Printed interval | Closest eligible median | Gap | Relative discrepancy |
|---|---:|---|---:|---:|---:|
| PGIC–Pain,6months,PT | 2.8 | [2.75,2.85] | 3.0 | 0.15 | 0.05357 |
| PGIC–Pain,12months,PT | 2.8 | [2.75,2.85] | 3.0 | 0.15 | 0.05357 |
| PGIC–Pain,12months,UC | 2.2 | [2.15,2.25] | 2.0 | 0.15 | 0.06818 |
| PGIC–General,3months,PT | 2.7 | [2.65,2.75] | 2.5 | 0.15 | 0.05556 |
| PGIC–General,6months,UC | 1.8 | [1.75,1.85] | 2.0 | 0.15 | 0.08333 |

The relative gaps are each greater than0.05. This is a check of the stated score and labeled statistic; it does not calculate or substitute a preferred analysis and does not assume that a median equals a model mean. An interpolation or score transformation that permits these medians has not been supplied for the single-item PGIC raw scores.

**Focus area:** C, statistical method logic and effect-summary identity.

**Proposed review domain:** statistical_results.

**Proposed relationship type:** S_C. **All relationships:** S_C,S_W. The supplied main REPORT defines the PGIC scale; the results supplement REPORT labels and prints the summary. The supplement's own mean description is an additional S_W quantity-definition tension. No PLAN document is a conflicting party.

**Qualifying route:** Route B.

**Affected result or extracted value:** Raw PGIC–Pain and PGIC–General outcome summaries at the five listed treatment/timepoint locations, and whether a data extractor should treat each center and pair of bounds as a median/IQR or another summary.

**Why context does not resolve it:** B1: the discrepancy concerns the statistical identity of specific reported outcome values. B2: the table explicitly labels median/percentiles, while its introductory paragraph refers to means; the linear-GEE note describes only between-group differences. No supplied score transformation or median construction explains the five values on the defined single-item scale. B3: median/IQR versus mean/interval is a different extracted quantity and determines which summary can be used in evidence synthesis. The source does not identify the intended statistic at once.

**Alternatives and missing definitions:** The raw columns could be means with uncertainty intervals, consistent with the supplement p15 description; they could instead summarize a transformed PGIC score or a defined interpolated/aggregate quantity. The supplied text does not identify such a raw-score transformation, the median rule, or an interval construction for those raw columns. In the set-valued mathematical definition of a median, any point between two middle observations can be a median; the calculation above uses the ordinary empirical rule of their average. A disclosed alternative interpolation could therefore resolve the numerical restriction. No raw data identify those middle observations. This is a limitation for the independent inclusion screen, rather than an assertion that all possible median definitions exclude the printed centers. The between-group GEE contrasts remain distinct quantities and are not themselves challenged by this finding. A diagnostic column-permutation pattern is recorded separately in S624; it is not assumed in the calculation above.

**Exact human question:** For the five PGIC raw-score entries listed above, what score and summary statistic produced the centers and bounds: empirical medians/interquartile ranges of the defined1–7 item, means with intervals, or a transformed/aggregate score? Please identify the applicable definition and confirm which statistic a data extractor should take from the raw-score columns.

**Linked relationships:** S617,S618,S619,S620,S623.

## Excluded observations

Only apparent issues decided not to emit are listed here. Reconciled checks are recorded in the S inventory.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-005p17 PGIC remaining fractional raw centers: Pain PT3=2.9,UC3=1.9,HC6=2.1,UC6=2.1,HC12=2.1; General UC3=1.6,PT12=2.6,HC12=1.9,UC12=1.9 | These centers also fall between eligible ordinary single-item medians, but their half-unit interval gaps to the nearest eligible median are0.05 and relative discrepancies range0.0172–0.0313, at most0.05. These occurrences are outside the five-location finding under the display-precision rule. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-005p17 all21 raw-summary/contrast rows, p15 intro, p18 note b | Subtracting raw centers under printed PT/HC/UC headings differs from many GEE mean contrasts. A diagnostic UC/PT/HC permutation of raw columns makes all21 contrast triples feasible within one-decimal rounding. However the raw centers explicitly represent medians and the contrasts model means; no supplied method establishes equality between the two. This numerical permutation alone does not reproduce an arm-label or mean-difference inconsistency. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-005p17 physical functioning6/12months omnibusP=.005/.001; contextual DOC-001p11 footnote c and DOC-005p15 intro | A diagnostic same-covariance normal-CI, joint two-contrast Wald reconstruction matches social3 and physical3 Ps within rounding but yields physical6 approximateP=.015–.040 and physical12 approximateP=.0036–.020. eTable11 does not specify its exact omnibus reference distribution/degrees of freedom, normal-versus-t CI rule, or whether omnibus and CIs use the same fitted covariance. An exact conflict cannot be asserted by importing these choices from convention or another display; no null/significance contradiction exists at .05. | CONDITIONAL_OR_UNREPORTED |

## Diagnostic details and limitations

The omnibus diagnostic uses h=(upper−lower)/2, SE=h/1.959964, Var(c)=Var(a)+Var(b)−2Cov(a,b) for a=PT−UC,b=HC−UC,c=HC−PT, then a quadratic Wald statistic and a chi-square2 survival probability. This is expressly an approximation and is not the supplied eTable11 test definition. Numerical exploration allowed every printed estimate and CI endpoint its0.05 half-unit interval and constrained c=b−a and symmetric intervals around each estimate. A finite grid gave social3 P approximately0.00017–0.00182 and physical3 approximately0.1529–0.3124, both containing their printed three-decimal ranges; physical6 approximately0.01520–0.04009 and physical12 approximately0.00361–0.02028. These are diagnostic grid ranges, not certified global bounds, and no precise covariance, reference distribution or degrees of freedom are inferred as the source method. The diagnostic is preserved for fresh pass2 review rather than promoted as an exact calculation.

The individual repeated measures and HC clustering are described in the main methods; eTable11 specifies linear GEE and no adjustment/weighting/imputation. This combination is internally coherent. Missing per-outcome sample counts, covariance, variance estimator and raw summary definition limit full mechanical reconstruction; the last is a source-grounded conflict for the PGIC finding, while other absent details alone are not findings. No noninferiority/equivalence/interim/stopping rule or conclusion occurs in the assigned scope. All21 source rows were covered and no scientific source-unit gap remains.

Counts: pass1; exact display scope DOC-005pp17–18;26 stable S records;21 complete row tuples;1 consolidated finding;3 excluded-observation rows. Paths: statistics/parts/raw_inventory.md;checkers/parts/stat1_raw.md; fresh derivatives preprocessing/stat1_raw/.



## Complete per-relationship pass1 completion index

This mechanical index expands the exact active shard assignments. Every listed relationship has its complete source-linked facts, check result and missing definitions in its assigned inventory part; no new scientific conclusion is assigned by this index.

| S ID | Fresh runtime | Status | Complete relationship record |
|---|---|---|---|
| S001 | root/stat1_main | PASS_1_COMPLETE | [S001 record](../statistics/parts/main_inventory.md) |
| S002 | root/stat1_main | PASS_1_COMPLETE | [S002 record](../statistics/parts/main_inventory.md) |
| S003 | root/stat1_main | PASS_1_COMPLETE | [S003 record](../statistics/parts/main_inventory.md) |
| S004 | root/stat1_main | PASS_1_COMPLETE | [S004 record](../statistics/parts/main_inventory.md) |
| S005 | root/stat1_main | PASS_1_COMPLETE | [S005 record](../statistics/parts/main_inventory.md) |
| S006 | root/stat1_main | PASS_1_COMPLETE | [S006 record](../statistics/parts/main_inventory.md) |
| S007 | root/stat1_main | PASS_1_COMPLETE | [S007 record](../statistics/parts/main_inventory.md) |
| S008 | root/stat1_main | PASS_1_COMPLETE | [S008 record](../statistics/parts/main_inventory.md) |
| S009 | root/stat1_main | PASS_1_COMPLETE | [S009 record](../statistics/parts/main_inventory.md) |
| S010 | root/stat1_main | PASS_1_COMPLETE | [S010 record](../statistics/parts/main_inventory.md) |
| S011 | root/stat1_main | PASS_1_COMPLETE | [S011 record](../statistics/parts/main_inventory.md) |
| S012 | root/stat1_main | PASS_1_COMPLETE | [S012 record](../statistics/parts/main_inventory.md) |
| S013 | root/stat1_main | PASS_1_COMPLETE | [S013 record](../statistics/parts/main_inventory.md) |
| S014 | root/stat1_main | PASS_1_COMPLETE | [S014 record](../statistics/parts/main_inventory.md) |
| S015 | root/stat1_main | PASS_1_COMPLETE | [S015 record](../statistics/parts/main_inventory.md) |
| S016 | root/stat1_main | PASS_1_COMPLETE | [S016 record](../statistics/parts/main_inventory.md) |
| S017 | root/stat1_main | PASS_1_COMPLETE | [S017 record](../statistics/parts/main_inventory.md) |
| S018 | root/stat1_main | PASS_1_COMPLETE | [S018 record](../statistics/parts/main_inventory.md) |
| S019 | root/stat1_main | PASS_1_COMPLETE | [S019 record](../statistics/parts/main_inventory.md) |
| S020 | root/stat1_main | PASS_1_COMPLETE | [S020 record](../statistics/parts/main_inventory.md) |
| S021 | root/stat1_main | PASS_1_COMPLETE | [S021 record](../statistics/parts/main_inventory.md) |
| S022 | root/stat1_main | PASS_1_COMPLETE | [S022 record](../statistics/parts/main_inventory.md) |
| S023 | root/stat1_main | PASS_1_COMPLETE | [S023 record](../statistics/parts/main_inventory.md) |
| S024 | root/stat1_main | PASS_1_COMPLETE | [S024 record](../statistics/parts/main_inventory.md) |
| S025 | root/stat1_main | PASS_1_COMPLETE | [S025 record](../statistics/parts/main_inventory.md) |
| S026 | root/stat1_main | PASS_1_COMPLETE | [S026 record](../statistics/parts/main_inventory.md) |
| S027 | root/stat1_main | PASS_1_COMPLETE | [S027 record](../statistics/parts/main_inventory.md) |
| S028 | root/stat1_main | PASS_1_COMPLETE | [S028 record](../statistics/parts/main_inventory.md) |
| S029 | root/stat1_main | PASS_1_COMPLETE | [S029 record](../statistics/parts/main_inventory.md) |
| S030 | root/stat1_main | PASS_1_COMPLETE | [S030 record](../statistics/parts/main_inventory.md) |
| S031 | root/stat1_main | PASS_1_COMPLETE | [S031 record](../statistics/parts/main_inventory.md) |
| S032 | root/stat1_main | PASS_1_COMPLETE | [S032 record](../statistics/parts/main_inventory.md) |
| S033 | root/stat1_main | PASS_1_COMPLETE | [S033 record](../statistics/parts/main_inventory.md) |
| S034 | root/stat1_main | PASS_1_COMPLETE | [S034 record](../statistics/parts/main_inventory.md) |
| S035 | root/stat1_main | PASS_1_COMPLETE | [S035 record](../statistics/parts/main_inventory.md) |
| S036 | root/stat1_main | PASS_1_COMPLETE | [S036 record](../statistics/parts/main_inventory.md) |
| S037 | root/stat1_main | PASS_1_COMPLETE | [S037 record](../statistics/parts/main_inventory.md) |
| S038 | root/stat1_main | PASS_1_COMPLETE | [S038 record](../statistics/parts/main_inventory.md) |
| S039 | root/stat1_main | PASS_1_COMPLETE | [S039 record](../statistics/parts/main_inventory.md) |
| S040 | root/stat1_main | PASS_1_COMPLETE | [S040 record](../statistics/parts/main_inventory.md) |
| S041 | root/stat1_main | PASS_1_COMPLETE | [S041 record](../statistics/parts/main_inventory.md) |
| S042 | root/stat1_main | PASS_1_COMPLETE | [S042 record](../statistics/parts/main_inventory.md) |
| S043 | root/stat1_main | PASS_1_COMPLETE | [S043 record](../statistics/parts/main_inventory.md) |
| S044 | root/stat1_main | PASS_1_COMPLETE | [S044 record](../statistics/parts/main_inventory.md) |
| S045 | root/stat1_main | PASS_1_COMPLETE | [S045 record](../statistics/parts/main_inventory.md) |
| S046 | root/stat1_main | PASS_1_COMPLETE | [S046 record](../statistics/parts/main_inventory.md) |
| S047 | root/stat1_main | PASS_1_COMPLETE | [S047 record](../statistics/parts/main_inventory.md) |
| S048 | root/stat1_main | PASS_1_COMPLETE | [S048 record](../statistics/parts/main_inventory.md) |
| S049 | root/stat1_main | PASS_1_COMPLETE | [S049 record](../statistics/parts/main_inventory.md) |
| S050 | root/stat1_main | PASS_1_COMPLETE | [S050 record](../statistics/parts/main_inventory.md) |
| S051 | root/stat1_main | PASS_1_COMPLETE | [S051 record](../statistics/parts/main_inventory.md) |
| S052 | root/stat1_main | PASS_1_COMPLETE | [S052 record](../statistics/parts/main_inventory.md) |
| S053 | root/stat1_main | PASS_1_COMPLETE | [S053 record](../statistics/parts/main_inventory.md) |
| S054 | root/stat1_main | PASS_1_COMPLETE | [S054 record](../statistics/parts/main_inventory.md) |
| S055 | root/stat1_main | PASS_1_COMPLETE | [S055 record](../statistics/parts/main_inventory.md) |
| S056 | root/stat1_main | PASS_1_COMPLETE | [S056 record](../statistics/parts/main_inventory.md) |
| S057 | root/stat1_main | PASS_1_COMPLETE | [S057 record](../statistics/parts/main_inventory.md) |
| S058 | root/stat1_main | PASS_1_COMPLETE | [S058 record](../statistics/parts/main_inventory.md) |
| S059 | root/stat1_main | PASS_1_COMPLETE | [S059 record](../statistics/parts/main_inventory.md) |
| S060 | root/stat1_main | PASS_1_COMPLETE | [S060 record](../statistics/parts/main_inventory.md) |
| S061 | root/stat1_main | PASS_1_COMPLETE | [S061 record](../statistics/parts/main_inventory.md) |
| S062 | root/stat1_main | PASS_1_COMPLETE | [S062 record](../statistics/parts/main_inventory.md) |
| S063 | root/stat1_main | PASS_1_COMPLETE | [S063 record](../statistics/parts/main_inventory.md) |
| S064 | root/stat1_main | PASS_1_COMPLETE | [S064 record](../statistics/parts/main_inventory.md) |
| S065 | root/stat1_main | PASS_1_COMPLETE | [S065 record](../statistics/parts/main_inventory.md) |
| S066 | root/stat1_main | PASS_1_COMPLETE | [S066 record](../statistics/parts/main_inventory.md) |
| S067 | root/stat1_main | PASS_1_COMPLETE | [S067 record](../statistics/parts/main_inventory.md) |
| S068 | root/stat1_main | PASS_1_COMPLETE | [S068 record](../statistics/parts/main_inventory.md) |
| S069 | root/stat1_main | PASS_1_COMPLETE | [S069 record](../statistics/parts/main_inventory.md) |
| S070 | root/stat1_main | PASS_1_COMPLETE | [S070 record](../statistics/parts/main_inventory.md) |
| S071 | root/stat1_main | PASS_1_COMPLETE | [S071 record](../statistics/parts/main_inventory.md) |
| S072 | root/stat1_main | PASS_1_COMPLETE | [S072 record](../statistics/parts/main_inventory.md) |
| S073 | root/stat1_main | PASS_1_COMPLETE | [S073 record](../statistics/parts/main_inventory.md) |
| S074 | root/stat1_main | PASS_1_COMPLETE | [S074 record](../statistics/parts/main_inventory.md) |
| S075 | root/stat1_main | PASS_1_COMPLETE | [S075 record](../statistics/parts/main_inventory.md) |
| S076 | root/stat1_main | PASS_1_COMPLETE | [S076 record](../statistics/parts/main_inventory.md) |
| S077 | root/stat1_main | PASS_1_COMPLETE | [S077 record](../statistics/parts/main_inventory.md) |
| S078 | root/stat1_main | PASS_1_COMPLETE | [S078 record](../statistics/parts/main_inventory.md) |
| S079 | root/stat1_main | PASS_1_COMPLETE | [S079 record](../statistics/parts/main_inventory.md) |
| S080 | root/stat1_main | PASS_1_COMPLETE | [S080 record](../statistics/parts/main_inventory.md) |
| S081 | root/stat1_main | PASS_1_COMPLETE | [S081 record](../statistics/parts/main_inventory.md) |
| S082 | root/stat1_main | PASS_1_COMPLETE | [S082 record](../statistics/parts/main_inventory.md) |
| S083 | root/stat1_main | PASS_1_COMPLETE | [S083 record](../statistics/parts/main_inventory.md) |
| S084 | root/stat1_main | PASS_1_COMPLETE | [S084 record](../statistics/parts/main_inventory.md) |
| S085 | root/stat1_main | PASS_1_COMPLETE | [S085 record](../statistics/parts/main_inventory.md) |
| S086 | root/stat1_main | PASS_1_COMPLETE | [S086 record](../statistics/parts/main_inventory.md) |
| S087 | root/stat1_main | PASS_1_COMPLETE | [S087 record](../statistics/parts/main_inventory.md) |
| S088 | root/stat1_main | PASS_1_COMPLETE | [S088 record](../statistics/parts/main_inventory.md) |
| S089 | root/stat1_main | PASS_1_COMPLETE | [S089 record](../statistics/parts/main_inventory.md) |
| S090 | root/stat1_main | PASS_1_COMPLETE | [S090 record](../statistics/parts/main_inventory.md) |
| S091 | root/stat1_main | PASS_1_COMPLETE | [S091 record](../statistics/parts/main_inventory.md) |
| S092 | root/stat1_main | PASS_1_COMPLETE | [S092 record](../statistics/parts/main_inventory.md) |
| S093 | root/stat1_main | PASS_1_COMPLETE | [S093 record](../statistics/parts/main_inventory.md) |
| S094 | root/stat1_main | PASS_1_COMPLETE | [S094 record](../statistics/parts/main_inventory.md) |
| S095 | root/stat1_main | PASS_1_COMPLETE | [S095 record](../statistics/parts/main_inventory.md) |
| S096 | root/stat1_main | PASS_1_COMPLETE | [S096 record](../statistics/parts/main_inventory.md) |
| S097 | root/stat1_main | PASS_1_COMPLETE | [S097 record](../statistics/parts/main_inventory.md) |
| S098 | root/stat1_main | PASS_1_COMPLETE | [S098 record](../statistics/parts/main_inventory.md) |
| S099 | root/stat1_main | PASS_1_COMPLETE | [S099 record](../statistics/parts/main_inventory.md) |
| S100 | root/stat1_main | PASS_1_COMPLETE | [S100 record](../statistics/parts/main_inventory.md) |
| S101 | root/stat1_main | PASS_1_COMPLETE | [S101 record](../statistics/parts/main_inventory.md) |
| S102 | root/stat1_main | PASS_1_COMPLETE | [S102 record](../statistics/parts/main_inventory.md) |
| S103 | root/stat1_main | PASS_1_COMPLETE | [S103 record](../statistics/parts/main_inventory.md) |
| S104 | root/stat1_main | PASS_1_COMPLETE | [S104 record](../statistics/parts/main_inventory.md) |
| S105 | root/stat1_main | PASS_1_COMPLETE | [S105 record](../statistics/parts/main_inventory.md) |
| S106 | root/stat1_main | PASS_1_COMPLETE | [S106 record](../statistics/parts/main_inventory.md) |
| S107 | root/stat1_main | PASS_1_COMPLETE | [S107 record](../statistics/parts/main_inventory.md) |
| S108 | root/stat1_main | PASS_1_COMPLETE | [S108 record](../statistics/parts/main_inventory.md) |
| S109 | root/stat1_main | PASS_1_COMPLETE | [S109 record](../statistics/parts/main_inventory.md) |
| S110 | root/stat1_main | PASS_1_COMPLETE | [S110 record](../statistics/parts/main_inventory.md) |
| S201 | root/stat1_reports | PASS_1_COMPLETE | [S201 record](../statistics/parts/reports_inventory.md) |
| S202 | root/stat1_reports | PASS_1_COMPLETE | [S202 record](../statistics/parts/reports_inventory.md) |
| S203 | root/stat1_reports | PASS_1_COMPLETE | [S203 record](../statistics/parts/reports_inventory.md) |
| S204 | root/stat1_reports | PASS_1_COMPLETE | [S204 record](../statistics/parts/reports_inventory.md) |
| S205 | root/stat1_reports | PASS_1_COMPLETE | [S205 record](../statistics/parts/reports_inventory.md) |
| S206 | root/stat1_reports | PASS_1_COMPLETE | [S206 record](../statistics/parts/reports_inventory.md) |
| S207 | root/stat1_reports | PASS_1_COMPLETE | [S207 record](../statistics/parts/reports_inventory.md) |
| S208 | root/stat1_reports | PASS_1_COMPLETE | [S208 record](../statistics/parts/reports_inventory.md) |
| S209 | root/stat1_reports | PASS_1_COMPLETE | [S209 record](../statistics/parts/reports_inventory.md) |
| S210 | root/stat1_reports | PASS_1_COMPLETE | [S210 record](../statistics/parts/reports_inventory.md) |
| S211 | root/stat1_reports | PASS_1_COMPLETE | [S211 record](../statistics/parts/reports_inventory.md) |
| S212 | root/stat1_reports | PASS_1_COMPLETE | [S212 record](../statistics/parts/reports_inventory.md) |
| S213 | root/stat1_reports | PASS_1_COMPLETE | [S213 record](../statistics/parts/reports_inventory.md) |
| S214 | root/stat1_reports | PASS_1_COMPLETE | [S214 record](../statistics/parts/reports_inventory.md) |
| S215 | root/stat1_reports | PASS_1_COMPLETE | [S215 record](../statistics/parts/reports_inventory.md) |
| S216 | root/stat1_reports | PASS_1_COMPLETE | [S216 record](../statistics/parts/reports_inventory.md) |
| S217 | root/stat1_reports | PASS_1_COMPLETE | [S217 record](../statistics/parts/reports_inventory.md) |
| S218 | root/stat1_reports | PASS_1_COMPLETE | [S218 record](../statistics/parts/reports_inventory.md) |
| S219 | root/stat1_reports | PASS_1_COMPLETE | [S219 record](../statistics/parts/reports_inventory.md) |
| S220 | root/stat1_reports | PASS_1_COMPLETE | [S220 record](../statistics/parts/reports_inventory.md) |
| S221 | root/stat1_reports | PASS_1_COMPLETE | [S221 record](../statistics/parts/reports_inventory.md) |
| S222 | root/stat1_reports | PASS_1_COMPLETE | [S222 record](../statistics/parts/reports_inventory.md) |
| S223 | root/stat1_reports | PASS_1_COMPLETE | [S223 record](../statistics/parts/reports_inventory.md) |
| S224 | root/stat1_reports | PASS_1_COMPLETE | [S224 record](../statistics/parts/reports_inventory.md) |
| S225 | root/stat1_reports | PASS_1_COMPLETE | [S225 record](../statistics/parts/reports_inventory.md) |
| S226 | root/stat1_reports | PASS_1_COMPLETE | [S226 record](../statistics/parts/reports_inventory.md) |
| S227 | root/stat1_reports | PASS_1_COMPLETE | [S227 record](../statistics/parts/reports_inventory.md) |
| S228 | root/stat1_reports | PASS_1_COMPLETE | [S228 record](../statistics/parts/reports_inventory.md) |
| S229 | root/stat1_reports | PASS_1_COMPLETE | [S229 record](../statistics/parts/reports_inventory.md) |
| S230 | root/stat1_reports | PASS_1_COMPLETE | [S230 record](../statistics/parts/reports_inventory.md) |
| S231 | root/stat1_reports | PASS_1_COMPLETE | [S231 record](../statistics/parts/reports_inventory.md) |
| S232 | root/stat1_reports | PASS_1_COMPLETE | [S232 record](../statistics/parts/reports_inventory.md) |
| S233 | root/stat1_reports | PASS_1_COMPLETE | [S233 record](../statistics/parts/reports_inventory.md) |
| S234 | root/stat1_reports | PASS_1_COMPLETE | [S234 record](../statistics/parts/reports_inventory.md) |
| S235 | root/stat1_reports | PASS_1_COMPLETE | [S235 record](../statistics/parts/reports_inventory.md) |
| S236 | root/stat1_reports | PASS_1_COMPLETE | [S236 record](../statistics/parts/reports_inventory.md) |
| S237 | root/stat1_reports | PASS_1_COMPLETE | [S237 record](../statistics/parts/reports_inventory.md) |
| S238 | root/stat1_reports | PASS_1_COMPLETE | [S238 record](../statistics/parts/reports_inventory.md) |
| S239 | root/stat1_reports | PASS_1_COMPLETE | [S239 record](../statistics/parts/reports_inventory.md) |
| S240 | root/stat1_reports | PASS_1_COMPLETE | [S240 record](../statistics/parts/reports_inventory.md) |
| S241 | root/stat1_reports | PASS_1_COMPLETE | [S241 record](../statistics/parts/reports_inventory.md) |
| S242 | root/stat1_reports | PASS_1_COMPLETE | [S242 record](../statistics/parts/reports_inventory.md) |
| S243 | root/stat1_reports | PASS_1_COMPLETE | [S243 record](../statistics/parts/reports_inventory.md) |
| S244 | root/stat1_reports | PASS_1_COMPLETE | [S244 record](../statistics/parts/reports_inventory.md) |
| S245 | root/stat1_reports | PASS_1_COMPLETE | [S245 record](../statistics/parts/reports_inventory.md) |
| S246 | root/stat1_reports | PASS_1_COMPLETE | [S246 record](../statistics/parts/reports_inventory.md) |
| S247 | root/stat1_reports | PASS_1_COMPLETE | [S247 record](../statistics/parts/reports_inventory.md) |
| S248 | root/stat1_reports | PASS_1_COMPLETE | [S248 record](../statistics/parts/reports_inventory.md) |
| S249 | root/stat1_reports | PASS_1_COMPLETE | [S249 record](../statistics/parts/reports_inventory.md) |
| S250 | root/stat1_reports | PASS_1_COMPLETE | [S250 record](../statistics/parts/reports_inventory.md) |
| S251 | root/stat1_reports | PASS_1_COMPLETE | [S251 record](../statistics/parts/reports_inventory.md) |
| S252 | root/stat1_reports | PASS_1_COMPLETE | [S252 record](../statistics/parts/reports_inventory.md) |
| S253 | root/stat1_reports | PASS_1_COMPLETE | [S253 record](../statistics/parts/reports_inventory.md) |
| S254 | root/stat1_reports | PASS_1_COMPLETE | [S254 record](../statistics/parts/reports_inventory.md) |
| S255 | root/stat1_reports | PASS_1_COMPLETE | [S255 record](../statistics/parts/reports_inventory.md) |
| S256 | root/stat1_reports | PASS_1_COMPLETE | [S256 record](../statistics/parts/reports_inventory.md) |
| S257 | root/stat1_reports | PASS_1_COMPLETE | [S257 record](../statistics/parts/reports_inventory.md) |
| S258 | root/stat1_reports | PASS_1_COMPLETE | [S258 record](../statistics/parts/reports_inventory.md) |
| S259 | root/stat1_reports | PASS_1_COMPLETE | [S259 record](../statistics/parts/reports_inventory.md) |
| S260 | root/stat1_reports | PASS_1_COMPLETE | [S260 record](../statistics/parts/reports_inventory.md) |
| S261 | root/stat1_reports | PASS_1_COMPLETE | [S261 record](../statistics/parts/reports_inventory.md) |
| S262 | root/stat1_reports | PASS_1_COMPLETE | [S262 record](../statistics/parts/reports_inventory.md) |
| S263 | root/stat1_reports | PASS_1_COMPLETE | [S263 record](../statistics/parts/reports_inventory.md) |
| S401 | root/stat1_plans | PASS_1_COMPLETE | [S401 record](../statistics/parts/plans_inventory.md) |
| S402 | root/stat1_plans | PASS_1_COMPLETE | [S402 record](../statistics/parts/plans_inventory.md) |
| S403 | root/stat1_plans | PASS_1_COMPLETE | [S403 record](../statistics/parts/plans_inventory.md) |
| S404 | root/stat1_plans | PASS_1_COMPLETE | [S404 record](../statistics/parts/plans_inventory.md) |
| S405 | root/stat1_plans | PASS_1_COMPLETE | [S405 record](../statistics/parts/plans_inventory.md) |
| S406 | root/stat1_plans | PASS_1_COMPLETE | [S406 record](../statistics/parts/plans_inventory.md) |
| S407 | root/stat1_plans | PASS_1_COMPLETE | [S407 record](../statistics/parts/plans_inventory.md) |
| S408 | root/stat1_plans | PASS_1_COMPLETE | [S408 record](../statistics/parts/plans_inventory.md) |
| S409 | root/stat1_plans | PASS_1_COMPLETE | [S409 record](../statistics/parts/plans_inventory.md) |
| S410 | root/stat1_plans | PASS_1_COMPLETE | [S410 record](../statistics/parts/plans_inventory.md) |
| S411 | root/stat1_plans | PASS_1_COMPLETE | [S411 record](../statistics/parts/plans_inventory.md) |
| S412 | root/stat1_plans | PASS_1_COMPLETE | [S412 record](../statistics/parts/plans_inventory.md) |
| S413 | root/stat1_plans | PASS_1_COMPLETE | [S413 record](../statistics/parts/plans_inventory.md) |
| S414 | root/stat1_plans | PASS_1_COMPLETE | [S414 record](../statistics/parts/plans_inventory.md) |
| S415 | root/stat1_plans | PASS_1_COMPLETE | [S415 record](../statistics/parts/plans_inventory.md) |
| S416 | root/stat1_plans | PASS_1_COMPLETE | [S416 record](../statistics/parts/plans_inventory.md) |
| S417 | root/stat1_plans | PASS_1_COMPLETE | [S417 record](../statistics/parts/plans_inventory.md) |
| S418 | root/stat1_plans | PASS_1_COMPLETE | [S418 record](../statistics/parts/plans_inventory.md) |
| S419 | root/stat1_plans | PASS_1_COMPLETE | [S419 record](../statistics/parts/plans_inventory.md) |
| S420 | root/stat1_plans | PASS_1_COMPLETE | [S420 record](../statistics/parts/plans_inventory.md) |
| S421 | root/stat1_plans | PASS_1_COMPLETE | [S421 record](../statistics/parts/plans_inventory.md) |
| S422 | root/stat1_plans | PASS_1_COMPLETE | [S422 record](../statistics/parts/plans_inventory.md) |
| S423 | root/stat1_plans | PASS_1_COMPLETE | [S423 record](../statistics/parts/plans_inventory.md) |
| S424 | root/stat1_plans | PASS_1_COMPLETE | [S424 record](../statistics/parts/plans_inventory.md) |
| S425 | root/stat1_plans | PASS_1_COMPLETE | [S425 record](../statistics/parts/plans_inventory.md) |
| S426 | root/stat1_plans | PASS_1_COMPLETE | [S426 record](../statistics/parts/plans_inventory.md) |
| S427 | root/stat1_plans | PASS_1_COMPLETE | [S427 record](../statistics/parts/plans_inventory.md) |
| S428 | root/stat1_plans | PASS_1_COMPLETE | [S428 record](../statistics/parts/plans_inventory.md) |
| S429 | root/stat1_plans | PASS_1_COMPLETE | [S429 record](../statistics/parts/plans_inventory.md) |
| S430 | root/stat1_plans | PASS_1_COMPLETE | [S430 record](../statistics/parts/plans_inventory.md) |
| S431 | root/stat1_plans | PASS_1_COMPLETE | [S431 record](../statistics/parts/plans_inventory.md) |
| S432 | root/stat1_plans | PASS_1_COMPLETE | [S432 record](../statistics/parts/plans_inventory.md) |
| S433 | root/stat1_plans | PASS_1_COMPLETE | [S433 record](../statistics/parts/plans_inventory.md) |
| S434 | root/stat1_plans | PASS_1_COMPLETE | [S434 record](../statistics/parts/plans_inventory.md) |
| S435 | root/stat1_plans | PASS_1_COMPLETE | [S435 record](../statistics/parts/plans_inventory.md) |
| S436 | root/stat1_plans | PASS_1_COMPLETE | [S436 record](../statistics/parts/plans_inventory.md) |
| S437 | root/stat1_plans | PASS_1_COMPLETE | [S437 record](../statistics/parts/plans_inventory.md) |
| S438 | root/stat1_plans | PASS_1_COMPLETE | [S438 record](../statistics/parts/plans_inventory.md) |
| S439 | root/stat1_plans | PASS_1_COMPLETE | [S439 record](../statistics/parts/plans_inventory.md) |
| S440 | root/stat1_plans | PASS_1_COMPLETE | [S440 record](../statistics/parts/plans_inventory.md) |
| S441 | root/stat1_plans | PASS_1_COMPLETE | [S441 record](../statistics/parts/plans_inventory.md) |
| S442 | root/stat1_plans | PASS_1_COMPLETE | [S442 record](../statistics/parts/plans_inventory.md) |
| S443 | root/stat1_plans | PASS_1_COMPLETE | [S443 record](../statistics/parts/plans_inventory.md) |
| S444 | root/stat1_plans | PASS_1_COMPLETE | [S444 record](../statistics/parts/plans_inventory.md) |
| S445 | root/stat1_plans | PASS_1_COMPLETE | [S445 record](../statistics/parts/plans_inventory.md) |
| S446 | root/stat1_plans | PASS_1_COMPLETE | [S446 record](../statistics/parts/plans_inventory.md) |
| S447 | root/stat1_plans | PASS_1_COMPLETE | [S447 record](../statistics/parts/plans_inventory.md) |
| S448 | root/stat1_plans | PASS_1_COMPLETE | [S448 record](../statistics/parts/plans_inventory.md) |
| S449 | root/stat1_plans | PASS_1_COMPLETE | [S449 record](../statistics/parts/plans_inventory.md) |
| S450 | root/stat1_plans | PASS_1_COMPLETE | [S450 record](../statistics/parts/plans_inventory.md) |
| S451 | root/stat1_plans | PASS_1_COMPLETE | [S451 record](../statistics/parts/plans_inventory.md) |
| S452 | root/stat1_plans | PASS_1_COMPLETE | [S452 record](../statistics/parts/plans_inventory.md) |
| S453 | root/stat1_plans | PASS_1_COMPLETE | [S453 record](../statistics/parts/plans_inventory.md) |
| S454 | root/stat1_plans | PASS_1_COMPLETE | [S454 record](../statistics/parts/plans_inventory.md) |
| S455 | root/stat1_plans | PASS_1_COMPLETE | [S455 record](../statistics/parts/plans_inventory.md) |
| S456 | root/stat1_plans | PASS_1_COMPLETE | [S456 record](../statistics/parts/plans_inventory.md) |
| S457 | root/stat1_plans | PASS_1_COMPLETE | [S457 record](../statistics/parts/plans_inventory.md) |
| S458 | root/stat1_plans | PASS_1_COMPLETE | [S458 record](../statistics/parts/plans_inventory.md) |
| S459 | root/stat1_plans | PASS_1_COMPLETE | [S459 record](../statistics/parts/plans_inventory.md) |
| S460 | root/stat1_plans | PASS_1_COMPLETE | [S460 record](../statistics/parts/plans_inventory.md) |
| S461 | root/stat1_plans | PASS_1_COMPLETE | [S461 record](../statistics/parts/plans_inventory.md) |
| S462 | root/stat1_plans | PASS_1_COMPLETE | [S462 record](../statistics/parts/plans_inventory.md) |
| S463 | root/stat1_plans | PASS_1_COMPLETE | [S463 record](../statistics/parts/plans_inventory.md) |
| S464 | root/stat1_plans | PASS_1_COMPLETE | [S464 record](../statistics/parts/plans_inventory.md) |
| S601 | root/stat1_raw | PASS_1_COMPLETE | [S601 record](../statistics/parts/raw_inventory.md) |
| S602 | root/stat1_raw | PASS_1_COMPLETE | [S602 record](../statistics/parts/raw_inventory.md) |
| S603 | root/stat1_raw | PASS_1_COMPLETE | [S603 record](../statistics/parts/raw_inventory.md) |
| S604 | root/stat1_raw | PASS_1_COMPLETE | [S604 record](../statistics/parts/raw_inventory.md) |
| S605 | root/stat1_raw | PASS_1_COMPLETE | [S605 record](../statistics/parts/raw_inventory.md) |
| S606 | root/stat1_raw | PASS_1_COMPLETE | [S606 record](../statistics/parts/raw_inventory.md) |
| S607 | root/stat1_raw | PASS_1_COMPLETE | [S607 record](../statistics/parts/raw_inventory.md) |
| S608 | root/stat1_raw | PASS_1_COMPLETE | [S608 record](../statistics/parts/raw_inventory.md) |
| S609 | root/stat1_raw | PASS_1_COMPLETE | [S609 record](../statistics/parts/raw_inventory.md) |
| S610 | root/stat1_raw | PASS_1_COMPLETE | [S610 record](../statistics/parts/raw_inventory.md) |
| S611 | root/stat1_raw | PASS_1_COMPLETE | [S611 record](../statistics/parts/raw_inventory.md) |
| S612 | root/stat1_raw | PASS_1_COMPLETE | [S612 record](../statistics/parts/raw_inventory.md) |
| S613 | root/stat1_raw | PASS_1_COMPLETE | [S613 record](../statistics/parts/raw_inventory.md) |
| S614 | root/stat1_raw | PASS_1_COMPLETE | [S614 record](../statistics/parts/raw_inventory.md) |
| S615 | root/stat1_raw | PASS_1_COMPLETE | [S615 record](../statistics/parts/raw_inventory.md) |
| S616 | root/stat1_raw | PASS_1_COMPLETE | [S616 record](../statistics/parts/raw_inventory.md) |
| S617 | root/stat1_raw | PASS_1_COMPLETE | [S617 record](../statistics/parts/raw_inventory.md) |
| S618 | root/stat1_raw | PASS_1_COMPLETE | [S618 record](../statistics/parts/raw_inventory.md) |
| S619 | root/stat1_raw | PASS_1_COMPLETE | [S619 record](../statistics/parts/raw_inventory.md) |
| S620 | root/stat1_raw | PASS_1_COMPLETE | [S620 record](../statistics/parts/raw_inventory.md) |
| S621 | root/stat1_raw | PASS_1_COMPLETE | [S621 record](../statistics/parts/raw_inventory.md) |
| S622 | root/stat1_raw | PASS_1_COMPLETE | [S622 record](../statistics/parts/raw_inventory.md) |
| S623 | root/stat1_raw | PASS_1_COMPLETE | [S623 record](../statistics/parts/raw_inventory.md) |
| S624 | root/stat1_raw | PASS_1_COMPLETE | [S624 record](../statistics/parts/raw_inventory.md) |
| S625 | root/stat1_raw | PASS_1_COMPLETE | [S625 record](../statistics/parts/raw_inventory.md) |
| S626 | root/stat1_raw | PASS_1_COMPLETE | [S626 record](../statistics/parts/raw_inventory.md) |
