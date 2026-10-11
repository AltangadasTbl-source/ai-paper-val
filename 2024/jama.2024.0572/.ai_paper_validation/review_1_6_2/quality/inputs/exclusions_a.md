# Complete excluded-observation audit handoff A

Mechanical lossless partition of all current checker excluded/reconsideration rows. No scientific decision is changed. Part A owns 47 original checker rows plus 45 second-pass rows; part B owns 28 original rows plus 66 second-pass rows. Their union contains all 75 initial and all 111 second-pass rows exactly once. The second-pass main row73 forwards F-ST2-601 for screening and is a qualifying reconsideration rather than a retained exclusion. Full original checker artifacts remain available.

## Original checker: numeric_parts/main.md

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p. 5 Table 1, coronary artery disease; N033 | Header n168 gives 39/168 = 23.214% vs 23.5% and 25/168 = 14.881% vs 15.4%. Even treating counts as exact, gaps after the printed ±0.05% interval are 0.236/23.5 = 0.0100 and 0.469/15.4 = 0.0305; allowing count/denominator half-units only reduces them. Both are below 0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p. 5 Table 1, tenecteplase, thrombolytics and anesthesia; N053, N054 | Tenecteplase is nested in thrombolytic recipients, not all168 participants: 4/33 = 12.121% vs12.5% and 1/28 = 3.571% vs3.7%; residual relative gaps are below0.05 even with exact counts. Anesthesia100/168 =59.524% vs59.9%, thrombolytics28/168 =16.667% vs16.8%, also within threshold. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p. 7 Figure 2, all four arm rows; N071, N072, N073, N074 | Whole-percentage segment totals are101,101,101,99. Independent half-unit intervals contain100; category colors, rather than text extraction order, establish missing-width categories. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 pp. 6, 7 and9, aRR abbreviation expansion; N080, N083, N086, N090, N092, N094, N098, N100, N102 | “Absolute risk reduction” expansion differs from the ratio quantity evident from modified Poisson methods, null1, ratio-valued intervals and footnotes stating higher rate ratio. The ratio interpretation is immediately identifiable; no conflict with an evidently computed alternate numeric measure was reproduced. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001 p. 9 Table3; N088, N090, N092, N094, N096, N098, N100, N102 | Crude within-arm mismatch/no-mismatch outcome ratios and median comparisons differ from some adjusted estimates; the table explicitly adjusts age, NIHSS, time and core. Direction reversals relative to crude counts do not establish a numeric conflict. | MODEL_VERSUS_CRUDE |
| REPORT DOC-001 p. 11 discussion “two-thirds” versus p. 9 204(61%); N113 | Approximate prose fraction is not an additional independent population discrepancy; the materially different p. 4 count is retained in F-NUM-001. | DUPLICATE_OF_INCLUDED |


## Original checker: numeric_parts/results_a.md

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC006 p9 eFigure4 9–12h; p12 eFigure6a≥150mL and6b≥150mL; pp26–32 integer category bars | Integer percentage pairs68/33,28/73,83/18 total101; category sums vary around100. Independent half-unit sums contain100 and feasible category integer-count bounds contain their N. Remaining gap0; no count discrepancy reproduced. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC006 p17 eFigure11 NCCT≥150mL | AdjustedRR0.12(.01–1.05) differs markedly from crude(1/17)/(1/22)=1.2941. The supplied analysis specifies adjusted modified-Poisson modeling; comparing this to a crude ratio does not reproduce a label/measure inconsistency. No reverse-direction favorable claim is made in this row's numerical label. | MODEL_VERSUS_CRUDE |
| DOC006 pp13–19 forests versus p8 flow | Forest/distribution totals168/168 differ from explicitly labeled as-treated170/166. Main article Methods p4 specifies randomized allocation for treatment effects across strata and as-treated for within-arm imaging associations. The forest strata are randomized treatment effects, so unlike analysis definitions explain the apparent mismatch. Plan/report population comparison belongs to the cross-source lane. | CONTEXT_RESOLVES |


