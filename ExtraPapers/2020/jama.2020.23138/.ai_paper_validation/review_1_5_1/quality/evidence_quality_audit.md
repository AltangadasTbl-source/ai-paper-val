# Evidence Quality Audit

This is a neutral quantitative quality-control audit. It preserves every stable candidate and makes no scientific disposition. All 14 candidates remain Pending Human Adjudication.

## Audit status

- **Stable candidate coverage:** C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, and C014 are present in both `candidate_ledger.md` and `verification/evidence_recheck.md`; the sets are identical at 14/14.
- **Direct-source coverage:** five of five direct-source rows are closed at the unit level. The totals are 147 PDF pages, partitioned into 32 reusable units and 115 fresh-required units, with 147 mapped units. Every row satisfies reusable plus fresh-required equals total, mapped equals total, and `COMPLETE` status.
- **Mapping and relationship coverage:** the durable mapping parts cover DOC-001 pages 1-12, DOC-002 pages 1-69, DOC-003 pages 1-45, DOC-004 pages 1-20, and DOC-005 page 1. The canonical inventories contain 125 unique N relationships and 90 unique S relationships. The numeric checker states 125/125 coverage; both statistical tables contain 90 unique per-relationship completion rows matching the 90-ID inventory.
- **Statistical execution:** pass 1 is `/root/statistical_pass_1` and pass 2 is `/root/statistical_pass_2`. They are distinct runtime IDs, each recorded as a fresh `gpt-5.6-terra` agent at high reasoning effort. Each pass covers all 90 S IDs. Pass 2 revisits the complete C001-C014 ledger and the evidence recheck.
- **Count-boundary audit:** the current evidence inventory expressly excludes legacy candidate, queue, checker, verifier, critic, and report content from discovery. The complete 147-page source map, 215-relationship checker scope, 14-ID ledger, and explicit no-limit statements provide durable evidence that neither an old ten-candidate list nor a top-N boundary controlled current discovery.
- **Display-zero rule:** no candidate mentions `P = 0`, `p = 0.000`, or equivalent. Both statistical passes report zero such displays and distinguish `P < .001` threshold notation from a display zero. No conditional independent-contradiction field is required for C001-C014.
- **Integrity and links:** all five current direct-source hashes and all 157 current reused-artifact hashes match their before-review ledgers. Every PDF link in the evidence recheck resolves to an existing local PDF and a page within that PDF. Protocol page 15 resolves as a page but contains no C007 evidence and must not be treated as an evidence location.
- **Coverage-manifest state:** all 26 data rows contain exactly one plain relative artifact path. Twenty-four rows are `COMPLETE`. The `evidence_quality` and `report_generation` rows remain placeholder `PENDING` rows and prevent final report-readiness until the coordinator repairs them.

The source and relationship work is complete. Report generation is ready only after the coordinator repairs the manifest and applies the candidate-specific wording constraints below.

## Evidence-card field audit rule

For every candidate below, the ledger supplies a heading, category, source locations, printed evidence, a consistency rule, an alternative interpretation, checker provenance, and a human question. It is not yet a final report card. Unless a candidate section below says otherwise, each final card still needs the following exact report fields assembled from the ledger and recheck: `Candidate statement`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. The existing `Category` and `Exact source locations` content must be retained under the exact required labels. A non-arithmetic label comparison must receive an explicit `Calculation` entry stating that no arithmetic is required and giving the reproducible identity, membership, or direction comparison.

Every final human-adjudication block must be exactly:

```markdown
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
```

No human-adjudication subfield exists yet because the final report has not been assembled. Therefore placeholder compliance is a required report-generation check, not a completed report check at this audit stage.

## C001 — Randomized total differs between the flow diagram and article population

- **Support and arithmetic:** Main PDF page 3 directly prints 551 assessed, 390 excluded, 161 randomized, two arm boxes of 80 randomized, and a footnote describing one withdrawal after randomization before treatment. Page 4 directly supplies the replacement mechanism. The calculations `551 - 390 = 161`, `80 + 80 = 160`, and `161 - 1 = 160` are correct.
- **Weakened-support constraint:** the card must not say that the package provides no reconciliation. The source supports a distinction between 161 initial allocation events and a replacement-maintained cohort of 160 treated participants, but the figure does not explicitly label that distinction in its branch structure. Do not infer an intention-to-treat defect, an unexplained missing participant, or a paper-conclusion effect.
- **Assumptions and duplicate review:** the only unresolved premise is whether the same word `randomized` is intended for both population counts. This is not a duplicate of the sample-size planning relationships, which reconcile at 160 after attrition allowance.
- **Pagination and fields:** pages 1, 3, and 4 are truthful. The final card needs every missing field listed in the common field audit, with the mechanical recheck reflecting the replacement explanation.
- **Bounded relevance:** if the human question confirms a labeling problem, an extractor could copy 160 or 161 as the randomized denominator. No downstream propagation or conclusion change is established.
- **Exact remaining human question:** Is Figure 1 intended to distinguish 161 total allocation events from the replacement-maintained cohort of 160 treated participants, and should its branch structure or the abstract's population wording explicitly name that distinction?

