# Complete excluded-observation audit handoff B

Mechanical lossless partition of all current checker excluded/reconsideration rows. No scientific decision is changed. Part A owns 47 original checker rows plus 45 second-pass rows; part B owns 28 original rows plus 66 second-pass rows. Their union contains all 75 initial and all 111 second-pass rows exactly once. The second-pass main row73 forwards F-ST2-601 for screening and is a qualifying reconsideration rather than a retained exclusion. Full original checker artifacts remain available.

## Original checker: statistical_parts/pass1_remaining_a.md

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


## Original checker: statistical_parts/pass1_tables_a.md

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-006 eTable5 p.41, mRS0–2 composite and both mRS0–3 volume rows; S4056,S4059,S4062 | Subtracting the separately printed arm-specific log slopes with independent-slope SEs would give diagnostic P≈.327 rather than .82 for mRS0–2 composite; identical printed mRS0–3 slopes give central diagnostic P≈1 rather than .32/.82. The source describes interaction models separately from within-arm associations and does not identify their coefficients/covariance with those separate fits. The reconstruction is not a method demonstrated to reproduce the whole display, so it cannot establish a printed same-analysis conflict or routeA4. No interaction P is treated as either arm's slope-effect P. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-006 eTable7 pp.43–44, all binary within-arm mismatch cells | Several crude mismatch/no-mismatch ratios and differences differ from the printed aRR/aRD. The table expressly adjusts age, NIHSS, timing and core volume; the supplied report does not state these estimates are crude. Model-based quantities need not equal crude count comparisons. | MODEL_VERSUS_CRUDE |
| REPORT DOC-006 eTable6 p.42 footnote versus main REPORT statistical methods p.4 | Main primary ordinal associations use PIM, while eTable6 specifies ordinal logistic regression for model-comparison criteria. This explicitly identified additional model-comparison analysis does not represent a mislabeled PIM estimate. | CONTEXT_RESOLVES |
| REPORT DOC-006 eTable7 pp.43–44, numeric column headings and last-column values | Local arm/last-column headings are absent, but denominator totals170/166 and supplied main/SAP interaction descriptions identify the arm association and heterogeneity structure. There is no reproduced misattribution to a different outcome/population or numerical conflict from the heading omission. | CONTEXT_RESOLVES |
| REPORT DOC-006 eTable7 p.43 EVT mRS0–2 aRD; S4084 | Negative displayed zero −0.000 can suggest an apparent sign disagreement with ratio1.02. It is a zero at the printed precision, no significant direction is asserted, and the difference scale is not specified as a fixed transformation of the ratio-scale coefficient. The signed-zero notation alone does not change the extracted printed zero or null reading. | NOTATION_OR_TYPOGRAPHY |


## Original checker: statistical_parts/pass1_tables_b_plan.md

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


## Second-pass main reconsideration: rows 41–75

## Excluded observations: all 75 prior rows independently reconsidered

This table is a row-by-row reconsideration of the complete prior catalogue, in its lossless order. Each retained exclusion has exactly one scope reason code. The two duplicate rows name their included C IDs. The qualifying reconsideration has no screened-out code: it is forwarded as F-ST2-601 for independent screening. Rows are locators, not additional finding IDs. Exact values and printed confidence/test roles were reread using direct selected-page text, source-page images, and complete current exact-source recheck facts. Source-defined methods and precision were checked without adopting earlier exclusion conclusions.

