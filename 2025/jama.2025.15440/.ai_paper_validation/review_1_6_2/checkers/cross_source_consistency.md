# Cross-source consistency review

## Scope and source authority

Fresh cross-source review of all four supplied sources: DOC-001 main article, nine physical PDF pages, REPORT; DOC-002 protocol v2.0, 26 pages, PLAN; DOC-003 SAP v1.2, 24 pages, PLAN; DOC-004 results supplement, 11 pages, REPORT. Document roles follow content. The complete main and support quantitative maps supplied the matching index; no earlier scientific conclusions were consulted. There is no supplied workbook, CSV, or other structured result source.

The review covered every applicable matched occurrence in abstract, Key Points, narrative, tables, figures, captions, footnotes and results supplement. Main relationships N001–N080 and S001–S028 and support relationships N101–N111 and S101–S124 were considered, matching population, time, contrast, model, measure, analysis set and displayed precision. Background/reference relationships have no applicable AMALFI matched result. Administrative and descriptive comparisons were screened under the scope tiers rather than promoted into findings.

Direct source confirmation of the finding used newly rendered main article pages 3 and 7 and SAP page 20. These derivatives were produced with the recorded package-local PDF helper, PyMuPDF 1.26.4, CPU, 200 dpi: `preprocessing/cross-checker-main3.png`, `preprocessing/cross-checker-main7.png`, `preprocessing/cross-checker-sap20.png`. Fresh SAP pages 5–23 layout text, `preprocessing/cross-checker-sap5-23.txt`, used the same recorded helper with PyMuPDF sorted reading order. Readable reusable main/results text and source-page images and fresh user-approved GPU protocol OCR/images were used as locators for the remaining comparisons. Derivatives do not override source pages.

## Complete matching and design comparison record

