# Statistical relationship inventory — pass 2, REPORT early shard

Fresh runtime: `/root/stat2_reports_early`; gpt-6.1-sol/high; FRESH_SPAWN. Exact assigned set: S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220. This part updates those existing stable records without replacing their pass-1 provenance. All source locations below are physical PDF pages. REPORT supplement is DOC-005; PLAN protocol/SAP are DOC-002/DOC-003. Main DOC-001 is REPORT. Source links use this part's four-level relative depth.

Complete inputs read: QUALITY_CONTROL_SCOPE.md, the 1.6.2 contract, performance profile, report specification/settings, assigned pass-1 packet, entire current 17-ID candidate ledger, all 26 initial screening decisions, all 17 mechanical recheck cards and all 47 original checker exclusion rows. No prior-run conclusions or web evidence used. Current source images were visually read; source/OCR authority and engine details are in the checker part.

## S201 — Outcome definitions, thresholds and directions

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.2, Outcome Measures](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=2).
- **Pass-2 check:** Severity is the mean of 11 BPI items, intensity of four, interference of seven, all 0–10 and higher worse. MCID is at least 30% decrease from baseline, so favorable response is an increase in the responder probability and RR above 1 for active versus UC. PHQ-8 sum 0–24 and GAD-7 sum 0–21 agree with eight/seven items each 0–3. PROMIS sleep is higher worse, social/physical higher better, with reference T mean 50/SD10 and the stated 60/40 thresholds. Item totals, scale ranges and directions reconcile with the assigned response rows; no superiority margin, noninferiority or equivalence rule is supplied for this relationship.
- **Named definition limits:** Raw PROMIS conversion tables and item-level scoring are absent; no reconstruction is needed for a printed conflict. Main scoring wording is considered in the prior-exclusion audit, without inventing an alternative score.
- **Finding/cross-lane implication:** No new finding.

