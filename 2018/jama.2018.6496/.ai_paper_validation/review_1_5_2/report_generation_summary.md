# Quantitative Quality-Control Consistency Review

## Pending Human Adjudication Notice

**All four candidate consistency issues in this report are Pending Human Adjudication.** This source-first review records printed quantitative, statistical, denominator, and definition relationships for human follow-up. It does not adjudicate candidates or prescribe a final correction.

## Executive Quality-Control Summary

Fresh review of the three supplied PDFs identified four distinct quantitative reporting quality-control candidates: one reverse-ordered confidence-interval display, one bounded denominator question, and two protocol-to-publication measure-definition comparisons. All are Pending Human Adjudication. The review mapped all 49 direct-source pages, registered all four stable IDs without a count cap, and did not treat any coherent display-zero P value as a candidate.

Small preventable reporting defects can matter when numeric results and outcome definitions are copied into systematic reviews, meta-analyses, guidelines, or later evidence products. The supplied package does not establish that propagation, a conclusion change, or harm occurred.

## Package and Fresh-Processing Provenance

The direct-source package contains three PDFs: the 11-page main article, a 25-page protocol, and a 13-page supporting-results/data-form document. All 49 PDF-page units were freshly prepared from supplied sources; zero units were reused. Fresh native and layout text were generated for every PDF. Forty-one result-relevant pages were rendered for visual confirmation. Relevant native/layout text was usable, so CPU OCR was not required (0 OCR pages), and no GPU was used.

| Source ID | Direct source | Role | Units mapped |
|---|---|---|---:|
| DOC-001 | `jama_driver_2018_oi_180054.pdf` | Main randomized clinical-trial article | 11/11 |
| DOC-002 | `joi180054supp1_prod.pdf` | Supporting clinical-trial protocol | 25/25 |
| DOC-003 | `joi180054supp2_prod.pdf` | Supporting results, interim analysis, figures, and data form | 13/13 |

No previous audit derivative, prior report, web material, external literature, or structured source outside these PDFs was used as evidence or as a discovery boundary.

## Scope, Complete Coverage, and Exclusions

The review covered numeric, denominator/proportion/total, inferential-statistical, cross-document, effect-measure/label/scale, and rate-versus-count relationships. Every direct source has zero reusable units, fresh-required units equal to total units, mapped units equal to total units, and `COMPLETE` status: 49/49 overall.

The review did not perform a general methodology, clinical, misconduct, raw-data, or conclusion-validity audit. Analysis-unit and population considerations were considered only where they created a concrete reported-number, denominator, label, or interpretation question. Coherent finite-precision P-value displays were not candidates; no assigned relationship displayed `P = 0` or equivalent.

## Quantitative and Statistical Relationship Coverage

The canonical numeric/reporting inventory contains 47 relationships (`N001` through `N047`). Numeric and cross-source checks addressed the complete inventory, including 118 matched occurrence comparisons after population, time, contrast, model, measure, scale, unit, reference, and precision matching.

The inferential-statistical inventory contains 37 relationships (`S001` through `S037`). A fresh high-effort Terra statistical reviewer completed pass 1 for 37/37 relationships, and a different fresh high-effort Terra statistical reviewer completed pass 2 for 37/37 relationships while revisiting all four ledger/recheck records. Pass 2 added no stable candidate. No relationship was excluded due to a queue, ranking, cap, or early stopping rule.

## Candidate Index

