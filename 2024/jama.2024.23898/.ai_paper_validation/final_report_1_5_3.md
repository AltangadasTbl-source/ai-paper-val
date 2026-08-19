# Quantitative Quality-Control Consistency Review — Workflow 1.5.3

## Pending Human Adjudication

All seven candidate consistency issues in this report are **Pending Human Adjudication**. They are reproducible reporting-quality observations, not findings that the paper’s conclusions are wrong. Small preventable defects can matter to downstream evidence extraction; this report does not claim propagation, conclusion change, or serious harm occurred.

## Executive Quality-Control Summary

Complete mapping of the supplied package identified **7** stable quantitative reporting-quality candidates: C001–C007. They concern endpoint clock origins and windows, subgroup category definitions and labels, confidence-interval labeling, and a table-to-prose inferential summary. No candidate is based on a display-zero P value. The complete stable set is presented below without a review queue, top-N subset, or deferred-by-cap section.

## Package and Reused-Evidence Provenance

The package contains five supplied PDFs: the main article (10 pages), protocol (66), SAP (40), results supplement (2), and data-sharing statement (1). Reusable source-linked native/normalized text and selected page renders covered the 10 main-article pages and 2 results-supplement pages. The remaining 107 pages were freshly extracted and mapped from their supplied PDFs. Reused evidence was a locator and transcription aid; cited candidate evidence was mechanically confirmed against the direct source pages.

## Scope, Complete Coverage, and Exclusions

| Source | Units | Reusable | Fresh-required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 main article | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-002 protocol | 66 | 0 | 66 | 66 | COMPLETE |
| DOC-003 SAP | 40 | 0 | 40 | 40 | COMPLETE |
| DOC-004 results supplement | 2 | 2 | 0 | 2 | COMPLETE |
| DOC-005 data-sharing statement | 1 | 0 | 1 | 1 | COMPLETE |
| **Total** | **119** | **12** | **107** | **119** | **COMPLETE** |

The review covered numeric, denominator, statistical, cross-document, measure/label/scale, and rate-versus-count relationships. Blank templates, protocol recruitment projections, references, and the administrative data-sharing statement were not treated as observed result values. No workbook, CSV, DOC, or DOCX was supplied.

## Quantitative and Statistical Relationship Coverage

The numeric inventory covers N001–N065. The statistical inventory covers S001–S033; both statistical passes record `PASS_1_COMPLETE` and `PASS_2_COMPLETE` for every statistical relationship. The cross-source review covered all five direct sources and 12 matched-result groups. The two pre-ID duplicates were correctly merged into C003 and C005; C004 and C007 remain separate because their comparators and consistency rules differ.

## Candidate Index

| ID | Category | Candidate |
|---|---|---|
| C001 | Cross-document numeric inconsistency | Primary-outcome 72-hour clock origin is not stated consistently |
| C002 | Cross-document numeric inconsistency | Postoperative opioid-consumption window is 24 hours versus 72 hours |
| C003 | Cross-document numeric inconsistency | Unplanned-readmission window is 90 days versus 30 days |
| C004 | Measure, label, or scale inconsistency | ERAS subgroup cut points differ from the protocol bands |
| C005 | Statistical reporting inconsistency | The eFigure assigns both 99% and 95% labels to the same intervals |
| C006 | Statistical reporting inconsistency | Day-5 EQ-5D inference conflicts with blanket no-difference prose |
| C007 | Measure, label, or scale inconsistency | ERAS subgroup is labeled as two levels versus three levels |

## Candidate Evidence Cards

## C001 — Primary-outcome 72-hour clock origin is not stated consistently

**Pending Human Adjudication**

