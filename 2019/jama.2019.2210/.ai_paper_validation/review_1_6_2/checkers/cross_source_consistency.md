# Cross-source consistency review — Workflow 1.6.2

Runtime task ID: /root/cross_checker. Fresh mandatory cross_source_consistency_reviewer, gpt-6.1-sol / medium. Complete assignment: matched REPORT/REPORT, REPORT/PLAN, and PLAN/PLAN relationships across DOC001 pp. 1–9, DOC002 pp. 1–45 (initial and final protocol/SAP and amendments), DOC003 pp. 1–41, and DOC004 p. 1. Source roles follow content: DOC002 PLAN; all other documents REPORT. No supplied structured participant/result file exists. Sources and reusable assets were preserved; no legacy scientific conclusions or external sources were read.

Read completely: QUALITY_CONTROL_SCOPE.md, workflow_1_6_2/review_contract.md, settings.toml, tooling_record.md, source_inventory.md, source_coverage.md, and the complete main_checking_map, support_core_checking_map, support_figures_a and support_figures_b. These maps cover all 96 pages. Direct Poppler pdftotext from source PDFs verified cited statements on main pp. 2–3 and 7, and plan pp. 19, 25, 31 and 45. CPU Poppler pdftoppm source renders at 100 dpi were created and visually inspected for main p. 3 and plan pp. 25 and 31; the source-linked reusable main p. 7 render was visually inspected. New derivatives: preprocessing/cross-main-p3.png, preprocessing/cross-plan-p25.png, preprocessing/cross-plan-p31.png. No OCR required. These direct-source checks resolve transcription; the independent rechecker will reread every registered location.

## Complete comparison coverage

The following 35 concept groups are the cross-source shard; composite rows retain every item or result occurrence in the named keyed map groups. Thus the shard remains below 120 cross-source relationships and does not require further division. This cross-source lane does not duplicate the statistical lane's row-by-row arithmetic/test reconstruction. Every matched occurrence is checked after matching population, time origin, contrast, model, measure, analysis set and printed precision. COMPLETE means comparison completed, including a finding or a screened-out apparent issue; it is not an adjudication.

