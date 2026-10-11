# Numeric consistency review — count and denominator scope

Runtime task: /root/numeric_checker. Fresh numeric consistency specialist; gpt-6.1-sol, medium reasoning. Assigned scope: main mapping M001–M089 and support REPORT mappings R001–R013, R025. Estimate checker separately owns M090–M124 and R014–R024. Full scope and review contract read; all 117 assigned compound numeric relationships reviewed without a finding target. Every displayed count, denominator, percentage, category total and repeated flow count is retained in [numeric relationship inventory](../relationships/numeric_relationship_inventory.md). All source locations in this artifact are REPORT by content.

Count arithmetic used exact printed integers, followed by conservative half-unit input intervals and each printed target's half-unit interval. An interval gap divided by the printed percentage must exceed 0.05 to qualify. Approximate graphical bar heights and model-based percentages are not treated as crude counts. No old candidate, report or checker conclusions, external sources or raw participant data were used.

## Findings

### F-NUM-001

**Title:** painTRAINER therapeutic-dose count and percentage do not reconcile.

**Relationships:** N024, N030. **Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Compared document roles:** REPORT main article Results paragraph versus REPORT main article allocation/flow. **Qualifying route:** Route A, category 3.

**Exact source locations:** [Main article physical PDF p4, Results, session completion paragraph](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); corroborating [physical PDF p5, Figure 1, painTRAINER randomized and session categories](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=5). The p4 paragraph states: “371 (43%) completed at least 6 sessions”; its immediate referent is those randomized to painTRAINER. Figure 1 prints painTRAINER randomized n776 and 371 completing 6–8 sessions, 156 completing 1–5 sessions, 249 completing 0 sessions. Their sum is 776.

**Printed inputs:** numerator371; randomized denominator776; displayed43%. The same paragraph prints527(68%) completing at least1 session. The health-coach counterparts are660(85%) and548(70%) with randomized n778.

**Rule and calculation:** percentage=100×count/randomized denominator. 100×371/776=47.809278%. With numerator [370.5,371.5] and denominator [775.5,776.5], the recomputed interval is [47.714102%,47.904578%]. Printed43% permits [42.5%,43.5%]. The interval gap is4.214102 percentage points; relative discrepancy=4.214102/43=0.0980024, exceeding0.05. The other three session-completion percentages reproduce under their stated randomized denominators. Figure 1's categories independently reproduce371 and776.

**Affected result or extracted value:** the fraction of randomized painTRAINER participants receiving the stated therapeutic dose of at least6 sessions; a data extractor could take43% or a value near47.8% from the accompanying count and randomized population.

**Why context does not resolve it:** this is a reproduced count/denominator/percentage discrepancy within one paragraph, an always-register category. The ability to calculate a percentage from the count does not remove the conflicting printed percentage.

**Alternatives and missing definition:**43% could refer to a different denominator or session-completion definition, but none is supplied in this paragraph. A denominator near863 would be needed for371/denominator to be43%; that exceeds the randomized painTRAINER population. The eight-session categories on p5 support the printed371 count without defining an alternative denominator.

**Exact human question:** Which numerator, denominator and percentage should be used for painTRAINER participants completing at least6 sessions, and what population or definition produced the printed43%?

**Direct-source confirmation:** fresh Poppler pdftotext26.01.0 layout extraction from supplied p4, CPU, confirms371(43%). Locator artifact: preprocessing/numeric_checker/main-p004.txt. No OCR normalization applied.

### F-NUM-002

**Title:** depression count and percentage in the all-observed workbook column do not reconcile.

**Relationships:** N112. **Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **Compared document roles:** REPORT results workbook current-depression cell, column header and missing-count footnote within the same worksheet. **Qualifying route:** Route A, category 3.

**Exact source locations:** [Results workbook](../../../joi250046supp5_prod_1755300121.16087.xlsx), worksheet **eTable 3**, E82, with row labelA82 “Current depression (PHQ-8 ≥10),c No. (%)”; E3 “(N=1568)”; E83 missing2; A110 states missing counts are excluded from the denominator of reported percentages. All-observed column labelE2; corresponding overall/other-pattern cellsB82:D82 and missingB83:D83 provide same-display comparators.

