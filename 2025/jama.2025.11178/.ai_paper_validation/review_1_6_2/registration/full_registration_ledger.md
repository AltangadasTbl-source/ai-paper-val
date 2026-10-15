# Candidate ledger — Workflow 1.6.2

All candidates are Pending Human Adjudication. Registration follows the complete independent initial screen:19 included findings consolidated into17 stable candidates. Source order uses earliest substantive conflicting source ID and physical page/cell, with screen-group order for ties; corroborating-only definitions do not move a candidate. All17 evidence states and document/relationship classifications are now mechanically rechecked. Inclusion audit is pending. Assigned IDs will never be deleted.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | REPORT main/TIDieR intervention duration vs PLAN protocol intervention duration | reproduced | PENDING | F-XS-002 |
| C002 | statistical_results | S_W | S_W | REPORT main adherence paragraph vs REPORT main Figure1 counts | reproduced | PENDING | F-NUM-001 |
| C003 | statistical_results | S_W | S_W | REPORT main SMD definition vs REPORT main Table3 contrasts | reproduced | PENDING | F-NUM-004, F-ST1-004 |
| C004 | statistical_results | S_W | S_W | REPORT main NNT method/Table2 internally; REPORT results supplement eTable8 internally | reproduced | PENDING | F-NUM-005 |
| C005 | protocol_report | P_R | P_R, S_C, S_W | REPORT main/results/workbook adjustment sets vs PLAN protocol/SAP primary adjustment sets | reproduced | PENDING | F-XS-003 |
| C006 | protocol_report | P_R | P_R | REPORT main secondary adjustment vs PLAN protocol/SAP secondary adjustment | reproduced | PENDING | F-XS-004 |
| C007 | protocol_report | P_R | P_R, P_P | REPORT main/results primary and sensitivity roles vs PLAN SAP roles; PLAN SAP amendment vs PLAN SAP retained methods | reproduced | PENDING | F-XS-005 |
| C008 | statistical_results | S_W | S_W | REPORT main Table2 RR intervals vs REPORT main Table2 NNT intervals | reproduced | PENDING | F-ST1-006 |
| C009 | statistical_results | S_W | S_W | REPORT main Table2 NNT point vs REPORT main Table2 NNT interval | reproduced | PENDING | F-ST1-001 |
| C010 | statistical_results | S_W | S_W | REPORT main Table3 SMD points vs REPORT main Table3 SMD intervals | reproduced | PENDING | F-ST1-002 |
| C011 | statistical_results | S_W | S_W | REPORT results supplement full primary adjustment vs REPORT results supplement restricted primary adjustment | reproduced | PENDING | F-ST1-205 |
| C012 | statistical_results | S_W | S_W | REPORT results supplement weight predictor list vs REPORT results supplement fitted weight-model coefficients | reproduced | PENDING | F-XS-007 |
| C013 | statistical_results | S_W | S_W | REPORT results supplement binary education specification vs REPORT results supplement education coefficients | reproduced | PENDING | F-XS-006 |
| C014 | statistical_results | S_W | S_W | REPORT results supplement coefficient intervals vs REPORT results supplement coefficient P values | reproduced | PENDING | F-ST1-201, F-ST1-202 |
| C015 | statistical_results | S_W | S_W | REPORT results supplement eTable8 any-follow-up total vs REPORT results supplement eTable8 three-month arm counts | reproduced | PENDING | F-NUM-003 |
| C016 | statistical_results | S_W | S_W | REPORT results supplement mean-summary narrative vs REPORT results supplement median/quartile table labels and values | reproduced | PENDING | F-XS-008 |
| C017 | statistical_results | S_W | S_W | REPORT workbook eTable3 count/percentage vs REPORT workbook denominator/missing count/footnote | reproduced | PENDING | F-NUM-002 |


## C001 — Planned versus reported online session duration

**Candidate statement:** Planned versus reported online session duration.

**Status:** Pending Human Adjudication

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main/TIDieR intervention duration vs PLAN protocol intervention duration

**Evidence state:** reproduced

**Inclusion audit:** PENDING

**Finding IDs:** F-XS-002

**Qualifying route:** Route B

**Classification rationale:** A report specification conflicts with prospective plan content; P_R takes precedence over other recorded relationships.

**Classification ambiguity:** None

### Independent screen and complete affected locations

Finding: **F-XS-002**. Earliest substantive compared location: DOC-001 p.3. Compared roles: REPORT main p.3; PLAN protocol pp.43–44; REPORT TIDieR pp.3–4. Proposed domain **protocol_report**, primary/all relationships **P_R**; main and TIDieR agree and merely corroborate the reported side.