## S202 — Primary response completeness and missingness decision

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.4, Missing Data](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [p.7, eTable1](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7); PLAN [DOC-003 p.19, section11](../../../../joi250046supp2_prod_1755300121.15087.pdf#page=19).
- **Pass-2 check:** Randomized 2331=777+776+778. Observed 3-month 1798=621+542+635, 77.1%; missing 22.9% exceeds the stated 15% branch. Arm 79.9%,69.8%,81.6% completeness also establishes differential missingness. Any follow-up 2036=703+643+690 and none 295=74+133+88; 2036+295=2331. The pattern counts sum 2039 rather than 2036; implied visits 5458 rather than 5449. Half-unit gaps 1/2036=.000491 and 4.5/5449=.000826 are at most .05. This is one display-precision observation, not an always-register category3 reproduction above the threshold.
- **Named definition limits:** Exact corrected pattern classification cannot be identified from supplied aggregate counts. That limit does not change whether the missingness branch is triggered.
- **Finding/cross-lane implication:** No new finding; C007 already records the primary/sensitivity role comparison, including the disclosed amendment and conditional branch.

## S203 — Additional predictor selection and analysis attribution

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.4, Adjustment](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [p.5, Non-Response Weighting](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), [p.7, eTable2](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), [p.8](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=8), [p.9](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=9), [p.10](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); PLAN [DOC-002 p.56](../../../../joi250046supp1_prod_1755300121.14087.pdf#page=56), [DOC-003 p.20](../../../../joi250046supp2_prod_1755300121.15087.pdf#page=20).
- **Pass-2 check:** The dual P<.10 selection rule uses adjusted 3-month MCID and 3-month missingness models for imputation/estimation, and MCID plus any-follow-up models for weights. These are distinct tests and response definitions, so one selection P is not a fitted-model coefficient P. Age's prespecified-base attribution, binary education versus three coefficients, and education versus employment in the weight set are already C005, C013 and C012. Their recheck facts remain source-supported and are not re-emitted.
- **Named definition limits:** Final covariate design matrices, selection-versus-final-fit coding and prospective age specification are absent. No preferred selection method is proposed.
- **Finding/cross-lane implication:** C005, C012, C013; no new finding.

## S204 — Pattern-mixture imputation design and response construction

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.4, equation](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=4), [p.5, imputation continuation](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=5).
- **Pass-2 check:** The conditional change model contains arm, time6/time12, arm×time, observed-pattern1/pattern2 and arm×pattern terms; reference cells are UC,3months,pattern3. It is fitted among participants with at least one observation using linear GEE, independence and robust person/coach clustering; predictions replace missing changes and MCID uses those changes plus baseline severity. These stated steps identify the linear-change versus binary-response analyses. The formula includes the listed term families shown in eTable3. The duplicated UC name in the arm definition is identifiable from the equation's PT/HC indicators and three-arm context; it does not alter a printed coefficient.
- **Named definition limits:** Exact change sign, individual predictions, truncation and joint covariance are not numerically supplied. The positive conditional PT/HC coefficients alone do not establish a direction reversal of marginal treatment response.
- **Finding/cross-lane implication:** Existing C013 coding question retained; no additional method conflict or new finding.

## S205 — Imputation population, observed visits and missing values

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.7, eTable1](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7), [p.8, eTable3 header](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=8).
- **Pass-2 check:** 2331−295=2036 any-follow-up persons; 2036×3=6108 full imputed visits; observed visits 1798+1790+1861=5449; 6108−5449=659 missing values. All reproduce exactly. The estimated target population of all randomized is distinguished from contributing imputation persons and visits; it is not an assertion that all2331 supplied observations.
- **Named definition limits:** Individual pattern assignment is absent; S202's small aggregate discrepancy remains below the precision threshold.
- **Finding/cross-lane implication:** No new finding.

## S206 — Primary estimation functional form, variance and clustering

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.5, second-step equation/method](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), [p.9, eTable4](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=9); REPORT [DOC-001 p.4](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); PLAN [DOC-003 p.20](../../../../joi250046supp2_prod_1755300121.15087.pdf#page=20).
- **Pass-2 check:** Log mean of binary MCID, Poisson GEE, arm/time/arm×time and robust provider/person sandwich are explicitly stated. Joint imputation/analysis variance is described by a supplied citation without numeric matrix. The form generates the treatment/time contrast families in eTable4. Main explicitly says tests are two-sided at .05; this is read, not inferred. Repeated observations/person and provider clustering are addressed in the printed description; no independent-samples method is asserted. Generic Poisson use for binary outcomes is internally coherent with the stated robust variance.
- **Named definition limits:** Numeric covariance, exact coefficient-test reference distribution, degrees of freedom and CI construction are not supplied. Exact coefficient P reconstruction therefore cannot be asserted from a normal approximation.
- **Finding/cross-lane implication:** C005/C007/C013/C014 remain the relevant recorded specification/test comparisons; no new finding.

## S207 — Nonresponse weighting and baseline missing covariates

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.5](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=5), [p.6](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=6), [p.10, eTables5–6](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=10); PLAN [DOC-003 p.4 amendment](../../../../joi250046supp2_prod_1755300121.15087.pdf#page=4), [p.19](../../../../joi250046supp2_prod_1755300121.15087.pdf#page=19).
- **Pass-2 check:** Logistic response is at least one follow-up in all randomized; raw weights1/p are scaled then applied to second-step estimation. Imputation handles intermittent missingness among2036 contributors; nonresponse weights represent those with none. Baseline means are imputed from available baseline data, which is distinct from outcome pattern-mixture imputation. Weight sum2036 persons and6108 visits identifies the contributor normalization in context; all-randomized estimand2331 is a distinct quantity. The July2024 SAP amendment expressly supplies IPW support; no absence of disclosure is claimed.
- **Named definition limits:** Individual probabilities and applied weight-model vector are absent; C012 addresses explicit predictor membership. C007 retains the final hierarchy question rather than asserting the amendment is absent.
- **Finding/cross-lane implication:** C007/C012; no new finding.

## S208 — Complete linear imputation coefficient/interval/P family

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.8, every eTable3 coefficient row](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=8); REPORT [DOC-001 p.4, two-sided .05](../../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4).
- **Pass-2 check:** All28 printed tuples have ordered endpoints and contained points. The seven direct95%CI-null/P conflicts are Pattern2 −.28(−.47,−.08),P.150; Pattern1 −.20(−.36,−.03),P.226; Pattern2×PT −.30(−.58,−.02),P.280; Pattern2×HC −.47(−.74,−.19),P.090; Site3 .19(.08,.29),P.069; Site4 .15(.05,.24),P.124; secondAA .16(.07,.25),P.077. Each remains C014/F-ST1-201; category1 has no rounding removal. Remaining rows have matching printed null/significance statuses. For Time6 .13(.07,.19),P.025, a normal-Wald diagnostic SE=.12/3.92=.030612,z4.2467 yields about.000022; this is not an exact reported test reproduction because its distribution/CI construction are absent. It does not become a further finding by assuming normal tests.
- **Named definition limits:** Numeric SEs, reference distribution/df, exact CI/test construction and unrounded values absent. Education mapping belongs C013; conditional direction belongs S204.
- **Finding/cross-lane implication:** C013/C014; no new finding.

