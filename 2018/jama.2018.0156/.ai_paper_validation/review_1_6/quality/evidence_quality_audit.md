# Workflow 1.6 Evidence Quality and Classification Audit

Pending Human Adjudication. This audit covers every stable candidate C001 through C031, all three direct sources, every current coverage row, both quantitative maps, all 445 numeric relationships, all 87 statistical relationships, all 47 matched families, all four checker outputs, and the complete merged mechanical recheck. No stable ID is deleted, merged, ranked, or suppressed. The evidence-state and suggested-review fields below quote and audit mechanical records; they are not human adjudications.

- Auditor runtime: /root/quality_auditor.
- Required named role: qc16_quality_control_auditor; recorded model gpt-6.1-sol; reasoning effort high; start mode FRESH_SPAWN.
- Audit stage status: COMPLETE for the pre-report scientific-evidence and classification scope.
- Covered IDs: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018, C019, C020, C021, C022, C023, C024, C025, C026, C027, C028, C029, C030, C031.
- Direct-source closure: 146/146 pages mapped; reusable 145 plus fresh-required 1 equals total 146.
- Relationship closure: N001 through N445, S001 through S087 in both passes, and F01 through F47.
- Classification totals: P_R 2; P_P 9; S_C 3; S_W 17. Review domains: statistical_results 18; report_internal_inconsistency 2; plan_material 9; protocol_report 2.
- Evidence-state totals: recorded_candidate 27; record_input_error 3; not_reproduced 1; repaired_residual 0. Mechanical suggested-review totals: retain 27; discuss 3; exclude 1.
- Report-stage boundary: the report is not yet assembled. Ledger/report value equality, all final card labels, exact human blank templates, report links, HTML and final validation require the coordinator's post-assembly mechanical checks. This audit does not attest a nonexistent report or a final validator result.

## Inputs and audit method

Normative controls read completely: QUALITY_CONTROL_SCOPE.md, PERFORMANCE_PROFILE.md, workflow_1_6/review_contract.md, workflow_1_6/report_spec.md, workflow_1_6/settings.toml. Current audit inputs: source_inventory.md, source_coverage.md, evidence_asset_inventory.md, coverage_manifest.md, routing_preflight.md, tooling_record.md, agent_execution_manifest.md, extraction/main_quantitative_evidence.md, the complete concatenated extraction/support_quantitative_evidence.md and its shard identities, relationships/numeric_relationship_inventory.md and its four parts, statistics/relationship_inventory.md, checkers/numeric_consistency.md, checkers/cross_source_consistency.md, checkers/statistical_pass_1.md, checkers/statistical_pass_2.md, candidate_ledger.md and its single classification table, verification/evidence_recheck.md and its retained second-shard provenance, and both recheck arithmetic records.

Reading was split into bounded sequential waves. The complete ledger, merged recheck and expanded statistical inventory were not loaded together as one scientific-input shard. Every numeric and statistical record was considered; boundary checks counted all records, rather than a selected candidate subset. Repeated canonical/part records are provenance duplicates, not additional relationships. No legacy scientific audit or old candidate set was read as discovery evidence. No web, external literature, custom Python analysis, OCR rerun or GPU operation was used. Shell tools were used for read-only inventory, structural comparison, page-bound checks and hash confirmation. Current source-linked direct visual recheck records are the authority for printed evidence; this audit does not claim a second independent rendering of all candidate pages.

## Complete source and coverage audit

| Source | Content role | Total | Reusable | Fresh-required | Mapped | Closure |
|---|---|---:|---:|---:|---:|---|
| DOC-001 jama_jabre_2018_oi_180004.pdf | REPORT main article | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-002 joi180004supp1_prod.pdf | PLAN protocol, operational annexes, amendments and SAP; historical values retain PLAN role | 134 | 133 | 1 | 134 | COMPLETE |
| DOC-003 joi180004supp2_prod.pdf | REPORT results supplement | 3 | 3 | 0 | 3 | COMPLETE |

Direct pdfinfo confirms 9, 134 and 3 physical PDF pages. There are no supplied Office, workbook or CSV units. The three source rows close both required identities: reusable plus fresh-required equals total, and mapped equals total. DOC-002 native/layout usable pages 1–51, 53–107 and 110–125 contribute 122 unique pages; source-matched OCR/images add pages 52, 108–109 and 126–133, eleven more. Page 134 is the sole fresh-required unit and has an exact direct Poppler rendering and full visual mapping: header/footer with an empty body. Empty extracted text was not used as a blank-page inference.

Scientific mapping is disjoint: main pages 1–9; PLAN support pages 1–32, 33–64, 65–96, 97–125 and 126–134; results supplement pages 1–3. The support-001 canonical artifact contains its original 35-page scope and the lossless later shard concatenation. That artifact's broader canonical contents do not create a second source assignment. The p64/p65 sentence continuation closes across adjacent parts. Every cover, contents, bibliography, prospective blank form and administrative page has an explicit applicability account; these are not unread pages. Relationship inventories retain every table cell, category sum, printed effect and interval, statistical definition and result-relevant label. Administrative numbers are distinguished from scientific results with a stated content basis.

