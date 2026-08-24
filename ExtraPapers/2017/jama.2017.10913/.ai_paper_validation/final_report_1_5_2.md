# Quantitative Quality-Control Consistency Review — Workflow 1.5.2

> **Pending Human Adjudication:** Every candidate in this report is a source-grounded quantitative reporting quality-control observation. None is a validity decision, correction, or finding of paper-level conclusion change.

## Executive Quality-Control Summary

Complete fresh review of the three supplied PDFs identified **9** distinct stable candidate consistency issues (C001-C009). Small preventable reporting defects can matter when numbers, definitions, or effect measures are extracted into systematic reviews, meta-analyses, guidelines, or later evidence products. This report does not claim that any defect propagated, changed a conclusion, or caused serious harm.

## Package and Fresh-Processing Provenance

The supplied package comprised three direct PDFs: DOC-001 (8 pages), DOC-002 (29 pages), and DOC-003 (10 pages), for **47 pages**. All 47 pages required and received fresh native and layout extraction; 43 result-relevant pages were rendered for visual confirmation. No OCR was needed because usable native/layout text was available for every page. Source hashes were recorded before processing and rechecked unchanged. The evidence base was the supplied PDFs and newly generated fresh derivatives only.

## Scope, Complete Coverage, and Exclusions

The review covered numeric, denominator/proportion/total, statistical, cross-document, measure/label/scale, and rate-versus-count consistency across all result-relevant main-article and support contents. Coverage was complete: 47/47 direct PDF pages mapped, **133** numeric relationships, **58** statistical relationships, and 30 matched cross-source families. There was no review queue, top-N subset, candidate cap, or deferred-by-cap section.

Excluded from scope were broad methodology, clinical, novelty, misconduct, and raw-data audits. Protocol planning/background material was compared only when population, time point, contrast, and analysis role matched. Coherent P-value display zeros were not candidates; none occurred in this package. S407 remained a diagnostic-only statistical relationship because the supplied sources do not establish compatible P-test and confidence-interval construction details.

## Quantitative and Statistical Relationship Coverage

Numeric mapping and checking covered N001-N047, N200-N231, and N600-N653 (133 relationships). Statistical pass 1 and the independent statistical pass 2 each completed S001-S031, S200-S215, and S400-S410 (58 relationships). Both statistical passes used distinct fresh `gpt-5.6-terra` agents at high reasoning effort. Pass 2 added no candidates. All stable IDs were mechanically rechecked against the direct PDF locations and quality audited.

## Candidate Index

| ID | Candidate statement | Category |
|---|---|---|
| C001 | Discontinuation-reason counts do not exhaust the stated 65 recipients stopping before 4 L | Denominator, proportion, or total inconsistency |
| C002 | Usual-care fluid-bolus percentage does not reconcile with its printed count and arm denominator | Denominator, proportion, or total inconsistency |
| C003 | Usual-care lactate-change IQR differs between narrative and Table 2 and is nonascending in the narrative | Cross-document numeric inconsistency |
| C004 | Respiratory-compromise oxygen-saturation threshold is labelled inconsistently | Measure, label, or scale inconsistency |
| C005 | Figure 2’s 94.2% vital-status percentage does not reconcile with displayed modified-ITT/28-day counts | Denominator, proportion, or total inconsistency |
| C006 | Protocol Table 2 column headers and row percentages use incompatible denominators | Denominator, proportion, or total inconsistency |
| C007 | Printed 28-day usual-care mortality percentage does not round from displayed follow-up and total-death counts | Denominator, proportion, or total inconsistency |
| C008 | HIV-negative subgroup risk ratio does not reconcile with its printed deaths and denominators | Numeric or arithmetic inconsistency |
| C009 | Protocol background culture-yield percentage does not round from its printed count and denominator | Denominator, proportion, or total inconsistency |

## Candidate Evidence Cards

## C001 — Discontinuation-reason counts do not exhaust the stated 65 recipients stopping before 4 L

**Status:** Pending Human Adjudication.