## S209 — Complete weighted primary RR/interval/P family

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.9, every eTable4 row](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=9).
- **Pass-2 check:** All23 printed rows, including identical HC/PT3M repetition, have contained points and ordered endpoints. PT/UC1.28(1.06,1.55),P.010; HC/UC1.54(1.3,1.82),P<.001; HC/PT1.2(1.03,1.4),P.019 show favorable active responder directions. Ratio closure1.54/1.28=1.203125 is compatible with1.2;6M1.62/1.44=1.125 with1.13;12M1.41/1.32=1.06818 with1.07 under half-units. Age1.15(1,1.33),P.046 and secondAA1.16(1,1.33),P.046 are already C014/F-ST1-202; printed null endpoints are retained regardless of unrounded alternatives. Other tuples' null/P statuses agree. The duplicate3M row agrees exactly and is not an exclusion.
- **Named definition limits:** Joint covariance/CI-test construction and unrounded null-adjacent endpoints absent; repeated site labels carry intentional healthcare-site suppression context. No crude-ratio comparison is made.
- **Finding/cross-lane implication:** C013/C014; no new finding.

## S210 — Complete response-logistic OR/interval/P family

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.10, every eTable5 coefficient](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=10).
- **Pass-2 check:** All16OR tuples have ordered endpoints and contained points. UC/PT2.05(1.50,2.79),P<.001 and HC/PT1.68(1.25,2.26),P<.001 agree with higher follow-up odds outside PT; these are response odds, not pain-response risks. Male.76(.57,1.00),P.053 has null/P agreement. PEG.96(.92,1.00),P.037 repeats C014/F-ST1-202 and remains under category1. All remaining printed null/P statuses agree. c-statistic.679 is not a regression coefficient or an interval-bearing treatment effect; no numeric uncertainty is supplied.
- **Named definition limits:** Numeric logistic test statistics, SEs, df, exact interval construction and final predictor vector absent. OR versus RR labels are coherent with the stated different outcomes/models.
- **Finding/cross-lane implication:** C012/C014; no new finding.

## S211 — Response-probability and analytic weight summaries

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.10, eTable6](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=10).
- **Pass-2 check:** Response probabilities mean.88,SD.07,min.50,P25.85,P50.90,P75.93,max.98 are ordered and bounded. Weights sum2036,mean1.00,SD.09,min.89,P25.94,P50.97,P751.03,max1.75 are ordered, and2036×1=2036. Reversed quantile pair products .50×1.75=.875, .85×1.03=.8755,.90×.97=.873,.93×.94=.8742,.98×.89=.8722 support a common positive scaling factor under half-unit intervals. The transformations are reciprocals before scaling; mean(1/p) is not set equal to1/mean(p).
- **Named definition limits:** Individual weight normalization and probability sample membership beyond the analytic context are not supplied numerically. No significance test or stopping rule applies to these descriptive summaries.
- **Finding/cross-lane implication:** No new finding.