## C002 — Baseline digoxin NT-proBNP summaries differ between main Tables 1 and 3

- **Support and arithmetic:** Table 1 and the narrative print 1095 with IQR 715-1527 pg/mL; Table 3 prints 1091 with IQR 710-1522 pg/mL for baseline digoxin with displayed n=80. The median difference is 4 pg/mL and both endpoint differences are 5 pg/mL.
- **Assumptions and alternatives:** the comparison assumes the same 80 observations and the same median/IQR convention. Participant-level data, quartile convention, data-freeze history, and hidden complete-case rules are absent; a distinct data version or convention remains possible.
- **Duplicate, pagination, and impact review:** this is distinct from C007's analyte-label comparison and C010's time-heading comparison. Pages 5, 6, and 7 are truthful. Do not imply that the 12-month treatment effect is inconsistent. The final card needs every common missing field.
- **Bounded relevance:** if confirmed, an extractor could copy either baseline NT-proBNP triple; no effect on the paper's conclusions is established.
- **Exact remaining human question:** Do Tables 1 and 3 use the same 80 baseline digoxin measurements and the same median/IQR convention, and, if so, which printed triple is intended?

## C003 — Baseline digoxin 12-lead ECG heart-rate mean differs between main Table 1 and eTable 2

- **Support and arithmetic:** the matched cells print 100.1 (16.8) and 100.3 (16.8) beats/min with n=80; `100.3 - 100.1 = 0.2` beats/min. Main Table 3 independently repeats 100.3 (16.8).
- **Assumptions and alternatives:** the comparison assumes a common participant set, ECG processing rule, and table version. Those production inputs are not supplied. The card must present a repeated-cell question, not an error mechanism.
- **Duplicate, pagination, and impact review:** C003, C004, and C005 share table locations but concern different printed cells and calculations; they remain separate relationships. Main page 5 and results-supplement page 14 are truthful. The final card needs every common missing field.
- **Bounded relevance:** if confirmed, an extractor could copy either one-decimal baseline ECG mean. No adjusted-effect or conclusion change is established.
- **Exact remaining human question:** Are these cells intended to summarize the same 80 baseline 12-lead ECG measurements, and which one-decimal mean corresponds to the intended dataset and processing rule?

## C004 — Baseline digoxin apical heart-rate mean differs between main Table 1 and eTable 2

- **Support and arithmetic:** the matched 30-second apical cells print 98.2 (15.1) and 98.3 (15.1) beats/min with n=80; the displayed difference is 0.1 beats/min.
- **Assumptions and alternatives:** the comparison requires the same participant set, assessment, source statistic, and rounding rule. At a half-tenth boundary, independently prepared tables could differ under different tie-breaking or source versions; that possibility does not erase the printed mismatch but prevents claiming a known production error.
- **Duplicate, pagination, and impact review:** this cell is distinct from C003 and C005. Main page 5 and results-supplement page 14 are truthful. The final card needs every common missing field.
- **Bounded relevance:** if confirmed, an extractor could copy either apical mean. No treatment-effect or paper-conclusion impact is established.
- **Exact remaining human question:** Are both cells derived from the same 80 baseline 30-second apical measurements, and which displayed mean is intended under the analysis dataset and rounding rule?

## C005 — Baseline digoxin radial-pulse SD differs between main Table 1 and eTable 2

- **Support and arithmetic:** both cells print mean 87.8 beats/min with n=80, while the SDs are 12.1 and 12.0; the displayed SD difference is 0.1 beats/min.
- **Assumptions and alternatives:** the comparison requires the same observations, SD convention, and rounding rule. Sample-versus-population SD, data-version, inclusion, and tie-breaking details are not supplied. Do not identify one value as the correction.
- **Duplicate, pagination, and impact review:** this is a separate SD relationship from the C003 and C004 mean relationships. Main page 5 and results-supplement page 14 are truthful. The final card needs every common missing field.
- **Bounded relevance:** if confirmed, an extractor could copy either radial-pulse SD. No adjusted-effect or conclusion change is established.
- **Exact remaining human question:** Should both cells use the same participant set and SD convention, and, if so, is the intended radial-pulse SD 12.0 or 12.1 beats/min?

