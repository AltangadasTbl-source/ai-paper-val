# Numeric consistency checker: protocol PDF pages1–128

Fresh disjoint numeric review of DOC-003, joi190092supp2_prod.pdf. Two bounded units: PE-N001–066 (globalN300–N365;66 relationships) and NPM001–089 (globalN366–N454;89 relationships), total155/155 groups checked. All constituent table rows, diagrams, grade categories, window columns and dose conversions were checked; arithmetic, totals, populations, denominators, missingness, scales, units, rate/count, reference/ordering, rounding and repeated-value tests were applied where meaningful. Prospective rules, administrative counts, instrument identifiers and historical estimates were kept distinct from observed trial results. No minimum/maximum or early stopping used. No old candidate/reports, external evidence, web or Python extraction used.

Every candidate below concerns PLAN content exclusively, including historical background and both prospectively supplied versions. All compared locations are PLAN; provisional relationship solely P_P. Document-role assignments follow content. Later amended rules alone were not candidates. NP-A–NP-O are local checker labels only; stable C IDs, judgments and dispositions are not assigned. No enrolled-patient effect, study-conclusion impact or actual event recoding is claimed. Candidates identify preventable quantitative or label ambiguity that could propagate when plan definitions are reused; human questions delimit missing information.

## Complete relationship coverage

All66 early and89 middle groups have one row each in ../relationships/numeric_protocol_early.md and ../relationships/numeric_protocol_middle.md. Every constituent row of originalTables1–10, finalTables1–10, trial-lens/axis-step tables, inflammation/cataractscales, source visual diagrams and equipment-unit conversions was examined. The original6–12extension timeline and original/finalboundaries were matched bydocumentversion. No inferentialtest/Pvaluewasprinted in these155numericgroups; the originalone-thirdinterimruleisassignedtostatisticalreview. No display-zerocandidate arose.

Fresh locator derivatives: preprocessing/numeric_protocol_source_pN.txt forN=11,16,22,26,27,36,43,44,45,50,52,53,87,103,110,117,123,124,125,126,127. Directcommand pdftotext -layout -f N -l N joi190092supp2_prod.pdf OUTPUT, Poppler26.01.0. These are new derivatives, not edits to supplied sources or reused assets. Existing mapped visualsourceimages pp15/19/80 and all14freshmiddlepages remain source-linked. Rechecker should visually confirm every cited page; text is locator, not final authority. Scientific coverage limitations: none. Missing supplied definitions are recorded in specific human questions.

## Source-grounded candidates

### NP-A: Planned maximum-follow-up completion predates eligible completion

