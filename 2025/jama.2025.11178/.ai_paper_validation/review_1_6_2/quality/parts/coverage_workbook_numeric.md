# Bounded quality audit — workbook, numeric inventory and RAW pass-2 checker

## Integration summary

COMPLETE for the assigned audit: DOC-006 one worksheet `eTable 3`, A1:J115; all 525 populated literal cells; S256 and S257 in both statistical passes; all 84 numeric families N001–N084; all five numeric findings and seven numeric exclusions; RAW pass-2 finding F-ST2-1001, its three exclusions and its 47-row revisit of original exclusions. No new finding is required. The five numeric findings remain supported by source values and the inclusion threshold; F-ST2-1001 remains supported as an explicitly diagnostic interval/test question, with unavailable inferential definitions preserved. Six findings each have exactly one canonical screening decision. Stable-card inclusion and classification are owned by the canonical auditor, not duplicated here.

Required repair: generated numeric-checker links use nonexistent spaced supplement filenames in F-NUM-002, F-NUM-003 and F-NUM-005. Replace only their targets with the supplied `joi250046supp5_prod_1755300121.16087.xlsx` and `joi250046supp4_prod_1755300121.15587.pdf`; preserve pages/cells/values. Coordinator notified. No scientific screening change, new candidate or suppression follows. Optional consistency repair: retain `.003205` rather than the rounded `.00318` in the RAW revisit's workbook-completeness diagnostic; both are below .05.

Source coverage closes 147/147 package units, including workbook 1=1 reusable+0 fresh-required and mapped=1. Review-stage controls remain in progress at audit time: finish registration, appended recheck, quality and report coverage rows and manifest entries before final validation. Neither a count target nor prior candidate selection appears in assigned discovery records. No web, source mutation, legacy conclusions, broad methodology auditor disposition used.

## Scope and direct authority

Read completely QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md; read the complete bounded current-run packet `review_packets/audit_workbook_numeric.md`, source_coverage.md, coverage_manifest.md and agent_execution_manifest.md. The packet contains the complete worksheet map, both S256/S257 records, complete numeric inventory and appendices, complete numeric checker and complete RAW pass-2 checker. The packet is an integration aid; exact supplied sources determine values.

Direct workbook authority was read with `unzip -p` for `xl/workbook.xml`, `xl/sharedStrings.xml` and `xl/worksheets/sheet1.xml`. Byte comparisons against the existing current-run XML derivatives returned identical content for all three. Local Node JavaScript parsed these source-confirmed XML files and compared every populated address/value with the full worksheet map. Source confirmation covers all cells, not a sample. The initial attempt to spawn unzip from Node returned EPERM; direct shell unzip succeeded, so no extraction limitation remains. No Python extraction or scientific orchestration was used.

Exact worksheet identity: `eTable 3`; sheetId 2; one sheet. The worksheet has 1140 stored/styled cell elements, of which 525 contain literal string or numeric values; zero formulas. The 525 map values match the exact XML/shared-string values, with zero missing addresses and zero differing values. A115 is styled/blank; it is not an omitted numeric row. Source links from this assigned part: [workbook](../../../../joi250046supp5_prod_1755300121.16087.xlsx), worksheet `eTable 3`, A1:J115.

Nine distinct page images were visually read: main PDF pp.4,9,10,11; results PDF pp.7,14,15,17,18. Current-run images in numeric_review and stat1_raw retain pinned PyMuPDF1.26.4 CPU provenance; original main p.9/results p.7 reusable source-page images were used only as page evidence. Values and page identity agree with the supplied source identities, current maps and direct mechanical recheck scope. No page was newly rendered by this shard; the distinct inspected-image count remains below 32. The bounded packet is approximately 116000 scientific characters; no full canonical support map or full ledger/recheck was loaded.

## Worksheet and inferential-family closure

