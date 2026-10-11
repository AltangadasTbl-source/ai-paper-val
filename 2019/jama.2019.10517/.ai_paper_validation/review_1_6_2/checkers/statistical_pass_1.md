# Statistical consistency pass 1 — Workflow 1.6.2

Fresh agent: `/root/statistics_pass_one`; gpt-6.1-sol/high; FRESH_SPAWN. Exact scope: all70 statistical relationships, S001–S066 and S081–S084, plus linked Table5/count/effect-identity relationships. The complete source-linked inventory is [relationship_inventory.md](../statistics/relationship_inventory.md). Scientific coverage gaps: none. No earlier candidate/checker/report conclusions or external material were read.

All reported main estimates are inside their ordered intervals. All printed null-exclusion/significance decisions reconcile, including Holm-adjusted secondary P values. No interval-versus-P/test conflict was screened out. No noninferiority, equivalence or formal efficacy-stopping boundary is supplied; primary inference is superiority. Model structures use individual randomization, repeated-participant mixed effects and specified covariates coherently. Named unavailable inputs limit exact recreation but do not limit coverage.

Direct engine: Poppler pdftotext on CPU; new raw derivatives in `preprocessing/statistics_pass_one/`. The current direct main/protocol layout and exact supplied source locations are authority; source-matched page images checked all nine supplementary plots and protocol p21 glyphs. Diagnostic approximations in the inventory are explicitly distinguished from reported fitted-model analyses. Documents: main article/results supplement are REPORT; protocol bundle is PLAN.

## Findings

### F-ST1-001

**Issue:** Primary relapse composite is printed more broadly in the report than in the supplied plan.