| Relationship scope | Exact source scope and comparison | Result of cross-source check |
|---|---|---|
| N002–N010; N108; S101, S104, S115 | Main pp. 1–4 Figure 1; protocol pp. 4, 10–15; SAP pp. 6–14, 16–17 | Individual 1:1 randomization, all 5040 randomized/2520 per arm, ITT irrespective of patch adherence, and source-specific complete follow-up match. Power target up to 5000 and realized 5040 are different quantities. Death within complete follow-up and national death totals have different source definitions. |
| N003, N011, N014–N051; N102, N109; S115, S119 | Main pp. 1–2, 4–5; results pp. 5–6; protocol pp. 4, 11–12, 18; SAP pp. 6, 9–10, 14–16, 24 | Baseline copies and aggregate summaries match to displayed precision; baseline adherence subgroup table uses row percentages, not randomized-arm prevalence. Eligibility lists compared item by item: sex/age, sex-specific score, consent, AF/flutter exclusion, latex exclusion. Score components compared individually: heart failure, hypertension, age ≥75, diabetes, prior stroke/TIA/thromboembolism, vascular disease, age 65–74, female sex. Diagram age observation is screened below. GP agreement and eligibility assessed before invitation are operational clarification; no changed analysis-population count is established. |
| N052–N056; S002–S009, S025; S101–S102 | Main abstract p. 1, Key Points p. 2, Outcomes/Analysis p. 3, Results p. 4, Figure 2 p. 6; protocol pp. 4, 9–11, 15; SAP pp. 5, 8–9, 13, 18 | Primary GP-record AF between randomization and 2.5 years, ratio of proportions 1.26 (1.02–1.57), P=.03, 172/2520 versus 136/2520 match. Age <80/≥80 and sex secondary comparisons, subgroup event/population counts, ratios, heterogeneity P=.78/.06 and narrative agree. Primary chi-square, absence of planned baseline adjustment and no-primary censoring agree. |
| S001, S027; N108, N110; S113–S118 | Main p. 3; protocol pp. 13–15, 19–22; SAP pp. 21–23 | Overall initial 2500/expanded 5000, 1.75%/4.4% assumptions, estimated 2.5-fold contrast, 2-fold alternative and stated subgroup power rationale match across narrative locations. All protocol power rows and projection labels were considered. Power-design .01 is distinct from analysis alpha .05. No noninferiority/equivalence margin is specified; null is no between-arm difference. Two-sided .05, 95% CIs, no formal multiplicity adjustment and interpretive allowance match. Numerical sample-size reproduction belongs to the statistical checking lane. |
| S012–S013, S026; S103–S104, S107 | Main pp. 3, 5; protocol pp. 4, 10–11, 15; SAP pp. 5, 7–9, 12–14, 18–19 | Five-year mean known-AF time remains secondary; the separately prespecified 2.5-year version is exploratory, as reported. Whole ITT mean, zero time if never diagnosed, death/withdrawal censoring and permutation approach match. SAP explicitly defers loss-without-AF imputation details; main states the implemented within-arm imputation. No incompatible planned imputation is printed. Five-year result timing is screened below. |
| N104; S105, S120–S122 | Main p. 3, p. 5 sensitivity statement; results p. 8 eFigure 1; SAP p. 18 | Primary-or-secondary-care AF sensitivity is distinct from primary GP-only AF. Overall 251/2520 versus 207/2520, ratio 1.21 (1.02–1.45), P=.03, and all age/sex rows are internally keyed to the sensitivity definition. Main's similar-results statement does not substitute primary-only counts into this display. |
| N057–N060; S010–S011; S106 | Main pp. 3, 5–6 Figure 3; SAP p. 19 | Prespecified exploratory log-rank time-to-first GP AF, death/withdrawal/GP loss censoring and 2.5-year cutoff match. Rate ratio 1.29 (1.03–1.61), P=.03 matches body/figure; conditional diagnosis medians 103/530 days are not all-randomized medians. Kaplan–Meier control 5.6% and primary crude proportion 5.40% are distinct estimands. |
| N006, N012, N061–N067; N101, N103, N105–N107; S014, S123–S124 | Main abstract p. 1, results pp. 4–5, discussion/conclusion pp. 7–8; results eMethods p. 2, eTable 1 p. 4, eTable 3 p. 7, eFigures 2–4 pp. 9–11; SAP pp. 6, 17, 20–21 | 2126/2520 adherence, 89 patch AF, 4.2% among wearers versus 3.53% of randomized, 13 additional flutter, AF-only versus combined AF/flutter populations, AF burden and grouped longest-episode percentages match. Main 14 (13–14) analyzable days agrees with supplement 13.5 (12.6–13.9) under displayed precision. Patch-to-GP record analysis conditions on detected AF and explicitly accommodates seven GP records preceding urgent report; no opposing time origin is printed. |
| N068–N070; S015–S017; S108–S110 | Main abstract p. 1, Analysis p. 3, Results p. 5, Figure 4A p. 7; SAP pp. 13–14, 19–20 | OAC chi-square proportions 364/2520 versus 322/2520, RR 1.13 (.98–1.30), P=.08 differ legitimately from time-to-event RR 1.15 (.99–1.34), P=.07. Mean exposure 1.63/1.14 months and difference .50 (.24–.75), P<.001 agree abstract/body. Month-of-randomization exclusion, calendar-month scale, 30-month cutoff, death/withdrawal censoring and lack of GP-loss censoring match. |
| S111; protocol §8.5.2 and SAP §6.5.1 | Protocol p. 16; SAP pp. 20–21; main p. 5 patch-to-GP follow-up; results p. 10 | Three nonrandomized diagnostic-route groups and group-specific OAC timing criteria compared separately. Reported patch-report-to-GP record interval matches one specified comparison. No primary/key-secondary replacement arises from other exploratory group comparisons not appearing in this publication. |
| N071–N077; S018–S024; S112 | Main abstract p. 1, Analysis p. 3, Results p. 5, Figure 4B/caption p. 7; protocol p. 16; SAP pp. 11–12, 20 | Death/stroke counts, time window and direction match within REPORT material; abstract/body stroke interval difference is screened below. Clinical-event analysis specification differs between SAP and report: F-XS-001. Ischemic stroke remains displayed separately, alongside additional any-stroke/hemorrhagic results, rather than disappearing from the report. |
| S028; S114 | Main p. 3; SAP pp. 22–23 | SAS version matches; later R/RStudio versions are allowed by SAP's 'or later' wording. |
| Interim/stopping framework | SAP pp. 9, 12, 21–22; protocol pp. 14–15; main pp. 2–3 | No formal safety/efficacy interim or stopping rule is planned. Blinded baseline/patch-detection review for recruitment expansion is explicitly distinguished from unblinded between-arm efficacy; descriptions reconcile. No prespecified outcome-dependent stop or multiplicity hierarchy is reported to have changed. |