| Location | Observation: pass 2 result, source check and applicable rule | Reason code |
|---|---|---|
| Prior row 41: REPORT DOC-001 p.9 Table3, definitionA MM independence;S041 | Retain exclusion. Ratio1.01 andRD−.001 have opposite tiny signs, but no supplied common-risk transformation identifies same adjusted estimand. Both include null; no own-effect P/test or reproducing multirow method. | CONDITIONAL_OR_UNREPORTED |
| Prior row 42: REPORT DOC-001 pp.3–4 PIM covariate-direction prose;pp.1,6–7 | Retain exclusion. ASPECTS is explicitly per-point decrease in same Table2/narrative; coded covariate scale resolves higher-value PIM prose without reversing an extracted estimate. | CONTEXT_RESOLVES |
| Prior row 43: REPORT DOC-006 p14/eFigure8,no≥1.2/10mL mismatch row (S1029),with the same comparison limitation across nonzero forest rowspp13-15 | Retain exclusion. eFigure8 adjusted5.99(.76–47.33) versus crude1.3125 is not a printed crude estimate. Source modified-Poisson covariates/model define separate quantity; category4 not reproduced. | MODEL_VERSUS_CRUDE |
| Prior row 44: REPORT DOC-006 pp13-15/eFigures7-9,especially p13core≥150/no≥1.2/10mL mismatch andp14core≥150asterisks (S1012,S1013,S1028); p13core150/mismatch≥1.2 andp14core150unprinted interaction slots (S1053,S1054,S1060); remaining finite interaction testsS1049-S1069except these missing slots | Retain exclusion. Three blank interaction slots/asterisks are visibly absent. No printed finite estimate/test or decision conflict exists there; finite all-zero rows are separately C004, never included in this exclusion. | CONDITIONAL_OR_UNREPORTED |
| Prior row 45: REPORT DOC-006 p17,eFigure11,NCCT≥150mL,S2026 | Retain exclusion. ExactNCCT≥150 RR.12 from adjusted method versus1/17÷1/22 is a model/crude contrast, not source-declared crude RR; printed direction label itself agrees. | MODEL_VERSUS_CRUDE |
| Prior row 46: REPORT DOC-006 p17,eFigure11,NCCT≥150mL,S2026 | Retain exclusion. Endpoint half-unit geometric centers span [.072284,.125797] and intersect point [.115,.125];minimum gap0. This is a labeled symmetry diagnostic, not assumed confidence construction. | ROUNDING_OR_DISPLAY_PRECISION |
| Prior row 47: REPORT DOC-006 p16,eFigure10,NCCT150 interaction,S2069 with effect rowsS2009-S2010 | Retain exclusion. Independent-log eFigure10 subgroup comparisons do not reproduce the full display: NCCT70 diagnostic.273 versus.2684 is close, but NCCT100 .01148 versus.0164 and NCCT150 .455 versus.8886 differ. Neither covariance nor interaction contrast is supplied; numerical near coincidence does not define a common reproducing method. | CONDITIONAL_OR_UNREPORTED |
| Prior row 48: PLAN DOC005p3 mismatch-ratio wording versus REPORT mainp3/DOC006p5 | Retain exclusion. SAP ratio is verbal without core/hypoperfused equation; report and mismatch≥1.2/1.8 definitions determine direction. No digit/sign replacement inferred from wording. | TERMINOLOGY_OR_WORDING |
| Prior row 49: PLAN DOC005p3 ADC notation versus REPORT mainp2 | Retain exclusion. ADC threshold620 consistent; malformed exponent/unit alone is identifiable locally. No supplied computed count/result changes with this typography. | NOTATION_OR_TYPOGRAPHY |
| Prior row 50: PLAN DOC005p5,mRS5-6 descriptive bullet | Retain exclusion. SAP complete-dependence heading and next model bullet expresslymRS5–6; isolated independent-ambulation descriptive phrase has no numerical result assigned to a different endpoint. | TERMINOLOGY_OR_WORDING |
| Prior row 51: REPORT DOC006pp10-12,eFigures5/6 | Retain exclusion. Trend figures provide percentages/P, but no binN, trend statistic or coefficient; bar direction agrees. An unweighted assumed test cannot become category4 without reconstructing other actual rows. | CONDITIONAL_OR_UNREPORTED |
| Prior row 52: REPORT DOC006pp20-25,eFigures14-19 | Retain exclusion. SAP explicitly permits logistic calibration fallback for marginal plots. Lack of per-panel calibration details alone yields no contradictory printed fitted number; C008 captures actual core-identity conflict. | CONDITIONAL_OR_UNREPORTED |
| Prior row 53: REPORT DOC006pp26-32,eFigure20a-aa versus PLAN DOC005p4 | Retain exclusion. Descriptive bars may show scores5/6 separately although primary PIM merges them; separation does not establish modeled5→6 success. Primary versus full-ordinal g-computation is expressly distinguished. | CONTEXT_RESOLVES |
| Prior row 54: REPORT DOC006pp24-25,contour time axes | Retain exclusion. Mainp10 states minutes and10minute effect scale; contour time origins explicitly differ. Missing axis-unit typography itself changes no plotted quantity; C009 retains predictor-definition comparison. | NOTATION_OR_TYPOGRAPHY |
| Prior row 55: REPORT DOC006p9 68+33%;p12 28+73%,83+18%;eFigure20 rounded category totals | Retain exclusion. Integer pairs101% have ±1 combined half-unit total including100. Rounding category sums is not category1 inference and does not remove C018 disjoint exact-count excesses. | ROUNDING_OR_DISPLAY_PRECISION |
| Prior row 56: REPORT DOC-006 eTable5 p.41, mRS0–2 composite and both mRS0–3 volume rows; S4056,S4059,S4062 | Retain exclusion. Direct eTable5 slopes/intervals reread. Independent-log diagnostics vary across rows and cannot reproduce a common interaction fit; one near coincidence cannot specify nuisance/covariance. No same-effect interval/P pair. | CONDITIONAL_OR_UNREPORTED |
| Prior row 57: REPORT DOC-006 eTable7 pp.43–44, all binary within-arm mismatch cells | Retain exclusion. eTable7 explicitly adjusts age,NIHSS,time/core; crude risk ratios/differences do not test its fitted adjusted measures. Direct current-source cells override any locator transcription. | MODEL_VERSUS_CRUDE |
| Prior row 58: REPORT DOC-006 eTable6 p.42 footnote versus main REPORT statistical methods p.4 | Retain exclusion. eTable6 explicitly says ordinal logistic for evaluation parameters, not PIM for the primary effect. Named supplementary model-comparison analysis is internally readable. | CONTEXT_RESOLVES |
| Prior row 59: REPORT DOC-006 eTable7 pp.43–44, numeric column headings and last-column values | Retain exclusion. Main/SAP treatment-association structure and totals170/166 identify eTable7 arms;last-column role is heterogeneity in context. No conflicting value attribution comes solely from absent headings. | CONTEXT_RESOLVES |
| Prior row 60: REPORT DOC-006 eTable7 p.43 EVT mRS0–2 aRD; S4084 | Retain exclusion. Direct eTable7−.000 rounds to printed zero: underlying interval[−.0005,.0005] crosses0. Ratio1.02 and signed displayed zero do not reproduce an established common-risk direction conflict. | NOTATION_OR_TYPOGRAPHY |
| Prior row 61: DOC-006 eTable8 pp45–46;S5001–S5024 | Retain exclusion. eTable8 RR/RD adjusted within-arm contrasts, not crude outcome ratios. Source no explicit shared risk-pair identity; neither crude2.072 nor RR/RD apparent direction alone reconstructs fitted quantities. | MODEL_VERSUS_CRUDE |
| Prior row 62: DOC-006 eTables8–10 pp45–50;S5025–S5062 | Retain exclusion. eTables8–10 last-column heading explicitlyinteraction. Individual ratioCI excludes1 beside its P is a different contrast, so category1 own-interval/test mismatch is not reproduced. | NOT_REPRODUCED |
| Prior row 63: DOC-006 eTable12 p52;S5063–S5066 | Retain exclusion. eTable12 P<.001 with medians/IQRs has no effectCI, rank statistic, ranks or variance. Quantile overlap is not a contradiction with the printed test. | CONDITIONAL_OR_UNREPORTED |
| Prior row 64: DOC-003 p14;S5111 | Retain exclusion. HistoricalOR2.56(2.50–8.47),P.04 contains point and excludes1. Log symmetry is not stated; other historical studies are separate paragraphs/analyses, not a reproducing same-display CI method. | CONDITIONAL_OR_UNREPORTED |
| Prior row 65: DOC-003 p78;S5084 | Retain exclusion. Minimization weight blank atprotocolp78 and2 atlaterSAPp37 names a missing earlier detail; no executed numeric decision/allocation conflict is printed. | CONDITIONAL_OR_UNREPORTED |
| Prior row 66: DOC-003 pp55–56;S5086 | Retain exclusion. MM mortality>20% scale not defined and no implemented trigger comparison supplied. Missing absolute/relative definition alone creates no reproduced stopping conclusion. | CONDITIONAL_OR_UNREPORTED |
| Prior row 67: DOC-003 p45;S5069 | Retain exclusion. Protocol continuous covariates with GeneralizedCMH lack stratum construction; no executed adjustedCMH result is supplied for testing. The reported imaging PIM method is separately defined, not silently equated. | CONDITIONAL_OR_UNREPORTED |
| Prior row 68: DOC-003 p46/DOC-004p11;S5072 | Retain exclusion. DiagnosticN range349–379 from allowed inputs overlaps fixed376±.5; no same-display method or stated exact simulation reconstruction establishes a residual> .05. | ROUNDING_OR_DISPLAY_PRECISION |
| Prior row 69: DOC-003 p46/DOC-004pp10–11;S5071 | Retain exclusion. Diagnostic standardized.324760 versus.34 is4.48% even before allowing half-units. Missing exact implementation plus precision threshold precludes category4 reproduction. | ROUNDING_OR_DISPLAY_PRECISION |
| Prior row 70: DOC-003 pp62–63;S5091,S5092 | Retain exclusion. N60 mortality tables32 versus diagnostic31 intervals touch at31.5;exact1/32=.03125≤.05. Rule is numerical threshold without an executed interval/P conflict, so category1 exception does not apply. | ROUNDING_OR_DISPLAY_PRECISION |
| Prior row 71: DOC-004 p16;S5096 | Retain exclusion. SAP explicitly2(WMW−.5) defines net effect although prose says probability; no executedARD cell or sign/result is printed under the alternate prose meaning. | TERMINOLOGY_OR_WORDING |
| Prior row 72: DOC-003 p51;S5067 | Retain exclusion. Protocolp51 second aim and profile definitions identify opposing groups in neighboring context; first rearranged wording does not assign a numeric result to another group. | TERMINOLOGY_OR_WORDING |
| Prior row 73: DOC-003 p48/DOC-004p10;S5075 | QUALIFYING_RECONSIDERATION; F-ST2-601 handoff. Direct protocolp48 explicitly selects/tests an optimal subgroup after final overall failure; directly viewed laterSAPp10 instead declares EVT not superior. This planned decision-rule difference can qualify RouteB without an executed final statistic; versioned revision is an alternative, not an operative mapping. Cross-reference plan-method reviewer's F-ST2-601; no duplicate finding ID emitted here. | — |
| Prior row 74: DOC-003 p46/DOC-004pp11–12;S5072,S5094 | Retain exclusion. Protocol alpha5% andSAP one-sided2.5% are compatible two-sided/one-sided nominal representations;family-wise.05 atstop lacks a suppliedZ/operative mapping, separately C014. Do not infer an executed alpha calculation. | CONTEXT_RESOLVES |
| Prior row 75: DOC-003 p16;S5118–S5120 | Retain exclusion. Safety increases3.60/3.43/4.49-fold all exceed a doubling; qualitative wording need not mean exact2.00. No printed numeral2 or replaced quantitative estimate; C012 preserves explicit P/significance conflict. | TERMINOLOGY_OR_WORDING |


