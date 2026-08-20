# Quantitative Quality-Control Consistency Review

## Pending Human Adjudication

All ten observations in this report are quality-control candidates only and remain **Pending Human Adjudication**. This review does not determine validity, importance, a correction, or an editorial action; it does not assign severity or draw a conclusion about the trial.

## Executive Quality-Control Summary

Fresh, source-first review of the complete supplied package identified 10 distinct reporting-consistency candidates: one matched narrative/figure hazard-ratio conflict, six exact-fraction versus displayed-difference diagnostics, and three point-estimate/interval containment mismatches. The complete candidate set is C001-C010 in ledger order. No candidate was based solely on a display-zero P value; no such display occurred in the mapped results.

## Package and Fresh-Processing Provenance

The package contained three supplied PDFs and no Office, workbook, CSV, or external source. All direct sources were processed afresh; no prior audit derivative was used as evidence, no source was modified, and no web material was used.

| Source | Role | Units | SHA-256 |
|---|---|---:|---|
| `jama_saccone_2017_oi_170144.pdf` | Main randomized clinical-trial article | 8 PDF pages | `ef598eafd5458d572fad896a0decfd921e810989970a9b3cc9e51d779812937f` |
| `joi170144supp1_prod.pdf` | Protocol / prespecified definitions and analysis plan | 16 PDF pages | `ad3a483ebb6fa19e67c030eb332b9a3df668a6fd8f5715ab09c02bad3008e2df` |
| `joi170144supp2_prod.pdf` | Results supplement with eTables | 4 PDF pages | `3b7a3ff0ee0fa03b443eb026c592f1da011aeeeea64cd4b19d20396cdd7e60e4` |

Fresh native and layout text were extracted for all 28 pages. Result-relevant tables and figures were rendered locally for visual confirmation. Native text was usable throughout; targeted CPU OCR was therefore not required.

## Scope, Complete Coverage, and Exclusions

All 28 direct-source page units were freshly required and mapped: DOC-001 8/8, DOC-002 16/16, and DOC-003 4/4. The mapping covered numeric values, denominators, proportions, differences, intervals, effect measures, labels, matched locations, protocol definitions, and result-relevant table and figure displays.

Excluded from candidate registration were general methodology, clinical interpretation, raw-data, novelty, and misconduct questions; external literature; untestable model reconstruction; and the correction notice where the prior wording was not supplied. Microbial categories in eTable 1 were not summed because mutual exclusivity was not stated.

## Quantitative and Statistical Relationship Coverage

The numeric/reporting inventory covered N001-N072 (72 of 72) across the main article, protocol, and supplement. The first independent statistical pass covered S001-S050 (50 of 50); the distinct second pass revisited S001-S050 (50 of 50) after candidate registration and mechanical recheck. Both passes were complete. Bootstrap, Cox, simulation, and Wald calculations were not reconstructed where matching source inputs were absent; direct printed relationships were still checked to the evidence-supported extent.

## Candidate Index

| ID | Category | Short observation | Status |
|---|---|---|---|
| C001 | Cross-document numeric inconsistency | Spontaneous-delivery HR differs between narrative and Figure 2B | Pending Human Adjudication |
| C002 | Numeric or arithmetic inconsistency | SPTB <32-week difference versus exact counts | Pending Human Adjudication |
| C003 | Numeric or arithmetic inconsistency | Operative-vaginal-delivery difference versus exact counts | Pending Human Adjudication |
| C004 | Numeric or arithmetic inconsistency | Chorioamnionitis difference versus exact counts | Pending Human Adjudication |
| C005 | Numeric or arithmetic inconsistency | Perinatal-death difference versus exact counts | Pending Human Adjudication |
| C006 | Statistical reporting inconsistency | Birth-weight <2500-g difference outside printed CI | Pending Human Adjudication |
| C007 | Numeric or arithmetic inconsistency | Respiratory-distress difference versus exact counts | Pending Human Adjudication |
| C008 | Numeric or arithmetic inconsistency | Cervical-length subgroup difference at rounding boundary | Pending Human Adjudication |
| C009 | Statistical reporting inconsistency | Cesarean-delivery difference outside printed CI | Pending Human Adjudication |
| C010 | Statistical reporting inconsistency | Operative-vaginal-delivery difference outside printed CI | Pending Human Adjudication |

## Candidate Evidence Cards

## C001 — Spontaneous-delivery hazard ratio conflicts across narrative and Figure 2B

