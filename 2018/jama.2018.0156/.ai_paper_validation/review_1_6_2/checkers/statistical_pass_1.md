# Statistical pass 1

Fresh runtime agent: `01a129b8-92ad-7b63-b00a-a605a8e9f04a`; run model `gpt-6.1-sol`; reasoning effort `high`. Scope: all 146 mapped source pages, DOC-001 pp1–9 REPORT; DOC-002 pp1–134 PLAN; DOC-003 pp1–3 REPORT. QUALITY_CONTROL_SCOPE.md and the 1.6.2 review contract were read completely. Current canonical main/support evidence maps, source/evidence inventories and tooling record were read. Sources were confirmed by direct PDF text and targeted page images. No old review conclusions, concurrent checker conclusions, external literature or web material was used.

Pass 1 covers 81 stable inferential/method/design relationships. Every ID is explicitly PASS_1_COMPLETE in the relationship inventory and the following coverage table. Candidate registration and independent inclusion screening belong to subsequent stages. All observations below were self-screened; there is no expected count. Nine findings and 19 excluded apparent observations are recorded.

Source abbreviations: main = jama_jabre_2018_oi_180004.pdf (REPORT), plan = joi180004supp1_prod.pdf (PLAN, throughout), results supplement = joi180004supp2_prod.pdf (REPORT). All links use physical PDF pages. Values of differences/CI limits are percentage points unless noted.

## Complete relationship coverage

