# Numeric consistency checker: assigned PLAN tail and SAP

Scope: 119 global numeric relationship groups N600–N718, with all constituent printed values preserved in `../relationships/numeric_plan_tail.md`. This is a fresh numeric review. All source locations are PLAN by content. Three distinct candidate observations are emitted below without stable candidate IDs or AI adjudications. Their repeated occurrences across original/final SAP are provenance of the same observation, not additional candidate counts.

## Complete check record

### Protocol tail: N600–N638 (N-PT001–039)

- N600: Miami nine-point figure is a named photographic scale, not nine participants or a trial outcome; no other assigned image contradicts its point count.
- N601: activity thresholds refer to AC/haze/retinal-choroidal inflammation, not edema alone; ≥1+ and the separate edema exception have different clinical predicates. No numeric contradiction follows.
- N602: duplicate observers are two people at baseline/6mo/12mo/failure; primary observer is explicitly used for the primary endpoint. These are measurement sources, not duplicate participant counts.
- N603: certification ≥80%, remedial retest for <80%; thresholds partition without overlap or gap.
- N604: five qualifying consecutive patients, grades within one; >one triggers extension and all-zero patients excluded. No arithmetic inconsistency between attempted and qualifying samples.
- N605: 20°×20°/49 sections/16 ART versus 30°×5°/seven sections/25 ART are separate scans. Repeated settings at PDF130–131 agree; two scans per eye.
- N606: Heidelberg quality ≥20 and central-subfield thickness each eye; quality score is not µm or an event count.
- N607: one cube plus one five-line raster per eye; image-only PDF133 directly viewed. Caption is exactly “512x218 HD”; no supplied competing acquisition dimension, so no conjectural correction from outside specifications.
- N608: Cirrus quality ≥5 is a different device scale from Heidelberg ≥20; image-only PDF134 mapped visually. No same-scale comparison is assumed.
- N609: at least two qualified operators is a minimum staffing count, distinct from two observer measurements and two eyes.
- N610: photo baseline/6mo/12mo/failure schedule agrees between PDF135 and143; failure substitutes earlier visit. NEI and Miami grades are separate photographic scale labels.
- N611: laboratory measurements include counts, percentages and analytes; CD4 restricted sites and baseline/3/6/12mo differ explicitly from general visit labs. No sum of nonexclusive test populations is asserted.
- N612: twice-ULN nonserious lab stop with one-month normalization/resumption rule versus immediate serious failure are distinct thresholds. Earlier restart explicitly permitted.
- N613: laboratory SAE immediate failure/no PhaseII switch; nonlaboratory SAE in N617 has conditional review. Different SAE subclasses do not contradict.
- N614: AST/ALT interval [2,5)×ULN and creatinine [1.5,2)mg/dL are internally ordered; IOP>24mmHg uses its own scale. WBC≤2.5 has no unit printed here: a missing local unit alone does not establish a competing numeric value/unit.
- N615: AST/ALT≥5×ULN joins [2,5) nonserious interval at five without overlap/gap; qualitative SAE categories may overlap and must not be summed.
- N616: onset/resolution each visit and SAE notice within24h are different clocks; no arithmetic conflict.
- N617: nonlaboratory relatedness review versus lab SAE immediate failure is disclosed distinction; six-month follow-up and six-month DSMC reporting are different schedules; death24h agrees with SAE24h.
- N618: rows observations, columns variables; NA is missing, not zero; no realized workbook denominator supplied.
- N619: pill count each visit and missed-dose logs have no actual count supplied; no adherence percentage inferred.
- N620: BSCVA letters plus Snellen equivalent are paired representations, not summed scales; no conversion data supplied.
- N621: clinical primary observer versus masked reading-center NEI/Miami and OCT morphology are different measures; no identical result is supplied for conflict.
- N622: hemoglobin ≤10 changed to ≤9 explicitly on1March2013. Historical values9–10 are amendment rationale, not contemporaneous conflicting threshold.
- N623: week2±3days and phaseI later safety visits7/8/10/11 are explicit distinct windows; surgery next6mo applies eligibility rather than success.
- N624: sequential site additions and three-month timeline movement have explicit amendment dates; no fixed contemporaneous site total in these clauses.
- N625: masking bags and prior-four-week steroid injection exclusion are disclosed amendments, not a count mismatch.
- N626: 14days→4weeks and60→90days have explicit revisions; 4weeks=28days under literal week arithmetic. They are not asserted equivalent to the prior durations.
- N627: old/new eligibility carried forward to PDF150 under8May2014 revision; population matching retains this boundary.
- N628: old90day activity, four-week steroid treatment/rebound thresholds and 1mg/kg are prior criteria.
- N629: new180day activity/rebound, ≥10mg/day for≥90days and injection4–180days are revised criteria; lower/upper bounds ordered. Native “³” is inequality encoding resolved in mapper, not cubic dose.
- N630: named eligible disease categories do not supply disjoint participant counts; no sum possible.
- N631: Riyadh addition and prednisone7.5mg/day maintained target are explicitly dated amendments, not a success failure numerator.
- N632: acuteVKH≥4weeks and baseline examination up to7days prior apply distinct eligibility/time predicates.
- N633: additional IND-VFQ at Indian sites, NEI-VFQ all sites, Miami preferred photographic scale, NEI eligibility and first90day edema injections are distinct fields/explicit amendments. No incompatible numeric result supplied.
- N634: remove month6 from6–12mo table is explicit version update; no silent duplicate visit count.
- N635: prior-IMT twelve-month window, >12mo earlier exception and any-time biologic exclusion distinguish drug classes; administrative7→10day submission has explicit amendment.
- N636: persistence≥28days crosses nonserious to serious laboratory-event classification; agrees with one-month language at practical scheduling precision, not an exact asserted calendar-day equality. CD4 restrictions repeat N611.
- N637: PhaseII usual two-week entry with explicit exception and omitted repeated forms has no actual duplicate/absent baseline count.
- N638: paper-to-REDCap replacement explicit dated operational amendment; no arm allocation counts supplied.