**Printed inputs:** E82=711(73.2); E3 N1568; E83 missing2. Thus the documented percentage denominator is1566. Overall B82=1116(47.9), missing B83=2 and N2331. Other-pattern C82=162(54.9), N295, missing0; D82=243(51.9), N468, missing0. Counts162+243+711=1116.

**Rule and calculation:** A110 requires100×711/(1568−2)=45.402299%. Allowing half-unit input intervals: count [710.5,711.5], N [1567.5,1568.5], missing [1.5,2.5], denominator [1565,1567]. Recomputed percentage interval [45.341417%,45.463259%]. Printed73.2% permits [73.15%,73.25%]. Interval gap=73.15−45.463259=27.686741 percentage points; relative discrepancy=27.686741/73.2=0.3782342, exceeding0.05. The three same-row comparator percentages reproduce from their stated denominators. Even using1568 without excluding missingness gives45.3444%, leaving the discrepancy.

**Affected result or extracted value:** baseline prevalence of current depression among participants with all primary-outcome follow-ups observed; a reader could extract73.2% or about45.4% from the accompanying count and denominator.

**Why context does not resolve it:** the count/denominator/percentage relationship within one worksheet qualifies under the always-register category, including descriptive baseline displays. Neighboring rows and the row count total support711 but do not identify which printed field should be used for extraction.

**Alternatives and missing definition:**73.2% could use an unprinted denominator near971, or711 could describe another population. Neither alternative is documented; the supplied E3/E83/A110 definition specifies1566. No provenance explanation or replacement value is inferred.

**Exact human question:** What count and denominator underlie the printed73.2% for current depression in the all-observed column, and which values should a reader use for this baseline result?

**Direct-source confirmation:** direct unzip of supplied workbook xl/worksheets/sheet1.xml and xl/sharedStrings.xml confirms E82 string711(73.2), E3 N1568, E83 numeric2 and A110 footnote; zero formulas. CPU ZIP/XML inspection is the authority, with the retained exact-cell extraction used only as a locator. Direct extracts are preserved in preprocessing/numeric_checker/sheet1.xml and sharedStrings.xml.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| Main p1/Table1 p6; workbook eTable 3 B11 and A113 | Main female count1712 versus workbook1713, with a self-reported/EHR fallback definition. Half-unit count intervals [1711.5,1712.5] and [1712.5,1713.5] meet; gap0. | ROUNDING_OR_DISPLAY_PRECISION |
| Main p7 secondary-outcomes narrative; Table3 p10 severity3-month SMD cells | Narrative−0.26/−0.36 versus table−0.25/−0.34. Half-unit gaps0 and.01 respectively; relative to narrative reference.36, .02778, below.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-005 p7 eTable1 observed-pattern rows; workbook eTable 3 D3 | Pattern188+283+1568=2039 versus any2036; interval gap1 relative1/2036=.000491. UC703/PT644/HC692 versus703/643/690 gives zero half-unit gaps. Weighted pattern5458 versus sum timepoint5449 gives interval gap4.5, relative.000826. Missing1-or2 workbook468 versus188+283=471 leaves gap1.5, relative1.5/468=.003205. All below.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-004 p6 fidelity review |1791+2350 completed sessions excludes training-period completed total, which is unprinted;193 is training sessions reviewed. Substituting193 as all training sessions would compare nonmatching totals. | CONDITIONAL_OR_UNREPORTED |
| DOC-004 p5; DOC-005 p13 modification narrative | Approximately140 versus454 enrolled at intervention change date is a peripheral administrative/enrollment comparison. Quantitative subset analysis populations and any planned decision-rule implications are separately assigned to cross-source and estimate checkers. | PERIPHERAL_COMPARISON |
| Workbook eTable 3 A103, A106 with B103:E103/B106:E106 | Threshold rows use mean(SD) wording while values visibly have counts and percentages; intended count/percentage reading is immediate and arithmetic reconciles. | TERMINOLOGY_OR_WORDING |

## Scope closure and limitations

