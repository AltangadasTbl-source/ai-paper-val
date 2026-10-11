# Numeric consistency review — main part 1

Fresh independent numeric review of MAIN-001..MAIN-067, N001..N067: DOC-001 physical PDF pages1–4, 67 assigned relationship groups. All content is REPORT by role. Matching main pp6–8 were inspected only to corroborate assigned results. Complete rules read: QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md. Tooling CPU; direct Poppler26.01.0 layout extraction; retained p3/p4 images visually inspected. No web or earlier findings/report conclusions were used.

Durable arithmetic evidence: ../relationships/numeric_relationship_inventory.md. Direct derivatives checkers/numeric_main_direct_pp1-4.txt and checkers/numeric_main_corrob_pp6-8.txt record the same source; direct source remains authority. Counts:67 groups;65 Table1 count cells, of which62 print percentages and3 print zero counts without percentages; all flow boxes/table totals checked. Findings2. Excluded apparent observations5. No assigned coverage gap.

## Findings

### F-NUM-001

**Title:** Abstract pooled death percentage does not reconcile with the reported cohort and death counts.

**Relationships:** N012, corroborated by N003/N027. Proposed primary relationship S_W; all relationships S_W.
**Exact source locations and roles:**
- REPORT [DOC-001 p1 abstract Results](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1): “There were 4 deaths (2.2%), 2 in each group.”
- REPORT [DOC-001 p4 Table1 headers](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=4): cohort N262; M96, B166.
- REPORT [DOC-001 p7 deaths narrative](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=7): four deaths over12years, two in each group.
- REPORT [DOC-001 p8 Table3 headers and Death row](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=8): M n96, Death2(2.1); B n166, Death2(1.2).

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
- REPORT [DOC-001 p1 abstract Results](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1): HbA1c “decreased by0.2% (95%CI,−0.5% to0.2%)” in M, and “by1.6% (95%CI,−1.8% to−1.3%)” in B.
- REPORT [DOC-001 p3 Results year7 paragraph](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3): M8.2→8.0, “difference,0.2% [95%CI,−0.5% to0.2%]”; B8.7→7.2, “difference,1.6% [95%CI,−1.8% to−1.3%].”
- REPORT [DOC-001 p6 Table2 HbA1c row and footnote b](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6): signed net changes M−0.2(−0.5 to0.2), B−1.6(−1.8 to−1.3); footnote specifies net change for HbA1c.

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

# Numeric consistency review: results and support shard

Scope: MAIN-068 through MAIN-144 (DOC-001 physical pages 5–11) and SUPPORT-B-001 through SUPPORT-B-039 (DOC-002 pages 41–65, DOC-003 pages 1–22, DOC-004 page 1). All 116 assigned grouped relationships were reviewed, with all underlying rows, numeric cells, contributor sequences and definitions retained in the linked mapper artifacts. Stable identifiers are N068–N183. No sampling or finding count limit was applied. Two findings and four excluded apparent observations are recorded below. No scientific coverage gap remains in this shard.

Source role is by content: DOC-001 and DOC-003 are REPORT; DOC-002 including its appendices is PLAN; DOC-004 is REPORT and supplies no result-bearing quantitative relationship. Source-linked reusable native/layout text and mapper image reconstructions were read; candidate printed values were independently confirmed using direct Poppler 26.01.0 `pdftotext -layout` on the exact supplied source. New derivatives: `preprocessing/numeric_extra_doc003_pp14-22.txt` (DOC-003 pages 14–22) and `preprocessing/numeric_extra_doc002_pp55-56.txt` (DOC-002 pages 55–56). Compute device CPU; no new OCR/rendering; no fallback; all supplied/reused assets unchanged.

## Complete checks

Figure 2: every contributor count in all four panels and all 13 visits checked. RYGB+SG+AGB sums reproduce pooled surgery counts separately for HbA1c and weight at every visit; outcome-specific counts are retained separately. Unlabelled model curves and raw-data boxplot elements are not exact numeric inputs. Changes in availability across annual visits do not imply loss-only monotonicity because missed visits can be followed by later observed visits.