| Assigned component | Complete evidence audit | Result |
|---|---|---|
| Rows 1–3 and B3:E3 | All overall/completeness labels, headers and counts; 2331,295,468,1568 | 295+468+1568=2331;468+1568=2036 |
| Rows 4–48 | All sites, demographics, education, income, marriage, race, residence and social determinant cells and missing counts | Every populated value represented; complete categorical partitions use N minus supplied missing counts |
| Rows 49–94 | All clinical conditions, encounter/condition summaries, specific pain sites, duration, PHQ8/GAD7, depression/anxiety, comorbidity and sleep cells | E82 discrepancy retained; other printed count/percentage identities reconcile after display precision |
| Rows 95–109 | All primary/secondary baseline summaries, threshold counts and associated missing counts | Continuous summaries and thresholds are not equated; every populated value represented |
| Rows 110–115 | Missing-denominator rule, common-data/EHR/sex footnotes, model-selection/bold rule, final blank row | Literal footnotes retained; no unstored value invented |
| S256 pass1 | All 32 populated H/I/J P-value cells and A114 selection rule | PASS_1_COMPLETE; separate MCID/nonresponse/3-month-missingness test identities retained |
| S256 pass2 | Exact-source H2/I2/J2, all 32 P cells and A114 | PASS_2_COMPLETE; values in [0,1] or valid upper bounds; no blank converted into a numeric P |
| S257 pass1 | B3:E3, A110 and results eTable 1 matching keys | PASS_1_COMPLETE; completeness partition and missing-excluded denominator rule checked |
| S257 pass2 | Exact workbook groups and results p.7 counts | PASS_2_COMPLETE; workbook 468 versus alternative 471 remains subthreshold; C017 distinct |

All 208 workbook count/percentage appendix rows were mechanically re-evaluated for source numerator/percentage alignment, printed numerator/denominator ratio and remaining relative gap using the printed percentage's decimal precision. Zero source tuple, arithmetic-ratio or relative-gap discrepancies arose in the derivative calculations. Only E82 exceeds the inclusion threshold. Its exact source inputs are E3 `(N=1568)`, E82 `711 (73.2)`, E83 `2`, A82 current depression PHQ8≥10 and A110 excluding missing from percentage denominators. Thus denominator 1566 has propagated half-unit interval[1565,1567], numerator[710.5,711.5]; recomputed percentage[45.341417,45.463259], printed percentage[73.15,73.25], relative gap .378234. This is route A category 3; reconstructability does not remove the extractable printed 73.2.

No CI, estimate, standard error or test statistic accompanies H/I/J selection Ps. Their numerical inferential reconstruction is therefore unavailable, rather than conflicting. Education H12=.0156/J12=.05/I12 blank meets the source's either-missingness description without asserting an overall-nonresponse P. Weight-membership discrepancies remain in their separately assigned existing candidate scope.

## Complete numeric-family audit

Every row below was read in the complete inventory. Families group an exhaustive source scope; they do not impose a limit on discovery. `COMPLETE` means the assigned family has durable printed inputs/checks and no unresolved coverage gap, including named unavailable definitions where applicable.

