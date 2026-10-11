# Quantitative Reporting Quality-Control Consistency Review — EPOCH Trial, Workflow 1.6

**Pending Human Adjudication — all 30 stable candidates.** Evidence states describe the review record. Suggested review dispositions mechanically pre-fill human review; they do not determine validity, importance, action, or a final correction.

# Executive Quality-Control Summary

The complete supplied package was reviewed for reproducible numeric, denominator, statistical, cross-document, measure-label, scale, and rate-versus-count consistency. The stable ledger contains **30 candidates**: 25 `recorded_candidate` and five `record_input_error` records. All 30 receive complete evidence cards below. The five input-error records explicitly correct unsupported initial comparison assumptions and retain their unresolved human questions.

Several observations concern small numeric or labeling details; others depend on an unresolved display convention, operational definition, or planned-versus-reported specification. Small preventable reporting defects can matter for downstream evidence extraction if confirmed. This package does not establish that an observation propagated, changed a conclusion, or caused serious harm. No candidate determines the paper’s scientific validity.

The direct-source recheck and final audit control the factual comparisons. In particular, C016 excludes an absent protocol ICU-readmission logit comparator; C006, C010, C024, C027, and C028 do not establish the numeric or semantic contradictions assumed at discovery. C029/C030 distinguish literal elapsed hours from a calendar rule while prominently retaining the protocol’s explicit support for intentional shorthand.

# Package and Reused-Evidence Provenance

The reviewed article is *Effect of a Pediatric Early Warning System on All-Cause Mortality in Hospitalized Pediatric Patients: The EPOCH Randomized Clinical Trial*. The package contains four unencrypted PDFs and no supplied Office, workbook, CSV, raw-data, or executed-model source. Roles are assigned by document content.