## Findings

### F-XS-001

**Title:** Clinical stroke/death comparisons use log-rank rate-ratio analyses although the supplied SAP specifies counts and proportions without hypothesis testing.

**Compared locations and document roles:**

- PLAN: [SAP, physical PDF page 20, §6.4.4](../../../joi250068supp2_prod_1760999665.29862.pdf#page=20), long-term clinical impact of screening.
- PLAN contextual alternatives: [SAP page 21, §6.6](../../../joi250068supp2_prod_1760999665.29862.pdf#page=21), additional non-prespecified exploratory analyses; [SAP page 5, §2](../../../joi250068supp2_prod_1760999665.29862.pdf#page=5), deviations described/justified in final report.
- REPORT: [main article page 3, Outcomes and Statistical Analysis](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=3), stroke/death exploratory comparisons and log-rank methods.
- REPORT: [main article page 7, Figure 4B and caption](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=7), clinical event counts and time-to-event rate ratios/95% CIs.
- REPORT affected repeated occurrences: [main article abstract page 1](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=1), stroke rate ratio; [main article Results page 5](../../../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=5), stroke event RR.

**Printed statements and values:** SAP §6.4.4 says that the trial is not powered for significant clinical-outcome differences and that numbers and proportions of hospitalisations, ischemic stroke, major bleeding, and all-cause/cardiovascular death will be reported, 'with no hypothesis testing performed.' Details are to be specified later. Main Outcomes identifies randomized stroke and death comparisons and points to the SAP for full details. Main Statistical Analysis states that time to first postrandomization stroke and death were analyzed using log-rank methods. Figure 4B calls its outputs rate ratios from time-to-event analyses, with unadjusted 95% CIs:

| Clinical outcome | Patch events /2520 | Usual-care events /2520 | Reported rate ratio (95% CI) |
|---|---:|---:|---|
| Cardiovascular death | 32 | 43 | .74 (.47–1.17) |
| Noncardiovascular death | 71 | 83 | .85 (.62–1.17) |
| Any death | 103 | 126 | .82 (.63–1.06) |
| Presumed ischemic stroke | 60 | 58 | 1.03 (.72–1.48) |
| Hemorrhagic stroke | 12 | 6 | 1.94 (.77–4.90) |
| Any stroke | 69 | 64 | 1.08 (.77–1.51) |

Abstract reports any-stroke 1.08 (.76–1.53); this small interval-copy difference is screened separately, not the basis of this finding. No clinical-event P value is printed in Figure 4B or the stroke narrative.

**Comparison logic:** Compare the planned clinical-event analysis with the reported clinical-event analysis for the same randomized arms and clinical events. The supplied SAP expressly specifies descriptive counts/proportions and no hypothesis testing; report introduces log-rank time-to-event analyses and comparative rate ratios with confidence intervals. These are different analysis specifications. This is a logical planned-versus-reported comparison, not a numerical calculation; half-unit rounding intervals and relative discrepancy are not applicable. The finding does not infer a missing clinical P value or assert that an unprinted test was performed. The report's explicit analysis specification is the observation.

**Focus area:** D, planned versus reported analysis specification.

**Proposed review domain:** `protocol_report`.

**Proposed relationship type / all relationships:** `P_R` / `P_R`.

**Qualifying route:** Route B.

**Affected result or extracted value:** The any-stroke rate ratio 1.08 and its confidence interval in the abstract/body and all six Figure 4B clinical-event rate-ratio analyses. Whether these are the planned descriptive analyses or additional non-prespecified time-to-event analyses changes their interpretation and how their analysis provenance is extracted.

**Why context does not resolve it:** The paper consistently labels these outcomes exploratory and cautions against definitive treatment-effect inference; those statements address interpretation, but do not identify the switch from the supplied SAP's descriptive clinical-event specification to log-rank time-to-event estimates. The method difference remains explicit even though no clinical-event P values are displayed. The additional-analysis clause permits new analyses but calls for their identification as non-prespecified; the reported clinical analyses are not expressly identified that way. B1 is met by the analysis-specification comparison, B2 by the unresolved provenance, and B3 by the abstract/figure clinical estimates named above.

**Supported alternatives and missing definition:** SAP §6.4.4 may reserve its descriptive rule for later long-term publications, with current 2.5-year rate ratios treated as additional exploratory analyses under §6.6. Log-rank outputs may have been used solely for estimation, without clinical-event hypothesis testing. A later analysis specification may exist, since the SAP defers details, but none is supplied. Those alternatives should be distinguished from a claim that the displayed analyses necessarily breached a decision rule.

**Human question:** Are the reported 2.5-year stroke/death log-rank rate ratios additional non-prespecified exploratory analyses, estimation-only extensions of SAP §6.4.4, or analyses covered by a later specification; and which supplied statement establishes their planned status?

## Excluded observations

Only apparent issues not emitted are listed here; reconciled comparisons are recorded in the coverage matrix above.

| Location | Observation | Reason code |
|---|---|---|
| Main abstract p. 1 versus main Results p. 5 / Figure 4B p. 7 | Any-stroke RR CI .76–1.53 versus .77–1.51. Lower-limit half-unit intervals [.755,.765] and [.765,.775] touch: gap 0. Upper-limit intervals [1.525,1.535] and [1.505,1.515] have gap .010; relative discrepancy .010/1.53=.00654, below .05. Same RR/counts/timeframe; no significance conflict. | ROUNDING_OR_DISPLAY_PRECISION |
| Protocol p. 11 Figure 1 versus same-page §6.2 and SAP p. 6 | Diagram age ≥54 versus explicit criterion ≥65 is a numeric eligibility-display discrepancy. No changed primary/key-secondary result, analysis-population size or decision rule is established; other eligibility elements match item by item. This age value is not an estimate, interval, count or percentage in route A category 2. | PERIPHERAL_COMPARISON |
| Protocol p. 11 diagram versus protocol pp. 4, 10, 15 / SAP pp. 8–9, 18 | Diagram's 2.5-year secondary subgroup bullet mentions age only; complete secondary specifications explicitly include sex. The diagram does not assign sex a conflicting outcome status, and the same protocol unambiguously specifies sex as secondary. | CONTEXT_RESOLVES |
| Protocol pp. 4, 10, 15 / SAP pp. 8–9 versus main p. 3 | Five-year secondary mean time with AF is not reported in the current 2.5-year paper. SAP p. 12 explicitly schedules a subsequent publication for five-year secondary results; SAP p. 19 separately prespecifies the reported 2.5-year exploratory version. No replacement of the five-year analysis is reproduced. | CONTEXT_RESOLVES |
| SAP pp. 14, 18 versus main p. 3 | SAP defers AF-loss imputation details; main describes the implemented assumption. No opposing planned algorithm is supplied, so an undocumented timing/detail alone cannot establish a discrepancy. | CONDITIONAL_OR_UNREPORTED |
| SAP p. 20 ischemic-stroke list versus main Figure 4B p. 7 | Any-stroke and hemorrhagic-stroke rows appear in addition to the separately reported presumed ischemic-stroke row. The listed ischemic endpoint is retained, and SAP p. 21 permits additional exploratory analyses; a changed composite or outcome status is not established by the additional rows alone. | CONTEXT_RESOLVES |
| SAP pp. 19–21 versus main/results supplement | Some planned exploratory OAC timing/nonrandomized group comparisons are not printed in this publication. They are neither primary nor key secondary analyses; omission alone creates no conflicting printed result or claimed prespecification. | CONDITIONAL_OR_UNREPORTED |

## Completion and limitations

Complete cross-source relationship scope: all applicable REPORT/REPORT and PLAN/REPORT matches in the 80 main numeric, 28 main inferential/design, 11 support numeric and 24 support inferential/design relationships, plus relevant PLAN/PLAN design specifications. One finding and seven excluded observations. No uncovered source unit remains in this assigned cross-source scope. Permutation implementation/replication counts, log-rank O−E/V and individual-level observations are not supplied; the separate outcome-derivation and health-economics documents named by the SAP are also not supplied. No preferred method is proposed. The finding is prepared for independent inclusion screening and human adjudication; no candidate IDs or dispositions are assigned.