## Original checker: numeric_parts/results_b.md

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-006 p.35,eTable1 coronary artery disease |39/170=22.94% versus23.2%;25/166=15.06% versus15.6%. Conservative half-count/denominator intervals give the latter[14.7147,15.4079]% versus[15.55,15.65]%;gap0.1421/15.6=0.0091. The apparent discrepancy does not exceed0.05; unknown row-specific denominators need not be inferred. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-006 p.36,eTable1 tenecteplase |4(12.5%) and1(3.7%) are treatment-subset cells;parent thrombolytic counts33/28 give12.12%/3.57%, within input/output half-unit intervals. Denominator is not the entire arm. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-006 p.36,eTable1 IV thrombolytics/general anesthesia |28/166=16.87% versus17.0%;100/170=58.82% versus59.5%. Half-unit intervals overlap or leave relative gap below0.05;no qualifying count/percentage inconsistency. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-006 pp.33–34,eFigure20 |Some seven-category percentage rows total99%,101% or102%; seven independently rounded integer percentages allow these sums. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-006 pp.38,41,eTables2/5 |EVT65/168 versus66/170 and MM31/168 versus30/166 for ambulation;tables explicitly distinguish intention-to-treat from as-treated. | CONTEXT_RESOLVES |
| DOC-006 pp.33–34,43–44,eFigure20/eTable7 |Figure core mismatch arm totals168/168;table7 arm totals170/166. Printed as-treated table7 title explains the different population. | CONTEXT_RESOLVES |
| DOC-006 pp.43–50,eTables7–10 adjusted measures |Several aRR/aRD/aGenOR point directions or magnitudes differ from crude ratios/differences of printed outcome frequencies (for example eTable8 EVT discordant1 mRS0–2 crude ratio(21/76)/(10/75)=2.07 versusaRR0.51). Models/adjustment and conditional within-arm comparisons are explicit;no display claims these estimates are crude. | MODEL_VERSUS_CRUDE |
| DOC-006 pp.45–48,eTables8/9 concordant denominator/adverse counts |EVT denominator75 versus74,MM82 versus83;adverse counts42 versus41 and59 versus60. All count intervals overlap or residual differences are below0.05. These nearby cells do not remove the larger discordant2 pattern. | ROUNDING_OR_DISPLAY_PRECISION |

Limitations: baseline row-specific denominators and eTable7 treatment/last-column headings are not printed; adjusted estimates and median summaries cannot be regenerated from aggregate data alone. All supplied cells assessed;no scientific coverage gap. Source-rendered images and direct native PDF extraction independently agree for every finding input. Statistical specialists own estimate/test method reconciliation, including comparison of aRR versus aRD significance for the same contrast;those comparisons have not been screened out here.


## Original checker: cross_source_parts/plans.md

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| Analysis SAPp.3 versus mainp.3/results eFigure1p.5 | SAP says ratio of core and hypoperfused volumes; the accompanying≥1.8/≥1.2 definitions and explicit report numerator/denominator identify the intended ratio immediately. No printed numeric value changes. | TERMINOLOGY_OR_WORDING |
| Protocolp.51 | Two written descriptions of the discordant direction use rearranged favorable/unfavorable CT/CTP names; the two profiles and neighboring aim/diagram identify them. | TERMINOLOGY_OR_WORDING |
| Parent protocolpp.17,42 versus earlier eligibility/visit accounts | Explicit additions of >100-mL patients and365-day follow-up account for these prospective changes. | CONTEXT_RESOLVES |
| Protocol planned interims200/380; parent SAPp.12; mainp.4 | Requested300-patient review and stopping are disclosed in both later plan and report; no printed interim statistic is supplied to reproduce a boundary-control conflict solely from timing. | CONDITIONAL_OR_UNREPORTED |
| Parent protocol/SAP versus current analysis SAP/report | Parent multiple imputation and WMW versus exploratory no-imputation/PIM could appear different; these describe different analysis tasks, and the specific imaging SAP expressly specifies the latter. | NOT_REPRODUCED |
| Current SAP all enrolled; mainp.4 and flowp.8 |352 randomized versus336 analyzed is fully explained by4 missing90-day outcomes and12 imaging exclusions, with no imputation planned. | CONTEXT_RESOLVES |
| Mainp.1/6/7 and analysis SAPp.4; eFigure14p.20 | Foregrounded ASPECTS association omits core, whereas planned model includes core; report explicitly presents the fully adjusted model as well and distinguishes its estimate/significance. No planned model is absent. | CONTEXT_RESOLVES |
| Protocolp.22/51/71 versus current discordance definitions | Original second aim15% superiority contrast uses50-mL imaging profiles; current exploratory SAP prospectively defines70-mL profiles and different contrasts. Treating them as the same missing primary analysis would misalign the tasks. | NOT_REPRODUCED |
| Parent SAPp.23 versus mainp.4/6/11 and current SAPp.7 | Broad total-lesion/core-overestimation concepts were prespecified; the current SAP distinguishes the concept from specific post hoc analyses. Apart from composite-primary status in F-XS-002, a concept's existence does not establish that every later implementation was prespecified. | CONTEXT_RESOLVES |
| Protocolp.49 versus trial SAPp.11 simulation scenario4 | Fixed-design power cell21.2% versus51.2% differs between prospective operating-characteristic tables. It is not an observed outcome, sample-size/power input, primary decision boundary or a changed planned sample size; therefore this plan-internal historical simulation comparison is peripheral. | PERIPHERAL_COMPARISON |
| Protocolp.78 versus trial SAPp.37 | Minimization weights and category detail differ across dated plans; current report agrees with later factor list including physician ASPECTS. No supplied statement attributes a particular conflicting weight to the reported primary estimate or decision rule. | PERIPHERAL_COMPARISON |
| Current SAP mismatch50/100-mL strata versus report continuous-mismatch displays | Extra threshold displays are not found among matched current results, but their omission alone does not establish replacement of a primary/key-secondary outcome analysis; the planned continuous association and two profile analyses are reported. | CONDITIONAL_OR_UNREPORTED |


