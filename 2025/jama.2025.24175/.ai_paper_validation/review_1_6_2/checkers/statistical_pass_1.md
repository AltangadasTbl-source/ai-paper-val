# Statistical consistency review — pass 1

Runtime agent: /root/statistical_pass_1. Fresh named statistical specialist, gpt-6.1-sol, high reasoning effort. All 111 stable inferential/method relationships are complete. All 73 support printed inferential/count-test rows were explicitly checked. There are 15 self-screened findings and 23 excluded apparent observations. No candidate IDs are assigned. Sources and retained assets were preserved; no external evidence or old scientific conclusions were read.

## Exact completed relationship scope

S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111

Every ID above has PASS_1_COMPLETE in statistics/relationship_inventory.md, with printed values/specification and a distinct check record. All 167 source units were mapped before checking. The 111-relationship inventory and relevant input text fit the assigned bounds. Historical PROVIDE is context only; administrative DOC-004/005 units contain no inferential relationships.

## Source-grounded calculation rules

Fisher calculations use probability-order two-sided hypergeometric summation with the printed integer patient counts; because integer-count half-unit ranges contain unique integers, no fractional contingency table is invented. Display precision for continuous estimates/limits and crude OR/RD arithmetic allows the full half-unit input/output ranges. Log interval centers and normal sample-size formulas are diagnostic unless the same construction reproduces companion rows in the same display. No unreported sidedness, degrees of freedom, covariance, variance estimator, estimand, model or population is inferred. Significance uses the supplied two-sided.05 rule and95%CIs. No requirement for a different analysis or adjustment is introduced.

## Self-screened findings

### F-ST1-001 — APACHE-treatment odds ratio lies below its interval