At the audit snapshot the coverage manifest has 34 data rows. Every row has exactly one plain relative artifact path; every already-completed row's path resolves. The only initially absent file was this assigned audit output, which this artifact now supplies. All pre-audit stage rows are COMPLETE; the evidence_quality row must be marked COMPLETE after handoff. The later report_generation row and report artifact are properly still prospective at this audit-before-report stage. Candidate registration enumerates every C ID. The disjoint evidence-recheck rows enumerate all 31 IDs, and the canonical merged body has every heading exactly once. Each statistical-pass scope explicitly enumerates every S001–S087; numeric parts close 120+120+120+85=445.

There is no evidence of a top-N boundary, desired finding count, old candidate list controlling discovery, or sampling after reuse. All source units were assigned before checking; both maps reconstruct full content; non-candidate numeric/statistical outcomes and the 47 matched-family outcomes are durable. The 31 stable IDs are the merged discovery output, not the assigned scientific discovery scope. No registered ID is omitted because its evidence state differs from recorded_candidate.

## Reproducibility, integrity and execution audit

Read-only `sha256sum --quiet -c` checks succeed for both source_hashes_before.sha256 and reused_artifact_hashes_before.sha256. All three source hashes and all 104 reused artifact hashes remain unchanged at this audit snapshot. New derivatives have recorded direct Poppler engine/version and source-page commands; historical OCR/renderer limitations are retained as provenance limitations. There is no fallback environment to remove. Tesseract/Office conversion absence creates no scientific-unit gap because there are no Office sources, reusable image/OCR coverage closes the image pages, and direct rendering closes p134.

All 485 PDF-page links in the current ledger, merged recheck, checkers and canonical maps resolve to supplied files and have physical page anchors within the source's actual bounds. PDF pagination is distinguished from printed article/protocol/SAP pagination. No Office pagination is fabricated. This mechanical path/page check supplements the recheck's exact heading/table visual confirmations; it does not establish an unseen final report's relative links.

The execution manifest contains the coordinator and all 14 actual specialists to date, 15 unique runtime IDs. Mandatory prior stages use distinct fresh specialist handles and the required recorded model/effort pairs. Optional support and recheck shards have unique handles and the same effort class as their parent role. Statistical pass 1 is /root/statistics_pass_1 and statistical pass 2 is /root/statistics_pass_2: distinct fresh gpt-6.1-sol/high rows with durable separate artifacts, neither a promoted mapper nor a follow-up effort change. Every S row retains PASS_1_COMPLETE and PASS_2_COMPLETE, and pass 2 explicitly revisits the complete 31-ID cross-lane ledger and all recheck facts. No new candidate was appended in pass 2. The future fresh report_generator row must be appended when that agent is spawned.

Routing preflight records PASS, the required coordinator and nine named preset pairs, Coordinator inference PASS and INTERACTIVE_CLI. The current-provider selection is a stated user override. Configuration and responding named-role execution are documented; independent actual-model/provider attestation and independent verification of the launch command are unavailable. This audit does not invent those attestations. The reported run-local validator compatibility adjustments concern only the bundled provider hardcoding and slash-containing runtime handles; the preserved validator/diff must remain reviewable, and no scientific coverage or classification rule may be weakened.

## Classification, duplicate relationships and card completeness

All 31 ledger rows have exactly one allowed primary category, one primary relationship type, an all-relationships value including that type, compared content roles, the mechanically derived domain, a recheck-supported evidence state, and the mechanically derived suggested review disposition. The recheck writeback values agree with the ledger table. Every current primary/all relationship is a singleton; there is no mixed-type candidate requiring an unresolved precedence choice. Precedence nevertheless was audited against all substantive comparisons. Corroborating plans do not add P_R to C013/C014; the plan's authorized-center total does not add P_R to C017; supplement corroboration does not add S_C to C016; report margin corroboration does not add P_R to C024/C030. Historical percentages inside the protocol remain PLAN for C026.

Possible shared causes were audited without deleting or merging IDs. C015 denominator conservation and C028 favorable-numerator conservation use different inputs/rules. C016 subset alignment is distinct from both. C020 versus C022 concern different named scales; C021 versus C023 concern distinct scale/operation alignments. C024 sign/threshold difference and C030 shared-boundary notation use different source forms and rules. Repeated percentages, plan versions and duplicate checker emissions retain provenance under the existing stable IDs. Similar rounding mechanisms across C001–C012 do not make different cells duplicate relationships.

Each stable record has exact locations, source/comparator values, applicable or explicitly conditional rule, reproduced computation or logical comparison, necessary-input status, missing definitions, alternatives, observation/inference distinction, exact human question, roles/type confirmation and evidence-state reason in the canonical recheck. No missing scientific evidence-card field remains unrecorded across the ledger/recheck pair. The ledger is not the final report-card template: all 22 report-spec labels and all classification fields must be instantiated by the report generator for every ID. The conditional Independent contradiction beyond P=0 display field is required only if a candidate card mentions an actual display-zero value. No stable ID here rests on such a value; no source display-zero P value was found in the completed statistical inventory. Finite precision, underflow or mathematical nonzero-tail reasoning is not accepted as an independent contradiction.

Human adjudication remains blank. At this pre-report stage there are no filled human adjudication subfields in the scientific input artifacts. For each final report card, Validity, Importance, Action, Initials and Notes must each use exactly `__`. The post-assembly validator must confirm all 155 values; this audit does not claim that a report not yet written already passes that check.

## Repairs and classification reconciliation record

