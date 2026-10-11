# Final Evidence-Quality Audit

## Audit status

- **Coverage status:** COMPLETE for the scientific mapping, relationship checking, candidate registration, and mechanical recheck scopes; coordinator repairs listed below are required before report generation is complete.
- **Stable candidate set audited:** C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, and C017.
- **Candidate ID-set check:** the ledger and evidence recheck contain the identical 17-ID set. This audit returns the same set. No stable ID was deleted, merged, ranked, suppressed, or given a scientific disposition.
- **Discovery-boundary check:** the source inventory, complete page ledger, mapping assignments, N001-N042 inventory, S001-S080 inventory, and checker completion records show complete assigned-unit review. The artifacts state that legacy candidate outputs were not scientific inputs. No top-N boundary, old candidate list, review queue, early stopping rule, or desired candidate count controlled discovery.
- **Tone check:** the candidate records use quality-control framing and keep uncertainty for human adjudication. They do not claim that the paper-level conclusion is wrong. Final report wording must preserve that boundary.

## Coverage, routing, and reproducibility audit

- `source_coverage.md` has exactly three direct-source rows. The arithmetic closes: DOC-001, 11 + 0 = 11 and 11 mapped; DOC-002, 18 + 7 = 25 and 25 mapped; DOC-003, 0 + 167 = 167 and 167 mapped. Package totals are 203 = 29 reusable + 174 fresh-required, with 203 mapped.
- Reusable-backed and fresh-required assignments close every direct-source row. The main map covers DOC-001 pages 1-11. The support shards are disjoint at DOC-002 pages 1-25 and DOC-003 pages 1-32, 33-64, 65-96, 97-128, 129-160, and 161-167; their union covers all 192 support pages. No scientific-coverage gap remains.
- Every current `coverage_manifest.md` data row contains one undecorated relative artifact path. The required mapping and checker artifacts exist. The `evidence_quality` and `report_generation` scopes remain outdated and are listed as repairs below.
- The routing preflight reports PASS with coordinator `gpt-5.6-sol`/`high`, ordinary specialists `gpt-5.6-terra`/`medium`, statistical specialists `gpt-5.6-terra`/`high`, Sol specialists `gpt-5.6-sol`/`high`, `Coordinator inference: PASS`, execution mode `INTERACTIVE_CLI`, and all nine presets verified.
- Statistical pass 1 agent `/root/statistics_pass_1` and statistical pass 2 agent `/root/statistics_pass_2` are distinct fresh runtime IDs, each recorded as `gpt-5.6-terra`/`high` with `FRESH_SPAWN`. Both passes explicitly cover S001-S080. Pass 2 also covers C001-C017 and the complete cross-lane checker and recheck facts.
- The source-hash ledger has 3 entries and the reusable-artifact hash ledger has 61 entries. `sha256sum --check` currently passes for all 64 paths. All candidate-ledger and evidence-recheck PDF links resolve to existing supplied PDFs, and every cited page is within the PDF page count.
- No candidate mentions `P = 0`, `p = 0.000`, or an equivalent display zero. The statistical inventory and both passes record zero display-zero relationships. Therefore no stable ID needs the conditional independent-contradiction field. A future card may mention a display zero only if it adds `**Independent contradiction beyond P=0 display:**` with a separate supplied-source contradiction; finite precision, underflow, or nonzero-tail reasoning is not sufficient.

## Common final-card field gap for C001-C017

The ledger is a registration artifact rather than the final evidence-card artifact. For every one of C001-C017, the report generator must expand the ledger and recheck facts into the exact required labels: **Candidate statement:**, **Category:**, **Exact source locations:**, **Source evidence:**, **Reported-versus-comparator:**, **Reasoning procedure:**, **Calculation:**, **Alternative source-grounded interpretations:**, **Mechanical evidence recheck:**, **Quality-control relevance:**, **Potential downstream evidence impact:**, **Human verification steps:**, and **Human adjudication fields:**. The last field must contain exactly:

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

No current human-adjudication subfield exists in the pre-report ledger, so placeholder compliance can be finalized only after report assembly. Every subfield must remain exactly `__`; no AI-generated value may replace it.

## C001 — Balloon-angioplasty female percentage does not reconcile with count and denominator