### Original SAP: N639–N665 (N-SAPE001–027)

- N639–N642: six-month primary endpoint, six-to-twelve-month continuation and four-week rescue visits retain distinct time origins and denominators.5mo sustained≥28days is an additional endpoint, not an equality between calendar month and28days. Secondary percentages/rates/SAE discontinuation remain distinct measures.
- N643–N644: four enumerated original sites match four identifier codes;5characters=1digit+1letter+3digits;4J101 conforms. Three randomization columns count correctly. Blocks4 probability2/3 and6 probability1/3 sum to1. Individual block-probability prose needs the size weighting in candidate PT-NUM-A.
- N645: five eye classes generate5×5=25 combinations. Requires oneC: eligible cells=5+4=9 and ineligible16. Every cell matches that rule; no double count of(C,C).
- N646: four baseline rows×five outcomes plus five baselineE NA cells=25; E denotes absent/never-assessable baseline and does not supply an observed six-month failure. Fail* exception is explicit.
- N647–N649: both-eye patient success versus selected eye outcomes has explicit unit distinction. Worst-to-date assignment versus baseline nonassessable exceptions are prospective rules without a realized conflicting numerator. “two observations per patient” can refer to the two timepoints and is not alone a quantified clash with eye-level analysis.
- N650–N652: anatomy0/1 and treatment0/1 are separate coding variables; −2/+4week windows are asymmetric by design. Four sites require three nonreference indicators, matching the printed reference rule.12mo success requires both6/12mo observations; logMAR2.0 is an assigned missing-eye value, not two letters or a person count. Edema patient denominator and thickness eye measurements retained.
- N653:108×2=216; .6−.4=.2; (.6+.4)/2=.5;10%loss leaves97.2 per arm in expected counts. Inferential80%power compatibility assigned stat lane.
- N654: all25cells checked: each drugB probability equals drugA plus detectable difference (20+18=38,20+21=41;30+20=50,30+23=53;40+20=60,40+23=63;50+20=70,50+22=72;60+19=79,60+21=81). All lie in[0,100]. Statistical power under subgroup composition belongs stat lane.
- N655: sequential .9×.95=.855 retention;108×.855=92.34 if additional5% conditional, vs91.8 if additive15% total. Wording “additional” alone does not settle that convention; no printed fixed twelve-month count contradicts either.
- N656:3.5mo median and lambdaC namedMTX versus historical medianMMF produce candidate PT-NUM-B. BSCVA6.5letters,2.63letters,108 each preserve units; actual power calculation belongs stat lane.
- N657:.6²=.36;8.4×sqrt(1−.36)=8.4×.8=6.72. Mean50 and scale0–100 are supplied as labels, not outcome count.2.57 power/MDE compatibility assigned stat lane.
- N658: discontinuation13%/4%tolerability and5%/5%safety apply separate causes; factor-two38/19=2.160µm SD and65/100µm differences all same unit. No cause sum asserted as observed data.
- N659: enrollment108×.9×.6=58.32(B/A),108×.9×.4=38.88(A/B); one decimal gives58.3/38.9. Completion×.95 gives55.404/36.936→55.4/36.9. Floor gives58/38. Printed formula n_j includes retentionr2 yet prose58/38 refers enrollment, explicitly separated by table captions. No standalone arithmetic candidate for enrollment/completion. Group identities compared to following table emit PT-NUM-C.
- N660–N661: all35power-table cells preserved. .42−.17=.25, not.17; .42−.15=.27; .40−.15=.25. Claimed17% versus25% detectable difference forwarded to stat lane rather than registered here as duplicate statistical observation. Count-header reversal against enrollment is PT-NUM-C. Other row sizes58/76,116/38,40/40 are explicitly sensitivity scenarios, not observed flow counts.
- N662: ten MI replications and ten hotdeck replications same count, not twenty distinct participants; no denominator inferred.
- N663: approximate accrual7–8/mo×30mo=210–240, encompassing216. At25%lower accrual,30/.75=40mo, while3years3mo=39mo; approximate7–8 rate gives completion36–41.14mo for216, including39. No precision-independent contradiction. About3/4 Indian recruitment is approximate and time-specific.
- N664: safety any dose, ITT randomized, PP excludes violations/<50%adherence are distinct declared populations. No realized denominator permits sum check.
- N665: data rows/columns/NA code and DSMC5–7member range are prospective; no workbook actual counts or source missingness supplied.