## C006 — Protocol assigns both PCS and physical-functioning labels to the primary endpoint

- **Support and rule:** protocol pages 14, 22, and 54 name PCS; pages 21 and 56 name physical functioning. The SAP and article identify PCS as primary, while the article separately reports physical functioning. The reproducible rule is measure-label identity; no arithmetic is required.
- **Assumptions and alternatives:** a drafting carryover or later supersession is plausible, but no amendment history establishes it. The card must not claim that the realized PCS analysis used the wrong outcome.
- **Duplicate, pagination, and impact review:** all cited pages are truthful. C006 concerns primary-endpoint identity and is distinct from the other scale-label candidates. The final card needs every common missing field.
- **Bounded relevance:** if confirmed, an extractor could classify the primary endpoint as PCS or as the physical-functioning domain. No change to the reported PCS estimate or paper conclusion is established.
- **Exact remaining human question:** Was six-month PCS the intended primary endpoint throughout, and should protocol pages 21 and 56 be amended or annotated to distinguish physical functioning from PCS?

## C007 — Protocol outcome wording says BNP while assay and results say NT-proBNP

- **Support and rule:** protocol pages 14, 22, and 54 use BNP; page 41 specifies an NT-proBNP assay; the SAP row and reported result use NT-proBNP. The package supplies no statement making the analyte labels interchangeable. No numeric conversion is the candidate rule.
- **Pagination repair:** protocol page 15 exists but contains no BNP or NT-proBNP evidence. The current ledger correctly omits it. The recheck retains page 15 only as a transparent repair notice; the final card must omit page 15 from `Exact source locations` and must not use it as evidence.
- **Assumptions and alternatives:** informal family shorthand is possible but not declared. Do not claim a measured-value conversion problem.
- **Duplicate and impact review:** this analyte-identity relationship is distinct from C002's repeated baseline values and C010's time heading. The final card needs every common missing field.
- **Bounded relevance:** if confirmed, an extractor could classify the biomarker as BNP instead of NT-proBNP. No numeric result or paper-conclusion change is established.
- **Exact remaining human question:** Was NT-proBNP the intended biomarker outcome throughout, and should the protocol outcome lists be standardized to that analyte?

## C008 — SAP AFEQT template footnote calls the scale a visual-analogue score

- **Support and rule:** the SAP defines AFEQT overall score and visibly attaches a `visual analogue score` range footnote to the AFEQT table, while the preceding table concerns EQ-5D VAS. Equal 0-100 ranges do not establish measure identity. No arithmetic is required.
- **Assumptions and alternatives:** copy-forward from the preceding template is plausible but not stated. The card must not imply that any populated AFEQT result was numerically calculated as VAS.
- **Duplicate, pagination, and impact review:** SAP pages 17, 19, and 36, main page 7, and results-supplement page 16 are truthful. This is distinct from C013's heart-rate/QoL footnote. The final card needs every common missing field.
- **Bounded relevance:** if confirmed, an extractor could mislabel AFEQT as a visual-analogue measure. No paper-conclusion effect is established.
- **Exact remaining human question:** Should the AFEQT footnote identify the AFEQT overall-score anchors rather than call it a visual analogue score?

## C009 — SAP reverses the favorable direction for E/e-prime

- **Support and rule:** SAP page 20 states lower E/e-prime is better; the page-37 E/e-prime template states higher values and a positive difference favor digoxin. These are opposite direction rules for the same signed contrast. The reported estimate of -0.1 with interval -1.1 to 0.9 is internally coherent and is context, not an arithmetic contradiction.
- **Assumptions and alternatives:** copied higher-is-better boilerplate is plausible but not declared. Do not infer a reversed fitted model or a changed conclusion.
- **Possible overlap:** C009 and C014 both concern E/e-prime direction, but they compare different printed statements: C009 is the SAP page-20 versus page-37 conflict; C014 is the main Table 3 universal footnote applied to lower-is-better rows. Preserve both IDs and make the distinct comparators explicit.
- **Pagination and impact review:** SAP pages 20 and 37 and main page 7 are truthful. The final card needs every common missing field.
- **Bounded relevance:** if confirmed, an extractor could reverse the favorable-direction coding for the E/e-prime contrast. No observed reversal or conclusion change is established.
- **Exact remaining human question:** Should the page-37 E/e-prime direction sentence say that lower values and a negative digoxin-minus-bisoprolol difference indicate the favorable direction?