## Second-pass checker: remaining_a

## Excluded observations

These are the eight apparent observations from the shard's pass-1 exclusion table, independently reread against always-register categories and display precision. No additional finding is concealed in them. Reconciled routine checks appear in the relationship table above rather than as excluded observations.

| Location | Observation | Reason code |
|---|---|---|
| PLAN DOC005p3 vs REPORT mainp3/results p5 | Ratio described as ratio 'of' core and hypoperfused volumes lacks an explicit reversed equation. Threshold>1 and immediate illustrative131/94=1.4 identify the intended quantity without a competing printed division result. No category2 numerical/direction slip reproduced. | TERMINOLOGY_OR_WORDING |
| PLAN DOC005p3 vs REPORT mainp2 | ADC unit/exponent typography is recoverable at numeric threshold620; no changed result or explicit conflicting calculated value established. | NOTATION_OR_TYPOGRAPHY |
| PLAN DOC005p5 mRS5–6 descriptive bullet | Independent-ambulation wording is beside explicit complete-dependence/death heading and5–6 model definition. No printed outcome result receives a competing definition in this bullet. | TERMINOLOGY_OR_WORDING |
| REPORT DOC006pp10–12 eFigures5/6 | No trend algorithm, bin denominators, coefficient, interval, SE, or statistic is supplied. A guessed unweighted trend is not a source-supported reproducing method for other rows, and there is no own CI/test conflict. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC006pp20–25 eFigures14–19 | Exact binary plotting model, reference covariates and coefficients are absent. The SAP expressly permits logistic calibration, and the curves contain no numeric result contradicting a source-defined fitting algorithm. C007/C008 handle the distinct observed direction/covariate conflicts already included. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC006pp26–32 vs PLAN DOC005p4 | Seven descriptive mRS categories do not assert that the merged ordinal comparison counted5→6 or6→5 treatment successes; main methods explicitly merge5/6. | CONTEXT_RESOLVES |
| REPORT DOC006pp24–25 axes | Time unit omitted beside a clearly named time origin; mainp10 supplies minutes explicitly. No competing value or different unit is printed. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC006p9 68+33; p12 28+73/83+18; eFigure20 totals | Individual integer-percentage±.5 intervals allow100 for101 totals. In two-category examples the interval is[100,102]; seven-category totals are more permissive. Gap0, relative discrepancy0, outside category1 because these are descriptive percentages rather than paired interval/tests. | ROUNDING_OR_DISPLAY_PRECISION |