| Record | Action or writeback | Reason and scope |
|---|---|---|
| C013 | Existing coordinator registration reconciliation retained: Statistical reporting inconsistency rather than numeric-lane draft Numeric or arithmetic inconsistency | The relationship interprets an inferential lower confidence limit against its NI threshold. Current ledger/recheck agree; S_W/statistical_results remains unchanged. This is a category reconciliation recorded in the ledger, not an auditor severity decision. |
| C016 | Current record_input_error/discuss retained; report must state unsupported subset identity explicitly | Figure actual-recipient rescue and ITT before-ROSC regrouping are not established as nested participant sets. Supplement corroboration adds no discrepancy type. |
| C021, C023 | Current record_input_error/discuss retained; report must separate assessment, entry and CRF collection | The source does not equate collection from an existing CRF at day 28 with a new measurement at day 28. |
| C031 | Current not_reproduced/exclude retained, with correct primary arithmetic | Original draft reused secondary 55/54 inputs. Primary 44/43 gives 0.114763993710 pp, which rounds to 0.11 and agrees with source. No residual mismatch remains. |
| C022 | Auditor requested and coordinator completed removal of unsupported 0–100 range from ledger calculation | Exact definition paragraphs p24/p79 state ventilation-difficulty construct without that numerical range. Range is unnecessary to the registered construct contrast. Original checker provenance remains preserved. |
| C024 and S074 | Auditor requested and coordinator completed literal source notation H1≥0.01 in current ledger location labels and statistical inventory Printed values | Source has unsigned positive 0.01 with neither a leading plus nor a minus. Positive-number mathematics remains correct; literal transcription is distinguished from interpreted sign. |
| N354 | Auditor requested and coordinator completed the same unsigned literal in current canonical numeric inventory and part003 | Prevents describing a mathematical plus-sign shorthand as a printed glyph. Comparison and 2-pp calculation are unchanged. |

No current role, primary type, all-relationships value, review domain, evidence state or suggested review disposition required an additional auditor classification change. All supportable auditor omissions above were sent to the coordinator and completed in the current inputs. Recheck states and source-grounded limitations govern the report; preserved registration/checker history is not silently overwritten or copied as the current conclusion.

## C001 — Completion percentage

**Classification audit:** Denominator, proportion, or total inconsistency; REPORT within the main abstract; S_W, all S_W; statistical_results; recorded_candidate; suggested retain. No conflicting PLAN location or mixed precedence issue.

**Evidence and arithmetic:** Main PDF p1 prints 2043 randomized, 2040 completed and 99.8%. The recheck reproduces 100×2040/2043=99.853157121880%, single nearest display 99.9%; printed-minus-derived difference −0.053157121880 pp. Exact location and all recheck fields are present; no pagination or arithmetic defect found.

**Assumptions and wording:** Single rounding is a diagnostic, not an asserted author rule. Truncation or staged half-even rounding explains 99.8; display-production rule and any alternate denominator remain the named human question. Distinct from C002's sex fraction. If confirmed, a data extractor could copy a completion percentage or denominator requiring clarification; no missing follow-up or conclusion change is established. **Writeback:** carry the conditional rule, alternatives and retain pre-fill into the complete report card.

## C002 — Randomized female percentage

**Classification audit:** Denominator, proportion, or total inconsistency; REPORT abstract fraction/percentage, with REPORT Table 1 as contextual population evidence; S_W, all S_W; statistical_results; recorded_candidate; suggested retain.

**Evidence and arithmetic:** Main p1 665/2043 and 32%; 100×665/2043=32.550171316691%→33 under nearest whole rounding. Main p5 ITT females 332+332=664 are a different population. Inputs, locations and recheck fields are complete, with no false page assignment.

**Assumptions and wording:** Truncation/coarse display is possible. Do not treat 665 versus 664 as a contradiction or assume the female count is wrong. C001 has different inputs and precision. If confirmed, extraction of the randomized-sex proportion could require a clarified convention; no baseline-test or inference impact is demonstrated. **Writeback:** preserve randomized/ITT distinction and the exact rounding question.

## C003 — BMV amiodarone percentage

**Classification audit:** Denominator, proportion, or total inconsistency; REPORT Table 1 cell/header; S_W, all S_W; statistical_results; recorded_candidate; suggested retain. PLAN nonmissing-percent rules are an alternative, not a conflicting comparator.

**Evidence and arithmetic:** Main p5 200(19.7), header 1018; 100×200/1018=19.646365422397%→19.6. Difference +0.053634577603 pp is correctly calculated. Recheck fields and physical page are complete.

**Assumptions and wording:** Row-specific denominator is unprinted; a smaller nonmissing denominator or staged rounding can reconcile. Header denominator must remain conditional. This is a different cell from every other percentage card. If confirmed, an extractor could carry an ambiguous baseline treatment percentage; no inferred treatment imbalance or trial-conclusion effect follows. **Writeback:** include missingness/rounding definitions and the source-grounded alternatives.

## C004 — ITT ETI ROSC percentage

**Classification audit:** Denominator, proportion, or total inconsistency; REPORT main narrative/Table 2; S_W, all S_W; statistical_results; recorded_candidate; suggested retain. Repeated same-report occurrences corroborate the printed fraction.

**Evidence and arithmetic:** Main p4 explicitly 397/1022[38.9%], p6 same count/percent; 38.845401174168%→38.8 under single rounding, discrepancy +0.054598825832 pp. The count-derived RD −4.6607 pp agrees with −4.7. Exact locations and required recheck fields are present.

