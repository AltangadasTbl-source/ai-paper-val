# Mechanical evidence recheck — Workflow 1.6.2

Runtime agent ID: 01a12967-ce19-7870-ab5f-360c3a26c7a7. Fresh qc162_evidence_rechecker; gpt-6.1-sol/high; FRESH_SPAWN. Scope: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, including all registered locations and all three occurrences of the C011 pattern. The 19 included checker findings were traced through the current inclusion screen and complete candidate ledger. QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely.

All eleven assigned IDs remain Pending Human Adjudication. Evidence states below record source observations, not dispositions. No source or earlier reusable asset was modified, and no legacy candidate or report was used as a scientific input. No source needed for a registered location was inaccessible.

## Source authority and absence-check scope

Direct sources were checked with `sha256sum -c .ai_paper_validation/review_1_6_2/source_hashes_before.sha256`; all five matched. Source authority was the visually read rendering of each exact supplied PDF page, identified by its one-based PDF page; native/layout text served only as a locator and for complete text searches. Existing initial-screen images were created directly from the same supplied sources, as recorded in screening/inclusion_screen.md, with CPU Poppler 26.01.0. The rechecker visually reread main pp. 1, 2, 3, 4, 6, 7, 8; protocol pp. 8, 9, 16, 17, 18, 20, 23, 28, 43, 44; SAP pp. 2, 3, 4, 5; results supplement pp. 3, 4, 15, 16, 18, 19, 20, 21, 22. These 30 reused current-run page images are under preprocessing/initial_screen/ and are tied to the source/engine register in the screen. They are faithful views of the supplied PDF, not authority independent of that PDF.

Additional direct CPU renderings were made with `pdftoppm -f N -l N -r 100 -singlefile -png SOURCE OUTPUT`, Poppler 26.01.0: DOC-004 p. 14 to preprocessing/evidence_recheck/support-p14.png; DOC-004 p. 17 to preprocessing/evidence_recheck/support-p17.png; DOC-001 p. 9 to preprocessing/evidence_recheck/main-p9.png; DOC-005 p. 1 to preprocessing/evidence_recheck/sharing-p1.png. All four were visually read. No OCR, GPU or fallback capability was needed; compute device remained CPU as recorded in tooling_record.md.

For C002, C008 and C009, the full current-source REPORT texts were read/searched across DOC-001 pp. 1–11, DOC-004 pp. 1–25 and DOC-005 p. 1. Searches included RERI, additive, sensitivity, Kaplan, log-rank, mixed model, survival, Cox, MDD and imputation. All analysis/result occurrences relevant to an absence claim were reread in the supplied-source page views: main pp. 1, 4, 6–9; supplement pp. 14–15 and 17–22; sharing p. 1. Main Table 1 and the supplement's adherence/concealment tables describe baseline, exposure or concealment, rather than the absent model/estimand; source maps and full text contain no unlocated additional MDD inference display. The appendix-9 graphic was visually checked because its plotted labels are not fully represented by text extraction: it supplies descriptive PHQ/IDS/GAD/utility trajectories, not a repeated-MDD or survival analysis. References and administrative pages add no analysis results. Absence is bounded to these supplied REPORT sources, not to material outside the package.

## Recheck classification summary

The content-based source roles are REPORT for the retrospective main article, results supplement and publication-associated sharing statement; PLAN for the prospective protocol and SAP. Physical supplement numbering does not determine role. Classification fields are confirmed for every ID; no role, primary relationship, all-relationships or domain change is required. P_R takes precedence over P_P, S_C and S_W; P_P over S_C and S_W; S_C over S_W. Corroboration is excluded from the relationships counted.

| ID | Evidence state | Review domain | Relationship type | All relationships | Determining recheck fact |
|---|---|---|---|---|---|
| C001 | reproduced | protocol_report | P_R | P_R | Matched daily EPA+DHA amounts remain separated beyond precision and the printed manufacturing allowance. |
| C002 | reproduced | protocol_report | P_R | P_R, P_P | The protocol primary suite differs from the SAP suite; specified primary Kaplan–Meier/log-rank and repeated-MDD analyses are not supplied as such in REPORT. |
| C003 | reproduced | statistical_results | S_C | S_C, S_W | Figure 1 prints online BMI <15, while the same-stage results appendix explicitly specifies 25–40. |
| C004 | reproduced | statistical_results | S_W | S_W | Four 196-participant combinations cannot reconcile with a printed total of 392. |
| C005 | reproduced | protocol_report | P_R | P_R | Planned active incidence 15% and group requirement 180 differ from reported 20% and 196 beyond display precision. |
| C006 | reproduced | protocol_report | P_R | P_R, P_P | Protocol main/primary IDS status differs from SAP/report secondary status. |
| C007 | reproduced | protocol_report | P_R | P_R, S_W | Supplied plans specify Cox and site/history analyses while REPORT applies post hoc designations, including an internal Methods/Results scope difference. |
| C008 | reproduced | protocol_report | P_R | P_R | The explicit primary RERI/additive sensitivity commitment has no matching supplied REPORT result. |
| C009 | reproduced | protocol_report | P_R | P_R | The SAP primary-MI paragraph promises reported missing-mechanism sensitivity; supplied sensitivity displays cover secondary scores, not primary MDD. |
| C010 | reproduced | statistical_results | S_C | S_C, S_W | The printed original-effect/complier-proportion explanation does not specify a mapping that reconciles the named ITT and CACE ORs. |
| C011 | reproduced | statistical_results | S_W | S_W | All three site coefficients exceed 0.05 relative gaps from rounded CI midpoints under the centered relationship that reproduces the six other nonreference rows. |

No registered value or location needed a transcription correction. Numerical intervals below allow each displayed input its own half-unit precision and the printed comparison quantity its own half-unit precision. A categorical specification or absent result has no meaningful numeric rounding interval; this is stated separately for each applicable ID.

## C001 — Planned and reported daily EPA+DHA dose

