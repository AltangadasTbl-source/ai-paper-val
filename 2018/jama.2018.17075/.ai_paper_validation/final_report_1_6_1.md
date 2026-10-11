# Quantitative Quality-Control Consistency Review — POLAR Randomized Clinical Trial

**Pending Human Adjudication**

Workflow 1.6.1 reviews quantitative reporting in the supplied package. Every candidate below remains Pending Human Adjudication. Evidence states and inclusion-audit decisions describe the review record; they do not adjudicate the paper or authorize a final correction.

## Executive Quality-Control Summary

Complete mapping of four supplied PDFs, comprising 229 pages, produced 140 numeric and 110 statistical relationships. Two distinct high-effort statistical agents reviewed all 110 statistical relationships. Independent inclusion screening considered seven checker findings: six included finding rows were consolidated into four stable candidates, and one finding was screened out. Exact-source recheck assigned `reproduced` to all four candidates; the independent quality-control audit recorded `CONFIRMED` inclusion for all four, with no additional finding.

The candidates concern assigned temperature-management duration, an internally incompatible Injury Severity Score quantile summary, attribution of a time-to-target-temperature test, and a repeated bleeding inferential-result pattern. Three belong to `statistical_results` and one to `protocol_report`. No inference is made about changed primary conclusions, actual downstream propagation, intervention adherence or clinical harm. C003 is expressly a bounded Pearson diagnostic and method/result-attribution question, rather than a reconstruction of unspecified original software output.

## Package and Reused-Evidence Provenance

The main report is the POLAR trial article by Cooper and colleagues, supplied as `jama_cooper_2018_oi_180132.pdf`. Document roles follow content: the main article, results supplement and data-sharing statement are REPORT; the protocol/SAP/amendment/DSMC governance bundle is PLAN. Embedded operational displays were identified by their content during mapping; the bound bundle was not treated as an independent completed-trial results supplement merely because of its filename.