**Assumptions and wording:** Staged rounding can give 38.9. An alternative denominator must be distinguished from the explicit narrative 1022. C007 concerns PP, not this ITT occurrence. If confirmed, a ROSC percentage could need clarified precision, without a demonstrated change to the count-based effect or reported inference. **Writeback:** preserve that bounded distinction.

## C005 — PP ETI CPC1 percentage

**Classification audit:** Denominator, proportion, or total inconsistency; REPORT Table 2 PP cell/total; S_W, all S_W; statistical_results; recorded_candidate; suggested retain.

**Evidence and arithmetic:** Main p6 34(3.5), PP 943; CPC counts 34+6+7+4+892=943. 100×34/943=3.605514316013%→3.6, difference −0.105514316013 pp. A denominator yielding 3.5 is larger than 943, so ordinary within-PP missingness does not explain it. Fields and source-page location are complete.

**Assumptions and wording:** Intended count/percent/population remains unresolved; do not prescribe a corrected cell. Primary favorable numerator 34+6=40 remains coherent and composite P=.76 is a whole-block test. If confirmed, CPC-category percentage extraction could require correction; no primary count or significance change is established. **Writeback:** retain exact numerator/denominator question and block-test boundary.

## C006 — PP BMV admission percentage

**Classification audit:** Denominator, proportion, or total inconsistency; REPORT Table 2; S_W, all S_W; statistical_results; recorded_candidate; suggested retain.

**Evidence and arithmetic:** Main p6 289(29.1), PP 995; 29.045226130653%→29.0, discrepancy +0.054773869347 pp. All recheck fields and truthful page/row locators are present.

**Assumptions and wording:** Smaller available-case denominator, e.g. 993, or staged rounding can explain the display, without evidence that either was used. Unknown CI/test construction does not support an added interval candidate. Distinct outcome/cell from C008. If confirmed, admission-proportion extraction could require a denominator or precision note; count-derived effect and nonsignificant P are not disproven. **Writeback:** preserve conditional header use and missing row definitions.

## C007 — PP ETI ROSC percentage

**Classification audit:** Denominator, proportion, or total inconsistency; REPORT Table 2 count/header/percentage/effect; S_W, all S_W; statistical_results; recorded_candidate; suggested retain.

**Evidence and arithmetic:** Main p6 high-resolution direct-source crop confirms 377, not 370; cell 377(30.0), PP 943. 39.978791092259%→40.0; count RD 100×(342/995−377/943)=−5.606931795776 pp→−5.6 agrees with effect. Displayed 34.4−30.0 instead gives +4.4. All exact inputs/recheck fields are complete; no corrected-input residual state is needed.

**Assumptions and wording:** A denominator near 1257 exceeds PP 943; intended percentage or population/cell assignment is the human question. This same percentage/direction relation incorporates duplicate checker provenance rather than an extra candidate. If confirmed, copying 30.0 could change an extracted descriptive contrast; no demonstrated change in count-based effect, CI/P or paper conclusion. **Writeback:** explicitly preserve 377 and the corroborating count-derived direction.

## C008 — PP day 28 survival difference

**Classification audit:** Numeric or arithmetic inconsistency; REPORT Table 2 within-document proportions/effect; S_W, all S_W; statistical_results; recorded_candidate; suggested retain.

**Evidence and arithmetic:** Main p6 54/995 versus 51/943, printed 0.1 pp; exact RD 0.018864204373 pp→0.0, discrepancy +0.081135795627 pp. Displayed 5.4−5.4 also yields 0.0. Registered point comparison and all recheck fields are complete. Source interval [−10,9.7] is preserved truthfully.

**Assumptions and wording:** Unadjusted estimator and header denominators are conditional; a weighted/adjusted or available-case computation is unprovided. Wide interval alone is not a source-grounded contradiction under an unspecified CI algorithm. This differs from C031's disproven primary input comparison. If confirmed, extraction of this secondary PP point effect could require clarification; no inference or conclusion change is established. **Writeback:** keep estimator/denominator question and distinguish arithmetic from CI diagnostics.

## C009 — ETI airway-difficulty percentage

**Classification audit:** Denominator, proportion, or total inconsistency; REPORT repeated abstract/narrative/Table 3 fraction; S_W, all S_W; statistical_results; recorded_candidate; suggested retain.

**Evidence and arithmetic:** Main pp1,4,6 explicitly 134/996(13.4); 13.453815261044%→13.5, discrepancy −0.053815261044 pp. Safety denominator is explicit and distinct from ITT. Required fields and repeated exact locations are complete.

**Assumptions and wording:** Truncation or staged half-even rounding can produce 13.4; a hypothetical larger denominator would conflict with the printed 996 unless clarified. Same repeated quantity has one ID. If confirmed, difficulty-percentage extraction could need a display convention note; correct count-based RD 4.7 and significance direction are not disproven. **Writeback:** preserve finite precision alternatives without inferring hidden subjects.

## C010 — Centre 9 ETI percentage

**Classification audit:** Denominator, proportion, or total inconsistency; REPORT within results-supplement eTable 1; S_W, all S_W; statistical_results; recorded_candidate; suggested retain. A supplement result cell is REPORT by content.

**Evidence and arithmetic:** Results PDF p2 71(7.0), ETI 1022; 6.947162426614%→6.9, discrepancy +0.052837573386 pp. Complete ETI centre counts sum 1022. Fields/page assignment are complete.