- **Evidence and calculation audit:** DOC-001 Table 1, PDF page 6, prints BA n=249, male 172 (69.1), and female 77 (30.1). The recheck reproduces 172 + 77 = 249 and 77/249 x 100 = 30.9237%, which ordinarily rounds to 30.9%; the printed 30.1% also makes the displayed sex percentages sum to 99.2%.
- **Assumption and category audit:** `Denominator, proportion, or total inconsistency` follows the scope. The final card must say that ordinary nearest-one-decimal rounding and use of the displayed arm denominator are the applied rule; it must not infer which printed field is wrong.
- **Pagination, duplication, and impact audit:** The page-6 link is truthful. NP-01 and cross-source Proposal 1 are the same printed relationship and were appropriately merged before stable IDs. No duplicate stable relationship is evident. Bounded downstream wording may identify extraction of the BA female baseline proportion; it must not claim a conclusion change.
- **Card-field repair:** Populate all common final-card fields, include the exact recheck arithmetic, name an undisclosed row denominator or transcription mechanism only as an alternative, and retain the exact human question.

## C002 — Balloon-angioplasty ischemic-stroke percentage is outside ordinary one-decimal rounding

- **Evidence and calculation audit:** DOC-001 Table 1 page 6 and DOC-002 Table S1 page 14 both print BA n=249 and 215 (86.4); 34 + 215 = 249. The recheck reproduces 215/249 x 100 = 86.3454%, ordinarily 86.3%, while 34/249 x 100 = 13.6546%, ordinarily 13.7%.
- **Assumption and category audit:** The category is in scope. Because the discrepancy is only 0.0046 percentage points below the ordinary 86.4% rounding interval, the final statement must remain conditional on the unstated rounding convention and must not call the repeated value definitively erroneous.
- **Pagination, duplication, and impact audit:** Both PDF links resolve and the repetition is one relationship, not two candidates. Bounded impact is limited to extraction of the qualifying-event composition.
- **Card-field repair:** Populate the common fields and explicitly distinguish the printed repetition from the diagnostic nearest-rounding interpretation.

## C003 — Table S4 procedure rows use 241 while the column header states 249

- **Evidence and calculation audit:** DOC-002 Table S4 page 17 prints a BA arm header of 249 and a linked footnote that 241 of 249 underwent BA. Procedure-category counts sum to 241, and examples 182/241 = 75.5%, 214/241 = 88.8%, and 42/241 = 17.4% reproduce the displayed percentages.
- **Assumption and category audit:** The denominator category is in scope, but the recheck finds the consistency rule only conditionally applicable because the footnote may fully define the procedure-applicable denominator. The final card must frame the observation as a denominator-label clarity question, not as established incorrect arithmetic.
- **Pagination, duplication, and impact audit:** Page 17 is truthful; no duplicate stable relationship was found. Any downstream statement is limited to a data extractor choosing 249 instead of the footnoted 241 for procedure rates.
- **Card-field repair:** Put the footnote and its potentially resolving interpretation prominently in `Alternative source-grounded interpretations` and `Mechanical evidence recheck`; do not imply that an explicit 241 row header is the only acceptable presentation.

## C004 — Table S6 BA 9 (3.9) conflicts with its displayed denominator 249

- **Evidence and calculation audit:** DOC-002 Table S6 page 19 prints BA n=249 and 9 (3.9). The recheck reproduces 9/249 x 100 = 3.6145%, ordinarily 3.6%, and notes diagnostically that 9/233 x 100 = 3.8627%, ordinarily 3.9%.
- **Assumption and category audit:** The denominator category is correct. Use of 233 is an inferred explanation based on a separately supplied PPS total, not a source label in Table S6.
- **Pagination, duplication, and impact audit:** The link is truthful. NP-04 and SP-02/S033 are one internal denominator-percentage relationship. C016 is not a duplicate: it compares the Table S6 numerator with the matched main-result numerator under a different consistency rule.
- **Card-field repair:** Populate the common fields, label 233 as diagnostic, and bound downstream impact to extraction of the centre-adjusted analysis population and risk.

## C005 — Table S7 group headers conflict with site totals and displayed site percentages

- **Evidence and calculation audit:** DOC-002 Table S7 page 20 prints headers 233/238, site totals 256/245, and event cells 4 (2.9), 19 (16.1), 7 (6.3), and 15 (11.2). The header total is 471 while site totals sum to 501. The recheck shows that the displayed percentages are compatible with diagnostic site-by-arm denominators 138/118 and 111/134, which sum to 249/252.
- **Assumption and category audit:** The denominator category is correct. The site-by-arm denominators are derived from the rounded cells plus totals and must never be presented as printed source values.
- **Pagination, duplication, and impact audit:** Pages 20, 5, and 23 resolve. NP-05, cross-source Proposal 4, and SP-03/S034 were appropriately merged. Bounded impact is limited to subgroup/site risk and interaction-table extraction.
- **Card-field repair:** Populate the common fields, label every derived denominator as diagnostic, and ask which disclosed population and site denominators were intended.

