# Statistical consistency review: pass 1

Runtime: /root/statistics_pass1. Fresh gpt-6.1-sol agent, high effort. Scope: every inferential and statistical-method relationship in all supplied sources, DOC-001 REPORT11pages, DOC-002 PLAN113pages, DOC-003 REPORT8pages. Complete main/support mappings read; direct native/layout source text reread at statistical/result locations. Five findings and eight excluded apparent observations. Stable inventory:105S IDs,73 numeric inferential rows and32 method/design/graph families, all PASS_1_COMPLETE. No scientific coverage gap. No candidate IDs or human dispositions assigned.

The numerical checks covered point containment, endpoint order, direction, null/interval/P compatibility, source-grounded method logic, sample-size inputs, primary/global tests, secondary/post-hoc/moderator rows, multiplicity and prospective missingness/sensitivity rules. Exact inverse-test reconstruction is limited where df,covariance,log-likelihoods,full power-software defaults or moderator scaling are absent. Normal/Wald inverse calculations are diagnostic approximations, never substitute analyses. All printed BH values reproduce with input rounding. No noninferiority,equivalence or numerical interim/stopping boundary is supplied for this trial.

## Findings

### F-ST1-001

**Title:** Three-month obesity confidence interval and multiplicity-corrected P value give different null decisions.