- **Relationships:** S085
- **Compared locations and document roles:** REPORT [DOC-003 p53, eFigure9 panel B, APACHEII≥25×Precision Immunotherapy](../../../joi250116supp2_prod_1771885794.27755.pdf#page=53).
- **Printed values/statements:** OR 0.11; 95% CI 0.36–3.42; P=.86, for 90-day mortality interaction.
- **Rule and calculation:** Containment requires lower≤estimate≤upper. 0.11<0.36. Half-unit ranges are estimate[0.105,0.115], lower[0.355,0.365], upper[3.415,3.425]; minimum gap 0.240, relative gap 0.240/0.11=2.182. Route A 1 does not admit display-precision screening. CI includes 1/P>.05 while the point itself indicates a far smaller odds ratio.
- **Focus area:** B
- **Proposed review domain:** statistical_results
- **Proposed relationship type / All relationships:** S_W / S_W
- **Qualifying route:** Route A, category 1
- **Affected result or extracted value:** 90-day APACHEII≥25 treatment interaction OR/95% CI.
- **Why context does not resolve it:** Point-estimate containment is an always-register category; recovering a possible intended value cannot remove the printed reading.
- **Alternative interpretations and missing definitions:** The point could be a substituted digit/decimal, or the limits could describe another coefficient. The supplied page does not identify which. No model or covariance is inferred.
- **Exact human question:** Which odds ratio and 95% confidence limits belong to the APACHEII≥25×precision-immunotherapy row for 90-day mortality?
### F-ST1-002 — Subgroup P values do not reproduce under the test reproducing companion rows

- **Relationships:** S054, S056, S058, S064, S070
- **Compared locations and document roles:** REPORT [DOC-003 p51 eFigure7 panel A](../../../joi250116supp2_prod_1771885794.27755.pdf#page=51), [p52 eFigure8 panel A](../../../joi250116supp2_prod_1771885794.27755.pdf#page=52), [p53 eFigure9 panel A](../../../joi250116supp2_prod_1771885794.27755.pdf#page=53); REPORT [DOC-001 p6 Statistical Analyses](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6) states Fisher exact comparisons; same-display companion rows establish the reproducing method.
- **Printed values/statements:** PI versus placebo: primary APACHE≥25 12/38 vs 8/40, P.439; primary CCI≥5 20/54 vs 7/76, P.003; primary SOFA≥10 25/67 vs 11/68, P.035; day 28 SOFA≥10 35/67 vs 48/68, P.045; day 90 SOFA≥10 49/67 vs 57/68, P.209.
- **Rule and calculation:** For fixed marginal integer counts, two-sided probability-order Fisher exact test sums hypergeometric probabilities no larger than the observed table. Results respectively .303200218, .000158910, .006531327, .034400792, .146989715. Integer count half-unit intervals contain only the printed integers; P half-unit intervals [.4385,.4395],[.0025,.0035],[.0345,.0355],[.0445,.0455],[.2085,.2095]. Minimum gaps .135299782,.002341090,.027968673,.010099208,.061510285; relative gaps .3082,.7804,.7991,.2244,.2943. Every gap exceeds .05. The method reproduces 13 of 18 rows within the display rule, including the low-severity companion rows on all three pages. eFigure 7 CCI low .474644→.475, APACHE low .00217654→.002, SOFA low .082691→.083; eFigure 8 CCI high .0196437→.020, CCI low .231037→.231, APACHE low .471708→.472, SOFA low .720788→.721; eFigure 9 APACHE rows 1.0→>.99, CCI low .0446232→.045, SOFA low .231337→.231. Small remaining differences eFigure 8 APACHE high .483109 versus.489 and eFigure 9 CCI high .125050 versus.123 have relative precision gaps≤.05.
- **Focus area:** B
- **Proposed review domain:** statistical_results
- **Proposed relationship type / All relationships:** S_W / S_W
- **Qualifying route:** Route A, category 4
- **Affected result or extracted value:** Primary and mortality subgroup P values in the five named rows.
- **Why context does not resolve it:** Same-display printed results that a reproducing method does not reproduce are always-register; a missing row-specific test definition cannot screen the pattern out.
- **Alternative interpretations and missing definitions:** A different test or population could have produced these five P values; that definition is not printed. This finding does not assume interaction-panel P values are crude Fisher tests, and does not infer exact numerical forest limits from pixels.
- **Exact human question:** Which tests and contingency counts produced the five named panel A P values, and why do the same-display companion rows reproduce using the displayed counts and two-sided Fisher exact test?
### F-ST1-003 — Repeated APACHE coefficient does not reconcile with same-display interval construction

- **Relationships:** S072, S078
- **Compared locations and document roles:** REPORT [DOC-003 p51 eFigure7 panel B](../../../joi250116supp2_prod_1771885794.27755.pdf#page=51) and [p52 eFigure8 panel B](../../../joi250116supp2_prod_1771885794.27755.pdf#page=52), APACHEII≥25 main-effect row.
- **Printed values/statements:** Both pages print OR 0.47,95% CI 0.30–1.62, P.70.
- **Rule and calculation:** The same-display log-symmetric ratio-interval reconstruction uses OR=sqrt(lower×upper). It gives sqrt(.30×1.62)=.697137, not.47. Half-unit limit ranges [.295,.305] and[1.615,1.625] yield reconstructed OR[.690235,.704006]; printed OR range[.465,.475], gap≥.215235; relative gap.215235/.47=.457947. This construction reproduces the other five rows on each page within the .05 rule: geometric centers 1.85046,.218404,5.93456,.566833,3.08799 against 1.85,.22,5.79,.56,3.08. A full-width log-Wald P diagnostic is approximately .08 using the printed point and interval, rather than.70; that P diagnostic is not used as an independently established test.
- **Focus area:** B
- **Proposed review domain:** statistical_results
- **Proposed relationship type / All relationships:** S_W / S_W
- **Qualifying route:** Route A, category 4
- **Affected result or extracted value:** APACHEII≥25 coefficient OR and 95% CI in primary-response and 28-day-mortality displays.
- **Why context does not resolve it:** Same-display interval reconstruction fails beyond display precision while reproducing companion rows; the alternative construction must be a human question.
- **Alternative interpretations and missing definitions:** A non-log-symmetric interval method, distinct analysis for the P value, or substituted point/limit/P digit could explain the row. Exact coefficient SE, interval procedure and test are unreported; no particular explanation is assigned.
- **Exact human question:** Which coefficient, interval-construction method and P-value test produced OR 0.47, CI 0.30–1.62, P.70 in both APACHE rows?
### F-ST1-004 — Unadjusted day 15 immunoparalysis odds ratio does not reconcile with displayed counts

- **Relationships:** S030
- **Compared locations and document roles:** REPORT [DOC-003 p22 eTable10, immunoparalysis day15 row](../../../joi250116supp2_prod_1771885794.27755.pdf#page=22).
- **Printed values/statements:** 40/106(37.7%) versus 29/122(23.8%); unadjusted OR 1.194[1.09,3.45]; RD 13.9[1.9,25.6]; P.030.
- **Rule and calculation:** Unadjusted OR=[40/(106−40)]/[29/(122−29)]=1.94357367. The identical count-cross-product method reproduces the other three rows (4.38462,2.14646,3.32308 versus 4.38,2.15,3.32). Allowing half-unit ranges for all printed counts/denominators gives OR[1.83860,2.05506], versus printed[1.1935,1.1945]. Gap≥.64410; relative gap≥.53945. CI midpoint on log scale sqrt(1.09×3.45)=1.93920 corroborates the count reading but is not substituted for the printed point.
- **Focus area:** B
- **Proposed review domain:** statistical_results
- **Proposed relationship type / All relationships:** S_W / S_W
- **Qualifying route:** Route A, category 2
- **Affected result or extracted value:** Unadjusted immunoparalysis day 15 response OR.
- **Why context does not resolve it:** A printed magnitude discrepancy beyond .05 is always-register, even if counts and interval suggest an intended value.
- **Alternative interpretations and missing definitions:** Point estimate could refer to another analysis, but the source labels it unadjusted and provides these counts. No adjusted-versus-crude comparison is presumed.
- **Exact human question:** Which unadjusted odds ratio belongs to the 40/106 versus 29/122 day 15 immunoparalysis response comparison?
### F-ST1-005 — MALS NNH1 direction contrasts with the reported serious-event risks

- **Relationships:** S038
- **Compared locations and document roles:** REPORT [DOC-003 p44 eTable15 MALS NNH1](../../../joi250116supp2_prod_1771885794.27755.pdf#page=44) versus [p27 eTable13 Any SAE patient row](../../../joi250116supp2_prod_1771885794.27755.pdf#page=27).
- **Printed values/statements:** Number needed to treat to induce at least 1 serious TEAE(NNH1)=8.8,95% CI 3.2–10.0. Any SAE: anakinra 20/25(80.0%) versus placebo 21/23(91.3%).
- **Rule and calculation:** Risk difference for inducing harm, PI−PL=.80−21/23=−.1130435; signed reciprocal−8.84615, corresponding to fewer serious-event patients under treatment, while the printed positive NNH labeled induce gives the opposite direction. Half-unit count/denominator intervals yield RD[−.190850,−.035606], entirely negative, reciprocal[−28.0854,−5.23973], disjoint from printed positive[8.75,8.85]. Even the most favorable gap is>13.98; relative gap>1.58. Printed 80.0/91.3% half-unit percentage intervals likewise preserve the reduced-risk direction.
- **Focus area:** A, B
- **Proposed review domain:** statistical_results
- **Proposed relationship type / All relationships:** S_W / S_W
- **Qualifying route:** Route A, category 2
- **Affected result or extracted value:** MALS NNH1 harm-versus-benefit direction.
- **Why context does not resolve it:** Direction/reference-group reversals are always-register; a label that changes harm into harm prevention changes the reading.
- **Alternative interpretations and missing definitions:** The authors may report unsigned reciprocal magnitudes for both benefit and harm or reverse the reference group for this row. Neither direction convention is defined in eTable 15. The reciprocal magnitude itself is close to 8.8; the finding concerns direction, not magnitude precision.
- **Exact human question:** Does 8.8 represent patients needed to prevent or to induce a serious TEAE in MALS, and what treatment/reference-group sign convention applies?
### F-ST1-006 — Finite NNH1 confidence intervals do not reconcile with stated nonsignificant safety tests

- **Relationships:** S038, S044
- **Compared locations and document roles:** REPORT [DOC-003 p44 eTable15 MALS/IP NNH1 intervals](../../../joi250116supp2_prod_1771885794.27755.pdf#page=44), [p27 eTable13 Any SAE patient row](../../../joi250116supp2_prod_1771885794.27755.pdf#page=27); PLAN [DOC-002 p70 Safety and significance rule](../../../joi250116supp1_prod_1771885794.26255.pdf#page=70) corroborates Fisher exact/two-sided.05; REPORT [DOC-001 p6](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6) supplies.05 rule.
- **Printed values/statements:** NNH1 MALS 8.8[3.2,10.0], IP 47.6[9.9,55.8], both 95% CIs. Corresponding Any SAE 20/25 vs 21/23 and 96/106 vs 108/122.
- **Rule and calculation:** Two-sided Fisher exact tests on these integer patient counts give MALS P=.419120073 andIP P=.669907887, both>.05. A confidence set corresponding to no risk difference contains the reciprocal singularity/infinite NNH; finite same-positive 95% bounds 3.2–10.0 and 9.9–55.8 exclude that no-effect limit. Reciprocal risk-difference intervals implied by the positive bounds are MALS[.1000,.3125] andIP[.017921,.101010], excluding 0 despite nonsignificant stated tests. The observed MALS risk difference is also negative, independently tracked F-ST1-005. This is an interval-versus-test conflict; the .05 display-precision exclusion does not apply.
- **Focus area:** B
- **Proposed review domain:** statistical_results
- **Proposed relationship type / All relationships:** S_W / S_W
- **Qualifying route:** Route A, category 1
- **Affected result or extracted value:** MALS and immunoparalysis NNH1 confidence intervals and safety-inference interpretation.
- **Why context does not resolve it:** Interval-versus-stated-test conflicts are always-register; differing interval/test analyses remain alternatives to document.
- **Alternative interpretations and missing definitions:** The NNH intervals may use a different population, sign convention, confidence method or analysis from the Any SAE/Fisher safety comparison. A bounded finite positive interval may also be shorthand for a split confidence set, but no such meaning is printed. The report does not state an alternative interval analysis.
- **Exact human question:** Which patient-risk comparison and confidence transformation produced these two positive finite NNH1 intervals, and how do they relate to the nonsignificant Fisher safety comparisons?
### F-ST1-007 — NNH5 lower limit has reciprocal magnitude unavailable for a binary risk difference

- **Relationships:** S042
- **Compared locations and document roles:** REPORT [DOC-003 p44 eTable15 MALS NNH5](../../../joi250116supp2_prod_1771885794.27755.pdf#page=44), with the three NNT rows on the same page providing reciprocal-risk-difference reconstruction.
- **Printed values/statements:** MALS number needed to induce at least 5 serious TEAEs:10.1,95% CI−0.3–12.9.
- **Rule and calculation:** For patients attaining a binary≥5-event status, any risk difference lies in[−1,1], so any nonzero reciprocal NNH limit has|NNH|≥1. The same-display reciprocal convention reproduces the three NNT points from the displayed primary risk differences and their confidence limits within the .05 rule. Printed−0.3 with half-unit range[−.35,−.25] implies risk difference[−4,−2.857143], outside[−1,1]. The nearest admissible negative reciprocal magnitude is 1; minimum numeric gap 1−.35=.65; relative gap.65/.3=2.16667. Neither a branch discontinuity nor sign reversal creates an admissible magnitude below 1.
- **Focus area:** B
- **Proposed review domain:** statistical_results
- **Proposed relationship type / All relationships:** S_W / S_W
- **Qualifying route:** Route A, category 4
- **Affected result or extracted value:** MALS NNH5 lower confidence limit−0.3.
- **Why context does not resolve it:** A printed interval limit failing the reciprocal method supported by the same display is always-register. The missing≥5 patient counts do not prevent the bounded-risk identity check.
- **Alternative interpretations and missing definitions:** The limit could be on the risk-difference scale rather than the NNH scale, could refer to another measure, or could contain a substituted numeric value. A confidence procedure extending risk differences outside their parameter bounds would need explicit explanation; it is not inferred.
- **Exact human question:** What scale and confidence transformation produced the MALS NNH5 limit−0.3, given that the row is labeled a number of patients needed to harm?
### F-ST1-008 — The complete primary-response interaction table is repeated under 28-day mortality

- **Relationships:** S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083
- **Compared locations and document roles:** REPORT [DOC-003 p51 eFigure7 panel B/caption](../../../joi250116supp2_prod_1771885794.27755.pdf#page=51) versus [p52 eFigure8 panel B/caption](../../../joi250116supp2_prod_1771885794.27755.pdf#page=52); REPORT [DOC-001 pp7-8 interaction narrative](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=8).
- **Printed values/statements:** Both panel B tables print all six rows identically: APACHE .47[.30,1.62], P.70; APACHE×therapy 1.85[.66,5.19], P.24; CCI .22[.09,.53], P.001; CCI×therapy 5.79[2.34,15.05], P<.0001; SOFA .56[.27,1.19], P.13; SOFA×therapy 3.08[1.37,6.96], P.007. p 51 caption attributes primary-response interactions; p 52 caption attributes 28-day-death interactions. Panel A event counts differ across the two outcomes.
- **Rule and calculation:** Outcome matching must identify which analysis produced a printed coefficient. An entire six-row OR/CI/P array is attributed to two distinct outcome models without explanation. The primary-response high-severity crude ORs are 1.84615,5.79832,3.08442, closely matching the printed therapy rows 1.85,5.79,3.08; death high-severity crude ORs are.66204,.416,.45573. This latter calculation is a diagnostic, not a demand that adjusted interaction coefficients equal crude subgroup ORs. The direct observation is the exactly repeated model-results array with different outcome attribution.
- **Focus area:** B, C
- **Proposed review domain:** report_internal_inconsistency
- **Proposed relationship type / All relationships:** S_W / S_W
- **Qualifying route:** Route B
- **Affected result or extracted value:** The interaction coefficients andP values supporting reduced 28-day mortality among high-CCI/high-SOFA patients.
- **Why context does not resolve it:** Six identical estimate/interval/test rows under different outcome captions leave the coefficient-to-outcome mapping unclear; the main narrative uses both as result evidence.
- **Alternative interpretations and missing definitions:** Distinct models could coincidentally yield some identical rounded quantities, but no supplied explanation assigns this entire array. Different effect coding or adjustment is not assumed. The source must identify the outcome, model, covariates and coefficients for each table.
- **Exact human question:** Which interaction-model output belongs to primary response, and which belongs to 28-day mortality, for all six repeated panel B rows?
### F-ST1-009 — Prospective primary outcome and analysis change from mean comparison to responder comparison

- **Relationships:** S001, S004, S090, S094, S101
- **Compared locations and document roles:** PLAN [DOC-002 p24 primary endpoint](../../../joi250116supp1_prod_1771885794.26255.pdf#page=24), [p27 planned primary test](../../../joi250116supp1_prod_1771885794.26255.pdf#page=27), [p66 SAP definition/imputation](../../../joi250116supp1_prod_1771885794.26255.pdf#page=66), [p67 SAP Fisher analysis](../../../joi250116supp1_prod_1771885794.26255.pdf#page=67); REPORT [DOC-001 pp3,5-6](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6).
- **Printed values/statements:** Protocol V 1.0: comparative difference in mean total SOFA until day 9;1.4-point between-arm mean decrease; for deaths use mean until death; Welch t-test. SAP/report: number/proportion achieving individual baseline-minus mean SOFA(days 2–9)>1.4/≥1.4; Fisher exact; death missing SOFA 24. Report primary 46/131 vs 26/145, OR 2.48, P.002. Protocol day 15 secondary mean becomes reported day 15 responder 52/131 vs 34/145.
- **Rule and calculation:** An arm-level continuous mean difference and an individual binary responder probability are distinct endpoints/estimands and require different stated tests; mean-through-death and death 24 imputation form different aggregates. The supplied later SAP agrees with report but the original protocol's planned primary mean/Welch result is not reported. No patient-level raw-data reconstruction or preferred analysis is proposed. The strict-versus-inclusive 1.4 inequality alone is not a discrepancy under the integer SOFA grids (Excluded observations).
- **Focus area:** D
- **Proposed review domain:** protocol_report
- **Proposed relationship type / All relationships:** P_R / P_R, P_P
- **Qualifying route:** Route A, category 5
- **Affected result or extracted value:** The definition and planned analysis of the primary day 9 SOFA outcome, including death handling, and corresponding day 15 mean/responder definition.
- **Why context does not resolve it:** Planned primary analyses replaced/not reported are always-register; later plan agreement does not remove the visible original planned-versus-reported comparison.
- **Alternative interpretations and missing definitions:** SAPV 2.0 dated May 18,2024 may document an authorized revision. This card does not decide whether the revision was appropriate or prespecified before unblinding. The package does not explicitly link a primary endpoint amendment to the earlier definition in the compared passages.
- **Exact human question:** Which primary outcome/estimand and death-handling rule was operative, what documented revision reconciles the mean/Welch specification with the responder/Fisher report, and where is the originally planned primary result or its replacement identified?
### F-ST1-010 — Reported power inputs describe a different calculation from the supplied protocol

- **Relationships:** S010, S095
- **Compared locations and document roles:** PLAN [DOC-002 p26 Power](../../../joi250116supp1_prod_1771885794.26255.pdf#page=26); REPORT [DOC-001 p5 Sample Size Calculation](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5).
- **Printed values/statements:** Protocol: detect 1.4-point mean SOFA difference, dispersion phrase 3.2, two-sided independent-group t-test,90% power,5% alpha, nQuery Advisor 6.02,117/group;40% MALS/60% IP population mix. Report: primary response 40% intervention vs 20% control,90% power,5% alpha,117/group. Both 280 with about 15% dropout.
- **Rule and calculation:** A mean-difference/dispersion power model and two binary responder probabilities are different prospective design inputs, even if target N coincides. The report cites the protocol for the latter but the supplied protocol's 40%/60% quantities are immune-state proportions, not arm-specific endpoint attainment. Diagnostic normal formulas yield 109.79/group from difference 1.4/SD 3.2 and 108.24/group from response.40/.20; these are approximations, not source-exact nQuery results. Half-unit input ranges and unreported binary procedure permit 117, so those numerical diagnostics are not additional findings.
- **Focus area:** D
- **Proposed review domain:** protocol_report
- **Proposed relationship type / All relationships:** P_R / P_R
- **Qualifying route:** Route B
- **Affected result or extracted value:** Power assumptions supporting the randomized target 280 and 117 analyzable patients per arm.
- **Why context does not resolve it:** The compared source specifications identify different effect scales and different meanings of 40%; neither names a conversion/revision that maps the report's binary assumptions to the cited mean-difference calculation.
- **Alternative interpretations and missing definitions:** A revised calculation, continuity/exact adjustment, alternative dispersion definition or updated endpoint assumptions could account for 117. The exact binary formula and prospective revision are missing; they are asked about, not supplied.
- **Exact human question:** Which effect-scale assumptions and calculation produced 117 patients per arm, and where is the 40% versus 20% responder-power specification documented relative to the supplied mean-difference protocol?
### F-ST1-011 — The immune-reversal result is linked to different windows and threshold components

- **Relationships:** S005, S053, S102
- **Compared locations and document roles:** PLAN [DOC-002 p25 reversal](../../../joi250116supp1_prod_1771885794.26255.pdf#page=25), [p69 SAP reversal](../../../joi250116supp1_prod_1771885794.26255.pdf#page=69), [p70 continuation](../../../joi250116supp1_prod_1771885794.26255.pdf#page=70); REPORT [DOC-001 p5 definition](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5), [p6 Table2 footnote](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), [p7 narrative](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7); REPORT [DOC-003 p50 eFigure6/caption](../../../joi250116supp2_prod_1771885794.27755.pdf#page=50).
- **Printed values/statements:** PLAN secondary reversal byday 15: MALS≥15% ferritin decrease; IPHLA-DR/Quantibrite above 8000 AND ferritin below 4420; death before 15 nonattainment. REPORT body p 5 IP increase in absolute number of more than 8000 per cell; Table 2 footnote reach>8000, sustained and≥2 serial draws; main narrative reversal byday 28; Cox figure censored day 28. Binary result 46/59 vs 32/66, OR 3.76[1.72,8.22], P.001; HR 2.38[1.50,3.77].
- **Rule and calculation:** Day 15 versus day 28 responder ascertainment and inclusion of a ferritin condition define different endpoints; increase BY 8000 versus reach 8000 define different IP thresholds. For baseline HLA approximately 3000, these readings require approximately 11000 versus 8000, respectively; this is a diagnostic illustration, not a patient-level calculation. Report serial-permanence/two-draw condition is additional to the compared PLAN definitions. These definitions cannot be treated as a single identical binary endpoint without a stated mapping.
- **Focus area:** D, C
- **Proposed review domain:** protocol_report
- **Proposed relationship type / All relationships:** P_R / P_R, S_W, S_C
- **Qualifying route:** Route A, category 5
- **Affected result or extracted value:** Secondary SIDF-reversal attainment 46/59 versus 32/66 and its associated OR/HR and time window.
- **Why context does not resolve it:** Composite/endpoint definitions changed across planned and reported passages are always-register. The Table 2 footnote supplies one possible intended threshold but does not reconcile the planned day 15 endpoint with reported day 28 ascertainment/ferritin condition.
- **Alternative interpretations and missing definitions:** day 28 Cox may be a separate posthoc time analysis while Table 2 retains day 15 binary attainment, but the main narrative explicitly connects binary reversal to day 28. Ferritin condition might be implicit in immune classification, yet that classification is baseline and not stated as the reversal criterion. 'increase' might mean reaching the absolute threshold; direct numeric readings remain recorded.
- **Exact human question:** What exact window, HLA-DR change-versus-level threshold, ferritin condition and sustained/two-draw rule generated the binary reversal counts and which planned reversal endpoint do they represent?
### F-ST1-012 — Current-trial outcome status changes within supplied plan versions and report

- **Relationships:** S103, S108
- **Compared locations and document roles:** PLAN [DOC-002 p7 synopsis](../../../joi250116supp1_prod_1771885794.26255.pdf#page=7), [p25 detailed hierarchy](../../../joi250116supp1_prod_1771885794.26255.pdf#page=25), [p27 test map](../../../joi250116supp1_prod_1771885794.26255.pdf#page=27), [p57 resolution appendix](../../../joi250116supp1_prod_1771885794.26255.pdf#page=57), [p70 SAP infection paragraph](../../../joi250116supp1_prod_1771885794.26255.pdf#page=70); REPORT [DOC-001 p5 six prespecifiedsecondary endpoints](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5).
- **Printed values/statements:** Protocol synopsis lists infection resolution and omics development among secondary endpoints; detailed protocol p 25 classifies both as exploratory, p 27 infection test is exploratory, p 57 resolution criteria exploratory. SAPp 70 places infection resolution in secondary section. Report p 5 calls infection resolution one of six prespecified secondary endpoints.
- **Rule and calculation:** Prespecified status is an explicit design element; secondary and exploratory status cannot both describe the same operative hierarchy without identifying the relevant version/revision. One repeated hierarchy pattern covers infection resolution and omics in the current trial; historical appendix outcomes are not compared. No multiplicity hierarchy is inferred.
- **Focus area:** D
- **Proposed review domain:** protocol_report
- **Proposed relationship type / All relationships:** P_R / P_R, P_P
- **Qualifying route:** Route A, category 5
- **Affected result or extracted value:** Prespecified status of day 15 infection resolution; plan internal status of omics development.
- **Why context does not resolve it:** Planned-versus-reported outcome status is always-register, including an apparent revised plan status that requires human clarification.
- **Alternative interpretations and missing definitions:** Synopsis may use' secondary' as an umbrella, or SAP may formalize an authorized status change. The detailed separate exploratory heading gives a distinct status. This card does not claim an undisclosed violation or require that exploratory omics be reported.
- **Exact human question:** Which operative hierarchy classified infection resolution and omics, and what revision or explicit umbrella usage reconciles the supplied secondary/exploratory labels?
### F-ST1-013 — Planned binary infection-resolution analysis differs from reported ordinal analysis

- **Relationships:** S006, S052, S104
- **Compared locations and document roles:** PLAN [DOC-002 p70 Infection resolution](../../../joi250116supp1_prod_1771885794.26255.pdf#page=70); REPORT [DOC-001 p6 Statistical Analyses/Table2](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), [DOC-003 p49 eFigure5](../../../joi250116supp2_prod_1771885794.27755.pdf#page=49).
- **Printed values/statements:** SAP binary resolved/not resolved atday 15, Fisher exact, OR/95% CI by Mantel-Haenszel; report four level resolved/intermediate/failure/superinfection, ordinal regression, worse outcome OR.59[.38,.91], P.018/.02. Main states that all analyses follow SAP.
- **Rule and calculation:** A binary response comparison and an ordered four category model analyze different quantitative contrasts. OR.59 is explicitly an ordinal worse-outcome OR, not the SAP's binary resolution OR; the planned binary analysis is not supplied alongside it. Binary resolved counts 58/131 vs 46/145 yield crude OR 1.70935 for resolution, but this diagnostic is not compared as a numerical contradiction to the ordinal OR.
- **Focus area:** D
- **Proposed review domain:** protocol_report
- **Proposed relationship type / All relationships:** P_R / P_R
- **Qualifying route:** Route B
- **Affected result or extracted value:** Reported secondary day 15 infection result OR.59 andP.018/.02, and its prespecified analysis mapping.
- **Why context does not resolve it:** The report explicitly names ordinal analysis while the cited SAP names binary Fisher/MH; no passage identifies ordinal analysis as a replacement/addition. Context distinguishes the models but does not reconcile the claim that all reported analyses follow SAP.
- **Alternative interpretations and missing definitions:** A disclosed amendment or additional ordinal analysis could coexist with an unreported binary analysis. No method p reference or causal interpretation is proposed.
- **Exact human question:** Which planned or revised specification authorized the ordinal infection analysis, and where is the SAP's binary resolution result or explicit replacement identified?
### F-ST1-014 — Adjusted primary-model covariate lists differ for the same printed result

- **Relationships:** S009, S018, S020, S022, S024, S026, S097
- **Compared locations and document roles:** REPORT [DOC-001 p6 confirmatorymodel](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6); REPORT [DOC-003 p21 eTable9 multivariatecolumn](../../../joi250116supp2_prod_1771885794.27755.pdf#page=21); PLAN [DOC-002 p67 model](../../../joi250116supp1_prod_1771885794.26255.pdf#page=67) corroborates APACHE as listed covariate.
- **Printed values/statements:** Main: model dependent response; independent variables: blinded intervention, baseline CCI, SOFA, study site; adjusted therapy OR 2.49[1.42,4.36]. eTable 9 multivariate includes precision therapy 2.49[1.42,4.36], APACHEII 1.00[.96,1.05], P.826; CCI.95[.84,1.07]; SOFA 1.02[.95,1.09]; site.80[.46,1.41]. SAP list includes APACHE II, CCI, SOFA, site.
- **Rule and calculation:** An explicitly enumerated primary model covariate list omits APACHE II while the linked multivariate output includes a quantified APACHE coefficient alongside exactly the same therapy OR/CI. Stepwise selection alone does not explain an APACHE coefficient in a model described without it; the supplied passages donot identify the table as a different full starting model.
- **Focus area:** C
- **Proposed review domain:** statistical_results
- **Proposed relationship type / All relationships:** S_C / S_C
- **Qualifying route:** Route B
- **Affected result or extracted value:** Adjusted primary precision OR 2.49 and its covariate-adjustment specification.
- **Why context does not resolve it:** The identical therapy result links the lists to the same reported analysis, but the absence-versus presence of APACHE prevents determination ofthe explicit final adjustment set from the methods passage alone.
- **Alternative interpretations and missing definitions:** The main list may be an abbreviated description or eTable 9 may show a full model rather than selected model. The table does not label that distinction. SAP corroborates one list and does not create a separate conflict relationship.
- **Exact human question:** Was APACHE II included in the model that produced adjusted OR 2.49, and does eTable 9 report the full starting model or the final stepwise model?
### F-ST1-015 — Several prespecified primary/key-secondary analysis results are not located

- **Relationships:** S098, S099, S107
- **Compared locations and document roles:** PLAN [DOC-002 p67 immune-stateprimaryanalysis](../../../joi250116supp1_prod_1771885794.26255.pdf#page=67), [p68 survivorprimarySOFA and28daymortality](../../../joi250116supp1_prod_1771885794.26255.pdf#page=68), [pp71-72 antibioticprimarysubgroup](../../../joi250116supp1_prod_1771885794.26255.pdf#page=71); REPORT [DOC-001 pp5-8](../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6); REPORT [DOC-003 pp21-24,47,51-53](../../../joi250116supp2_prod_1771885794.27755.pdf#page=22), and complete DOC-003 pp 1-54 map.
- **Printed values/statements:** Planned primary-response OR heterogeneity MALS vs IP by Breslow-Day/Tarone; survivor SOFA mean(days 1–9)/9 t-tests within immune phenotypes;28-day mortality MALS/IP subgroups; primary response appropriateness-of-antibiotics subgroup. Report provides MALS/IPday 9 response counts, overall 28 dayOR/HR, severity subgroups, and baseline appropriate antibiotic percentages but not these named analysis tests/results.
- **Rule and calculation:** Match specific outcome, population and test for each prospective analysis against complete all-unit report maps. No Breslow-Day/Tarone immune state primary test, survivor SOFA mean/t-test,28 day immune-stratum mortality result, or antibiotic appropriateness primary response contrast is located. A heatmap does not report a Student t comparison; baseline antibiotics counts are not primary response counts; severity strata are not immune phenotype strata. These are planned primary or key-secondary 28 day analyses, not an expectation that all nonkey/exploratory results be published.
- **Focus area:** D
- **Proposed review domain:** protocol_report
- **Proposed relationship type / All relationships:** P_R / P_R
- **Qualifying route:** Route A, category 5
- **Affected result or extracted value:** Prespecified primary immune heterogeneity/survivor/antibiotic analyses and key-secondary 28 day mortality immune-subgroup estimates/tests.
- **Why context does not resolve it:** Planned primary/key-secondary analysis not reported is always-register. Complete unit mapping, not a selected display search, underlies the absence claim.
- **Alternative interpretations and missing definitions:** Results could appear under another label or in the available graphs without an explicit numerical/test label; a supplied location or documented replacement would reconcile the issue. No outside paper or raw data is sought.
- **Exact human question:** Where are the results or explicit replacement/nonreporting statements for each of the four named prespecified primary/key-secondary analysis families?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-001 p 7 day 15 narrative vs Table 2 p 6 | Narrative 51/131 alongside 39.7% vs Table 2 52/131; half-unit count/denominator interval permits display difference≤.05. Not a statistical finding. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p 7 MALS primary P.04 vs DOC-003 p 22 P.034 | Printed half-unit intervals [.035,.045]vs[.0335,.0345]gap.0005/.04=.0125≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 pp 5-6 and DOC-002 pp 67,69 >1.4 vs≥1.4 | Exact 1.4 is unattainable for integer SOFA change on 1/8(day 9)or 1/14(day 15)grids;1.4×8=11.2,1.4×14=19.6. No operational classification difference under stated rules. | NOT_REPRODUCED |
| DOC-001 p 5 vs DOC-002 p 26 sample size 117 | Normal diagnostic 109.79 continuous/108.24 binary, not exact nQuery/unknown binary procedure; half-unit input intervals permit 117. No independent numeric failure. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 p 5 and DOC-002 p 26 N 280/≈15% dropout | 234/.85=275.294 versus 280,1.68% relative gap; approximately 15% dropout and rounded target reconcile. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 p 44 overall NNT lower 3.9 vs RD upper 27.2 | Reciprocal upper-risk limit produces NNT[3.6697,3.6832] vs printed[3.85,3.95]; minimum gap.1668/3.9=.0428≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 p 44 overall NNH1 point 200 vs Any SAE reciprocal absolute 240.44 | Full half-unit count/denominator RD interval crosses 0 and includes±.005; reciprocal 200 cannot be distinguished using the display rule. MALS direction and NNH1 interval issues are separate findings. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 p 44  IP NNH1 point 47.6 vs Any SAE reciprocal 48.985 | Relative point difference approximately.0291 before full input rounding,≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 p 44 NNH2–5 point/interval numeric reconstruction | Per patient≥2–5 event incidences and interval method unreported; do not invent counts from total repeated TEAEs. Bound−.3 failure is independent F-ST1-007. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 p 44 mixed-sign NNH confidence endpoints | Finite printed negative/positive endpoints may encode split reciprocal branches. An unstated rendering convention alone does not establish the finite interval as the confidence-set topology; no independent finding without a conflicting printed number beyond F-ST1-007. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 pp 51-53 panel B interaction P values vs crude high/low-stratum OR ratios | Exact interaction model, covariates, coding, covariance and test not reported. Comparing modeled coefficients with crude interaction ratios is conditional. Duplicated outcome attribution and point/interval failures remain findings. | MODEL_VERSUS_CRUDE |
| DOC-003 pp 51-53 panel B Wald P diagnostics (including CCI×therapy P<.0001) | Full-width log-Wald diagnostic is not an identified reported test; nominal CI/null significance agrees except separate containment finding. Unknown joint test/lower precision prevents exact P compatibility claim. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 p5 posthoc vs DOC-003 pp51-53 pre-defined cutoffs | The prospective procedure could be defined while numerical thresholds are derived after data collection; wording alone does not identify an analysis change. The apparent cutoff-outcome difference is separately excluded below because the figure caption does not assert a different ROC derivation. | TERMINOLOGY_OR_WORDING |
| DOC-001 p 5 continuous SOFA for all analyses vs binary response analysis p 6 | Continuously recorded SOFA enters an explicit responder transformation; measurement parameterization does not require every downstream model to be continuous. | CONTEXT_RESOLVES |
| DOC-002 p 67 logistic independent list omits treatment | Treatment contrast is implicit in the confirmatory trial model; report and result table explicitly supply it. Main APACHE list conflict tracked separately. | CONTEXT_RESOLVES |
| DOC-002 pp 69-70 immune-reversal wording at least 15% of baseline | Preceding/following decrease criterion makes the wording shortcut identifiable; no suppressed printed threshold conflict. | TERMINOLOGY_OR_WORDING |
| DOC-002 p 69 day 15 paragraph says until day 9 and primary endpoint | Explicit day 15 formula and 14 value denominator resolve nearby label slips; no changed number or window inferred from the label alone. | CONTEXT_RESOLVES |
| DOC-002 p 69 omitted plus glyphs in survivor SOFA formula | Enumerated day 1–15 values and/15 denominator identify addition. | NOTATION_OR_TYPOGRAPHY |
| DOC-002 p 26 dispersion phrase'mean difference in the standard deviation' | Field reader recognizes the sample-size dispersion context; no alternate variance estimate supplied. Source-scale power comparison is F-ST1-010. | TERMINOLOGY_OR_WORDING |
| DOC-002 pp 68-72 nonkey secondary 90 day immune/day 15 survivor and exploratory ROC nonreporting | No additional primary/key secondary result bearing established; planned primary/key 28 day omissions are F-ST1-015. | PERIPHERAL_COMPARISON |
| DOC-002 p 3 interim heading vs statistical section p 27 | Contents heading does not provide a stopping rule or claim an interim decision; absence of boundary alone is not a finding. | CONDITIONAL_OR_UNREPORTED |
| DOC-002 pp 35-53 historical PROVIDE printed inferential rows | Historical appendix does not describe ImmunoSep results or operative planned decision rules; no historical result aligned to current trial. | PERIPHERAL_COMPARISON |
| DOC-003 p 53 eFigure 9 caption versus PLAN DOC-002 pp 70-71 and REPORT DOC-001 p 5 | Caption says the cutoffs indicate increased risk for 90-day mortality, but does not explicitly say their ROC derivation used 90-day mortality. A 28-day-derived cutoff can also indicate 90-day risk; no conflicting derivation is reproduced. | CONTEXT_RESOLVES |

## Limits and handoff

Exact patient-level TEAE incidences at ≥2–5 event thresholds, coefficient standard errors/covariance/test statistics, raw longitudinal SOFA records and numerical forest limits are not supplied. Each missing input is named in the inventory. No scientific coverage gap remains. Every finding requires an independent inclusion screen before candidate registration and a direct-source mechanical recheck afterward. Any registered candidate remains Pending Human Adjudication.

Owned artifacts: statistics/relationship_inventory.md and checkers/statistical_pass_1.md. Runtime ID: /root/statistical_pass_1; the coordinator records it once in the execution manifest. Pass 2 must use a different fresh high-effort agent and review all 111 S IDs against the complete ledger, screening log and recheck facts.

