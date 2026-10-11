
# Exclusions from .ai_paper_validation/review_1_6_2/checkers/numeric_consistency.md

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p. 5 Table 1, coronary artery disease; N033 | Header n168 gives 39/168 = 23.214% vs 23.5% and 25/168 = 14.881% vs 15.4%. Even treating counts as exact, gaps after the printed ±0.05% interval are 0.236/23.5 = 0.0100 and 0.469/15.4 = 0.0305; allowing count/denominator half-units only reduces them. Both are below 0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p. 5 Table 1, tenecteplase, thrombolytics and anesthesia; N053, N054 | Tenecteplase is nested in thrombolytic recipients, not all168 participants: 4/33 = 12.121% vs12.5% and 1/28 = 3.571% vs3.7%; residual relative gaps are below0.05 even with exact counts. Anesthesia100/168 =59.524% vs59.9%, thrombolytics28/168 =16.667% vs16.8%, also within threshold. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p. 7 Figure 2, all four arm rows; N071, N072, N073, N074 | Whole-percentage segment totals are101,101,101,99. Independent half-unit intervals contain100; category colors, rather than text extraction order, establish missing-width categories. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 pp. 6, 7 and9, aRR abbreviation expansion; N080, N083, N086, N090, N092, N094, N098, N100, N102 | “Absolute risk reduction” expansion differs from the ratio quantity evident from modified Poisson methods, null1, ratio-valued intervals and footnotes stating higher rate ratio. The ratio interpretation is immediately identifiable; no conflict with an evidently computed alternate numeric measure was reproduced. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001 p. 9 Table3; N088, N090, N092, N094, N096, N098, N100, N102 | Crude within-arm mismatch/no-mismatch outcome ratios and median comparisons differ from some adjusted estimates; the table explicitly adjusts age, NIHSS, time and core. Direction reversals relative to crude counts do not establish a numeric conflict. | MODEL_VERSUS_CRUDE |
| REPORT DOC-001 p. 11 discussion “two-thirds” versus p. 9 204(61%); N113 | Approximate prose fraction is not an additional independent population discrepancy; the materially different p. 4 count is retained in F-NUM-001. | DUPLICATE_OF_INCLUDED |

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC006 p9 eFigure4 9–12h; p12 eFigure6a≥150mL and6b≥150mL; pp26–32 integer category bars | Integer percentage pairs68/33,28/73,83/18 total101; category sums vary around100. Independent half-unit sums contain100 and feasible category integer-count bounds contain their N. Remaining gap0; no count discrepancy reproduced. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC006 p17 eFigure11 NCCT≥150mL | AdjustedRR0.12(.01–1.05) differs markedly from crude(1/17)/(1/22)=1.2941. The supplied analysis specifies adjusted modified-Poisson modeling; comparing this to a crude ratio does not reproduce a label/measure inconsistency. No reverse-direction favorable claim is made in this row's numerical label. | MODEL_VERSUS_CRUDE |
| DOC006 pp13–19 forests versus p8 flow | Forest/distribution totals168/168 differ from explicitly labeled as-treated170/166. Main article Methods p4 specifies randomized allocation for treatment effects across strata and as-treated for within-arm imaging associations. The forest strata are randomized treatment effects, so unlike analysis definitions explain the apparent mismatch. Plan/report population comparison belongs to the cross-source lane. | CONTEXT_RESOLVES |

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

# Exclusions from .ai_paper_validation/review_1_6_2/checkers/cross_source_consistency.md

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


# Exclusions from .ai_paper_validation/review_1_6_2/checkers/statistical_pass_1.md

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

## Excluded observations

Only apparent issues actually considered and not emitted are listed; reconciled containment,direction,count and interaction checks are not exclusions. Neither row below covers the all-zero finite-estimate pattern in F-ST1-101.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-006 p14/eFigure8,no≥1.2/10mL mismatch row (S1029),with the same comparison limitation across nonzero forest rowspp13-15 | Diagnostic crudeRR from2/8EVT vs4/21MM is1.3125,whereas the forest RR is5.99(0.76-47.33). The source's adjusted/model-based regression supplies the contrast; this is not a stated crude estimate. Covariates and robust covariance are absent. The difference alone does not establish that the reported estimator fails to reproduce,so it is not routeA category4. | MODEL_VERSUS_CRUDE |
| REPORT DOC-006 pp13-15/eFigures7-9,especially p13core≥150/no≥1.2/10mL mismatch andp14core≥150asterisks (S1012,S1013,S1028); p13core150/mismatch≥1.2 andp14core150unprinted interaction slots (S1053,S1054,S1060); remaining finite interaction testsS1049-S1069except these missing slots | Asterisks and three missing interaction values have no estimate/test or estimation explanation; interaction-statistic/degrees-of-freedom/covariance definitions are absent. No contradictory finite value or subgroup inferential-decision claim is supplied at these locations. These omissions are recorded rather than supplied by convention. Planned-analysis reporting status is a separately assigned design scope,not inferred from these blank cells alone. | CONDITIONAL_OR_UNREPORTED |