**Relationships:** S026,S082. **Compared locations and roles:** REPORT [main Table3,physical p9,3mo row and footnotesb/c](../../../jama_barkin_2018_oi_180075.pdf#page=9); REPORT [main Results,physical p7,Post-hoc Analyses](../../../jama_barkin_2018_oi_180075.pdf#page=7); REPORT [main Statistical Methods,physical p4](../../../jama_barkin_2018_oi_180075.pdf#page=4). All locations belong to one REPORT document; primary relationship S_W; all relationships S_W.

**Printed values:** Adjusted obesity RR0.51,95%CI0.29–0.92,rawP.02,correctedP.10. Table3 footnoteb attributes RR to Poisson regression with robust standard errors adjusting baseline childBMI,age,sex;footnotec BH corrects five comparisons. Mainp4 states two-sidedα=.05. Mainp7 explicitly says the three-month effect was statistically significant before correction.

**Rule and calculation:** NullRR=1. The entire95%CI is below1,while correctedP.10>.05. The rawP.02<.05 matches the uncorrected95%CI. BH arithmetic itself reproduces:five×.02=.10 for the smallest rawP;remaining orderedP.13,.16,.57,.90 do not lower that value. This finding concerns the joint printed interval/corrected-test reading,not BH arithmetic. Category 1 is exempt from the display-precision screen. Even rounding upperlimit in[.915,.925] does not cross1;correctedP in[.095,.105] remains>.05.

**Focus area:** B. **Proposed review domain:** statistical_results.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** Three-month adjusted obesity RR0.51,its95%CI,and its inferential status after the stated correction.

**Why context does not resolve it:** RouteA category 1 requires retaining an interval-versus-P decision conflict even when the source attributes the interval and correctedP to different analyses. The correctedP and95%CI appear together in the same row and support different null decisions.

**Source-grounded alternatives and missing definition:** An uncorrected confidence interval paired intentionally with raw and BH-adjusted P values is supported by the rawP column and explicit narrative;this is a credible alternative rather than an inferred production explanation. No multiplicity-adjusted interval or rule mapping the95%CI to the correctedP is supplied. No preferred correction is proposed.

**Exact human question:** Is the0.29–0.92 interval intended solely as the uncorrected95%CI,while the correctedP.10 controls the multiple-time-point inference,and which inferential reading should accompany extraction of the three-month RR?

**Source confirmation:** Direct Poppler layout from p9/p7/p4 and source-linked rendered Table3 page visually confirm all values and column labels.

### F-ST1-002

**Title:** Three-month adjusted BMI estimate does not reproduce the interval-center rule supported by the other eTable1 rows.

**Relationships:** S031-S035. **Compared locations and roles:** REPORT [results supplement eTable1,physical p2,3month row](../../../joi180075supp2_prod.pdf#page=2) versus REPORT same-table9/12/24/36month rows and footnoteb. Primary relationship S_W;all relationships S_W.

**Printed values:** At3months,adjusted BMI difference−0.01 with95%CI−0.12 to0.13,rawP.83,correctedP.83. At9months:−.04(−.20,.12);12months:−.05(−.23,.13);24months:−.03(−.28,.22);36months:.05(−.29,.38). Footnoteb:estimates from the longitudinal mixed-effects regression model.

**Rule and calculation:** The additive symmetric-interval center (L+U)/2 reproduces the other four rows at displayed precision:−.04,−.05,−.03,and.045 compatible with.05. At3months it instead gives(−.12+.13)/2=+.005. Each two-decimal endpoint has half-unit.005:L∈[−.125,−.115],U∈[.125,.135],giving recomputed midpoint∈[0,.010]. The printed estimate−.01 has rounding interval[−.015,−.005]. Minimum gap=.005;relative discrepancy=.005/abs(−.01)=.50>.05. Thus no admissible rounded inputs reproduce a symmetric interval centered on the printed estimate. This is independent of null compatibility:the point is contained andbothCI/rawP support nonsignificance.

**Focus area:** B/C. **Proposed review domain:** statistical_results.

**Qualifying route:** Route A, category 4.

**Affected result or extracted value:** The three-month adjusted intervention-minus-control BMI difference−0.01 and its95%CI−0.12 to0.13;potential extraction of sign/magnitude from a table of model contrasts.

**Why context does not resolve it:** Category4 retains a printed estimate or interval that does not reproduce a rule reproducing the other rows. A guessed intended sign or endpoint is not a supplied value;the row could be extracted as printed. The issue is not asserted to be point-outside-interval.

**Source-grounded alternatives and missing definition:** The table may use an asymmetric interval construction or a separately computed contrast at this time point;footnoteb names a mixed-effects regression but supplies no interval-construction rule distinguishing this row. The symmetric rule is empirically supported by allfour other rows;no convention alone establishes it. An unreported row-specific interval method remains the human question. No alternate estimate or final correction is assigned.

**Exact human question:** Which interval/contrast calculation produced−0.01(−0.12,0.13) at3months,and why does its center differ from the printed estimate when the same symmetric-center rule reproduces all other time points?

**Source confirmation:** Direct pdftotext and visual reading of the exact source-linked eTable1 page confirm the minus sign and both endpoints;no derivative-only discrepancy.

### F-ST1-003

**Title:** Retained primary BMI sensitivity analyses have no reported results in the supplied package.

**Relationships:** S089,S091,S092,S093. **Compared locations and roles:** PLAN [original protocol p40](../../../joi180075supp1_prod.pdf#page=40),[p41](../../../joi180075supp1_prod.pdf#page=41),[p42](../../../joi180075supp1_prod.pdf#page=42);PLAN [revised protocol p93](../../../joi180075supp1_prod.pdf#page=93),[p94](../../../joi180075supp1_prod.pdf#page=94),[p95](../../../joi180075supp1_prod.pdf#page=95);PLAN [final analysis-adjustment summary p113,lines4129-4133,4144-4148](../../../joi180075supp1_prod.pdf#page=113). Comparator:REPORT [main statistical methods p4](../../../jama_barkin_2018_oi_180075.pdf#page=4),[primary results p6](../../../jama_barkin_2018_oi_180075.pdf#page=6),[Figure3 p7](../../../jama_barkin_2018_oi_180075.pdf#page=7),and complete REPORT [supplement pp1-8,contents p1](../../../joi180075supp2_prod.pdf#page=1). Primary relationship P_R;all relationships P_R.

**Printed statements:** Standard multiple imputation100draws and descriptive missing/nonmissing comparisons are planned. Finalp113 explicitly says MIwith/withoutauxiliaryvariables is still planned while ML is primary. Originalp40/revisedp93 state a safeguard cluster-structure fit and comparison of standard errors;finalp113 retains exploring heterogeneous variance secondarily. Originalp40/revisedp93 also propose linear-spline and restricted-cubic-spline checks of the quadratic trajectory and added baselineBMI×treatment/other model features. Main describes ML quadratic analysis and moderator series;the complete results supplement contains only BMI time-point contrasts,moderator coefficients,and three figures. It contains no MI-versus-ML,cluster-versus-primarySE,heterogeneous-variance or alternative-shape primary sensitivity outputs.

**Rule and reproduced comparison:** Planned primary-outcome sensitivity analyses remain source-linked design elements even when termed secondary analyses. Searching all REPORT result locations and the complete supplement contents yields no outputs for the retained MI and cluster/heterogeneous comparisons. The spline/additional-model proposals are associated locations in this omission pattern rather than a demand that every listed example be mandatory. Conditional constrained-MI thresholds,reweighting and pattern-mixture options are not treated as definitely required. This is a logical absence comparison;display-precision intervals are not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The reported primary36-month BMI trajectory conclusion,jointP.39,and its robustness under the explicitly retained missing-data and covariance/cluster sensitivity analyses.

**Why context does not resolve it:** RouteA category 5 retains a planned primary analysis not reported;the final adjustment summary expressly retains these primary-outcome sensitivity components. Reporting the primary ML result does not provide the named alternative results.

**Source-grounded alternatives and missing definition:** These analyses may have been performed but omitted from this paper/supplement,orreported in a document outside the supplied package;absence here does not establish absence of conduct. Some shape/model checks use suggestive/conditional wording and could have been judged unnecessary. The unconditional retained MI and heterogeneity/cluster comparisons anchor the finding. No model output supporting such decisions is supplied.

**Exact human question:** Where are the retained primary-outcome MI and cluster/heterogeneous-variance sensitivity results,and what analysis decisions or outputs show whether those checks changed the reported BMI trajectory inference?

**Source confirmation:** Direct native text confirms each plan specification and the complete current report map supports the absence search;visual sourcep113 confirms retained MI and heterogeneous sensitivity wording.

### F-ST1-004

**Title:** The claimed prespecified binary Poisson models are not specified in the supplied plan.

**Relationships:** S094,S095. **Compared locations and roles:** REPORT [main Statistical Methods p4](../../../jama_barkin_2018_oi_180075.pdf#page=4);REPORT [Table2 community-center footnotec p8](../../../jama_barkin_2018_oi_180075.pdf#page=8);REPORT [Table3 footnoteb p9](../../../jama_barkin_2018_oi_180075.pdf#page=9). PLAN [revised seven-secondary-outcome list p67](../../../joi180075supp1_prod.pdf#page=67),[original secondary analyses pp45-47](../../../joi180075supp1_prod.pdf#page=45),[revised secondary analyses pp98-100](../../../joi180075supp1_prod.pdf#page=98),[final SAP pp110-113](../../../joi180075supp1_prod.pdf#page=110),with complete PLANpp1-113 checked for other Poisson specifications. Primary relationship P_R;all relationships P_R.

**Printed statements:** Mainp4 describes OLS for continuous and Poisson with robust standard errors for binary outcomes,followed by 'Models were prespecified.' Table2 reports the Poisson center-use RR adjusting baseline use;Table3 reports the Poisson obesity RR adjusting baselineBMI,age,sex. Revisedplanp67 lists center use never/atleastonce among seven a priori secondary outcomes. The supplied plan analysis sections specify logistic regression for acceptableBMItrajectory/USDAadherence binary outcomes,and continuous multiple regression for sedentary activity;the finalSAP covers the primary BMI model. No Poisson/robust binary endpoint specification is present anywhere in the supplied plan.

**Rule and reproduced comparison:** A reported analysis characterized as prespecified must be distinguishable in the supplied prespecification material. The center-use endpoint is prespecified,but its reported Poisson robust model is absent;endpointprespecification does not itself specify the analysis model. No claim that the plan's binary USDAadherence/acceptabletrajectory outcome is identical to pointobesity or centeruse is made. The continuous OLS/multiple-regression family does not yield this finding. Text comparison,not numerical arithmetic;rounding not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The prespecified-analysis status and model provenance of center-useRRs1.47,1.21,1.29 and binary obesityRRs,particularly the abstract's36-month center-useRR1.29.

**Why context does not resolve it:** Category5 retains an analysis described as prespecified that the supplied plan does not contain. The supplied plan confirms the center-use outcome but not this statistical model;the final primary-analysis amendments do not document a binary Poisson analysis.

**Source-grounded alternatives and missing definition:** A separate prospective secondary-model specification may exist outside the supplied package;or 'Models were prespecified' may refer only to selected covariates/families rather than every model described in the preceding sentence. The post-hoc obesityoutcome may have had a model fixed before later outcome selection. The package supplies no such model-specification document or scope clarification. These alternatives do not contradict the observation about the supplied plan.

**Exact human question:** Which prospective specification establishes the Poisson robust center-use and obesity models,and does 'Models were prespecified' apply to those binary models or to a narrower set of analysis elements?

**Source confirmation:** Mainp4 visually confirmed;direct layouts of plan secondary sections/finalSAP and the complete source-matched plan searched for Poisson specification. No source transcription normalization used.

### F-ST1-005

**Title:** Original anthropometric outcome statuses differ from those retained in the reported analysis.

**Relationships:** S096,S103. **Compared locations and roles:** PLAN [original protocol p16,Table2PrimaryOutcomes/Table3SecondaryOutcomes](../../../joi180075supp1_prod.pdf#page=16);PLAN [revised outcomes p67](../../../joi180075supp1_prod.pdf#page=67);PLAN [original parentBMI-change analysis p45](../../../joi180075supp1_prod.pdf#page=45),[revised p98](../../../joi180075supp1_prod.pdf#page=98);REPORT [main Outcomes p3](../../../jama_barkin_2018_oi_180075.pdf#page=3). Primary relationship P_R;all relationships P_R,P_P because the original/revised plan also states different hierarchies.

**Printed statements:** Original Table2 lists childBMItrajectory,bodyfat%(tricepsskinfold),andwaistcircumference under 'Primary Outcomes';original Table3 lists parentBMI,bodyfat%,andwaist under 'Secondary Outcomes.' Revisedp67 specifies BMIprimary plus seven diet/activity/center-use secondary outcomes before nonbaseline arm-unblinding. Mainp3 identifies childBMItrajectory as primary and those same seven secondary outcomes,and says parentanthropometrics and childwaist/triceps were collected but 'not included as secondary outcomes in this analysis.' Originalp45/revisedp98 retain modeling parentBMIchange over time as a predictor of childBMItrajectory;reporting baselineparentBMI as a moderator does not supply that longitudinalchange analysis.

**Rule and reproduced comparison:** A prespecified outcome whose primary/secondary status changes belongs to routeA5. Childwaist/skinfold are explicitly originalprimary;parentanthropometrics explicitly originalsecondary;the current analysis does not retain them in those statuses. The seven-endpoint list documents a revised hierarchy,which is part of the comparison,not evidence that the original statuses never existed. No numeric display discrepancy is asserted;rounding not applicable. The repeated hierarchy pattern is one finding rather than one finding per instrument.

**Focus area:** D. **Proposed review domain:** protocol_report.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Which endpoints comprise the prespecified primary/secondary anthropometric result set and whether the reported BMI-only primary conclusion represents the original or revised outcome hierarchy.

**Why context does not resolve it:** RouteA category 5 retains documented outcome-status changes. The report explains what is excluded from this analysis,but the supplied original plan still assigns the instruments primary/secondary status. Reader extraction of prespecified endpoint status can therefore differ by version.

**Source-grounded alternatives and missing definition:** Revisedp67 documents a before-unblinding seven-secondary list,and the report clearly discloses that the other anthropometrics are outside this analysis;the hierarchy may have been formally narrowed and the other planned analyses reserved for anotherpublication. No claim is made that an amendment was improper or that unreported analyses were not conducted. A dated endpoint-status change/remapping and location of any separate results remain useful context for human adjudication.

**Exact human question:** Which dated outcome-hierarchy specification supersedes the original primary childwaist/skinfold and secondary parentanthropometric designations,and where should the corresponding planned anthropometric results be located for package extraction?

**Source confirmation:** Direct source-native p16/p67/p45/p98/mainp3 text confirms labels and exclusions;source maps maintain version identities.

## Excluded observations

Only apparent issues not emitted are listed;routine successful checks remain in the S inventory. Exactly one normative reason code per observation. Eight observations.

| Location | Observation | Reason code |
|---|---|---|
| REPORT mainp7 Figure3caption,versusmainp4model,S080 | Caption says failed to reject a null that terms were jointly 'different' rather than equal tozero;methods,reportedP.39 andcurveclarify the intended null atonce without changing a printednumber | TERMINOLOGY_OR_WORDING |
| REPORT mainp9 discussion,S080 | 'No meaningful difference' has no explicit equivalence/clinicalmargin;no formal equivalence test or conflicting margin/interval is printed | CONDITIONAL_OR_UNREPORTED |
| REPORT supplementp3 baselineenergy moderator,S048-S049 | Energy covariate centering/scaling notspecified beyond calories;large coefficient alone doesnot reproduce a contradiction without an assumedscale | CONDITIONAL_OR_UNREPORTED |
| PLANpp42-43/95-96 andREPORT mainp4,S085 | Treating .4 as cross-sectional Cohen d gives another sample-size formula,whereas suppliedplan explicitly defines polynomial randomtrend standardization;missingODdefaults prevent independent numerical reproduction | CONDITIONAL_OR_UNREPORTED |
| PLANpp41-42/95,S090 | No constrained-MI thresholds,reweighted-MI or pattern-mixture output;source explicitly makes these optional or conditional on observed missingness patterns | CONDITIONAL_OR_UNREPORTED |
| REPORT mainpp6/10,supplementp4footnotea,S099 | Categorical subgroup effect P values are not numeric between-category interactiontests;footnote states within-categoryeffects,while exact joint moderator test/covariance is absent and no conflicting interactionP isprinted | CONDITIONAL_OR_UNREPORTED |
| PLANpp45/98,S104 | Reboundformula uses original coefficientnotation after finalmodelnotation changed;this secondary auxiliary calculation has no reported primary/keysecondary output relying on it | PERIPHERAL_COMPARISON |
| PLANpp48/101,S104 | Genetics aimregresses a baselineoutcome on GRS×time;this auxiliary plan-internal specification is not a reported primary/keysecondary result or primarydecisionrule | PERIPHERAL_COMPARISON |

## Completion and limits

Every S001-S105 record is PASS_1_COMPLETE. Five findings emitted after independent source-based self-screening;the initial inclusion screener must decide all five. F-ST1-003 through005 may overlap current cross-source checker findings and should be consolidated by issue while preserving allsource locations. No fixed number was sought. Point/interval/P checks cover all73 printed inferential rows;BH calculations cover every secondary,obesity andBMI time-point family;all38 moderator rows retained. Exact model-variance/test-output or ODsoftware reconstruction is limited by named absentinputs. No preferred analysis,clinicalcritique,raw-data audit or externalresearch was introduced. A different freshhigh agent mustperform pass2 using the completeledger,screening andmechanicalrecheck.

## Explicit pass-1 relationship coverage

Every relationship below is documented PASS_1_COMPLETE in the canonical inventory and included in this completed first pass:

S001,S002,S003,S004,S005,S006,S007,S008,S009,S010,S011,S012,S013,S014,S015,S016,S017,S018,S019,S020,S021,S022,S023,S024,S025,S026,S027,S028,S029,S030,S031,S032,S033,S034,S035,S036,S037,S038,S039,S040,S041,S042,S043,S044,S045,S046,S047,S048,S049,S050,S051,S052,S053,S054,S055,S056,S057,S058,S059,S060,S061,S062,S063,S064,S065,S066,S067,S068,S069,S070,S071,S072,S073,S074,S075,S076,S077,S078,S079,S080,S081,S082,S083,S084,S085,S086,S087,S088,S089,S090,S091,S092,S093,S094,S095,S096,S097,S098,S099,S100,S101,S102,S103,S104,S105