## C006 — Table S8 per-protocol percentages conflict with headers 249/252

- **Evidence and calculation audit:** DOC-002 Table S8 page 21 is labelled PPS but prints headers 249/252. Its rows reproduce against supplied PPS denominators 233/238, including 9/233 = 3.9%, 33/238 = 13.9%, 6/233 = 2.6%, and 20/238 = 8.4% at one decimal.
- **Assumption and category audit:** The denominator category is correct. A copy-forward header mechanism is only an inferred production explanation.
- **Pagination, duplication, and impact audit:** Page 21 and comparators at DOC-001 page 5 and DOC-002 page 23 resolve. NP-06, cross-source Proposal 5, and SP-04/S035-S038 are the same denominator relationship. Bounded impact concerns PPS denominators and sensitivity-result extraction.
- **Card-field repair:** Populate the common fields and do not prescribe 233/238 as a correction without human confirmation of the PPS definition.

## C007 — Table S9 as-treated percentages conflict with headers 249/252

- **Evidence and calculation audit:** DOC-002 Table S9 page 22 is labelled ATS but prints headers 249/252. Most cells reproduce against the separately supplied ATS denominators 247/254, including 11/247 = 4.5%, 34/254 = 13.4%, and 19/254 = 7.5% at one decimal.
- **Assumption and category audit:** The denominator category is correct. The explanation that headers were copied from the primary analysis is not directly observed.
- **Pagination, duplication, and impact audit:** Pages 22 and 23 resolve. NP-07, cross-source Proposal 6, and SP-05/S039-S042 were appropriately merged. C014 is distinct because it tests the separate 8 (3.3) cell under both supplied denominators.
- **Card-field repair:** Populate the common fields, retain the ATS-definition uncertainty, and limit downstream wording to ATS population/risk extraction.

## C008 — Baseline stenosis categories include values outside the stated 70%-99% eligibility range

- **Evidence and calculation audit:** DOC-001 pages 2, 5, and 6 print the 70%-99% eligibility interval and Table 1 categories containing two AMM participants at 60%-69% plus one participant per arm at 100%; four displayed baseline values are outside the interval.
- **Assumption and category audit:** `Analysis-unit or population inconsistency` is permissible only conditionally. The supplied pages do not establish that eligibility and Table 1 use the same measurement time, reader, angiogram, or adjudication rule. The final candidate statement must therefore describe a cross-location threshold/category mismatch with measurement identity unresolved, not assert that four participants were ineligible.
- **Pagination, duplication, and impact audit:** All three links resolve. NP-08 is one relationship. Bounded impact concerns extraction of the analysed baseline stenosis distribution and eligibility definition, not study eligibility validity.
- **Card-field repair:** Carry the missing identity conditions and the recheck's alternative measurements/protocol-deviation interpretations into the final card.

## C009 — Thirty-day follow-up tolerance is plus or minus 3 days in the supplement but plus or minus 7 days elsewhere

- **Evidence and calculation audit:** DOC-002 page 6 prints 30 plus or minus 3 days; DOC-001 page 3 and DOC-003 page 15 print 30 plus or minus 7 days. The tolerance half-widths differ by four days; the numerical endpoint-to-endpoint interval widths are 6 and 14 days.
- **Assumption and category audit:** `Measure, label, or scale inconsistency` is correct. The current sources do not define distinct operational and protocol windows.
- **Pagination, duplication, and impact audit:** All links resolve and NP-09 is one relationship. Bounded impact is limited to extraction or implementation of the nominal 30-day follow-up window.
- **Card-field repair:** In the final `Calculation`, say `numerical interval width` or compare the half-widths. Avoid calling 6 and 14 the inclusive number of calendar days.

## C010 — Protocol V2.0 gives 21-day and 14-day lower bounds for the same stroke criterion

- **Evidence and calculation audit:** DOC-003 pages 7 and 21 are both within Protocol V2.0 and print 21-90 days and 14-90 days for the ischemic-stroke eligibility interval. The lower bounds differ by seven days.
- **Assumption and category audit:** The measure/label category is correct after same-version and criterion matching. The source does not establish which occurrence governed enrolment.
- **Pagination, duplication, and impact audit:** Both links resolve; NP-10 is one relationship. Bounded impact concerns protocol eligibility-window extraction.
- **Card-field repair:** Populate the common fields and keep stale synopsis, unmarked amendment, or another production mechanism as alternatives rather than conclusions.

## C011 — BA 3-month aspirin percentage does not reconcile with count and displayed arm denominator