Locations: [main p.3, Health Coach and Online Program](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=3); [protocol p.43, §10.1.1](../../../joi250046supp1_prod_1755300121.14087.pdf#page=43); [protocol p.44, coach overview](../../../joi250046supp1_prod_1755300121.14087.pdf#page=44); [TIDieR p.3, Procedures](../../../joi250046supp3_prod_1755300121.15087.pdf#page=3); [TIDieR p.4, When and How Much](../../../joi250046supp3_prod_1755300121.15087.pdf#page=4). Retain planned PT45–60 versus reported PT30–45 minutes, eight sessions/12 weeks in both; coach60 versus45–60 minutes overlaps and is context, not a separate numeric discrepancy. **Route B**: a permitted intervention-duration comparison, with unresolved convention and a different extractable treatment duration; self-pacing or a revised duration estimate remains an alternative, rather than an inferred intervention revision.

### Included finding evidence and checker provenance

Source checker: checkers/cross_source_consistency.md; finding F-XS-002.

#### F-XS-002

**Observation:** Expected session lengths differ between the protocol and the reported intervention descriptions.

**Exact locations and document roles:** PLAN [protocol p.43, section 10.1.1 painTRAINER overview](../../../joi250046supp1_prod_1755300121.14087.pdf#page=43); PLAN [protocol p.44, section 10.1.2 coach overview](../../../joi250046supp1_prod_1755300121.14087.pdf#page=44); REPORT [main article p.3, Health Coach Program and Online Program](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=3); REPORT [TIDieR p.3, Procedures row](../../../joi250046supp3_prod_1755300121.15087.pdf#page=3); REPORT [TIDieR p.4, When and How Much row](../../../joi250046supp3_prod_1755300121.15087.pdf#page=4).

**Printed values:** Protocol painTRAINER sessions take 45–60 minutes and coach sessions take 60 minutes. Main and TIDieR reports give painTRAINER 30–45 minutes and coach 45–60 minutes. All locations describe eight sessions, approximately weekly, with a 12-week intended completion period.

**Comparison logic and reproduction:** For painTRAINER, the corresponding stated lower and upper durations each differ by 15 minutes. Half-minute precision intervals are [44.5,45.5] versus [29.5,30.5] for the lower endpoint and [59.5,60.5] versus [44.5,45.5] for the upper endpoint. The gaps are 14 minutes, or 14/45=0.311 and 14/60=0.233 relative to the protocol endpoints, both above .05. Coach 60-minute expectation lies at the reported range's upper endpoint and is corroborating context, not a separately reproduced numeric-copy discrepancy. This single finding concerns the changed session-duration description, primarily the painTRAINER range.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** The duration/dose of the online intervention associated with the primary RR1.28 versus UC and HC-versus-PT RR1.20.

**Why context does not resolve it:** The supplied report does not explain whether the shorter online durations reflect a program revision, delivered duration, or a revised expectation. The range changes the intervention dose extracted for replication or synthesis.

**Supported alternatives:** The protocol may provide a conservative completion estimate whereas the reports describe experience during the trial; a revised duration estimate or session-content change is another possibility. The source confirms self-pacing and pause/resume features but does not select between these readings.

**Human question:** Does 30–45 versus 45–60 minutes describe a revised online session dose, actual completion time, or different duration conventions, and which planned and delivered duration should be extracted?


## C002 — Therapeutic-dose adherence percentage

**Candidate statement:** Therapeutic-dose adherence percentage.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main adherence paragraph vs REPORT main Figure1 counts

**Evidence state:** reproduced

**Inclusion audit:** PENDING

**Finding IDs:** F-NUM-001

**Qualifying route:** Route A, category 3

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

### Independent screen and complete affected locations

Finding: **F-NUM-001**. Earliest location: DOC-001 p.4. REPORT versus REPORT within main; domain **statistical_results**, primary/all relationships **S_W**. Locations: [main p.4, Results adherence paragraph](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4) and [p.5, Figure 1 PT allocation/session counts](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=5). **Route A, category 3**: retain 371 (43%) of randomized776 and the complete precision calculation above; Figure 1 corroborates 371 for6–8 sessions. No stated alternative denominator supports43%.

### Included finding evidence and checker provenance

Source checker: checkers/numeric_consistency.md; finding F-NUM-001.

#### F-NUM-001

PainTRAINER therapeutic-dose count and percentage do not reconcile.

- **Exact source locations and roles:** REPORT [main article PDF p.4, Results adherence paragraph, printed p.595](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), REPORT [p.5 Figure 1, painTRAINER allocation and session categories, printed p.596](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=5).
- **Printed inputs:** Of those randomized to painTRAINER, 371 (43%) completed at least 6 sessions. Figure 1 gives 776 randomized, 371 completing 6–8 sessions,156 completing 1–5 and 249 none. At least one session is separately 527 (68%).
- **Rule and calculation:** Percentage is 100×371/776=47.809278%. Half-unit inputs give [100×370.5/776.5,100×371.5/775.5]=[47.714102%,47.904578%]. Printed 43% interval=[42.5%,43.5%]. Remaining gap=4.214102 percentage points; relative gap=4.214102/43=0.098002>0.05.
- **Focus area:** A, counts and denominators.
- **Proposed review domain:** statistical_results.
- **Proposed relationship type:** S_W.
- **Qualifying route:** Route A, category 3.
- **Affected result or extracted value:** The proportion of randomized painTRAINER participants receiving the stated therapeutic dose of at least six sessions.
- **Why context does not resolve it:** Route A category 3 applies to the count/denominator/percentage relationship in the adherence display. The readable neighboring 68% value does not remove the conflicting 43% reading.
- **Alternatives and missing definition:** An alternative denominator would be required to yield 43%; neither 776 randomized nor 527 initiating sessions yields it. The count may describe a different dose category, but Figure 1 repeats 371 for 6–8 sessions. No alternative denominator or category is stated.
- **Exact human question:** Which numerator, denominator and percentage should represent painTRAINER participants completing at least six sessions?


## C003 — SMD construction across Table 3

**Candidate statement:** SMD construction across Table 3.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main SMD definition vs REPORT main Table3 contrasts

**Evidence state:** reproduced

**Inclusion audit:** PENDING

**Finding IDs:** F-NUM-004, F-ST1-004

**Qualifying route:** Route A, category 4

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

### Independent screen and complete affected locations

Included findings: **F-NUM-004, F-ST1-004**. Earliest location: DOC-001 p.4 SMD definition. REPORT versus REPORT within main; domain **statistical_results**, primary/all relationships **S_W**. Locations: [main p.4, SMD method](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), [p.10, all severity/intensity/interference/social/physical MD and SMD columns](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), [p.11, both PGIC blocks and footnote d](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11).

Retain all three contrasts for the following20 outcome/time rows: severity3/12 months; intensity3/6/12; interference3/6/12; social3/6/12; physical3/6/12; PGIC-pain3/6/12; PGIC-general3/6/12. Seventeen rows have the additive-triple discrepancy in F-NUM-004, and the other three are severity12, intensity3 and interference12, where MD/SMD scaling gives HC/PT intervals [−.036429,.036429], [−.043,.043], [−.029444,.029444], versus printed −.11,−.08,−.12, remaining relative gaps .623377,.400,.712963. Retain physical3 HC/UC and physical6/12 HC/PT and PGIC-pain12 HC/PT sign comparisons as additional manifestations within those rows. **Route B** qualifies the numeric-checker pattern; **Route A, category 4** additionally qualifies the expanded method-reproduction pattern because the common-SD definition does reproduce severity6 within the required precision. Do not split additive, scale and sign manifestations of this same standardized-contrast construction. Actual UC-change SDs and fitted code are absent; different standardizers or contrast assignments remain questions, not assumptions.

### Included finding evidence and checker provenance

Source checker: checkers/numeric_consistency.md; finding F-NUM-004.

#### F-NUM-004

The stated common-denominator definition of SMD does not reproduce the three displayed pairwise SMD point estimates in 17 Table 3 rows.

- **Exact source locations and roles:** REPORT [main PDF p.4 Statistical Analysis SMD definition](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), REPORT [p.10 Table 3](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), REPORT [p.11 Table 3 continuation and footnote d](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11). Every affected outcome/timepoint is listed below.
- **Printed inputs and rule:** SMD is adjusted mean difference divided by the standard deviation of change in the usual care plus group at the given time. For three common adjusted group means and one common positive denominator, SMD(HC−UC)=SMD(PT−UC)+SMD(HC−PT). Each printed SMD has precision 0.01; the sum has ±0.010 input interval and HC−UC output has ±0.005. Remaining gap=max(0,|b−a−c|−0.015), relative to|b|. This comparison is between model-based contrasts from the same display, not between a model and a crude ratio.

| Outcome/time | PT−UC | HC−UC printed | HC−PT | Recomputed HC−UC interval | Printed interval | Gap | Relative gap |
|---|---:|---:|---:|---|---|---:|---:|
| Severity 3 mo | -0.25 | -0.34 | -0.13 | -0.390 to -0.370 | -0.345 to -0.335 | 0.025 | 0.073529 |
| Intensity 6 mo | -0.17 | -0.27 | -0.04 | -0.220 to -0.200 | -0.275 to -0.265 | 0.045 | 0.166667 |
| Intensity 12 mo | -0.16 | -0.27 | -0.03 | -0.200 to -0.180 | -0.275 to -0.265 | 0.065 | 0.240741 |
| Interference 3 mo | -0.25 | -0.34 | -0.13 | -0.390 to -0.370 | -0.345 to -0.335 | 0.025 | 0.073529 |
| Interference 6 mo | -0.27 | -0.37 | -0.14 | -0.420 to -0.400 | -0.375 to -0.365 | 0.025 | 0.067568 |
| Social 3 mo | 0.12 | 0.01 | 0.20 | 0.310 to 0.330 | 0.005 to 0.015 | 0.295 | 29.500000 |
| Social 6 mo | 0.18 | 0.06 | 0.26 | 0.430 to 0.450 | 0.055 to 0.065 | 0.365 | 6.083333 |
| Social 12 mo | 0.19 | 0.07 | 0.27 | 0.450 to 0.470 | 0.065 to 0.075 | 0.375 | 5.357143 |
| Physical 3 mo | 0.09 | -0.02 | 0.16 | 0.240 to 0.260 | -0.025 to -0.015 | 0.255 | 12.750000 |
| Physical 6 mo | 0.15 | 0.02 | 0.22 | 0.360 to 0.380 | 0.015 to 0.025 | 0.335 | 16.750000 |
| Physical 12 mo | 0.20 | 0.07 | 0.27 | 0.460 to 0.480 | 0.065 to 0.075 | 0.385 | 5.500000 |
| PGIC pain 3 mo | -0.62 | -0.62 | -0.37 | -1.000 to -0.980 | -0.625 to -0.615 | 0.355 | 0.572581 |
| PGIC pain 6 mo | -0.54 | -0.55 | -0.29 | -0.840 to -0.820 | -0.555 to -0.545 | 0.265 | 0.481818 |
| PGIC pain 12 mo | -0.55 | -0.57 | -0.29 | -0.850 to -0.830 | -0.575 to -0.565 | 0.255 | 0.447368 |
| PGIC general 3 mo | -0.66 | -0.66 | -0.40 | -1.070 to -1.050 | -0.665 to -0.655 | 0.385 | 0.583333 |
| PGIC general 6 mo | -0.46 | -0.50 | -0.24 | -0.710 to -0.690 | -0.505 to -0.495 | 0.185 | 0.370000 |
| PGIC general 12 mo | -0.53 | -0.58 | -0.28 | -0.820 to -0.800 | -0.585 to -0.575 | 0.215 | 0.370690 |

- **Focus area:** C, statistical method logic and effect-measure identity.
- **Proposed review domain:** statistical_results.
- **Proposed relationship type:** S_W.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** All 17 listed standardized treatment contrasts, including direction and magnitude of standardized physical/social/global outcomes.
- **Why context does not resolve it:** The common UC denominator is explicit in both methods and footnote; the displayed contrast headings give no alternative contrast order, denominator or model definition that makes these point identities hold. Extracting the printed SMDs versus reconstructing the stated standardized contrasts produces materially different values.
- **Alternatives and missing definition:** Different contrast-specific standardizers, separate models, or a different column alignment could explain some values but none is stated. The UC change SD is not printed, so its absolute value cannot be reconstructed independently. Four rows satisfy the additive identity within precision; they are not affected locations.
- **Exact human question:** Which contrast ordering and standardizing denominator produced the 17 listed SMD triples, and how do those values follow the stated common usual-care change SD definition?

Source checker: checkers/statistical_pass_1.md; finding F-ST1-004.

#### F-ST1-004

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


## C004 — Reciprocal NNT point-reproduction pattern

**Candidate statement:** Reciprocal NNT point-reproduction pattern.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main NNT method/Table2 internally; REPORT results supplement eTable8 internally

**Evidence state:** reproduced

**Inclusion audit:** PENDING

**Finding IDs:** F-NUM-005

**Qualifying route:** Route A, category 4

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

### Independent screen and complete affected locations

Included finding: **F-NUM-005**; duplicates **F-ST1-005, F-ST1-206**. Earliest location: DOC-001 p.4 NNT method. Compared roles REPORT main and REPORT results supplement, with separate internal percentage/NNT comparisons; domain **statistical_results**, primary/all relationships **S_W** (the sources do not print conflicting copies of the same analysis).

Locations: [main p.4, NNT definition](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); [main p.9, Table 2 severity6 HC/UC, interference6 HC/UC and footnote d](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9); [supplement p.14, eTable 8 Reminder Letters Added6 months PT/UC and footnote d](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14). **Route A, category 4**: adjusted percentages37.1/22.9 with NNT8,40.9/24.3 with NNT7,35.6/21.3 with NNT8 yield the three disjoint recomputed/printed intervals in the finding justification. The reciprocal calculation reproduces the other display rows within scope tolerance. Upward integer reporting is an alternative, particularly for main rows, but cannot remove the reproduced route-A observations under the prescribed half-unit rule.

### Included finding evidence and checker provenance

Source checker: checkers/numeric_consistency.md; finding F-NUM-005.

#### F-NUM-005

Three printed NNT point estimates do not reproduce under the stated reciprocal adjusted-risk-difference method after display precision.

- **Exact source locations and roles:** REPORT [main p.9 Table 2 severity 6 months HCvsUC and interference 6 months HCvsUC, footnote d](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), REPORT [main p.4 NNT definition](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), REPORT [results supplement p.14 eTable 8 reminder-letter subset 6 months PTvsUC, footnote d](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14).
- **Printed inputs, rule and calculations:** NNT=1/(adjusted response proportion difference)=100/(difference in displayed percentage points). Each rate has half-unit 0.05 percentage points, so each difference has ±0.10; each integer NNT has ±0.5. The same rule reproduces the other point rows within the required relative-gap threshold.

| Exact row/contrast | Printed response percentages | Printed NNT | Recomputed NNT interval | Printed interval | Gap | Relative gap |
|---|---|---:|---|---|---:|---:|
| Main Table 2 severity 6 mo HC−UC |37.1 versus 22.9|8|6.993007 to 7.092199|7.5 to 8.5|0.407801|0.050975|
| Main Table 2 interference 6 mo HC−UC |40.9 versus 24.3|7|5.988024 to 6.060606|6.5 to 7.5|0.439394|0.062771|
| eTable 8 reminder subset 6 mo PT−UC |35.6 versus 21.3|8|6.944444 to 7.042254|7.5 to 8.5|0.457746|0.057218|

- **Focus area:** C, reproduced method arithmetic.
- **Proposed review domain:** statistical_results.
- **Proposed relationship type:** S_W for each document's internal rate/NNT comparison; all relationships S_W.
- **Qualifying route:** Route A, category 4.
- **Affected result or extracted value:** Adjusted NNT for the three six-month treatment contrasts listed.
- **Why context does not resolve it:** Route A category 4 applies. A convention of always rounding NNT upward might explain integer presentation, but the mandated half-unit/relative-gap rule leaves discrepancies greater than 0.05 in these rows and no alternative computation is stated.
- **Alternatives and missing definition:** Upward integer rounding, an undisplayed risk difference, or another method may have been used. The half-unit bounds of the displayed adjusted percentages cannot support these printed integer readings under ordinary rounding. No raw counts are used in this comparison.
- **Exact human question:** Which unrounded adjusted risk differences and integer-reporting rule produced these three NNT point estimates?

Related screened duplicate findings (not included Finding IDs): F-ST1-005, F-ST1-206. Their full affected locations are retained in the consolidated screen group and checker outputs.


## C005 — Age as a prespecified base adjustment covariate

**Candidate statement:** Age as a prespecified base adjustment covariate.

**Status:** Pending Human Adjudication

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C, S_W

**Compared document roles:** REPORT main/results/workbook adjustment sets vs PLAN protocol/SAP primary adjustment sets

**Evidence state:** reproduced

**Inclusion audit:** PENDING

**Finding IDs:** F-XS-003

**Qualifying route:** Route A, category 5

**Classification rationale:** A report specification conflicts with prospective plan content; P_R takes precedence over other recorded relationships.

**Classification ambiguity:** None

### Independent screen and complete affected locations

Finding: **F-XS-003**. Earliest location: DOC-001 p.4 adjustment list. Compared roles REPORT main/results/workbook versus PLAN protocol/SAP; domain **protocol_report**, primary relationship **P_R**, all relationships **P_R, S_C, S_W**.

Locations: [main p.4, Statistical Analysis covariates](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); [protocol p.56, §15.5](../../../joi250046supp1_prod_1755300121.14087.pdf#page=56); [SAP p.20, §§13–14](../../../joi250046supp2_prod_1755300121.15087.pdf#page=20); [results p.4, Adjustment](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4); [p.7 eTable 2 all-model variables](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); [p.8 eTable 3 age](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8); [p.9 eTable 4 age](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); [p.10 eTable 5 age](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); [workbook eTable 3, G2, A10 and G10](../../../joi250046supp5_prod_1755300121.16087.xlsx). **Route A, category 5**: retain the six-factor explicit plan/main specification versus the report's seven-factor prespecified base set and workbook age flag. SAP§13 names age as a potential baseline variable, not fixed primary adjustment; a missing additional prospective specification remains an alternative.

### Included finding evidence and checker provenance

Source checker: checkers/cross_source_consistency.md; finding F-XS-003.

#### F-XS-003

**Observation:** Age is described as a prespecified base adjustment factor in report material, although the supplied primary analysis specifications do not include it in that set.

**Exact locations and document roles:** PLAN [protocol p.56, section 15.5 adjustment list](../../../joi250046supp1_prod_1755300121.14087.pdf#page=56); PLAN [SAP p.20, section 14 adjustment list](../../../joi250046supp2_prod_1755300121.15087.pdf#page=20); REPORT [main article p.4, Statistical Analysis adjustment sentence](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); REPORT [results supplement p.4, Adjustment, base-set sentence](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4); REPORT [results supplement p.7, eTable 2 variables included in all models](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); REPORT [p.8 eTable 3 age coefficient](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8); REPORT [p.9 eTable 4 age coefficient](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); REPORT [p.10 eTable 5 age coefficient](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); REPORT [supplied workbook, worksheet eTable 3, G2 and A10/G10](../../../joi250046supp5_prod_1755300121.16087.xlsx).

**Printed statements and values:** Both plans and main p.4 name baseline severity, sex, site, residence, multisite pain and mental-health condition for the primary model. Supplement p.4 first repeats that list, then calls the base set prespecified and inserts age. eTable 2 includes age≥65 versus <65 in all models. Age coefficients are 0.19 (0.12–0.27) in imputation, RR1.15 (1–1.33) in primary estimation, and OR0.97 (0.70–1.35) in weighting. Workbook G2 is “Pre-specified Adjustment Variables”; G10 flags age with X.

**Comparison logic and reproduction:** The six named plan factors were compared item by item; age is an additional seventh baseline factor in the reported base set and fitted models. SAP section 13 mentions age among potential baseline variables, but neither the section 14 primary specification nor the documented amendments states that it is a fixed primary adjustment factor. No numeric-copy arithmetic is required; recomputed interval and relative discrepancy are not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R, S_C, S_W.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecified versus added covariate specification for the primary severity MCID adjusted RRs1.28,1.54,1.20 and their intervals.

**Why context does not resolve it:** Category 5 applies to an analysis element described as prespecified that is not contained in the supplied primary specification. A generic potential-variable list does not identify the final fixed base model or the timing of age's addition.

**Supported alternatives:** An additional supplied-plan section or amendment may have been intended to authorize age; it may have been selected after baseline/missingness examination; or the report's prespecified wording may refer only to the six original factors. The fitted tables establish age's use, but not its prespecification.

**Human question:** Which prospective specification made age a fixed primary adjustment covariate, and was age included in the model producing the main primary results as a prespecified or subsequently added factor?


## C006 — Secondary-analysis adjustment specification

**Candidate statement:** Secondary-analysis adjustment specification.

**Status:** Pending Human Adjudication

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main secondary adjustment vs PLAN protocol/SAP secondary adjustment

**Evidence state:** reproduced

**Inclusion audit:** PENDING

**Finding IDs:** F-XS-004

**Qualifying route:** Route B

**Classification rationale:** A report specification conflicts with prospective plan content; P_R takes precedence over other recorded relationships.

**Classification ambiguity:** None

### Independent screen and complete affected locations

Finding: **F-XS-004**. Earliest location: DOC-001 p.4 secondary model paragraph. REPORT versus PLAN; domain **protocol_report**, primary/all relationships **P_R**. Locations: [main p.4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); [main p.10 Table 3](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10); [main p.11 Table 3 continuation](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11); [protocol p.57, §15.6](../../../joi250046supp1_prod_1755300121.14087.pdf#page=57); [SAP p.21, §15](../../../joi250046supp2_prod_1755300121.15087.pdf#page=21). **Route B**: preserve the plan's baseline severity/all-strata list and its “same proposed approach” phrase, versus reported primary structure plus each secondary baseline value; the latter prevents reducing the finding to a wording variation because the model producing named intensity/interference/functioning estimates remains differently specified. The inheritance phrase may authorize some common primary factors, so outcome-specific baseline adjustment is the clearest unmatched element.

### Included finding evidence and checker provenance

Source checker: checkers/cross_source_consistency.md; finding F-XS-004.

#### F-XS-004

**Observation:** The secondary outcome adjustment set is expanded in the report relative to the explicit plan lists.

**Exact locations and document roles:** PLAN [protocol p.57, section 15.6 final analysis sentence](../../../joi250046supp1_prod_1755300121.14087.pdf#page=57); PLAN [SAP p.21, section 15 secondary analysis paragraph](../../../joi250046supp2_prod_1755300121.15087.pdf#page=21); REPORT [main article p.4, secondary modeling paragraph](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); REPORT [main Table 3 pp.10–11](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10).

**Printed statements:** Both plans explicitly state baseline pain severity and all stratification variables as secondary-analysis covariates. The report says the same modeling structures as the primary analysis were applied, with added adjustment for the given baseline secondary outcome. The primary structure in the preceding paragraph additionally includes multisite pain and mental-health condition.

**Comparison logic and reproduction:** Baseline severity, sex, site and residence match. The report additionally specifies outcome-specific baseline adjustment and imports the primary structure's multisite-pain and mental-health factors. The plan's general “same proposed approach” phrase and its explicit final covariate list are retained separately; neither explicitly names the given baseline secondary outcome. This is an analysis specification comparison; recomputed interval and relative discrepancy are not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** Adjusted intensity, interference, social-role, physical-functioning and global-impression secondary estimates and mean differences in Tables 2–3.

**Why context does not resolve it:** The specific covariate lists differ and the report does not identify an amendment or distinguish which baseline terms apply to each outcome. This determines the adjusted estimand extracted for the abstract's secondary pain/functioning results.

**Supported alternatives:** “Same proposed approach” may have been intended to inherit the entire primary covariate set, while the final plan sentence gives only minimum covariates; outcome-specific baseline adjustment may have been an additional specification. A later amendment may explain the expansion.

**Human question:** What exact covariate set was planned and used for each secondary outcome, including its baseline value, multisite pain and mental-health condition, and where is any expansion documented?


## C007 — Primary versus sensitivity missing-data analysis roles

**Candidate statement:** Primary versus sensitivity missing-data analysis roles.

**Status:** Pending Human Adjudication

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** REPORT main/results primary and sensitivity roles vs PLAN SAP roles; PLAN SAP amendment vs PLAN SAP retained methods

**Evidence state:** reproduced

**Inclusion audit:** PENDING

**Finding IDs:** F-XS-005

**Qualifying route:** Route A, category 5

**Classification rationale:** A report specification conflicts with prospective plan content; P_R takes precedence over other recorded relationships.

**Classification ambiguity:** The SAP amendment and conditional weighted-first branch may explain the reported primary analysis; the retained unconditional MAR wording remains the registered comparator. Mechanical recheck confirms P_R and P_P while retaining this alternative.

### Independent screen and complete affected locations

Finding: **F-XS-005**. Earliest location: DOC-001 p.4 missing-data methods. REPORT versus PLAN, plus retained plan-internal primary/MAR versus amended pattern-mixture/IPW wording; domain **protocol_report**, primary relationship **P_R**, all relationships **P_R, P_P**.

Locations: [main p.4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); [SAP p.4, July2024 IPW amendment](../../../joi250046supp2_prod_1755300121.15087.pdf#page=4); [SAP p.19, §11](../../../joi250046supp2_prod_1755300121.15087.pdf#page=19); [results p.4 Missing Data](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4); [p.9 eTable 4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); [p.11 eTable 7 sensitivity introduction/complete-case block](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11). **Route A, category 5**: retain the different primary/follow-up/MAR and primary/weighted-MNAR labels, rather than treating different estimates as matching numeric copies. The final amendment explicitly supports adding IPW and the threshold paragraph permits a pattern-mixture first approach; these are substantive alternatives that may explain the reported implementation, but do not erase the retained unconditional primary-MAR wording and report's primary/sensitivity assignment. Do not claim that the follow-up result is absent: the corresponding complete-case estimates are supplied in eTable7.

### Included finding evidence and checker provenance

Source checker: checkers/cross_source_consistency.md; finding F-XS-005.

#### F-XS-005

**Observation:** The role of the follow-up/MAR and weighted pattern-mixture analyses differs between the SAP primary-analysis paragraph and the report.

**Exact locations and document roles:** PLAN [SAP p.19, section 11](../../../joi250046supp2_prod_1755300121.15087.pdf#page=19); PLAN [SAP p.4, July 17, 2024 IPW amendment](../../../joi250046supp2_prod_1755300121.15087.pdf#page=4); REPORT [main article p.4, missing-data paragraph](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); REPORT [results supplement p.4, Missing Data opening paragraph](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4); REPORT [p.9 eTable 4 primary estimation model](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); REPORT [p.11 eTable 7 sensitivity introduction and complete-case block](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11).

**Printed statements and values:** SAP section 11 says the primary analyses analyze patients with follow-up and assume MAR given baseline covariates, then describes sensitivity analyses when >15% missing at 3 months or group differential, including pattern-mixture/IPW and worst/best case. Its amendment says the current approach already imputes by pattern mixture and adds IPW to permit interpretation among all randomized. The report says the threshold caused the primary analysis to use MNAR imputation, nonresponse weighting and adjustment. The report's complete-case analysis is labeled sensitivity: 3-month PT/UC RR1.34 (1.12–1.61), HC/UC1.48 (1.24–1.75), HC/PT1.10 (0.94–1.29). Its primary weighted-imputed RRs are1.28,1.54,1.20.

**Comparison logic and reproduction:** These are explicitly distinct analyses and are not numeric copies. The observable difference is the assigned primary-versus-sensitivity role and associated MAR versus MNAR assumption. The >15% or differential rule is present in both sources; SAP section 11 does not explicitly state that meeting it replaces the primary MAR analysis. Recomputed numeric interval and relative discrepancy are not applicable to this specification comparison.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R, P_P.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Which three-month severity analysis is designated primary and which missing-data assumption accompanies RRs1.28,1.54,1.20.

**Why context does not resolve it:** Category 5 applies to replacement of a planned primary analysis. The amendment corroborates that weighted pattern-mixture estimation was intended, but section 11 retains the contrasting primary MAR statement and sensitivity wording; the supplied plan does not explicitly reconcile their roles.

**Supported alternatives:** The July 2024 amendment may authorize weighted MNAR as primary and section 11 may retain an earlier description; the threshold branch may have been intended to switch the primary analysis; or the report may use “primary” for an analysis that was prospectively sensitivity. The complete-case result is reported, so this finding does not assert its numerical absence.

**Human question:** Under the final approved SAP, was the primary analysis the follow-up/MAR model or the weighted MNAR pattern-mixture model, and what statement or amendment assigned the final primary-versus-sensitivity roles?


## C008 — RR versus finite NNT null coverage

**Candidate statement:** RR versus finite NNT null coverage.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table2 RR intervals vs REPORT main Table2 NNT intervals

**Evidence state:** reproduced

**Inclusion audit:** PENDING

**Finding IDs:** F-ST1-006

**Qualifying route:** Route B

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

### Independent screen and complete affected locations

Finding: **F-ST1-006**. Earliest substantive result: DOC-001 p.9; p.4 is method context. REPORT versus REPORT within main; domain **statistical_results**, primary/all relationships **S_W**. Locations: [main p.4, binary model/NNT definition](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), [main p.9, Table 2 HC/PT severity6/12, intensity3/12, interference6/12 and footnotes b,d,e](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9). **Route B**: retain the six exact RR/NNT pairs and reciprocal implied RD intervals from the finding; RR=1 and RD=0 express the same response-equality null, but interval constructions may differ. This is a direct ambiguity about displayed null coverage and benefit-interval extraction, not a reconstructed pairwise P value or an assumed exact common-covariance contradiction. Missing RD interval construction and differing parameter-specific intervals remain explicit alternatives.

### Included finding evidence and checker provenance

Source checker: checkers/statistical_pass_1.md; finding F-ST1-006.

#### F-ST1-006

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


## C009 — NNT point outside its confidence interval

**Candidate statement:** NNT point outside its confidence interval.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table2 NNT point vs REPORT main Table2 NNT interval

**Evidence state:** reproduced

**Inclusion audit:** PENDING

**Finding IDs:** F-ST1-001

**Qualifying route:** Route A, category 1

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

### Independent screen and complete affected locations

Finding: **F-ST1-001**. Earliest location: DOC-001 p.9, Table 2 intensity12 HC/PT. REPORT internal; domain **statistical_results**, primary/all relationships **S_W**. [Exact source p.9](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9): **63 (18–38)**. **Route A, category 1**: point containment fails without an inferential-method assumption; this separate rule is not merged with IG08's null-coverage question.

### Included finding evidence and checker provenance

Source checker: checkers/statistical_pass_1.md; finding F-ST1-001.

#### F-ST1-001

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


## C010 — SMD points outside printed confidence intervals

**Candidate statement:** SMD points outside printed confidence intervals.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table3 SMD points vs REPORT main Table3 SMD intervals

**Evidence state:** reproduced

**Inclusion audit:** PENDING

**Finding IDs:** F-ST1-002

**Qualifying route:** Route A, category 1

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

### Independent screen and complete affected locations

Finding: **F-ST1-002**. Earliest location: DOC-001 p.10. REPORT internal; domain **statistical_results**, primary/all relationships **S_W**. Locations: [main p.10 Table 3](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) and [p.11 PGIC-pain continuation](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11). **Route A, category 1**: preserve all fourteen tuples: severity12 PT/UC−.25(−.24,.01),HC/UC−.36(−.35,−.12); intensity12 HC/UC−.27(−.26,−.12); interference12 PT/UC−.26(−.25,.01),HC/UC−.37(−.36,−.11); physical6 PT/UC.15(.09,−.06),HC/UC.02(−.03,−.18),HC/PT.22(.16,.05); physical12 PT/UC.20(.18,−.03),HC/UC.07(.04,−.16),HC/PT.27(.25,.09); PGIC-pain12 PT/UC−.55(−.50,.05),HC/UC−.57(−.54,−.08),HC/PT−.29(−.25,.14). Sorting endpoint order does not remove any of these containment failures. This is distinct from IG03's point-construction rule; F-ST1-003's order-only observation is screened separately.

### Included finding evidence and checker provenance

Source checker: checkers/statistical_pass_1.md; finding F-ST1-002.

#### F-ST1-002

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


## C011 — Covariate set of restricted primary analyses

**Candidate statement:** Covariate set of restricted primary analyses.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement full primary adjustment vs REPORT results supplement restricted primary adjustment

**Evidence state:** reproduced

**Inclusion audit:** PENDING

**Finding IDs:** F-ST1-205

**Qualifying route:** Route B

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

### Independent screen and complete affected locations

Finding: **F-ST1-205**. Earliest substantive comparator: DOC-005 p.4 primary adjustment description. REPORT internal; domain **statistical_results**, primary/all relationships **S_W**. Locations: [results p.4, Adjustment](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4); [p.7 eTable 2 final imputation/estimation variables](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); [p.13 Protocol Change Subset Analyses](../../../joi250046supp4_prod_1755300121.15587.pdf#page=13); [p.14 eTable 8 footnote b and all three subset blocks](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14). **Route B**: education/employment are selected for primary estimation but absent from the explicit subset adjustment list despite the “primary analysis restricting to subsets” attribution. Preserve every3/6/12-month row in pre-enhancement, post-enhancement and reminder-letter blocks, especially the3-month primary-outcome estimates. An abbreviated footnote or a deliberately refitted base-only model is possible but not identified; do not infer missing weighting/imputation merely from silence.

### Included finding evidence and checker provenance

Source checker: checkers/statistical_pass_1.md; finding F-ST1-205.

#### F-ST1-205

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


## C012 — Final response-weight model predictor membership

**Candidate statement:** Final response-weight model predictor membership.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement weight predictor list vs REPORT results supplement fitted weight-model coefficients

**Evidence state:** reproduced

**Inclusion audit:** PENDING

**Finding IDs:** F-XS-007

**Qualifying route:** Route B

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

### Independent screen and complete affected locations

Included finding: **F-XS-007**; duplicate **F-ST1-203**. Earliest location: DOC-005 p.4 selection narrative; p.5 specifies weighting. REPORT internal; domain **statistical_results**, primary/all relationships **S_W**. Locations: [results p.4, Adjustment/selection](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4); [p.5, Non-Response Weighting](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5); [p.7 eTable 2 final weight-model list](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); [p.10 eTable 5 complete coefficient display](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); corroborating [workbook eTable 3 A18,H18:J18](../../../joi250046supp5_prod_1755300121.16087.xlsx). **Route B**: retain listed education versus fitted employment OR1.49(1.11,2.00),P=.008; workbook employment selection Ps<.001,.0228,.0591 corroborate possible inclusion without resolving the final education omission. This is a primary-analysis model-membership question, not peripheral coefficient copying.

### Included finding evidence and checker provenance

Source checker: checkers/cross_source_consistency.md; finding F-XS-007.

#### F-XS-007

**Observation:** The listed selected predictors for nonresponse weights differ from those displayed in the fitted weight model.

**Exact locations and document roles:** REPORT [results supplement p.7, eTable 2 final nonresponse variable list](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); REPORT [p.10, eTable 5 full coefficient display](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); REPORT [p.5, Non-Response Weighting specification](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5); REPORT [workbook worksheet eTable 3, A18 and H18:J18](../../../joi250046supp5_prod_1755300121.16087.xlsx).

**Printed values:** eTable 2 lists additional weighting predictors PEG, PHQ-8, GAD-7, any negative social determinant and education (any college versus HS or less). eTable 5 displays PEG, PHQ-8, GAD-7, negative SDOH and “Not employed” OR1.49 (1.11–2.00), P=.008, but no education term. Employment is listed for imputation/estimation, not weighting, in eTable 2. The workbook gives employment selection tests H18<.001, I18=.0228 and J18=.0591; these are separate outcome/nonresponse/3-month-missingness tests.

**Comparison logic and reproduction:** The base factors match. Four of the five additional weighting factors match; the final list specifies education where the coefficient display has employment. The source excludes health-care-site identification, not education coefficients. This is a model-membership comparison; recomputed interval and relative discrepancy are not applicable.

**Focus area:** C. **Proposed review domain:** statistical_results. **Relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** The response-weight model used for primary population-average adjusted severity RRs and percentages.

**Why context does not resolve it:** Neither the full fitted table nor the final list explains whether education, employment, or both contributed to the weights. The selection tests support possible employment inclusion but do not resolve education's absence from the displayed final fit.

**Supported alternatives:** The final list may retain an earlier selected model; the coefficient table may omit education; the weights may have used employment instead. The supplied materials do not identify the implemented predictor vector.

**Human question:** Did the final nonresponse model include education, employment, or both, and which specification generated the weights used for the primary results?

Related screened duplicate findings (not included Finding IDs): F-ST1-203. Their full affected locations are retained in the consolidated screen group and checker outputs.


## C013 — Education coding and coefficient attribution

**Candidate statement:** Education coding and coefficient attribution.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement binary education specification vs REPORT results supplement education coefficients

**Evidence state:** reproduced

**Inclusion audit:** PENDING

**Finding IDs:** F-XS-006

**Qualifying route:** Route B

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

### Independent screen and complete affected locations

Included finding: **F-XS-006**; duplicate **F-ST1-204**. Earliest location: DOC-005 p.7 eTable 2 final variable list. REPORT internal; domain **statistical_results**, primary/all relationships **S_W**. Locations: [results p.7 eTable 2 education selection](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); [p.8 eTable 3 all three education rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8); [p.9 eTable 4 all three education rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); corroborating [workbook eTable 3 A12:A16](../../../joi250046supp5_prod_1755300121.16087.xlsx). **Route B**: retain binary “any college vs HS degree or less” versus three model coefficients, both repeated AA labels and their distinct numeric estimates/intervals/Ps, and available distinct workbook categories. The repeated label alone might be wording, but the binary-versus-three-parameter model conflict prevents immediate identification of the adjustment generating the primary result and coefficient extraction.

### Included finding evidence and checker provenance

Source checker: checkers/cross_source_consistency.md; finding F-XS-006.

#### F-XS-006

**Observation:** Education is described as binary in the final selected-variable list but represented by multiple distinct parameters in the fitted primary models.

**Exact locations and document roles:** REPORT [results supplement p.7, eTable 2 final imputation/estimation variable list](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); REPORT [p.8 eTable 3 education rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8); REPORT [p.9 eTable 4 education rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); REPORT [workbook worksheet eTable 3, A12:A16](../../../joi250046supp5_prod_1755300121.16087.xlsx).

**Printed values:** eTable 2 selects education “any college vs. HS degree or less.” The imputation table has two separate AA-degree rows with estimates −0.02 (−0.11–0.08) and0.16 (0.07–0.25), and a graduate-degree row0.39 (0.29–0.49), each relative to high school or less. The estimation table similarly has education RRs0.97 (0.82–1.16),1.16 (1–1.33),1.35 (1.13–1.61). Workbook categories distinguish high school or less, associate/technical, college, doctoral/postgraduate.

**Comparison logic and reproduction:** A single binary college indicator has one coefficient relative to HS or less; three separate level coefficients describe a different design matrix. The issue is not merely the repeated AA name; the number and grouping of coefficients disagree with the binary final list. No arithmetic on rounded estimates is needed; recomputed interval and relative discrepancy are not applicable.

**Focus area:** C. **Proposed review domain:** statistical_results. **Relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** Education coding in the imputation and primary estimation models producing adjusted severity MCID results.

**Why context does not resolve it:** The reader cannot identify whether the fitted primary models used a pooled college indicator or three education levels. The workbook establishes available categories but does not identify the final model matrix.

**Supported alternatives:** The selected-variable summary may describe an initial screen rather than final coding; the fitted models may use four-category education; or some displayed parameter labels may not describe the final fit. No replacement coefficient is inferred.

**Human question:** Was education binary or represented by three nonreference levels in each final imputation and estimation model, and what educational level does each printed coefficient represent?

Related screened duplicate findings (not included Finding IDs): F-ST1-204. Their full affected locations are retained in the consolidated screen group and checker outputs.


## C014 — Coefficient CI versus P-value null-significance pattern

**Candidate statement:** Coefficient CI versus P-value null-significance pattern.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement coefficient intervals vs REPORT results supplement coefficient P values

**Evidence state:** reproduced

**Inclusion audit:** PENDING

**Finding IDs:** F-ST1-201, F-ST1-202

**Qualifying route:** Route A, category 1

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

### Independent screen and complete affected locations

Included findings: **F-ST1-201, F-ST1-202**, consolidated as one repeated coefficient interval/test compatibility issue with all10 rows. Earliest substantive location: DOC-005 p.8. REPORT internal; domain **statistical_results**, primary/all relationships **S_W**. Locations: [results p.8 eTable 3 seven rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8); [p.9 eTable 4 Age≥65 and second AA rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); [p.10 eTable 5 PEG row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10). Context: [results p.4 imputation description](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [p.5 model methods](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), [main p.4 two-sidedα=.05](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); the main source only corroborates the test level and does not create S_C.

**Route A, category 1**: retain eTable3 Pattern2−.28(−.47,−.08),P=.150; Pattern1−.20(−.36,−.03),P=.226; Pattern2/PT−.30(−.58,−.02),P=.280; Pattern2/HC−.47(−.74,−.19),P=.090; Site3 .19(.08,.29),P=.069; Site4 .15(.05,.24),P=.124; second AA .16(.07,.25),P=.077; eTable4 Age RR1.15(1,1.33),P=.046 and second AA RR1.16(1,1.33),P=.046; eTable5 PEG OR.96(.92,1.00),P=.037. Unrounded null-adjacent endpoints may explain the latter three, but the scope expressly exempts all these interval-versus-P comparisons from display-precision removal. Different test/interval constructions remain alternatives, with no inferred Wald standard errors, reference distributions or replacement numbers.

### Included finding evidence and checker provenance

Source checker: checkers/statistical_pass_1.md; finding F-ST1-201.

#### F-ST1-201

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

Source checker: checkers/statistical_pass_1.md; finding F-ST1-202.

#### F-ST1-202

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


## C015 — Within-header three-month subset counts

**Candidate statement:** Within-header three-month subset counts.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable8 any-follow-up total vs REPORT results supplement eTable8 three-month arm counts

**Evidence state:** reproduced

**Inclusion audit:** PENDING

**Finding IDs:** F-NUM-003

**Qualifying route:** Route A, category 3

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

### Independent screen and complete affected locations

Finding: **F-NUM-003**. Earliest conflicting display: DOC-005 p.14 first eTable 8 population header. REPORT internal; domain **statistical_results**, primary/all relationships **S_W**. [Results p.14 first header](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14): randomized454;366 with any follow-up;PT149,HC153,UC152 at3months. Corroboration: [p.7 eTable 1 full follow-up counts](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); [p.13 subgroup definition](../../../joi250046supp4_prod_1755300121.15587.pdf#page=13); samep.14 next header. **Route A, category 3**: the within-header nesting discrepancy exceeds display tolerance; randomized target-population counts are a possible interpretation, but do not identify why this block uses the same “at3months” description as observed contributors in the other blocks. Retain subtraction-based UC109/PT94/HC108 only as corroborating arithmetic, not as a required replacement.

### Included finding evidence and checker provenance

Source checker: checkers/numeric_consistency.md; finding F-NUM-003.

#### F-NUM-003

The first eTable 8 subgroup header labels randomized-size arm counts as three-month counts that exceed its any-follow-up total.

- **Exact source locations and roles:** REPORT [results supplement PDF p.14, eTable 8 first population header](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14). Corroborating REPORT [same supplement p.7 eTable 1](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), p.14 next subgroup header and [p.13 population description](../../../joi250046supp4_prod_1755300121.15587.pdf#page=13).
- **Printed inputs:** Randomized prior to 8/9/2021,N=454;366 with at least 1 follow-up;PT=149,HC=153,UC=152 at 3-months. After enhancement at 3-months:UC512/PT448/HC527. Full 3-month observed counts areUC621/PT542/HC635.
- **Rule and calculation:** Observed-at-three-month contributors must be a subset of participants with at least one follow-up.149+153+152=454>366. Sum half-unit interval=[452.5,455.5], any-follow-up interval=[365.5,366.5]; minimum excess 86; relative excess 86/366=0.234973>0.05. Conditional corroborating subtraction from full versus post-enhancement counts gives prior 3-month UC109/PT94/HC108, total 311. This subtraction is not needed for the reproduced within-header nesting discrepancy.
- **Focus area:** A.
- **Proposed review domain:** statistical_results.
- **Proposed relationship type:** S_W.
- **Qualifying route:** Route A, category 3.
- **Affected result or extracted value:** Three-month arm-specific analysis/contributor counts for the primary pain-severity sensitivity analysis before engagement enhancement.
- **Why context does not resolve it:** Route A category 3 applies to the printed count relationship. The matching randomized total makes randomized arm sizes a plausible alternative, but does not change the explicit at 3-months label; neighboring subset headers use observed 3-month counts.
- **Alternatives and missing definition:**149/153/152 may be randomized target-population counts rather than observed contributors, potentially including those represented through weighting. The header does not define this departure from the other blocks. If so, the human question concerns the labeled denominator rather than the randomization total.
- **Exact human question:** Do PT149,HC153 andUC152 denote randomized arm sizes or observed three-month contributors, and which three-month counts apply to this first sensitivity-analysis subgroup?


## C016 — Raw-score summary statistic and bounds in eTable 11

**Candidate statement:** Raw-score summary statistic and bounds in eTable 11.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement mean-summary narrative vs REPORT results supplement median/quartile table labels and values

**Evidence state:** reproduced

**Inclusion audit:** PENDING

**Finding IDs:** F-XS-008

**Qualifying route:** Route B

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None. Mechanical recheck confirms S_W; the initial S_C proposal was aligned because the main scale definition is corroborating only.

### Independent screen and complete affected locations

Included finding: **F-XS-008**; duplicate **F-ST1-601**. Earliest substantive label conflict: DOC-005 p.15; DOC-001 p.11 provides the exact PGIC score definition needed for the numerical check. REPORT results supplement internal comparison; domain **statistical_results**, primary/all relationships **S_W**. The main PGIC scale definition corroborates the numerical premise and does not create S_C. This classification alignment follows the independent mechanical recheck; the inclusion decision is unchanged.

Locations: [main p.11, Table 3 PGIC footnotes h/i](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11); [results p.15, Additional Unadjusted Data and Analyses](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15); [p.17, eTable 11 title/header and all21 rows](../../../joi250046supp4_prod_1755300121.15587.pdf#page=17); [p.18 note b](../../../joi250046supp4_prod_1755300121.15587.pdf#page=18). **Route B**: preserve the mean-versus-median/quartile source descriptions and all raw-column locations, including the mixed-width HC3-month PGIC entries. The precision-qualified numerical subset is PGIC-pain PT6=2.8,PT12=2.8,UC12=2.2; PGIC-general PT3=2.7,UC6=1.8; each printed half-unit interval is separated from its nearest ordinary empirical single-item median by .15, relative gaps .053571,.053571,.068182,.055556,.083333. Other fractional centers, such as2.9 or2.6, have relative gaps≤.05 and are not separate numerical discrepancies. A set-valued or interpolated median definition remains an alternative; the independent inclusion rests on the unresolved extractable summary identity, not on asserting that every mathematical definition of a median excludes these values. No equality between raw medians and model mean differences or arm-column permutation is assumed.

### Included finding evidence and checker provenance

Source checker: checkers/cross_source_consistency.md; finding F-XS-008.

#### F-XS-008

**Observation:** The raw-score summary label in eTable 11 conflicts with the narrative's mean description and with the possible medians of the reported PGIC scale.

**Exact locations and document roles:** REPORT [results supplement p.15, Additional Unadjusted Data and Analyses introduction](../../../joi250046supp4_prod_1755300121.15587.pdf#page=15); REPORT [p.17, eTable 11 title and raw-score header, every outcome block at 3/6/12 months](../../../joi250046supp4_prod_1755300121.15587.pdf#page=17); REPORT [main p.11, Table 3 PGIC scale footnotes h–i](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11).

**Printed values and labels:** The introduction says eTable 11 provides unadjusted mean secondary outcomes. The title says median/interquartile ranges, and the group header says “Raw Score Median (25%-tile,75%tile).” All 21 rows are affected by this summary label: severity, intensity, interference, social-role functioning, physical functioning, PGIC pain and PGIC general, each at3/6/12 months. PGIC is one item with integer response categories1–7. Printed PT PGIC-pain summaries are2.9 (2.8,2.9),2.8 (2.7,2.9),2.8 (2.7,2.9); PT general summaries are2.7 (2.6,2.7),2.5 (2.4,2.6),2.6 (2.4,2.7). HC3-month PGIC entries instead have2.0 (1.0,3.0) and2.0 (1.0,2.0).

**Comparison logic and reproduction:** A conventional sample median of a one-item integer score is integer or half-integer. The half-unit rounding intervals for2.9,2.8,2.7 and2.6 are respectively [2.85,2.95], [2.75,2.85], [2.65,2.75] and [2.55,2.65], each containing no possible such median. This is a quantity/summary-type comparison; a relative numeric-copy discrepancy is not applicable. No arithmetic comparison of medians with mean differences is asserted.

**Focus area:** C. **Proposed review domain:** statistical_results. **Relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** Whether the unadjusted secondary group summaries are means with confidence intervals, medians with quartiles, or mixed summary types, for extraction of all21 eTable11 rows.

**Why context does not resolve it:** The conflicting mean/median descriptions and the different PGIC interval shapes do not establish a single intended quantity. The label changes both the central statistic and meaning of the parentheses.

**Supported alternatives:** Most entries may be means with95% intervals while the HC3-month PGIC entries are medians/quartiles; all entries may have been intended as a different model-based summary; or a mixture of summaries may be intentional. No numerical relabeling or replacement is proposed.

**Human question:** What central statistic and interval type is reported for each group in eTable11, particularly the HC3-month PGIC cells, and which entries should be extracted as means versus medians?

Related screened duplicate findings (not included Finding IDs): F-ST1-601. Their full affected locations are retained in the consolidated screen group and checker outputs.


## C017 — Workbook All Observed depression percentage

**Candidate statement:** Workbook All Observed depression percentage.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT workbook eTable3 count/percentage vs REPORT workbook denominator/missing count/footnote

**Evidence state:** reproduced

**Inclusion audit:** PENDING

**Finding IDs:** F-NUM-002

**Qualifying route:** Route A, category 3

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

### Independent screen and complete affected locations

Finding: **F-NUM-002**. Earliest workbook location: DOC-006 eTable 3 E3, then E82/E83/A110. REPORT internal; domain **statistical_results**, primary/all relationships **S_W**. [Supplied workbook eTable 3, E3,A82,E82,A83,E83,A110](../../../joi250046supp5_prod_1755300121.16087.xlsx). **Route A, category 3**: retain all exact cells, decoded source shared-string values and nonmissing-denominator calculation in the justification. The count711 and N1568−missing2 imply a percentage near45.4 rather than printed73.2; no restricted assessment denominator is stated. Checker links containing inserted spaces in the source filename were locator slips; the supplied workbook and exact XML cells above were used for this decision.

### Included finding evidence and checker provenance

Source checker: checkers/numeric_consistency.md; finding F-NUM-002.

#### F-NUM-002

The workbook's All Observed depression count and percentage do not reconcile with its stated missing-value denominator rule.

- **Exact source locations and roles:** REPORT [supplied workbook](../../../joi250046supp5_prod_1755300121.16087.xlsx), worksheet eTable 3, E3 subgroup N, A82/E82 current-depression row, A83/E83 missing count, and A110 denominator footnote. Direct sheet 1.xml E82 references shared-string 290, confirmed as 711 (73.2); E3 references 144, confirmed as(N=1568); E83 is numeric 2.
- **Printed inputs:** All Observed N=1568; current depression PHQ-8≥10,711 (73.2); missing 2. FootnoteA110 excludes missing from percentage denominators.
- **Rule and calculation:** Denominator 1568−2=1566. Percentage 100×711/1566=45.402299%. N and missing each receive half-unit intervals, yielding denominator[1565,1567]; numerator[710.5,711.5]. Recomputed percentage interval=[45.341417%,45.463259%]. Printed 73.2% interval=[73.15%,73.25%]. Gap=27.686741 points; relative=27.686741/73.2=0.378234>0.05. Count partition 162+243+711=1116 matches the overall row, independently corroborating count alignment.
- **Focus area:** A.
- **Proposed review domain:** statistical_results.
- **Proposed relationship type:** S_W.
- **Qualifying route:** Route A, category 3.
- **Affected result or extracted value:** Depression prevalence among participants with all primary follow-up outcomes observed.
- **Why context does not resolve it:** Route A category 3 applies even though the printed count and footnote allow a reader to compute another percentage.73.2 remains an extractable printed reading.
- **Alternatives and missing definition:**73.2% would require a denominator near 971 rather than the stated 1566. A restricted assessment denominator is not stated. Another percentage or count may have been supplied to the cell; production mechanism is unknown.
- **Exact human question:** What numerator and nonmissing denominator support the 73.2% printed in eTable 3 cell E82?
