# Numeric consistency review

Runtime agent 01a12bd6-46ce-7101-aa0e-61b820f40eb1, gpt-6.1-sol/medium, FRESH_SPAWN. Scope: every mapped quantitative numeric relationship in main REPORT11 pages, results REPORT25 pages and PLAN167 pages. Canonical inventory N001–N131 is complete; each relationship has an explicit check outcome. Controls were read fully. Canonical support-map lossless completion gate was confirmed before scientific checking. No web, old candidate/report conclusions or source modifications were used.

Four distinct findings below. Repeated sensitivity-header occurrences are consolidated. Exact source reproduction used supplied pdf_tools.py text with pinned PyMuPDF1.26.4 for mainp 8 and supplementpp19–23; fresh source render supplementp13,200 dpi,CPU,at preprocessing/numeric_checker-supp13.png was inspected visually. Sources are final authority; text derivatives are locator aids. No OCR required. Statistical-method checks beyond numeric arithmetic are also covered by the separate statistical reviewers and independent screening can consolidate overlapping findings.

## Findings

### F-NUM-001

**Title:** Ninety-day balloon-group mRS2 count and percentage do not reconcile.

**Relationships:** N055; within REPORT DOC-002, proposed relationship S_W, proposed review domain statistical_results; focus A.

**Exact source locations and document roles:** REPORT [results supplement PDFp13, FigureS4, BA row, mRS2 leader annotation and group header](../../../joi240088supp1_prod_1746815064.21247.pdf#page=13). Fresh direct render explicitly shows BAGroup(N=249), mRS2 “2.0 (N=50)”; other score annotations 205,36,2,0,0,1.

**Printed inputs and rule/calculation:** 50/249×100=20.0803%, compared with printed 2.0%. Printed inputs intervals 49.5–50.5 and 248.5–249.5 imply recomputed percentage 19.8397–20.3219%; printed 2.0 interval 1.95–2.05. Gap 17.7897 percentagepoints; relative discrepancy 17.7897/2.0=8.89485, above 0.05. Conversely 2.0% and 249 implycount 4.84575–5.11475, comparedwithprintedcount 49.5–50.5. Seven printed counts total 294, whereas groupheader 249; even conservative half-unit suminterval 290.5–297.5 vs 248.5–249.5 hasgap 41,relative 41/249=.16466. Allowing no negative counts strengthens that total gap.

**Qualifying route:** Route A, category 3. The apparent digit-based explanation is also consistent with category 2, but no production mechanism is assumed.

**Affected result or extracted value:** BA90-day mRS2 frequency and the complete 90-day ordinal outcome distribution.

**Why context does not resolve it:** RouteA category 3 always registers a reproduced count/denominator/percentage conflict within one display, even if a plausible intended count can be inferred. A reader extractingN50 obtains a materially different distribution.

**Alternatives and missing definition:** N5 would be approximately 2.0% and yield total 249; alternatively N50 could be the intended count and require a different percentage and distribution. Both are hypotheses; source gives no amendment at this location.

**Human question:** Which count, percentage and denominator should be used for BA mRS2 at 90 days, and what is the complete mutually exclusive BA score distribution?

### F-NUM-002

**Title:** Center-adjusted primary table prints a different balloon-group primary count under the same population header.

**Relationships:** N022,N086; REPORT DOC-001 versus REPORT DOC-002, proposed relationship S_C, proposed review domain statistical_results; focus A.

**Exact source locations and document roles:** REPORT [main PDFp 8, Table 2 primary row](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8) printsB11(4.4), n 249, M34(13.5),n 252; REPORT [results supplement PDFp19, TableS6 primary row and headers](../../../joi240088supp1_prod_1746815064.21247.pdf#page=19) printsB9(3.9),n 249,M34(13.5),n 252. TableS6 labels the analysis center-effect adjustment and specifies Cox treatment-effect adjustment for groups and centers. Primary composite definitions agree.

**Printed inputs and rule/calculation:** A model adjustment can alter a treatment-effect estimate but does not itself change the observed primary-event count under the same stated analysis population/endpoint. Count intervalsBmain 10.5–11.5 andS68.5–9.5 havegap 1,relative 1/11=.09091. Matching printed event percentages 4.4 interval 4.35–4.45 versus 3.9 interval 3.85–3.95 havegap.40 percentagepoints,relative.40/4.4=.09091. Both exceed.05. Within S6 alone,9/249 recomputation versus 3.9 has a small gap that does not exceed the mandated threshold; this finding rests on matching primary counts/copies, not that small percentage calculation.

**Qualifying route:** Route B.

**Affected result or extracted value:** Primary composite event count/incidence for the balloon group in the center-adjusted sensitivity analysis and its alignment with the main primary analysis.

**Why context does not resolve it:** B1 count/analysis-population comparison is in focus and involves primary efficacy. B2 neither table identifies a different denominator, eligibility set, endpoint definition or window that explains 9 versus 11. B3 extracting either 9 or 11 changes the primary balloon-event frequency. The printed 9(3.9) resembles a per-protocol summary, but no such population is identified in S6; that resemblance is an alternative, not resolution.

**Alternatives and missing definition:** S6 could contain an undisclosed subset or a count from a different analysis population, or its event summary could refer to another primary-count summary while HR0.32 comes from the stated full population. The table does not specify which.

**Human question:** What analysis population, primary-event count and observed incidence produced the center-adjusted TableS6 result, and how does its balloon count relate to 11/249 in the main primary table?

### F-NUM-003

**Title:** Sensitivity-analysis displays use population headers that do not reconcile with their stated populations and totals.

**Relationships:** N004,N005,N087–N089,N092. Proposed primary relationship S_C; all relationships S_C,S_W; REPORT main and results supplement; proposed review domain statistical_results; focus A. One repeated population-header pattern is consolidated across TableS7 and TableS8, retaining all affected header and component locations.

**Exact source locations and document roles:** REPORT [results supplement PDFp20, TableS7, both arm headers and both site-count rows](../../../joi240088supp1_prod_1746815064.21247.pdf#page=20) has headersB233,M238,site totals 256 and 245,and primary counts 4/19 and 7/15. REPORT [results supplement PDFp21, TableS8 per-protocol title, B249/M252 headers, primary and all three component rows](../../../joi240088supp1_prod_1746815064.21247.pdf#page=21) labels PPS while printing headers 249/252. REPORT [main PDFp 5, Figure 1 final per-protocol boxes](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5) givesB233,M238. REPORT [results supplement PDFp23, TableS10 per-protocol section](../../../joi240088supp1_prod_1746815064.21247.pdf#page=23) explicitly gives 233/238. No within-display TableS7 footnote identifies a different population behind the two site totals.

**Printed inputs and rule/calculation:** TableS7 armheaders sum 233+238=471, while its two mutually exhaustive site categories sum 256+245=501. Half-unit suminterval 470–472 versus 500–502 yieldsgap 28,relative 28/471=.05945> .05. TableS8Bheader 249 comparedwithsamePPpopulation 233 hasinterval 248.5–249.5 versus 232.5–233.5,gap 15,relative 15/249=.06024>.05; M252 comparedwith 238 gives 251.5–252.5 versus 237.5–238.5,gap13,relative 13/252=.05159>.05. All TableS8 primary/component counts 9/33,6/4,1/18,3/20 and percentages 3.9/13.9,2.6/1.7,.4/7.6,1.3/8.4 are preserved as affected display context. Those individual count/percentage recomputations against the headers do not independently exceed the half-unit display-precision threshold; the reproduced discrepancy is the population count itself and the TableS7 exhaustive totals.

**Qualifying route:** Route A, category 3 for TableS7 within-display totals; Route B for TableS8 matched per-protocol analysis-population sizes.

**Affected result or extracted value:** Arm denominators and population membership for the primary outcome's center interaction and per-protocol sensitivity analyses, including TableS8 all component frequencies.

**Why context does not resolve it:** TableS7 counts in one display qualify byRouteA regardless of a plausible header explanation. ForTableS8, finalPPsizes 233/238 versus 249/252 are result-relevant population counts that exceedprecision; the source gives competing denominator labels without indicating which applies to each reported sensitivity result. A reader can hypothesize copied header values but still cannot establish intended population from the printed sensitivity display alone.

**Alternatives and missing definition:** TableS7 may use full eligible population 501 with 233/238 headers fromPP; TableS8 may usePP233/238 with 249/252 headers fromthefullprimarypopulation. Alternatively eitherdisplaymay use additional undisclosedpopulation rules. No direct evidence establishes the production mechanism. TableS9ATS249/252 vs 247/254 is belowthreshold and is not part of this included pattern.

**Human question:** Which arm sizes and analysis populations apply to each TableS7 site row and to the TableS8 primary/component results, and how do the printed headers reconcile with the full and per-protocol participant counts?

### F-NUM-004

**Title:** One-year outside-territory stroke incidence difference lies outside its printed interval.

**Relationships:** N025; REPORT DOC-001, S_W, proposed review domain statistical_results; focus B.

**Exact source location and document role:** REPORT [main PDFp 8, Table 2, any stroke outside qualifying-artery territory within 1 year](../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8). Direct current-source text showsB3(1.2),M4(1.6),incidence difference−0.4(−2.4 to−1.7),HR0.76(0.17 to 3.40),P.72.

**Printed inputs and rule/calculation:** A point estimate must belong to its interval for the same stated quantity. −0.4 is greater than the printed upper bound−1.7, so it is outside[−2.4,−1.7]. Even half-unitintervals for the estimate[−.45,−.35] and upperbound[−1.75,−1.65] remain disjoint,gap 1.20; however RouteAcategory 1 does not permit treating interval/test conflicts as rounding. The interval also excludes 0 whilethe rowP.72 isnonsignificant and HRintervalcontains 1; different test attribution may be an alternative, but point containment alone is decisive for registration.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** One-year outside-territory stroke incidence-difference upper confidence limit, interval direction and its relationship to the point estimate/test.

**Why context does not resolve it:** Category 1 always registers a reproduced point-estimate/interval conflict. Reconstructing a plausible upper-bound sign from other rows cannot remove the printed reading.

**Alternatives and missing definition:** A positive upper bound could yield containment and a null-containing interval; the source does not identify another analysis for this printed difference interval. No replacement value is assigned.

**Human question:** What confidence interval belongs to the printed−0.4 percentage-point outside-territory stroke difference, and which analysis/test produced its interval andPvalue?

## Excluded observations

Only apparent discrepancies are listed; reconciled checks remain in the N inventory. Each row has exactly one reason code. The count-based FigureS5 death comparison alone has half-unitintervals touching; the separate cross-source reviewer evaluates the nonoverlapping 0.8%versus 0.4%copies, which are not screened out by the count-only observation.

| Location | Observation | Reason code |
|---|---|---|
| REPORT mainpp 1,4,6 | Age 58.0 is called mean inabstract andmedian inbody; sameprintednumber, summary-type wording alone establishes no numeric conflict. | TERMINOLOGY_OR_WORDING |
| REPORT mainpp 4–5 | Narrative attributes 11 exclusions towithdrawal whileflow gives 10 withdrawalsplus 1 unrecruitedallocation; flow immediately identifies reasons withoutchanging 501 analysis size. | CONTEXT_RESOLVES |
| REPORT mainp 4 | Male 343(69.1)of 501 vs 68.46%; maxrecomputed 100×343.5/500.5=68.6314,printedlower 69.05; gap.4186/69.1=.00606. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT mainp 6Table 1 female | B77(30.1)of 249 vs 30.92%; min 100×76.5/249.5=30.6613,printedupper 30.15; gap.5113/30.1=.01699. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT mainp 6Table 1NIHSS | M51(20.5)of 252 vs 20.24%; max 100×51.5/251.5=20.4771 overlapsprinted 20.45–20.55. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT mainp 6Table 1 stenosis | B25(10.4)of 249 vs 10.04%; max 100×25.5/248.5=10.2616,printedlower 10.35; gap.0884/10.4=.00850. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplementp 14S1 non-zone | B131(61.9)of 215 vs 60.93%; max 100×131.5/214.5=61.3054,printedlower 61.85; gap.5446/61.9=.00880. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplementp19S6 | Within-table 9(3.9)of 249 vs 3.61%; max 100×9.5/248.5=3.82294,printedlower 3.85; gap.02706/3.9=.00694. The cross-sourceprimarycountconflictisF-NUM-002. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplementp21S8 | Counts 9/33,6/4,1/18,3/20 againstheaders 249/252 haveindividualpercentagegapsbelowthreshold; largestremainingrelativegapfor 33(13.9)is(13.85−100×33.5/251.5)/13.9=.0381237753. PopulationheaderconflictisF-NUM-003. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplementp 22S9 vs p23S10ATS | Armheaders 249/252 vs 247/254 differby 2 each; half-unitgap 1/reference 249 or 252≈.004; allindividualpercentageswithinprecision. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplementp13S5 within-display | AMMcounts 169+58+13+3+3+1+2=249 vsheader 252; sevenhalf-unitinputintervalsoverlapheaderinterval. Individualpercentagesusing 252 alsohavegap≤.05 relative. Thisdoesnotexcludeaseparate 0.8%vs 0.4%deathcopycomparison. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT mainp 7 vs supplementp 17 | Arterialperforation 0.4%vs 0(0.0%)isaperipheralproceduralcrosscopy; nochangedprimaryresult,populationorplanneddecisionruleestablished. | PERIPHERAL_COMPARISON |
| REPORT mainTable 2HRs/subgroupHRs | Some CoxHRs differfromcrude count-risk ratios; displayexplicitlyusesCox/time-to-eventandprimaryPlogrank,soevent-countdivisiondoesnotreproduceHRidentity. | MODEL_VERSUS_CRUDE |
| REPORT supplementp24S11 | Disablingstroke 18Mvs 14 overallotherSAEsdoesnotestablishanexclusiveunion; nostatementthatthespecificstrokeendpointmustbecountedintheother-SAE summary. | CONDITIONAL_OR_UNREPORTED |
| PLAN pp 69,103,151,153 | Final 7%vs 15%implies 53.33%reductionversus 50%hypothesis; half-unitinputrangepermits 48.28–58.06%,overlaps 50±.5. | ROUNDING_OR_DISPLAY_PRECISION |

## Completion and limitations

All 131 stableNrelationships checked; 4 findings; 15 excludedobservations. Exact 203-pageunitcoverage is supplied by the complete new maps. Missing raw individual event times and continuous-score data limit numeric reconstruction to supplied displays; no missing-source unit. Stable S relationships and all statistical/planned analysis implications remain covered by statistical/cross-source specialists rather than inferred from unreported models. No finding cap or expected count was used. No source/reused artifact changed.

Final-audit annotation: exclusion row 9's S8 33/252 versus 13.9% relative residual was recomputed as (13.85−100×33.5/251.5)/13.9 = .0381237753. It remains below .05; the exclusion reason and separate population-header finding are unchanged. The original current-run diagnostic .03774 is preserved here as annotation provenance.