## C010 — SAP NT-proBNP heading says six months but its table includes a 12-month row

- **Support and rule:** SAP page 40 is headed `at 6 months` but displays baseline, 6-month, and 12-month rows; page 21 plans both follow-ups and the article reports a 12-month result. The set named by the heading omits a displayed follow-up. No arithmetic is required.
- **Compound-card repair:** pg/mL and ng/L are factor-1 equivalent mass-concentration units and do not supply an independent contradiction. The final card must center only the time-heading mismatch. Unit equivalence may appear as non-candidate context, but the human question and relevance must not turn optional unit standardization into a second finding.
- **Assumptions and alternatives:** an unrevised template heading is plausible but not stated. Do not claim that the 12-month result was unplanned or omitted from analysis.
- **Duplicate, pagination, and impact review:** SAP pages 17, 21, and 40 and main page 7 are truthful. C010 is distinct from C002 and C007. The final card needs every common missing field.
- **Bounded relevance:** if confirmed, an extractor could miss or misclassify the planned 12-month NT-proBNP row. No numeric effect or paper-conclusion change is established.
- **Exact remaining human question:** Should the page-40 table heading name both the 6- and 12-month NT-proBNP analyses?

## C011 — SAP EHRA example uses an undefined class 3a

- **Support and rule:** SAP page 18 defines `{1, 2a, 2b, 3, 4}` and then uses `3a` in an example. The set-membership comparison `3a` is not in the printed set is reproducible. Reading `3a` as `3` yields the stated two-category movement through `2b` to `2a`, but that is an inferred explanation.
- **Assumptions and alternatives:** a typographic substitution for class 3 is plausible but not established. Do not imply that a realized participant result used class 3a.
- **Duplicate, pagination, and impact review:** SAP page 18 is truthful. This scale-category example is distinct from the realized EHRA inferential relationships, which the statistical passes found internally coherent. The final card needs every common missing field.
- **Bounded relevance:** if confirmed, an implementer could copy an undefined EHRA category into the binary-improvement rule. No reported-result or conclusion change is established.
- **Exact remaining human question:** Was the example intended to say baseline EHRA class 3, and should `3a` be changed accordingly?

## C012 — SAP ambulatory-HR template uses monitor duration where the visit time point is expected

- **Corrected direct observation:** direct visual recheck of SAP page 38 shows `24-hour` in the ambulatory row's `Time point` cell. The row is not under `Baseline`; the nearby baseline cell belongs to the separate 12-lead ECG section. SAP page 20 states that the ambulatory measure is collected once with no baseline score, and results-supplement page 9 labels it end uptitration.
- **Weakened-support constraint:** the only remaining question is whether `24-hour` describes monitor duration where the visit label should identify end uptitration. The source may intentionally use duration in that column while leaving visit timing implicit. The card must not repeat the numeric checker's false baseline-placement premise or claim a known timing error.
- **Assumptions and alternatives:** interpreting the column as a visit-time field and `24-hour` as duration is a reasoned reading of the heading and outcome name, not a direct declaration by the SAP. No arithmetic is required.
- **Duplicate, pagination, and impact review:** SAP pages 20 and 38 and results-supplement page 9 are truthful. C012 is not a duplicate of the internally coherent adjusted 24-hour heart-rate result. The final card needs every common missing field and must use the corrected heading shown here.
- **Bounded relevance:** if confirmed, an extractor could label monitor duration as the assessment visit or omit the end-uptitration visit. No numerical or paper-conclusion effect is established.
- **Exact remaining human question:** Should the SAP page-38 `Time point` cell identify the end-uptitration visit rather than repeat the 24-hour monitor duration?

## C013 — Results-supplement heart-rate table describes higher values as better quality of life