## Original checker: cross_source_parts/reports.md

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| Mainp.4 follow-up MRI8/336;p.9 MRI204; supplementp.51 eTable11 N101+24+79=204 | The additional support population corroborates the reproduced main follow-up MRI population discrepancy already emitted as F-NUM-001. Preservep.51 as an affected/corroborating location for that issue rather than creating another finding. | DUPLICATE_OF_INCLUDED |
| Mainp.5 Table1 versus supplementpp.35–36 eTable1 | Apparent differences in baseline copies,including median/IQRs,sex/race/referral/occlusion counts and time summaries,are baseline descriptive comparisons; explicitly168/168ITT versus170/166as-treated populations also distinguish them. No primary/key result or analysis-population size is changed. | PERIPHERAL_COMPARISON |
| Mainp.7 Table2/p.9 Table3 versus supplementpp.13–15forests/p.38 eTable2/p.32–34 distributions | Apparent34/170 versus34/168,66/170 versus65/168 and mismatch contributor differences arise between received-treatment and randomized groups. These are not matched arm-specific population definitions. Two MM-to-EVT crossovers explain the net arm/outcome transfers in the overall copies. | NOT_REPRODUCED |
| Mainp.9 infarct/growth narrative versus supplementpp.38/51 eTables2/11 | Follow-up infarct IQRs170(123–268)vs170(123–266),168(110–253)vs168(109–254),and MMgrowth95(56–125)vs95(56–135)are post hoc imaging-summary copies. The125/135 endpoint minimumgap9/135=.0667 exceedsprecision,but this exploratory outcome comparison does not change a primary/key outcome or analysis population. The difference is not an estimate-CI or test conflict. | PERIPHERAL_COMPARISON |
| MainTable2/3 footnotes pp.7/9 versus model methods p.4 and ratio labels in supplement | aRR expanded as absolute risk reduction versus evident modified-Poisson ratio,ratio null1 and explicit higher-rate-ratio footnote. The intended ratio quantity is identifiable immediately; no numeric computation as an alternative effect measure is established. | TERMINOLOGY_OR_WORDING |
| Mainp.8 mismatch-presence narrative/Table3p.9 versus eFigure17 continuous curves | Higher crude favorable-outcome proportions with binary mismatch presence do not establish that adjusted continuous mismatch-volume slopes must increase; they differ in contrast and modeling. The independent direction conflict with the explicit continuous narrative is retained in F-XS-102. | MODEL_VERSUS_CRUDE |
| Supplement eFigures7–13 pp.13–19 versus eFigure20 pp.26–34 | Apparent one-percentage-point differences when rounded mRS category percentages are cumulated,including independent rounding totals99–101%,reconcile after each segment’shalf-unit allowance; no separate distribution mismatch beyondF-XS-101/F-XS-104 was reproduced. | ROUNDING_OR_DISPLAY_PRECISION |


## Original checker: statistical_parts/pass1_main.md

## Excluded observations