117 complete compound relationships:89 main records,13 support families and15 workbook blocks, the latter preserving all525 nonempty cells. Two findings and six excluded-observation patterns. All count percentages within Table1 reconcile; flow recruitment, exclusions, allocation, sessions, terminal statuses, hospitalization/death group totals and all eTable1 displayed percentages were checked. The workbook category partitions, characteristic-missing denominators, category row sums and all count percentages were checked; only E82 exceeds the display-precision threshold. Mean(SD) cells are never tested as count percentages. Apparent graph shapes are not exact printed values.

No assigned scientific coverage gap. Raw-data reconstruction of continuous means/SDs and exact unnumbered histogram heights is unavailable from supplied displays; those absent inputs were not invented. Inferential conflicts, plan comparisons and adjusted-estimate transformations remain fully assigned to the other specialist lanes. Auxiliary arithmetic files contain calculations only; classification and inclusion reasoning above are agent-authored.
# Numeric consistency checker — estimate displays shard

Exact scope: main M090–M124 (Table2,Table3,all footnotes and closing narrative) and REPORT support R014–R024 (eTables3–11,eFigure2 and associated definitions). All locations are REPORT by results content. Stable relationship inventory: relationships/parts/numeric_estimates_inventory.md, N121–N166. Four independently reproduced findings; six excluded-observation patterns. There is no finding-count target.

Scientific controls read completely: QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md. Tooling: tooling_record.md; direct Poppler26.01.0, CPU. Source visual derivatives generated by pdftoppm -f N -l N -r140 -singlefile -png from the exact supplied PDFs: preprocessing/numeric_estimates/main-9.png,main-10.png,main-11.png,supp-8.png,supp-17.png. Complete direct-source/native locator transcripts from the new maps supplied all other assigned rows. No old candidate/report material used.

## Findings

### F-NUM-101

**Issue:** Main Table3 standardized mean difference intervals have reversed numeric endpoints, points outside their intervals, and null inclusion inconsistent with the corresponding unstandardized intervals.

**Compared locations and roles:** REPORT [DOC-001 Table3 physicalp10](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), REPORT [continuation and footnote d physicalp11](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11). Source columns are PTvsUC;HCvsUC;HCvsPT. The direct source visually confirms the following values.

**Printed inputs and rule:** A95% interval is presented lower to upper and must contain its point. Footnote d defines SMD as the adjusted difference divided by the positive UC change SD at that outcome/time. A positive rescaling preserves zero inclusion. All18 social/physical SMD intervals are printed in descending order:

| Outcome,time | PTvsUC SMD(CI) | HCvsUC SMD(CI) | HCvsPT SMD(CI) |
|---|---|---|---|
| Social3m | .12(.23 to .11) | .01(.12 to−.00) | .20(.29 to .19) |
| Social6m | .18(.23 to .05) | .06(.11 to−.06) | .26(.30 to .15) |
| Social12m | .19(.21 to .01) | .07(.09 to−.10) | .27(.28 to .12) |
| Physical3m | .09(.16 to .07) |−.02(.05 to−.04) | .16(.22 to .15) |
| Physical6m | .15(.09 to−.06) | .02(−.03 to−.18) | .22(.16 to .05) |
| Physical12m | .20(.18 to−.03) | .07(.04 to−.16) | .27(.25 to .09) |

Even after sorting endpoints for a diagnostic containment check, all six physical6/12m point estimates are outside the resulting intervals. Additional points outside ordered intervals are:

| Outcome,time,contrast | Printed point | Printed95%CI |
|---|---:|---|
| Severity12m PTvsUC |−.25 |−.24 to .01 |
| Severity12m HCvsUC |−.36 |−.35 to−.12 |
| Intensity12m HCvsUC |−.27 |−.26 to−.12 |
| Interference12m PTvsUC |−.26 |−.25 to .01 |
| Interference12m HCvsUC |−.37 |−.36 to−.11 |
| GlobalPain12m PTvsUC |−.55 |−.50 to .05 |
| GlobalPain12m HCvsUC |−.57 |−.54 to−.08 |
| GlobalPain12m HCvsPT |−.29 |−.25 to .14 |