## Second-pass checker: tables_a

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT eTable5 physicalp41; interaction S4047,S4050,S4053,S4056,S4059,S4062,S4065,S4068 | Independent-slope diagnostic contrasts sometimes differ from printed interaction Ps, especially identical printed ambulation slopes. Supplied separate arm fits are not identified as coefficients of the interaction model; exact combined-model nuisance/variance mapping is absent, and no source-established reproducing method is demonstrated. No arm CI is equated with its interaction P. | CONDITIONAL_OR_UNREPORTED |
| REPORT eTable7 physicalpp43–44; binary mismatch cells | Crude no-mismatch/mismatch ratios or differences can differ from adjusted RR/RD. The footnote expressly adjusts age,NIHSS,timing,core volume; no crude effect is claimed. | MODEL_VERSUS_CRUDE |
| REPORT eTable6 physicalp42; REPORT mainp4 | Ordinal logistic model-comparison criteria and primary PIM coefficients use distinct expressly named analyses. The separate additional criteria analysis identifies which numbers it produces. | CONTEXT_RESOLVES |
| REPORT eTable7 physicalpp43–44 | Arm and last-column headings absent locally, but as-treated170/166 denominator partitions, main/SAP interaction context and table structure resolve arm association/heterogeneity. No conflicting result attribution is reproduced. | CONTEXT_RESOLVES |
| REPORT eTable7 physicalp43; S4084 | Negative displayed zero−.000 besideRR1.02 supplies no changed extracted zero, significant reversal or fixed RR/RD transformation. Both intervals contain their own null. | NOTATION_OR_TYPOGRAPHY |
| REPORT eTable7 physicalp43; S4095,S4096; already screened F-ST1-401 | RR1.29(.93–1.79) contains1 whileRD.168(.011–.325) excludes0. Distinct adjusted scales/confidence constructions have no supplied common identity/own-effect test; a contradictory same-analysis inference would depend on an unstated mapping. Initial independent screening already records this observation; it is not re-emitted. | CONDITIONAL_OR_UNREPORTED |
| REPORT eTable7 physicalp44; S4104,S4106,S4107,S4108,S4109,S4111,S4112,S4113,S4114 | An apparent reviewer inventory/source alignment concern was reread against direct source and current source render. All saved-inventory/source values were identical, so no source-value transcription correction or reporting inconsistency is reproduced. | NOT_REPRODUCED |