Table 2: all 17 rows, baseline and year-7 means/SD or medians/IQR, adjusted changes, limits, contrasts, percentages, ORs and P values checked with footnotes. Continuous changes are model estimates, not arithmetic of the marginal raw means. For every continuous contrast, the two printed within-group changes and the between-group difference reconcile under input half-unit intervals. Binary comparisons are odds ratios under GEE, not crude risk ratios; urine albumin:creatinine changes are folds and their between-group comparison is a difference of folds. Each estimate is inside its ordered interval. Group-comparison interval null membership agrees with significance. Narrative weight-loss magnitudes reverse the sign of negative weight changes coherently. Medication subsets sum to overall medication percentages at baseline and year 7.

Narrative: 162/166=97.590%, 62/163=38.037%,72/119=60.504%; dialysis2/96=2.083%; retinopathy5/96=5.208%,2/166=1.205%; crossover24/96=25%, components8+15+1=24; revisions7+4+1+3=15 and15/166=9.036%. Printed precision reconciles. BMI subgroup HbA1c differences and weight differences reconcile under half-unit intervals, including -1.5-(-0.4)=-1.1 versus printed -1.2 and19.3-10.1=9.2. Weight loss percentage comparisons and procedure direction agree. Remission contributor counts in Figure 3 are outcome-specific and must not replace available HbA1c counts or assume model percentages are raw fractions.

Table 3: all 26 rows, both columns, zero entries, full denominators96/166, matching narrative fractions and event footnotes checked. Every percentage reconciles with100*n/N after displayed precision; no event categories are assumed mutually exclusive. Examples20/166=12.048% printed12%;22/166=13.253% printed13.3%;5/96=5.208% printed5.2%. No event rate is misidentified as person-time incidence density.

Plan Appendix2: all five columns and flow categories checked, including randomized totals355, intervention325, deaths3, lost20, eligibility302. Each column eligibility equals intervention−deaths−lost:154−2−12=140;61−0−5=56;38−0−3=35;40−1−0=39;32−0−0=32. Historical demographic percentages, summaries and one-year outcomes retained with denominator availability limitations; no comparison to current primary analysis is forced. The randomization dropout footnote has the separate reproduced discrepancy below. SF-36 and AUDIT-C score/frequency categories checked; three0–4 AUDIT-C items yield0–12, with sex-specific thresholds stated. Ancillary cost utility numeric thresholds and BMI ranges checked without auditing clinical/economic methodology.

Supplement methods and figures: ITT and PP time-dependent exposure definitions, weight units, annual medication category sums, contributor Ns in all four eFigure5 panels, all six eFigure mappings, subgroup caption numbers and effect-measure meanings reviewed. Graph coordinates lacking printed labels are locators only. Overall repeated-visit P values are distinct from single-visit Table2/eTable2 tests. Availability counts do not exceed corresponding randomized treatment group sizes.

eTable1: every categorical count/percentage, sex/race/BMI group total, medication cell, continuous mean/SD and median/IQR reviewed. Sex179+83=262 and93+37=130; 12-year race39+89+2=130. The 7-year Other race count/percentage is recorded below. ACEi and ARB counts need not be disjoint because overlapping medication use is possible; their combined count is not inferred by simple addition.

eTable2: all17 rows and all model intervals/contrasts/P values plus pages15–16 footnotes reviewed. Continuous printed group contrasts reconcile with displayed within-group change half-unit intervals, including rounded weight−8.4 versus−19.3−(−10.8)=−8.5, SBP0.3 versus−4.5−(−4.7)=0.2, and total cholesterol−1.2 versus−5.5−(−4.2)=−1.3. Every estimate is within its interval; all printed group null/significance pairs agree. Year12 medication categories34.4+59.4=93.8 and53.5+29.1=82.6. Remission MED0 and undefined/near-infinite OR are disclosed by footnotee, not reconstructed as a finite conventional OR.

