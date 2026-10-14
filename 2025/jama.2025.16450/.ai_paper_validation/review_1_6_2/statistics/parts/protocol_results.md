# Inferential-statistical inventory: protocol and results supplement

Scope DOC-002 PLAN pp1–35 and DOC-005 REPORT pp1–16. Extraction only; no candidate adjudication or diagnostic calculation. S201–S279: 79 relationships (19 prospective specifications, 33 eTable3 results including NA rows, 20 eTable4 results, one eTable4 method definition, six historical locator groups). Each row retains exact analysis identity and is a required input to both later statistical passes. Complete printed counts/percentages/means/quartiles and every footnote are retained in extraction/parts/protocol_results.md. N groups provide cross-reference. Effect direction is budesonide+surfactant relative to surfactant alone for all eTable results. Headers SAF322/313 are participant totals, not automatically each nonmissing outcome denominator. No estimate is assumed crude where model adjustment is specified.

## Prospective protocol specifications

| ID | Exact PLAN location | Statistical relationship | Matching main-paper key |
|---|---|---|---|
| S201 | DOC-002 pp4,7,20 | PrimaryphysiologicBPD/death36w;ITTallrandomized;superioritydirectionlowerincidence | Primary outcome/status/definition |
| S202 | DOC-002 pp4,17–18 | Individual1:1block-urnrandomization,NICU×GA<26/≥26w;independentmultiples;kit-openingrandomization | Randomization unit/stratification |
| S203 | DOC-002 pp5,7,21 | Secondarydeath36w | Mortality secondary status |
| S204 | DOC-002 pp5,7,21 | SecondaryphysiologicBPD36w | BPD secondary status |
| S205 | DOC-002 pp5,7,21 | SecondaryJensenordinalseverity36w,support-definedfourlevels | BPDseverity ordinal analysis |
| S206 | DOC-002 pp5,7,21 | Secondarygrade3BPD36w | Grade3binary status |
| S207 | DOC-002 pp5,7,21 | Secondarypostnatalsteroids7dPLDthrough36w | Steroid outcome/window |
| S208 | DOC-002 pp5,7,21 | SecondaryNDI,death,NDI/death22–26moCA;NDIdefinitionagreedatfirstfollowup | Deferred long-term endpoint status |
| S209 | DOC-002 pp5,21–23 | ExploratoryNIHseverity,ventilationdays28/36w,intubationafter50h28/36w,repeat surfactant after50hto7dPLD,wheeze/cough22–26mo | Exploratory outcome hierarchy |
| S210 | DOC-002 pp5,22–23,27 | SafetyAE7d168h,SIP/PVL30d720h,ICH3-daygrace,growth36w;recording/severityrules | Safety endpoint/windows |
| S211 | DOC-002 p25§5.1 | PrimaryrobustPoisson,sandwichvariance,fixedNICUanddichotomousGA;lowvolume/convergenceNICUpoolingwithincenter | Primarymodel/covariates |
| S212 | DOC-002 p25§5.1 | Continuouslinear,binaryrobustPoisson,countPoisson,ordinalproportionalodds,nominalgeneralizedlogits;fixedstratifiers | Secondary model families |
| S213 | DOC-002 p25§5.1 | ITTprimary/secondaryefficacy,asreceivedsafetyandprespecifiedsecondaryasreceived | Analysis populations/sensitivity |
| S214 | DOC-002 p25§5.1 | Missingdata/lossapproachdeferredtoSAPbeforeunmaskedreview | Missing-data specification |
| S215 | DOC-002 pp25–26§5.2Table5 | Primarypower58%vs48%,RRnull1,twosidedoverallalpha.05/final.044,90%;539/armtwoproportion,550/armrobustPoissonsimulation,5%attritiontarget1160;Table5all6cells | Power/sample-size assumptions |
| S216 | DOC-002 pp25–26§5.2 | Secondarycomparisonsdescriptive;printedassertiongreaterbaseline>58%givesgreaterpowerfor10pointreduction | Multiplicity/power assertion |
| S217 | DOC-002 pp28–29§5.5.2.1 | SafetyPocockLan-DeMetsat40/~3%,25/50/75%with.0033/.0196/.0212/.0214;robustPoissonfixedsite/GA,possiblepooling/site-randomGLMM | Safety monitoring |
| S218 | DOC-002 p29§5.5.2.2 | EfficacyLan-DeMetsO'Brien-Flemingat25/50/75%,alpha.000015/.0030/.0183,final.0440overall.05;actualinformationdependent | Efficacy monitoring |
| S219 | DOC-002 p29§5.5.2.3 | Futilityupper2sided80%CIofconditionalpowerfails>.50at50%or>.30at75%;discretionaryslowenrollment | Futility decision rule |