## S212 — Complete-case sensitivity method and multiplicity rule

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.11, eTable7 introduction/header/notesb–e](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11); PLAN [DOC-003 p.19, sections10–11](../../../../joi250046supp2_prod_1755300121.15087.pdf#page=19).
- **Pass-2 check:** Complete case removes missing outcomes, no imputation or weighting;3M1798=621+542+635. Seven listed baseline factors produce modified-Poisson GEE adjusted percentages, RRs and reciprocal NNTs. The omnibus Wald P is a three-arm test; pairwise comparisons are interpreted only when omnibusP<.05. All three complete-case omnibusPs<.001 satisfy the rule. Omnibus significance does not imply that HC/PT is significant. The adjusted versus full-primary results are distinct analyses and should not be compared as copies.
- **Named definition limits:** Exact pairwise covariance/RD intervals, omnibus statistic and df are absent. C007 records sensitivity/primary hierarchy; the provided complete-case result is not absent from the package.
- **Finding/cross-lane implication:** C005/C007 background; no new finding.

## S213 — Worst/best-case sensitivity method and population

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.11, worst/best-case block and notes](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11); PLAN [DOC-003 p.19](../../../../joi250046supp2_prod_1755300121.15087.pdf#page=19).
- **Pass-2 check:** Missing PT/HC outcomes set0 and missingUC set1, yielding all2331=777+776+778. This deliberately unfavorable active direction matches the plan's supplied second sensitivity approach. The same seven-factor adjustment and GEE method are explicit. All three omnibusPs<.001 pass the stated gate. NNT notes describe disconnected positive-to-infinity and negative-to-negative-infinity branches when RD crosses0; a positive then negative endpoint is not treated as a finite conventional interval.
- **Named definition limits:** Per-person assignments, RD covariance and exact pairwise CI method absent; no superiority conclusion for the primary analysis is inferred from this different sensitivity analysis.
- **Finding/cross-lane implication:** No new finding.

## S214 — eTable7 complete-case3-month tuple

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.11, complete-case3M row](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11).
- **Printed tuple:** PT32.2(28.5,36.3),HC35.5(32.0,39.3),UC24.0(20.9,27.6); RR PT/UC1.34(1.12,1.61),HC/UC1.48(1.24,1.75),HC/PT1.10(.94,1.29); omnibusP<.001; NNT13(8,33),9(7,15),31(13,−60).
- **Pass-2 check:** All group/RR points contained, endpoints ordered; RR points agree with corresponding adjusted proportions after half-unit arithmetic. NNT point intervals from100/(rate difference) are [12.048193,12.345679],[8.620690,8.771930],[29.411765,31.250000]. Printed13 has expanded[12.5,13.5],gap.154321/13=.011871; the other two overlap. HC/PT RR includes1 and NNT's two branches include infinity, matching the footnote's null interpretation. Omnibus gate passes without claiming every pair differs.
- **Named definition limits:** RD CI and covariance absent; marginal group CIs cannot reproduce NNT limits without them.
- **Finding/cross-lane implication:** No new finding; precision pattern in checker exclusions.

## S215 — eTable7 complete-case6-month tuple

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.11, complete-case6M row](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11).
- **Printed tuple:** PT40.1(36.3,44.3),HC41.1(37.4,45.1),UC26.6(23.4,30.3); RR1.51(1.28,1.77),1.54(1.32,1.81),1.02(.90,1.17); omnibusP<.001; NNT8(6,13),7(6,11),101(16,−22).
- **Pass-2 check:** Group/RR containment, endpoint order and favorable active directions hold. RR ratios agree under printed precision. Reciprocal NNT point intervals [7.352941,7.462687],[6.849315,6.944444],[90.909091,111.111111] give PT gap7.5−7.462687=.037313/8=.004664 and overlap for the other two. HC/PT RR-null and disconnected NNT-null interpretation agree; omnibus gate passes.
- **Named definition limits:** RD interval covariance/construction absent; no pairwise P is supplied and none is inferred from omnibusP.
- **Finding/cross-lane implication:** No new finding.

## S216 — eTable7 complete-case12-month tuple

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.11, complete-case12M row](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11).
- **Printed tuple:** PT41.0(37.3,45.1),HC41.5(37.9,45.4),UC30.5(27.2,34.3); RR1.34(1.16,1.56),1.36(1.17,1.57),1.01(.89,1.15); omnibusP<.001; NNT10(7,20),10(7,15),217(22,−28).
- **Pass-2 check:** Group/RR containment/order/direction and ratio reproduction hold. NNT point intervals [9.433962,9.615385],[9.009009,9.174312],[166.666667,250.000000] give second point gap9.5−9.174312=.325688/10=.032569; first/third overlap. Thus no above-.05 reciprocal discrepancy. HC/PT's RR and disconnected NNT agree in their null interpretation, and omnibus gate passes.
- **Named definition limits:** Same RD covariance/CI and exact pairwise tests absent as S214/S215.
- **Finding/cross-lane implication:** No new finding.

## S217 — eTable7 worst/best-case3-month tuple

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.11, worst/best-case3M row](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11).
- **Printed tuple:** PT22.7(20.0,25.8),HC29.3(26.3,32.6),UC39.4(36.1,43.0); RR.58(.49,.67),.74(.65,.85),1.29(1.09,1.52); omnibusP<.001; NNT−6(−9,−5),−10(−18,−7),16(10,40).
- **Pass-2 check:** Ordered/contained group andRR intervals; active-versusUC RRs below1 and negative NNTs agree with this unfavorable sensitivity assignment. HC/PT benefit direction agrees. Reciprocal NNT intervals [−6.024096,−5.952381],[−10.000000,−9.803922],[14.925373,15.384615] overlap first/second printed points; third gap15.5−15.384615=.115385/16=.007212. Gate passes. No NI/equivalence or stopping conclusion is made.
- **Named definition limits:** Exact RD covariance/CI construction absent; independent marginal CI subtraction is not used.
- **Finding/cross-lane implication:** No new finding.

