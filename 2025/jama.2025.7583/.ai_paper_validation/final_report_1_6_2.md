# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.6.2

**Pending Human Adjudication.** Every candidate in this report remains Pending Human Adjudication. Evidence states and inclusion-audit outcomes describe the review record; they are not human adjudications.

## Executive Quality-Control Summary

Complete review of the supplied EMPROTECT package identified **four stable candidates**, C001–C004. Three concern planned-versus-reported statistical design: an explicitly planned complication comparison without a supplied comparative result, a strict versus inclusive primary recurrence boundary, and a disclosed amendment to the primary composite's death component. One concerns the participant samples underlying baseline midline-shift summaries. The amendment is explicitly documented in SAP version 2, which states that its final version was prepared before final database lock.

All 119 physical pages in five supplied PDFs were mapped. Nine initial checker findings underwent independent inclusion screening: seven were included and consolidated into four issues; two were screened out. Both distinct statistical passes completed all 67 statistical relationships. Mechanical source recheck reproduced all four candidates; the independent inclusion audit recorded CONFIRMED for all four. No scientific coverage gap remains. These are candidate reporting issues requiring human adjudication, with bounded potential relevance to evidence extraction; no change to the trial conclusion is established.

## Package and Reused-Evidence Provenance

The supplied main article reports randomized middle meningeal artery embolization versus standard care after chronic subdural hematoma surgery. Source roles were assigned from content: the main article and results supplement are REPORT; the protocol, prospective addenda and SAP are PLAN. Stable evidence units are physical PDF pages. There are no supplied Office, workbook or CSV sources.