### Original/final SAP middle: N666–N684 (N-SAPL001–019)

- N666:216/3=72, two-thirds=144. Approximate six-month delay after72nd enrollment refers when outcomes mature, not accrual count error.
- N667:15 versus30American projected interim patients scale exactly twofold. They are explicitly approximate enrollment projections, not a fixed quarter of72 or144. Alpha fractions reviewed independently statistically;24hSAE notice agrees protocol.
- N668: four pooled any/serious ocular/systemic categories are overlapping, not mutually exclusive totals. Subject risk and multiple-events/person rate separated in printed methods.
- N669:100dpi, four-digit date, NA and figure/table parity are operational labels; no realized data table supplied.
- N670:≥8digit seed is not randomization block length. Generator algorithm versus cited bibliography is not independently a contradictory supplied output count.
- N671–N673: final2017 six/twelve-month and rescue rules retain dates. Two-step SUN examples2+→.5+,3+→1+,4+→2+ use ordered grades, not arithmetic subtraction on numeral labels. “4+ to 2+0.” is punctuation/endnote-looking debris without a supplied distinct grade2+0 definition; no numeric outcome inferred.
- N674–N675: nine named sites match nine encoded first digits and5character ID. Four-site retained administrative sentences occur alongside explicit superseding REDCap update; historical four-site list is not a reported nine-site enrollment sum. No candidate solely from those obsolete list clauses. Block probability statement repeated: PT-NUM-A.
- N676: final two5×5matrices reproduce9eligible/16ineligible and25outcome cells as original; no asymmetric eye eligibility.
- N677–N679: final measurement/missing-eye/baseline summary/outcome/−2/+4window definitions repeat matched original rules. Added vasculitis differs by explicit amendment. Units and patient/eye denominators distinguished; no realization supplied.
- N680: country/site<3pool rule is a prospective sparsity threshold, not an actual sample count. Dropout loss versus AE/intolerance0failure matches original.
- N681: same logMAR2.0 missing-eye and twelve-month both-time/both-eye definitions; four discontinuation labels count four. Starting-treatment steroid-free denominator explicit and distinct from ITT.
- N682:10%margin preserved, but inequality/CI orientation assigned statistical specialist; no numeric margin correction guessed.
- N683:216=2×108,.6−.4=.2,pbar=.5,10%loss→97.2perarm. Original/final inputs match; numeric arithmetic coherent.
- N684: all25sensitivity cells repeated and checked as N654; subgroup25%target is different endpoint/sample subgroup from20%overall target.

### Final SAP tail: N685–N718 (N-ST001–034)