| Group | Exact mapped scope and comparison | Record | Status |
|---|---|---|---|
| XS01 | M001–M002, M010–M014, M026–M029; P002–P003/P044: single-center individual randomization, 3:2 allocation, blocks of 5, all ten block orders, 251/166 and 417 | Allocation and individual trial unit reconcile; target 400 is an enrollment target, not an asserted observed total | COMPLETE |
| XS02 | P004–P006/P001, M011/M014/M104: initial 1200, initial capsule paragraph 1000, final 2000, amendment date and treatment duration | Final 2×1000 and report 2000 agree; initial comparison in exclusions | COMPLETE |
| XS03 | P007, M012: all six eligibility items individually—histopathology/site, clinical I–III, age, diagnosis/first surgery center, no vitamin D, no urinary stones | Six matched items reconcile; epidermal/epithelial naming and registration-form boundary in exclusions | COMPLETE |
| XS04 | P008, M012/M001/M026: all four exclusion items individually—non-total resection, serious pre-supplement postoperative complications, non-epithelial pathology, pathological 0/IV | Four criteria and pre-randomization exclusion context reconcile | COMPLETE |
| XS05 | P009/P018, M003/M015/M032/M067/M106: primary composite components, time origin, event/censor criterion list item by item | Start medication and randomization coincide in report; earliest relapse or any-cause death matches; censor wording in exclusions | COMPLETE |
| XS06 | P010/P012, M006/M015/M033/M068: OS/all-cause death definitions and time origins | Same any-cause-death outcome; OS duration versus death incidence are distinct representations | COMPLETE |
| XS07 | P011/P013/P014/P046, M015/M034/M081–M089: relapse, primary-cancer death, non-primary death definitions and form classification | Relapse matches; cancer-specific/noncancer wording observation in exclusions; model change in F-XS-003 | COMPLETE |
| XS08 | P015–P017, M015/M098–M103: every tertiary/safety item and final synopsis versus body/amendment | F-XS-001 for de novo status; urinary stone, hypercalcemia, fracture, admission-event definitions otherwise reconcile | COMPLETE |
| XS09 | P031–P032, M020/M067/M068/M091–M094: primary and OS analysis population, curve method, Cox model, confidence level | ITT/Cox/95% match; curve method F-XS-002 | COMPLETE |
| XS10 | P033, M023/M069/M081–M083/M098–M103: relapse/safety analysis effect measure | F-XS-003 | COMPLETE |
| XS11 | P019/P038, M023/M024/M070/M071/M105: covariates, missingness, imputation, PH checks, sensitivity methods | Adjusted age/stage, MI and PH checks explicitly post hoc; no unsupported prespecification claim; exclusions explain absent plan details | COMPLETE |
| XS12 | P037/P035, M021/M035/M056/M091–M095: baseline subgroup boundaries, three planned groups, interaction/multiplicity | Low/middle boundaries and exploratory interpretation match; high-group omission F-XS-004 | COMPLETE |
| XS13 | P021/P022/P036, M018/M021/M059–M065/M039; FA026–FA040/FB001–FB006: seven prespecified loci and all 21 genotype labels/statuses | Final plan names all seven loci; captions prespecified; FokI/CDX2 nomenclature observation in exclusions | COMPLETE |
| XS14 | P035/P034, M021/M022, all FA/FB interaction records: interaction construction, two-sided .05 level and multiplicity | Multiplicative interactions match; unadjusted subgroup testing and exploratory caution agree; no margin/noninferiority rule supplied | COMPLETE |
| XS15 | P025–P027/P002, M019: sample-size/power inputs, allocation, historical assumptions, initial/final version amendments | Final N400, 240/160, 75%/62%, .05, 80%, 1% match report; initial blank SAP acknowledged by amendment; numerical reproduction assigned statistical lane | COMPLETE |
| XS16 | P023/P024/P028, M019/M022/M029: accrual target, follow-up, all interim/stopping/success rules | >400 enrollment/annual interim after 200/.001 Peto match; three interims report no boundary met; planned versus actual duration distinction in exclusions | COMPLETE |
| XS17 | P039/P040, M016/M027–M029/M103: follow-up after medication stops, ascertainment, adherence and safety sets | Continued outcome follow-up matches; safety PP is explicitly reported and no contradictory plan safety set supplied | COMPLETE |
| XS18 | M005/M009/M010/M032/M067/M104/M106: abstract, Key Points, narrative, graph, discussion and conclusion primary results | 50/43, 77%/69%, HR .76 (.50–1.14), P .18 and null conclusion match | COMPLETE |
| XS19 | M006/M033/M068: abstract/body/figure OS | 37/25, 82%/81%, HR .95 (.57–1.57), P .83 match | COMPLETE |
| XS20 | M007/M037/M091: abstract/body/figure middle-baseline primary result | 85%/71%, HR .46 (.24–.86), P .02, interaction .04 match | COMPLETE |
| XS21 | M035/M056/M092–M094/M038: other baseline subgroup counts, outcomes and measures | Low/middle populations, HR/CI/P match; high count 5 matches omitted-group statement | COMPLETE |
| XS22 | M034/M069/M072/M081–M089: all Table 2 component outcomes and narrative counterparts | Total/middle/low relapse effect estimates and test values agree; direction footnote F-XS-005 | COMPLETE |
| XS23 | M008/M080/M098–M103: every repeated safety count, denominator and analysis-set label | Abstract fracture 3/5 and stone 2/0 match until-censoring set 227/147; other Table 3 sets are explicitly distinct | COMPLETE |
| XS24 | M024/M039/M056/M105; FA021–FA025: seven baseline missing and four MI subgroup outcome rows | 3+4=7; 248+162=410 baseline observed; complete-case and imputed HR/CI/P copies match at printed precision | COMPLETE |
| XS25 | M025/M076, FA001–FA019: achieved-average five-bin populations, two graph annotations and all table models | Graph .29 (.11–.74) P .01 and .39 (.18–.84) P .02 match unadjusted table counterparts; adjusted counterparts kept distinct; achieved mean distinct from baseline | COMPLETE |
| XS26 | P020/P029, M016/M017/M025/M036/M074–M079, FA020: longitudinal assay, annual month, median/IQR, within/between tests | Time/units, increased vitamin-D direction and stable placebo match; graph approximate values not compared as exact printed copies | COMPLETE |
| XS27 | M040–M041/M066/M031, FB007–FB010: sex and age subgroup counts/statuses | Men173/103, women78/63, ≤65=106/91, >65=145/75 match table sums; all post hoc labels match main | COMPLETE |
| XS28 | M042/M051–M055/M073, FB011–FB020: BMI, site, stage and pathology subgroup definitions/statuses/counts | Available-data BMI249/165 and all site/stage/pathology arm counts reconcile; site omits two small-bowel patients consistently; main identifies analyses post hoc | COMPLETE |
| XS29 | M059–M065, FA026–FA040/FB001–FB006: every genotype risk-table baseline count versus table genotype count | All copies match except DBP1 TG57/59, handled under display precision in exclusions | COMPLETE |
| XS30 | M039/M073, FA026–FA040/FB001–FB020: main statements on SNP and post hoc interaction nonsignificance | All displayed numeric interaction P values exceed .05; within-men P=.04 is a within-subgroup treatment test, not an interaction conflict | COMPLETE |
| XS31 | M090/M020/M032/M069/M072/M081–M089: treatment-reference/direction labels | F-XS-005 | COMPLETE |
| XS32 | M067–M069/M091–M097 and all figure captions/risk tables: time/risk-set/axis quantity matching | Cumulative hazard versus cumulative incidence kept distinct; Figure 3C caption/risk-table observation excluded | COMPLETE |
| XS33 | P001/P016/P022/P037/P045/P049: all amendment/version statements, outcome statuses, form criteria and result contents | Disclosed dose/sample-size/subgroup/DBP amendments respected; version label/date and form peripheral items excluded | COMPLETE |
| XS34 | M001–M002/M004/M029–M031/M066: abstract baseline/flow/follow-up summaries and main table/figure copies | Flow 439−22=417 and exclusion timing reconcile; mean versus median age and follow-up distribution differences are nonmatching summaries | COMPLETE |
| XS35 | M107/P042–P050 and all no-applicable source units: references, molecular operations, blank forms, funding, sharing | All mapped content reviewed for prospective criterion or result definition; no additional result/design conflict. No supplied raw structured data to match | COMPLETE |

