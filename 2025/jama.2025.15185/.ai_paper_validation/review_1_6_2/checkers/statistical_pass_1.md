# Statistical consistency review — pass 1

Fresh agent `/root/statistics_pass_1`; gpt-6.1-sol/high; FRESH_SPAWN. The coordinator records the tool-return runtime ID. Exact scope: S001–S094, all94 current-run inferential/design relationships, including both endpoints grouped in S025, every row grouped in S056–S062, and every protocol clause grouped in S068–S094. Durable checks for every ID are in `statistics/relationship_inventory.md`, each marked PASS_1_COMPLETE. No candidate IDs or adjudications are assigned here.

Read completely: QUALITY_CONTROL_SCOPE.md, workflow1.6.2 review contract, current settings, AGENTS instructions and tooling/source inventories. Scientific input was limited to current fresh mappings and supplied sources. All earlier scientific findings, screening records, diagnostic arithmetic and reports were excluded. No web used. Current affirmative source statements cited below were checked using direct PDF-derived images; complete current report maps establish missing outputs. Each finding was independently self-screened against both inclusion routes; no count target was used.

The printed primary CI/P and all supplementary CI/test decisions reconcile. Primary−.90[−3.78,1.98],P=.54: contained,ordered,CI includes0,P>.05. Normal-CI reverse calculation gives SE1.4694,z−.6125 and approximatelyP.54; this is a **diagnostic approximation**, not the actual MI test. No pooled df or SE is printed. All secondary/sensitivity intervals contain their estimates, with no reversed endpoints; every printed null decision agrees with its CI. No superiority, NI, equivalence, multiplicity, efficacy-interim or stopping conclusion contradicts its stated numeric rule. Proposed domains and relationships below are review-routing fields only.

## Findings

### F-ST1-001

**Observation:** The protocol primary mixed model includes center and stroke type; the SAP and implemented primary linear model omit them.

**Relationships:** S003,S005,S009,S017,S044,S067,S072,S078,S083,S092. **Focus area:** D (also C). **Proposed review domain:** protocol_report. **Proposed primary relationship:** P_R. **All relationships:** P_R,P_P.

