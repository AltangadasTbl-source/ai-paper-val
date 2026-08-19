# Cross-Source Quantitative Consistency Review

## Scope and method

- **Assigned scope completed:** every matched result or definition reconstructed in `extraction/main_quantitative_evidence.md` and `extraction/support_quantitative_evidence.md`, covering the supplied main article (DOC-001), protocol (DOC-002), master/regimen SAP (DOC-003), eMethods/eTables/eFigure (DOC-004), collaborator list (DOC-005), and data-sharing statement (DOC-006).
- **Matching rule:** a difference was considered only after matching regimen (CNM-Au8 Regimen C), population/analysis set, time horizon, contrast/reference group, outcome definition, model, scale/unit, and printed precision. Planned protocol/SAP quantities were not compared as if they were observed results. Where a source distinction explained a difference (for example shared versus regimen-only placebo, FAS versus ERO, or prespecified versus post hoc sensitivity analysis), no candidate was emitted.
- **Direct-source confirmation:** every candidate below was checked against the supplied PDF pages named in its links. Native/layout extractions and evidence maps were locators only.
- **Display-zero rule:** no candidate was generated for a display-zero P value. No matched display-zero result produced an independent supplied-source contradiction in this scope.

## Matched relationships checked without a qualifying difference

- Abstract, Results narrative, Figure 1, and Table 1 regimen randomization/completion counts: 161 randomized, 120 active, 41 regimen placebo, 164 shared placebo where applicable, and 145 regimen-randomized completers reconcile after analysis-set and shared-control matching.
- Primary DRR: abstract/Results/Figure 2/eTable 2 agree at printed precision for DRR 0.97, 95% CrI 0.783 to 1.175, and posterior probability 0.65 versus eTable 2's 0.6450 (the latter rounds to 0.65).
- Secondary SVC and PAV-free survival: Results narrative, Table 2, eTable 3A, and their stated FAS/shared-placebo contrast agree after matching analysis set and model.
- Treatment-emergent AE counts and percentages: abstract, Results narrative, and eTable 5 agree after recognizing that the article uses whole percentages while eTable 5 prints one decimal place and both use the safety denominators 120 and 163.
- The serum-NfL post hoc sensitivity analysis agrees after direction matching: the main article reports active minus placebo as -9.7% (95% CI -18.5% to 0.1%; P=.05), while the eFigure reports placebo minus active as +9.7% (95% CI -0.1% to +18.5%; P=.051). These are direction-reversed displays and P-value precision, not a qualifying difference.
- Protocol and SAP sample sizes, allocation ratios, endpoint definitions, visit schedules, and statistical rules were treated as planned/versioned definitions. Differences from realized enrollment or later versioned documents were not candidates unless a like-for-like observed result contradicted them; none did in the supplied sources.
- DOC-005 and DOC-006 contain no matched quantitative trial result. No supplied structured data, workbook, CSV, or Office source exists.

## Candidate records for human adjudication