## eTable 3: adverse-event participant experience

Methods DOC-005 p6: default robust Poisson adjusted GA strata and pooled center, RR95%CI, alpha.05 descriptive only. Superscript b is crude unadjusted OR with exact95%CI used to approximate RR for low prevalence; superscript e is Mantel-Haenszel common OR approximating RR stratified by GA×pooledcenter for convergence; burden c uses Wilcoxon rank sum P. These stated exceptions are retained separately. All event windows/death definitions from p6 apply. An NA interval/result is explicitly tracked.

| ID | REPORT source location/outcome | Budesonide / surfactant printed counts or summary | Printed estimate (95% CI) or P | Method exception |
|---|---|---|---|---|
| S220 | DOC-005 p5AnyAE |242(75.4%)/202(64.5%)|1.16(1.05,1.28)|Default |
| S221 | DOC-005 p5AnyAEofinterest |240(74.8%)/193(61.7%)|1.20(1.09,1.33)|Default |
| S222 | DOC-005 p5AEtubeblockage |3(.9%)/4(1.3%)|.73(.16,3.28)|b crudeOR/exactCI |
| S223 | DOC-005 p5AEhypoxemia/bradycardia |2(.6%)/3(1.0%)|.65(.11,3.90)|b crudeOR/exactCI |
| S224 | DOC-005 p5AEpulmonaryairleak |16(5.0%)/18(5.8%)|.86(.45,1.66)|Default |
| S225 | DOC-005 p5AEhypotension |56(17.4%)/59(18.8%)|.92(.67,1.27)|Default |
| S226 | DOC-005 p5AEhypertension |28(8.7%)/21(6.7%)|1.28(.75,2.10)|Default |
| S227 | DOC-005 p5AEhyperglycemia |214(66.7%)/156(49.8%)|1.33(1.17,1.51)|Default |
| S228 | DOC-005 p5AEintracranialhemorrhage |40(12.5%)/37(11.8%)|1.03(.69,1.54)|Default |
| S229 | DOC-005 p5AEearlysepsis |9(2.8%)/8(2.6%)|1.06(.41,2.75)|Default |
| S230 | DOC-005 p5AElatesepsis |70(22.4%)/70(23.7%)|.93(.70,1.24)|Default |
| S231 | DOC-005 p5AEPVL |15(4.8%)/13(4.3%)|1.09(.52,2.26)|Default |
| S232 | DOC-005 p5AESIP |17(5.3%)/9(2.9%)|1.82(.83,4.02)|Default |
| S233 | DOC-005 p5AEother |27(8.4%)/32(10.2%)|.80(.50,1.30)|Default |
| S234 | DOC-005 p5AEpulmonaryhemorrhage |11(3.4%)/14(4.5%)|.75(.35,1.62)|Default |
| S235 | DOC-005 p5AEburdenevents/participant |Mean1.6(1.5)/1.3(1.4);median1(1,2)/1(0,2)|P=.004|c Wilcoxon |
| S236 | DOC-005 p5AnySAE |64(19.9%)/54(17.3%)|1.13(.82,1.55)|Default |
| S237 | DOC-005 p5AnySAEofinterest |53(16.5%)/42(13.4%)|1.20(.83,1.73)|Default |
| S238 | DOC-005 p5AnyfatalSAE |22(6.9%)/25(8.0%)|.84(.49,1.44)|Default;d windowdefinition |
| S239 | DOC-005 p5SAEtubeblockage |1(.3%)/1(.3%)|.98(.06,15.66)|b crudeOR/exactCI |
| S240 | DOC-005 p5SAEhypoxemia/bradycardia |1(.3%)/2(.6%)|.49(.04,5.39)|b crudeOR/exactCI |
| S241 | DOC-005 p5SAEairleak |5(1.6%)/12(3.8%)|.37(.13,1.06)|e stratifiedMHcommonOR |
| S242 | DOC-005 p5SAEhypotension |13(4.0%)/8(2.6%)|1.53(.64,3.63)|Default |
| S243 | DOC-005 p5SAEhypertension |0(0.0%)/1(.3%)|NA|b crudeOR/exactCI indicated |
| S244 | DOC-005 p6SAEhyperglycemia |8(2.5%)/3(1.0%)|2.64(.69,10.05)|b crudeOR/exactCI |
| S245 | DOC-005 p6SAEintracranialhemorrhage |17(5.3%)/19(6.1%)|.85(.45,1.58)|Default |
| S246 | DOC-005 p6SAEearlysepsis |4(1.2%)/2(.6%)|1.96(.36,10.79)|b crudeOR/exactCI |
| S247 | DOC-005 p6SAElatesepsis |5(1.6%)/2(.6%)|2.46(.47,12.78)|b crudeOR/exactCI |
| S248 | DOC-005 p6SAEPVL |0(0.0%)/0(0.0%)|NA|No estimated contrast |
| S249 | DOC-005 p6SAESIP |15(4.7%)/9(2.9%)|1.61(.72,3.61)|Default |
| S250 | DOC-005 p6SAEother |18(5.6%)/20(6.4%)|.84(.46,1.55)|Default |
| S251 | DOC-005 p6SAEpulmonaryhemorrhage |8(2.5%)/8(2.6%)|.94(.35,2.48)|Default |
| S252 | DOC-005 p6SAEburdenevents/participant |Mean.3(.6)/.3(.6);median0(0,0)/0(0,0)|P=.42|c Wilcoxon |