| Source ID | Actual supplied file | Role | Physical PDF pages |
|---|---|---|---:|
| DOC-001 | [jama_parshuram_2018_oi_180015.pdf](<../jama_parshuram_2018_oi_180015.pdf#page=1>) | REPORT — main article | 11 |
| DOC-002 | [joi180015supp1_prod.pdf](<../joi180015supp1_prod.pdf#page=1>) | PLAN — protocol, operational appendices, and historical background | 37 |
| DOC-003 | [joi180015supp2_prod.pdf](<../joi180015supp2_prod.pdf#page=1>) | PLAN — statistical analysis plan | 7 |
| DOC-004 | [joi180015supp3_prod.pdf](<../joi180015supp3_prod.pdf#page=1>) | REPORT — results supplement, definitions, figures, tables, and power comparisons | 14 |
| Total | Four PDFs; two REPORT and two PLAN documents | 25 REPORT pages; 44 PLAN pages | 69 |

The curator identified 66 eligible existing assets: eight native/layout text files, 53 rendered pages, four PDF information records, and one stale structural page-status manifest. The 65 reused assets were hashed before review. The stale manifest’s former tooling/coverage claims were not used scientifically. Historical producing engines are partly unrecorded. Current source identity, page boundaries, direct layout text, and targeted visual rechecks establish locator fitness; the supplied PDFs remain final evidence authority. Partial graph-text ordering on results pages 2/4 was handled with complementary images. No old candidate set, classification, verifier, critic, review queue, or final report defined discovery scope.

Durable provenance: [source inventory](review_1_6/source_inventory.md), [asset inventory](review_1_6/evidence_asset_inventory.md), [source hashes before review](review_1_6/source_hashes_before.sha256), and [reused-asset hashes before review](review_1_6/reused_artifact_hashes_before.sha256).

# Scope, Complete Coverage, and Exclusions

Every physical source page was freshly mapped scientifically, including references, historical plan material, and administrative pages with no applicable quantitative result. Reusable extraction reduced preprocessing, not reasoning or coverage. No source page required extraction-gap mapping; targeted fresh direct-source confirmation was nevertheless performed for candidate recheck.

| Source | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 | 37 | 37 | 0 | 37 | COMPLETE |
| DOC-003 | 7 | 7 | 0 | 7 | COMPLETE |
| DOC-004 | 14 | 14 | 0 | 14 | COMPLETE |
| Total PDF_PAGE units | 69 | 69 | 0 | 69 | COMPLETE |

Every row partitions total units into reusable and fresh-required units and has mapped units equal to total. The [source coverage ledger](review_1_6/source_coverage.md), [coverage manifest](review_1_6/coverage_manifest.md), [main evidence map](review_1_6/extraction/main_quantitative_evidence.md), and [support evidence map](review_1_6/extraction/support_quantitative_evidence.md) provide the complete assignments and durable outcomes. There is no scientific source-coverage gap.

The review prioritizes concrete quantitative reporting consistency. Analysis-unit and population issues qualify only through a reported number, denominator, statistic, label, or interpretation. Broad methodological quality, study design, clinical judgment, novelty, misconduct, and raw-data auditing are outside scope. Only supplied local evidence was used; no web or external literature was consulted. Coherent display-zero P values alone are excluded (`DISPLAY_ZERO_NOT_CANDIDATE`); neither display precision nor a reconstructed tiny positive probability establishes a contradiction.

# Quantitative and Statistical Relationship Coverage

The canonical inventories contain **154 numeric/reporting relationships (N001–N154)** and **112 statistical or inferential-definition relationships (S001–S112)**. Coverage includes all hospital-table rows and descriptive cell families; counts, totals, percentages and extrema; intervals, P values, model/adjustment labels and effect measures; repeated narrative/table/figure results; definitions, populations, exposure units, and prospective/historical plan quantities. Support mapper keys are explicitly bound to canonical relationship IDs.

Fresh distinct statistical agents `root/stats1` and `root/stats2`, each `gpt-6.1-sol` / `high`, reviewed all 112 statistical relationships. Every relationship has `PASS_1_COMPLETE` and `PASS_2_COMPLETE` records. Pass 2 considered the complete initial stable ledger and exact-source recheck and added the two different endpoint-window comparisons now C029/C030; a separate fresh appended-ID rechecker confirmed them. The main and support mapping lanes were distinct and disjoint; numeric, cross-source, and first statistical checking were independently performed. The final fresh auditor covered all 30 IDs, classifications, source pages, and N/S relationships.

Checks included arithmetic and rounding, numerator/denominator identity, interval containment and order, direction, matched-result agreement, response/measure units, exposure scale, rate/count distinctions, and model-specific interpretation. Statistical compatibility was assessed only where the package supplied compatible tests, sidedness, models, variance or adjustment definitions. Ratios and identity-link differences remain separate fits; crude arm arithmetic is not substituted for adjusted estimators. Unrounded covariance, test outputs, patient records, and unspecified Bayesian conventions were not reconstructed.

Records: [numeric inventory](review_1_6/relationships/numeric_relationship_inventory.md), [statistical inventory](review_1_6/statistics/relationship_inventory.md), [numeric checker](review_1_6/checkers/numeric_consistency.md), [cross-source checker](review_1_6/checkers/cross_source_consistency.md), [statistical pass 1](review_1_6/checkers/statistical_pass_1.md), [statistical pass 2](review_1_6/checkers/statistical_pass_2.md), [exact-source recheck](review_1_6/verification/evidence_recheck.md), and [final evidence-quality audit](review_1_6/quality/evidence_quality_audit.md).

# Document-Role Classification Summary

`S_W` compares locations within one REPORT; `S_C` compares two different REPORT documents; `P_R` compares PLAN and REPORT content; `P_P` compares PLAN content internally or across plans. Historical results inside a protocol remain PLAN. A corroborating document creates no extra discrepancy relationship. Primary precedence is `P_R` > `P_P` > `S_C` > `S_W`. Review domains and suggested dispositions follow the mechanical rules in QUALITY_CONTROL_SCOPE.md.

| Primary relationship type | Candidates |
|---|---:|
| S_W | 6 |
| S_C | 7 |
| P_R | 6 |
| P_P | 11 |
| Total | 30 |

| Review domain | Candidates |
|---|---:|
| report_internal_inconsistency | 11 |
| protocol_report | 6 |
| plan_material | 11 |
| statistical_results | 2 |
| Total | 30 |

| Evidence state | Candidates |
|---|---:|
| recorded_candidate | 25 |
| record_input_error | 5 |
| not_reproduced | 0 |
| repaired_residual | 0 |
| Total | 30 |

Each count table independently reconciles to the 30 stable IDs. Mechanical suggestions are `retain` for 25 and `discuss` for five; none receives `exclude`. These are human-review pre-fills only. Every record remains Pending Human Adjudication. The five `record_input_error` IDs are C006, C010, C024, C027, and C028. Exact final classification values come from the [stable ledger](review_1_6/candidate_ledger.md), as confirmed by recheck and audit.

# Candidate Index

| Stable ID | Primary category | Relationship type | Review domain | Evidence state |
|---|---|---|---|---|
| C001 | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C002 | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C003 | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | recorded_candidate |
| C004 | Cross-document numeric inconsistency | S_C | report_internal_inconsistency | recorded_candidate |
| C005 | Cross-document numeric inconsistency | S_C | report_internal_inconsistency | recorded_candidate |
| C006 | Cross-document numeric inconsistency | P_R | protocol_report | record_input_error |
| C007 | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C008 | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C009 | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C010 | Rate-versus-count inconsistency | P_P | plan_material | record_input_error |
| C011 | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | recorded_candidate |
| C012 | Measure, label, or scale inconsistency | P_R | protocol_report | recorded_candidate |
| C013 | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | recorded_candidate |
| C014 | Denominator, proportion, or total inconsistency | P_R | protocol_report | recorded_candidate |
| C015 | Measure, label, or scale inconsistency | P_R | protocol_report | recorded_candidate |
| C016 | Measure, label, or scale inconsistency | P_R | protocol_report | recorded_candidate |
| C017 | Measure, label, or scale inconsistency | P_R | protocol_report | recorded_candidate |
| C018 | Denominator, proportion, or total inconsistency | P_P | plan_material | recorded_candidate |
| C019 | Denominator, proportion, or total inconsistency | P_P | plan_material | recorded_candidate |
| C020 | Numeric or arithmetic inconsistency | P_P | plan_material | recorded_candidate |
| C021 | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C022 | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C023 | Numeric or arithmetic inconsistency | S_W | statistical_results | recorded_candidate |
| C024 | Denominator, proportion, or total inconsistency | S_W | statistical_results | record_input_error |
| C025 | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C026 | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C027 | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | record_input_error |
| C028 | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | record_input_error |
| C029 | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | recorded_candidate |
| C030 | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | recorded_candidate |

# Candidate Evidence Cards

Every card below is Pending Human Adjudication. Recheck facts supersede any corrected discovery assertion preserved in the ledger. The source evidence is directly printed or visual; calculation and inferred explanations are explicitly separated.

## C001 — Main figure group encoding

**Pending Human Adjudication**

**Candidate statement:** The main mortality figure gives opposite group-to-line assignments in its legend and caption.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Figure 2 legend versus caption

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** REPORT versus REPORT within main article; S_W only; category Measure, label, or scale inconsistency; report_internal_inconsistency. Results table is corroboration, not an additional discrepancy relationship. No classification ambiguity.

**Classification ambiguity:** None

**Exact source locations:** [jama_parshuram_2018_oi_180015.pdf — PDF p. 8; main Figure 2 legend and caption, p8](<../jama_parshuram_2018_oi_180015.pdf#page=8>); visual inspection of fresh render.

**Source evidence:** Legend assigns BedsidePEWS to blue-gray circles/solid line and usual care to orange circles/dashed line.

**Reported-versus-comparator:** Caption assigns intervention hospitals to the dashed orange line and usual care to the solid blue line; slopes 0.57 and 0.53 are printed.

**Reasoning procedure:** Yes. A single figure's group-to-line encoding must agree between legend and explanatory caption. Reversed printed/visual encodings are direct. A production transposition is inferred.

**Calculation:** The two group-to-color/style mappings are reversed. The plot's rightmost blue-gray point near (6.03,0.8) also matches intervention hospital C in [joi180015supp3_prod.pdf — PDF p. 9; results eTable 2, p9](<../joi180015supp3_prod.pdf#page=9>).

**Alternative source-grounded interpretations:** Caption descriptors may be transposed, or legend/plot descriptors may be transposed. Hospital letters/table coordinates support the plotted group encoding but do not prescribe a correction. Missing inputs/definitions: Which encoding the authors intended for group-specific slopes; underlying fitted-line output if slope attribution is to be resolved.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for the encoding comparison. Exact fitted model outputs are unavailable and unnecessary to establish the reversed descriptions. Evidence-record determination: recorded_candidate, determined by directly observed reversed encodings. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a reversed group-to-line assignment or slope attribution. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a reversed group-to-line assignment or slope attribution. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Which group-to-line assignment and slope attribution are intended?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Supplemental figure group encoding

**Pending Human Adjudication**

**Candidate statement:** The supplemental mortality figure gives opposite group-to-color and line-style assignments in its legend and caption.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results eFigure 1 legend versus caption

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both discrepant locations are REPORT content in the same results supplement; S_W only; Measure, label, or scale inconsistency; report_internal_inconsistency. eTable 2 only corroborates group identity. No ambiguity.

**Classification ambiguity:** None

**Exact source locations:** [joi180015supp3_prod.pdf — PDF p. 2; results eFigure 1, p2](<../joi180015supp3_prod.pdf#page=2>) visually rendered and [joi180015supp3_prod.pdf — PDF p. 3; caption, p3](<../joi180015supp3_prod.pdf#page=3>).

**Source evidence:** Legend usual care is salmon/red dotted; BedsidePEWS is turquoise dashed. H and C are turquoise; U is salmon.

**Reported-versus-comparator:** Caption identifies A–J as BedsidePEWS and K–U as usual care, but says intervention salmon/dotted and usual care blue/dashed.

**Reasoning procedure:** Yes, identity of group/color/style for the same quantitative graph. Source-rendered group encodings and caption words are direct; a transposition mechanism is inferred.

**Calculation:** H (2.47,5.21) and U (2.77,3.13) match [joi180015supp3_prod.pdf — PDF p. 9; eTable 2, p9](<../joi180015supp3_prod.pdf#page=9>) and their plotted colors; caption colors/styles reverse both legend groups.

**Alternative source-grounded interpretations:** Caption rather than plotted group encoding may be transposed; this does not identify a final correction. Missing inputs/definitions: Author-intended figure descriptors and fitted plotting code, if the mechanism is to be determined.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for direct encoding comparison and point confirmation. Evidence-record determination: recorded_candidate, determined by directly reversed group descriptors. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a reversed supplemental group-to-line assignment. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a reversed supplemental group-to-line assignment. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Which color/style wording is intended for each fitted group line?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Main figure horizontal-period label

**Pending Human Adjudication**

**Candidate statement:** The main mortality figure’s literal horizontal-axis period label differs from its caption, supplemental axis, and corroborating hospital coordinate.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT main Figure 2 axis versus caption and REPORT results eFigure 1/eTable 2

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Main axis/caption produce S_W; main versus distinct REPORT results supplement produces S_C. Primary S_C by precedence; All relationships S_C, S_W; Measure, label, or scale inconsistency; report_internal_inconsistency. No role ambiguity.

**Classification ambiguity:** None

**Exact source locations:** [jama_parshuram_2018_oi_180015.pdf — PDF p. 8; main Figure 2, p8](<../jama_parshuram_2018_oi_180015.pdf#page=8>), [joi180015supp3_prod.pdf — PDF p. 2; results eFigure 1, p2](<../joi180015supp3_prod.pdf#page=2>), and [joi180015supp3_prod.pdf — PDF p. 9; eTable 2 hospital C, p9](<../joi180015supp3_prod.pdf#page=9>).

**Source evidence:** Main x-axis says deaths per 1000 discharges during baseline **and intervention** periods; its caption says coordinates are baseline and intervention rates.

**Reported-versus-comparator:** Supplement x-axis says baseline period. C has baseline 4/663 (6.03), intervention 1/1250 (0.8), total discharges 1913.

**Reasoning procedure:** Yes: a plotted baseline rate and a combined-period rate have different denominators/time definitions. Axis words, table counts, and point position are direct; an extra axis phrase is an inferred production explanation.

**Calculation:** 4000/663=6.03318; 5000/1913=2.61370. Both fresh-rendered plots put C near x=6.03,y=0.8, not x=2.61.

**Alternative source-grounded interpretations:** The axis may be a loose description of the two-dimensional display; the caption and supplemental baseline axis define the actual horizontal quantity. Missing inputs/definitions: Whether the main horizontal label intends a combined rate or simply inadvertently names both displayed periods.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for rates and visual discrimination; exact plotting coordinates not supplied as structured data, but the difference is far larger than graphical resolution. Evidence-record determination: recorded_candidate, determined by incompatible literal horizontal time label and directly corroborated baseline coordinates. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a different horizontal time basis for mortality rates. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a different horizontal time basis for mortality rates. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: What exact time basis should the main x-axis communicate?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Usual-care baseline patient-day minimum

**Pending Human Adjudication**

**Candidate statement:** The usual-care baseline patient-day minimum is 6665 in the flow figure and 6655 in the hospital table.

**Category:** Cross-document numeric inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main Figure 1 versus REPORT results eTable 3

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** REPORT main versus REPORT results supplement; S_C only; Cross-document numeric inconsistency; report_internal_inconsistency; no ambiguity.

**Classification ambiguity:** None

**Exact source locations:** [jama_parshuram_2018_oi_180015.pdf — PDF p. 3; main Figure 1 baseline box, p3](<../jama_parshuram_2018_oi_180015.pdf#page=3>) and [joi180015supp3_prod.pdf — PDF p. 11; results eTable 3, p11](<../joi180015supp3_prod.pdf#page=11>).

**Source evidence:** Main usual-care baseline range 6665–31575; total 162497.

**Reported-versus-comparator:** Table baseline K–U values 10164,6655,8941,8917,11705,12126,13335,16077,14304,28698,31575; L is 6655.

**Reasoning procedure:** Yes, integer minimum among the same eleven usual-care hospitals/period. Values and minimum/sum arithmetic are direct/reproducible; transcription mechanism is inferred.

**Calculation:** Minimum=6655; sum=162497; printed flow minimum differs by 10. Matching total, maximum, group, and phase support alignment.

**Alternative source-grounded interpretations:** One hospital row or flow extremum may contain a transcription difference; a distinct 10-day definition is not disclosed. Missing inputs/definitions: Which original count or extremum is intended; no missing input prevents the printed comparison.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes, all eleven counts and total. Evidence-record determination: recorded_candidate, determined by reproduced 10-day extremum mismatch with matching cohort totals. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a different site-level patient-day minimum. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a different site-level patient-day minimum. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Which baseline minimum is intended, and do the two sources intentionally use different hospital-day definitions?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Usual-care intervention discharge maximum

**Pending Human Adjudication**

**Candidate statement:** The usual-care intervention discharge maximum is 29956 in the flow figure and 26956 in the hospital table.

**Category:** Cross-document numeric inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main Figure 1 versus REPORT results eTable 2

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** REPORT main versus REPORT results supplement; S_C only; Cross-document numeric inconsistency; report_internal_inconsistency; no ambiguity.

**Classification ambiguity:** None

**Exact source locations:** [jama_parshuram_2018_oi_180015.pdf — PDF p. 3; main Figure 1 intervention/analysis boxes, p3](<../jama_parshuram_2018_oi_180015.pdf#page=3>) and [joi180015supp3_prod.pdf — PDF p. 9; results eTable 2, p9](<../joi180015supp3_prod.pdf#page=9>).

**Source evidence:** Main twice gives range 3672–29956 and total 94366.

**Reported-versus-comparator:** Table K–U intervention discharges 7285,5642,3811,3672,4638,5471,6440,7327,5886,26956,17238.

**Reasoning procedure:** Yes, maximum among the same eleven hospitals/phase. Source values and extremum calculation are observed/reproduced; a typographic cause is inferred.

**Calculation:** Maximum=26956; sum=94366; flow maximum exceeds table maximum by 3000. Minimum also agrees at 3672.

**Alternative source-grounded interpretations:** Flow extremum or T row may be transcribed differently; matching total/minimum strongly supports the registered alignment. Missing inputs/definitions: Intended source discharge maximum, if either printed count is to be changed.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes, all site counts, group total, and period definition. Evidence-record determination: recorded_candidate, determined by exact 3000-discharge maximum disagreement. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a different site-level discharge maximum. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a different site-level discharge maximum. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Which intervention maximum is intended, and does Figure 1 deliberately use a different site dataset?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Anticipated bed inputs and unsupported common-basis assumption

**Pending Human Adjudication**

**Candidate statement:** The anticipated bed total and participating-site bed count have different supported input bases; the initially assumed common census basis is not established.

**Category:** Cross-document numeric inconsistency

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT results anticipated power inputs versus PLAN protocol participating-site data

**Review domain:** protocol_report

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** REPORT results versus PLAN protocol by content; residual comparison P_R only; Cross-document numeric inconsistency; protocol_report. Ambiguity is common basis, not roles. The appendix corroborates a supported power basis and creates no separate P_P discrepancy.

**Classification ambiguity:** The common bed-census basis is unsupported; source-supported power and participating-site inputs differ in purpose.

**Exact source locations:** [joi180015supp3_prod.pdf — PDF p. 14; results eTable 5, p14](<../joi180015supp3_prod.pdf#page=14>), [joi180015supp1_prod.pdf — PDF p. 14; protocol sample-size section, p14](<../joi180015supp1_prod.pdf#page=14>), and [joi180015supp1_prod.pdf — PDF p. 29; power appendix, p29](<../joi180015supp1_prod.pdf#page=29>).

**Source evidence:** Results anticipated 20 hospitals/2397 ward beds, 99389 discharges/397556 days; caption explicitly tabulates power assumptions including constant cluster size.

**Reported-versus-comparator:** Protocol p14 presents the 21 participating sites’ available data as 2322 beds, with the same 99389 admissions and 397556 patient-days. Appendix sets n=20 and average bed size 119.85.

**Reasoning procedure:** Conditional only. Equality would apply if the bed rows represented the same participating-site census, but the report explicitly frames its column as power assumptions. Printed counts and exact power product are direct/reproduced; equating their bed basis is an unsupported registered assumption.

**Calculation:** 2397−2322=75; 20×119.85=2397 exactly. These are different numbers with a supplied alternative basis, not a reproduced common-basis bed discrepancy.

**Alternative source-grounded interpretations:** 2397 is the constant-cluster power total derived directly from the protocol appendix, while 2322 is the available participating-site count. Shared admissions/day inputs do not make every row a census. Missing inputs/definitions: Whether the report's anticipated bed row is an actual census or constant-cluster power input; source mapping of each anticipated row.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for both printed numbers and power-derived 2397; no for establishing identical bed-population/basis. Evidence-record determination: record_input_error, determined by unsupported bed-row alignment and exact source-supported alternative power total. Whether any residual labeling discrepancy exists remains unsettled. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a power-input bed total treated incorrectly as an observed site census. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a power-input bed total treated incorrectly as an observed site census. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Does the anticipated bed row intend the constant-cluster power total, and should its basis be explicitly distinguished from the available-site census?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Mortality absolute-reduction scale

**Pending Human Adjudication**

**Candidate statement:** The mortality power appendix’s 0.9% absolute reduction differs by a factor of ten from the same plan’s 0.09% and 0.9-per-1000 summaries.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol appendix versus sample-size summary

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All conflicting locations PLAN; P_P only; Measure, label, or scale inconsistency; plan_material. [jama_parshuram_2018_oi_180015.pdf — PDF p. 4; Main p4](<../jama_parshuram_2018_oi_180015.pdf#page=4>) supports 0.9/1000 only and adds no discrepancy relationship.

**Classification ambiguity:** None

**Exact source locations:** [joi180015supp1_prod.pdf — PDF p. 29; protocol p29 appendix](<../joi180015supp1_prod.pdf#page=29>), [joi180015supp1_prod.pdf — PDF p. 14; p14 sample size](<../joi180015supp1_prod.pdf#page=14>), and [joi180015supp1_prod.pdf — PDF p. 1; p1 summary](<../joi180015supp1_prod.pdf#page=1>).

**Source evidence:** Appendix says 18% relative reduction corresponds to absolute risk reduction 0.9%; baseline 5.1/1000; more precise RRR 0.178 also printed.

**Reported-versus-comparator:** p14 says 18% relative and absolute 0.09%; p1 says 0.9 deaths/1000.

**Reasoning procedure:** Yes, matched mortality power scenario and percent/per-thousand conversion. Printed percentage disagreement and conversion are direct/reproduced; a decimal transcription is inferred.

**Calculation:** 5.1×0.18=0.918 deaths/1000=0.0918%; 0.9/1000=0.09%; 0.9%=9/1000. RRR0.178 gives0.9078/1000 and does not rescue the percentage.

**Alternative source-grounded interpretations:** Decimal/unit transcription or another baseline; no alternative baseline matching this 18% scenario is supplied. Missing inputs/definitions: Whether an unreported alternative scenario generated the appendix percentage.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for arithmetic and unit comparison; no original power execution needed. Evidence-record determination: recorded_candidate, determined by tenfold percentage scale difference. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a tenfold different planned absolute-effect percentage. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a tenfold different planned absolute-effect percentage. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Which absolute percentage belongs to this mortality power scenario?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Cardiac-arrest intensity codes

**Pending Human Adjudication**

**Candidate statement:** The protocol’s cardiac-arrest intensity codes differ between the endpoint definition/scale and abstraction-table legend.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol intensity definition/Table 5 versus Table 6 legend

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** PLAN throughout; P_P only; Measure, label, or scale inconsistency; plan_material. No role ambiguity; alternate-scale ambiguity remains named.

**Classification ambiguity:** An undisclosed earlier scale version could explain the legend; no such version is supplied.

**Exact source locations:** [joi180015supp1_prod.pdf — PDF p. 11; protocol p11 clinical definition](<../joi180015supp1_prod.pdf#page=11>), [joi180015supp1_prod.pdf — PDF p. 24; Table 5 p24](<../joi180015supp1_prod.pdf#page=24>), and [joi180015supp1_prod.pdf — PDF p. 27; Table 6 legend p27](<../joi180015supp1_prod.pdf#page=27>).

**Source evidence:** Definition rates cardiac arrests 6 or 7 on the Children's Resuscitation Intensity Scale.

**Reported-versus-comparator:** Table 6 legend names cardiac arrest scale rating 4 or 5. Table 5 assigns 4 to circulatory support, 5 to respiratory/circulatory support, 6 to chest compressions/ECMO, 7 to death.

**Reasoning procedure:** Yes, discrete codes on the same named endpoint intensity scale. Codes/definitions are direct; a stale legend is inferred.

**Calculation:** {4,5} differs from {6,7}; their treatment definitions are visibly different. No rounding applies.

**Alternative source-grounded interpretations:** A stale legend or alternate unlabelled scale may explain it; no such scale is supplied in the bound plan. Missing inputs/definitions: Whether Table 6 refers to an undisclosed prior intensity scale; the actual review-form code version.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for code mapping. Event-level coding is unavailable and not needed for the printed comparison. Evidence-record determination: recorded_candidate, determined by inconsistent endpoint-to-code assignment. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a different cardiac-arrest endpoint code set. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a different cardiac-arrest endpoint code set. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Which intensity codes were intended to trigger the Table 6 cardiac-arrest abstraction?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Preventability threshold boundary

**Pending Human Adjudication**

**Candidate statement:** The protocol’s strict preventability threshold excludes rating 4 while its enumeration and table legend include it.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol strict threshold versus enumeration/Table 7

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** PLAN/PLAN, P_P only; Measure, label, or scale inconsistency; plan_material. [joi180015supp3_prod.pdf — PDF p. 6; Results p6](<../joi180015supp3_prod.pdf#page=6>) and [jama_parshuram_2018_oi_180015.pdf — PDF p. 7; main p7](<../jama_parshuram_2018_oi_180015.pdf#page=7>) corroborate inclusion of 4 and do not create extra P_R discrepancy relationships.

**Classification ambiguity:** None

**Exact source locations:** [joi180015supp1_prod.pdf — PDF p. 11; protocol p11](<../joi180015supp1_prod.pdf#page=11>) and [joi180015supp1_prod.pdf — PDF p. 28; Table 7 p28](<../joi180015supp1_prod.pdf#page=28>).

**Source evidence:** p11 says consensus rating “at >4.”

**Reported-versus-comparator:** The immediately following sentence expressly includes ratings 4,5,6; Table 7 legend says a rating of 4 or more.

**Reasoning procedure:** Yes, membership at integer boundary 4 on the same six-point scale. Conflicting membership definitions are direct; possible typographic cause is inferred.

**Calculation:** >4 selects {5,6}; 4 or more selects {4,5,6}. Rating 4 fails the first and satisfies the second.

**Alternative source-grounded interpretations:** A strict-symbol typo rather than a different analysis threshold; no correction assigned. Missing inputs/definitions: Applied operational cutoff and number of events rated 4; neither is inferred from 21/27 or 29/32.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for boundary comparison; no event ratings to quantify its consequences. Evidence-record determination: recorded_candidate, determined by reproduced boundary contradiction. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a different preventability boundary. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a different preventability boundary. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Was rating 4 included in the applied preventability dichotomy?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — Annual versus two-year historical admissions

**Pending Human Adjudication**

**Candidate statement:** The annual and two-year historical counts cannot be treated as the same cohort without the missing reference-period definition.

**Category:** Rate-versus-count inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol annual input versus historical two-year dataset

**Review domain:** plan_material

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Historical material remains PLAN by content; P_P only; Rate-versus-count inconsistency; plan_material. Ambiguity is matching historical periods, not source roles.

**Classification ambiguity:** The historical reference periods and cohort identity are not established.

**Exact source locations:** [joi180015supp1_prod.pdf — PDF p. 14; protocol p14](<../joi180015supp1_prod.pdf#page=14>) and [joi180015supp1_prod.pdf — PDF p. 30; historical appendix p30](<../joi180015supp1_prod.pdf#page=30>).

**Source evidence:** p14 describes 1052 urgent ICU admissions/year from four Ontario pediatric hospitals, without identifying a year or dataset period.

**Reported-versus-comparator:** p30 explicitly describes 1052 admissions in two years following 31 January 2007 from the four largest Ontario pediatric referral hospitals, alongside 55963 discharges and 150 code-blue events.

**Reasoning procedure:** Only if the counts represent the same historical cohort. Count/year and two-year count cannot otherwise be equated solely by numerical identity. Printed periods/counts are direct. Registering a same-cohort annualization contradiction assumes an alignment not established by the supplied text.

**Calculation:** For the p30 cohort, 1052/2=526/year; labeling that aggregate 1052/year would double annualization. The calculation is conditional; it does not establish p14's cohort identity.

**Alternative source-grounded interpretations:** The same four centers could supply another annual series or estimate of 1052; p14 does not give the dates that would exclude this. Missing inputs/definitions: The reference period/source dataset for p14 and whether it is the p30 2007–2008 aggregate.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for p30's annualized count; no definitive identification of p14's historical series/year. Evidence-record determination: record_input_error, determined by unsupported historical-series alignment. Exact dates of p14 remain missing, so a residual discrepancy cannot be settled. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns an unsupported historical annual frequency. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy an unsupported historical annual frequency. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Are both occurrences 1052 drawn from the same two-year dataset, or is p14 a separate annual cohort/estimate?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — Fluid-resuscitation threshold

**Pending Human Adjudication**

**Candidate statement:** The main SCDE definition includes exactly 60 mL/kg while the results supplement’s strict threshold excludes that boundary.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main SCDE threshold versus REPORT results definition

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** REPORT main versus REPORT results supplement; S_C only; Measure, label, or scale inconsistency; report_internal_inconsistency. [joi180015supp1_prod.pdf — PDF p. 24; Protocol Table 5 p24](<../joi180015supp1_prod.pdf#page=24>) only corroborates the strict boundary and adds no P_R relationship.

**Classification ambiguity:** None

**Exact source locations:** [jama_parshuram_2018_oi_180015.pdf — PDF p. 4; main Study Outcomes p4](<../jama_parshuram_2018_oi_180015.pdf#page=4>) and [joi180015supp3_prod.pdf — PDF p. 6; results eTable 1 p6](<../joi180015supp3_prod.pdf#page=6>).

**Source evidence:** Main lists fluid boluses of 60 mL/kg or greater within the 12 hours before ICU admission.

**Reported-versus-comparator:** Results definition gives >60 mL/kg in the 12 hours before transfer.

**Reasoning procedure:** Yes, strict versus inclusive numerical threshold for the matched SCDE component. Printed threshold difference is direct; changes in SCDE event totals are not established.

**Calculation:** Exactly 60 mL/kg with no other qualifying component satisfies ≥60 but fails >60.

**Alternative source-grounded interpretations:** Threshold wording/symbol may be inexact, or measurement tolerance may govern classification. Neither resolves printed inclusion/exclusion. Missing inputs/definitions: Operational fluid threshold/tolerance and counts of events exactly 60 without another qualifying component.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for threshold logic; boundary-patient data are absent. Evidence-record determination: recorded_candidate, determined by reproduced boundary membership difference. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a different fluid-volume boundary for SCDE. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a different fluid-volume boundary for SCDE. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Which threshold governed event classification at exactly 60 mL/kg?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C012 — Circulatory component conjunction

**Pending Human Adjudication**

**Candidate statement:** The protocol’s circulatory component requires fluids and vasoactive support, while the report definitions allow either component.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol circulatory conjunction versus REPORT main/results disjunction

**Review domain:** protocol_report

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** PLAN versus REPORT main/results; P_R only; Measure, label, or scale inconsistency; protocol_report. Main and results agree on disjunction, so no additional S_C. No role ambiguity.

**Classification ambiguity:** None

**Exact source locations:** [joi180015supp1_prod.pdf — PDF p. 24; protocol Table 5 p24](<../joi180015supp1_prod.pdf#page=24>), [jama_parshuram_2018_oi_180015.pdf — PDF p. 4; main p4](<../jama_parshuram_2018_oi_180015.pdf#page=4>), and [joi180015supp3_prod.pdf — PDF p. 6; results eTable 1 p6](<../joi180015supp3_prod.pdf#page=6>).

**Source evidence:** Protocol level 4 requires >60 mL/kg fluid and administration of inotrope/vasopressor; it is SCDE Yes.

**Reported-versus-comparator:** Results says >60 fluid and/or inotrope/vasopressor; main composite of one or more components separately lists vasoactive medication or qualifying fluid boluses.

**Reasoning procedure:** Yes, AND versus OR for the matched circulatory component, independent of C011's numerical boundary. Different Boolean definitions are direct; amendment mechanism and count effect are unestablished.

**Calculation:** Fluid-only or vasoactive-only without another component satisfies report disjunction and fails protocol conjunction.

**Alternative source-grounded interpretations:** Definition amended or plan conjunction imprecise; no supplied amendment resolves which explanation applies. Missing inputs/definitions: Final operational conjunction, a documented change if any, and affected treatment combinations.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for logical comparison, no event-level treatment patterns or amendment history. Evidence-record determination: recorded_candidate, determined by reproduced logical membership difference. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a different logical circulatory component definition. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a different logical circulatory component definition. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Which circulatory rule was applied, and does the textual difference reflect an amendment or description error?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C013 — ICU rate wording versus patient duration summaries

**Pending Human Adjudication**

**Candidate statement:** The literal blanket ICU rate wording has a different dimension from the explicitly per-patient duration summaries; its intended scope remains undefined.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT main ICU-rate wording versus main patient narrative and REPORT results patient summaries

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** REPORT main/internal patient narrative produces S_W; main versus REPORT results supplement produces S_C; primary S_C; All relationships S_C, S_W; Measure, label, or scale inconsistency; report_internal_inconsistency. [joi180015supp2_prod.pdf — PDF p. 7; SAP p7](<../joi180015supp2_prod.pdf#page=7>) corroborates per-patient aggregation only and adds no P_R. Scope ambiguity recorded.

**Classification ambiguity:** The scope of the blanket ICU rate statement is unqualified; selected event outcomes may have been intended.

**Exact source locations:** [jama_parshuram_2018_oi_180015.pdf — PDF p. 4; main Data Analyses p4](<../jama_parshuram_2018_oi_180015.pdf#page=4>), [jama_parshuram_2018_oi_180015.pdf — PDF p. 6; main patient narrative p6](<../jama_parshuram_2018_oi_180015.pdf#page=6>), [joi180015supp3_prod.pdf — PDF p. 12; results eTable 4 p12](<../joi180015supp3_prod.pdf#page=12>), and [joi180015supp3_prod.pdf — PDF p. 13; footnotes p13](<../joi180015supp3_prod.pdf#page=13>).

**Source evidence:** Main says patient outcomes are expressed per 1000 patient-days in ICU (ICU outcomes).

**Reported-versus-comparator:** eTable 4 is expressly per-patient; 686/967 patients, total-LOS means 9.4/9 days, ventilator-free means 23.9/24 days, MV means 4.1/3.7 days; footnotes define per-patient totals/means and continuous mean differences. Main p6 explicitly describes 1653 patients remaining in ICU for 15212 days.

**Reasoning procedure:** Yes, the literal blanket rate denominator has dimensions different from day totals/means per patient. Its intended scope is conditional. General denominator statement and patient-summary dimensions are direct; an intended scope restriction is inferred.

**Calculation:** Mean duration=sum of patient durations/number of patients, measured in days; it is not events per 1000 ICU patient-days. The table's Gaussian mean differences 1.28,0.26,0.69 are dimensionally day differences.

**Alternative source-grounded interpretations:** Main statement may apply only to selected event outcomes, with patient resource summaries exempt; that scope is not explicitly qualified locally. Missing inputs/definitions: Which subset of ICU outcomes the main per-1000-day statement intends to describe.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for outcome dimensions and patient summary definitions; raw patient durations are unnecessary for this label comparison. Evidence-record determination: recorded_candidate, determined by literal denominator/dimension mismatch pending named scope definition. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a patient-duration mean labeled as a patient-day event rate. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a patient-duration mean labeled as a patient-day event rate. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Precisely which ICU outcomes should carry the per-1000-ICU-day label, and which are patient duration means?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C014 — ICU-readmission denominator

**Pending Human Adjudication**

**Candidate statement:** The protocol specifies hospital discharges for ICU readmission, whereas the SAP and report specify ICU discharges.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN protocol hospital-discharge denominator versus PLAN SAP and REPORT main ICU-discharge denominator

**Review domain:** protocol_report

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** PLAN protocol versus REPORT main establishes P_R; PLAN protocol versus PLAN SAP is independently conflicting P_P. Primary P_R; All relationships P_R, P_P; Denominator, proportion, or total inconsistency; protocol_report. Roles confirmed; no extra S_W.

**Classification ambiguity:** None

**Exact source locations:** [joi180015supp1_prod.pdf — PDF p. 12; protocol p12](<../joi180015supp1_prod.pdf#page=12>), [joi180015supp2_prod.pdf — PDF p. 5; SAP shell p5](<../joi180015supp2_prod.pdf#page=5>), and [jama_parshuram_2018_oi_180015.pdf — PDF p. 7; main Table 3 p7](<../jama_parshuram_2018_oi_180015.pdf#page=7>), visually checked.

**Source evidence:** Protocol says PICU mortality and unplanned re-admission (hospital,PICU) per thousand hospital discharges.

**Reported-versus-comparator:** SAP ICU-readmission row denominator PatientDischargesICU. Main ICU readmission <48h: 94(28.40)/108(21.25), rates per 1000 ICU discharges in footnote h; hospital discharges 50173/94366.

**Reasoning procedure:** Yes, explicit hospital-discharge versus ICU-discharge units for the same ICU-readmission endpoint. Opposing denominator labels are direct; historical change mechanism is inferred.

**Calculation:** Hospital denominators would give 94000/50173=1.87352 and108000/94366=1.14448, rather than28.40 and21.25. No hospital-to-ICU denominator substitution is justified.

**Alternative source-grounded interpretations:** Later SAP revises an overgeneralized protocol statement; the report and SAP agree. This is not evidence of a protocol violation. Missing inputs/definitions: Documented final denominator revision and any populations excluded from the stated ICU-discharge denominator.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for printed unit contrast and diagnostic hospital rates; unrounded ICU-rate reconstruction is not needed. Evidence-record determination: recorded_candidate, determined by directly different endpoint denominator definitions. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a hospital rather than ICU discharge denominator. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a hospital rather than ICU discharge denominator. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: What original/final ICU-readmission denominator was intended, and is its change documented?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C015 — Predicted-mortality patient/discharge label

**Pending Human Adjudication**

**Candidate statement:** The SAP’s predicted-mortality discharge label differs from its patient aggregation and the results supplement’s patient percentages.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN SAP discharge label versus its patient aggregation and REPORT results patient denominator

**Review domain:** protocol_report

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** PLAN SAP internally conflicts (P_P); PLAN SAP discharge label versus REPORT results patient definition conflicts (P_R). Primary P_R; All relationships P_R, P_P; Measure, label, or scale inconsistency; protocol_report. Repeat-admission handling limits exact rate reconstruction, not role assignment.

**Classification ambiguity:** The intended discharge subset and patient-versus-admission aggregation require clarification.

**Exact source locations:** [joi180015supp2_prod.pdf — PDF p. 7; SAP ICU analysis p7](<../joi180015supp2_prod.pdf#page=7>), [joi180015supp3_prod.pdf — PDF p. 12; results eTable 4 p12](<../joi180015supp3_prod.pdf#page=12>), [joi180015supp3_prod.pdf — PDF p. 13; prediction footnote p13](<../joi180015supp3_prod.pdf#page=13>), and [jama_parshuram_2018_oi_180015.pdf — PDF p. 7; main admission-event row p7](<../jama_parshuram_2018_oi_180015.pdf#page=7>).

**Source evidence:** SAP label “PIM II Prediction Mortality (/1000 urgent ICU discharges)” accompanies average probability across admissions and an explicit one-record-per-patient analysis.

**Reported-versus-comparator:** Results footnote sums each patient's inverse-logit and presents predicted numbers rounded to integer, percentages of total patients. Table post predicted38(5.5%)/44(4.6%), with686/967 patients. Main urgent admission events828/1178.

**Reasoning procedure:** Yes: averaging within patient then across patients defines a patient probability, not a per-urgent-ICU-discharge rate when patients may have multiple admissions. Percent versus per1000 conversion alone cannot change the population unit. Opposing denominator labels and patient aggregation are direct; the printed-count ratios are diagnostics because the prediction counts are rounded. No inferential mean difference is reconstructed.

**Calculation:** Rounded-count diagnostics38/686×100=5.53936% and44/967×100=4.55016%, compatible with printed patient percentages. Admission-event diagnostics38/828×1000=45.89372 and44/1178×1000=37.35144 differ from approximately55/46 per1000 patients; these event counts are not asserted to equal every eligible urgent discharge count.

**Alternative source-grounded interpretations:** SAP row may retain an admission/discharge label while its implemented aggregation and report use patient predictions; an undisclosed separate discharge quantity may exist. Missing inputs/definitions: Intended SAP row denominator, final unrounded predicted sums, and urgent-discharge population if a separate discharge analysis was intended.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for denominator definitions and dimensional comparison; no underlying probability sums or precise urgent-discharge subset. Evidence-record determination: recorded_candidate, determined by source-defined patient aggregation opposing the discharge row label. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a patient prediction labeled as a discharge-based rate. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a patient prediction labeled as a discharge-based rate. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Is this outcome a patient probability/percentage, or was a distinct discharge-based prediction intended in the SAP label?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C016 — ICU-readmission Poisson versus logistic label

**Pending Human Adjudication**

**Candidate statement:** The SAP ICU-readmission shell names Poisson, whereas the report names logistic regression and an odds ratio; the alleged protocol ICU-logit comparator is absent and excluded.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP ICU-readmission Poisson shell versus REPORT main logistic OR

**Review domain:** protocol_report

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** PLAN SAP versus REPORT main; primary P_R; All relationships **P_R only**; Measure, label, or scale inconsistency; protocol_report. Correction: remove P_P because the registered protocol ICU-readmission logit statement is absent. Preserve that assertion in historical discovery provenance, explicitly removed from the final comparison; no stable ID is deleted. Roles themselves are confirmed.

**Classification ambiguity:** None

**Exact source locations:** [joi180015supp2_prod.pdf — PDF p. 5; SAP shell p5](<../joi180015supp2_prod.pdf#page=5>), [jama_parshuram_2018_oi_180015.pdf — PDF p. 7; main Table 3/footnote d p7](<../jama_parshuram_2018_oi_180015.pdf#page=7>), and [joi180015supp1_prod.pdf — PDF p. 16; protocol analysis p16](<../joi180015supp1_prod.pdf#page=16>).

**Source evidence:** SAP Unplanned ICU Readmissions uses ICU-discharge denominators and “Poisson.” SAP pp1–3 define binomial logit versus Poisson log-rate model families.

**Reported-versus-comparator:** Main ICU readmission<48h gives OR1.11(0.77–1.61), P=.58; footnote d explicitly names logistic regression. The registered claim that protocol p16 specifies an identical logit model for ICU readmission is **not matched**: that list does not contain ICU readmission.

**Reasoning procedure:** Yes to the SAP/report named model/measure identity. No to a nonexistent protocol ICU-readmission model comparator. Model names and OR are direct; production-model change or shell obsolescence is inferred. The unsupported protocol comparison is a discovered registration input error within provenance, while the independent SAP/report mismatch remains.

**Calculation:** Poisson shell label and logistic OR label differ for the matched ICU-readmission endpoint. A Poisson log-rate model produces a rate-ratio scale and a logistic model an odds-ratio scale; no aggregate-count conversion is performed.

**Alternative source-grounded interpretations:** Shell uses Poisson generically despite the SAP's separate binomial section, or the final model was revised. The protocol cannot corroborate this row's logit specification because its list omits ICU readmission. Missing inputs/definitions: Whether the SAP shell is generic/outdated, a distinct intended analysis, or a subsequently revised model specification.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for SAP/report printed labels and source-defined family distinctions. Final production code, outputs, and explicit shell-row link are absent. Evidence-record determination: recorded_candidate, determined by surviving direct SAP/report model-label comparison after removal of unsupported corroboration. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a different planned ICU-readmission model family or effect-measure interpretation. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a different planned ICU-readmission model family or effect-measure interpretation. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Which model specification generated the reported ICU-readmission OR, and how should the SAP Poisson shell row be interpreted?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C017 — Hospital-readmission Poisson versus logistic label

**Pending Human Adjudication**

**Candidate statement:** The SAP hospital-readmission shell names Poisson, whereas the protocol names logit and the report names logistic regression and an odds ratio.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN SAP hospital-readmission Poisson shell versus PLAN protocol logit and REPORT main logistic OR

**Review domain:** protocol_report

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** P_R between PLAN SAP and REPORT main; P_P between PLAN SAP and PLAN protocol independently conflicting labels. Primary P_R; All relationships P_R, P_P; Measure, label, or scale inconsistency; protocol_report. P_P retained because its exact hospital-readmission comparison exists, unlike C016. The protocol also corroborates the report; corroboration alone was not used to add P_P.

**Classification ambiguity:** None

**Exact source locations:** [joi180015supp2_prod.pdf — PDF p. 5; SAP shell p5](<../joi180015supp2_prod.pdf#page=5>), [jama_parshuram_2018_oi_180015.pdf — PDF p. 7; main Table 3/footnote d p7](<../jama_parshuram_2018_oi_180015.pdf#page=7>), and [joi180015supp1_prod.pdf — PDF p. 16; protocol p16](<../joi180015supp1_prod.pdf#page=16>).

**Source evidence:** SAP Unplanned Hospital Readmission uses hospital-discharge denominators and Poisson.

**Reported-versus-comparator:** Main hospital readmission<48h gives OR0.93(0.61–1.41), P=.74 and logistic-regression footnote. Protocol explicitly lists unplanned hospital re-admission within48h among outcomes analyzed with an identical logit model.

**Reasoning procedure:** Yes, same endpoint/discharge denominator with differing named model families and measure labels. Model labels are direct; shell revision mechanism inferred.

**Calculation:** Poisson shell versus report logistic OR and separately versus protocol logit are two independently checkable label comparisons. No OR-to-rate-ratio conversion attempted.

**Alternative source-grounded interpretations:** Generic/stale shell table or changed final specification; other SAP binomial pages and original protocol support logistic, but do not identify the production history. Missing inputs/definitions: Whether shell Poisson label denotes a separate planned analysis, a generic placeholder, or a revision.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for both comparisons; final execution code and explicit shell-row link absent. Evidence-record determination: recorded_candidate, determined by reproducible same-endpoint model-label differences. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a different planned hospital-readmission model family or effect-measure interpretation. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a different planned hospital-readmission model family or effect-measure interpretation. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: How should the planned shell Poisson row be reconciled with the protocol logit specification and reported logistic OR?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C018 — Historical ICU-admission percentage

**Pending Human Adjudication**

**Candidate statement:** The historical 14.5% does not follow ordinary nearest rounding of the displayed 1052/7300 fraction; exact denominator and formatting definitions remain missing.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN historical numerator/ICU discharge denominator versus percentage

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** PLAN historical material throughout; P_P only; Denominator, proportion, or total inconsistency; plan_material. No report relationship. Exactness ambiguity named.

**Classification ambiguity:** Exactness of the displayed historical denominator and its rounding rule are not stated.

**Exact source locations:** [joi180015supp1_prod.pdf — PDF p. 30; protocol historical table p30](<../joi180015supp1_prod.pdf#page=30>).

**Source evidence:** Unplanned PICU admits1052; PICU discharges7300.

**Reported-versus-comparator:** Printed14.5% per PICU discharges.

**Reasoning procedure:** Yes, table's directly identified numerator/denominator percentage; rounding comparison is conditional on displayed counts being the exact inputs. Counts and percentage are direct; arithmetic is reproduced; different denominator production is inferred.

**Calculation:** 100×1052/7300=14.4109589%, which rounds to14.4% to one decimal;14.5% differs by0.0890411 percentage points, exceeding ordinary nearest-rounding tolerance0.05.

**Alternative source-grounded interpretations:** Historical denominator may be rounded or subset-adjusted. For numerator1052, a14.5%-rounded result would require denominator approximately7230–7280, rather than exact7300. Missing inputs/definitions: Whether7300 is exact, a different eligible ICU-discharge denominator, and historical percentage rounding rule.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for displayed arithmetic. It is not stated whether7300 is a rounded historical aggregate. Evidence-record determination: recorded_candidate, determined by nonreconciliation of directly labeled printed inputs under ordinary nearest rounding, pending named historical-input definition. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns an incompatible historical fraction/percentage pairing. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy an incompatible historical fraction/percentage pairing. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Which exact denominator and rounding rule produced14.5%?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C019 — Historical admissions per hospital discharges

**Pending Human Adjudication**

**Candidate statement:** The historical rate of 18 per 1000 differs from nearest-integer rounding of 1052/55963 × 1000, although intentional truncation would yield 18.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN historical numerator/hospital discharge denominator versus rate

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** PLAN historical material, P_P only; Denominator, proportion, or total inconsistency; plan_material. Conditional formatting ambiguity remains named.

**Classification ambiguity:** Nearest rounding versus truncation and exact eligible historical inputs are not specified.

**Exact source locations:** [joi180015supp1_prod.pdf — PDF p. 30; protocol historical table/narrative p30](<../joi180015supp1_prod.pdf#page=30>).

**Source evidence:** 1052 unplanned PICU admissions; table Hospital Admissions55963 and narrative explicitly55963 Hospital Discharges for the two-year period.

**Reported-versus-comparator:** 18 per1000 Hospital Discharges.

**Reasoning procedure:** Yes for table/narrative same-period count/denominator; integer-rate rounding convention remains unspecified. Counts/rate are direct; nearest-rounding calculation is diagnostic, not an asserted source formatting policy.

**Calculation:** 1000 × 1052 / 55963 = 18.79813448171113. Nearest-integer rounding gives 19, not the printed 18; the difference 0.79813448171113 exceeds the 0.5 nearest-rounding tolerance. Intentional integer truncation gives 18 exactly. The package does not specify a common rate-formatting policy.

**Alternative source-grounded interpretations:** Truncating18.798 to an integer gives18 exactly. Other table rates can round ordinarily (150/55963×1000=2.68 shown3), so one consistent truncation rule is not established. Missing inputs/definitions: Intentional truncation versus nearest rounding, or an alternative eligible discharge denominator.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for displayed fraction; no percentage/rate formatting policy. Evidence-record determination: recorded_candidate, determined by registered conditional nearest-rounding discrepancy reproduced with explicit truncation alternative. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns an ambiguously formatted historical per-1000-discharge rate. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy an ambiguously formatted historical per-1000-discharge rate. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Was18 deliberately truncated, or does its source numerator/denominator differ from the displayed two-year counts?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C020 — Stat-call absolute reduction arithmetic

**Pending Human Adjudication**

**Candidate statement:** The stat-call baseline rate and relative reduction do not reproduce the printed absolute reduction within their displayed rounding precision.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN stat-call baseline/relative reduction versus absolute reduction

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** PLAN internal; P_P only; Numeric or arithmetic inconsistency; plan_material; no role ambiguity.

**Classification ambiguity:** None

**Exact source locations:** [joi180015supp1_prod.pdf — PDF p. 30; protocol p30 Stat Calls paragraph](<../joi180015supp1_prod.pdf#page=30>).

**Source evidence:** Baseline8.13 stat calls/1000 patient-days; relative reduction0.181; Poisson regression named.

**Reported-versus-comparator:** Absolute reduction1.45 calls/1000 patient-days in the same paragraph.

**Reasoning procedure:** Yes, absolute reduction=baseline rate×relative reduction for the same endpoint and rate scale. Three printed inputs and multiplication are direct/reproduced; a power-scenario mismatch is inferred.

**Calculation:** 8.13×0.181=1.47153. Printed-precision intervals8.125–8.135 and0.1805–0.1815 yield products1.4665625–1.4765025;1.45's nearest-rounding interval1.445–1.455 does not overlap.

**Alternative source-grounded interpretations:** Absolute reduction may refer to another scenario; required relative reduction1.45/8.13≈0.17835 differs from0.181 beyond its printed rounding precision. Missing inputs/definitions: Any alternate unprinted baseline/power scenario or conversion used for1.45.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for arithmetic; original power outputs not supplied and not reconstructed. Evidence-record determination: recorded_candidate, determined by reproduced product disagreement beyond printed rounding tolerance. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns incompatible stat-call power-scenario inputs. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy incompatible stat-call power-scenario inputs. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Do all three printed quantities use the same baseline and scenario, and what explains the nonoverlapping arithmetic?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C021 — Code-blue nested denominator wording

**Pending Human Adjudication**

**Candidate statement:** The code-blue absolute-reduction phrase contains two per-thousand unit cues; one denominator gives coherent arithmetic and two give a different scale.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN code-blue rate reduction versus nested printed unit

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** PLAN internal, P_P only; Measure, label, or scale inconsistency; plan_material. Unit-phrase interpretation ambiguity explicitly preserved.

**Classification ambiguity:** The second per-thousand cue may be redundant unit wording rather than an additional divisor.

**Exact source locations:** [joi180015supp1_prod.pdf — PDF p. 30; protocol p30 Code Blue paragraph](<../joi180015supp1_prod.pdf#page=30>).

**Source evidence:** Baseline0.75/1000 patient-days and relative reduction0.41.

**Reported-versus-comparator:** Absolute reduction “0.3/1000 events per thousand patient days.”

**Reasoning procedure:** Yes for dimensional unit wording; numerical0.3 alone is coherent. Both unit cues are direct; applying an additional divisor is a literal dimensional reading, not evidence the analysts actually used that divisor.

**Calculation:** 0.75×0.41=0.3075 events/1000days, which rounds0.3. Reading both printed divisors literally gives0.0003 events/1000days, a further factor1000.

**Alternative source-grounded interpretations:** Conventional redundant unit phrasing may intend one per-thousand denominator; then the numeric reduction is coherent. Missing inputs/definitions: Whether /1000 is an intentionally redundant unit cue rather than an additional division.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for arithmetic/unit reading; no need for power recalculation. Evidence-record determination: recorded_candidate, determined by the reproduced nested-unit labeling question; no erroneous power implementation is inferred. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns an extra per-thousand divisor during conversion. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy an extra per-thousand divisor during conversion. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: What single event/person-time unit is intended by this phrase?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C022 — Identity-Poisson coefficient exposure scale

**Pending Human Adjudication**

**Candidate statement:** The SAP identity-Poisson exposure columns put intercept and treatment coefficients on different scales, requiring a defined conversion before a common per-1000-day interpretation.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN SAP exposure columns versus coefficient scale description

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** PLAN SAP code versus PLAN SAP explanatory comments; P_P only; Measure, label, or scale inconsistency; plan_material. Generic coefficient-unit ambiguity remains named; no additional report discrepancy asserted.

**Classification ambiguity:** The generic rate-difference comment does not state coefficient units or post-fit conversion.

**Exact source locations:** [joi180015supp2_prod.pdf — PDF p. 3; SAP code/comments p3 lines114–131](<../joi180015supp2_prod.pdf#page=3>).

**Source evidence:** Comment names Nlin coefficient usual-care intercept and NlinG coefficient rate difference. Code defines Nlin=N/1000; GNlin=N×(Group==BedsidePEWS); BNlin=N×Baseline; model x~Nlin+GNlin+BNlin−1 with Poisson identity.

**Reported-versus-comparator:** Exposure columns scale intercept by N/1000 but treatment by N. NlinG/GNlin name reversal and EPOCH$$BNlin syntax are printed but are not registered as independent syntax candidates.

**Reasoning procedure:** Yes as a symbolic dimensional check. Any interpretation of intercept and difference on one per1000-day rate scale requires a conversion because the printed columns scale them differently. Unequal exposure scalings and exact conversion factor are direct/reproduced. Treating the comment as an already-per1000 rate difference is conditional, and no fitted reported number is alleged to have the wrong scale.

**Calculation:** Let coefficients be α,β,γ: expected x=Nα/1000+NIβ+NBγ. Dividing by N/1000 gives rate per1000days=α+1000Iβ+1000Bγ. The treatment coefficient β is per-day difference, requiring1000β for per1000days; α is per1000days.

**Alternative source-grounded interpretations:** The comment may intend β in per-day units and a later1000 conversion, or draft code may differ from implementation. The source does not explicitly state that every coefficient is already per1000days. Missing inputs/definitions: Unit intended by the generic “rate difference” comment and any production column scaling/coefficient rescaling.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for exact symbolic column scaling; actual fitted coefficients, run code, and post-fit conversions unavailable. Evidence-record determination: recorded_candidate, determined by reproduced unequal coefficient scales with the registered conditional reporting-scale question pending the named conversion definition. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a coefficient interpreted on the wrong exposure scale. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a coefficient interpreted on the wrong exposure scale. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: What units govern the Nlin/GNlin coefficients, and was the treatment coefficient multiplied by1000 before reporting per1000-day differences?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C023 — PIM upper-example display probability

**Pending Human Adjudication**

**Candidate statement:** The upper PIM example’s 99.9% differs from ordinary nearest-decimal display of the supplied inverse-logit formula, while truncation or a cap could explain it.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results PIM example versus supplied inverse-logit formula

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** REPORT within one results supplement; S_W only; Numeric or arithmetic inconsistency; statistical_results. Display-policy ambiguity explicitly preserved.

**Classification ambiguity:** The example-percentage truncation or upper-cap policy is not supplied.

**Exact source locations:** [joi180015supp3_prod.pdf — PDF p. 7; results eTable 1 p7](<../joi180015supp3_prod.pdf#page=7>) and [joi180015supp3_prod.pdf — PDF p. 13; eTable 4 footnotes b/c p13](<../joi180015supp3_prod.pdf#page=13>).

**Source evidence:** PIM score+9.7778 gives printed predicted mortality99.9%; PaO2=40 and BE=−35. The minus sign on p13 wraps at the line end; p7 also explicitly reads−35, so no sign discrepancy exists.

**Reported-versus-comparator:** Footnote b supplies inverse-logit1/(1+exp(−PIM)); minimum−8.4137 is shown as0.02%.

**Reasoning procedure:** Yes for formula/example consistency; nearest-decimal display rule is a conditional diagnostic because the source only expressly specifies nearest-integer rounding for predicted counts, not the upper example percentage. Score, formula, and printed percentage are direct; nearest rounding is a conditional diagnostic, and a display cap is a possible explanation.

**Calculation:** 100/(1+exp(−9.7778))=99.9943306823%. Nearest0.1 percentage point is100.0%, not99.9%; difference0.0943307 exceeds0.05. Lower example gives approximately0.02218%, coherent at0.02%. Score±0.00005 has negligible impact on the upper diagnostic.

**Alternative source-grounded interpretations:** Truncation to one decimal or a99.9% cap yields the printed value and avoids display100%; neither policy is stated. No interpretation of100% as actual certainty is imposed. Missing inputs/definitions: Percentage truncation/capping rule, especially whether99.9% is an intentional upper display cap.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for score/formula; full scoring coefficients are unnecessary because the given score is the input. Evidence-record determination: recorded_candidate, determined by reproduced registered conditional formula/nearest-rounding discrepancy pending the named display rule. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a differently transformed example probability. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a differently transformed example probability. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Is99.9% an intentional truncation/cap, or should the example follow another documented percentage display rule?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C024 — Overnight ICU categories and unsupported exhaustiveness

**Pending Human Adjudication**

**Candidate statement:** The displayed overnight ICU categories cover eight of ten hospitals, but their exhaustiveness and universal overnight presence are not established; the initial sum-to-ten premise is unsupported.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main hospital total versus overnight ICU category counts

**Review domain:** statistical_results

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** REPORT within main Table 1; S_W only; Denominator, proportion, or total inconsistency; statistical_results. Registered residual classification preserved; ambiguity is exhaustiveness, not roles.

**Classification ambiguity:** Exhaustiveness of the displayed overnight ICU categories and universal in-house presence are unsupported.

**Exact source locations:** [jama_parshuram_2018_oi_180015.pdf — PDF p. 5; main Table 1 p5](<../jama_parshuram_2018_oi_180015.pdf#page=5>).

**Source evidence:** BedsidePEWS10 hospitals; most senior ICU physician in-house overnight: staff2(20%), fellow5(50%), resident1(10%).

**Reported-versus-comparator:** Usual-care counts1+3+7=11. Eligibility footnote says all had pediatric ICU staff; continuous-in-house wording in footnote d is attached to the **ward** physician row, not a claim that each ICU has an in-house overnight physician.

**Reasoning procedure:** Sum-to10 is conditional on exhaustive overnight ICU categories and every hospital having an in-house overnight ICU physician. Neither is stated by the source. Displayed categories cover8/10 directly. Treating this as an exhaustive-category contradiction is an unsupported registration assumption; no staffing defect is inferred.

**Calculation:** 2+5+1=8;20+50+10=80%. The two-hospital residual is reproduced as coverage of displayed categories, but not as an established denominator contradiction. Individual percentages correctly use10.

**Alternative source-grounded interpretations:** Two hospitals may have no ICU physician in-house overnight, another category, or missing information. Having ICU staff physicians generally does not require in-house overnight presence. Missing inputs/definitions: Whether all hospitals had a most-senior in-house overnight ICU physician; categories for absence, other staffing, or missing data.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for displayed counts/percentages; no category exhaustiveness or missing/no-in-house status for two hospitals. Evidence-record determination: record_input_error, determined by unsupported category-exhaustiveness/presence assumption. The residual reporting-completeness question cannot be settled from this table. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns an unsupported exhaustive staffing-category total. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy an unsupported exhaustive staffing-category total. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: What overnight ICU presence/category or missing-data status describes the remaining two hospitals, and was the displayed list intended to be exhaustive?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C025 — Continuous-outcomes shell heading

**Pending Human Adjudication**

**Candidate statement:** The SAP’s Continuous outcomes shell heading accompanies count/rate rows and Poisson models; it may instead describe derived hospital summaries.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN SAP Continuous outcomes heading versus count/rate rows and taxonomy

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** PLAN internal; P_P only; Measure, label, or scale inconsistency; plan_material. Heading-semantics ambiguity retained.

**Classification ambiguity:** The heading may describe derived hospital rate summaries rather than modeled response distributions.

**Exact source locations:** [joi180015supp2_prod.pdf — PDF p. 5; SAP Shell Tables p5](<../joi180015supp2_prod.pdf#page=5>), [joi180015supp2_prod.pdf — PDF p. 1; binary/count taxonomy p1](<../joi180015supp2_prod.pdf#page=1>), [joi180015supp2_prod.pdf — PDF p. 2; Poisson count definition p2](<../joi180015supp2_prod.pdf#page=2>), and [joi180015supp2_prod.pdf — PDF p. 3; Gaussian individual outcomes pp3–4](<../joi180015supp2_prod.pdf#page=3>).

**Source evidence:** Shell heading Continuous outcomes precedes resuscitation calls, stat calls, urgent ICU consultations, urgent ICU admissions, ICU readmissions, and hospital readmission.

**Reported-versus-comparator:** All six rows show count/denominator expressions and Poisson; earlier SAP distinguishes count from binary outcomes and separately labels individual continuous outcomes with Gaussian models.

**Reasoning procedure:** Yes as a response-type/quantity-label check; interpretation of the heading as referring to continuous derived rates rather than modeled counts remains conditional. Heading, row formulas, and Poisson labels are direct; an inherited/unqualified heading is a possible explanation.

**Calculation:** Discrete event numerators modeled by Poisson are count responses; dividing by patient-days yields rate summaries and by discharge counts yields proportions. These summaries differ from the explicitly described patient Gaussian continuous outcomes.

**Alternative source-grounded interpretations:** Hospital rates may be treated as continuous summaries, so the heading could describe summaries instead of response distributions. It does not establish incorrect estimates. Missing inputs/definitions: Whether Continuous means hospital rate-summary variables rather than modeled outcome responses.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for printed heading, numerators/denominators, and source model taxonomy; no heading-author intent. Evidence-record determination: recorded_candidate, determined by the registered conditional heading/model-taxonomy difference reproduced with its alternative interpretation. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a different modeled response type. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a different modeled response type. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Does the heading identify derived hospital rate summaries or actual modeled response types, and what type description should readers extract?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C026 — Historical AUC endpoint scale

**Pending Human Adjudication**

**Candidate statement:** The historical AUC range prints 0.83–86, creating an extraction-scale question; an abbreviated decimal suffix could coherently mean 0.86.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN historical AUC endpoint versus AUC scale labeling

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Historical/background data inside PLAN; P_P only; Measure, label, or scale inconsistency; plan_material. Endpoint shorthand ambiguity retained.

**Classification ambiguity:** The upper endpoint may use compressed decimal-suffix notation.

**Exact source locations:** [joi180015supp1_prod.pdf — PDF p. 6; protocol p6 systematic-review paragraph](<../joi180015supp1_prod.pdf#page=6>), with probability-scale comparison supplied by [joi180015supp1_prod.pdf — PDF p. 1; protocol p1 AUC labels](<../joi180015supp1_prod.pdf#page=1>).

**Source evidence:** Printed “AUCROC 0.83-86” for adult scores distinguishing ICU from high-dependency patients.

**Reported-versus-comparator:** Same plan uses AUCROC0.91 and0.87; conventional area/probability scale is bounded0–1.

**Reasoning procedure:** Yes for explicit AUC endpoint scale, subject to abbreviated-range notation rather than literal86. Literal printed string is direct; the intended expanded endpoint is inferred, not assigned as a correction.

**Calculation:** Literal86 exceeds upper probability bound1 by85. Reading86 as the abbreviated suffix of0.86 gives a coherent0.83–0.86 range.

**Alternative source-grounded interpretations:** Compressed decimal suffix notation may intentionally mean0.86. This is a printed extraction/scale ambiguity, not evidence that the historical AUC computation was86. Missing inputs/definitions: Intended upper endpoint and whether abbreviated-decimal range notation is intentional.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for exact printed string and scale diagnostic. The cited historical review is not supplied and was not consulted. Evidence-record determination: recorded_candidate, determined by reproduced explicit-scale ambiguity in the registered AUC range. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns a literal out-of-scale AUC endpoint. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy a literal out-of-scale AUC endpoint. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Should86 be interpreted as an intentionally abbreviated0.86 endpoint, or does another scale convention apply?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C027 — Generic adjusted label versus baseline-unadjusted SCDE difference

**Pending Human Adjudication**

**Candidate statement:** The SCDE difference and interval agree across locations; generic adjusted wording does not establish baseline adjustment and may refer to hospital clustering.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main generic adjusted label versus baseline-unadjusted SCDE footnote

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** REPORT within main article; S_W only; Measure, label, or scale inconsistency; report_internal_inconsistency. Roles confirmed; residual relationship retained with explicit semantic ambiguity.

**Classification ambiguity:** Generic adjusted may mean hospital clustering rather than baseline covariates.

**Exact source locations:** [jama_parshuram_2018_oi_180015.pdf — PDF p. 1; main abstract p1](<../jama_parshuram_2018_oi_180015.pdf#page=1>), [jama_parshuram_2018_oi_180015.pdf — PDF p. 6; SCDE narrative p6](<../jama_parshuram_2018_oi_180015.pdf#page=6>), [jama_parshuram_2018_oi_180015.pdf — PDF p. 7; Table 3 footnote a p7](<../jama_parshuram_2018_oi_180015.pdf#page=7>), and [jama_parshuram_2018_oi_180015.pdf — PDF p. 5; GEE fallback explanation p5](<../jama_parshuram_2018_oi_180015.pdf#page=5>).

**Source evidence:** Abstract/narrative says adjusted between-group rate difference−0.34(−0.73,0.05)/1000 patient-days. Narrative separately explicitly calls the0.77 rate ratio baseline-adjusted.

**Reported-versus-comparator:** Table 3 footnote a says the SCDE difference model was not adjusted for baseline values. Main p4–5 states models account for hospital clustering; [jama_parshuram_2018_oi_180015.pdf — PDF p. 6; Table 2 footnote c p6](<../jama_parshuram_2018_oi_180015.pdf#page=6>) explicitly uses “adjusted for clustering by hospital.”

**Reasoning procedure:** No categorical contradiction follows unless generic adjusted is defined as baseline-adjusted. Baseline-unadjusted GEE can still account for hospital clustering; the source uses adjustment language for clustering elsewhere. Different specificity of the words is direct. Treating generic adjusted as necessarily baseline-adjusted is the unsupported registered semantic assumption.

**Calculation:** Estimate and CI are identical at all compared locations, so numerical alignment holds. Logical equivalence “adjusted = adjusted for baseline” is not supplied. The footnote excludes baseline, not cluster accounting; separate rate-ratio P=.03 is not assigned to the identity-link difference.

**Alternative source-grounded interpretations:** Adjusted refers to cluster accounting, while baseline-adjusted is reserved for the ratio; the article's own Table 2 phrasing supports this distinction. No contradiction in the printed−0.34/CI is reproduced. Missing inputs/definitions: Which adjustment dimension the abstract/narrative's generic word denotes; final output identifying variance/clustering and covariates if terminology is to be resolved.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for same-result words, footnote, and clustering framework; no local definition of generic adjusted in this SCDE sentence. Evidence-record determination: record_input_error, determined by unsupported equivalence of generic adjustment and baseline adjustment. A residual terminology question cannot be settled without the local definition; this is not a proven baseline-label contradiction. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns an unsupported baseline-adjustment status for the SCDE difference. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy an unsupported baseline-adjustment status for the SCDE difference. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Does adjusted for the−0.34 difference mean hospital clustering, and should it be explicitly qualified to prevent baseline-adjustment misclassification?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C028 — Generic adjusted label versus baseline-unadjusted physician-call difference

**Pending Human Adjudication**

**Candidate statement:** The physician-call difference and interval agree across locations; generic adjusted wording does not establish baseline adjustment and may refer to hospital clustering.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main generic adjusted label versus baseline-unadjusted physician-call footnote

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** REPORT internal; S_W only; Measure, label, or scale inconsistency; report_internal_inconsistency. No role correction; semantic ambiguity explicit.

**Classification ambiguity:** Generic adjusted may mean hospital clustering rather than baseline covariates.

**Exact source locations:** [jama_parshuram_2018_oi_180015.pdf — PDF p. 8; main Other Outcomes p8](<../jama_parshuram_2018_oi_180015.pdf#page=8>), [jama_parshuram_2018_oi_180015.pdf — PDF p. 7; Table 3 footnote a p7](<../jama_parshuram_2018_oi_180015.pdf#page=7>), and [jama_parshuram_2018_oi_180015.pdf — PDF p. 5; GEE fallback p5](<../jama_parshuram_2018_oi_180015.pdf#page=5>).

**Source evidence:** Narrative says adjusted between-group rate difference3.10(−1.92,8.11)/1000 patient-days; separate adjusted rate ratio1.17(0.73,1.88), P=.52.

**Reported-versus-comparator:** Table 3 footnote a says immediate-call-for-physician difference model was not adjusted for baseline. GEE framework accounts for center clustering; [jama_parshuram_2018_oi_180015.pdf — PDF p. 6; Table 2 footnote c p6](<../jama_parshuram_2018_oi_180015.pdf#page=6>) explicitly describes adjustment for clustering by hospital.

**Reasoning procedure:** No categorical contradiction without defining generic adjusted as baseline-adjusted. Cluster accounting does not imply baseline covariate inclusion, and baseline removal does not imply clustering removal. Words and same-result identity are direct. Inferring baseline adjustment solely from generic adjusted is an unsupported semantic alignment.

**Calculation:** Difference/CI match exactly between narrative and table. No numerator, estimate, or CI mismatch exists. The baseline-unadjusted GEE difference can coexist with an adjusted-for-clustering description; separate ratio/P value not conflated with the difference.

**Alternative source-grounded interpretations:** Adjusted denotes cluster accounting; article uses that sense elsewhere. Alternatively the narrative may intend an imprecise blanket baseline label, but source does not determine which interpretation. Missing inputs/definitions: Meaning of generic adjusted for this identity-link difference, including what clustering/variance accounting persisted after baseline removal.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. Yes for textual/result alignment and framework; no explicit local adjustment definition in the physician-call narrative. Evidence-record determination: record_input_error, determined by unsupported generic-adjusted/baseline-adjusted equivalence, with residual terminology unresolved. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns an unsupported baseline-adjustment status for the physician-call difference. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy an unsupported baseline-adjustment status for the physician-call difference. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: Which adjustment does the3.10 narrative label denote, and should the text distinguish clustering from baseline covariates?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C029 — ICU-readmission elapsed-hours label versus calendar-day cutoff

**Pending Human Adjudication**

**Candidate statement:** The literal ICU-readmission <48-hour label and third-following-midnight definition have different temporal membership; the protocol explicitly supports an intentional calendar shorthand.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main ICU-readmission hours label versus REPORT results calendar cutoff

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Confirmed primary S_C; all relationships S_C. The discrepancy is the time-window label versus operational definition across two different REPORT documents. The PLAN location corroborates and explains the calendar convention and adds no separate discrepancy relationship. Precedence P_R > P_P > S_C > S_W therefore does not change S_C. Category is Measure, label, or scale inconsistency; derived review domain is report_internal_inconsistency. Classification ambiguity: None for roles or relationship; intended label meaning remains the named human question.

**Classification ambiguity:** None for document roles or relationship. The intended hours shorthand and implemented time window remain unresolved.

**Exact source locations:** [jama_parshuram_2018_oi_180015.pdf — PDF p. 7; Main article, physical PDF p. 7, Table 3 ICU readmission row](<../jama_parshuram_2018_oi_180015.pdf#page=7>); [joi180015supp3_prod.pdf — PDF p. 6; results supplement, physical PDF p. 6, eTable 1 Unplanned ICU Readmission row](<../joi180015supp3_prod.pdf#page=6>); and [joi180015supp1_prod.pdf — PDF p. 12; protocol, physical PDF p. 12, outcome 4](<../joi180015supp1_prod.pdf#page=12>). All three were inspected as fresh direct-source page images and layout text.

**Source evidence:** Main Table 3 prints “ICU readmission <48 h” with footnote h. The intervention-period BedsidePEWS and usual-care event counts are 94 and 108, their rates are 28.40 and 21.25, adjusted between-group rate difference is 4.95 (−1.62 to 11.52), adjusted ratio is OR, 1.11 (0.77 to 1.61), and P value is .58. Footnote h states that rates are expressed per 1000 discharges from the ICU. These numbers identify the row; this candidate does not assert a numerical disagreement in them.

**Reported-versus-comparator:** Results eTable 1 prints “Re-admission before midnight of the second full calendar day after ICU discharge. Thus, re-admission occurred before the 3rd midnight following ICU discharge.” Protocol outcome 4 prints “Unplanned PICU readmission within 48 hours of PICU discharge” and expressly operationalizes that wording as before midnight of the second complete day following discharge, alternatively before the third midnight. The protocol therefore supplies an explicit source-grounded reason that hours wording may be an operational shorthand.

**Reasoning procedure:** Yes for the endpoint time-window label. A literal strict elapsed interval <48 hours and a calendar cutoff before the third following midnight are different membership rules. The ICU readmission outcome name aligns the main row with the supplement definition; the source does not require a statistical-model assumption for this comparison. Applying the same unplanned, otherwise eligible constructed readmission to both rules isolates the time condition. Direct observations are the main label, supplement definition, protocol operationalization, printed row values and rate footnote. The 70-hour membership difference is reproduced logical reasoning. Intentional shorthand and the rule actually applied to 94/108 events are possible explanations or unknown facts, not direct observations. No trial participant is asserted to have the constructed timing.

**Calculation:** Yes. On a constructed ordinary calendar week without a clock change, discharge Monday 01:00 and unplanned ICU readmission Wednesday 23:00 yield 24 + 24 + 22 = 70 elapsed hours. The first following midnight is Tuesday 00:00, the second Wednesday 00:00, and the third Thursday 00:00. Wednesday 23:00 is before Thursday 00:00 and is after 48 elapsed hours, so it satisfies the calendar condition and fails <48 hours. For this discharge, the third midnight is 71 hours after discharge. On ordinary 24-hour days, that cutoff varies approximately from 48 to 72 elapsed hours with discharge time. This is a constructed logical counterexample, not a trial event or a reanalysis.

**Alternative source-grounded interpretations:** The protocol itself names “within 48 hours” and immediately declares the third-midnight operational rule. This supports an intentional abbreviated endpoint name rather than an actual difference in event classification. The result supplement could be documenting that same convention while Table 3 compresses it to “<48 h.” The protocol explanation does not make literal <48 elapsed hours identical to the calendar rule; it supplies a possible intended meaning. No event or effect change is inferred.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. The exact label, full calendar definition, outcome identity, and temporal rule are available and sufficient to reproduce the label membership difference. Missing for an actual count or estimate comparison are patient discharge/readmission timestamps, event-level eligibility and unplanned-status classifications, final case-report/analysis implementation of the cutoff, and an explicit report-side definition of whether “<48 h” denotes literal elapsed time or the protocol's calendar shorthand. Without those inputs, neither affected events nor a revised count, rate, OR, confidence interval, or P value can be calculated. Evidence-record determination: recorded_candidate. The direct source confirms both cited statements and reproduces the registered literal-hours versus calendar-cutoff membership difference. The exact implemented endpoint and intended hours shorthand remain missing definitions as registered. No source transcription or alignment was disproven; the strong protocol shorthand alternative limits interpretation without settling the report-side label question. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns an elapsed-hours rather than calendar-day ICU-readmission endpoint. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy an elapsed-hours rather than calendar-day ICU-readmission endpoint. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: For the ICU-readmission result with intervention-period events 94/108, was the implemented endpoint literal elapsed <48 hours or the before-third-midnight calendar operationalization, and should the report's “<48 h” label be interpreted as shorthand for that calendar rule?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C030 — Hospital-readmission elapsed-hours label versus calendar-day cutoff

**Pending Human Adjudication**

**Candidate statement:** The literal hospital-readmission <48-hour label and third-following-midnight definition have different temporal membership; the protocol explicitly supports an intentional calendar shorthand.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main hospital-readmission hours label versus REPORT results calendar cutoff

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Confirmed primary S_C; all relationships S_C. The substantive comparison is a REPORT label against a different REPORT's calendar definition. PLAN protocol outcome 3 corroborates the calendar convention and supports shorthand; it is not an additional discrepancy relationship. Precedence P_R > P_P > S_C > S_W leaves S_C. Category is Measure, label, or scale inconsistency; derived review domain is report_internal_inconsistency. Classification ambiguity: None for document roles or relationship; intended label meaning remains the exact human question.

**Classification ambiguity:** None for document roles or relationship. The intended hours shorthand and implemented time window remain unresolved.

**Exact source locations:** [jama_parshuram_2018_oi_180015.pdf — PDF p. 7; Main article, physical PDF p. 7, Table 3 hospital readmission row](<../jama_parshuram_2018_oi_180015.pdf#page=7>); [joi180015supp3_prod.pdf — PDF p. 6; results supplement, physical PDF p. 6, eTable 1 Unplanned Hospital Readmission row](<../joi180015supp3_prod.pdf#page=6>); and [joi180015supp1_prod.pdf — PDF p. 12; protocol, physical PDF p. 12, outcome 3](<../joi180015supp1_prod.pdf#page=12>). All three were inspected as fresh direct-source page images and layout text.

**Source evidence:** Main Table 3 prints “Hospital readmission <48 h” with footnote c. The intervention-period BedsidePEWS and usual-care event counts are 170 and 387, their rates are 3.39 and 4.10, adjusted between-group rate difference is −0.71 (−4.92 to 3.49), adjusted ratio is OR, 0.93 (0.61 to 1.41), and P value is .74. Footnote c states that rates are expressed per 1000 patient discharges from the hospital. These values identify the row; no numerical inferential disagreement is asserted by this candidate.

**Reported-versus-comparator:** Results eTable 1 prints “Re-admission to any inpatient area in the hospital before midnight of the second day full calendar day after discharge. Thus, re-admission occurred before the 3rd midnight following hospital discharge.” The awkward “second day full calendar day” word order is present visually and was not silently normalized. Protocol outcome 3 names “Unplanned re-admission to hospital within 48 hours of hospital discharge,” then states that the outcome will be operationalized before midnight of the second day of discharge and expressly before the third midnight following discharge. The explicit third-midnight sentence is the corroborating temporal comparator; the protocol wording is not used to infer another event boundary.

**Reasoning procedure:** Yes for the endpoint time-window label. A strict <48-hour elapsed-time condition and before-third-midnight calendar condition do not have identical membership. Hospital readmission in the main row aligns with the supplement's hospital readmission definition. A constructed otherwise eligible unplanned return to an inpatient hospital area can satisfy all non-time conditions for both rules, leaving only the temporal membership comparison. Directly observed are the exact main label, supplement wording including its unusual word order, protocol operationalization, counts, rates, estimates and footnote c. The constructed 70-hour membership comparison is derived logic. Intentional shorthand, actual implementation, and whether any trial event lies between the two cutoffs remain inferred possibilities or unknown. No patient is attributed the constructed timestamps.

**Calculation:** Yes. In a constructed ordinary calendar week without a clock change, hospital discharge Monday 01:00 and unplanned hospital readmission Wednesday 23:00 give 24 + 24 + 22 = 70 elapsed hours. Following midnights are Tuesday 00:00, Wednesday 00:00, and Thursday 00:00. Wednesday 23:00 is before the third midnight Thursday 00:00 and fails the <48-hour test. The third-midnight cutoff is 71 hours after this discharge; on ordinary 24-hour days it is approximately 48–72 hours after discharge depending on discharge time. This reproduces a definition-level counterexample without claiming any actual event count difference.

**Alternative source-grounded interpretations:** The protocol explicitly treats “within 48 hours” as a name to be operationalized by the third following midnight. The Table 3 hours label may be an abbreviated name for that same outcome and the supplement may describe the implemented operational convention. This is stronger support for shorthand than a merely hypothetical explanation. It does not establish that the literal elapsed-hours reading and calendar membership are equal, and no change to an actual event or effect estimate follows from the supplied comparison.

**Mechanical evidence recheck:** Cited locations and printed source/comparator statements were directly checked. The main label, supplement calendar cutoff, matching outcome identity, and protocol operationalization suffice for the logical rule comparison. Missing for implementation and numerical consequences are patient discharge/readmission timestamps, eligibility and unplanned-event classifications, final case-report/analysis cutoff implementation, and an explicit report-side definition resolving literal elapsed <48 hours versus calendar shorthand. These missing inputs prevent identifying affected events or calculating changes to 170/387 counts, rates, differences, ORs, intervals, or P values. Evidence-record determination: recorded_candidate. Fresh direct-source reading confirms the registered label and operational definition, including the supplement's awkward wording, and reproduces the literal-hours/calendar membership difference. The implementation and label meaning remain the registered unresolved definitions. No transcription or source alignment is disproven. Protocol-supported shorthand is an alternative interpretation, not proof that the literal label denotes the same elapsed-time set. The suggested review disposition is solely a mechanical pre-fill for human review.

**Quality-control relevance:** This comparison concerns an elapsed-hours rather than calendar-day hospital-readmission endpoint. It warrants the precise human question below within the quantitative reporting scope; unresolved conventions and unsupported inputs limit what can be concluded.

**Potential downstream evidence impact:** If human review confirms a preventable reporting defect, a data extractor, systematic review, or meta-analysis could copy an elapsed-hours rather than calendar-day hospital-readmission endpoint. No propagation, effect-estimate change, conclusion change, or serious harm is established by this record.

**Human verification steps:** Open each linked physical source page; match the outcome, population, period, model and units before applying the stated rule. Reproduce the calculation or logical comparison, examine the source-grounded alternative, and obtain the named missing definitions or implementation evidence. Exact remaining question: For the hospital-readmission result with intervention-period events 170/387, did event classification use literal elapsed <48 hours or the before-third-midnight calendar rule, and what quantitative time window should a data extractor take from the “<48 h” label?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

# Downstream Evidence-Chain Considerations

If confirmed, even small preventable transcription, boundary, label, or unit defects can be copied into a systematic-review extraction sheet, meta-analysis, guideline evidence table, or later publication. The cards name the specific quantity or definition at risk of being copied. This is a conditional possibility. The package provides no evidence that copying occurred, that an estimate changed downstream, or that the trial’s conclusion changed.

An extraction decision should preserve distinctions between historical PLAN quantities and trial REPORT results, counts and rates, patient and discharge denominators, model families and effect scales, clustering and baseline adjustment, and elapsed-hour versus operational calendar windows. Input-error records particularly require clarification of the assumed comparison basis before treating them as reporting defects. Human resolution of a shorthand or formatting policy may settle a card without establishing a numeric error.

# Limitations and Missing Definitions

The review is limited to the four supplied aggregate PDFs. No patient-level raw records, executed production models, plotting code, exact unrounded prediction sums, covariance/test outputs, or complete operational revision history is supplied. Per-card questions name missing definitions: figure encodings and axis scope; intended extrema; power versus census bed basis; historical cohort periods, exact denominators and rounding; endpoint boundaries and conjunction; scope of ICU rate wording; final denominator/model history; patient-versus-discharge prediction aggregation; coefficient rescaling; PIM cap/truncation; overnight category exhaustiveness; shell-heading meaning; AUC shorthand; adjustment dimension; and implemented readmission cutoff/timestamps.

The five input-error records correct unsupported same-basis, same-cohort, exhaustive-category, or generic-to-baseline assumptions. Conditional arithmetic does not establish those assumptions. Nearest-rounding diagnostics in C018/C019/C023 are bounded by absent exact-input or display-policy definitions. C021/C022/C025/C026 retain plausible unit, coefficient, summary-type, or decimal shorthand interpretations. C029/C030 are constructed temporal comparisons on ordinary 24-hour days without clock changes, supported by a strong protocol shorthand alternative; neither actual patient events nor changed counts or model effects can be inferred.

Historical derivative engines are partly unrecorded. OCR and Office conversion are unavailable, but no supplied unit needed either: all 69 pages were completely mapped using usable text or images and exact candidate source confirmation. The configured coordinator model and interactive launch are distinguished from unavailable independent runtime/launch attestation. The explicit current-provider instruction differs from the original validator’s literal provider requirement. These provenance limits create no scientific coverage gap. Full limitations are recorded in [limitations.md](review_1_6/limitations.md).

# Human Adjudication Checklist

1. Verify each candidate’s source page, printed value, comparator, population, time period, model, scale, and denominator.
2. Reproduce only the supplied rule or the explicitly conditional diagnostic; consider alternatives and missing definitions before drawing a conclusion.
3. Obtain implementation/version evidence where the printed comparison alone cannot identify intended meaning or numerical consequences.
4. Decide whether the observation is a reporting defect and whether a correction or clarification is appropriate; record the reviewer’s assessment, importance, action, initials, and notes in the blank card fields.
5. Treat suggested dispositions as mechanical starting values, resolve every stable ID, and retain a documented reason for the human decision.
6. Keep any confirmed reporting correction separate from claims about trial conclusions or downstream consequences, which require their own evidence.

# Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

The source hashes were recorded before scientific work. Both hash sets were recomputed after Markdown assembly: all four direct sources and 65 reused assets are unchanged, and the before/after hash files are byte-identical. Recomputed records: [source hashes after review](review_1_6/source_hashes_after.sha256) and [reused-asset hashes after review](review_1_6/reused_artifact_hashes_after.sha256). Local integrity logs, tooling cleanup status, and the final machine-readable validation records preserve the completion evidence. HTML rendering and validation follow final Markdown assembly.

| Source file | SHA-256 before review |
|---|---|
| jama_parshuram_2018_oi_180015.pdf | 92c3a3edd598a1073e39f8d0733352b3aea3bec30731b9ef0326e68f2e6088ba |
| joi180015supp1_prod.pdf | 67409a1493b032cb49b26a4444e37eabeb2a432d2d0b5576914baac310490306 |
| joi180015supp2_prod.pdf | 6dab9fdc7fa6ca0da2031d5a483a58ba8ad9a3b0c6c4e7c45eb17708535465a4 |
| joi180015supp3_prod.pdf | 3b58616d0af25610fe9e4bab11ac42c7e38dae588e3d965ec306b8e5b55d1eb3 |

Direct tools: Poppler `pdfinfo`, `pdftotext`, `pdftoppm`, and `pdftocairo` 25.03.0, local SHA-256 tools, and Pandoc 3.1.11.1; CPU only. Targeted fresh layout and page-image derivative commands, pages, resolution, and engines are recorded in the [tooling record](review_1_6/tooling_record.md), [asset inventory](review_1_6/evidence_asset_inventory.md), and [recheck](review_1_6/verification/evidence_recheck.md). No fallback environment or package installation was needed; fallback state is NOT_NEEDED and removal state NOT_CREATED.

## Agent execution and routing provenance

The [execution manifest](review_1_6/agent_execution_manifest.md) records every actual agent, including the coordinator and report generator, once. Identifiers omit the leading slash solely for the validator’s alphanumeric-first grammar; prepending `/` restores the exact canonical runtime task path returned by the collaboration tool. Opaque runtime UUIDs are not exposed. The coordinator row is its package-configured `gpt-6.1-sol` / `high` contract, not independently attested runtime model identity. Named specialist pairs are tool-defined. All mandatory specialist stages used distinct fresh agents; the appended recheck is an additional fresh agent.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/stats1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_rechecker | root/recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/stats2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_rechecker_append | root/recheck_append | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/evidence_recheck_append.md |
| quality_control_auditor | root/audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

[Routing preflight](review_1_6/routing_preflight.md) records PASS, successful coordinator and specialist inference, and all nine named presets. It discloses that independent coordinator runtime-model and interactive-launch attestation are unavailable. Provider follows the user’s explicit current-session override. No credentials or provider configuration were changed.

The [provider override record](review_1_6/provider_override.md) documents a copy of the supplied validator whose sole adaptation is the expected provider literal. The original helper remains unchanged. Both machine-readable outcomes are preserved: [original provider-contract result](review_1_6/review_validation_original_provider_contract.json) and [current-provider-compatible validation result](review_1_6/review_validation.json). The original provider literal is openrouter; the user-authorized preflight instead records current-session-provider. All scientific, evidence, coverage, classification, and integrity checks are identical. A provider-compatible PASS is distinct from an unqualified PASS of the original provider contract and must be read with the disclosed runtime-attestation limitations.

## Reproducibility performance

The following exact performance fields match [run_state.md](review_1_6/run_state.md), finalized immediately after complete Markdown assembly. Elapsed time covers inventory, full mapping, checking, both statistical passes, all recheck waves, audit, and complete evidence-card assembly. Final source-integrity recomputation is complete; HTML rendering, cleanup, and validation follow final Markdown assembly. The target is a planning range, never a coverage or candidate boundary.

- **Target basis:** Four unencrypted PDFs with 69 physical pages; complete reusable native/layout text plus 53 existing rendered pages remove bulk preprocessing. Scope includes 37 protocol pages, a seven-page SAP, two results figures and several hospital/patient tables requiring visual checks; two disjoint mapping lanes, three concurrent checkers, both statistical passes, full recheck, audit, and report generation remain mandatory. This target reflects reusable coverage and relationship complexity, not page count alone.
- **Total source units:** 69
- **Fresh-source units:** 0
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-10-11T00:43:40Z
- **Finished UTC:** 2026-10-11T01:26:39Z
- **Observed elapsed minutes:** 42.98
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Additional pass-2 discovery required a distinct fresh two-ID exact-source recheck wave on three pages and propagation through the full 30-ID audit/report. Complete 112-relationship two-pass coverage and full 30-card assembly took longer than the reuse-based planning estimate; no coverage or candidate was omitted.