**Assumptions and wording:** Two-stage rounding can reconcile 7.0; an alternative smaller denominator is not printed and must respect the centre-column identity. Not a duplicate of C012's different centre numerator. If confirmed, a centre contribution percentage could require a precision note; no centre-model effect or missing total is established. **Writeback:** retain exact cell and rounding question.

## C011 — Centre 18 BMV percentage

**Classification audit:** Denominator, proportion, or total inconsistency; REPORT eTable 1 within results supplement; S_W, all S_W; statistical_results; recorded_candidate; suggested retain.

**Evidence and arithmetic:** Results p2 29(2.9), BMV 1018; 2.848722986248%→2.8, discrepancy +0.051277013752 pp. Centre counts sum 1018. Fields/source pagination are complete.

**Assumptions and wording:** Staged 2.8487→2.85→2.9 is possible; display rule or other denominator remains unknown. C012 is the other arm's separate fraction, not the same rule/input tuple. If confirmed, a centre contribution percentage could require clarification without changing aggregate membership or any fitted model. **Writeback:** retain the BMV-specific numerator and convention question.

## C012 — Centre 18 ETI percentage

**Classification audit:** Denominator, proportion, or total inconsistency; REPORT eTable 1 within results supplement; S_W, all S_W; statistical_results; recorded_candidate; suggested retain.

**Evidence and arithmetic:** Results p2 24(2.4), ETI 1022; 2.348336594912%→2.3, discrepancy +0.051663405088 pp. Complete centre column sum corroborates 1022. Required fields and exact page are present.

**Assumptions and wording:** Staged 2.3483→2.35→2.4 can reconcile. Shared centre/rounding mechanism with C011 does not duplicate its arm-specific printed input. If confirmed, centre percentage extraction could need a rounding note; no altered trial totals or center-adjustment impact is established. **Writeback:** preserve the ETI-specific comparison and alternatives.

## C013 — Lower-confidence-limit relational wording

**Classification audit:** Statistical reporting inconsistency; REPORT main result versus REPORT main NI decision rule; S_W, all S_W; statistical_results; recorded_candidate; suggested retain. Existing numeric-lane category reconciliation is recorded above; PLAN corroboration adds no P_R.

**Evidence and arithmetic:** Main p4 lower −1.64 and word greater, p3 threshold −1; −1.64−(−1)=−0.64 pp and −1.64<−1. No missing inferential method is needed for ordering. Locations, direct text, rule and recheck fields are complete.

**Assumptions and wording:** Word intent is the human question. The printed failure-to-demonstrate-NI conclusion agrees with the numbers; do not claim reversal of the paper conclusion. Distinct from C024/C030's plan notation. If confirmed, an extractor could copy an inconsistent relational sentence; underlying bound and conclusion remain coherent. **Writeback:** report a wording question while explicitly preserving the coherent conclusion.

## C014 — Pause-count difference labeled seconds

**Classification audit:** Measure, label, or scale inconsistency; REPORT main quantity definition/result/discussion; S_W, all S_W; report_internal_inconsistency; recorded_candidate; suggested retain.

**Evidence and arithmetic:** Main pp3,4,7 define number of pauses >2 seconds, give 27 versus 16 and difference 11 seconds, CI 7–15. 27−16=11 on the named count scale; event qualification duration is not a conversion to seconds. All fields and exact source locations are complete.

**Assumptions and wording:** Aggregation mean/median and intended measured variable are unreported; do not infer a per-patient distribution or call the numerical CI wrong. PLAN duration endpoints describe another quantity and are not a conflicting comparator. If confirmed, a synthesis could copy the wrong unit for the pause effect; no clinical or paper-conclusion impact is demonstrated. **Writeback:** retain quantity/unit/aggregation question and count-duration distinction.

## C015 — Post-hoc denominator conservation

**Classification audit:** Denominator, proportion, or total inconsistency; REPORT main ITT/named count versus REPORT results-supplement regrouped totals; S_C, all S_C; statistical_results; recorded_candidate; suggested retain.

**Evidence and arithmetic:** Main pp4,6 ITT 1018/1022 and n=155; results p3 regrouped 863/1174. 1018−863=155;1174−1022=152;2040→2037. Pure transfer of 155 would give 1177 ETI. Locations and required recheck fields are complete.

**Assumptions and wording:** Main says after exclusion, so pure reassignment is not proven. Three additional exclusions/availability changes could explain total; membership/rule is absent. C028 compares numerator conservation and stays distinct. If confirmed, extracting the post-hoc population could require a combined exclusion/transfer definition; no effect or conclusion error is established. **Writeback:** retain explicit exclusion wording and avoid stating patients were actually lost without a membership definition.

## C016 — Rescue and regrouping set alignment

**Classification audit:** Denominator, proportion, or total inconsistency; REPORT main Figure versus REPORT main post-hoc count, supplement corroboration only; S_W, all S_W; statistical_results; record_input_error; suggested discuss.

**Evidence and arithmetic:** Main p4 rescue 146 under 1014 actual BMV recipients, p6 before-ROSC regrouping 155; results p3 BMV reduction 1018−863=155. Difference 155−146=9 is correct; a subset contradiction is not established. All recheck fields and exact locators are complete.

