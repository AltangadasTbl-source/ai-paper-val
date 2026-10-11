# Statistical consistency review — PASS 1 primary shard

Runtime agent: `/root/statistical_pass1`; exact model `gpt-6.1-sol`; reasoning effort `high`; fresh mandatory statistical pass1. Scope: S001-S100, every main inferential result and model, protocol statistical design/power relationship, report eTables2/4 and all inferential figure panels. Independent fresh high statistical extra shard covers eTables3/5/6, S121-S222, with its own durable findings/exclusions. The coordinator merges that shard; no scientific scope is omitted. This primary shard emits9 findings and10 excluded observations.

Read QUALITY_CONTROL_SCOPE.md and the1.6.2 review contract completely. Supplied PDFs and freshly reconstructed main/support maps are the scientific inputs. Source-linked reusable native/layout text locates evidence; direct Poppler26.01.0 source extraction confirms protocol pp26-36 and supplement pp15-18, and exact main source-page locators supply the printed main values. Direct source-linked main p6 and protocol pp26/28 images were visually inspected. New CPU derivatives: `statistics/protocol_statistical_direct.txt` and `statistics/supplement_outcomes_direct.txt`; commands/engine recorded in the relationship inventory. No web, earlier conclusion, raw-data or preferred-method audit, or unsanctioned Python was used.

## Complete check closure

S001-S041 preserve all printed within-group and between-group estimates, CIs, P values or SEs for Table2/eTable2/eTable4. S042-S056 preserve all remaining narrative contrasts and annual inferential figure panels, retaining every mapped visit without inventing unlabeled exact graph coordinates. S057-S100 check all supplied models, missing-data/IPW steps, population/contrast definitions, endpoint hierarchy, multiplicity/stopping rules and complete prospective power inputs. Every point/CI, endpoint order, direction and null decision is checked, including every nonsignificant row. No numerical CI-versus-P null-significance conflict appears within a tabulated row. The positive narrative HbA1c estimate versus its signed CI is retained under routeA1 despite its reduction-magnitude alternative.

Numeric group changes reconcile with surgery-minus-medical differences under half-unit rounding intervals, including Table2 LDL5.4 versus rounded5.3, eTable2 weight−8.4 versus rounded−8.5 and SBP.3 versus rounded.2. Binary ORs are model quantities, not crude risk/odds ratios. Exact P reproduction is constrained by unstated reported degrees of freedom, covariance and test distribution. Diagnostic normal/Wald approximations are labeled and do not replace the reported tests. One within-group binary interval does not reproduce the log-symmetric pattern of the other cells in the same display, with a greater-than5% discrepancy after complete rounding bounds.

Protocol primary H0 beta7=0 and two-sided.05 agree with the reported primary superiority direction, apart from the documented endpoint/model comparisons below. The package supplies no noninferiority, equivalence or formal efficacy stopping margin/rule. Secondary unadjusted endpoint comparisons and adjusted pairwise surgery comparisons are distinct families. Planning302×.8≈242 and the complete power graph sample sizes reconcile. Monte Carlo powers cannot be exactly recreated without implementation/allocation details; all printed inputs, formulas A1-A4 and TablesA5/A6 are retained. TableA6 has a labeled diagnostic event-based reproduction within display precision. Zero exact-coordinate inference is made from graphs.

## Findings

### F-ST1-001

**Issue:** The same year-12 HbA1c group contrast has different reported P values.

**Locations and roles:** REPORT [main p1 abstract](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1) and REPORT [main p3 Results](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), compared with REPORT [supplement p15 eTable2 HbA1c](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15); REPORT [supplement p4 primary model](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4) provides the model. Relationship S018; main/support matched main year-12 occurrence.

**Printed values:** Main difference−1.1%,95%CI−1.7% to−.5%,P=.002; eTable2 identical difference andCI butP<.001.

**Rule and calculation:** Match population, outcome, visit12, surgery-minus-medical contrast, ITT model and identical CI before comparing. P=.002 has rounding interval[.0015,.0025); P<.001 lies below.001. The intervals are separated by at least.0005, giving relative discrepancy at least.0005/.002=.25, above.05. Both individual results are significant, so this is a matched-P discrepancy, not a null-significance CI conflict. A normal approximation from this CI is diagnostic only; it is not used to choose a P value.