eTable3: every count, observed denominator, percentage and subgroup total across eight abnormalities checked. For anemia25+8+2=35 and78+36+33=147; each other three-procedure total uses81+37+33=151; event sums48,20,35,1,66,23 reconcile. Every printed n/N percentage agrees under half-unit intervals. No denominator is replaced by full randomized166 when assay availability differs.

eTable4: all seven LSmean/SE/difference/SE/P rows reviewed. Surgery-minus-medical differences reconcile with rounding: hemoglobin13−13.7 vs−0.8 is compatible with printed13 half-unit interval; albumin4.1−4.1 can accommodate−0.01. Difference SE0.0 is displayed at one decimal, permits nonzero small values; it is not treated as exact zero.

eTables5–6: all48 adverse-event rows,25 procedure rows and both96/166 denominators checked; every count/percentage reconciles. Operation-specific event percentages in eTable5footnotes reconstruct group counts: abdominal pain14/41,20/89,3/36 sums37; GERD15/41,10/89,4/36 sums29; dysphagia5/41,4/89,3/36 sums12; dumping7/89,1/41 sums8. No mutually exclusive row totals are invented. Printed event tests are retained for statistical specialists rather than inferred from percentage differences alone.

eTable7: all explicit n/N percentages and timing/range checked, with group/procedure denominators96,36,41 kept distinct. Crossover component counts sum24; conversion/revision counts sum15 matching main text and eTable6. DOC-004 and all assigned administrative/reference units are explicitly no-applicable numeric scope.

## Findings

### F-NUM-101

**Relationship:** N171 (SUPPORT-B-027).