## Excluded observations

Only apparent issues decided against emission are listed; reconciling checks are retained in the relationship inventory.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-006 p17,eFigure11,NCCT≥150mL,S2026 | Printed adjusted RR.12(.01-1.05) contrasts with a crude ratio from1/17 versus1/22, equal to22/17=1.2941. The stated modified Poisson model adjusts prognostic variables, so crude direction and magnitude do not reproduce its adjusted estimate. The missing fitted coefficients cannot establish a conflicting adjusted calculation. | MODEL_VERSUS_CRUDE |
| REPORT DOC-006 p17,eFigure11,NCCT≥150mL,S2026 | Log-center diagnostic sqrt(.01×1.05)=.10247 differs from printed.12. Allowing endpoint half-unit intervals [.005,.015] and[1.045,1.055] gives a geometric-center interval [.072284,.125797], overlapping the point's[.115,.125]. Display-precision gap0; relative discrepancy0. This diagnostic does not assume the CI method as final authority. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-006 p16,eFigure10,NCCT150 interaction,S2069 with effect rowsS2009-S2010 | A diagnostic independent-normal reconstruction from GenOR1.70(1.33-2.19) and2.21(1.16-4.19) yields SE of log-difference≈.35146,z≈.74650,two-sided P≈.455, whereas printed interactionP=.8886. This diagnostic assumes independent subgroup estimates and a common log-Wald test; the source supplies neither that covariance nor the interaction coefficient/test statistic. It is not a method shown to reproduce the other interaction rows of this display. | CONDITIONAL_OR_UNREPORTED |

The final exclusion does not remove any interval-versus-own-P conflict: the printed P is explicitly an interaction test, not the P of either subgroup's treatment effect. Subgroup effect CIs do not establish the fitted interaction covariance or test. No Route A category4 observation has been reproduced by a method reproducing the other rows.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| PLAN DOC005p3 mismatch-ratio wording versus REPORT mainp3/DOC006p5 | SAP says ratio 'of' core and hypoperfused volumes, but does not print core/hypoperfused equation. Field context, threshold>1 and report examples immediately identify conventional hypoperfused/core; no explicit numerical reverse equation was reproduced. | TERMINOLOGY_OR_WORDING |
| PLAN DOC005p3 ADC notation versus REPORT mainp2 | ADC unit/exponent typography differs; intended imaging threshold is identifiable from immediate imaging context and consistent threshold620, with no changed extracted result established. | NOTATION_OR_TYPOGRAPHY |
| PLAN DOC005p5,mRS5-6 descriptive bullet | Descriptive bullet says independent ambulation under the complete-dependence/death heading; neighboring model bullet explicitly gives5-6. Endpoint identity is immediately recoverable and no numeric outcome is misattributed. | TERMINOLOGY_OR_WORDING |
| REPORT DOC006pp10-12,eFigures5/6 | Trend algorithm, bin denominators, fitted coefficient and test statistic are absent. Comparing P to an unweighted bar slope or assumed trend test would depend on unsupported method inputs; no interval/test conflict is printed. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC006pp20-25,eFigures14-19 | Individual panel binary-model/logistic calibration choice, reference covariate distribution and coefficients are not stated. SAP permits logistic calibration fallback; absence alone does not contradict plotted values. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC006pp26-32,eFigure20a-aa versus PLAN DOC005p4 | Separate descriptive5/6 bars appear despite merged modeled ordinal outcome. Descriptive distributions do not establish that5-to6 shifts contributed to PIM/g-computation treatment success. | CONTEXT_RESOLVES |
| REPORT DOC006pp24-25,contour time axes | Time units are omitted from axes, while mainp10 explicitly describes increments in minutes and figures clearly name each time origin. The omission alone does not change a printed quantity or fitted result. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC006p9 68+33%;p12 28+73%,83+18%;eFigure20 rounded category totals | Integer-percentage totals101% are compatible with individual±.5-point rounding intervals, which include a100% total. These are not independent inferential tests. | ROUNDING_OR_DISPLAY_PRECISION |

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-006 eTable5 p.41, mRS0–2 composite and both mRS0–3 volume rows; S4056,S4059,S4062 | Subtracting the separately printed arm-specific log slopes with independent-slope SEs would give diagnostic P≈.327 rather than .82 for mRS0–2 composite; identical printed mRS0–3 slopes give central diagnostic P≈1 rather than .32/.82. The source describes interaction models separately from within-arm associations and does not identify their coefficients/covariance with those separate fits. The reconstruction is not a method demonstrated to reproduce the whole display, so it cannot establish a printed same-analysis conflict or routeA4. No interaction P is treated as either arm's slope-effect P. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-006 eTable7 pp.43–44, all binary within-arm mismatch cells | Several crude mismatch/no-mismatch ratios and differences differ from the printed aRR/aRD. The table expressly adjusts age, NIHSS, timing and core volume; the supplied report does not state these estimates are crude. Model-based quantities need not equal crude count comparisons. | MODEL_VERSUS_CRUDE |
| REPORT DOC-006 eTable6 p.42 footnote versus main REPORT statistical methods p.4 | Main primary ordinal associations use PIM, while eTable6 specifies ordinal logistic regression for model-comparison criteria. This explicitly identified additional model-comparison analysis does not represent a mislabeled PIM estimate. | CONTEXT_RESOLVES |
| REPORT DOC-006 eTable7 pp.43–44, numeric column headings and last-column values | Local arm/last-column headings are absent, but denominator totals170/166 and supplied main/SAP interaction descriptions identify the arm association and heterogeneity structure. There is no reproduced misattribution to a different outcome/population or numerical conflict from the heading omission. | CONTEXT_RESOLVES |
| REPORT DOC-006 eTable7 p.43 EVT mRS0–2 aRD; S4084 | Negative displayed zero −0.000 can suggest an apparent sign disagreement with ratio1.02. It is a zero at the printed precision, no significant direction is asserted, and the difference scale is not specified as a fixed transformation of the ratio-scale coefficient. The signed-zero notation alone does not change the extracted printed zero or null reading. | NOTATION_OR_TYPOGRAPHY |