**Candidate statement:** The four printed discontinuation-reason counts total 50 rather than the stated 65 patients stopping before 4 L, conditional on the listed reasons being exhaustive and non-overlapping.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 4](<../jama_andrews_2017_oi_170091.pdf#page=4>), Hemodynamic Interventions, left column.

**Source evidence:** The article prints 41/106 (38.7%) receiving 4 L or more and “the remaining 65 patients (61.3%)” stopping before 4 L, followed by reason counts 32, 9, 5, and 4.

**Reported-versus-comparator:** Reported remaining group: 65; comparator sum of listed reasons: 32+9+5+4.

**Reasoning procedure:** Apply an integer-partition check only if “due to” introduces a complete, once-per-patient list.

**Calculation:** 32+9+5+4=50; 65−50=15. The displayed percentages total 47.2% of 106, consistent with 50 people.

**Alternative source-grounded interpretations:** The list may be non-exhaustive, reasons may overlap, or an unlisted operational/time reason may exist; none is specified in the passage.

**Mechanical evidence recheck:** Direct-PDF recheck found the 65-person statement and all four counts at the cited location; exhaustiveness and overlap are not defined.

**Quality-control relevance:** The numbers describe intervention-process exposure and reasons for not reaching 4 L.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy an incomplete or ambiguously partitioned discontinuation-reason distribution into an intervention-process table.

**Human verification steps:** Confirm whether categories were exhaustive and mutually exclusive; identify any residual category or overlap rule; verify the intended denominator statement.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Usual-care fluid-bolus percentage does not reconcile with its printed count and arm denominator

**Status:** Pending Human Adjudication.

**Candidate statement:** The printed usual-care bolus result, 50 (48.3%), does not reconcile with the adjacent 103-person usual-care analysis population under ordinary nearest-tenth rounding.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 4](<../jama_andrews_2017_oi_170091.pdf#page=4>), Hemodynamic Interventions and Figure 1; comparator DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 6](<../jama_andrews_2017_oi_170091.pdf#page=6>), Table 2 header.

**Source evidence:** The narrative prints “50 patients (48.3%)” receiving any intravenous fluid bolus. Figure 1 and Table 2 print usual-care n=103.

**Reported-versus-comparator:** Reported 50 (48.3%) versus 50/103 using the displayed usual-care analysis population.

**Reasoning procedure:** Compare the count/percentage pair with the directly displayed arm denominator, while retaining that the process sentence itself does not print a denominator.

**Calculation:** 50/103×100=48.543689%, ordinarily 48.5%, not 48.3%. The exact back-calculated denominator from 50/0.483 is nonintegral (about 103.52); neither 103 nor 104 yields 48.3% under ordinary nearest-tenth rounding.

**Alternative source-grounded interpretations:** An unstated process-measure denominator or calculation rule may have been used, or the count or percentage may be misprinted.

**Mechanical evidence recheck:** Direct-PDF recheck confirmed the 50 (48.3%) statement and both 103-person comparator displays; it found no stated available-case or rounding rule.

**Quality-control relevance:** This is a reported usual-care fluid-exposure proportion.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a bolus count, percentage, or denominator that does not describe the same population.

**Human verification steps:** Retrieve the process-measure denominator and rounding convention; reconcile it with Figure 1/Table 2; determine whether count, percentage, or population label needs qualification.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Usual-care lactate-change IQR differs between narrative and Table 2 and is nonascending in the narrative

**Status:** Pending Human Adjudication.

**Candidate statement:** The usual-care lactate-change IQR is printed as 2.2 to 1.1 in the narrative but −2.2 to 1.1 in Table 2.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 4](<../jama_andrews_2017_oi_170091.pdf#page=4>), Hemodynamic Interventions, right column; comparator DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 6](<../jama_andrews_2017_oi_170091.pdf#page=6>), Table 2 lactate-change row.

**Source evidence:** p. 4 prints median −0.5 mmol/L; IQR 2.2 to 1.1 mmol/L. Table 2 prints −0.5 (−2.2 to 1.1) mmol/L for the same labelled group/time point.

**Reported-versus-comparator:** Narrative lower endpoint 2.2 versus Table 2 lower endpoint −2.2; narrative order 2.2>1.1.

**Reasoning procedure:** Check endpoint ordering and agreement of a matched group, measure, and baseline-to-6-hour time point.

**Calculation:** 2.2>1.1; the two displays differ by the sign of the lower endpoint.

**Alternative source-grounded interpretations:** Either location may contain a transcription/sign error, or an unlabelled subset distinction may exist.

**Mechanical evidence recheck:** Direct-PDF recheck confirmed both IQR displays and their matching labels.

**Quality-control relevance:** The display reports the distribution of lactate change.

**Potential downstream evidence impact:** If confirmed, a reviewer could copy the wrong lower-tail direction or an internally nonascending IQR.

**Human verification steps:** Check source data or production files for the intended endpoint; confirm whether both locations use the identical population and time point.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Respiratory-compromise oxygen-saturation threshold is labelled inconsistently

**Status:** Pending Human Adjudication.

**Candidate statement:** Respiratory compromise is defined as a decrease in oxygen saturation of >=3% in methods/results but as more than 3% in a Table 2 footnote.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 3](<../jama_andrews_2017_oi_170091.pdf#page=3>), outcomes definition; comparator DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 6](<../jama_andrews_2017_oi_170091.pdf#page=6>), Table 2 footnote b.

**Source evidence:** p. 3 prints >=3%; p. 4 says 3% or greater; Table 2 footnote b says more than 3% from baseline.

**Reported-versus-comparator:** `>=3%` includes exactly 3 percentage points; `>3%` excludes exactly 3.

**Reasoning procedure:** Compare the logical boundary for the same named outcome.

**Calculation:** The boundary-set difference is exactly `{3%}`; no rounding is involved.

**Alternative source-grounded interpretations:** “More than 3%” may be informal wording, one label may be typographical, or an undisclosed stricter table definition may exist.

**Mechanical evidence recheck:** Direct-PDF recheck found each threshold wording at the cited locations; individual oxygen-saturation values and operational coding are absent.

**Quality-control relevance:** The threshold defines a reported safety outcome and its Table 2 count.

**Potential downstream evidence impact:** If confirmed, an extractor or reproducer could apply a different safety-outcome boundary or copy an ambiguous definition.

**Human verification steps:** Confirm the operational threshold used for analysis; check whether exactly-3% observations existed; align methods, results, and table wording.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Figure 2’s 94.2% vital-status percentage does not reconcile with displayed modified-ITT/28-day counts

**Status:** Pending Human Adjudication.

**Candidate statement:** Figure 2 prints 194 patients (94.2%) with known 28-day vital status, whereas the displayed primary-analysis and follow-up counts yield 194/209=92.8%.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 4](<../jama_andrews_2017_oi_170091.pdf#page=4>), Figure 1; comparator DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 6](<../jama_andrews_2017_oi_170091.pdf#page=6>), Figure 2 caption.

**Source evidence:** Figure 1 prints 106 and 103 primary-analysis participants, 9 and 6 losses after discharge, and 97 per group in 28-day analysis. Figure 2 prints 194 patients (94.2%) but no denominator.

**Reported-versus-comparator:** Reported 194 (94.2%) versus the 209-person cohort derived from the displayed 106+103 counts.

**Reasoning procedure:** Reconcile Figure 1’s arm totals, losses, and 28-day totals with the Figure 2 percentage while distinguishing printed from derived denominators.

**Calculation:** 106+103=209; 9+6=15; 209−15=194; 194/209×100=92.822967%, ordinarily 92.8%. 194/206×100=94.174757%, ordinarily 94.2%, but 206 is only an inferred back-calculated denominator and is not printed.

**Alternative source-grounded interpretations:** The caption may use an unstated population rule, the percentage may be misprinted, or “known” may refer to a different population.

**Mechanical evidence recheck:** Direct-PDF recheck confirmed the Figure 1 counts and that Figure 2 prints no denominator for its 94.2% statement.

**Quality-control relevance:** Vital-status completeness is a quantitative follow-up denominator.

**Potential downstream evidence impact:** If confirmed, a reviewer could extract an ambiguous follow-up-completeness percentage or denominator.

**Human verification steps:** Identify the caption denominator and population rule; reconcile it with the 209 primary-analysis participants and 194 known-status total.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Protocol Table 2 column headers and row percentages use incompatible denominators

**Status:** Pending Human Adjudication.

**Candidate statement:** Protocol Table 2 prints Total n=76, SSSP n=36, and Control n=44, although 36+44=80, and its control-row percentages are incompatible with n=44.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** DOC-002, [joi170091supp1_prod.pdf — PDF p. 9](<../joi170091supp1_prod.pdf#page=9>), Table 2, “Baseline characteristics in SSSP participants.”

**Source evidence:** Headers print Total n=76, SSSP n=36, Control n=44. Control cells include 31 (78), 27 (68), 14 (35), 13 (33), 13 (33), and 17 (42).

**Reported-versus-comparator:** Printed total 76 versus 36+44=80; printed control percentages versus their corresponding count/44 percentages.

**Reasoning procedure:** Apply the exact three-column partition identity and calculate each cited control percentage from the printed n=44 header.

**Calculation:** 76 != 36+44. From n=44: 31/44=70.5%, 27/44=61.4%, 14/44=31.8%, 13/44=29.5%, and 17/44=38.6%, not the printed 78, 68, 35, 33, and 42. n≈40 is diagnostic only: it places the displayed values within 0.5 points, but no single ordinary tie rule maps the .5 values to both printed 33 and 42.

**Alternative source-grounded interpretations:** A header, total, or row percentage may be erroneous; row-specific available-case denominators or mismatched preliminary versions may have been used.

**Mechanical evidence recheck:** Direct-PDF recheck confirmed all headers and cited cells. The intended population, row denominators, and rounding rule are not supplied.

**Quality-control relevance:** The table is a preliminary baseline description whose denominators determine interpretation of its frequencies.

**Potential downstream evidence impact:** If confirmed, an extractor could copy baseline frequencies with incompatible total/group denominators.

**Human verification steps:** Verify the intended total, SSSP, and control populations; retrieve row-level denominators and rounding convention; repair headers/cells only after source confirmation.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Printed 28-day usual-care mortality percentage does not round from displayed follow-up and total-death counts

**Status:** Pending Human Adjudication.

**Candidate statement:** Under ordinary nearest-tenth rounding and matching 28-day populations, the printed usual-care mortality of 45.3% does not reconcile with 97 participants per group and 109/194 total deaths.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 5](<../jama_andrews_2017_oi_170091.pdf#page=5>), Clinical Outcomes; comparator DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 4](<../jama_andrews_2017_oi_170091.pdf#page=4>), Figure 1; and DOC-003, [joi170091supp2_prod.pdf — PDF p. 5](<../joi170091supp2_prod.pdf#page=5>), eMethods.

**Source evidence:** DOC-001 prints 97 participants per group and 67.0% versus 45.3% mortality. DOC-003 prints 109/194 28-day deaths.

**Reported-versus-comparator:** Reported usual-care 45.3% versus the derived 44/97 percentage after ordinary rounding identifies 65 protocol deaths from 67.0% of 97 and subtracts from 109.

**Reasoning procedure:** Use the supplied integer totals and ordinary one-decimal rounding conditionally, explicitly treating arm death counts as derived.

**Calculation:** 67.0% of 97 uniquely implies 65 under ordinary nearest-tenth rounding; 109−65=44; 44/97×100=45.360825%, ordinarily 45.4%, not 45.3%.

**Alternative source-grounded interpretations:** The 109/194 total may be from a different analysis population, the display may be truncated, or a count/percentage may be erroneous.

**Mechanical evidence recheck:** Direct-PDF recheck confirmed the 97-per-arm display, mortality percentages, and 109/194 total; direct arm death counts and a rounding rule are absent.

**Quality-control relevance:** The usual-care mortality percentage is a reported secondary-outcome measure.

**Potential downstream evidence impact:** If confirmed, a reviewer could copy an arm mortality percentage or derive an arm death count that does not use the same rounding/population convention.

**Human verification steps:** Confirm arm-specific deaths, population identity, and rounding/truncation convention for the 28-day result.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — HIV-negative subgroup risk ratio does not reconcile with its printed deaths and denominators

**Status:** Pending Human Adjudication.

**Candidate statement:** The HIV-negative subgroup’s printed RR of 0.75 differs from the crude risk ratio 0.60 calculated from the printed 3/9 and 5/9 deaths.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** DOC-001, [jama_andrews_2017_oi_170091.pdf — PDF p. 7](<../jama_andrews_2017_oi_170091.pdf#page=7>), Figure 3, HIV-negative subgroup row.

**Source evidence:** The row prints denominators 9/9, deaths 3 (33.3%) and 5 (55.6%), and RR 0.75 (95% CI, 0.23-2.44).

**Reported-versus-comparator:** Reported RR 0.75 versus the crude displayed-count ratio from 3/9 and 5/9.

**Reasoning procedure:** Calculate the crude RR only from the displayed event counts and denominators; do not assume it is the intended estimator.

**Calculation:** (3/9)/(5/9)=3/5=0.60, not 0.75. The displayed percentages themselves agree with 3/9 and 5/9 at one decimal.

**Alternative source-grounded interpretations:** The RR may use an undisclosed non-crude estimator, weighting, or population, or one displayed element may be misprinted.

**Mechanical evidence recheck:** Direct-PDF recheck confirmed the row values and found no stated adjusted/standardized estimator for the subgroup RR.

**Quality-control relevance:** The effect measure is directly reported for a subgroup.

**Potential downstream evidence impact:** If confirmed, an extractor could record incompatible subgroup event counts and risk ratio.

**Human verification steps:** Obtain the subgroup estimator, weights/adjustment and analysis population; verify which displayed component is intended if the RR was crude.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Protocol background culture-yield percentage does not round from its printed count and denominator

**Status:** Pending Human Adjudication.

**Candidate statement:** The protocol’s background culture-yield display 36 (22.3%) of 161 does not reconcile with ordinary one-decimal rounding.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** DOC-002, [joi170091supp1_prod.pdf — PDF p. 7](<../joi170091supp1_prod.pdf#page=7>), “Blood cultures and antibiotics” background paragraph.

**Source evidence:** The paragraph prints, after excluding probable contaminants, 36 (22.3%) of 161 septic patients with positive aerobic blood cultures.

**Reported-versus-comparator:** Reported 22.3% versus 36/161.

**Reasoning procedure:** Apply ordinary one-decimal percentage rounding to the printed count and denominator.

**Calculation:** 36/161×100=22.360248%, ordinarily 22.4%, not 22.3%.

**Alternative source-grounded interpretations:** The display may be truncated, a count/denominator may be contextual shorthand, or an unprinted denominator may have been used.

**Mechanical evidence recheck:** Direct-PDF recheck confirmed the 36, 22.3%, and 161 values; no rounding convention is printed.

**Quality-control relevance:** This is a printed background microbiological yield.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy a culture-yield percentage that does not identify its calculation convention unambiguously.

**Human verification steps:** Confirm the denominator and rounding/truncation convention; verify whether the printed count and percentage were produced from the same source population.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If a candidate is confirmed, the relevant count, percentage, denominator, threshold, distribution endpoint, or effect measure could be copied into a later extraction sheet or evidence synthesis. The supplied package does not establish any actual propagation, clinical consequence, or change in the study’s conclusions.

## Limitations and Missing Definitions

The package contains no raw observations, analysis code, direct arm-specific 28-day death counts, universal rounding convention, or complete row-specific estimator/test/variance details. These omissions constrain mechanism identification and some reconciliations; they do not determine an adjudication outcome. All sources were PDFs, so Office/workbook/CSV evidence was not applicable. Fresh text extraction can flatten table geometry; rendered pages were used to confirm relevant table/figure layouts. Protocol values may be planning, background, or preliminary material and were not assumed equivalent to final-trial results.

## Human Adjudication Checklist

1. Verify each cited PDF location against the direct supplied source.
2. Confirm population, denominator, time point, contrast, and calculation/rounding rule for each candidate.
3. Distinguish printed facts from diagnostic calculations and alternative explanations.
4. Record validity, importance, action, initials, and notes in each card; do not treat this report as a final correction.
5. Preserve candidate IDs and evidence provenance when communicating any adjudicated correction.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and Source Integrity

Fresh direct-source extraction used `pdfinfo`, `pdftotext`, `pdftotext -layout`, and targeted 150-dpi `pdftoppm` rendering. No OCR was required. SHA-256 hashes for all three direct PDFs were recorded before processing and matched on the preprocessing recheck. Canonical evidence, relationship, checker, recheck, and audit artifacts are under [`review_1_5_2/`](review_1_5_2/).

### Agent Execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | `run_state.md` |
| fresh_source_preprocessor | root/fresh_preprocessing | gpt-5.6-terra | medium | FRESH_SPAWN | `evidence_asset_inventory.md` |
| main_quantitative_mapper | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/main_quantitative_evidence.md` |
| support_quantitative_mapper_protocol | root/support_protocol_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/parts/support_protocol_quantitative_evidence.md` |
| support_quantitative_mapper_results | root/support_results_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/parts/support_results_quantitative_evidence.md` |
| numeric_consistency_main_protocol | root/numeric_main_protocol | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/parts/numeric_main_protocol.md` |
| numeric_consistency_support_results | root/numeric_support_results | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/parts/numeric_support_results.md` |
| cross_source_checks | root/cross_source_review | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/cross_source_consistency.md` |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_1.md` |
| evidence_recheck | root/evidence_recheck | gpt-5.6-sol | high | FRESH_SPAWN | `verification/evidence_recheck.md` |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_2.md` |
| evidence_quality | root/quality_audit | gpt-5.6-sol | high | FRESH_SPAWN | `quality/evidence_quality_audit.md` |
| report_generation | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | `report_generation_summary.md` |

### Performance

- **Target basis:** Three supplied PDFs totaling 47 pages, all requiring fresh native and layout extraction; one 8-page main article, one 29-page protocol with dispersed quantitative definitions, and one 10-page results supplement with five tables require full mapping, cross-document matching, and two complete statistical passes. Native text tooling is available and no Office conversion is expected.
- **Total source units:** 47
- **Fresh-source units:** 47
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-08-20T16:50:53Z
- **Finished UTC:** 2026-08-20T17:27:09Z
- **Observed elapsed minutes:** 36.3
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token-Usage and Cost Metadata

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

The runtime did not expose authoritative response-level token counts for the coordinator or any of the 12 specialist agents. Accordingly, every manifested agent has an `UNAVAILABLE` ledger row with exact `__` token fields; the displayed zero is only the sum of known counts, not an estimate of actual use.

| Model | Agents | Exact records | Totals-only records | Unavailable records | Known total tokens | Known cost (USD) | Complete estimated cost (USD) | Status |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| gpt-5.6-sol | 3 | 0 | 0 | 3 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| gpt-5.6-terra | 10 | 0 | 0 | 10 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |

These amounts are token-only API-equivalent estimates under the pricing snapshot dated 2026-08-18T00:00:00Z, not an invoice. Per-agent detail is recorded in `review_1_5_2/token_usage_summary.md` and `review_1_5_2/token_usage_summary.json`.

The coordinator fills the authoritative response-level token accounting after Markdown assembly and before rendering. Cached input/cache-write counts are input subsets and reasoning counts are output subsets; neither is added again to total tokens. Any price is a token-only API-equivalent estimate under the dated pricing snapshot, not an invoice. Per-agent detail will be in `review_1_5_2/token_usage_ledger.csv` and `review_1_5_2/token_usage_summary.md`.

Standalone HTML rendering and mechanical validation completed successfully after Markdown assembly; these local steps are excluded from the observed review duration.
