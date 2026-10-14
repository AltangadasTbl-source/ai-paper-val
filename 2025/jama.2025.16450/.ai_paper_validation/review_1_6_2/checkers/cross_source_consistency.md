# Cross-source consistency — complete disjoint union

Fresh specialist shard records follow without loss.

# Cross-source consistency review: main report, results supplement, protocol and SAP

Scope completed: DOC-001 REPORT, all matched results in abstract, Key Points, narrative, Tables 1–3, Figures 1–2, captions and footnotes; DOC-005 REPORT eTables 1–8 and their matched main-paper statements; DOC-002 PLAN protocol and DOC-004 PLAN SAP statistical design and endpoint specifications. DOC-003 manual comparisons belong to a separate checker shard and are not emitted here. There are no supplied structured result files. Three findings and ten excluded observations are recorded below. No candidate IDs or adjudications are assigned.

The complete scope and review contract were read. Inputs were the fresh main numeric and statistical maps (85 and 48 relationships in separate bounded parts), the protocol/results map and its relationship inventories, and the SAP map. Comparisons match population, time, contrast, analysis set, model and measure before comparing a number. The completion matrix contains 67 grouped matched relationships, below the 120-relationship bound; groups retain their source inventory identifiers. Protocol/SAP native font encoding is unusable. Their complete fresh visual maps and readable OCR are locators; exact source-linked rendered pages confirm the statements supporting findings. Main PDF page 3 was freshly rendered with the permitted fallback helper, PyMuPDF 1.26.4, 200 dpi, CPU, to cross-main-p003.png. Existing source-linked main pp5,7,8 and SAP pp11,22,29,30,38,39 were inspected visually. No source or reused asset was changed, and no prior scientific conclusions were read.

## Findings

### F-XS-001 — Prespecified primary-outcome analyses are absent or replaced in the supplied report