Each row is one apparent observation that was considered and self-screened out; reconciled checks are retained in S records. These rows receive no finding IDs. Missing definitions are named rather than replaced by conventional assumptions. Pass2 must revisit them against always-register categories.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 pp.6–7 and9, aRR expansion/footnote |The expansion “absolute risk reduction” appears alongside positive ratio-scale estimates, multiplicative intervals, and a footnote explicitly saying aRR>1 means a higher rate ratio. The intended ratio reading is identifiable at once; no printed numerical value changes. The footnote’s “with endovascular thrombectomy” is read with the explicit within-arm column/reference structure, rather than as a separate treatment contrast.|TERMINOLOGY_OR_WORDING|
| REPORT DOC-001 p.9 Table3, mismatch counts versus adjusted effects |Examples: definitionB EVT independence crude ratio(28/111)/(6/59)=2.480...,versus printed adjustedaRR1.20; definitionB EVT dependence/death crude risks46/111 vs31/59 decrease while adjustedaRR1.18>1. The model explicitly adjusts age,NIHSS,time andcore. These are modeled associations, not printed crude estimates; crude recomputation does not test their stated method.|MODEL_VERSUS_CRUDE|
| REPORT DOC-001 p.7 Table2, core/ambulation interactionP=.25;S029/S037 |Both arm-specificaRR point estimates print0.91,withCIs[0.87,0.95] and[0.85,0.98]. Diagnostic only: assuming independent identical-estimand log-Wald arm estimates, SEs≈0.02244/0.03631 giveP≈1; allowing all inputs half-unit precision yields maximum diagnostic absolute z≈0.283 and minimumP≈.777. The source does not establish that its treatment×core interaction coefficient equals the difference of these separate-arm model coefficients, nor name the contrast/df/covariance/common-nuisance fit. No independent-Wald method reproducing the same display is established. Thus the diagnostic is conditional,not a reproduced interval-versus-own-test conflict.|CONDITIONAL_OR_UNREPORTED|
| REPORT DOC-001 p.9 Table3, definitionB dependence/death interactionP>.99;S047/S054 |Diagnostic only: independent log-Wald comparison ofaRR1.18[0.82,1.70] andaRR1.05[0.79,1.38] givesSEs≈.18599/.14230,z≈.49844,P≈.618. The printedP>.99 is an interaction,whose RR-versus-RD scale,contrast,model coefficient mapping andcovariance/testdf are not printed. This calculation does not reproduce the stated interaction method for other rows,so cannot establish a source conflict.|CONDITIONAL_OR_UNREPORTED|
| REPORT DOC-001 p.9 Table3, definitionA MM independence;S041 |Printed adjustedaRR1.01 andadjustedaRD−0.001 have opposite tiny point directions. Main methods state modifiedPoisson for secondary outcomes and predictedmargins,without specifying howaRD is generated or whetherboth estimands derive from one common pair ofadjustedprobabilities. Bothintervals include null. A direction contradiction follows only if that unreported mapping is assumed; no printed number is reconstructed or changed.|CONDITIONAL_OR_UNREPORTED|
| REPORT DOC-001 pp.3–4 PIM covariate-direction prose;pp.1,6–7 |PIM prose refers to higher values of the covariate of interest while ASPECTS associations are per1-point decrease. Immediate scale labels in narrative/Table2 define the covariate as a decrease and core as an increase; direction is readable without reversing any printedestimate. No proposed alternative analysis.|CONTEXT_RESOLVES|

The diagnostic independence calculations are arithmetic aids, not reconstructions of the reported fitted interaction. For ratio rows with no numeric effect P, log-symmetry is not used to infer a missing SE/test or to create a finding.


## Original checker: statistical_parts/pass1_forest_a.md

## Excluded observations

Only apparent issues actually considered and not emitted are listed; reconciled containment,direction,count and interaction checks are not exclusions. Neither row below covers the all-zero finite-estimate pattern in F-ST1-101.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-006 p14/eFigure8,no≥1.2/10mL mismatch row (S1029),with the same comparison limitation across nonzero forest rowspp13-15 | Diagnostic crudeRR from2/8EVT vs4/21MM is1.3125,whereas the forest RR is5.99(0.76-47.33). The source's adjusted/model-based regression supplies the contrast; this is not a stated crude estimate. Covariates and robust covariance are absent. The difference alone does not establish that the reported estimator fails to reproduce,so it is not routeA category4. | MODEL_VERSUS_CRUDE |
| REPORT DOC-006 pp13-15/eFigures7-9,especially p13core≥150/no≥1.2/10mL mismatch andp14core≥150asterisks (S1012,S1013,S1028); p13core150/mismatch≥1.2 andp14core150unprinted interaction slots (S1053,S1054,S1060); remaining finite interaction testsS1049-S1069except these missing slots | Asterisks and three missing interaction values have no estimate/test or estimation explanation; interaction-statistic/degrees-of-freedom/covariance definitions are absent. No contradictory finite value or subgroup inferential-decision claim is supplied at these locations. These omissions are recorded rather than supplied by convention. Planned-analysis reporting status is a separately assigned design scope,not inferred from these blank cells alone. | CONDITIONAL_OR_UNREPORTED |


## Original checker: statistical_parts/pass1_forest_b.md

## Excluded observations

