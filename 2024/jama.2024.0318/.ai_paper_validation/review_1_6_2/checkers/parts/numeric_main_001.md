# Numeric consistency review — main part 1

Fresh independent numeric review of MAIN-001..MAIN-067, N001..N067: DOC-001 physical PDF pages1–4, 67 assigned relationship groups. All content is REPORT by role. Matching main pp6–8 were inspected only to corroborate assigned results. Complete rules read: QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md. Tooling CPU; direct Poppler26.01.0 layout extraction; retained p3/p4 images visually inspected. No web or earlier findings/report conclusions were used.

Durable arithmetic evidence: ../relationships/numeric_relationship_inventory.md. Direct derivatives checkers/numeric_main_direct_pp1-4.txt and checkers/numeric_main_corrob_pp6-8.txt record the same source; direct source remains authority. Counts:67 groups;65 Table1 count cells, of which62 print percentages and3 print zero counts without percentages; all flow boxes/table totals checked. Findings2. Excluded apparent observations5. No assigned coverage gap.

## Findings

### F-NUM-001

**Title:** Abstract pooled death percentage does not reconcile with the reported cohort and death counts.

**Relationships:** N012, corroborated by N003/N027. Proposed primary relationship S_W; all relationships S_W.
**Exact source locations and roles:**
- REPORT [DOC-001 p1 abstract Results](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1): “There were 4 deaths (2.2%), 2 in each group.”
- REPORT [DOC-001 p4 Table1 headers](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=4): cohort N262; M96, B166.
- REPORT [DOC-001 p7 deaths narrative](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=7): four deaths over12years, two in each group.
- REPORT [DOC-001 p8 Table3 headers and Death row](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=8): M n96, Death2(2.1); B n166, Death2(1.2).

**Printed inputs:** pooled count4, printed percentage2.2%, cohort262=96+166, death counts2+2=4. Table3 uses participant cohort denominators.

**Rule and calculation:** count/denominator percentage must reconcile. 100×4/(96+166)=1.526717557%. Under required half-unit intervals, count4 becomes[3.5,4.5], cohort262 becomes[261.5,262.5]; recomputation interval [1.333333333%,1.720841300%]. Printed2.2% interval[2.15%,2.25%]. Gap2.15−1.720841300=0.429158700 percentage points; relative discrepancy0.429158700/2.2=0.195072136 (>0.05). Even independently rounding the two component counts and two denominators gives [100×3/263,100×5/261]=[1.140684,1.915709]%, still separated from[2.15,2.25] by0.234291/2.2=0.106496 (>0.05).

**Focus area:** A, counts and denominators.
**Proposed review domain:** statistical_results.
**Qualifying route:** Route A, category 3 (count, denominator and percentage in abstract paragraph); also Route B for the matched abstract/body cohort and death result.

**Affected result or extracted value:** pooled12-year mortality percentage in the abstract, paired with four deaths and262 participants.

**Why context does not resolve it:** The immediate abstract reports262 participants but supplies no alternative death-percentage denominator. Table3 and the narrative corroborate the same four deaths and full-group denominators. The count and percentage cannot both represent that pooled cohort; category3 does not permit resolving this by reconstructing an intended percentage.

**Alternatives:** A separate risk set, available-follow-up population, or other mortality denominator may have been used for2.2%, but none is named at the compared locations. The group percentages2.1% and1.2% individually reconcile with2/96 and2/166 and are not candidates from this comparison.

**Exact human question:** Which denominator and mortality quantity does the abstract’s2.2% represent for its four deaths, and how should it be reconciled with the262-participant cohort and Table3 group counts?

### F-NUM-002

**Title:** Positive year7 HbA1c change values are paired with negative signed intervals and table changes.

**Relationships:** N006,N007,N031; repeated pattern consolidated. Proposed primary relationship S_W; all relationships S_W.
**Exact source locations and roles:**
- REPORT [DOC-001 p1 abstract Results](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1): HbA1c “decreased by0.2% (95%CI,−0.5% to0.2%)” in M, and “by1.6% (95%CI,−1.8% to−1.3%)” in B.
- REPORT [DOC-001 p3 Results year7 paragraph](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3): M8.2→8.0, “difference,0.2% [95%CI,−0.5% to0.2%]”; B8.7→7.2, “difference,1.6% [95%CI,−1.8% to−1.3%].”
- REPORT [DOC-001 p6 Table2 HbA1c row and footnote b](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6): signed net changes M−0.2(−0.5 to0.2), B−1.6(−1.8 to−1.3); footnote specifies net change for HbA1c.

