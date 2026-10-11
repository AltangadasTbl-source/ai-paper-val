# Cross-source consistency review

Fresh mandatory cross-source stage; complete assigned scope: DOC-001 REPORT, physical pages 1–11; DOC-002 PLAN, pages 1–37; DOC-003 PLAN, pages 1–7; DOC-004 REPORT, pages 1–14. Source-linked current main/support quantitative maps and their complete transcripts were used as locators. No old candidate, disposition, classification, or report was used. No external evidence, packages, Python, OCR, or source/asset mutation was used. No stable candidate IDs or human judgments are assigned here. All observations require human adjudication.

Engine: available direct Poppler `pdftotext -layout -f N -l N SOURCE -`, inspected stdout for main pp4,8, protocol pp14,24,27–30, SAP pp1–3,5,7, results supplement pp3,6–7,13–14. Existing rendered main p8 and supplement p2 images were visually inspected; historical rendering engine is unrecorded, direct-source recheck remains final authority. Quantitative maps restore table layout; graph positions below are approximate diagnostics, never fabricated printed coordinates.

## Complete matched-relationship coverage

Population, period, contrast, adjustment, reference group, measure, unit, analysis set, and precision were matched before comparison. Distinct GEE identity-link differences and log-link ratios were kept distinct. Mapping keys here refer to the current mapper artifacts; numeric/statistical checkers own canonical inventories.