| Family | Audited scope and rule | Status |
|---|---|---|
| N001 | Allocation 2333 versus analytical 2331 with two explicit UC exclusions | COMPLETE |
| N002 | Invitation/screening 54497,62125,7628 partition | COMPLETE |
| N003 | Eligibility 4481 and 3147; administrative other-reason list not declared exhaustive | COMPLETE |
| N004 | Consent/randomization 3147→2475→2333 | COMPLETE |
| N005 | PT776 session partition 371+156+249,527 initiating,43% | COMPLETE; F-NUM-001 retained |
| N006 | HC778 partition 548+112+118,660 initiating | COMPLETE |
| N007 | All PT no-session subcategories | COMPLETE |
| N008 | All HC no-session subcategories | COMPLETE |
| N009 | Withdrawal/death/completion 2210 and 94.81% | COMPLETE; prior assessment overlap not assumed absent |
| N010 | Every arm/time and any/all/no-follow-up count | COMPLETE |
| N011 | Age/sex/socioeconomic baseline denominators | COMPLETE |
| N012 | All race categories and category totals | COMPLETE |
| N013 | Residence/social determinant rows; overlapping categories | COMPLETE |
| N014 | High severity and pain-duration counts | COMPLETE |
| N015 | All specific pain-site percentages; overlapping conditions | COMPLETE |
| N016 | Encounter/condition medians and IQRs | COMPLETE; no arithmetic-mean identity imposed |
| N017 | Opioid and mental/related condition counts | COMPLETE; three-site opioid denominator retained |
| N018 | Comorbidity and primary baseline means/medians/dispersion | COMPLETE |
| N019 | Secondary baseline social/physical limitations | COMPLETE |
| N020 | Narrative baseline aggregates and qualified workbook comparisons | COMPLETE |
| N021 | Hospitalization 183,events 247,deaths 17 and arm percentages | COMPLETE |
| N022 | Severity 3 mo group percentages,allRR/NNT point identities | COMPLETE |
| N023 | Severity 6 mo allRR/NNT point identities | COMPLETE; F-NUM-005 retained |
| N024 | Severity 12 mo allRR/NNT point identities | COMPLETE |
| N025 | Intensity 3 mo RR/NNT points;16 versus reciprocal residual.007212 | COMPLETE; precision exclusion retained |
| N026 | Intensity 6 mo allRR/NNT point identities | COMPLETE |
| N027 | Intensity 12 mo allRR/NNT point identities | COMPLETE |
| N028 | Interference 3 mo allRR/NNT point identities | COMPLETE |
| N029 | Interference 6 mo allRR/NNT point identities | COMPLETE; F-NUM-005 retained |
| N030 | Interference 12 mo allRR/NNT point identities | COMPLETE |
| N031 | Severity 3 mo adjusted continuous/SMD common-SD/additivity | COMPLETE; F-NUM-004 retained |
| N032 | Severity 6 mo SMD residual.005,relative.013889 | COMPLETE; precision exclusion retained |
| N033 | Severity 12 mo SMD additive identity | COMPLETE |
| N034 | Intensity 3 mo SMD additive identity | COMPLETE |
| N035 | Intensity 6 mo SMD residual.045,relative.166667 | COMPLETE; F-NUM-004 retained |
| N036 | Intensity 12 mo SMD residual.065,relative.240741 | COMPLETE; F-NUM-004 retained |
| N037 | Interference 3 mo SMD residual.025,relative.073529 | COMPLETE; F-NUM-004 retained |
| N038 | Interference 6 mo SMD residual.025,relative.067568 | COMPLETE; F-NUM-004 retained |
| N039 | Interference 12 mo SMD additive identity | COMPLETE |
| N040 | Social 3 mo SMD residual.295,relative 29.5 | COMPLETE; F-NUM-004 retained |
| N041 | Social 6 mo SMD residual.365,relative 6.083333 | COMPLETE; F-NUM-004 retained |
| N042 | Social 12 mo SMD residual.375,relative 5.357143 | COMPLETE; F-NUM-004 retained |
| N043 | Physical 3 mo SMD residual.255,relative 12.75 | COMPLETE; F-NUM-004 retained |
| N044 | Physical 6 mo SMD residual.335,relative 16.75 | COMPLETE; F-NUM-004 retained |
| N045 | Physical 12 mo SMD residual.385,relative 5.5 | COMPLETE; F-NUM-004 retained |
| N046 | PGICpain 3 mo SMD residual.355,relative.572581 | COMPLETE; F-NUM-004 retained |
| N047 | PGICpain 6 mo SMD residual.265,relative.481818 | COMPLETE; F-NUM-004 retained |
| N048 | PGICpain 12 mo SMD residual.255,relative.447368 | COMPLETE; F-NUM-004 retained |
| N049 | PGICgeneral 3 mo SMD residual.385,relative.583333 | COMPLETE; F-NUM-004 retained |
| N050 | PGICgeneral 6 mo SMD residual.185,relative.37 | COMPLETE; F-NUM-004 retained |
| N051 | PGICgeneral 12 mo SMD residual.215,relative.370690 | COMPLETE; F-NUM-004 retained |
| N052 | Intervention sessions,durations,training arithmetic | COMPLETE |
| N053 | Outreach 356/776→45.9% | COMPLETE |
| N054 | Reviewed fidelity 193+89+17=299 and stated percentage denominators | COMPLETE; full training total unavailable |
| N055 | Outcome scale identities and 30%MCID | COMPLETE |
| N056 | Every session-histogram axis/arm/bar mapped | COMPLETE; exact unlabeled bar counts unavailable |
| N057 | All eTable 1 follow-up percentages and pattern totals | COMPLETE; subthreshold pattern excluded |
| N058 | Imputation/estimation 6108,5449,659 and coefficient/RR identities | COMPLETE |
| N059 | Weight sum 2036,6108 visits,OR identity,scaled inverse probabilities | COMPLETE |
| N060 | Complete-case primary sensitivity 1798 and allrate/RR/NNT points | COMPLETE |
| N061 | Worst/best primary sensitivity 2331,allrate/RR/NNT points | COMPLETE |
| N062 | Prior-enhancement 454/366/149+153+152 population nesting | COMPLETE; F-NUM-003 retained |
| N063 | After-enhancement 1877/1670/1487 subset nesting and points | COMPLETE |
| N064 | Reminder 1038/935/858 and allrate/RR/NNT points | COMPLETE; F-NUM-005 retained |
| N065 | All 27 unadjusted n/N(%) andRR point comparisons | COMPLETE; adjusted model versus crude distinction retained |
| N066 | All 15 unadjusted change-summary rows/contrasts | COMPLETE; medians not substituted for means |
| N067 | All 21 raw-summary rows/contrasts | COMPLETE; source-summary identity assigned separately |
| N068 | Workbook site and completeness partitions | COMPLETE |
| N069 | Workbook age/sex and copied-baseline precision | COMPLETE |
| N070 | Workbook education categories/missing counts | COMPLETE |
| N071 | Workbook employment counts/missing counts | COMPLETE |
| N072 | Workbook income categories/missing counts | COMPLETE |
| N073 | Workbook marriage counts/missing counts | COMPLETE |
| N074 | Workbook race categories/missing counts | COMPLETE |
| N075 | Workbook residence/social determinant counts/missing | COMPLETE |
| N076 | Workbook encounters/conditions/opioids | COMPLETE |
| N077 | Workbook specific pain sites/missing rows | COMPLETE; blanks not converted to stored zeros |
| N078 | Workbook duration categories/missing counts | COMPLETE |
| N079 | Workbook depression/anxiety counts/summaries | COMPLETE; F-NUM-002 retained |
| N080 | Workbook other related conditions/missing | COMPLETE |
| N081 | Workbook primary/secondary baseline andPEG missing | COMPLETE |
| N082 | Entire worksheet 525 populated cells,208 percentage checks,selection headers/flags | COMPLETE |
| N083 | Report effect-measure identity definitions RR/OR/RD/NNT/SMD | COMPLETE; no model/crude substitution |
| N084 | Covers,references and blank/nonresult source units | COMPLETE; no applicable result relationship omitted |