Thus14 points fail containment, including the six physical6/12m points above. At least the following pairs additionally disagree on zero inclusion under the stated rescaling:

| Outcome,time,contrast | Adjusted mean-differenceCI | SMD CI, preserving printed endpoints |
|---|---|---|
| Severity12m PTvsUC |−.6 to−.2 |−.24 to .01 |
| Intensity12m PTvsUC |−.4 to−.1 |−.16 to .00 |
| Interference12m PTvsUC |−.7 to−.3 |−.25 to .01 |
| Social3m HCvsUC | .8 to2.2 | .12 to−.00 |
| Social6m HCvsUC | .8 to2.2 | .11 to−.06 |
| Social12m HCvsUC | .6 to2.1 | .09 to−.10 |
| Physical3m HCvsUC | .2 to1.2 | .05 to−.04 |
| Physical6m PTvsUC | .1 to1.2 | .09 to−.06 |
| Physical6m HCvsUC |−.1 to .9 |−.03 to−.18 |
| Physical6m HCvsPT |−.8 to .3 | .16 to .05 |
| Physical12m PTvsUC | .3 to1.5 | .18 to−.03 |
| Physical12m HCvsUC | .2 to1.4 | .04 to−.16 |
| Physical12m HCvsPT |−.7 to .5 | .25 to .09 |
| GlobalPain12m PTvsUC |−.8 to−.5 |−.50 to .05 |

**Calculation and precision:** Category1 point/interval and transformed-null conflicts do not use the rounding exclusion. Endpoint reversals are numeric values, not glyphs. For example social3m PTvsUC first endpoint .23 has interval[.225,.235], second .11 has[.105,.115]; minimum reversal gap .110, relative to .11=1.000, above .05. Every listed descending pair has a positive gap greater than5% after ±.005 endpoint rounding. For physical6m PTvsUC the point interval[.145,.155] lies above sorted upper-endpoint interval[.085,.095] by .050; the printed point .15 also visibly lies outside .09 to−.06. The source's definition supplies the positive-scale invariant without needing the unprinted SD.

**Focus area:** B,C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W.
**Qualifying route:** Route A, category1 for containment and interval/test-null coherence; Route A, category2 for reversed numeric endpoint pattern.
**Affected result or extracted value:** SMD point estimates and95%CIs for continuous pain/function/global outcomes in Table3; the extracted direction and interval-significance reading may change.
**Why context does not resolve it:** These are printed numerical interval/estimate conflicts in always-register categories. Sorting the social/physical endpoint pairs still leaves physical6/12m points outside and does not supply the intervals to extract. Footnote d states the normalization but does not explain the distinct intervals.
**Alternatives and missing definition:** The endpoints or SMD column associations may have been transposed; the SMDs may use a separate calculation not identified by footnote d. Different interval procedures are an alternative for null comparisons and do not remove the printed point-containment conflicts. This card does not prescribe an interval.
**Exact human question:** Which SMD point estimates, column associations and95% confidence limits apply to each affected outcome/time/contrast, and how were those limits obtained under Table3 footnote d?

### F-NUM-102

**Issue:** Table3 SMD points do not reconcile with the printed common-UC-SD normalization across contrasts.

**Compared locations and roles:** REPORT [DOC-001 p10 Table3](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), REPORT [p11 Table3 continuation and footnote d](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11). All comparisons are within Table3. All20 affected outcome/time rows are named below; severity6m alone does not qualify after display precision.

**Printed inputs and rule:** Footnote d states: adjusted between-group mean difference divided by SD in change in outcome at the given time point among the UC group. Therefore, for a common positive SD, SMD_HC/PT=SMD_HC/UC−SMD_PT/UC. This is a source-defined identity, not an assumed crude estimator. Each SMD input permits ±.005, so the recomputed interval is central difference±.010; the compared printed HC/PT value permits±.005.

