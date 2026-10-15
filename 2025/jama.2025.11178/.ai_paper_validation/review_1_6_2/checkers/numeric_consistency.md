# Fresh Numeric Consistency Review

Scope: all 14 main article pages and all 27 supporting REPORT units: intervention-description PDF pages 1–7, results-supplement PDF pages 1–19, and workbook worksheet eTable 3 A1:J115, all 525 populated cells. Numeric relationship inventory: 84 stable families N001–N084, including every applicable displayed count, denominator, percentage, total, flow quantity and effect-measure identity. Counts within families were checked exhaustively; this is not row sampling. Current fresh maps supplied the locators. No previous conclusions or web evidence were used.

Findings: 5, including two count/percentage discrepancies, one subgroup count-label discrepancy, one consolidated SMD identity pattern and one consolidated NNT point-reproduction pattern. Excluded apparent-observation patterns: 7. No candidate IDs, adjudications or suggested corrections are assigned.

Numeric rules: separately propagate every input's half-unit interval, then compare with the printed output's half-unit interval; remaining relative gap must exceed 0.05. Exact source confirmation used current CPU PyMuPDF 1.26.4 renders of main pages 4,10,11 and supplement 4 page 14, plus direct workbook ZIP XML/shared strings. All compared documents below are REPORT by content. Links are relative to this checker artifact. The four rendered derivatives reside in preprocessing/numeric_review; their engine is pdf_tools.py render, PyMuPDF 1.26.4, 200 dpi, CPU. No source or reused asset was modified.

### F-NUM-001

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

### F-NUM-002

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

### F-NUM-003

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

### F-NUM-004

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

### F-NUM-005

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

## Excluded observations

Only apparent issues not emitted are listed. Reconciled arithmetic checks remain in the N inventory.

| Location | Observation | Reason code |
|---|---|---|
| Results supplement p.7 eTable 1; p.8 eTable 3; workbook D3 | Pattern counts 188+283+1568=2039 versus 2036 any follow-up; PT644 vs 643,HC692 vs 690; weighted pattern visits 5458 versus observed 5449; corresponding 650 versus 659 missing. Even nonoverlapping input/output precision leaves relative gaps below 0.05. Example 5458 sum interval[5455,5461] versus observed[5447.5,5450.5], gap 4.5/5449=.000826. Workbook D3=468 also differs from 188+283=471 by a relative gap below 0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| Main baseline/narrative versus workbook baseline copies | Female 1712 versus 1713; current-depression 47.8%versus 47.9%; numerous differences in copied descriptives remain below 0.05 after precision and/or refer to subgroup-qualified summaries. These are distinct from the within-cell E82 finding. | ROUNDING_OR_DISPLAY_PRECISION |
| Main Table 2/eTables 7–8 other reciprocal NNT point rows | Small integer NNT deviations remaining after half-units have relative gaps at most 0.05. Example main intensity 3 mo PT−UC rates 24.3−17.7 gives[14.925373,15.384615], printed 16 interval[15.5,16.5], gap.115385/16=.007212. Four SMD additive rows also meet the precision rule and are retained in the inventory. | ROUNDING_OR_DISPLAY_PRECISION |
| Results supplement pp.16–18 eTables 10/11 | Subtracting printed group medians/IQR to reproduce model-based mean differences assumes medians are model means; no such equality is stated. Statistical questions about source headings are reviewed separately. | CONDITIONAL_OR_UNREPORTED |
| Intervention supplement p.6 fidelity denominators |1791+2350=4141 versus total 4626. Training reviewed count 193 is supplied, but total training-session denominator is not supplied; an unreported 485-session component could explain the partition. Reviewed counts 193+89+17 do sum 299. | CONDITIONAL_OR_UNREPORTED |
| Main methods/Table 2/Table 3 and results supplement pp.5/7–10 |2331 randomized target population versus 2036 any-follow-up contributors, weight sum 2036 persons/6108 visits, and observed-at-time counts are explicitly different quantities under the reported nonresponse weighting/imputation. | CONTEXT_RESOLVES |
| Main p.8/p.12 Discussion residence description |Roughly 40% rural/underserved versus 44% elsewhere is an explicitly approximate narrative description, not a replacement numeric extraction for the baseline 44% result. | CONTEXT_RESOLVES |

## Limitations and closure

All 84 numeric relationship families are complete. Exact histogram bin numerators are not printed; no fabricated bar counts were used. UC change SD and individual raw data are unavailable; effect identity used the supplied common-denominator definition, not external methodology. PLAN statistical design comparisons and detailed interval/test compatibility are assigned to separate fresh specialist lanes. Findings use supplied source evidence only; no unreviewed source unit or incomplete assigned numeric family remains.