**Focus area:** B. **Proposed review domain:** statistical_results.
**Proposed relationship:** S_C. **All relationships:** S_C.
**Qualifying route:** Route B.
**Affected result or extracted value:** The abstract-reported year-12 HbA1c P value accompanying−1.1[−1.7,−.5]%.
**Why context does not resolve it:** The primary-follow-up contrast is directly extractable, both locations identify the same displayed estimate/interval, and neither assigns a different test or population to its P value.
**Alternatives and missing definition:** A different test distribution or updated report version could explain identical rounded intervals with different P values; the source does not identify that distinction. The article notes a July24,2024 correction but does not say that it accounts for this comparison.
**Exact human question:** Which P value and test belong to the reported year-12 ITT HbA1c contrast, and why does eTable2 printP<.001 while the abstract and narrative printP=.002?

### F-ST1-002

**Issue:** Planned relative-percent HbA1c change and the reported net-change primary result represent different quantities.

**Locations and roles:** PLAN [protocol p17 primary outcome](../../../../joi240004supp1_prod_1721756962.80052.pdf#page=17), PLAN [p26 A1](../../../../joi240004supp1_prod_1721756962.80052.pdf#page=26), PLAN [p27 hypothesis/power](../../../../joi240004supp1_prod_1721756962.80052.pdf#page=27), PLAN [p29 TableA1](../../../../joi240004supp1_prod_1721756962.80052.pdf#page=29); REPORT [main p2 primary outcome/methods](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), REPORT [main p6 Table2 footnoteb](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), REPORT [supplement p15 eTable2 footnote](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15) and REPORT [p4 model](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4). Relationships S001,S018,S057,S064,S069,S070.

**Printed values/statements:** Plan Y is percent change from baseline and power assumes surgical−20% atyear5 to−15% atyear7. Main methods likewise say percent change. Table2 specifically calls HbA1c “net change,” while other numeric outcomes use “relative changes.” Its primary M/B changes−.2/−1.6 and group−1.4[−1.8,−1.0]% are net changes; eTable2 gives−1.1[−1.7,−.5]%.

**Rule and calculation:** Relative percent change100×(follow-up−baseline)/baseline and net HbA1c percentage-point change follow-up−baseline are not the same scale. The protocol's−15% assumption and report's net-change footnote establish that this is a quantity-definition comparison, not a crude-versus-adjusted estimate comparison. No fitted effect is reconstructed from raw means. Rounding intervals/relative discrepancy are not applicable to competing quantity definitions.

**Focus area:** D, withC in report interpretation. **Proposed review domain:** protocol_report.
**Proposed relationship:** P_R. **All relationships:** P_R, S_C, S_W.
**Qualifying route:** Route B.
**Affected result or extracted value:** The scale and endpoint specification for the primary year-7−1.4% and year-12−1.1% HbA1c treatment contrasts.
**Why context does not resolve it:** The table establishes a net-change quantity while the prospective A1 response and report analysis label specify percent change. A reader cannot infer whether the planned model response changed or the methods label was used for the net response.
**Alternatives and missing definition:** A disclosed amendment or a shorthand use of “percent change” for change in an already-percent HbA1c variable could explain the report. The supplied plan's relative-change power assumptions remain distinct and no explicit response-scale amendment is given.
**Exact human question:** Was the primary model fitted to relative-percent HbA1c change or to net HbA1c percentage-point change, and how does the reported response correspond to the prospective A1 endpoint?

### F-ST1-003

**Issue:** The planned mixed-effects logistic main-secondary analyses are replaced by reported GEE analyses.

**Locations and roles:** PLAN [protocol p27 A2](../../../../joi240004supp1_prod_1721756962.80052.pdf#page=27); REPORT [main p3 methods](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), REPORT [supplement pp4-5](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4); results REPORT [main p6 remission/control rows](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6) and REPORT [supplement p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15). Relationships S012,S016,S017,S029,S033,S034,S058,S077.

**Printed statements/values:** A2 explicitly specifies patient-random-effect longitudinal logistic regression for glycemic control, remission and partial remission; beta7 logOR is the main secondary test. Reports explicitly use GEE with site/baseline HbA1c and sandwich standard errors. Remission is abstract-reported, including year7 OR3.39[1.25,9.17],P=.02 and year12 rates0/12.7%,P<.001.

**Rule and calculation:** Mixed-effects logistic regression with a patient random intercept and GEE are different stated analysis families, with different conditioning/estimand interpretations. Both may be coherent choices; the observation is the supplied planned-versus-reported replacement, not a preference. The planned model result is not reported. Numerical rounding intervals are not applicable to the model specification.

**Focus area:** D. **Proposed review domain:** protocol_report.
**Proposed relationship:** P_R. **All relationships:** P_R.
**Qualifying route:** Route A, category5.
**Affected result or extracted value:** Abstract-reported remission and primary glycemic-control secondary odds ratios, their population interpretation and planned analysis identity.
**Why context does not resolve it:** Category5 covers the planned key-secondary analysis that is replaced/not reported; remission is key by its abstract occurrence. Reported model details do not identify a supplied prospective amendment.
**Alternatives and missing definition:** An updated analysis plan may have selected population-average GEE effects in place of the prospective random-intercept logistic analysis. No such amendment or corresponding planned-model result is supplied. The exact GEE working correlation is not inferred.
**Exact human question:** Was the planned A2 mixed-effects logistic analysis performed, or replaced by GEE, and which model/estimand should the reported remission and control odds ratios represent?

### F-ST1-004

**Issue:** The supplied report does not contain the explicitly promised primary sensitivity-analysis package.

**Locations and roles:** PLAN [protocol p30 missing-data sensitivities](../../../../joi240004supp1_prod_1721756962.80052.pdf#page=30), PLAN [p31 censoring/postcrossover sensitivity](../../../../joi240004supp1_prod_1721756962.80052.pdf#page=31), PLAN [p34 baseline sensitivities](../../../../joi240004supp1_prod_1721756962.80052.pdf#page=34); REPORT [main p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3), REPORT [supplement pp4-6](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4), REPORT [p9 eFigure2](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=9). Absence was checked across the complete11-page main report and22-page result supplement, not solely the cited method paragraph. Relationships S044,S057,S060,S061,S079-S082,S086.

**Printed statements/values:** Plan says it will also perform MICE with Rubin combination, pattern-mixture dropout analyses, a final IPTW×censoring-weight sensitivity, an additional PP sensitivity discarding all postcrossover outcomes, and extra baseline HbA1c/BMI/imbalance-covariate sensitivities. Report describes random censoring/MAR and a truncated treatment-IPW analysis that reassigns exposure after crossover; its year7 primary sensitivity difference is−1.5[−2.1,−.9]%,P<.001. It supplies no results from the other promised primary sensitivities.

**Rule and calculation:** A planned primary sensitivity whose analysis/result is not reported qualifies independently of a missing non-key outcome. The report's stated IPW reallocation is not the additional operation of discarding outcomes after crossover, and its treatment-weight formula does not include the planned censoring-weight product. No claim that these analyses were never conducted is made. Numerical rounding is inapplicable to missing named analyses; all printed primary-IPW results reconcile.

**Focus area:** D. **Proposed review domain:** protocol_report.
**Proposed relationship:** P_R. **All relationships:** P_R.
**Qualifying route:** Route A, category5.
**Affected result or extracted value:** Planned sensitivity characterization of the primary year7 HbA1c contrast and its missing-data/crossover/covariate robustness.
**Why context does not resolve it:** Category5 covers planned primary analyses that are not reported. One reported sensitivity does not identify results of the independently named sensitivity operations.
**Alternatives and missing definition:** The analyses may exist in another unavailable report, may have been removed by a prospective amendment, or may have been conducted but omitted here. The supplied package does not identify which. This is one consolidated nonreporting pattern with every affected primary analysis retained.
**Exact human question:** Where are the planned MICE, pattern-mixture, censoring-weighted, postcrossover-censored and expanded baseline-covariate primary sensitivity results, or what supplied amendment explains their absence/replacement?

### F-ST1-005

**Issue:** The reported remission definition adds a medication-free duration to the supplied prospective definition.

**Locations and roles:** PLAN [protocol p18 remission](../../../../joi240004supp1_prod_1721756962.80052.pdf#page=18), PLAN [p29 TableA1](../../../../joi240004supp1_prod_1721756962.80052.pdf#page=29); REPORT [main p2 outcome definition](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=2), REPORT [p7 Figure3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=7), REPORT [p1 abstract remission](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1). Relationship S065 and all reported remission occurrences S012,S029,S050.

**Printed statements/values:** Plan remission=HbA1c<6.5% off diabetes medications; no duration is in either definition. Report requires HbA1c<6.5% without diabetes medications for at least3months and annual assessment. Key remission results are M/B6.2/18.2% at7years and0/12.7% at12years.

**Rule and calculation:** Compare the prospective endpoint window with the reported key-secondary endpoint. A minimum medication-free duration is a membership criterion, not a synonym for the HbA1c threshold. The plan's absence of duration is not treated as an explicit zero-month rule; the concrete additional report criterion is the observed difference. No event-count change is inferred without data. Numeric rounding is not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report.
**Proposed relationship:** P_R. **All relationships:** P_R.
**Qualifying route:** Route B.
**Affected result or extracted value:** Definition attached to the abstract-reported remission percentages and odds ratios.
**Why context does not resolve it:** The report's duration could exclude otherwise qualifying off-medication participants; the supplied prospective definition does not identify that window or an amendment. A data extractor cannot match the endpoints using the threshold alone.
**Alternatives and missing definition:** The duration may be an operational clarification based on a referenced later remission definition rather than a changed planned endpoint. References are supplied but no external source is consulted; the available protocol does not state this medication-free window.
**Exact human question:** Did the planned remission endpoint include the three-month medication-free requirement, and what prospective/operational specification defines the endpoint underlying the reported remission results?

### F-ST1-006

**Issue:** The protocol labels the site term fixed while the primary power calculation supplies a variance component for that term.

**Locations and roles:** PLAN [protocol p26 A1/site definition](../../../../joi240004supp1_prod_1721756962.80052.pdf#page=26), PLAN [p28 power inputs](../../../../joi240004supp1_prod_1721756962.80052.pdf#page=28), PLAN [p31 heterogeneity description](../../../../joi240004supp1_prod_1721756962.80052.pdf#page=31). REPORT [supplement p4 fixed-site model](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4) corroborates one side only. Relationships S068,S072,S083.

**Printed statements/values:** A1 specifies fixed site covariate and says b_i is a fixed site effect; patient c_ij is Gaussian random with sigma_c². Primary power explicitly says variance components estimated from fitting the current mixed model include sigma_b=.06,sigma_c=.15,sigma_e=.10,rho=.13 under A1. The p31 paragraph further describes site effects following a distribution and the final interval as describing heterogeneity.

**Rule and calculation:** A fixed site coefficient has no random-effect variance component under the stated A1 parameterization. A nonzero sigma_b listed as its variance component requires a definition or an additional random site term/distribution; none is supplied alongside A1. This affects the stated model used for primary power, rather than an exact claim that a simulated power is numerically unreproducible. Rounding sigma_b to[.055,.065) does not turn it into a defined fixed coefficient or identify its random distribution; numerical discrepancy ratio is not applicable to the parameter-type comparison.

**Focus area:** D/C. **Proposed review domain:** plan_material.
**Proposed relationship:** P_P. **All relationships:** P_P.
**Qualifying route:** Route B.
**Affected result or extracted value:** Primary HbA1c power-model specification and interpretation of the planned site-heterogeneity component.
**Why context does not resolve it:** The same primary model is explicitly cited for the power simulations, but its site term is assigned incompatible fixed/variance-component descriptions. The reported fixed-site model does not define the simulation parameter.
**Alternatives and missing definition:** sigma_b could describe empirical spread of fixed site coefficients or a separately simulated random site effect. Either requires the source to define the quantity and its role. The duplicated fixed site terms gamma^T Z and b_i alone are not a separate finding because the plan explicitly permits identifiability constraints.
**Exact human question:** What quantity does sigma_b=.06 represent in the A1 power simulations, and was the site effect fixed or randomly distributed in the planned analysis and simulation model?

### F-ST1-007

**Issue:** One within-group medication odds-ratio interval does not reproduce the log-symmetric interval pattern of the same display.

**Locations and roles:** REPORT [main p6 Table2, use of medications, medical change column](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6); comparator REPORT sameTable2 other binary within-group/group OR cells; REPORT [supplement p4 GEE/sandwich inference](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4). Relationship S013.

**Printed values:** Medical use-of-medications within-group OR0.10,95%CI0.01to3.27. Other binary cells include medical oral/GLP1 OR0.53[.29,.97], medical insulin OR1.93[1.07,3.46], medical HbA1c<7 OR2.77[1.38,5.54], surgical remission36.2[1.9,699.0] and every remaining binary Table2 interval.

**Rule and calculation:** A log-symmetric exponentiated interval has OR=sqrt(lower×upper). This method reproduces every other binary OR cell of the same display within half-unit input/estimate bounds, including all11 other within-group cells and all6 group cells. For the medical medication cell, the nominal center is sqrt(.01×3.27)=.1808314. Printed lower.01 permits[.005,.015), upper3.27 permits[3.265,3.275); hence the complete recomputed center interval is[.1277693,.2216416). Printed OR.10 permits[.095,.105). Gap=.1277693−.105=.0227693; relative discrepancy=.0227693/.10=.227693, above.05. Comparison is interval geometry under a reproducing display method, not a crude OR from baseline/year7 percentages.

**Focus area:** B/C. **Proposed review domain:** statistical_results.
**Proposed relationship:** S_W. **All relationships:** S_W.
**Qualifying route:** Route A, category4.
**Affected result or extracted value:** The medical year7-versus-baseline diabetes-medication odds ratio and its95%CI.
**Why context does not resolve it:** Category4 requires registration when a method reproduces the remaining rows but not the affected printed value beyond display precision. Unknown interval construction is the human question, not a reason to remove the printed mismatch.
**Alternatives and missing definition:** This cell could use a deliberately asymmetric interval procedure, different contrast, or a lower limit from another calculation. The report supplies GEE/sandwich standard errors but does not identify a distinct procedure for this cell. No particular corrected OR or bound is proposed. Its nonsignificant null conclusion and narrativeP=.19 do agree; the issue concerns interval geometry rather than significance.
**Exact human question:** Which interval construction or analysis produces OR0.10[0.01,3.27], and why is its log-scale center distinct from the log-symmetric pattern that reproduces the other Table2 binary intervals?

### F-ST1-008

**Issue:** Planned vascular/safety CMH analyses differ from the reported chi-squared/Fisher analyses.

**Locations and roles:** PLAN [protocol p34 Aim2 model](../../../../joi240004supp1_prod_1721756962.80052.pdf#page=34), PLAN [p35 continuation](../../../../joi240004supp1_prod_1721756962.80052.pdf#page=35); REPORT [supplement p6 methods](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=6), REPORT [p20 eTable5 footnoteb](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=20), REPORT [p21 eTable6 footnoteb](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21), REPORT [p17 nutritional comparisons](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17). Relationship S089; individual reported tests are independently covered by extraS121-S222.

**Printed statements/values:** Plan micro/macrovascular events use2×2tables compared with CMH and states safety major events/complications are analyzed in the same manner. Report percentages use chi-squared or Fisher exact tests; result footnotes repeat those families. Example reported tests include nutritional and safety comparisons, abdominal painP=.02 and dysphagiaP=.005 in eTable5; the exact source does not supply a CMH result.

**Rule and calculation:** CMH and ordinary chi-squared/Fisher are distinct explicitly named analysis families. The missing stratum definition does not erase the stated planned-versus-reported specification. No preferred test, implied site stratum or recomputed CMH P value is proposed. The extra shard reproduces the reported row tests under their reported families; this finding is the design/analysis comparison. Numerical rounding bounds are inapplicable.

**Focus area:** D. **Proposed review domain:** protocol_report.
**Proposed relationship:** P_R. **All relationships:** P_R.
**Qualifying route:** Route B.
**Affected result or extracted value:** Analysis identity/adjustment attached to reported adverse-event and safety P values and the abstract's cardiovascular comparison.
**Why context does not resolve it:** The prospective text links the safety endpoint analyses to CMH while the report assigns a different test family, without identifying a replacement specification. That difference can change the test interpretation attached to extractable reported P values.
**Alternatives and missing definition:** A revised plan may have allowed unstratified exact/chi-square analyses for sparse outcomes, or CMH may have been used for a separate composite while the listed row tests were additional analyses. The available sources do not state this mapping. The protocol does not explicitly name the stratum variable in this paragraph.
**Exact human question:** Which vascular/safety outcomes received the planned CMH analysis, with which strata, and what supplied specification maps those analyses to the reported chi-squared/Fisher row tests?

### F-ST1-009

**Issue:** The printed positive surgery HbA1c point estimate is outside its signed negative confidence interval.

**Locations and roles:** REPORT [main p1 abstract](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1), REPORT [main p3 Results](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3); corroborating REPORT [main p6 Table2 HbA1c](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6). Relationship S001, matched positive narrative occurrences.

**Printed values:** Abstract says HbA1c “decreased by1.6%” with95%CI−1.8%to−1.3%; narrative prints “difference,1.6%” with the same signed CI. Table2 prints−1.6[−1.8,−1.3] for surgery. Medical narrative/abstract also use positive0.2 reduction/difference magnitude alongside signed interval−.5to.2, while Table2 prints−.2.

**Rule and calculation:** The literal positive1.6 is not in[−1.8,−1.3]. For completeness, half-unit intervals positive point[1.55,1.65) and nearest negative upper bound[−1.35,−1.25) remain separated by at least2.80; relative to1.6 this is1.75. RouteA1 point-estimate containment is not a rounding-screen category. The medical point.2 is not independently outside its printed CI; it is retained only as a companion magnitude/signed-scale occurrence in the repeated pattern.

**Focus area:** B. **Proposed review domain:** statistical_results.
**Proposed relationship:** S_W. **All relationships:** S_W.
**Qualifying route:** Route A, category1.
**Affected result or extracted value:** The surgery year7 within-group HbA1c change and interval as printed in abstract/narrative.
**Why context does not resolve it:** Category1 always registers the literal point-versus-interval reading; the positive reduction-magnitude reading is explicitly an alternative. The table supplies a signed counterpart but does not change the positive printed point.
**Alternatives and missing definition:** The positive number may intentionally describe a reduction magnitude while the interval remains on the signed-change scale. This is immediate contextual evidence to preserve for human review, rather than an independent notation exclusion of the category1 observation.
**Exact human question:** Are the positive abstract/narrative points deliberate reduction magnitudes paired with signed-change intervals, or should the point and interval be read on a common signed scale?

## Excluded observations

Only apparent issues not emitted are listed; reconciling checks remain in S records.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC001 Table2/DOC003 eTable2, all model estimates; DOC001 Figures2/3 and DOC003 eFigures2/3/5/6 | Crude changes/odds from raw means, percentages or contributor counts differ from adjusted LS/GEE estimates; modeled baseline loss points may differ from raw zero-change values. Source does not identify those estimates as crude. | MODEL_VERSUS_CRUDE |
| REPORT DOC003 pp15-16 eTable2 footnotes | Several copied footnotes say year7 although the table heading, columns and remission footnote identify year12; the immediate display establishes the intended visit. | CONTEXT_RESOLVES |
| REPORT DOC001 p4 narrative versus p6 glycemic-threshold row | Narrative HbA1c≤6.5 versus table HbA1c<6.5 symbol in the same matched P=.002 result; no changed printed value or boundary-subgroup result supplied. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC003 p13 eFigure6 caption versus DOC001 p7/SAP BMI analysis | BMI>35 caption versus ≥35 complement of <35 analysis; no affected boundary participant or changed result identified. | NOTATION_OR_TYPOGRAPHY |
| PLAN DOC002 pp26-27 A1 | Both gamma^T Z and b_i represent fixed-site terms, but the source explicitly permits coefficient constraints for identifiability. This is distinct from the emitted power variance-component comparison. | CONTEXT_RESOLVES |
| REPORT DOC003 pp5-6 GEE missingness assertion | General MAR handling cannot be reconstructed from GEE/sandwich description alone without the outcome/observed-case mechanism or missingness-weight implementation. No raw mechanism or conflicting numeric estimate is supplied; the concern depends on an unstated mechanism. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC002 p28 glycemic-control power projection | Diagnostic ordinary linear fit of logits to75/63/48% preliminary surgery rates predicts about34% atyear7 rather than assumed39%; source does not specify a fit to those points or require them as exact constraints. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC002 pp18,27,31-36 and61-63; complete REPORT DOC001/DOC003 | No supplied report results for non-key QOL/UKPDS/BMI, descriptive relapse, exploratory taxonomy/predictor models or ancillary ICER; absence alone does not establish missing primary/key-secondary analysis or a prespecification claim. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC002 p35 TableA5 footnote | Common SD is described as a covariance diagonal element; nearby SD6% and standardized-effect definition make the intended dispersion quantity clear without a changed printed estimate. | TERMINOLOGY_OR_WORDING |
| REPORT DOC003 p18 eTable4 calcium/albumin | Calcium contrast SE0.0 is one-decimal rounding, not established zero variance; albumin point/SE rounded inputs permit P=.72. These apparent point/SE/test mismatches vanish under complete display intervals. | ROUNDING_OR_DISPLAY_PRECISION |

## Limitations and handoff

No scientific-coverage gap in S001-S100. Exact graph coordinates, model covariance/df/test distributions and Monte Carlo implementation are not printed; these limits are named in every affected record. No exact alternate P, site strata, predictor censoring rule or estimand mapping is inferred from convention. All9 findings require independent inclusion screening. The independent extra shard has102 relationships,0 findings and1 excluded rounding pattern and will be merged by the coordinator. The statistical second pass must use a different fresh runtime agent and reread every S record plus the complete ledger/screen/recheck and every checker exclusion.