**Assumptions and wording:** Registered nesting of actual-recipient rescue and ITT regrouping sets is unsupported; timing/procedure definitions and participant members are absent. Reasons 55/100 may overlap. Do not state nine additional eligible rescue subjects are proven. C015's denominator identity uses a different rule. Only if humans establish a common set could downstream extraction of rescue/reassignment counts need reconciliation. **Writeback:** lead the report card with the unsupported alignment and exact membership question, preserving record_input_error/discuss.

## C017 — EMS organizations and investigator-centre rows

**Classification audit:** Cross-document numeric inconsistency; REPORT main versus REPORT results supplement; S_C, all S_C; report_internal_inconsistency; recorded_candidate; suggested retain. Authorized PLAN sites are contextual, not a discrepancy comparator.

**Evidence and arithmetic:** Main p2 reports 20 EMS centres, 15 France/5 Belgium, and p4 refers to eTable 1; results p2 lists 21 distinct contributing codes, including centre 2 with 0 BMV/3 ETI. Column totals 1018/1022 reconcile. Count 21 is not inferred from maximum code 25. All fields/locations are complete.

**Assumptions and wording:** Investigator centre may be an organizational subunit/replacement of an EMS centre; final mapping is absent. C029 is a different plan-body/authorized-roster relationship. If confirmed, extraction of organizational study setting could require mapping; no center-model covariance or outcome-count error is established. **Writeback:** preserve unit-mapping ambiguity and avoid asserting final country split without its full roster evidence.

## C018 — Historical success and difficulty complement

**Classification audit:** Numeric or arithmetic inconsistency; REPORT historical claims inside main discussion; S_W, all S_W; statistical_results; recorded_candidate; suggested retain.

**Evidence and arithmetic:** Main p7 91.8% success <3 attempts followed by thus 9.2% difficulty, with 1941/1272 background counts. 100−91.8=8.2;91.8+9.2=101.0, beyond joint one-decimal tolerance. Exact text, rule and recheck fields are present.

**Assumptions and wording:** Complement identity is conditional on same population/events; difficulty may overlap success or use another denominator. No external historical study truth is claimed. C026 compares another historical result across documents. If confirmed, a secondary source could copy an unexplained historical percentage derivation; no trial outcome or conclusion impact is established. **Writeback:** preserve denominator/event-partition question and conditional complement wording.

## C019 — Planned monthly accrual arithmetic

**Classification audit:** Numeric or arithmetic inconsistency; PLAN original/later summary and recruitment tables; P_P, all P_P; plan_material; recorded_candidate; suggested retain.

**Evidence and arithmetic:** PLAN pp10,24,65,66,79 supply 2000, 20 centres, 24 months, 100/centre, 5/centre/month. 20×100=2000; 5×24=120; 5×24×20=2400; 100/24=4.166666667; 100/5=20 months. No false page or arithmetic defect; fields are complete.

**Assumptions and wording:** Rates are expected inclusions and may be approximate/aspirational, apply to fewer active months, or exceed a minimum final target; simultaneous exact 24-month accrual is conditional. Realized enrolment and sample-size 1912 are different quantities. If confirmed, extraction of operational recruitment assumptions could need clarification; no feasibility, power or trial-conclusion judgment follows. **Writeback:** retain active-month/rate/minimum-target question.

## C020 — IDS construct wording

**Classification audit:** Measure, label, or scale inconsistency; PLAN definition versus PLAN collective purpose sentence; P_P, all P_P; plan_material; recorded_candidate; suggested retain.

**Evidence and logical rule:** PLAN pp24/79 define seven intubation difficulty parameters; pp25/80 include IDS with VAS, mRS, CPC in language describing neurological function at day 28. Literal procedural and neurological constructs differ. All exact locations and recheck fields are present.

**Assumptions and wording:** Collective assessment-program framing may be loose rather than a literal redefinition. No transformed neurological score or observed IDS misuse is supplied. C022 concerns VAS, and C021 a separate IDS operation-timing premise. If confirmed, a data dictionary could copy the wrong IDS construct; no clinical suitability or realized outcome error is inferred. **Writeback:** retain scope-of-sentence question and procedural construct.

## C021 — IDS assessment versus CRF collection

**Classification audit:** Measure, label, or scale inconsistency; PLAN chronology/source-data procedures; P_P, all P_P; plan_material; record_input_error; suggested discuss.

**Evidence and logical rule:** PLAN pp21/76 mark prehospital IDS; pp33/87 say collected directly from CRF at day 28 (+7). Source does not say measured anew at day 28. Same-operation timing identity is unsupported; literal wording and all recheck fields/locators are present.

**Assumptions and wording:** First assessment, entry and record collection are different possible operations. Source-data heading and p87 separated follow-up list support later retrieval as an alternative, without proving that workflow occurred. C023 concerns VAS and remains separately identified. No delayed measurement or resulting bias is established; if clarified, a prospective metadata extractor could record the correct operation/time. **Writeback:** preserve record_input_error/discuss and ask about each operation separately.

## C022 — VAS construct wording

**Classification audit:** Measure, label, or scale inconsistency; PLAN definition versus PLAN collective purpose sentence; P_P, all P_P; plan_material; recorded_candidate; suggested retain.

**Evidence and logical rule:** PLAN pp24/79 define subjective BMV difficulty VAS; pp25/80 include VAS in the statement describing neurological function at day 28. Registered contrast is construct identity. These definition paragraphs do not print a 0–100 range. All fields and exact pages are present; unsupported range wording was removed from the current ledger through the coordinator.