- N685: additional5%twelve-month loss repeats N655, no fixed incompatible denominator.
- N686: exact historical/hazard label mismatch repeats PT-NUM-B; no independent power-based diagnosis here.
- N687: BSCVA SD6.5letters/MDE2.63letters/108 repeats N656; letters not logMAR or Snellen units.
- N688:.6²=.36 and8.4sqrt(.64)=6.72 repeat N657. Inferential MDE2.57 versus2.63 question handed to stat lane.
- N689:13%/4%tolerability and5%both safety preserve separate reasons;10%loss is planning assumption.
- N690:38%=2×19%; all proportions within[0,1].
- N691:160µmSD,65µmMDE,100µmhistorical difference share units;108beforeloss is explicit. Actual power stat lane.
- N692: rescue reason classes efficacy/safety/tolerability repeated; no source counts asserted, so no cause subtotal manufactured.
- N693–N697: exact enrollment/completion calculations repeat N659. n0/n1 initial code agrees table, but probability code is switched at the next formula; power table AthenB58/BthenA38 reverses enrollment A/B38.9/B/A58.3. PT-NUM-C. Seven row input vectors all read and checked; sensitivity rows explicitly change scenarios. Summary58DrugA/38DrugB ambiguous as rescue vs first-line label, retained in same candidate.
- N698:90day sensitivity versus >90day deviation is wording of intervention policy, no observed event at exactly90days supplied to yield concrete numeric contradiction.
- N699: approximate3/4India matches original planning value; no REPORT population aligned here.
- N700:7–8×30=210–240contains216;25%slower requires40ratherthan39months only under an exact30month baseline, whereas source rates/durations approximate. Four-site graph label is prospective retained operational text, without four-versus-nine plotted realized count.
- N701: PhaseI12mo/PhaseII6mo different time origins; no result matching without phase key.
- N702–N705: any-dose safety vs randomizedITT vs exclusionsPP;<50%adherence threshold, rowobservations/columnvariables/NA and subject disposition frequencies are prospective; no realized denominator conflict.
- N706:216/3=72; interim thirds coherent; DSMC5–7 separate count.
- N707: masked TreatmentA/B are presentation labels; no printed source drug mapping supplied for outcomes.
- N708:15/30American interim counts double, approximate enrollment projection. No actual numerator mismatch.
- N709–N710: randomized drug exposure assumption, AE counts and person risks versus recurrent-event rates expressly distinguish units. Four overlapping pooled categories are not summed into a total.
- N711: NA unique missing matches original/final and protocol; no actual cells supplied.
- N712: logMAR abbreviation identifies visual-acuity transform, not literal acuity letters count; no numeric conversion offered.
- N713:≥8digit seed is minimum length, no realized random seed to inspect.
- N714: threshold≥2+and two-step reduction versus≥1+to0 are separate endpoints/denominators; explicit revisions not contradiction.
- N715–N716: nine named sites and nine encoded digits reconcile exactly, and reproduce current site list.
- N717: injection sensitivity/deviation amendments repeat clauses, no event count at the boundary supplied.
- N718: revision says REDCap starting18Jan2017 and all lists electronic asof17Jan2017; body says18Jan2017forboth. This operational date could distinguish preparation from patient randomization; no concrete quantitative outcome/allocation inconsistency is supplied, so it is recorded as context rather than a candidate.

## Candidate PT-NUM-A: individual block-size probability wording