The main baseline appendix contains all 107 explicit count/percentage pairs. Every listed denominator, displayed precision interval and remaining-gap result was read. Counts without printed percentages retain partition checks. Main medians, PROMIS transforms, category overlaps and site-limited opioid denominators are not forced into incompatible identities.

## Numeric-finding audit

| Finding | Exact source-confirmation and threshold audit | Canonical screening mapping |
|---|---|---|
| F-NUM-001 | Main p.4 visibly prints 371(43%) and randomizedPT776 in its matching flow/map. Half-unit percentage[47.714102,47.904578] versus[42.5,43.5],relative.098002. Route A3 counts; no alternative denominator stated. | Exactly one INCLUDE→C002 |
| F-NUM-002 | All seven workbook denominator/row locations read directly from exact ZIP XML/sharedstrings. Percentage interval[45.341417,45.463259] versus[73.15,73.25],relative.378234. Route A3. | Exactly one INCLUDE→C017 |
| F-NUM-003 | Exact results p.14 first header visibly gives 454 randomized,366 anyfollowup,PT149/HC153/UC152 at 3 months. Sum interval[452.5,455.5] versus[365.5,366.5],minimum gap86,relative.234973. Route A3; randomized/weighted-size alternative remains question. | Exactly one INCLUDE→C015 |
| F-NUM-004 | Exact mainp.4 commonUCchangeSD definition and all 17 listed p.10/11 SMDtriples reread. Remaining additive gaps exceed.05 relative for every included row; four other rows subthreshold. Route B counts as method/identity question affecting namedSMDextracts; not crude-versus-model comparison. Companion statistical findings expand the consolidated pattern; no duplicate issue registered. | Exactly one INCLUDE→C003 |
| F-NUM-005 | Main p.9 andresultsp.14 rate/NNTvalues reread, source reciprocal definition retained. Independent JavaScript intervals reproduce three gaps .0509751773,.0627705628,.0572183099> .05. Route A4; upwardinteger-reporting convention and undisplayedRD remain alternatives, not an adjudication. | Exactly one INCLUDE→C004 |