**Candidate statement:** The matched primary GI-3 result is described as 72 hours “after surgery/operation” in the article but as 72 hours “after the start of operation” in the SAP; the printed clock origin is not explicitly aligned.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [main article — PDF p. 1](<../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=1>); [main article — PDF p. 5](<../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5>); [main article — PDF p. 6](<../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6>); [SAP — PDF p. 9](<../joi240139supp2_prod_1741633738.17362.pdf#page=9>).

**Source evidence:** The article reports the same 160/279 versus 164/278 GI-3 result as “72 hours after surgery,” “at 72 hours after operation,” and “by 72 h after operation.”

**Reported-versus-comparator:** The SAP defines the same GI-3 composite “at 72 hours after the start of operation.”

**Reasoning procedure:** A fixed time-window endpoint needs an identifiable time zero. The SAP explicitly names operation start; the article wording does not. This is a label-alignment question, not a demonstrated difference in derivation.

**Calculation:** No numerical recalculation is claimed. The matched counts and effects agree; the reproducible comparison is the presence versus absence of “start of operation.”

**Alternative source-grounded interpretations:** “After surgery/operation” may be shorthand for the SAP origin, or the final derivation may have used completion of surgery, anaesthesia start, or another timestamp not supplied.

**Mechanical evidence recheck:** All four cited pages and the otherwise matching GI-3 result were found. The package lacks the final derivation specification, timestamp fields, analysis code, and a definition equating the article wording with operation start.

**Quality-control relevance:** An endpoint clock origin is part of the quantitative definition.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an ambiguous endpoint clock origin; no propagation or conclusion change is assumed.

**Human verification steps:** Inspect the final data dictionary, timestamp fields, and derivation code; identify time zero; then align each article label to the confirmed definition.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Postoperative opioid-consumption window is 24 hours versus 72 hours

**Pending Human Adjudication**

**Candidate statement:** The article defines and reports postoperative morphine-equivalent consumption through 24 hours, while the protocol and SAP define the matched endpoint through 72 hours.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [main article — PDF p. 4](<../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=4>); [main article — PDF p. 6](<../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6>); [protocol — PDF p. 17](<../joi240139supp1_prod_1741633738.16362.pdf#page=17>); [SAP — PDF p. 11](<../joi240139supp2_prod_1741633738.17362.pdf#page=11>).

**Source evidence:** The article names postoperative opioid consumption “up to 24 hours” and reports OME medians 70.6 mg versus 45.0 mg, each n=210.

**Reported-versus-comparator:** The protocol specifies cumulative morphine-equivalent consumption until 72 hours after operation start; the SAP specifies total in-hospital opioid consumption up to 72 hours.

**Reasoning procedure:** Cumulative consumption over 24 and 72 hours are different measures unless a supplied source establishes equivalence or a distinct endpoint.

**Calculation:** `72 hours − 24 hours = 48 hours`. Aggregate 24-hour medians cannot reconstruct 72-hour medians.

**Alternative source-grounded interpretations:** The final analysis may intentionally report a distinct 24-hour measure, or the planned 72-hour endpoint may have changed before final analysis.

**Mechanical evidence recheck:** All cited labels, medians, IQRs, sample sizes, and planning definitions were matched. No final amendment, outcome dictionary, 72-hour output, participant-level data, or derivation record is supplied.

**Quality-control relevance:** The accumulation window defines the reported quantity.

**Potential downstream evidence impact:** If confirmed, an extractor could attach the published medians to the wrong window; no propagation or conclusion change is assumed.

**Human verification steps:** Obtain the final outcome definition/amendment and output; confirm the window generating 70.6 and 45.0 mg; determine whether 72-hour values were analysed.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Unplanned-readmission window is 90 days versus 30 days

**Pending Human Adjudication**

**Candidate statement:** Table 3 labels 31 versus 34 unplanned readmissions within 90 days, while article Methods, protocol, and SAP define the endpoint within 30 days.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [main article — PDF p. 4](<../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=4>); [main article — PDF p. 8](<../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=8>); [protocol — PDF p. 18](<../joi240139supp1_prod_1741633738.16362.pdf#page=18>); [SAP — PDF p. 10](<../joi240139supp2_prod_1741633738.17362.pdf#page=10>); [SAP — PDF p. 27](<../joi240139supp2_prod_1741633738.17362.pdf#page=27>).

**Source evidence:** Article Methods says within 30 days; Table 3 says within 90 days and prints 31/279 (11.1%) versus 34/278 (12.2%).

**Reported-versus-comparator:** The protocol and SAP (including the SAP dummy-table heading) specify unplanned readmission within 30 days.

**Reasoning procedure:** Counts and proportions from 30- and 90-day ascertainment windows are not interchangeable without an identified redefinition.

**Calculation:** `90 days − 30 days = 60 days`; `31 / 279 × 100 = 11.11%` and `34 / 278 × 100 = 12.23%`, reproducing the printed percentages at one decimal place but not the window.

**Alternative source-grounded interpretations:** Table 3 may contain 30-day counts under a 90-day label, or the final endpoint may have changed to 90 days while other text remained unrevised.

**Mechanical evidence recheck:** All five locations, windows, counts, denominators, and percentages were matched. Participant-level readmission dates, final cutoff output, endpoint dictionary, and amendment history are absent.

**Quality-control relevance:** Follow-up window is necessary to identify a readmission measure.

**Potential downstream evidence impact:** If confirmed, an extractor could record the wrong follow-up duration for these proportions; no propagation or conclusion change is assumed.

**Human verification steps:** Reproduce counts under both windows from final data; inspect amendment history and final output; align Methods and Table 3 to the confirmed definition.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — ERAS subgroup cut points differ from the protocol bands

**Pending Human Adjudication**

**Candidate statement:** The protocol gives example ERAS compliance bands of 0–30%, 30–60%, and greater than 60%, whereas the eFigure defines low as fewer than 5 and high as at least 7 of 10 criteria; the printed definitions are not directly reconciled.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [protocol — PDF p. 17](<../joi240139supp1_prod_1741633738.16362.pdf#page=17>); [protocol — PDF p. 18](<../joi240139supp1_prod_1741633738.16362.pdf#page=18>); [SAP — PDF p. 15](<../joi240139supp2_prod_1741633738.17362.pdf#page=15>); [results supplement — PDF p. 2](<../joi240139supp3_prod_1741633738.18862.pdf#page=2>).

**Source evidence:** The eFigure displays high n=191, moderate n=274, low n=92; it defines high as ≥7/10 and low as <5/10, and says the definitions were not predefined.

**Reported-versus-comparator:** The protocol calls its bands “e.g.” 0–30%, 30–60%, and >60%; the SAP names high/moderate/low without cut points.

**Reasoning procedure:** A categorization rule must map criterion counts to categories unambiguously. The protocol qualifier means its bands cannot be assumed to govern the final analysis.

**Calculation:** `4 / 10 × 100 = 40%`. The eFigure classifies 4/10 as low, while 40% is in the protocol’s printed 30–60% example band. `191 + 274 + 92 = 557`.

**Alternative source-grounded interpretations:** The “e.g.” bands may be illustrative and a final 0–4/5–6/7–10 rule may have superseded them; alternatively, the scales may not have been aligned. The eFigure does not expressly define moderate.

**Mechanical evidence recheck:** The cited bands, thresholds, counts, and category labels were found. Final code, eligible-item denominator/missing-data rule, explicit moderate definition, and supersession record are absent.

**Quality-control relevance:** Subgroup categories need a reproducible scale definition.

**Potential downstream evidence impact:** If confirmed, an extractor could reproduce or label adherence categories incorrectly; no erroneous subgroup assignment, propagation, or conclusion change is assumed.

**Human verification steps:** Obtain final ERAS variable list, denominator rule, and categorization code; reproduce all three counts; determine whether the example protocol bands were superseded.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — The eFigure assigns both 99% and 95% labels to the same intervals

**Pending Human Adjudication**

**Candidate statement:** The eFigure legend labels horizontal subgroup intervals as 99% CIs, while its caption calls the displayed within-subgroup intervals 95% CIs.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [results supplement — PDF p. 2](<../joi240139supp3_prod_1741633738.18862.pdf#page=2>); [SAP — PDF p. 15](<../joi240139supp2_prod_1741633738.17362.pdf#page=15>).

**Source evidence:** The eFigure legend says “99% CI”; its caption states that right-hand within-subgroup relative risks have “95% confidence interval.”

**Reported-versus-comparator:** The SAP specifies two-sided 1% subgroup tests and corresponding 99% CIs, supporting the legend’s planned convention but not proving the plotted calculation.

**Reasoning procedure:** One displayed within-subgroup interval set requires an unambiguous confidence-level label unless separate interval sets are explicitly distinguished.

**Calculation:** `99% − 95% = 4 percentage points`; the explicit labels have no rounding tolerance.

**Alternative source-grounded interpretations:** The caption may use generic 95% wording, the legend may be incorrect, or different interval types may have been intended but not distinguished.

**Mechanical evidence recheck:** The legend, caption, plotted linkage, interval values, and SAP convention were directly matched. Populated output, interval-construction metadata, SEs, covariance details, and confirmed confidence level are absent.

**Quality-control relevance:** Confidence level changes the uncertainty represented by a forest plot.

**Potential downstream evidence impact:** If confirmed, an extractor could record subgroup intervals under the wrong confidence level; no effect-estimate, propagation, or conclusion change is assumed.

**Human verification steps:** Inspect populated subgroup output and interval-construction settings; determine the level for each interval; then correct or distinguish legend and caption wording.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Day-5 EQ-5D inference conflicts with blanket no-difference prose

**Pending Human Adjudication**

**Candidate statement:** Table 2 reports a day-5 EQ-5D-5L contrast with a 95% CI excluding zero and P=.04, whereas Results says there was no statistically significant EQ-5D-5L difference between groups.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [main article — PDF p. 5](<../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5>); [main article — PDF p. 6](<../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6>); [SAP — PDF p. 13](<../joi240139supp2_prod_1741633738.17362.pdf#page=13>); [SAP — PDF p. 14](<../joi240139supp2_prod_1741633738.17362.pdf#page=14>).

**Source evidence:** Day 5 is −0.057 (95% CI, −0.111 to −0.003), P=.04; Results uses blanket “no significant difference” prose for EQ-5D-5L.

**Reported-versus-comparator:** The SAP uses 95% CIs apart from subgroups, no secondary-outcome multiplicity adjustment, and time-by-treatment contrasts at each EQ-5D time point.

**Reasoning procedure:** Under the printed time-specific framework, the row is nominally non-null. The comparison does not establish an overall EQ-5D effect, clinical importance, or that the paper conclusion is wrong.

**Calculation:** `−0.111 < −0.057 < −0.003`; zero is outside the interval; `.04 < .05`.

**Alternative source-grounded interpretations:** The prose may summarize an overall repeated-measures pattern, use an unstated endpoint-level decision rule, or omit mention of a nominal time-point result.

**Mechanical evidence recheck:** The table, prose, CI framework, repeated-measures description, and no-adjustment statement were matched. No omnibus statistic, endpoint hierarchy, narrative decision rule, or populated model output is supplied.

**Quality-control relevance:** Narrative statistical summaries should make clear their relation to displayed time-specific results.

**Potential downstream evidence impact:** If confirmed, an extractor could omit a nominal day-5 contrast or apply the blanket summary to every time point; no overall effect, propagation, or conclusion change is assumed.

**Human verification steps:** Identify the estimand and decision rule governing the prose; inspect model output for the time-specific contrast and any omnibus test; qualify the narrative accordingly.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — ERAS subgroup is labeled as two levels versus three levels

**Pending Human Adjudication**

**Candidate statement:** Article Methods calls the ERAS subgroup “high vs low,” while the SAP and eFigure name high, moderate, and low strata for the displayed interaction.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [main article — PDF p. 5](<../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5>); [SAP — PDF p. 15](<../joi240139supp2_prod_1741633738.17362.pdf#page=15>); [results supplement — PDF p. 2](<../joi240139supp3_prod_1741633738.18862.pdf#page=2>).

**Source evidence:** The eFigure prints high n=191, moderate n=274, and low n=92, with one interaction P=.966; the SAP names the same three levels.

**Reported-versus-comparator:** The article phrase names only high and low and does not identify it as shorthand or a separate extreme-level contrast.

**Reasoning procedure:** A subgroup label should identify levels represented in the reported interaction. Three displayed rows do not, by themselves, prove the final model matrix or degrees of freedom.

**Calculation:** `191 + 274 + 92 = 557`. One interaction P appears beside the three-row factor, supporting a three-level display without reconstructing its coding.

**Alternative source-grounded interpretations:** “High vs low” may be shorthand for the three-level factor, or it may describe an extreme-level contrast while the eFigure displays a separate three-level interaction.

**Mechanical evidence recheck:** The two-level article phrase, three-level SAP/eFigure labels, counts, RRs, intervals, and P value were matched. Final formula, factor coding, degrees of freedom, contrast matrix, and populated output are absent.

**Quality-control relevance:** Complete subgroup labels are needed to identify the reported factor.

**Potential downstream evidence impact:** If confirmed, an extractor could record a two-level subgroup for a three-stratum display; no interaction-calculation, propagation, or conclusion change is assumed.

**Human verification steps:** Inspect final model formula, coding, degrees of freedom, contrasts, and output; confirm represented levels; align Methods wording with the analysis performed.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed after human review, these observations could affect how an evidence extractor records endpoint windows, clock origins, subgroup categories, confidence levels, or nominal time-point findings. They do not establish that any extraction error, systematic-review propagation, guideline effect, treatment effect, or conclusion change occurred.

## Limitations and Missing Definitions

See [limitations.md](<review_1_5_3/limitations.md>). The package lacks participant-level data, final endpoint derivation records, complete amendment history, populated model output, subgroup interval metadata, ERAS coding, factor coding/contrasts, and a stated EQ-5D narrative decision rule. Planning documents cannot alone determine whether a later documented change was appropriate.

## Human Adjudication Checklist

For each candidate: confirm direct source wording; obtain the named final analysis record or code; select among only the source-grounded alternatives; document the resolution; and complete Validity, Importance, Action, Initials, and Notes in the card. Do not infer a conclusion change from this report.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

- **Routing preflight:** PASS; Coordinator inference: PASS; execution mode: INTERACTIVE_CLI.
- **Source coverage:** 119 total units; 12 reusable units; 107 fresh-source units; 119 mapped units.
- **Source integrity:** PASS. All five direct-source and all 38 reused-artifact SHA-256 baselines were recomputed after report assembly and matched their pre-review values.
- **Candidate-ID reconciliation:** Ledger, recheck, quality audit, and this report contain C001, C002, C003, C004, C005, C006, C007.

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode |
|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION |
| reuse_asset_curator | root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN |
| main_quantitative_mapper | root/main_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN |
| support_quantitative_mapper | root/support_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN |
| numeric_consistency_reviewer | root/numeric_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN |
| cross_source_consistency_reviewer | root/cross_source_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN |
| statistics_pass_1 | root/statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN |
| evidence_rechecker | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN |
| statistics_pass_2 | root/statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN |
| quality_control_auditor | root/quality_control_auditor | gpt-5.6-sol | high | FRESH_SPAWN |
| report_generator | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN |

### Reproducibility performance

- **Target basis:** This package has five direct PDF sources and 119 unique PDF-page units. Twelve units have complete reusable native-text or visual coverage, while 107 units across the 66-page protocol, 40-page SAP, and one-page data-sharing statement require fresh direct-source mapping. The encrypted protocol and SAP have usable copy permissions but no reusable extraction, and the workflow requires complete main/support mapping, two statistical passes, rechecking, audit, and report assembly.
- **Total source units:** 119
- **Fresh-source units:** 107
- **Target elapsed minutes:** 65-90
- **Started UTC:** 2026-08-19T04:39:46Z
- **Finished UTC:** 2026-08-19T05:03:45Z
- **Observed elapsed minutes:** 24.0
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Output tokens | Total tokens | Known token cost (USD) |
|---|---:|---:|---:|---:|
| gpt-5.6-sol | 0 | 0 | 0 | 0.000000 |
| gpt-5.6-terra | 0 | 0 | 0 | 0.000000 |

Authoritative response-level token counts were not exposed by this runtime for the coordinator or any manifested specialist. Accordingly, the deterministic summary retains a known subtotal of zero while the total-token count and complete price remain incomplete; no usage was estimated from report text. Cached input and cache-write counts are input subsets; reasoning is an output subset and is not added again. Any available amount uses the bundled pricing snapshot dated 2026-08-18 and is a token-only estimate, not an invoice. Per-agent detail is in `review_1_5_3/token_usage_summary.md`.