Only apparent issues decided against emission are listed; reconciling checks are retained in the relationship inventory.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-006 p17,eFigure11,NCCT≥150mL,S2026 | Printed adjusted RR.12(.01-1.05) contrasts with a crude ratio from1/17 versus1/22, equal to22/17=1.2941. The stated modified Poisson model adjusts prognostic variables, so crude direction and magnitude do not reproduce its adjusted estimate. The missing fitted coefficients cannot establish a conflicting adjusted calculation. | MODEL_VERSUS_CRUDE |
| REPORT DOC-006 p17,eFigure11,NCCT≥150mL,S2026 | Log-center diagnostic sqrt(.01×1.05)=.10247 differs from printed.12. Allowing endpoint half-unit intervals [.005,.015] and[1.045,1.055] gives a geometric-center interval [.072284,.125797], overlapping the point's[.115,.125]. Display-precision gap0; relative discrepancy0. This diagnostic does not assume the CI method as final authority. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-006 p16,eFigure10,NCCT150 interaction,S2069 with effect rowsS2009-S2010 | A diagnostic independent-normal reconstruction from GenOR1.70(1.33-2.19) and2.21(1.16-4.19) yields SE of log-difference≈.35146,z≈.74650,two-sided P≈.455, whereas printed interactionP=.8886. This diagnostic assumes independent subgroup estimates and a common log-Wald test; the source supplies neither that covariance nor the interaction coefficient/test statistic. It is not a method shown to reproduce the other interaction rows of this display. | CONDITIONAL_OR_UNREPORTED |

The final exclusion does not remove any interval-versus-own-P conflict: the printed P is explicitly an interaction test, not the P of either subgroup's treatment effect. Subgroup effect CIs do not establish the fitted interaction covariance or test. No Route A category4 observation has been reproduced by a method reproducing the other rows.


## Second-pass main reconsideration: rows 1–40

## Excluded observations: all 75 prior rows independently reconsidered

This table is a row-by-row reconsideration of the complete prior catalogue, in its lossless order. Each retained exclusion has exactly one scope reason code. The two duplicate rows name their included C IDs. The qualifying reconsideration has no screened-out code: it is forwarded as F-ST2-601 for independent screening. Rows are locators, not additional finding IDs. Exact values and printed confidence/test roles were reread using direct selected-page text, source-page images, and complete current exact-source recheck facts. Source-defined methods and precision were checked without adopting earlier exclusion conclusions.