**Printed inputs:** B positive1.6 with entirely negative interval[−1.8,−1.3] in both abstract and narrative; Table2 corresponding−1.6. M positive0.2 labeled difference in narrative versus−0.2 table.

**Rule and calculation:** A point estimate cannot lie outside its reported confidence interval when it refers to the same signed quantity. Positive1.6 is greater than upper limit−1.3 by2.9 percentage points; the interval does not contain it. Category1 is never dismissed by rounding. For additional cross-location sign comparison, positive1.6 interval[1.55,1.65] and negative−1.6 interval[−1.65,−1.55] have gap3.10, relative gap3.10/1.6=1.9375. M narrative positive0.2 interval[0.15,0.25] versus table−0.2 interval[−0.25,−0.15] has gap0.30, relative gap0.30/0.2=1.50. M positive0.2 by itself is inside its interval, so it is not a separate point-containment finding; it is another occurrence of the narrative/table sign pattern. Raw B7.2−8.7=−1.5 has rounding interval[−1.6,−1.4] overlapping signed table−1.6; magnitude1.5 versus1.6 is not the issue.

**Focus area:** B, estimate and interval/direction logic.
**Proposed review domain:** statistical_results.
**Qualifying route:** Route A, category 1 for the B estimate outside its interval; Route A, category 2 for narrative signed-difference versus table signed-net-change readings.

**Affected result or extracted value:** signed within-group year7 HbA1c changes extracted from the abstract/narrative with their95%confidence intervals.

**Why context does not resolve it:** The positive B printed estimate lies outside its negative interval, an always-register category1. “Decreased by” can signal a positive decrease magnitude, but the same line supplies a negative-change interval and the narrative calls it a difference. That interpretation must be recorded as an alternative, rather than using it to screen out the interval-versus-estimate conflict.

**Alternatives:** The authors may intend positive decrease magnitudes for the prose point values while reporting confidence intervals on the signed follow-up-minus-baseline change scale. Table2 supplies a coherent signed estimate/interval representation. If that mixed representation was intended, the human reviewer can determine how to interpret paired prose estimates and intervals. No fitted-model reconstruction is needed for this printed sign comparison.

**Exact human question:** Do the positive year7 HbA1c values in the abstract and narrative represent decrease magnitudes or signed changes, and on which scale are their accompanying intervals to be read?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p3 Figure1 N026 | Arm branches193+122=315 versus parent305. Half-unit sum[314,316], parent[304.5,305.5]; relative gap8.5/305=.027869≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p1/p3 cohort summary and p4 Table1 N004/N029/N044 | White177/262=67.5573% versus67.2%. Relative discrepancy below.05 even before allowing half-unit counts; rounded input intervals overlap printed interval. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p4 Table1 β-blockers N066 | B30/166=18.0723% versus18.2%; half-unit ratio interval[17.7177,18.4290] overlaps[18.15,18.25]. Explicit subgroup35 denominator also supports30/165=18.1818%. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p3 HbA1c and p6 Table2 N031 | Raw B7.2−8.7=−1.5 versus modeled table−1.6; half-unit difference interval[−1.6,−1.4] overlaps[−1.65,−1.55]. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p4 Table1 triglycerides and urine albumin:creatinine N059/N061 | Mean(SD) label accompanies two-ended parenthetic ranges; field reader recognizes range-format summaries; no source-grounded numeric contradiction or result-changing quantity is established. | TERMINOLOGY_OR_WORDING |

## Limitations and completed scope

All67 assigned groups and all printed Table1 count/percentage cells received explicit checks in the inventory. Model-based percentage denominators and adjusted effects cannot be regenerated where events or fitted objects are absent; no missing definition alone was emitted. Statistical endpoint/model logic and further matched locations retain their independent assigned reviewers. No source or reusable artifact was modified.

