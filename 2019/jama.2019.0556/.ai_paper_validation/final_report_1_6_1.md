# Quantitative Reporting Quality-Control Consistency Review — MooDFOOD Trial

**Workflow 1.6.1 · Pending Human Adjudication**

All five stable candidates require human adjudication. Mechanical reproduction, inclusion screening, and independent inclusion audit are distinct records; none supplies a human disposition. The two candidates whose inclusion the auditor questioned remain fully documented.

# Executive Quality-Control Summary

Complete review of five supplied PDFs, comprising 102 physical pages, produced five stable candidates, C001–C005. Eight independently screened findings were consolidated into these five issues. All five concern planned versus reported design or analysis and have review domain `protocol_report`, primary relationship `P_R`, and evidence state `reproduced`. The independent audit recorded `CONFIRMED` for C001–C003 and `QUESTIONED` for C004–C005.

The candidates concern daily EPA+DHA dose, primary-MDD model priority and Cox prespecification, the unavailable planned additive-interaction sensitivity, IDS endpoint placement, and distinct power assumptions and contrasts. For the latter two, source-grounded contextual interpretations may resolve the comparison: broad protocol terminology for IDS and coexisting interaction/main-effect powering calculations. Their stable IDs are retained transparently. No candidate establishes a change to a reported treatment estimate or a paper-level conclusion.

# Package and Reused-Evidence Provenance

The package reports the MooDFOOD randomized trial of multinutrient supplementation and food-related behavioral activation for prevention of major depressive disorder (MDD). Source roles follow content. A prospective protocol or SAP remains `PLAN` even when supplied as a numbered supplement.