No candidate rests solely on a very small P displayed as zero. No omitted numeric apparent observation in these five groups qualifies as a separate issue. The 17-row numeric SMD additivity finding and companion absolute-scale/sign relationships are one registered issue in the current screening, with all affected locations preserved by the primary auditor.

## All seven numeric exclusions audited

| Original numeric exclusion | Threshold reassessment | Audit action |
|---|---|---|
| 1: follow-up pattern totals,visit sums,650 vs 659/workbook 468 vs 471 | Route A3 considered. Source eTable 1 is visibly 188/283/1568.5458 sum half interval[5455,5461] versus observed 5449[5447.5,5450.5],relative gap.000826; completeness 468 vs 471 lower gap1.5/468=.003205. Remainingmissing-count gap likewisebelow.05. | Retain ROUNDING_OR_DISPLAY_PRECISION |
| 2: main/workbook descriptive copies | Female 1712 vs 1713 half intervals touch; currentdepression 47.8 vs 47.9 half intervals touch. Other copied descriptive values are qualified/peripheral; E82 within-display discrepancy remainsseparate. | Retain ROUNDING_OR_DISPLAY_PRECISION |
| 3: other reciprocal NNT points/fourSMDrows | Route A4 requires reproducedgreater-than.05 point gap. Main intensity 3 PT/UC[14.925373,15.384615]vs 16[15.5,16.5],relative.007212. Maximum other excluded NNT gap.048611. Severity 6 SMDadditivegap.013889 (alternative reference .041667) remains below.05. Category 1 interval/test observations are tracked separately, never removed here. | Retain ROUNDING_OR_DISPLAY_PRECISION |
| 4: eTable 10/11 rawcenter subtraction vs GEEmean differences | Source explicitly separates medians/quartiles and fitted mean contrasts; no equality between these quantities is stated. Summary identity candidate remainsseparate. | Retain CONDITIONAL_OR_UNREPORTED |
| 5: fidelity 1791+2350=4141 vs 4626 | Reviewed counts 193+89+17=299 reconcile. Source lacks full training-session denominator; an exhaustive complete-session partition is not asserted. No reproducedRoute A3 arises from absent component alone. | Retain CONDITIONAL_OR_UNREPORTED |
| 6: randomized 2331,fittedcontributors 2036,weight 2036/6108 | Source explicitly distinguishes target populations,persons,repeatedvisits and nonresponse/imputation steps; no matching numerical quantity conflicts. | Retain CONTEXT_RESOLVES |
| 7: roughly 40% rural vs 44%baseline | Explicit approximation contextualizes narrative; does not replace baseline 44%extract. | Retain CONTEXT_RESOLVES |

## RAW pass-2 finding and calculation audit