| ID | Candidate | Category | Status |
|---|---|---|---|
| [C001](#c001--reverse-ordered-confidence-interval-endpoints-for-all-patient-first-attempt-duration) | Reverse-ordered confidence-interval endpoints for all-patient first-attempt duration | Statistical reporting inconsistency | Pending Human Adjudication |
| [C002](#c002--two-patient-ettstylet-denominator-difference-across-linked-hypoxemia-outcomes) | Two-patient ETT+stylet denominator difference across linked hypoxemia outcomes | Denominator, proportion, or total inconsistency | Pending Human Adjudication |
| [C003](#c003--protocol-and-published-hypoxemia-observation-windows-use-different-endpoint-events) | Protocol and published hypoxemia observation windows use different endpoint events | Measure, label, or scale inconsistency | Pending Human Adjudication |
| [C004](#c004--protocol-and-published-first-attempt-duration-measures-use-different-endpoint-events) | Protocol and published first-attempt-duration measures use different endpoint events | Measure, label, or scale inconsistency | Pending Human Adjudication |

## Candidate Evidence Cards

## C001 — Reverse-ordered confidence-interval endpoints for all-patient first-attempt duration

**Status:** Pending Human Adjudication

**Candidate statement:** DOC-001 Table 3 prints the all-patient first-attempt-duration confidence limits in descending order (`4 to -1`); the intended unclustered limits remain unresolved.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [DOC-001 Table 3 — PDF p. 7](<../jama_driver_2018_oi_180054.pdf#page=7>); [DOC-003 eTable 1 — PDF p. 2](<../joi180054supp2_prod.pdf#page=2>); [DOC-003 eTable 1 note — PDF p. 3](<../joi180054supp2_prod.pdf#page=3>); [DOC-001 statistical-analysis methods — PDF p. 4](<../jama_driver_2018_oi_180054.pdf#page=4>).

**Source evidence:** Table 3 prints all-patient medians of `38 (29 to 51)` and `36 (25 to 54)` seconds, difference `1 (4 to -1)`, and `P=.24`. The main methods name Hodges-Lehmann median between-group differences with associated 95% confidence intervals. The clustered eTable prints `1 s (-1 s to 4 s), P=.95` and states that inferential columns were recalculated for physician clustering.

**Reported-versus-comparator:** The reported main-table interval is `4 to -1`; the applicable lower-to-upper display convention requires a lower endpoint not greater than the upper endpoint. The clustered interval is contextual distinct-model evidence, not an unclustered replacement.

**Reasoning procedure:** Compare the two printed main-table endpoints in their displayed order and verify that other intervals use lower-to-upper notation. Preserve the unclustered/clustered model distinction rather than substituting one analysis for another.

**Calculation:** `4 > -1`; the displayed sequence is decreasing. Reordering to `-1 to 4` is only a diagnostic possibility, not an assigned correction.

**Alternative source-grounded interpretations:** An unstated reverse-order convention or source-specific transcription could explain the display. The clustered result supports the possibility of a reversed display, but its stated recalculation for physician clustering means it does not establish the intended unclustered values.

**Mechanical evidence recheck:** All cited locations were found and their source strings matched. The endpoint-order rule is applicable; the direct comparison was reproduced. Individual durations, the unclustered analysis-specific output, and a table-production record are unavailable, so the recheck cannot determine whether endpoints were transposed.

**Quality-control relevance:** A descending interval display can cause a reader or data extractor to reverse, normalize, or copy the limits inconsistently.

**Potential downstream evidence impact:** If human adjudication confirms a display defect, a systematic-review or meta-analysis extractor could otherwise copy the confidence limits in the wrong order. No supplied evidence shows that this occurred or that a conclusion changed.

**Human verification steps:** Inspect the original unclustered Hodges-Lehmann output and table-production file; identify the intended limits and their order; document whether the Table 3 sequence was transposed.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Two-patient ETT+stylet denominator difference across linked hypoxemia outcomes

**Status:** Pending Human Adjudication

**Candidate statement:** The ETT+stylet denominators differ by two across linked waveform-dependent outcomes (`366` versus `364`), and the supplied aggregate sources do not establish whether the difference is intentional under an outcome-specific denominator rule.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-001 Table 3 — PDF p. 7](<../jama_driver_2018_oi_180054.pdf#page=7>); [DOC-001 Table 5 — PDF p. 9](<../jama_driver_2018_oi_180054.pdf#page=9>); [DOC-002 protocol secondary outcomes — PDF p. 9](<../joi180054supp1_prod.pdf#page=9>); [DOC-002 analytic issues — PDF p. 21](<../joi180054supp1_prod.pdf#page=21>).

**Source evidence:** Table 3 reports ETT+stylet first-attempt success without hypoxemia as `282/366 (77%)`. Table 5 reports ETT+stylet hypoxemia as `50/364 (14%)`. Both footnotes invoke matching hypoxemia threshold/window language and unavailable valid waveform; the Bougie denominators are 371 in both linked rows. The protocol defines success without hypoxemia as first-attempt success plus no hypoxemia.

**Reported-versus-comparator:** The ETT+stylet denominators are `366` for the composite and `364` for hypoxemia alone. Denominator identity is expected only if both rows require an observed hypoxemia classification for every denominator member; the printed sources do not state the implemented denominator-construction rule.

**Reasoning procedure:** Compare the two arm-specific denominators, their common waveform qualification, matching Bougie denominators, and the protocol composite definition. Do not assume the outcomes are simple complements.

**Calculation:** `366 - 364 = 2`. Relative to the randomized ETT+stylet total, `376 - 366 = 10` and `376 - 364 = 12`. Aggregate counts cannot identify the two patients.

**Alternative source-grounded interpretations:** A patient known to have failed the first attempt may be deterministically classifiable as not achieving the composite without a usable waveform, while lacking a hypoxemia-only classification. Outcome-specific missing-data handling could therefore make the composite denominator larger. The aggregate sources do not show whether either explanation accounts for these two patients.

**Mechanical evidence recheck:** Both table locations, the shared waveform wording, and the protocol definition were found and matched. The arithmetic was reproduced. The conditional denominator rule remains necessary because joint patient-level classifications, the implemented code/rule, and the relevant patient identities are absent.

**Quality-control relevance:** Without a stated construction rule, a reader cannot reproduce which ETT+stylet patients contribute to each displayed percentage.

**Potential downstream evidence impact:** If human adjudication identifies a denominator-label or documentation defect, an outcome extractor could otherwise copy a percentage without the correct analysis denominator. No supplied evidence shows propagation or conclusion change.

**Human verification steps:** Reconcile patient IDs across first-attempt success, waveform availability, and hypoxemia; inspect analysis code and the missing-data log; determine whether the two additional composite-denominator patients were deterministically classifiable failures; document the applicable rule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Protocol and published hypoxemia observation windows use different endpoint events

**Status:** Pending Human Adjudication

**Candidate statement:** The protocol ends hypoxemia surveillance one minute after ETT-cuff inflation, while the published materials end it one minute after intubation-attempt completion; the supplied package does not document whether those events were treated as equivalent or whether the definition changed.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-002 protocol secondary outcomes — PDF p. 9](<../joi180054supp1_prod.pdf#page=9>); [DOC-002 protocol measurement procedure — PDF p. 10](<../joi180054supp1_prod.pdf#page=10>); [DOC-001 Table 3 — PDF p. 7](<../jama_driver_2018_oi_180054.pdf#page=7>); [DOC-001 Table 5 — PDF p. 9](<../jama_driver_2018_oi_180054.pdf#page=9>); [DOC-003 eTable 1 note — PDF p. 3](<../joi180054supp2_prod.pdf#page=3>); [DOC-003 postintubation form — PDF p. 10](<../joi180054supp2_prod.pdf#page=10>).

**Source evidence:** DOC-002 states that hypoxemia observation begins at first-attempt start and ends one minute after ETT-cuff inflation; page 10 repeats the cuff-inflation endpoint and 20-second recording schedule. DOC-001 Tables 3 and 5 and DOC-003 eTable 1 describe hypoxemia during or within one minute after completion of the intubation attempt. DOC-003 defines attempt 1 end as blade removal.

**Reported-versus-comparator:** The threshold and starting event agree. The planned endpoint is one minute after cuff inflation; the published endpoint is one minute after attempt completion/blade removal. These are nonidentical named procedural events.

**Reasoning procedure:** Compare the exact protocol and published window-end text, then apply the supplied data-form definition of attempt completion. Do not infer that cuff inflation and blade removal are interchangeable without a supplied identity or change rule.

**Calculation:** No numeric recalculation is applicable. The reproducible comparison is `one minute after ETT-cuff inflation` versus `one minute after attempt completion/blade removal`.

**Alternative source-grounded interpretations:** “Attempt completion” could be shorthand for cuff inflation, or the events could have occurred close together in practice. The data form explicitly defines attempt end as blade removal, so operational equivalence is not established by the supplied package.

**Mechanical evidence recheck:** The protocol pages 9 and 10, published tables, eTable note, and data form were found and matched. The threshold and start event align; the end-event terms do not. No amendment, implemented surveillance-stop timestamp, or operational equivalence rule is supplied.

**Quality-control relevance:** The named stop event determines which desaturation observations are eligible for the outcome and should be traceable across protocol and results reporting.

**Potential downstream evidence impact:** If human adjudication confirms a definition change or labeling defect, a review or guideline extractor could otherwise record the published hypoxemia result under the protocol's different observation window. No supplied evidence establishes actual propagation or a changed conclusion.

**Human verification steps:** Inspect implemented timing instructions, amendment history, analysis specification, and timestamp logic; identify the surveillance-stop event used in analyzed data; document any approved change or equivalence rule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Protocol and published first-attempt-duration measures use different endpoint events

**Status:** Pending Human Adjudication

**Candidate statement:** The protocol defines first-attempt time to intubation through ETT-cuff inflation, whereas the published analyses use blade removal; the supplied package does not document how or why the measurement endpoint changed.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-002 protocol — PDF p. 9](<../joi180054supp1_prod.pdf#page=9>); [DOC-001 outcome methods — PDF p. 3](<../jama_driver_2018_oi_180054.pdf#page=3>); [DOC-001 Table 3 — PDF p. 7](<../jama_driver_2018_oi_180054.pdf#page=7>); [DOC-003 eTable 1 note — PDF p. 3](<../joi180054supp2_prod.pdf#page=3>); [DOC-003 data form — PDF p. 10](<../joi180054supp2_prod.pdf#page=10>).

**Source evidence:** The protocol defines first-attempt time to intubation from attempt start through ETT-cuff inflation with the tube in the trachea. The article and eTable define duration from laryngoscope-blade insertion through blade removal and report all-patient medians of 38 versus 36 seconds. The data form also identifies blade removal as attempt end.

**Reported-versus-comparator:** The start event is compatible. The planned endpoint is cuff inflation; the published endpoint is blade removal. The latter can define a different time scale and a duration for failed attempts.

**Reasoning procedure:** Compare the explicitly named timing endpoints across protocol, main methods, table, eTable, and data form. Keep the protocol-planned and published implemented measures distinct unless a supplied amendment or harmonization rule connects them.

**Calculation:** No numeric recalculation is applicable. The patient-level difference would be `time(blade removal) - time(cuff inflation)`, but neither paired timestamps nor a defined equivalence are supplied.

**Alternative source-grounded interpretations:** The final analysis may deliberately use blade removal so failed attempts receive a duration, or the labels may refer to a harmonized timing procedure not described in the sources. Repetition in article, supplement, and form supports use of the published operational measure but does not document its relation to the protocol endpoint.

**Mechanical evidence recheck:** Each cited location was found and matched. The comparison retains a compatible start and nonidentical end events. Patient-level timing data, revised-plan/amendment documentation, stopwatch-stop instructions, and failed-attempt handling are unavailable.

**Quality-control relevance:** The stop event defines the reported time scale and affects whether failed attempts have a measurable duration under the same rule.

**Potential downstream evidence impact:** If human adjudication confirms a definition or labeling defect, a meta-analysis or outcome extractor could otherwise treat the protocol and published duration as the same measure. No supplied evidence shows actual propagation or conclusion change.

**Human verification steps:** Inspect protocol/amendment history, stopwatch/data-collection instructions, analysis code, and timestamp fields; determine which stop event generated each published duration analysis and how failed attempts were handled.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed by human adjudication, the candidates describe information a downstream evidence user could copy: confidence-interval ordering, denominator construction, a hypoxemia observation window, or a duration-measure endpoint. Such details can affect faithful data extraction and measure matching. This report makes no claim that any downstream product copied these data, that any conclusion changed, or that harm occurred.

## Limitations and Missing Definitions

- The supplied package contains aggregate PDF evidence only; participant-level data, analysis code, table-production files, and structured result exports are absent.
- Exact row-specific confidence-interval algorithms, variance estimators, test statistics, interaction models, sparse-cell rules, cluster-model details, and interim futility calculations are incompletely specified.
- C001 lacks unclustered Hodges-Lehmann output; C002 lacks joint success/waveform/hypoxemia classifications and denominator-construction logic; C003 and C004 lack amendments, implemented timing instructions, and paired cuff-inflation/blade-removal timestamps.
- Figure curves were not digitized. Printed captions, risk sets, effect estimates, intervals, reference groups, and model labels were mapped; no registered candidate depends on curve-coordinate extraction.
- All relevant native and layout text was usable; 41 pages were rendered and 0 pages required OCR. No web or external literature was used.

## Human Adjudication Checklist

- Confirm each cited printed value or definition in the supplied PDF locations.
- Obtain source records needed to answer the candidate-specific human verification steps.
- Record validity, importance, action, initials, and notes in each card without changing stable IDs.
- If an amendment, analysis record, or production record resolves a candidate, preserve the original candidate and document the adjudication separately.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Source Integrity and Fresh Coverage

| Source | SHA-256 before review | Units |
|---|---|---:|
| `jama_driver_2018_oi_180054.pdf` | `684db2edf58f16d1d24e8ddb6a463429b027450314c923e06700acdd0167e7d2` | 11/11 |
| `joi180054supp1_prod.pdf` | `38c1822278c238d2e9f217cd626c307b9d7ad8152f93f3281a03f58990e6108c` | 25/25 |
| `joi180054supp2_prod.pdf` | `b8b7e9731b69407ff10ffc262eb42477965333e3697461e848d8fe50e13b4b31` | 13/13 |

Pre-review hashes were recorded for all three direct sources. Post-review source-hash verification is to be recorded at finalization; source inputs were not modified by this review.

### Agent-Execution Metadata

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| coordinator | `/root` | gpt-5.6-sol | high | CURRENT_SESSION | `run_state.md` |
| fresh_source_preprocessing | `/root/fresh_preprocessing` | gpt-5.6-terra | medium | FRESH_SPAWN | `evidence_asset_inventory.md` |
| main_evidence_mapping | `/root/main_mapper` | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/main_quantitative_evidence.md` |
| support_evidence_mapping | `/root/support_mapper` | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/support_quantitative_evidence.md` |
| numeric_checks | `/root/numeric_review` | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/numeric_consistency.md` |
| cross_source_checks | `/root/cross_source_review` | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/cross_source_consistency.md` |
| statistics_pass_1 | `/root/statistics_pass_1` | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_1.md` |
| evidence_recheck | `/root/evidence_recheck` | gpt-5.6-sol | high | FRESH_SPAWN | `verification/evidence_recheck.md` |
| statistics_pass_2 | `/root/statistics_pass_2` | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_2.md` |
| evidence_quality | `/root/evidence_quality_audit` | gpt-5.6-sol | high | FRESH_SPAWN | `quality/evidence_quality_audit.md` |
| report_generation | `/root/report_generator` | gpt-5.6-terra | medium | FRESH_SPAWN | `report_generation_summary.md` |

The two required statistical reviewers are distinct fresh agents and each completed all 37 assigned statistical relationships.

### Reproducibility Performance

- **Target basis:** Three direct PDFs contain 49 pages (11-page main article plus 25- and 13-page support files); all 49 pages require fresh native/layout extraction, complete result-relevant mapping, and two statistical passes, with no Office conversion expected and targeted rendering only for visual verification.
- **Total source units:** 49
- **Fresh-source units:** 49
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-08-24T01:50:53Z
- **Finished UTC:** __FINISHED_UTC__
- **Observed elapsed minutes:** __OBSERVED_MINUTES__
- **Target status:** __TARGET_STATUS__
- **Exceedance causes:** __EXCEEDANCE_CAUSES__

### Token-Usage and Cost Metadata

- **Token accounting status:** __TOKEN_ACCOUNTING_STATUS__
- **Total-token count status:** __TOTAL_TOKEN_COUNT_STATUS__
- **Total tokens:** __TOTAL_TOKENS__
- **Known token cost (USD):** __KNOWN_TOKEN_COST_USD__
- **Estimated complete token cost (USD):** __ESTIMATED_COMPLETE_TOKEN_COST_USD__

| Model | Token totals and token-only API-equivalent estimate under the dated price snapshot |
|---|---|
__TOKEN_MODEL_ROWS__

Per-agent response-level detail is recorded in `review_1_5_2/token_usage_ledger.csv` and summarized in `review_1_5_2/token_usage_summary.md`. Cached input and cache-write counts are input subsets, and reasoning counts are output subsets; they are not added again to total tokens. Amounts are token-only API-equivalent estimates under the dated pricing snapshot, not invoices; non-token tools, storage, subscriptions, taxes, and other charges are outside this estimate.