| Outcome,time | Printed SMD PT/UC;HC/UC;HC/PT | Recomputed HC/PT interval | Printed HC/PT interval | Relative gap |
|---|---|---|---|---:|
| Severity3m |−.25;−.34;−.13 |[−.100,−.080]|[−.135,−.125]|.19231|
| Intensity6m |−.17;−.27;−.04 |[−.110,−.090]|[−.045,−.035]|1.12500|
| Intensity12m |−.16;−.27;−.03 |[−.120,−.100]|[−.035,−.025]|2.16667|
| Interference3m |−.25;−.34;−.13 |[−.100,−.080]|[−.135,−.125]|.19231|
| Interference6m |−.27;−.37;−.14 |[−.110,−.090]|[−.145,−.135]|.17857|
| Social3m | .12;.01;.20 |[−.120,−.100]|[.195,.205]|1.47500|
| Social6m | .18;.06;.26 |[−.130,−.110]|[.255,.265]|1.40385|
| Social12m | .19;.07;.27 |[−.130,−.110]|[.265,.275]|1.38889|
| Physical3m | .09;−.02;.16 |[−.120,−.100]|[.155,.165]|1.59375|
| Physical6m | .15;.02;.22 |[−.140,−.120]|[.215,.225]|1.52273|
| Physical12m | .20;.07;.27 |[−.140,−.120]|[.265,.275]|1.42593|
| GlobalPain3m |−.62;−.62;−.37 |[−.010,.010]|[−.375,−.365]|.95946|
| GlobalPain6m |−.54;−.55;−.29 |[−.020,.000]|[−.295,−.285]|.91379|
| GlobalPain12m |−.55;−.57;−.29 |[−.030,−.010]|[−.295,−.285]|.87931|
| GlobalGeneral3m |−.66;−.66;−.40 |[−.010,.010]|[−.405,−.395]|.96250|
| GlobalGeneral6m |−.46;−.50;−.24 |[−.050,−.030]|[−.245,−.235]|.77083|
| GlobalGeneral12m |−.53;−.58;−.28 |[−.060,−.040]|[−.285,−.275]|.76786|

Three further rows have overlapping SMD-additivity intervals, but their SMDs fail direct shared-SD normalization. For each, compute the allowable SD from PTvsUC difference/SMD, then propagate the printed HCvsPT difference through that positive SD range:

| Outcome,time | PTvsUC adjusted difference;SMD | Implied UC SD interval | HCvsPT adjusted difference;SMD | Recomputed HC/PT SMD interval | Printed SMD interval | Relative gap |
|---|---|---|---|---|---|---:|
| Severity12m |−.4;−.25 |[1.37255,1.83673]| .0;−.11 |[−.03643,.03643]|[−.115,−.105]|.62340|
| Intensity3m |−.3;−.21 |[1.16279,1.70732]|−.0;−.08 |[−.04300,.04300]|[−.085,−.075]|.40000|
| Interference12m |−.5;−.26 |[1.69811,2.15686]| .0;−.12 |[−.02944,.02944]|[−.125,−.115]|.71296|

Differences printed to one decimal permit±.05; SMDs to two decimals permit±.005. These propagated intervals use all half-unit combinations, not central values alone. Each listed interval gap divided by absolute printed HC/PT SMD exceeds .05. The sign discordance in physical3m HCvsUC (.7 difference,−.02 SMD), physical6/12m HCvsPT (−.3/−.1 difference,.22/.27 SMD), and globalPain12m HCvsPT (.1 difference,−.29 SMD) further illustrates the same normalization pattern.

**Focus area:** B,C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W.
**Qualifying route:** Route B.
**Affected result or extracted value:** Table3 SMD point estimates for all listed20 outcome/time rows and three comparisons; these are values a data extractor can take as standardized effects.
**Why context does not resolve it:** The stated UC denominator is common to the three contrasts. The algebra and full display-precision intervals leave no interpretation of the listed SMDs consistent with that definition. A reader cannot identify intended points or group labels from the table alone.
**Alternatives and missing definition:** Different standardization populations or SMD contrast associations could explain different numbers, but footnote d does not specify them. The source does not print UC SD values. No preferred method or replacement value is proposed.
**Exact human question:** Which denominator and contrast association produced each listed SMD, and how do those points relate to the adjusted contrasts and the UC SD definition in footnote d?

