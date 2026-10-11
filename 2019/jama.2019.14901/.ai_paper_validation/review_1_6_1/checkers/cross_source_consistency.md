# Cross-source and matched-result consistency review

Fresh mandatory reviewer runtime: `01a128e0-7bc2-7152-a260-a42c4a4fcd31`; configured role `qc161_cross_source_consistency_reviewer`, gpt-6.1-sol/medium. Exact scope: every matched result across DOC-001 pp.1–11 and DOC-003 pp.1–9, every applicable planned-versus-reported and plan-internal statistical-design relationship in DOC-002 pp.1–48, and explicit applicability assessment of DOC-004 p.1. Source roles by content: DOC-001, DOC-003, DOC-004 REPORT; DOC-002 PLAN. No old scientific conclusions, external evidence, or web used. All assigned source/evidence units were covered without sampling.

Read QUALITY_CONTROL_SCOPE.md and the complete 1.6.1 review contract, settings, tooling record, source inventory, and both complete new evidence maps. Reusable text and the new maps were locators. Direct Poppler `pdftotext -layout` source reads covered relevant main methods/results, protocol synopsis and pp.25–35, supplement tables, and administrative statement. Findings were confirmed by fresh direct-source rendering and visual reading: DOC-001 pp.1,4,6,8; DOC-002 pp.31,33,34; DOC-003 p.2. Engine: direct Poppler 26.01.0 CPU `pdftoppm`, `-singlefile`, `-scale-to 1600` (protocol/supplement/main p.1) or `1800` (main pp.4,6,8). Unique derivatives are `preprocessing/cross_source/main-p1.png`, `main-p4.png`, `main-p6.png`, `main-p8.png`, `protocol-p31.png`, `protocol-p33.png`, `protocol-p34.png`, and `results-p2.png`, all beneath that directory. No source or reused asset changed.

## Coverage and matching record

| Evidence scope | Comparison completed | Outcome |
|---|---|---|
| Main abstract, Key Points, narrative, Figure 1, Table 1, all footnotes | Randomized 648 versus analyzed 641; arm assignments 306/342 versus analysis 302/339; demographics refer to their stated population; all table rows matched to supplementary strata where possible | Population differences explained by seven secondary exclusions. Baseline cross-location discrepancies screened below. |
| Main primary result throughout pp.1,2,6–9; Figure 2; subgroup Figure 3; supplement eTables 3–5 | Day-7 reintubation 55/302 versus 40/339; risk difference, CI, P, direction, reference arm; PaCO2 strata 48/63 and 254/276; all center totals | Primary matched counts and effect agree; stratified counts sum to totals. Whole versus decimal percentages reconcile. Proportion and survival tests distinguished. |
| Main secondary narrative/Table 2; supplement eTable 1 and all eTable 3/4 rows | All outcome/time/count matches, exact totals across PaCO2 strata; respiratory-failure day 7, reintubation 48h/72h/ICU, ICU/hospital/day-90 mortality; exploratory composite and reintubated mortality | Two respiratory-failure reporting discrepancies below. Remaining matching counts reconcile. Differences between strata and pooled continuous distributions are not contradictions. |
| Figure 2/3 captions, footnotes and risk tables; survival eFigure | Population, origin, time, censoring/risk count, curve direction and statistical labels | Risk counts are contributors rather than event denominators. Survival-figure axis wording screened below; no unprinted curve coordinates inferred. |
| Protocol pp.9–11,25–32 and main pp.2–4 | Day-7 endpoint; respiratory-failure definition; reintubation decision criteria; eligibility; treatment dose/duration; strata; secondary hierarchy | Primary day-7 window, treatment prescription, and strata agree. Reintubation acidosis threshold discrepancy below. Other omissions/context-resolved differences screened below. |
| Protocol pp.33–35 and report methods/results | Primary chi-square; logistic covariate rules; primary survival/Cox; missingness/population; subgroup analyses; secondary methods; sample size and power | Primary chi-square and planning inputs agree. Planned Cox and two subgroup families have no corresponding reported results; findings below. Do not equate prognostic logistic modeling with adjusted treatment-effect modeling. |
| Protocol all pp.1–48, including p.41 schedule, p.42 local weaning form, Helsinki pp.43–48 | Plan-internal endpoint, power inputs, analysis population, decision rules; applicable prospective intervention/design information; margin, hypothesis direction, interim/stopping/multiplicity | No additional qualifying plan-internal inconsistency. Trial is superiority; no noninferiority/equivalence margin, trial-specific efficacy interim/stopping rule or multiplicity hierarchy is supplied. Optional local weaning form is not a universal trial criterion. |
| Main pp.10–11; supplement p.1; DOC-004 p.1 | Administrative/reference contents and applicability | No additional current-trial matched result or planned analysis. DOC-004 is administrative REPORT with data unavailable; no applicable statistical relationship. |