| Source ID | Actual supplied filename | Content role | Physical pages |
|---|---|---|---:|
| DOC-001-MAIN | [jama_shotar_2025_oi_250033_1750956987.75881.pdf](../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=1) | REPORT | 9 |
| DOC-002-PROTOCOL | [joi250033supp1_prod_1750956987.76581.pdf](../joi250033supp1_prod_1750956987.76581.pdf#page=1) | PLAN | 63 |
| DOC-003-ADMIN | [joi250033supp3_prod_1750956987.77681.pdf](../joi250033supp3_prod_1750956987.77681.pdf#page=1) | PLAN | 23 |
| DOC-004-RESULTS-SUPP | [joi250033supp4_prod_1750956987.77981.pdf](../joi250033supp4_prod_1750956987.77981.pdf#page=1) | REPORT | 15 |
| DOC-005-SAP | [joi250033supp5_prod_1750956987.78281.pdf](../joi250033supp5_prod_1750956987.78281.pdf#page=1) | PLAN | 9 |
| Total | Five PDFs | Two REPORT; three PLAN | 119 |

Fresh scientific discovery used supplied sources and source-linked reusable evidence, without earlier candidate selections or reports as scientific inputs. The [evidence-asset inventory](review_1_6_2/evidence_asset_inventory.md) records 296 eligible legacy assets: 248 USABLE, 16 PARTIAL, 26 DUPLICATE and 6 STALE, with none UNREADABLE. Complementary usable page images/OCR cover partial native layers. Asset counts overlap source pages and therefore do not count independent source units. Older extraction engine versions are sometimes unrecorded. Candidate facts were confirmed against current supplied-source text and renders, with derivatives serving as transcription aids.

Twelve current scientific derivatives are separately documented with their source units and pinned PyMuPDF 1.26.4 engine. These targeted confirmations do not change the original reusable/fresh-required coverage partition. Source and reusable-asset fingerprints are retained in [source hashes before review](review_1_6_2/source_hashes_before.sha256) and [reused-asset hashes before review](review_1_6_2/reused_artifact_hashes_before.sha256).

## Scope, Complete Coverage, and Exclusions

The review addresses counts and denominators, estimate/test logic, statistical method logic, and planned-versus-reported statistical design under the supplied QUALITY_CONTROL_SCOPE.md. It covers every supplied page, including covers, references, forms and administrative image pages, with applicability recorded for units without result-relevant relationships.

| Source ID | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---:|---:|---:|---:|---|
| DOC-001-MAIN | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-002-PROTOCOL | 63 | 63 | 0 | 63 | COMPLETE |
| DOC-003-ADMIN | 23 | 23 | 0 | 23 | COMPLETE |
| DOC-004-RESULTS-SUPP | 15 | 15 | 0 | 15 | COMPLETE |
| DOC-005-SAP | 9 | 9 | 0 | 9 | COMPLETE |
| Total | 119 | 119 | 0 | 119 | COMPLETE |

The [source coverage ledger](review_1_6_2/source_coverage.md) partitions every source into reusable and fresh-required units and documents complete mapping. Administrative PDF pages 16–22 combine sparse native text with retained images/OCR. Main mapping, protocol mapping and other-support mapping are disjoint. Their full outputs and all stage assignments are recorded in the [coverage manifest](review_1_6_2/coverage_manifest.md). Zero fresh-required units reflects available reusable extraction, while every page still received fresh scientific mapping.

Excluded scope includes broad methodology, clinical, novelty, misconduct and raw-data audits, preferences for alternative analyses, and peripheral cross-document comparisons that do not change a primary/key secondary result, an analysis-population size or a planned decision rule. Numeric display precision, resolved wording, model-based versus crude quantities, and absent details without a conflicting printed value or statement were screened under the defined rules. Only supplied package evidence was used; unavailable cited documents were neither fetched nor assigned inferred contents.

## Quantitative and Statistical Relationship Coverage

The [main map](review_1_6_2/extraction/main_quantitative_evidence.md) contains 108 local extraction records. The [complete support map](review_1_6_2/extraction/support_quantitative_evidence.md) preserves 47 prospective protocol records plus seven peripheral groups and 35 other-support groups. These extraction families overlap the global relationship inventories and must not be added as independent findings.

| Review layer | Completed scope | Durable record |
|---|---|---|
| Numeric consistency | 112 numeric families, N001–N112 | [Numeric inventory](review_1_6_2/relationships/numeric_relationship_inventory.md); [numeric checker](review_1_6_2/checkers/numeric_consistency.md) |
| Cross-source consistency | 14 matched review groups spanning report/report, report/plan and plan-internal comparisons | [Cross-source checker](review_1_6_2/checkers/cross_source_consistency.md) |
| Statistical pass 1 | 67/67 relationships, S001–S067; each PASS_1_COMPLETE | [Statistical inventory](review_1_6_2/statistics/relationship_inventory.md); [pass 1](review_1_6_2/checkers/statistical_pass_1.md) |
| Statistical pass 2 | Same 67/67 relationships; each PASS_2_COMPLETE; zero new findings | [Statistical inventory](review_1_6_2/statistics/relationship_inventory.md); [pass 2](review_1_6_2/checkers/statistical_pass_2.md) |
| Mechanical recheck | C001, C002, C003, C004 and every affected source location | [Evidence recheck](review_1_6_2/verification/evidence_recheck.md) |
| Independent quality audit | Four candidates; nine screening decisions; 27 checker exclusions; all coverage/classification records | [Evidence-quality audit](review_1_6_2/quality/evidence_quality_audit.md) |

The review matched outcome, population, time point, contrast, reference, model, imputation and measurement scale before comparing values. It checked participant flow and evaluability, baseline samples, outcome and safety displays, subgroup partitions, recurrence components, prospective endpoints/models/missingness, and sample-size/interim/multiplicity decisions. Every printed estimate was inside its ordered interval, and printed interval/P pairs agreed in their null-versus-significance reading. Source-supported Pearson/Fisher checks reproduced the relevant binary secondary P values. Normal/log-normal calculations for adjusted estimates remained diagnostics; unavailable covariance, pooled degrees of freedom, GEE contrasts, bootstrap construction and sequential-power implementation were not supplied by assumption.

Pass 2 independently revisited all 27 checker exclusions: numeric 7, cross-source 12 and statistical pass 1 eight. It also reread the two screened-out findings and every candidate's recheck implications. It emitted no new finding, so the conditional second inclusion-screen stage was not applicable. The audit changed no screening decision and added no candidate.

## Inclusion Screening Summary

Inclusion requires reproduction and either Route A, an always-register category, or Route B, all three criteria of being in focus, unresolved by immediate context and bearing on interpretation/extraction. For numeric comparisons the half-unit input/output interval gap must exceed the specified relative 0.05 threshold; interval-versus-test conflicts are never dismissed as rounding. The count was not calibrated to any expected number.

| Decision | Reason code | Finding count |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 7 |
| SCREENED_OUT | NOT_REPRODUCED | 0 |
| SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | 0 |
| SCREENED_OUT | NOTATION_OR_TYPOGRAPHY | 0 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 1 |
| SCREENED_OUT | MODEL_VERSUS_CRUDE | 0 |
| SCREENED_OUT | CONTEXT_RESOLVES | 1 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 0 |
| SCREENED_OUT | PERIPHERAL_COMPARISON | 0 |
| SCREENED_OUT | OUT_OF_FOCUS | 0 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 0 |
| Total screened findings | All decisions | 9 |

Seven INCLUDE findings consolidate into four stable candidates, retaining all finding provenance and affected locations. The two SCREENED_OUT decisions concern secondary-outcome exploratory interpretation, resolved by the retained secondary hierarchy and explicit lack of multiplicity correction, and center representation, resolved by the reported zero estimated center variance. Neither reproduces the premise of a Route A category-5 change. These counts reconcile to the single [independent screening log](review_1_6_2/screening/inclusion_screen.md). The 27 self-excluded checker observations are a separate accounting layer, not additional independently screened finding IDs; all were revisited by pass 2 and the audit.

## Review-Domain Summary

| Review domain | Definition | Stable candidate count |
|---|---|---:|
| statistical_results | Counts, denominators, estimates, intervals, tests and statistical method logic in report material | 1 |
| report_internal_inconsistency | Report conflicts about the outcome, time, analysis set or comparison to which a result belongs | 0 |
| protocol_report | Report versus prospective plan differences in statistical design or analysis | 3 |
| plan_material | Plan-internal inconsistencies in statistical design relied on by reported analysis | 0 |
| Total | One domain per stable candidate | 4 |

| Primary relationship type | Definition | Stable candidate count |
|---|---|---:|
| P_R | REPORT differs from PLAN | 3 |
| P_P | Conflict solely within PLAN | 0 |
| S_C | Conflict between different REPORT documents | 0 |
| S_W | Conflict within one REPORT document | 1 |
| Total | One primary relationship per candidate | 4 |

C002 additionally involves P_P; precedence P_R > P_P > S_C > S_W makes P_R primary. Counts of memberships in All relationships are P_R=3, P_P=1, S_C=0 and S_W=1; these five memberships overlap across four candidates. Corroborating documents are not additional conflicting relationships.

| Evidence state | Stable candidate count |
|---|---:|
| reproduced | 4 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| Total | 4 |

Inclusion audit: CONFIRMED=4; QUESTIONED=0. All four remain Pending Human Adjudication.

## Candidate Index

| ID | Candidate reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| C001 | Planned complication comparison has no supplied comparative result | protocol_report | P_R | reproduced | CONFIRMED |
| C002 | Strict versus inclusive primary recurrence boundary | protocol_report | P_R | reproduced | CONFIRMED |
| C003 | Disclosed cause-restricted death amendment in primary composite | protocol_report | P_R | reproduced | CONFIRMED |
| C004 | Midline-shift samples exceed stated unilateral populations | statistical_results | S_W | reproduced | CONFIRMED |

## Candidate Evidence Cards

## C001 — Planned complication comparison has no supplied comparative result

Pending Human Adjudication.

**Candidate statement:** The supplied protocol and SAP explicitly specify a between-arm comparison of minor and major procedure complications, whereas the abstract-listed endpoint is reported with intervention-arm risks alone and no identifiable comparative result in the supplied reports.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol/SAP complication analysis vs REPORT main article/results supplement complication reporting

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-005, F-ST1-003

**Qualifying route:** Route A, category 5

**Classification rationale:** The prospective protocol/SAP analysis specifications are PLAN; the executed-results article and results supplement are REPORT. Matching plans and matching reports do not add P_P or S_C. The conflicting planned-versus-reported analysis relationship is P_R.

**Classification ambiguity:** The control endpoint definition, performed or replaced comparative analysis and any corresponding documented change are not supplied.

**Exact source locations:** PLAN [joi250033supp1_prod_1750956987.76581.pdf — p. 50, secondary-endpoint analysis](../joi250033supp1_prod_1750956987.76581.pdf#page=50); PLAN [joi250033supp5_prod_1750956987.78281.pdf — p. 4, section 2.2](../joi250033supp5_prod_1750956987.78281.pdf#page=4), [p. 7, section 3.6 fifth bullet](../joi250033supp5_prod_1750956987.78281.pdf#page=7). REPORT [jama_shotar_2025_oi_250033_1750956987.75881.pdf — p. 1, abstract](../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=1), [p. 3, Secondary End Points/Statistical Analysis](../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=3), [p. 6, Table 2 complication rows, footnote j and narrative](../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=6), [p. 7, complication narrative](../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=7). REPORT [joi250033supp4_prod_1750956987.77981.pdf — p. 12, eTable 3](../joi250033supp4_prod_1750956987.77981.pdf#page=12), [p. 13, eTable 3 continuation](../joi250033supp4_prod_1750956987.77981.pdf#page=13).

**Source evidence:** Both plans specify experimental-versus-control complication comparisons using chi-square or Fisher exact tests as appropriate. The abstract lists complications among secondary endpoints and reports minor 3/171 (1.8%) and major 1/171 (0.6%). Table 2 presents those risks and components, with blank standard-care, difference/interval and P cells. Its footnote points to eTable 3, which has only an Embolization (N=171) column. The narrative describes one thrombectomy event, two transient neurological deficits and one headache. The separate adverse-event comparison in Table 3 is not the named procedure-complication comparison.

**Reported-versus-comparator:** Reported intervention-only major/minor risks and descriptions versus the explicit planned two-arm chi-square/Fisher complication analysis. The abstract's general statement about secondary endpoints does not identify a complication-specific comparative result.

**Reasoning procedure:** Match the endpoint and planned analysis across both plans; establish key-secondary relevance from its abstract listing; inspect main Table 2, its linked complete eTable 3 and report narrative/methods for the corresponding comparator and inference. The complete supplied report mapping and source search located no such result. Preserve blank cells as unavailable values.

**Calculation:** The descriptive risks reconcile: 100×1/171=0.584795%, 100×3/171=1.754386% and 100×2/171=1.169591%. Allowing half-unit intervals for every input gives [0.291545,0.879765]%, [1.457726,2.052786]% and [0.874636,1.466276]%, overlapping printed 0.6±0.05%, 1.8±0.05% and 1.2±0.05%; gap zero. The candidate is a categorical planned-analysis comparison, not a percentage discrepancy. No control count or test is computed from blank cells.

**Affected result or extracted value:** Whether the key secondary minor/major procedure-complication endpoint has comparative inference accompanying intervention risks 1.8% and 0.6%.

**Why context does not resolve it:** Route A, category 5 registers a planned key secondary analysis that is not reported. Procedure-specific descriptive safety reporting can explain an alternative presentation but does not supply the explicitly planned comparative result.

**Alternative source-grounded interpretations:** Because controls did not undergo embolization, the investigators may have intentionally used descriptive intervention-only safety reporting; alternatively a comparison may have been performed and omitted from supplied reporting. The package does not establish which occurred or provide a replacement-analysis specification. No preferred analysis is proposed.

**Mechanical evidence recheck:** Every cited location and printed plan/report statement was found and matched. Current-source main p. 6 rendering confirmed the blank comparator cells; full eTable 3 inspection confirmed the single intervention column. The planned-versus-reported logical comparison and descriptive arithmetic reproduced. Roles, P_R and domain were retained. Missing inputs are the control endpoint definition, executed comparative result and any analysis-change documentation; these limit characterization of the realized analysis, not the observable supplied-source comparison. The remaining question is whether the planned comparison was performed or replaced and what result or documented change accompanies this endpoint.

**Potential downstream evidence impact:** An extractor could copy the 0.6% and 1.8% risks as intervention-only descriptive results. A comparative safety estimate for this key-secondary endpoint is not supplied. No propagation, treatment-conclusion change or harm is established.

## C002 — Strict versus inclusive primary recurrence boundary

Pending Human Adjudication.

**Candidate statement:** The SAP prints a primary-composite midline-shift criterion >5 mm, whereas the supplied protocol, main article and results supplement use ≥5 mm or equivalent inclusive wording.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN SAP primary threshold vs REPORT main article/results supplement and PLAN protocol primary threshold

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001, F-ST1-002

**Qualifying route:** Route A, category 5

**Classification rationale:** SAP/protocol locations are prospective PLAN and article/results locations are REPORT. SAP versus report establishes P_R; the independent SAP versus protocol boundary comparison establishes P_P. P_R has precedence. Agreeing report copies add no S_C.

**Classification ambiguity:** The applied adjudication boundary and measurement/rounding implementation are not supplied.

**Exact source locations:** PLAN [joi250033supp5_prod_1750956987.78281.pdf — p. 3, section 2.1 first bullet](../joi250033supp5_prod_1750956987.78281.pdf#page=3). PLAN [joi250033supp1_prod_1750956987.76581.pdf — p. 7, synopsis](../joi250033supp1_prod_1750956987.76581.pdf#page=7), [p. 16, section 4.1.1 primary endpoint](../joi250033supp1_prod_1750956987.76581.pdf#page=16), [p. 21, both follow-up recurrence definitions](../joi250033supp1_prod_1750956987.76581.pdf#page=21), [p. 31, section 8.1](../joi250033supp1_prod_1750956987.76581.pdf#page=31). REPORT [jama_shotar_2025_oi_250033_1750956987.75881.pdf — p. 3, End Points](../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=3). REPORT [joi250033supp4_prod_1750956987.77981.pdf — p. 11, eTable 2 criteria 1 and 1a](../joi250033supp4_prod_1750956987.77981.pdf#page=11), [p. 15, EMPROTECT primary endpoint](../joi250033supp4_prod_1750956987.77981.pdf#page=15).

**Source evidence:** The SAP visibly prints >5 mm. Protocol locations repeat ≥5 mm or expanded inclusive wording; the article says 5 mm or greater. Results-supplement criteria 1/1a and its EMPROTECT summary print ≥5 mm. The shift branch contains 11/24 intervention and 17/33 control recurrence cases, not identified exact-boundary cases.

**Reported-versus-comparator:** Inclusive primary recurrence criterion in protocol/report versus strict criterion in SAP for the otherwise matched homolateral recurrence component.

**Reasoning procedure:** Match the primary composite's shift branch, distinguish it from symptomatic recurrence and the separate >10-mm thickness branch, visually confirm the SAP operator and compare predicates at the boundary. Keep other qualifying components and actual implementation separate from the printed definitions.

**Calculation:** For an asymptomatic otherwise qualifying recurrence with x=5.0 mm and no other qualifying component, x>5 is false and x≥5 is true. The two predicates therefore define different inclusion sets. Half-unit numeric discrepancy arithmetic does not reconcile an inclusion operator. The 11 and 17 shift-component counts do not reveal how many cases were exactly 5 mm, so no numerical count or treatment-effect change is calculated.

**Affected result or extracted value:** Primary recurrence definition attached to observed 24/162 versus 33/157, adjusted OR 0.64 (95% CI, 0.36–1.14), and its midline-shift component.

**Why context does not resolve it:** Route A, category 5 registers a reproduced difference in a primary-composite definition. Repeated inclusive definitions do not determine which printed boundary was implemented.

**Alternative source-grounded interpretations:** The inclusive rule may have governed all adjudications despite the SAP's strict wording; alternatively the strict boundary may have been implemented and reported inclusively. Symptoms, thickness, surgery or readmission could independently qualify an exactly-boundary case. Actual boundary cases and their other criteria are unavailable.

**Mechanical evidence recheck:** Every source location and operator was found and matched; the current-source SAP render confirmed the strict glyph and targeted protocol reads confirmed inclusive wording. The protocol p. 16 section label was corrected to 4.1.1 before stable registration, without changing a registered value. The predicate comparison reproduced; roles, P_R/P_P precedence and domain were retained. Missing inputs are the applied rule, measurement conventions, exact-boundary cases and other criteria. The remaining question is which boundary governed adjudication and whether any case qualified solely at exactly 5 mm.

**Potential downstream evidence impact:** An extractor could attach either >5 mm or ≥5 mm to the primary result and adjusted OR. The available package does not establish a changed participant count, effect estimate, significance reading or clinical conclusion.

## C003 — Disclosed cause-restricted death amendment in primary composite

Pending Human Adjudication.

**Candidate statement:** The original protocol treats deaths without recurrence as primary failures without a cause restriction; the reported final composite uses neurological/unknown-cause deaths as recurrences and imputes other-cause deaths as nonevaluable outcomes. **SAP version 2 explicitly documents this amendment and states that its final version was prepared before final database lock.**

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN original protocol death rule vs REPORT main article/results supplement final death rule; PLAN final SAP corroborates and discloses amendment

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002, F-ST1-001

**Qualifying route:** Route A, category 5

**Classification rationale:** Original final protocol PLAN differs from final article/results REPORT. The amended final SAP corroborates the report and expressly documents the change; it is context rather than an additional unresolved P_P relationship. Distinct interim/final and primary/sensitivity rules have explicit stage/analysis labels and do not add S_C or S_W conflicts.

**Classification ambiguity:** Amendment disclosure is explicit. Its authorization/lock records beyond the supplied statement and its quantitative effect are not reconstructed. SAP version 2 is dated 2024/02/28 in the version table; its document heading is 20/03/2024 and signatures 15/04/2024. These separate descriptions do not establish reconstructed authorization dates.

**Exact source locations:** PLAN [joi250033supp1_prod_1750956987.76581.pdf — p. 48, interim analysis](../joi250033supp1_prod_1750956987.76581.pdf#page=48), [p. 49, final primary analysis](../joi250033supp1_prod_1750956987.76581.pdf#page=49). PLAN [joi250033supp5_prod_1750956987.78281.pdf — p. 5, interim analysis](../joi250033supp5_prod_1750956987.78281.pdf#page=5), [p. 6, final analysis](../joi250033supp5_prod_1750956987.78281.pdf#page=6), [p. 8, version-change table](../joi250033supp5_prod_1750956987.78281.pdf#page=8). REPORT [jama_shotar_2025_oi_250033_1750956987.75881.pdf — p. 3, Statistical Analysis](../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=3), [p. 4, Figure 1](../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=4), [p. 5, Primary End Point narrative](../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=5), [p. 6, Table 2](../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=6). REPORT [joi250033supp4_prod_1750956987.77981.pdf — p. 5, imputation methods](../joi250033supp4_prod_1750956987.77981.pdf#page=5), [p. 9, no-imputation sensitivity footnote](../joi250033supp4_prod_1750956987.77981.pdf#page=9), [p. 11, recurrence/death criteria](../joi250033supp4_prod_1750956987.77981.pdf#page=11).

**Source evidence:** The original protocol's final-analysis paragraph assigns failure to deaths without recurrence without restricting cause. Final SAP p. 6 restricts those failures to neurological/undetermined deaths; p. 8 expressly lists the changed definition. The report matches the amended rule. Figure 1 lists other-cause deaths 3/8 among nonevaluable outcomes; the primary components include neurological/undetermined deaths 2/1. Main p. 5 repeats the event decomposition. The no-imputation sensitivity separately assigns non-neurological deaths no event under its own label.

**Reported-versus-comparator:** Original all-death failure definition versus the disclosed cause-restricted final recurrence definition with imputation of other-cause nonevaluable outcomes. Final SAP and final report agree.

**Reasoning procedure:** Compare original and amended final-analysis death sets, preserve interim/final distinctions, match the final rule to flow/narrative/table/component displays and retain amendment history. Separate observed counts from imputed inference and from the labeled no-imputation sensitivity.

**Calculation:** Observed components reconcile: 22+2=24 and 32+1=33. Nonevaluable totals are 5+3+1=9 and 8+5+1=14, leaving 171−9=162 and 171−14=157 evaluable. Half-unit event-component sums [23,25] and [32,34] overlap printed event intervals 24±0.5 and 33±0.5; gap zero. A non-neurological death without prior recurrence is a failure under the original rule but is not directly assigned recurrence under the final rule. Numeric rounding cannot reconcile those categorical sets. The aggregate 3/8 other-cause deaths do not supply a counterfactual original-rule adjusted OR, imputed event total or P value.

**Affected result or extracted value:** Primary composite definition and death/missingness handling accompanying 24/162 versus 33/157 and multiply imputed adjusted OR 0.64 (95% CI, 0.36–1.14), P=.13.

**Why context does not resolve it:** Route A, category 5 registers a reproduced composite-definition change. The expressly disclosed final-SAP amendment is material context and remains prominent; disclosure does not remove that route-A comparison.

**Alternative source-grounded interpretations:** This may be an intended prospectively documented final-analysis amendment, consistent with the SAP statement that its final version preceded final database lock. The final SAP and report are coherent with that amended definition. The original broader rule remains a distinct supplied specification; the package provides no quantified primary result under it. No unauthorized change or concealment is inferred.

**Mechanical evidence recheck:** Every affected plan/report location and statement was found and matched, including the additional main p. 5 narrative occurrence retained in this card. Current-source main p. 6 and results p. 9 renders confirmed component counts and sensitivity coding. Logical death-set comparison and observed arithmetic reproduced. Roles, P_R alone and domain were retained because the final SAP corroborates and discloses the amendment. Individual cause/prior-recurrence overlap, imputed datasets and an original-definition fitted result are absent. The remaining question is how the supplied amendment should accompany extraction of the final result and whether an original-definition analysis is available.

**Potential downstream evidence impact:** An extractor could associate the original all-death rule or amended cause-restricted/imputed rule with the primary OR and observed counts. Recording the reported final definition together with the supplied amendment context could prevent ambiguity in endpoint mapping. No actual treatment-estimate, significance or conclusion change is established.

## C004 — Midline-shift samples exceed stated unilateral populations

Pending Human Adjudication.

**Candidate statement:** Main Table 1 describes midline-shift summaries as unilateral-only but prints n=161 in each arm, exceeding the same display's unilateral populations of 127 and 130.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 1 midline-shift samples vs REPORT same-table unilateral populations and footnote

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Qualifying route:** Route A, category 3

**Classification rationale:** The participant sample constraint concerns counts within one REPORT display. No plan or other report document is a conflicting comparator. Counts/populations determine statistical_results with S_W.

**Classification ambiguity:** The intended participant sample/population or a different measurement unit is not specified.

**Exact source locations:** REPORT [jama_shotar_2025_oi_250033_1750956987.75881.pdf — physical p. 5, Table 1 headers, Unilateral CSDH row, Midline shift row and continuation footnote d](../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=5). Physical p. 5 is printed journal p. 131; evidence links use physical pagination.

**Source evidence:** Group headers are n=171 each. Unilateral CSDH is 127 (74.3%) versus 130 (76.0%). Midline shift is median 10 mm (IQR, 7–13) [n=161] versus 10.5 mm (IQR, 7–14) [n=161]. Superscript d links that row to the footnote limiting the data to unilateral CSDH.

**Reported-versus-comparator:** Each printed participant sample n=161 versus the same-arm unilateral population 127/130 under the table's explicit unilateral-only restriction.

**Reasoning procedure:** Visually verify row alignment, both sample labels and the superscript/footnote linkage; apply the patient-subset constraint separately by arm; allow half-unit rounding intervals for all counts. Treat both arms as one repeated pattern and distinguish feasible full-arm samples from the stated unilateral restriction.

**Calculation:** Central excesses are 161−127=34 and 161−130=31. With each sample in [160.5,161.5] and unilateral populations in [126.5,127.5] and [129.5,130.5], minimum gaps are 160.5−127.5=33 and 160.5−130.5=30. Relative discrepancies are 33/161=0.204968944 and 30/161=0.186335404, both above 0.05. Individual unilateral percentages reconcile: 100×127/171=74.269006% and 100×130/171=76.023392%, compatible with the printed 74.3% and 76.0%.

**Affected result or extracted value:** Both sample sizes and the unilateral/full-arm population attached to the baseline midline-shift medians 10 and 10.5 mm.

**Why context does not resolve it:** Route A, category 3 covers the reproduced within-display count constraint. Independently Route B applies: the sample/population counts are in focus, the table does not identify which population/sample labels govern extraction, and those labels determine the samples attributed to the named medians. This is not a comparison of baseline copies across documents.

**Alternative source-grounded interpretations:** The n=161 samples are feasible under full-arm n=171 and might include bilateral participants despite the footnote; alternatively the sample labels could denote another unstated set or unit. The table does not define repeated-scan or hemisphere-level samples, so neither explanation is a fact. Ordered medians/IQRs do not identify the intended population.

**Mechanical evidence recheck:** Current-source text and visual rendering confirmed both unilateral counts, sample labels, medians/IQRs and footnote linkage. The subset rule and half-unit minimum gaps reproduced. REPORT role, S_W and statistical_results were retained. Individual measurements and intended sample/unit definitions are unavailable. The remaining question is which participants and sample sizes underlie each median; no replacement n or median is proposed.

**Potential downstream evidence impact:** An extractor could attribute n=161 to each unilateral-only summary or use an unidentified unilateral sample. The sample sizes and represented population therefore need clarification. No discrepancy in the medians themselves, primary treatment estimate or clinical conclusion is established.

## Downstream Evidence-Chain Considerations

Evidence extraction can carry endpoint definitions, populations, time points, sample sizes and comparative-versus-descriptive labels alongside estimates. A systematic review or meta-analysis could reuse one of these fields without retaining its plan/version context. These candidates identify specific points where that mapping could need clarification. They do not establish that a value has propagated, that a synthesis or guideline conclusion has changed, or that harm has occurred. No preferred analysis or final correction is proposed.

## Limitations and Missing Definitions

All supplied-source units have complete scientific mapping; there is no supplied-page coverage gap. Cited Supplements 2, 6 and 7, a separate DSMB charter and separate analysis inputs are not supplied and were not obtained or assigned inferred contents. The scope therefore cannot establish whether unavailable documents contain additional amendment or analysis information.

Raw participant measurements, ranks, exact-boundary cases and their other composite criteria, death-cause/prior-recurrence overlap, imputed datasets and fitted-model coefficients/covariances are unavailable. GEE contributor coding, correlation/variance/contrast definitions, exact pooled test degrees of freedom, bootstrap construction and full sequential power/spending implementation are not provided. Actual interim statistics and conditional-power outputs are not supplied. These bound exact numerical replication and do not independently create candidates.

Candidate-specific limits are the executed complication comparison/control definition (C001), implemented boundary and exact-boundary cases (C002), original-definition primary result and quantitative amendment effect (C003), and intended sample/population/unit underlying the medians (C004). Blank cells are not zero counts. Observed fractions are not imputed event totals. No aggregate-count reconstruction supplies a counterfactual adjusted estimate.

Some historical extraction/OCR engine versions are undocumented. Current candidate confirmations use exact supplied-source text/renders, with pinned engine provenance where newly produced. Direct PDF/OCR utilities were absent; the recorded temporary package-local fallback covered needed PDF information, text/layout and rendering. Existing reusable OCR/images made new OCR unnecessary, including image-rich administrative units. The complete limitation record is [limitations.md](review_1_6_2/limitations.md).

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

### Reproducibility and source integrity

The review used only the supplied package. [Routing preflight](review_1_6_2/routing_preflight.md) reports PASS, run model gpt-6.1-sol, source DEFAULT, execution INTERACTIVE_CLI, provider CURRENT_SESSION, coordinator inference PASS and ten verified named presets. The [source inventory](review_1_6_2/source_inventory.md), evidence inventory, coverage manifest, relationship inventories, screening log, ledger, recheck and audit retain the durable chain from source units to all four cards.

Direct sha256sum checks at curation/audit and final post-assembly recomputation matched all five supplied-source hashes and all 296 reused-asset hashes. The final [source hashes](review_1_6_2/source_hashes_after.sha256) and [reused-asset hashes](review_1_6_2/reused_artifact_hashes_after.sha256) are identical to their before inventories. The audit mechanically checked 621 earlier PDF evidence links for existing targets, valid physical pages and #page=N anchors. The standalone HTML uses embedded styling and local links. Final mechanical validation is recorded in [review_validation.json](review_1_6_2/review_validation.json); temporary-tooling removal is recorded in the [bootstrap log](review_1_6_2/tooling/bootstrap_log.json) and tooling record. These local completion operations follow scientific Markdown assembly and do not extend the recorded review duration.

Tooling is recorded in [tooling_record.md](review_1_6_2/tooling_record.md). Linux probe time was 2026-10-11T16:07:56Z. Direct pdfinfo, pdftotext, pdftoppm, pdftocairo, tesseract and libreoffice were absent; pandoc was available. Temporary fallback packages were PyMuPDF==1.26.4 and pypdf==5.9.0, with info/text/layout/render used. Targeted PDF renders ran on CPU. The user requested GPU OCR and selected the existing /home/juliz/venvs/stt/bin/python environment, containing rapidocr-onnxruntime==1.4.4 and onnxruntime-gpu==1.28.0. Read-only Windows PowerShell 5.1/nvidia-smi checks confirmed an RTX 5070 Laptop GPU with driver 616.56. No new OCR or GPU OCR was required. Historical OCR reuse is distinct from current CPU rendering; no global packages were installed. The temporary fallback is removed after rendering, with its actual removal state retained in the linked tooling records.

### Agent execution

The following complete manifest contains 13 distinct runtime IDs. All specialists were fresh distinct spawns. Ordinary specialists used medium effort; statistical, screening, recheck and audit specialists used high effort. The coordinator used high effort. The two statistical agents were distinct from each other and all other stages.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12bb5-7d06-7e53-8626-6674bf5f1f12 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12bba-670c-7de2-bbc2-d54fc0338c04 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12bbd-7fc1-77e2-aba1-6d633239c859 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12bbd-b9c8-7193-ab38-81d4361d11e9 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_other | 01a12bbd-f041-7681-ae2d-1e570d8c0948 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/other_support_quantitative_evidence.md |
| numeric_consistency_reviewer | 01a12bc4-5fd4-75e2-83e5-902a2215ae7a | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a12bc4-a327-7353-973d-873176305f75 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a12bc4-da4e-7872-9b54-7504ad4553d6 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a12bd0-1da8-7853-a91b-e1e467622b2b | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a12bd5-58d1-7073-87fa-573d501cd889 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a12bda-7e88-79b3-87e9-04b0f5c2fa7b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | 01a12be2-17c4-7ae0-bdd1-fa336db2aeec | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a12be9-d67e-7bb3-8e6e-dae568a2c5e0 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Artifact paths in the manifest are relative to review_1_6_2/. The durable [execution manifest](review_1_6_2/agent_execution_manifest.md) retains stage provenance. No second screener was required because statistical pass 2 emitted zero new findings.

### Reproducibility performance

- **Target basis:** Five PDF sources contain 119 physical pages with 119 reusable units and no fresh-required extraction units. Main/results tables and figures and seven administrative image pages have retained visual assets. Full protocol, prospective addenda and SAP mapping remains required. Three bounded text mapping scopes (main; protocol; addenda/results/SAP) and the mandatory mapping, checker, screening, recheck, second statistical pass, audit and report waves are expected; no Office conversion or new OCR is currently required. A 30–45 minute planning target reflects low preprocessing burden and full prospective/report relationship reconstruction.
- **Total source units:** 119
- **Fresh-source units:** 0
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-10-11T16:09:06Z
- **Finished UTC:** 2026-10-11T17:06:48Z
- **Observed elapsed minutes:** 57.70
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Complete sequential high-effort review waves covered 67 statistical relationships twice, nine independent screening decisions, four source-confirmed candidate rechecks and all 27 exclusions in the audit; targeted source confirmation, full audit documentation and complete report assembly extended the 30-45 minute planning target. No source unit or candidate was omitted to meet the target.