**Exact linked locations and roles:** PLAN [protocol p25, section 5.1](../../../joi250072supp1_prod_1761000786.68881.pdf#page=25); PLAN [SAP p22, analysis populations](../../../joi250072supp3_prod_1761000786.6988.pdf#page=22), [p29, section 7.7](../../../joi250072supp3_prod_1761000786.6988.pdf#page=29), [pp36–37, primary model](../../../joi250072supp3_prod_1761000786.6988.pdf#page=36), [p38, sections 9.4.1–9.4.2](../../../joi250072supp3_prod_1761000786.6988.pdf#page=38). REPORT [main p3, analysis methods](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=3), [p7, Table 2 and Sensitivity and Subgroup Analyses](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=7), [p9, Figure 2 and caption](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=9); REPORT [results supplement p2, eTable 1](../../../joi250072supp4_prod_1761000786.6988.pdf#page=2), all eight eTables pp2–16 inspected for additional primary analyses.

**Printed statements and values:** SAP section 9.4.1 says the ITT primary methods will be replicated in mITT, PP and SAF; SAF groups infants by actual treatment. Section 9.4.2 says baseline factors known to affect BPD, including birth weight, sex and race/ethnicity, will enter a secondary primary-outcome model alongside site and gestational age, with an adjusted RR and 95% CI reported. Section 7.7 specifies treatment interactions for site/center, randomization gestational-age group, race and sex in the robust Poisson primary-outcome model. That primary model codes BPD/death as 1. The report provides ITT, ITT excluding untreated, and PP primary models; Table 2 explicitly uses randomized treatment for every row and only gestational strata and seven-level pooled center adjustment. Primary RRs are 1.00 (0.90–1.11), 1.00 (0.90–1.10) and 1.00 (0.90–1.11). Figure 2 analyzes the complementary favorable outcome, survival without physiologic BPD, with overall RR 1.00 (0.81–1.24), and factors gestational age, chorioamnionitis, baseline FIO2, sex and race. No SAF primary-outcome model, additional-baseline-covariate primary-outcome result, site/center interaction result, or interaction analysis for the planned adverse composite is reported in the supplied report documents. eTable 1 describes SAF but gives no primary effect estimate.

**Comparison logic:** Item-by-item matching shows mITT and PP replication present. SAF replication and the additional-covariate model are not present. The reported favorable-outcome subgroup RR is not the planned adverse-composite model: a risk ratio for a complement is not the reciprocal of the adverse-outcome risk ratio, and interaction tests on those scales are not interchangeable. The report's displayed subgroup analyses therefore do not document the specified adverse-composite interactions, including site/center. These repeated absent/replaced primary-analysis specifications are consolidated as one reporting pattern. This is a logical presence/identity comparison; half-unit numeric rounding cannot supply an absent analysis.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R. The protocol corroborates the planned as-received analysis; it does not create a separate plan-internal conflict.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Primary BPD/death sensitivity RRs and the provenance and outcome scale of primary-outcome heterogeneity analyses.

**Why context does not resolve it:** This is the always-register category of a planned primary analysis not reported or replaced. Reporting safety outcomes as treated does not provide an as-treated primary efficacy result; naming SAF in a disposition table does not provide its model. The report supplies no disclosed amendment or results for the omitted models.

**Supported alternatives and missing definition:** The analyses may have been conducted but not included in the supplied publication, or replaced following early termination. Favorable-outcome subgroup analyses may have been added as descriptive analyses; SAP permits additional ad hoc analyses. Those possibilities do not identify the results of the specified primary analyses. The missing information is whether those planned models and adverse-composite interactions were performed, and where their results or documented changes are available.

**Exact human question:** Were the prespecified SAF as-treated primary model, additional-baseline-covariate primary model, and adverse-composite interaction analyses (including site/center) performed; if so, where are their results, and if replaced, what documented change connects the plan to the reported analyses?

### F-XS-002 — Reported ordinal BPD models differ from the planned ordinal models

**Exact linked locations and roles:** PLAN [protocol p25, section 5.1](../../../joi250072supp1_prod_1761000786.68881.pdf#page=25); PLAN [SAP p39, section 9.5](../../../joi250072supp3_prod_1761000786.6988.pdf#page=39), with ordinal BPD outcome definitions at [pp32–35](../../../joi250072supp3_prod_1761000786.6988.pdf#page=32). REPORT [main p3, ordinal secondary BPD outcome](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=3) and [p8, Table 3 severity rows and footnote a](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=8).

**Printed statements and values:** Protocol specifies proportional odds for ordinal outcomes and generalized logits for nominal outcomes. SAP explicitly gives BPD severity/grade as an ordinal example to be analyzed by proportional odds; if that assumption fails, it specifies partial proportional odds or a Mantel–Haenszel mean-score test using standardized midranks. Nominal unordered categories separately receive generalized-logit models. Report Table 3 footnote a instead states that ORs were estimated by logistic regression (generalized logit). Pragmatic grade 1, 2 and 3 versus no BPD yield ORs 0.87 (0.54–1.41), 0.88 (0.55–1.42) and 0.99 (0.51–1.89); NIH grades yield 1.13 (0.59–2.17), 0.63 (0.30–1.34) and 0.87 (0.47–1.63), each with no BPD as reference.

**Comparison logic:** Both locations identify the same severity distributions at 36 weeks PMA, with gestational-stratum and site/pooled-center adjustment. Category-specific no-BPD-reference generalized-logit contrasts are different quantities from cumulative proportional-odds contrasts. Generalized logit is not among the SAP's stated fallback methods for an ordinal outcome. The NIH and pragmatic occurrences form one repeated model/measure pattern. This is a categorical model comparison, so the numeric display-precision rule is not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** The secondary pragmatic BPD severity analysis and its extracted ORs, with the parallel exploratory NIH severity ORs as another occurrence.

**Why context does not resolve it:** B1 is satisfied by a planned-versus-reported analysis specification. B2 is satisfied because the published footnote clearly names a different model and the supplied plan does not identify generalized logit as an ordinal fallback. B3 is satisfied because the reported ORs compare each grade with no BPD rather than a cumulative severity contrast; the two estimands cannot be extracted interchangeably. The report's explicit model description identifies the published values but does not explain the plan-to-report change.

**Supported alternatives and missing definition:** Severity may have been treated as nominal in the analysis, or generalized logit may have replaced the planned model following fit or assumption assessment. SAP permits additional descriptive analyses, but the supplied report does not identify this as an additional analysis or give the planned ordinal results. The needed information is the implemented ordinal model, assumption assessment and any documented model change.

**Exact human question:** What explains use of generalized-logit category-specific ORs for the BPD severity outcomes instead of the planned proportional-odds model or its stated ordinal fallbacks, and were the planned ordinal analyses also performed and reported?

### F-XS-003 — Moderate hyperglycemia has an additional qualification pathway in the report

**Exact linked locations and roles:** PLAN [SAP p11, section 3.2.4.1, Hyperglycemia](../../../joi250072supp3_prod_1761000786.6988.pdf#page=11). REPORT [main p3, Outcomes](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=3), [p1 abstract hyperglycemia result](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=1), [p6 Safety Outcomes](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=6), and [results supplement p5, eTable 3 hyperglycemia](../../../joi250072supp4_prod_1761000786.6988.pdf#page=5).

**Printed statements and values:** SAP moderate hyperglycemia is 120–180 mg/dL on two determinations at least six hours apart. The main report describes 120–180 mg/dL on two consecutive determinations at least six hours apart **or** more than two determinations within 24 hours with no intervening normal value. The report attributes the adverse-event increase primarily to moderate hyperglycemia. Abstract and eTable 3 give 66.7% versus 49.8%, adjusted RR 1.33 (1.17–1.51), with eTable 3 counts 214 versus 156.

**Comparison logic:** Compare the criteria separately: glucose range agrees; two measurements at least six hours apart is shared, although the report additionally requires consecutive determinations; the report's alternative of more than two readings within 24 hours without a normal value has no counterpart in the SAP list. Three qualifying readings clustered within less than six hours satisfy that alternative without satisfying the SAP six-hour separation. This example is a logical demonstration of different criterion sets, not an assumption about observed patients. No observed reclassification count is claimed. The difference is in an endpoint qualification rule, not numeric rounding.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R. No manual comparison is included in this shard.

**Qualifying route:** Route B.

**Affected result or extracted value:** Hyperglycemia participant experience, 66.7% versus 49.8% and adjusted RR 1.33 (1.17–1.51), highlighted in the abstract.

**Why context does not resolve it:** B1 is satisfied by a planned-versus-reported endpoint criterion. B2 is satisfied because the extra OR pathway and consecutive-reading requirement define distinguishable qualification sets; immediate report/SAP context does not identify which set produced the counts. B3 is satisfied because the report says moderate hyperglycemia primarily explains the safety difference, so qualification can affect the highlighted hyperglycemia result. The difference is not merely an abbreviated severity name.

**Supported alternatives and missing definition:** The report may state a fuller operational criterion omitted from the SAP, or the qualification rule may have been amended. The supplied report does not explain the relationship between these printed lists. Actual measurement times and the number qualifying solely through the additional pathway are unavailable; the finding does not claim a numerical change in incidence.

**Exact human question:** Which complete moderate-hyperglycemia criterion set produced the reported participant counts, and how does the additional 24-hour pathway and consecutive-reading requirement relate to the SAP's two-determination six-hour criterion?

## Matched-relationship completion matrix

Every row is COMPLETE. A matching result means its count, outcome, time, population, contrast, measure, model and direction reconcile; it is not an excluded observation. The grouped matrix records all assigned matched relationships without duplicating every numeric check owned by the numeric checker.

| Group | Source inventory and exact matched scope | Result of comparison |
|---|---|---|
| XS01 | Main N001/S022/S024: abstract, Key Points, pp3–4 planned/enrolled size; protocol pp25–26; SAP p23 | 641 of1160,55.3%; target1160 and simulation1100 agree. |
| XS02 | Main N014/N051/N052: abstract mean birth weight/GA versus p4 narrative and Table 1 |810g/256g and25.9 weeks/1.9 weeks reconcile with arm summaries at displayed precision. |
| XS03 | Main S001: abstract/Key Points/pp6–7/Table 2/p9 primary outcome |68.5%/67.9%, RR 1.00(.90–1.11), no reduction; agree. |
| XS04 | Main S004: abstract/p6/Table 2/p9 death component |15.3%/13.2%, RR 1.13(.78–1.64); agree. |
| XS05 | Main S005: abstract/p6/Table 2/p9 survivor BPD |62.9%/63.0%, RR .99(.87–1.12); agree with survivor denominators272/276. |
| XS06 | Main S019 versus supplement S227: abstract/p6/p7/eTable 3 |66.7%/49.8%, RR 1.33(1.17–1.51); exact match. Definition question is F-XS-003. |
| XS07 | Main S020 versus supplement S220: p6 any AE/eTable 3 |75.4%/64.5%, RR 1.16(1.05–1.28); exact match. |
| XS08 | Main S021 versus supplement S257: pp6–7 PDA/eTable 4 |49.8%/56.8%, RR .86(.75–.99); exact match. |
| XS09 | Main S002/N011/N017 versus supplement N225: treated ITT primary |Population635, complete outcome634=319+315; withdrawal explains difference. |
| XS10 | Main S003/N011/N017 versus supplement N225/N229: PP primary |Population617=309+308;18 major violations; agree. |
| XS11 | Main N006 versus supplement N225/N229 footnotes: reportable randomization |642 randomized, one data-redacted,641 in analyses; reconcile. |
| XS12 | Main N007/N008 versus supplement N225: randomized versus SAF |323/318 randomized,320/315 treated by assignment,322/313 actual-treatment SAF; crossing treatment explains. |
| XS13 | Main N009/N010/N012 versus supplement N225/N229: untreated/withdrawal rules |Six untreated overall, five in complete-outcome exclusions, two missing primary; reconcile. |
| XS14 | Main N075/N076 versus supplement N226: dose counts |ITT exposure221/194 one-dose,99/121 two-dose versus SAF 220/195 and102/118; populations differ explicitly. |
| XS15 | Main N078/N079 versus supplement N226: first/second-dose ages |Assignment versus actual-treatment means are distinct summaries; no matched-value conflict. |
| XS16 | Main N015/N044–N047: aggregate antenatal exposure versus Table 1 |99.1% steroids,89.8% full course,96.1% magnesium,71.2% antibiotics reconcile. |
| XS17 | Main N016/N059/N060/N063/N077: delivery aggregate versus Table 1 |85.1% PPV,64.5% CPAP,58.5% intubation,27.6% delivery-room first-dose reconcile. |
| XS18 | Main N018/N024/N027/N049: discussion rounded baseline aggregates |36% Black,17% Hispanic,75% cesarean reconcile with observed denominators. |
| XS19 | Main N018/S004: discussion36 weeks survival |86% survival agrees with 91/639 deaths at displayed precision. |
| XS20 | Main N020–N050: maternal Table 1 rows and text/caption definitions |No other duplicated main/supplement baseline quantities; observed denominators remain row-specific. |
| XS21 | Main N053 versus Figure 2 actualGA factor |Randomization-stratum versus actualGA distinction is explicit; label observation excluded below. |
| XS22 | Main N054–N058: sex, SGA, Apgar baselines |Figure 2 sex contributor totals agree; remaining rows have no duplicate result. |
| XS23 | Main N061/N062/N064–N074: resuscitation/baseline respiratory summaries |All table context mapped; Figure 2 FIO2 contributor split agrees after unavailable endpoints. |
| XS24 | Main N080/N071/N072/S033/S034: Figure 2 FIO2 exclusions |641−182=459 respiratory-data participants; model contributors458 minus endpoint missingness; reconcile. |
| XS25 | Main S006/S007/S008: pragmatic severity versus p6 no difference statement |All grade intervals contain 1; distribution totals269/270; model difference F-XS-002. |
| XS26 | Main S009: grade 3 binary versus p6 |RR 1.07(.65–1.77), RD .69(−4.34–5.71); narrative agrees. |
| XS27 | Main S010: additionalsteroids versus p6 |RR .89(.73–1.09), RD−3.84(−10.45–2.77); narrative agrees. |
| XS28 | Main S011/S012/S013: NIH severity versus p6 |Category-specific OR intervals contain 1; definition distinct from pragmatic; model difference F-XS-002. |
| XS29 | Main S014: IMVdays day 28 versus pp6–7 |MD−1.49(−2.97–−.01); fewer-day narrative agrees. |
| XS30 | Main S015: IMVdays36 weeks versus p6 |MD−2.04(−5.32–1.23); no stated36 weeks reduction. |
| XS31 | Main S016/S017: intubation day 28/36 weeks versus p6 |Both RRs.87 exclude1; fewer-infants narrative agrees. |
| XS32 | Main S018: extra surfactant versus p6 and footnote |RR-labeled approximate common OR.69(.33–1.46), no difference; approximation disclosed. |
| XS33 | Main S028 versus S001: Figure 2 overall favorable composite |101/321 and102/318 complement220/321 and216/318 exactly; different adjustedRRs/intervals belong to different outcomes. |
| XS34 | Main S029/S030/S040: GA Figure 2 estimates/P and p7 statement |Subgroup RR intervals contain 1, factorP .72; no significant difference agrees. |
| XS35 | Main S031/S032/S041: chorio Figure 2 estimates/P |Intervals contain 1, P .35; p7 no significant subgroup difference agrees. |
| XS36 | Main S033/S034/S042: FIO2 Figure 2 estimates/P/posthoc discussion |Intervals contain 1, P .45; posthoc analysis disclosed. |
| XS37 | Main S035/S036/S043: sex Figure 2 estimates/P |Intervals contain 1, P .28; p7 narrative agrees. |
| XS38 | Main S037/S038/S039/S044: race Figure 2 estimates/P |Intervals contain 1, P .33; p7 narrative agrees. |
| XS39 | Main S045/S046/S047/S048: model captions/direction/interpretation |Randomized efficacy and actual-treatment safety, A/B direction, descriptive labels align across report. Planned-model issues retained separately. |
| XS40 | Protocol N201/S201; SAP N405; main S001: primary endpoint |PhysiologicBPD or all-cause death by36 weeks; status/time/components agree. |
| XS41 | Protocol N205/S203/S204; SAP N406/N407; main S004/S005 |Death36 weeks and physiologicBPD amongsurvivors 36 weeks secondary status agree. |
| XS42 | Protocol N205/N206; SAP N408/N409; main S006–S009 |Pragmatic severity and binary grade 3 remain secondary 36 weeks; threshold-symbol observation excluded below. |
| XS43 | Protocol N205; SAP N410; main S010 |Additional systemic steroids 7 days PLD–36 weeks agree, evolving BPD/CLD definition agrees. |
| XS44 | Protocol N205/N212; SAP N411/N412; main Outcomes |Long-term NDI/death/composite22–26 months belong to stage 2 follow-up; no present early-outcome status change. |
| XS45 | Protocol N207; SAP N413; main S011–S013 |NIH severity remains exploratory 36 weeks, distinct support-duration definition agrees. |
| XS46 | Protocol N207; SAP N414; main S014/S015 |IMV day counts day 28/36 weeks, invasive modalities agree. |
| XS47 | Protocol N207; SAP N415; main S016/S017 |New/continued intubation after 50 hours throughday 28/36 weeks agree. |
| XS48 | Protocol N207; SAP N416; main S018 |Repeat surfactant after 50 hours through 7 days PLD endpoint agrees; collection-column observation excluded below. |
| XS49 | Protocol N207/N212; SAP N417 |Wheeze or cough 22–26 months exploratory status agrees; stage 2 not yet reported. |
| XS50 | Protocol N202/N203; SAP N403; main N081/N084: eligibility |Liveborn GA 22+0–28+6 OR BW 401–1000 inclusive; surfactant decision≤48 hours agree. |
| XS51 | Protocol p16; SAP p15; main p2: exclusion list |Terminal illness, instability or limited care, prior surfactant, prior systemicsteroid agree item by item. |
| XS52 | Same eligibility list: indomethacin |Maternal 24 hours, infant prior, and planned through 7 days PLD agree item by item. |
| XS53 | Same eligibility list: congenital/conflicting trial criteria |Chromosomal conditions or malformations, infection, neuromuscular respiratory disease, conflicting trial agree item by item. |
| XS54 | Protocol N204; SAP N404/S401; main N081/S026 |1:1, infant unit, independent multiples, block urn, NICU×GA strata agree. |
| XS55 | Protocol N209/N210; SAP N402; main N081; supplement N226 |Dose 1 surfactant 2.5mL/kg, dose 2 1.25mL/kg; budesonide 1mL/kg=.25mg/kg each; maximum 2≤50 hours agree. |
| XS56 | Protocol N211; SAP p15; main p3 |Early steroids discouraged, indomethacin prohibition 7 days PLD agree. |
| XS57 | Protocol N213; SAP S420–S422; main S025/S045 |Primary robust Poisson, sandwich, fixed GA and allowed site and center pooling, A/B RR, null 1, two-sided test agree. |
| XS58 | Protocol N214; SAP S402/N435; main S026; supplement N225 |ITT all randomized, mITT treated as assigned, SAF treated as received, PP assigned/no major violations agree item by item; redacted infant exclusion disclosed. |
| XS59 | Protocol N216; SAP S406/S425; main N010 |Primaryavailablecases excludes 2missing;2/641<5%, MI condition not reached. |
| XS60 | Protocol N217/N218; SAP S403; main S022 |.58→.48,10 points,90% power, overall .05,539 large-sample/550 simulation per arm,5% attrition→1160 agree. |
| XS61 | Protocol N221/N223; SAP S408–S412; main S023 |Safety first 40,25/50% andefficacy25/50%; early stop makesfuture 75%look inapplicable. |
| XS62 | Protocol N224; SAP S414; main S024 |Upper80%conditionalpowerCI<.50 at50% and<.30 at75%; reported50%futility agrees with rule. ActualCP values unavailable. |
| XS63 | Protocol N223; SAP S412/S416/S421; main S025/S045 |Overall.05, exact alpha information/priorlooks, unused spending recoverable; report .049 not inconsistent with nominal planned final.044. |
| XS64 | Protocol N215; SAP S426/S427/S430; main S027/S046 |Binary robust Poisson, continuous linear; SAP permits linear for count outcomes; methods compatible. Ordinal difference F-XS-002. |
| XS65 | Protocol N208/N220; SAP N418/S431–S433; main p3; supplement eTables3/6/7/8 |Moderate or worse or unexpected mild,7 day AE/30 day SIP-PVL, actual treatment safety, participant versus event units and fatal SAE windows agree. Glucose criteria F-XS-003. |
| XS66 | SAP S434/N428–N434; main clinical/growth; supplement eTable 4 |Birth–GDBstatus≤120d clinical composites, stage 3 ROP,36 weeksgrowth 10th percentile/death and Z scores andas-treated population agree item by item. |
| XS67 | Protocol/SAP plan-internal analysis/endpoint/hypothesis/power/multiplicity lists |Current SAP refines protocol, retains primary/early secondary hierarchy, models and rule values; conditional or version changes in the excluded table. No further qualifying plan-internal conflict. |

## Excluded observations

Only apparent differences that were considered and not emitted are listed. Reconciled checks remain in the completion matrix.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main p8 Table 3b versus PLAN protocol p21/SAP pp9,32 |Pragmatic grade 1 is printed as cannula less than 2 L/min in report versus ≤2 L/min in plans; the neighboring grade 2 >2 and named Jensen scale make the intended boundary immediately recognizable; no observed reclassification is shown. | NOTATION_OR_TYPOGRAPHY |
| REPORT main p5 Table 1 versus pp2–3 and p9 Figure 2; PLAN SAP p17 |Baseline GA label “<26 wk 7 d” differs from formal <26-week stratum and actual-gestational-age figure; this descriptive baseline label does not change a printed primary/subgroup result or analysis-set size. | PERIPHERAL_COMPARISON |
| REPORT abstract five secondary outcomes versus PLAN protocol/SAP eight |The report describes five outcomes at 36 weeks; the remaining three are 22–26-month stage 2 follow-up outcomes explicitly separated in SAP data-lock plan. | TERMINOLOGY_OR_WORDING |
| PLAN protocol p21 provisional NDI examples versus SAP pp3,10,33–34 final criteria |Protocol says NDI definition will be agreed at first follow-up after the Bayley switch; SAP revision explicitly finalizes cognitive and motor scores <70, GMFCS 4–5, hearing/vision. Protocol GMFCS 3–5 examples are provisional, not concurrent final criteria. | CONTEXT_RESOLVES |
| PLAN SAP p25 unconditional missing sensitivity summary versus p38 threshold |Section 7.3 explicitly refers to section 9.4.3, where analysis is conditioned on more than 5% missing. Specific cross-referenced condition resolves the general sentence. | CONTEXT_RESOLVES |
| PLAN SAP p35 collection column 7 days PNA versus pp11,35–36 definition 7 days PLD |Detailed repeat-surfactant definition is explicit and matches report; collection column mismatch is peripheral and does not change a primary or key secondary outcome or planned decision rule. | PERIPHERAL_COMPARISON |
| REPORT supplement p8 abbreviations versus p7 heading/method paragraph |RR expanded as risk difference in abbreviations but risk ratio in heading and paragraph; dimensionless RR values and separate MD labels resolve the expansion immediately. | TERMINOLOGY_OR_WORDING |
| PLAN SAP p30 dose within 10% compliant versus REPORT major violations/exclusions and eTable 2 |Outside 10% dosing deviations are summarized, while PP excludes major violations; SAP p22 defines PP by major rather than all violations. Assuming every minor volume deviation is major is unsupported. | CONDITIONAL_OR_UNREPORTED |
| PLAN SAP pp29–30 assessment-window sensitivity versus REPORT absent timing-sensitivity result |Timing sensitivity is required only if out-of-window counts differ; that triggering comparison is not supplied. No conflicting statement or actual trigger is printed. | CONDITIONAL_OR_UNREPORTED |
| PLAN SAP pp43,48 Kaplan–Meier mortality display versus REPORT eTables 4/8 death summaries |The published clinical-safety mortality summaries lack the planned Kaplan–Meier curve, but this is neither primary nor key secondary and potential figure formats may change; it does not change a primary or key secondary result, analysis population size or decision rule. | PERIPHERAL_COMPARISON |

## Limitations and completion

All assigned matched main/report and protocol/SAP relationships are complete. Individual participant data, fitted coefficients/covariances, exact interim information fractions, actual conditional-power values, glucose measurement times and documented unpublished analyses are not supplied. These limit reproduction of fitted estimates and determination of any actual endpoint reclassification; they do not leave an assigned source unit unchecked. No manual inconsistency is emitted here. Three findings are prepared for the independent inclusion screen. Ten apparent observations are excluded once with one reason code each.


---

# Manual cross-source consistency review

Scope: every relevant comparison involving DOC-003 (PLAN), including its bound GDB manual, against DOC-001 and DOC-005 (REPORT), DOC-002 and DOC-004 (PLAN), and repetitions inside DOC-003. The four current manual maps cover PDF pages 1–162 completely. This review used those maps, the current main and support maps, and exact source-page images for apparent issues. It did not use prior scientific conclusions. Comparisons without a manual location belong to the separate cross-source shard. Numeric within-display arithmetic belongs to the numeric checker. No supplied workbook, CSV or Office result source exists.

The scope and review contract and cross-source role contract were read completely. Input was read in bounded blocks below 200,000 normalized characters. This output has 27 comparison groups, two findings and nine excluded observations; no relationship or finding limit was applied. Sources and reusable assets were preserved.

Source authority: the linked supplied PDFs. Current mappings and OCR are locators. Apparent safety discrepancies were visually checked on manual pages 37, 39 and 59 and SAP pages 11–12; oxygen criteria were visually checked on manual pages 130 and 148. Main page 3 was freshly rendered with the permitted temporary interpreter and pdf_tools.py render; derivative checkers/parts/manualcross-main-p 003.png, PyMuPDF 1.26.4, 200 dpi, CPU. Other checked page images were source-linked reusable renders, historical rendering engine unspecified. Their transcription does not replace the source.

## Comparison completion matrix

All rows are COMPLETE. Every list below was compared item by item. A statement absent from an operational manual does not by itself conflict with a statistical specification in the SAP. Quantities were matched by population, time, treatment contrast, measure, model and analysis set before comparison. Threshold criteria are logical rules rather than copies of a rounded estimated value; display interval arithmetic does not apply to the two findings.

| Group | Exact manual PLAN scope | Matched source scope and item-by-item comparison | Completion |
|---|---|---|---|
| MX01 | pp 7,11,19–22,25–27 | REPORT pp 1–2; protocol pp 4,16–17; SAP p 15. Liveborn; GA22 0/7–28 6/7 OR birthweight 401–1000 g inclusive; clinical surfactant decision; consent; randomization≤48 h; dose≤50 h. All inclusion items align. | COMPLETE |
| MX02 | pp 7,11,26–27,63,145 | REPORT p 2; protocol pp 4,16; SAP p 15. Each exclusion: terminal/unlikely survival, support limitation, prior surfactant, infant systemic steroids, maternal indomethacin 24 h, prior/planned infant indomethacin, congenital infection, major chromosomal/malformation, permanent respiratory neuromuscular condition, conflicting trial. Generic GDB classification is distinct from trial inclusion. | COMPLETE |
| MX03 | pp 7,11–12,20,22,24,28,75–76 | REPORT pp 2,4 and supplement p 2; protocol pp 17–18; SAP pp 16–17,22. 1:1; site/GA < 26 versus≥26 strata; independent allocation of multiples; opened kit defines randomization; unopened kit unused; randomized untreated remains randomized. Separate consent-redaction and treated/complete-outcome populations are stated in report/SAP. | COMPLETE |
| MX04 | pp 7–8,12,22,29,50,75–76 | REPORT pp 1–3 and supplement pp 3–4,9–10; protocol pp 18–19; SAP pp 14–15,30–31. First surfactant 2.5 mL/kg; second 1.25 mL/kg; budesonide 0.25 mg/kg in 1 mL/kg; maximum 2 study doses; 50 h window; additional open-label surfactant distinguished. Reported violations are explicitly identified. | COMPLETE |
| MX05 | pp 12–13,34–36,51 | REPORT p 3; protocol pp 19–20; SAP pp 15,33. Early steroids discouraged with resistant hypotension/adrenal exceptions; postnatal BPD steroids seven days after last dose through 36 weeks; indomethacin seven days after final dose. Calendar shorthand through day 9 is not a competing dose-relative definition. | COMPLETE |
| MX06 | pp 8,14,52,62 | REPORT pp 1–3,7; protocol pp 4,7,20; SAP pp 9–10,32,36–37. Primary physiologic BPD OR death by 36 weeks PMA; randomized population; same composite, direction and treatment contrast. Manual supplies no competing primary model/covariates. | COMPLETE |
| MX07 | pp 128–131,148 | REPORT pp 3,7 Table 2 c; protocol p 20 refers GDB; SAP pp 29,32. Trial-specific physiologic routing, day 36 screening, test through 37 weeks, NC/hood, ventilation/CPAP exclusion, actual hood versus effective NC oxygen. Transient increases < 2 h and feed-only oxygen excluded. | COMPLETE |
| MX08 | pp 130–131,148 | REPORT p 7 Table 2 c. Hood/NC < 27% and saturations≥90%; 27–30% and≥96%; room-air NC any flow; prior 24 h; majority definition; >30% exclusion. Apparent boundary/symbol differences are recorded below. | COMPLETE |
| MX09 | pp 149–150,156–158 | REPORT p 3 refers manual procedure. Hood reduction 2%/5 min; NC flow reductions; blender and 100% low-flow branches; removal; 5 min phase; stop < 90%5 continuous minutes OR < 80%15 sec; 30 min room air; rapid pass≥96%15 min. Narrative and worksheet rules reconcile under the stated stop criteria. | COMPLETE |
| MX10 | pp 151–155 | REPORT p 3 effective-oxygen lookup reference. Every lookup row/column, nearest-value/midpoint-up rule, illustrative 2 kg/0.15 L/min factor 8/27% result. No contrary report formula or actual infant conversion appears; hypothetical examples are not trial observations. | COMPLETE |
| MX11 | pp 8,14,162 | REPORT pp 3,8 Table 3 b; protocol pp 5,7,20; SAP pp 9–10,32–33. Death; physiologic BPD; Jensen ordinal; grade 3; steroid use: each status, time and component align. Jensen no support, NC≤2, NC > 2/noninvasive, invasive grade 3; terminology and isolated boundary symbol considered below. | COMPLETE |
| MX12 | pp 8,14–17,55–57 | REPORT early-outcome scope; protocol pp 5,21,23; SAP pp 3,10,18–19,33–36. Severe NDI, death, their composite at 22–26 months; separately deferred lock/publication. Cognition, motor, GMFCS, hearing, vision and example/final-definition status each compared. Respiratory wheeze/cough recalled 6 months and worst 2 weeks. | COMPLETE |
| MX13 | pp 8,14–15,30–34,128–129 | REPORT pp 3,8 Table 3; protocol p 21; SAP pp 10–11,34–36. NICHD/NIH severity; ventilation days 28 days/36 weeks; intubation after 50 h through 28 days/36 weeks; repeat surfactant after 50 h through 7 days postfinaldose. Manual collection fields do not specify a competing inferential model. | COMPLETE |
| MX14 | pp 15–16,35,37–45,58–60 | REPORT p 3, supplement pp 5–6,11–14; protocol pp 22–23; SAP pp 11–14,39–42. Treated safety population, actual treatment; 7 days/168 h postfinaldose; SIP/PVL30 days/720 h; moderate-or-greater plus unexpected mild; worsening/recurrence and highest-grade aggregation. Participant and event counts remain different quantities. | COMPLETE |
| MX15 | pp 39,59,61 | REPORT hypertension supplement pp 5,11,13; SAP p 12. Moderate 2–3 readings≥12 h, severe≥4 or medication, life-threatening sustained/multiple therapy; 95th percentile. Mean versus systolic quantity does not reconcile: F-XS-1001. | COMPLETE |
| MX16 | pp 39,59 | REPORT pp 1,3,6; SAP p 11. Moderate 120–180 twice≥6 h; severe > 180 twice≥6 h or insulin; life-threatening > 600 twice≥4 h; alternate > 2/24 h criterion. Alternate qualifying branch does not reconcile: F-XS-1002. | COMPLETE |
| MX17 | pp 38,58 | REPORT safety labels; SAP p 12. Tube replacement, associated HR < 80 and oxygen < 80 for 30 sec, chest compressions; hypoxemia/bradycardia HR < 80 and saturation≤80 with 30 sec duration and response; pulmonary air leak observation/aspiration, chest tube/HFV, oxygen > 80%. Isolated symbols and fatal-event wording considered below. | COMPLETE |
| MX18 | pp 38–39,59,118–119,146 | REPORT safety labels and supplement event tables; SAP pp 11–12. Hypotension agents/20 or 40 mL/kg/4 h/12 h; sepsis culture,≤72 versus > 72 h, antimicrobial duration, systemic symptoms and cardiovascular support/response. GDB infection ascertainment is distinct from graded AE ascertainment. | COMPLETE |
| MX19 | pp 15–16,39–40,59–60,107–110 | REPORT p 3 and supplement pp 5–6; SAP pp 12–13,41–42. ICH blood/distention/parenchyma/shift criteria and 3-day ultrasound grace; PVL30 days and moderate/extensive grade; SIPwithout NEC, deterioration/drain/surgery. GDB imaging≤28 days and later nearest 36 weeks are distinct observation windows. | COMPLETE |
| MX20 | pp 37,40–46 | REPORT supplement pp 12,14,16; protocol p 27; SAP p 42. SAE death, immediate life threat, prolongation, disability, important intervention, congenital/hospitalization qualification; grades 4/5, severe-alone distinction; follow until resolution/chronic/stable or 36 weeks; fatal onset versus later death. Initial hospital admission and prolongation are distinguished in context. | COMPLETE |
| MX21 | pp 49–54,75–76 | REPORT pp 4,7, supplement pp 2,9–10; SAP pp 22,30,38. Deviations and violations, untreated, assigned/actual treatment, withdrawal permission and existing data retained, no replacement; deviations do not independently create a manual PP-analysis rule. Different named analysis sets are explicit. | COMPLETE |
| MX22 | pp 81,84–108,121–129 | REPORT pp 4–6 and supplement pp 2,7–8,15–16; SAP pp 19,30,40–44. GDB population exception for trials; earlydeath≤12 h; first discharge/transfer/death/120 day status; prolonged admission later form; support snapshots and highest-mode hierarchy. Each attained/not-attained field is matched to its relevant endpoint. | COMPLETE |
| MX23 | pp 104–106,112–116,140,144 | REPORT supplement pp 7–8; SAP pp 13–14,43. ClinicalPDA evidence/treatment; death composites; NECmodifiedBell≥II; ROPstage≥3 versus generic disposition and eye-level therapy status. Clinical/growth safety hierarchy is specified by SAP; generic forms do not set a contrary outcome hierarchy. | COMPLETE |
| MX24 | pp 100–103,117,124,137–139,145–147 | REPORT supplement pp 7–8,15–16 and Figure 2; SAP pp 14,43–44. Growth 36 weeks±7 days and units; cause-of-death single antecedent category/autopsy versus fatalAE term; clinical/histologic chorioamnionitis. Generic renal/death and dictionary details are peripheral unless tied to a relevant decision. | COMPLETE |
| MX25 | pp 30–32,87–97,111–120,133–147,159–161 | REPORT baseline and clinical displays; SAPbaseline/clinical keys. Each measurement/window, medication/treatment-code field, nutrition, hearing, infection and organism dictionary checked for misattribution to a primary/keysecondary value. None supplies a contrary matched primary/keysecondary result. No trial result is inferred from empty forms/codes. | COMPLETE |
| MX26 | pp 7,11,16 | REPORT pp 1–4; protocol pp 25–29; SAP pp 23–29. Target 1160 and 1:1 align. Manual has monitoring prose, no power inputs, alpha-spending boundary, margin, formal stopping threshold or multiplicity rule to conflict with the detailed plans. Superiority direction agrees. | COMPLETE |
| MX27 | pp 25,30–32,53–54,75–76,98–102,128 | REPORT models and supplement populations; SAP pp 22,25,38–40. Missing-field collection, retained withdrawal data, attained-timepoint logic and all-randomized collection compared separately with complete-outcome ITT, treatedSAF, mITT,PP and missing-data analysis. No manual imputation or sensitivity estimator competes with SAP. Other cross lane covers detailed model/analysis differences without manual. | COMPLETE |

## Findings

### F-XS-1001

The planned hypertension classification uses different blood-pressure quantities.

- **Locations and roles:** PLAN [Manual p 39, hypertension](../../../joi250072supp2_prod_1761000786.6938.pdf#page=39) and PLAN [Manual p 59, Appendix A hypertension row](../../../joi250072supp2_prod_1761000786.6938.pdf#page=59), with PLAN [Manual p 61, Appendix B mean-pressure threshold table](../../../joi250072supp2_prod_1761000786.6938.pdf#page=61), versus PLAN [SAP p 12, hypertension](../../../joi250072supp3_prod_1761000786.6988.pdf#page=12). REPORT [Results supplement p 11, hypertension event counts](../../../joi250072supp4_prod_1761000786.6988.pdf#page=11) supplies the affected result, not a conflicting pressure definition.
- **Printed criteria:** Manual p 39 and Appendix A specify mean blood pressure above the 95th percentile for 2–3 determinations over at least 12 hours for moderate hypertension without medication, and at least 4 determinations over at least 12 hours or any antihypertensive for severe hypertension. Appendix B's numerical table is mean BP in mmHg. SAP p 12 instead specifies systolic blood pressure with the same determination counts, duration and medication alternatives.
- **Comparison logic:** Mean and systolic pressure are different measured quantities. The count, duration and medication criteria agree item by item; the pressure quantity does not. Reproduction does not depend on clinical assumptions or a calculation from trial counts. Display-rounding interval and relative discrepancy: not applicable to a named measurement quantity.
- **Focus area:** D, planned endpoint classification and safety decision criteria.
- **Proposed review domain:** plan_material. **Proposed relationship:** P_P. **All relationships:** P_P.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** The hypertension safety outcome and its reported 31 versus 23 events in eTable 6, including which measured pressure and threshold classify an event.
- **Why context does not resolve it:** Both plan descriptions name a definite pressure quantity while retaining the same other criteria. The manual's mean-pressure lookup supports mean pressure; the later SAP names systolic pressure. They cannot be treated as interchangeable terms, and the supplied passages do not identify an amendment or tell which quantity generated the reported events. This is a planned classification rule linked to a reported outcome, not a background or administrative comparison.
- **Supported alternatives:** The final SAP may have superseded the manual's mean-pressure rule, or the operational mean-pressure rule may have generated the event data while the SAP describes a different quantity. The supplied documents do not establish which applies; the report counts alone cannot decide it.
- **Exact human question:** Which blood-pressure quantity and percentile lookup were used to classify the reported hypertension events, and did the final SAP's systolic-pressure criterion supersede the manual's mean-pressure criterion?

### F-XS-1002

The hyperglycemia definition contains an additional qualifying measurement pattern in the manual narrative and report that is absent from the manual toxicity table and SAP.

- **Locations and roles:** PLAN [Manual p 39, all three hyperglycemia categories](../../../joi250072supp2_prod_1761000786.6938.pdf#page=39) versus PLAN [Manual p 59, Appendix A hyperglycemia row](../../../joi250072supp2_prod_1761000786.6938.pdf#page=59) and PLAN [SAP p 11, hyperglycemia](../../../joi250072supp3_prod_1761000786.6988.pdf#page=11); REPORT [Main p 3, moderate hyperglycemia definition](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=3). Affected REPORT result appears [Main p 1, abstract](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=1) and [Main p 6, safety outcomes](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=6).
- **Printed criteria:** Manual p 39 defines moderate 120–180 mg/dL on two consecutive determinations at least 6 hours apart OR more than 2 determinations within 24 hours without intervening normal values; severe > 180 mg/dL uses the same timing alternatives, plus insulin; life-threatening > 600 mg/dL uses two consecutive determinations at least 4 hours apart OR the more-than 2/24 hours alternative. Manual Appendix A p 59 and SAP p 11 give the two-measurement spacing branch and severe insulin alternative, but do not give the more-than 2/24 hours branch. Main p 3 expressly includes both branches for moderate hyperglycemia.
- **Comparison logic:** The alternate branch can classify repeated high measurements within a shorter interval even when no pair is 6 hours apart (or 4 hours for life-threatening events). It is a separate OR criterion, not a shorter description of the same requirement. The glucose thresholds, spaced-pair branch and insulin branch were compared separately and align. Display-rounding interval and relative discrepancy: not applicable to a logical eligibility branch.
- **Focus area:** D, planned-versus-reported endpoint definition and plan decision criteria.
- **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **All relationships:** P_R, P_P.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Reported hyperglycemia 66.7% versus 49.8%, adjusted RR 1.33(95% CI 1.17–1.51), and the interpretation that the adverse-event difference was mainly moderate hyperglycemia. The within-plan pattern additionally affects severe and life-threatening hyperglycemia classification.
- **Why context does not resolve it:** The report and operational narrative retain a qualifying branch absent from both the toxicity appendix and final SAP. No stated priority rule establishes whether the branch was deliberately retained, superseded, or omitted in abbreviated plan descriptions. The qualifying-measurement pattern can determine who contributes an event; this goes beyond a difference in wording. No individual glucose data are available to calculate its numerical effect.
- **Supported alternatives:** The Appendix/SAP may be abbreviated and the operational narrative may state the full intended definition; alternatively the spaced-pair rule may be the final definition and the report may retain the broader operational rule. Neither alternative is established by the cited text. This finding does not claim that any participant met only the alternate branch.
- **Exact human question:** Was the more-than 2 determinations within 24 hours without intervening normal values branch used in the reported hyperglycemia outcomes, and which definition governed classification when the manual narrative, toxicity appendix and final SAP differed?

## Excluded observations

Only apparent issues considered and excluded are listed here; reconciled checks appear in the completion matrix.

| Location | Observation | Reason code |
|---|---|---|
| PLAN [Manual p 148](../../../joi250072supp2_prod_1761000786.6938.pdf#page=148), REPORT [Main p 3](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=3), PLAN [SAP p 29](../../../joi250072supp3_prod_1761000786.6988.pdf#page=29) | Manual's 36+1 weeks notation is ambiguous in isolation, but the same paragraph screens exactly 36 weeks and tests no later than 37 weeks; this resolves the practical window without treating the plus symbol as a numerical endpoint discrepancy. | NOTATION_OR_TYPOGRAPHY |
| PLAN [Manual p 130](../../../joi250072supp2_prod_1761000786.6938.pdf#page=130) versus [p 148](../../../joi250072supp2_prod_1761000786.6938.pdf#page=148); REPORT [Main pp 3,7](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=7); PLAN [Manual pp 38,39,58,59](../../../joi250072supp2_prod_1761000786.6938.pdf#page=59); REPORT [Main p 8](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=8) versus PLAN [Manual pp 14,162](../../../joi250072supp2_prod_1761000786.6938.pdf#page=162) | Isolated strict/inclusive-symbol differences: majority > 90% versus≥90%; challenge 30% boundary in prose versus detailed 27–30% eligibility; tube blockage > 30 versus≥30 seconds; hypotension > 40 versus≥40 mL/kg; sepsis > 5 versus≥5 days; Jensen grade 1 < 2 versus≤2 L/min. No changed printed numeric value or actual boundary-classification result is established. Under the explicit instruction to exclude when in doubt about a symbol, these are consolidated as one symbol pattern. | NOTATION_OR_TYPOGRAPHY |
| PLAN [Manual pp 149–151,158](../../../joi250072supp2_prod_1761000786.6938.pdf#page=150) | Room-air pass prose says saturations remain≥90%, while the explicit stop rule and illustrative brief 85% dip allow short dips; immediate failure criteria and example resolve the intended continuation rule. | CONTEXT_RESOLVES |
| PLAN [Manual p 58, pulmonary air leak fatal grade](../../../joi250072supp2_prod_1761000786.6938.pdf#page=58) | Fatal-air-leak cell names a hypertensive event. The row, adjacent grades and other hypertension row make the copied event wording evident; no conflicting reported numerical classification is supplied. | TERMINOLOGY_OR_WORDING |
| PLAN [Manual pp 14,16](../../../joi250072supp2_prod_1761000786.6938.pdf#page=14), PLAN [Protocol p 21](../../../joi250072supp1_prod_1761000786.68881.pdf#page=21), PLAN [SAP pp 3,10,33–34](../../../joi250072supp3_prod_1761000786.6988.pdf#page=3) | Earlier severeNDI examples include GMFCS3–5; final SAP adds motorBSIDIV < 70 and GMFCS4–5. Earlier text explicitly leaves the definition to follow-up agreement; SAP revision history expressly finalizes the BayleyIV definition. No contradictory final definition is inferred from an explicitly provisional example. | CONTEXT_RESOLVES |
| PLAN [Manual pp 81,84](../../../joi250072supp2_prod_1761000786.6938.pdf#page=81) versus PLAN [Manual pp 7,11,26](../../../joi250072supp2_prod_1761000786.6938.pdf#page=11) | Generic GDB21–27 weeks differs from BiB22–28 weeks or birthweight eligibility; the GDB expressly permits trial exceptions. Generic registry eligibility does not change the BiB analysis population. | CONTEXT_RESOLVES |
| PLAN [Manual pp 37,46](../../../joi250072supp2_prod_1761000786.6938.pdf#page=37), REPORT [Supplement pp 12,14](../../../joi250072supp4_prod_1761000786.6988.pdf#page=12), PLAN [SAP p 42](../../../joi250072supp3_prod_1761000786.6988.pdf#page=42) | Manual footnote excludes requiring hospitalization as an SAE category in already-hospitalized premature infants; report/SAP retain prolongation of existing hospitalization. Initial admission and prolongation are clinically distinct in context; the footnote does not establish removal of prolongation. | TERMINOLOGY_OR_WORDING |
| PLAN [Manual pp 114–116,139,145](../../../joi250072supp2_prod_1761000786.6938.pdf#page=115) versus PLAN [SAP p 43](../../../joi250072supp3_prod_1761000786.6988.pdf#page=43) | Generic severeROP disposition includes therapy/detachment, while trial severeROP explicitly uses stage 3; renal death-code footnote/column logic is unspecified and generic malformation dictionaries differ by form purpose. These plan-internal generic fields do not change a primary/keysecondary result, analysis-population size or specified trial decision rule. | PERIPHERAL_COMPARISON |
| PLAN [Manual pp 15–16,77,109–110,130](../../../joi250072supp2_prod_1761000786.6938.pdf#page=77), REPORT [Main p 3](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=3) | Version/revision dates, postnatal/corrected-age naming, ordinary PVL/ICH scan times, per-timepoint contributor/measurement windows and administrative pointers differ by document purpose. They do not establish a contrary primary/keysecondary count, analysis population or decision rule. | PERIPHERAL_COMPARISON |

## Limitations

The package supplies no individual glucose histories or BP measurement data, so the number of events classified differently under the two safety criteria cannot be computed. This limits impact quantification, not reproduction of the conflicting printed plan criteria. No additional scientific coverage gap remains in the assigned manual-comparator scope. Mapping locators have some font-encoding and OCR gaps already closed by visual mapping; apparent issues were checked against source-linked images. No raw-data or clinical-methodology audit was performed.