## Second-pass checker: tables_b

## Excluded observations

These rows consolidate apparent issues considered and not newly emitted; reconciled routine checks remain in the per-S records.

| Location | Observation | Reason code |
|---|---|---|
| REPORT eTable8 pp45–46, S5001–S5024 | Adjusted effects differ from crude profile comparisons, notably EVT D1 independence adjustedRR.51 versus crude(21/76)/(10/75)=2.072. Source labels adjustment; no source-defined crude reproduction of other adjusted rows is established. | MODEL_VERSUS_CRUDE |
| REPORT eTables8–10 pp45–50, S5025–S5030,S5041–S5046,S5057–S5062 | Apparent effect-CI versus last-column-P conflicts pair individual treatment/profile effects with explicitly different interaction tests. Rereading headings does not reproduce an own-analysis interval/test conflict. | NOT_REPRODUCED |
| REPORT eTable8 pp45–46, S5009–S5012,S5015–S5016,S5019–S5020 | Opposing RR/RD point directions and differing null-inclusion readings require a common fitted-risk/CI mapping absent from the source; no own-effect P, shared estimand construction or same-display reproducing method establishes that mapping. | CONDITIONAL_OR_UNREPORTED |
| REPORT eTable12 p52, S5063–S5066 | Reconstructing P<.001 from medians/IQRs alone requires absent ranks/test output; distribution IQRs do not supply a matched effect CI or contradiction. | CONDITIONAL_OR_UNREPORTED |
| REPORT eTables8–10 pp45–50, concordant/discordant D2 favorable and adverse counts; S5003–S5004,S5009–S5010,S5015–S5016,S5021–S5024,S5033,S5040,S5049,S5056 and their associated interaction/context records | Disjoint MM outcome counts and competing favorable-event arm attribution reproduce the exact pattern already screened INCLUDE and registered as C018; all affected locations remain in that candidate. | DUPLICATE_OF_INCLUDED |