### F-NUM-103

**Issue:** Main Table2 HCvsPT NNT intervals do not reconcile with the displayed point and transformed-null interpretation.

**Compared locations and roles:** REPORT [DOC-001 p9 Table2 HCvsPT RR and NNT columns, footnotes d/e](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9).

| Outcome,time | Printed HCvsPT RR95%CI | Printed HCvsPT NNT95%CI |
|---|---|---|
| Severity6m |1.13(.98–1.30)|24(12–186)|
| Severity12m |1.07(.96–1.19)|41(17–76)|
| Intensity3m |1.11(.93–1.33)|37(14–57)|
| Intensity12m |1.05(.92–1.20)|63(18–38)|
| Interference6m |1.10(.96–1.27)|26(11–67)|
| Interference12m |1.07(.97–1.18)|39(16–79)|

**Rule and calculation:** The intensity12m point63 lies above its upper95% bound38. Even ±.5 integer display intervals leave point[62.5,63.5] and upperlimit[37.5,38.5] separated by24; gap/63=.38095. It is a category1 containment conflict independent of the interval estimator.

For the six rows, RR95%CIs include no-effect1 while every NNT CI is finite and strictly positive. Footnote d defines NNT=1/(adjusted response-probability difference), and footnote e states how an absolute-risk-differenceCI spanning0 produces disconnected NNT-to-infinity and NNH-to-negative-infinity bounds. A no-effect risk comparison has RD0 and reciprocal infinity rather than a finite exclusively beneficial NNT interval. These printed interval readings disagree about whether no-effect is included. No numerical sampling covariance is assumed; the comparison is the reported contrast's no-effect reading. Category1 interval/test-null conflict does not use a rounding exemption. The RR lowerlimits .92–.98 are below1 even after±.005, and all printed NNT bounds remain finitepositive after±.5.

**Focus area:** B,C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W.
**Qualifying route:** Route A, category1.
**Affected result or extracted value:** HCvsPT NNT confidence bounds for severity6/12m,intensity3/12m,interference6/12m; especially the intensity12m point63 and its95%CI18–38.
**Why context does not resolve it:** A point outside its interval is always-register. The footnote explains disconnected bounds but the affected rows do not print negative endpoints or infinities, so it does not identify which bounds to extract.
**Alternatives and missing definition:** RR andRD CIs might use different interval procedures. A negative NNH endpoint or a different numeric endpoint may have been intended. Different procedures are an alternative interpretation, not a resolution of the source's numerical containment conflict. The exact RD interval construction is not supplied in this display.
**Exact human question:** What HCvsPT absolute-risk-difference intervals and reciprocal NNT/NNH confidence sets underlie these rows, and which printed confidence limits belong to the intensity12m NNT63?

### F-NUM-104

**Issue:** Report model tables display95%CI null inclusion that differs from their printed P-value significance reading.