| S ID | Relationship | Pass 1 outcome | Status |
|---|---|---|---|
| S001 | Primary endpoint | Original definition and report align; amendment exception separately S002. | PASS_1_COMPLETE |
| S002 | Amended primary definition | F-ST1-006; endpoint success mapping cannot be resolved from aggregate CPC cells. | PASS_1_COMPLETE |
| S003 | Primary ITT estimate/CI/P | Estimate contained; ordered endpoints; NI lower bound<−1 and P>.025 agree. Diagnostic normal approximation yields P≈.107; exact algorithm absent. | PASS_1_COMPLETE |
| S004 | Primary PP estimate/CI/P | Estimate contained; NI not established. Diagnostic interval-derived normal P≈.122; no unidentified covariance/test inferred. | PASS_1_COMPLETE |
| S005 | Hierarchical primary result | Estimate contained; lower bound below−1; no P/test supplied; model not compared with crude difference. | PASS_1_COMPLETE |
| S006 | NI inequality narrative | F-ST1-001; printed numeric-order statement reverses relationship. | PASS_1_COMPLETE |
| S007 | Matched primary conclusions | Non-demonstration follows lower bound; no claim of statistical equivalence; S006 isolates numeric-order sentence. | PASS_1_COMPLETE |
| S008 | Sample-size success assumptions | Rates/contrast/alpha match across plan/report; historical rounded sources are planning inputs, not a model-versus-crude check. | PASS_1_COMPLETE |
| S009 | Sample-size reproduction | Diagnostic normal n=(.03×.97+.02×.98)(1.959964+.841621)^2/.02^2=955.60, rounding 956; exact simulation seed/implementation absent, no reproduced contradiction. | PASS_1_COMPLETE |
| S010 | Margin preservation logic | (2−1−0)/(2−0)=.5; coherent stated arithmetic; no clinical margin critique. | PASS_1_COMPLETE |
| S011 | Primary confidence reporting | Both allocate.025 to lower tail; bound used for stated NI decision aligns; no additional upper-tail claim or quantity conflict. | PASS_1_COMPLETE |
| S012 | Sequential NI/superiority gate | NI was not demonstrated; report does not claim a primary superiority test. Secondary superiority is separately specified. | PASS_1_COMPLETE |
| S013 | Protocol/native SAP hypothesis signs | Operational boundary clear; shared equality symbol is excluded notation observation; scanned sign differs in S014. | PASS_1_COMPLETE |
| S014 | Signed SAP hypothesis number | F-ST1-005; retain native and scan copy identity. | PASS_1_COMPLETE |
| S015 | Sidedness/alpha specifications | Primary NI one-tail decision compatible with CI; all-tests wording does not establish an additional printed conflict. | PASS_1_COMPLETE |
| S016 | ITT analysis set | Specific SAP eligibility clause explains2043 vs 2040 and no lost follow-up; analysis by allocation. | PASS_1_COMPLETE |
| S017 | PP analysis set | Definition matches plan; PP reason totals need not equal distinct exclusions; numeric flow relationship retained. | PASS_1_COMPLETE |
| S018 | Prespecified primary AT | F-ST1-008; planned primary AT not identifiable as reported; post hoc denominators 863/1174 differ from safety AT1028/999. | PASS_1_COMPLETE |
| S019 | Safety analysis set | Definition internally coherent; varying endpoint denominator1027/996 is outcome-specific; planned ITT additional set separately S053. | PASS_1_COMPLETE |
| S020 | Binary secondary test method | Independent randomized groups support stated tests; row algorithm not specified. No unreported df, continuity correction inferred. | PASS_1_COMPLETE |
| S021 | Continuous secondary method | Stated coherent choice; per-outcome distribution, test and variance not supplied; numeric checks only where source establishes inputs. | PASS_1_COMPLETE |
| S022 | Safety test method | Rate-null and significance agree for three comparative safety rows; no preferred test proposed. | PASS_1_COMPLETE |
| S023 | Secondary multiplicity | Reported exploratory qualification matches stated unadjusted rule; no adjusted stopping/superiority claim. | PASS_1_COMPLETE |
| S024 | Protocol interim rule | Numerical futility boundary and recalculation algorithm not supplied; no reported conflicting interim decision; S025 disclosed cancellation. | PASS_1_COMPLETE |
| S025 | SAP interim cancellation | Explicit cancellation explains planned versus final stage difference; not a claim that planned futility boundary was satisfied. | PASS_1_COMPLETE |
| S026 | Stopping/DSMB logic | No reported efficacy/futility/safety stopping conclusion to test; lack of threshold alone yields no finding. | PASS_1_COMPLETE |
| S027 | Primary missingness | No missing primary value or conflicting assignment supplied; 3 eligibility exclusions distinct from missingness. | PASS_1_COMPLETE |
| S028 | Conditional imputation sensitivity | Large threshold/MI specification absent; no primary missing data apparent; cannot infer trigger activation from convention. | PASS_1_COMPLETE |
| S029 | Secondary missing-value handling | Endpoint-specific denominators supplied in tables; no printed imputation conflict. | PASS_1_COMPLETE |
| S030 | Center adjustment/design | Plan does not state adjusted primary model; report labels added center model post hoc; no expectation imposed that unadjusted primary must include strata. | PASS_1_COMPLETE |
| S031 | Planned exploratory prognostic regression | Not described as prespecified primary/key secondary analysis; absence of exploratory regression is peripheral; model not substituted for primary estimate. | PASS_1_COMPLETE |
| S032 | Software specifications | Software version difference alone does not change stated result/model/decision; peripheral observation. | PASS_1_COMPLETE |
| S033 | ITT day 28 overall survival | Contained/ordered; null included, P>.05; Wald d.118993, CI[−1.83285, 2.07084]; matched copies agree. | PASS_1_COMPLETE |
| S034 | ITT CPC distribution | Components add to denominators; CPC 1+2=44/43; CPC 1–4=55/54; omnibus P not mistaken for primary NI P. | PASS_1_COMPLETE |
| S035 | ITT admission survival | Contained/ordered; null included, P>.05; Wald d−3.70301, CI[−7.70393, .29791]; narrative direction agrees. | PASS_1_COMPLETE |
| S036 | ITT ROSC | Contained/ordered; null excluded, P<.05; ETI higher; Wald d−4.66073, CI[−8.83436, −.48709]. | PASS_1_COMPLETE |
| S037 | PP day 28 overall survival | F-ST1-002 for interval; point difference apparent mismatch is display precision allowance; null and P significance agree. | PASS_1_COMPLETE |
| S038 | PP CPC distribution | Totals 995/943; primary 43/40; overall 54/51; 3.5% ETI CPC1 discrepancy screened by display rule; distribution P is not primary test. | PASS_1_COMPLETE |
| S039 | PP admission survival | F-ST1-002 includes upper endpoint; Wald CI[−8.16079, .07945]; lower endpoint alone≤5%gap after rounding; null/P threshold agree. | PASS_1_COMPLETE |
| S040 | PP ROSC | F-ST1-003 for ETI percentage; count-based Wald d−5.60693, CI[−9.90623, −1.30763] reproduces printed contrast and CI. | PASS_1_COMPLETE |
| S041 | Airway difficulty | Contained/ordered; null excluded, P<.05; higher BMV; nonnormal/adjusted detail not inferred; independent-proportion calculation compatible within precision. | PASS_1_COMPLETE |
| S042 | Airway procedural failure | Contained/ordered; null excluded, P<.05; higher BMV; count difference 4.60363; se.90351; plan composite separately S055. | PASS_1_COMPLETE |
| S043 | Gastric regurgitation | Contained/ordered; null excluded, P<.05; higher BMV; independent-proportion CI[4.9458, 10.4189]compatible. | PASS_1_COMPLETE |
| S044 | ETI-only complications | Counts/percentages align within rule; no comparison or null-test claim made; NA not missing inferential result. | PASS_1_COMPLETE |
| S045 | Difficulty scales summaries | Median inside IQR; different instruments are explicit; no invalid direct between-scale comparison claimed. | PASS_1_COMPLETE |
| S046 | Center 5 CCF | Contained/ordered; null/P nonsignificance agree; mean/median, test, SD/SE not provided; normal P from interval only diagnostic, not reproduction. | PASS_1_COMPLETE |
| S047 | Center 5 pauses | Difference27−16=11, ordered/contained, null excluded/P significant; seconds unit apparent issue excluded as notation; count outcome clear. | PASS_1_COMPLETE |
| S048 | ECMO/donation exclusion method | Population reduction 91 reproduces; BMV 35 ECMO+12 donation=47 and ETI 23+21=44 consistent with printed reductions; no assumed mutual exclusivity needed. | PASS_1_COMPLETE |
| S049 | ECMO/donation exclusion result | F-ST1-004 for same-display reproducing-method CI; estimate contained; null/P nonsignificance agree. | PASS_1_COMPLETE |
| S050 | Pre-ROSC crossover method | BMV 1018−863=155; ETI 1174−1022=152; total 2040→2037. Apparent three-patient difference is screened by the display-precision rule; no F ID. | PASS_1_COMPLETE |
| S051 | Pre-ROSC crossover result | Estimate contained; endpoints ordered; null included and P>.05; Wald d=.91782%, CI[−.87673, 2.71237] reproduces. Event totals 86 vs 87 overlap under display precision. | PASS_1_COMPLETE |
| S052 | Planned secondary AT analyses | F-ST1-008 consolidated planned-populations pattern; key secondary admission/day 28 reported in abstract. | PASS_1_COMPLETE |
| S053 | Planned safety ITT analyses | F-ST1-008 consolidated population pattern; difficulty/failure/regurgitation abstract results; no ITT table supplied. | PASS_1_COMPLETE |
| S054 | Endpoint status mapping | F-ST1-007; status categories may simultaneously apply but Route A category 5 retains comparison for human question. | PASS_1_COMPLETE |
| S055 | Technique-failure composite | F-ST1-009; reported key secondary failure maps only the procedural component; the planned composite includes death and regurgitation. | PASS_1_COMPLETE |
| S056 | Planned mRS/discharge outcomes | Peripheralnon-key secondary omission; neither abstract result nor plan-keydesignation; excluded observation. | PASS_1_COMPLETE |
| S057 | Planned interruption/TI-duration outcomes | No exact duration-to-count result matching; non-key planned measurements omitted; peripheral comparison rather than asserted prespecified primary replacement. | PASS_1_COMPLETE |
| S058 | Safety definition amendments | Disclosed amendments mapped; unreportednon-key complication inventory alone peripheral; regurgitation counts not misidentified as aspiration. | PASS_1_COMPLETE |
| S059 | Randomized intervention/rescue | Final amendment and report match; post-ROSC intubation is expected strategy; nofixed-dose/duration conflict. | PASS_1_COMPLETE |
| S060 | Day28 ascertainment | 28–35window matches plan; distinguishes ascertainment date from endpoint time. | PASS_1_COMPLETE |
| S061 | Analysis unit/randomization | Unit of analysis individual patient; proportions and between-group tests compatible; no paired-design or cluster-randomization claim. | PASS_1_COMPLETE |
| S062 | Baseline comparisons | Descriptive comment is not a conflicting formal test; baseline copy checks belong to numeric lane. | PASS_1_COMPLETE |
| S063 | Disposition/flow and inference | Analysis denominators are identified; analysis-set differences are distinct from missingness. S050 records a small post hoc count difference screened under display precision. | PASS_1_COMPLETE |
| S064 | Inferential count/denominator mapping | All individual count/rate checks performed; S040ETI30.0fails; other apparent low-precision deviations screened. | PASS_1_COMPLETE |
| S065 | Categorical summary precision | Main and supplement within-display rates inspected; no display precision assumed to remove Route A category1 interval/P conflict. | PASS_1_COMPLETE |
| S066 | Continuous summary precision | Presentation differences without primary/key inferential conflict is not a method finding; median/IQR endpoint order checked. | PASS_1_COMPLETE |
| S067 | IDS scoring and impossibility | Reportthreshold>5matches; finite-versus∞instruction not linked to quantitative contradiction; wording observation excluded. | PASS_1_COMPLETE |
| S068 | Han grading/threshold | Threshold maps grades3–4; procedural failure grade 4 distinguished; no conflicting reported cutoff. | PASS_1_COMPLETE |
| S069 | CPC coding and success components | CPC aggregates reproduce published primary/overallcounts; S002amended baseline exception remains distinct. | PASS_1_COMPLETE |
| S070 | VAS units/direction | Direction and range align; line-length unit unreported in plan but obvious report scale; no substantive unit conflict. | PASS_1_COMPLETE |
| S071 | Plan assessment timing statements | Explicit prehospital schedule and scale roles resolve plan wording; not different numerical outcome/timepoint. | PASS_1_COMPLETE |
| S072 | Primary assessor masking | Open intervention and blinded outcome assessment can both hold; no reported method conflict. | PASS_1_COMPLETE |
| S073 | Eligibility and postrandomization sets | Specific SAP ITT criterion resolves eligibility restrictions; counts and reason overlap retained without conflating ITT/PP. | PASS_1_COMPLETE |
| S074 | Historical planning/context contrasts | Not a crude reproduction of the historical adjusted OR; source-specific planning rates are explicit; cross-copy historical differences are peripheral. | PASS_1_COMPLETE |
| S075 | Center 5 monitor/unit window | Center 5 is explicit subgroup, not overall trial; within-minute CCF unit defined; no dispersion provided for quantitative exact P check. | PASS_1_COMPLETE |
| S076 | Secondary narrative direction | All reported secondary directions match count-based contrasts and CI/P significance except printed PP ETI percentage S040. | PASS_1_COMPLETE |
| S077 | OR versus difference representations | No OR number misidentified as RD; missing parallel OR presentation without distinct main/key analysis change excluded. | PASS_1_COMPLETE |
| S078 | Recruitment total/planned sample | Rounded recruitment target and observed recruitment above that target do not contradict power. No mandated stop at 2000 is stated. | PASS_1_COMPLETE |
| S079 | ITT primary-success aggregation | Exactcomponent-to-primary numerator agreement; null test for CPC distribution distinct from NI test. | PASS_1_COMPLETE |
| S080 | PP primary-success aggregation | Printed4.3/4.2, d.08agree within precision; NI result maps PP denominators; separateoverall-survival rowS037. | PASS_1_COMPLETE |
| S081 | Attempted ETI event attribution | Stated safety classification coherent with figure 2027; no forced crude actual-last-device classification; unreported per-event details not inferred. | PASS_1_COMPLETE |

