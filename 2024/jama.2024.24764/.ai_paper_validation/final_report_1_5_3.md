# Quantitative Quality-Control Consistency Review — Workflow 1.5.3

> **Pending Human Adjudication:** Every candidate in this report is a quality-control observation for human review. No candidate is a severity rating, final disposition, or conclusion about the paper's validity.

## Executive Quality-Control Summary

Complete supplied-source coverage identified **8** stable candidate consistency issues (C001-C008). They concern denominator conventions, response-unit labelling, a mortality-window discrepancy, and planned-versus-reported analytical specifications. Small preventable reporting defects can matter for downstream evidence extraction; this report does not assert that any defect propagated, changed a conclusion, or caused harm.

## Package and Reused-Evidence Provenance

The package contained four supplied PDFs: the main article (11 pages), SAP (46), results supplement (9), and protocol (48). Twenty source pages had complete reusable native-text coverage; 94 pages required fresh direct-source mapping. Reused OCR, page images, manifests, and document maps were used as locators and transcription aids only; the supplied PDFs remained the evidence authority. No Office document, workbook, or CSV source was supplied.

## Scope, Complete Coverage, and Exclusions

| Source | Total | Reusable | Fresh required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| Main article | 11 | 11 | 0 | 11 | Complete |
| SAP | 46 | 0 | 46 | 46 | Complete |
| Results supplement | 9 | 9 | 0 | 9 | Complete |
| Protocol | 48 | 0 | 48 | 48 | Complete |
| **Total** | **114** | **20** | **94** | **114** | **Complete** |

The review covered numeric, denominator, statistical, cross-document, measure/scale, rate/count, and concrete analysis-population relationships. It did not conduct a raw-data, clinical, study-design, misconduct, or external-literature audit. No candidate was created for a display-zero P value: no supplied result displayed `P = 0`, `p = 0.000`, or equivalent.

## Quantitative and Statistical Relationship Coverage

The numeric inventory covered N001-N060; the numeric checker completed all 60 records. The statistical inventory covered S001-S035. Statistical pass 1 and the independent statistical pass 2 each completed all 35 records. Cross-source review compared matched quantitative occurrences across all four supplied PDFs. Exact reconstruction was not claimed where the supplied sources omitted result-specific standard errors, degrees of freedom, final covariance/variance settings, model fallback details, or numerical plot data.

## Candidate Index