## S218 — eTable7 worst/best-case6-month tuple

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.11, worst/best-case6M row](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11).
- **Printed tuple:** PT28.6(25.6,31.9),HC33.1(30.0,36.5),UC41.3(38.0,44.9); RR.69(.60,.79),.80(.70,.91),1.16(1.00,1.34); omnibusP<.001; NNT−8(−13,−6),−13(−26,−8),23(12,227).
- **Pass-2 check:** Group/RR containment/order, ratio points and directions hold. NNT point intervals [−7.936508,−7.812500],[−12.345679,−12.048193],[21.739130,22.727273] give middle gap.154321/13=.011871 and overlap otherwise. Gate passes. HC/PT printed RR includes1, while finite positive NNT23(12,227) reciprocally implies RD[1/227,1/12]=[.004405,.083333]. The proposed C008 source expansion was independently screened out as ROUNDING_OR_DISPLAY_PRECISION: the printed lower RR1.00 permits true lower endpoints above1 within [.995,1.005], and P<.001 is omnibus, not a pairwise interval/P conflict. The existing C008 affected locations are unchanged.
- **Named definition limits:** Parameter-specific RR/RD CI methods, unrounded lowerRR endpoint and joint covariance absent; distinct constructions can yield distinct null coverage.
- **Finding/cross-lane implication:** Proposed C008 source expansion excluded independently as ROUNDING_OR_DISPLAY_PRECISION; no new finding.

## S219 — eTable7 worst/best-case12-month tuple

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.11, worst/best-case12M row](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=11).
- **Printed tuple:** PT31.3(28.2,34.6),HC34.4(31.2,37.8),UC43.0(39.6,46.7); RR.73(.64,.83),.80(.70,.91),1.10(.96,1.26); omnibusP<.001; NNT−9(−15,−7),−12(−21,−8),33(15,−194).
- **Pass-2 check:** Group/RR containment/order, ratio reproduction and unfavorable active-versusUC direction hold. Reciprocal point intervals [−8.620690,−8.474576],[−11.764706,−11.494253],[31.250000,33.333333] all overlap printed half-unit points. HC/PT RR straddles1 and NNT uses the footnote's infinity-reaching disconnected branches, so the null readings agree. Omnibus gate passes; no pairwise P is inferred.
- **Named definition limits:** RD covariance/CI construction and exact tests absent; this is not a primary-analysis result copy.
- **Finding/cross-lane implication:** No new finding.

## S220 — Protocol-change subset definitions, populations and adjustment

- **Status:** PASS_1_COMPLETE; PASS_2_COMPLETE
- **Exact locations and roles:** REPORT [DOC-005 p.13, Protocol Change Subset Analyses](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=13), [p.14, eTable8 headers/notes](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=14), [p.7, eTable1/eTable2](../../../../joi250046supp4_prod_1755300121.15587.pdf#page=7).
- **Pass-2 check:** Randomized pre/post454+1877=2331; any-follow-up366+1670=2036. Letters858 observed3M/1038=.82659 and935 any/1038=.90077 reproduce82.7%/90.1%. The enhancement boundary8/9/2021 is explicit; reminder-letter3/31/2022 analysis is explicitly post hoc. Seven-variable subset adjustment versus full selected education/employment primary adjustment remains C011, already screened. First header's PT149+HC153+UC152=454 at3months exceeds366 any-follow-up: minimum half-unit excess86/366=.234973. Pass1's proposed randomized-population interpretation is retained as an alternative, but cross-lane C015's RouteA3 observation is not removed as context or labeling. These dates describe retrospectively reported subsets, so these locations are REPORT.
- **Named definition limits:** First-header count convention and implemented subset covariate vectors absent. No missing weighting/imputation is inferred from the abbreviated footnote.
- **Finding/cross-lane implication:** C011/C015; no new finding. C004's reciprocal NNT occurrence is in the same table but assigned to later row relationships.

## Shard completion

20/20 assigned relationships explicitly PASS_2_COMPLETE. New finding headings:0. All count, denominator, estimate/test, method, multiplicity and cross-source implications relevant to these relationships were revisited. Existing C005,C007,C011,C012,C013,C014,C015 are cross-referenced rather than re-emitted; S218 was independently screened as a precision-compatible source expansion, excluded from C008. No scientific source-reading gap in the assigned scope. Missing exact covariance/test/CI/weight/model definitions remain bounded per relationship. No raw-data reanalysis or preferred-method recommendation was made.