**Assumptions and wording:** Collective programme purpose may preserve a procedural definition; sentence scope remains the human question. C020's IDS uses a different scale definition, and C023 concerns collection operations. If confirmed, extraction of VAS purpose could need clarification; no observed neurological VAS score, conversion or trial-conclusion error is supplied. **Writeback:** use the exact cited procedural construct, omit unsupported range and retain the sentence-scope alternative.

## C023 — VAS assessment versus CRF collection

**Classification audit:** Measure, label, or scale inconsistency; PLAN chronology/source-data procedures; P_P, all P_P; plan_material; record_input_error; suggested discuss.

**Evidence and logical rule:** PLAN pp21/76 mark prehospital VAS; pp33/87 say collected directly from CRF at day 28 (+7). The latter is not explicitly a new VAS assessment. All literal inputs, exact locations, rule-applicability boundary and recheck fields are present.

**Assumptions and wording:** Original assessment/entry/retrieval are not aligned as one event; later record collection can coexist with prehospital assessment. C021 uses IDS, so separate ID is retained despite shared sentence. No late-procedure measurement, outcome bias or estimate impact is established. If clarified, a metadata extractor could copy the correct operation time. **Writeback:** lead with unsupported operation alignment and preserve record_input_error/discuss.

## C024 — SAP alternative threshold sign

**Classification audit:** Statistical reporting inconsistency; PLAN image SAP versus PLAN native SAP and own PLAN decision rule; P_P, all P_P; plan_material; recorded_candidate; suggested retain. Report margin agreement is corroboration only.

**Evidence and arithmetic:** PLAN p130 H1≥0.01 (unsigned positive number, no printed leading plus); p121 H1≥−0.01; p133 lower CI>−0.01, same contrast. 0.01−(−0.01)=0.02 probability units=2 pp; image hypothesis pair leaves −0.01<d<0.01 uncovered. Exact visual recheck fields are complete. Literal-plus shorthand was repaired in current ledger/S074/N354.

**Assumptions and wording:** Missing-minus mechanism versus deliberately stronger alternative and governing representation are unresolved. C030's inclusive negative boundary is a distinct rule/source form. If confirmed, a reader could copy a different planned threshold; no implemented NI test error or changed conclusion is proven. **Writeback:** retain source literal, two-pp difference and sign/representation human question.

## C025 — Impossible-intubation IDS coding

**Classification audit:** Measure, label, or scale inconsistency; PLAN scale/coding tables; P_P, all P_P; plan_material; recorded_candidate; suggested retain.

**Evidence and logical rule:** PLAN pp52/103 display IDS=∞ for impossible intubation and the attained-score-before-abandonment rule, with sum N1–N7. Finite attempt/operator/technique contributions yield a finite attained score; ∞ is distinct. All fields and actual image-table locations are confirmed.

**Assumptions and wording:** Degree-of-difficulty sentinel and stored numeric score may be separate fields; source does not distinguish them. No actual impossible-case score, distribution or test is supplied. Other IDS construct/timing cards compare different statements. If confirmed, a prospective extraction/coding guide could need distinct category/value fields; no corrupted participant record or inference is established. **Writeback:** retain separate-field alternative and stored-score question.

## C026 — Historical PLAN/REPORT TI percentage

**Classification audit:** Cross-document numeric inconsistency; PLAN historical background versus REPORT main background/discussion; P_R, all P_R; protocol_report; recorded_candidate; suggested retain. Concordant PLAN repetitions and concordant REPORT repetitions add no P_P/S_W discrepancy.

**Evidence and arithmetic:** PLAN pp12/67 attribute a 649359-patient Japanese registry, TI 1.0% among 41972, BMV 2.9%; REPORT pp3/7 gives TI 1.1%, p7 the same 649359/BMV 2.9. 1.1−1.0=0.1 pp. Full fields and exact physical source pages are present.

**Assumptions and wording:** Matching has support, but exact TI event count, report subset/horizon, unadjusted/adjusted statistic and rounding are absent. Adjacent labels can arise from different tie conventions; contradiction is conditional on an aligned statistic. No external-study truth or misconduct inference. If confirmed, a copied historical strategy percentage could require alignment metadata; no current trial effect or conclusion impact is established. **Writeback:** preserve alignment limits and the exact underlying-statistic question.

## C027 — Centre identifier/site mapping

**Classification audit:** Measure, label, or scale inconsistency; REPORT main site label versus PLAN roster; P_R, all P_R; protocol_report; recorded_candidate; suggested retain.

**Evidence and logical rule:** REPORT p3 Centre No. 5 Saint Pierre, p4 CPR subset 115=56+59; PLAN p47 Centre 05 Beaujon/Clichy, p49 Centre 17 Saint-Pierre/Brussels. Same identifier/site identity conflicts if the numbering system is shared; 115 itself reconciles. Recheck fields/pages are complete.

**Assumptions and wording:** Final roster/renumbering and separate monitoring-scheme definitions are absent. Original roster cannot prove the final actual site. C017 counts organizations and C029 authorized sites, so neither duplicates this mapping. If confirmed, extraction of the 115-patient subset's setting could need a site-number map; no incorrect CCF measurement, membership or trial conclusion is established. **Writeback:** retain the physical site/numbering-scheme question and coherent 56+59 total.