**Exact source locations and roles:** REPORT [DOC-003 physical page14,eTable1,7-year column header N262 and Race/Other row](../../../joi240004supp2_prod_1721756962.82552.pdf#page=14). Within one REPORT display; proposed relationship S_W; all relationships S_W.

**Printed inputs:** N=262; Other race n=4 with1.9%; neighboring Black81(30.9%) and White176(67.2%). Footnotea explicitly defines categorical variables as n(%). The 12-year Other row2(1.5%) withN130 is a separate consistent row.

**Rule and calculation:** count/denominator/percentage in one display should reconcile under displayed precision. Direct fraction100*4/262=1.526718%. Permit numerator[3.5,4.5], denominator[261.5,262.5], giving recomputed percentage interval[1.333333%,1.720841%]. Printed1.9% has interval[1.85%,1.95%]. Gap=1.85−1.720841=0.129159 percentage points; relative discrepancy0.129159/1.9=0.067978>0.05. Integer count exactness would only widen the discrepancy. The race counts sum261 rather than262, which corroborates the need to identify the intended Other count but is not a separate finding.

**Focus area:** A. **Proposed review domain:** statistical_results. **Qualifying route:** Route A, category3.

**Affected result or extracted value:** Other race count and percentage in the7-year ARMMS-T2D analysis population; a data extractor may take4 or1.9%.

**Why context does not resolve it:** Route A count/percentage discrepancy within one display. Footnotes provide no alternate race denominator or modeled percentage. The surrounding rows do not establish whether count4 or percentage1.9 should be used.

**Alternatives and missing definition:** Count5 would give1.9084% and make race totals262, but this is a source-grounded arithmetic alternative, not a proposed correction. A different Other-race denominator is possible but is not identified in the display. There is no printed basis for treating this descriptive percentage as a model estimate.

**Exact human question:** Which Other-race count, denominator and percentage apply to the7-year population in eTable1, and how should the printed4(1.9%) be interpreted?

### F-NUM-102

**Relationships:** N145 and N146 (SUPPORT-B-001–002).

**Exact source locations and roles:** PLAN [DOC-002 physical page55,Appendix2,Randomized and Number underwent intervention rows](../../../joi240004supp1_prod_1721756962.80052.pdf#page=55) versus PLAN [same Appendix2 continuation page56,footnote dagger](../../../joi240004supp1_prod_1721756962.80052.pdf#page=56). One bound PLAN display; proposed relationship P_P; all relationships P_P.

**Printed inputs:** Randomized155,69,43,45,43(total355); underwent intervention154,61,38,40,32(total325). Footnote dagger states38 participants dropped at randomization and were not followed and do not qualify for ARMMS-T2D enrollment. Footnote is attached directly to Number underwent intervention row. Other losses explicitly listed are deaths and later lost-to-follow-up, applied after intervention to yield eligible total302.

**Rule and calculation:** If randomized participants who did not initiate intervention are those in the attached dropout footnote,355−325=30, not38. Permit all10 printed input counts their half-unit intervals: randomized sum[352.5,357.5]; intervention sum[322.5,327.5]; difference[25,35]. Printed38 has interval[37.5,38.5]; gap2.5 and relative discrepancy2.5/38=0.065789>0.05. All five intervention/death/loss/eligible columns otherwise reconcile. This is an arithmetic mismatch within the Appendix2 display rather than a comparison of historical administrative calendars across documents.

**Focus area:** A/D (participant eligibility and analysis-population accounting). **Proposed review domain:** plan_material. **Qualifying route:** Route A, category3.

**Affected result or extracted value:** Total post-randomization exclusion count and eligible enrollment pool specified in the supplied plan Appendix2; this is the plan account of the cohort from which the report population is selected.

**Why context does not resolve it:** Route A counts within one display. The row-attached footnote does not identify another randomized cohort, extra exclusions or different snapshot that reconciles38 with the displayed355 and325. Historical appendix status supplies a plausible provenance explanation but no arithmetic resolution.

**Alternatives and missing definition:** The footnote may refer to another historical cohort snapshot or participants outside the five displayed randomized counts. Treatment initiation and footnote dropout may be different categories. Those definitions are not stated here. Current report flow is not asserted to use this historical325 or302 directly, and report-versus-plan flow differences are not part of this finding. Independent screening must assess whether the plan cohort account is a relied-on statistical population element; no historical calendar or baseline-copy comparison is claimed.

**Exact human question:** What population and time point does the Appendix2 total38 randomized dropouts describe, and how does it reconcile with the displayed355 randomized and325 intervention initiators?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-001 p6 Table2 fasting-glucose change row | MED point change lacks the percent sign printed on its interval and other cells; footnoteb explicitly specifies relative percent change and fixes the unit without changing a number. | NOTATION_OR_TYPOGRAPHY |
| DOC-003 pp15–16 eTable2 footnotesa–c | Several footnotes say year7 while the title, all value columns and footnotee say year12; this footnote template wording does not change the printed values or leave their visit unidentified. | CONTEXT_RESOLVES |
| DOC-003 p18 eTable4 Calcium difference SE | Printed SE0.0 at one decimal can represent a small positive value below0.05; groupSE0.04/0.03 and P.03 therefore do not establish an exact-zero-SE contradiction. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p6 Table2 and DOC-003 pp15–16 eTable2 raw summaries versus adjusted changes/ORs | Arithmetic of marginal baseline/visit means and crude percentages differs from some model estimates; footnotes and supplementary mixed-model/GEE specifications identify the estimates as model-based. | MODEL_VERSUS_CRUDE |

No other apparent observation met an excluded-observation definition. Checks that reconcile are documented in the complete relationship inventory and are not listed as exclusions.
# Numeric consistency — protocol first-half shard

Scope: DOC-002 physical pp.1–40, PLAN throughout; all90 PLAN-A mapping keys N184–N273 in relationships/parts/numeric_plan_extra.md. Reviewed counts, denominators, percentages, within-display row/column totals, planning attrition, intervention-hours totals, effect-scale labels, and available design-number arithmetic. The supplied source is [protocol](../../../joi240004supp1_prod_1721756962.80052.pdf#page=1). Source-matched layout and the current support evidence map are locators; no old candidate or report conclusion was read. No other source scope is claimed.

## Findings

No reproduced observation in this numeric scope qualifies as a finding after the specified self-screen. Finding namespace F-NUM-201 onward remains unused. This conclusion does not adjudicate the separate statistical-method or planned-versus-reported reviews.

## Completed checks

All90 inventory rows are COMPLETE, with explicit no-applicable-numeric-check records for context/design-only keys. Cohort325−20−3=302;20/325=6.1538% and3/325=.9231% reconcile6%/.9%; retained302×.8=241.6 reconciles≈242; FigureA1N302/272/242/211 reconcile302×(1−missing0/10/20/30%). Half-unit recomputed bounds and zero interval gaps are in the inventory. TableA2 exercise176+196=372,12+222=234,0+183=183,0+174=174. TableA3 all surgical rows/columns sum192; TableA4RYGB site counts sum104 and repeat TableA3. Table1 has15 cluster rows; Chem20 has20 listed analytes; three contacts and three diabetes states reconcile their enumerations. Power94.6% and98.6% are possible473/500 and493/500 simulation fractions. Year7HR1.36 at30% remission,R².1 repeats TableA6 exactly. No unadjusted count-derived measure conflicts with OR/logOR/HR labels; no mutually exclusive interpretation was imposed on nested or overlapping endpoint groups.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| [PLAN p9](../../../joi240004supp1_prod_1721756962.80052.pdf#page=9), [PLAN p16](../../../joi240004supp1_prod_1721756962.80052.pdf#page=16) | BMI<35 prevalence35% versus one third: even treating one third as33.333%, printed35% lower bound34.5 gives gap1.1667/35=.03333≤.05; approximate prevalence does not reproduce beyond display threshold. | ROUNDING_OR_DISPLAY_PRECISION |
| [PLAN pp32–33](../../../joi240004supp1_prod_1721756962.80052.pdf#page=32), TableA4p33 | RYGB narrative150cm Roux limb exceptBWH75cm/approx50cm BP limb versusCROSSROADS table100–150cm/30–50cm describes historical operative ranges; it changes no primary/key-secondary result, analysis population, randomized-intervention dose/duration, or statistical decision rule. | PERIPHERAL_COMPARISON |
| [PLAN p35](../../../joi240004supp1_prod_1721756962.80052.pdf#page=35), TableA5 | Plain layout readsrho=0.11 by adjoiningrho=.1 and superscriptfootnote1. Footnote1 and surrounding autocorrelation range make the readingrho=.1 immediately clear; no numerical source substitution reproduced. | NOT_REPRODUCED |
| [PLAN p28](../../../joi240004supp1_prod_1721756962.80052.pdf#page=28), control-power paragraph | A specific extrapolation from75/63/48% and52/38/22% to39/11% would require assuming a fitted slope/intercept or which historical points define the assumed linear log-odds curves. They are not printed, and the year7 values are simulation assumptions rather than count-derived results; no unique arithmetic conflict reproduced here. The explicit trend claim remains assigned to statistical review. | CONDITIONAL_OR_UNREPORTED |
| [PLAN p35](../../../joi240004supp1_prod_1721756962.80052.pdf#page=35), detectable weight difference | Central delta.43–.47×residualSD6% gives2.58–2.82%, including statedapproximately2.8%; mandated rounded-input interval2.3375–3.0875% overlaps printed2.8±.05%. An apparent challenge that2.8 must equal.43×6 has zero interval gap. | ROUNDING_OR_DISPLAY_PRECISION |

Only apparent observations are listed here; all other completed checks reconcile or have no applicable numeric arithmetic. No routeA observation is screened out after reproduction. Source-grounded model/power design statements are retained in full for both statistical passes rather than replaced by diagnostic assumptions.

## Limits and closure

90 relationships;0 findings;5 excluded observations;0 unreviewed mapping keys and0 scientific coverage gaps. FigureA1 point ordinates are unlabeled. Exact Monte Carlo andPASS11 reproduction lacks complete settings/data; no invented values or alternative preferred analysis used. Sources/reuse unchanged; no web, Office/CSV source, or new derivative used. Relationship and checker artifacts are the two assigned paths only.
