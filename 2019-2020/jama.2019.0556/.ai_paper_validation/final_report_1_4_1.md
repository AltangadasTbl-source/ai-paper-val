# Quantitative Quality-Control Consistency Review: MooDFOOD Trial Package

## Pending Human Adjudication

**All nine observations in this report are Pending Human Adjudication.** They are source-grounded reporting-consistency questions, not findings of study invalidity, misconduct, or a changed clinical conclusion.

## Executive Quality-Control Summary

This complete five-document review registered **9** distinct candidate consistency issues: two numeric/arithmetic, three measure/label/scale, two cross-document numeric, and two statistical-reporting issues. The review covered all **102/102** supplied PDF pages, mapped `N001-N095` and `S001-S054`, and completed both statistical passes. Candidate IDs are `C001-C009`; no candidate count cap was used.

## Package and Reused-Evidence Provenance

The package contains five direct PDFs: DOC-001 main article (11 pages), DOC-002 protocol (60), DOC-003 statistical analysis plan (5), DOC-004 results supplement (25), and DOC-005 data-sharing statement (1). Direct PDFs were the authority for all candidate evidence. Their before-review SHA-256 values were recorded in `review_1_4_1/source_hashes_before.sha256`.

- `jama_bot_2019_oi_190007.pdf`: `74b85a4b77870fda5ff0ce2f8287a2533a11ee81745d4031155f4af2986bd980`
- `joi190007supp1_prod.pdf`: `b8f3980eacaa908929e57fc6aadd4de0e7a5691a4978be0e2fe4b544455858db`
- `joi190007supp2_prod.pdf`: `b14aaebd8fbded6d36e1ca618cc9f51f2c76d50e486a8c18b4fa56fb183bced7`
- `joi190007supp3_prod.pdf`: `eeb826267cc5662b7736f625a226f37bdeb9ce8cfc6d7556d7ef6fdba5b53246`
- `joi190007supp4_prod.pdf`: `207c317e14618cc7fa6c86853e12ef03bebd2dff3676fa2383762ca248688641`

Seventy-two eligible reusable evidence assets were inventoried: 48 usable, 16 partial, 6 stale, 2 duplicate, and none unreadable. Native text covered DOC-001 pp. 1-11 and DOC-004 pp. 1-2 and 16-23; OCR/rendered assets were locator aids only. Legacy candidate, disposition, and final-report material was excluded from scientific discovery.

## Scope, Complete Coverage, and Exclusions

The direct-source page union was complete: DOC-001 11 pages, DOC-002 60, DOC-003 5, DOC-004 25, and DOC-005 1. The initial reusable-derivative gap of 81 pages was repaired by direct mapping in disjoint support shards; it remains an asset limitation, not a scientific-coverage gap. DOC-005 contained no applicable quantitative relationship. No web, external literature, Office file, workbook, CSV, or raw participant data was used.

The review addressed reporting consistency in numbers, denominators, labels, scales, statistics, and matched cross-document statements. It did not conduct a broad design, clinical, novelty, misconduct, or raw-data audit.

## Quantitative and Statistical Relationship Coverage

The unified numeric inventory contains `N001-N095` (95 relationships), including trial flow, baseline tables, event/rate quantities, adherence, outcomes, protocol planning, statistical-plan definitions, and supplement definitions. The statistical inventory contains `S001-S054` (54 relationships). Every S relationship has `PASS_1_COMPLETE` and `PASS_2_COMPLETE` status. Numeric checks, cross-source checks, direct mechanical rechecks, and the final evidence-quality audit conserved exactly `C001-C009`.

## Candidate Index

| ID | Category | Short statement |
|---|---|---|
| C001 | Measure, label, or scale inconsistency | Table 2 footnote repeats the supplements-without-therapy label. |
| C002 | Measure, label, or scale inconsistency | Adherence cutoff is inclusive in definitions but strict in Results prose. |
| C003 | Measure, label, or scale inconsistency | eAppendix 8 footnote markers point to unrelated rows. |
| C004 | Statistical reporting inconsistency | eAppendix 10 prints `p=0`. |
| C005 | Numeric or arithmetic inconsistency | Main sample-size total conflicts with four stated cell counts. |
| C006 | Numeric or arithmetic inconsistency | Protocol calls 30% versus 15% a 25% difference. |
| C007 | Cross-document numeric inconsistency | Protocol and publication give different sample-size inputs. |
| C008 | Measure, label, or scale inconsistency | Protocol names DSM-IV and DSM-5 for the same endpoint. |
| C009 | Statistical reporting inconsistency | Analysis-plan threshold lacks a comparison operator. |