The three pertinent pass1_tables_b_plan exclusion rows were reread against exact source and the Route A catalogue. MODEL_VERSUS_CRUDE remains applicable; no mislabeled crude-effect claim or reproducing method was found. The apparent interaction/individual interval conflict remains NOT_REPRODUCED. The eTable12 numerical-P reconstruction remains conditional because no contradictory test/CI/statistic is supplied. The additional RR/RD review above does not infer the absent covariance/estimand mapping.


## Second-pass checker: plan_methods

## Excluded observations

Only apparent observations not emitted are listed. Reconciled checks are in the per-S table. Existing included patterns are referenced above without duplicate exclusions or findings.

| Location | Observation | Reason code |
|---|---|---|
| PLAN protocol p.14; S5111 | Historical OR2.56(2.50–8.47),P.04 is asymmetric under a diagnostic log-Wald convention; estimate containment and significance agree. The source gives no common historical-study CI model, and no method is shown to reproduce other rows of this display. | CONDITIONAL_OR_UNREPORTED |
| PLAN protocol p.78 versus trial SAP p.37; S5084 | Protocol mismatch weight is blank; later plan supplies2. No observed allocation contradicts a stated weight or permits a source-defined reproduction of allocation. | CONDITIONAL_OR_UNREPORTED |
| PLAN protocol pp.55–56; S5086 | The >20% mortality-increase scale is unnamed without a supplied actual threshold application or contradicting pair of calculations. | CONDITIONAL_OR_UNREPORTED |
| PLAN protocol p.45; S5069 | Generalized-CMH continuous-covariate stratum construction is unreported; no specific output contradicts its supplied description. | CONDITIONAL_OR_UNREPORTED |
| PLAN protocol p.46/trial SAP p.11; S5072 | Diagnostic normal sample size363.57865 versus WMW/ASSISTant fixed376 is not a uniquely established exact algorithm; first-pass half-unit input bounds349–379 overlap376±.5. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN protocol p.46/trial SAP pp.10–11; S5071 | Diagnostic untied half-tie standardized effect.32475953 versus.34 differs4.48% even before input precision; method's tie variance not specified. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN protocol pp.62–63; S5091/S5092 | Stated Beta(.4,.6) rule reaches>.95 at31/60 but printed inclusive trigger begins32. Half-unit intervals touch and exact integer relative difference1/32=.03125≤.05; this is not an interval-versus-ownP category1 comparison. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN trial SAP p.16; S5096 | ARD's probability wording versus explicit2(WMW−.5) is immediately resolved as a net contrast by the printed transformation; no executed ARD is supplied in conflict. | TERMINOLOGY_OR_WORDING |
| PLAN protocol p.51; S5067 | The first second-aim comparison repeats the same discordant imaging profile in two word orders; immediate second paragraph and p.22 identify the opposite intended profiles without changing a printed numeric result. | TERMINOLOGY_OR_WORDING |
| PLAN protocol p.46/trial SAP pp.11–12; S5072/S5094 | Unspecified protocol fixed alpha.05, explicit one-sided.025 and family-wise.05 alone do not identify differing operational calibration; no unsupported sidedness mapping assumed. | CONTEXT_RESOLVES |
| PLAN protocol p.16; S5118–S5120 | Historical safety increases described qualitatively as doubled correspond to displayed fold increases3.60/3.43/4.49; exact counts and percentages remain visible. The independent significance/test issue is C012, not this wording. | TERMINOLOGY_OR_WORDING |