**Candidate statement:** The narrative prints HR 0.36 (95% CI, 0.54-0.87) for spontaneous delivery through 34 weeks, whereas Figure 2B prints HR 0.68 with the identical CI.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [Main article — PDF p. 5](<../jama_saccone_2017_oi_170144.pdf#page=5>), Primary Outcome narrative; [main article — PDF p. 6](<../jama_saccone_2017_oi_170144.pdf#page=6>), Figure 2B, “Spontaneous delivery only.”

**Source evidence:** The p. 5 narrative states HR 0.36; Figure 2B states HR 0.68. Both print 95% CI 0.54-0.87 for the spontaneous-delivery Cox/KM context.

**Reported-versus-comparator:** Reported narrative HR 0.36 versus Figure 2B HR 0.68, and narrative HR 0.36 versus its printed CI [0.54, 0.87].

**Reasoning procedure:** Match outcome, time horizon, analysis context, and CI; then check cross-location equality and point-estimate containment in the same-scale ordered interval.

**Calculation:** 0.36 != 0.68; 0.36 < 0.54, while 0.54 <= 0.68 <= 0.87.

**Alternative source-grounded interpretations:** Figure 2A is a distinct all-delivery analysis (HR 0.70, 95% CI 0.55-0.88), not a resolution of the matched spontaneous-delivery conflict. An unreported model difference or transcription error remains possible but is not established.

**Mechanical evidence recheck:** Both cited values, the identical CI, the outcome label, and the Figure 2B identity were found and the logical comparisons reproduced. Cox coefficients, standard errors, and an authoritative output identifying the intended HR are absent.

**Quality-control relevance:** A matched result should identify the same point estimate across its narrative and figure occurrence and be compatible with its own CI.

**Potential downstream evidence impact:** If confirmed, an extractor could copy the narrative HR or the Figure 2B HR into a systematic review or evidence table; this report does not assert that either was propagated or changed a conclusion.

**Human verification steps:** Obtain the Cox model output for spontaneous delivery through 34 weeks; confirm the event/censoring specification and intended HR/CI; compare the production files for the narrative and Figure 2B.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — SPTB under 32 weeks difference does not round from printed counts

**Candidate statement:** Table 2 prints 10/150 (6.7%) versus 14/150 (9.3%) and a -2.6% difference; the exact fractions yield -2.666..., conventionally -2.7% to one decimal.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [Main article — PDF p. 5](<../jama_saccone_2017_oi_170144.pdf#page=5>), Table 2, spontaneous preterm birth <32 weeks.

**Source evidence:** The arm headers are n=150; the row prints 10 (6.7), 14 (9.3), and -2.6%.

**Reported-versus-comparator:** Printed -2.6% versus the exact-fraction, one-decimal result -2.7%.

**Reasoning procedure:** Compute 100 times the pessary risk minus the control risk from the printed counts and denominators; compare with standard nearest-one-decimal rounding.

**Calculation:** 100*(10/150 - 14/150) = -2.666... -> -2.7%; 6.7 - 9.3 = -2.6%.

**Alternative source-grounded interpretations:** The printed value is reproducible by subtracting displayed rounded percentages. The methods describe cumulative-incidence differences and bootstrap CIs but do not state whether rounded displays, exact risks, or another denominator produced the point difference.

**Mechanical evidence recheck:** Counts, denominators, displayed percentages, contrast order, and printed difference were located; the arithmetic reproduced. The production code and point-estimate rounding convention are not supplied.

**Quality-control relevance:** The row requires a stated convention to reconcile its exact counts with the displayed point difference.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy a last-digit risk difference that differs from an exact-fraction calculation; no downstream use or conclusion change is asserted.

**Human verification steps:** Review the table-generation dataset/code and identify the denominator and rounding convention used for risk differences.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Operative-vaginal-delivery difference does not round from printed counts

**Candidate statement:** Table 2 prints 5/150 (3.3%) versus 10/150 (6.7%) and -3.4%; exact fractions yield -3.333..., conventionally -3.3%.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [Main article — PDF p. 5](<../jama_saccone_2017_oi_170144.pdf#page=5>), Table 2, operative vaginal delivery.

**Source evidence:** The row prints the two arm counts, percentages, -3.4% difference, and 95% CI -2.1 to 9.1.

**Reported-versus-comparator:** Printed -3.4% versus exact-fraction rounding -3.3%. This arithmetic diagnostic is distinct from C010’s point/CI containment rule.

**Reasoning procedure:** Use the printed counts under n=150 per arm and standard nearest-one-decimal rounding.

**Calculation:** 100*(5/150 - 10/150) = -3.333... -> -3.3%; 3.3 - 6.7 = -3.4%.

**Alternative source-grounded interpretations:** The printed -3.4% is reproduced by displayed-percentage subtraction. The main article describes cumulative-incidence differences without defining the calculation convention.

**Mechanical evidence recheck:** The full row, headers, and comparator were found and the calculation reproduced. Table-production code and an explicit exact-risk versus rounded-display rule are absent.

**Quality-control relevance:** The observed counts and displayed difference need an explicit common calculation convention for transparent quantitative extraction.

**Potential downstream evidence impact:** If confirmed, an evidence table could reproduce a last-digit difference under a convention not clear from the report; no propagation or clinical implication is claimed.

**Human verification steps:** Confirm the intended point-difference calculation and rounding rule from source analysis materials.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Chorioamnionitis difference does not round from printed counts

**Candidate statement:** Table 2 prints 5/150 (3.3%) versus 7/150 (4.7%) and -1.4%; exact fractions yield -1.333..., conventionally -1.3%.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [Main article — PDF p. 5](<../jama_saccone_2017_oi_170144.pdf#page=5>), Table 2, chorioamnionitis.

**Source evidence:** The row supplies both n=150 arm counts, percentages, -1.4% difference, and CI -3.7 to 6.6.

**Reported-versus-comparator:** Printed -1.4% versus exact-fraction rounding -1.3%.

**Reasoning procedure:** Calculate the risk difference from the printed fractions and compare it with standard one-decimal rounding.

**Calculation:** 100*(5/150 - 7/150) = -1.333... -> -1.3%; 3.3 - 4.7 = -1.4%.

**Alternative source-grounded interpretations:** Subtraction of displayed rounded percentages reproduces -1.4%. The supplied methods do not specify that this was the point-estimate convention or identify another denominator.

**Mechanical evidence recheck:** The cited row and headers were found; the fraction and displayed-percentage calculations reproduced. Internal unrounded values and production code are missing.

**Quality-control relevance:** The reported difference is not transparent from exact printed counts without an unstated calculation convention.

**Potential downstream evidence impact:** If confirmed, a reviewer could copy an ambiguous last-digit risk difference into an evidence extraction; this does not assert any downstream use or effect.

**Human verification steps:** Confirm the calculation source, denominator, and rounding policy for this Table 2 risk difference.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Perinatal-death difference does not round from printed counts

**Candidate statement:** Table 2 prints 2/150 (1.3%) versus 4/150 (2.7%) and -1.4%; exact fractions yield -1.333..., conventionally -1.3%.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [Main article — PDF p. 5](<../jama_saccone_2017_oi_170144.pdf#page=5>), Table 2, perinatal death.

**Source evidence:** The row prints the counts, percentages, -1.4% difference, 95% CI -2.5 to 5.6, RR 0.50 (0.09-2.69), and P=.68.

**Reported-versus-comparator:** Printed -1.4% versus exact-fraction rounding -1.3%.

**Reasoning procedure:** Compare the reported difference with the nearest-one-decimal risk difference from the two printed fractions.

**Calculation:** 100*(2/150 - 4/150) = -1.333... -> -1.3%; 1.3 - 2.7 = -1.4%.

**Alternative source-grounded interpretations:** The table value equals displayed-percentage subtraction. The supplied methods do not state that this convention, rather than exact fractions or an alternate calculation, governed the point difference.

**Mechanical evidence recheck:** The full row and arm denominators were located and both comparisons were reproduced. Production code and the point-estimate convention are unavailable.

**Quality-control relevance:** Transparent reporting requires knowing whether a point difference reflects exact event risks or displayed rounded values.

**Potential downstream evidence impact:** If confirmed, a later evidence product could copy a last-digit difference without its calculation convention; no downstream propagation or conclusion change is claimed.

**Human verification steps:** Inspect the analysis output or production table and document the intended denominator and rounding convention.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Birth weight under 2500 g difference lies outside its printed CI

**Candidate statement:** eTable 2 prints a -11.3% risk difference for birth weight <2500 g with 95% CI -1.1 to +21.2; the point estimate is outside that interval.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [Results supplement — PDF p. 3](<../joi170144supp2_prod.pdf#page=3>), eTable 2, birth weight <2500 grams.

**Source evidence:** Pessary 28/150 (18.7%), control 45/150 (30.0%), difference -11.3%, CI -1.1 to +21.2, RR 0.62 (0.41-0.94), P=.03.

**Reported-versus-comparator:** Printed -11.3% risk difference versus its printed ordered CI [-1.1, +21.2].

**Reasoning procedure:** Check containment of the labeled point estimate in its same-scale interval, with count and RR direction used as corroborating context rather than a reconstructed CI.

**Calculation:** 100*(28/150 - 45/150) = -11.333... -> -11.3%; -11.3 < -1.1, so the point is outside the printed interval.

**Alternative source-grounded interpretations:** A reverse contrast could explain the sign pattern because +11.3 lies within the printed interval, while the RR and counts favor the negative pessary-minus-control direction. A sign/endpoint transcription issue is also possible; neither is established and no replacement CI is inferred.

**Mechanical evidence recheck:** The row values, interval, RR, and P value were found and containment reproduced. Bootstrap resamples, CI output, and an authoritative contrast-direction record are not supplied.

**Quality-control relevance:** A labeled risk difference and its CI should share direction and scale and contain the point estimate.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an internally mismatched risk difference/CI pair into a meta-analysis or evidence table; no propagation or conclusion change is asserted.

**Human verification steps:** Retrieve the bootstrap output and verify the risk-difference contrast direction and signed endpoints for this row.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Respiratory-distress-syndrome difference does not round from printed counts

**Candidate statement:** eTable 2 prints 14/150 (9.3%) versus 31/150 (20.7%) and -11.4%; exact fractions yield -11.333..., conventionally -11.3%.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [Results supplement — PDF p. 3](<../joi170144supp2_prod.pdf#page=3>), eTable 2, respiratory distress syndrome.

**Source evidence:** The row prints two N=150 arm values, -11.4%, CI -19.9 to -2.9, RR 0.45 (0.25-0.81), and P=.01.

**Reported-versus-comparator:** Printed -11.4% versus exact-fraction rounding -11.3%.

**Reasoning procedure:** Calculate the crude percentage-point difference from the printed counts and compare against nearest-one-decimal rounding.

**Calculation:** 100*(14/150 - 31/150) = -11.333... -> -11.3%; 9.3 - 20.7 = -11.4%.

**Alternative source-grounded interpretations:** The printed difference is exactly reproduced from displayed percentages. eTable 2 identifies number/percentage displays but does not define whether these rounded percentages generated the point difference.

**Mechanical evidence recheck:** Counts, denominators, percentages, contrast, and difference were found and the calculation reproduced. The table-production code and explicit convention are absent.

**Quality-control relevance:** The row’s exact fractions and its presented risk difference need a stated convention to reconcile.

**Potential downstream evidence impact:** If confirmed, a systematic reviewer could copy a last-digit difference that depends on an unclear convention; no downstream use or effect is claimed.

**Human verification steps:** Verify the source calculation and rounding convention for the eTable 2 difference.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Cervical-length subgroup difference is on the opposite side of the rounding boundary

**Candidate statement:** eTable 3 prints 3/56 (5.4%) versus 10/42 (23.8%) and -18.4%; exact fractions yield -18.45238..., which rounds to -18.5%.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [Results supplement — PDF p. 4](<../joi170144supp2_prod.pdf#page=4>), eTable 3, TVU cervical length <=10 mm subgroup.

**Source evidence:** The subgroup row prints the exact fractions, displayed percentages, -18.4% difference, CI -34.6 to -3.3, RR 0.23 (0.07-0.77), and P=.02.

**Reported-versus-comparator:** Printed -18.4% versus exact-fraction nearest-one-decimal rounding -18.5%.

**Reasoning procedure:** Derive the percentage-point contrast from the printed subgroup fractions and compare with one-decimal rounding, noting the rounding boundary.

**Calculation:** 100*(3/56 - 10/42) = -18.452380... -> -18.5%; 5.4 - 23.8 = -18.4%. The exact value is about 0.00238 percentage points beyond the -18.45 midpoint toward -18.5.

**Alternative source-grounded interpretations:** Displayed-percentage subtraction yields -18.4%. eTable 3 does not specify whether it uses exact fractions, display-rounded percentages, or an alternate internal convention; the near-boundary position makes that distinction material.

**Mechanical evidence recheck:** Exact numerators, denominators, displayed percentages, and difference were found; both computations reproduced. The point-estimate production rule is absent.

**Quality-control relevance:** A transparent subgroup estimate requires a stated rule when exact-fraction and rounded-display calculations fall on opposite sides of a rounding boundary.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy the displayed subgroup difference without knowing its convention; no propagation or conclusion change is asserted.

**Human verification steps:** Inspect the subgroup analysis output and document the calculation and rounding rule used for the displayed risk difference.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Cesarean-delivery difference lies outside its printed CI

**Candidate statement:** Table 2 prints a -8.0% cesarean-delivery difference with 95% CI -3.2 to 19.0; the point estimate is outside the interval.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [Main article — PDF p. 5](<../jama_saccone_2017_oi_170144.pdf#page=5>), Table 2, cesarean delivery.

**Source evidence:** Pessary 45/150 (30.0%), control 57/150 (38.0%), difference -8.0%, CI -3.2 to 19.0, RR 0.79 (0.57-1.09), P=.18.

**Reported-versus-comparator:** Printed -8.0% risk difference versus its printed ordered CI [-3.2, 19.0].

**Reasoning procedure:** Check containment of the same-scale point estimate in the reported CI and compare the point direction with printed arm risks.

**Calculation:** 30.0 - 38.0 = -8.0; -8.0 < -3.2, therefore -8.0 is outside [-3.2, 19.0].

**Alternative source-grounded interpretations:** A control-minus-pessary CI could be a possible explanation because +8.0 lies within the interval, but the shared Table 2 column does not state mixed contrast directions. A sign or endpoint production error is also possible; no corrected interval is supplied.

**Mechanical evidence recheck:** The row, interval, arm percentages, RR, and P value were located and containment reproduced. Bootstrap draws and an authoritative signed CI output are unavailable.

**Quality-control relevance:** A point risk difference should lie in its labeled interval under the same contrast and scale.

**Potential downstream evidence impact:** If confirmed, a later evidence synthesis could copy a nonreconciling risk difference/CI pair; this review makes no claim that this occurred or changed a conclusion.

**Human verification steps:** Obtain the bootstrap risk-difference output and confirm contrast direction and signed CI endpoints.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — Operative-vaginal-delivery difference lies outside its printed CI

**Candidate statement:** Table 2 prints a -3.4% operative-vaginal-delivery difference with 95% CI -2.1 to 9.1; the point estimate is outside the interval.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [Main article — PDF p. 5](<../jama_saccone_2017_oi_170144.pdf#page=5>), Table 2, operative vaginal delivery.

**Source evidence:** Pessary 5/150 (3.3%), control 10/150 (6.7%), difference -3.4%, CI -2.1 to 9.1, RR 0.50 (0.18-1.43), P=.29.

**Reported-versus-comparator:** Printed -3.4% risk difference versus its printed ordered CI [-2.1, 9.1]. This containment diagnostic is distinct from C003’s exact-fraction rounding rule.

**Reasoning procedure:** Check point-estimate containment in the labeled same-scale CI, independently of the exact-fraction rounding diagnostic.

**Calculation:** -3.4 < -2.1, so -3.4 is outside [-2.1, 9.1]; +3.4 would lie within the interval.

**Alternative source-grounded interpretations:** A reverse-contrast interval or endpoint/sign transcription could explain the observed mismatch, but neither is established from the supplied package and no replacement CI is inferred.

**Mechanical evidence recheck:** The row, point estimate, endpoints, and companion RR/P values were found and containment reproduced. Bootstrap output and authoritative contrast-direction information are absent.

**Quality-control relevance:** The printed point and CI must have a transparent common direction and scale for reliable numerical extraction.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a mismatched point/interval pair into a systematic review or evidence table; no downstream propagation or conclusion change is asserted.

**Human verification steps:** Verify the signed risk-difference CI against the bootstrap output and table-production materials.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

Small preventable reporting defects can matter when a systematic review, meta-analysis, guideline, or data extractor copies a point estimate, confidence interval, or displayed difference. The candidate cards identify the bounded fields that could be copied if a candidate is confirmed. The supplied package does not show that any propagation, conclusion change, or harm occurred.

## Limitations and Missing Definitions

- Authoritative Cox coefficients, standard errors, and model output are absent for C001.
- The source does not state whether percentage-point estimates were calculated from exact fractions, unrounded internal risks, or displayed rounded percentages for C002-C005, C007, and C008.
- Bootstrap resamples, complete CI construction output, and authoritative contrast-direction records are absent for C006, C009, and C010.
- Sample-size simulation code, outcome variance inputs, and Wald covariance/standard-error inputs are absent, preventing exact reconstruction beyond supplied definitions.
- eTable 1 microbial categories are not declared mutually exclusive; they were not summed against the positive-swab total.
- A correction notice refers to earlier cervical-length wording that is not in the supplied package; no correction-specific mismatch was inferred.

## Human Adjudication Checklist

1. Confirm each cited PDF location and printed value against the supplied source.
2. Obtain source analysis output or production materials where the report lacks a calculation or model definition.
3. Decide whether each candidate reflects an intended convention, a production discrepancy, or another documented explanation.
4. Record validity, importance, action, initials, and notes in the five fields on the corresponding card.
5. If an amendment is considered, independently verify the replacement value, interval, label, and all matched occurrences.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

- **Profile:** 1.5.2
- **Package boundary:** Current package root only
- **Direct sources inventoried:** 3
- **Total source units:** 28
- **Fresh-source units:** 28
- **Prior audit evidence reused:** 0 units
- **External browsing:** Not used
- **OCR mode:** CPU-only, native text first; OCR units 0
- **Source hashes before review:** Recorded in `review_1_5_2/source_hashes_before.sha256`.
- **Source hashes after review:** Recomputed in `review_1_5_2/source_hashes_after.sha256`; all three direct-source SHA-256 values are unchanged.
- **Hash status:** UNCHANGED

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| coordinator | root | gpt-5.6-sol | high | CURRENT_SESSION | `review_1_5_2/run_state.md` |
| fresh_source_preprocessing | root/fresh_preprocessing | gpt-5.6-terra | medium | FRESH_SPAWN | `review_1_5_2/source_inventory.md` |
| main_evidence_mapping | root/main_mapping | gpt-5.6-terra | medium | FRESH_SPAWN | `review_1_5_2/extraction/main_quantitative_evidence.md` |
| support_evidence_mapping | root/support_mapping | gpt-5.6-terra | medium | FRESH_SPAWN | `review_1_5_2/extraction/support_quantitative_evidence.md` |
| numeric_checks | root/numeric_checks | gpt-5.6-terra | medium | FRESH_SPAWN | `review_1_5_2/checkers/numeric_consistency.md` |
| cross_source_checks | root/cross_source_checks | gpt-5.6-terra | medium | FRESH_SPAWN | `review_1_5_2/checkers/cross_source_consistency.md` |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | `review_1_5_2/checkers/statistical_pass_1.md` |
| evidence_recheck | root/evidence_recheck | gpt-5.6-sol | high | FRESH_SPAWN | `review_1_5_2/verification/evidence_recheck.md` |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | `review_1_5_2/checkers/statistical_pass_2.md` |
| evidence_quality | root/evidence_quality | gpt-5.6-sol | high | FRESH_SPAWN | `review_1_5_2/quality/evidence_quality_audit.md` |
| report_generation | root/report_generation | gpt-5.6-terra | medium | FRESH_SPAWN | `review_1_5_2/report_generation.md` |

### Reproducibility performance

- **Target basis:** Three supplied PDF sources totaling 28 pages: an 8-page main randomized-trial article, a 16-page protocol with result-relevant definitions, and a 4-page results supplement. All units require fresh native/layout extraction; native text is expected to be usable, but table rendering and complete cross-document/statistical matching create moderate relationship volume. The target is bounded against, and materially below, the 102-page/49.4-minute calibration package.
- **Total source units:** 28
- **Fresh-source units:** 28
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-08-20T16:52:32Z
- **Finished UTC:** 2026-08-20T17:23:48Z
- **Observed elapsed minutes:** 31.3
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

The runtime exposed no authoritative per-response token counts for any of the 11 manifested agents. The zeroes below are known recorded subtotals, not an assertion that model use was zero; therefore total-token count status and complete price remain incomplete. Cached input and cache-write counts are input subsets, and reasoning counts are output subsets; none is added again to total tokens. All monetary values are token-only API-equivalent estimates under the 2026-08-18 local price snapshot, not invoices.

| Model | Input tokens | Cached input tokens | Cache-write tokens | Output tokens | Reasoning tokens | Total tokens | Known token cost (USD) | Estimated complete token cost (USD) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.6-sol | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ |
| gpt-5.6-terra | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ |

Per-agent response-level status is retained in `review_1_5_2/token_usage_ledger.csv`; deterministic model and package rollups are retained in `review_1_5_2/token_usage_summary.md` and `review_1_5_2/token_usage_summary.json`.