## Findings

### F-ST1-001

**Title:** Primary-result numeric-order statement reverses the printed CI bound and NI threshold.

**Relationships:** S003, S006, S007, S011, S012. **Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Exact locations and document roles:** REPORT [main p3, Statistical Analysis, primary decision rule](../../../jama_jabre_2018_oi_180004.pdf#page=3) versus REPORT [main p4, Primary Outcome, ITT result and immediately following sentence](../../../jama_jabre_2018_oi_180004.pdf#page=4).

**Printed values:** Accept NI if the lower CI limit is higher than −1%. The result is difference 0.11%, one-sided 97.5% CI −1.64% to infinity, NI P=.11. The next sentence states that the lower limit was greater than the threshold, thus NI was not demonstrated.

**Rule and calculation:** −1.64% < −1%, so the printed ordering statement reverses the numeric comparison; if the lower bound really were greater, the stated rule would accept NI. Allowing displayed lower bound [−1.645,−1.635] and even a broad half-unit margin interval [−1.5,−.5] leaves the lower bound below the threshold: minimum gap .135, relative to the printed bound .135/1.64=.0823 >.05. The conclusion of no demonstrated NI agrees with the printed interval and P value, but the intervening numeric-order statement does not.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** The interpretation of the primary noninferiority decision and its direction relative to the −1 percentage-point margin.

**Why context does not resolve it:** Route A category 2 retains a direction statement that reverses the printed values; the consistent conclusion elsewhere is an alternative, not removal of this numeric-order observation.

**Alternatives and missing definitions:** The result/conclusion may be intended as printed, with the comparison statement referring to the opposite ordering; alternatively the sentence could refer to another bound or threshold. No other bound or threshold is identified in that sentence. No revised value is proposed.

**Exact human question:** Which confidence bound and noninferiority threshold does the sentence saying “greater than the threshold” refer to, and how should its ordering be read alongside the reported −1.64% lower bound and −1% rule?

### F-ST1-002

**Title:** Two Table 2 per-protocol intervals do not reproduce under a method that reproduces the other comparable rows.

**Relationships:** S033, S035, S036, S037, S039, S040, S064. **Focus areas:** B, C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Exact locations and document roles:** REPORT [main p6, Table 2, PP Survival at 28d and Survival to hospital admission](../../../jama_jabre_2018_oi_180004.pdf#page=6), with the three ITT binary rows and PP ROSC row in the same display as method-reproduction comparators. REPORT [main p3, secondary rate methods](../../../jama_jabre_2018_oi_180004.pdf#page=3).

**Printed values:** PP denominators 995/943. Survival28d:54(5.4%) versus51(5.4%), difference 0.1%, 95% CI −10 to9.7, P=.99. Admission:289(29.1%) versus312(33.1%), difference−4.0%, 95% CI −7.6 to0.6, P=.055. The display labels BMV(%)−ETI(%).

**Rule and calculation:** A same-display reproducing calculation is the independent-proportions 95% Wald interval: d=100(a/n−b/m), SE=100√[p(1−p)/n+q(1−q)/m], CI=d±1.95996398454SE. This is a reproducing method, not an assertion that the unnamed source CI algorithm was Wald. It gives ITT survival[−1.83285,2.07084], admission[−7.70393,.29791], ROSC[−8.83436,−.48709] and PP ROSC[−9.90623,−1.30763], each compatible with its printed Table 2 interval under the display rule. It gives PP survival d=.0188642, SE=1.0287562, CI[−1.99746,2.03519], and PP admission d=−4.0406699, SE=2.1021388, CI[−8.16079,.07945].

**Display-precision calculation:** Each count/denominator is allowed ±.5 and each decimal endpoint its half-unit; the whole-number −10 endpoint is allowed ±.5. Conservative interval arithmetic gives PP survival lower endpoint[−2.11639,−1.87850], upper[1.91622,2.15412]. Printed endpoint intervals[−10.5,−9.5] and[9.65,9.75] have gaps≥7.38361 and≥7.49588, relative discrepancies≥.73836 and≥.77277. PP admission recomputed upper endpoint[−.05950,.21837] versus printed[.55,.65] has gap≥.33163, relative discrepancy≥.55272. The admission lower endpoint alone is screened by the ≤.05 relative rule and is not the qualifying observation. The survival point difference 0.1 alone is also not the qualifying observation.

**Qualifying route:** Route A, category 4.

**Affected result or extracted value:** The PP day 28 overall-survival interval and the PP admission-survival upper confidence limit extracted from Table 2.

**Why context does not resolve it:** Route A category 4 retains rows not reproduced by a method that does reproduce the remaining comparable display rows. No distinct model/CI method is labeled for either affected row.

**Alternatives and missing definitions:** A distinct CI estimator or input population could have been used for these two rows; neither is specified. It is also possible that the limits have a different intended reading. The P values and null inclusion agree qualitatively; no interval-versus-significance finding is inferred here.

**Exact human question:** What CI method, inputs and population produced the PP survival interval −10 to9.7 and the PP admission upper limit0.6, given that the independent-proportions95% calculation reproduces the other binary rows of Table 2?

### F-ST1-003

**Title:** The per-protocol ETI ROSC percentage does not reconcile with its displayed count, denominator or difference.

**Relationships:** S040, S064, S076. **Focus areas:** A, B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Exact locations and document roles:** REPORT [main p6, Table 2, PP heading and Return of spontaneous circulation row](../../../jama_jabre_2018_oi_180004.pdf#page=6).

**Printed values:** PP ETI n=943; ROSC377(30.0%). BMV 342/995(34.4%). Difference−5.6%, 95% CI[−9.9,−1.3], P=.01.

**Rule and calculation:** 100×377/943=39.97879%, not30.0%. The count-based difference 100(342/995−377/943)=−5.60693% agrees with the printed−5.6%, whereas the printed percentages34.4−30.0=+4.4% reverse its sign.

**Display-precision calculation:** Count377±.5 and denominator943±.5 give percentage[39.90461,40.05305]; printed 30.0 gives[29.95,30.05]. Gap9.85461/30.0=.328487 >.05.

**Qualifying route:** Route A, category 3; the reading also meets category 2 because the printed percentage changes the apparent direction/magnitude.

**Affected result or extracted value:** ETI per-protocol ROSC risk and its direction relative to BMV.

**Why context does not resolve it:** Route A category 3 retains a count/denominator/percentage discrepancy within one display; reconstruction from the count does not remove the printed extraction value.

**Alternatives and missing definitions:** The count/denominator and difference may be the intended result, or30.0 may refer to another population; no alternate denominator/population is labeled. No correction is assigned.

**Exact human question:** Which ETI per-protocol ROSC percentage and denominator should be used for extraction, and how does the displayed377(30.0%) relate to n=943 and the difference−5.6%?

### F-ST1-004

**Title:** The eTable2 exclusion-analysis interval does not reproduce under the method that reproduces its companion row.

**Relationships:** S048, S049, S051. **Focus areas:** B, C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Exact locations and document roles:** REPORT [results supplement p3, eTable2, ECMO/donation exclusion row and pre-ROSC reclassification row](../../../joi180004supp2_prod.pdf#page=3). The main [p3 post hoc method](../../../jama_jabre_2018_oi_180004.pdf#page=3) is REPORT corroboration and does not add a cross-document conflict.

**Printed values:** Exclusion row43/971(4.4%) versus39/978(4.0%), difference 0.4%, 95% CI[−2.2,1.3], P=.63. Companion row41/863 versus45/1174, difference 0.9%, CI[−.9,2.7], P=.31.

**Rule and calculation:** The independent-proportions95% Wald method in F-ST1-002 gives companion difference.9178197 and CI[−.8767332,2.7123725], reproducing the displayed companion row. For the exclusion row it gives d=.4406942, SE=.9095908 and CI[−1.3420710,2.2234595]; the displayed interval has a different center/direction of asymmetry.

**Display-precision calculation:** Allowing each integer input ±.5 gives conservative recomputed lower endpoint[−1.46027,−1.22381] and upper[2.10520,2.34166]. Printed endpoint ranges[−2.25,−2.15] and[1.25,1.35] yield gaps≥.68973 and≥.75520; relative discrepancies≥.31351 and≥.58092, both >.05.

**Qualifying route:** Route A, category 4.

**Affected result or extracted value:** The95% risk-difference interval for favorable day 28 survival after excluding ECMO-CPR and donation cases.

**Why context does not resolve it:** Route A category 4 applies because the same calculation reproduces the other row of this display. No separate CI method or model is printed for the exclusion row. The estimate is contained and the interval/P value agree about zero, which does not resolve the limit values.

**Alternatives and missing definitions:** A different CI estimator or input set may have been used, or the displayed limits may have another intended reading. The source supplies neither a distinct estimator nor a model adjustment.

**Exact human question:** Which CI method and inputs produced[−2.2,1.3] for43/971 versus39/978, and why does that row differ from the calculation reproducing the companion eTable2 interval?

### F-ST1-005

**Title:** Signed and native SAP copies specify different signed noninferiority alternative boundaries.

**Relationships:** S013, S014, S015. **Focus area:** D. **Proposed review domain:** plan_material. **Proposed relationship type:** P_P. **All relationships:** P_P.

**Exact locations and document roles:** PLAN [plan p130, signed SAP section4.1](../../../joi180004supp1_prod.pdf#page=130) versus PLAN [plan p121, native SAP section4.1](../../../joi180004supp1_prod.pdf#page=121); PLAN [p133, signed SAP section8.2.1](../../../joi180004supp1_prod.pdf#page=133) supplies the operational lower-limit rule.

**Printed values:** Signed p130 H1:πBVM−πTI≥0.01, no minus glyph; native p121 H1:πBVM−πTI≥−0.01. Both H0 statements have≤−0.01. The signed rule accepts NI if lower 95% CI>−0.01. Both copies identify version1/footer18February2015.

**Rule and calculation:** Positive.01 is a+1 percentage-point boundary; negative.01 is a−1 percentage-point boundary. The+1 alternative and−1 CI rule partition the contrast differently and leave a two-percentage-point interval between the null boundary and the scanned alternative. Half-unit ranges[.005,.015] and[−.015,−.005] have gap.01, relative discrepancy1.0 >.05.

**Qualifying route:** Route B.

**Affected result or extracted value:** The signed planned NI hypothesis and margin used to interpret the primary survival difference.

**Why context does not resolve it:** The signed copy and its own operational rule disagree, while the otherwise matching native copy gives the opposite sign. This is a printed signed-number change in a primary decision specification, not a question about a conventional equality glyph. Which copy/rule governs is not specified.

**Alternatives and missing definitions:** The operational rule/native copy may represent the intended signed boundary; the scan may encode a different hypothesis. A scan-associated omitted mark is also possible. Direct image inspection confirms the supplied visible reading, but no assumption about production is made.

**Exact human question:** Which signed alternative boundary governs the primary NI analysis: the signed SAP’s≥+0.01, the native SAP’s≥−0.01, or the signed SAP’s lower-CI>−0.01 decision rule?

### F-ST1-006

**Title:** The amended primary success definition is not carried into the reported CPC 1–2 definition.

**Relationships:** S001, S002, S069, S079, S080. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R, P_P.

**Exact locations and document roles:** PLAN [plan p71, final protocol section4.1.1](../../../joi180004supp1_prod.pdf#page=71) and PLAN [p110, MS1 primary-endpoint amendment](../../../joi180004supp1_prod.pdf#page=110), versus REPORT [main p1 Abstract](../../../jama_jabre_2018_oi_180004.pdf#page=1), REPORT [p3 Outcomes](../../../jama_jabre_2018_oi_180004.pdf#page=3), REPORT [p6 Table 2 footnote b](../../../jama_jabre_2018_oi_180004.pdf#page=6). PLAN [p122 native SAP section6.1](../../../joi180004supp1_prod.pdf#page=122) and PLAN [p131 signed SAP section6.1](../../../joi180004supp1_prod.pdf#page=131) also retain CPC≤2 only.

**Printed values/statements:** Final protocol/amendment: in pre-randomization neurological disability, survival with the same degree of disability counts as favorable neurological function. Report/SAP: survival at day 28 with CPC≤2; Table 2 explicitly codes CPC 1 and 2 as success. Primary counts44/1018 and 43/1022 equal the sums of CPC 1+2.

**Rule and calculation:** A baseline-relative preserved disability endpoint can classify survival with persistent CPC 3 or4 differently from an absolute CPC≤2 endpoint. The amended definition and the reported coding rule therefore are not identical; no numeric recalculation is justified without pre-randomization disability data. This is a source-defined endpoint comparison, not a diagnostic statistical approximation.

**Qualifying route:** Route B.

**Affected result or extracted value:** The primary favorable day 28 survival outcome definition underlying44 and 43 successes and the reported NI interval.

**Why context does not resolve it:** The amendment explicitly adds the exception, while the report’s numerical success coding explicitly uses CPC 1+2. Aggregate CPC counts do not show whether any participant qualified through the exception or whether the exception was implemented.

**Alternatives and missing definitions:** No relevant participant may have had baseline neurological disability; the exception may have been implemented without changing the counted successes; or the reported analysis may have used CPC≤2 alone. Missing definition: how baseline disability was incorporated into the final primary success indicator, and which protocol/SAP version governed it.

**Exact human question:** Was the amended baseline-disability exception applied to the primary endpoint, and how does its coding relate to the reported CPC 1+2 success counts44 and 43?

### F-ST1-007

**Title:** The supplied SAP and protocol/report give different outcome-status assignments for the same airway endpoints.

**Relationships:** S041, S042, S043, S054, S058. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R, P_P.

**Exact locations and document roles:** PLAN [plan p122, SAP sections6.1 and 6.2](../../../joi180004supp1_prod.pdf#page=122) and PLAN [p131 signed duplicate](../../../joi180004supp1_prod.pdf#page=131), versus PLAN [p71 final protocol secondary-endpoint list](../../../joi180004supp1_prod.pdf#page=71) and REPORT [main p3 Outcomes](../../../jama_jabre_2018_oi_180004.pdf#page=3), REPORT [p1 Abstract secondary endpoints/results](../../../jama_jabre_2018_oi_180004.pdf#page=1), REPORT [p6 Table 3](../../../jama_jabre_2018_oi_180004.pdf#page=6).

**Printed statements:** SAP efficacy secondary criteria are admission survival,day 28 survival,ROSC and IDS. Its section6.2 Safety Endpoints places BMV VAS,Han classification,BMV/ETI failure and gastric regurgitation in safety. Final protocol labels these secondary endpoints. The report’s secondary-endpoint paragraph lists BMVdifficulty,Han classification and BMV/ETI failure, with complications collected; their results are reported in the abstract and Table 3 Safety Population.

**Rule and calculation:** Compare explicit outcome-status headings for the same instruments/events; no arithmetic is needed. The classification map for BMVdifficulty/proceduralfailure/regurgitation spans secondary and safety in the supplied materials.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecified outcome status of airway difficulty, failure and regurgitation results used in abstract/Table 3, including which planned analysis family/populations apply.

**Why context does not resolve it:** Route A category 5 retains a prespecified outcome-status change. The report’s safety table is an alternative interpretation of overlapping status, not a reason to suppress the source-defined comparison.

**Alternatives and missing definitions:** Safety and secondary may be concurrent labels, or the protocol/report may use an amended hierarchy different from SAPsection6. The package does not explicitly map those labels to a single prespecified hierarchy for the final analysis.

**Exact human question:** Were BMVdifficulty, airway failure and gastric regurgitation prespecified as safety outcomes, secondary efficacy outcomes, or both, and which status/analysis specification governed the reported abstract and Table 3 results?

### F-ST1-008

**Title:** Additional prespecified primary and key secondary analysis populations are not identifiable in the reported package.

**Relationships:** S018, S019, S052, S053. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R.

**Exact locations and document roles:** PLAN [plan p121, SAP section5.3](../../../joi180004supp1_prod.pdf#page=121), PLAN [p124, sections8.2.1,8.2.3,8.2.4](../../../joi180004supp1_prod.pdf#page=124), and PLAN [signed p130](../../../joi180004supp1_prod.pdf#page=130) and PLAN [signed p133](../../../joi180004supp1_prod.pdf#page=133), versus REPORT [main p3 analysis definitions](../../../jama_jabre_2018_oi_180004.pdf#page=3), REPORT [p4 primary/safety results](../../../jama_jabre_2018_oi_180004.pdf#page=4), REPORT [p6 Tables2/3](../../../jama_jabre_2018_oi_180004.pdf#page=6), REPORT [results supplement p3,eTable2](../../../joi180004supp2_prod.pdf#page=3). All REPORT pages1–9 and supplement pages1–3 were inspected for the additional analyses.

**Printed statements/values:** SAP requires primary95% CI/NI analyses in ITT,PP and AT; AT groups adult cardiac-arrest patients by technique really received. Secondary analyses also PP and AT. Safety analyses ITT and AT. Report supplies primaryITT1018/1022 andPP995/943; Table 2 secondaryITT/PP; Table 3 actual-treatment safety1028/999. eTable2’s post hoc reclassification uses863/1174 and a conventional95% CI/P, not a labeled primary NI AT analysis.

**Rule and calculation:** Match planned populations and decision rules, not merely “as-treated” wording. No supplied table identifies the prespecified primary AT NI result, AT key-secondary admission/day 28 survival results, or ITT airway-difficulty/failure/regurgitation results. Those secondary results appear in the abstract and therefore are key secondary under the scope definition. The different eTable2 population and post hoc label do not establish equivalence to the SAPAT set or its planned NI rule.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecified primary AT favorable-survival NI estimate/CI and key-secondary results in the additionally planned populations.

**Why context does not resolve it:** Route A category 5 retains a planned primary/key-secondary analysis not reported. The safety AT table and post hoc reclassification corroborate that additional received-treatment analyses exist, but do not supply the planned population-specific results.

**Alternatives and missing definitions:** The eTable2 row might have been intended to serve as the primary AT result, but its mapping to the SAP set, NI decision and other AT outcomes is absent. The additional results may exist outside the supplied package or may have been superseded; neither explanation is disclosed here.

**Exact human question:** Where are the SAP-prespecified primary AT NI analysis, AT admission/day 28 survival analyses and ITT airway safety analyses, or what disclosed analysis amendment replaced them and how does eTable2 map to those planned sets?

### F-ST1-009

**Title:** Reported airway failure represents a component of the protocol’s technique-failure composite, without an explicit mapping.

**Relationships:** S042, S054, S055. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R.

**Exact locations and document roles:** PLAN [plan p16, original protocol section4.1.2](../../../joi180004supp1_prod.pdf#page=16), PLAN [p71, final protocol section4.1.2](../../../joi180004supp1_prod.pdf#page=71), PLAN [p110, amendment composite specification](../../../joi180004supp1_prod.pdf#page=110), versus REPORT [main p1 secondary endpoints/results](../../../jama_jabre_2018_oi_180004.pdf#page=1), REPORT [p3 Outcomes](../../../jama_jabre_2018_oi_180004.pdf#page=3), REPORT [p6 Table 3 BMV or ETI failure](../../../jama_jabre_2018_oi_180004.pdf#page=6).

**Printed statements/values:** Protocol technique failure is day 28 mortality OR regurgitation during the procedure OR procedural failure, explicitly inability to ventilate BMV or to intubate ETI. Report lists rate of BMV/ETI failure and reports69/1028(6.7%) versus21/996(2.1%). The supplied report does not identify a combined mortality/regurgitation/procedure-failure result. Day28 deaths in Table 2 are963/1018 and 968/1022, showing the reported failure rate is not the planned death-containing composite.

**Rule and calculation:** A union containing day 28 death cannot be the small procedural-failure risk reported as6.7% or2.1% in this trial. Different safety/ITT populations prevent an exact common-denominator recomputation and are not silently equated; the source definition itself distinguishes composite versus component. Composite status/definition is compared directly.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Definition and prespecified status of the airway failure result in the abstract/Table 3 and whether that result represents the planned technique-failure composite.

**Why context does not resolve it:** Route A category 5 retains a prespecified composite-definition change; the report does not explicitly map the similarly named failure result to the separate procedural component or report the composite.

**Alternatives and missing definitions:** Procedural failure may be a separately planned safety component and the report may intend only that endpoint; the composite may simply not be presented. Missing definition: the endpoint map linking the reported “BMV or ETI failure” to the protocol composite and its component.

**Exact human question:** Does the reported BMV/ETI failure result represent the planned technique-failure composite or its procedural component, and where is the composite defined by death, regurgitation or procedural failure accounted for in the final outcome hierarchy?

## Excluded observations

These are only apparent issues considered and not emitted; successful reconciliations are recorded in the S coverage table. Each row has exactly one reason code. No reproduced Route A category is excluded.

| Location | Observation | Reason code |
|---|---|---|
| PLAN pp36,90,121,130 hypotheses; operational rule pp37,91,124,133 | H0 and native H1 share equality at−.01. The supplied strict lower-CI rule identifies the operational boundary at once; no signed numeric change is involved. The distinct positive number on scanned p130 is F-ST1-005. | NOTATION_OR_TYPOGRAPHY |
| REPORT main pp3,4; PLAN pp124,133 | Two-sided95% method versus one-sided 97.5% result. Both use a.025 lower tail; the bound and NI decision are identifiable, with no conflicting printed tail probability. | CONTEXT_RESOLVES |
| REPORT main p6, PP day 28 survival | Count-derived difference.018864 versus printed.1. Allowing integer input±.5 gives difference[−.09001,.12773], overlapping printed[.05,.15]. This excludes only the point difference, not F-ST1-002’s intervals. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p6, PP admission lower CI | Reproducing-method lower endpoint conservative[−8.29972,−8.02185] versus printed[−7.65,−7.55]. Remaining gap.37185/7.6=.04893≤.05. Upper endpoint qualifies separately in F-ST1-002. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p6, PP CPC 1 ETI | 34/943=3.6055% versus3.5%. Allowing34±.5 and 943±.5 gives[3.55061,3.66048]; printed[3.45,3.55], gap.00061/3.5=.00017≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p4, CCF | Normal-tail P reconstructed from displayedCI would differ from.70. No per-row mean/median, t/Mann–Whitney choice, dispersion or distribution is supplied; exact P dependence on the interval would be assumed. Null/significance agree. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p4, pauses | Difference11 “seconds” appears after repeated descriptions as number of pauses;27−16=11 identifies a count immediately. Unit-only wording does not change a printed number. | NOTATION_OR_TYPOGRAPHY |
| REPORT main pp3,4; PLAN pp17,72,92 | Unadjusted primary versus center-stratified randomization and post hoc random-center model. No supplied primary model claim requires center adjustment, and the hierarchical difference.05 is explicitly modeled. | MODEL_VERSUS_CRUDE |
| PLAN pp36,91 versus pp120,129 | Protocol interim looks at 50%/75% versus SAP final-only analyses. SAP explicitly states cancellation; there is no reported conflicting numerical stopping/futility conclusion. | CONTEXT_RESOLVES |
| PLAN pp37,92,123,132; REPORT main pp4,6 | Alternative imputation/MI sensitivity trigger may appear unreported because PP differs from ITT. “Large” is not defined; primary follow-up/CPC tables supply no missing outcomes to replace. No trigger activation is stated. | CONDITIONAL_OR_UNREPORTED |
| PLAN pp37,92 versus REPORT main statistical/results sections | Planned exploratory prognostic logistic regression has no reported result; it is not a planned primary/key-secondary result-producing analysis or a claim that reported values came from that model. | PERIPHERAL_COMPARISON |
| PLAN pp38,92 versus pp124,133 and REPORT main p4 | SAS 9.2 versus9.4 without a model, result, population or decision change. | PERIPHERAL_COMPARISON |
| PLAN pp16,71 versus REPORT result pages | Non-key secondary mRS,discharge survival,TI completion/interruption durations,CPR duration and individual complication inventory not reported. They are not abstract results or designated key-secondary analyses; count-based pause results are explicitly post hoc. | PERIPHERAL_COMPARISON |
| PLAN pp25,33,80,87 versus schedule pp21,76 and REPORT main p3 | IDS/VAS grouped with day 28 instruments in some plan wording, while explicit out-of-hospital lists and schedule identify their procedure-time role. No conflicting reported number is mapped to another timepoint. | TERMINOLOGY_OR_WORDING |
| PLAN pp52,103, IDS | Impossible category∞ versus finite score at abandonment in scale instructions. No supplied failure case score or result depends on selecting one; conventional category versus recorded score wording is resolvable. | TERMINOLOGY_OR_WORDING |
| REPORT main pp4,6 versus results supplement p3, pre-ROSC reclassification | 155 removed fromBMV but152 added toETI; total2040→2037; event87→86. Integer half-unit intervals give expected ETI[1176,1178] versus printed[1173.5,1174.5], gap1.5/1174=.00128≤.05; event-total intervals overlap. Apparent three-patient difference alone is screened. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main pp3,7 versus PLAN pp12,67 | Historical registry counts650000 versus649359 and historical ETI survival1.1% versus1.0% differ in background copies. The prespecified planning inputs are explicitly BMV 3%,ETI 2% in every sample-size section; the background copies do not change those inputs or a trial result. | PERIPHERAL_COMPARISON |
| PLAN pp37,91,124,133 versus REPORT main pp3,6 | Methods specify OR and difference intervals, while results present differences only. No printed OR is mislabeled, and parallel effect-measure presentation alone does not establish a missing distinct primary/key-secondary analysis. | CONDITIONAL_OR_UNREPORTED |
| PLAN pp123,132 versus REPORT main pp5,6 | The descriptive-summary list includes min,max and mean intervals not all presented in the report’s baseline/scale summaries. This does not change a primary/key-secondary result or its producing analysis. | PERIPHERAL_COMPARISON |

## Source-grounded calculation and limitations

Fresh derivatives are stored only under preprocessing/statistics_1: main-layout.txt, results-layout.txt, sap-layout.txt; main-p6.png, results-p3.png, plan-p121.png and plan-p130.png. Engines: direct Poppler pdftotext and pdftoppm25.03.0; compute device CPU. Command list and arithmetic are in preprocessing/statistics_1/calculation_record.md. No OCR or Python helper was needed.

All reported intervals contain their printed estimate and have ordered endpoints. All printed null-versus-P/significance checks reconcile; the interval-limit findings are retained under the distinct same-display reproducing-method category. No current-trial SE or test statistic is supplied. Exact algorithms for the primary NI P values, binary CIs, χ²/Fisher row choice, continuous variance/test and simulations are missing; diagnostic normal approximations are not source assertions. Numerical futility and imputation-trigger rules are absent. Scientific coverage gaps: none. Findings await an independent inclusion screener and human adjudication; no severity, disposition or correction is assigned.

Completion counts: 81 relationships;9 findings;19 excluded observations;146 mapped physical pages across 3 sources.