| Assigned relationship scope | Matched supplied locations and result |
|---|---|
| Main N001–N004 / SUP-001,004 | Abstract, key points, flow, Methods, Results and protocol populations/dates. 21 analyzed hospitals =10+11; 23 randomized less2 withdrawn; 144539 discharges=50173+94366; 559443 days=251859+307584. Protocol22 intended and23 randomized are different planning/realized quantities. Strict/inclusive age bounds differ but no exact-age subject count is supplied; no candidate solely from general eligibility wording. |
| Main N005–N012 / SUP-003,004,013,014,016,017 | All flow totals/means/ranges, five-week run-in, three extensions, documentation sample totals, table1 counts. Means round correctly. Exact eTables expose two differing flow extrema (observations below). Five-patient weekly sampling, 8109/8190=99.0%, and post sample5420=2588+2832 agree. Revised seven-to-five documentation threshold and last-set analysis explicitly disclosed main p4; no candidate from that change alone. |
| Main N013–N016 / SUP-005,006,009–012,015,018 | All numerical endpoint thresholds, scale codes, resource units, denominator and aggregation/model definitions matched to displayed event families. Distinct concrete endpoint/denominator/scale conflicts recorded below. Changes to stratum inclusion and nonconvergent baseline-adjusted difference models disclosed in main Methods/table footnotes; no undocumented-equivalence assumption. |
| Main N017 / SUP-001,007,008,019 | All mortality/SCDE power inputs, absolute and relative units, annual/two-year historical counts and anticipated/actual study totals compared. Distinct source roles maintained even for historical background in protocol. Actual244 deaths and386 SCDE agree across main table3 and eTables2,3,5;1.7 versus1.69 is display precision. Expected507≈99389×5.1/1000 and795≈397556×2/1000. Bed inputs differ conditionally below. |
| Main N018–N024 / SUP-016,017,019 | Every main table1 hospital characteristic and each flow group summary checked against matching counts/denominators; table1 wardbeds937+1148=2085 agrees eTable5. Baseline hospital days129700+162497=292197 and discharges26664+46718=73382 agree. ICU and hospital discharges are kept distinct. |
| Main N025–N026 / S001–S008 / SUP-014 | Every table2 row matched narrative: seven mean/SD observation frequencies plus count/proportion completeness row. Narrative repeated differences/CIs/raw P agree; adjusted Holm P is a different printed column. FigureS2 distributions visually compatible with ≥5 completeness99.0%/60.9%; no graph-digitization candidate. |
| Main N027–N029 / S009–S021 / SUP-015–019 | Every main table3 cell checked against matched eTable2/eTable3 aggregate cells, abstract, Results and Discussion. Mortality52/97 vs61/147; noDNR26/42 vs16/47; SCDE80/127 vs144/259; arrest15/27 vs18/32; preventable11/21 vs12/29 all agree. 244 totaldeaths−89 noDNR=155 DNR=63.5%. SCDE386=127+259; cardiac59=27+32;127/828=15.3%,259/1178=22.0%;21/27=77.8%,29/32=90.6%, discussion78%/91% agree. Physician1727+1157=2884; consultation1015+1694=2709; resuscitation126+179=305 agree. No pooling of calls as unique patients. |
| Main S009–S011, S016–S018, S024–S025 / SUP-E01,E02 | All repeated inferential values agree, including abstract mortality0.01(−0.80,0.81),OR1.01(.61,1.69),P.96 and deterioration−.34(−.73,.05),RR.77(.61,.97),P.03. SCDE identity difference footnote says unadjusted baseline whereas ratio is adjusted; they are not the same inferential model. Narrative blanket adjustment wording is a concrete label question for statistical lane rather than a new numeric conflict here. |
| Main S022 / SUP-005,015 | Main preventability κ.35(.15,.51), threshold4 and percentages match REPORT definitions; PLAN has distinct scale/threshold conflicts below. |
| Main S023 / N030 / SUP-013,G01 | All graph axes, color/style/group legend, caption, exact hospital table coordinates and slope interpretation checked. Two independent reversals and one horizontal-axis label conflict recorded. Slopes.57/.53 and P.94 are not independently reconstructable without fitted-model variance; no candidate solely from unknown convention. |
| Main S024–S025 / SUP-012,018,E01–E15 | All eTable4 descriptive patient rows and fifteen effect/CI/P triples checked for main narrative overlap, SAP aggregation and units; main urgentICU109=42+67 deaths;1653=686+967 per-patient analysis, distinct from2006=828+1178 admissions. LOS/ventilation summary totals not required to equal rounded mean×N exactly. Predicted mortality is sum of patient inverse logits rounded to integer, not observed deathcount. |
| SUP-H01–H23 / SUP-001,002 and protocol tables1,2 | Every historical AUC/P/count family and narrative reuse matched to its own historical population/threshold. Different instruments and original versus simplified scores do not imply equal sensitivity. Protocol82%,>80%, and83% involve historical descriptions without enough sample/threshold alignment to register a discrepancy. Bibliographic number/date differences alone excluded. |
| SUP-P01–P05 | All five power families inspected, including mortality18%, lower-baseline19.9%, SCDE31%, codeblue41%,stat18.1%. Printed stat1.45 versus8.13×.181≈1.4715 is a numeric-lane arithmetic relationship, not an independent cross-source mismatch. Codeblue nested `/1000` units likewise numeric/statistical-lane issue. |
| SUP-G02,E16 | Documentation significance has no separate fitted numeric statistic to compare; Bayesianκ.43(.17,.77) is contained and no other same-method CI is supplied. |
| Administrative/reference units | Main pp10–11, protocol pp17–18,21–23,25–26,31–37 and supplement cover inspected through complete source maps; administrative timings or literature identifiers have no additional matched reported-result contradiction. |

Limitations: No supplied raw data/workbook/CSV, patient identifiers, final analysis code execution, or model covariance. Precise plot-coordinate estimates are not printed; use supplied hospital table values. Historical reusable image engine unrecorded. These constrain mechanisms or reconstruction, not assigned scientific coverage.

## Distinct quality-control observations

### Observation X-A — Main mortality graph group encoding reversed in caption

