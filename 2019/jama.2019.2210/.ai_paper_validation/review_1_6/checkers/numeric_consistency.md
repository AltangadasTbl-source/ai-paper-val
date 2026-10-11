# Canonical numeric consistency review — complete disjoint union

The coordinator losslessly merged two distinct fresh medium-effort numeric agents: N001-N120 main scope and N121-N220 remaining main/support scope. All 220 relationship bundles and their individual printed components were checked. The original disjoint main part is preserved in checkers/parts/numeric-main.md; the independent support part is preserved in checkers/numeric_support_consistency.md. Thirteen checker-local emissions are retained here before genuine duplicate merging with other lanes into stable candidates. The original source-grounded reasoning follows unchanged.

## Original main shard

Runtime UUID: 01a12868-d20d-7603-b09d-5a1375e78ae9. Model/effort: gpt-6.1-sol/medium, fresh numeric-reviewer spawn, current authorized provider. Assigned scope: DOC-001 M001–M120, physical PDF pages 1–7, REPORT. N001–N120 contain all printed components and repetitions; 120 relationships checked, six distinct candidates emitted. M121–M134 and support documents are assigned to the independent numeric support shard. No stable candidate IDs or adjudications are assigned here.

Read completely: QUALITY_CONTROL_SCOPE.md, workflow_1_6/review_contract.md, extraction/main_quantitative_evidence.md. Scope is exact quantitative-reporting consistency; participant timing qualifies below because it conflicts with a reported IQR. All sources and reused derivatives preserved. Source-linked reusable native/layout locators for pp.1–7 inspected; reusable images pp.5,7 visually inspected; fresh direct-source Poppler pdftotext layout pp.2,4,5,7 stored in preprocessing/numeric-main-p2.txt, numeric-main-p4.txt, numeric-main-p5.txt and numeric-main-p7.txt. No OCR needed. No old candidate or report conclusions, external evidence, web or extra Python used.

## Completed checks and noncandidate relationships

Every N row in relationships/numeric_relationship_inventory.md records its printed inputs, location and applied check result. All arithmetic, count bounds, mutually exclusive category totals, percentage precision, missingness, measured versus randomized population identity, reference-group/direction, measures, units, rates versus risk/count distinctions, repeated values, interval containment and printed risk-array components were checked. Integer percentages use 0.5 percentage-point tolerance; one-decimal percentages use 0.05; exact count/identity comparisons have zero tolerance. The six candidates below are the complete emissions, with no count-based stopping.

All efficacy count percentages reconcile, as do death partitions. All subgroup and pooled risk arrays have correct baseline identity, nonnegative nonincreasing counts, nonnegative subgroup residuals and ordered corresponding endpoint populations. At-risk counts are not event counts. Five-year survival percentages are censoring-dependent estimates and need not equal crude fractions. Change ratios of paired participant values need not equal ratios of aggregate medians, so 87% versus (41−21)/21 is not a candidate. A mean age66 and median age66 can coexist; no age-summary mismatch inferred. BMI totals249/165 are below randomized251/166; missingness without a concrete percentage mismatch is not alone a candidate. Genotype percentages use measured category totals; applying randomized totals wholesale would manufacture discrepancies. Rounded category percentages need not sum to100%, as the source footnote states. No display-zero P value appears. Inferential interval/P-value calculations requiring unprinted model/test conventions are reserved to the independent statistical lane; CI order, containment and narrative direction were checked here.

## Candidate NM-01 — vitamin D middle-baseline percentage

Relationship: N051,N052,N053,N022. Proposed primary category: Denominator, proportion, or total inconsistency.

