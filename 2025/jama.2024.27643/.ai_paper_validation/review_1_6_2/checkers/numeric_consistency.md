# Numeric consistency review

Runtime agent: /root/numeric_checker. Fresh numeric_consistency_reviewer, gpt-6.1-sol/medium. Complete numeric scope: all404 pages of six supplied PDFs, using seven disjoint complete mapper artifacts. Stable inventory N001–N060 in ../relationships/numeric_relationship_inventory.md records every bundle and no-applicable group. Counts:60 relationship bundles;4 findings;14 excluded observations. No scientific coverage gaps. Direct source confirmation, extraction engines and limitations are documented below. All findings remain proposed observations for independent inclusion screening; no C IDs or dispositions assigned.

Source roles: DOC-001 main article and DOC-004 results supplement are REPORT; DOC-002 protocol and DOC-003 SAP are PLAN; DOC-005 roster and DOC-006 sharing statement are REPORT. Only source content supplies those assignments.

## Findings

### F-NUM-001 — Primary modeled mortality rates differ between the main article and its cited primary efficacy table

**Relationships:** N021. **Focus area:** A/B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_C; all relationships S_C. **Qualifying route:** Route B.

**Compared locations and roles:** REPORT [main PDFp4, Primary Efficacy Outcome](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4); REPORT [results supplement PDFp15, eTable2, Mortality Event Rate](../../../joi240158supp3_prod_1742927563.7911.pdf#page=15). Main paragraph explicitly attributes both rates to the Bayesian shared parameter model and cites eTable2. Table has that same primary function/mortality analysis title, combined active doses and shared placebo. Both printed units are events per month.

**Printed inputs:** Main: shared placebo0.007, pooled active0.006. eTable2: shared placebo median0.010 and mean0.010(SD0.0026),95%CrI0.0054–0.0154; pooled active median0.009 and mean0.009(SD0.0025),95%CrI0.0052–0.0150. Primary DRR0.97,CrI0.783–1.175 agrees across these locations, establishing the common comparison.

**Rule and calculation:** Matched copies of the same estimated monthly mortality component should agree beyond display precision unless a separate fit/summary is identified. Shared main half-unit interval[0.0065,0.0075],table[0.0095,0.0105];gap0.002;relative discrepancy0.002/0.007=0.285714. Active main[0.0055,0.0065],table[0.0085,0.0095];gap0.002;relative discrepancy0.002/0.006=0.333333. Both exceed0.05. Recomputed interval here is the comparator's own printed-value interval; no crude count/person-time rate replaces the model.

**Affected result or extracted value:** The two monthly mortality component estimates of the primary shared-parameter disease-progression analysis.

**Why context does not resolve it:** Both places name the same primary model, population and monthly unit; both table mean and median differ from the narrative, so a mean/median distinction does not reconcile the readings. The source gives no alternative fit identifier for this pair.

**Alternatives and missing definition:** Separate fitted versions or mortality-only versus joint-model summaries could give different rates, but the main paragraph explicitly names the joint shared-parameter model. An unstated parameter definition or summary convention could be relevant. These are possibilities, not established production explanations.

**Exact human question:** Which pair of monthly mortality event-rate estimates belongs to the reported primary Bayesian shared-parameter analysis, and do the narrative and eTable2 summarize different fitted quantities?

### F-NUM-002 — Key secondary SVC values carry monthly and 24-week change readings

**Relationships:** N023. **Focus area:** B/C. **Proposed review domain:** report_internal_inconsistency. **Proposed relationship type:** S_C; all relationships S_C,S_W. **Qualifying route:** Route B.

**Compared locations and roles:** REPORT [main PDFp4, Secondary Efficacy Outcomes](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4); REPORT [results supplement PDFp16, eTable3A,24-week Change Estimate](../../../joi240158supp3_prod_1742927563.7911.pdf#page=16). Within main paragraph, “mean change in SVC over24weeks” is followed by repeated “PPN per month” and “PPN/month” units. The supplement directly prints the same values as24-week changes.

**Printed inputs:** Combined active−9.32, dose30−7.84,dose60−10.79,shared placebo−8.53; pooled difference−0.78,95%CI−4.25to2.68. Main attaches monthly units; eTable3A attaches24-week change units to all corresponding estimates. The immediately following baseline-NfL sensitivity displays−1.73/−1.55PPN per month, without a corresponding table of those sensitivity values.

**Rule and calculation:** A24-week total change and monthly slope have different dimensions. Main−9.32/−8.53 match the table's total-change numbers exactly, with zero scalar-copy gaps; the discrepancy is quantity identity. Using supplied SAP month conversion days×12/365.25,24weeks=168days corresponds5.51951months. If the table total−9.32±0.005 were expressed as an average monthly change, its interval would be approximately[−1.689462,−1.687651]PPN/month, disjoint from literal main[−9.325,−9.315];gap about7.625538/9.32=0.818191. This conversion is a unit diagnostic, not a proposed analysis or fitted slope calculation. The24-week time label is treated as a defined horizon, not an uncertain raw count.

**Affected result or extracted value:** The units and magnitude of the key secondary24-week SVC change and treatment difference, including both individual-dose estimates.

**Why context does not resolve it:** The main sentence simultaneously labels a24-week change and a monthly quantity; the exact values are also printed as total changes elsewhere. A reader extracting a monthly slope could take the literal main unit, while a reader extracting a24-week change could take the table header. The available model descriptions distinguish repeated-measures changes from random slopes but do not label this primary paragraph as a conversion.

**Alternatives and missing definition:** The main monthly wording may refer to the random-slopes analysis while the table refers to repeated-measures total changes; alternatively the main unit may be intended as PPN over24weeks. Which analysis generated each number needs identification. The following sensitivity rates are not assumed to be the same fit.

**Exact human question:** Are−9.32,−8.53 and−0.7824-week changes/differences or monthly rates, and which SVC analysis and unit should be extracted for the key secondary result?

### F-NUM-003 — Regimen-placebo exclusion statement does not reconcile with the survival denominator

**Relationships:** N024. **Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W; all relationships S_W. **Qualifying route:** Route B.

**Compared locations and roles:** REPORT [main PDFp4, Secondary Efficacy Outcomes, death/PAV paragraph](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4); REPORT [main PDFp7, Table2 regimen-placebo rows and footnotea](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=7).

**Printed inputs:** Main p4 says “4 of the41participants in the regimen placebo group and2 in the shared placebo group were excluded due to having no follow-up time (1 had PAV at baseline and1 terminated early at baseline visit).” Table2 reports regimen placebo4/41, while shared placebo9/162. Footnotea specifies2 shared-placebo exclusions, one baseline PAV and one early termination at baseline. Randomized regimen placebo is41 and shared placebo164.

**Rule and calculation:** Under the literal regimen exclusion statement,41−4=37 eligible rather than41. Half-unit intervals[40.5,41.5]−[3.5,4.5] produce recomputed eligible[36,38]. Printed table denominator41 has interval[40.5,41.5];gap2.5;relative discrepancy2.5/41=0.060976>0.05. By contrast,164−2=162 matches the shared denominator. Retaining the Table2 event numerator4, central percentages4/37=10.81% versus4/41=9.76% illustrate the extraction consequence; they do not establish the intended excluded persons.

**Affected result or extracted value:** The regimen-only key secondary PAV/death analysis population and control denominator used for its pooled and individual-dose comparisons.

**Why context does not resolve it:** The sentence grammatically applies “were excluded” to4of41 as well as2shared participants. Table2 gives4as the regimen event count and retains41as denominator. The parenthetical describes only2persons, leaving whether4means exclusions or outcomes unclear. This is a printed count/analysis-population conflict rather than a general missing-detail critique.

**Alternatives and missing definition:** The4of41 may be intended as the regimen-placebo event count, with only the2shared participants excluded. Alternatively the regimen table may retain a randomized denominator while Cox modeling omits4persons. Neither interpretation is expressly separated in the paragraph/table.

**Exact human question:** Were any regimen-placebo participants excluded for zero follow-up, or does4of41refer to death/PAV events; what is the regimen-only survival analysis denominator?

### F-NUM-004 — Serum NfL contrasts do not reproduce the back-transformed ratio calculation supported by the plasma rows

**Relationships:** N039. **Focus area:** B/C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W; all relationships S_W. **Qualifying route:** Route A, category 4.

**Compared locations and roles:** All REPORT [results supplement PDFp17,eTable3B, pooled/30mg/60mg plasma and serum NfL rows and footnote](../../../joi240158supp3_prod_1742927563.7911.pdf#page=17). The footnote states serum and plasma NfL were modeled log-transformed and exponentiated back, and expands GMR as geometric mean ratio. The same table uses one difference column for all six rows. Corroborating interpretation, REPORT [main PDFp8,Biomarker Analyses/Figure3](../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8) explicitly calls the treatment comparisons geometric mean ratios; that location is an alternative-definition aid rather than a separate qualifying cross-location discrepancy.

**Printed inputs:** Plasma placebo+7.9% throughout; active pooled−2.3%,30mg−1.3%,60mg−3.4%; printed differences−9.5%,−8.5%,−10.5%. Serum placebo+26.8% throughout; active pooled+0.4%,30mg+1.4%,60mg−0.5%; printed differences−26.4%,−25.5%,−27.4%. Corresponding serum intervals−50.3to−2.6,−52.2to1.3,−45.1to−0.7. Differences are percentages rather than positive raw ratios.

**Rule and calculation:** If A and P are each percent changes in back-transformed geometric means, the exponentiated between-group change contrast as a percent is100[(1+A/100)/(1+P/100)−1]. The supported method reproduces every plasma row: central−9.453%,−8.526%,−10.473% round to−9.5,−8.5,−10.5. Serum central recomputations are−20.820%,−20.032%,−21.530%; their half-unit input intervals versus the printed contrasts are:

| Serum row | Recomputed interval (%) | Printed difference interval (%) | Interval gap | Relative discrepancy |
|---|---|---|---:|---:|
| Pooled |[−20.890816,−20.749507]|[−26.45,−26.35]|5.459184|5.459184/26.4=0.206787|
|30mg|[−20.102483,−19.960552]|[−25.55,−25.45]|5.347517|5.347517/25.5=0.209707|
|60mg|[−21.600315,−21.459566]|[−27.45,−27.35]|5.749685|5.749685/27.4=0.209843|

Every relative gap exceeds0.05. Arithmetic subtraction instead gives0.4−26.8=−26.4,1.4−26.8=−25.4 and−0.5−26.8=−27.3; the two0.1differences are within half-unit intervals. Thus the serum rows align with an arithmetic percentage-point contrast while plasma supports a relative geometric contrast. This is not a crude raw-participant ratio; both inputs are the table's adjusted modeled changes.

**Affected result or extracted value:** The scale/definition and extracted magnitude of all three regimen-only serum NfL treatment contrasts in eTable3B.

**Why context does not resolve it:** Route A category4 applies: the source-supported back-transformation method reproduces the plasma rows but not the serum rows beyond display precision. The unstated definition is the human question. The common heading does not identify a switch of contrast scale.

**Alternatives and missing definition:** Serum may intentionally report the arithmetic percentage-point difference of individually back-transformed changes, while plasma reports a relative geometric contrast. A separate directly modeled treatment estimand could also be involved. If so, the serum/plasma distinction and the confidence-interval scale require definition. No preferred analysis is proposed; the printed quantities are recorded literally.

**Exact human question:** What is the intended serum NfL contrast in eTable3B—an arithmetic difference of percentage changes or an exponentiated geometric mean ratio—and why does its calculation differ from the plasma rows under the same reported transformation?

## Excluded observations

Only apparent issues considered but not emitted appear here; reconciled checks remain in the N inventory. The exact half-unit rule is applied to counts as required, including small integer differences.

| Location | Observation | Reason code |
|---|---|---|
|DOC-001 pp1,4,6,abstract/body meanage|58.4vs57.7years gap.60/58.4=1.027% afterhalf intervals;weightedTable1age58.02likewisebelow5%.|ROUNDING_OR_DISPLAY_PRECISION|
|DOC-001 p1fatigue;DOC-004 p22fatigue|12/120vs10.8% gap.289749/10.8=2.683%;count12vs13copieshalfintervalstouch. Neither is reproduced by mandatedrule.|ROUNDING_OR_DISPLAY_PRECISION|
|DOC-001 p5regimenplacebofollow-upreasons|Total6versus2+1+1+1=5; recomputed[3,7]overlapstotal[5.5,6.5].|ROUNDING_OR_DISPLAY_PRECISION|
|DOC-001 p4completionvsFigure1|Shared137/164=83.54%vs85%;roundingintervalgaprelative1.40%below5%.|ROUNDING_OR_DISPLAY_PRECISION|
|DOC-001 p6racefootnote|Threeunknownracevs164−160=4;subtractioninputinterval[3,5]overlaps[2.5,3.5].|ROUNDING_OR_DISPLAY_PRECISION|
|DOC-001 p9RCT13eventsvspp4,7fiveplusnine|Countsuminterval[13,15]overlapsprinted[12.5,13.5];independent14pointsumdoesnotpassprecisionrule.|ROUNDING_OR_DISPLAY_PRECISION|
|DOC-004 p21moderateTEAE|Pooled44vs22+24=46;sum[45,47]vsprinted[43.5,44.5]gap.5/44=1.136%.|ROUNDING_OR_DISPLAY_PRECISION|
|DOC-004 p21sharedTEAEseverityeventtotal|Mild673+moderate164+severe47=884vsany889;sum[882.5,885.5]vs[888.5,889.5]gap3/889=.337%;below5%.|ROUNDING_OR_DISPLAY_PRECISION|
|DOC-001 p4vsDOC-004 p15functionalCrIs;DOC-001 p8plasmaCIcopies|Matchedfunctionalboundgapsunder1.3%;plasmaupper−.4vs−.5halfintervalstouch,lower−17.8vs−18.0relativegap.562%.|ROUNDING_OR_DISPLAY_PRECISION|
|DOC-001 p7Figure2A vsDOC-004 p14eTable1visitcounts|Observedcountsanddeath/PAV-excludedfunctionalcontributorsdiffer;per-timepointcomparisondoesnotchangeFASrandomizedsize.|PERIPHERAL_COMPARISON|
|DOC-001 p8serumresultvsDOC-004 p17serumrow|30.8vs26.8change,−23.2vs−26.4contrast,−39.5vs−50.3lowerCI exceed5%,butmatchedexploratorycross-documentcopiesareperipheral;within-tableeffectidentityisF-NUM-004.|PERIPHERAL_COMPARISON|
|DOC-001 p7Table2adjustedHRvscrudeeventratios|AdjustedCoxHRs.46/.06/.96/.25/.03/.47neednotmatchcrudeeventriskratios;profilelikelihoodCIstated.|MODEL_VERSUS_CRUDE|
|DOC-002 pp100–101,171–172particlequantities|Particleper60mLnot60timespermL,butthesearehistorical/preclinicalPLANrationale,nottrialresult/power/decisionrule.|PERIPHERAL_COMPARISON|
|DOC-001 p7exploratoryassistedventilation16(18%)/9(31%)|Baselineprevalent-eventexclusionsestablishoutcome-specificrisksets;exactdenominatorsnotprinted. Assumptions120/41donotestablisha reproducedcount/denominatorconflict.|CONDITIONAL_OR_UNREPORTED|

## Evidence and limitations

Direct source confirmation used fresh sorted-layout text mainPDFpp1–9 andresultsPDFpp15–17, plus visually inspected CPU200dpi renders mainp4,p5,p8 andresultsp15,p16,p17 under ../preprocessing/numeric/. Commands use /home/juliz/venvs/stt/bin/python workflow_1_6_2/scripts/pdf_tools.py; engine PyMuPDF1.28.0. Only missing direct-tool capabilities text/layout/render were used. All suppliedsources and reusedassets preserved. No newOCR needed. UserGPUrequest retained;noCPUOCRperformed.

Sourcevisualp5confirms1regimen-placebodeath;initialmapperM028transcription3wasreported tocoordinatorforcorrection. Itdoesnotproduceafinding. All250eTable5cells,all35subgroupnumericrows,andbothfullsecondary tableswerecovered;parametersandprospective examplesareexplicitlytrackedinNinventory. Unprintedcurvecoordinates,unknownoutcome-specificrisksets,rawdatamomentsandcompleteobservedmodeldataareunavailableandnotinvented. No numericalcoveragegap remains.