| Source ID | Supplied source | Role | PDF pages | SHA-256 |
|---|---|---|---:|---|
| DOC-001 | [jama_cooper_2018_oi_180132.pdf](<../jama_cooper_2018_oi_180132.pdf#page=1>) | REPORT | 10 | `14987ad9741b9c9f617a24af239ae72407ffe41ee14953df33665f1593e35253` |
| DOC-002 | [joi180132supp1_prod.pdf](<../joi180132supp1_prod.pdf#page=1>) | PLAN | 194 | `305596802f9ac59c1e76fd9233529b98d92ef918d13fccd35112109ed60cb547` |
| DOC-003 | [joi180132supp2_prod.pdf](<../joi180132supp2_prod.pdf#page=1>) | REPORT | 24 | `b00fbac777719817be84e45f350898aa031a3eb6d17fb73a42de710239f1ab7d` |
| DOC-004 | [joi180132supp3_prod.pdf](<../joi180132supp3_prod.pdf#page=1>) | REPORT | 1 | `7d6634553269ddfc0208a4e0d7b46639b8212f3126d59e3add8b4b033d42ebf3` |

The curator inventoried and hash-protected 285 eligible preprocessing assets: four complete native texts, four layout texts, 229 rendered pages, 43 single-page excerpts, four PDF-information records and one document/page locator. These reside in the existing `review_1_5_2/preprocessing/` directory and were preserved. No earlier candidate set, checker conclusion, screening record, classification, adjudication record or report supplied scientific discovery input.

All complete native text files matched current direct-source `pdftotext` output. Plan native/layout text was partial on 27 pages, but readable source-matched rendered pages covered them. Overlapping excerpts were locators, not additional unique units. Current identity and confirmation tools used Poppler 25.03.0 and SHA-256; the legacy image renderer/version is unrecorded. Reused evidence located content; direct supplied PDF pages were the final authority for every candidate.

Full provenance appears in the [source inventory](review_1_6_1/source_inventory.md), [evidence-asset inventory](review_1_6_1/evidence_asset_inventory.md), [source hashes](review_1_6_1/source_hashes_before.sha256) and [reused-artifact hashes](review_1_6_1/reused_artifact_hashes_before.sha256).

## Scope, Complete Coverage, and Exclusions

The review covered counts and denominators, estimate/test logic, statistical method logic, and planned-versus-reported statistical design. Mapping covered the complete supplied evidence, including historical and final plans, amendments, interim governance material, non-plan supplementary tables/figures, and the data-sharing statement. Historical specifications were distinguished from disclosed final changes. This was not a raw-data, clinical-methods, novelty or misconduct review, and no preferred analysis was proposed.

| Source ID | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-002 | 194 | 194 | 0 | 194 | COMPLETE |
| DOC-003 | 24 | 24 | 0 | 24 | COMPLETE |
| DOC-004 | 1 | 1 | 0 | 1 | COMPLETE |
| Total | 229 | 229 | 0 | 229 | COMPLETE |

Reusable-backed units and fresh-required units partition every direct source. Zero fresh-required units means that usable derivatives existed for every page; scientific discovery and mapping were conducted afresh across every unit. All 27 native-blank plan pages—140–162, 183–185 and 187—were visually mapped. Sparse raster instruments and flowcharts, including plan page 39 and pages 103–107, also received visual inspection. The main mapper covered pages 1–10; three disjoint support scopes covered plan pages 1–69, 70–138 and 139–194, with the final support scope also covering all 25 remaining support pages. No scientific-coverage gap remains.

The [source-coverage ledger](review_1_6_1/source_coverage.md), [coverage manifest](review_1_6_1/coverage_manifest.md), [main map](review_1_6_1/extraction/main_quantitative_evidence.md) and [support map](review_1_6_1/extraction/support_quantitative_evidence.md) preserve the assignments and applicability decisions. Each coverage-manifest row names one artifact path.

Rounding/display precision, immediately resolvable notation or wording, adjusted estimates compared with crude ratios, conditional computations, peripheral cross-location descriptions and out-of-focus observations were excluded under the scope rules. A display-zero P value alone was not registered. Descriptive baseline differences between documents and per-time-point contributor counts were peripheral unless they changed an eligible result, analysis-population size or decision rule. C002 instead concerns the ordering of quantiles within one distribution cell.

## Quantitative and Statistical Relationship Coverage

The [numeric inventory](review_1_6_1/relationships/numeric_relationship_inventory.md) contains N001–N140; the [statistical inventory](review_1_6_1/statistics/relationship_inventory.md) contains S001–S110. Grouped relationships retain their underlying counts, estimates, confidence limits, populations, contrasts, time points, methods and matching locations. The [ID crosswalk](review_1_6_1/relationships/id_crosswalk.md) preserves transfer from mapping without selection.

| Review stage | Complete scope | Artifact |
|---|---|---|
| Numeric review | All 140 numeric relationships and underlying mapped cells | [Numeric checker](review_1_6_1/checkers/numeric_consistency.md) |
| Cross-source review | All matched REPORT/PLAN result-relevant relationships | [Cross-source checker](review_1_6_1/checkers/cross_source_consistency.md) |
| Statistical pass 1 | All S001–S110; explicit PASS_1_COMPLETE records | [Pass 1](review_1_6_1/checkers/statistical_pass_1.md) |
| Statistical pass 2 | All S001–S110; complete ledger, screening and recheck; explicit PASS_2_COMPLETE records | [Pass 2](review_1_6_1/checkers/statistical_pass_2.md) |

Pass 1 used fresh agent `/root/statistics_1`; pass 2 used distinct fresh agent `/root/statistics_2`, both `gpt-6.1-sol`/`high`. Pass 2 revisited all statistical relationships and the cross-lane candidates, including the C002 within-cell quantile distinction. It emitted no new finding, so no pass-2 inclusion screener was required. Neither pass replaced adjusted effects with crude ratios, assumed unprinted model inputs, or interpreted a nonsignificant superiority comparison as equivalence.

The independent [evidence recheck](review_1_6_1/verification/evidence_recheck.md) directly extracted, rendered and visually read all nine unique candidate source pages. The [quality audit](review_1_6_1/quality/evidence_quality_audit.md) covered every stable ID, all screening decisions, all 102 checker excluded-observation rows, every coverage row and all classifications. It found no additional qualifying issue or screening repair.

## Inclusion Screening Summary

Inclusion required a reproduced, in-focus comparison that was not resolved at once by immediate context and could change interpretation or extraction of a named result. The fresh independent screener reread cited sources and consolidated repeated findings without a candidate-count target.

| Decision | Reason code | Finding rows |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 6 |
| SCREENED_OUT | CONTEXT_RESOLVES | 1 |
| SCREENED_OUT | NOT_REPRODUCED | 0 |
| SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | 0 |
| SCREENED_OUT | NOTATION_OR_TYPOGRAPHY | 0 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 0 |
| SCREENED_OUT | MODEL_VERSUS_CRUDE | 0 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 0 |
| SCREENED_OUT | PERIPHERAL_COMPARISON | 0 |
| SCREENED_OUT | OUT_OF_FOCUS | 0 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 0 |
| Total screened findings | All decisions | 7 |

Six INCLUDE rows map to four distinct issues: C001/F-XS-002; C002/F-NUM-002; C003/F-ST1-002; C004/F-NUM-001, F-XS-001 and F-ST1-001. The three bleeding findings remain included provenance under one repeated-pattern candidate. F-XS-003 was screened out as CONTEXT_RESOLVES: the supplied monitoring framework distinguishes nominal alpha .05 from a slightly adjusted final-look boundary, and no identified primary/key-secondary decision depended on the narrow threshold difference. No conclusion about the actual software cutoff was made. The [screening log](review_1_6_1/screening/inclusion_screen.md) contains exactly one decision per emitted finding.

Checker self-exclusions are a separate accounting set: numeric 28, cross-source 26, statistical pass 1 26 and statistical pass 2 22, totaling 102 observation rows audited. They are not added to the seven independently screened finding rows. The audit reviewed both inclusion and exclusion directions and changed no screening decision.

## Review-Domain Summary

`statistical_results` covers counts, estimates, intervals, tests and statistical methods in REPORT material. `report_internal_inconsistency` covers an unresolved conflict about the outcome, time point, analysis set or contrast to which a reported number belongs. `protocol_report` covers REPORT-versus-PLAN statistical design or analysis elements. `plan_material` covers such inconsistencies solely within PLAN material. These are human-review categories, not adjudications.

| Review domain | Stable candidates |
|---|---:|
| statistical_results | 3 |
| report_internal_inconsistency | 0 |
| protocol_report | 1 |
| plan_material | 0 |
| Total | 4 |

| Primary relationship type | Meaning | Stable candidates |
|---|---|---:|
| P_R | REPORT versus PLAN | 1 |
| P_P | Solely within PLAN | 0 |
| S_C | Between different REPORT documents | 2 |
| S_W | Within one REPORT document | 1 |
| Total | One primary type per candidate | 4 |

All-relationship sets are P_R for C001, S_W for C002, and S_C, S_W for C003/C004. S_C takes precedence over S_W in the latter two. Corroborating plan content does not create a conflicting relationship.

| Evidence state | Stable candidates |
|---|---:|
| reproduced | 4 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| Total | 4 |

Inclusion audit: CONFIRMED 4; QUESTIONED 0. Every candidate remains Pending Human Adjudication regardless of these record fields.

## Candidate Index

| Stable ID | Candidate | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| C001 | Assigned management duration | protocol_report | P_R | reproduced | CONFIRMED |
| C002 | Injury Severity Score quantile ordering | statistical_results | S_W | reproduced | CONFIRMED |
| C003 | Timing-test attribution | statistical_results | S_C | reproduced | CONFIRMED |
| C004 | Bleeding inferential blocks | statistical_results | S_C | reproduced | CONFIRMED |

## Candidate Evidence Cards

## C001 — Duration attributed to assigned normothermic management

**Pending Human Adjudication**

**Candidate statement:** The report describes temperature management in both groups for 7 days, while the final plan specifies 96 hours for control/all-patient pyrexia avoidance followed by local unit/ward care. The duration attributed to randomized comparator and post-rewarming management remains unclear.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main article pp.1,3 vs PLAN final protocol pp.77,101

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002

**Classification rationale:** A reported randomized intervention duration differs from supplied final prospective plan instructions. The plan-only H post-rewarming difference is contextual, rather than an additional statistical-design relationship.

**Classification ambiguity:** Plan p77 gives H post-rewarming normothermia a7-day maximum, while p101 hands post-rewarming/all-patient management to local protocol after96hours. No later extension or actual received-duration distinction is established.

**Exact source locations:**

- [jama_cooper_2018_oi_180132.pdf, PDF p. 1, abstract Interventions; printed p. 2211](<../jama_cooper_2018_oi_180132.pdf#page=1>) — REPORT both-group duration.
- [jama_cooper_2018_oi_180132.pdf, PDF p. 3, Rewarming and Normothermia; printed p. 2213](<../jama_cooper_2018_oi_180132.pdf#page=3>) — REPORT post-rewarming and control management.
- [joi180132supp1_prod.pdf, PDF p. 77, Version 9 §12.11; printed protocol p. 25](<../joi180132supp1_prod.pdf#page=77>) — PLAN control handoff and hypothermia context.
- [joi180132supp1_prod.pdf, PDF p. 101, Version 9 Appendix F §26.5; printed protocol p. 49](<../joi180132supp1_prod.pdf#page=101>) — PLAN post-rewarming/all-patient handoff.

**Source evidence:** The abstract describes both groups as temperature-managed for 7 days. Main methods describe maintaining normothermia, with automated wraps if required, up to 7 days postrandomization after rewarming. Plan §12.11 permits hypothermia post-rewarming normothermia up to 7 days or ICU discharge, but specifies control pyrexia avoidance up to 96 hours postrandomization and then unit protocol. Appendix F gives post-rewarming pad management and all-patient pyrexia avoidance a 96-hour postrandomization handoff to ward/unit protocol; maximum hypothermia separately remains 7 days.

**Reported-versus-comparator:** Reported both-group/post-rewarming 7-day management versus prospective 96-hour control/all-patient handoff. Maximum hypothermia and subsequent ordinary care are distinct quantities; neither is substituted for assigned comparator duration.

**Reasoning procedure:** Match the postrandomization anchor and assigned management component, convert durations to hours, and preserve the explicit handoff. Treat continuing local ICU care and possible superseded instructions as unresolved explanations, rather than establishing actual exposure or adherence.

**Calculation:** 96 hours = 4 days; 7 days = 168 hours; difference = 72 hours. These are prescriptions, not measured means. Even conservative half-unit allowances of [95.5,96.5) hours and [156,180) hours are disjoint.

**Affected result or extracted value:** Duration of assigned comparator/post-rewarming temperature management extracted alongside the six-month favorable GOS-E primary contrast, 117/240 versus 111/226. No change in that effect estimate is demonstrated.

**Why context does not resolve it:** The report does not identify the 96-hour handoff or a duration amendment. The supplied passages do not distinguish trial-assigned management from local care during days 5–7, and plan hypothermia instructions themselves retain both maxima/handoff descriptions.

**Alternative source-grounded interpretations:** The report may summarize continued local care after 96 hours; a later operational extension may have applied; or Appendix F may retain an earlier instruction. The main-plan seven-day hypothermia passage corroborates part of the report. None establishes which comparator/post-rewarming period was operative, and none implies that ordinary care stopped after 96 hours.

**Mechanical evidence recheck:** All four cited locations were found, directly extracted, freshly rendered and visually read. Report and plan statements, time anchors and the logical duration comparison matched. Roles, P_R classification and protocol_report domain were confirmed without transcription correction. The `reproduced` state records unresolved duration attribution, not intervention adherence. Missing inputs are the operative days 5–7 assignment, any superseding amendment and actual arm-specific exposure records.

**Potential downstream evidence impact:** If confirmed, a trial extractor could copy a different assigned comparator duration or combine protocolized and ordinary-care periods in an intervention description. No actual propagation, treatment-effect change or guideline consequence is established.

**Human verification steps:** Compare the cited final-protocol sections with operative amendment and trial-management records, if available. Establish which duration represented randomized control/post-rewarming management and how days 5–7 were classified. Record the source supporting that distinction without inferring universal received exposure.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Normothermia Injury Severity Score median and lower quartile

**Pending Human Adjudication**

**Candidate statement:** The normothermia Injury Severity Score summary, 20.0 (20.5–35.0), labeled median (IQR), does not satisfy quantile ordering even within printed precision.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table1 p.5 median vs lower quartile

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-002

**Classification rationale:** The incompatible quantities occur within one REPORT distribution row. This is an internal statistical ordering relationship, rather than a cross-location baseline comparison.

**Classification ambiguity:** None

**Exact source locations:** [jama_cooper_2018_oi_180132.pdf, PDF p. 5, Table 1 Injury Severity Score row, both arm columns, IQR definition and footnote h; printed p. 2215](<../jama_cooper_2018_oi_180132.pdf#page=5>).

**Source evidence:** The normothermia column, headed n = 240, prints median 20.0 and IQR 20.5–35.0. The hypothermia column prints 26.0 (18.0–34.0). IQR denotes interquartile range, and footnote h specifies a 0–75 scale with higher scores representing greater severity. The line wrapping retains the normothermia attribution.

**Reported-versus-comparator:** Median 20.0 versus lower quartile 20.5 for the same distribution, under the required ordering Q1 ≤ median ≤ Q3. The other arm is contextual evidence, not a proposed replacement.

**Reasoning procedure:** Read the column and median/IQR label directly, compare the median with its own quartiles, and apply half-unit precision intervals. This tests one numerical distribution identity; it does not compare descriptive baseline summaries across locations or infer altered treatment balance.

**Calculation:** Median interval [19.95,20.05), Q1 interval [20.45,20.55), and Q3 interval [34.95,35.05). The median interval lies entirely below Q1, with limiting separation 0.40. The displayed difference is 0.5. No combination within these intervals restores the required order.

**Affected result or extracted value:** Normothermia baseline Injury Severity Score median and lower quartile describing the reported trial population.

**Why context does not resolve it:** Neighboring values and the scale footnote do not supply an intended median or first quartile. More than one component could require clarification; an apparent numerical change cannot be selected from immediate context.

**Alternative source-grounded interpretations:** The intended median or lower quartile may differ from the displayed value. Fresh visual reading does not support a line/column reassignment. No underlying summary or alternate population is supplied to choose a replacement.

**Mechanical evidence recheck:** Direct extraction, fresh rendering and visual inspection confirmed the complete normothermia cell, column heading, label, scale and opposite-arm context. The quantile rule and precision intervals were independently reproduced. S_W/statistical_results and `reproduced` were confirmed without transcription correction. The missing input is the authoritative normothermia distribution summary; patient-level scores are unnecessary for establishing the displayed ordering inconsistency.

**Potential downstream evidence impact:** If confirmed, a baseline-data extractor could copy an incompatible median/IQR or select a different summary after clarification. This does not establish a change in the primary analysis denominator, adjusted effect or trial conclusion.

**Human verification steps:** Inspect Table 1 against the original normothermia Injury Severity Score summary. Establish the median, first quartile and third quartile for that same population, and document the authoritative source. Do not substitute the opposite-arm or another population's values.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Time-to-33°C comparison and printed P value

**Pending Human Adjudication**

**Candidate statement:** Pearson diagnostics of the stated unadjusted equal-proportions chi-square family do not match P = .09 under either source-supported category interpretation. The original tested category set, chi-square implementation and favorable-GOS-E result attribution remain unclear; the diagnostics do not reconstruct unspecified original SAS output.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT main article pp.4,5 vs REPORT results supplement eTable7 p.11

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-002

**Classification rationale:** REPORT main method/nonsignificant claim is compared with REPORT supplementary counts/P, alongside an internal supplementary count/test relationship. Precedence S_C over S_W; no conflicting PLAN comparator.

**Classification ambiguity:** Exact tested categories and chi-square implementation are unprinted. Pearson homogeneity calculations are diagnostics of the stated equal-proportions test, not reconstructed raw-data output.

**Exact source locations:**

- [jama_cooper_2018_oi_180132.pdf, PDF p. 4, Statistical Analysis timing and significance paragraphs; printed p. 2214](<../jama_cooper_2018_oi_180132.pdf#page=4>).
- [jama_cooper_2018_oi_180132.pdf, PDF p. 5, Additional Outcomes; printed p. 2215](<../jama_cooper_2018_oi_180132.pdf#page=5>).
- [joi180132supp2_prod.pdf, PDF p. 11, eTable 7, all four categories and merged P cell; printed appendix p. 10](<../joi180132supp2_prod.pdf#page=11>).

**Source evidence:** Main methods specify an unadjusted chi-square test for equal favorable-outcome proportions by time for cooled patients to reach 33°C, SAS 9.4 and two-sided P < .05. The results narrative states no significant timing-group differences and cites eTable 7. That table prints favorable counts 18/49, 28/67, 32/59 and 39/65 for 1–7 hours, 8–13 hours, >13 hours and Never. Their favorable proportions are 36.7%, 41.8%, 54.2% and 60.0%. One P = .09 occupies a merged cell spanning all four rows.

**Reported-versus-comparator:** The merged .09 and linked nonsignificant narrative versus diagnostic Pearson homogeneity calculations from either all four displayed categories or the three attained-temperature categories. Pearson is not explicitly named in the source. The two category readings are bounded diagnostics, not an exhaustive set of possible original implementations.

**Reasoning procedure:** Match favorable counts to their displayed categories, form favorable/unfavorable cells, compute Pearson homogeneity separately for the four-row and attained-temperature-only interpretations, and compare to the printed precision interval. Preserve the missing category set, implementation/correction and actual degrees of freedom as the unresolved source-to-result mapping. The printed P and nonsignificant narrative agree with each other.

**Calculation:** Four-row cells are (18,31), (28,39), (32,27), (39,26), totaling 117 favorable and 123 unfavorable, N = 240. Using pooled favorable probability .4875, χ² = Σ(O−E)²/E = 8.133762156, diagnostic df = 3, P ≈ .0433268. The three attained-temperature rows give 78 favorable of 175, χ² = 3.658952245, diagnostic df = 2, P ≈ .1604976. Neither is within [.085,.095), the half-unit interval for .09. Exact integer counts are not varied as rounded proportions. The four-row diagnostic is below .05 and the three-row diagnostic above .05, but neither identifies the actual analysis.

**Affected result or extracted value:** The favorable-GOS-E association with time to reach 33°C: tested categories, extracted P, test implementation and nonsignificant description. This timing association is distinct from the randomized primary treatment contrast; no causal timing effect is asserted.

**Why context does not resolve it:** A merged cell spans four categories while the method's achieved-temperature wording permits a three-group reading. Neither diagnostic yields .09, and no other local category set or implementation connects that P to the displayed counts. This is a concrete method/result-attribution gap, rather than a claim based solely on an absent detail.

**Alternative source-grounded interpretations:** Testing only attained-temperature groups, an unshown subset, another chi-square implementation or a differently matched output could explain the value. The supplied passages do not select any such explanation. No omitted records, adjustment, stratification or alternative model is assumed. The review does not establish that every possible unprinted implementation is incompatible with .09.

**Mechanical evidence recheck:** All three locations were directly reread and freshly visually confirmed, including row alignment and the merged cell. Counts, method family and narrative matched; both explicitly bounded Pearson diagnostics were independently reproduced. The `reproduced` state refers to this diagnostic/result-attribution inconsistency, not reconstruction of the unspecified software test. REPORT roles, S_C precedence over S_W and statistical_results were confirmed. Missing inputs are the tested category set, chi-square implementation/correction, actual degrees of freedom and original timing-analysis output.

**Potential downstream evidence impact:** If confirmed, an extractor could attribute .09 and its nonsignificant interpretation to a different timing-category comparison or computation. No significant association, primary-treatment conclusion change or actual downstream propagation is established by these diagnostics.

**Human verification steps:** Inspect the original timing contingency table and SAS output. Establish whether Never was included, which records/categories were tested, the chi-square implementation and degrees of freedom, and which displayed favorable-GOS-E comparison produced .09. Keep any diagnostic recomputation separate from the documented original result.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Bleeding RR, confidence interval and P attribution

**Pending Human Adjudication**

**Candidate statement:** Both main bleeding rows attach explicitly unadjusted RRs incompatible with their own event counts, and their P values conflict with the matched results supplement. Diagnostic CI resemblance supports checking a repeated inferential-block attribution pattern; it does not establish the original CI estimator or a final replacement.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT main article Table2 p.7 vs REPORT results supplement eTable6 p.10

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001, F-XS-001, F-ST1-001

**Classification rationale:** Both within-main count/inferential blocks and matched main-versus-supplement P assignments conflict. REPORT/REPORT relationship S_C takes precedence over S_W; a plan does not constitute a conflicting comparator.

**Classification ambiguity:** None

**Exact source locations:**

- [jama_cooper_2018_oi_180132.pdf, PDF p. 1, abstract Results safety rates; printed p. 2211](<../jama_cooper_2018_oi_180132.pdf#page=1>) — corroborating intracranial event rates.
- [jama_cooper_2018_oi_180132.pdf, PDF p. 3, Outcomes and Statistical Analysis; printed p. 2213](<../jama_cooper_2018_oi_180132.pdf#page=3>) — adverse-event window, population and unadjusted methods.
- [jama_cooper_2018_oi_180132.pdf, PDF p. 4, Statistical Analysis; printed p. 2214](<../jama_cooper_2018_oi_180132.pdf#page=4>) — two-sided significance and software conventions.
- [jama_cooper_2018_oi_180132.pdf, PDF p. 5, Adverse Events; printed p. 2215](<../jama_cooper_2018_oi_180132.pdf#page=5>) — intracranial narrative and Table 2/eTable 6 citations.
- [jama_cooper_2018_oi_180132.pdf, PDF p. 7, Table 2, both bleeding rows, headers and intention-to-treat note; printed p. 2217](<../jama_cooper_2018_oi_180132.pdf#page=7>) — both complete inferential blocks.
- [joi180132supp2_prod.pdf, PDF p. 10, eTable 6, both cerebral/non-cerebral bleeding rows and arm headers; printed appendix p. 9](<../joi180132supp2_prod.pdf#page=10>) — identical event sets with different P attachments.

**Source evidence:** Adverse events within 10 days of randomization are compared with unadjusted chi-square equal-proportions tests, relative risks/risk differences and 95% CIs, using randomized groups excluding consent withdrawals. The main report specifies SAS 9.4, two-sided P < .05, no multiple-comparison adjustment and exploratory secondary outcomes. Abstract and narrative repeat intracranial rates 18.1% versus 15.4%, without a separate bleeding RR/CI/P block.

| Outcome | Main H versus N counts (%) | Main RD, percentage points (95% CI) | Main RR (95% CI) | Main P | Matched supplementary P |
|---|---|---|---|---|---|
| Intracranial bleeding | 47/260 (18.1) versus 37/240 (15.4) | 2.7 (−3.9 to 9.2) | 1.23 (0.43–3.5) | .70 | .43 |
| Extracranial bleeding | 8/260 (3.1) versus 6/240 (2.5) | 0.6 (−2.3 to 3.5) | 1.17 (0.79–1.74) | .43 | .70 |

The supplement explicitly repeats n = 260/240 headers and both event-count pairs; it supplies no independent RR/CI block. The intracranial upper RR bound is printed 3.5, with one decimal.

**Reported-versus-comparator:** Each main RR versus its source-established unadjusted risk-ratio identity; each outcome-specific main P versus the matched supplementary P. These contradictions are independent of the unprinted CI estimator. CI and Pearson calculations below are supporting diagnostics only.

**Reasoning procedure:** Match outcome, 10-day window, H-versus-N direction, denominators and unadjusted method across tables. Recompute exact-count RRs, test displayed precision intervals and compare outcome-specific P attachments. Keep counts/percentages/RDs on their printed rows. Consolidate the paired pattern and corroborating locations into one candidate without choosing a final inferential reassignment.

**Calculation:** Intracranial RR = (47/260)/(37/240) = 1.172557173, outside [1.225,1.235), the interval for printed 1.23. Extracranial RR = (8/260)/(6/240) = 1.230769231, outside [1.165,1.175), the interval for printed 1.17. Count-derived risks and differences round to the printed 18.1%, 15.4%, 2.7 percentage points and 3.1%, 2.5%, 0.6 percentage points. Each outcome's main/supplement P intervals [.695,.705) and [.425,.435) are disjoint, regardless of test implementation.

Diagnostic Pearson comparisons give χ² = .631871801/P ≈ .4266694 for intracranial bleeding and χ² = .152625153/P ≈ .6960393 for extracranial bleeding, df = 1. Diagnostic log-Wald 95% intervals, using SE(log RR) = √(1/a−1/n+1/b−1/m), are .791181–1.737769 and .433345–3.495582. These resemble the opposite main rows' limits within their printed precision, including the one-decimal 3.5 limit. That resemblance supports checking a possible exchanged block but does not establish the CI construction or authorize a replacement. Counts are exact discrete inputs, and the distinct adjusted primary-outcome model is not assigned to these adverse events.

**Affected result or extracted value:** Outcome-specific unadjusted RR, 95% CI and P for intracranial bleeding, an abstract safety outcome, together with the paired extracranial comparison and all repeated locations.

**Why context does not resolve it:** Count-consistent risks/RDs and incompatible RR/CI/P blocks appear on the same named rows under unadjusted methods. Recognizing a possible block exchange cannot establish authoritative complete inferential attribution. The supplement resolves neither RR nor CI from independent output, although its matched P attachments conflict directly.

**Alternative source-grounded interpretations:** Inferential blocks may have exchanged row attribution while counts and risk differences retained theirs. An undisclosed alternative computation could explain some components. Neither is established, and no different population or adjusted adverse-event model is stated locally. No final complete block is prescribed.

**Mechanical evidence recheck:** All six cited pages, both repeated rows and arm headers were directly extracted, freshly rendered and visually read. All printed values, including the 3.5 endpoint, matched without correction. Exact RR identities and disjoint matched P attachments were reproduced; interval calculations remained diagnostic. REPORT roles, S_C precedence over S_W, statistical_results and `reproduced` were confirmed. Missing inputs are original outcome-specific inferential output, exact CI construction and any documented alternative computation/population.

**Potential downstream evidence impact:** If confirmed, an extractor could attach another bleeding outcome's effect estimate, interval or P to the named event. Both printed P values remain nonsignificant. No neurologic primary conclusion change, actual propagation or clinical consequence is inferred.

**Human verification steps:** Compare original 10-day intracranial and extracranial adverse-event output with both supplied tables. Establish the RR, CI construction and P for each matched event set and population. Document complete outcome attribution without relying solely on the diagnostic resemblance of exchanged blocks.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

The candidates identify specific values or definitions a systematic reviewer, meta-analyst or guideline extractor might copy: assigned management duration, a baseline median/IQR, timing-test attribution, or outcome-specific safety RR/CI/P. Human clarification could alter such extraction without establishing a change in the randomized primary treatment estimate. Preserve endpoint, population, contrast, time anchor and model labels with any extracted value. Diagnostic recomputations should remain separate from supplied original results. This review documents potential relevance; it provides no evidence that propagation, conclusion change or harm occurred.

## Limitations and Missing Definitions

Every supplied page and registered relationship was mapped; no scientific-coverage gap remains. The [limitations record](review_1_6_1/limitations.md) distinguishes complete coverage from unresolved definitions and provenance limits.

- The legacy page-image renderer/version is unrecorded. Candidate source pages nevertheless received fresh direct-source extraction/rendering and visual confirmation.
- Tesseract and Office conversion were unavailable, but all direct sources were PDFs; readable reusable images and available direct PDF tools covered every raster unit. No OCR or Office conversion was needed and no fallback environment was created.
- Some graphical quantiles or ordinates lack printed numeric labels. Maps preserve visible direction and printed counts without inventing exact graphical values.
- Plan PDF pages 52 and 181 contain bibliographic locators for external protocol/SAP publications, not the full external papers. Only supplied package content was used; no external retrieval occurred.
- Participant-level data, original complete model/test output and some covariance/scoring inputs are absent. Adjusted results and unprinted CI/test implementations were not replaced by conventional crude or diagnostic calculations.
- Resolution inputs missing for the four candidates are an operative duration/amendment distinction, the authoritative Injury Severity Score quantiles, timing-test category/implementation output, and outcome-specific bleeding inferential output. These limits do not hide an unmapped source unit.

## Human Adjudication Checklist

For each stable candidate, inspect every linked source location and confirm endpoint, population, time point, contrast and analysis label. Distinguish printed contradictions from diagnostic arithmetic and unestablished explanations. Obtain the named authoritative output or operative definition where available; assess whether the interpretation or extraction would differ. Complete Validity, Importance, Action, Initials and Notes in the candidate's five blank fields. Preserve the stable ID and evidence history when recording the human decision.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

The [routing preflight](review_1_6_1/routing_preflight.md) records PASS, Coordinator inference: PASS, INTERACTIVE_CLI, Provider: CURRENT_SESSION, and verification of all ten named presets. The coordinator uses `gpt-6.1-sol`/`high`; ordinary specialists use `gpt-6.1-sol`/`medium`; statistical, screening, recheck and audit specialists use `gpt-6.1-sol`/`high`. Mandatory stages used distinct fresh runtime agents. Source identity and reused-asset fitness/integrity were audited; final before/after hash comparison and mechanical validation are coordinator finalization steps.

Direct tooling and commands are recorded in [tooling_record.md](review_1_6_1/tooling_record.md). The workflow used local CPU tools, reusable text/images, direct Poppler extraction/rendering, SHA-256 and transparent diagnostic arithmetic. No GPU, web, global package installation or scientific Python orchestration was used. Fallback environment: NOT_NEEDED; fallback packages/capabilities: None; removal state: NOT_CREATED. HTML rendering is performed locally after timing finalization.

### Agent execution

The [execution manifest](review_1_6_1/agent_execution_manifest.md) records all 15 actual agents, including the coordinator and optional disjoint mapping/numeric shards. Each row below reproduces its runtime model, effort, start mode and primary artifact relative to the run directory.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | /root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | /root/curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | /root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_mapping_shard_1 | /root/plan_mapper_1 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/plan_001.md |
| support_mapping_shard_2 | /root/plan_mapper_2 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/plan_002.md |
| support_quantitative_mapper | /root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | /root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_review_shard_2 | /root/numeric_checker_2 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_002.md |
| cross_source_consistency_reviewer | /root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | /root/statistics_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | /root/screener_1 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | /root/rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | /root/statistics_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | /root/auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | /root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

### Reproducibility performance

- **Target basis:** Four PDF sources comprise 229 pages with 229 reusable-backed units and no fresh preprocessing units. Full source-matched native text exists for 202 pages and readable rendered pages for all 229; 27 plan pages need visual mapping. The 390,416-byte plan extraction requires three disjoint support shards under the 200,000-character context bound, alongside the ten-page main article and 24-page results supplement. No Office conversion or new OCR is needed. Complete numeric, cross-source, two statistical passes, inclusion screening, evidence recheck, audit and report stages remain mandatory; expected multi-agent review waves and plan-version comparisons support a 35–55 minute planning range.
- **Total source units:** 229
- **Fresh-source units:** 0
- **Target elapsed minutes:** 35-55
- **Started UTC:** 2026-10-11T02:52:41Z
- **Finished UTC:** PENDING
- **Observed elapsed minutes:** PENDING
- **Target status:** PENDING
- **Exceedance causes:** Pending completion

The coordinator finalizes these exact fields from [run_state.md](review_1_6_1/run_state.md) immediately after complete Markdown assembly. Local HTML rendering and mechanical validation are excluded from review duration. Any subsequent model-based repair requires updated timing. The planning range never limits coverage or candidate count.

The ledger, recheck, audit and report contain C001–C004 in full. Report classification fields follow the final ledger table; seven screened findings reconcile to six included provenance rows and four candidates. The final mechanical validation record is [review_validation.json](review_1_6_1/review_validation.json). At report assembly, coordinator timing finalization, final hash comparisons, standalone HTML rendering and mechanical validation remain pending; this report does not pre-claim their outcome.