F-ST2-1001 has exactly one canonical INCLUDE decision, mapped to C018. Physical function 6/12 source p.17 tuples were visually read in every contrast/P column; p.18 specifies unadjusted linear GEE mean differences and 95%CIs; p.15 calls the display a replication without adjustment,weighting or imputation. Main p.11 Wald/three group note corroborates diagnostic family rather than supplying a conflicting copy. REPORT internal S_W and statistical_results remain consistent; no S_C relationship is created merely by corroboration.

All 19 witness calculations in `preprocessing/stat2_raw/calculation_record.md` were independently recomputed in JavaScript from printed witness points/halfwidths. Every additive contrast relation holds up to machineprecision; every Q agrees to its printed precision; each diagnosticP matches its displayedPinterval or<.001 bound. Social 3 Q 13.4119895427,P.00122355494 matches.001±.0005; physical 3 Q 3.10158751217,P.21207956755 matches.212±.0005. All 17 other witnessesgiveP<.001. Witnesses demonstrate same-display numerical reproduction, not identification ofthe authors' fitted method.

The conservative physical bounds were independently recomputed over every outer region point vertex and all 8 variance box vertices. Minimum vertex determinants are positive(.01195380637/.02217991416), so the whole affine variance boxes are positive definite. The joint Wald quadratic is convex separately in point vector and covariance matrix; successive vertex maximization bounds the enlarged Cartesian product region. Ignoring CI center/width coupling and,for 12 months,the third contrast constraint only enlarges the feasible set. Thus the bound covers all precision-feasible parameters under this diagnostic family and does not depend on a finite grid search.

| Source physical row | Conservative maximum diagnostic Q | Diagnostic P lower bound | Printed P half-unit interval | Gap/printed P |
|---|---:|---:|---|---:|
| 6 months,MD1.1(.3,1.9),.4(-.3,1.1),-.6(-1.4,.1) | 8.556087823817016 | .013869766053172373 | [.0045,.0055] | 1.6739532106 |
| 12 months,MD1.2(.4,2),.9(0,1.8),-.3(-1.2,.6) | 12.281125558721055 | .0021537112129520757 | [.0005,.0015] | .6537112130 |

Reproduction is supported under the explicit common 95%normal-CI/two-dimensionalchi-squareWald diagnostic family that reproduces other 19 rows. Route A1 interval/test status avoids a precision-removal decision. No exact author covariance,confidence critical value,reference distribution,df or test implementation is inferred. DifferentCI/test covariance or estimands remain genuine human questions, not concealed assumptions. Both printedPs remain below.05; no .05-level superiority reversal or trial conclusion change isasserted. The sampledP ranges are diagnostic and are notproofs or replacement values. Theproofbounds are theinferential-method question's numerical support.

## All three RAW pass-2 exclusions audited

| RAW excluded observation | Reassessment | Audit action |
|---|---|---|
| Remaining 9 fractional PGIC centers | Integer/half-integer ordinary median lattice after±.05 leaves.05 gap; relative .017241–.031250≤.05. Five qualifying PGIC locations and all 21 summary identity rows remain C016. | Retain ROUNDING_OR_DISPLAY_PRECISION |
| Rawcenter subtraction/permutation versus fitted GEE mean contrasts | The quantity definitions are medians and fitted means. An alternative arm permutation diagnostic does not establish equality or a contradicted arm identity. | Retain CONDITIONAL_OR_UNREPORTED |
| Existing mean/median identity and five qualifying median locations | Already retained C016/F-XS-008 with F-ST1-601 duplicate; no stable ID merging/suppression proposed. | Retain DUPLICATE_OF_INCLUDED |

## All 47 original-exclusion revisits audited

This audit checks the RAWchecker's complete revisit table and its reasoning against the scope categories. Original nonnumeric lanes' exact source/card inclusion is assigned to companion audits; no fresh row-levelsourcecheck oftheirwhole scopes is claimedhere. Every route A category and precision exception was considered. The full originaldecision provenance remains in current checker parts.