Compared locations and document roles: REPORT [main article p.5 Table1 baseline25(OH)D rows](../../../jama_urashima_2019_oi_190023.pdf#page=5), with REPORT [p.4 baseline subgroup totals](../../../jama_urashima_2019_oi_190023.pdf#page=4) and REPORT [p.6 missing baseline statement](../../../jama_urashima_2019_oi_190023.pdf#page=6). The discrepancy is internal to one REPORT.

Printed inputs: vitamin D low102(41), middle142(58), high4(1.6); randomized D251. Placebo71(44),90(56),1(0.6); total randomized417; seven missing baseline levels; pooled measured groups173,232,5.

Reproducible rule/calculation: mutually exclusive low/middle/high measured categories total102+142+4=248. 100×142/248=57.2580645%, differing from58% by0.7419355 percentage point, beyond integer-rounding tolerance0.5. Randomized denominator251 yields56.5737%, also not58%. All displayed category counts total410 and seven missing reconcile417. This registers the individual142(58) cell, not the rounded percentage-column sum.

Direct observation: source prints142(58) and exhaustive category counts. Derived inference: 248 is the category-based measured denominator, not an explicitly printed arm-specific denominator. No claim is made about cause. Alternatives: a different percentage-specific denominator, a count transcription, or a nonstandard rounding rule might explain the cell; excluding high produces244 and58.1967% for middle, but would yield41.8033% for low rather than printed41%, so it does not give one coherent denominator for the low/middle pair.

Quality-control relevance: the inconsistent count/percentage can be propagated when extracting baseline subgroup composition. Exact human question: What denominator and rounding rule were used for the vitamin D middle25(OH)D cell, and should its count or displayed percentage be reconciled with the complete baseline category totals?

## Candidate NM-02 — placebo ApaI GT percentage

Relationship: N064,N065,N066. Proposed primary category: Denominator, proportion, or total inconsistency.

Compared locations and document roles: REPORT [main article p.5 Table1 continued, ApaI GG/GT/TT placebo cells and rounding footnote](../../../jama_urashima_2019_oi_190023.pdf#page=5). All compared content is REPORT in the same document.

Printed inputs: placebo ApaI GG69(46), GT61(40), TT20(13); header placebo n166. Vitamin D corresponding counts96,104,31 are not substituted for placebo.

Reproducible rule/calculation: 69+61+20=150 measured genotype counts;100×61/150=40.6666667%, differing from40% by0.6666667 percentage point, beyond0.5 tolerance. The other placebo cells69/150=46.0% and20/150=13.3333% reconcile46 and13. Randomized166 gives36.7470%, not40%. A percentage total99% alone would be allowed; this observation concerns the individual61(40) pair.

Direct observation: all counts/percentages printed as above, confirmed by direct layout text and visual locator. Derived inference:150 is the measured-category denominator. Alternatives: genotype-specific percentage denominators, truncation rather than nearest rounding, or a count/percentage transcription. Uniform truncation does not explain all genotype percentages, but rounding details are not assumed conclusively.

Quality-control relevance: a mislabeled genotype frequency could enter subgroup summaries or systematic evidence extraction. Exact human question: Does placebo ApaI GT use the common measured denominator150, and what source count, denominator or rounding rule accounts for the printed40%?

## Candidate NM-03 — Table2 hazard-ratio direction footnote

Relationship: N104 with N086,N094,N009. Proposed primary category: Measure, label, or scale inconsistency.

Compared locations and document roles: REPORT [main article p.7 Table2 footnotea and relapse row](../../../jama_urashima_2019_oi_190023.pdf#page=7); REPORT [p.6 competing-risk result narrative](../../../jama_urashima_2019_oi_190023.pdf#page=6); REPORT [p.3 statistical model and treatment description](../../../jama_urashima_2019_oi_190023.pdf#page=3). All are one REPORT.

Printed inputs: Table2 footnote says “Hazard ratio (HR) values greater than 1 indicate that vitamin D supplementation was associated with a decreased probability of the outcome.” Relapse rows include total subdistributionHR0.75(0.48–1.17) and middle0.44(0.21–0.89). P.6 says middle cumulative incidence is significantly lower in vitamin D than placebo with0.44. Main results consistently describe vitamin D compared with placebo.

Reproducible rule/calculation: for the stated vitamin-D-versus-placebo event-hazard contrast, ratio above1 is larger vitamin D event hazard and ratio below1 is smaller. The source itself pairs0.44<1 with lower outcome incidence, while the universal footnote pairs>1 with decreased probability. Ratio direction is an exact label/contrast comparison with zero numerical tolerance; probability and hazard are not equated numerically.

Direct observation: conflicting sign wording and printed effect/narrative. Derived inference: applying the article's treatment contrast to the universal footnote. Alternatives: the footnote might intend an inverse reference contrast or a complementary favorable endpoint, but neither is named and the table endpoints are relapse and death.

Quality-control relevance: the direction label could reverse interpretation during evidence reuse even though results narratives give the intended direction. Exact human question: What treatment reference group and outcome direction does footnotea intend, and how should the greater-than1 statement be reconciled with the reported lower relapse incidence atHR0.44?

## Candidate NM-04 — Figure3C risk-table presence versus caption

Relationship: N114,N116. Proposed primary category: Numeric or arithmetic inconsistency.

Compared locations and document roles: REPORT [main article p.7 Figure3 panelC and its caption](../../../jama_urashima_2019_oi_190023.pdf#page=7); same REPORT.

Printed inputs: panelC “Death, baseline25(OH)D level20–40ng/mL” has “No. at risk” placebo90,88,70,51,34,22,11 and vitaminD142,139,115,88,61,41,20 at years0–6. Caption says “Numbers at risk for panel C are not given because of weighting.”

Reproducible rule/calculation: caption claims an absent table while directly displayed panelC has two rows of seven numeric risk counts. Presence/identity comparison uses zero tolerance; no values are digitized from curves or converted from weights.

Direct observation: labeled panelC contains the printed risk rows, and caption states none given. No unreported weighting method is inferred. Alternatives: the caption could name the wrong panel, or rows may be unweighted counts while a distinct weighted risk quantity was intended; the caption does not distinguish those quantities.

Quality-control relevance: a reader extracting cohort risk counts or interpreting weighted displays faces conflicting guidance about the displayed numbers. Exact human question: Does the caption refer to this panelC and these risk rows, and are the displayed counts the intended numbers at risk or a different unweighted quantity?

## Candidate NM-05 — pooled stageII narrative percentage

Relationship: N020,N046 with N045,N047. Proposed primary category: Denominator, proportion, or total inconsistency.

Compared locations and document roles: REPORT [main article p.4 Study Population stage distribution and n417](../../../jama_urashima_2019_oi_190023.pdf#page=4); REPORT [p.5 Table1 cancer-stage counts](../../../jama_urashima_2019_oi_190023.pdf#page=5). Same REPORT.

Printed inputs: body states “Disease stages were I, II, and III in44%,26%, and30% of patients, respectively.” Table1 stageII vitaminD63 and placebo48; stageI115/67, stageIII73/51, arm totals251/166.

Reproducible rule/calculation: all stage counts sum251+166=417. Pooled stageII63+48=111;100×111/417=26.6187050%. Difference from26% is0.6187050 percentage point, beyond integer rounding tolerance0.5. StagesI182/417=43.6451% andIII124/417=29.7362% round44 and30. An unweighted average of arm percentages(25+29)/2=27% also does not yield26%.

Direct observation: printed stage counts and pooled percentage. Derived inference: the statement's denominator is all417 described in the same population paragraph, supported by exhaustive stage table sums. Alternatives: a different stage definition or population, a count transcription, or truncation for this percentage. Uniform truncation would not reproduce44%/30% for the other stages.

Quality-control relevance: pooled stage mix can be copied into baseline comparability or evidence tables. Exact human question: Are the narrative stageII percentage and Table1 stageII counts based on the same417 participants, and what denominator or rounding rule reconciles26% with111 participants?

## Candidate NM-06 — postoperative randomization window versus reported IQR

Relationship: N003,N019. Proposed primary category: Numeric or arithmetic inconsistency.

Compared locations and document roles: REPORT [main article p.2 Trial Design statement](../../../jama_urashima_2019_oi_190023.pdf#page=2); REPORT [p.4 Study Population postoperative randomization timing](../../../jama_urashima_2019_oi_190023.pdf#page=4). Same REPORT. This is a concrete timing-summary inconsistency rather than a general participant-flow/design criticism.

Printed inputs: p.2 says “in this study, patients who did not meet exclusion criteria were randomized and started supplementation at the first outpatient visit between2 and4 weeks after operation.” P.4 says participants randomized and started medication at median23.5(IQR13–44)days after operation.

Reproducible rule/calculation:2–4weeks=14–28days. If the p.2 statement is the realized inclusion window, every observed timing, hence its lower/upper quartile, must be within[14,28]. Printed quartiles13 and44 lie outside: lower1day earlier, upper16days later. Even interpreting integer IQR bounds with±0.5day display tolerance does not put44 inside28. Week wording may be approximate; this is preserved as the human question.

Direct observation: fixed-seeming trial timing statement and actual IQR. Derived inference: converting weeks using7days/week and applying the bounded-observation property of quantiles. Alternatives: p.2 may summarize intended/usual scheduling rather than a strict observed window; allowed clinical deviations could explain timings without contradicting the actual IQR. No adherence, eligibility or protocol-violation judgment is made.

Quality-control relevance: timing windows and timing dispersion can be reused in trial summaries and population comparisons; the apparent realized-window statement can misdescribe the reported distribution. Exact human question: Does “between2 and4weeks” describe a strict realized randomization range or intended/usual scheduling, and what wording or numeric definition reconciles it with IQR13–44days?

## Limitations and completion

No missing scientific unit within assigned M001–M120. Denominators for some measured subsets, exact change-ratio summary definition and full statistical covariance/test conventions are not printed in assigned pages; absent definitions alone generated no candidate. All six candidates retain source-grounded alternatives and exact unresolved questions. Fresh complete direct-source recheck is mandatory before coordinator classification/report assembly. Candidate count6; relationship count120. All remain Pending Human Adjudication.

# Complete supplementary numeric consistency check

Fresh numeric shard; runtime 01a12869-0016-7623-8936-bbcb5dbab14a; gpt-6.1-sol/medium. Scope COMPLETE: M121–M134, U001–U087; canonical N121–N220, 100 relationship bundles; 7 distinct document-grounded candidate observations. No stable candidate IDs, severity, validity, adjudication or dispositions assigned. Exact rules and roles accompany each observation. Source evidence and reusable derivatives preserved. Current provider retained. No web, old scientific conclusions, extra Python, or GPU used.

Full input register: relationships/numeric_support_inventory.md and complete fresh mapper transcriptions. Direct fresh derivatives: preprocessing/numeric-support-main-p8.txt (Poppler pdftotext 26.01.0, layout, main physical page 8); preprocessing/numeric-support-results-p4.txt (same engine, results physical page 4); preprocessing/numeric-support-plan-p23.png (Poppler pdftoppm 26.01.0, PNG, scale-to1600, PLAN physical page 23, visually opened). Existing PLAN native/layout files are direct fresh extractions for all 45 pages. Numerical calculations below use printed values; no model estimated from unsupplied data.

## Complete main numeric scope N121–N134

N121: calcium medians and IQR order checked: vitamin D 9.3[8.9,9.6] to9.3[9.1,9.6] mg/dL, P=.09; placebo9.3[9.0,9.6] to9.3[9.1,9.5],P=.44. All medians lie within quartiles. Identical marginal medians do not imply identical paired measurements or P=1. N122: median change ratios0%,0%,between-armP=.10 coherent; marginal median percentage change is zero but not a substitute for the printed paired summary. No candidate.

N123–N126: all 24 Table3 count/percentage pairs checked using exact stated populations. Column order is until-censoring D/P, adherent1year D/P, randomized D/P. Denominators227/147/243/160/251/166. Raw reproduced percentages:

| ID | Printed counts | Printed percentages | 100×count/denominator percentages | Numeric result |
|---|---|---|---|---|
| N123 | 3/5/3/6/3/6 | 1.3/3.4/1.2/3.8/1.2/3.6 | 1.32159/3.40136/1.23457/3.75000/1.19522/3.61446 | All reconcile at0.05point tolerance, including exact3.75 tie |
| N124 | 2/0/4/2/4/4 | .9/0.0/1.6/1.3/1.6/2.4 | .88106/0/1.64609/1.25000/1.59363/2.40964 | All reconcile, including exact1.25 tie |
| N125 | 19/9/20/13/21/15 | 8.4/6.1/8.2/8.1/8.4/9.0 | 8.37004/6.12245/8.23045/8.12500/8.36653/9.03614 | All reconcile |
| N126 | 15/8/16/9/16/9 | 6.6/5.4/6.6/5.6/6.4/5.4 | 6.60793/5.44218/6.58436/5.62500/6.37450/5.42169 | All reconcile |

N127–N128: six population labels/denominators and footnotes checked against every cell. Nonadherent lost vitaminD participant is excluded from per-protocol groups. Per-protocol sets are subsets of randomized groups:227≤243≤251,147≤160≤166; every outcome count nondecreasing over those sets. Fracture/stone/severe-event/de-novo rows need not sum because outcomes can overlap; no supplied mutually-exclusive assertion. Severe adverse events require admission, de novo organs differ from primary; no rate/person-time label. N129: per-protocol fracture and stone counts/percentages exactly repeated in abstract and adverse-event prose; hypercalcemia zero is a participant-event statement and no conflicting count supplied. No candidate.

N130–N132: all background numbers read (70% lower,20ng/mL,400IU/d7years,1100IU/d;155/1200IU/d,64studies/44165participants,8cohorts;25871/2000IU/d,3otherRCTs). No within-package matched inconsistent numeral, additive requirement or inferential statistic supplied. Do not infer trial counts from outside cohorts. N133: approximately10% stopping,5high baseline,7missing,20/40 cutoffs,1–6month surveillance and5year conclusion retain distinct populations.7missing=3+4 from eTable2; missing7 is not the4 omitted from average-over-follow-up eTable1. N134: bibliographic/date/funding identifiers carry no clinical arithmetic; COMPLETE NOT_APPLICABLE.

## PLAN numeric scope N135–N160

| ID | Exact check applied to every component | Result / observation |
|---|---|---|
| N135 | CC21.4/CT12.1/TT15.6months and log-rank.005 repeated pp.3,6,18,21–22; unit and genotype alignment | Exact repetitions coherent; no test reconstructed without participant inputs |
| N136 | Initial1200IU objectives pp.3,7,8 versus2×600IU/day p.9 | 1200=2×600, coherent |
| N137 | Initial2capsules/day p.4 and600IU p.9 versus1000IU/capsule p.12;366capsules/bottle | Candidate NS-A;366/2=183days, no printed annual bottle-duration claim |
| N138 | Final2000IU pp.18,23;2×1000 p.25;2daily p.19;1000capsules366/bottle p.28; change p.45 | 2000=2×1000;366/2=183days; disclosed1200→2000 change alone no candidate |
| N139 | Planned400=240+160,240/160=1.5=3/2,allocation60/40%; initial and final summaries | Exact target counts agree; actual417 is distinct achieved enrollment |
| N140 | Stop>400 pp.3/18 versus after400 p.31; ID400follow2years | Boundary language differs but achieved417 could reflect concurrent entry; no internal count contradicted by these design instructions alone |
| N141 | 50+50+10=110annual cancers,80recruits/year×5=400;5+2=7years | Recruitment subset80≤110; all arithmetic coherent |
| N142 | Initialtarget400p.3 versus blank calculation headingsp.14 and amendmentp.45 that sizewasblank | Candidate NS-B |
| N143 | Final printed Freedman log full inputs/output p.30 | Details below; all displayed arithmetic coherent |
| N144 | Annual after200,interimP<.001 versus finalP<.05; firstmidterm timingp.45 | Different decision stages; no numeric contradiction; no inference from missing interim results |
| N145 | Wilcoxon signed-rank change; t/Mann–Whitney distribution distinction; chi-square dichotomous | Units/roles distinct; no incompatible printed test statistic in assigned scope |
| N146 | ITT/KM/CoxHR95%CI,RFS/OS,two-sided.05,Stata14.0 | HR measure and endpoint labels preserved; follow-up durations not person-time rates |
| N147 | PlannedRR for relapse/safety; mainTable3counts/% only | Count/proportion table does not claim RR; cross-source inferential matching assigned to cross lane |
| N148 | Multiplicative interactions,no correction;5VDR,2DBP; amendments |5namedVDRmarkers+2DBP exact; distinct interaction from treatment-effectP |
| N149 | RFS event earliestrelapse/death; censor no-relapseANDalive pp.9/25 versus OR pp.13/29 | Candidate NS-C; concrete endpoint/event-versus-censor label mismatch |
| N150 | OS all-cause-death,alivecensor,supplement-origin,lastoutpatient pp.9–10/13/25/29 | OS wording coherent; no event count supplied in PLAN to derive new observed number |
| N151 | Finalde-novo notoutcome p.19 versus tertiaryoutcomep.25 and amendmentp.45; nonprimary-deathformp.41 | Candidate NS-F; primary cancer death versus new-primary death distinction itself coherent |
| N152 | Annual calendar-matched25(OH)D,−80°C pp.11/27; annualp.13/28; biochemical25(OH)D distinct1,25(OH)2D | Timing and units coherent; no exact printed box summaries to recalculate |
| N153 | Baselinelow<20,middle20≤x≤40,high(40)p.23 versushigh>40p.31 | Candidate NS-D; missing inequality visually confirmed |
| N154 | Historicalrs7041T-homozygote25%reduction/P<.0001 p.22,DBP1rs7041/DBP2rs4588p.27 | No supplied comparator serum mean or duplicated conflicting effect; no test reconstructed |
| N155 | FokI/BsmI/CDX2/ApaI/TaqI identifiers repeatedpp.12/27; PCRlabels p.36 | Named marker repetitions coherent; strings not numerical effect estimates; CDK2resultlabel addressedN220 |
| N156 | Age30–90 pp.9/24 versus30≤age<90p.38 | Candidate NS-E, conditional age90boundary label |
| N157 | ClinicalI–III/pathological0,IVexclusions; stageII/IIIchemotherapydistinctions | No inconsistent printed numerical outcome caused by clinical/pathological distinction; no broad design candidate |
| N158 |10permutations×5positions,each3A2P; random1–10;3:2 | All50positions checked; sequencesAAAPP,AAPAP,AAPPA,APAAP,APAPA,APPAA,PAAAP,PAAPA,PAPAA,PPAAA;10unique=choose(5,2),30A20P |
| N159 | Annual>11months versus<11months pp.42; self-reportedcompliance/withdrawal | Exact11unassigned in form, but no affected reported numeric count identified; no qualifying candidate solely for operational form incompleteness |
| N160 | Versionlabels/dates and amendments p.2/17/45 | FinalVer.1versusver.3/date and12.8versus12.18administrative ambiguity; no concrete clinical numeric result mismatch established; no candidate |

N143 reproduced calculations using printed p.30: log(.75)/log(.62)=.6018002666, matching hazardratio.6018 within0.00005. Allocation1.5 givesp1=1/(1+1.5)=.4 and160/240,total400. Event probability=.4(1−.62)+.6(1−.75)=.302. Freedman planning diagnostic with normal quantilesz.975=1.959964,z.80=.841621 givesE*=(z.975+z.80)^2(1+1.5×.6018003)^2/[1.5(1−.6018003)^2]=119.4690; sampleE*/[.302×.99]=399.59, rounding upward to400. E=120 is rounded planning count; rounding E first and independently regeneratingN would double-round. N400×.99×.302=119.592 rounds120. Printed surv75/62percent,alpha5%,power80%,withdrawal1%,N400 and split160/240 all coherent. No candidate from software log spaces or rounding.

Complete additional PLAN units: safe200–2000IU/dayp.15/32 contains both1200and2000 doses; insurance100000000/personand300000000/trial is administrative and not a3participant limit; PCRp.36 all initial/step temperatures98/95/94/93,annealing68/59/62/66/55,extension72,stopping16°C and30/30/35/35/25cycles have explicit°C,s,minunits and no independently asserted summed duration. Blood samplingfasting/within2h/within4h are selectable clinical fields with no reported frequencies; illustrativeMarch1–June26,2012death date is chronologically afterrelapse and not an observed participant event. No substantive numeric field ignored.

## Results numeric scope N161–N220

N161–N176 independently cover all16 eTable1 nonreference outcome×model×concentration results. Inputs by averagegroup, orderedRFSHR/AHR then deathHR/AHR:

| N IDs | Group | All four printed HR[95%CI],P |
|---|---|---|
| N161–N164 |20–<30 | .62[.37,1.02],.06; .61[.37,1.01],.05; .66[.35,1.24],.20; .64[.34,1.20],.16 |
| N165–N168 |30–<40 | .47[.27,.84],.01; .44[.24,.82],.009; .39[.18,.84],.02; .33[.15,.74],.007 |
| N169–N172 |40–<50 | .29[.11,.74],.01; .26[.10,.71],.008; .44[.17,1.16],.10; .34[.12,.96],.04 |
| N173–N176 |≥50 | .44[.21,.96],.04; .40[.18,.92],.03; .55[.24,1.29],.17; .43[.17,1.08],.07 |

All16 have positiveHR,orderedpositiveCI,containpointestimate and explicitly use<20reference; AHR adjusts supplementation, not an alternative outcome or serum unit. No numeric label contradiction. P=.05 with upper1.01 is not independently contradictory at displayed precision or without the exact test/CI convention; statistical lane receives all inferential tuples. HRs are serum-group associations pooling randomized arms, not active/placebotreatmentHRs. CIs/Ps not recalculated as observed analysis.

N177–N180: eTable2 fourMI effects independently checked: lowRFS1.15[.65,2.05],.63; lowdeath1.36[.66,2.81],.41; middleRFS.46[.24,.86],.02; middledeath.60[.28,1.30],.20. Allpositive,ordered,containestimate; middleRFS below1 bothends,otherscross1. No number of imputation draws or variance rule supplied; differing complete-case effect is not a numeric contradiction by itself.

N181–N215 cover every subgroup risk-array component and inference label, full inputs in appendix below (35rows×8riskentries=280numbers). At0/2/4/6years every count nonnegativeinteger and each arm's fournumbers nonincreasing. No at-risk array adds participants over time. Every estimableHRpositiveandinsideorderedCI, P/Pinteraction between0and1. N195/TaqICC hasHR/CI/interactiondasheswithP1.00 and riskarrays4/2/1/0,5/3/3/1; numeric lane does not infer a contradiction from unspecified nonestimability/test. Curves' upperlimits .60,.80,1.00,1.60,2.00 are cumulativehazardaxis values and may legitimately exceed1; not percentages. Latecurveordering need not equal a wholefollow-upCoxHRdirection. Exactcurvecoordinates are absent, so no numerical claim is fabricated from smooth curves.

Cross-panel subgroup sum checks at each common time (DthenP):

| Subgroup partition / exact results pages | D summed0/2/4/6 | P summed0/2/4/6 | Arithmetic interpretation |
|---|---|---|---|
| Sexpp.28–29 |251/176/93/35 |166/113/54/16 | Exhaustive, alltimes matched with age/stage/histology |
| Agepp.30–31 |251/176/93/35 |166/113/54/16 | Exhaustive, ≤65versus>65, matchessex |
| Stagepp.37–39 |251/176/93/35 |166/113/54/16 | I+II+III matchessexexactly |
| Histologypp.40–41 |251/176/93/35 |166/113/54/16 | Adeno+nonadeno matchessexexactly |
| Cancer sitespp.34–36 |250/175/92/34 |165/112/54/16 | Smallintestinal1perarm omitted from these3sitepanels, not a fabricated total mismatch |
| BMIpp.32–33 |249/174/92/35 |165/112/53/16 | MissingBMI2D/1P; sums≤allparticipants at eachtime |
| FokIpp.7–9 |245/174/93/35 |157/108/53/16 | Genotypedsubset, sums≤allparticipants at eachtime |
| BsmIpp.10–12 |231/162/92/34 |150/104/51/14 | Genotypedsubset; alltimesmonotone |
| CDK2pp.13–15 |230/162/92/34 |150/104/51/14 | Genotypedsubset; onefewerDthanothermarkers not an exactsharedgenotypingassertion |
| ApaIpp.16–18 |231/162/92/34 |150/104/51/14 | Genotypedsubset; matchesBsmItotals |
| TaqIpp.19–21 |231/162/92/34 |150/104/51/14 | Genotypedsubset; matchesBsmItotals |
| DBP1pp.22–24 |231/162/92/34 |150/104/51/14 | Genotypedsubset; matchesBsmItotals |
| DBP2pp.25–27 |231/162/92/34 |150/104/51/14 | Genotypedsubset; matchesBsmItotals |

N216: eFigure1A mean-levelHR.29[.11,.74],P.01 matchesunadjusted40–<50RFS N169; allfive riskarrays114/64/29/10,123/78/32/9,94/70/39/17,39/38/21/8,43/37/25/7 checked; sums413/287/146/51. N217: eFigure1B mean-levelHR.39[.18,.84],P.02 matchesunadjusted30–<40death N167; fivearrays114/78/36/13,123/87/37/12,94/76/43/17,39/39/21/8,43/42/28/7 checked; sums413/322/165/57. Allnonnegative/nonincreasing; deathriskcounts≥RFSriskcounts for eachmean-level/time asexpected becauseRFS removeseventsadditionalto death. All baseline pooledgroups equal eTable1 sums:40+74=114,56+67=123,71+23=94,39+0=39,42+1=43. Different follow-up endpoint produces different later riskcounts legitimately.

N218: eFigure2 annual1/2/3/4year legend,colortreatmentassignment,0–100ng/mLaxis,treatmentleft/rightandcalendar-monthcaptionchecked. No exact printedquartiles,whiskerrule,annualdenominators or rawpoints; approximateboxcoordinates not used to create arithmetic contradiction.

N219: all eTable1groupcounts/percentages/totals and eTable2missingness checked. Dcounts40+56+71+39+42=248; P74+67+23+0+1=165;total413. D100×count/248=16.129/22.581/28.629/15.726/16.935→16/23/29/16/17;P100×count/165=44.848/40.606/13.939/0/.606→45/41/14/0/.6. D248/413=60.048→60%,P165/413=39.952→40%. IndependentroundedsumsD101%,P100.6% legitimate (cellsroundtolerance). eTable2missing3/251=1.195%→1%,4/166=2.410%→2%,3+4=7. eTable1omits3D/1P relative251/166; itsaverage-over-coursegroups are distinct frombaselinemissingness3D/4P, so no unsupportedidentity imposed.

N220: contents/captions allnumericphenotype/genotypelabelschecked; geneticCDK2 pp.13–15 versus plannedCDX2andPCR Cdx2 iscandidate NS-G. 'Posthoc'cancersitecontentsversusgeneric'Subgroup'captions not a quantitativecontradiction. Age≤65 includes65despite colloquial'youngerthanmedian'caption; explicitinequalityandplot65andyoungermatch. Baseline20–40 andaverage20–<30/30–<40 are different groupingvariables, not contradictory scales.

No display-zero P value encountered; no candidate based on zero display. Every relationship COMPLETE with the named missing coordinate/variance limitations. Scientific coverage gap: none.

## Candidate observations (all Pending Human Adjudication)

### NS-A — Initial PLAN daily dose and capsule strength do not reconcile

Relationships N136,N137. Locations and roles: [initial intervention p.9](../../../joi190023supp1_prod.pdf#page=9) PLAN prints2×600IU/day; [initial synopsis p.4](../../../joi190023supp1_prod.pdf#page=4) PLAN prints2capsules/day; [initial capsule preparation p.12](../../../joi190023supp1_prod.pdf#page=12) PLAN prints1000IU/capsule. Rule: dailyIU=numbercapsules×IU/capsule;2×600=1200 versus2×1000=2000; difference800IU/day, tolerance0IU for stated integer strengths. Direct observation: different capsule strengths inside the sameinitialprotocol. Derived arithmetic: implieddose2000 differs from1200objective. Alternative: later1000IU language may have been copied into theinitialversion; amendmentp.45 documentslater1200→2000change but does not explain thisinternalversiondiscordance. Relevance: supplied initialdose can be extracted two ways, affecting evidence-table treatment labels; no conclusion-impact assertion. Humanquestion: Which capsule strength and daily dose belong to theinitialprotocol, and wasp.12 retrospectively updated? All compared locations PLAN.

### NS-B — Initial target400 conflicts with amendment account of blank initial sample size

Relationship N142. Locations/roles: [initial synopsis p.3](../../../joi190023supp1_prod.pdf#page=3) PLAN prints'Total,n=400;vitaminD,n=240;placebo,n=160' and stop>400; [initial calculation p.14](../../../joi190023supp1_prod.pdf#page=14) PLAN has blank'Sample size'/'Sample size calculation'; [amendment p.45](../../../joi190023supp1_prod.pdf#page=45) PLAN says'sample size was blank at2008.12.25,but fixed as400…2009.10.8'. Rule: numeric target400 is present, while thehistory asserts absence in thatversion; binarypresencecomparison, no roundingtolerance.240+160=400 verifies theprintedtarget. Directobservation: target appears in suppliedinitialsynopsis and is absent initscalculationsection. Inference: amendment'blank'statesentiretargetwasunset; alternative it meant only blankcalculationsection, or initialsynopsiswasupdatedlater. Relevance: extraction ofplannedinitialenrollment and changetiming differs. Humanquestion: Does'blank'mean thecalculationheadingonly, or was theinitialsynopsis amended aftertheinitialdate? All compared locations PLAN.

### NS-C — RFS censor rule uses OR where the endpoint definition uses AND

Relationship N149. Locations/roles: [initial endpoint p.9](../../../joi190023supp1_prod.pdf#page=9) and [final endpoint p.25](../../../joi190023supp1_prod.pdf#page=25), bothPLAN, define earliestrelapseordeathand censor'no relapse and remain alive'; [initial censor p.13](../../../joi190023supp1_prod.pdf#page=13) and [final censor p.29](../../../joi190023supp1_prod.pdf#page=29),bothPLAN, state'relapse-free or alive'. Printedcomponents: relapse,death,AND/OR; no numericaleventcountprintedattheselocations. Rule: forR=relapse,F=death,event=R∨F,nonevent=¬R∧¬F; printedORnonevent=¬R∨¬F also accepts R=1,F=0andR=0,F=1. Truth-table tolerance0logicalstates. Directobservation: conflicting censorlabels for thesamequantitativetime-to-eventmeasure. Inference: literalOR would label anevent ascensored; noassertionthiswasimplemented. Alternative: informalOR or untranslatededitingartifact while analysisuses intendedAND. Relevance: RFS statistic/estimand definition can be misextracted. Humanquestion: Is OR a wordingerror, and which event/censor definition generated RFS? All compared locations PLAN.

### NS-D — Final PLAN high25(OH)D group loses its inequality

Relationship N153. Locations/roles: [final design p.23](../../../joi190023supp1_prod.pdf#page=23) PLAN printslow<20,middle≥20to≤40,high'(40ng/mL)'; [final subgroup analysis p.31](../../../joi190023supp1_prod.pdf#page=31) PLAN printshigh>40. Directp.23PNG visuallyopened: no greater-than symbolbefore40. Rule: disjoint low/middle/high partitionrequires high>40; ifhigh40 means equality,40 belongs tobothmiddle/high and>40 isunassigned. Exactboundary comparison, tolerance0ng/mL on statedcriterion; no guessing laboratoryprecision. Directobservation: missing inequalityinprintedgroupdefinition. Inference: literal40-only group overlaps atboundary, inconsistentwithp.31. Alternative: shorthand missing>withoutdifferentanalysis; cannot conclude countsaffected. Relevance: explicit quantitativesubgrouplabel/scale definition canpropagate into subgroup coding. Humanquestion: Should p.23 highgroup read>40ng/mL as inp.31? Both compared locations PLAN.

### NS-E — Age90 boundary differs between inclusion text and registration criterion

Relationship N156. Locations/roles: [initial inclusion p.9](../../../joi190023supp1_prod.pdf#page=9) PLAN and [final inclusion p.24](../../../joi190023supp1_prod.pdf#page=24) PLAN print'Age30–90years'; [registration form p.38](../../../joi190023supp1_prod.pdf#page=38) PLAN prints'Age30≤<90years'. Rule: inclusive range30≤age≤90 includes90 whereas30≤age<90 excludes90; oneboundaryvalue disagreement, no integerroundingtolerance. Directobservation: printedpopulation boundarylabels differ. Inference conditional on conventional inclusive interpretation of30–90; thedashcouldmean anunspecifiedupperbound. Alternative: completedage convention or formwasupdatedseparately. No claim anobservedparticipantwasineligible. Relevance: exacteligibility/populationlabel for extracting denominators differs; no broadsamplingconcern. Humanquestion: Is the upperboundary inclusive or exclusive, and whatagecriterion wasused? All compared locations PLAN; main observedage correspondence belongs tocross-source lane.

### NS-F — Final PLAN assigns de novo cancer incompatible outcome labels

Relationship N151. Locations/roles: [final synopsis p.19](../../../joi190023supp1_prod.pdf#page=19) PLAN states de-novocancer'adverseevent,not…outcome'; [final detailed outcomes p.25](../../../joi190023supp1_prod.pdf#page=25) PLAN names it'Tertiaryoutcome'; [amendment p.45](../../../joi190023supp1_prod.pdf#page=45) PLAN says itwas separated fromsecondaryandsafetyoutcomesandinsertedastertiary. Rule: one outcome in a singlefinalplan cannot simultaneouslybe labelednotanoutcome and atertiaryoutcome; exactmeasure/outcomelabel comparison, no numerictolerance. Directobservation: finalplanretains incompatibleclassificationlabels. Inference: synonym or stale synopsis mayexplainit; noassertionthatanyobservedevent wasmissed. Alternative: safety collectioncontinued whileadditionaltertiaryanalysisperformed, with synopsiswordingnotupdated. Relevance: the label attached toreported de-novocancercounts/effectcanbe inconsistentlycoded; no broadprotocolviolationclaim. Humanquestion: Was de-novocancer atertiaryoutcome, safetyoutcome, or both in thefinalplan, and which label should readersuse? All compared locations PLAN.

### NS-G — Quantitative genotype effects are labeled CDK2 versus CDX2

Relationships N187–N189,N155,N220. Locations/roles: [results eFigure3G p.13](../../../joi190023supp2_prod.pdf#page=13), [3H p.14](../../../joi190023supp2_prod.pdf#page=14),[3I p.15](../../../joi190023supp2_prod.pdf#page=15),allREPORT, printCDK2GG/GA/AA withHR.69[.34,1.38],.72[.39,1.32],1.82[.48,6.88] andriskbaselineD89/103/38,P49/77/24. [final genetic methods p.27](../../../joi190023supp1_prod.pdf#page=27) PLAN namesCDX2rs11568820; [PCR appendix p.36](../../../joi190023supp1_prod.pdf#page=36) PLAN namesCdx2; [initial methods p.12](../../../joi190023supp1_prod.pdf#page=12)PLAN alsoCDX2. Rule: namedmeasuredmarker attachedto genotypeeffect estimates should match thesupplied markerdefinition; stringCDK2≠CDX2, zerocharacter-mismatchtolerance. Directobservation: identicalCDK2labelsthroughoutthreeresultpanelsversusCDX2inmethods. Inference: onelettertranscriptionerror could explain allthree, notprovenfrom externalgeneinformation. Alternative: distinctgeneanalyzed but notidentified in suppliedmethods. Relevance: downstream evidence couldattributeHRs/riskcounts toadifferentmarker. Humanquestion: Do allthree CDK2panels report theplannedCDX2rs11568820results, and which marker label iscorrect? Compared discrepancy locations REPORT versusPLAN; mainCDX2methods maycorroboratePLAN but are notneededto thiscandidate.

## Complete subgroup component appendix

Each row below is the corresponding numeric relationship N181–N215 in source page order7–41. Every component has been checked as described above; no tuple or risknumber excluded. Roles REPORT for allrows. Exact PDF location is the pagecolumn in joi190023supp2_prod.pdf.

| Unit | Page/figure | Subgroup | HR[95%CI] | P | Pinteraction | Placebo0/2/4/6 | VitaminD0/2/4/6 | Coverage |
|---|---|---|---|---|---|---|---|---|
| U052 | 7/3A | FokI CC | .65[.34,1.26] | .20 | .65 | 57/37/19/8 | 92/64/35/9 | COMPLETE |
| U053 | 8/3B | FokI CT | .77[.42,1.43] | .41 | .90 | 75/53/24/5 | 117/89/48/23 | COMPLETE |
| U054 | 9/3C | FokI TT | .97[.32,2.88] | .95 | .67 | 25/18/10/3 | 36/21/10/3 | COMPLETE |
| U055 | 10/3D | BsmI AA | .44[.03,7.16] | .56 | .66 | 8/3/1/0 | 14/11/5/2 | COMPLETE |
| U056 | 11/3E | BsmI AG | .60[.24,1.48] | .27 | .50 | 23/13/7/1 | 42/26/15/3 | COMPLETE |
| U057 | 12/3F | BsmI GG | .86[.52,1.41] | .55 | .38 | 119/88/43/13 | 175/125/72/29 | COMPLETE |
| U058 | 13/3G | CDK2 GG | .69[.34,1.38] | .29 | .64 | 49/32/18/5 | 89/62/34/7 | COMPLETE |
| U059 | 14/3H | CDK2 GA | .72[.39,1.32] | .28 | .63 | 77/54/25/7 | 103/72/46/20 | COMPLETE |
| U060 | 15/3I | CDK2 AA | 1.82[.48,6.88] | .38 | .19 | 24/18/8/2 | 38/28/12/7 | COMPLETE |
| U061 | 16/3J | ApaI GG | 1.00[.49,2.05] | .99 | .35 | 69/53/30/9 | 96/73/39/15 | COMPLETE |
| U062 | 17/3K | ApaI GT | .70[.38,1.27] | .24 | .63 | 61/42/18/5 | 104/65/40/14 | COMPLETE |
| U063 | 18/3L | ApaI TT | .53[.15,1.84] | .32 | .49 | 20/9/3/0 | 31/24/13/5 | COMPLETE |
| U064 | 19/3M | TaqI TT | .87[.52,1.46] | .60 | .35 | 115/86/42/13 | 172/122/70/29 | COMPLETE |
| U065 | 20/3N | TaqI TC | .49[.22,1.10] | .08 | .20 | 31/16/8/1 | 54/37/19/4 | COMPLETE |
| U066 | 21/3O | TaqI CC | -[-,-] | 1.00 | - | 4/2/1/0 | 5/3/3/1 | COMPLETE |
| U067 | 22/3P | DBP1 TT | .71[.42,1.22] | .22 | .63 | 82/54/27/7 | 134/92/53/23 | COMPLETE |
| U068 | 23/3Q | DBP1 TG | 1.00[.44,2.24] | .99 | .49 | 59/43/21/6 | 87/63/37/9 | COMPLETE |
| U069 | 24/3R | DBP1 GG | .65[.14,2.92] | .57 | .91 | 9/7/3/1 | 10/7/2/2 | COMPLETE |
| U070 | 25/3S | DBP2 CC | .60[.34,1.05] | .07 | .16 | 81/52/18/6 | 115/78/49/15 | COMPLETE |
| U071 | 26/3T | DBP2 CA | 1.19[.55,2.60] | .66 | .16 | 58/46/29/7 | 91/64/33/14 | COMPLETE |
| U072 | 27/3U | DBP2 AA | .80[.20,3.20] | .75 | 1.00 | 11/6/4/1 | 25/20/10/5 | COMPLETE |
| U073 | 28/4A | Men | .59[.37,.97] | .04 | .13 | 103/64/28/9 | 173/120/65/30 | COMPLETE |
| U074 | 29/4B | Women | 1.18[.56,2.51] | .66 | .13 | 63/49/26/7 | 78/56/28/5 | COMPLETE |
| U075 | 30/5A | Age<=65 | .86[.44,1.68] | .65 | .48 | 91/68/33/11 | 106/76/45/18 | COMPLETE |
| U076 | 31/5B | Age>65 | .63[.37,1.05] | .07 | .48 | 75/45/21/5 | 145/100/48/17 | COMPLETE |
| U077 | 32/6A | BMI<25kg/m2 | .75[.49,1.16] | .20 | .87 | 144/99/47/14 | 208/141/68/28 | COMPLETE |
| U078 | 33/6B | BMI>=25kg/m2 | .88[.22,3.55] | .86 | .87 | 21/13/6/2 | 41/33/24/7 | COMPLETE |
| U079 | 34/7A | Esophageal cancer | 1.01[.42,2.44] | .99 | .65 | 18/7/3/2 | 22/11/4/2 | COMPLETE |
| U080 | 35/7B | Gastric cancer | .84[.40,1.76] | .64 | .88 | 68/53/26/8 | 106/84/50/17 | COMPLETE |
| U081 | 36/7C | Colorectal cancer | .69[.39,1.24] | .22 | .66 | 79/52/25/6 | 122/80/38/15 | COMPLETE |
| U082 | 37/8A | StageI | .39[.14,1.13] | .08 | .14 | 67/53/29/7 | 115/100/61/22 | COMPLETE |
| U083 | 38/8B | StageII | 1.20[.51,2.80] | .68 | .23 | 48/34/14/6 | 63/42/18/7 | COMPLETE |
| U084 | 39/8C | StageIII | .86[.51,1.46] | .58 | .62 | 51/26/11/3 | 73/34/14/6 | COMPLETE |
| U085 | 40/9A | Adenocarcinoma | .70[.43,1.13] | .14 | .47 | 147/104/50/14 | 226/164/89/33 | COMPLETE |
| U086 | 41/9B | Nonadenocarcinoma | 1.18[.54,2.60] | .68 | .47 | 19/9/4/2 | 25/12/4/2 | COMPLETE |