- **Evidence and calculation audit:** DOC-002 Table S3 page 16 prints BA n=249 and aspirin 234 (93.9). The recheck reproduces 234/249 x 100 = 93.9759%, ordinarily 94.0%.
- **Assumption and category audit:** The denominator category is correct under ordinary nearest rounding. A different integer evaluated denominator no larger than the 249-person arm does not naturally yield 93.9% under that rule; source-grounded alternatives should emphasize truncation, weighting, or an otherwise undisclosed display rule rather than imply a known hidden denominator.
- **Pagination, duplication, and impact audit:** Page 16 resolves; NP-11 is one relationship. Bounded impact concerns follow-up medication-use extraction.
- **Card-field repair:** Populate the common fields and name the missing evaluated denominator, missingness handling, and display rule without prescribing a replacement.

## C012 — Figure S1 repeats “2nd meeting” for three chronologically distinct meetings

- **Evidence and calculation audit:** Direct visual recheck of DOC-002 Figure S1 page 10 confirms labels `1st`, `2nd`, `2nd`, and `2nd meeting` on four distinct dates. Each meeting's reported-case arithmetic separately reconciles.
- **Assumption and category audit:** The measure/label category is correct if the ordinal is a single chronological sequence. An unprinted review-cycle convention remains a source-grounded alternative.
- **Pagination, duplication, and impact audit:** Page 10 resolves; NP-12 is one relationship. Bounded impact concerns interpretation or extraction of the CEC meeting timeline, not endpoint counts.
- **Card-field repair:** Populate the common fields, retain the fully reconciling case-count arithmetic, and ask whether the ordinal denotes chronology or a repeated cycle.

## C013 — Recurring visit sentence ambiguously repeats visit numbers 9 and 11

- **Evidence and calculation audit:** The sentence appears on DOC-003 page 35 in original Protocol V2.0 and identically on page 96 in final Protocol V2.3. It lists `visit 8, visit 9, visit 10, visit 11, visit 9, and visit 11`; the page-15 schedule identifies visits 8-11 as the four recurring visits.
- **Assumption and category audit:** The measure/label category is appropriate, but the current ledger and NP-13 description falsely call page 35 final-protocol material and assume a six-visit sequence needing fifth and sixth replacement identifiers. The schedule supports a plausible alternative that visits 9 and 11 are the face-to-face subset and the sentence lacks clarifying syntax.
- **Pagination, duplication, and impact audit:** Page 35 itself is truthful but its version descriptor is wrong; page 96 is the truthful final-protocol occurrence and must be added. This remains one repeated relationship, not two candidates. Bounded impact concerns longitudinal visit labeling only.
- **Card-field repair:** Repair the ledger and final card to cite both page 35 as Protocol V2.0 and page 96 as Protocol V2.3. Reframe the statement and human question around ambiguous subset-versus-sequence syntax; do not ask for new visit identifiers as though a six-visit sequence were established.

## C014 — Table S9 BA 8 (3.3) does not round from either supplied ATS or displayed denominator

- **Evidence and calculation audit:** DOC-002 Table S9 page 22 prints BA 8 (3.3); Table S10 page 23 supplies ATS N=247 while Table S9 displays 249. The recheck reproduces 8/247 x 100 = 3.2389% and 8/249 x 100 = 3.2129%, both ordinarily 3.2%.
- **Assumption and category audit:** `Numeric or arithmetic inconsistency` is correct under ordinary rounding. An unprinted outcome-specific risk set or nonstandard display rule remains possible.
- **Pagination, duplication, and impact audit:** Both links resolve. NP-14 is distinct from C007's population-header relationship. Bounded impact concerns extraction of the early ATS event risk.
- **Card-field repair:** Populate the common fields and state both supplied-denominator calculations without implying that 247 is definitively the cell denominator.

## C015 — Narrative assigns all 11 pre-analysis exclusions to consent withdrawal while Figure 1 assigns only 10

- **Evidence and calculation audit:** DOC-001 narrative page 4 says 11 were excluded due to consent withdrawal. Figure 1 page 5 prints seven BA plus three AMM consent withdrawals and one separate erroneous randomization assignment. Thus 7 + 3 = 10 consent withdrawals, and 10 + 1 = 11 total removals.
- **Assumption and category audit:** `Cross-document numeric inconsistency` covers matched narrative-versus-figure occurrences under the scope. The source does not establish whether the erroneous-assignment participant also withdrew consent.
- **Pagination, duplication, and impact audit:** Both links resolve; cross-source Proposal 2 is one relationship. Bounded impact concerns extraction of participant-flow reason categories, not the 501-person analysis total, which reconciles.
- **Card-field repair:** Populate the common fields, explicitly state that the total flow reconciles, and keep umbrella shorthand or dual classification as alternatives.