| Original ordinal | Reassessed observation | Audit result |
|---:|---|---|
| 01 | Numeric pattern totals/visits/D3 | Subthreshold count gaps; retain precision |
| 02 | Numeric baseline copies | Qualifiedcopy/subthreshold; retain precision |
| 03 | Numeric otherNNT/SMDpoints | Subthreshold method points; existing qualifying patterns retained |
| 04 | Numeric medians versus modeledMD | Source equality not established; conditional remains |
| 05 | Numeric fidelity denominator | Unreported training total; no exhaustive partition contradiction |
| 06 | Numeric populations/weights | Explicitly different quantities; context resolves |
| 07 | Numeric approximation 40/44 | Explicit approximation; context resolves |
| 08 | Cross narrativeSMDcopies | Half-unit gaps 0/.01;relative 0/.0294≤.05 |
| 09 | Cross adjusted/alternative analyses | Explicit model/population distinctions; no matchedcopy |
| 10 | Cross eTable 9 adjustedtitle | Adjacent unadjusted definition resolves method label |
| 11 | Cross eTable 10 mean/median wording | Distinct descriptive and fitted summaries |
| 12 | Cross interference wording/timing | Adjacent outcome/window definition; no changed status/composite |
| 13 | Cross 140/454 calendar counts | Administrative calendar quantity; explicit fitted subset separately retained |
| 14 | Cross workbook 468/471 | Exact relative .003205≤.05; retain precision |
| 15 | Cross eligibility omissions | No affirmed conflicting population/count; missing detail alone |
| 16 | Cross moderator/mediator timing/equation | Ancillary plan internal elements without reported primary/keysecondary impact |
| 17 | Cross PGIC/arm terminology | Adjacentscale andarm definitions resolve naming |
| 18 | Cross ancillary output absence | No established changed outcome status or unreported primary/keysecondary analysis |
| 19 | Main severity 6 SMD | .041667 underalternate reference≤.05; qualifyingC003 rows remain |
| 20 | Main narrative severitySMD | Same subthresholdcopyas 08 |
| 21 | Main physical 6 P=.05 gate | PrintedPinterval [.045,.055] admitsgateP<.05; no pairedinterval/Pconflict established |
| 22 | Main simulation samplesize | Exact simulation unavailable; no statedalgorithm/same display reproduction conflict |
| 23 | Main PGICmean-changeheading | Immediatechange-impression definition; C016 distinct |
| 24 | Main intensity/interference wording | No numeric/status/composite contradiction established |
| 25 | Main benefit narrative | No all contrast claim conflictingwith direction/nullcoverage |
| 26 | Reports pattern counts | Same subthreshold family as 01 |
| 27 | Reports otherNNTpoints | Maximum .048611≤.05; C004 qualifyingrows retained |
| 28 | Reports extraCIwidth/Pdiagnostics | Exact mapping absent without same-display reproducing family established; direct null conflicts retained C014 |
| 29 | Reports imputation coefficient direction | Conditional coefficient without contradictory directionstatement |
| 30 | Reports weightscale 2331/2036 | Adjacentweight/person/visitdefinitions distinct |
| 31 | Reports severity omittedlist | Narrative and complete fitted models explicitlyinclude it |
| 32 | Reports eTable 9 title | Same immediate unadjusted definition as 10 |
| 33 | Reports eTable 10 median/mean | Separate quantities,not mismatching copies |
| 34 | Reports VClabel | Adjacent arm identity resolved; no number reassignment |
| 35 | Plans normal power diagnostics | Alternative unstated algorithm does not reproduce statedsimulation |
| 36 | Plans relative change term | Active/controlratio explicit and coherent |
| 37 | Plans interference intensity word | Adjacent seven item definition resolves wording |
| 38 | Plans missing 3 month cell | Adjacent primary analysis/window supplies definition |
| 39 | Plans moderator 6/3 month | Ancillary plan comparison without named primary/keysecondary result impact |
| 40 | Plans mediation equation term | Unfitted ancillary quantity; no contradictory reported result |
| 41 | Plans mediatorbaseline | Notification survey explicitly designated baseline |
| 42 | Plans historical 30/current 60 eligibility | Disclosedhistory/current definition distinction |
| 43 | Plans qualitative framework list | Outside quantitative/statistical design focus |
| 44 | Plans hospitalization review update | Disclosed amendment; no outcome-status/definition conflict established |
| 45 | RAW fractional PGIC centers | Individual ordinary median gaps≤.05; summary issue retained |
| 46 | RAWcolumns versus meancontrasts | Different quantities; conditional remains; C016 retained |
| 47 | RAW physical 6/12 omnibus reconstruction | Reopened with 19 row reproduction and conservative bounds; now F-ST2-1001→C018,not excluded |