**Finding provenance:** F-NUM-002, F-XS-002. **Location found / source and comparator matched:** Yes for each location below; all were visually read.

| Exact supplied-source location | Role confirmed by content | Matched source text/value and role in comparison |
|---|---|---|
| [Main p. 1, abstract Interventions](../../../jama_bot_2019_oi_190007.pdf#page=1) | REPORT | Daily supplements contain 1412-mg omega-3 fatty acids, administered for one year. |
| [Main p. 2, Multinutrient Supplements](../../../jama_bot_2019_oi_190007.pdf#page=2) | REPORT | 1412 mg eicosapentaenoic and docosahexaenoic omega-3 fatty acids, ratio 3:1; two pills per day, one year. |
| [Results supplement p. 4, eAppendix 2](../../../joi190007supp3_prod.pdf#page=4) | REPORT | Two daily pills; one oil capsule with 1412 mg EPA+DHA at ratio 3:1 and a separate vitamin/mineral pill. |
| [Protocol p. 8, Summary intervention](../../../joi190007supp1_prod.pdf#page=8) | PLAN | One capsule and one pill; omega-3 fatty acids 1000 mg per capsule, EPA/DHA ratio 3:1, EPA >700 mg and DHA >100 mg. |
| [Protocol p. 18, intervention box](../../../joi190007supp1_prod.pdf#page=18) | PLAN | Two pills daily for one year; 1000 mg omega-3 per capsule, the same EPA/DHA description. |
| [Protocol p. 20, composition box](../../../joi190007supp1_prod.pdf#page=20) | PLAN | Fish-oil composition and acceptable deviation 90%–125%; separate composition document C1.2 is referenced. |
| [Protocol p. 23, Omega-3 PUFA fish oils](../../../joi190007supp1_prod.pdf#page=23) | PLAN | Explicit intended dose EPA+DHA = 1.0 g per day, establishing the matched active chemical quantity. |

**Consistency rule applicable / calculation reproduced:** Yes. Compare the same daily EPA+DHA dose after g-to-mg conversion. The conservative PLAN interval from 1.0 g is [950,1050] mg; REPORT 1412 is [1411.5,1412.5] mg. Gap = 361.5 mg, relative discrepancy 361.5/1412 = 0.256020. Even generously extending the 125% upper allowance to 125.5% gives a PLAN upper limit 1050 × 1.255 = 1317.75 mg. Remaining gap = 93.75 mg; 93.75/1412 = 0.066395 >0.05. This already allows the broadest printed PLAN dose interval; the 1000-mg display is narrower. Route B applies to intervention dose under focus D and exposure extraction for primary MDD.

**Necessary inputs available / exact missing inputs:** The daily regimen, matched EPA+DHA quantity, units and manufacturing allowance are available. The operative final formulation specification, supplied contents of C1.2, capsule-mass basis and documented amendment connecting 1.0 g to 1412 mg are unavailable. Laboratory FAME fractions mentioned elsewhere do not themselves identify a changed daily target or total capsule mass.

**Source-grounded alternative interpretation:** A changed formulation or a manufacturing/composition basis could explain the reporting difference. Protocol p. 23 and results-supplement p. 4 both explicitly identify EPA+DHA, so total oil versus active-fatty-acid terminology alone does not reconcile those two statements.

**Direct observation versus inferred explanation:** The different printed daily amounts and residual gaps are direct observations. A formulation revision, release specification or production mechanism is an inferred possible explanation, not established by this recheck.

**Classification confirmation / ambiguity:** Primary P_R; all P_R; domain protocol_report. PLAN intervention specifications conflict with retrospective REPORT exposure descriptions. Concordant main/supplement values do not add S_C; concordant PLAN dose occurrences do not add P_P. Ambiguity concerns the governing formulation/amendment, not the content-based roles.

**Evidence state:** reproduced. The source-matched EPA+DHA amounts still exceed the display rule after the stated allowance.

**Exact remaining human question:** Which specification governed the final daily EPA+DHA dose, and which documented formulation amendment or dose basis reconciles the protocol's 1.0 g/day with the reported 1412 mg/day?

## C002 — Planned primary analysis suite

**Finding provenance:** F-XS-005, F-ST1-004. **Location found / source and comparator matched:** Yes for every below-cited location; visually confirmed.

| Exact supplied-source location | Role | Matched specification or reported analysis |
|---|---|---|
| [Protocol p. 43, §§10.1–10.2](../../../joi190007supp1_prod.pdf#page=43) | PLAN | Primary parameters: Kaplan–Meier, log-rank and Cox for MDD time-to-event; two-way and four-way comparisons; country/history adjustment; additional mixed models across baseline, 3, 6 and 12 months for MDD onset and IDS, accounting for repeated observations and country clustering. |
| [SAP p. 2, Outcomes](../../../joi190007supp2_prod.pdf#page=2) | PLAN | Primary outcome is cumulative MDD since baseline, yes/no; IDS is secondary. |
| [SAP p. 3, Fourth analysis](../../../joi190007supp2_prod.pdf#page=3) | PLAN | Effect-coded logistic primary analysis with main effects/interactions; mixed models or GEE for secondary continuous outcomes. |
| [SAP p. 4, Secondary analysis](../../../joi190007supp2_prod.pdf#page=4) | PLAN | Cox time-to-MDD is a secondary analysis. |
| [Main p. 1, abstract main measures](../../../jama_bot_2019_oi_190007.pdf#page=1) | REPORT | Cumulative one-year MDD; logistic regression with −1/+1 effect coding. |
| [Main p. 4, Statistical Methods](../../../jama_bot_2019_oi_190007.pdf#page=4) | REPORT | Primary logistic MDD; Cox called post hoc; GEE exchangeable-correlation longitudinal ANCOVA for secondary outcomes at 3, 6 and 12 months, baseline adjusted. |
| [Main p. 6, Table 2 and continuation](../../../jama_bot_2019_oi_190007.pdf#page=6) | REPORT | Primary imputed ORs and post hoc time-to-event HRs; site/history adjustment and MI. No Kaplan–Meier/log-rank/four-cell or repeated-MDD model result appears here. |
| [Main p. 8, Table 3 and footnotes](../../../jama_bot_2019_oi_190007.pdf#page=8) | REPORT | IDS is secondary; overall inference from GEE, 12-month inference from robust linear regression. |

**Consistency rule applicable / logical comparison reproduced:** Yes, route A category 5: replaced or unreported specified primary analyses. The protocol primary suite is different from the SAP/report primary logistic suite. Full REPORT text and source-result rereads find no Kaplan–Meier/log-rank/four-way results or repeated-MDD mixed-model result as specified. The reported IDS GEE/robust-linear specification differs from the protocol primary mixed-model specification; SAP explicitly permits GEE, so this is not a claim that GEE conflicts with SAP. The reporting of a Cox HR does not, by itself, report the other planned components. Display-precision interval check: not applicable to categorical model/comparison specifications and absence of a named result; no numerical discrepancy is inferred from an unavailable fit.

**Necessary inputs available / exact missing inputs:** Specifications, named outcome, scheduled times and reported models/results are available. Exact fitted repeated-MDD model, planned four-way contrasts, country-clustering implementation and prospective chronology connecting protocol version 7 to the undated SAP are not supplied. Raw data/model code are unnecessary to reproduce the specification difference but would be necessary for re-estimation. Site adjustment may account for country when sites correspond to countries; no failure of that adjustment is asserted.

**Source-grounded alternative interpretation:** The SAP may prospectively replace the protocol suite, and the reported GEE may implement an acceptable repeated-outcome specification under that SAP. Those possibilities are supported by the supplied SAP language but its governing amendment relationship is not documented in the compared source passages.

**Direct observation versus inferred explanation:** The changed named models and missing matching planned primary result displays are direct bounded observations. An intentional later governing revision is an inferred alternative. No preferred model or claim about numerical consequences is made.

**Classification confirmation / ambiguity:** P_R primary; all P_R, P_P; protocol_report. Protocol versus SAP produces a genuine PLAN/PLAN analysis-specification relationship, not mere corroboration, and protocol versus report produces P_R. P_R has precedence. Chronology/amendment authority is the ambiguity. Cox's separate prespecified/post hoc label is handled in C007 and is not independently duplicated here.

**Evidence state:** reproduced. The exact source specifies primary components not reported as such, alongside distinct SAP/report specifications.

**Exact remaining human question:** Which prospective specification governed primary MDD and IDS analyses, and where are the replacement or nonreporting of protocol primary Kaplan–Meier/log-rank/four-way and repeated-MDD/IDS mixed-model analyses documented?

## C003 — Online-screening BMI cutoff

**Finding provenance:** F-XS-001. **Location found / source and comparator matched:** Yes. [Main p. 3, Figure 1 online exclusions](../../../jama_bot_2019_oi_190007.pdf#page=3), REPORT, visually prints 1451 excluded with BMI <15 or >40. The same figure separately prints 18 telephone exclusions with BMI <25. [Results supplement p. 3, inclusion criteria assessed with the online screening tool](../../../joi190007supp3_prod.pdf#page=3), REPORT, explicitly specifies BMI 25–40 for that online stage. [Main p. 2, eligibility](../../../jama_bot_2019_oi_190007.pdf#page=2), REPORT, defines BMI 25–40; [main p. 1, abstract population](../../../jama_bot_2019_oi_190007.pdf#page=1), REPORT, prints the same range. [Protocol p. 16, inclusion criteria](../../../joi190007supp1_prod.pdf#page=16), PLAN, confirms BMI 25–40 but is corroboration only.

**Consistency rule applicable / calculation reproduced:** Yes, route A category 2: differing printed numeric cutoffs change the population represented by 1451 exclusions. Allow 15 its interval [14.5,15.5] and reference 25 [24.5,25.5]. Gap 9; relative discrepancy 9/25 = 0.36 >0.05. The upper cutoff 40 agrees. Counts/flow sums themselves reconcile; the registered issue is the lower cutoff attached to the count, not an invented alternative count.

**Necessary inputs available / exact missing inputs:** Printed cutoffs, explicit stage identity and flow count are available. Individual screening records, actual online software rule and distribution of BMI among the 1451 exclusions are absent; these are unnecessary to reproduce the label discrepancy but necessary to establish the actually applied rule or any changed count.

**Source-grounded alternative interpretation:** The 18 later BMI <25 exclusions suggest a possible intentionally looser early screen. This is not excluded as a possible mechanism, but it does not reconcile the supplement's explicit same-stage online 25–40 statement with Figure 1's 15. No actual eligibility breach is inferred.

**Direct observation versus inferred explanation:** The differing printed online cutoffs and the 18 telephone exclusions are direct. Numeric substitution or staged screening is an inferred explanation; no substituted value is assigned.

**Classification confirmation / ambiguity:** Primary S_C; all S_C, S_W; statistical_results. The main figure differs from the same-stage results-supplement statement and from main population/eligibility statements. Protocol corroboration does not create P_R. Stage interpretation is the ambiguity, not source role. Numeric flow-label content belongs in statistical_results, not the wording-only category.

**Evidence state:** reproduced. Visual reading confirms 15, not 25, in the online Figure 1 label and confirms 25 in the explicit online comparator.

**Exact remaining human question:** Which lower BMI cutoff was applied during online screening, and how should the 1451-exclusion label be reconciled with the results appendix's online 25–40 criterion and the later 18 BMI <25 exclusions?

## C004 — Sample-size total and factorial cell counts

**Finding provenance:** F-NUM-001, F-ST1-001. **Location found / source and comparator matched:** Yes. [Main p. 4, Sample Size upper right column](../../../jama_bot_2019_oi_190007.pdf#page=4), REPORT, visually states 392 participants, 196 in each of four possible intervention combinations, for main intervention effects. The same paragraph states 22% follow-up attrition and 250 participants per intervention combination. These are two compared quantities in one retrospective report paragraph.

**Consistency rule applicable / calculation reproduced:** Yes, route A category 3, with category 2 support. Exact arithmetic is 4 ×196 =784 versus printed 392. Four is the exact factorial cell count, not a rounded measurement. Allowing 196 [195.5,196.5] gives total [782,786]; 392 gives [391.5,392.5]. Gap 389.5 participants, relative discrepancy 389.5/392 =0.993622 >0.05. Subsequent 196/(1−0.22) =251.282 is compatible with 250 after precision: [195.5/0.785,196.5/0.775] = [249.0446,253.5484] overlaps [249.5,250.5]. Thus the attrition calculation is not an additional reproduced discrepancy. No sample-size test algorithm is needed for the four-cell identity.

**Necessary inputs available / exact missing inputs:** All arithmetic inputs, four-cell structure and printed quantities are available. The intended counting unit of 392—whole trial, pooled factor level or another comparison—is absent. Exact power-calculation code is absent but not required to establish the count identity.

**Source-grounded alternative interpretation:** 392 may refer to a pooled factor level made of two 196-participant cells; alternatively 196 may have been intended for each of two pooled conditions. The 250-per-combination continuation supports a per-cell reading for 196 but cannot turn the explicitly printed 392 into the whole four-cell sum.

**Direct observation versus inferred explanation:** Printed counts and the identity failure are direct. A pooled-factor counting convention is an inferred possible interpretation; no final replacement count is assigned.

**Classification confirmation / ambiguity:** S_W primary/all; statistical_results. Both conflicting counts are within one REPORT paragraph. Protocol corroboration is unnecessary and creates no P_R. Ambiguity concerns the counting unit, not classification.

**Evidence state:** reproduced. The exact PDF confirms both counts in the same paragraph and their intervals remain separated.

**Exact remaining human question:** Does 392 denote the entire pre-attrition trial or one pooled factor level, and how should it reconcile with 196 in each of four combinations and the subsequent 250-per-combination target?

## C005 — Primary power assumptions

**Finding provenance:** F-XS-003, F-ST1-002. **Location found / source and comparator matched:** Yes. [Protocol p. 16, §4.4](../../../joi190007supp1_prod.pdf#page=16), PLAN, prints control cumulative MDD 30%, intervention 15%, 180 participants per group, two-sided alpha .05, power .90, dropout 20% and 250 per intervention arm. It also says a difference of 25% and refers to additive intervention interaction. [Protocol p. 17, calculation continuation](../../../joi190007supp1_prod.pdf#page=17), PLAN, says 250 is sufficient and synergistic rather than additive treatments would lead to four-treatment-group comparisons with 80% power. [Main p. 4, Sample Size](../../../jama_bot_2019_oi_190007.pdf#page=4), REPORT, prints active 20% versus control 30%, 33% reduction, 196 per combination, alpha .05, power .90, attrition 22% and 250 per combination for main effects.

**Consistency rule applicable / calculation reproduced:** Yes, route B under planned power assumptions. Active-incidence PLAN [14.5,15.5]% versus REPORT [19.5,20.5]% leaves gap 4 percentage points; 4/20 =0.20. PLAN 180 [179.5,180.5] versus REPORT 196 [195.5,196.5] leaves gap 15; 15/196 =0.076531 (15/180 =0.083333). Both exceed .05. Control 30%, alpha .05 and power .90 agree. Dropout [19.5,20.5]% versus [21.5,22.5]% leaves gap 1 point, relative 1/22 =.045455 or 1/20 =.05, so it is precision-compatible under the mandated rule and is not an independently reproduced discrepancy. Diagnostic power formulas are not substituted for the source's unspecified factorial algorithm.

**Necessary inputs available / exact missing inputs:** Printed probabilities, group sizes, nominal power/alpha and factorial context are available. The operative primary contrast, additive/synergistic interaction assumption, group-counting convention, exact calculation algorithm and prospective amendment mapping are unavailable. The protocol's 25% wording has no explicit absolute/relative basis; this recheck does not manufacture a separate internal numeric comparison from that ambiguity.

**Source-grounded alternative interpretation:** A revised anticipated active event rate, or distinct additive-interaction versus main-effect power contrasts, may account for the two specifications. The plan explicitly discusses interaction and the report main effects. Neither supplies the governing revision or a mapping of 180 to 196.

**Direct observation versus inferred explanation:** The differing printed assumptions are direct. A changed design calculation or amendment is inferred; the recheck does not state that a particular power algorithm fails or infer clinical consequences from raw data.

**Classification confirmation / ambiguity:** P_R primary/all; protocol_report. The compared planned and reported calculation specifications differ. Protocol's additive/synergistic explanation supplies context, not an independently established P_P conflict under the registered rule. Ambiguity concerns the operative contrast and revision chronology.

**Evidence state:** reproduced. The active-incidence and per-group printed-value intervals remain separated beyond .05.

**Exact remaining human question:** Which prospective primary-MDD event-rate and comparison assumptions governed the trial's power calculation, and what specification reconciles planned 15%/180 with reported 20%/196?

## C006 — Outcome hierarchy

**Finding provenance:** F-XS-004, F-ST1-003. **Location found / source and comparator matched:** Yes for all affected outcome-status occurrences.

| Exact location | Role | Matched hierarchy |
|---|---|---|
| [Protocol p. 8, main study parameters](../../../joi190007supp1_prod.pdf#page=8) and [p. 9, continuation](../../../joi190007supp1_prod.pdf#page=9) | PLAN | MDD and IDS depressive symptomatology are in the main study-parameter list; IDS is on p. 9. |
| [Protocol p. 28, §§8.1.1–8.1.2](../../../joi190007supp1_prod.pdf#page=28) | PLAN | Main endpoints include MDD and IDS; secondary endpoints include GAD-7 and quality of life. |
| [Protocol p. 43, §10.1](../../../joi190007supp1_prod.pdf#page=43) | PLAN | Primary parameter analysis includes MDD onset and IDS-score severity. |
| [SAP p. 2, Outcomes](../../../joi190007supp2_prod.pdf#page=2) | PLAN | MDD primary; PHQ and IDS secondary; GAD and health-related quality of life under Other. |
| [Main p. 4, Outcomes](../../../jama_bot_2019_oi_190007.pdf#page=4) | REPORT | MDD primary; PHQ, IDS, GAD and utility secondary; secondary findings advised to be interpreted as exploratory because of multiple comparisons. |
| [Main p. 8, Table 3 heading](../../../jama_bot_2019_oi_190007.pdf#page=8) | REPORT | IDS, PHQ, GAD and utility displayed as Secondary Outcomes. |

**Consistency rule applicable / logical comparison reproduced:** Yes, route A category 5. IDS explicitly moves between main/primary and secondary outcome sets. The GAD/utility Other-versus-secondary occurrences are also found; whether Other conveys an inferential tier is ambiguous, and IDS alone establishes the reproduced status difference. Display-precision interval check: not applicable to categorical status labels. The secondary-results exploratory caution is not treated as a separate unexplained change of prespecified hierarchy.

**Necessary inputs available / exact missing inputs:** Named scales, plan/report hierarchy headings and analysis headings are available. A dated governing hierarchy amendment and definition of SAP Other are absent. No raw outcome values are necessary for the status comparison.

**Source-grounded alternative interpretation:** The SAP may document an intended revision of IDS hierarchy, and Other may be an organizational heading rather than a distinct outcome rank. The package does not establish the revision's authority/timing. Main versus primary wording is reinforced by protocol §10.1, rather than assumed from a title alone.

**Direct observation versus inferred explanation:** The placement of the same outcomes beneath the headings is direct. A deliberate re-ranking or administrative grouping explanation is inferred; no inference about the numerical effect estimates is made.

**Classification confirmation / ambiguity:** P_R primary; all P_R, P_P; protocol_report. Protocol/report IDS ranks differ, as do protocol/SAP ranks; SAP is PLAN by prospective content. P_R takes precedence. Other and the governing hierarchy chronology are the ambiguity.

**Evidence state:** reproduced. The directly read IDS main/primary and secondary classifications remain distinct.

**Exact remaining human question:** Which prospective hierarchy governed IDS, GAD and utility, and what amendment or explicit meaning of Other reconciles the supplied plan and report headings?

## C007 — Planned analyses labeled post hoc

**Finding provenance:** F-XS-006, F-XS-007, F-ST1-005. **Location found / source and comparator matched:** Yes, including every Cox and site/history occurrence in this repeated status pattern.

| Exact location | Role | Matched evidence |
|---|---|---|
| [Protocol p. 43, §10.1](../../../joi190007supp1_prod.pdf#page=43) | PLAN | Cox time-to-MDD is specified in primary-parameter analysis. |
| [Protocol p. 44, interaction paragraph](../../../joi190007supp1_prod.pdf#page=44) | PLAN | Country interactions in Cox MDD and mixed symptom models are prospectively described. |
| [SAP p. 4, Secondary analysis and Effect modification](../../../joi190007supp2_prod.pdf#page=4) | PLAN | Cox time-to-MDD and history/center modification are explicitly specified secondary analyses. |
| [SAP p. 5, Effect modification continuation](../../../joi190007supp2_prod.pdf#page=5) | PLAN | Interaction terms, P<.05 criterion and presentation in text/tables are specified. |
| [Main p. 4, Outcomes/Statistical Methods](../../../jama_bot_2019_oi_190007.pdf#page=4) | REPORT | Time-to-first-MDD/Cox called post hoc. Site/history modification described separately from baseline-severity analyses, which are explicitly post hoc. |
| [Main p. 6, Table 2](../../../jama_bot_2019_oi_190007.pdf#page=6) | REPORT | Post Hoc Outcome: Time to MDD Onset; supplement HR 1.05 (.86–1.27), therapy .91 (.75–1.10), interaction .91 (.75–1.11). |
| [Main p. 7, MDD results continuation](../../../jama_bot_2019_oi_190007.pdf#page=7) | REPORT | Repeats Cox HRs/P values .65, .32 and .36 under the time-to-first-MDD analysis. |
| [Main p. 8, Effect Modification and Sensitivity Analyses](../../../jama_bot_2019_oi_190007.pdf#page=8) | REPORT | Collectively calls site, history and baseline symptom modification post hoc, then describes PHQ/baseline, GAD/baseline and utility/site results. |
| [Results supplement p. 18, eAppendix 10](../../../joi190007supp3_prod.pdf#page=18) | REPORT | History does not moderate primary/secondary outcomes; baseline PHQ and GAD moderation and utility/site moderation described; PHQ Table A. |
| [Results supplement p. 19, GAD Table B](../../../joi190007supp3_prod.pdf#page=19) | REPORT | History/site terms and baseline-GAD interactions displayed; supplement/baseline interaction B .062, P .022. |
| [Results supplement p. 20, utility Tables C1/C2](../../../joi190007supp3_prod.pdf#page=20) | REPORT | Site/history terms; F-BA×UK B .017, CI .001–.033, P .041; UK/Netherlands subgroup results. |

**Consistency rule applicable / logical comparison reproduced:** Yes, route A category 5. Explicit PLAN Cox and site/history analysis commitments coexist with REPORT post hoc designations. Within REPORT, the Methods' separate post hoc qualification of baseline severity differs in scope from the Results' collective site/history/baseline post hoc statement. The numeric HR/moderation results are found and help identify the same analyses; no numeric discrepancy is alleged. Display-precision interval check: not applicable to prespecified/post hoc status. Baseline severity itself is not alleged to have been planned.

**Necessary inputs available / exact missing inputs:** The prespecified textual commitments, compared reported status and named results are available. SAP finalization date, outcome-inspection timeline, analysis-specific amendments and the intended scope/meaning of post hoc are absent. Protocol country interactions and SAP center/history specifications are not claimed identical in every model detail; both support the stated planned status of the registered analysis components.

**Source-grounded alternative interpretation:** Post hoc may mean additional to the article's primary logistic model, or the SAP may have been finalized after some analysis decisions. Main Methods may intend to reserve that label for baseline severity. These interpretations need chronology or a narrower reading of the Results sentence to reconcile the printed statuses.

**Direct observation versus inferred explanation:** Explicit planning language and reported post hoc labels are direct. Timing, collective-label scope and motivation are inferred alternatives; no intent is assigned.

**Classification confirmation / ambiguity:** P_R primary; all P_R, S_W; protocol_report. PLAN/REPORT status differs, and REPORT Methods/Results status scope differs internally. Supplement tables corroborate the identity and content of the analyses without a separate S_C status conflict; protocol/SAP both prospectively specify them, so their different primary/secondary ranks are not a separate P_P relationship in this status candidate. P_R precedes S_W. Ambiguity is undated SAP chronology and the label's scope.

**Evidence state:** reproduced. Planned Cox and site/history specifications and their post hoc report labels are found exactly.

**Exact remaining human question:** Were Cox and site/history modification specified before outcome inspection, and how should their collective post hoc designation reconcile with the supplied plans and the Methods' separate baseline-severity qualification?

## C008 — Planned additive primary interaction result

**Finding provenance:** F-XS-008, F-ST1-006. **Location found / source and comparator matched:** Yes. [SAP p. 4, Interaction of intervention strategies for our primary outcome](../../../joi190007supp2_prod.pdf#page=4), PLAN, explicitly specifies multiplicative logistic A×B interaction plus additive sensitivity using RERI from a linear odds-ratio model, likelihood-based 95% CI and recoding to the assumed lowest-risk joint reference. [Main p. 4, Statistical Methods](../../../jama_bot_2019_oi_190007.pdf#page=4), REPORT, describes jointly modeled intervention effects/interactions. [Main p. 6, Table 2](../../../jama_bot_2019_oi_190007.pdf#page=6), REPORT, supplies interaction OR .93 (.76–1.14), P .48 and HR .91 (.75–1.11), P .36. [Main p. 7, narrative](../../../jama_bot_2019_oi_190007.pdf#page=7), REPORT, repeats those multiplicative results. All supplemental comparator locations were visually found: [p. 18 moderation](../../../joi190007supp3_prod.pdf#page=18), [p. 19 GAD moderation](../../../joi190007supp3_prod.pdf#page=19), [p. 20 utility moderation](../../../joi190007supp3_prod.pdf#page=20), [p. 21 no-MI sensitivity](../../../joi190007supp3_prod.pdf#page=21), [p. 22 CACE](../../../joi190007supp3_prod.pdf#page=22), all REPORT. None labels a primary additive RERI result.

**Consistency rule applicable / logical comparison reproduced:** Yes, route A category 5 for a planned primary-outcome analysis not reported. Multiplicative OR/HR interaction is not an additive RERI result. The full supplied REPORT scope described above contains no RERI/additive coefficient, CI, test or identified replacement. No RERI is estimated from crude printed event counts. Display-precision interval check: not applicable to absence of the specified estimand/result; printed multiplicative values are transcribed only to establish that the available comparison uses another scale.

**Necessary inputs available / exact missing inputs:** The affirmative plan commitment and full supplied REPORT result set are available. The fitted linear-OR/additive model, chosen joint reference, RERI result/CI and any withdrawal or replacement amendment are absent. Raw data would be required to conduct the analysis, but not to reproduce the bounded reporting absence.

**Source-grounded alternative interpretation:** The additive analysis may have been replaced or recorded elsewhere. The available multiplicative null result may have motivated not displaying additional analysis, but this is not stated and cannot stand as the RERI result.

**Direct observation versus inferred explanation:** Explicit plan and no matching result in the supplied package are direct bounded observations. Whether the analysis was conducted or why it was not displayed is not observed.

**Classification confirmation / ambiguity:** P_R primary/all; protocol_report. The prospective SAP commitment differs from the supplied retrospective REPORT set. Concordant report omissions are not themselves an S_C relationship; no PLAN/PLAN RERI discrepancy is registered. Unprovided amendment/result provenance is the ambiguity.

**Evidence state:** reproduced. The committed primary additive result is not found in the complete supplied REPORT set.

**Exact remaining human question:** Was the primary RERI sensitivity analysis conducted, and where is its result or a prospectively documented replacement reported?

## C009 — Planned primary missingness sensitivity

**Finding provenance:** F-ST1-010. **Location found / source and comparator matched:** Yes. [SAP p. 5, Missing data and drop-out](../../../joi190007supp2_prod.pdf#page=5), PLAN, specifies 100 primary-outcome MI datasets under MAR with Rubin pooling and immediately promises that, because missing-mechanism assumptions cannot be validated, sensitivity analyses will be conducted and reported. [Main p. 4, Statistical Methods](../../../jama_bot_2019_oi_190007.pdf#page=4), REPORT, states 100-MI/MAR/Rubin analysis and GEE without MI as sensitivity for the continuous secondary setting. [Main p. 6, Table 2 and missingness narrative](../../../jama_bot_2019_oi_190007.pdf#page=6), REPORT, supplies imputed primary ORs 1.06/.93/.93 and comparisons of missing rates, but no alternative missing-mechanism primary estimate. [Main p. 8, sensitivity/CACE narrative](../../../jama_bot_2019_oi_190007.pdf#page=8), REPORT, identifies depression, anxiety and utility score sensitivity without MI. [Results supplement p. 21, eAppendix 11](../../../joi190007supp3_prod.pdf#page=21), REPORT, explicitly shows secondary PHQ/IDS/GAD/utility without MI. [Results supplement p. 22, eAppendix 12](../../../joi190007supp3_prod.pdf#page=22), REPORT, includes primary CACE ORs but explicitly retains MI; it addresses compliance rather than an identified alternative missing mechanism.

**Consistency rule applicable / logical comparison reproduced:** Yes, route A category 5. The promised sensitivity sits in the primary-outcome MI/MAR paragraph; the complete REPORT set contains secondary-score missingness sensitivity and MI-CACE, but no identified primary-MDD missingness-sensitivity analysis/result. Comparing missing rates does not provide that result. Display-precision interval check: not applicable to the absence of a promised analysis; no arithmetic conflict between observed dropout counts and imputation is inferred.

**Necessary inputs available / exact missing inputs:** The plan paragraph's context, reported primary imputation and all supplied sensitivity displays are available. Exact planned primary sensitivity model, intended scope of the generic sentence, primary sensitivity result and any formal limitation/revision are absent. Individual missingness data cannot be checked from the package and are not needed to identify this reporting absence.

**Source-grounded alternative interpretation:** The broad sensitivity sentence may have been intended to be satisfied by secondary GEE only, despite its immediate primary-MI context. A primary result may exist outside the supplied set. These remain clarifications rather than assumed additional required methods.

**Direct observation versus inferred explanation:** The printed commitment, immediate context and named supplied sensitivity outcomes are direct. Whether the authors intended a separate primary analysis, and whether it was conducted, are inferred/unresolved questions; no preferred missing-data method is suggested.

**Classification confirmation / ambiguity:** P_R primary/all; protocol_report. PLAN commitment versus REPORT analysis coverage determines the relationship; agreeing REPORT occurrences do not add S_C. Ambiguity concerns the sensitivity sentence's intended scope and any revision.

**Evidence state:** reproduced. No matching primary-MDD missingness sensitivity is supplied despite the primary-MI-context promise; no printed primary sensitivity result was missed in the report search.

**Exact remaining human question:** Which primary-MDD analysis fulfilled the reported missing-data-sensitivity commitment, or was that commitment formally limited to secondary outcomes?

## C010 — CACE explanation and MDD estimate mapping

**Finding provenance:** F-ST1-007. **Location found / source and comparator matched:** Yes for every compared location, with additional exact context on supplement p. 14.

| Exact supplied-source location | Role | Matched source values or explanation |
|---|---|---|
| [Main p. 6, Table 2](../../../jama_bot_2019_oi_190007.pdf#page=6) | REPORT | ITT imputed supplement OR 1.06 (.87–1.29), therapy .93 (.76–1.13); site/history/intervention adjustment, effect coding −1/+1. |
| [Main p. 8, CACE narrative](../../../jama_bot_2019_oi_190007.pdf#page=8) | REPORT | No supplement primary effect and significant therapy CACE OR .78 (.64–.95); account for adherence. |
| [Results supplement p. 14, eAppendix 7 opening](../../../joi190007supp3_prod.pdf#page=14) | REPORT | Instrumental-variable/latent-complier explanation, retained randomization and observed treatment compliance used to estimate control compliance. |
| [Results supplement p. 15, eAppendix 7 continuation](../../../joi190007supp3_prod.pdf#page=15) | REPORT | Structural equation model explanation; CACE described as difference between compliers' outcomes, then as ratio of original intervention effect estimate to treatment-arm complier proportion. |
| [Results supplement p. 16, adherence table](../../../joi190007supp3_prod.pdf#page=16) | REPORT | Therapy ≥8 sessions, N=512, adherence 71.9% and 70.7% in the two therapy cells; main allocation confirms 256 participants each. |
| [Results supplement p. 22, eAppendix 12](../../../joi190007supp3_prod.pdf#page=22) | REPORT | Therapy CACE OR .78 (.64–.95); supplement .84 (.67–1.07). MI, site/history adjustment, logistic MDD-any-follow-up outcome, effect coding −1/+1; supplement compliance omega-3 ≥70%, therapy 8/21 sessions. |

**Consistency rule applicable / calculation reproduced:** Yes, route B, bounded to the stated method mapping for these named MDD estimates. Let c be a positive compliance proportion, 0<c≤1. A literal ratio of the printed supplement OR interval [1.055,1.065] to c cannot be below 1.055. Dividing its positive log by c and exponentiating likewise cannot fall below 1.055. Printed CACE [.835,.845] leaves minimum gap 1.055−.845 =.210; relative gap .210/.84 =.25 >.05. The direction cannot reverse under either literal mapping.

For therapy, the observed equal-cell average compliance has rounding interval [(0.7185+0.7065)/2,(0.7195+0.7075)/2] = [.7125,.7135]. An explicitly labeled **log-OR ratio diagnostic**, not a reconstruction of the fitted SEM, gives exp(log(OR)/c) over ITT OR [.925,.935] and that compliance interval = [.896354,.910104]. Printed therapy CACE [.775,.785] leaves gap .111354 and relative .111354/.78 =.142762 >.05. The OR-scale literal ratio also cannot produce a lower therapy OR, but the log-scale diagnostic is the informative bounded comparison. These calculations test the supplied ratio explanation and do not assert that every valid logistic CACE estimate must be a rescaled Table 2 coefficient. No crude event ratio or alternative analysis is substituted.

**Necessary inputs available / exact missing inputs:** The reported ITT/CACE values, outcome, adjustment labels, effect coding, ratio wording and observed therapy compliance are available. The exact original numerator intended by eAppendix 7, its scale, fitted compliance probabilities, first/second-stage SEM equations, treatment-interaction handling and relationship of that fitted model to Table 2 are unavailable. Those are necessary to reproduce the actual logistic CACE fit, which this recheck does not claim to have reconstructed.

**Source-grounded alternative interpretation:** The ratio statement may illustrate a linear outcome difference, while p. 22's logistic/SEM CACE uses a different fitted numerator or conditional population. The opening eAppendix acknowledges latent compliance and a structural equation model. This could permit the printed ORs; the printed materials do not identify its scale/equations or its mapping to the cited original MDD effect. Thus the reproduced issue is an unclear method/result mapping, not a claim that the printed ORs are impossible under any model.

**Direct observation versus inferred explanation:** ITT and CACE values, ratio wording and failure of the literal mappings are direct. Treating that ratio as the exact logistic algorithm would be an inference and is explicitly not asserted. A nonlinear SEM or different numerator is an alternative requiring specification.

**Classification confirmation / ambiguity:** Primary S_C; all S_C, S_W; statistical_results. The method explanation/CACE table differ in clarity from the named main-article original MDD values across REPORT documents; within the supplement, the explanation and logistic table need the same unspecified mapping. No PLAN document is needed or added by corroboration. Ambiguity concerns scale and fitted model, not roles. The main narrative's nonsignificant supplement description agrees with both OR intervals; no narrative-direction candidate is inferred.

**Evidence state:** reproduced. The ratio explanation does not identify a source-grounded transformation reconciling the named MDD ORs; the display diagnostic remains beyond .05. The evidence state does not adjudicate the fitted CACE results.

**Exact remaining human question:** Which original effect, scale, compliance proportion and CACE/SEM model yield the MDD ORs .84 and .78, and how does that mapping relate to eAppendix 7's ratio explanation and Table 2's ITT values?

## C011 — Site coefficients and same-table interval construction

**Finding provenance:** F-ST1-008. **Location found / source and comparator matched:** Yes. All three affected rows and all six comparator rows were visually read at [results supplement p. 19, Table B](../../../joi190007supp3_prod.pdf#page=19), REPORT, headed interaction between supplements and overall anxiety severity follow-up. Netherlands is the reference. Exact affected tuples are Spain B .107, 95% CI −.424 to .520, P .694; United Kingdom B .117, CI −.371 to .638, P .637; Germany B .058, CI −.401 to .606, P .804. No source digit or location differs from the ledger.

**Consistency rule applicable / calculation reproduced:** Yes, route A category 4, limited to the centered coefficient/CI relationship B=(L+U)/2 that reproduces the other rows of this same display. Allow all printed endpoint and coefficient half-units, including the coarser .17 and .52 endpoint precision in comparator rows.

| Affected site | Printed B interval | Recomputed CI midpoint interval | Minimum gap | Relative gap / printed B |
|---|---|---|---:|---:|
| Spain | [.1065,.1075] | [.0475,.0485] | .0580 | .542056 |
| United Kingdom | [.1165,.1175] | [.1330,.1340] | .0155 | .132479 |
| Germany | [.0575,.0585] | [.1020,.1030] | .0435 | .750000 |

| Same-table comparator | Matched B; CI | Printed B interval | Recomputed midpoint interval | Relationship reproduced |
|---|---|---|---|---|
| Supplements | −.107; −.384 to .17 | [−.1075,−.1065] | [−.10975,−.10425] | Overlap; gap 0 |
| F-BA | −.054; −.329 to .221 | [−.0545,−.0535] | [−.0545,−.0535] | Overlap; gap 0 |
| History of depression | −.317; −.698 to .063 | [−.3175,−.3165] | [−.3180,−.3170] | Overlap; gap 0 |
| Baseline GAD-7 | .464; .409 to .52 | [.4635,.4645] | [.46175,.46725] | Overlap; gap 0 |
| F-BA × baseline GAD-7 | −.016; −.068 to .036 | [−.0165,−.0155] | [−.0165,−.0155] | Overlap; gap 0 |
| Supplements × baseline GAD-7 | .062; .009 to .115 | [.0615,.0625] | [.0615,.0625] | Overlap; gap 0 |

All affected point estimates lie inside ordered intervals. All three site intervals include zero and their P values exceed .05; there is no interval-null/P decision conflict. The baseline GAD printed P=0 is a display-zero convention, independent of the registered pattern. An implied upper-endpoint diagnostic 2B−L gives .638/.605/.517, but no replacement endpoint is assigned. In particular, the UK's upper-endpoint-only relative gap is within .05; its registered coefficient-midpoint comparison above is the independent .132479 gap.

**Necessary inputs available / exact missing inputs:** All nine nonreference B/CI tuples, endpoint precision, confidence-level heading and P values are available. Exact CI algorithm, fitted model output, and any rule applying asymmetric or different-model CIs specifically to site rows are absent. These missing definitions prevent reproducing the actual inferential construction, but do not remove the same-display centered relationship finding. The comparison does not impose universal symmetry on all confidence intervals.

**Source-grounded alternative interpretation:** Site intervals may use an asymmetric procedure or be derived from a different fit than their coefficients; no such distinction appears in the table. This is a possibility, not an established method. The remaining rows support a centered construction, and each of the three site gaps persists after display precision.

**Direct observation versus inferred explanation:** The three tuples, control-row overlap and site-row interval gaps are direct. A specific asymmetric construction, differing model or production mechanism is inferred and remains unresolved. The common pattern is retained as one ID with all three sites.

**Classification confirmation / ambiguity:** S_W primary/all; statistical_results. All comparisons occur within one retrospective REPORT table. No report-versus-plan or between-report inconsistency is needed. Statistical construction is the ambiguity; the source role and relationship are unambiguous.

**Evidence state:** reproduced. Each site's coefficient-midpoint interval gap exceeds .05 while the same centered relationship reproduces the six other nonreference rows.

**Exact remaining human question:** What coefficient/CI construction was used for each site row, and why do those three tuples not follow the centered construction reproduced by the remaining rows?

## Completion and unresolved definitions

Covered IDs: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011. Evidence states: reproduced 11; reproduced_after_transcription_correction 0; not_reproduced 0. Classification corrections: none. No ID was deleted, suppressed or assigned a disposition. Every cited location was found; every affected occurrence and numeric comparator was matched to source content.

Remaining limitations are exact final formulation/amendment provenance; dated governing protocol/SAP hierarchy and analysis chronology; actual online screening implementation; sample-size counting unit/algorithm; missing committed RERI and primary-MDD sensitivity results or formal replacements; fitted CACE mapping/compliance model; and site-specific CI construction. Each is localized in its own card and exact human question. These are interpretive/model-input limitations, not inaccessible-source or coverage gaps. Source and reused assets were preserved; new files consist only of this artifact and the four declared CPU page images in preprocessing/evidence_recheck/.