## Candidate Evidence Cards

## C001 — Table 2 footnote duplicates the supplements-without-therapy label

**Candidate statement:** Table 2 footnote d assigns both event components to supplements without therapy, although the second component is elsewhere identified as supplements with therapy.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-001 Table 2 — PDF p. 6](<../jama_bot_2019_oi_190007.pdf#page=6>); [Figure 1 — PDF p. 3](<../jama_bot_2019_oi_190007.pdf#page=3>); [Results — PDF p. 7](<../jama_bot_2019_oi_190007.pdf#page=7>).

**Source evidence:** Footnote d prints 32/256 (12.5%) and 22/256 (8.6%) both as “supplements without therapy.” Footnote f and Results identify 22/256 (8.6%) as supplements with therapy.

**Reported-versus-comparator:** Repeated “without therapy” versus the Figure 1 allocation/Results and footnote-f “with therapy” label for 22/256.

**Reasoning procedure:** Match the two components to the mutually exclusive 2x2 supplement strata.

**Calculation:** 32+22=54 events and 256+256=512; 22/256=8.59375%, rounded 8.6%. The other partition is 25+32=57 without therapy and 26+22=48 with therapy.

**Alternative source-grounded interpretations:** Counts, percentages, total, OR, CI, and P value reconcile; the problem may be confined to one footnote label.

**Mechanical evidence recheck:** Direct PDF text extraction and page rendering found all locations and printed wording. Inputs reproduce the label mismatch; missing are the production proof and original four-cell source labels.

**Quality-control relevance:** A four-cell treatment label is needed to interpret the event components of a factorial result.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy the wrong therapy-stratum label while retaining the correct event count.

**Human verification steps:** Inspect the production table/proof and original analysis labels; confirm whether the second phrase should be “with therapy.”

**Human adjudication fields:**

- Validity: __
- Importance: __
- Action: __
- Initials: __
- Notes: __

## C002 — Supplement-adherence cutoff changes from inclusive to strict wording

**Candidate statement:** The predefined and supplement cutoff is `>=70%`, whereas Results describes adherence as “more than 70%.”

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-001 Methods — PDF p. 4](<../jama_bot_2019_oi_190007.pdf#page=4>); [Results — PDF p. 6](<../jama_bot_2019_oi_190007.pdf#page=6>); [DOC-004 eAppendix 8 — PDF p. 16](<../joi190007supp3_prod.pdf#page=16>); [eAppendix 12 — PDF p. 22](<../joi190007supp3_prod.pdf#page=22>).

**Source evidence:** Methods/eAppendices print `>=70%`; Results says 77% had adherence “more than 70%.”

**Reported-versus-comparator:** Strict `>70%` prose versus inclusive `>=70%` operational/table wording.

**Reasoning procedure:** Compare whether equality at the stated 70% boundary is included.

**Calculation:** eAppendix 8 pill-weight multinutrient counts are 135+134+126+120=515; 515/666=77.3%, compatible with the rounded 77%. `>=70%` includes exactly 70%; `>70%` does not.

**Alternative source-grounded interpretations:** Results may use informal prose for the inclusive criterion and no participant may lie exactly at 70%.

**Mechanical evidence recheck:** Direct pages confirm the wording and counts. Missing are boundary-level adherence values, the selected pill component, operational code/data dictionary, and an unrounded Results numerator/denominator.

**Quality-control relevance:** Cutoff wording can alter an adherence numerator at the boundary.

**Potential downstream evidence impact:** If confirmed, an evidence user could apply a different adherence definition when extracting a per-protocol/CACE-related quantity.

**Human verification steps:** Identify the operational cutoff and component behind 77%; count observations equal to 70%.

**Human adjudication fields:**

- Validity: __
- Importance: __
- Action: __
- Initials: __
- Notes: __

## C003 — eAppendix 8 footnote markers point to unrelated adherence rows

**Candidate statement:** Visible asterisks attach to four adherence rows but the corresponding note defines Morisky score; the Morisky row is unmarked and the kappa note has no visible double-marker target.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-004 eAppendix 8 — PDF p. 16](<../joi190007supp3_prod.pdf#page=16>).

**Source evidence:** Four `>=70%` rows carry `*`; the `*` note defines average Morisky score. The Morisky row has no marker. The `**` note gives kappas 0.73/0.70 but no row visibly carries `**`.

**Reported-versus-comparator:** Marker placements versus the content and apparent targets of the two notes.

**Reasoning procedure:** Treat each marker as a required row-to-note cross-reference.

**Calculation:** Logical reproduction: four visible `*` targets map to the sole Morisky note; zero visible `**` targets map to the kappa note; no arithmetic applies.

**Alternative source-grounded interpretations:** Production may have shifted markers; the intended corrected arrangement cannot be determined from the PDF.

**Mechanical evidence recheck:** Direct page rendering confirms all markers and notes. Missing are the editable table, proof, and author correction record.

**Quality-control relevance:** Footnotes qualify the meaning and provenance of adherence statistics.

**Potential downstream evidence impact:** If confirmed, an extractor could associate Morisky or agreement information with the wrong adherence rows.

**Human verification steps:** Inspect the production source to identify intended `*` and `**` row assignments.

**Human adjudication fields:**

- Validity: __
- Importance: __
- Action: __
- Initials: __
- Notes: __

## C004 — eAppendix 10 prints a literal P value of zero

**Candidate statement:** The baseline GAD-7 row displays `p=0` without threshold notation or a rounding convention.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [DOC-004 eAppendix 10B — PDF p. 19](<../joi190007supp3_prod.pdf#page=19>).

**Source evidence:** The row prints B=0.464, 95% CI 0.409 to 0.52, and `p=0`.

**Reported-versus-comparator:** Literal zero P field versus the row’s positive coefficient/wholly positive interval; no independent exact P occurrence is supplied.

**Reasoning procedure:** Check the reported P display and use the rounded interval only as a labelled diagnostic, not an exact recalculation.

**Calculation:** Diagnostic only: SE approximately (0.520-0.409)/(2x1.96)=0.0283; z approximately 0.464/0.0283=16.4, consistent with a very small positive two-sided tail probability, not an exact recovered P value.

**Alternative source-grounded interpretations:** `0` may be fixed-precision software/export rendering of a very small positive P value.

**Mechanical evidence recheck:** Direct rendering confirms the literal `0`. Missing are unrounded B/CI/P, SE/test statistic, degrees of freedom, interval/test method, covariance estimator, and display convention.

**Quality-control relevance:** P-value display should distinguish an exact value from a thresholded small value.

**Potential downstream evidence impact:** If confirmed, a systematic reviewer or meta-analyst could copy `P=0` as an exact statistic.

**Human verification steps:** Retrieve unrounded output and the journal/software P-value display rule.

**Human adjudication fields:**

- Validity: __
- Importance: __
- Action: __
- Initials: __
- Notes: __

## C005 — Main-article sample-size total conflicts with four stated cell counts

**Candidate statement:** The article says 392 participants were needed while parenthetically stating 196 in each of four combinations.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [DOC-001 Sample Size — PDF p. 4](<../jama_bot_2019_oi_190007.pdf#page=4>).

**Source evidence:** It prints “392 participants (196 in each of the 4 possible intervention combinations)” and then 22% attrition with 250 per intervention combination.

**Reported-versus-comparator:** Reported total 392 versus four stated cells of 196; later four cells of 250 provide an internal comparator.

**Reasoning procedure:** Sum the stated mutually exclusive combination cells.

**Calculation:** 4x196=784, not 392; 392/196=2. Conversely, 4x250=1000, consistent with the later per-combination statement.

**Alternative source-grounded interpretations:** 392 may be a marginal two-level factorial contrast (196+196), although the sentence says 196 in each of four combinations.

**Mechanical evidence recheck:** Direct page confirms the complete statement. Missing are the power-calculation output/formula, allocation unit for 196/392, and production manuscript.

**Quality-control relevance:** Sample-size units affect interpretation of planned power and factorial allocation.

**Potential downstream evidence impact:** If confirmed, a trial reviewer could copy an incorrect planned total or per-cell sample size.

**Human verification steps:** Obtain the calculation/output and identify whether 392 is marginal or total; clarify the printed phrase/number.

**Human adjudication fields:**

- Validity: __
- Importance: __
- Action: __
- Initials: __
- Notes: __

## C006 — Protocol calls a 30% versus 15% contrast a 25% difference

**Candidate statement:** The protocol’s stated 25% difference does not reconcile with its displayed 30% control and 15% intervention incidences under ordinary absolute or relative metrics.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [DOC-002 Sample Size — PDF p. 16](<../joi190007supp1_prod.pdf#page=16>).

**Source evidence:** The protocol prints “difference of 25%,” followed by 30% control and 15% intervention one-year incidence.

**Reported-versus-comparator:** 25% wording versus the two printed incidences.

**Reasoning procedure:** Compute absolute percentage-point and control-relative differences.

**Calculation:** 30%-15%=15 percentage points; (30%-15%)/30%=50%; risk ratio=15%/30%=0.50. None equals 25%.

**Alternative source-grounded interpretations:** The 25% may refer to an unstated calculation parameter or drafting carryover.

**Mechanical evidence recheck:** Direct page confirms all three values. Missing are the metric definition, calculation parameterization/output, and amendment/draft history.

**Quality-control relevance:** Event-rate assumptions determine a power calculation’s documented meaning.

**Potential downstream evidence impact:** If confirmed, a protocol reviewer could extract the wrong assumed effect size.

**Human verification steps:** Retrieve the power calculation and define what “25%” was intended to represent.

**Human adjudication fields:**

- Validity: __
- Importance: __
- Action: __
- Initials: __
- Notes: __

## C007 — Protocol and publication state different sample-size assumptions

**Candidate statement:** Matched enrollment-planning passages report different active event rates, uninflated sample quantities, and attrition assumptions.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-001 Sample Size — PDF p. 4](<../jama_bot_2019_oi_190007.pdf#page=4>); [DOC-002 Sample Size — PDF p. 16](<../joi190007supp1_prod.pdf#page=16>); [DOC-002 continuation — PDF p. 17](<../joi190007supp1_prod.pdf#page=17>).

**Source evidence:** Publication: 30% versus 20%, 33% reduction, 196 stated per combination, 22% attrition, 250 per combination. Protocol: 30% versus 15%, 180 per group, 20% dropout, 250 per arm.

**Reported-versus-comparator:** Same one-year factorial trial’s publication planning inputs versus protocol planning inputs.

**Reasoning procedure:** Match trial/design/time frame, then compare effect-rate, pre-attrition, and attrition quantities.

**Calculation:** Protocol contrast: 15 percentage points/50% relative reduction. Publication: 10 points/33.3% relative reduction. Attrition differs by 2 points; both final targets imply 4x250=1000.

**Alternative source-grounded interpretations:** Protocol version 7 may reflect another planning stage or a legitimate amendment; the compared pages do not document the transition.

**Mechanical evidence recheck:** Direct pages confirm both passages. Missing are original calculation files, dated amendments/change history, plan provenance, and the assumptions that governed enrollment.

**Quality-control relevance:** Cross-document planning assumptions should be traceable when the same trial is described.

**Potential downstream evidence impact:** If confirmed, a reviewer could record inconsistent anticipated event rates or power assumptions.

**Human verification steps:** Locate dated amendments/recalculations and identify the final operative assumptions.

**Human adjudication fields:**

- Validity: __
- Importance: __
- Action: __
- Initials: __
- Notes: __

## C008 — Protocol uses incompatible DSM editions for the primary endpoint

**Candidate statement:** The protocol names DSM-IV and DSM-5 for the same MINI-assessed 12-month MDD endpoint and schedule.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-002 endpoint summary — PDF p. 8](<../joi190007supp1_prod.pdf#page=8>); [DOC-002 Methods 8.1.1 — PDF p. 28](<../joi190007supp1_prod.pdf#page=28>); [DOC-001 Primary Outcome — PDF p. 4](<../jama_bot_2019_oi_190007.pdf#page=4>).

**Source evidence:** Protocol p. 8 prints DSM-IV/MINI; p. 28 prints DSM-5/MINI V5.01, both with baseline, 3-, 6-, and 12-month assessment. The article identifies DSM-IV/MINI 5.0.

**Reported-versus-comparator:** DSM-IV endpoint label versus DSM-5 label for matching endpoint/schedule.

**Reasoning procedure:** Compare diagnostic-edition labels after matching endpoint, MINI family, and time schedule.

**Calculation:** Logical comparison only: DSM-IV and DSM-5 are distinct labels; no arithmetic applies.

**Alternative source-grounded interpretations:** An unrevised section may remain, or the label difference may not have altered the operational MINI assessment.

**Mechanical evidence recheck:** Direct pages confirm both labels. Missing are administered MINI forms/modules, scoring algorithm, operative case-definition manual, training/data dictionary, amendment history, and classification-impact evidence.

**Quality-control relevance:** The diagnostic standard labels the primary endpoint’s measurement definition.

**Potential downstream evidence impact:** If confirmed, an evidence synthesis could record an inconsistent diagnostic standard for the endpoint.

**Human verification steps:** Confirm the operative diagnostic edition and whether any version transition changed assessment/classification.

**Human adjudication fields:**

- Validity: __
- Importance: __
- Action: __
- Initials: __
- Notes: __

## C009 — Analysis-plan significance threshold lacks a comparison operator

**Candidate statement:** The statistical analysis plan prints `p 0.05` for the two-sided significance threshold without an operator.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [DOC-003 statistical analysis plan — PDF p. 3](<../joi190007supp2_prod.pdf#page=3>); [local interaction rule — PDF p. 5](<../joi190007supp2_prod.pdf#page=5>).

**Source evidence:** The global sentence is `the 2-sided significance threshold will be set at p 0.05`. A p. 5 local modifier rule separately prints `p<0.05`.

**Reported-versus-comparator:** Operator-free global threshold versus the locally explicit `<` comparison.

**Reasoning procedure:** A threshold must specify the relation that classifies P values.

**Calculation:** The p. 3 syntax cannot classify 0.049, 0.050, or 0.051. Under p. 5’s local `p<0.05`, 0.049 meets that local rule; this comparator does not correct p. 3.

**Alternative source-grounded interpretations:** A less-than glyph may have been lost in production; it renders elsewhere in the same plan.

**Mechanical evidence recheck:** Direct PDF text and rendering confirm no operator on p. 3. Missing are the editable plan, conversion history, global equality rule, and confirmation that p. 5 applies globally.

**Quality-control relevance:** An operator is essential for a reproducible stated significance convention.

**Potential downstream evidence impact:** If confirmed, a reviewer could be unable to determine the plan’s exact significance rule.

**Human verification steps:** Inspect the original SAP/source file and confirm whether the intended convention was `P<.05`, `P<=.05`, or another rule.

**Human adjudication fields:**

- Validity: __
- Importance: __
- Action: __
- Initials: __
- Notes: __

## Downstream Evidence-Chain Considerations

If confirmed, these issues could affect copied treatment labels, adherence definitions, table-note interpretation, P-value notation, planned sample-size inputs, or endpoint diagnostic labels. Such effects are bounded to potential reuse in data extraction, systematic reviews, meta-analyses, or guidance work; this review does not establish that any propagation occurred or that any study conclusion changed.

## Limitations and Missing Definitions

Direct PDF confirmation was available for every candidate, but individual-level data, unrounded analysis output, source-table proofs, original power calculations, amendment histories, and some model/test details were not supplied. Therefore, the review does not determine boundary classifications for C002, an exact P value for C004, intended production corrections for C001/C003/C009, the operative power assumptions for C005-C007, or the operative DSM assessment definition for C008. OCR confidence/provenance metadata was incomplete and was not treated as final evidence. No structured-table, workbook, CSV, or figure-data asset was supplied.

## Human Adjudication Checklist

- Review each card’s direct PDF evidence and its named missing inputs.
- Determine validity, importance, action, initials, and notes for each C001-C009 card.
- Preserve the distinction between printed observation, derived comparison, and possible explanation.
- If a correction is contemplated, verify it against the production source, original analysis output, protocol/SAP revision history, or data dictionary as appropriate.

## Reproducibility, Source-Integrity, and Performance Metadata

- **Review profile:** 1.4.1; reusable evidence assets with restarted candidate discovery.
- **Direct source scope:** 5 PDFs, 102/102 pages.
- **Reusable assets before review:** 72; source and reused-artifact before-hash manifests retained in `review_1_4_1/`.
- **Target elapsed minutes:** 20-25
- **Started UTC:** 2026-08-18T06:09:33Z
- **Finished UTC:** 2026-08-18T06:58:55Z
- **Observed elapsed minutes:** 49.4
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Final quality-audit repair required direct mapping of 81 pages without reusable extraction; runtime-profile repair reran both statistical passes at explicit Terra high effort; expanded coverage increased the relationship set to 95 numeric and 54 statistical units and the candidate set to 9.

The coordinator must finalize the timing fields immediately after Markdown assembly, recompute source and reused-asset hashes, render standalone HTML once, and run the profile validator.