The 47-row reconsideration is complete;46 prior exclusions remain supported by its statedreasoning and one was independently screened/registered. No additional F-QA finding arises from this assigned checker audit. No small-P-as-zero observation is promoted; interval-versus-P/test and point outside interval categories are not suppressed by a≤.05 numerical precision condition.

## Controls, repairs and limitations

Every direct-source row satisfies reusable+fresh-required=total and mapped=total:14=14+0;77=20+57;29=0+29;7=7+0;19=18+1;1=1+0. Total 147=60+87=mapped 147. The workbook source-unit scope is one complete worksheet rather than 525 separateunits. Source maps cover all styled/blanks aswellasall populatedvalues.

At audit read time each coverage artifact cell contains one plain relative path; complete assigned mappings/checkers/both pass parts are present. Statistical primary runtime root/stat1_main is distinct from root/stat2_main_early; root/stat1_reports/root/stat2_reports_late and root/stat1_raw/root/stat2_raw are also distinct fresh gpt-6.1-sol/high. Initial root/initial_screen and pass 2 root/pass2_screen are distinct fresh high screeners. Optional PLAN context repair agents are separately recorded. Current review quality/report stage rows and appended C018 recheck closure require coordinator finalization; this shard does not claim those future outputs are complete. All actual agents,including this optional shard,must remain in manifest once.

No old candidate listor count target appears in assigned source discovery/self-screen decisions. Every observed repeat pattern has one existing issue mapping; no stableC ID isdeleted,ranked,merged or suppressed. Stable candidate-card fields, exact report classification agreement andall 18 inclusion audit states belongtothe canonicalauditor. Current artifact neutral word scan returned only standard error in statistical method statements; forbidden descriptionsof authors/values werenotfoundin numericchecker/inventory or RAWpass2 checker.

| Repair | Reason | Coordinator action |
|---|---|---|
| Numericchecker F-NUM-002 workbooklink;F-NUM-003/005 supplementlinks | Target filename contains insertedspaces and does not resolve to supplied source | Mechanically repair generated targets and copied current run links;donotchange source or values |
| RAWrevisit ordinal 14 `.00318` summary | Exactpropagated countsum gap1.5/468=.0032051282; both readings remain below.05 | Optional diagnostic clarification; no screenchange |
| Finalmanifest/coverage stages | Audit occurs before full QA/report completion | Coordinator record each actual audit/reportagent and every assigned artifact once; close appended recheck and all candidate-stage scopes |

Remaining source limitations are exact training-session total; unlabeled histogram numerators; raw participant values; UC change SDs; unrounded risk differences; CI/test reference distributions,df/covariances; model selection test statistics. Their absence is named rather than guessed. It leaves no scientific coverage gap for the assigned worksheet,N families or checker outputs. For F-ST2-1001 the diagnostic reconstruction must remain clearly distinguished from the unknown author procedure; no correction or paper-level impact is recommended. Every candidate remains Pending Human Adjudication.

## Coordinator repair completion

Allgenerated exactsource links now use suppliedfilenames and artifact-relativepaths; sourcepages/cells/values preserved. Linkrepair is resolved. The optional subthreshold completeness ratio depends on which printed copy is the reference (.003205 for468 versus .003185 for471); bothremainbelow.05 and neither affects inclusion. Currentappendedrecheck is complete forC018; finalquality/report controls remain coordinatorwork.