| Location | Observation: pass 2 result, source check and applicable rule | Reason code |
|---|---|---|
| Prior row 01: REPORT DOC-001 p. 5 Table 1, coronary artery disease; N033 | Retain exclusion. Input percentages 23.5/15.4 and counts39/25 reread. Even exact-count residual ratios .010/.0305 are at most .05; half-units reduce the gap. Category3 requires greater than .05. | ROUNDING_OR_DISPLAY_PRECISION |
| Prior row 02: REPORT DOC-001 p. 5 Table 1, tenecteplase, thrombolytics and anesthesia; N053, N054 | Retain exclusion. Subset33/28 identifies tenecteplase denominators;4/33 and1/28 remain within .05 after output half-units. Anesthesia/thrombolytic gaps likewise below threshold, not substituted count slips. | ROUNDING_OR_DISPLAY_PRECISION |
| Prior row 03: REPORT DOC-001 p. 7 Figure 2, all four arm rows; N071, N072, N073, N074 | Retain exclusion. Four main Figure2 totals101/101/101/99 lie in [97.5,104.5] or corresponding segment sum ranges containing100. Independent total rounding does not screen the separate C006 category allocation. | ROUNDING_OR_DISPLAY_PRECISION |
| Prior row 04: REPORT DOC-001 pp. 6, 7 and9, aRR abbreviation expansion; N080, N083, N086, N090, N092, N094, N098, N100, N102 | Retain exclusion. Ratio footnote and modified-Poisson method explicitly identify aRR despite its expanded name. No competing numerical difference estimate is established; category2 numeric slip is absent. | TERMINOLOGY_OR_WORDING |
| Prior row 05: REPORT DOC-001 p. 9 Table3; N088, N090, N092, N094, N096, N098, N100, N102 | Retain exclusion. Source Table3 explicitly adjusted within-arm associations. Crude mismatch ratios test a different estimand and cannot supply category4 reconstruction. | MODEL_VERSUS_CRUDE |
| Prior row 06: REPORT DOC-001 p. 11 discussion “two-thirds” versus p. 9 204(61%); N113 | Retain exclusion. The unresolved8-versus204 follow-up population is already C001. Approximate two-thirds prose is corroboration of that issue rather than a new numeric pattern. | DUPLICATE_OF_INCLUDED |
| Prior row 07: DOC006 p9 eFigure4 9–12h; p12 eFigure6a≥150mL and6b≥150mL; pp26–32 integer category bars | Retain exclusion. Pairs68/33,28/73,83/18 have [100,102]% sums containing100. Category3 count logic reconciles under independent half-units. | ROUNDING_OR_DISPLAY_PRECISION |
| Prior row 08: DOC006 p17 eFigure11 NCCT≥150mL | Retain exclusion. Exact eFigure11 .12(.01–1.05),1/17,1/22 reread. Source states adjusted analysis; crude22/17 does not reconstruct modified-Poisson coefficients. | MODEL_VERSUS_CRUDE |
| Prior row 09: DOC006 pp13–19 forests versus p8 flow | Retain exclusion. The randomized-versus-received distinction is explicitly mainp4;168/168 versus170/166 differs by two crossovers. Planned allocation issue separately already C002. | CONTEXT_RESOLVES |
| Prior row 10: DOC-006 p.35,eTable1 coronary artery disease | Retain exclusion. Direct baseline25/166 versus15.6% yields allowable[14.7147,15.4079]% versus[15.55,15.65]%;minimum relative gap .0091≤.05.39/170 comparison also within rule. | ROUNDING_OR_DISPLAY_PRECISION |
| Prior row 11: DOC-006 p.36,eTable1 tenecteplase | Retain exclusion. Four and one tenecteplase events are nested among33/28 thrombolytic recipients. Whole-arm denominator is not the printed quantity; no category3 excess. | ROUNDING_OR_DISPLAY_PRECISION |
| Prior row 12: DOC-006 p.36,eTable1 IV thrombolytics/general anesthesia | Retain exclusion. Exact100/170 versus59.5% and28/166 versus17.0% leave relative discrepancies below.05 after half-units; no category3 issue. | ROUNDING_OR_DISPLAY_PRECISION |
| Prior row 13: DOC-006 pp.33–34,eFigure20 | Retain exclusion. Seven rounded segments allow total102 within [98.5,105.5]%; 99/101 similarly contain100. None is an interval-versus-test conflict. | ROUNDING_OR_DISPLAY_PRECISION |
| Prior row 14: DOC-006 pp.38,41,eTables2/5 | Retain exclusion. Source eTable2 is ITT while eTable5 denominators170/166 are as-treated;65/168 and66/170 are nonmatched arm allocations explained by disclosed crossovers. | CONTEXT_RESOLVES |
| Prior row 15: DOC-006 pp.33–34,43–44,eFigure20/eTable7 | Retain exclusion. Figure distributions label randomized arms while eTable7 says as-treated;168/168 versus170/166 does not reproduce a same-population count contradiction. | CONTEXT_RESOLVES |
| Prior row 16: DOC-006 pp.43–50,eTables7–10 adjusted measures | Retain exclusion. All eTables7–10 explicitly adjusted or modeled. Crude2.072 versus adjusted.51 lacks stated crude estimand identity; no source-established method reconstruction. | MODEL_VERSUS_CRUDE |
| Prior row 17: DOC-006 pp.45–48,eTables8/9 concordant denominator/adverse counts | Retain exclusion. Intervals for75/74 and82/83 counts touch;42/41 and59/60 touch or differ relatively by≤.05. C018 independently preserves materially greater disjoint-count excesses. | ROUNDING_OR_DISPLAY_PRECISION |
| Prior row 18: Analysis SAPp.3 versus mainp.3/results eFigure1p.5 | Retain exclusion. SAP ratio language prints no reverse equation. Report explicitly hypoperfused/core and thresholds>1 resolve wording without changing a numerical value. | TERMINOLOGY_OR_WORDING |
| Prior row 19: Protocolp.51 | Retain exclusion. Protocolp51 names both discordant profiles;neighboring profile definition identifies comparison despite reordered words. No reported count/effect is mapped to another profile by this phrase. | TERMINOLOGY_OR_WORDING |
| Prior row 20: Parent protocolpp.17,42 versus earlier eligibility/visit accounts | Retain exclusion. Protocolp17 explicitly says amendment includes>100mL and later follow-up calendar includes365days; disclosed change resolves historical prospective chronology. | CONTEXT_RESOLVES |
| Prior row 21: Protocol planned interims200/380; parent SAPp.12; mainp.4 | Recorded C014; prior conditional rationale superseded. The actual300-boundary rejection despite200/380 and unchanged-design language is already C014. Retain this source comparison as duplicate, not as a missing-statistic basis to suppress it. | DUPLICATE_OF_INCLUDED |
| Prior row 22: Parent protocol/SAP versus current analysis SAP/report | Retain exclusion. Parent main-trial missing-data/WMW rules and later imaging-analysis no-imputation/PIM rules specify distinct tasks. Same current analysis is not compared to its governing different method. | NOT_REPRODUCED |
| Prior row 23: Current SAP all enrolled; mainp.4 and flowp.8 | Retain exclusion. 352−12−4=336, randomized168/168; four unavailable90day outcomes are disclosed. No unexplained analysis-population count remains; C002 concerns arm attribution, not this subtraction. | CONTEXT_RESOLVES |
| Prior row 24: Mainp.1/6/7 and analysis SAPp.4; eFigure14p.20 | Retain exclusion. Mainp6 explicitly prints core-adjustedASPECTS.96(.86–1.07) alongside unadjusted-for-core.91(.82–1.00); planned full adjustment is supplied and clearly distinguished. | CONTEXT_RESOLVES |
| Prior row 25: Protocolp.22/51/71 versus current discordance definitions | Retain exclusion. Original50mL second-aim profile and current70mL exploratory profile explicitly differ in task/threshold. No matched primary report value is established by equating them. | NOT_REPRODUCED |
| Prior row 26: Parent SAPp.23 versus mainp.4/6/11 and current SAPp.7 | Retain exclusion. ParentSAPp23 broad union/largest-core concept does not classify every later implementation. C003 already captures the explicit primary/prespecified versus post-hoc comparison. | CONTEXT_RESOLVES |
| Prior row 27: Protocolp.49 versus trial SAPp.11 simulation scenario4 | Retain exclusion. Exact21.2 versus51.2 power outputs confirmed;gap29.90/21.2=1.4104. They are simulation outputs, not inputs or an executed boundary; F-ST1-503 screening already records this peripheral observation. | PERIPHERAL_COMPARISON |
| Prior row 28: Protocolp.78 versus trial SAPp.37 | Retain exclusion. Protocolp78 and laterSAPp37 weights are versioned randomization particulars. No stated executed primary inference or analysis N changes with this weight comparison; prospective source does not reproduce an operating discrepancy. | PERIPHERAL_COMPARISON |
| Prior row 29: Current SAP mismatch50/100-mL strata versus report continuous-mismatch displays | Recorded C016; prior conditional rationale superseded. SpecificSAPp6 invokes§5.2 primarymRS analyses at mismatch50/100mL. Their bounded REPORT absence is already C016. Earlier exclusion's non-key-secondary premise does not apply; duplicate category5 now recorded. | DUPLICATE_OF_INCLUDED |
| Prior row 30: Mainp.4 follow-up MRI8/336;p.9 MRI204; supplementp.51 eTable11 N101+24+79=204 | Retain exclusion. Main8/336 versus204 plus supplement101+24+79 is exactly C001. Corroboration is retained without a further conflicting relationship or finding. | DUPLICATE_OF_INCLUDED |
| Prior row 31: Mainp.5 Table1 versus supplementpp.35–36 eTable1 | Retain exclusion. Baseline main168/168 and supplement170/166 are descriptive copies and different allocations. No within-display numeric gap beyond.05 or primary population uncertainty is raised by these copies. | PERIPHERAL_COMPARISON |
| Prior row 32: Mainp.7 Table2/p.9 Table3 versus supplementpp.13–15forests/p.38 eTable2/p.32–34 distributions | Retain exclusion. Main Table2/3 received-treatment and forests randomized arms explicitly differ; two disclosed crossovers explain overall favorable-event transfers. Do not equate distinct allocations. | NOT_REPRODUCED |
| Prior row 33: Mainp.9 infarct/growth narrative versus supplementpp.38/51 eTables2/11 | Retain exclusion. Main IQR125 versus supplement135 gap9/135=.0667 reproduced, but these are exploratory infarct-growth descriptive quantiles, not treatment-effect CIs or primary/key outcome; category1 absent. | PERIPHERAL_COMPARISON |
| Prior row 34: MainTable2/3 footnotes pp.7/9 versus model methods p.4 and ratio labels in supplement | Retain exclusion. Printed numerical ratio/null1 and higher-rate-ratio footnote establish the aRR quantity immediately; abbreviation expansion alone is wording, not category2 value reversal. | TERMINOLOGY_OR_WORDING |
| Prior row 35: Mainp.8 mismatch-presence narrative/Table3p.9 versus eFigure17 continuous curves | Retain exclusion. Binary mismatch presence adjusted/crude associations and continuous-volume slopes have different contrasts. C007 retains the actual same-continuous-direction discrepancy; categorical-to-continuous inference is not forced. | MODEL_VERSUS_CRUDE |
| Prior row 36: Supplement eFigures7–13 pp.13–19 versus eFigure20 pp.26–34 | Retain exclusion. Cumulated rounded-category intervals overlap corresponding rounded percentage copies for ordinary rows. C006 andC018 retain the distinct threshold/attribution discrepancies; rounding does not supersede them. | ROUNDING_OR_DISPLAY_PRECISION |
| Prior row 37: REPORT DOC-001 pp.6–7 and9, aRR expansion/footnote | Retain exclusion. Main ratio footnote/modifiedPoisson contract identifies measure. Within-arm headings determine comparison despite treatment phrasing; no alternate numeric measure calculation is printed. | TERMINOLOGY_OR_WORDING |
| Prior row 38: REPORT DOC-001 p.9 Table3, mismatch counts versus adjusted effects | Retain exclusion. Crude28/111 divided6/59=2.480 differs from explicitly adjusted1.20; adverse crude reduction can differ from adjusted1.18. Count inputs are not fitted covariate-adjusted coefficients. | MODEL_VERSUS_CRUDE |
| Prior row 39: REPORT DOC-001 p.7 Table2, core/ambulation interactionP=.25;S029/S037 | Retain exclusion. Independent-log diagnostic tested across all eight Table2 rows, not presumed. Multiple other binary interactions do not reproduce (.757 vs.58;.551 vs.73;.275 vs.37); common-nuisance mapping absent. No category1 own-test or established category4 method. | CONDITIONAL_OR_UNREPORTED |
| Prior row 40: REPORT DOC-001 p.9 Table3, definitionB dependence/death interactionP>.99;S047/S054 | Retain exclusion. Table3 binary diagnostics .356/.712/.914/.741/.618 disagree systematically with .47/.65/.75/.60/>.99. Near-matching ordinalPIM rows do not validate a binary interaction method or RR/RD scale. | CONDITIONAL_OR_UNREPORTED |