## C028 — Post-hoc favorable-numerator conservation

**Classification audit:** Numeric or arithmetic inconsistency; REPORT main primary versus REPORT results-supplement regrouping; S_C, all S_C; statistical_results; recorded_candidate; suggested retain.

**Evidence and arithmetic:** Main p4 primary 44/43; results p3 second block 41/45, same day 28 CPC≤2 label. 44+43=87 versus 41+45=86; BMV loses 3 favorable cases, ETI gains 2. All fields/locators are complete.

**Assumptions and wording:** Pure reassignment with unchanged inclusion/outcome is conditional; displayed denominators also fall by 3, so one favorable subject could be excluded or recoded. Missing membership/rule cannot identify who. C015 uses different denominator inputs and a conservation identity and must not merge. If confirmed, post-hoc numerator extraction could require an additional eligibility/outcome rule; no specific favorable outcome change or conclusion impact is proven. **Writeback:** retain the numerator-versus-denominator distinction and exact membership question.

## C029 — Consolidated PLAN body versus amended roster count

**Classification audit:** Cross-document numeric inconsistency; PLAN later protocol body versus PLAN amendment; P_P, all P_P; plan_material; recorded_candidate; suggested retain. Actual enrolling 21 is a different quantity and adds no P_R/S_C.

**Evidence and arithmetic:** PLAN pp65/72 combined V1.4/V2 body 20 centres, 15 France/5 Belgium; p112 amended 20→25, withdraw 1/add 6. 20−1+6=25. Exact full country-split extrapolation is unnecessary; all registered fields/page anchors are present.

**Assumptions and wording:** Amendment detaches the roster to avoid body version changes. Body 20 may be historical/fixed context rather than a current count; effective-date/roster-governance alignment is unprovided. C017 actual report centres is distinct. If confirmed, extraction of current plan participating-centre count could need version/roster framing; no protocol violation, power error or trial conclusion change is established. **Writeback:** retain the detachment explanation and current-versus-historical human question; do not assert an unsupported full country split.

## C030 — Inclusive NI hypotheses and strict decision boundary

**Classification audit:** Statistical reporting inconsistency; PLAN hypotheses versus PLAN strict CI rule in original/later protocol and native SAP; P_P, all P_P; plan_material; recorded_candidate; suggested retain.

**Evidence and logical rule:** PLAN pp36/90/121 H0 d≤−0.01, H1 d≥−0.01; pp37/91/124 lower CI>−0.01, summary p66 corroboration. At d=−0.01 both hypotheses are true, strict decision false. Required fields and truthful source pages are complete; p11 summary is not needed as a visually rechecked authority.

**Assumptions and wording:** Inclusive alternative can be closure/limiting shorthand; intent and implemented boundary handling are unprovided. C024 positive alternative threshold is a separate sign/value identity. If confirmed, copying literal hypothesis notation could need clarification; strict operational rule is consistent and no wrong fitted inference or changed trial conclusion is proven. **Writeback:** retain the notation-intent question and separate it from implementation.

## C031 — Corrected primary arithmetic reconciles

**Classification audit:** Numeric or arithmetic inconsistency for the retained registered comparison; REPORT same-main primary inputs; S_W, all S_W; statistical_results; not_reproduced; suggested exclude. Classification describes the registered relationship despite its disproof.

**Evidence and arithmetic:** Main pp1/4 primary 44/1018 versus 43/1022, difference 0.11; p3 contrast definition. 100×(44/1018−43/1022)=0.114763993710 pp→0.11. Draft 0.118993152607 used secondary 55/54 and cannot be assigned to primary 44/43. Correct inputs explicitly disprove the mismatch; all recheck fields/source pages are complete.

**Assumptions and wording:** No alternative method, truncation or hidden estimator is needed for point reconciliation. Unknown NI P variance is material to other inference questions but cannot sustain this draft. This card records an input mix-up; no unresolved primary effect defect remains. There is no confirmed downstream source-value impact for this comparison; preserving the correction prevents copying the unsupported AI claim. **Writeback:** retain the ID, lead with reconciliation, not_reproduced/exclude and Pending Human Adjudication; no final human judgment.

## Final handoff and bounded limitations

The complete pre-report audit covers all 31 IDs and all assigned source/relationship units. Three current-input precision repairs were completed through the coordinator: C022 unsupported range; C024/S074 unsigned source glyph; N354 unsigned source glyph. Existing C013 category reconciliation is explicitly recorded; no additional classification change is needed. The canonical ledger/recheck ID sets are identical and this artifact returns every ID.

Remaining scientific limitations are named definitions, not omitted review: production rounding/row denominators/estimators; exact test/CI variance/inversion; historical statistic/population/horizon; regrouping membership/outcome exclusions; rescue set identity; final organizational/site-number maps; approximate accrual semantics; detached-roster temporal framing; construct-sentence scope; score-versus-category coding; assessment/CRF collection operations; NI boundary/sign intent. No conclusion change, actual propagation, misconduct or broad methodological disposition is asserted.

The coordinator must mark the audit coverage row COMPLETE, spawn/record the fresh medium report generator, assemble all 31 cards with identical classification values and all required fields, confirm each of 155 human adjudication values is exactly `__`, finalize performance/integrity/tooling records, render standalone HTML and complete validation. Final report/HTML checks are post-audit completion requirements, not claimed results of this pre-report artifact.