Relationships: N643,N675. Primary suggested category: Numeric or arithmetic inconsistency. Compared locations and roles: original SAP [PDF9 §2.4.3](../../../joi190092supp3_prod.pdf#page=9) PLAN and [PDF10 opening continuation](../../../joi190092supp3_prod.pdf#page=10) PLAN; final [PDF50 §2.4.3](../../../joi190092supp3_prod.pdf#page=50) PLAN. All are one bound plan bundle.

Printed inputs: block size4 chosen probability2/3; size6 chosen probability1/3. Prose: “Individuals have a higher probability of being in a block of size 6 because the blocks are larger.” Direct observation: probabilities and wording read from direct Poppler extraction. Calculation: participant weighting normalizes4×2/3 and6×1/3; P(participant in4)=8/14=4/7=57.1429%; P(participant in6)=6/14=3/7=42.8571%. Thus the long-run individual probability of size6 is lower than size4 by14.2857percentagepoints under the printed design.

Tolerance: exact fractions; rounding at even one percentagepoint cannot reverse the ordering. Inference is the size-weighted interpretation of “higher probability”; no realized allocation claim. Alternative: “higher” could mean higher than the block-selection probability1/3 rather than higher than size4. Indeed3/7>1/3 by2/21. A finite stopped list may also have a different realized fraction; no realized fraction is reported. Quality-control relevance: prose can misstate the quantitative randomization description used by later extractors; no claim about achieved balance or conclusions. Human question: Does “higher probability” compare size6 with size4, or compare the individual probability with the one-third block-selection probability, and should the intended comparator be stated explicitly?

## Candidate PT-NUM-B: hazard drug label attached to historical median

Relationships: N656,N686. Primary suggested category: Measure, label, or scale inconsistency. Compared locations and roles: original [SAP PDF24 secondary outcome2](../../../joi190092supp3_prod.pdf#page=24) PLAN; final [SAP PDF65 secondary outcome2](../../../joi190092supp3_prod.pdf#page=65) PLAN. Each location contains both sides of the comparison.

Printed inputs: lambdaC is hazard in methotrexate group; lambdaI is hazard in mycophenolate mofetil group; historical median3.5months is explicitly attributed to mycophenolate mofetil; parenthesis states lambdaC=log(2)/3.5mo for calculation. Direct observation: direct Poppler confirms these same label strings in original and final. Rule: under the supplied exponential hazard parameterization, median3.5mo corresponds to log(2)/3.5=0.1980420516 permonth. Applying the displayed historical MMF median to its named hazard points to lambdaI, whereas source assigns that value to lambdaC(MTX).

Tolerance: categorical drug identity has no rounding tolerance; hazard arithmetic rounded1e−9/month. Inference: the historical median is used as the intended MMF anchor, as opposed to an independently assumed MTX median. Alternative: calculation may intentionally anchor MTX at the same3.5mo as historical MMF or interchange C/I labels under a symmetric formula; neither is expressly stated. Power2.47months is not independently asserted wrong by this numeric observation. Quality-control relevance: named planning-arm input can be extracted under the wrong treatment label. Human question: Is log(2)/3.5 intended for the methotrexate or mycophenolate hazard, and does the calculation intentionally reuse the historical MMF median as a methotrexate assumption?

## Candidate PT-NUM-C: rescue sequence/count and probability-index reversal

Relationships: N659–N661,N693–N697. Primary suggested category: Measure, label, or scale inconsistency. Compared locations and roles: original [SAP PDF25–26 rescue planning](../../../joi190092supp3_prod.pdf#page=25) PLAN, [PDF26 formula and table headers](../../../joi190092supp3_prod.pdf#page=26) PLAN, [PDF27 table and summary](../../../joi190092supp3_prod.pdf#page=27) PLAN; final [PDF66 planning](../../../joi190092supp3_prod.pdf#page=66) PLAN, [PDF67 enrollment/formula/header](../../../joi190092supp3_prod.pdf#page=67) PLAN, [PDF68 table/summary](../../../joi190092supp3_prod.pdf#page=68) PLAN.

Printed inputs:108perinitialarm, retention.9, initialsuccessA.60/B.40. Enrollment table B/A58.3, A/B38.9; expected completion55.4/36.9. Index definesj0=Brescue afterAfailure,j1=Arescue afterBfailure; prose n1=58,n0=38. Following power-table first row labels AthenB58, BthenA38. Probability definitionsp0=MTXrescue afterMMFfailure,p1=MMFrescue afterMTXfailure; first table scenario .42forBafterA and.15forAafterB. Summary says58DrugA/38DrugB.

Direct observation: direct Poppler extraction confirms all labels and cells; direct imagePDF68 visually confirms row58,38,.42,.15,87% and summary. Calculations: afterAfailure108×.9×(1−.60)=38.88→38.9enrolling,36.936→36.9completing; afterBfailure108×.9×(1−.40)=58.32→58.3enrolling,55.404→55.4completing. Floors38forAthenB and58forBthenA follow the printed rule. Thus power-table first row reverses the two sequence counts relative to its own enrollment table. Also fixedj0/j1 sequencing and laterp0/p1 drug names swap associated identities when combined with those header probabilities: the labels and the numeric weights cannot all be retained simultaneously.

Tolerance: table rounding ±0.05person at one decimal; floor differences <1person permitted; reversal gap20persons exceeds either. This is identity/count comparison, not a reconstructed power adjudication. Alternatives: A/B may have been redefined between tables, or power-table counts are a new sensitivity scenario; however text names first row “main scenario” and provides no recoding. Summary58DrugA may mean rescueA, which matches enrollment table, rather than first-lineA, highlighting the unresolved drug-stage key. Quality-control relevance: rescue sample sizes can be transcribed under the opposite treatment sequence, affecting reuse of plan descriptions or power assumptions; no claim about observed rescue outcomes. Human question: Which table sequence labels and n0/p0 versus n1/p1 assignments are intended, and is the58/38power-table main scenario a recoded or changed scenario relative to the38.9/58.3enrollment calculation?

## Crosslane handoff and limitations

Statistical specialists must check power/MDE/CI relationships independently, including17%versus25%rescue difference, QoL/BSCVA MDEs, primary/subgroup power and noninferiority inequality. No old candidate/report data used. No candidate count limit or early stopping used. All119assigned groups inspected and all printed vectors retained. No extraction/scientific coverage gap. Exact randomization comparator and intended hazard/sequence definitions are unresolved human questions, not missing-page limitations. All original sources and reused assets unchanged. Every candidate compares PLAN with PLAN; the coordinator determines formal relationship classifications and stable IDs.