**Locations and roles:** PLAN [protocol PDF p.12](../../../joi190079supp1_prod.pdf#page=12), section3.9.8, lines553–573; REPORT [main PDF p.4](../../../jama_flint_2019_oi_190079.pdf#page=4), Primary Outcome:Relapse; REPORT [main PDF p.7](../../../jama_flint_2019_oi_190079.pdf#page=7), Table3/primary result. Related S IDs:S049,S040,S001,S035.

**Printed statements:** Plan HAM-D≥18 also requires an absolute increase of5points relative to RCT entry on at least one visit. Re-emerging SCID psychosis also requires SADS delusion/hallucination severity≥3. Psychiatric hospitalization is specifically for depression, psychosis, suicidality, or mania/hypomania. Main formal relapse definition lists HDRS≥18, SCID-rated psychosis, or hospitalization in a psychiatric unit without these additional qualifiers. Table3's hospitalization footnote does retain the specified causes.

**Rule and calculation:** Compare prespecified primary-composite conjunctions with reported decision criteria. The printed report removes the additional5-point/SADS≥3 conditions and prints an unqualified hospitalization component. These are differences in the formal endpoint rule, not differences of numeric rounding. For illustration of the rule only, an RCT-entry HDRS15 and later HDRS18 meets the printed report threshold but lacks the plan's5-point increase. This illustration is not an observed participant.

**Focus area:**D. **Proposed review domain:**protocol_report. **Proposed relationship type:**P_R. **All relationships:**P_R.

**Qualifying route:**Route A, category5.

**Affected result or extracted value:**Primary relapse classification underlying13/64 versus34/62 and the adjusted HR .25 [.13,.48].

**Why context does not resolve it:**RouteA5 specifically covers changed primary composites. Table3 narrows hospitalization but does not identify which threshold conjunction was used for all relapse events; the supplied package gives no explicit endpoint amendment.

**Alternatives and missing definition:**The report may abbreviate unchanged operational rules, or the study may have used an amended relapse rule. The plan's preferable one-week duration explicitly allows safety exceptions and is not treated as an absolute rule conflict.

**Human question:**Which operational relapse criteria generated the reported47relapses, and were the5-point increase, SADS≥3 and specified hospitalization-cause conditions retained or amended?

### F-ST1-002

**Issue:**The plan's primary glycemic measure is absent from the supplied main-secondary glycemic results.

**Locations and roles:**PLAN [protocol PDF p.10](../../../joi190079supp1_prod.pdf#page=10), Metabolic Measures, lines484–488, and [p.14](../../../joi190079supp1_prod.pdf#page=14), exploratory model specification; REPORT [main PDF p.1](../../../jama_flint_2019_oi_190079.pdf#page=1), Main Outcomes/Results; [main PDF pp.4,7-8](../../../jama_flint_2019_oi_190079.pdf#page=7), Secondary Outcomes/Table4; REPORT [supplement2 pp.8-9](../../../joi190079supp2_prod.pdf#page=8), eFigures7–8. Related S IDs:S047,S014,S015,S064,S065.

**Printed statements:**Plan says HOMA insulin resistance is the primary glycemic-function measure and HbA1c a secondary glycemic measure; HOMA is calculated whenever fasting glucose and insulin are measured. Main abstract calls serum glucose/HbA1c main secondary outcomes and presents those estimates, while the complete supplied results display contains no HOMA or insulin result.

**Rule and calculation:**Compare the prespecified glycemic outcome hierarchy and reported outcome set. HOMA is a derived insulin-resistance quantity requiring insulin and glucose; a fasting-glucose estimate or HbA1c estimate does not by itself constitute a HOMA estimate. No HOMA formula is imported from external material. Display precision is not applicable to different outcomes.

**Focus area:**D. **Proposed review domain:**protocol_report. **Proposed relationship type:**P_R. **All relationships:**P_R.

**Qualifying route:**Route A, category5.

**Affected result or extracted value:**The primary glycemic-safety outcome a reader should extract, and the meaning of the reported nonsignificant glucose/HbA1c trajectories.

**Why context does not resolve it:**RouteA5 covers outcome-status changes and prespecified key-outcome nonreporting. The report identifies glycemic outcomes but does not account for the plan's primary glycemic measure or identify an amendment.

**Alternatives and missing definition:**HOMA may have been reported separately, not estimable, or removed by amendment; none of these is established in the supplied evidence. HbA1c's evident mg/dL unit-label slip is separately excluded and is not this finding.

**Human question:**What happened to the prespecified primary glycemic measure HOMA, and which amended hierarchy or result should accompany the reported glucose/HbA1c outcomes?

### F-ST1-003

**Issue:**The supplied package does not present the prespecified secondary H3 age/weight hypothesis.

**Locations and roles:**PLAN [protocol PDF p.3](../../../joi190079supp1_prod.pdf#page=3), Secondary Aims/H3, lines122–129; [protocol PDF p.14](../../../joi190079supp1_prod.pdf#page=14), H3 analysis, lines680–686; [p.16](../../../joi190079supp1_prod.pdf#page=16), H3 power; REPORT [main PDF p.2](../../../jama_flint_2019_oi_190079.pdf#page=2), Methods scope paragraph. Related S IDs:S042,S053,S056.

**Printed statements:**H3, explicitly a secondary hypothesis, states that older age is associated with less weight gain during the open-label phase, tested with age×time mixed-effects analysis from acute baseline. Main states that onlyAims1–2 are reported and that age/weight and metabolic associations are not presented. All supplied result pages were mapped; no H3 estimate/test is present.

**Rule and calculation:**Compare explicitly prespecified secondary hypothesis with supplied reported analyses. H3 is unreported in this package; it cannot be substituted with the primary Cox age HR .78 or an exploratory randomized-phase age moderator. Display precision does not apply to an absent specified outcome analysis.

**Focus area:**D. **Proposed review domain:**protocol_report. **Proposed relationship type:**P_R. **All relationships:**P_R.

**Qualifying route:**Route A, category5.

**Affected result or extracted value:**Age-specific open-label weight-gain evidence under the trial's prespecified secondary hypothesis.

**Why context does not resolve it:**The omission is expressly disclosed, but routeA5 requires registration of prespecified key-secondary analyses not reported; disclosure is recorded as context rather than an exclusion.

**Alternatives and missing definition:**H3 may be in a separate article beyond the supplied package. No assertion is made that it was not analyzed, or that it changed the randomized relapse conclusion. Exploratory genetic/age aims are distinct and excluded.

**Human question:**Where is the prespecified H3 age×time secondary result, and should it be linked to complete the supplied trial outcome record?

### F-ST1-004

**Issue:**Prespecified exclusion of subsequent metabolic data after a lipid-treatment change is reported as a post hoc sensitivity analysis.

**Locations and roles:**PLAN [protocol PDF p.14](../../../joi190079supp1_prod.pdf#page=14), H2, lines673–679; REPORT [main PDF p.5](../../../jama_flint_2019_oi_190079.pdf#page=5), statistical sensitivity paragraph, and [p.7](../../../jama_flint_2019_oi_190079.pdf#page=7), Secondary Outcomes drug-change paragraph. Related S IDs:S052,S036,S038; numeric N070.

**Printed statements:**Plan:after new/changed hyperlipidemia treatment, pertinent later metabolic values will be excluded from the mixed model; data still collected for DSMB. Report:post hoc sensitivity analyses exclude pertinent observations after statin/hypoglycemic start/change, while primary metabolic analyses include all participants;12participants had statins started/changed (6perarm), with sensitivity results qualitatively similar.

**Rule and calculation:**The lipid-data exclusion is specified as part of planned H2 fitting, whereas report places it in an additional post hoc sensitivity analysis. This is a difference in which observation set produces the headline weight/metabolic models and in prespecification status. The additional glucose-drug rule has no matching prospective rule in this cited plan paragraph and is not treated as though it did.

**Focus area:**D. **Proposed review domain:**protocol_report. **Proposed relationship type:**P_R. **All relationships:**P_R.

**Qualifying route:**Route B.

**Affected result or extracted value:**Headline total-cholesterol/triglyceride treatment×time estimates, especially .29 [.13,.45] and −.153 [−.306,.004], and their main-analysis versus sensitivity-analysis status.

**Why context does not resolve it:**B1:planned/reported missing-data and observation-selection specification. B2:the report does not explain the change from mandatory H2 exclusion to post hoc sensitivity. B3:the number/identity of observations used in the extracted headline lipid estimate can differ; qualitative similarity does not establish identical numeric estimates.

**Alternatives and missing definition:**An amendment may have deliberately retained all pertinent observations for the primary model. The report may use 'all participants' while already censoring some measurements; if so, exact model-specific observation sets and the meaning of the sensitivity statement are needed.

**Human question:**Were observations after lipid-treatment starts/changes excluded in the headline H2 models or only in sensitivity models, and what explains their reported post hoc status despite the supplied plan?

### F-ST1-005

**Issue:**The safety-analysis group definition does not reconcile between the plan's medications-taken classification and the report's randomized-group presentation.

**Locations and roles:**PLAN [protocol PDF p.14](../../../joi190079supp1_prod.pdf#page=14), lines666–667, and [p.16](../../../joi190079supp1_prod.pdf#page=16), lines766–772; REPORT [main PDF p.4](../../../jama_flint_2019_oi_190079.pdf#page=4), Statistical Analyses; [main PDF p.7](../../../jama_flint_2019_oi_190079.pdf#page=7), Secondary Outcomes; [main PDF p.8](../../../jama_flint_2019_oi_190079.pdf#page=8), Table4; REPORT [supplement2 PDF pp.2-9](../../../joi190079supp2_prod.pdf#page=2), randomized-group plot titles. Related S IDs:S052,S057,S036,S058–S065; numeric N010–N013.

**Printed statements:**Plan safety hypotheses H2/H3 and exploratory E1/E2 use classification based on medications taken during protocolized treatment. Main says analyses include all randomized participants, specifies treatment-group mixed effects and describes comparisons in randomized groups; Table4 uses randomized arm n64/n62, and all supplementary metabolic plots are explicitly titled randomized groups. Main Figure1 identifies seven participants who did not receive treatment as randomized, and primary post hoc sensitivity excludes seven medication discontinuers retained for research.

**Rule and calculation:**Treatment assignment and medications actually taken are different group definitions where nonadherence/crossover occurs. Seven randomized participants' medication discontinuation is explicitly reported; the report does not specify how medications-taken safety classification maps to its randomized-group estimates. This is not a comparison of an adjusted effect with a crude ratio.

**Focus area:**D. **Proposed review domain:**protocol_report. **Proposed relationship type:**P_R. **All relationships:**P_R.

**Qualifying route:**Route B.

**Affected result or extracted value:**The analysis population/contrast assigned to the eight headline anthropometric/metabolic effects and their reported model trajectories.

**Why context does not resolve it:**B1:prespecified/reported analysis-population classification. B2:no safety reclassification or observation-censoring mapping is provided to reconcile the two definitions. B3:classification of nonadherent participants affects which treatment contrast a data extractor records.

**Alternatives and missing definition:**All randomized subjects can in principle be included yet reclassified by exposure, or reported arm labels may denote baseline assignment while safety estimates are otherwise exposure-classified. The current text does not establish such a mapping. The seven identified Figure1 deviations are not assumed to be exactly the same persons in the post hoc exclusion without individual identities.

**Human question:**Do the reported safety models classify participants by randomized allocation or medications taken, and how are nonadherence/crossover periods handled relative to the prespecified regulatory safety approach?

### F-ST1-006

**Issue:**Prespecified randomized weight and missingness-sensitivity analyses are not reported in the supplied package.

**Locations and roles:**PLAN [protocol PDF p.10](../../../joi190079supp1_prod.pdf#page=10), Anthropometric Measures, lines473–483; PLAN [protocol PDF p.16](../../../joi190079supp1_prod.pdf#page=16), Strategies for Attrition, lines769–772; REPORT [main PDF pp.4-5](../../../jama_flint_2019_oi_190079.pdf#page=5), mixed-model/missingness specification; [main PDF p.7](../../../jama_flint_2019_oi_190079.pdf#page=7), secondary analysis results; [main PDF p.8](../../../jama_flint_2019_oi_190079.pdf#page=8), Table4; REPORT [supplement2 PDF pp.1-10](../../../joi190079supp2_prod.pdf#page=1), complete result plot supplement. Related S IDs:S047,S057,S036,S037,S048.

**Printed statements:**Plan specifies separate BMI models as an alternative to weight forAims2–5, secondary weight analysis accounting for depression-related loss derived from premorbid weight, and treatment-effect comparisons with models including Intent-to-Attend at entry to address attrition. Report's complete randomized weight result provides the weight model/waist alternative; the supplied package contains no BMI model, no premorbid-weight-adjusted weight result, and no Intent-to-Attend model comparison. Premorbid weight is used in the separate adverse-event threshold definition, which does not supply the planned secondary weight model.

**Rule and calculation:**Compare explicit planned secondary/attrition sensitivity analyses attached to the abstract's key secondary weight and metabolic results with the complete supplied output. The planned analyses have no reported counterpart; waist circumference does not stand in for BMI, an adverse-event threshold does not stand in for a weight-change adjustment, and a dropout-pattern mixture is distinct from an Intent-to-Attend covariate comparison. Display precision is not applicable. Consolidated as one nonreporting pattern with all affected planned analysis locations.

**Focus area:**D. **Proposed review domain:**protocol_report. **Proposed relationship type:**P_R. **All relationships:**P_R.

**Qualifying route:**Route A, category5.

**Affected result or extracted value:**Secondary weight treatment×time effect .13 [.11,.15], its prespecified alternative/adjusted effect and missingness sensitivity of the anthropometric/metabolic treatment estimates.

**Why context does not resolve it:**RouteA5 covers planned primary/key-secondary analyses not reported. These analyses were expressly planned for outcomes actually reported as main secondary results; no supplied result or amendment identifies their status.

**Alternatives and missing definition:**They may be separately reported, omitted after amendment, or performed without printed output. Only absence from the supplied report record is observed; no assertion of nonperformance is made. Exploratory portions ofAims4–5 are not independently registered.

**Human question:**Where are the prespecified BMI, depression-related-weight-loss adjustment, and Intent-to-Attend treatment-effect comparisons, or what amendment explains their omission from the supplied randomized secondary-result record?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| Main pp.1,7; Table4 p.8; supplement2 p.9 | HbA1c daily effect carries mg/dL label, while outcome and5.9-level source scale unambiguously identify percentage; no numeric rescaling is printed. | NOTATION_OR_TYPOGRAPHY |
| Main pp.7-8 Table4, all16within-arm changes | Differences from subtraction of the two displayed marginal summaries; explicit missingness footnote and separate within-group estimand explain why these are not paired-data calculations. | CONTEXT_RESOLVES |
| Main p.7 NNT2.8/HR .25 versus crude event risks | HR-based NNT is not the crude inverse risk difference; missing survival/time mapping is named. Crude2.89635 versus printed2.8 also leaves only1.66%gap after display intervals. | MODEL_VERSUS_CRUDE |
| Main pp.1,7 primary HR versus13/64 and34/62 | Adjusted Cox HR .25 is not crude risk ratio .3704; censoring and covariates are explicit. | MODEL_VERSUS_CRUDE |
| Main p.7 secondary P values versus normal diagnostics from95%CIs | Exact unadjusted secondary test, degrees of freedom and multiplicity family are not printed; all null-exclusion/significance directions agree. No unadjusted-CI normal approximation can establish incompatibility of Holm-adjusted P values. | CONDITIONAL_OR_UNREPORTED |
| Main p.9 Table5 cholesterol CIs | An ordinary Wald diagnostic gives about−6.87to15.64 rather than−8to17.2; its construction is unprinted and it does not reproduce the other rows, whose sparse-event CIs are expressly exact. | CONDITIONAL_OR_UNREPORTED |
| Main p.4; protocol pp.15-16 | Exact survival/repeated-measure simulation recreation lacks event/censor generators, number of simulations, observation times, slope variance and covariance structure; diagnostic approximations and table thresholds do not show a printed conflict. | CONDITIONAL_OR_UNREPORTED |
| Protocol p.10 covariate overview versusp.14 detailed Cox selection; main p.4 | Overview refers to the analytic section, which supplies explicit conditions for five extra predictors. No printed data establish a triggered condition. | CONTEXT_RESOLVES |
| Protocol p.21; main p.2 | Locator text lost underlined equality bars in HAM-D/DAS thresholds; exact image reads≥21and≥2and matches report. | NOT_REPRODUCED |
| Main p.2 versus protocol exploratory genetic/age/PK aims | Exploratory results beyond current article's expressly limitedAims1–2; no primary/key-secondary analysis is substituted by these aims. | PERIPHERAL_COMPARISON |
| Supplement2 pp.2-10 | Shaded bands have no caption-defined level/type, exact coordinates or covariance; no conflicting printed band meaning or test is supplied. | CONDITIONAL_OR_UNREPORTED |
| Main p.7 SAS .022points/week; supplement2 p.10; main pp.4-5 Poisson model | Curve-based log-ratio diagnostic is suggestive, but source supplies neither link nor back-transformation nor exact marginal contrast. It cannot establish a raw-points versus link-scale inconsistency from convention alone. | CONDITIONAL_OR_UNREPORTED |
| Protocol p.40 EPSE benztropine; main pp.4-5,7 | No benztropine use/adjustment output is printed; this non-key safety model detail alone supplies no conflicting coefficient or triggered covariate statement. | CONDITIONAL_OR_UNREPORTED |
| Protocol p.41 versus main pp.4,6 | Descriptive dose-change outputs unprinted; no actual increase, prohibited dose or fixed-dose result is supplied. | CONDITIONAL_OR_UNREPORTED |
| Protocol pp.13-14 versus main p.4 PH diagnostics | Different stated proportional-hazards diagnostic procedures do not establish conflicting model assumptions or a numeric result; no diagnostic statistic conflicts. | CONDITIONAL_OR_UNREPORTED |

Excluded-observation count:15. Findings count:6. No reconciled routine check is classified as an excluded observation. The two post hoc versus planned observation-selection and treatment-classification findings use routeB; concrete omissions/composite differences use routeA5. All findings require independent inclusion screening before candidate assignment; no C IDs or dispositions were assigned.

## Explicit pass completion

| S ID | Status | Check record |
|---|---|---|
| S001 | PASS_1_COMPLETE | Contains .25; positive ordered limits; excludes1 and significant; lower O risk agrees. Diagnostic log-Wald P≈.000032; not an exact test reproduction. |
| S002 | PASS_1_COMPLETE | Contains .78; includes1; nonsignificant. Diagnostic log-Wald P≈.434. |
| S003 | PASS_1_COMPLETE | Contains2.45; includes1; nonsignificant. Diagnostic P≈.055. No report establishes the reverse reference group. |
| S004 | PASS_1_COMPLETE | Ordered and contained; includes1; diagnostic P≈.355. |
| S005 | PASS_1_COMPLETE | Ordered and contained; includes1; diagnostic P≈.868; exact variance/test unprinted. |
| S006 | PASS_1_COMPLETE | Ordered and contained; includes1; diagnostic P≈.151. |
| S007 | PASS_1_COMPLETE | Ordered and contained; excludes1; diagnostic P≈.000013; post hoc set explicitly distinguished from primary126. |
| S008 | PASS_1_COMPLETE | Ordered, contained, excludes0 and significant. Linear interaction is distinct from full quadratic trajectory and within-arm change. |
| S009 | PASS_1_COMPLETE | Ordered, contained, excludes0 and significant; Holm adjustment stated. |
| S010 | PASS_1_COMPLETE | Ordered, contained, excludes0 and significant; higher O daily interaction agrees with figure early trajectories. |
| S011 | PASS_1_COMPLETE | Ordered, contained, includes0 and nonsignificant; Holm-adjusted P need not equal unadjusted-CI Wald diagnostic. |
| S012 | PASS_1_COMPLETE | Ordered, contained, includes0; nonsignificant; no null conflict. |
| S013 | PASS_1_COMPLETE | Ordered, contained, includes0; nonsignificant; pattern-mixture averaging stated. No variance or averaging weights supplied. |
| S014 | PASS_1_COMPLETE | Ordered, contained, includes0; nonsignificant. Quadratic-time model precludes endpoint secant replacement. |
| S015 | PASS_1_COMPLETE | Ordered and contained; includes0 and nonsignificant. % scale unambiguously supplied by Table4 and eFigure8; unit label observation excluded. |
| S016 | PASS_1_COMPLETE | Ordered, contained, excludes0 and significant. Increasing O/decreasing P direction agrees; exact link-scale/back-transformation and marginal contrast not supplied. |
| S017 | PASS_1_COMPLETE | Ordered, contained; positive change agrees with weight-gain discussion. Footnote explicitly distinguishes paired change from two displayed marginal means. |
| S018 | PASS_1_COMPLETE | Ordered, contained; negative change agrees with discussion; no P printed. |
| S019 | PASS_1_COMPLETE | Ordered, contained; positive change; no P printed; paired observations unavailable. |
| S020 | PASS_1_COMPLETE | Ordered, contained; negative change; no P printed. |
| S021 | PASS_1_COMPLETE | Ordered, contained; includes0; descriptive decline agrees with narrative, which does not claim significant within-arm decline. |
| S022 | PASS_1_COMPLETE | Ordered, contained; decline agrees with narrative; no P printed. |
| S023 | PASS_1_COMPLETE | Ordered, contained; includes0; missingness footnote prevents marginal-mean subtraction substitution. |
| S024 | PASS_1_COMPLETE | Ordered, contained; within-arm result is not the between-arm linear interaction S011. |
| S025 | PASS_1_COMPLETE | Ordered, contained; no P printed; within-arm change differs from between-arm S012 estimand. |
| S026 | PASS_1_COMPLETE | Ordered, contained; negative change; no P printed. |
| S027 | PASS_1_COMPLETE | Ordered, contained; includes0; printed mean subtraction not a paired-data reconstruction. |
| S028 | PASS_1_COMPLETE | Ordered, contained; includes0; rounded identical marginal means do not determine paired change. |
| S029 | PASS_1_COMPLETE | Ordered, contained; includes0; difference of medians not substituted for median change. |
| S030 | PASS_1_COMPLETE | Ordered, contained; negative change; no P printed; exact paired values unavailable. |
| S031 | PASS_1_COMPLETE | Ordered, contained; includes0; no P printed. |
| S032 | PASS_1_COMPLETE | Ordered, contained; includes0; no P printed. |
| S033 | PASS_1_COMPLETE | Direction agrees with Cox and count results; risk sets decrease and terminal counts agree with flow. Event/censor timings unavailable for exact log-rank recreation. |
| S034 | PASS_1_COMPLETE | 20-point difference gives NNT5. Plan table power .82 at15%attrition is compatible with at-least80% summary. Revision disclosed; no new generator or revised power assumptions supplied. |
| S035 | PASS_1_COMPLETE | Specified individual-randomized Cox model structurally coherent; actual diagnostics supplied by description. Conditional additional covariates are not proven triggered; Different diagnostic procedures supply no conflicting statistic; prespecified key-secondary sensitivities are tracked in F-ST1-006. |
| S036 | PASS_1_COMPLETE | Repeated-subject structure explicitly modeled. No extrapolation of .13 daily coefficient into36-week linear change. Planned safety classification comparison F-ST1-005; planned analyses F-ST1-006. |
| S037 | PASS_1_COMPLETE | Stated mixed structures coherent; pattern averaging limited to triglycerides. Exact link/back-transform unavailable, no convention imposed. Intent-to-Attend comparison F-ST1-006. |
| S038 | PASS_1_COMPLETE | Holm explains larger adjusted P without any significance conflict. Planned lipid censoring F-ST1-004. Table5 four intervals ordered and contain estimates/null; no significant difference claim agrees. |
| S039 | PASS_1_COMPLETE | Dimensions and time units preserved. HbA1c unit slip excluded because Table4/eFigure8 identify % without a numeric rescaling conflict. |
| S040 | PASS_1_COMPLETE | Direction, duration, contrasts and null agree with reported primary conclusion; no noninferiority/equivalence margin or claim. |
| S041 | PASS_1_COMPLETE | All three H2 variables reported, triglyceride nonsignificant. Post hoc multiplicity/exploratory interpretation openly disclosed; no prespecified label assigned to an absent plan analysis. |
| S042 | PASS_1_COMPLETE | Prespecified secondary hypothesis explicitly not presented in supplied report; F-ST1-003. |
| S043 | PASS_1_COMPLETE | Report expressly limits scope toAims1-2; exploratory analysis omission alone is excluded, unlike secondary H3. |
| S044 | PASS_1_COMPLETE | Visual source p21 confirms ≥ glyphs and agreement with report. Plan MMSE exceptions and extra stabilization visits are permissions; no observed exception or extension supplied. |
| S045 | PASS_1_COMPLETE | Same stratification variables, same ratio; current sample revision disclosed. No cluster/paired sample structure contradicted. |
| S046 | PASS_1_COMPLETE | Detailed plan p14 conditions inclusion on imbalance and relapse correlation. No printed result demonstrates those conditions; overview is read with its referenced analytic section. |
| S047 | PASS_1_COMPLETE | HOMA not reported and main secondary glycemic display uses glucose/HbA1c: F-ST1-002. BMI/premorbid adjustment not reported: F-ST1-006. |
| S048 | PASS_1_COMPLETE | Main in-person schedule matches research visit timing; omission of phone-contact detail does not prove contact stopped. No endpoint denominator changed by a stated conflict. |
| S049 | PASS_1_COMPLETE | Plan adds ≥5HAM-D increase, SADS≥3 psychosis confirmation, specified hospitalization causes; main criteria broaden printed definition: F-ST1-001. Preferable duration is not absolute. |
| S050 | PASS_1_COMPLETE | Primary ITT and sidedness/alpha agree. Report Holm post hoc openly disclosed. No actual baseline test/triggered adjustment supplied; no preferred test imposed. |
| S051 | PASS_1_COMPLETE | Core Cox covariates/censoring structure agrees. Prior-week HAM-D dropout and time-period interaction diagnostic details are not printed; no contradictory diagnostic statistic is supplied. |
| S052 | PASS_1_COMPLETE | F-ST1-005 classification; F-ST1-004 main/sensitivity exclusion. Choice of random structures internally coherent; spline absence alone is not a conflicting numeric method result. |
| S053 | PASS_1_COMPLETE | H3 nonreporting F-ST1-003; E1 omission excluded as exploratory. |
| S054 | PASS_1_COMPLETE | No supplied genetic result conflicts with stated specification. Exploratory aims expressly outside current article; no clinical efficacy inference from ancestry/QC figures. |
| S055 | PASS_1_COMPLETE | No drug-exposure estimate/test supplied or contradictory primary analysis dependency; exploratory omission does not become an unperformed-analysis claim. |
| S056 | PASS_1_COMPLETE | All six survival/table rows and six repeated-measure rows checked for internally ordered/sufficient power. Diagnostic fixed-time two-proportion powers approximate survival table; exact simulation generators and mixed covariance/slope variance unprinted. |
| S057 | PASS_1_COMPLETE | ITT and pattern-mixture described in report; Intent-to-Attend comparison absent F-ST1-006. Safety-classification instruction repeated F-ST1-005. |
| S058 | PASS_1_COMPLETE | Both curves within their shading; ordered axes; O rises/P falls net; crossing and curvature explain why linear coefficient is not endpoint average. Exact plotted values/band definitions unprinted. |
| S059 | PASS_1_COMPLETE | O increase/P decline agrees with positive interaction. Model curves not substituted for marginal raw Table4 means. |
| S060 | PASS_1_COMPLETE | Both net declines, greater P decline and early positive O−P interaction agree; no global linear extrapolation. |
| S061 | PASS_1_COMPLETE | Both decline, steeper P; small positive O−P slope agrees. Overlap of marginal bands does not determine between-arm P. |
| S062 | PASS_1_COMPLETE | Both decline, greater O fall agrees with negative interaction; no sign conflict or unprinted significant-group claim. |
| S063 | PASS_1_COMPLETE | All four treatment/dropout legends retained; means inside bands. Pattern weights/counts unprinted; cannot replace averaged interaction with one pattern slope. |
| S064 | PASS_1_COMPLETE | Early O decline and curvature compatible with negative linear coefficient; late O endpoint above P does not reverse a linear-time parameter. |
| S065 | PASS_1_COMPLETE | O declines faster; sign agrees; % scale confirms evident label interpretation. Means remain within shading. |
| S066 | PASS_1_COMPLETE | O rises/P falls; source figure has no numerical contrast or band definition. Link/back-transformation diagnostic cannot certify that .022 is a raw rather than link-scale contrast. |
| S081 | PASS_1_COMPLETE | No fixed numerical interim/stopping boundary printed and no inferential stopping claim reported; reduced sample explicitly approved. Conditional authority not invented into alpha-spending. |
| S082 | PASS_1_COMPLETE | No benztropine use count or triggered numerical comparison supplied; safety covariate detail alone outside primary/keysecondary routeA5, excluded with named absence. |
| S083 | PASS_1_COMPLETE | Same concomitant sertraline intervention; descriptive baseline median is not a dose-change result. Unprinted changes do not establish prohibited increase. |
| S084 | PASS_1_COMPLETE | Main target range/median and4-week switch consistent with flexible protocol; no fixed-dose analysis contradicted. Unprinted dosechanges alone do not establish altered intervention. |


Limitations: exact test/covariance/simulation and individual paired/survival data unprinted; plot coordinates/band definitions unprinted; these are named reconstruction limits, not scientific coverage gaps. All70 S IDs are PASS_1_COMPLETE. A different fresh statistical agent must perform pass2 with the ledger, screen and mechanical source recheck.