## C016 — Table S6 BA event count 9 conflicts with the matched primary-analysis count 11

- **Evidence and calculation audit:** DOC-001 pages 5 and 8 print BA 11 (4.4%) under n=249 for the primary composite; DOC-002 Table S6 page 19 prints BA 9 (3.9) under the same 249 header and matched composite wording. The count difference is two; AMM remains 34.
- **Assumption and category audit:** The cross-document category is correct after endpoint and header matching. Centre adjustment alone does not explain a changed observed count, but a complete-case subset or unlabelled alternative population/endpoint remains possible and must not be ruled out without source data.
- **Pagination, duplication, and impact audit:** All links resolve. C016 is distinct from C004's within-table denominator-percentage arithmetic. Bounded impact concerns extraction of the centre-adjusted sensitivity analysis and its event count; no paper-level conclusion impact is established.
- **Card-field repair:** Populate the common fields, include the source-grounded Table S10 no-revascularization count of 9 only as an alternative carryover explanation, and ask for the Table S6 population and endpoint definition.

## C017 — One-year incidence-difference point estimate lies outside its confidence interval

- **Evidence and calculation audit:** DOC-001 Table 2 page 8 prints BA 3/249 (1.2%), AMM 4/252 (1.6%), incidence difference -0.4%, and 95% CI -2.4% to -1.7%. The point estimate is outside the ordered interval. The crude difference `(3/249 - 4/252) x 100 = -0.3825` percentage points reproduces -0.4% at one decimal.
- **Assumption and category audit:** `Statistical reporting inconsistency` is correct. The exact CI construction and any adjusted estimand are not supplied; the final card must not infer which endpoint or sign should change.
- **Pagination, duplication, and impact audit:** Page 8 resolves. Cross-source Proposal 7 and SP-01/S013 are the same relationship and were appropriately merged. Bounded impact concerns extraction of this secondary incidence difference and interval; it cannot be expanded into an unsupported claim about the primary conclusion.
- **Card-field repair:** Populate the common fields, separate direct non-containment from the diagnostic crude comparator, and retain the missing CI-method/estimand definition.

## Required coordinator repairs before report generation

1. Repair C013 in `candidate_ledger.md` and its upstream NP-13 description: page 35 is Protocol V2.0, not final protocol; add the identical Protocol V2.3 occurrence at page 96 and reframe the unresolved question as subset-versus-sequence syntax.
2. Repair proposal provenance in `relationships/numeric_relationship_inventory.md`: remove the unrelated NP-12 reference from N001; link N032 to NP-12; link N038 to NP-13; and add NP-14 to N025. Then describe the coverage count as 14 N relationships carrying one or more of 14 numeric proposals, if that is the intended metric.
3. Update `coverage_manifest.md` after this artifact is accepted: enumerate C001-C017 explicitly in the `evidence_quality` scope and mark the row COMPLETE. Replace the `report_generation` placeholder scope with the same explicit ID set when the report is generated, and mark that row COMPLETE only after every card exists.
4. Generate every final card with all exact labels listed above and the five exact `__` human placeholders. Carry the candidate-specific qualifications from this audit into the card fields, especially C003, C008, C009, C011, C013, C016, and C017.
5. Keep C004 and C016 distinct, and keep C007 and C014 distinct. Do not merge, delete, renumber, rank, or suppress any stable ID during these repairs.

## Limitations

- The supplied PDFs do not contain participant-level data, production tables, risk-set logs, unrounded percentages, analytic code, Cox coefficients/standard errors, covariance matrices, interaction statistics/degrees of freedom, or the selected row-level test for many P values. The audit therefore cannot identify the intended corrected value for any candidate.
- Report-generation, token-accounting, final hash recomputation, HTML rendering, and mechanical validation had not occurred when this audit was written. Human-placeholder compliance and ledger/recheck/quality/report ID-set identity must be rechecked after the report exists.
- Several candidates depend on an unstated identity or display convention rather than irreconcilable arithmetic alone. Their final cards must preserve the named missing definition and the source-grounded alternative interpretation.

## Compact completion record

- **Covered IDs:** C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017.
- **Scientific source coverage:** 203 of 203 direct-source pages mapped.
- **Relationship coverage:** N001-N042; S001-S080 with both statistical passes complete.
- **Display-zero-only candidates:** 0.
- **Coordinator repairs requested:** C013 version/location and framing; numeric-inventory provenance; coverage-manifest candidate scopes; complete final-card fields and exact human placeholders.
- **Artifact:** `.ai_paper_validation/review_1_5_3/quality/evidence_quality_audit.md`.