## Second-pass checker: forest_a

## Excluded observations

Both own pass-1 exclusions were independently revisited. No row belongs to an always-register category on the supplied evidence. Existing included patterns are cross-referenced above and are not re-emitted or counted as new exclusions. Reconciled checks are retained in the per-S table rather than this table.

| Location | Observation | Reason code |
|---|---|---|
| REPORT p.14 eFigure8 mismatch1.2/10 absent, S1029; adjusted nonzero forest rows pp.13–15 | CrudeRR=(2/8)/(4/21)=1.3125 differs from adjusted5.99(.76–47.33). Covariate-specific model output cannot be reconstructed from the marginal event counts. A crude method is not established as reproducing the adjusted rows elsewhere in this display; routeA4 therefore does not follow from this diagnostic comparison. | MODEL_VERSUS_CRUDE |
| REPORT pp.13–15, asterisks S1012/S1013/S1028 and absent interaction slots S1053/S1054/S1060; unsupplied interaction coefficients/statistics/covariance | Blank or asterisk cells provide no contradictory finite estimate, interval, own-test P or inferential decision. These are secondary binary analyses, not a source-established unreported primary/key-secondary analysis; no routeA5 category is inferred. Interaction covariance/test definitions are missing without a printed incompatibility. | CONDITIONAL_OR_UNREPORTED |


## Second-pass checker: forest_b

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT [DOC-006 p17,eFigure11,NCCT≥150mL,S2026](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=17) | RR.12(.01–1.05) differs from crude (1/17)/(1/22)=1.2941, but the source explicitly reports robust adjusted modified-Poisson risks. Raw counts do not reproduce this adjusted estimate; no same-display unadjusted method is established. | MODEL_VERSUS_CRUDE |
| REPORT [DOC-006 p17,eFigure11,NCCT≥150mL,S2026](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=17) | Central geometric-center diagnostic .10247 versus printed.12 yields overlapping half-unit-compatible intervals [.072284,.125797] and [.115,.125]; gap0 and relative discrepancy0. No printed own-effect P/test conflicts. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [DOC-006 p16,eFigure10,NCCT150 interaction,S2069](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=16) | Independent-normal subgroup-CI approximation gives P≈.455372 versus printed.8886, but its assumed coefficient independence/log-Wald interaction mapping is absent and it does not reproduce the other interaction rows coherently (all 32 diagnostics above). This is not an established category4 reproducing method, nor a row interval-versus-own-P comparison. | CONDITIONAL_OR_UNREPORTED |