## eTable 4: clinical and growth outcomes

Methods DOC-005 p8: binary robust Poisson RR; continuous robust normal-identity GLM least-squares MD; both adjusted GA strata and pooled center. SAF as received322/313. Binary denominator = number with nonmissing outcome. Alpha.05 descriptive. Clinical outcomes GDBin-hospitalstatus≤120d or earlier death/transfer/home;NEC/PDA/ROP unavailable for death<12h. Growth36w unavailable if GDBstatus<35w, standardized Olsen2010;clinicaldeathcomposite120d,growthdeathcomposite36w. Outcome rows below map S253–S272. No Pvalues printed in these rows.

| ID | REPORT source location/outcome | Budesonide / surfactant printed data | Printed contrast (95% CI) | Method |
|---|---|---|---|---|
| S253 | DOC-005 p7death120dPNA |50/321(15.6%)/44/313(14.1%)|RR1.09(.76,1.57)|Poisson |
| S254 | DOC-005 p7NECorDeath |77/320(24.1%)/72/313(23.0%)|RR1.04(.79,1.37)|Poisson |
| S255 | DOC-005 p7NEC |35/319(11.0%)/40/308(13.0%)|RR.85(.56,1.29)|Poisson |
| S256 | DOC-005 p7PDAorDeath |182/320(56.9%)/197/313(62.9%)|RR.89(.79,1.00)|Poisson |
| S257 | DOC-005 p7PDA |159/319(49.8%)/175/308(56.8%)|RR.86(.75,.99)|Poisson |
| S258 | DOC-005 p7PDAmedicaltherapyorDeath |121/316(38.3%)/128/311(41.2%)|RR.91(.76,1.09)|Poisson |
| S259 | DOC-005 p7PDAmedicaltherapy |84/315(26.7%)/98/306(32.0%)|RR.80(.64,1.01)|Poisson |
| S260 | DOC-005 p7PDAsurgery/catheterorDeath |54/320(16.9%)/47/313(15.0%)|RR1.11(.78,1.57)|Poisson |
| S261 | DOC-005 p7PDAsurgery/catheter |5/319(1.6%)/3/308(1.0%)|RR1.62(.38,6.83)|b crudeOR/exactCI |
| S262 | DOC-005 p7stage3ROPorDeath |87/318(27.4%)/83/310(26.8%)|RR1.02(.80,1.29)|Poisson |
| S263 | DOC-005 p7stage3ROP |37/277(13.4%)/40/270(14.8%)|RR.87(.60,1.28)|Poisson |
| S264 | DOC-005 p7weightzscore36w |−1.1(.9)/−1.2(.8)|MD.07(−.08,.22)|NormalidentityGLM |
| S265 | DOC-005 p7weight<10thpercentile |107/261(41.0%)/113/259(43.6%)|RR.95(.78,1.15)|Poisson |
| S266 | DOC-005 p7weight<10thorDeath |155/309(50.2%)/154/300(51.3%)|RR.98(.84,1.14)|Poisson |
| S267 | DOC-005 p7lengthzscore36w |−2.0(1.0)/−2.0(1.0)|MD.04(−.12,.21)|NormalidentityGLM |
| S268 | DOC-005 p7length<10thpercentile |201/261(77.0%)/201/259(77.6%)|RR.99(.90,1.08)|Poisson |
| S269 | DOC-005 p7length<10thorDeath |249/309(80.6%)/242/300(80.7%)|RR1.00(.93,1.08)|Poisson |
| S270 | DOC-005 p7headcircumferencezscore36w |−1.5(1.0)/−1.6(1.0)|MD.04(−.132,.203)|NormalidentityGLM |
| S271 | DOC-005 p7headcircumference<10thpercentile |141/261(54.0%)/140/258(54.3%)|RR1.00(.85,1.16)|Poisson |
| S272 | DOC-005 p7headcircumference<10thorDeath |189/309(61.2%)/181/299(60.7%)|RR1.01(.89,1.14)|Poisson |
| S273 | DOC-005 p8method/quantitydefinitions |Headerp7RRrelative risk,footnotep8RR=riskdifference;binaryparagraphrelative risks;continuousleast-squaresMD,GA/centeradjustment;nonmissingdenominators/timewindows |Printed definitions retained exactly without diagnosis |Method/labels |