## Excluded observations

Only apparent issues not emitted are listed. Checks that reconcile are documented in the relationship inventory.

| Location | Observation | Reason code |
|---|---|---|
| DOC-006 eTable8 pp45–46;S5001–S5024 | Several adjusted profile RR/RD directions differ from crude ratios/differences, notably EVT mRS0–2 D1 crude(21/76)/(10/75)=2.072 vsadjustedRR.51. Source labels adjusted; no crude-effect claim. | MODEL_VERSUS_CRUDE |
| DOC-006 eTables8–10 pp45–50;S5025–S5062 | Individual effect intervals excluding1 beside nonsignificant last-column P initially resemble null-test conflicts; heading explicitly says interaction, a different contrast. No matched interval/P contradiction reproduced. | NOT_REPRODUCED |
| DOC-006 eTable12 p52;S5063–S5066 | P<.001 cannot be reconstructed from medians/IQRs alone; no contradictory matched effectCI/statistic or named ranks supplied. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 p14;S5111 | HistoricalOR2.56(2.50–8.47),P=.04 is asymmetric under a diagnostic log-Wald convention; point containment/significance agree. CI method/test not stated, and no same-display method reproduced. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 p78;S5084 | Target-mismatch minimization weight blank; later SAPp37 provides2. No executed allocation discrepancy supplied. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 pp55–56;S5086 | Absolute/relative scale of MMmortality increase>20% unspecified without an executed triggering comparison. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 p45;S5069 | GeneralizedCMH “stratified” adjustment names continuous age/NIHSS/time/core, but stratum construction missing; no executed numeric implementation contradicts text. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 p46/DOC-004p11;S5072 | Diagnostic normalN363.579 vsfixed376; half-unit input ranges approximately349–379 overlap376±.5; exact WMW/simulation variance not claimed. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 p46/DOC-004pp10–11;S5071 | Diagnostic half-tie untie-normal standardizedeffect.324760 vsprinted.34 differs4.48% before rounding; named standardized-effect implementation absent. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 pp62–63;S5091,S5092 | Beta(.4,.6) posterior atN60 reaches>.95 with31events(.9644096), printed threshold32. Integer intervals[30.5,31.5]and[31.5,32.5]touch; gap0. Even exact integer discrepancy1/32=.03125≤.05. Same pattern consolidated. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-004 p16;S5096 | ARD's probability description differs from explicit2(WMW−.5) transformation; source formula immediately identifies net effect and no executedARDvalue is supplied. | TERMINOLOGY_OR_WORDING |
| DOC-003 p51;S5067 | First second-aim comparison repeats unfavorableCT/favorableCTP in two word orders; opposite profiles are identified by p22, second p51 paragraph and p71diagram. | TERMINOLOGY_OR_WORDING |
| DOC-003 p48/DOC-004p10;S5075 | Earlier final overall-failure subgroup-rescue branch not restated in later SAP; no final analysis executed because300stop disclosed, and no numerical final result is in conflict. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 p46/DOC-004pp11–12;S5072,S5094 | Fixedalpha.05 vsone-sided.025 andfamily-wise.05 do not by themselves establish inconsistent calibration; sidedness is specified at distinct stages. | CONTEXT_RESOLVES |
| DOC-003 p16;S5118–S5120 | Narrative says safety outcomes “doubled” although displayed crude increases are3.60,3.43,4.49fold; this contextual qualitative increase is historical wording, and exact values remain explicit. Separate P-versus-significance issue emittedF-ST1-506. | TERMINOLOGY_OR_WORDING |