| ID | Category | Candidate |
|---|---|---|
| [C001](#c001--smoking-percentages-use-a-different-denominator-from-the-printed-smoking-totals) | Denominator, proportion, or total inconsistency | Smoking percentages and printed smoking totals use different denominators. |
| [C002](#c002--operating-surgeon-level-totals-exceed-participant-denominators-without-a-multi-response-qualifier) | Denominator, proportion, or total inconsistency | Operating-surgeon levels exceed participant denominators without a multi-response qualifier. |
| [C003](#c003--fascia-closing-surgeon-level-totals-exceed-participant-denominators-without-a-multi-response-qualifier) | Denominator, proportion, or total inconsistency | Fascia-closing levels exceed participant denominators without a multi-response qualifier. |
| [C004](#c004--skin-closing-surgeon-level-totals-exceed-participant-denominators-without-a-multi-response-qualifier) | Denominator, proportion, or total inconsistency | Skin-closing levels exceed participant denominators without a multi-response qualifier. |
| [C005](#c005--control-arm-mortality-differs-between-participant-flow-and-30-day-safety-reporting) | Cross-document numeric inconsistency | Participant flow and 30-day mortality report different control counts. |
| [C006](#c006--longitudinal-quality-of-life-covariance-specification-differs-between-sap-and-final-article) | Statistical reporting inconsistency | SAP and final article name different QoL covariance specifications. |
| [C007](#c007--length-of-stay-effect-measure-and-model-differ-between-sapprotocol-and-final-article) | Measure, label, or scale inconsistency | Planned and final length-of-stay effect measures/models differ. |
| [C008](#c008--australia-inclusive-length-of-stay-result-differs-from-the-stated-uk-only-analysis-population) | Analysis-unit or population inconsistency | Australia-inclusive length-of-stay result differs from UK-only planned population. |

## Candidate Evidence Cards

## C001 — Smoking percentages use a different denominator from the printed smoking totals

**Candidate statement:** The smoking rows print variable-specific totals of 405 and 402, while all six percentages reproduce the group-header denominators 411 and 410 without an explanatory convention.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_atherton_2025_oi_240145_1741627844.85412.pdf — PDF p. 5, Table 1](<../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=5>)

**Source evidence:** Smoking counts are 220/95/90 and 223/70/109; they sum to printed `Total No.` values 405 and 402. Group headers are 411 and 410.

**Reported-versus-comparator:** Reported percentages are 53.5/23.1/21.9 and 54.4/17.1/26.6; comparator denominators are printed smoking totals 405/402 versus group headers 411/410.

**Reasoning procedure:** Compare each count and percentage with both available denominator pairs, while preserving the possibility that the table intentionally uses randomized-group denominators.

**Calculation:** `220+95+90=405`; `223+70+109=402`. `220/411=53.53%` and the other five printed percentages likewise reproduce 411/410, not 405/402.

**Alternative source-grounded interpretations:** `Total No.` may denote nonmissing smoking records while percentages intentionally use all randomized participants; the page does not state that convention or identify the six and eight unclassified records.

**Mechanical evidence recheck:** Location, counts, headers, totals, percentages, and arithmetic were directly matched; the missing input is the intended denominator convention.

**Quality-control relevance:** A table should make clear whether the percentages represent observed smoking records or all randomized participants.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy smoking prevalence or missingness using a different denominator convention. No propagation or conclusion change is asserted.

**Human verification steps:** Confirm the table programming specification, smoking missingness, and intended denominator; add a table note if percentages deliberately use 411/410.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Operating-surgeon level totals exceed participant denominators without a multi-response qualifier

**Candidate statement:** Operating-surgeon category totals exceed the printed participant denominators without a statement that the rows permit multiple responses.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_atherton_2025_oi_240145_1741627844.85412.pdf — PDF p. 7, Table 2](<../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=7>)

**Source evidence:** Under `No. of participants (%)`, consultant/registrar/senior-house-officer values are 319/123/4 and 318/110/1, with group denominators 411 and 410.

**Reported-versus-comparator:** Category totals 446 and 429 are compared with participant denominators 411 and 410; percentage totals are 108.5% and 104.6%.

**Reasoning procedure:** Apply the single-response participant-category rule conditionally, because multiple operating-surgeon levels could legitimately be recorded for one participant.

**Calculation:** `319+123+4=446` (35 above 411); `318+110+1=429` (19 above 410).

**Alternative source-grounded interpretations:** More than one surgeon level may have operated on a participant, making the rows multi-response; no qualifier appears on the page.

**Mechanical evidence recheck:** Printed counts, denominators, label, and sums were matched. The necessary missing definition is whether one participant could contribute to more than one level.

**Quality-control relevance:** The response unit determines whether these rows are interpretable as exclusive participant proportions or an operator-level distribution.

**Potential downstream evidence impact:** If confirmed, an extractor could treat multi-response rows as exclusive participant proportions. No outcome-analysis or conclusion effect is asserted.

**Human verification steps:** Confirm the data-collection response unit and add a multi-response/denominator qualifier if applicable.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Fascia-closing surgeon level totals exceed participant denominators without a multi-response qualifier

**Candidate statement:** Fascia-closing surgeon-level totals exceed participant denominators without a stated multi-response rule.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_atherton_2025_oi_240145_1741627844.85412.pdf — PDF p. 7, Table 2 continuation](<../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=7>)

**Source evidence:** Consultant/registrar/senior-house-officer fascia-closing counts are 201/218/26 and 193/225/15 under group denominators 411 and 410.

**Reported-versus-comparator:** Totals 445 and 433 are compared with 411 and 410; percentage totals are 108.2% and 105.7%.

**Reasoning procedure:** Test the conditional single-response interpretation, while recognizing that co-closure could yield multiple level records per participant.

**Calculation:** `201+218+26=445` (34 above 411); `193+225+15=433` (23 above 410).

**Alternative source-grounded interpretations:** Co-closure by more than one surgeon level may make the rows intentionally multi-response; the table gives no response-unit definition.

**Mechanical evidence recheck:** Source values, denominators, labels, and calculations were directly matched; the multi-response definition is unavailable.

**Quality-control relevance:** The source should identify the counting unit when category totals are not mutually exclusive.

**Potential downstream evidence impact:** If confirmed, reuse of these rows could apply an unsupported unit or exclusivity assumption. No propagation or conclusion change is asserted.

**Human verification steps:** Verify whether one participant can be counted at more than one fascia-closing level and clarify the table label/footnote.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Skin-closing surgeon level totals exceed participant denominators without a multi-response qualifier

**Candidate statement:** Skin-closing surgeon-level totals exceed participant denominators without a stated multi-response rule.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_atherton_2025_oi_240145_1741627844.85412.pdf — PDF p. 7, Table 2 continuation](<../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=7>)

**Source evidence:** Consultant/registrar/senior-house-officer skin-closing counts are 115/214/96 and 102/241/73 under denominators 411 and 410.

**Reported-versus-comparator:** Totals 425 and 416 are compared with 411 and 410; percentage totals are 103.5% and 101.5%.

**Reasoning procedure:** Apply the single-response rule conditionally, as multiple people participating in a closure could instead explain the totals.

**Calculation:** `115+214+96=425` (14 above 411); `102+241+73=416` (6 above 410).

**Alternative source-grounded interpretations:** The rows may be intended multi-response entries, but the source does not state this.

**Mechanical evidence recheck:** Printed counts, percentages, denominators, and sums were matched. The response-unit definition remains missing.

**Quality-control relevance:** Clear labelling prevents category percentages from being read as an exclusive patient-level distribution when they are not.

**Potential downstream evidence impact:** If confirmed, a downstream table extraction could use an incorrect patient-level or operator-level interpretation. No harm or conclusion change is asserted.

**Human verification steps:** Verify the skin-closure recording rule and amend the label or footnote if multiple levels were allowed.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Control-arm mortality differs between participant flow and 30-day safety reporting

**Candidate statement:** Participant flow reports 25 deaths (10 intervention, 15 control), whereas Table 3 and the safety narrative report 24 deaths within 30 days (10 intervention, 14 control).

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_atherton_2025_oi_240145_1741627844.85412.pdf — PDF p. 3, Figure 1](<../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=3>); [PDF p. 6, safety narrative](<../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=6>); [PDF p. 8, Table 3](<../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=8>)

**Source evidence:** Figure 1 reports 10 and 15 deaths. The narrative and Table 3 report mortality within 30 days as 10/411 and 14/410.

**Reported-versus-comparator:** Figure 1 total 25 and control count 15 are compared with the explicitly 30-day total 24 and control count 14.

**Reasoning procedure:** Compare matched arm counts while preserving the source's distinct or unspecified event-time windows.

**Calculation:** `10+15=25`; `10+14=24`; intervention counts agree and control counts differ by one.

**Alternative source-grounded interpretations:** Figure 1 may include one control-arm death outside the 30-day window; Figure 1 does not name its mortality window.

**Mechanical evidence recheck:** All three locations and printed counts were matched. The missing input is the Figure 1 death-time window and event dates.

**Quality-control relevance:** Event count and time-window labels should reconcile across flow and safety reporting.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a different control-arm mortality count, total, or window. No assertion is made that mortality reporting or the paper's conclusion is wrong.

**Human verification steps:** Reconcile individual death dates with Figure 1 and Table 3, then state the Figure 1 mortality window or correct the displayed count.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Longitudinal quality-of-life covariance specification differs between SAP and final article

**Candidate statement:** The SAP specifies unstructured covariance with robust sandwich standard errors for the QoL model family, while the final article specifies independent covariance.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [joi240145supp1_prod_1741627844.87412.pdf — PDF p. 26, SAP](<../joi240145supp1_prod_1741627844.87412.pdf#page=26>); [jama_atherton_2025_oi_240145_1741627844.85412.pdf — PDF p. 4, Statistical Analysis](<../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=4>)

**Source evidence:** The SAP prints `unstructured` covariance and robust sandwich standard errors for SF-12/EQ-5D repeated measures; the final article prints `independent` covariance for that outcome-model family.

**Reported-versus-comparator:** Final-article independent covariance is compared with SAP unstructured covariance and robust sandwich variance estimation.

**Reasoning procedure:** Compare the named model specifications directly; do not infer whether a variance estimator was absent merely because the article is silent.

**Calculation:** Not applicable; `unstructured` and `independent` are distinct named covariance specifications.

**Alternative source-grounded interpretations:** An amendment, diagnostic, convergence consideration, or concise article description may explain the difference; no such record is supplied.

**Mechanical evidence recheck:** Both printed descriptions were directly matched. Final covariance/variance-estimation output and any amendment are unavailable.

**Quality-control relevance:** Accurate model-specification reporting supports reproducible interpretation of QoL uncertainty estimates.

**Potential downstream evidence impact:** If confirmed, evidence users could extract or interpret the QoL model specification or uncertainty method differently. No claim is made that estimates, P values, or conclusions changed.

**Human verification steps:** Inspect the final analysis code/output and amendment history; identify the covariance and variance-estimation settings used for published estimates.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Length-of-stay effect measure and model differ between SAP/protocol and final article

**Candidate statement:** SAP/protocol describe adjusted mean difference, or skewed-data unadjusted median difference, whereas the final article reports log-transformed adjusted ratios of geometric means for length of stay.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi240145supp1_prod_1741627844.87412.pdf — PDF p. 25, SAP](<../joi240145supp1_prod_1741627844.87412.pdf#page=25>); [joi240145supp4_prod_1741627844.90412.pdf — PDF p. 39, protocol](<../joi240145supp4_prod_1741627844.90412.pdf#page=39>); [jama_atherton_2025_oi_240145_1741627844.85412.pdf — PDF p. 4](<../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=4>); [PDF p. 8, Table 3](<../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=8>)

**Source evidence:** The final article reports adjusted ratios of geometric means 0.91 and 0.96 after log transformation; SAP/protocol plan additive mean-difference or median-difference reporting.

**Reported-versus-comparator:** Multiplicative, dimensionless ratios of geometric means are compared with additive differences in days for the same endpoint.

**Reasoning procedure:** Compare effect-measure scale and model descriptions, using the UK-only result as the population-matched comparison and retaining population identity separately in C008.

**Calculation:** Not reproducible from aggregate printed data: medians/IQRs cannot reconstruct geometric means, fitted log-scale coefficients, or adjusted ratios.

**Alternative source-grounded interpretations:** Nonnormality noted in the article may have motivated the final approach, but the supplied skewness branch specifies a median difference and no amendment or decision rule is supplied.

**Mechanical evidence recheck:** Planned and final model/effect-measure statements and Table 3 ratios were matched. Executed model output and amendment documentation are unavailable.

**Quality-control relevance:** Effect-measure identity is necessary for correct comparison, synthesis, and interpretation.

**Potential downstream evidence impact:** If confirmed, a data extractor could use an incorrect LOS scale, effect measure, or model label. No claim is made that the ratios or conclusion are wrong.

**Human verification steps:** Verify the final analysis decision rule/amendment and state which effect measure was intended for extraction and interpretation.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Australia-inclusive length-of-stay result differs from the stated UK-only analysis population

**Candidate statement:** SAP and protocol specify UK-only length-of-stay reporting, while the final article additionally reports a UK-and-Australia result.

**Category:** Analysis-unit or population inconsistency

**Exact source locations:** [joi240145supp1_prod_1741627844.87412.pdf — PDF p. 18, SAP endpoint](<../joi240145supp1_prod_1741627844.87412.pdf#page=18>); [PDF p. 25, SAP population](<../joi240145supp1_prod_1741627844.87412.pdf#page=25>); [joi240145supp4_prod_1741627844.90412.pdf — PDF p. 24, protocol](<../joi240145supp4_prod_1741627844.90412.pdf#page=24>); [jama_atherton_2025_oi_240145_1741627844.85412.pdf — PDF p. 1, abstract](<../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=1>); [PDF p. 8, Table 3](<../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=8>)

**Source evidence:** SAP/protocol state that LOS is UK-only and exclude Australian-randomized participants. The final article reports UK-only ratio 0.91 (95% CI 0.82-1.02), P=.12 and UK-and-Australia ratio 0.96 (0.88-1.06), P=.21.

**Reported-versus-comparator:** A UK-and-Australia analysis population is compared with the planned UK-only endpoint population.

**Reasoning procedure:** Treat population definition as part of result identity; do not infer whether the additional all-country analysis was planned, amended, sensitivity, exploratory, or post hoc.

**Calculation:** No arithmetic reconstruction is required: `UK patients only` and `UK and Australian patients` are different populations.

**Alternative source-grounded interpretations:** The all-country result may be an additional intended analysis while the UK-only result remains the designated endpoint; the supplied package does not label its status.

**Mechanical evidence recheck:** The SAP, final results, and protocol statement were directly matched. The correct protocol locator is PDF p. 24. Amendment status, result-specific denominators, and missing-data rules are unavailable.

**Quality-control relevance:** Population labels are essential to correct identification and pooling of endpoint estimates.

**Potential downstream evidence impact:** If confirmed, downstream extraction or pooling could attach the LOS estimate to a UK-only versus all-country population label incorrectly. No conclusion change is asserted.

**Human verification steps:** Review later SAPs/amendments and final model metadata; identify the all-country analysis status, denominators, missing-data rules, and designated endpoint population.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed, these observations could affect how data extractors record denominators, response units, mortality windows, population labels, effect measures, or model descriptions. They are presented as bounded risks to downstream evidence products such as systematic reviews, meta-analyses, and guidelines, not as evidence that reuse occurred or that any conclusion changed.

## Limitations and Missing Definitions

The supplied package does not include participant-level data, executed code, final model output, later amendments, result-specific standard errors/degrees of freedom, all covariance/variance settings, or unprinted denominator and response-unit definitions. Plotted tipping-point coordinates were not supplied numerically. These limitations prevent adjudication and exact reconstruction in the affected records; they do not erase direct printed comparisons.

## Human Adjudication Checklist

1. Confirm each cited source location and transcription.
2. Resolve the named denominator, response-unit, time-window, model, amendment, or population definition.
3. Determine validity, importance, and any action in the card fields.
4. Record reviewer initials and notes without changing stable candidate IDs.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and Source Integrity

- **Routing preflight:** PASS; coordinator inference PASS; execution mode `INTERACTIVE_CLI`; all nine named role presets verified.
- **Source-unit counts:** 114 total; 20 reusable; 94 fresh-required; 114 mapped.
- **Source integrity:** Four direct-source SHA-256 hashes and 51 reused-artifact SHA-256 hashes were recorded before review. Pre-close recomputation and validation remain coordinator closeout work.
- **Evidence boundary:** Supplied local package sources only; no web evidence used; no source or reused artifact was modified.

### Agent Execution

| Stage | Agent ID | Model | Effort |
|---|---|---|---|
| coordinator | `/root` | gpt-5.6-sol | high |
| reuse_asset_curator | `/root/reuse_asset_curator` | gpt-5.6-terra | medium |
| main_quantitative_mapper | `/root/main_quantitative_mapper` | gpt-5.6-terra | medium |
| support_quantitative_mapper | `/root/support_quantitative_mapper` | gpt-5.6-terra | medium |
| numeric_consistency_reviewer | `/root/numeric_consistency_reviewer` | gpt-5.6-terra | medium |
| cross_source_consistency_reviewer | `/root/cross_source_consistency_reviewer` | gpt-5.6-terra | medium |
| statistics_pass_1 | `/root/statistical_pass_1` | gpt-5.6-terra | high |
| evidence_rechecker | `/root/evidence_rechecker` | gpt-5.6-sol | high |
| statistics_pass_2 | `/root/statistical_pass_2` | gpt-5.6-terra | high |
| evidence_rechecker_append_C008 | `/root/evidence_rechecker_c008` | gpt-5.6-sol | high |
| quality_control_auditor | `/root/quality_control_auditor` | gpt-5.6-sol | high |
| report_generator | `/root/report_generator` | gpt-5.6-terra | medium |

### Performance

- **Target basis:** Four supplied PDFs contain 114 PDF-page source units. Twenty main-article/results-supplement pages have complete page-delimited native text, with visual/OCR companions on 13 table/figure pages; 94 SAP/protocol pages require fresh direct-source mapping. The mixed main article, results supplement, SAP, and protocol require two mapping lanes and the mandatory downstream checking, recheck, and reporting waves.
- **Total source units:** 114
- **Fresh-source units:** 94
- **Target elapsed minutes:** 55-75
- **Started UTC:** 2026-08-19T05:20:02Z
- **Finished UTC:** 2026-08-19T05:44:37Z
- **Observed elapsed minutes:** 24.6
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token Usage and Cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Token totals |
|---|---|
| gpt-5.6-sol | Known total 0; 4 unavailable response records; known cost USD 0.000000; complete total and price unavailable |
| gpt-5.6-terra | Known total 0; 8 unavailable response records; known cost USD 0.000000; complete total and price unavailable |

Per-agent detail will be recorded in `review_1_5_3/token_usage_summary.md`. Any available amount uses the bundled dated fixed-model rates and is a token-only estimate, not an invoice. Cached input and cache-write counts are input subsets, and reasoning tokens are an output subset; none is added again to total tokens.