| Source ID | Actual source filename | Content and role | Physical pages |
|---|---|---|---:|
| DOC-001 | [jama_bot_2019_oi_190007.pdf](../jama_bot_2019_oi_190007.pdf#page=1) | Main trial article; REPORT | 11 |
| DOC-002 | [joi190007supp1_prod.pdf](../joi190007supp1_prod.pdf#page=1) | Protocol version 7, July 11, 2017, with final amendments; PLAN | 60 |
| DOC-003 | [joi190007supp2_prod.pdf](../joi190007supp2_prod.pdf#page=1) | Prevention-trial analysis plan; PLAN | 5 |
| DOC-004 | [joi190007supp3_prod.pdf](../joi190007supp3_prod.pdf#page=1) | Supplementary results and contextual methods; REPORT | 25 |
| DOC-005 | [joi190007supp4_prod.pdf](../joi190007supp4_prod.pdf#page=1) | Published data-sharing statement; REPORT | 1 |
| Total | Five supplied PDFs | No supplied Office, workbook, CSV, or individual-level data source | 102 |

The [asset inventory](review_1_6_1/evidence_asset_inventory.md) records 267 reused source-linked assets: 142 USABLE, 84 DUPLICATE, and 41 PARTIAL; none selected was STALE or UNREADABLE. Native/layout text, CPU OCR locators, rendered pages, and source-location metadata were reused. Overlapping derivatives count once toward page coverage. Partial image-heavy results text on DOC-004 pp.16–23 is backed by readable full-page images. Preserved plain text covers pages omitted from an older selected-page manifest. These assets supported fresh discovery; prior candidate selections, screening decisions, dispositions, and reports were not scientific inputs.

Direct supplied sources remain the evidence authority. Poppler 26.01.0 text extraction and targeted rendering confirmed candidate locations. Older text/render engines include PyMuPDF and Tesseract CPU OCR; optional preserved targeted-image engine metadata is incomplete, but direct current-source confirmation closes that provenance limitation for registered evidence. No web or external literature was used.

# Scope, Complete Coverage, and Exclusions

Scope comprises counts and denominators; estimate and test logic; statistical method logic; and planned versus reported statistical design under [QUALITY_CONTROL_SCOPE.md](../QUALITY_CONTROL_SCOPE.md). Every supplied source unit was mapped, including covers, references, administrative pages, and figures. The [source-coverage ledger](review_1_6_1/source_coverage.md) reconciles as follows.

| Source ID | Unit type | Total | Reusable | Fresh-required | Mapped | Status |
|---|---|---:|---:|---:|---:|---|
| DOC-001 | PDF_PAGE | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 | PDF_PAGE | 60 | 60 | 0 | 60 | COMPLETE |
| DOC-003 | PDF_PAGE | 5 | 5 | 0 | 5 | COMPLETE |
| DOC-004 | PDF_PAGE | 25 | 25 | 0 | 25 | COMPLETE |
| DOC-005 | PDF_PAGE | 1 | 1 | 0 | 1 | COMPLETE |
| Total | PDF_PAGE | 102 | 102 | 0 | 102 | COMPLETE |

Zero fresh-required extraction units means reusable evidence was available for every page; it does not mean that scientific mapping or direct-source confirmation was omitted. Fresh main and support mappers had disjoint, exhaustive scopes. The [coverage manifest](review_1_6_1/coverage_manifest.md) records each stage and each artifact separately.

Display rounding, display-zero P values, obvious notation, context-resolved wording, model-based versus crude contrasts, conditional observations, and peripheral comparisons were excluded under the prescribed rules. Broad methodology, clinical, novelty, misconduct, raw-data, and preferred-analysis reviews are outside scope. No expected candidate count or elapsed-time target restricted discovery.

# Quantitative and Statistical Relationship Coverage

The [numeric inventory](review_1_6_1/relationships/numeric_relationship_inventory.md) contains 51 relationships: N001–N029 and N100–N121. The [statistical inventory](review_1_6_1/statistics/relationship_inventory.md) contains 77 relationships: S001–S032 and S050–S094. Numbering separates mapper scopes; gaps in numeric sequences are not uncovered registered relationships. Cross-source review covered XS-G01–XS-G36, 36 matched comparison groups.

Numeric review covered counts, denominators, totals, rates, dispersion, display precision, and effect-measure identity. Statistical coverage included primary ORs/HRs, all 16 main secondary estimates, eight standardized effects, 39 nonreference moderation/adjustment coefficients, 24 no-imputation result cells, eight CACE estimates, and applicable prospective specifications. Matching respected population, time, contrast, scale, model, and adjustment.

Two different fresh `gpt-6.1-sol/high` specialists reviewed all 77 statistical relationships. Both `PASS_1_COMPLETE` and `PASS_2_COMPLETE` records are present for every relationship. Pass 2 used the complete ledger, initial screen, and recheck facts and emitted no new finding; consequently no pass-2 inclusion screen or appended ID was needed. Missing model-specific covariance, degrees of freedom, or fitted inputs limit exact numerical reconstruction where stated, rather than leaving relationships unchecked.

# Inclusion Screening Summary

An issue qualifies only if reproduced from supplied evidence, within focus, unresolved at once by a statistically literate reader from immediate context, and capable of changing interpretation or extraction of a named result. The [screening log](review_1_6_1/screening/inclusion_screen.md) has one initial decision per finding.

| Decision or consolidation measure | Count |
|---|---:|
| Findings screened | 8 |
| INCLUDE — MEETS_THRESHOLD | 8 |
| SCREENED_OUT | 0 |
| Consolidated stable candidates | 5 |

| Screened-out reason code | Finding rows |
|---|---:|
| NOT_REPRODUCED | 0 |
| ROUNDING_OR_DISPLAY_PRECISION | 0 |
| NOTATION_OR_TYPOGRAPHY | 0 |
| TERMINOLOGY_OR_WORDING | 0 |
| MODEL_VERSUS_CRUDE | 0 |
| CONTEXT_RESOLVES | 0 |
| CONDITIONAL_OR_UNREPORTED | 0 |
| PERIPHERAL_COMPARISON | 0 |
| OUT_OF_FOCUS | 0 |
| DUPLICATE_OF_INCLUDED | 0 |
| Total SCREENED_OUT finding rows | 0 |

The eight finding rows comprise five cross-source and three statistical-pass-1 findings; numeric and pass-2 checkers emitted none. Three overlapping pairs share stable IDs while retaining both included provenance rows. Checker self-screening observations are separate from finding-screening decisions: 18 numeric, 21 cross-source, 28 pass-1, and 32 pass-2 excluded-observation rows total 99, all independently audited. They are neither 99 additional findings nor report cards. The audit reconciled pass-1's S067 exclusion to already included C003, which covers an explicit unconditional primary-outcome analysis commitment, rather than an arbitrary missing detail; no additional finding or candidate count results.

The [quality audit](review_1_6_1/quality/evidence_quality_audit.md) confirmed inclusion for three stable issues and questioned it for two. It did not rewrite initial INCLUDE decisions or delete stable IDs. Those audit assessments and their reasons appear in the index and cards.

# Review-Domain Summary

`statistical_results` covers counts, estimates, tests, and statistical method logic in REPORT content. `report_internal_inconsistency` covers REPORT disagreement about attribution of a result. `protocol_report` covers REPORT versus PLAN statistical design/analysis comparisons. `plan_material` covers statistical-design inconsistencies solely within PLAN content. These are review categories, not adjudications.

| Review domain | Candidates |
|---|---:|
| statistical_results | 0 |
| report_internal_inconsistency | 0 |
| protocol_report | 5 |
| plan_material | 0 |
| Total | 5 |

| Primary relationship type | Candidates |
|---|---:|
| P_R | 5 |
| P_P | 0 |
| S_C | 0 |
| S_W | 0 |
| Total | 5 |

C002 and C004 also involve P_P; precedence P_R > P_P > S_C > S_W assigns their primary type P_R. Their additional relationships do not create additional candidates.

| Evidence state | Candidates |
|---|---:|
| reproduced | 5 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| Total | 5 |

| Inclusion audit | Candidates |
|---|---:|
| CONFIRMED | 3 |
| QUESTIONED | 2 |
| Total | 5 |

# Candidate Index

| Stable ID | Candidate | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| C001 | Planned and reported daily EPA+DHA dose | protocol_report | P_R | reproduced | CONFIRMED |
| C002 | Primary MDD model priority and Cox prespecification | protocol_report | P_R | reproduced | CONFIRMED |
| C003 | Planned additive-interaction sensitivity not reported | protocol_report | P_R | reproduced | CONFIRMED |
| C004 | IDS endpoint hierarchy across protocol, SAP and report | protocol_report | P_R | reproduced | QUESTIONED |
| C005 | Primary MDD power assumptions and contrasts | protocol_report | P_R | reproduced | QUESTIONED |

# Candidate Evidence Cards

## C001 — Planned and reported daily EPA+DHA dose

**Pending Human Adjudication**

**Candidate statement:** The protocol explicitly defines intended EPA+DHA as 1.0 g/day, while both reported intervention descriptions define 1412 mg/day for the same one-year randomized supplement regimen; the supplied formulation/tolerance context does not reconcile these masses.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol pp.8,18,20,23 vs REPORT main pp.1,2 and results supplement pp.4,5

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002

**Classification rationale:** Protocol content is PLAN and main/supplementary results are REPORT. The REPORT dose occurrences agree, so no S_C relationship exists. Tolerance and version context do not establish another plan-internal inconsistency.

**Classification ambiguity:** Formulation amendment chronology and the detailed tolerance-component definition are not supplied.

**Exact source locations:** Protocol [p.1 cover/version](../joi190007supp1_prod.pdf#page=1), [p.8 summary](../joi190007supp1_prod.pdf#page=8), [p.18 §5.1 treatment](../joi190007supp1_prod.pdf#page=18), [p.20 composition/tolerance box](../joi190007supp1_prod.pdf#page=20), and [p.23 omega-3 intended dose](../joi190007supp1_prod.pdf#page=23); main [p.1 Interventions](../jama_bot_2019_oi_190007.pdf#page=1), [p.2 Multinutrient Supplements](../jama_bot_2019_oi_190007.pdf#page=2); results [p.4 eAppendix 2](../joi190007supp3_prod.pdf#page=4), [p.5 composition testing](../joi190007supp3_prod.pdf#page=5). The affected primary estimate is in main [p.6 Table 2](../jama_bot_2019_oi_190007.pdf#page=6).

**Source evidence:** Protocol pp.8/18 specify omega-3 1000 mg per capsule and EPA/DHA ratio 3:1; p.23 expressly defines EPA+DHA = 1.0 g per day. Protocol p.20 permits manufacturing deviation 90%–125% and references C1.2. Main p.2 and results p.4 explicitly give 1412 mg EPA and DHA, ratio 3:1, in one capsule plus one vitamin/mineral pill daily for one year. Results p.5 gives EPA 67.9 g/100 g FAME (SD 0.85), DHA 14.6 g/100 g FAME (SD 1.55), and selenium average 30 micrograms (SD 0.4); these laboratory fractions are not daily-dose masses. The protocol cover identifies version 7 with final amendments without mapping a formulation change.

**Reported-versus-comparator:** REPORT EPA+DHA 1412 mg/day versus PLAN EPA+DHA 1000 mg/day; duration and daily regimen match.

**Reasoning procedure:** Match the explicit active EPA+DHA mass, daily frequency, and duration; convert g to mg; apply the printed tolerance generously to that mass; allow half-unit rounding intervals. Do not reconstruct dose from FAME fractions.

**Calculation:** 1.0 g = 1000 mg; 1412 − 1000 = 412 mg/day, 41.2% of nominal planned dose. Nominal upper tolerance gives 1000 × 1.25 = 1250 mg, 162 mg below 1412 mg. Conservatively, 1.0 g permits [950,1050) mg, and integer 125% permits an upper 125.5%; even 1050 × 1.255 = 1317.75 mg remains below the reported lower display bound 1411.5 mg. Display precision cannot bridge the gap even under this generous tolerance interpretation.

**Affected result or extracted value:** Intervention EPA+DHA dose attached to the primary multinutrient MDD OR 1.06 (95% CI 0.87–1.29). The reported OR is not numerically challenged.

**Why context does not resolve it:** Explicit EPA+DHA definitions prevent immediate resolution as capsule oil versus active fatty acids. The reported 1412-mg regimen itself is clear; its relationship to the supplied intended 1.0-g regimen is not documented, and ordinary manufacturing tolerance does not bridge it.

**Alternative source-grounded interpretations:** A delivered formulation revision or retained preliminary-dose wording could explain the comparison. The referenced C1.2 composition document is not separately supplied. Formulation history and tolerance applicability remain missing definitions; neither an amendment nor a laboratory daily-dose conversion is inferred.

**Mechanical evidence recheck:** Direct-source text and targeted visual confirmation matched every occurrence and reproduced the conservative tolerance/precision comparison. No candidate-affecting transcription or page correction was needed; state `reproduced`.

**Potential downstream evidence impact:** If confirmed, an evidence extractor using the protocol could attach 1000 mg/day while one using the reported intervention could attach 1412 mg/day to the same trial estimate. No propagation, clinical effect, or conclusion change is established.

**Human verification steps:** Read the linked dose definitions and tolerance box; obtain the referenced formulation specification or amendment chronology if available. Ask what documented formulation history reconciles planned EPA+DHA 1.0 g/day with reported 1.412 g/day.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Primary MDD model priority and Cox prespecification

**Pending Human Adjudication**

**Candidate statement:** The protocol assigns time-to-event/Cox methods to primary-study-parameter analysis, whereas SAP/report prioritize cumulative-MDD logistic regression; independently, the SAP explicitly plans secondary Cox time-to-onset analysis that the report repeatedly designates post hoc.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN protocol p.43 vs PLAN SAP pp.3,4 and REPORT main pp.1,2,4,6,7

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003, F-ST1-002

**Classification rationale:** The substantive protocol/SAP priority comparison is P_P; protocol/report priority and SAP/report Cox status are P_R. P_R takes precedence. Clearly attributed REPORT ORs and HRs do not create an S_W conflict.

**Classification ambiguity:** Operative SAP date/version, prospective amendment chronology, and any narrower implementation meant by post hoc are unavailable.

**Exact source locations:** Protocol [p.43 §§10.1/10.2](../joi190007supp1_prod.pdf#page=43); SAP [p.3 Fourth analysis](../joi190007supp2_prod.pdf#page=3), [p.4 Secondary analysis](../joi190007supp2_prod.pdf#page=4); main [p.1 Main Outcome and Measures/Results](../jama_bot_2019_oi_190007.pdf#page=1), [p.2 Study Design](../jama_bot_2019_oi_190007.pdf#page=2), [p.4 Outcomes/Statistical Methods](../jama_bot_2019_oi_190007.pdf#page=4), [p.6 Table 2](../jama_bot_2019_oi_190007.pdf#page=6), and [p.7 Onset of MDD](../jama_bot_2019_oi_190007.pdf#page=7).

**Source evidence:** Protocol §10.1 specifies Kaplan–Meier/log-rank/Cox for MDD time-to-event, two-way/four-way intervention comparisons, and mixed regression for MDD/IDS. SAP p.3 specifies primary logistic new-MDD regression with effect-coded interventions and interaction; p.4 specifies secondary Cox onset analysis with HRs, intervals, and P values. Main p.4 calls time-to-MDD/Cox post hoc, and Table 2 labels the onset outcome Post Hoc. Main p.2 points to both supplied plans. Table 2 and p.7 report supplement/therapy/interaction primary ORs 1.06 (0.87–1.29), 0.93 (0.76–1.13), 0.93 (0.76–1.14), with P=.57/.47/.48, and Cox HRs 1.05 (0.86–1.27), 0.91 (0.75–1.10), 0.91 (0.75–1.11), with P=.65/.32/.36.

**Reported-versus-comparator:** REPORT primary logistic and post hoc Cox versus PLAN protocol primary-study-parameter time-to-event/mixed methods and SAP primary logistic/planned secondary Cox.

**Reasoning procedure:** Match cumulative MDD versus time-to-onset, producing model, intervention contrast, and prospective status. Compare analysis hierarchy/status rather than requiring ORs and HRs to equal one another.

**Calculation:** This is a logical status comparison. Repeated two-decimal estimates, interval limits, and P values agree within their half-unit intervals; ±0.005 display allowance cannot change planned-secondary versus post-hoc designations. No estimate, CI, or P value fails a stated numeric rule in this card.

**Affected result or extracted value:** Prospective primary-model metadata and, especially, planned-supporting versus post-hoc status of the three Cox HRs 1.05/0.91/0.91. The producing model of each result is clear.

**Why context does not resolve it:** SAP supersession could reconcile primary logistic priority, but does not alone reconcile the SAP's own explicit secondary Cox provision with the report's repeated post hoc label. Onset/censoring visits and proportional-hazard checking are described without identifying a narrower implementation as the reason for that status.

**Alternative source-grounded interpretations:** SAP could refine the protocol prospectively, or post hoc could refer to a narrower later Cox implementation. Neither chronology nor that narrower distinction is established in the supplied package. No analytical decision timing is inferred.

**Mechanical evidence recheck:** Direct-source readings matched all cited model/status statements and results; SAP p.4 and protocol p.43 were visually confirmed. The planned-secondary/post-hoc comparison remains; no transcription correction or classification change was required.

**Potential downstream evidence impact:** If confirmed, an extractor could record a matched onset HR as post hoc rather than prospectively planned supporting evidence. No preferred model, changed treatment estimate, bias, or conclusion change is asserted.

**Human verification steps:** Compare protocol §10.1, the SAP's primary/secondary specifications, and every report post hoc label. Ask which hierarchy operated prospectively and what exact version, decision, or implementation distinction reconciles the planned secondary Cox analysis with its post hoc designation.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Planned additive-interaction sensitivity not reported

**Pending Human Adjudication**

**Candidate statement:** The SAP unconditionally specifies primary-MDD additive-interaction sensitivity using RERI and a likelihood-based 95% CI; the complete supplied REPORT union contains no matching additive estimate/CI or documented reconciliation.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP p.4 vs REPORT main pp.1,4,6,7,8 and results supplement pp.21,22, with complete REPORT coverage

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-005

**Classification rationale:** PLAN SAP is compared with the complete REPORT result union. REPORT locations jointly establish reporting scope and do not conflict with one another, so no S_C/S_W relationship is added.

**Classification ambiguity:** Whether the additive analysis was actually conducted is outside the supplied evidence.

**Exact source locations:** SAP [p.4 primary-outcome interaction section](../joi190007supp2_prod.pdf#page=4); main [p.1 combination Results](../jama_bot_2019_oi_190007.pdf#page=1), [p.4 Statistical Methods](../jama_bot_2019_oi_190007.pdf#page=4), [p.6 Table 2](../jama_bot_2019_oi_190007.pdf#page=6), [p.7 Onset of MDD](../jama_bot_2019_oi_190007.pdf#page=7), [p.8 sensitivity analyses](../jama_bot_2019_oi_190007.pdf#page=8); results [p.21 eAppendix 11](../joi190007supp3_prod.pdf#page=21), [p.22 eAppendix 12](../joi190007supp3_prod.pdf#page=22). Full bounded absence scope: main physical pp.1–11 (linked [first](../jama_bot_2019_oi_190007.pdf#page=1)/[last](../jama_bot_2019_oi_190007.pdf#page=11)); results pp.1–25 ([first](../joi190007supp3_prod.pdf#page=1)/[last](../joi190007supp3_prod.pdf#page=25)), including visually checked [p.17 trajectories](../joi190007supp3_prod.pdf#page=17); data-sharing [p.1](../joi190007supp4_prod.pdf#page=1).

**Source evidence:** SAP specifies additional additive-interaction sensitivity via RERI from a linear odds-ratio model, likelihood-based 95% CI, and lowest-assumed-risk joint-reference recoding. This promise follows speculative biological rationale but is not conditional on significant multiplicative interaction. Main reports logistic interaction OR 0.93 (0.76–1.14), P=.48, and Cox interaction HR 0.91 (0.75–1.11), P=.36. Main p.8 and results pp.21/22 give other sensitivities: no-imputation secondary coefficients and CACE, including MDD therapy OR 0.78 (0.64–0.95) and supplement OR 0.84 (0.67–1.07). Results p.17 contains secondary symptom/utility trajectories; the data-sharing statement supplies access terms rather than additional results.

**Reported-versus-comparator:** PLAN additive primary-MDD RERI/CI commitment versus REPORT multiplicative interaction and other named sensitivities, with no matching additive result located throughout all 37 supplied REPORT pages.

**Reasoning procedure:** Read the unconditional plan commitment; inspect all REPORT pages and maps; search RERI, additive/additivity, biological interaction, linear odds, likelihood-based, interaction, and sensitivity; examine matches in context and image-only displays. Distinguish a planned primary-outcome analysis reporting absence from an arbitrary requested detail.

**Calculation:** The comparison is logical and bounded by complete supplied REPORT coverage. Multiplicative interaction OR/HR does not identify the distinct planned additive estimand. Repeated printed estimates reconcile within half-unit precision. No RERI is reconstructed from crude counts because model parameters, covariance, joint recoding, and likelihood-CI inputs are unavailable; rounding cannot supply an absent estimand.

**Affected result or extracted value:** Completeness and additive-scale interpretation of combined-intervention primary-MDD evidence; the planned RERI and its likelihood-based 95% CI are unavailable for extraction.

**Why context does not resolve it:** Neither reported multiplicative interaction nor secondary no-imputation/CACE estimates provide the SAP's named additive-departure result. No supplied passage identifies replacement, deferral, or a reporting decision. This is an explicit primary-outcome design commitment, not a preferred additional analysis.

**Alternative source-grounded interpretations:** The analysis could have been conducted but omitted from supplied results, or prospectively replaced/deferred. No such event is demonstrated. The absence statement is restricted to the supplied REPORT union and does not assert that the analysis was unperformed or what its result would be.

**Mechanical evidence recheck:** Independent full-document direct-source text, contextual searches, complete maps, and visual inspection of results p.17 confirmed the positive matches and full bounded absence. State `reproduced`; no source/page correction was needed.

**Potential downstream evidence impact:** If confirmed, an evidence synthesis seeking additive combined-intervention evidence cannot extract the promised RERI/CI from this package. No significance, direction, propagation, or conclusion reversal for the unavailable analysis is known.

**Human verification steps:** Read SAP p.4 and all linked reported interaction/sensitivity outputs; verify the 37-page reporting union. Ask where the planned primary-MDD RERI/likelihood-based CI or its documented reconciliation is available. Do not infer analysis execution from absence alone.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — IDS endpoint hierarchy across protocol, SAP and report

**Pending Human Adjudication**

**Candidate statement:** IDS appears under the protocol's main-endpoint and primary-study-parameter headings while SAP/report explicitly classify it secondary; the independent audit questions whether this is substantive hierarchy rather than context-resolved broad terminology.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN protocol pp.9,28,43 vs PLAN SAP p.2 and REPORT main pp.4,8

**Evidence state:** reproduced

**Inclusion audit:** QUESTIONED
The protocol's p.14 secondary-objectives paragraph includes depressive symptom scores, and broad main/primary-study-parameter headings do not establish formal co-primary/key status. The explicit SAP/report secondary hierarchy supplies a coherent terminology/refinement interpretation; under the scope's doubt rule, not-resolved-by-context inclusion is not securely established.

**Finding IDs:** F-XS-004, F-ST1-003

**Classification rationale:** Protocol/SAP placement comparison is P_P and protocol/report placement comparison is P_R; P_R takes precedence. SAP/report secondary agreement creates no additional conflict. The numerical result reconciles and is not the candidate basis.

**Classification ambiguity:** Formal co-primary/key hierarchy and chronology are not established; broad protocol terminology and the protocol's secondary symptom-objective context may resolve the comparison.

**Exact source locations:** Protocol [p.9 main-endpoint summary](../joi190007supp1_prod.pdf#page=9), [p.14 §2 Secondary Objective, contextual evidence](../joi190007supp1_prod.pdf#page=14), [p.28 §§8.1.1/8.1.2](../joi190007supp1_prod.pdf#page=28), [p.43 §§10.1/10.2](../joi190007supp1_prod.pdf#page=43); SAP [p.2 Outcomes](../joi190007supp2_prod.pdf#page=2); main [p.4 Secondary Outcomes/Statistical Methods](../jama_bot_2019_oi_190007.pdf#page=4), [p.8 Table 3/IDS narrative](../jama_bot_2019_oi_190007.pdf#page=8).

**Source evidence:** Protocol pp.9/28 list IDS depressive symptomatology at baseline,3,6,12 months as a main study parameter; p.43 places its mixed-regression analysis in Primary study parameter(s), separate from PHQ-9/other secondary parameters. SAP p.2 explicitly lists IDS30-SR at T3/T6/T12 as secondary. Main p.4 calls IDS secondary and secondary analyses exploratory because of multiple comparisons. Crucially, protocol p.14 lists depressive symptom scores among secondary objectives, although that paragraph does not name IDS specifically. Main p.8 reports IDS supplement overall coefficient 0.60 (0.15–1.05), P=.01, and adjusted mean difference 1.20 (0.29–2.10), P=.01.

**Reported-versus-comparator:** REPORT/SAP secondary IDS status versus protocol main/primary parameter placement, qualified by the protocol's own secondary symptom-objective context. No formal co-primary demotion is established.

**Reasoning procedure:** Match instrument and follow-up window; compare list membership, analysis headings, and explicit status; retain p.14 context. Separate this textual placement comparison from the correctly identified effect-coding transformation and distinguish broad parameter terminology from an operational endpoint decision rule.

**Calculation:** With stated factor 2, coefficient [0.595,0.605) doubles to [1.19,1.21), overlapping printed mean difference 1.20's [1.195,1.205). Lower coefficient limit [0.145,0.155) doubles to [0.29,0.31), overlapping printed 0.29's [0.285,0.295); upper [1.045,1.055) doubles to [2.09,2.11), overlapping 2.10's [2.095,2.105). The estimates/limits reconcile under coding and precision. Heading placement is textual; precision does not determine formal hierarchy.

**Affected result or extracted value:** Prospective hierarchy metadata attached to the IDS supplement coefficient 0.60 and equivalent full difference 1.20, both with P=.01. Numeric result, producing model, and report secondary status remain identifiable.

**Why context does not resolve it:** Initial screening considered repeated separate main/primary versus secondary sections insufficiently reconciled. The independent audit questions that criterion: p.14 and explicit SAP/report secondary status support immediate broad-terminology resolution. This live inclusion concern is retained without asserting that an unresolved formal hierarchy has been demonstrated.

**Alternative source-grounded interpretations:** Protocol main/primary parameters may be broader than formal co-primary endpoints; SAP may prospectively refine that terminology. Protocol p.14 supports this interpretation. Alternatively an operative hierarchy revision could exist, but its chronology and operational definition are absent. No formal co-primary success or multiplicity rule is inferred.

**Mechanical evidence recheck:** All printed placements and the coding/precision reconciliation were reproduced. The independent auditor added direct-source p.14 context. Evidence state records reproduced source comparison, while `QUESTIONED` records the separate threshold concern; no ID or original finding provenance was removed.

**Potential downstream evidence impact:** If human review establishes a substantive hierarchy difference, an extractor's prospective IDS hierarchy metadata could change. Present evidence does not establish confirmatory status, a required adjustment, a changed effect, or a conclusion change.

**Human verification steps:** Read p.14 together with pp.9/28/43 and SAP/report secondary status. Ask how the operative protocol defines main/primary parameters, whether any formal IDS hierarchy was specified, and whether the broad-terminology context resolves the candidate under the inclusion threshold.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Primary MDD power assumptions and contrasts

**Pending Human Adjudication**

**Candidate statement:** Protocol and report state different expected incidence and attrition inputs while explicitly powering different contrasts; the auditor questions treating these coexisting specifications as a qualifying inconsistency without an established matched powering parameter.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol pp.16,17 vs REPORT main pp.4,9

**Evidence state:** reproduced

**Inclusion audit:** QUESTIONED
The protocol powers an interaction-oriented contrast and the report powers marginal main effects; both can coexist with a common 250-per-cell target. Missing operational mapping alone does not establish contradictory assumptions for the same matched contrast. Under the context/conditional boundary, not-resolved-by-context inclusion is not securely established.

**Finding IDs:** F-XS-001, F-ST1-001

**Classification rationale:** The printed design specifications compare PLAN protocol with REPORT main, giving P_R only. SAP supplies no separate power comparator. The evidence state reproduces distinct source inputs without establishing that their contrasts are identical or incompatible.

**Classification ambiguity:** Explicitly distinct powering contrasts may coexist; operational mapping, exact interaction alternative/algorithm, and revision chronology are absent.

**Exact source locations:** Protocol [p.1 final-amendment version](../joi190007supp1_prod.pdf#page=1), [p.16 §4.4 Sample size calculation](../joi190007supp1_prod.pdf#page=16), [p.17 continuation](../joi190007supp1_prod.pdf#page=17); main [p.4 Sample Size](../jama_bot_2019_oi_190007.pdf#page=4), [p.9 power discussion/limitations](../jama_bot_2019_oi_190007.pdf#page=9).

**Source evidence:** Protocol specifies expected control 30%, intervention 15%, two-sided alpha .05, 90% power, 180/group, 20% dropout, and a sufficient 250/intervention-arm target. It names additive-interaction interest and, for synergy rather than additivity, a pure-treatment-group comparison with 80% power. Main specifies intervention main effects, control 30% versus active 20%, 33% relative/10-percentage-point absolute reduction, two-sided alpha .05, 90% power, 196/factorial cell, 22% attrition, and 250/combination. Its 392/196 wording is interpretable through marginal versus cell allocations. Main p.9 says lower-than-expected MDD onset reduced power. The protocol cover supplies version context without a calculation-amendment mapping.

**Reported-versus-comparator:** REPORT 30%/20%,22%-attrition marginal-main-effect specification versus PLAN 30%/15%,20%-dropout interaction-oriented specification, with a conditional synergy calculation. These are distinct declared contrasts, not demonstrably the same marginal population.

**Reasoning procedure:** Preserve each assumption set with its named contrast and power objective; check units/rounding; identify the common target. Do not impose a common sample-size algorithm or treat one active risk as necessarily replacing the other.

**Calculation:** Printed active inputs differ by 20−15 = 5 percentage points, and dropout inputs by 22−20 = 2 points. Active-risk display intervals [14.5,15.5)% and [19.5,20.5)% do not overlap; dropout intervals [19.5,20.5)% and [21.5,22.5)% do not overlap. These show distinct printed inputs, not contradictory matched contrasts. Report relative reduction (30−20)/30 = one-third reconciles with 33%; absolute reduction is 10 points. Recruitment diagnostics 196/(1−.22) ≈ 251.28 and 180/(1−.20) = 225 do not establish arithmetic failure: inputs are approximate, targets may be sufficient rather than minimum, and exact contrast-specific algorithms are unavailable. Protocol introductory 25% wording and report 392/196 grouping are context-resolved and not candidate bases.

**Affected result or extracted value:** Contrast-specific primary-design expected incidence, effect, attrition, and power-basis metadata accompanying the reported primary-MDD result. No treatment estimate or achieved power is recalculated.

**Why context does not resolve it:** Initial screening retained a question about how both specifications governed recruitment. The independent audit finds that explicitly different contrasts supply a coherent coexistence interpretation without changing any reported primary estimate; absent operational mapping alone does not establish the required matched contradiction. This threshold concern remains explicit.

**Alternative source-grounded interpretations:** An interaction-oriented calculation and a separate main-effect calculation can both support the same approximately 250-per-cell target. This is the strongest source-grounded interpretation and remains live. Prospective assumption revision with retained earlier wording is also possible but not demonstrated. Exact interaction alternative, comparison algorithm, and role of each calculation are unavailable.

**Mechanical evidence recheck:** Direct-source text and visual confirmation matched both input sets and contrast labels, reproducing their precision-separated source comparison. Recheck did not require identical algorithms or rule out coexistence. The audit subsequently questioned inclusion; evidence state remains `reproduced` and the stable ID remains.

**Potential downstream evidence impact:** An extractor can retain both input sets with their declared contrasts. If human review establishes an operative revision or substantive inconsistency, primary-design metadata could change. Present evidence establishes neither altered achieved power nor downstream propagation or a conclusion change.

**Human verification steps:** Read protocol pp.16/17 and main p.4 jointly; retain interaction, conditional synergy, and main-effect purposes separately. Ask how these specifications jointly define recruitment, whether a documented revision exists, and whether the distinct-contrast context already resolves the candidate under the inclusion threshold.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

# Downstream Evidence-Chain Considerations

An evidence extractor may copy intervention dose, prospective analysis status, available interaction estimands, endpoint hierarchy, or design assumptions together with a trial effect estimate. The cards identify specific metadata or values potentially affected if human review confirms a candidate. They do not establish actual propagation, clinical harm, changed estimates, altered achieved power, or changed conclusions. Model-based estimates are retained with their stated model and are not replaced by crude recomputations. For QUESTIONED items, coherent contextual alternatives remain part of the evidence record.

# Limitations and Missing Definitions

The review uses only the supplied package; no raw trial data, complete fitted model covariance, analysis-specific degrees of freedom, or executable design calculations are supplied. Exact CI/P/standard error identities and model reconstruction are therefore bounded where the source does not establish the required algorithm. These limitations do not create a source-unit or relationship-coverage gap.

C1.2 formulation requirements and a documented dose-amendment mapping are unavailable. The SAP lacks an operative date/version, and protocol-to-SAP model/hierarchy chronology is not established. A narrower meaning of post hoc Cox is not identified. No additive RERI/CI or replacement/deferment statement is present in the supplied REPORT union; actual execution remains unknown. Formal IDS co-primary/key hierarchy is undefined, and secondary-objective context may resolve broad headings. Exact interaction-power alternatives and the operational relationship of coexisting power calculations are not supplied. Optional old targeted-render engine metadata is incomplete; current direct-source checks confirm registered locations. No technical tooling limitation or unmapped supplied-source unit remains. See [limitations.md](review_1_6_1/limitations.md).

# Human Adjudication Checklist

- Read every exact linked source location, including contextual and repeated occurrences.
- Distinguish mechanical reproduction from threshold inclusion and from the final human decision.
- Evaluate the contextual alternatives for C004/C005 before assigning any interpretation.
- Identify missing operative amendments, definitions, or results where available; do not infer them from source absence.
- Retain contrast, outcome, population, model, coding, time point, and units when extracting a reported estimate.
- Complete each card's Validity, Importance, Action, Initials, and Notes fields; every field remains blank for human review.

# Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

## Source integrity and durable provenance

[Source inventory](review_1_6_1/source_inventory.md), [asset inventory](review_1_6_1/evidence_asset_inventory.md), [coverage manifest](review_1_6_1/coverage_manifest.md), [ledger](review_1_6_1/candidate_ledger.md), [recheck](review_1_6_1/verification/evidence_recheck.md), and [quality audit](review_1_6_1/quality/evidence_quality_audit.md) retain the complete audit trail. The before-hash records cover every supplied source and all 267 selected reused assets: [source hashes](review_1_6_1/source_hashes_before.sha256), [reused-asset hashes](review_1_6_1/reused_artifact_hashes_before.sha256). The independent audit's SHA-256 checks found all unchanged; final coordinator hash comparison is required after assembly. All pre-existing scientific-review artifacts were preserved.

| Supplied source | SHA-256 |
|---|---|
| jama_bot_2019_oi_190007.pdf | 74b85a4b77870fda5ff0ce2f8287a2533a11ee81745d4031155f4af2986bd980 |
| joi190007supp1_prod.pdf | b8f3980eacaa908929e57fc6aadd4de0e7a5691a4978be0e2fe4b544455858db |
| joi190007supp2_prod.pdf | b14aaebd8fbded6d36e1ca618cc9f51f2c76d50e486a8c18b4fa56fb183bced7 |
| joi190007supp3_prod.pdf | eeb826267cc5662b7736f625a226f37bdeb9ce8cfc6d7556d7ef6fdba5b53246 |
| joi190007supp4_prod.pdf | 207c317e14618cc7fa6c86853e12ef03bebd2dff3676fa2383762ca248688641 |

All candidate links point to actual supplied filenames and physical PDF pages. Reusable derivatives are locators, not evidence substitutes. Local link validation and ledger/recheck/audit/report ID equality are final coordinator checks.

## Routing, tooling, and actual agent execution

[Routing preflight](review_1_6_1/routing_preflight.md) reports PASS, Coordinator inference PASS, execution mode INTERACTIVE_CLI, Provider CURRENT_SESSION, and all ten named presets verified against their fixed model/effort pairs. The documented launch command is the workflow contract; sandbox process launch arguments are not exposed. No provider configuration or credentials were changed.

The [tooling record](review_1_6_1/tooling_record.md) records Linux, probe UTC 2026-10-11T02:44:22Z, Python 3.14.4, and available pdfinfo, pdftotext, pdftoppm, pdftocairo, tesseract, libreoffice, and pandoc. Direct confirmations used CPU-only Poppler 26.01.0; hashes used uutils coreutils 0.10.0; installed OCR is Tesseract 5.5.0/leptonica 1.86.0. Fallback environment NOT_NEEDED; fallback packages/capabilities None; removal NOT_CREATED; tooling limitations None. No GPU, global package installation, or new OCR rerun was needed.

The [execution manifest](review_1_6_1/agent_execution_manifest.md) records every actual agent exactly once. All use gpt-6.1-sol; all specialist stages are fresh and have distinct runtime IDs.

| Stage | Runtime agent ID | Model | Reasoning effort | Start mode |
|---|---|---|---|---|
| coordinator | 01a128d7-ced6-7203-913d-d0bb174814ae | gpt-6.1-sol | high | CURRENT_SESSION |
| reuse_asset_curator | 01a128d9-3d06-70d2-a1d0-5ccead0a7851 | gpt-6.1-sol | medium | FRESH_SPAWN |
| main_quantitative_mapper | 01a128dc-0958-7843-9e64-b1c2e7717e86 | gpt-6.1-sol | medium | FRESH_SPAWN |
| support_quantitative_mapper | 01a128dc-2bf3-7ca2-aea2-96572b17b6a6 | gpt-6.1-sol | medium | FRESH_SPAWN |
| numeric_consistency_reviewer | 01a128e0-854d-7331-83cd-8bd180d1e2b7 | gpt-6.1-sol | medium | FRESH_SPAWN |
| cross_source_consistency_reviewer | 01a128e0-a2d6-7b50-be69-41a055ba6b47 | gpt-6.1-sol | medium | FRESH_SPAWN |
| statistics_pass_1 | 01a128e0-c784-7a33-87ba-81b76f900a82 | gpt-6.1-sol | high | FRESH_SPAWN |
| inclusion_screener | 01a128e5-2413-7142-a2ea-ee880aee0ed9 | gpt-6.1-sol | high | FRESH_SPAWN |
| evidence_rechecker | 01a128e9-9623-7823-b691-4b423018a8b4 | gpt-6.1-sol | high | FRESH_SPAWN |
| statistics_pass_2 | 01a128ed-614f-7511-81f2-7bfca2b8d7fb | gpt-6.1-sol | high | FRESH_SPAWN |
| quality_control_auditor | 01a128f2-2c90-7a32-9beb-7e6e34e8d448 | gpt-6.1-sol | high | FRESH_SPAWN |
| report_generator | 01a128f9-255f-7fb3-b284-6ed8c63b70c1 | gpt-6.1-sol | medium | FRESH_SPAWN |

## Reproducibility performance

The coordinator finalizes the following fields immediately after complete Markdown assembly. Local HTML rendering and mechanical validation fall outside the observed review window; any later model-based repair requires an updated finish time.

- **Target basis:** Five supplied PDFs contain 102 pages, all backed by usable native/layout text or readable rendered pages; zero fresh-required extraction units and no Office conversion or OCR rerun anticipated. Support text is about 153380 characters and main layout about 103173, within two mapper scopes. Table/figure visual review and eleven fresh specialist stages require sequential screening, recheck, second statistical pass, audit, and reporting waves.
- **Total source units:** 102
- **Fresh-source units:** 0
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-10-11T02:44:22Z
- **Finished UTC:** 2026-10-11T03:24:03Z
- **Observed elapsed minutes:** 39.68
- **Target status:** MET_TARGET
- **Exceedance causes:** None

Standalone HTML rendering, final source/reused-asset hash comparison, coverage-stage closure, and mechanical validation are coordinator finalization steps. Their outcome is recorded in review_1_6_1/review_validation.json; this report-generation artifact does not pre-claim a validator result.