## Historical PLAN statistical locator groups

Historical figures in protocol rationale are retained in extraction with all printed numbers and tests. They are not BiB report outcomes. Each row names a complete bounded set for the checkers to open if needed; no prospective hypothesis is inferred from these data.

| ID | Exact PLAN location | Complete locator group |
|---|---|---|
| S274 | DOC-002 p10 | PriorRCTBPD/deathRR/CI/NNT,followupNDIandmeta-analysis3effects/intervals;fullprintedtriplesinextractionN235 |
| S275 | DOC-002 p11Table1 | All14demographicdescriptiverowswithP,294vs173historicalcohorts;fullrowsN236 |
| S276 | DOC-002 p12Table2 | All22respiratory/definition/timepointrowtests;chi-square/t/Mann-Whitneyfootnotes;fullrowsN237 |
| S277 | DOC-002 p13Tables3–4 | All16morbidity+16discharge/growthrowtestsandfootnotes;fullrowsN238 |
| S278 | DOC-002 p14 | PriorSIP13%vs4%P.02anddose-rangingdescriptives;fullN239 |
| S279 | DOC-002 p24 | SevenhistoricalRR/CI/Presults:death/BPD,BPD,death,PDAclosure,reintubation,NDI,long-termdeath;fullN240 |

No inferential tests appear in eTables1,2,5,6,7,8. Their counts, denominators, dose formulas and observation windows remain mapped as N225,N226,N229–N232 and support method relationships above. No subgroup or sensitivity result display occurs in these two assigned sources; protocol prespecifies as-received secondary analysis but provides no results. Complete source reading found no confidence intervals or Pvalues omitted from the source-linked result appendix.
