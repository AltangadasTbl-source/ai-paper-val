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

**Exact source locations and roles:** REPORT [DOC-003 physical page14,eTable1,7-year column header N262 and Race/Other row](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=14). Within one REPORT display; proposed relationship S_W; all relationships S_W.

**Printed inputs:** N=262; Other race n=4 with1.9%; neighboring Black81(30.9%) and White176(67.2%). Footnotea explicitly defines categorical variables as n(%). The 12-year Other row2(1.5%) withN130 is a separate consistent row.

**Rule and calculation:** count/denominator/percentage in one display should reconcile under displayed precision. Direct fraction100*4/262=1.526718%. Permit numerator[3.5,4.5], denominator[261.5,262.5], giving recomputed percentage interval[1.333333%,1.720841%]. Printed1.9% has interval[1.85%,1.95%]. Gap=1.85−1.720841=0.129159 percentage points; relative discrepancy0.129159/1.9=0.067978>0.05. Integer count exactness would only widen the discrepancy. The race counts sum261 rather than262, which corroborates the need to identify the intended Other count but is not a separate finding.

**Focus area:** A. **Proposed review domain:** statistical_results. **Qualifying route:** Route A, category3.

**Affected result or extracted value:** Other race count and percentage in the7-year ARMMS-T2D analysis population; a data extractor may take4 or1.9%.

**Why context does not resolve it:** Route A count/percentage discrepancy within one display. Footnotes provide no alternate race denominator or modeled percentage. The surrounding rows do not establish whether count4 or percentage1.9 should be used.

**Alternatives and missing definition:** Count5 would give1.9084% and make race totals262, but this is a source-grounded arithmetic alternative, not a proposed correction. A different Other-race denominator is possible but is not identified in the display. There is no printed basis for treating this descriptive percentage as a model estimate.

**Exact human question:** Which Other-race count, denominator and percentage apply to the7-year population in eTable1, and how should the printed4(1.9%) be interpreted?

### F-NUM-102

**Relationships:** N145 and N146 (SUPPORT-B-001–002).

**Exact source locations and roles:** PLAN [DOC-002 physical page55,Appendix2,Randomized and Number underwent intervention rows](../../../../joi240004supp1_prod_1721756962.80052.pdf#page=55) versus PLAN [same Appendix2 continuation page56,footnote dagger](../../../../joi240004supp1_prod_1721756962.80052.pdf#page=56). One bound PLAN display; proposed relationship P_P; all relationships P_P.

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