### Candidate 1 — Shared-placebo ALSFRS-R credible interval differs between Results narrative and eTable 2

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-001 Results — PDF p. 4](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>); [DOC-004 eTable 2 — PDF p. 15](<../../../joi240158supp3_prod_1742927563.7911.pdf#page=15>).
- **Matched result:** primary Bayesian shared-parameter model, combined CNM-Au8 versus shared placebo, through week 24; ALSFRS-R slope in the shared-placebo component; points per month.
- **Printed values:** DOC-001 reports shared-placebo mean slope **-1.03 points/month (95% CrI -1.176 to -0.892)**. DOC-004 eTable 2 reports the corresponding “Regimen C placebo w/ sharing” slope **-1.03 (SD 0.073), 95% credible interval (-1.181, -0.894)**.
- **Comparison logic:** the point estimate, model label, treatment comparison, placebo sharing, endpoint component, and time horizon match. Both intervals are printed to three decimal places, so the endpoints are not the same displayed values and are not reconciled by the table’s more detailed reporting precision.
- **Supported alternatives:** the two locations may have been generated from different model runs, posterior summaries, data locks, or a postproduction table update. The supplied pages do not identify a different analysis set, model, or cutoff date that would explain the difference.
- **Quality-control relevance:** a data extractor could reproduce different uncertainty bounds for the same primary model parameter.
- **Human verification steps:** inspect the statistical-program output and production files for the primary Bayesian model; identify the dataset lock/model run used for the article narrative and eTable 2; confirm whether either interval was transcribed from a different posterior summary.

### Candidate 2 — Pooled-active ALSFRS-R credible interval differs between Results narrative and eTable 2

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-001 Results — PDF p. 4](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>); [DOC-004 eTable 2 — PDF p. 15](<../../../joi240158supp3_prod_1742927563.7911.pdf#page=15>).
- **Matched result:** primary Bayesian shared-parameter model, combined CNM-Au8 30/60 mg versus shared placebo, through week 24; pooled-active ALSFRS-R slope; points per month.
- **Printed values:** DOC-001 reports pooled-active mean slope **-1.00 points/month (95% CrI -1.153 to -0.858)**. DOC-004 eTable 2 reports pooled CNM-Au8 **-1.00 (SD 0.075), 95% credible interval (-1.143, -0.847)**.
- **Comparison logic:** population, contrast, primary-model component, unit, and time point match. The credible-interval endpoints differ at the common three-decimal displayed precision; the common point estimate does not resolve the interval discrepancy.
- **Supported alternatives:** distinct posterior runs or a table/narrative transcription update could account for the difference, but no supplied-source statement names a different run, data cutoff, population, or summary convention.
- **Quality-control relevance:** the same pooled-active primary-model parameter would have two different reported uncertainty intervals.
- **Human verification steps:** compare the primary-model posterior output used for the manuscript against that used for eTable 2; verify model seed/run, analysis database snapshot, and whether one interval was copied from an earlier output.

### Candidate 3 — Bayesian mortality event rates differ between Results narrative and eTable 2

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-001 Results — PDF p. 4](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>); [DOC-004 eTable 2 — PDF p. 15](<../../../joi240158supp3_prod_1742927563.7911.pdf#page=15>).
- **Matched result:** primary Bayesian shared-parameter function-and-mortality model, combined CNM-Au8 versus shared placebo, through week 24; model-estimated mortality event rate; events/month.
- **Printed values:** DOC-001 states **0.007 events/month** for shared placebo and **0.006 events/month** for pooled CNM-Au8. DOC-004 eTable 2 states **0.010 events/month** for shared placebo (95% credible interval 0.0054 to 0.0154) and **0.009 events/month** for pooled CNM-Au8 (0.0052 to 0.0150).
- **Comparison logic:** DOC-001 explicitly cites eTable 2 for this primary Bayesian model output. The group labels, contrast, model, unit, and time horizon match. Differences of 0.003 events/month in each group cannot arise from the displayed three-decimal precision.
- **Supported alternatives:** a different event definition, posterior run, or reportable time scale might explain the values, but neither cited page supplies such a distinction. The exact source of “mortality” versus the protocol’s composite survival component requires confirmation.
- **Quality-control relevance:** a reader or evidence extractor would obtain materially different model-estimated event rates for the reported primary analysis.
- **Human verification steps:** verify the event definition and time scale in the analysis dataset/code; reconcile the posterior summary in the Results text with eTable 2; document whether one location uses mortality alone and the other uses the composite death/PAV component.

### Candidate 4 — Serum NfL regimen-only results differ between Figure 3/Results narrative and eTable 3B

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-001 Figure 3 and Biomarker Analyses — PDF p. 8](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8>); [DOC-004 eTable 3B — PDF p. 17](<../../../joi240158supp3_prod_1742927563.7911.pdf#page=17>).
- **Matched result:** serum NfL, baseline to week 24, pooled CNM-Au8 (n=120) versus regimen-C placebo (n=41), regimen-only/post hoc analysis; natural-log model back-transformed to percent/geometric-mean-ratio scale.
- **Printed values:** DOC-001 Figure 3 and text report placebo **+30.8%** (43.1 to 56.5 pg/mL), active **+0.4%** (60.6 to 60.8 pg/mL), and treatment difference **-23.2% (95% CI -39.5% to -2.5%; P=.03)**. DOC-004 eTable 3B reports placebo **+26.8%**, active **+0.4%**, and difference **-26.4% (95% CI -50.3% to -2.6%; P=.03)**.
- **Comparison logic:** the main article states that serum NfL was rerun as a regimen-only result because plates differed and directs readers to eTable 3A/3B; eTable 3B identifies the ERO/regimen-placebo analysis, pooled CNM-Au8, log transformation, and the same adjustment covariates. Thus population, contrast, outcome, time, model scale, and displayed P-value match, while placebo change, contrast estimate, and interval differ beyond precision.
- **Supported alternatives:** the figure/text may show a distinct but insufficiently labeled serum-NfL run, or eTable 3B may reflect an updated result. The supplied sources do not name separate plate-selection rules, analysis dates, or covariate specifications for two regimen-only serum analyses.
- **Quality-control relevance:** the reported biomarker effect size and confidence interval could be copied differently into evidence tables or downstream analyses.
- **Human verification steps:** obtain the serum-NfL analysis specification and outputs for Figure 3 and eTable 3B; verify participant/sample inclusion, plate handling, baseline values, model covariates, and whether two distinct regimen-only analyses were intended and labeled.

### Candidate 5 — Plasma NfL confidence intervals vary across Figure 3, Results narrative, and eTable 3B

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-001 Figure 3 — PDF p. 8](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8>); [DOC-001 Biomarker Analyses — PDF p. 8](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8>); [DOC-004 eTable 3B — PDF p. 17](<../../../joi240158supp3_prod_1742927563.7911.pdf#page=17>).
- **Matched result:** plasma NfL, baseline to week 24, pooled CNM-Au8 (n=120) versus regimen-C placebo (n=41), regimen-only analysis; log-transformed model back-transformed to percent/geometric-mean-ratio scale.
- **Printed values:** Figure 3 prints **-9.5% (95% CI -17.8% to -0.5%; P=.04)**. The DOC-001 narrative prints **-9.5% (95% CI -17.8% to -0.4%; P=.04)**. DOC-004 eTable 3B prints **-9.5% (95% CI -18.0% to 0; P=.04)**.
- **Comparison logic:** all three locations identify the same point estimate and P value, and the article directs the reader to eTable 3B for the plasma result. The upper confidence endpoint differs between Figure 3 (-0.5%), narrative (-0.4%), and eTable 3B (0); the lower endpoint in eTable 3B also differs. These cannot all be the same value at their stated displayed precision. No source labels a different plasma population, time point, contrast, model, or confidence level.
- **Supported alternatives:** the table may have rounded its endpoints differently from the figure/text or may have been produced from another run. Exact unrounded intervals are absent, so this cannot determine which printed display should prevail.
- **Quality-control relevance:** the interval’s relation to the null is reported differently across displays, which can affect extraction of the stated uncertainty.
- **Human verification steps:** inspect the plasma-NfL model output and table/figure source files; reproduce the unrounded interval; determine whether `0` in eTable 3B is a rounded endpoint and whether the two Figure 3/text endpoints derive from one or different output versions.

### Candidate 6 — Discussion states 13 RCT events where Table 2 reports 14 matched death/PAV events

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-001 Table 2 — PDF p. 7](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=7>); [DOC-001 Discussion — PDF p. 9](<../../../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=9>).
- **Matched result:** pooled CNM-Au8 and shared-placebo RCT-period death/PAV survival analysis through week 24; event count across both groups.
- **Printed values:** Table 2 reports **5/120** pooled CNM-Au8 and **9/162** shared placebo for PAV-free survival, totaling **14** reported events. The Discussion states that there were “**a total of 13 events** in the RCT period in the shared placebo group and the combined CNM-Au8 groups.”
- **Comparison logic:** the Discussion’s immediately preceding sentence discusses survival benefit for the 30-mg group versus shared and regimen placebo groups, and its “shared placebo group and combined CNM-Au8 groups” language matches Table 2’s pooled-active/shared-placebo comparison. Under the Table 2 event definition (death or PAV) and denominators, 5 + 9 = 14, not 13.
- **Supported alternatives:** the Discussion may intentionally refer to a narrower event definition, a different cutoff, or a subset excluding one event. It does not state such a definition, whereas Table 2 explicitly defines the endpoint as PAV-free survival and supplies the denominators.
- **Quality-control relevance:** an overall event count is a high-value datum for evidence extraction and contextual interpretation of an exploratory survival result.
- **Human verification steps:** identify the event list/cutoff underlying the Discussion sentence; check whether it excludes a baseline PAV, event outside an RCT-period definition, or another pre-specified subset; then align the wording or Table 2 count with the confirmed definition.

## Completion record

- **Matched relationship groups checked:** 39 main-map relationships plus all support-map matches relevant to realized results, including abstract, Results narrative, tables, figures/captions, footnotes, eMethods/eTables/eFigure, protocol definitions, and SAP definitions. Planned-versus-observed and versioned-definition comparisons were screened but not converted into contradictions without like-for-like matching.
- **Raw qualifying candidate records:** 6 (no stable candidate IDs assigned; no AI judgment or disposition assigned).
- **Limitations:** supplied sources contain no raw data, analysis code, run logs, unrounded posterior summaries, or structured datasets. Several protocol/SAP documents are versioned planning documents; they establish matching definitions but cannot on their own settle a difference between observed result displays. Candidate records remain pending human adjudication.