## Findings

### F-XS-001

**Title:** De novo cancer has tertiary status in the final protocol body but safety/adverse-event status in the final synopsis and report.

**Compared locations and document roles:** PLAN [final protocol p. 25, Tertiary outcome](../../../joi190023supp1_prod.pdf#page=25); PLAN [amendment summary p. 45, Double (triple) cancer incidence](../../../joi190023supp1_prod.pdf#page=45); PLAN [final synopsis p. 19, Outcomes](../../../joi190023supp1_prod.pdf#page=19); REPORT [main pp. 2–3, Outcomes](../../../jama_urashima_2019_oi_190023.pdf#page=3) and REPORT [Table 3 p. 8](../../../jama_urashima_2019_oi_190023.pdf#page=8). The initial synopsis [PLAN p. 4](../../../joi190023supp1_prod.pdf#page=4) supports the earlier adverse-event status, not the final-body tertiary status.

**Printed statements and values:** Final body lists de novo cancer in organs other than the primary site after supplementation as a “Tertiary outcome.” Amendment says it was separated from secondary and safety outcomes and inserted as tertiary on 2012.12.8. Final synopsis says it is included as an adverse event, “not as an outcome.” Report's safety-outcome list includes this same de novo cancer definition. Table 3 reports de novo cancer 15/8 in continuing-to-censoring PP, 16/9 in >1-year PP, and 16/9 in randomized sets, with percentages 6.6/5.4, 6.6/5.6 and 6.4/5.4.

**Comparison logic:** Match organ restriction, post-supplement start and de novo definition. The same endpoint is explicitly given different hierarchical statuses; the amendment expressly separates tertiary from safety. This is a categorical comparison, so numerical display precision is not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationships:** P_R and P_P; primary P_R by precedence.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Outcome-status extraction and the analysis-population interpretation of Table 3's de novo cancer counts.

**Why context does not resolve it:** Category 5 registers a prespecified outcome-status change. The supplied amendment states tertiary status, but the final synopsis and report retain adverse-event/safety status without identifying which hierarchy governed reporting.

**Supported alternatives:** The final synopsis may retain the earlier status; the report may intentionally present the tertiary endpoint within a safety table; a later status amendment may exist but is not supplied. Each is an interpretation, not an observed fact.

**Exact human question:** Was de novo cancer a tertiary efficacy endpoint or a safety/adverse-event endpoint in the final analysis, and what supplied amendment or reporting decision explains its status and corresponding analysis sets?

### F-XS-002

**Title:** Planned Kaplan–Meier primary/OS curves are replaced by reported Nelson–Aalen cumulative hazards.

**Compared locations and document roles:** PLAN [initial SAP p. 14](../../../joi190023supp1_prod.pdf#page=14); PLAN [final synopsis p. 19](../../../joi190023supp1_prod.pdf#page=19); PLAN [final SAP p. 31, methods c–d](../../../joi190023supp1_prod.pdf#page=31); REPORT [main p. 3, Statistical Analysis](../../../jama_urashima_2019_oi_190023.pdf#page=3); REPORT [Figure 2A–B and caption p. 6](../../../jama_urashima_2019_oi_190023.pdf#page=6); REPORT [Figure 3 and caption p. 7](../../../jama_urashima_2019_oi_190023.pdf#page=7). The amendment summary [PLAN p. 45](../../../joi190023supp1_prod.pdf#page=45) lists no curve-method amendment.

**Printed statements and values:** SAP c says “Kaplan-Meier survival curves will be created on an intent-to-treat analysis.” Report says effects on relapse/death and total deaths were estimated using Nelson–Aalen cumulative hazard curves; figures and captions explicitly use cumulative hazard. Report primary HR .76 (.50–1.14), P .18 and OS HR .95 (.57–1.57), P .83 are the same Cox targets planned in method d; the conflict concerns method c, not those Cox copies.

**Comparison logic:** Match randomized ITT population, primary relapse/death and OS time-to-event endpoints and time origin. Kaplan–Meier survival and Nelson–Aalen cumulative hazard are distinct estimators/quantities. No Kaplan–Meier result or disclosed curve-method amendment appears in the complete report maps. Categorical method comparison; numerical display precision not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecified primary and key-secondary survival-curve method; identification of the estimator underlying survival versus hazard displays and the reported 5-year survival percentages.

**Why context does not resolve it:** Category 5 registers a planned primary/key-secondary analysis replaced or not reported. The report clearly labels its curves, but does not state whether planned Kaplan–Meier estimation was retained for the 5-year percentages or amended.

**Supported alternatives:** Kaplan–Meier may have produced the percentages while Nelson–Aalen was used only for presentation; method c may have been amended after the supplied SAP. Neither explanation is supplied explicitly.

**Exact human question:** Were the planned Kaplan–Meier analyses performed, including estimation of the 5-year relapse-free/overall survival percentages, and what explains the replacement of their planned curve displays by Nelson–Aalen cumulative hazards?

### F-XS-003

**Title:** Planned relapse/safety risk-ratio analyses are not the effect measures reported for those outcomes.

**Compared locations and document roles:** PLAN [initial SAP p. 14, method e](../../../joi190023supp1_prod.pdf#page=14); PLAN [final SAP p. 31, method e](../../../joi190023supp1_prod.pdf#page=31); REPORT [main p. 3, Statistical Analysis/post hoc analysis](../../../jama_urashima_2019_oi_190023.pdf#page=3); REPORT [Figure 2C p. 6](../../../jama_urashima_2019_oi_190023.pdf#page=6); REPORT [Table 2 p. 7](../../../jama_urashima_2019_oi_190023.pdf#page=7); REPORT [Table 3 p. 8](../../../jama_urashima_2019_oi_190023.pdf#page=8).

**Printed statements and values:** Both SAP versions method e specify relapse and safety outcomes evaluated using “risk ratio (RR).” Report calls relapse competing-risk/subdistribution-HR analysis post hoc. Total relapse subdistribution HR .75 (.48–1.17), P .21; baseline low 1.18 (.64–2.19), P .59; middle .44 (.21–.89), P .02. Safety Table 3 gives counts/percentages in three explicit analysis sets, with no reported RR. Across the complete report maps, no relapse or safety RR analysis is reported.

**Comparison logic:** Match relapse incidence and safety definitions before comparing measure identity. Risk ratio and subdistribution hazard ratio are different measures; a post hoc HR does not identify whether the planned RR was retained. Safety descriptive counts are not a reported RR analysis. This is a categorical method/prespecified-analysis comparison, not a discrepancy between an adjusted estimate and a crude calculation; no crude ratio is offered as a substitute. Numerical display precision is not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** Relapse effect-measure extraction and identification of the prespecified treatment comparisons for the reported relapse and safety outcomes.

**Why context does not resolve it:** B1: explicit planned/report statistical analysis specification. B2: the post hoc label identifies the reported competing-risk analysis but does not identify the status of the planned RR analysis. B3: these alternatives estimate different quantities and the effect measure selected for extraction can change. The safety observations share the same SAP method-e pattern and are consolidated rather than emitted separately.

**Supported alternatives:** RRs may have been calculated but omitted, or the method may have been amended; safety may have been deliberately restricted to descriptions. No amendment covering method e is identified in the supplied amendment list.

**Exact human question:** Were the prespecified relapse and safety RR analyses conducted and retained, or replaced/omitted, and what analysis amendment or reporting decision establishes which effect measures apply?

### F-XS-004

**Title:** The prespecified high-baseline vitamin-D subgroup of the primary outcome was not analyzed.

**Compared locations and document roles:** PLAN [final SAP p. 31, subgroup list i and interaction rule](../../../joi190023supp1_prod.pdf#page=31); PLAN [amendment summary p. 45](../../../joi190023supp1_prod.pdf#page=45); REPORT [main p. 3, Statistical Analysis](../../../jama_urashima_2019_oi_190023.pdf#page=3); REPORT [Table 1 p. 5](../../../jama_urashima_2019_oi_190023.pdf#page=5); REPORT [Figure 3 caption p. 7](../../../jama_urashima_2019_oi_190023.pdf#page=7); REPORT [limitations p. 8](../../../jama_urashima_2019_oi_190023.pdf#page=8).

**Printed statements and values:** SAP lists low <20, middle ≥20 to ≤40 and high >40 ng/mL and interaction evaluation for listed subgroups. Amendment records the 20/40 cutoffs introduced after trial start and before first interim. Report calls all three groups prespecified, but specifies two-way low/middle interactions only, excluding high because small n. Table 1 high counts are 4 vitamin D and 1 placebo. Figure 3 caption says the high group had only 5 patients and “was not evaluated.” Limitations repeats its insufficient number.

**Comparison logic:** Three named planned baseline groups versus two evaluated groups for the primary relapse/death subgroup analysis. The five-person count and the reason for omission are disclosed; no small-subgroup exclusion criterion is supplied in the SAP. Categorical analysis-scope comparison; display precision does not apply.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Scope of prespecified primary-outcome subgroup analysis and interpretation of the reported low/middle interaction P=.04.

**Why context does not resolve it:** Category 5 registers a planned primary-outcome analysis not reported. The disclosed practical reason is recorded as context; it does not change the fact that the planned group is absent from the analysis. This finding does not propose analyzing five patients or challenge that choice.

**Supported alternatives:** An analysis amendment or minimum subgroup-size rule may have authorized the omission; neither appears in the supplied plan. Report may intentionally regard this as a disclosed departure.

**Exact human question:** Was the omission of the prespecified >40 ng/mL primary-outcome subgroup and restriction to low/middle interaction an amended analysis rule or a reporting decision, and how should that change be recorded?

### F-XS-005

**Title:** Table 2's printed HR direction statement reverses the treatment contrast used for the reported values.

**Compared locations and document roles:** REPORT [Table 2 footnote a and all outcome rows p. 7](../../../jama_urashima_2019_oi_190023.pdf#page=7); REPORT [main p. 3, analysis contrast](../../../jama_urashima_2019_oi_190023.pdf#page=3); REPORT [p. 6, relapse narrative and Figure 2C](../../../jama_urashima_2019_oi_190023.pdf#page=6); REPORT [Figure 3 p. 7](../../../jama_urashima_2019_oi_190023.pdf#page=7).

**Printed statements and values:** Footnote a says “Hazard ratio (HR) values greater than 1 indicate that vitamin D supplementation was associated with a decreased probability of the outcome.” Table 2 relapse subdistribution HRs are .75 total, 1.18 low and .44 middle; cancer-specific-death HRs 1.09, 1.45, .78; noncancer-death HRs .70, 1.11, .39. Main p. 6 identifies middle relapse HR .44 (.21–.89), P .02 as significantly lower under vitamin D. Figure 3 middle relapse/death HR .46 (.24–.86) is accompanied by the lower vitamin-D cumulative-hazard curve.

**Comparison logic:** The report treatment contrast and lower-than-one benefit interpretation establish vitamin D relative to placebo for adverse-event outcomes. The footnote instead attributes decreased outcome probability to greater-than-one ratios. This is a direction/reference-group conflict, not rounding or a absent symbol. All nine Table 2 estimates are affected by the shared direction rule; no nine-fold finding duplication is made. Numeric copies themselves match, so recomputed-copy intervals have zero discrepancy; the reproduced conflict is categorical reversal, for which numerical display precision is not applicable.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** Direction coding of the nine Table 2 relapse and cause-specific-death estimates, including the middle-baseline relapse HR .44.

**Why context does not resolve it:** Category 2 registers printed direction/reference statements that reverse the values. Adjacent figures/narrative supply an alternative intended interpretation but a reader can still extract the printed footnote direction.

**Supported alternatives:** The footnote may have intended values below 1; alternatively it may assume a reversed treatment reference, which does not reconcile with the report's .44 lower-relapse statement. No final replacement wording is proposed.

**Exact human question:** What treatment reference and effect direction should apply to Table 2's HR/subdistribution-HR values, given the greater-than-one decreased-probability statement and the narrative/figure interpretation of values below 1?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| PLAN pp. 9/12/25/28/45 | Initial intervention 2×600 IU differs from initial capsule paragraph 1000 IU; the reviewed final dose and report agree at 2×1000=2000 and amendment explicitly records pretrial increase | CONTEXT_RESOLVES |
| PLAN p. 23 versus p. 31 | High group's design parenthesis prints 40 ng/mL without a comparator; complete low/middle categories and SAP's >40 define the intended boundary immediately | NOTATION_OR_TYPOGRAPHY |
| PLAN pp. 9/24/38 and REPORT p. 2 | Registration form age30≤<90 versus narrative age30–90, additional consent/surgeon-judgment checkboxes versus numbered criteria; no demonstrated change to randomized or analyzed population | PERIPHERAL_COMPARISON |
| PLAN pp. 9/24 and REPORT p. 2 | Epidermal versus epithelial carcinoma labels, with identical anatomical sites and exclusion examples | TERMINOLOGY_OR_WORDING |
| PLAN pp. 13/29 versus pp. 9/25 | Follow-up paragraph says relapse-free “or alive,” whereas explicit primary definition requires no relapse and alive; clear primary definition resolves intended composite censoring wording | TERMINOLOGY_OR_WORDING |
| PLAN pp. 10/25/41 and REPORT pp. 2/7 | “Non-cancer” plan examples include de novo cancer progression; report says noncancer death while plan explicitly distinguishes primary from non-primary cancer deaths; no source result/count demonstrates reallocation | TERMINOLOGY_OR_WORDING |
| PLAN pp. 12/27 and REPORT p. 3; REPORT supplement pp. 13–15 | FokI rs10735810 versus rs2228570 and CDX2 versus CDK2 labels; matching locus/genotype/sample groups identify intended subgroup, with no different numeric outcome assignment demonstrated | TERMINOLOGY_OR_WORDING |
| PLAN pp. 17/45 | Final cover printed version1 versus amendment-history version3; dates establish supplied final version and no analysis rule differs solely because of version numbering | PERIPHERAL_COMPARISON |
| PLAN pp. 45 and 17/18 | DBP/de novo amendment dates2012.12.8 versus final-version/subgroup date2012.12.18; calendar detail does not establish a changed decision rule or result | PERIPHERAL_COMPARISON |
| PLAN pp. 3/14/18/30/45 | Initial blank sample-size SAP versus initial synopsis400; final amended400 is supplied and report relies on final calculation, so initial-document residual does not alter reported plan assumptions | CONTEXT_RESOLVES |
| PLAN pp. 30–31 and REPORT pp. 3–4 | Planned80/year×5 accrual and7-year total versus actual enrollment January2010–April2016 and follow-up2018; the former are explicitly planning assumptions, latter observed calendar | CONTEXT_RESOLVES |
| PLAN p. 31 and REPORT p. 3/supplement eTable2 | Missing-data exclusion/MI, age/stage adjustment and PH checks absent from SAP; report explicitly labels these analyses post hoc, so absence alone creates no prespecification conflict | CONDITIONAL_OR_UNREPORTED |
| REPORT p. 7 Figure3C caption and risk table | Caption says panelC risk numbers not given because weighting; displayed risk numbers are present, but the pointer/text does not change a primary/key-secondary estimate or starting analysis-population count | PERIPHERAL_COMPARISON |
| REPORT p. 5 DBP1 TG and supplement p. 23 | Placebo genotype count57 versus starting risk count59: half-unit intervals[56.5,57.5] and[58.5,59.5], gap1; reference57 gives relative discrepancy1/57=.01754≤.05 | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT abstract p. 1 and narrative p. 4 | Age66 is explicitly mean in abstract and median in narrative; these are separate summaries and the package does not establish either value as the other's copy | NOT_REPRODUCED |
| REPORT supplement p. 6 versus main p. 7 | MI subgroup estimates/CI/P equal complete-case printed results at displayed precision; equality alone does not establish a conflict with the imputation claim | CONDITIONAL_OR_UNREPORTED |

## Completion and limitations

Five findings, sixteen excluded observations, and thirty-five complete matched-concept comparison groups. The four source roles and all 96 mapped pages enter this review. Historical background, references, blank administrative forms and sharing statements have no additional eligible quantitative comparison. The report supplies no row-level data, exact curve coordinates, exact longitudinal box-plot summaries, further analysis amendments, or full interaction contrast definitions; none was inferred. Missing details alone were not made findings. Statistical method reproduction and row-level estimate/test compatibility are independently owned by the two statistical passes. No scientific-coverage gap in assigned cross-source scope. Every finding remains a finding for independent inclusion screening; no C IDs, severity, disposition or correction is assigned here.