**Exact locations and roles:** PLAN [protocol PDFp86,§11.4.2](../../../joi250066supp1_prod_1761597796.4601.pdf#page=86), corroborated by PLAN [p56,statistical considerations](../../../joi250066supp1_prod_1761597796.4601.pdf#page=56); PLAN [SAPp10,§5.2](../../../joi250066supp2_prod_1761597796.4701.pdf#page=10); REPORT [mainp4,Statistical Analyses](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4), REPORT [mainp5,prespecification paragraph](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5), REPORT [analysis codep1,lines19–26](../../../joi250066supp5_prod_1761597796.4751.pdf#page=1). Earlier PLANp10 andp39 contain baseline+treatment+randomcenter without stroke type; the latest versionp86 is the primary comparator.

**Printed statements and values:** Protocolp86 specifies FMMA at3months, baselineFMA covariate, treatment and acuteischemic/hemorrhagic event type fixed effects, and one random intercept percenter. SAPp10 specifies a linear model with baselineFMA and two-level treatment. Mainp4 states a linear baselineFMA-adjusted treatment model. Code explicitly fits `lm(fma_affected.Visit_3 ~ fma_affected.Visit_1.cent + medication)`. Mainp5 says the SAP is in line with general statistical considerations in the final protocol and differences concern statistical terminology. Reported primary coefficient−0.90,95%CI−3.78to1.98,P=.54.

**Rule and calculation:** Compare specified design matrices and variance structure for the same primary outcome/population: protocol requires baseline+treatment+stroke-type fixed terms and center random intercept; implemented formula contains baseline+treatment only. This is an analysis replacement, not a model estimate versus crude ratio. No numerical rounding can add the omitted terms; recomputed interval/relative numeric discrepancy are not applicable to this categorical model comparison.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The primary adjusted3-monthFMA treatment effect−0.90[−3.78,1.98],P=.54 and its prespecified-model attribution.

**Why context does not resolve it:** Category5 applies to the planned primary analysis replaced in reporting. SAP precedence before database closure can establish the implemented model but does not make it the same model as the printed protocol. This does not question either model as a stated choice.

**Alternatives and missing definitions:** The later SAP may intentionally supersede the protocol or a model amendment may exist outside the supplied package. No source identifies an amendment accounting for removal of stroke type/center or supplies the original protocol-model result. These facts could explain the change; they do not make the printed specifications identical.

**Exact human question:** Which prespecified primary model is the reported−0.90-point estimate attributed to, and what supplied amendment or documented analysis change accounts for removing the protocol's stroke-type fixed effect and center random intercept?

### F-ST1-002

**Observation:** The all-randomized primary analysis population in the protocol becomes a survivor-only primary analysis in the SAP/report.

**Relationships:** S009,S017,S032,S035,S077,S091. **Focus area:** D (also A,C). **Proposed review domain:** protocol_report. **Proposed primary relationship:** P_R. **All relationships:** P_R,P_P.

**Exact locations and roles:** PLAN [protocolp86,§§11.4.1–11.4.2](../../../joi250066supp1_prod_1761597796.4601.pdf#page=86), PLAN [protocolp87,§11.5](../../../joi250066supp1_prod_1761597796.4601.pdf#page=87); PLAN [SAPp4,§3.2 andfootnote1](../../../joi250066supp2_prod_1761597796.4701.pdf#page=4); REPORT [mainp4,Statistical Analyses](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4), REPORT [mainp5,Figure1](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5); REPORT [results supplementp12,population definitions](../../../joi250066supp3_prod_1761597796.4701.pdf#page=12) and [p13,estimand1](../../../joi250066supp3_prod_1761597796.4701.pdf#page=13).

**Printed statements and values:** ProtocolFAS consists of all randomized participants, each analyzed according to allocation; primary FMMA analysis follows this specification, with MICE for missing values and complete-case sensitivity. No primary death exclusion is specified. SAPp4 keeps deceased in formalFAS but explicitly says they contribute only to treatment-policyIII/composite; missingFMA is imputed only among survivors. Mainp4 excludes deaths from the primary analysis, calling this FAS.610 randomized;28deaths;582primary,296L+286P. Death-imputed/composite sensitivities have610.

**Rule and calculation:** All-randomized and survivor-primary contribution rules are different analysis-population specifications for the same primary endpoint.610−28=582; exclusions are11L+17P=28;582/610=95.4098%. Counts reconcile internally and are not themselves a count discrepancy. The finding is the planned/report population change; display intervals and relative discrepancy are not applicable to that logical change.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Population/estimand underlying primary−0.90[−3.78,1.98],P=.54,n582 rather than all610 randomized.

**Why context does not resolve it:** Category5 applies to replacement of the planned primary analysis. The SAP clearly defines the later survivor contribution rule, so the report is understandable, but the protocol's all-randomized primary specification is substantively different. The FAS name alone is not the finding.

**Alternatives and missing definitions:** The estimand framework may be a prospective amendment superseding the protocol, as the main article's terminology discussion suggests. The protocol does not state how death would have been represented in its original primary FMMA analysis; that missing rule limits reconstruction but does not change its all-randomized wording.

**Exact human question:** Was exclusion of the28pre-assessment deaths from the primary analysis a prospective change to the protocol's all-randomized analysis, and which documented specification establishes the intended primary population and original handling of death?

### F-ST1-003

**Observation:** The supplied report does not present the prespecified primary-estimand subgroup package and additional protocol primary sensitivity adjustments.

**Relationships:** S013,S051,S078,S092. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed primary relationship:** P_R. **All relationships:** P_R.

**Exact locations and roles:** PLAN [SAPp12,§7.2](../../../joi250066supp2_prod_1761597796.4701.pdf#page=12) and [p15,subgroup addendum](../../../joi250066supp2_prod_1761597796.4701.pdf#page=15); PLAN [protocolp86,§11.4.3b–c](../../../joi250066supp1_prod_1761597796.4601.pdf#page=86). REPORT [mainp5,methods](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5), [mainp6,Primary Outcome](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), [mainp7,Additional Post Hoc Analyses](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=7); REPORT [supplementp18,eTables7/8](../../../joi250066supp3_prod_1761597796.4701.pdf#page=18), [p27,eFigure7](../../../joi250066supp3_prod_1761597796.4701.pdf#page=27). Absence was checked against the complete current DOC-001pp1–10 and DOC-004pp1–27 maps, not a sampled paragraph.

**Printed statements and values:** SAP specifies seven primary-estimand subgroup analyses, using subgroup and treatment×subgroup terms and a forest plot: age<median/≥median; sex; distal motor0/>0; corticalNIHSSsum0/>0; baselineSSRI; ischemic/hemorrhagicstroke; baselineFMAseverity. Addendum specifies baselineFMA<median/≥median. Protocol additionally prespecifies a treatment×stroke-type sensitivity and exploratory primary adjustments for age,sex,dementia,selectivehand/wrist,corticaldysfunction,fatigue,SSRI,extrapyramidalsymptoms andimpetus. Report shows posthoc baselineFMA≤35/>35, a continuous baseline×treatment model, and nonlinear baseline sensitivities; it supplies no results for the seven planned subgroup interactions or the other specified covariate-adjusted primary sensitivity. Baseline overall median is34.

**Rule and calculation:** A posthoc≤35/>35 split is not the SAP's<34/≥34median split; its treatment coefficients also do not supply the other six subgroup-interaction analyses. The published continuous interaction tests another specified contrast. The complete report inventory contains no corresponding forest plot/table or coefficients. This is not a request for a preferred new subgroup analysis. Numeric recomputed intervals/relative discrepancy are not applicable to missing planned analysis outputs.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecified sensitivity/heterogeneity interpretation of the primary3-monthFMA treatment effect and its contrast with the reported posthoc severity result.

**Why context does not resolve it:** Category5 requires registration of planned primary analyses not reported. The main article's explicit omission of other-time/subset secondary measures does not identify these primary-estimand subgroup analyses as deferred or replaced. Calling the displayed severity analysis posthoc does not supply the planned median-based interactions.

**Alternatives and missing definitions:** The analyses may have been performed or reserved for another publication; a prospective amendment may remove them. No supplied result or cross-reference identifies such output or change. Median tie handling and per-subgroup sample sizes are also unprinted and were not inferred.

**Exact human question:** Where are the prespecified primary-estimand subgroup interaction results and protocol primary sensitivity adjustments reported, or what documented change deferred or replaced them, including the planned median-based severity split?

### F-ST1-004

**Observation:** The planned center interaction analysis is represented only by a graph labeled posthoc, without the planned model result.

**Relationships:** S015,S049,S064,S092. **Focus area:** D (also C). **Proposed review domain:** protocol_report. **Proposed primary relationship:** P_R. **All relationships:** P_R.

**Exact locations and roles:** PLAN [SAPp11,§7](../../../joi250066supp2_prod_1761597796.4701.pdf#page=11), PLAN [protocolp86,§11.4.3a](../../../joi250066supp1_prod_1761597796.4601.pdf#page=86); REPORT [mainp5,center-analysis paragraph](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5), REPORT [supplementp25,eFigure5](../../../joi250066supp3_prod_1761597796.4701.pdf#page=25). Complete current main/supplement maps establish absence of a center-interaction result.

**Printed statements and values:** SAP specifies including center and treatment-by-center interaction in the main model and graphical display stratified bycenter or groups ofcenters. Protocol prespecifies the graph. Mainp5 describes a “post hoc exploratory plot” for treatment-effect heterogeneity, pooling centers with<50participants; eFigure5 gives group boxplots andpatientdots. No center×treatment model result/test is supplied.

**Rule and calculation:** A graphical comparison supplies neither the specified model interaction nor its estimate/test. The plot's prespecification attribution also differs from the protocol/SAP. No statistic, SE, degrees of freedom or center-specific adjusted effect can be reconstructed from the printed boxplots, so none is invented. Display intervals/relative discrepancy are not applicable.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Planned center-related sensitivity of the primary FMA treatment effect and whether the displayed heterogeneity assessment was prespecified.

**Why context does not resolve it:** Category5 applies to the planned primary supplementary model not reported. Labeling the graph exploratory is consistent with the plan, but labeling it posthoc and presenting a graph alone does not establish performance/reporting of the planned center-interaction model.

**Alternatives and missing definitions:** “Posthoc” may refer only to the particular plotting implementation or pooling<50, while the broader question was prespecified. The model may have been fit without its output being supplied. Those explanations leave the model result unlocated.

**Exact human question:** Was the planned primary model including center and treatment×center fitted, where is its result reported, and does the posthoc designation apply only to the graph implementation rather than to the prespecified center heterogeneity analysis?

### F-ST1-005

**Observation:** The reported mRS/PRAI missing-data procedures replace the planned general secondary-outcome imputation rule.

**Relationships:** S014,S048,S055,S093. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed primary relationship:** P_R. **All relationships:** P_R.

**Exact locations and roles:** PLAN [SAPp11,§6](../../../joi250066supp2_prod_1761597796.4701.pdf#page=11); REPORT [mainp5,secondary methods](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5); REPORT [supplementp7,Deviations](../../../joi250066supp3_prod_1761597796.4701.pdf#page=7) and [p15,eTable4](../../../joi250066supp3_prod_1761597796.4701.pdf#page=15).

**Printed statements and values:** SAP says patients missing a secondary outcome will be imputed as for the primary analysis, except potential-harm outcomes. Main says missing mRS/PRAI were not imputed. Supplement explicitly discloses that deaths before3months received mRS6 and missingPRAI were not imputed. eTable4 mRSOR.93[.69,1.23],n596;PRAI n546 withn270placebo/n276levodopa,51events each. Disclosure is retained; it is not characterized as hidden.

**Rule and calculation:** Compare the same secondary-outcome missingness rule in PLAN and REPORT: general MI versus stated exceptions.546=270+276 and mRS596 is a distinct analysis size from primary582; these are coherent reported denominators, not miscounts. The issue is the replacement of the planned analysis rule. Display intervals/relative discrepancy are not applicable to a missing-data rule change.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** mRS adjustedOR.93[.69,1.23],n596 and PRAI observed no-relevant-improvement proportions,n546; how missingness/death contributes to those analyses.

**Why context does not resolve it:** This is a planned-versus-reported analysis change in the always-register category. Explicit disclosure identifies the later procedure and is an important alternative/context fact; it does not make it the planned MI procedure. No preferred imputation approach is proposed.

**Alternatives and missing definitions:** mRS6 has an explicit death meaning and may be a deliberate prospective refinement. The source directly explains both exceptions. It does not supply a dated amendment, missing counts byarm, or whether any surviving missingmRS were also excluded rather than imputed; the main statement is broader than the supplement's death-onlymRS explanation.

**Exact human question:** Confirm the final missing-data rule and participant counts for mRS and PRAI, including surviving participants with missingmRS, and identify the documented change from the SAP's secondary-outcome imputation rule.

### F-ST1-006

**Observation:** A planned affected-side FMA secondary outcome is reported as an unaffected-side outcome.

**Relationships:** S007,S024,S033,S047,S055,S085. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed primary relationship:** P_R. **All relationships:** P_R.

**Exact locations and roles:** PLAN [SAPp5,§4.2](../../../joi250066supp2_prod_1761597796.4701.pdf#page=5) and [p10,§5.3 final paragraph](../../../joi250066supp2_prod_1761597796.4701.pdf#page=10); REPORT [mainp3,secondary outcome3](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3), [mainp6,secondary result](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6); REPORT [supplementp7,deviation3](../../../joi250066supp3_prod_1761597796.4701.pdf#page=7) and [p15,eTable4row1](../../../joi250066supp3_prod_1761597796.4701.pdf#page=15).

**Printed statements and values:** SAP lists FMMA of the affected side as a secondary measure and says the affected-side secondary analysis excludes bilateral pathology. Report identifies unaffected-side totalFMA,meansL89.67(SD9.87),P89.14(10.32),effect.63[−.72,1.99],n582. Supplement explicitly says the calculation was performed for the unaffected side despite the SAP's affected-side wording.

**Rule and calculation:** Affected and unaffected sides are distinct measured endpoints, not interchangeable numeric units. The planned secondary endpoint has been replaced in the report, with a reported explanation. This is not the unchanged primary affected-side totalFMA. No rounding calculation applies to side identity; the printed effect/CI has valid containment/order/null behavior.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The secondary adjustedFMA effect.63[−.72,1.99] and whether it answers the planned affected-side secondary endpoint.

**Why context does not resolve it:** Category5 covers planned-versus-reported outcome/analysis changes. The source makes the actual reported side clear, which must be preserved in extraction; it does not equate the two sides or establish that the planned affected-side analysis was supplied. This finding concerns endpoint identity rather than capitalization or scale nomenclature.

**Alternatives and missing definitions:** The SAP side may have been an unintended label, as the reported explanation states; the intended prospective endpoint may always have been unaffected-sideFMA. No pre-analysis version in the supplied SAP prints that endpoint or explains how the bilateral-pathology exclusion maps to the final n582.

**Exact human question:** Confirm that.63[−.72,1.99] is the unaffected-side totalFMA effect and identify the prospective endpoint specification and bilateral-pathology rule corresponding to that reported secondary analysis.

### F-ST1-007

**Observation:** The PROMIS-29 result is a single scalar although the supplied outcome definition gives seven domains with different directions and no scalar scoring rule.

**Relationships:** S019,S058,S074,S085. **Focus area:** C. **Proposed review domain:** statistical_results. **Proposed primary relationship:** S_W. **All relationships:** S_W.

**Exact locations and roles:** REPORT [mainp3,Secondary Outcomes](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3), REPORT [mainp6,PROMIS-29 result](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6). REPORT [supplementp15,eTable4PROMIS29row](../../../joi250066supp3_prod_1761597796.4701.pdf#page=15) corroborates the single-scalar presentation; it does not create an additional discrepancy relationship. PLANprotocolp70 states population mean50/SD10 and lists domains, but is contextual and not a conflicting side.

**Printed statements and values:** Main defines PROMIS-29 as7domains×4items with raw range4–20perdomain; higher scores indicate better function in some domains and worse in others. Main then reports one PROMIS-29 mean66(SD14)L and65(14)P and one adjustedmean difference−.37[−3.34,2.61]. eTable4 likewise gives one mean/SD pergroup,64.74/14.33L and65.11/13.79P,and the same adjusted effect. Neither supplied report defines how domains were selected, combined or recoded for this scalar.

**Rule and calculation:** A single domain bounded4–20 cannot have a groupmean64.74or66; even the rounding intervals [65.5,66.5] and [19.5,20.5] are disjoint, minimumgap45/66=68.18%. This arithmetic does **not** assert that the result is an out-of-range total; it establishes that a different, undefined scoring step is needed. The method observation is the missing mapping from the explicitly multidomain, differently oriented definition to the single printed outcome/regression. No preferred PROMIS scoring method is proposed.

**Qualifying route:** Route B.

**Affected result or extracted value:** PROMIS-29 adjustedmean difference−.37[−3.34,2.61],its scale and direction,which determine whether and how the effect is interpretable or extractable.

**Why context does not resolve it:** The immediate definition supplies several domain scores with opposing directions, while the result supplies one scalar. Calling it a PROMIS-29 score does not specify which function of the domains was modeled; the single adjusted difference cannot identify that function. This is tied to a printed range/result mismatch, not merely an unreported model detail with no conflicting statement.

**Alternatives and missing definitions:** The result could be a raw aggregate, a selected domain transformed to another metric, or a composite with directional recoding. None is identified in the supplied report. Missing definitions are the constituent items/domains, aggregation/transform, directional recoding and corresponding baseline covariate used in this regression. External scoring conventions were not inferred.

**Exact human question:** What exact item/domain scoring, aggregation or transformation and directional recoding produced the single PROMIS-29 outcome and its baseline covariate used for−.37[−3.34,2.61],and what is that reported scalar's range and direction?

## Excluded observations

Only apparent issues judged not to meet the threshold are listed. Reconciling checks remain in the S inventory. Each row has one reason code; no interval/P conflict is excluded.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 pp1,6 and DOC-004 p15 | FMA medians68 versus64 or crude differences in means need not equal negative adjusted coefficients; the models are explicitly adjusted. | MODEL_VERSUS_CRUDE |
| REPORT DOC-001 p6 versus DOC-004 p15, PROMIS10 | Mean28 in both arms versus29.87P/30.04L. L half-unit gap30.035−28.5=1.535, relative5.482%; P gap1.365/28=4.875%. The remaining L difference is a non-key secondary copy comparison, absent from the abstract, changing no primary/key result or analysis-population size. | PERIPHERAL_COMPARISON |
| REPORT DOC-001 p6 versus DOC-004 p15, PROMIS29/PRAI | PROMIS29 L66 versus64.74: gap65.5−64.745=.755, relative1.144%. PRAI placebo52 versus51: exact-count difference1/52=1.923%. Both below5%. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-004 pp12,13, composite | Narrative OR versus explicit win-ratio strategy, table definition and SAP wins/wins rule: intended quantity identifiable at once. Upper CI copies1.25/1.26 have touching half-unit intervals. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-004 p15, effect header | Shared mean-difference-on-FMA header over mRS is resolved by the explicit ordinal-OR method and mRS row.93[.69,1.23]. | CONTEXT_RESOLVES |
| REPORT DOC-004 p14 versus DOC-001 p4, estimand11 | Table exclusion wording uses low rehabilitation “and” low drug, while main inclusion requires both adherences. Explicit adherent-subset definition clarifies the conjunction. No unpublished overlap assumed. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001 p5 versus DOC-004 p7, imputation | Main secondary summary-score imputation versus supplement FMA item-level then secondary summary-score imputation can be read as primary FMA first, then secondary outcomes. No explicit secondary-FMA item-level statement conflicts. | CONTEXT_RESOLVES |
| PLAN DOC-003 p11 versus p7, policyIII | p11 repeats a complete-case caption; p7 and result table explicitly define death imputation. Underlying model is the same and result identity is clear. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-002 pp10,37,56,84 versus REPORT DOC-001 p3 | Normal sample-size approximation545.061 versus t-test548 is diagnostic. Allowing SD[24.5,25.5] and delta[5.5,6.5] gives diagnostic N[446.039,674.874], overlapping printed[547.5,548.5]; gap0, relative discrepancy0. Additional bounded protocol confirmation independently supplied this interval calculation. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-004 p17, eTable6 | Overall145 versus67+79=146 and classification totals146: exact-count relative difference1/145=.690%, below5%. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-004 p16, eTable5 |29 event outcomes of death versus28 participants who died are explicitly different units. | CONTEXT_RESOLVES |
| REPORT DOC-004 p25, eFigure5 | At3months title versus change-from-baseline axis: the axis states change and this non-key exploratory display changes no exact primary estimate. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 pp34,86 | Visit2 parenthetical after3months and terminal sensitivity(c,d) pointers are resolved by repeated schedule/subset definitions. No conflicting primary population count is established by these pointers. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 pp39,86 versus REPORT DOC-001 p4 | PP permits justified reduced dose; the posthoc strict≥80% adherence set need not be identical. Exact membership would require unpublished information. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-003 pp10,16–18 and REPORT DOC-001 p3 | Missing non-key later/subset, binary-walking and exploratory biomarker/registry/fatigue outputs are not abstract results or designated key. Separate-publication allowance and partial secondary reporting make these comparisons peripheral. Planned primary subgroups are separately emitted in F-ST1-003. | PERIPHERAL_COMPARISON |
| REPORT DOC-006 p1 and PLAN DOC-003 p11 | Unpublished imputation objects, function definitions, bootstrap pooling, predictors and MI degrees of freedom do not establish a code/result conflict. No evaluated result appears in the code. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 pp1,3, intervention | Abstract three-times-daily39-day wording compresses the explicitly defined escalation/full-dose/taper regimen; the detailed schedule identifies treatment. | CONTEXT_RESOLVES |
| PLAN DOC-002 pp20,39,65,69,78,86 | Poststroke/treatment-onset wording versus repeated3months after randomization±14days is resolved by detailed schedules. No observed off-window result is asserted. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001 pp3,7 versus PLAN outcome hierarchy | Secondary findings called exploratory for multiplicity remain secondary endpoints. Nonsignificant benefit/harm discussion does not claim equivalence. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-002 pp38,85, PROMIS power | Exact80% PROMIS power lacks specified effect/variance inputs; no contradictory printed calculation is supplied. Added from the independent bounded protocol confirmation. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 pp38,85, DSMC charter | Numeric safety-alert thresholds are deferred to an unsupplied charter; no reported threshold-crossing or stopping decision conflicts. Added from the independent bounded protocol confirmation. | CONDITIONAL_OR_UNREPORTED |
| PLAN earlier eligibility versus version1.4 and REPORT current eligibility | Version1.4 explicitly includes hemorrhagic stroke and deletes synopsis rehospitalization. Supplied versions explain the earlier/current eligibility and endpoint-list difference. Added from the independent bounded protocol confirmation. | CONTEXT_RESOLVES |

## Source confirmation and limitations

Current renders used the supplied `pdf_tools.py render` with package-local pinned PyMuPDF1.26.4,200dpi,CPU. DOC-002 pp86,87 became `preprocessing/statistical_current/protocol-86.png` and `protocol-87.png`; DOC-003 pp4,5,10,11,12,15 became `sap-04.png`,`sap-05.png`,`sap-10.png`,`sap-11.png`,`sap-12.png`,`sap-15.png`; DOC-001 pp3,4,5,6 became `main-03.png`,`main-04.png`,`main-05.png`,`main-06.png`; DOC-004 pp7,15 became `results-07.png`,`results-15.png`. Additional renders DOC-006p1→`code-01.png` and DOC-004pp13,25→`results-13.png`,`results-25.png` confirmed the primary code, estimand table and center graph. All17 renders were opened with view_image. Formula and remaining display transcriptions come from the current complete source maps. No source or older asset was modified.

The raw current mapping files total228870bytes including the numeric index, historical/contextual material and administrative coverage. Statistical evidence was selected through S scopes and targeted clauses, but the exact normalized scientific character count was not mechanically measured. The coordinator repaired the context-bound ambiguity through a separate fresh high-effort agent `/root/statistics_protocol_confirmation`: all27 protocol relationships S068–S094 were independently covered below200000characters and32rendered pages, with no omitted clause or newly emitted finding. Its artifacts are [protocol confirmation checker](statistical_pass_1_protocol_confirmation.md) and [27-record confirmation inventory](../statistics/protocol_confirmation_inventory.md). These are optional pass1 confirmation records, not pass2. All seven finding patterns have matching source facts in that confirmation; this is not an independent inclusion-screen decision. Six of its nine excluded patterns duplicate canonical rows; three were appended above. The canonical table now contains22 excluded observations exactly once each; the nine-row part preserves original provenance.

Exact pooled standard errors/degrees of freedom, covariance, imputation predictors, participant overlaps and unprinted subgroup coefficients are not supplied. No exact model test or bootstrap interval was fabricated from rounded results. Diagnostic approximations are marked. Mandatory pass1 scope94/94; findings7; canonical excluded-observation rows22; scientific coverage gaps0. Fresh pass2 must revisit every S record using the later ledger, screening and recheck under a distinct runtime agent.

## Explicit per-relationship pass-1 record index

The following rows are a lossless mechanical copy of the pass-1 source scopes, substantive checks and completed statuses already authored by the fresh pass-1 specialist in the canonical statistical inventory. The coordinator adds this explicit index so every ID appears individually in the checker artifact, rather than only in the reviewed S001–S094 range. No new statistical inference or model call is substituted for either specialist pass.

| S ID | Exact source scope and role | Pass-1 check and result | Pass-1 status |
|---|---|---|---|
| S001 | REPORT DOC-001 p1; p6 match | −0.90 within [−3.78,1.98]; CI crosses0 and P=.54 exceeds .05. Normal-CI diagnostic SE1.4694,z−.6125 is compatible; actual pooled MI df/SE not printed, so no exact reverse engineering. Same primary effect across report locations. | PASS_1_COMPLETE |
| S002 | REPORT DOC-001 pp1,2,7,8 | Nonsignificant superiority conclusion follows S001; no equivalence or noninferiority claim inferred from lack of significance. | PASS_1_COMPLETE |
| S003 | REPORT DOC-001 p2 | Participant-randomized parallel superiority design, not cluster randomization; multicenter alone does not require a preferred model. Planned actual model comparison F-ST1-001. | PASS_1_COMPLETE |
| S004 | REPORT DOC-001 p2; PLAN DOC-002 pp16,38,40,62,85,87 | Safety reviews at200/400/500 do not conflict with absence of efficacy interim analysis. No efficacy stopping calculation printed; DSMC-charter numeric alert boundaries not supplied. | PASS_1_COMPLETE |
| S005 | REPORT DOC-001 p3; PLAN DOC-002 pp27,55,74 | Center-stratified minimization1:1 with80% biasing probability reconciles; reported baseline-only model versus explicitly planned center adjustment is F-ST1-001. No cluster-randomized analysis imposed. | PASS_1_COMPLETE |
| S006 | REPORT DOC-001 p3; PLAN DOC-002 pp54,69,78 and DOC-003 pp3,5 | Primary affected FMA final score3months±14days,0–100,66+34=100; higher better. Week5 is separate secondary. Posthoc adjusted change estimator equivalence checked S057. | PASS_1_COMPLETE |
| S007 | REPORT DOC-001 p3 | Secondary endpoints remain labeled secondary while findings are exploratory for multiplicity. No familywise superiority claim made. Non-key unreported later/subset results are not assumed primary/key. Outcome-side change F-ST1-006; missing-data changes F-ST1-005. | PASS_1_COMPLETE |
| S008 | REPORT DOC-001 p3; PLAN DOC-002 pp37,38,84,85 | Two-sample t-test plan SD25,delta6,power.80,two-sided.05,n548; normal approximation545.06 is diagnostic only and within display precision.610×.90=549; target/evaluable values reconcile. Actual power software/rounding not specified. | PASS_1_COMPLETE |
| S009 | REPORT DOC-001 p4; PLAN DOC-003 pp4,7,10 and DOC-002 p86 | Linear baseline+treatment model, survivor imputation and two-sided.05 clear; F-ST1-001 planned mixed model and F-ST1-002 all-randomized versus survivor-primary population. Main/code/SAP current model agree. | PASS_1_COMPLETE |
| S010 | REPORT DOC-001 p4; DOC-004 pp12,13; PLAN DOC-003 pp6–12 | Seven supplementary estimands match five named intercurrent-event types; thresholds80%,at least one week<5sessions/week over4weeks and window retained. Composite ratios not treated as FMA differences. | PASS_1_COMPLETE |
| S011 | REPORT DOC-001 p4; DOC-004 p14 | Posthoc death0 n610 gives−.03[−3.27,3.21], contained, ordered,crosses0; death0 differs deliberately from death-imputation sensitivity. No test printed. | PASS_1_COMPLETE |
| S012 | REPORT DOC-001 p4; DOC-004 p14; PLAN DOC-002 p86 | Joint medication-and-rehabilitation adherent subset n395,.32[−3.25,3.89] is contained and nonsignificant by CI. PP protocol permits justified reduced dosage, so do not assume exactly same membership. Table conjunction wording excluded once. | PASS_1_COMPLETE |
| S013 | REPORT DOC-001 pp5,6; DOC-004 p27; PLAN DOC-003 pp12,15 | Posthoc≤35/>35 differs from planned median split<median/≥median; baseline overall median34. Missing planned subgroup package F-ST1-003, not a claim that posthoc35 is intrinsically unsuitable. Graph subgroup CIs cross0. | PASS_1_COMPLETE |
| S014 | REPORT DOC-001 p5; DOC-004 pp7,15; PLAN DOC-003 pp10,11 | Baseline-adjusted secondary regressions and mRS ordinal logistic appropriate to stated scale; no preferred model proposed. F-ST1-005 changed missing-data rules; item/summary FMA wording excluded in pass-1 table. | PASS_1_COMPLETE |
| S015 | REPORT DOC-001 p5; DOC-004 p25; PLAN DOC-003 p11 and DOC-002 p86 | Center graph pooling<50 prespecified in principle; plan also specifies center/interaction model. Reporting-status/model coverage question F-ST1-004. No center-specific coefficient or test inferred from boxplots. | PASS_1_COMPLETE |
| S016 | REPORT DOC-001 p5; DOC-004 pp18,26 | Posthoc spline baseline association and treatment interactions distinguished. F-tests in S061/S062 are model comparisons, not treatment-effect P values. | PASS_1_COMPLETE |
| S017 | REPORT DOC-001 p5; REPORT DOC-006 p1; PLAN DOC-002 p86 and DOC-003 p10 | R4.3.1/model code consistent with current SAP baseline+treatment fit. Protocol–SAP statistical changes are substantive model/population comparisons F-ST1-001/002; terminology alone not registered. | PASS_1_COMPLETE |
| S018 | REPORT DOC-001 p6; DOC-004 p13 | Primary effect repeats S001; medians68/64 are descriptive, not adjusted mean difference.582=610−28;296+286=582;551complete+31imputed=582. | PASS_1_COMPLETE |
| S019 | REPORT DOC-001 pp3,6; DOC-004 p15 | PROMIS29−.37 within[−3.34,2.61],crosses0; no P given. Scalar scoring definition F-ST1-007. Descriptive mean66 versus64.74 gap is display/peripheral, not inference against model. | PASS_1_COMPLETE |
| S020 | REPORT DOC-001 p6; DOC-004 p15 | PROMIS10 .18 within[−.98,1.33],crosses0; actual raw scale10–50 contains reported means.28 versus30.04 is excluded non-key secondary copy comparison, not a CI/test finding. | PASS_1_COMPLETE |
| S021 | REPORT DOC-001 p6; DOC-004 p15 | PRAI51/276=18.48%,52/270=19.26% reconcile with18/19%; supplement51/270=18.89%. The one-person copy gap is below display rule and non-key; no imputed P invented.546=270+276. | PASS_1_COMPLETE |
| S022 | REPORT DOC-001 p6; DOC-004 p15 | Affected upper adjusted−.73 within[−2.97,1.50],ordered,crosses0. Descriptive39/39 does not replace baseline adjustment. Item/score wording checked and excluded in pass-1 table. | PASS_1_COMPLETE |
| S023 | REPORT DOC-001 p6; DOC-004 p15 | Affected lower−.13 within[−1.02,.77],ordered,crosses0. Same item/score wording checked and excluded in pass-1 table. | PASS_1_COMPLETE |
| S024 | REPORT DOC-001 p6; DOC-004 pp7,15; PLAN DOC-003 pp5,10 | Unaffected FMA .63 within[−.72,1.99],ordered,crosses0. Planned-side comparison F-ST1-006; FMA item/score wording excluded in pass-1 table. | PASS_1_COMPLETE |
| S025 | REPORT DOC-001 p6; DOC-004 p15 | Both retained endpoints checked separately: NIHSS−.14[−.61,.33],RMI−.33[−1.04,.37];containment/order/null coherent. Outcome directions differ by scales; no contrary benefit claim. | PASS_1_COMPLETE |
| S026 | REPORT DOC-001 p6; DOC-004 p15 | Ordinal OR.93 in[.69,1.23],CI crosses1; ordinal model is explicitly identified. Same group medians3 do not constrain ordinal OR to1. Missing-data population n596 compared in F-ST1-005. | PASS_1_COMPLETE |
| S027 | REPORT DOC-001 p6; DOC-004 p15 | Week5 affected total .02 within[−2.81,2.84],crosses0. Descriptive57/56 vs modeled.02 is not a discrepancy. | PASS_1_COMPLETE |
| S028 | REPORT DOC-001 p7; DOC-004 p18 | Spline association/noninteraction narrative matches F-testP<.01 for spline vs linear and P>.75 for spline×treatment. Treatment−.87[−3.65,1.92],P=.541 remains nonsignificant. | PASS_1_COMPLETE |
| S029 | REPORT DOC-001 p7 | Reported absence of detected benefit/harm does not state equivalence. Primary CI excludes a +6-point benefit but includes small positive/negative effects. Safety counts are events versus people; no inferential safety equality test supplied. | PASS_1_COMPLETE |
| S030 | REPORT DOC-001 pp7,8 | Final nonsignificant-superiority conclusion matches S001/S018. No NI/equivalence margin or conclusion imported. | PASS_1_COMPLETE |
| S031 | PLAN DOC-003 pp2,3; REPORT DOC-001 pp2,3 | Superiority1:1,100/25mg tid full-dose phase plus identical rehabilitation matches detailed39-day dose schedule. Abstract compressed dosing wording resolved by phase definitions. | PASS_1_COMPLETE |
| S032 | PLAN DOC-003 p4; REPORT DOC-001 pp4,5 and DOC-004 pp12,13 | SAP footnote explicitly retains deceased in formalFAS but limits contribution to death/composite estimands; report FAS uses582survivors. This nomenclature is clear; protocol all-randomized primary difference tracked F-ST1-002. | PASS_1_COMPLETE |
| S033 | PLAN DOC-003 p5; REPORT DOC-001 p3 and DOC-004 p15 | PrimaryVisit3 and secondaryVisits2–5 retained. Affected-to-unaffected total substitution F-ST1-006. Secondary/exploratory terminology not outcome promotion/demotion. | PASS_1_COMPLETE |
| S034 | PLAN DOC-003 p6; DOC-002 pp70,71,85 | RMI0–15,independent walking≥7 clear; harm windows distinguish3months SAE/nonserious and12months death/recurrent stroke. Missing non-key binary walking secondary publication not assumed unreported key result. | PASS_1_COMPLETE |
| S035 | PLAN DOC-003 pp6,7; REPORT DOC-004 pp12,13 | Five estimand attributes and primary randomization despite intercurrent events coherent with separately stated survivor contribution; substantive protocol primary population comparison F-ST1-002. | PASS_1_COMPLETE |
| S036 | PLAN DOC-003 p7; REPORT DOC-004 pp12,13 | Complete-case mITT551=282+269,−.39[−3.33,2.56],same baseline-adjusted model. No complete-case P printed. | PASS_1_COMPLETE |
| S037 | PLAN DOC-003 p7; REPORT DOC-004 pp12,13 | Death-imputed analysis n610,−.98[−3.77,1.81] contains estimate/crosses0. SAPp11 complete-case caption is evident label repetition; p7 explicit imputation controls. | PASS_1_COMPLETE |
| S038 | PLAN DOC-003 pp8,11; REPORT DOC-004 pp12,13 | Unmatched win ratio survivor/death/survival/FMA ordering explicit;1.06[.86,1.26] contains1 and estimate,positive means more treatmentwins. Odds-ratio narrative label resolved by explicit win-ratio definition/table. | PASS_1_COMPLETE |
| S039 | PLAN DOC-003 p11; REPORT DOC-004 pp12,13 |1000bootstrap samples per imputed dataset and95%CI/null1 explicit. CI crosses1,so nonsignificant-sensitivity interpretation coherent. Exact bootstrap pooling details absent but no printed CI/test contradiction; not reconstructed as lognormal. | PASS_1_COMPLETE |
| S040 | PLAN DOC-003 pp8,12; REPORT DOC-004 p13 | Motor-impairingSAE exclusion n545,−1.41[−4.31,1.49];contained,ordered,crosses0. Excluded37 versus582 is possible; no event count equated to excludedpersons. | PASS_1_COMPLETE |
| S041 | PLAN DOC-003 pp8,9,12; REPORT DOC-004 p13 | <80%medication exclusion n496,−.57[−3.73,2.58];contained,ordered,crosses0. Main252+244=496adherent overall; no deceased-overlap assumptions made. | PASS_1_COMPLETE |
| S042 | PLAN DOC-003 pp9,12; REPORT DOC-004 p13 | Rehabilitation exclusion n450,.19[−3.11,3.49];contained,ordered,crosses0. Atleastoneweek<5over4weeks preserved,not silently replaced by average. | PASS_1_COMPLETE |
| S043 | PLAN DOC-003 pp9,12; REPORT DOC-004 p13 | Outside3months±14days exclusion n524,−.33[−3.31,2.65];contained,ordered,crosses0. No denominator reconstructed without visit records. | PASS_1_COMPLETE |
| S044 | PLAN DOC-003 p10; REPORT DOC-001 p4 and DOC-006 p1 | Final-outcome baseline-adjusted linear model and baseline-adjusted change coefficient equivalence: subtracting baseline changes baseline coefficient by−1 but not treatment coefficient on same data/design. Current SAP/report/code agree; original mixed model F-ST1-001. | PASS_1_COMPLETE |
| S045 | PLAN DOC-003 p10; REPORT DOC-006 p1 | Residual/leverage diagnostic loop supplied; no claim all assumptions failed or passed inferred. Transformations conditional,not a mandatory replacement model. Code not executed without data/imputations. | PASS_1_COMPLETE |
| S046 | PLAN DOC-003 p10; REPORT DOC-001 p5 | Continuous linear,binary logistic,ordinal logistic appropriate to explicitly stated structures; conditional robust/nonparametric alternatives not missing mandated analyses. | PASS_1_COMPLETE |
| S047 | PLAN DOC-003 p10; REPORT DOC-004 pp7,15 | Secondary primary estimand rule,affected-side bilateral-pathology exclusion and separate-publication allowance preserved. Side replacement F-ST1-006; population582 alone cannot establish whether excluded bilateral pathology existed. | PASS_1_COMPLETE |
| S048 | PLAN DOC-003 p11; REPORT DOC-004 p7 and DOC-001 p5 |100MICE/Rubin estimates/variances consistent. Planned secondary-imputation exceptions F-ST1-005; secondary-FMA item/summary wording excluded in pass-1 table. No covariance/predictor set invented. | PASS_1_COMPLETE |
| S049 | PLAN DOC-003 p11; REPORT DOC-001 p5 and DOC-004 p25 | Planned center+treatment×center model plusgraph versus posthocgraph-only presentation F-ST1-004. Center sample size<50 grouping not itself a candidate. | PASS_1_COMPLETE |
| S050 | PLAN DOC-003 p11; REPORT DOC-001 pp3,6,7 | Sensitivities explicitly no multiplicity adjustment,contextualized with primary; CIs all containnull. No significant familywise sensitivity conclusion contradicted. | PASS_1_COMPLETE |
| S051 | PLAN DOC-003 pp12,15; REPORT DOC-001 pp5–7 and DOC-004 pp18,27 | Seven primary-estimand subgroup interactions and median cutpoints versus posthoc≤35/>35 and continuous interaction; planned primary subgroup package not reported F-ST1-003. | PASS_1_COMPLETE |
| S052 | PLAN DOC-003 pp16,17; DOC-002 p87 | Biomarker/genetic hypotheses explicitly exploratory; unspecified concentration cutoffs are missing definitions without printed conflicting results. No biomarker trial coefficient reported. | PASS_1_COMPLETE |
| S053 | PLAN DOC-003 p18 | Registry/rehabilitation/fatigue/depression analyses and positive-result dependencies preserved; no reported coefficients or primary/key designation. Do not infer that absent exploratory outputs were never performed. | PASS_1_COMPLETE |
| S054 | REPORT DOC-004 p7; DOC-001 p5 |100MICE/Rubin pooling matchesSAP. FMA item-level versus entiresecondaryscore wording excluded in pass-1 table; no inference from unpublished predictor set. | PASS_1_COMPLETE |
| S055 | REPORT DOC-004 pp7,15; PLAN DOC-003 pp5,10,11 | mRS deaths assigned6, PRAI observed n546 and unaffected FMA n582 explicit. Planned changes F-ST1-005/006 retain disclosure. mRS596 is arithmetically compatible with28deaths+568other observations; actual allocation is not asserted. | PASS_1_COMPLETE |
| S056 | REPORT DOC-004 pp12,13 | All eight estimates−.90,−.39,−.98,1.06,−1.41,−.57,.19,−.33 are inside ordered CIs; linear CIs cross0, win-ratio CI crosses1. Sizes582,551,610,610,545,496,450,524. Upper copies1.25/1.26 below display threshold; OR label resolved. | PASS_1_COMPLETE |
| S057 | REPORT DOC-004 p14; DOC-001 p4 | All three posthoc rows checked: change−.90[−3.78,1.98]n582; death0−.03[−3.27,3.21]n610; joint adherence.32[−3.25,3.89]n395. Containment/order/null coherent. Conjunction excluded as wording; adjusted-change identity explains primary repeat. | PASS_1_COMPLETE |
| S058 | REPORT DOC-004 p15; DOC-001 p6 | All secondary estimates.63,−.73,−.13,.02,−.14,−.37,.18,OR.93,−.33 inside ordered CIs with null0/1 included. SMD is descriptive, not adjusted coefficient. PRAI51/270=18.89%,51/276=18.48%. Shared header resolved by explicit methods. Scoring gap F-ST1-007. | PASS_1_COMPLETE |
| S059 | REPORT DOC-004 pp16,17,19; DOC-001 pp6,7 |255SAE=129+126; severity103+106+46=255; outcomes6+76+29+0+142+2=255.29death event outcomes differ in unit from28people. AE145 versus146 below display threshold; classifications total146. No inferential equality claim supplied. | PASS_1_COMPLETE |
| S060 | REPORT DOC-004 p18,eTable7 |62.51[60.45,64.57] and.78[.69,.87],P<.001;−.90[−3.78,1.99],P=.542;interaction.00[−.12,.12],P=.971. Containment/order/null decisions coherent. Rounded.00 permits a small nonzero coefficient; pooled SE/df absent. | PASS_1_COMPLETE |
| S061 | REPORT DOC-004 p18,eTable8 |20.09[14.28,25.90];64.73[46.34,83.13];57.52[43.48,71.56];77.49[61.68,93.31],allP<.001;−.87[−3.65,1.92],P=.541. Containment/order/null decisions coherent. Three-df spline versus linear F-testP<.01 per imputation supports nonlinearity; no exact F/df invented. | PASS_1_COMPLETE |
| S062 | REPORT DOC-004 p18 | Spline×treatment F-testP>.75 across imputations supports no detected interaction. Linear interactionP=.971 tests a different model. Pooled P is not equated with per-imputation bounds. | PASS_1_COMPLETE |
| S063 | REPORT DOC-004 pp23,24; pp12,13 | Forest estimands1,2,3,5,6,7,8 use zero reference; negative favors placebo, positive levodopa. Directions match tables. Composite ratio appropriately absent from difference axis. | PASS_1_COMPLETE |
| S064 | REPORT DOC-004 p25; DOC-001 p5 | Center boxplots have change axis and at3months title. Exact coefficients/quantiles absent; no positions converted into exact numbers. Title comparison peripheral; planned model F-ST1-004. | PASS_1_COMPLETE |
| S065 | REPORT DOC-004 p26; p18 | Increasing nonlinear baseline–Visit3 association matches graph and F-test. Basis coefficient signs alone do not identify every curve property; prognostic curve is not a treatment effect. | PASS_1_COMPLETE |
| S066 | REPORT DOC-004 p27; DOC-001 pp5,6 | PH1death0/PH2adherence graphs match tables. PH3≤35/>35 CIs visually cross0; exact subgroup P/SE/n absent. Planned median interactions F-ST1-003; graphical approximations not extracted as exact. | PASS_1_COMPLETE |
| S067 | REPORT DOC-006 p1 | Printed model with(mice0,lm(Visit3~centeredbaseline+medication)), summary(pool(model)) and diagnostics match current model. N.imp not evaluated; unpublished objects/function behavior not assumed. No numeric result is printed in code. | PASS_1_COMPLETE |
| S068 | PLAN DOC-002 pp7,8,22,23 | Earlier outcome hierarchy matches the later core primary definition. Ischemic-only eligibility before version1.4 is documented version evolution. | PASS_1_COMPLETE |
| S069 | PLAN DOC-002 pp8,9,26–28 | Superiority1:1, minimization80%, center strata and eligibility coherent. The6-point target is a benefit/power assumption, not an equivalence margin. | PASS_1_COMPLETE |
| S070 | PLAN DOC-002 pp9,10,13,14,19–21,27,29–32 | Detailed39-day phases and primary visit3months after randomization govern looser onset wording. No off-window count inferred. | PASS_1_COMPLETE |
| S071 | PLAN DOC-002 pp10,23 | SD25, delta6,80% power, two-sided5%, n548;610×.90=549. Same sample-size check as S008. | PASS_1_COMPLETE |
| S072 | PLAN DOC-002 p10; REPORT DOC-001 p4 | Planned mixed baseline+treatment+random-center model differs from current linear fit: F-ST1-001. Generic secondary models and MICE reconcile with later detail. | PASS_1_COMPLETE |
| S073 | PLAN DOC-002 pp16,18,21,25 | DSMC safety review, no efficacy review, termination possibilities and safety windows consistent. Numeric charter boundaries not supplied. | PASS_1_COMPLETE |
| S074 | PLAN DOC-002 pp23–26 | FMA0–100=66+34; RMI0–15, walking≥7. PROMIS domain definitions and selected-center units preserved. Historical meta-analysis not used as a current-trial result. | PASS_1_COMPLETE |
| S075 | PLAN DOC-002 pp37,38 | Unadjusted t-test plan checked in S008.41.1−35.1=6;57%−45%=12points;12/45=26.67%≈27%. PROMIS power lacks numeric effect/variance inputs. | PASS_1_COMPLETE |
| S076 | PLAN DOC-002 pp38,40 | No efficacy stopping/interim plan conflicts with safety reviews. At-least-one-AE participant risk differs from event counts; no arm-specific risks inferred from overall177/115 affected people. | PASS_1_COMPLETE |
| S077 | PLAN DOC-002 pp39,40 | Randomized FAS, complete cases and PP defined; PP permits80% or justified reduced dose plus≥5 rehabilitation sessions/week. Primary population change F-ST1-002. Strict posthoc adherence need not equal PP. | PASS_1_COMPLETE |
| S078 | PLAN DOC-002 pp39,40 | Earlier center random effect: F-ST1-001.95%CI/two-sided5% coherent. Additional primary sensitivity outputs: F-ST1-003. No preferred adjustment proposed. | PASS_1_COMPLETE |
| S079 | PLAN DOC-002 pp40,42 | Genetic/biomarker analyses and future IPD intent are exploratory, with selected-center optional consent; no primary/key coefficient is reported. | PASS_1_COMPLETE |
| S080 | PLAN DOC-002 pp33–37 | Treatment days1–39, Visit2 at5weeks±7days and Visit3 at3months±14days coherent. p34 Visit2 parenthetical is resolved by the detailed schedule; pointer excluded. | PASS_1_COMPLETE |
| S081 | PLAN DOC-002 pp53–55 | Version1.4 explicitly adds hemorrhagic stroke and deletes rehospitalization from synopsis. Versioned changes not treated as undisclosed current-report differences. | PASS_1_COMPLETE |
| S082 | PLAN DOC-002 pp55,56,59,60,62 | Doses, windows and DSMC scope agree with report. Optional subsets/extension are not combined with primary denominator. Long-term schedule marks are peripheral. | PASS_1_COMPLETE |
| S083 | PLAN DOC-002 p56 | Version1.4 mixed model includes stroke type and random center: F-ST1-001. n548/610 and MICE reconcile; model change differs from a small power approximation. | PASS_1_COMPLETE |
| S084 | PLAN DOC-002 pp64,67,71,81–84 | Safety composite, windows and classifications retained. Charter thresholds absent, with no reported stopping decision in conflict. Counts cannot be inferred from definitions alone. | PASS_1_COMPLETE |
| S085 | PLAN DOC-002 pp65,68–72 | Primary final3-month FMA and scales coherent. Secondary side comparison F-ST1-006. Loose historical time wording does not define another current primary visit. | PASS_1_COMPLETE |
| S086 | PLAN DOC-002 pp66,67,72–76 | Participant randomization, center strata,80% minimization,610 target and39-day matched regimen coherent. Eligibility differences are versioned amendments. | PASS_1_COMPLETE |
| S087 | PLAN DOC-002 pp75–79 | Dose adaptations, withdrawal data, rehabilitation and central-rating rules retained. No printed result identifies conflicting local versus central primary estimates; no handoff inferred. | PASS_1_COMPLETE |
| S088 | PLAN DOC-002 pp79–81 | Baseline before allocation, Visit2/3 windows, clinical6/12-month and optional telephone24–60-month follow-up coherent. Matrix marks do not establish participant counts. | PASS_1_COMPLETE |
| S089 | PLAN DOC-002 pp84,85 | t-test548, SD25, delta6, two-sided5%, power80%;610×.9=549. Walking45→57 gives12absolute/27relative. PROMIS missing power inputs named. Same check as S008/S075. | PASS_1_COMPLETE |
| S090 | PLAN DOC-002 pp85,87 | No efficacy stopping/interim analysis is consistent with safety monitoring. Unprovided charter boundaries not tested. | PASS_1_COMPLETE |
| S091 | PLAN DOC-002 p86 | All-randomized versus survivor primary: F-ST1-002. Complete cases require observed baseline/3-month FMA; justified reduced-dose PP prevents an assumed exact match to posthoc adherence. | PASS_1_COMPLETE |
| S092 | PLAN DOC-002 p86 | Fixed stroke type/random center: F-ST1-001; additional primary sensitivities: F-ST1-003; center model/graph: F-ST1-004. Terminal(c,d) cross-reference is a pointer, not a new primary population. | PASS_1_COMPLETE |
| S093 | PLAN DOC-002 p87 | Secondary models,95%CIs and two-sided5% coherent. Exploratory genetics/future IPD are not current key results. Secondary missing-data change F-ST1-005. | PASS_1_COMPLETE |
| S094 | PLAN DOC-002 p87 | Participant AE risks differ from reported event counts; no arm incidence inferred. MICE/complete-case rules retained. Substantive analysis changes F-ST1-001/002/005 are distinguished from disclosure dates. | PASS_1_COMPLETE |