**Compared locations and roles:** REPORT [DOC-005 p8 eTable3](../../../joi250046supp4_prod_1755300121.15587.pdf#page=8), REPORT [p9 eTable4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9), REPORT [p10 eTable5](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10). Each comparison is within one model-table row; roles assigned by results content.

| Exact row | Estimate | Printed95%CI | P |
|---|---:|---|---:|
| eTable3 Pattern:2observed follow-ups |−.28 |−.47 to−.08 |.150|
| eTable3 Pattern:1observed follow-up |−.20 |−.36 to−.03 |.226|
| eTable3 Pattern2\|painTRAINER |−.30 |−.58 to−.02 |.280|
| eTable3 Pattern2\|HealthCoach |−.47 |−.74 to−.19 |.090|
| eTable3 Site3 | .19 | .08 to .29 |.069|
| eTable3 Site4 | .15 | .05 to .24 |.124|
| eTable3 second Education:AA degree row | .16 | .07 to .25 |.077|
| eTable4 Age≥65vs<65 |1.15 |1.00 to1.33 |.046|
| eTable4 second Education:AA degree row |1.16 |1.00 to1.33 |.046|
| eTable5 PEGscore | .96 | .92 to1.00 |.037|

**Rule and calculation:** Use stated95%CIs and conventional .05 significance threshold. The first seven coefficient intervals exclude0 whileP>.05. Their nearest-to-null limits are respectively−.08,−.03,−.02,−.19,.08,.05,.07. The last three ratio intervals include1 at the displayed boundary whileP<.05. No Wald-normal reconstruction or unknown degrees of freedom is required for this printed interval/significance conflict. Category1 explicitly does not apply the rounding exclusion; possible underlying unrounded boundary limits for the last three rows are recorded as an alternative.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W.
**Qualifying route:** Route A, category1.
**Affected result or extracted value:** Model coefficient/ratio confidence intervals and P values for the named imputation,estimation and nonresponse-model rows.
**Why context does not resolve it:** These are interval-versus-P conflicts in an always-register category. Both are printed in the same model rows and the tables give no separate inferential attribution that determines which reading applies.
**Alternatives and missing definition:** Different analyses or inferential procedures could underlie CIs andP values; eTables4/5 boundary1.00 could reflect an underlying value on one side of1. The exact unrounded bounds and any different test attribution are not printed. These alternatives do not remove category1 registration.
**Exact human question:** For each named row, which95%CI andP value apply to the same model contrast, and were any CIs andtests obtained from distinct inferential procedures?

## Excluded observations

Only apparent observations not emitted are listed. Checks that reconcile are retained in the complete N inventory.

| Location | Observation | Reason code |
|---|---|---|
| DOC-001 p10 Table3severity6m SMD triplet |−.36−(−.26) gives recomputed HC/PT[−.110,−.090]; printed−.12 interval[−.125,−.115];gap.005/.12=.04167≤.05. Direct common-SD check also has only a small remaining gap (relative .0119). | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p9 Table2 and DOC-005 pp11,14 NNT point columns, especially reminder-letter6m PTvsUC8 | Reciprocal NNT points often are rounded upward: Table2severity3PT17.24→18,intensity3PT15.15→16,intensity6PT17.24→18. For eTable8 reminder6m proportions35.6−21.3 give reciprocal[6.94444,7.04225]; source-supported integer ceiling can yield7or8. Printed8 therefore reconciles; merely comparing to unrounded6.993 would omit the supported integer convention. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-005 pp16–17 eTables10–11 group medians and GEE mean-difference columns | Differences of displayed medians need not reproduce model mean differences; apparent column associations or direction conflicts obtained by treating medians as means depend on an unsupported equality. Captions explicitly identify medians/IQRs, while separate columns/footnotes define model mean differences. No raw means or a median-difference method is supplied. | CONDITIONAL_OR_UNREPORTED |
| DOC-005 pp8–9 duplicated EducationAA labels | Labels alone do not change the printed estimates or identify a conflicting numerical rule; named coefficient rows remain distinct values. | TERMINOLOGY_OR_WORDING |
| DOC-005 p15 eTable9 caption adjusted versus repeated unadjusted definitions | Narrative says no adjustment/weighting/imputation; column and footnote specify unadjustedGEE, and all27RRs reproduce unadjusted proportions within precision. Intended analysis is resolved by immediate context. | TERMINOLOGY_OR_WORDING |
| DOC-001 p11 Table3 global-change rows under overall mean-change-from-baseline heading | Footnotes explicitly define global scores as perceived change since study start on1–7scale. Their positive points are coherent change-perception scores and their group contrasts have the stated directions; heading wording does not independently conflict with a numeric value. | TERMINOLOGY_OR_WORDING |

## Coverage closure and limitations

46compound numeric relationships complete:35main-map records M090–M124 and11support-map records R014–R024. Every adjusted or unadjusted numeric cell, interval containment/order/direction, within-display numerator/percentage, source-defined transformation and model label in this assigned scope was checked. No source-unit gap. No numerical UC SDs, participant-level data or GEE covariance matrices are supplied for independent full interval reconstruction; those unavailable quantities are named rather than invented. eFigure2 has no exact bin-count labels. Independent statistical reviewers cover all inferential relationships and may emit duplicate provenance for screening consolidation.

