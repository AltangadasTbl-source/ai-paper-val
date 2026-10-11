# Numeric consistency checker

Fresh stage /root/numeric; all N001–N154 numeric relationships completed. See [complete inventory](../relationships/numeric_relationship_inventory.md). This review applies the bounded quantitative scope: source-grounded arithmetic, totals, denominators, percentages, units/scales/model labels and repeated values. Participant/sample-unit observations appear only when a printed number or label creates a concrete conditional inconsistency. No broad methods review; no old candidate conclusions; no external evidence. No stable candidate IDs or adjudications assigned here. Local NUM-* names are discovery provenance only.

Numeric discoveries:18 distinct observations. All roles below assigned by document content. Every candidate has source observation, reproducible comparison, tolerance, alternative and human question. Questions whose assumptions remain unsettled are explicitly conditional. No displayed-zero P candidate.

## NUM-01 — Usual-care baseline patient-day minimum

- **Exact locations and document roles:** [Figure1 UC baseline REPORT](../../../jama_parshuram_2018_oi_180015.pdf#page=3); [eTable3 hospitalL REPORT](../../../joi180015supp3_prod.pdf#page=11)
- **Printed inputs / direct observation:** Main range6665–31575; hospitalL6655, all other UC hospitals≥6655.
- **Reproducible rule, calculation and tolerance:** Exact minimum of21 source hospital-day values;UC minimum=min(10164,6655,8941,8917,11705,12126,13335,16077,14304,28698,31575)=6655. Printed6665 differs by10; integer tolerance0.
- **Inference and alternatives:** Matched11hospital populations andsame baseline phase; alternate10day definition not disclosed.
- **Primary category proposed:** Cross-document numeric inconsistency.
- **Relationships:** N008,N082; inferential families cross-referenced in canonical S inventory where relevant.
- **Quality-control relevance:** A copied numeric value or denominator may change downstream extraction or reconstruction; the package does not establish any effect on the paper's conclusion.
- **Exact human question:** Which baseline minimum belongs in Figure1, and is any hospital-level denominator intended to differ from eTable3?

## NUM-02 — Usual-care intervention discharge maximum

- **Exact locations and document roles:** [Figure1 UC intervention andanalysis REPORT](../../../jama_parshuram_2018_oi_180015.pdf#page=3); [eTable2 hospitalT REPORT](../../../joi180015supp3_prod.pdf#page=9)
- **Printed inputs / direct observation:** Figure1 twice prints discharge range3672–29956;hospitalT26956 and all otherUCpost counts≤26956.
- **Reproducible rule, calculation and tolerance:** max(7285,5642,3811,3672,4638,5471,6440,7327,5886,26956,17238)=26956;difference3000; exactinteger tolerance0.
- **Inference and alternatives:** A different hospitalization count would require population redefinition, but group94366 andothercounts match.
- **Primary category proposed:** Cross-document numeric inconsistency.
- **Relationships:** N011,N069; inferential families cross-referenced in canonical S inventory where relevant.
- **Quality-control relevance:** A copied numeric value or denominator may change downstream extraction or reconstruction; the package does not establish any effect on the paper's conclusion.
- **Exact human question:** Is29956 an incorrect maximum, or does Figure1 use a different site discharge dataset?

## NUM-03 — Mortality power absolute reduction percentage

- **Exact locations and document roles:** [Power appendix PLAN](../../../joi180015supp1_prod.pdf#page=29); [Sample size section PLAN](../../../joi180015supp1_prod.pdf#page=14)
- **Printed inputs / direct observation:** p29 18%relative reduction corresponds to0.9%absolute;baseline5.1/1000. p14 gives0.09%absolute.
- **Reproducible rule, calculation and tolerance:** .18×.0051=.000918 probability=.0918percentage points≈.09%, or.918/1000≈.9/1000. Printed0.9% is factor≈10. Ordinary .9%±.05percentage point incompatible with .09%.
- **Inference and alternatives:** Rounded relative reduction permits .09%; neither backgroundbaseline3.2/1000 nor percentversusper 1000  rescues .9% without changingunit.
- **Primary category proposed:** Measure, label, or scale inconsistency.
- **Relationships:** N017,N037; inferential families cross-referenced in canonical S inventory where relevant.
- **Quality-control relevance:** A copied numeric value or denominator may change downstream extraction or reconstruction; the package does not establish any effect on the paper's conclusion.
- **Exact human question:** Should the appendix absolute reduction be0.09%/0.9per 1000 , or is a different baseline intended?

## NUM-04 — Historical unplanned ICU admission percentage

- **Exact locations and document roles:** [Ontario table PLAN](../../../joi180015supp1_prod.pdf#page=30)
- **Printed inputs / direct observation:** 1052 unplanned PICU admissions;7300 PICU discharges;14.5%/PICU discharges.
- **Reproducible rule, calculation and tolerance:** 100×1052/7300=14.4109589%;nearest0.1%→14.4%, discrepancy.0890411percentage point>tolerance.05.
- **Inference and alternatives:** Historicalcounts may have different inclusion/time basis, but suppliedtable explicitly names7300 denominator;ordinarytruncation also14.4%.
- **Primary category proposed:** Denominator, proportion, or total inconsistency.
- **Relationships:** N038; inferential families cross-referenced in canonical S inventory where relevant.
- **Quality-control relevance:** A copied numeric value or denominator may change downstream extraction or reconstruction; the package does not establish any effect on the paper's conclusion.
- **Exact human question:** What count or discharge denominator yields the printed14.5%?

## NUM-05 — Historical unplanned ICU admissions per hospital discharges

- **Exact locations and document roles:** [Ontario table PLAN](../../../joi180015supp1_prod.pdf#page=30)
- **Printed inputs / direct observation:** 1052 unplanned PICU admissions;55963 hospital admissions/discharges;18/1000hospitaldischarges.
- **Reproducible rule, calculation and tolerance:** 1000×1052/55963=18.7981366;nearestinteger19, not18;discrepancy.79814>.5.
- **Inference and alternatives:** Truncation to integer produces18 and is possible; source does not state truncation and otherrows are compatible withnearestrounding. Conditional roundingquestion retained.
- **Primary category proposed:** Denominator, proportion, or total inconsistency.
- **Relationships:** N038; inferential families cross-referenced in canonical S inventory where relevant.
- **Quality-control relevance:** A copied numeric value or denominator may change downstream extraction or reconstruction; the package does not establish any effect on the paper's conclusion.
- **Exact human question:** Was18 intentionally truncated, or do denominator/numerator/time period differ?

## NUM-06 — Stat-call power absolute reduction product

- **Exact locations and document roles:** [StatCalls PLAN](../../../joi180015supp1_prod.pdf#page=30)
- **Printed inputs / direct observation:** Baseline8.13/1000days;RRR.181;ARR1.45calls/1000days.
- **Reproducible rule, calculation and tolerance:** 8.13×.181=1.47153/1000. Propagating printedprecision:8.125≤baseline<8.135 and.1805≤RRR<.1815 givesARR1.4665625–1.4765025;printed1.45 interval1.445–1.455 does notoverlap.
- **Inference and alternatives:** IfRRR recalculated usingunprinted input,requiredRRR1.45/8.13≈.17835 differs from.181 atprintedprecision. Other analysis assumptions unprinted, so not redoingpower.
- **Primary category proposed:** Numeric or arithmetic inconsistency.
- **Relationships:** N038; inferential families cross-referenced in canonical S inventory where relevant.
- **Quality-control relevance:** A copied numeric value or denominator may change downstream extraction or reconstruction; the package does not establish any effect on the paper's conclusion.
- **Exact human question:** Which ofbaseline,RRR,orARR should be reconciled, and wasARR calculated from an unstated power scenario?

## NUM-07 — Code-blue absolute reduction denominator phrase

- **Exact locations and document roles:** [CodeBlue PLAN](../../../joi180015supp1_prod.pdf#page=30)
- **Printed inputs / direct observation:** Baseline0.75/1000patient days,RRR.41;ARR printed '0.3/1000 events per thousand patient days'.
- **Reproducible rule, calculation and tolerance:** Product.75×.41=.3075 events/1000patient days→.3. Literal'.3/1000eventsperthousanddays' applies an additional1000 divisor: .0003events/1000days, factor1000 away. Numeric.3 coherent if one divisor is redundant.
- **Inference and alternatives:** Phrase may be typographical redundancy; no claim the actualpower analysis applied extra divisor.
- **Primary category proposed:** Measure, label, or scale inconsistency.
- **Relationships:** N038; inferential families cross-referenced in canonical S inventory where relevant.
- **Quality-control relevance:** A copied numeric value or denominator may change downstream extraction or reconstruction; the package does not establish any effect on the paper's conclusion.
- **Exact human question:** Should the ARR unit read0.3eventsper 1000 patient days with a single denominator?

## NUM-08 — Identity Poisson exposure and treatment coefficient scale

- **Exact locations and document roles:** [SAP lines114–131 PLAN](../../../joi180015supp2_prod.pdf#page=3)
- **Printed inputs / direct observation:** Comment saysNlin coefficient isusualcareintercept andNlinG coefficientrate difference. CodeNlin=N/1000;GNlin=N×(Group==BedsidePEWS);x~Nlin+GNlin+BNlin−1.
- **Reproducible rule, calculation and tolerance:** Ignore malformedvariable assignment as a separate syntaxissue;symbolicallyx=Nα/1000+N×Iβ+N×baselineγ. DividebyN/1000:eventsper 1000 days=α+1000Iβ+1000baselineγ. GNlin coefficientβ isdifferenceper day, whileinterceptα isper 1000 days; conversionfactor1000 exact.
- **Inference and alternatives:** NamedNlinGvsGNlin may be a drafting typo; actual production code may haveconsistent scaling or later coefficient rescaling, not supplied. Cannot assert fitted reports are wrong.
- **Primary category proposed:** Measure, label, or scale inconsistency.
- **Relationships:** N040; inferential families cross-referenced in canonical S inventory where relevant.
- **Quality-control relevance:** A copied quantity definition or scale may change downstream extraction or reconstruction; the package does not establish any effect on the paper's conclusion.
- **Exact human question:** Wereall exposure-derivedcolumns scaled identically, or was the reportedtreatment coefficient multipliedby1000 beforeinterpretation?

## NUM-09 — PIM predicted mortality denominator and scale in SAP

- **Exact locations and document roles:** [ICU table PLAN](../../../joi180015supp2_prod.pdf#page=7); [eTable4 REPORT](../../../joi180015supp3_prod.pdf#page=12); [eTable4 denominator/prediction footnotes REPORT](../../../joi180015supp3_prod.pdf#page=13)
- **Printed inputs / direct observation:** SAP row labelPIMII PredictionMortality(/1000urgentICUdischarges) butdescriptionaverageprobabilityoveradmissions andone recordper patient. eTable4 N(%) uses393/686/531/967patients andfootnotepercentageoftotalpatients.
- **Reproducible rule, calculation and tolerance:** Probabilityq becomes100qpercent or1000q per 1000 . Averaging within patient then across patients doesnotcreate a perICUdischarge quantitywhenmultiple admissions; exactfactor10betweenpercent andper 1000 , plusdistinctdenominatorunit.
- **Inference and alternatives:** Table title may be unupdated SAPshell; productionanalysis could be fullycoherent. InternalP_P label/description plusP_R report comparison; coordinator derivesprecedence.
- **Primary category proposed:** Measure, label, or scale inconsistency.
- **Relationships:** N042; inferential families cross-referenced in canonical S inventory where relevant.
- **Quality-control relevance:** A copied quantity definition or scale may change downstream extraction or reconstruction; the package does not establish any effect on the paper's conclusion.
- **Exact human question:** ShouldSAP label use predictedmortality probability/percentageper patient, or did a discharge-basedanalysis underlie a differentquantity?

## NUM-10 — Cardiac arrest intensity scale values

- **Exact locations and document roles:** [Clinical endpoint definition PLAN](../../../joi180015supp1_prod.pdf#page=11); [Table6 legend PLAN](../../../joi180015supp1_prod.pdf#page=27); [Table5 PLAN](../../../joi180015supp1_prod.pdf#page=24)
- **Printed inputs / direct observation:** Cardiacarrestp11 intensity6or7;Table6legendp27 cardiac arrestscale4or5. Table5 six/seven arecompressions/ECMOorwarddeath, four/fivecirculatorysupport±intubation.
- **Reproducible rule, calculation and tolerance:** Discrete categorical identityrule: {4,5}≠{6,7};notrounding, tolerance0;scalelabel inconsistent forsameendpoint.
- **Inference and alternatives:** Table6 mightrefer toearlierversion ofscale, butboundprotocol hasno namedalternate4/5cardiac arrestscheme.
- **Primary category proposed:** Measure, label, or scale inconsistency.
- **Relationships:** N035; inferential families cross-referenced in canonical S inventory where relevant.
- **Quality-control relevance:** A copied quantity definition or scale may change downstream extraction or reconstruction; the package does not establish any effect on the paper's conclusion.
- **Exact human question:** Which intensitycategories shouldtrigger cardiac arrest dataabstraction inTable6?

## NUM-11 — Preventability threshold excludes and includes category 4

- **Exact locations and document roles:** [Preventability definition PLAN](../../../joi180015supp1_prod.pdf#page=11); [Table7 PLAN](../../../joi180015supp1_prod.pdf#page=28)
- **Printed inputs / direct observation:** p11 consensusrating>4;immediately lists4,5,6 aspreventable. Table7rating 4 or more.
- **Reproducible rule, calculation and tolerance:** Oninteger6-pointscale >4→{5,6},≥4→{4,5,6};category 4membership contradictory; tolerance0.
- **Inference and alternatives:** Likely a comparator typo; no claimhowmany trialeventswould change becauseevent ratings not supplied.
- **Primary category proposed:** Denominator, proportion, or total inconsistency.
- **Relationships:** N035; inferential families cross-referenced in canonical S inventory where relevant.
- **Quality-control relevance:** A copied quantity definition or scale may change downstream extraction or reconstruction; the package does not establish any effect on the paper's conclusion.
- **Exact human question:** Wascategory 4 intended tocount aspotentially preventable, and shouldthe comparatorbe≥4?

## NUM-12 — PIM inverse-logit upper example probability

- **Exact locations and document roles:** [eTable1 PIM definition REPORT](../../../joi180015supp3_prod.pdf#page=7); [eTable4 footnotesb/c REPORT](../../../joi180015supp3_prod.pdf#page=13)
- **Printed inputs / direct observation:** PIMscore+9.7778, predictedmortality99.9%;inverse-logit1/(1+exp(−PIM)) supplied;minimum−8.4137→.02%.
- **Reproducible rule, calculation and tolerance:** 100/(1+exp(−9.7778))=99.9943306823%,nearest0.1percentage point100.0%, discrepancy.0943307>.05. Score±.00005 barelychanges result. Minimumgives.02218%, coherent. BE−35 occursbothlocations (p13minus wrapsline), not+35.
- **Inference and alternatives:** Truncation orceiling99.9% mayintentionallyavoid100%;rule notstated. Highprobability notliteralcertainty. Retainconditionaldisplayquestion only.
- **Primary category proposed:** Numeric or arithmetic inconsistency.
- **Relationships:** N045,N048; inferential families cross-referenced in canonical S inventory where relevant.
- **Quality-control relevance:** A copied quantity definition or scale may change downstream extraction or reconstruction; the package does not establish any effect on the paper's conclusion.
- **Exact human question:** Is99.9% anintentionaldisplaycap/truncation, or shouldnumericalexample followstatedinverse-logitandrounding?

## NUM-13 — Anticipated pediatric ward bed total

- **Exact locations and document roles:** [Sample assumptions PLAN](../../../joi180015supp1_prod.pdf#page=14); [Power appendix PLAN](../../../joi180015supp1_prod.pdf#page=29); [eTable5 anticipated REPORT](../../../joi180015supp3_prod.pdf#page=14)
- **Printed inputs / direct observation:** Protocol2322totalbedswith99389admissions/397556days;appendixmean119.85beds,n20;reportanticipated2397beds withsame99389/397556.
- **Reproducible rule, calculation and tolerance:** 2397−2322=75beds;119.85×20=2397 exact. Printedhistoricalcount2322differs fromreportanticipatedcount2397;rounding tolerance0 forcounts.
- **Inference and alternatives:** Reportmightpresentstandardizedpowerinput20×119.85 instead ofparticipating-sitehistoricaltotal; then2397isderivedassumption, nottranscriptionerror. Sameadmission/dayinputs makecomparisonrelevant; missingbasis retained.
- **Primary category proposed:** Cross-document numeric inconsistency.
- **Relationships:** N037,N049; inferential families cross-referenced in canonical S inventory where relevant.
- **Quality-control relevance:** A copied numeric value or denominator may change downstream extraction or reconstruction; the package does not establish any effect on the paper's conclusion.
- **Exact human question:** DoesAnticipated2397 representactualpretrialsitebeds or20×assumedmean, andshouldfootnote distinguishit fromprotocol2322?

## NUM-14 — Historical Ontario urgent ICU admission annualization

- **Exact locations and document roles:** [SCDE sample assumption PLAN](../../../joi180015supp1_prod.pdf#page=14); [HistoricalOntario table/narrative PLAN](../../../joi180015supp1_prod.pdf#page=30)
- **Printed inputs / direct observation:** p14 1052 urgentICUadmissions/yearfrom4Ontariocenters;p30same1052 over2yearsfollowing31January2007.
- **Reproducible rule, calculation and tolerance:** Ifsame cohort,timeannualized1052/2=526/year;rate1052/year doublesannualcount. Exactfactor2, tolerance0 afterperiodmatch.
- **Inference and alternatives:** A differenthistoricalcohortorupdatedannualseries mayyieldsamecount1052, but source doesnotdistinguishthese series. This isconditionalmatchedcohort discrepancy, not an assumptionthatallhistoricalcounts align.
- **Primary category proposed:** Rate-versus-count inconsistency.
- **Relationships:** N037,N038; inferential families cross-referenced in canonical S inventory where relevant.
- **Quality-control relevance:** A copied numeric value or denominator may change downstream extraction or reconstruction; the package does not establish any effect on the paper's conclusion.
- **Exact human question:** Does1052refer toannualdata atp14 or2-yearaggregate atp30, orarethese independently defined cohorts?

## NUM-15 — Most senior overnight ICU physician categories leave two BP hospitals

- **Exact locations and document roles:** [Table1 ICUstaffing andeligibility footnote REPORT](../../../jama_parshuram_2018_oi_180015.pdf#page=5)
- **Printed inputs / direct observation:** BP10hospitals;mostseniorICUphysicianovernight staff2(20%),fellow5(50%),resident1(10%);usualcare1+3+7=11.
- **Reproducible rule, calculation and tolerance:** Forone mostseniorcategoryperhospital,2+5+1=8 vs10;percentagecolumns sum20+50+10=80%, leaving2hospitals/20%; countsindividuallycorrect. Conditionalexhaustivenessconstraint, tolerance0.
- **Inference and alternatives:** Unlistedstaffcategory,unavailableovernightphysician ormissingdata mayaccountfor2;footnoteallhadpediatricICUstaffdoesnotbyitselfassertallstaffovernight. Do not turninto generic staffingcritique.
- **Primary category proposed:** Denominator, proportion, or total inconsistency.
- **Relationships:** N021; inferential families cross-referenced in canonical S inventory where relevant.
- **Quality-control relevance:** A copied numeric value or denominator may change downstream extraction or reconstruction; the package does not establish any effect on the paper's conclusion.
- **Exact human question:** WhatmostseniorovernightICUstaffcategory ormissing-data statusaccountsfortheother2BP hospitals?

## NUM-16 — SAP shell count outcomes headed Continuous outcomes

- **Exact locations and document roles:** [Shell Tables PLAN](../../../joi180015supp2_prod.pdf#page=5); [binary/count taxonomy PLAN](../../../joi180015supp2_prod.pdf#page=1)
- **Printed inputs / direct observation:** ShellheadingContinuousoutcomes;rowsResuscitationCalls,StatCalls,UrgentConsults,UrgentICUAdmissions,ICU/HospitalReadmissions, eachcount/denominator andPoisson. p1 separatestheseeventsascount outcomes.
- **Reproducible rule, calculation and tolerance:** Count/denominatorisrateorproportion;Poissonconditionalresponsecount isdiscrete, notcontinuousmeasurement. Sixrowlabels contrastedwithshell heading;exacttypeidentity, no rounding.
- **Inference and alternatives:** Headingmaymeanrate-summaryvariables acrosshospitals, continuousderivedratiosrather thanresponsecounts;sourceusesmodel classes elsewhere. Doesnotimplynumericestimateswrong.
- **Primary category proposed:** Measure, label, or scale inconsistency.
- **Relationships:** N041; inferential families cross-referenced in canonical S inventory where relevant.
- **Quality-control relevance:** A copied numeric value or denominator may change downstream extraction or reconstruction; the package does not establish any effect on the paper's conclusion.
- **Exact human question:** DoesContinuousoutcomes merelynamehospitalrate summaries, orshouldheadingidentifycount/rateoutcomesandtheir actualmodel response?

## NUM-17 — SAP readmission shell Poisson versus reported binary logistic labels

- **Exact locations and document roles:** [Readmission shellrows PLAN](../../../joi180015supp2_prod.pdf#page=5); [Binary/count rules PLAN](../../../joi180015supp2_prod.pdf#page=1); [Table3 readmissions andfootnoted REPORT](../../../jama_parshuram_2018_oi_180015.pdf#page=7)
- **Printed inputs / direct observation:** SAPbothreadmissionsPoisson withdischargedenominators;mainICUreadmissionOR1.11, hospitalreadmissionOR.93, logisticfootnoted;SAPbinaryrules usedischargesforbinary andpatient daysforcount.
- **Reproducible rule, calculation and tolerance:** Effectmeasuremodel identity:Poissonloglink yieldsrate/riskratio, binomiallogitOR. Discharge denominator alone doesnot makeaPoissonimpossible;directmismatch isnamedPoissonversusreportedlogisticOR, not deriveddisapproval.
- **Inference and alternatives:** Plans mayhave changed,Poissoncould be exploratorysensitivity,or shell may be mislabeled. Actualanalysisnotreconstructed;protocolp16logitcorroboratesreport butdoesnotadddiscrepancy.
- **Primary category proposed:** Measure, label, or scale inconsistency.
- **Relationships:** N041; inferential families cross-referenced in canonical S inventory where relevant.
- **Quality-control relevance:** A copied quantity definition or scale may change downstream extraction or reconstruction; the package does not establish any effect on the paper's conclusion.
- **Exact human question:** WerePoissonreadmission rows alternate analyses, orwereplannedprimary modelsupdated tologistic, andwhichlabelsgovern?

## NUM-18 — Historical AUC range upper endpoint scale

- **Exact location and document role:** [Protocol p6, Systematic Reviews, PLAN](../../../joi180015supp1_prod.pdf#page=6).
- **Printed inputs / direct observation:** Adult early warning scores discriminate ICU from high dependency patients with “AUCROC 0.83-86”.
- **Rule, calculation and tolerance:** An AUC expressed on the probability scale lies between 0 and 1. A literal upper endpoint of 86 exceeds 1 by 85; decimal rounding cannot account for this. If 86 represents an abbreviated decimal suffix, the range is 0.83–0.86 and is coherent.
- **Inference and alternatives:** The absent decimal may be shorthand or a small transcription defect. The scientific result cannot be reconstructed from the supplied historical summary; no external article was consulted. The observation concerns the printed scale and potential ambiguity in downstream extraction.
- **Primary category proposed:** Measure, label, or scale inconsistency.
- **Relationships:** N032; PLAN versus PLAN bound and label within the protocol.
- **Quality-control relevance:** A reader or automated extractor could preserve an impossible upper endpoint unless the decimal interpretation is explicit. No effect on trial conclusions is inferred.
- **Exact human question:** Is 86 an intentional abbreviated decimal endpoint, and should the range be written 0.83–0.86 to make the AUC scale explicit?

## Complete non-candidate review

Hospital tables:all21rows×4eTable2rates and21×6eTable3rates reconcile, as do20total-rowrates,21dischargeidentities andall30groupcolumn sum identities. All nonDNRdeathcountssubsetofalldeaths;allpotentially preventablearrestssubsetofcardiac arrests, whicharesubsetofdeterioration. MainTable3allprintedcruderates withavailabledenominators reconcile;the4postperiod ICUdenominator-dependent cells remain compatible with acommonintegerdenominator but exactdenominators areunprinted. Theyare not falselycertified againstanassumed denominator.

MainTable2: all28mean/SDcells coherent,4count/proportioncells correct;8109forms=1270+2588+1419+2832 and99%of8190afterrounding. Sevenmeasurement frequencies are per24hours and not the singlelast-set completenessvariable. AdjustedGEE means/proportions are not rawdifferences or simpledifference-in-differences. eTable4:all20rows with4group/timecells andall15inferredcomparisonfamilies covered;roundedpredicteddeathcounts are not exactintegers forpercentage reconstruction. Total-versusaverage LOS, firstadmissionventilatorfreedays,per patienttechnology sums andanyusebinaryvariables distinguished. Repeated rounded quartiles/counts do not themselves establish duplication.

Protocol historicalTable2:all22rows counts,medians/IQRs andAUCscales inspected;allage/hospital/eventsubgroup sums match1388controls+686cases=2074. Other historicalstudies not pooled acrosscohorts. All14mortalityrates average5.10642857→5.11. Historical mortality2202/678365×1000=3.246→3.2. Power SCDE2×.31=.62;codeblue.75×.41=.3075→.3 andstatcalls8.13×.181=1.47153(exceptionNUM-06). Fullclusterpowerformula unavailable locally; no claimpowerwrongfromunreportedvariance inputs. Nuisance model syntax typos alone are outside this numeric scientific scope.

eTable5 anticipateddeaths99389×.0051=506.8839→507;SCDE397556×.002=795.112→795;actualpostdays559443,discharges144539,deaths244,SCDE386 allmatch mainandsitetables;observed1.7/.69rates coherent. Nominalbetween-clusterSD.00076/.00071 not forcedtoequalκ times the crudeaggregate becausehospitalweighted/unweightedmeans andBayesianκ estimates differ.

## Limitations

Direct text uses suppliedPDFsin English;nativefont warnings didnot preventcell reading. Complete page-unitmaps supply scope;only target directPDFpages were re-extracted fornumeric confirmation, withno OCR needed. This lane didnot certify graphmarker coordinates or fittedmodels:graph group/axis encodings are assigned to cross-sourcechecker andinferentialuncertainty to two statisticalpasses. Lackof raw data/unrounded probabilities or exactpost ICU discharges limitscalculation, notsource coverage. All relationships have explicit outcomes; every candidate remains forcoordinator merge andexactsource recheck.