- **Support and rule:** results-supplement page 14 is a beats/min heart-rate table whose footnote says higher values represent better quality of life. The same clause appears on an actual AFEQT quality-of-life table on page 16. A heart-rate unit is not a QoL scale under any supplied definition. No arithmetic is required.
- **Assumptions and alternatives:** copied footnote text is plausible but not stated. The candidate concerns the measure label; it must not assert that a higher heart rate is clinically worse or that any heart-rate effect was interpreted incorrectly in the narrative.
- **Duplicate, pagination, and impact review:** results-supplement page 14 and main pages 4 and 6 are truthful; page 16 is truthful corroborating context if used. C013 is distinct from the three baseline heart-rate cell differences. The final card needs every common missing field.
- **Bounded relevance:** if confirmed, an extractor could misclassify a heart-rate contrast as a quality-of-life interpretation. No paper-conclusion effect is established.
- **Exact remaining human question:** Should the quality-of-life clause be removed from eTable 2 or replaced with a heart-rate-specific explanation of the adjusted contrast direction?

## C014 — Main Table 3 uses a universal higher-is-better footnote for lower-is-better measures

- **Support and calculation:** main Table 3 applies an unqualified higher-is-better footnote while including NYHA score and E/e-prime. The narrative describes lower NYHA as favorable, and the SAP says lower E/e-prime is better. The displayed NYHA means give `1.5 - 2.0 = -0.5`, which is directionally consistent with the adjusted -0.6; the difference between -0.5 and -0.6 is not a candidate because the latter is adjusted.
- **Assumptions and alternatives:** the footnote may have been intended only for applicable higher-is-better outcomes, but the source does not delimit it. Do not claim that every Table 3 row is directionally reversed or that the fitted results are wrong.
- **Possible overlap:** retain C014 separately from C009. C014 tests the scope of the main-table footnote across NYHA and E/e-prime; C009 tests two opposed SAP statements for E/e-prime.
- **Pagination and impact review:** main pages 6 and 7 and SAP page 20 are truthful. The final card needs every common missing field.
- **Bounded relevance:** if confirmed, an extractor could assign the wrong favorable direction to lower-is-better rows. No conclusion change is established.
- **Exact remaining human question:** Should Table 3 limit the higher-is-better statement to applicable outcomes and explicitly state lower-is-better exceptions for NYHA class and E/e-prime?

## Coordinator repairs required before report generation

1. Replace the `coverage_manifest.md` `evidence_quality` placeholder scope with the explicit C001-C014 list, retain `quality/evidence_quality_audit.md` as its single artifact path, and set the row to `COMPLETE`.
2. Replace the `report_generation` placeholder scope with the explicit C001-C014 list. Set it to `COMPLETE` only after the complete Markdown report exists and contains all 14 cards. Keep exactly one artifact path in the row.
3. Update the final sentence of `source_coverage.md`. Its current statement says mapped means only a downstream assignment and does not claim scientific relationship mapping. The completed extraction and relationship artifacts now support actual mapping of all 147 units; the final coverage ledger should state that closure rather than preserve an initialization-stage disclaimer.
4. Generate every report card with all exact labels required by `report_spec.md`, use one complete local PDF link ending in `#page=N` for every cited page, and use the exact five `__` human-adjudication placeholders. Omit protocol page 15 from C007 evidence.
5. Use the direct recheck as authority over the two stale numeric-checker premises: C001 has a printed replacement explanation, and C012 is not placed under Baseline. Preserve the stable IDs while using only the narrowed source-grounded questions in this audit. Keep C010 centered on its time-heading mismatch rather than treating equivalent units as a second candidate.
6. Keep C009 and C014 separate and explain their distinct printed comparators. Keep C003-C005 separate as different table cells. Do not merge, delete, renumber, rank, or suppress any stable ID.
7. Bound every downstream statement to what an extractor, review, meta-analysis, or guideline could copy if the human question is confirmed. Do not assert actual propagation, a changed pooled effect, or an incorrect paper conclusion.
8. After the report-generation agent is spawned, add it exactly once to `agent_execution_manifest.md`; then complete the token ledger, timing, report rendering, hash recheck, and final validator steps required by the workflow. These post-audit completion artifacts do not yet exist and cannot be certified here.

## Limitations

- The supplied package contains no participant-level data, table-generation programs, protocol/SAP amendment history, table-freeze history, or full inferential implementation details. Those absences are preserved as human questions and do not authorize removal of a stable ID.
- Exact P-value, statistic, or standard-error reconstruction is not possible for relationships whose degrees of freedom, variance estimator, covariance, sidedness, realized model route, or estimand mapping are absent. Both statistical passes correctly treat those as named limits.
- The final Markdown report, standalone HTML, token summaries, after-review hashes, and validator result are downstream of this audit. Their completeness must be checked after report assembly.
- Current evidence supports neutral reporting-consistency questions only. It does not establish a paper-level conclusion effect or any unbounded downstream effect.