- Relationships: N307 / PE-N008.
- Compared locations and document roles: [DOC-003 PDF p11](../../../joi190092supp2_prod.pdf#page=11) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: Table1: enrollment November2012–May2015; six-month follow-up+one-month window throughDecember2015; maximum12-month follow-up+one-month window throughJuly2015; database lock/analysis throughApril2016.
- Reproducible rule/calculation and tolerance: The latest May2015 entrants require at least May2016 for12months, and approximatelyJune2016 includingone-month window. July2015 is only2months afterMay2015, and is earlier than the separately printed December2015 six-month completion. Calendar arithmetic permits±1month ambiguity in month-only dates; discrepancy≥10months remains.
- Direct observation versus inference: Direct observation: all four dates are printed in one original-version table. Inference: follow-up duration is applied to the latest permissible entrant, rather than an actual enrollment record.
- Alternatives and missing definitions: July2015 could be a stale projected date or a subset deadline; table says finish maximum follow-up, without a subset qualifier. Later2017-version schedule is a disclosed different version and does not create this candidate.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Which enrollment cutoff and population are intended for the July 2015 maximum follow-up completion, and how does that date reconcile with the original May 2015 enrollment end?

### NP-B: Original leukocyte classification leaves exactly1000/μL without a class

- Relationships: N318 / PE-N019.
- Compared locations and document roles: [DOC-003 PDF p16](../../../joi190092supp2_prod.pdf#page=16) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: Table3: non-serious leukocytes >1000 and<2500/μL lasting less than1month; serious<2500 lastingmorethan1month or≤999/μL.
- Reproducible rule/calculation and tolerance: For a newly observed count exactly1000/μL,1000>1000 isfalse and1000≤999 isfalse. Before1month, neither printed class contains this value. Tolerance0 cells/μL for integer printed cutoffs.
- Direct observation versus inference: Direct observation: strict >1000 and≤999 differ by an uncovered integer. Inference: acute1000/μL test value demonstrates the gap; no patient with this value is claimed.
- Alternatives and missing definitions: Could reflect intended integer≥1000 non-serious or≤1000 serious, or discretionary clinical grading; finalversionp81 uses≤1000 and thus is a separate amended context.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Which class is intended for a leukocyte count exactly 1000/μL lasting less than one month in the original protocol?

### NP-C: Original platelet classes overlap at20000/μL

- Relationships: N318 / PE-N019.
- Compared locations and document roles: [DOC-003 PDF p16](../../../joi190092supp2_prod.pdf#page=16) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: Table3: non-serious platelets20000to75000/μL lasting less than1month; serious≤20000/μL or<75000/μL lastinggreaterthan1month.
- Reproducible rule/calculation and tolerance: For a count20000/μL newly observed, an inclusive20,000–75,000 interval includes it and≤20,000 also includes it. Exact printed integer boundary; tolerance0.
- Direct observation versus inference: Direct observation: same table supplies overlapping endpoints. Inference: interpreting “to” inclusively makes class non-unique at20000.
- Alternatives and missing definitions: Lower bound “to” could be intended open despite usual inclusive range notation; finalversionp81 serious<20000 is a different version and not independent mismatch.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Is 20000/μL a serious or non-serious platelet abnormality in the original Table 3, and is the lower boundary of its non-serious range inclusive?

### NP-D: Original AST/ALT event class differs at supplied boundary values

- Relationships: N320 / PE-N021; N364 / PE-N065.
- Compared locations and document roles: [DOC-003 PDF p16](../../../joi190092supp2_prod.pdf#page=16) (PLAN); [DOC-003 PDF p52](../../../joi190092supp2_prod.pdf#page=52) (PLAN); [DOC-003 PDF p53](../../../joi190092supp2_prod.pdf#page=53) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: p16Table3: non-serious AST/ALT2to5×ULN; serious>5×ULN. p52§6.1 example abnormal findings>2but<5×ULN. p53§6.2 serious≥5×ULN.
- Reproducible rule/calculation and tolerance: At exactly5×ULN, Table3 places value in2–5 non-serious range and excludesitfrom>5serious;§6.2 includes5 asserious. At exactly2×ULN Table3 includes2 but§6.1 example excludesit. Tolerance0 at dimensionless printed endpoints; primary contradiction is the explicit5×class boundary.
- Direct observation versus inference: Direct observation: same2012MOP has different inequalities for matching laboratory analytes. Inference: boundary-value substitutions reveal mutually different labels; no actual AE counts reconstructed.
- Alternatives and missing definitions: §6.1 examples could be nonexhaustive, so2×alone neednotcontradict. Table3mayhavepriority over prose, or viceversa, but no precedence printed. Finalversion amended Table3 notthecandidate.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: For original-protocol adverse-event coding, is AST/ALT exactly 5×ULN serious or non-serious, and which original section controls the boundaries?

### NP-E: Same-drug follow-up extension receives alternate-drug phase label

- Relationships: N328 / PE-N029; N303 / PE-N004; N334 / PE-N035.
- Compared locations and document roles: [DOC-003 PDF p9](../../../joi190092supp2_prod.pdf#page=9) (PLAN); [DOC-003 PDF p22](../../../joi190092supp2_prod.pdf#page=22) (PLAN); [DOC-003 PDF p26](../../../joi190092supp2_prod.pdf#page=26) (PLAN); [DOC-003 PDF p27](../../../joi190092supp2_prod.pdf#page=27) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: p22: held7.5mg/day first6months “untiltheendofPhaseI”; further corticosteroid reduction allowed “inPhaseII, ifpatientscontinueonthesamemedicationasPhaseI.” p26§4.1.1 andp27Table10: same-drug extension PhaseI6–12months; p27§4.1.2: PhaseII alternate-treatment rescue afterfailure.
- Reproducible rule/calculation and tolerance: Identity rule: a continuation onthefirstdrug atmonths6–12 maps toPhaseI6–12, whilePhaseII issecond-drug rescue. The same continuation is labeledPhaseII onp22 andPhaseI onpp26–27. Exact label/time/drug alignment; tolerance0.
- Direct observation versus inference: Direct observation: originalversion uses both phase labels for the same-drug continuation. Inference: steroid-taper phase indexing could be mis-extracted if p22 isreadliterally.
- Alternatives and missing definitions: “PhaseII” might mean a general second6-monthperiod inthatparagraph; elsewhereformalPhaseII isalternate-drug rescue. No efficacy conclusion inferred.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Does the p22 permission for further tapering on the same medication apply to Phase I months 6–12, or to formal Phase II alternate-drug rescue?

### NP-F: Original visit-window column states weeks for day-valued entries

- Relationships: N334 / PE-N035.
- Compared locations and document roles: [DOC-003 PDF p26](../../../joi190092supp2_prod.pdf#page=26) (PLAN); [DOC-003 PDF p27](../../../joi190092supp2_prod.pdf#page=27) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: p26Table9 andp27Table10 columnheader “Window(weeks)”; cells explicitly±15days and−15to+30days.
- Reproducible rule/calculation and tolerance: Dimensional identity: a day-valued interval has unitsdays, notweeks. ±15days=±15/7weeks≈±2.143weeks, not±15weeks;−15/+30days=−2.143/+4.286weeks. Exact unit label; rounding0.001week shown onlyforcalculation.
- Direct observation versus inference: Direct observation: header andcells use incompatible displayed units. Inference: header-only extraction could expand window sevenfold; actual scheduling error notclaimed.
- Alternatives and missing definitions: Explicit cell units may fully disambiguate human use; header could be a carried template label. This limitscandidate to labeling.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Which unit is intended for the original Tables 9–10 Window column, and should its header be interpreted together with each cell's explicit days?

### NP-G: Original Month6 window differs across adjoining phase-I schedule tables

- Relationships: N334 / PE-N035.
- Compared locations and document roles: [DOC-003 PDF p26](../../../joi190092supp2_prod.pdf#page=26) (PLAN); [DOC-003 PDF p27](../../../joi190092supp2_prod.pdf#page=27) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: p26Table9 PhaseI0–6months: Month6M6-I window−15to+30days. p27Table10 PhaseI6–12months: Month6M6-I window±15days.
- Reproducible rule/calculation and tolerance: Samebaseline,codeM6-I,timeMonth6: lower limits−15 agree; upperlimits30vs15 differ15days. Exact day endpoints; tolerance0.
- Direct observation versus inference: Direct observation: overlapping Month6 rows in originalversion provide different windows. Inference: matchingtheMonth6 primary/extensiontransitionvisit assumesoneassessmentservesboth.
- Alternatives and missing definitions: Table10Month6 might mean a separateextensionentryassessment or require a narrowerwindow for extension, while theprimaryendpointallows+30days; distinction isnotnamed.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Are these two M6-I rows the same visit, and is its permitted upper window +15 or +30 days when defining extension entry and the six-month endpoint?

### NP-H: Tumbling-E score formula requires more letters on one line than the line contains

- Relationships: N351 / PE-N052; N449 / NPM084.
- Compared locations and document roles: [DOC-003 PDF p43](../../../joi190092supp2_prod.pdf#page=43) (PLAN); [DOC-003 PDF p44](../../../joi190092supp2_prod.pdf#page=44) (PLAN); [DOC-003 PDF p124](../../../joi190092supp2_prod.pdf#page=124) (PLAN); [DOC-003 PDF p125](../../../joi190092supp2_prod.pdf#page=125) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: Originalp43 andfinalp124 scoring: “If10ormorelettersofthefirstline” correctat4m, score=correct4mletters+30. p44/p125 Snellen rule describes at least4of5letters correctly on a line.
- Reproducible rule/calculation and tolerance: A five-letterline permits atmost5correct; requested10first-linecorrect>5by5. Integerlettercounts allow0 tolerance. Formula total70+30=100 itself is coherent; inconsistencyis first-line qualifying condition.
- Direct observation versus inference: Direct observation: bothversions repeat the first-line10letter clause and4of5rowdescription. Inference: takingfirstline literallymakesqualifierunattainable; sourceforms/table may clarifyintendedtotal.
- Alternatives and missing definitions: “firstline” could be a wording error for totalletters, or encompass two rows informally. Distinguish this clause from separate low-vision threshold candidateNP-I.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Does “10 or more letters of the first line” mean total letters across the chart, and what observable criterion enables the four-meter letter score plus 30?

### NP-I: Tumbling-E low-vision/scoring thresholds do not cover the same letter counts

- Relationships: N347 / PE-N048; N348 / PE-N049; N351 / PE-N052; N447 / NPM082; N449 / NPM084.
- Compared locations and document roles: [DOC-003 PDF p42](../../../joi190092supp2_prod.pdf#page=42) (PLAN); [DOC-003 PDF p43](../../../joi190092supp2_prod.pdf#page=43) (PLAN); [DOC-003 PDF p44](../../../joi190092supp2_prod.pdf#page=44) (PLAN); [DOC-003 PDF p123](../../../joi190092supp2_prod.pdf#page=123) (PLAN); [DOC-003 PDF p124](../../../joi190092supp2_prod.pdf#page=124) (PLAN); [DOC-003 PDF p125](../../../joi190092supp2_prod.pdf#page=125) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: pp42–43 andp123 procedure: <10totallettersat4m→1m; <10totallettersat1m→lowvision. pp43–44,p124–125 scoring:≤3correctlettersofthelargestlineat4m→1mscore;≤3lettersat1m→lowvision.
- Reproducible rule/calculation and tolerance: At1m count4–9 satisfies<10 butnot≤3; e.g.5<10true and5≤3false. At4m total9with5correctlargest-lineletters satisfies<10total butnot≤3largest-line. Integercounts; tolerance0. SameE-chart/version comparisons; letter-chartp112<20isadifferentprocedure andnotaninputhere.
- Direct observation versus inference: Direct observation: procedure/scoring use different thresholds andcountunits(total versusline). Inference: constructed counts exhibitundefined/inconsistentmapping; no patient-specificmeasurementclaimed.
- Alternatives and missing definitions: Low-visiontesting could be performedbelow10 while numericalletter-score remains usableuntil≤3, with separateencodingrules. Package'swithin-scopeprose doesn'tstate this split.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: For E-chart one-meter counts 4–9, and four-meter totals below 10 with more than three largest-line letters correct, should a letter score, low-vision category, or both be recorded, and which threshold controls analysis?

### NP-J: Vitreous-cell grades both include zero cells

- Relationships: N355 / PE-N056; N453 / NPM088.
- Compared locations and document roles: [DOC-003 PDF p45](../../../joi190092supp2_prod.pdf#page=45) (PLAN); [DOC-003 PDF p127](../../../joi190092supp2_prod.pdf#page=127) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: BothTables: grade0=“Nocells”; grade0.5+=“0to5cells”; highergrades1+=6–10,2+=11–20,3+=21–50,4+>50.
- Reproducible rule/calculation and tolerance: 0cells satisfies nocells andinclusive0–5. Integercount0 requiresno rounding; tolerance0. This is asecondarycollectedcellscale, explicitlynotprimary inflammationcontrol.
- Direct observation versus inference: Direct observation: two displayed bins overlap atzero in bothversions. Inference: literal lookupmakesgradeambiguous; no actualgradecount difference demonstrated.
- Alternatives and missing definitions: 0to5 could colloquially mean occasionalobservedcells versus trulyabsentcells, requiring aqualifiernotprinted. TheprimaryAC/hazeendpointisnotclaimedaffected.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Should zero vitreous cells receive grade 0 or 0.5+, and does the 0.5+ interval have an unstated positive lower boundary or sampling distinction?

### NP-K: Original white-cell event example changes numeric scale without a unit marker

- Relationships: N364 / PE-N065; N318 / PE-N019.
- Compared locations and document roles: [DOC-003 PDF p16](../../../joi190092supp2_prod.pdf#page=16) (PLAN); [DOC-003 PDF p53](../../../joi190092supp2_prod.pdf#page=53) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: p16Table3 leukocyte thresholds >1000and<2500/μL or≤999/μL. p53§6.1 example WBC reduction “tobelow2.5”, no WBC unit stated in this example.
- Reproducible rule/calculation and tolerance: 2500/2.5=1000. Values reconcile onlyif2.5 is expressed inthousandcells/μL(10³/μL) or10⁹/L ratherthan cells/μL; printedTable3 unit cannotbe carried unchanged. Exact factor1000; tolerance0 forscaleidentity.
- Direct observation versus inference: Direct observation: the samenon-seriousWBCconcept is printedas2500/μL versus2.5withoutunit. Inference: missingunitmaydenoteaconventionalrescaling, ratherthan thresholdconflict.
- Alternatives and missing definitions: Laboratories commonly use scaled WBCunits; an omittedunit here couldexplainbothvalues. This is aconditional scale-labelcandidate, not aclaimthat2.5literallymeans2.5cells/μL.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: What unit and scale are intended for “below 2.5” in original §6.1, and is this the same non-serious event boundary as Table 3 below 2500/μL?

### NP-L: Mycophenolate maintenance bottle described as30-day supply contains16⅔days at full dose

- Relationships: N402 / NPM037; N403 / NPM038; N401 / NPM036.
- Compared locations and document roles: [DOC-003 PDF p86](../../../joi190092supp2_prod.pdf#page=86) (PLAN); [DOC-003 PDF p87](../../../joi190092supp2_prod.pdf#page=87) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: p86 MMF maintenance1.5gBID=3pillsAM+3pillsPM (500mgpill),6pills/day. p87 maintenancebottles “30days’worth…plusadditionalpillsasabuffer”; MMF bottles100pills each. Monthlydispense200pills; baseline14-day introductory+100pillmaintenance.
- Reproducible rule/calculation and tolerance: Full-dose30daysrequires30×6=180pills beforebuffer;100/6=16.667days, short80pills/13.333days. Monthly200/6=33.333days coherentbuffer. Baseline14+100/6=30.667dayscoherentfirst-monthsupply. Exact pillarithmetic tolerance0pills; durationsreportedto0.001day.
- Direct observation versus inference: Direct observation: bottle-level30-day claim and100pillcount conflict at printed full-dose regimen. Inference: computed duration is bottle-level, not assertionofpatientundersupply.
- Alternatives and missing definitions: General30-daysupplymightmean a dispensingpackageoftwobottles ratherthansinglebottle; baselineonlyneedsremaining≈16days. Reviseddefinitioncouldfullyexplain operationalintent.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Does “maintenance dose bottles will contain 30 days’ worth” refer to individual MMF 100-pill bottles or to the monthly 200-pill dispensing package?

### NP-M: Final letter-chart refraction Chart R has two numeric version identifiers

- Relationships: N420 / NPM055; N429 / NPM064.
- Compared locations and document roles: [DOC-003 PDF p103](../../../joi190092supp2_prod.pdf#page=103) (PLAN); [DOC-003 PDF p110](../../../joi190092supp2_prod.pdf#page=110) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: p103: ChartR “PrecisionVisionChartVersion2110” forrefraction. p110: Charts1,2,R correspond “2110,2111and2112,respectively”; ChartR usedforallmanifestsubjectiverefraction.
- Reproducible rule/calculation and tolerance: Respectivelymapping yieldsChartR2112, which differs fromChartR2110onp103 by2intheidentifier. Identifier identity, notnumericmagnitudecomparison; tolerance0.
- Direct observation versus inference: Direct observation: samefinalMOP namesChartRforidenticalrefractionusewithtwoidentifiers. Inference: twochartversions cannotbeunambiguouslyselectedfromtheselabels.
- Alternatives and missing definitions: Couldbealternativecatalogversions ormappingordererror; chartIDs notclinicalresults and no actualdeviceuseclaimed. Tumbling-E2305b isaseparatechartfamily.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Which Precision Vision numeric version is intended for the final letter-chart Chart R refraction procedure: 2110 or 2112, or are both interchangeable variants?

### NP-N: Intermediate E-chart sphere retest uses a lens different from its next conditional

- Relationships: N441 / NPM076; N438 / NPM073.
- Compared locations and document roles: [DOC-003 PDF p115](../../../joi190092supp2_prod.pdf#page=115) (PLAN); [DOC-003 PDF p117](../../../joi190092supp2_prod.pdf#page=117) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: p115 mediumacuity guide specifies sphere±1.00D trial/increment. p117 intermediate6/30–6/60 branch: if−1.00doesnotimproveletters, “retestusingthe+0.50lens”; nextlines branchon “Ifthe+1.00lens…” better/sameorworse.
- Reproducible rule/calculation and tolerance: Same sequential retest should supplythelens evaluatedby immediatelyfollowingconditional: +0.50versus+1.00 differ0.50D, factor2. Exact prescribedlenspower; tolerance0D.
- Direct observation versus inference: Direct observation: onebranch changes numeric lens label without anintervening1.00Dpresentation. Inference: interpretingconditionalasthere-testresponse createsunmatchedprobe/result.
- Alternatives and missing definitions: NOTEallowschangingtriallensesifacuityimprovessignificantly, buttriggerhereisfailureof−1.00toimproveletters; +0.50mightbeadeliberateadditionalprobe whose conditional wasnotwritten.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: After the intermediate E-chart −1.00 D probe fails to improve the letters read, should the retest use +0.50 D or +1.00 D, and which probe's response governs the next branch?

### NP-O: Final cataract category list omits the expressly defined grade3

- Relationships: N451 / NPM086; N452 / NPM087.
- Compared locations and document roles: [DOC-003 PDF p125](../../../joi190092supp2_prod.pdf#page=125) (PLAN); [DOC-003 PDF p126](../../../joi190092supp2_prod.pdf#page=126) (PLAN). All comparisons are within PLAN content; relationship P_P.
- Printed inputs: p125 opacitystandards1=clinicalpresence,2=clinicalsignificance,3=severeoccurrence; halfgradesallowed(example1.5). p126 allopacitytypes severitycategories “<1,1,1.5,2,2.5,>3”.
- Reproducible rule/calculation and tolerance: Value3 is expresslydefined but belongs to none ofthelistedcategories:3not<1,not1/1.5/2/2.5,and3not>3. Exact ordinalgrade, tolerance0.
- Direct observation versus inference: Direct observation: prose standard3 andcategorylist>3 arebothprinted. Inference: mapping astandard3measurementtoalistcategory isundefined; no actualcataractdistributionclaimed.
- Alternatives and missing definitions: Finalcategorycouldintentionallymean≥3, orformsallow3separately despiteproselist. Missing comparator definition requireshumanreview.
- Quality-control relevance: A bounded plan-material numeric or labeling question may affect faithful reuse of this definition. No actual outcome alteration is established.
- Exact human question: Which category receives an opacity matching the grade 3 standard, and is the final category intended as >3 or ≥3?

## Completion

155 quantitative relationship groups checked;15 distinct document-grounded local candidates emitted. All repeated manifestations of the same mismatch are grouped on one card. Other checks reconcile or lack an independently supplied contradiction, with reasons in the two complete inventories. Original/finalprotocolchanges were respected as disclosedcontexts, ratherthancomparedasidenticalrules. Nocandidateisregistered solelyforanunreportedmodeldetail orforvery-smallPdisplayzero. NoassignedstableCIDs, severity, validity, dispositions orfinalcorrections.