All 97 main numeric/reporting groups, 32 main statistical groups, 21 support numeric groups, and 17 support statistical groups were considered for matching; every cell in their attached tables was covered. This checker does not assign global S IDs or statistical-pass states.

## Findings

### F-XS-001

**Title:** Day-7 respiratory-failure absolute difference differs between abstract/narrative and Table 2.

**Locations and roles:** REPORT [DOC-001 p.1, abstract Results](../../../jama_thille_2019_oi_190108.pdf#page=1); REPORT [DOC-001 p.6, Secondary Outcomes](../../../jama_thille_2019_oi_190108.pdf#page=6); REPORT [DOC-001 p.8, Table 2 respiratory-failure row](../../../jama_thille_2019_oi_190108.pdf#page=8). Corroborating counts only: REPORT [DOC-003 p.2, eTable 1 first row](../../../joi190108supp2_prod.pdf#page=2) and [pp.6–7, subgroup eTables](../../../joi190108supp2_prod.pdf#page=6).

**Printed values:** Abstract and main narrative print 21% versus 29%, difference −8.7%, 95% CI −15.2% to −1.8%, P=.01. Table 2 prints intervention 70/339 (21%), control 88/302 (29%), absolute difference −8.5%, the same CI and P.

**Comparison logic:** Same overall analyzed population, same day-7 endpoint, intervention-minus-control contrast, and same CI/P. Counts imply 100×(70/339−88/302)=−8.4901 percentage points. Differences displayed to one decimal occupy disjoint half-unit intervals: −8.7 implies [−8.75,−8.65], whereas −8.5 implies [−8.55,−8.45]. The distinct point estimates cannot be rounding of one estimate. No adjusted estimate or different analysis set is labeled in either location.

**Focus area:** A/B. **Proposed review domain:** `statistical_results`. **Proposed relationship type:** `S_W`. **All relationships:** `S_W` (supplement corroborates counts and does not create the contrast).

**Affected result or extracted value:** Absolute intervention effect on the abstract-reported key secondary outcome of postextubation respiratory failure at day 7.

**Why context does not resolve it:** The same endpoint effect is explicitly given as −8.7 twice and −8.5 once, with identical accompanying inference and no explanation of a different estimator. Counts support the table but do not explain the alternate repeated effect statement or identify whether an unreported analysis generated it.

**Supported alternatives:** Table uses the count-based risk difference; narrative reflects another unlabelled calculation or transcription. The package does not establish the latter explanation. No alternate value is selected for human review.

**Human verification steps:** Compare all three source locations, confirm the denominator/model for the narrative estimate, and establish which effect estimate was intended for this endpoint.

### F-XS-002

**Title:** Day-7 respiratory-failure P value differs between main report and results supplement.

**Locations and roles:** REPORT [DOC-001 p.1 abstract](../../../jama_thille_2019_oi_190108.pdf#page=1), [p.6 Secondary Outcomes](../../../jama_thille_2019_oi_190108.pdf#page=6), [p.8 Table 2](../../../jama_thille_2019_oi_190108.pdf#page=8), and [p.4 Statistical Analysis](../../../jama_thille_2019_oi_190108.pdf#page=4); REPORT [DOC-003 p.2 eTable 1 first row](../../../joi190108supp2_prod.pdf#page=2).

**Printed values:** Main abstract, narrative and Table 2 give P=.01 for respiratory failure at day 7. eTable 1 gives P=.02 for the same 88/302 versus 70/339, 29% versus 21% row. Main methods say postextubation respiratory-failure rates at day 7 were compared by chi-square; the supplement does not label another test or analysis set.

**Comparison logic:** Same population, event counts, denominators, time, and contrast. At two decimal places, the half-unit intervals for .01 and .02 have no shared interior; only their .015 boundary touches, which cannot generate both displayed values under one consistent rounding convention. This is a cross-location comparison of printed tests, not a claim that one specific chi-square variant must have been used.

**Focus area:** B/C. **Proposed review domain:** `statistical_results`. **Proposed relationship type:** `S_C`. **All relationships:** `S_C`.

**Affected result or extracted value:** P value attached to the abstract-reported key secondary day-7 respiratory-failure comparison. Both values are below .05; no change in the reported direction or binary significance conclusion is claimed.

**Why context does not resolve it:** No supplementary test label, adjustment, alternative denominator, or analysis-population explanation distinguishes this P value from the main comparison. A reader cannot establish which printed test result applies, or whether two analyses were intended.

**Supported alternatives:** The two locations may use distinct chi-square implementations, or one value may reflect a transcription difference. Neither explanation is established in the supplied package.

**Human verification steps:** Confirm the first eTable 1 row versus Table 2 and the test/continuity-correction settings; establish whether the supplementary P pertains to a different specified analysis.

### F-XS-003

**Title:** Respiratory-acidosis threshold in the reintubation rule differs between plan and report.

**Locations and roles:** PLAN [DOC-002 p.30, section 5.4 start](../../../joi190108supp1_prod.pdf#page=30), [p.31 continuation](../../../joi190108supp1_prod.pdf#page=31); REPORT [DOC-001 p.4 Outcomes](../../../jama_thille_2019_oi_190108.pdf#page=4). Affected reported endpoint: [DOC-001 p.8 Table 2 primary row](../../../jama_thille_2019_oi_190108.pdf#page=8).

**Printed statements:** The protocol's reintubation respiratory-failure criterion requires at least two components including respiratory acidosis pH<7.35 and PaCO2>45 mm Hg. The main report's severe respiratory failure leading to reintubation requires at least two components including pH<7.25 and PaCO2>45 mm Hg. Other listed respiratory thresholds match (rate>35, high oxygen requirement/ratio≤100, distress). This comparison is of reintubation criteria, not the separate secondary respiratory-failure definition, which uses pH<7.35 in both sources.

**Comparison logic:** With PaCO2>45, values 7.25≤pH<7.35 qualify as the acidosis component under the plan but not under the report. For example, pH7.30 plus one matching respiratory component meets the plan's two-component severe-failure rule but not the report's rule unless another component is present. This is a rule comparison, not an assertion that any actual patient's management or event status changed. Display precision cannot reconcile distinct stated cutoffs.

**Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship type:** `P_R`. **All relationships:** `P_R`.

**Affected result or extracted value:** Operational decision rule underlying the primary day-7 reintubation outcome, reported as 40/339 versus 55/302, and related reintubation-criteria results.

**Why context does not resolve it:** Both thresholds occur explicitly in the same severe-failure/reintubation context. The report does not describe this change, and the supplied protocol contains no amendment replacing the cutoff. The separate pH<7.35 secondary definition cannot explain this contrast.

**Supported alternatives:** A later analysis/operational amendment may have specified 7.25, or one threshold may be a reporting transcription. No supplied document establishes which applied; no amendment or clinical consequence is inferred.

**Human verification steps:** Confirm both severe-failure definitions and obtain the applicable dated operational rule/amendment; determine which threshold guided reported primary outcome ascertainment.

### F-XS-004

**Title:** Prespecified Cox analysis for primary reintubation has no corresponding reported estimate.

**Locations and roles:** PLAN [DOC-002 p.33 section 6.2](../../../joi190108supp1_prod.pdf#page=33). REPORT [DOC-001 p.4 methods](../../../jama_thille_2019_oi_190108.pdf#page=4), [p.7 additional analyses](../../../jama_thille_2019_oi_190108.pdf#page=7), [p.8 Table 2](../../../jama_thille_2019_oi_190108.pdf#page=8); REPORT [DOC-003 pp.1–9](../../../joi190108supp2_prod.pdf#page=1), all supplied results-supplement contents.

**Printed statements:** Plan primary section specifies Cox proportional-hazards regression for variables associated with reintubation at P<.20, backward selection, final P<.05, with adjusted relative risk/hazard ratio and 95% CI. Report describes chi-square, Kaplan–Meier/log-rank, primary logistic adjusted OR=.60 (.38–.93), and post hoc hospital random effects. No Cox model, HR, or corresponding CI appears in the complete REPORT package. Day-7 reintubation is the primary outcome.

**Comparison logic:** The primary-outcome section explicitly commits to a Cox analysis; the supplied report package presents other models/tests and contains no result from that specified analysis. This finding records absence of the prespecified primary analysis from supplied reporting, and does not claim that the logistic OR is an HR or that a Cox analysis must replace the stated chi-square primary comparison.

**Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship type:** `P_R`. **All relationships:** `P_R`.

**Affected result or extracted value:** Availability and prespecified-analysis interpretation of adjusted time-to-reintubation results alongside the reported primary reintubation comparison.

**Why context does not resolve it:** The reported logistic OR and unadjusted Kaplan–Meier/log-rank analyses are different measures/models, and no supplied text says the planned Cox analyses were withdrawn, amended, completed with no eligible covariates, or reported elsewhere in the package. This rests on an explicit plan commitment rather than a preference for additional methods.

**Supported alternatives:** Analyses may have been amended, performed without reported estimates, or not undertaken. The package does not establish which; no effect value or consequence is inferred.

**Human verification steps:** Review dated SAP/amendments and determine whether planned Cox analyses were retained and, if so, locate their results or explanation of their reporting status. The plan does not identify every forced/selected variable, so do not reconstruct the models from aggregate counts.

### F-XS-005

**Title:** Two prespecified primary-outcome subgroup families are absent from the supplied results reporting.

**Locations and roles:** PLAN [DOC-002 p.34 section 6.4](../../../joi190108supp1_prod.pdf#page=34). REPORT [DOC-001 p.4 subgroup methods](../../../jama_thille_2019_oi_190108.pdf#page=4), [p.7 subgroup results](../../../jama_thille_2019_oi_190108.pdf#page=7), [p.8 Figure 3](../../../jama_thille_2019_oi_190108.pdf#page=8); REPORT [DOC-003 pp.1–9](../../../joi190108supp2_prod.pdf#page=1), complete results supplement.

**Printed statements:** Protocol specifies primary and secondary subgroup analyses by PaCO2, and additionally in patients with underlying cardiac or respiratory disease and by weaning test (T-piece versus minimal pressure support). Report subgroup methods/results and eTables 3/4 give PaCO2 comparisons only: hypercapnic day-7 risk difference −12.9%, nonhypercapnic −5.0%, interaction P=.25. Cardiac/respiratory disease and weaning-test types appear as baseline descriptors, but no primary-outcome subgroup effect/result by those factors is reported.

**Comparison logic:** Two explicitly prespecified primary-outcome subgroup families lack results in the complete supplied REPORT materials. Baseline characteristic rows are not outcome analyses and cannot serve as their reported results. Consolidated as one repeated omission pattern across two subgroup factors, without claiming that results outside the package do not exist.

**Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship type:** `P_R`. **All relationships:** `P_R`.

**Affected result or extracted value:** Prespecified subgroup results for primary day-7 reintubation by chronic cardiac/respiratory disease and by spontaneous-breathing-test mode; interpretation of the reported primary-outcome subgroup evidence as the complete prespecified set.

**Why context does not resolve it:** The plan explicitly states these analyses will be performed and the report explains only PaCO2 subgroup analysis, without amendment or explanation for the other two families. Different clinical names cannot resolve an entirely absent outcome analysis.

**Supported alternatives:** An applicable later SAP may have removed these factors, or the analyses may have been conducted but not reported in supplied materials. Neither is established; no subgroup effect or interaction is inferred.

**Human verification steps:** Confirm the prespecified factors against the dated applicable SAP/amendments and determine whether their primary-outcome analyses were retained and where their results/reporting explanation are located.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT main pp.1,3,4 | 648 randomized versus 641 analyzed; assigned 306/342 versus analyzed 302/339; seven exclusions and exact reason counts are stated. | CONTEXT_RESOLVES |
| REPORT main pp.1,4,5; supplement pp.3–4 | Randomized demographics and analyzed baseline rows have different populations; supplementary baseline disease/physiology/sex values and pooled rows are peripheral descriptive comparisons. | PERIPHERAL_COMPARISON |
| REPORT main p.6; supplement p.4 | Supplement hypercapnic cough/secretions percentages differ from printed fractions/main pooled description; these are baseline descriptive values and do not change the primary/key-secondary outcome or analysis population. | PERIPHERAL_COMPARISON |
| REPORT main pp.1,2,6,8; supplement pp.6–8 | Primary 11.8/18.2 versus whole 12/18 percentages and supplementary .0489 versus .049 reflect display precision. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main pp.7–8; supplement p.7 | Nonhypercapnic P=.10 in narrative versus .1057 in eTable and log-rank .11 in Figure 3; separate proportion/survival tests and low-precision reporting do not change inference or extracted effects. | CONTEXT_RESOLVES |
| REPORT main Table 2 p.8; supplement pp.6–7 | Every matching stratum event count sums to the reported pooled count; pooled and stratum-specific stay distributions/continuous differences need not coincide. | NOT_REPRODUCED |
| REPORT main pp.7–8; supplement pp.6–7 | Exploratory per-stratum composite/reintubated mortality differences versus pooled measures concern different populations; no repeated key-result contrast remains. | PERIPHERAL_COMPARISON |
| REPORT main Figures 2/3; supplement eFigure p.9 | Individual-time risk counts are censored contributor counts and not event totals; small count differences or curve risk-table comparisons are peripheral. | PERIPHERAL_COMPARISON |
| REPORT supplement p.9 eFigure | Axis says Days Since Intubation, while title says survival from extubation to day 90 and baseline is 302/339; immediate caption/title resolves the intended origin. | NOTATION_OR_TYPOGRAPHY |
| REPORT main p.8 Table 2 | Shared percent difference heading also spans stays labeled in days; row units make the intended units clear. This is separate from unspecified continuous-estimator issues assigned to statistical review. | NOTATION_OR_TYPOGRAPHY |
| REPORT main pp.4,8; PLAN pp.33–34 | Prognostic outcome-association/backward-selected logistic model versus reported stratum/baseline-imbalance treatment-effect adjustment; treating these as a proved replacement requires identifying them as the same planned model, which the package does not establish. | CONDITIONAL_OR_UNREPORTED |
| PLAN p.34; REPORT main pp.4,7–8 | Planned mortality Cox analysis is introduced in the absence of interaction; the package does not establish that condition, so an unconditional omission finding for ICU mortality is not registered. | CONDITIONAL_OR_UNREPORTED |
| PLAN pp.9,25,33; REPORT main p.4 | Planned ventilatory-support-free days through day 14 not reported; this secondary endpoint is neither abstract-reported nor designated key secondary, and does not change an analysis population or primary/key-secondary result. | PERIPHERAL_COMPARISON |
| PLAN p.33; REPORT main pp.3–4 | Plan ITT after eligibility validation versus extubated/complete-primary-outcome analysis; eligibility exclusions and three missing primary outcomes are disclosed, and no contrary trial-specific imputation rule is supplied. | CONTEXT_RESOLVES |
| PLAN p.30; REPORT main p.4 | Planned tachypnea lasting at least 2h versus abbreviated report respiratory-rate criterion without duration; omission alone does not establish the duration requirement was removed. | CONDITIONAL_OR_UNREPORTED |
| PLAN p.31; REPORT main p.4 | Plan agitation/hemodynamic numeric details versus abbreviated report severe neurological/hemodynamic descriptions; actual discordant endpoint classification is not established. | CONDITIONAL_OR_UNREPORTED |
| PLAN pp.29–30; REPORT main pp.2–3,6 | Same prescribed HFNC 50 L/min, ≥48h; NIV first ≥4h, ≥12h/day, PS≥5, PEEP5–10 and oxygen target≥92%; delivered mean durations/settings differ from prescribed targets with intolerance explicitly stated. | CONTEXT_RESOLVES |
| PLAN pp.10,26–29; REPORT main pp.2–3 | At least/>24h wording and abbreviated eligibility/SBT descriptions leave the same intended population readily identifiable; no changed analysis-population size established. | TERMINOLOGY_OR_WORDING |
| PLAN pp.27–28,42 | Appendix local weaning form has stricter/no-vasopressor and one-hour T-piece steps; protocol expressly offers it where no local weaning protocol exists and otherwise permits usual practice. | CONTEXT_RESOLVES |
| PLAN pp.11,32 | Study-duration synopsis/body arithmetic and recruitment calendar differences are administrative, without a statistical decision-rule consequence. | PERIPHERAL_COMPARISON |
| PLAN pp.33–35; REPORT main p.4 | N590 inflated by approximate 10% to rounded target650, power80%, two-sided alpha .05, rates18%/10% and difference8% match. Historical expected rates15–20% encompass18%. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN all pages; REPORT main p.4 | No supplied noninferiority/equivalence margin, trial-specific efficacy-interim boundary, stopping rule or multiplicity hierarchy contradicts report superiority/exploratory-secondary statements. | CONDITIONAL_OR_UNREPORTED |
| PLAN pp.14–20,34–35 | Historical literature/cohort counts and rates describe other trials or planning rationale; not current-trial matched outcomes. | PERIPHERAL_COMPARISON |
| PLAN p.33; REPORT main p.4 | SAS9.2 versus9.4 version statements alone do not establish a changed statistical specification/result. | OUT_OF_FOCUS |
| DOC-004 p.1 REPORT; main pp.10–11 | Data unavailable, contributor/funding/reference material supplies no applicable current-trial quantitative contrast. | OUT_OF_FOCUS |

## Completion and limitations

Complete scope: DOC-001 11/11 pages, DOC-002 48/48 pages, DOC-003 9/9 pages, DOC-004 1/1 page; five self-screened findings and 25 excluded-observation patterns. No scientific coverage gap or tooling limitation. No separately supplied SAP/amendment, raw data, workbook or CSV exists in this package. No exact continuous-estimator algorithm or undocumented patient-level endpoint reassignment was inferred. These are reporting findings for independent inclusion screening, not adjudications, and no C IDs or final correction is assigned.