- Locations/roles: [Main Figure2 graph legend and fitted lines, p8](../../../jama_parshuram_2018_oi_180015.pdf#page=8), REPORT; [same Figure2 caption, p8](../../../jama_parshuram_2018_oi_180015.pdf#page=8), REPORT. Corroboration only: [eTable2 A–J/K–U assignments, p9](../../../joi180015supp3_prod.pdf#page=9), REPORT.
- Printed inputs: legend assigns BedsidePEWS(10 hospitals) blue-gray circles/solid line and usualcare(11 hospitals) orange/dashed line. Caption assigns BedsidePEWS “dashed orange line” and usualcare “solid blue line,” alongside group slopes0.57 and0.53.
- Rule/direct observation: one plotted line/group cannot simultaneously have the two reversed encodings in the same figure. This is group attribution of quantitative fitted mortality relationships, not general wording.
- Alternatives: caption labels or plotted legend could be transposed; exact A–J hospital coordinates corroborate the graph legend, but no final correction is prescribed.
- Human verification: inspect Figure2 legend, line styles, and eTable2 pointC baseline6.03/post.8 to determine intended group-to-slope encoding.
- Provenance: current main N030/S023, support SUP-013; fresh cross-source graph inspection. Relationships: S_W; primary-category suggestion Measure, label, or scale inconsistency.

### Observation X-B — Supplemental mortality graph group encoding reversed in caption

- Locations/roles: [eFigure1 graph/legend, p2](../../../joi180015supp3_prod.pdf#page=2), REPORT; [eFigure1 caption, p3](../../../joi180015supp3_prod.pdf#page=3), REPORT; [eTable2 group letter identities, p9](../../../joi180015supp3_prod.pdf#page=9), REPORT (corroboration).
- Printed inputs: graph legend assigns usualcare salmon/red dotted line and BedsidePEWS turquoise dashed line; A–J points turquoise, K–U salmon. Caption correctly assigns A–J BedsidePEWS/K–U usualcare but then says BedsidePEWS marked salmon/usualcare blue and intervention dotted salmon/usualcare dashed blue.
- Rule/direct observation: quantitative group/color/style assignments in caption are opposite the legend and letter identities.
- Alternatives: transposed caption descriptors or legend; A–J letters and eTable2 favor legend, pending source verification.
- Human verification: trace pointH and pointU from eTable2 to eFigure1 and resolve which fitted line/group description is intended.
- Provenance: SUP-013/G01; fresh graph and direct caption text. Relationship S_W; category suggestion Measure, label, or scale inconsistency. Distinct from X-A because source figure and printed comparator differ.

### Observation X-C — Main mortality graph horizontal-axis period label conflicts with coordinates

- Locations/roles: [Main Figure2 axis/caption, p8](../../../jama_parshuram_2018_oi_180015.pdf#page=8), REPORT; [eFigure1 baseline axis, p2](../../../joi180015supp3_prod.pdf#page=2), REPORT; [eTable2 hospitalC, p9](../../../joi180015supp3_prod.pdf#page=9), REPORT.
- Printed inputs: main horizontal axis “Deaths per1000 Discharges During Baseline and Intervention Periods”; caption says coordinates baseline/intervention. Supplement horizontal axis says baselineperiod. HospitalC baseline4/663=6.03/1000,post1/1250=.8/1000,total5/1913.
- Rule/calculation: combined-period C rate=5/1913×1000≈2.61, distinct from baseline6.03. Main rightmost blue-gray point is nearx6.03,y.8, as in eFigure1 C; it represents baseline rather than combined-period mortality.
- Alternatives: axis may contain an extra period phrase; changing plotted coordinates would be a different hypothesis. Graph coordinates are approximate visual diagnostics; exact rates come from eTable2.
- Human verification: compare both plots and hospitalC table; determine intended horizontal-period label.
- Provenance N030/SUP-013,016. Substantive relationships S_W and S_C; category suggestion Measure, label, or scale inconsistency.

### Observation X-D — Usual-care baseline patient-day minimum differs

- Locations/roles: [Main Figure1 usualcare baseline box, p3](../../../jama_parshuram_2018_oi_180015.pdf#page=3), REPORT; [eTable3 baseline patient days, p11](../../../joi180015supp3_prod.pdf#page=11), REPORT.
- Printed inputs: Figure1 usualcare162497 days,range6665–31575. eTable3 usualcarehospitalL6655; all other usualcarebaseline values exceed6655.
- Rule/direct observation: matched 11-hospital baseline minimum must equal minimum of listed rows;6665≠6655, difference10 days. Group total matches162497, so alignment is not to withdrawn hospitals.
- Alternatives: one printed extremum or hospital row may be transcribed incorrectly; no automatic correction.
- Human verification: compare L's baseline source count and recompute eleven-row minimum and total.
- Provenance N008/SUP-017. Relationship S_C; category Cross-document numeric inconsistency.

### Observation X-E — Usual-care intervention discharge maximum differs

- Locations/roles: [Main Figure1 intervention and analysis boxes, p3](../../../jama_parshuram_2018_oi_180015.pdf#page=3), REPORT; [eTable2 postrandomization discharges, p9](../../../joi180015supp3_prod.pdf#page=9), REPORT.
- Printed inputs: both main usualcareboxes94366 discharges,range3672–29956. eTable2 maximumhospitalT26956,with nextlargestU17238.
- Rule: matched 11-hospital postrandomization maximum29956≠26956; difference3000 discharges. Total94366 matches table.
- Alternatives: flow extremum or hospitalrow error; repetition of flow boxes does not create a second observation.
- Human verification: check T's original discharge count and all eleven-row extrema.
- Provenance N011/SUP-016. Relationship S_C; category Cross-document numeric inconsistency.

### Observation X-F — Anticipated ward-bed input differs between report and protocol

- Locations/roles: [eTable5 anticipated pediatricwardbeds, p14](../../../joi180015supp3_prod.pdf#page=14), REPORT; [protocol sample-size assumptions, p14](../../../joi180015supp1_prod.pdf#page=14), PLAN; [protocol appendix assumptions, p29](../../../joi180015supp1_prod.pdf#page=29), PLAN (alternative basis).
- Printed inputs: eTable5 anticipated2397 beds with99389 discharges/397556 days. Protocol participating-hospitalinput2322 beds with same99389/397556. Protocol appendix20hospitals×mean119.85beds.
- Rule/diagnostic: same count companions identify apparent matching anticipated cohort, but2397−2322=75; alternatively20×119.85=2397 exactly, so eTable5 may summarize constant-size power design instead of observed candidate-hospital total.
- Missing definition/alternatives: design-derived2397 versus participating-site2322 is a supported distinction, not assumed resolved. Tablecaption mentions constantcluster-size assumptions but does not explicitly identify bedrow source. No protocol violation is inferred.
- Human verification: identify whether anticipated wardbedrow is model total or participating-site census and label the basis consistently with discharge/day rows.
- Provenance SUP-007,019; relationship P_R if matching anticipated cohort is intended, classification ambiguity explicit; category Cross-document numeric inconsistency.

### Observation X-G — Protocol mortality absolute-reduction percentage differs by factor ten

- Locations/roles: [protocol mortality appendix, p29](../../../joi180015supp1_prod.pdf#page=29), PLAN; [protocol sample-size summary,p1](../../../joi180015supp1_prod.pdf#page=1), PLAN; [protocol sample-size assumptions,p14](../../../joi180015supp1_prod.pdf#page=14), PLAN. [Main power,p4](../../../jama_parshuram_2018_oi_180015.pdf#page=4), REPORT corroborates0.9/1000 only.
- Printed inputs: appendix18%relative reduction “absolute risk reduction of0.9%”; p14 same18% at5.1/1000 gives0.09%; p1 gives0.9deaths/1000.
- Rule/calculation:5.1/1000×.18=.918/1000=.0918%, rounding to.9/1000=.09%;.9% equals9/1000 and exceeds baseline5.1/1000.
- Alternatives: decimal/unit transcription in appendix or different undocumented baseline. No final correction assigned.
- Human verification: confirm absolute scale used in original power calculation and compare p1,p14,p29.
- Provenance SUP-P01,007. Relationship P_P; main corroboration creates no P_R discrepancy. Category Measure, label, or scale inconsistency.

### Observation X-H — Protocol cardiac-arrest scale codes differ

- Locations/roles: [protocol narrative,p11](../../../joi180015supp1_prod.pdf#page=11), PLAN; [protocol Table5,p24](../../../joi180015supp1_prod.pdf#page=24), PLAN; [protocol Table6 legend,p27](../../../joi180015supp1_prod.pdf#page=27), PLAN.
- Printed inputs: narrative cardiacarrests rated6or7; Table5 level6compressions/ECMO and7warddeath, levels4circulatory and5respiratory+circulatorysupport. Table6legend says cardiacarrest “scale rating4or5.”
- Rule: same named resuscitationintensityscale cannot map arrest simultaneously to4/5 and6/7 with displayed different category treatments. This is quantitative scale-code attribution for adjudicated arrestcounts, not a design critique.
- Alternatives: outdated legend codes or different undisclosed scale; adjacent Table5 and narrative support6/7.
- Human verification: confirm actual review-form intensity coding and Table6legend source.
- Provenance SUP-005. Relationship P_P; category Measure, label, or scale inconsistency.

### Observation X-I — Protocol preventability threshold excludes and includes rating4

- Locations/roles: [protocol narrative,p11](../../../joi180015supp1_prod.pdf#page=11), PLAN; [protocol Table7 legend,p28](../../../joi180015supp1_prod.pdf#page=28), PLAN. [REPORT eTable1,p6](../../../joi180015supp3_prod.pdf#page=6), REPORT and [main Table3footnotei,p7](../../../jama_parshuram_2018_oi_180015.pdf#page=7), REPORT corroborate inclusion4 only.
- Printed inputs: p11 consensusrating“>4” yet immediately enumerates4,5,6 as potentiallypreventable. Table7 “4or more.”
- Rule: numericrating4 fails>4 and meets≥4; both cannot define same dichotomy. The reported21/27 and29/32 are threshold-dependent but number of rating4events is not supplied; do not infer how counts would change.
- Alternatives: strict-symbol typo or obsolete threshold, pending source review.
- Human verification: inspect final consensus-rating cutoff applied and harmonize prospective threshold description. Corroborating report definitions do not create a report-plan discrepancy.
- Provenance SUP-005,015/S022. Relationship P_P; category Measure, label, or scale inconsistency.

### Observation X-J — Historical urgent-ICU1052 count has annual versus two-year time basis

- Locations/roles: [protocol sample-size assumptions,p14](../../../joi180015supp1_prod.pdf#page=14), PLAN; [protocol appendix,p30](../../../joi180015supp1_prod.pdf#page=30), PLAN.
- Printed inputs: fourOntariopediatric hospitals1052urgentICUadmissions/year; appendixsamefour-centerdataset1052urgentPICUadmissions in two years following31January2007, with55963discharges/150codeblueevents.
- Rule/calculation:1052 overtwo years annualizes526, not1052. Counts/time cannot be interchanged without factor2 when matched cohort is intended.
- Alternatives: p14 may reference a different year/cohort coincidentally having1052, or appendixperiod/count may differ; exact historical table identification is missing. No derived change to power asserted.
- Human verification: establish the original data interval used for SCDE assumptions and distinguish annualized versus two-year count.
- Provenance SUP-007,008. Relationship P_P; category Rate-versus-count inconsistency.

### Observation X-K — SCDE fluid threshold includes versus excludes exactly60mL/kg

- Locations/roles: [main StudyOutcomes,p4](../../../jama_parshuram_2018_oi_180015.pdf#page=4), REPORT; [eTable1SCDE,p6](../../../joi180015supp3_prod.pdf#page=6), REPORT. [protocol Table5,p24](../../../joi180015supp1_prod.pdf#page=24), PLAN corroboratesstrict>60 only.
- Printed inputs: mainfluidboluses“60mL/kg or greater” within12hours; eTable1“>60ml/kg” within12hours. Reported SCDEcounts127/259 and386total refer to this composite.
- Rule: exactly60 with no other component satisfies≥60 but not>60. This is a numerical boundary discrepancy defining a reported quantitative endpoint; no count of boundarypatients is supplied and no change in386 is claimed.
- Alternatives: fluidthreshold symbol/phrase transcription or operational tolerance; intended comparator unknown.
- Human verification: inspect event adjudication threshold and any source patients exactly60mL/kg; identify which report definition matches applied rule.
- Provenance N013/SUP-015,005. Relationship S_C; protocolonly corroboratesone side, no independent P_R required. Category Measure, label, or scale inconsistency.

### Observation X-L — SCDE circulatory component uses AND versus OR

- Locations/roles: [protocol Table5level4,p24](../../../joi180015supp1_prod.pdf#page=24), PLAN; [eTable1SCDE,p6](../../../joi180015supp3_prod.pdf#page=6), REPORT; [main StudyOutcomes,p4](../../../jama_parshuram_2018_oi_180015.pdf#page=4), REPORT.
- Printed inputs: protocol>60mL/kg fluids AND inotrope/vasopressor forcirculatorylevel4(markedSCDEYes); reporteTable1>60fluids “and/or” anyinotrope; main listsvasoactive medication OR qualifyingfluid among one-or-morecomponents.
- Rule: fluidonly orvasoactiveonly,withoutanotherSCDEcomponent,is positiveunderreportOR butnotunderprotocolAND. Different logical definitions attach tosame reported composite386=127+259, not mere missingmodeldetail.
- Alternatives: endpoint definition amended, report prose broadened, or protocol conjunction inexact; no amendment evidence in supplied package establishes reason. No resulting count change or protocol violation inferred.
- Human verification: obtain the operationalcirculatorycriterion applied to event abstraction and determine whether discrepancy reflects amendment or descriptive error.
- Provenance N013/SUP-005,015. Relationship P_R; category Measure, label, or scale inconsistency. Distinct fromX-K:logical conjunction differs independent of60boundary.

### Observation X-M — Blanket ICU-outcome denominator conflicts with per-patient resource summaries

- Locations/roles: [main DataAnalyses,p4](../../../jama_parshuram_2018_oi_180015.pdf#page=4), REPORT; [eTable4resourceoutcomes,p12–13](../../../joi180015supp3_prod.pdf#page=12), REPORT (link [footnotes,p13](../../../joi180015supp3_prod.pdf#page=13)); [SAP patientaggregation,p7](../../../joi180015supp2_prod.pdf#page=7), PLAN corroboration only.
- Printed inputs: mainpatientoutcomes expressed“per1000patient-days in theICU(ICUoutcomes).” eTable4ICUtotalLOSpostmeans9.4/9days,ventilator-freedays23.9/24,MVdays4.1/3.7; tablefootnote explicitlyper-patienttotal/meanICUstays and means/SD, differences1.28/.26/.69 respectively. Patientdenominators686/967.
- Rule: per-patientdurationmean(sumdays/patients) differs dimensionally from event/durationrateper1000ICUpatientdays; displayed day means and Gaussian mean differences are not quantitiesper1000ICUpatientdays.
- Alternatives: maindenominatorstatementintendedonlya subset ofICUoutcomes; eTable4per-patientanalysesotherwisecoherent. This is scope/labelofprintedunit, not demandfornewanalysis.
- Human verification: identify preciselywhichICUoutcomesmainrate-denominatorstatementcovers and confirm resource means/differences use patientrecords as defined.
- Provenance N015/SUP-012,018. Relationships S_C andS_W (same-mainMethods/OtherOutcomesunitcontext); category Measure, label, or scale inconsistency. SAP corroborates REPORTtable, no P_R discrepancy.

### Observation X-N — ICU-readmission reported denominator differs from original protocol

- Locations/roles: [protocol readmissiondefinitions,p12](../../../joi180015supp1_prod.pdf#page=12), PLAN; [main Table3 ICUreadmissionrow/footnote,p7](../../../jama_parshuram_2018_oi_180015.pdf#page=7), REPORT; [SAP shelltable,p5](../../../joi180015supp2_prod.pdf#page=5), PLAN.
- Printed inputs: protocol “PICUmortality,andunplannedre-admission(hospital,PICU)willberepresentedperthousandhospitaldischarges.” MainpostICUreadmission94(28.40)/108(21.25) explicitlyper1000ICUdischarges; SAPtableunplannedICUreadmissiondenominatorICUdischarges. Mainhospitaldischarges50173/94366.
- Rule/diagnostic:94/50173×1000≈1.874 and108/94366×1000≈1.144, not28.40/21.25; displayed ICU-readmissionrateunits follow ICU discharge denominator. Mortality is not part of this discrepancy because maintableoffersbothICUandhospitalmortalitydenominators.
- Alternatives: laterSAPchangeddenominator, originalprotocolphraseovergeneralized, or units revised. Supplied finalSAP supportsREPORTdenominator butdoesnoteraseconflictwithinPLANversions. No protocol violation alleged.
- Human verification: confirm intended original and final ICUreadmissiondenominator and whether change was documented; use finallabelwhenextracting reported rates.
- Provenance S020/SUP-006,011. Relationships P_R andP_P; category Measure, label, or scale inconsistency.

## Non-candidates and extraction correction

- Important source-reading correction: support map's apparent eTable4PIMbaseexcess+35 versus eTable1−35 mismatch is not reproduced in direct layout text. On supplementp13, minus sign is at end of previous line and35 at beginningnextline; printed input is−35, agreeingp7. Do not register a candidate from native-text line-wrap loss.
- “144539patients(100%)” equals printed dischargecount, but packagehasnoall-hospitalunique-patientcount todisproveequality. RepeatedurgentICUstaysdonotbythemselvesdemonstratemultiplehospitaldischargesinthesameperiod. No candidate solelyfrommissinguniqueidentifierdefinition.
- DiscussionCIbound0.8 versus endpoint.81 is compatibleone-decimalwording, not independently contradictory.
- Main“adjustedbetween-groupratedifference”forSCDE versus tablefootnoteunadjustedbaseline is a statistical-lane concrete labelrelationship; the source values and distinct fittedmodels are preserved in full coverage above. It is not silently treated as estimate/CI/P incompatibility.
- No supplied displayed-zeroP value produces an independent cross-source contradiction. DISPLAY_ZERO_NOT_CANDIDATE policy applied; none registered for formatting.

Emitted distinct observations:17. Assigned matched-result coverage complete; no scientific unit left unmapped by this stage. Classifications above are relationship/category suggestions for coordinator mechanics, not adjudications. Every eventual stable candidate remains Pending Human Adjudication.

### Observation X-O — SAP predicted-mortality discharge denominator differs from per-patient reported quantity

- Locations/roles: [SAP ICU analysis table, p7](../../../joi180015supp2_prod.pdf#page=7), PLAN; [eTable4 predicted mortality row, p12](../../../joi180015supp3_prod.pdf#page=12), REPORT; [eTable4 footnote b, p13](../../../joi180015supp3_prod.pdf#page=13), REPORT; [main urgent ICU admission count, Table3,p7](../../../jama_parshuram_2018_oi_180015.pdf#page=7), REPORT (denominator comparator).
- Printed inputs: SAP row “PIM II Prediction Mortality (/1000 urgent ICU discharges)” while table description says average probability over admissions and introductory analysis says one record per patient. eTable4 post BedsidePEWS predicted38(5.5%), usual44(4.6%), with686/967 patients; footnote sums patient inverse logits and divides by total patients. Main admission events828/1178.
- Rule/diagnostic: per-patient prediction and per-admission discharge prediction have different denominator labels when repeat admissions are combined. Rounded predicted counts give38/686×100≈5.54% and44/967×100≈4.55%, matching displayed patient proportions;38/828×1000≈45.89 and44/1178×1000≈37.35, distinct from patient quantities55/46 per1000. These diagnostics use rounded predicted counts, not original probability sums. Admission counts are denominator comparators, not proof that every admission count equals discharge count in all circumstances.
- Alternatives: SAP row label is inherited from an admission-based analysis while its description and REPORT use patient means; or a different discharge population is intended. No change to fitted0.69 percentage-point difference is inferred.
- Human verification: determine intended denominator and reporting scale for this named predicted-mortality outcome and reconcile SAP row label with its patient aggregation description.
- Provenance: direct fresh SAPp7 inspection, SUP-012,018/S025. Relationships P_R and P_P; category Measure, label, or scale inconsistency. Missing final prediction records limit reconstruction only.

### Observation X-P — SAP ICU-readmission Poisson model label versus reported odds ratio

- Locations/roles: [SAP shell table, p5](../../../joi180015supp2_prod.pdf#page=5), PLAN; [main Table3 ICU-readmission row and model footnotes, p7](../../../jama_parshuram_2018_oi_180015.pdf#page=7), REPORT; [protocol model specification, p16](../../../joi180015supp1_prod.pdf#page=16), PLAN (corroboration of logistic model).
- Printed inputs: SAP “Unplanned ICU Readmissions” uses ICU discharge denominator and model “Poisson.” Main matched outcome ICU readmission within48 hours reports adjusted “OR”1.11(.77–1.61),P.58. Original protocol says the identical mortality logit approach will be used for unplanned ICU readmission.
- Rule: Poisson log-link count/rate modelling gives rate-ratio interpretation; the reported row explicitly names odds ratio from a logistic model. They are different measure/model labels even with the same discharge denominator. The numeric OR is not transformed to an RR without data.
- Alternatives: obsolete or mislabeled SAP shell-table family; final analysis changed to logistic; unspecified link in shell-table weakens any reconstruction claim but does not reconcile printed Poisson versus logistic labels. No assumption that code shown was actually run.
- Human verification: inspect the final fitted family/link for ICU-readmission OR and reconcile the shell-table model designation. This is a concrete reported measure label, not a generic design criticism.
- Provenance: fresh SAPp5 inspection, main S020/SUP-009,011. Relationships P_R and P_P; category Measure, label, or scale inconsistency. Distinct from X-N because comparator here is model/measure, not exposure denominator.

### Observation X-Q — SAP hospital-readmission Poisson model label versus reported odds ratio

- Locations/roles: [SAP shell table,p5](../../../joi180015supp2_prod.pdf#page=5), PLAN; [main Table3 hospital-readmission row and model footnotes,p7](../../../jama_parshuram_2018_oi_180015.pdf#page=7), REPORT; [protocol model specification,p16](../../../joi180015supp1_prod.pdf#page=16), PLAN (corroboration).
- Printed inputs: SAP “Unplanned Hospital Readmission” uses hospital discharges and “Poisson.” Main hospital readmission within48 hours reports adjusted OR.93(.61–1.41),P.74. Protocol specifies same logit approach as mortality for this outcome.
- Rule: named Poisson count/rate family conflicts with logistic odds-ratio outcome family; hospital discharge exposure itself agrees. No numerical conversion between OR and RR is asserted.
- Alternatives: shell-table label outdated, final family changed, or unspecified-link shell notation; supplied output code is absent so implementation mechanism remains unknown.
- Human verification: confirm final model family/link for the displayed hospital-readmission OR and reconcile the SAP row designation.
- Provenance: fresh SAPp5 inspection, main S021/SUP-009,011. Relationships P_R and P_P; category Measure, label, or scale inconsistency. Separate from X-P because the outcome, printed ratio, and matched row differ.

Final emitted distinct observation count: 17 (X-A through X-Q). No stable IDs were assigned or removed.
